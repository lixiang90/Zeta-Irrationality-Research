import Mathlib
import Zeta7.Arith.DirectBound

/-!
# 极点值的赋值界（b=8：`μ_X(1/(t + j²)) = j⁶(X - H⁽⁷⁾_j) - 1/6 + 1/(2j)`）

镜像 `Apery/Arith/PoleVal.lean`（mo271，Apache-2.0）。b=8 差异：
* 指数 5 → 7（H⁽⁵⁾ → H⁽⁷⁾、配对同余 `1/(p−u)⁵ + 1/u⁵` → `⁷`）；
* 极点权重 `j⁴` → `j⁶`；
* `VG_quarter`（1/4，需 `p ≥ 3`）→ `VG_sixth`（1/6，需 **`p ≥ 5`**）；
  故 `GV_poleValue_lt/sq/mul` 的假设 `3 ≤ p` 升级为 `5 ≤ p`（机器素数区 p ≥ 7 无碍）；
* `GV_poleValue_sq` 的界 `−5` → `−7`（H⁽⁷⁾_j 对 `j < p²` 的界 −7，即本库
  `DirectBound.VG_H7`）；`GV_poleValue_mul` 的界 `−1` 保持闭合：
  `v_p(j⁶) = 6` 与 `−7` 恰合成 `6 + (−7) = −1`（b=6 为 `4 + (−5) = −1`）；
* `GV_poleValue_congr` 无 `1/6` 参与（常数项相消），保持 `3 ≤ p`。
-/

open Finset Polynomial

namespace Zeta7

variable {p : ℕ} [hp : Fact p.Prime]

/-- `v_p(1/u) ≥ -e` if `v_p(u) ≤ e`。 -/
lemma VG_inv_nat_le {u : ℕ} (hu : u ≠ 0) {e : ℕ} (he : padicValNat p u ≤ e) :
    VG p ((u : ℚ)⁻¹) (-(e : ℚ)) := by
  refine VG.inv (by exact_mod_cast hu) ?_
  rw [padicValRat.of_nat]; exact_mod_cast he

lemma padicValNat_lt_p {u : ℕ} (hu : 1 ≤ u) (hup : u < p) : padicValNat p u = 0 :=
  padicValNat.eq_zero_of_not_dvd fun h => absurd (Nat.le_of_dvd (by omega) h) (by omega)

lemma padicValNat_lt_sq {u : ℕ} (hu : 1 ≤ u) (hup : u < p ^ 2) : padicValNat p u ≤ 1 := by
  by_contra h
  rw [not_le] at h
  have : p ^ 2 ∣ u := (padicValNat_dvd_iff_le (by omega)).mpr h
  exact absurd (Nat.le_of_dvd (by omega) this) (by omega)

