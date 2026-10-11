"""Exact finite identities for the bridge note; no parameter search."""
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import json

import sympy as s


def cofactor_frame(m, scales, lower, A, B):
    C = s.Matrix.vstack(s.diag(*scales), s.Matrix(lower) * s.diag(*scales))
    A, B = s.Matrix(A), s.Matrix(B)
    M = A.row_join(B).row_join(C)
    minors = [int(C[list(I), :].det()) for I in combinations(range(m + 2), m)]
    g = reduce(gcd, (abs(v) for v in minors))
    d = int(C[:m, :].det())
    U = []
    for k in (m, m + 1):
        row = [s.Integer(0)] * (m + 2)
        top = -C[k, :] * C[:m, :].adjugate() / g
        for j in range(m):
            row[j] = top[j]
        row[k] = s.Integer(d) / g
        assert all(v.q == 1 for v in row)
        U.append(row)
    U = s.Matrix(U)
    T = U * A.row_join(B)
    assert U * C == s.zeros(2, m)
    assert M.det() != 0
    assert T.det() == s.Rational(d, g * g) * M.det()
    # Arbitrary invertible rational change of nuisance-column basis preserves ratio.
    R = s.eye(m)
    R[0, 0] = 3
    if m > 1:
        R[0, 1] = 1
    C2 = C * R
    minors2 = [int(C2[list(I), :].det()) for I in combinations(range(m + 2), m)]
    g2 = reduce(gcd, (abs(v) for v in minors2))
    assert s.Rational(max(map(abs, minors)), g) == s.Rational(max(map(abs, minors2)), g2)
    return {
        "m": m, "C": [list(map(int, C.row(i))) for i in range(m + 2)],
        "A": list(map(int, A)), "B": list(map(int, B)),
        "g": g, "max_minor": max(map(abs, minors)), "d": d,
        "U": [list(map(int, U.row(i))) for i in range(2)],
        "target_coefficients": [list(map(int, T.row(i))) for i in range(2)],
        "det_M": int(M.det()), "det_target": int(T.det()),
        "det_identity": True, "basis_change_ratio_identity": True,
    }


def cyclic_test(label, seed, connection):
    x, X = s.symbols("x X")
    q = len(seed)
    p = s.Matrix([seed])
    rows = []
    for _ in range(q):
        rows.append(list(p))
        p = p.applyfunc(lambda t: x * s.diff(t, x)) + p * connection
    D = s.factor(s.Matrix(rows).det())
    num, den = s.fraction(s.cancel(D))
    assert not den.has(X)  # No target-parameter denominators in clearing.
    px = s.Poly(num, x)
    coeff = px.all_coeffs()
    G = s.Poly(reduce(s.gcd, coeff), X).monic().as_expr()
    return {"label": label, "q": q, "cyclic_determinant": str(D),
            "clearing_denominator": str(den), "exception_polynomial": str(G)}


def main():
    x, X = s.symbols("x X")
    frames = [
        cofactor_frame(1, [2], [[2], [3]], [1, 5, 7], [2, 9, 13]),
        cofactor_frame(2, [2, 6], [[2, 2], [3, 5]], [1, 3, 10, 22], [2, 4, 15, 28]),
        cofactor_frame(3, [2, 6, 10], [[1, 2, 3], [3, 1, 2]],
                       [1, 3, 5, 23, 20], [2, 4, 6, 33, 25]),
    ]
    r = x / (1 - x)
    A2 = s.Matrix([[0, 0], [r, 0]])  # basis (1, Li_1)
    A3 = s.Matrix([[0, 0, 0], [r, 0, 0], [0, 1, 0]])
    cyclic = [
        cyclic_test("Li1_minus_X", [-X, 1], A2),
        cyclic_test("1_plus_(1-X)_Li1", [1, 1 - X], A2),
        cyclic_test("Li2_minus_X_Li1", [0, -X, 1], A3),
    ]
    assert cyclic[0]["exception_polynomial"] == "1"
    assert s.factor(s.sympify(cyclic[1]["exception_polynomial"])) == (X - 1)**2
    assert cyclic[2]["exception_polynomial"] == "1"
    out = {"status": "exact_identities_verified", "frames": frames, "cyclic": cyclic,
           "scope": "Fixed exact examples, not a search or a zeta irrationality proof."}
    dest = Path(__file__).with_suffix(".json")
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": out["status"], "frame_m": [1, 2, 3], "cyclic_tests": 3,
                      "output": str(dest)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
