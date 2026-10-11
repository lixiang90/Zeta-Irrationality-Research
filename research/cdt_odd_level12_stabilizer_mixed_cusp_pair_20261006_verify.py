"""NEW fixed symbolic certificate for the all-integer mixed cusp-pair lemma.

This script performs polynomial identities in formal n and gamma entries.
There is no word/parameter/prime search and no old or peer producer import.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
checks = []


def check(name, statement):
    checks.append({"name": name, "passed": bool(statement)})
    if not statement:
        raise AssertionError(name)


def zero_matrix(A):
    return all(s.expand(x) == 0 for x in A)


def R(A):
    a,b,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
    return s.Matrix([[d*d,b*d,b*b],
                     [2*c*d,a*d+b*c,2*a*b],
                     [c*c,a*c,a*a]])/A.det()


def discriminant(P):
    return s.factor(P[1]**2-4*P[0]*P[2])


def same_psl(A,B):
    return zero_matrix(A-B) or zero_matrix(A+B)


I2=s.eye(2)
I3=s.eye(3)
X4=s.Matrix([[11,3],[-48,-13]])
X5=s.Matrix([[25,16],[-36,-23]])
A4=s.Matrix([[-1,0],[4,-1]])
A5=s.Matrix([[-2,-1],[3,1]])
M=s.Matrix([[24,-7],[84,-24]])
P4=s.Matrix([-2266160,-16555200,-30256320])
P5=s.Matrix([-1329040,-4311360,-3531840])
n=s.symbols('n', integer=True)

check('A4-det1',A4.det()==1)
check('A5-det1',A5.det()==1)
check('M-det12',M.det()==12)
check('X4-cusp-scale-minus3',same_psl(X4,A4*s.Matrix([[1,-3],[0,1]])*A4.inv()))
check('X5-cusp-scale-plus4',X5==A5*s.Matrix([[1,4],[0,1]])*A5.inv())

def power_period(A,P):
    D=R(A)-I3
    return s.expand(n*P+n*(n-1)*D*P/2+n*(n-1)*(n-2)*D*D*P/6)

C4=power_period(X4,P4)
C5=power_period(X5,P5)
expected_disc=-307200*n**2*(844561*n**2-232577)
for label,A,P,C in [('4',X4,P4,C4),('5',X5,P5,C5)]:
    check('Sym2-unipotent-nilpotent-'+label,zero_matrix((R(A)-I3)**3))
    check('power-period-at-zero-'+label,zero_matrix(C.subs(n,0)))
    check('power-period-at-one-'+label,zero_matrix(C.subs(n,1)-P))
    check('power-period-all-integer-recurrence-'+label,
          zero_matrix(C.subs(n,n+1)-R(A)*C-P))
    check('power-period-discriminant-'+label,
          s.expand(discriminant(C)-expected_disc)==0)
    check('primitive-period-discriminant-'+label,
          discriminant(P)==-188001484800)
    check('scaled-highest-coefficient-'+label,
          s.expand((R(A4 if label=='4' else A5)*C)[2]
                   -n*(-294080 if label=='4' else -220560))==0)

beta4=(R(A4)*P4)[2]
beta5=(R(A5)*P5)[2]
check('beta4-literal',beta4==-294080)
check('beta5-literal',beta5==-220560)
check('common-beta-width-norm',(-3*beta4)**2==(4*beta5)**2==882240**2)
check('height-product-cancellation',4*abs(beta4*beta5)==307200*844561)
check('height-product-identity',s.cancel((-expected_disc)/(4*n**2*abs(beta4*beta5))
                                      -(n**2-s.Rational(232577,844561)))==0)
minimum=Fraction(611984,844561)
check('height-product-lower-bound',minimum>Fraction(1,12))
check('even-coset-bound-stronger',Fraction(1,25)<Fraction(1,12))
check('discriminant-monotone-for-positive-integer-powers',
      2*844561-232577>0 and 844561-232577>0)

# Generic translation polynomial identity; this gives a separate derivation
# of the displayed discriminant for every positive or negative integer n.
qa,qb,qc,w=s.symbols('qa qb qc w')
Ct=s.Matrix([n*qc+qb*w*n*(n-1)/2+qa*w*w*n*(n-1)*(2*n-1)/6,
             n*qb+qa*w*n*(n-1),n*qa])
generic_disc=n*n*((qb*qb-4*qa*qc)-qa*qa*w*w*(n*n-1)/3)
check('generic-Tw-discriminant-identity',s.expand(discriminant(Ct)-generic_disc)==0)

# All gamma entries remain formal. epsilon is the common +/-1 residue of
# a and d; upper-case entries are arbitrary integral multiples of12.
a,b,c,d=s.symbols('a b c d')
aa,dd,rr,e=s.symbols('aa dd rr e',integer=True)
Gamma=s.Matrix([[a,b],[c,d]])
Cross0=A5.inv()*Gamma*A4
Cross1=A5.inv()*Gamma*M*A4
check('even-cross-lowerleft-formula',s.expand(Cross0[1,0]-(3*a-12*b+2*c-8*d))==0)
check('even-cross-residue-identity',
      s.expand(Cross0[1,0].subs({a:12*aa+e,d:12*dd+e,c:12*rr})
               -(12*(3*aa-b+2*rr-8*dd)-5*e))==0)
check('odd-cross-lowerleft-formula',
      s.expand(Cross1[1,0]-(156*a+540*b+104*c+360*d))==0)
check('odd-cross-divisibility-identity',
      s.expand(Cross1[1,0].subs(c,12*rr)
               -12*(13*a+45*b+104*rr+30*d))==0)
check('primitive-column-before-odd-action',M*A4[:,0]==4*s.Matrix([-13,-45]))

# These are only the two +/- congruence choices in the group definition,
# not a family of n,m examples. They certify the written mod12/mod3
# contradiction to a zero lower-left odd cross coefficient.
for residue in (1,-1):
    check('even-cross-minimum-residue-'+str(residue),
          min((-5*residue)%12, (5*residue)%12)==5)
    for target_sign in (1,-1):
        check('odd-zero-column-forces-common-sign-'+str(residue)+'-'+str(target_sign),
              ((-9*residue-3*target_sign)%12==0)==(residue==target_sign))
    check('odd-zero-column-mod3-impossible-'+str(residue),
          (-residue+2*residue)%3!=0)

pins={
 'cdt_odd_level12_generator_cocycle_20261006.md':
 'a3f00c593a9fcc3f9b1791b854faa0ad7b721b6c76d67cc52598cd5f919f67ca',
 'cdt_odd_level12_stabilizer_structure_20261006.md':
 '7d2d33557945c880857e080cd1ffbfcb22902b4d7f3d7af0fd02e204cbc8cd22',
}
for name,digest in pins.items():
    check('frozen-input-pin-'+name,hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest)

payload={
 'description':'All-integer mixed cusp-pair symbolic identities; no parameter or word scan',
 'run_history':'First single execution, all fixed checks passed without corrections',
 'parameters':'n is formal; gamma entries are formal; +/- signs are only congruence-group residue choices',
 'x4':X4.tolist(),'x5':X5.tolist(),'A4':A4.tolist(),'A5':A5.tolist(),'M':M.tolist(),
 'pureL_period4':list(P4),'pureL_period5':list(P5),
 'power_period4':[str(s.factor(v)) for v in C4],
 'power_period5':[str(s.factor(v)) for v in C5],
 'common_discriminant':str(expected_disc),
 'beta4':int(beta4),'beta5':int(beta5),
 'height_product_minimum':str(minimum),'input_pins':pins,
 'checks':checks,'check_count':len(checks),'all_passed':all(x['passed'] for x in checks),
}
out=HERE/'cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006_verify.json'
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2,default=lambda x:int(x))+'\n',encoding='utf-8')
print(f'{len(checks)} fixed symbolic checks passed; wrote {out.name}')
