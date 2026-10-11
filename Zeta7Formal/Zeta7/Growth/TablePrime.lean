import Mathlib
import Zeta7.Growth.TailPrime

/-!
# 内区连续形式：`-L_p ≤ p Ê(K/p, k) + C`

`Ê(x, k) = -2u⌊x⌋ + 16u⌊αx⌋ + 2J(u) - uk + 2 ∑_{i,j} b_{ij}(k) c_{ij}({x}, {αx})`，
其中 `u = λx`，`b_{ij}` 是类函数 `ψ(k, B + 8a' - a)` 在基 `1, A, E` 下的系数，
`c_{ij}` 是连续区间计数。（b=8 版：`16`、`−6`、`8a'`。）
-/

open Finset

namespace Zeta7

/-- 类函数系数（b=8：`16q' − 2q − 6 + 8b − a`）。 -/
noncomputable def bIn (q q' : ℕ) (k : ℤ) (i j : Fin 3) : ℝ :=
  bcoef (fun a => bcoef (fun b => (psiR k (16 * (q' : ℤ) - 2 * (q : ℤ) - 6 + 8 * (b : ℤ) - a) : ℝ)) j) i

/-- **内区连续函数。** -/
noncomputable def Ein (x : ℝ) (k : ℤ) : ℝ :=
  -2 * (37 / 40 * x) * (⌊x⌋₊ : ℝ) + 16 * (37 / 40 * x) * (⌊3 / 40 * x⌋₊ : ℝ) + 2 * Jc (37 / 40 * x) -
    37 / 40 * x * k +
    2 * ∑ i, ∑ j, bIn ⌊x⌋₊ ⌊3 / 40 * x⌋₊ k i j * ccount (Int.fract x) (Int.fract (3 / 40 * x)) i j

/-- 表界加性误差。 -/
noncomputable def Ctab (n p : ℕ) (k : ℤ) : ℝ :=
  5 * ∑ i, ∑ j, |bIn (40 * n / p) (3 * n / p) k i j| +
    ((ktopI n p - kloI n p : ℤ) : ℝ) * (L0I n p : ℝ) + 2 * Bmax n p + 1

variable {p : ℕ} [hp : Fact p.Prime]

section
variable {n : ℕ} (hn : 33 ≤ n) (hodd : 2 * (p / 2) + 1 = p) (hp7 : 7 ≤ p)
  (hsmall : ¬ p * Mcut ≤ 40 * n) (hin : 3 * p ≤ 40 * n) (hsq : 2 * (40 * n) < p ^ 2)
  (hdeg : 7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2)

set_option maxHeartbeats 1000000 in
include hn hodd hp7 hsmall hin hsq hdeg in
/-- **内区连续形式上界。** -/
theorem table_Lp_le (k : ℤ) (hk1 : kloI n p ≤ k) (hk2 : k ≤ ktopI n p) :
    -(Lp n p : ℝ) ≤ (p : ℝ) * Ein (40 * n / p) k + Ctab n p k := by
  have hp0 : 0 < p := by omega
  have hpR0 : (0 : ℝ) < p := by exact_mod_cast hp0
  have main := inner_Lp_le hn hodd hp7 hsmall hin hsq hdeg k hk1 hk2
  -- 取整与小数部分
  have hx : (40 * n / p : ℝ) = ((40 * n : ℕ) : ℝ) / (p : ℕ) := by push_cast; ring
  have hfl : ⌊(40 * n / p : ℝ)⌋₊ = 40 * n / p := by rw [hx, Nat.floor_div_eq_div]
  have hfl' : ⌊(3 : ℝ) / 40 * (40 * n / p)⌋₊ = 3 * n / p := by
    rw [show (3 : ℝ) / 40 * (40 * n / p) = ((3 * n : ℕ) : ℝ) / (p : ℕ) by push_cast; ring,
      Nat.floor_div_eq_div]
  have hfK : Int.fract ((40 * n / p : ℝ)) = ((40 * n % p : ℕ) : ℝ) / p := by
    rw [hx]; exact Int.fract_div_natCast_eq_div_natCast_mod
  have hfN : Int.fract ((3 : ℝ) / 40 * (40 * n / p)) = ((3 * n % p : ℕ) : ℝ) / p := by
    rw [show (3 : ℝ) / 40 * (40 * n / p) = ((3 * n : ℕ) : ℝ) / (p : ℕ) by push_cast; ring]
    exact Int.fract_div_natCast_eq_div_natCast_mod
  -- 类和
  have hcs := class_sum_approx hodd (Nat.mod_lt (40 * n) hp0) (Nat.mod_lt (3 * n) hp0)
    (hIn n p k)
  have hb : ∀ i j, bcoef (fun a => bcoef (fun b => hIn n p k a b) j) i =
      bIn (40 * n / p) (3 * n / p) k i j := fun i j => rfl
  simp only [hb] at hcs
  rw [abs_le] at hcs
  -- layer 项
  have hlay : 2 * layer p 1000 (37 * n : ℕ) = (p : ℝ) * (2 * Jc (37 / 40 * (40 * n / p))) := by
    rw [layer_eq hp0]
    have : ((37 * n : ℕ) : ℝ) / p = 37 / 40 * (40 * n / p) := by push_cast; ring
    rw [this]; ring
  unfold Ein Ctab
  rw [hfl, hfl', hfK, hfN]
  have e1 : ((37 * n : ℕ) : ℝ) = (p : ℝ) * (37 / 40 * (40 * n / p)) := by
    push_cast; field_simp
  rw [hlay] at main
  rw [e1] at main
  have hE : ((k - kloI n p : ℤ) : ℝ) * (L0I n p : ℝ) ≤ ((ktopI n p - kloI n p : ℤ) : ℝ) * (L0I n p : ℝ) := by
    apply mul_le_mul_of_nonneg_right _ (by positivity)
    exact_mod_cast (show k - kloI n p ≤ ktopI n p - kloI n p by omega)
  nlinarith [hcs.2, hE]

end

end Zeta7
