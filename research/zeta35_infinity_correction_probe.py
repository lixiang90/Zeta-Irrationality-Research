"""Finite truncated-positive moment corrections, with full content accounting.

The correction changes polynomial moments only and preserves the simple-pole
functional, including its X coefficient.  It is not asserted to be a positive
measure globally.  Arb verifies a sufficient relative-matrix norm bound.
"""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat, arb, arb_mat, arb_poly, ctx
import zeta35_mixed_moments as mixed
from zeta35_target31 import content_and_primitive, rational_log, primes_to

sys.set_int_max_str_digits(0)


def aq(x):
    return arb(int(x.numerator))/int(x.denominator)


def valuation_packet(q):
    num,den = abs(int(q.numerator)), int(q.denominator)
    vals = {}
    for p in primes_to(200):
        v = 0
        while num % p == 0:
            num //= p
            v += 1
        while den % p == 0:
            den //= p
            v -= 1
        if v:
            vals[str(p)] = v
    assert num == den == 1, (num.bit_length(),den.bit_length())
    return vals


def main():
    K,N,h,A5,B = mixed.original.entries(1)
    A3 = mixed.shifted_mu3_entries(1)
    A = [a-3*b for a,b in zip(A5,A3)]
    W = Poly(mixed.original.Dpoly(N)**6)
    D = Poly(mixed.original.Dpoly(K))
    quotients = [(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    ctx.prec = 12000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    H = arb_mat([[aq(A[i+j])+theta*aq(B[i+j]) for j in range(h)] for i in range(h)])
    Hinv = H.inv()
    baseline = mixed.original.det_poly(h,A,B)
    base_content, base_coeff = content_and_primitive(baseline)
    base_value = arb_poly(base_coeff)(theta)
    assert base_value > 0
    rows = []
    primes = (41,43,47,53)
    for ps in [(p,) for p in primes]+[primes]:
        corr = [Q(0) for _ in A]
        moment_specs = []
        for p in ps:
            e = p-3
            u = 3*pow(2,-1,p) % p
            if u > p//2:
                u -= p
            c = Q(u,p)
            moment_specs.append(dict(p=p,e=e,correction=str(c)))
            for s,q in enumerate(quotients):
                corr[s] += c*q[e] if e<=q.degree() else 0
        Cq = fmpq_mat([[corr[i+j] for j in range(h)] for i in range(h)])
        C = arb_mat([[aq(corr[i+j]) for j in range(h)] for i in range(h)])
        rel = Hinv*C
        trace2 = (rel*rel).trace()
        ratio = (H-C).det()/H.det()
        modified = [a-c for a,c in zip(A,corr)]
        poly = mixed.original.det_poly(h,modified,B)
        content, coeff = content_and_primitive(poly)
        value = arb_poly(coeff)(theta)
        for x in (Q(-1),Q(0),Q(1)):
            direct = fmpq_mat([[modified[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
            assert direct == poly(x)
        relative_norm_certified = trace2 < 1
        # trace(relative^2) is the sum of squares of real eigenvalues, because
        # H^-1*C is similar to a real symmetric matrix.
        if relative_norm_certified:
            assert ratio > 0 and value > 0
        row = dict(primes=ps,moment_specs=moment_specs,correction_rank=Cq.rank(),
                   trace_relative_square_interval=str(trace2),
                   relative_norm_certified=relative_norm_certified,
                   determinant_ratio_interval=str(ratio),
                   modified_target_value_interval=str(value),
                   target_positive=value>0, degree=poly.degree(),
                   log_abs_primitive_interval=str(abs(value).log()),
                   log_abs_primitive=float(abs(value).log()),
                   content=str(content),
                   log_content_gain=float(rational_log(content/base_content)),
                   content_gain_valuations=valuation_packet(content/base_content),
                   coefficient_checks=['-1','0','1'])
        rows.append(row)
        print(ps,'rank',row['correction_rank'],'norm certified',relative_norm_certified,
              'log trace2',float(abs(trace2).log()),'positive',row['target_positive'],
              'log|P|',row['log_abs_primitive'],'content gain',row['log_content_gain'],flush=True)
    out = dict(status='finite_checks_passed',K=K,N=N,h=h,m=6,
               baseline_log_primitive=float(base_value.log()),
               scope='K=40 only; sufficient norm test failure is not proof of indefiniteness; '
                     'positive determinant alone is not proof of positive definiteness.',
               rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__ == '__main__':
    main()
