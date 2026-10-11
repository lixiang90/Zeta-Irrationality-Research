"""Exact alpha=1/8 window gain from the two-sided kernel determinant bound."""
import json
from pathlib import Path
from fractions import Fraction as F
from first_layer_gain import integral


if __name__=='__main__':
    left=F(1,3);right=F(3,8)
    gain=integral(left,right,F(-6),F(19,8))
    first=F(11,1152)
    full=F(127,11520)
    assert gain==F(1,96) and gain-first==F(1,1152)
    assert full-gain==F(7,11520)
    result=dict(alpha='1/8',window=[str(left),str(right)],
        uniform_local_bound='45*N-23*p+21+a',
        new_density='37/8-20*y',previous_density='9/4-14*y',
        gain_density='19/8-6*y',proved_window_gain=str(gain),gain_float=float(gain),
        additional_gain_over_first_layer=str(gain-first),
        still_conjectural_additional_gain=str(full-gain),
        scope='Only the named window at alpha=1/8 is updated. No full arithmetic constant, real-side bound, or alpha=1/40 gap has been recomputed.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
