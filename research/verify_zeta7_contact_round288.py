"""Exact pole, shift and prime checks for the fourth derivative in round 288."""

from fractions import Fraction as Q
from functools import cache
from math import comb, factorial, gcd, isqrt, lcm, log, prod


@cache
def harmonic(k, order):
    return harmonic(k - 1, order) + Q(1, k**order) if k else Q(0)


@cache
def poles(n, centered=True):
    rows = []
    for k in range(n + 1):
        # Exponential of the logarithm of the regular part through degree three.
        logs = [4 * (harmonic(k, j) + (-1)**j * harmonic(n - k, j))
                for j in (1, 2, 3)]
        jet = [Q(1)]
        for j in (1, 2, 3):
            jet.append(sum(logs[i - 1] * jet[j - i] for i in range(1, j + 1)) / j)
        scale = comb(n, k)**4
        if centered:
            jet = [(n - 2*k) * value + (2 * jet[j - 1] if j else 0)
                   for j, value in enumerate(jet)]
        rows.append(tuple(scale * jet[4 - order] for order in (1, 2, 3, 4)))
    return tuple(rows)


@cache
def rational_part(n, b):
    return -sum(comb(j + 3, 4) * a * harmonic(b + k, j + 4)
                for k, row in enumerate(poles(n))
                for j, a in enumerate(row, 1))


def derivative_value(n, t, centered):
    # Differentiate the product itself using four applications of Leibniz.
    jet = [Q(1), Q(0), Q(0), Q(0), Q(0)]
    for k in range(n + 1):
        local = [Q((-1)**i * comb(3 + i, 3), (t + k)**(4 + i)) for i in range(5)]
        jet = [sum(jet[i] * local[j - i] for i in range(j + 1)) for j in range(5)]
    return factorial(n)**4 * ((2*t + n) * jet[4] + 2*jet[3] if centered else jet[4])


def residue(value, p):
    assert value.denominator % p, (value, p)
    return value.numerator * pow(value.denominator, -1, p) % p


def primes(limit):
    return [p for p in range(5, limit + 1)
            if all(p % j for j in range(2, isqrt(p) + 1))]


def check_rows():
    for n in range(25):
        coefficients = poles(n)
        totals = [sum(row[j] for row in coefficients) for j in range(4)]
        assert totals == [0, 0, 2*(-1)**n * comb(2*n, n), 0]
        for t in (1, 3, n + 3):
            partial = sum(a * Q(1, (t+k)**j) for k, row in enumerate(coefficients)
                          for j, a in enumerate(row, 1))
            assert partial == (2*t+n) * Q(factorial(n), prod(range(t, t+n+1)))**4
            difference = rational_part(n, t-1) - rational_part(n, t)
            assert difference == derivative_value(n, t, centered=True) > 0
        cap = lcm(*range(1, 2*n + 1))**8
        assert cap % rational_part(n, n).denominator == 0
    print('Exact partial fractions, period coefficients and differentiated products: n=0..24')


