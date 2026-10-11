"""Exact projective optimization of every primitive output in a positive cone.

Only rational endpoints enter the selection and certification. Arb values are
diagnostics, not inputs to the choice of the integer forms.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq
from critical_lift_probe import output_map, primitive


def simplest_parents(lo, hi):
    assert 0 <= lo < hi
    p, q, r, s = 0, 1, 1, 0
    jumps = 0
    while True:
        middle = F(p+r, q+s)
        if lo < middle < hi:
            break
        if middle <= lo:
            k = (lo.numerator*q-p*lo.denominator)//(r*lo.denominator-lo.numerator*s)
            assert k >= 1
            p, q = p+k*r, q+k*s
        else:
            k = (r*hi.denominator-hi.numerator*s)//(hi.numerator*q-p*hi.denominator)
            assert k >= 1
            r, s = r+k*p, s+k*q
        jumps += 1
    assert r*q-p*s == 1
    assert F(p,q) <= lo and (s==0 or hi <= F(r,s))
    assert lo < F(p+r,q+s) < hi
    return (p,q),(r,s),jumps


def optimize(lo, hi):
    lower,upper,jumps=simplest_parents(lo,hi)
    p,q=lower;r,s=upper
    candidates=[(-p,q),(r,-s)]
    bounds=[max(a+b*lo,a+b*hi) for a,b in candidates]
    choice=min(range(2),key=lambda i:bounds[i])
    epsilon=bounds[choice]
    Q=q+s
    assert F(1,Q) <= epsilon <= F(2,Q)
    return dict(left=lower,right=upper,Q=Q,inside=F(p+r,Q),
                pair=candidates[choice],epsilon=epsilon,jumps=jumps,
                other_pair=candidates[1-choice],other_epsilon=bounds[1-choice])


def lift(row, pair):
    lo=row['optimal_lower_ray'];hi=row['optimal_upper_ray']
    al,bl=map(int,lo['primitive_output_pair'])
    ah,bh=map(int,hi['primitive_output_pair'])
    assert bl>0 and bh<0
    ql,pl=bl,-al;qu,pu=-bh,ah
    delta=pu*ql-pl*qu
    a,b=pair
    A=qu*a+pu*b;B=ql*a+pl*b
    assert A>=0 and B>=0 and delta>0
    d=row['w']+4
    coefficients=[fmpq(0)]*d
    for ray,mult in ((lo,A),(hi,B)):
        scale=fmpq(ray['primitive_scale'])
        for j,v in zip(ray['support'],ray['weights']):
            coefficients[j]+=mult*scale*int(v)
    integers,input_scale=primitive(coefficients)
    lam=input_scale*delta
    assert lam>0 and all(v>=0 for v in integers)
    n=row['n'];head=row['head'];y0=(2*(head+1)+n)**2
    out,_=output_map(n,head=head,degrees=tuple(range(0,2*d,2)))
    for ray in (lo,hi):
        sparse={j:int(v) for j,v in zip(ray['support'],ray['weights'])}
        center_ray=[sum(v*math.comb(i,j)*(-y0)**(i-j) for i,v in sparse.items() if i>=j) for j in range(d)]
        ray_values=[sum((out[k][j]*center_ray[j] for j in range(d)),fmpq(0)) for k in (0,3,5,7)]
        ra,rb=map(int,ray['primitive_output_pair']);rs=fmpq(ray['primitive_scale'])
        assert ray_values==[fmpq(ra)/rs,0,0,fmpq(rb)/rs]
    centered=[sum(integers[i]*math.comb(i,j)*(-y0)**(i-j) for i in range(j,d)) for j in range(d)]
    values=[sum((out[k][j]*centered[j] for j in range(d)),fmpq(0)) for k in (0,3,5,7)]
    assert values==[lam*a,0,0,lam*b]
    return dict(nonnegative_shifted_coefficients=list(map(str,integers)),
                unnormalized_output_scale=str(lam),
                maximum_coefficient_bits=max(v.bit_length() for v in integers),
                nonzero_coefficient_count=sum(v!=0 for v in integers),
                endpoint_determinant=str(delta),combination_weights=[str(A),str(B)])


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'positive_head_cone.json').read_text())['rows']
    rows=[]
    for old in source:
        lo=F(old['lower_bound']);hi=F(old['upper_bound'])
        opt=optimize(lo,hi)
        a,b=opt['pair'];Q=opt['Q']
        lifted=lift(old,(a,b))
        bound_ray=old['optimal_upper_ray'] if b>0 else old['optimal_lower_ray']
        ra,rb=map(int,bound_ray['primitive_output_pair'])
        multiplier=F(-b,rb)
        assert multiplier>0
        assert (multiplier*ra,multiplier*rb)==(opt['epsilon']-a,-b)
        with ctx.workprec(max(abs(a).bit_length(),abs(b).bit_length())+512):
            value=arb(a)+arb(b)*arb(7).zeta()
            bound=arb(fmpq(opt['epsilon'].numerator,opt['epsilon'].denominator))
            assert value>0 and value<bound
            row=dict(n=old['n'],head=old['head'],w=old['w'],
                lower_bound=str(lo),upper_bound=str(hi),
                minimum_denominator_in_open_interval=str(Q),
                simplest_internal_fraction=str(opt['inside']),
                farey_left=list(map(str,opt['left'])),farey_right=list(map(str,opt['right'])),
                primitive_output_pair=list(map(str,opt['pair'])),
                exact_optimal_uniform_bound=str(opt['epsilon']),
                log_uniform_bound_per_n=(bound.log()/old['n']).str(20),
                log_actual_value_per_n=(value.log()/old['n']).str(20),
                actual_value_ball=value.str(25),
                log_minimum_denominator_per_n=(arb(Q).log()/old['n']).str(20),
                stern_brocot_jumps=opt['jumps'],integer_lift=lifted)
            row['upper_bound_certificate']=dict(
                endpoint_ray='upper' if b>0 else 'lower',
                positive_multiplier=str(multiplier),
                explanation='epsilon minus the chosen form equals this positive multiple of the certified endpoint form.')
        rows.append(row)
        print(json.dumps({k:row[k] for k in ('n','w','minimum_denominator_in_open_interval','log_uniform_bound_per_n','actual_value_ball')}),flush=True)
    (folder/'farey_cone_optimizer.json').write_text(json.dumps(dict(
        scope='Finite exact interval certificates, globally optimal uniform bounds within the specified projective cone, and exact positive integer lifts. No irrationality conclusion.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
