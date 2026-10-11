"""Double-pole rational functions and pure odd-zeta derivative forms.

The output identity is exact. Arb enclosures certify finite values only.
"""
import json
import math
import sys
from pathlib import Path
from flint import fmpq, arb, ctx
from critical_lift_probe import primitive, harmonic_table

sys.set_int_max_str_digits(0)


def coefficients(n,h,d=2):
    """R=n!^2/h!^d (t-h)_h^d/(t)_(n+1)^2, d even, dh<=2n."""
    assert d%2==0 and d*h<=2*n
    H=harmonic_table(n+h,1)
    A=[];B=[]
    for k in range(n+1):
        b=math.comb(n,k)**2*math.comb(k+h,h)**d
        a=b*((d+2)*H[k][1]-d*H[k+h][1]-2*H[n-k][1])
        A.append(a);B.append(fmpq(b))
    assert sum(A)==0
    return A,B


def row(n,h,s,A,B,H,d=2,offset=0):
    r=s-2;assert r%2==1 and s>=3
    const=-sum((A[k]*H[k+offset][s-1]+(s-1)*B[k]*H[k+offset][s] for k in range(n+1)),fmpq(0))
    q=(s-1)*sum(B)
    pair,scale=primitive([const,q]);assert pair[1]>0 and scale>0
    den=math.lcm(int(const.denominator),int(q.denominator))
    content=math.gcd(int(const*den),int(q*den))
    with ctx.workprec(2*max(abs(x).bit_length() for x in pair)+512):
        value=arb(pair[0])+arb(pair[1])*arb(s).zeta()
        assert not value.contains(0)
        raw=value/arb(scale)
        result=dict(n=n,h=h,s=s,zero_multiplicity=d,summation_offset=offset,A=list(map(str,A)),B=list(map(str,B)),
                    constant=str(const),zeta_coefficient=str(q),primitive_pair=list(map(str,pair)),
                    primitive_scale=str(scale),clearing_denominator=str(den),output_content=str(content),
                    raw_value=raw.str(24),primitive_value=value.str(24),positive=bool(value>0),
                    log_raw_per_n=(abs(raw).log()/n).str(18),
                    log_scale_per_n=(arb(scale).log()/n).str(18),
                    log_primitive_per_n=(abs(value).log()/n).str(18))
    return result


def main():
    rows=[]
    for n in (4,8,16,32,64,128):
        H=harmonic_table(n,11)
        for h in sorted(set((0,n//2,n))):
            A,B=coefficients(n,h)
            for s in (3,5,7,9,11):
                rec=row(n,h,s,A,B,H);rows.append(rec)
                if h==n and s in (3,7,9):
                    print(n,h,s,rec['log_raw_per_n'],rec['log_scale_per_n'],rec['log_primitive_per_n'],flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Pure single-zeta identities and certified finite values. No inference of asymptotic positivity or irrationality from numerical rates.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
