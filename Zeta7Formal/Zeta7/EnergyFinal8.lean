import Mathlib
import Zeta7.EnergyRaw8
import Zeta7.PotentialIneq8
import Zeta7.Potential8
import Zeta7.Phi8
import Zeta7.Table7.All

/-!
# b=8 构型不等式（式 (6.9) 类比）

镜像 `Apery/EnergyFinal.lean`：由 energy_raw8（ε = K⁻⁶）、位势不等式
`Zeta7.Table7.All.potential_ineq`、尾部界与正则化误差界得
`energy_ineq_final8`：对任意 h = 39n 个正、两两不同的构型点，

`2∑_{i<j} log|tᵢ−tⱼ| − K∑V₈(tᵢ) + ∑√tᵢ ≤ (λ₈M₀_8 − I(ρ₈))K² + 5·39n + 6·39n·log K`。

b=8 常数：Err8 加权和 622√t + 1421（λ₈·637/1457 放缩）；e3 系数 16α = 0.4；
尾部粗估计系数 1.15·log t；最终 39n。
-/

open MeasureTheory Set Real Filter Topology Finset

namespace Zeta7

lemma sqrt_add_le' {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    Real.sqrt (a + b) ≤ Real.sqrt a + Real.sqrt b := by
  rw [Real.sqrt_le_iff]
  refine ⟨by positivity, ?_⟩
  have h1 := Real.sq_sqrt ha
  have h2 := Real.sq_sqrt hb
  nlinarith [Real.sqrt_nonneg a, Real.sqrt_nonneg b]

