"""Compute p*mu modulo p^r using only Bernoulli numbers up to index r.

The exact localization formula truncates after k=r: every omitted term has
p-valuation >=r. This avoids large-index Bernoulli arithmetic for higher
layers. Correction-matrix Smith data are not determinant-content bounds.
"""
import json,time,math
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq,nmod_mat,fmpz_mat
from joint_exact import Dcache,moment
from joint_padic import residue
from b8_hankel import vp as integer_valuation
from layer_projection import local_basis,local_data

def moments_mod(p,count,precision):
    assert p>=7 and precision>=1
    modulus=p**precision;maxpower=2*count+2
    sums=[0]*(maxpower+1)
    for c in range(1,(p+1)//2):
        power=1
        for n in range(maxpower+1):
            sums[n]=(sums[n]+2*power)%modulus;power=power*c%modulus
    sums[0]=(sums[0]+1)%modulus  # the origin contribution
    coefficients=[]
    for k in range(precision+1):
        q=fmpq.bernoulli(k)*fmpq(math.prod(range(k+1,k+6)),720)*p**k
        coefficients.append(residue(q,p,0,precision))
    out=[]
    for e in range(count):
        value=sum(coefficients[k]*math.comb(2*e+7,k+5)*sums[2*e+2-k]
                  for k in range(min(precision,2*e+2)+1))
        out.append((-1)**e*value%modulus)
    return out

def correction_gram(K,N,p,precision):
    h=K-N;modulus=p**precision;maxdegree=8*N+2*h-2-K
    values=moments_mod(p,max(0,maxdegree+1),precision)
    W=Dcache(N)**8;D=Dcache(K);ys=[]
    from flint import fmpz_poly
    t=fmpz_poly([0,1]);P=W
    for e in range(2*h-1):
        Q=P//D
        ys.append(sum(int(Q[k])*values[k] for k in range(3*p-4,Q.degree()+1))%modulus)
        P*=t
    basis,weights,tags=local_basis(K,N,p)
    C=nmod_mat(h,h,[int(P[j])%modulus for P in basis for j in range(h)],modulus)
    Y=nmod_mat(h,h,[ys[i+j] for i in range(h) for j in range(h)],modulus)
    return C*Y*C.transpose(),weights,tags

def smith_mod(matrix,p,precision):
    """Rectangular Smith valuations, censored when >= precision."""
    A=[row[:] for row in matrix];n=len(A);m=len(A[0]) if n else 0
    modulus=p**precision;shift=0;out=[];row_order=list(range(n))
    def vp(a):
        if not a:return precision-shift
        v=0
        while a%p==0:a//=p;v+=1
        return v
    for k in range(min(n,m)):
        v,i,j=min((vp(A[i][j]),i,j) for i in range(k,n) for j in range(k,m))
        if shift+v>=precision:
            return out, min(n,m)-len(out), row_order[:len(out)]
        if v:
            divisor=p**v;modulus//=divisor;shift+=v
            for a in range(k,n):
                for b in range(k,m):
                    assert A[a][b]%divisor==0
                    A[a][b]//=divisor
        A[k],A[i]=A[i],A[k]
        row_order[k],row_order[i]=row_order[i],row_order[k]
        for row in A:row[k],row[j]=row[j],row[k]
        inverse=pow(A[k][k],-1,modulus)
        for a in range(k+1,n):
            factor=A[a][k]*inverse%modulus
            if factor:
                for b in range(k+1,m):A[a][b]=(A[a][b]-factor*A[k][b])%modulus
            A[a][k]=0
        out.append(shift)
    return out,0,row_order[:len(out)]

if __name__=='__main__':
    start=time.time();count=0
    for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
        for precision in [1,2,3,4,6,8]:
            values=moments_mod(p,6*p,precision)
            assert all(x==residue(moment(e),p,-1,precision) for e,x in enumerate(values))
            count+=len(values)
    full=[]
    for K,N,p in [(32,4,11),(48,6,17),(64,8,23),(40,1,11)]:
        M,w,_=correction_gram(K,N,p,6);_,_,Y,_,_=local_data(K,N,p)
        assert all(M[i,j]==residue(Y[i,j],p,-1,6) for i in range(K-N) for j in range(K-N))
        full.append(dict(K=K,N=N,p=p,entries=(K-N)**2,precision=6))
    scaled=[]
    for K,N,p in [(128,16,43),(256,32,89),(400,50,137)]:
        t=time.time();M,w,_=correction_gram(K,N,p,6)
        Z=[i for i,v in enumerate(w) if v==0];H=[i for i,v in enumerate(w) if v==-F(1,2)]
        rectangle=[[int(M[i,j]) for j in Z] for i in Z+H]
        slopes,censored,pivot_rows=smith_mod(rectangle,p,6)
        assert not censored and len(slopes)==len(Z)
        minor=fmpz_mat(len(Z),len(Z),[v for i in pivot_rows for v in rectangle[i]])
        minor_valuation=integer_valuation(minor.det(),p)
        assert minor_valuation==sum(slopes)
        rank_mod_p=nmod_mat(len(rectangle),len(Z),[v%p for row in rectangle for v in row],p).rank()
        assert rank_mod_p==slopes.count(0)
        multiplicities={str(v):slopes.count(v) for v in sorted(set(slopes))}
        row=dict(K=K,N=N,p=p,rows=len(Z+H),columns=len(Z),
                 smith_multiplicities=multiplicities,at_least_six=censored,
                 independent_minor_valuation=minor_valuation,rank_mod_p=rank_mod_p,
                 seconds=time.time()-t)
        scaled.append(row);print(json.dumps(row),flush=True)
    result=dict(moment_checks=count,matrix_checks=full,
                matrix_entries_checked=sum(r['entries'] for r in full),scaled=scaled,
                seconds=time.time()-start,
                scope='Smith layers of the rectangular pY correction projection only; not of A+XB or its determinant')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['scaled','matrix_checks']}),flush=True)
