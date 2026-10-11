"""Finite exact multi-prefix and h screening; no extrapolated proof claims."""
import argparse,json,time
from pathlib import Path
from joint_exact import experiment,canonical


def cases(K):
    # Two separated zero prefixes; include controls with the same total degree.
    unit=K//16
    profiles=[[(unit,b)] for b in [2,4,6,8,10,12]]
    profiles += [[(unit,b1),(unit*j,b2)] for j in [2,3,4]
                 for b1,b2 in [(2,2),(4,2),(6,2),(2,4),(4,4),(2,6)]]
    for profile in profiles:
        nmax=max(n for n,b in profile)
        for h in sorted(set([3*K//4,K-nmax,K,5*K//4])):
            yield canonical(profile),h


if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--K",type=int,default=16)
    ap.add_argument("--out",default="joint_scan16.json")
    ap.add_argument("--refine",help="Scale the best distinct shapes from this prior result file")
    ap.add_argument("--top",type=int,default=6)
    args=ap.parse_args();folder=Path(__file__).parent
    if args.refine:
        prior=json.loads((folder/args.refine).read_text());chosen=[];seen=set()
        for r in sorted(prior,key=lambda r:r["score"]):
            key=(tuple(map(tuple,r["profile"])),r["h"])
            if key in seen:continue
            seen.add(key);chosen.append(r)
            if len(chosen)>=args.top:break
        jobs=[]
        for r in chosen:
            assert args.K%r["K"]==0
            factor=args.K//r["K"]
            jobs.append((tuple((n*factor,b) for n,b in r["profile"]),r["h"]*factor))
    else:jobs=list(cases(args.K))
    rows=[];start=time.time();out=folder/args.out
    for i,(profile,h) in enumerate(jobs):
        r,*_=experiment(args.K,profile,h);rows.append(r)
        out.write_text(json.dumps(rows,indent=2),encoding="utf-8")
        print(f"{i+1}/{len(jobs)} "+json.dumps(r)+f" elapsed={time.time()-start:.1f}",flush=True)
