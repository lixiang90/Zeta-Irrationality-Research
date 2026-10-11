"""All-coefficient outer-prime lower bounds for W=D_N^6 D_M^2.

The lower bound uses a CRT pole basis and an exceptional-moment rank loss.
Exact rational contents and Arb values supply finite checks, not its proof.
"""
import argparse
import json
from pathlib import Path
from math import prod
from flint import fmpq, fmpq_poly, arb, ctx
from sympy import primerange
from joint_exact import (entries, determinant_tail_split, content, norm_scalar,
                         evaluate_primitive_ball)


def vp(q,p):
    q=fmpq(q)
    if not q:
        raise ValueError('valuation of zero')
    value=0;a=abs(int(q.p));b=int(q.q)
    while a%p==0:a//=p;value+=1
    while b%p==0:b//=p;value-=1
    return value


def outer_bound(K,N,M,h,p):
    assert 1<=N<=M<K and h>=K-M
    assert p>=7 and 3*p>K and p*p>2*K and p>2*M
    weights=[];classes=[]
    for c in range(1,(p+1)//2):
        poles=[j for j in range(1,K+1) if j%p in [c,p-c]]
        ell=len(poles);n=sum(j>p for j in poles)
        d=ell-int(c<=M)
        if not d:continue
        assert 0<=n<=d
        local=[min(0,2*i+6*int(c<=N)+2*int(c<=M)-ell-6) for i in range(n)]+[0]*(d-n)
        weights+=local
        classes.append(dict(c=c,ell=ell,big=n,surviving=d,twice_weights=local))
    q=K//p;weights +=[-(2*q-1)]*q
    weights +=[0]*(h-(K-M))
    assert len(weights)==h
    r=min(h,max(0,2*h+6*N+2*M-K-3*p+3))
    z=sum(w==0 for w in weights);base=sum(weights)
    return dict(p=p,base=base,moment_rank=r,zero_weights=z,
                lower=base-min(r,z),twice_weights=weights,classes=classes)


def experiment(K,N,M,h):
    profile=[(N,6),(M,2)]
    aa,bb=entries(K,profile,h)
    P=determinant_tail_split(aa,bb,K,M,h)
    ct,lv,bits=evaluate_primitive_ball(P)
    scale=norm_scalar(K,profile,h);normalized_content=ct*scale
    with ctx.workprec(160):
        logc=arb(normalized_content).log()
        score=lv/K**2;arithmetic=logc/K**2;real=(lv+logc)/K**2
        row=dict(K=K,N=N,M=M,h=h,degree=P.degree(),score=float(score.mid()),
                 score_ball=score.str(30),arithmetic_gain=float(arithmetic.mid()),
                 arithmetic_gain_ball=arithmetic.str(30),real=float(real.mid()),real_ball=real.str(30),
                 content=str(ct),normalized_content=str(normalized_content),
                 primitive_polynomial=[str(c) for c in P/ct],local=[])
    for p in (primerange(7,2*K+1) if h>=K-M else []):
        if 3*p<=K or p*p<=2*K or p<=2*M:continue
        bound=outer_bound(K,N,M,h,p)
        actual=vp(ct,p);bound.update(actual=actual,slack=actual-bound['lower'])
        assert actual>=bound['lower'],(K,N,M,h,p,actual,bound)
        simple=(2*p>K+M and p<=K-M and h==K-N)
        if simple:
            assert bound['base']==-9*(K-p)+6*N+2*M-1
        bound['simple_window']=simple
        row['local'].append(bound)
    print(json.dumps(dict(K=K,N=N,M=M,h=h,degree=P.degree(),score=row['score'],
                          certified_primes=len(row['local']),
                          exact_lower_bounds=sum(r['slack']==0 for r in row['local']))),flush=True)
    return row


def run(scale):
    K=24*scale;N=scale;rows=[]
    # Joint variation of endpoint and h; every endpoint includes its degree
    # matched dimension and the same h=K-N comparison.
    jobs=[(K,N,M,h) for M in range(N,6*N+1,N) for h in sorted({K-M,K-N})]
    if scale==1:
        jobs +=[(K,N,M,K) for M in [1,2,3,4]]
    output=Path(__file__).with_name(f'two_prefix_outer_K{K}.json')
    for job in jobs:
        rows.append(experiment(*job))
        output.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    return rows


def controls(scale):
    K=24*scale;N=scale
    rows=[experiment(K,N,N,K-a*N) for a in range(1,7)]
    Path(__file__).with_name(f'two_prefix_controls_K{K}.json').write_text(
        json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    return rows


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--scale',type=int,default=1)
    parser.add_argument('--controls',action='store_true')
    args=parser.parse_args();controls(args.scale) if args.controls else run(args.scale)
