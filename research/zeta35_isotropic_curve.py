"""A complete rational curve of exact common-isotropic 33-planes.

K=40, N=3, W=D_N^4, ambient dimension 37. Completeness is for the
three rational equations H_66=H_68=H_72=0, NOT for all local congruences.
No finite result is an irrationality proof.
"""
import json, math, time
from pathlib import Path
from flint import fmpq as Q, fmpq_mat as Mat, arb, arb_poly, ctx
from zeta35_target31_scan import entries
from zeta35_infinity_basis import dyadic_basis, finite_check
from zeta35_true_subspaces import pencil_polynomial
from zeta35_target31 import content_and_primitive, rational_log

ROOT = Path(__file__).parent


def plane(t):
    rows = [[Q(int(i == j)) for j in range(37)] for i in range(31)]
    v = [Q(0)]*37
    w = [Q(0)]*37
    if t is None:
        v[31] = w[32] = Q(1)
    else:
        v[32], v[31] = Q(1), -t
        w[35], w[34], w[33], w[31] = Q(1), t, -t*t/2, -t**4/8
    return Mat(rows+[v, w])


def check_plane(C):
    assert C.rank() == 33
    for s in (66, 68, 72):
        H = Mat([[int(i+j == s) for j in range(37)] for i in range(37)])
        assert C*H*C.transpose() == Mat(33, 33)


def evaluate(A, B, t):
    C = plane(t)
    check_plane(C)
    AA, BB = C*A*C.transpose(), C*B*C.transpose()
    P = pencil_polynomial(AA, BB)
    for x in (-1, 0, 1):
        assert P(x) == (AA+x*BB).det()
    ct, coeff = content_and_primitive(P)
    ctx.prec = max(abs(c).bit_length() for c in coeff)+5600
    value = arb_poly(coeff)(3*arb(3).zeta()+arb(5).zeta())
    assert value > 0
    return dict(t='infinity' if t is None else str(t), degree=P.degree(),
                target_rank=BB.rank(), content=str(ct), primitive_coefficients=list(map(str, coeff)),
                log_p=float(value.log()), log_p_interval=str(value.log()),
                log_delta=float(value.log()+rational_log(ct)))


def run():
    start = time.perf_counter()
    _, aa, bb = entries(40, 3, 4, 37)
    _, _, _, T = dyadic_basis(40, 3, 4, 37)
    A, B, checks = finite_check(40, 3, 4, aa, bb, T)
    # Fixed before evaluation: small rational parameters and natural K^2 scale.
    ts = {Q(p, q) for q in (1, 2, 3, 4) for p in range(-12, 13)}
    ts.update(Q(400*k) for k in range(-16, 17))
    ts.update(Q(10)**k*s for k in range(1, 7) for s in (-1, 1))
    rows = [evaluate(A, B, None)]
    for i, t in enumerate(sorted(ts)):
        row = evaluate(A, B, t)
        rows.append(row)
        if i%20 == 0:
            print(i, str(t), row['log_p'], flush=True)
    out = dict(scope='complete geometric parametrization; finite predetermined rational sample',
               K=40, N=3, m=4, ambient=37, dimension=33, prime_checks=checks,
               sample_count=len(rows), rows=rows, seconds=time.perf_counter()-start)
    (ROOT/'zeta35_isotropic_curve.json').write_text(json.dumps(out, indent=2), encoding='utf-8')
    print('BEST', [(r['t'], r['log_p']) for r in sorted(rows, key=lambda r:r['log_p'])[:8]], flush=True)


if __name__ == '__main__':
    run()
