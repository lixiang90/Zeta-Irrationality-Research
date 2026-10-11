"""Exact certificate for a ramified Catalan pullback; no parameter scan."""
from pathlib import Path
import json
import sympy as S

s=S.symbols('s')
t=s**4
rho=4*t/(1+t)**2
T=S.factor(rho/S.diff(rho,s))
th=lambda v:S.factor(T*S.diff(v,s))
L2=lambda v:S.factor((1-rho)*th(th(v))+(1-S.Rational(3,2)*rho)*th(v)+(S.Rational(3,16)-rho/2)*v)
y1=(1+t)/s
y2=(1+t)/s**3
assert L2(y1)==0 and L2(y2)==0
lead=S.factor((1-rho)*T**2)
assert lead==s**2/16
wronskian=S.factor(y1*S.diff(y2,s)-S.diff(y1,s)*y2)
v1=S.factor(-y2/(32*lead*wronskian))
v2=S.factor(y1/(32*lead*wronskian))
assert S.cancel(v1-1/(4*(1+t)))==0 and S.cancel(v2+s**2/(4*(1+t)))==0

Ab=S.Function('A')(s)
Bb=S.Function('B')(s)
Fpull=(y1*Ab-y2*Bb)/4
rules={S.diff(Ab,s):1/(1+t),S.diff(Bb,s):s**2/(1+t)}
dp=lambda v:S.factor(S.diff(v,s).subs(rules))
thetaF=S.factor(T*dp(Fpull))
theta2F=S.factor(T*dp(thetaF))
L2_F=S.factor((1-rho)*theta2F+(1-S.Rational(3,2)*rho)*thetaF+(S.Rational(3,16)-rho/2)*Fpull)
assert L2_F==S.Rational(1,32)

Q=t**2-14*t+1
K=32*s**3*(1-t)/((1+t)*Q)
PA=-4*s**2*(7-t)/Q
PB=4*(1-7*t)/Q
Rpull=S.factor(6*thetaF+5*Fpull)
assert S.factor(-K*Rpull-PA*Ab-PB*Bb)==0
assert S.factor(K-S.diff(S.log((1+t)/S.sqrt(Q)),s))==0

# A cyclic vector test after the separate actual-function independence proof.
M=S.Matrix([[0,0,0,0],[1/(1+t),0,0,0],[s**2/(1+t),0,0,0],[0,PA,PB,K]])
rows=[S.Matrix([[0,0,0,1]])]
for _ in range(3):
    rows.append((rows[-1].diff(s)+rows[-1]*M).applyfunc(S.factor))
det=S.factor(S.Matrix.vstack(*rows).det())
assert det!=0
assert S.gcd(Q,S.diff(Q,s))==1 and S.degree(Q,s)==8

# Fixed origin jet verifies the unique analytic branch and normalization.
order=25
Aj=sum(S.Rational((-1)**n,4*n+1)*s**(4*n+1) for n in range(7))
Bj=sum(S.Rational((-1)**n,4*n+3)*s**(4*n+3) for n in range(7))
jet=S.series((y1*Aj-y2*Bj)/4,s,0,order).removeO()
expected=S.series(sum(16**n*S.factorial(2*n)*S.factorial(2*n+1)/S.factorial(4*n+3)*rho**n for n in range(7)),s,0,order).removeO()
assert S.expand(jet-expected)==0
assert jet.subs(s,0)==S.Rational(1,6)

result={
 'cover':str(rho),'theta_pullback':str(T)+' * d/ds',
 'homogeneous_rational_solutions':[str(y1),str(y2)],
 'second_derivative_leading_coefficient':str(lead),
 'wronskian':str(wronskian),'variation_coefficients':[str(v1),str(v2)],
 'L2_F_pullback':str(L2_F),'system_matrix':str(M),'cyclic_determinant':str(det),
 'homogeneous_curve_polynomial':str(Q),'curve_squarefree':True,
 'curve_degree':8,'smooth_projective_hyperelliptic_genus':3,
 'scope':'Actual independence and continuation are proved separately; no global slit-domain assertion.',
 'all_checks_passed':True
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
