"""Exact positive divisibility filters of the zeta(7) moment functional.

nu_c(R) = sum_d c_d/d^2 * mu(R(t/d^2)).
The density retains frequencies n with weight a(n)=sum_{d|n} c_d.
All arithmetic below is rational; evaluation uses Arb. Finite experiments
are not asymptotic estimates or an irrationality proof.
"""
from functools import lru_cache
from math import lcm
from pathlib import Path
import argparse
import hashlib
import json
from flint import fmpq, fmpq_poly, arb, ctx
from joint_exact import (Dcache, moment, entries_from_polynomial, determinant,
                         evaluate_primitive_ball, norm_scalar, canonical)


def canonical_filter(coefficients):
    return tuple(sorted((int(d), fmpq(c)) for d, c in coefficients if c))


def positivity_data(coefficients):
    cs = canonical_filter(coefficients)
    assert cs and all(d >= 1 for d, _ in cs)
    assert len({d for d, _ in cs}) == len(cs)
    period = lcm(*(d for d, _ in cs))
    assert period <= 100000, 'Use divisor classes for large periods.'
    values = [sum((c for d, c in cs if n % d == 0), fmpq(0))
              for n in range(1, period + 1)]
    assert min(values) >= 0 and max(values) > 0
    return dict(period=period, minimum=str(min(values)), maximum=str(max(values)),
                a1=str(values[0]), mean=str(sum(values, fmpq(0))/period),
                first_frequency=next(i+1 for i, v in enumerate(values) if v))


@lru_cache(None)
def harmonic7(n):
    return sum((fmpq(1, j**7) for j in range(1, n+1)), fmpq(0))


def filtered_entries(K, W, h, coefficients):
    cs = canonical_filter(coefficients)
    D = fmpq_poly(Dcache(K))
    W = fmpq_poly(W)
    derivative = D.derivative()
    beta = sum((c*d**6 for d, c in cs), fmpq(0))
    residues = [(j, W(-j*j)/derivative(-j*j))
                for j in range(1, K+1) if W(-j*j)]
    poles = {j: sum((c*(-(d*j)**6*harmonic7(d*j)-fmpq(1, 6)
                        +fmpq(1, 2*d*j)) for d, c in cs), fmpq(0))
             for j, _ in residues}
    @lru_cache(None)
    def filtered_moment(e):
        return moment(e)*sum((c/fmpq(d**(2*e+2)) for d, c in cs), fmpq(0))
    aa, bb = [], []
    P = W
    powers = [fmpq(1)]*len(residues)
    for e in range(2*h-1):
        quotient = P//D
        a = sum((c*filtered_moment(k) for k, c in enumerate(quotient)), fmpq(0))
        b = fmpq(0)
        for i, (j, r) in enumerate(residues):
            factor = r*powers[i]
            a += factor*poles[j]
            b += factor*beta*j**6
            powers[i] *= -j*j
        aa.append(a)
        bb.append(b)
        P *= fmpq_poly([0, 1])
    return aa, bb


