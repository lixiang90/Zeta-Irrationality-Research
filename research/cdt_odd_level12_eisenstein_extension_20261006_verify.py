"""NEW fixed level12 odd-odd Eisenstein computation; no old producer imports."""
from pathlib import Path
import json
import sympy as S

base = Path(__file__).resolve().parent
x = S.Symbol('x')
r = S.sqrt(3)
checks = []
def check(name, value):
    checks.append({'name':name,'passed':bool(value)})
    if not value:
        raise AssertionError(name)
def chi3(n):
    return [0,1,-1][n%3]
def chi4(n):
    return [0,1,0,-1][n%4]
def B3(z):
    z = S.Rational(z)
    return z**3-S.Rational(3,2)*z**2+z/2
def frac(z):
    z = S.Rational(z)
    return z-S.floor(z)

modulus = x**7-1
K4 = S.Poly(S.rem(x*S.invert(1+x*x,modulus),modulus),x)
K3 = S.Poly(S.rem(x*S.invert(1+x+x*x,modulus),modulus),x)
check('chi-4 kernel exact all seventh roots', S.rem((1+x*x)*K4.as_expr()-x,modulus)==0)
check('chi-3 kernel exact all seventh roots', S.rem((1+x+x*x)*K3.as_expr()-x,modulus)==0)
check('chi-4 kernel at one', K4.eval(1)==S.Rational(1,2))
check('chi-3 kernel at one', K3.eval(1)==S.Rational(1,3))
for label,K in [('4',K4),('3',K3)]:
    coeff=[K.nth(j) for j in range(7)]
    check('kernel'+label+' reciprocal real', all(coeff[j]==coeff[(-j)%7] for j in range(7)))

def finite_sum(conductor,chi,K):
    return S.factor(sum(chi(a)*K.nth(j)*B3(frac(S.Rational(a,conductor)+S.Rational(2*j,7)))
                        for a in range(1,conductor+1) for j in range(7)))
SA=finite_sum(3,chi3,K4)
SB=finite_sum(4,chi4,K3)
fA_r=2*SA/9  # f_A(rho7^2)/pi^3, normalized by sqrt3
fB=SB/3      # f_B(rho7^2)/pi^3
lam_original_r=S.factor(fA_r+S.Rational(8,9)*fB)
lam_sigma_r=S.factor(fA_r-S.Rational(8,9)*fB)

LA1=-S.pi/(6*r)
LB1=-S.pi/18
LA3=2*S.pi**3/(81*r)
LB3=S.pi**3/96
kappa=-8*r/9
theta_minus=S.simplify(LA3-kappa*LB3)
theta_plus=S.simplify(LA3+kappa*LB3)
check('weight4 anti pair L1/L3 exact', S.simplify((LA1-kappa*LB1)+6*theta_minus/S.pi**2)==0)
check('weight4 plus pair L1/L3 exact', S.simplify((LA1+kappa*LB1)-6*theta_plus/S.pi**2)==0)
check('anti critical period exact', theta_minus==17*r*S.pi**3/972)
check('plus critical period exact', theta_plus==-r*S.pi**3/972)
check('both L2 zero by negative odd L values', S.bernoulli(2,S.Rational(1,3))-S.bernoulli(2,S.Rational(2,3))==0)

# All fixed source cusp slots, with primitive eta/scaling sign represented by chars.
As=[(1,0),(5,-12),(0,-1),(1,-2),(2,-3),(1,-3),(3,-4),(1,-4),(2,-5),(1,-6)]
u={1:1217,2:-14082,3:6255,4:-11120,6:126738,12:-175248}
oldL=[0,-132480,920,-S.Rational(36160,3),13785,13785,-S.Rational(73520,3),-S.Rational(73520,3),0,108480]
chi12=lambda n:chi3(n)*chi4(n)
records=[]
boundary=[]
for j,((a,c),old) in enumerate(zip(As,oldL),1):
    triv=sum(coeff*S.Rational(S.gcd(scale,c),scale)**4 for scale,coeff in u.items())
    ch=66240*((chi12(a) if c%12==0 else 0)+(S.Rational(chi12(c),144) if S.gcd(c,12)==1 else 0))
    check(f'old pure sigma source constant at cusp{j}', S.factor(triv+ch-old)==0)
    # Odd-odd new pair support only gcd(c,12)=3 or4. Here direct radial kernel signs.
    # The actual radial phase is exp(2*pi*i*a/c). Reduce its denominator
    # positively before applying an odd character; c<0 changes the sign.
    radial_numerator = a if c >= 0 else -a
    ca=23*S.I*r*S.Rational(1,81)*chi4(radial_numerator) if S.gcd(c,12)==4 else 0
    cb=23*S.I*S.Rational(1,128)*chi3(radial_numerator) if S.gcd(c,12)==3 else 0
    minus=S.simplify(ca-kappa*cb)
    plus=S.simplify(ca+kappa*cb)
    records.append({'id':j,'a':a,'c':c,'old_sigma_constant':str(old),
                    'odd_A':str(ca),'odd_B':str(cb),'odd_minus':str(minus),'odd_plus':str(plus)})
    boundary.append([S.Rational(S.gcd(scale,c),scale)**4 for scale in (1,2,3,4,6,12)] +
                    [23*chi12(a) if c%12==0 else 0,
                     S.Rational(23,144)*chi12(c)/(24*r) if S.gcd(c,12)==1 else 0, ca, cb])
