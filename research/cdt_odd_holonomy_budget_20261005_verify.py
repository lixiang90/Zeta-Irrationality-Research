"""Finite exact cost classification, not a numerical parameter or prime scan.

The 744 cases exhaust discrete n^e choices for r=1,...,5; the report proves
all r>=6 directly. Sorted row-sum costs are a relaxation of nested columns.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import factorial, comb
import json
import hashlib
import sympy as S

HERE=Path(__file__).resolve().parent
x=S.symbols('x')
def harmonic(n):
    return sum((S.Rational(1,j) for j in range(1,n+1)),S.Rational(0))
@lru_cache(None)
def Ipieces(m):
    points={S.Rational(1),S.Rational(m)}
    for h in range(1,m):
        points.update(t for t in [S.Rational(m-1,h),S.Rational(m,h)] if 1<t<m)
    points=sorted(points)
    C=S.Rational(3,2)+(m-1)*harmonic(m-2)+harmonic(m-1)/2
    pieces=[(S.Rational(0),S.Rational(1),C-m*x+x*x/2)]
    for lo,hi in zip(points,points[1:]):
        mid=(lo+hi)/2
        I=S.Rational(0)
        for h in range(1,m):
            if m-1-h*mid>0:
                I+=(m-1-h*x)/h
        for k in range(1,m):
            y=m-k*mid
            if y>=1:
                I+=S.Rational(1,2*k)
            elif y>0:
                I+=(m-k*x)**2/(2*k)
        pieces.append((lo,hi,S.expand(I)))
    return pieces
@lru_cache(None)
def sharp(m,total,maximum):
    if maximum==0:
        return S.Rational(0),S.Rational(0)
    possibilities=[]
    for lo,hi,I in Ipieces(m):
        P=S.expand(total*x+maximum*I)
        candidates=[lo,hi]
        der=S.diff(P,x)
        if der.has(x):
            root=S.solve(der,x)[0]
            if lo<=root<=hi:
                candidates.append(root)
        for t in candidates:
            possibilities.append((S.factor(S.Rational(2,m*m)*P.subs(x,t)),t))
    return min(possibilities,key=lambda q:q[0])
assert sharp(3,3,2)[0]==S.Rational(17,12)
assert sharp(4,6,3)[0]==S.Rational(63,32)

tables=[]
case_count=0
for r in range(1,6):
    m=r+3
    best=None
    # Every larger e is dominated, by all-scale necessary layer bounds.
    for e1,e2,e3 in product(range(2),range(3),range(4)):
        for aux in product(range(2),repeat=r-1):
            es=[0,e1,e2,e3]+list(aux)
            sigmas=[S.Rational(0),S.Rational(1-e1),S.Rational(2-e2),S.Rational(3-e3)]
            sigmas += [harmonic(ell-1 if e else ell) for ell,e in zip(range(2,r+1),aux)]
            sigmas=sorted(sigmas)
            flat=sum((2*i-1)*q for i,q in enumerate(sigmas,start=1))/(m*m)
            sh,at=sharp(m,sum(es),max(es))
            total=S.factor(flat+sh)
            case_count+=1
            item={'tau':total,'flat':S.factor(flat),'sharp':sh,'xi':at,
                  'e_polylogs':[e1,e2,e3],'e_log_powers':list(aux),'sorted_sigma_lower':sigmas}
            if best is None or total<best['tau']:
                best=item
    assert best['tau']>S.Rational(7,5)  # log4<7/5, proved in report.
    tables.append({'r':r,'m':m,'exhaustive_cases':24*2**(r-1),'minimum_relaxed_cost':best})
assert case_count==744

# One fixed coefficient identity: log^4/4! at n=3p+1,p=7 has valuation -3.
N=22
L=[Fraction(0)]+[Fraction(1,n) for n in range(1,N+1)]
def multiply(a,b):
    return [sum((a[j]*b[n-j] for j in range(n+1)),Fraction(0)) for n in range(N+1)]
power=[Fraction(1)]+[Fraction(0)]*N
for _ in range(4):
    power=multiply(power,L)
coef=power[N]/factorial(4)
def vp(q,p):
    a,b=q.numerator,q.denominator
    if not a:
        return None
    v=0
    while a%p==0:
        a//=p;v+=1
    while b%p==0:
        b//=p;v-=1
    return v
assert vp(coef,7)==-3

# Six discrete choices for the classical zeta3 tail-lift natural system.
lift=[]
for e1,e2 in product(range(2),range(3)):
    sigmas=sorted([S.Rational(0),S.Rational(1-e1),S.Rational(2-e2),S.Rational(3)])
    flat=sum((2*i-1)*q for i,q in enumerate(sigmas,start=1))/16
    sh,at=sharp(4,e1+e2,max(e1,e2))
    lift.append({'e':[0,e1,e2,0],'sigma':sigmas,'tau':S.factor(flat+sh)})
assert min(q['tau'] for q in lift)==S.Rational(17,8)

lift_augmented=[]
for r in range(1,6):
    m=r+3
    best=None
    for e1,e2 in product(range(2),range(3)):
        for aux in product(range(2),repeat=r-1):
            es=[0,e1,e2,0]+list(aux)
            sigmas=[S.Rational(0),S.Rational(1-e1),S.Rational(2-e2),S.Rational(3)]
            sigmas += [harmonic(ell-1 if e else ell) for ell,e in zip(range(2,r+1),aux)]
            sigmas=sorted(sigmas)
            flat=sum((2*i-1)*q for i,q in enumerate(sigmas,start=1))/(m*m)
            sh,at=sharp(m,sum(es),max(es))
            tau=S.factor(flat+sh)
            if best is None or tau<best['tau']:
                best={'tau':tau,'e':[e1,e2]+list(aux),'sigma_lower':sigmas,'xi':at}
    assert best['tau']>S.Rational(7,5)
    lift_augmented.append({'r':r,'minimum_relaxed_cost':best,'case_count':6*2**(r-1)})

# Fixed j=7 trace coefficient from the full symbolic coefficient formula.
j,n,p=7,4,7
trace_coefficient=sum((Fraction((-1)**h*comb(n,h),n*(n+h)**(j-1))
                       for h in range(n+1)),Fraction(0))
assert vp(trace_coefficient,p)==-6
source_prime_unit=4
A_first=-504
assert source_prime_unit*A_first==-2016
level_x,level_t=S.symbols('level_x level_t')
quotient=level_x/(1+8*level_x+12*level_x**2)
assert S.factor(quotient.subs(level_x,1/(12*level_x))-quotient)==0
assert S.discriminant(12*level_t*level_x**2+(8*level_t-1)*level_x+level_t,level_x)==16*level_t**2-16*level_t+1
assert S.Rational(7)*(1-S.Rational(1,64))==S.Rational(441,64)

# A new, different family: rank8 odd-weight target plus T_1,...,T_r.
# Lower sums are the all-scale row minima; upper sums use genuinely nested
# constant b=1 columns, so no compatibility of fractional scales is assumed.
odd_model_tate=[]
odd_model_type_cases=0
for r in range(11):
    m=r+8
    lower_best=upper_best=None
    for es in product(range(2),repeat=r):
        sh,at=sharp(m,sum(es),max(es,default=0))
        lower=sorted([S.Rational(0)]+[harmonic(j-e) for j,e in enumerate(es,1)]+[S.Rational(7)]*7)
        upper=sorted([S.Rational(0)]+[S.Rational(j-e) for j,e in enumerate(es,1)]+[S.Rational(7)]*7)
        def row_flat(row):
            return S.factor(sum((2*i-1)*v for i,v in enumerate(row,1))/(m*m))
        lf,uf=row_flat(lower),row_flat(upper)
        li={'tau':S.factor(lf+sh),'flat':lf,'sharp':sh,'xi':at,
            'e_Tate':list(es),'sigma_lower':lower}
        ui={'tau':S.factor(uf+sh),'flat':uf,'sharp':sh,'xi':at,
            'e_Tate':list(es),'sigma_safe':upper,'all_active_b':1}
        if lower_best is None or li['tau']<lower_best['tau']:
            lower_best=li
        if upper_best is None or ui['tau']<upper_best['tau']:
            upper_best=ui
        odd_model_type_cases+=1
    odd_model_tate.append({'r':r,'rank':m,'type_cases':2**r,
                           'minimum_relaxed_lower':lower_best,
                           'best_legal_unit_column_upper':upper_best})
assert odd_model_type_cases==2047
assert harmonic(10)>S.Rational(29,10)
assert harmonic(20)>S.Rational(7,2)
assert harmonic(40)>4
assert harmonic(80)>S.Rational(9,2)
assert harmonic(235)<7
# Each concave polynomial attains its interval minimum at an endpoint.
strengthened_flat=S.Rational(43,10)
harmonic_segment_bounds=[(10,20,S.Rational(29,10)),
                         (20,30,S.Rational(359,100)),
                         (30,45,S.Rational(399,100)),
                         (45,70,S.Rational(439,100))]
assert all(harmonic(a)>h for a,b,h in harmonic_segment_bounds)
assert harmonic(70)>S.Rational(483,100)
assert harmonic(56)>S.Rational(23,5)
global_lower_segments=[(a,b,S.expand(x*(x+2)*h-x*(x+5)/2+7*(14*x+63)-strengthened_flat*(x+8)**2))
                       for a,b,h in harmonic_segment_bounds]
assert all(P.subs(x,a)>0 and P.subs(x,b)>0 for a,b,P in global_lower_segments)
assert S.Rational(7)*(14*10+63)/(10+8)**2>strengthened_flat
assert S.Rational(23,5)*(1-S.Rational(57**2,244**2))>strengthened_flat
# A specific proposed h_Y0(2) cover has derivative <=16(2+sqrt3)<60;
# exp(41/10)>60 by a positive Taylor truncation, so log derivative<4.1.
assert (S.Rational(7,4))**2>3
assert sum((S.Rational(41,10)**k/S.factorial(k) for k in range(16)),S.Rational(0))>60

md=HERE/'cdt_odd_holonomy_budget_20261005.md'
payload={'scope':'Exact exhaustive discrete type relaxation; not an n/p parameter search.',
         'case_count':case_count,'polylog3_with_consecutive_log_powers':tables,
         'r_ge_6_flat_bound':str(S.Rational(199,135)),
         'zeta3_tail_lift_six_cases':lift,
         'zeta3_tail_lift_with_log_powers':lift_augmented,
         'fixed_Li7_trace_example':{'p':p,'n':n,'coefficient':str(trace_coefficient),'valuation':-6},
         'level12_highest_prime_packet':{'prime_unit':4,'A_first':-504,'product':-2016},
         'level12_Fricke_quotient':{'invariant':True,'discriminant':'16*t^2-16*t+1',
                                  'rank8_conditional_flat_cost':'441/64'},
         'rank8_odd_model_plus_Tate':{'complete_type_case_count':odd_model_type_cases,
                                     'r_0_through_10':odd_model_tate,
                                     'all_r_flat_strict_lower':'43/10',
                                     'global_concave_segments':[[str(a),str(b),str(P)] for a,b,P in global_lower_segments]},
         'one_fixed_log_packet':{'ell':4,'p':7,'n':22,'coefficient':str(coef),'valuation':-3},
         'I4_piecewise':[[str(a),str(b),str(P)] for a,b,P in Ipieces(4)],
         'report_sha256':hashlib.sha256(md.read_bytes()).hexdigest() if md.exists() else None,
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/'cdt_odd_holonomy_budget_20261005_verify.json'
target.write_text(json.dumps(payload,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'minimum_costs':[[r['r'],str(r['minimum_relaxed_cost']['tau'])] for r in tables],
                  'lift_minimum':'17/8',
                  'lift_augmented_minima':[[r['r'],str(r['minimum_relaxed_cost']['tau'])] for r in lift_augmented],
                  'rank8_plus_Tate_bounds':[[r['r'],str(r['minimum_relaxed_lower']['tau']),str(r['best_legal_unit_column_upper']['tau'])] for r in odd_model_tate],
                  'all_checks_passed':True},ensure_ascii=False))
