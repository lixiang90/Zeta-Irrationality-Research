"""Exact and interval branch checks for level20 actual period leaves.

Global modular geometry is an explicit input supplied by the root model.
No new numerical irrationality theorem is asserted.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as S
import mpmath as M

BASE=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    assert bool(value),name
    checks.append(name)
chi=lambda n:{0:0,1:1,2:-1,3:-1,4:1}[n%5]
frac=lambda v:v-v.numerator//v.denominator
B3=lambda x:x**3-F(3,2)*x*x+F(1,2)*x
def constants(x,c):
    D=[-F(1,5)*sum(j*chi(n+c*j) for j in range(5)) for n in range(1,c+1)]
    Eg=sum(D[n-1]*(B3(frac(F(x*n,c)))-F(5,8)*B3(frac(F(2*x*n,c)))+
                  F(1,16)*B3(frac(F(4*x*n,c)))) for n in range(1,c+1))
    def fg(b):return F(1,2)*sum((-1)**(k+1)*chi(u)*B3(frac(F(b*k,c)+F(u,5)))
                              for k in range(1,c) for u in range(1,5))
    Fg=fg(x)-F(1,2)*fg(2*x)
    return D,Eg,Fg,F(2,3)*Eg-F(5,6)*Fg,F(2,3)*Eg+F(5,6)*Fg

t,z,v=S.symbols('t z v');r=S.sqrt(5)
Delta=1-12*t+28*t*t-32*t**3+16*t**4
alpha=S.Rational(1,2)-S.sqrt((r-1)/8)
beta=S.Rational(1,2)+S.sqrt((r-1)/8)
gm=S.Rational(1,2)-S.I*S.sqrt((r+1)/8)
gp=S.conjugate(gm)
check('centered exact quartic',S.expand(Delta.subs(t,v+S.Rational(1,2)))==16*v**4+4*v*v-1)
check('four roots are simple',S.gcd(Delta,S.diff(Delta,t))==1)
for name,b in [('alpha',alpha),('beta',beta),('gamma_minus',gm),('gamma_plus',gp)]:
    check(f'exact Delta root {name}',S.simplify(Delta.subs(t,b))==0)

G=z*(1-z*z)/(1+z+z*z+z**3+z**4)
K=z/(1-z)-S.Rational(5,2)*z*z/(1-z*z)+z**4/(1-z**4)
check('actual F20 integrated kernel',S.cancel(K-z/(1+z)+S.Rational(1,2)*z*z/(1+z*z))==0)
check('actual G reciprocal antisymmetry',S.cancel(G+G.subs(z,1/z))==0)
check('F20 reciprocal constant one half',S.cancel(K+K.subs(z,1/z)-S.Rational(1,2))==0)

rows=[('alpha',1,0,1,0,1,F(0),F(0),F(0),F(0)),
      ('gamma_minus',3,1,7,-1,3,F(-1,8),F(-4,25),F(1,20),F(-13,60)),
      ('gamma_plus',3,2,27,-2,3,F(1,8),F(4,25),F(-1,20),F(13,60)),
      ('beta',9,2,9,-2,9,F(-43,216),F(19,135),F(-1,4),F(-5,324))]
periods=[]
for name,a,b,d,x,c,ee,ff,cm,cp in rows:
    gamma=S.Matrix([[a,b],[20*b,d]])
    sigma=S.Matrix([[-20*b,-d],[20*a,20*b]])
    check(f'exact Gamma0 matrix {name}',gamma.det()==1)
    check(f'exact elliptic square {name}',sigma*sigma==-20*S.eye(2))
    h=S.Rational(-b,a);N=20*a*a
    act=S.cancel((sigma[0,0]*(h+z)+sigma[0,1])/(sigma[1,0]*(h+z)+sigma[1,1]))
    check(f'actual shifted involution {name}',S.cancel(act-h+1/(N*z))==0)
    D,e,f,minus,plus=constants(x,c)
    check(f'finite E20 sum {name}',e==ee)
    check(f'finite F20 sum {name}',f==ff)
    check(f'full minus cusp period {name}',minus==cm)
    check(f'full plus cusp period {name}',plus==cp)
    if name!='alpha':
        check(f'necessary minus regularity fails {name}',minus!=0)
        check(f'necessary plus regularity fails {name}',plus!=0)
    for n in range(1,c):check(f'finite D antisymmetry {name} n{n}',D[c-n-1]==-D[n-1])
    check(f'finite D zero at origin {name}',sum(D)==0 and D[-1]==0)
    cyclo=S.Poly(S.cyclotomic_poly(c,z),z,domain=S.QQ)
    for m in range(c):
        zz=z**m
        # Verify the actual Abel Fourier kernel in its cyclotomic field.
        num=S.Poly(zz*(1-zz*zz),z,domain=S.QQ).rem(cyclo)
        den=S.Poly(1+zz+zz**2+zz**3+zz**4,z,domain=S.QQ).rem(cyclo)
        lhs=(num*S.invert(den,cyclo)).rem(cyclo)
        rhs=S.Poly(sum(S.Rational(w.numerator,w.denominator)*z**(m*n) for n,w in enumerate(D,1)),z,domain=S.QQ).rem(cyclo)
        check(f'actual Abel kernel Fourier identity {name} m{m}',lhs==rhs)
    periods.append({'branch':name,'a':a,'b':b,'d':d,'character':chi(d),'effective_level':N,
                    'E20':str(e),'F20':str(f),'minus_pi3':str(minus),'plus_pi3':str(plus)})

# Directed interval eta products, with a separate exact bound for the infinite tail.
M.iv.dps=50
rho=F(9,10);cutoff=600
tail=8*rho**(cutoff+1)/((1-rho)*(1-rho**(cutoff+1)))
check('eta log-tail small',tail<F(1,2))
check('exact final t tail bound',40*tail<F(1,10**18))
eps=M.iv.mpf('0.000000000000000001')
boxes={'alpha':('0.106','0.108','-0.001','0.001'),
       'beta':('0.892','0.894','-0.001','0.001'),
       'gamma_minus':('0.499','0.501','-0.637','-0.635'),
       'gamma_plus':('0.499','0.501','0.635','0.637')}
isolation=[]
for name,a,b,d,*unused in rows:
    tau=M.iv.mpc(-M.iv.mpf(b)/a,1/(a*M.iv.sqrt(20)))
    q=M.iv.exp(2*M.iv.pi*1j*tau)
    check(f'eta q bound {name}',abs(q)<M.iv.mpf(9)/10)
    hn=1/q
    for n in range(1,cutoff+1):
        hn*=((1-q**(4*n))*(1-q**(5*n))/((1-q**n)*(1-q**(20*n))))**2
    check(f'finite eta H bound {name}',abs(hn)<10)
    check(f'finite eta inverse denominator {name}',abs(hn+1)>1)
    tn=1/(hn+1)
    lo,hi,ilo,ihi=map(M.iv.mpf,boxes[name])
    check(f'rigorous actual real root isolation {name}',tn.real-eps>lo and tn.real+eps<hi)
    check(f'rigorous actual imag root isolation {name}',tn.imag-eps>ilo and tn.imag+eps<ihi)
    isolation.append({'branch':name,'finite_eta_real':str(tn.real),'finite_eta_imag':str(tn.imag),'explicit_t_error_bound':'<1e-18'})

R=S.Rational(103,40);a0=S.Rational(80,103)
phi=4209*z/(4120+3200*z)
check('exact Mobius circle map',S.cancel(phi-(-2+R*(z+a0)/(1+a0*z)))==0)
check('Mobius maps zero to zero',phi.subs(z,0)==0)
check('positive exact derivative',S.diff(phi,z).subs(z,0)==S.Rational(4209,4120)>1)
check('Mobius pole outside closed disc',S.Rational(4120,3200)>1)
check('origin in image circle',R>2)
check('alpha circle comparison bound',S.Rational(9,4)<R) # alpha<1/4
check('beta circle comparison bound',S.Rational(11,4)>R) # beta>3/4
check('cusp1 outside image',3>R)
check('sqrt5 lower rational bound',S.Rational(11,5)**2<5)
check('complex branches outside image',(S.Rational(51)+S.Rational(11,5))/8>R*R)
check('alpha between zero and one quarter',2**2<5<3**2 and (S.Rational(1,4))**2<(S.Rational(2)-1)/8)
check('sqrt5 upper rational bound',5<S.Rational(9,4)**2)
check('complex omission derivative strict less13',256*(3+S.Rational(9,4))/8<13**2)
def exp_lower(q,n):
    out=F(1);term=F(1)
    for k in range(1,n+1):term*=q/k;out+=term
    return out
check('log13 less thirteen fifths',exp_lower(F(13,5),12)>13)
check('log16 below rank4 natural flat',exp_lower(F(45,16),12)>16)

# The three finite elliptic points and infinity yield a new genus-one cover.
aa2=(r-1)/8;cc2=(r+1)/8
disc=-4*cc2*(aa2+cc2)**2
j=S.simplify(256*(aa2-3*cc2)**3/disc)
expected=S.Rational(32,5)*(47+21*r)
check('new three-elliptic curve discriminant nonzero',S.simplify(disc)!=0)
check('new three-elliptic curve exact j',S.simplify(j-expected)==0)
check('new curve exact norm j',S.simplify(j*j.xreplace({r:-r}))==S.Rational(4096,25))

TT=S.Matrix([[1,1],[0,1]]);WW=S.Matrix([[0,-1],[20,0]])
check('actual Hecke scaled translation',S.simplify(S.sqrt(20)*(z/S.sqrt(20)+1)-z-S.sqrt(20))==0)
check('actual Hecke scaled inversion',S.simplify(S.sqrt(20)*(-1/(20*(z/S.sqrt(20))))+1/z)==0)
check('Hecke parameter above two',20>4)
check('Hecke lower parabolic',WW*TT.inv()*WW.inv()==S.Matrix([[1,0],[20,1]]))
check('Hecke conjugate principal elliptic',TT*WW*TT.inv()*WW.inv()==S.Matrix([[21,1],[20,1]]))
de,ee,ff,cm,cp=constants(-1,21)
check('additional principal elliptic E period zero',ee==0)
check('additional principal elliptic F period zero',ff==0)
check('additional principal elliptic both true regular periods',cm==0 and cp==0)
check('full common cover strict size lower bound',F(4209,4120)>1)

out={'status':'exact_level20_leaf_checks_passed','checks':len(checks),
     'periods':periods,'branch_identity_intervals':isolation,
     'eta_cutoff':cutoff,'eta_log_tail_bound':str(tail),'explicit_t_error_bound':'<1e-18',
     'legal_common_map':'4209*z/(4120+3200*z)','legal_common_map_derivative':'4209/4120',
     'full_common_surface':'cusp-filled coarse Hecke quotient parameter sqrt(20)',
     'full_common_cover_size_proved':'4209/4120 <= rho <=16; global analytic proof in report',
     'conditional_derivative_bounds':{'omit_gamma_unique_zero':'<13','omit_cusp1_unique_zero':'<=16'},
     'new_three_elliptic_j':'32*(47+21*sqrt(5))/5',
     'scope':'canonical four lifts; finite local monodromy proof in report; full root modular geometry is explicit input',
     'not_proved':['regularity classification over every globally continued leaf','exact Hecke conformal size or boundary capacity','optimal common cover','strict CDT capacity bound','new numerical irrationality theorem']}
(BASE/'cdt_odd_level20_leaf_20261006_verify.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':len(checks),'numeric_irrationality_proved':False}))
