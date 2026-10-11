"""NEW independent trivial-character Manin/degeneracy calculation.

No frozen or peer mathematical producer is imported or executed.
Only SymPy exact rational linear algebra and a fixed eta/Sturm jet are used.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import json
import sympy as sp

EYE = sp.eye(2)
S = sp.Matrix([[0, -1], [1, 0]])
T = sp.Matrix([[1, 1], [0, 1]])
STAR = sp.diag(-1, 1)

def projective_key(A, level):
    c, d = (int(z) for z in A[1, :])
    units = [u for u in range(level) if sp.gcd(u, level) == 1]
    return min((u*c % level, u*d % level) for u in units)

def polynomial_action(g):
    a, b, c, d = list(g)
    return sp.Matrix([[d*d, b*d, b*b],
                      [2*c*d, a*d+b*c, 2*a*b],
                      [c*c, a*c, a*a]])

def convergents(x):
    x = Fraction(x)
    a, b = x.numerator, x.denominator
    p0, p1, q0, q1 = 0, 1, 1, 0
    result = [(1, 0)]
    while b:
        k = a//b
        a, b = b, a-k*b
        p0, p1, q0, q1 = p1, k*p1+p0, q1, k*q1+q0
        result.append((p1, q1))
    return result

class Manin:
    def __init__(self, level):
        self.level = level
        self.reps = [EYE]
        self.keys = {projective_key(EYE, level): 0}
        for A in self.reps:
            for g in (S, T):
                B = A*g
                k = projective_key(B, level)
                if k not in self.keys:
                    self.keys[k] = len(self.reps)
                    self.reps.append(B)
        self.size = 3*len(self.reps)
        self.S = self.induced(S)
        self.T = self.induced(T)
        self.R = self.induced(T*S)
        self.relations = (sp.eye(self.size)+self.S).col_join(
            sp.eye(self.size)+self.R+self.R**2)
        self.period = sp.Matrix.hstack(*self.relations.nullspace())
        self.star = sp.zeros(self.size)
        for j, A in enumerate(self.reps):
            k = self.normalize(STAR*A*STAR)
            self.star[3*j:3*j+3, 3*k:3*k+3] = polynomial_action(STAR)

    def normalize(self, A):
        k = self.keys[projective_key(A, self.level)]
        gamma = A*self.reps[k].inv()
        assert gamma.det() == 1 and gamma[1, 0] % self.level == 0
        return k

    def induced(self, g):
        M = sp.zeros(self.size)
        for j, A in enumerate(self.reps):
            k = self.normalize(A*g.inv())
            M[3*j:3*j+3, 3*k:3*k+3] = polynomial_action(g)
        return M

    def edge_row(self, alpha, beta, Q):
        # g maps 0 to alpha and infinity to beta, with positive determinant.
        a, c = beta
        b, d = alpha
        g = sp.Matrix([[a, b], [c, d]])
        if g.det() == -1:
            g[:, 0] = -g[:, 0]
        assert g.det() == 1
        k = self.normalize(g)
        q = polynomial_action(g)*sp.Matrix(Q)
        row = sp.zeros(1, self.size)
        row[0, 3*k:3*k+3] = sp.Matrix([[q[2], -q[1]/2, q[0]]])
        return row

    def endpoint_row(self, x, Q):
        if x is None:
            return sp.zeros(1, self.size)
        cv = convergents(x)
        return sum((self.edge_row(cv[j], cv[j-1], Q)
                    for j in range(1, len(cv))), sp.zeros(1, self.size))

    def slash(self, g):
        M = sp.zeros(self.size)
        det = g.det()
        for j, A in enumerate(self.reps):
            B = g*A
            a, b, c, d = list(B)
            alpha = Fraction(int(b), int(d)) if d else None
            beta = Fraction(int(a), int(c)) if c else None
            polys = [(b*b, -2*b*d, d*d),
                     (2*a*b, -2*(a*d+b*c), 2*c*d),
                     (a*a, -2*a*c, c*c)]
            for z, Q in enumerate(polys):
                QQ = [sp.Rational(v, det) for v in Q]
                M[3*j+z, :] = (self.endpoint_row(alpha, QQ)
                               - self.endpoint_row(beta, QQ))
        return M

    def hecke(self, p):
        maps = [sp.Matrix([[1, b], [0, p]]) for b in range(p)]
        maps.append(sp.Matrix([[p, 0], [0, 1]]))
        return p*sum((self.slash(g) for g in maps), sp.zeros(self.size))

def restrict_kernel(operator, basis):
    ns = (operator*basis).nullspace()
    return basis*sp.Matrix.hstack(*ns) if ns else sp.zeros(basis.rows, 0)

def serial(A):
    return [[str(v) for v in row] for row in A.tolist()]

checks = {}
def verify(name, proposition):
    checks[name] = bool(proposition)
    if not proposition:
        raise AssertionError(name)

m6, m12 = Manin(6), Manin(12)
B5_6, B5_12 = m6.hecke(5), m12.hecke(5)
c6 = restrict_kernel(B5_6-6*sp.eye(m6.size), m6.period)
old12 = restrict_kernel(B5_12-6*sp.eye(m12.size), m12.period)
even6 = restrict_kernel(m6.star-sp.eye(m6.size), c6)
odd6 = restrict_kernel(m6.star+sp.eye(m6.size), c6)
lift = sp.zeros(m12.size, m6.size)
for j, A in enumerate(m12.reps):
    k = m6.normalize(A)
    lift[3*j:3*j+3, 3*k:3*k+3] = sp.eye(3)
D2 = m12.slash(sp.diag(2, 1))
Umap = (sp.eye(m12.size)-D2)*lift
Ueven, Uodd = Umap*even6, Umap*odd6
W12 = m12.slash(sp.Matrix([[0, -1], [12, 0]]))
omega6 = m6.endpoint_row(Fraction(0), [0, 0, 1])
omega12 = m12.endpoint_row(Fraction(0), [0, 0, 1])
central6 = sp.zeros(1, m6.size)
central6[0, 1] = 1
central12 = sp.zeros(1, m12.size)
central12[0, 1] = 1
end = m12.endpoint_row(Fraction(2, 7),
                       [sp.Rational(4, 49), -sp.Rational(4, 7), 1])

verify("level6 has12 cosets", len(m6.reps) == 12)
verify("level12 has24 cosets", len(m12.reps) == 24)
verify("level6 Manin dimension6", m6.period.cols == 6)
verify("level12 Manin dimension12", m12.period.cols == 12)
verify("level6 T5=6 cusp dimension2", c6.cols == 2)
verify("level12 T5=6 old dimension4", old12.cols == 4)
verify("level6 cusp parity1+1", even6.cols == odd6.cols == 1)
verify("lift satisfies Manin", m12.relations*lift*c6 == sp.zeros(144, 2))
verify("degeneracy satisfies Manin", m12.relations*D2*lift*c6 == sp.zeros(144, 2))
verify("U lies in old T5=6", (B5_12-6*sp.eye(72))*Umap*c6 == sp.zeros(72, 2))
verify("U anti W12", (W12+sp.eye(72))*Umap*c6 == sp.zeros(72, 2))
verify("Ueven nonzero", Ueven != sp.zeros(72, 1))
verify("Uodd nonzero", Uodd != sp.zeros(72, 1))
verify("L3 U half L3 f6", omega12*Ueven == omega6*even6/2)
verify("central U zero", central12*Uodd == sp.zeros(1, 1))
verify("f6 even L3 carrier nonzero", (omega6*even6)[0] != 0)
verify("f6 odd L2 carrier nonzero", (central6*odd6)[0] != 0)
re_coeff = sp.factor((end*Ueven)[0]/(omega12*Ueven)[0])
im_coeff = sp.factor((end*Uodd)[0]/(central6*odd6)[0])
verify("U exact even endpoint relation",
       (end-re_coeff*omega12)*Ueven == sp.zeros(1, 1))
verify("U exact odd endpoint relation",
       end*Uodd-im_coeff*central6*odd6 == sp.zeros(1, 1))

# Fixed independent eta jet. Newman/eta modularity and Sturm applicability
# are explained in the NEW note; this does not prove period independence.
LIMIT = 41
coef = [1]+[0]*LIMIT
for d in (1, 2, 3, 6):
    for k in range(d, LIMIT+1, d):
        for repeat in range(2):
            for n in range(LIMIT, k-1, -1):
                coef[n] -= coef[n-k]
f6 = [0]+coef[:LIMIT]
verify("eta q coefficient1 is1", f6[1] == 1)
verify("f6 T5=6 through Sturm bound8", all(
    f6[5*n]+(125*f6[n//5] if n%5 == 0 else 0) == 6*f6[n]
    for n in range(1, 9)))

r = sp.sqrt(3)
R = sp.Rational(5, 14)*sp.Matrix([[1-3*r, 1+r],
                                [-33+27*r, 1-3*r]])
conjR = R.applyfunc(lambda z: z.subs(r, -r))
square = (R*conjR).applyfunc(sp.simplify)
verify("real endpoint semilinear square trace", sp.trace(square) == -sp.Rational(250, 7))
verify("real endpoint semilinear square determinant", sp.factor(square.det()) == sp.Rational(15625, 2401))
verify("semilinear square has no eigenvalue1", sp.factor((sp.eye(2)-square).det()) == sp.Rational(103776, 2401))
verify("semilinear square negative eigenvalues", 875**2 > 3*500**2)
A, B, rr = sp.symbols("A B r")
alpha, baralpha = A+B*rr, A-B*rr
expr = sp.rem((alpha-baralpha)*(1-3*rr)-(1+rr)*alpha*baralpha-33+27*rr,
              rr**2-3, rr).expand()
verify("two source equations difference", sp.expand(expr.coeff(rr)-expr.coeff(rr, 0)) == 20*(B+3))
verify("two source equations no rational A", sp.expand(expr.coeff(rr, 0).subs(B, -3)) == 48-A*A)
verify("48 not rational square", sp.sqrt(48).is_Rational is False)

data = {"date": "2026-10-06",
        "scope": "NEW exact trivial-character Manin and level6-to12 degeneracy. Actual U endpoint uses L3(U) and L2(f6), not L2(U)=0. No numerical period linear independence or irrationality theorem.",
        "execution_history": ["First NEW execution failed at an incorrect expected level6 Manin dimension8 (correct dimension6), before final output.", "Second NEW execution corrects only that dimension expectation; 21 checks passed, no old/peer producer imported or executed.", "Third NEW execution adds seven fixed exact semilinear matrix/two-source obstruction checks, supporting the three-source iff criterion proved in the NEW note."],
        "checks": checks, "passed": sum(checks.values()),
        "level6_cosets": [serial(A) for A in m6.reps],
        "level12_cosets": [serial(A) for A in m12.reps],
        "level6_even_cusp_basis": serial(even6),
        "level6_odd_cusp_basis": serial(odd6),
        "U_even_period_vector_from_f6_basis": serial(Ueven),
        "U_odd_period_vector_from_f6_basis": serial(Uodd),
        "L3_f6_even_row": serial(omega6*even6),
        "L2_f6_odd_row": serial(central6*odd6),
        "L3_U_even_row": serial(omega12*Ueven),
        "endpoint_U_even_row": serial(end*Ueven),
        "endpoint_U_odd_row": serial(end*Uodd),
        "Re_endpoint_U_from_L3_U": str(re_coeff),
        "Im_endpoint_U_from_2pi_L2_f6": str(im_coeff),
        "R_sigmaR": serial(square),
        "det_identity_minus_R_sigmaR": str(sp.factor((sp.eye(2)-square).det())),
        "f6_q1_to8": f6[1:9]}
Path(__file__).with_suffix(".json").write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: data[k] for k in ("passed", "Re_endpoint_U_from_L3_U", "Im_endpoint_U_from_2pi_L2_f6", "f6_q1_to8")}, ensure_ascii=False, indent=2))
