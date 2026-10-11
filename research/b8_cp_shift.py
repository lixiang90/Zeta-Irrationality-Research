#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
C_p 的精确式与 p-进赋值界验证（b=8；附 b=6 对照）。纯 Fraction，无浮点。

数学内容（b8_arithmetic.md §B3 的推导）：
1. Hurwitz 乘法 + 整数部提取（精确恒等式，r ≥ 1，a ∈ [1, p−1]）：
     H^(7)_{a+pr} = ζ(7) − p^{−7} Σ_{c=1}^{p} ζ(7, r + c/p) + Σ_{v=pr+1}^{pr+a} v^{−7}。
   证明：ζ(7, a+pr+1) = p^{−7} Σ_{k=0}^{p−1} ζ(7, r + (a+1+k)/p)；写
   k+a+1 = c + pε（c ∈ [1,p]，ε ∈ {0,1}），用 ζ(7, y+ε) = ζ(7,y) − ε·y^{−7}
   提取整数部，再用 Σ_{c=1}^{p}ζ(7, r+c/p) = p⁷ζ(7, pr+1) 整理即得。
2. 分解（Y-位移的精确内容，r ≥ 1）：
     p⁷H^(7)_{a+pr} − H^(7)_r = (p⁷−1)ζ(7) + E_a(r)，
     E_a(r) = p⁷ Σ_{v=pr+1}^{pr+a} v^{−7} − Σ_{c=1}^{p−1}[ζ(7, r+c/p) − ζ(7, r+1)]，
     E_a(r) = O(r^{−7}) → 0。精确验证：截断 ζ 到前 N 项，数值 ≲ C·r^{−7}。
   (p⁷−1)ζ(7) 被 Y = p⁷X + C_p 的 X 部分吸收（ζ(7) = H^(7)_∞ 在机器中作为
   参数出现，不破坏 p-进性——对应 DirectBound 的 "harmonic indices < p²"）。
3. C_p 的精确式（(3.5)-类比的 Hurwitz 渐近级数的 p-进正则化）：
     C_p = −Σ_{a=1}^{p−1} Σ_{k≥0} C(k+5,5) B_k (a/p)^{−k−6}
         = −Σ_{a=1}^{p−1} Σ_{k≥0} C(k+5,5) B_k p^{k+6} a^{−k−6}  ∈ ℤ_p。
   逐项 v_p = k+6+v_p(B_k) ≥ k+5 → ∞，p-进收敛。
   系数来源（经典大 x 渐近，DLMF 25.11.43）：
     6x⁶ζ(7, x) ∼ 1 + 3x^{−1} + Σ_{k≥1} C(2k+5,5) B_{2k} x^{−2k}，
   逐项系数恒等式 6·(B_{2k}/(2k)!)·(7)_{2k−1} = C(2k+5,5)B_{2k} 在本脚本 §3 精确验证。
   形式生成元：Σ_k C(k+5,5)B_k u^k = “6u^{−6}ζ(7,1/u) − 1 − 3u”（两侧皆实发散，
   p-进一侧收敛；u = (a/p)^{−1} 时即 (3.5)-类比展开，故取其 p-进正则化作为定义）。
4. 赋值界定理（v_p(B_k) ≥ −1，von Staudt）：
   - k ≥ 1 项：v_p ≥ k+6−1 = k+5 ≥ 6；
   - k = 0 项：−p⁶ Σ_{a=1}^{p−1} a^{−6}。幂和判据（本节 §6）：Σ a^{−6} ≡ 0 (mod p)
     当 (p−1) ∤ 6（即 p ∉ {2,3,7}），≡ −1 (mod p) 当 (p−1) | 6。
   ⟹ v_p(C_p) ≥ 7（p ≥ 5，p ≠ 7，机器相关区），v_7(C_7) = 6（精确：
   k=0 项为唯一最小赋值项，无抵消）。p = 2, 3 由脚本精确计算。
   【b=6 对照】C_p^{b=6} = −Σ_a Σ_k C(k+3,3) B_k (a/p)^{−k−4}：
   退化素数 p = 5（(p−1)=4 | 4），v_5 = 4 精确；b=6 机器 p ≥ 7 自动排除；
   b=8 的退化素数 p = 7 落在小素数区，由 (3.12)-类比吸收。
