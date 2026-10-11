"""Root-evaluation congruence lattices in the full square-integer-valued space.

Candidate selection uses high-precision midpoints. Contents are exact; final
determinant values use Arb. A sampled gcd is explicitly an upper bound until
the entire total-degree Newton simplex has been evaluated.
"""
import argparse
import itertools
import json
import math
import time
from pathlib import Path

import mpmath as mp
from flint import fmpq, fmpq_poly, fmpz_mat, nmod_mat, arb, ctx
from sympy import factorint

from arithmetic_subspaces import congruence_kernel
from block_pencil_fixed_divisor import gcdq
from growing_integer_space import basis, reduced_round, trace_metric
from joint_exact import Dcache, entries_from_polynomial, determinant, content, evaluate_primitive_ball

FOLDER = Path(__file__).parent


class Family:
    def __init__(self, K=24, N=1, L=3):
        self.K, self.N, self.L = K, N, L
        self.h = K-N-L
        self.Q0 = fmpq_poly(Dcache(N+L)//Dcache(N))
        self.ds = [basis(i)*math.factorial(L)**2 for i in range(L)]
        self.aa, self.bb = entries_from_polynomial(K, Dcache(N)**8, K-N)
        self.E = [[int(basis(i)(-j*j)) for i in range(L)] for j in range(N+1, N+L+1)]

    def polynomial(self, u):
        return self.Q0+sum((x*d for x, d in zip(u, self.ds)), fmpq_poly([]))

    def entries(self, Q):
        c = list(Q**2)
        a = [sum((x*self.aa[e+k] for k, x in enumerate(c)), fmpq(0)) for e in range(2*self.h-1)]
        b = [sum((x*self.bb[e+k] for k, x in enumerate(c)), fmpq(0)) for e in range(2*self.h-1)]
        return a, b

    def det(self, u):
        a, b = self.entries(self.polynomial(u))
        return determinant(a, b, self.h)

    def score(self, u):
        Q = self.polynomial(u)
        P = self.det(u)
        ct, lv, bits = evaluate_primitive_ball(P)
        with ctx.workprec(160):
            score = lv/self.K**2
        return dict(parameters=list(map(str, u)), Q=list(map(str, Q)), content=str(ct),
                    score=float(score.mid()), score_ball=score.str(30), precision_bits=bits)


def root_lattice(E, moduli):
    """Full-rank row basis B of E*u=0 modulo the respective row moduli."""
    L = len(E[0])
    B = fmpz_mat([[int(i == j) for j in range(L)] for i in range(L)])
    for row, modulus in zip(E, moduli):
        for p, exponent in factorint(modulus).items():
            p = int(p)
            for e in range(int(exponent)):
                vals = [sum(int(B[i,j])*row[j] for j in range(L)) for i in range(L)]
                assert all(x % p**e == 0 for x in vals)
                C = nmod_mat(1, L, [x//p**e % p for x in vals], p)
                B = (congruence_kernel(C, p)*B).hnf()
    assert all(sum(int(B[i,j])*row[j] for j in range(L)) % modulus == 0
               for row, modulus in zip(E, moduli) for i in range(L))
    return B


def metric(K, N, L):
    path = FOLDER/f'growing_trace_certificate_K{K}.json'
    if path.exists():
        data = json.loads(path.read_text())
        assert data['N'] == N and data['L'] == L
        mp.mp.dps = 230
        A = mp.matrix([[mp.mpf(v) for v in row] for row in data['trace_metric_A_midpoint']])
        b = mp.matrix([mp.mpf(v) for v in data['trace_metric_b_midpoint']])
        return A, b
    _, _, A, b, _, _ = trace_metric(K,N,L)
    return A, b


def lattice_round(B, A, b, h):
    L = B.nrows()
    bm = mp.matrix([[int(B[i,j]) for j in range(L)] for i in range(L)])
    center = mp.lu_solve(A, -b)
    z, T, _ = reduced_round(bm*A*bm.T, mp.lu_solve(bm.T, center))
    u = [sum(int(B[i,j])*z[i] for i in range(L)) for j in range(L)]
    U = fmpz_mat(T)*B
    um = mp.matrix([[int(U[i,j]) for j in range(L)] for i in range(L)])
    gram = um*A*um.T
    epsilon = sum(gram[i,i] for i in range(L))/4
    minimum = h+(b.T*center)[0]
    return u, U, minimum, epsilon


def matrix_rows(B):
    return [[int(B[i,j]) for j in range(B.ncols())] for i in range(B.nrows())]


def scan(K, N, L, choices):
    fam = Family(K,N,L); A,b = metric(K,N,L)
    rows=[];cache={};seen=set();start=time.time()
    path=FOLDER/f'directional_congruence_K{K}.json'
    for moduli in itertools.product(choices, repeat=L):
        B=root_lattice(fam.E,moduli)
        key=tuple(int(x) for x in B.entries())
        if key in seen:continue
        seen.add(key)
        u,U,minimum,epsilon=lattice_round(B,A,b,fam.h)
        if tuple(u) not in cache:cache[tuple(u)]=fam.score(u)
        r=dict(moduli=list(moduli),index=str(abs(int(B.det()))),basis=matrix_rows(B),
               reduced_basis=matrix_rows(U),minimum_midpoint=mp.nstr(minimum,35),
               rounding_midpoint=mp.nstr(epsilon,35),trace_upper_midpoint=mp.nstr(minimum+epsilon,35),
               candidate=cache[tuple(u)])
        rows.append(r)
        if len(rows)%20==0:
            print(json.dumps(dict(lattices=len(rows),unique_points=len(cache),elapsed=time.time()-start,
                                  best=min(v['score'] for v in cache.values()))),flush=True)
    result=dict(K=K,N=N,L=L,h=fam.h,evaluation_matrix=fam.E,choices=choices,rows=rows,
                unique_candidates=len(cache),selection_only='Trace quantities here are midpoints, not certificates.')
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(path=str(path),lattices=len(rows),unique_points=len(cache),elapsed=time.time()-start,
                         best=sorted(cache.values(),key=lambda v:v['score'])[:3])),flush=True)


def simplex(L,d):
    if L==1:
        for x in range(d+1):yield (x,)
    else:
        for x in range(d+1):
            for tail in simplex(L-1,d-x):yield (x,)+tail


def fixed_divisor(K,N,L,moduli,tag):
    fam=Family(K,N,L);B=root_lattice(fam.E,moduli);d=2*fam.h
    path=FOLDER/f'directional_fixed_divisor_{tag}.json'
    start=time.time();G=fmpq(0);changes=[];count=0
    for z in simplex(L,d):
        u=[sum(int(B[i,j])*z[i] for i in range(L)) for j in range(L)]
        ct=content(fam.det(u));g=gcdq([G,ct])
        if g!=G:changes.append(dict(z=list(z),content=str(ct),gcd=str(g)));G=g
        count+=1
        if count%200==0:print(json.dumps(dict(tag=tag,count=count,total=math.comb(d+L,L),elapsed=time.time()-start,changes=len(changes))),flush=True)
    assert count==math.comb(d+L,L)
    result=dict(K=K,N=N,L=L,h=fam.h,moduli=moduli,basis=matrix_rows(B),degree_bound=d,
                points=count,fixed_divisor=str(G),gcd_changes=changes,elapsed=time.time()-start,
                certificate='Complete total-degree Newton simplex: exact uniform divisor on the entire row lattice.')
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(path=str(path),points=count,elapsed=time.time()-start)),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1);p.add_argument('--L',type=int,default=3)
    p.add_argument('--choices',default='1,6,30,210,2310');p.add_argument('--fixed');p.add_argument('--tag',default='trial');p.add_argument('--benchmark',action='store_true')
    a=p.parse_args()
    if a.benchmark:
        fam=Family(a.K,a.N,a.L);start=time.time()
        for j in range(10):content(fam.det([j]*(a.L)))
        print(json.dumps(dict(seconds_per_determinant=(time.time()-start)/10)))
    elif a.fixed:fixed_divisor(a.K,a.N,a.L,list(map(int,a.fixed.split(','))),a.tag)
    else:scan(a.K,a.N,a.L,list(map(int,a.choices.split(','))))
