"""Independent finite enumeration for the interval-cone minimax theorem."""
from fractions import Fraction as F
import json
import math
from pathlib import Path
import random

from farey_cone_optimizer import optimize


def ceil(x):
    return -((-x.numerator)//x.denominator)


def check(lo,hi):
    ans=optimize(lo,hi);eps=ans['epsilon'];Q=ans['Q']
    # Verify minimum denominator directly, without a continued-fraction routine.
    for q in range(1,Q):
        first=(lo*q).numerator//(lo*q).denominator+1
        last=ceil(hi*q)-1
        assert first>last
    inside=ans['inside'];assert inside.denominator==Q
    # Every vector with endpoint values in [0,eps] has |b| <= eps/(hi-lo).
    B=int(eps/(hi-lo))
    best=None;vectors=0
    for b in range(-B,B+1):
        a=ceil(max(-b*lo,-b*hi))
        if a==0 and b==0:a=1
        value=max(a+b*lo,a+b*hi)
        assert min(a+b*lo,a+b*hi)>=0
        best=value if best is None else min(best,value)
        vectors+=1
    assert best==eps
    return vectors


def main():
    rng=random.Random(20261001)
    cases=[]
    for _ in range(400):
        den=rng.randint(2,30)
        left=F(rng.randint(0,80),den)
        right=left+F(rng.randint(1,12),den)
        cases.append((left,right))
    for _ in range(160):
        center=F(rng.randint(1,300),rng.randint(2,99))
        width=F(1,rng.randint(1000,20000))
        cases.append((max(F(0),center-width),center+2*width))
    checked=sum(check(lo,hi) for lo,hi in cases)
    stalled=[]
    for n in (4,16,64,256):
        delta=F(1,2**n)
        lo=F(3,2)-delta;hi=F(3,2)+delta
        ans=optimize(lo,hi)
        assert ans['Q']==2 and ans['epsilon']==F(1,2)+delta
        # The positive small-form parallelogram has unbounded area but
        # contains no nonzero integer vector when its cap is 1/4.
        area=F(1,4)**2/(hi-lo)
        stalled.append(dict(n=n,minimum_denominator=2,optimal_bound=str(ans['epsilon']),
                            area_with_cap_one_quarter=str(area)))
    result=dict(random_interval_cases=len(cases),enumerated_integer_candidates=checked,
                rational_stagnation_examples=stalled)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
