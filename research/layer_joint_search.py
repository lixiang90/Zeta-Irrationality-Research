"""Three-prefix search with rigorous value balls and fixed-ratio refinement."""
import argparse,json,time
from pathlib import Path
from joint_exact import experiment

def screen_jobs():
    for Ns in [(1,2,3),(1,2,4)]:
        for b1 in [1,2,3,4,6]:
            for b2 in [1,2,3,4]:
                for b3 in [1,2,3,4]:
                    if not 6<=b1+b2+b3<=12:continue
                    if sum(n*b for n,b in zip(Ns,[b1,b2,b3]))>32:continue
                    profile=list(zip(Ns,[b1,b2,b3]))
                    for h in [18,21,24]:yield 24,profile,h

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,default=24)
    ap.add_argument('--top',type=int,default=6);args=ap.parse_args()
    folder=Path(__file__).parent;out=folder/f'layer_joint_search{args.K}.json'
    rows=json.loads(out.read_text()) if out.exists() else []
    done={(r['K'],tuple(map(tuple,r['profile'])),r['h']) for r in rows}
    if args.K==24:jobs=list(screen_jobs())
    else:
        prior=json.loads((folder/'layer_joint_search24.json').read_text())
        chosen=sorted(prior,key=lambda r:r['score_per_lambda'])[:args.top]
        assert args.K%24==0;m=args.K//24
        jobs=[(args.K,[(m*n,b) for n,b in r['profile']],m*r['h']) for r in chosen]
    start=time.time();best=min((r['score_per_lambda'] for r in rows),default=1e9)
    for K,profile,h in jobs:
        if (K,tuple(profile),h) in done:continue
        r,*_=experiment(K,profile,h);r['score_per_lambda']=r['score']*K/h
        rows.append(r);done.add((K,tuple(profile),h))
        if r['score_per_lambda']<best:
            best=r['score_per_lambda'];print('BEST '+json.dumps(r),flush=True)
        if len(rows)%25==0 or args.K!=24:
            out.write_text(json.dumps(rows,indent=2));print(f'{len(rows)}/{len(jobs)} elapsed={time.time()-start:.1f}s',flush=True)
    out.write_text(json.dumps(rows,indent=2))
