"""Two fixed BB gauge examples at the two prescribed primes 11 and 13.

No prime/parameter search. General packet necessity is proved in the report.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

def vp(x,p):
    assert x
    a,b=abs(x.numerator),x.denominator
    k=0
    while a%p==0:
        a//=p
        k+=1
    while b%p==0:
        b//=p
        k-=1
    return k

def residue(x,p):
    assert x.denominator%p
    return x.numerator%p*pow(x.denominator%p,-1,p)%p

def f_const(n):
    harm=F(0)
    total=F(0)
    for k in range(1,n+1):
        total+=F((-1)**(k-1),k**3*comb(2*k,k))*(F(1,k**4)+5*harm)
        harm+=F(1,k**4)
    return -F(5,2)*comb(2*n,n)*total

def uv(n):
    harm=sum((F(1,k**4) for k in range(1,n)),F(0))
    return ((-1)**n*(F(1,n**5)+F(5,n)*harm),
            (-1)**n*(F(1,n**6)+F(5,n**2)*harm))

def second_example(n):
    u,v=uv(n)
    return u+v+10*F((-1)**(n-1),(n-1)**4)

cases=[]
for p in [11,13]:
    n=p+2
    first=(n-1)**7*f_const(n)
    first_previous=p**7*f_const(p+1)
    # (theta-1)^7 kills the p+1 packet, but at p+2 it preserves -15.
    first_previous*=p**7
    target1=residue(p**7*first,p)
    assert vp(first,p)==-7 and target1==(-15)%p
    assert residue(first_previous,p)==0
    second=second_example(n)
    previous=second_example(p+1)
    target2=residue(p**4*second,p)
    assert vp(second,p)==-4 and target2==residue(-F(15,4),p)
    assert residue(p**4*previous,p)==0
    cases.append({'p':p,
                  'theta_minus_one_pow7_f_index':n,
                  'theta_minus_one_pow7_f_valuation':vp(first,p),
                  'theta_minus_one_pow7_f_p7_residue':target1,
                  'theta_minus_one_pow7_f_p_plus_one_residue':residue(first_previous,p),
                  'U_plus_V_plus_10zL4_index':n,
                  'U_plus_V_plus_10zL4_valuation':vp(second,p),
                  'U_plus_V_plus_10zL4_p4_residue':target2,
                  'U_plus_V_plus_10zL4_p_plus_one_residue':residue(p**4*previous,p)})

result={'scope':'Two prescribed fixed rational gauge examples; all-prime proof remains in the report.',
        'parameter':'c=0 for the exact f coefficient examples; the proof covers every fixed rational c.',
        'expected_first_packet':'-15 modulo p',
        'expected_second_packet':'-15/4 modulo p',
        'second_gauge':'U+V+10z*L4; p+1 packet cancelled, p+2 packet survives',
        'cases':cases,'all_exact_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
