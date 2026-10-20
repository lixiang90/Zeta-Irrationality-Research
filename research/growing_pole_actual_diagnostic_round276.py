"""One exact m=2 check of the original source and the proposed R >= 0."""
import json
from pathlib import Path

import sympy as s

m = 2
n, N, M, count = 8*m, 8*m-1, 4*m-1, 2*m
x, a, z = s.symbols("x a z")

def b(r, value):
    return s.prod(h-value for h in range(r))/s.factorial(r)

lagrange = [
    s.prod((x-k)/s.Rational(j-k) for k in range(count) if k != j)
    for j in range(count)
]
polys = []
for i in range(m):
    r = N-i
    br = b(r, a)
    F = 0
    for j in range(count):
        k = j//2
        value = b(i, k)
        if j % 2 == 0:
            value -= b(r, s.Rational(j-1, 2))
        value /= 2
        derivative = -s.diff(br, a).subs(a, s.Rational(j-1, 2))/4
        ell = lagrange[j]
        eta = s.diff(ell, x).subs(x, j)
        F += value*(1-2*(x-j)*eta)*ell**2 + derivative*(x-j)*ell**2
    F = s.Poly(s.expand(F), x)
    coeff = [
        (-1)**h*sum((-1)**(h-t)*s.binomial(h, t)*F.eval(2*t+1)
                    for t in range(h+1))
        for h in range(M+1)
    ]
    v = sum(coeff[h]*z**(M-h) for h in range(M+1))
    polys.append(s.Poly(z**i+z**(4*m)*v, z))

# Verify the complete defining G5 system, not only its resulting product traces.
ac = [s.Rational(s.binomial(2*k, k), 4**k) for k in range(N+1)]
lc = [s.Integer(0)]+[s.Rational(1, k) for k in range(1, N+1)]
alc = [sum(ac[k-h]*lc[h] for h in range(k+1)) for k in range(N+1)]
families = [[s.Integer(k == 0) for k in range(N+1)],
            [v-s.Integer(k == 0) for k, v in enumerate(ac)], lc, alc]
for i, p in enumerate(polys):
    u = p-s.Poly(z**i, z)
    for j in range(m):
        for index, fc in enumerate(families):
            left = sum(c*fc[N-j-degree] for (degree,), c in u.terms()
                       if degree <= N-j)
            right = (s.Rational(int(i == j), 2) if index == 0
                     else -fc[N-i-j]/2)
            assert s.cancel(left-right) == 0, (i, j, index, left, right)

# Full pole moments: [rational, zeta(2), G, log(2), pi].
proper = {1: (s.Integer(0), s.Integer(1), s.Integer(2), s.Integer(0), s.Integer(0))}
states = {value: [s.Integer(1), s.Integer(0), s.Integer(0), s.Integer(0)]
          for value in (s.Integer(1), s.Rational(1, 2))}
for j in range(2, n+1):
    for value, state in states.items():
        f, fp, u, up = state
        factor = 1-value/(j-1)
        states[value] = [factor*f, factor*fp-f/(j-1),
                         factor*u+s.Rational(1, 2**(j-1)*(j-1)),
                         factor*up-u/(j-1)]
    f1, fp1, u1, up1 = states[s.Integer(1)]
    fh, fph, uh, uph = states[s.Rational(1, 2)]
    proper[j] = (-2*up1-uph/2, f1, 2*fh, -2*fp1, -fph/4)

R = s.zeros(m)
period_columns = []
for i in range(m):
    row = []
    for j in range(m):
        vector = [s.Integer(0)]*5
        product = polys[i]*polys[j]
        for (degree,), c in product.terms():
            if degree < n:
                moments = proper[n-degree]
            else:
                power = degree-n
                rational = sum(s.binomial(power, h)*
                               (s.Rational(2, (h+1)**2)+
                                s.Rational(2, (2*h+1)**2))
                               for h in range(power+1))
                moments = (rational, 0, 0, 0, 0)
            vector = [s.cancel(v+c*w) for v, w in zip(vector, moments)]
        expected = [s.Integer(i == j), 2*s.Integer(i == j), 0, 0]
        assert vector[1:] == expected, (i, j, vector)
        R[i, j] = vector[0]
        row.append([str(c) for c in vector[1:]])
    period_columns.append(row)
assert R == R.T
result = {
    "scope": "Only m=2, exact rational reconstruction; no asymptotic inference.",
    "decision_use": "Test R positive semidefinite as a possible full-scale obstruction.",
    "m": m,
    "p_i": [str(p.as_expr()) for p in polys],
    "R": [[str(R[i, j]) for j in range(m)] for i in range(m)],
    "period_columns_zeta2_G_log2_pi": period_columns,
    "leading_principal_minors": [str(R[:k, :k].det()) for k in range(1, m+1)],
    "leading_principal_signs": [int(s.sign(R[:k, :k].det())) for k in range(1, m+1)],
}
Path(__file__).with_suffix(".json").write_bytes(
    (json.dumps(result, ensure_ascii=False, indent=2)+"\n").encode("utf-8")
)
print(json.dumps(result, ensure_ascii=False, indent=2))
