"""Certified piecewise arithmetic budget for D_N^6 D_M^2, h=K-M.

All arithmetic integrations and uniform-test enclosures are rational.
The real lower bound diagnoses this budget, not the unknown optimal content.
"""
import argparse
import json
import math
from fractions import Fraction as F
from pathlib import Path
from global_envelope import lower_envelope, area
from restart_obstruction_certificate import (double_integral,log_iv,PI,
                                             outward_decimal,iv)


def linadd(a,b):return (a[0]+b[0],a[1]+b[1])
def linmul(a,c):return (a[0]*c,a[1]*c)
def linval(a,x):return a[0]*x+a[1]
def cross(a,b):
    return (b[1]-a[1])/(a[0]-b[0]) if a[0]!=b[0] else None


def geometry(alpha,beta,R):
    lam=1-beta;lo=1/(2*lam);cuts={lo,F(R)}
    for c in (F(1),alpha,beta,2*lam):
        cuts.update(F(k)/c for k in range(math.ceil(c*lo),math.floor(c*R)+1))
    cuts=sorted(cuts);refined=set(cuts)
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2;lines=[(F(0),F(0)),(F(0),F(1,2))]
        for a in (F(1),alpha,beta):
            q=math.floor(a*x);lines +=[(a,-F(q)),(-a,F(q+1))]
        for i,a in enumerate(lines):
            for b in lines[:i]:
                c=cross(a,b)
                if c is not None and l<c<r:refined.add(c)
    for c in (F(3)/(1+6*alpha),F(3)/(6*alpha+beta)):
        if lo<c<R:refined.add(c)
    return sorted(refined)


def count_at(z,u):return math.floor(z-u)+math.floor(z+u)+1


def local_cells(l,r,alpha,beta):
    x=(l+r)/2;lines=[(F(0),F(0)),(F(0),F(1,2))]
    for a in (F(1),alpha,beta):
        q=math.floor(a*x)
        lines += [(a,-F(q)),(-a,F(q+1))]
    # Geometry construction certifies all branch orders throughout the cell.
    for i,a in enumerate(lines):
        for b in lines[:i]:
            assert (linval(a,l)-linval(b,l))*(linval(a,r)-linval(b,r))>=0
    lines=sorted(set(a for a in lines if 0<=linval(a,x)<=F(1,2)),key=lambda a:linval(a,x))
    out=[]
    for a,b in zip(lines,lines[1:]):
        length=linadd(b,linmul(a,-1));u=(linval(a,x)+linval(b,x))/2
        if not linval(length,x):continue
        ell,n,m=(count_at(c*x,u) for c in (F(1),alpha,beta))
        small=count_at(min(F(1),x),u)-count_at(min(F(1),beta*x),u)
        big=ell-m-small;eta=6*n+2*m
        ws=[min(0,2*i+eta-ell-6) for i in range(big)]+[0]*small
        assert len(ws)==ell-m
        out.append(dict(length=length,offset=eta-ell-6,raw=sum(ws),zero=ws.count(0)))
    assert sum((a['length'][0] for a in out),F(0))==0
    assert sum((a['length'][1] for a in out),F(0))==F(1,2)
    return out


