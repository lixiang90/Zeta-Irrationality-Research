import Mathlib

/-!
# ζ(7) 的实数定义与 mathlib `riemannZeta` 桥接

从 `Main.lean` 拆出（Positivity 层需要 `zeta7`，而 `Main` import Positivity——
拆分为独立模块避免循环依赖；镜像 `Apery.Zeta5`）。
-/

namespace Zeta7

/-- ζ(7) 为实数（与 `Apery.zeta5` 同构的定义）。 -/
noncomputable def zeta7 : ℝ := ∑' n : ℕ, 1 / (n : ℝ) ^ 7

/-- 与 mathlib `riemannZeta` 的桥接（镜像 `Apery.riemannZeta_five`）。 -/
theorem riemannZeta_seven : riemannZeta 7 = (zeta7 : ℂ) := by
  have h := zeta_nat_eq_tsum_of_gt_one (k := 7) (by norm_num)
  rw [Nat.cast_ofNat] at h
  rw [h, zeta7, Complex.ofReal_tsum]
  push_cast
  rfl

end Zeta7
