import Mathlib
import Zeta5Irrational.Params

/-!
# 数值事实（论文式 (5.18)–(5.20)、(6.4)、(7.2)、Appendix B Table 3/4、Appendix C）

全部有理恒等式均以 `norm_num` 严格验证（与论文 Appendix B 的精确分数一致）。
-/

open scoped Polynomial

namespace Zeta5Irrational

/-- 论文式 (7.2) 与 Appendix B.3：−1600(A₂₀₀ + Ū) − 139/5 的精确正值余量。 -/
theorem margin_200_sub :
    -1600 * (AM 200 + Ubar) - 139 / 5 = 3089837638249482469 / 58872425992515135000 := by
  norm_num [AM, Ubar, Astar, lambdaP]

/-- 推论：−1600(A₂₀₀ + Ū) > 139/5（论文式 (7.2) 左）。 -/
theorem margin_200 : 139 / 5 < -1600 * (AM 200 + Ubar) := by
  have h := margin_200_sub
  norm_num at h
  linarith

/-- 论文式 (7.2) 与 Appendix B.3：−1600(A₁₀₀₀₀₀ + Ū) − 7907/100 的精确正值余量。 -/
theorem margin_100000_sub :
    -1600 * (AM 100000 + Ubar) - 7907 / 100
      = 29873543950273155160680943 / 3679526624532195937500000000 := by
  norm_num [AM, Ubar, Astar, lambdaP]

/-- 推论：−1600(A₁₀₀₀₀₀ + Ū) > 7907/100（论文式 (7.2) 右）。 -/
theorem margin_100000 : 7907 / 100 < -1600 * (AM 100000 + Ubar) := by
  have h := margin_100000_sub
  norm_num at h
  linarith

/-- 论文 Appendix C.2：ϱ·c − 260 = −1/80。 -/
theorem rho_c_sub : (6933 / 500 : ℚ) * (75 / 4) - 260 = -1 / 80 := by
  norm_num

/-- 论文 Appendix C.2：ε − λ/c = 1/24000。 -/
theorem eps_sub_lambda_div_c : (79 / 1600 : ℚ) - (37 / 40) / (75 / 4) = 1 / 24000 := by
  norm_num

/-- 论文 Appendix C.2：λεϱ 组合 λϱ − ε = 511067/40000。 -/
theorem lambda_rho_sub_eps : (37 / 40 : ℚ) * (6933 / 500) - 79 / 1600 = 511067 / 40000 := by
  norm_num

/-- 论文 §6：式 (6.14)/(6.15) 中 K²logK 项相消的系数恒等式
    2λ(λ + 6α − 1) + (2λ − 12αλ − 2λ²) = 0（代入 λ = 37/40, α = 3/40）。 -/
theorem k2logk_cancellation :
    2 * (37 / 40 : ℚ) * (37 / 40 + 6 * (3 / 40 : ℚ) - 1) +
      (2 * (37 / 40 : ℚ) - 12 * (3 / 40 : ℚ) * (37 / 40 : ℚ) - 2 * (37 / 40 : ℚ) ^ 2) = 0 := by
  norm_num

/-- 论文 Appendix B：R 的二次系数相消
    2λ − 12λα + 2(H² − H − λ²) − 18α² + 6α = 0（代入 λ = 37/40, α = 3/40, H = 23/20）。 -/
theorem quadratic_cancellation :
    2 * (37 / 40 : ℚ) - 12 * (37 / 40 : ℚ) * (3 / 40 : ℚ) +
      2 * ((23 / 20 : ℚ) ^ 2 - 23 / 20 - (37 / 40 : ℚ) ^ 2) -
      18 * (3 / 40 : ℚ) ^ 2 + 6 * (3 / 40 : ℚ) = 0 := by
  norm_num

/-- Table 3（论文 Appendix B）：内区积分 ∫₃^20 R(x)/x³ dx 按单位区间的十七项之和
    （式 (5.18) 的右端）。 -/
