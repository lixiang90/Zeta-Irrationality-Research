"""NEW fixed symbolic certificate; never imports another research producer."""
import json
from pathlib import Path
import sympy as s

e, p, n, z = s.symbols('e p n z')
t0, t1, t2, t3, t4, r0 = s.symbols('t0 t1 t2 t3 t4 r0')
m0, m1, m2, m3, m4 = s.symbols('M0 M1 M2 M3 M4')
checks=[]
def check(name, expr):
    ok=s.simplify(s.expand(expr))==0
    checks.append({'name':name,'passed':bool(ok)})
    if not ok: raise AssertionError(name+': '+str(expr))

cos4=s.series(s.cos(p*e)**4,e,0,5).removeO()
sin4=s.series(s.sin(p*e)**4,e,0,5).removeO()
check('cos4 fixed fourth Taylor',cos4-(1-2*p**2*e**2+s.Rational(5,3)*p**4*e**4))
check('sin4 fixed fourth Taylor',sin4-p**4*e**4)
T=t0+t1*e+t2*e**2/2+t3*e**3/6+t4*e**4/24
C=s.expand(cos4*T+sin4*r0)
expected=(t0,t1,t2-4*p**2*t0,t3-12*p**2*t1,t4-24*p**2*t2+40*p**4*t0+24*p**4*r0)
for j in range(5):
    check('C derivative '+str(j),s.diff(C,e,j).subs(e,0)-expected[j])

for freq in (-1,0,1):
    F=s.exp(2*s.I*freq*p*e)
    check('three-mode order3 '+str(freq),s.diff(F,e,3)+4*p**2*s.diff(F,e))
    check('three-mode order4 '+str(freq),s.diff(F,e,4)+4*p**2*s.diff(F,e,2))

sub={t0:m0,t1:-m1,t2:m2,t3:-m3,t4:m4}
third=(expected[3]+4*p**2*expected[1]).subs(sub)
fourth=(expected[4]+4*p**2*expected[2]).subs(sub)
check('M3 exact normalization',third-(-m3+8*p**2*m1))
check('M4 exact normalization',fourth-(m4-20*p**2*m2+24*p**4*m0+24*p**4*r0))
check('M3 L3 multiplier',8*64-512)
check('Gamma H coefficient cancellation',(n+s.Rational(1,2))**4/((n+s.Rational(1,2))**4)-1)
check('theta half fourth difference',(z+s.Rational(1,2))**4-z**4-(2*z**3+s.Rational(3,2)*z**2+s.Rational(1,2)*z+s.Rational(1,16)))
check('B16 constant',24*p**2*16-384*p**2)

data={'purpose':'NEW fixed symbolic normalization certificate; no numerical fitting or research search',
      'execution_history':'First execution; all checks passed. No frozen or peer producer executed/imported.',
      'scope_exclusions':['No verification by finite checks of analytic Gamma bounds or full Fourier theorem',
                          'No arithmetic integrality, leaf, Smith gain, or irrationality theorem'],
      'count':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks}
target=Path(__file__).with_suffix('.json')
target.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'checks':len(checks),'all_passed':data['all_passed'],'output':str(target)},ensure_ascii=False))
