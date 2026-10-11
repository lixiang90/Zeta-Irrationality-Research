#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(3.12)-类比 小素数逐项损耗表（b=8）。纯 Fraction / 整数运算，无浮点。

数学内容（写入 b8_arithmetic.md §C7）：

损耗模型。极点函数 G_K = (K!)²·A(x)/∏_{r∈Pl}(x−r)，Pl = {±1,…,±K}，
A 为 ≤d 次整值多项式；τ₈ 逐项作用后每「次应用」的 p-进损耗上界：

  ① 极点阶乘比：v_p((K!)²/∏_{s≠r}(r−s)) ≥ −⌊log_p 2K⌋。
     恒等式（极点集 {±1,…,±K}，|r| = ρ）：
       ∏_{s≠r}(r−s) = (−1)^{K−ρ}(K−ρ)!(K+ρ)!/ρ，
     故 v_p((K!)²/∏) = c₂ − c₁ + v_p(ρ)，其中 c₁ = 加法进位 carries_p(K,ρ)，
     c₂ = 减法借位 borrows_p(K,ρ)，c₁ ≤ ⌊log_p(K+ρ)⌋ ≤ ⌊log_p 2K⌋。
     【本脚本 §4 用 digit-sum/Legendre 精确验证 + 直接分数乘积复核闭式】
     锋利：p=2, K=3, r=3 给 −2 = −⌊log₂6⌋；p=7, K=6, r=6 给 −1。
  ② 调和主部：v_p(H⁽⁷⁾_j) ≥ −7⌊log_p j⌋（H⁽⁷⁾_j = Σ_{v≤j} v^{−7}）。
     锋利：j = pᵐ 时 v_p = −7m 精确（v = pᵐ 项 −7m 严格主导）。
     【§2 精确验证；§3 复核 j = pᵐ 精确取等】
  ③ κ 归一化：τ₈ 的 720 分母 + von Staudt：v_p(κ⁻_d) ≥ −1−v_p(720)，
     即损耗 1+v_p(720)，p = (2,3,5,7,≥11) 给 (5,3,2,1,1)。
     【§3 精确验证，κ⁻_d = (d)₆·B_{d−6}/720，B₁=−1/2】
  ④ C_p 位移（仅分布公式路线）：v_p(C_p) ≥ 6 全素数成立，且
     v_p(C_p) = 6 精确 ⟺ p ∈ {2,3,7}；p ≥ 5 时 = 7。
     【§5 复算 b8_cp_shift.py §4 的精确分数合并法】

合计（每次应用）：
  K 相关：⌊log_p 2K⌋ + 7⌊log_p K⌋ ≤ 8⌊log_p max(2K, d+1)⌋  （§C.6 同款）；
  常数（路线 A = 分布公式）：L_p = 1 + v_p(720) + v_p(C_p)
                            = (11, 9, 9, 7, 8)，p = (2,3,5,7,≥11)，一致上界 11；
  常数（路线 B = DirectBound，mo271 策略）：C_p 不出现，
                            L_p^B = 1 + v_p(720) = (5,3,2,1,1)，一致上界 5。

b=8 版 (3.12) 类比（钉死完整常数）：
  v_p^G(F_K) ≥ −8h⌊log_p(c_{α,λ}K)⌋ − h·L_p   （路线 A；换 L_p^B 得路线 B）

【§6 经验安全余量】从 b8_hankel_*.txt 的全量 v_p^G(F) 数据复核加强界
  −8h⌊log_p 5K⌋ − h·L_p（L_p 含 C_p，p ≥ 7 段）：全部 margin ≥ 0 即零违规。
