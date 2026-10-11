import Zeta7.Arith.MomentVal

/-!
# Stronger integral range for the zeta(7) moments

The five factors in μmono cancel the Bernoulli denominator for
2e+2 = j(p-1), j=1,...,5. Thus the integral range extends from
e+3 < 2p to e+4 < 3p. This lemma does not alter the unfinished
global normalization chain.

Validation note (2026-09-28): the full MomentVal import did not finish loading
in the current Windows session. This file is not claimed kernel-checked here.
The five-factor cancellation itself was checked separately in
MomentCancellation.lean, with axioms [propext, Quot.sound].
-/
namespace Zeta7

variable {p : ℕ} [hp : Fact p.Prime]

theorem VG_μmono_int_strong (hp7 : 7 ≤ p) {e : ℕ}
    (he : e + 4 < 3 * p) : VG p (μmono e) 0 := by
  unfold μmono
  rw [show 2 * e + 2 = 2 * (e + 1) by ring, div_eq_mul_inv]
  have hsign : VG p ((-1 : ℚ) ^ e) 0 := by
    rcases neg_one_pow_eq_or ℚ e with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  by_cases hd : (p - 1) ∣ 2 * (e + 1)
  · obtain ⟨j, hj⟩ := hd
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
    have hprod : VG p
        (((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) : ℕ) : ℚ) 1 := by
      apply VG.of_eq
      intro hne
      rw [padicValRat.of_nat]
      have hdvd : p ∣ (2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) := by
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
      have hnonzero : (2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) ≠ 0 := by
        positivity
      have := one_le_padicValNat_of_dvd hnonzero hdvd
      exact_mod_cast this
    have := ((hsign.mul (VG_bernoulli_even (e + 1))).mul hprod).mul (VG_inv720 hp7)
    push_cast at this
    simpa using this
  · have hprod : VG p
        (((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) : ℕ) : ℚ) 0 :=
      VG.natCast _
    have := ((hsign.mul (VG_bernoulli_even_int (e + 1) hd)).mul hprod).mul (VG_inv720 hp7)
    push_cast at this
    simpa using this

#print axioms VG_μmono_int_strong

end Zeta7
