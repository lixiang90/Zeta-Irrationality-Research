import Mathlib
import Zeta7.Weight
import Zeta7.Moments
import Zeta7.PartialFractions
import Zeta7.Zeta7Def
import Zeta7.HermiteFormula

/-!
# Proposition 2.2-类比（s = 7）：矩表示与 `Δ_n(ζ(7)) > 0`

镜像 `Apery/Positivity.lean`（mo271，Apache-2.0），s = 5 → s = 7：

* `pole_moment` : Hermite 公式在 `s = 7`，
  `∫₀^∞ w(y) / (y² + j²) dy = j⁶ (ζ(7) - H_j^{(7)}) - 1/6 + 1/(2j)` —— 已在
  `Zeta7.HermiteFormula` 中证明（六次分部积分 + Mittag-Leffler 展开）；
* `moment_rep` : `μ_{ζ(7)}(P / D_K) = ∫₀^∞ (P / D_K)(y²) w(y) dy` 且可积，
  由多项式矩（`mono_moment`）、极点矩与部分分式合成；
* `Δ_pos` : `Δ_n(ζ(7)) > 0`，因为 `G_n(ζ(7))` 是正权的 Gram 矩阵。
-/

open Polynomial MeasureTheory Set Finset
open scoped Matrix

namespace Zeta7

/-- **Hermite 公式（s = 7）**（Proposition 2.2-类比的极点矩），证明见
`Zeta7.HermiteFormula`。 -/
theorem pole_moment (j : ℕ) (hj : 1 ≤ j) :
    ∫ y in Ioi 0, w y / (y ^ 2 + (j : ℝ) ^ 2) =
      (j : ℝ) ^ 6 * (zeta7 - (H7 j : ℝ)) - 1 / 6 + 1 / (2 * (j : ℝ)) :=
  hermite_pole j hj

/-- 被积函数 `w(y) / (y² + j²)` 在 `(0, ∞)` 上可积（以 `w` 的指数衰减界控制）。
Mathlib 无 `integrableOn_pow_mul_exp_neg_mul`，改用 `integrableOn_rpow_mul_exp_neg_rpow`
（`s := ↑e`、`p := 1`），再化 `rpow` 为 `pow`。 -/
lemma integrableOn_pole (j : ℕ) (hj : 1 ≤ j) :
    IntegrableOn (fun y => w y / (y ^ 2 + (j : ℝ) ^ 2)) (Ioi 0) := by
  have h1 : IntegrableOn (fun y : ℝ => y ^ 1 * Real.exp (-(Real.pi * y))) (Ioi 0) := by
    have h := integrableOn_rpow_mul_exp_neg_mul_rpow (s := ((1 : ℕ) : ℝ)) (p := (1 : ℝ))
      (b := Real.pi) (by norm_num) zero_lt_one Real.pi_pos
    convert h using 1
    ext y
    simp only [Nat.cast_one, Real.rpow_one, pow_one]
    congr 1
    ring
  have h0 : IntegrableOn (fun y : ℝ => y ^ 0 * Real.exp (-(Real.pi * y))) (Ioi 0) := by
    have h := integrableOn_rpow_mul_exp_neg_mul_rpow (s := ((0 : ℕ) : ℝ)) (p := (1 : ℝ))
      (b := Real.pi) (by norm_num) zero_lt_one Real.pi_pos
    convert h using 1
    ext y
    simp only [Nat.cast_zero, Real.rpow_zero, pow_zero, Real.rpow_one]
    congr 1
    ring
  have hg : IntegrableOn (fun y : ℝ => 128 * (y ^ 1 * Real.exp (-(Real.pi * y))) +
      41 * (y ^ 0 * Real.exp (-(Real.pi * y)))) (Ioi 0) :=
    (h1.const_mul 128).add (h0.const_mul 41)
  have hj' : (1 : ℝ) ≤ j := by exact_mod_cast hj
  refine hg.mono' (aemeasurable_w.div (by fun_prop : Measurable fun y : ℝ => y ^ 2 + (j : ℝ) ^ 2).aemeasurable).aestronglyMeasurable ?_
  refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
  have hy : 0 < y := hy
  have hw := w_pos hy
  have hden : (1 : ℝ) ≤ y ^ 2 + (j : ℝ) ^ 2 := by nlinarith
  rw [Real.norm_of_nonneg (div_nonneg hw.le (by positivity))]
  calc w y / (y ^ 2 + (j : ℝ) ^ 2) ≤ w y := div_le_self hw.le hden
    _ ≤ (128 * y + 41) * Real.exp (-(Real.pi * y)) := w_le hy
    _ = _ := by ring

