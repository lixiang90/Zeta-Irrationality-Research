"""Positive-error rational approximants to theta from its Stieltjes functional.

All coefficients, denominators and error bounds are computed over Q.
Arb checks compare independent zeta evaluation with those bounds.
"""
import argparse
import json
import math
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, arb, ctx
from sympy import primerange


def moment(e):
    m5=Q(-1)**e*Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24
    m3=Q(-1)**(e+1)*Q.bernoulli(2*e+4)*(2*e+5)/2
    return m5-3*m3


def integral(p,mu):
    return sum((p[k]*mu[k] for k in range(len(p))),Q(0))


def qlog(q):
    assert q>0
    return math.log(int(q.numerator))-math.log(int(q.denominator))


def seed(m,mu):
    H=Mat([[mu[i+j] for j in range(m)] for i in range(m)])
    v=H.solve(Mat([[-mu[m+i]] for i in range(m)]))
    q=Poly([v[i,0] for i in range(m)]+[Q(1)])
    for j in range(m):
        assert integral(q*Poly([0]*j+[1]),mu)==0
    h=integral(q*q,mu)
    alpha=integral(q*q*Poly([0,1]),mu)/h
    assert h>0 and alpha>0
    return q,h,alpha


def main(maxm,maxN):
    ctx.prec=512
    mu=[moment(e) for e in range(2*maxm+2)]
    H3=[Q(0)];H5=[Q(0)]
    for N in range(1,maxN+1):
        H3.append(H3[-1]+Q(1,N**3));H5.append(H5[-1]+Q(1,N**5))
    theta=3*arb(3).zeta()+arb(5).zeta()
    primes=list(map(int,primerange(2,maxN+1)))
    seeds=[];rows=[]
    path=Path(__file__).with_suffix('.json')
    for m in range(1,maxm+1):
        q,h,alpha=seed(m,mu)
        seeds.append(dict(m=m,coefficients=[str(c) for c in q],norm=str(h),alpha=str(alpha)))
        current=[]
        for N in range(1,maxN+1):
            z=N*N;value=q(-z)
            quotient,remainder=divmod(Poly([value])-q,Poly([z,1]))
            assert not remainder
            pade=integral(quotient,mu)/value
            R=H5[N]+3*H3[N]+(pade+Q(3*(N*N-N),2)+1-Q(1,2*N))/N**4
            den=int(R.denominator)
            rough=den
            for prime in primes:
                if prime>N:
                    break
                while rough%prime==0:
                    rough//=prime
            lower=h/(N**4*value**2*(z+alpha))
            upper=h/(N**6*value**2)
            if 3<=m<=24 and N<=100:
                # A finite-grid certificate, not an asymptotic assertion.
                assert den*lower>1
            # Orthogonal polynomial identity implies strict error bounds.
            actual=theta-arb(R)
            assert actual>arb(lower) and actual<arb(upper)
            row=dict(m=m,N=N,log_denominator=math.log(den),
                     log_denominator_primes_above_N=math.log(rough),
                     log_error_lower=qlog(lower),log_error_upper=qlog(upper),
                     log_integer_error_lower=qlog(den*lower),
                     log_integer_error_upper=qlog(den*upper),
                     log_actual_integer_error=float((den*actual).log()))
            current.append(row)
        rows+=current
        best=min(current,key=lambda v:v['log_actual_integer_error'])
        print('m',m,'best N',best['N'],'log(D*error)',round(best['log_actual_integer_error'],6),flush=True)
        path.write_text(json.dumps(dict(scope='finite exact rational scan with analytic bounds; no irrationality proof',
                                       maxm=maxm,maxN=maxN,seeds=seeds,rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--maxm',type=int,default=24)
    p.add_argument('--maxN',type=int,default=100);args=p.parse_args()
    main(args.maxm,args.maxN)
