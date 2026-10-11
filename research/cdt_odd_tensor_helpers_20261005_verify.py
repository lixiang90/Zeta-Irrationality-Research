"""Fixed exact checks for actual K-even tensor backgrounds and a legal CDT table.

No numerical periods, no prime or n-parameter search, no finite-to-all-scale claim.
"""
from fractions import Fraction as F
from math import factorial, lcm, comb
from pathlib import Path
import json
import hashlib
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
STEM = "cdt_odd_tensor_helpers_20261005"
N = 72
R = 25  # The explicit table uses r=24; this is fixed before coefficient checks.
checks = []


def record(name, **data):
    checks.append({"name": name, **data})


def harmonic(n):
    return sum((F(1, j) for j in range(1, n+1)), F(0))


def frac(v):
    return str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}"


def mul(a, b):
    out = [F(0)]*(N+1)
    for i in range(N+1):
        if not a[i]:
            continue
        for j in range(N+1-i):
            if b[j]:
                out[i+j] += a[i]*b[j]
    return out


def pow_series(a, e):
    out = [F(0)]*(N+1)
    out[0] = F(1)
    for _ in range(e):
        out = mul(out, a)
    return out


T = [[F(0)]*(N+1) for _ in range(R+1)]
T[0][0] = F(1)
for j in range(1, R+1):
    running = F(0)
    for n in range(1, N+1):
        running += T[j-1][n-1]
        T[j][n] = running/n
K = {}
for m in (2, 4, 6):
    v = [F(0)]*(N+1)
    for n in range(1, N+1):
        v[n] = ((F(n)-F(1, 2))*v[n-1] + T[m-1][n])/n
    K[m] = v
record("fixed_coefficient_algorithms", N=N, even_indices=[2, 4, 6], log_degree=R)

lcms = [1]*(N+1)
for n in range(1, N+1):
    lcms[n] = lcm(lcms[n-1], n)