theorem table3_sum :
    (26807 / 161280 : ℚ) + (37383 / 704000 : ℚ) + (37523 / 8236800 : ℚ) +
      (-120923 / 6552000 : ℚ) + (-10025233 / 356428800 : ℚ) +
      (-110029309 / 3348864000 : ℚ) + (-2278419487 / 64465632000 : ℚ) +
      (-282415081 / 7724640000 : ℚ) + (-3236921227 / 87524236800 : ℚ) +
      (-3350220001 / 90899827200 : ℚ) + (7424224373 / 2217983040000 : ℚ) +
      (16775764609 / 955086612480 : ℚ) + (369043847 / 30810528000 : ℚ) +
      (651380108633 / 86461373856000 : ℚ) + (472851276229 / 119820121344000 : ℚ) +
      (4930060867 / 4724197793280 : ℚ) + (-15199801 / 11563552000 : ℚ)
      = 322437603634266857629 / 7535670527041937280000 := by
  norm_num

/-- Table 4（论文 Appendix B）：外区被积函数的十一段仿射式 T(y) = b + cy 的积分和，
    ∑ (b(r−l) + c(r²−l²)/2) = I_out = 127751/96000（式 (5.10)）。 -/
theorem table4_sum :
    ((279 / 40 : ℚ) * (43 / 120 - 1 / 3) + (-9) * ((43 / 120 : ℚ) ^ 2 - (1 / 3 : ℚ) ^ 2) / 2) +
    ((451 / 40 : ℚ) * (37 / 100 - 43 / 120) + (-21) * ((37 / 100 : ℚ) ^ 2 - (43 / 120 : ℚ) ^ 2) / 2) +
    ((377 / 40 : ℚ) * (13 / 30 - 37 / 100) + (-16) * ((13 / 30 : ℚ) ^ 2 - (37 / 100 : ℚ) ^ 2) / 2) +
    ((429 / 40 : ℚ) * (37 / 80 - 13 / 30) + (-19) * ((37 / 80 : ℚ) ^ 2 - (13 / 30 : ℚ) ^ 2) / 2) +
    ((17 / 4 : ℚ) * (1 / 2 - 37 / 80) + (-5) * ((1 / 2 : ℚ) ^ 2 - (37 / 80 : ℚ) ^ 2) / 2) +
    ((51 / 10 : ℚ) * (43 / 80 - 1 / 2) + (-3) * ((43 / 80 : ℚ) ^ 2 - (1 / 2 : ℚ) ^ 2) / 2) +
    ((231 / 20 : ℚ) * (37 / 60 - 43 / 80) + (-15) * ((37 / 60 : ℚ) ^ 2 - (43 / 80 : ℚ) ^ 2) / 2) +
    ((97 / 10 : ℚ) * (13 / 20 - 37 / 60) + (-12) * ((13 / 20 : ℚ) ^ 2 - (37 / 60 : ℚ) ^ 2) / 2) +
    ((42 / 5 : ℚ) * (37 / 40 - 13 / 20) + (-10) * ((37 / 40 : ℚ) ^ 2 - (13 / 20 : ℚ) ^ 2) / 2) +
    ((1 : ℚ) * (1 - 37 / 40) + (-2) * ((1 : ℚ) ^ 2 - (37 / 40 : ℚ) ^ 2) / 2) +
    ((37 / 20 : ℚ) * (37 / 20 - 1) + (-1) * ((37 / 20 : ℚ) ^ 2 - (1 : ℚ) ^ 2) / 2)
      = 127751 / 96000 := by
  norm_num

/-- 秩修正函数 d(y)（论文式 (5.9)），y ∈ (1/3, 1/2) 上：
    d(y) = (1 + 4α − 3y − (1 + α − 3y)₊)₊，α = 3/40。 -/
noncomputable def rankCorr (y : ℝ) : ℝ :=
  max (1 + 4 * (3 / 40 : ℝ) - 3 * y - max (1 + (3 / 40 : ℝ) - 3 * y) 0) 0

/-- 论文 §5.2：∫_{1/3}^{1/2} d(y) dy = 9/640（式 (5.9) 后）。分段：
    (1/3, 43/120] 上 d = 9/40；(43/120, 13/30] 上 d = 13/10 − 3y；(13/30, 1/2) 上 d = 0。 -/
