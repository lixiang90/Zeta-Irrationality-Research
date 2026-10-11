import Mathlib
import Apery.Energy
import Zeta7.Positivity
import Zeta7.DetIntegral
import Zeta7.EnergyFinal8
import Zeta7.Field8

/-!
# 能量界 (6.14) 类比（b=8, (K:N:h) = 40:1:39）

镜像 `Apery/EnergyBound.lean`：

* `integrand_le8`：被积函数的点态界（Vandermonde² · ∏ν ≤ exp(Aconst8)·∏gK₈）；
* `log_Δ_le'8`：(6.14)-类比，`log Δ_K(ζ(7)) ≤ 2h(h + b·N − K)·log K + (λM₀ − I(ρ))·K² + O(h·log K) + O(h)`，
  其中 h = 39n, K = 40n, b·N = 8n。

b=8 差异（相对 mo271 的 b=6）：ν 的分子为 `D_N(y²)⁸`（幂 8），权重 `w` 的界为
`log w ≤ 6 + log(1 + 2πy) − πy`（衰减率 π 而非 2π），gK₈ 为 `(1 + 2πy)·e^{−y/K}`。
-/

open Filter Topology Set MeasureTheory Finset Polynomial

namespace Zeta7

lemma aeval_D_eq8 (m : ℕ) (s : ℝ) : aeval s (D m) = ∏ j ∈ Icc 1 m, (s + (j : ℝ) ^ 2) := by
  simp only [D, map_prod, map_add, aeval_X, aeval_C, eq_ratCast, Rat.cast_pow, Rat.cast_natCast]

lemma sum_Ioi_card_mul_two8 (h : ℕ) : (∑ i : Fin h, (Finset.Ioi i).card) * 2 = h * (h - 1) := by
  simp only [Fin.card_Ioi]
  rw [Fin.sum_univ_eq_sum_range (fun i => h - 1 - i) h, Finset.sum_range_reflect (fun i => i) h,
    Finset.sum_range_id_mul_two]

lemma sum_Ioi_const8 (h : ℕ) (c : ℝ) :
    ∑ i : Fin h, ∑ _j ∈ Finset.Ioi i, c = (h : ℝ) * ((h : ℝ) - 1) / 2 * c := by
  simp only [Finset.sum_const, nsmul_eq_mul, ← Finset.sum_mul]
  have := sum_Ioi_card_mul_two8 h
  rcases Nat.eq_zero_or_pos h with rfl | hh
  · simp
  have hcast : ((∑ i : Fin h, (Finset.Ioi i).card : ℕ) : ℝ) = (h : ℝ) * ((h : ℝ) - 1) / 2 := by
    have h2 : (((∑ i : Fin h, (Finset.Ioi i).card) * 2 : ℕ) : ℝ) = ((h * (h - 1) : ℕ) : ℝ) := by
      rw [this]
    push_cast [Nat.cast_sub (by omega : 1 ≤ h)] at h2 ⊢
    linarith
  rw [← hcast]
  push_cast
  ring

