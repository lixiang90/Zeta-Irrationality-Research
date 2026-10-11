"""Verify the whole quadratic pencil by direct restricted determinants.

Twenty decomposable Pluecker vectors span all quadratic functions on Gr(2,4).
The one remaining coefficient ambiguity is fixed by the Bianchi identity.
This does not call the bordered-minor producer.
"""
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path
from flint import fmpq as Q, fmpq_mat as Mat, fmpq_poly as Poly, fmpz_mat as ZMat
from zeta35_graph_scaling import setup
from zeta35_true_subspaces import pencil_polynomial

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
PAIRS = list(itertools.combinations(range(4),2))
QUAD = list(itertools.combinations_with_replacement(range(6),2))


def plane(p):
    antisymmetric = [[Q(0) for _ in range(4)] for _ in range(4)]
    for (i,j),value in zip(PAIRS,p):
        antisymmetric[i][j],antisymmetric[j][i] = Q(value),-Q(value)
    a,b = next(pair for pair,value in zip(PAIRS,p) if value)
    r = antisymmetric[a][b]
    x = [-antisymmetric[b][k]/r for k in range(4)]
    y = [antisymmetric[a][k] for k in range(4)]
    assert [x[i]*y[j]-x[j]*y[i] for i,j in PAIRS] == list(map(Q,p))
    return x,y


def main():
    start = time.perf_counter()
    source = ROOT/'zeta35_two_row_pencil.json'
    src = json.loads(source.read_text())
    assert src['pairs'] == list(map(list,PAIRS))
    assert src['quadratic_monomials'] == list(map(list,QUAD))
    cols,relation = src['coefficients'],src['relation']
    F = ZMat(list(map(list,zip(*cols))))
    assert F.rank() == 17
    assert F*ZMat([[c] for c in relation]) == ZMat(68,1)
    vectors = [[int(i == j) for i in range(6)] for j in range(6)]
    for i,j in itertools.combinations(range(6),2):
        if set(PAIRS[i]) & set(PAIRS[j]):
            vectors.append([int(k == i)+int(k == j) for k in range(6)])
    vectors.extend([[1,0,1,-1,0,1],[0,1,1,1,1,0]])
    measurements = [[p[i]*p[j] for i,j in QUAD] for p in vectors]
    assert len(vectors) == 20 and ZMat(measurements).rank() == 20
    assert ZMat(measurements+[relation]).rank() == 21
    for p in vectors:
        assert p[0]*p[5]-p[1]*p[4]+p[2]*p[3] == 0
    _,A,B,_,_ = setup(2,68)
    scale = Q(src['common_rational_scale'])
    for index,p in enumerate(vectors):
        x,y = plane(p)
        C = Mat(67,69)
        for i in range(65):
            C[i,i] = 1
        for j in range(4):
            C[65,65+j],C[66,65+j] = x[j]*src['tail_weights'][j],y[j]*src['tail_weights'][j]
        AA,BB = C*A*C.transpose(),C*B*C.transpose()
        direct = pencil_polynomial(AA,BB)
        expected = Poly([sum(w*col[k] for w,col in zip(measurements[index],cols))
                         for k in range(68)])*scale
        assert direct == expected and direct.degree() <= 67
        for t in (-1,0,1):
            assert direct(t) == (AA+t*BB).det()
        print('PLANE',index+1,'of',len(vectors),'verified',flush=True)
    out = dict(K=80,h=67,complete_quadratic_pencil_verified=True,
               direct_plane_polynomials=20,coefficient_equalities=20*68,
               direct_determinant_checks=20*3,measurement_rank=20,
               measurement_rank_with_bianchi=21,
               coefficient_rank=17,extended_rank=18,
               source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
               seconds=time.perf_counter()-start,lean_formalized=False)
    (ROOT/'zeta35_two_row_pencil_verified.json').write_text(json.dumps(out,indent=2))
    print(out,flush=True)


if __name__ == '__main__':
    main()
