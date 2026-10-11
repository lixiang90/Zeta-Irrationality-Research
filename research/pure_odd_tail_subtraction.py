"""Remove the finite rational head instead of increasing zero multiplicity."""
import json
from pathlib import Path
from pure_odd_derivative_probe import coefficients,row,harmonic_table


def main():
    rows=[]
    for n in (4,8,16,32,64,128):
        A,B=coefficients(n,n);H=harmonic_table(2*n,11)
        for s in (3,5,7,9,11):
            rec=row(n,n,s,A,B,H,offset=n);rows.append(rec)
            if s in (5,7,9):print('tail',n,s,'positive',rec['positive'],'raw',rec['log_raw_per_n'],
                                   'scale',rec['log_scale_per_n'],'final',rec['log_primitive_per_n'],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Exact rational head subtraction preserves pure single-zeta support; rigorous finite values, no asymptotic claim.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
