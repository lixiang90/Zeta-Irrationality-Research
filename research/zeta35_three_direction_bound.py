"""An all-parameter bound for the full three-direction last-row family.

Space: psi_0,...,psi_65, u*psi_66+v*psi_67+83*w*psi_68.
Integer parameters are primitive. The bound also covers non-saturated rows,
so it is stronger in domain than the locally saturated family requires.
"""
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
    a = json.loads((ROOT/'zeta35_graph_scaling_n2_q67.json').read_text())
    b = json.loads((ROOT/'zeta35_graph_scaling_n2_q68.json').read_text())
    ca,cb = [list(map(Poly,x['coefficients'])) for x in (a,b)]
    alignment = ca[0].leading_coefficient()/cb[0].leading_coefficient()
    assert ca[0] == alignment*cb[0]
    pars,A,B,checks,restrict = setup(2,68)
    C0 = restrict(1,0)
    B0 = C0*B*C0.transpose()
    raw_scale = B0.det()/ca[0].leading_coefficient()
    C = restrict(0,1)
    C[66,67] = 1
    AA,BB = C*A*C.transpose(),C*B*C.transpose()
    p = pencil_polynomial(AA,BB)
    assert p.degree() == 67
    for x in (-2,-1,0,1,2):
        assert p(x) == (AA+x*BB).det()
    # Coefficient order u^2,uv,uw,v^2,vw,w^2.
    polys = [ca[0],ca[1],alignment*cb[1],ca[2],
             p/raw_scale-ca[2]-alignment*cb[2],alignment*cb[2]]
    den = math.lcm(*(int(c.denominator) for p in polys for c in p))
    cols = [[int(p[i]*den) for i in range(68)] for p in polys]
    g = math.gcd(*(v for col in cols for v in col))
    cols = [[v//g for v in col] for col in cols]
    CM = ZMat(list(map(list,zip(*cols))))
    H,T = CM.hnf(transform=True)
    assert T*CM == H
    hnf = [[int(H[i,j]) for j in range(6)] for i in range(6)]
    assert all(H[i,j] == 0 for i in range(6,68) for j in range(6))
    coords = Mat(CM)*Mat(hnf).inv()
    assert all(x.denominator == 1 for x in coords.entries())
    S = ZMat(hnf).snf()
    exponent = int(S[5,5])
    assert exponent > 0
    # Directly certify exponent*Z^6 is contained in the coefficient row lattice.
    inverse_certificate = Mat(hnf).inv()*exponent
    assert all(x.denominator == 1 for x in inverse_certificate.entries())
    ctx.prec = max(abs(v).bit_length() for col in cols for v in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    q = [arb_poly(col)(theta) for col in cols]
    metric = arb_mat([[q[0],q[1]/2,q[2]/2],
                      [q[1]/2,q[3],q[4]/2],[q[2]/2,q[4]/2,q[5]]])
    trace = q[0]+q[3]+q[5]
    determinant = metric.det()
    assert q[0] > 0 and q[0]*q[3]-q[1]*q[1]/4 > 0 and determinant > 0
    # For eigenvalues 0<lambda1<=lambda2<=lambda3,
    # lambda1 >= 4*det(metric)/trace(metric)^2.
    lower = 4*determinant/(trace*trace*exponent)
    baseline = q[0]/math.gcd(*cols[0])
    # Additional direct polynomial checks for mixed directions.
    for u,v,w in ((1,1,1),(2,-3,1)):
        C = restrict(u,w)
        C[66,67] = v
        AA,BB = C*A*C.transpose(),C*B*C.transpose()
        coefficients = [sum(weights[j]*cols[j][i] for j in range(6)) for i in range(68)
                        for weights in [(u*u,u*v,u*w,v*v,v*w,w*w)]]
        pp = Poly(coefficients)*raw_scale*Q(g,den)
        for x in (-1,0,1):
            assert pp(x) == (AA+x*BB).det()
    out = dict(K=80,h=67,tail=[66,67,68],tail_multipliers=[1,1,83],
               scope='uniform bound for all primitive integer triples',
               coefficients=cols,hnf=hnf,smith_exponent=str(exponent),
               exponent_log=float(arb(exponent).log()),
               baseline_log=float(baseline.log()),
               lower_log=lower.log().str(45),lower_log_float=float(lower.log()),
               lower_exceeds_one=bool(lower > 1),seconds=time.perf_counter()-start)
    (ROOT/'zeta35_three_direction_bound.json').write_text(json.dumps(out,indent=2))
    print({k:v for k,v in out.items() if k not in ('coefficients','hnf','smith_exponent')},flush=True)


if __name__ == '__main__':
    main()
