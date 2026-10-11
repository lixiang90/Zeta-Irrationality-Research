"""Joint constructions suggested by the top deformation coefficient.

Extra numerator zeros lie BEYOND the last denominator pole. Positivity of
the zeta(7) moment construction is preserved. All scores use the exact
primitive polynomial and rigorous Arb evaluation; finite scores are not
asymptotic conclusions.
"""
import json,time
from pathlib import Path
from flint import fmpq_poly
from joint_exact import Dcache,entries_from_polynomial,determinant,content
from stability_trace import trace_certificate


if __name__=='__main__':
    out=Path(__file__).with_suffix('.json');start=time.time()
    rows=json.loads(out.read_text()) if out.exists() else []
    cache={(r['K'],r['N'],r['h'],r['outer_power']):r for r in rows}
    for K in [24,48,72]:
        for N in [K//24,K//12,K//6]:
            for beta in [0,1]:
                h=K-N;key=(K,N,h,beta)
                if key in cache:continue
                W=Dcache(N)**8
                block=Dcache(3*K//2)//Dcache(K)
                if beta:W*=block**beta
                aa,bb=entries_from_polynomial(K,W,h)
                P=determinant(aa,bb,h)
                cert=trace_certificate(P,K)
                row=dict(K=K,N=N,h=h,outer_power=beta,outer_start=K+1,outer_end=3*K//2,**cert)
                rows.append(row);cache[key]=row;out.write_text(json.dumps(rows,indent=2))
                print(json.dumps(row)+f' elapsed={time.time()-start:.1f}s',flush=True)
