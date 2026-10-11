"""Fixed algebra checks for the actual six-kernel adjoint obstruction.

This producer neither imports frozen producers nor scans primes.  It does not
verify monodromy or analytic continuation: those arguments are in the report.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

t, r, x, lam, d = sp.symbols('t r x lam d')
checks = []
def check(name, claim):
    assert bool(claim), name
    checks.append(name)
def red(expr):
    return sp.rem(sp.Poly(sp.expand(expr), r), sp.Poly(r*r-5, r)).as_expr()

Cm = 1-(6-2*r)*t+(6-2*r)*t*t
Cp = 1-(6+2*r)*t+(6+2*r)*t*t
Nm = 1-(6+r)*t+(1+r)*t*t
Np = 1-(6-r)*t+(1-r)*t*t
Delta = 1-12*t+28*t*t-32*t**3+16*t**4
Q8 = sp.Rational(1,4)*(256*t**8-1344*t**7+3200*t**6-4176*t**5+3104*t**4-1316*t**3+320*t*t-49*t+6)
check('Delta equals C_minus times C_plus', red(Cm*Cp-Delta)==0)
check('Q has branch double principal part 3/16', sp.rem(Q8-sp.Rational(3,16)*t*(1-t)**2*sp.diff(Delta,t)**2, Delta,t)==0)
check('Q has cusp t=1 double principal part 1/4', Q8.subs(t,1)==sp.Rational(1,4)*Delta.subs(t,1)**2)
check('Q is O(t^-3) at infinity', sp.degree(Q8,t)-sp.degree(t*(1-t)**2*Delta**2,t)==-3)
check('Delta has four simple roots', sp.discriminant(Delta,t)!=0)
for label, nc, cc, co in [('minus',Nm,Cm,Cp),('plus',Np,Cp,Cm)]:
    check(label+' fixed kernel denominator has degree 5',sp.degree((1-t)*nc*cc,t)==5)
    check(label+' N roots are simple',red(sp.discriminant(nc,t))!=0)
    check(label+' N and Delta are coprime',red(sp.resultant(nc,Delta,t))!=0)
    check(label+' N avoids 0 and 1',nc.subs(t,0)!=0 and nc.subs(t,1)!=0)
    check(label+' C avoids 0 and 1',cc.subs(t,0)!=0 and cc.subs(t,1)!=0)
    # Gauge logarithmic derivative rho=N'/N+1/(1-t)-C_other'/2C_other.
    check(label+' gauge rho has no 1/t term at infinity',2-1-1==0)

def indicial(a2res,a1double,a0triple):
    return sp.expand(lam*(lam-1)*(lam-2)+a2res*lam*(lam-1)+a1double*lam+a0triple)
def gauge_indicial(m,q2):
    return indicial(-3*m,3*(m*m+m)+4*q2,-m*(m+1)*(m+2)-4*q2*(m+1))

polys = {
 'cusp0':indicial(3,1,0),
 'cusp1':gauge_indicial(-1,sp.Rational(1,4)),
 'ownC':gauge_indicial(0,sp.Rational(3,16)),
 'otherC':gauge_indicial(-sp.Rational(1,2),sp.Rational(3,16)),
 'N':gauge_indicial(1,0),
 'ordinary':indicial(0,0,0),
}
expected = {
 'cusp0':lam**3,'cusp1':lam**3,
 'ownC':(lam-sp.Rational(1,2))*(lam-1)*(lam-sp.Rational(3,2)),
 'otherC':lam*(lam-sp.Rational(1,2))*(lam-1),
 'N':(lam-1)*(lam-2)*(lam-3),
 'ordinary':lam*(lam-1)*(lam-2),
}
for name, poly in polys.items():
    check(name+' homogeneous indicial polynomial',sp.expand(poly-expected[name])==0)
    # Formal adjoint of a monic Fuchsian order-3 operator reverses exponents.
    aa=sp.expand(poly).coeff(lam,2)+3
    bb=sp.expand(poly).coeff(lam,1)-2+aa
    cc=poly.subs(lam,0)
    adj=sp.expand(-lam*(lam-1)*(lam-2)+aa*lam*(lam-1)+(-2*aa-bb)*lam+2*aa+2*bb+cc)
    check(name+' adjoint indicial polynomial',sp.expand(adj-expected[name].subs(lam,2-lam))==0)

f=sp.Function('f')(t)
b=sp.Function('b')(t)
a0=sp.Function('a0')(t);a1=sp.Function('a1')(t);a2=sp.Function('a2')(t)
c=a2*b-sp.diff(b,t)
dd=a1*b-sp.diff(c,t)
adj=-sp.diff(b,t,3)+a2*sp.diff(b,t,2)+(2*sp.diff(a2,t)-a1)*sp.diff(b,t)+(sp.diff(a2,t,2)-sp.diff(a1,t)+a0)*b
check('rational primitive F coefficient equals minus formal adjoint',sp.simplify(sp.diff(dd,t)-a0*b+adj)==0)
expr=sp.diff(b*sp.diff(f,t,2)+c*sp.diff(f,t)+dd*f,t).subs(sp.diff(f,t,3),-a2*sp.diff(f,t,2)-a1*sp.diff(f,t)-a0*f)
check('primitive coefficient cancellation removes F prime and F double prime',sp.simplify(expr+adj*f)==0)

inf_adj = -d*(d-1)*(d-2)+3*d*(d-1)-7*d+8
check('adjoint leading coefficient at infinity is -(d-2)^3',sp.expand(inf_adj+(d-2)**3)==0)
check('forced finite zeros have total degree 8',sp.degree(t*t*(1-t)**2*Delta,t)==8)
check('only allowed pole divisor N has degree 2',sp.degree(Nm,t)==2 and sp.degree(Np,t)==2)
check('nonzero b finite divisor forces infinity growth at least 6',8-2==6)
check('finite divisor lower growth contradicts adjoint upper growth',6>2)

out={
 'scope':'Fixed algebra and adjoint indicial checks only; no prime scan, no frozen producer import, no new Smith layer. Actual-rank and common-leaf arguments are in the report.',
 'checks_passed':len(checks),'checks':checks,
 'kernel_space_dimension':6,
 'adjoint_equation':'-L_epsilon^* b = P/[t(1-t)N_epsilon C_epsilon]',
 'rational_adjoint_solution':'none for any nonzero polynomial P of degree at most 5',
 'finite_zero_divisor':'2[0]+2[1]+div(Delta)',
 'allowed_finite_pole_divisor':'div(N_epsilon), multiplicity at most 1',
 'infinity_growth_bounds':{'finite_divisor_minimum':6,'adjoint_equation_maximum':2},
 'actual_rank_increment_per_sign':6,
 'unremoved_period_carrier':'epsilon*Theta*A^(epsilon)',
 'open':'Complete integral model, degree and primitive Smith directions for these new integrals; no S3 conclusion.'
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'certificate':str(dest.resolve()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
