"""Three prescribed group-derived endpoints, not a prime/parameter scan.

Standalone new certificate.  No old or peer producer is imported/executed.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import gcd
import json
import sympy as sp

checks=[]
def check(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value: raise AssertionError(name)
def B3(x): return x**3-Q(3,2)*x*x+Q(1,2)*x
def frac(x): return x-x.numerator//x.denominator
def chi(a): return {1:1,5:-1,7:-1,11:1}.get(a%12,0)
U={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
def endpoint(k,h,sg):
    hi=pow(h,-1,k)
    def T(a):
        ai=pow(a,-1,k)
        return sum((k-2*((m*ai)%k))*B3(Q(m,k)) for m in range(1,k))/(3*k)
    triv=sum(Q(240*u,j**3)*T((h*j)%k) for j,u in U.items())
    H=[0]*k
    for a in range(1,13): H[(h*a)%k]+=chi(a)
    cs=[0]*k;step=(12*h)%k;m=0
    for n in range(1,k):
        nxt=(m+step)%k;cs[nxt]=cs[m]+H[nxt];m=nxt
    check('E recurrence closes '+str(k),cs[0]-cs[m]==H[0])
    check('E finite kernel at one '+str(k),sum(cs)==0)
    check('E finite kernel odd '+str(k),all(cs[k-m]==-cs[m] for m in range(1,k)))
    E=Q(2,3)*sum(c*B3(Q(m,k)) for m,c in enumerate(cs))
    F=Q(12,3*k)*sum((k-2*((m*hi)%k))*sum(chi(a)*B3(frac(Q(a,12)+Q(m,k))) for a in range(1,13)) for m in range(1,k))
    I=triv+2880*(E+sg*F)
    check('radial character/pole compatibility '+str(k),chi(k)==-sg)
    return {'triv':triv,'E':E,'kappaF':F,'Tate':I}

data13=endpoint(13,1,-1)
data37=endpoint(37,15,-1)
data139=endpoint(139,9,1)
for key,val in {'triv':Q(18547200,2197),'E':Q(-472,2197),'kappaF':Q(5968,2197),'Tate':Q(0)}.items():
    check('endpoint13 '+key,data13[key]==val)
for key,val in {'triv':Q(683326080,50653),'E':Q(7004,50653),'kappaF':Q(7433,50653),'Tate':Q(498240,37)}.items():
    check('endpoint37 '+key,data37[key]==val)
for key,val in {'triv':Q(25179461760,2685619),'E':Q(-156120,2685619),'kappaF':Q(26135960,8056857),'Tate':Q(2578560,139)}.items():
    check('endpoint139 '+key,data139[key]==val)

W=sp.Matrix([[0,-1],[12,0]])
M=sp.Matrix([[24,-7],[84,-24]])
Mc=sp.Matrix([[-24,-7],[84,24]])
g5=sp.Matrix([[5,2],[12,5]])
eta=sp.Matrix([[1,0],[12,1]])
Jb=g5*W*g5.inv()
J0=eta*W*eta.inv()
Js=eta*M*eta.inv()
check('deck gamma5 det and character',g5.det()==1 and chi(5)==-1)
check('W other exact matrix',Jb==sp.Matrix([[180,-73],[444,-180]]))
check('W filled translate exact matrix',J0==sp.Matrix([[12,-1],[156,-12]]))
check('M unfilled translate exact matrix',Js==sp.Matrix([[108,-7],[1668,-108]]))
check('eta is already original Hecke word',W*sp.Matrix([[1,-1],[0,1]])*W.inv()==eta)
check('M conjugate same Gamma coset',Mc*M.inv()==sp.Matrix([[97,-28],[-336,97]]))
check('W other anti coset in Gamma',Jb*W.inv()==sp.Matrix([[73,15],[180,37]]) and chi(37)==1)
check('M translate anti coset in Gamma',all(z.q==1 for z in Js*M.inv()) and (Js*M.inv())[1,0]%12==0 and chi(int((Js*M.inv())[1,1]))==1)
for name,J,h,k in [('Wother',Jb,15,37),('Wfilled',J0,1,13),('Munfilled',Js,9,139)]:
    check(name+' determinant and trace',J.det()==12 and sp.trace(J)==0)
    check(name+' central square',J*J==-12*sp.eye(2))
    check(name+' endpoint reduced',sp.Rational(J[0,0],J[1,0])==sp.Rational(h,k))

expected={1:Q(460),2:Q(-36160,3),3:Q(13785),4:Q(-73520,3),6:Q(108480),12:Q(-66240)}
cusp={}
for c in [1,2,3,4,6,12]:
    bc=sum(Q(u)*Q(gcd(c,j),j)**4 for j,u in U.items())
    ac=1-Q(c*c,12)
    cusp[c]=(bc,ac)
    check('cusp trivial source '+str(c),bc==expected[c])
    check('cusp gauge nonzero '+str(c),ac!=0)
    if c in [2,3,4,6]: check('cusp top cube nonzero '+str(c),bc*ac!=0)

v,r,t=sp.symbols('v r t')
def red(x):
    x=sp.cancel(x)
    num,den=sp.fraction(x)
    return sp.rem(num,r*r-3,r)==0
for delta in [1,-1]:
    aa=2+delta*r
    tv=(v+delta*r/v-1-delta*r)/(2*(1-delta*r))
    check('t involution '+str(delta),red(tv.subs(v,delta*r/v)-tv))
    check('t two zero cusps '+str(delta),red(tv.subs(v,1)) and red(tv.subs(v,delta*r)))
    check('t other real cusps '+str(delta),red(tv.subs(v,-1)-aa) and red(tv.subs(v,-delta*r)-aa))
    check('t complex cusp '+str(delta),red(tv.subs(v,sp.I)-(aa+sp.I)/2))
    check('complex cusp squared modulus '+str(delta),red((aa**2+1)/4-aa))
    vp=sp.expand(2*(1-delta*r)*t+1+delta*r)
    check('double cover discriminant '+str(delta),red(vp**2-4*delta*r-(1-delta*r)**2*(1-4*aa*t+4*t*t)))
    gg=(1-4*aa*t+4*t*t)**2
    check('fixed holomorphic derivative gauge '+str(delta),sp.degree(gg,t)==4 and gg.subs(t,0)==1)
    check('unit Mobius derivative '+str(delta),sp.diff(t/(1-t/aa),t).subs(t,0)==1)
    check('unit Mobius infinity cusp '+str(delta),sp.limit(t/(1-t/aa),t,sp.oo)==-aa)
check('a plus times a minus unit',sp.expand((2+r)*(2-r)-(4-r*r))==0)
check('complex cusp radius identity',sp.expand((2+r)**2+1-4*(2+r))==r*r-3)

out={'check_count':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,
 'endpoints':{str(k):{a:str(b) for a,b in dat.items()} for k,dat in [(13,data13),(37,data37),(139,data139)]},
 'cusp_constants':{str(c):{'triv':str(b),'gauge':str(a)} for c,(b,a) in cusp.items()},
 'scope':['exact group-derived fixed endpoints only','no old producer','no scan',
          'not a classification of all branch leaf cocycles','no CDT numerical conclusion']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':out['all_passed']},ensure_ascii=False))
