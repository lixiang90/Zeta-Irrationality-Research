"""NEW FIRST1 mechanism verification, r=1,2,4 only; no nonzero-prime table.
No old/peer producer import or execution. Exclusive guard prevents rerun.
"""
from pathlib import Path
import hashlib
import json
import math
import traceback

BASE = Path(__file__).resolve()
GUARD = BASE.with_suffix(".guard.json")
OUT = BASE.with_suffix(".json")
with GUARD.open("x", encoding="utf-8") as f:
    json.dump({"state": "STARTED_FIRST1", "scope": "fixed-middle Racah identities only"}, f)

checks = 0
def check(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)

def tr(a):
    return [list(x) for x in zip(*a)]

def mm(a, b, p):
    bt = tr(b)
    return [[sum(x*y for x, y in zip(row, col)) % p for col in bt] for row in a]

def add(a, b, p, sign=1):
    return [[(x+sign*y) % p for x, y in zip(ar, br)] for ar, br in zip(a, b)]

def rank(a, p):
    b = [row[:] for row in a]
    r = 0
    for j in range(len(b[0])):
        piv = next((i for i in range(r, len(b)) if b[i][j] % p), None)
        if piv is None:
            continue
        b[r], b[piv] = b[piv], b[r]
        z = pow(b[r][j], -1, p)
        b[r] = [(v*z) % p for v in b[r]]
        for i in range(len(b)):
            if i != r:
                z = b[i][j]
                b[i] = [(x-z*y) % p for x, y in zip(b[i], b[r])]
        r += 1
        if r == len(b):
            break
    return r

def det(a, p):
    b = [row[:] for row in a]
    ans = 1
    n = len(b)
    for j in range(n):
        piv = next((i for i in range(j, n) if b[i][j] % p), None)
        if piv is None:
            return 0
        if piv != j:
            b[j], b[piv] = b[piv], b[j]
            ans = -ans
        z = b[j][j] % p
        ans = ans*z % p
        zi = pow(z, -1, p)
        for i in range(j+1, n):
            q = b[i][j]*zi % p
            for k in range(j, n):
                b[i][k] = (b[i][k]-q*b[j][k]) % p
    return ans % p

def inverse(a, p):
    n = len(a)
    b = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        piv = next(i for i in range(j, n) if b[i][j] % p)
        b[j], b[piv] = b[piv], b[j]
        z = pow(b[j][j], -1, p)
        b[j] = [x*z % p for x in b[j]]
        for i in range(n):
            if i != j:
                z = b[i][j]
                b[i] = [(x-z*y) % p for x, y in zip(b[i], b[j])]
    return [row[n:] for row in b]

def diag(xs):
    return [[x if i == j else 0 for j in range(len(xs))] for i, x in enumerate(xs)]

def poch(x, n, p):
    return math.prod((x+j) % p for j in range(n)) % p

def gram(evals, weights, p):
    return [[sum(w*x*y for w, x, y in zip(weights, a, b)) % p
             for b in evals] for a in evals]

