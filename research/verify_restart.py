"""Independent checks of the restart calculations (not a proof of irrationality)."""
import json
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
import numpy as np
from scipy.integrate import quad
from b8_hankel import mu_monomial
from restart_probe import field
from restart_obstruction_certificate import primal_bound,double_integral,log_iv,atan_iv,PI
from restart_arithmetic import arithmetic

mp.mp.dps=650  # tiny-argument alternating-series intervals can be < 1e-480 wide
def m(q): return mp.mpf(q.numerator)/q.denominator
def contains(v,x): assert m(v.lo)<=x<=m(v.hi),(v,x)
for q in [F(1,40),F(2,5),F(2),F(39,20),F(1,10000),F(1000)]:
    contains(log_iv(q),mp.log(m(q)))
    contains(atan_iv(q),mp.atan(m(q)))
contains(PI,mp.pi)

# Independent gamma/Euler formula for the positive moments.
for e in range(12):
    expected=(-1)**e*mp.bernpoly(2*e+2,0)*mp.factorial(2*e+7)/(720*mp.factorial(2*e+2))
    actual=mu_monomial(e)
    assert mp.almosteq(mp.mpf(int(actual.p))/int(actual.q),expected)
assert str(mu_monomial(0))=="7/12"

# Check the exact antiderivative against a different, numerical integration path.
for alpha in [F(1,40),F(3,100),F(3,40)]:
    D=F(4,25); lam=1-alpha
    average=quad(lambda t:float(field(t,float(alpha))),0,float(D),epsabs=1e-12)[0]/float(D)
    C=-2*float(lam)+16*float(alpha*lam)*(1-np.log(float(alpha)))+3*float(lam)**2-2*float(lam)**2*np.log(float(2*lam))
    numeric=float(lam)**2*(np.log(float(D))-1.5)-float(lam)*average+C
    exact=primal_bound(alpha)
    assert abs(numeric-float(exact.lo))<1e-10

# Midpoint quadrature converges to the existing exact INNER/OUTER tables.
references={.025:(float(F(20895472586622029179,16690300170635520000)),float(F(318121,144000))),
            .075:(float(F(120667538150827615739401,708353029541942104320000)),float(F(263569,144000)))}
for alpha,(inside,outside) in references.items():
    result=arithmetic(alpha,n=48000)
    assert abs(result["inner"]-inside)<.00015
    assert abs(result["outer"]-outside)<.00015

rows=json.loads(Path(__file__).with_name("restart_nested.json").read_text())
for row in rows:
    assert row["success"] and abs(row["mass_error"])<1e-10
    assert row["primal"]<=row["numerical_upper"]
print("PASS: rational interval formulas, 12 independent moment checks, field integral,")
print("      2 exact arithmetic-table calibrations, and optimized measure mass constraints.")
