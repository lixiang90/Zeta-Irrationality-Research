"""Same-parameter asymptotic budget for integer-valued translated blocks."""
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path
from scipy.optimize import minimize_scalar
import numpy as np
from two_prefix_budget import linadd,linmul,linval,cross,count_at,deficit
from global_envelope import lower_envelope,area
from restart_obstruction_certificate import double_integral,log_iv,PI,outward_decimal


def profiles(alpha,blocks):
    roots={alpha:8};selected={alpha:1};norm={alpha:8}
    for a,L in blocks:
        for endpoint,v in ((a+L,1),(a,-1)):
            roots[endpoint]=roots.get(endpoint,0)+2*v
            selected[endpoint]=selected.get(endpoint,0)+v
        norm[L]=norm.get(L,0)+2
    return ({k:v for k,v in roots.items() if v},
            {k:v for k,v in selected.items() if v},norm)


def geometry(alpha,blocks,R):
    root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks)
    lo=1/(2*lam);cuts={lo,F(R)}
    for a in {F(1),2*lam,*root,*sel,*norm}:
        cuts.update(F(k)/a for k in range(math.ceil(a*lo),math.floor(a*R)+1))
    refined=set(cuts);cuts=sorted(cuts)
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2;lines=[(F(0),F(0)),(F(0),F(1,2))]
        for a in {F(1),*root,*sel}:
            q=math.floor(a*x);lines +=[(a,-F(q)),(-a,F(q+1))]
        for i,a in enumerate(lines):
            for b in lines[:i]:
                c=cross(a,b)
                if c is not None and l<c<r:refined.add(c)
    for x in (F(3)/(1+6*alpha),F(3)/(1+6*alpha-lam)):
        if lo<x<R:refined.add(x)
    return sorted(refined)


def lines_for(alpha,blocks,l,r):
    root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks);x=(l+r)/2
    q,j=math.floor(x),math.floor(2*lam*x)
    normalize=(lam*(-2*q+2*sum(v*math.floor(a*x) for a,v in norm.items())+2*j),-F(j*(j+1),2))
    lines=[(F(0),F(0)),(F(0),F(1,2))]
    for a in {F(1),*root,*sel}:
        q=math.floor(a*x);lines +=[(a,-F(q)),(-a,F(q+1))]
    for i,a in enumerate(lines):
        for b in lines[:i]:assert (linval(a,l)-linval(b,l))*(linval(a,r)-linval(b,r))>=0
    lines=sorted(set(v for v in lines if 0<=linval(v,x)<=F(1,2)),key=lambda v:linval(v,x))
    cells=[];base=(F(0),F(0));zero=(F(0),F(0))
    for a,b in zip(lines,lines[1:]):
        length=linadd(b,linmul(a,-1));u=(linval(a,x)+linval(b,x))/2
        if not linval(length,x):continue
        ell=count_at(x,u);eta=sum(v*count_at(a*x,u) for a,v in root.items())
        removed=sum(v*count_at(a*x,u) for a,v in sel.items())
        small=count_at(min(F(1),x),u)-sum(v*count_at(min(F(1),a*x),u) for a,v in sel.items())
        big=ell-removed-small
        assert min(big,small,removed)>=0
        ws=[min(0,2*i+eta-ell-6) for i in range(big)]+[0]*small
        base=linadd(base,linmul(length,sum(ws)));zero=linadd(zero,linmul(length,ws.count(0)))
        cells.append((length,eta-ell-6))
    rank=max([(F(0),F(0)),(1+6*alpha,-F(3))],key=lambda v:linval(v,x))
    rank=min([rank,(lam,F(0))],key=lambda v:linval(v,x))
    out={'crt_rank':linadd(normalize,linadd(linmul(base,-1),rank)),
         'crt_zero':linadd(normalize,linadd(linmul(base,-1),zero))}
    for k in range(min(b for length,b in cells)-2,max(b for length,b in cells)+math.ceil(4*lam*r)+4):
        val=linadd(normalize,(-lam*k,F(0)))
        for length,b in cells:val=linadd(val,linmul(length,deficit(k,b)))
        out[f'allocation:{k}']=val
    return out


