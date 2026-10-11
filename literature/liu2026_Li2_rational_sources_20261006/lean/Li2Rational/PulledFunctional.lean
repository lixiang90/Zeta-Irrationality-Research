/-
SPDX-License-Identifier: Apache-2.0
Derived from Li2NegHalf by Qian Tang (GitHub: dtq1997), file `Li2/OriginalIntegralComparison.lean`.
Modified for Li2Rational by Si-Qi Liu.
-/

import Li2.OriginalIntegerTests
import Li2Rational.PrimeFieldPoleExtension
import Li2Rational.NumeratorDissection

open Polynomial Li2
open scoped BigOperators
namespace Li2Rational.Family
open Li2
noncomputable section
variable [Parameter] [Nondegenerate] [Admissible]
variable {p : ℕ} [hp : Fact p.Prime] [Ordinary p]

omit [Admissible] in
theorem original_pulled_polynomial_UV (hp4 : 3 < p) (m : ℕ) (F : ℚ[X])
    (a : Fin p) (Y : ℚ_[p]) :
    (fieldPrimePoleU hp4
      (rationalPolynomialSeries ((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ)))) 0).eval Y -
      (a.val:ℚ_[p])/(p:ℚ_[p])*(fieldPrimePoleV hp4
        (rationalPolynomialSeries ((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ)))) 0).eval Y =
    (parameterU (primeParameter p) ((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ))):ℚ_[p]) -
      (a.val:ℚ_[p])/(p:ℚ_[p])*
        (parameterV (primeParameter p) ((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ))):ℚ_[p]) := by
  change (fieldPrimePoleU hp4
      (((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ))).map (Rat.castHom ℚ_[p]) :
        PowerSeries ℚ_[p]) 0).eval Y - (a.val:ℚ_[p])/(p:ℚ_[p])*
      (fieldPrimePoleV hp4
        (((F /ₘ D m).comp (C (p:ℚ)*X-C (a.val:ℚ))).map (Rat.castHom ℚ_[p]) :
          PowerSeries ℚ_[p]) 0).eval Y = _
  rw [fieldPrimePoleU_polynomial, fieldPrimePoleV_polynomial]

omit [Admissible] in
theorem original_pulled_simplePole_UV (hp4 : 3 < p) (Y : ℚ_[p])
    (j a : ℕ) (hj : j ≤ 4*p-4) (ha : a < p) :
    pulledSimplePoleContribution Y j a =
      (fieldPrimePoleU hp4 (pulledPoleRegular j a) (pulledPoleResidue j a hj ha)).eval Y -
        (a:ℚ_[p])/(p:ℚ_[p])*
          (fieldPrimePoleV hp4 (pulledPoleRegular j a) (pulledPoleResidue j a hj ha)).eval Y := by
  unfold pulledSimplePoleContribution pulledPoleRegular pulledPoleResidue
  dsimp only
  by_cases hm : p ∣ j+(p-1-a)+1
  · simp only [dif_pos hm]
    rw [fieldPrimePoleU_single, fieldPrimePoleV_single]
    simp only [eval_mul, eval_C, eval_map]
    rw [primeUPole_eval₂, primeVPole_eval₂]
    dsimp only [primeMatchingPoleIndex]
    ring
  · simp only [dif_neg hm]
    rw [fieldPrimePoleU_regular, fieldPrimePoleV_regular, eval_C, eval_C,
      fieldRestrictedU_integral _ _ (padicReciprocalSeries_isRestricted _ _ _ _),
      fieldRestrictedV_integral _ _ (padicReciprocalSeries_isRestricted _ _ _ _)]

omit [Admissible] in
theorem numeratorPulledValue_field (hp4 : 3 < p) (Y : ℚ_[p])
    (m : ℕ) (hm : m ≤ 4*p-4) (F : ℚ[X]) (a : Fin p) :
    numeratorPulledValue Y m F a =
      (fieldPrimePoleU hp4 (originalPulledRegular m F a)
        (originalPulledResidue m hm F a)).eval Y - (a.val:ℚ_[p])/(p:ℚ_[p]) *
      (fieldPrimePoleV hp4 (originalPulledRegular m F a)
        (originalPulledResidue m hm F a)).eval Y := by
  have hu := original_fieldPoleFunctional
    (fun n : ℕ => ((n+1:ℕ):ℤ_[p])*integralParameterMoment (primeParameter p)
      (primeParameter_moment_integral) n)
    (fun j : Fin 4 => (primeUPole j.val (by omega)).map (algebraMap ℤ_[p] ℚ_[p]))
    m hm F a
  have hv := original_fieldPoleFunctional
    (derivativeMoments (integralParameterMoment (primeParameter p)
      (primeParameter_moment_integral)))
    (fun j : Fin 4 => (primeVPole j.val (by omega)).map (algebraMap ℤ_[p] ℚ_[p]))
    m hm F a
  change _ = (fieldPoleFunctional _ _ _ _).eval Y - _*(fieldPoleFunctional _ _ _ _).eval Y
  rw [hu, hv]
  simp only [eval_add, eval_finset_sum, eval_mul, eval_C]
  rw [mul_add, add_sub_add_comm]
  unfold numeratorPulledValue
  rw [← original_pulled_polynomial_UV hp4 m F a Y]
  congr 1
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_coe_sort]
  apply Finset.sum_congr rfl
  intro j _
  rw [original_pulled_simplePole_UV hp4 Y j.val a.val
    ((Finset.mem_Icc.mp j.property).2.trans hm) a.isLt]
  simp only [originalResidue, Rat.cast_div, fieldPrimePoleU, fieldPrimePoleV]
  ring

