"""Exact-check MILP candidates for residue-balanced pole deletion sets.

MILP only selects a candidate. All integrality, residue equalities, contents,
and determinant values are subsequently checked exactly. No solver status is
used to assert impossibility or an asymptotic existence theorem.
"""
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from flint import fmpq,fmpq_poly,arb,ctx
from joint_exact import (Dcache,entries_from_polynomial,determinant_pole_split,
                         evaluate_primitive_ball)
from two_prefix_outer import vp


def choose(K,N,M,primes):
    js=list(range(N+1,K+1));rows=[[1]*len(js)];rhs=[M-N]
    for p in primes:
        for c in range((p+1)//2):
            row=[int(min(j%p,(-j)%p)==c) for j in js]
            rows.append(row);rhs.append(sum(row[:M-N]))
    mat=np.array(rows,dtype=float);rhs=np.array(rhs,dtype=float)
    # Decreasing real-cost surrogate: zeros far to the right are cheaper.
    costs=np.array([math.log1p((.47*K/j)**2) for j in js])
    ans=milp(costs,integrality=np.ones(len(js)),bounds=Bounds(0,1),
             constraints=LinearConstraint(mat,rhs,rhs),options={'time_limit':30})
    if ans.x is None:return dict(found=False,status=str(ans.message))
    xs=[int(round(x)) for x in ans.x]
    assert all(x in (0,1) for x in xs)
    assert all(sum(a*x for a,x in zip(row,xs))==int(b) for row,b in zip(rows,rhs))
    chosen=list(range(1,N+1))+[j for j,x in zip(js,xs) if x]
    assert len(chosen)==M and chosen==sorted(set(chosen))
    for p in primes:
        for c in range((p+1)//2):
            assert sum(min(j%p,(-j)%p)==c for j in chosen)==sum(min(j%p,(-j)%p)==c for j in range(1,M+1))
    return dict(found=True,set=chosen,solver_status=str(ans.message),
                changed=chosen!=list(range(1,M+1)),residue_equalities=len(rows))


def experiment(K,N,chosen):
    M=len(chosen);h=K-M;t=fmpq_poly([0,1]);DA=fmpq_poly([1]);T=fmpq_poly([1])
    for j in range(1,K+1):
        if j in chosen:DA*=t+j*j
        else:T*=t+j*j
    W=Dcache(N)**6*DA**2;aa,bb=entries_from_polynomial(K,W,h)
    P=determinant_pole_split(aa,bb,T,h);ct,lv,bits=evaluate_primitive_ball(P)
    kappa=fmpq(math.factorial(K),math.factorial(N)**6*math.prod(chosen)**2)
    detq=fmpq(1)
    for i in range(1,h):detq*=fmpq(2,math.factorial(2*i))
    S=kappa**(2*h)*detq**2
    with ctx.workprec(160):
        lc=arb(S*ct).log()/K**2;score=lv/K**2;real=score+lc
        return dict(K=K,N=N,M=M,h=h,set=chosen,degree=P.degree(),
                    score=float(score.mid()),score_ball=score.str(30),
                    real=float(real.mid()),real_ball=real.str(30),
                    arithmetic_gain=float(lc.mid()),arithmetic_gain_ball=lc.str(30),
                    content=str(ct),normalized_content=str(S*ct),
                    primitive_polynomial=[str(c) for c in P/ct])


def main():
    folder=Path(__file__).parent;rows=[];cache={}
    jobs=[(48,2,8,[13]),(48,2,8,[13,17]),(48,2,8,[13,17,19]),
          (96,4,16,[17,19,23]),(96,4,16,[17,19,23,29,31]),
          (96,4,16,[17,19,23,29,31,37])]
    for K,N,M,primes in jobs:
        ans=choose(K,N,M,primes);row=dict(K=K,N=N,M=M,primes=primes,selection=ans)
        if ans['found']:
            key=(K,N,tuple(ans['set']))
            if key not in cache:cache[key]=experiment(K,N,ans['set'])
            result=cache[key];row['result']=result
            old=next(r for r in json.loads((folder/f'two_prefix_outer_K{K}.json').read_text())['rows']
                     if r['M']==M and r['h']==K-M)
            assert result['real']<=old['real']+1e-12
            row['real_change']=result['real']-old['real']
            row['arithmetic_change']=result['arithmetic_gain']-old['arithmetic_gain']
            row['score_change']=result['score']-old['score']
            row['protected_prime_actual_changes']=[dict(p=p,change=vp(fmpq(result['normalized_content'])/fmpq(old['normalized_content']),p)) for p in primes]
        rows.append(row)
        (folder/'residue_balanced_zeros.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in row.items() if k!='result'}),flush=True)


if __name__=='__main__':main()
