"""Audit a two-sided kernel construction without assuming the full cokernel.

Finite certificates complement the uniform argument in two_sided_analysis.md.
All matrix arithmetic uses exact rationals or residue rings, never floats.
"""
import argparse
import json
import time
from pathlib import Path
from math import gcd
from functools import reduce
import sympy as sp
from flint import fmpq_poly, fmpq_mat, nmod_mat
from six_pole_kernel import matrix
from layer_projection import local_basis
from joint_exact import Dcache
from joint_padic import residue
from kernel_hensel import field, block, divided, as_rows


def symbolic():
    H = sp.Symbol('H')
    nodes = [0, 1, -1, -2, 2, 3]
    den = {z: sp.prod(z-y for y in nodes if y != z) for z in nodes}
    weights = {-1: 1, 2: 1, -2: H, 3: H}
    def S(k): return sum(sp.Rational(z**k, den[z]) for z in nodes)
    def C(k): return sum(w*sp.Rational(z**k, den[z]) for z,w in weights.items())
    moments = [sp.factor(C(8+s)+S(s+2)/6+S(s+1)/2+7*S(s)/12) for s in range(7)]
    U = sp.Matrix(3,3,lambda i,j:moments[i+j])
    det = sp.factor(U.det())
    numerator = sp.Poly(sp.fraction(det)[0],H)
    assert reduce(gcd, [int(c) for c in numerator.all_coeffs()]) == 1
    V = sp.Matrix(4,4,lambda i,j:moments[i+j])
    outer = sp.Matrix(4,4,lambda i,j:C(i+j))
    det4=sp.factor(V.det())
    numerator4=sp.Poly(sp.fraction(det4)[0],H)
    assert reduce(gcd,[int(c) for c in numerator4.all_coeffs()])==1
    original4=sp.factor(det4.subs(H,sp.Rational(129,128)))
    return H, moments, dict(inner_moments=[str(x) for x in moments],
        inner_determinant=str(det), outer_determinant=str(sp.factor(outer.det())),
        inner_determinant_content=1,
        extended_inner_determinant=str(det4),extended_determinant_content=1,
        original_extended_determinant=str(original4),
        original_extended_numerator_factors={str(k):v for k,v in sp.factorint(sp.numer(original4)).items()},
        pairing_schur_scalar=str(sp.factor(V.det()/det)))


