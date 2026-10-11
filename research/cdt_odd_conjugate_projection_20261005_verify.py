"""Exact finite checks for the true level-20 two-embedding period model.

This certificate does not establish a numerical irrationality theorem.
All-scale analytic claims are proved in the companion report.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import json
import sympy as S

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    assert bool(value),name
    checks.append(name)
def chi(n):
    return {0:0,1:1,2:-1,3:-1,4:1}[n%5]
def pair(a=0,b=0):return (Q(a),Q(b))
def add(u,v):return (u[0]+v[0],u[1]+v[1])
def neg(u):return (-u[0],-u[1])
def mul(u,v):return (u[0]*v[0]+5*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def scale(u,c):return (u[0]*c,u[1]*c)
def conj(u):return (u[0],-u[1])
def norm(u):return u[0]**2-5*u[1]**2
def coeff(k,n,which):
    if n==0:return Q(-1,5) if k==2 and which=='E' else (Q(1) if k==4 and which=='E' else Q(0))
    return Q(sum((chi(d) if which=='E' else chi(n//d))*d**(k-1)
                 for d in range(1,n+1) if n%d==0))
def old(k,n,which,j):return coeff(k,n//j,which) if n%j==0 else Q(0)
def v(n,sgn=-1):
    return pair(old(4,n,'E',1)-5*old(4,n,'E',2)+4*old(4,n,'E',4),
                sgn*Q(5,4)*(old(4,n,'F',1)-20*old(4,n,'F',2)+64*old(4,n,'F',4)))
def f(n,sgn=-1):return scale(v(n,sgn),Q(1,n**3)) if n else pair()
def a(n,sgn=-1):return pair(coeff(2,n,'E'),sgn*4*old(2,n,'F',4))
def h_nonconstant_period(n,sgn=-1):
    return sum_pairs(mul(a(j,sgn),f(n-j,sgn)) for j in range(n+1))
def sum_pairs(items):
    z=pair()
    for u in items:z=add(z,u)
    return z
def residual(u,p):
    return tuple((x.numerator%p)*pow(x.denominator%p,-1,p)%p for x in u)
def js(u):return [str(x) for x in u]

r=S.sqrt(5);t=S.symbols('t');pi=S.pi;X=S.symbols('L3_chi')
for k,expected in [(2,S.Rational(-2,5)),(4,S.Integer(2))]:
    B=sum(chi(j)*S.bernoulli(k,S.Rational(j,5)) for j in range(1,6))*5**(k-1)
    check(f'generalized Bernoulli L(1-{k},chi)',S.simplify(-B/k-expected)==0)
check('E2 constant fixed at minus one fifth',coeff(2,0,'E')==Q(-1,5))
check('E4 constant fixed at one',coeff(4,0,'E')==1)

z=S.symbols('z');PE=1-5*z+4*z*z;PF=1-20*z+64*z*z
for n,e in [(0,0),(1,S.Rational(-1,2)),(2,0)]:
    check(f'PE({n})',S.simplify(PE.subs(z,S.Rational(1,2)**n)-e)==0)
for n,e in [(2,0),(3,S.Rational(-1,2))]:
    check(f'PF({n})',S.simplify(PF.subs(z,S.Rational(1,2)**n)-e)==0)
check('reflected oldpolynomial',S.expand(256*z*z*PE.subs(z,1/(16*z))-4*PF)==0)

# Coefficient vectors in E1,E2,E4,F1,F2,F4; omit common tau^4.
M=S.zeros(6)
for i,j,k in [(0,5,256*125*r),(1,4,16*125*r),(2,3,125*r),
              (3,2,256*r),(4,1,16*r),(5,0,r)]:M[j,i]=k
vm=S.Matrix([1,-5,4,-5*r/4,25*r,-80*r])
vp=vm.xreplace({r:-r})
check('weight4 antiFricke level20 full matrix',S.simplify(M*vm+400*vm)==S.zeros(6,1))
check('weight4 plusFricke conjugate full matrix',S.simplify(M*vp-400*vp)==S.zeros(6,1))
check('weight4 double Fricke scalar',M*M==160000*S.eye(6))

# Weight2 columns E(tau),F(4tau), omit common tau^2.
M2=S.Matrix([[0,r],[80*r,0]])
am=S.Matrix([1,-4*r]);ap=S.Matrix([1,4*r])
check('weight2 antiFricke actual multiplier',S.simplify(M2*am+20*am)==S.zeros(2,1))
check('weight2 plusFricke actual conjugate',S.simplify(M2*ap-20*ap)==S.zeros(2,1))
check('weight2 double Fricke scalar',M2*M2==400*S.eye(2))

theta=-5*r*X/16
L1=25*r*X/(8*pi*pi)
L3m=(-5*r/4)*S.Rational(-1,2)*S.Rational(-1,2)*X
L3p=-L3m
check('pure L3 period coefficient',S.simplify(L3m-theta)==0)
check('two periods are opposites',S.simplify(L3p+theta)==0)
check('lower L1 residue relation',S.simplify(L1+10*theta/pi**2)==0)
Pm=L3m+(2*pi*S.I*t)**2*L1/2
Pp=L3p+(2*pi*S.I*t)**2*L1/2
check('full minus period polynomial',S.simplify(Pm-theta*(1+20*t*t))==0)
check('full plus period polynomial without Tate',S.simplify(Pp+theta*(1-20*t*t))==0)

def cusp(k,which,j,c):
    g=gcd(j,c);cn=c//g
    C=Q(-1,5) if k==2 else Q(1)
    factor=Q(g,j)**k
    if which=='E':return pair(factor*chi(j//g)*C if cn%5==0 else 0)
    return pair(0,factor*chi(cn)*C/Q(5**k)) if cn%5 else pair()
def cusp_v(c,sgn):
    e=add(add(cusp(4,'E',1,c),scale(cusp(4,'E',2,c),-5)),scale(cusp(4,'E',4,c),4))
    ff=add(add(cusp(4,'F',1,c),scale(cusp(4,'F',2,c),-20)),scale(cusp(4,'F',4,c),64))
    return add(e,mul(pair(0,sgn*Q(5,4)),ff))
def cusp_a(c,sgn):return add(cusp(2,'E',1,c),mul(pair(0,sgn*4),cusp(2,'F',4,c)))
cs=[1,2,4,5,10,20]
vmc=[Q(0),Q(17,100),Q(-17,20),Q(85,64),Q(-17,4),Q(0)]
vpc=[Q(0),Q(-17,100),Q(17,20),Q(85,64),Q(-17,4),Q(0)]
amc=[Q(1,100),Q(1,25),Q(4,25),Q(-1,5),Q(-1,5),Q(-1,5)]
apc=[Q(-1,100),Q(-1,25),Q(-4,25),Q(-1,5),Q(-1,5),Q(-1,5)]
cusp_table=[]
for c,em,ep,ea,eb in zip(cs,vmc,vpc,amc,apc):
    check(f'full Vminus cusp {c}',cusp_v(c,-1)==pair(em))
    check(f'full Vplus cusp {c}',cusp_v(c,+1)==pair(ep))
    check(f'full Aminus cusp {c}',cusp_a(c,-1)==pair(ea))
    check(f'full Aplus cusp {c}',cusp_a(c,+1)==pair(eb))
    cusp_table.append({'c':c,'width':20//gcd(c*c,20),'Vminus':str(em),'Vplus':str(ep),'Aminus':str(ea),'Aplus':str(eb)})
check('six cusp widths',[x['width'] for x in cusp_table]==[20,5,5,4,1,1])
for c,expected in [(2,Q(17,120)),(4,Q(-17,6)),(5,Q(-17,6)),(10,Q(17,120))]:
    for sgn in [-1,+1]:
        top=scale(mul(cusp_a(c,sgn),cusp_v(c,sgn)),Q((20//gcd(c*c,20))**3,6))
        check(f'true cusp top logarithm c{c} sign{sgn}',top==pair(expected))

for n in range(55):
    check(f'actual two coefficient embeddings n{n}',v(n,+1)==conj(v(n,-1)) and a(n,+1)==conj(a(n,-1)))
check('nonzero target constant multipliers',a(0)==pair(Q(-1,5)) and a(1)==pair(1))
check('packet norm fixed nonzero',norm(pair(1,Q(-5,4)))==Q(-109,16))
packet=[]
for p in [11,13,17,19,23,29,31,37,41,43,47,53]:
    for sgn in [-1,+1]:
        b=scale(h_nonconstant_period(p+1,sgn),p**3)
        expected=pair(1,sgn*Q(5,4)*chi(p))
        check(f'top three-layer shifted packet p{p} sign{sgn}',residual(b,p)==residual(expected,p))
        check(f'packet nonzero at both prime places p{p} sign{sgn}',norm(expected).numerator%p!=0)
    packet.append({'p':p,'chi':chi(p),'expected_minus':js(pair(1,-Q(5,4)*chi(p))),'norm':str(Q(-109,16))})

ell=13;lam=1-ell**3
for n in range(1,41):
    for sgn in [-1,+1]:
        lhs=add(scale(f(ell*n,sgn),ell**3),neg(f(n//ell,sgn) if n%ell==0 else pair()))
        check(f'actual Hecke interchange jet n{n} sign{sgn}',lhs==scale(f(n,-sgn),lam))
for n in range(1,181):
    for sgn in [-1,+1]:
        c=ell-1 if n%ell==0 else -1
        rhs=neg(f(n,sgn))
        if n%ell==0:rhs=add(rhs,scale(f(n//ell,-sgn),Q(lam,ell**2)))
        if n%(ell**2)==0:rhs=add(rhs,scale(f(n//(ell**2),sgn),Q(1,ell**2)))
        check(f'Ramanujan trace actual jet n{n} sign{sgn}',scale(f(n,sgn),c)==rhs)
check('trace13 minus endpoint plus12theta',Q(lam,ell**2)*(-1)+Q(1,ell**2)-1==12)
check('trace13 plus endpoint minus12theta',Q(lam,ell**2)-Q(1,ell**2)+1==-12)

out={'status':'exact_level20_two_embedding_checks_passed','checks':len(checks),
     'scope':'finite exact arithmetic checks; global period proof in companion report; no numerical irrationality theorem',
     'target':'L(3,chi5)','period':'-5*sqrt(5)*L(3,chi5)/16',
     'middle_L2_period':'zero in both primitive Eisenstein components',
     'cusp_table':cusp_table,'top_packets':packet,
     'first_12_Vminus':[js(v(n,-1)) for n in range(12)],
     'first_12_Aminus':[js(a(n,-1)) for n in range(12)],
     'unproved':['complete cyclic rank on the actual quotient','full ordered denominator types','two-embedding admissible covers and strict CDT bound','new numerical irrationality or linear independence']}
(ROOT/'cdt_odd_conjugate_projection_20261005_verify.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks':len(checks),'numeric_irrationality_proved':False},ensure_ascii=False))