/-- `log D_m(y²) = 2m log K + ∑_{j<m} log(t + ((j+1)/K)²)`，`t = (y/K)²`（Zeta7 的 `D`）。 -/
lemma log_aeval_D8 (m : ℕ) {K y : ℝ} (hK : 0 < K) (hy : 0 < y) :
    Real.log (aeval (y ^ 2) (D m)) =
      2 * m * Real.log K + ∑ j ∈ range m, Real.log ((y / K) ^ 2 + (((j : ℝ) + 1) / K) ^ 2) := by
  rw [aeval_D_eq8, Real.log_prod (fun j _ => by positivity), sum_Icc_eq_sum_range']
  have : ∀ j : ℕ, Real.log (y ^ 2 + ((j + 1 : ℕ) : ℝ) ^ 2) =
      2 * Real.log K + Real.log ((y / K) ^ 2 + (((j : ℝ) + 1) / K) ^ 2) := by
    intro j
    have e : y ^ 2 + ((j + 1 : ℕ) : ℝ) ^ 2 = K ^ 2 * ((y / K) ^ 2 + (((j : ℝ) + 1) / K) ^ 2) := by
      push_cast; field_simp
    rw [e, Real.log_mul (by positivity) (by positivity), Real.log_pow]
    push_cast; ring
  simp_rw [this]
  rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
  ring

/-- `∀ ℓ, (ℓ+1)^6 ≤ M₈·(3/2)^ℓ`，`M₈ = 15^6·2^14/3^14 = 186624000000/4782969`
（`f(ℓ) = (ℓ+1)^6/(3/2)^ℓ` 在 `ℓ = 14` 取最大值：比值 `((ℓ+2)/(ℓ+1))^6 ≤ 3/2` 对 `ℓ ≥ 14`）。 -/
lemma pow_six_le_M8 : ∀ ℓ : ℕ, ((ℓ : ℝ) + 1) ^ 6 ≤ (186624000000 / 4782969 : ℝ) * (3 / 2 : ℝ) ^ ℓ := by
  intro ℓ
  rcases lt_or_ge ℓ 14 with h | h
  · interval_cases ℓ <;> norm_num
  · refine Nat.le_induction ?_ ?_ _ h
    · norm_num
    · intro m hm ih
      have hm14 : (14 : ℝ) ≤ m := by exact_mod_cast hm
      have h1 : ((m : ℝ) + 2) / ((m : ℝ) + 1) ≤ 16 / 15 := by
        rw [div_le_div_iff₀ (by positivity) (by norm_num)]
        nlinarith
      have h2 : (((m : ℝ) + 2) / ((m : ℝ) + 1)) ^ 6 ≤ (3 / 2 : ℝ) := by
        calc (((m : ℝ) + 2) / ((m : ℝ) + 1)) ^ 6 ≤ (16 / 15 : ℝ) ^ 6 :=
              pow_le_pow_left₀ (by positivity) h1 6
          _ ≤ 3 / 2 := by norm_num
      calc (((m + 1 : ℕ) : ℝ) + 1) ^ 6 = ((m : ℝ) + 2) ^ 6 := by push_cast; ring
        _ = (((m : ℝ) + 2) / ((m : ℝ) + 1)) ^ 6 * ((m : ℝ) + 1) ^ 6 := by
            field_simp
        _ ≤ (3 / 2 : ℝ) * ((186624000000 / 4782969 : ℝ) * (3 / 2 : ℝ) ^ m) :=
            mul_le_mul h2 ih (pow_nonneg (by positivity) _) (by norm_num)
        _ = (186624000000 / 4782969 : ℝ) * (3 / 2 : ℝ) ^ (m + 1) := by push_cast; ring

/-- `y ≥ 1/10` 时 `wS` 的尖锐界：`wS y ≤ 16·M₈·e^{−2πy}`。 -/
lemma wS_le_sharp8 {y : ℝ} (hy : (1 / 10 : ℝ) ≤ y) :
    wS y ≤ (16 * 186624000000 / 4782969 : ℝ) * Real.exp (-(2 * Real.pi * y)) := by
  have hpi3 : (3 : ℝ) ≤ Real.pi := Real.pi_gt_three.le
  have hy0 : (0 : ℝ) ≤ y := by linarith
  have h1 : (3 / 5 : ℝ) ≤ 2 * Real.pi * y := by nlinarith [Real.pi_pos]
  have hx : Real.exp (-(2 * Real.pi * y)) ≤ 5 / 8 := by
    have h2 : Real.exp (-(2 * Real.pi * y)) ≤ Real.exp (-(3 / 5 : ℝ)) :=
      Real.exp_le_exp.mpr (by linarith)
    have h3 : Real.exp (-(3 / 5 : ℝ)) ≤ 5 / 8 := by
      have h4 : (8 / 5 : ℝ) ≤ Real.exp (3 / 5) := by
        have := Real.add_one_le_exp (3 / 5 : ℝ)
        linarith
      rw [Real.exp_neg]
      have h5 := inv_anti₀ (show (0 : ℝ) < 8 / 5 by norm_num) h4
      rwa [inv_div] at h5
    exact h2.trans h3
  have key : ∀ ℓ : ℕ, ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) ≤
      (186624000000 / 4782969 : ℝ) * ((15 / 16 : ℝ) ^ ℓ * Real.exp (-(2 * Real.pi * y))) := by
    intro ℓ
    have hxl : Real.exp (-(2 * Real.pi * y)) ^ ℓ ≤ (5 / 8 : ℝ) ^ ℓ :=
      pow_le_pow_left₀ (Real.exp_pos _).le hx ℓ
    have he : Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) =
        Real.exp (-(2 * Real.pi * y)) * Real.exp (-(2 * Real.pi * y)) ^ ℓ := by
      rw [← Real.exp_nat_mul, ← Real.exp_add]
      congr 1
      push_cast
      ring
    calc ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y))
        = (((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * y)) ^ ℓ) *
            Real.exp (-(2 * Real.pi * y)) := by rw [he]; ring
      _ ≤ ((186624000000 / 4782969 : ℝ) * (3 / 2 : ℝ) ^ ℓ * (5 / 8 : ℝ) ^ ℓ) *
            Real.exp (-(2 * Real.pi * y)) := by
          have h3 : ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * y)) ^ ℓ ≤
              (186624000000 / 4782969 : ℝ) * (3 / 2 : ℝ) ^ ℓ * (5 / 8 : ℝ) ^ ℓ :=
            mul_le_mul (pow_six_le_M8 ℓ) hxl (pow_nonneg (Real.exp_pos _).le _)
              (by positivity)
          exact mul_le_mul_of_nonneg_right h3 (Real.exp_pos _).le
      _ = (186624000000 / 4782969 : ℝ) * ((15 / 16 : ℝ) ^ ℓ * Real.exp (-(2 * Real.pi * y))) := by
          have e2 : (3 / 2 : ℝ) ^ ℓ * (5 / 8 : ℝ) ^ ℓ = (15 / 16 : ℝ) ^ ℓ := by
            rw [← mul_pow]; congr 1; norm_num
          rw [← e2]; ring
  have hgeom : Summable fun ℓ : ℕ => (15 / 16 : ℝ) ^ ℓ :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  calc wS y = ∑' ℓ : ℕ, ((ℓ : ℝ) + 1) ^ 6 * Real.exp (-(2 * Real.pi * ((ℓ : ℝ) + 1) * y)) := rfl
    _ ≤ ∑' ℓ : ℕ, (186624000000 / 4782969 : ℝ) *
          ((15 / 16 : ℝ) ^ ℓ * Real.exp (-(2 * Real.pi * y))) :=
        (summable_w_term (by positivity)).tsum_le_tsum key
          (Summable.mul_left _ (hgeom.mul_right _))
    _ = (186624000000 / 4782969 : ℝ) * (∑' ℓ : ℕ, (15 / 16 : ℝ) ^ ℓ) *
          Real.exp (-(2 * Real.pi * y)) := by
        rw [tsum_mul_left, tsum_mul_right]
        ring
    _ = (16 * 186624000000 / 4782969 : ℝ) * Real.exp (-(2 * Real.pi * y)) := by
        rw [tsum_geometric_of_lt_one (by norm_num) (by norm_num)]
        norm_num

/-- `y ≥ 1/10` 时 `w` 的尖锐界：`w y ≤ 300·(1+2πy)^7·e^{−2πy}`。 -/
lemma w_sharp8 {y : ℝ} (hy : (1 / 10 : ℝ) ≤ y) :
    w y ≤ 300 * (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(2 * Real.pi * y)) := by
  have hs := wS_le_sharp8 hy
  have hpi := Real.pi_gt_d2.le
  have hy0 : (0 : ℝ) ≤ y := by linarith
  have h2pi0 : (2 : ℝ) * Real.pi ≠ 0 := by positivity
  have ht : 0 ≤ (1 + 2 * Real.pi * y) ^ 7 := pow_nonneg (by positivity) 7
  have hfac : (16 * 186624000000 / 4782969 : ℝ) / (720 * Real.pi) ≤ 300 := by
    rw [div_le_iff₀ (by positivity)]
    calc (16 * 186624000000 / 4782969 : ℝ) ≤ 624358 := by norm_num
      _ ≤ 216000 * 3.14 := by norm_num
      _ ≤ 216000 * Real.pi := mul_le_mul_of_nonneg_left hpi (by norm_num)
      _ = 300 * (720 * Real.pi) := by ring
  have hy7' : y ^ 7 ≤ (1 + 2 * Real.pi * y) ^ 7 / (2 * Real.pi) ^ 7 := by
    rw [le_div_iff₀ (pow_pos (by positivity) 7)]
    calc y ^ 7 * (2 * Real.pi) ^ 7 = (2 * Real.pi * y) ^ 7 := by ring
      _ ≤ (1 + 2 * Real.pi * y) ^ 7 :=
          pow_le_pow_left₀ (by positivity) (by linarith [Real.pi_pos]) 7
  have key : (2 * Real.pi) ^ 6 * y ^ 7 * (16 * 186624000000 / 4782969 : ℝ) / 360 ≤
      300 * (1 + 2 * Real.pi * y) ^ 7 := by
    have step1 : ((2 * Real.pi) ^ 6 * y ^ 7) * ((16 * 186624000000 / 4782969 : ℝ) / 360) ≤
        ((2 * Real.pi) ^ 6 * ((1 + 2 * Real.pi * y) ^ 7 / (2 * Real.pi) ^ 7)) *
          ((16 * 186624000000 / 4782969 : ℝ) / 360) :=
      mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hy7' (show (0 : ℝ) ≤ (2 * Real.pi) ^ 6 by positivity))
        (show (0 : ℝ) ≤ (16 * 186624000000 / 4782969 : ℝ) / 360 by positivity)
    rw [show ((2 * Real.pi) ^ 6 * y ^ 7) * ((16 * 186624000000 / 4782969 : ℝ) / 360) =
        (2 * Real.pi) ^ 6 * y ^ 7 * (16 * 186624000000 / 4782969 : ℝ) / 360 by ring,
      show ((2 * Real.pi) ^ 6 * ((1 + 2 * Real.pi * y) ^ 7 / (2 * Real.pi) ^ 7)) *
          ((16 * 186624000000 / 4782969 : ℝ) / 360) =
        (16 * 186624000000 / 4782969 : ℝ) / (720 * Real.pi) * (1 + 2 * Real.pi * y) ^ 7 by
        field_simp
        ring] at step1
    exact step1.trans (mul_le_mul_of_nonneg_right hfac ht)
  calc w y = (2 * Real.pi) ^ 6 * y ^ 7 / 360 * wS y := rfl
    _ ≤ (2 * Real.pi) ^ 6 * y ^ 7 / 360 *
        ((16 * 186624000000 / 4782969 : ℝ) * Real.exp (-(2 * Real.pi * y))) :=
        mul_le_mul_of_nonneg_left hs (by positivity)
    _ = ((2 * Real.pi) ^ 6 * y ^ 7 * (16 * 186624000000 / 4782969 : ℝ) / 360) *
          Real.exp (-(2 * Real.pi * y)) := by ring
    _ ≤ (300 * (1 + 2 * Real.pi * y) ^ 7) * Real.exp (-(2 * Real.pi * y)) :=
        mul_le_mul_of_nonneg_right key (Real.exp_pos _).le
    _ = 300 * (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(2 * Real.pi * y)) := by ring

/-- `log 169 ≤ 6`。 -/
lemma log_169_le_six : Real.log 169 ≤ 6 := by
  rw [Real.log_le_iff_le_exp (by norm_num)]
  have he : (2.7182818283 : ℝ) ^ 6 ≤ Real.exp 6 := by
    have h1 : (2.7182818283 : ℝ) < Real.exp 1 := Real.exp_one_gt_d9
    have e : Real.exp 6 = Real.exp 1 ^ 6 := by rw [← Real.exp_nat_mul]; norm_num
    rw [e]
    exact pow_le_pow_left₀ (by norm_num) h1.le 6
  calc (169 : ℝ) ≤ 2.7182818283 ^ 6 := by norm_num
    _ ≤ Real.exp 6 := he

/-- `log 300 ≤ 6`。 -/
lemma log_300_le_six : Real.log 300 ≤ 6 := by
  rw [Real.log_le_iff_le_exp (by norm_num)]
  have he : (2.7182818283 : ℝ) ^ 6 ≤ Real.exp 6 := by
    have h1 : (2.7182818283 : ℝ) < Real.exp 1 := Real.exp_one_gt_d9
    have e : Real.exp 6 = Real.exp 1 ^ 6 := by rw [← Real.exp_nat_mul]; norm_num
    rw [e]
    exact pow_le_pow_left₀ (by norm_num) h1.le 6
  calc (300 : ℝ) ≤ 2.7182818283 ^ 6 := by norm_num
    _ ≤ Real.exp 6 := he

/-- **b=8 权重界（统一）**：`log w(y) ≤ 6 + π/10 + 7·log(1 + 2πy) − 2πy`（`y > 0`）。
`y ≥ 1/10` 用尖锐界（`w_sharp8`），`y < 1/10` 用粗糙界加 `π/10` 余量。 -/
lemma w_log_le8 {y : ℝ} (hy : 0 < y) :
    Real.log (w y) ≤ 6 + Real.pi / 10 + 7 * Real.log (1 + 2 * Real.pi * y) - 2 * Real.pi * y := by
  rcases le_or_gt y (1 / 10) with h | h
  · -- 粗糙区域：`−πy ≤ −2πy + π/10`
    have h1 : w y ≤ (128 * y + 41) * Real.exp (-(Real.pi * y)) := w_le hy
    have h2 : (128 * y + 41 : ℝ) ≤ 169 * (1 + 2 * Real.pi * y) := by
      have hpi := Real.pi_gt_three
      nlinarith [mul_le_mul_of_nonneg_left hpi.le hy.le]
    have he : 0 < Real.exp (-(Real.pi * y)) := Real.exp_pos _
    have h3 : w y ≤ 169 * (1 + 2 * Real.pi * y) * Real.exp (-(Real.pi * y)) :=
      h1.trans (mul_le_mul_of_nonneg_right h2 he.le)
    have hp : 0 < 169 * (1 + 2 * Real.pi * y) * Real.exp (-(Real.pi * y)) := by positivity
    have hlog := Real.log_le_log (w_pos hy) h3
    rw [Real.log_mul (ne_of_gt (by positivity : (0 : ℝ) < 169 * (1 + 2 * Real.pi * y)))
        (ne_of_gt he),
      Real.log_mul (by norm_num)
        (ne_of_gt (by positivity : (0 : ℝ) < 1 + 2 * Real.pi * y)), Real.log_exp] at hlog
    have hlog1 : 0 ≤ Real.log (1 + 2 * Real.pi * y) :=
      Real.log_nonneg (by have := Real.pi_pos; nlinarith)
    have hpi := Real.pi_pos
    have hpy : Real.pi * y ≤ Real.pi * (1 / 10 : ℝ) :=
      mul_le_mul_of_nonneg_left h Real.pi_pos.le
    linarith [log_169_le_six, hpy, hlog1]
  · -- 尖锐区域
    have hs := w_sharp8 (le_of_lt h)
    have hp : 0 < 300 * (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(2 * Real.pi * y)) := by positivity
    have hlog := Real.log_le_log (w_pos hy) hs
    rw [Real.log_mul (ne_of_gt (by positivity : (0 : ℝ) < 300 * (1 + 2 * Real.pi * y) ^ 7))
        (ne_of_gt (Real.exp_pos _)),
      Real.log_mul (by norm_num)
        (pow_ne_zero 7 (ne_of_gt (by positivity : (0 : ℝ) < 1 + 2 * Real.pi * y))),
      Real.log_pow, Real.log_exp] at hlog
    push_cast at hlog
    linarith [log_300_le_six, Real.pi_pos]

/-- (6.14)-类比的常数 `A_n`（b=8, h = 39n, b·N = 8n）。 -/
noncomputable def Aconst8 (n : ℕ) : ℝ :=
  2 * (39 * n) * (39 * n + 8 * n - 40 * n : ℝ) * Real.log (Kr n) +
    (lam8 * M0_8 - Irho8) * Kr n ^ 2 + 20 * (39 * n) * Real.log (Kr n) +
    (16 * Real.log 2 + 27 + Real.pi / 10) * (39 * n)

/-- 一维因子 `gK₈(y) = (1 + 2πy)^7 e^{−y/K}`。 -/
noncomputable def gK8 (n : ℕ) (y : ℝ) : ℝ := (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(1 / Kr n * y))

/-- **点态界**（(6.10) 被积函数，b=8）：对正的两两不同 `y`。 -/
theorem integrand_le8 (n : ℕ) (hn : 0 < n) (y : Fin (39 * n) → ℝ) (hy : ∀ i, 0 < y i)
    (hinj : Function.Injective y) :
    (Matrix.vandermonde fun j => y j ^ 2).det ^ 2 * ∏ j, ν n (y j) ≤
      Real.exp (Aconst8 n) * ∏ i, gK8 n (y i) := by
  set K : ℝ := Kr n with hKdef
  have hK : 0 < K := by simp only [hKdef, Kr]; positivity
  have h1n : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hK1 : 1 ≤ K := by
    simp only [hKdef, Kr]
    linarith
  set t : Fin (39 * n) → ℝ := fun i => (y i / K) ^ 2 with htdef
  have ht : ∀ i, 0 < t i := fun i => by
    simp only [htdef]; have := hy i; positivity
  have htinj : Function.Injective t := by
    intro i j hij
    simp only [htdef] at hij
    have := (pow_left_inj₀ (div_pos (hy i) hK).le (div_pos (hy j) hK).le two_ne_zero).mp hij
    exact hinj ((div_left_inj' hK.ne').mp this)
  -- positivity of both sides
  have hdet : (Matrix.vandermonde fun j => y j ^ 2).det ≠ 0 := by
    rw [Matrix.det_vandermonde_ne_zero_iff]
    intro i j hij
    exact hinj ((pow_left_inj₀ (hy i).le (hy j).le two_ne_zero).mp hij)
  have hν : ∀ j, 0 < ν n (y j) := fun j => ν_pos n (hy j)
  have hL : 0 < (Matrix.vandermonde fun j => y j ^ 2).det ^ 2 * ∏ j, ν n (y j) :=
    mul_pos (by positivity) (Finset.prod_pos fun j _ => hν j)
  have hg : ∀ i, 0 < gK8 n (y i) := fun i => by unfold gK8; have := hy i; positivity
  have hR : 0 < Real.exp (Aconst8 n) * ∏ i, gK8 n (y i) :=
    mul_pos (Real.exp_pos _) (Finset.prod_pos fun i _ => hg i)
  rw [← Real.log_le_log_iff hL hR]
  -- log of the left-hand side
  have hne : ∀ i j : Fin (39 * n), j ∈ Finset.Ioi i → y j ^ 2 - y i ^ 2 ≠ 0 := by
    intro i j hj h0
    have this : y j ^ 2 = y i ^ 2 := by linarith
    exact (Finset.mem_Ioi.mp hj).ne' (hinj ((pow_left_inj₀ (hy j).le (hy i).le two_ne_zero).mp this))
  have hdet2 : Real.log ((Matrix.vandermonde fun j => y j ^ 2).det ^ 2) =
      ∑ i, ∑ j ∈ Finset.Ioi i, (4 * Real.log K + 2 * Real.log |t j - t i|) := by
    rw [Matrix.det_vandermonde]
    simp only [← Finset.prod_pow]
    rw [Real.log_prod (fun i _ =>
      (Finset.prod_pos fun j hj => lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 (hne i j hj)))).ne')]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Real.log_prod (fun j hj => pow_ne_zero 2 (hne i j hj))]
    refine Finset.sum_congr rfl fun j hj => ?_
    have e : y j ^ 2 - y i ^ 2 = K ^ 2 * (t j - t i) := by
      simp only [htdef]; field_simp
    have hne' : t j - t i ≠ 0 := by
      intro h0; apply hne i j hj; rw [e, h0, mul_zero]
    rw [Real.log_pow, e, ← Real.log_abs, abs_mul, Real.log_mul (by positivity)
      (abs_pos.mpr hne').ne', abs_of_pos (by positivity : (0:ℝ) < K ^ 2), Real.log_pow]
    push_cast; ring
  -- log of each weight
  have hν_le : ∀ i, Real.log (ν n (y i)) ≤
      (16 * n - 2 * (40 * n)) * Real.log K - K * Vfield8 (t i) + 16 * Real.log (2 * K) +
        22 + Real.pi / 10 + 7 * Real.log (1 + 2 * Real.pi * y i) := by
    intro i
    have hyi := hy i
    have hDN := aeval_D_pos n (t := y i ^ 2) (by positivity)
    have hDK := aeval_D_pos (40 * n) (t := y i ^ 2) (by positivity)
    have hw := w_pos hyi
    unfold ν
    rw [Real.log_mul (by positivity) hw.ne', Real.log_div (by positivity) hDK.ne', Real.log_pow,
      log_aeval_D8 _ hK hyi, log_aeval_D8 _ hK hyi]
    -- comparison lemmas
    have hN : ((n : ℕ) : ℝ) / K = 1 / 40 := by
      simp only [hKdef, Kr]
      have hn0 : (n : ℝ) ≠ 0 := by exact_mod_cast hn.ne'
      field_simp
    have hKK : ((40 * n : ℕ) : ℝ) / K = 1 := by
      simp only [hKdef, Kr]
      have hn0 : (n : ℝ) ≠ 0 := by exact_mod_cast hn.ne'
      field_simp
      norm_num
    have h1 := Apery.sum_log_le_integral (ht i) hK1 (m := n) (by omega)
      (by simp only [hKdef, Kr]; push_cast; nlinarith [h1n])
    have h2 := Apery.integral_le_sum_log (ht i) hK (40 * n)
    rw [hN] at h1
    rw [hKK] at h2
    -- the weight（`−2πy` 与 `−K·Vfield8` 中隐含的 `−2πy` 相消）
    have hw' : Real.log (w (y i)) ≤ 6 + Real.pi / 10 + 7 * Real.log (1 + 2 * Real.pi * y i) -
        2 * Real.pi * y i := w_log_le8 hyi
    have hsqrt : Real.sqrt (t i) = y i / K := by
      simp only [htdef]; exact Real.sqrt_sq (by positivity)
    have hV : K * Vfield8 (t i) = 2 * Real.pi * y i + K * (∫ u in (0:ℝ)..1, Real.log (t i + u ^ 2)) -
        8 * (K * ∫ u in (0:ℝ)..(1 / 40), Real.log (t i + u ^ 2)) := by
      unfold Vfield8; rw [hsqrt]; field_simp
    push_cast at h1 h2 ⊢
    rw [hV]
    nlinarith [h1, h2, hw']
  -- assemble
  rw [Real.log_mul (by positivity) (Finset.prod_pos fun j _ => hν j).ne', hdet2,
    Real.log_prod (fun j _ => (hν j).ne'), Real.log_mul (Real.exp_pos _).ne'
    (Finset.prod_pos fun i _ => hg i).ne', Real.log_exp, Real.log_prod (fun i _ => (hg i).ne')]
  have hE := energy_ineq_final8 n hn t ht htinj
  have hsqrt : ∀ i, Real.sqrt (t i) = y i / K := fun i => by
    simp only [htdef]; exact Real.sqrt_sq (div_pos (hy i) hK).le
  simp_rw [hsqrt] at hE
  have hgi : ∀ i, Real.log (gK8 n (y i)) = 7 * Real.log (1 + 2 * Real.pi * y i) - y i / K := by
    intro i
    unfold gK8
    rw [Real.log_mul (by have := hy i; positivity) (Real.exp_pos _).ne', Real.log_exp, Real.log_pow]
    push_cast; ring
  simp_rw [hgi]
  simp only [Finset.sum_add_distrib, sum_Ioi_const8]
  have hsum_le := Finset.sum_le_sum fun i (_ : i ∈ Finset.univ) => hν_le i
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, ← Finset.mul_sum] at hsum_le
  have hlog2K : Real.log (2 * K) = Real.log 2 + Real.log K := Real.log_mul two_ne_zero hK.ne'
  rw [hlog2K] at hsum_le
  unfold Aconst8
  simp only [Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum]
  simp only [← Finset.mul_sum] at hE
  rw [← hKdef] at *
  push_cast at *
  have hlogK0 : 0 ≤ Real.log K := Real.log_nonneg hK1
  nlinarith [hE, hsum_le, hlogK0]

/-- `gK₈` 在 `(0,∞)` 上可积。 -/
lemma integrableOn_gK8 (n : ℕ) (hn : 0 < n) : IntegrableOn (gK8 n) (Ioi 0) := by
  have hK : 0 < Kr n := by simp only [Kr]; positivity
  have hr : 0 < 1 / Kr n := by positivity
  have hg : IntegrableOn (fun y : ℝ => (2 * Real.pi) ^ 7 * 128 * (y ^ 0 * Real.exp (-(1 / Kr n * y))) +
      (2 * Real.pi) ^ 7 * 128 * (y ^ 7 * Real.exp (-(1 / Kr n * y)))) (Ioi 0) :=
    ((Apery.integrableOn_pow_mul_exp_neg_mul 0 hr).const_mul _).add
      ((Apery.integrableOn_pow_mul_exp_neg_mul 7 hr).const_mul _)
  have hcont : Continuous (gK8 n) := by unfold gK8; fun_prop
  refine hg.mono' hcont.aestronglyMeasurable ?_
  refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
  have hy : 0 < y := hy
  rw [Real.norm_of_nonneg (by unfold gK8; positivity)]
  unfold gK8
  have h1 : (1 + 2 * Real.pi * y) ^ 7 ≤ (2 * Real.pi) ^ 7 * (1 + y) ^ 7 := by
    rw [← mul_pow]
    exact pow_le_pow_left₀ (by positivity) (by nlinarith [Real.pi_gt_three]) 7
  have h2 : (1 + y) ^ 7 ≤ 128 * (1 + y ^ 7) := by
    rcases le_or_gt y 1 with h | h
    · have h3 : (1 + y) ^ 7 ≤ 2 ^ 7 := pow_le_pow_left₀ (by linarith) (by linarith) 7
      have h4 : 0 ≤ y ^ 7 := by positivity
      nlinarith
    · have h3 : (1 + y) ^ 7 ≤ (2 * y) ^ 7 := pow_le_pow_left₀ (by linarith) (by linarith) 7
      have h4 : 0 ≤ y ^ 7 := by positivity
      nlinarith
  have he : 0 ≤ Real.exp (-(1 / Kr n * y)) := (Real.exp_pos _).le
  calc (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(1 / Kr n * y))
      ≤ (2 * Real.pi) ^ 7 * (128 * (1 + y ^ 7)) * Real.exp (-(1 / Kr n * y)) := by
        gcongr
        exact h1.trans (by gcongr)
    _ = (2 * Real.pi) ^ 7 * 128 * (y ^ 0 * Real.exp (-(1 / Kr n * y))) +
        (2 * Real.pi) ^ 7 * 128 * (y ^ 7 * Real.exp (-(1 / Kr n * y))) := by
        simp only [pow_zero, one_mul]; ring

/-- `∫₀^∞ gK₈ ≤ (2π)^7·128·5041·K^8`（K ≥ 1）。 -/
lemma integral_gK8_le (n : ℕ) (hn : 0 < n) :
    ∫ y in Ioi 0, gK8 n y ≤ (2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8 := by
  have hK1 : (1 : ℝ) ≤ Kr n := by
    have h1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
    simp only [Kr]
    nlinarith
  have hK0 : 0 < Kr n := by linarith
  have hr : 0 < 1 / Kr n := by positivity
  have hnn : 0 ≤ᵐ[volume.restrict (Ioi 0)] fun y : ℝ => gK8 n y :=
    (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => by
      have : (0 : ℝ) < y := hy
      unfold gK8; positivity)
  have hmono : ∀ᵐ y ∂(volume.restrict (Ioi 0)), gK8 n y ≤
      (2 * Real.pi) ^ 7 * 128 * (y ^ 0 * Real.exp (-(1 / Kr n * y))) +
        (2 * Real.pi) ^ 7 * 128 * (y ^ 7 * Real.exp (-(1 / Kr n * y))) := by
    refine (ae_restrict_iff' measurableSet_Ioi).mpr (Filter.Eventually.of_forall fun y hy => ?_)
    have hy : (0:ℝ) < y := hy
    unfold gK8
    have h1 : (1 + 2 * Real.pi * y) ^ 7 ≤ (2 * Real.pi) ^ 7 * (1 + y) ^ 7 := by
      rw [← mul_pow]
      exact pow_le_pow_left₀ (by positivity) (by nlinarith [Real.pi_gt_three]) 7
    have h2 : (1 + y) ^ 7 ≤ 128 * (1 + y ^ 7) := by
      rcases le_or_gt y 1 with h | h
      · have h3 : (1 + y) ^ 7 ≤ 2 ^ 7 := pow_le_pow_left₀ (by linarith) (by linarith) 7
        have h4 : 0 ≤ y ^ 7 := by positivity
        nlinarith
      · have h3 : (1 + y) ^ 7 ≤ (2 * y) ^ 7 := pow_le_pow_left₀ (by linarith) (by linarith) 7
        have h4 : 0 ≤ y ^ 7 := by positivity
        nlinarith
    have he : 0 ≤ Real.exp (-(1 / Kr n * y)) := (Real.exp_pos _).le
    calc (1 + 2 * Real.pi * y) ^ 7 * Real.exp (-(1 / Kr n * y))
        ≤ (2 * Real.pi) ^ 7 * (128 * (1 + y ^ 7)) * Real.exp (-(1 / Kr n * y)) := by
          gcongr
          exact h1.trans (by gcongr)
      _ = (2 * Real.pi) ^ 7 * 128 * (y ^ 0 * Real.exp (-(1 / Kr n * y))) +
          (2 * Real.pi) ^ 7 * 128 * (y ^ 7 * Real.exp (-(1 / Kr n * y))) := by
          simp only [pow_zero, one_mul]; ring
  calc ∫ y in Ioi 0, gK8 n y
      ≤ ∫ y in Ioi 0, ((2 * Real.pi) ^ 7 * 128 * (y ^ 0 * Real.exp (-(1 / Kr n * y))) +
          (2 * Real.pi) ^ 7 * 128 * (y ^ 7 * Real.exp (-(1 / Kr n * y)))) :=
        integral_mono_of_nonneg hnn
          (((Apery.integrableOn_pow_mul_exp_neg_mul 0 hr).const_mul _).add
            ((Apery.integrableOn_pow_mul_exp_neg_mul 7 hr).const_mul _)) hmono
    _ = (2 * Real.pi) ^ 7 * 128 * ((0 : ℕ).factorial / (1 / Kr n) ^ (0 + 1)) +
          (2 * Real.pi) ^ 7 * 128 * ((7 : ℕ).factorial / (1 / Kr n) ^ (7 + 1)) := by
        rw [integral_add ((Apery.integrableOn_pow_mul_exp_neg_mul 0 hr).const_mul _)
          ((Apery.integrableOn_pow_mul_exp_neg_mul 7 hr).const_mul _), integral_const_mul,
          integral_const_mul, Apery.integral_pow_mul_exp_neg_mul 0 hr,
          Apery.integral_pow_mul_exp_neg_mul 7 hr]
    _ = (2 * Real.pi) ^ 7 * 128 * (Kr n + 5040 * Kr n ^ 8) := by
        simp only [Nat.factorial]; norm_num
        field_simp
    _ ≤ (2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8 := by
        have hKK : Kr n ≤ Kr n ^ 8 := by
          calc Kr n = Kr n ^ 1 := (pow_one _).symm
            _ ≤ Kr n ^ 8 := pow_le_pow_right₀ hK1 (by norm_num)
        have hpi : 0 < (2 * Real.pi) ^ 7 * 128 := by positivity
        nlinarith

/-- `log ((2π)^7·128·5041) ≤ 27`。 -/
lemma log_C_le8 : Real.log ((2 * Real.pi) ^ 7 * 128 * 5041) ≤ 27 := by
  rw [Real.log_le_iff_le_exp (by positivity)]
  have he : (2.7182818283 : ℝ) ^ 27 ≤ Real.exp 27 := by
    have h1 : (2.7182818283 : ℝ) < Real.exp 1 := Real.exp_one_gt_d9
    have e : Real.exp 27 = Real.exp 1 ^ 27 := by rw [← Real.exp_nat_mul]; norm_num
    rw [e]
    exact pow_le_pow_left₀ (by norm_num) h1.le 27
  have hC : (2 * Real.pi) ^ 7 * 128 * 5041 ≤ 2.7182818283 ^ 27 := by
    have hpi : Real.pi ≤ 3.15 := Real.pi_lt_d2.le
    calc (2 * Real.pi) ^ 7 * 128 * 5041 ≤ (2 * 3.15 : ℝ) ^ 7 * 128 * 5041 := by
          gcongr <;> nlinarith [hpi]
      _ ≤ 2.7182818283 ^ 27 := by norm_num
  calc (2 * Real.pi) ^ 7 * 128 * 5041 ≤ 2.7182818283 ^ 27 := hC
    _ ≤ Real.exp 27 := he

/-- **(6.14)-类比**（b=8）：`Δ_K(ζ(7))` 的能量界，来自构型不等式 `energy_ineq_final8`。 -/
theorem log_Δ_le'8 (n : ℕ) (hn : 0 < n) :
    Real.log (aeval zeta7 (Δ n)) ≤
      2 * (39 * n) * (39 * n + 8 * n - 40 * n : ℝ) * Real.log (Kr n) +
        (lam8 * M0_8 - Irho8) * Kr n ^ 2 + 28 * (39 * n) * Real.log (Kr n) + 66 * (39 * n) := by
  have hK : 0 < Kr n := by simp only [Kr]; positivity
  have h1n : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hK1 : 1 ≤ Kr n := by simp only [Kr]; linarith
  have hlogK : 0 ≤ Real.log (Kr n) := Real.log_nonneg hK1
  have hΔ := Δ_pos n hn
  rw [Δ_eq_integral] at hΔ ⊢
  set I := ∫ x : Fin (39 * n) → ℝ, (Matrix.vandermonde fun j => x j ^ 2).det ^ 2 * ∏ j, ν n (x j)
    ∂(Measure.pi fun _ : Fin (39 * n) => μpos) with hI
  have hfac : (0 : ℝ) < ((39 * n).factorial : ℝ) := by positivity
  have hIpos : 0 < I := by
    by_contra hneg
    push Not at hneg
    have this : (1 / ((39 * n).factorial : ℝ)) * I ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos (by positivity) hneg
    linarith
  have hgint := integrableOn_gK8 n hn
  have hg0 : 0 ≤ ∫ y in Ioi 0, gK8 n y :=
    setIntegral_nonneg measurableSet_Ioi fun y hy => by
      have : (0 : ℝ) < y := hy
      unfold gK8; positivity
  have hg1 : ∫ y in Ioi 0, gK8 n y ≤ (2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8 :=
    integral_gK8_le n hn
  -- the integral bound
  have hμ : (Measure.pi fun _ : Fin (39 * n) => μpos) =
      Measure.pi fun _ : Fin (39 * n) => Apery.μpos := rfl
  have hbound : I ≤ Real.exp (Aconst8 n) * ((2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8) ^ (39 * n) := by
    calc I ≤ ∫ x : Fin (39 * n) → ℝ, Real.exp (Aconst8 n) * ∏ i, gK8 n (x i)
          ∂(Measure.pi fun _ : Fin (39 * n) => μpos) := by
          refine integral_mono_of_nonneg ?_ ((Integrable.fintype_prod fun _ => hgint).const_mul _) ?_
          · rw [hμ]
            filter_upwards [Apery.ae_pos_injective (39 * n)] with x hx
            exact mul_nonneg (sq_nonneg _) (Finset.prod_pos fun j _ => ν_pos n (hx.1 j)).le
          · rw [hμ]
            filter_upwards [Apery.ae_pos_injective (39 * n)] with x hx
            exact integrand_le8 n hn x hx.1 hx.2
      _ = Real.exp (Aconst8 n) * (∫ y in Ioi 0, gK8 n y) ^ (39 * n) := by
          rw [integral_const_mul, integral_fintype_prod_eq_prod (fun _ => gK8 n), Finset.prod_const,
            Finset.card_univ, Fintype.card_fin]
      _ ≤ Real.exp (Aconst8 n) * ((2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8) ^ (39 * n) := by
          gcongr
  have hlog1 : Real.log (1 / ((39 * n).factorial : ℝ) * I) ≤ Real.log I := by
    rw [Real.log_mul (by positivity) hIpos.ne']
    have this : Real.log (1 / ((39 * n).factorial : ℝ)) ≤ 0 := by
      rw [one_div, Real.log_inv]
      linarith [Real.log_nonneg (by exact_mod_cast Nat.one_le_iff_ne_zero.mpr (Nat.factorial_ne_zero _) :
        (1 : ℝ) ≤ ((39 * n).factorial : ℝ))]
    linarith
  have hlog2 : Real.log 2 ≤ 0.7 := by have := Real.log_two_lt_d9; linarith
  have hlogpi : Real.pi / 10 ≤ 0.315 := by
    have := Real.pi_lt_d2; linarith
  have hC := log_C_le8
  have hCpos : (0 : ℝ) < (2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8 := by positivity
  calc Real.log (1 / ((39 * n).factorial : ℝ) * I) ≤ Real.log I := hlog1
    _ ≤ Real.log (Real.exp (Aconst8 n) *
          ((2 * Real.pi) ^ 7 * 128 * 5041 * Kr n ^ 8) ^ (39 * n)) := by
        refine Real.log_le_log hIpos hbound
    _ = Aconst8 n + (39 * n) * (Real.log ((2 * Real.pi) ^ 7 * 128 * 5041) +
          8 * Real.log (Kr n)) := by
        rw [Real.log_mul (Real.exp_pos _).ne' (by positivity), Real.log_exp, Real.log_pow,
          Real.log_mul (by positivity) (by positivity), Real.log_pow]
        push_cast; ring
    _ ≤ _ := by
        unfold Aconst8
        nlinarith [hlog2, hlogpi, hC, hlogK, h1n]

end Zeta7
