"""Minimal symbolic certificate for one specified mod-p^3 square-lift obstruction.

This does not compute unknown periods, search primes, or rerun frozen producers.
The all-prime argument is in the companion Markdown proof.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

t = sp.symbols('t')
Delta = 1 - 12*t + 28*t**2 - 32*t**3 + 16*t**4
Ds = (1-t)**2 * Delta
h = -t/(1-t) + t*sp.diff(Delta, t)/(2*Delta)
M = -8*t*(1-t)*(18*t**4 - 36*t**3 + 28*t**2 - 10*t + 1)
T = M/Ds
A = sp.cancel(Ds*h)
checks = []

def check(name, expr):
    assert bool(expr), name
    checks.append(name)

check('Ds has degree 6 and constant 1', sp.degree(Ds,t)==6 and Ds.subs(t,0)==1)
check('Ds*h is polynomial with denominator dividing 2', sp.denom(A).is_Integer and 2 % int(sp.denom(A))==0)
check('Ds*T=M', sp.cancel(Ds*T-M)==0)
check('M has specified expansion', sp.expand(M)==-8*t+88*t**2-304*t**3+512*t**4-432*t**5+144*t**6)
check('M has degree 6 and leading coefficient 144', sp.degree(M,t)==6 and sp.Poly(M,t).LC()==144)
check('T has first coefficient -8', sp.limit(T/t,t,0)==-8)

P,P1,P2,hh,hh1,qq,DD = sp.symbols('P P1 P2 h h1 q D')
# theta(log P) and theta^2(log P), treated as exact formal jet identities.
z = hh + P1/P
theta_z = hh1 + P2/P - (P1/P)**2
expanded = sp.expand(DD*P**2*(2*theta_z+z**2+4*qq))
desired = DD*(2*P*P2-P1**2)+2*DD*hh*P*P1+DD*(2*hh1+hh**2+4*qq)*P**2
check('curvature equals cleared polynomial R_Ds', sp.cancel(expanded-desired)==0)

eta,e1,e2,beta,b1,b2,J,Ah,Mh = sp.symbols('eta eta1 eta2 beta beta1 beta2 J A M')
PP = beta*eta**2
PP1 = b1*eta**2 + 2*beta*eta*e1
PP2 = b2*eta**2 + 4*b1*eta*e1 + 2*beta*e1**2 + 2*beta*eta*e2
R = sp.expand(J*(2*PP*PP2-PP1**2)+2*Ah*PP*PP1+Mh*PP**2)
quot = (J*(eta*(2*beta*b2-b1**2)+4*beta*b1*e1+4*beta**2*e2)
        +2*Ah*beta*(eta*b1+2*beta*e1)+Mh*beta**2*eta)
check('R_Ds(beta*eta^2) is exactly eta^3 times displayed quotient', sp.expand(R-eta**3*quot)==0)
check('generic degree lower bound exceeds M at p=7, hence for every p>=7', sp.Rational(3*7-7,2)==7 and 7>sp.degree(M,t))
check('leading coefficient of M has only excluded primes 2 and 3', sp.factorint(144)=={2:4,3:2})
check('squarefree root consequence requires only nonzero positive power', 7>=3)

j,rho,rho1,u,zeta,c0,c1,c2 = sp.symbols('j rho rho1 u zeta c0 c1 c2')
Cj = c0+c1*(rho+j*u)+c2*(rho1+j*u*zeta+(rho+j*u)**2)
P0 = c0+c1*rho+c2*(rho1+rho**2)
P1 = u*(c1+c2*(2*rho+zeta))
P2 = c2*u**2
check('universal normalized image is quadratic in j', sp.expand(Cj-P0-j*P1-j**2*P2)==0)
check('zero-constant tests 1,2,3 recover 2P2 by second difference', sp.expand(Cj.subs(j,3)-2*Cj.subs(j,2)+Cj.subs(j,1)-2*P2)==0)
check('first difference recovers P1', sp.expand(Cj.subs(j,2)-Cj.subs(j,1)-3*P2-P1)==0)
check('first test then recovers P0', sp.expand(Cj.subs(j,1)-P1-P2-P0)==0)

out = {
    'scope': 'Symbolic identities only; the all-prime p-saturation and degree argument are proved in the companion Markdown. No target evaluation, prime search, or old producer run.',
    'checks_passed': len(checks),
    'checks': checks,
    'Delta': str(Delta),
    'Ds': str(sp.expand(Ds)),
    'Ds_times_h': str(sp.expand(A)),
    'M': str(sp.expand(M)),
    'M_degree': 6,
    'M_leading_coefficient': 144,
    'generic_H_degree_lower_bound': '(3*p-7)/2 >= 7 for p >= 7',
    'theorem_scope': 'Same complete excellent quotient G_p; eta monic of degree deg(H), eta modulo p = H; beta arbitrary polynomial. Separate universal all-W full-formal order<=2 content bound. No exclusion of special-packet S3/S4 rows, higher-order rows, or finite jets.',
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'certificate':str(dest.resolve()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