lemma VG_H7_lt {j : ℕ} (hj : j < p) : VG p (H7 j) 0 := by
  unfold H7
  refine VG.sum _ fun u hu => ?_
  have hu' := Finset.mem_Icc.mp hu
  rw [one_div, show ((u : ℚ) ^ 7) = ((u ^ 7 : ℕ) : ℚ) by push_cast; ring]
  refine (VG_inv_nat_le (e := 0) (pow_ne_zero _ (by omega)) ?_).mono (by norm_num)
  rw [padicValNat.pow (p := p) u 7, padicValNat_lt_p hu'.1 (by omega)]

/-- b=8：`1/6` 在 `p ≥ 5` 时 p-integral（p=3 时 3∣6，故假设较 b=6 的 1/4 升级）。 -/
lemma VG_sixth (hp5 : 5 ≤ p) : VG p (1 / 6 : ℚ) 0 := by
  rw [one_div, show (6 : ℚ) = ((6 : ℕ) : ℚ) by norm_num]
  refine (VG_inv_nat_le (e := 0) (by norm_num) ?_).mono (by norm_num)
  rw [show (6 : ℕ) = 2 * 3 by norm_num, padicValNat.mul (by norm_num) (by norm_num)]
  have := Fact.mk Nat.prime_two
  rw [padicValNat_primes (p := p) (q := 2) (by omega)]
  have := Fact.mk Nat.prime_three
  rw [padicValNat_primes (p := p) (q := 3) (by omega)]

lemma VG_inv_2j (hp3 : 3 ≤ p) {j e : ℕ} (hj : 1 ≤ j) (he : padicValNat p j ≤ e) :
    VG p (1 / (2 * (j : ℚ))) (-(e : ℚ)) := by
  rw [one_div, show (2 * (j : ℚ)) = ((2 * j : ℕ) : ℚ) by push_cast; ring]
  refine VG_inv_nat_le (by omega) ?_
  have := Fact.mk Nat.prime_two
  rw [padicValNat.mul (by norm_num) (by omega), padicValNat_primes (p := p) (q := 2) (by omega)]
  omega

/-- `1 ≤ j < p` 时极点值 p-integral。 -/
lemma GV_poleValue_lt (hp5 : 5 ≤ p) {j : ℕ} (hj : 1 ≤ j) (hjp : j < p) : GV p (poleValue j) 0 := by
  unfold poleValue
  have h1 : GV p (C ((j : ℚ) ^ 6) * (X - C (H7 j))) 0 := by
    have := GV.C_mul (VG.natCast (p := p) (j ^ 6)) (GV.X.sub (GV.C (VG_H7_lt hjp)))
    simpa using this
  refine (h1.sub (GV.C (VG_sixth hp5))).add (GV.C ?_)
  have := VG_inv_2j (by omega : 3 ≤ p) hj (e := 0) (by rw [padicValNat_lt_p hj hjp])
  simpa using this

/-- `1 ≤ j < p²` 时极点值 `≥ -7`。 -/
lemma GV_poleValue_sq (hp5 : 5 ≤ p) {j : ℕ} (hj : 1 ≤ j) (hjp : j < p ^ 2) :
    GV p (poleValue j) (-7) := by
  unfold poleValue
  have h1 : GV p (C ((j : ℚ) ^ 6) * (X - C (H7 j))) (-7) := by
    have := GV.C_mul (VG.natCast (p := p) (j ^ 6)) ((GV.X.mono (by norm_num)).sub (GV.C (VG_H7 hjp)))
    simpa using this
  refine (h1.sub ((GV.C (VG_sixth hp5)).mono (by norm_num))).add (GV.C ?_)
  exact (VG_inv_2j (by omega : 3 ≤ p) hj (e := 1) (padicValNat_lt_sq hj hjp)).mono (by norm_num)

/-- `j = pk`、`1 ≤ k < p` 时极点值 `≥ -1`（`v_p(j⁶) = 6` 与 H⁽⁷⁾ 界 −7 恰合成 −1）。 -/
lemma GV_poleValue_mul (hp5 : 5 ≤ p) {k : ℕ} (hk : 1 ≤ k) (hkp : k < p) :
    GV p (poleValue (p * k)) (-1) := by
  have hj : 1 ≤ p * k := Nat.one_le_iff_ne_zero.mpr (by positivity)
  have hjp : p * k < p ^ 2 := by rw [sq]; exact Nat.mul_lt_mul_of_pos_left hkp (by omega)
  unfold poleValue
  have h4 : VG p (((p * k : ℕ) : ℚ) ^ 6) 6 := by
    right
    rw [padicValRat.pow, padicValRat.of_nat, padicValNat.mul (by omega) (by omega),
      padicValNat_self, padicValNat_lt_p hk hkp]; norm_num
  have h1 : GV p (C (((p * k : ℕ) : ℚ) ^ 6) * (X - C (H7 (p * k)))) (-1) := by
    have := GV.C_mul h4 ((GV.X.mono (by norm_num)).sub (GV.C (VG_H7 hjp)))
    refine this.mono (by norm_num)
  refine (h1.sub ((GV.C (VG_sixth hp5)).mono (by norm_num))).add (GV.C ?_)
  exact VG_inv_2j (by omega : 3 ≤ p) hj (e := 1) (padicValNat_lt_sq hj hjp)

lemma VG_int_dvd_one {z : ℤ} (h : (p : ℤ) ∣ z) : VG p (z : ℚ) 1 := VG_int_one h

/-- `1/(p-u)⁷ + 1/u⁷ ≡ 0 (mod p)`。 -/
lemma VG_pair (hp3 : 3 ≤ p) {u : ℕ} (hu : 1 ≤ u) (hup : u < p) :
    VG p (1 / ((p : ℚ) - u) ^ 7 + 1 / (u : ℚ) ^ 7) 1 := by
  have hpu : ((p : ℚ) - u) = ((p - u : ℕ) : ℚ) := by push_cast [Nat.cast_sub hup.le]; ring
  have hne1 : ((p - u : ℕ) : ℚ) ≠ 0 := by exact_mod_cast (by omega : p - u ≠ 0)
  have hne2 : (u : ℚ) ≠ 0 := by exact_mod_cast (by omega : u ≠ 0)
  rw [hpu, div_add_div _ _ (pow_ne_zero _ hne1) (pow_ne_zero _ hne2), div_eq_mul_inv]
  have hnum : VG p (1 * (u : ℚ) ^ 7 + ((p - u : ℕ) : ℚ) ^ 7 * 1) 1 := by
    have := VG_int_one (p := p) (z := (u : ℤ) ^ 7 + ((p : ℤ) - u) ^ 7) (by
      rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]; push_cast
      rw [ZMod.natCast_self]; ring)
    convert this using 1
    push_cast [Nat.cast_sub hup.le]; ring
  have hden : VG p (((p - u : ℕ) : ℚ) ^ 7 * (u : ℚ) ^ 7)⁻¹ 0 := by
    rw [show ((p - u : ℕ) : ℚ) ^ 7 * (u : ℚ) ^ 7 = (((p - u) ^ 7 * u ^ 7 : ℕ) : ℚ) by push_cast; ring]
    have hA : (p - u) ^ 7 ≠ 0 := pow_ne_zero _ (by omega)
    have hB : u ^ 7 ≠ 0 := pow_ne_zero _ (by omega)
    refine (VG_inv_nat_le (e := 0) (mul_ne_zero hA hB) ?_).mono (by norm_num)
    rw [padicValNat.mul hA hB, padicValNat.pow (p := p) _ 7,
      padicValNat.pow (p := p) _ 7, padicValNat_lt_p (by omega) (by omega),
      padicValNat_lt_p hu hup]
  simpa using hnum.mul hden

