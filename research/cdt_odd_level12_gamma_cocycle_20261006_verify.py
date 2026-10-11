"""NEW fixed cyclic Fourier certificate at the four predetermined interpolation cusps."""
from fractions import Fraction as F
from pathlib import Path
import json

checks=[]
def check(name,condition):
    passed=bool(condition)
    checks.append({'name':name,'passed':passed})
    if not passed:
        raise AssertionError(name)

def chi(n):
    n%=12
    return 1 if n in (1,11) else -1 if n in (5,7) else 0
def zero(k): return [F(0)]*k
def poly(k,terms):
    p=zero(k)
    for m,c in terms:
        p[m%k]+=F(c)
    return p
def add(p,q): return [a+b for a,b in zip(p,q)]
def scale(p,a): return [a*c for c in p]
def mul(p,q):
    k=len(p); out=zero(k)
    for i,a in enumerate(p):
        if a:
            for j,b in enumerate(q):
                if b: out[(i+j)%k]+=a*b
    return out
def star(p):
    k=len(p)
    return [p[(-m)%k] for m in range(k)]
def b3(x): return x*x*x-F(3,2)*x*x+x/2
def tate(p,a=1):
    k=len(p)
    return F(2,3)*sum(c*b3(F((a*m)%k,k)) for m,c in enumerate(p))
def ordinary(l):
    return poly(l,[(m,F(1,2)-F(m,l)) for m in range(1,l)])

source={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
d=2880
check('fixed source constant constraint',sum(source.values())==-23*d)
check('fixed source zeta3 constraint',sum(F(v,j**3) for j,v in source.items())==0)
check('critical L4 pole normalization',F(144)*F(115,3)==5520)
check('complete pole cancellation',240*sum(source.values())+5520*d==0)
check('finite Gauss conductor chi0',chi(0)==0)
values={}

# Exactly the four points stated in G19; no search, no variable research choices.
for k in (12,24,36,48):
    r=k//12
    one=poly(k,[(0,1)])
    y=poly(k,[(12,1)])
    H=poly(k,[(a,chi(a)) for a in range(1,13)])
    J=poly(k,[(a,a*chi(a)) for a in range(1,13)])
    I=poly(k,[(12*l,F(1,r)) for l in range(r)])
    K=poly(k,[(12*l,(F(r-1,2)-l)/r) for l in range(r)])
    R=scale(mul(I,H),F(1,12))
    C=add(mul(H,K),mul(I,add(scale(H,F(1,2)),scale(J,-F(1,12)))))
    check(f'k{k} projector',mul(I,I)==I)
    check(f'k{k} yI equals I',mul(y,I)==I)
    check(f'k{k} complementary inverse',mul(add(one,scale(y,-1)),K)==add(one,scale(I,-1)))
    check(f'k{k} IK zero',mul(I,K)==zero(k))
    check(f'k{k} residue even',star(R)==R)
    check(f'k{k} finitepart odd',star(C)==scale(C,-1))
    check(f'k{k} pole finitepart CRT',mul(I,C)==mul(I,add(scale(H,F(1,2)),scale(J,-F(1,12)))))
    check(f'k{k} nonpole CRT',mul(add(one,scale(y,-1)),C)==mul(add(one,scale(I,-1)),H))
    A=poly(k,[(r*a,chi(a)) for a in range(1,13)])
    O=ordinary(k)
    G=scale(mul(A,O),F(12))
    V2=poly(k,[(0,F(1,2)),(k//2,-F(1,2))])
    V3=poly(k,[(0,F(2,3)),(k//3,-F(1,3)),(2*k//3,-F(1,3))])
    check(f'k{k} even Gauss carrier',star(A)==A)
    check(f'k{k} Gauss square conductor normalization',mul(A,A)==scale(mul(V2,V3),F(12)))
    check(f'k{k} scaled F odd Tate polynomial',star(G)==scale(G,-1))
    check(f'k{k} no F pole phase',chi(k)==0)
    triv=sum(F(240*v,j**3)*tate(ordinary(k//j)) for j,v in source.items())
    e=tate(C)
    f=tate(G)
    total=triv+d*(e+f)
    expected=F(14720*r)-F(320,r)
    check(f'k{k} actual finite value eta normalization',total==expected)
    values[str(k)]={'trivial_Tate':str(triv),'E_Tate':str(e),
                    'scaled_F_Tate':str(f),'h_over_i_pi3':str(total)}

# The fixed four seed points are distinct; deleting any one leaves rational invertible Vandermonde.
points=[F(1,12*j) for j in (1,2,3,4)]
for omit in range(4):
    xs=[x for j,x in enumerate(points) if j!=omit]
    determinant=(xs[1]-xs[0])*(xs[2]-xs[0])*(xs[2]-xs[1])
    check(f'fixed interpolation omit{omit+1}',determinant!=0)

result={'scope':'NEW four fixed finite interpolation cusps; all-k proof in MD',
        'passed':len(checks),'checks':checks,'finite_values':values}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({'passed':len(checks),'failed':0,'finite_values':values}))
