"""Check fixed dyadic shifts and the actual seven-layer band on the first ray degree."""

from argparse import ArgumentParser
from fractions import Fraction
from math import comb, gcd, isqrt, log, prod

from verify_odd_pade_band_round286 import series_state
from verify_odd_pade_tied_round285 import (
    beta_ratio, direct_scalar, positive_g, residue, scaled_h6, v2,
)


def dyadic_scalar(d, bits):
    """Evaluate D1 to the requested precision, using its general, degree-dependent tail bound."""
    n = 2 * d
    exponent = (2 * n).bit_length() - 1
    assert 2*d + 7 + v2(n) + n.bit_count() - exponent >= bits
    cutoff = exponent + bits + 6
    total = Fraction()
    for t in range(max(1-n, 1-cutoff), min(n-2, cutoff-1) + 1):
        end = 2*n + t
        local_exponent = (n ^ end).bit_length() - 1
        factor = beta_ratio(d, t) * Fraction(2)**(6*(exponent-local_exponent))
        order = v2(factor.numerator) - v2(factor.denominator)
        if abs(t) + order >= bits:
            continue
        g = positive_g(d, t, bits-order) if t > 0 else 1 << -t
        if g == 0 or v2(g) + order >= bits:
            continue
        unit_bits = bits - v2(g) - order
        unit_modulus = 1 << unit_bits
        base = scaled_h6(n+1, 2*n, exponent, unit_bits)
        shortened = scaled_h6(n+1, end, local_exponent, unit_bits)
        total -= g * factor * (shortened * pow(base, -1, unit_modulus) % unit_modulus)
    return residue(total, 1 << bits)


