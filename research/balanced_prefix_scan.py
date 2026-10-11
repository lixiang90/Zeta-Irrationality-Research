"""One further matched-degree redistribution: D_N^2 D_(2N)^6."""
import json
from pathlib import Path
from joint_exact import experiment, content
from verify_overlapping_prefix import allocation
from two_prefix_outer import vp
from sympy import primerange


def main():
    rows=[];path=Path(__file__).with_suffix('.json')
    for N in (1,2,3,4):
        K=24*N;h=20*N;profile=[(N,2),(2*N,6)]
        r,P,aa,bb=experiment(K,profile,h);ct=content(P)
        r.update(N=N,content=str(ct),raw_polynomial=list(map(str,P)))
        checks=[]
        for p in primerange(7,2*K+1):
            if p*p<=2*K+12*N+4:continue
            lower=allocation(K,profile,h,p)['bound'];actual=vp(ct,p);assert actual>=lower
            checks.append(dict(p=p,lower=lower,actual=actual))
        r['allocation_checks']=checks;rows.append(r)
        path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        print(json.dumps({k:r[k] for k in ['K','N','score_ball']}),flush=True)


if __name__=='__main__':main()