/-- `H⁽⁷⁾_{p-1} ≡ 0 (mod p)`。 -/
lemma VG_H7_pm1 (hp3 : 3 ≤ p) : VG p (H7 (p - 1)) 1 := by
  have h2 : 2 * H7 (p - 1) = ∑ u ∈ Icc 1 (p - 1), (1 / ((p : ℚ) - u) ^ 7 + 1 / (u : ℚ) ^ 7) := by
    unfold H7
    rw [Finset.sum_add_distrib, two_mul]
    congr 1
    apply Finset.sum_nbij' (fun u => p - u) (fun u => p - u)
    · intro u hu; simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hu ⊢
      omega
    · intro u hu; simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hu ⊢
      omega
    · intro u hu; simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hu
      omega
    · intro u hu; simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hu
      omega
    · intro u hu
      simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hu
      push_cast [Nat.cast_sub (show u ≤ p by omega)]; ring_nf
  have hsum : VG p (2 * H7 (p - 1)) 1 := by
    rw [h2]; exact VG.sum _ fun u hu =>
      VG_pair hp3 (Finset.mem_Icc.mp hu).1 (by have := (Finset.mem_Icc.mp hu).2; omega)
  have hhalf : VG p ((1 / 2 : ℚ)) 0 := by
    rw [one_div, show (2 : ℚ) = ((2 : ℕ) : ℚ) by norm_num]
    have := Fact.mk Nat.prime_two
    refine (VG_inv_nat_le (e := 0) (by norm_num) ?_).mono (by norm_num)
    rw [padicValNat_primes (p := p) (q := 2) (by omega)]
  have this := hhalf.mul hsum
  rw [show 1 / 2 * (2 * H7 (p - 1)) = H7 (p - 1) by ring] at this
  simpa using this

