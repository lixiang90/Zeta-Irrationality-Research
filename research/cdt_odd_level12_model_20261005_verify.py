"""Exact level-12 model data. Finite checks supplement the pole-bound proof."""
from fractions import Fraction as F
from math import comb, gcd, lcm
from pathlib import Path
import json, sys
import sympy as sp
sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
N=36
def pad(a): return list(a[:N])+[F(0)]*max(0,N-len(a))
def add(a,b): return [a[i]+b[i] for i in range(N)]
def scale(a,c): return [v*c for v in a]
def mul(a,b):
    out=[F(0)]*N
    for i,v in enumerate(a):
        if not v: continue
        for j in range(N-i):
            if b[j]:out[i+j]+=v*b[j]
    return out
def inv(a):
    out=[F(0)]*N;out[0]=1/a[0]
    for n in range(1,N):out[n]=-sum(a[k]*out[n-k] for k in range(1,n+1))/a[0]
    return out
def pw(a,k):
    if k<0:return pw(inv(a),-k)
    out=pad([F(1)])
    for _ in range(k):out=mul(out,a)
    return out
def compose(a,b):
    assert b[0]==0
    out=pad([]);p=pad([F(1)])
    for v in a:
        out=add(out,scale(p,v));p=mul(p,b)
    return out
def derivative(a): return pad([(i+1)*a[i+1] for i in range(N-1)])
def revert(a):
    assert a[0]==0 and a[1]==1
    unit=pad(a[1:]);iu=inv(unit);p=pad([F(1)]);out=pad([])
    for n in range(1,N):
        p=mul(p,iu);out[n]=p[n-1]/n
    assert all(v.denominator==1 for v in out)
    return out
