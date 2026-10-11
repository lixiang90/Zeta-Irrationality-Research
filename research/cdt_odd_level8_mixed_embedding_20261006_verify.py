"""New fixed exact certificate; no old producers or downloaded source execution."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

checks = []

def chk(name, value):
    value = bool(value)
    checks.append({'name': name, 'passed': value})
    if not value:
        raise AssertionError(name)

t = sp.symbols('tau')
r = sp.sqrt(2)
W = sp.Matrix([[0, -1], [8, 0]])
ga = sp.Matrix([[3, 1], [8, 3]])
gb = sp.Matrix([[3, -1], [-8, 3]])
M, Mp = ga*W, gb*W
chk('gamma determinant one', ga.det() == 1)
chk('gamma prime determinant one', gb.det() == 1)
chk('gamma character minus', sp.kronecker_symbol(8, 3) == -1)
chk('M exact', M == sp.Matrix([[8, -3], [24, -8]]))
chk('M prime exact', Mp == sp.Matrix([[-8, -3], [24, 8]]))
for name, mat in [('M', M), ('Mprime', Mp)]:
    chk(name+' determinant 8', mat.det() == 8)
    chk(name+' trace zero', sp.trace(mat) == 0)
    chk(name+' square minus 8I', mat*mat == -8*sp.eye(2))
    a,b,c,d = list(mat)
    qm = 1 + (c*t+d)**2/8
    transform = (c*t+d)**2/8 * qm.subs(t, (a*t+b)/(c*t+d))
    chk(name+' quadratic invariant', sp.cancel(transform-qm) == 0)
    center = sp.Rational(a,c)
    chk(name+' endpoint quadratic value one', qm.subs(t, center) == 1)
    fixed = center + sp.I*sp.sqrt(8)/c
    chk(name+' exact fixed point', sp.simplify((a*fixed+b)/(c*fixed+d)-fixed) == 0)
    chk(name+' quadratic not T periodic', sp.expand(qm.subs(t,t+1)-qm) != 0)

def genB(j, D):
    return sp.expand(D**(j-1)*sum(sp.kronecker_symbol(D,a)*sp.bernoulli(j,sp.Rational(a,abs(D))) for a in range(1,abs(D)+1)))

# For negative fundamental discriminant, the conductor is abs(D), not D.
def genB_signed(j, disc):
    cond = abs(disc)
    return sp.expand(cond**(j-1)*sum(sp.kronecker_symbol(disc,a)*sp.bernoulli(j,sp.Rational(a,cond)) for a in range(1,cond+1)))

chk('B2 chi8', genB_signed(2,8) == 2)
chk('Lminus1 chi8', -genB_signed(2,8)/2 == -1)
chk('B4 chi8', genB_signed(4,8) == -44)
chk('E4 constant chi8', -genB_signed(4,8)/8 == sp.Rational(11,2))
chk('B3 chi minus3', genB_signed(3,-3) == sp.Rational(2,3))
chk('B3 chi minus24', genB_signed(3,-24) == 138)
for a in range(1,25):
    chk('product character residue '+str(a), sp.kronecker_symbol(8,a)*sp.kronecker_symbol(-3,a) == sp.kronecker_symbol(-24,a))
    if sp.gcd(a,24) == 1:
        chk('chi minus24 signs '+str(a), sp.kronecker_symbol(-24,a) == (1 if a < 12 else -1))

pi = sp.pi
L3m3 = 2*pi**3*genB_signed(3,-3)/(3*3**sp.Rational(5,2))
L3m24 = 2*pi**3*genB_signed(3,-24)/(3*24**sp.Rational(5,2))
chk('critical L3 minus3', sp.simplify(L3m3-4*pi**3/(81*sp.sqrt(3))) == 0)
chk('critical L3 minus24', sp.simplify(L3m24-23*pi**3/(288*sp.sqrt(6))) == 0)
L4c8 = -sp.sqrt(8)/2*(2*pi/8)**4*genB_signed(4,8)/sp.factorial(4)
chk('critical kappa L4', sp.simplify(16*r*L4c8-sp.Rational(165,8)*pi**4/90) == 0)

rho = -sp.Rational(1,2)+sp.I*sp.sqrt(3)/2
for root,sg in [(rho,1),(sp.conjugate(rho),-1)]:
    chk('Lambert root '+str(sg), sp.simplify(root/(1-root)+sp.Rational(1,2)-sg*sp.I*sp.sqrt(3)/6) == 0)
    ek = (root-root**3-root**5+root**7)/(1-root**8)
    chk('E chi root '+str(sg), sp.simplify(ek-sg*sp.I*sp.sqrt(3)) == 0)
z=sp.symbols('z')
ek=(z-z**3-z**5+z**7)/(1-z**8)
chk('E chi removable at one', sp.limit(ek,z,1) == 0)
chk('radial divergence cancels', sp.Rational(1320)*(1-sp.Rational(1,64))-63*sp.Rational(165,8) == 0)
chk('U finite imaginary coefficient', sp.Rational(1320)*(1+sp.Rational(1,8))*sp.Rational(2,243) == sp.Rational(110,9))
chk('E finite imaginary coefficient', sp.simplify(63*sp.sqrt(3)*L3m3/pi**3-sp.Rational(28,9)) == 0)
chk('F finite imaginary coefficient', sp.simplify(1008*r*sp.sqrt(3)*L3m24/(6*pi**3)-sp.Rational(161,12)) == 0)
chk('complete lambda imaginary coefficient', sp.Rational(110,9)+sp.Rational(28,9)+sp.Rational(161,12) == sp.Rational(115,4))

xu,xv = sp.symbols('xiU xiV')
xi,psi=xu+xv,xu-xv
poly_u=xu*(1+8*t**2)-462*sp.I*pi**3*t**3+sp.Rational(231,32)*sp.I*pi**3/t
poly_vm=xv*(1+8*t**2)+462*sp.I*pi**3*t**3-sp.Rational(231,32)*sp.I*pi**3/t
poly_vp=-xv*(1-8*t**2)-42*sp.I*pi**3*t+462*sp.I*pi**3*t**3+sp.Rational(231,32)*sp.I*pi**3/t
chk('original pure period cancellation', sp.expand(poly_u+poly_vm-xi*(1+8*t**2)) == 0)
chk('sigma full Laurent period', sp.expand(poly_u+poly_vp-(psi+8*xi*t**2-42*sp.I*pi**3*t+sp.Rational(231,16)*sp.I*pi**3/t)) == 0)
chk('cusp constant 693', 2*63*sp.Rational(11,2) == 693)
chk('reciprocal coefficient 231/16', sp.Rational(693)*8/(6*8**2) == sp.Rational(231,16))
chk('cubic coefficient 462', sp.Rational(693,2)*8/6 == 462)
qm=1+8*(3*t-1)**2
qmp=1+8*(3*t+1)**2
C=sp.Rational(115,4)*sp.I*pi**3
chk('complete endpoint trace residual', sp.expand(((psi+C)*qm+(psi-C)*qmp)/2-(9*psi*(1+8*t**2)-1380*sp.I*pi**3*t)) == 0)

data={'description':'Fixed level8 mixed-embedding exact audit; analytic proofs live in the companion report.',
      'check_count':len(checks),'all_passed':all(c['passed'] for c in checks),'checks':checks,
      'scope':['No old producer execution','No numerical irrationality theorem','No assignment sigma(zeta3) or sigma(L3)','No global leaf/capacity computation']}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'check_count':len(checks),'all_passed':data['all_passed']},ensure_ascii=False))
