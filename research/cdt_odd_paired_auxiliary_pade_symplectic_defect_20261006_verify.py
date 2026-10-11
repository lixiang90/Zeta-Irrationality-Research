"""NEW first-only structural probe: real CRT graph modules and critical shifts.

No old or peer producer is read, imported, or executed. Only previously
examined r-values are used. Nearby degree profiles probe the symplectic
defect mechanism; they do not certify the actual target or infinite primes.
"""
from pathlib import Path
import json
import hashlib

OUT = Path(__file__).with_suffix(".json")
if OUT.exists():
    raise RuntimeError("First execution only; preserve output and do not rerun.")


def trim(a, p):
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b, p):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def scal(a, c, p):
    return trim([c*x for x in a], p)


def mul(a, b, p):
    c = [0] * max(0, len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % p
    return trim(c, p)


def divrem(a, b, p):
    assert b
    a = trim(a[:], p)
    q = [0] * max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while a and len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*inv % p
        q[k] = c
        for j, x in enumerate(b):
            a[k+j] = (a[k+j]-c*x) % p
        a = trim(a, p)
    return trim(q, p), a


def evaluate(a, x, p):
    v = 0
    for c in reversed(a):
        v = (v*x+c) % p
    return v


def power(a, n, p):
    v = [1]
    while n:
        if n & 1:
            v = mul(v, a, p)
        a = mul(a, a, p)
        n //= 2
    return v


def rank_det(a, p):
    a = [[x % p for x in row] for row in a]
    n = len(a)
    det, rank = 1, 0
    for col in range(n):
        hit = next((j for j in range(rank, n) if a[j][col]), None)
        if hit is None:
            continue
        if hit != rank:
            a[hit], a[rank] = a[rank], a[hit]
            det = -det
        pivot = a[rank][col]
        det = det*pivot % p
        inv = pow(pivot, -1, p)
        for j in range(rank+1, n):
            c = a[j][col]*inv % p
            for k in range(col, n):
                a[j][k] = (a[j][k]-c*a[rank][k]) % p
        rank += 1
    return rank, det % p if rank == n else 0


def sd_lp(row, shift):
    options = [(len(f)-1+shift[i], i)
               for i, f in enumerate(row) if f]
    assert options
    return max(options)


def weak_popov(rows, shift, p):
    rows = [[f[:] for f in row] for row in rows]
    reductions = 0
    while True:
        leaders = [sd_lp(row, shift) for row in rows]
        hit = next(((i, j) for i in range(len(rows))
                    for j in range(i+1, len(rows))
                    if leaders[i][1] == leaders[j][1]), None)
        if hit is None:
            return rows, leaders, reductions
        i, j = hit
        if leaders[i][0] > leaders[j][0]:
            i, j = j, i
        pos = leaders[i][1]
        gap = leaders[j][0]-leaders[i][0]
        c = rows[j][pos][-1]*pow(rows[i][pos][-1], -1, p) % p
        old_measure = len(rows)*(leaders[j][0])+pos
        for k in range(len(rows)):
            rows[j][k] = add(rows[j][k],
                            [0]*gap+scal(rows[i][k], -c, p), p)
        new_sd, new_lp = sd_lp(rows[j], shift)
        assert len(rows)*new_sd+new_lp < old_measure
        reductions += 1
        assert reductions < 200000


def numerator(weights, nodes, P, p):
    q = []
    for w, x in zip(weights, nodes):
        Ppart, rem = divrem(P, [-x, 1], p)
        assert not rem
        q = add(q, scal(Ppart, w, p), p)
    return q


def beta(row, other, size, P, p):
    v = []
    for i in range(size):
        v = add(v, mul(row[i], other[size+i], p), p)
        v = add(v, scal(mul(row[size+i], other[i], p), -1, p), p)
    q, rem = divrem(v, P, p)
    assert not rem
    return q


def module_profile(Nmat, P, bounds, p):
    size = len(Nmat)
    zero = []
    rows = []
    for i in range(size):
        rows.append([[1] if j == i else [] for j in range(size)] +
                    [Nmat[i][j][:] for j in range(size)])
    for i in range(size):
        rows.append([zero[:] for _ in range(size)] +
                    [P[:] if j == i else [] for j in range(size)])
    shift = [-b for b in bounds]
    reduced, leaders, count = weak_popov(rows, shift, p)
    degrees = sorted(sd for sd, _ in leaders)
    assert sum(degrees) == 0
    assert all(degrees[i]+degrees[-1-i] == 0
               for i in range(2*size))
    checks = 0
    for i, row in enumerate(reduced):
        for j in range(size):
            rem = row[size+j][:]
            for k in range(size):
                rem = add(rem, scal(mul(row[k], Nmat[k][j], p), -1, p), p)
            assert not divrem(rem, P, p)[1]
            checks += 1
        for j, other in enumerate(reduced):
            f = beta(row, other, size, P, p)
            if f:
                assert len(f)-1 <= leaders[i][0]+leaders[j][0]
            checks += 1
    return degrees, count, checks


def hankel(weights, nodes, d, p):
    return [[sum(w*pow(x, i+j, p) for w, x in zip(weights, nodes)) % p
             for j in range(d)] for i in range(d)]


def padded_psc(P, g, d, p):
    N = len(P)-1
    polynomials = [[0]*j+P for j in reversed(range(d-1))]
    polynomials += [[0]*j+g for j in reversed(range(d))]
    columns = list(reversed(range(N-d, N+d-1)))
    a = [[f[k] if k < len(f) else 0 for k in columns]
         for f in polynomials]
    assert len(a) == 2*d-1 and all(len(row) == len(a) for row in a)
    return rank_det(a, p)[1]


cases = []
for r in (1, 2, 4, 6, 7):
    p, N = 18*r+1, 5*r+1
    nodes = [k*k % p for k in range(5*r+1)]
    P, S = [1], [1]
    for x in nodes:
        P = mul(P, [-x, 1], p)
    for j in range(5*r+1, 9*r+1):
        S = mul(S, [-j*j, 1], p)
    fermat = [0]*(9*r+2)
    fermat[1], fermat[-1] = p-1, 1
    assert mul(P, S, p) == fermat
    values = [evaluate(S, x, p) for x in nodes]
    mu = [1 if k == 0 or k >= r else 2 for k in range(5*r+1)]
    gamma = [2 if k == 0 else (4 if k < r else 5)
             for k in range(5*r+1)]
    gw = [v*pow(s, -5, p) % p for v, s in zip(mu, values)]
    hw = [v*pow(s, 3, p) % p for v, s in zip(mu, values)]
    cw = [v*pow(s, -1, p) % p for v, s in zip(gamma, values)]
    g, h, c = (numerator(w, nodes, P, p) for w in (gw, hw, cw))
    previous, current = P, g
    prs = [len(P)-1]
    while current:
        prs.append(len(current)-1)
        previous, current = current, divrem(previous, current, p)[1]
    scalar = []
    for d in sorted({max(1, r-1), r, r+1}):
        degrees, operations, checks = module_profile([[g]], P, [d, N-d], p)
        rank, det = rank_det(hankel(gw, nodes, d, p), p)
        assert d-rank == sum(max(0, -v) for v in degrees)
        psc = padded_psc(P, g, d, p)
        assert psc == pow(-1, d*(d-1)//2, p)*det % p
        assert (det != 0) == (N-d in prs[1:])
        scalar.append({"profile_T": d, "shifted_degrees": degrees,
                       "corank": d-rank, "padded_psc": psc,
                       "subresultant_Hankel_identity": True,
                       "weak_Popov_reductions": operations,
                       "graph_symplectic_degree_checks": checks})
    matrix = []
    for bT in sorted({max(1, r-1), r, r+1}):
        for bQ in (3*r-1, 3*r, 3*r+1):
            bounds = [bT, bQ, N-bT, N-bQ]
            degrees, operations, checks = module_profile([[g, c], [c, h]],
                                                        P, bounds, p)
            G = hankel(gw, nodes, bT, p)
            H = hankel(hw, nodes, bQ, p)
            C = [[sum(w*pow(x, i+j, p) for w, x in zip(cw, nodes)) % p
                  for j in range(bQ)] for i in range(bT)]
            gram = [G[i]+C[i] for i in range(bT)]
            gram += [[C[j][i] for j in range(bT)]+H[i] for i in range(bQ)]
            rank, _ = rank_det(gram, p)
            assert bT+bQ-rank == sum(max(0, -v) for v in degrees)
            matrix.append({"profile_T_Q": [bT, bQ], "shifted_degrees": degrees,
                           "corank": bT+bQ-rank,
                           "actual_profile": bT == r and bQ == 3*r,
                           "weak_Popov_reductions": operations,
                           "graph_symplectic_degree_checks": checks})
    cases.append({"r": r, "p": p, "P_degree": N,
                  "scalar_Euclidean_remainder_degrees": prs,
                  "scalar_profiles": scalar, "matrix_profiles": matrix})
    print(json.dumps({"r": r, "p": p, "PRS_degrees": prs,
                      "matrix_defects": [z["shifted_degrees"] for z in matrix]},
                     ensure_ascii=False), flush=True)

record = {
    "status": "PASS finite structural mechanism only",
    "own_new_execution_count": 1,
    "old_or_peer_execution_import_rerun_count": 0,
    "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Five already examined r-values, exact graph weak-Popov shift profiles, symplectic degree constraints, corank equivalence, scalar padded-PSC/Hankel sign and PRS degree flag. Nearby profiles are diagnostics, not the original target.",
    "not_proved": ["Infinite actual unit subsequence", "All-r balanced module",
                   "Any new arithmetic cost or irrationality"],
    "cases": cases
}
OUT.write_text(json.dumps(record, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
