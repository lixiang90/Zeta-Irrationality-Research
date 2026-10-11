"""New finite observability calculation from saved actual N=1 matrices.

No previous producer is rerun. All operations are in F_101. Nonzero cyclic
determinants imply all-complex-gamma rank at the specified rational mu and
N=1 after lifting; no all-N or irrationality theorem follows.
"""
import hashlib
import json
from pathlib import Path

INPUT = Path(__file__).with_name("cdt_mixed_actual_moment_pencil_N1_20261007.json")
data = json.loads(INPUT.read_text(encoding="utf-8"))
P = data["modulus"]
assert P == 101 and data["N"] == 1


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) % P for col in bt]
            for row in a]


def difference(a, b):
    return [[(x-y) % P for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def gauss(a):
    a = [row[:] for row in a]
    rows, cols = len(a), len(a[0])
    pivot, determinant = 0, 1
    columns, pivots, swaps = [], [], []
    for col in range(cols):
        selected = next((i for i in range(pivot, rows) if a[i][col]), None)
        if selected is None:
            continue
        if selected != pivot:
            a[pivot], a[selected] = a[selected], a[pivot]
            swaps.append([pivot, selected])
            determinant = -determinant
        value = a[pivot][col]
        determinant = determinant * value % P
        columns.append(col)
        pivots.append(value)
        for i in range(pivot + 1, rows):
            scale = a[i][col] * pow(value, -1, P) % P
            if scale:
                a[i] = [(x-scale*y) % P for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return dict(rank=pivot, columns=columns, pivots=pivots, swaps=swaps,
                determinant=determinant % P if rows == cols and pivot == rows
                else 0 if rows == cols else None)


def inverse(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    aug = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        i = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[i] = aug[i], aug[j]
        scale = pow(aug[j][j], -1, P)
        aug[j] = [x * scale % P for x in aug[j]]
        for i in range(n):
            if i != j:
                scale = aug[i][j]
                aug[i] = [(x-scale*y) % P for x, y in zip(aug[i], aug[j])]
    result = [row[n:] for row in aug]
    assert matmul(a, result) == [[int(i == j) for j in range(n)] for i in range(n)]
    return result


E0, E1, CF = [data["matrices"][key] for key in ("E0", "E1", "CF")]
d, p, m = 9, 35, 34
T0, T1 = [row[:d] for row in E0[p:]], [row[d:] for row in E0[p:]]
W = matmul(inverse(T0), T1)
S0 = difference([row[d:] for row in E0[:p]], matmul([row[:d] for row in E0[:p]], W))
S1 = difference([row[d:] for row in E1[:p]], matmul([row[:d] for row in E1[:p]], W))
C1 = [row[d:] for row in CF[:p]]
chosen = gauss(transpose(C1))["columns"]
assert len(chosen) == m
extra = next(i for i in range(p) if i not in chosen)
Cinv = inverse([C1[i] for i in chosen])
A = matmul(Cinv, [S0[i] for i in chosen])
B = matmul(Cinv, [S1[i] for i in chosen])
v = difference([S0[extra]], matmul([C1[extra]], A))[0]
zero1 = difference([S1[extra]], matmul([C1[extra]], B))[0]
assert all(x == 0 for x in zero1)
assert matmul(Cinv, [C1[i] for i in chosen]) == [[int(i == j) for j in range(m)] for i in range(m)]

records = []
for mu in (1, 2, -1, 0):
    mm = [[(A[i][j]+mu*B[i][j]) % P for j in range(m)] for i in range(m)]
    rows = [v]
    for i in range(1, m):
        rows.append(matmul([rows[-1]], mm)[0])
    result = gauss(rows)
    records.append(dict(mu=mu, matrix=mm, observability_matrix=rows, gaussian=result))

out = dict(classification="finite_N1_exact_observability_certificate",
           input_path=str(INPUT), input_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
           modulus=P, N=1, row_normalization=data["row_normalization"],
           size=dict(tail=d, nonzero_P=p, residual=m),
           tail_inverse=inverse(T0), W=W, S0=S0, S1=S1, C1=C1,
           selected_C1_rows=chosen, extra_row=extra, C1_inverse=Cinv,
           canonical=dict(A=A, B=B, v=v, extra_S1=zero1), records=records,
           inference="A nonzero saved cyclic determinant certifies fixed N=1, fixed rational mu, all complex gamma full-pool rank; not a chosen omitted-tail minor, not all N, not a numerical irrationality result",
           historical_producer_runs=0, previous_producer_rerun=False)
dest = Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(dict(path=str(dest), sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
                     chosen=chosen, extra=extra, v_nonzero=any(v),
                     results=[dict(mu=r["mu"], rank=r["gaussian"]["rank"],
                                   det=r["gaussian"]["determinant"])
                              for r in records])))
