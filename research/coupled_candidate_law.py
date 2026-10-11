"""Test an initial Smith equality and a weaker determinant lower bound.

The equality is disproved, for example at p=53. It is retained as a
counterexample regression check. The weaker lower bound is not proved.
A rank formula for its
coefficient-extraction model is proved in the report, but identification of
the actual Schur block with that model remains open.
"""
import json,time,math
from pathlib import Path
from sympy import primerange
from coupled_pencil import normalized_pencil
from distribution_modular import smith_mod
from coupled_schur import counts

def prediction(K,N,p):
    a=3*p-K-1;d=3*N-p+1;b=max(0,min(a,2*d-a))
    assert 0<=a<=N and d>0
    cs={0:4*p-5*N-2,1:N-a,2:b,3:d-b}
    cs={str(k):v for k,v in cs.items() if v}
    tropical=38*N-21*p+19+2*a
    gauss=48*N-24*p+22+a-b
    return dict(a=a,d=d,model_rank=b,smith_counts=cs,tropical=tropical,gauss=gauss)

if __name__=='__main__':
    folder=Path(__file__).parent;rows=[];failures=[];start=time.time()
    out=Path(__file__).with_suffix('.json')
    previous=json.loads(out.read_text())['rows'] if out.exists() else []
    cache={(r['K'],r['N'],r['p']):r for r in previous}
    jobs=[]
    for p in primerange(7,62):
        for N in range(math.ceil(p/3),3*p//8+1):
            for a in range(N+1):jobs.append((3*p-1-a,N,p))
    for p in [71,83,101]:
        for N in sorted({math.ceil(p/3),3*p//8}):
            d=3*N-p+1
            for a in sorted({0,1,d-1,d,d+1,min(N,2*d-1),min(N,2*d),N}):
                if 0<=a<=N:jobs.append((3*p-1-a,N,p))
    for K,N,p in sorted(set(jobs),key=lambda x:(x[2],x[1],-x[0])):
        if (K,N,p) in cache:
            row=cache[K,N,p];rows.append(row)
            if not row['matches']:failures.append(row)
            continue
        z=normalized_pencil(K,N,p,8);slopes,censored,_=smith_mod(z['A'],p,8)
        assert not censored
        pre=prediction(K,N,p)
        row=dict(K=K,N=N,p=p,prediction=pre,tropical=z['tropical'],smith_counts=counts(slopes),
                 B_min=z['B_min'],generic_certified=z['B_min']>=max(slopes))
        if row['generic_certified']:row['gauss']=z['tropical']+sum(slopes)
        row['matches']=(row['tropical']==pre['tropical'] and row['smith_counts']==pre['smith_counts']
                        and row.get('gauss')==pre['gauss'])
        if not row['matches']:
            failures.append(row);print('FAIL '+json.dumps(row),flush=True)
        rows.append(row)
        if len(rows)%20==0:
            out.write_text(json.dumps(dict(rows=rows,failures=failures),indent=2))
            print(f'{len(rows)}/{len(set(jobs))} cases; failures={len(failures)}; {time.time()-start:.1f}s',flush=True)
    lower_failures=[r for r in rows if not r['generic_certified'] or r['gauss']<r['prediction']['gauss']]
    summary=dict(cases=len(rows),matches=sum(r['matches'] for r in rows),failures=len(failures),
                 generic_certified=sum(r['generic_certified'] for r in rows),seconds=time.time()-start,
                 lower_bound_failures=len(lower_failures),
                 status='Smith equality disproved; determinant lower bound remains a conjecture')
    out.write_text(json.dumps(dict(summary=summary,failures=failures,lower_bound_failures=lower_failures,rows=rows),indent=2))
    print('SUMMARY '+json.dumps(summary),flush=True)
