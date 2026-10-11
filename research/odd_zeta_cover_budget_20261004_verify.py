"""Exact cover identities, finite piecewise optimization, and Arb radius bound.

There is no parameter scan. All-prime denominator witnesses are proved in the
companion report. Actual rank after the cover is a separate root-task input.
"""
from pathlib import Path
import json
import sympy as sy
from flint import arb, ctx

s, w, xi = sy.symbols('s w xi')
rho = 4*s**4/(1+s**4)**2
rp = sy.diff(rho,s)
D = s**8-14*s**4+1
fa = (1+s**4)/(4*s)
fb = -(1+s**4)/(4*s**3)
ua = sy.factor(rho/rp*sy.diff(fa,s))
ub = sy.factor(rho/rp*sy.diff(fb,s))
forcing = sy.factor(fa/(1+s**4)+fb*s**2/(1+s**4))
k = 2*w/(1-4*w)
r = -10*w/(1-4*w)
t = -12*w/(1-4*w)
K = 32*s**3*(1-s**4)/((1+s**4)*D)
P = -4*s**2*(7-s**4)/D
Q = 4*(1-7*s**4)/D
checks = {
    'F_derivative_rational_forcing_zero': forcing,
    'K_chain_rule_difference': sy.factor(rp/rho*k.subs(w,rho)-K),
    'P_chain_rule_difference': sy.factor(rp/rho*(r.subs(w,rho)*fa+t.subs(w,rho)*ua)-P),
    'Q_chain_rule_difference': sy.factor(rp/rho*(r.subs(w,rho)*fb+t.subs(w,rho)*ub)-Q),
    'one_minus_four_rho_difference': sy.factor(1-4*rho-D/(1+s**4)**2),
}
assert all(v == 0 for v in checks.values())

pieces = [
    (sy.Integer(0),sy.Integer(1), sy.Rational(83,12)-4*xi+xi**2/2),
    (sy.Integer(1),sy.Rational(4,3),sy.Rational(21,4)-2*xi+(4-3*xi)**2/6),
    (sy.Rational(4,3),sy.Rational(3,2),sy.Rational(21,4)-2*xi),
    (sy.Rational(3,2),sy.Integer(2),sy.Rational(7,2)-xi+(2-xi)**2),
    (sy.Integer(2),sy.Integer(3),sy.Rational(7,2)-xi),
    (sy.Integer(3),sy.Integer(4),(4-xi)**2/2),
]
# An exact exhaustive optimization of six explicitly proved quadratic pieces.
def minimum(linear_cost):
    vals=[]
    for lo,hi,ip in pieces:
        gp=sy.expand(linear_cost*xi+ip)
        points=[lo,hi]
        for cp in sy.solve(sy.diff(gp,xi),xi):
            if cp.is_real and lo <= cp <= hi:
                points.append(cp)
        vals.extend([sy.simplify(gp.subs(xi,p)) for p in points])
    return min(vals)
min1, min2 = minimum(1),minimum(2)
assert min1 == sy.Rational(7,2)
assert min2 == sy.Rational(21,4)
for j in range(5):
    hi=pieces[j][1]
    assert sy.simplify(pieces[j][2].subs(xi,hi)-pieces[j+1][2].subs(xi,hi)) == 0

ctx.prec=200
R4=(arb(3)/8).gamma()**2*(arb(1)/4).gamma()/(4*(arb(3)/4).gamma()*(arb(5)/8).gamma()**2)
logR4=R4.log()
radius_check = (arb('2.01967414836515') < R4 < arb('2.01967414836517'))
log_check = (arb('0.702') < logR4 < arb('0.703'))
budget_check = logR4 < arb(15)/16
assert radius_check and log_check and budget_check

result={
    'symbolic_cover_checks': {k:str(v) for k,v in checks.items()},
    'I_piecewise': [{'lo':str(lo),'hi':str(hi),'I':str(sy.expand(ip))} for lo,hi,ip in pieces],
    'exact_min_xi_plus_I': str(min1),
    'exact_min_2xi_plus_I': str(min2),
    'one_log_sharp_cost': str(min1/8),
    'two_logs_sharp_cost': str(min2/8),
    'natural_safe_flat_cost': '35/64',
    'natural_safe_total_cost': '77/64',
    'necessary_natural_table_costs_by_logs_using_n': ['15/16','19/16','35/32'],
    'R4_Arb': str(R4),
    'log_R4_Arb': str(logR4),
    'strict_radius_bracket_certified': bool(radius_check),
    'strict_log_bracket_certified': bool(log_check),
    'best_natural_table_cost_exceeds_log_R4': bool(budget_check),
    'Arb_precision_bits': ctx.prec,
    'scope': 'Natural 1,A,B,f_c(rho) table only; not arbitrary rational gauge or another cover.',
    'all_checks_passed': True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
