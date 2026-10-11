"""Exact finite checks for the mixed Bernoulli distribution compatibility note.

This checks moments and polynomial identities, not determinant valuations.
The universal Z_p statements in the note use von Staudt-Clausen and norm
bounds; testing a=1,3,p does not prove them by itself.
"""
import json
import math
from pathlib import Path

from flint import fmpq as Q

ROOT = Path(__file__).resolve().parent


def tau_monomial(d, s):
    r = s - 2
    if d < r:
        return Q(0)
    return Q(math.comb(d, r), s - 1) * Q.bernoulli(d - r)


def vp(q, p):
    if not q:
        return None
    n, den = abs(int(q.numerator)), int(q.denominator)
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    while den % p == 0:
        den //= p
        result -= 1
    return result


def minimum_nonzero(vals):
    return min(v for v in vals if v is not None)


def primes(lower, upper):
    return [p for p in range(lower, upper + 1)
            if all(p % q for q in range(2, math.isqrt(p) + 1))]


def distribution_rhs(d, s, p):
    total = Q(0)
    # Expand g(c+p*x) exactly, and apply the Bernoulli functional.
    for c in range(p):
        for k in range(d + 1):
            total += Q(math.comb(d, k)) * c**(d-k) * p**k * tau_monomial(k, s)
    return total / p**(s-1)


def main():
    rows = []
    coefficient_checks = 0
    for p in primes(7, 101):
        ds = list(range(4*p))
        t5 = [tau_monomial(d, 5) for d in ds]
        t3 = [tau_monomial(d, 3) for d in ds]
        v5 = [vp(x, p) for x in t5]
        v3 = [vp(x, p) for x in t3]
        assert all(v is None or v >= 0 for v in v5[:4*p-1])
        assert v5[4*p-1] == -1
        assert all(v is None or v >= 0 for v in v3[:2*p-1])
        assert v3[2*p-1] == -1
        assert all(v is None or v >= -1 for v in v3)
        scaled_minima = {}
        for a in (1, 3, p):
            scaled = [vp(Q(a*p*p)*x, p) for x in t3]
            assert all(v is None or v >= 1 for v in scaled)
            scaled_minima[str(a)] = minimum_nonzero(scaled)
            coefficient_checks += len(ds)
        raw_mixed = [vp(x+3*y, p) for x, y in zip(t5, t3)]
        distributed_mixed = [vp(x+3*p*p*y, p) for x, y in zip(t5, t3)]
        first_raw = next(d for d, v in enumerate(raw_mixed) if v is not None and v < 0)
        first_distributed = next(d for d, v in enumerate(distributed_mixed) if v is not None and v < 0)
        assert first_raw == 2*p-1 and first_distributed == 4*p-1
        coefficient_checks += 2*len(ds)
        rows.append(dict(
            p=p, monomial_degrees_checked=[0, 4*p-1],
            tau5_integral_through=4*p-2, tau5_first_bad_degree=4*p-1,
            tau5_first_bad_valuation=v5[4*p-1],
            tau3_integral_through=2*p-2, tau3_first_bad_degree=2*p-1,
            tau3_first_bad_valuation=v3[2*p-1],
            scaled_tau3_valuation_minima=scaled_minima,
            original_a3_first_bad_degree=first_raw,
            distributed_a3_first_bad_degree=first_distributed,
        ))
    distribution_checks = 0
    for p in (7, 11, 13):
        for s in (3, 5):
            for d in range(65):
                assert distribution_rhs(d, s, p) == tau_monomial(d, s)
                distribution_checks += 1
    result = dict(
        status='exact_finite_checks_passed',
        scope='Bernoulli moments and polynomial distribution only; no determinant gain',
        universal_argument='See zeta35_distribution_compatibility_note.md; arbitrary a in Z_p uses v_p(a)>=0',
        primes_checked=len(rows), coefficient_checks=coefficient_checks,
        exact_polynomial_distribution_checks=distribution_checks,
        polynomial_distribution_primes=[7, 11, 13], polynomial_distribution_degrees=[0, 64],
        rows=rows,
    )
    (ROOT / 'verify_zeta35_distribution_compatibility.json').write_text(
        json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({key:value for key,value in result.items() if key!='rows'}, indent=2))


if __name__ == '__main__':
    main()