"""
from fractions import Fraction as Q
from math import comb, floor, log


def Blist(n):
    """Bernoulli 数，B₁ = −1/2 约定（κ⁻ 的 minus 约定）。"""
    bs = [Q(1)]
    for m in range(1, n + 1):
        bs.append(-Q(1, m + 1) * sum(Q(comb(m + 1, k)) * bs[k] for k in range(m)))
    return bs


BS = Blist(90)


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def vp_int(n, p):
    if n == 0:
        return 10 ** 9
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_fact(n, p):
    """v_p(n!)（Legendre 和，精确整数）。"""
    v, q = 0, p
    while q <= n:
        v += n // q
        q *= p
    return v


def ilog(n, p):
    """精确 ⌊log_p n⌋（n ≥ 1），整数循环，无浮点。"""
    e = 0
    q = p
    while q <= n:
        q *= p
        e += 1
    return e


def H7(d):
    return sum(Q(1, v ** 7) for v in range(1, d + 1))


def vp(q, p):
    if q == 0:
        return 10 ** 9
    n, d = q.numerator, q.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


PRIMES = [p for p in range(2, 100) if is_prime(p)]

print("=== 1. 720 = 2⁴·3²·5 精确分解 ===")
n = 720
facs = {}
for p in PRIMES:
    while n % p == 0:
        n //= p
        facs[p] = facs.get(p, 0) + 1
print(f"    720 = {facs}，余数 {n}（应为 1：{n == 1}）")
for p in (2, 3, 5, 7, 11):
    print(f"    v_{p}(720) = {vp_int(720, p)}")

print("\n=== 2. 调和主部：v_p(H⁽⁷⁾_j) ≥ −7⌊log_p j⌋ ===")
bad = 0
jmax = 1500
for p in PRIMES:
    H = H7(jmax)
    # 增量维护 H⁽⁷⁾_j；逐 j 检查代价高，改为对数档检查 j = 1..jmax 抽样+全量边界
    Hj = Q(0)
    for j in range(1, jmax + 1):
        Hj += Q(1, j ** 7)
        bnd = -7 * ilog(j, p)
        if vp(Hj, p) < bnd:
            bad += 1
            if bad < 5:
                print(f"  !! p={p} j={j}: v_p = {vp(Hj, p)} < {bnd}")
print(f"违规数 = {bad}（p ≤ 97，j ≤ {jmax}）")

print("\n=== 3. κ⁻_d = (d)₆·B_{d−6}/720 的小素数赋值 + 锋利性 ===")
print("    v_p(κ⁻_d) ≥ −1−v_p(720)（p = 2,3,5,7）；并验证 j=p 时调和界取等、")


def kappa_minus(d):
    return Q(prod(d - i for i in range(6))) * BS[d - 6] / 720


def prod(it):
    r = 1
    for x in it:
        r *= x
    return r


bad = 0
minv = {}
for p in (2, 3, 5, 7):
    mv = 10 ** 9
    for d in range(6, 80):
        v = vp(kappa_minus(d), p)
        mv = min(mv, v)
        if v < -1 - vp_int(720, p):
            bad += 1
            if bad < 5:
                print(f"  !! p={p} d={d}: v_p(κ⁻) = {v}")
    minv[p] = mv
print(f"违规数 = {bad}；min v_p(κ⁻_d)："
      + "，".join(f"p={p}:{minv[p]}" for p in (2, 3, 5, 7)))
print("    （min 应分别 ≥ −5,−3,−2,−1 = −1−v_p(720)；"
      "von Staudt 锋利时取等）")
# 调和界锋利性：v_p(H⁽⁷⁾_{pᵐ}) = −7m 精确（v = pᵐ 项严格主导）
bad = 0
for p in (2, 3, 5, 7, 11, 13):
    for m in (1, 2, 3):
        j = p ** m
        if j > 1500:
            continue
        v = vp(H7(j), p)
        if v != -7 * m:
            bad += 1
            print(f"  !! p={p} m={m}: v_p(H⁽⁷⁾_{j}) = {v} ≠ {-7*m}")
print(f"调和界锋利性违规数 = {bad}（v_p(H⁽⁷⁾_{'{pᵐ}'}) = −7m 精确，"
      f"p ≤ 13，m ≤ 3）")

print("\n=== 4. 极点阶乘比：v_p((K!)²/∏_{s≠r}(r−s)) ≥ −⌊log_p 2K⌋ ===")
print("    极点集 Pl = {±1,…,±K}；闭式 ∏_{s≠r}(r−s) = (−1)^{K−ρ}(K−ρ)!(K+ρ)!/ρ，ρ=|r|")


def pole_prod_direct(K, r):
    return prod(r - s for s in list(range(-K, 0)) + list(range(1, K + 1)) if s != r)


bad = 0
# 4a. 闭式复核（|直接分数乘积| vs |公式|；符号与 v_p 无关故只比对绝对值）
for K in range(1, 9):
    for r in list(range(-K, 0)) + list(range(1, K + 1)):
        rho = abs(r)
        direct = abs(pole_prod_direct(K, r))
        formula = prod(range(1, K - rho + 1)) * prod(range(1, K + rho + 1)) // rho
        if direct != formula:
            bad += 1
            if bad < 5:
                print(f"  !! 闭式不合：K={K} r={r}: {direct} != {formula}")
print(f"闭式复核违规数 = {bad}")

# 4b. digit-sum 界：v_p((K!)²/∏) = 2v_p(K!)−v_p((K−ρ)!)−v_p((K+ρ)!)+v_p(ρ) ≥ −⌊log_p 2K⌋
bad = 0
Kmax = 150
for p in PRIMES:
    for K in range(1, Kmax + 1):
        bnd = -ilog(2 * K, p)
        for rho in range(1, K + 1):
            v = (2 * vp_fact(K, p) - vp_fact(K - rho, p) - vp_fact(K + rho, p)
                 + vp_int(rho, p))
            if v < bnd:
                bad += 1
                if bad < 5:
                    print(f"  !! p={p} K={K} ρ={rho}: v = {v} < {bnd}")
print(f"阶乘比界违规数 = {bad}（p ≤ 97，K ≤ {Kmax}）")

# 4c. 锋利性
for p, K, r in ((2, 3, 3), (7, 6, 6), (3, 2, 2), (5, 4, 4)):
    rho = abs(r)
    v = (2 * vp_fact(K, p) - vp_fact(K - rho, p) - vp_fact(K + rho, p)
         + vp_int(rho, p))
    print(f"    锋利 p={p} K={K} r={r}: v_p = {v}，界 = "
          f"{-ilog(2 * K, p)}（取等：{v == -ilog(2 * K, p)}）")

print("\n=== 5. C_p 赋值（精确分数合并法，复算 b8_cp_shift.py §4） ===")
CP = {}
for p in PRIMES:
    terms = [(k, a, vp(Q(comb(k + 5, 5)) * BS[k] * Q(p ** (k + 6)) * Q(1, a ** (k + 6)), p))
             for a in range(1, p) for k in range(11)]
    vmin = min(t[2] for t in terms)
    cnt = sum(1 for t in terms if t[2] == vmin)
    if cnt == 1:
        CP[p] = vmin
    else:
        s = sum(Q(comb(k + 5, 5)) * BS[k] * Q(p ** (k + 6)) * Q(1, a ** (k + 6))
                for k, a, v in terms if v == vmin)
        CP[p] = vp(s, p)
    if p <= 13 or p in (17, 19, 23, 97):
        print(f"    p={p:2d}: v_p(C_p) = {CP[p]}")
assert all(CP[p] >= 6 for p in PRIMES)
eq67 = [p for p in PRIMES if CP[p] == 6]
print(f"    v_p(C_p) ≥ 6 全素数成立；= 6 精确 ⟺ p ∈ {eq67}（应为 [2, 3, 7]）")

print("\n=== 6. 损耗表合成 与 b=8 版 (3.12) 类比 ===")
print("    每行 = 单次应用的最大 p-进损耗（上界；负号表示损失）")
print("    p        2    3    5    7   ≥11")
rows = {
    "极点 ⌊log_p 2K⌋": None,
    "调和 7⌊log_p K⌋": None,
    "κ 1+v_p(720)": [1 + vp_int(720, p) for p in (2, 3, 5, 7, 11)],
    "C_p v_p(C_p)（路线A）": [CP[2], CP[3], CP[5], CP[7], CP[11]],
}
for name, vals in rows.items():
    if vals:
        print(f"    {name:<22}" + "".join(f"{v:>5}" for v in vals))
L_A = [1 + vp_int(720, p) + CP[p] for p in (2, 3, 5, 7, 11)]
L_B = [1 + vp_int(720, p) for p in (2, 3, 5, 7, 11)]
print(f"    {'常数合计 L_p（路线A）':<22}" + "".join(f"{v:>5}" for v in L_A))
print(f"    {'常数合计 L_p（路线B）':<22}" + "".join(f"{v:>5}" for v in L_B))
print(f"    一致上界：路线A max L_p = {max(L_A)}；路线B max L_p = {max(L_B)}")
print("    (3.12)-类比（钉死）：v_p^G(F_K) ≥ −8h⌊log_p(c_{α,λ}K)⌋ − h·L_p")

print("\n=== 7. 经验安全余量：加强界 −8h⌊log_p 5K⌋ − h·L_p 对 b8_hankel_* 数据 ===")
import glob
import re
pat_head = re.compile(r"^n=(\d+) K=(\d+) N=(\d+) h=(\d+)")
pat_mid = re.compile(r"middle p=\s*(\d+).*v_p\^G\(F\)=\s*(-?\d+)")
pat_out = re.compile(r"outer p=\s*(\d+).*v_p\^G\(F\)=\s*(-?\d+)")
cur = None
margins = {}
for fn in sorted(glob.glob("research/b8_hankel*.txt")):
    for line in open(fn, encoding="utf-8"):
        m = pat_head.match(line)
        if m:
            cur = (int(m.group(1)), int(m.group(2)), int(m.group(4)))
            continue
        m = pat_mid.search(line) or pat_out.search(line)
        if m and cur:
            p, v = int(m.group(1)), int(m.group(2))
            n_, K, h = cur
            Lp = 1 + vp_int(720, p) + CP.get(p, 7 if p > 7 else CP.get(p, 6))
            marg = v + 8 * h * ilog(5 * K, p) + h * Lp
            margins.setdefault((n_, p), []).append(marg)
worst = []
for (n_, p), ms in sorted(margins.items()):
    worst.append((min(ms), n_, p, len(ms)))
worst.sort()
print("    (n, p, 数据点数, 最小余量) 前 12 最差：")
for w, n_, p, c in worst[:12]:
    print(f"    n={n_} p={p:3d} ×{c:2d}  min margin = {w}")
print(f"    总数据点 {sum(len(m) for m in margins.values())}，"
      f"最小余量 {min(w[0] for w in worst)}（≥ 0 即加强界零违规）")