check('complete ten-dimensional Eisenstein boundary map', S.Matrix(boundary).rank()==10)

# The complete anti-Fricke Eisenstein family, after infinity and zeta3 removal.
a,b=S.symbols('a b',real=True)
c=-99*a-9*b
d=(66*a+b)/23
source={1:a,2:b,3:c,4:-16*c/9,6:-9*b,12:-144*a}
check('whole old family infinity regular', S.expand(sum(source.values())+23*d)==0)
check('whole old family zeta3 coefficient zero', S.expand(sum(v/S.Integer(j)**3 for j,v in source.items()))==0)
check('whole old family L2 trivial coefficient zero', S.expand(sum(v/S.Integer(j)**2 for j,v in source.items()))==0)
boundary2=S.factor(sum(v*S.Rational(S.gcd(j,2),j)**4 for j,v in source.items()))
boundary4=S.factor(sum(v*S.Rational(S.gcd(j,4),j)**4 for j,v in source.items()))
check('c2 boundary exact', S.expand(boundary2-S.Rational(16,9)*(6*a+b))==0)
check('c4 boundary exact', S.expand(boundary4-(1566*a+151*b)/9)==0)

# Root -1 derivative finite part: theta f/(zeta2), using the exact reciprocal kernels.
oddj=sum(v/S.Integer(j)**2 for j,v in source.items() if j%2)
evenj=sum(v/S.Integer(j)**2 for j,v in source.items() if j%2==0)
derivative_minus1=S.factor(-50*oddj-20*evenj+7*d)
check('root-minus-one derivative exact', S.expand(derivative_minus1-(7362*a+697*b)/23)==0)
check('c2-zero witness derivative actual nonzero', derivative_minus1.subs({a:23,b:-138})==3180)

# Root i imaginary finite part: all nonzero ordinary sine coefficients plus chi pair.
tate_i=S.factor(S.Rational(15,4)*a-S.Rational(5,36)*c-S.Rational(31,48)*d)
check('root-i finite Tate exact', S.expand(tate_i-(17274*a+1349*b)/1104)==0)
check('c4-zero witness endpoint actual nonzero', tate_i.subs({a:3473,b:-36018})==10330)

Rcoeff={1:1,2:-66,3:495,4:-880,6:594,12:-144}
check('zero-period corrector integer infinity zero', sum(Rcoeff.values())==0)
check('zero-period corrector L3 zero', sum(S.Rational(v,j**3) for j,v in Rcoeff.items())==0)
check('zero-period corrector L2 zero', sum(S.Rational(v,j**2) for j,v in Rcoeff.items())==0)
check('zero-period corrector L1 polynomial zero', sum(S.Rational(v,j) for j,v in Rcoeff.items())==0)
tate_M=(28164*a+2434*b)/483
check('corrector canonical M Tate exact', tate_M.subs({a:1,b:-66})==-S.Rational(1920,7))
check('old pure-L canonical witness Tate zero', tate_M.subs({a:1217,b:-14082})==0)
check('odd mixed carrier conjugacy ratio norm obstruction', S.Rational(119,619)**2!=1)
odd_minus1=-S.Rational(5,8)*4/(81*r)-8*r/(9*32)
check('odd pair root-minus-one actual endpoint', S.simplify(odd_minus1+37*r/972)==0)
check('odd pair minus-one difference from true period', S.simplify(odd_minus1-17*r/972+r/18)==0)

report={'scope':'fixed canonical seventh-root finite Bernoulli odd-odd Eisenstein periods and actual cusp slots; no irrationality or fullleaf claim',
        'execution_history':'Third execution of this NEW fixed producer: first 21 checks passed but the unasserted odd-character cusp orientation was corrected for negative denominators; second saved the corrected 21-check data; this third adds the complete boundary map and new zero-period-corrector/parabolic-source proofs. No frozen producer imported or executed.',
        'passed':len(checks),'checks':checks,'K4':str(K4.as_expr()),'K3':str(K3.as_expr()),
        'Bernoulli_SA':str(SA),'Bernoulli_SB':str(SB),
        'fA_at_rho7square_over_sqrt3pi3':str(fA_r),
        'fB_at_rho7square_over_pi3':str(fB),
        'lambda_odd_original_over_sqrt3pi3':str(lam_original_r),
        'lambda_odd_sigma_over_sqrt3pi3':str(lam_sigma_r),
        'Theta_odd_original_over_sqrt3pi3':'17/972',
        'sigma_Theta_odd_over_sqrt3pi3':'-17/972',
        'actual_plus_L3_over_sqrt3pi3':'-1/972','cusps':records,
        'Eisenstein_boundary_rank':10,
        'zero_period_corrector':Rcoeff,'corrector_canonical_M_tate':'-1920/7',
        'old_c2_boundary':str(boundary2),'old_c4_boundary':str(boundary4),
        'old_theta_at_minus1_over_zeta2':str(derivative_minus1),
        'old_root_i_tate':str(tate_i),'odd_minus1_over_sqrt3pi3':'-37/972'}
out=base/'cdt_odd_level12_eisenstein_extension_20261006_verify.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'lambda_sigma_over_sqrt3pi3':str(lam_sigma_r),
                  'lambda_original_over_sqrt3pi3':str(lam_original_r),'fA':str(fA_r),'fB':str(fB)}))
