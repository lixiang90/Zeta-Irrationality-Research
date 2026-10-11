"""Fixed exact checks for the uniform endpoint nonzero bridge.
All-scale assertions are proved in the accompanying report; no scan or
numerical evaluation of zeta values or Catalan's constant is performed.
"""
from fractions import Fraction as F
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json

def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def vp(a,p):
    assert a
    out=0
    while a%p==0:
        out+=1;a//=p
    return out

def vp_frac(a,p):
    return vp(a.numerator,p)-vp(a.denominator,p)

def mod_frac(a,p):
    assert a.denominator%p
    return a.numerator*pow(a.denominator,-1,p)%p

def div_data(n,q):
    N=n*q
    A=[comb(N,r)*comb(n+r,n)**q for r in range(N+1)]
    c=[(-1)**r*a for r,a in enumerate(A)]
    d=[0]*N;d[-1]=c[-1]
    for r in range(N-1,0,-1):d[r-1]=c[r]-d[r]
    B=c[0]-d[0]
    assert B==sum(A)
    assert d[-1]==(-1)**N*A[-1]
    assert all(d[m]==(-1)**(m+1)*sum(A[m+1:]) for m in range(N))
    return N,A,d,B

zeta_cases=[]
for q,n,k,p in [(2,3,3,5),(3,4,5,11),(7,6,7,41)]:
    assert prime(p) and p==q*n-1 and p>2*q
    C=q**q+(q+1)**q
    e=F(2**(k-1)-1,2**(k-1))
    assert C%p and e.numerator%p
    N,A,d,B=div_data(n,q)
    cp=C*pow(q**q,-1,p)%p
    assert [r for r,a in enumerate(A) if a%p]==[0,1,p,p+1]
    assert B%p==2*cp%p!=0
    assert d[p-1]%p==(-cp)%p
    rational=sum((F(d[m],(m+1)**k) for m in range(N)),F())
    assert vp_frac(rational,p)==-k
    alpha=-rational/(e*B)
    assert vp_frac(alpha,p)==-k
    residue=mod_frac(p**k*alpha,p)
    assert residue==mod_frac(F(2**(k-2),2**(k-1)-1),p)
    M,s=rational.denominator,rational.numerator
    h=gcd(e.numerator*M*B,e.denominator*s)
    assert h%p
    zeta_cases.append({'q':q,'n':n,'k':k,'p':p,'vp_S':-k,
                       'vp_B':0,'vp_alpha':-k,'p_k_alpha_mod_p':residue,
                       'primitive_pair_vp':[k,0]})

catalan_cases=[]
for q,n,p in [(2,2,7),(3,2,11),(7,3,41)]:
    assert prime(p) and p==2*q*n-1 and q>=2 and n>=2
    N,A,d,B=div_data(n,q)
    assert N+n<p
    assert d[-1]%p
    rational=sum((F(d[m],(2*m+1)**2) for m in range(N)),F())
    assert vp_frac(rational,p)==-2
    alpha=-rational/B
    vb=vp(B,p)
    assert vp_frac(alpha,p)==-2-vb
    M,s=rational.denominator,rational.numerator
    h=gcd(M*B,s)
    assert h%p
    assert vp(M*B//h,p)==2+vb and vp(s//h,p)==0
    catalan_cases.append({'q':q,'n':n,'p':p,'vp_S_G':-2,
                          'vp_B':vb,'vp_alpha':-2-vb,
                          'd_top_mod_p':d[-1]%p,
                          'primitive_pair_vp':[2+vb,0]})

out=Path(__file__).with_suffix('.json')
result={'status':'passed','scope':'six preselected exact cases; no numerical periods or scans',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'zeta_cases':zeta_cases,'catalan_cases':catalan_cases,
        'not_asserted':['all n nonzero','effective exceptional threshold',
                        'uniform threshold in q or k','negative primitive exponent',
                        'irrationality of any new constant']}
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'passed','zeta_cases':3,'catalan_cases':3}))
