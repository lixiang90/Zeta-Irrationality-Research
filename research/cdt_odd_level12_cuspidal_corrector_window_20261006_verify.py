"""NEW fixed cusp basis and two-block reflection certificate; no old producer imports."""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as S

base=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({"name":name,"passed":bool(value)})
    if not value:
        raise AssertionError(name)

v=S.symbols("v")
r=S.sqrt(3)
P=v*(v*v-1)*(v*v-3)*(v*v+1)*(v*v+3)
check("full finite cusp polynomial degree9",S.degree(P,v)==9)
check("nine distinct finite cusps",S.gcd(P,S.diff(P,v))==1)
check("Fricke cusp polynomial exact",S.cancel(P.subs(v,r/v)-9*r*P/v**10)==0)
for k in range(7):
    ratio=S.cancel((3/v**4)*(r/v)**k/P.subs(v,r/v)/(v**(6-k)/P))
    check("C"+str(k)+" exact W coefficient",S.simplify(ratio-r**(k-3))==0)
    check("C"+str(k)+" diamond character",S.cancel((-v)**k/P.subs(v,-v)-(-1)**(k+1)*v**k/P)==0)
WM=S.zeros(7)
for k in range(7): WM[6-k,k]=r**(k-3)
WI=WM.extract([1,3,5],[1,3,5])
WC=WM.extract([0,2,4,6],[0,2,4,6])
check("trivial cusp anti dimension1",3-(WI+S.eye(3)).rank()==1)
check("chi cusp anti dimension2",4-(WC+S.eye(4)).rank()==2)

N=12
def mul(a,b):
    out=[0]*(N+1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                if y: out[i+j]+=x*y
    return out
one=[1]+[0]*N
def inv(a):
    assert a[0]==1
    b=one.copy()
    for n in range(1,N+1):
        b[n]=-sum(a[j]*b[n-j] for j in range(1,n+1))
    return b
def power(a,e):
    if e<0: return power(inv(a),-e)
    out=one.copy()
    for _ in range(e): out=mul(out,a)
    return out
def factor(qdegree,e):
    a=one.copy()
    if qdegree<=N: a[qdegree]=-1
    return power(a,e)
exponents={1:-3,2:2,3:1,4:-1,6:-2,12:3}
xunit=one.copy()
for d,e in exponents.items():
    for n in range(1,N//d+1):
        xunit=mul(xunit,factor(d*n,e))
x=[0]+xunit[:N]
u=[0]*(N+1)
for n in range(1,N+1):
    u2=mul(u,u)
    xu=mul(x,u)
    xu2=mul(x,u2)
    u[n]=x[n]-u2[n]-2*xu[n]-2*xu2[n]
u2=mul(u,u)
check("all fixed q u equation",all(u[n]+u2[n]==x[n]-2*mul(x,u)[n]-2*mul(x,u2)[n] for n in range(N+1)))
vv=[1]+[2*z for z in u[1:]]
du=[n*u[n] for n in range(N+1)]
# du^2/u is q times a product of three integral unit series.
duu=mul(du,du)
uq=u[1:]+[0]
duuq=duu[2:]+[0,0]
core=mul(duuq,inv(uq))
core=[0]+core[:N]
units=[]
units.append([1]+u[1:])
units.append([1]+[-2*(u[n]+u2[n]) for n in range(1,N+1)])
units.append([1]+[2*(u[n]+u2[n]) for n in range(1,N+1)])
units.append([1]+[u[n]+u2[n] for n in range(1,N+1)])
den=one.copy()
for unit in units: den=mul(den,unit)
Cs=[]
for k in range(7):
    a=mul(mul(core,power(vv,k-1)),inv(den))
    Cs.append([-z for z in a])
    check("16C"+str(k)+" fixed coefficients integral",all(isinstance(z,int) for z in a))
    check("16C"+str(k)+" leading coefficient -1",Cs[k][1]==-1)
# Degree N data use u to N only; final coefficient may lose one due division by u.
check("full seven basis independent fixed jets",S.Matrix([[Cs[k][n] for k in range(7)] for n in range(1,9)]).rank()==7)

f6=one.copy()
for d in (1,2,3,6):
    for n in range(1,N//d+1): f6=mul(f6,factor(d*n,2))
f6=[0]+f6[:N]
f62=[f6[n//2] if n%2==0 else 0 for n in range(N+1)]
norm=[F(Cs[5][n]-3*Cs[1][n],2) for n in range(N+1)]
check("anti trivial eta identity Sturm coefficients1..8",all(norm[n]==f6[n]-4*f62[n] for n in range(1,9)))
check("anti trivial eta identity extra coefficients9..11",all(norm[n]==f6[n]-4*f62[n] for n in range(9,12)))

a=S.symbols("a",positive=True)
source_ratio=v*v+r+3/(v*v)
check("positive chi source ratio exact",S.cancel((v**6-3*r)/(v*v*(v*v-r))-source_ratio)==0)
check("ratio lower endpoint3r",S.simplify(source_ratio.subs(v,S.sqrt(r))-3*r)==0)
check("ratio upper endpoint4+r",S.simplify(source_ratio.subs(v,1)-(4+r))==0)
check("ratio derivative exact negative on1<x<r",S.diff(a+r+3/a,a)==1-3/a**2)

n,m=S.symbols("n m",integer=True)
p0=44160*n
p1=529920*n*n
p2=2119680*n**3-46080*n
mu=p0+(m+S.Rational(2,7))*p1+(m*m+S.Rational(4,7)*m+S.Rational(1,12))*p2
sn=644*n**3+552*n*n+147*n
sm=S.expand(S.Rational(7,1920)*mu)
fac=12*n*m*(14*(46*n*n-1)*m+368*n*n+161*n-8)
check("two block full scalar factor",S.expand(sm-sn-fac)==0)
k=S.symbols("k",integer=True,nonnegative=True)
AA=368*n*n+161*n-8
BB=14*(46*n*n-1)
for sign in (1,-1):
    ns=sign*(k+1)
    check("extra root numerator positive branch"+str(sign),all(z>0 for z in S.Poly(AA.subs(n,ns),k).all_coeffs()))
    check("extra root strictly less denominator branch"+str(sign),all(z>0 for z in S.Poly((BB-AA).subs(n,ns),k).all_coeffs()))
check("n0 only T conjugacy",sm.subs(n,0)==0)

report={
    "date":"2026-10-06",
    "scope":"NEW exact complete cusp basis/W decomposition/integral q model, eta anti normalization by Sturm, positive-source ratio identities, full two-block reflection family. No period independence, third zero generator, or numerical irrationality theorem.",
    "execution_history":"First execution passed47 checks; second replaces two dimension bookkeeping checks by actual Fricke eigenspace rank checks and passes47. No old or peer producer import/execution; no word/parameter/prime scan.",
    "passed":len(checks),"checks":checks,
    "C16_coefficients1_to11":{str(k):Cs[k][1:12] for k in range(7)},
    "anti_trivial_eta_coefficients1_to8":[str(z) for z in norm[1:9]],
    "two_block_scalar":str(sm),
    "period_ratio_interval":["3*sqrt(3)","4+sqrt(3)"]
}
(base/"cdt_odd_level12_cuspidal_corrector_window_20261006_verify.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"passed":len(checks),"scope":report["scope"]}))

