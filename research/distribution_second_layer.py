"""Exact second-layer functional on the canonical lift F_p(t)^6.

For p>=7, m=(p-1)/2, F_p=prod_{c=1}^m(t+c^2), Q in Z_(p)[t]:
  mu(F_p^6 Q) == -sum_{c=1}^m c Q(-c^2) (mod p).
The left side is p-integral. This is a theorem proved in the accompanying
report; these finite rational checks independently audit its implementation.
"""
import json,time
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_mat
from sympy import primerange
from joint_exact import Dcache,moment
from joint_padic import val,residue

def shifted_moments(P,n):
    return [sum((c*moment(i+e) for i,c in enumerate(P)),fmpq(0)) for e in range(n)]

def check_prime(p):
    m=(p-1)//2;F=Dcache(m);values=shifted_moments(F**6,2*m+2)
    predicted=[-sum(c*pow(-c*c,e,p) for c in range(1,m+1))%p for e in range(len(values))]
    for e,(v,y) in enumerate(zip(values,predicted)):
        assert val(v,p)>=0 and residue(v,p,0)==y,(p,e,v,y)
    # The Gram matrix on polynomials of degree <m has no second-layer radical.
    gram=nmod_mat(m,m,[predicted[i+j] for i in range(m) for j in range(m)],p)
    det=int(gram.det());expected=1
    for c in range(1,m+1):expected=expected*(-c)%p
    for c in range(1,m+1):
        for d in range(c+1,m+1):expected=expected*(c*c-d*d)**2%p
    assert det==expected!=0
    # Multiplicity seven, but not six, uniformly kills the next moment layer.
    seven=shifted_moments(F**7,m+1)
    assert all(val(v,p)>=1 for v in seven)
    assert predicted[0]!=0  # -m(m+1)/2 = 1/8 mod p.
    assert predicted[0]==pow(8,-1,p)
    # Check all Lagrange tests: they isolate one root and give weight -c.
    for c in range(1,m+1):
        L=F//fmpq_poly([c*c,1]);L=L/L(-c*c)
        actual=sum((a*values[e] for e,a in enumerate(L)),fmpq(0))
        assert residue(actual,p,0)==(-c)%p
    return dict(p=p,m=m,six_power_checks=len(values),seven_power_checks=len(seven),
                lagrange_checks=m,gram_rank=m,gram_determinant=det,
                mu_F6_mod_p=predicted[0])

if __name__=='__main__':
    start=time.time();rows=[]
    for p in primerange(7,60):
        rows.append(check_prime(p));print(json.dumps(rows[-1]),flush=True)
    result=dict(primes=len(rows),six_power_checks=sum(r['six_power_checks'] for r in rows),
                seven_power_checks=sum(r['seven_power_checks'] for r in rows),
                lagrange_checks=sum(r['lagrange_checks'] for r in rows),rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print('SUMMARY '+json.dumps({k:v for k,v in result.items() if k!='rows'})+f' seconds={time.time()-start:.1f}',flush=True)
