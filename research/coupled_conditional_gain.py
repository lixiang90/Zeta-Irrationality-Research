"""Exact CONSEQUENCE of an unproved uniform lower bound, not a new certificate."""
import json
from pathlib import Path
from fractions import Fraction as F
from flint import nmod_mat

def integrate_line(l,r,a,b):return a*(r*r-l*l)/2+b*(r-l)

if __name__=='__main__':
    model_checks=0
    for d in range(1,21):
        for a in range(2*d+3):
            M=nmod_mat(d,d,[int(i+j==a-1) for i in range(d) for j in range(d)],101)
            assert M.rank()==max(0,min(a,2*d-a));model_checks+=1
    alpha=F(1,8)
    cuts=[F(1,3),F(11,32),F(7,20),F(3,8)]
    pieces=[];gain=F(0);third=F(0)
    for l,r in zip(cuts,cuts[1:]):
        def values(y):
            a=3*y-1;d=3*alpha-y;b=max(F(0),min(a,2*d-a))
            candidate=48*alpha-24*y+a-b
            previous=F(9,4)-14*y
            return candidate-previous,d-b
        x0=(3*l+r)/4;x1=(l+3*r)/4;y0=values(x0);y1=values(x1)
        slopes=[(y1[i]-y0[i])/(x1-x0) for i in range(2)]
        intercepts=[y0[i]-slopes[i]*x0 for i in range(2)]
        for k in range(1,8):
            x=l+(r-l)*F(k,8)
            assert all(values(x)[i]==slopes[i]*x+intercepts[i] for i in range(2))
        area=integrate_line(l,r,slopes[0],intercepts[0]);gain+=area
        extra=integrate_line(l,r,slopes[1],intercepts[1]);third+=extra
        pieces.append(dict(left=str(l),right=str(r),gain_slope=str(slopes[0]),
                           gain_intercept=str(intercepts[0]),area=str(area),third_layer_area=str(extra)))
    result=dict(alpha=str(alpha),conditional_gain=str(gain),conditional_gain_float=float(gain),
                conditional_third_layer_area=str(third),model_rank_checks=model_checks,pieces=pieces,
                status='Conditional on the conjectural complete-pencil lower bound. Do not subtract from certified arithmetic constants.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
