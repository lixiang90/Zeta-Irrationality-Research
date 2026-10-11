"""NEW first-only actual lambda2 moment-reduction identities, not a prime table.
Only previously considered r=1,2,4; no old or peer mathematics input is read.
No assertion of critical determinant nonzero, infinite units, or margin.
"""
from pathlib import Path
from math import comb, factorial
import json
import traceback
import hashlib

OUT=Path(__file__).with_suffix('.json')
with OUT.open('x',encoding='utf-8') as stream:
    json.dump({'status':'STARTED_FIRST_ONLY','old_peer_inputs':0},stream)

def trim(f,p):
    f=[c%p for c in f]
    while f and f[-1]==0: f.pop()
    return f

def add(f,g,p):
    return trim([(f[i] if i<len(f) else 0)+(g[i] if i<len(g) else 0) for i in range(max(len(f),len(g)))],p)

def scale(f,c,p): return trim([c*x for x in f],p)

def mul(f,g,p):
    if not f or not g: return []
    h=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): h[i+j]=(h[i+j]+a*b)%p
    return trim(h,p)

def power(f,n,p):
    h=[1]
    for _ in range(n): h=mul(h,f,p)
    return h

def shift(f,p):
    h=[0]*len(f)
    for j,c in enumerate(f):
        for i in range(j+1): h[i]=(h[i]+c*comb(j,i))%p
    return trim(h,p)

def evaluate(f,x,p):
    value=0
    for c in reversed(f): value=(value*x+c)%p
    return value

def operator(g,j,a,p):
    if j in (1,5):
        return add(mul(power([a+1,1],j,p),shift(g,p),p),scale(mul(power([-a-1,1],j,p),g,p),-1,p),p)
    if j==-3:
        return add(mul(power([-a,1],3,p),shift(g,p),p),scale(mul(power([a,1],3,p),g,p),-1,p),p)
    raise ValueError(j)

def reduce_even(f,j,a,p):
    offset={1:0,5:4,-3:2}[j]
    remainder=f[:]
    g=[]
    limit=len(f)-1-offset
    for n in reversed(range(0,limit+1,2)):
        b=power([-pow(2,-1,p),1],n,p)
        image=operator(b,j,a,p)
        assert len(image)==n+offset+1
        assert all(image[i]==0 for i in range(1,len(image),2))
        leading=(n+2*j*(a+1) if j>0 else n-6*a)%p
        assert image[-1]==leading!=0
        degree=n+offset
        coefficient=(remainder[degree] if degree<len(remainder) else 0)*pow(leading,-1,p)%p
        remainder=add(remainder,scale(image,-coefficient,p),p)
        g=add(g,scale(b,coefficient,p),p)
    assert len(remainder)<=offset
    assert all(remainder[i]==0 for i in range(1,len(remainder),2))
    assert add(operator(g,j,a,p),remainder,p)==f
    return g,remainder

def one_case(r):
    p=18*r+1
    a=5*r
    S=[]
    for k in range(a+1):
        val=1
        for q in range(a+1,9*r+1): val=val*(k*k-q*q)%p
        S.append(val)
    assert all(S)
    inverse=[pow(v,-1,p) for v in S]
    h=[inverse[k]*pow(inverse[0],-1,p)%p for k in range(a+1)]
    assert h[0]==1
    for k in range(a): assert h[k+1]*(k-a)%p==h[k]*(k+a+1)%p
    mu=[1 if k==0 or k>=r else 2 for k in range(a+1)]
    gamma=[2 if k==0 else (4 if k<r else 5) for k in range(a+1)]
    def G(f): return sum(mu[k]*pow(inverse[k],5,p)*evaluate(f,k,p) for k in range(a+1))%p
    def H(f): return sum(mu[k]*pow(S[k],3,p)*evaluate(f,k,p) for k in range(a+1))%p
    def C(f): return sum(gamma[k]*inverse[k]*evaluate(f,k,p) for k in range(a+1))%p
    A0,A1,B0=G([1]),G([0,0,1]),H([1])
    cross_checks=scalar_checks=QQ_checks=0
    for d in range(4*r-1):
        f=[0]*(2*d)+[1]
        g,rem=reduce_even(f,1,a,p)
        assert rem==[]
        boundary=(-5*factorial(10*r+1)*evaluate(g,a+1,p)-factorial(4*r+1)*factorial(6*r)*evaluate(g,r,p))%p
        assert C(f)==boundary
        cross_checks+=1
    for d in range(2*r-1):
        f=[0]*(2*d)+[1]
        g,rem=reduce_even(f,5,a,p)
        c0=rem[0] if rem else 0
        c1=rem[2] if len(rem)>2 else 0
        boundary=(c0*A0+c1*A1-pow(factorial(10*r+1),5,p)*evaluate(g,a+1,p)
                  +pow(factorial(4*r+1)*factorial(6*r),5,p)*evaluate(g,r,p))%p
        assert G(f)==boundary
        scalar_checks+=1
    for d in range(6*r-1):
        f=[0]*(2*d)+[1]
        g,rem=reduce_even(f,-3,a,p)
        c0=rem[0] if rem else 0
        denom=pow(factorial(4*r)*factorial(6*r-1),3,p)
        boundary=(c0*B0-evaluate(g,r,p)*pow(denom,-1,p))%p
        assert H(f)==boundary
        QQ_checks+=1
    full=sum((1 if k==0 else 2)*pow(S[k],3,p) for k in range(a+1))%p
    dixon=((-1)**(r+1)*factorial(15*r)*pow(pow(factorial(5*r),3,p)*pow(factorial(10*r),3,p),-1,p))%p
    assert full==dixon!=0
    return {'r':r,'p':p,'actual_initial_G_constant':A0,'actual_initial_G_x2':A1,'actual_initial_H_constant':B0,
            'cross_boundary_identities':cross_checks,'G_two_seed_reductions':scalar_checks,'H_one_seed_reductions':QQ_checks,
            'full_QQ_Dixon_unit':full,'critical_determinant_nonzero_asserted':False}

try:
    cases=[one_case(r) for r in (1,2,4)]
    result={'status':'PASS','execution_count':1,'cases':cases,'moment_identity_count':sum(c['cross_boundary_identities']+c['G_two_seed_reductions']+c['H_one_seed_reductions'] for c in cases),
            'old_peer_execute_import_rerun_count':0,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Fixed original lambda2 moments and true middle boundaries on old r1,2,4 only; no prime-table extension.',
            'not_proved':['Infinite M5 units','Infinite rational-target nonzero','Global integer model and norm improvement','Strict margin','New special-value theorem']}
except BaseException as exc:
    result={'status':'FAIL_PRESERVED_FIRST_ONLY','execution_count':1,'exception':repr(exc),'traceback':traceback.format_exc(),'old_peer_execute_import_rerun_count':0}
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    raise
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
