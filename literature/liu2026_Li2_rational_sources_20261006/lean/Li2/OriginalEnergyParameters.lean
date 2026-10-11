/-
SPDX-License-Identifier: Apache-2.0
Derived from Li2NegHalf by Qian Tang (GitHub: dtq1997), file `Li2/OriginalEnergyParameters.lean`.
Modified for Li2Rational by Si-Qi Liu.
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Positivity

namespace Li2
noncomputable section

def originalEnergyU : ℝ := (9 + Real.sqrt 129) / 8
def originalEnergyA : ℝ := Real.sqrt (originalEnergyU ^ 2 - 1)
def originalEnergyV : ℝ := Real.sqrt (originalEnergyA ^ 2 + 16)
def originalEnergyS (x : ℝ) : ℝ := Real.sqrt (originalEnergyA ^ 2 - x ^ 2)
def originalEnergyRho (x : ℝ) : ℝ :=
  if |x| ≤ originalEnergyA then
    (3 * Real.log ((originalEnergyU + originalEnergyS x) / (originalEnergyU - originalEnergyS x)) -
      Real.log ((originalEnergyV + originalEnergyS x) / (originalEnergyV - originalEnergyS x))) /
      (8 * Real.pi)
  else 0

def originalEnergyRhoBound : ℝ :=
  3 * Real.log ((originalEnergyU + originalEnergyA) / (originalEnergyU - originalEnergyA)) / (8 * Real.pi)

lemma originalEnergy_one_lt_u : 1 < originalEnergyU := by
  unfold originalEnergyU
  have h := Real.sqrt_nonneg (129 : ℝ)
  linarith
lemma originalEnergy_u_pos : 0 < originalEnergyU := lt_trans zero_lt_one originalEnergy_one_lt_u
lemma originalEnergy_u_quadratic : 4 * originalEnergyU ^ 2 - 9 * originalEnergyU - 3 = 0 := by
  unfold originalEnergyU
  nlinarith [Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 129)]
lemma originalEnergy_a_radicand_pos : 0 < originalEnergyU ^ 2 - 1 := by
  nlinarith [originalEnergy_one_lt_u, sq_nonneg (originalEnergyU - 1)]
lemma originalEnergy_a_nonneg : 0 ≤ originalEnergyA := Real.sqrt_nonneg _
lemma originalEnergy_a_pos : 0 < originalEnergyA := by
  unfold originalEnergyA
  exact Real.sqrt_pos.mpr originalEnergy_a_radicand_pos
lemma originalEnergy_a_sq : originalEnergyA ^ 2 = originalEnergyU ^ 2 - 1 := by
  unfold originalEnergyA
  exact Real.sq_sqrt originalEnergy_a_radicand_pos.le
lemma originalEnergy_a_lt_u : originalEnergyA < originalEnergyU := by
  apply (sq_lt_sq₀ originalEnergy_a_nonneg originalEnergy_u_pos.le).mp
  rw [originalEnergy_a_sq]
  linarith
lemma originalEnergy_v_pos : 0 < originalEnergyV := by
  unfold originalEnergyV
  apply Real.sqrt_pos.mpr
  positivity
lemma originalEnergy_v_sq : originalEnergyV ^ 2 = originalEnergyA ^ 2 + 16 := by
  unfold originalEnergyV
  apply Real.sq_sqrt
  positivity
lemma originalEnergy_v_eq : originalEnergyV = 3 * originalEnergyU - 3 := by
  apply (sq_eq_sq₀ originalEnergy_v_pos.le
    (show 0 ≤ 3 * originalEnergyU - 3 by linarith [originalEnergy_one_lt_u])).mp
  rw [originalEnergy_v_sq, originalEnergy_a_sq]
  nlinarith [originalEnergy_u_quadratic]
lemma originalEnergy_a_lt_v : originalEnergyA < originalEnergyV := by
  apply (sq_lt_sq₀ originalEnergy_a_nonneg originalEnergy_v_pos.le).mp
  rw [originalEnergy_v_sq]
  linarith
lemma originalEnergy_u_lt_v : originalEnergyU < originalEnergyV := by
  apply (sq_lt_sq₀ originalEnergy_u_pos.le originalEnergy_v_pos.le).mp
  rw [originalEnergy_v_sq, originalEnergy_a_sq]
  linarith