lemma H7_succ' {j : ℕ} (hj : 1 ≤ j) : H7 j = H7 (j - 1) + 1 / (j : ℚ) ^ 7 := by
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
  unfold H7
  rw [Finset.sum_Icc_succ_top (by omega), Nat.add_sub_cancel]

lemma H7_split {c : ℕ} (hc : 1 ≤ c) (hcp : c < p) :
    H7 (p - 1) = H7 (p - c) + ∑ u ∈ Icc 1 (c - 1), 1 / ((p : ℚ) - u) ^ 7 := by
  unfold H7
  rw [show Icc 1 (p - 1) = Ioc 0 (p - 1) from Finset.Icc_add_one_left_eq_Ioc 0 _,
    show Icc 1 (p - c) = Ioc 0 (p - c) from Finset.Icc_add_one_left_eq_Ioc 0 _]
  have h := Finset.sum_Ioc_consecutive (fun k : ℕ => 1 / (k : ℚ) ^ 7) (Nat.zero_le (p - c))
    (show p - c ≤ p - 1 by omega)
  rw [← h]
  congr 1
  apply Finset.sum_nbij' (fun k => p - k) (fun u => p - u)
  · intro k hk; simp only [Finset.mem_Ioc, Finset.mem_Icc, Finset.coe_Ioc, Finset.coe_Icc,
      Set.mem_Ioc, Set.mem_Icc, Finset.mem_coe] at hk ⊢; omega
  · intro u hu; simp only [Finset.mem_Ioc, Finset.mem_Icc, Finset.coe_Ioc, Finset.coe_Icc,
      Set.mem_Ioc, Set.mem_Icc, Finset.mem_coe] at hu ⊢; omega
  · intro k hk; simp only [Finset.mem_Ioc, Finset.coe_Ioc, Set.mem_Ioc, Finset.mem_coe] at hk; omega
  · intro u hu; simp only [Finset.mem_Icc, Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe] at hu; omega
  · intro k hk
    simp only [Finset.mem_Ioc, Finset.coe_Ioc, Set.mem_Ioc, Finset.mem_coe] at hk
    push_cast [Nat.cast_sub (show k ≤ p by omega)]
    ring_nf