def case(r):
    p = 18*r+1
    a = 5*r
    d = 3*r
    half = pow(2, -1, p)
    fac = [math.factorial(i) % p for i in range(3*a+1)]
    sval = [math.prod((k*k-j*j) % p for j in range(a+1, 9*r+1)) % p
            for k in range(a+1)]
    s0 = sval[0]
    full = [half*pow(sval[0], 3, p) % p] + [pow(s, 3, p) for s in sval[1:]]
    mid = [full[k] if k < r else 0 for k in range(a+1)]
    for k in range(a+1):
        w = 1 if k == 0 else 2*pow(poch(-a, k, p)*pow(poch(a+1, k, p), -1, p), 3, p)
        check(2*full[k] % p == pow(s0, 3, p)*w % p, "halfjet Racah weight")
    h0 = fac[3*a]*pow(fac[a], 3, p)*pow(pow(fac[2*a], 3, p), -1, p) % p
    hs, kappas, ds, ev = [], [], [], []
    for n in range(a+1):
        kn = poch(n-3*a-1, n, p)*pow(pow(poch(-a, n, p), 3, p), -1, p) % p
        hn = h0*poch(n-3*a-1, n, p)*fac[n]*pow(poch(-2*a, n, p), 3, p)
        hn = hn*pow(poch(-3*a, 2*n, p)*pow(poch(-a, n, p), 3, p) % p, -1, p) % p
        hs.append(hn)
        kappas.append(kn)
        ds.append(half*pow(s0, 3, p)*hn % p)
        check(hn != 0 and kn != 0, "all complete norms and leading units")
        row = []
        for k in range(a+1):
            ans = 0
            for j in range(n+1):
                den = pow(poch(-a, j, p), 3, p)*fac[j] % p
                ans += poch(-n, j, p)*poch(n-3*a-1, j, p)*poch(-k, j, p)*poch(k, j, p)*pow(den, -1, p)
            row.append(ans % p)
        ev.append(row)
    norms = gram(ev, full, p)
    for i in range(a+1):
        for j in range(a+1):
            check(norms[i][j] == (ds[i] if i == j else 0), "complete Racah orthogonality")
    mon = [[pow(k*k, i, p) for k in range(a+1)] for i in range(d)]
    D = gram(mon, full, p)
    Di = inverse(D, p)
    check(det(D, p) == math.prod(ds[n]*pow(kappas[n]*kappas[n] % p, -1, p) % p for n in range(d)) % p, "complete determinant")
    V = [[pow(k*k, i, p) for k in range(r)] for i in range(d)]
    E = diag(full[:r])
    H = gram(mon, [(x+y) % p for x, y in zip(full, mid)], p)
    check(H == add(D, mm(mm(V, E, p), tr(V), p), p), "actual H update")
    check(rank(mm(mm(V, E, p), tr(V), p), p) == r, "middle rank exactly r")
    K = mm(mm(tr(V), Di, p), V, p)
    for k in range(r):
        for l in range(r):
            spectral = sum(ev[n][k]*ev[n][l]*pow(ds[n], -1, p) for n in range(d)) % p
            check(K[k][l] == spectral, "known spectral kernel")
            if k != l:
                x, y = k*k % p, l*l % p
                pn_x, pn_y = ev[d][k]*pow(kappas[d], -1, p), ev[d][l]*pow(kappas[d], -1, p)
                pm_x, pm_y = ev[d-1][k]*pow(kappas[d-1], -1, p), ev[d-1][l]*pow(kappas[d-1], -1, p)
                rho = ds[d-1]*pow(kappas[d-1]*kappas[d-1] % p, -1, p) % p
                cd = (pn_x*pm_y-pm_x*pn_y)*pow(rho*(x-y) % p, -1, p) % p
                check(cd == spectral, "CD distinct-node formula")
    hg = gram(ev[:d], [(x+y) % p for x, y in zip(full, mid)], p)
    lambdas = [n*(n-3*a-1) % p for n in range(d)]
    bcut = -a**3 % p if r == 1 else (r-1-a)**3*pow(2*(2*r-1), -1, p) % p
    omega = full[r-1]*bcut % p
    comm = [[(lambdas[i]-lambdas[j])*hg[i][j] % p for j in range(d)] for i in range(d)]
    for i in range(d):
        for j in range(d):
            rhs = omega*(ev[i][r]*ev[j][r-1]-ev[i][r-1]*ev[j][r]) % p
            check(comm[i][j] == rhs, "actual rank-two boundary displacement")
        check(any(hg[j][i] for j in range(d)), "no spectral coordinate in actual H kernel")
    check(rank(comm, p) == 2, "rank-two exact")
    tmon = mon[:r]
    wg, wc = [], []
    for k, s in enumerate(sval):
        fold = half if k == 0 else 1
        inner = fold if k < r else 0
        wg.append((fold+inner)*pow(s, -5, p) % p)
        wc.append((5*fold-inner)*pow(s, -1, p) % p)
    G = gram(tmon, wg, p)
    C = [[sum(w*x*y for w, x, y in zip(wc, row, col)) % p for col in mon] for row in tmon]
    CDi = mm(C, Di, p)
    CDiV = mm(CDi, V, p)
    n11 = add(G, mm(CDi, tr(C), p), p, -1)
    n22 = [[(-x-y) % p for x, y in zip(ar, br)] for ar, br in zip(inverse(E, p), K)]
    N = [ar + [(-x) % p for x in br] for ar, br in zip(n11, CDiV)]
    N += [[(-x) % p for x in ar] + br for ar, br in zip(tr(CDiV), n22)]
    M = [ar+br for ar, br in zip(G, C)] + [ar+br for ar, br in zip(tr(C), H)]
    check(det(M, p) == pow(-1, r, p)*det(E, p)*det(D, p)*det(N, p) % p, "actual 4r-to-2r determinant")
    check(4*r-rank(M, p) == 2*r-rank(N, p), "actual corank equality")
    return {"r": r, "p": p, "complete_profiles": a+1, "actual_profile": [r, 3*r],
            "mechanisms": ["halfjet", "Racah norms", "CD", "middle update",
                           "rank-two flux", "fixed M5 bordered determinant", "corank"],
            "asserted_infinite_units": False, "asserted_M5_unit": False}

try:
    cases = [case(r) for r in [1, 2, 4]]
    payload = {"state": "PASS_FIRST1", "successful_runs": 1, "failed_runs": 0,
               "old_or_peer_execution_import_rerun": 0, "checks": checks, "cases": cases,
               "scope": "mechanism identities only; no prime table extension or M5 unit assertion",
               "source_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False))
except BaseException as exc:
    payload = {"state": "FAILED_FIRST1", "successful_runs": 0, "failed_runs": 1,
               "checks_before_failure": checks, "error": repr(exc),
               "traceback": traceback.format_exc(), "source_sha256": hashlib.sha256(BASE.read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False))
    raise
