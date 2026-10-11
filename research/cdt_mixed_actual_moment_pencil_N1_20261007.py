"""New bounded certificate for the actual N=1 mixed moment pencil.

Only F_101 exact arithmetic; no period approximation or proposed relation.
The 44 x 43 row pool uses kappa*4^d*Jacobi rows, kappa=2^56,
the triangular low section and the zero-end endpoint completion.
This certifies finite generic rank, not all-N nonvanishing.
"""
from math import comb
from pathlib import Path
import hashlib
import json

PRIME = 101
N, A, H, h, q, b, n, L, e = 1, 19, 65, 2, 4, 7, 43, 54, 6


def inv(x):
    assert x % PRIME
    return pow(x % PRIME, -1, PRIME)


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


def power_linear(sign, degree):
    # (x+sign)^degree
    return [comb(degree, j) * sign ** (degree - j) % PRIME
            for j in range(degree + 1)]


def generalized_binom(upper, degree):
    ans = 1
    for j in range(degree):
        ans = ans * (upper - j) * inv(j + 1) % PRIME
    return ans


def jacobi(degree):
    out = [0] * (degree + 1)
    for v in range(degree + 1):
        scalar = (generalized_binom(degree + e - inv(2), v)
                  * generalized_binom(degree - inv(2), degree - v)
                  * pow(inv(2), degree, PRIME)) % PRIME
        term = mul(power_linear(-1, degree - v), power_linear(1, v))
        for j, val in enumerate(term):
            out[j] = (out[j] + scalar * val) % PRIME
    # 4^d, rather than 8^d; its integrality has a separate paper proof.
    return [val * pow(4, degree, PRIME) % PRIME for val in out]


def coefficient(poly, index):
    return poly[index] if 0 <= index < len(poly) else 0


def cindex(index):
    if index < 0 or index % 2:
        return 0
    half = index // 2
    return comb(2 * half, half) * pow(inv(4), half, PRIME) % PRIME


def C(poly, j):
    return sum(val * cindex(i - j) for i, val in enumerate(poly)) % PRIME


def HH(poly, j):
    return sum(val * cindex(j - i - 1) for i, val in enumerate(poly)) % PRIME


filter_weights = [(-1) ** v * comb(q, v) % PRIME for v in range(q + 1)]


def filtered(values, k):
    return sum(filter_weights[v] * values[b + k + v]
               for v in range(q + 1)) % PRIME


def section(delta):
    low = [0] * L
    for k in range(A - b - q + 1, n):
        jlast = b + k + q
        target = filtered(delta, k)
        previous = sum(filter_weights[v] * low[b + k + v]
                       for v in range(q)) % PRIME
        low[jlast] = (target - previous) * inv(filter_weights[-1]) % PRIME
    m = L - A - 1
    vpoly = [sum(comb(h + r - 1, r) * low[A + 1 + u - r]
                 for r in range(u + 1)) % PRIME for u in range(m)]
    completed = [0] * (A + 1) + mul(vpoly, power_linear(-1, h))
    # h is even, so (t-1)^h=(1-t)^h.
    assert len(completed) <= H
    assert completed[:L] == low
    assert sum(completed) % PRIME == 0
    assert sum(j * val for j, val in enumerate(completed)) % PRIME == 0
    return completed


def gaussian(matrix):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot = 0
    pivots, swaps = [], []
    det = 1
    for col in range(cols):
        selected = next((r for r in range(pivot, rows) if a[r][col]), None)
        if selected is None:
            continue
        if selected != pivot:
            a[pivot], a[selected] = a[selected], a[pivot]
            swaps.append([pivot, selected])
            det = -det
        value = a[pivot][col]
        pivots.append([pivot, col, value])
        det = det * value % PRIME
        for r in range(pivot + 1, rows):
            scalar = a[r][col] * inv(value) % PRIME
            if scalar:
                for j in range(col, cols):
                    a[r][j] = (a[r][j] - scalar * a[pivot][j]) % PRIME
        pivot += 1
        if pivot == rows:
            break
    return dict(rank=pivot, pivots=pivots, swaps=swaps,
                determinant=(det % PRIME if rows == cols and pivot == rows
                             else 0 if rows == cols else None))


# Exact source rational arrays, reduced modulo 101. All denominators are
# units, because their prime factors are <=65; 101 is one fixed modulus.
moments = [0] * H
moments[0] = 2
for i in range(2, H, 2):
    moments[i] = i * moments[i - 2] * inv(i + 1) % PRIME
minus = [0] * H
plus = [0] * L
minus[1] = 2
for d in range(2, H):
    minus[d] = ((d - 1) * minus[d - 2] + moments[d - 2]
                + moments[d - 1]) * inv(d) % PRIME
