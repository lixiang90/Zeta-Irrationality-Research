"""Stronger outer-prime bound, with exact rational integration and finite checks.

The accompanying joint_divisibility.md supplies the mathematical argument.
This script does not certify the entire asymptotic/Lean normalization chain.
"""
import argparse,json,math,sys,time
from fractions import Fraction as F
from pathlib import Path
from sympy import primerange
from joint_exact import experiment
from joint_padic import val

GROWTH=Path(__file__).resolve().parents[1]/"Zeta7Formal/scripts/growth"
sys.path.insert(0,str(GROWTH))
from table_b8_39 import bcoef,ccount,Jc_fast


def components(x,alpha,strong):
    q=math.floor(x);u=(1-alpha)*x
    def go(a,d):
        return sum(min(F(0),i+(4 if strong else 3)*d-F(2*q+a+6,2))
                   for i in range(max(0,2*q+a-2)))
    s=sum(bcoef(lambda a:bcoef(lambda d:go(a,d))[j])[i]
          *ccount(x-q,alpha*x-math.floor(alpha*x),i,j)
          for i in range(3) for j in range(3))
    def count_negative(a,d):
        return sum(i+4*d-F(2*q+a+6,2)<0 for i in range(max(0,2*q+a-2)))
    negatives=sum(bcoef(lambda a:bcoef(lambda d:count_negative(a,d))[j])[i]
          *ccount(x-q,alpha*x-math.floor(alpha*x),i,j)
          for i in range(3) for j in range(3))
    return (-2*u*q+2*Jc_fast(u)-2*s,
            max(F(0),(1+6*alpha)*x-(3 if strong else 2)),u-negatives)


def outer(x,alpha,strong,cap=False):
    base,rank,z=components(x,alpha,strong)
    return base+(min(rank,z) if cap else rank)


def integral(alpha,strong,cap=False):
    lo=1/(2*(1-alpha));hi=F(3);c=1+6*alpha
    # All floor, class-overlap and rank breakpoints; extra points are harmless.
    steps=[F(1,2),1/(2*alpha),1/(2*(1-alpha)),1/(1-alpha),1/(1+alpha),F(2)/c,F(3)/c]
    cuts={lo,hi}
    for step in steps:
        for k in range(math.ceil(lo/step),math.floor(hi/step)+1):cuts.add(k*step)
    if cap:
        initial=sorted(cuts)
        for l,r in zip(initial,initial[1:]):
            x0=l+(r-l)/4;x1=l+3*(r-l)/4
            _,r0,z0=components(x0,alpha,strong);_,r1,z1=components(x1,alpha,strong)
            slope=((r1-z1)-(r0-z0))/(x1-x0)
            if slope:
                root=x0-(r0-z0)/slope
                if l<root<r:cuts.add(root)
    cuts=sorted(cuts);pieces=[];total=F(0)
    for l,r in zip(cuts,cuts[1:]):
        xs=[l+(r-l)*F(k,8) for k in range(1,8)]
        ys=[outer(x,alpha,strong,cap) for x in xs]
        a=(ys[1]-ys[0])/(xs[1]-xs[0]);b=ys[0]-a*xs[0]
        assert all(y==a*x+b for x,y in zip(xs,ys))
        area=a*(1/l-1/r)+b/2*(1/l**2-1/r**2)
        total+=area;pieces.append([str(z) for z in [l,r,a,b,area]])
    return total,pieces


def delta_bound(K,N,p):
    assert N<=K//8 and 3*p>K and 2*K<p*p and p>=7
    h=K-N;q=K//p
    weight2=0;negative_count=0
    for c in range(1,(p+1)//2):
        ell=sum(j%p in (c,p-c) for j in range(1,K+1))
        nb=sum(j%p in (c,p-c) for j in range(p+1,K+1))
        d=int(c<=N)
        assert nb==max(0,ell-2)
        ws=[min(0,2*i+8*d-ell-6) for i in range(nb)]
        weight2+=sum(ws);negative_count+=sum(w<0 for w in ws)
    # Crude but uniform O(1) contribution of the zero residue class.
    zero=-q*(2*q-1)
    rank=min(h,max(0,K+6*N-3*p+3))
    z=h-negative_count-q
    loss=min(rank,z)
    return weight2+zero-loss,dict(weight2=weight2,zero=zero,rank=rank,zero_weights=z,rank_loss=loss)


def finite_check():
    rows=[];start=time.time();out=Path(__file__).with_suffix('.json')
    for K in [16,24,32,40,48,56,64]:
        for N in range(1,K//8+1):
            _,P,*_=experiment(K,[(N,8)],K-N)
            for p in primerange(max(7,K//3+1),2*(K-N)+1):
                if 2*K>=p*p:continue
                actual=min(val(c,p) for c in P)
                bound,parts=delta_bound(K,N,p)
                assert actual>=bound,(K,N,p,actual,bound,parts)
                rows.append(dict(K=K,N=N,p=p,actual=actual,bound=bound,slack=actual-bound,**parts))
            print(f'K={K} N={N}: {len(rows)} exact checks, {time.time()-start:.1f}s',flush=True)
            out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
    return rows


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--finite',action='store_true');args=ap.parse_args()
    result=[]
    for alpha in [F(1,40),F(3,40),F(1,8)]:
        old,op=integral(alpha,False);new,np=integral(alpha,True);capped,cp=integral(alpha,True,True)
        r=dict(alpha=str(alpha),old=str(old),new=str(new),gain=str(old-new),
               old_float=float(old),new_float=float(new),gain_float=float(old-new),
               capped=str(capped),capped_float=float(capped),total_gain=str(old-capped),
               total_gain_float=float(old-capped),cap_extra_gain=str(new-capped),pieces=cp)
        result.append(r);print(json.dumps({k:v for k,v in r.items() if k!='pieces'}),flush=True)
    Path(__file__).with_name('joint_outer_integrals.json').write_text(json.dumps(result,indent=2))
    if args.finite:finite_check()
