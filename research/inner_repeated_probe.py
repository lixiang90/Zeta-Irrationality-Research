"""Finite tests of a conjectural repeated inner-window formula.

Base leading estimate: (14q-2)N-7K.
Candidate improvement: 5N+6q-1. No uniform theorem is asserted.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from coupled_pencil import normalized_pencil
from distribution_modular import smith_mod
from remainder_windows import continuous_cost
from global_envelope import normalization_cost


def check(p,q,N,r=3):
    K=q*p+r
    assert N<=r and 2*r+6*N<=p and p*p>2*K
    d=normalized_pencil(K,N,p,12);ss,censored,_=smith_mod(d['A'],p,12)
    assert not censored and d['B_min']>=max(ss)
    actual=d['tropical']+sum(ss)
    E,name=continuous_cost(F(K,p),F(N,K))
    lead=p*(normalization_cost(F(K,p),F(N,K))-E)
    base=(14*q-2)*N-7*K
    assert lead==base
    return dict(K=K,N=N,p=p,q=q,r=r,certified_full_polynomial=True,gauss=actual,
                residual=actual-base,candidate_residual=5*N+6*q-1,
                candidate_slack=actual-base-(5*N+6*q-1),
                B_min=d['B_min'],smith_max=max(ss),leading_candidate=name)


if __name__=='__main__':
    rows=[];out=Path(__file__).with_name('inner_repeated_certificates.json')
    for p,q,N in [(23,q,N) for q in range(4,9) for N in [1,2]]+[
        (31,7,1),(31,7,2),(31,8,1),(31,8,2),(41,7,2)]:
        r=check(p,q,N);rows.append(r);out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps(r),flush=True)
