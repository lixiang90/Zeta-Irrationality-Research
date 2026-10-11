"""Exact extreme rays of a positive coefficient cone after zeta3/5 elimination.

The cone gives rational upper/lower bounds on zeta7. Endpoint optimality is
within this specified sufficient positivity cone, not all positive polynomials.
"""
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq
from critical_lift_probe import output_map, primitive, cross


def cone(n,head,w):
    assert n%2==0 and 7*n-2*head-2*w>=1
    d=w+4
    out,_=output_map(n,head=head,degrees=tuple(range(0,2*d,2)))
    y0=(2*(head+1)+n)**2
    shifted=[[sum((out[k][j]*math.comb(i,j)*(-y0)**(i-j) for j in range(i+1)),fmpq(0))
              for i in range(d)] for k in (0,3,5,7)]
    a,b=shifted[1:3]
    rays=[]
    def add(support,weights):
        if all(x<0 for x in weights):weights=[-x for x in weights]
        if not all(x>0 for x in weights):return
        weights,_=primitive(weights)
        assert sum((a[j]*v for j,v in zip(support,weights)),fmpq(0))==0
        assert sum((b[j]*v for j,v in zip(support,weights)),fmpq(0))==0
        vals=[sum((shifted[k][j]*v for j,v in zip(support,weights)),fmpq(0)) for k in (0,3)]
        pair,scale=primitive(vals)
        rays.append(dict(support=list(support),weights=weights,pair=pair,scale=scale))
    for i in range(d):
        if a[i]==0 and b[i]==0:add((i,),[fmpq(1)])
    for i,j in itertools.combinations(range(d),2):
        if a[i]*b[j]-a[j]*b[i]:continue
        row=a if a[i] or a[j] else b
        add((i,j),[row[j],-row[i]])
    for support in itertools.combinations(range(d),3):
        weights=cross([a[i] for i in support],[b[i] for i in support])
        add(support,weights)
    assert rays
    assert set().union(*(set(r['support']) for r in rays))==set(range(d))
    relevant=[r for r in rays if r['pair'][1]]
    lower=max((r for r in relevant if r['pair'][1]>0),key=lambda r:fmpq(-r['pair'][0],r['pair'][1]))
    upper=min((r for r in relevant if r['pair'][1]<0),key=lambda r:fmpq(-r['pair'][0],r['pair'][1]))
    lo=fmpq(-lower['pair'][0],lower['pair'][1]);hi=fmpq(-upper['pair'][0],upper['pair'][1])
    assert lo<hi
    bits=max(max(abs(x).bit_length() for x in r['pair']) for r in rays)+512
    with ctx.workprec(bits):
        z=arb(7).zeta()
        assert arb(lo)<z and z<arb(hi)
        best=None;best_value=None
        for r in rays:
            q0,q7=r['pair']
            value=arb(q0)+arb(q7)*z
            assert value>0
            # Verify positivity independently by the first nonzero summand.
            t=head+1 if r['support'][0]==0 else head+2
            x=2*t+n;y=x*x-y0
            pol=sum(v*y**j for j,v in zip(r['support'],r['weights']))
            num=pol*math.prod(x*x-(n+2*ell)**2 for ell in range(1,head+1))
            den=math.prod((t+j)**7 for j in range(n+1))
            first=r['scale']*fmpq(num,den)
            assert value>arb(first)
            r['log_value_per_n']=(value.log()/n).str(20)
            r['first_term_gt_one']=bool(first>1)
            if q7 and (best is None or value<best_value):best=r;best_value=value
        def packed(r):
            return dict(support=r['support'],weights=list(map(str,r['weights'])),
                        primitive_output_pair=list(map(str,r['pair'])),
                        primitive_scale=str(r['scale']),log_value_per_n=r['log_value_per_n'],
                        first_term_gt_one=r['first_term_gt_one'])
        result=dict(n=n,head=head,w=w,coefficient_count=d,
                    cone_dimension=d-2,extreme_ray_count=len(rays),
                    all_extreme_ray_first_terms_gt_one=all(r['first_term_gt_one'] for r in rays),
                    lower_bound=str(lo),upper_bound=str(hi),
                    log_interval_width_per_n=(arb(hi-lo).log()/n).str(20),
                    optimal_lower_ray=packed(lower),optimal_upper_ray=packed(upper),
                    smallest_primitive_extreme_ray=packed(best),
                    all_rays=[packed(r) for r in rays])
        if n==4 and head==4 and w==0:
            # Interior arithmetic combinations can beat every normalized ray.
            # This exact example produces the fixed form zeta(7)-1, so endpoint
            # optimization is not optimization of all primitive form values.
            assert lo>1
            alpha=(hi-1)/(hi-lo);beta=(lo-1)/(hi-lo)
            lifted=[fmpq(0)]*d
            for r,weight in ((lower,alpha/lower['pair'][1]),
                             (upper,beta/(-upper['pair'][1]))):
                for j,v in zip(r['support'],r['weights']):
                    lifted[j]+=weight*r['scale']*v
            integer_lift,_=primitive(lifted)
            vals=[sum((shifted[k][j]*integer_lift[j] for j in range(d)),fmpq(0)) for k in (0,3)]
            pair,_=primitive(vals)
            assert pair==[-1,1] and all(x>=0 for x in integer_lift)
            result['interior_counterexample']=dict(primitive_output_pair=pair,
                nonnegative_integer_coefficients=list(map(str,integer_lift)),
                unnormalized_output_scale=str(vals[1]),
                normalized_value=(z-1).str(24),
                explanation='A fixed form, not an irrationality sequence. Shows that primitive normalization is not optimized by checking extreme rays alone.')
    return result


def main():
    rows=[];path=Path(__file__).with_suffix('.json')
    for n in (4,8,16,24):
        for w in sorted(set((0,2,4,8,n))):
            row=cone(n,n,w);rows.append(row)
            print(json.dumps(dict(n=n,w=w,rays=row['extreme_ray_count'],
                log_width_per_n=row['log_interval_width_per_n'],
                best_log_form_per_n=row['smallest_primitive_extreme_ray']['log_value_per_n'],
                all_first_gt_one=row['all_extreme_ray_first_terms_gt_one'])),flush=True)
        path.write_text(json.dumps(dict(scope='Exact endpoint optimization in the specified positivity cone; finite tests only.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
