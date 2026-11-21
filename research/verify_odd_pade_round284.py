"""Exact finite checks for the scalar and the two exceptional primes of round 284."""

from fractions import Fraction
from math import comb, lcm


def product(left, right):
    coefficients = [0] * (len(left) + len(right) - 1)
    for i, value in enumerate(left):
        if value:
            for j, other in enumerate(right):
                coefficients[i + j] += value * other
    return coefficients


def integral_head(d):
    """Return the coefficients of D² W, D P(-1), and D for the monic S5."""
    m = d - 1
    translated = [Fraction(1)]
    for j in range(1, m + 1):
        ratio = Fraction((m - j + 1) * (2 * j + 1), j * (2 * m - j + 1))
        translated.append(translated[-1] * ratio)
    scale = lcm(*(value.denominator for value in translated))
    ascending = [int(scale * value) for value in reversed(translated)]
    monomial = [
        sum(ascending[j] * comb(j, i) for j in range(i, m + 1))
        for i in range(m + 1)
    ]
    factor = [(-1) ** j * comb(d, j) for j in range(d + 1)]
    polynomial = [0] * d + product(factor, monomial)
    at_minus_one = sum((-1) ** j * value for j, value in enumerate(polynomial))
    square = product(polynomial, polynomial)
    head = [0] * (len(square) - 1)
    above = 0
    for k in range(len(square) - 1, 0, -1):
        above = square[k] - above
        head[k - 1] = above
    assert head[0] == square[0] - at_minus_one**2
    assert at_minus_one == (-1) ** d * 2 * (2 * d - 1) * scale
    return head, at_minus_one, scale


def main():
    for d, prime, digit in [(29, 103, 24), (594, 2371, 1564)]:
        head, _, scale = integral_head(d)
        modulus = prime**3
        coefficient = head[prime - 1] * pow(scale**2, -1, modulus) % modulus
        assert coefficient == digit * prime**2
        print(f"d={d}, p={prime}: C/p^2 = {digit} mod p")

    # A tied minimum, the k=1 and k=2 corrections, and an exact power of two.
    for d, expected in [(9, 49), (17, 74), (64, 184), (130, 319)]:
        head, at_minus_one, _ = integral_head(d)
        rational = -sum(Fraction(value, k**7) for k, value in enumerate(head, 1))
        denominator = (rational / at_minus_one**2).denominator
        exponent = (denominator & -denominator).bit_length() - 1
        assert exponent == expected
        print(f"w=7, d={d}: v2(denominator) = {exponent}")


if __name__ == "__main__":
    main()