def tail(alpha,blocks,R=40,end=400):
    root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks)
    width=1+sum(abs(v) for v in root.values());constant=F(width*width+5,32)
    cuts={F(R),F(end)}
    for a in {F(1),*norm}:
        cuts.update(F(k)/a for k in range(math.ceil(a*R),math.floor(a*end)+1))
    cuts=sorted(cuts);rational=constant/2*(F(1,R*R)-F(1,end*end))+8*lam/end
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2
        b=lam*(6-2*math.floor(x)+2*sum(v*math.floor(a*x) for a,v in norm.items()))
        rational+=b*(1/l-1/r)
    coef=2*lam*(1-sum(v*a for a,v in norm.items()))
    return rational+coef*log_iv(F(end,R)),dict(width=width,constant=str(constant),
            rational=str(rational),log_coefficient=str(coef),log_argument=str(F(end,R)),small_tail=str(8*lam/end))


def Cstar(alpha,blocks):
    root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks)
    return (-2*lam+sum((2*v*a*lam*(1-log_iv(a)) for a,v in norm.items()),0)
            +3*lam*lam-2*lam*lam*log_iv(2*lam))


def real_lower(alpha,blocks,s):
    root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks)
    mean=F(4,3)*PI*s+(double_integral(F(1),s)-sum((v*double_integral(a,s) for a,v in root.items()),0))/(s*s)
    return lam*lam*(log_iv(s*s)-F(3,2))-lam*mean+Cstar(alpha,blocks)


def choose_s(alpha,blocks):
    root,sel,norm=profiles(alpha,blocks);lam=float(1-alpha-sum(L for a,L in blocks))
    def J(c,s):
        D=s*s
        return (D*c+c**3/3)*np.log(D+c*c)-c**3/3*np.log(c*c)-7*D*c/3+4*s**3*np.arctan(c/s)/3
    def val(s):return lam*lam*(np.log(s*s)-1.5)-lam*(4*np.pi*s/3+(J(1,s)-sum(v*J(float(a),s) for a,v in root.items()))/(s*s))
    ans=minimize_scalar(lambda s:-val(s),bounds=(.02,1.5),method='bounded')
    return F(round(10000*ans.x),10000)


def run(alpha,blocks,R=40,end=400):
    lam=1-alpha-sum(L for a,L in blocks)
    assert 0<alpha<=F(1,8) and lam>F(1,2)
    for i,(a,L) in enumerate(blocks):
        assert a>=alpha and a+L<=1 and L>0
        if i:assert blocks[i-1][0]+blocks[i-1][1]<=a
    cuts=geometry(alpha,blocks,R);pieces=[]
    for l,r in zip(cuts,cuts[1:]):pieces+=lower_envelope(l,r,lines_for(alpha,blocks,l,r))
    tailval,tailinfo=tail(alpha,blocks,R,end);A=area(pieces)+tailval
    s=choose_s(alpha,blocks);B=real_lower(alpha,blocks,s)
    row=dict(alpha=str(alpha),blocks=[[str(a),str(L)] for a,L in blocks],lambda_=str(lam),
             cutoff=R,tail_end=end,A_interval=outward_decimal(A),A_float=float(A.hi),
             B_interval=outward_decimal(B),B_float=float(B.lo),test_s=str(s),
             gap_interval=outward_decimal(A+B),gap_float=float((A+B).lo),
             tail=tailinfo,base_cells=len(cuts)-1,envelope_pieces=len(pieces),
             pieces=[[str(x) for x in p] for p in pieces])
    print(json.dumps({k:v for k,v in row.items() if k not in ('pieces','tail')}),flush=True)
    return row


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--alpha',default='1/24');p.add_argument('--length',default='1/8')
    p.add_argument('--starts',default='1/24,1/12,1/8,1/4,1/2,7/8')
    a=p.parse_args();rows=[];path=Path(__file__).with_name('integer_block_budget.json')
    for start in map(F,a.starts.split(',')):
        rows.append(run(F(a.alpha),[(start,F(a.length))]))
        path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
