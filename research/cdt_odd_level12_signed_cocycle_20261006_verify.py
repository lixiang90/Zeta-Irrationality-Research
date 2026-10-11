"""NEW fixed symbolic certificate; no imported research producer or parameter scan."""
import json
from pathlib import Path
import sympy as s

t, n, j, Theta = s.symbols('t n j Theta', real=True)
T=s.Matrix([[1,1],[0,1]])
W=s.Matrix([[0,-1],[12,0]])
M=s.Matrix([[24,-7],[84,-24]])
Mp=s.Matrix([[-24,-7],[84,24]])
eta=s.Matrix([[1,0],[12,1]])
etan=s.Matrix([[1,0],[12*n,1]])
etain=s.Matrix([[1,0],[-12*n,1]])
checks=[]

def add(name, condition):
    passed=bool(condition)
    checks.append({'name':name,'passed':passed})
    if not passed:
        raise AssertionError(name)

def eq(a,b):
    return s.cancel(a-b)==0

def slash(poly,g):
    a,b,c,d=list(g)
    return s.cancel((c*t+d)**2*poly.subs(t,(a*t+b)/(c*t+d))/g.det())

add('M determinant12',M.det()==12)
add('M tracezero',s.trace(M)==0)
add('M central square',M*M==-12*s.eye(2))
add('Mprime determinant12',Mp.det()==12)
add('Mprime central square',Mp*Mp==-12*s.eye(2))
add('Mprime coset ratio',Mp*M.inv()==s.Matrix([[97,-28],[-336,97]]))
add('eta W conjugate',W*T.inv()*W.inv()==eta)
add('eta membership determinant1',eta.det()==1)
add('W eta scalar TminusW',W*eta==-12*T.inv()*W.inv())
add('tau2 eta unchanged',eq(slash(t**2,eta),t**2))
add('tau eta',eq(slash(t,eta),t+12*t**2))
add('negative weight slash right action',eq(slash(slash(1+3*t+7*t**2,W),eta),slash(1+3*t+7*t**2,W*eta)))

# Work in the real rational coefficient of i*pi^3. Cubic completion is -176640*t^3.
cubic=-176640*t**3
D=s.expand(cubic.subs(t,t-1)-cubic)
add('completed translation defect',eq(D,529920*t**2-529920*t+176640))
add('completed reciprocal W coefficient',eq(slash(cubic,W),s.Rational(3680,3)/t))
add('translation W polynomial',eq(slash(D,W),44160+529920*t+2119680*t**2))
add('Theta tau2 exact cancellation',eq(slash(12*Theta*t**2,eta)-12*Theta*t**2,0))
P=44160+529920*t+2073600*t**2
add('actual eta defect',eq(slash(D,W)+slash(-3840*t,eta)+3840*t,P))
add('base positive discriminant',s.discriminant(P/44160,t)==-s.Rational(1008,23))
Pn=44160*n+529920*n**2*t+(2119680*n**3-46080*n)*t**2
add('Pn zero at0',eq(Pn.subs(n,0),0))
add('Pn base at1',eq(Pn.subs(n,1),P))
add('full integer recurrence',eq(Pn.subs(n,n+1)-Pn,slash(P,etan)))
add('full inverse recurrence',eq(Pn.subs(n,-n),-slash(Pn,etain)))
add('all n discriminant',eq(s.discriminant(Pn,t),-4069785600*n**2*(23*n**2-2)))
Jn=etan*M*etain
expected=s.Matrix([[24+84*n,-7],[84+576*n+1008*n**2,-24-84*n]])
add('Jn full symbolic matrix',all(eq(x,y) for x,y in zip(Jn,expected)))
add('Jn determinant',eq(Jn.det(),12))
add('Jn trace',eq(s.trace(Jn),0))
add('Jn full endpoint',eq(Jn[0,0]/Jn[1,0],(7*n+2)/(84*n**2+48*n+7)))
Cjn=slash(Pn+slash(Pn,M),etain)
Q=1+(Jn[1,0]*t-Jn[0,0])**2/12
lam=1920*n*(644*n**2+552*n+147)/(84*n**2+48*n+7)
add('Jn exact scalar period',eq(Cjn,lam*Q))
add('Jn invariant quadratic',eq(slash(Q,Jn),Q))
add('Jn period fixed n1',eq(lam.subs(n,1),s.Rational(2578560,139)))
add('numerator quadratic positive discriminant',s.discriminant(644*n**2+552*n+147,n)==-73968)
add('denominator quadratic positive discriminant',s.discriminant(84*n**2+48*n+7,n)==-48)

result={'scope':'NEW fixed symbolic identities; no search, no imported producer',
        'checks':checks,'passed':len(checks),
        'eta_polynomial':str(P),'eta_n_polynomial':str(Pn),
        'Jn_Tate_coefficient':str(lam)}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'passed':len(checks),'failed':0}))
