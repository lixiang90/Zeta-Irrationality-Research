"""Same-alpha arithmetic envelope, with exact rational piece certificates.

This integrates written local lemmas, not a completed Lean proof of zeta(7).
Minima of finitely many affine candidates are certified on whole intervals.
The tail envelope is integrated exactly, with a rational enclosure for log.
"""
import argparse
import json
import math
import sys
import time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

from joint_outer_strong import components, GROWTH, integral as old_outer_integral
from layer_uniform_rank import rank_cap_limit
from table_b8_39 import ccount, Jc_fast, psiR
from restart_obstruction_certificate import log_iv, primal_bound, outward_decimal


def cuts_for(alpha, lo, hi):
    steps = [F(1, 2), 1/(2*alpha), 1/(2*(1-alpha)),
             1/(1-alpha), 1/(1+alpha)]
    cuts = {lo, hi}
    for step in steps:
        cuts.update(k*step for k in range(math.ceil(lo/step), math.floor(hi/step)+1))
    # Changes of rank and of the six-pole min/max branches.
    special = [F(3), 1/(2*alpha), 2/(1+6*alpha), 3/(1+6*alpha),
               4/(1+3*alpha), 5/(1+6*alpha)]
    window = third_window(alpha)
    if window:
        special += list(window)
    cuts.update(x for x in special if lo < x < hi)
    return sorted(cuts)


def third_window(alpha):
    left_y = max(F(1, 3), 8*alpha/3)
    right_y = min((1+alpha)/3, 3*alpha)
    return (1/right_y, 1/left_y) if left_y < right_y else None


def six_pole_gain(alpha):
    assert 0 < alpha <= F(1, 8)
    return (9*alpha-1)*(183*alpha-7)/180 if alpha > F(1, 9) else F(0)


def remaining_six_pole_ceiling(alpha):
    """Max extra gain on the proved third-layer window, from [X^h] Delta."""
    assert F(1, 9) <= alpha <= F(1, 8)
    return (9*alpha-1)*(159-251*alpha)/60


def leading_coefficient_cost(x, alpha):
    """A LOWER bound on the true cost, not a new usable divisibility bound.

    Assumes p>2N. All possible extra content is capped by the X^h coefficient.
    """
    assert alpha*x < F(1, 2)
    q = math.floor(x)
    f, g = x-q, alpha*x
    raw_ceiling = 7*((2*q-1)*g+min(g, f)+max(F(0), g+f-1))
    return normalization_cost(x, alpha)-raw_ceiling


@lru_cache(None)
def psi_coefficients(q, qp, k):
    B = 16*qp-2*q-6
    v = [[psiR(k, B+8*b-a) for b in range(3)] for a in range(3)]
    v = [[r[0], r[1]-r[0], r[2]-r[1]] for r in v]
    return tuple(v[0] + [v[1][j]-v[0][j] for j in range(3)]
                 + [v[2][j]-v[1][j] for j in range(3)])


def counts(x, alpha):
    return [ccount(x-math.floor(x), alpha*x-math.floor(alpha*x), i, j)
            for i in range(3) for j in range(3)]


def normalization_cost(x, alpha):
    u = (1-alpha)*x
    return -2*u*math.floor(x)+16*u*math.floor(alpha*x)+2*Jc_fast(u)


def six_pole_cost(x, alpha):
    # raw v_p(Delta)/p = (48 alpha-1)x-21-b, not v_p(F)/p.
    b = max(F(0), min(3-x, (6*alpha+1)*x-5))
    return normalization_cost(x, alpha)-((48*alpha-1)*x-21-b)


def affine(xs, ys):
    a = (ys[1]-ys[0])/(xs[1]-xs[0])
    b = ys[0]-a*xs[0]
    assert all(y == a*x+b for x, y in zip(xs, ys))
    return a, b


def certify_base_cell(alpha, l, r):
    """Check primitive branch ordering at endpoints, rather than sampling kinks."""
    mid = (l+r)/2
    q, qp, j = math.floor(mid), math.floor(alpha*mid), math.floor(2*(1-alpha)*mid)
    assert q <= l <= r <= q+1
    assert qp <= alpha*l <= alpha*r <= qp+1
    assert j <= 2*(1-alpha)*l <= 2*(1-alpha)*r <= j+1
    def values(x):
        f, g = x-q, alpha*x-qp
        return [F(0), F(1, 2), f, g, 1-f, 1-g]
    vl, vr = values(l), values(r)
    assert all((vl[i]-vl[k])*(vr[i]-vr[k]) >= 0
               for i in range(6) for k in range(i))


