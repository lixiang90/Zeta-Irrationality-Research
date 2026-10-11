"""Preserve double poles but flatten head zeros beyond the derivative order."""
import json
from pathlib import Path
from pure_odd_derivative_probe import coefficients,row,harmonic_table


def main():
    rows=[]
    for s in (3,5,7,9,11):
        d=s-1;m=d//2
        for h in (2,4,8,16,32):
            for extra in (0,h//2,h):
                n=m*h+extra;A,B=coefficients(n,h,d);H=harmonic_table(n,s)
                rec=row(n,h,s,A,B,H,d);rows.append(rec)
                if h==32 and extra==0:
                    print(n,h,s,'positive',rec['positive'],'raw',rec['log_raw_per_n'],'scale',rec['log_scale_per_n'],'final',rec['log_primitive_per_n'],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Pure single-zeta forms with head zero multiplicity s-1; exact coefficients and rigorous finite Arb evaluations, not asymptotic inference.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
