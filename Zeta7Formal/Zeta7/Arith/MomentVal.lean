import Mathlib
import Zeta7.Arith.DirectBound

/-!
# 多项式矩的赋值界（b=8）

`μ(t^e) = (-1)^e B_{2e+2} (2e+3)(2e+4)(2e+5)(2e+6)(2e+7)/720` 满足
`v_p ≥ -1`（`p ≥ 7`），且当 `e < 2p - 3` 时 p-integral（von Staudt–Clausen）。

镜像 `Apery/Arith/MomentVal.lean`（mo271，Apache-2.0）。b=8 差异：
* 矩公式三因子 `(2e+3)(2e+4)(2e+5)/24` → 五因子 `.../(2e+6)(2e+7)/720`；
* `VG_inv24`（24 只含素数 2、3，`p ≥ 5` 即整）→ `VG_inv720`（720 = 2⁴·3²·5，
  **素数 5 进入归一化**，假设升级为 `p ≥ 7`，即本库机器素数区）；
* `VG_μmono`/`VG_μmono_int` 的假设同步升级 `5 ≤ p` → `7 ≤ p`；
* `VG_μmono_int` 整性情形的因子整除论证按五因子重写（mo271 的三因子
  `Dvd.dvd.mul_right` 嵌套模式对五因子不可机械延伸，改为显式链——
  且原模板该处从未编译，嵌套 `_` 的 unification 行为未验证）。
-/

open Finset

namespace Zeta7

variable {p : ℕ} [hp : Fact p.Prime]

lemma VG_bernoulli_even (k : ℕ) : VG p (_root_.bernoulli (2 * k)) (-1) := by
  obtain ⟨z, hz⟩ := Bernoulli.vonStaudt_clausen k
  have e : _root_.bernoulli (2 * k) = (z : ℚ) - ∑ q ∈ range (2 * k + 2) with q.Prime ∧ (q - 1) ∣ 2 * k,
      (1 : ℚ) / q := by rw [hz]; ring
  rw [e]
  refine ((VG.intCast (p := p) z).mono (by norm_num)).sub (VG.sum _ fun q hq => ?_)
  rw [Finset.mem_filter] at hq
  have hq0 : (q : ℚ) ≠ 0 := by exact_mod_cast hq.2.1.ne_zero
  rw [one_div]
  refine VG.inv hq0 ?_
  rw [padicValRat.of_nat]
  have this : padicValNat p q ≤ 1 := by
    by_cases hpq : p = q
    · subst hpq; rw [padicValNat_self]
    · have := Fact.mk hq.2.1
      rw [padicValNat_primes hpq]; omega
  exact_mod_cast this

lemma VG_bernoulli_even_int (k : ℕ) (hk : ¬ (p - 1) ∣ 2 * k) :
    VG p (_root_.bernoulli (2 * k)) 0 := by
  obtain ⟨z, hz⟩ := Bernoulli.vonStaudt_clausen k
  have e : _root_.bernoulli (2 * k) = (z : ℚ) - ∑ q ∈ range (2 * k + 2) with q.Prime ∧ (q - 1) ∣ 2 * k,
      (1 : ℚ) / q := by rw [hz]; ring
  rw [e]
  refine (VG.intCast (p := p) z).sub (VG.sum _ fun q hq => ?_)
  rw [Finset.mem_filter] at hq
  have hq0 : (q : ℚ) ≠ 0 := by exact_mod_cast hq.2.1.ne_zero
  have hpq : p ≠ q := fun h => hk (h ▸ hq.2.2)
  rw [one_div]
  refine (VG.inv (r := 0) hq0 ?_).mono (by norm_num)
  have := Fact.mk hq.2.1
  rw [padicValRat.of_nat, padicValNat_primes hpq]; simp

/-- b=8：`720⁻¹` 在 `p ≥ 7` 时 p-integral（720 = 2⁴·3²·5，素数 5 入账）。 -/
lemma VG_inv720 (hp7 : 7 ≤ p) : VG p ((720 : ℚ)⁻¹) 0 := by
  refine (VG.inv (r := 0) (by norm_num) ?_).mono (by norm_num)
  rw [show (720 : ℚ) = ((720 : ℕ) : ℚ) by norm_num, padicValRat.of_nat, padicValNat_720 hp7]
  simp

