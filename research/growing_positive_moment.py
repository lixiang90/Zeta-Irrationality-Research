"""Growing-degree positivity via root supports and quadratic residuals.

Candidate search is heuristic; nonnegative primal and moment dual identities
are exact and certify global optimality whenever both pass.
"""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, arb, ctx
from discrete_positive_cone_probe import shifted_map, dot, mul
from critical_lift_probe import cross, primitive
from farey_cone_optimizer import optimize


def node(n,r):return (3*n+2+2*r)**2-(3*n+2)**2


def coefficients(p):return [p[i] for i in range(len(p))]


def eval_poly(p,x):
    v=fmpq(0)
    for a in reversed(p):v=v*x+a
    return v


def quadratic_tail_minimum(n,q,start):
    """Exact minimum of a positive-leading quadratic on nodes r>=start."""
    while q and q[-1]==0:q=q[:-1]
    assert q and q[-1]>0
    candidates={start}
    if len(q)==3:
        vertex=-q[1]/(2*q[2])
        if vertex>node(n,start):
            a,b=start,max(start+1,1)
            while node(n,b)<=vertex:b=2*b+1
            while b>a+1:
                mid=(a+b)//2
                if node(n,mid)<=vertex:a=mid
                else:b=mid
            candidates.update((a,b))
    return min((eval_poly(q,node(n,r)),r) for r in candidates)


def candidate(n,w,M,starts,infinity):
    # w even: infinity face uses w nodes, finite face uses w+1 nodes.
    roots=([0] if not infinity else [])+[r for s in starts for r in (s,s+1)]
    if len(set(roots))!=len(roots):return None
    roots.sort();d=w+3
    assert len(roots)==w+(not infinity)
    H=fmpq_poly([1])
    for r in roots:H*=fmpq_poly([-node(n,r),1])
    h=coefficients(H)
    lifted=[[fmpq(0)]*k+h for k in range(3)]
    B=[[dot(line,p) for p in lifted] for line in M]
    q=cross(B[1],B[2])
    if not any(q):return None
    q,qs=primitive(q);q=list(map(fmpq,q))
    if next(x for x in reversed(q) if x)<0:q=[-x for x in q]
    out=[dot(line,q) for line in B]
    if out[3]==0:return None
    r=-out[0]/out[3]
    P=mul(h,q)
    # H is a discrete nonnegative extreme polynomial. At its zeros Q may be negative.
    rootset=set(roots);last=max(roots,default=-1)
    checks=[(eval_poly(q,node(n,j)),j) for j in range(last+1) if j not in rootset]
    checks.append(quadratic_tail_minimum(n,q,last+1))
    minq,where=min(checks)
    primal=minq>=0
    # Three exact conditions annihilate H, yH, y^2 H and determine a dual.
    constraints=fmpq_mat([[B[1][j],B[2][j],B[3][j]] for j in range(3)])
    if not constraints.det():return None
    dual=constraints.inv()*fmpq_mat([[-B[0][j]] for j in range(3)])
    assert dual[2,0]==r
    functional=[M[0][j]+dual[0,0]*M[1][j]+dual[1,0]*M[2][j]+r*M[3][j] for j in range(d+1)]
    mu=[]
    derivative=H.derivative()
    for j in roots:
        y=node(n,j)
        quotient,rem=divmod(H,fmpq_poly([-y,1]));assert not rem
        lagrange=quotient/derivative(y)
        mu.append(dot(functional,coefficients(lagrange)))
    if infinity:
        mu.append(functional[d]-sum((a*node(n,j)**d for j,a in zip(roots,mu)),fmpq(0)))
    identity=all(functional[k]==sum((mu[i]*node(n,j)**k for i,j in enumerate(roots)),fmpq(0))
                 +(mu[-1] if infinity and k==d else 0) for k in range(d+1))
    assert identity
    dual_positive=all(a>=0 for a in mu)
    pair,scale=primitive([out[0],out[3]])
    return dict(n=n,w=w,starts=list(starts),nodes=roots,infinity=infinity,
        endpoint=str(r),sign=1 if out[3]>0 else -1,primal_positive=primal,
        quadratic_minimum_checked=str(minq),minimum_node=where,
        quadratic=list(map(str,q)),H=list(map(str,h)),polynomial=list(map(str,P)),
        output=list(map(str,out)),primitive_output=pair,primitive_scale=str(scale),
        dual_auxiliary=[str(dual[0,0]),str(dual[1,0])],dual_weights=list(map(str,mu)),
        dual_positive=dual_positive,negative_dual_nodes=[roots[i] if i<len(roots) else 'infinity'
            for i,a in enumerate(mu) if a<0],global_optimal=primal and dual_positive)


