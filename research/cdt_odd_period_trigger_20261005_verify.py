"""Fixed exact certificate for the level-12 odd-period trigger; no zeta numerics."""
from fractions import Fraction as Q
from math import gcd, lcm, factorial
from pathlib import Path
import hashlib
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
MD = HERE / 'cdt_odd_period_trigger_20261005.md'
OUT = HERE / 'cdt_odd_period_trigger_20261005_verify.json'
checks = []

def check(name, condition, data=None):
    if not condition:
        raise AssertionError(name)
    checks.append({'name': name, 'passed': True, 'data': data})

D = (1, 2, 3, 4, 6, 12)
U = (4, -2288, 46332, -146432, 185328, -82944)
V = dict(zip(D, U))
check('F8 constant term vanishes', sum(U) == 0)
check('F8 Fricke anti weighted pairs', all(Q(V[d], d**4) == -Q(V[12//d], (12//d)**4) for d in D))
check('F8 primitive Fourier common integer factor', gcd(*U) == 4)
P = {s: sum(Q(u, d**s) for d,u in zip(D,U)) for s in range(9)}
expected = {0:Q(0), 1:Q(1672), 2:Q(0), 3:Q(-44), 4:Q(0), 5:Q(11,3), 6:Q(0), 7:Q(-209,216), 8:Q(0)}
for s in range(9):
    check(f'P({s}) exact', P[s] == expected[s], str(P[s]))
theta = P[7] * Q(-1,2)
check('Theta7 rational factor', theta == Q(209,432), str(theta))
# zeta'(-6) = -720/[2*(2*pi)^6] zeta(7); normalize pi^(-6) away.
L1_factor = P[1] * Q(-factorial(6), 2*2**6)
check('L1 regularized zero-times-pole residue', L1_factor == -9405, str(L1_factor))
highest_poly = L1_factor * Q(-2**6, factorial(6))
check('highest polynomial term equals 12^3 Theta', highest_poly == 12**3*theta, str(highest_poly))
cusp_expected = (Q(0), Q(-476,81), Q(6273,64), Q(-2788,9), Q(476), Q(0))
cusps = []
for c,expected_c in zip(D,cusp_expected):
    val = sum(Q(gcd(c,d),d)**8*u for d,u in zip(D,U))/480
    check(f'cusp c={c} constant', val == expected_c, str(val))
    cusps.append({'c':c,'constant':str(val)})
check('paired cusps vanish but form is not cuspidal', cusps[0]['constant']=='0' and cusps[-1]['constant']=='0' and any(v!=0 for v in cusp_expected))

tau,A,f,T,a,b = sp.symbols('tau A f T a b')
A_W = -12**3*tau**6*A
f_W = T-(f-T)/(12**3*tau**6)
B=A*f
B_W=sp.expand(A_W*f_W)
check('B exact Fricke difference', sp.simplify(B_W-(B-T*(1+12**3*tau**6)*A))==0)
check('H exact Fricke invariance', sp.simplify(A_W*(f_W-T)-A*(f-T))==0)
check('relation is exact branch kernel', sp.simplify((a*A_W+b*B_W)-(a*A+b*B)+(a+b*T)*(1+12**3*tau**6)*A)==0)
w=sp.symbols('w')
tau0=sp.I/sp.sqrt(12)
tau_w=tau0*(1+w)/(1-w)
W_tau=-1/(12*tau_w)
check('local W coordinate changes sign', sp.simplify((W_tau-tau0)/(W_tau+tau0)+w)==0)

N=30
def sigma(k,n):
    return sum(d**k for d in range(1,n+1) if n%d==0)
an=[0]+[sum(u*sigma(7,n//d) for d,u in zip(D,U) if n%d==0) for n in range(1,N+1)]
An=[-1727]+[-504*sigma(5,n)+(1728*504*sigma(5,n//12) if n%12==0 else 0) for n in range(1,N+1)]
fn=[Q(0)]+[Q(an[n],n**7) for n in range(1,N+1)]
bn=[sum(Q(An[n-j])*fn[j] for j in range(1,n+1)) for n in range(N+1)]
L=lcm(*range(1,N+1))
check('all f Fourier denominators cleared including 2 and 3', all((v*L**7).denominator==1 for v in fn))
check('all B Fourier denominators cleared including 2 and 3', all((v*L**7).denominator==1 for v in bn))
df=lcm(*(v.denominator for v in fn))
df_formula=lcm(*(n**7//gcd(n**7,an[n]) for n in range(1,N+1)))
db=lcm(*(v.denominator for v in bn))
contents=gcd(L**7,*[int(v*L**7) for v in bn])
check('f exact complete content formula', df==df_formula, str(df))
check('B exact complete content formula', db==L**7//contents, {'denominator':str(db),'content':str(contents)})

def vp(n,p):
    if n==0:
        return None
    r=0
    while n%p==0:
        n//=p
        r+=1
    return r
def vq(x,p):
    return vp(x.numerator,p)-vp(x.denominator,p)
def modq(x,p):
    return (x.numerator*pow(x.denominator,-1,p))%p
for p in (5,11,13,17,19):
    check(f'fixed prime {p} packet coefficient', vq(bn[p+1],p)==-7 and modq(bn[p+1]*p**7,p)==(-2016)%p, {'valuation':vq(bn[p+1],p),'scaled_residue':modq(bn[p+1]*p**7,p)})
check('fixed primepower 25 unit Fourier numerator', an[25]%5==4 and vq(bn[25],5)==-14)
# One fixed integer unit coordinate q=x+x^2; the proof applies to all such coordinates.
def mul(u,v,n):
    out=[Q(0)]*(n+1)
    for i,a in enumerate(u):
        for j,b in enumerate(v):
            if i+j<=n: out[i+j]+=a*b
    return out
coord=[Q(0),Q(1),Q(1)]+[Q(0)]*(N-2)
power=[Q(1)]+[Q(0)]*N
pulled=[Q(0)]*(N+1)
for j in range(N+1):
    for k in range(N+1): pulled[k]+=bn[j]*power[k]
    power=mul(power,coord,N)
for p in (5,11,13,17,19):
    check(f'fixed integer-unit coordinate prime {p}', vq(pulled[p+1],p)==-7)

result={'status':'passed','scope':'Fixed exact identities and finite Fourier certificates; no numerical zeta(7), no parameter scan, no irrationality claim.',
        'check_count':len(checks),'checks':checks,'F8_divisors':D,'F8_E8_numerators':U,'Theta7_factor':str(theta),'cusps':cusps,
        'finite_prefix_N':N,'f_coefficients':[str(v) for v in fn],'A6_coefficients':An,'B_coefficients':[str(v) for v in bn],
        'report_sha256':hashlib.sha256(MD.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'check_count':result['check_count'],'report_sha256':result['report_sha256'],'script_sha256':result['script_sha256']},ensure_ascii=False))
