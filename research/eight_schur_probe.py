"""Local Schur block diagnostics for the eight/nine-pole window."""
import json,time,argparse
from pathlib import Path
from flint import nmod_mat,nmod_poly
from coupled_pencil import normalized_pencil
from eight_pole_probe import fixed_normalization,fixed_weights
from kernel_hensel import field,block,divided,as_rows,lift
from second_pairing import unit_inverse
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import residue
from eight_local_scalar import rational_model


def run(p,N,r):
    K=4*p+r;h=K-N;prec=6;mod=p**prec
    d=normalized_pencil(K,N,p,10);aa,bb,tau=fixed_normalization(d,p,prec)
    assert all(x%(p*p)==0 for row in bb for x in row)
    M=nmod_mat(aa,mod);tags=d['tags'];s=[fixed_weights(t) for t in tags]
    R=[i for i,t in enumerate(tags) if (t['c']==0 and t['i']==3) or (t['delta'] and t['i']>=5)]
    S=[i for i in range(h) if i not in R]
    U=block(M,S,S,mod);U0=field(U,p)
    offclass=[(i,j) for i in S for j in S if tags[i]['c']!=tags[j]['c'] and int(M[i,j])%p]
    blocks=[]
    for c in sorted({tags[i]['c'] for i in S}):
        ii=[i for i in S if tags[i]['c']==c]
        blocks.append(dict(c=c,size=len(ii),rank=block(M,ii,ii,p).rank()))
    row=dict(p=p,N=N,r=r,K=K,core=len(R),eliminated=len(S),unit_rank=U0.rank(),
             unit_offclass_nonzero=len(offclass),blocks=blocks,X_coefficients_divisible_by_p2=True)
    if U0.rank()!=len(S):return row
    V=unit_inverse(U,p,prec)
    A=block(M,R,R,mod)-block(M,R,S,mod)*V*block(M,S,R,mod)
    assert A==A.transpose()
    A1=divided(A,p,1)
    row.update(symmetric=True,core_divisible_by_p=True,first_pairing_rank=A1.rank(),
               first_pairing=as_rows(A1),core_tags=[tags[i] for i in R])
    # Is this first pairing a sum of N independent evaluation functionals
    # supported on the three coordinates associated with each inner class?
    row['pairing_offclass_nonzero']=sum(bool(A1[i,j]) for i in range(len(R)) for j in range(len(R))
        if tags[R[i]]['c']!=tags[R[j]]['c'])
    row['pairing_blocks']=[dict(c=c,indices=[i for i,k in enumerate(R) if tags[k]['c']==c],
        rank=block(A1,[i for i,k in enumerate(R) if tags[k]['c']==c],
                         [i for i,k in enumerate(R) if tags[k]['c']==c],p).rank()) for c in range(N+1)]
    basis,_,_=local_basis(K,N,p);n=len(R);t=nmod_poly([0,1],p)
    F=nmod_poly([int(x)%p for x in Dcache((p-1)//2)],p)
    dn=nmod_poly([int(x)%p for x in Dcache(N)],p)
    dr=nmod_poly([int(x)%p for x in Dcache(r)],p)
    phi=t**3*F**8*dr//dn**4
    polys=[]
    for i in R:
        quotient,rem=divmod(nmod_poly([int(x)%p for x in basis[i]],p),phi)
        assert not rem;polys.append(quotient)
    C=nmod_mat(n,n,[int(f[j]) for f in polys for j in range(n)],p)
    assert C.rank()==n
    Av=C.inv()*A1*C.inv().transpose()
    ell=[int((dr*t**k%(F**2))[p-2]) for k in range(2*n-1)]
    L=nmod_mat(n,n,[ell[i+j] for i in range(n) for j in range(n)],p)
    J=nmod_mat(n,2*N+1,[int(dn[i-j]) if 0<=i-j<=N else 0 for i in range(n) for j in range(2*N+1)],p)
    AJ,LJ=Av*J,L*J
    predicted_scalar=residue(rational_model()[0],p,0)
    assert AJ==predicted_scalar*LJ
    row['independent_rational_scalar_verified']=True
    positions=[(i,j) for i in range(n) for j in range(2*N+1) if LJ[i,j]]
    if positions:
        i,j=positions[0];scalar=int(AJ[i,j])*pow(int(LJ[i,j]),-1,p)%p
        fits=AJ==scalar*LJ
        remainder=Av-scalar*L
        assert scalar==predicted_scalar
        row.update(laurent_scalar=scalar,laurent_model_fits=fits,laurent_rank=L.rank(),
                   local_remainder_rank=remainder.rank(),local_remainder_kills_DN=not remainder*J)
    else:
        remainder=Av
        row.update(laurent_scalar=None,laurent_model_fits=not AJ,laurent_rank=L.rank(),
                   local_remainder_rank=Av.rank(),local_remainder_kills_DN=not AJ)
    row['expected_overflow']=min(2*N+1,max(0,6*N+r-p+3))
    E=nmod_mat(N,n,[pow(-c*c,k,p) for c in range(1,N+1) for k in range(n)],p)
    E0=block(E,range(N),range(N),p)
    W=E0.inv().transpose()*block(remainder,range(N),range(N),p)*E0.inv()
    row['remainder_equals_evaluation_form']=remainder==E.transpose()*W*E
    row['evaluation_weights_diagonal']=all(not W[i,j] for i in range(N) for j in range(N) if i!=j)
    assert row['laurent_model_fits'] and row['remainder_equals_evaluation_form'] and row['evaluation_weights_diagonal']
    n2=2*N+1-row['expected_overflow']
    if n2:
        JR=block(J,range(n),range(n2),p)
        ZR=lift(C.inv().transpose()*JR,mod)
        ZS=-V*block(M,S,R,mod)*ZR
        Z=nmod_mat(h,n2,[0]*(h*n2),mod)
        for ii,zz in [(R,ZR),(S,ZS)]:
            for k,i in enumerate(ii):
                for j in range(n2):Z[i,j]=zz[k,j]
        divided(M*Z,p,2)
        assert field(Z,p).rank()==n2
    row.update(second_model_lifts=n2,second_lifts_verified=True,
               first_model_lifts=n,model_bound=59*N-7*K+23-row['expected_overflow'])
    return row


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--extra',action='store_true');args=ap.parse_args()
    out=Path(__file__).with_suffix('.json')
    rows=json.loads(out.read_text()) if args.extra else [];start=time.time()
    jobs=[(p,p//8,(p-1)//2) for p in [53,59,61,67]] if args.extra else [(11,1,1),(13,1,1),(17,1,1),(17,2,2),(29,3,4),(31,2,7),(43,4,5),(47,4,5),
                  (29,3,8),(29,3,9),(29,3,11),(29,3,14),(29,4,4),(31,4,4),(31,4,5),(31,4,11),(31,4,15),
                  (37,4,12),(37,4,14),(37,4,18),(41,4,20),(47,5,23)]
    for p,N,r in jobs:
        row=run(p,N,r);rows.append(row)
        print(json.dumps({k:v for k,v in row.items() if k not in ['blocks','first_pairing','core_tags']})+f' seconds={time.time()-start:.1f}',flush=True)
        out.write_text(json.dumps(rows,indent=2))
