"""Independently reconstruct and verify the two selected determinant pencils."""
import json
import math
from pathlib import Path
from flint import fmpq_poly, arb, arb_poly, ctx
from zeta35_target31_scan import entries
from zeta35_infinity_basis import dyadic_basis, finite_check
from zeta35_true_subspaces import pencil_polynomial
from zeta35_local_graph import restriction
from zeta35_target31 import content_and_primitive

ROOT = Path(__file__).parent


def main():
    data = json.loads((ROOT/'zeta35_local_graph_crt.json').read_text())
    source = json.loads((ROOT/'zeta35_local_graph.json').read_text())
    cols = source['coefficients']
    selected = [data['results'][0], next(r for r in data['results'] if r['maximal'])]
    _, aa, bb = entries(40,3,4,37)
    _, _, _, T = dyadic_basis(40,3,4,37)
    A,B,_ = finite_check(40,3,4,aa,bb,T)
    certs = []
    for row in selected:
        u,v = row['u'],row['v']
        C = restriction(u,v)
        AA,BB = C*A*C.transpose(),C*B*C.transpose()
        poly = pencil_polynomial(AA,BB)
        # 34 distinct evaluations identify any polynomial of degree <= 33.
        for x in range(-16,18):
            assert poly(x) == (AA+x*BB).det()
        ct,coeff = content_and_primitive(poly)
        expected = [u*u*x+u*v*y+v*v*z for x,y,z in zip(*cols)]
        gcd = math.gcd(*expected)
        assert coeff == [c//gcd for c in expected]
        assert gcd == int(row['content']) and BB.rank() == 33
        ctx.prec = max(abs(c).bit_length() for c in coeff)+6000
        theta = 3*arb(3).zeta()+arb(5).zeta()
        val = arb_poly(coeff)(theta)
        assert val > 0
        certs.append(dict(u=u,v=v,degree=poly.degree(),target_rank=BB.rank(),
                          primitive_coefficients=list(map(str,coeff)),
                          rational_content=str(ct),family_integer_content=str(gcd),
                          value_interval=val.str(40),log_interval=val.log().str(40),
                          max_coefficient_bits=max(abs(c).bit_length() for c in coeff),
                          exact_evaluation_points=34))
    (ROOT/'zeta35_local_graph_verified.json').write_text(json.dumps(certs,indent=2))
    print([{k:v for k,v in row.items() if k not in ('primitive_coefficients','rational_content')}
           for row in certs])


if __name__ == '__main__':
    main()
