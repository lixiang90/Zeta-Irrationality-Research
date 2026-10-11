"""Corrected fixed-ratio content data and exact local rank/Smith probes."""
import argparse,json,time
from pathlib import Path
import numpy as np
from sympy import primerange
from joint_exact import experiment,norm_scalar,binomial_matrices
from joint_padic import analyze,val
from restart_arithmetic import eout,ein


def run(K,N):
    profile=[(N,8)];h=K-N;start=time.time()
    print(f"START K={K} N={N} h={h}",flush=True)
    folder=Path(__file__).parent
    r,P,aa,bb=experiment(K,profile,h,folder/f"joint_cache_K{K}_N{N}.json")
    S=norm_scalar(K,profile,h);F=P*S
    print("DETERMINANT "+json.dumps(r)+f" seconds={time.time()-start:.1f}",flush=True)
    primes=list(primerange(7,2*h+1));outer=[];inner=[]
    for p in primes:
        x=K/p;actual=min(val(c,p) for c in F)
        if x<3:
            model=float(eout(np.array([x]),N/K)[0])
            outer.append(dict(p=p,actual=actual,model_leading=-p*model,
                              gain=actual+p*model))
        elif x<=20:
            model=float(ein(np.array([x]),N/K)[0])
            inner.append(dict(p=p,actual=actual,model_leading=-p*model,
                              gain=actual+p*model))
    r["outer_gain_proxy"]=sum(t["gain"]*np.log(t["p"]) for t in outer)/K**2
    r["outer_primes"]=outer;r["inner_primes"]=inner
    selected=sorted(set(min([p for p in primes if p<=K],key=lambda p:abs(p/K-y)) for y in [.4,.55,.7,.9]))
    A,B=binomial_matrices(K,profile,h,aa,bb)
    assert (A+B).det()==F(1)
    r["local"]=[]
    for p in selected:
        t=analyze(A,B,F,p)
        r["local"].append(t)
        print("LOCAL "+json.dumps(dict(K=K,N=N,**t)),flush=True)
    r["seconds"]=time.time()-start
    return r


if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--pairs",default="40:1,40:3,80:2,80:6")
    ap.add_argument("--out",default="joint_baseline.json");args=ap.parse_args()
    rows=[];out=Path(__file__).with_name(args.out)
    for item in args.pairs.split(","):
        K,N=map(int,item.split(":"));rows.append(run(K,N))
        out.write_text(json.dumps(rows,indent=2),encoding="utf-8")
