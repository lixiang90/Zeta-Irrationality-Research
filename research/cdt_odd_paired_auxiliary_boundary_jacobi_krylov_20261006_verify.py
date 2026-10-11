"""NEW FIRST-ONLY structural verifier for actual boundary Jacobi/Krylov identities.

Only r=1,2,4 already examined previously. No prime-table extension. No old or
peer mathematical files read/imported/executed. All-scale proofs remain paper.
"""
from pathlib import Path
from math import comb
import json
import hashlib

TARGET = Path(__file__).with_suffix(".json")
assert not TARGET.exists(), "FIRST ONLY: refuse replacement or rerun"


def trim(v, p):
    v = [a % p for a in v]
    while len(v) > 1 and not v[-1]:
        v.pop()
    return v or [0]


def add(v, w, p):
    z = [0] * max(len(v), len(w))
    for i, a in enumerate(v):
        z[i] += a
    for i, a in enumerate(w):
        z[i] += a
    return trim(z, p)


def scale(v, a, p):
    return trim([a*x for x in v], p)


def mul(v, w, p):
    z = [0] * (len(v)+len(w)-1)
    for i, a in enumerate(v):
        for j, b in enumerate(w):
            z[i+j] += a*b
    return trim(z, p)


def power(v, n, p):
    z = [1]
    for _ in range(n):
        z = mul(z, v, p)
    return z


def shifted(v, c, p):
    z = [0] * len(v)
    for i, a in enumerate(v):
        for j in range(i+1):
            z[j] += a*comb(i, j)*pow(c, i-j, p)
    return trim(z, p)


def evaluate(v, x, p):
    z = 0
    for a in reversed(v):
        z = (z*x+a) % p
    return z


def remainder(v, w, p):
    z = trim(v[:], p)
    while z != [0] and len(z) >= len(w):
        a = z[-1]*pow(w[-1], -1, p) % p
        j = len(z)-len(w)
        for i, b in enumerate(w):
            z[i+j] -= a*b
        z = trim(z, p)
    return z


