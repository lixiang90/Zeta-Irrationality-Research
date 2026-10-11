"""New fixed D12 canonical rho_7^2 exact certificate; no parameter scan."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

checks=[]
def chk(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value:
        raise AssertionError(name)

def B3(x):
    return x*x*x-Q(3,2)*x*x+Q(1,2)*x

def frac(x):
    return x-(x.numerator//x.denominator)

def chi12(a):
    return int(sp.kronecker_symbol(12,a))

# Im finite Lambert / pi^3, via the exact discrete cot Fourier identity.
def tim(h):
    hi=pow(h,-1,7)
    return sum(Q(7-2*((m*hi)%7))*B3(Q(m,7)) for m in range(1,7))/21

T={h:tim(h) for h in range(1,7)}
A=240*(T[2]-T[3]/12)
B=30*T[4]-10*T[5]
C=Q(80,9)*T[6]-Q(20,3)*T[1]
weights={m:7-2*((4*m)%7) for m in range(1,7)}
inner={m:sum(chi12(a)*B3(frac(Q(a,12)+Q(m,7))) for a in range(1,13)) for m in range(1,7)}
KF=Q(12,21)*sum(weights[m]*inner[m] for m in range(1,7))
x=sp.symbols('x')
cyc=sp.cyclotomic_poly(7,x)
H=sum(chi12(a)*x**(2*a) for a in range(1,13))
E=sp.rem(H*sp.invert(1-x**24,cyc),cyc,x)
E=sp.expand(E-E.subs(x,1)*cyc/7)
Ecoef=[Q(E.coeff(x,m)) for m in range(7)]
KE=Q(2,3)*sum(Ecoef[m]*B3(Q(m,7)) for m in range(7))
J=KE+KF
Ia=A-99*C+Q(66,23)*J
Ib=B-9*C+J/23

for h in range(1,4):
    chk('Lambert h and minus h '+str(h),T[7-h] == -T[h])
for m in range(1,4):
    chk('chi inner odd '+str(m),inner[7-m] == -inner[m])
chk('E kernel exact polynomial',E == x-x**3+x**4-x**6)
chk('E kernel constant at one',E.subs(x,1)==0)
chk('E kernel denominator identity',sp.rem((1-x**24)*E-H,x**7-1,x)==0)
for m in range(1,7):
    chk('E kernel odd '+str(m),Ecoef[7-m] == -Ecoef[m])
chk('E imaginary coefficient',KE == Q(12,343))
chk('T1 exact',T[1] == Q(12,343))
chk('T2 exact',T[2] == Q(4,343))
chk('T3 exact',T[3] == 0)
chk('G1 imaginary',A == Q(960,343))
chk('G2 imaginary',B == Q(40,343))
chk('G3 imaginary',C == Q(-80,147))
chk('kappa F imaginary',KF == Q(550,1029))
chk('character plus imaginary',J == Q(586,1029))
chk('zeta free a coefficient',Ia == Q(28164,483))
chk('zeta free b coefficient',Ib == Q(2434,483))
for m,value in [(1,Q(311,2352)),(2,Q(383,2352)),(3,Q(1,14))]:
    chk('Bernoulli inner '+str(m),inner[m]==value)

tau=sp.symbols('tau')
W=sp.Matrix([[0,-1],[12,0]])
gamma=sp.Matrix([[7,2],[24,7]])
M=gamma*W
chk('gamma determinant',gamma.det()==1)
chk('gamma char minus',chi12(7)==-1)
chk('M exact',M==sp.Matrix([[24,-7],[84,-24]]))
chk('M determinant',M.det()==12)
chk('M trace zero',sp.trace(M)==0)
chk('M square',M*M==-12*sp.eye(2))
qm=1+12*(7*tau-2)**2
Mt=(24*tau-7)/(84*tau-24)
R=(84*tau-24)**2/12
chk('M period polynomial invariant',sp.cancel(R*qm.subs(tau,Mt)-qm)==0)
chk('M endpoint quadratic one',qm.subs(tau,sp.Rational(2,7))==1)
fp=sp.Rational(2,7)+sp.I*sp.sqrt(3)/42
chk('M canonical fixed point',sp.simplify(Mt.subs(tau,fp)-fp)==0)
for j,l,factor in [(1,12,144),(2,6,9),(3,4,sp.Rational(16,9))]:
    chk('old Fricke forward '+str(j),sp.Rational(12**2,j**4)==factor)
    chk('old Fricke backward '+str(l),sp.Rational(12**2,l**4)*factor==1)

aa,bb,cc,dd=sp.symbols('a b c d')
const=143*aa+8*bb+sp.Rational(7,9)*cc-23*dd
zet=-110*aa-10*bb-sp.Rational(10,9)*cc
chk('zeta free c constraint',zet.subs(cc,-99*aa-9*bb)==0)
chk('zeta free d constraint',sp.expand(const.subs({cc:-99*aa-9*bb,dd:(66*aa+bb)/23}))==0)
im=sp.Rational(A)*aa+sp.Rational(B)*bb+sp.Rational(C)*cc+sp.Rational(J)*dd
chk('Tate reduced exact form',sp.expand(im.subs({cc:-99*aa-9*bb,dd:(66*aa+bb)/23})-(28164*aa+2434*bb)/483)==0)
av,bv,cv,dv=1217,-14082,6255,2880
chosen={aa:av,bb:bv,cc:cv,dd:dv}
chk('chosen infinity constant zero',const.subs(chosen)==0)
chk('chosen zeta3 free',zet.subs(chosen)==0)
chk('chosen Tate free',im.subs(chosen)==0)
chk('chosen character nonzero',dv!=0)
chk('chosen period factor',12*dv==34560)
chk('constraints rank three',sp.Matrix([[143,8,sp.Rational(7,9),-23],[-110,-10,-sp.Rational(10,9),0],[sp.Rational(A),sp.Rational(B),sp.Rational(C),sp.Rational(J)]]).rank()==3)
triv={1:av,2:bv,3:cv,4:-sp.Rational(16,9)*cv,6:-9*bv,12:-144*av}
chk('expanded coefficients exact',triv=={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248})
chk('expanded coefficients integers',all(v==int(v) for v in triv.values()))
chk('expanded constant plus character',sum(triv.values())+23*dv==0)
chk('expanded L3 zero',sum(sp.Rational(v,j**3) for j,v in triv.items())==0)
chk('expanded L1 zero',sum(sp.Rational(v,j) for j,v in triv.items())==0)
chk('canonical radial pole cancels',240*sum(sp.Rational(v,j**4) for j,v in triv.items())-sp.Rational(115,3)*dv==0)

def generalizedB(n):
    return sp.expand(12**(n-1)*sum(chi12(a)*sp.bernoulli(n,sp.Rational(a,12)) for a in range(1,13)))
chk('B2 chi12',generalizedB(2)==4)
chk('B4 chi12',generalizedB(4)==-184)
chk('E4 constant23',-generalizedB(4)/8==23)
kappa=24*sp.sqrt(3)
L2=sp.sqrt(12)/2*(2*sp.pi/12)**2*generalizedB(2)/sp.factorial(2)
L4=-sp.sqrt(12)/2*(2*sp.pi/12)**4*generalizedB(4)/sp.factorial(4)
chk('critical kappa L2',sp.simplify(kappa*L2-4*sp.pi**2)==0)
chk('critical kappa L4',sp.simplify(kappa*L4-sp.Rational(115,3)*sp.pi**4/90)==0)
chk('sigma L2 coefficient',-sp.Rational(2,3)*dv==-1920)
chk('sigma W constant',46*dv==132480)
chk('sigma reciprocal coefficient',Q(23*dv,54)==Q(3680,3))
chk('sigma linear Tate coefficient',Q(4*dv,3)==3840)

results={'T_im':{str(h):str(v) for h,v in T.items()},'inner_B3':{str(m):str(v) for m,v in inner.items()},
 'triv_im':[str(A),str(B),str(C)],'E_im':str(KE),'kappa_F_im':str(KF),'char_plus_im':str(J),
 'zeta_free_im':[str(Ia),str(Ib)],'chosen':[av,bv,cv,dv],
 'expanded_triv':{str(j):int(v) for j,v in triv.items()},'pure_period_factor':34560}
data={'check_count':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,'results':results,
      'scope':['one canonical rho7 squared','finite exact Bernoulli/Fourier algebra','no prime or parameter scan',
               'no old producer execution','no new irrationality theorem','no algebraic coordinate, actual rank or budget computed']}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':data['all_passed'],'results':results},ensure_ascii=False))
