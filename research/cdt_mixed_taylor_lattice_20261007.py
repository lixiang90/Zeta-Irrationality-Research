"""Exact primitive leading-coefficient ideals for finite mixed-period Taylor pools.

This is a NEW finite experiment.  It does not prove an asymptotic lattice saving,
irrationality, a common analytic map, or Hermite--Pade perfectness for all degrees.
No numerical period values or PSLQ are used.  The test parameters are a=b=1,u=0.
"""

from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import hashlib
import json

import sympy as sp
from flint import fmpz_mat


def coefficient_sequences(count, a=Fraction(1), b=Fraction(1), u=Fraction(0)):
    one = [Fraction(int(n == 0)) for n in range(count)]
    atan = [Fraction(0)] * count
    beta2 = [Fraction(0)] * count
    square = [Fraction(0)] * count
    for n in range(1, count):
        chi = 0 if n % 2 == 0 else (-1) ** ((n - 1) // 2)
        atan[n] = Fraction(chi, n)
        beta2[n] = Fraction(chi, n * n)
        square[n] = sum((atan[k] * atan[n - k] for k in range(1, n)), Fraction(0))
    mixed = [a * beta2[n] + 16 * b * square[n] for n in range(count)]
    lift = [Fraction(0)] * count
    for n in range(1, count):
        lift[n] = (sum(mixed[:n], Fraction(0)) - u) / n

    # Check the exact ODE and square identity in this entire finite prefix.
    for n in range(count - 1):
        lhs = (n + 1) * mixed[n + 1]
        rhs = a * atan[n + 1] + 32 * b * sum(
            ((-1) ** k * atan[n - 2 * k] for k in range(n // 2 + 1)), Fraction(0)
        )
        assert lhs == rhs
        assert (n + 1) * lift[n + 1] == sum(mixed[: n + 1], Fraction(0)) - u
    return {"1": one, "A": atan, "B": beta2, "S": square, "Psi": mixed, "F": lift}


def primitive_contact(record_names, degree_bound):
    m = len(record_names)
    columns = [(name, k) for name in record_names for k in range(degree_bound)]
    dimension = len(columns)
    sequence = coefficient_sequences(dimension + 12)

    def row(n):
        return [sequence[name][n - k] if n >= k else Fraction(0) for name, k in columns]

    rows = [row(n) for n in range(dimension + 10)]
    matrix = sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in values] for values in rows])
    _, independent_rows = matrix.T.rref()
    assert len(independent_rows) == dimension, (record_names, degree_bound)
    contact = independent_rows[-1]
    earlier = matrix[:contact, :]
    nullspace = earlier.nullspace()
    assert len(nullspace) == 1
    vector = nullspace[0]
    denominator = lcm(*(int(entry.q) for entry in vector))
    integers = [int(entry * denominator) for entry in vector]
    common = reduce(gcd, (abs(v) for v in integers))
    integers = [v // common for v in integers]
    if next(v for v in integers if v) < 0:
        integers = [-v for v in integers]
    assert reduce(gcd, (abs(v) for v in integers)) == 1
    assert earlier * sp.Matrix(integers) == sp.zeros(contact, 1)

    leading = sum((v * c for v, c in zip(integers, rows[contact])), Fraction(0))
    assert leading != 0
    naive = lcm(*(value.denominator for value in rows[contact]))
    assert naive % leading.denominator == 0

    # Primitivity + a one-dimensional rational kernel proves that all integral
    # contact vectors are Z multiples of this vector.  Consequently their first
    # coefficient ideal is EXACTLY leading*Z for this finite contact window.
    return {
        "functions": record_names,
        "polynomial_degrees_less_than": degree_bound,
        "column_count": dimension,
        "independent_row_indices": list(independent_rows),
        "contact_order": contact,
        "first_mD_rows_full_rank": contact == dimension - 1,
        "integral_contact_kernel_rank": 1,
        "primitive_vector": integers,
        "columns": [[name, k] for name, k in columns],
        "first_coefficient": {"numerator": leading.numerator, "denominator": leading.denominator},
        "leading_coefficient_ideal": "first_coefficient * Z; exact for this finite integer kernel",
        "sliding_window_naive_lcm": naive,
        "leading_denominator_saving_factor": naive // leading.denominator,
        "maximum_absolute_polynomial_coefficient": max(abs(v) for v in integers),
    }


def saturated_leading_ideal(record_names, degree_bound, contact):
    """Compute the exact leading ideal for a wider integer contact kernel.

    An explicit unimodular row transformation of the transposed cleared matrix
    gives a basis of its full integer image lattice.  An inverse rational matrix
    then finds the least vertical lattice point; its integral preimage is returned.
    This is a complete finite lattice computation, without a height theorem.
    """
    columns = [(name, k) for name in record_names for k in range(degree_bound)]
    sequence = coefficient_sequences(contact + 1)
    rows = [[sequence[name][n - k] if n >= k else Fraction(0)
             for name, k in columns] for n in range(contact + 1)]
    common = lcm(*(value.denominator for row in rows for value in row))
    cleared = fmpz_mat([[int(common * value) for value in row] for row in rows])
    h, transform = cleared.transpose().hnf(transform=True)
    assert h == transform * cleared.transpose()
    assert abs(int(transform.det())) == 1
    rank = contact + 1
    assert all(h[i, j] == 0 for i in range(rank, len(columns)) for j in range(rank))
    basis = sp.Matrix([[int(h[j, i]) for j in range(rank)] for i in range(rank)])
    assert basis.det() != 0
    unit = sp.zeros(rank, 1)
    unit[-1] = 1
    inverse_unit = basis.inv() * unit
    delta = lcm(*(int(entry.q) for entry in inverse_unit))
    coordinates = [int(delta * entry) for entry in inverse_unit] + [0] * (len(columns) - rank)
    generator = [sum(int(transform[j, i]) * coordinates[j] for j in range(len(columns)))
                 for i in range(len(columns))]
    expected = fmpz_mat([[0] if n < contact else [delta] for n in range(rank)])
    assert cleared * fmpz_mat([[v] for v in generator]) == expected
    coefficient = Fraction(delta, common)
    direct = [sum((q * value for q, value in zip(generator, row)), Fraction(0)) for row in rows]
    assert direct == [Fraction(0)] * contact + [coefficient]
    naive = lcm(*(value.denominator for value in rows[-1]))
    assert naive % coefficient.denominator == 0
    return {
        "functions": record_names,
        "polynomial_degrees_less_than": degree_bound,
        "column_count": len(columns),
        "contact_order": contact,
        "integer_contact_kernel_rank": len(columns) - contact,
        "clearing_denominator_entire_prefix": common,
        "least_positive_vertical_image_coordinate": delta,
        "leading_coefficient_ideal": {"numerator": coefficient.numerator,
                                      "denominator": coefficient.denominator},
        "sliding_window_naive_lcm": naive,
        "leading_denominator_saving_factor": naive // coefficient.denominator,
        "explicit_integer_generator": generator,
        "generator_maximum_absolute_coefficient": max(abs(v) for v in generator),
        "unimodular_transform_determinant": int(transform.det()),
        "verification": "H=U*A^t; det(U)=+-1; bottom zero rows; delta minimal by denominators of inverse basis times e_last; A*q=delta*e_last",
        "height_scope": "The returned preimage is an exact witness, not a minimum-height generator or an asymptotic bound.",
    }


def main():
    records = [
        primitive_contact(names, degree)
        for names in [["1", "A", "Psi", "F"], ["1", "A", "B", "S", "F"]]
        for degree in range(1, 7)
    ]
    wider = [
        saturated_leading_ideal(names, degree, multiplier * degree)
        for names, multipliers in [(["1", "A", "Psi", "F"], [2, 3]),
                                   (["1", "A", "B", "S", "F"], [2, 3, 4])]
        for degree in range(2, 7)
        for multiplier in multipliers
    ]
    source = Path(__file__).resolve()
    payload = {
        "parameters": {"a": "1", "b": "1", "u": "0"},
        "scope": "12 one-dimensional and 25 wider exact finite Taylor kernels only; no all-degree perfectness or asymptotic lattice/height theorem",
        "target_relation_assumed_for_arithmetic": False,
        "period_numeric_evaluation": False,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "proof_of_finite_ideal": "The rational kernel is one-dimensional. Its gcd-one integer vector generates its intersection with Z^q, so the image of the leading-coefficient functional is leading*Z.",
        "records": records,
        "saturated_wider_kernels": wider,
    }
    output = source.with_suffix(".json")
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for rec in records:
        print(
            len(rec["functions"]), rec["polynomial_degrees_less_than"],
            "contact", rec["contact_order"],
            "den", rec["first_coefficient"]["denominator"],
            "saving", rec["leading_denominator_saving_factor"],
        )
    for rec in wider:
        print("wider", len(rec["functions"]), rec["polynomial_degrees_less_than"],
              rec["contact_order"], "ideal", rec["leading_coefficient_ideal"],
              "saving", rec["leading_denominator_saving_factor"])
    print("PASS: 12 primitive and 25 wider exact finite leading-coefficient ideals")


if __name__ == "__main__":
    main()
