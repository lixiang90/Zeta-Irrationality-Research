"""NEW first-only mechanism verifier; no old or peer source is imported or run.

Only r=1,2,4 previously examined auxiliary primes. Actual target determinants
are compared by identities, never asserted to be units. Full actual QQ profile
and the p19 parameter-family counterexample are separate proved mechanisms.
"""
from pathlib import Path
from math import comb
import json
import hashlib

out = Path(__file__).with_suffix(".json")
if out.exists():
    raise SystemExit("FIRST-ONLY guard: output exists; do not rerun")
checks = 0

def require(value):
    global checks
    checks += 1
    assert value

def det(a, p):
    a = [row[:] for row in a]
    n, result = len(a), 1
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j] % p), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        v = a[j][j] % p
        result = result * v % p
        inv = pow(v, -1, p)
        for i in range(j + 1, n):
            t = a[i][j] * inv % p
            for k in range(j + 1, n):
                a[i][k] = (a[i][k] - t * a[j][k]) % p
    return result % p

def mv(a, v, p):
    return [sum(x * y for x, y in zip(row, v)) % p for row in a]

def gram(cols, weights, p):
    return [[sum(w * x * y for w, x, y in zip(weights, a, b)) % p
             for b in cols] for a in cols]

def add(a, b, p):
    return [[(x + y) % p for x, y in zip(ar, br)] for ar, br in zip(a, b)]

def prod(values, p):
    z = 1
    for v in values:
        z = z * v % p
    return z

def interpolate(values, p):
    ans = [0] * len(values)
    for i, y in enumerate(values):
        poly, denominator = [1], 1
        for j in range(len(values)):
            if j == i:
                continue
            q = [0] * (len(poly) + 1)
            for k, c in enumerate(poly):
                q[k] = (q[k] - j * c) % p
                q[k + 1] = (q[k + 1] + c) % p
            poly = q
            denominator = denominator * (i - j) % p
        scale = y * pow(denominator, -1, p) % p
        for k, c in enumerate(poly):
            ans[k] = (ans[k] + scale * c) % p
    return ans

def peval(poly, x, p):
    y = 0
    for c in reversed(poly):
        y = (y * x + c) % p
    return y

def pder(poly, p):
    return [(j * poly[j]) % p for j in range(1, len(poly))]

