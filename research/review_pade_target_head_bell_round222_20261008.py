"""Independent finite exact audit through direct logarithmic derivatives.

One run; only n=0,2,4. Does not import or rerun the root producer.
"""
from fractions import Fraction
from math import comb, factorial, prod
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "pade_target_head_bell_review_round222_20261008.json"
assert not OUTPUT.exists(), "Do not overwrite the independent frozen output."


def principal_part(n, k):
    """F(v) = v^6 R_n(-k+v); use F^(h)(0), not factor convolution."""
    numerator_distances = [distance for j in range(1, n + 1)
                           for distance in (-k - j, n + j - k)]
    denominator_distances = [r - k for r in range(n + 1) if r != k]
    f0 = Fraction(prod(numerator_distances) ** 3,
                  prod(denominator_distances) ** 6)
    assert f0 > 0
    logarithmic_derivatives = {r: (-1) ** (r - 1) * factorial(r - 1) * (
        3 * sum((Fraction(1, d ** r) for d in numerator_distances), Fraction(0))
        - 6 * sum((Fraction(1, d ** r) for d in denominator_distances), Fraction(0)))
        for r in range(1, 6)}
    derivatives = [f0]
    for h in range(1, 6):
        derivatives.append(sum((comb(h - 1, r - 1)
                                * logarithmic_derivatives[r] * derivatives[h - r]
                                for r in range(1, h + 1)), Fraction(0)))
    return {6 - h: derivatives[h] / factorial(h) for h in range(6)}


def calculate_row(n):
    assert n in (0, 2, 4)
    parts = [principal_part(n, k) for k in range(n + 1)]
    for k in range(n + 1):
        for j in range(1, 7):
            assert parts[n - k][j] == (-1) ** j * parts[k][j]
    values = [Fraction(s - 1) * (1 - Fraction(1, 2 ** (s - 1)))
              * sum(((-1) ** k * parts[k][s - 1] for k in range(n + 1)), Fraction(0))
              for s in (3, 5, 7)]
    return values, parts


def determinant_by_elimination(rows):
    matrix = [list(row) for row in rows]
    determinant = Fraction(1)
    for column in range(3):
        pivot_row = next(row for row in range(column, 3) if matrix[row][column])
        if pivot_row != column:
            matrix[column], matrix[pivot_row] = matrix[pivot_row], matrix[column]
            determinant = -determinant
        pivot = matrix[column][column]
        determinant *= pivot
        for row in range(column + 1, 3):
            multiplier = matrix[row][column] / pivot
            for j in range(column + 1, 3):
                matrix[row][j] -= multiplier * matrix[column][j]
            matrix[row][column] = Fraction(0)
    return determinant


calculations = [calculate_row(n) for n in (0, 2, 4)]
rows = [values for values, parts in calculations]
delta = determinant_by_elimination(rows)
certificate = json.loads((BASE / "pade_target_head_certificate_round222_20261008.json")
                         .read_text(encoding="utf-8"))
for n, values, recorded in zip((0, 2, 4), rows, certificate["rows"]):
    assert recorded["n"] == n
    assert values == [Fraction(recorded[name]) for name in ("A3", "A5", "A7")]
assert delta == Fraction(certificate["Delta0"])
assert delta != 0
record = {
    "round": 222,
    "algorithm": "direct F(0), rational logarithmic derivatives, Bell recurrence, Fraction Gaussian determinant",
    "scope": "Only n=0,2,4 and Delta_0. One independent run; no infinite nonzero, recurrence, rank or numerical irrationality claim.",
    "rows": [{"n": n, **{name: str(value) for name, value in zip(("A3", "A5", "A7"), values)}}
             for n, values in zip((0, 2, 4), rows)],
    "principal_parts": [{"n": n, "poles": [{"k": k, "c_j": {str(j): str(part[j]) for j in range(1, 7)}}
                                               for k, part in enumerate(parts)]}
                        for n, (values, parts) in zip((0, 2, 4), calculations)],
    "Delta0": str(delta),
    "matches_root_certificate": True,
    "nonzero": True,
}
OUTPUT.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: value for key, value in record.items() if key != "principal_parts"},
                 ensure_ascii=False, indent=2))
