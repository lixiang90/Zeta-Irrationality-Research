"""One exact m=2 object diagnostic; no asymptotic or parameter scan."""
import json
from pathlib import Path

import mpmath as mp
import sympy as s

m = 2
n = 2 * m - 1
t, w, eps, Z = s.symbols("t w eps Z")
R = s.prod((t + j) ** 3 for j in range(1, n + 1)) / s.prod(
    (t + k + s.Rational(1, 2)) ** 3 for k in range(n + 1)
)
nodes, data = [], []
for k in range(m):
    rho = -k - s.Rational(1, 2)
    x = rho + m
    local = s.prod((rho + eps + j) ** 3 for j in range(1, n + 1)) / s.prod(
        (rho + eps + h + s.Rational(1, 2)) ** 3
        for h in range(n + 1) if h != k
    )
    a3 = s.cancel(local.subs(eps, 0))
    g = s.cancel(s.diff(local, eps).subs(eps, 0) / a3)
    h = s.cancel(s.diff(local, eps, 2).subs(eps, 0) / (2 * a3))
    alpha = s.cancel((3 - g) / (4 * x))
    gamma = s.cancel(-alpha**2 - (h + 4*x*g*alpha + 2*alpha)/(4*x*x))
    nodes.append(x*x)
    data.append((a3, alpha, gamma))

polys = []
for i in range(m):
    ell = s.prod((w - nodes[j]) / (nodes[i] - nodes[j])
                 for j in range(m) if j != i)
    di = s.diff(ell, w).subs(w, nodes[i])
    ei = sum((nodes[i] - nodes[j])**-2 for j in range(m) if j != i)
    a3, alpha, gamma = data[i]
    u = alpha - 3*di
    v = gamma/2 - 3*di*alpha + (9*di**2 + 3*ei)/2
    p = s.Poly(s.expand(ell**3 * (1 + u*(w-nodes[i]) + v*(w-nodes[i])**2)), w)
    for k in range(m):
        expected = (1, data[k][1], data[k][2]) if i == k else (0, 0, 0)
        assert tuple(s.diff(p.as_expr(), w, r).subs(w, nodes[k])
                     for r in range(3)) == expected
    polys.append(p)

moments = [s.Rational(1, 2)]
for r in range(1, 2*(6*m-2)+1):
    moments.append(-sum(s.binomial(r, k)*moments[k] for k in range(r))/2)

def euler(poly):
    return sum(c * moments[power[0]] for power, c in poly.terms())

def head(k, power):
    return sum(s.Rational((-1)**v, (2*v+1)**power) for v in range(k))

sigma = (-1)**(m+1)
A, B = s.zeros(m), s.zeros(m)
for i in range(m):
    for j in range(i, m):
        F = s.cancel(R * polys[i].as_expr().subs(w, (t+m)**2)
                     * polys[j].as_expr().subs(w, (t+m)**2))
        num, den = s.fraction(F)
        H, rem = s.div(s.Poly(num, t), s.Poly(den, t))
        proper, finite_head = 0, 0
        if i == j:
            for k, c2 in [(i, 3*data[i][0]), (n-i, -3*data[i][0])]:
                c3 = data[i][0]
                proper += c3/(t+k+s.Rational(1,2))**3 + c2/(t+k+s.Rational(1,2))**2
                for order, c in [(3,c3), (2,c2)]:
                    finite_head += (-1)**k * 2**(order+2)*order*(order+1)*c*head(k,order+2)
        assert s.cancel(F-H.as_expr()-proper) == 0
        rho0 = euler(H.diff((t, 2))) - finite_head
        A[i,j] = A[j,i] = s.cancel(-sigma*rho0)
    B[i,i] = sigma*192*(-1)**i*data[i][0]

Q = s.Poly(s.cancel((A+Z*B).det()/B.det()), Z)
assert Q.LC() == 1 and Q.degree() == m
lcd = s.ilcm(*[s.denom(c) for c in Q.all_coeffs()])
primitive = s.Poly(Q.as_expr()*lcd, Z)
assert primitive.get_domain().is_ZZ
assert s.igcd(*[int(c) for c in primitive.all_coeffs()]) == 1

mp.mp.dps = 60
Y = 4*(5*mp.pi**5/1536) - 3*mp.dirichlet(4, [0,1,0,-1])
qval = mp.polyval([mp.mpf(str(c.p))/int(c.q) for c in Q.all_coeffs()], Y)
primitive_value = int(lcd)*qval
result = {
    "scope": "Only m=2; exact rational algebra plus unvalidated numerical diagnostics; no asymptotic inference.",
    "decision_use": "Check actual normalization and prioritize the remaining real-rate/content proof.",
    "m": m, "n": n,
    "p_i": [str(p.as_expr()) for p in polys],
    "A": [[str(A[i,j]) for j in range(m)] for i in range(m)],
    "B": [[str(B[i,j]) for j in range(m)] for i in range(m)],
    "Q_descending": [str(c) for c in Q.all_coeffs()],
    "minimal_lcd": str(lcd),
    "primitive_descending": [str(c) for c in primitive.all_coeffs()],
    "Y_numeric": mp.nstr(Y, 45),
    "Q_Y_numeric": mp.nstr(qval, 45),
    "primitive_Y_numeric": mp.nstr(primitive_value, 45),
    "log_abs_Q_Y_div_m2": mp.nstr(mp.log(abs(qval))/(m*m), 30),
    "log_abs_primitive_Y_div_m2": mp.nstr(mp.log(abs(primitive_value))/(m*m), 30),
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