def deficit(k,b):
    n=max(0,(k-b+1)//2)
    return n*(k-b)-n*(n-1)


def candidate_lines(l,r,alpha,beta):
    lam=1-beta;x=(l+r)/2;cells=local_cells(l,r,alpha,beta)
    q,qn,qm,j=(math.floor(c*x) for c in (F(1),alpha,beta,2*lam))
    norm=(lam*(-2*q+12*qn+4*qm+2*j),-F(j*(j+1),2))
    base=(F(0),F(0));zero=(F(0),F(0))
    for c in cells:
        base=linadd(base,linmul(c['length'],c['raw']))
        zero=linadd(zero,linmul(c['length'],c['zero']))
    rank=min([(F(0),F(0)),(1+6*alpha,-F(3))],key=lambda a:-linval(a,x))
    rank=min([rank,(lam,F(0))],key=lambda a:linval(a,x))
    # Keep both valid corrections as separate candidates; lower_envelope handles
    # their crossing exactly, without an extra numerical branch search.
    lines={'residue_rank':linadd(norm,linadd(linmul(base,-1),rank)),
           'residue_zero':linadd(norm,linadd(linmul(base,-1),zero))}
    bmin=min(c['offset'] for c in cells);bmax=max(c['offset'] for c in cells)
    for k in range(bmin-2,bmax+math.ceil(4*lam*r)+4):
        value=linadd(norm,(-lam*k,F(0)))
        for c in cells:value=linadd(value,linmul(c['length'],deficit(k,c['offset'])))
        lines[f'allocation:{k}']=value
    return lines


def real_lower(alpha,beta,s):
    lam=1-beta;D=s*s
    mean=F(4,3)*PI*s+(double_integral(F(1),s)-6*double_integral(alpha,s)-2*double_integral(beta,s))/D
    C=(-2*lam+12*alpha*lam*(1-log_iv(alpha))+4*beta*lam*(1-log_iv(beta))
       +3*lam*lam-2*lam*lam*log_iv(2*lam))
    return lam*lam*(log_iv(D)-F(3,2))-lam*mean+C


def choose_s(alpha,beta):
    # Only selection uses floating point. The chosen rational is recertified.
    from scipy.optimize import minimize_scalar
    import numpy as np
    a,b=float(alpha),float(beta);lam=1-b
    def J(c,s):
        D=s*s
        return (D*c+c**3/3)*np.log(D+c*c)-c**3/3*np.log(c*c)-7*D*c/3+4*s**3*np.arctan(c/s)/3
    def score(s):return lam*lam*(np.log(s*s)-1.5)-lam*(4*np.pi*s/3+(J(1,s)-6*J(a,s)-2*J(b,s))/(s*s))
    res=minimize_scalar(lambda s:-score(s),bounds=(.03,1.5),method='bounded')
    return F(round(10000*res.x),10000)


def tail_budget(alpha,beta,R,end):
    """A variance bound of width 9 gives the same 43/16 remainder."""
    lam=1-beta;cuts={F(R),F(end)}
    for a in (F(1),alpha,beta):
        cuts.update(F(k)/a for k in range(math.ceil(a*R),math.floor(a*end)+1))
    cuts=sorted(cuts)
    rational=F(43,32)*(F(1,R*R)-F(1,end*end))+8*lam/end
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2
        b=lam*(6-2*math.floor(x)+12*math.floor(alpha*x)+4*math.floor(beta*x))
        rational+=b*(1/l-1/r)
    coef=2*lam*(1-6*alpha-2*beta)
    value=rational+coef*log_iv(F(end,R))
    return value,dict(rational=str(rational),log_coefficient=str(coef),
                      log_argument=str(F(end,R)),small_tail=str(8*lam/end),cells=len(cuts)-1)


def run_one(alpha,beta,R=40,tail_end=400):
    assert 0<alpha<=beta<F(1,2) and alpha<=F(1,8)
    cuts=geometry(alpha,beta,R);pieces=[]
    for l,r in zip(cuts,cuts[1:]):
        pieces.extend(lower_envelope(l,r,candidate_lines(l,r,alpha,beta)))
    tail,tail_info=tail_budget(alpha,beta,R,tail_end)
    A=area(pieces)+tail;s=choose_s(alpha,beta);B=real_lower(alpha,beta,s)
    bands={}
    for name,lo,hi in [('x_lt_2',F(0),F(2)),('x_2_3',F(2),F(3)),('x_3_6',F(3),F(6)),('x_ge_6',F(6),F(R))]:
        part=[(max(l,lo),min(r,hi),n,a,b) for l,r,n,a,b in pieces if max(l,lo)<min(r,hi)]
        bands[name]=str(area(part))
    row=dict(alpha=str(alpha),beta=str(beta),lambda_=str(1-beta),cutoff=R,
             A_interval=outward_decimal(A),A_float=float(A.hi),tail_info=tail_info,
             tail_interval=outward_decimal(tail),test_s=str(s),tail_end=tail_end,
             B_interval=outward_decimal(B),B_float=float(B.lo),
             budget_obstruction_interval=outward_decimal(A+B),gap_float=float((A+B).lo),
             base_cells=len(cuts)-1,envelope_pieces=len(pieces),bands=bands,
             pieces=[[str(v) for v in p] for p in pieces])
    print(json.dumps({k:v for k,v in row.items() if k!='pieces'}),flush=True)
    return row


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--alpha',default='1/24')
    parser.add_argument('--multipliers',default='1,2,3,4,5,6');parser.add_argument('--cutoff',type=int,default=40)
    parser.add_argument('--tail-end',type=int,default=400)
    parser.add_argument('--out',default='two_prefix_budget.json');args=parser.parse_args()
    rows=[];path=Path(__file__).with_name(args.out);a=F(args.alpha)
    for m in map(F,args.multipliers.split(',')):
        rows.append(run_one(a,a*m,args.cutoff,args.tail_end))
        path.write_text(json.dumps(dict(status='written bounds and rational certificates, not a Lean proof',rows=rows),indent=2),encoding='utf-8')
