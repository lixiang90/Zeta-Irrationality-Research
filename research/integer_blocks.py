"""Integer-valued consecutive root blocks and budgeted local divisibility.

W = D_N^8 product B_(a,L)^2. Disjoint blocks lie to the right of N.
Normalization uses block lengths, not the product of selected pole labels.
"""
import argparse
import heapq
import json
import math
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx
from sympy import primerange
from joint_exact import (Dcache,entries_from_polynomial,determinant_pole_split,
                         evaluate_primitive_ball)
from two_prefix_outer import vp


def roots(N,blocks):
    out=list(range(1,N+1))
    for a,L in blocks:
        assert a>=N and L>=1
        out+=list(range(a+1,a+L+1))
    assert len(out)==len(set(out))
    return sorted(out)


def polynomials(K,N,blocks):
    selected=roots(N,blocks);assert max(selected)<K+1 and len(selected)<K
    t=fmpq_poly([0,1]);W=Dcache(N)**8;T=fmpq_poly([1])
    for a,L in blocks:W*=(Dcache(a+L)//Dcache(a))**2
    for j in range(1,K+1):
        if j not in selected:T*=t+j*j
    return selected,W,T


def scalar(K,N,blocks,h):
    denominator=math.factorial(N)**8
    for a,L in blocks:denominator*=math.factorial(L)**2
    kappa=fmpq(math.factorial(K),denominator);detq=fmpq(1)
    for i in range(1,h):detq*=fmpq(2,math.factorial(2*i))
    return kappa**(2*h)*detq**2


def local_bound(K,N,selected,p):
    M=len(selected);h=K-M;assert p>=7 and p*p>2*K
    bucket=lambda j:min(j%p,(-j)%p)
    full=[0]*((p+1)//2);core=full.copy();removed=full.copy()
    for j in range(1,K+1):full[bucket(j)]+=1
    for j in range(1,N+1):core[bucket(j)]+=1
    for j in selected:removed[bucket(j)]+=1
    weights=[]
    for c in range(1,len(full)):
        ell,m=full[c],removed[c];eta=6*core[c]+2*m
        big=sum(j>p and j not in selected and bucket(j)==c for j in range(1,K+1))
        weights +=[min(0,2*i+eta-ell-6) for i in range(big)]
        weights +=[0]*(ell-m-big)
    q,qn,qm=full[0],core[0],removed[0]
    weights +=[min(0,4*i+12*qn+4*qm-2*q+1) for i in range(q-qm)]
    assert len(weights)==h
    rank=min(h,max(0,K+6*N-3*p+3))
    residue=sum(weights)-min(rank,weights.count(0));allocation=None
    offsets=[1+12*qn+4*qm-2*q]+[6*core[c]+2*removed[c]-full[c]-6 for c in range(1,len(full))]
    if p*p>2*K+12*N+4:
        heap=[(b,c) for c,b in enumerate(offsets)];heapq.heapify(heap);allocation=0
        for _ in range(h):
            b,c=heapq.heappop(heap);allocation+=b;heapq.heappush(heap,(b+(4 if c==0 else 2),c))
    return dict(p=p,residue=residue,allocation=allocation,
                lower=max(residue,allocation) if allocation is not None else residue,
                offsets=offsets)


def ilog(p,x):
    n=0
    while x>=p:x//=p;n+=1
    return n


def budget(K,N,selected,S,ct):
    h=K-len(selected);records=[]
    # For our scan N <= K/8, moments are p-integral for p>2K.
    assert N<=K//8
    with ctx.workprec(160):
        lower_log=arb(0)
        for p in primerange(2,2*K+1):
            if p>=7 and p*p>2*K:
                r=local_bound(K,N,selected,p);lower=r['lower']+vp(S,p)
            else:
                r=dict(p=p,source='integer_valued_small_prime')
                lower=-8*h*ilog(p,4*K+12*N+4)-h*vp(fmpq(720),p)
            actual=vp(S*ct,p);assert actual>=lower,(K,N,selected,p,actual,lower)
            lower_log+=lower*arb(p).log()
            records.append(dict(p=p,lower=lower,actual=actual,slack=actual-lower))
        return lower_log/K**2,records


def experiment(K,N,blocks,save_poly=False):
    selected,W,T=polynomials(K,N,blocks);h=T.degree()
    aa,bb=entries_from_polynomial(K,W,h);P=determinant_pole_split(aa,bb,T,h)
    ct,lv,bits=evaluate_primitive_ball(P);S=scalar(K,N,blocks,h)
    with ctx.workprec(160):
        lc=arb(S*ct).log()/K**2;score=lv/K**2;real=score+lc
        lb,local=budget(K,N,selected,S,ct)
        row=dict(K=K,N=N,blocks=blocks,M=len(selected),h=h,degree=P.degree(),
                 score=float(score.mid()),score_ball=score.str(30),
                 real=float(real.mid()),real_ball=real.str(30),
                 arithmetic_gain=float(lc.mid()),arithmetic_gain_ball=lc.str(30),
                 certified_arithmetic_lower=float(lb.mid()),certified_arithmetic_lower_ball=lb.str(30),
                 finite_score_upper_ball=(real-lb).str(30),
                 content=str(ct),scalar=str(S),local=local)
    if save_poly:row['primitive_polynomial']=[str(c) for c in P/ct]
    return row


def run(K,N,lengths,starts):
    path=Path(__file__).with_name(f'integer_blocks_K{K}.json')
    rows=json.loads(path.read_text())['rows'] if path.exists() else []
    seen={(r['K'],r['N'],tuple(tuple(b) for b in r['blocks'])) for r in rows}
    for L in lengths:
        for a in starts:
            if a<N or a+L>K:continue
            key=(K,N,((a,L),))
            if key in seen:continue
            row=experiment(K,N,[(a,L)]);rows.append(row);seen.add(key)
            path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
            print(json.dumps({k:row[k] for k in ('K','N','blocks','h','score')}),flush=True)
    return rows


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=24);p.add_argument('--N',type=int,default=1)
    p.add_argument('--lengths',default='1,2,3,4,5,6,7,8');p.add_argument('--starts',default='all')
    a=p.parse_args();starts=range(a.N,a.K) if a.starts=='all' else map(int,a.starts.split(','))
    run(a.K,a.N,list(map(int,a.lengths.split(','))),list(starts))
