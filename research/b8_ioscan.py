#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
I_out 的标量部分（v_p(S_K) 贡献）对一般 b 的精确计算与校准。

论文 (5.10)：I_out = ∫_{1/3}^{2λ} [ R0(y) - d(y) - 2λ⌊1/y⌋ + Σ_{j=1}^{b-1}(2λ-jy)_+ ] dy
本脚本计算标量部分 S_b = ∫[ -2λ⌊1/y⌋ + Σ_{j=1}^{b-1}(2λ-jy)_+ ]（与 R0/d 无关），
并用 b=6 校准：对论文 (5.8)/(5.9) 的 b=6 系数做**分段精确**有理积分得 ∫(R0-d)，
检查 S_6 + ∫(R0-d) == 127751/96000（论文 I_out 精确值）——通过即为校准成功。
"""
from fractions import Fraction as F

def scal_part(b, lam, al=None):
    """S_b = ∫_{1/3}^{2λ} [ -2λ⌊1/y⌋ + Σ_{j=1}^{b-1}(2λ-jy)_+ ] dy，精确有理。
    断点：y=1, 1/2（floor）与 y=2λ/j（正部）。"""
    pts = {F(1, 3), F(2) * lam, F(1, 2), F(1)}
    for j in range(1, b):
        y = F(2) * lam / j
        if F(1, 3) < y < F(2) * lam:
            pts.add(y)
    pts = sorted(pts)
    total = F(0)
    for l, r in zip(pts, pts[1:]):
        ym = (l + r) / 2
        fl = int(F(1) / ym)
        slope = F(0); icept = F(-2) * lam * fl
        for j in range(1, b):
            if F(2) * lam - j * ym > 0:
                slope += F(-j); icept += F(2) * lam
        total += icept * (r - l) + slope * (r * r - l * l) / 2
    return total

def rank_corr_integral(b, al):
    """∫d(y)dy，d(y) = (1+(b-2)α-3y-(1+α-3y)_+)_+ · 1_{(1/3,1/2)}。
    分段：p1=(1+α)/3（内层正部断点），p2=(1+(b-2)α)/3（外层正部断点）。"""
    c = F(b - 2) * al
    p1 = (F(1) + al) / 3
    p2 = (F(1) + c) / 3
    lo = F(1, 3)
    hi = min(F(1, 2), p2)
    total = F(0)
    # 段 1：y ∈ (lo, min(p1,hi))，d = c - α（常数，-3y 相消）
    r1 = min(p1, hi)
    if r1 > lo:
        total += (c - al) * (r1 - lo)
    # 段 2：y ∈ (max(p1,lo), hi)，d = 1+c-3y
    l2 = max(p1, lo)
    if hi > l2:
        total += (F(1) + c) * (hi - l2) - F(3) * (hi * hi - l2 * l2) / 2
    return total

def r0_minus_d_integral_b6(al):
    """论文 (5.8)/(5.9) b=6 系数的 ∫(R0-d)，分段精确。"""
    lam = F(37, 40)
    def seg(l, r, slope, icept):
        return icept * (r - l) + slope * (r * r - l * l) / 2
    p1 = (F(1) + al) / 3       # 1/3..1/2 支的内层断点
    p1b = (F(1) + al) / 2      # 1/2..1 支的内层断点 (1+α-2y)
    p2b = (F(1) + 4 * al) / 2  # (1+4α-2y)_+ 断点
    total = F(0)
    # 支 1：y ∈ (1/3, 1/2)：R0 = 8-9y-8α-5min(α,1-2y)-5(1+α-3y)_+，再减 d
    # min(α,1-2y) 断点 y=(1-α)/2；d = (1+4α-3y-(1+α-3y)_+)_+
    m1 = (F(1) - al) / 2
    dA = rank_corr_integral  # d 的积分单独算
    # R0 支 1 分段：(1/3, min(m1,p1))、(p1, m1) 或 (m1, p1)、其后
    # 段 a: y < min(α vs 1-2y 断点 m1, 内层断点 p1)
    # 情形 α=3/40: m1 = 37/80 = 0.4625, p1 = 43/120 ≈ 0.3583 → p1 < m1
    pts = sorted({F(1,3), F(1,2), p1, m1, (F(1)+4*al)/3})
    for l, r in zip(pts, pts[1:]):
        if r <= l: continue
        ym = (l + r) / 2
        slope = F(-9); icept = F(8) - 8 * al
        if ym < m1:   # min(α, 1-2y) = α
            icept -= 5 * al
        else:         # min = 1-2y
            slope += F(10); icept -= F(5)
        inner = F(1) + al - 3 * ym
        if inner > 0:
            slope += F(15); icept -= F(5) * (F(1) + al)
        total += seg(l, r, slope, icept)
    # 支 2：y ∈ (1/2, 1)：R0 = 7(1-y)-6min(α,1-y)-6(1+α-2y)_+ + (1+4α-2y)_+
    pts2 = sorted({F(1,2), F(1), p1b, p2b})
    for l, r in zip(pts2, pts[1:]) if False else zip(pts2, pts2[1:]):
        if r <= l: continue
        ym = (l + r) / 2
        slope = F(-7); icept = F(7)
        if ym > p1b:  # min = α（注意 (1-y) 在 y>1-α 时小于 α；p1b = (1+α)/2 是 1+α-2y 的断点）
            pass
        # min(α, 1-y)：y < 1-α 时 min = α；否则 min = 1-y
        if ym < F(1) - al:
            icept -= 6 * al
        else:
            slope += F(6); icept -= F(6)
        inner = F(1) + al - 2 * ym
        if inner > 0:
            slope += F(12); icept -= 6 * (F(1) + al)
        inner2 = F(1) + 4 * al - 2 * ym
        if inner2 > 0:
            slope += F(-2); icept += F(1) + 4 * al
        total += seg(l, r, slope, icept)
    return total - rank_corr_integral(6, al)

if __name__ == "__main__":
    al6, lam6 = F(3, 40), F(37, 40)
    print("=== b=6 校准 ===")
    S6 = scal_part(6, lam6)
    d6 = rank_corr_integral(6, al6)
    print(f"S_6                 = {S6} = {float(S6):.10f}")
    print(f"∫d_6                = {d6} = {float(d6):.10f}   论文 9/640 = {float(F(9,640)):.10f}  {'✓' if d6==F(9,640) else '✗'}")
    I_r0d6 = r0_minus_d_integral_b6(al6)
    print(f"∫(R0-d)_6           = {I_r0d6} = {float(I_r0d6):.10f}")
    tot = S6 + I_r0d6
    print(f"S_6 + ∫(R0-d)_6     = {tot}")
    print(f"论文 I_out          = {F(127751,96000)}")
    print(f"校准: {'✓ 精确吻合' if tot == F(127751,96000) else '✗ 差 ' + str(tot - F(127751,96000))}")

    print("\n=== b=8 标量部分（与 α 无关） ===")
    for lam_s, lam in (("37/40", F(37,40)), ("9/10", F(9,10))):
        S8 = scal_part(8, lam)
        S6x = scal_part(6, lam)
        print(f"λ={lam_s}: S_8 = {S8} = {float(S8):.8f}   (与 S_6 同: {S8==S6x})")
    print("注：λ=37/40 时 (2λ-jy)_+ 对 j>=6 在 (1/3,2λ) 上恒 0，故 S_8 = S_6 为恒等事实；")
    print("I_out 的 b-依赖全部经由 R0-d 的成本部分（removed-class 表，见 b8_arithmetic.md §G）。")