def candidates(alpha, l, r):
    certify_base_cell(alpha, l, r)
    xs = [l+(r-l)*F(j, 4) for j in (1, 2, 3)]
    mid = xs[1]
    lines = {}
    if mid < 3:
        # These are all valid simultaneous upper bounds for arithmetic cost.
        vals = [components(x, alpha, True) for x in xs]
        for j, name in [(1, 'rank'), (2, 'zero')]:
            lines[name] = affine(xs, [v[0]+v[j] for v in vals])
        lines['projection'] = affine(xs, [v[0]+rank_cap_limit(x, alpha)
                                          for x, v in zip(xs, vals)])
    else:
        q, qp = math.floor(mid), math.floor(alpha*mid)
        cs = [counts(x, alpha) for x in xs]
        ns = [normalization_cost(x, alpha) for x in xs]
        us = [(1-alpha)*x for x in xs]
        # Every k in this range is an admissible existing inner-prime bound.
        # No assertion about an unbounded integer optimization is needed.
        for k in range(-2*q-8, 8*q+21):
            co = psi_coefficients(q, qp, k)
            ys = [n-u*k+2*sum(a*b for a, b in zip(co, c))
                  for n, u, c in zip(ns, us, cs)]
            lines[f'inner:{k}'] = affine(xs, ys)
        if mid < 1/(2*alpha):
            vals = [components(x, alpha, True) for x in xs]
            for j, name in [(1, 'rank'), (2, 'zero')]:
                lines[name] = affine(xs, [v[0]+v[j] for v in vals])
            lines['projection'] = affine(xs, [v[0]+rank_cap_limit(x, alpha)
                                              for x, v in zip(xs, vals)])
    w = third_window(alpha)
    if w and w[0] < mid < w[1]:
        lines['six_pole'] = affine(xs, [six_pole_cost(x, alpha) for x in xs])
    return lines


def lower_envelope(l, r, lines):
    """Exact finite lower hull; endpoint inequalities certify each entire cell."""
    cur = l
    pieces = []
    while cur < r:
        name = min(lines, key=lambda n: (lines[n][0]*cur+lines[n][1], lines[n][0], n))
        a, b = lines[name]
        nxt = r
        for a2, b2 in lines.values():
            if a2 < a:
                cross = (b2-b)/(a-a2)
                if cur < cross < nxt:
                    nxt = cross
        assert nxt > cur
        # An affine difference nonnegative at both endpoints is nonnegative throughout.
        assert all(a*x+b <= a2*x+b2 for x in [cur, nxt] for a2, b2 in lines.values())
        pieces.append((cur, nxt, name, a, b))
        cur = nxt
    return pieces


def area(pieces):
    return sum((a*(1/l-1/r)+b*(1/l**2-1/r**2)/2
                for l, r, _, a, b in pieces), F(0))


def exact_tail(alpha, M=400):
    """Integral of [x(6lambda+2lambda{x}-16lambda{alpha x})+43/16]/x^3."""
    M = F(M)
    assert M >= 20
    assert 2*(1-alpha)*M <= 1000  # Preserve the existing J_c truncation interface.
    cuts = {F(20), M}
    cuts.update(F(k) for k in range(21, math.ceil(M)))
    cuts.update(F(k)/alpha for k in range(math.floor(20*alpha)+1, math.ceil(M*alpha)))
    cuts = sorted(cuts)
    lam = 1-alpha
    rational = F(43, 32)*(F(1, 400)-1/M**2)
    for l, r in zip(cuts, cuts[1:]):
        x = (l+r)/2
        b = lam*(6-2*math.floor(x)+16*math.floor(alpha*x))
        rational += b*(1/l-1/r)
    log_co = 2*lam*(1-8*alpha)
    value = rational+log_co*log_iv(M/20)
    return value, dict(rational=str(rational), log_coefficient=str(log_co),
                       log_argument=str(M/20), cells=len(cuts)-1,
                       enclosure=outward_decimal(value))