for d in range(2, L):
    plus[d] = ((d - 2) * plus[d - 2] + 2 * inv(d - 1)) * inv(d - 1) % PRIME
M0 = [[0] * L for _ in range(H)]
for i in range(H):
    M0[i][0] = minus[i]
for j in range(L):
    M0[0][j] = plus[j]
for i in range(1, H):
    for j in range(1, L):
        M0[i][j] = (M0[i - 1][j - 1] - moments[i - 1] * inv(j)) % PRIME
harm1, harm2 = [0] * H, [0] * H
for i in range(1, H):
    harm1[i] = (harm1[i - 1] + inv(i)) % PRIME
    harm2[i] = (harm2[i - 1] + inv(i) ** 2) % PRIME
Z0 = [[(-harm2[i] if i == j else (harm1[i] - harm1[j]) * inv(i - j)) % PRIME
       for j in range(L)] for i in range(H)]

rows = []
for d in range(9, 44):
    pp = [0] * A + mul(power_linear(-1, h), jacobi(d))
    pp = [val * pow(2, 56, PRIME) % PRIME for val in pp]
    cc = [C(pp, j) for j in range(L)]
    hh = [HH(pp, j) for j in range(L)]
    d0, d1 = section(hh), section([(-val) % PRIME for val in cc])
    assert all(filtered(cc, k) == 0 for k in range(9))
    assert all(filtered([(hh[j] - coefficient(d0, j)) % PRIME
                         for j in range(L)], k) == 0 for k in range(n))
    assert all(filtered([(-cc[j] - coefficient(d1, j)) % PRIME
                         for j in range(L)], k) == 0 for k in range(n))
    rows.append(dict(kind="Jacobi", degree=d, P=pp, D0=d0, D1=d1))
for r in range(9):
    dd = [0] * (L + r) + power_linear(-1, h)
    assert len(dd) <= H
    rows.append(dict(kind="pure_D_tail", tail=r, P=[0], D0=dd, D1=[0]))

E0, E1, CF = [], [], []
for row in rows:
    ppoly, d0, d1 = row["P"], row["D0"], row["D1"]
    z0 = [sum(coefficient(ppoly, i) * M0[i][j]
              - 3 * inv(2) * coefficient(d0, i) * Z0[i][j]
              for i in range(H)) % PRIME for j in range(L)]
    z1 = [sum(-3 * inv(2) * coefficient(d1, i) * Z0[i][j]
              for i in range(H)) % PRIME for j in range(L)]
    cs = [C(ppoly, j) for j in range(L)]
    E0.append([filtered(z0, k) for k in range(n)])
    E1.append([filtered(z1, k) for k in range(n)])
    CF.append([filtered(cs, k) for k in range(n)])

evaluations = []
for mu in (1, 2, -1):
    for gamma in (0, 1, -1):
        mat = [[(E0[r][k] + mu * E1[r][k] + gamma * CF[r][k]) % PRIME
                for k in range(n)] for r in range(len(rows))]
        evaluations.append(dict(mu=mu, gamma=gamma, full_pool=gaussian(mat),
                                selected_square=gaussian(mat[:-1])))

output = dict(
    classification="finite_exact_modular_certificate_only",
    actual_relation_assumed=False, periods_approximated=False,
    modulus=PRIME, N=N, parameters=dict(A=A,H=H,h=h,q=q,b=b,n=n,L=L,e=e),
    row_normalization="kappa*4^d*J_d for Jacobi; kappa=2^56; no primitive claim",
    gamma_definition="4u/alpha", mu_definition="16beta/alpha",
    pencil="E0 + mu E1 + gamma CF",
    rows=rows, matrices=dict(E0=E0, E1=E1, CF=CF),
    component_ranks=dict(E0=gaussian(E0)["rank"], E1=gaussian(E1)["rank"],
                         CF=gaussian(CF)["rank"],
                         CF_residual=gaussian([row[9:] for row in CF[:35]])["rank"],
                         tail_first9=gaussian([row[:9] for row in E0[35:]])),
    evaluations=evaluations,
    inference_scope="Only finite N=1 generic polynomial nonzero witnesses; no all-N or all-rational-parameter conclusion",
)
dest = Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
print(json.dumps(dict(path=str(dest),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
                     component_ranks=output["component_ranks"],
                     tests=[dict(mu=x["mu"], gamma=x["gamma"],
                                 rank=x["full_pool"]["rank"],
                                 det=x["selected_square"]["determinant"])
                            for x in evaluations]), ensure_ascii=False))
