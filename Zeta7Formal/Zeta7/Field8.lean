import Mathlib
import Zeta7.Measure7

/-!
# b=8 外场的闭式（A.5 类比）

`∫₀^c log(t + u²) du = c log(t + c²) - 2c + 2√t arctan(c/√t)`（t > 0），故
`V₈(t) = log(1+t) - 8α log(t+α²) - 2 + 16α + 2√t (π + arctan(1/√t) - 8 arctan(α/√t))`，
α = 1/40（镜像 `Apery/PotentialV.lean`；微积分部分与 b 无关，系数 6/12 → 8/16）。
-/

open Filter Topology Set MeasureTheory

namespace Zeta7

/-- b=8 外场（式 (6.1) 类比）：`V₈(t) = 2π√t + ∫₀¹ log(t+u²) du - 8 ∫₀^α log(t+u²) du`。 -/
noncomputable def Vfield8 (t : ℝ) : ℝ :=
  2 * Real.pi * Real.sqrt t + (∫ u in (0 : ℝ)..1, Real.log (t + u ^ 2)) -
    8 * ∫ u in (0 : ℝ)..(1 / 40 : ℝ), Real.log (t + u ^ 2)

/-- `u ↦ log (t + u²)` 的原函数（与 b 无关）。 -/
noncomputable def GVpot8 (t u : ℝ) : ℝ :=
  u * Real.log (t + u ^ 2) - 2 * u + 2 * Real.sqrt t * Real.arctan (u / Real.sqrt t)

lemma hasDerivAt_GV8 {t : ℝ} (ht : 0 < t) (u : ℝ) : HasDerivAt (GVpot8 t) (Real.log (t + u ^ 2)) u := by
  have hs : 0 < Real.sqrt t := Real.sqrt_pos.mpr ht
  have hs2 : Real.sqrt t ^ 2 = t := Real.sq_sqrt ht.le
  have h1 : HasDerivAt (fun u : ℝ => u * Real.log (t + u ^ 2))
      (1 * Real.log (t + u ^ 2) + u * ((2 * u) / (t + u ^ 2))) u := by
    have hlog : HasDerivAt (fun u : ℝ => Real.log (t + u ^ 2)) ((2 * u) / (t + u ^ 2)) u := by
      have := ((hasDerivAt_pow 2 u).const_add t).log (by positivity)
      simpa using this
    exact (hasDerivAt_id u).mul hlog
  have h2 : HasDerivAt (fun u : ℝ => 2 * u) 2 u := by simpa using (hasDerivAt_id u).const_mul 2
  have h3 : HasDerivAt (fun u : ℝ => 2 * Real.sqrt t * Real.arctan (u / Real.sqrt t))
      (2 * Real.sqrt t * ((1 / (1 + (u / Real.sqrt t) ^ 2)) * (1 / Real.sqrt t))) u := by
    have := ((hasDerivAt_id u).div_const (Real.sqrt t)).arctan
    simpa using this.const_mul (2 * Real.sqrt t)
  have h := (h1.sub h2).add h3
  refine h.congr_deriv ?_
  have hne : t + u ^ 2 ≠ 0 := by positivity
  field_simp
  rw [hs2]
  ring

/-- `∫₀^c log(t + u²) du = c log(t + c²) - 2c + 2√t arctan(c/√t)`（t > 0）。 -/
lemma integral_log_add_sq8 {t : ℝ} (ht : 0 < t) (c : ℝ) :
    ∫ u in (0 : ℝ)..c, Real.log (t + u ^ 2) =
      c * Real.log (t + c ^ 2) - 2 * c + 2 * Real.sqrt t * Real.arctan (c / Real.sqrt t) := by
  have := intervalIntegral.integral_eq_sub_of_hasDerivAt (a := 0) (b := c) (f := GVpot8 t)
    (f' := fun u => Real.log (t + u ^ 2)) (fun u _ => hasDerivAt_GV8 ht u)
    ((Continuous.log (by fun_prop) (fun u => by positivity)).intervalIntegrable _ _)
  rw [this]
  simp [GVpot8]

/-- **(A.5) 类比**：b=8 外场的闭式。 -/
theorem Vfield8_eq {t : ℝ} (ht : 0 < t) :
    Vfield8 t = Real.log (1 + t) - 8 * (1 / 40) * Real.log (t + (1 / 40) ^ 2) - 2 + 16 * (1 / 40) +
      2 * Real.sqrt t * (Real.pi + Real.arctan (1 / Real.sqrt t) - 8 * Real.arctan ((1 / 40) / Real.sqrt t)) := by
  unfold Vfield8
  rw [integral_log_add_sq8 ht, integral_log_add_sq8 ht]
  ring_nf

end Zeta7
