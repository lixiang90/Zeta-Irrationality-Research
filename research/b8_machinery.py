#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 算术机器（τ_8 泛函）的恒等式与赋值界验证（修正版）。

关键约定事实（本脚本的核心发现）：
- τ_8(x^m) = kappa_m := (m)_5 * B_{m-5}/720。
- 生成函数依赖 B_1 约定：
    B_1 = +1/2:  F(t) = t^6/(720(e^t-1)) + t^6/720
    B_1 = -1/2:  F0(t) = t^6/(720(e^t-1))
- 差分恒等式 tau_8(g(x+1)-g(x)) = g^{(6)}(0)/720 在 B_1=+1/2 下对所有多项式成立；
  分布恒等式 sum_a e^{at} F0(pt) = p^6 F0(t) 在 B_1=-1/2 下成立。
- 【对构造无影响】pullback 像只含奇次幂 x^{2e+7}，其 kappa 只含偶数指标
  Bernoulli 数（约定无关）。kappa_6 = B_1 从不被使用。

验证：
1. 生成函数（两种约定，截断比较）；
2. 差分恒等式（B_1=+1/2，全部次数）；
3. 分布恒等式（B_1=-1/2 生成函数，截断比较）；
4. von Staudt 赋值界 v_p(kappa_d) >= -1（p>=7, d<=79）；
5. 调和损失界 v_p(H_j^{(7)}) >= -7*floor(log_p j)（j<400）。
"""
import mpmath as mp
import math
from fractions import Fraction as F

mp.mp.dps = 50


def bern(m, conv):
    if m == 1:
        return mp.mpf(1) / 2 if conv == 'plus' else mp.mpf(-1) / 2
    return mp.bernoulli(m)


def kappa(m, conv='plus'):
    if m < 5:
        return mp.mpf(0)
    return mp.fprod(range(m - 4, m + 1)) * bern(m - 5, conv) / 720


def tau_poly(coeffs, conv='plus'):
    return sum(c * kappa(k, conv) for k, c in enumerate(coeffs))


def F_gen(t, conv):
    base = t ** 6 / (720 * (mp.e ** t - 1))
    return base + t ** 6 / 720 if conv == 'plus' else base


print("=== 1. 生成函数（截断 m<M 与闭式比较） ===")
for conv in ('plus', 'minus'):
    for t in (mp.mpf('0.2'), mp.mpf('0.5')):
        lhs = sum(kappa(m, conv) * t ** m / mp.factorial(m) for m in range(0, 30))
        d = lhs - F_gen(t, conv)
        print(f"conv={conv} t={t}: diff = {mp.nstr(d, 5)}")

print("\n=== 2. 差分恒等式 tau_8(P(X+1)-P(X)) = P^{(6)}(0)/720  [B_1=+1/2] ===")
for deg in (1, 5, 6, 7, 8, 11):
    d = [math.comb(deg, k) for k in range(deg)]
    lhs = tau_poly(d, 'plus')
    rhs = mp.factorial(deg) / mp.factorial(deg - 6) / 720 if deg >= 6 else mp.mpf(0)
    print(f"deg={deg}: diff = {mp.nstr(lhs - rhs, 5)}")

print("\n=== 3. 分布恒等式 sum_a e^{at} F0(pt) = p^6 F0(t)  [B_1=-1/2] ===")
for p in (2, 3, 5, 7, 11):
    for t in (mp.mpf('0.13'), mp.mpf('0.31')):
        lhs = sum(mp.e ** (a * t) * F_gen(p * t, 'minus') for a in range(p))
        rhs = mp.mpf(p) ** 6 * F_gen(t, 'minus')
        print(f"p={p} t={t}: diff = {mp.nstr(lhs - rhs, 5)}")

print("\n=== 4. von Staudt 界 v_p(kappa_d) >= -1  (7<=p<=59, 5<=d<=79) ===")
def to_frac(x):
    return F(mp.nstr(x, 40)).limit_denominator(10 ** 30)

def vp(q, p):
    if q == 0:
        return 10 ** 9
    num, den = q.numerator, q.denominator
    v = 0
    while num % p == 0:
        num //= p; v += 1
    while den % p == 0:
        den //= p; v -= 1
    return v

bad = 0
for p in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59):
    for d in range(5, 80):
        B = to_frac(mp.bernoulli(d - 5)) if d - 5 != 1 else F(1, 2)
        kq = F(math.prod(range(d - 4, d + 1))) * B / 720
        v = vp(kq, p)
        if v < -1:
            bad += 1
            print(f"  !! p={p} d={d}: v_p = {v}")
print(f"违规数 = {bad}")

print("\n=== 5. 调和损失 v_p(H_j^{(7)}) >= -7*floor(log_p j)  (j<400, p-adic 赋值追踪) ===")
class Padic:
    """x = p^val * unit，unit 为 p-进单位，存 unit mod p^PREC。"""
    PREC = 64
    def __init__(self, val, unit, p):
        self.p, self.val, self.unit = p, val, unit % (p ** self.PREC)
    @classmethod
    def one_over(cls, n7, p):
        # 1/n^7 的 p-adic 分解：n = p^a * m
        a, m = 0, n7
        while m % p == 0:
            m //= p; a += 1
        inv = pow(m, -1, p ** cls.PREC)  # m^{-1} mod p^PREC
        u = pow(inv, 7, p ** cls.PREC)
        return cls(-7 * a, u, p)
    def __add__(self, o):
        p = self.p
        if self.val == o.val:
            s = (self.unit + o.unit) % (p ** self.PREC)
            gain = 0
            while s % p == 0:
                s //= p; gain += 1
                if gain > self.PREC - 2:
                    break
            return Padic(self.val + gain, s, p)
        if self.val < o.val:
            if o.val - self.val < self.PREC:
                return Padic(self.val, self.unit + o.unit * pow(p, o.val - self.val, p ** self.PREC), p)
            return self
        if self.val - o.val < self.PREC:
            return Padic(o.val, o.unit + self.unit * pow(p, self.val - o.val, p ** self.PREC), p)
        return o

bad6 = 0
for p in (2, 3, 5, 7, 11, 13):
    acc = Padic(10 ** 9, 0, p)  # 0 元
    for j in range(1, 400):
        acc = acc + Padic.one_over(j, p)
        v = acc.val
        bound = -7 * int(mp.log(j) / mp.log(p))
        if v < bound:
            bad6 += 1
            if bad6 < 5:
                print(f"  !! p={p} j={j}: v_p = {v} < {bound}")
print(f"违规数 = {bad6}")
