"""NEW, first-execution-only exact auxiliary-prime probe.

Scope: finitely many local restrictions at s=5, n=2m, p=9m+1.
No old or peer producer is executed/imported. This file imports stdlib only.
It is not a proof for all m, all primes, or an irrationality assertion.
"""
import json
import math
from pathlib import Path

OUT = Path(__file__).with_suffix(".json")
if OUT.exists():
    raise RuntimeError("First-execution-only probe: output already exists; do not rerun.")


def rank_fp(rows, p):
    if not rows:
        return 0
    a = [[int(x) % p for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        hit = next((i for i in range(r, len(a)) if a[i][c]), None)
        if hit is None:
            continue
        a[r], a[hit] = a[hit], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                fac = a[i][c]
                a[i] = [(x - fac * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def local_kernel(rows, p, modulus):
    a = [[int(x) % modulus for x in row] for row in rows]
    pivots = []
    r = 0
    width = len(a[0])
    for c in range(width):
        hit = next((i for i in range(r, len(a)) if a[i][c] % p), None)
        if hit is None:
            continue
        a[r], a[hit] = a[hit], a[r]
        inv = pow(a[r][c], -1, modulus)
        a[r] = [(x * inv) % modulus for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                fac = a[i][c]
                a[i] = [(x - fac * y) % modulus for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    if r != len(rows):
        raise ArithmeticError("Constraint reduction did not have full row rank.")
    free = [j for j in range(width) if j not in pivots]
    cols = []
    for f in free:
        col = [0] * width
        col[f] = 1
        for i, c in enumerate(pivots):
            col[c] = (-a[i][f]) % modulus
        cols.append(col)
    for row in rows:
        for col in cols:
            if sum(x * y for x, y in zip(row, col)) % modulus:
                raise ArithmeticError("Local kernel identity failed.")
    return cols


def valuation(x, p, ceiling):
    if x == 0:
        return ceiling
    v = 0
    while x % p == 0 and v < ceiling:
        v += 1
        x //= p
    return v


def smith_mod(rows, p, precision):
    a = [row[:] for row in rows]
    out = []
    offset = 0
    while a:
        e, ii, jj = min(
            (valuation(x, p, precision), i, j)
            for i, row in enumerate(a) for j, x in enumerate(row)
        )
        if e == precision:
            out.extend([">=" + str(offset + precision)] * len(a))
            break
        a[0], a[ii] = a[ii], a[0]
        for row in a:
            row[0], row[jj] = row[jj], row[0]
        if e:
            fac = p ** e
            a = [[x // fac for x in row] for row in a]
            precision -= e
            offset += e
        modulus = p ** precision
        inv = pow(a[0][0], -1, modulus)
        out.append(offset)
        a = [
            [(a[i][j] - a[i][0] * inv * a[0][j]) % modulus
             for j in range(1, len(a))]
            for i in range(1, len(a))
        ]
    return out


def restriction_case(m, source_r):
    p = 9 * m + 1
    precision = 8
    modulus = p ** precision
    h, n, N = 6 * m, 2 * m, 12 * m
    dvals = {}
    for z in range(1, 4 * m + 1):
        prod = 1
        pcount = 0
        for j in range(z, z + N + 1):
            if j == p:
                pcount += 1
            else:
                prod = (prod * j) % modulus
        if pcount != 1:
            raise ArithmeticError("Actual d_z did not contain exactly one p.")
        dvals[z] = prod
    constraints = []
    for z in range(1, 2 * m + 1):
        zp = 4 * m + 1 - z
        constraints.append([
            (dvals[zp] * pow(z, i, modulus) -
             dvals[z] * pow(zp, i, modulus)) % modulus
            for i in range(h)
        ])
    basis_cols = local_kernel(constraints, p, modulus)
    dim = len(basis_cols)
    neg_eval = [[sum(col[i] * pow(-ell, i, p) for i in range(h)) % p
                 for col in basis_cols] for ell in range(3 * m)]
    eval_rank = rank_fp(neg_eval, p)
    if eval_rank != 5 * m // 2:
        raise ArithmeticError("Negative evaluation rank disagreed with paper identity.")
    harmonic = {}
    for v in (1, 3, 4, 5):
        vals = [0]
        total = 0
        for j in range(1, 16 * m + 1):
            term = 1 if j == p else (p ** v * pow(pow(j, -1, modulus), v, modulus)) % modulus
            total = (total + term) % modulus
            vals.append(total)
        harmonic[v] = vals
    moments = [0] * (2 * h - 1)
    for j in range(N + 1):
        w = (math.comb(N, j) ** 2 * math.comb(4 * m + j, j) ** 3) % modulus
        ct = (5 * harmonic[1][j] - 3 * harmonic[1][4 * m + j]
              - 2 * harmonic[1][N - j]) % modulus
        ut = (8 * source_r * p * harmonic[3][j] - 6 * harmonic[4][j]) % modulus
        vt = (ct * ut + 24 * (source_r * p * harmonic[4][j] - harmonic[5][j])) % modulus
        powers = [1]
        for _ in range(2 * h - 2):
            powers.append((powers[-1] * (-j)) % modulus)
        for e in range(2 * h - 1):
            derivative = 0 if e == 0 else e * powers[e - 1]
            moments[e] = (moments[e] + w * (p * ut * derivative + vt * powers[e])) % modulus
    ambient = [[moments[i + j] for j in range(h)] for i in range(h)]
    temp = [[sum(ambient[i][j] * col[j] for j in range(h)) % modulus
             for col in basis_cols] for i in range(h)]
    gram = [[sum(col[i] * temp[i][b] for i in range(h)) % modulus
             for b in range(dim)] for col in basis_cols]
    smith = smith_mod(gram, p, precision)
    tdim = m // 2
    small = [[0] * tdim for _ in range(tdim)]
    center = (4 * m + 1) * pow(2, -1, p) % p
    for ell in range(3 * m):
        t = (-ell) % p
        spos = 1
        for z in range(1, 4 * m + 1):
            spos = spos * (t - z) % p
        wt = pow(pow(spos, -1, p), 5, p)
        yy = (t - center) ** 2 % p
        for a in range(tdim):
            for b in range(tdim):
                small[a][b] = (small[a][b] + wt * pow(yy, a + b, p)) % p
    return {
        "m": m, "n": n, "p": p, "s": 5, "r": source_r, "X": 0,
        "precision": precision, "paired_dimension": dim,
        "constraint_rank": len(constraints), "negative_eval_rank": eval_rank,
        "leading_restricted_gram_rank": rank_fp(gram, p),
        "orthogonal_complement_small_gram_rank": rank_fp(small, p),
        "orthogonal_complement_small_dimension": tdim,
        "smith_exponents_of_p5_restricted_gram": smith,
        "all_smith_exponents_detected_below_precision": all(isinstance(x, int) for x in smith),
        "X_term_enters_at_p_power": 5
    }


cases = []
for m in (2, 4, 8, 12, 14):
    for source_r in (0, 1):
        case = restriction_case(m, source_r)
        cases.append(case)
        print(json.dumps(case, ensure_ascii=False), flush=True)

result = {
    "status": "finite-exact-probe-only",
    "new_own_execution_count": 1,
    "old_or_peer_execution_import_rerun_count": 0,
    "scope": "Exact p^8 local paired constraint kernels and restricted Gram Smith probes at five auxiliary primes, s5,r0/r1,X0. This does not prove all-m nonzero or all-prime content.",
    "cases": cases,
    "all_checked_local_identities_passed": True
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
