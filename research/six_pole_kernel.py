"""Explicit polynomial models for the first three six-pole Smith filters.

First-column estimates are backed by the Taylor proof in the accompanying
report. The second/third filter identifications are finite certificates only.
"""
import argparse,json,time
from pathlib import Path
from flint import fmpq_poly,fmpq_mat,nmod_poly,nmod_mat
from layer_projection import local_basis
from joint_exact import Dcache
from coupled_pencil import raw_pencil,vp_mod
from joint_padic import residue
from boundary_kernel import smith_columns


def weights(tags,a):
    u=[];v=[]
    for q in tags:
        c,i=q['c'],q['i']
        if c==0:u.append(-1 if i==0 else 1);v.append(-2 if i==0 else 0)
        elif q['delta']:
            u.append(min(i-(1 if c<=a else 2),1));v.append(min(i-2,0))
        else:u.append(i-7 if i<4 else -1);v.append(i-5 if i<4 else -2)
    return u,v


def matrix(K,N,p,a,delta,precision=10):
    z=raw_pencil(K,N,p,precision+14,harmonic_deformation=delta)
    u,v=weights(z['tags'],a);n=K-N;modulus=p**precision
    def norm(M):
        result=[]
        for i in range(n):
            row=[]
            for j in range(n):
                e=z['shift']+u[i]+v[j];x=int(M[i,j])
                assert e>=0 and x%p**e==0 and z['precision']-e>=precision
                row.append(x//p**e%modulus)
            result.append(row)
        return result
    return norm(z['A']),norm(z['B']),u,v


def analyze(p,N,a,center=1):
    K=3*p-1-a;h=K-N;d=3*N-p+1;L=10
    A,B,u,v=matrix(K,N,p,a,0,L);Ac,_,_,_=matrix(K,N,p,a,center,L)
    A1,_,_,_=matrix(K,N,p,a,1,L)
    assert sum(u)+sum(v)==38*N-21*p+19+2*a
    basis,_,_=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    F=Dcache((p-1)//2);phi1=fmpq_poly([0,0,1])*(F**8//Dcache(N)**5)
    phi2=fmpq_poly([0,0,1])*(F**8//(Dcache(N)**4*Dcache(a)))
    dim=h-phi1.degree();assert dim==N-a+d
    Q=[phi1*fmpq_poly([0]*k+[1]) for k in range(dim)]
    co=C.transpose().solve(fmpq_mat(h,dim,[q[i] for i in range(h) for q in Q]))
    Z=nmod_mat([[residue(co[i,k],p,-v[i]) for k in range(dim)] for i in range(h)],p)
    assert Z.rank()==dim
    for M in [A,A1,B]:assert not nmod_mat([[x%p for x in row] for row in M],p)*Z
    slopes,V=smith_columns(Ac,p,L,3)
    product=nmod_mat([[x%(p**3) for x in row] for row in Ac],p**3)*nmod_mat(V,p**3)
    assert all(int(product[i,j])%p**min(s,3)==0 for j,s in enumerate(slopes) for i in range(h))
    bmin=min(vp_mod(x,p,L) for row in B for x in row)
    levels=[]
    for level in [1,2,3]:
        polys=[]
        for j,s in enumerate(slopes):
            if s<level:continue
            P=sum((basis[i]*(V[i][j]*p**(-v[i])) for i in range(h)),fmpq_poly([]))
            polys.append(nmod_poly([int(c)%p for c in P],p))
        factor=phi1 if level==1 else phi2
        ff=nmod_poly([int(c)%p for c in factor],p)
        if level<3:
            model=[ff*nmod_poly([0]*k+[1],p) for k in range(h-ff.degree())]
        elif a<=d:
            da=nmod_poly([int(c)%p for c in Dcache(a)],p)
            model=[ff*da*nmod_poly([0]*k+[1],p) for k in range(d-a)]
        else:model=[ff*nmod_poly([0]*k+[1],p) for k in range(min(d,a-d))]
        def rank(ps):
            return nmod_mat(len(ps),h,[int(q[k]) for q in ps for k in range(h)],p).rank() if ps else 0
        rank_actual=rank(polys);rank_model=rank(model)
        levels.append(dict(level=level,smith_directions=len(polys),image_rank=rank_actual,
                           model_dimension=rank_model,model_contained=rank(polys+model)==rank_actual,
                           spaces_equal=rank_actual==rank_model==rank(polys+model)))
    return dict(p=p,N=N,a=a,K=K,d=d,center=center,first_kernel_dimension=dim,
                first_kernel_all_delta_X=True,finite_whole_matrix_integral=True,
                actual_lifts_verified_mod_p3=True,B_min=bmin,
                tropical=sum(u)+sum(v),smith_sum=sum(slopes),levels=levels)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--triples',default='11:4:0,11:4:1,11:4:2,11:4:3,11:4:4,13:5:0,13:5:1,13:5:2,13:5:3,13:5:4,13:5:5,17:6:0,17:6:1,17:6:2,17:6:3,17:6:4,17:6:5,17:6:6,43:16:0,43:16:3,43:16:7,43:16:13,53:18:0,53:18:1,53:18:3,53:18:5,83:31:0,83:31:5,83:31:12,83:31:23')
    ap.add_argument('--center',type=int,default=1);ap.add_argument('--out',default='six_pole_kernel.json')
    args=ap.parse_args();rows=[];start=time.time()
    for item in args.triples.split(','):
        r=analyze(*map(int,item.split(':')),center=args.center);rows.append(r)
        Path(__file__).with_name(args.out).write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps(r)+f' time={time.time()-start:.1f}',flush=True)
