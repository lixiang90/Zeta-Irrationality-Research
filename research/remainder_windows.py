"""Exact content versus existing local bounds and their leading envelopes.

Projection and third-layer columns are finite lower bounds. The continuous
inner envelope discards finite O(1) terms and is NOT a finite lower bound.
"""
import json
import math
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq, fmpq_poly
from sympy import primerange

from global_envelope import counts, psi_coefficients, normalization_cost, third_window, six_pole_cost
from joint_outer_strong import components
from layer_uniform_rank import rank_cap_limit
from layer_inner_extension import bound
from joint_exact import content
from joint_padic import val

HERE=Path(__file__).parent


def continuous_cost(x,alpha):
    q=math.floor(x);qp=math.floor(alpha*x);norm=normalization_cost(x,alpha)
    cand=[]
    if x>=3:
        cs=counts(x,alpha);u=(1-alpha)*x
        for k in range(-2*q-8,8*q+21):
            s=sum(a*b for a,b in zip(psi_coefficients(q,qp,k),cs))
            cand.append((norm-u*k+2*s,f'inner:{k}'))
    if alpha*x<F(1,2):
        base,r,z=components(x,alpha,True)
        cand.extend([(base+r,'rank'),(base+z,'zero'),(base+rank_cap_limit(x,alpha),'projection')])
    w=third_window(alpha)
    if w and w[0]<=x<=w[1]:
        cand.append((six_pole_cost(x,alpha),'six_pole'))
    assert cand
    return min(cand)


def third_finite(K,N,p):
    a=3*p-1-K
    if p>=11 and (p+2)//3<=N<=3*p//8 and 0<=a<=N:
        d=3*N-p+1;b=max(0,min(a,2*d-a))
        return 48*N-24*p+22+a-b
    return None


def harmonic_flags(p,q):
    # These factors are only a warning of possible exceptional behavior.
    # Their presence alone does not prove a determinant rank drop.
    hs=[]
    for a in range(1,q+1):
        H=sum((F(1,j**7) for j in range(1,a+1)),F(0))
        if H.denominator%p and H.numerator%p==0:hs.append(a)
    return hs


def run_cache(filename):
    data=json.loads((HERE/filename).read_text());r=data['result']
    K=r['K'];[(N,beta)]=r['profile'];assert beta==8 and r['h']==K-N
    P=fmpq_poly([fmpq(c) for c in data['poly']]);ct=content(P)
    assert str(ct)==data['content']
    alpha=F(N,K);rows=[]
    for p in primerange(max(7,2*N+1,math.isqrt(2*K)+1),K//2+1):
        x=F(K,p);q=K//p
        if x>20:continue
        actual=val(ct,p);projection=bound(K,N,p);third=third_finite(K,N,p)
        known=max(projection,third if third is not None else projection)
        assert actual>=known
        E,name=continuous_cost(x,alpha)
        leading=p*(normalization_cost(x,alpha)-E)
        residual=F(actual)-leading
        rows.append(dict(p=p,q=q,x=str(x),actual_gauss=actual,projection_lower_bound=projection,
                         third_lower_bound=third,best_available_finite_lower_bound=known,
                         finite_residual=actual-known,leading_candidate=name,
                         leading_raw_estimate=str(leading),leading_residual=str(residual),
                         residual_over_K=str(residual/K),harmonic_zero_indices=harmonic_flags(p,q)))
    groups=defaultdict(list)
    for t in rows:groups[t['q']].append(t)
    summary=[]
    for q,rs in sorted(groups.items()):
        ordinary=[r for r in rs if not r['harmonic_zero_indices']]
        if ordinary:
            residuals=[F(r['leading_residual']) for r in ordinary]
            summary.append(dict(q=q,count=len(rs),unflagged_count=len(ordinary),
                                min_leading_residual=str(min(residuals)),max_leading_residual=str(max(residuals)),
                                max_residual_over_K=str(max(residuals)/K)))
    return dict(source=filename,K=K,N=N,alpha=str(alpha),score=r['score'],score_ball=r.get('score_ball'),
                arithmetic_exact=r['arithmetic_exact'],real_exact_numeric=r['real_exact_numeric'],
                content_recomputed=True,rows=rows,summary=summary)


def exception43():
    from coupled_pencil import normalized_pencil
    from distribution_modular import smith_mod
    rows=[]
    for delta in [0,1]:
        d=normalized_pencil(120,3,43,8,harmonic_deformation=delta)
        ss,censored,_=smith_mod(d['A'],43,8)
        assert not censored and d['B_min']>=max(ss)
        rows.append(dict(delta=delta,original_functional=delta==0,tropical=d['tropical'],
                         B_min=d['B_min'],smith={str(s):ss.count(s) for s in sorted(set(ss))},
                         max_smith=max(ss),censored=censored,gauss_certified=True,
                         gauss=d['tropical']+sum(ss),projection=bound(120,3,43)))
    assert rows[0]['gauss']==-599 and rows[1]['gauss']==-630
    (HERE/'remainder_exception43.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    return rows


def main():
    files=['joint_cache_K40_N1.json','joint_cache_K80_N2.json',
           'remainder_cache_K120_N3.json','remainder_cache_K160_N4.json',
           'joint_cache_K40_N3.json','joint_cache_K80_N6.json']
    rows=[run_cache(f) for f in files]
    result=dict(status='Exact finite contents; leading-envelope residuals are diagnostics, not finite/asymptotic gain certificates.',
                rows=rows,exception43=exception43())
    (HERE/'remainder_windows.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    for r in rows:
        print(json.dumps({k:r[k] for k in ['K','N','score','summary']}),flush=True)


if __name__=='__main__':main()
