"""Resolve Smith patterns across the six-pole window instead of fitting a few scales."""
import json,time
from pathlib import Path
from distribution_modular import smith_mod
from coupled_pencil import normalized_pencil
from coupled_schur import counts

if __name__=='__main__':
    out=Path(__file__).with_suffix('.json');rows=[];start=time.time()
    jobs=[]
    for p in [11,17,23,31,43,59]:
        for N in sorted({max(1,p//10),p//4,p//3,3*p//8}):
            for a in sorted({0,N//2,N}):jobs.append((3*p-1-a,N,p))
    for a in range(17):jobs.append((128-a,16,43))
    for K,N,p in sorted(set(jobs)):
        d=normalized_pencil(K,N,p,8);slopes,censored,_=smith_mod(d['A'],p,8)
        assert not censored
        row=dict(K=K,N=N,p=p,a=3*p-K-1,tropical=d['tropical'],
                 B_min=d['B_min'],smith_counts=counts(slopes),smith_sum=sum(slopes),
                 max_slope=max(slopes),generic_certified=d['B_min']>=max(slopes))
        if row['generic_certified']:row['gauss']=d['tropical']+sum(slopes)
        rows.append(row)
        if len(rows)%10==0:
            out.write_text(json.dumps(rows,indent=2));print(f'{len(rows)}/{len(set(jobs))} cases, {time.time()-start:.1f}s',flush=True)
    out.write_text(json.dumps(rows,indent=2))
    for r in rows:
        if r['p']==43 and r['N']==16:print(json.dumps(r),flush=True)
    print('SUMMARY '+json.dumps(dict(cases=len(rows),generic_certified=sum(r['generic_certified'] for r in rows),seconds=time.time()-start)),flush=True)
