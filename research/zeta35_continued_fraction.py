"""Exact identities and denominator audit for the continued fraction of theta.

Source of the continued fraction: arXiv:2308.11829v2, Table 4.
The finite identities and the denominator obstruction are derived independently.
No irrationality claim is made by this program.
"""
import json
import math
from pathlib import Path

import sympy as sp
from flint import fmpq as Q, arb, ctx


def w(n):
    return 3*n*n+3*n+1


def a(n):
    return n**5+(n+1)**5+6*(n**3+(n+1)**3)


def verify_symbolic():
    x=sp.symbols('x')
    recurrence=sp.expand((x+1)**5*w(x+1)-a(x)*w(x)+x**5*w(x-1))
    telescoping=sp.cancel(1/(x**5*w(x-1)*w(x))
                          -1/x**5-3/x**3-sp.Rational(9,2)*(1/w(x)-1/w(x-1)))
    assert recurrence==0 and telescoping==0
    return dict(polynomial_solution=True, rational_telescoping=True)


def main():
    checks=verify_symbolic()
    # p_n/q_n = a_0 + b_1/(a_1 + ... + b_n/a_n), b_n=-n^10.
    pm, p=1,7
    qm, q=0,1
    s=Q(1,7)
    for n in range(101):
        if n:
            pm,p=p,a(n)*p-n**10*pm
            qm,q=q,a(n)*q-n**10*qm
            s+=Q(1,(n+1)**5*w(n)*w(n+1))
        assert p==math.factorial(n+1)**5*w(n+1)
        assert Q(q,p)==s
    checks['exact_convergents_0_to_100']=True

    ctx.prec=512
    theta=3*arb(3).zeta()+arb(5).zeta()
    H3=H5=S=Q(0)
    rows=[]
    selected={1,2,5,10,20,40,80,160,320,640}
    for M in range(1,max(selected)+1):
        H3+=Q(1,M**3)
        H5+=Q(1,M**5)
        S+=Q(1,M**5*w(M-1)*w(M))
        R=H5+3*H3+Q(9,2*w(M))
        assert R==Q(9,2)+S
        if M not in selected:
            continue
        error=theta-arb(R)
        lower=arb(Q(1,72*(M+1)**8))
        upper=arb(Q(1,72*M**8))*arb(Q(3*(M+1)**2,3*(M+1)**2-1))
        assert error>lower and error<upper
        denominator=int(R.denominator)
        retained=[]
        for p0 in sp.primerange(max(5,M//2+1),M+1):
            if w(M)%p0:
                # Exactly one summand has a denominator divisible by p0.
                assert denominator%p0**5==0 and denominator%p0**6!=0
                retained.append(int(p0))
        rows.append(dict(M=M,log_denominator=math.log(denominator),
                         log_error=error.log().str(25),
                         log_denominator_times_error=(denominator*error).log().str(25),
                         scaled_error=(M**8*error).str(25),
                         forced_primes=retained))
    out=dict(scope='exact identities, finite checks, and numerical illustration; no irrationality proof',
             checks=checks,rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
