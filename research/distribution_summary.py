"""Deduplicate the finite construction experiments for reporting."""
import json
from pathlib import Path

if __name__=='__main__':
    folder=Path(__file__).parent;allrows={};summaries=[]
    for name in ['distribution_search24','distribution_search48','distribution_search72',
                 'distribution_origin24','distribution_origin48']:
        rows=json.loads((folder/(name+'.json')).read_text())
        for r in rows:allrows[r['K'],r['h'],tuple(r['shape']),r.get('origin',0)]=r
        origin=[r for r in rows if r.get('origin',0)]
        summaries.append(dict(file=name,cases=len(rows),best=min(rows,key=lambda r:r['score_per_lambda']),
                              best_origin=min(origin,key=lambda r:r['score_per_lambda']) if origin else None))
    dimension=json.loads((folder/'distribution_dimension.json').read_text())['rows']
    for r in dimension:allrows[r['K'],r['h'],tuple(r['shape']),r.get('origin',0)]=r
    assert all(r['strictly_positive'] for r in allrows.values())
    result=dict(unique_cases=len(allrows),all_strictly_positive=True,files=summaries,
                dimension_cases=len(dimension))
    (folder/'distribution_summary.json').write_text(json.dumps(result,indent=2))
    print('unique cases',len(allrows))
    for r in summaries:
        best=r['best'];origin=r['best_origin']
        print(r['file'],r['cases'],'best',best['shape'],best.get('origin',0),best['h'],best['score'],
              'best origin',({k:origin[k] for k in ['shape','origin','h','score','score_per_lambda']} if origin else None))
