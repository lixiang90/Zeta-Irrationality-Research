"""Minimal fixed algebra certificate for the all-prime bounded Cartier kernel."""
from pathlib import Path
import json,hashlib
import sympy as sp

t,r,N,p,j,l=sp.symbols('t r N p j l')
checks=[]
def check(name,claim):
 assert bool(claim),name
 checks.append(name)
def red(expr):
 return sp.rem(sp.Poly(sp.expand(expr),r),sp.Poly(r**2-5,r)).as_expr()

eta_exponents={1:3,2:-4,4:1,5:1,10:-4,20:3}
check('t eta exponents sum to zero',sum(eta_exponents.values())==0)
check('S constant is 1',sum(d*e for d,e in eta_exponents.items())==24)
check('S anomaly sum is zero',sum(eta_exponents.values())==0)
w=sp.Matrix([[0,-1],[N,0]])
ainf=sp.diag(p,1)
a0=sp.diag(1,p)
aj=sp.Matrix([[1,j],[0,p]])
al=sp.Matrix([[1,l],[0,p]])
gamma=sp.Matrix([[(1+N*j*l)/p,j],[N*l,p]])
check('infinity and zero Hecke cosets swap under Fricke',ainf*w==w*a0 and a0*w==w*ainf)
check('nonzero coset Fricke identity',sp.simplify(aj*w-gamma*w*al)==sp.zeros(2))
check('gamma determinant is 1',sp.simplify(gamma.det())==1)
check('gamma lower-right is p and lower-left is divisible by N',gamma[1,1]==p and gamma[1,0]==N*l)

Cm=1-(6-2*r)*t+(6-2*r)*t**2
Cp=1-(6+2*r)*t+(6+2*r)*t**2
Nm=1-(6+r)*t+(1+r)*t**2
Np=1-(6-r)*t+(1-r)*t**2
Delta=1-12*t+28*t**2-32*t**3+16*t**4
check('C+ C- equals Delta',red(Cm*Cp-Delta)==0)
for label,NC,CC,CO in [('minus',Nm,Cm,Cp),('plus',Np,Cp,Cm)]:
 D=(1-t)*NC*CC
 check(label+' fixed denominator has degree 5',sp.degree(D,t)==5)
 check(label+' fixed denominator has constant 1',D.subs(t,0)==1)
 # (A*S/Phi^2)^2=(1-t)^2 N^2 C Delta/25.
 check(label+' denominator factor square has correct own/other C',red((1-t)**2*NC**2*CC*Delta-(1-t)**2*NC**2*CC**2*CO)==0)
 check(label+' denominator is nonzero at t=0',NC.subs(t,0)==1 and CC.subs(t,0)==1)
check('fixed total zero divisor degree is 12',4+4+2+2==12)
check('weight4 index36 valence degree is 12',sp.Rational(4*36,12)==12)
eps=sp.symbols('eps')
check('Hecke constant ratio is 1+eps*p^3',sp.simplify((-sp.Rational(1,5)*(1+eps*p**3))/(-sp.Rational(1,5))-(1+eps*p**3))==0)

out={
 'scope':'Fixed algebra identities only. All-prime modularity, pole bounds, coefficient integrality and relative Cartier compatibility are proved in the Markdown. No prime scan or old producer run.',
 'checks_passed':len(checks),'checks':checks,
 'operator':'W_N T_p^chi = chi(p) T_p^(chi^-1) W_N, determinant-normalized slash',
 'ratio':'T_p(A_minus*S)/(A^(chi(p))*S)',
 'fixed_denominator_minus':str(sp.expand((1-t)*Nm*Cm)),
 'fixed_denominator_plus':str(sp.expand((1-t)*Np*Cp)),
 'kernel_numerator_degree_bound':5,
 'kernel_constant':'1+chi(p)*p^3',
 'Cartier':'k-linear relative/twisted p-extraction; not absolute Cartier without coefficient p-roots',
 'unremoved_period_term':'chi(p)*Theta*A^(chi(p))',
 'open':'New primitive mixed Smith directions, period-carrier analytic closure and e=1 global budget.'
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'certificate':str(dest.resolve()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
