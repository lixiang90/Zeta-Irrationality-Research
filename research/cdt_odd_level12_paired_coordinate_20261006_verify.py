"""NEW fixed exact checks for the D12 source and paired quotient coordinates.

No old producer is imported or executed.  There is one prescribed source,
one prescribed seventh-root endpoint, six prescribed cusps and order-12
formal expansions.  These checks supplement the proofs in the MD file.
"""
from fractions import Fraction as F
from math import gcd, comb
from pathlib import Path
import json
import sympy as sp

checks = []
def check(label, actual, expected=True):
    ok = actual == expected
    if not ok and isinstance(actual,sp.Expr) and not isinstance(expected,bool):
        ok = sp.simplify(actual-sp.sympify(expected)) == 0
    checks.append({"label": label, "passed": bool(ok)})
    if not ok:
        raise AssertionError((label, actual, expected))

def B3(x):
    return x**3-F(3,2)*x**2+F(1,2)*x
def frac(x):
    return x-x.numerator//x.denominator
def chi(a):
    return {1:1,5:-1,7:-1,11:1}.get(a % 12,0)

T = {}
for a in range(1,7):
    ia = pow(a,-1,7)
    T[a] = F(1,21)*sum((7-2*((m*ia)%7))*B3(F(m,7))
                       for m in range(1,7))
check("ordinary six finite B3 values", list(T.values()),
      [F(12,343),F(4,343),0,0,F(-4,343),F(-12,343)])
triv = [240*(T[2]-T[3]/12),30*T[4]-10*T[5],
        F(80,9)*T[6]-F(20,3)*T[1]]
check("three actual oldscale Tate coefficients",triv,
      [F(960,343),F(40,343),F(-80,147)])
# An independent reciprocal Fourier polynomial, not the short kernel in
# the source-period producer, gives the E-character contribution.
Etate = F(-2,21)*sum(chi(a)*k*B3(frac(F(2*(a+12*k),7)))
                    for a in range(1,13) for k in range(1,7))
check("independent E-character finite sum",Etate,F(12,343))
weights = [7-2*((4*m)%7) for m in range(1,7)]
inner = [sum(chi(a)*B3(frac(F(a,12)+F(m,7))) for a in range(1,13))
         for m in range(1,7)]
check("Gauss finite weights",weights,[-1,5,-3,3,-5,1])
check("first three Gauss B3 inner values",inner[:3],
      [F(311,2352),F(383,2352),F(1,14)])
check("Gauss B3 odd pairing",inner[3:],[-inner[2],-inner[1],-inner[0]])
weighted = sum(w*b for w,b in zip(weights,inner))
check("weighted Gauss B3 sum",weighted,F(275,294))
Ftate = F(12,21)*weighted
check("kappa F-character Tate coefficient",Ftate,F(550,1029))
check("C-plus Tate coefficient",Etate+Ftate,F(586,1029))

a,b,c,d=1217,-14082,6255,2880
check("source infinity constant",-143*a-8*b-F(7,9)*c+23*d,0)
check("source zeta-three coefficient",-110*a-10*b-F(10,9)*c,0)
check("source Tate coefficient",triv[0]*a+triv[1]*b+triv[2]*c+(Etate+Ftate)*d,0)
check("nonzero retained character coefficient",d,2880)
check("Theta multiplier",12*d,34560)
source={1:a,2:b,3:c,4:-F(16,9)*c,6:-9*b,12:-144*a}
check("complete integer trivial expansion",[source[j] for j in (1,2,3,4,6,12)],
      [1217,-14082,6255,-11120,126738,-175248])
check("integer character sqrt-three multiplier",-24*d,-69120)
check("trivial first Dirichlet factor",sum(u/F(j) for j,u in source.items()),0)
check("trivial second Dirichlet factor",sum(u/F(j)**2 for j,u in source.items()),0)
check("trivial third Dirichlet factor",sum(u/F(j)**3 for j,u in source.items()),0)
check("radial pole cancellation",240*sum(u/F(j)**4 for j,u in source.items()),F(115*d,3))
check("ordinary W conjugate constant",46*d,132480)
check("ordinary W conjugate L2 / pi squared",F(-2*d,3),-1920)
check("ordinary W reciprocal / i pi cubed",F(8*132480,6*12**2),F(3680,3))

z,v,s,h=sp.symbols("z v s h")
gamma=sp.Matrix([[7,2],[24,7]])
W=sp.Matrix([[0,-1],[12,0]])
M=sp.Matrix([[24,-7],[84,-24]])
check("actual M equals gamma W",gamma*W,M)
check("actual M central square",M*M,-12*sp.eye(2))
tau=z+sp.Rational(2,7)
Mtau=(24*tau-7)/(84*tau-24)
check("actual centered M",sp.factor(Mtau-sp.Rational(2,7)), -1/(588*z))
P0,P1,P2=sp.symbols("P0 P1 P2")
period=P0+P1*z+P2*z*z
trans=sp.expand(588*z*z*period.subs(z,-1/(588*z))-period)
eigenspace=sp.solve(sp.Poly(trans,z).coeffs(),[P1,P2],dict=True)
check("plus period eigenline",eigenspace,[{P1:0,P2:588*P0}])

