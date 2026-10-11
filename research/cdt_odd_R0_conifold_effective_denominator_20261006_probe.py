"""NEW exact finite-prefix experiment; does not execute/import old math producers.

This script constructs the explicitly printed conifold recurrence from scratch.
Its data are finite evidence, not an all-n denominator proof or irrationality test.
First and only planned execution: after this NEW file is saved.
"""
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path
import json

N = 180

def series(initial, beta):
    c = [F(z) for z in initial]
    hn = F(1)
    for n in range(N - 2):
        an = (n + 3) * (n + 2)**2 * (n + 1)
        bn = F((n + 2) * (n + 1) * (8*n*n + 20*n + 15), 2)
        cn = F((n + 1) * (12*n**3 + 24*n*n + 23*n + 8), 2)
        en = F(64*n**4 + 32*n**3 + 40*n*n + 8*n + 1, 16)
        prev = c[n - 1] if n else F(0)
        c.append((bn*c[n + 2] - cn*c[n + 1] + en*c[n]
                  - F(2*n - 1, 2)**4*prev + F(beta, 16)*hn) / an)
        hn *= F(2*n - 1, 2*(n + 1))
    return c

def v2(z):
    e = 0
    while z and z % 2 == 0:
        z //= 2
        e += 1
    return e

ds = [1]
for n in range(1, N + 5):
    ds.append(lcm(ds[-1], n))

data = {name: series(init, beta) for name, init, beta in [
    ("g0", (1, 0, 0), 0), ("g1", (0, 1, 0), 0),
    ("g2", (0, 0, 1), 0), ("h", (0, 0, 0), 1),
]}
assert [data[s][3] for s in data] == [F(1, 192), F(-1, 3), F(5, 4), F(1, 192)]
records = {}
for name, coeff in data.items():
    power = 4 if name == "h" else 3
    residual = [z.denominator // gcd(z.denominator, ds[n+3]**power)
                for n, z in enumerate(coeff)]
    odd = [r // 2**v2(r) for r in residual]
    binary = [v2(r) for r in residual]
    records[name] = {
        "denominator_LCM_power": power,
        "prefix_max_binary_residual": max(binary),
        "largest_odd_residual": max(odd),
        "first_odd_residual_above_one": next((n for n,r in enumerate(odd) if r != 1), None),
        "max_binary_slope_plus_one": str(max((F(e,n+1) for n,e in enumerate(binary)), default=F(0))),
        "candidate_16_power_n_plus_one_prefix_integral": all(e <= 4*(n+1) and o == 1
                                                           for n,e,o in zip(range(len(coeff)),binary,odd)),
        "binary_residual_by_index": binary,
        "odd_residual_by_index": odd,
        "coefficients": [str(z) for z in coeff],
    }
out = {
    "status": "finite_exact_recurrence_data_only",
    "prefix_degree": N,
    "executions_planned": 1,
    "old_or_peer_math_producers_executed_or_imported": 0,
    "scope": "Finite local Taylor prefixes only; no all-n theorem, effective optimal C, Betti comparison or numerical irrationality claim.",
    "records": records,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n",encoding="utf-8")
print(json.dumps({s:{k:v for k,v in r.items() if k not in
                     ["coefficients","binary_residual_by_index","odd_residual_by_index"]}
                  for s,r in records.items()},ensure_ascii=False,indent=2))