def eta_unit(ds,rs):
    out=pad([F(1)])
    for d,r in zip(ds,rs):
        for m in range(d,N,d):
            factor=pad([])
            for j in range((N-1)//m+1):
                bc=comb(r,j) if r>=0 and j<=r else (0 if r>=0 else (-1)**j*comb(-r+j-1,j))
                factor[j*m]=F((-1)**j*bc)
            out=mul(out,factor)
    return out
def coeffs(a):return [str(v) for v in a]
def pol(a,var): return sum(sp.Rational(v.numerator,v.denominator)*var**i for i,v in enumerate(a))
def vp(v,p):
    if v==0:return None
    a,b=abs(v.numerator),v.denominator;out=0
    while a%p==0:a//=p;out+=1
    while b%p==0:b//=p;out-=1
    return out
def sigma(n,k):return sum(d**k for d in range(1,n+1) if n%d==0)
ds=[1,2,3,4,6,12]
rh=[3,-2,-1,1,2,-3]
orders=sp.Matrix([[sp.Rational(12,24*sp.gcd(c*c,12))*sp.Rational(sp.gcd(c,d)**2,d) for d in ds] for c in ds])
assert orders*sp.Matrix(rh)==sp.Matrix([1,0,0,0,0,-1])
assert sum(rh)==0 and sum(d*r for d,r in zip(ds,rh))==-24
assert sum((12//d)*r for d,r in zip(ds,rh))==24
assert sp.prod(sp.Rational(d)**r for d,r in zip(ds,rh))==sp.Rational(1,144)
assert list(reversed(rh))==[-r for r in rh]
cusp_h={}
cusp_exponents={}
for i,c in enumerate(ds[:-1]):
    target=sp.zeros(6,1);target[i]=1;target[-1]=-1
    rc=list(orders.inv()*target)
    assert all(r.q==1 for r in rc)
    assert sum(rc)==0
    assert sum(d*r for d,r in zip(ds,rc))%24==0
    assert sum((12//d)*r for d,r in zip(ds,rc))%24==0
    product=sp.prod(sp.Rational(d)**r for d,r in zip(ds,rc))
    assert sp.sqrt(product).is_Rational
    cusp_exponents[str(c)]=[int(r) for r in rc]
    cusp_h[str(c)]=int(-rh[0]+rc[0])
assert cusp_h=={'1':0,'2':-6,'3':-4,'4':-3,'6':-2}
u=eta_unit(ds,[-r for r in rh])
x=pad([F(0)]+u[:-1])
qx=revert(x)
S=add(pad([F(1)]),pad([F(0)]+mul(derivative(u),inv(u))[:-1]))
Sx=compose(S,qx)
A=pad([F(-1727)]+[F(-504*sigma(n,5)+(1728*504*sigma(n//12,5) if n%12==0 else 0)) for n in range(1,N)])
cs=[4,-2288,46332,-146432,185328,-82944]
assert sum(cs)==0
Fa=pad([F(0)]+[F(sum(c*sigma(n//d,7) for d,c in zip(ds,cs) if n%d==0)) for n in range(1,N)])
f=pad([F(0)]+[Fa[n]/n**7 for n in range(1,N)])
Ax=compose(A,qx);Fx=compose(Fa,qx)
Rser=mul(Ax,pw(Sx,-3));Tser=mul(Fx,pw(Sx,-4))
X=sp.Symbol('x')
Dpoly=sp.Poly((1+2*X)*(1+3*X)*(1+4*X)*(1+6*X),X)
D=pad([F(int(Dpoly.nth(i))) for i in range(5)])
RN=mul(Rser,pw(D,3));TN=mul(Tser,pw(D,4))
assert all(v==0 for v in RN[13:N-1]),coeffs(RN)
assert all(v==0 for v in TN[16:N-1]),coeffs(TN)
R=sp.cancel(pol(RN[:13],X)/Dpoly.as_expr()**3)
T=sp.cancel(pol(TN[:16],X)/Dpoly.as_expr()**4)
assert sp.cancel(R-R.subs(X,1/(12*X)))==0
assert sp.cancel(T+T.subs(X,1/(12*X)))==0
# Q = -1/2 (S'/S)' -1/4 (S'/S)^2 -1/(2x) S'/S.
log_derivative=mul(derivative(Sx),inv(Sx))
regularQ=add(scale(derivative(log_derivative),F(-1,2)),scale(mul(log_derivative,log_derivative),F(-1,4)))
xQ=add(pad([F(0)]+regularQ[:-1]),scale(log_derivative,F(-1,2)))
QN=mul(xQ,pw(D,2))
assert all(v==0 for v in QN[7:N-3]),coeffs(QN)
Q=sp.cancel(pol(QN[:7],X)/(X*Dpoly.as_expr()**2))
assert sp.degree(sp.numer(Q),X)<=6
for k in [2,3,4,6]:
    xc=sp.Rational(-1,k)
    assert sp.limit((X-xc)**2*Q,X,xc)==sp.Rational(1,4)
assert sp.limit(X**2*Q,X,sp.oo)==0
# Integral Fricke quotient: t=x/(1+8x+12x^2).
den=add(pad([F(1)]),add(scale(x,8),scale(mul(x,x),12)))
tq=mul(x,inv(den))
qt=revert(tq)
assert compose(tq,qt)==pad([F(0),F(1)])
At=compose(A,qt);Bt=compose(mul(A,f),qt)
safe=[]
for n in range(1,N):
    delta=lcm(*range(1,n+1))**7
    assert (Bt[n]*delta).denominator==1
    safe.append(n)
packets=[]
for p in (11,13,17,19,23,29,31):
    assert vp(Bt[p+1],p)==-7
    assert (Bt[p+1]*p**7).denominator%p!=0
    w=Bt[p+1]*p**7
    residue=(w.numerator*pow(w.denominator,-1,p))%p
    assert residue==(-2016)%p
    packets.append({'p':p,'index':p+1,'valuation':-7,'leading_residue':residue})
tt=X/(1+8*X+12*X**2)
assert sp.cancel(tt-tt.subs(X,1/(12*X)))==0
alpha=(2-sp.sqrt(3))/4;beta=(2+sp.sqrt(3))/4
assert sp.simplify(tt.subs(X,1/sp.sqrt(12))-alpha)==0
assert sp.simplify(tt.subs(X,-1/sp.sqrt(12))-beta)==0
assert tt.subs(X,sp.Rational(-1,4))==1 and tt.subs(X,sp.Rational(-1,3))==1
# Exact cusp constants produce the log^7 monodromy test.
Ac=1-sp.Rational(1728,6**6)
Fc=sum(sp.Rational(c,480)*sp.Rational(sp.gcd(2,d),d)**8 for d,c in zip(ds,cs))
assert Ac==sp.Rational(26,27) and Fc==sp.Rational(-476,81)
# Explicit second-order and modular ratios directly on the Fricke quotient.
local_t=mul(pad([F(0),F(1)]),inv(pad([F(1),F(8),F(12)])))
xt=revert(local_t)
one_minus=pad([F(1),F(-1)])
Delta=pad([F(1),F(-16),F(16)])
Rtn=mul(compose(Rser,xt),pw(one_minus,3))
Iser=mul(Tser,mul(pad([F(0),F(1)]),inv(pad([F(1),F(0),F(-12)]))))
Itn=mul(compose(Iser,xt),pw(one_minus,4))
assert all(v==0 for v in Rtn[7:N-1])
assert all(v==0 for v in Itn[9:N-1])
Z=sp.Symbol('t')
Rt=sp.cancel(pol(Rtn[:7],Z)/(1-Z)**3)
It=sp.cancel(pol(Itn[:9],Z)/(1-Z)**4)
v=1/X-12*X
assert sp.cancel(R-Rt.subs(Z,tt))==0
assert sp.cancel(T-v*It.subs(Z,tt))==0
St=compose(Sx,xt)
ld=mul(derivative(St),inv(St))
regular=add(scale(derivative(ld),F(-1,2)),scale(mul(ld,ld),F(-1,4)))
regular=add(regular,scale(mul(mul(derivative(Delta),inv(Delta)),ld),F(-1,4)))
tQt=add(pad([F(0)]+regular[:-1]),scale(ld,F(-1,2)))
Qtn=mul(tQt,mul(pw(one_minus,2),Delta))
assert all(a==0 for a in Qtn[4:N-3])
Qt=sp.cancel(pol(Qtn[:4],Z)/(Z*(1-Z)**2*(1-16*Z+16*Z**2)))
Pt=1/Z+(-16+32*Z)/(2*(1-16*Z+16*Z**2))
td=sp.diff(tt,X)
assert sp.cancel(Qt.subs(Z,tt)*td**2-Q)==0
assert sp.cancel(Pt.subs(Z,tt)-(sp.diff(td,X)+td/X)/td**2)==0
Ut=sp.cancel(Rt*It/(Z**8*(1-16*Z+16*Z**2)**3))
assert sp.limit(Z**7*Ut,Z,sp.oo)==12376
assert -Ac*Fc*3**7/sp.factorial(7)==sp.Rational(1547,630)
# Execute the canonical seven-order operator as exact Laurent jets.
# Pole-bound/Bol arguments in the report establish the all-order identity.
def ratjet(expr):
    nu,de=map(lambda e:sp.Poly(e,Z),sp.fraction(sp.cancel(expr)))
    an=[F(nu.nth(i)) for i in range(nu.degree()+1)]
    ad=[F(de.nth(i)) for i in range(de.degree()+1)]
    on=next(i for i,a in enumerate(an) if a)
    od=next(i for i,a in enumerate(ad) if a)
    values=mul(pad(an[on:]),inv(pad(ad[od:])))
    return {i+on-od:a for i,a in enumerate(values) if a and i+on-od<N}
def la(a,b):
    d=dict(a)
    for k,v in b.items():d[k]=d.get(k,F(0))+v
    return {k:v for k,v in d.items() if v}
def ls(a,c):return {k:v*c for k,v in a.items() if v*c}
def lm(a,b):
    d={}
    for i,v in a.items():
        for j,w in b.items():
            if -14<=i+j<N:d[i+j]=d.get(i+j,F(0))+v*w
    return {k:v for k,v in d.items() if v}
def ld(a):return {k-1:k*v for k,v in a.items() if k*v}
pj=ratjet(Pt);qj=ratjet(Qt);rg=ratjet(sp.diff(Rt,Z)/Rt)
mr=[[{} for j in range(7)] for i in range(7)]
for j in range(7):
    mr[j][j]=la(rg,ls(pj,-j))
    if j<6:mr[j][j+1]={0:F(6-j)}
    if j>0:mr[j][j-1]=ls(qj,-j)
rows=[[{0:F(1)}]+[{} for _ in range(6)]]
for n in range(7):
    prev=rows[-1];new=[ld(a) for a in prev]
    for i in range(7):
        for j in range(7):new[j]=la(new[j],lm(prev[i],mr[i][j]))
    rows.append(new)
ell=[{} for _ in range(7)]
for i in range(6,-1,-1):
    rem=rows[7][i]
    for j in range(i+1,7):rem=la(rem,ls(lm(ell[j],rows[j][i]),-1))
    diagonal=F(sp.factorial(6)/sp.factorial(6-i))
    assert rows[i][i]=={0:diagonal}
    ell[i]=ls(rem,1/diagonal)
def op7(a):
    jets=[{n:v for n,v in enumerate(a) if v}]
    for i in range(7):jets.append(ld(jets[-1]))
    value=jets[7]
    for i in range(7):value=la(value,ls(lm(ell[i],jets[i]),-1))
    return value
av=op7(At);bv=op7(Bt);uv=ratjet(Ut)
for n in range(-7,15):
    assert av.get(n,0)==0,(n,av.get(n))
    assert bv.get(n,0)==uv.get(n,0),(n,bv.get(n),uv.get(n))
data={
 'status':'exact_level12_model_checks_passed',
 'scope':'Exact series identities with geometric pole bounds documented separately; no irrationality conclusion.',
 'truncation_order':N-1,'hauptmodul_eta_exponents':rh,'cusp_h_values':cusp_h,'cusp_unit_exponents':cusp_exponents,
 'x_q_first':coeffs(x[:10]),'t_q_first':coeffs(tq[:10]),'q_t_first':coeffs(qt[:10]),
 'D':str(Dpoly.as_expr()),
 'Q_numerator':coeffs(QN[:7]),'Q_denominator':'x*D(x)^2',
 'R_numerator':coeffs(RN[:13]),'R_denominator':'D(x)^3',
 'T_numerator':coeffs(TN[:16]),'T_denominator':'D(x)^4',
 'Q_factored':str(sp.factor(Q)),'R_factored':str(sp.factor(R)),'T_factored':str(sp.factor(T)),
 'integer_inverse_verified':True,'fricke_R_invariant':True,'fricke_T_anti_invariant':True,
 'natural_prefix_safe_checked_through':N-1,'highest_p_packets':packets,
 'cusp_2_constants':{'A6':str(Ac),'F8':str(Fc),'product_nonzero':True},
 'quotient_P':str(sp.factor(Pt)),'quotient_Q':str(sp.factor(Qt)),
 'quotient_R':str(sp.factor(Rt)),'quotient_I':str(sp.factor(It)),
 'quotient_forcing_U':str(sp.factor(Ut)),
 'log7_at_infinity_leading':'1547/630',
 'forcing_infinity_leading':'12376',
 'canonical_sym6_operator_jet_checks':{'A_homogeneous':True,'B_forcing':True,'checked_exponents':[-7,14]},
 'quotient_R_numerator':coeffs(Rtn[:7]),'quotient_I_numerator':coeffs(Itn[:9]),
 'quotient_Q_numerator':coeffs(Qtn[:4]),
 'natural_rank8_flat_cost':'441/64',
 'not_proved':['admissible common analytic cover and its exact capacity','strict CDT holonomy contradiction','new irrationality of zeta(7)']
}
out=ROOT/'research/cdt_odd_level12_model_20261005_verify.json'
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ('status','x_q_first','t_q_first','q_t_first','quotient_P','quotient_Q','quotient_R','quotient_I','cusp_2_constants')},ensure_ascii=False))

