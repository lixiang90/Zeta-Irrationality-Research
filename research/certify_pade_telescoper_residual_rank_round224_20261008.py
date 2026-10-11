"""One bounded exact specialization of the paper-derived remainder matrix.

Input: n=6 and centered even shifts j=0,...,6 only.  No sequence values,
recurrence guessing, parameter scanning, external CAS, or old producers.
Arithmetic: fractions.Fraction throughout.  The paper proof supplies the
global rational-function reduction and degree bound; this run supplies a
finite nonzero-minor witness if the specialized matrix has full row rank.
"""

from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json


N = 6
MAX_SHIFT = 6
POLE_ORDER = 9
SERIES_SIZE = 9
DESTINATION = Path(__file__).with_name(
    "pade_telescoper_residual_rank_certificate_round224_20261008.json"
)


def integer_binomial(exponent, index):
    if exponent >= 0:
        return comb(exponent, index) if index <= exponent else 0
    return (-1) ** index * comb(-exponent + index - 1, index)


def times_truncated(left, right):
    result = [Q(0)] * SERIES_SIZE
    for i, a in enumerate(left):
        for j, b in enumerate(right[: SERIES_SIZE - i]):
            result[i + j] += a * b
    return result


def factor_series(distance, slope, exponent):
    distance = Q(distance)
    assert distance != 0
    return [
        Q(integer_binomial(exponent, h))
        * distance ** (exponent - h)
        * slope**h
        for h in range(SERIES_SIZE)
    ]


def product_series(factors, scalar=1):
    result = [Q(scalar)] + [Q(0)] * (SERIES_SIZE - 1)
    for distance, slope, exponent in factors:
        result = times_truncated(
            result, factor_series(distance, slope, exponent)
        )
    return result


def pole_normalized_p_over_b(n, shift, pole_index):
    """Coefficients h^0..h^8 of h^9 P_j(n+i+h)/B(n+i+h-1)."""
    i = pole_index
    factors = []
    for r in range(3 * shift):
        factors += [(2 * n + i + 1 + r, 1, 3), (n - i + 1 + r, -1, 3)]
    for r in range(shift):
        factors.append((n + i + 1 + r, 1, -9))
        if r != i - 1:
            factors.append((1 - i + r, -1, -9))
    factors += [(n + i, 1, -9), (n - i + 1, -1, -3)]
    # The omitted factor is (-h)^(-9), so the scalar is (-1)^(j+1).
    return product_series(factors, (-1) ** (shift + 1))


def a_over_b_series(n, pole_index):
    """A(n+i+h)/B(n+i+h-1), regular at h=0 for n>=i."""
    i = pole_index
    return product_series(
        [(2 * n + i + 1, 1, 3), (-i, -1, 9),
         (n + i, 1, -9), (n - i + 1, -1, -3)],
        -1,
    )


def positive_certificate(n, shift):
    """Y_+(z)=sum c[i,l]/(z-n-i)^l, eliminating poles high to low."""
    answer = {}
    next_coefficients = {l: Q(0) for l in range(1, 10)}
    for i in range(shift, 0, -1):
        normalized = pole_normalized_p_over_b(n, shift, i)
        ratio = a_over_b_series(n, i)
        current = {}
        for l in range(1, 10):
            current[l] = -normalized[9 - l] + sum(
                (next_coefficients[h] * ratio[h - l] for h in range(l, 10)),
                Q(0),
            )
        answer[i] = current
        next_coefficients = current
    return answer


def positive_value(n, coefficients, z):
    return sum(
        (c / (z - n - i) ** l
         for i, row in coefficients.items() for l, c in row.items()),
        Q(0),
    )


def full_y_value(n, coefficients, z):
    return positive_value(n, coefficients, z) + positive_value(
        n, coefficients, n - z + 1
    )


def p_value(n, shift, z):
    result = Q((-1) ** shift)
    for r in range(3 * shift):
        result *= ((n + z + 1 + r) * (2 * n - z + 1 + r)) ** 3
    for r in range(shift):
        result /= ((z + 1 + r) * (n - z + 1 + r)) ** 9
    return result


def remainder_value(n, shift, coefficients, z):
    a = -(n + z + 1) ** 3 * (n - z) ** 9
    bminus = z**9 * (2 * n - z + 1) ** 3
    return (
        p_value(n, shift, z)
        - a * full_y_value(n, coefficients, z + 1)
        + bminus * full_y_value(n, coefficients, z)
    )


def polynomial_times_linear(coefficients, root):
    answer = [Q(0)] * (len(coefficients) + 1)
    for j, c in enumerate(coefficients):
        answer[j] -= root * c
        answer[j + 1] += c
    return answer


