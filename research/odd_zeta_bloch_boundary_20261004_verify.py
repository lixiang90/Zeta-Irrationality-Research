"""Exact algebraic checks for the averaged Catalan endpoint Bloch construction.

The local specialization proof, Steinberg exactness and Borel injectivity are
written arguments in the companion report, not conclusions of this certificate.
"""
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix('.json')
a, b, I = S.sqrt(2), S.sqrt(3), S.I
s = (a*b-a)/2
x = S.Symbol('x')
Q = lambda v: v**8 - 14*v**4 + 1
checks = {}

def check(name, condition, evidence):
    truth = bool(condition)
    checks[name] = {'passed': truth, 'evidence': evidence}
    if not truth:
        raise AssertionError(name)

simp = S.simplify
check('endpoint_curve_and_branch',
      simp(Q(s)) == 0 and simp(s*s-(2-b)) == 0,
      {'s0': str(s), 'square': str(simp(s*s)), 'Q_s0': str(simp(Q(s)))})
poly = S.minimal_polynomial(a+b+I, x)
check('number_field_degree_8', S.Poly(poly, x).degree() == 8,
      {'primitive_element': 'sqrt(2)+sqrt(3)+i', 'minimal_polynomial': str(poly),
       'degree': 8, 'complex_pairs': 4, 'reason_for_no_real_embedding': 'contains i'})
conjugates = []
for ea, eb in [(1,1),(-1,1),(1,-1),(-1,-1)]:
    sc = simp((ea*a*eb*b-ea*a)/2)
    h = { (1,1): s, (-1,1): -s, (1,-1): -1/s, (-1,-1): 1/s }[(ea,eb)]
    check('conjugate_' + str((ea,eb)),
          simp(sc-h) == 0 and simp(Q(sc)) == 0,
          {'a_sign': ea, 'b_sign': eb, 's_image': str(sc), 'V4_image': str(simp(h))})
    conjugates.append({'a_sign': ea, 'b_sign': eb, 'i_image': 'i', 's_image': str(sc)})
xp, xm = simp(s+1/s), simp(s-1/s)
up, um = simp((xp+a)/(xp-a)), simp((xm-I*a)/(xm+I*a))
check('elliptic_endpoints',
      simp(xp-a*b) == 0 and simp(xm+a) == 0,
      {'x_plus': str(xp), 'x_minus': str(xm)})
check('unit_endpoint_values',
      simp(up-(2+b)) == 0 and simp(um-I) == 0,
      {'u_plus_B': str(up), 'u_minus_B': str(um),
       'F_plus_B': '1 via local order 2/1 argument', 'F_minus_B': '-1'})
qplus = x**4-4*x**2-12
rplus = I*x*(6-x*x)/a
rminus = x*(x*x+6)/a
check('plus_regularized_F_limit',
      simp(qplus.subs(x,xp)) == 0
      and simp(S.diff(qplus,x).subs(x,xp)) != 0
      and simp(rplus.subs(x,xp)) == 0
      and simp(S.diff(rplus,x).subs(x,xp)) != 0,
      {'q_plus_derivative': str(simp(S.diff(qplus,x).subs(x,xp))),
       'r_plus_derivative': str(simp(S.diff(rplus,x).subs(x,xp))),
       'orders_at_y0': {'y':1, 'x_minus_sqrt6':2, 'r_plus':2},
       'regular_F_plus_value':'1'})
check('minus_F_unit_limit', simp(rminus.subs(x,xm)) != 0,
      {'r_minus_B':str(simp(rminus.subs(x,xm))), 'regular_F_minus_value':'-1'})
# The four extending-i embeddings are permuted transitively by the sign changes.
perms = []
labels = [(1,1),(-1,1),(1,-1),(-1,-1)]
for ma,mb in [(-1,1),(1,-1)]:
    P = S.zeros(4)
    for col,(ea,eb) in enumerate(labels):
        row = labels.index((ma*ea,mb*eb))
        P[row,col] = 1
    perms.append(P)
constraints = (perms[0]-S.eye(4)).col_join(perms[1]-S.eye(4))
kernel = constraints.nullspace()
check('full_regulator_fixed_space_is_diagonal',
      len(kernel) == 1 and kernel[0] == S.ones(4,1),
      {'constraint_rank': constraints.rank(), 'fixed_dimension':len(kernel),
       'basis':[list(v) for v in kernel],
       'qualification':'abstract embedding-coordinate calculation, no numeric regulator test'})
check('i_is_root_of_unity', I**4 == 1,
      {'identity':'i^4=1; bilinearity gives delta(4[i])=0 in antisymmetric tensor'})
report = ROOT / 'research/odd_zeta_bloch_boundary_20261004.md'
result = {
    'status':'passed', 'as_of':'2026-10-04', 'exact_arithmetic':'SymPy algebraic numbers and rational matrices',
    'checks': checks, 'conjugates':conjugates,
    'written_proof':str(report.relative_to(ROOT)).replace('\\','/'),
    'written_proof_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),
    'not_verified_by_finite_computation':[
        'Steinberg exactness; actual existence of a finite Bloch chain',
        'General ordinary-value/leading-unit boundary lemma',
        'Borel–Suslin injectivity of the full number-field regulator',
        'Irrationality of Catalan or any zeta value',
        'Lean formalization'
    ]
}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(checks),'certificate':str(OUT.relative_to(ROOT))},ensure_ascii=False))