theorem integral_rankCorr : ∫ y in (1 / 3 : ℝ)..(1 / 2 : ℝ), rankCorr y = 9 / 640 := by
  have hcont : Continuous rankCorr := by
    unfold rankCorr
    fun_prop
  have hint : ∀ a b, IntervalIntegrable rankCorr MeasureTheory.volume a b :=
    fun a b => hcont.intervalIntegrable a b
  have e1 : rankCorr =ᶠ[MeasureTheory.ae (MeasureTheory.volume.restrict
      (Set.uIoc (1 / 3 : ℝ) (43 / 120 : ℝ)))] fun _ => (9 / 40 : ℝ) := by
    filter_upwards [MeasureTheory.self_mem_ae_restrict (measurableSet_uIoc :
      MeasurableSet (Set.uIoc (1 / 3 : ℝ) (43 / 120 : ℝ)))] with y hy
    rcases Set.mem_uIoc.1 hy with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · have h2' : (0:ℝ) ≤ 1 + (3 / 40:ℝ) - 3 * y := by nlinarith
      have h9 : (1:ℝ) + 4 * (3/40:ℝ) - 3 * y - (1 + (3/40:ℝ) - 3 * y) = 9 / 40 := by ring
      simp only [rankCorr, max_eq_left h2', h9, max_eq_left (by norm_num : (0:ℝ) ≤ 9 / 40)]
    · have h2' : (0:ℝ) ≤ 1 + (3 / 40:ℝ) - 3 * y := by nlinarith
      have h9 : (1:ℝ) + 4 * (3/40:ℝ) - 3 * y - (1 + (3/40:ℝ) - 3 * y) = 9 / 40 := by ring
      simp only [rankCorr, max_eq_left h2', h9, max_eq_left (by norm_num : (0:ℝ) ≤ 9 / 40)]
  have e2 : rankCorr =ᶠ[MeasureTheory.ae (MeasureTheory.volume.restrict
      (Set.uIoc (43 / 120 : ℝ) (13 / 30 : ℝ)))] fun y => 13 / 10 - 3 * y := by
    filter_upwards [MeasureTheory.self_mem_ae_restrict (measurableSet_uIoc :
      MeasurableSet (Set.uIoc (43 / 120 : ℝ) (13 / 30 : ℝ)))] with y hy
    rcases Set.mem_uIoc.1 hy with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · have h2' : 1 + (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have h3 : (0:ℝ) ≤ 13 / 10 - 3 * y := by nlinarith
      have hr : (1:ℝ) + 4 * (3/40:ℝ) - 3 * y - max (1 + (3/40:ℝ) - 3 * y) 0
          = 13 / 10 - 3 * y := by rw [max_eq_right h2']; ring
      simp only [rankCorr, hr, max_eq_left h3]
    · have h2' : 1 + (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have h3 : (0:ℝ) ≤ 13 / 10 - 3 * y := by nlinarith
      have hr : (1:ℝ) + 4 * (3/40:ℝ) - 3 * y - max (1 + (3/40:ℝ) - 3 * y) 0
          = 13 / 10 - 3 * y := by rw [max_eq_right h2']; ring
      simp only [rankCorr, hr, max_eq_left h3]
  have e3 : rankCorr =ᶠ[MeasureTheory.ae (MeasureTheory.volume.restrict
      (Set.uIoc (13 / 30 : ℝ) (1 / 2 : ℝ)))] fun _ => (0 : ℝ) := by
    filter_upwards [MeasureTheory.self_mem_ae_restrict (measurableSet_uIoc :
      MeasurableSet (Set.uIoc (13 / 30 : ℝ) (1 / 2 : ℝ)))] with y hy
    rcases Set.mem_uIoc.1 hy with ⟨h1, h2⟩ | ⟨h1, h2⟩
    · have h2' : 1 + (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have h3 : 1 + 4 * (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have hrw : max (1 + (3/40:ℝ) - 3 * y) 0 = 0 := max_eq_right h2'
      rw [rankCorr, hrw,
        max_eq_right (by nlinarith : (1:ℝ) + 4 * (3 / 40:ℝ) - 3 * y - 0 ≤ 0)]
    · have h2' : 1 + (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have h3 : 1 + 4 * (3 / 40:ℝ) - 3 * y ≤ 0 := by nlinarith
      have hrw : max (1 + (3/40:ℝ) - 3 * y) 0 = 0 := max_eq_right h2'
      rw [rankCorr, hrw,
        max_eq_right (by nlinarith : (1:ℝ) + 4 * (3 / 40:ℝ) - 3 * y - 0 ≤ 0)]
  -- 仿射段积分：以 13/10·y − 3/2·y² 为原函数（微积分基本定理）
  have hmid : ∫ y in (43/120:ℝ)..(13/30:ℝ), (13/10 - 3 * y : ℝ)
      = 13/10 * (13/30 - 43/120) - 3 * ((13/30:ℝ)^2 - (43/120:ℝ)^2) / 2 := by
    have hF : ∀ y : ℝ, HasDerivAt (fun y => 13/10 * y - 3/2 * y ^ 2) (13/10 - 3 * y) y := by
      intro y
      have h1 : HasDerivAt (fun y : ℝ => 13/10 * y) (13/10 * 1) y :=
        (hasDerivAt_id' y).const_mul _
      have h2 : HasDerivAt (fun y : ℝ => 3/2 * y ^ 2) (3/2 * (2 * y ^ (2 - 1))) y :=
        (hasDerivAt_pow 2 y).const_mul _
      have h3 := h1.sub h2
      rw [show 13/10 * 1 - 3/2 * (2 * y ^ (2 - 1)) = 13/10 - 3 * y by ring] at h3
      exact h3
    have hintf : IntervalIntegrable (fun y => 13/10 - 3 * y) MeasureTheory.volume
        (43/120:ℝ) (13/30:ℝ) := by
      apply Continuous.intervalIntegrable
      fun_prop
    rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hF x) hintf]
    ring
  have i1 : ∫ y in (1/3:ℝ)..(43/120:ℝ), rankCorr y = (9/40 : ℝ) * (43/120 - 1/3) := by
    rw [intervalIntegral.integral_congr_ae_restrict e1, intervalIntegral.integral_const]
    ring
  have i2 : ∫ y in (43/120:ℝ)..(13/30:ℝ), rankCorr y
      = 13/10 * (13/30 - 43/120) - 3 * ((13/30:ℝ)^2 - (43/120:ℝ)^2) / 2 := by
    rw [intervalIntegral.integral_congr_ae_restrict e2, hmid]
  have i3 : ∫ y in (13/30:ℝ)..(1/2:ℝ), rankCorr y = 0 := by
    rw [intervalIntegral.integral_congr_ae_restrict e3]
    exact intervalIntegral.integral_zero
  calc (∫ y in (1/3:ℝ)..(1/2:ℝ), rankCorr y)
      = ((∫ y in (1/3:ℝ)..(43/120:ℝ), rankCorr y)
          + (∫ y in (43/120:ℝ)..(13/30:ℝ), rankCorr y))
        + (∫ y in (13/30:ℝ)..(1/2:ℝ), rankCorr y) := by
        rw [add_assoc, intervalIntegral.integral_add_adjacent_intervals (hint _ _) (hint _ _),
          intervalIntegral.integral_add_adjacent_intervals (hint _ _) (hint _ _)]
    _ = 9 / 640 := by rw [i1, i2, i3, add_zero]; norm_num


/-- Taylor 下界：exp x ≥ S_n - R_n（0 ≤ x ≤ 1）。 -/
private theorem exp_ge_taylor_sub (x : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (n : ℕ) (hn : 0 < n) :
    (∑ m ∈ Finset.range n, x ^ m / m.factorial)
      - x ^ n * (n.succ / (n.factorial * n)) ≤ Real.exp x := by
  have hb := Real.exp_bound (x := x) (by rw [abs_of_nonneg hx0]; linarith) hn
  have h2 := (abs_sub_le_iff.1 hb).2
  rw [abs_of_nonneg hx0] at h2
  linarith

/-- exp 2 的下界。 -/
private theorem exp_two_ge : (7.389056 : ℝ) ≤ Real.exp 2 := by
  have h1 : ((∑ m ∈ Finset.range 14, (1 : ℝ) ^ m / m.factorial)
      - (1 : ℝ) ^ 14 * (15 / ((Nat.factorial 14) * 14))) ≤ Real.exp 1 :=
    exp_ge_taylor_sub 1 (by norm_num) (by norm_num) 14 (by norm_num)
  have hsq : (7.389056 : ℝ) ≤ ((∑ m ∈ Finset.range 14, (1 : ℝ) ^ m / m.factorial)
      - (1 : ℝ) ^ 14 * (15 / ((Nat.factorial 14) * 14))) ^ 2 := by
    norm_num [Finset.sum_range_succ]
  rw [show (2 : ℝ) = 1 + 1 by norm_num, Real.exp_add]
  have hnn : (0 : ℝ) ≤ ((∑ m ∈ Finset.range 14, (1 : ℝ) ^ m / m.factorial)
      - (1 : ℝ) ^ 14 * (15 / ((Nat.factorial 14) * 14))) := by
    norm_num [Finset.sum_range_succ]
  calc (7.389056 : ℝ) ≤ ((∑ m ∈ Finset.range 14, (1 : ℝ) ^ m / m.factorial)
        - (1 : ℝ) ^ 14 * (15 / ((Nat.factorial 14) * 14))) ^ 2 := hsq
    _ ≤ Real.exp 1 * Real.exp 1 := by
      rw [pow_two]
      exact mul_le_mul h1 h1 hnn (Real.exp_nonneg 1)

/-- log 18 的上界。 -/
private theorem log_18_lt : Real.log 18 < 2.890372 := by
  rw [Real.log_lt_iff_lt_exp (by norm_num)]
  have hr : ((∑ m ∈ Finset.range 12, (0.890372 : ℝ) ^ m / m.factorial)
      - (0.890372 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) ≤ Real.exp (0.890372 : ℝ) :=
    exp_ge_taylor_sub (0.890372 : ℝ) (by norm_num) (by norm_num) 12 (by norm_num)
  have h18 : (18 : ℝ) < (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.890372 : ℝ) ^ m / m.factorial)
        - (0.890372 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
    norm_num [Finset.sum_range_succ]
  have hexp : (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.890372 : ℝ) ^ m / m.factorial)
        - (0.890372 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12)))
      ≤ Real.exp 2 * Real.exp (0.890372 : ℝ) := by
    have hnn : (0 : ℝ) ≤ ((∑ m ∈ Finset.range 12, (0.890372 : ℝ) ^ m / m.factorial)
        - (0.890372 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
      norm_num [Finset.sum_range_succ]
    exact mul_le_mul exp_two_ge hr hnn (Real.exp_nonneg 2)
  rw [show (2.890372 : ℝ) = 2 + 0.890372 by norm_num, Real.exp_add]
  linarith

/-- log (1600/111) 的上界。 -/
private theorem log_1600_111_lt : Real.log (1600 / 111) < 2.66823 := by
  rw [Real.log_lt_iff_lt_exp (by norm_num)]
  have hr : ((∑ m ∈ Finset.range 12, (0.66823 : ℝ) ^ m / m.factorial)
      - (0.66823 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) ≤ Real.exp (0.66823 : ℝ) :=
    exp_ge_taylor_sub (0.66823 : ℝ) (by norm_num) (by norm_num) 12 (by norm_num)
  have h18 : (1600 / 111 : ℝ) < (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.66823 : ℝ) ^ m / m.factorial)
        - (0.66823 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
    norm_num [Finset.sum_range_succ]
  have hexp : (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.66823 : ℝ) ^ m / m.factorial)
        - (0.66823 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12)))
      ≤ Real.exp 2 * Real.exp (0.66823 : ℝ) := by
    have hnn : (0 : ℝ) ≤ ((∑ m ∈ Finset.range 12, (0.66823 : ℝ) ^ m / m.factorial)
        - (0.66823 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
      norm_num [Finset.sum_range_succ]
    exact mul_le_mul exp_two_ge hr hnn (Real.exp_nonneg 2)
  rw [show (2.66823 : ℝ) = 2 + 0.66823 by norm_num, Real.exp_add]
  linarith

/-- log ((43 + 4√114)/5) 的上界。 -/
private theorem log_43_lt : Real.log ((43 + 4 * Real.sqrt 114) / 5) < 2.84152 := by
  rw [Real.log_lt_iff_lt_exp (by positivity)]
  have h1 : Real.sqrt 114 < 10.67708 := by
    rw [Real.sqrt_lt' (by norm_num)]
    norm_num
  have hup : ((43 + 4 * Real.sqrt 114) / 5 : ℝ) < 17.141664 := by linarith
  have hr : ((∑ m ∈ Finset.range 12, (0.84152 : ℝ) ^ m / m.factorial)
      - (0.84152 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) ≤ Real.exp (0.84152 : ℝ) :=
    exp_ge_taylor_sub (0.84152 : ℝ) (by norm_num) (by norm_num) 12 (by norm_num)
  have h18 : (17.141664 : ℝ) < (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.84152 : ℝ) ^ m / m.factorial)
        - (0.84152 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
    norm_num [Finset.sum_range_succ]
  have hexp : (7.389056 : ℝ)
      * ((∑ m ∈ Finset.range 12, (0.84152 : ℝ) ^ m / m.factorial)
        - (0.84152 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12)))
      ≤ Real.exp 2 * Real.exp (0.84152 : ℝ) := by
    have hnn : (0 : ℝ) ≤ ((∑ m ∈ Finset.range 12, (0.84152 : ℝ) ^ m / m.factorial)
        - (0.84152 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
      norm_num [Finset.sum_range_succ]
    exact mul_le_mul exp_two_ge hr hnn (Real.exp_nonneg 2)
  rw [show (2.84152 : ℝ) = 2 + 0.84152 by norm_num, Real.exp_add]
  linarith

/-- log (4/3) 的上界。 -/
private theorem log_4_3_lt : Real.log (4 / 3) < 0.287683 := by
  rw [Real.log_lt_iff_lt_exp (by norm_num)]
  have hr : ((∑ m ∈ Finset.range 12, (0.287683 : ℝ) ^ m / m.factorial)
      - (0.287683 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) ≤ Real.exp (0.287683 : ℝ) :=
    exp_ge_taylor_sub (0.287683 : ℝ) (by norm_num) (by norm_num) 12 (by norm_num)
  have h43 : (4 / 3 : ℝ) < ((∑ m ∈ Finset.range 12, (0.287683 : ℝ) ^ m / m.factorial)
      - (0.287683 : ℝ) ^ 12 * (13 / ((Nat.factorial 12) * 12))) := by
    norm_num [Finset.sum_range_succ]
  linarith

/-- κ（论文式 (C.6)）。 -/
noncomputable def kappa : ℝ :=
  2 * Real.pi / Real.sqrt 3 + Real.log (4 / 3) + (9 / 20) * Real.log 18 +
    (37 / 40) * (1 + Real.log (1600 / 111)) +
    (37 / 20) * Real.log ((43 + 4 * Real.sqrt 114) / 5)

/-- 论文式 (C.6)：κ < 6933/500。
    证明：对各超越项建立有理上界 —— `Real.pi_lt_d6`（π < 3.141593）与 `Real.lt_sqrt`/
    `Real.sqrt_lt'`（√3、√114 的有理夹逼）处理 2π/√3 与分子的 √114；
    对 log 用 `Real.log_lt_iff_lt_exp` 转化为 exp 的下界，再由 `Real.exp_bound`
    （Taylor 余项）给出 exp 2、exp r（r = 小数部分）的显式有理下界，
    最终 `linarith` 汇总（总和 13.86590515 ≤ 13.866）。 -/
theorem kappa_lt : kappa < (6933 / 500 : ℝ) := by
  have h1 : 2 * Real.pi / Real.sqrt 3 < 3.6276 := by
    have hpi : 2 * Real.pi < 6.283186 := by
      have h := Real.pi_lt_d6
      linarith
    have hsq3 : (1.7320508 : ℝ) < Real.sqrt 3 := by
      rw [Real.lt_sqrt (by norm_num)]
      norm_num
    have hpos : (0 : ℝ) < Real.sqrt 3 := Real.sqrt_pos.2 (by norm_num)
    have hstep : 2 * Real.pi / Real.sqrt 3 < 6.283186 / Real.sqrt 3 :=
      div_lt_div_of_pos_right hpi hpos
    have hfin : 6.283186 / Real.sqrt 3 < 3.6276 := by
      rw [div_lt_iff₀ hpos]
      have h2 : (6.283186 : ℝ) ≤ 3.6276 * 1.7320508 := by norm_num
      have h3 : (3.6276 : ℝ) * 1.7320508 < 3.6276 * Real.sqrt 3 :=
        mul_lt_mul_of_pos_left hsq3 (by norm_num)
      linarith
    exact hstep.trans hfin
  have hsum : (3.6276 : ℝ) + 0.287683 + 1.3006674 + 3.39314275 + 5.256812
      ≤ 6933 / 500 := by norm_num
  rw [kappa]
  linarith [h1, log_4_3_lt, log_18_lt, log_1600_111_lt, log_43_lt, hsum]

end Zeta5Irrational
