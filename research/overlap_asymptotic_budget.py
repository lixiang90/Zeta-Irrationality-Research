"""Rational-envelope budget for overlapping prefixes and truncated dimension.

All envelope geometry is exact. Floating point only selects a rational test
measure; its obstruction value is recomputed using rational interval series.
"""
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path
from scipy.optimize import minimize_scalar
import numpy as np
from two_prefix_budget import linadd,linmul,linval,cross,count_at,deficit
from global_envelope import lower_envelope,area
from restart_obstruction_certificate import double_integral,log_iv,PI,outward_decimal


def profile(alpha,a):
    b=5*alpha-a;lam=1-4*alpha
    roots={}
    for c,e in [(alpha,4),(a,2),(b,2)]:roots[c]=roots.get(c,0)+e
    assert 0<alpha<=F(1,8) and alpha<=a<=b<1 and F(1,2)<=lam<=1-b
    return roots,b,lam


def geometry(alpha,a,R):
    roots,b,lam=profile(alpha,a);lo=1/(2*lam);cuts={lo,F(R)}
    for c in {F(1),2*lam,*roots}:
        cuts.update(F(k)/c for k in range(math.ceil(c*lo),math.floor(c*R)+1))
    cuts=sorted(cuts);refined=set(cuts)
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2;lines=[(F(0),F(0)),(F(0),F(1,2))]
        for c in {F(1),*roots}:
            q=math.floor(c*x);lines +=[(c,-F(q)),(-c,F(q+1))]
        for i,v in enumerate(lines):
            for w in lines[:i]:
                z=cross(v,w)
                if z is not None and l<z<r:refined.add(z)
    degree=sum(c*e for c,e in roots.items())
    for denom in (degree+2*lam-1,degree+lam-1):
        if denom>0:
            z=3/denom
            if lo<z<R:refined.add(z)
    return sorted(refined)


def local_cells(alpha,a,l,r):
    roots,b,lam=profile(alpha,a);x=(l+r)/2;lines=[(F(0),F(0)),(F(0),F(1,2))]
    for c in {F(1),*roots}:
        q=math.floor(c*x);lines +=[(c,-F(q)),(-c,F(q+1))]
    for i,v in enumerate(lines):
        for w in lines[:i]:assert (linval(v,l)-linval(w,l))*(linval(v,r)-linval(w,r))>=0
    lines=sorted(set(v for v in lines if 0<=linval(v,x)<=F(1,2)),key=lambda v:linval(v,x))
    cells=[]
    for v,w in zip(lines,lines[1:]):
        length=linadd(w,linmul(v,-1));u=(linval(v,x)+linval(w,x))/2
        if not linval(length,x):continue
        ell=count_at(x,u);removed=count_at(b*x,u);eta=sum(e*count_at(c*x,u) for c,e in roots.items())
        small=count_at(min(F(1),x),u)-count_at(min(F(1),b*x),u);big=ell-removed-small
        assert min(small,big,removed)>=0
        weights=[min(0,2*i+eta-ell-6) for i in range(big)]+[0]*small
        cells.append(dict(length=length,offset=eta-ell-6,weights=weights))
    dimension=(F(0),F(0))
    for c in cells:dimension=linadd(dimension,linmul(c['length'],len(c['weights'])))
    assert dimension==(1-b,F(0))
    return cells


def candidate_lines(alpha,a,l,r):
    roots,b,lam=profile(alpha,a);x=(l+r)/2;cells=local_cells(alpha,a,l,r)
    q=math.floor(x);j=math.floor(2*lam*x)
    norm=(lam*(-2*q+2*sum(e*math.floor(c*x) for c,e in roots.items())+2*j),-F(j*(j+1),2))
    degree=sum(c*e for c,e in roots.items())
    rank=max([(F(0),F(0)),(degree+2*lam-1,-F(3))],key=lambda v:linval(v,x))
    rank=min([rank,(lam,F(0))],key=lambda v:linval(v,x))
    out={};wmin=min([0]+[w for c in cells for w in c['weights']])
    for threshold in range(min(-1,wmin),1):
        for clipped in (False,True):
            # h smallest finite weights = max_t h*t - sum (t-w)_+.
            cost=linadd(norm,(-lam*threshold,F(0)))
            for c in cells:
                ds=sum(max(0,threshold-(min(w,-1) if clipped else w)) for w in c['weights'])
                cost=linadd(cost,linmul(c['length'],ds))
            if not clipped:cost=linadd(cost,rank)
            out[f'crt_{"clipped" if clipped else "rank"}:{threshold}']=cost
    for k in range(min(c['offset'] for c in cells)-2,max(c['offset'] for c in cells)+math.ceil(4*lam*r)+4):
        cost=linadd(norm,(-lam*k,F(0)))
        for c in cells:cost=linadd(cost,linmul(c['length'],deficit(k,c['offset'])))
        out[f'allocation:{k}']=cost
    return out


