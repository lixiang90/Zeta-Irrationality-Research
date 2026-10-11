"""Fixed algebra for the characteristic-p rational Cartier primitive.

No prime scan, no frozen-producer import, no numerical irrationality claim.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

t,r,p=sp.symbols('t r p')
checks=[]
def check(name,claim):
    assert bool(claim),name
    checks.append(name)
def red(expr):
    return sp.rem(sp.Poly(sp.expand(expr),r),sp.Poly(r*r-5,r)).as_expr()
def norm(expr):
    return red(expr*expr.subs(r,-r))

N=1-(6+r)*t+(1+r)*t*t
C=1-(6-2*r)*t+(6-2*r)*t*t
check('N discriminant is 37+8r',red(sp.discriminant(N,t)-(37+8*r))==0)
check('N discriminant norm is 1049',norm(red(sp.discriminant(N,t)))==1049)
check('C discriminant is 32-16r',red(sp.discriminant(C,t)-(32-16*r))==0)
check('C discriminant norm is -256',norm(red(sp.discriminant(C,t)))==-256)
check('own N C resultant is -80+60r',red(sp.resultant(N,C,t)-(-80+60*r))==0)
check('own resultant norm is -11600',norm(red(sp.resultant(N,C,t)))==-11600)
check('resultant fixed prime factorization',-11600==-2**4*5**2*29)
check('1049 is prime',sp.isprime(1049))
check('N values at 0 and 1',N.subs(t,0)==1 and N.subs(t,1)==-4)
check('C values at 0 and 1',C.subs(t,0)==1 and C.subs(t,1)==1)
check('N leading coefficient norm is -4',norm(1+r)==-4)
check('C leading coefficient norm is 16',norm(6-2*r)==16)
check('kernel denominator degree is 5',sp.degree((1-t)*N*C,t)==5)
check('bounded primitive E degree is 3p-3',sp.expand(2*(p-1)+2*(p-1)/2-3*(p-1))==0)
check('rational b denominator degree is 3p+2',sp.expand(1+2*p+2*(p+1)/2-(3*p+2))==0)
check('degree5 numerator gives a finite infinity value',sp.expand(5+3*(p-1)-(3*p+2))==0)
check('degree4 numerator gives vanishing infinity value',sp.expand(4+3*(p-1)-(3*p+2))==-1)

J=sp.Function('J')(t)
HP=sp.Function('HP')(t)
NN=sp.Function('N')(t)
CC=sp.Function('C')(t)
ell=t*sp.diff(NN,t)/NN+sp.Rational(1,2)*t*sp.diff(CC,t)/CC+t*sp.diff(HP,t)/HP
u=J/HP
expr=sp.diff(u,t)*t+u*ell
expected=(t*sp.diff(J,t)+J*(t*sp.diff(NN,t)/NN+sp.Rational(1,2)*t*sp.diff(CC,t)/CC))/HP
check('Hasse log derivative cancels from primitive equation',sp.simplify(expr-expected)==0)
poly_left=NN*CC*t*sp.diff(J,t)+t*(sp.diff(NN,t)*CC+sp.Rational(1,2)*NN*sp.diff(CC,t))*J
check('complete polynomial certificate has correct coefficients',sp.simplify(NN*CC*HP*expr-poly_left)==0)
rhoE=(p-1)*t*sp.diff(NN,t)/NN+(p-1)/2*t*sp.diff(CC,t)/CC
rhoEA=rhoE+t*sp.diff(NN,t)/NN+sp.Rational(1,2)*t*sp.diff(CC,t)/CC
check('bounded homogeneous numerator E is killed in characteristic p',sp.simplify(rhoEA-p*(t*sp.diff(NN,t)/NN+sp.Rational(1,2)*t*sp.diff(CC,t)/CC))==0)

out={
 'scope':'Fixed polynomial norms, degree identities and the full primitive certificate only. No prime scan or historical producer. Rational Cartier exactness, global pole bounds and off-p cancellation are proved in the Markdown.',
 'checks_passed':len(checks),'checks':checks,
 'fixed_collision_bad_primes':[2,5,29,1049],
 'Hasse_collision_scope':'Hasse/N and Hasse/C intersections are allowed; they only lower poles of b.',
 'primitive':'u=J/P_Hasse, degJ<=3p-3, J(0)=0, theta_t(u*A)=Q*A mod p',
 'coefficient_Frobenius':'Relative C(A^p*b)=sigma_p(A)*C(b), including inert residue fields.',
 'forced_numerator_conditions':'Pc(0)=Pc(1)=0 and degPc<=4',
 'polynomial_certificate':'NC*thetaJ+t*(Nprime*C+N*Cprime/2)*J=(Pc/(1-t))*P_Hasse',
 'second_layer_scope':'Off-p component can be removed by u*Y; a slow-variable coker obstruction remains.',
 'open':'Actual allowed-degree old-column representation, full-prefix slow elimination and original-CDT Smith/height budget.'
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'certificate':str(dest.resolve()),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
