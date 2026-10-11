"""Exact Bernoulli localization and uniform higher-layer annihilators.

For p>=7, F=prod_{1<=c< p/2}(t+c^2), s>=1 and p>2s+3:
    mu(t^s F^(2s+6) Q) in p^(2s+1) Z_(p).
Also mu(F^8 Q) = (7p/12) Q(0) mod p^2.
The normalized leading layer is mu_s times the coefficient of t^-1 in
Q / (t Fbar^2). It vanishes for deg Q < p-1, but generally not at degree p-1.
Proofs, including limitations for rational quotients, are in the report.
"""
import json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_mat
from joint_exact import Dcache,moment
from joint_padic import val,residue
from distribution_second_layer import shifted_moments

def mu(P):
    return sum((c*moment(e) for e,c in enumerate(P)),fmpq(0))

def next_layer_moment(e,p):
    """[t^-1] t^e / (t (t^m-(-1)^m)^2), modulo p."""
    m=(p-1)//2
    if e==0 or e%m:return 0
    j=e//m
    return (j-1)*pow((-1)**m,j,p)%p

def localization(P,p):
    # Exact identity for H=(d/dx)^5[x^7 P(-x^2)].
    f=fmpq_poly([0]*7+[1])*fmpq_poly(P)(fmpq_poly([0,0,-1]))
    H=f
    for _ in range(5):H=H.derivative()
    d=H;total=fmpq(0)
    for k in range(H.degree()+1):
        total+=fmpq.bernoulli(k)*fmpq(p)**(k-1)/math.factorial(k)/720*(
                    d(0)+2*sum(d(c) for c in range(1,(p+1)//2)))
        d=d.derivative()
    return total

if __name__=='__main__':
    checks=[]
    for p in [7,11,13,17,19,23,29,31,37,41,43,47,53,59]:
        F=Dcache((p-1)//2)
        vals=shifted_moments(F**8,p+3)
        assert all(val(v-fmpq(7*p,12)*int(e==0),p)>=2 for e,v in enumerate(vals))
        if p>7:assert val(vals[0],p)==1
        checks.append(dict(p=p,rank_one_checks=len(vals),constant_valuation=val(vals[0],p)))
    annihilators=[]
    for p in [7,11,13,17,19,23,29,31,37,41,43]:
        F=Dcache((p-1)//2)
        for s in range(1,5):
            if p<=2*s+3:continue
            P=fmpq_poly([0]*s+[1])*F**(2*s+6)
            vals=shifted_moments(P,p+3)
            assert all(val(v,p)>=2*s+1 for v in vals)
            coefficient=residue(moment(s),p,0)
            assert all(residue(v,p,2*s+1)==coefficient*next_layer_moment(e,p)%p
                       for e,v in enumerate(vals))
            assert all(val(v,p)>=2*s+2 for v in vals[:p-1])
            if coefficient:assert val(vals[p-1],p)==2*s+1
            minimum=min(val(v,p) for v in vals)
            annihilators.append(dict(p=p,s=s,checks=len(vals),lower=2*s+1,
                                     leading_coefficient=coefficient,
                                     actual_minimum=minimum,
                                     first_minimum=next(e for e,v in enumerate(vals) if val(v,p)==minimum)))
    exact=[]
    for p in [7,11,13]:
        for P in [fmpq_poly([1,2,0,-3,1]), fmpq_poly(Dcache((p-1)//2)**6),
                  fmpq_poly([0,1])*Dcache((p-1)//2)**8]:
            assert localization(P,p)==mu(P)
            exact.append(dict(p=p,degree=P.degree()))
    ranks=[]
    for p in [7,11,13,17,19,23,29,31,37,41,43]:
        gram=nmod_mat(p,p,[next_layer_moment(i+j,p) for i in range(p) for j in range(p)],p)
        det=int(gram.det());assert det==pow(-1,p*(p-1)//2,p)
        ranks.append(dict(p=p,rank=p,determinant=det))
    result=dict(rank_one_checks=sum(r['rank_one_checks'] for r in checks),
                annihilator_checks=sum(r['checks'] for r in annihilators),
                exact_localization_checks=len(exact),next_layer_ranks=ranks,rank_one=checks,
                annihilators=annihilators,localization=exact)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['rank_one','annihilators','localization']}),flush=True)
    print(json.dumps(annihilators),flush=True)
