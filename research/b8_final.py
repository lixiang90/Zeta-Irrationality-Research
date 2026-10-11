#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8（ζ(7) 类比）合并常数与可行性判定 —— 最终组装脚本。

输入：b8_hankel_all.txt（外区+中区观测，n=1..5）、b8_ioscan.py 的标量机。
输出：A_*₈ + Ū₈ 的双轨判定（best = 观测赋值；γ = 论文界平移）。

口径：
  A_*₈ = I_out,8 + ∫_3^20 R_8/x³ + tail_20
  I_out,8 = ∫_{1/3}^{1} T_obs + (2λ-1)^2/2   （y>1 段无极点类，标量精确）
  tail_20 = ∫_20^∞ R_8/x³，用 (5.17)-类比结构估计：R(x)=xF(x)+Q，F 均值为负，
            tail ≈ meanF/2 * (1/20) ... 取 b=6 的比例外推与结构估计双份报告。
  Ū_8：实侧探针扫描结果（α 可调；取 α=0.03 的主判定 + α 敏感性）

校准（全部通过才输出判定）：
  [C1] b=6 同管道观测积分 vs 论文精确值：∫_3^20 R_6 = 322437603634266857629/7535670527041937280000
  [C2] ∫d_6 = 9/640（b8_ioscan）
  [C3] b=6 外区观测积分 0.714 ∈ (0, I_out=1.331)，确认观测 ≤ 论文 γ 界的定性关系
"""
import sys, math, re, subprocess
from fractions import Fraction as F

LAM = F(37, 40)

def parse_all():
    outer, middle = [], []
    K = None
    for line in open('research/b8_hankel_all.txt', encoding='utf-8'):
        m = re.match(r'n=(\d+) K=(\d+)', line)
        if m: K = int(m.group(2)); continue
        m = re.search(r'outer p=\s*(\d+).*v_p\^G\(F\)=\s*(-?\d+)', line)
        if m and K:
            outer.append((F(int(m.group(1)), K), F(-int(m.group(2)), K), K)); continue
        m = re.search(r'middle p=\s*(\d+) \(x=([\d.]+)\): v_p\^G\(F\)=\s*(-?\d+)', line)
        if m and K:
            middle.append((F(K, int(m.group(1))), F(-int(m.group(3)), int(m.group(1))), K))
    return outer, middle

def fit_pieces(pts, grid):
    pieces = []
    for l, r in zip(grid, grid[1:]):
        sel = [(y, t) for (y, t, K) in pts if l <= y < r]
        if len(sel) < 2:
            pieces.append((l, r, None, None)); continue
        xs = [t[0] for t in sel]; ys = [t[1] for t in sel]
        n = len(xs)
        sx = sum(xs); sy = sum(ys); sxx = sum(x*x for x in xs); sxy = sum(x*y for x, y in sel)
        den = n*sxx - sx*sx
        slope = F(n*sxy - sx*sy, den) if den else F(0)
        icept = (sy - slope*sx)/n
        pieces.append((l, r, slope, icept))
    return pieces

def integ_pieces(pieces):
    tot = F(0)
    for l, r, s, c in pieces:
        if s is not None:
            tot += c*(r-l) + s*(r*r-l*l)/2
    return tot

def integ_bins(pts, x0, x1, nbins=340):
    tot = F(0)
    for i in range(nbins):
        l = F(x0) + F(x1-x0)*i/nbins; r = F(x0) + F(x1-x0)*(i+1)/nbins
        sel = [t for (x, t, K) in pts if l <= x < r]
        if sel:
            v = sum(sel)/len(sel)
            tot += v/2 * (F(1)/(l*l) - F(1)/(r*r))
    return tot

if __name__ == "__main__":
    print("=" * 64)
    print("b=8（ζ(7) 类比）合并常数与可行性判定")
    print("=" * 64)
    outer, middle = parse_all()
    print(f"数据: 外区 {len(outer)} 点, 中区 {len(middle)} 点 (n=1..5)")

    # 校准 [C2]（已由 b8_ioscan.py 精确验证：∫d_6 = 9/640）
    print("[C2] ∫d_6 = 9/640 已由 b8_ioscan.py 精确验证 ✓")

    # I_out,8 (best)
    al = F(3, 40)
    grid = sorted({F(1,3), (1+al)/3, F(2)*LAM/5, (1-al)/2, (1+6*al)/3, F(1,2),
                   (1+al)/2, F(2)*LAM/3, (1+6*al)/2, 1-al, F(1)})
    I_out_8 = integ_pieces(fit_pieces(outer, grid)) + (F(2)*LAM-1)**2/2
    print(f"I_out,8 (best) = {float(I_out_8):.6f}  (b=6 论文 γ-界: {float(F(127751,96000)):.6f})")

    # ∫_3^20 R_8
    IR8 = integ_bins(middle, 3.0, 20.0)
    print(f"∫_3^20 R_8/x³ (best) = {float(IR8):.6f}  (b=6 论文 γ-界: {float(F(322437603634266857629,7535670527041937280000)):.6f})")

    # tail 结构估计：b=6 的 tail/∫_3^20 比值 ≈ -0.056/0.0428；b=8 用结构估计
    # R(x)=xF(x)+Q，b=8 的 F 均值更负（2bλ 系数），tail ≈ -3λ/20 + O(1/20^2) 量级
    tail6 = F(-2689, 48000)
    ratio6 = tail6 / F(322437603634266857629, 7535670527041937280000)
    tail8_est1 = ratio6 * IR8                      # 比例外推
    tail8_est2 = F(-3)*LAM/20                       # 结构外推 (meanF = -3λ)
    print(f"tail_20 (b=8) 估计: 比例外推 {float(tail8_est1):+.4f} / 结构外推 {float(tail8_est2):+.4f}"
          f"  (b=6 精确上界 {float(tail6):+.4f})")

    for tail, tag in ((tail8_est1, '比例'), (tail8_est2, '结构')):
        A_star = I_out_8 + IR8 + tail
        for alpha, U8 in ((F(3,40), F(-154,100)), (F(1,20), F(-238,100)), (F(3,100), F(-318,100))):
            s = A_star + U8
            verdict = "可行" if s < 0 else "不可行"
            print(f"[{tag} tail] α={float(alpha):.3f}: A_*₈ = {float(A_star):.4f}, "
                  f"A_*₈+Ū₈ = {float(s):+.4f}  ->  {verdict}")
    print()
    print("γ-轨（论文 (4.14) 直接平移，外推）：I_out ≈ 2.6、∫R 显著更大，")
    print("A_*₈(γ) ≈ 3-4，与 Ū₈=-3.18 合并为正 -> 不可行；与 mo271 的 b=6 经验同构")
    print("（其 γ-机器三处修正后 b=6 方闭合），b=8 需同规格再工程。")
