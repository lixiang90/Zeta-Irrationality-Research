"""Exact tests of the localized Bernoulli functional modulo p and p^2."""
import json
from pathlib import Path
from math import prod
from sympy import primerange
from joint_exact import moment
from joint_padic import residue

def finite_sum_moments(p,n):
    modulus=p*p;inv720=pow(720,-1,modulus)
    powers=[a*a%modulus for a in range(1,p)]
    steps=powers[:];rows=[]
    for e in range(n):
        value=(-1)**e*prod(2*e+r for r in range(3,8))*inv720*sum(powers)%modulus
        actual=residue(moment(e),p,-1,precision=2)
        assert value==actual,(p,e,value,actual)
        rows.append(value)
        powers=[a*b%modulus for a,b in zip(powers,steps)]
    return rows

if __name__=='__main__':
    counts=[]
    for p in primerange(7,60):
        rows=finite_sum_moments(p,6*p)
        counts.append(dict(p=p,moments_checked=len(rows),first_nonintegral=next(e for e,x in enumerate(rows) if x%p)))
        assert counts[-1]['first_nonintegral']==3*p-4
    Path(__file__).with_suffix('.json').write_text(json.dumps(counts,indent=2))
    print(json.dumps(dict(primes=len(counts),checks=sum(r['moments_checked'] for r in counts),rows=counts)),flush=True)
