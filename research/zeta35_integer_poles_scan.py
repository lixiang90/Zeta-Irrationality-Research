"""Vary zero count independently of pole count, retaining exact target alignment."""
import json
from pathlib import Path
from flint import fmpq as Q
from zeta35_integer_poles import run

root=Path(__file__).parent
rows=[run(20,Q(M,20),False) for M in range(51)]
best=sorted((v for v in rows if v['positivity_at_all_integer_summands']),
            key=lambda v:v['log_abs_integer_form'])[:8]
print('best N20',[(v['M'],v['log_abs_integer_form']) for v in best],flush=True)
scaled=[]
for scale in (2,4):
    for v in best:
        scaled.append(run(scale*20,Q(v['M'],20)))
(root/'zeta35_integer_poles_scan.json').write_text(json.dumps(dict(
    scope='finite exact scan, independently varied zero count',rows=rows,scaled=scaled),indent=2),encoding='utf-8')
