"""Fixed exact certificates for second p-adic blocks and primitive root payment."""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, gcd
import hashlib
import json
import sys
import sympy as sp

sys.stdout.reconfigure(encoding='utf-8')
HERE = Path(__file__).resolve().parent
REPORT = HERE/'odd_zeta_log_primitive_20261005.md'
OUT = Path(__file__).with_suffix('.json')

def vp_int(x,p):
    assert x != 0
    x=abs(x); v=0
    while x%p==0:
        x//=p;v+=1
    return v

def vp(x,p):
    x=F(x)
    return vp_int(x.numerator,p)-vp_int(x.denominator,p)

def residue(x,m):
    x=F(x)
    assert gcd(x.denominator,m)==1
    return x.numerator*pow(x.denominator,-1,m)%m

constants=[]
for H in range(1,7):
    w=[sum((F((-1)**j,j**7) for j in range(1,l+1)),F()) for l in range(H+1)]
    kap=sum((comb(H,l)*w[l] for l in range(H+1)),F())
    lam=sum((l*comb(H,l)*w[l] for l in range(H+1)),F())
    rho=lam-F(H,2)*kap
    dif=-F(H,2)*sum((F((-1)**l*comb(H-1,l),(l+1)**7) for l in range(H)),F())
    assert rho==dif and rho<0
    U=-lam;V=kap
    assert kap*U+lam*V==0
    assert U+F(H,2)*V==-rho!=0
    constants.append({'H':H,'kappa':str(kap),'lambda':str(lam),'rho':str(rho),
                      'difference_identity_exact':True,'formal_loss_direction_exact':True})

cases=[]
for n,p in [(6,41),(7,19),(23,37),(27,31)]:
    N=7*n;H,d=divmod(N,p)
    assert sp.isprime(p) and p>7 and n<p<=N and N<p*p and 1<=H<=6
    a=[comb(N,r)*comb(n+r,n)**7 for r in range(N+1)]
    B=sum(a);tail=0;T=[0]*(N+1);S=F()
    for j in range(N,0,-1):
        tail+=a[j];T[j]=tail;S+=F((-1)**j*tail,j**7)
    assert S<0
    Z=p**7*S;alpha=-64*S/(63*B)
    h=gcd(63*S.denominator*B,64*S.numerator)
    q=alpha.denominator
    assert q==63*S.denominator*B//h
    r=vp(B,p);t=vp(Z,p);payment=vp(q,p)
    assert r>=0 and t>=0 and payment==max(0,7+r-t)
    harms=[F()]
    for j in range(1,p):
        harms.append(harms[-1]+F(1,j))
    e=min(d,p-n-1)
    b=[comb(d,s)*comb(n+s,n)**7 for s in range(e+1)]
    C=sum(b)
    A=sum((b[s]*H*(harms[d]-harms[d-s]) for s in range(e+1)),F())
    D=sum((b[s]*(harms[d-s]+7*harms[n+s]-8*harms[s]) for s in range(e+1)),F())
    E=sum((F((-1)**(s-d-1)*factorial(d)*factorial(s-d-1),factorial(s))*comb(n+s,n)**7
           for s in range(d+1,p-n)),F())
    U=A+H*E;V=D-E
    blocks=[]
    for l in range(H+1):
        block=sum(a[l*p:min((l+1)*p,N+1)])
        predicted=comb(H,l)*(C+p*(U+l*V))
        assert residue(block,p*p)==residue(predicted,p*p)
        for s in range(d+1,p-n):
            if l==H:continue
            actual=F(comb(N,l*p+s),p)
            expected=H*comb(H-1,l)*F((-1)**(s-d-1)*factorial(d)*factorial(s-d-1),factorial(s))
            assert residue(actual,p)==residue(expected,p)
        blocks.append({'l':l,'actual_mod_p2':block%(p*p),
                       'predicted_mod_p2':residue(predicted,p*p)})
    kap=F(constants[H-1]['kappa']);lam=F(constants[H-1]['lambda']);rho=F(constants[H-1]['rho'])
    assert residue(kap,p)!=0 and residue(rho,p)!=0
    predicted_B=2**H*(C+p*(U+F(H,2)*V))
    predicted_Z=kap*C+p*(kap*U+lam*V)
    assert residue(B,p*p)==residue(predicted_B,p*p)
    assert residue(Z,p*p)==residue(predicted_Z,p*p)
    assert residue(Z-kap*F(B,2**H),p*p)==residue(p*rho*V,p*p)
    W=sum((F((-1)**j*T[j],j**7) for j in range(1,N+1) if j%p),F())
    top=sum((F((-1)**l*T[l*p],l**7) for l in range(1,H+1)),F())
    assert Z==top+p**7*W
    face=None
    if C%p==0:
        aa=F(C,p)+U+F(H,2)*V
        bb=kap*(F(C,p)+U)+lam*V
        assert residue(F(B,2**H*p),p)==residue(aa,p)
        assert residue(Z/p,p)==residue(bb,p)
        face={'a_mod_p':residue(aa,p),'b_mod_p':residue(bb,p)}
    if n==6:assert r==t==0 and payment==7
    if n==7:assert r==t==2 and payment==7 and face=={'a_mod_p':0,'b_mod_p':0}
    if n in (23,27):assert r==t==1 and payment==7 and face['b_mod_p']!=0
    cases.append({'n':n,'p':p,'H':H,'d':d,'e':e,
                  'C_mod_p':C%p,'U_mod_p':residue(U,p),'V_mod_p':residue(V,p),
                  'B_mod_p2':B%(p*p),'Z_mod_p2':residue(Z,p*p),
                  'v_B':r,'v_Z':t,'v_M':vp(S.denominator,p),
                  'v_complete_gcd':vp(h,p),'primitive_root_denominator_payment':payment,
                  'alpha_numerator':alpha.numerator,'alpha_denominator':q,
                  'first_nonzero_Z_residue':residue(Z/p**t,p),
                  'face':face,'blocks':blocks,'exact_top_plus_regular_part_identity':True})

symbol_L,symbol_K,symbol_C,symbol_D,symbol_x=sp.symbols('L K C D x')
assert sp.expand(symbol_K*symbol_x-symbol_K*symbol_L*symbol_x-symbol_K*(1-symbol_L)*symbol_x)==0
assert sp.cancel((sp.Rational(64,63)*symbol_D/symbol_C)*symbol_x-sp.Rational(64,63)*symbol_D*symbol_x/symbol_C)==0

result={'status':'fixed_exact_primitive_jet_certificates_passed','as_of':'2026-10-05',
        'report_sha256':hashlib.sha256(REPORT.read_bytes()).hexdigest(),
        'constants':constants,'fixed_cases':cases,
        'normalized_difference_symbolic_identity':'K*L^n-K*L^(n+1)=K*(1-L)*L^n',
        'all_scale_claims_from_written_proof':[
            'Primitive root denominator valuation with complete content included',
            'All lower-digit good and borrowed blocks through modulus p squared',
            'Nonzero rho from positive Mellin integral',
            'Seven-layer restoration when vZ is one and vB at least one',
            'Exact deficit and second-zero-domain conditional budgets',
            'Unconditional three-adjacent rational-root denominator height from normalized saddle and rational separation'],
        'not_claimed':[
            'Universal restoration of seven layers',
            'Realization or exclusion of the actual single-loss face at infinitely many primes',
            'Density bound for the second zero domain',
            'Unconditional primitive divergence',
            'Parameter scan or new irrationality theorem']}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'fixed_cases':len(cases)},ensure_ascii=False))
