"""New bounded-source algebra certificate; no prime or target-number scan."""
from pathlib import Path
import json
import sympy as s

T = s.symbols("t")
theta = lambda value: s.expand(T * s.diff(value, T))
labels = []


def check(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    labels.append(label)


f = s.Function("f")(T)
j = s.Function("j")(T)
q = s.Function("qproj")(T)
m = s.Function("m")(T)
b2 = -3 * j
b1 = 3 * (j**2 - theta(j)) + 4 * q
b0 = -j**3 + 3 * j * theta(j) - theta(theta(j)) - 4 * q * j + 2 * theta(q)


def power_theta(value, n):
    for _ in range(n):
        value = theta(value)
    return value


def euler(value):
    return power_theta(value, 3) + b2 * power_theta(value, 2) + b1 * theta(value) + b0 * value


def shifted(value):
    return theta(value) - j * value


gauge_action = shifted(shifted(shifted(f))) + 4 * q * shifted(f) + 2 * theta(q) * f
check("Euler gauge identity (S11)", s.expand(gauge_action - euler(f)) == 0)

composite = (
    m * power_theta(f, 4)
    + (3 * theta(m) + b2 * m) * power_theta(f, 3)
    + (3 * power_theta(m, 2) + 2 * b2 * theta(m) + b1 * m) * power_theta(f, 2)
    + (power_theta(m, 3) + b2 * power_theta(m, 2) + b1 * theta(m) + b0 * m) * theta(f)
)
check("Composite right-factor expansion (S15)", s.expand(euler(m * theta(f)) - composite) == 0)
check("Zeroth coefficient is identically zero", s.expand(composite).coeff(f) == 0)

# Generic polynomials verify the degree recurrence before cancellations.
dpoly = sum(s.symbols(f"D0:6")[i] * T**i for i in range(6))
for d in range(6):
    coefficients = s.symbols(f"P0:{d + 1}")
    ppoly = sum(coefficients[i] * T**i for i in range(d + 1))
    numerator = dpoly
    for order in range(4):
        check(
            f"Generic derivative numerator degree d={d} j={order}",
            s.Poly(numerator, T).degree() <= 5 + order * d,
        )
        cleared_numerator = s.expand(numerator * ppoly ** (3 - order))
        check(
            f"Cleared numerator degree d={d} j={order}",
            s.Poly(cleared_numerator, T).degree() <= 5 + 3 * d,
        )
        numerator = s.expand(theta(numerator) * ppoly - (order + 1) * numerator * theta(ppoly))

# Fixed model factors and rational degree bookkeeping, without an old producer.
root = s.sqrt(5)
cm = 1 - (6 - 2 * root) * T + (6 - 2 * root) * T**2
cp = 1 - (6 + 2 * root) * T + (6 + 2 * root) * T**2
nm = 1 - (6 + root) * T + (1 + root) * T**2
np = 1 - (6 - root) * T + (1 - root) * T**2
delta = s.expand(cm * cp)
check("Delta product is the fixed rational quartic", s.expand(delta - (1 - 12*T + 28*T**2 - 32*T**3 + 16*T**4)) == 0)
for name, own, opp, n in (("minus", cm, cp, nm), ("plus", cp, cm, np)):
    lam = s.expand((1 - T) * n * opp)
    den = s.expand((1 - T) * n * own)
    check(f"{name} lambda degree five", s.Poly(lam, T).degree() == 5)
    check(f"{name} D degree five", s.Poly(den, T).degree() == 5)
    check(f"{name} clearing B degree twenty-seven", 3*s.Poly(lam, T).degree() + 3*s.Poly(delta, T).degree() == 27)
    check(f"{name} B and D constant one", lam.subs(T, 0) == den.subs(T, 0) == delta.subs(T, 0) == 1)

check("All cleared coefficients have degree at most 47", all(27 + max(5 + 3*d, 4*d) <= 47 for d in range(6)))

# Independent matching in the actual four-symbol connection.
r0, r1, r2, r3 = [s.Function(f"r{i}")(T) for i in range(4)]
k0, k1, k2 = s.symbols("K K1 K2")
u = s.Function("Ubar")(T)
formal_derivative = (
    theta(r0)
    + theta(r1)*k0 + r1*k1
    + theta(r2)*k1 + r2*k2
    + theta(r3)*k2 + r3*(u - b0*k0 - b1*k1 - b2*k2)
)
expected = (
    theta(r0) + u*r3
    + (theta(r1) - b0*r3)*k0
    + (r1 + theta(r2) - b1*r3)*k1
    + (r2 + theta(r3) - b2*r3)*k2
)
check("Four rational-exactness equations (S20)", s.expand(formal_derivative - expected) == 0)

payload = {
    "scope": "New symbolic Euler/right-factor/degree certificate only; no prime sample, no p-adic lift, no Smith or rank theorem certified by computation.",
    "checks_passed": len(labels),
    "check_labels": labels,
    "operator_order": 4,
    "slow_polynomial_degree_bound": 47,
    "requires_mathematical_proof": [
        "Actual L3 H=U and L3 A=0",
        "All-good-prime Cartier kernel and integral prefix",
        "B clears all Euler coefficients and forcing",
        "Actual rank4 and right-factor pullback interpretation",
        "Any new mixed integral-coordinate Smith gain",
    ],
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"checks_passed": len(labels), "certificate": str(destination)}, ensure_ascii=False))
