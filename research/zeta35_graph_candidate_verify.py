"""Reconstruct a selected optimized pencil and check all interpolation points."""
import argparse
import json
import math
import sys
from pathlib import Path
from flint import arb, arb_poly, ctx
from zeta35_graph_scaling import setup
from zeta35_true_subspaces import pencil_polynomial
from zeta35_target31 import content_and_primitive
sys.set_int_max_str_digits(0)


def main(path):
    src = json.loads(path.read_text())
    opt = json.loads(path.with_name(path.stem+'_optimized.json').read_text())
    row = opt['best'][0]
    u,v = int(row['u']),int(row['v'])
    pars,A,B,_,restriction = setup(src['n'],src['high'])
    C = restriction(u,v)
    AA,BB = C*A*C.transpose(),C*B*C.transpose()
    poly = pencil_polynomial(AA,BB)
    h = src['h']
    assert poly.degree() == h and BB.rank() == h
    for x in range(h+1):
        assert poly(x) == (AA+x*BB).det()
    content,coeff = content_and_primitive(poly)
    cols = src['coefficients']
    expected = [u*u*x+u*v*y+v*v*z for x,y,z in zip(*cols)]
    g = math.gcd(*expected)
    assert coeff == [c//g for c in expected] and g == int(row['content'])
    ctx.prec = max(abs(c).bit_length() for c in coeff)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    value = arb_poly(coeff)(theta)
    assert value > 0
    out = dict(K=src['K'],h=h,u=str(u),v=str(v),high=src['high'],rho=src['rho'],
               target_rank=BB.rank(),degree=poly.degree(),exact_points=h+1,
               primitive_coefficients=list(map(str,coeff)),
               log_interval=value.log().str(45))
    path.with_name(path.stem+'_candidate_verified.json').write_text(json.dumps(out,indent=2))
    print({k:v for k,v in out.items() if k != 'primitive_coefficients'},flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    args = p.parse_args()
    main(Path(args.source))
