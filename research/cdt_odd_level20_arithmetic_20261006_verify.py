"""Exact arithmetic checks for level20 Q-trace and lawful CDT type tables.

Fixed rational c=1 tests coefficient formulas; it is not an approximation to L3.
All-scale rank/filter proofs remain in the report and the separate geometry model.
"""
from fractions import Fraction as F
from math import comb, factorial, lcm
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
STEM = "cdt_odd_level20_arithmetic_20261006"
N = 56
checks = []


def record(name, **data):
    checks.append({"name": name, **data})


def pad(a):
    return list(a[:N])+[F(0)]*max(0, N-len(a))


def add(a, b):
    return [a[i]+b[i] for i in range(N)]


def scale(a, c):
    return [v*c for v in a]


def mul(a, b):
    out = [F(0)]*N
    for i, v in enumerate(a):
        if v:
            for j in range(N-i):
                if b[j]:
                    out[i+j] += v*b[j]
    return out


def inverse(a):
    assert a[0]
    out = pad([1/a[0]])
    for n in range(1, N):
        out[n] = -sum(a[k]*out[n-k] for k in range(1, n+1))/a[0]
    return out


def pw(a, k):
    out = pad([F(1)])
    for _ in range(k):
        out = mul(out, a)
    return out


def compose(a, b):
    assert b[0] == 0
    out = pad([])
    power = pad([F(1)])
    for v in a:
        if v:
            out = add(out, scale(power, v))
        power = mul(power, b)
    return out


def revert(a):
    assert a[0] == 0 and a[1] == 1
    inverse_unit = inverse(pad(a[1:]))
    power = pad([F(1)])
    out = pad([])
    for n in range(1, N):
        power = mul(power, inverse_unit)
        out[n] = power[n-1]/n
    return out