/-- 区间正则化误差（常数 637/1457 仅依赖 r ≥ 1/450，与表无关；镜像 Apery.errj_le）。 -/
lemma errj_le8 {ε t m r : ℝ} (hε : 0 < ε) (hε1 : ε ≤ 1) (ht : 0 < t) (hm : 0 < m ∧ m < 2)
    (hr : 1 / 450 ≤ r) :
    errj ε t m r ≤ Real.sqrt ε * (637 * Real.sqrt t + 1457) := by
  unfold errj
  have hr0 : 0 < r := by linarith
  have hse : 0 ≤ Real.sqrt ε := Real.sqrt_nonneg ε
  have hst : 0 ≤ Real.sqrt t := Real.sqrt_nonneg t
  have hεs : ε ≤ Real.sqrt ε := by
    rw [Real.le_sqrt hε.le hε.le]; nlinarith
  have h1 : ε / r ≤ 450 * ε := by rw [div_le_iff₀ hr0]; nlinarith
  have habs : |t - m| ≤ t + 2 := by rw [abs_le]; constructor <;> linarith
  have h2 : ε / r * ((ε + 2 * |t - m|) / r) ≤ 450 ^ 2 * ε * (2 * t + 5) := by
    have : (ε + 2 * |t - m|) / r ≤ 450 * (2 * t + 5) := by
      rw [div_le_iff₀ hr0]; nlinarith
    calc ε / r * ((ε + 2 * |t - m|) / r) ≤ (450 * ε) * (450 * (2 * t + 5)) :=
          mul_le_mul h1 this (by positivity) (by positivity)
      _ = 450 ^ 2 * ε * (2 * t + 5) := by ring
  have hs2 : Real.sqrt 2 ≤ 14143 / 10000 := by
    rw [Real.sqrt_le_iff]; constructor <;> norm_num
  have hs5 : Real.sqrt 5 ≤ 22361 / 10000 := by
    rw [Real.sqrt_le_iff]; constructor <;> norm_num
  have h3 : Real.sqrt (ε / r * ((ε + 2 * |t - m|) / r)) ≤
      450 * Real.sqrt ε * (14143 / 10000 * Real.sqrt t + 22361 / 10000) := by
    calc Real.sqrt (ε / r * ((ε + 2 * |t - m|) / r))
        ≤ Real.sqrt (450 ^ 2 * ε * (2 * t + 5)) := Real.sqrt_le_sqrt h2
      _ = 450 * Real.sqrt ε * Real.sqrt (2 * t + 5) := by
          rw [Real.sqrt_mul (by positivity), Real.sqrt_mul (by positivity),
            Real.sqrt_sq (by norm_num)]
      _ ≤ 450 * Real.sqrt ε * (Real.sqrt (2 * t) + Real.sqrt 5) := by
          apply mul_le_mul_of_nonneg_left (sqrt_add_le' (by positivity) (by norm_num))
          positivity
      _ ≤ 450 * Real.sqrt ε * (14143 / 10000 * Real.sqrt t + 22361 / 10000) := by
          apply mul_le_mul_of_nonneg_left _ (by positivity)
          rw [Real.sqrt_mul (by norm_num)]
          have := mul_le_mul_of_nonneg_right hs2 hst
          linarith
  nlinarith

lemma sum_cρ_fin8 : ∑ j : Fin 16, cρ8 (j + 1) = lam8 := by
  rw [← Sρ8_sixteen, Sρ8, sum_Icc_eq_sum_range', Fin.sum_univ_eq_sum_range (fun j => cρ8 (j + 1))]

/-- 总正则化误差（λ₈ = 39/40 加权：0.975·637 ≤ 622，0.975·1457 ≤ 1421）。 -/
lemma Err_le8 {ε t : ℝ} (hε : 0 < ε) (hε1 : ε ≤ 1) (ht : 0 < t) :
    Err8 ε t ≤ Real.sqrt ε * (622 * Real.sqrt t + 1421) := by
  unfold Err8
  have hse : 0 ≤ Real.sqrt ε := Real.sqrt_nonneg ε
  have hst : 0 ≤ Real.sqrt t := Real.sqrt_nonneg t
  calc ∑ j : Fin 16, cρ8 (j + 1) * errj ε t (mρ8 (j + 1)) (rρ8 (j + 1))
      ≤ ∑ j : Fin 16, cρ8 (j + 1) * (Real.sqrt ε * (637 * Real.sqrt t + 1457)) := by
        refine Finset.sum_le_sum fun j _ => ?_
        exact mul_le_mul_of_nonneg_left (errj_le8 hε hε1 ht (mρ8_bounds j) (rρ8_ge j))
          (cρ8_pos _ (by simp only [Finset.mem_Icc]; omega)).le
    _ = lam8 * (Real.sqrt ε * (637 * Real.sqrt t + 1457)) := by
        rw [← Finset.sum_mul, sum_cρ_fin8]
    _ ≤ _ := by
        simp only [lam8]
        nlinarith

/-- V₈ 的尾部下界（(6.8) 类比）：`V₈(t) ≥ 2π√t + log t − 8α(log t + α²/t)`。 -/
lemma Vfield8_ge_tail {t : ℝ} (ht : 2 ≤ t) :
    2 * Real.pi * Real.sqrt t + Real.log t - 8 * (1 / 40) * (Real.log t + (1 / 40) ^ 2 / t) ≤
      Vfield8 t := by
  unfold Vfield8
  have ht0 : 0 < t := by linarith
  have hcont : Continuous fun u : ℝ => Real.log (t + u ^ 2) :=
    (continuous_const.add (continuous_pow 2)).log (fun u => by simp only [Pi.add_apply]; nlinarith [sq_nonneg u])
  have h1 : Real.log t ≤ ∫ u in (0 : ℝ)..1, Real.log (t + u ^ 2) := by
    have e : ∫ u in (0 : ℝ)..1, Real.log t = Real.log t := by simp
    rw [← e]
    refine intervalIntegral.integral_mono_on zero_le_one (by simp) (hcont.intervalIntegrable _ _) ?_
    intro u _
    exact Real.log_le_log ht0 (by nlinarith)
  have h2 : ∫ u in (0 : ℝ)..(1 / 40 : ℝ), Real.log (t + u ^ 2) ≤
      1 / 40 * (Real.log t + (1 / 40 : ℝ) ^ 2 / t) := by
    have e : ∫ u in (0 : ℝ)..(1 / 40), Real.log (t + (1 / 40 : ℝ) ^ 2) =
        1 / 40 * Real.log (t + (1 / 40 : ℝ) ^ 2) := by simp
    have hcg : Continuous fun _ : ℝ => Real.log (t + (1 / 40 : ℝ) ^ 2) :=
      continuous_const.log (fun _ => by positivity)
    have hle : ∫ u in (0 : ℝ)..(1 / 40), Real.log (t + u ^ 2) ≤
        ∫ u in (0 : ℝ)..(1 / 40), Real.log (t + (1 / 40 : ℝ) ^ 2) :=
      intervalIntegral.integral_mono_on (by norm_num) (hcont.intervalIntegrable _ _)
        (hcg.intervalIntegrable _ _) (fun u hu => by
          apply Real.log_le_log (by positivity)
          have hu0 : 0 ≤ u := hu.1
          have : u ≤ 1 / 40 := by simpa using hu.2
          nlinarith [sq_nonneg u])
    have hlog : Real.log (t + (1 / 40 : ℝ) ^ 2) ≤ Real.log t + (1 / 40 : ℝ) ^ 2 / t := by
      have : Real.log (t + (1 / 40 : ℝ) ^ 2) = Real.log t + Real.log (1 + (1 / 40 : ℝ) ^ 2 / t) := by
        rw [← Real.log_mul ht0.ne' (by positivity)]; congr 1; field_simp
      rw [this]
      have := Real.log_le_sub_one_of_pos (by positivity : (0:ℝ) < 1 + (1 / 40 : ℝ) ^ 2 / t)
      linarith
    rw [e] at hle
    linarith
  have h3 : 2 * Real.pi * Real.sqrt t ≤ 2 * Real.pi * Real.sqrt t := le_refl _
  have hlog2 : Real.log (t + (1 / 40 : ℝ) ^ 2) ≤ Real.log t + (1 / 40 : ℝ) ^ 2 / t := by
    have : Real.log (t + (1 / 40 : ℝ) ^ 2) = Real.log t + Real.log (1 + (1 / 40 : ℝ) ^ 2 / t) := by
      rw [← Real.log_mul ht0.ne' (by positivity)]; congr 1; field_simp
    rw [this]
    have := Real.log_le_sub_one_of_pos (by positivity : (0:ℝ) < 1 + (1 / 40 : ℝ) ^ 2 / t)
    linarith
  nlinarith

/-- 带 `c√t` 余量的尾部界（`0 ≤ c ≤ 1/20`）。 -/
lemma potential_ineq_tail8' {t c : ℝ} (ht : 2 ≤ t) (hc0 : 0 ≤ c) (hc : c ≤ 1 / 20) :
    2 * Uρ8 t - Vfield8 t + c * Real.sqrt t ≤ M0_8 := by
  have ht0 : 0 < t := by linarith
  have hU := Uρ8_le_log ht
  have hV := Vfield8_ge_tail ht
  have hs : Real.sqrt t ^ 2 = t := Real.sq_sqrt ht0.le
  have hs0 : 0 < Real.sqrt t := Real.sqrt_pos.mpr ht0
  have hlog : Real.log t ≤ 2 * (Real.sqrt t - 1) := by
    have e : Real.log (Real.sqrt t ^ 2) = 2 * Real.log (Real.sqrt t) := by
      rw [Real.log_pow]; norm_num
    rw [hs] at e
    rw [e]
    linarith [Real.log_le_sub_one_of_pos hs0]
  have hcs : c * Real.sqrt t ≤ 1 / 20 * Real.sqrt t := mul_le_mul_of_nonneg_right hc hs0.le
  have hpi := Real.pi_gt_d2
  have h2 : (1.41 : ℝ) ≤ Real.sqrt t := Real.le_sqrt_of_sq_le (by norm_num; linarith)
  have ht' : (1 : ℝ) / t ≤ 1 / 2 := one_div_le_one_div_of_le (by norm_num) ht
  have hps : (3.14 : ℝ) * Real.sqrt t ≤ Real.pi * Real.sqrt t :=
    mul_le_mul_of_nonneg_right hpi.le hs0.le
  have key : 2 * Uρ8 t - Vfield8 t + c * Real.sqrt t ≤
      (23 / 20 : ℝ) * Real.log t - 2 * Real.pi * Real.sqrt t + (1 / 20) * Real.sqrt t +
        (1 / 5) * ((1 / 40 : ℝ) ^ 2 / t) := by linarith [hU, hV, hcs]
  have key1 : (23 / 20 : ℝ) * Real.log t ≤ (23 / 10) * (Real.sqrt t - 1) := by linarith [hlog]
  have key2 : (157 / 25 : ℝ) * Real.sqrt t ≤ 2 * Real.pi * Real.sqrt t := by linarith [hps]
  have key3 : (1 / 5 : ℝ) * ((1 / 40 : ℝ) ^ 2 / t) ≤ 1 / 16000 := by
    have h1600 : (1 / 40 : ℝ) ^ 2 = 1 / 1600 := by norm_num
    rw [h1600]
    calc (1 / 5 : ℝ) * (1 / 1600 / t) = (1 / 8000) * (1 / t) := by ring
      _ ≤ (1 / 8000) * (1 / 2) := mul_le_mul_of_nonneg_left ht' (by norm_num)
      _ = 1 / 16000 := by norm_num
  show _ ≤ -6.35
  nlinarith [key, key1, key2, key3, h2]

/-- 点态不等式（(6.7) 类比）：`2Uρ8 − V₈ + (2/K)√t ≤ M₀_8 + 3/K`（K ≥ 40）。 -/
lemma pointwise_bound8 {K t : ℝ} (hK : 40 ≤ K) (ht : 0 < t) :
    2 * Uρ8 t - Vfield8 t + 2 / K * Real.sqrt t ≤ M0_8 + 3 / K := by
  have hK0 : 0 < K := by linarith
  rcases le_or_gt t 2 with h | h
  · have h1 := potential_ineq t ht
    have hs : Real.sqrt t ≤ 3 / 2 := by
      rw [Real.sqrt_le_iff]; constructor <;> [norm_num; nlinarith]
    have : 2 / K * Real.sqrt t ≤ 3 / K := by
      rw [show 3 / K = 2 / K * (3 / 2) by ring]
      exact mul_le_mul_of_nonneg_left hs (by positivity)
    exact add_le_add h1 this
  · have h1 := potential_ineq_tail8' (c := 2 / K) h.le (by positivity)
      (by rw [div_le_iff₀ hK0]; linarith)
    have : (0 : ℝ) ≤ 3 / K := by positivity
    linarith

/-- 有序对的双重和 = 2 倍无序对和（通用恒等式）。 -/
lemma sum_pairs_eq {h : ℕ} (t : Fin h → ℝ) :
    ∑ i, ∑ i', Real.log |t i - t i'| = ∑ i, ∑ j ∈ Finset.Ioi i, 2 * Real.log |t j - t i| := by
  have hsplit : ∀ i : Fin h, ∑ i', Real.log |t i - t i'| =
      ∑ i' ∈ Finset.Iio i, Real.log |t i - t i'| + ∑ i' ∈ Finset.Ioi i, Real.log |t i - t i'| := by
    intro i
    have e1 : (Finset.univ : Finset (Fin h)).filter (fun x => x < i) = Finset.Iio i := by
      ext x; simp
    have e2 : (Finset.univ : Finset (Fin h)).filter (fun x => ¬ x < i) = Finset.Ici i := by
      ext x; simp [not_lt]
    rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun x => x < i), e1, e2,
      ← Finset.add_sum_Ioi_eq_sum_Ici, sub_self, abs_zero, Real.log_zero, zero_add]
  simp_rw [hsplit]
  rw [Finset.sum_add_distrib]
  have hcomm : ∑ i, ∑ i' ∈ Finset.Iio i, Real.log |t i - t i'| =
      ∑ i, ∑ i' ∈ Finset.Ioi i, Real.log |t i - t i'| := by
    rw [Finset.sum_comm' (t' := Finset.univ) (s' := fun i' => Finset.Ioi i')]
    · refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun i' _ => ?_
      rw [abs_sub_comm]
    · intro x y
      simp only [Finset.mem_univ, Finset.mem_Iio, Finset.mem_Ioi, true_and, and_true]
  rw [hcomm, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [abs_sub_comm]; ring

/-- **式 (6.9) 类比**（b=8 常数）。 -/
theorem energy_ineq_final8 (n : ℕ) (hn : 0 < n) (t : Fin (39 * n) → ℝ) (ht : ∀ i, 0 < t i)
    (hinj : Function.Injective t) :
    (∑ i, ∑ j ∈ Finset.Ioi i, 2 * Real.log |t j - t i|) - Kr n * ∑ i, Vfield8 (t i) +
        ∑ i, Real.sqrt (t i) ≤
      (lam8 * M0_8 - Irho8) * Kr n ^ 2 + 5 * (39 * n) + 6 * (39 * n) * Real.log (Kr n) := by
  have hK : 40 ≤ Kr n := by
    simp only [Kr]; have : (1 : ℝ) ≤ n := by exact_mod_cast hn
    linarith
  have hK0 : 0 < Kr n := by linarith
  set K := Kr n with hKdef
  set ε : ℝ := K ^ (-6 : ℤ) with hε_def
  have hε : 0 < ε := by rw [hε_def]; positivity
  have hε1 : ε ≤ 1 := by
    rw [hε_def, zpow_neg, inv_le_one_iff₀]
    right; exact one_le_zpow₀ (by linarith) (by norm_num)
  have hsqrtε : Real.sqrt ε = K ^ (-3 : ℤ) := by
    have e : (K ^ (-3 : ℤ)) ^ 2 = ε := by
      rw [hε_def, ← zpow_natCast, ← zpow_mul]; norm_num
    rw [← e, Real.sqrt_sq (by positivity)]
  have hlogε : Real.log ε = -6 * Real.log K := by
    rw [hε_def, Real.log_zpow]; push_cast; ring
  have hraw := energy_raw n hn t hinj hε
  rw [← hKdef, sum_pairs_eq, hlogε] at hraw
  have hErr : ∀ i, Err8 ε (t i) ≤ 1 / K ^ 3 * (622 * Real.sqrt (t i) + 1421) := fun i => by
    have := Err_le8 hε hε1 (ht i)
    rw [hsqrtε, zpow_neg, zpow_ofNat] at this
    rw [one_div]; exact this
  have hK2 : 1 / K ^ 2 ≤ 1 / 1600 :=
    one_div_le_one_div_of_le (by norm_num) (by nlinarith)
  have hpt : ∀ i, 2 * K * (Uρ8 (t i) + Err8 ε (t i)) - K * Vfield8 (t i) + Real.sqrt (t i) ≤
      K * M0_8 + 5 := by
    intro i
    have h1 := pointwise_bound8 hK (ht i)
    have h2 := hErr i
    have hs := Real.sqrt_nonneg (t i)
    have e1 : 2 * K * (1 / K ^ 3 * (622 * Real.sqrt (t i) + 1421)) =
        1 / K ^ 2 * (1244 * Real.sqrt (t i) + 2842) := by field_simp; ring
    have e2 : 1 / K ^ 2 * (1244 * Real.sqrt (t i) + 2842) ≤
        1 / 1600 * (1244 * Real.sqrt (t i) + 2842) :=
      mul_le_mul_of_nonneg_right hK2 (by positivity)
    have e3 : K * (2 / K * Real.sqrt (t i)) = 2 * Real.sqrt (t i) := by field_simp
    have e4 : K * (3 / K) = 3 := by field_simp
    have h1' := mul_le_mul_of_nonneg_left h1 hK0.le
    rw [mul_add, mul_add, mul_sub, e3, e4] at h1'
    have h2' := mul_le_mul_of_nonneg_left h2 (by positivity : (0:ℝ) ≤ 2 * K)
    rw [e1] at h2'
    nlinarith
  have hsum := Finset.sum_le_sum fun i (_ : i ∈ Finset.univ) => hpt i
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, ← Finset.mul_sum] at hsum
  simp only [Finset.sum_add_distrib] at hraw
  have hlam : ((39 * n : ℕ) : ℝ) * (K * M0_8) = lam8 * M0_8 * K ^ 2 := by
    rw [hKdef]; simp only [Kr, lam8]; push_cast; ring
  rw [hlam] at hsum
  push_cast at hraw hsum ⊢
  linarith [hraw, hsum]

end Zeta7