def interpolate_degree_five(nodes, values):
    answer = [Q(0)] * 6
    for i, x in enumerate(nodes):
        numerator, denominator = [Q(1)], Q(1)
        for j, y in enumerate(nodes):
            if i != j:
                numerator = polynomial_times_linear(numerator, y)
                denominator *= x - y
        for j, c in enumerate(numerator):
            answer[j] += values[i] * c / denominator
    return answer


def polynomial_value(coefficients, x):
    answer = Q(0)
    for c in reversed(coefficients):
        answer = answer * x + c
    return answer


def determinant(matrix):
    work = [row[:] for row in matrix]
    answer = Q(1)
    for column in range(len(work)):
        pivot = next((r for r in range(column, len(work))
                      if work[r][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            answer = -answer
        p = work[column][column]
        answer *= p
        for r in range(column + 1, len(work)):
            multiplier = work[r][column] / p
            for c in range(column + 1, len(work)):
                work[r][c] -= multiplier * work[column][c]
            work[r][column] = Q(0)
    return answer


def rank(matrix):
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((r for r in range(pivot_row, len(work))
                      if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot], work[pivot_row] = work[pivot_row], work[pivot]
        p = work[pivot_row][column]
        for r in range(pivot_row + 1, len(work)):
            multiplier = work[r][column] / p
            for c in range(column, len(work[0])):
                work[r][c] -= multiplier * work[pivot_row][c]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def fraction_text(value):
    return str(value.numerator) + "/" + str(value.denominator)


def main():
    nodes_w = [Q(j, 13) for j in range(6)]
    nodes = [w * w for w in nodes_w]
    columns = []
    all_poles = []
    extra_checks = []
    for shift in range(MAX_SHIFT + 1):
        certificate = positive_certificate(N, shift)
        values = []
        for w in nodes_w:
            right = remainder_value(N, shift, certificate, Q(N, 2) + w)
            left = remainder_value(N, shift, certificate, Q(N, 2) - w)
            assert right == left, ("reflection", shift, w)
            values.append(right)
        column = interpolate_degree_five(nodes, values)
        extra_w = Q(7, 13)
        exact_extra = remainder_value(N, shift, certificate, Q(N, 2) + extra_w)
        interpolated_extra = polynomial_value(column, extra_w**2)
        assert exact_extra == interpolated_extra, ("extra point", shift)
        columns.append(column)
        all_poles.append({
            str(i): {str(l): fraction_text(c) for l, c in row.items()}
            for i, row in certificate.items()
        })
        extra_checks.append({"shift": shift, "extra_w": "7/13", "equal": True})

    matrix = [[columns[j][i] for j in range(7)] for i in range(6)]
    minors = [
        (-1) ** omitted * determinant([
            [row[j] for j in range(7) if j != omitted] for row in matrix
        ])
        for omitted in range(7)
    ]
    kernel_checks = [sum((row[j] * minors[j] for j in range(7)), Q(0))
                     for row in matrix]
    assert all(value == 0 for value in kernel_checks)
    matrix_rank = rank(matrix)
    full_rank = matrix_rank == 6
    payload = {
        "scope": {
            "n": N, "centered_shifts": list(range(7)), "pole_order": 9,
            "arithmetic": "fractions.Fraction; no numerical approximation",
            "mathematical_runs_for_this_task": 1,
            "sequence_values_or_recurrence_guessing": False,
            "global_degree_and_identity_proof": "paper-derived, not inferred from samples",
        },
        "positive_pole_certificates": all_poles,
        "remainder_basis": ["1", "w^2", "w^4", "w^6", "w^8", "w^10"],
        "remainder_matrix": [[fraction_text(c) for c in row] for row in matrix],
        "signed_maximal_minors": [fraction_text(c) for c in minors],
        "minor_numerator_bit_lengths": [abs(c.numerator).bit_length() for c in minors],
        "minor_denominator_bit_lengths": [c.denominator.bit_length() for c in minors],
        "rank": matrix_rank, "full_row_rank": full_rank,
        "all_seven_signed_minors_nonzero": all(c != 0 for c in minors),
        "cofactor_kernel_checks": [fraction_text(c) for c in kernel_checks],
        "reflection_checks": "all six reconstruction nodes, all seven columns, exact",
        "extra_point_checks": extra_checks,
        "claim": (
            "Finite nonzero-minor witness for the paper's rational remainder matrix. "
            "No claim of minimal sequence order, infinite nonvanishing, or a CDT gate."
        ),
    }
    DESTINATION.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(DESTINATION), "rank": matrix_rank,
        "all_minors_nonzero": payload["all_seven_signed_minors_nonzero"],
        "first_minor_bits": payload["minor_numerator_bit_lengths"][0],
        "last_minor_bits": payload["minor_numerator_bit_lengths"][-1],
        "exact_checks_passed": True, "mathematical_runs": 1,
    }))


if __name__ == "__main__":
    main()