def search(n,w,M,infinity,previous=None):
    base=list(range(0 if infinity else 1,w+(not infinity),2))
    seen={}; count=0
    def get(starts):
        nonlocal count
        starts=tuple(starts)
        if starts not in seen:
            seen[starts]=candidate(n,w,M,starts,infinity);count+=1
        return seen[starts]
    # First allow each of the final two pairs to move; earlier pairs stay contiguous.
    prefix=base[:-2]
    first=base[-2] if len(base)>=2 else base[-1]
    if len(base)==1:
        seeds=[(r,) for r in range(first,first+12)]
    else:
        seeds=[tuple(prefix+[a,b]) for a in range(first,first+10) for b in range(a+2,a+14)]
    # Test near-prefix candidates first, then coordinate descent if needed.
    seeds.sort(key=lambda s:sum(s))
    best=None
    for starts in seeds:
        c=get(starts)
        if c and c['global_optimal']:
            c['searched_candidates']=count;return c
        if c and c['primal_positive']:
            if best is None or c['sign']*fmpq(c['endpoint'])>best['sign']*fmpq(best['endpoint']):best=c
    if best:
        for step in range(100):
            improved=False
            for i in range(len(base)):
                for delta in (-1,1,2):
                    s=best['starts'][:];s[i]+=delta
                    if s[0]<(0 if infinity else 1) or any(b<a+2 for a,b in zip(s,s[1:])):continue
                    c=get(s)
                    if c and c['global_optimal']:
                        c['searched_candidates']=count;return c
                    if c and c['primal_positive'] and c['sign']==best['sign'] and c['sign']*fmpq(c['endpoint'])>best['sign']*fmpq(best['endpoint']):
                        best=c;improved=True
            if not improved:break
    if best:best['searched_candidates']=count
    return best


def summary(n,w,edges):
    lower=next(e for e in edges if e['sign']==1);upper=next(e for e in edges if e['sign']==-1)
    lo=fmpq(lower['endpoint']);hi=fmpq(upper['endpoint']);assert lo<hi
    width=hi-lo;opt=optimize(F(str(lo)),F(str(hi)))
    with ctx.workprec(256):
        def rate(q):return (arb(q).log()/n).str(16)
        endpoint_rates=[]
        for e in (lower,upper):
            q=abs(e['primitive_output'][1])
            endpoint_rates.append(dict(sign=e['sign'],log_denominator_per_n=rate(q),
                log_width_times_denominator_per_n=rate(width*q)))
        return dict(n=n,w=w,lower=lower,upper=upper,
            full_cone_optimal=all(e['global_optimal'] for e in edges),
            width=str(width),log_width_per_n=rate(width),endpoint_rates=endpoint_rates,
            optimal_pair=list(opt['pair']),epsilon=str(opt['epsilon']),
            epsilon_arb=arb(fmpq(str(opt['epsilon']))).str(18),
            log_epsilon_per_n=rate(fmpq(str(opt['epsilon']))),
            minimum_internal_denominator=str(opt['Q']))


def main():
    folder=Path(__file__).parent;rows=[]
    for n,w in ((4,4),(8,8),(12,12),(16,16),(20,20),(24,24),(32,32)):
        M=shifted_map(n,w)
        edges=[]
        for infinity in (True,False):
            edge=search(n,w,M,infinity)
            if edge is None:raise RuntimeError((n,w,infinity,'no candidate'))
            edges.append(edge)
            print('edge',n,w,infinity,edge['global_optimal'],edge['starts'],edge['searched_candidates'],flush=True)
        r=summary(n,w,edges);rows.append(r)
        print('rates',n,r['log_width_per_n'],r['endpoint_rates'],r['epsilon_arb'],flush=True)
        (folder/'growing_positive_moment.json').write_text(json.dumps(dict(
            scope='Finite growing-degree cases; global optimality only where primal and full moment dual certificates both pass.',
            rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
