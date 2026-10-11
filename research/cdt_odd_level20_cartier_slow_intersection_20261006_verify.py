"""One fixed characteristic-zero 11-column jet, independent explicit inputs.

No prime search, frozen producer import, or numerical L-value is used.
The coordinate comes from the eta product h; E/F are divisor sums.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from math import comb
from pathlib import Path
import json

ORDER = 12
MINOR_ORDER = 11

@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __add__(self, x):
        x = kk(x); return K(self.a + x.a, self.b + x.b)
    __radd__ = __add__
    def __neg__(self): return K(-self.a, -self.b)
    def __sub__(self, x): return self + (-kk(x))
    def __rsub__(self, x): return kk(x) - self
    def __mul__(self, x):
        x = kk(x)
        return K(self.a*x.a + 5*self.b*x.b, self.a*x.b + self.b*x.a)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = kk(x); d = x.a*x.a - 5*x.b*x.b
        if not d: raise ZeroDivisionError
        return self * K(x.a/d, -x.b/d)
    def __rtruediv__(self, x): return kk(x)/self
    def conj(self): return K(self.a, -self.b)
    def norm(self): return self.a*self.a - 5*self.b*self.b
    def enc(self): return [str(self.a), str(self.b)]

def kk(x): return x if isinstance(x, K) else K(F(x), F(0))
ZERO = K()
ONE = K(F(1))
SQRT5 = K(F(0), F(1))

def padded(a): return list(a) + [ZERO]*(ORDER + 1 - len(a))
def add(a,b): return [a[i]+b[i] for i in range(ORDER+1)]
def scale(a,x): return [v*x for v in a]
def mul(a,b):
    out = [ZERO]*(ORDER+1)
    for i,x in enumerate(a):
        if x == ZERO: continue
        for j in range(ORDER+1-i):
            if b[j] != ZERO: out[i+j] = out[i+j]+x*b[j]
    return out
def inv(a):
    out = [ZERO]*(ORDER+1); out[0] = ONE/a[0]
    for n in range(1,ORDER+1):
        out[n] = -sum((a[j]*out[n-j] for j in range(1,n+1)),ZERO)/a[0]
    return out
def compose(a,b):
    if b[0] != ZERO: raise ValueError("inner constant must vanish")
    out = [ZERO]*(ORDER+1)
    for x in reversed(a):
        out = mul(out,b); out[0] = out[0]+x
    return out
def shifted(a,n): return [ZERO]*n+a[:ORDER+1-n]
def eta_factor(degree, exponent):
    # (1-q^degree)^exponent, for the specified integer exponent.
    out = [ZERO]*(ORDER+1)
    for j in range(ORDER//degree+1):
        if exponent >= 0:
            c = (-1)**j*comb(exponent,j) if j <= exponent else 0
        else:
            c = comb(-exponent+j-1,j)
        out[j*degree] = kk(c)
    return out

checks = []
def check(name, proposition):
    if not proposition: raise AssertionError(name)
    checks.append(name)

# h=q^-1 product eta4^2 eta5^2 /(eta1^2 eta20^2).
eta_exponents = {1:-2,4:2,5:2,20:-2}
Hbar = padded([ONE])
for d,e in eta_exponents.items():
    for n in range(1,ORDER//d+1): Hbar = mul(Hbar,eta_factor(d*n,e))
qvar = padded([ZERO,ONE])
tq = shifted(inv(add(Hbar,qvar)),1)
Tbar = tq[1:]+[ZERO]
qt = qvar
for _ in range(ORDER): qt = shifted(inv(compose(Tbar,qt)),1)
check("eta coordinate first six", tq[1:7] == [kk(x) for x in [1,-3,4,-7,13,-20]])
check("q(t) first six", qt[1:7] == [kk(x) for x in [1,3,14,82,539,3793]])
check("t(q(t)) exact truncation", compose(tq,qt) == qvar)
check("q(t(q)) exact truncation", compose(qt,tq) == qvar)
check("eta coordinate integral", all(x.b == 0 and x.a.denominator == 1 for x in tq))
check("inverse coordinate integral", all(x.b == 0 and x.a.denominator == 1 for x in qt))

def chi(n):
    v=n%5
    return 0 if v==0 else (1 if v in (1,4) else -1)
def eisenstein(weight):
    E = [ZERO]*(ORDER+1); G = [ZERO]*(ORDER+1)
    E[0] = kk(F(-1,5) if weight==2 else 1)
    for n in range(1,ORDER+1):
        E[n] = kk(sum(chi(d)*d**(weight-1) for d in range(1,n+1) if n%d==0))
        G[n] = kk(sum(chi(n//d)*d**(weight-1) for d in range(1,n+1) if n%d==0))
    return E,G
E2,G2=eisenstein(2)
E4,G4=eisenstein(4)
def old(a,d): return [a[n//d] if n%d==0 else ZERO for n in range(ORDER+1)]
def actual(sign):
    root = sign*SQRT5
    A = add(E2, scale(old(G2,4),-4*root))
    VE = add(add(E4,scale(old(E4,2),-5)),scale(old(E4,4),4))
    VF = add(add(G4,scale(old(G4,2),-20)),scale(old(G4,4),64))
    V = add(VE,scale(VF,-5*root/4))
    f = [ZERO]+[V[n]/(n**3) for n in range(1,ORDER+1)]
    At=compose(A,qt); ft=compose(f,qt)
    N=padded([ONE, -(6+root), 1+root])
    C=padded([ONE, -(6-2*root), 6-2*root])
    D=mul(mul(padded([ONE,-ONE]),N),C)
    Factual=mul(At,ft)
    source=mul(Factual,inv(D))
    Xi=[]
    for j in range(6):
        Xi.append([ZERO]+[source[n-j]/n if n>=j else ZERO for n in range(1,ORDER+1)])
    return dict(A=A,V=V,f=f,At=At,ft=ft,D=D,Xi=Xi)

minus=actual(1); plus=actual(-1)
check("weight4 cusp constant cancels", minus['V'][0] == ZERO)
check("actual f constant is zero", minus['f'][0] == ZERO)
check("A infinity normalization", minus['A'][0] == kk(F(-1,5)))
check("V first coefficient", minus['V'][1] == ONE-5*SQRT5/4)
check("f+ is coefficient conjugate", plus['f'] == [x.conj() for x in minus['f']])
check("A+ is coefficient conjugate", plus['A'] == [x.conj() for x in minus['A']])
check("six Xi are actual conjugates", plus['Xi'] == [[x.conj() for x in a] for a in minus['Xi']])
check("fixed denominator D constant", minus['D'][0] == ONE)

L=[ZERO]+[kk(F(1,n)) for n in range(1,ORDER+1)]
Li2=[ZERO]+[kk(F(1,n*n)) for n in range(1,ORDER+1)]
T3=scale(mul(mul(L,L),L),F(1,6))
R=mul(L,Li2)
M=[ZERO]+[kk(sum((F(1,j*j) for j in range(1,n)),F(0))/n) for n in range(1,ORDER+1)]
Li3=[ZERO]+[kk(F(1,n**3)) for n in range(1,ORDER+1)]
Kcoeff=[F(0)]
for n in range(1,ORDER+1): Kcoeff.append(F(2*n-1,2*n)*Kcoeff[-1]+F(1,n*n))
IK=[ZERO]+[kk(Kcoeff[n]/n) for n in range(1,ORDER+1)]
BG=[T3,R,M,Li3,IK]
check("IK first five independent recurrence", [x.a for x in IK[1:6]] == [F(1),F(1,2),F(17,54),F(2,9),F(21,125)])

def determinant(matrix):
    A=[list(row) for row in matrix]; out=ONE
    for i in range(len(A)):
        pivot=next((j for j in range(i,len(A)) if A[j][i]!=ZERO),None)
        if pivot is None: return ZERO
        if pivot!=i: A[i],A[pivot]=A[pivot],A[i]; out=-out
        x=A[i][i]; out=out*x
        for j in range(i+1,len(A)):
            c=A[j][i]/x
            for k in range(i,len(A)): A[j][k]=A[j][k]-c*A[i][k]
    return out

bg5=[[col[n] for col in BG] for n in range(1,6)]
check("background fixed five-minor", determinant(bg5) == kk(F(-1,3110400)))
columns=minus['Xi']+BG
matrix=[[col[n] for col in columns] for n in range(1,MINOR_ORDER+1)]
det=determinant(matrix)
check("fixed 11x11 minor nonzero", det != ZERO)
plusmatrix=[[col[n] for col in plus['Xi']+BG] for n in range(1,MINOR_ORDER+1)]
check("fixed plus minor is conjugate", determinant(plusmatrix) == det.conj())
check("minor norm nonzero", det.norm() != 0)
check("all eleven primitives vanish at zero", all(col[0] == ZERO for col in columns))

data={
    'scope':'One preselected 11x11 characteristic-zero minor; not a prime search or an S2 existence proof.',
    'order':ORDER,'minor_degrees':list(range(1,12)),
    'columns':['Xi0-','Xi1-','Xi2-','Xi3-','Xi4-','Xi5-','T3','L_Li2','Li1_2','Li3','I_K'],
    'eta_exponents':eta_exponents,
    'checks':checks,'checks_passed':len(checks),
    'matrix':[[v.enc() for v in row] for row in matrix],
    'determinant':det.enc(),
    'determinant_norm':str(det.norm()),
    'bad_norm_numerator':str(abs(det.norm().numerator)),
    'bad_norm_denominator':str(det.norm().denominator),
    'coordinate_tq':[x.enc() for x in tq],
    'coordinate_qt':[x.enc() for x in qt],
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:data[k] for k in ['checks_passed','determinant','determinant_norm','bad_norm_numerator','bad_norm_denominator']},indent=2))
