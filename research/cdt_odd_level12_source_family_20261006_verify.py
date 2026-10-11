"""New fixed exact algebra for the D12 source family; no scans or old producers."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp

checks = []
def check(label, expr, expected=0):
    ok = sp.simplify(expr - expected) == 0
    checks.append({"label": label, "passed": bool(ok)})
    if not ok:
        raise AssertionError(label)

r = sp.sqrt(3)
Z, d, B, C = sp.symbols("Z d B C")
a = 7*Z/480 + sp.Rational(1217,2880)*d
b = -21*Z/80 - sp.Rational(2347,480)*d
c = 3*Z/160 + sp.Rational(139,64)*d
check("family infinity constant",143*a+8*b+sp.Rational(7,9)*c-23*d)
check("family ordinary third period",-110*a-10*b-sp.Rational(10,9)*c,Z)
check("family canonical conjugate Tate coefficient",
      sp.Rational(960,343)*a+sp.Rational(40,343)*b-sp.Rational(80,147)*c+
      sp.Rational(586,1029)*d)
check("family irregular cusp constant",sp.Rational(8,81)*(9*a+9*b-c),
      -(6*Z+113*d)/27)

zchoice = {Z:103680,d:0}
lchoice = {Z:0,d:2880}
joint = {Z:103680*B,d:2880*r*C}
for label, choice, expected in [
    ("zeta",zchoice,(1512,-27216,1944)),
    ("pure L",lchoice,(1217,-14082,6255)),
    ("joint",joint,(1512*B+1217*r*C,-27216*B-14082*r*C,1944*B+6255*r*C))
]:
    for index,(expr,value) in enumerate(zip((a,b,c),expected)):
        check(label+" source coordinate "+str(index),expr.subs(choice),value)
check("joint original character period",12*r*(2880*r*C),103680*C)
check("joint actual conjugate character period",-12*r*(-2880*r*C),103680*C)
check("joint irregular cusp constant",(-(6*Z+113*d)/27).subs(joint),
      -(622080*B+325440*r*C)/27)
check("joint log cubed coefficient",(-(6*Z+113*d)/27).subs(joint)*sp.Rational(2,3)/6,
      -(622080*B+325440*r*C)/243)

zold = {1:1512,2:-27216,3:1944,4:-3456,6:244944,12:-217728}
lold = {1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
check("zeta source constant",sum(zold.values()))
check("zeta source period",sum(sp.Rational(v,j**3) for j,v in zold.items())*-120,
      103680)
check("zeta source first Dirichlet factor",sum(sp.Rational(v,j) for j,v in zold.items()),10368)
check("pure L source ordinary third zero",sum(sp.Rational(v,j**3) for j,v in lold.items()))

eps, P = sp.symbols("eps P")
fp = 240*1217*(1+P**3)+2880*(1+eps*P**3)-69120*r*(eps+P**3)
alpha = 294960-69120*r*eps
beta = 292080+2880*eps-69120*r
check("pure L pth coefficient identity",fp,alpha+P**3*beta)
norm = 294960**2-3*69120**2
check("pure L main norm",norm,72668678400)
check("fixed norm factorization",2**8*3**2*5**2*419*3011,norm)
f1 = 240*1217+2880-69120*r
f2 = 240*9*1217-240*14082+2880-8*69120*r
check("pure L first coefficient",f1,294960-69120*r)
check("pure L second coefficient",f2,-748080-552960*r)
det = sp.expand(f1*f2.xreplace({r:-r})-f2*f1.xreplace({r:-r}))
# Substitution at the explicit sqrt is kept separate from any unknown periods.
sig1 = 294960+69120*r
sig2 = -748080+552960*r
check("source pair fixed minor",f1*sig2-f2*sig1,429616742400*r)
check("gauge first denominator carrier",-24*alpha,-7079040+1658880*r*eps)

U,X,Y,VU,VX,VY = sp.symbols("U X Y VU VX VY")
up = (1+P**3)*U-P**3*VU+(1+eps*P**3)*X-eps*P**3*VX+\
     (eps+P**3)*Y-eps*P**3*VY
R = U+X+eps*Y
S = U+eps*X+Y
Tvp = VU+eps*VX+eps*VY
check("exact whole source Hecke decomposition",up,R+P**3*S-P**3*Tvp)
check("plus source leading",R.subs(eps,1),U+X+Y)
check("minus source leading",R.subs(eps,-1),U+X-Y)
data = {
    "check_count":len(checks),"all_passed":all(x["passed"] for x in checks),
    "checks":checks,
    "results":{"main_norm":norm,"source_pair_minor":"429616742400*sqrt(3)",
               "joint_period":"103680*(B*zeta(3)+C*L(3,chi12))"},
    "scope":["one fixed symbolic two-period family","fixed source norm and first two coefficients",
             "no prime or parameter scan","no old producer execution",
             "finite algebra supplements global proofs","no new numerical irrationality theorem"]
}
Path(__file__).with_suffix(".json").write_text(json.dumps(data,indent=2),encoding="utf-8")
print(json.dumps({"check_count":len(checks),"all_passed":data["all_passed"]}))
