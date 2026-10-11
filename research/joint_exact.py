"""Exact multi-prefix Hankel engine for fixed zeta(7).

W(t)=prod D_N(t)^beta, independent h. Coefficients and contents are exact;
new transcendental evaluations use rigorous Arb ball arithmetic. The retained
mpmath evaluator is an independent numerical cross-check, not a certificate.
"""
from functools import lru_cache
from math import factorial, gcd, lcm, log
from pathlib import Path
import json
import sys
import mpmath as mp
from flint import fmpq, fmpq_poly, fmpq_mat, arb, ctx
from b8_hankel import Dpoly, mu_monomial, vp
from restart_free_dimension import determinant as determinant_interpolation

sys.set_int_max_str_digits(0)
Dcache=lru_cache(None)(Dpoly)
moment=lru_cache(None)(mu_monomial)


def determinant(aa,bb,h):
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    lead=B.det()
    if lead:return (-(B.inv()*A)).charpoly()*lead
    constant=A.det()
    if constant:
        # det(A+XB)=det(A) X^h charpoly(-A^{-1}B)(1/X).
        # Reversal retains the zeros forced by singular B and avoids h+1 determinants.
        cp=(-(A.inv()*B)).charpoly()
        return fmpq_poly([cp[h-i] for i in range(h+1)])*constant
    return determinant_interpolation(aa,bb,h)


def determinant_tail_split(aa,bb,K,nmax,h):
    """Eliminate the X-independent polynomial sector when h exceeds the pole count."""
    T=Dcache(K)//Dcache(nmax)
    return determinant_pole_split(aa,bb,T,h)


def determinant_pole_split(aa,bb,T,h):
    """Exact Schur reduction for any monic polynomial of surviving poles."""
    L=T.degree();s=h-L
    assert T[L]==1
    if s<=0 or L==0:return determinant(aa,bb,h)
    basis=[fmpq_poly([0]*i+[1]) for i in range(L)]
    basis += [fmpq_poly(T)*fmpq_poly([0]*j+[1]) for j in range(s)]
    C=fmpq_mat(h,h,[b[j] for b in basis for j in range(h)])
    # The degree-ordered basis is monic triangular, so det(C)=1.
    assert all(b.degree()==i and b[i]==1 for i,b in enumerate(basis))
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    A=C*A*C.transpose();B=C*B*C.transpose()
    assert all(not B[i,j] for i in range(h) for j in range(h) if i>=L or j>=L)
    low=fmpq_mat(L,L,[A[i,j] for i in range(L) for j in range(L)])
    topB=fmpq_mat(L,L,[B[i,j] for i in range(L) for j in range(L)])
    U=fmpq_mat(L,s,[A[i,L+j] for i in range(L) for j in range(s)])
    D=fmpq_mat(s,s,[A[L+i,L+j] for i in range(s) for j in range(s)])
    d=D.det();b=topB.det()
    if not d or not b:return determinant(aa,bb,h)
    schur=low-U*D.inv()*U.transpose()
    return (-(topB.inv()*schur)).charpoly()*(d*b)


def canonical(profile):
    out={}
    for N,beta in profile:
        assert N>=0 and beta>=0 and int(N)==N and int(beta)==beta
        if N and beta: out[N]=out.get(N,0)+beta
    return tuple(sorted(out.items()))


def entries(K,profile,h):
    profile=canonical(profile)
    assert K>0 and h>0 and all(N<=K for N,b in profile)
    W=fmpq_poly([1])
    for N,beta in profile: W*=Dcache(N)**beta
    return entries_from_polynomial(K,W,h)


def entries_from_polynomial(K,W,h):
    """The numerator need not have monotone root multiplicities."""
    assert K>0 and h>0
    D=fmpq_poly(Dcache(K))
    H=[fmpq(0)]
    for j in range(1,K+1): H.append(H[-1]+fmpq(1,j**7))
    deriv=D.derivative()
    residues=[(j,W(-j*j)/deriv(-j*j)) for j in range(1,K+1) if W(-j*j)]
    aa=[]; bb=[]; P=W
    powers=[fmpq(1)]*len(residues)
    for e in range(2*h-1):
        quotient=P//D
        a=sum((c*moment(k) for k,c in enumerate(quotient)),fmpq(0))
        b=fmpq(0)
        for idx,(j,r) in enumerate(residues):
            c=r*powers[idx]
            a+=c*(-j**6*H[j]-fmpq(1,6)+fmpq(1,2*j))
            b+=c*j**6
            powers[idx]*=-j*j
        aa.append(a); bb.append(b)
        P=P*fmpq_poly([0,1])
    return aa,bb


