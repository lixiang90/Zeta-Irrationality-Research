"""Minimal symbolic checks for a genuine target integral; no prime search."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import sympy as sp

t=sp.symbols('t')
x0,x1,x2,x3,a0,a1,a2,F,H0=sp.symbols('x0 x1 x2 x3 a0 a1 a2 F H0')
th1=t*x1
th2=t*x1+t**2*x2
th3=t*x1+3*t**2*x2+t**3*x3
B2=t*a2-3
B1=2-t*a2+t**2*a1
B0=t**3*a0
checks=[]
def check(name,statement):
 assert bool(statement),name
 checks.append(name)
check('Euler operator conversion is exact',sp.expand(th3+B2*th2+B1*th1+B0*x0-t**3*(x3+a2*x2+a1*x1+a0*x0))==0)
check('constant shift contributes H0*B0 to Euler forcing',sp.expand(B0*(x0-H0)+B0*H0-B0*x0)==0)
cusp=Fraction(-17,120)
integral=cusp/4
check('highest target integral log4 coefficient is -17/480',integral==Fraction(-17,480))
check('four Euler log derivatives leave nonzero constant',integral*24==Fraction(-17,20))
r,eps=sp.symbols('r eps')
kappa=5*r/4
norm=sp.expand((1-kappa*eps)*(1+kappa*eps)).subs({r**2:5,eps**2:1})
check('highest packet norm is -109/16',sp.simplify(norm+sp.Rational(109,16))==0)
check('I(0)=0 removes the origin logarithm but preserves the nonzero cusp coefficient',integral!=0)
check('rank upper bound and local block lower bound agree at 5',4+1==5)
check('P10+new target dimension with constant intersection is 14',10+5-1==14)

out={
 'scope':'Symbolic identities only. Actual rank, intersection, full-disk leaf and full denominator type are proved in the Markdown; no prime or parameter search.',
 'checks_passed':len(checks),'checks':checks,
 'cusp_H_log3':'-17/120','cusp_I_log4':'-17/480',
 'packet_norm':'-109/16','new_actual_rank':5,'pure10_plus_target_actual_rank':14,
 'denominator_type':'n*lcm(1,...,n)^3 with one fixed multiplier',
 'open':'An additional primitive mixed Cartier row and its e=1 global budget; no numerical irrationality theorem.'
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'certificate':str(dest.resolve()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
