"""Exact, bounded certificates for the actual trigamma/Lerch projection report.

No numerical evaluation of zeta, Dirichlet L-values, or trigamma is used.
The independent numerical-period input is CDT Theorem A, not this script.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from functools import reduce
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def content(values):
    return reduce(math.gcd, (abs(int(v)) for v in values), 0)


def lcm(values):
    return reduce(math.lcm, (int(v) for v in values), 1)


def row(n):
    r = (n - 1) % 6 + 1
    q = (n - r) // 6
    aa = [12, 4, 3, 4, 12, 1]
    bb = [5, 1, 0, -1, -5, 0]
    cc = -36 * sum((sp.Rational(1, (r + 6 * k) ** 2) for k in range(q)), sp.S.Zero)
    return sp.Matrix([cc, aa[r - 1], sp.Rational(9, 2) * bb[r - 1]])


def scalar_prefix(m, coeffs, N):
    D = lcm(range(1, m * (N + 1) + 1)) ** 2
    vals = [sum((sp.Rational(c, (m * n + a) ** 2)
                 for a, c in coeffs.items()), sp.S.Zero) for n in range(N + 1)]
    ints = [int(D * v) for v in vals]
    h = content([D] + ints)
    exact = lcm([v.q for v in vals])
    assert D // h == exact
    return {"m": m, "coeffs": coeffs, "N": N, "safe_D": str(D),
            "integer_content_including_D": str(h), "exact_prefix_denominator": str(exact),
            "coefficients": [str(v) for v in vals]}


def cyclic(m, coeffs):
    aa = sorted(coeffs)
    t = len(aa)
    U = sp.Matrix([[v for a in aa for v in (
        coeffs[a] * (-sp.Rational(a, m)) ** k,
        sp.Rational(coeffs[a] * k, m) * (-sp.Rational(a, m)) ** (k - 1) if k else 0
    )] for k in range(2 * t)])
    expected = sp.prod(sp.Rational(coeffs[a] ** 2, m) for a in aa)
    expected *= sp.prod((sp.Rational(a - b, m)) ** 4 for a, b in itertools.combinations(aa, 2))
    assert U.det() == expected != 0
    n = sp.Symbol("n")
    S = sum(coeffs[a] * sp.prod((m * n + b) ** 2 for b in aa if b != a) for a in aa)
    for a in aa:
        assert sp.expand(S).subs(n, -sp.Rational(a, m)) == coeffs[a] * sp.prod((b-a)**2 for b in aa if b != a)
    return {"m": m, "coeffs": coeffs, "rank": 2 * t + 1,
            "confluent_jet_determinant": str(U.det()), "forcing_polynomial": str(sp.expand(S))}


def main():
    a = sp.Matrix([[12, 4, 3, 4, 12, 1], [5, 1, 0, -1, -5, 0]])
    M = sp.diag(2, 9) * a
    assert abs(a[:, [5, 1]].det()) == 1
    snf = smith_normal_form(M, domain=ZZ)
    assert abs(snf[0, 0]) == 1 and abs(snf[1, 1]) == 18
    K = sp.Matrix([[1, 0, 0, 0], [-5, 0, 1, 5], [0, 1, 0, 0],
                   [0, 0, 1, 0], [0, 0, 0, 1], [8, -3, -8, -32]])
    assert a * K == sp.zeros(2, 4)
    # Together with the two image lifts, K is an integral basis of Z^6.
    lifts = sp.zeros(6, 2)
    lifts[5, 0] = 1
    lifts[1, 1] = 1
    lifts[5, 1] = -4
    assert abs(K.row_join(lifts).det()) == 1
    assert a * lifts == sp.eye(2)
    # Simultaneous pure-L endpoint and deletion of the x=1 monodromy.
    U_pure = a[:1, :].col_join(sp.ones(1, 6))
    K_pure = sp.Matrix([[0, 1, 0, 0], [1, -5, 1, 5], [0, 2, -3, -13],
                        [-1, 0, 1, 0], [0, 0, 0, 1], [0, 2, 1, 7]])
    pure_lifts = sp.Matrix([[0, 0], [1, -1], [-1, 1], [0, 0], [0, 0], [0, 1]])
    assert U_pure*K_pure == sp.zeros(2, 4)
    assert U_pure*pure_lifts == sp.eye(2)
    assert abs(K_pure.row_join(pure_lifts).det()) == 1
    assert a[1:2, :]*K_pure == sp.Matrix([[2, 0, 0, 0]])

    x = sp.Symbol("x")
    G0 = sp.cancel((x-x**2)/(1-x**3))
    assert G0 == x/(x**2+x+1)
    periodic_cyclic = []
    for s in [1, 2, 3]:
        J = sp.zeros(s+1)
        for k in range(s):
            J[k, s-k] = 1
        J[s, 0] = G0
        expected = (-1)**(s*(s+1)//2)*G0
        assert sp.factor(J.det()-expected) == 0
        periodic_cyclic.append({"weight": s, "rank": s+1, "jet_determinant": str(expected)})
    N_character = 12
    D_character = lcm(range(1, N_character+1))**2
    character_vals = [sp.Rational((0, 1, -1)[n % 3], n**2) for n in range(1, N_character+1)]
    h_character = content([D_character]+[int(D_character*v) for v in character_vals])
    L_without_3 = lcm(range(1, N_character+1))
    while L_without_3 % 3 == 0:
        L_without_3 //= 3
    assert D_character//h_character == L_without_3**2

    assert row(7) - row(1) == sp.Matrix([-36, 0, 0])
    assert 49 * row(13) - 49 * row(1) == sp.Matrix([-1800, 0, 0])
    T = sp.Matrix.hstack(sp.Matrix([1, 0, 0]), row(1), row(2), row(7))
    assert T.rank() == 3
    assert T * sp.Matrix([36, -1, 0, 1]) == sp.zeros(3, 1)
    primitive_rows = []
    for n in [1, 2, 7, 13]:
        v = row(n)
        D = lcm([x.q for x in v])
        ints = [int(D*x) for x in v]
        h = content(ints)
        primitive_rows.append({"n": n, "period_row_C_A_B": [str(x) for x in v],
                               "D": D, "full_content": h,
                               "primitive_row": [x//h for x in ints]})

    # Full joint coefficient-congruence lattice, not separate row gcds.
    m, N = 3, 2
    D = lcm(range(1, m*(N+1)+1))**2
    B = sp.Matrix([[D*sp.Rational(1, (m*n+a0)**2) for n in range(N+1)] for a0 in [1, 3]])
    A = B.T.row_join(D*sp.eye(N+1))
    S = smith_normal_form(A, domain=ZZ)
    ds = [abs(int(S[j, j])) for j in range(N+1)]
    minors = [A[:, cols].det() for cols in itertools.combinations(range(A.cols), A.rows)]
    assert content(minors) == math.prod(ds)
    index = D**(N+1)//math.prod(ds)
    lattice_basis = sp.Matrix([[784, -196], [0, 81]])
    assert abs(lattice_basis.det()) == index == 63504
    assert all(x.q == 1 for x in lattice_basis.T*B/D)
    separate_row_product = math.prod(lcm([sp.Rational(1, (m*n+a0)**2).q
                                        for n in range(N+1)]) for a0 in [1, 3])
    assert separate_row_product == 4*index

    # General coarse staircase rate and its exact comparison with the rank-3 case.
    m_symbol = sp.Symbol("m", integer=True, positive=True)
    num = 9*(7*m_symbol**3+6*m_symbol**2)-13*(2*m_symbol+1)**2
    assert sp.expand(num-(m_symbol-1)*(63*m_symbol**2+65*m_symbol+13)) == 0
    # log 2 = 2 atanh(1/3); bound the tail by a geometric series.
    partial = 2*sum((sp.Rational(1, (2*j+1)*3**(2*j+1)) for j in range(8)), sp.S.Zero)
    tail = sp.Rational(2, 17*3**17)/(1-sp.Rational(1, 9))
    assert partial+tail < sp.Rational(7, 10)
    assert sp.Rational(7, 5) < sp.Rational(13, 9)
    cdt_tau = sp.Rational(191, 49)+sp.Rational(27, 80)
    assert cdt_tau == sp.Rational(16603, 3920)

    # Fixed selected prime certificates illustrate the proved all-prime shift lemma.
    prime_shift = []
    for p in [5, 7, 11]:
        C = row(p+6)[0]
        assert int(C.p) % p != 0 and int(C.q) % p**2 == 0 and int(C.q) % p**3 != 0
        prime_shift.append({"p": p, "shift_n": p+6, "rational_C": str(C), "valuation": -2})

    result = {
        "scope": "Exact algebraic certificates only; period independence uses CDT Theorem A.",
        "checks_passed": True,
        "base_image_matrix_for_2_trigamma": [[int(v) for v in M.row(j)] for j in range(2)],
        "smith_invariant_factors": [1, 18],
        "saturated_kernel_basis": [[int(v) for v in K.row(j)] for j in range(6)],
        "unimodular_completion_determinant": int(K.row_join(lifts).det()),
        "pure_L_and_mean_zero_kernel_basis": [[int(v) for v in K_pure.row(j)] for j in range(6)],
        "pure_L_mean_zero_image_b": [2, 0, 0, 0],
        "pure_L_mean_zero_unimodular_completion": int(K_pure.row_join(pure_lifts).det()),
        "periodic_character_G0": str(G0),
        "periodic_weight_cyclic_certificates": periodic_cyclic,
        "character_prefix": {"N": N_character, "safe_D": str(D_character),
                              "full_content_including_D": str(h_character),
                              "exact_denominator": str(D_character//h_character)},
        "primitive_period_rows": primitive_rows,
        "joint_prefix_lattice": {"m": m, "N": N, "D": str(D), "smith_factors": ds,
                                  "residue_rows": [1, 3], "index_in_Z2": str(index),
                                  "integer_filter_basis_columns": [[int(v) for v in lattice_basis.row(j)] for j in range(2)],
                                  "separate_row_denominator_product": str(separate_row_product)},
        "scalar_prefix_models": [scalar_prefix(3, {1: 1, 2: -1}, 3),
                                 scalar_prefix(3, {1: 1, 3: -4}, 3),
                                 scalar_prefix(6, {1: 1, 2: -5, 6: 8}, 2)],
        "cyclic_rank_certificates": [cyclic(3, {1: 1, 2: -1}),
                                      cyclic(6, {1: 1, 2: -5, 6: 8})],
        "coarse_rate_at_m1": "13/9", "coarse_rate_at_m6": "1728/169",
        "log2_rational_upper_bound": str(partial+tail),
        "CDT13_exact_tau": str(cdt_tau),
        "prime_shift_certificates": prime_shift,
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"checks_passed": True, "output": str(out), "sha256": hashlib.sha256(out.read_bytes()).hexdigest()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
