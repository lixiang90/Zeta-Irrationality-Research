"""NEW exact rational certificate; first execution only, no old/peer imports.

The all-scale determinant theorem is proved on paper in the matching NEW MD.
This program certifies only its closed logarithmic constants for B=5,6,8.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

N = 80


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(c, a):
    return (c * a[0], c * a[1]) if c >= 0 else (c * a[1], c * a[0])


def atanh_log(r):
    assert F(1) <= r <= F(2)
    t = (r - 1) / (r + 1)
    lo = 2 * sum((t ** (2*j + 1) / (2*j + 1) for j in range(N)), F(0))
    tail = 2 * t ** (2*N + 1) / ((2*N + 1) * (1 - t*t))
    return lo, lo + tail


LOG2 = atanh_log(F(2))


def log_interval(r):
    assert r > 0
    k = 0
    while r < 1:
        r *= 2
        k -= 1
    while r >= 2:
        r /= 2
        k += 1
    return add(atanh_log(r), scale(F(k), LOG2))


def closed_beta(B):
    d, L = F(B - 4), F(B + 2)
    terms = [
        (2*d*L, L), (-2*d*B, F(B)), (-4*d, F(2)),
        (d*d/2, 32*d/(d+12)),
        (3*(L*L+4)/2, 2*(L-2)/(L+2)),
        (-6*L, (L*L-4)*(L+6)**2/(128*L*L)),
    ]
    ans = (-d*d, -d*d)
    for c, r in terms:
        ans = add(ans, scale(c, log_interval(r)))
    return ans, terms


def exact_string(r):
    return f"{r.numerator}/{r.denominator}"


def thousand_window(a):
    lo, hi = a
    lower = lo.numerator * 1000 // lo.denominator
    upper = -((-hi.numerator * 1000) // hi.denominator)
    return F(lower, 1000), F(upper, 1000)


OLD_TANGENT_UPPER = {5: F(7643,1000), 6: F(17477,1000), 8: F(43030,1000)}
OLD_SAFE_COST_UPPER = {5: F(17834,1000), 6: F(35939,1000), 8: F(81249,1000)}
cert = {"status": "PASS", "method": "exact Fraction atanh series, N=80", "producer_execution": "first execution only", "scope": "closed beta constants only; no finite-n inference", "layouts": []}
checks = 0
for B in (5, 6, 8):
    d, L = F(B-4), F(B+2)
    t = d*(d+12)/8
    assert 9*(4+t) == L*L+t
    assert (t+(L*L+4)/2+3*(4+t))/((L+2)**2/2) == 2*(L-2)/(L+2)
    assert (2*L*3*(4+t)+4*L*L+(L*L+4)*t/2)/(8*L*L) == (L*L-4)*(L+6)**2/(128*L*L)
    checks += 3
    beta, terms = closed_beta(B)
    window = thousand_window(beta)
    assert window[0] < beta[0] <= beta[1] < window[1]
    assert beta[0] > OLD_TANGENT_UPPER[B]
    assert beta[1] < OLD_SAFE_COST_UPPER[B]
    checks += 3
    cert["layouts"].append({
        "B": B, "d": int(d), "R_squared": exact_string(t),
        "beta_exact_interval": [exact_string(q) for q in beta],
        "beta_thousand_window": [exact_string(q) for q in window],
        "strict_gain_over_old_tangent_upper_at_least": exact_string(window[0]-OLD_TANGENT_UPPER[B]),
        "old_safe_cost_upper": exact_string(OLD_SAFE_COST_UPPER[B]),
        "matched_margin_not_proved": True,
        "log_terms": [{"coefficient": exact_string(c), "argument": exact_string(r)} for c,r in terms],
    })
cert["exact_checks"] = checks
cert["producer_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
out = Path(__file__).with_suffix(".json")
assert not out.exists(), "Refuse overwrite or rerun of NEW certificate."
out.write_text(json.dumps(cert, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status":"PASS", "exact_checks":checks, "windows":[{"B":r["B"],"beta":r["beta_thousand_window"],"gain_lower":r["strict_gain_over_old_tangent_upper_at_least"]} for r in cert["layouts"]]}, ensure_ascii=False))
