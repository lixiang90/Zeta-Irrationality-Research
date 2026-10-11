import Mathlib
import Zeta7.Phi8
import Zeta7.Potential8

/-!
# b=8 位势不等式的归约层（镜像 `Apery/PotentialIneq.lean`）

复用 Apery 的证书形状（Uω_le_inside/right/left、log_le_of_pow_two_upper、
arctan_ge_half/le_half 等，b 无关）；b=8 部分：Uρ8_eq 展开、Vstar8 (A.6)、
Vfield8_ge_Vstar、Uρ8_le_log（λ = 39/40）、potential_ineq_tail8（尾部常数重算：
2λ = 1.95、8α = 0.2、2−16α = 1.6、e3 常数 16α = 0.4）。
-/

open Finset Set
open scoped BigOperators

namespace Zeta7

open Apery (Uω)

/-! ### 证书形状（抄录自 `Apery/PotentialIneq.lean`，该文件不在 Apery 的编译闭包内，
故此处内联为 Zeta7 引理；内容 b 无关，署名 mo271 / Apache-2.0）。 -/

lemma Uω_le_inside {a b t u : ℝ} (h1 : a ≤ t) (h2 : t ≤ b) (hu : Real.log ((b - a) / 4) ≤ u) :
    Uω a b t ≤ u := by
  rw [Apery.Uω_of_mem h1 h2]; exact hu

lemma Uω_le_right {a b t s u : ℝ} (hab : a < b) (h : b ≤ t) (hs0 : 0 ≤ s)
    (hs : (t - a) * (t - b) ≤ s ^ 2) (hu : Real.log ((t - (a + b) / 2 + s) / 2) ≤ u) :
    Uω a b t ≤ u := by
  rw [Apery.Uω_of_ge hab h]
  refine le_trans (Real.log_le_log ?_ ?_) hu
  · have := Real.sqrt_nonneg ((t - a) * (t - b)); linarith
  · have : Real.sqrt ((t - a) * (t - b)) ≤ s := Real.sqrt_le_iff.mpr ⟨hs0, hs⟩
    linarith

lemma Uω_le_left {a b t s u : ℝ} (hab : a < b) (h : t ≤ a) (hs0 : 0 ≤ s)
    (hs : (t - a) * (t - b) ≤ s ^ 2) (hu : Real.log (((a + b) / 2 - t + s) / 2) ≤ u) :
    Uω a b t ≤ u := by
  rw [Apery.Uω_of_le hab h]
  refine le_trans (Real.log_le_log ?_ ?_) hu
  · have := Real.sqrt_nonneg ((t - a) * (t - b)); linarith
  · have : Real.sqrt ((t - a) * (t - b)) ≤ s := Real.sqrt_le_iff.mpr ⟨hs0, hs⟩
    linarith

lemma Uω_le_log8 {a b t : ℝ} (ha : 0 ≤ a) (hab : a < b) (h : b ≤ t) : Uω a b t ≤ Real.log t := by
  rw [Apery.Uω_of_ge hab h]
  refine Real.log_le_log ?_ ?_
  · have := Real.sqrt_nonneg ((t - a) * (t - b)); linarith
  · have hs : Real.sqrt ((t - a) * (t - b)) ≤ t - (a + b) / 2 := by
      refine Real.sqrt_le_iff.mpr ⟨by linarith, ?_⟩
      nlinarith [sq_nonneg (a - b)]
    linarith

/-- `Uρ8` 的十六项显式展开（Table 7 证书发射用）。 -/
lemma Uρ8_eq (t : ℝ) : Uρ8 t =
    cρ8 1 * Uω (aρ8 1) (bρ8 1) t + cρ8 2 * Uω (aρ8 2) (bρ8 2) t + cρ8 3 * Uω (aρ8 3) (bρ8 3) t +
    cρ8 4 * Uω (aρ8 4) (bρ8 4) t + cρ8 5 * Uω (aρ8 5) (bρ8 5) t + cρ8 6 * Uω (aρ8 6) (bρ8 6) t +
    cρ8 7 * Uω (aρ8 7) (bρ8 7) t + cρ8 8 * Uω (aρ8 8) (bρ8 8) t + cρ8 9 * Uω (aρ8 9) (bρ8 9) t +
    cρ8 10 * Uω (aρ8 10) (bρ8 10) t + cρ8 11 * Uω (aρ8 11) (bρ8 11) t + cρ8 12 * Uω (aρ8 12) (bρ8 12) t +
    cρ8 13 * Uω (aρ8 13) (bρ8 13) t + cρ8 14 * Uω (aρ8 14) (bρ8 14) t + cρ8 15 * Uω (aρ8 15) (bρ8 15) t +
    cρ8 16 * Uω (aρ8 16) (bρ8 16) t := by
  unfold Uρ8
  simp only [Finset.sum_Icc_succ_top (show 1 ≤ 16 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 15 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 14 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 13 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 12 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 11 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 10 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 9 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 8 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 7 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 6 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 5 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 4 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 3 by norm_num), Finset.sum_Icc_succ_top (show 1 ≤ 2 by norm_num),
    Finset.Icc_self, Finset.sum_singleton]

