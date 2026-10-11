import Mathlib
import Zeta7.Growth.PieceIdx

/-!
# 分段线性函数 / x³ 的积分（b-无关）

`∫_a^b (A x + B)/x³ dx = A(1/a − 1/b) + B/2·(1/a² − 1/b²)`。
镜像 `Apery/Growth/TableIntegrals.lean` 的 `integral_lin_div_cube`
（内/外表积分本身依赖 b=8 表数据，待研究侧管道产出后登记）。
-/

open Finset intervalIntegral

namespace Zeta7

lemma integral_lin_div_cube (A B : ℝ) {a b : ℝ} (ha : 0 < a) (hab : a ≤ b) :
    ∫ x in a..b, (A * x + B) / x ^ 3 = A * (1 / a - 1 / b) + B / 2 * (1 / a ^ 2 - 1 / b ^ 2) := by
  have hpos : ∀ x ∈ Set.uIcc a b, 0 < x := by
    intro x hx; rcases Set.mem_uIcc.mp hx with h | h <;> linarith [h.1]
  have hb : 0 < b := by linarith
  rw [integral_eq_sub_of_hasDerivAt (f := fun x => -A / x - B / 2 / x ^ 2)]
  · field_simp; ring
  · intro x hx
    have hx0 := (hpos x hx).ne'
    have d1 := (hasDerivAt_const x (-A)).div (hasDerivAt_id x) hx0
    have d2 := (hasDerivAt_const x (B / 2)).div (hasDerivAt_pow 2 x) (pow_ne_zero 2 hx0)
    have this := d1.sub d2
    refine this.congr_deriv ?_
    simp only [id]
    field_simp
    ring
  · apply ContinuousOn.intervalIntegrable
    apply ContinuousOn.div (by fun_prop) (by fun_prop)
    intro x hx; exact pow_ne_zero 3 (hpos x hx).ne'

end Zeta7
