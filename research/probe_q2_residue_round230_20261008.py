"""Eight preselected exact probes, not an all-scale rank certificate."""
from fractions import Fraction as F
from math import comb, isqrt
from pathlib import Path
import json

CASES = [(1, 5), (3, 11), (3, 13), (4, 17),
         (5, 17), (5, 19), (8, 29), (8, 31)]
MAX_L = max(3*d + 1 for d, p in CASES)

def moment(e):
    if e % 2:
        return F(0)
    a = e // 2
    return F(2 * 4**a, (2*a + 1) * comb(2*a, a))

cs = [F(comb(2*l, l), 4**l) for l in range(MAX_L + 1)]
hs = [sum((F(1, k) for k in range(l+1, 2*l+1)), F(0))
      for l in range(MAX_L + 1)]
Q, R = [F(0)], [F(0)]
for l in range(1, MAX_L + 1):
    Q.append(((2*l-1)*Q[-1] + moment(2*l-2))/(2*l))
    R.append(((2*l-1)*R[-1] + Q[l-1] - Q[l])/(2*l))

# Independent finite-sum formulas from the actual recurrence, all exact.
alpha = [sum((moment(2*a)**2 / 2 for a in range(l)), F(0))
         for l in range(MAX_L + 1)]
for l in range(MAX_L + 1):
    rho = sum((alpha[a-1]/(2*a*(2*a-1)) - moment(2*a-2)**2/(4*a)
               for a in range(1, l+1)), F(0))
    assert Q[l] == cs[l]*alpha[l]
    assert R[l] == cs[l]*rho

def mod(v, p):
    assert v.denominator % p, "Nonintegral residue requested"
    return (v.numerator % p) * pow(v.denominator, -1, p) % p

def rank(matrix, p):
    a = [row[:] for row in matrix]
    nr, nc = len(a), len(a[0])
    k = 0
    for col in range(nc):
        pivot = next((r for r in range(k, nr) if a[r][col] % p), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        scale = pow(a[k][col], -1, p)
        a[k] = [(v*scale) % p for v in a[k]]
        for r in range(nr):
            if r != k and a[r][col]:
                c = a[r][col]
                a[r] = [(x-c*y) % p for x, y in zip(a[r], a[k])]
        k += 1
        if k == nr:
            break
    return k

results = []
for d, p in CASES:
    m, L = d+1, 3*d+1
    assert L < p <= 2*(L-m)+1
    assert all(p % t for t in range(2, isqrt(p)+1))
    A = [[mod(cs[r+s], p) for r in range(2*m)] for s in range(m)]
    B = [[mod(4*cs[r+s]*hs[r+s], p) for r in range(2*m)] for s in range(m)]
    pa = []
    for s in range(m):
        row = []
        for r in range(2*m):
            l, j = r+s, 2*(d-s)
            tail = R[l] - sum((moment(2*l+v-1)/v**2 for v in range(1, j+1)), F(0))
            row.append(mod(p*tail, p))
        pa.append(row)
    rb, rp, full = rank(B, p), rank(pa, p), rank(B+pa, p)
    zero_columns = sum(all(pa[s][r] == 0 for s in range(m)) for r in range(2*m))
    expected_zero = (p-1)//2 - d + 1
    assert zero_columns >= expected_zero
    results.append({"d": d, "p": p, "m": m, "source_pole_rows": L-(p-1)//2,
                    "rank_B": rb, "rank_p_a": rp, "rank_stacked_residue": full,
                    "rank_E_mod_p": rank(A+B, p), "polar_rank_increment": full-rb,
                    "required_rank": 2*m,
                    "matrices": {"A": A, "B": B, "p_a_transpose": pa}})

out = {"round": 230, "method": "Exact Fraction and finite-field elimination",
       "scope": "Eight fixed cases only; no infinite rank or irrationality claim",
       "independent_rational_tail_checks": MAX_L+1, "cases": results}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": "PASS", "cases": [
    {k: v for k, v in row.items() if k != "matrices"} for row in results]}, ensure_ascii=False))
