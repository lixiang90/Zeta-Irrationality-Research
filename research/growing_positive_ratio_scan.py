"""Finite aspect-ratio comparisons with separately checked global certificates."""
import json
from pathlib import Path
from flint import fmpq, arb, ctx
from growing_positive_moment import shifted_map, search, summary
from growing_positive_arithmetic import audit
from positive_head_cone import cone


def main():
    folder=Path(__file__).parent;rows=[]
    for n in (8,12,16,24):
        for w in (n//2,3*n//2,2*n):
            M=shifted_map(n,w)
            edges=[search(n,w,M,inf) for inf in (True,False)]
            if any(e is None for e in edges) or {e['sign'] for e in edges}!={-1,1}:
                rows.append(dict(n=n,w=w,search_failed=True));continue
            row=summary(n,w,edges)
            row['arithmetic']=[audit(e,M) for e in edges]
            baseline=cone(n,n+w,0)
            blo=fmpq(baseline['lower_bound']);bhi=fmpq(baseline['upper_bound'])
            lo=fmpq(row['lower']['endpoint']);hi=fmpq(row['upper']['endpoint'])
            if row['full_cone_optimal']:assert blo<=lo<hi<=bhi
            with ctx.workprec(256):
                row['width_improvement_over_full_head']=(arb(bhi-blo)/arb(hi-lo)).str(16)
                row['log_width_improvement_over_full_head_per_n']=((arb(bhi-blo)/arb(hi-lo)).log()/n).str(16)
            rows.append(row)
            print(n,w,'global',row['full_cone_optimal'],'width',row['log_width_per_n'],
                  'first terms',[e['log_first_term_per_n'] for e in row['arithmetic']],
                  'head gain',row['width_improvement_over_full_head'],flush=True)
            (folder/'growing_positive_ratio_scan.json').write_text(json.dumps(dict(
                scope='Finite parameter ratios; search outputs are global only with both certificates, and no asymptotic rate is inferred.',
                rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