omit [Admissible] in
theorem numeratorPulledValue_integral_of_cleared (hp4 : 3 < p) (Y : ℚ_[p])
    (m : ℕ) (hm : m ≤ 4*p-4) (F : ℚ[X]) (a : Fin p) (c : ℚ_[p])
    (g : PowerSeries ℤ_[p]) (hg : PowerSeries.IsRestricted 1 g) (r : Fin 4 → ℤ_[p])
    (he : primeDiscPolynomialSeries a.val m *
      PowerSeries.map (algebraMap ℤ_[p] ℚ_[p]) (integralPoleNumerator (primePoleCenters p) g r) =
      PowerSeries.C c * (fieldPoleDenominator (primePoleCenters p) : PowerSeries ℚ_[p]) *
        rationalPolynomialSeries (F.comp (C (p:ℚ)*X-C (a.val:ℚ)))) :
    c * numeratorPulledValue Y m F a =
      (primePoleU hp4 g r).eval₂ (algebraMap ℤ_[p] ℚ_[p]) Y - (a.val:ℚ_[p])/(p:ℚ_[p]) *
        (primePoleV hp4 g r).eval₂ (algebraMap ℤ_[p] ℚ_[p]) Y := by
  obtain ⟨hgEq,hrEq⟩ := originalPulled_eq_integral_of_cleared m hm F a c g hg r he
  have hu : C c * fieldPrimePoleU hp4 (originalPulledRegular m F a)
      (originalPulledResidue m hm F a) =
      (primePoleU hp4 g r).map (algebraMap ℤ_[p] ℚ_[p]) := by
    change C c * fieldPoleFunctional _ _ _ _ = _
    rw [← fieldPoleFunctional_smul _ _ _ (originalPulledRegular_isRestricted m F a) _ c,
      hgEq, hrEq]
    exact fieldPrimePoleU_integral hp4 g hg r
  have hv : C c * fieldPrimePoleV hp4 (originalPulledRegular m F a)
      (originalPulledResidue m hm F a) =
      (primePoleV hp4 g r).map (algebraMap ℤ_[p] ℚ_[p]) := by
    change C c * fieldPoleFunctional _ _ _ _ = _
    rw [← fieldPoleFunctional_smul _ _ _ (originalPulledRegular_isRestricted m F a) _ c,
      hgEq, hrEq]
    exact fieldPrimePoleV_integral hp4 g hg r
  have hu' := congrArg (fun P : (ℚ_[p])[X] => P.eval Y) hu
  have hv' := congrArg (fun P : (ℚ_[p])[X] => P.eval Y) hv
  simp only [eval_mul, eval_C, eval_map] at hu' hv'
  rw [numeratorPulledValue_field hp4 Y m hm F a, mul_sub, hu']
  rw [← hv']
  ring

omit [Admissible] in
theorem numeratorPulledValue_integer_test (hp4 : 3 < p) (Y : ℚ_[p])
    (m : ℕ) (hm : m ≤ 4*p-4) (F : ℚ[X]) (a : Fin p) (c : ℚ_[p])
    (g : PowerSeries ℤ_[p]) (hg : PowerSeries.IsRestricted 1 g) (r : Fin 4 → ℤ_[p])
    (he : primeDiscPolynomialSeries a.val m *
      PowerSeries.map (algebraMap ℤ_[p] ℚ_[p]) (integralPoleNumerator (primePoleCenters p) g r) =
      PowerSeries.C c * (fieldPoleDenominator (primePoleCenters p) : PowerSeries ℚ_[p]) *
        rationalPolynomialSeries (F.comp (C (p:ℚ)*X-C (a.val:ℚ)))) (T : ℤ[X]) :
    let gT := integralPoleMulRegular (primePoleCenters p)
      (integralDiscTestPolynomial T a : PowerSeries ℤ_[p]) g r
    let rT := integralPoleMulResidue (primePoleCenters p)
      (integralDiscTestPolynomial T a : PowerSeries ℤ_[p]) r
    c * numeratorPulledValue
      Y m (F*T.map (Int.castRingHom ℚ)) a =
      (primePoleU hp4 gT rT).eval₂ (algebraMap ℤ_[p] ℚ_[p]) Y - (a.val:ℚ_[p])/(p:ℚ_[p]) *
        (primePoleV hp4 gT rT).eval₂ (algebraMap ℤ_[p] ℚ_[p]) Y := by
  apply numeratorPulledValue_integral_of_cleared hp4 Y m hm
  · exact integralPoleMulRegular_isRestricted _ _ _ (polynomial_isRestricted _) hg _
  · exact original_test_integral_cleared m F a c g r he T

end
end Li2Rational.Family
