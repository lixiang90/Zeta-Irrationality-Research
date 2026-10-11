"""NEW exact rational integration of the proved residue-minor lower-bound model.

No old/peer producer imports. This computes a bound model, not actual p-adic
orders and not a special-value theorem. Paper proof supplies its applicability.
"""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json


def fl(x):
    return x.numerator // x.denominator


def aff_value(ab, x):
    return ab[0] * x + ab[1]


def model_groups(s, x):
    a, b, c = fl(6 / x), fl(2 / x), fl(3 / x)
    thresholds = [(Q(0), Q(0)), (Q(-a), Q(6)),
                  (Q(b + 1), Q(-2)), (Q(1), Q(0))]
    thresholds.sort(key=lambda v: aff_value(v, x))
    groups = defaultdict(lambda: [Q(0), Q(0)])
    for lo, hi in zip(thresholds, thresholds[1:]):
        mass = (hi[0] - lo[0], hi[1] - lo[1])  # x * interval length
        if aff_value(mass, x) == 0:
            continue
        assert aff_value(mass, x) > 0
        u = (aff_value(lo, x) + aff_value(hi, x)) / (2 * x)
        q = fl(6 / x - u)
        w = 2 * int(u > 6 / x - a) + 3 * int(u >= 1 - (2 / x - b))
        exception = int(x > 6 - x * u and x > 2 + x * u)
        costs = []
        for m in range(1, 2 * (q + 1) + 1):
            cost = 2 * m + w - s - 2 + (s - 1) * int(m > 2 * q)
            cost += exception * (int(m == 1) - int(m == 2))
            costs.append(cost)
            groups[cost][0] += mass[0]
            groups[cost][1] += mass[1]
        assert costs == sorted(costs), (s, x, q, w, exception)
    return c, sorted((cost, (v[0], v[1])) for cost, v in groups.items())


def optimum_affine(s, x):
    c, groups = model_groups(s, x)
    used = (Q(0), Q(0))
    result = (Q(c * (c + 1)), Q(-6 * c))
    for cost, mass in groups:
        next_used = (used[0] + mass[0], used[1] + mass[1])
        if aff_value(next_used, x) >= 3:
            remaining = (-used[0], Q(3) - used[1])
            return (result[0] + cost * remaining[0], result[1] + cost * remaining[1])
        result = (result[0] + cost * mass[0], result[1] + cost * mass[1])
        used = next_used
    raise AssertionError("insufficient residue rank")


def pieces(s, epsilon):
    breaks = {epsilon, Q(6), Q(4)}
    # Floor boundaries and the order crossing of {6/x}, 1-{2/x}.
    for numerator in (2, 3, 6, 8):
        for k in range(1, fl(Q(numerator) / epsilon) + 1):
            z = Q(numerator, k)
            if epsilon < z < 6:
                breaks.add(z)
    ans = []
    bb = sorted(breaks)
    for left, right in zip(bb, bb[1:]):
        mid = (left + right) / 2
        _, groups = model_groups(s, mid)
        extra = {left, right}
        used = (Q(0), Q(0))
        for _, mass in groups:
            used = (used[0] + mass[0], used[1] + mass[1])
            if used[0]:
                z = (Q(3) - used[1]) / used[0]
                if left < z < right:
                    extra.add(z)
        ee = sorted(extra)
        for l, r in zip(ee, ee[1:]):
            ab = optimum_affine(s, (l + r) / 2)
            # Exact in-cell checks; validity for whole cell follows paper proof.
            for z in ((3*l+r)/4, (l+3*r)/4):
                assert aff_value(ab, z) == aff_value(optimum_affine(s, z), z)
            if ans and ans[-1][1] == l and ans[-1][2] == ab:
                ans[-1] = (ans[-1][0], r, ab)
            else:
                ans.append((l, r, ab))
    assert ans[0][0] == epsilon and ans[-1][1] == 6
    return ans


def serial(q):
    return str(q.numerator) if q.denominator == 1 else str(q)


def run(s, epsilon):
    pp = pieces(s, epsilon)
    integral = sum(a*(r*r-l*l)/2+b*(r-l) for l,r,(a,b) in pp)
    # g_s(x)>=-3s-29x/16 on (0,epsilon); from the paper's Cauchy bound.
    tail_lower = -3*s*epsilon - Q(29,32)*epsilon**2
    lower = integral + tail_lower
    return {
        "s": s, "epsilon": serial(epsilon), "piece_count": len(pp),
        "exact_main_integral": serial(integral),
        "proved_tail_lower_bound": serial(tail_lower),
        "global_sum_lower_bound": serial(lower),
        "safe_A_upper_bound": serial(-lower),
        "safe_A_decimal_for_orientation": float(-lower),
        "pieces": [{"left":serial(l),"right":serial(r),"slope":serial(a),"intercept":serial(b)}
                   for l,r,(a,b) in pp],
    }


if __name__ == "__main__":
    results = [run(s, Q(1, 100)) for s in (4, 5, 7)]
    output = {
        "status": "exact_residue_minor_model_integrated",
        "scope": "Exact LP lower-bound model only, not actual determinant valuations, not a proof of irrationality; applicability and tail are paper lemmas.",
        "new_producer_execution_ordinal": 1,
        "old_or_peer_producer_execution_import_rerun": 0,
        "results": results,
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps([{k:v for k,v in r.items() if k != "pieces"} for r in results],ensure_ascii=False))
