"""NEW, FIRST-ONLY: original saturated paired basis versus unit-tail rank.

No old or peer source/data is opened or imported. This finite mechanism check
does not prove the all-scale paper theorem. Its output is created exclusively
before any mathematical calculation, so a failure remains recorded.
"""
from pathlib import Path
from math import comb, factorial, gcd
import json
import traceback

OUT = Path(__file__).with_suffix('.json')
with OUT.open('x', encoding='utf-8') as handle:
    json.dump({'status': 'STARTED_NOT_PASS', 'first_only': True}, handle)


def prime(p):
    return p > 1 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def binom_z(z, i):
    if z >= 0:
        return comb(z, i) if i <= z else 0
    return (-1) ** i * comb(i - z - 1, i)


def rank(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for j in range(r + 1, len(a)):
            k = a[j][c]
            if k:
                a[j] = [(v - k * w) % p for v, w in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def dot(row, col, p):
    return sum(v * w for v, w in zip(row, col)) % p


checks = 0
cases = []
try:
    for n in range(1, 29):
        for p in range(7, 2 * n + 1):
            if not prime(p) or p * p <= 8 * n:
                continue
            degree = 3 * n
            aa, r2 = divmod(2 * n, p)
            qq, rr = divmod(3 * n, p)
            hh, r6 = divmod(6 * n, p)
            vv = p - r2
            uu = min(r6 + 1, vv)
            overlap = max(0, 2 * uu - vv)
            assert aa * overlap % 2 == 0
            ff = aa * uu - aa * overlap // 2
            predicted = qq * uu + min(rr, uu) - ff
            assert 0 <= predicted
            d = [None] + [factorial(6 * n + m) // factorial(m - 1)
                          for m in range(1, 2 * n + 1)]
            columns = []
            for m in range(1, n + 1):
                mirror = 2 * n + 1 - m
                gg = gcd(d[m], d[mirror])
                pm, qm = d[m] // gg, d[mirror] // gg
                col = [0] * degree
                for site, coeff in ((m, pm), (mirror, qm)):
                    for i in range(site - 1, 2 * n):
                        col[i] += coeff * (-1) ** (i - site + 1) * comb(i, site - 1)
                columns.append([v % p for v in col])
            for i in range(2 * n, degree):
                col = [0] * degree
                col[i] = 1
                columns.append(col)
            assert rank(list(map(list, zip(*columns))), p) == 2 * n
            checks += 1
            for m in range(1, n + 1):
                mirror = 2 * n + 1 - m
                gg = gcd(d[m], d[mirror])
                constraint = [(d[mirror] // gg * binom_z(m - 1, i)
                               - d[m] // gg * binom_z(mirror - 1, i)) % p
                              for i in range(degree)]
                assert all(dot(constraint, col, p) == 0 for col in columns)
                checks += len(columns)
            values, jets = [], []
            for rho in range(uu):
                for lift in range(1, hh + 1):
                    j = rho + lift * p
                    assert j <= 6 * n
                    row = [binom_z(-j - 1, i) % p for i in range(degree)]
                    derivative = [sum((-1) ** (k - 1) * pow(k, -1, p)
                                      * row[i - k * p]
                                      for k in range(1, i // p + 1)) % p
                                  for i in range(degree)]
                    values.append([dot(row, col, p) for col in columns])
                    jets.append([dot(derivative, col, p) for col in columns])
                    checks += 1
            value_rank = rank(values, p)
            hermite_rank = rank(values + jets, p)
            assert value_rank == hermite_rank
            checks += 1
            exact_domain = qq >= aa + 1
            assert value_rank <= predicted
            if exact_domain:
                assert value_rank == predicted
            checks += 1 + int(exact_domain)
            cases.append(dict(n=n, p=p, a=aa, Q=qq, R=rr, V=vv, u=uu,
                              supported_constraints=ff, predicted_rank=predicted,
                              actual_value_rank=value_rank,
                              actual_hermite_rank=hermite_rank,
                              exact_domain=exact_domain))
    assert cases and any(not c['exact_domain'] for c in cases)
    result = dict(status='PASS', first_only=True, own_run_count=1,
                  old_or_peer_producer_execution=0, cases=len(cases), checks=checks,
                  exact_cases=sum(c['exact_domain'] for c in cases),
                  cap_only_cases=sum(not c['exact_domain'] for c in cases),
                  all_scale_proof=False, records=cases)
    OUT.write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}))
except BaseException:
    OUT.write_text(json.dumps(dict(status='FAIL', first_only=True, own_run_count=1,
                                   old_or_peer_producer_execution=0, checks=checks,
                                   records=cases, error=traceback.format_exc()), indent=2),
                   encoding='utf-8')
    raise
