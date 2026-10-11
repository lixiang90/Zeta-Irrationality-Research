"""Fixed exact checks for the balanced Smith bridge; no source producer rerun."""
from fractions import Fraction as F
from pathlib import Path
import json

checks=[]
def check(label, condition):
    assert condition, label
    checks.append(label)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

for m,dist,baseline in [(4,[4,1,1,2],6),(7,[4,5,3,2],14)]:
    R=sum(dist); mass=sum(i*c for i,c in enumerate(dist))
    check(f'm{m}_local_floor_mass',mass==baseline+3)
    for d in [2,4]:
        poly=[1]
        for _ in range(d): poly=mul(poly,dist)
        check(f'm{m}_d{d}_tensor_rank',sum(poly)==R**d)
        check(f'm{m}_d{d}_tensor_floor_mass',sum(i*c for i,c in enumerate(poly))==d*R**(d-1)*mass)
        check(f'm{m}_d{d}_threshold_sum',sum(sum(poly[l:]) for l in range(1,3*d+1))==d*R**(d-1)*mass)

def gamma(a):
    u=min(a,F(2,3));v=min(a,F(1,3))
    return 2*u-F(3,2)*u*u+v-F(3,2)*v*v
check('gamma_1',gamma(F(1))==F(5,6))
check('gamma_two_thirds',gamma(F(2,3))==F(5,6))
check('gamma_one_third',gamma(F(1,3))==F(2,3))
check('unit4_tau',sum(F((2*i-1)*c,16) for i,c in enumerate([0,3,3,3],1))==F(45,16))
check('unit7_tau',sum(F((2*i-1)*c,49) for i,c in enumerate([0,1,2,2,3,3,3],1))==F(18,7))
check('unit4_kappa',F(45,16)-F(5,3*16)==F(65,24))
check('unit7_kappa',F(18,7)-F(5,3*49)==F(373,147))

records=[]
for name,r,extra,m,tau,kappa,gate in [
    ('B3',3,False,8,F(167,64),F(31,12),F(62,21)),
    ('B4',4,False,9,F(2597,972),F(859,324),F(859,288)),
    ('B5',5,False,10,F(1369,500),F(2041,750),F(2041,675)),
    ('B4_K2L',4,True,10,F(1087,400),F(3241,1200),F(3241,1080)),
]:
    theta=[F(0)]+[F(j) for j in range(1,r+1)]+[F(1)]+[F(1)]*3
    if extra: theta.append(F(2))
    theta.sort()
    a0=min(F(i)/v for i,v in enumerate(theta) if v)
    check(name+'_actual_rows',len(theta)==m)
    check(name+'_matching_window',a0==1)
    check(name+'_kappa',tau-F(5,3*m*m)==kappa)
    check(name+'_necessary_scale',F(m,m-1)*kappa==gate)
    check(name+'_still_above_29_10',gate>F(29,10))
    records.append(dict(name=name,m=m,a0=str(a0),tau=str(tau),kappa=str(kappa),necessary_rho=str(gate)))

check('log16_below_29_10',sum(F(29,10)**j/__import__('math').factorial(j) for j in range(12))>16)
out=dict(scope='exact finite floor/transport/arithmetic checks only; DVR, tensor flag, all-prime and limits proved in report',checks_passed=len(checks),check_labels=checks,fixed_arrays=records)
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} fixed exact checks passed; {dest}')
