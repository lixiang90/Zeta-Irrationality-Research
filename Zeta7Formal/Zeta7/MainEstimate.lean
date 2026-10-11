import Mathlib
import Zeta7.Growth
import Zeta7.Construction
import Zeta7.Zeta7Def
import Zeta7.Degree
import Zeta7.Constants
import Zeta7.RealBound
import Zeta7.Norm

/-!
# 主估计（Theorem 2.1 类比）的组装

三个输入，两个已证、一个为能量链（`Zeta7.RealBound.real_bound`，唯一 sorry）：

* `natDegree_F`：✅（`Zeta7.Degree`，(2.9)-类比）；
* `real_bound`：能量链（Prop 6.3 类比，ε-形式）；
* 归一化：`integral_mN`（✅，`Zeta7.Norm`，整性）+ `growth_mN`
  （✅，`Zeta7.Growth`，`log mN ≤ (Aeff + ε)·K²`）+ `mN_pos`（✅），
  且 `Aeff + U < 0`（✅ `Aeff_margin`，margin ≈ −1.2）。

 decay 率 c = 800·(−(Aeff+U)) > 0（b=6 的镜像；论文原值 139/5 的位置）。
组装与 mo271 `Apery.MainEstimate` 同构（ε-形式接口使低阶项系数无需预定）。
-/

open Polynomial Filter Topology Finset

namespace Zeta7

/-- **归一化（Proposition 5.1/5.2 类比）**：正有理列 mN，mN·F ∈ ℤ[X]（n ≥ 1），
且增长受 Aeff 控制。全部由 `Zeta7.Norm` / `Zeta7.Growth` 已证结果包装。 -/
theorem normalization :
    ∃ m : ℕ → ℚ, (∀ n, 0 < m n) ∧
      (∀ᶠ n in atTop, ∃ Q : ℤ[X], Q.map (Int.castRingHom ℚ) = C (m n) * F n) ∧
      ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, Real.log (m n) ≤ ((Aeff : ℝ) + ε) * Kr n ^ 2 :=
  ⟨mN, mN_pos, (eventually_ge_atTop 1).mono fun _ hn => integral_mN hn, growth_mN⟩

/-- **Theorem 2.1 类比**：对所有充分大的 n，存在整系数多项式 Q（次数 37n）使
`0 < Q(ζ(7)) < exp(−c·n²)`，c = 800·(−(Aeff+U)) > 0。 -/
theorem main_estimate :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n in Filter.atTop, ∃ Q : ℤ[X],
      Q.natDegree = 37 * n ∧
      0 < aeval zeta7 Q ∧ aeval zeta7 Q ≤ Real.exp (-c * (n : ℝ) ^ 2) := by
  obtain ⟨m, hm_pos, hm_int, hm_log⟩ := normalization
  set δ : ℝ := -((Aeff : ℝ) + U) with hδ_def
  have hδ : 0 < δ := by
    have h : ((Aeff + U : ℚ) : ℝ) < 0 := by exact_mod_cast Aeff_margin
    push_cast at h
    rw [hδ_def]; linarith
  have hδ4 : 0 < δ / 4 := by positivity
  refine ⟨800 * δ, by positivity, ?_⟩
  filter_upwards [hm_int, hm_log (δ / 4) hδ4, real_bound (δ / 4) hδ4,
    eventually_gt_atTop 0] with n ⟨Q, hQ⟩ hlog_growth hlog_real hn
  obtain ⟨hFpos, hFlog⟩ := hlog_real
  have hc : (0 : ℝ) < m n := by exact_mod_cast hm_pos n
  have hQeval : aeval zeta7 Q = (m n : ℝ) * aeval zeta7 (F n) := by
    rw [← aeval_map_algebraMap ℚ zeta7 Q]
    simp only [algebraMap_int_eq, hQ, map_mul, aeval_C]
    rfl
  refine ⟨Q, ?_, ?_, ?_⟩
  · have h1 : (Q.map (Int.castRingHom ℚ)).natDegree = Q.natDegree :=
      natDegree_map_eq_of_injective (Int.cast_injective) Q
    rw [← h1, hQ, natDegree_C_mul (by exact_mod_cast (hm_pos n).ne'), natDegree_F]
  · rw [hQeval]; exact mul_pos hc hFpos
  · rw [hQeval, ← Real.log_le_iff_le_exp (mul_pos hc hFpos), Real.log_mul hc.ne' hFpos.ne']
    have hK2 : Kr n ^ 2 = 1600 * (n : ℝ) ^ 2 := by simp only [Kr]; ring
    rw [hK2] at hlog_growth
    have hFprobe : Real.log (aeval zeta7 (F n)) ≤ ((U : ℝ) + δ / 4) * Kr n ^ 2 := hFlog
    have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by positivity
    have hsum : Real.log (m n) + Real.log (aeval zeta7 (F n)) ≤
        (Aeff + U + δ / 4 + δ / 4) * (1600 * (n : ℝ) ^ 2) := by
      have hg := mul_le_mul_of_nonneg_right hlog_growth (by positivity : (0:ℝ) ≤ 1600 * (n:ℝ)^2)
      have hr := mul_le_mul_of_nonneg_right hFlog (by positivity : (0:ℝ) ≤ 1600 * (n:ℝ)^2)
      rw [add_mul] at hg hr
      linarith
    have hcoef : (Aeff + U + δ / 4 + δ / 4 : ℝ) = -δ / 2 := by rw [hδ_def]; ring
    rw [hcoef] at hsum
    have e2 : -δ / 2 * (1600 * (n : ℝ) ^ 2) = -800 * δ * (n : ℝ) ^ 2 := by ring
    linarith

end Zeta7
