#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ζ(7) 类比泛函极点值的精确推导与数值验证（已修正版）。

结论（60 位精度验证，全部通过）：
1. 权 w_7(y) = y^7 f^{(6)}(y)/360（f = 1/(e^{2πy}−1)）的极点积分：
   等价地 w_7(y) = (2π)^6 y^7 Σ_{n≥1}n^6e^{-2πny}/360；不可重复乘 (2π)^6。
     I7(a) = ∫₀^∞ w_7(y)/(y²+a²) dy = a^6 ζ(7,a) − 1/(2a) − 1/6     （精确恒等式）
   推导：六次 IBP（边界干净：u = y^7/(y²+a²) 在 0 点 7 阶零点）+
         DLMF 25.11.29（Hermite 公式）：
         2∫₀^∞ f(y) Im(a−iy)^{-s} dy = ζ(s,a) − a^{1-s}/(s-1) − a^{-s}/2。
   注意 Σ_l l^6 q^l = q(1+57q+302q²+302q³+57q⁴+q⁵)/(1−q)^7（分母 7 次！）。

2. μ 泛函极点值（与论文式 (2.3) 同构）：
     μ_{7,X}(1/(t+j²)) = j^6 (X − H_j^{(7)}) − 1/6 + 1/(2j)
   → ℚ_p 数据干净，Fauzan §3–5 机器的数据层面无障碍。

3. τ-机器 b=8 恒等式（数值验证）：
     τ_8((x+1)^e − x^e) = [e≥6]·e!/(e−6)!/720，  其中
     τ_8(x^m) = m(m−1)(m−2)(m−3)(m−4)·B_{m−5}/720  （用 B₁ = +1/2 约定！）
   论文"Bernoulli 数约定 B₁ = −1/2"只适用于 μ-矩公式；τ 的 κ_d 用经典约定。

4. 【更正】之前版本的 r(a) 残差系 Eulerian 分母 bug 所致，已不存在。
   【发现】μ-世界差分恒等式 μ(P(X+1)−P(X)) = C(P⁗(0)/24) 按字面为假
   （P=X⁴: LHS=121/12 ≠ 0）；(3.2)/(3.3) 属于 τ-世界。
   Lean 项目的 eq_3_3_poly / eq_3_2_poly 陈述需重述（经 pullback 或改为 τ 版本）。
"""
import mpmath as mp
import math

mp.mp.dps = 60
pi = mp.pi


def S6(q):
    # Σ_{l≥1} l^6 q^l —— 分母 (1-q)^7（7 次，不是 6 次！）
    return q * (1 + 57 * q + 302 * q ** 2 + 302 * q ** 3 + 57 * q ** 4 + q ** 5) / (1 - q) ** 7


def I7(a):
    return mp.quad(lambda y: y ** 7 * (2 * pi) ** 6 * S6(mp.exp(-2 * pi * y)) / (360 * (y ** 2 + a ** 2)),
                   [0, 1, mp.inf])


def tau8(m):
    # τ_8(x^m) = m(m−1)(m−2)(m−3)(m−4) B_{m−5}/720，Bernoulli 用 B_1=+1/2 约定
    if m < 5:
        return mp.mpf(0)
    B = mp.bernoulli(m - 5)
    if m - 5 == 1:
        B = mp.mpf(1) / 2  # 经典约定 B_1 = +1/2
    return mp.fprod(range(m - 4, m + 1)) * B / 720


if __name__ == "__main__":
    print("=== 1. I7(a) = a^6 ζ(7,a) − 1/(2a) − 1/6 ===")
    for a in (1, 2, 3, 5, 8):
        d = I7(a) - (a ** 6 * mp.zeta(7, a) - 1 / (2 * a) - mp.mpf(1) / 6)
        print(f"a={a}: diff = {mp.nstr(d, 5)}")

    print("\n=== 2. 极点值 μ_{7,X}(1/(t+j^2)) = j^6(X − H_j^{(7)}) − 1/6 + 1/(2j) ===")
    zeta7 = mp.zeta(7)
    H7 = lambda j: sum(mp.mpf(1) / v ** 7 for v in range(1, j + 1))
    for j in (1, 2, 3, 5):
        d = I7(j) - (j ** 6 * (zeta7 - H7(j)) - mp.mpf(1) / 6 + 1 / (2 * j))
        print(f"j={j}: diff = {mp.nstr(d, 5)}")

    print("\n=== 3. τ_8 差分恒等式: τ_8((x+1)^e − x^e) ?= e!/(e−6)!/720 ===")
    for e in (5, 6, 7, 8, 10):
        lhs = sum(math.comb(e, k) * tau8(k) for k in range(e))
        rhs = mp.fprod(range(e - 5, e + 1)) / 720 if e >= 6 else mp.mpf(0)
        print(f"e={e}: LHS={mp.nstr(lhs, 10)}  RHS={mp.nstr(rhs, 10)}  diff={mp.nstr(lhs - rhs, 3)}")
