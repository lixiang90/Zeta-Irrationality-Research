# Outer pieces of Eout on [K/(2h), 3] = [1/(2 lam), 3].
# Kinks: f in {0,1/2} (1/2 grid), 2*lam*x in ZZ (1/(2 lam) grid), {al x} kinks
# (1/(2 al) grid), max-term kink at 2/CMAX. Validation mode '37' reproduces the
# old b=8 (40:3:37) outer integral exactly.
import sys, pickle, math, os
from fractions import Fraction as Fr
from table_b8_39 import Eout, lam, al, CMAX

TUNE = sys.argv[1] if len(sys.argv) > 1 else '39'
if TUNE == '37':
    assert (lam, al) == (Fr(37, 40), Fr(3, 40)), "run with LAM_NUM=37 LAM_DEN=40 AL_NUM=3 AL_DEN=40"
    lo, dens, out = Fr(20, 37), [Fr(1, 2), Fr(20, 3), Fr(20, 37), Fr(40, 37), Fr(40, 43), Fr(40, 29)], '/tmp/outer37.pkl'
else:
    assert lam + al == 1, f"expected lam + al = 1, got {lam} + {al}"
    lo = 1 / (2 * lam)
    dens = [Fr(1, 2), 1 / (2 * al), 1 / (2 * lam), 1 / lam, 1 / (1 + al), 2 / CMAX]
    slug = os.environ.get('SLUG', 'b8_39')
    out = f'outer_pieces_{slug}.pkl'
hi = Fr(3)

cands = set([lo, hi])
for den in dens:
    k = math.ceil(lo / den - Fr(1, 10 ** 9))
    while k * den <= hi:
        cands.add(k * den); k += 1
cands = sorted(c for c in cands if lo <= c <= hi)
pieces = []
for x0, x1 in zip(cands, cands[1:]):
    if x0 == x1: continue
    xs = [x0 + (x1 - x0) * Fr(i, 4) for i in (1, 2, 3)]
    ys = [Eout(x) for x in xs]
    a = (ys[1] - ys[0]) / (xs[1] - xs[0]); b = ys[0] - a * xs[0]
    assert ys[2] == a * xs[2] + b, f"Eout not affine on [{x0},{x1}]: {ys[2]} vs {a*xs[2]+b}"
    pieces.append((x0, x1, a, b))
tot = sum(a * (1 / x0 - 1 / x1) + b / 2 * (1 / x0 ** 2 - 1 / x1 ** 2)
          for x0, x1, a, b in pieces)
print(len(pieces), tot, float(tot))
if TUNE == '37':
    print("expected 263569/144000 =", float(Fr(263569, 144000)), "match:", tot == Fr(263569, 144000))
pickle.dump(pieces, open(out, 'wb'))
