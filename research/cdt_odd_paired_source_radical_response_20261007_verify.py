"""NEW first-only source-response check; never imports or runs old/peer producers.

Actual finite scope: r=1,2,4 only, literal harmonics/weights and mod-p^2
halfjet representatives. They are not asserted to be exact char0 paired lifts.
All-scale lift independence is proved in the accompanying paper.
No actual higher Smith or new auxiliary-unit sample is calculated.
"""
from pathlib import Path
from math import comb, factorial
import json
import hashlib

RESULT = Path(__file__).with_suffix('.json')
GUARD = Path(__file__).with_suffix('.guard.json')
with GUARD.open('x', encoding='utf-8') as f:
    json.dump({'state': 'STARTED_FIRST1', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'old_or_peer_execute_import': 0}, f)
assert not RESULT.exists()
checks = 0


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def add(a, b, mod):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    return [v % mod for v in c]


def scale(a, k, mod):
    return [v * k % mod for v in a]


def mul(a, b, mod):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % mod
    return c


def factors(offsets, mod):
    a = [1]
    for x in offsets:
        a = mul(a, [x, 1], mod)
    return a


def ev(a, x, mod):
    y = 0
    for v in reversed(a):
        y = (y * x + v) % mod
    return y


def derivative(a, mod):
    return [i * a[i] % mod for i in range(1, len(a))] or [0]


def nullspace(a, p):
    b = [[v % p for v in row] for row in a]
    pivots, row = [], 0
    n = len(b[0])
    for col in range(n):
        pivot = next((i for i in range(row, len(b)) if b[i][col]), None)
        if pivot is None:
            continue
        b[row], b[pivot] = b[pivot], b[row]
        v = pow(b[row][col], -1, p)
        b[row] = [x * v % p for x in b[row]]
        for i in range(len(b)):
            if i != row and b[i][col]:
                v = b[i][col]
                b[i] = [(x - v * y) % p for x, y in zip(b[i], b[row])]
        pivots.append(col)
        row += 1
        if row == len(b):
            break
    basis = []
    for col in range(n):
        if col not in pivots:
            v = [0] * n
            v[col] = 1
            for i, j in enumerate(pivots):
                v[j] = -b[i][col] % p
            basis.append(v)
    return basis


def gram(x, weights, p):
    n = len(x[0])
    return [[sum(w * row[i] * row[j] for row, w in zip(x, weights)) % p
             for j in range(n)] for i in range(n)]


