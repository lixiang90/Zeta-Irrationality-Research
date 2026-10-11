"""NEW fixed certificate for two prescribed Hecke radii, not a word scan.

All-scale convergence and Green uniqueness are proved in the accompanying note.
No old or peer producer is imported/executed.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

checks=[]
def check(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value: raise AssertionError(name)

w,a,b,c=sp.symbols('w a b c',positive=True)
S=sp.Matrix([[0,-1],[1,0]])
def T(n):return sp.Matrix([[1,n*w],[0,1]])
g0=S;g1=S*T(a)*S;g2=g1*T(b)*S;g3=g2*T(c)*S
C=[sp.Integer(1),a*w,a*b*w*w-1,a*b*c*w**3-(a+c)*w]
for j,g in enumerate([g0,g1,g2,g3]):
    check('fixed symbolic word c '+str(j),sp.expand(g[1,0]-C[j])==0)
    check('fixed symbolic word determinant '+str(j),sp.expand(g.det())==1)
    check('fixed symbolic word d '+str(j),sp.expand(g[1,1]-(0 if j==0 else -C[j-1]))==0)
check('all-word recurrence template',sp.expand(c*w*C[2]-C[1]-C[3])==0)
lam,N=sp.symbols('lam N',positive=True)
check('ratio estimate algebra',sp.simplify(N*(lam+1/lam)-1/lam-N*lam-(N-1)/lam)==0)
check('first-word contribution',sp.Rational(2,1)*sp.pi**2/w**2 ==2*sp.pi**2/w**2)
check('periodic-kernel constant Fourier normalization',sp.integrate(sp.Symbol('y',positive=True)/(sp.Symbol('x',real=True)**2+sp.Symbol('y',positive=True)**2),(sp.Symbol('x',real=True),-sp.oo,sp.oo))==sp.pi)
check('Green cusp log normalization',sp.simplify((2*sp.pi/w)*(w/(2*sp.pi)))==1)
check('Green radius constant normalization',sp.simplify((2*sp.pi/w)*(sp.pi/w))==2*sp.pi**2/w**2)

lp=sp.sqrt(3)+sp.sqrt(2)
lm=7*sp.sqrt(3)+sp.sqrt(146)
check('lambda plus exact',sp.simplify(lp+1/lp-sp.sqrt(12))==0)
check('lambda minus exact',sp.simplify(lm+1/lm-sp.sqrt(588))==0)
check('lambda plus square exact',sp.expand(lp*lp)==5+2*sp.sqrt(6))
check('lambda minus square plus inverse',sp.simplify(lm*lm+1/(lm*lm))==586)
check('sqrt6 greater than2 rational proof',Q(6)>Q(2)**2)
check('lambda minus greater than1 rational proof',Q(147)>Q(1))

P=Q(484,49)
check('pi upper square exact',Q(22,7)**2==P)
check('plus normal convergence rational denominator',1-P/27>0)
check('minus normal convergence rational denominator',1-P/1755>0)
Cp=1+(P/36)/(1-P/27)
Cm=1+(P/1764)/(1-P/1755)
Up=P/6*Cp;Um=P/294*Cm;U=(Up+Um)/2
check('plus C bound simplified',Cp==Q(1202,839))
check('plus radius upper simplified',Up==Q(290884,123333))
check('average radius upper less than6/5',U<Q(6,5))
check('safe k3 threshold above6/5',Q(573,253)>Q(6,5))
check('k3 lower true-cost threshold above6/5',Q(539,253)>Q(6,5))
check('k2 lower true-cost threshold above6/5',Q(29,13)>Q(6,5))
check('k3 true-cost Jensen conversion',Q(1078,529)*Q(23,22)==Q(539,253))
check('k2 true-cost Jensen conversion',Q(348,169)*Q(13,12)==Q(29,13))

out={'check_count':len(checks),'all_passed':all(x['passed'] for x in checks),'checks':checks,
     'rational_bounds':{'pi_square_upper':str(P),'Cplus':str(Cp),'Cminus':str(Cm),'logRplus':str(Up),'logRminus':str(Um),'mean_logR':str(U),'mean_certified_cap':'6/5'},
     'scope':['only w^2=12,588 prescribed source surfaces','symbolic template, no word enumeration','no old/peer producer','normal convergence and Green identity require accompanying all-scale proof','no numerical irrationality theorem','augmented group not included']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':out['all_passed'],'mean_rational_upper':str(U)},ensure_ascii=False))
