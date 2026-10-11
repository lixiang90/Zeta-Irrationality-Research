"""Uniform projected-rank cap from the rational generating function of p*mu.

For m=(p-1)/2 and s=(-1)^m:
  sum_{e>=0} (p mu_e mod p) z^e = -z^(6m-1)/(6(1-s z^m)^6).
Thus the pairing is a residue at infinity with denominator D_K(t)(t^m-s)^6.
The proof and the rank cap are in layer_analysis.md.
"""
import json,math,time
from pathlib import Path
from fractions import Fraction as F
from joint_outer_strong import integral,components,bcoef,ccount
from layer_projection import local_data,modrank
from joint_exact import moment
from joint_padic import residue


def rank_cap(K,N,p):
    total=0
    for c in range(N+1,(p+1)//2):
        ell=sum(j%p in (c,p-c) for j in range(1,K+1))
        nb=max(0,ell-2)
        zbad=ell-min(nb,(ell+7)//2)
        total+=2*zbad+max(0,6-ell)
    return total


def rank_cap_limit(x,alpha):
    q=math.floor(x)
    def h(a,d):
        if d:return 0
        ell=2*q+a
        zbad=ell-min(max(0,ell-2),math.ceil(F(ell+6,2)))
        return 2*zbad+max(0,6-ell)
    return sum(bcoef(lambda a:bcoef(lambda d:h(a,d))[j])[i]
               *ccount(x-q,alpha*x,i,j) for i in range(3) for j in range(3))


def improved_integral(alpha):
    old,oldpieces=integral(alpha,True,True);cuts=set()
    for ls,rs,*_ in oldpieces:
        l=F(ls);r=F(rs);cuts.update([l,r]);xs=[l+(r-l)/4,l+3*(r-l)/4]
        data=[]
        for x in xs:
            _,rank,z=components(x,alpha,True);s=rank_cap_limit(x,alpha)
            data.append([rank-s,z-s])
        for k in range(2):
            slope=(data[1][k]-data[0][k])/(xs[1]-xs[0])
            if slope:
                root=xs[0]-data[0][k]/slope
                if l<root<r:cuts.add(root)
    cuts=sorted(cuts);total=F(0);pieces=[]
    def value(x):
        base,r,z=components(x,alpha,True)
        return base+min(r,z,rank_cap_limit(x,alpha))
    for l,r in zip(cuts,cuts[1:]):
        xs=[l+(r-l)*F(k,8) for k in range(1,8)];ys=[value(x) for x in xs]
        a=(ys[1]-ys[0])/(xs[1]-xs[0]);b=ys[0]-a*xs[0]
        assert all(y==a*x+b for x,y in zip(xs,ys))
        total+=a*(1/l-1/r)+b*(1/l**2-1/r**2)/2
        pieces.append([str(t) for t in [l,r,a,b]])
    gain=old-total
    assert gain==max(F(0),15*alpha-1)**2/72
    return dict(alpha=str(alpha),previous_outer=str(old),new_outer=str(total),
                gain=str(gain),gain_float=float(gain),pieces=pieces)


def check_generating_function():
    from math import comb
    count=0
    for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
        m=(p-1)//2;s=(-1)**m
        for e in range(6*p):
            predicted=0
            if (e+1)%m==0:
                j=(e+1)//m
                if j>=6:predicted=-pow(6,-1,p)*s**j*comb(j-1,5)%p
            assert residue(moment(e),p,-1)==predicted
            count+=1
    return count


if __name__=='__main__':
    folder=Path(__file__).parent;start=time.time();checks=[];rank_checks=0
    for row in json.loads((folder/'joint_outer_strong.json').read_text()):
        K,N,p=row['K'],row['N'],row['p'];s=rank_cap(K,N,p)
        bound=row['weight2']+row['zero']-min(row['rank'],row['zero_weights'],s)
        assert row['actual']>=bound
        item=dict(K=K,N=N,p=p,rank_cap=s,bound=bound,actual=row['actual'])
        if row['rank']>0:
            _,_,Y,w,_=local_data(K,N,p)
            Z=[i for i in range(len(w)) if w[i]==0];H=[i for i in range(len(w)) if w[i]==-F(1,2)]
            rr=modrank(Y,p,Z+H,Z)
            assert rr<=s
            item['projected_rank']=rr;rank_checks+=1
        checks.append(item)
    integrals=[improved_integral(F(i,40)) for i in range(1,6)]
    result=dict(generating_function_checks=check_generating_function(),determinant_checks=len(checks),
                projected_rank_checks=rank_checks,integrals=integrals,checks=checks)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['integrals','checks']}),flush=True)
    for r in integrals:print({k:v for k,v in r.items() if k!='pieces'},flush=True)
    print('seconds',time.time()-start,flush=True)
