"""One fixed five-function Taylor minor; no prime samples or old imports."""
from fractions import Fraction as F
from pathlib import Path
import json

labels = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    labels.append(label)


def determinant(matrix):
    rows = [list(row) for row in matrix]
    value = F(1)
    for column in range(len(rows)):
        pivot = next(i for i in range(column, len(rows)) if rows[i][column])
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            value = -value
        entry = rows[column][column]
        value *= entry
        for i in range(column + 1, len(rows)):
            multiplier = rows[i][column] / entry
            rows[i] = [a - multiplier * b for a, b in zip(rows[i], rows[column])]
    return value


expected = [
    [F(0), F(0), F(0), F(1), F(1)],
    [F(0), F(1), F(1, 2), F(1, 8), F(1, 2)],
    [F(1, 6), F(3, 4), F(5, 12), F(1, 27), F(17, 54)],
    [F(1, 4), F(41, 72), F(49, 144), F(1, 64), F(2, 9)],
    [F(7, 24), F(65, 144), F(41, 144), F(1, 125), F(21, 125)],
]
matrix = []
k_coefficients = [F(0)]
for n in range(1, 6):
    t3 = sum((F(1, 6 * a * b * (n - a - b))
              for a in range(1, n)
              for b in range(1, n - a)), F(0))
    product = sum((F(1, a * (n - a) ** 2)
                   for a in range(1, n)), F(0))
    multiple = sum((F(1, j * j) for j in range(1, n)), F(0)) / n
    k_coefficients.append(F(2 * n - 1, 2 * n) * k_coefficients[-1] + F(1, n * n))
    matrix.append([t3, product, multiple, F(1, n ** 3), k_coefficients[-1] / n])
    check(f"Definitions give exact row n={n}", matrix[-1] == expected[n - 1])

check("K coefficients from t(1-t)K'=tK/2+L", k_coefficients[1:] == [F(1), F(1), F(17, 18), F(8, 9), F(21, 25)])
minor = determinant(matrix)
check("Fixed five-column minor", minor == -F(1, 3110400))
check("Only 2,3,5 occur in the minor denominator", 3110400 == 2 ** 9 * 3 ** 5 * 5 ** 2)

payload = {
    "scope": "A single exact n=1..5 Taylor minor for T3,L*Li2,Li(1,2),Li3,I_K. No prime scan; does not prove direct sum with Xi, S2 success, or height gain.",
    "checks_passed": len(labels),
    "check_labels": labels,
    "matrix": [[str(value) for value in row] for row in matrix],
    "determinant": str(minor),
    "denominator_prime_factors": {"2": 9, "3": 5, "5": 2},
    "conditional_all_prime_consequence": "For p>=7 and a slow prefix including coefficients 1..5, this five-column minor is a unit.",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"checks_passed": len(labels), "certificate": str(destination)}, ensure_ascii=False))
