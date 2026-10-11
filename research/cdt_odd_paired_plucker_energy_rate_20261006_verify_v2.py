"""NEW v2 first-execution-only rational interval certificate for scalar constants.

The separate v1 first execution passed its mathematical assertions, then failed
at Python huge-integer serialization. V1 is preserved and never rerun.

No old or peer producer imports. This checks constants, not the all-n proof,
the actual determinant's nonvanishing, or an arithmetic comparison margin.
"""
from fractions import Fraction as F
from pathlib import Path
import json

N = 80


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(x, a):
    a = F(a)
    return (a * x[0], a * x[1]) if a >= 0 else (a * x[1], a * x[0])


def atan_small(x):
    x = F(x)
    if x < 0:
        return scale(atan_small(-x), -1)
    assert 0 <= x <= F(1, 2)
    value = sum(((-1)**k * x**(2*k+1) / (2*k+1) for k in range(N)), F(0))
    next_term = x**(2*N+1) / (2*N+1)
    # N even: partial sum ends with a negative term.
    return value, value + next_term


PI = add(scale(atan_small(F(1, 5)), 16), scale(atan_small(F(1, 239)), -4))


def atan(x):
    x = F(x)
    if x < 0:
        return scale(atan(-x), -1)
    if x > 1:
        return add(scale(PI, F(1, 2)), scale(atan(1/x), -1))
    if x > F(1, 2):
        return add(scale(PI, F(1, 4)), atan_small((x-1)/(x+1)))
    return atan_small(x)


def log_reduced(x):
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    value = 2*sum((z**(2*k+1)/(2*k+1) for k in range(N)), F(0))
    remainder = 2*z**(2*N+1)/((2*N+1)*(1-z*z))
    return value, value + remainder


LOG2 = log_reduced(F(2))


def log(x):
    x = F(x)
    assert x > 0
    k = 0
    while x < 1:
        x *= 2
        k -= 1
    while x > 2:
        x /= 2
        k += 1
    return add(log_reduced(x), scale(LOG2, k))


def J(A, y):
    A, y = F(A), F(y)
    if y == 0:
        return add(scale(log(A), A), (-A, -A))
    return add(add(scale(log(A*A+y*y), A/2), (-A, -A)), scale(atan(A/y), y))


C0 = add(add(scale(log(6), 12), scale(LOG2, -6)), (-F(6), -F(6)))


def Q(y):
    return add(add(add(C0, scale(J(2, y), 7)), scale(J(8, y), -2)), scale(PI, -2*y))


def derivative(y, extra):
    ans = add(add(scale(atan(2/y), 7), scale(atan(8/y), -2)), scale(PI, -2))
    if extra:
        q = 2*y/(1+y*y)
        ans = add(ans, (q, q))
    return ans


def bracket(extra):
    lo, hi = F(0), F(1)
    assert derivative(hi, extra)[1] < 0
    for _ in range(72):
        mid = (lo+hi)/2
        d = derivative(mid, extra)
        if d[0] > 0:
            lo = mid
        else:
            assert d[1] < 0
            hi = mid
    assert derivative(lo, extra)[0] > 0 > derivative(hi, extra)[1]
    return lo, hi


def Q_interval(y):
    lo, hi = y
    # J_A increases with y; interval operations keep every sign explicitly.
    return add(add(add(C0, scale((J(2, lo)[0], J(2, hi)[1]), 7)),
                   scale((J(8, lo)[0], J(8, hi)[1]), -2)),
               (-2*PI[1]*hi, -2*PI[0]*lo))


y0, y1 = bracket(False), bracket(True)
M0, M1 = Q_interval(y0), Q_interval(y1)
M1 = add(M1, (log(1+y1[0]**2)[0], log(1+y1[1]**2)[1]))
C_basis = add(add(add(scale(LOG2, 176), scale(log(3), -21)), scale(log(7), -49)),
              (F(15, 2), F(15, 2)))
beta = scale(add(add(add(M0, M1), scale(LOG2, F(1, 2))), C_basis), -1)
assert beta[0] > F(7)
assert beta[1] < F(8)


def serialize(interval):
    # Outward rounding is exact; never serialize the huge internal numerators.
    decimal_den = 10**14
    lo = F((interval[0].numerator*decimal_den)//interval[0].denominator, decimal_den)
    hi = F(-((-interval[1].numerator*decimal_den)//interval[1].denominator), decimal_den)
    assert lo <= interval[0] <= interval[1] <= hi
    return {"lower": str(lo), "upper": str(hi),
            "approx_lower": float(lo), "approx_upper": float(hi)}


result = {
    "status": "PASS",
    "scope": "Exact rational intervals for two scalar saddle constants and beta0 only.",
    "execution_count": 1,
    "prior_failed_new_producer_runs": 1,
    "prior_failed_source": "cdt_odd_paired_plucker_energy_rate_20261006_verify.py",
    "prior_failure": "Python huge-integer serialization after mathematical assertions; v1 never rerun",
    "old_or_peer_math_import_execute_rerun": 0,
    "external_lean": 0,
    "series_terms": N,
    "root_bisections_each": 72,
    "pi": serialize(PI),
    "y0": serialize(y0), "y1": serialize(y1),
    "M0": serialize(M0), "M1": serialize(M1),
    "basis_constant": serialize(C_basis),
    "beta0": serialize(beta),
    "proved_constant_checks": ["0<y0<1", "0<y1<1", "7<beta0<8"],
    "not_proved_by_script": ["all-n determinant bound", "infinite nonzero", "arithmetic margin"]
}
target = Path(__file__).with_suffix(".json")
assert not target.exists(), "FIRST ONLY: refuse replacement or rerun"
target.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ("status", "y0", "y1", "beta0")}, indent=2))