def packed_den(n, a, b):
    out = factorial(a)*factorial(b)
    for h in range(1, a+1):
        out *= lcms[n//h]**2
    for h in range(a+1, a+b+1):
        out *= lcms[n//h]
    return out


fixed_monomials = [(a, b) for a in range(4) for b in range(4-a)]
for a, b in fixed_monomials:
    v = mul(pow_series(K[2], a), T[b])
    v = [x/factorial(a) for x in v]
    for n in range(N+1):
        assert (packed_den(n, a, b)*v[n]).denominator == 1
record("sym3_all_monomial_prefix_safety", monomials=len(fixed_monomials),
       coefficients_checked=len(fixed_monomials)*(N+1))

for j in range(R):
    v = mul(K[2], T[j])
    for n in range(N+1):
        assert (packed_den(n, 1, j)*v[n]).denominator == 1
record("explicit_r24_chain_product_prefix_safety", products=R,
       coefficients_checked=R*(N+1))

mixed = mul(mul(K[2], K[4]), T[2])
for n in range(N+1):
    den = factorial(2)
    for j in (1, 2):
        den *= lcms[n//j]**2 * lcms[n//(2*j)]**2
    for j in (1, 2):
        den *= lcms[n//j]
    assert (den*mixed[n]).denominator == 1
record("general_even_product_safe_type_fixed_example", product="K2*K4*T2",
       coefficients_checked=N+1)

t, kval, lval = sp.symbols("t kval lval")
dK = kval/(2*(1-t)) + lval/(t*(1-t))
dL = 1/(1-t)
for a, b in fixed_monomials:
    f = kval**a*lval**b/(factorial(a)*factorial(b))
    lhs = sp.diff(f, kval)*dK + sp.diff(f, lval)*dL
    rhs = a*f/(2*(1-t))
    if a:
        rhs += (b+1)*kval**(a-1)*lval**(b+1) / (
            factorial(a-1)*factorial(b+1)*t*(1-t))
    if b:
        rhs += kval**a*lval**(b-1)/(factorial(a)*factorial(b-1)*(1-t))
    assert sp.cancel(lhs-rhs) == 0
record("tensor_derivative_exact_polynomial_identity", fixed_cases=len(fixed_monomials))

z, ell = sp.symbols("z ell")
for m in (2, 4, 6):
    d = m-1
    cm = -sp.Rational((-2)**d, factorial(d))
    lhs = -2*(-2*ell)**d/(factorial(d)*(1-z*z))
    rhs = cm*ell**d*2/(1-z*z)
    assert sp.cancel(lhs-rhs) == 0
record("quadratic_cover_exact_integral_identity", fixed_indices=[2, 4, 6])

# An automorphism acts on functions, so substitution matrices multiply in
# the reverse order. Generic additive basepoint constants must cancel.
c, h = sp.symbols("c h")
D = 5
M0 = sp.eye(D+2)
alphas = sp.symbols("alpha1:6")
for d in range(1, D+1):
    for j in range(d+1):
        M0[d, j] = comb(d, j)*(h*c)**(d-j)
    M0[d, D+1] = alphas[d-1]
M1 = sp.eye(D+2)
M1[0, D+1] = -c
comm = sp.simplify(M1.inv()*M0.inv()*M1*M0)
expected = sp.eye(D+2)
for d in range(1, D+1):
    expected[d, D+1] = -c*(-h*c)**d
assert all(sp.simplify(x) == 0 for x in comm-expected)
vandermonde = sp.Matrix([[j**d for d in (1, 3, 5)] for j in (1, 2, 3)])
assert vandermonde.det() == 720
record("monodromy_commutator_generic_basepoint_constants_cancel",
       largest_I_degree=D, fixed_odd_translation_determinant=str(vandermonde.det()))

# Explicit weights (K2,K4,K6,L)=(1,3,5,1); different monomials counted once.
weighted = [(a2, a4, a6, b)
            for a2 in range(7) for a4 in range(3) for a6 in range(2)
            for b in range(7) if a2+3*a4+5*a6+b <= 6]
u = sp.symbols("u")
hilbert = sp.series(1/((1-u)**2*(1-u**3)*(1-u**5)), u, 0, 7).removeO()
assert len(weighted) == sum(hilbert.coeff(u, j) for j in range(7))
record("weighted_actual_monomial_rank_fixed_count", indices=[2, 4, 6],
       weight_cutoff=6, background_rank=len(weighted),
       rank8_plus_background=7+len(weighted))

# Rows and columns for the explicit r=24,q=7 table.
rows = [("1", F(0)), ("T1", F(1)), ("K2", F(2))]
for j in range(2, R+1):
    rows.extend([(f"T{j}", 1+harmonic(j-1)), (f"K2*T{j-1}", 1+harmonic(j))])
bg_count = len(rows)
assert bg_count == 2*R+1
for j in range(7):
    rows.append((f"theta^{j}H", 6+harmonic(R)))
columns = [(F(1), 1), (F(1), 2)]
for j in range(2, R+1):
    # T_j is at zero-based row 2j-1; K*T_(j-1) is at row 2j.
    columns.append((F(1, j), 2*j))
columns.extend([(F(1), bg_count)]*5)
for i, (name, sigma) in enumerate(rows):
    assert sum((b for b, start in columns if i >= start), F(0)) == sigma
    for b, start in columns:
        assert start >= 0 and b > 0
    if name.startswith("T"):
        j = int(name[1:])
        needed = [F(1, h) for h in range(1, j+1)]
    elif name == "K2":
        needed = [F(1), F(1)]
    elif name.startswith("K2*T"):
        j = int(name.split("T")[1])
        needed = [F(1), F(1)] + [F(1, h) for h in range(2, j+2)]
    elif "H" in name:
        needed = [F(1)]*7
    else:
        needed = []
    available = sorted((b for b, start in columns if i >= start), reverse=True)
    assert len(available) >= len(needed)
    assert all(b >= a for b, a in zip(available, sorted(needed, reverse=True)))
m = len(rows)
tau = sum((F(2*i+1)*sigma for i, (_, sigma) in enumerate(rows)), F(0))/m**2
formula = harmonic(R)+F(R*R+85*R+189, 2*(R+4)**2)
assert tau == formula == F(41751570293347, 7504844146800)
assert tau < F(1056, 169)
record("explicit_legal_nested_table_r24", target_quotient_rank=7, r=24,
       actual_rank=m, all_e=0, tau_sharp="0", tau_flat=frac(tau),
       rows=[{"name": name, "sigma": frac(sigma)} for name, sigma in rows],
       columns=[{"scale": frac(b), "zero_based_first_active_row": start}
                for b, start in columns],
       all_columns_zero_prefix_constant_tail=True)

x = sp.symbols("x", positive=True)
g7 = (x*x+85*x+189)/(2*(x+4)**2)
assert sp.cancel(sp.diff(g7, x) + (77*x+38)/(2*(x+4)**3)) == 0
assert sp.cancel(g7-sp.Rational(1, 2) - (77*x+173)/(2*(x+4)**2)) == 0
segments = [(1, 3), (4, 8), (9, 14), (15, 24), (25, 40), (41, 56)]
bounds = []
for lo, hi in segments:
    bound = harmonic(lo)+F(hi*hi+85*hi+189, 2*(hi+4)**2)
    assert bound > F(51, 10)
    bounds.append({"range": [lo, hi], "exact_lower_bound": frac(bound)})
assert harmonic(57) > F(23, 5)
g3 = (x*x+13*x+15)/(2*(x+2)**2)
delta = 1/(x+1)+g3.subs(x, x+1)-g3
positive = (2*x**4+11*x**3+34*x*x+70*x+53)/(
    2*(x+1)*(x+2)**2*(x+3)**2)
assert sp.cancel(delta-positive) == 0
assert harmonic(1)+F(1+13+15, 2*9) == F(47, 18)
record("all_R_exact_natural_table_bounds",
       q7_safe_tau_strictly_greater_than="51/10", segments=bounds,
       q3_strict_increase_positive_numerator="2R^4+11R^3+34R^2+70R+53",
       q3_minimum="47/18")

report = ROOT/"research"/(STEM+".md")
out = {
    "status": "exact_tensor_helper_checks_passed",
    "report": report.name,
    "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
    "checks": checks,
    "scope": [
        "All-scale independence and prime-prefix safety are proved in the report.",
        "Finite exact checks audit implementation, not all-scale implications.",
        "The r24 table is a safe feasible input, not the optimum of all types.",
        "No new numerical irrationality or linear independence theorem proved.",
        "No admissible-cover capacity quotient has been established here."
    ],
}
path = ROOT/"research"/(STEM+"_verify.json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": out["status"], "check_groups": len(checks),
                  "actual_r24_rank": m, "tau_safe": frac(tau)}, ensure_ascii=False))

