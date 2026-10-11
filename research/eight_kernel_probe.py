"""Explicit polynomial kernel experiments; finite certificates, not a theorem."""
import json,time
from pathlib import Path
from flint import nmod_mat,fmpq_mat,fmpq_poly
from coupled_pencil import normalized_pencil
from eight_pole_probe import fixed_normalization,fixed_weights
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import residue
from kernel_hensel import field,block,FieldImage,divided,same_rowspace,lift,as_rows


def run(p,N,r):
    K=4*p+r;h=K-N;precision=6;mod=p**precision
    d=normalized_pencil(K,N,p,10)
    aa,bb,tau=fixed_normalization(d,p,precision)
    M=nmod_mat(aa,mod);M0=field(M,p)
    s=[fixed_weights(t) for t in d['tags']];v=[x-x//2 for x in s]
    even=[i for i,x in enumerate(s) if x%2==0]
    odd=[i for i,x in enumerate(s) if x%2]
    out=dict(p=p,N=N,r=r,K=K,h=h,even=len(even),even_rank=block(M,even,even,p).rank(),
             odd=len(odd),odd_rank=block(M,odd,odd,p).rank(),first_nullity=h-M0.rank())
    basis,_,tags=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    t=fmpq_poly([0,1]);F=Dcache((p-1)//2)
    phi=t**3*F**8*Dcache(r)//Dcache(N)**4
    n=h-phi.degree();assert n==3*N+1
    qs=[phi*t**k for k in range(n)]
    co=C.transpose().solve(fmpq_mat(h,n,[q[i] for i in range(h) for q in qs]))
    try:
        Z=nmod_mat(h,n,[residue(co[i,k],p,1-v[i],precision) for i in range(h) for k in range(n)],mod)
    except (ValueError,AssertionError,ZeroDivisionError) as e:
        out['coordinate_error']=str(e);return out
    out.update(model_rank=field(Z,p).rank(),kernel_product_rank=(M0*field(Z,p)).rank())
    if M0*field(Z,p):return out
    I=FieldImage(M0,p);O1=I.quotient(divided(M*Z,p,1))
    E=nmod_mat(N,n,[pow(-j*j,k,p) for j in range(1,N+1) for k in range(n)],p)
    out.update(first_obstruction_rank=O1.rank(),obstruction_equals_DN_evaluations=same_rowspace(O1,E,p))
    if not same_rowspace(O1,E,p):return out
    dn=Dcache(N);J=nmod_mat(n,2*N+1,[int(dn[i-j]) if 0<=i-j<=N else 0 for i in range(n) for j in range(2*N+1)],mod)
    Z2=Z*J;Y=I.solve(-divided(M*Z2,p,1));Q2=Z2+p*lift(Y,mod)
    divided(M*Q2,p,2)
    out.update(second_lifts=2*N+1,second_lifts_verified=True,second_lift_rank=field(Q2,p).rank())
    return out


if __name__=='__main__':
    rows=[];start=time.time()
    for p,N,r in [(17,1,1),(17,2,2),(29,3,4),(31,2,7),(43,4,5)]:
        row=run(p,N,r);rows.append(row)
        print(json.dumps(row)+f' seconds={time.time()-start:.1f}',flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