/-- **同余**：`poleValue (p - c) ≡ poleValue c (mod p)`（`1 ≤ c < p`；
b=8 常数项 −1/6 相消，无需 `VG_sixth`，保持 `3 ≤ p`）。 -/
theorem GV_poleValue_congr (hp3 : 3 ≤ p) {c : ℕ} (hc : 1 ≤ c) (hcp : c < p) :
    GV p (poleValue (p - c) - poleValue c) 1 := by
  set d := p - c with hd
  have hdq : (d : ℚ) = p - c := by rw [hd]; push_cast [Nat.cast_sub hcp.le]; ring
  have hc0 : (c : ℚ) ≠ 0 := by exact_mod_cast (by omega : c ≠ 0)
  have hd0 : (d : ℚ) ≠ 0 := by exact_mod_cast (by omega : d ≠ 0)
  set S' := ∑ u ∈ Icc 1 (c - 1), 1 / ((p : ℚ) - u) ^ 7 with hS'
  set Sc := ∑ u ∈ Icc 1 (c - 1), 1 / (u : ℚ) ^ 7 with hSc
  have hHd : H7 d = H7 (p - 1) - S' := by rw [H7_split hc hcp]; ring
  have hHc : H7 c = Sc + 1 / (c : ℚ) ^ 7 := by rw [H7_succ' hc]; rfl
  set κ : ℚ := -(d : ℚ) ^ 6 * H7 d + (c : ℚ) ^ 6 * H7 c + (1 / (2 * (d : ℚ)) - 1 / (2 * (c : ℚ)))
    with hκ
  have hκ' : κ = -(d : ℚ) ^ 6 * H7 (p - 1) + ((d : ℚ) ^ 6 - (c : ℚ) ^ 6) * S' +
      (c : ℚ) ^ 6 * ∑ u ∈ Icc 1 (c - 1), (1 / ((p : ℚ) - u) ^ 7 + 1 / (u : ℚ) ^ 7) +
      (1 / (2 * (c : ℚ)) + 1 / (2 * (d : ℚ))) := by
    rw [hκ, hHd, hHc, Finset.sum_add_distrib, ← hS', ← hSc]
    field_simp
    ring
  have hdiff : poleValue d - poleValue c = C ((d : ℚ) ^ 6 - (c : ℚ) ^ 6) * X + C κ := by
    unfold poleValue
    rw [hκ]
    ext n
    simp only [coeff_add, coeff_sub, coeff_C_mul, coeff_C, coeff_X, coeff_neg, mul_sub]
    split_ifs <;> ring
  rw [hdiff]
  have hd4 : VG p ((d : ℚ) ^ 6 - (c : ℚ) ^ 6) 1 := by
    have := VG_int_one (p := p) (z := (d : ℤ) ^ 6 - (c : ℤ) ^ 6) (by
      rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]; push_cast
      rw [hd, Nat.cast_sub hcp.le, ZMod.natCast_self]; ring)
    simpa using this
  refine (by simpa using GV.C_mul hd4 (GV.X (p := p)) : GV p _ 1).add (GV.C ?_)
  rw [hκ']
  have t1 : VG p (-(d : ℚ) ^ 6 * H7 (p - 1)) 1 := by
    have := ((VG.natCast (p := p) (d ^ 6)).mul (VG_H7_pm1 hp3)).neg
    rw [show -(d : ℚ) ^ 6 * H7 (p - 1) = -(((d ^ 6 : ℕ) : ℚ) * H7 (p - 1)) by push_cast; ring]
    simpa using this
  refine ((t1.add ?_).add ?_).add ?_
  · refine (hd4.mul (VG.sum (r := 0) _ fun u hu => ?_)).mono (by norm_num)
    have hu' := Finset.mem_Icc.mp hu
    have hu2 : u < p := by omega
    rw [show ((p : ℚ) - u) = ((p - u : ℕ) : ℚ) by push_cast [Nat.cast_sub (show u ≤ p by omega)]; ring,
      one_div, show (((p - u : ℕ) : ℚ) ^ 7) = (((p - u) ^ 7 : ℕ) : ℚ) by push_cast; ring]
    refine (VG_inv_nat_le (e := 0) (pow_ne_zero _ (Nat.sub_ne_zero_of_lt hu2)) ?_).mono (by norm_num)
    rw [padicValNat.pow (p := p) _ 7, padicValNat_lt_p (Nat.one_le_iff_ne_zero.mpr
      (Nat.sub_ne_zero_of_lt hu2)) (Nat.sub_lt (by omega) (by omega))]
  · have := (VG.natCast (p := p) (c ^ 6)).mul (VG.sum (r := 1) _ fun u hu =>
      VG_pair hp3 (Finset.mem_Icc.mp hu).1
        (lt_of_le_of_lt (Finset.mem_Icc.mp hu).2 (lt_of_le_of_lt (Nat.sub_le c 1) hcp)))
    simpa using this
  · have e : 1 / (2 * (c : ℚ)) + 1 / (2 * (d : ℚ)) = (p : ℚ) * (1 / (2 * (c * d : ℕ) : ℚ)) := by
      push_cast; rw [hdq]
      have : ((p : ℚ) - c) ≠ 0 := by rw [← hdq]; exact hd0
      field_simp; ring
    rw [e]
    have hp1 : VG p (p : ℚ) 1 := by simpa using VG.primePow (p := p) 1
    have hd1 : 1 ≤ d := by omega
    have hdp : d < p := by omega
    have hc0' : c ≠ 0 := by omega
    have hd0' : d ≠ 0 := by omega
    refine (hp1.mul (VG_inv_2j (by omega : 3 ≤ p) (Nat.one_le_iff_ne_zero.mpr
      (Nat.mul_ne_zero hc0' hd0'))
      (e := 0) (by
        rw [padicValNat.mul hc0' hd0', padicValNat_lt_p hc hcp, padicValNat_lt_p hd1 hdp]))).mono
      (by norm_num)

end Zeta7
