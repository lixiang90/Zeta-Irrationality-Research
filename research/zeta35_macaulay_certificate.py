"""Exact integer ideal-membership certificate and layered analytic bound."""
import json
import math
import sys
import time
from pathlib import Path
from flint import fmpz_mat as ZMat, fmpq_mat as QMat, arb, arb_poly, arb_mat, ctx
from zeta35_macaulay_content import macaulay
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    start = time.perf_counter()
    src = json.loads((ROOT/'zeta35_three_direction_bound.json').read_text())
    rows = json.loads((ROOT/'zeta35_macaulay_content.json').read_text())['rows']
    chosen = next(r for r in rows if r['degree'] == 5)
    degree,d = chosen['degree'],int(chosen['content_upper'])
    monomials,matrix = macaulay(src['hnf'],degree)
    M = ZMat(matrix)
    H,T = M.hnf(transform=True)
    assert T*M == H
    n = len(monomials)
    HH = ZMat([[H[i,j] for j in range(n)] for i in range(n)])
    TT = ZMat([[T[i,j] for j in range(M.nrows())] for i in range(n)])
    inv = QMat(HH).inv()*d
    assert all(x.denominator == 1 for x in inv.entries())
    U = ZMat([[int(inv[i,j]) for j in range(n)] for i in range(n)])
    R = U*TT
    identity = ZMat([[d if i == j else 0 for j in range(n)] for i in range(n)])
    assert R*M == identity
    # R is an explicit integer polynomial certificate, not merely Smith data.
    certificate = dict(degree=degree,monomials=monomials,content_upper=str(d),
                       identity='R * Macaulay(H, 5) = d * I_21',
                       multipliers=[[str(R[i,j]) for j in range(R.ncols())] for i in range(R.nrows())])
    (ROOT/'zeta35_macaulay_certificate.json').write_text(json.dumps(certificate,indent=2))

    cols = src['coefficients']
    previous = json.loads((ROOT/'zeta35_graph_scaling_n2_q67.json').read_text())
    ratio = QMat([[cols[0][-1]]])[0,0]/previous['coefficients'][0][-1]
    for new,old in zip([cols[0],cols[1],cols[3]],previous['coefficients']):
        assert all(x == ratio*y for x,y in zip(new,old))
    zero_case = json.loads((ROOT/'zeta35_graph_scaling_n2_q67_bound_verified.json').read_text())
    ctx.prec = max(abs(c).bit_length() for col in cols for c in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    q = [arb_poly(col)(theta) for col in cols]
    B = arb_mat([[q[0],q[1]/2],[q[1]/2,q[3]]])
    full = arb_mat([[q[0],q[1]/2,q[2]/2],[q[1]/2,q[3],q[4]/2],[q[2]/2,q[4]/2,q[5]]])
    sigma = full.det()/B.det()
    assert q[0] > 0 and B.det() > 0 and sigma > 0
    bound = sigma/d
    assert bound > arb(20).exp()
    assert arb(zero_case['lower_log_interval']) > bound.log()
    result = dict(K=80,h=67,degree=degree,content_upper=str(d),
                  content_upper_log=arb(d).log().str(45),
                  schur_log=sigma.log().str(45),
                  w_nonzero_log_lower=bound.log().str(45),
                  w_zero_log_lower=zero_case['lower_log_interval'],
                  all_parameters_log_lower=bound.log().str(45),
                  theorem='For every nonzero rational direction, the primitive polynomial value is > exp(20).',
                  seconds=time.perf_counter()-start)
    (ROOT/'zeta35_three_direction_closed_bound.json').write_text(json.dumps(result,indent=2))
    print({k:v for k,v in result.items() if k != 'content_upper'},flush=True)


if __name__ == '__main__':
    main()
