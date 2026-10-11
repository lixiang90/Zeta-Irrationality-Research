"""Exact first-node derivative contribution for the naive double-zero family."""
import json
from pathlib import Path
from flint import fmpq,arb,ctx
from pure_odd_derivative_probe import coefficients,row,harmonic_table


def first_node(n,r):
    H=harmonic_table(n+1,r)
    ell=[fmpq(0)]+[2*fmpq(-H[n-1][j]+(-1)**j*H[n+1][j],j) for j in range(1,r-1)]
    jet=[fmpq(1)]
    for k in range(1,r-1):jet.append(sum((j*ell[j]*jet[k-j] for j in range(1,k+1)),fmpq(0))/k)
    result=-jet[r-2]/(n*n*(n+1)**2);assert result>0
    return result


def main():
    rows=[]
    for n in (16,32,64,128,256):
        A,B=coefficients(n,n);H=harmonic_table(n,11)
        for s in (5,7,9,11):
            rec=row(n,n,s,A,B,H);first=first_node(n,s-2)
            pair=list(map(int,rec['primitive_pair']))
            with ctx.workprec(2*max(abs(x).bit_length() for x in pair)+512):
                raw=(arb(pair[0])+arb(pair[1])*arb(s).zeta())/arb(fmpq(rec['primitive_scale']))
                rec.update(first_node=str(first),raw_to_first_ratio=(raw/arb(first)).str(24))
            rows.append(rec)
        print('head comparison',n,[r['raw_to_first_ratio'] for r in rows[-4:]],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Exact first-node contribution and certified finite ratios. The fixed-order asymptotic is proved in the accompanying report.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
