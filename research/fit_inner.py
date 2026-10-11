#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中区（内区）极限函数 R_8(x) 的经验拟合与 ∫R 计算。

观测：γ_p^in = pΓ(K/p) + O(1)，v_p(S_K) = p𝓝(K/p) + O(1)，R = −Γ − 𝓝，
故 R_obs(x) := −v_p^G(F)/p（x = K/p，中区素数 K/M < p ≤ K/3）。
校准：同管道对 b=6 应复现 ∫_3^20 R_6(x)/x³ dx = 322437603634266857629/7535670527041937280000
（论文 (5.18)，精确有理）。
"""
import sys, math, re
from fractions import Fraction as F
sys.path.insert(0, 'Zeta5-mo271/scripts')
from math import gcd, lcm
from flint import fmpq
from hankel import entries, det_poly
from sympy import primerange

B8 = True

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

def vS(K, N, h, p, b):
    return 2*h*legendre(K,p) - 2*b*h*legendre(N,p) \
        - 2*sum(legendre(2*i,p) for i in range(1,h)) + (h-1)*(2 if p==2 else 0)

def content_of(Delta, h):
    g, l = 0, 1
    for i in range(h + 1):
        c = Delta[i]
        g = gcd(g, int(c.p)); l = lcm(l, int(c.q))
    return g, l

def middle_obs_b6(n):
    K, N, h, a, b = entries(n)
    Delta = det_poly(h, a, b)
    g, l = content_of(Delta, h)
    out = []
    for p in primerange(7, 2*h+1):
        if K // 40 < p <= K // 3:
            vF = vS(K,N,h,p,6) + vp(g,p) - vp(l,p)
            out.append((F(K, p), F(-vF, p)))
    return out

def parse_middle():
    import glob
    pts = []
    for fn in ['research/b8_hankel_all.txt'] + glob.glob('research/b8_hankel_n*.txt'):
        K = None
        for line in open(fn, encoding='utf-8'):
            m = re.match(r'n=(\d+) K=(\d+)', line)
            if m: K = int(m.group(2))
            m = re.search(r'middle p=\s*(\d+) \(x=([\d.]+)\): v_p\^G\(F\)=\s*(-?\d+)', line)
            if m and K:
                p = int(m.group(1)); vF = int(m.group(3))
                pts.append((F(K, p), F(-vF, p)))
    return pts

def fit_bins(pts, x0, x1, nbins):
    """分箱最小二乘（箱内常值近似，用于积分）。"""
    out = []
    for i in range(nbins):
        l = x0 + (x1 - x0) * i / nbins
        r = x0 + (x1 - x0) * (i + 1) / nbins
        sel = [t for (x, t) in pts if l <= float(x) < r]
        out.append((F(l), F(r), sum(sel)/len(sel) if sel else None, len(sel)))
    return out

if __name__ == "__main__":
    print("=== b=6 中区校准 ===")
    all6 = []
    for n in (2, 3, 4):
        all6 += middle_obs_b6(n)
    I6 = F(0)
    for l, r, v, cnt in fit_bins(all6, 3.0, 20.0, 340):
        if v is not None:
            I6 += v * (F(1)/l - F(1)/r) / l  # ∫ v/x³ dx = v(1/l² - ...) 修正：v*(1/l-1/r) 是 ∫v/x²；需 /x³：
    # 正确积分：∫_l^r v/x³ dx = v/2 * (1/l² - 1/r²)
    I6 = F(0)
    for l, r, v, cnt in fit_bins(all6, 3.0, 20.0, 340):
        if v is not None:
            I6 += v / 2 * (F(1)/(l*l) - F(1)/(r*r))
    target = F(322437603634266857629, 7535670527041937280000)
    print(f"b=6 观测 ∫_3^20 R/x³ = {float(I6):.8f}   论文 (5.18) = {float(target):.8f}   差 {float(I6-target):+.6f}")

    print("\n=== b=8 中区 ===")
    pts8 = parse_middle()
    print(f"数据点: {len(pts8)}")
    I8 = F(0)
    for l, r, v, cnt in fit_bins(pts8, 3.0, 20.0, 340):
        if v is not None:
            I8 += v / 2 * (F(1)/(l*l) - F(1)/(r*r))
    print(f"b=8 观测 ∫_3^20 R_8(x)/x³ dx = {float(I8):.6f}   (b=6 同段 = {float(target):.6f})")
    xs = sorted(x for x, _ in pts8)
    print(f"x 覆盖 [{float(xs[0]):.2f}, {float(xs[-1]):.2f}]")
