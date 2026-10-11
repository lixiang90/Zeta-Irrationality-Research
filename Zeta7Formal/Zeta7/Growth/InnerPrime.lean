import Mathlib
import Zeta7.Growth.ClassData
import Zeta7.Norm

/-!
# 内区：`-L_p` 的每素数上界（镜像 `Apery/Growth/InnerPrime.lean`，b=8）

`K/400 < p ≤ K/3`（且 `n` 足够大使边条件成立）时，每个 `k ∈ [klo, ktop]` 给出
`-L_p ≤ -2h q + 16h q' + 2T(h) - hk + 2∑_{c=1}^m ψ(k, B + 8a'_c - a_c) + (k-klo)L₀ + 2B₀ + 1`，
`q = ⌊K/p⌋`，`q' = ⌊N/p⌋`，`B = 16q' - 2q - 6`（b=8；b=6 为 `12q' - 2q - 4`、`6a'`），
类计数 `a_c, a'_c` 见 `ClassSum`，层蛋糕 `T` 见 `ClassData`。

b=8 差异：`12h q' → 16h q'`（vS 的 `(N!)^{16h}`）、`B` 与 `hIn` 的 `12→16`、
`−4→−6`、`6a'→8a'`；`Bse_zero` 的 `5+12q'−2q → 7+16q'−2q`；hdeg `7+2(24n+74n)`。
-/

open Finset

namespace Zeta7

variable {p : ℕ} [hp : Fact p.Prime]

lemma sum_erase_zero_eq_Icc {m : ℕ} (F : ℕ → ℚ) :
    ∑ c ∈ (univ : Finset (Fin (m + 1))).erase 0, F c = ∑ c ∈ Icc 1 m, F c := by
  have h1 := Finset.add_sum_erase (univ : Finset (Fin (m + 1))) (fun c => F c) (Finset.mem_univ 0)
  rw [Fin.sum_univ_eq_sum_range (fun c => F c), Finset.sum_range_eq_add_Ico _ (by omega)] at h1
  simp only [Fin.val_zero] at h1
  have h2 : Ico 1 (m + 1) = Icc 1 m := by ext c; simp only [Finset.mem_Ico, Finset.mem_Icc]; omega
  rw [h2] at h1
  linarith

/-- 内外区的 `-v_p(S_K)`（b=8：`(N!)^{16h}` 给 `16h⌊N/p⌋`）。 -/
lemma neg_vSK_le {n : ℕ} (hn : 1 ≤ n) (hp3 : 3 ≤ p) (hN : 3 * n < p ^ 2)
    (hH : 2 * (37 * n) < p ^ 2) (J : ℕ) (hJ : 2 * (37 * n) ≤ J * p) :
    -(vSK n p : ℝ) ≤ -2 * (37 * n : ℕ) * ((40 * n / p : ℕ) : ℝ) +
      16 * (37 * n : ℕ) * ((3 * n / p : ℕ) : ℝ) + 2 * layer p J (37 * n : ℕ) := by
  have h := vS_eq (by omega : 0 < n) hp.out
  have e : vSK n p = (InnerData.mk n 200 p).vS := rfl
  rw [e, h]
  have h1 := padicValNat_factorial_ge (p := p) (k := 40 * n)
  have h2 := padicValNat_factorial_small (p := p) (k := 3 * n) hN
  have h3 : ∀ i ∈ Icc 1 (37 * n - 1), padicValNat p (2 * i).factorial = 2 * i / p := fun i hi =>
    padicValNat_factorial_small (by have := (Finset.mem_Icc.mp hi).2; omega)
  have hsum : (((∑ i ∈ Icc 1 (37 * n - 1), 2 * i / p : ℕ)) : ℝ) ≤ layer p J (37 * n : ℕ) := by
    have := sum_floor_le_layer (p := p) J (37 * n) hJ
    rw [Finset.sum_range_eq_add_Ico _ (by omega)] at this
    have e2 : Ico 1 (37 * n) = Icc 1 (37 * n - 1) := by
      ext c; simp only [Finset.mem_Ico, Finset.mem_Icc]; omega
    rw [e2] at this
    rw [Nat.cast_sum]
    simpa using this
  have hs : ∑ i ∈ Icc 1 (37 * n - 1), (padicValNat p (2 * i).factorial : ℤ) =
      ((∑ i ∈ Icc 1 (37 * n - 1), 2 * i / p : ℕ) : ℤ) := by
    rw [Nat.cast_sum]; exact Finset.sum_congr rfl (fun i hi => by rw [h3 i hi])
  rw [hs, h2]
  generalize padicValNat p (40 * n).factorial = A at h1 ⊢
  generalize padicValNat p 4 = B
  generalize (∑ i ∈ Icc 1 (37 * n - 1), 2 * i / p) = Sg at hsum ⊢
  generalize 40 * n / p = q at h1 ⊢
  generalize 3 * n / p = q'
  have h1R : (q : ℝ) ≤ (A : ℝ) := by exact_mod_cast h1
  have hB : (0 : ℝ) ≤ (B : ℝ) := by positivity
  have hnR : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  push_cast at hsum ⊢
  nlinarith [mul_le_mul_of_nonneg_left h1R (show (0 : ℝ) ≤ 74 * n by positivity),
    mul_nonneg (show (0 : ℝ) ≤ 37 * n - 1 by linarith) hB]

