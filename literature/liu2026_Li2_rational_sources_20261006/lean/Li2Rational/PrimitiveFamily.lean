/-
SPDX-License-Identifier: Apache-2.0
Derived from Li2NegHalf by Qian Tang (GitHub: dtq1997), file
`Li2/PrimitiveBinomialNormalization.lean`.
Modified for Li2Rational by Si-Qi Liu.
-/

import Li2Rational.Family
import Li2.PrimitivePrimeLog

open Polynomial Li2
open scoped BigOperators
namespace Li2Rational.Family
noncomputable section
variable [Parameter]
def primitiveQ (n : ℕ) : ℤ[X] :=
  if Q n = 0 then 0 else
    (IsLocalization.integerNormalization (nonZeroDivisors ℤ) (Q n)).primPart

theorem primitiveQ_isPrimitive (n : ℕ) (hn : Q n ≠ 0) :
    (primitiveQ n).IsPrimitive := by
  simp only [primitiveQ, if_neg hn]
  exact Polynomial.isPrimitive_primPart _

theorem primitiveQ_natDegree_le (n : ℕ) : (primitiveQ n).natDegree ≤ 2*n := by
  unfold primitiveQ
  split_ifs with hn
  · simp
  rw [Polynomial.natDegree_primPart]
  apply le_trans _ (Q_natDegree_le n)
  apply Polynomial.natDegree_le_iff_coeff_eq_zero.mpr
  intro k hk
  apply Polynomial.notMem_support_iff.mp
  intro h
  have hs := IsLocalization.integerNormalization_support (nonZeroDivisors ℤ) (Q n)
  exact (Polynomial.notMem_support_iff.mpr (Polynomial.coeff_eq_zero_of_natDegree_lt hk)) (hs h)

theorem primitiveQ_proportional (n : ℕ) :
    ∃ a : ℚ, a ≠ 0 ∧ (primitiveQ n).map (algebraMap ℤ ℚ) = C a * Q n := by
  by_cases hn : Q n = 0
  · exact ⟨1, one_ne_zero, by simp [primitiveQ, hn]⟩
  let R := IsLocalization.integerNormalization (nonZeroDivisors ℤ) (Q n)
  have hR : R ≠ 0 := fun hz => hn (IsFractionRing.integerNormalization_eq_zero_iff.mp hz)
  have hcont : R.content ≠ 0 := fun hz => hR (Polynomial.content_eq_zero_iff.mp hz)
  have hcontQ : (R.content : ℚ) ≠ 0 := by exact_mod_cast hcont
  obtain ⟨b, hb, hmap⟩ := IsLocalization.integerNormalization_spec (nonZeroDivisors ℤ) (Q n)
  have hb0 : b ≠ 0 := nonZeroDivisors.ne_zero hb
  have hbQ : (b : ℚ) ≠ 0 := by exact_mod_cast hb0
  refine ⟨(b : ℚ)/(R.content : ℚ), div_ne_zero hbQ hcontQ, ?_⟩
  apply Polynomial.ext
  intro k
  have hfac := congrArg (fun f : ℤ[X] => (f.map (algebraMap ℤ ℚ)).coeff k)
    R.eq_C_content_mul_primPart
  have hco : (b : ℚ) * (Q n).coeff k = (R.content : ℚ) * (R.primPart.coeff k : ℚ) := by
    dsimp only at hfac
    rw [show R.map (algebraMap ℤ ℚ) = b • Q n from hmap] at hfac
    simpa using hfac
  simp only [primitiveQ, if_neg hn, coeff_map, coeff_C_mul]
  change (R.primPart.coeff k : ℚ) = (b : ℚ)/(R.content : ℚ) * (Q n).coeff k
  apply (mul_left_cancel₀ hcontQ)
  field_simp
  nlinarith [hco]

def primitiveScale (n : ℕ) : ℚ := (primitiveQ_proportional n).choose

lemma primitiveScale_ne_zero (n : ℕ) : primitiveScale n ≠ 0 :=
  (primitiveQ_proportional n).choose_spec.1

lemma primitiveScale_spec (n : ℕ) :
    (primitiveQ n).map (algebraMap ℤ ℚ) = C (primitiveScale n) * Q n :=
  (primitiveQ_proportional n).choose_spec.2

def P (n : ℕ) : ℤ[X] :=
  if 0 < primitiveScale n then primitiveQ n else -primitiveQ n

def d (n : ℕ) : ℚ := |primitiveScale n|

theorem d_pos (n : ℕ) : 0 < d n := abs_pos.mpr (primitiveScale_ne_zero n)

theorem P_eq_d_Q (n : ℕ) : (P n).map (algebraMap ℤ ℚ) = C (d n) * Q n := by
  by_cases h : 0 < primitiveScale n
  · simpa only [P, if_pos h, d, abs_of_pos h] using primitiveScale_spec n
  · have hneg : primitiveScale n < 0 :=
      lt_of_le_of_ne (le_of_not_gt h) (primitiveScale_ne_zero n)
    simp only [P, if_neg h, Polynomial.map_neg, primitiveScale_spec,
      d, abs_of_neg hneg, map_neg, neg_mul]

theorem P_natDegree_le (n : ℕ) : (P n).natDegree ≤ 2*n := by
  unfold P
  split_ifs <;> simpa using primitiveQ_natDegree_le n

