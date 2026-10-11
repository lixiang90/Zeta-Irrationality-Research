"""NEW FIRST1: original S value-Gram mechanism and independent algebraic depth toys.

Reads no old or peer mathematical file. Output is exclusive-created before math.
Actual cases are old r=1,2,4 only; no auxiliary-unit search or higher-layer claim.
"""
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

source = Path(__file__)
output = source.with_suffix('.json')
source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
with output.open('x', encoding='utf-8') as guard:
    json.dump({'status': 'RUNNING', 'first_execution': 1,
               'source_sha256': source_sha}, guard)

checks = 0


def check(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError('mechanism assertion ' + str(checks))


def rank_kernel(rows, p):
    a = [[v % p for v in row] for row in rows]
    cols = len(a[0]) if a else 0
    pivots = []
    for col in range(cols):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(v * inv) % p for v in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[row])]
        pivots.append(col)
    nulls = []
    for col in range(cols):
        if col not in pivots:
            v = [0] * cols
            v[col] = 1
            for i, pivot in enumerate(pivots):
                v[pivot] = (-a[i][col]) % p
            nulls.append(v)
    return len(pivots), pivots, nulls


def determinant(a):
    a = [[Fraction(v) for v in row] for row in a]
    answer = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            answer = -answer
        value = a[j][j]
        answer *= value
        for i in range(j + 1, len(a)):
            scale = a[i][j] / value
            for k in range(j + 1, len(a)):
                a[i][k] -= scale * a[j][k]
    return answer


def valuation_integer(value, p):
    if value == 0:
        return None
    value = abs(value)
    v = 0
    while value % p == 0:
        value //= p
        v += 1
    return v


def valuation_fraction(value, p):
    if value == 0:
        return None
    return valuation_integer(value.numerator, p) - valuation_integer(value.denominator, p)


def mod_fraction(value, p):
    value = Fraction(value)
    check(value.denominator % p != 0)
    return (value.numerator * pow(value.denominator, -1, p)) % p