def check_prime_laws():
    no_carry = carry = vanishing_top = 0
    prime_list = primes(83)
    for n in range(39):
        for b in sorted({0, 1, 2, 3, 5, 8, 12, n//2, n, 2*n, 3*n + 1}):
            actual = rational_part(n, b)
            for p in prime_list:
                if p*p <= 2*(n+b+1) or p > n+b:
                    continue
                u, r = divmod(n, p)
                v, s = divmod(b, p)
                if r+s < p:
                    predicted = (-1)**r * comb(2*r, r) * rational_part(u, v)
                    assert residue(actual * p**7 - predicted, p) == 0, (n, b, p)
                    no_carry += 1
                else:
                    partial_sum = sum((r-2*c)*comb(r, c)**4 for c in range(p-s, r+1))
                    factor = derivative_value(u, v+1, centered=False)
                    assert residue(actual * p**8 + partial_sum * factor, p) == 0, (n, b, p)
                    if n == b:
                        h = p-1-r
                        reflected = sum((h+1+2*c)*comb(h+c, c)**4 for c in range(h+1))
                        assert (reflected - partial_sum) % p == 0
                    carry += 1
                    vanishing_top += residue(actual * p**8, p) == 0
    print(f'Prime-law checks: no carry={no_carry}, carry={carry} (zero top residue={vanishing_top})')


def primitive_examples():
    print('n b log(D)/n log(g)/n log(D/g)/n')
    for n in (12, 24, 48, 96, 160):
        a = rational_part(n, n)
        target = 30 * comb(2*n, n)
        g = gcd(abs(a.numerator), target)
        assert Q(-a, (-1)**n * target).denominator * g == a.denominator * target
        print(n, n, *(f'{x/n:.7f}' for x in
                       (log(a.denominator), log(g), log(a.denominator) - log(g))))


def integer_determinant(rows):
    matrix = [row.copy() for row in rows]
    size = len(matrix)
    previous = sign = 1
    for k in range(size - 1):
        if matrix[k][k] == 0:
            pivot_row = next((i for i in range(k+1, size) if matrix[i][k]), None)
            if pivot_row is None:
                return 0
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k+1, size):
            for j in range(k+1, size):
                value = pivot*matrix[i][j] - matrix[i][k]*matrix[k][j]
                quotient, remainder = divmod(value, previous)
                assert remainder == 0
                matrix[i][j] = quotient
        previous = pivot
    return sign * matrix[-1][-1]


def primitive_hankel(m):
    constants, leading, row_denominators = [], [], []
    for i in range(m):
        terms = [(rational_part(k, k) / k, Q(30 * (-1)**k * comb(2*k, k), k))
                 for k in range(i+1, i+m+1)]
        multiplier = lcm(*(value.denominator for pair in terms for value in pair))
        constants.append([int(a * multiplier) for a, _ in terms])
        leading.append([int(b * multiplier) for _, b in terms])
        row_denominators.append(multiplier)

    def at(x):
        return integer_determinant([[a + x*b for a, b in zip(ar, br)]
                                    for ar, br in zip(constants, leading)])

    differences = [at(x) for x in range(m+1)]
    falling = [1]
    coefficients = [Q(0)] * (m+1)
    for k in range(m+1):
        for j, value in enumerate(falling):
            coefficients[j] += Q(differences[0] * value, factorial(k))
        differences = [right - left for left, right in zip(differences, differences[1:])]
        following = [0] * (len(falling)+1)
        for j, value in enumerate(falling):
            following[j] -= k*value
            following[j+1] += value
        falling = following
    assert all(value.denominator == 1 for value in coefficients)
    assert coefficients[-1] == integer_determinant(leading)
    assert (-1)**m * coefficients[-1] > 0
    assert at(-2) == sum(value * (-2)**j for j, value in enumerate(coefficients))
    return Q(prod(row_denominators), gcd(*(int(value) for value in coefficients)))


def hankel_examples():
    print('m  log(kappa)/m^2')
    for m in (1, 2, 3, 4, 6, 8, 10, 12):
        kappa = primitive_hankel(m)
        print(m, f'{(log(kappa.numerator)-log(kappa.denominator))/m**2:.8f}')


def modular_hankel(anti_diagonals, size, p, scaled_rows=None):
    matrix = [[anti_diagonals[i+j] for j in range(size)] for i in range(size)]
    if scaled_rows:
        start, entries = scaled_rows
        for i in range(start, size):
            matrix[i] = [entries[i+j] for j in range(size)]
    determinant = 1
    for i in range(size):
        pivot = next((k for k in range(i, size) if matrix[k][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            matrix[i], matrix[pivot] = matrix[pivot], matrix[i]
            determinant = -determinant
        determinant = determinant * matrix[i][i] % p
        inverse = pow(matrix[i][i], -1, p)
        for k in range(i+1, size):
            multiplier = matrix[k][i] * inverse % p
            if multiplier:
                for j in range(i+1, size):
                    matrix[k][j] = (matrix[k][j] - multiplier*matrix[i][j]) % p
    return determinant


@cache
def target_moment(k):
    return Q(30 * (-1)**k * comb(2*k, k), k)


def check_outer_band():
    checks = 0
    for m in range(4, 14):
        for p in primes(4*m - 2):
            if p <= max(2*m, 13):
                continue
            first = (p+1)//2
            a = first-m
            e = m-a
            unit = pow(-1, e*(e-1)//2) * pow(455 * pow(16, -1, p), e, p)
            # Degree <= m < p, so these m+1 values test the whole polynomial.
            for x in range(m+1):
                values = [rational_part(k, k)/k + x*target_moment(k) for k in range(1, 2*m)]
                # Top a rows never use positions k >= first.
                top = [residue(v, p) if k < first else 0 for k, v in enumerate(values, 1)]
                last = [residue(v * p**8, p) for v in values]
                full = modular_hankel(top, m, p, (a, last))
                assert full == unit * modular_hankel(top, a, p) % p
                checks += 1
    print(f'Full outer-band polynomial identity: {checks} evaluation checks')
    print('m  primes  nonzero-leading-coefficient  nonzero-polynomial')
    for m in (16, 32, 64, 128):
        total = leading_units = good = 0
        for p in primes(4*m-2):
            if p <= max(2*m, 13):
                continue
            a = (p+1)//2-m
            target = [residue(target_moment(k), p) for k in range(1, 2*a)]
            total += 1
            if modular_hankel(target, a, p):
                leading_units += 1
                good += 1
                continue
            constant = [residue(rational_part(k, k)/k, p) for k in range(1, 2*a)]
            for x in range(a+1):
                if modular_hankel([(v+x*w) % p for v, w in zip(constant, target)], a, p):
                    good += 1
                    break
        print(m, total, leading_units, good)


def check_slopes():
    checks = 0
    for a, c in ((1, 2), (2, 1), (2, 3), (3, 2)):
        step = a+c
        for m in (4, 7, 10):
            terms = [(rational_part(c*k, a*k)/(c*k), target_moment(c*k))
                     for k in range(1, 2*m)]
            for p in primes(step*(2*m-1)-1):
                if p <= step*m:
                    continue
                first = (p+step-1)//step
                ell = step*first-p
                z = Q(c*ell, step)
                generalized_binomial = Q(1)
                low = -z
                for j in range(1, ell+1):
                    generalized_binomial *= (z-j+1)/j
                    low += (2*j-z) * generalized_binomial**4
                assert low != 0
                coefficient = residue(-35*low/z, p)
                assert coefficient == residue(terms[first-1][0]*p**8, p)
                small = first-m
                e = m-small
                factor = (-1)**(e*(e-1)//2) * pow(coefficient, e, p)
                for x in range(m+1):
                    values = [constant+x*target for constant, target in terms]
                    top = [residue(v, p) if k < first else 0 for k, v in enumerate(values, 1)]
                    last = [residue(v*p**8, p) for v in values]
                    lhs = modular_hankel(top, m, p, (small, last))
                    assert lhs == factor * modular_hankel(top, small, p) % p
                    checks += 1
    print(f'Rational-slope determinant law: {checks} evaluation checks at four slopes')


if __name__ == '__main__':
    check_rows()
    check_prime_laws()
    primitive_examples()
    hankel_examples()
    check_outer_band()
    check_slopes()
