import Mathlib
import Zeta7.Constants
import Zeta7.Degree
import Zeta7.Stirling
import Zeta7.Zeta7Def
import Zeta7.Positivity
import Zeta7.DetIntegral
import Zeta7.Kernel
import Zeta7.ZeroMass
import Zeta7.Gaussian
import Zeta7.Construction
import Zeta7.EnergyBound8
import Zeta7.EnergyConst8

/-!
# ζ(7) 实侧界（§6 类比）：接口与分解

`real_bound`（Prop 6.3 类比）是 `main_estimate` 的最后输入。mo271 的 b=6 对应物
（`Apery.RealBound`）由四条已证成分组装：

* `Δ_pos`：✅（`Zeta7.Positivity`，正矩表示 `moment_rep`）；
* `log_S_le8`（(6.15) 类比）：✅ `Zeta7.Stirling.log_S_le8`（系数 `(2λ − 16αλ − 2λ²)`
  与 `Cstar8` 按 (K:N:h) = 40:1:39 计算，K²·log K 与 n² 部分与 (6.14)-类比逐符号恒等）；
* `log_Δ_le'8`（(6.14) 类比）：✅ `Zeta7.EnergyBound8`（Andréief `Δ_eq_integral` +
  (6.11)/(6.12) 初等界 + 构型不等式 `energy_ineq_final8`（Lemma 6.1/6.2 类比，
  比较测度 ρ 的 Table7 证书））；
* `energy_const8`（(6.4) 数值不等式）：✅ `Zeta7.EnergyConst8`（16 原子 log 下界的
  artanh 部分和证书；U = −43/20，认证值 f = −2.1546… ≤ U，见
  `research/gen_energy_const8.py` 与 `research/b8_verdict.md` 附录 2）。

组装：K²·log K 项精确相消，K² 常数项由 `energy_const8` 门控，剩余
`1326·n·log K + 2691·n = o(K²)` 由 `log x / x → 0`
（`Real.tendsto_pow_log_div_mul_add_atTop`）吸收。低阶项系数在 ε-形式下
被 ε·K² 吸收（无需 b=6 的 27·K·logK + 200·K 强形式）。
-/

open Polynomial Filter Topology Finset

namespace Zeta7

