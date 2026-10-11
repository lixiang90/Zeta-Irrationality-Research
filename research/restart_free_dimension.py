"""Exact determinant experiments with independent K,N,h,beta and fixed zeta(7).

Only evaluations at zeta(7) use high precision; coefficients/content are exact.
The output is finite-size evidence, never an asymptotic irrationality certificate.
"""
import json
from pathlib import Path
from math import gcd,lcm
import mpmath as mp
from flint import fmpq,fmpz,fmpq_poly,fmpq_mat
from b8_hankel import Dpoly,mu_monomial


def entries_general(K,N,h,beta):
    DN,DK=Dpoly(N),Dpoly(K)
    W=fmpq_poly(DN**beta); D=fmpq_poly(DK)
    harmonics=[fmpq(0)]
    for j in range(1,K+1): harmonics.append(harmonics[-1]+fmpq(1,j**7))
    residues=[]
    for j in range(N+1,K+1):
        pole=-j*j
        residues.append((j,fmpq(DN(pole))**beta/D.derivative()(pole)))
    aa=[];bb=[]
    for e in range(2*h-1):
        quotient=(W*fmpq_poly([0]*e+[1]))//D
        a=sum((quotient[k]*mu_monomial(k) for k in range(quotient.degree()+1)),fmpq(0))
        b=fmpq(0)
        for j,r in residues:
            c=r*(-j*j)**e
            b+=c*j**6
            a+=c*(-j**6*harmonics[j]-fmpq(1,6)+fmpq(1,2*j))
        aa.append(a);bb.append(b)
    return aa,bb


def determinant(aa,bb,h):
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    lead=B.det()
    if lead: return (-(B.inv()*A)).charpoly()*lead
    # Exact Newton interpolation; does not assume a nonzero leading coefficient.
    values=[(A+B*fmpq(i)).det() for i in range(h+1)]
    poly=fmpq_poly([0]); basis=fmpq_poly([1])
    for j in range(h+1):
        poly+=basis*values[0]
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
        basis=basis*fmpq_poly([-j,1])/fmpq(j+1)
    assert poly(fmpq(h+2))==(A+B*fmpq(h+2)).det()
    return poly


def run(K,N,h,beta):
    a,b=entries_general(K,N,h,beta)
    poly=determinant(a,b,h)
    assert poly.degree()<=min(h,K-N)
    g=0;den=1
    for c in poly:
        g=gcd(g,int(c.p));den=lcm(den,int(c.q))
    primitive=poly/fmpq(g,den)
    assert all(c.q==1 for c in primitive)
    bits=max(abs(int(c.p)).bit_length() for c in primitive)
    # Enough absolute precision to evaluate the primitive polynomial by Horner.
    mp.mp.dps=int(bits*.30103)+150
    z=mp.zeta(7)
    value=mp.mpf(0)
    for c in reversed(list(primitive)): value=value*z+mp.mpf(int(c.p))
    assert value>0
    answer=dict(K=K,N=N,h=h,beta=beta,degree=poly.degree(),precision=mp.mp.dps,
                log_primitive_value_over_K2=float(mp.log(value)/(K*K)),
                log_content_over_K2=float((mp.log(g)-mp.log(den))/(K*K)))
    print(json.dumps(answer),flush=True)
    return answer


if __name__=="__main__":
    rows=[]
    for K in [12,20,40]:
        for beta in [4,8]:
            for h in [K//2,K-1,K+2]: rows.append(run(K,1,h,beta))
    Path(__file__).with_name("restart_free_dimension.json").write_text(json.dumps(rows,indent=2))
