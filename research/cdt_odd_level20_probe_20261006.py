"""Exploratory exact jets for the level-20 Fricke model; no numeric theorem."""
from fractions import Fraction as F
from math import comb, gcd
import sympy as sp
import sys
sys.stdout.reconfigure(encoding='utf-8')
N=48
def pad(a):return list(a[:N])+[F(0)]*max(0,N-len(a))
def add(a,b):return [a[i]+b[i] for i in range(N)]
def scale(a,c):return [v*c for v in a]
def mul(a,b):
 out=[F(0)]*N
 for i,v in enumerate(a):
  if v:
   for j in range(N-i):
    if b[j]:out[i+j]+=v*b[j]
 return out
def inv(a):
 out=pad([]);out[0]=1/a[0]
 for n in range(1,N):out[n]=-sum(a[k]*out[n-k] for k in range(1,n+1))/a[0]
 return out
def pw(a,k):
 if k<0:return pw(inv(a),-k)
 out=pad([F(1)])
 for _ in range(k):out=mul(out,a)
 return out
def shift(a,k):return pad([F(0)]*k+a) if k>=0 else pad(a[-k:])
def derivative(a):return pad([(i+1)*a[i+1] for i in range(N-1)])
def theta(a):return [i*v for i,v in enumerate(a)]
def compose(a,b):
 assert b[0]==0
 out=pad([]);p=pad([F(1)])
 for v in a:out=add(out,scale(p,v));p=mul(p,b)
 return out
def revert(a):
 assert a[0]==0 and a[1]==1
 p=pad([F(1)]);iu=inv(pad(a[1:]));out=pad([])
 for n in range(1,N):p=mul(p,iu);out[n]=p[n-1]/n
 return out
