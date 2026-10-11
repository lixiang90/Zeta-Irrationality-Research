"""Independent verification of the saved integer polynomial identities.

Does not import the Macaulay constructor or local Smith algorithm used by
the producer. Rebuilds every coefficient by direct monomial multiplication.
"""
import json
import math
import sys
from pathlib import Path
from flint import fmpz_mat as ZMat, arb, arb_poly, ctx
from zeta35_graph_bound_verify import normal_exists, infinity_exists
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    src = json.loads((ROOT/'zeta35_three_direction_bound.json').read_text())
    cert = json.loads((ROOT/'zeta35_macaulay_certificate.json').read_text())
    C = ZMat(list(map(list,zip(*src['coefficients']))))
    HH,T = C.hnf(transform=True)
    assert T*C == HH
    assert [[int(HH[i,j]) for j in range(6)] for i in range(6)] == src['hnf']
    degree,d = cert['degree'],int(cert['content_upper'])
    assert degree == 5
    targets = [tuple(m) for m in cert['monomials']]
    expected_targets = {(i,j,degree-i-j) for i in range(degree+1) for j in range(degree-i+1)}
    assert len(targets) == len(set(targets)) == 21 and set(targets) == expected_targets
    cubics = sorted({(i,j,3-i-j) for i in range(4) for j in range(4-i)},reverse=True)
    quadratics = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
    # Direct dictionary multiplication F_i times a cubic monomial.
    matrix = []
    for cubic in cubics:
        for generator in src['hnf']:
            product = {}
            for quadratic,coefficient in zip(quadratics,generator):
                monomial = tuple(cubic[i]+quadratic[i] for i in range(3))
                product[monomial] = coefficient
            matrix.append([product.get(m,0) for m in targets])
    M = ZMat(matrix)
    R = ZMat([[int(c) for c in row] for row in cert['multipliers']])
    assert R.nrows() == 21 and R.ncols() == 60
    assert R*M == ZMat([[d if i == j else 0 for j in range(21)] for i in range(21)])

    cols = src['coefficients']
    ctx.prec = max(abs(c).bit_length() for col in cols for c in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    a,b,c,f,g,h = [arb_poly(col)(theta) for col in cols]
    det2 = a*f-b*b/4
    assert a > 0 and det2 > 0
    sigma = h-(f*c*c/4-b*c*g/4+a*g*g/4)/det2
    assert sigma > 0 and (sigma/d).log() > 20

    old = json.loads((ROOT/'zeta35_graph_scaling_n2_q67.json').read_text())
    bounds = json.loads((ROOT/'zeta35_graph_scaling_n2_q67_optimized.json').read_text())
    for new,previous in zip([cols[0],cols[1],cols[3]],old['coefficients']):
        assert all(x*old['coefficients'][0][-1] == y*cols[0][-1] for x,y in zip(new,previous))
    for row in bounds['local']:
        p,e,cap = row['p'],row['e'],row['cap']
        if e < cap:
            assert not normal_exists(old['hnf'],p,e+1,1)
            assert not infinity_exists(old['hnf'],p,e+1)
    old_G = math.prod(row['p']**row['e'] for row in bounds['local'])
    aa,bb,cc = [arb_poly(col)(theta) for col in old['coefficients']]
    assert (aa/math.gcd(*old['coefficients'][0])).log() > 337
    assert ((cc-bb*bb/(4*aa))/old_G).log() > 337
    result = dict(integer_identities=21,integer_multipliers_per_identity=60,
                  coefficient_equalities=441,degree=5,
                  certificate_verified=True,original_row_lattice_inclusion=True,
                  independent_schur_log_lower=(sigma/d).log().str(50),
                  w_zero_log_lower_exceeds=337,all_parameters_log_lower_exceeds=20,
                  lean_formalized=False)
    (ROOT/'zeta35_macaulay_certificate_verified.json').write_text(json.dumps(result,indent=2))
    print(result,flush=True)


if __name__ == '__main__':
    main()
