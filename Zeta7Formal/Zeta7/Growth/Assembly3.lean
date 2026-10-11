import Mathlib
import Zeta7.Growth.Assembly2
import Zeta7.Growth.InnerSum

/-!
# Growth：三个范围的素数和

b=8 平移：`big_prime_facts` 的 hdeg `7 + 2(24n + 74n) − 80n + 1`；
`range2_le` 的尾加性 `27/16` → `43/16`；`range3_le` 的 `pieceIdx tIn 131`。
-/

open Finset Filter

namespace Zeta7

lemma range_sum_le {a b : ℕ} (F : ℕ → ℝ) (f : ℝ → ℝ) (K C : ℝ) (hC : 0 ≤ C)
    (h : ∀ k ∈ Ioc a b, k.Prime → F k ≤ k * f (K / k) + C) :
    ∑ k ∈ Ioc a b, cPrime k * F k ≤
      ∑ k ∈ Ioc a b, (k : ℝ) * cPrime k * f (K / k) + C * Chebyshev.theta b := by
  have hθ : ∑ k ∈ Ioc a b, cPrime k ≤ Chebyshev.theta b := by
    refine le_trans ?_ (sum_cPrime_le_theta b)
    apply Finset.sum_le_sum_of_subset_of_nonneg
    · intro k hk; simp only [Finset.mem_Ioc] at hk ⊢; omega
    · intro k _ _; exact cPrime_nonneg' k
  have hterm : ∀ k ∈ Ioc a b, cPrime k * F k ≤ (k : ℝ) * cPrime k * f (K / k) + C * cPrime k := by
    intro k hk
    by_cases hp : k.Prime
    · have := h k hk hp
      have hc := cPrime_nonneg' k
      nlinarith [mul_le_mul_of_nonneg_left this hc]
    · simp [cPrime, hp]
  refine (Finset.sum_le_sum hterm).trans ?_
  rw [Finset.sum_add_distrib, ← Finset.mul_sum]
  nlinarith [mul_le_mul_of_nonneg_left hθ hC]

/-- 大 `n` 下 `n/10` 以上素数的事实（b=8 hdeg：`7 + 2(24n + 74n) − 80n + 1 = 116n + 8`，
故阈值从 10400 提到 12000，hsq 相应加强为 `11600n + 900 ≤ 100k²`）。 -/
lemma big_prime_facts {n k : ℕ} (hn : 12000 ≤ n) (hk : n / 10 < k) (hp : k.Prime) :
    7 ≤ k ∧ 2 * (k / 2) + 1 = k ∧ ¬ k * Mcut ≤ 40 * n ∧ 2 * (40 * n) < k ^ 2 ∧
      7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < k ^ 2 ∧ (n : ℝ) ≤ 10 * k := by
  have h10 : n + 1 ≤ 10 * k := by omega
  have hsq : 11600 * n + 900 ≤ k ^ 2 * 100 := by nlinarith
  have hodd' : 2 * (k / 2) + 1 = k := by
    rcases Nat.even_or_odd k with ⟨j, hj⟩ | ⟨j, hj⟩
    · exfalso
      have : 2 ∣ k := ⟨j, by omega⟩
      rcases hp.eq_one_or_self_of_dvd 2 this with h | h
      · omega
      · omega
    · omega
  refine ⟨by omega, hodd', by unfold Mcut; omega, by omega, by omega, ?_⟩
  exact_mod_cast (show n ≤ 10 * k by omega)

/-- **范围 2**（内区尾段，b=8 加性 `43/16`）。 -/
lemma range2_le {n : ℕ} (hn : 12000 ≤ n) :
    ∑ k ∈ Ioc (n / 10) (2 * n), cPrime k * (-(Lp n k : ℝ)) ≤
      psum (fun x => x * Ftail x + 43 / 16) 20 400 (Kr n) + 10 ^ 7 * Chebyshev.theta (2 * n : ℕ) := by
  have hps : psum (fun x => x * Ftail x + 43 / 16) 20 400 (Kr n) =
      ∑ k ∈ Ioc (n / 10) (2 * n), (k : ℝ) * cPrime k * ((fun x => x * Ftail x + 43 / 16) (Kr n / k)) := by
    unfold psum
    rw [show (400 : ℝ) = ((400 : ℕ) : ℝ) by norm_num, show (20 : ℝ) = ((20 : ℕ) : ℝ) by norm_num,
      floor_Kr_div n 400 (by norm_num), floor_Kr_div n 20 (by norm_num),
      show 40 * n / 400 = n / 10 by omega, show 40 * n / 20 = 2 * n by omega]
  rw [hps]
  refine range_sum_le (fun k => -(Lp n k : ℝ)) (fun x => x * Ftail x + 43 / 16) (Kr n) (10 ^ 7)
    (by norm_num) fun k hk hp => ?_
  have hk' := Finset.mem_Ioc.mp hk
  obtain ⟨hp7, hodd, hsmall, hsq, hdeg, hn10⟩ := big_prime_facts hn hk'.1 hp
  have := Fact.mk hp
  have h := tail_Lp_le (p := k) (n := n) (by omega) hodd hp7 hsmall (by omega) hsq hdeg
  have hC := Ctail_le (n := n) (p := k) hp.pos (by
    unfold Mcut at hsmall; rw [not_le] at hsmall
    exact (Nat.div_lt_iff_lt_mul hp.pos).mpr (by linarith)) hn10
  have e : Kr n / k = 40 * n / k := by simp [Kr]
  simp only [e]
  linarith