/-- `P(y²) / D_K(y²) · w(y)`。 -/
noncomputable def integrand (K : ℕ) (P : ℚ[X]) (y : ℝ) : ℝ :=
  aeval (y ^ 2) P / aeval (y ^ 2) (D K) * w y

/-- 被积函数在 `y > 0` 处的逐点分解。 -/
lemma integrand_eq_sum (K : ℕ) (P : ℚ[X]) {y : ℝ} (hy : 0 < y) :
    integrand K P y =
      (∑ e ∈ range ((P /ₘ D K).natDegree + 1),
          ((P /ₘ D K).coeff e : ℝ) * (y ^ (2 * e) * w y)) +
        ∑ j ∈ Icc 1 K, (res K P j : ℝ) * (w y / (y ^ 2 + (j : ℝ) ^ 2)) := by
  unfold integrand
  rw [partial_fractions K P (t := y ^ 2) (by positivity), aeval_eq_sum_range, add_mul,
    Finset.sum_mul, Finset.sum_mul]
  congr 1
  · refine Finset.sum_congr rfl fun e _ => ?_
    try simp only [Rat.smul_def, eq_ratCast, ← pow_mul]
    ring
  · refine Finset.sum_congr rfl fun j _ => ?_
    ring

/-- `μ_{ζ(7)}(P / D_K)` 用商多项式系数与留数表示。 -/
lemma aeval_μX (K : ℕ) (P : ℚ[X]) :
    aeval zeta7 (μX K P) =
      (∑ e ∈ range ((P /ₘ D K).natDegree + 1), ((P /ₘ D K).coeff e : ℝ) * (μmono e : ℝ)) +
        ∑ j ∈ Icc 1 K, (res K P j : ℝ) *
          ((j : ℝ) ^ 6 * (zeta7 - (H7 j : ℝ)) - 1 / 6 + 1 / (2 * (j : ℝ))) := by
  simp only [μX, map_add, aeval_C, map_sum, map_mul, poleValue, map_sub, aeval_X, eq_ratCast]
  congr 1
  · unfold μpoly
    rw [Polynomial.sum_over_range' _ (fun n => by simp) _ (Nat.lt_succ_self _)]
    push_cast
    rfl
  · refine Finset.sum_congr rfl fun j _ => ?_
    simp only [res]
    push_cast
    ring

/-- **Proposition 2.2-类比**（矩表示）：对每个多项式 `P`，`(P / D_K)(y²) w(y)`
在 `(0, ∞)` 上可积且其积分等于 `μ_{ζ(7)}(P / D_K)`。 -/
theorem moment_rep (K : ℕ) (P : ℚ[X]) :
    IntegrableOn (integrand K P) (Ioi 0) ∧
      aeval zeta7 (μX K P) = ∫ y in Ioi 0, integrand K P y := by
  set Q := P /ₘ D K with hQ
  have hint1 : ∀ e ∈ range (Q.natDegree + 1),
      IntegrableOn (fun y => (Q.coeff e : ℝ) * (y ^ (2 * e) * w y)) (Ioi 0) :=
    fun e _ => (mono_moment e).1.const_mul _
  have hint2 : ∀ j ∈ Finset.Icc 1 K,
      IntegrableOn (fun y => (res K P j : ℝ) * (w y / (y ^ 2 + (j : ℝ) ^ 2))) (Ioi 0) :=
    fun j hj => (integrableOn_pole j (Finset.mem_Icc.mp hj).1).const_mul _
  have hsumint : IntegrableOn (fun y =>
      (∑ e ∈ range (Q.natDegree + 1), (Q.coeff e : ℝ) * (y ^ (2 * e) * w y)) +
        ∑ j ∈ Icc 1 K, (res K P j : ℝ) * (w y / (y ^ 2 + (j : ℝ) ^ 2))) (Ioi 0) :=
    (integrable_finsetSum _ hint1).add (integrable_finsetSum _ hint2)
  have hEq : EqOn (fun y =>
      (∑ e ∈ range (Q.natDegree + 1), (Q.coeff e : ℝ) * (y ^ (2 * e) * w y)) +
        ∑ j ∈ Icc 1 K, (res K P j : ℝ) * (w y / (y ^ 2 + (j : ℝ) ^ 2))) (integrand K P) (Ioi 0) :=
    fun y hy => (integrand_eq_sum K P hy).symm
  refine ⟨hsumint.congr_fun hEq measurableSet_Ioi, ?_⟩
  rw [← setIntegral_congr_fun measurableSet_Ioi hEq, integral_add (integrable_finsetSum _ hint1)
    (integrable_finsetSum _ hint2), integral_finsetSum _ hint1, integral_finsetSum _ hint2,
    aeval_μX]
  congr 1
  · refine Finset.sum_congr rfl fun e _ => ?_
    rw [integral_const_mul, (mono_moment e).2]
  · refine Finset.sum_congr rfl fun j hj => ?_
    rw [integral_const_mul, pole_moment j (Finset.mem_Icc.mp hj).1]

/-- 正权 `ν(y) = D_{3n}(y²)⁸ / D_{40n}(y²) · w(y)`（b=8 故幂次 8）。 -/
noncomputable def ν (n : ℕ) (y : ℝ) : ℝ :=
  aeval (y ^ 2) (D n) ^ 8 / aeval (y ^ 2) (D (40 * n)) * w y

lemma ν_pos (n : ℕ) {y : ℝ} (hy : 0 < y) : 0 < ν n y := by
  unfold ν
  have h1 := aeval_D_pos n (t := y ^ 2) (by positivity)
  have h2 := aeval_D_pos (40 * n) (t := y ^ 2) (by positivity)
  have h3 := w_pos hy
  positivity

lemma integrand_eq (n : ℕ) (i j : ℕ) (y : ℝ) :
    integrand (40 * n) (D n ^ 8 * X ^ (i + j)) y =
      (y ^ 2) ^ i * (y ^ 2) ^ j * ν n y := by
  simp only [integrand, ν, map_mul, map_pow, aeval_X]
  rw [pow_add]; ring

set_option maxHeartbeats 800000 in
/-- **正性**：`Δ_n(ζ(7)) > 0`，来自矩表示。 -/
theorem Δ_pos (n : ℕ) (_hn : 0 < n) : 0 < aeval zeta7 (Δ n) := by
  have hdet : aeval zeta7 (Δ n) = ((G n).map (aeval zeta7)).det := by
    have := RingHom.map_det (aeval zeta7 : ℚ[X] →ₐ[ℚ] ℝ).toRingHom (G n)
    simpa [Δ, RingHom.mapMatrix_apply] using this
  rw [hdet]
  have hentry : ∀ i j : Fin (39 * n),
      ((G n).map (aeval zeta7)) i j =
        ∫ y in Ioi 0, integrand (40 * n) (D n ^ 8 * X ^ ((i : ℕ) + (j : ℕ))) y := by
    intro i j
    rw [Matrix.map_apply]
    exact (moment_rep _ _).2
  have hint : ∀ i j : Fin (39 * n),
      IntegrableOn (integrand (40 * n) (D n ^ 8 * X ^ ((i : ℕ) + (j : ℕ)))) (Ioi 0) :=
    fun i j => (moment_rep _ _).1
  apply Matrix.PosDef.det_pos
  refine Matrix.PosDef.of_dotProduct_mulVec_pos ?_ ?_
  · refine Matrix.IsHermitian.ext fun i j => ?_
    simp only [star_trivial, Matrix.map_apply, G]
    rw [Nat.add_comm (j : ℕ) i]
  · intro x hx
    set f : Fin (39 * n) → Fin (39 * n) → ℝ → ℝ := fun i j y =>
      x i * x j * integrand (40 * n) (D n ^ 8 * X ^ ((i : ℕ) + (j : ℕ))) y with hf
    have hfint : ∀ i j, IntegrableOn (f i j) (Ioi 0) := fun i j => (hint i j).const_mul _
    have hpt : ∀ y, ∑ i, ∑ j, f i j y = (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y := by
      intro y
      simp only [hf, integrand_eq]
      rw [sq (∑ i, x i * (y ^ 2) ^ (i : ℕ)), Finset.sum_mul_sum, Finset.sum_mul]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [Finset.sum_mul]
      refine Finset.sum_congr rfl fun j _ => ?_
      ring
    have hq : star x ⬝ᵥ ((G n).map (aeval zeta7) *ᵥ x) =
        ∫ y in Ioi 0, (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y := by
      have h1 : star x ⬝ᵥ ((G n).map (aeval zeta7) *ᵥ x) = ∑ i, ∑ j, ∫ y in Set.Ioi 0, f i j y := by
        simp only [dotProduct, Matrix.mulVec, star_trivial, hentry, hf, Finset.mul_sum]
        refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
        rw [integral_const_mul]; ring
      rw [h1]
      have h2 : ∀ i, ∑ j, ∫ y in Set.Ioi 0, f i j y = ∫ y in Set.Ioi 0, ∑ j, f i j y :=
        fun i => (integral_finsetSum _ (fun j _ => hfint i j)).symm
      simp_rw [h2]
      rw [← integral_finsetSum _ (fun i _ => integrable_finsetSum _ (fun j _ => hfint i j))]
      exact integral_congr_ae (Filter.Eventually.of_forall fun y => hpt y)
    rw [hq]
    have hsq : IntegrableOn (fun y => (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y) (Ioi 0) := by
      have : (fun y => (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y) = fun y => ∑ i, ∑ j, f i j y :=
        funext fun y => (hpt y).symm
      rw [this]
      exact integrable_finsetSum _ fun i _ => integrable_finsetSum _ fun j _ => hfint i j
    have hnn : 0 ≤ᵐ[volume.restrict (Ioi 0)]
        fun y => (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y := by
      refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
      exact mul_nonneg (sq_nonneg _) (ν_pos n hy).le
    rw [setIntegral_pos_iff_support_of_nonneg_ae hnn hsq]
    set q : ℝ[X] := ∑ i : Fin (39 * n), C (x i) * X ^ (i : ℕ) with hqdef
    have hqeval : ∀ y : ℝ, q.eval (y ^ 2) = ∑ i, x i * (y ^ 2) ^ (i : ℕ) := by
      intro y; simp [hqdef, eval_finsetSum]
    have hq0 : q ≠ 0 := by
      intro h0
      apply hx
      funext i
      have hc : q.coeff (i : ℕ) = x i := by
        simp only [hqdef, finsetSum_coeff, coeff_C_mul_X_pow]
        rw [Finset.sum_eq_single i]
        · simp
        · intro b _ hb; rw [if_neg]; exact fun h => hb (Fin.ext h.symm)
        · intro h; exact absurd (Finset.mem_univ i) h
      rw [← hc, h0, coeff_zero]; rfl
    have hroots : Set.Finite {t : ℝ | IsRoot q t} := Polynomial.finite_setOfPred_isRoot hq0
    have hB : Set.Finite {y : ℝ | IsRoot q (y ^ 2)} := by
      refine (hroots.image Real.sqrt |>.union (hroots.image fun t => -Real.sqrt t)).subset ?_
      intro y hy
      simp only [Set.mem_ofPred_eq] at hy
      rcases le_or_gt 0 y with h | h
      · exact Or.inl ⟨y ^ 2, hy, Real.sqrt_sq h⟩
      · exact Or.inr ⟨y ^ 2, hy, by
          show -Real.sqrt (y ^ 2) = y
          rw [Real.sqrt_sq_eq_abs, abs_of_neg h, neg_neg]⟩
    have hsub : Set.Ioi 0 \ {y : ℝ | IsRoot q (y ^ 2)} ⊆
        Function.support (fun y => (∑ i, x i * (y ^ 2) ^ (i : ℕ)) ^ 2 * ν n y) ∩ Set.Ioi 0 := by
      intro y hy
      obtain ⟨hy0, hyB⟩ := hy
      refine ⟨?_, hy0⟩
      simp only [Function.mem_support]
      have hqy : q.eval (y ^ 2) ≠ 0 := fun h => hyB h
      rw [hqeval] at hqy
      exact mul_ne_zero (pow_ne_zero _ hqy) (ν_pos n hy0).ne'
    calc (0 : ENNReal) < ⊤ := ENNReal.zero_lt_top
      _ = volume (Set.Ioi (0 : ℝ) \ {y : ℝ | IsRoot q (y ^ 2)}) := by
        rw [measure_sdiff_null (hB.measure_zero volume), Real.volume_Ioi]
      _ ≤ _ := measure_mono hsub

end Zeta7