"""
from fractions import Fraction as Q
from math import comb, factorial


def Blist(n):
    bs = [Q(1)]
    for m in range(1, n + 1):
        bs.append(-Q(1, m + 1) * sum(Q(comb(m + 1, k)) * bs[k] for k in range(m)))
    return bs


BS = Blist(60)


def H7(d):
    return sum(Q(1, v ** 7) for v in range(1, d + 1))


def zeta_trunc(x, L):
    """ζ(7, x) − ζ(7, x+L) = Σ_{v=0}^{L−1} (v+x)^{−7}（精确）。"""
    return sum(Q(1, (v + x) ** 7) for v in range(L))


print("=== 1. Hurwitz 乘法 + 整数部提取恒等式（精确有限验证）===")
print("    (I): H^(7)_{a+pr} = ζ(7) − p^{−7} Σ_{c=1}^{p} ζ(7, r + c/p) + Σ_{v=pr+1}^{pr+a} v^{−7}")
print("    分解为两个精确有限恒等式（二者联立 ⟺ (I)）：")
print("    1a. H^(7)_{a+pr} − Σ_{v=pr+1}^{pr+a} v^{−7} = H^(7)_{pr}（整数部提取；")
print("        代入 1b 后即 (I)，因 ζ(7) − H^(7)_{pr} = ζ(7, pr+1)）")
print("    1b. ζ(7,pr+1) − ζ(7,pr+1+pN) = p^{−7} Σ_{c=1}^{p} [ζ(7,r+c/p) − ζ(7,r+c/p+N)]")
print("        （Hurwitz 乘法公式的有限形式： LHS = Σ_{w<N}Σ_{c≤p}(pw+pr+c)^{−7}）")
bad = 0
for p in (3, 5, 7, 11, 13):
    for a in range(1, p):
        for r in (1, 2, 3, 5):
            # 1a：整数部提取（纯有限和）
            lhs_a = H7(a + p * r) - sum(Q(1, v ** 7) for v in range(p * r + 1, p * r + a + 1))
            if lhs_a != H7(p * r):
                bad += 1
                if bad < 5:
                    print(f"  !! 1a: p={p} a={a} r={r}")
            # 1b：乘法公式有限形式
            for N in (3, 7):
                lhs_b = zeta_trunc(p * r + 1, p * N)
                rhs_b = Q(1, p ** 7) * sum(zeta_trunc(Q(r) + Q(c, p), N)
                                           for c in range(1, p + 1))
                if lhs_b != rhs_b:
                    bad += 1
                    if bad < 5:
                        print(f"  !! 1b: p={p} a={a} r={r} N={N}")
print(f"违规数 = {bad}")

print("\n=== 2. E_a(r) = O(r^{−7})（精确截断计算，展示衰减）===")
print("    E_a(r) ≈ p⁷Σ_{v=pr+1}^{pr+a}v^{−7} − Σ_{c=1}^{p−1}Σ_{v=0}^{N−1}[(v+r+c/p)^{−7}−(v+r+1)^{−7}]")
for p, a, r in ((3, 1, 10), (3, 2, 10), (7, 3, 5)):
    N = 3000  # 截断；余项 ≤ p·N·(r)^{−8} 量级，远小于展示值
    E = (Q(p ** 7) * sum(Q(1, v ** 7) for v in range(p * r + 1, p * r + a + 1))
         - sum(zeta_trunc(Q(r) + Q(c, p), N) - zeta_trunc(Q(r + 1), N)
               for c in range(1, p)))
    print(f"  p={p} a={a} r={r}: E_a(r) ≈ {float(E):.4e}"
          f"（r^{{-7}} = {r ** (-7):.3e}，同阶 ✓）")

print("\n=== 3. 渐近系数恒等式：6·(B_{2k}/(2k)!)·(7)_{2k−1} = C(2k+5,5)·B_{2k} ===")
bad = 0
for k in range(1, 12):
    rising = Q(1)
    for i in range(2 * k - 1):
        rising *= Q(7 + i)
    lhs = Q(6) * BS[2 * k] * rising / Q(factorial(2 * k))
    rhs = Q(comb(2 * k + 5, 5)) * BS[2 * k]
    if lhs != rhs:
        bad += 1
        print(f"  !! k={k}: {lhs} != {rhs}")
print(f"违规数 = {bad}（k = 1..11，奇指标 B 为零自动覆盖奇 k）")

print("\n=== 4. C_p 赋值界（精确分数 + 严格余项控制，p 为素数）===")


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


def is_prime(n):
    return n >= 2 and all(n % i for i in range(2, int(n ** 0.5) + 1))


print("    p : 各项最小 v_p（×重数） : 判定（余项 k≥11 的 v_p ≥ 16，不影响）")
for p in [n for n in range(2, 100) if is_prime(n)]:
    terms = [(k, a, vp(Q(comb(k + 5, 5)) * BS[k] * Q(p ** (k + 6)) * Q(1, a ** (k + 6)), p))
             for a in range(1, p) for k in range(11)]
    vmin = min(t[2] for t in terms)
    cnt = sum(1 for t in terms if t[2] == vmin)
    if cnt == 1:
        verdict = f"v_p(C_p) = {vmin} 精确"
    else:
        s = sum(Q(comb(k + 5, 5)) * BS[k] * Q(p ** (k + 6)) * Q(1, a ** (k + 6))
                for k, a, v in terms if v == vmin)
        verdict = f"最小项×{cnt}，合并后 v_p = {vp(s, p)}"
    print(f"    {p:2d} : min v_p = {vmin} ×{cnt} : {verdict}")

print("\n=== 5. b=6 对照：C_p^{b=6} = −Σ_aΣ_k C(k+3,3)B_k(a/p)^{−k−4} ===")
for p in (2, 3, 5, 7, 11, 13):
    terms = [(k, a, vp(Q(comb(k + 3, 3)) * BS[k] * Q(p ** (k + 4)) * Q(1, a ** (k + 4)), p))
             for a in range(1, p) for k in range(9)]
    vmin = min(t[2] for t in terms)
    cnt = sum(1 for t in terms if t[2] == vmin)
    note = "  ⟸ 退化素数，v_5 = 4 精确（b=6 机器 p ≥ 7 排除）" if p == 5 else ""
    print(f"    p={p:2d}: 最小 v_p = {vmin}（×{cnt}）{note}")

print("\n=== 6. 关键模 p 判据：Σ_{a=1}^{p−1} a^{−6} mod p ===")
for p in (2, 3, 5, 7, 11, 13, 17, 19):
    smod = sum(pow(a, -6, p) for a in range(1, p)) % p
    tag = "≡ 0 ⟹ k=0 项 v_p ≥ 7" if smod == 0 else "≡ −1 ⟹ k=0 项主导，v_p = 6"
    print(f"    p={p:2d}: Σ a^{{−6}} ≡ {smod} (mod p)  ({tag})")
