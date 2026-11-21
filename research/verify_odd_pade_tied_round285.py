"""Check the complete weight-seven scalar modulo 8, including the two large examples."""

from fractions import Fraction
from math import comb, prod

from verify_odd_pade_round284 import integral_head, product


def v2(integer):
    """Exponent of two in a nonzero integer."""
    return (integer & -integer).bit_length() - 1


def residue(value, modulus):
    """A canonical residue, also for rationals with an even denominator."""
    scale = 1 << v2(value.denominator)
    odd = value.denominator // scale
    lifted_modulus = modulus * scale
    return Fraction(value.numerator * pow(odd, -1, lifted_modulus) % lifted_modulus, scale)


def direct_scalar(d):
    head, at_minus_one, _ = integral_head(d)
    moment = sum(Fraction(value, k**7) for k, value in enumerate(head, 1)) / at_minus_one**2
    n = 2 * d
    base = sum(Fraction((-1)**i * comb(n - 1, i), (n + 1 + i)**7) for i in range(n))
    return 4**d * moment / base, moment.denominator


def beta_ratio(d, t):
    n = 2 * d
    if t >= 0:
        return Fraction(prod(range(n, n + t)), prod(range(2*n + 1, 2*n + t + 1)))
    return Fraction(prod(range(2*n + t + 1, 2*n + 1)), prod(range(n + t, n)))


def positive_g(d, t, bits):
    """Compute g_t from the original R_m(2-z)^2 modulo 2**bits (C3)."""
    m = d - 1
    degree = min(m, bits - 1)
    modulus = 1 << bits
    translated = [0] * (degree + 1)
    for j in range(degree + 1):
        coefficient = Fraction(2**j * comb(m, j) * comb(m + j, 2*j), comb(2*m + 1, 2*j))
        coefficient_mod = coefficient.numerator * pow(coefficient.denominator, -1, modulus) % modulus
        for i in range(j + 1):
            translated[i] += coefficient_mod * comb(j, i) * (-1)**i * 2**(j - i)
    square = product(translated, translated)
    return sum(square[j] << (j - t) for j in range(t, len(square))) % modulus


def scaled_h6(lo, hi, exponent, bits):
    """h_6(2**exponent / i) for lo <= i <= hi, omitting zero residues."""
    modulus = 1 << bits
    step = 1 << max(0, exponent - bits + 1)
    first = (lo + step - 1) // step * step
    h = [1, 0, 0, 0, 0, 0, 0]
    for i in range(first, hi + 1, step):
        order = v2(i)
        variable = (1 << (exponent - order)) * pow(i >> order, -1, modulus)
        for j in range(1, 7):
            h[j] = (h[j] + variable * h[j - 1]) % modulus
    return h[6]


def beta_sum_mod8(d):
    """Evaluate D1 without using K(d), a tie classification, or either proposed congruence."""
    n = 2 * d
    exponent = (2 * n).bit_length() - 1
    # Every normalized moment has valuation >= |t|-exponent-6.
    # The constant head has valuation 2d+7+v2(2d)+s2(2d)-exponent >= 3.
    cutoff = exponent + 8
    total = Fraction()
    for t in range(max(1 - n, -cutoff), min(n - 2, cutoff) + 1):
        # The highest differing bit of n and end gives the largest valuation on [n+1, end].
        end = 2*n + t
        local_exponent = (n ^ end).bit_length() - 1
        factor = beta_ratio(d, t) * Fraction(2)**(6 * (exponent - local_exponent))
        factor_order = v2(factor.numerator) - v2(factor.denominator)
        if abs(t) + factor_order >= 3:
            continue
        g = positive_g(d, t, 3 - factor_order) if t > 0 else 1 << -t
        if g == 0:
            continue
        bits = 3 - factor_order - v2(g)
        if bits <= 0:
            continue
        base = scaled_h6(n + 1, 2*n, exponent, bits)
        numerator = scaled_h6(n + 1, end, local_exponent, bits)
        quotient = numerator * pow(base, -1, 1 << bits) % (1 << bits)
        total -= g * factor * quotient
    return residue(total, 8)


def main():
    # Cross-check the truncated calculation against the original rational polynomial and all its moments.
    expected = {9: 4, 25: 6, 41: 0, 57: 2, 73: 4}
    for d in sorted(set(range(1, 20)) | set(expected)):
        scalar, denominator = direct_scalar(d)
        observed = residue(scalar, 8)
        assert beta_sum_mod8(d) == observed, d
        if d in expected:
            assert observed == expected[d], d
            print(f"d={d}: J mod 8 = {observed}, v2(c) = {v2(denominator)}")
    exceptional = 9 + 2**18
    outside_singleton = 9 + 2**19
    assert beta_sum_mod8(exceptional) == 0
    other_residue = beta_sum_mod8(outside_singleton)
    assert other_residue % 4 == 2
    print(f"d={exceptional}: J mod 8 = 0")
    print(f"d={outside_singleton}: J mod 8 = {other_residue} (mod 4 = 2)")

    # Bound all omitted singleton classes by a geometric series, with rational rounding.
    last = 24
    singleton = sum(Fraction(1, 2**(2*k + v2(k) + k.bit_count() + 1)) for k in range(1, last + 1))
    remainder = Fraction(1, 12 * 4**last)
    multiple = Fraction(2, 3 * 4**9)
    after_four = 1 - singleton - remainder - multiple + Fraction(1, 32)
    after_eight = after_four + Fraction(1, 64) - Fraction(1, 2**19)
    assert after_four > Fraction("0.95859551631")
    assert after_eight > Fraction("0.97421860896")


if __name__ == "__main__":
    main()
