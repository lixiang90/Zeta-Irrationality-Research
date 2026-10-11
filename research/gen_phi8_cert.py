#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 Φ/Pfun 证书生成器：计算全部有理常数并发射 Zeta7/Phi8.lean。

内容（镜像 Apery/Potential.lean 的 Φ/Pfun 部分，系数 6→8）：
- Pfun8/Φ8 定义、hasDerivAt、y0_8 = √(319/1280) 处导数符号、单调性；
- qm8 = 7/5000, qp8 = 9/6250（V 极小窗口，含根 0.00142887）；
- 符号证书 Pfun8_sqrt_qm8_neg / Pfun8_sqrt_qp8_pos（mo271 式有理界证明，数值预检）。
"""
from fractions import Fraction as F
import math

AL = F(1, 40)
QM = F(7, 5000)      # 0.0014
QP = F(9, 6250)      # 0.00144

def sqrt_squeeze(q, prec=10**14):
    s = F(math.isqrt((q.numerator * prec * prec) // q.denominator), prec)
    while s * s > q: s -= F(1, prec)
    while (s + F(1, prec)) ** 2 <= q: s += F(1, prec)
    return s, s + F(1, prec)

def atan_poly(x, n):
    """Σ_{i<n} (−1)^i x^{2i+1}/(2i+1)，Fraction 精确。"""
    s = F(0); xp = x
    for i in range(n):
        s += xp / (2 * i + 1) if i % 2 == 0 else -xp / (2 * i + 1)
        xp *= x * x
    return s

def atan_rem(x, n):
    return x ** (2 * n + 1) / (2 * n + 1)

def lean(q):
    return f"({q.numerator} / {q.denominator} : ℝ)" if q.denominator != 1 else f"({q.numerator} : ℝ)"

# ---------- √qm / √qp 夹逼 ----------
qm_lo, qm_hi = sqrt_squeeze(QM)
qp_lo, qp_hi = sqrt_squeeze(QP)

# ---------- Pfun(√qm) < 0 的常数 ----------
# 需：π + π/2 − atan(s) − 8 atan(α/s) < 0
# 下界：atan(s) ≥ P16(s_lo)；atan(α/s) ≥ 2·(P28(x_lo))，x_lo = (α/s_hi)/(1+sqrt_hi(1+(α/s_hi)²))
s_lo, s_hi = qm_lo, qm_hi
x_for = AL / s_hi
sq_for = 1 + x_for * x_for
_, sq_hi = sqrt_squeeze(sq_for)
x_lo = x_for / (1 + sq_hi)
P16 = atan_poly(s_lo, 16)
R16 = atan_rem(s_lo, 16)
P28 = atan_poly(x_lo, 28)
R28 = atan_rem(x_lo, 28)
# 数值预检（含余项 slack）
pi_hi = F(31415926535897932384626433832796, 10**31)
lhs = pi_hi + pi_hi / 2                       # π + π/2 上界
rhs = (P16 - R16) + 8 * (2 * (P28 - R28))     # atan(s) + 8·atan(α/s) 下界（atan(α/s) ≥ 2 atan(x) ≥ 2(P28−R28)）
assert lhs < rhs, f"Pfun(√qm8)<0 证书数值预检失败: {float(lhs)} !< {float(rhs)}"
margin1 = rhs - lhs

# ---------- Pfun(√qp) > 0 的常数 ----------
# 需：π + π/2 − atan(s) − 8 atan(α/s) > 0
# 上界：atan(s) ≤ P17(s_hi)+R17；atan(α/s) ≤ 2·(P29(x_hi)+R29)，x_hi = (α/s_lo)/(1+sqrt_lo(1+(α/s_lo)²))
s2_lo, s2_hi = qp_lo, qp_hi
x2_for = AL / s2_lo
sq2_for = 1 + x2_for * x2_for
sq2_lo, _ = sqrt_squeeze(sq2_for)
x2_hi = x2_for / (1 + sq2_lo)
P17 = atan_poly(s2_hi, 17)
R17 = atan_rem(s2_hi, 17)
P29 = atan_poly(x2_hi, 29)
R29 = atan_rem(x2_hi, 29)
pi_lo = F(31415926535897932384626433832795, 10**31)
lhs2 = pi_lo + pi_lo / 2
rhs2 = (P17 + R17) + 8 * (2 * (P29 + R29))
assert rhs2 < lhs2, f"Pfun(√qp8)>0 证书数值预检失败: {float(rhs2)} !< {float(lhs2)}"
margin2 = lhs2 - rhs2

print(f"预检通过：qm 证书余量 {float(margin1):.3e}，qp 证书余量 {float(margin2):.3e}")

# ---------- 发射 ----------
header = '''import Mathlib
import Zeta7.Field8
import Zeta7.Potential8
import Apery.Certificates

/-!
# b=8 的 Φ/Pfun 与 V₈ 的单峰性（镜像 `Apery/Potential.lean` 后半）

`P(y) = π + atan(1/y) − 8 atan(α/y)`（α = 1/40）：`Φ'(y) = 2P(y)`，V₈(t) = Φ(√t)。
P 在 y₀ = √(319/1280) 处取最大（y₀² = α(8−α)/(1−8α)），在 (0, y₀) 递增、(y₀, ∞) 递减；
P(0⁺) = −5π/2 < 0，P(y₀) > 0，P(+∞) = π > 0，故恰有一零点 y₁（Φ 的唯一极小点），
t₁ = y₁² ∈ (qm8, qp8) = (7/5000, 9/6250)。符号证书由 `research/gen_phi8_cert.py` 生成。
-/

open Filter Topology Set MeasureTheory Finset

namespace Zeta7

/-- `P(y) = π + atan(1/y) − 8 atan(α/y)`（b=8；Apery.Pfun 的系数 6→8）。 -/
noncomputable def Pfun8 (y : ℝ) : ℝ :=
  Real.pi + Real.arctan (1 / y) - 8 * Real.arctan ((1 / 40 : ℝ) / y)

/-- `Φ(y) = V₈(y²)`（Apery.Φ 的系数 6→8、12→16）。 -/
noncomputable def Φ8 (y : ℝ) : ℝ :=
  Real.log (1 + y ^ 2) - 8 * (1 / 40 : ℝ) * Real.log (y ^ 2 + (1 / 40 : ℝ) ^ 2) - 2 + 16 * (1 / 40 : ℝ) +
    2 * y * Pfun8 y

lemma Vfield8_eq_Φ8 {t : ℝ} (ht : 0 < t) : Vfield8 t = Φ8 (Real.sqrt t) := by
  rw [Vfield8_eq ht]
  unfold Φ8 Pfun8
  rw [Real.sq_sqrt ht.le]

lemma hasDerivAt_Φ8 {y : ℝ} (hy : 0 < y) : HasDerivAt Φ8 (2 * Pfun8 y) y := by
  have h1 := ((hasDerivAt_pow 2 y).const_add (1 : ℝ)).log (by positivity : (1 : ℝ) + y ^ 2 ≠ 0)
  have h2 := (((hasDerivAt_pow 2 y).add_const ((1 / 40 : ℝ) ^ 2)).log (by positivity)).const_mul
    (8 * (1 / 40 : ℝ))
  have h3 := (hasDerivAt_inv hy.ne').arctan
  have h4 := ((hasDerivAt_inv hy.ne').const_mul (1 / 40 : ℝ)).arctan
  have hP0 := ((hasDerivAt_const y Real.pi).add h3).sub (h4.const_mul 8)
  have hP : HasDerivAt Pfun8 _ y :=
    hP0.congr_of_eventuallyEq (Filter.Eventually.of_forall fun x => by
      simp only [Pfun8, Pi.add_apply, Pi.sub_apply, one_div, div_eq_mul_inv, one_mul])
  have h5 := ((hasDerivAt_id y).const_mul (2 : ℝ)).mul hP
  have h := (((h1.sub h2).sub_const (2 : ℝ)).add_const (16 * (1 / 40 : ℝ))).add h5
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun x => ?_)).congr_deriv ?_
  · simp only [Φ8, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, id]
    try ring
  · unfold Pfun8
    have hne1 : (1 : ℝ) + y ^ 2 ≠ 0 := by positivity
    have hne2 : y ^ 2 + (1 / 40 : ℝ) ^ 2 ≠ 0 := by positivity
    simp only [Nat.cast_ofNat, show (2 : ℕ) - 1 = 1 from rfl, pow_one, id]
    field_simp
    ring

lemma hasDerivAt_Pfun8 {y : ℝ} (hy : 0 < y) :
    HasDerivAt Pfun8 (-1 / (y ^ 2 + 1) + 8 * (1 / 40 : ℝ) / (y ^ 2 + (1 / 40 : ℝ) ^ 2)) y := by
  have h3 := (hasDerivAt_inv hy.ne').arctan
  have h4 := ((hasDerivAt_inv hy.ne').const_mul (1 / 40 : ℝ)).arctan
  have hP0 := ((hasDerivAt_const y Real.pi).add h3).sub (h4.const_mul 8)
  refine (hP0.congr_of_eventuallyEq (Filter.Eventually.of_forall fun x => by
    simp only [Pfun8, Pi.add_apply, Pi.sub_apply, one_div, div_eq_mul_inv, one_mul])).congr_deriv ?_
  have hne1 : y ^ 2 + (1 : ℝ) ≠ 0 := by positivity
  have hne2 : y ^ 2 + (1 / 40 : ℝ) ^ 2 ≠ 0 := by positivity
  field_simp
  ring

/-- 拐点 y₀² = α(8−α)/(1−8α) = 319/1280。 -/
noncomputable abbrev y0_8 : ℝ := Real.sqrt (319 / 1280)

lemma deriv_Pfun8_nonneg {y : ℝ} (hy : 0 < y) (hy0 : y ≤ y0_8) :
    0 ≤ -1 / (y ^ 2 + 1) + 8 * (1 / 40 : ℝ) / (y ^ 2 + (1 / 40 : ℝ) ^ 2) := by
  have hy2 : y ^ 2 ≤ 319 / 1280 := by
    have := Real.sqrt_le_sqrt (le_of_eq (Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 319 / 1280)).symm)
    calc y ^ 2 ≤ y0_8 ^ 2 := pow_le_pow_left₀ hy.le hy0 2
      _ = 319 / 1280 := Real.sq_sqrt (by norm_num)
  rw [div_add_div _ _ (by positivity) (by positivity)]
  refine div_nonneg ?_ (by positivity)
  nlinarith

lemma deriv_Pfun8_nonpos {y : ℝ} (hy0 : y0_8 ≤ y) :
    -1 / (y ^ 2 + 1) + 8 * (1 / 40 : ℝ) / (y ^ 2 + (1 / 40 : ℝ) ^ 2) ≤ 0 := by
  have hy2 : 319 / 1280 ≤ y ^ 2 := by
    calc (319 / 1280 : ℝ) = y0_8 ^ 2 := (Real.sq_sqrt (by norm_num)).symm
      _ ≤ y ^ 2 := pow_le_pow_left₀ (Real.sqrt_nonneg _) hy0 2
  rw [div_add_div _ _ (by positivity) (by positivity)]
  refine div_nonpos_of_nonpos_of_nonneg ?_ (by positivity)
  nlinarith

lemma Pfun8_monotoneOn : MonotoneOn Pfun8 (Ioc 0 y0_8) := by
  refine monotoneOn_of_deriv_nonneg (convex_Ioc 0 y0_8) ?_ ?_ ?_
  · intro y hy; exact (hasDerivAt_Pfun8 hy.1).continuousAt.continuousWithinAt
  · intro y hy
    rw [interior_Ioc] at hy
    exact (hasDerivAt_Pfun8 hy.1).differentiableAt.differentiableWithinAt
  · intro y hy
    rw [interior_Ioc] at hy
    rw [(hasDerivAt_Pfun8 hy.1).deriv]
    exact deriv_Pfun8_nonneg hy.1 hy.2.le

lemma Pfun8_antitoneOn : AntitoneOn Pfun8 (Ici y0_8) := by
  have hy0 : 0 < y0_8 := Real.sqrt_pos.mpr (by norm_num)
  refine antitoneOn_of_deriv_nonpos (convex_Ici y0_8) ?_ ?_ ?_
  · intro y hy; exact (hasDerivAt_Pfun8 (hy0.trans_le hy)).continuousAt.continuousWithinAt
  · intro y hy
    rw [interior_Ici] at hy
    exact (hasDerivAt_Pfun8 (hy0.trans hy)).differentiableAt.differentiableWithinAt
  · intro y hy
    rw [interior_Ici] at hy
    rw [(hasDerivAt_Pfun8 (hy0.trans hy)).deriv]
    exact deriv_Pfun8_nonpos (le_of_lt hy)
'''

# ---- 证书引理（数值常数内嵌）----
cert = '''
/-- V₈ 极小窗口（含 Φ 的唯一极小点 t₁ = y₁²）。 -/
noncomputable abbrev qm8 : ℝ := 7 / 5000
noncomputable abbrev qp8 : ℝ := 9 / 6250

lemma sqrt_qm8_pos : 0 < Real.sqrt qm8 := Real.sqrt_pos.mpr (by norm_num)
lemma sqrt_qp8_pos : 0 < Real.sqrt qp8 := Real.sqrt_pos.mpr (by norm_num)

/-- 数值事实（证书）：`P(√q₋) < 0`。常数由 `research/gen_phi8_cert.py` 生成。 -/
lemma Pfun8_sqrt_qm8_neg : Pfun8 (Real.sqrt qm8) < 0 := by
  set s := Real.sqrt qm8 with hs
  have hs_pos : 0 < s := sqrt_qm8_pos
  have hs_lo : @@s_lo@@ ≤ s := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)
  have hs_hi : s ≤ @@s_hi@@ := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)
  have h1 : Real.arctan (1 / s) = Real.pi / 2 - Real.arctan s := by
    rw [one_div, Real.arctan_inv_of_pos hs_pos]
  have hS2 : @@P16 - R16@@ ≤ ∑ i ∈ Finset.range (2 * 8), (-1 : ℝ) ^ i * (@@s_lo@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
  have h2 : @@P16 - R16@@ ≤ Real.arctan s :=
    hS2.trans ((Apery.arctan_ge_partial (by norm_num) (by norm_num) 8).trans
      (Real.arctan_strictMono.monotone hs_lo))
  have h3 : Real.arctan ((1 / 40 : ℝ) / @@s_hi@@) ≤ Real.arctan ((1 / 40 : ℝ) / s) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hs_pos hs_hi)
  have h4 : Real.arctan ((1 / 40 : ℝ) / @@s_hi@@) =
      2 * Real.arctan (((1 / 40 : ℝ) / @@s_hi@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s_hi@@) ^ 2))) :=
    Apery.arctan_eq_two_mul_arctan (by norm_num)
  have h5 : @@x_lo@@ ≤ ((1 / 40 : ℝ) / @@s_hi@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s_hi@@) ^ 2)) := by
    have hsq : Real.sqrt (1 + ((1 / 40 : ℝ) / @@s_hi@@) ^ 2) ≤ @@sq_hi@@ := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)
    rw [show @@x_lo@@ = ((1 / 40 : ℝ) / @@s_hi@@) / (1 + @@sq_hi@@) by norm_num]
    exact div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)
  have hS6 : @@2*(P28 - R28)@@ ≤ 2 * ∑ i ∈ Finset.range (2 * 14), (-1 : ℝ) ^ i * (@@x_lo@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
  have hx0 : (0:ℝ) ≤ @@x_lo@@ := by norm_num
  have hx1 : @@x_lo@@ < 1 := by norm_num
  have step1 : 2 * ∑ i ∈ Finset.range (2 * 14), (-1 : ℝ) ^ i * (@@x_lo@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) ≤ 2 * Real.arctan (((1 / 40 : ℝ) / @@s_hi@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s_hi@@) ^ 2))) :=
    mul_le_mul_of_nonneg_left ((Apery.arctan_ge_partial hx0 hx1 14).trans
      (Real.arctan_strictMono.monotone h5)) (by norm_num : (0:ℝ) ≤ 2)
  have h6 := step1
  have hpi := Real.pi_lt_d20
  unfold Pfun8
  rw [h1]
  linarith

/-- 数值事实（证书）：`0 < P(√q₊)`。常数由 `research/gen_phi8_cert.py` 生成。 -/
lemma Pfun8_sqrt_qp8_pos : 0 < Pfun8 (Real.sqrt qp8) := by
  set s := Real.sqrt qp8 with hs
  have hs_pos : 0 < s := sqrt_qp8_pos
  have hs_lo : @@s2_lo@@ ≤ s := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)
  have hs_hi : s ≤ @@s2_hi@@ := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)
  have h1 : Real.arctan (1 / s) = Real.pi / 2 - Real.arctan s := by
    rw [one_div, Real.arctan_inv_of_pos hs_pos]
  have hS2 : ∑ i ∈ Finset.range (2 * 8 + 1), (-1 : ℝ) ^ i * (@@s2_hi@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) ≤ @@P17 + R17@@ := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
  have h2 : Real.arctan s ≤ @@P17 + R17@@ :=
    ((Real.arctan_strictMono.monotone hs_hi).trans (Apery.arctan_le_partial (by norm_num) (by norm_num) 8)).trans hS2
  have h3 : Real.arctan ((1 / 40 : ℝ) / s) ≤ Real.arctan ((1 / 40 : ℝ) / @@s2_lo@@) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) (by norm_num) hs_lo)
  have h4 : Real.arctan ((1 / 40 : ℝ) / @@s2_lo@@) =
      2 * Real.arctan (((1 / 40 : ℝ) / @@s2_lo@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s2_lo@@) ^ 2))) :=
    Apery.arctan_eq_two_mul_arctan (by norm_num)
  have h5 : ((1 / 40 : ℝ) / @@s2_lo@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s2_lo@@) ^ 2)) ≤ @@x2_hi@@ := by
    have hsq : @@sq2_lo@@ ≤ Real.sqrt (1 + ((1 / 40 : ℝ) / @@s2_lo@@) ^ 2) := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)
    rw [show @@x2_hi@@ = ((1 / 40 : ℝ) / @@s2_lo@@) / (1 + @@sq2_lo@@) by norm_num]
    exact div_le_div_of_nonneg_left (by norm_num) (by positivity) (by linarith)
  have hS6 : 2 * ∑ i ∈ Finset.range (2 * 14 + 1), (-1 : ℝ) ^ i * (@@x2_hi@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) ≤ @@2*(P29 + R29)@@ := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num
  have hx0 : (0:ℝ) ≤ @@x2_hi@@ := by norm_num
  have hx1 : @@x2_hi@@ < 1 := by norm_num
  have step1 : 2 * Real.arctan (((1 / 40 : ℝ) / @@s2_lo@@) / (1 + Real.sqrt (1 + ((1 / 40 : ℝ) / @@s2_lo@@) ^ 2))) ≤ 2 * ∑ i ∈ Finset.range (2 * 14 + 1), (-1 : ℝ) ^ i * (@@x2_hi@@ ^ (2 * i + 1) / (2 * (i : ℝ) + 1)) :=
    mul_le_mul_of_nonneg_left ((Real.arctan_strictMono.monotone h5).trans
      (Apery.arctan_le_partial hx0 hx1 14)) (by norm_num : (0:ℝ) ≤ 2)
  have h6 := step1.trans hS6
  have hpi := Real.pi_gt_d20
  unfold Pfun8
  rw [h1]
  linarith

lemma Pfun8_pos_of_one_le {y : ℝ} (hy : 1 ≤ y) : 0 < Pfun8 y := by
  unfold Pfun8
  have h1 : 0 ≤ Real.arctan (1 / y) := Real.arctan_nonneg.mpr (by positivity)
  have h2 : Real.arctan ((1 / 40 : ℝ) / y) ≤ (1 / 40 : ℝ) / y := Apery.arctan_le_self' (by positivity)
  have h3 : (1 / 40 : ℝ) / y ≤ 1 / 40 := by
    rw [div_le_iff₀ (by linarith)]; nlinarith
  linarith [Real.pi_gt_three]

lemma Pfun8_one_pos : 0 < Pfun8 1 := Pfun8_pos_of_one_le le_rfl

/-- `P ≤ 0` on `(0, √q₋]`。 -/
lemma Pfun8_nonpos {y : ℝ} (hy : 0 < y) (hy' : y ≤ Real.sqrt qm8) : Pfun8 y ≤ 0 :=
  (Pfun8_monotoneOn ⟨hy, hy'.trans sqrt_qm8_le_y0⟩ ⟨sqrt_qm8_pos, sqrt_qm8_le_y0⟩ hy').trans
    Pfun8_sqrt_qm8_neg.le

/-- `0 ≤ P` on `[√q₊, ∞)`。 -/
lemma Pfun8_nonneg {y : ℝ} (hy : Real.sqrt qp8 ≤ y) : 0 ≤ Pfun8 y := by
  rcases le_or_gt y y0_8 with h | h
  · exact Pfun8_sqrt_qp8_pos.le.trans (Pfun8_monotoneOn ⟨sqrt_qp8_pos, sqrt_qp8_le_y0⟩
      ⟨sqrt_qp8_pos.trans_le hy, h⟩ hy)
  · rcases le_or_gt y 1 with h1 | h1
    · have hy0 : y0_8 ≤ 1 := by
        rw [show (1 : ℝ) = Real.sqrt 1 by simp]; exact Real.sqrt_le_sqrt (by norm_num)
      exact Pfun8_one_pos.le.trans (Pfun8_antitoneOn (show y ∈ Ici y0_8 from h.le)
        (show (1:ℝ) ∈ Ici y0_8 from hy0) h1)
    · exact (Pfun8_pos_of_one_le h1.le).le

lemma Φ8_antitoneOn : AntitoneOn Φ8 (Ioc 0 (Real.sqrt qm8)) := by
  refine antitoneOn_of_deriv_nonpos (convex_Ioc _ _) ?_ ?_ ?_
  · intro y hy; exact (hasDerivAt_Φ8 hy.1).continuousAt.continuousWithinAt
  · intro y hy
    rw [interior_Ioc] at hy
    exact (hasDerivAt_Φ8 hy.1).differentiableAt.differentiableWithinAt
  · intro y hy
    rw [interior_Ioc] at hy
    rw [(hasDerivAt_Φ8 hy.1).deriv]
    linarith [Pfun8_nonpos hy.1 hy.2.le]

lemma Φ8_monotoneOn : MonotoneOn Φ8 (Ici (Real.sqrt qp8)) := by
  refine monotoneOn_of_deriv_nonneg (convex_Ici _) ?_ ?_ ?_
  · intro y hy; exact (hasDerivAt_Φ8 (sqrt_qp8_pos.trans_le hy)).continuousAt.continuousWithinAt
  · intro y hy
    rw [interior_Ici] at hy
    exact (hasDerivAt_Φ8 (sqrt_qp8_pos.trans hy)).differentiableAt.differentiableWithinAt
  · intro y hy
    rw [interior_Ici] at hy
    rw [(hasDerivAt_Φ8 (sqrt_qp8_pos.trans hy)).deriv]
    linarith [Pfun8_nonneg hy.le]

/-- V₈ 在 (0, qm8] 上单调不增。 -/
lemma Vfield8_antitoneOn : AntitoneOn Vfield8 (Ioc 0 qm8) := by
  intro x hx y hy hxy
  rw [Vfield8_eq_Φ8 hx.1, Vfield8_eq_Φ8 hy.1]
  exact Φ8_antitoneOn
    ⟨Real.sqrt_pos.mpr hx.1, Real.sqrt_le_sqrt hx.2⟩
    ⟨Real.sqrt_pos.mpr hy.1, Real.sqrt_le_sqrt hy.2⟩
    (Real.sqrt_le_sqrt hxy)

/-- V₈ 在 [qp8, ∞) 上单调不减。 -/
lemma Vfield8_monotoneOn : MonotoneOn Vfield8 (Ici qp8) := by
  intro x hx y hy hxy
  have hq : (0:ℝ) < qp8 := by norm_num
  have hx0 : (0:ℝ) < x := hq.trans_le hx
  have hy0 : (0:ℝ) < y := hq.trans_le hy
  rw [Vfield8_eq_Φ8 hx0, Vfield8_eq_Φ8 hy0]
  exact Φ8_monotoneOn (Real.sqrt_le_sqrt hx) (Real.sqrt_le_sqrt hy) (Real.sqrt_le_sqrt hxy)

end Zeta7
'''

# hy0_8_pos 在 Pfun8_nonpos 之后定义但前面引用了——调整顺序：把 hy0_8_pos 等提前
cert = cert.replace("""/-- `P ≤ 0` on `(0, √q₋]`。 -/
lemma Pfun8_nonpos""", """lemma hy0_8_pos : 0 < y0_8 := Real.sqrt_pos.mpr (by norm_num)
lemma sqrt_qm8_le_y0 : Real.sqrt qm8 ≤ y0_8 := Real.sqrt_le_sqrt (by norm_num)
lemma sqrt_qp8_le_y0 : Real.sqrt qp8 ≤ y0_8 := Real.sqrt_le_sqrt (by norm_num)

