"""Reproduce the full node-window scan and fair head-degree comparisons."""
import json
from pathlib import Path
from flint import arb, fmpq, ctx
from discrete_positive_cone_probe import run
from positive_head_cone import cone


def main():
    ctx.prec=256
    folder=Path(__file__).parent
    old=json.loads((folder/'positive_head_cone.json').read_text())['rows']
    results=[]
    for n,w in ((4,2),(4,4),(8,4),(8,8),(16,8),(24,8)):
        r=run(n,w,'extreme_window',next(x for x in old if x['n']==n and x['w']==w))
        lo=fmpq(r['lower']['endpoint']);hi=fmpq(r['upper']['endpoint']);checks=[]
        for shift in range(w+1):
            c=cone(n,n+shift,w-shift)
            lower=fmpq(c['lower_bound']);upper=fmpq(c['upper_bound'])
            checks.append(dict(head=n+shift,w=w-shift,lo=str(lower),hi=str(upper),
                window_width_over_head_width=(arb(hi-lo)/arb(upper-lower)).str(15),
                head_contains_window=bool(lower<=lo and hi<=upper)))
        r['head_budget_checks']=checks;results.append(r)
        print(n,w,'generators',r['generator_count'],'dual certificates',
              r['lower']['dual_verified'],r['upper']['dual_verified'],flush=True)
        (folder/'discrete_positive_full_window.json').write_text(json.dumps(dict(
            scope='Complete extreme patterns only within node window 0..12. Global certificates, when available, are in discrete_positive_global_certificate.json.',
            rows=results),indent=2),encoding='utf-8')


if __name__=='__main__':main()