def actual_case(r):
    m, n, p = 2 * r, 4 * r, 18 * r + 1
    mod, c = p ** 4, 4 * m + 1
    A = factors(range(3 * m), mod)
    Ap = derivative(A, mod)
    S = factors((-z for z in range(1, 4 * m + 1)), mod)
    center = [(-c * pow(2, -1, mod)) % mod, 1]
    centered_square = mul(center, center, mod)
    Q = [[1]]
    for _ in range(1, 3 * r):
        Q.append(mul(Q[-1], centered_square, mod))
    L = [[ev(Q[i], -l, p) * pow(ev(Ap, -l, p) * ev(S, -l, p) % p, -1, p) % p
          for l in range(3 * m)] for i in range(r)]
    zb = nullspace(L, p)
    check(len(zb) == 5 * r, 'literal image dimension')
    Z = [[v[l] for v in zb] for l in range(3 * m)]
    strong = []
    cardinal = [scale(factors((k for k in range(3 * m) if k != l), mod),
                      pow(ev(Ap, -l, mod), -1, mod), mod) for l in range(3 * m)]
    for v in zb:
        poly = [0]
        for l, value in enumerate(v):
            poly = add(poly, scale(cardinal[l], value, mod), mod)
        strong.append(poly)
    shared = [l for l in range(3 * m) if ev(A, c + l, p) == 0]
    check(len(shared) == m - 1, 'true shared mask')
    I = factors(shared, mod)
    Adiv = factors((l for l in range(3 * m) if l not in shared), mod)
    halfcorrection = scale(mul(Adiv, derivative(I, mod), mod), p * pow(2, -1, mod), mod)
    weak = [add(mul(A, q, mod), mul(halfcorrection, q, mod), mod) for q in Q]
    polys, delta = strong + weak, [0] * (5 * r) + [1] * (3 * r)
    d = len(polys)
    check(d == 8 * r and max(len(v) - 1 for v in polys) < 6 * m, 'original degree cutoff')
    J = [[ev(Ap, -l, p) * ev(q, -l, p) % p for q in Q] for l in range(3 * m)]
    eta = [pow(2, -1, p) if l in shared else 0 for l in range(3 * m)]
    W = [pow(comb(12 * m, j), 2, mod) * pow(comb(4 * m + j, j), 3, mod) % mod
         for j in range(12 * m + 1)]
    D = [W[p + l] % p for l in range(3 * m)]
    for l in range(3 * m):
        check(D[l] != 0, 'unit tail weight')
        for i, q in enumerate(weak):
            value = ev(q, -p - l, mod)
            check(value % p == 0, 'actual weak tail value')
            check((value // p - (eta[l] - 1) * J[l][i]) % p == 0, 'translated halfjet')
            check((ev(derivative(q, mod), -p - l, p) - J[l][i]) % p == 0, 'weak derivative')
    hs = {}
    for exponent in range(1, 6):
        h = [0]
        for k in range(1, 16 * m + 1):
            term = 1 if k == p else pow(p, exponent, mod) * pow(pow(k, -1, mod), exponent, mod) % mod
            h.append((h[-1] + term) % mod)
        hs[exponent] = h
    raw_a = [[0] * d for _ in range(d)]
    raw_b = [[0] * d for _ in range(d)]
    for j, weight in enumerate(W):
        cs = (5 * hs[1][j] - 3 * hs[1][4 * m + j] - 2 * hs[1][12 * m - j]) % mod
        ua = -8 * p ** 2 * hs[3][j] % mod
        va = p * (-8 * cs * hs[3][j] - 24 * hs[4][j]) % mod
        ub = -6 * p * hs[4][j] % mod
        vb = (-6 * cs * hs[4][j] - 24 * hs[5][j]) % mod
        values = [ev(v, -j, mod) for v in polys]
        derivs = [ev(derivative(v, mod), -j, mod) for v in polys]
        for i in range(d):
            for k in range(i, d):
                pv, pd = values[i] * values[k], values[i] * derivs[k] + derivs[i] * values[k]
                raw_a[i][k] = (raw_a[i][k] + weight * (ua * pd + va * pv)) % mod
                raw_b[i][k] = (raw_b[i][k] + weight * (ub * pd + vb * pv)) % mod
    def model(s):
        matrix = [[0] * d for _ in range(d)]
        for i in range(d):
            for k in range(i, d):
                total = 0
                for l, weight in enumerate(D):
                    if k < 5 * r:
                        term = -(s + 1) * Z[l][i] * Z[l][k]
                    elif i < 5 * r:
                        term = Z[l][i] * (s - (s + 1) * eta[l]) * J[l][k - 5 * r]
                    else:
                        ds = 1 - eta[l] ** 2 - s * (1 - eta[l]) ** 2
                        term = J[l][i - 5 * r] * ds * J[l][k - 5 * r]
                    total += weight * term
                matrix[i][k] = matrix[k][i] = total % p
        return matrix
    a4, a5 = model(4), model(5)
    E = [Z[l] + [-(1 - eta[l]) * v % p for v in J[l]] for l in range(3 * m)]
    mass = gram(E, D, p)
    for i in range(d):
        for k in range(i, d):
            div_a = p ** (delta[i] + delta[k] + 1)
            div_b = p ** (delta[i] + delta[k])
            check(raw_a[i][k] % div_a == 0, 'whole source a normalization')
            check(raw_b[i][k] % div_b == 0, 'whole source b normalization')
            check((raw_a[i][k] // div_a - 8 * a4[i][k]) % p == 0, 'actual source a response')
            check((raw_b[i][k] // div_b - 6 * a5[i][k]) % p == 0, 'actual source b leading')
            check((a4[i][k] - a5[i][k] - mass[i][k]) % p == 0, 'affine pencil mass identity')
    return {'r': r, 'n': n, 'p': p, 'dimension': d, 'shared_nodes': shared,
            'strong_dimension': 5 * r, 'weak_dimension': 3 * r,
            'source_a_normalized_response_matches': True,
            'source_b_leading_matches': True, 'pencil_mass_identity': True,
            'actual_anchor_higher_Smith_computed': False,
            'exact_char0_pairing_of_representatives_asserted': False,
            'scope': 'literal actual mod-p^2 halfjet jets suffice; paper proves independence of exact higher lift corrections'}


try:
    cases = [actual_case(r) for r in (1, 2, 4)]
    toy = []
    for p in (19, 37, 73):
        for k in (1, 2, 3):
            roots = [a for a in range(p) if any((8 * a + j + 1) % p == 0 for j in range(k))]
            check(len(roots) == k, 'toy affine residual root count')
            toy.append({'p': p, 'k': k, 'bad_source_residues': roots,
                        'scope': 'general diagonal residual toy, not actual original anchor'})
    out = {'status': 'PASS', 'first_only': True, 'successful_runs': 1, 'failed_runs': 0,
           'checks': checks, 'cases': cases, 'residual_toys': toy,
           'old_or_peer_execute_import_rerun': 0, 'external_Lean_execution': 0,
           'auxiliary_unit_prime_table_extended': False,
           'infinite_actual_radical_mass_unit_proved': False,
           'fixed_rational_source_infinite_success_proved': False,
           'actual_higher_Smith_or_new_M5_unit_asserted': False}
    with RESULT.open('x', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps({'status': 'PASS', 'checks': checks, 'cases': len(cases), 'toys': len(toy)}))
except Exception as error:
    if not RESULT.exists():
        with RESULT.open('x', encoding='utf-8') as f:
            json.dump({'status': 'FAILED_FIRST1', 'checks_before_failure': checks,
                       'error': repr(error), 'reruns': 0}, f, indent=2)
    raise
