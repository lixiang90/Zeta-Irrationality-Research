import Li2Rational.LargePrimes
import Li2.RationalPrimeLog

open Li2
namespace Li2Rational.Family
noncomputable section
variable [Parameter] [Nondegenerate]

abbrev rationalNumerator : ℤ := Parameter.value.num
abbrev rationalDenominator : ℤ := Parameter.value.den

lemma rationalNumerator_ne_zero : rationalNumerator ≠ 0 := by
  intro h
  exact Nondegenerate.ne_zero (Rat.num_eq_zero.mp h)
omit [Nondegenerate] in
lemma rationalDenominator_ne_zero : rationalDenominator ≠ 0 := by
  exact_mod_cast Parameter.value.den_nz
omit [Nondegenerate] in
lemma rationalData_eq : Parameter.value = (rationalNumerator:ℚ)/rationalDenominator := by
  simp only [rationalDenominator,rationalNumerator,Int.cast_natCast,Rat.num_div_den]
lemma rationalData_distinct : rationalNumerator ≠ rationalDenominator := by
  intro h
  have he := rationalData_eq
  rw [h,div_self (by exact_mod_cast rationalDenominator_ne_zero)] at he
  exact Nondegenerate.ne_one he
omit [Nondegenerate] in
lemma rationalData_coprime (p : ℕ) (hp : p.Prime) :
    ¬((p:ℤ) ∣ rationalNumerator ∧ (p:ℤ) ∣ rationalDenominator) := by
  rintro ⟨ha,hb⟩
  have han : p ∣ Parameter.value.num.natAbs := Int.natCast_dvd.mp ha
  have hbn : p ∣ Parameter.value.den := by exact_mod_cast hb
  have h := Nat.dvd_gcd han hbn
  rw [Parameter.value.reduced.gcd_eq_one] at h
  exact hp.ne_one (Nat.dvd_one.mp h)

def arithmeticCutoff (a b : ℤ) : ℕ := 5+a.natAbs+b.natAbs+(b-a).natAbs

omit [Parameter] [Nondegenerate] in
lemma arithmeticCutoff_not_dvd {a b : ℤ} (ha : a ≠ 0) (hb : b ≠ 0) (hab : a ≠ b)
    {p : ℕ} (hp : arithmeticCutoff a b < p) :
    ¬(p:ℤ) ∣ a ∧ ¬(p:ℤ) ∣ b ∧ ¬(p:ℤ) ∣ b-a := by
  have h (m : ℤ) (hm : m ≠ 0) (hmp : m.natAbs < p) : ¬(p:ℤ) ∣ m := by
    intro hd
    exact Nat.not_dvd_of_pos_of_lt (Int.natAbs_pos.mpr hm) hmp (Int.natCast_dvd.mp hd)
  unfold arithmeticCutoff at hp
  exact ⟨h a ha (by omega),h b hb (by omega),h (b-a) (sub_ne_zero.mpr hab.symm) (by omega)⟩

end
end Li2Rational.Family