/-- `v_p(μ(t^e)) ≥ -1`（b=8 五因子矩）。 -/
theorem VG_μmono (hp7 : 7 ≤ p) (e : ℕ) : VG p (μmono e) (-1) := by
  unfold μmono
  rw [show 2 * e + 2 = 2 * (e + 1) by ring, div_eq_mul_inv]
  have h1 : VG p ((-1 : ℚ) ^ e) 0 := by
    rcases neg_one_pow_eq_or ℚ e with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  have h3 : VG p (((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) : ℕ) : ℚ) 0 :=
    VG.natCast _
  have this := ((h1.mul (VG_bernoulli_even (e + 1))).mul h3).mul (VG_inv720 hp7)
  push_cast at this
  simpa using this

/-- `μ(t^e)` 对 `e + 3 < 2p` 为 p-integral（von Staudt–Clausen 整性情形）。 -/
theorem VG_μmono_int (hp7 : 7 ≤ p) {e : ℕ} (he : e + 3 < 2 * p) : VG p (μmono e) 0 := by
  unfold μmono
  rw [show 2 * e + 2 = 2 * (e + 1) by ring, div_eq_mul_inv]
  have h1 : VG p ((-1 : ℚ) ^ e) 0 := by
    rcases neg_one_pow_eq_or ℚ e with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  by_cases hd : (p - 1) ∣ 2 * (e + 1)
  · -- `2e + 2 = j (p - 1)` with `j ∈ {1, 2, 3}`
    obtain ⟨j, hj⟩ := hd
    have hp1 : 1 ≤ p - 1 := by omega
    have hj3 : j ≤ 3 := by
      by_contra h; rw [not_le] at h
      have this : (p - 1) * 4 ≤ (p - 1) * j := Nat.mul_le_mul_left _ h
      omega
    have hj0 : 1 ≤ j := by
      rcases Nat.eq_zero_or_pos j with h | h
      · rw [h, mul_zero] at hj; omega
      · exact h
    have hprod : VG p (((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) : ℕ) : ℚ) 1 := by
      apply VG.of_eq
      intro hne
      rw [padicValRat.of_nat]
      have hdvd : p ∣ (2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) := by
        interval_cases j
        · -- `2e + 2 = p - 1`，故 `p ∣ 2e + 3`
          have hpa : p ∣ 2 * e + 3 := ⟨1, by omega⟩
          exact (((hpa.mul_right (2 * e + 4)).mul_right (2 * e + 5)).mul_right
            (2 * e + 6)).mul_right (2 * e + 7)
        · -- `2e + 2 = 2(p - 1)`，故 `p ∣ 2e + 4`
          have hpb : p ∣ 2 * e + 4 := ⟨2, by omega⟩
          exact (((Dvd.dvd.mul_left hpb (2 * e + 3)).mul_right (2 * e + 5)).mul_right
            (2 * e + 6)).mul_right (2 * e + 7)
        · -- `2e + 2 = 3(p - 1)`，故 `p ∣ 2e + 5`
          have hpc : p ∣ 2 * e + 5 := ⟨3, by omega⟩
          exact ((Dvd.dvd.mul_left hpc ((2 * e + 3) * (2 * e + 4))).mul_right
            (2 * e + 6)).mul_right (2 * e + 7)
      have hne' : (2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) ≠ 0 := by positivity
      have this := one_le_padicValNat_of_dvd hne' hdvd
      exact_mod_cast this
    have this := ((h1.mul (VG_bernoulli_even (e + 1))).mul hprod).mul (VG_inv720 hp7)
    push_cast at this
    simpa using this
  · have h3 : VG p (((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7) : ℕ) : ℚ) 0 :=
      VG.natCast _
    have this := ((h1.mul (VG_bernoulli_even_int (e + 1) hd)).mul h3).mul (VG_inv720 hp7)
    push_cast at this
    simpa using this

end Zeta7
