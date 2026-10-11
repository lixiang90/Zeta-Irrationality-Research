"""Exact integration of CONDITIONAL wider inner-window gain.

No conjectural bound is added to global_envelope.py or to Lean constants.
Endpoint tests certify the integration, not the determinant conjecture.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from global_envelope import cuts_for,candidates,lower_envelope,area,affine,normalization_cost


def new_raw(x,alpha,q):
    overflow=min(2*alpha*x,max(F(0),(6*alpha+1)*x-q-1))
    return ((14*q-2)*alpha-7)*x+5*min(alpha*x,x-q)-overflow


def gain(alpha,q=4,prefix=True):
    lo=F(q) if prefix else F(q)/(1-alpha)
    hi=min(F(2*q+1,2),1/(2*alpha))
    if lo>=hi:return dict(alpha=str(alpha),q=q,prefix=prefix,gain='0',gain_float=0,pieces=[])
    cuts=set(cuts_for(alpha,lo,hi))
    cuts.update(x for x in [F(q)/(1-alpha),F(q+1)/(1+6*alpha),F(q+1)/(1+4*alpha)] if lo<x<hi)
    cuts=sorted(cuts);old=[];new=[]
    for l,r in zip(cuts,cuts[1:]):
        lines=candidates(alpha,l,r)
        old.extend(lower_envelope(l,r,lines))
        xs=[l+(r-l)*F(j,4) for j in [1,2,3]]
        line=affine(xs,[normalization_cost(x,alpha)-new_raw(x,alpha,q) for x in xs])
        lines['wide_conjecture']=line
        new.extend(lower_envelope(l,r,lines))
    g=area(old)-area(new);assert g>=0
    return dict(alpha=str(alpha),q=q,prefix=prefix,x_interval=[str(lo),str(hi)],
                gain=str(g),gain_float=float(g),pieces=[[str(x) for x in p] for p in new])


def upper_gain(alpha,q=4):
    lo=F(q+1)/(1+alpha);hi=F(q+1)
    if alpha*hi>=F(1,2):return None
    cuts=cuts_for(alpha,lo,hi);old=[];new=[]
    for l,r in zip(cuts,cuts[1:]):
        lines=candidates(alpha,l,r);old.extend(lower_envelope(l,r,lines))
        xs=[l+(r-l)*F(j,4) for j in [1,2,3]]
        lines['upper_conjecture']=affine(xs,[normalization_cost(x,alpha)-(((14*q+12)*alpha-1)*x-6*(q+1)) for x in xs])
        new.extend(lower_envelope(l,r,lines))
    g=area(old)-area(new)
    return dict(alpha=str(alpha),q=q,upper_slice=True,x_interval=[str(lo),str(hi)],gain=str(g),gain_float=float(g))


if __name__=='__main__':
    rows=[]
    for a in map(F,['1/200','1/100','1/66','1/50','1/40','1/32','1/24','1/16','1/8']):
        rows.extend([gain(a,4,False),gain(a,4,True)])
        up=upper_gain(a)
        if up:rows.append(up)
        repeated=[gain(a,q,True) for q in range(4,13) if F(q)<1/(2*a)]
        rows.append(dict(alpha=str(a),hypothetical_q4_to_q12=str(sum((F(r['gain']) for r in repeated),F(0))),
                         individual=[{k:v for k,v in r.items() if k!='pieces'} for r in repeated]))
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        status='All gains CONDITIONAL on the unproved wider determinant bounds; rational integration only.',rows=rows),indent=2))
    for row in rows:print(json.dumps({k:v for k,v in row.items() if k not in ['pieces','individual']}),flush=True)
