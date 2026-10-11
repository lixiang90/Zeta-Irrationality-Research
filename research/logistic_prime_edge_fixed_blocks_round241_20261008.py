"""One bounded exact check of three fixed V3 Gram blocks; no prime scan.

The functional is recomputed from integer monic division and every residue.
This is an arithmetic check of independently derived paper constants, not
evidence by sampling for a varying-prime assertion.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def multiply(a, b):
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def divide_monic(a, b):
    a = list(a)
    quotient = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coefficient = a[-1]
        quotient[shift] = coefficient
        for j, y in enumerate(b):
            a[shift + j] -= coefficient * y
        a.pop()
    return quotient


def v3_monomial_over_nodes(exponent, nodes):
    denominator = [F(1)]
    for j in nodes:
        denominator = multiply(denominator, [F(j), F(1)])
    quotient = divide_monic([F(0)] * exponent + [F(1)], denominator)
    # All quotients here have degree at most 3, so only their cubic term
    # survives three differentiations; B_0^+ = 1.
    assert len(quotient) <= 4
    polynomial_value = 6 * quotient[3] if len(quotient) == 4 else F(0)
    pole_value = F(0)
    for j in nodes:
        residue_denominator = 1
        for k in nodes:
            if k != j:
                residue_denominator *= k - j
        residue = F((-j) ** exponent, residue_denominator)
        harmonic = sum((F(1, a ** 5) for a in range(1, j + 1)), F(0))
        pole_value += 24 * residue * harmonic
    return polynomial_value + pole_value


def determinant(matrix):
    a = [list(row) for row in matrix]
    result = F(1)
    for column in range(len(a)):
        pivot = next((j for j in range(column, len(a)) if a[j][column]), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            a[pivot], a[column] = a[column], a[pivot]
            result = -result
        entry = a[column][column]
        result *= entry
        for j in range(column + 1, len(a)):
            ratio = a[j][column] / entry
            for k in range(column + 1, len(a)):
                a[j][k] -= ratio * a[column][k]
            a[j][column] = F(0)
    return result


def prime_factors(value):
    value = abs(value)
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            power = 0
            while value % divisor == 0:
                value //= divisor
                power += 1
            factors.append([divisor, power])
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors.append([value, 1])
    return factors


records = []
for name, offset, nodes, size in [
    ('zero', 1, (1, 2, 3, 4), 4),
    ('low', 3, (1, 2, 3, 4), 3),
    ('high', 3, (1, 2, 3), 2),
]:
    moments = [v3_monomial_over_nodes(offset + e, nodes)
               for e in range(2 * size - 1)]
    matrix = [[moments[i + j] for j in range(size)] for i in range(size)]
    det = determinant(matrix)
    records.append({'type': name, 'size': size,
                    'moments': [str(x) for x in moments],
                    'determinant': str(det),
                    'numerator_factors': prime_factors(det.numerator),
                    'denominator_factors': prime_factors(det.denominator)})

payload = {'round': 241, 'kind': 'single bounded exact constant check',
           'variable_prime_sampling': False, 'blocks': records,
           'does_not_prove': ['full distribution', 'full varying-prime determinant',
                             'irrationality', 'all-prime primitive cost']}
destination = Path(__file__).with_suffix('.json')
assert not destination.exists(), 'Do not rerun a completed recorded arithmetic check'
destination.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
print(json.dumps(payload, indent=2))
