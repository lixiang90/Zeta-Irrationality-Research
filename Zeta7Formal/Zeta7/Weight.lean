import Mathlib

/-!
# 权 `w` 的 b=8 版（式 (2.10)-类比）

`w(y) = (2π)⁶ y⁷ / 360 · ∑_{ℓ ≥ 1} ℓ⁶ e^{-2πℓy}`（6!/2 = 360），其正性、
上界 `w(y) ≤ (128 y + 41) e^{-π y}`（y > 0，`wS_le` 的粗糙合成），以及
`(0, ∞)` 上的可测性。（镜像 `Apery.Weight`；b=8 差异：级数幂 4→6、
前置因子 `(2π)⁴y⁵/12 → (2π)⁶y⁷/360`、上界常数 `32y+11 → 128y+41`。）
-/

open MeasureTheory Set Filter Topology

namespace Zeta7

/-- The series `∑_{ℓ ≥ 1} ℓ⁶ e^{-2πℓy}`. -/
noncomputable def wS (y : ℝ) : ℝ :=
  ∑' ℓ : ℕ, ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y))

/-- The weight `w(y) = (2π)⁶ y⁷ / 360 · ∑_{ℓ ≥ 1} ℓ⁶ e^{-2πℓy}` of (2.10)-类比。 -/
noncomputable def w (y : ℝ) : ℝ := (2 * Real.pi) ^ 6 * y ^ 7 / 360 * wS y

lemma summable_w_term {y : ℝ} (hy : 0 < y) :
    Summable fun ℓ : ℕ => ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) := by
  have h := Real.summable_pow_mul_exp_neg_nat_mul 6 (r := 2 * Real.pi * y) (by positivity)
  have h2 := (summable_nat_add_iff 1).mpr h
  refine h2.congr fun ℓ => ?_
  push_cast
  ring_nf

lemma wS_pos {y : ℝ} (hy : 0 < y) : 0 < wS y :=
  (summable_w_term hy).tsum_pos (fun ℓ => by positivity) 0 (by positivity)

lemma w_pos {y : ℝ} (hy : 0 < y) : 0 < w y := by
  unfold w; have := wS_pos hy; positivity

/-- `1 / (1 - e^{-x}) ≤ 1 + 1 / x` for `x > 0`。 -/
lemma one_div_one_sub_exp_neg_le {x : ℝ} (hx : 0 < x) :
    1 / (1 - Real.exp (-x)) ≤ 1 + 1 / x := by
  have h1 : x + 1 ≤ Real.exp x := Real.add_one_le_exp x
  have h2 : Real.exp (-x) = 1 / Real.exp x := by rw [Real.exp_neg, one_div]
  have h3 : 0 < Real.exp x := Real.exp_pos x
  have h4 : Real.exp (-x) < 1 := by rw [h2, div_lt_one h3]; linarith
  rw [div_le_iff₀ (by linarith), h2]
  have hid : (1 + 1 / x) * (1 - 1 / Real.exp x) =
      1 + (Real.exp x - x - 1) / (x * Real.exp x) := by
    field_simp
    ring
  rw [hid]
  have : 0 ≤ (Real.exp x - x - 1) / (x * Real.exp x) := div_nonneg (by linarith) (by positivity)
  linarith

