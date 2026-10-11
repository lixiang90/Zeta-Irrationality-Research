/-
SPDX-License-Identifier: Apache-2.0
Derived from Li2NegHalf by Qian Tang (GitHub: dtq1997), file `Li2/MomentFunctional.lean`.
Modified for Li2Rational by Si-Qi Liu.
-/

import Li2Rational.Family
import Li2.MomentFunctional

open Polynomial Li2
open scoped BigOperators
namespace Li2Rational.Family
noncomputable section
variable [Parameter]

class Admissible : Prop where
  norm_lt_one : ‖(Parameter.value : ℝ)‖ < 1
  ne_zero : Parameter.value ≠ 0

variable [Admissible]

abbrev li2Value : ℝ := li2 (Parameter.value : ℝ)

theorem summable_li2Value :
    Summable (fun k : ℕ => (Parameter.value : ℝ)^(k+1)/((k : ℝ)+1)^2) := by
  apply summable_abs_iff.mp
  apply Summable.of_nonneg_of_le (fun _ => abs_nonneg _)
    (fun k => ?_) ((summable_geometric_of_lt_one (abs_nonneg (Parameter.value : ℝ))
      (by simpa only [Real.norm_eq_abs] using Admissible.norm_lt_one)).mul_right
        |(Parameter.value : ℝ)|)
  rw [← pow_succ, abs_div, abs_pow, abs_of_nonneg (by positivity : (0 : ℝ) ≤ ((k : ℝ)+1)^2)]
  apply div_le_self (by positivity)
  have hk : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  nlinarith

lemma moment_series (k : ℕ) :
    (parameterMoment Parameter.value k : ℝ) =
      ∑' m : ℕ, (Parameter.value : ℝ)^(m+1)*((m : ℝ)+1)^k :=
  parameterMoment_cast_eq_series Parameter.value Admissible.norm_lt_one k

lemma summable_positiveRealMoment (k : ℕ) :
    Summable (fun m : ℕ => (Parameter.value : ℝ)^(m+1)*((m:ℝ)+1)^k) := by
  simpa [parameterRealMoment] using
    summable_parameterRealMoment (Parameter.value : ℝ) Admissible.norm_lt_one k

omit [Admissible] in
lemma U_eq_sum (f : ℚ[X]) :
    U f = f.sum (fun k a => a*((k:ℚ)+1)*parameterMoment Parameter.value k) := by
  induction f using Polynomial.induction_on' with
  | add f g hf hg =>
    rw [U_add, hf, hg, Polynomial.sum_add_index]
    · intro k
      simp
    · intro k a b
      ring
  | monomial k a =>
    simp [U, parameterU, X_mul_monomial, derivative_monomial_succ,
      parameterG_monomial, Polynomial.sum_monomial_index]

omit [Admissible] in
lemma polynomialIntegrand_term (f : ℚ[X]) (m : ℕ) :
    (Parameter.value : ℝ)^(m+1) * polynomialIntegrand f ((m:ℝ)+1) =
      ∑ k ∈ f.support, ((f.coeff k:ℝ)*((k:ℝ)+1)) *
        ((Parameter.value : ℝ)^(m+1) * ((m:ℝ)+1)^k) := by
  unfold polynomialIntegrand Polynomial.sum
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k _
  ring

theorem summable_polynomialIntegrand (f : ℚ[X]) :
    Summable (fun m : ℕ => (Parameter.value : ℝ)^(m+1) * polynomialIntegrand f ((m:ℝ)+1)) := by
  simp_rw [polynomialIntegrand_term]
  apply summable_sum
  intro k _
  exact (summable_positiveRealMoment k).mul_left _

theorem U_real_series (f : ℚ[X]) : (U f:ℝ) =
    ∑' m : ℕ, (Parameter.value : ℝ)^(m+1) * polynomialIntegrand f ((m:ℝ)+1) := by
  simp_rw [polynomialIntegrand_term]
  rw [Summable.tsum_finsetSum]
  · simp_rw [tsum_mul_left]
    rw [U_eq_sum]
    unfold Polynomial.sum
    push_cast
    simp_rw [moment_series]
  · intro k _
    exact (summable_positiveRealMoment k).mul_left _

end
end Li2Rational.Family
