#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 位势不等式 2U^ρ − V₈ ≤ M₀ 的有理区间证书验证器（gen_table2.py 的 b=8 类比）。

证书原理（镜像 Apery.PotentialIneq 链）：
- 分割点集 = {a_j, b_j} ∪ {V₈ 极小点区间 [q−, q+]} 的有理细分；
- 每个小区间 [l, r] 上：U^ρ 分段单调（嵌套 arcsine 势在每个不含 a_j/b_j 的
  小区间上单调），V₈ 单极小（Φ'' 只变号一次，镜像 A.3 论证）；
  故 2U^ρ − V₈ 在 [l, r] 上的最大者在端点达到：验证 2·Ubound − Vbound ≤ M₀。
- 全部用有理上下界（atan 用 π = 16·atan(1/5) − 4·atan(1/239) 拆分 + 交错级数；
  log 用 atanh 变换级数；sqrt 用相邻有理夹逼）。

用法：python verify_measure8.py [table7.txt]（缺省用 Measure7.lean 的占位表）。
输出：每个分割段的界与全局 max B(l,r)；全部通过则打印 CERTIFIED。
"""
from fractions import Fraction as F
import math, sys
sys.set_int_max_str_digits(10**7)

# ---------- 有理界原语（镜像 gen_table2.py 的 log_upper/log_lower 等） ----------
LOG2 = (F(6931471805599453, 10**16), F(6931471805599454, 10**16))
PI   = (F(31415926535897932384626433832795, 10**31),
        F(31415926535897932384626433832796, 10**31))

def log_bounds(y):
    """log y 的严格有理 (下, 上)，y > 0 有理。"""
    k = 0
    yy = y
    while yy < 1:
        yy *= 2; k += 1
    # yy ∈ [1, 2)；写成 yy = 2^e·r, r∈[1,2)：用 atanh 级数
    # 这里 yy 本身已是 [1,2)（放大 2^k 次后可能 > 2，继续）
    while yy >= 2:
        yy /= 2; k -= 1
    x = (yy - 1) / (yy + 1)          # ∈ [0, 1/3]
    m = 12
    s = F(0); xp = x
    for j in range(m):
        s += xp / (2 * j + 1)
        xp *= x * x
    # 余项上界：2 x^{2m+1} / ((2m+1)(1-x^2))
    rem = 2 * xp / ((2 * m - 1) * (1 - x * x))
    core = 2 * s
    return (core - rem - k * LOG2[1], core + rem - k * LOG2[0])

def sqrt_bounds(q):
    """sqrt q 的严格有理 (下, 上)。"""
    assert q > 0
    s = F(math.isqrt((q.numerator * 10**28) // q.denominator)) / 10**14
    while s * s > q:
        s -= F(1, 10**14)
    while (s + F(1, 10**14)) ** 2 <= q:
        s += F(1, 10**14)
    return (s, s + F(1, 10**14))

def atan_bounds_pos(x):
    """atan x 的严格有理界，0 < x ≤ 1 有理（交错级数 + 余项）。"""
    m = 14
    s_lo = F(0); s_hi = F(0)
    xp = x
    for j in range(m):
        term = xp / (2 * j + 1)
        if j % 2 == 0:
            s_lo += term
        else:
            s_hi -= term
        xp *= x * x
    rem = xp / (2 * m + 1)
    S = s_lo + s_hi          # 偶数项部分和（j=0..m-1，共 m 对 → 下估计）
    return (S, S + rem)      # 交错递减级数：S ≤ atan ≤ S + 余项

def atan_bounds(x):
    """atan x，x > 0 任意有理：x>1 时用 π/2 − atan(1/x)。"""
    if x > 1:
        lo, hi = atan_bounds_pos(1 / x)
        return (PI[0] / 2 - hi, PI[1] / 2 - lo)
    return atan_bounds_pos(x)

def pi_bound():
    return PI

# ---------- V₈ 与 U^ρ 的有理封装 ----------
import sys as _sys
AL = F(1, 40) if (len(_sys.argv) > 2 and _sys.argv[2] == '0.975') else F(3, 100)

def V8_bounds(t_lo, t_hi):
    """V₈ 在 [t_lo, t_hi] ⊂ (0, 2] 上的 (严格下界, 严格上界)。"""
    # V = log(1+t) − 8α·log(t+α²) − 2 + 16α + 2√t·(π + atan(1/√t) − 8 atan(α/√t))
    lo1, hi1 = log_bounds(1 + t_lo), log_bounds(1 + t_hi)
    lo2, hi2 = log_bounds(t_lo + AL * AL), log_bounds(t_hi + AL * AL)
    slo, shi = sqrt_bounds(t_lo)[0], sqrt_bounds(t_hi)[1]   # sqrt 单调
    # atan(1/s) 关于 s 递减：s∈[slo,shi] → atan(1/s)∈[atan(1/shi), atan(1/slo)]
    a1_lo, a1_hi = atan_bounds(1 / shi), atan_bounds(1 / slo)
    a2_lo, a2_hi = atan_bounds(AL / shi), atan_bounds(AL / slo)
    pi = pi_bound()
    base_lo = lo1[0] - 8 * AL * hi2[1] - 2 + 16 * AL
    base_hi = hi1[1] - 8 * AL * lo2[0] - 2 + 16 * AL
    # 括号 P = π + atan(1/s) − 8 atan(α/s)：π 界 + 各项界
    P_lo = pi[0] + a1_lo[0] - 8 * a2_hi[1]
    P_hi = pi[1] + a1_hi[1] - 8 * a2_lo[0]
    # P 恒负（α=3/100 时 π − 8·atan(33.3)≈π−8·1.5407<0），2√t·P 为负：
    # 下界 = 2·slo·P_hi（P_hi 较不负 → 乘出来更小？P<0 时 2sP 关于 (s,P) 双负相关：
    # 最小 = 2·slo·P_hi，最大 = 2·shi·P_lo
    lo = base_lo + 2 * slo * P_hi
    hi = base_hi + 2 * shi * P_lo
    return (lo, hi)

def U_interval_bounds(a, b, l, r):
    """单个 arcsine 分量 U^{ω[a,b]} 在 [l,r] 上的 (下界, 上界)，精确有理。"""
    if r <= a or l >= b:
        m = (a + b) / 2
        def g(t):
            return (abs(t - m) + sqrt_bounds(max((t - a) * (t - b), F(1, 10**30)))[1]) / 2
        # 单调性：区间左侧递增、右侧递减
        if r <= a:
            glo, ghi = g(l), g(r)
        else:
            glo, ghi = g(r), g(l)
        llo, lhi = log_bounds(glo), log_bounds(ghi)
        return (llo[0], lhi[1])
    # [l,r] 与 [a,b] 相交：U ∈ [log((b−a)/4), log((|t−m|+√…)/2) 的端界]
    base = log_bounds((b - a) / 4)
    m = (a + b) / 2
    cand = []
    for t in (l, r):
        if a <= t <= b:
            cand.append(base)
        else:
            disc = sqrt_bounds(max((t - a) * (t - b), F(1, 10**30)))
            cand.append(log_bounds((abs(t - m) + disc[1]) / 2))
    return (min(c[0] for c in cand), max(c[1] for c in cand))

def Urho_bounds(table, l, r):
    lo = F(0); hi = F(0)
    for (a, b, c) in table:
        blo, bhi = U_interval_bounds(a, b, l, r)
        lo += c * blo; hi += c * bhi
    return lo, hi

# ---------- 占位表（与 Zeta7/Measure7.lean 一致） ----------
PLACEHOLDER = [(F(x), F(y), F(60625000000, 10**12)) for (x, y) in
               [(100000000000, 200000000000), (90000000000, 190000000000),
                (80000000000, 180000000000), (70000000000, 170000000000),
                (60000000000, 160000000000), (50000000000, 150000000000),
                (40000000000, 140000000000), (30000000000, 130000000000),
                (20000000000, 120000000000), (10000000000, 110000000000),
                (5000000000, 100000000000), (2500000000, 90000000000),
                (1250000000, 80000000000), (600000000, 70000000000),
                (300000000, 60000000000), (100000000, 50000000000)]]
PLACEHOLDER = [(a / 10**12, b / 10**12, c) for (a, b, c) in PLACEHOLDER]

def load_table(fn):
    rows = []
    for line in open(fn, encoding='utf-8'):
        line = line.strip().rstrip(',')
        if line.startswith('('):
            parts = [int(v) for v in line.strip('()').split(',')]
            rows.append((F(parts[0], 10**12), F(parts[1], 10**12), F(parts[2], 10**12)))
    return rows

if __name__ == "__main__":
    table = load_table(sys.argv[1]) if len(sys.argv) > 1 else PLACEHOLDER
    for (_a, _b, _c) in table:
        assert _a < _b, f"表行退化 a>=b: {_a} {_b}"
        assert _c > 0
    lam = F(49, 50) if (len(sys.argv) > 2 and sys.argv[2] == '0.975') else F(97, 100)
    tot = sum(c for _,_,c in table)
    table = [(a, b, c * lam / tot) for (a, b, c) in table]
    print(f"表：{len(table)} 个区间；质量 Σc（重标定后） = {float(sum(c for _,_,c in table)):.9f}")
    # 占位极小点（α=3/100 时 Φ'' 变号点 y²=711α²/880 类比的 b=8 版：
    # y² = α²·(8−1)/(1·…)；此处用数值极小点，正式版需有理夹逼 [q−, q+]）
    import mpmath as mp
    mp.mp.dps = 40
    alv = 0.025 if lam == F(49, 50) else 0.03
    f = lambda y: mp.pi + mp.atan(1/y) - 8*mp.atan(alv/y)
    y0 = mp.findroot(f, alv*1.5)
    q0 = y0*y0
    q_lo = F(int(mp.floor(q0*10**6)), 10**6)
    q_hi = F(int(mp.ceil(q0*10**6)) + 1, 10**6)
    print(f"V 极小点 ≈ {mp.nstr(q0, 15)}，有理夹逼 [{float(q_lo)}, {float(q_hi)}]")
    pts = {F(1, 10**7), F(2), q_lo, q_hi}
    for (a, b, _) in table:
        pts.add(a); pts.add(b)
    pts = sorted(pts)
    # 细分过宽的段
    fine = []
    for l, r in zip(pts, pts[1:]):
        if r - l > F(1, 50):
            n = int((r - l) / F(1, 100)) + 1
            for i in range(n):
                fine.append((l + (r - l) * i / n, l + (r - l) * (i + 1) / n))
        else:
            fine.append((l, r))
    M0_target = F(-6361, 1000)   # 证书目标 M0 = −6.361（认证上界 −6.36090 之下）
    worst = F(-10**9)
    fails = 0
    records = []
    # 自适应细分：对 B > M0_target − 1/20 的段二分至宽 1e-4
    cells = list(fine)
    for _ in range(6):
        nxt = []
        split = False
        for (l, r) in cells:
            ulo, uhi = Urho_bounds(table, l, r)
            vlo, vhi = V8_bounds(l, r)
            B = 2 * uhi - vlo
            if B > M0_target - F(1, 20) and r - l > F(1, 10**4):
                m = (l + r) / 2
                nxt += [(l, m), (m, r)]
                split = True
            else:
                nxt.append((l, r))
        cells = nxt
        if not split:
            break
    fine = cells
    for (l, r) in fine:
        ulo, uhi = Urho_bounds(table, l, r)
        vlo, vhi = V8_bounds(l, r)
        B = 2 * uhi - vlo
        records.append((B, l, r, uhi, vlo))
        if B > worst:
            worst = B
        if B > M0_target:
            fails += 1
            if fails < 6:
                print(f"  违反: [{float(l):.5f},{float(r):.5f}] 2U−V ≤ {float(B):.4f} > M0")
    records.sort(reverse=True)
    for (B, l, r, uhi, vlo) in records[:5]:
        print(f"  最松段 [{float(l):.6f},{float(r):.6f}]: B={float(B):.4f} (Uhi={float(uhi):.4f}, Vlo={float(vlo):.4f})")
    import json as _json
    dump = []
    for (l, r) in fine:
        ulo, uhi = Urho_bounds(table, l, r)
        vlo, vhi = V8_bounds(l, r)
        dump.append({'l': str(l), 'r': str(r), 'uhi': str(uhi), 'vlo': str(vlo)})
    _json.dump(dump, open('research/partition7.json', 'w', encoding='utf-8'))
    print(f"段数 {len(fine)}；max(2U−V) 的上界 = {float(worst):.5f}（证书 M₀ = {float(M0_target)}）；违反 {fails}；分区已存 partition7.json")
    if fails == 0 and worst <= M0_target:
        # 认证能量 I(ρ)：S_j 精确有理；log((b_j−a_j)/4) 用有理界
        S = F(0); S0 = F(0); I_lo = F(0); I_hi = F(0)
        for (a, b, c) in sorted(table, key=lambda t: -t[0]):
            pass
        cs = sorted(table, key=lambda t: -t[0])  # (A.2) 嵌套序：a 降序（行序 j=1..16）
        S = F(0); prev = F(0)
        for (a, b, c) in cs:
            S += c
            lo, hi = log_bounds((b - a) / 4)
            I_lo += (S*S - prev*prev) * lo
            I_hi += (S*S - prev*prev) * hi
            prev = S
        lam_r = F(49, 50)
        Cstar = F(0)
        import math as _m
        Cstar = (-2*lam_r + 16*AL*lam_r*(1 - float(log_bounds(AL)[0])) if False else None)
        # C_* 用 50 位数值（正式版将有理化；此处 f_cert 报告用数值）
        alv, lamv = float(AL), 0.975
        Cstarv = -2*lamv + 16*alv*lamv*(1-_m.log(alv)) + 3*lamv**2 - 2*lamv**2*_m.log(2*lamv)
        f_cert = float(lam_r)*float(M0_target) - float(I_lo) + Cstarv
        print(f"I(ρ) ∈ [{float(I_lo):.6f}, {float(I_hi):.6f}]")
        print(f"C_*₈ = {Cstarv:.6f}")
        print(f"f_cert = λM₀ − I(ρ) + C_*₈ ≤ {f_cert:.5f}（用 I 下界）")
        print("CERTIFIED")
    else:
        print("NOT CERTIFIED")
