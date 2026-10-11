"""Exact uneliminated very-well-poised forms in zeta(3), zeta(5).

R_n(t)=(n!)^4 (2t+n) prod_{k=1}^n (t-k)(t+n+k)
       / prod_{j=0}^n(t+j)^6.
Stores both standard integer normalization d_n^6 and primitive triples.
Finite computations are not irrationality certificates for individual terms.
"""
import json
import math
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
from zeta35_broad_search import mul

ROOT = Path(__file__).parent


def coefficients(n, order=6):
    assert order in (4, 6)
    p = Poly([n, 2])
    for k in range(1, n + 1):
        p *= Poly([-k * (n + k), n, 1])
    p *= math.factorial(n) ** (order-2)
    d = math.lcm(*range(1, n + 1))
    hs = [[Q(0)] for _ in range(7)]
    for s in range(1, 7):
        for j in range(1, n + 1):
            hs[s].append(hs[s][-1] + Q(1, j**s))
    totals = [Q(0)] * 7
    constant = Q(0)
    partial = []
    for j in range(n + 1):
        local = [sum((p[i] * math.comb(i, k) * Q(-j)**(i-k)
                      for i in range(k, len(p))), Q(0)) for k in range(order)]
        for ell in range(n + 1):
            if ell != j:
                local = mul(local, [Q((-1)**k * math.comb(k+order-1, k), (ell-j)**(order+k))
                                    for k in range(order)], order)
        cs = [Q(0)] + [local[order-s] for s in range(1, order+1)]
        for s in range(1, order+1):
            assert (cs[s] * d**(order-s)).denominator == 1
            totals[s] += cs[s]
            constant -= cs[s] * hs[s][j]
        partial.append(cs)
    assert all(totals[s] == 0 for s in (1, 2, 4, 6))
    # Independent rational-function evaluation of partial fractions.
    for x in (Q(n+1), Q(n+2), Q(1, 2)):
        lhs = p(x) / math.prod((x+j)**order for j in range(n+1))
        rhs = sum((cs[s] / (x+j)**s for j, cs in enumerate(partial)
                   for s in range(1, order+1)), Q(0))
        assert lhs == rhs
    raw = (totals[3], totals[5], constant)
    standard_q = [v * d**(6 if order == 6 else 3) for v in raw]
    assert all(v.denominator == 1 for v in standard_q)
    standard = [int(v) for v in standard_q]
    gcd = math.gcd(*standard)
    primitive = [v // gcd for v in standard]
    # Positive binomial identity for the highest zeta coefficient.
    tj = [sum(math.comb(n-j, k-j) * math.comb(n, k) * math.comb(n+k, k)
              for k in range(j, n+1)) for j in range(n+1)]
    u = sum(math.comb(n, i)**2 * math.comb(n, j)**2 * math.comb(n+j-i, n) * tj[j]
            for j in range(n+1) for i in range(j+1))
    if order == 6:
        assert raw[1] == 2*u and u > 0
    else:
        assert raw[1] == 0
        assert raw[0] == 2*sum(math.comb(n, j)**2*math.comb(n+j, n)**2 for j in range(n+1))
    bits = max(abs(v).bit_length() for v in standard)
    ctx.prec = bits + 512
    value = standard[0]*arb(3).zeta() + standard[1]*arb(5).zeta() + standard[2]
    assert value > 0
    return dict(n=n, order=order, raw=[str(v) for v in raw], standard=[str(v) for v in standard],
                primitive=[str(v) for v in primitive], gcd=str(gcd),
                standard_log=float(value.log()), primitive_log=float((value/gcd).log()),
                a_over_b=float(raw[0]/raw[1]) if raw[1] else None, coefficient_bits=bits,
                precision_bits=ctx.prec)


def phase_certificate():
    # Write x=1+y. Saddle numerator has exactly one positive root:
    # 3 - 106 y - 378 y^2 - 546 y^3 - 420 y^4 - 182 y^5 - 42 y^6 - 4 y^7.
    ctx.prec = 192
    lo, hi = Q(102583176901299, 10**14), Q(102583176901301, 10**14)
    def saddle(x):
        return x**7*(x+2) - (x-1)*(x+1)**7
    assert saddle(lo) > 0 and saddle(hi) < 0
    x = arb('1.02583176901300', '0.00000000000001')
    f = 7*x*x.log() - (x-1)*(x-1).log() + (x+2)*(x+2).log() - 7*(x+1)*(x+1).log()
    assert f + 6 < arb('-0.38')
    return dict(root_bracket=[str(lo), str(hi)], phase_interval=str(f),
                normalized_phase_interval=str(f+6), upper_bound='-0.38')


if __name__ == '__main__':
    records = []
    for n in [1, 2, 3, 4, 8, 16, 32, 64]:
        row = coefficients(n)
        apery = coefficients(n, 4)
        a, b, c = map(int, row['standard'])
        u, _, v = map(int, apery['standard'])
        epsilon = 1 if a+u != 0 else 2
        mixed = [a+epsilon*u, b, c+epsilon*v]
        assert mixed[0] != 0 and mixed[1] > 0
        ctx.prec = max(abs(v).bit_length() for v in mixed) + 512
        mixed_value = mixed[0]*arb(3).zeta()+mixed[1]*arb(5).zeta()+mixed[2]
        assert mixed_value > 0
        row['apery_standard'] = apery['standard']
        row['mixed_epsilon'] = epsilon
        row['mixed_standard'] = [str(v) for v in mixed]
        row['mixed_log'] = float(mixed_value.log())
        records.append(row)
        print(n, row['standard_log'], row['primitive_log'], row['a_over_b'],
              row['raw'] if n <= 3 else '', flush=True)
    result = dict(status='exact coefficient checks and interval phase bound; not individual irrationality certificates',
                  phase=phase_certificate(), records=records)
    (ROOT / 'zeta35_uneliminated.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
