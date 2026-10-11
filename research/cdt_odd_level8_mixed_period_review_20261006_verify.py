"""New fixed exact review of the D8 Lambert endpoint and M-cocycle.
No old producer is imported or executed; no numerical unknown L-value is used.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as s

checks=[]
def check(name,v):
    if not v: raise AssertionError(name)
    checks.append(name)
def chi8(n):
    n%=8
    return 1 if n in (1,7) else -1 if n in (3,5) else 0
def chi3(n):
    n%=3
    return 1 if n==1 else -1 if n==2 else 0
def B2(x): return x*x-x+F(1,6)
def B3(x): return x*x*x-F(3,2)*x*x+F(1,2)*x
def B4(x): return x**4-2*x**3+x*x-F(1,30)
def Bchi(D,chi,k,B):
    return D**(k-1)*sum((chi(a)*B(F(a,D)) for a in range(1,D+1)),F(0))
check('B2 chi8',Bchi(8,chi8,2,B2)==2)
check('B4 chi8',Bchi(8,chi8,4,B4)==-44)
check('B3 chi-3',Bchi(3,chi3,3,B3)==F(2,3))
check('B3 chi-24',Bchi(24,lambda n:chi8(n)*chi3(n),3,B3)==138)
check('odd chi-24 units',[chi8(a)*chi3(a) for a in [1,5,7,11,13,17,19,23]]==[1,1,1,1,-1,-1,-1,-1])

tau=s.symbols('tau')
gamma=s.Matrix([[3,1],[8,3]])
W=s.Matrix([[0,-1],[8,0]])
M=gamma*W
check('gamma determinant one',gamma.det()==1)
check('gamma character minus',chi8(3)==-1)
check('actual M matrix',M==s.Matrix([[8,-3],[24,-8]]))
check('M square central',M*M==-8*s.eye(2))
mt=(8*tau-3)/(24*tau-8)
z=s.symbols('z')
check('translated Fricke map',s.simplify(mt.subs(tau,F(1,3)+z)-(F(1,3)-1/(72*z)))==0)
JM=(24*tau-8)**2/8
qM=1+8*(3*tau-1)**2
check('period generator fixed',s.cancel(JM*qM.subs(tau,mt)-qM)==0)
monomials=[s.Integer(1),tau,tau**2]
matrix=s.Matrix([[s.Poly(s.cancel(JM*x.subs(tau,mt)),tau).nth(i) for x in monomials] for i in range(3)])
check('Sym2 plus eigenspace dimension one',len((matrix-s.eye(3)).nullspace())==1)
check('generator normalized at endpoint',qM.subs(tau,F(1,3))==1)

rho=(-1+s.sqrt(3)*s.I)/2
x=s.symbols('x')
e=x*(1-x*x)/(1+x**4)
check('e chi endpoint 1',s.simplify(e.subs(x,1))==0)
check('e chi endpoint rho',s.simplify(e.subs(x,rho)-s.I*s.sqrt(3))==0)
check('e chi endpoint inverse rho',s.simplify(e.subs(x,rho**2)+s.I*s.sqrt(3))==0)
L3m3=2*s.Rational(2,3)/(3*3**2*s.sqrt(3))
L3m24=2*s.Integer(138)/(3*24**2*s.sqrt(24))
L4p8=s.Integer(44)/(3*8**3*s.sqrt(8))
check('critical L3 chi-3 over pi3',s.simplify(L3m3-4/(81*s.sqrt(3)))==0)
check('critical L3 chi-24 over pi3',s.simplify(L3m24-23/(288*s.sqrt(6)))==0)
check('critical L4 chi8 over pi4',s.simplify(L4p8-11/(768*s.sqrt(2)))==0)

# Unknown Zeta3 and noncritical L3chi8 remain separate actual-symbol inputs.
Z,L,P3=s.symbols('Zeta3 L3chi8 Pi3',real=True)
triv=1320*(-s.Rational(7,16)*Z+s.I*P3/108)
Eendpoint=63*s.I*s.sqrt(3)*L3m3*P3
Fendpoint=1008*s.sqrt(2)*(-L/2+s.I*L3m24*P3/(2*s.sqrt(3)))
check('trivial finite real coefficient',s.expand(triv).coeff(Z)==-s.Rational(1155,2))
check('trivial finite imaginary coefficient',s.simplify(triv.subs(Z,0)/(s.I*P3))==s.Rational(110,9))
check('E chi finite imaginary coefficient',s.simplify(Eendpoint/(s.I*P3))==s.Rational(28,9))
check('F chi finite real coefficient',s.expand(Fendpoint).coeff(L)==-504*s.sqrt(2))
check('F chi finite imaginary coefficient',s.simplify(Fendpoint.subs(L,0)/(s.I*P3))==s.Rational(161,12))
check('whole true endpoint',s.simplify(triv+Eendpoint+Fendpoint-(-s.Rational(1155,2)*Z-504*s.sqrt(2)*L+s.Rational(115,4)*s.I*P3))==0)
resU=1320*s.Rational(63,64)*s.Rational(1,90)/81
resF=-63*16*s.sqrt(2)*L4p8/81
check('whole radial pole residue cancels',s.simplify(resU+resF)==0)

psi=s.symbols('psi',real=True)
lam=psi+s.Rational(115,4)*s.I*P3
lamp=psi-s.Rational(115,4)*s.I*P3
qMp=1+8*(3*tau+1)**2
avg=s.expand((lam*qM+lamp*qMp)/2)
check('endpoint average is psi',(lam+lamp)/2==psi)
check('complete trace retains linear Tate term',s.expand(avg-(9*psi*(1+8*tau*tau)-1380*s.I*P3*tau))==0)
check('period not T periodic',s.expand(qM.subs(tau,tau+1)-qM)==144*tau+24)

data={'checks_passed':len(checks),'checks':checks,
      'scope':'One fixed exact Bernoulli/endpoint/trace/matrix check; analytic limits and Bol proof remain in the review MD.',
      'endpoint_coefficients':{'Zeta3':'-1155/2','sqrt2_L3chi8':'-504','i_pi3':'115/4'},
      'endpoint_parts_i_pi3':['110/9','28/9','161/12'],
      'M':[[8,-3],[24,-8]],'Sym2_matrix':str(matrix),'period_generator':str(s.expand(qM))}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(checks),'endpoint_coefficients':data['endpoint_coefficients']},ensure_ascii=False))