divisors=(1,2,3,4,6,12)
exponents=(3,-2,-1,1,2,-3)
order_matrix=sp.Matrix([[sp.Rational(12*gcd(c,j)**2,24*gcd(c,12//c)*c*j)
                        for j in divisors] for c in divisors])
orders=order_matrix*sp.Matrix(exponents)
check("eta h cusp divisor",list(orders),[1,0,0,0,0,-1])
check("eta h weight",sum(exponents),0)
check("eta h two congruences",(sum(j*r for j,r in zip(divisors,exponents))%24,
      sum((12//j)*r for j,r in zip(divisors,exponents))%24),(0,0))
eta_units={}
cusp_values={}
for index,cusp in enumerate(divisors[:-1]):
    target=sp.zeros(6,1);target[index]=1;target[5]=-1
    vector=list(order_matrix.inv()*target)
    check("cusp eta exponents integral "+str(cusp),all(r.q==1 for r in vector))
    check("cusp eta weight and congruences "+str(cusp),
          (sum(vector),sum(j*r for j,r in zip(divisors,vector))%24,
           sum((12//j)*r for j,r in zip(divisors,vector))%24),(0,0,0))
    prod=sp.prod(sp.Rational(j)**r for j,r in zip(divisors,vector))
    check("cusp eta square character "+str(cusp),sp.sqrt(prod).is_Rational,True)
    eta_units[str(cusp)]=[int(r) for r in vector]
    cusp_values[cusp]=vector[0]-3
check("independent cusp constant calculation",[cusp_values[c] for c in divisors[:-1]],
      [0,-6,-4,-3,-2])
check("eta Fricke exponent reversal",list(reversed(exponents)),[-r for r in exponents])
check("eta Fricke positive prefactor",sp.prod(sp.Rational(j)**r for j,r in zip(divisors,exponents)),sp.Rational(1,144))
widths={c:12//gcd(c*c,12) for c in divisors}
cusp_chars=[chi(1+c*widths[c]) for c in divisors]
check("six exact parabolic character values",cusp_chars,[1,-1,1,1,-1,1])

def red(expr):
    num,den=sp.fraction(sp.factor(expr))
    num=sp.rem(sp.Poly(num,s),sp.Poly(s*s-3,s)).as_expr()
    den=sp.rem(sp.Poly(den,s),sp.Poly(s*s-3,s)).as_expr()
    if num == 0: return sp.Integer(0)
    den0=den.subs(s,0);den1=sp.diff(den,s)
    top=sp.rem(sp.Poly(sp.expand(num*(den0-den1*s)),s),sp.Poly(s*s-3,s)).as_expr()
    return sp.factor(top/(den0*den0-3*den1*den1))
hv=(6-2*v*v)/(v*v-1)
R=lambda arg:(arg+6)/(arg+2)
check("actual cover rational parameter",sp.factor(R(hv)-v*v),0)
check("Fricke square transformation",sp.factor(R(12/h)-3/R(h)),0)
check("Fricke h action from v action",red(hv.subs(v,s/v)-12/hv),0)
u=sp.symbols("u")
xu=u*(1+u)/(1-2*u-2*u*u)
check("integer u equation",sp.factor(1/hv.subs(v,1+2*u)-xu),0)
tm=u*(1-(1+s)*u)/(1+2*u)
tp=u*(1-(1-s)*u)/(1+2*u)
tmv=(v+s/v-1-s)/(2*(1-s))
tpv=(v-s/v-1+s)/(2*(1+s))
check("two t-minus formulas",red(tmv.subs(v,1+2*u)-tm),0)
check("two t-plus formulas",red(tpv.subs(v,1+2*u)-tp),0)
check("t-minus actual W invariance",red(tmv.subs(v,s/v)-tmv),0)
check("t-plus actual M invariance",red(tpv.subs(v,-s/v)-tpv),0)
check("both quotient local leading",(sp.limit(tm/u,u,0),sp.limit(tp/u,u,0)),(1,1))
check("W paired zero cusps",(red(tmv.subs(v,1)),red(tmv.subs(v,s))),(0,0))
check("W paired other real cusps",(red(tmv.subs(v,-1)),red(tmv.subs(v,-s))),(2+s,2+s))
check("W paired complex cusp one",red(tmv.subs(v,sp.I)-(2+s+sp.I)/2),0)
check("W paired complex cusp two",red(tmv.subs(v,-sp.I)-(2+s-sp.I)/2),0)
aa=sp.symbols("aa",positive=True)
branchminus=tmv.subs({s:aa**2,v:aa})
branchminus_other=tmv.subs({s:aa**2,v:-aa})
check("first W branch",sp.factor(branchminus), (aa-1)/(2*(aa+1)))
check("second W branch",sp.factor(branchminus_other), (aa+1)/(2*(aa-1)))
check("W branch product",sp.factor(branchminus*branchminus_other),sp.Rational(1,4))
branchplus=tpv.subs({s:aa**2,v:sp.I*aa})
check("M branch formula",sp.factor(branchplus), (aa**2-1+2*sp.I*aa)/(2*(1+aa**2)))
check("M branch absolute square",sp.factor(branchplus*sp.conjugate(branchplus)),sp.Rational(1,4))

# Fixed order-12 eta/formal checks. The all-order assertions are proved
# recursively in the report; these coefficients are only corroboration.
NN=12
ZERO=(F(0),F(0)); ONE=(F(1),F(0))
def ka(x): return (F(x),F(0)) if not isinstance(x,tuple) else x
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def inv(a):
    n=a[0]*a[0]-3*a[1]*a[1]
    return(a[0]/n,-a[1]/n)
def sa(a,b):return[add(x,y) for x,y in zip(a,b)]
def scale(a,c):return[mul(x,ka(c)) for x in a]
def sm(a,b):
    r=[ZERO]*(NN+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b[:NN+1-i]):r[i+j]=add(r[i+j],mul(x,y))
    return r
def sinv(a):
    r=[ZERO]*(NN+1);r[0]=inv(a[0])
    for n in range(1,NN+1):
        q=ZERO
        for j in range(1,n+1):q=add(q,mul(a[j],r[n-j]))
        r[n]=neg(mul(r[0],q))
    return r
def compose(a,b):
    r=[ZERO]*(NN+1);power=[ONE]+[ZERO]*NN
    for c in a:r=sa(r,scale(power,c));power=sm(power,b)
    return r
def reverse(a):
    assert a[0]==ZERO and a[1]==ONE
    r=[ZERO]*(NN+1);r[1]=ONE
    for n in range(2,NN+1):r[n]=neg(compose(a,r)[n])
    return r
def integral(a):return all(c[0].denominator==c[1].denominator==1 for c in a)
eta=[ONE]+[ZERO]*NN
for j,e in zip(divisors,[-r for r in exponents]):
    for m in range(1,NN//j+1):
        fact=[ZERO]*(NN+1)
        for k in range(NN//(j*m)+1):
            bc=sp.binomial(e,k)*(-1)**k
            fact[j*m*k]=(F(int(bc)),F(0))
        eta=sm(eta,fact)
xq=[ZERO]+eta[:NN]
uq=[ZERO]*(NN+1)
for n in range(1,NN+1):
    residual=sa(sa(uq,sm(uq,uq)),scale(xq,-1))
    residual=sa(residual,scale(sm(xq,uq),2))
    residual=sa(residual,scale(sm(xq,sm(uq,uq)),2))
    uq[n]=neg(residual[n])
den=sa([ONE]+[ZERO]*NN,scale(uq,2))
tminus=sm(sa(uq,scale(sm(uq,uq),(-F(1),-F(1)))),sinv(den))
tplus=[(c[0],-c[1]) for c in tminus]
qminus=reverse(tminus);qplus=reverse(tplus)
check("fixed eta x first five",[c[0] for c in xq[1:6]],[1,3,7,15,30])
check("fixed integral u and its inverse",integral(uq) and integral(reverse(uq)))
check("fixed integral both t and both inverses",all(integral(a) for a in (tminus,tplus,qminus,qplus)))
check("fixed t-minus inverse identity",compose(tminus,qminus),[ZERO,ONE]+[ZERO]*(NN-1))
check("fixed t-plus inverse identity",compose(tplus,qplus),[ZERO,ONE]+[ZERO]*(NN-1))
check("fixed exact coefficient conjugacy",qplus,[(a,-b) for a,b in qminus])

cuspF=sum(u*F(gcd(2,j),j)**4 for j,u in source.items())
cuspA=1-12*F(2,12)**2
check("irregular cusp source nonzero constant",cuspF,F(-36160,3))
check("irregular cusp gauge constant",cuspA,F(2,3))
check("actual log-cubed leading coefficient",cuspF*cuspA/6,F(-36160,27))

snapshot={"fixed_source":{"a":a,"b":b,"c":c,"d":d},
 "ordinary_B3_Tate":{str(k):str(v) for k,v in T.items()},
 "Etate":str(Etate),"kappa_Ftate":str(Ftate),"eta_units":eta_units,
 "parabolic_characters":cusp_chars,
 "tminus_first_12":[[str(a),str(b)] for a,b in tminus[1:]],
 "q_of_tminus_first_12":[[str(a),str(b)] for a,b in qminus[1:]],
 "cusp_log_cubed_coefficient":str(cuspF*cuspA/6)}
out={"scope":"one fixed D12 source, endpoint, cusp model and order-12 formal check; no scans",
     "check_count":len(checks),"checks":checks,"snapshot":snapshot,
     "all_passed":all(c["passed"] for c in checks)}
output=Path(__file__).with_suffix(".json")
output.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"check_count":len(checks),"all_passed":out["all_passed"],"output":str(output)},ensure_ascii=False))
