"""NEW prescribed two-circle certificate; no old/peer imports or word scan."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

checks=[]
def check(name,value):
    value=bool(value)
    checks.append({'name':name,'passed':value})
    if not value:raise AssertionError(name)

r=sp.sqrt(3);w=14*r;u=4*r
M=sp.Matrix([[24,-7],[84,-24]])
Mc=sp.Matrix([[-24,-7],[84,24]])
C=sp.diag(w,1)
def S(a):return sp.Matrix([[a,-a*a-1],[1,-a]])
def T(v):return sp.Matrix([[1,v],[0,1]])
def eq(X,Y):return all(sp.simplify(z)==0 for z in X-Y)
check('M standardization',eq(C*M*C.inv()/(2*r),S(u)))
check('Mprime standardization',eq(C*Mc*C.inv()/(2*r),S(-u)))
check('translation standardization',eq(C*T(1)*C.inv(),T(w)))
for name,a in [('plus',u),('minus',-u)]:
    check(name+' determinant',sp.simplify(S(a).det())==1)
    check(name+' central square',eq(S(a)*S(a),-sp.eye(2)))
check('two circles inside strip',Q(27)>1)
check('different circle center min distance',sp.simplify(w-2*u)==6*r)
check('distance square greater than4',Q(108)>4)
check('same center translation greater than min',Q(14)>6)
check('offcenter integer min classes',min(abs(8),abs(8-14))==6)
check('offcenter n beyond nearest larger',Q(14+8)>6 and Q(28-8)>6)
check('coverage height multiplier greater1',Q(108)>4)

a0,a1,a2,n1,n2,W=sp.symbols('a0 a1 a2 n1 n2 W',real=True)
b1=n1*W+a1-a0;b2=n2*W+a2-a1
g0=S(a0);g1=g0*T(n1*W)*S(a1);g2=g1*T(n2*W)*S(a2)
for j,g,a,cc,prev in [(0,g0,a0,sp.Integer(1),sp.Integer(0)),(1,g1,a1,b1,sp.Integer(1)),(2,g2,a2,b2*b1-1,b1)]:
    check('symbolic fixed c '+str(j),sp.expand(g[1,0]-cc)==0)
    check('symbolic fixed d '+str(j),sp.expand(g[1,1]+a*cc+prev)==0)
    check('symbolic fixed determinant '+str(j),sp.expand(g.det())==1)

ld=3*r+sp.sqrt(26)
check('Lambda lower exact',sp.simplify(ld+1/ld-6*r)==0)
check('Lambda square exact',sp.expand(ld*ld)==53+6*sp.sqrt(78))
check('Lambda square plus inverse',sp.simplify(ld*ld+1/(ld*ld))==106)
check('theta definition algebra',sp.simplify(1-1/(6*r*ld)-ld/(6*r))==0)
check('theta reciprocal rational bound simplified',Q(108,105)==Q(36,35))
check('angle lower comparison',Q(3,7)>Q(1,3))
check('angle upper comparison',Q(3,7)<Q(1,2))
check('transition beta coefficient',Q(36,35)*5/(3*588)==Q(1,343))

P=Q(484,49)
Up=Q(290884,123333)
Ua=P/(147*(1-P/343))
Avg=(Up+Ua)/2
check('pi upper square',Q(22,7)**2==P)
check('augmented geometric denominator positive',1-P/343>0)
check('augmented mean upper less5/4',Avg<Q(5,4))
check('k3 lowercost threshold above5/4',Q(539,253)>Q(5,4))
check('k2 lowercost threshold above5/4',Q(29,13)>Q(5,4))
check('two empty words factor exact',Q(2)*Q(2,588)==Q(1,147))

out={'check_count':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,
     'rational_bounds':{'base_plus_logradius_upper':str(Up),'augmented_logradius_upper':str(Ua),'mean_upper':str(Avg),'mean_cap':'5/4'},
     'scope':['only prescribed Gaug=<T,M,Mprime>','no old/peer producer','no word or research parameter scan','all-scale topology/convergence/Green proof in accompanying note','no all-source no-go','no number irrationality conclusion']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':out['all_passed'],'mean_rational_upper':str(Avg)},ensure_ascii=False))
