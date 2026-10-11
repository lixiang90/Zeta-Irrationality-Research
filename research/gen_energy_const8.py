#!/usr/bin/env python3
# 生成 Zeta7/EnergyConst8.lean：energy_const8 = (6.4)-类比 的数值认证。
# 证书：log x >= 2*sum_{i<m} u^{2i+1}/(2i+1) - k*0.6931471808，u = (r-1)/(r+1), r = 2^k*x >= 1，
# 与 Apery.log_ge_of_pow_two 的语句逐字对齐（Apery/EnergyConst.lean 的 b=6 模式）。
from fractions import Fraction as Fr

TABLE7 = [(23805751, 7233498018, 88359644486),
          (23805236, 24475480029, 99121090942),
          (13780926, 53387677936, 107241598886),
          (4483874, 90545533724, 82115389762),
          (4483625, 131074600165, 77454394089),
          (3851833, 183808371265, 89612496606),
          (1564143, 242780558682, 78099713936),
          (1360324, 306011065675, 72197849402),
          (745743, 365490311924, 56650775746),
          (383988, 426183534933, 58654077061),
          (247221, 481648846822, 38926352971),
          (159595, 523624475376, 36581913253),
          (111989, 591522748269, 62952958579),
          (54900, 747509679905, 133255592),
          (50233, 778759015742, 16227595547),
          (36652, 1389338921242, 10670893142)]

T = 10 ** 12
M_TERMS = 10
LOG2_UB = Fr(6931471808, 10 ** 10)  # 与 Apery.log_ge_of_pow_two 中的字面量 0.6931471808 一致
DEN = 10 ** 13  # 证书值向下取整的分母（同 b=6 的 /10^13）

