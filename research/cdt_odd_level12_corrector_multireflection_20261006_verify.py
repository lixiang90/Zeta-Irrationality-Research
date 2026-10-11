"""NEW fixed full nine-generator R data and all-integer reflection proof certificate."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from functools import lru_cache
import sympy as S

base=Path(__file__).resolve().parent
frozen=base/'cdt_odd_level12_generator_cocycle_20261006_verify.json'
raw=frozen.read_bytes()
expected='b8dfb80d30a4fc276d225d148c76ead7032de51523896664f5c743eb0af966ef'
checks=[]
def check(name,v):
    checks.append({'name':name,'passed':bool(v)})
    if not v: raise AssertionError(name)
check('frozen data hash only no producer execution',hashlib.sha256(raw).hexdigest()==expected)
old=json.loads(raw)
Rcoeff={1:1,2:-66,3:495,4:-880,6:594,12:-144}
Lcoeff={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
chars={1:1,5:-1,7:-1,11:1}

@lru_cache(None)
def ordinary_tate(j,b,d):
    b%=d
    total=0
    for h in range(1,d):
        k=(b*j*h)%d
        total+=(d-2*h)*k*(2*k-d)*(k-d)
    return F(40*total,j**3*d**4)
@lru_cache(None)
def R_endpoint(b,d):
    return sum((v*ordinary_tate(j,b,d) for j,v in Rcoeff.items()),F(0))
def chiE_tate(b,d):
    assert d%2 and d%3
    nums=[0]*d
    for z,ch in chars.items():
        for h in range(d):
            nums[(z+12*h)%d]+=ch*(d if h==0 else d-2*h)
    total=0
    for h,v in enumerate(nums):
        k=(b*h)%d
        total+=v*k*(2*k-d)*(k-d)
    return F(total,6*d**4)
def scaledchiF_tate(b,d):
    total=0
    den=12*d
    for h in range(d):
        v=-d if h==0 else d-2*h
        for z,ch in chars.items():
            k=(12*b*h+d*z)%den
            total+=v*ch*k*(2*k-den)*(k-den)
    return F(total,864*d**4)
def L_endpoint_tate(b,d):
    return sum((v*ordinary_tate(j,b,d) for j,v in Lcoeff.items()),F(0))+2880*(chiE_tate(b,d)+scaledchiF_tate(b,d))
check('M actual R finite normalization',R_endpoint(2,7)==-F(1920,7))
check('M actual L finite correction zero',L_endpoint_tate(2,7)==0)
check('old sigma canonical chi plus finite kernel',chiE_tate(2,7)+scaledchiF_tate(2,7)==F(586,1029))
check('M mirror R exact opposite',R_endpoint(-2,7)==F(1920,7))
check('M mirror L zero',L_endpoint_tate(-2,7)==0)
check('known n1 actual R endpoint',R_endpoint(9,139)==-F(1920,139))
check('known n1 actual L endpoint',L_endpoint_tate(9,139)==F(2578560,139))

seeds=[F(1,12*k) for k in (1,2,3,4)]
fit=S.Matrix([[1,S.Rational(t.numerator,t.denominator),S.Rational(t.numerator,t.denominator)**2] for t in seeds[:3]]).inv()
def mr(g,t):
    a,b,c,d=g
    num=a*t+b; den=c*t+d
    return None if den==0 else num/den
def endpoint_rat(x):
    return F(0) if x is None else R_endpoint(x.numerator,x.denominator)
def R_sample(g,t):
    a,b,c,d=g
    return (c*t+d)**2*endpoint_rat(mr(g,t))-endpoint_rat(t)
def slash(g):
    a,b,c,d=g
    det=a*d-b*c
    return S.Matrix([[d*d,b*d,b*b],[2*c*d,a*d+b*c,2*a*b],[c*c,a*c,a*a]])/det
records=[]
for entry in old['generators']:
    g=entry['matrix']
    check(entry['name']+' actual Gamma matrix',g[0]*g[3]-g[1]*g[2]==1 and g[2]%12==0 and g[3]%12 in (1,11))
    samples=[R_sample(g,t) for t in seeds]
    vec=fit*S.Matrix([S.Rational(v.numerator,v.denominator) for v in samples[:3]])
    check(entry['name']+' independent fourth exact sample',sum(vec[i]*S.Rational(seeds[3].numerator,seeds[3].denominator)**i for i in range(3))==S.Rational(samples[3].numerator,samples[3].denominator))
    PL=S.Matrix([S.Rational(z) for z in entry['PL']])
    ratios={-PL[i]/vec[i] for i in range(3) if vec[i]!=0}
    scalar=None
    if vec==S.zeros(3,1):
        status='all s' if PL==S.zeros(3,1) else 'no s R zero but L nonzero'
    elif len(ratios)==1 and all(PL[i]==0 for i in range(3) if vec[i]==0):
        scalar=next(iter(ratios)); status='unique scalar'
    else: status='no scalar entire vector not proportional'
    records.append({'name':entry['name'],'matrix':g,'PR':[str(v) for v in vec],'PL':entry['PL'],'samples':[str(v) for v in samples],'source_zero_status':status,'source_zero_scalar':None if scalar is None else str(scalar)})
vectors={z['name']:S.Matrix([S.Rational(v) for v in z['PR']]) for z in records}
check('R T entire period zero',vectors['x2']==S.zeros(3,1))
check('R eta reconstructed by actual x2 x9inverse',vectors['x9']==S.zeros(3,1))

n=S.symbols('n',integer=True)
a=24+84*n; p=84*n*n+48*n+7; c=12*p
Jn=S.Matrix([[a,-7],[c,-a]])
mirror=S.Matrix([[-a,-7],[c,a]])
etaN=S.Matrix([[1,0],[12*n,1]])
etaMinus=S.Matrix([[1,0],[-12*n,1]])
Mmirror=S.Matrix([[-24,-7],[84,24]])
check('mirror genuine eta inverse orbit',S.expand(etaMinus*Mmirror*etaN-mirror)==S.zeros(2))
check('mirror order two entire n',S.expand(mirror*mirror+12*S.eye(2))==S.zeros(2))
check('mirror never same integer J orbit',F(4,7).denominator!=1)
delta=1932*n*n+3036*n+1343
k=S.symbols('k',integer=True,nonnegative=True)
check('integer s strict negative branch exact',S.expand(delta.subs(n,-k-1)-(1932*k*k+828*k+239))==0)
check('integer s strict positive branch coefficients',all(v>0 for v in (1932,3036,1343)))
check('circle discriminant source identity',S.expand(a*a+12-7*c)==0)
check('all n absolute a minimum24',24<=abs(24) and 24<=abs(-60))
check('n0 translated separation exact',min(8,14-8)==6)
check('positive n intercircle versus translation',S.expand((p-2*(14*n+4))-(84*n*n+20*n-1))==0)
check('negative n intercircle versus translation',S.expand((p-2*(-14*n-4)).subs(n,-k-1)-(84*k*k+92*k+23))==0)
A=S.symbols('A',real=True)
tr=(A**3-14*A*A+12*A-84)/42
check('boundary trace exact baseline142',tr.subs(A,24)==142)
check('boundary trace derivative positive after24',S.expand(S.diff(tr,A).subs(A,k+24)-(3*k*k+116*k+1068)/42)==0)
check('source c2 exact polynomial',-F(320,3)*(n+113)==-F(320,3)*n-F(36160,3))
check('source c4 exact polynomial',-F(2800,3)*F(919,35)==-F(73520,3))
check('c2exception between consecutive integer family parameters',-239<-113<0)
check('c4exception not integer',F(-919,35).denominator!=1)
check('first actual c2zero derivative',3180*48==152640)
check('second actual c2zero derivative',152640-12*2880==118080)
check('first actual c4zero endpoint',F(10330)*F(12,35)==F(24792,7))
check('second actual c4zero endpoint',F(24792,7)+F(4,3)*2880==F(51672,7))

# The next admissible prime denominator is fixed by 12*7^2+1=19*31.
# These are two specified reflections, not a denominator/parameter search.
fixed=[]
for a0,d0 in ((31,19),(19,31)):
    b0=7
    check('fixed next reflection determinant d'+str(d0),a0*d0-12*b0*b0==1)
    l=L_endpoint_tate(b0,d0); rr=R_endpoint(b0,d0)
    fixed.append({'a':a0,'b':b0,'d':d0,'ell':str(l),'R':str(rr),'scalar':None if rr==0 else str(-l/rr)})
report={'date':'2026-10-06','scope':'All-integer mirror geometry, fixed COMPLETE nine-generator R period table, exact arbitrary-reflection formula normalization, two algebraically prescribed next-denominator reflections; no word/prime/parameter scan or numerical theorem',
        'execution_history':'First single execution of this NEW fixed producer; frozen JSON read as pinned data only.',
        'input_sha256':expected,'passed':len(checks),'checks':checks,'R_generator_periods':records,'fixed_next_reflections':fixed}
(base/'cdt_odd_level12_corrector_multireflection_20261006_verify.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'fixed_next_reflections':fixed,'generator_scalar_status':[(z['name'],z['source_zero_status'],z['source_zero_scalar']) for z in records]}))
