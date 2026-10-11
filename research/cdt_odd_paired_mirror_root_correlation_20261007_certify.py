"""One DISTINCT guarded FIRST1: elementary closed-cell mirror/root bound.

Only independent stdlib Fraction arithmetic is used. No old or peer source,
saved certificate, determinant, prime, or unit-table input is read or executed.
The explicit c(q), P(q) formulas are mathematical inputs from the frozen paper.
All 4096 closed cells are covered by signed interval arithmetic. No sample is
used to establish the global lower bound. Success or failure is preserved.
"""
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
GUARD = HERE.with_name(HERE.stem + '_guard.json')
SOURCE_SHA = hashlib.sha256(HERE.read_bytes()).hexdigest()
with GUARD.open('x', encoding='utf-8') as handle:
    json.dump({'state': 'STARTED_FIRST1', 'source_sha256': SOURCE_SHA,
               'created_utc': datetime.now(timezone.utc).isoformat(),
               'rerun_forbidden': True,
               'scope': 'Elementary c(q)+P(q)+7q^2/9 complete closed-cell lower envelope only'},
              handle, indent=2)


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


def scale(a, value):
    return mul(a, point(value))


TERMS = 24
CELLS = 4096


def log_core(x):
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    total, power = F(0), z
    for k in range(TERMS):
        total += power / (2 * k + 1)
        power *= z * z
    remainder = 2 * power / ((2 * TERMS + 1) * (1 - z * z))
    return (2 * total, 2 * total + remainder)


LOG2 = log_core(F(2))


@lru_cache(maxsize=None)
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
    return add(log_core(x), scale(LOG2, exponent))


@lru_cache(maxsize=None)
def f_point(x):
    x = F(x)
    if x == 0:
        return point(0)
    assert x > 0
    return sub(scale(log_point(x), x * x / 2), point(3 * x * x / 4))


@lru_cache(maxsize=None)
def fp_point(x):
    x = F(x)
    if x == 0:
        return point(0)
    assert x > 0
    return sub(scale(log_point(x), x), point(x))


def f01(a):
    # f'=x(log x-1)<=0 on [0,1]; zero is its continuous value.
    assert 0 <= a[0] <= a[1] <= 1
    return (f_point(a[1])[0], f_point(a[0])[1])


def fp01(a):
    # f''=log x<=0 on (0,1]; f'(0)=0 by continuity.
    assert 0 <= a[0] <= a[1] <= 1
    return (fp_point(a[1])[0], fp_point(a[0])[1])


def f14(a):
    # f' is increasing on [1,4]; its absolute maximum on a cell
    # is bounded by the interval enclosures of its two endpoints.
    assert 1 <= a[0] <= a[1] <= 4
    left, right = fp_point(a[0]), fp_point(a[1])
    lipschitz = max(abs(left[0]), abs(left[1]), abs(right[0]), abs(right[1]))
    midpoint = (a[0] + a[1]) / 2
    halfwidth = (a[1] - a[0]) / 2
    middle = f_point(midpoint)
    return (middle[0] - lipschitz * halfwidth,
            middle[1] + lipschitz * halfwidth)


F1, F2, F3, F7 = (f_point(F(k)) for k in (1, 2, 3, 7))


def c_cell(q):
    one_minus_q = sub(point(1), q)
    ll = add(add(sub(f14(sub(point(2), q)), scale(F1, 4)),
                 scale(f01(q), 3)),
             scale(mul(one_minus_q, fp01(q)), 2))
    hh = add(add(add(sub(f14(add(point(3), q)), scale(F3, 2)),
                     f14(sub(point(3), q))),
                 scale(F1, -2)),
             add(scale(f01(one_minus_q), 2),
                 scale(mul(q, fp01(one_minus_q)), 2)))
    lh = scale(add(add(add(sub(f14(sub(point(3), q)), scale(F2, 2)),
                          neg(f14(sub(point(3), scale(q, 2))))),
                      scale(f14(sub(point(2), q)), 2)),
                   sub(f14(add(point(1), q)), F1)), 2)
    return add(add(ll, hh), lh)


@lru_cache(maxsize=None)
def P_point(q):
    q = F(q)
    return scale(add(add(sub(add(f_point(7 + q), f_point(7 - q)), scale(F7, 2)),
                         neg(add(f_point(1 + q), f_point(1 - q)))),
                     scale(F1, 2)), 2)


def d_cell(lo, hi):
    # P(q) is increasing and nonnegative on [0,1], by the paper's
    # P'=2[B(1+q)-B(1-q)]>=0 and B'>0. 7q^2/9 is also increasing.
    c = c_cell((lo, hi))
    plo = max(F(0), P_point(lo)[0])
    phi = max(F(0), P_point(hi)[1])
    return (c[0] + plo + F(7, 9) * lo * lo,
            c[1] + phi + F(7, 9) * hi * hi)


def outward(a, digits=12):
    denominator = 10 ** digits
    low_value, high_value = a[0] * denominator, a[1] * denominator
    lower = low_value.numerator // low_value.denominator
    upper = -((-high_value.numerator) // high_value.denominator)
    assert F(lower, denominator) <= a[0] <= a[1] <= F(upper, denominator)
    return {'lower_num': lower, 'upper_num': upper, 'denominator': denominator}


try:
    cells = []
    smallest_lower = None
    smallest_lower_index = None
    for index in range(CELLS):
        lo, hi = F(index, CELLS), F(index + 1, CELLS)
        bounds = d_cell(lo, hi)
        assert bounds[0] <= bounds[1]
        cells.append({'index': index, 'lo': str(lo), 'hi': str(hi),
                      'bounds': outward(bounds)})
        if smallest_lower is None or bounds[0] < smallest_lower:
            smallest_lower, smallest_lower_index = bounds[0], index
    assert len(cells) == CELLS
    assert cells[0]['lo'] == '0' and cells[-1]['hi'] == '1'
    assert smallest_lower > F(43, 50)
    sample = F(2 * smallest_lower_index + 1, 2 * CELLS)
    sample_bounds = d_cell(sample, sample)
    result = {
        'state': 'PASS_FIRST1', 'source_sha256': SOURCE_SHA,
        'scope': 'Elementary c(q)+P(q)+7q^2/9 global lower bound over all q in [0,1]',
        'cell_count': CELLS, 'closed_cell_cover': True,
        'log_series_terms': TERMS,
        'threshold': '43/50',
        'global_minimum': outward((smallest_lower, sample_bounds[1])),
        'minimum_lower_cell_index': smallest_lower_index,
        'sample_for_global_upper_only': str(sample),
        'cells': cells,
        'limitations': [
            'Whole-cell lower enclosures, not point sampling, prove the elementary global lower bound',
            'All-n mirror/root fee transfer and atanh root penalty are separate paper proofs',
            'No primes, determinant values, unit ranks, infinite nonzero or arithmetic margin tested',
            'No old or peer mathematical producer or certificate input read, imported or executed',
            'No new numerical irrationality or linear-independence theorem or Lean formalization'
        ]
    }
    with OUT.open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
    print(json.dumps({key: value for key, value in result.items() if key != 'cells'}, indent=2))
except BaseException as error:
    if not OUT.exists():
        with OUT.open('x', encoding='utf-8') as handle:
            json.dump({'state': 'FAILED_FIRST1', 'source_sha256': SOURCE_SHA,
                       'error_type': type(error).__name__, 'error': str(error),
                       'rerun_allowed': False}, handle, indent=2)
    raise