/-- The bound `wS y ≤ 720 (1 + 1/(πy)) e^{-πy} / (πy)⁶`。 -/
lemma wS_le {y : ℝ} (hy : 0 < y) :
    wS y ≤ 720 / (Real.pi * y) ^ 6 * (1 + 1 / (Real.pi * y)) * Real.exp (-(Real.pi * y)) := by
  have hpy : 0 < Real.pi * y := by positivity
  set q : ℝ := Real.exp (-(Real.pi * y)) with hq
  have hq0 : 0 ≤ q := (Real.exp_pos _).le
  have hq1 : q < 1 := by
    rw [hq, ← Real.exp_zero]; exact Real.exp_lt_exp.mpr (by linarith)
  -- termwise bound
  have hterm : ∀ ℓ : ℕ, ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) ≤
      720 / (Real.pi * y) ^ 6 * (q * q ^ ℓ) := by
    intro ℓ
    have hl : (0 : ℝ) ≤ (ℓ : ℝ) + 1 := by positivity
    have hpow := Real.pow_div_factorial_le_exp (x := Real.pi * y * ((ℓ : ℝ) + 1)) (by positivity) 6
    have hexp : Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) =
        Real.exp (-(Real.pi * y * ((ℓ : ℝ) + 1))) * (q * q ^ ℓ) := by
      rw [hq, ← Real.exp_nat_mul, ← Real.exp_add, ← Real.exp_add]; congr 1; ring
    rw [hexp]
    have hE : Real.exp (-(Real.pi * y * ((ℓ : ℝ) + 1))) = 1 / Real.exp (Real.pi * y * ((ℓ : ℝ) + 1)) := by
      rw [Real.exp_neg, one_div]
    rw [hE]
    have hEpos : 0 < Real.exp (Real.pi * y * ((ℓ : ℝ) + 1)) := Real.exp_pos _
    have hqq : 0 ≤ q * q ^ ℓ := by positivity
    have key : ((ℓ : ℝ) + 1) ^ 6 * (1 / Real.exp (Real.pi * y * ((ℓ : ℝ) + 1))) ≤
        720 / (Real.pi * y) ^ 6 := by
      rw [mul_one_div, div_le_div_iff₀ hEpos (by positivity)]
      have : (Real.pi * y * ((ℓ : ℝ) + 1)) ^ 6 / (6 : ℕ).factorial =
          (Real.pi * y) ^ 6 * ((ℓ : ℝ) + 1) ^ 6 / 720 := by
        rw [Nat.factorial]; norm_num; ring
      rw [this] at hpow
      nlinarith [pow_pos hpy 6]
    calc ((ℓ : ℝ) + 1) ^ 6 * (1 / Real.exp (Real.pi * y * ((ℓ : ℝ) + 1)) * (q * q ^ ℓ))
        = (((ℓ : ℝ) + 1) ^ 6 * (1 / Real.exp (Real.pi * y * ((ℓ : ℝ) + 1)))) * (q * q ^ ℓ) := by
          ring
      _ ≤ 720 / (Real.pi * y) ^ 6 * (q * q ^ ℓ) := mul_le_mul_of_nonneg_right key hqq
  have hgeom : Summable fun ℓ : ℕ => 720 / (Real.pi * y) ^ 6 * (q * q ^ ℓ) :=
    ((summable_geometric_of_lt_one hq0 hq1).mul_left q).mul_left _
  calc wS y ≤ ∑' ℓ : ℕ, 720 / (Real.pi * y) ^ 6 * (q * q ^ ℓ) :=
        (summable_w_term hy).tsum_le_tsum hterm hgeom
    _ = 720 / (Real.pi * y) ^ 6 * (q * (1 / (1 - q))) := by
        rw [tsum_mul_left, tsum_mul_left, tsum_geometric_of_lt_one hq0 hq1, one_div]
    _ ≤ 720 / (Real.pi * y) ^ 6 * (1 + 1 / (Real.pi * y)) * q := by
        have h := one_div_one_sub_exp_neg_le hpy
        rw [← hq] at h
        have h720 : 0 ≤ 720 / (Real.pi * y) ^ 6 := by positivity
        calc 720 / (Real.pi * y) ^ 6 * (q * (1 / (1 - q)))
            ≤ 720 / (Real.pi * y) ^ 6 * (q * (1 + 1 / (Real.pi * y))) := by gcongr
          _ = 720 / (Real.pi * y) ^ 6 * (1 + 1 / (Real.pi * y)) * q := by ring

/-- The bound `w(y) ≤ (128 y + 41) e^{-πy}` for `y > 0`（b=8 常数；128 = 2·(2π)⁶/(360·π⁶)·…，
128/π ≈ 40.7 ≤ 41）。 -/
lemma w_le {y : ℝ} (hy : 0 < y) : w y ≤ (128 * y + 41) * Real.exp (-(Real.pi * y)) := by
  unfold w
  have h := wS_le hy
  have hpi := Real.pi_gt_three
  have hpy : 0 < Real.pi * y := by positivity
  have hc : 0 ≤ (2 * Real.pi) ^ 6 * y ^ 7 / 360 := by positivity
  calc (2 * Real.pi) ^ 6 * y ^ 7 / 360 * wS y
      ≤ (2 * Real.pi) ^ 6 * y ^ 7 / 360 *
          (720 / (Real.pi * y) ^ 6 * (1 + 1 / (Real.pi * y)) * Real.exp (-(Real.pi * y))) :=
        mul_le_mul_of_nonneg_left h hc
    _ = (128 * y + 128 / Real.pi) * Real.exp (-(Real.pi * y)) := by
        field_simp
        ring
    _ ≤ (128 * y + 41) * Real.exp (-(Real.pi * y)) := by
        have : 128 / Real.pi ≤ 41 := by
          rw [div_le_iff₀ (by positivity)]; linarith [Real.pi_gt_d2]
        have he : 0 ≤ Real.exp (-(Real.pi * y)) := (Real.exp_pos _).le
        nlinarith

/-- `wS` is a.e.-measurable on `(0, ∞)`, as the pointwise limit of continuous partial sums. -/
lemma aemeasurable_wS : AEMeasurable wS (volume.restrict (Ioi 0)) := by
  refine aemeasurable_of_tendsto_metrizable_ae' (f := fun n y =>
    ∑ ℓ ∈ Finset.range n, ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y))) ?_ ?_
  · intro n
    refine (Continuous.measurable ?_).aemeasurable
    exact continuous_finsetSum _ fun ℓ _ => continuous_const.mul (Real.continuous_exp.comp (by fun_prop))
  · refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
    exact (summable_w_term hy).hasSum.tendsto_sum_nat

lemma aemeasurable_w : AEMeasurable w (volume.restrict (Ioi 0)) := by
  unfold w
  exact (aemeasurable_const.mul (measurable_id.pow_const 7).aemeasurable |>.div_const 360).mul
    aemeasurable_wS

end Zeta7
