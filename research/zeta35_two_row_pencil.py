"""Exact Gr(2,4) determinant pencil after a fixed 65-dimensional head.

Tail basis: psi_65, psi_66, psi_67, 83*psi_68. The six Pluecker
coordinates are ordered 01,02,03,12,13,23. All rational planes are covered.
"""
import itertools
import json
import math
import sys
import time
from pathlib import Path
from flint import fmpq as Q, fmpq_mat as Mat, fmpq_poly as Poly, fmpz_mat as ZMat, arb, arb_poly, arb_mat, ctx
from zeta35_graph_scaling import setup
from zeta35_true_subspaces import pencil_polynomial
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    start = time.perf_counter()
    _,A,B,_,_ = setup(2,68)
    weights = [1]*68+[83]
    A = Mat([[A[i,j]*weights[i]*weights[j] for j in range(69)] for i in range(69)])
    B = Mat([[B[i,j]*weights[i]*weights[j] for j in range(69)] for i in range(69)])
    checkpoint = ROOT/'zeta35_two_row_minors.json'
    cache = json.loads(checkpoint.read_text()) if checkpoint.exists() else {}
    def minor(rows,cols,key):
        AA = Mat([[A[i,j] for j in cols] for i in rows])
        BB = Mat([[B[i,j] for j in cols] for i in rows])
        if key in cache:
            p = Poly([Q(c) for c in cache[key]])
        else:
            p = pencil_polynomial(AA,BB)
            cache[key] = list(map(str,p.coeffs()))
            checkpoint.write_text(json.dumps(cache))
        for x in (-1,0,1):
            assert p(x) == (AA+x*BB).det()
        print('MINOR',key,'degree',p.degree(),'seconds',time.perf_counter()-start,flush=True)
        return p
    head = list(range(65))
    D = minor(head,head,'head')
    C = [[None]*4 for _ in range(4)]
    for i in range(4):
        for j in range(i,4):
            C[i][j] = C[j][i] = minor(head+[65+i],head+[65+j],f'{i}{j}')
    pairs = list(itertools.combinations(range(4),2))
    quad = list(itertools.combinations_with_replacement(range(6),2))
    matrix = [[None]*6 for _ in range(6)]
    polys = []
    for i,j in quad:
        a,b = pairs[i]
        c,d = pairs[j]
        numerator = C[a][c]*C[b][d]-C[a][d]*C[b][c]
        quotient,remainder = divmod(numerator,D)
        assert remainder == 0 and quotient.degree() <= 67
        matrix[i][j] = matrix[j][i] = quotient
        polys.append(quotient*(1 if i == j else 2))
    assert matrix[0][5]-matrix[1][4]+matrix[2][3] == 0
    den = math.lcm(*(int(c.denominator) for p in polys for c in p))
    columns = [[int(p[k]*den) for k in range(68)] for p in polys]
    common = math.gcd(*(v for col in columns for v in col))
    columns = [[v//common for v in col] for col in columns]
    F = ZMat(list(map(list,zip(*columns))))
    relation = [0]*21
    for pair,sign in [((0,5),1),((1,4),-1),((2,3),1)]:
        relation[quad.index(pair)] = sign
    assert F*ZMat([[v] for v in relation]) == ZMat(68,1)
    rank = F.rank()
    print('COEFFICIENT_RANK',rank,flush=True)
    extended = ZMat([list(row) for row in zip(*columns)]+[relation])
    ctx.prec = max(abs(v).bit_length() for col in columns for v in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(col)(theta) for col in columns]
    metric = arb_mat(6,6)
    for (i,j),v in zip(quad,values):
        metric[i,j] = metric[j,i] = v if i == j else v/2
    for k in range(1,7):
        assert arb_mat([[metric[i,j] for j in range(k)] for i in range(k)]).det() > 0
    baseline = values[0]/math.gcd(*columns[0])
    out = dict(K=80,N=6,h=67,head_dimension=65,tail=[65,66,67,68],
               tail_weights=[1,1,1,83],pairs=pairs,quadratic_monomials=quad,
               coefficients=columns,relation=relation,coefficient_rank=rank,
               extended_rank=extended.rank(),
               degree_two_full_rank=extended.rank() == 21,
               common_rational_scale=str(Q(common,den)),
               baseline_log=baseline.log().str(40),seconds=time.perf_counter()-start)
    output = ROOT/'zeta35_two_row_pencil.json'
    output.write_text(json.dumps(out,indent=2))
    if '--raw-only' in sys.argv:
        print('DONE raw data, ranks',rank,out['extended_rank'],
              'baseline',out['baseline_log'],flush=True)
        return
    H,T = extended.hnf(transform=True)
    assert T*extended == H
    extended_rank = extended.rank()
    hnf = [[int(H[i,j]) for j in range(21)] for i in range(extended_rank)]
    assert all(H[i,j] == 0 for i in range(extended_rank,H.nrows()) for j in range(21))
    # A rank-deficient degree-two module need not give a uniform content
    # bound. Preserve its exact data for higher-degree ideal computations.
    smith = ZMat(hnf).snf()
    exponent = int(smith[extended_rank-1,extended_rank-1])
    if extended_rank == 21:
        coords = Mat(extended)*Mat(hnf).inv()
        assert all(v.denominator == 1 for v in coords.entries())
        assert all(v.denominator == 1 for v in (Mat(hnf).inv()*exponent).entries())
    out.update(hnf=hnf,
               smith_nonzero_exponent=str(exponent),
               seconds=time.perf_counter()-start)
    output.write_text(json.dumps(out,indent=2))
    print('DONE','baseline',out['baseline_log'],'seconds',out['seconds'],flush=True)


if __name__ == '__main__':
    main()
