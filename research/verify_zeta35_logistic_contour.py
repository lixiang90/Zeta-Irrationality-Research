"""Independent numeric kernel and exact p-adic checks for the theta contour functional.
Numerical quadrature is a diagnostic; it does not certify an infinite-scale bound.
"""
import json
from pathlib import Path
import mpmath as mp
from flint import fmpq as Q
from zeta35_logistic_contour import moment

mp.mp.dps=90
pi=mp.pi

def rho(y):
    return pi/(2*mp.cosh(pi*y)**2)

def w(y):
    t=mp.tanh(pi*y)
    return mp.j*rho(y)*((pi**3/3)*t*(2-3*t*t)+3*pi*t)

checks=[]
for j in (0,1,2,5):
    integrand=lambda y: 2*mp.re(w(y)/(mp.mpf('0.5')+mp.j*y+j))
    value=mp.quad(integrand,[0,mp.mpf('.5'),1,2,mp.inf])
    expected=3*mp.zeta(3,j+1)+mp.zeta(5,j+1)
    error=abs(value-expected)
    assert error<mp.mpf('1e-80')
    checks.append(dict(j=j,quadrature=str(value),expected=str(expected),absolute_error=str(error)))

for e in range(9):
    value=mp.quad(lambda y: 2*mp.re((mp.mpf('0.5')+mp.j*y)**e*w(y)),[0,mp.mpf('.5'),1,2,mp.inf])
    rational=moment(e)
    expected=mp.mpf(int(rational.numerator))/int(rational.denominator)
    assert abs(value-expected)<mp.mpf('1e-80')


def primes(limit):
    return [p for p in range(5,limit+1) if all(p%d for d in range(2,int(p**.5)+1))]

for p in primes(101):
    for e in range(2*p-1):
        assert int(moment(e).denominator)%p
    bad=moment(2*p-1)
    assert int(bad.denominator)%p==0
    reduced=bad*p
    actual=(int(reduced.numerator)*pow(int(reduced.denominator),-1,p))%p
    assert actual==(-3*pow(2,-1,p))%p
    for e in range(4*p-1):
        assert int(moment(e,0).denominator)%p
    assert int(moment(4*p-1,0).denominator)%p==0

Path(__file__).with_suffix('.json').write_text(json.dumps(dict(status='diagnostic_checks_passed',
    scope='quadrature at four poles and moments 0..8; exact thresholds for primes <=101; general proof in literature_status_20261004.md',
    poles=checks),indent=2),encoding='utf-8')
print('4 pole quadratures, 9 polynomial moments, and exact threshold checks for primes <=101 passed')
