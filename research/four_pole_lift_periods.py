"""Separate the arithmetic output period from the constructed positive lift."""
import json,math,sys
from pathlib import Path
from flint import fmpq as Q, fmpq_mat
from critical_lift_probe import primitive

sys.set_int_max_str_digits(0)


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows'];rows=[]
    for row in source:
        H=row['lattice']['image_hnf'];D=int(row['lattice']['clearing_scale'])
        basis=fmpq_mat([[H[j][i] for j in range(2)] for i in range(2)])
        v=list(map(int,row['optimized']['pair']))
        coords=list(basis.inv()*fmpq_mat([[D*x] for x in v]))
        primitive_coords,period=primitive(coords)
        assert period>0 and math.gcd(*primitive_coords)==1
        assert basis*fmpq_mat([[x] for x in primitive_coords])==fmpq_mat([[period*D*x] for x in v])
        c=Q(row['optimized']['output_scale']);k=c/period
        assert k.denominator==1 and k>0
        result=dict(n=row['n'],m=row['m'],s=row['s'],pair=list(map(str,v)),
                    minimum_arithmetic_output_multiplier=str(period),image_primitive_coordinates=list(map(str,primitive_coords)),
                    constructed_positive_output_multiplier=str(c),constructed_dilation=str(k),
                    constructed_dilation_bits=int(k).bit_length())
        rows.append(result)
        if row['s']==7 and (row['n'],row['m']) in ((8,8),(12,8),(24,12),(32,12)):
            print(row['n'],row['m'],'dilation bits',int(k).bit_length(),'period',str(period)[:100],flush=True)
    (folder/'four_pole_lift_periods.json').write_text(json.dumps(dict(status='passed',rows=rows,
        scope='Exact lattice membership period; positive lifting at that minimum is not asserted. Primitive image coordinates prove the period is minimal.'),indent=2),encoding='utf-8')
    print('verified periods',len(rows))


if __name__=='__main__':main()
