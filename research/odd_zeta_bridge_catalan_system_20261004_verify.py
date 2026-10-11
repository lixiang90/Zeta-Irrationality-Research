"""Exact certificates for the Catalan generating-function system.

This checks symbolic identities and a fixed finite set of Taylor coefficients.
It does not replace the local-index proofs of actual function independence.
Run with Python 3 + sympy from the project root.
"""
from pathlib import Path
import json
import sympy as s

w = s.symbols('w')
X = s.symbols('X')
theta = lambda f: w*s.diff(f, w)
A = (8*w-3)/(16*(1-w))
B = (3*w-2)/(2*(1-w))
k = 2*w/(1-4*w)
M = s.Matrix([
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1/(32*(1-w)), A, B, 0],
    [0, -10*w/(1-4*w), -12*w/(1-4*w), k],
])
rows = [s.Matrix([[0, 0, 0, 1]])]
for j in range(3):
    rows.append((rows[-1].applyfunc(theta)+rows[-1]*M).applyfunc(s.factor))
cyclic_det = s.factor(s.Matrix.vstack(*rows).det())
assert cyclic_det != 0

# Hypergeometric input coefficients: F(w)=sum 16^n B_n w^n.
coeff = lambda n: 16**n*s.factorial(2*n)*s.factorial(2*n+1)/s.factorial(4*n+3)
count = 7  # a fixed identity check, not a parameter search
F = sum(coeff(n)*w**n for n in range(count+1))
U = theta(F)
R = 6*U+5*F
L2F = (theta(theta(F))+theta(F)+s.Rational(3,16)*F
       -w*(theta(theta(F))+s.Rational(3,2)*theta(F)+s.Rational(1,2)*F))
L2_jet = s.series(L2F, w, 0, count).removeO()
assert L2_jet == s.Rational(1,32)
ratio_checks = []
for n in range(count):
    expected = ((s.Rational(2*n+1, 2)*(n+1))/
                ((n+s.Rational(5,4))*(n+s.Rational(7,4))))
    assert s.cancel(coeff(n+1)/coeff(n)-expected) == 0
    ratio_checks.append(str(expected))

gcoeff = [X]
for n in range(count):
    # (1-4w) f'_X - 2 f_X = -2 R(w).
    gcoeff.append(s.expand(((4*n+2)*gcoeff[n]-2*(6*n+5)*coeff(n))/(n+1)))
fx = sum(gcoeff[n]*w**n for n in range(count+1))
f_eq_jet = s.series((1-4*w)*s.diff(fx,w)-2*fx+2*R,
                    w,0,count).removeO()
assert f_eq_jet == 0
known_a = [-s.Rational(5,3), -s.Rational(569,105), -s.Rational(189946,10395)]
for n, a in enumerate(known_a,1):
    assert s.expand(gcoeff[n]-s.binomial(2*n,n)*X) == a

# Ordinary-derivative residue matrices of the rational-relation obstruction.
H = s.Matrix([[k,-A],[-1,k-B]])
residues = {}
expected_spectra = {
    s.Rational(0): [s.Rational(1,4),s.Rational(3,4)],
    s.Rational(1,4): [-s.Rational(1,2),-s.Rational(1,2)],
    s.Rational(1): [s.Rational(0),s.Rational(1,2)],
}
for point, expected in expected_spectra.items():
    mat = (H/w).applyfunc(lambda h: s.limit((w-point)*h,w,point))
    values = sorted([eig for eig,mul in mat.eigenvals().items() for _ in range(mul)])
    assert values == sorted(expected)
    residues[str(point)] = {'matrix':str(mat),'spectrum':[str(v) for v in values]}
H_inf = H.applyfunc(lambda h:s.limit(h,w,s.oo))
assert sorted(H_inf.eigenvals().keys()) == [s.Rational(0),s.Rational(1,2)]

certificate = {
    'description':'Exact symbolic certificates; actual independence is proved in the companion report.',
    'system_matrix':str(M),
    'cyclic_determinant':str(cyclic_det),
    'cyclic_det_scope':'Formal row determinant, not by itself proof of actual function independence.',
    'hypergeometric_coefficient_ratios':ratio_checks,
    'L2_F_jet':str(L2_jet),
    'f_X_equation_jet':str(f_eq_jet),
    'a_tilde_n1_n3':[str(a) for a in known_a],
    'rational_relation_residues':residues,
    'H_infinity':str(H_inf),
    'all_checks_passed':True,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(certificate,ensure_ascii=False,indent=2))
