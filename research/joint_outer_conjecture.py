"""Test a newly observed large-prime content formula; not a uniform proof."""
import json,time
from pathlib import Path
from sympy import primerange
from joint_exact import experiment
from joint_padic import val

if __name__=="__main__":
    rows=[];bad=[];start=time.time();folder=Path(__file__).parent
    for K in [16,24,32,40,48,56,64]:
        for N in range(1,K//8+1):
            r,P,*_=experiment(K,[(N,8)],K-N)
            for p in primerange(max(11,(K+N+2)//2),K-N+1):
                if 2*p<K+N+1:continue
                vals=[val(c,p) for c in P]
                actual=min(vals);pred=-9*(K-p)+8*N-1
                deg=max(i for i,v in enumerate(vals) if v==actual)
                row=dict(K=K,N=N,p=p,actual=actual,pred=pred,reduction_degree=deg,
                         predicted_degree=2*p-K-N-1,
                         rank_corrected_pred=pred-max(0,K+6*N-3*p+3))
                assert actual==row['rank_corrected_pred']
                rows.append(row)
                if actual!=pred or deg!=row["predicted_degree"]:bad.append(row)
            print(f"K={K} N={N} checked={len(rows)} exceptions={len(bad)} elapsed={time.time()-start:.1f}",flush=True)
            (folder/"joint_outer_conjecture.json").write_text(json.dumps(dict(rows=rows,exceptions=bad),indent=2))