/-- 内区表函数。 -/
noncomputable def fIn (x : ℝ) : ℝ := gIn (pieceIdx tIn 131 x) x

lemma tIn_zero : tIn 0 = 3 := by simp [tIn, tInL]
lemma tIn_last : tIn 131 = 20 := by simp [tIn, tInL]

/-- **范围 3**（内区表）。 -/
lemma range3_le {n : ℕ} (hn : 12000 ≤ n) :
    ∑ k ∈ Ioc (2 * n) (40 * n / 3), cPrime k * (-(Lp n k : ℝ)) ≤
      psum fIn 3 20 (Kr n) + 10 ^ 8 * Chebyshev.theta (40 * n / 3 : ℕ) := by
  have hps : psum fIn 3 20 (Kr n) =
      ∑ k ∈ Ioc (2 * n) (40 * n / 3), (k : ℝ) * cPrime k * fIn (Kr n / k) := by
    unfold psum
    rw [show (3 : ℝ) = ((3 : ℕ) : ℝ) by norm_num, show (20 : ℝ) = ((20 : ℕ) : ℝ) by norm_num,
      floor_Kr_div n 3 (by norm_num), floor_Kr_div n 20 (by norm_num),
      show 40 * n / 20 = 2 * n by omega]
  rw [hps]
  refine range_sum_le (fun k => -(Lp n k : ℝ)) fIn (Kr n) (10 ^ 8) (by norm_num) fun k hk hp => ?_
  have hk' := Finset.mem_Ioc.mp hk
  obtain ⟨hp7, hodd, hsmall, hsq, hdeg, hn10⟩ := big_prime_facts hn (by omega) hp
  have := Fact.mk hp
  have hin : 3 * k ≤ 40 * n := by have := Nat.div_mul_le_self (40 * n) 3; omega
  have hkR : (0 : ℝ) < k := by exact_mod_cast hp.pos
  set x : ℝ := 40 * n / k with hx
  have hx3 : 3 ≤ x := by
    rw [hx, le_div_iff₀ hkR]; exact_mod_cast (show 3 * k ≤ 40 * n by omega)
  have hx20 : x < 20 := by
    rw [hx, div_lt_iff₀ hkR]; exact_mod_cast (show 40 * n < 20 * k by omega)
  obtain ⟨hi, hx1, hx2⟩ := pieceIdx_spec tIn_mono (x := x) (by rw [tIn_zero]; exact hx3)
    (by rw [tIn_last]; exact hx20)
  set i := pieceIdx tIn 131 x with hidef
  have hmem : x ∈ Set.Ico (tIn i) (tIn (i + 1)) := ⟨hx1, hx2⟩
  have hkr := inner_table_k i hi x hmem
  have hfl : ⌊x⌋₊ = 40 * n / k := by
    rw [hx, show (40 * n : ℝ) / k = ((40 * n : ℕ) : ℝ) / (k : ℕ) by push_cast; ring,
      Nat.floor_div_eq_div]
  rw [hfl] at hkr
  have hk1 : kloI n k ≤ kIn i := hkr.1
  have hk2 : kIn i ≤ ktopI n k := hkr.2
  have h := table_Lp_le (p := k) (n := n) (by omega) hodd hp7 hsmall hin hsq hdeg (kIn i) hk1 hk2
  have htab := inner_table i hi x hmem
  have hq20 : 40 * n / k ≤ 20 := by
    have : 40 * n < 20 * k := by omega
    exact Nat.le_of_lt_succ ((Nat.div_lt_iff_lt_mul hp.pos).mpr (by omega))
  have hC := Ctab_le (n := n) (p := k) hq20 hk1 hk2
  unfold fIn
  rw [← hidef, ← htab]
  rw [← hx] at h
  linarith

/-- **范围 4**（外区）。 -/
lemma range4_le {n : ℕ} (hn : 12000 ≤ n) :
    ∑ k ∈ Ioc (40 * n / 3) (2 * (37 * n)), cPrime k * (-(Lp n k : ℝ)) ≤
      psum Eout (20 / 37) 3 (Kr n) + 10 ^ 5 * Chebyshev.theta (2 * (37 * n) : ℕ) := by
  have hps : psum Eout (20 / 37) 3 (Kr n) =
      ∑ k ∈ Ioc (40 * n / 3) (2 * (37 * n)), (k : ℝ) * cPrime k * Eout (Kr n / k) := by
    unfold psum
    rw [show (3 : ℝ) = ((3 : ℕ) : ℝ) by norm_num, floor_Kr_div n 3 (by norm_num), floor_Kr_outer,
      show 74 * n = 2 * (37 * n) by ring]
  rw [hps]
  refine range_sum_le (fun k => -(Lp n k : ℝ)) Eout (Kr n) (10 ^ 5) (by norm_num) fun k hk hp => ?_
  have hk' := Finset.mem_Ioc.mp hk
  obtain ⟨hp7, hodd, _, hsq, _, _⟩ := big_prime_facts hn (by omega) hp
  have := Fact.mk hp
  have hout : 40 * n < 3 * k := by
    have := Nat.lt_div_mul_add (a := 40 * n) (show 0 < 3 by norm_num); omega
  have h := outer_Lp_le (p := k) (n := n) (by omega) hodd hp7 hout hk'.2 hsq
  have hq2 : 40 * n / k ≤ 2 := Nat.le_of_lt_succ ((Nat.div_lt_iff_lt_mul hp.pos).mpr (by omega))
  have hC := Cout_le (n := n) (p := k) hq2
  have e : Kr n / k = 40 * n / k := by simp [Kr]
  rw [e]
  linarith

end Zeta7
