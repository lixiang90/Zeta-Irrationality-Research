"""Fixed integrated tuple, exact cutoff audit; no legacy producer execution."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = 'cdt_odd_level20_integrated_tensor_bridge_20261006'
checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)
def polyadd(p, q):
    return tuple(a+b for a,b in zip(p,q))
def polysub(p, q):
    return tuple(a-b for a,b in zip(p,q))
def value(p, x):
    return p[0]+p[1]*x+p[2]*x*x
def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)), F(0))
def ipoly(m, mid):
    if mid < 1:
        return (F(3,2)+(m-1)*harmonic(m-2)+harmonic(m-1)/2,
                F(-m), F(1,2))
    p = (F(0),F(0),F(0))
    for h in range(1,m):
        if m-1-h*mid>0:
            p = polyadd(p, (F(m-1,h),F(-1),F(0)))
    for k in range(1,m):
        y = m-k*mid
        if y>=1:
            p = polyadd(p, (F(1,2*k),F(0),F(0)))
        elif y>0:
            p = polyadd(p, (F(m*m,2*k),F(-m),F(k,2)))
    return p
def gamma_poly(mid):
    if mid<F(1,3):
        return (F(0),F(3),F(-3))
    if mid<F(2,3):
        return (F(1,6),F(2),F(-3,2))
    return (F(5,6),F(0),F(0))
def gamma(x):
    return value(gamma_poly(x), x)

m=8
sigmas=[0,1,2,2,2,3,3,3]
es=[0,0,0,0,1,0,0,0]
nus=[a+b for a,b in zip(sigmas,es)]
flat=sum(F(2*i-1)*s for i,s in enumerate(sigmas,1))/m**2
check('actual_nested_unit_flat',flat==F(81,32))
check('sequence_factors',sum(es)==max(es)==1)
check('prefix_valuations',nus==[0,1,2,2,3,3,3,3])
floor_counts=[sum(3-n>=k for n in nus) for k in [1,2,3]]
check('three_background_thresholds',floor_counts==[4,2,1])
check('floor_sum',sum(3-n for n in nus)==7)
check('matching_total_baseline',F(sum(nus),m)==3-F(7,m))
check('matching_flat_sharp_baseline',F(sum(sigmas),m)+F(sum(es),m)==F(17,8))
check('gamma_continuous_1_3',value((F(0),F(3),F(-3)),F(1,3))==value((F(1,6),F(2),F(-3,2)),F(1,3)))
check('gamma_continuous_2_3',value((F(1,6),F(2),F(-3,2)),F(2,3))==F(5,6))
check('gamma_saturation',gamma(F(1))==F(5,6))
check('m8_C_direct',F(3,2)+7*harmonic(6)+harmonic(7)/2==F(1117,56))

points={F(0),F(1,3),F(2,3),F(1),F(m)}
for j in range(1,m):
    points.update(t for t in [F(m-1,j),F(m,j)] if 1<t<m)
points=sorted(points)
pieces=[]
minimum=None
argmin_intervals=[]
for lo,hi in zip(points,points[1:]):
    mid=(lo+hi)/2
    I=ipoly(m,mid)
    P=polyadd(I,(F(0),F(1),F(0)))
    Q=polysub(P,gamma_poly(mid))
    candidates=[lo,hi]
    if Q[2]:
        vertex=-Q[1]/(2*Q[2])
        if lo<=vertex<=hi:
            candidates.append(vertex)
    qmin=min(value(Q,t) for t in candidates)
    check(f'cutoff_piece_{lo}_{hi}_lower',qmin>=F(20,3))
    if Q[1]==Q[2]==0 and Q[0]==F(20,3):
        argmin_intervals.append([lo,hi])
    minimum=qmin if minimum is None else min(minimum,qmin)
    pieces.append({'lo':str(lo),'hi':str(hi),'I':list(map(str,I)),
                   'P_minus_gamma':list(map(str,Q)),
                   'minimum':str(qmin)})
for left,right in zip(pieces,pieces[1:]):
    t=F(left['hi'])
    check(f'continuity_at_{t}',value(tuple(map(F,left['I'])),t)==value(tuple(map(F,right['I'])),t))
check('unified_minimum_P_minus_gamma',minimum==F(20,3))
check('complete_constant_minimizer_interval',argmin_intervals==[[F(4),F(7)]])
kappa=flat+2*minimum/m**2
check('exact_integrated_kappa',kappa==F(263,96))
check('rank8_necessary_scale',m*kappa/(m-1)==F(263,84))
check('rank8_scale_above_14_5',F(263,84)>F(14,5))
family=[]
for rank,old,wanted in [(13,F(1345,468),F(335,117)),
                         (14,F(2577,910),F(3853,1365)),
                         (15,F(1769,630),F(14,5))]:
    optimistic=old-F(5,3*rank*(rank-1))
    check(f'family_{rank}_optimistic_gain',optimistic==wanted)
    check(f'family_{rank}_floor',optimistic>=F(14,5))
    family.append({'rank':rank,'old_relaxed_necessary_scale':str(old),
                   'max_known_S1_S2_credit':str(F(5,3*rank*(rank-1))),
                   'new_optimistic_lower_bound':str(optimistic)})
check('family13_gap',F(335,117)-F(14,5)==F(37,585))
check('family14_gap',F(3853,1365)-F(14,5)==F(31,1365))
term=F(1)
exp_lower=term
for j in range(1,11):
    term*=F(14,5)/j
    exp_lower+=term
check('positive_Taylor_log16_bound',exp_lower>16)
check('height_gain_to_final_cost',F(5,6)/m*F(2,m)==F(5,3*m*m))
report={'status':'fixed_integrated_tensor_cutoff_exact_audit_passed',
        'scope':'Fixed rank8 unit array; full cutoff rational verification. '
                'Three legacy family lower constants reused read-only; no legacy producer run.',
        'check_count':len(checks),'checks':checks,'cutoff_pieces':pieces,
        'constant_minimizer_intervals':[[str(a),str(b)] for a,b in argmin_intervals],
        'kappa':str(kappa),'rank8_necessary_rho':str(m*kappa/(m-1)),
        'optimistic_families':family,'exp_14_5_11_term_lower':str(exp_lower),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/(BASE+'_verify.json')
target.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'{len(checks)} fixed exact checks passed; {target.name}')
