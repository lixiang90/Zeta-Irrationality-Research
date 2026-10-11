import Mathlib.Data.Nat.Log
import Mathlib.Data.Nat.MaxPowDiv
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.Tactic

/-!
# ζ(7) 形式化：H⁽⁷⁾ 调和和的 p-进赋值下界

陈述（`Zeta7/Main.lean` 的 `harmonic7_valuation`）：
`v_p(∑_{v=1}^j 1/v^7) ≥ -7·⌊log_p j⌋`。

证明思路（超度量归纳）：`j = 0` 空和；归纳步
- `p ^ padicValNat p (j+1) ∣ j+1`，故单项赋值 `v_p((j+1)⁻⁷) = -7·padicValNat p (j+1) ≥ -7·log_p (j+1)`；
- 归纳假设给出求和部分的对应下界；
- `padicValRat p` 的下凸性（`min_le_padicValRat_add`）合并两者。
-/

namespace Zeta7

open Finset

theorem harmonic7_val_aux (p j : ℕ) (hp : p.Prime) :
    padicValRat p (∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7) ≥
      -7 * (Nat.log p j : ℤ) := by
  haveI : Fact p.Prime := ⟨hp⟩
  induction j with
  | zero =>
      rw [Finset.Icc_eq_empty (by norm_num : ¬ (1 : ℕ) ≤ 0), Finset.sum_empty,
        padicValRat.zero, Nat.log_zero_right]
      norm_num
  | succ j IH =>
      -- 单步展开求和区间：sum_Icc_succ_top 给出 `∑[1,j] + f(j+1)`
      have hsum : (∑ v ∈ Finset.Icc 1 (j + 1), (1 : ℚ) / (v : ℚ) ^ 7) =
          (∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7) +
            (1 : ℚ) / ((j + 1 : ℕ) : ℚ) ^ 7 :=
        Finset.sum_Icc_succ_top (f := fun v => (1 : ℚ) / (v : ℚ) ^ 7) (by omega)
      rw [hsum]
      -- 归纳假设升级为 j+1 的下界
      have hlog : Nat.log p j ≤ Nat.log p (j + 1) := Nat.log_mono_right (Nat.le_succ j)
      have IH' : padicValRat p (∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7) ≥
          -7 * (Nat.log p (j + 1) : ℤ) := by
        rw [show (Nat.log p (j + 1) : ℤ) =
            ((Nat.log p j : ℕ) : ℤ) + ((Nat.log p (j + 1) - Nat.log p j : ℕ) : ℤ) by
              rw [Nat.cast_sub hlog]; push_cast; ring]
        omega
      -- 单项赋值界：v_p((j+1)⁻⁷) = -7·padicValNat p (j+1) ≥ -7·log_p (j+1)
      have hdvd : p ^ padicValNat p (j + 1) ∣ j + 1 := by
        refine ⟨Nat.divMaxPow (j + 1) p, ?_⟩
        rw [mul_comm]
        exact (Nat.divMaxPow_mul_pow_padicValNat p (j + 1)).symm
      have hsingle : padicValRat p ((1 : ℚ) / ((j + 1 : ℕ) : ℚ) ^ 7) ≥
          -7 * (Nat.log p (j + 1) : ℤ) := by
        rw [one_div, padicValRat.inv, padicValRat.pow, padicValRat.of_nat]
        have hle : padicValNat p (j + 1) ≤ Nat.log p (j + 1) := by
          rw [Nat.le_log_iff_pow_le hp.one_lt (Nat.succ_ne_zero j)]
          exact Nat.le_of_dvd (Nat.succ_pos j) hdvd
        omega
      -- 合并两项（超度量 + 下凸性）
      rcases eq_or_ne ((∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7) +
          (1 : ℚ) / ((j + 1 : ℕ) : ℚ) ^ 7) 0 with hz | hz
      · rw [hz, padicValRat.zero]
        have hnonneg : 0 ≤ Nat.log p (j + 1) := Nat.zero_le _
        omega
      · have hmin : min (padicValRat p (∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7))
            (padicValRat p ((1 : ℚ) / ((j + 1 : ℕ) : ℚ) ^ 7)) ≥
            -7 * (Nat.log p (j + 1) : ℤ) := le_min IH' hsingle
        have h := padicValRat.min_le_padicValRat_add (p := p) hz
        omega

end Zeta7