def determinant(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    answer = 1
    for j in range(len(a)):
        i = next((i for i in range(j, len(a)) if a[i][j]), None)
        if i is None:
            return 0
        if i != j:
            a[i], a[j] = a[j], a[i]
            answer = -answer
        pivot = a[j][j]
        answer = answer*pivot % p
        inv = pow(pivot, -1, p)
        for i in range(j+1, len(a)):
            q = a[i][j]*inv % p
            for k in range(j, len(a)):
                a[i][k] = (a[i][k]-q*a[j][k]) % p
    return answer % p


def matvec(jacobi, v, p):
    return [sum(a*b for a, b in zip(row, v)) % p for row in jacobi]


def run(r):
    p, a = 18*r+1, 5*r
    checks = 0

    def check(condition):
        nonlocal checks
        checks += 1
        assert condition, (r, p, checks)

    half = pow(2, -1, p)
    gamma = -98*pow(27, -1, p) % p
    jump = [r*(1-r), 1, 1]
    A = mul(mul(mul([half, 1], [a, -1], p),
                power([a+1, 1], 6, p), p), jump, p)
    B = mul(mul(mul([half, 1], power([a, -1], 5, p), p),
                power([a+1, 1], 2, p), p), jump, p)
    An, Bn = [x*((-1)**i) % p for i, x in enumerate(A)], [x*((-1)**i) % p for i, x in enumerate(B)]
    diagonal = scale(add(A, An, p), -1, p)

    def operator(f, mode):
        forward, backward = (A, An) if mode == 0 else (B, Bn)
        z = add(add(mul(forward, shifted(f, 1, p), p),
                    mul(backward, shifted(f, -1, p), p), p),
                mul(diagonal, f, p), p)
        return add(z, [0]*8+scale(f, gamma, p), p)

    def leading(d, mode):
        if mode == 0:
            return -(2*d+pow(3, -1, p))*(2*d+98*pow(9, -1, p)) % p
        return -(2*d-13*pow(9, -1, p))*(2*d+82*pow(9, -1, p)) % p

    for mode, length in ((0, r), (4, 3*r)):
        for d in range(length):
            f = [0]*(2*d)+[1]
            z = operator(f, mode)
            check(len(z) == 2*d+9 and z[-1] == leading(d, mode) != 0)
            check(all(not z[i] for i in range(1, len(z), 2)))

    Svalues = []
    weights, alpha, Rvalues = [], [], []
    for k in range(a+1):
        value = 1
        for v in range(a+1, 9*r+1):
            value = value*(k*k-v*v) % p
        check(value != 0)
        Svalues.append(value)
        weights.append(((1 if k == 0 else 2) if k < r else 1)*pow(value, -5, p) % p)
        alpha.append(2 if k < r else 5)
        Rvalues.append(pow(value, 4, p))

    jacobi = [[0]*(a+1) for _ in range(a+1)]
    for k in range(a+1):
        forward, backward = evaluate(A, k, p), evaluate(An, k, p)
        jacobi[k][k] = (-forward-backward+gamma*pow(k, 8, p)) % p
        if k < a:
            jacobi[k][k+1] = (2*forward if k == 0 else forward) % p
        if k:
            jacobi[k][k-1] = backward
    check(not jacobi[r-1][r] and not jacobi[r][r-1])
    for k in range(a):
        if k != r-1:
            check(jacobi[k][k+1] != 0 and jacobi[k+1][k] != 0)
        check(weights[k]*jacobi[k][k+1] % p == weights[k+1]*jacobi[k+1][k] % p)

    for mode, length in ((0, r), (4, 3*r)):
        for d in range(length):
            f = [0]*(2*d)+[1]
            observed = [evaluate(operator(f, mode), k, p) for k in range(a+1)]
            values = [pow(k, 2*d, p) for k in range(a+1)]
            if mode == 0:
                predicted = matvec(jacobi, values, p)
            else:
                v = [q*z % p for q, z in zip(Rvalues, values)]
                predicted = [q*pow(z, -1, p) % p for q, z in zip(matvec(jacobi, v, p), Rvalues)]
            check(observed == predicted)

    def basis(mode, length):
        rows, product_lc = [], 1
        for d in range(length):
            f = [0]*(2*(d % 4))+[1]
            for _ in range(d//4):
                f = operator(f, mode)
            check(len(f) == 2*d+1 and f[-1] != 0)
            product_lc = product_lc*f[-1] % p
            rows.append([evaluate(f, k, p) for k in range(a+1)])
        return rows, product_lc

    T, dt = basis(0, r)
    Q, dq = basis(4, 3*r)
    tm = [[pow(k, 2*d, p) for k in range(a+1)] for d in range(r)]
    qm = [[pow(k, 2*d, p) for k in range(a+1)] for d in range(3*r)]

    def gram(trows, qrows):
        vectors = [(v, [0]*(a+1)) for v in trows]
        vectors += [([0]*(a+1), v) for v in qrows]
        matrix = []
        for t, q in vectors:
            row = []
            for v, z in vectors:
                row.append(sum(weights[k]*(t[k]*v[k]+alpha[k]*Rvalues[k]*(t[k]*z[k]+q[k]*v[k])
                                          +Rvalues[k]**2*q[k]*z[k]) for k in range(a+1)) % p)
            matrix.append(row)
        return matrix

    scalar = lambda rows: [[sum(weights[k]*x[k]*y[k] for k in range(a+1)) % p for y in rows] for x in rows]
    check(determinant(scalar(T), p) == dt*dt*determinant(scalar(tm), p) % p)
    check(determinant(gram(T, Q), p) == (dt*dq)**2*determinant(gram(tm, qm), p) % p)

    blocks = []
    for start, end in ((0, r), (r, a+1)):
        j = [row[start:end] for row in jacobi[start:end]]
        m, w = len(j), weights[start:end]
        prefixes = [[1]]
        for i in range(m):
            z = mul([-j[i][i], 1], prefixes[-1], p)
            if i:
                z = add(z, scale(prefixes[-2], -j[i-1][i]*j[i][i-1], p), p)
            check(len(z) == i+2 and z[-1] == 1)
            prefixes.append(z)
            if i:
                x, y = z[:], prefixes[-2][:]
                while y != [0]:
                    x, y = y, remainder(x, y, p)
                check(len(x) == 1 and x[0] != 0)
        endpoint = [1]+[0]*(m-1)
        moments = []
        v = endpoint[:]
        for _ in range(2*m):
            moments.append(w[0]*v[0] % p)
            v = matvec(j, v, p)
        for length in range(1, m+1):
            expected = pow(w[0], length, p)
            for h in range(1, length):
                expected = expected*pow(j[h-1][h]*j[h][h-1], length-h, p) % p
            hankel = [[moments[i+k] for k in range(length)] for i in range(length)]
            check(expected != 0 and determinant(hankel, p) == expected)
        for z in range(5):
            matrix = [[((z if i == k else 0)-j[i][k]) % p for k in range(m)] for i in range(m)]
            check(determinant(matrix, p) == evaluate(prefixes[-1], z, p))
        blocks.append({"length": m, "characteristic_polynomial": prefixes[-1],
                       "all_endpoint_hankel_norms_units": True,
                       "characteristic_may_have_multiple_roots": True})
    return {"r": r, "p": p, "checks": checks, "critical_T_length": r,
            "critical_Q_length": 3*r, "T_basis_determinant": dt, "Q_basis_determinant": dq,
            "blocks": blocks, "actual_target_nonzero_not_asserted": True}


cases = [run(r) for r in (1, 2, 4)]
result = {"status": "PASS", "execution_count": 1,
          "scope": "Boundary-preserving scalar/matrix operator, degree-leading units, actual Krylov determinant scaling, continuants and endpoint norms only; three already examined scales.",
          "old_or_peer_execute_import_rerun": 0,
          "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "cases": cases,
          "total_checks": sum(c["checks"] for c in cases),
          "not_proved_by_program": ["all-scale operator lemmas", "all-r or infinite simultaneous target units",
                                    "new arithmetic cost", "new special-value theorem"]}
TARGET.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "cases": len(cases),
                  "total_checks": result["total_checks"]}))
