"""Fixed exact certificates for the q=7 log-moment nonzero bridge.

No numerical evaluation of zeta(7), no parameter scan.  The two endpoint
signs use an explicitly proved positive Euler expansion of eta(7).
The arithmetic identities are proved for every prime in the report;
three predetermined scales check the implementation only.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, isqrt
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

sys.stdout.reconfigure(encoding='utf-8')
OUT = Path(__file__).with_suffix('.json')
u, L = S.symbols('u L')

def frac(x):
    return f'{x.numerator}/{x.denominator}'

def prime_exact(p):
    return p >= 2 and all(p % a for a in range(2, isqrt(p)+1))

def data(n, q=7, k=7):
    N = n*q
    A = [comb(N,r)*comb(n+r,n)**q for r in range(N+1)]
    c = [(-1)**r*a for r,a in enumerate(A)]
    d = [0]*N
    d[-1] = c[-1]
    for r in range(N-1,0,-1):
        d[r-1] = c[r]-d[r]
    B = c[0]-d[0]
    assert B == sum(A)
    assert all(d[m] == (-1)**(m+1)*sum(A[m+1:]) for m in range(N))
    rational = sum((F(d[m],(m+1)**k) for m in range(N)),F())
    return A,c,d,B,rational

def vp(a,p):
    if a == 0:
        return None
    out=0
    while a % p == 0:
        a//=p; out+=1
    return out

def rational_mod(x,p):
    assert x.denominator % p
    return x.numerator*pow(x.denominator,-1,p)%p

def interval_mul(x,y):
    v=[a*b for a in x for b in y]
    return min(v),max(v)

def interval_polynomial(coeff,x):
    v=(F(),F())
    for c in coeff:
        lo,hi=interval_mul(v,x)
        v=(lo+c,hi+c)
    return v

def interval_record(v):
    return {'lower':frac(v[0]),'upper':frac(v[1]),
            'sign':1 if v[0]>0 else -1 if v[1]<0 else 0}

# Euler/Rodrigues identity, two fixed scales; the general proof is algebraic.
euler_cases=[]
for n in [1,2]:
    q=7;N=n*q
    coeff=[(-1)**r*comb(N,r) for r in range(N+1)]
    for j in range(1,n+1):
        for _ in range(q):
            coeff=[a*(r+j) for r,a in enumerate(coeff)]
    norm=factorial(n)**q
    assert all(a % norm==0 for a in coeff)
    coeff=[a//norm for a in coeff]
    _,c,_,_,_=data(n)
    assert coeff==c
    euler_cases.append({'n':n,'q':q,'degree':N,'identity':'passed'})

# Exact log(2) interval from the atanh series, with a geometric tail bound.
Mlog=32
log_lo=2*sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(Mlog)),F())
log_hi=log_lo+F(9,4*(2*Mlog+1)*3**(2*Mlog+1))
kernel=L**6/(factorial(6)*(1+u))
for _ in range(7):
    kernel=S.cancel(-u*S.diff(kernel,u)+S.diff(kernel,L))
kernel_cases=[]
for power,want in [(1,1),(8,-1)]:
    poly=S.Poly(kernel.subs(u,S.Rational(1,2**power)),L)
    coeff=[F(int(a.p),int(a.q)) for a in poly.all_coeffs()]
    bound=interval_polynomial(coeff,(power*log_lo,power*log_hi))
    assert interval_record(bound)['sign']==want
    kernel_cases.append({'u':f'1/{2**power}','L':f'{power}*log(2)',
                         'polynomial_coeff_desc':[frac(a) for a in coeff],
                         'interval':interval_record(bound)})

# eta(7)=sum_{j>=0}2^(-j-1)b_j with 0<b_j<=1.
# b_j=sum_{r=0}^j(-1)^r binom(j,r)/(r+1)^7, so a K-term
# rational lower bound has error strictly less than 2^-K.
Keta=384
diffs=[F(1,(j+1)**7) for j in range(Keta)]
eta_lo=F()
for j in range(Keta):
    assert F()<diffs[0]<=1
    eta_lo+=diffs[0]/2**(j+1)
    diffs=[diffs[r]-diffs[r+1] for r in range(len(diffs)-1)]
eta_hi=eta_lo+F(1,2**Keta)
endpoint_cases=[]
for n,want in [(1,-1),(8,1)]:
    _,_,_,B,rational=data(n)
    interval=(B*eta_lo+rational,B*eta_hi+rational)
    assert interval_record(interval)['sign']==want
    endpoint_cases.append({'n':n,'q':7,'k':7,'B':str(B),
                           'S':frac(rational),'interval':interval_record(interval)})

# The only fixed constant in the Lucas computation; trial division is exact.
C=7**7+8**7
assert C==3*5*194713 and prime_exact(194713)
assert all(a%7!=6 for a in [3,5,194713])
arith_cases=[]
for n,p in [(2,13),(6,41),(12,83)]:
    assert p==7*n-1 and prime_exact(p)
    A,c,d,B,rational=data(n)
    surviving=[r for r,a in enumerate(A) if a%p]
    assert surviving==[0,1,p,p+1]
    cp=C*pow(7**7,-1,p)%p
    assert B%p==2*cp%p!=0
    assert d[p-1]%p==(-cp)%p
    assert vp(rational.numerator,p)==0
    assert vp(rational.denominator,p)==7
    alpha=-F(64,63)*rational/B
    assert vp(alpha.numerator,p)-vp(alpha.denominator,p)==-7
    assert rational_mod(p**7*alpha,p)==32*pow(63,-1,p)%p
    # Actual reduced (63MB,64s) integer pair: no p-content.
    M=rational.denominator;s=rational.numerator
    h=gcd(63*M*B,64*s)
    assert h%p and vp(63*M*B//h,p)==7 and vp(64*s//h,p)==0
    arith_cases.append({'n':n,'p':p,'B_mod_p':B%p,
                       'd_pminus1_mod_p':d[p-1]%p,
                       'vp_S':-7,'vp_alpha':-7,
                       'p7alpha_mod_p':rational_mod(p**7*alpha,p),
                       'reduced_integer_pair_vp':[7,0],
                       'surviving_A_indices':surviving})

result={'status':'passed','scope':'fixed exact checks; all-scale claims use the report proofs',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'Euler_identity_cases':euler_cases,
        'log2_interval':interval_record((log_lo,log_hi)),
        'adjoint_kernel_sign_cases':kernel_cases,
        'eta7_bound':{'K':Keta,'tail_upper':'1/'+str(2**Keta)},
        'endpoint_sign_cases':endpoint_cases,
        'constant_C':str(C),'C_factorization':[3,5,194713],
        'prime_progression_cases':arith_cases,
        'not_asserted':['all n nonzero','fixed sign','negative normalized exponent',
                        'zeta(7) irrationality','new Lean formalization']}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','output':str(OUT),'endpoint_signs':[-1,1],
                  'arithmetic_scales':[2,6,12]},ensure_ascii=False))
