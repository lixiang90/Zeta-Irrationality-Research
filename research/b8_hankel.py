#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 Hankel 行列式的经验赋值验证（mo271 valuations.py 方法论的直接推广）。

改动（相对 mo271 的 hankel.py，全部对应 Fauzan 论文 b=6 -> b=8）：
- W = DN**8（原 **6）
- mu(t^k) = (-1)^k B_{2k+2} * prod_{i=3}^{7}(2k+i) / 720（原 3 因子 /24）
- 极点常数项 -1/6 + 1/(2j)（原 -1/4 + 1/(2j)），X 系数 j**6（原 j**4）
- v_p(S_K) = 2h*leg(K) - 16h*leg(N) - 2*sum(leg(2i)) + (h-1)*v_p(4)（原 12h）
- (3.12)-类比界：-8h*floor(log_p(5K)) - h*v_p(720)（原 6h 与 24）
- (2.9)-类比首项：prod j**6 * DN(-j*j)**7（原 j**4 * DN**5）

输出：
1. (2.9)-类比首项系数精确校验；
2. 全素数 (3.12)-类比界校验（ Violations 报告）；
3. 外区素数的经验 v_p^G(Delta) 观测表（供 b=8 外区极限函数拟合，目标第 (2)(3) 项）。
"""
import sys, math
from math import gcd, lcm
from flint import fmpq, fmpz, fmpq_poly, fmpz_poly, fmpq_mat
from sympy import primerange

B = 8  # 标号；实际导数阶为 B-2=6

def Dpoly(m):
    p = fmpz_poly([1])
    for j in range(1, m + 1):
        p *= fmpz_poly([j * j, 1])
    return p

def mu_monomial(k):
    num = fmpq(-1) ** k * fmpq.bernoulli(2 * k + 2)
    # 2026-09-28: the previous endpoint B+1 inserted an erroneous (2k+8).
    # Integral formula: (2k+7)! / (720*(2k+2)!), matching Construction.μmono.
    for i in range(3, B):
        num *= (2 * k + i)
    return num / fmpq(math.factorial(B - 2))  # 720 = 6!

def entries(n):
    K, N, h = 40 * n, 3 * n, 37 * n
    DN, DK = Dpoly(N), Dpoly(K)
    W = DN ** B                             # b=6: DN**6；B=8: DN**8
    E = 2 * h - 1
    maxk = max(0, B * N + E - 1 - K)       # D_N has t-degree N, not 2N
    mus = [mu_monomial(k) for k in range(maxk + 1)]
    H = [fmpq(0)]
    for j in range(1, K + 1):
        H.append(H[-1] + fmpq(1, j ** (B - 1)))   # H^{(7)}
    base = {}
    for j in range(N + 1, K + 1):
        num = fmpq(DN(fmpz(-j * j))) ** B
        den = fmpq(1)
        for k in range(1, K + 1):
            if k != j:
                den *= (k * k - j * j)
        base[j] = num / den
    Wq, DKq = fmpq_poly(W), fmpq_poly(DK)
    a, b = [], []
    poleC = lambda j: -fmpq(j ** (B - 2)) * H[j] - fmpq(1, B - 2) + fmpq(1, 2 * j)
    for e in range(E):
        Pe = (Wq * fmpq_poly([0] * e + [1])) // DKq
        ae = fmpq(0)
        for k in range(Pe.degree() + 1):
            ae += Pe[k] * mus[k]
        be = fmpq(0)
        for j in range(N + 1, K + 1):
            c = base[j] * fmpq(-j * j) ** e
            be += c * (j ** (B - 2))
            ae += c * poleC(j)
        a.append(ae); b.append(be)
    return K, N, h, a, b

def det_poly(h, a, b):
    A = fmpq_mat(h, h, [a[i + j] for i in range(h) for j in range(h)])
    Bm = fmpq_mat(h, h, [b[i + j] for i in range(h) for j in range(h)])
    detB = Bm.det()
    C = -(Bm.inv() * A)
    return C.charpoly() * detB

def vp(x, p):
    x = int(x)
    if x == 0: return 10 ** 9
    v = 0
    while x % p == 0: x //= p; v += 1
    return v

def legendre(m, p):
    s = 0; q = p
    while q <= m: s += m // q; q *= p
    return s

def vS(K, N, h, p):
    return 2 * h * legendre(K, p) - 2 * B * h * legendre(N, p) \
        - 2 * sum(legendre(2 * i, p) for i in range(1, h)) + (h - 1) * (2 if p == 2 else 0)

def run(n):
    K, N, h, a, b = entries(n)
    Delta = det_poly(h, a, b)
    print(f"n={n} K={K} N={N} h={h} deg Delta = {Delta.degree()}")
    # (2.9)-analog 首项校验
    DN = Dpoly(N)
    lead = fmpq((-1) ** ((h * (h - 1)) // 2))
    for j in range(N + 1, K + 1):
        lead *= fmpq(j ** (B - 2)) * fmpq(DN(fmpz(-j * j))) ** (B - 1)
    print(f"  (2.9)-analog leading coeff check: {Delta[h] == lead}")
    # content
    g, l = 0, 1
    for i in range(h + 1):
        c = Delta[i]
        g = gcd(g, int(c.p)); l = lcm(l, int(c.q))
    bad = []
    for p in primerange(2, 2 * h + 1):
        vD = vp(g, p) - vp(l, p)
        vF = vS(K, N, h, p) + vD
        b312 = -8 * h * int(math.floor(math.log(5 * K) / math.log(p) + 1e-12)) - h * vp(720, p)
        if vF < b312:
            bad.append(('3.12-analog', p, vF, b312))
        # 外区观测
        cond = p >= 7 and p <= K < 3 * p and p * p > 2 * K and 2 * N < p and 7 * N <= 2 * p - 2
        if cond:
            print(f"  outer p={p:3d} (y={p/K:.3f}): v_p(cont Δ)={vD:5d}  v_p^G(F)={vF:5d}")
        # 中区观测（x = K/p，用于 R_8(x) 拟合；M=40 截断对应论文内区范围）
        if K // 40 < p <= K // 3 and p >= 7:
            print(f"  middle p={p:3d} (x={K/p:.4f}): v_p^G(F)={vF:6d}")
    print(f"  (3.12)-analog VIOLATIONS: {bad if bad else 'none'}")
    sys.stdout.flush()

if __name__ == "__main__":
    for n in map(int, sys.argv[1:] if len(sys.argv) > 1 else ['1']):
        run(n)
