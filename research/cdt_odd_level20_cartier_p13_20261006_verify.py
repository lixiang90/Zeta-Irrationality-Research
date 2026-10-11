"""Independent, single-prime p=13 Hecke computation. No old producer imports.

The eta coordinate is reconstructed by its integer logarithmic derivative,
the character Eisenstein series by divisor sums, and both six-function bases
by exact series division. Full weight-four Sturm prefixes certify T_13.
"""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import hashlib
import json

P = 13
STURM = 12
ORDER = P * STURM
ZERO = (0, 0)
ONE = (1, 0)
labels = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    labels.append(label)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def scalar(x, n):
    return (n * x[0], n * x[1])


def inverse(x):
    norm = x[0] * x[0] - 5 * x[1] * x[1]
    return (F(x[0], norm), F(-x[1], norm))


def convolution(x, y):
    result = [ZERO] * (ORDER + 1)
    for i, a in enumerate(x[:ORDER + 1]):
        if a == ZERO:
            continue
        for j, b in enumerate(y[:ORDER + 1 - i]):
            if b != ZERO:
                result[i + j] = add(result[i + j], mul(a, b))
    return result


def series_inverse(x):
    assert x[0] == ONE
    result = [ONE] + [ZERO] * ORDER
    for n in range(1, ORDER + 1):
        value = ZERO
        for i in range(1, n + 1):
            value = add(value, mul(x[i], result[n - i]))
        result[n] = neg(value)
    return result


def polynomial_product(x, y):
    result = [ZERO] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            result[i + j] = add(result[i + j], mul(a, b))
    return result


def matrix_product(x, y):
    result = []
    for row in x:
        line = []
        for column in zip(*y):
            value = ZERO
            for a, b in zip(row, column):
                value = add(value, mul(a, b))
            line.append(value)
        result.append(line)
    return result


def matrix_add(x, y):
    return [[add(a, b) for a, b in zip(row, other)] for row, other in zip(x, y)]


def matrix_scale(x, n):
    return [[scalar(a, n) for a in row] for row in x]


def determinant(x):
    rows = [[(F(a), F(b)) for a, b in row] for row in x]
    result = ONE
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if rows[i][j] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            rows[pivot], rows[j] = rows[j], rows[pivot]
            result = neg(result)
        value = rows[j][j]
        result = mul(result, value)
        inv = inverse(value)
        for i in range(j + 1, len(rows)):
            multiplier = mul(rows[i][j], inv)
            rows[i] = [sub(a, mul(multiplier, b)) for a, b in zip(rows[i], rows[j])]
    return result


def mod_rank(x):
    rows = [[(a % P, b % P) for a, b in row] for row in x]
    pivots = []
    current = 0
    for j in range(len(rows[0])):
        pivot = next((i for i in range(current, len(rows)) if rows[i][j] != ZERO), None)
        if pivot is None:
            continue
        rows[current], rows[pivot] = rows[pivot], rows[current]
        a, b = rows[current][j]
        norm = (a * a - 5 * b * b) % P
        inv_norm = pow(norm, -1, P)
        inv = (a * inv_norm % P, -b * inv_norm % P)
        rows[current] = [(u % P, v % P) for u, v in (mul(entry, inv) for entry in rows[current])]
        for i in range(len(rows)):
            if i == current:
                continue
            factor = rows[i][j]
            rows[i] = [(u % P, v % P) for u, v in
                       (sub(a0, mul(factor, b0)) for a0, b0 in zip(rows[i], rows[current]))]
        pivots.append(j)
        current += 1
        if current == len(rows):
            break
    return current, pivots


def chi(n):
    return (0, 1, -1, -1, 1)[n % 5]