/-- `V*` of (A.6) 类比（系数 6→8，qm/qp → qm8/qp8）。 -/
noncomputable def Vstar8 : ℝ :=
  Real.log (1 + qm8) - 8 * (1 / 40 : ℝ) * Real.log (qp8 + (1 / 40 : ℝ) ^ 2) - 2 + 16 * (1 / 40 : ℝ) +
    2 * Real.sqrt qp8 * (Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8))

lemma Vfield8_ge_Vstar {t : ℝ} (h1 : qm8 ≤ t) (h2 : t ≤ qp8) : Vstar8 ≤ Vfield8 t := by
  have hqm : (0 : ℝ) < qm8 := by norm_num
  have ht : 0 < t := hqm.trans_le h1
  rw [Vfield8_eq ht]
  unfold Vstar8
  have hs1 : Real.sqrt qm8 ≤ Real.sqrt t := Real.sqrt_le_sqrt h1
  have hs2 : Real.sqrt t ≤ Real.sqrt qp8 := Real.sqrt_le_sqrt h2
  have hsqm := sqrt_qm8_pos
  have hst : 0 < Real.sqrt t := Real.sqrt_pos.mpr ht
  have hP1 : Real.arctan (1 / Real.sqrt qp8) ≤ Real.arctan (1 / Real.sqrt t) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hst hs2)
  have hP2 : Real.arctan ((1 / 40 : ℝ) / Real.sqrt t) ≤ Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hsqm hs1)
  have hPneg : Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8) < 0 := by
    have := Pfun8_sqrt_qm8_neg
    unfold Pfun8 at this
    have h := Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsqm
      (Real.sqrt_le_sqrt (by norm_num : qm8 ≤ qp8)))
    linarith
  have hL1 : Real.log (1 + qm8) ≤ Real.log (1 + t) := Real.log_le_log (by norm_num) (by linarith)
  have hL2 : Real.log (t + (1 / 40 : ℝ) ^ 2) ≤ Real.log (qp8 + (1 / 40 : ℝ) ^ 2) :=
    Real.log_le_log (by positivity) (add_le_add h2 le_rfl)
  have hprod : 2 * Real.sqrt qp8 * (Real.pi + Real.arctan (1 / Real.sqrt qp8) -
      8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8)) ≤
      2 * Real.sqrt t * (Real.pi + Real.arctan (1 / Real.sqrt t) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt t)) := by
    have hPle : Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8) ≤
        Real.pi + Real.arctan (1 / Real.sqrt t) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt t) := by linarith
    calc 2 * Real.sqrt qp8 * (Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8))
        ≤ 2 * Real.sqrt t * (Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8)) :=
          mul_le_mul_of_nonpos_right (by linarith) hPneg.le
      _ ≤ _ := mul_le_mul_of_nonneg_left hPle (by positivity)
  have hL2' : 8 * (1 / 40 : ℝ) * Real.log (t + (1 / 40 : ℝ) ^ 2) ≤ 8 * (1 / 40 : ℝ) * Real.log (qp8 + (1 / 40 : ℝ) ^ 2) :=
    mul_le_mul_of_nonneg_left hL2 (by norm_num)
  set X := Real.log (1 + t) with hX
  set Y := Real.log (t + (1 / 40 : ℝ) ^ 2) with hY
  set A := 2 * Real.sqrt t * (Real.pi + Real.arctan (1 / Real.sqrt t) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt t)) with hA
  set X0 := Real.log (1 + qm8) with hX0
  set Y0 := Real.log (qp8 + (1 / 40 : ℝ) ^ 2) with hY0
  set A0 := 2 * Real.sqrt qp8 * (Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40 : ℝ) / Real.sqrt qm8)) with hA0
  linarith

/-- 尾部的 `Uρ8 ≤ λ log t`（λ = 39/40）。 -/
lemma Uρ8_le_log {t : ℝ} (ht : 2 ≤ t) : Uρ8 t ≤ (39 / 40) * Real.log t := by
  unfold Uρ8
  have hsum : ∑ j ∈ Finset.Icc 1 16, cρ8 j = 39 / 40 := by
    have := Sρ8_sixteen; unfold Sρ8 at this; rw [this]
  rw [← hsum, Finset.sum_mul]
  refine Finset.sum_le_sum fun j hj => ?_
  refine mul_le_mul_of_nonneg_left ?_ (cρ8_pos j hj).le
  refine Uω_le_log8 ?_ (aρ8_lt_bρ8 j hj) ?_
  · simp only [Finset.mem_Icc] at hj; obtain ⟨hj1, hj2⟩ := hj
    interval_cases j <;> norm_num [aρ8, table7]
  · have : bρ8 j ≤ 2 := by
      simp only [Finset.mem_Icc] at hj; obtain ⟨hj1, hj2⟩ := hj
      interval_cases j <;> norm_num [bρ8, table7]
    linarith

