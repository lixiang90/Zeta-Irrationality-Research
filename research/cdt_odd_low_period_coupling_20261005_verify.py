"""Exact fixed checks for the real chi_5, level-10 period coupling.

This certificate checks algebraic identities, normalizations and complete
fixed prefixes. The report supplies analytic proofs. It is not an
irrationality certificate or a proof of a global CDT rank inequality.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import lcm
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks: list[dict] = []


def check(name: str, condition: bool, detail=None) -> None:
    if not condition:
        raise AssertionError(name)
    entry = {"name": name, "passed": True}
    if detail is not None:
        entry["detail"] = detail
    checks.append(entry)


def chi(n: int) -> int:
    return 0 if n % 5 == 0 else (1 if n % 5 in (1, 4) else -1)


def frac(x: Q) -> Q:
    return x - x.numerator // x.denominator


def b3(x: Q) -> Q:
    x = frac(x)
    return x**3 - Q(3, 2) * x**2 + Q(1, 2) * x


def chars_bernoulli(k: int):
    return sp.Rational(5) ** (k - 1) * sum(
        chi(a) * sp.bernoulli(k, sp.Rational(a, 5)) for a in range(1, 5)
    )


sqrt5 = sp.sqrt(5)
pi = sp.pi
J, Lphi, tau = sp.symbols("J Lphi tau")
check("chi_even_and_mean_zero", chi(-1) == 1 and sum(chi(a) for a in range(5)) == 0)
check("E2_chi_constant", sp.simplify(-chars_bernoulli(2) / 4) == -sp.Rational(1, 5))
check("E4_chi_constant", sp.simplify(-chars_bernoulli(4) / 8) == 1)
check("L_chi_minus1", -chars_bernoulli(2) / 2 == -sp.Rational(2, 5))
check("L_chi_minus3", -chars_bernoulli(4) / 4 == 2)

x = sp.symbols("x")
phi5 = sp.cyclotomic_poly(5, x)
gauss = sum(chi(a) * x**a for a in range(1, 5))
check("gauss_sum_square", sp.rem(gauss**2 - 5, phi5, x) == 0)
G = x * (1 - x**2) / phi5
check("G_actual_reciprocal", sp.cancel(G.subs(x, 1/x) + G) == 0)
check("half_kernel_reciprocal", sp.cancel(x/(1+x) + (1/x)/(1+1/x) - 1) == 0)
check("half_kernel_oldform_identity", sp.cancel(x/(1-x) - 2*x**2/(1-x**2) - x/(1+x)) == 0)


def fricke_matrix(k: int, M: int):
    ds = [d for d in range(1, M+1) if M % d == 0]
    W = sp.zeros(2*len(ds))
    for i, d in enumerate(ds):
        j = ds.index(M//d)
        W[len(ds)+j, i] = 5**(k-1)*sqrt5*(sp.Rational(M, d))**k
        W[j, len(ds)+i] = sqrt5*(sp.Rational(M, d))**k
    return ds, W


a = 5*sqrt5/4
b = sqrt5/2
for k, vec, sign in (
    (4, [1, -1, a, -16*a], -1),
    (4, [1, -1, -a, 16*a], 1),
    (2, [1, -1, b, -4*b], -1),
    (2, [1, -1, -b, 4*b], 1),
):
    ds, W = fricke_matrix(k, 2)
    v = sp.Matrix(vec)
    check(f"level10_weight{k}_eigen{sign}", all(
        sp.simplify(t) == 0 for t in W*v-sign*10**(k//2)*v
    ))
    check(f"level10_weight{k}_square_eigen{sign}", W*W == 10**k*sp.eye(4))

Lprime_minus2 = -25*sqrt5*J/(4*pi**2)
Lchi2 = 4*pi**2/(25*sqrt5)
Theta = 5*sqrt5*J/8
P10 = lambda s: 1 - sp.Rational(2)**(-s)
Q10 = lambda s: 1 - 16*sp.Rational(2)**(-s)
v_minus1 = sp.simplify(P10(1)*Lprime_minus2)
v_minus2 = sp.simplify(P10(2)*(pi**2/6)*(-sp.Rational(2,5)) + a*Q10(2)*(-sp.Rational(1,12))*Lchi2)
v_plus2 = sp.simplify(P10(2)*(pi**2/6)*(-sp.Rational(2,5)) - a*Q10(2)*(-sp.Rational(1,12))*Lchi2)
v_minus3 = sp.simplify(a*Q10(3)*(-sp.Rational(1,2))*J)
check("level10_Lminus1", sp.simplify(v_minus1+5*Theta/pi**2) == 0)
check("level10_Lminus2", v_minus2 == 0)
check("level10_Lplus2", v_plus2 == -pi**2/10)
check("level10_Lminus3", v_minus3 == Theta)
check("level10_Frcke_minus_period_polynomial",
      sp.expand(Theta+(2*pi*sp.I*tau)**2*v_minus1/2-Theta*(1+10*tau**2)) == 0)
check("level10_Frcke_plus_period_polynomial",
      sp.expand(-Theta+2*pi*sp.I*tau*v_plus2+(2*pi*sp.I*tau)**2*v_minus1/2
                +Theta*(1-10*tau**2)+sp.I*pi**3*tau/5) == 0)
Lchi1 = 2*Lphi/sqrt5
Lprime0 = sqrt5*Lchi1/2
P2low = lambda s: 1-sp.Rational(2)**(-s)
Q2low = lambda s: 1-4*sp.Rational(2)**(-s)
check("level10_Bminus_L1",
      sp.simplify(P2low(1)*Lprime0+b*Q2low(1)*(-sp.Rational(1,2))*Lchi1-Lphi) == 0)
check("level10_Bplus_L1",
      sp.simplify(P2low(1)*Lprime0-b*Q2low(1)*(-sp.Rational(1,2))*Lchi1) == 0)

gamma = sp.Matrix([[13, 3], [30, 7]])
W10 = sp.Matrix([[0, -1], [10, 0]])
sigma = W10*gamma
check("gamma_level_and_character", gamma.det() == 1 and gamma[1,0] % 10 == 0 and chi(int(gamma[1,1])) == -1)
check("sigma_trace_and_square", sigma.trace() == 0 and sigma*sigma == -10*sp.eye(2))
h = -sp.Rational(3,13)
z = sp.symbols("z")
sig_action = (sigma[0,0]*(h+z)+sigma[0,1])/(sigma[1,0]*(h+z)+sigma[1,1])
check("sigma_actual_shifted_fricke", sp.cancel(sig_action-h+1/(1690*z)) == 0)
check("sigma_gauge_factor", sp.expand((130*tau+30)**2/10-1690*(tau+sp.Rational(3,13))**2) == 0)

# Fixed cusp -3/13: D_n is the exact Abel sum of chi over n+13 Z>=0.
c, numerator = 13, -3
D = {n: -Q(1,5)*sum(k*chi(n+c*k) for k in range(5)) for n in range(1,c+1)}
check("D_cusp_zero", D[c] == 0)
check("D_cusp_antisymmetric", all(D[c-n] == -D[n] for n in range(1,c)))
# Verify the rational Fourier decomposition modulo Phi_13, independently
# of Bernoulli summation.
phi13 = sp.cyclotomic_poly(13, x)
Gnum, Gden = sp.fraction(sp.cancel(G))
polyD = sum(sp.Rational(v.numerator,v.denominator)*x**n for n,v in D.items())
check("D_fourier_decomposition_at_all_primitive13_roots",
      sp.rem(sp.expand(Gnum-Gden*polyD),phi13,x) == 0)
Eg = sum(D[n]*(b3(Q(numerator*n,c))-b3(Q(2*numerator*n,c))/8) for n in D)
Fg = Q(1,2)*sum(
    (-1)**(k+1)*chi(u)*b3(Q(numerator*k,c)+Q(u,5))
    for k in range(1,c) for u in range(1,5)
)
kappa = Q(2,3)*Eg-Q(5,6)*Fg
check("Eg_minus3_over13", Eg == Q(-45,338), str(Eg))
check("Fg_minus3_over13", Fg == Q(18,4225), str(Fg))
check("kappa_minus3_over13", kappa == Q(-6,65), str(kappa))

N = 36
divs = lambda n: [d for d in range(1,n+1) if n%d == 0]
Ec = lambda k,n: sum(chi(d)*d**(k-1) for d in divs(n))
Fc = lambda k,n: sum(chi(n//d)*d**(k-1) for d in divs(n))


def arrays(k, scalar, factor):
    ans = []
    for n in range(1,N+1):
        E = Ec(k,n)-(Ec(k,n//2) if n%2 == 0 else 0)
        F = Fc(k,n)-(factor*Fc(k,n//2) if n%2 == 0 else 0)
        ans.append((E, F, sp.simplify((E+scalar*F)/n**(k-1))))
    return ans


vcoeff = arrays(4,a,16)
gcoeff = arrays(2,b,4)
common = lcm(*range(1,N+1))
for n,(E,F,v) in enumerate(vcoeff,1):
    oddE = sum(Q(chi(n//m),m**3) for m in divs(n) if m%2)
    halfF = sum(Q(chi(d)*(-1)**(n//d-1),d**3) for d in divs(n))
    check(f"f_actual_kernel_coefficient_{n}", sp.simplify(v-sp.Rational(oddE.numerator,oddE.denominator)-a*sp.Rational(halfF.numerator,halfF.denominator)) == 0)
    check(f"f_complete_safe_integer_coefficient_{n}",
          (4*common**3*E) % n**3 == 0 and (5*common**3*F) % n**3 == 0)
for n,(E,F,g) in enumerate(gcoeff,1):
    oddE = sum(Q(chi(n//m),m) for m in divs(n) if m%2)
    halfF = sum(Q(chi(d)*(-1)**(n//d-1),d) for d in divs(n))
    check(f"g_actual_kernel_coefficient_{n}", sp.simplify(g-sp.Rational(oddE.numerator,oddE.denominator)-b*sp.Rational(halfF.numerator,halfF.denominator)) == 0)
    check(f"g_complete_safe_integer_coefficient_{n}",
          (2*common*E) % n == 0 and common*F % n == 0)
    Ram = 12 if n%13 == 0 else -1
    rootsum = sum(x**((aa*n)%13) for aa in range(1,13))
    check(f"true_ramanujan13_trace_coefficient_{n}",
          sp.rem(rootsum-Ram,phi13,x) == 0)

# Audit the separate, new level-20 closure. This is an independent fixed
# matrix/critical-value check; its analytic proof lives in the other report.
for k, vec, sign in (
    (4, [1,-5,4,-a,20*a,-64*a], -1),
    (4, [1,-5,4,a,-20*a,64*a], 1),
    (2, [1,0,0,0,0,-4*sqrt5], -1),
    (2, [1,0,0,0,0,4*sqrt5], 1),
):
    ds,W = fricke_matrix(k,4)
    v = sp.Matrix(vec)
    check(f"independent_level20_weight{k}_eigen{sign}",
          all(sp.simplify(t) == 0 for t in W*v-sign*20**(k//2)*v))
Theta20 = -5*sqrt5*J/16
P20 = lambda s: 1-5*sp.Rational(2)**(-s)+4*sp.Rational(4)**(-s)
Q20 = lambda s: 1-20*sp.Rational(2)**(-s)+64*sp.Rational(4)**(-s)
check("independent_level20_two_middle_zeros", P20(2) == Q20(2) == 0)
check("independent_level20_Lminus3", sp.simplify(-a*Q20(3)*(-sp.Rational(1,2))*J-Theta20) == 0)
L120 = sp.simplify(P20(1)*Lprime_minus2)
check("independent_level20_L1", sp.simplify(L120+10*Theta20/pi**2) == 0)
check("independent_level20_plus_period",
      sp.expand(-Theta20+(2*pi*sp.I*tau)**2*L120/2+Theta20*(1-20*tau**2)) == 0)

# Independent zeta(3) calibration supplied by the root branch.
uz = {1:7,2:-132,5:825,10:-700}
Pz = lambda s: sum(sp.Rational(u)*sp.Rational(d)**(-s) for d,u in uz.items())
check("zeta3_source_constant_zero",sum(uz.values()) == 0)
check("zeta3_source_fricke_anti",all(uz[10//d] == -sp.Rational(100)*u/d**4 for d,u in uz.items()))
check("zeta3_source_middle_zero",Pz(2) == 0)
check("zeta3_source_L3_multiplier",240*Pz(3)*(-sp.Rational(1,2)) == 432)
check("zeta3_source_L1_multiplier",240*Pz(1)*(-sp.Rational(1,4)) == -2160)

result = {
    "status":"exact_low_period_coupling_checks_passed",
    "fixed_check_count":len(checks),
    "prefix_length":N,
    "checks":checks,
    "exact_cusp":{"h":"-3/13","effective_fricke_level":1690,
                  "Eg":str(Eg),"Fg":str(Fg),"kappa":str(kappa)},
    "safe_full_prefix_models":{"f":"4 L_N^3 O_Q(sqrt5)",
                               "g":"2 L_N O_Q(sqrt5)"},
    "analytic_proofs_supplied_by_report":[
        "true Fricke period polynomials",
        "radial cusp limits and root reciprocal identities",
        "Bernoulli evaluation and sigma regular projection"
    ],
    "not_proved":[
        "new numerical irrationality or linear independence",
        "a simultaneous admissible CDT cover at level 10",
        "optimal full-scale denominators or content",
        "a strict arithmetic holonomy contradiction",
        "Lean formal verification"
    ]
}
out=ROOT/"cdt_odd_low_period_coupling_20261005_verify.json"
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"fixed_check_count":len(checks),
                  "exact_cusp":result["exact_cusp"]},ensure_ascii=False))
