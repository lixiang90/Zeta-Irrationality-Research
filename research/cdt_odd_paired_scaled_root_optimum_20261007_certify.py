"""DISTINCT guarded FIRST1: elementary constants for the scaled-root paper.

No old or peer source is executed/imported/read. This does not test determinants,
primes, or the all-n theorem. The successful or failed source/output/guard is kept.
"""
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
GUARD = HERE.with_name(HERE.stem + '_guard.json')
SOURCE_SHA = hashlib.sha256(HERE.read_bytes()).hexdigest()
with GUARD.open('x', encoding='utf-8') as handle:
    json.dump({'state': 'STARTED_FIRST1', 'source_sha256': SOURCE_SHA,
               'created_utc': datetime.now(timezone.utc).isoformat(),
               'scope': 'Elementary scaled-root real intervals only; no prime/determinant tests'}, handle, indent=2)

def point(x):
    x = F(x)
    return (x, x)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def neg(a):
    return (-a[1], -a[0])

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    values = [a[i] * b[j] for i in (0, 1) for j in (0, 1)]
    return (min(values), max(values))

def div(a, b):
    assert b[0] * b[1] > 0
    return mul(a, (1 / b[1], 1 / b[0]))

def sq(a):
    if a[0] <= 0 <= a[1]:
        return (F(0), max(a[0] ** 2, a[1] ** 2))
    return (min(a[0] ** 2, a[1] ** 2), max(a[0] ** 2, a[1] ** 2))

TERMS = 96

def atan_small(x):
    assert abs(x) <= F(1, 2)
    if x < 0:
        return neg(atan_small(-x))
    power = x
    total = F(0)
    for k in range(TERMS):
        total += (-1) ** k * power / (2 * k + 1)
        power *= x * x
    next_term = power / (2 * TERMS + 1)
    return (total, total + next_term)  # TERMS even: next term positive

PI = sub(mul(point(16), atan_small(F(1, 5))),
         mul(point(4), atan_small(F(1, 239))))

def atan_point(x):
    x = F(x)
    if x < 0:
        return neg(atan_point(-x))
    if x > 1:
        return sub(div(PI, point(2)), atan_point(1 / x))
    if x > F(1, 2):
        return add(div(PI, point(4)), atan_small((x - 1) / (x + 1)))
    return atan_small(x)

def atan(a):
    return (atan_point(a[0])[0], atan_point(a[1])[1])

def log_core(x):
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    total, power = F(0), z
    for k in range(TERMS):
        total += power / (2 * k + 1)
        power *= z * z
    tail = 2 * power / ((2 * TERMS + 1) * (1 - z * z))
    return (2 * total, 2 * total + tail)

LOG2 = log_core(F(2))

def log_point(x):
    x = F(x)
    assert x > 0
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x > 2:
        x /= 2
        exponent += 1
    return add(log_core(x), mul(point(exponent), LOG2))

def log(a):
    assert a[0] > 0
    return (log_point(a[0])[0], log_point(a[1])[1])

def sqrt_point(x):
    x = F(x)
    lo, hi = F(0), max(F(1), x)
    for _ in range(90):
        mid = (lo + hi) / 2
        if mid * mid < x:
            lo = mid
        else:
            hi = mid
    return (lo, hi)

def Qprime(y):
    # Exact identity valid also at y=0; avoids singular atan(A/y).
    return add(sub(div(PI, point(2)), mul(point(7), atan(div(y, point(2))))),
               mul(point(2), atan(div(y, point(8)))))

def JA(A, y):
    assert y[0] > 0
    return add(sub(mul(point(F(A, 2)), log(add(point(A * A), sq(y)))), point(A)),
               mul(y, atan(div(point(A), y))))

CONSTANT = sub(sub(mul(point(12), log_point(6)), mul(point(6), LOG2)), point(6))

def Q(y):
    assert y[0] > 0
    return sub(add(CONSTANT, sub(mul(point(7), JA(2, y)), mul(point(2), JA(8, y)))), mul(mul(point(2), PI), y))

def I(s):
    root = sqrt_point(s)
    return add(sub(log_point(1 + s), point(2)),
               mul(root, sub(PI, mul(point(2), atan(root)))))

def enclose_decreasing_root(function, lo, hi, steps=34):
    lo, hi = F(lo), F(hi)
    assert function(point(lo))[0] > 0
    assert function(point(hi))[1] < 0
    for _ in range(steps):
        mid = (lo + hi) / 2
        value = function(point(mid))
        if value[0] > 0:
            lo = mid
        elif value[1] < 0:
            hi = mid
        else:
            # Exact interval uncertainty never permits an invalid sign decision.
            break
    return (lo, hi)