lemma originalEnergyS_nonneg (x : ℝ) : 0 ≤ originalEnergyS x := Real.sqrt_nonneg _
lemma originalEnergyS_le_a (x : ℝ) : originalEnergyS x ≤ originalEnergyA := by
  unfold originalEnergyS
  apply (Real.sqrt_le_left originalEnergy_a_nonneg).mpr
  nlinarith [sq_nonneg x]
lemma originalEnergy_u_sub_s_pos (x : ℝ) : 0 < originalEnergyU - originalEnergyS x := by
  have h := originalEnergyS_le_a x
  linarith [originalEnergy_a_lt_u]
lemma originalEnergy_v_sub_s_pos (x : ℝ) : 0 < originalEnergyV - originalEnergyS x := by
  have h := originalEnergyS_le_a x
  linarith [originalEnergy_a_lt_v]

private lemma originalEnergy_logRatio_nonneg {c s : ℝ} (hs : 0 ≤ s) (hsc : s < c) :
    0 ≤ Real.log ((c + s) / (c - s)) := by
  apply Real.log_nonneg
  apply (le_div_iff₀ (sub_pos.mpr hsc)).mpr
  linarith
private lemma originalEnergy_logRatio_le_of_parameter_le
    {c d s : ℝ} (hs : 0 ≤ s) (hsc : s < c) (hcd : c ≤ d) :
    Real.log ((d + s) / (d - s)) ≤ Real.log ((c + s) / (c - s)) := by
  have hds : 0 < d - s := by linarith
  have hcs : 0 < c - s := sub_pos.mpr hsc
  apply Real.log_le_log
  · exact div_pos (by linarith) hds
  · apply (div_le_div_iff₀ hds hcs).mpr
    nlinarith [mul_nonneg hs (sub_nonneg.mpr hcd)]
private lemma originalEnergy_logRatio_le_of_argument_le
    {c s t : ℝ} (hs : 0 ≤ s) (hst : s ≤ t) (htc : t < c) :
    Real.log ((c + s) / (c - s)) ≤ Real.log ((c + t) / (c - t)) := by
  have hcs : 0 < c - s := by linarith
  have hct : 0 < c - t := sub_pos.mpr htc
  have hc : 0 ≤ c := by linarith
  apply Real.log_le_log
  · exact div_pos (by linarith) hcs
  · apply (div_le_div_iff₀ hcs hct).mpr
    nlinarith [mul_nonneg hc (sub_nonneg.mpr hst)]

lemma originalEnergyRhoBound_nonneg : 0 ≤ originalEnergyRhoBound := by
  unfold originalEnergyRhoBound
  apply div_nonneg
  · exact mul_nonneg (by norm_num)
      (originalEnergy_logRatio_nonneg originalEnergy_a_nonneg originalEnergy_a_lt_u)
  · positivity
lemma originalEnergyRho_bounds (x : ℝ) :
    0 ≤ originalEnergyRho x ∧ originalEnergyRho x ≤ originalEnergyRhoBound := by
  have hs := originalEnergyS_nonneg x
  have hsa := originalEnergyS_le_a x
  have hsu : originalEnergyS x < originalEnergyU := lt_of_le_of_lt hsa originalEnergy_a_lt_u
  have hsv : originalEnergyS x < originalEnergyV := lt_trans hsu originalEnergy_u_lt_v
  have hlu := originalEnergy_logRatio_nonneg hs hsu
  have hlv := originalEnergy_logRatio_nonneg hs hsv
  have hvu := originalEnergy_logRatio_le_of_parameter_le hs hsu originalEnergy_u_lt_v.le
  have hmax := originalEnergy_logRatio_le_of_argument_le hs hsa originalEnergy_a_lt_u
  unfold originalEnergyRho
  split_ifs with hx
  · constructor
    · apply div_nonneg
      · linarith
      · positivity
    · unfold originalEnergyRhoBound
      apply div_le_div_of_nonneg_right
      · linarith
      · positivity
  · exact ⟨le_rfl, originalEnergyRhoBound_nonneg⟩
lemma originalEnergyRho_nonneg (x : ℝ) : 0 ≤ originalEnergyRho x := (originalEnergyRho_bounds x).1
lemma originalEnergyRho_le (x : ℝ) : originalEnergyRho x ≤ originalEnergyRhoBound := (originalEnergyRho_bounds x).2
lemma originalEnergyRho_eq_zero_of_outside {x : ℝ} (hx : originalEnergyA < |x|) :
    originalEnergyRho x = 0 := by
  simp only [originalEnergyRho, not_le.mpr hx, if_false]

end
end Li2
