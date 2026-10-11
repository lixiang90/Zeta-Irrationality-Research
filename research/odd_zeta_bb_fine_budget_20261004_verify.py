"""Fixed exact checks for the BB natural fine-budget report.

Three prescribed prime/prime-power examples support auditing; they are not
the all-prime proof. There is no parameter scan or numerical zeta call.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json

def vp_fraction(x,p):
    assert x != 0
    num,den=abs(x.numerator),x.denominator
    val=0
    while num % p == 0:
        num//=p
        val+=1
    while den % p == 0:
        den//=p
        val-=1
    return val

def prescribed_case(p,a):
    q=p**a
    N=q+1
    harm=F(0)
    terms=[]
    for n in range(1,N+1):
        term=F((-1)**(n-1),n**3*comb(2*n,n))*(F(1,n**4)+5*harm)
        terms.append(term)
        harm+=F(1,n**4)
    d=-F(5,2)*comb(2*N,N)*sum(terms,F(0))
    hn=sum((F(1,j**4) for j in range(1,N)),F(0))
    un=(-1)**N*(F(1,N**5)+F(5,N)*hn)
    vn=(-1)**N*(F(1,N**6)+F(5,N**2)*hn)
    values={
        't_q':vp_fraction(terms[q-1],p),
        'min_t_k_for_k_below_q': min(vp_fraction(t,p) for t in terms[:q-1]),
        't_q_plus_one':vp_fraction(terms[q],p),
        'f_q_plus_one_constant_part':vp_fraction(d,p),
        'U_q_plus_one':vp_fraction(un,p),
        'V_q_plus_one':vp_fraction(vn,p),
    }
    assert values['t_q'] == -7*a
    assert values['min_t_k_for_k_below_q'] >= -7*a+6
    assert values['t_q_plus_one'] == -4*a
    assert values['f_q_plus_one_constant_part'] == -7*a
    assert values['U_q_plus_one'] == values['V_q_plus_one'] == -4*a
    assert comb(2*q,q)%p==2 and comb(2*N,N)%p==4%p
    return {'p':p,'a':a,'q':q,'coefficient_index':N,
            'valuations':values,'constant_part_f_exact':str(d),
            'c_coefficient_f_integer':comb(2*N,N)}

table=[[0]*7 for _ in range(5)]+[[1]*4+[0]*3 for _ in range(2)]+[[1]*7]
for j in range(7):
    col=[row[j] for row in table]
    assert col == sorted(col) and set(col).issubset({0,1})
sigma=[sum(row) for row in table]
flat=sum((F(2*i+1,64)*sigma[i] for i in range(8)),F(0))
assert sigma == [0,0,0,0,0,4,4,7]
assert flat == F(201,64)
result={
    'scope':'Natural eight functions in the original coordinate, not an arbitrary rational gauge.',
    'prescribed_exact_cases':[prescribed_case(7,1),prescribed_case(11,1),prescribed_case(7,2)],
    'nested_lcm_safe_table':table,
    'row_sums':sigma,
    'safe_e_vector':[0,1,2,3,4,1,2,0],
    'flat_cost_exact':str(flat),
    'all_exact_checks_passed':True,
    'not_proved_by_sampling':['all sufficiently large primes','all prime powers','fine-budget necessity'],
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'cases':[{k:v for k,v in x.items() if k not in ['constant_part_f_exact','c_coefficient_f_integer']} for x in result['prescribed_exact_cases']],
                  'flat_cost_exact':str(flat),'all_exact_checks_passed':True},ensure_ascii=False,indent=2))
