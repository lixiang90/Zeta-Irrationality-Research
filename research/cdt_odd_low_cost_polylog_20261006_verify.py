"""Exact implementation checks for a genuine ten-dimensional pure background.

The all-prime statements and functional independence are proved in the companion
report. Finite coefficients below check those formulas, not a new irrationality.
"""
from fractions import Fraction as F
from math import factorial, gcd, lcm
from pathlib import Path
import json

N = 84
checks = 0


def check(condition):
    global checks
    assert condition
    checks += 1


def mul(a, b):
    return [sum((a[k] * b[n-k] for k in range(n+1)), F(0))
            for n in range(N+1)]


one = [F(1)] + [F(0)] * N
L = [F(0)] + [F(1, n) for n in range(1, N+1)]
Q = [F(0)] + [F(1, n*n) for n in range(1, N+1)]
Z = [F(0)] + [F(1, n*n*n) for n in range(1, N+1)]
Ts = [one]
for j in range(1, 8):
    Ts.append([a / j for a in mul(Ts[-1], L)])
R = mul(L, Q)
M = [F(0)]
h2 = F(0)
for n in range(1, N+1):
    M.append(h2 / n)
    h2 += F(1, n*n)
K = [F(0)]
for n in range(1, N+1):
    K.append(((n-F(1,2))*K[n-1] + F(1,n))/n)
I = [F(0)] + [K[n]/n for n in range(1, N+1)]

# Exact Taylor coefficient forms of every connection equation.
for n in range(N):
    check((n+1)*L[n+1] == sum(one[:n+1]))
    check((n+1)*Q[n+1] == L[n+1])
    check((n+1)*Z[n+1] == Q[n+1])
    check((n+1)*R[n+1] == sum(Q[:n+1])+2*Ts[2][n+1])
    check((n+1)*M[n+1] == sum(Q[:n+1]))
    check((n+1)*I[n+1] == K[n+1])
    for j in range(2, 8):
        check((n+1)*Ts[j][n+1] == sum(Ts[j-1][:n+1]))
for n in range(1, N+1):
    check(n*K[n]-(n-F(1,2))*K[n-1] == L[n])
    h1 = sum((F(1,k) for k in range(1,n)), F(0))
    h2 = sum((F(1,k*k) for k in range(1,n)), F(0))
    check(R[n] == 2*h1/(n*n)+h2/n)
    check(K[n-1]/n == -2*K[n]+2*K[n-1]+2*Q[n])
    check(sum(K[:n])/n == 2*K[n]-2*Q[n]-2*Ts[2][n])

# Every prime, including 2: each integer assertion checks the entire denominator.
Ls = [1]
for n in range(1, N+1):
    Ls.append(lcm(Ls[-1], n))
for n in range(1, N+1):
    check((Ls[n]**2*K[n]).denominator == 1)
    check((n*Ls[n]**2*I[n]).denominator == 1)
    check((Ls[n]**3*I[n]).denominator == 1)
    for f in (R, M):
        check((n*Ls[n]**2*f[n]).denominator == 1)
        check((Ls[n]**2*Ls[n//2]*f[n]).denominator == 1)
    for j in range(1, 8):
        d_integrated = n
        d_flat = factorial(j)
        for h in range(1, j):
            d_integrated *= Ls[(n-1)//h]
        for h in range(1, j+1):
            d_flat *= Ls[n//h]
        check((d_integrated*Ts[j][n]).denominator == 1)
        check((d_flat*Ts[j][n]).denominator == 1)


def mod_fraction(a, p):
    assert a.denominator % p
    return a.numerator * pow(a.denominator, -1, p) % p


packets = []
for p in (5, 7, 11, 13, 17, 19):
    vals = {
        "p2Kp": mod_fraction(p*p*K[p], p),
        "p2Kp1": mod_fraction(p*p*K[p+1], p),
        "p3Ip": mod_fraction(p**3*I[p], p),
        "p2Ip1": mod_fraction(p*p*I[p+1], p),
        "p2Rp1": mod_fraction(p*p*R[p+1], p),
        "p3R2p": mod_fraction(p**3*R[2*p], p),
        "p2Mp1": mod_fraction(p*p*M[p+1], p),
        "p3M2p": mod_fraction(p**3*M[2*p], p),
    }
    for key in ("p2Kp", "p3Ip", "p2Rp1", "p3R2p", "p2Mp1"):
        check(vals[key] == 1)
    for key in ("p2Kp1", "p2Ip1", "p3M2p"):
        check(vals[key] == pow(2, -1, p))
    packets.append({"p": p, "residues": vals})

check(sum((F(14,5)**j/factorial(j) for j in range(11)), F(0)) > 16)
budget_path = Path(__file__).with_name("cdt_odd_level20_pure_budget_20261006_verify.json")
budget = json.loads(budget_path.read_text(encoding="utf-8"))
check(budget["status"] == "exact_specified_pure_helper_type_audit_passed")
expected = [(13,F(1345,507),F(1345,468)),
            (14,F(2577,980),F(2577,910)),
            (15,F(1769,675),F(1769,630))]
budget_summary = []
for f, (m, tau, threshold) in zip(budget["families"], expected):
    check(f["actual_rank_conditional_on_companion_proof"] == m)
    check(F(f["minimum_total_lower"]) == tau)
    check(F(f["necessary_rho_lower"]) == threshold)
    check(F(m,m-1)*tau == threshold)
    check(threshold > F(14,5))
    budget_summary.append({"rank":m,"tau_lower":str(tau),
                           "necessary_log_radius_lower":str(threshold)})

out = {
    "status": "exact_pure_background_checks_passed",
    "checks": checks,
    "N": N,
    "actual_background_rank": 10,
    "single_target_combined_rank": 13,
    "packets": packets,
    "independence_basis": "CDT MPL8 plus sign K2 plus origin-residue obstruction for integral K2/t",
    "all_prime_proofs": "Companion report, not inference from the finite sample",
    "budget_certificate": "cdt_odd_level20_pure_budget_20261006_verify.json",
    "specified_type_budget_summary": budget_summary,
    "new_numeric_irrationality_proved": False,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": out["status"], "checks": checks, "json": str(path)}, ensure_ascii=False))
