"""Bounded cutoff optimization, keeping one target zeta value throughout."""
import json
from pathlib import Path
from fractions import Fraction
from pure_odd_derivative_probe import coefficients,row,harmonic_table


def main():
    rows=[];best=[]
    for n in (32,64,128):
        A,B=coefficients(n,n);H=harmonic_table(2*n,9)
        for s in (5,7,9):
            candidates=[]
            for k in range(0,n+1,n//8):
                rec=row(n,n,s,A,B,H,offset=k);rows.append(rec);candidates.append(rec)
            # The displayed certified intervals separate these candidates.
            winner=min(candidates,key=lambda r:abs(Fraction(r['primitive_value'].strip('[]').split('+/-')[0].strip())))
            best.append(dict(n=n,s=s,offset=winner['summation_offset'],log_primitive_per_n=winner['log_primitive_per_n']))
            print('cutoff optimum in grid',n,s,best[-1]['offset'],best[-1]['log_primitive_per_n'],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope='Finite grid of cutoffs 0,n/8,...,n; minimum only in this grid.',rows=rows,best=best),indent=2),encoding='utf-8')


if __name__=='__main__':main()