def best_uniform_s(alpha):
    # Numerical choice only. The value at this exact rational s is certified below.
    from restart_probe import uniform_primal
    s = math.sqrt(uniform_primal(float(alpha))['right'])
    return F(round(10000*s), 10000)


def run_alpha(alpha):
    assert 0 < alpha <= F(1, 8)
    lo, hi = 1/(2*(1-alpha)), F(20)
    cuts = cuts_for(alpha, lo, hi)
    pieces = []
    prev_pieces = []
    old_inner = []
    for l, r in zip(cuts, cuts[1:]):
        lines = candidates(alpha, l, r)
        pieces.extend(lower_envelope(l, r, lines))
        prev_pieces.extend(lower_envelope(l, r, {k:v for k,v in lines.items() if k != 'six_pole'}))
        if l >= 3:
            old_inner.extend(lower_envelope(l, r, {k:v for k,v in lines.items() if k.startswith('inner:')}))
    outer = area([p for p in pieces if p[1] <= 3])
    inner = area([p for p in pieces if p[0] >= 3])
    third_gain = area(prev_pieces)-area(pieces)
    inner_gain = area(old_inner)-inner
    if alpha <= F(1, 9):
        assert third_gain == 0
    if alpha == F(1, 8):
        assert third_gain == F(127, 11520)
    if alpha == F(1, 40):
        assert inner_gain == F(387, 17920)
    assert third_gain == six_pole_gain(alpha)
    old_outer, _ = old_outer_integral(alpha, False)
    tail, tail_data = exact_tail(alpha)
    small = 8*(1-alpha)/400
    A = outer+inner+tail+small
    s = best_uniform_s(alpha)
    B = primal_bound(alpha, s)
    gap = A+B
    assert gap.hi-gap.lo < F(1, 10**25)
    # Cross-check the existing earlier table / boundary-remainder tail.
    sys.path.insert(0, str(GROWTH))
    from aeff_scan import tail_bound
    prior_tail, _ = tail_bound(1-alpha, alpha)
    assert tail.hi <= prior_tail
    row = dict(alpha=str(alpha), outer=str(outer), inner=str(inner), small=str(small),
               old_inner=str(area(old_inner)), old_outer=str(old_outer),
               inner_gain=str(inner_gain), six_pole_gain=str(third_gain),
               tail=tail_data, tail_recovery=outward_decimal(prior_tail-tail),
               A_interval=outward_decimal(A), uniform_s=str(s),
               B_interval=outward_decimal(B), gap_interval=outward_decimal(gap),
               A_float=float(A.lo), B_float=float(B.lo), gap_float=float(gap.lo),
               pieces=[[str(x) for x in p] for p in pieces],
               six_pole_window_x=[str(x) for x in third_window(alpha)] if third_window(alpha) else None)
    if alpha >= F(1, 9):
        ceiling = remaining_six_pole_ceiling(alpha)
        row['remaining_six_pole_ceiling'] = str(ceiling)
        row['gap_even_with_perfect_window'] = outward_decimal(gap-ceiling)
    if alpha <= F(1, 15):
        # Entire geometrical six-pole strip, larger than our empty proved window here.
        ceiling = 2*alpha+3*alpha**2
        row['full_six_pole_strip_ceiling'] = str(ceiling)
        row['gap_even_with_perfect_strip'] = outward_decimal(gap-ceiling)
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alphas', default='1/40,1/20,3/40,1/10,1/9,7/60,3/25,1/8')
    ap.add_argument('--out', default='global_envelope.json')
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args()
    start = time.time()
    rows = []
    for alpha in map(F, args.alphas.split(',')):
        row = run_alpha(alpha)
        rows.append(row)
        if args.quiet:
            print(f"alpha={alpha} A={row['A_float']:.12f} gap={row['gap_float']:.12f}", flush=True)
        else:
            print(json.dumps({k:v for k,v in row.items() if k not in ('pieces','tail')}), flush=True)
        Path(__file__).with_name(args.out).write_text(json.dumps(dict(
            status='Exact piece and rational interval certificates for written bounds; not a Lean proof.',
            rows=rows), indent=2), encoding='utf-8')
    print('seconds', time.time()-start, flush=True)


if __name__ == '__main__':
    main()