def tail_budget(alpha,a,R,end):
    roots,b,lam=profile(alpha,a);cuts={F(R),F(end)}
    for c in {F(1),*roots}:
        cuts.update(F(k)/c for k in range(math.ceil(c*R),math.floor(c*end)+1))
    cuts=sorted(cuts);rational=F(43,32)*(F(1,R*R)-F(1,end*end))+8*lam/end
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2;co=lam*(6-2*math.floor(x)+2*sum(e*math.floor(c*x) for c,e in roots.items()))
        rational+=co*(1/l-1/r)
    co=2*lam*(1-sum(c*e for c,e in roots.items()))
    return rational+co*log_iv(F(end,R)),dict(rational=str(rational),log_coefficient=str(co),log_argument=str(F(end,R)),small_tail=str(8*lam/end))


def real_lower(alpha,a,s):
    roots,b,lam=profile(alpha,a)
    mean=F(4,3)*PI*s+(double_integral(F(1),s)-sum((e*double_integral(c,s) for c,e in roots.items()),0))/(s*s)
    C=-2*lam+sum((2*e*c*lam*(1-log_iv(c)) for c,e in roots.items()),0)+3*lam*lam-2*lam*lam*log_iv(2*lam)
    return lam*lam*(log_iv(s*s)-F(3,2))-lam*mean+C


def choose_s(alpha,a):
    roots,b,lam=profile(alpha,a);lf=float(lam)
    def J(c,s):
        D=s*s
        return (D*c+c**3/3)*np.log(D+c*c)-c**3/3*np.log(c*c)-7*D*c/3+4*s**3*np.arctan(c/s)/3
    def value(s):
        return lf*lf*(np.log(s*s)-1.5)-lf*(4*np.pi*s/3+(J(1,s)-sum(e*J(float(c),s) for c,e in roots.items()))/(s*s))
    ans=minimize_scalar(lambda s:-value(s),bounds=(.02,1.5),method='bounded')
    return F(round(10000*ans.x),10000)


def run(alpha,a,R=40,end=400):
    roots,b,lam=profile(alpha,a);cuts=geometry(alpha,a,R);pieces=[];allocation_only=[]
    for l,r in zip(cuts,cuts[1:]):
        candidates=candidate_lines(alpha,a,l,r)
        pieces+=lower_envelope(l,r,candidates)
        allocation_only+=lower_envelope(l,r,{k:v for k,v in candidates.items() if k.startswith('allocation:')})
    tail,info=tail_budget(alpha,a,R,end);arithmetic=area(pieces)+tail
    s=choose_s(alpha,a);real=real_lower(alpha,a,s);bands={}
    for name,lo,hi in [('x_lt_2',F(0),F(2)),('x_2_3',F(2),F(3)),('x_3_6',F(3),F(6)),('x_ge_6',F(6),F(R))]:
        part=[(max(l,lo),min(r,hi),n,m,c) for l,r,n,m,c in pieces if max(l,lo)<min(r,hi)]
        bands[name]=str(area(part))
    row=dict(alpha=str(alpha),a=str(a),b=str(b),lambda_=str(lam),cutoff=R,tail_end=end,
             arithmetic_interval=outward_decimal(arithmetic),arithmetic_float=float(arithmetic.hi),
             test_s=str(s),real_obstruction_interval=outward_decimal(real),real_obstruction_float=float(real.lo),
             gap_interval=outward_decimal(arithmetic+real),gap_float=float((arithmetic+real).lo),
             truncated_crt_gain=str(area(allocation_only)-area(pieces)),bands=bands,tail=info,
             base_cells=len(cuts)-1,pieces=[[str(v) for v in z] for z in pieces])
    print(json.dumps({k:v for k,v in row.items() if k not in ['pieces','tail','bands']}),flush=True)
    return row


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--alpha',default='1/24');p.add_argument('--multipliers',default='1,3/2,2,9/4,5/2')
    p.add_argument('--cutoff',type=int,default=40);p.add_argument('--tail-end',type=int,default=400);p.add_argument('--out',default='overlap_asymptotic_budget.json');args=p.parse_args()
    rows=[];alpha=F(args.alpha);path=Path(__file__).with_name(args.out)
    for m in map(F,args.multipliers.split(',')):
        rows.append(run(alpha,m*alpha,args.cutoff,args.tail_end))
        path.write_text(json.dumps(dict(scope='A fixed certified arithmetic budget and a lower bound for its comparison-measure method; not a lower bound on actual primitive determinants.',rows=rows),indent=2),encoding='utf-8')
