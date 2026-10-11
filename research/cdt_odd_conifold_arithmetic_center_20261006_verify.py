"""NEW symbolic identities only; no imports of old or peer producers."""
from pathlib import Path
import hashlib
import json
import sympy as s

t = s.symbols('t')
n, rho = s.symbols('n rho')
f = s.Function('f')(t)

def theta(expr):
    return -(1-t)*s.diff(expr,t)

lhs1 = f
lhs2 = f
for _ in range(4):
    lhs1 = theta(lhs1)
    lhs2 = theta(lhs2)+lhs2/2
pf = s.expand(lhs1-(1-t)*lhs2)
a = [-(1-t)/16, (1-t)*(4-5*t), (1-t)**2*(29*t-15)/2,
     (1-t)**3*(2-8*t), t*(1-t)**4]
assert s.simplify(pf-sum(a[j]*s.diff(f,t,j) for j in range(5))) == 0

fall = lambda z,j: s.prod(z-k for k in range(j))
ip = s.expand(fall(rho,4)+2*fall(rho,3))
assert s.factor(ip-rho*(rho-1)**2*(rho-2)) == 0
il = s.expand(-(rho-3)*ip)
assert s.factor(il+rho*(rho-1)**2*(rho-2)*(rho-3)) == 0

# For all symbolic n, coefficient of c_(n+offset) in [t^n]Pf.
coefficients = {}
for offset in range(-1,4):
    value = sum(s.expand(a[j]).coeff(t,j-offset)*fall(n+offset,j)
                for j in range(5) if j-offset >= 0)
    coefficients[offset] = s.factor(value)
expected = {
    3: (n+3)*(n+2)**2*(n+1),
    2: -(n+2)*(n+1)*(8*n**2+20*n+15)/2,
    1: (n+1)*(12*n**3+24*n**2+23*n+8)/2,
    0: -(64*n**4+32*n**3+40*n**2+8*n+1)/16,
    -1: (n-s.Rational(1,2))**4,
}
for offset in expected:
    assert s.simplify(coefficients[offset]-expected[offset]) == 0
assert all(s.degree(s.expand(a[j]),t) <= j+1 for j in range(5))
assert s.expand(a[4]).coeff(t,0) == 0

c0,c1,c2,beta = s.symbols('c0 c1 c2 beta')
c3 = s.solve(expected[3].subs(n,0)*s.Symbol('c3')+
             expected[2].subs(n,0)*c2+expected[1].subs(n,0)*c1+
             expected[0].subs(n,0)*c0-beta/16,s.Symbol('c3'))[0]
assert s.simplify(c3-((beta+c0)/192-c1/3+5*c2/4)) == 0

root = Path(__file__).resolve().parent
output = {
    'status':'passed',
    'kind':'symbolic operator and all-n coefficient identity only',
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'identities': ['Euler-to-conifold operator','P indicial polynomial',
                   'L indicial polynomial','five all-n recurrence coefficients',
                   'no missing Taylor offsets','first forced coefficient'],
    'recurrence_coefficients':{str(k):str(v) for k,v in coefficients.items()},
    'old_or_peer_producer_executed':False,
    'initial_periods_algebraic_proved':False,
    'numeric_irrationality_proved':False,
    'lean_verified':False,
}
target=root/'cdt_odd_conifold_arithmetic_center_20261006_verify.json'
target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':output['status'],'output':str(target),
                  'numeric_irrationality_proved':False},ensure_ascii=False))
