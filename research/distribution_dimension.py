"""Check the cost of enlarging the polynomial sector enough for t F_p^8."""
import json
from pathlib import Path
from flint import fmpq_poly
from joint_exact import Dcache
from distribution_search import run_shape

if __name__=='__main__':
    thresholds=[];K=24;N=1;t=fmpq_poly([0,1])
    for p in [7,11]:
        m=(p-1)//2;T=Dcache(K)//Dcache(N)
        R=t*Dcache(N)*(Dcache(m)//Dcache(N))**4
        degree=4*m-3*N+1;h=K-N+degree+1
        assert R.degree()==degree
        P=fmpq_poly(Dcache(N)**7*T)*R**2
        assert not P%(t*Dcache(m)**8)
        thresholds.append(dict(K=K,N=N,p=p,minimum_R_degree=degree,minimum_h=h))
    rows=[]
    for h in [24,30,34,36,42,48]:
        for a in [0,1]:
            r,_=run_shape(24,[8],h,a);rows.append(r)
            print(json.dumps({k:r[k] for k in ['K','h','origin','score','score_per_lambda']}),flush=True)
    result=dict(thresholds=thresholds,rows=rows,all_strictly_positive=all(r['strictly_positive'] for r in rows))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