def eta_unit(ds, rs):
    out = pad([F(1)])
    for d, r in zip(ds, rs):
        for m in range(d, N, d):
            fac = pad([])
            for j in range((N-1)//m+1):
                if r >= 0:
                    bc = comb(r, j) if j <= r else 0
                else:
                    bc = (-1)**j*comb(-r+j-1, j)
                fac[j*m] = F((-1)**j*bc)
            out = mul(out, fac)
    return out


def chi(n):
    return (0, 1, -1, -1, 1)[n % 5]


def E(k):
    constant = F(-1, 5) if k == 2 else F(1)
    return pad([constant]+[
        F(sum(chi(d)*d**(k-1) for d in range(1, n+1) if n % d == 0))
        for n in range(1, N)])


def Fseries(k):
    return pad([F(0)]+[
        F(sum(chi(n//d)*d**(k-1) for d in range(1, n+1) if n % d == 0))
        for n in range(1, N)])


def old(a, d):
    return [a[n//d] if n % d == 0 else F(0) for n in range(N)]


def theta(a):
    return [n*v for n, v in enumerate(a)]


def valuation(v, p):
    assert v
    a, b = abs(v.numerator), v.denominator
    ans = 0
    while a % p == 0:
        a //= p
        ans += 1
    while b % p == 0:
        b //= p
        ans -= 1
    return ans


def modp(v, p):
    assert v.denominator % p
    return v.numerator*pow(v.denominator, -1, p) % p


unit = eta_unit([1, 2, 4, 5, 10, 20], [-3, 4, -1, -1, 4, -3])
tq = pad([F(0)]+inverse(unit)[:-1])
qt = revert(tq)
assert all(v.denominator == 1 for v in tq+qt)
assert tq[:5] == [0, 1, -3, 4, -7]
assert compose(tq, qt) == pad([0, 1])
record("fixed_integer_coordinate_and_inverse_jets", N=N,
       t_first=[str(v) for v in tq[:8]], q_first=[str(v) for v in qt[:8]])

EE, FF = E(2), old(Fseries(2), 4)
VE = add(add(E(4), scale(old(E(4), 2), -5)), scale(old(E(4), 4), 4))
VF = add(add(Fseries(4), scale(old(Fseries(4), 2), -20)), scale(old(Fseries(4), 4), 64))
u = [F(0)]+[VE[n]/n**3 for n in range(1, N)]
v = [F(0)]+[F(5, 4)*VF[n]/n**3 for n in range(1, N)]
trace_body = add(scale(mul(EE, u), 2), scale(mul(FF, v), 40))
trace_c = scale(FF, F(-25, 2))
diff_body = add(scale(mul(EE, v), -2), scale(mul(FF, u), -8))
diff_c = scale(EE, F(5, 8))
assert trace_c[0] == 0 and trace_c[4] == F(-25, 2)
assert diff_c[0] == F(-1, 8)

e, f, U, V, c = sp.symbols("E F u v c")
r = sp.sqrt(5)
hm = (e-4*r*f)*(U-r*V+5*r*c/16)
hp = (e+4*r*f)*(U+r*V-5*r*c/16)
assert sp.expand(hm+hp-(2*e*U+40*f*V-sp.Rational(25, 2)*f*c)) == 0
assert sp.expand((hm-hp)/r-(-2*e*V-8*f*U+sp.Rational(5, 8)*e*c)) == 0
assert sp.simplify((hm*hp).subs({e: -sp.Rational(1, 5), f: 0, U: 0, V: 0})
                   +sp.Rational(5, 256)*c*c) == 0
record("formal_trace_difference_norm_target_identity",
       trace_constant="0", trace_q4_target="-25c/2",
       difference_constant="-c/8", norm_constant="-5c^2/256")

bodies = [compose(a, qt) for a in (trace_body, trace_c, diff_body, diff_c)]
ET, FT = compose(EE, qt), compose(FF, qt)
trace = add(bodies[0], bodies[1])  # fixed formal rational c=1
diff = add(bodies[2], bodies[3])
lcms = [1]*N
for n in range(1, N):
    lcms[n] = lcm(lcms[n-1], n)
for a in bodies:
    for n, value in enumerate(a):
        assert (80*lcms[n]**3*value).denominator == 1
for k in range(6):
    row = trace
    for _ in range(k):
        row = theta(row)
    for n, value in enumerate(row):
        assert (80*lcms[n]**3*value).denominator == 1
record("all_fixed_prefix_trace_difference_and_derivative_safety",
       N=N, fixed_clear_factor=80, safe_type="L_N^3",
       formal_rational_c="1", target_coefficient_checked_separately=True)

packets = []
for p in (11, 13):
    eps = chi(p)
    assert eps in (-1, 1)
    ct = add(scale(ET, 2), scale(FT, 50*eps))
    cj = add(scale(FT, -8), scale(ET, F(-5, 2)*eps))
    for s in (1, 2, 4):
        assert modp(p**3*trace[p+s], p) == modp(ct[s], p)
        assert modp(p**3*diff[p+s], p) == modp(cj[s], p)
    assert valuation(trace[p+1], p) == -3
    assert valuation(diff[p+1], p) == -3
    packets.append({"p": p, "chi": eps, "trace_p1_residue": 2,
                    "difference_p1_residue": str(F(-5, 2)*eps)})
mixed = trace
for _ in range(3):
    mixed = add(theta(mixed), scale(mixed, -1))
log = [F(0)]+[F(1, n) for n in range(1, N)]
mixed = add(mixed, log)
assert valuation(mixed[15], 13) == -3
assert modp(13**3*mixed[15], 13) == 4
record("preselected_both_prime_classes_and_fixed_mixed_row_packets",
       packets=packets, mixed_row="(theta-1)^3*T+L",
       mixed_p=13, mixed_offset=2, mixed_residue=4)

norm = scale(add(mul(trace, trace), scale(mul(diff, diff), -5)), F(1, 4))
for n, value in enumerate(norm):
    assert (4*80**2*lcms[n]**3*lcms[n//2]**3*value).denominator == 1
for p in (11, 13):
    assert valuation(norm[2*p+1], p) == -6
    assert modp(p**6*norm[2*p+1], p) == modp(F(109, 40), p)
record("norm_weighted_convolution_safety_and_fixed_six_layer_packet",
       safe_type="L_N^3*L_floor(N/2)^3", safe_sigma="9/2",
       necessary_sigma="3", p_values=[11, 13], offset=1, residue="109/40",
       no_actual_norm_rank_claim=True)

t = sp.symbols("t")
cm = t*t-t+(3-r)/8
cp = t*t-t+(3+r)/8
Delta = 16*t**4-32*t**3+28*t*t-12*t+1
assert sp.expand(16*cm*cp-Delta) == 0
assert sp.resultant(cm, cp, t) == sp.Rational(5, 16)
assert sp.discriminant(cm, t) == (r-1)/2
assert sp.discriminant(cp, t) == (-r-1)/2
record("quadratic_twist_nonsquare_divisor_exact_checks",
       resultant="5/16", discriminants=["(sqrt5-1)/2", "(-sqrt5-1)/2"],
       all_roots_simple_disjoint=True,
       cyclic_rank_not_inferred_from_jets=True)

x = sp.symbols("x")
H = lambda n: sum((sp.Rational(1, j) for j in range(1, n+1)), sp.Rational(0))


@lru_cache(None)
def Ipieces(m):
    points = {sp.Rational(1), sp.Rational(m)}
    for h in range(1, m):
        points.update(a for a in (sp.Rational(m-1, h), sp.Rational(m, h)) if 1 < a < m)
    points = sorted(points)
    C = sp.Rational(3, 2)+(m-1)*H(m-2)+H(m-1)/2
    pieces = [(sp.Rational(0), sp.Rational(1), C-m*x+x*x/2)]
    for lo, hi in zip(points, points[1:]):
        mid = (lo+hi)/2
        I = sp.Rational(0)
        for h in range(1, m):
            if m-1-h*mid > 0:
                I += (m-1-h*x)/h
        for k in range(1, m):
            y = m-k*mid
            if y >= 1:
                I += sp.Rational(1, 2*k)
            elif y > 0:
                I += (m-k*x)**2/(2*k)
        pieces.append((lo, hi, sp.expand(I)))
    return pieces


def sharp(m, total, maximum):
    if maximum == 0:
        return sp.Rational(0), sp.Rational(0)
    vals = []
    for lo, hi, I in Ipieces(m):
        objective = sp.expand(total*x+maximum*I)
        candidates = [lo, hi]
        der = sp.diff(objective, x)
        if der.has(x):
            stat = sp.solve(der, x)[0]
            if lo <= stat <= hi:
                candidates.append(stat)
        vals.extend((sp.Rational(2, m*m)*objective.subs(x, a), a) for a in candidates)
    return min(vals)


tables = []
for eL, eT in product((0, 1), repeat=2):
    rows = [("1", 0, 0), ("L", 1-eL, eL), ("T2", 2-eT, eT), ("K2", 2, 0)]
    rows += [(f"theta^{j}T", 3, 0) for j in range(6)]
    rows.sort(key=lambda a: a[1])
    m = len(rows)
    flat = sum(sp.Rational(2*i+1)*a[1] for i, a in enumerate(rows))/m**2
    shrp, xi = sharp(m, eL+eT, max(eL, eT))
    columns = []
    for j in range(1, 4):
        columns.append(next(i for i, a in enumerate(rows) if a[1] >= j))
    for i, a in enumerate(rows):
        assert sum(i >= start for start in columns) == a[1]
    tables.append({"e_L": eL, "e_T2": eT, "flat": str(flat),
                   "sharp": str(shrp), "total": str(flat+shrp),
                   "sharp_minimizer": str(xi), "actual_rank": m,
                   "unit_column_start_rows": columns,
                   "zero_prefix_constant_tail": True})
assert [a["total"] for a in tables] == ["279/100", "293/100", "59/20", "599/200"]
assert 3*(1-sp.Rational(1, 49)) == sp.Rational(144, 49)
record("four_complete_lawful_rank10_fine_types", tables=tables,
       best_fixed_type="279/100", no_claim_of_global_optimum=True)

k_rows = [0, 1, 2, 2, 3, 3, 3]
k_tau = sum(sp.Rational(2*i+1)*v for i, v in enumerate(k_rows))/49
assert k_tau == sp.Rational(18, 7)
record("closed_number_field_arithmetic_input", actual_K_rank=7,
       safe_arithmetic_cost=str(k_tau), Q_trace_rank=10,
       Q_trace_safe_cost="279/100",
       closed_number_field_corollary_proved_in_report=True,
       full_G_common_cover_proved_in_companion_report=True,
       archimedean_capacity_data_sufficient=False,
       proof_not_inferred_from_finite_coefficients=True)

assert 7*sp.Rational(18,7)/6 == 3
assert 10*sp.Rational(279,100)/9 == sp.Rational(31,10)
assert 8*sp.Rational(257,96)/7 == sp.Rational(257,84)
record("plain_Jensen_capacity_necessary_thresholds",
       K_rank7_rho_necessary_strictly_above="3",
       Q_rank10_rho_necessary_strictly_above="31/10",
       K_rank8_arbitrary_matrix_necessary_strictly_above="257/84",
       Jensen_proof_in_report_not_inferred_from_numerical_integrals=True)

actual_table_costs = [(8, sp.Rational(167,64)), (11, sp.Rational(340,121)),
                      (9, sp.Rational(2597,972)), (12, sp.Rational(4937,1728)),
                      (10, sp.Rational(1369,500)), (10, sp.Rational(1087,400))]
actual_thresholds = [sp.Rational(m,m-1)*tau for m,tau in actual_table_costs]
assert all(a > sp.Rational(29,10) for a in actual_thresholds)
assert sum(sp.Rational(29,10)**k/sp.factorial(k) for k in range(9)) > 16
record("six_fixed_actual_transport_thresholds",
       costs=[{"actual_rank":m,"tau_double":str(tau),"necessary_rho":str(rho)}
              for (m,tau),rho in zip(actual_table_costs,actual_thresholds)],
       transport_optimality_proved_by_separate_full_interval_certificates=True,
       exp_29_over_10_positive_series_lower_exceeds_16=True,
       all_thresholds_strictly_above_log16=True,
       fixed_tables_only_not_adaptive_lattices=True)

# A proposed array with .5->1 or 1/3->1 does not satisfy CDT (6.0.3).
bad_columns = [[0, 0, sp.Rational(1, 2), sp.Rational(1, 2), 1, 1],
               [0, 0, 0, sp.Rational(1, 3), sp.Rational(1, 3), 1]]
for col in bad_columns:
    assert len({v for v in col if v}) > 1
valid_bg = [0, 1, sp.Rational(3, 2), sp.Rational(11, 6), sp.Rational(17, 6)]
q_joint = valid_bg+[sp.Rational(23, 6)]*6
k_single = valid_bg+[sp.Rational(23, 6)]*3
tauQ = sum((2*i+1)*v for i, v in enumerate(q_joint))/121
tauK = sum((2*i+1)*v for i, v in enumerate(k_single))/64
assert tauQ == sp.Rational(2501, 726)
assert tauK == sp.Rational(595, 192)
record("varying_positive_scale_rejection_and_legal_repair",
       varying_columns_not_CDT_6_0_3=True,
       retained_fraction_Q_rank11_cost=str(tauQ),
       retained_fraction_K_rank8_cost=str(tauK))

report = ROOT/"research"/(STEM+".md")
out = {
    "status": "exact_level20_arithmetic_checks_passed",
    "report": report.name,
    "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
    "checks": checks,
    "scope": [
        "Actual rank proof depends on the full level20 geometry module and nonsplit extension.",
        "Finite coefficients do not prove global cyclic rank.",
        "The fixed rational test c=1 does not evaluate the unknown L3 value.",
        "Q-rank10 cost279/100 is a lawful safe input, not a global minimum.",
        "The report derives a limited closed-system e0 number-field corollary of CDT.",
        "No admissible archimedean capacity contradiction established.",
        "No new numerical irrationality or linear independence theorem proved."
    ],
}
path = ROOT/"research"/(STEM+"_verify.json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": out["status"], "check_groups": len(checks),
                  "actual_Q_table_rank": 10, "lawful_safe_tau": "279/100"}))

