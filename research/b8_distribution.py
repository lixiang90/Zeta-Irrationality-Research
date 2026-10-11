#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 分布恒等式的精确（纯分数，无浮点）验证。

对应 b8_arithmetic.md §B2 的严格推导：
- F_-(t) = t^6/(720(e^t-1)) = sum_m kappa^-_m t^m/m!（B_1 = -1/2 约定）；
  kappa^-_m = kappa^+_m - [m=6]。
- 几何级数 sum_{a=0}^{p-1} e^{at} = (e^{pt}-1)/(e^t-1) 对任意正整数 p 成立。
- 故 sum_a e^{at} F_-(pt) = p^6 F_-(t)（形式幂级数/亚纯恒等式）。
- 系数比较（e^{at}F_-(pt) 的 t^m 系数 = tau_-((a+pX)^m)/m!）给出
  多项式版分布恒等式：sum_a tau_-((a+pX)^m) = p^6 kappa^-_m，即
  tau_-(g) = p^{-6} sum_a tau_-(g(a+pX))（一切 g ∈ Q[X]，一切正整数 p）。

【修正项分析】B_1=+1/2 约定下分布恒等式带修正项：
  tau_+(g) - p^{-6} sum_a tau_+(g(a+pX))
    = c6(g) - sum_{n>=6} C(n,6) S_{n-6}(p) c_n(g)，
  其中 c_n(g) = [x^n]g，S_k(p) = sum_{a=0}^{p-1} a^k（S_0 = p）。
  来源：tau_+ = tau_- + Δ，Δ(g) = c6(g)，而
  c6(g(a+pX)) = p^6 sum_{n>=6} C(n,6) a^{n-6} c_n(g)。
  注意：修正项对奇多项式一般不消失（g = x^7, p = 2 给 -7）。
  【推论·构造适用版】对奇 g（如 pullback 像 x^7 R(-x^2)）：
  tau_+(g) = tau_-(g)（c6 = 0，且奇次幂的 kappa 值约定无关），故
  p^6 tau(g) = sum_a tau_-(g(a+pX)) —— RHS 用 minus 约定，这是分布步骤
  在 b=8 的正确形式（与 mo271 b=6 同构）。
