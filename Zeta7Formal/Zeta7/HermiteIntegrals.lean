import Mathlib
import Zeta7.Hermite

/-!
# The rational integrals in Hermite's formula (s = 7)

* `∫₀^∞ g₆(y)/y dy = π/a`;
* `∫₀^∞ g₆(y) y/(y² + n²) dy = π a⁶/(a + n)⁷` for `n > 0` (separate closed forms for
  `n ≠ a` and `n = a`).
The antiderivatives (a rational function plus arctan terms) are verified by differentiation.
-/

open Filter Topology Set MeasureTheory

namespace Zeta7

/-- `g₆(y) / y` as a rational function (continuous at `0`). -/
noncomputable def h6 (a y : ℝ) : ℝ :=
  2 * a ^ 6 * (7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6) / (y ^ 2 + a ^ 2) ^ 7

lemma g6_div_eq_h6 (a : ℝ) {y : ℝ} (hy : y ≠ 0) : g6 a y / y = h6 a y := by
  unfold g6 h6; field_simp

lemma abs_h6_le {a : ℝ} (ha : 0 < a) (y : ℝ) : |h6 a y| ≤ 128 / (y ^ 2 + a ^ 2) := by
  unfold h6
  have hden : 0 < y ^ 2 + a ^ 2 := by positivity
  rw [abs_div, abs_of_pos (by positivity : (0 : ℝ) < (y ^ 2 + a ^ 2) ^ 7),
    div_le_div_iff₀ (by positivity) hden]
  have hP : |7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6| ≤
      64 * (y ^ 2 + a ^ 2) ^ 3 := by
    rw [abs_le]
    constructor <;> nlinarith [sq_nonneg (y ^ 3), sq_nonneg (y ^ 2 * a), sq_nonneg (y * a ^ 2),
      sq_nonneg (a ^ 3)]
  have h1 : |2 * a ^ 6 * (7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6)| ≤
      2 * a ^ 6 * (64 * (y ^ 2 + a ^ 2) ^ 3) := by
    rw [abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ 2 * a ^ 6)]
    exact mul_le_mul_of_nonneg_left hP (by positivity)
  have h2 : a ^ 6 ≤ (y ^ 2 + a ^ 2) ^ 3 := by
    nlinarith [sq_nonneg (y ^ 3), sq_nonneg (y ^ 2 * a), sq_nonneg (y * a ^ 2)]
  calc |2 * a ^ 6 * (7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6)| * (y ^ 2 + a ^ 2)
      ≤ 2 * a ^ 6 * (64 * (y ^ 2 + a ^ 2) ^ 3) * (y ^ 2 + a ^ 2) := by gcongr
    _ ≤ 2 * (y ^ 2 + a ^ 2) ^ 3 * (64 * (y ^ 2 + a ^ 2) ^ 3) * (y ^ 2 + a ^ 2) := by gcongr
    _ = 128 * (y ^ 2 + a ^ 2) ^ 7 := by ring

lemma integrableOn_of_le_inv_sq {a : ℝ} (ha : 0 < a) {f : ℝ → ℝ}
    (hf : AEStronglyMeasurable f (volume.restrict (Ioi 0)))
    {C : ℝ} (hC : ∀ y, 0 < y → |f y| ≤ C / (y ^ 2 + a ^ 2)) : IntegrableOn f (Ioi 0) := by
  have hg : IntegrableOn (fun y : ℝ => (C * (1 + 1 / a ^ 2)) * (1 + y ^ 2)⁻¹) (Ioi 0) :=
    (integrable_inv_one_add_sq.const_mul _).integrableOn
  refine hg.mono' hf ?_
  refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
  have hy : 0 < y := hy
  rw [Real.norm_eq_abs]
  have hC0 : 0 ≤ C := by
    by_contra hneg
    push Not at hneg
    have h1 := hC y hy
    have h2 : C / (y ^ 2 + a ^ 2) < 0 := div_neg_of_neg_of_pos hneg (by positivity)
    linarith [abs_nonneg (f y)]
  calc |f y| ≤ C / (y ^ 2 + a ^ 2) := hC y hy
    _ = C * (1 / (y ^ 2 + a ^ 2)) := by ring
    _ ≤ C * ((1 + 1 / a ^ 2) * (1 / (1 + y ^ 2))) := by gcongr; exact inv_sq_add_le ha y
    _ = _ := by ring

