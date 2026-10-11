"""Read-back verification of whole-cone buffered integer certificates."""
import json,sys
from pathlib import Path
from fractions import Fraction as F
from verify_four_pole_positive_lattice import reconstruct

sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ceil(x):return -((-x.numerator)//x.denominator)


def main():
    folder=Path(__file__).parent
    data=json.loads((folder/'four_pole_conductor.json').read_text())
    def keyed(name):return {(r['n'],r['m'],r['s']):r for r in json.loads((folder/name).read_text())['rows']}
    lifts=keyed('four_pole_minimal_lifts.json');source=keyed('four_pole_positive_lattice.json');periods=keyed('four_pole_lift_periods.json')
    seeds=data['rows']+data['rational_axis_regions']
    for seed in seeds:
        key=tuple(seed[k] for k in ('n','m','s'));n,m,s=key
        C2,a,b,B=reconstruct(n,m,s);p=list(map(int,seed['integer_polynomial']));Z=seed['zero_basis']
        assert Z==lifts[key]['zero_basis'] # This full saturated basis is certified separately.
        beta=[sum(abs(sum(line[i]*Z[i][j] for i in range(m+1))) for j in range(m-2))/F(2) for line in B]
        assert all(dot(line,p)>=rad for line,rad in zip(B,beta)) and dot(C2,p)==0
        assert max(abs(x).bit_length() for x in p)==seed['input_bits']
        if 'constant' in seed:
            g=F(seed['constant']);assert dot(a,p)==g>0 and dot(b,p)==0
            old=source[key];v=list(map(int,old['optimized']['pair']))
            lo,hi=F(old['optimized']['lower']),F(old['optimized']['upper'])
            slack=min(v[0]+v[1]*lo,v[0]+v[1]*hi)
            c0=F(periods[key]['minimum_arithmetic_output_multiplier'])
            assert int(seed['target_dilation_bound'])==max(1,ceil(g/(c0*slack)))
        else:
            assert [dot(a,p),dot(b,p)]==list(map(F,seed['output']))
    # Small human-readable counterexample reproduced in the report.
    C2,a,b,B=reconstruct(2,3,7)
    p0=[-11360,2380,9921,-1030];z=[12864,-2704,-11220,1165]
    c=[dot(line,p0) for line in B];A=[dot(line,z) for line in B]
    assert max(-v/x for v,x in zip(c,A) if x>0)==F(206,233)
    assert min(-v/x for v,x in zip(c,A) if x<0)==F(117673,132114)
    p=[9*x+8*y for x,y in zip(p0,z)]
    assert p==[672,-212,-471,50] and [dot(C2,p),dot(a,p),dot(b,p)]==[0,-34560,34560]
    result=dict(status='passed',buffered_regions=len(data['rows']),target_independent_axis_regions=len(data['rational_axis_regions']),
                human_readable_minimum_n2_m3=9,
                method='Independent partial-fraction derivative polynomials; full zero-lattice comparison; exact buffer inequalities, output values and universal target thresholds.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result)


if __name__=='__main__':main()
