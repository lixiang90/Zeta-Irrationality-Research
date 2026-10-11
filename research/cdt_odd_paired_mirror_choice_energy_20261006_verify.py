"""NEW FIRST-ONLY exact interval certificate for matched mirror-choice energy.

No old or peer producer imports/reads. Grid cells cover the entire real q
interval: each cell bound uses proved monotonicity or a uniform derivative
bound, not a sampled minimum. The all-n determinant proof is separate.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

TARGET = Path(__file__).with_suffix('.json')
assert not TARGET.exists(), 'FIRST ONLY: refuse replacement or rerun'
TERMS = 24
CELLS = 4096


def add(*intervals):
    return sum((v[0] for v in intervals), F(0)), sum((v[1] for v in intervals), F(0))


def scale(interval, coefficient):
    coefficient = F(coefficient)
    if coefficient >= 0:
        return coefficient*interval[0], coefficient*interval[1]
    return coefficient*interval[1], coefficient*interval[0]


def product(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


@lru_cache(None)
def reduced_log(x):
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    z2 = z*z
    term = z
    total = F(0)
    for k in range(TERMS):
        total += term/(2*k+1)
        term *= z2
    total *= 2
    remainder = 2*term/((2*TERMS+1)*(1-z2))
    return total, total+remainder


LOG2 = reduced_log(F(2))


@lru_cache(None)
def log(x):
    x = F(x)
    assert x > 0
    power = 0
    while x < 1:
        x *= 2
        power -= 1
    while x > 2:
        x /= 2
        power += 1
    return add(reduced_log(x), scale(LOG2, power))


@lru_cache(None)
def f_at(x):
    x = F(x)
    if x == 0:
        return F(0), F(0)
    return add(scale(log(x), x*x/2), (-3*x*x/4, -3*x*x/4))


@lru_cache(None)
def fp_at(x):
    x = F(x)
    if x == 0:
        return F(0), F(0)
    return add(scale(log(x), x), (-x, -x))


def f01(lo, hi):
    # f'=x(log x-1) <= 0 for 0<=x<=1.
    assert 0 <= lo <= hi <= 1
    return f_at(hi)[0], f_at(lo)[1]


def fp01(lo, hi):
    # f''=log x <=0 on (0,1]; fp(0)=0 by continuity.
    assert 0 <= lo <= hi <= 1
    return fp_at(hi)[0], fp_at(lo)[1]


def f14(lo, hi):
    # For 1<=x<=4, -1<=f'(x)<=4(log4-1)<2.
    assert 1 <= lo <= hi <= 4
    midpoint = (lo+hi)/2
    radius = hi-lo  # 2 * half-width
    value = f_at(midpoint)
    return value[0]-radius, value[1]+radius


F1 = (F(-3, 4), F(-3, 4))
F2, F3, F7 = f_at(F(2)), f_at(F(3)), f_at(F(7))
assert log(F(4))[1] < F(3, 2)


def c_interval(lo, hi):
    low = add(f14(2-hi, 2-lo), scale(F1, -4), scale(f01(lo, hi), 3),
              scale(product((1-hi, 1-lo), fp01(lo, hi)), 2))
    high = add(f14(3+lo, 3+hi), scale(F3, -2), f14(3-hi, 3-lo),
               scale(F1, -2), scale(f01(1-hi, 1-lo), 2),
               scale(product((lo, hi), fp01(1-hi, 1-lo)), 2))
    cross = scale(add(f14(3-hi, 3-lo), scale(F2, -2),
                      scale(f14(3-2*hi, 3-2*lo), -1),
                      scale(f14(2-hi, 2-lo), 2), f14(1+lo, 1+hi),
                      scale(F1, -1)), 2)
    return add(low, high, cross)


def penalty_at(q):
    # P(q)=2 int_(1-q)^1 [B(2-t)-B(t)]dt is nondecreasing.
    return scale(add(f_at(7+q), f_at(7-q), scale(F7, -2),
                     scale(f_at(1+q), -1), scale(f_at(1-q), -1),
                     scale(F1, 2)), 2)


def outward(interval, denominator=10**9):
    lo = F((interval[0].numerator*denominator)//interval[0].denominator, denominator)
    hi = F(-((-interval[1].numerator*denominator)//interval[1].denominator), denominator)
    assert lo <= interval[0] <= interval[1] <= hi
    return {'lower': str(lo), 'upper': str(hi),
            'approx_lower': float(lo), 'approx_upper': float(hi)}


minimum_lower = None
minimum_index = None
sample_upper = None
sample_index = None
cell_bounds = []
for index in range(CELLS):
    lo, hi = F(index, CELLS), F(index+1, CELLS)
    c = c_interval(lo, hi)
    penalty_lo, penalty_hi = penalty_at(lo), penalty_at(hi)
    lower = c[0] + max(F(0), penalty_lo[0])
    upper = c[1] + penalty_hi[1]
    if minimum_lower is None or lower < minimum_lower:
        minimum_lower, minimum_index = lower, index
    midpoint = (lo+hi)/2
    sample = add(c_interval(midpoint, midpoint), penalty_at(midpoint))
    if sample_upper is None or sample[1] < sample_upper:
        sample_upper, sample_index = sample[1], index
    cell_bounds.append(outward((lower, upper)))

certified = outward((minimum_lower, sample_upper))
result = {
    'status': 'PASS',
    'scope': 'Uniform interval lower bound for c(q)+P(q) on all 0<=q<=1 only.',
    'execution_count': 1,
    'old_or_peer_execute_import_rerun': 0,
    'external_lean': 0,
    'cells': CELLS,
    'log_series_terms': TERMS,
    'all_q_cover': '4096 closed rational intervals; monotonicity and derivative bounds cover every point',
    'global_minimum_interval': certified,
    'minimum_lower_cell': minimum_index,
    'smallest_certified_sample_upper_cell': sample_index,
    'cell_bounds': cell_bounds,
    'not_proved_by_program': ['all-n determinant bound', 'variational supremum equality',
                              'actual determinant nonzero', 'arithmetic margin'],
}
TARGET.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k: result[k] for k in ('status', 'cells', 'global_minimum_interval',
                                      'minimum_lower_cell', 'smallest_certified_sample_upper_cell')}, indent=2))
