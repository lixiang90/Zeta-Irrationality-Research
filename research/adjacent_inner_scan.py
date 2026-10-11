"""Explore q=4 phases beyond the original narrow window.

Valuations are finite full-X certificates when the B/Smith test succeeds.
Continuous residuals are diagnostics; their O(1) terms are not new gains.
"""
import json,time,argparse
from pathlib import Path
from fractions import Fraction as F
from coupled_pencil import normalized_pencil
from distribution_modular import smith_mod
from eight_pole_probe import fixed_normalization
from global_envelope import normalization_cost
from remainder_windows import continuous_cost


def run(p,N,r,q=4):
    K=q*p+r;d=normalized_pencil(K,N,p,10)
    ss,cut,_=smith_mod(d['A'],p,10)
    assert not cut and d['B_min']>=max(ss)
    actual=d['tropical']+sum(ss)
    E,name=continuous_cost(F(K,p),F(N,K))
    lead=p*(normalization_cost(F(K,p),F(N,K))-E)
    row=dict(p=p,N=N,r=r,q=q,K=K,gauss=actual,gauss_certified=True,
        tropical=d['tropical'],B_min=d['B_min'],smith={str(s):ss.count(s) for s in sorted(set(ss))},
        leading_name=name,leading_raw=str(lead),leading_residual=str(F(actual)-lead),
        narrow_candidate=(14*q+3)*N-7*K+6*q-1,
        narrow_candidate_slack=actual-((14*q+3)*N-7*K+6*q-1))
    if q==4 and N<=r<=(p-1)//2:
        try:
            A,B,tau=fixed_normalization(d,p)
            fs,fc,_=smith_mod(A,p,6);assert not fc
            row.update(fixed_integral=True,fixed_tau=tau,
                first=sum(s>=1 for s in fs),second=sum(s>=2 for s in fs),
                fixed_smith={str(s):fs.count(s) for s in sorted(set(fs))})
        except AssertionError:row['fixed_integral']=False
    return row


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--large',action='store_true');ap.add_argument('--repeated',action='store_true');args=ap.parse_args()
    if args.repeated:
        jobs=[(31,2,r,q) for q in [3,5,6,8,10,12] for r in [2,6,15]]
        jobs += [(37,3,r,6) for r in [0,3,18]]+[(41,4,r,8) for r in [4,20]]
        name='adjacent_inner_repeated.json'
    elif args.large:
        jobs=[(p,N,r,4) for p,N in [(67,7),(97,10)] for r in [0,N-1,N,(p-6*N)//2,(p-1)//2-2*N,(p-1)//2,(p-1)//2+N,p-N,p-1]]
        name='adjacent_inner_large.json'
    else:
        jobs=[]
        for p in [29,31,37]:
            for N in [1,2,3,4]:
                for r in sorted({0,N-1,N,max(N,(p-6*N)//2),(p-1)//2-N,(p-1)//2,(p-1)//2+N,p-N,p-1}):
                    jobs.append((p,N,r,4))
        name='adjacent_inner_scan.json'
    out=Path(__file__).with_name(name);cache={}
    if out.exists():cache={(x['p'],x['N'],x['r'],x['q']):x for x in json.loads(out.read_text())}
    rows=[];start=time.time()
    for job in jobs:
        row=cache.get(job) or run(*job);rows.append(row)
        out.write_text(json.dumps(rows,indent=2))
        if len(rows)%10==0 or args.large or args.repeated:print(json.dumps(row)+f' cases={len(rows)} seconds={time.time()-start:.1f}',flush=True)
    print('completed',len(rows),'seconds',time.time()-start,flush=True)
