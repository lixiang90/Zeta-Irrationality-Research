"""Fixed rational diagonal-block models; not a global localization proof."""
import json
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat, nmod_mat
from sympy import factorint
from eight_local_scalar import rational_model
from coupled_pencil import normalized_pencil
from eight_pole_probe import fixed_normalization
from joint_padic import residue


def models():
    _, nine = rational_model()
    V9 = fmpq_mat([[fmpq(x) for x in r] for r in nine['matrix']])
    inner = fmpq_mat(5, 5, [V9[i+4, j+4] for i in range(5) for j in range(5)])
    # For the first six outer coordinates quotient degree <= 2, so the
    # polynomial functional contributes zero. Nodes 0 and 1 have weight zero.
    z = fmpq_poly([0, 1]); D = fmpq_poly([1]); nodes = list(range(-3, 5))
    for a in nodes:
        D *= z-a
    H = [fmpq(0)]
    for j in range(1, 4):
        H.append(H[-1]+fmpq(1, j**7))
    moments = [sum((H[-a if a < 0 else max(0, a-1)]*a**e/D.derivative()(a)
                    for a in nodes), fmpq(0)) for e in range(11)]
    outer = fmpq_mat(6, 6, [moments[i+j] for i in range(6) for j in range(6)])
    # In the CRT basis the last two middle coordinates use the product of
    # seven high poles, not z^7 and z^8. This is a monic determinant-one change.
    Q = fmpq_poly([1])
    for a in [-4, -3, -2, -1, 2, 3, 4]:
        Q *= z-a
    basis = [z**i for i in range(7)]+[Q, z*Q]
    C = fmpq_mat(9, 9, [f[j] for f in basis for j in range(9)])
    assert C.det() == 1
    return {'inner5': inner, 'middle9': C*V9*C.transpose(), 'outer6': outer}


def run(p, N, r):
    K = 4*p+r
    data = normalized_pencil(K, N, p, 10)
    aa, bb, _ = fixed_normalization(data, p, 6)
    assert all(x % (p*p) == 0 for row in bb for x in row)
    tags = data['tags']; fixed = models(); rows = []
    for c in range(1, (p-1)//2+1):
        kind = 'inner5' if c <= N else 'middle9' if c <= r else 'outer6'
        V = fixed[kind]; n = V.nrows()
        ids = [i for i, t in enumerate(tags) if t['c'] == c and t['i'] < n]
        assert len(ids) == n
        outside = 1
        for j in range(N+1, K+1):
            if min(j % p, (-j) % p) != c:
                outside = outside*(j*j-c*c) % p
        prefix = 1
        for j in range(1, N+1):
            if j != c:
                prefix = prefix*(j*j-c*c) % p
        exponent = 0 if kind == 'inner5' else -8 if kind == 'middle9' else -7
        scalar = -pow(c, 6, p)*outside*pow(prefix, 7, p)*pow(2*c, exponent, p) % p
        actual = nmod_mat(n, n, [aa[i][j] % p for i in ids for j in ids], p)
        predicted = nmod_mat(n, n, [scalar*pow(2*c, i+j, p)*residue(V[i, j], p, 0) % p
                                    for i in range(n) for j in range(n)], p)
        rows.append(dict(c=c, kind=kind, matches=actual == predicted,
                         actual_rank=actual.rank(), predicted_rank=predicted.rank()))
    return dict(p=p, N=N, r=r, checks=rows, all_match=all(x['matches'] for x in rows))


if __name__ == '__main__':
    determinants = {}
    for name, V in models().items():
        value = V.det()
        determinants[name] = dict(value=str(value),
                                  numerator_factors={str(p): int(e) for p, e in factorint(int(value.p)).items()},
                                  denominator_factors={str(p): int(e) for p, e in factorint(int(value.q)).items()})
    output = dict(determinants=determinants, rows=[])
    for p, N, r in [(11, 1, 1), (17, 1, 1), (19, 2, 3), (29, 3, 4),
                    (31, 4, 15), (37, 4, 10), (43, 4, 5), (47, 5, 23)]:
        row = run(p, N, r); output['rows'].append(row)
        print(json.dumps({k: v for k, v in row.items() if k != 'checks'}), flush=True)
        assert row['all_match'], row
        Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
