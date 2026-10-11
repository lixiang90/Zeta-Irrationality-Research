"""New finite checks only; imports no frozen mathematical producers."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []
def check(name, value):
    value = bool(value)
    checks.append({'name': name, 'passed': value})
    assert value, name

def vp(a, p):
    if not a:
        return 100000
    a = F(a)
    z = 0
    n, d = a.numerator, a.denominator
    while n % p == 0:
        n //= p; z += 1
    while d % p == 0:
        d //= p; z -= 1
    return z

def delta(n, q):
    r = n % q
    if q % 4 == 1:
        return int(r >= (3*q+1)//4)-int(r >= (q-1)//4)
    return int(r >= (q+1)//4)-int(r >= (3*q-1)//4)

cn = [F(1)]
an = [F(0), F(256, 81)]
for n in range(1, 97):
    cn.append(cn[-1]*F(4*n-1, 4*n+1)**4)
for n in range(2, 97):
    an.append(an[-1]*F(2*n-2, 2*n+1)**4)
primes = list(s.primerange(3, 390))
ok = True
for p in primes:
    for n in range(97):
        q, total = p, 0
        while q <= 4*n+1:
            total += delta(n, q); q *= p
        ok &= vp(cn[n], p) == 4*total
check('actual Q9 all listed primes n=0..96', ok)
check('all J coefficients n=0..96 are 2-units', all(vp(c, 2)==0 for c in cn))
dj = dh = 1
okj = okh = True
for n in range(97):
    dj = lcm(dj, cn[n].denominator)
    if n:
        dh = lcm(dh, an[n].denominator)
    ej = eh = 1
    for p in primes:
        q = p if p % 4 == 1 else p*p
        step = q
        while q <= 4*n+1:
            ej *= int(p)**4; q *= step
        q = p
        while q <= 2*n+1:
            eh *= int(p)**4; q *= p
    okj &= dj == ej; okh &= dh == eh
check('exact least J prefix denominator N=0..96', okj)
check('exact least H prefix denominator N=0..96', okh)
check('inert p3 denominator not deleted c2', cn[2]==F(7,15)**4 and vp(cn[2],3)==-4)
check('J coefficient forcing recurrence all n=1..96', all((F(n)+F(1,4))**4*cn[n]==(F(n)-F(1,4))**4*cn[n-1] for n in range(1,97)))

def add(a,b):
    return [ (a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b))) ]
def mul(a,b, length=None):
    out = [F(0)]*(len(a)+len(b)-1 if length is None else length)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<len(out): out[i+j]+=x*y
    return out
def scale(a,c): return [c*x for x in a]
def th(a): return [i*x for i,x in enumerate(a)]
def theta_power(a,k): return [i**k*x for i,x in enumerate(a)]
def modular(a,p,e):
    a=F(a)
    assert vp(a,p)>=0
    modulus=p**e
    return a.numerator*pow(a.denominator,-1,modulus)%modulus

for p in [5,13,17]:
    h,d=(p-1)//4,(p-1)//2
    N=min(96,(p*p-2)//4)
    t,v=[F(1)],[F(0)]
    for j in range(1,d+1):
        t.append(t[-1]*F(2*j-1,2*j)**4)
        v.append(t[-1]*4*sum((F(2,2*k+1)-F(1,k+1) for k in range(j)),F(0)))
    u=scale(cn[:N],p**4)
    packet=[F(0)]*N
    for k in range((N-h+p-1)//p):
        n0=h+k*p
        if n0>=N: break
        w=u[n0]
        for j in range(d+1):
            if n0+j<N:
                packet[n0+j]+=w*(t[j]+p*F(4*k+1,4)*v[j])
    check(f'actual full-prefix packet p={p} N={N}', all(vp(a-b,p)>=2 for a,b in zip(u,packet)))
    b=add(mul(t,th(v)),scale(mul(v,th(t)),-1))
    q=add(mul(t,t),b)
    p2=mul(q,t)
    p1=scale(mul(add(scale(q,2*h),th(q)),t),-1)
    p0=add(mul(add(scale(q,h*h),scale(th(q),h)),t),mul(th(q),th(t)))
    p0=add(p0,scale(mul(q,th(th(t))),-1))
    correction=add(mul(t,th(b)),scale(mul(b,th(t)),-2))
    p0=add(p0,scale(correction,-F(p,4)))
    l1=add(mul(t,th(u),N),scale(mul(add(scale(t,h),th(t)),u,N),-1))
    l2=add(add(mul(p2,th(th(u)),N),mul(p1,th(u),N)),mul(p0,u,N))
    check(f'actual L1,L2,derivatives prefix p={p}', all(vp(a,p)>=1 for a in l1) and all(vp(a,p)>=2 for a in l2))
    check(f'QT top degree and p-unit p={p}', len(p2)-1==3*d and vp(p2[-1],p)==0)

# Generic fast/slow conjugation identities, not a finite-prime argument.
T,V=s.Function('T'),s.Function('V')
x,h,p,b=s.symbols('x h p b')
theta=lambda e:s.diff(e,x)*x
tt,vv=T(x),V(x)
BB=tt*theta(vv)-vv*theta(tt)
QQ=tt**2+BB
check('generic clearing identity', s.simplify(QQ*theta(BB)-BB*theta(QQ)-tt*(tt*theta(BB)-2*BB*theta(tt)))==0)
a=h+theta(tt)/tt
PP2=QQ*tt
PP1=-(2*h*QQ+theta(QQ))*tt
PP0=(h*h*QQ+h*theta(QQ))*tt+theta(QQ)*theta(tt)-QQ*theta(theta(tt))-p*b*(tt*theta(BB)-2*BB*theta(tt))
dd=tt*theta(BB)-2*BB*theta(tt)
check('generic conjugation theta coefficient', s.simplify(-2*a*PP2-dd-PP1)==0)
check('generic conjugation constant coefficient', s.simplify(PP2*(a*a-theta(a))+dd*a-p*b*dd-PP0)==0)
check('generic nested L2 modp theta coefficient', s.simplify(QQ*theta(tt)+(-h*QQ-theta(QQ))*tt-QQ*(h*tt+theta(tt))-PP1)==0)
check('generic nested L2 modp constant coefficient', s.simplify(-QQ*theta(h*tt+theta(tt))+(h*QQ+theta(QQ))*(h*tt+theta(tt))-(PP0+p*b*dd))==0)
y=s.symbols('y', real=True)
tau=2*(s.integrate(4*s.Rational(4,5),(y,0,s.Rational(4,5)))+s.integrate(4*(1-y/4),(y,s.Rational(4,5),4)))
gamma=s.Rational(1,2)*(s.integrate(3*(1-y/2),(y,0,2))+s.integrate(2*(1-3*y/2),(y,0,s.Rational(2,3))))
check('ordinary full-density max transport', tau==s.Rational(384,25))
check('split two-layer prime integral', gamma==s.Rational(11,6))
check('same-rank-five normalized kappa', tau/2-2*gamma/25==s.Rational(113,15))
check('Gamma quarter endpoint multiplier arithmetic', 4**4*(s.sqrt(2))**4==1024)
output={'scope':'Finite rational/algebraic checks; no proof of all-prime valuations, global rank, analytic leaf, or numeric irrationality.',
        'execution_history':['first single execution; see exit status in delivery review'],
        'checks':checks,'finite_check_count':len(checks),'all_passed':all(c['passed'] for c in checks),
        'numeric_irrationality_proved':False,'lean_verified':False}
out=ROOT/'cdt_odd_quarter_shift_smith_20261006_verify.json'
out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'all_passed':output['all_passed'],'certificate':str(out)},ensure_ascii=False))
