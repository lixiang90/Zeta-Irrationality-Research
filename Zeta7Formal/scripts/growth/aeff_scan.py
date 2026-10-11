# Assemble the Aeff(alpha) scan table from the per-alpha pickles produced by
# gen_pieces_b8_39.py / outer_gen_b8_39.py, recomputing the tail bound with the
# same formulas as tail_b8_39.py (cross-checked for alpha = 3/40 and 1/40).
# Usage: python aeff_scan.py          (all alphas must have pickles)
#        python aeff_scan.py a060 a050 ...   (subset)
import sys, os, math, pickle, json
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
SPECS = {   # slug: (LAM_NUM, LAM_DEN, AL_NUM, AL_DEN)
    'a060': (47, 50, 3, 50),
    'a050': (19, 20, 1, 20),
    'a045': (191, 200, 9, 200),
    'a040': (24, 25, 1, 25),
    'a030': (97, 100, 3, 100),
    'b8_39': (39, 40, 1, 40),   # (40:1:39) reference point
    'a075': (37, 40, 3, 40),    # (40:3:37) old tuning reference point
}

def tail_bound(lam, al):
    assert 2 * lam * 400 <= 1000
    CO_P = 8 * lam / al
    CO_C = 8 * lam / al ** 2
    Pbar = (CO_P - lam) / 6
    slack = 2 * math.ceil((CO_C + lam) / 60)
    G0 = lambda v: v * (1 - v) * (2 * v - 1) / 6
    def qT(i): return Fr((60 + i) // 3)
    def qT2(i): return Fr(math.floor((60 + i) * al / 3))
    def PT(i, x):
        f = x - qT(i); g = al * x - qT2(i)
        return CO_P * g * (1 - g) - lam * f * (1 - f)
    def CT(i, x):
        return CO_C * G0(al * x - qT2(i)) - lam * G0(x - qT(i))
    def PhiT(i, x):
        return PT(i, x) / x ** 2 + 2 * CT(i, x) / x ** 3 - Pbar / x ** 2 + lam / x - Fr(43, 32) / x ** 2
    val = PhiT(1140, Fr(400)) - PhiT(0, Fr(20)) + slack * (1 / Fr(20) ** 3 - 1 / Fr(400) ** 3)
    return val, slack

def integ(pieces, k=False):
    tot = Fr(0)
    for p in pieces:
        x0, x1 = Fr(p[0]), Fr(p[1])
        a, b = Fr(p[-2]), Fr(p[-1])
        tot += a * (1 / x0 - 1 / x1) + b / 2 * (1 / x0 ** 2 - 1 / x1 ** 2)
    return tot

def run(slug):
    ln, ld, an, ad = SPECS[slug]
    lam = Fr(ln, ld); al = Fr(an, ad)
    P = pickle.load(open(os.path.join(HERE, f'pieces_{slug}.pkl'), 'rb'))
    T = integ(P)
    for x0, x1, k, a, b in P:
        q = math.floor(Fr(x0))
        assert -2 * q - 8 <= k <= 8 * q + 20, (slug, x0, k, q)
    O = pickle.load(open(os.path.join(HERE, f'outer_pieces_{slug}.pkl'), 'rb'))
    outer = integ(O)
    tail, slack = tail_bound(lam, al)
    small = 8 * lam / 400
    Aeff = T + outer + tail + small
    return dict(slug=slug, lam=f"{ln}/{ld}", al=f"{an}/{ad}", npieces=len(P),
                nouter=len(O), T=[T.numerator, T.denominator], outer=[outer.numerator, outer.denominator],
                tail=[tail.numerator, tail.denominator], slack=slack, small=[small.numerator, small.denominator],
                Aeff=[Aeff.numerator, Aeff.denominator])

def fmt(q):
    return f"{q.numerator}/{q.denominator}"

if __name__ == '__main__':
    slugs = sys.argv[1:] or ['a060', 'a050', 'a045', 'a040', 'a030']
    rows = []
    print("| α | λ | 内区 (段数) | 外区 (段数) | 尾段 (slack) | 小素数 | **Aeff(α)** |")
    print("|---|---|---|---|---|---|---|")
    for s in slugs:
        r = run(s)
        rows.append(r)
        T = Fr(*r['T']); O = Fr(*r['outer']); Ta = Fr(*r['tail']); Sm = Fr(*r['small']); A = Fr(*r['Aeff'])
        print(f"| {r['al']} | {r['lam']} | {fmt(T)} = {float(T):.6f} ({r['npieces']}) | "
              f"{fmt(O)} = {float(O):.6f} ({r['nouter']}) | {fmt(Ta)} = {float(Ta):.6f} ({r['slack']}) | "
              f"{fmt(Sm)} = {float(Sm):.6f} | **{fmt(A)} = {float(A):.6f}** |")
    with open(os.path.join(HERE, '..', '..', '..', 'research', 'aeff_scan.json'), 'w') as fh:
        json.dump(rows, fh, indent=1)
    print("\nwrote research/aeff_scan.json")
