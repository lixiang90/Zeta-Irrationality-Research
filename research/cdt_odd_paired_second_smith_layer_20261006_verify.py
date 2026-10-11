"""NEW first-only exact finite verifier of actual primitive CRT blocks.

No old/peer input is read, imported, or run.  The JSON guard is created before
arithmetic begins; any failed first execution remains visible and cannot rerun.
The all-scale theorem is the MD proof, not this finite check.
"""
from fractions import Fraction
from math import comb, factorial, gcd, isqrt
from pathlib import Path
import hashlib
import json

OUTPUT = Path(__file__).with_suffix(".json")
if OUTPUT.exists():
    raise SystemExit("first-only guard: output already exists")
OUTPUT.write_text(json.dumps({"status": "first_execution_started"}), encoding="utf-8")


def primes_upto(bound):
    return [p for p in range(2, bound + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def vp(value, p):
    if value == 0:
        return 10**9
    value = Fraction(value)
    numerator, denominator = abs(value.numerator), value.denominator
    ans = 0
    while numerator % p == 0:
        numerator //= p
        ans += 1
    while denominator % p == 0:
        denominator //= p
        ans -= 1
    return ans


def exact_dvr_smith(matrix, p):
    """Min-valuation pivots and exact Schur complements; Z_p operations.

    The minimum pivot makes every elimination multiplier p-integral.  The
    remaining valuations therefore give the exact rectangular Smith layers.
    Fractions preserve all higher actual units, rather than mod-p substitutes.
    """
    a = [[Fraction(v) for v in row] for row in matrix]
    result = []
    while a:
        candidates = [(vp(v, p), i, j)
                      for i, row in enumerate(a)
                      for j, v in enumerate(row) if v]
        assert candidates, "unexpected deficient block"
        val, i, j = min(candidates)
        assert val >= 0, "nonintegral actual image"
        a[0], a[i] = a[i], a[0]
        for row in a:
            row[0], row[j] = row[j], row[0]
        pivot = a[0][0]
        result.append(val)
        a = [[a[r][c] - a[r][0] * a[0][c] / pivot
              for c in range(1, len(a[0]))]
             for r in range(1, len(a))]
    assert result == sorted(result)
    return result


def local_eval(l, j, p):
    return p**j * factorial(j) * comb(l, j) if l >= j else 0


checks = 0
cases = []
block_total = 0
for n in range(18, 65):
    kmax, pole_length = 2*n - 1, 6*n + 1
    d = [factorial(k + pole_length) // factorial(k) for k in range(2*n)]
    for p in primes_upto(n):
        if not (n/2 < p <= n and p*p > 8*n and p > 17):
            continue
        a, z = divmod(kmax, p)
        h, e = divmod(pole_length, p)
        tau = p-e
        seen = set()
        smith = []
        types = {}
        mixed, mixed4 = 0, 0
        for r in range(p):
            if r in seen:
                continue
            s = (z-r) % p
            seen.update((r, s))
            sites_r = list(range(r, kmax+1, p))
            sites_s = list(range(s, kmax+1, p))
            length = len(sites_r)
            assert length == len(sites_s) and 2 <= length <= 4
            rows = []
            if r == s:
                assert length % 2 == 0
                for l in range(length//2):
                    k, mirror = sites_r[l], sites_r[length-1-l]
                    content = gcd(d[k], d[mirror])
                    q, pp = d[mirror]//content, d[k]//content
                    rows.append([q*local_eval(l, j, p)
                                 - pp*local_eval(length-1-l, j, p)
                                 for j in range(length)])
                predicted = [0] if length == 2 else [0, 1]
                kind = "center_L" + str(length)
            else:
                different = (r >= tau) != (s >= tau)
                for l in range(length):
                    k, mirror = sites_r[l], sites_s[length-1-l]
                    assert k+mirror == kmax
                    content = gcd(d[k], d[mirror])
                    q, pp = d[mirror]//content, d[k]//content
                    rows.append([q*local_eval(l, j, p) for j in range(length)]
                                + [-pp*local_eval(length-1-l, j, p)
                                   for j in range(length)])
                if different:
                    predicted = {2: [0, 1], 3: [0, 1, 1],
                                 4: [0, 1, 1, 2]}[length]
                    mixed += 1
                    mixed4 += int(length == 4)
                else:
                    predicted = {2: [0, 0], 3: [0, 0, 1],
                                 4: [0, 0, 1, 1]}[length]
                kind = ("mixed" if different else "same") + "_L" + str(length)
            actual = exact_dvr_smith(rows, p)
            assert actual == predicted, (n, p, r, s, kind, actual, predicted)
            checks += 1
            block_total += 1
            types[kind] = types.get(kind, 0) + 1
            smith.extend(actual)
        mh = max(0, min(tau, z+1-tau, (z+1)//2))
        mt = max(0, min(tau-z-1, p-tau, (p-z-1)//2))
        m4 = mh if a == 3 else 0
        assert (mixed, mixed4) == (mh+mt, m4)
        checks += 1
        predicted_counts = [p-mixed, n-p+mixed-mixed4, mixed4]
        actual_counts = [smith.count(v) for v in range(3)]
        assert actual_counts == predicted_counts and len(smith) == n
        checks += 1
        delta = sum(smith)
        assert delta == n-p+mixed+mixed4
        checks += 1
        cases.append({"n": n, "p": p, "a": a, "z": z, "h": h,
                      "e": e, "M_head": mh, "M_tail": mt, "M4": m4,
                      "smith_counts_012": actual_counts, "delta": delta,
                      "block_types": types})

assert cases and any(c["M4"] > 0 for c in cases)
output = {"status": "PASS", "first_execution_only": True,
          "scope": "finite actual exact primitive CRT blocks, n18..64, p>17, n/2<p<=n, p^2>8n",
          "old_or_peer_inputs_read": 0,
          "old_or_peer_producers_executed_or_imported": 0,
          "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "case_count": len(cases), "block_count": block_total,
          "asserted_checks": checks, "cases": cases,
          "not_claimed": "Finite checks are not the all-scale proof or an auxiliary-prime unit theorem."}
OUTPUT.write_text(json.dumps(output, indent=2), encoding="utf-8")
print(json.dumps({key: output[key] for key in ("status", "case_count", "block_count", "asserted_checks")}))
