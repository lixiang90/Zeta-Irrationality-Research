"""NEW exact rational-image calculation, no imports of any research producer.

Uses Abramov's denominator algorithm via SymPy rsolve_ratio on one fixed
operator. No scans of degrees, n, research parameters or primes.
"""
from pathlib import Path
import hashlib
import json
import sympy as s
from sympy.solvers.recurr import rsolve_ratio

HERE = Path(__file__).resolve().parent
n = s.Symbol('n', integer=True)
d = s.Symbol('d')
Q = 8*n**4+16*n**3+20*n**2+12*n+3
P = 48*n**3+80*n**2+40*n+5
# y_n=h_n R(n), h_(n+1)/h_n=256*n^4/(n+3/2)^4.
clearing = (n+s.Rational(3,2))**4*(n-1)**4
cplus = 256*(n+1)**5*n**4*(n-1)**4
czero = -32*(2*n+1)*Q*clearing
cminus = 256*n**5*(n+s.Rational(1,2))**4*(n+s.Rational(3,2))**4
forcing = -384*n**2*P*clearing
coeff = [s.expand(p.subs(n,n+1)) for p in (cminus,czero,cplus)]
rhs = s.expand(forcing.subs(n,n+1))
print('Calling one fixed Abramov rational solver...', flush=True)
answer = rsolve_ratio(coeff,rhs,n)
print('Abramov answer:', answer, flush=True)
checks=[]
def check(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value:
        raise AssertionError(name)
check('h-forward-ratio denominator clearing',s.cancel(cplus/clearing-256*(n+1)**5*n**4/(n+s.Rational(3,2))**4)==0)
check('h-backward-ratio denominator clearing',s.cancel(cminus/clearing-256*n**5*(n+s.Rational(1,2))**4/(n-1)**4)==0)
check('zero-coefficient clearing',s.cancel(czero/clearing+32*(2*n+1)*Q)==0)
check('forcing clearing',s.cancel(forcing/clearing+384*n**2*P)==0)
check('fixed Abramov answer is none',answer is None)
# Exact proof inputs: no solution degree scans or values of n are sampled.
check('forward coefficient complete root factorization',s.factor(cplus)==256*n**4*(n-1)**4*(n+1)**5)
check('backward coefficient complete root factorization',s.expand(cminus-256*n**5*(n+s.Rational(1,2))**4*(n+s.Rational(3,2))**4)==0)
check('local n=1 c nonzero',cminus.subs(n,1)!=0)
check('local n=-3/2 a nonzero',cplus.subs(n,-s.Rational(3,2))!=0)
check('n=1 remaining coefficient divisibility4',all(s.rem(pol,(n-1)**4,n)==0 for pol in (cplus,czero,forcing)))
check('n=-3/2 remaining coefficient divisibility4',all(s.rem(pol,(n+s.Rational(3,2))**4,n)==0 for pol in (czero,cminus,forcing)))
ap=s.Poly(cplus,n);bp=s.Poly(czero,n);cp=s.Poly(cminus,n)
top0=ap.nth(13)+bp.nth(13)+cp.nth(13)
top1=ap.nth(12)+bp.nth(12)+cp.nth(12)+d*(ap.nth(13)-cp.nth(13))
indicial=(ap.nth(11)+bp.nth(11)+cp.nth(11)
          +d*(ap.nth(12)-cp.nth(12))
          +d*(d-1)/2*(ap.nth(13)+cp.nth(13)))
check('infinity leading13 cancellation',s.expand(top0)==0)
check('infinity leading12 cancellation',s.expand(top1)==0)
check('all-degree indicial exact',s.expand(indicial-256*(d-3)*(d-5))==0)
check('forcing degree13',s.Poly(forcing,n).degree()==13)
check('forcing nonzero',forcing!=0)
check('forced local factors coprime',s.gcd(n**4,(n+s.Rational(1,2))**4,n)==1)
if answer is not None:
    residual=sum(coeff[i]*answer.subs(n,n+i) for i in range(3))-rhs
    check('returned-rational-particular-exact',s.cancel(residual)==0)
pins={}
for suffix in ['.md','_verify.py','_verify.json']:
    path=HERE/('cdt_odd_classical_derivative_projection_20261006'+suffix)
    pins[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
report={'execution_record':'Second execution of this NEW fixed producer. First exact solver call returned None and four clearing checks passed, then file-pin path .verify.py caused FileNotFoundError before JSON. Corrected only input-pin filename convention and added independent full rational-obstruction proof identities. No old or peer producer imports or scans.',
        'solver':'SymPy rsolve_ratio (Abramov universal denominator algorithm)',
        'answer':str(answer),'checks':checks,'passed':len(checks),'pins':pins,
        'indicial':str(s.factor(indicial)),
        'forced_local_factor':'n^4*(n+1/2)^4',
        'pole_endpoints':{'leftmost':['0','1','2'],'rightmost':['-1','-3/2','-5/2']},
        'scope':'Exact proof inputs for no rational multiplier of the specified forcing term. Whole-pole orbit argument and all-hypergeometric reduction are in the new Markdown; no assertion about nested sums or arbitrary Dfinite particular solutions.'}
HERE.joinpath('cdt_odd_classical_zeta7_forcing_20261006_verify.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'answer':str(answer),'passed':len(checks)}),flush=True)
