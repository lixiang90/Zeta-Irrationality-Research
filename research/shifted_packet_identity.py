"""Exact Bernoulli reflection identity for 2q/2q+1 shifted zero packets.

The proof is in inner_window_extension_analysis.md. Finite checks below
independently verify the symbolic cancellation and p-adic remainder order.
"""
import json,math
from pathlib import Path
from flint import fmpq,fmpq_poly
from sympy import factorint
from joint_padic import val


def functional(poly,p=1):
    return sum((fmpq.bernoulli(k)*fmpq(math.prod(range(k+1,k+6)),720)
                *fmpq(p)**(k-1)*poly[k+5] for k in range(max(0,poly.degree()-4))),fmpq(0))


def packet(q,p=1,odd=False):
    z=fmpq_poly([1])
    for k in range(-q,q+int(odd)):z*=fmpq_poly([-k*p,1])
    return z


def run():
    t=fmpq_poly([0,1]);models=[];checks=[]
    for q in range(3,11):
        P=packet(q);Q=packet(q,odd=True);c=functional(P*t)
        assert functional(P)==0 and functional(Q)==c and functional(P*t*t)==-c
        models.append(dict(q=q,even_packet=[str(v) for v in P],first_scalar=str(c),
                           numerator_factors={str(k):int(v) for k,v in factorint(abs(int(c.p))).items()}))
        for p in [23,29,31,37]:
            assert p>2*q+1
            for a in [fmpq_poly([1]),t,t*t,fmpq_poly([2,-3,5,0,7,1]),t**(p+3)+2*t+3]:
                for odd in [False,True]:
                    got=functional(packet(q,p,odd)*a,p)
                    leading=c*p**(2*q-5)*a[0 if odd else 1]
                    diff=got-leading
                    assert not diff or val(diff,p)>=2*q-4
                    checks.append(dict(q=q,p=p,odd=odd,degree_a=a.degree(),mod_power=2*q-4))
    out=dict(status='Symbolic identities and finite congruence verification; not a determinant theorem.',
             models=models,congruence_checks=len(checks),checks=checks)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(dict(models=[{k:v for k,v in x.items() if k!='even_packet'} for x in models],checks=len(checks))),flush=True)
    return out


if __name__=='__main__':run()
