"""Exact Rouché certificate and outward-rounded saddle inputs; no finite asymptotic fitting."""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sympy as s
from flint import arb, acb, ctx

ctx.prec = 256
HERE = Path(__file__).resolve()
REPORT = HERE.with_name("odd_zeta_log_saddle_20261005.md")
OUT = HERE.with_suffix(".json")
w, v = s.symbols("w v")
P = w**8 + (w-1)**7*(w+7)
center = s.Rational(11128732, 10**7) + s.I*s.Rational(15247965, 10**7)
radius = s.Rational(1, 10**6)
shifted = s.Poly(s.expand(P.subs(w,center+v)), v)
def norm_one(z):
    return abs(s.re(z)) + abs(s.im(z))
def norm_lower(z):
    return max(abs(s.re(z)), abs(s.im(z)))
coeff = [s.expand(shifted.nth(j)) for j in range(9)]
rouche_left = norm_one(coeff[0]) + sum(norm_one(coeff[j])*radius**j for j in range(2,9))
rouche_right = norm_lower(coeff[1])*radius
assert rouche_left < rouche_right
rouche = {
    "center": str(center), "radius": str(radius),
    "exact_l1_upper_left": str(rouche_left), "exact_component_lower_right": str(rouche_right),
    "passed": True, "conclusion": "exactly one zero in the disk by Rouche",
}

checks = {}
def check(name, flag):
    assert flag, name
    checks[name] = True

Fprime = 8/w - 7/(w-1) - 1/(w+7)
check("F_double_prime_rational_identity", s.cancel(Fprime + 56/(w*(w-1)*(w+7))) == 0)
# Gamma recurrence product factors at fixed prescribed inputs.
z = s.symbols("z")
gamma_cases = []
for q,n in ((7,1),(3,2)):
    N=q*n
    rational=s.Rational((-1)**N*s.factorial(N),s.factorial(n)**q)*s.prod((z-j)**q for j in range(1,n+1))/s.prod(z+r for r in range(N+1))
    recurrence=s.Rational((-1)**N*s.factorial(N),s.factorial(n)**q)*s.rf(z-n,n)**q/s.rf(z,N+1)
    check("Gamma_recurrence_q%d_n%d"%(q,n),s.cancel(rational-recurrence)==0)
    gamma_cases.append({"q":q,"n":n,"passed":True})
check("connector_rational_bound", 9*s.Rational(3,5)**7 < 1)
pi=s.pi
C0=s.sqrt(7)/(2*pi)**3
full_constant=2*pi**6*C0*s.sqrt(2*pi)/s.factorial(6)
check("full_gaussian_prefactor",s.simplify(full_constant-s.sqrt(7)*pi**3*s.sqrt(2*pi)/2880)==0)
check("Stirling_power_n",s.Rational(1)-4-s.Rational(1,2)==-s.Rational(7,2))

ball=acb(arb("1.1128732 +/- 0.000001"),arb("1.5247965 +/- 0.000001"))
a,b=ball.real,ball.imag
def F(z):
    return 7*arb(7).log()+8*z*z.log()-7*(z-1)*(z-1).log()-(z+7)*(z+7).log()
H=F(ball)+acb(0,arb.pi())*ball
fp=8*ball.log()-7*(ball-1).log()-(ball+7).log()
fpp=-56/(ball*(ball-1)*(ball+7))
h=(ball-1)**arb("3.5")/(ball**4*(ball+7).sqrt())
D=acb(0,1)*arb(7).sqrt()*arb.pi()**3*(2*arb.pi()).sqrt()/2880*h/fpp.sqrt()
Hhalf=F(acb(a,arb("0.5")))+acb(0,arb.pi())*acb(a,arb("0.5"))
Fzero=F(acb(a))
turn=a*(a-1)*(a+7)/(3*a+6)
theta=H.imag-3*arb.pi()
check("right_upper_root_rectangle",a>arb("1.1128") and a<arb("1.1130") and b>arb("1.5247") and b<arb("1.5249"))
check("positive_peak_A",H.real>arb("1.817") and H.real<arb("1.819"))
check("Omega_interval",H.imag>arb("9.177") and H.imag<arb("9.179"))
check("log_branch_Fprime",fp.imag>arb(-4) and fp.imag<arb(-2))
check("nondegenerate_gaussian",fpp.real>arb(2))
check("connector_origin_less_zero",Fzero.real<arb(0))
check("connector_half_less_one",Hhalf.real<arb(1))
check("saddle_beyond_turn",b*b-turn>arb(0))
check("nonzero_complex_amplitude",D.real<arb("-0.005") and D.imag>arb("0.002"))
check("phase_sine_nonzero",theta>arb("-0.25") and theta<arb("-0.24") and theta.sin()<arb("-0.24"))
Lambda=-(7*(ball-1)/(ball+7))**7
check("algebraic_growth_factor_nonreal",Lambda.imag<arb(-1) and abs(Lambda)>arb(6))
f_t=lambda t:(7-t)*(1+t)**7-t**8
check("real_B_saddle_root_bracket",f_t(s.Rational(5373,1000))>0 and f_t(s.Rational(5374,1000))<0)
B_height_upper=7*(7*(1+arb("5.374"))/(7-arb("5.374"))).log()
check("real_B_height_upper",B_height_upper<arb("23.19"))
check("conditional_budget_strict_positive",s.Rational(1817,1000)+42-s.Rational(2319,100)-7*s.Rational(294,100)>0)

result = {
    "status":"saddle_input_certificates_passed", "as_of":"2026-10-05",
    "precision_bits":ctx.prec, "rouche":rouche, "checks":checks,
    "root_enclosure":str(ball), "H_enclosure":str(H), "Fprime_enclosure":str(fp),
    "Fdouble_enclosure":str(fpp), "amplitude_enclosure":str(D),
    "theta_enclosure":str(theta), "sine_theta_enclosure":str(theta.sin()),
    "algebraic_Lambda_enclosure":str(Lambda),
    "real_B_height_upper_at_bracket_endpoint":str(B_height_upper),
    "connector_origin_enclosure":str(Fzero), "connector_half_enclosure":str(Hhalf),
    "gamma_product_cases":gamma_cases,
    "written_proof_sha256":hashlib.sha256(REPORT.read_bytes()).hexdigest(),
    "scope":(
        "Exact rational Rouche bound proves a zero exists in a specified disk. Arb/Acb bounds "
        "enclose the whole disk and certify branches, positive peak and amplitude inputs. "
        "Contour deformation, global maximum, uniform tails and all-scale Gaussian asymptotics "
        "rely on the written proof, not numerical integral fitting. No irrationality or Lean theorem."
    ),
}
OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"exact_rouche":True,"checks":len(checks),"A":str(H.real)},ensure_ascii=False))

