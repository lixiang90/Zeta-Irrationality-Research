"""NEW fixed symbolic certificate; no frozen or peer producer imports."""
from pathlib import Path
import hashlib
import json
import sympy as sp

x, n, e, r = sp.symbols('x n e r')
checks = []

def check(name, lhs, rhs):
    diff=lhs-rhs
    ok = (all(sp.simplify(v) == 0 for v in diff)
          if isinstance(diff, sp.MatrixBase) else sp.simplify(diff) == 0)
    checks.append({'name': name, 'passed': bool(ok)})
    if not ok:
        raise AssertionError((name, lhs, rhs))

ratio = ((n-sp.Rational(1, 2)+e)/(n+e))**4
check('all n>=1 coefficient recurrence', (n+e)**4*ratio,
      (n-sp.Rational(1, 2)+e)**4)
check('fibering residue coefficient ratio',
      (2*n+2)*(2*n+1)/((n+1)**2*4),
      (n+sp.Rational(1,2))/(n+1))
for j in range(5):
    q = sp.Symbol('q')
    check(f'forcing epsilon derivative {j}',
          sp.diff(e**4*sp.exp(q*e), e, j).subs(e,0),
          24 if j == 4 else 0)

def theta(expr):
    return sp.expand(x*sp.diff(expr,x))

def theta_shift(expr, shift, power):
    for _ in range(power):
        expr=sp.expand(theta(expr)+shift*expr)
    return expr

y=sp.Function('y')(x)
expr=theta_shift(y,0,4)-x*theta_shift(y,sp.Rational(1,2),4)
coeffs=[sp.expand(expr).coeff(sp.diff(y,x,j)) for j in range(5)]
expected=[-x/16,x*(1-5*x),x**2*(7-sp.Rational(29,2)*x),
          x**3*(6-8*x),x**4*(1-x)]
for j in range(5):check(f'ordinary coefficient order {j}',coeffs[j],expected[j])
check('indicial at zero',sum(sp.limit(coeffs[j]/x**j,x,0)*sp.prod(r-k for k in range(j)) for j in range(5)),r**4)
check('indicial at one',
      -sp.prod(r-k for k in range(4))-2*sp.prod(r-k for k in range(3)),
      -r*(r-1)**2*(r-2))
check('left theta operator',theta(expr),
      theta_shift(y,0,5)-x*theta_shift(theta_shift(y,sp.Rational(1,2),4),1,1))

T=sp.zeros(5)
for j in range(5):
    for k in range(j+1):T[j,k]=sp.binomial(j,k)
N=T-sp.eye(5)
check('fourth monodromy difference',N**4,sp.Matrix(5,5,lambda i,j:24 if (i,j)==(4,0) else 0))
check('fifth monodromy difference',N**5,sp.zeros(5))

stem=Path(__file__).with_suffix('')
out=stem.with_suffix('.json')
payload={'scope':'fixed symbolic identities only; no numeric period evaluation',
         'checks':checks,'check_count':len(checks),'all_passed':all(z['passed'] for z in checks),
         'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':payload['all_passed'],'output':str(out)}))
