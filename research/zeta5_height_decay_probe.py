"""Primitive height/value budgets from the exact cached Hankel polynomials.

Finite Arb enclosures only; these do not establish asymptotic rates or
irrationality of any new number. --rebuild-pure independently reconstructs
the pure zeta(5) determinant before comparing every coefficient.
"""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

from flint import arb, arb_poly, ctx

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent


def short_ball(x):
    return x.str(45)


def run(ns, rebuild_pure=False):
    if rebuild_pure:
        import zeta35_mixed_moments as mixed
        from zeta35_target31 import content_and_primitive
    records = []
    for n in ns:
        path = ROOT / f"zeta35_target31_n{n}.json"
        raw = path.read_bytes()
        data = json.loads(raw)
        K = data["K"]
        if rebuild_pure:
            k, N, h, A, B = mixed.original.entries(n)
            poly = mixed.original.det_poly(h, A, B)
            content, rebuilt = content_and_primitive(poly)
            pure = next(r for r in data["rows"] if r["a"] == 0)
            assert k == K and str(content) == pure["content"]
            assert rebuilt == list(map(int, pure["primitive_coefficients"]))
        for row in data["rows"]:
            coefficients = list(map(int, row["primitive_coefficients"]))
            assert math.gcd(*coefficients) == 1
            assert len(coefficients) - 1 == data["h"] == row["degree"]
            height = max(map(abs, coefficients))
            ctx.prec = height.bit_length() + 2*K*K + 2000
            theta = arb(5).zeta() + row["a"]*arb(3).zeta()
            value = arb_poly(coefficients)(theta)
            assert value > 0
            log_value = value.log()
            log_height = arb(height).log()
            # l2 coefficient norm bounds Mahler measure. The lower bound
            # follows |c_j| <= binom(deg,j) M(P) <= 2^deg M(P).
            log_mahler_lower = log_height - row["degree"]*arb(2).log()
            log_mahler_upper = arb(sum(c*c for c in coefficients)).log()/2
            record = dict(
                n=n, K=K, N=data["N"], h=data["h"], a=row["a"],
                target="zeta(5)" if row["a"] == 0 else f"{row['a']}*zeta(3)+zeta(5)",
                source=path.name, source_sha256=hashlib.sha256(raw).hexdigest(),
                primitive_gcd=1, degree=row["degree"],
                height_bit_length=height.bit_length(),
                max_coefficient_index=max(range(len(coefficients)), key=lambda i: abs(coefficients[i])),
                log_height=short_ball(log_height),
                height_rate=short_ball(log_height/(K*K)),
                log_value=short_ball(log_value),
                decay_rate=short_ball(-log_value/(K*K)),
                decay_height_ratio=short_ball(-log_value/log_height),
                quadratic_norm_budget=short_ball((-log_value-log_height)/(K*K)),
                mahler_rate_lower=short_ball(log_mahler_lower/(K*K)),
                mahler_rate_upper=short_ball(log_mahler_upper/(K*K)),
                pure_coefficients_rebuilt=bool(rebuild_pure and row["a"] == 0),
                status="finite_exact_and_arb_checks_passed",
            )
            # The cache's rounded float is used only as a redundant check.
            assert abs(float(log_value) - row["log_p"]) < 1e-8
            records.append(record)
            print(f"K={K} a={row['a']} height/K2={float(log_height/(K*K)):.9f} "
                  f"decay/K2={float(-log_value/(K*K)):.9f} "
                  f"decay/height={float(-log_value/log_height):.9f}", flush=True)
    result = dict(
        scope="finite primitive polynomial height/decay budgets, not asymptotic claims",
        precision="adaptive Arb: height bits + 2*K^2 + 2000",
        source_definition="D_N(t)^6/D_K(t), K=40n, N=3n, h=37n",
        records=records,
    )
    (ROOT / "zeta5_height_decay_probe.json").write_text(
        json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs="*", type=int, default=[1, 2, 3])
    parser.add_argument("--rebuild-pure", action="store_true")
    args = parser.parse_args()
    run(args.n, args.rebuild_pure)
