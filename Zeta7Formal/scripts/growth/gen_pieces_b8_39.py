# Robust pieces of min_k Ein(.,k) on [3,20]: candidate k's = minimizers at 19 sample
# points + 5 best at midpoint; then a verification pass scans every merged piece and
# adds any globally-better k (fixpoint). Mirrors the original gen_pieces.py but
# guarantees the exact lower envelope.
import sys, pickle, math, os
sys.setrecursionlimit(10000)
from fractions import Fraction as Fr
from table_b8_39 import Ein, lam, al, CMAX

TUNE = sys.argv[1] if len(sys.argv) > 1 else '39'
if TUNE == '37':   # validation mode: reproduce the old b=8 (40:3:37) table
    assert (lam, al) == (Fr(37, 40), Fr(3, 40)), "run with LAM_NUM=37 LAM_DEN=40 AL_NUM=3 AL_DEN=40"
    dens = [Fr(1, 2), Fr(20, 3), Fr(20, 37), Fr(40, 37), Fr(40, 43)]
    out = '/tmp/pieces37.pkl'
else:
    # generic tuning from env: kink-separating dens are alpha-only
    assert lam + al == 1, f"expected lam + al = 1, got {lam} + {al}"
    dens = [Fr(1, 2), 1 / (2 * al), 1 / (2 * lam), 1 / lam, 1 / (1 + al)]
    slug = os.environ.get('SLUG', 'b8_39')
    out = f'pieces_{slug}.pkl'

KMIN = int(os.environ.get('KMIN', -40))
KMAX = int(os.environ.get('KMAX', 240))

lo, hi = Fr(3), Fr(20)
cands = set([lo, hi])
for den in dens:
    k = math.ceil(lo / den)
    while k * den <= hi:
        cands.add(k * den); k += 1
cands = sorted(c for c in cands if lo <= c <= hi)

def lin(x0, x1, k):
    xs = [x0 + (x1 - x0) * Fr(i, 4) for i in (1, 2, 3)]
    ys = [Ein(x, k) for x in xs]
    a = (ys[1] - ys[0]) / (xs[1] - xs[0]); b = ys[0] - a * xs[0]
    assert ys[2] == a * xs[2] + b, f"not linear on [{x0},{x1}] k={k}"
    return a, b

# extra candidate k's collected by the verification pass
extra = set()
for it in range(6):
    pieces = []
    for x0, x1 in zip(cands, cands[1:]):
        mid = (x0 + x1) / 2
        cand = set(extra)
        cand.update(sorted(range(KMIN, KMAX), key=lambda k: Ein(mid, k))[:5])
        for t in [Fr(i, 20) for i in range(1, 20)]:
            x = x0 + (x1 - x0) * t
            cand.add(min(range(KMIN, KMAX), key=lambda k: Ein(x, k)))
        lines = {k: lin(x0, x1, k) for k in cand}
        cur = x0
        while cur < x1:
            xm = cur + (x1 - cur) / 1000
            kbest = min(lines, key=lambda k: (lines[k][0] * xm + lines[k][1], lines[k][0]))
            a, b = lines[kbest]
            nxt = x1
            for k, (a2, b2) in lines.items():
                if a2 < a:
                    xc = (b2 - b) / (a - a2)
                    if cur < xc < nxt: nxt = xc
            pieces.append((cur, nxt, kbest, a, b))
            cur = nxt
    merged = []
    for p in pieces:
        if merged and merged[-1][2:] == p[2:] and merged[-1][1] == p[0]:
            merged[-1] = (merged[-1][0], p[1]) + p[2:]
        else:
            merged.append(p)
    # verification: scan each merged piece; if some k beats the line, record it
    extra = set()
    viol = 0
    for (x0, x1, k, a, b) in merged:
        for r in range(1, 40):
            x = x0 + (x1 - x0) * Fr(r, 40)
            kb = min(range(KMIN, KMAX), key=lambda kk: Ein(x, kk))
            if Ein(x, kb) < a * x + b:
                extra.add(kb); viol += 1
    print(f"iter {it}: pieces {len(merged)}, violations {viol}")
    if not viol:
        break
if viol:
    raise SystemExit("could not reach fixpoint")

tot = Fr(0)
for (x0, x1, k, a, b) in merged:
    q = math.floor(x0)
    assert -2 * q - 8 <= k <= 8 * q + 20, f"k={k} not admissible for q={q}"
    tot += a * (1 / x0 - 1 / x1) + b / 2 * (1 / x0 ** 2 - 1 / x1 ** 2)
print("pieces", len(merged), "integral", tot, float(tot))
pickle.dump(merged, open(out, 'wb'))