"""
from fractions import Fraction as Q
from math import comb, prod
import random

random.seed(20260924)


def bernoulli_minus(n):
    """精确 Bernoulli 数（B_1 = -1/2 约定），递推 sum_{k=0}^{m} C(m+1,k) B_k = 0。"""
    B = [Q(0)] * (n + 1)
    B[0] = Q(1)
    for m in range(1, n + 1):
        B[m] = -Q(1, m + 1) * sum(Q(comb(m + 1, k)) * B[k] for k in range(m))
    return B[n]


# 健全性检查
assert bernoulli_minus(0) == 1
assert bernoulli_minus(1) == Q(-1, 2)
assert bernoulli_minus(2) == Q(1, 6)
assert bernoulli_minus(4) == Q(-1, 30)


def kappa_minus(m):
    if m < 5:
        return Q(0)
    return Q(prod(range(m - 4, m + 1))) * bernoulli_minus(m - 5) / 720


def kappa_plus(m):
    return kappa_minus(m) + (Q(1) if m == 6 else Q(0))


def tau(coeffs, kap):
    """线性泛函 tau(x^k) = kap(k)，coeffs 为多项式系数列表。"""
    return sum(Q(c) * kap(k) for k, c in enumerate(coeffs))


def shift_scale(coeffs, a, p):
    """g ↦ g(a + pX)。返回系数列表（次数不变）。"""
    out = [Q(0)] * len(coeffs)
    for k, c in enumerate(coeffs):
        for j in range(k + 1):
            out[j] += Q(c) * comb(k, j) * Q(a) ** (k - j) * Q(p) ** j
    return out


def pow_sum(k, p):
    """S_k(p) = sum_{a=0}^{p-1} a^k（S_0 = p）。"""
    return sum(Q(a) ** k for a in range(p))


print("=== 1. 多项式版分布恒等式（B_1=-1/2，精确分数）===")
print("    sum_a tau_-((a+pX)^m) = p^6 kappa^-_m，p = 1..40（含合数），m = 0..40")
bad = 0
for p in range(1, 41):
    for m in range(0, 41):
        lhs = sum(tau(shift_scale([Q(0)] * m + [Q(1)], a, p), kappa_minus)
                  for a in range(p))
        rhs = Q(p ** 6) * kappa_minus(m)
        if lhs != rhs:
            bad += 1
            if bad < 5:
                print(f"  !! p={p} m={m}: {lhs} != {rhs}")
print(f"违规数 = {bad}（共 40*41 = 1640 例）")

print("\n=== 2. plus 约定修正项公式（精确分数）===")
print("    tau_+(g) - p^{-6} sum_a tau_+(g(a+pX))")
print("      = c6(g) - sum_{n>=6} C(n,6) S_{n-6}(p) c_n(g)，随机稠密 g，次数 ≤ 12")
bad = 0
for trial in range(60):
    deg = random.randint(0, 12)
    g = [Q(random.randint(-5, 5), random.randint(1, 6)) for _ in range(deg + 1)]
    for p in range(1, 14):
        diff = tau(g, kappa_plus) - sum(tau(shift_scale(g, a, p), kappa_plus)
                                        for a in range(p)) / Q(p ** 6)
        corr = (g[6] if len(g) > 6 else Q(0)) - sum(
            Q(comb(n, 6)) * pow_sum(n - 6, p) * g[n] for n in range(6, len(g)))
        if diff != corr:
            bad += 1
            if bad < 5:
                print(f"  !! trial={trial} p={p}: diff={diff} != corr={corr}")
print(f"违规数 = {bad}（共 60*13 = 780 例）")

print("\n=== 3. 构造适用版：奇 g 的 p^6 tau(g) = sum_a tau_-(g(a+pX)) ===")
print("    g = x^7 R(-x^2)（随机奇系数，次数 ≤ 21），p = 1..13，LHS/RHS 精确相等")
bad = 0
for trial in range(60):
    g = [Q(0)] * 22
    for n in range(1, 22, 2):  # 只含奇次幂
        g[n] = Q(random.randint(-4, 4), random.randint(1, 5))
    for p in range(1, 14):
        lhs = Q(p ** 6) * tau(g, kappa_plus)
        rhs = sum(tau(shift_scale(g, a, p), kappa_minus) for a in range(p))
        if lhs != rhs:
            bad += 1
            if bad < 5:
                print(f"  !! trial={trial} p={p}: {lhs} != {rhs}")
print(f"违规数 = {bad}（共 60*13 = 780 例）")

print("\n=== 4. 反例登记：奇多项式修正项不消失 ===")
g = [Q(0)] * 8
g[7] = Q(1)  # g = x^7
p = 2
lhs = tau(g, kappa_plus)
rhs_scaled = sum(tau(shift_scale(g, a, p), kappa_plus) for a in range(p))
corr = Q(0) - Q(comb(7, 6)) * pow_sum(1, p)  # -C(7,6) S_1(2) = -7
print(f"  g = x^7, p = 2: tau_+(g) - 2^{{-6}} sum_a tau_+((a+2X)^7)"
      f" = {lhs - rhs_scaled / Q(p ** 6)}（公式给 {corr}，"
      f"故 plus 约定下分布恒等式对奇 g 也失败，必须用 minus 约定）")

print("\n=== 5. 抽样打印：p=7, m=8 的逐项贡献（B_1=-1/2）===")
p, m = 7, 8
for a in range(p):
    print(f"  a={a}: tau_-((a+{p}X)^{m}) = {tau(shift_scale([Q(0)]*m+[Q(1)], a, p), kappa_minus)}")
print(f"  求和 = {sum(tau(shift_scale([Q(0)]*m+[Q(1)], a, p), kappa_minus) for a in range(p))}"
      f" = p^6 kappa^-_8 = {Q(p**6) * kappa_minus(m)}")
