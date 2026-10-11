"""Finite content ceilings from one exact coefficient, without interpolation.

For each prime, lower <= v_p(content F) <= v_p(F(0)). Equality certifies the
complete polynomial's content valuation even when that polynomial is not built.
"""
import json
import math
from pathlib import Path
from flint import fmpq, fmpq_mat, arb, ctx
from sympy import primerange
from joint_exact import entries
from two_prefix_outer import vp
from overlap_truncated_crt import crt_bound
from verify_overlapping_prefix import allocation


def main():
    folder=Path(__file__).parent;rows=[]
    for K,N,A,B in [(96,4,9,11),(192,8,18,22)]:
        h=K-4*N;profile=[(N,4),(A,2),(B,2)]
        aa,bb=entries(K,profile,h)
        constant=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)]).det();assert constant
        if K==96:
            saved=json.loads((folder/'overlapping_prefix_scan.json').read_text())['rows']
            r=next(r for r in saved if r['K']==K and r['A']==A)
            assert constant==fmpq(r['raw_polynomial'][0])
        checks=[]
        with ctx.workprec(160):
            room=arb(0);bands={}
            for p in primerange(7,2*K+1):
                if p*p<=2*K+12*N+4:continue
                lower=max(crt_bound(K,profile,h,p)['lower'],allocation(K,profile,h,p)['bound'])
                upper=vp(constant,p);assert upper>=lower
                difference=upper-lower;room+=difference*arb(p).log()/K**2
                checks.append(dict(p=p,lower=lower,upper=upper,ceiling_slack=difference,exact_content=difference==0))
            for name,cond in [('p_le_K3',lambda p:3*p<=K),('K3_to_K2',lambda p:3*p>K and 2*p<=K),('p_gt_K2',lambda p:2*p>K)]:
                rs=[r for r in checks if cond(r['p'])]
                bands[name]=dict(count=len(rs),room_ball=sum((r['ceiling_slack']*arb(r['p']).log()/K**2 for r in rs),arb(0)).str(30))
            row=dict(K=K,N=N,A=A,B=B,h=h,constant_coefficient=str(constant),prime_checks=checks,
                     checked=len(checks),exact_content_primes=sum(r['exact_content'] for r in checks),
                     maximum_remaining_gain_ball=room.str(30),bands=bands,
                     scope='A rigorous finite upper bound for additional content on the checked primes only; no asymptotic or small-prime conclusion.')
        rows.append(row)
        (folder/'overlap_content_ceiling.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in row.items() if k not in ['constant_coefficient','prime_checks']}),flush=True)


if __name__=='__main__':main()
