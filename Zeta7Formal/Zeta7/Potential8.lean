import Mathlib
import Apery.Potential
import Zeta7.Measure7

/-!
# b=8 比较测度的位势 U^{ρ₈} 与单调性

镜像 `Apery/Potential.lean` 的 Uρ 部分（该文件的 Uω 闭式与单调性与 b 无关，
直接复用 `Apery.Uω` 及其引理）。Uρ8 用 b=8 表 table7 的质量/区间。
-/

open Filter Topology Set Finset

namespace Zeta7

open Apery (Uω Uω_of_mem Uω_of_ge Uω_of_le Uω_monotoneOn_Ici Uω_antitoneOn_Iic)

/-- b=8 比较测度 ρ₈ 的位势。 -/
noncomputable def Uρ8 (t : ℝ) : ℝ := ∑ j ∈ Icc 1 16, cρ8 j * Uω (aρ8 j) (bρ8 j) t

/-- 表 7 的区间非退化（逐行 `norm_num`）。 -/
lemma aρ8_lt_bρ8 : ∀ j ∈ Finset.Icc 1 16, aρ8 j < bρ8 j := by
  intro j hj
  fin_cases hj <;> simp [aρ8, bρ8, table7] <;> norm_num

lemma cρ8_pos : ∀ j ∈ Finset.Icc 1 16, 0 < cρ8 j := by
  intro j hj
  fin_cases hj <;> simp [cρ8, table7] <;> norm_num

/-- 嵌套性：aρ8 1 是最小左端点之外的参照点（表 7 的 a 降序、b 升序，逐行验证）。 -/
lemma aρ8_one_le_bρ8 : ∀ j ∈ Finset.Icc 1 16, aρ8 1 ≤ bρ8 j := by
  intro j hj
  fin_cases hj <;> simp [aρ8, bρ8, table7] <;> norm_num

lemma aρ8_le_bρ8_one : ∀ j ∈ Finset.Icc 1 16, aρ8 j ≤ bρ8 1 := by
  intro j hj
  fin_cases hj <;> simp [aρ8, bρ8, table7] <;> norm_num

lemma aρ8_le_aρ8_one : ∀ j ∈ Finset.Icc 1 16, aρ8 j ≤ aρ8 1 := by
  intro j hj
  fin_cases hj <;> simp [aρ8, table7] <;> norm_num

lemma bρ8_one_le_bρ8 : ∀ j ∈ Finset.Icc 1 16, bρ8 1 ≤ bρ8 j := by
  intro j hj
  fin_cases hj <;> simp [bρ8, table7] <;> norm_num

/-- `Uρ8` 在 `(-∞, aρ8 1]` 上单调不增。 -/
lemma Uρ8_antitoneOn : AntitoneOn Uρ8 (Iic (aρ8 1)) := by
  intro x hx y hy hxy
  unfold Uρ8
  refine Finset.sum_le_sum fun j hj => ?_
  refine mul_le_mul_of_nonneg_left ?_ (cρ8_pos j hj).le
  exact Apery.Uω_antitoneOn_Iic' (aρ8_lt_bρ8 j hj)
    (show x ∈ Iic (bρ8 j) from (show x ≤ aρ8 1 from hx).trans (aρ8_one_le_bρ8 j hj))
    (show y ∈ Iic (bρ8 j) from (show y ≤ aρ8 1 from hy).trans (aρ8_one_le_bρ8 j hj)) hxy

/-- `Uρ8` 在 `[bρ8 1, ∞)` 上单调不减。 -/
lemma Uρ8_monotoneOn : MonotoneOn Uρ8 (Ici (bρ8 1)) := by
  intro x hx y hy hxy
  unfold Uρ8
  refine Finset.sum_le_sum fun j hj => ?_
  refine mul_le_mul_of_nonneg_left ?_ (cρ8_pos j hj).le
  exact Apery.Uω_monotoneOn_Ici' (aρ8_lt_bρ8 j hj)
    (show x ∈ Ici (aρ8 j) from (aρ8_le_bρ8_one j hj).trans hx)
    (show y ∈ Ici (aρ8 j) from (aρ8_le_bρ8_one j hj).trans hy) hxy

/-- `Uρ8` 在 `[aρ8 1, bρ8 1]` 上为常值 `∑ cⱼ log((bⱼ − aⱼ)/4)`（恒等式 (A.1) 类比）。 -/
lemma Uρ8_of_mem {t : ℝ} (h1 : aρ8 1 ≤ t) (h2 : t ≤ bρ8 1) :
    Uρ8 t = ∑ j ∈ Icc 1 16, cρ8 j * Real.log ((bρ8 j - aρ8 j) / 4) := by
  simp only [Uρ8, sum_mul]
  apply Finset.sum_congr rfl
  intro j hj
  rw [Uω_of_mem ((aρ8_le_aρ8_one j hj).trans h1) (h2.trans (bρ8_one_le_bρ8 j hj))]

end Zeta7
