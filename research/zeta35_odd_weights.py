"""Explore previously omitted positive odd powers of D_N, with exact polynomials."""
import argparse,contextlib,io,json
from pathlib import Path
from zeta35_target31_scan import run

def main(scale):
    root=Path(__file__).parent;rows=[]
    path=root/f'zeta35_odd_weights_scale{scale}.json'
    if scale==1:
        cases=[(N,m,40-N-drop) for m in (1,3,5) for N in (2,3,4,5,6,8,10,12) for drop in (0,2,4)]
    else:
        previous=json.loads((root/'zeta35_odd_weights_scale1.json').read_text())
        cases=[(scale*r['N'],r['m'],scale*r['h']) for r in sorted(previous['rows'],key=lambda r:r['log_p'])[:6]]
    for i,(N,m,h) in enumerate(cases):
        with contextlib.redirect_stdout(io.StringIO()):row=run(40*scale,N,m,h)
        rows.append(row)
        path.write_text(json.dumps(dict(scope='finite odd-power scan only',rows=rows),indent=2),encoding='utf-8')
        if scale>1 or (i+1)%12==0:
            best=min(rows,key=lambda r:r['log_p'])
            print('done',i+1,'best',(best['K'],best['N'],best['m'],best['h'],best['log_p']),flush=True)
    print('best',[{k:r[k] for k in ('K','N','m','h','log_p')} for r in sorted(rows,key=lambda r:r['log_p'])[:8]],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--scale',type=int,default=1);main(p.parse_args().scale)
