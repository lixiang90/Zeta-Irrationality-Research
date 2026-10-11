"""Reflected head-zero spaces, exact elimination and primitive budgets."""
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq
from critical_lift_probe import output_map, primitive, cross


def probe(n, head):
    assert n % 2 == 0 and 2*head <= 7*n-1
    out, local = output_map(n, head=head)
    assert all(out[k][j] == 0 for k in (1,2,4,6) for j in range(4))
    p, _ = primitive(cross(out[3][:3], out[5][:3]))
    assert p[-1]
    if p[-1] < 0:
        p = [-x for x in p]
    a = [sum((out[k][j]*p[j] for j in range(3)), fmpq(0)) for k in range(8)]
    assert all(a[k] == 0 for k in (1,2,3,4,5,6)) and a[7]
    pair, factor = primitive([a[0], a[7]])
    T = head+1
    y0 = (2*T+n)**2
    shifted = [p[0]+p[1]*y0+p[2]*y0*y0, p[1]+2*p[2]*y0, p[2]]
    positive = all(x >= 0 for x in shifted) and shifted[0] > 0
    def numerator(t):
        x = 2*t+n
        return (p[0]+p[1]*x*x+p[2]*x**4)*math.prod(x*x-(n+2*ell)**2 for ell in range(1,head+1))
    def denominator(t):
        return math.prod((t+j)**7 for j in range(n+1))
    first = fmpq(numerator(T),denominator(T))
    # Uniform power tail bound. Valid for all n,L in this file, independently
    # of positivity; positivity additionally makes the first term a lower bound.
    u = T+n+head
    exponent = 7*(n+1)-2*head-4
    assert exponent > 1
    upper = fmpq(4**head*u**(2*head)*(abs(p[0])+4*abs(p[1])*u*u+16*abs(p[2])*u**4),denominator(T))
    upper *= 1+fmpq(u,exponent-1)
    q0,q7=pair
    bits=max(abs(q0).bit_length(),abs(q7).bit_length())+512
    with ctx.workprec(bits):
        value=arb(q0)+arb(q7)*arb(7).zeta()
        assert not value.contains(0)
        assert abs(value) <= arb(factor*upper)
        if positive:
            assert value >= arb(factor*first)
        row=dict(n=n,head=head,decay_M=7*n-2*head+2,
            numerator_centered_even_coefficients=list(map(str,p)),output_pair=list(map(str,pair)),
            primitive_scale=str(factor),positive_on_tail_certificate=positive,
            shifted_numerator_coefficients=list(map(str,shifted)),
            log_abs_primitive_per_n=(abs(value).log()/n).str(20),
            log_denominator_per_n=(arb(abs(q7)).log()/n).str(20),
            log_error_per_n=((abs(value)/abs(q7)).log()/n).str(20),
            log_upper_bound_per_n=(arb(factor*upper).log()/n).str(20),
            log_first_term_per_n=(arb(abs(factor*first)).log()/n).str(20),
            primitive_first_term_gt_one=bool(positive and factor*first>1))
    for t in (1,head+1,head+n+2):
        for col,d in enumerate((0,2,4,6)):
            x=2*t+n
            direct=fmpq(x**d*math.prod(x*x-(n+2*ell)**2 for ell in range(1,head+1)),denominator(t))
            pf=sum((local[j][col][k]/(t+j)**k for j in range(n+1) for k in range(1,8)),fmpq(0))
            assert direct==pf
    return row


def main():
    path=Path(__file__).with_suffix('.json')
    rows=[]
    for n in (4,8,12,16,24,32):
        for head in (0,n//4,n//2,n,3*n//2,2*n,5*n//2,3*n):
            row=probe(n,head);rows.append(row)
            print(json.dumps({k:row[k] for k in ('n','head','positive_on_tail_certificate','log_abs_primitive_per_n','log_error_per_n','primitive_first_term_gt_one')}),flush=True)
        path.write_text(json.dumps(dict(scope='Finite exact arithmetic and Arb enclosures; no asymptotic conclusion.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
