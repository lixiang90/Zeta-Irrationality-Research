"""The full lattice of polynomials integer-valued at negative integer squares.

Continuous trace minimization selects a center. Integer LLL/Babai rounding
selects candidates; only exact content and Arb evaluations certify outcomes.
"""
import argparse,json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,fmpz_mat,arb,ctx
import mpmath as mp
from joint_exact import Dcache,entries_from_polynomial,content
from rational_square_nodes import experiment,entries_nodes,node_list,product


def basis(i):
    return fmpq_poly([1]) if i==0 else fmpq_poly([0,2*(-1)**i])*Dcache(i-1)/math.factorial(2*i)


def coordinates(P):
    n=P.degree();a=[]
    for i in range(n+1):
        v=P(-i*i)-sum((a[j]*basis(j)(-i*i) for j in range(i)),fmpq(0));a.append(v)
    assert sum((basis(i)*a[i] for i in range(n+1)),fmpq_poly([]))==P
    return a


def lattice_index(N,L):
    P0=Dcache(N+L)//Dcache(N);cols=[];fac=math.factorial(L)**2
    for s in range(1,L+1):
        P=Dcache(N+s+L)//Dcache(N+s)
        c=coordinates(fmpq_poly(P-P0)/fac);c += [fmpq(0)]*(L-len(c))
        assert all(x.q==1 for x in c);cols.append(c)
    matrix=fmpz_mat(L,L,[int(v) for col in cols for v in col]);det=abs(int(matrix.det()));assert det
    return dict(N=N,L=L,index=str(det),log_index=float(mp.log(det)),matrix=[[int(v) for v in col] for col in cols])


def mval(x):return mp.mpf(int(x.p))/int(x.q)


def trace_metric(K,N,L,kind='integer'):
    h=K-N-L;nodes=node_list(K,kind)
    # The affine lattice is anchored at an INTEGER block even when denominator
    # nodes are changed. This keeps Q(-x^2)/(L!)^2 integer-valued.
    P0=fmpq_poly(Dcache(N+L)//Dcache(N));fac=math.factorial(L)**2
    directions=[basis(i)*fac for i in range(L)]
    aa,bb,T=entries_nodes(nodes,product(nodes[:N])**8,K-N)
    bits=max(max(abs(int(x.p)).bit_length(),int(x.q).bit_length()) for x in aa+bb)
    mp.mp.dps=max(100,int(bits*.30103)+100)
    z=mp.zeta(7);mom=[mval(a)+mval(b)*z for a,b in zip(aa,bb)]
    def weighted_mom(P):return [sum(mval(c)*mom[e+i] for i,c in enumerate(P)) for e in range(2*h-1)]
    vv=weighted_mom(P0**2)
    H=mp.matrix([[vv[i+j] for j in range(h)] for i in range(h)])
    inv=H**-1;kernel=[mp.mpf(0)]*(2*h-1)
    for i in range(h):
        for j in range(h):kernel[i+j]+=inv[i,j]
    t=[sum(kernel[e]*mom[e+k] for e in range(2*h-1)) for k in range(2*L+1)]
    inner=lambda A,B:sum(mval(c)*t[i] for i,c in enumerate(A*B))
    A=mp.matrix([[inner(a,b) for b in directions] for a in directions]);b=mp.matrix([inner(P0,a) for a in directions])
    center=mp.lu_solve(A,-b);minimum=mp.mpf(h)+(b.T*center)[0]
    assert minimum>0 and minimum<h
    return P0,directions,A,b,center,minimum


def reduced_round(A,center):
    L=A.rows;chol=mp.cholesky(A);largest=max(abs(v) for v in chol)
    scale=mp.mpf(2)**384/largest
    approx=fmpz_mat(L,L,[int(mp.nint(chol[i,j]*scale)) for i in range(L) for j in range(L)])
    assert approx.det()!=0
    red,T=approx.lll(transform=True);assert abs(int(T.det()))==1 and T*approx==red
    tm=mp.matrix([[int(T[i,j]) for j in range(L)] for i in range(L)])
    G=tm*A*tm.T;target=tm*A*center
    # Gram-Schmidt in the reduced row basis, with exact integer transform T.
    mu=mp.matrix(L);norm=[];star=[]
    for i in range(L):
        s=mp.matrix([int(j==i) for j in range(L)])
        for j in range(i):
            mu[i,j]=sum(G[i,k]*star[j][k] for k in range(L))/norm[j]
            s-=mu[i,j]*star[j]
        star.append(s);norm.append((s.T*G*s)[0]);assert norm[-1]>0
    nearest=[0]*L
    for j in reversed(range(L)):
        numerator=sum(star[j][k]*target[k] for k in range(L))
        numerator-=sum(nearest[i]*mu[i,j]*norm[j] for i in range(j+1,L))
        nearest[j]=int(mp.nint(numerator/norm[j]))
    u=[sum(nearest[i]*int(T[i,j]) for i in range(L)) for j in range(L)]
    return u,[[int(T[i,j]) for j in range(L)] for i in range(L)],norm


def run(K,N,L,kind='integer',neighbors=False):
    P0,ds,A,b,center,minimum=trace_metric(K,N,L,kind);h=K-N-L
    u,T,norm=reduced_round(A,center);naive=[int(mp.nint(x)) for x in center]
    candidates=[('prefix' if kind=='integer' else 'integer_block_anchor',[0]*L),('naive',naive),('lll',u)]
    if neighbors:
        for j,v in enumerate(T):
            for sign in (-1,1):candidates.append((f'lll_neighbor_{j}_{sign}',[x+sign*y for x,y in zip(u,v)]))
    rows=[];seen=set()
    path=Path(__file__).with_name(f'growing_integer_space_K{K}_L{L}_{kind}.json')
    info=dict(K=K,N=N,L=L,kind=kind,dimension=L,continuous_trace_minimum=mp.nstr(minimum,35),
              continuous_trace_gain_bound=mp.nstr(h*mp.log(minimum/h)/K**2,35),
              center=[mp.nstr(x,45) for x in center],lll_transform=T,
              orthogonal_norms=[mp.nstr(x,25) for x in norm],precision_digits=mp.mp.dps,
              translated_block_lattice=lattice_index(N,L),rows=rows)
    for label,ui in candidates:
        if tuple(ui) in seen:continue
        seen.add(tuple(ui));Q=P0+sum((d*v for d,v in zip(ds,ui)),fmpq_poly([]))
        assert Q[L]==1
        cc=coordinates(Q/math.factorial(L)**2);assert all(x.q==1 for x in cc)
        r=experiment(K,N,N+L,kind,Q,label);r['parameters']=[str(x) for x in ui]
        vec=mp.matrix(ui);trace=mp.mpf(h)+2*(b.T*vec)[0]+(vec.T*A*vec)[0]
        assert trace>0;r['trace_relative']=mp.nstr(trace,30)
        r['trace_gain_bound']=mp.nstr(h*mp.log(trace/h)/K**2,30)
        rows.append(r);path.write_text(json.dumps(info,indent=2),encoding='utf-8')
        print(json.dumps({k:r[k] for k in ('K','label','score','real','arithmetic_gain','trace_gain_bound')}),flush=True)
    return info


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1)
    p.add_argument('--L',type=int,default=3);p.add_argument('--kind',default='integer');p.add_argument('--neighbors',action='store_true')
    a=p.parse_args();run(a.K,a.N,a.L,a.kind,a.neighbors)
