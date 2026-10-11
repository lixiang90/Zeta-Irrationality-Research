import Mathlib
import Zeta7.HermiteIBP
import Zeta7.HermiteIntegrals
import Zeta7.Zeta7Def
import Zeta7.Construction

/-!
# Hermite's formula at `s = 7` for integer arguments

`∫₀^∞ w(y) / (y² + j²) dy = j⁶ (ζ(7) - H_j^{(7)}) - 1/6 + 1/(2j)` for `j ≥ 1`,
i.e. the pole moments (2.3) of the paper (Proposition 2.2).
-/

open Filter Topology Set MeasureTheory Finset

namespace Zeta7

/-- `∫₀^∞ y/(y² + a²)² dy = 1/(2a²)`. -/
lemma integral_y_div_sq_sq {a : ℝ} (ha : 0 < a) :
    ∫ y in Ioi 0, y / (y ^ 2 + a ^ 2) ^ 2 = 1 / (2 * a ^ 2) := by
  have hd : ∀ y : ℝ, HasDerivAt (fun y : ℝ => -1 / (2 * (y ^ 2 + a ^ 2))) (y / (y ^ 2 + a ^ 2) ^ 2) y := by
    intro y
    have hne : 2 * (y ^ 2 + a ^ 2) ≠ 0 := by positivity
    have := (hasDerivAt_const y (-1 : ℝ)).div (((hasDerivAt_pow 2 y).add_const (a ^ 2)).const_mul 2) hne
    refine this.congr_deriv ?_
    field_simp
    ring
  have hint : IntegrableOn (fun y : ℝ => y / (y ^ 2 + a ^ 2) ^ 2) (Ioi 0) := by
    refine integrableOn_of_le_inv_sq ha (C := 1 / (2 * a)) ((by fun_prop : Continuous fun y : ℝ => y).div
      (by fun_prop) (fun y => by positivity)).aestronglyMeasurable (fun y hy => ?_)
    rw [abs_of_nonneg (by positivity)]
    have h2 : y / (y ^ 2 + a ^ 2) ≤ 1 / (2 * a) := by
      rw [div_le_div_iff₀ (by positivity) (by positivity)]; nlinarith [sq_nonneg (y - a)]
    calc y / (y ^ 2 + a ^ 2) ^ 2 = (y / (y ^ 2 + a ^ 2)) * (1 / (y ^ 2 + a ^ 2)) := by
          field_simp
      _ ≤ (1 / (2 * a)) * (1 / (y ^ 2 + a ^ 2)) := by gcongr
      _ = 1 / (2 * a) / (y ^ 2 + a ^ 2) := by ring
  have hlim : Tendsto (fun y : ℝ => -1 / (2 * (y ^ 2 + a ^ 2))) atTop (𝓝 0) := by
    refine tendsto_const_nhds.div_atTop ?_
    exact ((tendsto_pow_atTop two_ne_zero).atTop_add tendsto_const_nhds).const_mul_atTop two_pos
  have := integral_Ioi_of_hasDerivAt_of_tendsto' (a := 0) (fun y _ => hd y) hint hlim
  rw [this]
  field_simp
  ring

