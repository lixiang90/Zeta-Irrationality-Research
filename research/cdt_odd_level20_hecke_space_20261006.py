"""New exact finite Hecke-space experiment. No historical producer imports.

All series use Z[sqrt(5)] pairs. The six-dimensional space theorem is
proved in the companion note; fixed coefficient checks verify normalization.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sys
import sympy as sp

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
N = 132
ZERO = (0, 0)
ONE = (1, 0)

def add(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[0], -a[1])
def sub(a, b): return add(a, neg(b))
def mul(a, b): return (a[0]*b[0]+5*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def scale(a, n): return (n*a[0], n*a[1])
def conv(a, b, limit=N):
    c=[ZERO]*(limit+1)
    for i, x in enumerate(a[:limit+1]):
        if x == ZERO: continue
        for j, y in enumerate(b[:limit+1-i]):
            if y != ZERO: c[i+j]=add(c[i+j],mul(x,y))
    return c
def inv(a, limit=N):
    assert a[0]==ONE
    c=[ONE]+[ZERO]*limit
    for n in range(1,limit+1):
        c[n]=neg(sum_pairs(mul(a[i],c[n-i]) for i in range(1,min(n,len(a)-1)+1)))
    return c
def sum_pairs(xs):
    s=ZERO
    for x in xs: s=add(s,x)
    return s
def pprod(a,b): return conv(a,b,len(a)+len(b)-2)
def compose(poly,t):
    out=[ZERO]*(N+1)
    for c in reversed(poly):
        out=conv(out,t)
        out[0]=add(out[0],c)
    return out
def chi(n): return [0,1,-1,-1,1][n%5]

def eta_unit(exponents, shift):
    s=[ONE]+[ZERO]*N
    for d,e in exponents.items():
        for n in range(d,N+1,d):
            # Multiplication by (1-q^n)^e, including negative e.
            factor=[ZERO]*(N+1)
            factor[0]=ONE
            for j in range(1,N//n+1):
                if e>=0:
                    if j>e: break
                    val=(-1)**j*int(sp.binomial(e,j))
                else: val=int(sp.binomial(-e+j-1,j))
                factor[j*n]=(val,0)
            s=conv(s,factor)
    return [ZERO]*shift+s[:N+1-shift]

t=eta_unit({1:3,4:1,5:1,20:3,2:-4,10:-4},1)
E=[ZERO]*(N+1); E[0]=(-1,0) # five times E2
F=[ZERO]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d): E[n]=add(E[n],(5*chi(d)*d,0))
for n in range(1,N//4+1):
    for m in range(1,N//(4*n)+1): F[4*m*n]=add(F[4*m*n],(chi(n)*m,0))
S=[ZERO]*(N+1);S[0]=ONE
# The exact eta logarithmic derivative, without E2 rational divisions.
for d,e in {1:3,4:1,5:1,20:3,2:-4,10:-4}.items():
    for k in range(d,N+1,d):
        for n in range(k,N+1,k): S[n]=add(S[n],(-e*k,0))

bases={}; divisors={}
for sign in [-1,1]: # sign is A's subscript sign, A_- at -1
    A=[add(E[n],(0,sign*20*F[n][0])) for n in range(N+1)]
    # N_- has -sqrt5*t + sqrt5*t^2.
    n_poly=[ONE,(-6,sign),(1,-sign)]
    c_poly=[ONE,(-6,-2*sign),(6,2*sign)]
    D=pprod(pprod([ONE,(-1,0)],n_poly),c_poly)
    divisors[sign]=D
    base=conv(conv(A,S),inv(compose(D,t)))
    basis=[base]
    for j in range(1,6): basis.append(conv(basis[-1],t))
    bases[sign]=basis
    assert all(basis[j][j]==(-1,0) and all(x==ZERO for x in basis[j][:j]) for j in range(6))

checks=[]
def check(label, condition):
    assert condition,label
    checks.append(label)

check('t fixed first coefficients', t[:7]==[(0,0),(1,0),(-3,0),(4,0),(-7,0),(13,0),(-20,0)])
matrices={}
for p in [3,7,11]:
    eps=chi(p)
    for sign in [-1,1]:
        target=sign*eps
        columns=[]
        for j,series in enumerate(bases[sign]):
            extract=[]
            for n in range(13):
                a=series[p*n]
                if n%p==0:a=add(a,scale(series[n//p],eps*p**3))
                extract.append(a)
            coords=[]
            rem=extract[:]
            for i in range(6):
                c=neg(rem[i]);coords.append(c)
                for n in range(13):rem[n]=sub(rem[n],mul(c,bases[target][i][n]))
            check(f'T{p} sign{sign} basis{j} full Sturm prefix', all(x==ZERO for x in rem))
            columns.append(coords)
        matrices[p,sign]=[[columns[j][i] for j in range(6)] for i in range(6)]

def mm(A,B):return [[sum_pairs(mul(A[i][k],B[k][j]) for k in range(6)) for j in range(6)] for i in range(6)]
def mv(A,v):return [sum_pairs(mul(A[i][k],v[k]) for k in range(6)) for i in range(6)]
def expr(a):return sp.Rational(a[0])+sp.Rational(a[1])*sp.sqrt(5)
def sym(A):return sp.Matrix([[expr(a) for a in row] for row in A])
def encode(a):return [str(a[0]),str(a[1])]

U=mm(matrices[3,1],matrices[3,-1])
V=mm(matrices[7,1],matrices[3,-1])
W=matrices[11,-1]
check('T3 squared commutes with T11',mm(U,W)==mm(W,U))
check('T3 squared commutes with T7T3',mm(U,V)==mm(V,U))
# Explicit level10 cusp basis: products of character weight2 Eisenstein
# forms and ordinary holomorphic weight2 forms S_d=dE2(d*tau)-E2(tau).
ordinary={}
for d in [2,5,10]:
    a=[(d-1,0)]+[ZERO]*N
    for k in range(1,N+1):
        for n in range(k,N+1,k):a[n]=add(a[n],(24*k,0))
    for k in range(d,N+1,d):
        for n in range(k,N+1,k):a[n]=add(a[n],(-24*k,0))
    ordinary[d]=a
combE=[sum_pairs([scale(ordinary[2][n],-5),neg(ordinary[5][n]),ordinary[10][n]]) for n in range(N+1)]
combF=[sum_pairs([neg(ordinary[2][n]),scale(ordinary[5][n],-5),scale(ordinary[10][n],5)]) for n in range(N+1)]
F1=[ZERO]*(N+1)
for n in range(1,N+1):
    for m in range(1,N//n+1):F1[m*n]=add(F1[m*n],(chi(n)*m,0))
hE=conv(E,combE);hF=conv(F1,combF)
check('level10 cusp normalized coefficient integrality',all(x[0]%120==0 and x[1]==0 for x in hE) and all(x[0]%24==0 and x[1]==0 for x in hF))
e=[x[0]//120 for x in hE];f=[x[0]//24 for x in hF]
check('level10 cusp difference divisible by4',all((b-a)%4==0 for a,b in zip(e,f)))
level10=[f,[(b-a)//4 for a,b in zip(e,f)]]
check('level10 cusp independent leading coefficients',[a[:3] for a in level10]==[[0,1,0],[0,0,1]])
T3_10=[]
for j,a in enumerate(level10):
    image=[a[3*n]+(-27*a[n//3] if n%3==0 else 0) for n in range(7)]
    co=[image[1],image[2]]
    check(f'level10 T3 basis{j} Sturm equality',all(image[n]==sum(co[i]*level10[i][n] for i in range(2)) for n in range(7)))
    T3_10.append(co)
T3_10=sp.Matrix(T3_10).T
check('level10 T3 square minus4',T3_10**2==-4*sp.eye(2))
oldjets=sp.Matrix([[a[n] if scale_q==1 else (a[n//2] if n%2==0 else 0) for a,scale_q in [(level10[0],1),(level10[1],1),(level10[0],2),(level10[1],2)]] for n in range(13)])
check('level20 four old cusp forms independent',oldjets.rank()==4)
E4=[1]+[0]*N;F4=[0]*(N+1)
for d in range(1,N+1):
    for n in range(d,N+1,d):E4[n]+=chi(d)*d**3
for n in range(1,N+1):
    for m in range(1,N//n+1):F4[m*n]+=chi(n)*m**3
eisjets=sp.Matrix([[a[n//d] if n%d==0 else 0 for a,d in [(E4,1),(E4,2),(E4,4),(F4,1),(F4,2),(F4,4)]] for n in range(13)])
check('level20 six Eisenstein forms independent',eisjets.rank()==6)
constmat=[]
for c in [1,2,4,5,10,20]:
    row=[]
    for family in ['E','F']:
        for d in [1,2,4]:
            from math import gcd
            g=gcd(c,d)
            if family=='E':a=Fraction(g,d)**4*chi(d//g) if (c//g)%5==0 else Fraction(0)
            else:a=Fraction(g,d)**4*chi(c//g)/625 if (c//g)%5 else Fraction(0)
            row.append(sp.Rational(a.numerator,a.denominator))
    constmat.append(row)
check('level20 full cusp constant map rank6',sp.Matrix(constmat).rank()==6)
source=divisors[-1]
krylov=[];v=source
for k in range(7):
    krylov.append(v);v=mv(U,v)
Kmat=sp.Matrix.hstack(*(sp.Matrix([expr(x) for x in col]) for col in krylov[:6]))
rank=Kmat.rank()
fixed_stable=[]
for operator in [V,W]:
    extended=sp.Matrix.hstack(Kmat,*(sp.Matrix([expr(x) for x in mv(operator,col)]) for col in krylov[:3]))
    fixed_stable.append(extended.rank()==rank)
check('fixed source space T7T3 stability',fixed_stable[0])
check('fixed source space T11 stability',fixed_stable[1])
char=sp.Poly(sym(U).charpoly().as_expr()).as_expr()
minimal=None
for k in range(1,7):
    if sp.Matrix.hstack(*(sp.Matrix([expr(x) for x in col]) for col in krylov[:k+1])).rank()==k:
        sol=sp.Matrix.hstack(*(sp.Matrix([expr(x) for x in col]) for col in krylov[:k])).gauss_jordan_solve(sp.Matrix([expr(x) for x in krylov[k]]))[0]
        minimal=[str(sp.simplify(x)) for x in sol];break
projectors={}; kernels={}
for name,eigen in [('E',676),('O',-4),('N',-76)]:
    M=sp.eye(6);den=1
    for other in [676,-4,-76]:
        if other!=eigen:M=M*(sym(U)-other*sp.eye(6));den*=eigen-other
    v0=M*sp.Matrix([expr(x) for x in source])/den
    v1=sym(matrices[3,-1])*v0
    projectors[name]={'T3_squared_eigenvalue':eigen,'minus_coordinates':[str(sp.simplify(x)) for x in v0], 'plus_T3_coordinates':[str(sp.simplify(x)) for x in v1]}
    check(f'source {name} projector nonzero',v0!=sp.zeros(6,1))
    check(f'source {name} projector eigenrelation',all(sp.simplify(x)==0 for x in sym(U)*v0-eigen*v0))
    kernels[name]=v0
check('three exact source component directions independent',sp.Matrix.hstack(*kernels.values()).rank()==3)
out={'scope':'Exact fixed Hecke matrices on both six-dimensional Fricke eigenspaces; no prime scan or claimed Smith gain.',
     'checks_passed':len(checks),'check_labels':checks,'series_order':N,
     'primes':[3,7,11], 'T3_squared_characteristic_polynomial':str(sp.factor(char)),
     'T3_squared_source_krylov_rank':rank,'source_annihilator_relation':minimal,
     'level10_cusp_T3_matrix':[[str(x) for x in row] for row in T3_10.tolist()],
     'level10_cusp_basis_prefixes':[a[:13] for a in level10],
     'level20_old_cusp_jet_rank':oldjets.rank(),
     'level20_Eisenstein_jet_rank':eisjets.rank(),
     'level20_Eisenstein_cusp_constant_matrix':[[str(x) for x in row] for row in constmat],
     'source_spectral_projectors':projectors,
     'fixed_source_space_T7T3_T11_stable':fixed_stable,
     'matrices':{f'{p}:{sign}':[[encode(a) for a in row] for row in M] for (p,sign),M in matrices.items()},
     'source_divisors':{str(s):[encode(a) for a in D] for s,D in divisors.items()},
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['checks_passed','T3_squared_characteristic_polynomial','T3_squared_source_krylov_rank','source_annihilator_relation']},ensure_ascii=False))
