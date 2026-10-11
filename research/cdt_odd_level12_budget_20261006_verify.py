"""Fixed exact arithmetic for the pure-L D12 budget, without prior producers.

This is not a function-rank, denominator, leaf, or Smith-bridge certificate.
Only the formulas explicitly listed in the accompanying proof are checked.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import math

checks = []

def ck(name, value, expected=True):
    checks.append({"name": name, "passed": value == expected,
                   "actual": str(value), "expected": str(expected)})
    if value != expected:
        raise AssertionError(name)

def flat(rows):
    m = len(rows)
    return sum(Q((2*i-1)*s, m*m) for i, s in enumerate(rows, 1))

ck("prime-source constant", 1217*240+2880, 294960)
ck("prime-source ordinary p3 coefficient", 1217*240, 292080)
ck("character source coefficient", 2880*24, 69120)
ck("unscaled norm", 1229**2-3*288**2, 1261609)
ck("source norm", 294960**2-3*69120**2, 72668678400)
ck("source norm factorization", 2**8*3**2*5**2*419*3011, 72668678400)

fixed_tables = [
    ("bare4", (0,3,3,3), Q(0), Q(45,16), Q(15,4)),
    ("L5", (0,1,3,3,3), Q(0), Q(66,25), Q(33,10)),
    ("LK6", (0,1,2,3,3,3), Q(0), Q(47,18), Q(47,15)),
    ("LTK7", (0,1,2,2,3,3,3), Q(0), Q(18,7), Q(3)),
    ("LTKI8", (0,1,2,2,2,3,3,3), Q(15,64), Q(177,64), Q(177,56)),
]
for name, rows, sharp, tau, necessary in fixed_tables:
    computed = flat(rows)+sharp
    ck(name+" full cost", computed, tau)
    ck(name+" Jensen threshold", len(rows)*computed/(len(rows)-1), necessary)

ck("m8 exact sharp normalization", Q(2,8**2)*Q(15,2), Q(15,64))
ck("m4 benchmark gamma5/6 cost", Q(45,16)-Q(2,4**2)*Q(5,6), Q(65,24))
ck("m4 benchmark gamma5/6 Jensen", Q(4,3)*Q(65,24), Q(65,18))
ck("degree2p/4p saturation", Q(1,2)+Q(1,8), Q(5,8))
ck("conditional gamma5/8 cost", Q(45,16)-Q(2,16)*Q(5,8), Q(175,64))
ck("conditional gamma5/8 Jensen", Q(4,3)*Q(175,64), Q(175,48))
ck("kernel group PSL index", 24*2, 48)
ck("quotient weight2 valence", Q(2*24,12), Q(4))

# A strict rational comparison, without numerical log as proof.
exp_lower = sum(Q(14,5)**j / math.factorial(j) for j in range(11))
ck("exp14/5 positive prefix exceeds16", exp_lower > 16)
ck("all five necessary costs exceed14/5", all(t[4] > Q(14,5) for t in fixed_tables))
ck("bare tau exceeds14/5", Q(45,16) > Q(14,5))

out = {
    "scope": "Fixed exact numbers only; no old producer imports or prime/parameter search.",
    "checks": checks,
    "passed_count": len(checks),
    "all_passed": all(x["passed"] for x in checks),
    "display_only": {
        "gamma_needed_if_avg_cap_log16": 22.5-6*math.log(16),
        "maxcap_window_needed": (22.5-6*math.log(16))/9,
    },
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(f"{len(checks)} fixed exact checks passed")
