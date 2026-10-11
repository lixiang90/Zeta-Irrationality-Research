"""One fixed rank19 unit table, using exact arithmetic and no old producer."""
from pathlib import Path
from fractions import Fraction as F
import json
import math

labels = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    labels.append(label)


background_sigma = [0, 0, 1, 1, 2, 2, 2, 2, 2, 2]
background_e = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
sigma = background_sigma + [3]*3 + [3]*6
e = background_e + [0]*3 + [1]*6
m = len(sigma)
nu = [x+y for x, y in zip(sigma, e)]
s = max(nu)
theta = sorted(F(0) if b == 0 else F(1) for b in sigma)
a0 = min(F(i, 1)/q for i, q in enumerate(theta) if i > 0 and q > 0)

check("Actual fixed rows total nineteen", m == 19)
check("Sigma sorted unit multiplicities", sorted(sigma) == [0]*2+[1]*2+[2]*6+[3]*9)
check("Sum sigma forty-one", sum(sigma) == 41)
check("E fourteen and e-star one", sum(e) == 14 and max(e) == 1)
check("Matching a-zero two", a0 == 2)
check("Nu exact multiplicities", sorted(nu) == [0,1]+[2]*3+[3]*8+[4]*6)
check("Sum nu fifty-five and cap four", sum(nu) == 55 and s == 4)
flat_numerator = sum((2*i+1)*b for i, b in enumerate(sorted(sigma)))
flat = F(flat_numerator, m*m)
check("Flat numerator nine hundred sixty-three", flat_numerator == 963)
check("Flat cost exact", flat == F(963,361))
floors = [s-v for v in nu]
counts = [sum(v >= threshold for v in floors) for threshold in range(1,s+1)]
check("Baseline threshold counts", counts == [13,5,2,1])
check("Baseline floor sum twenty-one", sum(floors) == sum(counts) == 21)
check("Matching normalized baseline", F(s)-F(sum(floors),m) == F(sum(nu),m))


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))


def i_m(x):
    if x <= 1:
        c = F(3,2)+(m-1)*harmonic(m-2)+harmonic(m-1)/2
        return c-m*x+x*x/2
    return (
        sum((max(F(0), F(m-1)-k*x)/k for k in range(1,m)),F(0))
        +sum((min(F(1),max(F(0),F(m)-k*x))**2/(2*k) for k in range(1,m)),F(0))
    )


h14 = harmonic(14)
pmin = F(37,2)*h14
left = F(19,15)
right = F(9,7)
check("Plateau ordered and above one", F(1) < left < right < m)
check("Harmonic fourteen exact", h14 == F(1171733,360360))
for name, x in (("left",left), ("right",right)):
    check(f"{name} plateau split fourteen active", all(F(m)-k*x >= 1 for k in range(1,15)))
    check(f"{name} plateau fifteen to eighteen inactive", all(F(m)-k*x <= 0 for k in range(15,m)))
    check(f"{name} direct I expression plateau", 14*x+i_m(x) == pmin)
check("P derivative on zero-to-one is negative", F(14-m)+F(1) < 0)
gamma = F(5,6)
check("Fixed cutoff gives full old gamma", min(a0,right,F(1)) >= F(2,3))
kappa = flat+F(2,m*m)*(pmin-gamma)
gate = F(m,m-1)*kappa
check("Kappa exact", kappa == F(389780201,130089960))
check("Necessary gate exact", gate == F(389780201,123243120))
check("Necessary gate minus fourteen-fifths exact", gate-F(14,5) == F(8939893,24648624))
check("Eleven-term positive Taylor sum exceeds sixteen", sum((F(14,5)**j/F(math.factorial(j)) for j in range(11)),F(0)) > 16)

payload = {
    "scope": "One fixed actual rank19 unit array; no prime/type scan, no new integral Smith gain. All-xi optimality and actual mathematical inputs are proved/cited in the report.",
    "checks_passed": len(labels),
    "check_labels": labels,
    "sigma": sigma,
    "e": e,
    "nu": nu,
    "cap": s,
    "baseline_threshold_counts": counts,
    "matching_a0": str(a0),
    "fixed_cutoff": str(right),
    "flat": str(flat),
    "old_gamma": str(gamma),
    "kappa": str(kappa),
    "necessary_geometry_scale": str(gate),
    "minimizer_interval": [str(left),str(right)],
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks_passed":len(labels),"certificate":str(output)},ensure_ascii=False))
