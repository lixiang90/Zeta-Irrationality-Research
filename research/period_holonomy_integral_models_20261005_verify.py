"""Exact identities for the conductor-three integral holonomy test model.

The finite coefficient checks are diagnostics, not the all-scale denominator proof.
No frozen file is modified. Run with Python 3 and SymPy.
"""
from pathlib import Path
from fractions import Fraction
from math import comb, lcm
import hashlib
import json
import sympy as S

HERE = Path(__file__).resolve().parent
s, z, v, b, c, d, x = S.symbols('s z v b c d x')
A = s * (1 + s)
K = 1 + 3*s + 3*s*s
psi = s / (1 + s)
checks = {}
def check(name, expression):
    expression = S.factor(expression)
    checks[name] = bool(expression == 0)
    if not checks[name]:
        raise AssertionError((name, expression))

check('mobius_derivative', S.diff(psi,s)/(1+psi+psi**2)-1/K)
check('log_derivative', S.diff(psi,s)/psi-1/A)
check('integer_inverse', psi.subs(s,z/(1-z))-z)
connection = S.Matrix([[0,0,0],[1/K,0,0],[0,1/A,0]])
cyclic = S.Matrix([[0,0,1],[0,1/A,0],[1/(A*K),-S.diff(A,s)/A**2,0]])
check('cyclic_determinant', cyclic.det()+1/(K*A**2))
check('infinity_omega1', -1/(v*v+3*v+3) - (1/K*S.diff(1/v,v)).subs(s,1/v))
check('infinity_omega2', -1/(1+v) - (1/A*S.diff(1/v,v)).subs(s,1/v))

M0 = S.Matrix([[1,0,0],[0,1,0],[0,3,1]])
Ml = S.Matrix([[1,0,0],[-1,1,0],[-1,0,1]])
Mu = S.Matrix([[1,0,0],[1,1,0],[-1,0,1]])
Mm = S.Matrix([[1,0,0],[0,1,0],[2,-3,1]])
checks['monodromy_unimodular'] = all(M.det()==1 for M in [M0,Ml,Mu,Mm])
checks['compatible_product'] = M0*Ml*Mu*Mm == S.eye(3)
assert checks['monodromy_unimodular'] and checks['compatible_product']

f = v*v+3*v+3
check('first_blowup_chart', f.subs(3,v*b)-v*(v+b+v*b))
check('second_blowup_v_chart', (v+b+v*b).subs(b,v*c)-v*(1+c+v*c))
check('second_blowup_b_chart', (v+b+v*b).subs(v,b*d)-b*(1+d+b*d))

def chi(n):
    return 0 if n%3==0 else (1 if n%3==1 else -1)
def coefficients(j, N):
    orig = [Fraction(0)] + [Fraction(chi(n), n**j) for n in range(1,N+1)]
    pulled = [Fraction(0)]
    for n in range(1,N+1):
        pulled.append(sum((Fraction((-1)**(n-r)*comb(n-1,r-1))*orig[r]
                           for r in range(1,n+1)), Fraction(0)))
    return orig,pulled
N = 12  # One fixed prefix, not a parameter search.
prefix_checks = {}
examples = {}
for j in [1,2]:
    orig,pulled = coefficients(j,N)
    recovered = [Fraction(0)] + [sum((Fraction(comb(n-1,r-1))*pulled[r]
                                     for r in range(1,n+1)),Fraction(0))
                                for n in range(1,N+1)]
    assert recovered==orig
    do = lcm(*(q.denominator for q in orig))
    dh = lcm(*(q.denominator for q in pulled))
    base = lcm(*range(1,N+1))
    while base%3==0:
        base//=3
    assert do==dh==base**j
    prefix_checks[str(j)] = {'N':N,'denominator':do,'inverse_recovered':True}
    examples[str(j)] = [str(q) for q in pulled[1:7]]

Ipieces = [S.Rational(17,4)-3*x+x*x/2,
           S.Rational(19,4)-4*x+x*x,
           S.Rational(5,2)-x,
           (3-x)**2/2]
intervals = [(S.Rational(0),S.Rational(1)),(S.Rational(1),S.Rational(3,2)),
             (S.Rational(3,2),S.Rational(2)),(S.Rational(2),S.Rational(3))]
def sharp(total, maximum):
    vals=[]
    for I,(lo,hi) in zip(Ipieces,intervals):
        objective=total*x+maximum*I
        candidates=[lo,hi]
        candidates += [r for r in S.solve(S.diff(objective,x),x)
                       if r.is_real and lo<=r<=hi]
        vals += [(S.factor(objective.subs(x,t)),t) for t in candidates]
    value,attained=min(vals,key=lambda a:a[0])
    return S.factor(S.Rational(2,9)*value),attained
tau_pure,at_pure=sharp(3,2)
tau_log,at_log=sharp(2,1)
tau_one,at_one=sharp(1,1)
assert tau_pure==S.Rational(17,12)
assert tau_log==S.Rational(5,6)
assert tau_one==S.Rational(5,9)
assert S.Rational(5,9)+tau_log==S.Rational(25,18)

md = HERE / 'period_holonomy_integral_models_20261005.md'
payload = {
    'scope':'Exact symbolic diagnostics; all-scale statements have proofs in report.',
    'checks':checks,
    'connection':str(connection),
    'cyclic_determinant':str(S.factor(cyclic.det())),
    'boundary_discriminant':str(S.discriminant(K,s)),
    'boundary_resultants_with_s_and_s_plus_1':[str(S.resultant(K,s,s)),str(S.resultant(K,s+1,s))],
    'monodromy_column_matrices':{n:[list(row) for row in M.tolist()] for n,M in
                               [('origin',M0),('lower_cyclotomic_pole',Ml),
                                ('upper_cyclotomic_pole',Mu),('minus_one',Mm)]},
    'fixed_prefix_diagnostics':prefix_checks,
    'first_six_pulled_coefficients':examples,
    'm3_I_xi_piecewise':[str(q) for q in Ipieces],
    'tau_sharp':{'pure_0_1_2':str(tau_pure),'0_1_1':str(tau_log),'0_1_0':str(tau_one)},
    'best_natural_type_tau':'25/18',
    'report_sha256':hashlib.sha256(md.read_bytes()).hexdigest() if md.exists() else None,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
target = HERE/'period_holonomy_integral_models_20261005_verify.json'
target.write_text(json.dumps(payload,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'all_checks_passed':all(checks.values()),'json':str(target),
                  'report_sha256':payload['report_sha256']},ensure_ascii=False))
