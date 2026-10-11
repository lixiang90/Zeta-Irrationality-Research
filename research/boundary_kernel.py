"""Inspect the mod-p reductions of genuine deep Smith directions.

Column transformations are tracked; these are lifts from the complete matrix,
not nullspaces of the leading quotient-moment matrix alone.
"""
import json,argparse
from pathlib import Path
from flint import nmod_poly,nmod_mat,fmpq_poly,fmpq_mat
from boundary_structure import matrices
from joint_padic import val,hungarian,residue
from coupled_pencil import vp_mod
from layer_projection import local_basis
from joint_exact import Dcache


def smith_columns(rows,p,precision,transform_precision=1):
    A=[r[:] for r in rows];n=len(A);modulus=p**precision
    V=[[int(i==j) for j in range(n)] for i in range(n)];slopes=[]
    transform_modulus=p**transform_precision
    for k in range(n):
        s,i,j=min((vp_mod(A[i][j],p,precision),i,j) for i in range(k,n) for j in range(k,n))
        assert s<precision
        A[k],A[i]=A[i],A[k]
        for R in (A,V):
            for row in R:row[k],row[j]=row[j],row[k]
        divisor=p**s;localmod=modulus//divisor;inv=pow(A[k][k]//divisor,-1,localmod)
        for i in range(k+1,n):
            assert A[i][k]%divisor==0
            f=(A[i][k]//divisor)*inv%localmod
            for j in range(k+1,n):A[i][j]=(A[i][j]-f*A[k][j])%modulus
            A[i][k]=0
        for j in range(k+1,n):
            assert A[k][j]%divisor==0
            f=(A[k][j]//divisor)*inv%localmod
            assert precision-s>=transform_precision
            for i in range(n):V[i][j]=(V[i][j]-f*V[i][k])%transform_modulus
            A[k][j]=0
        slopes.append(s)
    return slopes,V


def analyze(p,N):
    A,B,tags,_,_=matrices(p,N);h=A.nrows();L=12
    basis,_,_=local_basis(2*p-1,N,p)
    cost=[[min(val(A[i,j],p),val(B[i,j],p)) for j in range(h)] for i in range(h)]
    u,v,T=hungarian(cost)
    M=[[residue(A[i,j],p,u[i]+v[j],L) for j in range(h)] for i in range(h)]
    slopes,V=smith_columns(M,p,L,3)
    product=nmod_mat([[x%(p**3) for x in row] for row in M],p**3)*nmod_mat(V,p**3)
    assert all(int(product[i,j])%p**min(s,3)==0 for j,s in enumerate(slopes) for i in range(h))
    # Our observed column normalization has v_i <= 0. Keep exact scaling.
    assert max(v)<=0
    F=Dcache((p-1)//2);Z=fmpq_poly([0,1])*(F**6//Dcache(N)**4)
    levels=[]
    for level in [1,2,3]:
        polynomials=[]
        for j,s in enumerate(slopes):
            if s<level:continue
            P=sum((basis[i]*(V[i][j]*p**(-v[i])) for i in range(h)),fmpq_poly([]))
            polynomials.append(nmod_poly([int(c)%p for c in P],p))
        predicted=Z//Dcache(N) if level==1 else Z
        z=nmod_poly([int(c)%p for c in predicted],p)
        remainders=[bool(q%z) for q in polynomials]
        rank=nmod_mat(len(polynomials),h,[int(q[k]) for q in polynomials for k in range(h)],p).rank()
        model=[z*nmod_poly([0]*k+[1],p) for k in range(h-z.degree())]
        combined=polynomials+model
        joined=nmod_mat(len(combined),h,[int(q[k]) for q in combined for k in range(h)],p).rank()
        levels.append(dict(level=level,directions=len(polynomials),polynomial_rank=rank,
                           predicted_factor_degree=z.degree(),predicted_dimension=h-z.degree(),
                           all_divisible_by_predicted_factor=not any(remainders),
                           model_contained_in_actual=joined==rank))
    return dict(p=p,N=N,d=3*N-p+1,actual_lifts_verified_mod_p3=True,levels=levels)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='11:4,13:5,17:6,19:7,23:8,29:10,31:11,43:16')
    args=ap.parse_args();rows=[]
    for pair in args.pairs.split(','):
        r=analyze(*map(int,pair.split(':')));rows.append(r);print(json.dumps(r),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