def primes_between(low, high):
    sieve = bytearray(b'\1') * high
    sieve[:2] = b'\0\0'
    for k in range(2, isqrt(high-1) + 1):
        if sieve[k]:
            sieve[k*k::k] = b'\0' * ((high-1-k*k)//k + 1)
    return [p for p in range(low+1, high) if sieve[p]]


def step(d, n):
    """Common integer recurrence for the square of F(-1/4,1/4;d+1/2;z)."""
    j, i = n-1, n-2
    lead = 2*n*(2*n+2*d-1)*(n+2*d-1)
    middle = 8*j**3 + (12*d-6)*j*j - (4*d-1)*j - d
    tail = -i*(2*i-1)*(2*i+1)
    return lead, middle, tail


def strip_matrix_product(d, primes, integer):
    """Compute the prefix numerator modulo the prime product by binary splitting.

    A matrix (D,a,b,c,e,f,g) has rows (D,a,b), (0,c,e), (0,f,g).
    Its first coordinate sums the series. The two other coordinates propagate
    consecutive coefficients, starting from the column (1,1,0).
    """
    def multiply(right, left):
        D, a, b, c, e, f, g = right
        L, h, i, j, k, l, m = left
        return (D*L, D*h+a*j+b*l, D*i+a*k+b*m,
                c*j+e*l, c*k+e*m, f*j+g*l, f*k+g*m)

    def balanced_product(values):
        if len(values) <= 24:
            return prod(values, start=integer(1))
        midpoint = len(values)//2
        return balanced_product(values[:midpoint]) * balanced_product(values[midpoint:])

    modulus = balanced_product(primes)
    modulus_bits = modulus.bit_length()

    def interval(start, end):
        if end-start <= 24:
            D, a, b, c, e, f, g = map(integer, (1, 0, 0, 1, 0, 0, 1))
            for n in range(start, end):
                lead, mid, tail = step(d, n)
                # Left multiplication by the sparse single-step matrix.
                c, e, f, g = mid*c+tail*f, mid*e+tail*g, lead*c, lead*e
                D, a, b = lead*D, lead*a+c, lead*b+e
            block = (D, a, b, c, e, f, g)
        else:
            middle = (start + end)//2
            block = multiply(interval(middle, end), interval(start, middle))
        if max(x.bit_length() for x in block) > modulus_bits:
            return tuple(x % modulus for x in block)
        return block

    D, a, *_ = interval(1, d+1)
    # For every band prime, prod(D_n) has valuation exactly two.
    assert D % modulus == 0
    numerator = (D+a) % modulus
    common = numerator.gcd(modulus) if hasattr(numerator, 'gcd') else gcd(numerator, modulus)
    return int(common), modulus_bits


def direct_odd_square(d):
    o, prefix = [Fraction(1)], [Fraction(1)]
    for i in range(d):
        o.append(o[-1] * Fraction((4*i-1)*(4*i+1), 8*(i+1)*(2*d+2*i+1)))
        prefix.append(prefix[-1]+o[-1])
    return sum(o[i]*prefix[d-i] for i in range(d+1))


def upper_moment_mod_prime(d, p):
    """Independent W2 calculation at a single prime, starting from the even Gauss series."""
    q = 3*d-1-p
    coeff, prefix = [1], [1]
    for i in range(1, q+1):
        numerator = (4*i-4*d-3)*(4*i-4*d-1)
        denominator = 8*i*(2*i-2*d+1)
        value = coeff[-1] * numerator * pow(denominator, -1, p) % p
        if value == 0:
            break
        coeff.append(value)
        prefix.append((prefix[-1]+value) % p)
    last = len(coeff)-1
    return sum(x*prefix[min(last, q-i)] for i,x in enumerate(coeff)) % p


def band_check(d, integer):
    primes = primes_between(max(127, 2*d), 3*d)
    common, size = strip_matrix_product(d, primes, integer)
    bad = [p for p in primes if common % p == 0]
    assert prod(bad) == common
    if d < 250:
        h = direct_odd_square(d)
        K = Fraction(2*d+1, 2**d) * prod(
            (Fraction(2*j+3, j) for j in range(d, 2*d-1)), start=Fraction(1))
        z = 4*(2*d-1)**2 - series_state(3*d-1)[0]
        assert K**2*h == z
        assert bad == [p for p in primes if z.numerator % p == 0]
        delta = (2*d-1)**2 - z
        assert delta < 0
        for p in bad:
            delta_mod = delta.numerator * pow(delta.denominator, -1, p) % p
            assert pow(delta_mod, (p-1)//2, p) == 1
    sample = primes if d < 250 else (primes[0], primes[len(primes)//2], primes[-1], *bad)
    for p in sample:
        assert (upper_moment_mod_prime(d, p) == 0) == (common % p == 0), (d, p)
    if d in (262153, 786441):
        assert common == 1
        assert len(primes) == {262153: 19558, 786441: 54247}[d]
    weight = sum(log(p) for p in primes if common % p) / d
    print(f'd={d}, count={len(primes)}, bad={bad}, gcd={common}, '
          f'product_bits={size}, T/d={weight:.10f}', flush=True)
    return common


def limit_by_coefficient(C):
    """The coefficient of the reflected rational polynomial, prior to the sign proof."""
    N = 2*C-1
    v = [Fraction(0) for _ in range(C+1)]
    for j in range(C+1):
        r = Fraction((-2)**j * comb(C+j, j)*comb(C+j, 2*j), comb(2*C+2*j, 2*j))
        for k in range(j+1):
            v[k] += r * comb(j,k)
    b = [1]
    for k in range(1, N+1):
        b.append(comb(2*C+k-1, k)-b[-1])
    return sum(x*y*b[N-i-j] for i,x in enumerate(v)
               for j,y in enumerate(v) if i+j<=N) / comb(4*C-1,N)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('--ray-exponent', type=int, action='append', default=[],
                        help='also evaluate the entire odd-prime band at d=2**s-262135')
    args = parser.parse_args()
    for d in range(1, 24):
        scalar, _ = direct_scalar(d)
        assert residue(scalar, 64) == dyadic_scalar(d, 6)
    for C in range(1, 33):
        limit = limit_by_coefficient(C)
        assert limit != 0
        assert dyadic_scalar(2**40-C, 7) == residue(limit, 128), C
    for d in range(1, 129):
        h = direct_odd_square(d)
        assert v2(h.numerator) - v2(h.denominator) == -2*d - 2 + (3*d).bit_count()
        if d <= 20:
            z = 4*(2*d-1)**2 - series_state(3*d-1)[0]
            assert v2(z.denominator) == 6*d - (3*d).bit_count()
            assert all(z.numerator % p == 0 for p in primes_between(3*d, 4*d))
    for s in (19, 20, 21, 22, 23, 24, 40, 80):
        d = 2**s-262135
        z = 2**(s-18)-1
        assert dyadic_scalar(d, 6) == (-20-36*pow(z,-1,64)) % 64
    for d in (73, 105, 169, 233):
        g = band_check(d, int)
        if d == 169:
            assert g == 359
    assert upper_moment_mod_prime(705, 2111) == 0
    if args.ray_exponent:
        from flint import fmpz
        for s in args.ray_exponent:
            if s < 19:
                parser.error('the specified ray starts at s=19')
            band_check(2**s-262135, fmpz)


if __name__ == '__main__':
    main()
