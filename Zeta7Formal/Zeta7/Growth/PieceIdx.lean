import Mathlib

/-!
# 分区定位（b-无关）

对严格递增网格 `t 0 < t 1 < … < t m`，`pieceIdx t m x` 是含
`x ∈ [t 0, t m)` 的段 `[t i, t (i+1))` 的下标。
镜像 `Apery/Growth/PieceIdx.lean`。
-/

namespace Zeta7

open Classical in
/-- 含 `x` 的段。 -/
noncomputable def pieceIdx (t : ℕ → ℝ) (m : ℕ) (x : ℝ) : ℕ := Nat.findGreatest (fun i => t i ≤ x) m

lemma grid_mono {t : ℕ → ℝ} {m : ℕ} (h : ∀ i < m, t i < t (i + 1)) {i j : ℕ} (hij : i ≤ j) (hj : j ≤ m) :
    t i ≤ t j := by
  induction j with
  | zero => have this : i = 0 := by omega
            rw [this]
  | succ j ih =>
    rcases Nat.lt_or_ge i (j + 1) with h1 | h1
    · exact (ih (by omega) (by omega)).trans (h j (by omega)).le
    · have this : i = j + 1 := by omega
      rw [this]

/-- `x ∈ [t 0, t m)` 落在段 `pieceIdx t m x`。 -/
lemma pieceIdx_spec {t : ℕ → ℝ} {m : ℕ} (h : ∀ i < m, t i < t (i + 1)) {x : ℝ}
    (h0 : t 0 ≤ x) (hm : x < t m) :
    pieceIdx t m x < m ∧ t (pieceIdx t m x) ≤ x ∧ x < t (pieceIdx t m x + 1) := by
  classical
  unfold pieceIdx
  set i := Nat.findGreatest (fun i => t i ≤ x) m with hi
  have hspec : t i ≤ x := Nat.findGreatest_spec (P := fun i => t i ≤ x) (Nat.zero_le m) h0
  have hle : i ≤ m := Nat.findGreatest_le m
  have hlt : i < m := by
    rcases Nat.lt_or_ge i m with h1 | h1
    · exact h1
    · have this : i = m := by omega
      rw [this] at hspec; linarith
  refine ⟨hlt, hspec, ?_⟩
  by_contra hc
  rw [not_lt] at hc
  have this := Nat.findGreatest_is_greatest (P := fun i => t i ≤ x) (n := m) (k := i + 1) (by omega)
    (by omega)
  exact this hc

/-- 段 `i` 内部下标即 `i`。 -/
lemma pieceIdx_eq {t : ℕ → ℝ} {m : ℕ} (h : ∀ i < m, t i < t (i + 1)) {i : ℕ} (hi : i < m) {x : ℝ}
    (hx : x ∈ Set.Ico (t i) (t (i + 1))) : pieceIdx t m x = i := by
  classical
  unfold pieceIdx
  rw [Nat.findGreatest_eq_iff]
  refine ⟨hi.le, fun _ => hx.1, fun j hj1 hj2 => ?_⟩
  have this := grid_mono h (show i + 1 ≤ j by omega) hj2
  exact not_le.mpr (lt_of_lt_of_le hx.2 this)

end Zeta7
