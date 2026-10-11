"""Exact comparison with the existing inner table on 3 <= K/p <= 4.

The local-basis argument only requires p>2N and p^2>2K; it does not require
K<3p. This script uses that extension, with all finite O(1) terms retained
in its determinant checks. The global Lean chain is not certified here.
"""
import json,pickle,math
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq,fmpq_poly
from layer_uniform_rank import rank_cap,rank_cap_limit
from joint_outer_strong import components,GROWTH
from table_b8_39 import Ein,al
from joint_padic import val
from layer_projection import local_data,modrank

def bound(K,N,p):
    assert p>2*N and 2*K<p*p and p>=7
    h=K-N;q=K//p;base=-q*(2*q-1);negative=q
    for c in range(1,(p+1)//2):
        ell=sum(j%p in (c,p-c) for j in range(1,K+1));nb=max(0,ell-2)
        ws=[min(0,2*i+8*int(c<=N)-ell-6) for i in range(nb)]
        base+=sum(ws);negative+=sum(w<0 for w in ws)
    z=h-negative;r=min(h,max(0,K+6*N-3*p+3));s=rank_cap(K,N,p)
    return base-min(r,z,s)


def inner_gain(lo=F(3),hi=F(4)):
    alpha=F(1,40);assert al==alpha
    assert F(3)<=lo<hi<=1/(2*alpha)
    prior=pickle.loads((GROWTH/'pieces_b8_39.pkl').read_bytes())
    prior=[(max(l,lo),min(r,hi),k,a,b) for l,r,k,a,b in prior if l<hi and r>lo]
    cuts={lo,hi}
    for l,r,k,a,b in prior:
        cuts.update([l,r])
        for t in [F(1,4),F(1,2),F(3,4)]:
            x=l+(r-l)*t;assert Ein(x,k)==a*x+b
    for step in [F(1,2),1/(2*(1-alpha)),1/(1-alpha),1/(1+alpha),1/(2*alpha)]:
        for k in range(math.ceil(lo/step),math.floor(hi/step)+1):cuts.add(k*step)
    def terms(x):
        base,r,z=components(x,alpha,True);return base,[r,z,rank_cap_limit(x,alpha)]
    def old(x):
        _,_,_,a,b=next(t for t in prior if t[0]<=x<=t[1]);return a*x+b
    initial=sorted(cuts)
    for l,r in zip(initial,initial[1:]):
        xs=[l+(r-l)/4,l+3*(r-l)/4];vals=[terms(x)[1] for x in xs]
        for i,j in [(0,1),(0,2),(1,2)]:
            v0=vals[0][i]-vals[0][j];v1=vals[1][i]-vals[1][j]
            slope=(v1-v0)/(xs[1]-xs[0])
            if slope:
                root=xs[0]-v0/slope
                if l<root<r:cuts.add(root)
    def new(x):
        base,losses=terms(x);return base+min(losses)
    initial=sorted(cuts)
    for l,r in zip(initial,initial[1:]):
        x0=l+(r-l)/4;x1=l+3*(r-l)/4;v0=old(x0)-new(x0);v1=old(x1)-new(x1)
        slope=(v1-v0)/(x1-x0)
        if slope:
            root=x0-v0/slope
            if l<root<r:cuts.add(root)
    total=F(0);pieces=[];cuts=sorted(cuts)
    for l,r in zip(cuts,cuts[1:]):
        xs=[l+(r-l)*F(k,8) for k in range(1,8)];ys=[max(F(0),old(x)-new(x)) for x in xs]
        a=(ys[1]-ys[0])/(xs[1]-xs[0]);b=ys[0]-a*xs[0]
        assert all(y==a*x+b for x,y in zip(xs,ys))
        area=a*(1/l-1/r)+b*(1/l**2-1/r**2)/2;total+=area
        if area:pieces.append([str(v) for v in [l,r,a,b,area]])
    return dict(alpha=str(alpha),interval=[str(lo),str(hi)],
                subintervals=len(cuts)-1,gain=str(total),gain_float=float(total),positive_pieces=pieces)

if __name__=='__main__':
    folder=Path(__file__).parent;rows=[]
    for file,p in [('joint_cache_K40_N1.json',11),('joint_cache_K40_N3.json',11),
                   ('joint_cache_K80_N2.json',23),('joint_cache_K80_N6.json',23)]:
        data=json.loads((folder/file).read_text());K=data['result']['K'];N=data['result']['profile'][0][0]
        P=fmpq_poly([fmpq(c) for c in data['poly']]);actual=min(val(c,p) for c in P);lower=bound(K,N,p)
        assert actual>=lower
        A,B,Y,w,tags=local_data(K,N,p)
        Z=[i for i in range(len(w)) if w[i]==0];H=[i for i in range(len(w)) if w[i]==-F(1,2)]
        rr=modrank(Y,p,Z+H,Z);assert rr<=rank_cap(K,N,p)
        # Audit the uncorrrected matrix weights beyond the old K<3p range.
        assert all(min(val(A[i,j]-Y[i,j],p),val(B[i,j],p))>=w[i]+w[j]
                   for i in range(len(w)) for j in range(len(w)))
        rows.append(dict(K=K,N=N,p=p,bound=lower,actual=actual,projected_rank=rr))
    result=dict(checks=rows,inner_improvement=inner_gain())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
