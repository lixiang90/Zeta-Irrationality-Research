"""One bounded exact quotient-algebra certificate; no sequence sampling.

Scope fixed before execution: degree-six g(u), p=-(1+2/u)^9,
the six-by-seven power matrix, all maximal cofactors and its monic
annihilating polynomial.  Uses only Fraction arithmetic and writes one JSON.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def trim(a):
    a = list(map(F, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [F(0)] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return trim(c)


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i + j] += v * w
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        i = len(a) - len(b)
        v = a[-1] / b[-1]
        q[i] += v
        for j, w in enumerate(b):
            a[i + j] -= v * w
        a = trim(a)
    return trim(q), trim(a)


def gcd(a, b):
    while trim(b) != [0]:
        a, b = b, divrem(a, b)[1]
    a = trim(a)
    return [v / a[-1] for v in a]


def deriv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def det(a):
    a = [list(row) for row in a]
    v = F(1)
    for j in range(len(a)):
        i = next((i for i in range(j, len(a)) if a[i][j]), None)
        if i is None:
            return F(0)
        if i != j:
            a[i], a[j] = a[j], a[i]
            v = -v
        pivot = a[j][j]
        v *= pivot
        for i in range(j + 1, len(a)):
            c = a[i][j] / pivot
            for k in range(j + 1, len(a)):
                a[i][k] -= c * a[j][k]
            a[i][j] = F(0)
    return v


g = mul([1, -2, -2], [1, -4, 0, 2, 1])
assert g == [1, -6, 6, 10, -3, -6, -2]
assert gcd(g, deriv(g)) == [1]
inv_u = [-v for v in g[1:]]
assert divrem(mul([0, 1], inv_u), g)[1] == [1]
V = add([1], [2 * v for v in inv_u])


def qmul(a, b):
    return divrem(mul(a, b), g)[1]


p = [F(1)]
for _ in range(9):
    p = qmul(p, V)
p = [-v for v in p]
powers = [[F(1)]]
for _ in range(6):
    powers.append(qmul(powers[-1], p))
M = [[powers[j][i] if i < len(powers[j]) else F(0)
      for j in range(7)] for i in range(6)]
cofactors = [(-1) ** j * det([[row[k] for k in range(7) if k != j]
                              for row in M]) for j in range(7)]
assert all(cofactors)
chi = [v / cofactors[-1] for v in cofactors]
assert chi[-1] == 1
assert all(sum(M[i][j] * cofactors[j] for j in range(7)) == 0
           for i in range(6))
assert gcd(chi, deriv(chi)) == [1]
check = [F(0)]
for j in range(7):
    check = add(check, [chi[j] * v for v in powers[j]])
assert check == [0]

linear = [19683, 1]
trace_previous, trace_current = F(2), F(6)
for _ in range(2, 10):
    trace_previous, trace_current = trace_current, 6 * trace_current + 3 * trace_previous
quadratic = [-19683, trace_current, 1]
known = mul(linear, quadratic)
cubic, rem = divrem(chi, known)
assert rem == [0] and len(cubic) == 4 and cubic[-1] == 1
assert mul(known, cubic) == chi

# Independent factor certificate on each V-factor, rather than a root scan.
V_factors = [[-3, -6, 1], [-3, 1], [-3, 3, -9, 1]]
q_factors = [quadratic, linear, cubic]
factor_checks = []
for vf, qf in zip(V_factors, q_factors):
    raw = [F(0)]
    for j, c in enumerate(qf):
        term = [F(0)] * (9 * j + 1)
        term[9 * j] = c * (-1) ** j
        raw = add(raw, term)
    remainder = divrem(raw, vf)[1]
    assert remainder == [0]
    factor_checks.append(remainder)


def encoded(x):
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else str(x)
    if isinstance(x, list):
        return [encoded(v) for v in x]
    if isinstance(x, dict):
        return {k: encoded(v) for k, v in x.items()}
    return x


out = {
    "scope": "Fixed degree-six quotient algebra; successful repaired execution after one recorded failed execution; no sequence values, scans or recurrence guessing.",
    "coefficient_order": "ascending powers",
    "g_u": g,
    "inverse_u_mod_g": inv_u,
    "V_mod_g": V,
    "p_minus_V_power9_mod_g": p,
    "power_remainders_j0_through6": powers,
    "power_matrix_6_by7": M,
    "signed_maximal_cofactors": cofactors,
    "monic_characteristic_polynomial": chi,
    "factors": {"linear": linear, "quadratic": quadratic, "cubic": cubic},
    "factor_substitution_remainders": factor_checks,
    "checks": {"all_seven_cofactors_nonzero": True,
               "cofactor_kernel_exact": True,
               "chi_of_p_zero_mod_g": True,
               "g_squarefree": True, "chi_squarefree": True,
               "factor_product_exact": True},
}
path = Path(__file__).with_name("pade_leading_symbol_certificate_round225_20261008.json")
path.write_text(json.dumps(encoded(out), indent=2) + "\n", encoding="utf-8")
print(json.dumps({"output": str(path), "characteristic": encoded(chi),
                  "cubic_factor": encoded(cubic), "checks": out["checks"]}))
