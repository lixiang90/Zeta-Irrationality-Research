"""Independent coefficient, ideal-membership and analytic verification.

Rebuilds products by exponent dictionaries. Does not import the producer's
Macaulay/HNF constructor or local Smith algorithm.
"""
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path
from flint import fmpz_mat as ZMat, fmpq_mat as QMat, arb, arb_poly, ctx
from zeta35_graph_bound_verify import normal_exists, infinity_exists

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    source = ROOT/'zeta35_two_row_pencil.json'
    src = json.loads(source.read_text())
    cert_path = ROOT/'zeta35_plucker_p12_certificate.json'
    cert = json.loads(cert_path.read_text())
    pairs = [(0,0),(0,1),(0,3),(1,1),(1,3),(3,3)]
    indices = [src['quadratic_monomials'].index(list(p)) for p in pairs]
    expected = [[src['coefficients'][i][k] for i in indices] for k in range(68)]
    assert cert['coefficients'] == expected
    F = ZMat(expected)
    H = ZMat([[int(v) for v in row] for row in cert['hnf']])
    U = ZMat([[int(v) for v in row] for row in cert['coefficient_to_hnf_multipliers']])
    assert U.nrows() == 6 and U.ncols() == 68 and U*F == H
    d = int(cert['content_upper'])
    targets = list(map(tuple,cert['monomials']))
    cubics = list(map(tuple,cert['multiplier_monomials']))
    assert len(set(targets)) == 21
    assert set(targets) == {(a,b,5-a-b) for a in range(6) for b in range(6-a)}
    assert len(set(cubics)) == 10
    assert set(cubics) == {(a,b,3-a-b) for a in range(4) for b in range(4-a)}
    quadratics = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
    rows = []
    for cubic in cubics:
        for i in range(6):
            product = {}
            for j,quadratic in enumerate(quadratics):
                key = tuple(a+b for a,b in zip(cubic,quadratic))
                product[key] = int(H[i,j])
            rows.append([product.get(m,0) for m in targets])
    M = ZMat(rows)
    R = ZMat([[int(v) for v in row] for row in cert['macaulay_multipliers']])
    assert R.nrows() == 21 and R.ncols() == 60
    assert R*M == ZMat([[d if i == j else 0 for j in range(21)] for i in range(21)])
    cols = [src['coefficients'][i] for i in indices]
    ctx.prec = max(abs(c).bit_length() for col in cols for c in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    a,b,c,f,g,h = [arb_poly(col)(theta) for col in cols]
    det2 = a*f-b*b/4
    assert a > 0 and det2 > 0
    sigma = h-(f*c*c-b*c*g+a*g*g)/(4*det2)
    assert sigma > 0 and (sigma/d).log() > 25

    # The w=0 boundary is exactly the previous adjacent binary family.
    old = json.loads((ROOT/'zeta35_graph_scaling_n2_q67.json').read_text())
    opt = json.loads((ROOT/'zeta35_graph_scaling_n2_q67_optimized.json').read_text())
    assert old['rho'] == 1
    for new,old_col in zip([cols[0],cols[1],cols[3]],old['coefficients']):
        assert all(x*old['coefficients'][0][-1] == y*cols[0][-1] for x,y in zip(new,old_col))
    old_F = ZMat(list(map(list,zip(*old['coefficients']))))
    old_H,old_U = old_F.hnf(transform=True)
    assert old_U*old_F == old_H
    assert [[int(old_H[i,j]) for j in range(3)] for i in range(3)] == old['hnf']
    assert all(v.denominator == 1 for v in (QMat(old_F)*QMat(old['hnf']).inv()).entries())
    determinant = math.prod(old['hnf'][i][i] for i in range(3))
    assert determinant == math.prod(int(p)**e for p,e in opt['factors'].items())
    for row in opt['local']:
        p,e,cap = row['p'],row['e'],row['cap']
        assert cap == opt['factors'][str(p)]
        if e < cap:
            assert not normal_exists(old['hnf'],p,e+1,1)
            assert not infinity_exists(old['hnf'],p,e+1)
    G = math.prod(row['p']**row['e'] for row in opt['local'])
    aa,bb,cc = [arb_poly(col)(theta) for col in old['coefficients']]
    assert aa > 0 and cc-bb*bb/(4*aa) > 0
    boundary1 = aa/math.gcd(*old['coefficients'][0])
    boundary2 = (cc-bb*bb/(4*aa))/G
    assert boundary1.log() > 337 and boundary2.log() > 337
    out = dict(certificate_verified=True,original_coefficient_equalities=408,
               generator_inclusion_equalities=36,ideal_membership_equalities=441,
               degree=5,coefficient_matrix_shape=[68,6],
               macaulay_matrix_shape=[60,21],primitive_content_divides_d=True,
               nonzero_p12_log_lower=(sigma/d).log().str(55),
               p12_zero_boundary_log_lower_exceeds=337,
               all_Gr2_3_parameters_log_lower_exceeds=25,
               source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
               certificate_sha256=hashlib.sha256(cert_path.read_bytes()).hexdigest(),
               lean_formalized=False)
    (ROOT/'zeta35_plucker_p12_certificate_verified.json').write_text(json.dumps(out,indent=2))
    print(out,flush=True)


if __name__ == '__main__':
    main()
