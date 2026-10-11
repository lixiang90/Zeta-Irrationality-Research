"""Audit the complete-pencil certificate across a range of primes and ratios."""
import json,time
from pathlib import Path
from sympy import primerange
from coupled_pencil import normalized_pencil
from coupled_schur import integral_solve_certificate,counts
from distribution_modular import smith_mod
from joint_exact import experiment
from joint_padic import val

if __name__=='__main__':
    start=time.time();rows=[];polynomials={};special=[]
    out=Path(__file__).with_suffix('.json')
    for K in [24,32,40,48,64,80,120]:
        Ns=sorted({1,max(1,3*K//40),K//8})
        for N in Ns:
            for p in primerange(max(7,2*N+1),2*K+1):
                if p*p<=2*K:continue
                d=normalized_pencil(K,N,p,8)
                slopes,censored,_=smith_mod(d['A'],p,8)
                assert not censored
                crude=d['B_min']>=max(slopes)
                row=dict(K=K,N=N,p=p,tropical=d['tropical'],B_min=d['B_min'],
                         smith_counts=counts(slopes),constant_valuation=d['tropical']+sum(slopes),
                         crude_certificate=crude)
                if not crude:
                    cert=integral_solve_certificate(d['A'],d['B'],p,8)
                    row['solve_certificate']=cert
                    if (K,N) not in polynomials:polynomials[K,N]=experiment(K,[(N,8)],K-N)[1]
                    P=polynomials[K,N];actual=min(val(c,p) for c in P)
                    row['exact_gauss']=actual;row['specialization_excess']=row['constant_valuation']-actual
                    if cert['certified']:assert actual==row['constant_valuation']
                    special.append(row);print('SPECIAL '+json.dumps(row),flush=True)
                rows.append(row)
            print(f'K={K} N={N}: {len(rows)} cases, {time.time()-start:.1f}s',flush=True)
            out.write_text(json.dumps(dict(rows=rows,special=special),indent=2))
    summary=dict(cases=len(rows),crude_certified=sum(r['crude_certificate'] for r in rows),
                 new_certified=sum(r.get('solve_certificate',{}).get('certified',False) for r in rows),
                 failed=sum(not r['solve_certificate']['certified'] for r in special),seconds=time.time()-start)
    out.write_text(json.dumps(dict(summary=summary,special=special,rows=rows),indent=2))
    print('SUMMARY '+json.dumps(summary),flush=True)
