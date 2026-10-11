"""Exact entry-by-entry audit of the strengthened class-basis argument."""
import json,time
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat
from joint_exact import entries,Dcache,moment
from joint_outer_strong import delta_bound
from joint_padic import val

def audit(K,N,p):
    h=K-N;aa,bb=entries(K,[(N,8)],h)
    tail=list(range(N+1,K+1));classes={}
    for j in tail:classes.setdefault(min(j%p,(-j)%p),[]).append(j)
    polys=[];weights=[]
    for c,inside in sorted(classes.items()):
        base=fmpq_poly([1]);big=fmpq_poly([1])
        for j in tail:
            if j not in inside:base*=fmpq_poly([j*j,1])
        larger=[j for j in inside if j>p]
        for j in larger:big*=fmpq_poly([j*j,1])
        nb=len(larger)
        ell=sum(min(j%p,(-j)%p)==c for j in range(1,K+1))
        for i in range(len(inside)):
            polys.append(base*(fmpq_poly([c*c,1])**i if i<nb else big*fmpq_poly([c*c,1])**(i-nb)))
            weights.append(-F(2*ell-1,2) if c==0 else
                           min(F(0),i+4*int(c<=N)-F(ell+6,2)) if i<nb else F(0))
    C=fmpq_mat(h,h,[v[j] for v in polys for j in range(h)])
    assert val(C.det(),p)==0
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    W=Dcache(N)**8;D=Dcache(K);bad=[];t=fmpq_poly([0,1]);P=W
    for e in range(2*h-1):
        quotient=P//D
        bad.append(sum((quotient[k]*moment(k) for k in range(3*p-4,quotient.degree()+1)),fmpq(0)))
        P*=t
    Y=fmpq_mat(h,h,[bad[i+j] for i in range(h) for j in range(h)])
    bound,parts=delta_bound(K,N,p)
    assert Y.rank()<=parts['rank']
    assert all(val(Y[i,j],p)>=-1 for i in range(h) for j in range(h))
    A=C*(A-Y)*C.transpose();B=C*B*C.transpose()
    minimum=F(10**6)
    for i in range(h):
        for j in range(h):
            margin=min(val(A[i,j],p),val(B[i,j],p))-weights[i]-weights[j]
            assert margin>=0,(K,N,p,i,j,margin,weights[i],weights[j])
            minimum=min(minimum,margin)
    assert sum(w==0 for w in weights)==parts['zero_weights']
    assert 2*sum(weights)-parts['rank_loss']==bound
    return dict(K=K,N=N,p=p,bound=bound,correction_rank=Y.rank(),rank_bound=parts['rank'],
                minimum_entry_margin=str(minimum),basis_determinant_is_p_unit=True)

if __name__=='__main__':
    rows=[];start=time.time()
    for K,N,p in [(16,2,7),(24,3,11),(32,4,11),(32,4,13),(32,4,19),
                  (40,1,17),(40,3,17),(40,5,17),(40,5,23),(40,5,41),(64,8,23),(64,8,37)]:
        r=audit(K,N,p);rows.append(r);print(json.dumps(r)+f' elapsed={time.time()-start:.1f}',flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
