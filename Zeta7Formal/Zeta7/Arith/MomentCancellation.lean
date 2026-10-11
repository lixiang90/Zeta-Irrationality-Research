import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.IntervalCases
import Mathlib.Data.Nat.Basic

/-!
The arithmetic core of the improved moment-integrality range. This small file
does not import the unfinished global normalization development.
-/
namespace Zeta7.MomentCancellation

theorem five_factors_divisible {p e : ℕ} (hp : 7 ≤ p)
    (he : e + 4 < 3 * p) (hd : (p - 1) ∣ 2 * (e + 1)) :
    p ∣ (2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) := by
  obtain ⟨j, hj⟩ := hd
  have hj5 : j ≤ 5 := by
    by_contra h
    have h6 : 6 ≤ j := by omega
    have := Nat.mul_le_mul_left (p - 1) h6
    omega
  have hj1 : 1 ≤ j := by
    by_contra h
    have hj0 : j = 0 := by omega
    rw [hj0, mul_zero] at hj
    omega
  interval_cases j
  · have h : p ∣ 2 * e + 3 := ⟨1, by omega⟩
    exact (((h.mul_right (2 * e + 4)).mul_right (2 * e + 5)).mul_right
      (2 * e + 6)).mul_right (2 * e + 7)
  · have h : p ∣ 2 * e + 4 := ⟨2, by omega⟩
    exact (((Dvd.dvd.mul_left h (2 * e + 3)).mul_right (2 * e + 5)).mul_right
      (2 * e + 6)).mul_right (2 * e + 7)
  · have h : p ∣ 2 * e + 5 := ⟨3, by omega⟩
    exact ((Dvd.dvd.mul_left h ((2 * e + 3) * (2 * e + 4))).mul_right
      (2 * e + 6)).mul_right (2 * e + 7)
  · have h : p ∣ 2 * e + 6 := ⟨4, by omega⟩
    exact (Dvd.dvd.mul_left h ((2 * e + 3) * (2 * e + 4) * (2 * e + 5))).mul_right
      (2 * e + 7)
  · have h : p ∣ 2 * e + 7 := ⟨5, by omega⟩
    exact Dvd.dvd.mul_left h ((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6))

#print axioms five_factors_divisible

end Zeta7.MomentCancellation
