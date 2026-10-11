"""Saturated hyperplanes with local radical constraints for the zeta(7) pencil.

Selection uses exact Gram LLL for a rational approximation to zeta(7).
All reported polynomial contents are exact; final values are Arb certified.
No LLL output is used as a proof of an asymptotic existence statement.
"""
import argparse
import json
from functools import reduce
from math import gcd, lcm
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, fmpz_mat, nmod_mat, arb, ctx
from joint_exact import entries, binomial_matrices, content, evaluate_primitive_ball
from mixed_subspaces import determinant_matrices
from sympy import primerange


def integer_pencil(K, N, m):
    aa, bb = entries(K, [(N, 8)], m)
    A, B = binomial_matrices(K, [(N, 8)], m, aa, bb)
    g = content(fmpq_poly(list(A.entries())+list(B.entries())))
    A, B = A/g, B/g
    assert all(x.q == 1 for x in list(A.entries())+list(B.entries()))
    return A, B, g


def adjugate_coefficients(A, B):
    m = A.nrows(); a = A.det()
    assert a
    det = determinant_matrices(A, B)
    Ai = A.inv(); C = -Ai*B; last = Ai
    coefficients = [last*a]
    for k in range(1, m):
        last = C*last+Ai*(det[k]/a)
        coefficients.append(last*a)
    assert all(H == H.transpose() for H in coefficients)
    assert all(x.q == 1 for H in coefficients for x in H.entries())
    # Independent adjugate evaluations, including beyond the coefficient range.
    for x in [0, 1, m+2]:
        H = fmpq_mat(m, m)
        for coeff in reversed(coefficients):
            H = H*x+coeff
        assert (A+B*x)*H == fmpq_mat([[det(x) if i == j else 0 for j in range(m)] for i in range(m)])
    return det, coefficients


def rational_metric(A, B):
    m = A.nrows()
    bits = max(abs(int(x.p)).bit_length() for x in list(A.entries())+list(B.entries()))+64*m+256
    with ctx.workprec(bits+80):
        q = 1 << bits
        p = (arb(7).zeta()*q).floor().unique_fmpz()
        assert p is not None
    G = fmpz_mat(m, m, [int(q*A[i,j]+p*B[i,j]) for i in range(m) for j in range(m)])
    cp = G.charpoly()
    # Real eigenvalues (symmetry) plus alternating elementary-symmetric signs
    # certify strict positive definiteness of this rational selection metric.
    assert G == G.transpose() and all((-1)**(m-i)*cp[i] > 0 for i in range(m))
    H = G.inv()*G.det()
    g = reduce(gcd, (abs(int(x.p)) for x in H.entries()), 0)
    dual = fmpz_mat(m, m, [int(x/g) for x in H.entries()])
    return dual, bits


def radical(A, B, p):
    m = A.nrows()
    stack = nmod_mat(2*m, m, [int(x) % p for x in list(A.entries())+list(B.entries())], p)
    R, d = stack.nullspace()
    R = nmod_mat(m, d, [int(R[i,j]) for i in range(m) for j in range(d)], p)
    assert not stack*R
    return R, d


def congruence_kernel(C, p):
    """Row basis of {x in Z^m: C*x^T=0 mod p}."""
    R, rank = C.rref(); m = C.ncols()
    pivots = [next(j for j in range(m) if R[i,j]) for i in range(rank)]
    free = [j for j in range(m) if j not in pivots]
    rows = []
    for j in free:
        v = [0]*m; v[j] = 1
        for i, col in enumerate(pivots):
            v[col] = -int(R[i,j])
        rows.append(v)
    for col in pivots:
        v = [0]*m; v[col] = p; rows.append(v)
    T = fmpz_mat(rows)
    assert abs(T.det()) == p**rank
    assert not C*nmod_mat(m, m, [int(x) % p for x in T.transpose().entries()], p)
    return T


def normal_lattice(m, conditions):
    L = fmpz_mat([[int(i == j) for j in range(m)] for i in range(m)])
    for p, R in conditions:
        C = R.transpose()*nmod_mat(m, m, [int(x) % p for x in L.transpose().entries()], p)
        L = (congruence_kernel(C, p)*L).hnf()
    assert abs(L.det()) == reduce(lambda a, pr: a*pr[0]**pr[1].ncols(), conditions, 1)
    return L


