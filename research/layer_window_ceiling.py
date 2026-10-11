"""Leading-coefficient ceiling on all extra divisibility in the six-class window."""
import json
from pathlib import Path
from fractions import Fraction as F
from math import prod
from joint_exact import experiment,Dcache
from joint_padic import val

def ceiling(alpha):
    # y=p/K in [1/3,(1+alpha)/3]. The two rank-loss branches meet at y=5 alpha.
    lo=F(1,3);hi=(1+alpha)/3
    cuts=sorted(set([lo,hi]+([5*alpha] if lo<5*alpha<hi else [])))
    total=F(0);pieces=[]
    for l,r in zip(cuts,cuts[1:]):
        y=(l+r)/2
        # Leading coefficient: U/K = 35 alpha + 7 - 21 y.
        # Prior bound: B/K = 30 alpha - 2 - 12 y - min(1+6 alpha-3y,1+alpha-2y).
        if 1+6*alpha-3*y<=1+alpha-2*y:
            a=-12;b=11*alpha+10
        else:a=-11;b=6*alpha+10
        area=a*(r*r-l*l)/2+b*(r-l)
        total+=area;pieces.append(dict(lo=str(l),hi=str(r),slope=str(a),constant=str(b),area=str(area)))
    return total,pieces

if __name__=='__main__':
    checks=[]
    for K,N,p in [(32,4,11),(48,6,17),(56,7,19),(64,8,23)]:
        _,P,*_=experiment(K,[(N,8)],K-N);h=K-N
        lead=(-1)**(h*(h-1)//2)*prod(j**6*int(Dcache(N)(-j*j))**7 for j in range(N+1,K+1))
        assert P[h]==lead
        a=3*p-K-1
        assert val(P[h],p)==35*N-7*a+12
        checks.append(dict(K=K,N=N,p=p,leading_valuation=val(P[h],p)))
    rows=[]
    for alpha in [F(1,40),F(3,40),F(1,8)]:
        bound,pieces=ceiling(alpha)
        rows.append(dict(alpha=str(alpha),ceiling=str(bound),ceiling_float=float(bound),pieces=pieces))
    assert F(rows[0]['ceiling'])==F(83,1600)
    folder=Path(__file__).parent
    prior=next(r for r in json.loads((folder/'restart_obstruction_certificate.json').read_text())['rows'] if r['alpha']=='1/40')
    new=next(r for r in json.loads((folder/'joint_outer_integrals.json').read_text()) if r['alpha']=='1/40')
    remaining=F(prior['gap_interval'][0])-F(new['total_gain'])-F(83,1600)
    inner=F(json.loads((folder/'layer_inner_extension.json').read_text())['inner_improvement']['gain'])
    result=dict(checks=checks,rows=rows,remaining_before_inner=str(remaining),
                inner_gain=str(inner),remaining_obstruction_lower=str(remaining-inner),
                remaining_obstruction_float=float(remaining-inner))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