/-- `∫₀^∞ y/(y² + a²)³ dy = 1/(4a⁴)`. -/
lemma integral_y_div_sq_cube {a : ℝ} (ha : 0 < a) :
    ∫ y in Ioi 0, y / (y ^ 2 + a ^ 2) ^ 3 = 1 / (4 * a ^ 4) := by
  have hd : ∀ y : ℝ, HasDerivAt (fun y : ℝ => -1 / (4 * (y ^ 2 + a ^ 2) ^ 2)) (y / (y ^ 2 + a ^ 2) ^ 3) y := by
    intro y
    have hne : 4 * (y ^ 2 + a ^ 2) ^ 2 ≠ 0 := by positivity
    have := (hasDerivAt_const y (-1 : ℝ)).div
      ((((hasDerivAt_pow 2 y).add_const (a ^ 2)).pow 2).const_mul 4) hne
    refine this.congr_deriv ?_
    simp only [Pi.div_apply, Pi.mul_apply, Pi.pow_apply]
    field_simp
    ring
  have hint : IntegrableOn (fun y : ℝ => y / (y ^ 2 + a ^ 2) ^ 3) (Ioi 0) := by
    refine integrableOn_of_le_inv_sq ha (C := 1 / (2 * a ^ 3)) ((by fun_prop : Continuous fun y : ℝ => y).div
      (by fun_prop) (fun y => by positivity)).aestronglyMeasurable (fun y hy => ?_)
    rw [abs_of_nonneg (by positivity)]
    have h2 : y / (y ^ 2 + a ^ 2) ≤ 1 / (2 * a) := by
      rw [div_le_div_iff₀ (by positivity) (by positivity)]; nlinarith [sq_nonneg (y - a)]
    have h3 : a ^ 2 * (y ^ 2 + a ^ 2) ≤ (y ^ 2 + a ^ 2) ^ 2 := by
      nlinarith [sq_nonneg y, sq_nonneg a, mul_nonneg (sq_nonneg y) (sq_nonneg a)]
    calc y / (y ^ 2 + a ^ 2) ^ 3 = (y / (y ^ 2 + a ^ 2)) * (1 / (y ^ 2 + a ^ 2) ^ 2) := by
          field_simp
      _ ≤ (1 / (2 * a)) * (1 / (y ^ 2 + a ^ 2) ^ 2) := by gcongr
      _ = 1 / (2 * a) / ((y ^ 2 + a ^ 2) ^ 2) := by ring
      _ ≤ 1 / (2 * a) / (a ^ 2 * (y ^ 2 + a ^ 2)) := by
          exact div_le_div_of_nonneg_left (by positivity) (by positivity) h3
      _ = 1 / (2 * a ^ 3) / (y ^ 2 + a ^ 2) := by
          have hane : a ≠ 0 := ha.ne'
          have hy2 : y ^ 2 + a ^ 2 ≠ 0 := by positivity
          field_simp
  have hlim : Tendsto (fun y : ℝ => -1 / (4 * (y ^ 2 + a ^ 2) ^ 2)) atTop (𝓝 0) := by
    refine tendsto_const_nhds.div_atTop ?_
    exact ((tendsto_pow_atTop two_ne_zero).comp
      ((tendsto_pow_atTop two_ne_zero).atTop_add tendsto_const_nhds)).const_mul_atTop four_pos
  have := integral_Ioi_of_hasDerivAt_of_tendsto' (a := 0) (fun y _ => hd y) hint hlim
  rw [this]
  field_simp
  ring

/-- `∫₀^∞ |k₆ a n| ≤ 16a / n²`. -/
lemma integral_abs_k6_le {a n : ℝ} (ha : 0 < a) (hn : 0 < n) :
    ∫ y in Ioi 0, |k6 a n y| ≤ 16 * a / n ^ 2 := by
  have hint1 : IntegrableOn (fun y => |k6 a n y|) (Ioi 0) := (integrableOn_k6 ha hn).abs
  have hbase : IntegrableOn (fun y : ℝ => y / (y ^ 2 + a ^ 2) ^ 3) (Ioi 0) := by
    refine integrableOn_of_le_inv_sq ha (C := 1 / (2 * a ^ 3)) ((by fun_prop : Continuous fun y : ℝ => y).div
      (by fun_prop) (fun y => by positivity)).aestronglyMeasurable (fun y hy => ?_)
    rw [abs_of_nonneg (by positivity)]
    have h2 : y / (y ^ 2 + a ^ 2) ≤ 1 / (2 * a) := by
      rw [div_le_div_iff₀ (by positivity) (by positivity)]; nlinarith [sq_nonneg (y - a)]
    have h3 : a ^ 2 * (y ^ 2 + a ^ 2) ≤ (y ^ 2 + a ^ 2) ^ 2 := by
      nlinarith [sq_nonneg y, sq_nonneg a, mul_nonneg (sq_nonneg y) (sq_nonneg a)]
    calc y / (y ^ 2 + a ^ 2) ^ 3 = (y / (y ^ 2 + a ^ 2)) * (1 / (y ^ 2 + a ^ 2) ^ 2) := by
          field_simp
      _ ≤ (1 / (2 * a)) * (1 / (y ^ 2 + a ^ 2) ^ 2) := by gcongr
      _ = 1 / (2 * a) / ((y ^ 2 + a ^ 2) ^ 2) := by ring
      _ ≤ 1 / (2 * a) / (a ^ 2 * (y ^ 2 + a ^ 2)) := by
          exact div_le_div_of_nonneg_left (by positivity) (by positivity) h3
      _ = 1 / (2 * a ^ 3) / (y ^ 2 + a ^ 2) := by
          have hane : a ≠ 0 := ha.ne'
          have hy2 : y ^ 2 + a ^ 2 ≠ 0 := by positivity
          field_simp
  have hint2 : IntegrableOn (fun y : ℝ => 64 * a ^ 5 / n ^ 2 * (y / (y ^ 2 + a ^ 2) ^ 3)) (Ioi 0) :=
    hbase.const_mul _
  calc ∫ y in Ioi 0, |k6 a n y| ≤ ∫ y in Ioi 0, 64 * a ^ 5 / n ^ 2 * (y / (y ^ 2 + a ^ 2) ^ 3) := by
        refine setIntegral_mono_on hint1 hint2 measurableSet_Ioi fun y hy => ?_
        have hy : 0 < y := hy
        unfold k6
        rw [abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ y / (y ^ 2 + n ^ 2))]
        have h1 := abs_g6_le ha hy.le
        have h2 : y / (y ^ 2 + n ^ 2) ≤ y / n ^ 2 := by
          gcongr; nlinarith [sq_nonneg y]
        calc |g6 a y| * (y / (y ^ 2 + n ^ 2)) ≤
            64 * a ^ 5 / (y ^ 2 + a ^ 2) ^ 3 * (y / n ^ 2) := by gcongr
          _ = 64 * a ^ 5 / n ^ 2 * (y / (y ^ 2 + a ^ 2) ^ 3) := by ring
    _ = 64 * a ^ 5 / n ^ 2 * (1 / (4 * a ^ 4)) := by rw [integral_const_mul, integral_y_div_sq_cube ha]
    _ = 16 * a / n ^ 2 := by field_simp; ring

