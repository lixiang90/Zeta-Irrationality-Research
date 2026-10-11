#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外区极限函数的经验拟合与 I_out 计算。

方法论校准：对 b=6 用 mo271 的 hankel.py 精确计算外区素数的 -v_p^G(F)/K，
与论文 Table 4 的 T(y)（仿射分段，精确有理）逐点比较——若吻合（误差 O(1/K)），
则同一拟合管道用于 b=8 数据（b8_hankel_n*.txt），分段拟合 T_8(y) 并积分得 I_out,8。
"""
import sys, math, re
from fractions import Fraction as F
sys.path.insert(0, 'Zeta5-mo271/scripts')
from math import gcd, lcm
from flint import fmpq
from hankel import entries, det_poly
from sympy import primerange

AL, LAM = F(3, 40), F(37, 40)

TABLE4 = [(F(1,3),F(43,120),F(279,40),F(-9)),(F(43,120),F(37,100),F(451,40),F(-21)),
(F(37,100),F(13,30),F(377,40),F(-16)),(F(13,30),F(37,80),F(429,40),F(-19)),
(F(37,80),F(1,2),F(17,4),F(-5)),(F(1,2),F(43,80),F(51,10),F(-3)),
(F(43,80),F(37,60),F(231,20),F(-15)),(F(37,60),F(13,20),F(97,10),F(-12)),
(F(13,20),F(37,40),F(42,5),F(-10)),(F(37,40),F(1),F(1),F(-2)),(F(1,37,20) if False else F(1),F(37,20),F(37,20),F(-1))]
TABLE4[-1] = (F(1), F(37,20), F(37,20), F(-1))

def T6(y):
    for l, r, b, c in TABLE4:
        if l <= y < r:
            return b + c * y
    return F(0)

def vp(x, p):
    x = int(x)
    if x == 0: return 10**9
    v = 0
    while x % p == 0: x //= p; v += 1
    return v

def legendre(m, p):
    s = 0; q = p
    while q <= m: s += m // q; q *= p
    return s

def content_and_outer_b6(n):
    """mo271 b=6：外区素数观测。"""
    K, N, h, a, b = entries(n)
    Delta = det_poly(h, a, b)
    g, l = 0, 1
    for i in range(h + 1):
        c = Delta[i]
        g = gcd(g, int(c.p)); l = lcm(l, int(c.q))
    out = []
    for p in primerange(7, 2 * h + 1):
        if p >= 7 and p <= K < 3 * p and p * p > 2 * K and 2 * N < p and 5 * N <= 2 * p - 2:
            vS = 2*h*legendre(K,p) - 12*h*legendre(N,p) - 2*sum(legendre(2*i,p) for i in range(1,h)) + (h-1)*(2 if p==2 else 0)
            vF = vS + vp(g,p) - vp(l,p)
            out.append((F(p, K), F(-vF, K)))
    return out

def parse_b8_logs():
    import glob
    pts = []
    for fn in glob.glob('research/b8_hankel_n*.txt'):
        K = None
        for line in open(fn, encoding='utf-8'):
            m = re.match(r'n=(\d+) K=(\d+)', line)
            if m: K = int(m.group(2))
            m = re.search(r'outer p=\s*(\d+).*v_p\(cont Δ\)=\s*(-?\d+)\s+v_p\^G\(F\)=\s*(-?\d+)', line)
            if m and K:
                p = int(m.group(1)); y = F(p, K); vF = int(m.group(3))
                pts.append((y, F(-vF, K), K))
    return pts

def fit_pieces(pts, grid):
    """每个 grid 区间最小二乘拟合仿射段；返回 (list of (l,r,slope,icept), 最大相对残差)。"""
    pieces = []
    worst = F(0)
    for l, r in zip(grid, grid[1:]):
        sel = [(y, t) for (y, t, K) in pts if l <= y < r]
        if len(sel) < 2:
            pieces.append((l, r, None, None))
            continue
        xs = [t[0] for t in sel]; ys = [t[1] for t in sel]
        n = len(xs)
        sx = sum(xs); sy = sum(ys); sxx = sum(x*x for x in xs); sxy = sum(x*y for x, y in sel)
        denom = n*sxx - sx*sx
        if denom == 0:
            pieces.append((l, r, F(0), sy/n)); continue
        slope = F(n*sxy - sx*sy, denom)
        icept = (sy - slope*sx)/n
        for x, y in sel:
            resid = abs(y - (icept + slope*x))
            scale = max(abs(y), F(1))
            worst = max(worst, resid/scale)
        pieces.append((l, r, slope, icept))
    return pieces, worst

if __name__ == "__main__":
    print("=== 校准：b=6 经验 T_obs 的积分 vs 论文 I_out ===")
    all6 = []
    for n in (1, 2, 3):
        obs = content_and_outer_b6(n)
        all6 += [(y, t, 40 * n) for y, t in obs]
    grid6 = sorted({F(1,3), (1+AL)/3, F(2)*LAM/5, (1-AL)/2, (1+4*AL)/3, F(1,2),
                    (1+AL)/2, F(2)*LAM/3, (1+4*AL)/2, 1-AL, F(1), F(2)*LAM})
    pieces6, worst6 = fit_pieces(all6, grid6)
    I6 = F(0)
    for l, r, s, c in pieces6:
        if s is not None:
            I6 += c*(r-l) + s*(r*r-l*l)/2
    print(f"b=6 观测积分 = {float(I6):.6f}   论文 I_out = {float(F(127751,96000)):.6f}   差 = {float(I6 - F(127751,96000)):+.6f}")
    for l, r, s, c in pieces6:
        if s is not None:
            print(f"  [{float(l):.4f},{float(r):.4f}] T_obs,6 = {float(c):+.4f} {float(s):+.2f}*y   (Table4: b={float(T6((l+r)/2) - F(-21)*( (l+r)/2 )):.3f} 斜率≈)", )
    print(f"  拟合相对残差 ≈ {float(worst6):.3f}")

    print("\n=== b=8 分段拟合（网格来自断点族） ===")
    al = AL
    grid = sorted({F(1,3), (1+al)/3, F(2)*LAM/5, (1-al)/2, (1+(al*6))/3, F(1,2),
                   (1+al)/2, F(2)*LAM/3, (1+6*al)/2, 1-al, F(1), F(2)*LAM})
    pts = parse_b8_logs()
    print(f"数据点: {len(pts)} (来自 n=1..3)")
    pieces, worst = fit_pieces(pts, grid)
    I = F(0)
    for l, r, s, c in pieces:
        if s is None:
            print(f"  [{float(l):.4f},{float(r):.4f}] 数据不足")
            continue
        I += c*(r-l) + s*(r*r-l*l)/2
        print(f"  [{float(l):.4f},{float(r):.4f}] T = {float(c):+.4f} {float(s):+.2f}*y")
    print(f"拟合相对残差上界 ≈ {float(worst):.3f}")
    print(f"I_out,8 (初步, n=1..3) = {I} = {float(I):.6f}   (b=6 对照: 127751/96000 = {float(F(127751,96000)):.6f})")