/-- The limit `arctan (y / c) → π/2` as `y → ∞`, for `c > 0`. -/
lemma tendsto_arctan_div_atTop {c : ℝ} (hc : 0 < c) :
    Tendsto (fun y : ℝ => Real.arctan (y / c)) atTop (𝓝 (Real.pi / 2)) :=
  (Real.tendsto_arctan_atTop.mono_right nhdsWithin_le_nhds).comp (tendsto_id.atTop_div_const hc)

/-! ### `∫₀^∞ g₆(y)/y dy = π / a` -/

/-- Antiderivative of `h₆`. -/
noncomputable def A1 (a y : ℝ) : ℝ :=
  2 / a * Real.arctan (y / a) +
    y * (180 * a ^ 10 + 250 * a ^ 8 * y ^ 2 + 486 * a ^ 6 * y ^ 4 + 396 * a ^ 4 * y ^ 6 +
      170 * a ^ 2 * y ^ 8 + 30 * y ^ 10) / (15 * (a ^ 2 + y ^ 2) ^ 6)

lemma hasDerivAt_A1 {a : ℝ} (ha : 0 < a) (y : ℝ) : HasDerivAt (A1 a) (h6 a y) y := by
  have h1 := ((hasDerivAt_id y).div_const a).arctan.const_mul (2 / a)
  have hne : 15 * (a ^ 2 + y ^ 2) ^ 6 ≠ 0 := by positivity
  have c0 := ((hasDerivAt_pow 2 y).const_mul (250 * a ^ 8)).const_add (180 * a ^ 10)
  have c1 := c0.add ((hasDerivAt_pow 4 y).const_mul (486 * a ^ 6))
  have c2 := c1.add ((hasDerivAt_pow 6 y).const_mul (396 * a ^ 4))
  have c3 := c2.add ((hasDerivAt_pow 8 y).const_mul (170 * a ^ 2))
  have c4 := c3.add ((hasDerivAt_pow 10 y).const_mul 30)
  have hnum := (hasDerivAt_id y).mul c4
  have h2 := hnum.div ((((hasDerivAt_pow 2 y).const_add (a ^ 2)).pow 6).const_mul 15) hne
  have h := h1.add h2
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun t => ?_)).congr_deriv ?_
  · simp only [A1, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
  · simp only [h6, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
    field_simp
    ring

lemma tendsto_A1_atTop {a : ℝ} (ha : 0 < a) : Tendsto (A1 a) atTop (𝓝 (Real.pi / a)) := by
  have h1 : Tendsto (fun y : ℝ => 2 / a * Real.arctan (y / a)) atTop (𝓝 (2 / a * (Real.pi / 2))) :=
    (tendsto_arctan_div_atTop ha).const_mul _
  have hφ : Tendsto (fun u : ℝ => u * (180 * a ^ 10 * u ^ 10 + 250 * a ^ 8 * u ^ 8 +
        486 * a ^ 6 * u ^ 6 + 396 * a ^ 4 * u ^ 4 + 170 * a ^ 2 * u ^ 2 + 30) /
      (15 * (a ^ 2 * u ^ 2 + 1) ^ 6)) (𝓝 0) (𝓝 0) := by
    have : ContinuousAt (fun u : ℝ => u * (180 * a ^ 10 * u ^ 10 + 250 * a ^ 8 * u ^ 8 +
          486 * a ^ 6 * u ^ 6 + 396 * a ^ 4 * u ^ 4 + 170 * a ^ 2 * u ^ 2 + 30) /
        (15 * (a ^ 2 * u ^ 2 + 1) ^ 6)) 0 :=
      ContinuousAt.div (by fun_prop) (by fun_prop) (by norm_num)
    simpa using this.tendsto
  have h2 : Tendsto (fun y : ℝ => y * (180 * a ^ 10 + 250 * a ^ 8 * y ^ 2 +
        486 * a ^ 6 * y ^ 4 + 396 * a ^ 4 * y ^ 6 + 170 * a ^ 2 * y ^ 8 + 30 * y ^ 10) /
      (15 * (a ^ 2 + y ^ 2) ^ 6)) atTop (𝓝 0) := by
    refine (hφ.comp tendsto_inv_atTop_zero).congr' ?_
    filter_upwards [eventually_gt_atTop 0] with y hy
    simp only [Function.comp]
    field_simp
  have := h1.add h2
  unfold A1
  convert this using 2
  field_simp
  ring

lemma continuous_g6 (a : ℝ) (ha : 0 < a) : Continuous (g6 a) := by
  unfold g6
  exact (by fun_prop : Continuous fun y : ℝ =>
    2 * a ^ 6 * y * (7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6)).div
    (by fun_prop) (fun y => by positivity)

lemma integrableOn_h6 {a : ℝ} (ha : 0 < a) : IntegrableOn (h6 a) (Ioi 0) := by
  have hcont : Continuous (h6 a) := by
    unfold h6
    exact (by fun_prop : Continuous fun y : ℝ =>
      2 * a ^ 6 * (7 * a ^ 6 - 35 * a ^ 4 * y ^ 2 + 21 * a ^ 2 * y ^ 4 - y ^ 6)).div
      (by fun_prop) (fun y => by positivity)
  exact integrableOn_of_le_inv_sq ha hcont.aestronglyMeasurable (fun y _ => abs_h6_le ha y)

/-- `∫₀^∞ g₆(y)/y dy = π/a`. -/
lemma integral_h6 {a : ℝ} (ha : 0 < a) : ∫ y in Ioi 0, h6 a y = Real.pi / a := by
  have h := integral_Ioi_of_hasDerivAt_of_tendsto' (a := 0) (f := A1 a) (f' := h6 a)
    (fun y _ => hasDerivAt_A1 ha y) (integrableOn_h6 ha) (tendsto_A1_atTop ha)
  rw [h]; simp [A1]


/-! ### `∫₀^∞ g₆(y) y/(y² + n²) dy = π a⁶/(a + n)⁷` -/

/-- The integrand `g₆(y) · y/(y² + n²)`. -/
noncomputable def k6 (a n y : ℝ) : ℝ := g6 a y * (y / (y ^ 2 + n ^ 2))

lemma abs_k6_le {a n : ℝ} (ha : 0 < a) (hn : 0 < n) {y : ℝ} (hy : 0 < y) :
    |k6 a n y| ≤ 32 * a / n / (y ^ 2 + a ^ 2) := by
  unfold k6
  have h1 := abs_g6_le ha hy.le
  have h2 : y / (y ^ 2 + n ^ 2) ≤ 1 / (2 * n) := by
    rw [div_le_div_iff₀ (by positivity) (by positivity)]; nlinarith [sq_nonneg (y - n)]
  have h3 : 0 ≤ y / (y ^ 2 + n ^ 2) := by positivity
  rw [abs_mul, abs_of_nonneg h3]
  calc |g6 a y| * (y / (y ^ 2 + n ^ 2)) ≤
      64 * a ^ 5 / (y ^ 2 + a ^ 2) ^ 3 * (1 / (2 * n)) := by gcongr
    _ ≤ 64 * a ^ 5 / (a ^ 4 * (y ^ 2 + a ^ 2)) * (1 / (2 * n)) := by
        have hk : a ^ 4 * (y ^ 2 + a ^ 2) ≤ (y ^ 2 + a ^ 2) ^ 3 := by
          have h1 : a ^ 4 ≤ (y ^ 2 + a ^ 2) ^ 2 := by
            nlinarith [sq_nonneg (y ^ 2), mul_nonneg (sq_nonneg y) (sq_nonneg a)]
          calc a ^ 4 * (y ^ 2 + a ^ 2) ≤ (y ^ 2 + a ^ 2) ^ 2 * (y ^ 2 + a ^ 2) :=
                mul_le_mul_of_nonneg_right h1 (by positivity)
            _ = (y ^ 2 + a ^ 2) ^ 3 := by ring
        exact mul_le_mul_of_nonneg_right
          (div_le_div_of_nonneg_left (by positivity) (by positivity) hk) (by positivity)
    _ = 32 * a / n / (y ^ 2 + a ^ 2) := by
        have hane : a ≠ 0 := ha.ne'
        have hnne : n ≠ 0 := hn.ne'
        field_simp
        ring

lemma integrableOn_k6 {a n : ℝ} (ha : 0 < a) (hn : 0 < n) : IntegrableOn (k6 a n) (Ioi 0) := by
  have hcont : Continuous (k6 a n) := by
    unfold k6
    exact (continuous_g6 a ha).mul ((by fun_prop : Continuous fun y : ℝ => y).div (by fun_prop)
      (fun y => by positivity))
  exact integrableOn_of_le_inv_sq ha hcont.aestronglyMeasurable (fun y hy => abs_k6_le ha hn hy)

/-- Antiderivative of `k₆ a n` for `n ≠ a`; the denominators are powers of `D = a² - n²`. -/
noncomputable def A2 (a n y : ℝ) : ℝ :=
  (2 * a ^ 7 * (a ^ 6 + 21 * a ^ 4 * n ^ 2 + 35 * a ^ 2 * n ^ 4 + 7 * n ^ 6)) /
    (a ^ 2 - n ^ 2) ^ 7 * Real.arctan (y / a) -
  (2 * a ^ 6 * n * (7 * a ^ 6 + 35 * a ^ 4 * n ^ 2 + 21 * a ^ 2 * n ^ 4 + n ^ 6)) /
    (a ^ 2 - n ^ 2) ^ 7 * Real.arctan (y / n) +
  (y ^ 11 * (240 * a ^ 6 * (a ^ 2 + n ^ 2) * (a ^ 4 + 14 * a ^ 2 * n ^ 2 + n ^ 4)) +
    y ^ 9 * (80 * a ^ 6 * (17 * a ^ 8 + 248 * a ^ 6 * n ^ 2 + 220 * a ^ 4 * n ^ 4 -
      4 * a ^ 2 * n ^ 6 - n ^ 8)) +
    y ^ 7 * (48 * a ^ 6 * (66 * a ^ 10 + 927 * a ^ 8 * n ^ 2 + 682 * a ^ 6 * n ^ 4 -
      88 * a ^ 4 * n ^ 6 + 12 * a ^ 2 * n ^ 8 + n ^ 10)) +
    y ^ 5 * (48 * a ^ 8 * (81 * a ^ 10 + 1062 * a ^ 8 * n ^ 2 + 562 * a ^ 6 * n ^ 4 -
      168 * a ^ 4 * n ^ 6 + 77 * a ^ 2 * n ^ 8 - 14 * n ^ 10)) +
    y ^ 3 * (80 * a ^ 10 * (25 * a ^ 10 + 424 * a ^ 8 * n ^ 2 - 39 * a ^ 6 * n ^ 4 +
      105 * a ^ 4 * n ^ 6 - 42 * a ^ 2 * n ^ 8 + 7 * n ^ 10)) +
    y * (480 * a ^ 18 * (a ^ 2 + 3 * n ^ 2) * (3 * a ^ 2 + n ^ 2))) /
    (120 * (a ^ 2 - n ^ 2) ^ 6 * (a ^ 2 + y ^ 2) ^ 6)

lemma hasDerivAt_A2 {a n : ℝ} (ha : 0 < a) (hn : 0 < n) (hne : n ≠ a) (y : ℝ) :
    HasDerivAt (A2 a n) (k6 a n y) y := by
  have hD : a ^ 2 - n ^ 2 ≠ 0 := by
    intro h
    have : (a - n) * (a + n) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h' | h'
    · exact hne (by linarith)
    · linarith
  have h1 := ((hasDerivAt_id y).div_const a).arctan.const_mul
    ((2 * a ^ 7 * (a ^ 6 + 21 * a ^ 4 * n ^ 2 + 35 * a ^ 2 * n ^ 4 + 7 * n ^ 6)) /
      (a ^ 2 - n ^ 2) ^ 7)
  have h2 := ((hasDerivAt_id y).div_const n).arctan.const_mul
    ((2 * a ^ 6 * n * (7 * a ^ 6 + 35 * a ^ 4 * n ^ 2 + 21 * a ^ 2 * n ^ 4 + n ^ 6)) /
      (a ^ 2 - n ^ 2) ^ 7)
  have hne3 : 120 * (a ^ 2 - n ^ 2) ^ 6 * (a ^ 2 + y ^ 2) ^ 6 ≠ 0 := by positivity
  have d11 := (hasDerivAt_pow 11 y).mul_const
    (240 * a ^ 6 * (a ^ 2 + n ^ 2) * (a ^ 4 + 14 * a ^ 2 * n ^ 2 + n ^ 4))
  have d9 := d11.add ((hasDerivAt_pow 9 y).mul_const
    (80 * a ^ 6 * (17 * a ^ 8 + 248 * a ^ 6 * n ^ 2 + 220 * a ^ 4 * n ^ 4 -
      4 * a ^ 2 * n ^ 6 - n ^ 8)))
  have d7 := d9.add ((hasDerivAt_pow 7 y).mul_const
    (48 * a ^ 6 * (66 * a ^ 10 + 927 * a ^ 8 * n ^ 2 + 682 * a ^ 6 * n ^ 4 -
      88 * a ^ 4 * n ^ 6 + 12 * a ^ 2 * n ^ 8 + n ^ 10)))
  have d5 := d7.add ((hasDerivAt_pow 5 y).mul_const
    (48 * a ^ 8 * (81 * a ^ 10 + 1062 * a ^ 8 * n ^ 2 + 562 * a ^ 6 * n ^ 4 -
      168 * a ^ 4 * n ^ 6 + 77 * a ^ 2 * n ^ 8 - 14 * n ^ 10)))
  have d3 := d5.add ((hasDerivAt_pow 3 y).mul_const
    (80 * a ^ 10 * (25 * a ^ 10 + 424 * a ^ 8 * n ^ 2 - 39 * a ^ 6 * n ^ 4 +
      105 * a ^ 4 * n ^ 6 - 42 * a ^ 2 * n ^ 8 + 7 * n ^ 10)))
  have d1 := d3.add ((hasDerivAt_id y).mul_const
    (480 * a ^ 18 * (a ^ 2 + 3 * n ^ 2) * (3 * a ^ 2 + n ^ 2)))
  have h3 := d1.div ((((hasDerivAt_pow 2 y).const_add (a ^ 2)).pow 6).const_mul
    (120 * (a ^ 2 - n ^ 2) ^ 6)) hne3
  have h := (h1.sub h2).add h3
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun t => ?_)).congr_deriv ?_
  · simp only [A2, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
  · simp only [k6, g6, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
    have hyn : y ^ 2 + n ^ 2 ≠ 0 := by positivity
    have hya : a ^ 2 + y ^ 2 ≠ 0 := by positivity
    field_simp
    ring

lemma tendsto_A2_atTop {a n : ℝ} (ha : 0 < a) (hn : 0 < n) (hne : n ≠ a) :
    Tendsto (A2 a n) atTop (𝓝 (Real.pi * a ^ 6 / (a + n) ^ 7)) := by
  have hD : a ^ 2 - n ^ 2 ≠ 0 := by
    intro h
    have : (a - n) * (a + n) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.mp this with h' | h'
    · exact hne (by linarith)
    · linarith
  have h1 := (tendsto_arctan_div_atTop ha).const_mul
    ((2 * a ^ 7 * (a ^ 6 + 21 * a ^ 4 * n ^ 2 + 35 * a ^ 2 * n ^ 4 + 7 * n ^ 6)) /
      (a ^ 2 - n ^ 2) ^ 7)
  have h2 := (tendsto_arctan_div_atTop hn).const_mul
    ((2 * a ^ 6 * n * (7 * a ^ 6 + 35 * a ^ 4 * n ^ 2 + 21 * a ^ 2 * n ^ 4 + n ^ 6)) /
      (a ^ 2 - n ^ 2) ^ 7)
  have hφ : Tendsto (fun u : ℝ => u * (240 * a ^ 6 * (a ^ 2 + n ^ 2) *
        (a ^ 4 + 14 * a ^ 2 * n ^ 2 + n ^ 4) +
      u ^ 2 * (80 * a ^ 6 * (17 * a ^ 8 + 248 * a ^ 6 * n ^ 2 + 220 * a ^ 4 * n ^ 4 -
        4 * a ^ 2 * n ^ 6 - n ^ 8)) +
      u ^ 4 * (48 * a ^ 6 * (66 * a ^ 10 + 927 * a ^ 8 * n ^ 2 + 682 * a ^ 6 * n ^ 4 -
        88 * a ^ 4 * n ^ 6 + 12 * a ^ 2 * n ^ 8 + n ^ 10)) +
      u ^ 6 * (48 * a ^ 8 * (81 * a ^ 10 + 1062 * a ^ 8 * n ^ 2 + 562 * a ^ 6 * n ^ 4 -
        168 * a ^ 4 * n ^ 6 + 77 * a ^ 2 * n ^ 8 - 14 * n ^ 10)) +
      u ^ 8 * (80 * a ^ 10 * (25 * a ^ 10 + 424 * a ^ 8 * n ^ 2 - 39 * a ^ 6 * n ^ 4 +
        105 * a ^ 4 * n ^ 6 - 42 * a ^ 2 * n ^ 8 + 7 * n ^ 10)) +
      u ^ 10 * (480 * a ^ 18 * (a ^ 2 + 3 * n ^ 2) * (3 * a ^ 2 + n ^ 2))) /
      (120 * (a ^ 2 - n ^ 2) ^ 6 * (a ^ 2 * u ^ 2 + 1) ^ 6)) (𝓝 0) (𝓝 0) := by
    have : ContinuousAt (fun u : ℝ => u * (240 * a ^ 6 * (a ^ 2 + n ^ 2) *
          (a ^ 4 + 14 * a ^ 2 * n ^ 2 + n ^ 4) +
        u ^ 2 * (80 * a ^ 6 * (17 * a ^ 8 + 248 * a ^ 6 * n ^ 2 + 220 * a ^ 4 * n ^ 4 -
          4 * a ^ 2 * n ^ 6 - n ^ 8)) +
        u ^ 4 * (48 * a ^ 6 * (66 * a ^ 10 + 927 * a ^ 8 * n ^ 2 + 682 * a ^ 6 * n ^ 4 -
          88 * a ^ 4 * n ^ 6 + 12 * a ^ 2 * n ^ 8 + n ^ 10)) +
        u ^ 6 * (48 * a ^ 8 * (81 * a ^ 10 + 1062 * a ^ 8 * n ^ 2 + 562 * a ^ 6 * n ^ 4 -
          168 * a ^ 4 * n ^ 6 + 77 * a ^ 2 * n ^ 8 - 14 * n ^ 10)) +
        u ^ 8 * (80 * a ^ 10 * (25 * a ^ 10 + 424 * a ^ 8 * n ^ 2 - 39 * a ^ 6 * n ^ 4 +
          105 * a ^ 4 * n ^ 6 - 42 * a ^ 2 * n ^ 8 + 7 * n ^ 10)) +
        u ^ 10 * (480 * a ^ 18 * (a ^ 2 + 3 * n ^ 2) * (3 * a ^ 2 + n ^ 2))) /
        (120 * (a ^ 2 - n ^ 2) ^ 6 * (a ^ 2 * u ^ 2 + 1) ^ 6)) 0 :=
      ContinuousAt.div (by fun_prop) (by fun_prop) (by simp; positivity)
    simpa using this.tendsto
  have h3 : Tendsto (fun y : ℝ => (y ^ 11 * (240 * a ^ 6 * (a ^ 2 + n ^ 2) *
          (a ^ 4 + 14 * a ^ 2 * n ^ 2 + n ^ 4)) +
        y ^ 9 * (80 * a ^ 6 * (17 * a ^ 8 + 248 * a ^ 6 * n ^ 2 + 220 * a ^ 4 * n ^ 4 -
          4 * a ^ 2 * n ^ 6 - n ^ 8)) +
        y ^ 7 * (48 * a ^ 6 * (66 * a ^ 10 + 927 * a ^ 8 * n ^ 2 + 682 * a ^ 6 * n ^ 4 -
          88 * a ^ 4 * n ^ 6 + 12 * a ^ 2 * n ^ 8 + n ^ 10)) +
        y ^ 5 * (48 * a ^ 8 * (81 * a ^ 10 + 1062 * a ^ 8 * n ^ 2 + 562 * a ^ 6 * n ^ 4 -
          168 * a ^ 4 * n ^ 6 + 77 * a ^ 2 * n ^ 8 - 14 * n ^ 10)) +
        y ^ 3 * (80 * a ^ 10 * (25 * a ^ 10 + 424 * a ^ 8 * n ^ 2 - 39 * a ^ 6 * n ^ 4 +
          105 * a ^ 4 * n ^ 6 - 42 * a ^ 2 * n ^ 8 + 7 * n ^ 10)) +
        y * (480 * a ^ 18 * (a ^ 2 + 3 * n ^ 2) * (3 * a ^ 2 + n ^ 2))) /
        (120 * (a ^ 2 - n ^ 2) ^ 6 * (a ^ 2 + y ^ 2) ^ 6)) atTop (𝓝 0) := by
    refine (hφ.comp tendsto_inv_atTop_zero).congr' ?_
    filter_upwards [eventually_gt_atTop 0] with y hy
    simp only [Function.comp]
    field_simp
  have := (h1.sub h2).add h3
  unfold A2
  convert this using 2
  have hsum : a + n ≠ 0 := by positivity
  have hdiff : a - n ≠ 0 := sub_ne_zero.mpr (Ne.symm hne)
  have hDf : a ^ 2 - n ^ 2 = (a - n) * (a + n) := by ring
  rw [hDf]
  field_simp
  ring

/-- `∫₀^∞ g₆(y) y/(y² + n²) dy = π a⁶/(a + n)⁷` for `n ≠ a`. -/
lemma integral_k6_ne {a n : ℝ} (ha : 0 < a) (hn : 0 < n) (hne : n ≠ a) :
    ∫ y in Ioi 0, k6 a n y = Real.pi * a ^ 6 / (a + n) ^ 7 := by
  have h := integral_Ioi_of_hasDerivAt_of_tendsto' (a := 0) (f := A2 a n) (f' := k6 a n)
    (fun y _ => hasDerivAt_A2 ha hn hne y) (integrableOn_k6 ha hn) (tendsto_A2_atTop ha hn hne)
  rw [h]; simp [A2]

/-- Antiderivative of `k₆ a a`. -/
noncomputable def A2e (a y : ℝ) : ℝ :=
  Real.arctan (y / a) / (64 * a) +
    y * (-105 * a ^ 12 + 30660 * a ^ 10 * y ^ 2 - 27069 * a ^ 8 * y ^ 4 +
      4992 * a ^ 6 * y ^ 6 + 1981 * a ^ 4 * y ^ 8 + 700 * a ^ 2 * y ^ 10 + 105 * y ^ 12) /
      (6720 * (a ^ 2 + y ^ 2) ^ 7)

lemma hasDerivAt_A2e {a : ℝ} (ha : 0 < a) (y : ℝ) : HasDerivAt (A2e a) (k6 a a y) y := by
  have h1 := ((hasDerivAt_id y).div_const a).arctan.div_const (64 * a)
  have hne : 6720 * (a ^ 2 + y ^ 2) ^ 7 ≠ 0 := by positivity
  have c0 := ((hasDerivAt_pow 2 y).const_mul (30660 * a ^ 10)).const_add (-105 * a ^ 12)
  have c1 := c0.add ((hasDerivAt_pow 4 y).const_mul (-27069 * a ^ 8))
  have c2 := c1.add ((hasDerivAt_pow 6 y).const_mul (4992 * a ^ 6))
  have c3 := c2.add ((hasDerivAt_pow 8 y).const_mul (1981 * a ^ 4))
  have c4 := c3.add ((hasDerivAt_pow 10 y).const_mul (700 * a ^ 2))
  have c5 := c4.add ((hasDerivAt_pow 12 y).const_mul 105)
  have hnum := (hasDerivAt_id y).mul c5
  have h2 := hnum.div ((((hasDerivAt_pow 2 y).const_add (a ^ 2)).pow 7).const_mul 6720) hne
  have h := h1.add h2
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun t => ?_)).congr_deriv ?_
  · simp only [A2e, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
    ring
  · simp only [k6, g6, id, Pi.add_apply, Pi.sub_apply, Pi.mul_apply, Pi.div_apply, Pi.pow_apply]
    have hya : a ^ 2 + y ^ 2 ≠ 0 := by positivity
    have hya' : y ^ 2 + a ^ 2 ≠ 0 := by positivity
    field_simp
    ring

lemma tendsto_A2e_atTop {a : ℝ} (ha : 0 < a) :
    Tendsto (A2e a) atTop (𝓝 (Real.pi * a ^ 6 / (a + a) ^ 7)) := by
  have h1 := (tendsto_arctan_div_atTop ha).div_const (64 * a)
  have hφ : Tendsto (fun u : ℝ => u * (-105 * a ^ 12 * u ^ 12 + 30660 * a ^ 10 * u ^ 10 -
        27069 * a ^ 8 * u ^ 8 + 4992 * a ^ 6 * u ^ 6 + 1981 * a ^ 4 * u ^ 4 +
        700 * a ^ 2 * u ^ 2 + 105) / (6720 * (a ^ 2 * u ^ 2 + 1) ^ 7)) (𝓝 0) (𝓝 0) := by
    have : ContinuousAt (fun u : ℝ => u * (-105 * a ^ 12 * u ^ 12 + 30660 * a ^ 10 * u ^ 10 -
          27069 * a ^ 8 * u ^ 8 + 4992 * a ^ 6 * u ^ 6 + 1981 * a ^ 4 * u ^ 4 +
          700 * a ^ 2 * u ^ 2 + 105) / (6720 * (a ^ 2 * u ^ 2 + 1) ^ 7)) 0 :=
      ContinuousAt.div (by fun_prop) (by fun_prop) (by norm_num)
    simpa using this.tendsto
  have h2 : Tendsto (fun y : ℝ => y * (-105 * a ^ 12 + 30660 * a ^ 10 * y ^ 2 -
        27069 * a ^ 8 * y ^ 4 + 4992 * a ^ 6 * y ^ 6 + 1981 * a ^ 4 * y ^ 8 +
        700 * a ^ 2 * y ^ 10 + 105 * y ^ 12) / (6720 * (a ^ 2 + y ^ 2) ^ 7)) atTop (𝓝 0) := by
    refine (hφ.comp tendsto_inv_atTop_zero).congr' ?_
    filter_upwards [eventually_gt_atTop 0] with y hy
    simp only [Function.comp]
    field_simp
  have := h1.add h2
  unfold A2e
  convert this using 2
  field_simp
  ring

/-- `∫₀^∞ g₆(y) y/(y² + a²) dy = π a⁶/(2a)⁷`. -/
lemma integral_k6_eq {a : ℝ} (ha : 0 < a) :
    ∫ y in Ioi 0, k6 a a y = Real.pi * a ^ 6 / (a + a) ^ 7 := by
  have h := integral_Ioi_of_hasDerivAt_of_tendsto' (a := 0) (f := A2e a) (f' := k6 a a)
    (fun y _ => hasDerivAt_A2e ha y) (integrableOn_k6 ha ha) (tendsto_A2e_atTop ha)
  rw [h]; simp [A2e]

/-- `∫₀^∞ g₆(y) y/(y² + n²) dy = π a⁶/(a + n)⁷` for all `n > 0`. -/
lemma integral_k6 {a n : ℝ} (ha : 0 < a) (hn : 0 < n) :
    ∫ y in Ioi 0, k6 a n y = Real.pi * a ^ 6 / (a + n) ^ 7 := by
  rcases eq_or_ne n a with rfl | hne
  · exact integral_k6_eq ha
  · exact integral_k6_ne ha hn hne

end Zeta7
