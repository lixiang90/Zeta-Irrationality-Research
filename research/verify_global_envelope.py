"""Cross-check the global arithmetic normalization and window ceilings.

New exact identities are checked separately from finite existing data and
ordinary numerical quadrature, which is only a cross-check of interval results.
"""
import json
import math
import pickle
import sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
from flint import fmpq
from sympy import primerange

from global_envelope import (GROWTH, area, affine, exact_tail, six_pole_gain,
                             remaining_six_pole_ceiling, leading_coefficient_cost)
from joint_exact import norm_scalar
from joint_padic import val

HERE = Path(__file__).parent


def capacity_by_q(row):
    alpha = F(row['alpha'])
    cap = min(F(20), 1/(2*alpha))
    sums = defaultdict(F)
    for ls, rs, name, sa, sb in row['pieces']:
        l, r = F(ls), min(F(rs), cap)
        if r <= l:
            continue
        xs = [l+(r-l)*F(j, 4) for j in (1, 2, 3)]
        a, b = affine(xs, [leading_coefficient_cost(x, alpha) for x in xs])
        a, b = F(sa)-a, F(sb)-b
        assert all(a*x+b >= 0 for x in [l, r])
        sums[math.floor((l+r)/2)] += area([(l, r, 'ceiling', a, b)])
    return {str(k):str(v) for k,v in sorted(sums.items())}


def check_cached_identities():
    out = []
    for K, N in [(40, 1), (40, 3), (80, 2), (80, 6)]:
        data = json.loads((HERE/f'joint_cache_K{K}_N{N}.json').read_text())
        h = K-N
        lead = (-1)**(h*(h-1)//2)
        for j in range(N+1, K+1):
            lead *= j**6*math.prod(c*c-j*j for c in range(1, N+1))**7
        assert fmpq(data['poly'][h]) == lead
        scalar = norm_scalar(K, [(N, 8)], h)
        count = 0
        for p in primerange(math.isqrt(2*K)+1, 2*h+1):
            assert p*p > 2*K
            predicted = 2*h*(K//p-8*(N//p))-2*sum((2*i)//p for i in range(1, h))
            assert val(scalar, p) == predicted
            count += 1
        out.append(dict(K=K, N=N, leading_identity=True, normalization_prime_checks=count))
    return out


def main():
    data = json.loads((HERE/'global_envelope_scan.json').read_text())
    rows = {F(r['alpha']):r for r in data['rows']}
    calibrations = []
    for alpha, slug in [(F(1, 40),'b8_39'),(F(3, 100),'a030'),
                        (F(1, 25),'a040'),(F(1, 20),'a050')]:
        row = rows[alpha]
        old = pickle.loads((GROWTH/f'pieces_{slug}.pkl').read_bytes())
        assert area(old) == F(row['old_inner'])
        old_outer = pickle.loads((GROWTH/f'outer_pieces_{slug}.pkl').read_bytes())
        # Prior outer tuples do not have the candidate-name slot.
        total = sum((F(p[-2])*(1/F(p[0])-1/F(p[1]))
                     +F(p[-1])*(1/F(p[0])**2-1/F(p[1])**2)/2 for p in old_outer), F(0))
        assert total == F(row['old_outer'])
        calibrations.append(dict(alpha=str(alpha), inner=True, outer=True))
    window_checks = []
    for alpha, row in rows.items():
        assert F(row['six_pole_gain']) == six_pole_gain(alpha)
        if alpha > F(1, 9):
            # Integrate the three affine gain branches independently of x-envelope.
            l, r = F(1, 3), 3*alpha
            c, d = (1+3*alpha)/4, (1+6*alpha)/5
            def integ(l, r, a, b): return a*(r*r-l*l)/2+b*(r-l)
            gain = integ(l, c, -10, 14*alpha+2)+integ(c, d, -2, 8*alpha)+integ(d, r, -7, 14*alpha+1)
            cap = integ(l, r, -7, alpha+9)-gain
            assert gain == six_pole_gain(alpha)
            assert cap == remaining_six_pole_ceiling(alpha)
            window_checks.append(dict(alpha=str(alpha), gain=str(gain), remaining_ceiling=str(cap),
                                      gap_even_with_perfect_window=row['gap_even_with_perfect_window']))
    mp.mp.dps = 60
    quadratures = []
    def m(v): return mp.mpf(v.numerator)/v.denominator
    for alpha in [F(1, 40), F(1, 8)]:
        a = m(alpha); lam = 1-a
        cuts = sorted({F(20), F(400)} | {F(k) for k in range(21, 400)}
                      | {F(k)/alpha for k in range(math.floor(20*alpha)+1, math.ceil(400*alpha))})
        total = mp.mpf(0)
        for l, r in zip(cuts, cuts[1:]):
            mid = (l+r)/2; q, qp = math.floor(mid), math.floor(alpha*mid)
            total += mp.quad(lambda x: (x*(6*lam+2*lam*(x-q)-16*lam*(a*x-qp))+mp.mpf(43)/16)/x**3,
                             [m(l), m(r)])
        tail, _ = exact_tail(alpha)
        assert abs(total-m(tail.lo)) < mp.mpf('1e-35')
        quadratures.append(dict(alpha=str(alpha), tail_numeric=mp.nstr(total, 45),
                                status='Numerical cross-check only; enclosure is the rational-series certificate.'))
    old_finite = json.loads((HERE/'joint_outer_strong.json').read_text())
    grouped = defaultdict(list)
    for r in old_finite:
        grouped[r['K']//r['p']].append(r)
    saturation = {str(q):dict(cases=len(rs), equality=sum(r['slack']==0 for r in rs),
                               max_slack=max(r['slack'] for r in rs),
                               exceptions=[dict(K=r['K'],N=r['N'],p=r['p'],slack=r['slack'])
                                           for r in rs if r['slack'] and q < 2])
                  for q,rs in grouped.items()}
    result = dict(status='Exact algebraic checks plus explicitly labelled numerical / finite-data checks.',
                  old_table_agreement=calibrations, cached_identities=check_cached_identities(),
                  window_checks=window_checks, tail_quadrature=quadratures,
                  scanned_parameters=len(rows), all_scanned_gaps_positive=all(F(r['gap_interval'][0])>0 for r in rows.values()),
                  capacity_by_q={str(a):capacity_by_q(rows[a]) for a in [F(1,40),F(1,8)]},
                  earlier_finite_saturation=saturation)
    (HERE/'global_envelope_validation.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    # Refresh the short reference table from the fully recomputed scan.
    wanted=[F(1,40),F(1,20),F(3,40),F(1,10),F(1,9),F(7,60),F(3,25),F(1,8)]
    (HERE/'global_envelope.json').write_text(json.dumps(dict(status=data['status'], rows=[rows[a] for a in wanted]), indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['capacity_by_q','tail_quadrature']}, indent=2))


if __name__ == '__main__':
    main()
