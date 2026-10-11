"""NEW fixed symbolic certificate; no primes, imports of project producers, or scans."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as s

p,h=s.symbols('p h')
T=s.symbols('T0:5')
V=s.symbols('V0:5')
W=s.symbols('W0:5')
def delta(expr):
    ans=0
    for family in (T,V):
        for i in range(4):
            ans += s.diff(expr,family[i])*family[i+1]
    for i in range(4):
        ans += s.diff(expr,W[i])*p*W[i+1]
    return s.expand(ans)
def full_theta(expr):
    return s.expand(h*expr+delta(expr))

B=T[0]*V[1]-V[0]*T[1]
B1=delta(B)
Q=T[0]**2+B
Q1=delta(Q)
P2=Q*T[0]
P1=-(2*h*Q+Q1)*T[0]
P0=(h*h*Q+h*Q1)*T[0]+Q1*T[1]-Q*T[2]-p*s.Rational(1,2)*(T[0]*B1-2*B*T[1])
U=T[0]*W[0]+p*V[0]*(W[1]+W[0]/2)
residual=s.Poly(s.expand(P2*full_theta(full_theta(U))+P1*full_theta(U)+P0*U),p)
first=s.expand(T[0]*full_theta(T[0]*W[0])-(h*T[0]+T[1])*T[0]*W[0])

checks=[]
def ck(label,condition,value=None):
    assert bool(condition),label
    checks.append({'name':label,'passed':True,'value':str(value) if value is not None else None})
ck('S1 abstract all-W identity',s.expand(first-p*T[0]**2*W[1])==0)
ck('S2 abstract p^0 coefficient',residual.nth(0)==0)
ck('S2 abstract p^1 coefficient',residual.nth(1)==0)
ck('Q derivative identity',s.expand(Q1-2*T[0]*T[1]-B1)==0)
ck('QT^2 to QT cancellation',s.expand(Q*B1-B*Q1-T[0]*(T[0]*B1-2*B*T[1]))==0)
ck('B derivative cancellation',s.expand(B1-(T[0]*V[2]-V[0]*T[2]))==0)
# The product (Q theta-hQ-Q1) o (T theta-hT-T1).
nested_const=s.expand(Q*delta(-h*T[0]-T[1])+(-h*Q-Q1)*(-h*T[0]-T[1]))
nested_theta=s.expand(Q*(delta(T[0])-h*T[0]-T[1])+(-h*Q-Q1)*T[0])
ck('nested order2 coefficient',s.expand(Q*T[0]-P2)==0)
ck('nested order1 coefficient',s.expand(nested_theta-P1)==0)
ck('nested order0 coefficient mod p',s.expand(nested_const-P0.subs(p,0))==0)
nu=[0]+[4]*4+[11]*5
ck('actual row count',len(nu)==10)
ck('sum nu',sum(nu)==71)
ck('baseline capped floor',sum(11-v for v in nu)==39)
gamma1=3*(Fraction(2)-Fraction(2)**2/4)
gamma2=2*(Fraction(2,3)-3*Fraction(2,3)**2/4)
ck('gamma first threshold',gamma1==3,gamma1)
ck('gamma second threshold',gamma2==Fraction(2,3),gamma2)
gamma=gamma1+gamma2
ck('layered gamma',gamma==Fraction(11,3),gamma)
ck('near-balanced cost normalization',2*gamma/Fraction(100)==Fraction(11,150),2*gamma/100)

out={'scope':'Fixed abstract symbolic all-W elimination and rational ledger only; no p examples, no all-prefix numerical certificate.',
     'count':len(checks),'all_passed':True,'checks':checks,
     'abstract_residual_p2':str(s.factor(residual.nth(2)))}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'count':len(checks),'all_passed':True}))
