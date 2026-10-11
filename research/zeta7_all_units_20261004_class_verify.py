"""Exhaustive independent audit of the small-depth p2 protected root classes.

The bounded producer was launched before its initial-empty-tree label fix.
This audit records the single zero-class label correction without overwriting
the producer data, and exhausts all unit pairs for each completed positive set.
"""
import hashlib
import json
import sys
from pathlib import Path
from flint import fmpq as Q

sys.set_int_max_str_digits(0)
folder = Path(__file__).parent


def v2(c):
    n, d = abs(int(c.numerator)), int(c.denominator)
    return ((n & -n).bit_length()-1)-((d & -d).bit_length()-1)


def main():
    names = ["zeta7_two_moment_partial_20261004_coefficients.json",
             "zeta7_joint_lattice_20261004_completion.json",
             "zeta7_all_units_20261004_hensel_p2.json"]
    source, baseline, h = [json.loads((folder/n).read_text(encoding="utf-8")) for n in names]
    coeff = [(r["i"], r["j"], [Q(c) for c in r["polynomial_coefficients"]])
             for r in source["coefficients"]]
    v0 = v2(Q(baseline["original_baseline_content"]))
    result = []
    for row in h["rows"]:
        a = row["a"]
        for saved in row["cases"]:
            if saved["status"] != "protected_root_classes":
                continue
            x_only = "b_range" in saved
            b = saved["b_range"][0] if x_only else saved["b"]
            weighted = [(i, j, k, c*Q(2)**(i*a+j*b))
                        for i, j, cs in coeff if not (x_only and j)
                        for k, c in enumerate(cs) if c]
            m = min(v2(c) for i, j, k, c in weighted)
            D = v0 - m
            assert D == saved["depth"] and D <= 7
            modulus = 2**D
            polys = {}
            for i, j, k, c in weighted:
                c = c / Q(2)**m
                if v2(c) >= D:
                    continue
                n, d = int(c.numerator), int(c.denominator)
                assert d % 2
                polys.setdefault(k, []).append((i, j, n*pow(d, -1, modulus) % modulus))

            def zero(u, v):
                up = [pow(u, i, modulus) for i in range(11)]
                vp = [pow(v, j, modulus) for j in range(3)]
                return all(sum(c*up[i]*vp[j] for i, j, c in terms) % modulus == 0
                           for terms in polys.values())

            tested = (modulus//2) * (1 if x_only else modulus//2)
            roots = {(u, v) for u in range(1, modulus, 2)
                     for v in ([1] if x_only else range(1, modulus, 2)) if zero(u, v)}
            saved_roots = {tuple(map(int, r)) for r in saved["roots"]}
            assert roots == saved_roots and len(roots) == saved["classes"]
            correction = not bool(roots)
            result.append(dict(a=a, b=saved.get("b"), b_range=saved.get("b_range"),
                               target_power=D, all_unit_pairs_directly_evaluated=tested,
                               exact_protected_classes=len(roots),
                               independently_corrected_classification="excluded_all_units" if correction else "protected_root_classes",
                               producer_empty_class_label_needs_correction=correction))
            print("full classes audit", a, b, "pairs", tested, "roots", len(roots), flush=True)
    assert sum(r["producer_empty_class_label_needs_correction"] for r in result) == 1
    out = dict(status="passed", results=result,
               file_hashes={n: hashlib.sha256((folder/n).read_bytes()).hexdigest() for n in names},
               scope="Every listed positive class set is complete by direct exhaustive residue evaluation. The one producer classes=0 label is an empty protection set, not existence. Original producer JSON preserved.")
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
