"""Independent exact rank audit and geometric formulas for Gr(2,4).

This reads the producer's coefficient file, but does not import its helpers.
It certifies the rational kernel by exact integer multiplication and records
which two relations have universal Hankel/exterior explanations.
"""
import itertools
import json
import math
import sys
from pathlib import Path

from flint import fmpq_mat as QMat, fmpz_mat as ZMat

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def primitive_integer(vector):
    den = math.lcm(*(int(x.denominator) for x in vector))
    values = [int(x * den) for x in vector]
    common = math.gcd(*values)
    values = [x // common for x in values]
    if next(x for x in values if x) < 0:
        values = [-x for x in values]
    return values


def main():
    data = json.loads((ROOT / 'zeta35_two_row_pencil.json').read_text())
    quadratic = list(itertools.combinations_with_replacement(range(6), 2))
    assert data['quadratic_monomials'] == [list(x) for x in quadratic]
    coefficients = list(map(list, zip(*data['coefficients'])))
    F = QMat(coefficients)
    reduced, rank = F.rref()
    pivots = [next(j for j in range(21) if reduced[i, j]) for i in range(rank)]
    free = [j for j in range(21) if j not in pivots]
    kernels = []
    for j in free:
        vector = [F[0, 0] * 0 for _ in range(21)]
        vector[j] = F[0, 0] * 0 + 1
        for i, pivot in enumerate(pivots):
            vector[pivot] = -reduced[i, j]
        kernels.append(primitive_integer(vector))
    integer_F = ZMat(coefficients)
    for vector in kernels:
        assert integer_F * ZMat([[x] for x in vector]) == ZMat(68, 1)
    assert QMat(kernels).rank() == len(kernels) == 4
    assert rank == 17

    # In monomial tails, the normalized alternants are
    # 1, e1, e1^2-e2, e2, e1*e2-e3, e2^2-e1*e3.
    # Hence s1^2=s2+s11 and s22=s1*s21-s2*s11.
    # The second is the compound-matrix Bianchi relation. A lower Toeplitz
    # basis change preserves the first; tail weight 83 gives the coefficient
    # below. These are relations between coefficient polynomials, not extra
    # equations that parameter Pluecker coordinates must satisfy.
    hankel_relation = [0] * 21
    hankel_relation[quadratic.index((0, 2))] = -1
    hankel_relation[quadratic.index((0, 3))] = -83
    hankel_relation[quadratic.index((1, 1))] = 166
    bianchi = [0] * 21
    for pair, sign in [((0, 5), 1), ((1, 4), -1), ((2, 3), 1)]:
        bianchi[quadratic.index(pair)] = sign
    for relation in [hankel_relation, bianchi]:
        assert integer_F * ZMat([[x] for x in relation]) == ZMat(68, 1)

    # The Pluecker equation has the same vector as the Bianchi relation,
    # but is used as an extra ROW in the ideal rather than a kernel COLUMN.
    extended = QMat(coefficients + [bianchi])
    assert extended.rank() == 18
    result = dict(
        coefficient_rank=rank,
        extended_rank=18,
        monomials=[list(x) for x in quadratic],
        pivot_columns=pivots,
        free_columns=free,
        primitive_integer_kernel=kernels,
        universal_hankel_relation=hankel_relation,
        universal_bianchi_relation=bianchi,
        exact_kernel_checks=4 * 68,
        interpretation=(
            'Degree-two rank deficiency does not imply a projective basepoint. '
            'The separate degree-three Macaulay rank certificate is required.'
        ),
    )
    (ROOT / 'zeta35_two_row_geometry_verified.json').write_text(
        json.dumps(result, indent=2)
    )
    print('rank', rank, 'extended', 18, 'kernel equations', 4 * 68)
    for relation in kernels:
        print([(quadratic[j], value) for j, value in enumerate(relation) if value])


if __name__ == '__main__':
    main()
