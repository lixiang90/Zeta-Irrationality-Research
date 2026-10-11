"""One bounded exact-rational evaluation of round216 logarithmic expressions.

No finite-N coefficient, rank, determinant, prime scan or historical producer.
Log intervals use a positive atanh series with a rigorous geometric tail.
This verifies explicit expression values, not the mathematical derivations.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import json

TERMS = 160

def log_ratio(lo, hi):
    z = F(hi-lo, hi+lo)
    zz = z*z
    power = z
    total = F(0)
    for j in range(TERMS):
        total += 2*power/(2*j+1)
        power *= zz
    tail = 2*power/F(2*TERMS+1)/(1-zz)
    return total, total+tail

L2 = log_ratio(1, 2)

def log_integer(q):
    if q == 1:
        return F(0), F(0)
    k = q.bit_length()-1
    r0, r1 = log_ratio(1 << k, q)
    return k*L2[0]+r0, k*L2[1]+r1

def atom(q, coefficient=1):
    return (F(0), {q: F(coefficient)})

def constant(q):
    return (F(q), {})

def combine(*items):
    c = F(0)
    d = {}
    for scale, (a, b) in items:
        c += scale*a
        for k, v in b.items():
            d[k] = d.get(k, F(0)) + scale*v
    return c, {k:v for k,v in d.items() if v}

def X(q):
    if q == 0:
        return constant(0)
    return combine((1, constant(-F(q*q,4))), (1, atom(q,F(q*q,2))))

def H(a, b, c):
    return combine((1,X(a)), (1,X(b+a)), (-1,X(b)),
                   (1,X(c+a)), (-1,X(c)), (-1,X(b+c+2*a)),
                   (1,X(b+c+a)))

V = combine((F(1,2),X(90)), (-1,X(54)), (F(1,2),X(18)),
            (-648,atom(36)), (1,constant(324)))
C = combine((46,atom(46)), (-44,atom(44)), (63,atom(63)), (-65,atom(65)))
JD = combine((2,V), (1,H(44,38,4)), (-1,H(8,110,4)))
PREFIX = combine((2592,atom(2)), (F(1,2),H(44,11,0)), (F(1,2),H(8,110,4)))
UM = combine((1,PREFIX),(36,C))
UD = combine((2592,atom(2)), (1,V), (F(1,2),H(44,38,4)), (F(1,2),H(44,11,0)))
BM = combine((38,atom(38)),(2,atom(2)),(-40,atom(40)))
UM_ONLY = combine((1,PREFIX),(18,BM))

expressions = {'endpoint_C_star':C,'C_vandermonde_leading':V,
               'minimal_D_input_Gram_leading':JD,
               'complete_mixed_trace_upper':UM,
               'D_only_joint_upper_not_mixed':UD,
               'M_only_component_upper_not_mixed':UM_ONLY,
               'mixed_trace_gap_against_existing_entry_lower':combine((1,UM),(1,constant(11440))),
               'mixed_trace_gap_against_proposed_content_lower_PENDING_PAPER_AUDIT':combine((1,UM),(1,constant(F(27323,4))))}

def decimal_bound(x, mode):
    with localcontext() as ctx:
        ctx.prec = 70
        ctx.rounding = mode
        return str(Decimal(x.numerator)/Decimal(x.denominator))

results = {}
for name, (c, d) in expressions.items():
    low = high = c
    for q, coeff in d.items():
        a,b = log_integer(q)
        low += coeff*(a if coeff>0 else b)
        high += coeff*(b if coeff>0 else a)
    assert low <= high
    results[name] = {'lower':decimal_bound(low,ROUND_FLOOR),
                     'upper':decimal_bound(high,ROUND_CEILING),
                     'rational_constant':str(c),
                     'log_coefficients':{str(k):str(v) for k,v in sorted(d.items())}}
assert F(results['endpoint_C_star']['upper']) < 0
assert F(results['mixed_trace_gap_against_existing_entry_lower']['lower']) > 0
assert F(results['mixed_trace_gap_against_proposed_content_lower_PENDING_PAPER_AUDIT']['lower']) > 0

receipt={'date':'2026-10-07','round':216,'actual_run':1,
         'scope':'exact expression evaluation only; no coefficient/rank/prime computations',
         'proof_method':'160 positive atanh terms after binary range reduction; exact Fraction sums and geometric upper tail; outward-rounded Decimal endpoints',
         'mathematical_derivations_not_verified_by_this_program':True,
         'proposed_arithmetic_lower_requires_separate_paper_audit':True,
         'expressions':results}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:{'lower':v['lower'],'upper':v['upper']} for k,v in results.items()},indent=2))