def eta(ds,rs):
 out=pad([F(1)])
 for d,r in zip(ds,rs):
  for m in range(d,N,d):
   fac=pad([])
   for j in range((N-1)//m+1):
    bc=comb(r,j) if r>=0 and j<=r else (0 if r>=0 else (-1)**j*comb(-r+j-1,j))
    fac[j*m]=F((-1)**j*bc)
   out=mul(out,fac)
 return out
def polynomial_at_h(unit,degree,H):
 rem=list(unit);cs=[F(0)]*(degree+1)
 for j in range(degree,-1,-1):
  k=degree-j;cs[j]=rem[k]
  rem=add(rem,scale(shift(pw(H,j),k),-cs[j]))
 assert all(v==0 for v in rem[:N-degree-3]),(cs,rem)
 return cs
def pol(a,v):return sum(sp.Rational(x.numerator,x.denominator)*v**i for i,x in enumerate(a))
def chi(n):return (0,1,-1,-1,1)[n%5]
ds=[1,2,4,5,10,20]
H=eta(ds,[-2,0,2,2,0,-2])
U=eta(ds,[-3,4,-1,-1,4,-3])
assert U==add(H,pad([F(0),F(1)]))
BB=eta(ds,[0,2,0,0,2,0]);B=shift(BB,1)
numy=mul(add(theta(H),scale(H,-1)),inv(BB))
P=pol(polynomial_at_h(mul(numy,numy),4,H),sp.Symbol('h'))
print('P4(h)=',sp.factor(P))
tq=mul(pad([F(0),F(1)]),inv(add(H,pad([F(0),F(1)]))))
qt=revert(tq)
assert all(v.denominator==1 for v in qt)
t=sp.Symbol('t');h=sp.Symbol('h')
Delta=sp.expand(t**4*P.subs(h,1/t-1))
print('Delta(t)=',sp.factor(Delta))
print('tq',tq[:10]);print('qt',qt[:10])
AE=pad([F(-1,5)]+[F(sum(chi(d)*d for d in range(1,n+1) if n%d==0)) for n in range(1,N)])
AF=pad([F(0)]+[F(-4*sum(chi((n//4)//d)*d for d in range(1,n//4+1) if (n//4)%d==0)) if n%4==0 else F(0) for n in range(1,N)])
T0=mul(AE,inv(BB));T1=mul(AF,inv(BB))
sq0=add(mul(T0,T0),scale(mul(T1,T1),5));sq1=scale(mul(T0,T1),2)
fac=mul(pw(H,2),pw(add(H,pad([F(0),F(1)])),2))
P0=pol(polynomial_at_h(mul(sq0,fac),6,H),h)
P1=pol(polynomial_at_h(mul(sq1,fac),6,H),h)
R2h=sp.factor((P0+sp.sqrt(5)*P1)/(h**2*(h+1)**2),extension=sp.sqrt(5))
print('(A-/B)^2=',R2h)
print('P0=',sp.factor(P0));print('P1=',sp.factor(P1))
R2t=sp.factor((t**2/Delta*R2h).subs(h,1/t-1),extension=sp.sqrt(5))
print('(A-/S)^2=',R2t)
print('Delta roots:',sp.nroots(Delta))
# Base projective connection, with global pole bound t(1-t)^2 Delta^2.
Tunit=pad(tq[1:]);Sq=add(pad([F(1)]),mul(theta(Tunit),inv(Tunit)))
St=compose(Sq,qt);ss=mul(derivative(St),inv(St))
tQ=add(add(scale(shift(derivative(ss),1),F(-1,2)),scale(shift(mul(ss,ss),1),F(-1,4))),scale(ss,F(-1,2)))
Dc=pad([F(int(sp.Poly(Delta,t).nth(i))) for i in range(5)])
om=pad([F(1),F(-1)])
Qnum=mul(tQ,mul(pw(om,2),pw(Dc,2)))
assert all(v==0 for v in Qnum[9:N-5]),Qnum
Q=sp.cancel(pol(Qnum[:9],t)/(t*(1-t)**2*Delta**2))
print('Q(t)=',sp.factor(Q))
# Complete rational inhomogeneous forcing: U=A V/(theta t)^3.
ek=[F(0)]+[F(sum(chi(d)*d**3 for d in range(1,n+1) if n%d==0)) for n in range(1,N)]
fk=[F(0)]+[F(sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d==0)) for n in range(1,N)]
VE=pad([F(0)]+[ek[n]-(5*ek[n//2] if n%2==0 else 0)+(4*ek[n//4] if n%4==0 else 0) for n in range(1,N)])
VF=pad([F(0)]+[F(-5,4)*(fk[n]-(20*fk[n//2] if n%2==0 else 0)+(64*fk[n//4] if n%4==0 else 0)) for n in range(1,N)])
AV0=add(mul(AE,VE),scale(mul(AF,VF),5));AV1=add(mul(AE,VF),mul(AF,VE))
dunit=pad(theta(tq)[1:]);fac=mul(pw(Tunit,2),pw(dunit,-3))
U0=compose(mul(pad(AV0[1:]),fac),qt)
U1=compose(mul(pad(AV1[1:]),fac),qt)
Ud=mul(pw(om,3),Dc)
Un0=mul(U0,Ud);Un1=mul(U1,Ud)
assert all(v==0 for v in Un0[7:N-5]),Un0
assert all(v==0 for v in Un1[7:N-5]),Un1
Un=pol(Un0[:7],t)+sp.sqrt(5)*pol(Un1[:7],t)
forcing=sp.cancel(Un/(t**2*(1-t)**3*Delta))
print('U numerator=',sp.factor(Un,extension=sp.sqrt(5)))
print('U=',sp.factor(forcing,extension=sp.sqrt(5)))
cp=1-(6+2*sp.sqrt(5))*t+(6+2*sp.sqrt(5))*t**2
cm=cp.xreplace({sp.sqrt(5):-sp.sqrt(5)})
Nm=1-(6+sp.sqrt(5))*t+(1+sp.sqrt(5))*t**2
Rp2=Nm**2/(25*(1-t)**2*cp)
assert sp.simplify(R2t-Rp2)==0
assert sp.expand(cp*cm-Delta)==0
rho=sp.cancel(sp.diff(Nm,t)/Nm+1/(1-t)-sp.diff(cp,t)/(2*cp))
Pbase=1/t
a2=sp.cancel(3*Pbase-3*rho)
a1=sp.cancel(3*(rho**2-sp.diff(rho,t))-6*Pbase*rho+sp.diff(Pbase,t)+4*Q+2*Pbase**2)
a0=sp.cancel(-rho**3+3*rho*sp.diff(rho,t)-sp.diff(rho,t,2)+3*Pbase*(rho**2-sp.diff(rho,t))-(sp.diff(Pbase,t)+4*Q+2*Pbase**2)*rho+2*sp.diff(Q,t)+4*Pbase*Q)
print('L3 gauge constructed; coefficient numerator degrees',[(sp.degree(sp.numer(a),t),sp.degree(sp.denom(a),t)) for a in (a0,a1,a2)])
