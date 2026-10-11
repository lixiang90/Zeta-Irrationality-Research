"""Finite exact diagnostics for a direct logistic-contour theta functional.

T(f) = -E(f''' )/24 - 3 E(f')/2; E(t^k) = B'_k.
T((t+j)^-1) = theta - H_j^5 - 3 H_j^3.
No asymptotic arithmetic bound or nonvanishing theorem is claimed.
"""
import argparse
import json
import math
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, fmpq_mat, arb, arb_poly, ctx


def bernoulli_prime(k):
    return Q(1, 2) if k == 1 else Q.bernoulli(k)


def moment(e, a=3):
    answer = Q(0)
    if e >= 3:
        answer -= Q(e*(e-1)*(e-2), 24)*bernoulli_prime(e-3)
    if e >= 1:
        answer -= Q(a*e, 2)*bernoulli_prime(e-1)
    return answer


def dpoly(K):
    answer = fmpq_poly([1])
    for j in range(1, K+1):
        answer *= fmpq_poly([j, 1])
    return answer


def entries(K, N, m, h, a=3):
    DN, DK = dpoly(N), dpoly(K)
    W = DN**m
    H = [Q(0)]
    for j in range(1, K+1):
        H.append(H[-1]+Q(1, j**5)+Q(a, j**3))
    base = {}
    for j in range(N+1, K+1):
        base[j] = W(-j)/math.prod(k-j for k in range(1, K+1) if k != j)
    intercept, slope = [], []
    for e in range(2*h-1):
        quotient = (W*fmpq_poly([0]*e+[1]))//DK
        value = sum((quotient[k]*moment(k,a) for k in range(quotient.degree()+1)), Q(0))
        unknown = Q(0)
        for j, residue in base.items():
            term = residue*Q(-j)**e
            unknown += term
            value -= term*H[j]
        intercept.append(value)
        slope.append(unknown)
    return intercept, slope


def determinant_polynomial(intercept, slope, h):
    # Exact Newton interpolation works also when the X coefficient matrix is singular.
    poly = fmpq_poly([0])
    basis = fmpq_poly([1])
    for x in range(h+1):
        value = fmpq_mat([[intercept[i+j]+x*slope[i+j] for j in range(h)] for i in range(h)]).det()
        poly += basis*((value-poly(x))/basis(x))
        basis *= fmpq_poly([-x,1])
    for x in (-1, h+1):
        direct = fmpq_mat([[intercept[i+j]+x*slope[i+j] for j in range(h)] for i in range(h)]).det()
        assert direct == poly(x)
    return poly


def calculate(K, N, m, h, a=3):
    intercept, slope = entries(K,N,m,h,a)
    poly = determinant_polynomial(intercept,slope,h)
    if poly.is_zero():
        return dict(K=K,N=N,m=m,h=h,a=a,zero_polynomial=True)
    den = math.lcm(*(int(c.denominator) for c in poly))
    nums = [int(c*den) for c in poly]
    gcd = math.gcd(*nums)
    primitive = [c//gcd for c in nums]
    ctx.prec = max(abs(c).bit_length() for c in primitive)+K*K+2000
    target = a*arb(3).zeta()+arb(5).zeta()
    value = arb_poly(primitive)(target)
    assert not value.contains(0)
    # Exact target coefficient at the rational point follows the source-independent
    # residue formula; finite checks cannot assert that the true target is irrational.
    answer = dict(K=K,N=N,m=m,h=h,a=a,degree=poly.degree(),
        content=str(Q(gcd,den)),primitive_coefficients=list(map(str,primitive)),
        log_abs_interval=str(abs(value).log()),log_abs=float(abs(value).log()),
        sign=1 if value>0 else -1,
        independent_determinant_check_points=[-1,h+1],
        bits=ctx.prec)
    print(K,N,m,h,a,answer['log_abs'],flush=True)
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n',type=int,default=6)
    parser.add_argument('--scan',action='store_true')
    args = parser.parse_args()
    if args.scan:
        rows = [calculate(5*n,n,m,h)
                for n in range(1,args.max_n+1)
                for m in range(2,9)
                for h in (2*n,3*n,4*n)]
        out = Path(__file__).with_name('zeta35_logistic_contour_scan.json')
    else:
        rows = [calculate(5*n,n,4,3*n) for n in range(1,args.max_n+1)]
        out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(dict(status='finite_exact_and_arb_checks_passed',
        scope='specified ordinary-pole family only; no uniform arithmetic or nonvanishing claim',
        rows=rows),indent=2),encoding='utf-8')


if __name__ == '__main__':
    main()