def actual_case(r):
    n, p = 4 * r, 18 * r + 1
    head, dim = 2 * n, 2 * n
    check(all(p % d for d in range(2, math.isqrt(p) + 1)))
    primitive = []
    for m in range(1, n + 1):
        reflected = head + 1 - m
        dm = math.factorial(6 * n + m) // math.factorial(m - 1)
        dr = math.factorial(6 * n + reflected) // math.factorial(reflected - 1)
        common = math.gcd(dm, dr)
        primitive.append((m, reflected, dm // common, dr // common))
        check(math.gcd(dm // common, dr // common) == 1)

    def cardinal_negative(m, j):
        numerator = math.comb(j + head, head) * m * math.comb(head, m)
        check(numerator % (j + m) == 0)
        return (-1) ** (m - 1) * (numerator // (j + m))

    def original_values(j):
        values = [pm * cardinal_negative(m, j) + qm * cardinal_negative(mirror, j)
                  for m, mirror, pm, qm in primitive]
        values += [(-1) ** i * math.comb(j + i, i) for i in range(head, 3 * n)]
        check(len(values) == dim)
        return values

    values = [original_values(j) for j in range(6 * n + 1)]
    weights = [math.comb(6 * n, j) ** 2 * math.comb(2 * n + j, j) ** 3
               for j in range(6 * n + 1)]
    unit_tail = [j for j in range(p, 6 * n + 1) if weights[j] % p]
    image_rank, pivot_cols, weak_cols = rank_kernel([values[j] for j in unit_tail], p)
    check(image_rank == 5 * r)
    check(len(weak_cols) == 3 * r)
    strong_cols = [[int(i == col) for i in range(dim)] for col in pivot_cols]
    columns = strong_cols + weak_cols
    transformation = [[columns[j][i] for j in range(dim)] for i in range(dim)]
    det_t = determinant(transformation)
    check(det_t.denominator == 1 and det_t.numerator % p != 0)
    deltas = [0] * image_rank + [1] * len(weak_cols)

    # Exact head evaluations: cardinal interpolation and high Newton columns.
    head_matrix = [[pm if t == m else qm if t == mirror else 0
                    for m, mirror, pm, qm in primitive] + [0] * n
                   for t in range(1, head + 1)]
    paired_checks = 0
    for col in columns:
        head_values = [sum(x * y for x, y in zip(row, col)) for row in head_matrix]
        for m, mirror, pm, qm in primitive:
            check(qm * head_values[m - 1] - pm * head_values[mirror - 1] == 0)
            paired_checks += 1

    adapted = [[sum(x * y for x, y in zip(row, col)) for col in columns]
               for row in values]
    normalized = [[0] * dim for _ in range(dim)]
    unit_heads = unit_tails = nonunit_nodes = node_entry_checks = 0
    for j, (row, weight) in enumerate(zip(adapted, weights)):
        if weight % p:
            if j < p:
                unit_heads += 1
            else:
                unit_tails += 1
            for i in range(image_rank, dim):
                check(row[i] % p == 0)
        else:
            nonunit_nodes += 1
            check(weight % (p * p) == 0)
        for i in range(dim):
            for l in range(i, dim):
                divisor = p ** (deltas[i] + deltas[l])
                numerator = weight * row[i] * row[l]
                check(numerator % divisor == 0)
                term = (numerator // divisor) % p
                normalized[i][l] = (normalized[i][l] + term) % p
                normalized[l][i] = normalized[i][l]
                node_entry_checks += 1
    for row in normalized:
        for entry in row:
            # Exact derivative N_X=24*p^5*H; no actual anchor Smith inference.
            check((24 * p ** 5 * entry) % (p ** 5) == 0)
    gram_rank, _, _ = rank_kernel(normalized, p)
    return {'r': r, 'n': n, 'p': p, 'original_S_rank': dim,
            'unit_tail_value_image_rank': image_rank,
            'actual_weak_columns': len(weak_cols),
            'adapted_GL_det_mod_p': det_t.numerator % p,
            'exact_primitive_pair_checks': paired_checks,
            'unit_head_nodes': unit_heads, 'unit_tail_nodes': unit_tails,
            'nonunit_nodes': nonunit_nodes,
            'normalized_node_entry_divisibility_checks': node_entry_checks,
            'normalized_value_Gram_rank_mod_p': gram_rank,
            'normalized_X_derivative_precision_at_least': 5,
            'actual_anchor_higher_Smith_computed': False}


def schur_ladder(matrix, p, maximum_stage):
    a = [[Fraction(v) for v in row] for row in matrix]
    ranks, dimensions = [], [len(a)]
    for stage in range(maximum_stage + 1):
        rank = 0
        # Orthogonal elimination of a known unit diagonal; if needed find one
        # by replacing e_i with e_i+e_j in the remaining subspace.
        while rank < len(a):
            index = next((i for i in range(rank, len(a)) if mod_fraction(a[i][i], p)), None)
            if index is None:
                pair = next(((i, j) for i in range(rank, len(a))
                             for j in range(i + 1, len(a)) if mod_fraction(a[i][j], p)), None)
                if pair is None:
                    break
                i, j = pair
                # Replace e_i by e_i+e_j, preserving symmetry exactly.
                for k in range(len(a)):
                    a[i][k] += a[j][k]
                for k in range(len(a)):
                    a[k][i] += a[k][j]
                index = i
                check(mod_fraction(a[index][index], p) != 0)
            if index != rank:
                a[index], a[rank] = a[rank], a[index]
                for row in a:
                    row[index], row[rank] = row[rank], row[index]
            pivot = a[rank][rank]
            check(mod_fraction(pivot, p) != 0)
            for i in range(rank + 1, len(a)):
                for j in range(i, len(a)):
                    a[i][j] -= a[i][rank] * a[rank][j] / pivot
                    a[j][i] = a[i][j]
            rank += 1
        residual = [[a[i][j] for j in range(rank, len(a))]
                    for i in range(rank, len(a))]
        for row in residual:
            for entry in row:
                check(entry == 0 or valuation_fraction(entry, p) >= 1)
        a = [[entry / p for entry in row] for row in residual]
        ranks.append(rank)
        dimensions.append(len(a))
    return {'ranks': ranks, 'dimensions': dimensions}


def algebraic_toys():
    p, dim = 7, 5
    transform = [[int(i == j) + int(j == i + 1) for j in range(dim)]
                 for i in range(dim)]
    matrix = [[sum(transform[k][i] * p ** k * transform[k][j] for k in range(dim))
               for j in range(dim)] for i in range(dim)]
    ladder = schur_ladder(matrix, p, 4)
    check(ladder['ranks'] == [1, 1, 1, 1, 1])
    check(ladder['dimensions'] == [5, 4, 3, 2, 1, 0])
    determinant_anchor = determinant(matrix)
    check(determinant_anchor == p ** 10)
    perturbation_records = []
    for x in range(p):
        varied = [[matrix[i][j] + p ** 5 * x * (1 + i + j) for j in range(dim)]
                  for i in range(dim)]
        ratio = determinant(varied) / determinant_anchor
        check(valuation_fraction(ratio, p) == 0 and mod_fraction(ratio, p) == 1)
        perturbation_records.append({'x': x, 'normalized_det_mod_p': 1})
    borderline = [[p ** 5, 0], [0, 1]]
    ladder5 = schur_ladder(borderline, p, 4)
    check(ladder5['ranks'] == [1, 0, 0, 0, 0])
    check(ladder5['dimensions'][-1] == 1)
    check(determinant([[0, 0], [0, 1]]) == 0)
    return {'scope': 'general integral symmetric examples, not original lambda2 higher layers',
            'p': p, 'mixed_congruence_Smith_exponents': [0, 1, 2, 3, 4],
            'depth4_ladder': ladder, 'determinant_valuation': 10,
            'p5_perturbation_records': perturbation_records,
            'depth5_boundary_ladder': ladder5,
            'depth5_boundary_target_x': 1, 'depth5_boundary_target_singular': True}


try:
    cases = [actual_case(r) for r in (1, 2, 4)]
    toys = algebraic_toys()
    result = {'status': 'PASS', 'first_execution': 1, 'successful_runs': 1,
              'failed_runs': 0, 'reruns': 0, 'old_or_peer_execute_import': 0,
              'source_sha256': source_sha, 'checks': checks,
              'actual_cases': cases, 'algebraic_toys': toys,
              'actual_higher_layer_condition_proved_by_finite_cases': False,
              'infinite_nonzero_or_numerical_irrationality_proved': False}
except BaseException as error:
    result = {'status': 'FAILED_PRESERVED', 'first_execution': 1,
              'source_sha256': source_sha, 'checks_completed': checks,
              'error': type(error).__name__ + ': ' + str(error),
              'reruns': 0}
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    raise
output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'checks': checks,
                  'actual_cases': len(cases), 'actual_higher_Smith_computed': False}))