/-- 零类亏界（b=8：`7 + 16q' − 2q`、`−6`）。 -/
noncomputable def Bmax (n p : ℕ) : ℝ :=
  max 0 ((ktopI n p : ℝ) / 2 - ((7 + 16 * ((3 * n / p : ℕ) : ℝ) - 2 * ((40 * n / p : ℕ) : ℝ)) - 6) / 2) *
    (max 0 ((ktopI n p : ℝ) / 2 - ((7 + 16 * ((3 * n / p : ℕ) : ℝ) - 2 * ((40 * n / p : ℕ) : ℝ)) - 6) / 2) / 2 + 1)

/-- 内区类函数（b=8：`16q' − 2q − 6 + 8a' − a`）。 -/
noncomputable def hIn (n p : ℕ) (k : ℤ) (a a' : ℕ) : ℝ :=
  (psiR k (16 * ((3 * n / p : ℕ) : ℤ) - 2 * ((40 * n / p : ℕ) : ℤ) - 6 + 8 * (a' : ℤ) - a) : ℝ)

section
variable {n : ℕ} (hn : 33 ≤ n) (hodd : 2 * (p / 2) + 1 = p) (hp7 : 7 ≤ p)
  (hsmall : ¬ p * Mcut ≤ 40 * n) (hin : 3 * p ≤ 40 * n) (hsq : 2 * (40 * n) < p ^ 2)
  (hdeg : 7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2)

include hodd in
lemma betaI_eq {c : ℕ} (hc1 : 1 ≤ c) (hcm : c ≤ p / 2) :
    betaI n p (m := p / 2) (⟨c, by omega⟩ : Fin (p / 2 + 1)) =
      16 * ((3 * n / p : ℕ) : ℤ) - 2 * ((40 * n / p : ℕ) : ℤ) - 6 +
        8 * (aCnt p (3 * n % p) c : ℤ) - aCnt p (40 * n % p) c := by
  unfold betaI
  simp only
  rw [SX_class hodd hc1 hcm, SX_class hodd hc1 hcm]
  push_cast; ring

include hodd hsmall in
lemma q_lt : 40 * n / p < 400 := by
  unfold Mcut at hsmall
  rw [not_le] at hsmall
  exact (Nat.div_lt_iff_lt_mul (by omega)).mpr (by linarith)

include hodd in
lemma klo_le_beta (c : Fin (p / 2 + 1)) (hc : c ≠ 0) : kloI n p ≤ betaI n p c := by
  have hc1 : 1 ≤ (c : ℕ) := by
    rcases Nat.eq_zero_or_pos (c : ℕ) with h | h
    · exact absurd (Fin.ext h) hc
    · exact h
  have hcm := Nat.lt_succ_iff.mp c.isLt
  have e := betaI_eq (n := n) hodd hc1 hcm
  simp only [Fin.eta] at e
  rw [e]
  unfold kloI aCnt
  generalize 3 * n / p = q' at *
  generalize 40 * n / p = q at *
  split_ifs <;> omega

include hodd in
lemma rowsK_klo : rowsK (betaI n p (m := p / 2)) (kloI n p) = 0 := by
  unfold rowsK
  refine Finset.sum_eq_zero fun c hc => ?_
  have := klo_le_beta (n := n) hodd c (Finset.mem_erase.mp hc).1
  unfold lrow; omega

include hodd in
lemma Bse_eq_beta (c : Fin (p / 2 + 1)) (hc : c ≠ 0) :
    Bse p (40 * n) (3 * n) (c : ℕ) = (betaI n p c : ℚ) + 6 := by
  have hc0 : (c : ℕ) ≠ 0 := fun h => hc (Fin.ext h)
  unfold Bse betaI
  rw [if_neg hc0]
  push_cast; ring

lemma Bse_zero_eq : Bse p (40 * n) (3 * n) 0 = 7 + 16 * ((3 * n / p : ℕ) : ℚ) - 2 * ((40 * n / p : ℕ) : ℚ) := by
  unfold Bse
  simp only [if_pos, Nat.cast_zero, Int.cast_zero]
  rw [SX_zero, SX_zero]
  push_cast; ring

include hn hodd hp7 hsmall hin hsq hdeg in
/-- 内区边条件成立。 -/
lemma innerOK_of : InnerOK n p := by
  have hm1 : 1 ≤ p / 2 := by omega
  set β := betaI n p (m := p / 2) with hβdef
  have hq := q_lt hodd hsmall
  have hlo : rowsK β (kloI n p) + L0I n p ≤ 37 * n := by
    rw [rowsK_klo hodd]; unfold L0I; omega
  set kf := kfSel β (37 * n) (L0I n p) (kloI n p) (ktopI n p) with hkf
  have hfeas : rowsK β kf + L0I n p ≤ 37 * n :=
    kfSel_feasible β (37 * n) (L0I n p) (kloI n p) (ktopI n p) hlo
  have hkfle : kf ≤ ktopI n p := kfSel_le β (37 * n) (L0I n p) (kloI n p) (ktopI n p) (by
    unfold kloI ktopI; generalize 40 * n / p = q; omega)
  have hβ : ∀ c : Fin (p / 2 + 1), c ≠ 0 → Bse p (40 * n) (3 * n) (c : ℕ) = (β c : ℚ) + 6 :=
    fun c hc => Bse_eq_beta hodd c hc
  refine ⟨hodd, hm1, hp7, Sep_PlK hsq, by nlinarith, hdeg, ?_, ?_⟩
  · exact sum_allocK β (37 * n) kf (by omega)
  · -- 零类条件
    have h1 := tmin_allocK_le hm1 (Bse p (40 * n) (3 * n)) β hβ (37 * n) kf
    have hA0 : allocI n p (p / 2) 0 = 37 * n - rowsK β kf := by
      unfold allocI allocK; rw [if_pos rfl]
    have hL0 : L0I n p ≤ allocI n p (p / 2) 0 := by rw [hA0]; omega
    have hL0R : ((L0I n p : ℕ) : ℚ) ≤ (allocI n p (p / 2) 0 : ℚ) := by exact_mod_cast hL0
    rw [Bse_zero_eq]
    have hb1 : (β ⟨1, by omega⟩ : ℚ) ≤ 16 * ((3 * n / p : ℕ) : ℚ) + 10 := by
      have e := betaI_eq (n := n) hodd (c := 1) le_rfl (by omega)
      have : β ⟨1, by omega⟩ ≤ 16 * ((3 * n / p : ℕ) : ℤ) + 10 := by
        rw [hβdef, e]; unfold aCnt; generalize 3 * n / p = q' at *; generalize 40 * n / p = q at *
        split_ifs <;> omega
      have h' := (Int.cast_le (R := ℚ)).mpr this
      rw [Int.cast_add, Int.cast_mul, Int.cast_natCast] at h'
      norm_num at h'
      exact h'
    have hkfR : (kf : ℚ) ≤ ktopI n p := by exact_mod_cast hkfle
    unfold ktopI at hkfR
    unfold L0I at hL0R
    rw [Int.cast_add, Int.cast_mul, Int.cast_natCast] at hkfR
    norm_num at hkfR
    push_cast at hL0R
    refine h1.trans ?_
    rw [div_le_iff₀ (by norm_num : (0 : ℚ) < 2)]
    have hq0 : (0 : ℚ) ≤ ((40 * n / p : ℕ) : ℚ) := by positivity
    have hq0' : (0 : ℚ) ≤ ((3 * n / p : ℕ) : ℚ) := by positivity
    refine max_le ?_ ?_ <;> linarith

include hn hodd hp7 hsmall hin hsq hdeg in
/-- **内区每素数上界**（离散形式）。 -/
theorem inner_Lp_le (k : ℤ) (hk1 : kloI n p ≤ k) (hk2 : k ≤ ktopI n p) :
    -(Lp n p : ℝ) ≤ -2 * (37 * n : ℕ) * ((40 * n / p : ℕ) : ℝ) +
      16 * (37 * n : ℕ) * ((3 * n / p : ℕ) : ℝ) + 2 * layer p 1000 (37 * n : ℕ) -
      (37 * n : ℕ) * (k : ℝ) +
      2 * ∑ c ∈ Icc 1 (p / 2), hIn n p k (aCnt p (40 * n % p) c) (aCnt p (3 * n % p) c) +
      ((k - kloI n p : ℤ) : ℝ) * (L0I n p : ℝ) + 2 * Bmax n p + 1 := by
  have hm1 : 1 ≤ p / 2 := by omega
  have hOK := innerOK_of hn hodd hp7 hsmall hin hsq hdeg
  have hLp : Lp n p = vSK n p + ⌊2 * WI n p⌋ := by
    unfold Lp; rw [if_neg hsmall, if_pos hin, if_pos hOK]
  have hq := q_lt hodd hsmall
  -- `v_p(S_K)`
  have hv := neg_vSK_le (p := p) (n := n) (by omega) (by omega) (by nlinarith) (by nlinarith) 1000
    (by
      unfold Mcut at hsmall; rw [not_le] at hsmall
      nlinarith)
  -- 分配
  set β := betaI n p (m := p / 2) with hβdef
  have hlo : rowsK β (kloI n p) + L0I n p ≤ 37 * n := by
    rw [rowsK_klo hodd]; unfold L0I; omega
  set kf := kfSel β (37 * n) (L0I n p) (kloI n p) (ktopI n p) with hkf
  have hfeas : rowsK β kf + L0I n p ≤ 37 * n :=
    kfSel_feasible β (37 * n) (L0I n p) (kloI n p) (ktopI n p) hlo
  have hkfle : kf ≤ ktopI n p := kfSel_le β (37 * n) (L0I n p) (kloI n p) (ktopI n p) (by
    unfold kloI ktopI; generalize 40 * n / p = q; omega)
  have hβ : ∀ c : Fin (p / 2 + 1), c ≠ 0 → Bse p (40 * n) (3 * n) (c : ℕ) = (β c : ℚ) + 6 :=
    fun c hc => Bse_eq_beta hodd c hc
  have hW := sum_wcap_allocK hm1 (Bse p (40 * n) (3 * n)) β hβ (37 * n) kf (by omega)
  have hWI : WI n p = ∑ s, wcap hm1 (allocK β (37 * n) kf) (Bse p (40 * n) (3 * n)) s := by
    unfold WI; rw [dif_pos hm1]; rfl
  rw [← hWI] at hW
  have hPhi := PhiK_le_kf β (37 * n) (L0I n p) (kloI n p) (ktopI n p) hlo hk1 hk2
  -- `Φ(k)` 写成类和
  have hsumQ : ∑ c ∈ (univ : Finset (Fin (p / 2 + 1))).erase 0, psiR k (β c) =
      ∑ c ∈ Icc 1 (p / 2), psiR k (16 * ((3 * n / p : ℕ) : ℤ) - 2 * ((40 * n / p : ℕ) : ℤ) - 6 +
        8 * (aCnt p (3 * n % p) c : ℤ) - aCnt p (40 * n % p) c) := by
    have e := sum_erase_zero_eq_Icc (m := p / 2) (fun c => psiR k
      (8 * (SX p (3 * n) (((c : ℕ) : ℤ) : ZMod p) : ℤ) - (SX p (40 * n) (((c : ℕ) : ℤ) : ZMod p) : ℤ) - 6))
    refine e.trans (Finset.sum_congr rfl fun c hc => ?_)
    have hc' := Finset.mem_Icc.mp hc
    have := betaI_eq (n := n) hodd hc'.1 hc'.2
    unfold betaI at this
    simp only at this ⊢
    rw [this]
  have hPhik : (PhiK β (37 * n) k : ℝ) = ((37 * n : ℕ) : ℝ) * k / 2 -
      ∑ c ∈ Icc 1 (p / 2), hIn n p k (aCnt p (40 * n % p) c) (aCnt p (3 * n % p) c) := by
    unfold PhiK
    rw [hsumQ]
    unfold hIn
    push_cast
    ring
  -- 零类亏
  have hB0 : max 0 ((kf : ℚ) / 2 - (Bse p (40 * n) (3 * n) 0 - 6) / 2) *
      (max 0 ((kf : ℚ) / 2 - (Bse p (40 * n) (3 * n) 0 - 6) / 2) / 2 + 1) ≤ (Bmax n p : ℝ) := by
    rw [Bse_zero_eq]
    unfold Bmax
    have hkR : ((kf : ℤ) : ℝ) ≤ ((ktopI n p : ℤ) : ℝ) := by exact_mod_cast hkfle
    push_cast
    generalize ((40 * n / p : ℕ) : ℝ) = qR
    generalize ((3 * n / p : ℕ) : ℝ) = qR'
    generalize ((ktopI n p : ℤ) : ℝ) = tR at hkR ⊢
    generalize ((kf : ℤ) : ℝ) = kR at hkR ⊢
    set D1 := max 0 (kR / 2 - (7 + 16 * qR' - 2 * qR - 6) / 2) with hD1
    set D2 := max 0 (tR / 2 - (7 + 16 * qR' - 2 * qR - 6) / 2) with hD2
    have h0 : 0 ≤ D1 := le_max_left _ _
    have h12 : D1 ≤ D2 := max_le_max (le_refl 0) (by linarith)
    nlinarith
  have hfl : ((⌊2 * WI n p⌋ : ℤ) : ℝ) ≥ 2 * (WI n p : ℝ) - 1 := by
    have := Int.lt_floor_add_one (2 * WI n p)
    have : ((2 * WI n p : ℚ) : ℝ) < ((⌊2 * WI n p⌋ : ℤ) : ℝ) + 1 := by exact_mod_cast this
    push_cast at this; linarith
  have hWR : ((PhiK β (37 * n) kf : ℚ) : ℝ) - ((max 0 ((kf : ℚ) / 2 - (Bse p (40 * n) (3 * n) 0 - 6) / 2) *
      (max 0 ((kf : ℚ) / 2 - (Bse p (40 * n) (3 * n) 0 - 6) / 2) / 2 + 1) : ℚ) : ℝ) ≤ (WI n p : ℝ) := by
    exact_mod_cast hW
  have hPR : ((PhiK β (37 * n) k : ℚ) : ℝ) ≤ ((PhiK β (37 * n) kf : ℚ) : ℝ) +
      ((k - kloI n p : ℤ) : ℝ) * (L0I n p : ℝ) / 2 := by
    have := (Rat.cast_le (K := ℝ)).mpr hPhi
    push_cast at this ⊢
    linarith
  rw [hLp]
  push_cast
  rw [hPhik] at hPR
  push_cast at hWR hB0 hv hPR
  linarith

end

end Zeta7
