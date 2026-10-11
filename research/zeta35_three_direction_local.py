"""Eliminate one coordinate and bound three-variable content projectively.

Each unit-coordinate chart is constrained by both binary projections.
These are necessary conditions, so their combination gives an upper bound,
not a claim that the bound is attained.
"""
import json
import itertools
import math
import sys
from pathlib import Path
from flint import fmpz_mat as ZMat, fmpq_mat as Mat, arb, arb_poly, arb_mat, ctx
from sympy import factorint
from zeta35_graph_bound_verify import normal_exists
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def main():
    src = json.loads((ROOT/'zeta35_three_direction_bound.json').read_text())
    cols = src['coefficients']
    monomials = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
    factors = {int(p):int(e) for p,e in factorint(int(src['smith_exponent'])).items()}
    projections = []
    for eliminated,other,unit in itertools.permutations(range(3)):
        order = [eliminated,other,unit]
        indices = [monomials.index(tuple(sorted((order[i],order[j])))) for i,j in monomials]
        CM = ZMat([[col[i] for col in [cols[k] for k in indices]] for i in range(68)])
        H,T = CM.hnf(transform=True)
        assert T*CM == H
        top = [[int(H[i,j]) for j in range(6)] for i in range(6)]
        coords = Mat(CM)*Mat(top).inv()
        assert all(c.denominator == 1 for c in coords.entries())
        bottom = [row[3:] for row in top[3:]]
        bounds = {}
        for p,cap in factors.items():
            lo,hi = 0,cap+1
            while hi-lo > 1:
                mid = (lo+hi)//2
                if normal_exists(bottom,p,mid,1):
                    lo = mid
                else:
                    hi = mid
            if lo < cap:
                assert not normal_exists(bottom,p,lo+1,1)
            bounds[p] = lo
        projections.append(dict(eliminated=eliminated,other=other,unit=unit,
                                bottom_hnf=bottom,bounds=bounds))
    local = []
    for p,cap in factors.items():
        charts = [min(r['bounds'][p] for r in projections if r['unit'] == unit) for unit in range(3)]
        local.append(dict(p=p,smith_cap=cap,chart_bounds=charts,bound=max(charts)))
    upper = math.prod(r['p']**r['bound'] for r in local)
    ctx.prec = max(abs(v).bit_length() for col in cols for v in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    q = [arb_poly(col)(theta) for col in cols]
    M = arb_mat([[q[0],q[1]/2,q[2]/2],[q[1]/2,q[3],q[4]/2],[q[2]/2,q[4]/2,q[5]]])
    trace = q[0]+q[3]+q[5]
    lower = 4*M.det()/(trace**2*upper)
    assert lower > 0
    out = dict(scope='upper bound via binary projections, not exact maximal content',
               projections=projections,local=local,content_upper=str(upper),
               upper_log=float(arb(upper).log()),lower_log=lower.log().str(45),
               lower_exceeds_one=bool(lower > 1))
    (ROOT/'zeta35_three_direction_local.json').write_text(json.dumps(out,indent=2))
    print('LOCAL',local)
    print('UPPER_LOG',out['upper_log'],'LOWER_LOG',out['lower_log'],flush=True)


if __name__ == '__main__':
    main()
