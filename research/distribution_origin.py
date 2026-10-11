"""Jointly vary the origin zero, positive-root multiplicities, and dimension."""
import argparse,json,time
from pathlib import Path
from distribution_search import run_shape

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,default=24)
    args=ap.parse_args();folder=Path(__file__).parent
    out=folder/f'distribution_origin{args.K}.json'
    rows=json.loads(out.read_text()) if out.exists() else []
    done={(tuple(r['shape']),r['origin'],r['h']) for r in rows}
    if args.K==24:
        prior=json.loads((folder/'distribution_search24.json').read_text())
        shapes=[r['shape'] for r in sorted(prior,key=lambda r:r['score'])[:8]]
        shapes+=[[8],[7],[8,2],[7,3]]
        jobs=[(shape,a,h) for shape in shapes for a in [0,1,2,3,4,6] for h in [21,24,27]]
    else:
        assert args.K%24==0;m=args.K//24
        prior=json.loads((folder/'distribution_origin24.json').read_text())
        chosen=sorted(prior,key=lambda r:r['score_per_lambda'])[:6]
        withorigin=[r for r in prior if r['origin']]
        chosen+=sorted(withorigin,key=lambda r:r['score_per_lambda'])[:2]
        jobs=[]
        for r in chosen:
            # Test a fixed origin multiplicity and, separately, a fixed ratio.
            for a in {r['origin'],m*r['origin']}:
                jobs.append((r['shape'],a,m*r['h']))
    start=time.time();best=min((r['score_per_lambda'] for r in rows),default=1e9)
    for shape,a,h in jobs:
        key=(tuple(shape),a,h)
        if key in done:continue
        r,_=run_shape(args.K,shape,h,a);rows.append(r);done.add(key)
        if r['score_per_lambda']<best:
            best=r['score_per_lambda'];print('BEST '+json.dumps(r),flush=True)
        if len(rows)%20==0 or args.K!=24:
            out.write_text(json.dumps(rows,indent=2))
            print(f'{len(rows)} cases, {time.time()-start:.1f}s',flush=True)
    out.write_text(json.dumps(rows,indent=2))
    print('SUMMARY '+json.dumps(dict(K=args.K,cases=len(rows),
          negative_cases=sum(r['score']<0 for r in rows),
          best=min(rows,key=lambda r:r['score_per_lambda']))),flush=True)
