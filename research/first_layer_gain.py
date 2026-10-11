"""Exact window gain from the proved first-layer bound, alpha=1/8 only."""
import json
from pathlib import Path
from fractions import Fraction as F


def integral(l,r,slope,intercept):return slope*(r*r-l*l)/2+intercept*(r-l)


if __name__=='__main__':
    l=F(1,3);r=F(3,8)
    gain=integral(l,r,F(-5),F(2))
    assert gain==F(11,1152)
    old=json.loads(Path(__file__).with_name('coupled_conditional_gain.json').read_text())
    conjectural=F(old['conditional_gain']);remaining=conjectural-gain
    assert remaining==F(17,11520)
    result=dict(alpha='1/8',window=[str(l),str(r)],
                uniform_local_bound='42*N-22*p+20+a',
                new_density='17/4-19*y',previous_density='9/4-14*y',
                gain_density='2-5*y',proved_window_gain=str(gain),gain_float=float(gain),
                still_conjectural_additional_gain=str(remaining),
                scope='This is an improvement of the named old bound in this window at alpha=1/8. No full arithmetic constant or alpha=1/40 gap is updated.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
