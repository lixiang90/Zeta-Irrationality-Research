"""Exact finite checks for the two-moment band, the transfer and its positive minors."""

from fractions import Fraction as F
from itertools import combinations
from math import isqrt, log

from verify_odd_pade_round284 import integral_head


def parameters(q):
    return -F(4*q + 1, 12), F(5 - 4*q, 12), F(7 - 2*q, 6)


def series_state(q):
    a, b, c = parameters(q)
    coeff = [F(1)]
    prefix = [F(1)]
    for i in range(q + 1):
        coeff.append(coeff[-1] * (a + i) * (b + i) / ((c + i) * (i + 1)))
        prefix.append(prefix[-1] + coeff[-1])
    total = sum(coeff[i] * prefix[q - i] for i in range(q + 1))
    last = sum(coeff[i] * coeff[q - i] for i in range(q + 1))
    following = sum(coeff[i] * coeff[q + 1 - i] for i in range(q + 2))
    return total, last, following


def advance(q, state):
    """Transfer W3 and W5 evaluated in rational arithmetic."""
    a, b, c = parameters(q)
    x, y, h = c - 1, a + b, a*b
    alpha = ((2 - c) / x)**2

    def middle(i):
        return -2*i**3 - 3*(y+x)*i**2 + (-4*y*x-4*h-y+x)*i - 2*h*(2*x+1)

    def square_operator(i):
        def evaluate(z):
            A = z*h / (1-z)
            B = (z*y-x) / (1-z)
            w = (1-z) / x
            v = 1-z + (2-c)*z/x
            return v*v - A*w*w + (v*w - B*w*w/2)*i + w*w*i*i/2

        p0 = evaluate(0)
        minus_one = evaluate(-1)
        p1 = (alpha - minus_one) / 2
        return p0, p1, alpha - p0 - p1

    total, last, following = state
    coeff = {q: last, q + 1: following}
    for i in range(q, q + 3):
        lead = (i+2) * (i+2+x) * (i+2+2*x)
        tail = (i+2*a) * (i+y) * (i+2*b)
        coeff[i+2] = -(middle(i+1)*coeff[i+1] + tail*coeff[i]) / lead
    operators = {i: square_operator(i) for i in range(q+1, q+5)}
    new_total = (alpha * (total + following)
                 + sum(operators[q+2][:2]) * coeff[q+2] + operators[q+3][0] * coeff[q+3])
    new_coeff = [sum(operators[i-j][j] * coeff[i-j] for j in range(3)) for i in (q+3, q+4)]
    return new_total, *new_coeff


def check_positive_matrix():
    limit = [[1, -F(2, 9), F(35, 18)], [0, -F(1, 18), F(11, 18)],
             [0, -F(11, 108), F(49, 108)]]
    change = [[1, 0, 0], [-F(5, 4), F(3, 2), -F(1, 4)], [-F(1, 2), F(1, 2), 0]]
    positive = [[66, 138, 12], [23, 170, 23], [12, 138, 66]]
    for i in range(3):
        for j in range(3):
            assert 216*sum(limit[i][k]*change[k][j] for k in range(3)) == sum(
                change[i][k]*positive[k][j] for k in range(3))
    minors = [[positive[i][k]*positive[j][l] - positive[i][l]*positive[j][k]
               for k, l in combinations(range(3), 2)] for i, j in combinations(range(3), 2)]
    assert minors == [[8046, 1242, 1134], [7452, 4212, 7452], [1134, 1242, 8046]]
    assert 66*minors[2][2] - 138*minors[2][1] + 12*minors[2][0] == 373248


def residue(value, modulus):
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def check_original(d):
    head, at_minus_one, scale = integral_head(d)
    moment = sum(F(value, i**7) for i, value in enumerate(head, 1)) / at_minus_one**2
    common = 4*(2*d-1)**2 - series_state(3*d-1)[0]
    good, bad = [], []
    for p in range(max(128, 2*d+1), 3*d):
        if any(p % i == 0 for i in range(2, isqrt(p) + 1)):
            continue
        raw = F(head[2*p-1], scale**2)
        upper = series_state(3*d-1-p)[0]
        assert residue(raw, p) == residue(upper, p) == residue(4*common, p)
        retains_seven = moment.denominator % p**7 == 0
        assert retains_seven == (residue(raw, p) != 0)
        assert moment.denominator % p**8 != 0
        (good if retains_seven else bad).append(p)
        if (d, p) == (169, 359):
            assert residue(F(head[p-1], scale**2), p**2) == 199*p
            assert residue(raw, p**2) == 231*p
            assert residue(moment * p**7, p**2) == 200*p
            assert moment.denominator % p**6 == 0
    if d == 169:
        assert bad == [359] and len(good) == 27
    print(f"d={d}: {len(good)} of {len(good)+len(bad)} primes retain seven layers, "
          f"T/d={sum(log(p) for p in good)/d:.10f}, exceptions={bad}")


if __name__ == "__main__":
    check_positive_matrix()
    for index in range(26):
        assert advance(index, series_state(index)) == series_state(index + 3)
    assert series_state(3)[0] == F(116105, 5184)
    for degree in (73, 105, 169, 233):
        check_original(degree)
    print("Transfer, minors, original scalar and common rational all agree.")