/-- `P ≤ 0` on `(0, √q₋]`。 -/
lemma Pfun8_nonpos""")
cert = cert.replace("""lemma hy0_8_pos : 0 < y0_8 := Real.sqrt_pos.mpr (by norm_num)
lemma sqrt_qm8_le_y0 : Real.sqrt qm8 ≤ y0_8 := Real.sqrt_le_sqrt (by norm_num)
lemma sqrt_qp8_le_y0 : Real.sqrt qp8 ≤ y0_8 := Real.sqrt_le_sqrt (by norm_num)

lemma Φ8_antitoneOn""", """lemma Φ8_antitoneOn""")
# 修正 Pfun8_nonpos 的调用（hy0_8_pos 已前置）
cert = cert.replace("(Ioc_subset_Ioc_right hsy ⟨hy0_8_pos, le_rfl⟩)", "(Ioc_subset_Ioc_right hsy ⟨sqrt_qm8_pos, sqrt_qm8_le_y0⟩)")

for _k, _v in {
    's_lo': s_lo, 's_hi': s_hi, 'sq_hi': sq_hi, 'x_lo': x_lo,
    'P16 - R16': P16 - R16, '2*(P28 - R28)': 2*(P28 - R28),
    's2_lo': s2_lo, 's2_hi': s2_hi, 'sq2_lo': sq2_lo, 'x2_hi': x2_hi,
    'P17 + R17': P17 + R17, '2*(P29 + R29)': 2*(P29 + R29),
}.items():
    cert = cert.replace('@@' + _k + '@@', lean(_v))
assert '@@' not in cert, "有未替换的令牌"
with open('Zeta7Formal/Zeta7/Phi8.lean', 'w', encoding='utf-8') as f:
    f.write(header + cert)
print("emitted Zeta7/Phi8.lean")
