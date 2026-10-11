"""Deterministic exploratory search, including odd multiplicities and free h."""
import json,random,time,argparse
from pathlib import Path
from joint_exact import experiment,canonical

def jobs(K,count):
    assert K==24
    profiles=set()
    for N in range(1,9):
        for b in range(1,17):
            if N*b<=36:profiles.add(((N,b),))
    for N1 in range(1,5):
        for N2 in range(N1+1,9):
            for b1 in range(1,9):
                for b2 in range(1,9):
                    if N1*b1+N2*b2<=36:profiles.add(((N1,b1),(N2,b2)))
    alljobs=[(profile,h) for profile in sorted(profiles) for h in [6,9,12,15,18,21,24,27]
             if 2*h+sum(n*b for n,b in profile)>K-3]
    random.Random(20260928).shuffle(alljobs)
    return alljobs[:count]

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--count",type=int,default=1200)
    args=ap.parse_args();out=Path(__file__).with_name("joint_broad24.json")
    rows=[];best=1e9;best_perrow=1e9;start=time.time()
    for i,(profile,h) in enumerate(jobs(24,args.count)):
        r,*_=experiment(24,profile,h)
        r["score_per_lambda"]=r["score"]*24/h
        rows.append(r)
        if r["score"]<best or r["score_per_lambda"]<best_perrow:
            best=min(best,r["score"]);best_perrow=min(best_perrow,r["score_per_lambda"])
            print("NEW_BEST "+json.dumps(r),flush=True)
        if (i+1)%50==0:
            out.write_text(json.dumps(rows,indent=2),encoding="utf-8")
            print(f"progress {i+1}, elapsed {time.time()-start:.1f}s, best {best:.8f}, per_lambda {best_perrow:.8f}",flush=True)
    out.write_text(json.dumps(rows,indent=2),encoding="utf-8")