def dilation_entries_independent(K, W, h, coefficients):
    """Independent route: embed the dilated pole set into D_{dK}."""
    aa, bb = [fmpq(0)]*(2*h-1), [fmpq(0)]*(2*h-1)
    for d, c in canonical_filter(coefficients):
        T = fmpq_poly([1])
        for j in range(1, K+1):
            T *= fmpq_poly([(d*j)**2, 1])
        numerator = fmpq_poly([w/fmpq(d**(2*i)) for i, w in enumerate(W)])
        numerator *= d**(2*K)*(Dcache(d*K)//T)
        a, b = entries_from_polynomial(d*K, numerator, h)
        for e in range(2*h-1):
            aa[e] += c*a[e]/d**(2*e+2)
            bb[e] += c*b[e]/d**(2*e+2)
    return aa, bb


def experiment(K, profile, h, coefficients, label):
    cs = canonical_filter(coefficients)
    positive = positivity_data(cs)
    W = fmpq_poly([1])
    for N, b in canonical(profile):
        W *= Dcache(N)**b
    aa, bb = filtered_entries(K, W, h, cs)
    poly = determinant(aa, bb, h)
    ct, log_value, bits = evaluate_primitive_ball(poly)
    S = norm_scalar(K, profile, h)
    with ctx.workprec(max(160, bits)):
        raw_log = log_value+arb(ct).log()
        real = (raw_log+arb(S).log())/K**2
        arithmetic = -arb(ct*S).log()/K**2
        result = dict(K=K, profile=[list(x) for x in canonical(profile)], h=h,
                      label=label, coefficients=[[d, str(c)] for d, c in cs],
                      beta=str(sum((c*d**6 for d, c in cs), fmpq(0))),
                      positivity=positive, degree=poly.degree(),
                      degenerate_constant=poly.degree() == 0,
                      score=float((log_value/K**2).mid()),
                      score_ball=(log_value/K**2).str(30),
                      arithmetic_ball=arithmetic.str(30), real_ball=real.str(30),
                      raw_log_ball=raw_log.str(30), precision_bits=bits,
                      primitive_hash=hashlib.sha256(str(poly/ct).encode()).hexdigest())
    if poly.degree() == 0:
        assert poly/ct == fmpq_poly([1])
    return result


FILTERS = [
    ('baseline', [(1, 1)]),
    ('odd', [(1, 1), (2, -1)]),
    ('not_multiple_3', [(1, 1), (3, -1)]),
    ('coprime_6', [(1, 1), (2, -1), (3, -1), (6, 1)]),
    ('even_only', [(2, 1)]),
    ('lambda_1_2', [(1, 1), (2, fmpq(-1, 2))]),
    ('lambda_1_63', [(1, 1), (2, fmpq(-1, 63))]),
    ('lambda_1_64', [(1, 1), (2, fmpq(-1, 64))]),
    ('lambda_1_65', [(1, 1), (2, fmpq(-1, 65))]),
    ('lambda_1_128', [(1, 1), (2, fmpq(-1, 128))]),
]


def validate():
    checks = 0
    for K, N, h in [(3, 1, 2), (5, 1, 4), (6, 2, 4)]:
        W = Dcache(N)**8
        for label, cs in FILTERS:
            aa, bb = filtered_entries(K, W, h, cs)
            assert (aa, bb) == dilation_entries_independent(K, W, h, cs), label
            if label == 'baseline':
                assert (aa, bb) == entries_from_polynomial(K, W, h)
            if label == 'lambda_1_64':
                assert all(not b for b in bb)
            checks += 1
    results = [experiment(8, [(1, 8)], 7, cs, label) for label, cs in FILTERS]
    base = next(r for r in results if r['label'] == 'baseline')
    half = next(r for r in results if r['label'] == 'lambda_1_2')
    with ctx.workprec(160):
        difference = arb(half['raw_log_ball'])-arb(base['raw_log_ball'])
        assert difference < 0 and difference > -7*arb(2).log()
    return dict(independent_dilation_checks=checks,
                beta_zero_constant_verified=True,
                gram_comparison_half_filter_verified=True, small_results=results)


def scan(extended=False):
    output = Path(__file__).with_name('filtered_measure_extended.json' if extended
                                     else 'filtered_measure_scan.json')
    rows = []
    configurations = ([(40, [(1, 8)], 39), (48, [(2, 8)], 46)] if extended else
                      [(12, [(1, 8)], 11), (24, [(1, 8)], 23),
                       (24, [(1, 3), (2, 2), (3, 1)], 21)])
    filters = [f for f in FILTERS if f[0] in ('baseline', 'odd', 'not_multiple_3',
                                            'lambda_1_63')] if extended else FILTERS
    for K, profile, h in configurations:
        for label, cs in filters:
            r = experiment(K, profile, h, cs, label)
            rows.append(r)
            output.write_text(json.dumps(rows, indent=2), encoding='utf-8')
            print(json.dumps({k: r[k] for k in ('K', 'profile', 'label', 'degree', 'score')}), flush=True)
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--scan', action='store_true')
    parser.add_argument('--extend', action='store_true')
    args = parser.parse_args()
    if args.scan or args.extend:
        scan(args.extend)
    else:
        result = validate()
        Path(__file__).with_name('filtered_measure_validation.json').write_text(
            json.dumps(result, indent=2), encoding='utf-8')
        print(json.dumps({k: v for k, v in result.items() if k != 'small_results'}))
