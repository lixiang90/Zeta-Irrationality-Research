"""Necessary x interval from the y-independent leading 36x36 Gram block."""
import json,sys,math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx,fmpq_mat
import b8_hankel as b8
from zeta7_moment_extension_20261004 import aq,ball,positive_pivots

sys.set_int_max_str_digits(0)


def main():
    K,N,h,A,B=b8.entries(1);W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    quotient=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    E=[q[47] for q in quotient];F=[q[55] for q in quotient]
    hh=36
    assert all(not F[i+j] for i in range(hh) for j in range(hh))
    rank=fmpq_mat([[E[i+j] for j in range(hh)] for i in range(hh)]).rank()
    assert rank==8
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(hh)] for i in range(hh)])
    C=arb_mat([[aq(E[i+j]) for j in range(hh)] for i in range(hh)])
    rows=[]
    for sign in [-1,1]:
        lo,hi=80,240
        assert positive_pivots(H-C*aq(Q(sign*2**lo,17)))['positive_definite'] is True
        assert positive_pivots(H-C*aq(Q(sign*2**hi,17)))['positive_definite'] is False
        while hi-lo>1:
            mid=(lo+hi)//2;pd=positive_pivots(H-C*aq(Q(sign*2**mid,17)))
            assert pd['positive_definite'] is not None
            if pd['positive_definite']:lo=mid
            else:hi=mid
        c_inside=Q(sign*2**lo,17);c_outside=Q(sign*2**hi,17)
        pd_inside=positive_pivots(H-C*aq(c_inside));pd_outside=positive_pivots(H-C*aq(c_outside))
        if 'pivot_interval' in pd_outside:pd_outside['pivot_interval']=arb(pd_outside['pivot_interval']).str(80)
        rows.append(dict(sign=sign,last_positive_bit=lo,first_negative_bit=hi,
                         inside_x=str(c_inside),outside_x=str(c_outside),
                         inside_log_abs=ball(aq(abs(c_inside)).log()),outside_log_abs=ball(aq(abs(c_outside)).log()),
                         positive_check_inside=pd_inside,positive_check_outside=pd_outside))
    M=2**77*3**33*5**12*7**7*11**2
    out=dict(status='passed',K=K,N=N,h=h,necessary_principal_block_size=hh,rank_moment47_in_block=rank,
             moment55_vanishes_in_block=True,rows=rows,
             tested_representative_valuation_product=str(M),representative_minimum_log_abs_x=ball(aq(Q(M,17)).log()),
             scope='The two-sided failed blocks imply a rigorous necessary open x interval '
                   'for every real y, by convexity. The representative valuation product '
                   'is not proved necessary for all local protection solutions. '
                   'Comparison of this product excludes only that certified representative strategy.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print([(r['sign'],r['last_positive_bit'],r['first_negative_bit'],r['outside_log_abs']) for r in rows],
          'representative log min',out['representative_minimum_log_abs_x'],flush=True)


if __name__=='__main__':main()