def sigma1(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


# t=q*F_eta. Euler's logarithmic-derivative recursion is independent of
# the historical eta-product multiplication implementation.
eta_exponents = {1: 3, 2: -4, 4: 1, 5: 1, 10: -4, 20: 3}
logarithmic = [0] + [
    -sum(exponent * divisor * sigma1(n // divisor)
         for divisor, exponent in eta_exponents.items() if n % divisor == 0)
    for n in range(1, ORDER + 1)
]
eta_coefficients = [1] + [0] * ORDER
for n in range(1, ORDER + 1):
    value = sum(logarithmic[k] * eta_coefficients[n - k] for k in range(1, n + 1))
    assert value % n == 0
    eta_coefficients[n] = value // n
t = [ZERO] + [(x, 0) for x in eta_coefficients[:ORDER]]
S = [ONE] + [(x, 0) for x in logarithmic[1:]]
check("Independent eta recursion matches fixed coordinate normalization", t[:7] == [(0, 0), (1, 0), (-3, 0), (4, 0), (-7, 0), (13, 0), (-20, 0)])
E5 = [(-1, 0)] + [(5 * sum(chi(d) * d for d in range(1, n + 1) if n % d == 0), 0) for n in range(1, ORDER + 1)]
F2 = [ZERO] + [(sum(chi(d) * (n // d) for d in range(1, n + 1) if n % d == 0), 0) for n in range(1, ORDER + 1)]
F2_at4 = [F2[n // 4] if n % 4 == 0 else ZERO for n in range(ORDER + 1)]
t_powers = [[ONE] + [ZERO] * ORDER]
for j in range(1, 6):
    t_powers.append(convolution(t_powers[-1], t))
bases = {}
for sign in (-1, 1):
    A5 = [add(e, (0, sign * 20 * f[0])) for e, f in zip(E5, F2_at4)]
    Npoly = [ONE, (-6, sign), (1, -sign)]
    Cpoly = [ONE, (-6, -2 * sign), (6, 2 * sign)]
    Dpoly = polynomial_product(polynomial_product([ONE, (-1, 0)], Npoly), Cpoly)
    Dseries = [ZERO] * (ORDER + 1)
    for j, coefficient in enumerate(Dpoly):
        Dseries = [add(a, mul(coefficient, b)) for a, b in zip(Dseries, t_powers[j])]
    base = convolution(convolution(A5, S), series_inverse(Dseries))
    bases[sign] = [convolution(base, power) for power in t_powers]
    check(f"Six basis leading coefficient units sign={sign}", all(bases[sign][j][j] == (-1, 0) and all(a == ZERO for a in bases[sign][j][:j]) for j in range(6)))

matrices = {}
eps = chi(P)
for sign in (-1, 1):
    target = sign * eps
    columns = []
    for j, series in enumerate(bases[sign]):
        residual = [add(series[P * n], scalar(series[n // P], eps * P ** 3)) if n % P == 0 else series[P * n] for n in range(STURM + 1)]
        coordinates = []
        for i in range(6):
            coordinate = neg(residual[i])
            coordinates.append(coordinate)
            residual = [sub(a, mul(coordinate, b)) for a, b in zip(residual, bases[target][i])]
        check(f"Complete weight-four Sturm equality sign={sign} basis={j}", all(a == ZERO for a in residual))
        columns.append(coordinates)
    matrices[sign] = [list(row) for row in zip(*columns)]
check("Character at the single selected prime is minus one", eps == -1)
check("sqrt5 is inert at13", pow(5, (P - 1) // 2, P) == P - 1)
check("The two complete Hecke matrices are conjugate", matrices[1] == [[(a, -b) for a, b in row] for row in matrices[-1]])

# Explicit level-ten cusp forms u=hF/24 and v=(u-hE/24)/4.
ordinary = {}
for d in (2, 5, 10):
    ordinary[d] = [(d - 1, 0)] + [(24 * sigma1(n) - (24 * d * sigma1(n // d) if n % d == 0 else 0), 0) for n in range(1, ORDER + 1)]
comb_E = [add(add(scalar(a, -5), neg(b)), c) for a, b, c in zip(ordinary[2], ordinary[5], ordinary[10])]
comb_F = [add(add(neg(a), scalar(b, -5)), scalar(c, 5)) for a, b, c in zip(ordinary[2], ordinary[5], ordinary[10])]
hE5 = convolution(E5, comb_E)
hF = convolution(F2, comb_F)
check("Explicit cusp products have exact normalization divisibility", all(a % 120 == 0 and b == 0 for a, b in hE5) and all(a % 24 == 0 and b == 0 for a, b in hF))
e_cusp = [a // 120 for a, b in hE5]
u_cusp = [a // 24 for a, b in hF]
check("Explicit level10 v normalization is integral", all((u - e) % 4 == 0 for u, e in zip(u_cusp, e_cusp)))
v_cusp = [(u - e) // 4 for u, e in zip(u_cusp, e_cusp)]
cusp_columns = []
for j, series in enumerate((u_cusp, v_cusp)):
    image = [series[P * n] + (eps * P ** 3 * series[n // P] if n % P == 0 else 0) for n in range(7)]
    coordinates = [image[1], image[2]]
    check(f"Explicit level10 cusp T13 Sturm equality basis={j}", all(image[n] == coordinates[0] * u_cusp[n] + coordinates[1] * v_cusp[n] for n in range(7)))
    cusp_columns.append(coordinates)
T13_level10 = [list(row) for row in zip(*cusp_columns)]
old_scalar = -T13_level10[0][1]
check("Level10 T13 has the exact nonsplit T3 shape", T13_level10 == [[0, -old_scalar], [4 * old_scalar, 0]])

determinants = {sign: determinant(matrix) for sign, matrix in matrices.items()}
ranks = {sign: mod_rank(matrix) for sign, matrix in matrices.items()}
check("Both exact determinants are integers in Z[sqrt5]", all(a.denominator == b.denominator == 1 for a, b in determinants.values()))
check("Both mod13 matrices have full rank6", all(rank == 6 for rank, pivots in ranks.values()))

# The already frozen T3 matrices are read as data only, for optional
# old/new spectral identification; no old code is imported or executed.
frozen = Path(__file__).with_name("cdt_odd_level20_hecke_space_20261006.json")
prior = json.loads(frozen.read_text(encoding="utf-8"))
decode = lambda matrix: [[tuple(int(value) for value in entry) for entry in row] for row in matrix]
U = matrix_product(decode(prior["matrices"]["3:1"]), decode(prior["matrices"]["3:-1"]))
T13_squared = matrix_product(matrices[1], matrices[-1])
identity = [[ONE if i == j else ZERO for j in range(6)] for i in range(6)]
spectral = {}
for label, eigen, dimension in (("Eisenstein", 676, 3), ("old_cusp", -4, 2), ("new_cusp", -76, 1)):
    projector = identity
    denominator = 1
    for other in (676, -4, -76):
        if other != eigen:
            projector = matrix_product(projector, matrix_add(U, matrix_scale(identity, -other)))
            denominator *= eigen - other
    projector = matrix_scale(projector, F(1, denominator))
    image = matrix_product(T13_squared, projector)
    trace = ZERO
    for i in range(6):
        trace = add(trace, image[i][i])
    value = scalar(trace, F(1, dimension))
    check(f"T13 squared scalar on frozen {label} component", image == matrix_scale(projector, value[0]) if value[1] == 0 else False)
    spectral[label] = [str(value[0]), str(value[1])]
check("Eisenstein eigenvalue squared matches one-minus-p-cubed", spectral["Eisenstein"] == [str((1 - P ** 3) ** 2), "0"])
check("Old cusp squared scalar matches explicit level10 matrix", spectral["old_cusp"] == [str(-4 * old_scalar ** 2), "0"])

encode = lambda matrix: [[[str(a), str(b)] for a, b in row] for row in matrix]
result = {
    "scope": "Only p=13; full weight-four Sturm identities on both actual six-dimensional Fricke spaces, plus explicit level10 cusp verification. No prime scan, no Hecke-kernel density or Smith claim.",
    "prime": P,
    "series_precision": ORDER,
    "sturm_degree": STURM,
    "checks_passed": len(labels),
    "check_labels": labels,
    "matrix_convention": "column j is coordinates of T13 B_j(source sign), target sign=source sign*chi5(13); r^2=5; both bases scaled by5, which cancels from the matrix",
    "matrices": {str(sign): encode(matrix) for sign, matrix in matrices.items()},
    "exact_determinants": {str(sign): [str(a), str(b)] for sign, (a, b) in determinants.items()},
    "mod13_determinants": {str(sign): [int(a) % P, int(b) % P] for sign, (a, b) in determinants.items()},
    "mod13_ranks": {str(sign): rank for sign, (rank, pivots) in ranks.items()},
    "mod13_pivot_columns": {str(sign): pivots for sign, (rank, pivots) in ranks.items()},
    "level10_T13_matrix": T13_level10,
    "level10_nonsplit_scalar": old_scalar,
    "T13_squared_spectral_values": spectral,
    "frozen_T3_data_sha256": hashlib.sha256(frozen.read_bytes()).hexdigest(),
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: result[key] for key in ("prime", "checks_passed", "exact_determinants", "mod13_ranks", "level10_T13_matrix", "T13_squared_spectral_values")}, ensure_ascii=False))
