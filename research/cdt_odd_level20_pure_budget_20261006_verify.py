"""Exact finite audit of specified pure10 plus T4/T5 safe denominator types.

This computes lower bounds on tau-double, never substitutes row sums as safe
tau-double. The finite exponent/type choices are supplied by the companion
pure-helper proof, not fitted to primes or unknown numerical periods.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from pathlib import Path
import ast
import hashlib
import json
import sympy as sp

here = Path(__file__).resolve().parent
# Load only the two exact rational integral functions, not the producer body.
source = here/"cdt_odd_level20_arithmetic_20261006_verify.py"
tree = ast.parse(source.read_text(encoding="utf8"))
functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)
             and n.name in ("Ipieces", "sharp")]
assert len(functions) == 2
x = sp.symbols("x")
H = lambda n: sum((sp.Rational(1, j) for j in range(1, n+1)), sp.Rational(0))
exec(compile(ast.Module(body=functions, type_ignores=[]), "<sharp integral>", "exec"))
sharp = lru_cache(None)(sharp)

names = ["L", "T2", "Li2", "Li3", "T3", "L*Li2", "Li1,2", "I_K"]
base_options = [
    [(1, 0), (0, 1)],
    [(sp.Rational(3, 2), 0), (1, 1)],
    [(2, 0), (1, 1), (0, 2)],
    [(3, 0), (2, 1), (1, 2), (0, 3)],
    [(sp.Rational(11, 6), 0), (sp.Rational(3, 2), 1)],
    [(sp.Rational(5, 2), 0), (2, 1)],
    [(sp.Rational(5, 2), 0), (2, 1)],
    [(3, 0), (2, 1)],
]
families = []
for R in (3, 4, 5):
    options = base_options + [[(H(j), 0), (H(j-1), 1)] for j in range(4, R+1)]
    row_names = names+[f"T{j}" for j in range(4, R+1)]
    m = R+10
    buckets = {}
    count = 0
    best = None
    for choices in product(*options):
        count += 1
        sigmas = sorted([sp.Rational(0), sp.Rational(2)]
                        +[sp.Rational(s) for s, e in choices]+[sp.Rational(3)]*3)
        es = [e for s, e in choices]
        key = sum(es), max(es)
        flat = sum((2*i+1)*v for i, v in enumerate(sigmas))/m**2
        sh, xi = sharp(m, *key)
        total = flat+sh
        if key not in buckets:
            buckets[key] = {"type_count":0, "minimum_row_lower":flat,
                            "representative_choices":choices}
        buckets[key]["type_count"] += 1
        if flat < buckets[key]["minimum_row_lower"]:
            buckets[key]["minimum_row_lower"] = flat
            buckets[key]["representative_choices"] = choices
        if best is None or total < best[0]:
            best = total, choices, flat, sh, xi
    assert count == 768*2**(R-3)
    assert sum(b["type_count"] for b in buckets.values()) == count
    records = []
    for key, b in sorted(buckets.items()):
        sh, xi = sharp(m, *key)
        records.append({
            "sum_e":key[0], "max_e":key[1], "type_count":b["type_count"],
            "minimum_row_lower":str(b["minimum_row_lower"]),
            "sharp_exact":str(sh), "sharp_minimizer":str(xi),
            "minimum_total_lower":str(b["minimum_row_lower"]+sh),
            "representative_choices":[[str(s), e] for s, e in b["representative_choices"]],
        })
    assert min(sp.Rational(a["minimum_total_lower"]) for a in records) == best[0]
    families.append({
        "log_degree":R, "actual_rank_conditional_on_companion_proof":m,
        "target_rows":3, "specified_type_count":count,
        "row_names":row_names,
        "options_sigma_e":[[[str(s), e] for s, e in o] for o in options],
        "minimum_total_lower":str(best[0]),
        "minimum_row_lower":str(best[2]), "sharp_at_minimum":str(best[3]),
        "sharp_minimizer_at_minimum":str(best[4]),
        "best_choices":[[str(s), e] for s, e in best[1]],
        "necessary_rho_lower":str(sp.Rational(m, m-1)*best[0]),
        "all_sum_max_e_buckets":records,
    })

assert [a["minimum_total_lower"] for a in families] == ["1345/507", "2577/980", "1769/675"]
assert all(sp.Rational(a["necessary_rho_lower"]) > sp.Rational(14,5) for a in families)
assert sum(sp.Rational(14,5)**k/sp.factorial(k) for k in range(13)) > 16

baseline = []
for m, rows, sum_e in (
    (12, [0,0,1,1,2,2,2,2,2,3,3,3], 7),
    (13, [0,0,1,1,2,2,2,2,2,2,3,3,3], 8),
):
    flat = sum(sp.Rational(2*i+1)*v for i, v in enumerate(rows))/m**2
    sh, xi = sharp(m, sum_e, 1)
    baseline.append({"rank":m,"flat":str(flat),"sharp":str(sh),
                     "sharp_minimizer":str(xi),"safe_total":str(flat+sh),
                     "necessary_rho":str(sp.Rational(m,m-1)*(flat+sh))})
assert [a["safe_total"] for a in baseline] == ["54689/20160", "25477/9464"]
out = {
    "status":"exact_specified_pure_helper_type_audit_passed",
    "scope":"Exact lower audit for the explicitly listed safe type families; no global type optimum.",
    "arithmetic_integral_source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "baseline_complete_unit_tables":baseline,
    "families":families,
    "all_specified_family_necessary_thresholds_strictly_above_14_over_5":True,
    "exp_14_over_5_positive_series_lower_exceeds_16":True,
    "not_claimed":["row lower bounds equal tau-double",
                   "all possible denominators, rational gauges, or adaptive lattices are excluded",
                   "a new numerical irrationality theorem"],
}
(here/"cdt_odd_level20_pure_budget_20261006_verify.json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print(json.dumps({"status":out["status"],"families":[
    {"R":a["log_degree"],"m":a["actual_rank_conditional_on_companion_proof"],
     "types":a["specified_type_count"],"minimum_lower":a["minimum_total_lower"],
     "necessary_rho_lower":a["necessary_rho_lower"],"best_choices":a["best_choices"]}
    for a in families]}))