def content(poly):
    g=0; den=1
    for c in poly:
        g=gcd(g,int(c.p)); den=lcm(den,int(c.q))
    return fmpq(g,den)


def norm_scalar(K,profile,h):
    bottom=1
    for N,b in canonical(profile): bottom*=factorial(N)**b
    kappa=fmpq(factorial(K),bottom)
    qdet=fmpq(1)
    for i in range(1,h): qdet*=fmpq(2,factorial(2*i))
    return kappa**(2*h)*qdet**2


def binomial_matrices(K,profile,h,aa,bb):
    coeff=[]
    for i in range(h):
        qi=fmpq_poly([1]) if i==0 else fmpq_poly([0,2*(-1)**i])*Dcache(i-1)/fmpq(factorial(2*i))
        coeff.extend(qi[j] for j in range(h))
    C=fmpq_mat(h,h,coeff)
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    bottom=1
    for N,b in canonical(profile): bottom*=factorial(N)**b
    scale=fmpq(factorial(K),bottom)**2
    return C*A*C.transpose()*scale,C*B*C.transpose()*scale


def qlog(q):
    return mp.log(abs(mp.mpf(int(q.p))))-mp.log(mp.mpf(int(q.q)))


def evaluate_primitive(poly,precision_extra=100):
    ct=content(poly); primitive=poly/ct
    assert all(c.q==1 for c in primitive)
    bits=max(abs(int(c.p)).bit_length() for c in primitive)
    precision=int(bits*.30103)+precision_extra
    with mp.workdps(precision):
        z=mp.zeta(7); value=mp.mpf(0)
        for c in reversed(list(primitive)): value=value*z+mp.mpf(int(c.p))
        assert value>0
        lv=float(mp.log(value))
    return ct,lv,precision


def evaluate_primitive_ball(poly):
    ct=content(poly);primitive=poly/ct
    assert all(c.q==1 for c in primitive)
    bits=max(abs(int(c.p)).bit_length() for c in primitive)+400
    for _ in range(5):
        with ctx.workprec(bits):
            z=arb(7).zeta();value=arb(0)
            for c in reversed(list(primitive)):value=value*z+arb(c)
            if value>0:return ct,value.log(),bits
            if value<0:raise ValueError('negative determinant value')
        bits*=2
    raise ValueError('insufficient ball precision to certify positivity')


def experiment(K,profile,h,save=None):
    aa,bb=entries(K,profile,h)
    nmax=max((N for N,b in canonical(profile)),default=0)
    poly=determinant_tail_split(aa,bb,K,nmax,h)
    assert 0<=poly.degree()<=min(h,K-nmax)
    ct,lvball,bits=evaluate_primitive_ball(poly)
    lv=float(lvball.mid());precision=int(bits*.30103)
    S=norm_scalar(K,profile,h); cF=ct*S
    with ctx.workprec(160):
        lcFball=arb(cF).log();lcF=float(lcFball.mid())
        scoreball=(lvball/K**2).str(30)
        aball=(-lcFball/K**2).str(30)
        rball=((lvball+lcFball)/K**2).str(30)
    result=dict(K=K,profile=[list(p) for p in canonical(profile)],h=h,degree=poly.degree(),
                score=lv/K**2,arithmetic_exact=-lcF/K**2,
                real_exact_numeric=(lv+lcF)/K**2,precision=precision,
                evaluation='Arb ball arithmetic',score_ball=scoreball,
                arithmetic_ball=aball,real_ball=rball)
    if save:
        payload=dict(result=result,aa=[str(c) for c in aa],bb=[str(c) for c in bb],
                     poly=[str(c) for c in poly],content=str(ct),scalar=str(S))
        Path(save).write_text(json.dumps(payload),encoding="utf-8")
    return result,poly,aa,bb


if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("--K",type=int,default=40)
    p.add_argument("--h",type=int);p.add_argument("--profile",default="1:8")
    p.add_argument("--save")
    a=p.parse_args();profile=[tuple(map(int,t.split(":"))) for t in a.profile.split(",")]
    r,*_=experiment(a.K,profile,a.h or a.K-max(n for n,b in profile),a.save)
    print(json.dumps(r),flush=True)
