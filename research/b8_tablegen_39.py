#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8（ζ(7) 类比）Growth 三段表精确有理管道 + b=6 校准。

b 依赖公式（全部经 mo271 原文逐步核对，见 research/NOTES.md 进展 25）：
- Ein_b(x,k)  = -2λx⌊x⌋ + 2b·λx⌊αx⌋ + 2Jc(λx) - λx·k + 2Σ bIn_b·ccount，
  bIn_b 来自 psiR(k, 2b·q' - 2q - (b-2) + b·a' - a)。
- Eout_b(x)   = -2λx⌊x⌋ + 2Jc(λx) - 2Σ bGO_b·ccount + max(0, (λ+(b-1)α)x - 2)，
  GO_b(q,a,d) = Σ_{i<2q+a-2} min(0, i + 3d - (2q+a+(b-2))/2)。
- tail：Ftail_b = (b-2)λ + 2λ{x} - 2b·λ{αx}，加性常数 27/16；
  PT_b = (bλ/α)·g(1-g) - λf(1-f)，CT_b = (bλ/α²)G0(g) - λG0(f)，
  P̄_b = (bλ/α - λ)/6，PhiT = PT/x² + 2CT/x³ - P̄/x² + λ/x - (27/32)/x²，
  逐段 ≤ PhiT 差分 + 2M(1/l³-1/r³)，M = ⌈(bλ/α² + λ)/60⌉。
  tail 真值含 (2λ-2b·λα)·ln(400/20) 项（无理），mo271 式有理上界将其吸收。

校准（b=6 必须精确复现论文值）：
  内区 ∫_3^20  = 322437603634266857629/7535670527041937280000
  外区 ∫_{20/37}^3 = 129101/96000
  tail 有理上界 = -6843153/128000000
