"""Candidate inner-window bound: K=4p+r, N<=r, 2r+6N<=p.

The formula is a CONJECTURE until a uniform local argument is supplied.
Each recorded original-functional valuation is certified for the full X
polynomial when B_min >= the largest Smith exponent of normalized A.
"""
import argparse
import json
import time
from pathlib import Path
from fractions import Fraction as F
from coupled_pencil import normalized_pencil
from distribution_modular import smith_mod
from remainder_windows import continuous_cost
from global_envelope import normalization_cost


def fixed_weights(tag):
    i=tag['i']
    if tag['c']==0:return [-7,-3,1,2][i]
    if tag['delta']:return [-7,-5,-3,-1,1,2,2,2][i]
    if tag['ell']==9:return 2*i-15
    assert tag['ell']==8
    return [ -14,-12,-10,-8,-6,-4,-1,-1 ][i]


def fixed_normalization(d,p,target_precision=6):
    s=[fixed_weights(t) for t in d['tags']]
    rows=[v//2 for v in s];cols=[v-u for v,u in zip(s,rows)]
    modulus=p**target_precision
    def convert(M):
        ans=[]
        for i,row in enumerate(M):
            rr=[]
            for j,a in enumerate(row):
                change=d['rows'][i]+d['cols'][j]-rows[i]-cols[j]
                assert d['precision']+min(change,0)>=target_precision
                if change<0:
                    assert a%p**(-change)==0
                    a//=p**(-change)
                else:a*=p**change
                rr.append(a%modulus)
            ans.append(rr)
        return ans
    return convert(d['A']),convert(d['B']),sum(s)


def check(K,N,p,precision=10):
    r=K-4*p
    assert 1<=N<=r and 2*r+6*N<=p and p*p>2*K
    d=normalized_pencil(K,N,p,precision)
    ss,censored,_=smith_mod(d['A'],p,precision)
    assert not censored and d['B_min']>=max(ss)
    actual=d['tropical']+sum(ss)
    predicted=59*N-28*p-7*r+23
    E,name=continuous_cost(F(K,p),F(N,K))
    lead=p*(normalization_cost(F(K,p),F(N,K))-E)
    A,B,tau=fixed_normalization(d,p)
    fs,fc,_=smith_mod(A,p,6)
    assert not fc
    assert tau==54*N-28*p-7*r+21 and tau+sum(fs)==actual
    fixed_counts={str(s):fs.count(s) for s in sorted(set(fs))}
    h=K-N
    zero_cols=[j for j in range(h) if all(A[i][j]%p==0 for i in range(h))]
    row=dict(K=K,N=N,p=p,r=r,precision=precision,tropical=d['tropical'],
             B_min=d['B_min'],max_smith=max(ss),smith={str(s):ss.count(s) for s in sorted(set(ss))},
             gauss_certified=True,gauss=actual,predicted=predicted,slack=actual-predicted,
             leading_candidate=name,leading_raw=str(lead),leading_residual=str(F(actual)-lead))
    row.update(fixed_tau=tau,fixed_smith=fixed_counts,
               first_nullity=sum(s>=1 for s in fs),second_nullity=sum(s>=2 for s in fs),
               fixed_integrality_checked=True,zero_columns=len(zero_cols),
               expected_first_nullity=3*N+1,expected_second_nullity=2*N+1)
    row['two_layer_target_holds']=(row['first_nullity']>=3*N+1 and row['second_nullity']>=2*N+1)
    return row


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--large',action='store_true');args=ap.parse_args()
    if args.large:
        jobs=[(120,3,29),(280,7,67),(400,10,97)]
        name='eight_pole_large.json'
    else:
        jobs=[]
        for p in [11,13,17,19,23,29,31,37,41,43,47]:
            for N in range(1,p//8+1):
                lo=N;hi=(p-6*N)//2
                for r in sorted({lo,(lo+hi)//2,hi}):
                    jobs.append((4*p+r,N,p))
        name='eight_pole_grid.json'
    out=Path(__file__).with_name(name)
    prior=json.loads(out.read_text()) if out.exists() else []
    cache={(x['K'],x['N'],x['p']):x for x in prior};rows=[];start=time.time()
    for job in jobs:
        row=cache.get(job)
        if row is None or 'fixed_tau' not in row:row=check(*job)
        rows.append(row)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        if row['slack']<0 or len(rows)%10==0 or args.large:
            print(json.dumps(row)+f' cases={len(rows)} seconds={time.time()-start:.1f}',flush=True)
    print('completed',len(rows),'violations',sum(x['slack']<0 for x in rows),
          'equalities',sum(x['slack']==0 for x in rows),'seconds',time.time()-start,flush=True)


if __name__=='__main__':main()
