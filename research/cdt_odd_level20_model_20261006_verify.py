"""Exact level-20 model checks; finite jets supplement stated global pole proofs."""
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path
import hashlib, json, sys
import sympy as sp
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
N=48
checks=[]
def check(label,condition):
 assert condition,label
 checks.append(label)
def pad(a):return list(a[:N])+[F(0)]*max(0,N-len(a))
def add(a,b):return [a[i]+b[i] for i in range(N)]
def scale(a,c):return [v*c for v in a]
def mul(a,b):
 out=pad([])
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
 check('bounded_h_polynomial_degree_'+str(degree),all(v==0 for v in rem[:N-degree-3]))
 return cs
def pol(a,v):return sum(sp.Rational(x.numerator,x.denominator)*v**i for i,x in enumerate(a))
def chi(n):return (0,1,-1,-1,1)[n%5]
ds=[1,2,4,5,10,20]
orders=sp.Matrix([[sp.Rational(20*gcd(c,d)**2,24*gcd(c,20//c)*c*d) for d in ds] for c in ds])
rs=[[-2,0,2,2,0,-2],[-3,4,-1,-1,4,-3],[0,2,0,0,2,0]]
expected=[[-1,0,1,1,0,-1],[-1,1,0,0,1,-1],[1]*6]
for i,(rr,ee) in enumerate(zip(rs,expected)):
 check('eta_cusp_divisor_'+str(i),orders*sp.Matrix(rr)==sp.Matrix(ee))
 check('eta_modularity_'+str(i),sum(d*r for d,r in zip(ds,rr))%24==0 and sum((20//d)*r for d,r in zip(ds,rr))%24==0)
 check('eta_square_character_'+str(i),sp.sqrt(sp.prod(sp.Rational(d)**r for d,r in zip(ds,rr))).is_Rational)
 check('eta_fricke_symmetry_'+str(i),list(reversed(rr))==rr)
check('curve_genus_one',1+sp.Rational(36,12)-sp.Rational(6,2)==1)
H=eta(ds,rs[0]);UU=eta(ds,rs[1]);BB=eta(ds,rs[2])
check('u_equals_h_plus_one_jets',UU==add(H,pad([F(0),F(1)])))
numy=mul(add(theta(H),scale(H,-1)),inv(BB))
h=sp.Symbol('h');t=sp.Symbol('t');r=sp.sqrt(5)
quartic=pol(polynomial_at_h(mul(numy,numy),4,H),h)
check('double_cover_quartic',quartic==h**4-8*h**3-2*h**2-8*h+1)
Delta=sp.expand(t**4*quartic.subs(h,1/t-1))
check('four_simple_branch_values',sp.discriminant(Delta,t)!=0)
cp=1-(6+2*r)*t+(6+2*r)*t**2;cm=cp.xreplace({r:-r})
check('quadratic_branch_factorization',sp.expand(cp*cm-Delta)==0)
tq=mul(pad([F(0),F(1)]),inv(add(H,pad([F(0),F(1)]))))
qt=revert(tq)
check('integer_forward_coordinate',all(v.denominator==1 for v in tq))
check('integer_inverse_coordinate',all(v.denominator==1 for v in qt))
check('coordinate_exact_composition',compose(tq,qt)==pad([F(0),F(1)]))
AE=pad([F(-1,5)]+[F(sum(chi(d)*d for d in range(1,n+1) if n%d==0)) for n in range(1,N)])
AF=pad([F(0)]+[F(-4*sum(chi((n//4)//d)*d for d in range(1,n//4+1) if (n//4)%d==0)) if n%4==0 else F(0) for n in range(1,N)])
T0=mul(AE,inv(BB));T1=mul(AF,inv(BB))
sq0=add(mul(T0,T0),scale(mul(T1,T1),5));sq1=scale(mul(T0,T1),2)
fac=mul(pw(H,2),pw(add(H,pad([F(0),F(1)])),2))
P0=pol(polynomial_at_h(mul(sq0,fac),6,H),h)
P1=pol(polynomial_at_h(mul(sq1,fac),6,H),h)
R2h=(P0+r*P1)/(h**2*(h+1)**2)
R2target=(h**2-(4+r)*h-4)**2*(h**2-(4-2*r)*h+1)/(25*h**2*(h+1)**2)
check('multiplier_square_global_candidate',sp.expand(sp.together(R2h-R2target).as_numer_denom()[0])==0)
Nm=1-(6+r)*t+(1+r)*t**2
check('gauge_square_in_t',sp.simplify(t**2*R2h.subs(h,1/t-1)/Delta-Nm**2/(25*(1-t)**2*cp))==0)
Tunit=pad(tq[1:]);Sq=add(pad([F(1)]),mul(theta(Tunit),inv(Tunit)))
St=compose(Sq,qt);ss=mul(derivative(St),inv(St))
tQ=add(add(scale(shift(derivative(ss),1),F(-1,2)),scale(shift(mul(ss,ss),1),F(-1,4))),scale(ss,F(-1,2)))
Dc=pad([F(int(sp.Poly(Delta,t).nth(i))) for i in range(5)]);om=pad([F(1),F(-1)])
Qnum=mul(tQ,mul(pw(om,2),pw(Dc,2)))
check('connection_degree_eight_bound_jets',all(v==0 for v in Qnum[9:N-5]))
Qn=pol(Qnum[:9],t);Q=Qn/(t*(1-t)**2*Delta**2)
Qexpected=(256*t**8-1344*t**7+3200*t**6-4176*t**5+3104*t**4-1316*t**3+320*t**2-49*t+6)/4
check('connection_explicit_numerator',Qn==Qexpected)
check('cusp_one_double_pole',sp.limit((t-1)**2*Q,t,1)==F(1,4))
check('branch_double_poles_polynomial_identity',sp.rem(sp.Poly(16*Qn-3*t*(t-1)**2*sp.diff(Delta,t)**2,t),sp.Poly(Delta,t)).is_zero)
ek=[F(0)]+[F(sum(chi(d)*d**3 for d in range(1,n+1) if n%d==0)) for n in range(1,N)]
fk=[F(0)]+[F(sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d==0)) for n in range(1,N)]
VE=pad([F(0)]+[ek[n]-(5*ek[n//2] if n%2==0 else 0)+(4*ek[n//4] if n%4==0 else 0) for n in range(1,N)])
VF=pad([F(0)]+[F(-5,4)*(fk[n]-(20*fk[n//2] if n%2==0 else 0)+(64*fk[n//4] if n%4==0 else 0)) for n in range(1,N)])
AV0=add(mul(AE,VE),scale(mul(AF,VF),5));AV1=add(mul(AE,VF),mul(AF,VE))
dunit=pad(theta(tq)[1:]);fac=mul(pw(Tunit,2),pw(dunit,-3))
U0=compose(mul(pad(AV0[1:]),fac),qt);U1=compose(mul(pad(AV1[1:]),fac),qt)
Ud=mul(pw(om,3),Dc);Un0=mul(U0,Ud);Un1=mul(U1,Ud)
check('forcing_degree_six_bound_jets',all(v==0 for v in Un0[7:N-5]+Un1[7:N-5]))
Un=pol(Un0[:7],t)+r*pol(Un1[:7],t)
check('forcing_nonzero',Un!=0)
# Exact Laurent jet check of the gauge Sym^2 operator, without huge expansion.
def pm(a,b):return (add(mul(a[0],b[0]),scale(mul(a[1],b[1]),5)),add(mul(a[0],b[1]),mul(a[1],b[0])))
def pi(a):
 ii=inv(add(mul(a[0],a[0]),scale(mul(a[1],a[1]),-5)))
 return mul(a[0],ii),scale(mul(a[1],ii),-1)
Np=(pad([F(1),F(-6),F(1)]),pad([F(0),F(-1),F(1)]))
Cp=(pad([F(1),F(-6),F(6)]),pad([F(0),F(-2),F(2)]))
nr=pm((derivative(Np[0]),derivative(Np[1])),pi(Np))
cr=pm((derivative(Cp[0]),derivative(Cp[1])),pi(Cp))
rho=(add(add(nr[0],inv(om)),scale(cr[0],F(-1,2))),add(nr[1],scale(cr[1],F(-1,2))))
zero=(F(0),F(0));one=(F(1),F(0))
def pcadd(a,b):return a[0]+b[0],a[1]+b[1]
def pcmul(a,b):return a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def ld(a,sh=0):return {i+sh:(v,a[1][i]) for i,v in enumerate(a[0]) if v or a[1][i]}
def la(a,b):
 o=dict(a)
 for k,v in b.items():o[k]=pcadd(o.get(k,zero),v)
 return {k:v for k,v in o.items() if v!=zero}
def ls(a,c):return {k:(v[0]*c,v[1]*c) for k,v in a.items() if v!=zero}
def lm(a,b):
 o={}
 for k,v in a.items():
  for j,w in b.items():
   if -8<=k+j<N:o[k+j]=pcadd(o.get(k+j,zero),pcmul(v,w))
 return {k:v for k,v in o.items() if v!=zero}
def dd(a):return {k-1:(k*v[0],k*v[1]) for k,v in a.items() if k and v!=zero}
rr=ld(rho);pp={-1:one};qq=ld((mul(Qnum,inv(mul(pw(om,2),pw(Dc,2)))),pad([])),-1)
rr2=lm(rr,rr);dr=dd(rr)
aa2=la(ls(pp,3),ls(rr,-3))
base1=la(lm(pp,pp),ls(qq,4))
aa1=la(la(ls(la(rr2,ls(dr,-1)),3),ls(lm(pp,rr),-6)),base1)
aa0=la(la(la(ls(lm(rr2,rr),-1),ls(lm(rr,dr),3)),ls(dd(dr),-1)),ls(lm(pp,la(rr2,ls(dr,-1))),3))
aa0=la(la(aa0,ls(lm(base1,rr),-1)),la(ls(dd(qq),2),ls(lm(pp,qq),4)))
def L3(jet):return la(la(la(dd(dd(dd(jet))),lm(aa2,dd(dd(jet)))),lm(aa1,dd(jet))),lm(aa0,jet))
At=(compose(AE,qt),compose(AF,qt))
fe=pad([F(0)]+[VE[n]/n**3 for n in range(1,N)])
ff=pad([F(0)]+[VF[n]/n**3 for n in range(1,N)])
Hraw=(compose(add(mul(AE,fe),scale(mul(AF,ff),5)),qt),compose(add(mul(AE,ff),mul(AF,fe)),qt))
forcingjet=ld((U0,U1),-2)
for label,res in [('homogeneous_multiplier',L3(ld(At))),('actual_inhomogeneous_identity',la(L3(ld(Hraw)),ls(forcingjet,-1)))]:
 check(label,all(res.get(k,zero)==zero for k in range(-5,N-12)))
check('distinct_quadratic_twists',sp.resultant(cp,cm,t)!=0 and sp.discriminant(cp,t)!=0 and sp.discriminant(cm,t)!=0)
check('cubic_cusp_log_nonzero',F(1,25)*F(17,100)*5**3/F(6)==F(17,120))
for n in range(1,N):
 d=20*lcm(*range(1,n+1))**3
 check('safe_three_lcm_layers_'+str(n),all((d*v[n]).denominator==1 for v in Hraw))
out={
 'status':'exact_level20_model_checks_passed','N':N,'checks':checks,
 'h_exponents':rs[0],'u_exponents':rs[1],'B_exponents':rs[2],
 'double_cover_quartic':str(quartic),'Delta':str(Delta),
 'Q':str(Q),'forcing_numerator_rational':[str(x) for x in Un0[:7]],
 'forcing_numerator_sqrt5':[str(x) for x in Un1[:7]],
 't_q':[str(x) for x in tq[:12]],'q_t':[str(x) for x in qt[:12]],
 'mathematical_rank_claim':{'each_embedding':4,'joint':7},
 'proof_scope':'Jets supplement global eta divisors, rational pole bounds, monodromy rank proof. No final arithmetic-holonomy contradiction and no new numerical irrationality theorem.',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
report=Path(__file__).with_name('cdt_odd_level20_model_20261006.md')
if report.exists():out['report_sha256']=hashlib.sha256(report.read_bytes()).hexdigest()
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'checks_passed':len(checks),'forcing_numerator':str(Un)},ensure_ascii=False))
