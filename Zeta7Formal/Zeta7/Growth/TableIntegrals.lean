import Mathlib
import Zeta7.Growth.Integral
import Zeta7.Growth.InnerSum
import Zeta7.Growth.OuterTable
import Zeta7.Growth.PieceIdx

/-!
# 分段表的积分

`∑_i ∫_{t_i}^{t_{i+1}} (a_i x + b_i)/x³ dx` 内区等于 b=8 的 `120667538150827615739401/708353029541942104320000`，
外区等于 `263569/144000`（b=8 表数据）。
-/

open Finset intervalIntegral

namespace Zeta7

lemma tIn_pos (i : ℕ) (hi : i ≤ 131) : 0 < tIn i := by
  have h0 : tIn 0 = 3 := by simp [tIn, tInL]
  have := grid_mono tIn_mono (Nat.zero_le i) hi
  linarith

lemma tOut_pos (i : ℕ) (hi : i ≤ 14) : 0 < tOut i := by
  have h0 : tOut 0 = 20 / 37 := by simp [tOut, tOutL]
  have := grid_mono tOut_mono (Nat.zero_le i) hi
  linarith

set_option maxHeartbeats 8000000 in
set_option maxRecDepth 100000 in
theorem inner_integrals :
    ∑ i ∈ range 131, ∫ x in tIn i..tIn (i + 1), gIn i x / x ^ 3 =
      120667538150827615739401 / 708353029541942104320000 := by
  rw [Finset.sum_congr rfl fun i hi => by
    have hi' := Finset.mem_range.mp hi
    exact integral_lin_div_cube _ _ (tIn_pos i hi'.le) (tIn_mono i hi').le]
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, tIn, tInL, aInL, bInL,
    List.getD_cons_succ, List.getD_cons_zero]
  norm_num

set_option maxHeartbeats 8000000 in
set_option maxRecDepth 100000 in
theorem outer_integrals :
    ∑ i ∈ range 14, ∫ x in tOut i..tOut (i + 1), gOut i x / x ^ 3 = 263569 / 144000 := by
  rw [Finset.sum_congr rfl fun i hi => by
    have hi' := Finset.mem_range.mp hi
    exact integral_lin_div_cube _ _ (tOut_pos i hi'.le) (tOut_mono i hi').le]
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, tOut, tOutL, aOutL, bOutL,
    List.getD_cons_succ, List.getD_cons_zero]
  norm_num

end Zeta7