/-- `2 Uρ8(t) − V₈(t) ≤ M₀_8` 对 `t ≥ 2`（尾部；b=8 常数重算）。 -/
theorem potential_ineq_tail8 {t : ℝ} (ht : 2 ≤ t) : 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  have ht0 : 0 < t := by linarith
  have hU := Uρ8_le_log ht
  rw [Vfield8_eq ht0]
  set s := Real.sqrt t with hs
  have hs2 : s ^ 2 = t := Real.sq_sqrt ht0.le
  have hs_ge : Real.sqrt 2 ≤ s := Real.sqrt_le_sqrt ht
  have hsqrt2 : (1.4 : ℝ) ≤ Real.sqrt 2 := Real.le_sqrt_of_sq_le (by norm_num)
  have hs1 : 1 < s := by linarith
  have hlog1 : Real.log t ≤ Real.log (1 + t) := Real.log_le_log ht0 (by linarith)
  have hlog2 : Real.log (t + (1 / 40 : ℝ) ^ 2) ≤ Real.log t + (1 / 40 : ℝ) ^ 2 / t := by
    have : Real.log (t + (1 / 40 : ℝ) ^ 2) = Real.log t + Real.log (1 + (1 / 40 : ℝ) ^ 2 / t) := by
      rw [← Real.log_mul ht0.ne' (by positivity)]; congr 1; field_simp
    rw [this]
    have := Real.log_le_sub_one_of_pos (by positivity : (0:ℝ) < 1 + (1 / 40 : ℝ) ^ 2 / t)
    linarith
  have harc1 : 1 / s - (1 / s) ^ 3 / 3 ≤ Real.arctan (1 / s) := by
    have h := Apery.arctan_ge_partial (x := 1 / s) (by positivity) (by rw [div_lt_one (by linarith)]; exact hs1) 1
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, one_div, inv_pow] at h ⊢
    norm_num at h ⊢
    linarith
  have harc2 : Real.arctan ((1 / 40 : ℝ) / s) ≤ (1 / 40 : ℝ) / s := Apery.arctan_le_self' (by positivity)
  have hlogt : Real.log t = 2 * Real.log s := by rw [← hs2, Real.log_pow]; push_cast; ring
  have hlogs : Real.log s ≤ s - 1 := Real.log_le_sub_one_of_pos (by linarith)
  have hpi := Real.pi_gt_three
  have hpos : 0 < s := by linarith
  have hkey : 2 * s * (Real.pi + Real.arctan (1 / s) - 8 * Real.arctan ((1 / 40 : ℝ) / s)) ≥
      2 * s * Real.pi + 2 - 2 / (3 * t) - 0.4 := by
    have e1 : 2 * s * (1 / s) = 2 := by field_simp
    have e2 : 2 * s * ((1 / s) ^ 3 / 3) = 2 / (3 * t) := by rw [← hs2]; field_simp; try ring
    have e3 : 2 * s * (8 * ((1 / 40 : ℝ) / s)) = 0.4 := by field_simp; try ring
    nlinarith [harc1, harc2, e1, e2, e3, hpos]
  have ht_inv : 2 / (3 * t) + (1 / 40 : ℝ) ^ 2 / t * (8 * (1 / 40 : ℝ)) ≤ 1 := by
    have e : 2 / (3 * t) + (1 / 40 : ℝ) ^ 2 / t * (8 * (1 / 40 : ℝ)) =
        (2 / 3 + (1 / 40 : ℝ) ^ 2 * (8 * (1 / 40 : ℝ))) / t := by
      field_simp; try ring
    rw [e, div_le_one ht0]
    linarith
  have hpi' : (3.14 : ℝ) < Real.pi := Real.pi_gt_d2
  have hsqrt2' : (1.41 : ℝ) ≤ Real.sqrt 2 := Real.le_sqrt_of_sq_le (by norm_num)
  have hspi : s * 3.14 ≤ s * Real.pi := mul_le_mul_of_nonneg_left hpi'.le hpos.le
  show _ ≤ -6.35
  nlinarith [hU, hlog1, hlog2, hkey, hlogt, hlogs, hs_ge, hsqrt2', ht_inv, hspi]

end Zeta7
