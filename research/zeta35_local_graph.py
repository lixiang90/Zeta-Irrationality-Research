"""A genuine local congruence family beyond exact rational isotropy.

U=span(psi_0,...,psi_31, u*psi_32+41*v*psi_33), gcd(u,v)=1, 41 does not divide u.
It is p-integral at p=41,43,47, but is not on the exact isotropic curve for v!=0.
"""
import json, math
from pathlib import Path
from flint import fmpq as Q, fmpq_mat as Mat, fmpq_poly as Poly, arb, arb_poly, ctx
from zeta35_target31_scan import entries
from zeta35_infinity_basis import dyadic_basis, finite_check
from zeta35_true_subspaces import pencil_polynomial

ROOT = Path(__file__).parent


def restriction(u, v):
    C = Mat([[int(i == j) for j in range(37)] for i in range(33)])
    C[32, 32], C[32, 33] = u, 41*v
    return C


def main():
    _, aa, bb = entries(40, 3, 4, 37)
    _, _, _, T = dyadic_basis(40, 3, 4, 37)
    A, B, checks = finite_check(40, 3, 4, aa, bb, T)
    def detpoly(u, v):
        C = restriction(u, v)
        return pencil_polynomial(C*A*C.transpose(), C*B*C.transpose())
    p0, p1, ps = detpoly(1, 0), detpoly(0, 1), detpoly(1, 1)
    pc = ps-p0-p1
    denominator = math.lcm(*(int(v.denominator) for p in (p0, pc, p1) for v in p))
    columns = [[int(p[i]*denominator) for i in range(34)] for p in (p0, pc, p1)]
    g = math.gcd(*(v for col in columns for v in col))
    columns = [[v//g for v in col] for col in columns]
    for u, v in ((1, 0), (3, 1), (-400, 3)):
        assert detpoly(u, v) == u*u*p0+u*v*pc+v*v*p1
    ctx.prec = max(abs(v).bit_length() for col in columns for v in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(col)(theta) for col in columns]
    assert values[0] > 0 and values[2] > 0
    us = {s*k for s in (-1, 1) for k in range(1, 129)}
    us.update(s*400*k for s in (-1, 1) for k in range(1, 257))
    candidates = {(1, 0)} | {(u, v) for u in us for v in (1, 2, 3)
                              if math.gcd(u, v) == 1 and u%41 != 0}
    rows = []
    for u, v in sorted(candidates):
        coeff = [u*u*columns[0][i]+u*v*columns[1][i]+v*v*columns[2][i] for i in range(34)]
        ct = math.gcd(*coeff)
        val = (u*u*values[0]+u*v*values[1]+v*v*values[2])/ct
        assert val > 0
        rows.append(dict(u=u, v=v, log_p=float(val.log()), content=str(ct)))
    best = sorted(rows, key=lambda r:r['log_p'])[:10]
    out = dict(scope='finite predetermined sample of locally integral true subspaces',
               count=len(rows), coefficients=columns, rows=rows, best=best,
               prime_checks=checks)
    (ROOT/'zeta35_local_graph.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print('COUNT',len(rows),'BEST',best)


if __name__ == '__main__':
    main()