def artanh_cert(r, m):
    """log r 的下界：2*sum_{i<m} u^{2i+1}/(2i+1)，u=(r-1)/(r+1)，r>=1（有理、向下舍入到 1/DEN）。"""
    u = (r - 1) / (r + 1)
    s = Fr(0)
    t = u
    for i in range(m):
        s += t / (2 * i + 1)
        t *= u * u
    v = 2 * s
    return Fr(v.numerator * DEN // v.denominator, DEN)

def log_lower_cert(x):
    """log x 的下界（x>0）：写成 x = 2^{-k}... 这里直接取最小 k 使 2^k x >= 1，
    证书 = artanh_cert(2^k x) - k*LOG2_UB，向下舍入。"""
    k = 0
    while Fr(2) ** k * x < 1:
        k += 1
    r = Fr(2) ** k * x
    v = artanh_cert(r, M_TERMS) - k * LOG2_UB
    return Fr(v.numerator * DEN // v.denominator, DEN), k, r

def rstr(v):
    if v.denominator == 1:
        return f"({v.numerator} : ℝ)"
    return f"({v.numerator} / {v.denominator} : ℝ)"

# ---- 原子与权重 ----
c = [Fr(x[2], T) for x in TABLE7]
S = []
s = Fr(0)
for j in range(16):
    s += c[j]
    S.append(s)
assert S[-1] == Fr(39, 40), S[-1]

weights = []
for j in range(16):
    prev = S[j - 1] if j else Fr(0)
    weights.append(S[j] ** 2 - prev ** 2)

atoms = [Fr(TABLE7[j][1] - TABLE7[j][0], 4 * T) for j in range(16)]

certs = []
for j in range(16):
    v, k, r = log_lower_cert(atoms[j])
    certs.append((v, k, r))

# ---- 验证目标不等式 ----
lam, alph = Fr(39, 40), Fr(1, 40)
M0 = Fr(-127, 20)
U = Fr(-43, 20)
# alph 与 2*lam 的对数下界证书
a_cert, a_k, a_r = log_lower_cert(alph)     # log(1/40)
l_cert, l_k, l_r = log_lower_cert(2 * lam)  # log(39/20)
Irho_LB = sum(w * v for w, (v, k, r) in zip(weights, certs))
Cstar_UB = -2 * lam + 16 * alph * lam * (1 - a_cert) + 3 * lam * lam - 2 * lam * lam * l_cert
f_cert = lam * M0 - Irho_LB + Cstar_UB
print(f"Irho8 认证下界 = {float(Irho_LB):.10f}")
print(f"Cstar8 认证上界 = {float(Cstar_UB):.10f}")
print(f"f 认证值 = {float(f_cert):.10f}  (需 <= {float(U):.4f})")
assert f_cert <= U, "证书不足以证明 energy_const8！"
print("emitter check OK")

# ---- 发射 Lean ----
L = []
A = L.append
A("import Mathlib")
A("import Zeta7.Constants")
A("import Zeta7.Measure7")
A("import Apery.EnergyConst")
A("")
A("/-! # (6.4)-类比（b=8）：`λ M₀ - I(ρ) + C* ≤ U` 的数值认证")
A("")
A("镜像 `Apery.EnergyConst`（b=6）。16 个原子 `(bρ8 j − aρ8 j)/4` 的 log 下界由")
A("`Apery.log_ge_of_pow_two`（artanh 部分和 + 2 的幂值域归约）认证，证书值由")
A("`research/gen_energy_const8.py` 以精确有理算术向下舍入生成，`norm_num` 逐项核验。")
A("-/")
A("")
A("open Finset")
A("")
A("namespace Zeta7")
A("")
A("/-- **(6.4)-类比**（b=8, (K:N:h) = 40:1:39）：`lam8 * M0_8 - Irho8 + Cstar8 ≤ U`。 -/")
A("theorem energy_const8 : lam8 * M0_8 - Irho8 + Cstar8 ≤ (U : ℝ) := by")
for j in range(16):
    v, k, r = certs[j]
    A(f"  have h{j+1} : {rstr(v)} ≤ Real.log ((bρ8 {j+1} - aρ8 {j+1}) / 4) := by")
    A(f"    have e : ((bρ8 {j+1} - aρ8 {j+1}) / 4) = ({atoms[j].numerator} / {atoms[j].denominator} : ℝ) := by")
    A("      simp [aρ8, bρ8, table7]; norm_num")
    A("    rw [e]")
    A(f"    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) {k} {M_TERMS} (by norm_num))")
    A("    simp only [Finset.sum_range_succ, Finset.sum_range_zero]")
    A("    norm_num")
# alph / 2*lam 的下界
A(f"  have hα8 : {rstr(a_cert)} ≤ Real.log alph8 := by")
A("    have e : alph8 = (1 / 40 : ℝ) := by norm_num [alph8]")
A("    rw [e]")
A(f"    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) {a_k} {M_TERMS} (by norm_num))")
A("    simp only [Finset.sum_range_succ, Finset.sum_range_zero]")
A("    norm_num")
A(f"  have hl8 : {rstr(l_cert)} ≤ Real.log (2 * lam8) := by")
A("    have e : (2 * lam8) = (39 / 20 : ℝ) := by norm_num [lam8]")
A("    rw [e]")
A(f"    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) {l_k} {M_TERMS} (by norm_num))")
A("    simp only [Finset.sum_range_succ, Finset.sum_range_zero]")
A("    norm_num")
# Sρ8 部分和
A("  have hS0 : Sρ8 0 = (0 : ℝ) := by simp [Sρ8]")
for j in range(16):
    A(f"  have hS{j+1} : Sρ8 {j+1} = {rstr(S[j])} := by")
    A("    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num")
# Irho8 展开
terms = " + ".join(f"({rstr(w)}) * Real.log ((bρ8 {j+1} - aρ8 {j+1}) / 4)"
                   for j, w in enumerate(weights))
A(f"  have hI : Irho8 = {terms} := by")
tops = "\n    ".join(f"Finset.sum_Icc_succ_top (show 1 ≤ {i} by norm_num),"
                    for i in range(16, 1, -1))
A(f"    simp only [Irho8, {tops} Finset.Icc_self, Finset.sum_singleton]")
A("    simp only [hS0, hS1, hS2, hS3, hS4, hS5, hS6, hS7, hS8, hS9, hS10, hS11, hS12, hS13, hS14, hS15, hS16]")
A("    norm_num")
A("  rw [hI]")
A("  unfold Cstar8")
A("  norm_num [U, M0_8, lam8, alph8] at *")
A("  linarith")
A("")
A("end Zeta7")

out = "\n".join(L) + "\n"
with open("Zeta7Formal/Zeta7/EnergyConst8.lean", "w", encoding="utf-8") as f:
    f.write(out)
print(f"written Zeta7Formal/Zeta7/EnergyConst8.lean ({len(out)} chars)")
