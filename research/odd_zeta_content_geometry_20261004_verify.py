"""Fixed exact identities for the content/geometry report.

No parameter search. These checks verify one symbolic recurrence identity,
one polynomial filter identity, and one explicitly declared rational example.
The all-n valuation and content statements are proved in the report.
"""
from pathlib import Path
import json
import math
import sympy as s

n, m, i = s.symbols('n m i', integer=True, nonnegative=True)
x, y = s.symbols('x y')
eta = 16**n*s.factorial(2*n)*s.factorial(2*n+1)/s.factorial(4*n+3)
tn = 16**n*(6*n+5)*s.factorial(2*n)*s.factorial(n)**2/s.factorial(4*n+3)
Bn1 = s.factorial(2*n+2)/s.factorial(n+1)**2
recurrence_ratio = s.factor(s.combsimp(Bn1*tn/eta))
assert s.simplify(recurrence_ratio-2*(6*n+5)/(n+1)) == 0

f=x*x*y*y
g=1-x*x-y*y
h=g*g-4*f
# Exactly the m=2 common-pole identity; general m is the binomial theorem.
fixed_m=2
left=sum((-64)**j*s.binomial(fixed_m,j)*(f*h)**j*g**(2*(fixed_m-j))
         for j in range(fixed_m+1))
right=(g*g-64*f*h)**fixed_m
filter_residual=s.factor(left-right)
assert filter_residual == 0
saving_exponent=s.simplify((n+m)+i-(n+i))
assert saving_exponent == m

# One fixed declared example, n=3, used only to check conventions/signs.
fixed_n=3
Bn=s.binomial(2*fixed_n,fixed_n)
an=-Bn*sum(16**k*(6*k+5)*s.factorial(2*k)*s.factorial(k)**2/
           s.factorial(4*k+3) for k in range(fixed_n))
an=s.cancel(an)
assert an == -s.Rational(189946,10395)
num,den=map(int,s.fraction(an))
common=math.gcd(abs(num),int(Bn))
primitive=[num//common,den*int(Bn)//common]
assert primitive == [-94973,103950]

result={
  'scope':'Fixed exact identities, not a parameter search or proof by finite samples.',
  'recurrence_ratio':str(recurrence_ratio),
  'geometric_filter_fixed_m':fixed_m,
  'geometric_filter_polynomial_residual':str(filter_residual),
  'base16_saving_exponent':str(saving_exponent),
  'fixed_example':{'n':fixed_n,'a_tilde':str(an),'B':int(Bn),
                   'gcd':common,'primitive_coefficients_1_G':primitive},
  'all_checks_passed':True
}
destination=Path(__file__).with_suffix('.json')
destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
