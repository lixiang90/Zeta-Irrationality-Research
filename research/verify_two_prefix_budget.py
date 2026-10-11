"""Independent checks for the generalized CRT, budget, and real formulas."""
import json
import math
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat
import mpmath as mp
from sympy import primerange
from two_prefix_inner import residue_bound,allocation_bound
from two_prefix_outer import vp
from joint_exact import Dcache,entries,moment,determinant_tail_split,content
from two_prefix_budget import (candidate_lines,geometry,linval,local_cells,
                              real_lower,tail_budget,deficit)
from restart_obstruction_certificate import log_iv,outward_decimal


def crt_check(K,N,M,h,p):
    info=residue_bound(K,N,M,h,p);t=fmpq_poly([0,1]);T=Dcache(K)//Dcache(M)
    W=Dcache(N)**6*Dcache(M)**2;denom=Dcache(K);aa,bb=entries(K,[(N,6),(M,2)],h)
    yy=[];poly=W
    for e in range(2*h-1):
        Q=poly//denom
        yy.append(sum((Q[k]*moment(k) for k in range(3*p-4,Q.degree()+1)),fmpq(0)))
        poly*=t
    basis=[];weights=[]
    for row in info['classes']:
        c=row['c'];local=fmpq_poly([1]);big=fmpq_poly([1])
        for j in range(M+1,K+1):
            if j%p in (c,p-c):
                local*=t+j*j
                if j>p:big*=t+j*j
        n=row['big']
        for i in range(row['surviving']):
            basis.append((T//local)*((t+c*c)**i if i<n else big*(t+c*c)**(i-n)))
        weights+=row['twice_weights']
    zero=fmpq_poly([1]);nz=0
    for j in range(M+1,K+1):
        if j%p==0:zero*=t+j*j;nz+=1
    basis +=[(T//zero)*t**i for i in range(nz)]
    basis +=[T*t**i for i in range(h-(K-M))]
    weights+=info['zero_class_weights']+[0]*(h-(K-M))
    assert weights==info['twice_weights']
    C=fmpq_mat(h,h,[b[j] for b in basis for j in range(h)])
    assert vp(C.det(),p)==0
    Y=fmpq_mat(h,h,[yy[i+j] for i in range(h) for j in range(h)])
    assert Y.rank()<=info['moment_rank']
    assert all(not x or vp(x,p)>=-1 for x in Y.entries())
    for values in ([a-y for a,y in zip(aa,yy)],bb):
        A=fmpq_mat(h,h,[values[i+j] for i in range(h) for j in range(h)])
        A=C*A*C.transpose()
        for i in range(h):
            for j in range(h):
                assert not A[i,j] or 2*vp(A[i,j],p)>=weights[i]+weights[j]
    return dict(K=K,N=N,M=M,h=h,p=p,entry_checks=2*h*h,
                base=info['base'],lower=info['lower'],basis_unit=True)


def fraction_mp(f):return mp.mpf(f.numerator)/f.denominator


def main():
    folder=Path(__file__).parent
    jobs=[(48,2,8,40,11),(48,2,8,46,13),(72,3,12,60,13),
          (96,4,16,80,17),(40,4,15,25,11),(56,8,20,36,11),
          (60,2,31,29,13),(60,2,31,29,17),(30,2,13,17,11),
          (15,1,4,11,7),(15,1,4,14,7),(40,2,24,16,11)]
    crt=[crt_check(*job) for job in jobs]
    # New full-polynomial cases include removed multiples of p and both small poles.
    new=[]
    for K,N,M,h in [(30,2,13,17),(40,2,24,16),(56,8,20,36),(60,2,31,29)]:
        aa,bb=entries(K,[(N,6),(M,2)],h);P=determinant_tail_split(aa,bb,K,M,h);ct=content(P)
        checks=[]
        for p in primerange(7,2*(K+6*N)+2):
            if p*p<=2*K:continue
            bound=residue_bound(K,N,M,h,p)['lower']
            if p*p>12*N+4*M+4*h-2*K+4:
                a=allocation_bound(K,N,M,h,p)
                bound=max(bound,a['lower']);k=a['threshold']
                dual=h*k
                for c,b in enumerate(a['offsets']):
                    step=4 if c==0 else 2;n=max(0,(k-b+step-1)//step)
                    dual-=n*(k-b)-step*n*(n-1)//2
                assert dual==a['lower']
            actual=vp(ct,p);assert actual>=bound
            checks.append(dict(p=p,lower=bound,actual=actual))
        new.append(dict(K=K,N=N,M=M,h=h,degree=P.degree(),content=str(ct),checks=checks))
    budget=[]
    for name in ('two_prefix_budget_refined.json','two_prefix_budget_alpha40.json'):
        budget+=json.loads((folder/name).read_text())['rows']
    piece_count=0;density_checks=0;real=[]
    for row in budget:
        a,b=F(row['alpha']),F(row['beta']);lam=1-b
        cuts=geometry(a,b,row['cutoff']);total=F(0)
        for piece in row['pieces']:
            l,r=map(F,piece[:2]);slope,intercept=map(F,piece[3:]);name=piece[2]
            x=(l+r)/2
            cell=next((cl,cr) for cl,cr in zip(cuts,cuts[1:]) if cl<x<cr)
            candidates=candidate_lines(*cell,a,b)
            assert candidates[name]==(slope,intercept)
            assert all(slope*t+intercept<=linval(v,t) for v in candidates.values() for t in (l,r))
            # Cross-check class densities using direct counts at fine rational sample points.
            cells=local_cells(*cell,a,b)
            for k in (-3,0,5,17):
                value=sum(linval(c['length'],x)*deficit(k,c['offset']) for c in cells)
                assert value>=0
                density_checks+=1
            total+=slope*(1/l-1/r)+intercept*(1/l**2-1/r**2)/2;piece_count+=1
        tail,_=tail_budget(a,b,row['cutoff'],row['tail_end']);A=total+tail
        assert outward_decimal(A)==row['A_interval']
        s=F(row['test_s']);B=real_lower(a,b,s)
        assert outward_decimal(A+B)==row['budget_obstruction_interval']
        with mp.workdps(65):
            am,bm,lm,sm=map(fraction_mp,(a,b,lam,s))
            def J(c,t):
                y=mp.sqrt(t)
                return c*mp.log(t+c*c)-2*c+2*y*mp.atan(c/y) if t else 2*c*(mp.log(c)-1)
            def V(t):return 2*mp.pi*mp.sqrt(t)+J(1,t)-6*J(am,t)-2*J(bm,t)
            C=-2*lm+12*am*lm*(1-mp.log(am))+4*bm*lm*(1-mp.log(bm))+3*lm*lm-2*lm*lm*mp.log(2*lm)
            numeric=lm*lm*(mp.log(sm*sm)-mp.mpf('1.5'))-lm*mp.quad(V,[0,sm*sm])/(sm*sm)+C
            assert abs(numeric-fraction_mp((B.lo+B.hi)/2))<mp.mpf('1e-35')
            real.append(dict(alpha=str(a),beta=str(b),independent_numeric=str(numeric)))
    # Actual finite slack: this is NOT an asymptotic extra gain.
    saved=json.loads((folder/'two_prefix_inner_validation.json').read_text())['rows'];slacks=[]
    for K in (24,48,72,96):
        N=K//24
        for multiple in (1,3,4):
            rows=[r for r in saved if (r['K'],r['N'],r['M'],r['h'])==(K,N,multiple*N,K-multiple*N)]
            bands={}
            for name,cond in [('p_le_K3',lambda p:3*p<=K),('K3_to_K2',lambda p:3*p>K and 2*p<=K),('p_gt_K2',lambda p:2*p>K)]:
                rs=[r for r in rows if cond(r['p'])]
                bands[name]=dict(samples=len(rs),max_slack=max((r['slack'] for r in rs),default=0),
                    weighted_slack=sum(r['slack']*math.log(r['p'])/K**2 for r in rs))
            slacks.append(dict(K=K,N=N,M=multiple*N,h=K-multiple*N,bands=bands))
    result=dict(crt_certificates=crt,new_full_polynomials=new,
                envelope_pieces_checked=piece_count,density_sanity_checks=density_checks,
                real_quadrature_cross_checks=real,finite_slacks=slacks)
    (folder/'two_prefix_budget_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(crt_certificates=len(crt),crt_entries=sum(r['entry_checks'] for r in crt),
                         new_full_polynomials=len(new),new_prime_checks=sum(len(r['checks']) for r in new),
                         envelope_pieces_checked=piece_count,real_cross_checks=len(real),finite_slacks=slacks)),flush=True)


if __name__=='__main__':main()