def peak_pair(s, steps=34):
    assert F(1, 2) <= s <= F(7, 10)
    left = enclose_decreasing_root(lambda y: sub(Qprime(y), div(mul(point(2), y), sub(point(s), sq(y)))), 0, F(1, 2), steps)
    right = enclose_decreasing_root(lambda y: add(Qprime(y), div(mul(point(2), y), sub(sq(y), point(s)))), 1, 2, steps)
    L = add(Q(left), log(sub(point(s), sq(left))))
    R = add(Q(right), log(sub(sq(right), point(s))))
    return left, right, L, R

def outward(a, digits=12):
    den = 10 ** digits
    low = (a[0] * den).numerator // (a[0] * den).denominator
    upper_value = a[1] * den
    high = -((-upper_value.numerator) // upper_value.denominator)
    assert F(low, den) <= a[0] <= a[1] <= F(high, den)
    return {'lower_num': low, 'upper_num': high, 'denominator': den}

try:
    s = F(4, 7)
    quarter, half, four_thirds = point(F(1, 4)), point(F(1, 2)), point(F(4, 3))
    cL, cR = F(121, 20), F(1403, 612)
    dL = sub(Qprime(quarter), point(F(56, 57)))
    dR = add(Qprime(four_thirds), point(F(42, 19)))
    left_upper = add(add(Q(quarter), log_point(F(57, 112))), div(sq(dL), point(2 * cL)))
    right_upper = add(add(Q(four_thirds), log_point(F(76, 63))), div(sq(dR), point(2 * cR)))
    head_integral = I(s)
    gain_left = add(sub(Q(half), left_upper), head_integral)
    gain_right = add(sub(Q(half), right_upper), head_integral)
    assert gain_left[0] > F(3, 5)
    assert gain_right[0] > F(3, 5)

    y0 = enclose_decreasing_root(Qprime, 0, 1, 40)
    M0 = Q(y0)
    left0, right0, L0, R0 = peak_pair(F(1, 2))
    left1, right1, L1, R1 = peak_pair(F(7, 10))
    assert sub(L0, R0)[1] < 0
    assert sub(L1, R1)[0] > 0
    slo, shi = F(1, 2), F(7, 10)
    steps_completed = 0
    for _ in range(18):
        mid = (slo + shi) / 2
        _, _, Lmid, Rmid = peak_pair(mid)
        difference = sub(Lmid, Rmid)
        if difference[1] < 0:
            slo = mid
        elif difference[0] > 0:
            shi = mid
        else:
            break
        steps_completed += 1
    _, _, Llo, Rlo = peak_pair(slo, 40)
    _, _, Lhi, Rhi = peak_pair(shi, 40)
    assert sub(Llo, Rlo)[1] < 0
    assert sub(Lhi, Rhi)[0] > 0
    Mstar = (max(Llo[0], Rhi[0]), min(Lhi[1], Rlo[1]))
    Istar = (I(slo)[0], I(shi)[1])
    gain_star = add(sub(M0, Mstar), Istar)
    a_range = (peak_pair(slo, 40)[0][0], peak_pair(shi, 40)[0][1])
    b_range = (peak_pair(slo, 40)[1][0], peak_pair(shi, 40)[1][1])
    assert gain_star[0] > F(3, 5)
    output = {
        'state': 'PASS_FIRST1', 'source_sha256': SOURCE_SHA,
        'scope': 'Elementary constants and unique single-scale crossing brackets; no determinant/prime experiments',
        'assertion_count': 7,
        's_fixed': '4/7', 'curvature_left': '121/20', 'curvature_right': '1403/612',
        'fixed_values': {name: outward(value) for name, value in {
            'Q_half': Q(half), 'left_upper': left_upper, 'right_upper': right_upper,
            'I_s': head_integral, 'gain_left': gain_left, 'gain_right': gain_right,
            'left_derivative_at_quarter': dL, 'right_derivative_at_four_thirds': dR}.items()},
        'optimum': {'s': outward((slo, shi)), 'a': outward(a_range), 'b': outward(b_range),
                    'M0': outward(M0), 'Mstar': outward(Mstar), 'Istar': outward(Istar),
                    'gain': outward(gain_star), 'outer_bisections_completed': steps_completed},
        'limitations': ['All-n determinant estimate and all-s unique-optimum theorem are paper proofs, not finite tests',
                        'Single-scale optimum is not the global optimum over multiple roots or actual complex phase',
                        'Original high/mirror/Gamma arithmetic-analytic fees remain paid once',
                        'No infinite determinant nonzero, auxiliary-unit, strict margin or irrationality theorem asserted']}
    with OUT.open('x', encoding='utf-8') as handle:
        json.dump(output, handle, indent=2)
    print(json.dumps(output, indent=2))
except BaseException as error:
    if not OUT.exists():
        with OUT.open('x', encoding='utf-8') as handle:
            json.dump({'state': 'FAILED_FIRST1', 'source_sha256': SOURCE_SHA,
                       'error_type': type(error).__name__, 'error': str(error),
                       'rerun_allowed': False}, handle, indent=2)
    raise
