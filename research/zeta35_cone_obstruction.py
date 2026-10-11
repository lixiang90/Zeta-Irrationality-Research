"""Locate the remaining low-denominator rational obstruction in exact intervals."""
import json
import math
from pathlib import Path
from flint import fmpq as Q
from zeta35_cone_lattice import cf_candidates


def simplest_inside(lo,hi):
    # Accelerated Stern-Brocot search; the first interior mediant has minimal
    # denominator among positive rationals strictly inside the interval.
    a,b,c,d=0,1,1,0
    while True:
        p,q=a+c,b+d
        m=Q(p,q)
        if lo<m<hi:
            return p,q
        if m<=lo:
            k=int(((lo*b-a)/(c-lo*d)).floor())
            assert k>=1
            a,b=a+k*c,b+k*d
        else:
            k=int(((c-hi*d)/(hi*b-a)).floor())
            assert k>=1
            c,d=c+k*a,d+k*b


def main():
    root=Path(__file__).parent
    rows=json.loads((root/'zeta35_cone_lattice.json').read_text(encoding='utf-8'))['rows']
    output=[]
    for row in rows:
        if row['d']<row['N']:
            continue
        lo,hi=Q(row['lower']),Q(row['upper']);delta=hi-lo
        p,q=simplest_inside(lo,hi)
        cutoff=math.isqrt(int(delta.denominator)//(2*int(delta.numerator)))
        output.append(dict(N=row['N'],d=row['d'],shortest_interior_fraction=[str(p),str(q)],
                           denominator_cutoff=str(cutoff),has_short_candidate=q<=cutoff))
    examples=[]
    target=Q(3,2)
    for k in (2,4,8,16,32):
        epsilon=Q(1,10**k);lo=target-epsilon;hi=target+epsilon
        candidates=cf_candidates(lo,'lower')|cf_candidates(hi,'upper')|{(0,1)}
        upper=lambda v:v[0]*(hi if v[0]>=0 else lo)+v[1]
        a,c=min(candidates,key=upper)
        actual=a*target+c
        assert actual>=Q(1,2)
        examples.append(dict(k=k,chosen=[str(a),str(c)],positive_value=str(actual),
                             proved_upper=str(upper((a,c)))))
    out=dict(scope='exact finite diagnostics and rational counterexample to a cone-only irrationality argument',
             intervals=output,rational_counterexamples=examples)
    (root/'zeta35_cone_obstruction.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print([(r['N'],r['has_short_candidate']) for r in output])
    print(examples)


if __name__=='__main__':
    main()
