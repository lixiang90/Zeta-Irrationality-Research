"""Fixed exact checks for the even algebraic-integral helper identities.

No parameter search, no period numerics, and no finite-to-asymptotic inference.
"""
from fractions import Fraction as F
from math import comb, factorial, lcm
from pathlib import Path
import hashlib
import json
import sys
import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
STEM = "cdt_odd_algebraic_helpers_20261005"
N = 128
M = 8
checks = []


def record(name, **data):
    checks.append({"name": name, **data})


def valuation(v, p):
    if v == 0:
        return None
    a, b, out = abs(v.numerator), v.denominator, 0
    while a % p == 0:
        a //= p
        out += 1
    while b % p == 0:
        b //= p
        out -= 1
    return out


def modp(v, p):
    assert v.denominator % p
    return v.numerator * pow(v.denominator, -1, p) % p


# Parameter Gauss identity: t=exp(-2v), u=t^z.
t, u, z = sp.symbols("t u z")
r = -(1-t)**2/(4*t)
rp = sp.diff(r, t)
G = t*(1/u-u)/(z*(1-t*t))


def dt(f):
    return sp.diff(f, t)+(z*u/t)*sp.diff(f, u)


Gr = sp.cancel(dt(G)/rp)
Grr = sp.cancel(dt(Gr)/rp)
gauss = sp.cancel(r*(1-r)*Grr+(sp.Rational(3, 2)-3*r)*Gr-(1-z*z)*G)
assert gauss == 0
record("parameter_gauss_identity", residual="0", initial_value="1 by t->1")

# Algebraic change identities used in the first-order uniqueness proof.
x = sp.symbols("x")
y = x*x/(x-1)
assert sp.cancel(x*sp.diff(y, x)/y-(2-x)/(1-x)) == 0
assert sp.cancel(x*(2-x)/(2*(1-x))-((1-x)**-1-(1-x))/2) == 0
record("hypergeometric_pullback_rational_identities", residual="0")

# T_d coefficients by theta T_d=x/(1-x) T_(d-1), an O(MN) exact algorithm.
T = [[F(0) for _ in range(N+1)] for _ in range(M)]
T[0][0] = F(1)
for d in range(1, M):
    running = F(0)
    for n in range(1, N+1):
        running += T[d-1][n-1]
        T[d][n] = running/n

K = {}
for m in range(2, M+1):
    out = [F(0) for _ in range(N+1)]
    for n in range(1, N+1):
        out[n] = ((F(n)-F(1, 2))*out[n-1]+T[m-1][n])/n
        assert n*out[n]-(F(n)-F(1, 2))*out[n-1] == T[m-1][n]
    K[m] = out
record("all_fixed_first_order_recurrences", m_values=list(K), through=N)

# Independent hypergeometric / finite-binomial formula (7), no ODE recursion.
hyper_coeff = {}
for k in (1, 2, 3, 4):
    e = [F(1)]+[F(0)]*(k-1)
    terms = []
    for n in range(0, 32):
        if n:
            for j in range(k-1, 0, -1):
                e[j] += e[j-1]/(n*n)
        terms.append(e[k-1]/((2*n+1)**2*comb(2*n, n)))
    for degree in range(1, 65):
        v = sum(((-1)**(k-1+n)*comb(degree-n-1, n)*terms[n]
                 for n in range(k-1, (degree-1)//2+1)), F(0))
        assert v == K[2*k][degree], (k, degree, v, K[2*k][degree])
    hyper_coeff[str(2*k)] = [str(v) for v in K[2*k][:12]]
record("independent_finite_binomial_formula", weights=[2, 4, 6, 8], through=64)

L = [1]
for n in range(1, N+1):
    L.append(lcm(L[-1], n))
safe_records = []
for k in (1, 2, 3, 4):
    for n in range(1, N+1):
        safe = L[n]**2
        for h in range(1, k):
            safe *= L[(n-1)//(2*h)]**2
        assert (safe*K[2*k][n]).denominator == 1, (k, n)
        assert (L[n]**(2*k)*K[2*k][n]).denominator == 1
    safe_records.append({"weight": 2*k, "through": N,
                         "safe_scale_sum": str(F(2)+sum((F(1, h) for h in range(1, k)), F(0)))})
record("complete_safe_types_fixed_prefixes", rows=safe_records)

# Fixed p and m lists test the exact block packets, rather than search for units.
packets = []
for p in (13, 17, 23):
    for m in (2, 4, 6):
        d = m-1
        for j in range(1, d):
            C = modp(p**j*K[m][j*p], p)
            h = d-j
            offsets = (1, h) if h >= 2 else (1, 2)
            residues = []
            for rr in sorted(set(offsets)):
                lhs = modp(p**j*K[m][j*p+rr], p)
                Ar = F(comb(2*rr, rr), 4**rr)
                rhs = (C*modp(Ar, p)+modp(K[m-j][rr]/factorial(j), p)) % p
                assert lhs == rhs
                residues.append({"offset": rr, "residue": lhs,
                                 "valuation": valuation(K[m][j*p+rr], p)})
            assert any(a["residue"] != 0 for a in residues)
            packets.append({"p": p, "m": m, "j": j, "C": C,
                            "offsets": residues})
        j = d
        residues = []
        for rr in (1, 2):
            lhs = modp(p**m*K[m][j*p+rr], p)
            rhs = modp(F(comb(2*rr, rr), 4**rr*j*factorial(j)), p)
            assert lhs == rhs and lhs != 0
            assert valuation(K[m][j*p+rr], p) == -m
            residues.append({"offset": rr, "residue": lhs, "valuation": -m})
        packets.append({"p": p, "m": m, "j": j, "top_packet": residues})
record("fixed_block_packets", rows=packets)

assert F(1, 2)*K[2][2]-F(3, 8)*K[2][1] == F(1, 8)
record("two_offset_unit_determinant", value="1/8")

rows = []
for k in (1, 2, 3, 4):
    m = 2*k
    lower = sum((F(1, j) for j in range(1, m-1)), F(0))+F(2, m-1)
    upper = F(2)+sum((F(1, j) for j in range(1, k)), F(0))
    assert lower <= upper
    rows.append({"m": m, "necessary_scale_sum": str(lower), "safe_scale_sum": str(upper)})
assert rows[0]["necessary_scale_sum"] == rows[0]["safe_scale_sum"] == "2"
record("necessary_vs_safe_cost_table", rows=rows)

md = ROOT/"research"/(STEM+".md")
data = {
    "status": "all_fixed_exact_checks_passed",
    "scope": "Fixed exact identity and coefficient checks; full-scale proofs are in the report. No numerical irrationality conclusion or parameter scan.",
    "report_sha256": hashlib.sha256(md.read_bytes()).hexdigest(),
    "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "first_even_coefficients": hyper_coeff,
    "not_proved": ["optimal higher-weight integrated denominator types",
                   "a common admissible multivalent map and strict CDT rank contradiction",
                   "new irrationality or independence of odd zeta or L values"],
}
out = ROOT/"research"/(STEM+"_verify.json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status": data["status"], "check_groups": len(checks),
                  "report_sha256": data["report_sha256"],
                  "verifier_sha256": data["verifier_sha256"]}, ensure_ascii=False))
