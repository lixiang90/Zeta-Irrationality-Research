import Li2Rational.ProfileCriterion
import Li2Rational.RateBounds

open Li2
namespace Li2Rational
noncomputable section
variable [Comparison.Geometry] [Comparison.BaseValid]

theorem irrational_integer_ratio (P : Comparison.Profile) {B : ℝ}
    (hrate : 12*Real.log 2+4+4*(P.mean-Comparison.comparisonEnergy) < B)
    (a b : ℤ) (ha : a ≠ 0) (hb : b ≠ 0)
    (hsmall : |(a:ℝ)/b| ≤ 1/(Comparison.comparisonBase:ℝ))
    (hmargin : B+Real.log (|(a:ℝ)/b| *(Comparison.comparisonBase:ℝ)) <
      (8/3)*Real.log (b.natAbs:ℝ)-(9/4)*Real.log ((b-a).natAbs:ℝ)-
        6*Real.log (a.natAbs:ℝ)+72/25) : Irrational (li2 ((a:ℝ)/b)) := by
  letI : Family.Parameter := ⟨(a:ℚ)/b⟩
  have hz : (Family.Parameter.value:ℝ)=(a:ℝ)/b := by
    change (((a:ℚ)/b:ℚ):ℝ)=_
    push_cast
    rfl
  have hb2 : (2:ℝ) ≤ Comparison.comparisonBase := by exact_mod_cast Comparison.Geometry.base_ge_two
  have hsmall' : |(a:ℝ)/b| < 1 := (hsmall.trans
    (one_div_le_one_div_of_le (by norm_num) hb2)).trans_lt (by norm_num)
  letI : Family.Nondegenerate := {
    ne_zero := by change (a:ℚ)/b ≠ 0; exact div_ne_zero (by exact_mod_cast ha) (by exact_mod_cast hb)
    ne_one := by
      intro h
      have he : (a:ℝ)/b=1 := by rw [← hz,h]; norm_num
      rw [he,abs_one] at hsmall'
      exact lt_irrefl _ hsmall' }
  letI : Family.Admissible := {
    norm_lt_one := by rw [Real.norm_eq_abs,hz]; exact hsmall'
    ne_zero := Family.Nondegenerate.ne_zero }
  have hi := Family.irrational_of_profile_rate P hrate a b hb rfl
    (by rw [hz]; exact hsmall) (by rw [hz]; exact hmargin)
  simpa only [Family.li2Value,hz] using hi

omit [Comparison.BaseValid] in
lemma log_profile_ratio (p q : ℝ) (hp : 0 < p) (hq : 0 < q) :
    Real.log ((p/q)*(Comparison.comparisonBase:ℝ)) =
      Real.log (Comparison.comparisonBase:ℝ)-Real.log (q/p) := by
  have hb : (0:ℝ) < Comparison.comparisonBase := by exact_mod_cast Comparison.comparisonBase_pos
  rw [Real.log_mul (div_ne_zero hp.ne' hq.ne') hb.ne',Real.log_div hp.ne' hq.ne',
    Real.log_div hq.ne' hp.ne']
  ring

theorem irrational_positive_profile (P : Comparison.Profile) {B : ℝ}
    (hrate : 12*Real.log 2+4+4*(P.mean-Comparison.comparisonEnergy) < B)
    (p q : ℕ) (hp : 0 < p) (hq : 0 < q)
    (hsmall : (Comparison.comparisonBase:ℝ)*(p:ℝ) ≤ (q:ℝ))
    (hmargin : B+Real.log (Comparison.comparisonBase:ℝ)-Real.log ((q:ℝ)/(p:ℝ)) <
      arithmeticRatePositive p q) : Irrational (li2 ((p:ℝ)/q)) := by
  have hpR : (0:ℝ) < p := by exact_mod_cast hp
  have hqR : (0:ℝ) < q := by exact_mod_cast hq
  have hb2 : (2:ℝ) ≤ Comparison.comparisonBase := by exact_mod_cast Comparison.Geometry.base_ge_two
  have hbR : (0:ℝ) < Comparison.comparisonBase := by linarith
  have hpq : (p:ℝ) < q := by nlinarith
  apply irrational_integer_ratio P hrate (p:ℤ) (q:ℤ)
    (by exact_mod_cast hp.ne') (by exact_mod_cast hq.ne')
  · simp only [Int.cast_natCast,abs_of_pos (div_pos hpR hqR)]
    apply (div_le_div_iff₀ hqR hbR).mpr
    nlinarith
  · simpa only [Nat.cast_natAbs,Int.cast_abs,Int.cast_sub,Int.cast_natCast,
      abs_of_pos hpR,abs_of_pos hqR,abs_of_pos (sub_pos.mpr hpq),
      abs_of_pos (div_pos hpR hqR),log_profile_ratio (p:ℝ) q hpR hqR,arithmeticRatePositive,
      add_sub_assoc] using hmargin

theorem irrational_negative_profile (P : Comparison.Profile) {B : ℝ}
    (hrate : 12*Real.log 2+4+4*(P.mean-Comparison.comparisonEnergy) < B)
    (p q : ℕ) (hp : 0 < p) (hq : 0 < q)
    (hsmall : (Comparison.comparisonBase:ℝ)*(p:ℝ) ≤ (q:ℝ))
    (hmargin : B+Real.log (Comparison.comparisonBase:ℝ)-Real.log ((q:ℝ)/(p:ℝ)) <
      arithmeticRateNegative p q) : Irrational (li2 (-(p:ℝ)/q)) := by
  have hpR : (0:ℝ) < p := by exact_mod_cast hp
  have hqR : (0:ℝ) < q := by exact_mod_cast hq
  have hbR : (0:ℝ) < Comparison.comparisonBase := by exact_mod_cast Comparison.comparisonBase_pos
  have hi := irrational_integer_ratio P hrate (-(p:ℤ)) (q:ℤ)
    (neg_ne_zero.mpr (by exact_mod_cast hp.ne')) (by exact_mod_cast hq.ne')
  apply (by simpa only [Int.cast_neg,Int.cast_natCast] using hi)
  · simp only [neg_div,abs_neg,abs_of_pos (div_pos hpR hqR)]
    apply (div_le_div_iff₀ hqR hbR).mpr
    nlinarith
  · simpa only [Nat.cast_natAbs,Int.cast_abs,Int.cast_sub,Int.cast_add,Int.cast_natCast,Int.cast_neg,
      sub_neg_eq_add,neg_div,abs_neg,abs_of_pos hpR,abs_of_pos hqR,
      abs_of_pos (add_pos hqR hpR),abs_of_pos (div_pos hpR hqR),
      log_profile_ratio (p:ℝ) q hpR hqR,arithmeticRateNegative,add_sub_assoc] using hmargin

end
end Li2Rational
