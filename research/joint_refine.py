"""Rescale promising shapes without confusing smaller h with better per-row gain."""
import json,time
from pathlib import Path
from joint_exact import experiment

if __name__=='__main__':
    folder=Path(__file__).parent;out=folder/'joint_refine.json';start=time.time()
    rows=json.loads(out.read_text()) if out.exists() else []
    done={(r['K'],tuple(map(tuple,r['profile'])),r['h']) for r in rows}
    jobs=[]
    for K in [24,48,72]:
        m=K//24
        for profile in [[(m,3),(2*m,3)],[(m,2),(2*m,3)],[(m,4),(2*m,4)],[(m,8)],[(2*m,8)]]:
            jobs.append((K,profile,K))
        jobs.append((K,[(m,3),(2*m,3)],3*K//4))
    for K,profile,h in jobs:
        if (K,tuple(profile),h) in done:continue
        r,*_=experiment(K,profile,h)
        r['score_per_lambda']=r['score']*K/h;rows.append(r)
        out.write_text(json.dumps(rows,indent=2))
        print(json.dumps(r)+f' elapsed={time.time()-start:.1f}',flush=True)
