"""One new fixed three-source calculation; no frozen producer execution."""
from pathlib import Path
import json
import sympy as s

a,b,d=s.symbols('a b d')
r=s.sqrt(2)
labels=[]
def check(name, condition):
    if not bool(condition): raise AssertionError(name)
    labels.append(name)
def zero(expr): return s.simplify(expr)==0

E=s.symbols('E1 E2 E4 E8')
old={1:E[0],2:E[1],4:E[2],8:E[3]}
W={old[j]:s.Rational(64,j**4)*old[8//j] for j in old}
G1=E[0]-64*E[3]
G2=E[1]-4*E[2]
check('G1 exact W8 anti',zero(G1.xreplace(W)+G1))
check('G2 exact W8 anti',zero(G2.xreplace(W)+G2))
ec,fc=s.symbols('Ec Fc')
kappa=16*r
CW={ec:kappa*fc,fc:ec/kappa}
check('character minus W anti',zero((ec-kappa*fc).xreplace(CW)+ec-kappa*fc))
check('character plus W plus',zero((ec+kappa*fc).xreplace(CW)-ec-kappa*fc))
constant=-63*a-3*b+s.Rational(11,2)*d
dc=(126*a+6*b)/11
check('full infinity constant zero condition',zero(constant.subs(d,dc)))
check('G1 L3 coefficient',-120*(1-s.Rational(64,8**3))==-105)
check('G2 L3 coefficient',-120*(s.Rational(1,2**3)-s.Rational(4,4**3))==-s.Rational(15,2))
check('character L3 coefficient',kappa/2==8*r)
Ureal=-s.Rational(1,2)*(240-30)
G2real=-s.Rational(1,2)*(30-15)
check('G1 finite real matches L3',Ureal==-105)
check('G2 finite real matches L3',G2real==-s.Rational(15,2))
tg=s.Rational(2,243)
c1=(240+30)*tg
c2=(-30-15)*tg
cc=s.Rational(4,81)+s.Rational(23,108)
check('G1 finite imaginary',c1==s.Rational(20,9))
check('G2 finite imaginary',c2==-s.Rational(10,27))
check('character finite imaginary',cc==s.Rational(85,324))
C=s.expand((a*c1+b*c2+d*cc).subs(d,dc))
check('complete family Tate coefficient',zero(C-(115*a-5*b)/22))
residue=s.Rational(945,4)*a+s.Rational(45,4)*b-s.Rational(165,8)*d
check('entire radial divergence cancellation',zero(residue.subs(d,dc)))
A=-105*a-s.Rational(15,2)*b
matrix=s.Matrix([[-105,-s.Rational(15,2)],[s.Rational(115,22),-s.Rational(5,22)]])
check('two projected constraints determinant',matrix.det()==s.Rational(2775,44))
check('only zero simultaneous solution',s.solve([A,C],[a,b])=={a:0,b:0})

pure={a:1,b:-14,d:s.Rational(42,11)}
tatefree={a:1,b:23,d:24}
for name,point in [('pure',pure),('tatefree',tatefree)]:
    check(name+' modular constant zero',zero(constant.subs(point)))
check('pure zeta coefficient zero',A.subs(pure)==0)
check('pure L3 coefficient 336sqrt2 over11',8*r*pure[d]==s.Rational(336,11)*r)
check('pure Tate coefficient 185over22',C.subs(pure)==s.Rational(185,22))
check('tatefree Tate coefficient zero',C.subs(tatefree)==0)
check('tatefree zeta coefficient',A.subs(tatefree)==-s.Rational(555,2))
check('tatefree L3 coefficient',8*r*tatefree[d]==192*r)
check('tatefree target coefficient identity',-s.Rational(3,2)*185==A.subs(tatefree))
check('tatefree target L coefficient identity',s.Rational(3,2)*128*r==8*r*tatefree[d])
check('pure integral fixed denominator',all(s.sympify(11*value).is_Integer for value in pure.values()))

M=s.Matrix([[8,-3],[24,-8]])
tau=s.symbols('tau')
qM=1+8*(3*tau-1)**2
check('actual M square',M*M==-8*s.eye(2))
check('actual M endpoint',s.Rational(8,24)==s.Rational(1,3))
check('qM not translation periodic',s.expand(qM.subs(tau,tau+1)-qM)!=0)
check('qM involution invariant',zero((24*tau-8)**2/8*qM.subs(tau,(8*tau-3)/(24*tau-8))-qM))

data={'scope':'Preselected level8 G1/G2/character three-source family; no scan, no new odd-L irrationality claim.',
      'checks_passed':len(labels),'checks':labels,
      'constraints_d':str(dc),'zeta_coefficient':str(A),'tate_coefficient':str(C),
      'constraint_determinant':str(matrix.det()),
      'pure_parameters':{'a':'1','b':'-14','d':'42/11'},
      'tatefree_parameters':{'a':'1','b':'23','d':'24'}}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks_passed':len(labels),'constraint_determinant':str(matrix.det())}))
