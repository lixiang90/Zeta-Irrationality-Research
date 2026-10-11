"""DISTINCT 20261007 FIRST1 rational inequalities; no old/peer imports.

The proof is in the accompanying NEW Markdown.  This program certifies only
the finitely many real inequalities used there, using Fraction series with
explicit remainders.  It is not a determinant/nonzero/prime experiment.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve()
GUARD = HERE.with_name(HERE.stem + '_guard.json')
OUTPUT = HERE.with_suffix('.json')
with GUARD.open('x', encoding='utf-8') as handle:
    json.dump({'state': 'STARTED_FIRST1', 'producer': HERE.name,
               'rerun_forbidden': True}, handle, indent=2)
if OUTPUT.exists():
    raise RuntimeError('existing output: FIRST1 only, never rerun')


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __rsub__(self, other):
        return I(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        values = [self.lo * other.lo, self.lo * other.hi,
                  self.hi * other.lo, self.hi * other.hi]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo * other.hi > 0
        return self * I(F(1) / other.hi, F(1) / other.lo)


N = 72


def small_atan(x):
    x = F(x)
    assert abs(x) <= F(1, 2)
    if x < 0:
        return -small_atan(-x)
    value = sum(((-1)**j * x**(2*j + 1) / (2*j + 1)
                 for j in range(N)), F(0))
    error = x**(2*N + 1) / (2*N + 1)
    return I(value - error, value + error)


PI = 16 * small_atan(F(1, 5)) - 4 * small_atan(F(1, 239))


def atan_point(x):
    x = F(x)
    if x < 0:
        return -atan_point(-x)
    if x > 1:
        return PI / 2 - atan_point(F(1) / x)
    if x > F(1, 2):
        return PI / 4 + small_atan((x - 1) / (x + 1))
    return small_atan(x)


def atan(x):
    x = x if isinstance(x, I) else I(x)
    return I(atan_point(x.lo).lo, atan_point(x.hi).hi)


def atanh_log_point(x):
    assert F(1) <= x <= F(2)
    z = (x - 1) / (x + 1)
    value = 2 * sum((z**(2*j + 1) / (2*j + 1)
                     for j in range(N)), F(0))
    tail = 2 * z**(2*N + 1) / ((2*N + 1) * (1-z*z))
    return I(value, value + tail)


LOG2 = atanh_log_point(F(2))


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
    return atanh_log_point(x) + exponent * LOG2


def log(x):
    x = x if isinstance(x, I) else I(x)
    assert x.lo > 0
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


left, right = F(1), F(2)
for _ in range(90):
    middle = (left + right) / 2
    if middle * middle < 2:
        left = middle
    else:
        right = middle
SQRT2 = I(left, right)


def J(A, y):
    y = y if isinstance(y, I) else I(y)
    return F(A, 2) * log(A*A + y*y) - A + y * atan(I(A) / y)


def Q(y):
    y = y if isinstance(y, I) else I(y)
    return (12*log(6)-6*LOG2-6 + 7*J(2, y)-2*J(8, y)-2*PI*y)


def Qprime(y):
    return 7*atan(I(2)/I(y))-2*atan(I(8)/I(y))-2*PI


def rounded(x):
    scale = 10**12
    lo = x.lo.numerator * scale // x.lo.denominator
    hi = -((-x.hi.numerator * scale) // x.hi.denominator)
    return {'lo_numerator': lo, 'hi_numerator': hi,
            'denominator': scale}


quarter, half, one, root = Q(F(1, 4)), Q(F(1, 2)), Q(1), Q(SQRT2)
comparisons = {
    'Qhalf_minus_Qquarter_minus_1over20': half-quarter-F(1,20),
    'Qhalf_minus_Qone_minus_1over20': half-one-F(1,20),
    'Qhalf_minus_Qsqrt2_minus_log3_minus_1over20': half-root-log(3)-F(1,20),
    'minus_log15over16_minus_1over20': -log(F(15,16))-F(1,20),
    'Qprime_quarter_positive': Qprime(F(1,4)),
    'minus_Qprime_one_positive': -Qprime(1),
    'minus_Qprime_two_minus_4over3_positive': -Qprime(2)-F(4,3),
    'pi_minus_3_positive': PI-3,
}
for name, interval in comparisons.items():
    assert interval.lo > 0, (name, rounded(interval))

result = {
    'state': 'PASS_FIRST1', 'scope': '8 rational real inequalities only',
    'old_peer_execution_import_rerun': 0,
    'finite_determinant_prime_cases': 0,
    'producer_sha256': hashlib.sha256(HERE.read_bytes()).hexdigest(),
    'series_terms': N, 'sqrt2_bisections': 90,
    'certified_gain': '1/20',
    'values': {name: rounded(value) for name, value in {
        'Qquarter':quarter, 'Qhalf':half, 'Qone':one, 'Qsqrt2':root,
        'pi':PI, 'sqrt2':SQRT2}.items()},
    'strict_positive_comparisons': {name:rounded(value)
                                    for name,value in comparisons.items()},
    'limitations': ['No determinant lower bound or target nonzero claim.',
                    'No odd zeta/L irrationality theorem.',
                    'Global/all-n estimates are paper proofs, not this finite certificate.'],
}
with OUTPUT.open('x', encoding='utf-8') as handle:
    json.dump(result, handle, ensure_ascii=False, indent=2)
print(json.dumps(result, ensure_ascii=False, indent=2))
