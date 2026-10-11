"""NEW first-execution-only finite-field structure probe.

Only folded exact G0/H0/C5 and their Gram ranks at finitely many auxiliary
primes are computed. No old/peer producer is read, executed, or imported.
The general centered/Wilson/Pearson/residue lemmas are paper proofs.
"""
import json
import math
from pathlib import Path

OUT = Path(__file__).with_suffix(".json")
if OUT.exists():
    raise RuntimeError("First execution only: preserve existing output, do not rerun.")


def prime(n):
    return n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1))


def rank_det_null(rows, p):
    a = [[x % p for x in row] for row in rows]
    size = len(a)
    pivots = []
    det = 1
    for col in range(size):
        row = len(pivots)
        hit = next((j for j in range(row, size) if a[j][col]), None)
        if hit is None:
            continue
        if hit != row:
            a[row], a[hit] = a[hit], a[row]
            det = -det
        pv = a[row][col]
        det = det * pv % p
        inv = pow(pv, -1, p)
        tail = a[row][col + 1:]
        for j in range(row + 1, size):
            if not a[j][col]:
                continue
            fac = a[j][col] * inv % p
            a[j][col + 1:] = [(x - fac * y) % p
                              for x, y in zip(a[j][col + 1:], tail)]
            a[j][col] = 0
        pivots.append(col)
    if len(pivots) == size:
        return size, det % p, None
    free = next(i for i in range(size) if i not in pivots)
    v = [0] * size
    v[free] = 1
    for row in range(len(pivots) - 1, -1, -1):
        col = pivots[row]
        v[col] = (-sum(a[row][j] * v[j] for j in range(col + 1, size))
                  * pow(a[row][col], -1, p)) % p
    assert any(v)
    assert all(sum(x * y for x, y in zip(row, v)) % p == 0 for row in rows)
    return len(pivots), 0, v


def moments(r, p):
    fact = [1]
    for k in range(1, p):
        fact.append(fact[-1] * k % p)
    gm, hm, cm = [0] * (2*r-1), [0] * (6*r-1), [0] * (4*r-1)
    checks = 0
    for k in range(5*r + 1):
        sval = 1
        for j in range(5*r + 1, 9*r + 1):
            sval = sval * (k*k - j*j) % p
        wilson = ((-1)**(r+k+1) * pow(fact[5*r-k] * fact[5*r+k] % p, -1, p)) % p
        assert sval == wilson and sval
        checks += 1
        sinv = pow(sval, -1, p)
        mult = 1 if k == 0 or k >= r else 2
        cross = 2 if k == 0 else (4 if k < r else 5)
        ug, uh, uc = mult * pow(sinv, 5, p), mult * pow(sval, 3, p), cross * sinv
        power = 1
        x = k*k % p
        for j in range(6*r - 1):
            hm[j] = (hm[j] + uh * power) % p
            if j < len(gm):
                gm[j] = (gm[j] + ug * power) % p
            if j < len(cm):
                cm[j] = (cm[j] + uc * power) % p
            power = power * x % p
    return gm, hm, cm, checks


cases = []
for r in range(1, 91):
    p = 18*r + 1
    if not prime(p):
        continue
    gm, hm, cm, checks = moments(r, p)
    g0 = [[gm[i+j] for j in range(r)] for i in range(r)]
    h0 = [[hm[i+j] for j in range(3*r)] for i in range(3*r)]
    cross = [[cm[i+j] for j in range(r)] for i in range(3*r)]
    joint = [
        (g0[i] + [cross[j][i] for j in range(3*r)]) if i < r
        else (cross[i-r] + h0[i-r]) for i in range(4*r)
    ]
    grank, gdet, gv = rank_det_null(g0, p)
    mrank, mdet, mv = rank_det_null(joint, p)
    case = {"r": r, "m": 2*r, "n": 4*r, "p": p,
            "G0_dimension": r, "G0_rank": grank, "G0_det": gdet,
            "M5_dimension": 4*r, "M5_rank": mrank, "M5_det": mdet,
            "centered_Wilson_node_checks": checks,
            "G0_null_vector_if_singular": gv,
            "M5_null_vector_if_singular": mv}
    cases.append(case)
    print(json.dumps({k: v for k, v in case.items() if "vector" not in k}), flush=True)

result = {"status": "finite-exact-structure-probe-only",
          "own_new_execution_count": 1, "old_or_peer_execution_import_rerun_count": 0,
          "scope": "All primes p=18r+1 with 1<=r<=90; exact centered folded matrices at s5, with all middle multiplicities and the actual half jet retained.",
          "not_proved": ["Infinite unit subsequence", "All-prime margin", "New irrationality"],
          "cases": cases}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
