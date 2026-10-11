"""Score nearby positive root configurations by primitive output upper bounds.

The upper bounds use an already independently certified global zeta interval.
No numerical value of zeta is used to choose candidates.
"""
import json
from pathlib import Path
from flint import fmpq, arb, ctx
from growing_positive_moment import shifted_map, candidate
from growing_positive_arithmetic import audit


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    rows+=json.loads((folder/'growing_positive_ratio_scan.json').read_text())['rows']
    results=[]
    for n,w in ((8,8),(16,16),(24,24),(24,48)):
        source=next(r for r in rows if r['n']==n and r['w']==w)
        lo=fmpq(source['lower']['endpoint']);hi=fmpq(source['upper']['endpoint'])
        M=shifted_map(n,w);tested=0;positive=0;records=[]
        for name in ('lower','upper'):
            edge=source[name];base=edge['starts'];patterns={tuple(base)}
            for i in range(len(base)):
                for change in (-2,-1,1,2):
                    s=base[:];s[i]+=change
                    if s[0]<(0 if edge['infinity'] else 1) or any(b<a+2 for a,b in zip(s,s[1:])):continue
                    patterns.add(tuple(s))
            best=None;best_bound=None
            for s in sorted(patterns):
                c=candidate(n,w,M,s,edge['infinity']);tested+=1
                if c is None or not c['primal_positive']:continue
                positive+=1;a,b=c['primitive_output']
                bound=max(a+b*lo,a+b*hi);assert bound>0
                if best is None or bound<best_bound:best=c;best_bound=bound
            a,b=edge['primitive_output'];baseline=max(a+b*lo,a+b*hi)
            with ctx.workprec(256):
                records.append(dict(original_face=name,best=best,upper_bound=str(best_bound),
                    baseline_upper_bound=str(baseline),
                    improvement=(arb(baseline)/arb(best_bound)).str(18),
                    log_best_upper_per_n=(arb(best_bound).log()/n).str(18),
                    arithmetic=audit(best,M)))
        result=dict(n=n,w=w,tested=tested,positive=positive,records=records);results.append(result)
        print(n,w,tested,positive,[(r['original_face'],r['improvement'],r['log_best_upper_per_n']) for r in records],flush=True)
        (folder/'growing_positive_arithmetic_neighbors.json').write_text(json.dumps(dict(
            scope='Finite one-pair shifts by at most two nodes; best certified upper bound in this local set only, no global arithmetic optimum claim.',
            rows=results),indent=2),encoding='utf-8')


if __name__=='__main__':main()