"""
from fractions import Fraction as F
import math, json

import os
LAM = F(int(os.environ.get('LAM_NUM', 37)), int(os.environ.get('LAM_DEN', 40)))
AL = F(int(os.environ.get('AL_NUM', 3)), int(os.environ.get('AL_DEN', 40)))
QD = int(3 / float(AL))  # qT' nat-divisor: 40 (old) / 120 (new)
INNER_DENS = [F(1, 2), 1 / (2 * AL), 1 / (2 * LAM), 1 / LAM, 1 / (1 + AL)]
OUTER_LO = 1 / (2 * LAM)   # K/(2h): 20/37 old, 20/39 new

def fl(x):
    return math.floor(x)

# ---------- 精确机器 ----------

def lrow(k, b):
    t = k - b + 1
    return max(0, t // 2)

def psiR(k, b):
    L = lrow(k, b)
    t = k - b
    return F(L * (t - L + 1), 2)

def bcoef(h):
    return [h(0), h(1) - h(0), h(2) - h(1)]

def cvLo(f):
    return [F(0), F(0), 1 - f]

def cvHi(f):
    return [F(1, 2), f, F(1, 2)]

def ccount(f, g, i, j):
    return max(F(0), min(min(cvHi(f)[i], cvHi(g)[j]), F(1, 2))
               - max(max(cvLo(f)[i], cvLo(g)[j]), F(0)))

def Jc_fast(u):
    mu = fl(2 * u)
    return mu * u - F(mu * (mu + 1), 4)

def make_Ein(b):
    def Ein(x, k):
        q = fl(x); qq = fl(AL * x)
        f = x - q; g = AL * x - qq
        B = 2 * b * qq - 2 * q - (b - 2)
        h = lambda a, bb: psiR(k, B + b * bb - a)
        s = F(0)
        for i in range(3):
            for j in range(3):
                c = bcoef(lambda a: bcoef(lambda bb: h(a, bb))[j])[i]
                s += c * ccount(f, g, i, j)
        u = LAM * x
        return -2 * u * q + 2 * b * u * qq + 2 * Jc_fast(u) - u * k + 2 * s
    return Ein

def make_Eout(b):
    def GO(q, a, d):
        L = 2 * q + a - 2
        if L <= 0:
            return F(0)
        return sum(min(F(0), i + 3 * d - F(2 * q + a + (b - 2), 2))
                   for i in range(L))
    def Eout(x):
        q = fl(x)
        f = x - q; g = AL * x - fl(AL * x)
        u = LAM * x
        s = F(0)
        for i in range(3):
            for j in range(3):
                c = bcoef(lambda a: bcoef(lambda bb: GO(q, a, bb))[j])[i]
                s += c * ccount(f, g, i, j)
        return (-2 * u * q + 2 * Jc_fast(u) - 2 * s
                + max(F(0), (LAM + (b - 1) * AL) * x - 2))
    return Eout

# ---------- 分段线性工具 ----------

def check_affine(fn, x0, x1, npts=8):
    """验证 fn 在 (x0,x1) 上仿射（npts 个内点），返回 (a,b)。"""
    xs = [x0 + (x1 - x0) * t / (npts + 1) for t in range(1, npts + 1)]
    ys = [fn(x) for x in xs]
    a = (ys[-1] - ys[0]) / (xs[-1] - xs[0])
    bb = ys[0] - a * xs[0]
    for x, y in zip(xs, ys):
        assert y == a * x + bb, f"not affine on ({x0},{x1}): at {x}"
    return a, bb

def grid(lo, hi, dens):
    cands = {lo, hi}
    for den in dens:
        k = math.ceil(lo / den)
        while k * den <= hi:
            cands.add(k * den)
            k += 1
    return sorted(c for c in cands if lo <= c <= hi)

# ---------- 内区：Ein 下包络 ----------

def inner_table(b, krange, topm=6, replica=False):
    Ein = make_Ein(b)
    lo, hi = F(3), F(20)
    cands = grid(lo, hi, INNER_DENS)
    pieces = []
    for x0, x1 in zip(cands, cands[1:]):
        mid = (x0 + x1) / 2
        ks = sorted(krange, key=lambda k: Ein(mid, k))[:topm]
        cand = set(ks)
        for t in range(1, 20):
            x = x0 + (x1 - x0) * F(t, 20)
            cand.add(min(krange, key=lambda k: Ein(x, k)))
        lines = {}
        for k in cand:
            if replica:
                # mo271 原算法：3 个内点校验
                xs = [x0 + (x1 - x0) * F(i, 4) for i in (1, 2, 3)]
                ys = [Ein(x, k) for x in xs]
                a = (ys[1] - ys[0]) / (xs[1] - xs[0]); bb = ys[0] - a * xs[0]
                assert ys[2] == a * xs[2] + bb, "not linear"
            else:
                a, bb = check_affine(lambda x, k=k: Ein(x, k), x0, x1)
            q = fl(x0)
            assert -2 * q - 6 <= k <= 8 * q + 20, \
                f"k={k} 越界于 q={q} (piece {x0},{x1})"
            lines[k] = (a, bb)
        # 下包络
        cur = x0
        while cur < x1:
            xm = cur + (x1 - cur) / 1000
            kbest = min(lines, key=lambda k: (lines[k][0] * xm + lines[k][1],
                                              lines[k][0]))
            a, bb = lines[kbest]
            nxt = x1
            for k, (a2, b2) in lines.items():
                if a2 < a:
                    xc = (b2 - bb) / (a - a2)
                    if cur < xc < nxt:
                        nxt = xc
            pieces.append((cur, nxt, kbest, a, bb))
            cur = nxt
    merged = []
    for p in pieces:
        if merged and merged[-1][2:] == p[2:] and merged[-1][1] == p[0]:
            merged[-1] = (merged[-1][0], p[1]) + p[2:]
        else:
            merged.append(list(p))
    tot = F(0)
    for x0, x1, k, a, bb in merged:
        tot += a * (1 / x0 - 1 / x1) + bb / 2 * (1 / x0 ** 2 - 1 / x1 ** 2)
    return merged, tot

# ---------- 外区：Eout 分段 ----------

def outer_table(b):
    Eout = make_Eout(b)
    lo, hi = OUTER_LO, F(3)
    boundary = F(2) / (LAM + (b - 1) * AL)  # max 项转折点
    cands = grid(lo, hi, [F(1, 2), 2 / (2 * AL), 1 / (2 * LAM), 1 / LAM, 1 / (1 + AL), boundary])
    pieces = []
    for x0, x1 in zip(cands, cands[1:]):
        a, bb = check_affine(Eout, x0, x1)
        pieces.append((x0, x1, a, bb))
    merged = []
    for p in pieces:
        if merged and merged[-1][2:] == p[2:] and merged[-1][1] == p[0]:
            merged[-1] = (merged[-1][0], p[1]) + p[2:]
        else:
            merged.append(list(p))
    tot = F(0)
    for x0, x1, a, bb in merged:
        tot += a * (1 / x0 - 1 / x1) + bb / 2 * (1 / x0 ** 2 - 1 / x1 ** 2)
    return merged, tot

# ---------- tail：PhiT 望远镜有理上界 ----------

def tail_bound(b):
    # 加性常数 c(b)：m/16（quad，b-无关）+ (b+1)²·m/16（popoviciu，φ 值域 b+1：
    # φ−L = b·{0,1} − {0,1} + 1 ∈ [0, b+1]）
    # 合成 p/8 + (1+(b+1)²)(p-1)/16 ≤ (5+(b+1)²)p/32。b=6 → 27/16 ✓，b=8 → 43/16。
    ctail = F(5 + (b + 1) ** 2, 32)
    FT = lambda i, x: ((b - 2) * LAM + 2 * LAM * (x - (60 + i) // 3)
                       - 2 * b * LAM * (AL * x - (60 + i) // QD))
    cg = b * LAM / AL            # PT 的 g(1-g) 系数
    cc = cg / AL                 # CT 的 G0(g) 系数
    Pbar = (cg - LAM) / 6
    G0 = lambda v: v * (1 - v) * (2 * v - 1) / 6
    M = math.ceil(float(cc + LAM) / 60)

    def PT(i, x):
        return (cg * (AL * x - (60 + i) // QD) * (1 - (AL * x - (60 + i) // QD))
                - LAM * (x - (60 + i) // 3) * (1 - (x - (60 + i) // 3)))

    def CT(i, x):
        return cc * G0(AL * x - (60 + i) // QD) - LAM * G0(x - (60 + i) // 3)

    def PhiT(i, x):
        return (PT(i, x) / x ** 2 + 2 * CT(i, x) / x ** 3 - Pbar / x ** 2
                + LAM / x - (ctail / 2) / x ** 2)

    # 直接精确积分（含对数）做数值核对；对数系数 A 为常数，Σ ln(r/l) = ln20
    A = 2 * LAM - 2 * b * LAM * AL
    tot_rat = F(0)
    for i in range(1140):
        l = F(60 + i, 3)
        r = F(60 + i + 1, 3)
        q = (60 + i) // 3
        qp = (60 + i) // QD
        B = (b - 2) * LAM - 2 * LAM * q + 2 * b * LAM * qp
        C = ctail
        tot_rat += B * (1 / l - 1 / r) + C / 2 * (1 / l ** 2 - 1 / r ** 2)
    log_part = float(A) * math.log(20)
    exact_val = log_part + float(tot_rat)

    bound = (PhiT(1140, F(400)) - PhiT(0, F(20))
             + 2 * M * (F(1, 8000) - F(1, 64000000)))
    return bound, exact_val, A, M

# ---------- 主流程 ----------

if __name__ == "__main__":
    import sys as _s
    if len(_s.argv) > 1 and _s.argv[1] == 'b8only':
        out = {}
        print(f"LAM={LAM} AL={AL} QD={QD} INNER_DENS={INNER_DENS} OUTER_LO={OUTER_LO}")
        print()
        print("【b=8 内区】")
        m8, I8 = inner_table(8, range(-40, 240), topm=6)
        print(f"  pieces={len(m8)}  integral={float(I8):.10f}")
        print(f"  精确 = {I8.numerator}/{I8.denominator}")
        print()
        print("【b=8 外区】")
        o8, J8 = outer_table(8)
        print(f"  pieces={len(o8)}  integral={float(J8):.10f}")
        print(f"  精确 = {J8.numerator}/{J8.denominator}")
        print()
        t8, e8, A8, M8 = tail_bound(8)
        print(f"【b=8 tail】 有理上界 = {float(t8):.10f} = {t8.numerator}/{t8.denominator}")
        print(f"  真值≈{e8:.8f}  bound>=真值: {float(t8) >= e8}  M={M8}")
        small = 8 * float(LAM) / 400
        print()
        print(f"A_*8 = T + outer + tail = {float(I8 + J8 + t8):.8f}")
        print(f"Aeff ≈ A_*8 + small(8λ/400={small:.5f}) = {float(I8 + J8 + t8) + small:.8f}")
        print(f"gate: Aeff < 2.15 ? {float(I8+J8+t8)+small < 2.15}")
        raise SystemExit
    out = {}
    print("=" * 70)
    print("【校准 1】b=6 内区（mo271 复刻：k∈[-20,80)，top4，3 内点）")
    m6, I6 = inner_table(6, range(-20, 80), topm=4, replica=True)
    tgt6 = F(322437603634266857629, 7535670527041937280000)
    print(f"  pieces={len(m6)}  integral={I6}")
    print(f"  论文   ={tgt6}  匹配: {I6 == tgt6}")
    out['b6_inner'] = {'npieces': len(m6), 'integral': [I6.numerator, I6.denominator],
                       'match_paper': I6 == tgt6}

    print()
    print("【校准 2】b=6 外区")
    o6, J6 = outer_table(6)
    tgtJ6 = F(129101, 96000)
    print(f"  pieces={len(o6)}  integral={J6}")
    print(f"  mo271 ={tgtJ6}  匹配: {J6 == tgtJ6}")
    out['b6_outer'] = {'npieces': len(o6), 'integral': [J6.numerator, J6.denominator],
                       'match_mo271': J6 == tgtJ6}

    print()
    print("【校准 3】b=6 tail")
    t6, e6, A6, M6 = tail_bound(6)
    tgtT6 = F(-6843153, 128000000)
    print(f"  bound={t6}  mo271={tgtT6}  匹配: {t6 == tgtT6}")
    print(f"  真值≈{e6:.8f} (含对数项 系数={float(A6):.6f}·ln20), bound≥真值: {float(t6) >= e6}")
    out['b6_tail'] = {'bound': [t6.numerator, t6.denominator], 'match_mo271': t6 == tgtT6}

    print()
    print("=" * 70)
    print("【b=8 内区】")
    m8, I8 = inner_table(8, range(-40, 240), topm=6)
    print(f"  pieces={len(m8)}  ∫_3^20 = {float(I8):.10f}")
    print(f"  精确 = {I8.numerator}/{I8.denominator}")
    out['b8_inner'] = {'npieces': len(m8), 'integral': [I8.numerator, I8.denominator],
                       'pieces': [[str(p[0]), str(p[1]), p[2], str(p[3]), str(p[4])]
                                  for p in m8]}

    print()
    print("【b=8 外区】")
    o8, J8 = outer_table(8)
    print(f"  pieces={len(o8)}  ∫ = {float(J8):.10f}")
    print(f"  精确 = {J8.numerator}/{J8.denominator}")
    out['b8_outer'] = {'npieces': len(o8), 'integral': [J8.numerator, J8.denominator],
                       'pieces': [[str(p[0]), str(p[1]), str(p[2]), str(p[3])]
                                  for p in o8]}

    print()
    print("【b=8 tail】")
    t8, e8, A8, M8 = tail_bound(8)
    print(f"  有理上界 = {float(t8):.10f}  = {t8.numerator}/{t8.denominator}")
    print(f"  真值  ≈ {e8:.8f} (对数系数 {float(A8):.6f}·ln20)，bound≥真值: {float(t8) >= e8}")
    out['b8_tail'] = {'bound': [t8.numerator, t8.denominator], 'M': M8,
                      'exact_val_approx': e8, 'log_coeff': [A8.numerator, A8.denominator]}

    print()
    print("=" * 70)
    Astar8 = I8 + J8 + t8
    Astar6 = tgt6 + tgtJ6 + tgtT6
    print(f"A_*6 (论文) = {float(Astar6):.8f}")
    print(f"A_*8 (精确表) = {float(Astar8):.8f}  = {Astar8.numerator}/{Astar8.denominator}")
    print(f"对照 b=8 观测拟合值: ∫R8≈0.1931, I_out≈1.5362 (b8_verdict.md)")
    out['A_star_8'] = [Astar8.numerator, Astar8.denominator]
    out['A_star_6_paper'] = [Astar6.numerator, Astar6.denominator]

    with open('research/b8_tables.json', 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print()
    print("已写出 research/b8_tables.json")