def run(p,N,a,center=1,example=False):
    assert sp.isprime(p) and p>=11 and (p+2)//3<=N<=3*p//8 and 0<=a<=N
    K=3*p-1-a; h=K-N; d=3*N-p+1; n1=N-a+d
    precision=6; mod=p**precision
    assert mod<2**64
    rows,_,u,v=matrix(K,N,p,a,center,precision)
    M=nmod_mat(rows,mod); M0=field(M,p)
    basis,_,tags=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    phi=fmpq_poly([0,0,1])*(Dcache((p-1)//2)**8//Dcache(N)**5)
    qs=[phi*fmpq_poly([0]*k+[1]) for k in range(n1)]
    co=C.transpose().solve(fmpq_mat(h,n1,[q[i] for i in range(h) for q in qs]))
    Z=nmod_mat(h,n1,[residue(co[i,k],p,-v[i],precision) for i in range(h) for k in range(n1)],mod)
    Z0=field(Z,p)
    assert Z0.rank()==n1 and not M0*Z0
    F1=divided(M*Z,p,1)
    Lraw=nmod_mat(h,n1,[residue(co[i,k],p,1-u[i]) for i in range(h) for k in range(n1)],p)
    S=[i for i,t in enumerate(tags) if (t['c']>N and t['i']<4) or (a<t['c']<=N and t['i']<3)]
    Sc=[i for i in range(h) if i not in S]
    T=[i for i,t in enumerate(tags) if 0<t['c']<=N and t['i']>=3]
    assert block(Z0,T,range(n1),p).rank()==n1
    assert block(Lraw,T,range(n1),p)==block(Z0,T,range(n1),p)
    assert not block(M0,S,Sc,p)
    U=block(M0,S,S,p)
    assert all(not M0[i,j] for i in S for j in S if tags[i]['c']!=tags[j]['c'])
    residual=M0.transpose()*Lraw
    assert not block(residual,Sc,range(n1),p)
    # Compare every complete inner block with the universal Hankel formula,
    # allowing its common local unit and (2c)^(i+j) diagonal factors.
    H,moments,_=symbolic()
    hv=(129*pow(128,-1,p)+center)%p
    ms=[int(sp.numer(x.subs(H,hv)))%p*pow(int(sp.denom(x.subs(H,hv))),-1,p)%p for x in moments]
    local_units=[]
    for c in range(a+1,N+1):
        ii=[i for i in S if tags[i]['c']==c]
        assert len(ii)==3
        expected=[[ms[r+s]*pow(2*c,r+s,p)%p for s in range(3)] for r in range(3)]
        pivot=next(((r,s) for r in range(3) for s in range(3) if expected[r][s]),None)
        assert pivot is not None
        r,s=pivot; unit=int(M0[ii[r],ii[s]])*pow(expected[r][s],-1,p)%p
        assert unit!=0
        assert all(int(M0[ii[r],ii[s]])==unit*expected[r][s]%p for r in range(3) for s in range(3)), ('inner model mismatch',p,N,a,c,as_rows(block(M0,ii,ii,p)),expected)
        local_units.append(unit)
    nodes=[0,1,-1,-2,2,3]
    harmonic={-1:1,2:1,-2:hv,3:hv}
    cm=[sum(w*pow(z,k,p)*pow(int(sp.prod(z-y for y in nodes if y!=z)),-1,p) for z,w in harmonic.items())%p for k in range(7)]
    for c in range(N+1,(p-1)//2+1):
        ii=[i for i in S if tags[i]['c']==c]
        expected=[[cm[r+s]*pow(2*c,r+s,p)%p for s in range(4)] for r in range(4)]
        r,s=next((r,s) for r in range(4) for s in range(4) if expected[r][s])
        unit=int(M0[ii[r],ii[s]])*pow(expected[r][s],-1,p)%p
        assert unit and all(int(M0[ii[r],ii[s]])==unit*expected[r][s]%p for r in range(4) for s in range(4))
    outside_support=[i for i in range(h) if i not in S and i not in T]
    assert not block(Lraw,outside_support,range(n1),p)
    outside_complete=[i for i in S+T if not a<tags[i]['c']<=N]
    assert not block(F1,outside_complete,range(n1),p)
    assert all(int(F1[i,k])==int(F1[i,0])*pow(-tags[i]['c']**2,k,p)%p for i in S+T for k in range(n1))
    result=dict(p=p,N=N,a=a,center=center,h=h,d=d,n1=n1,
        S_size=len(S),S_rank=U.rank(),actual_nullity=h-M0.rank(),
        supported_left_residual=True,primitive_high_coordinates=True,
        inner_universal_blocks=True,outer_universal_blocks=True,
        left_support_and_evaluation_factorization=True)
    if U.rank()!=len(S):
        result['status']='singular specialization; Gauss construction uses the parameter field'
        return result
    correction=U.transpose().inv()*block(residual,S,range(n1),p)
    L=nmod_mat(as_rows(Lraw),p)
    for r,i in enumerate(S):
        for k in range(n1): L[i,k]-=correction[r,k]
    assert L.rank()==n1 and not L.transpose()*M0
    pairing=L.transpose()*F1
    E=nmod_mat(N-a,n1,[pow(-c*c,k,p) for c in range(a+1,N+1) for k in range(n1)],p)
    # The multiplier D_N/D_a spans the kernel of evaluation.
    J=Dcache(N)//Dcache(a)
    mult=nmod_mat(n1,d,[int(J[i-j]) if 0<=i-j<len(J) else 0 for i in range(n1) for j in range(d)],p)
    assert not E*mult and mult.rank()==d
    assert not (Lraw.transpose()*F1)*mult
    assert not pairing*mult
    assert pairing==pairing.transpose()
    assert pairing.rank()<=N-a
    hankel=nmod_mat(3,3,[ms[i+j] for i in range(3) for j in range(3)],p)
    vv=nmod_mat(3,1,ms[3:6],p)
    if N>a:
        sigma=(ms[6]-int((vv.transpose()*hankel.inv()*vv)[0,0]))%p
        scalars=[]
        for c,unit in zip(range(a+1,N+1),local_units):
            index=next(i for i,t in enumerate(tags) if t['c']==c and t['i']==3)
            ac=int(Lraw[index,0]); assert ac
            scalars.append(ac*ac*unit*pow(2*c,6,p)%p)
        weights=nmod_mat(N-a,N-a,[scalars[i]*sigma%p if i==j else 0 for i in range(N-a) for j in range(N-a)],p)
        raw_weights=nmod_mat(N-a,N-a,[scalars[i]*ms[6]%p if i==j else 0 for i in range(N-a) for j in range(N-a)],p)
        assert Lraw.transpose()*F1==E.transpose()*raw_weights*E
        assert pairing==E.transpose()*weights*E
    else:sigma=None
    result.update(status='certified',pairing_rank=pairing.rank(),
        rank_upper_bound=N-a,new_determinant_bound=sum(u)+sum(v)+n1+d,
        raw_pairing_factors_through_evaluation=True,
        corrected_pairing_factors_through_evaluation=True,
        universal_pairing_scalar_verified=True,pairing_scalar=sigma,
        left_kernel_verified=True,right_kernel_verified=True)
    if example:
        result['certificate']=dict(M0=as_rows(M0),Z0=as_rows(Z0),L=as_rows(L),
            F1=as_rows(F1),pairing=as_rows(pairing),evaluation=as_rows(E))
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--triples',default='11:4:0,11:4:2,11:4:4,17:6:0,17:6:3,17:6:6,43:16:0,43:16:7,53:18:0,53:18:3,83:31:0,83:31:12')
    ap.add_argument('--center',type=int,default=1)
    ap.add_argument('--out',default='two_sided_kernel.json')
    args=ap.parse_args(); start=time.time(); results=[]
    symbolic_data=symbolic()[2]
    print(json.dumps(symbolic_data),flush=True)
    for item in args.triples.split(','):
        r=run(*map(int,item.split(':')),center=args.center,example=item=='11:4:2')
        results.append(r)
        Path(__file__).with_name(args.out).write_text(json.dumps(dict(symbolic=symbolic_data,cases=results),indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in r.items() if k!='certificate'})+f' elapsed={time.time()-start:.1f}',flush=True)