def saturated_kernel(u):
    m = len(u)
    H, T = fmpz_mat(m, 1, u).hnf(transform=True)
    assert H[0,0] == 1 and all(not H[i,0] for i in range(1,m)) and abs(T.det()) == 1
    C = fmpz_mat(m-1, m, [T[i,j] for i in range(1,m) for j in range(m)])
    C = C.lll()
    assert not C*fmpz_mat(m, 1, u)
    # All maximal minors recover the primitive normal (up to global sign).
    minors = [(-1)**j*fmpz_mat(m-1, m-1,
              [C[i,k] for i in range(m-1) for k in range(m) if k != j]).det() for j in range(m)]
    assert minors == u or minors == [-x for x in u]
    return fmpq_mat(C)


def valuation(n, p):
    n = abs(int(n)); assert n
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v


def normal_result(u, A, B, coefficients, K, label, conditions, direct=False,
                  condition_kind='ambient_radical', uniform_content=1):
    u = list(map(int, u)); divisor = reduce(gcd, map(abs, u), 0)
    u = [x//divisor for x in u]
    if next(x for x in u if x) < 0:
        u = [-x for x in u]
    m = len(u); U = fmpq_mat(1, m, u)
    P = fmpq_poly([(U*H*U.transpose())[0,0] for H in coefficients])
    ct, value, bits = evaluate_primitive_ball(P)
    assert ct.q == 1
    C = saturated_kernel(u)
    if direct:
        assert determinant_matrices(C*A*C.transpose(), C*B*C.transpose()) == P
    local = []
    for p, R in conditions:
        up = nmod_mat(m, 1, [x % p for x in u], p)
        preserved = not R.transpose()*up
        rank = nmod_mat(m-1, m, [int(x) % p for x in C.entries()], p).rank()
        assert rank == m-1
        v = valuation(ct.p, p)
        if preserved:
            if condition_kind=='ambient_radical':
                assert v >= R.ncols()
            else:
                assert int(ct.p) % (uniform_content*p) == 0
        local.append(dict(p=p, constraint_rank=R.ncols(), condition_kind=condition_kind,
                          preserved_after_saturation=preserved,
                          content_valuation=v, reduction_rank=rank))
    with ctx.workprec(max(bits, 160)):
        raw = value+arb(ct).log()
        return dict(label=label, normal=u, removed_normal_gcd=divisor,
                    height_bits=max(abs(x).bit_length() for x in u), degree=P.degree(),
                    score=float((value/K**2).mid()), score_ball=(value/K**2).str(30),
                    raw_log_ball=raw.str(30), content=str(ct), local=local,
                    direct_adjugate_check=direct, poly=[str(x) for x in P])


def adjugate_conditions(coefficients, m, K):
    g=reduce(gcd,(abs(int(x.p)) for H in coefficients for x in H.entries()),0)
    candidates=[]; diagnostics=[]
    for p in primerange(3,2*K+5):
        S=nmod_mat(m*len(coefficients),m,[int(x/g)%p for H in coefficients for x in H.entries()],p)
        row,rank=S.rref()
        diagnostics.append(dict(p=p,constraint_rank=rank))
        if 0<rank<m-1:
            R=nmod_mat(m,rank,[int(row[i,j]) for j in range(m) for i in range(rank)],p)
            candidates.append((p,R))
    candidates.sort(key=lambda pr:(pr[1].ncols(),-pr[0]))
    return g,candidates,diagnostics


def primitive_admissible(u, conditions):
    divisor = reduce(gcd, (abs(int(x)) for x in u), 0)
    if not divisor:
        return False
    return all(not R.transpose()*nmod_mat(len(u), 1, [int(x)//divisor % p for x in u], p)
               for p, R in conditions)


def run(K, N, m):
    A, B, g = integer_pencil(K, N, m)
    det, coefficients = adjugate_coefficients(A, B)
    dual, metric_bits = rational_metric(A, B)
    cd, ld, _ = evaluate_primitive_ball(det)
    adj_content = reduce(gcd, (abs(int(x.p)) for H in coefficients for x in H.entries()), 0)
    assert int(cd.p)**(m-1) % adj_content**m == 0
    primes = []
    all_radicals = []
    for p in primerange(3, 2*K+5):
        R, d = radical(A, B, p)
        if d:
            all_radicals.append(dict(p=p, dimension=d))
        if 0 < d < m-1:
            primes.append((p, R))
    primes.sort(key=lambda pr: (pr[1].ncols(), -pr[0]))
    selected = primes[:3]
    jobs = [('unconstrained', [])]
    jobs += [(f'radical_{p}', [(p, R)]) for p, R in selected]
    if len(selected) >= 2:
        jobs.append(('joint_radicals', selected[:2]))
    rows = [normal_result([0]*(m-1)+[1], A, B, coefficients, K, 'low_degree_baseline', [], True)]
    for label, conditions in jobs:
        L = normal_lattice(m, conditions)
        metric = L*dual*L.transpose()
        reduced, T = metric.lll(rep='gram', gram='exact', transform=True)
        assert reduced == T*metric*T.transpose() and abs(T.det()) == 1
        normals = T*L
        order = sorted(range(m), key=lambda i: reduced[i,i])[:3]
        for j, i in enumerate(order):
            row = normal_result([normals[i,k] for k in range(m)], A, B, coefficients,
                                K, f'{label}_{j}', conditions, j == 0)
            row.update(lattice_index=str(abs(L.det())), selection_metric_bits=metric_bits)
            rows.append(row)
        if conditions:
            candidates = [(int(reduced[i,i]), [int(normals[i,k]) for k in range(m)]) for i in range(m)]
            # Primitive residue classes form a punctured congruence set, not a
            # lattice. Also try two-row combinations if the shortest lattice
            # basis rows become inadmissible after removing their integer gcd.
            for i in range(m):
                for j in range(i+1, m):
                    for sign in [-1, 1]:
                        candidates.append((int(reduced[i,i]+reduced[j,j]+2*sign*reduced[i,j]),
                                           [int(normals[i,k]+sign*normals[j,k]) for k in range(m)]))
            candidates.sort(key=lambda pair: pair[0])
            good = []; seen = set()
            for _, u in candidates:
                if not primitive_admissible(u, conditions):
                    continue
                divisor = reduce(gcd, map(abs, u), 0)
                v = tuple(x//divisor for x in u)
                if v in seen or tuple(-x for x in v) in seen:
                    continue
                seen.add(v); good.append(u)
                if len(good) == 3:
                    break
            assert good, 'No admissible primitive residue class found in candidate pool.'
            for j, u in enumerate(good):
                row = normal_result(u, A, B, coefficients, K, f'{label}_admissible_{j}', conditions, j == 0)
                assert all(x['preserved_after_saturation'] for x in row['local'])
                row.update(lattice_index=str(abs(L.det())), selection_metric_bits=metric_bits)
                rows.append(row)
        print(json.dumps(dict(K=K, m=m, job=label, best=min(r['score'] for r in rows if r['label'].startswith(label)))), flush=True)
    with ctx.workprec(160):
        ambient_score = float((ld/K**2).mid()); ambient_ball = (ld/K**2).str(30)
    return dict(K=K, N=N, m=m, h=m-1, ambient_score=ambient_score,
                ambient_score_ball=ambient_ball, ambient_content=str(cd),
                adjugate_content=str(adj_content), integer_entry_scale=str(g),
                radicals=all_radicals, rows=rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--K', type=int, default=12)
    parser.add_argument('--N', type=int, default=1)
    parser.add_argument('--m', type=int)
    args = parser.parse_args()
    data = run(args.K, args.N, args.m or args.K-args.N+1)
    path = Path(__file__).with_name(f'arithmetic_subspaces_K{args.K}_N{args.N}_m{data["m"]}.json')
    path.write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k not in ['rows','ambient_content','adjugate_content','integer_entry_scale']}))
    print('baseline', data['rows'][0]['score'], 'best', min(r['score'] for r in data['rows']))