/-- `∑_{n ≥ 0} 1/(n + j + 1)⁷ = ζ(7) - H_j^{(7)}`. -/
lemma tsum_tail_eq (j : ℕ) :
    ∑' n : ℕ, 1 / ((j : ℝ) + ((n : ℝ) + 1)) ^ 7 = zeta7 - (H7 j : ℝ) := by
  have hz : Summable (fun m : ℕ => 1 / (m : ℝ) ^ 7) := Real.summable_one_div_nat_pow.mpr (by norm_num)
  have h := hz.sum_add_tsum_nat_add (j + 1)
  have hH : ∑ i ∈ range (j + 1), 1 / ((i : ℝ)) ^ 7 = (H7 j : ℝ) := by
    rw [Finset.sum_range_succ']
    simp only [Nat.cast_zero, ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, div_zero, add_zero]
    unfold H7
    push_cast
    have e1 : Finset.Icc 1 j = Finset.Ico 1 (j + 1) := by
      ext x; simp only [Finset.mem_Icc, Finset.mem_Ico]; omega
    rw [e1, Finset.sum_Ico_eq_sum_range, show j + 1 - 1 = j by omega]
    refine Finset.sum_congr rfl fun i _ => ?_
    push_cast; ring_nf
  have htail : ∑' n : ℕ, 1 / ((j : ℝ) + ((n : ℝ) + 1)) ^ 7 = ∑' n : ℕ, 1 / ((n + (j + 1) : ℕ) : ℝ) ^ 7 := by
    refine tsum_congr fun n => ?_
    push_cast; ring_nf
  rw [htail, ← hH]
  unfold zeta7
  linarith

/-- **Hermite's formula at `s = 7`** (the pole moments (2.3) of the paper). -/
theorem hermite_pole (j : ℕ) (hj : 1 ≤ j) :
    ∫ y in Ioi 0, w y / (y ^ 2 + (j : ℝ) ^ 2) =
      (j : ℝ) ^ 6 * (zeta7 - (H7 j : ℝ)) - 1 / 6 + 1 / (2 * (j : ℝ)) := by
  set a : ℝ := (j : ℝ) with ha_def
  have ha : 0 < a := by rw [ha_def]; exact_mod_cast hj
  -- Step 1: `w / (y² + a²) = g₀ · F₆`
  have h1 : ∫ y in Ioi 0, w y / (y ^ 2 + a ^ 2) = ∫ y in Ioi 0, g0 a y * F6 y := by
    refine setIntegral_congr_fun measurableSet_Ioi fun y hy => ?_
    have hy : 0 < y := hy
    have hne : y ^ 2 + a ^ 2 ≠ 0 := by positivity
    rw [w_eq_F6 hy]; unfold g0; field_simp; try ring
  -- Step 2: integrate by parts six times
  rw [h1, integral_g0F6_eq ha]
  -- Step 3: the pointwise decomposition of `g₆ F₀`
  have hdec : ∀ y, 0 < y → g6 a y * F0 y =
      -(1 / 2) * g6 a y + 1 / (2 * Real.pi) * h6 a y +
        1 / Real.pi * ∑' n : ℕ, k6 a ((n : ℝ) + 1) y := by
    intro y hy
    rw [F0_series hy, ← g6_div_eq_h6 a hy.ne']
    simp only [k6]
    rw [tsum_mul_left]
    have hy' : y ≠ 0 := hy.ne'
    field_simp
    try ring
  -- Step 4: integrability of the pieces
  have hA : IntegrableOn (fun y => -(1 / 2) * g6 a y) (Ioi 0) := (integrableOn_g6 ha).const_mul _
  have hB : IntegrableOn (fun y => 1 / (2 * Real.pi) * h6 a y) (Ioi 0) := (integrableOn_h6 ha).const_mul _
  have hprod : IntegrableOn (fun y => g6 a y * F0 y) (Ioi 0) :=
    integrableOn_of_prod_bound ha ((continuous_g6 a ha).continuousOn.mul continuousOn_F0)
      (fun y hy => abs_g6F0_le ha hy)
  have hC : IntegrableOn (fun y => 1 / Real.pi * ∑' n : ℕ, k6 a ((n : ℝ) + 1) y) (Ioi 0) := by
    have := (hprod.sub hA).sub hB
    refine this.congr_fun (fun y hy => ?_) measurableSet_Ioi
    have hy : 0 < y := hy
    simp only [Pi.sub_apply]
    rw [hdec y hy]; ring
  -- Step 5: the series of integrals
  have hnorm : Summable fun n : ℕ => ∫ y in Ioi 0, ‖k6 a ((n : ℝ) + 1) y‖ := by
    have hs : Summable fun n : ℕ => 16 * a / ((n : ℝ) + 1) ^ 2 := by
      have := (summable_nat_add_iff 1).mpr (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < 2))
      refine (this.mul_left (16 * a)).congr fun n => ?_
      push_cast; ring
    refine Summable.of_nonneg_of_le (fun n => integral_nonneg fun y => norm_nonneg _) (fun n => ?_) hs
    simp only [Real.norm_eq_abs]
    exact integral_abs_k6_le ha (by positivity)
  have hsum : ∫ y in Ioi 0, ∑' n : ℕ, k6 a ((n : ℝ) + 1) y =
      ∑' n : ℕ, ∫ y in Ioi 0, k6 a ((n : ℝ) + 1) y :=
    (integral_tsum_of_summable_integral_norm (fun n => integrableOn_k6 ha (by positivity)) hnorm).symm
  have hval : ∀ n : ℕ, ∫ y in Ioi 0, k6 a ((n : ℝ) + 1) y = Real.pi * a ^ 6 / (a + ((n : ℝ) + 1)) ^ 7 :=
    fun n => integral_k6 ha (by positivity)
  -- Step 6: assemble
  have hAB : IntegrableOn (fun y => -(1 / 2) * g6 a y + 1 / (2 * Real.pi) * h6 a y) (Ioi 0) := hA.add hB
  rw [setIntegral_congr_fun measurableSet_Ioi (fun y hy => hdec y hy), integral_add hAB hC,
    integral_add hA hB, integral_const_mul, integral_const_mul, integral_const_mul, integral_g6 ha,
    integral_h6 ha, hsum, tsum_congr hval]
  have htail : ∑' n : ℕ, Real.pi * a ^ 6 / (a + ((n : ℝ) + 1)) ^ 7 =
      Real.pi * a ^ 6 * (zeta7 - (H7 j : ℝ)) := by
    rw [← tsum_tail_eq j, ← tsum_mul_left]
    refine tsum_congr fun n => ?_
    rw [ha_def]; ring
  rw [htail]
  have hpi : Real.pi ≠ 0 := Real.pi_pos.ne'
  field_simp
  ring

end Zeta7