/-- `log (40 n) / n → 0`（低阶项吸收的钥匙）。 -/
lemma tendsto_logKr_div_nat_atTop :
    Tendsto (fun n : ℕ => Real.log (Kr n) / (n : ℝ)) atTop (𝓝 0) := by
  have hcore : Tendsto (fun x : ℝ => Real.log x / x) atTop (𝓝 0) := by
    simpa using Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero
  have h40 : Tendsto (fun x : ℝ => Real.log (40 * x) / x) atTop (𝓝 0) := by
    have hadd : Tendsto (fun x : ℝ => (Real.log 40 + Real.log x) / x) atTop (𝓝 0) := by
      have hconst : Tendsto (fun x : ℝ => (Real.log 40 : ℝ) / x) atTop (𝓝 0) := by
        have h := (tendsto_const_nhds (x := (Real.log 40 : ℝ))).mul tendsto_inv_atTop_zero
        simpa [div_eq_mul_inv] using h
      have h := hconst.add hcore
      simpa [add_div] using h
    have e : (fun x : ℝ => Real.log (40 * x) / x) =ᶠ[atTop]
        fun x => (Real.log 40 + Real.log x) / x := by
      filter_upwards [eventually_gt_atTop (0 : ℝ)] with x hx
      rw [Real.log_mul (by norm_num) hx.ne']
    exact hadd.congr' e.symm
  have h := h40.comp tendsto_natCast_atTop_atTop
  exact h.congr fun n => by simp only [Function.comp_apply, Kr]

/-- 辅助：`2691 ≤ ε·800·n`（低阶常数项的吸收）。 -/
lemma const_le_mul (ε n : ℝ) (hn : 2691 / (ε * 800) ≤ n) (hε : 0 < ε) :
    (2691 : ℝ) ≤ ε * 800 * n := by
  have hpos : (0 : ℝ) < ε * 800 := by positivity
  rw [div_le_iff₀ hpos] at hn
  nlinarith

/-- **Prop 6.3 类比（实侧主界，ε-形式）**：F_K(ζ(7)) 为正，且对任意 ε > 0，
最终 `log F_K(ζ(7)) ≤ (U + ε)·K²`（K = 40n，U = −43/20 = −2.15：
实侧认证值 f = λM₀ − I(ρ) + C* = −2.1546… ≤ U，见 `Zeta7.EnergyConst8`）。

证明分解（见文件头）：`Δ_pos` + `log_Δ_le'8` + `log_S_le8` + `energy_const8`。 -/
theorem real_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ n : ℕ in atTop,
      0 < aeval zeta7 (F n) ∧
        Real.log (aeval zeta7 (F n)) ≤ ((U : ℝ) + ε) * Kr n ^ 2 := by
  -- 低阶项 `1326·n·log K + 2691·n = o(K²)` 的最终吸收
  have hε1 : (0 : ℝ) < ε * 1600 / (2 * 1326) := by positivity
  have hkey : ∀ᶠ n : ℕ in atTop,
      1326 * (n : ℝ) * Real.log (Kr n) + 2691 * (n : ℝ) ≤ ε * 1600 * (n : ℝ) ^ 2 := by
    rw [eventually_atTop]
    obtain ⟨N₁, hN₁⟩ := Metric.tendsto_atTop.1 tendsto_logKr_div_nat_atTop
      (ε * 1600 / (2 * 1326)) hε1
    have hxpos : (0 : ℝ) < 2691 / (ε * 800) := by positivity
    refine ⟨max N₁ (Nat.ceil (2691 / (ε * 800))), fun n hn => ?_⟩
    have hn1 : N₁ ≤ n := (le_max_left _ _).trans hn
    have hn2 : (2691 : ℝ) / (ε * 800) ≤ n :=
      (Nat.le_ceil _).trans (by exact_mod_cast (le_max_right _ _).trans hn)
    have h1n : (1 : ℕ) ≤ n :=
      (Nat.succ_le_of_lt (Nat.ceil_pos.mpr hxpos)).trans ((le_max_right _ _).trans hn)
    have h1r : (1 : ℝ) ≤ n := by exact_mod_cast h1n
    have hn0 : (0 : ℝ) < (n : ℝ) := by linarith
    have hlt0 := hN₁ n hn1
    rw [Real.dist_eq, sub_zero] at hlt0
    have hlt' : Real.log (Kr n) / (n : ℝ) < ε * 1600 / (2 * 1326) :=
      (le_abs_self _).trans_lt hlt0
    have h1 : 1326 * (Real.log (Kr n) / (n : ℝ)) * (n : ℝ) ^ 2 ≤
        (ε * 1600 / (2 * 1326)) * 1326 * (n : ℝ) ^ 2 := by
      have h2 := mul_lt_mul_of_pos_right hlt' (sq_pos_of_ne_zero (ne_of_gt hn0))
      have h3 := mul_lt_mul_of_pos_left h2 (show (0 : ℝ) < 1326 by norm_num)
      nlinarith
    have e1 : 1326 * (n : ℝ) * Real.log (Kr n) =
        1326 * (Real.log (Kr n) / (n : ℝ)) * (n : ℝ) ^ 2 := by
      field_simp [ne_of_gt hn0]
    rw [e1]
    nlinarith [h1, const_le_mul ε n hn2 hε]
  rw [eventually_atTop] at hkey ⊢
  obtain ⟨N, hN⟩ := hkey
  refine ⟨max N 1, fun n hn => ?_⟩
  have hnN : N ≤ n := (le_max_left _ _).trans hn
  have hn : 0 < n := lt_of_lt_of_le (by norm_num) ((le_max_right _ _).trans hn)
  have hS : (0 : ℝ) < (S n : ℝ) := by exact_mod_cast S_pos n
  have hΔ := Δ_pos n hn
  have hF : aeval zeta7 (F n) = (S n : ℝ) * aeval zeta7 (Δ n) := by
    simp [F, aeval_C]
  refine ⟨by rw [hF]; positivity, ?_⟩
  rw [hF, Real.log_mul hS.ne' hΔ.ne']
  have h1 := log_Δ_le'8 n hn
  have h2 := log_S_le8 n hn
  have h3 := energy_const8
  have h3' : (lam8 * M0_8 - Irho8 + Cstar8) * Kr n ^ 2 ≤ (U : ℝ) * Kr n ^ 2 :=
    mul_le_mul_of_nonneg_right h3 (sq_nonneg _)
  -- 合并四条成分：K²·log K 精确相消，K² 常数由 energy_const8 门控
  have hmain : Real.log (S n : ℝ) + Real.log (aeval zeta7 (Δ n)) ≤
      (U : ℝ) * Kr n ^ 2 + 1326 * (n : ℝ) * Real.log (Kr n) + 2691 * (n : ℝ) := by
    simp only [Kr, lam8, alph8, U] at h1 h2 h3' ⊢
    nlinarith [h1, h2, h3']
  -- 低阶项吸收
  have hjunk := hN n hnN
  simp only [Kr, U] at hmain ⊢
  nlinarith [hmain, hjunk]

end Zeta7