theorem P_isPrimitive (n : ℕ) (hn : Q n ≠ 0) : (P n).IsPrimitive := by
  unfold P
  split_ifs
  · exact primitiveQ_isPrimitive n hn
  · apply Polynomial.isPrimitive_iff_isUnit_of_C_dvd.mpr
    intro r hr
    apply Polynomial.isPrimitive_iff_isUnit_of_C_dvd.mp (primitiveQ_isPrimitive n hn) r
    simpa using hr

def dtilde (n : ℕ) : ℚ := d n / (Sn n ^ (2*n) / Fn n)

lemma dtilde_pos (n : ℕ) : 0 < dtilde n :=
  div_pos (d_pos n) (Qtilde_scale_pos n)

lemma dtilde_ne_zero (n : ℕ) : dtilde n ≠ 0 := (dtilde_pos n).ne'

theorem P_eq_dtilde_Qtilde (n : ℕ) :
    (P n).map (algebraMap ℤ ℚ) = C (dtilde n) * Qtilde n := by
  calc
    (P n).map (algebraMap ℤ ℚ) = C (d n) * Q n := P_eq_d_Q n
    _ = C (dtilde n) * Qtilde n := by
      rw [Qtilde, ← mul_assoc, ← C_mul, dtilde,
        div_mul_cancel₀ _ (Qtilde_scale_pos n).ne']

lemma P_eq_zero_of_Q_eq_zero (n : ℕ) (hn : Q n = 0) : P n = 0 := by
  simp [P, primitiveQ, hn]

lemma P_eq_zero_iff_Q_eq_zero (n : ℕ) : P n = 0 ↔ Q n = 0 := by
  constructor
  · intro hP
    have h := P_eq_d_Q n
    rw [hP, Polynomial.map_zero] at h
    have hd : (C (d n) : ℚ[X]) ≠ 0 := by
      exact Polynomial.C_ne_zero.mpr (d_pos n).ne'
    exact (mul_eq_zero.mp h.symm).resolve_left hd
  · exact P_eq_zero_of_Q_eq_zero n

lemma Qtilde_eq_zero_iff_Q_eq_zero (n : ℕ) : Qtilde n = 0 ↔ Q n = 0 := by
  rw [Qtilde, mul_eq_zero, C_eq_zero]
  simp [(Qtilde_scale_pos n).ne']

lemma P_eq_zero_iff_Qtilde_eq_zero (n : ℕ) : P n = 0 ↔ Qtilde n = 0 :=
  (P_eq_zero_iff_Q_eq_zero n).trans (Qtilde_eq_zero_iff_Q_eq_zero n).symm

lemma P_isPrimitive_of_Qtilde_ne_zero (n : ℕ) (hn : Qtilde n ≠ 0) :
    (P n).IsPrimitive :=
  P_isPrimitive n ((Qtilde_ne_zero_iff n).mp hn)

theorem P_aeval_eq_dtilde_Qtilde (n : ℕ) (x : ℝ) :
    aeval x (P n) = (dtilde n : ℝ) * aeval x (Qtilde n) := by
  have h := congrArg (fun F : ℚ[X] => F.eval₂ (algebraMap ℚ ℝ) x)
    (P_eq_dtilde_Qtilde n)
  dsimp only at h
  rw [eval₂_map, eval₂_mul, eval₂_C] at h
  simpa only [aeval_def, ← IsScalarTower.algebraMap_eq ℤ ℚ ℝ] using h

lemma abs_P_aeval_eq_dtilde_Qtilde (n : ℕ) (x : ℝ) :
    |aeval x (P n)| = (dtilde n : ℝ) * |aeval x (Qtilde n)| := by
  rw [P_aeval_eq_dtilde_Qtilde, abs_mul,
    abs_of_pos (show (0:ℝ) < (dtilde n : ℝ) by exact_mod_cast dtilde_pos n)]

theorem Qtilde_coeff_valuation_minimum (p : ℕ) [Fact p.Prime] {n : ℕ}
    (hn : Qtilde n ≠ 0) :
    ∃ k, (Qtilde n).coeff k ≠ 0 ∧
      padicValRat p ((Qtilde n).coeff k) = -padicValRat p (dtilde n) ∧
      ∀ j, (Qtilde n).coeff j ≠ 0 →
        padicValRat p ((Qtilde n).coeff k) ≤ padicValRat p ((Qtilde n).coeff j) :=
  primitive_scale_coeff_valuation_minimum p (P n) (P_isPrimitive_of_Qtilde_ne_zero n hn)
    (Qtilde n) (dtilde n) (dtilde_ne_zero n) (P_eq_dtilde_Qtilde n)

theorem dtilde_padicVal_le_neg_GV (p : ℕ) [Fact p.Prime] {n : ℕ}
    (hn : Qtilde n ≠ 0) {r : ℚ} (hbound : GV p (Qtilde n) r) :
    (padicValRat p (dtilde n) : ℚ) ≤ -r := by
  obtain ⟨k, hk, hval, _⟩ := Qtilde_coeff_valuation_minimum p hn
  have h := (hbound k).resolve_left hk
  rw [hval, Int.cast_neg] at h
  linarith

end
end Li2Rational.Family
