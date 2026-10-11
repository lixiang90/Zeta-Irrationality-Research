"""Exact gain of the complete proved six-pole bound, alpha=1/8 only."""
import json
from pathlib import Path
from fractions import Fraction as F
from first_layer_gain import integral


if __name__=='__main__':
    pieces=[(F(1,3),F(11,32),F(-10),F(15,4)),
            (F(11,32),F(7,20),F(-2),F(1)),
            (F(7,20),F(3,8),F(-7),F(11,4))]
    gain=sum(integral(l,r,s,b) for l,r,s,b in pieces)
    assert gain==F(127,11520)
    assert gain-F(1,96)==F(7,11520)
    result=dict(alpha='1/8',window=['1/3','3/8'],
        bound='48*N-24*p+22+a-max(0,min(a,2*(3*N-p+1)-a))',
        proved_gain=str(gain),gain_float=float(gain),
        additional_over_second_layer=str(gain-F(1,96)),
        pieces=[dict(left=str(l),right=str(r),slope=str(s),intercept=str(b)) for l,r,s,b in pieces],
        scope='Uniform local bound only. No complete global arithmetic constant or real-side gap has been updated.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
