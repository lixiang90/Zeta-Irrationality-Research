"""Exact checks for the linear-form parameter-space quotient.

These checks concern rational coefficient maps, not the independence of zeta
values. General proofs are in arithmetic_parameter_space_analysis.md.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def rank(matrix):
    return DomainMatrix.from_Matrix(matrix).rank()


def coefficient_rows(s: int, n: int):
    columns = [(k, j) for k in range(1, s + 1) for j in range(n + 1)]
    convergence = sp.Matrix([[int(k == 1) for k, j in columns]])
    zeta = sp.Matrix([[int(k == ell) for k, j in columns]
                      for ell in range(2, s + 1)])
    constant = sp.Matrix([[-sp.harmonic(j, k) for k, j in columns]])
    return columns, convergence, constant.col_join(zeta)


def check_telescoping(s: int, n: int):
    columns, convergence, output = coefficient_rows(s, n)
    scols = [(k, j) for k in range(1, s + 1) for j in range(n)]
    difference = sp.zeros(len(columns), len(scols))
    index = {pair: i for i, pair in enumerate(columns)}
    for col, (k, j) in enumerate(scols):
        difference[index[k, j], col] = 1
        difference[index[k, j + 1], col] = -1
    at_one = sp.Matrix([[sp.Rational(1, (j + 1) ** k) for k, j in scols]])
    assert convergence * difference == sp.zeros(1, len(scols))
    expected = at_one.col_join(sp.zeros(s - 1, len(scols)))
    assert output * difference == expected
    assert rank(difference) == s * n
    all_rows = convergence.col_join(output)
    formal_kernel_dim = len(columns) - rank(all_rows)
    assert formal_kernel_dim == s * n - 1
    # Difference restricted by S(1)=0 is precisely the formal-output kernel:
    # containment is checked above, and dimensions agree.
    return {"s": s, "n": n, "convergent_dimension": len(columns) - 1,
            "formal_output_rank": rank(all_rows) - 1,
            "formal_zero_kernel_dimension": formal_kernel_dim}


def constrained_rank(s: int, n: int, decay_order: int):
    columns, convergence, output = coefficient_rows(s, n)
    rows = []
    for m in range(1, decay_order + 1):
        rows.append([(-1) ** (m - k) * sp.binomial(m - 1, k - 1)
                     * j ** (m - k) if k <= m else 0 for k, j in columns])
    for even in range(2, s + 1, 2):
        rows.append([int(k == even) for k, j in columns])
    constraints = sp.Matrix(rows)
    constraint_rank = rank(constraints)
    target = output[[0] + [k - 1 for k in range(3, s + 1, 2)], :]
    image_rank = rank(constraints.col_join(target)) - constraint_rank
    kernel_dimension = len(columns) - constraint_rank - image_rank
    assert kernel_dimension == max(s * n - decay_order, 0)
    if decay_order <= s * n:
        assert image_rank == (s + 1) // 2
    # For s=7, eliminate zeta(3), zeta(5), but retain constant and zeta(7).
    if s == 7:
        nuisance = constraints.col_join(target[[1, 2], :])
        zeta7_survives = rank(nuisance.col_join(target[3, :])) > rank(nuisance)
    else:
        zeta7_survives = None
    return {"s": s, "n": n, "decay_order": decay_order,
            "domain_dimension": len(columns) - constraint_rank,
            "formal_odd_output_rank": image_rank,
            "formal_zero_kernel_dimension": kernel_dimension,
            "zeta7_coefficient_survives_elimination": zeta7_survives}


def check_normalization():
    # A saturated image can arise from a nonsaturated presentation.
    # The redundant parameters do not create extra output directions.
    B = sp.Matrix([[1, 0, 1], [0, 1, 1]])
    assert rank(B) == 2
    # Smith coordinates suffice: (Gamma intersect m Z^r)/m has diagonal
    # delta_i/gcd(delta_i,m). Check the membership equivalence exactly.
    cases = 0
    for delta in range(1, 25):
        for m in range(1, 17):
            step = delta // sp.gcd(delta, m)
            for x in range(-30, 31):
                assert ((m * x) % delta == 0) == (x % step == 0)
            cases += 1
    t = sp.symbols("t", positive=True)
    zero_sum = 1 / t - 3 / (t + 1) + 2 / (t + 2)
    assert sp.cancel(zero_sum) == (2 - t) / (t ** 3 + 3 * t ** 2 + 2 * t)
    assert -(-3 * sp.harmonic(1) + 2 * sp.harmonic(2)) == 0
    return {"smith_coordinate_membership_cases": cases,
            "integer_membership_checks": cases * 61,
            "nonzero_rational_function_with_zero_sum": str(sp.factor(zero_sum))}


def main():
    result = {
        "scope": "Exact finite checks; no irrationality conclusion or asymptotic estimate.",
        "telescoping": [check_telescoping(s, n)
                        for s in (3, 5, 7) for n in (1, 2, 4)],
        "decay_and_elimination": [constrained_rank(7, 4, m)
                                  for m in (1, 8, 16, 24, 28, 29, 30, 31, 32)],
        "normalization": check_normalization(),
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