cases = []
for r in (1, 2, 4):
    p, a, N = 18 * r + 1, 5 * r, 5 * r + 1
    inv2, gamma = pow(2, -1, p), -98 * pow(27, -1, p) % p
    u = [k * k % p for k in range(N)]
    sy = [prod((v - k * k for k in range(a + 1, 9 * r + 1)), p) for v in u]
    R = [pow(s, 4, p) for s in sy]
    base = [pow(s, -5, p) * (inv2 if k == 0 else 1) % p
            for k, s in enumerate(sy)]
    actual = [w * (2 if k < r else 1) % p for k, w in enumerate(base)]

    def A(x):
        return ((x + inv2) * (a - x) * pow(x + a + 1, 6, p)
                * (x + r) * (x + 1 - r)) % p

    J = [[0] * N for _ in range(N)]
    for k in range(N):
        J[k][k] = (-A(k) - A(-k) + gamma * pow(k, 8, p)) % p
        if k < a:
            J[k][k + 1] = A(k) * (2 if k == 0 else 1) % p
        if k:
            J[k][k - 1] = A(-k)
    require(J[r - 1][r] == J[r][r - 1] == 0)

    def lam(channel, d):
        if channel == 0:
            return -(2 * d + pow(3, -1, p)) * (2 * d + 98 * pow(9, -1, p)) % p
        return -(2 * d - 13 * pow(9, -1, p)) * (2 * d + 82 * pow(9, -1, p)) % p

    def krylov(channel, m):
        columns, delta = [], 1
        for d in range(m):
            s, j = d % 4, d // 4
            v = [pow(t, s, p) * (R[k] if channel else 1) % p
                 for k, t in enumerate(u)]
            for _ in range(j):
                v = mv(J, v, p)
            if channel:
                v = [x * pow(R[k], -1, p) % p for k, x in enumerate(v)]
            lead = prod((lam(channel, s + 4 * h) for h in range(j)), p)
            require(lead != 0)
            delta = delta * lead % p
            columns.append(v)
        return columns, delta

    qfull, deltaN = krylov(4, N)
    vhead = [[pow(t, d, p) for d in range(N)] for t in u]
    qmatrix = [list(row) for row in zip(*qfull)]
    require(det(qmatrix, p) == deltaN * det(vhead, p) % p)
    qqweights = [w * z * z % p for w, z in zip(actual, R)]
    full_expected = deltaN ** 2 * det(vhead, p) ** 2 * prod(qqweights, p) % p
    full_actual = det(gram(qfull, qqweights, p), p)
    require(full_actual == full_expected and full_actual != 0)

    Tk, deltaT = krylov(0, r)
    Qk, deltaQ = krylov(4, 3 * r)
    QkR = [[x * R[k] % p for k, x in enumerate(v)] for v in Qk]
    Traw = [[pow(t, d, p) for t in u] for d in range(r)]
    QrawR = [[R[k] * pow(t, d, p) % p for k, t in enumerate(u)]
             for d in range(3 * r)]

    def M(columnsT, columnsQR, value):
        plus = columnsT + columnsQR
        minus = columnsT + [[-x % p for x in v] for v in columnsQR]
        gp = gram(plus, [3 * w % p for w in base], p)
        gm = gram(minus, [w * ((value - 3) if k < r else -2) % p
                          for k, w in enumerate(base)], p)
        return add(gp, gm, p)

    def G(value):
        return gram(Traw, [w * (value if k < r else 1) % p
                           for k, w in enumerate(base)], p)

    VM = [[pow(t, d, p) for d in range(r)] for t in u[:r]]
    gfactor = det(VM, p) ** 2 * prod(base[:r], p) % p
    Kprime = [prod((ui - uj for j, uj in enumerate(u[:r]) if i != j), p)
              for i, ui in enumerate(u[:r])]
    outerX = []
    for uk in u[r:]:
        middle_product = prod((uk - ui for ui in u[:r]), p)
        outerX.append([middle_product * pow((uk - ui) * Kprime[i] % p, -1, p) % p
                       for i, ui in enumerate(u[:r])])
    Xcols = [list(v) for v in zip(*outerX)]
    KDN = gram(Xcols, base[r:], p)
    KDN = [[z * pow(base[i], -1, p) % p for z in row]
           for i, row in enumerate(KDN)]
    A3 = M(Traw, QrawR, 3)
    L = [[pow(ui, d, p) for d in range(r)]
         + [(-R[k] * pow(ui, d, p)) % p for d in range(3 * r)]
         for k, ui in enumerate(u[:r])]
    mvalues = [det(M(Traw, QrawR, value), p) for value in range(r + 1)]
    mpoly = interpolate(mvalues, p)
    gpoly = interpolate([det(G(value), p) for value in range(r + 1)], p)
    require(gpoly[-1] == gfactor != 0)

    for value in range(p):
        mk = M(Tk, QkR, value)
        mr = M(Traw, QrawR, value)
        require(det(mk, p) == (deltaT * deltaQ) ** 2 * det(mr, p) % p)
        require(det(mr, p) == peval(mpoly, value, p))
        shifted = [[(z + (value if i == j else 0)) % p for j, z in enumerate(row)]
                   for i, row in enumerate(KDN)]
        require(det(G(value), p) == gfactor * det(shifted, p) % p)
        require(det(G(value), p) == peval(gpoly, value, p))
        if value in (2, 3, 8):
            border = [row[:] + [((value - 3) * L[j][i] * base[j]) % p
                                 for j in range(r)] for i, row in enumerate(A3)]
            border += [row[:] + [(-1 if i == j else 0) % p for j in range(r)]
                       for i, row in enumerate(L)]
            require(det(border, p) == (-1) ** r * det(mr, p) % p)

    endpoint_checks = 0
    for start, end in ((0, r), (r, N)):
        m = end - start
        JB = [row[start:end] for row in J[start:end]]
        bs = [JB[j][j - 1] for j in range(1, m)]
        theta = [[1], [-JB[0][0] % p, 1]]
        for j in range(1, m):
            prev, old = theta[-1], theta[-2]
            new = [0] * (j + 2)
            for h, c in enumerate(prev):
                new[h + 1] = (new[h + 1] + c) % p
                new[h] = (new[h] - JB[j][j] * c) % p
            ab = JB[j - 1][j] * JB[j][j - 1] % p
            for h, c in enumerate(old):
                new[h] = (new[h] - ab * c) % p
            theta.append(new)
        endpoint = [1] + [0] * (m - 1)
        powers = [endpoint]
        for _ in range(2 * m + 2):
            powers.append(mv(JB, powers[-1], p))
        moments = [base[start] * v[0] % p for v in powers]
        for j in range(m):
            vector = [sum(c * powers[h][i] for h, c in enumerate(theta[j])) % p
                      for i in range(m)]
            require(vector == [prod(bs[:j], p) if i == j else 0 for i in range(m)])
            endpoint_checks += 1
        extended = theta + [[0] + theta[-1]]
        for n in (1, m):
            H = [[moments[i + j] for j in range(n)] for i in range(n)]
            for c in (0, 1):
                modified = [[(moments[i + j + 1] - c * moments[i + j]) % p
                             for j in range(n)] for i in range(n)]
                require(det(modified, p) == (-1) ** n * det(H, p) * peval(theta[n], c, p) % p)
                squared = [[(moments[i + j + 2] - 2 * c * moments[i + j + 1]
                             + c * c * moments[i + j]) % p
                            for j in range(n)] for i in range(n)]
                wronskian = (peval(extended[n], c, p) * peval(pder(extended[n + 1], p), c, p)
                             - peval(pder(extended[n], p), c, p) * peval(extended[n + 1], c, p)) % p
                require(det(squared, p) == det(H, p) * wronskian % p)
    if r == 1:
        require(base == [3, 3, 7, 2, 18, 3])
        require(gpoly == [14, 3] and det(G(8), p) == 0 and det(G(2), p) == 1)
        require(8 not in (0, 3))
    cases.append({"r": r, "p": p, "N": N, "QQ_full_profile_unit": full_actual,
                  "delta4_full_N": deltaN, "G_lambda_coefficients": gpoly,
                  "M_lambda_coefficients": mpoly, "endpoint_connection_columns_checked": endpoint_checks,
                  "actual_G2_for_identity_only": det(G(2), p),
                  "actual_M2_for_identity_only": det(M(Traw, QrawR, 2), p)})

payload = {"status": "PASS", "execution_count": 1, "cases": cases, "exact_checks": checks,
           "old_or_peer_execute_import_rerun_count": 0,
           "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "scope": "Structural modified-target identities on old r=1,2,4 only; no auxiliary-prime table extension.",
           "counterexample_scope": "p19 lambda8 is a genuine chi-preserving parameter-family critical singularity, not the actual lambda2.",
           "not_proved": ["Infinite actual critical G2/M2 units", "Global Krylov fees",
                          "Strict margin", "Special-value theorem", "External Lean"]}
out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(json.dumps(payload, indent=2))
