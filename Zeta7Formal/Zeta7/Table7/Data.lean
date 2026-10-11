import Mathlib
import Zeta7.PotentialIneq8
import Apery.Certificates

namespace Zeta7

lemma aρ8_1 : aρ8 1 = (23805751 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_1 : bρ8 1 = (3616749009 / 500000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_1 : cρ8 1 = (44179822243 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_2 : aρ8 2 = (5951309 / 250000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_2 : bρ8 2 = (24475480029 / 1000000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_2 : cρ8 2 = (49560545471 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_3 : aρ8 3 = (6890463 / 500000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_3 : bρ8 3 = (3336729871 / 62500000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_3 : cρ8 3 = (53620799443 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_4 : aρ8 4 = (2241937 / 500000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_4 : bρ8 4 = (22636383431 / 250000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_4 : cρ8 4 = (41057694881 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_5 : aρ8 5 = (35869 / 8000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_5 : bρ8 5 = (26214920033 / 200000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_5 : cρ8 5 = (77454394089 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_6 : aρ8 6 = (3851833 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_6 : bρ8 6 = (36761674253 / 200000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_6 : cρ8 6 = (44806248303 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_7 : aρ8 7 = (1564143 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_7 : bρ8 7 = (121390279341 / 500000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_7 : cρ8 7 = (4881232121 / 62500000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_8 : aρ8 8 = (340081 / 250000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_8 : bρ8 8 = (12240442627 / 40000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_8 : cρ8 8 = (36098924701 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_9 : aρ8 9 = (745743 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_9 : bρ8 9 = (91372577981 / 250000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_9 : cρ8 9 = (28325387873 / 500000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_10 : aρ8 10 = (95997 / 250000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_10 : bρ8 10 = (426183534933 / 1000000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_10 : cρ8 10 = (58654077061 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_11 : aρ8 11 = (247221 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_11 : bρ8 11 = (240824423411 / 500000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_11 : cρ8 11 = (38926352971 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_12 : aρ8 12 = (31919 / 200000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_12 : bρ8 12 = (32726529711 / 62500000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_12 : cρ8 12 = (36581913253 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_13 : aρ8 13 = (111989 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_13 : bρ8 13 = (591522748269 / 1000000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_13 : cρ8 13 = (62952958579 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_14 : aρ8 14 = (549 / 10000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_14 : bρ8 14 = (149501935981 / 200000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_14 : cρ8 14 = (16656949 / 125000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_15 : aρ8 15 = (50233 / 1000000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_15 : bρ8 15 = (389379507871 / 500000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_15 : cρ8 15 = (16227595547 / 1000000000000 : ℝ) := by norm_num [cρ8, table7]
lemma aρ8_16 : aρ8 16 = (9163 / 250000000000 : ℝ) := by norm_num [aρ8, table7]
lemma bρ8_16 : bρ8 16 = (694669460621 / 500000000000 : ℝ) := by norm_num [bρ8, table7]
lemma cρ8_16 : cρ8 16 = (5335446571 / 500000000000 : ℝ) := by norm_num [cρ8, table7]

/-- Certified upper bound for `log y`（镜像 Apery.log_le_of_pow_two_upper，b 无关抄录）。 -/
lemma log_le_of_pow_two_upper {y : ℝ} (hy : 0 < y) (k m : ℕ) (hk : 1 ≤ 2 ^ k * y) :
    Real.log y ≤ 2 * ∑ j ∈ Finset.range m, (1 / (2 * (j : ℝ) + 1)) *
        ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ (2 * j + 1) +
      2 * ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ (2 * m + 1) /
        ((2 * m + 1) * (1 - ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ 2)) - k * 0.6931471803 := by
  have h1 := Apery.log_le_artanh hk m
  have h2 : Real.log (2 ^ k * y) = k * Real.log 2 + Real.log y := by
    rw [Real.log_mul (by positivity) hy.ne', Real.log_pow]
  have h3 := Real.log_two_gt_d9
  have hk0 : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  nlinarith [mul_le_mul_of_nonneg_left h3.le hk0]

lemma arctan_eq_pi_div_two_sub {x : ℝ} (hx : 0 < x) :
    Real.arctan x = Real.pi / 2 - Real.arctan (1 / x) := by
  rw [one_div, Real.arctan_inv_of_pos hx]; ring

lemma arctan_ge_half {x w : ℝ} (hx : 0 ≤ x) (hw : Real.sqrt (1 + x ^ 2) ≤ w) :
    2 * Real.arctan (x / (1 + w)) ≤ Real.arctan x := by
  rw [Apery.arctan_eq_two_mul_arctan hx]
  have hs : 0 ≤ Real.sqrt (1 + x ^ 2) := Real.sqrt_nonneg _
  refine mul_le_mul_of_nonneg_left (Real.arctan_strictMono.monotone ?_) (by norm_num)
  exact div_le_div_of_nonneg_left hx (by linarith) (by linarith)

lemma arctan_le_half {x w : ℝ} (hx : 0 ≤ x) (hw0 : 0 ≤ w) (hw : w ≤ Real.sqrt (1 + x ^ 2)) :
    Real.arctan x ≤ 2 * Real.arctan (x / (1 + w)) := by
  rw [Apery.arctan_eq_two_mul_arctan hx]
  refine mul_le_mul_of_nonneg_left (Real.arctan_strictMono.monotone ?_) (by norm_num)
  exact div_le_div_of_nonneg_left hx (by linarith) (by linarith)

/-- V₈ 下界模板（括号非负）。 -/
lemma Vfield8_ge_of_bounds_pos {p slo shi l1 l2 A1 A2 : ℝ} (hp : 0 < p) (hslo : 0 < slo)
    (hs1 : slo ≤ Real.sqrt p) (hs2 : Real.sqrt p ≤ shi) (hl1 : l1 ≤ Real.log (1 + p))
    (hl2 : Real.log (p + (1 / 40) ^ 2) ≤ l2) (hA1 : A1 ≤ Real.arctan (1 / shi))
    (hA2 : Real.arctan ((1 / 40) / slo) ≤ A2)
    (hP : 0 ≤ 3.14159265358979323846 + A1 - 8 * A2) :
    l1 - 8 * (1 / 40) * l2 - 2 + 16 * (1 / 40) + 2 * slo * (3.14159265358979323846 + A1 - 8 * A2) ≤ Vfield8 p := by
  rw [Vfield8_eq hp]
  have hsp : 0 < Real.sqrt p := Real.sqrt_pos.mpr hp
  have hshi : 0 < shi := hsp.trans_le hs2
  have hm1 : Real.arctan (1 / shi) ≤ Real.arctan (1 / Real.sqrt p) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsp hs2)
  have hm2 : Real.arctan ((1 / 40) / Real.sqrt p) ≤ Real.arctan ((1 / 40) / slo) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hslo hs1)
  have hpi := Real.pi_gt_d20
  have hPle : 3.14159265358979323846 + A1 - 8 * A2 ≤
      Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p) := by linarith
  have hprod : 2 * slo * (3.14159265358979323846 + A1 - 8 * A2) ≤
      2 * Real.sqrt p * (Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p)) :=
    mul_le_mul (by linarith) hPle hP (by positivity)
  have hl2' : 8 * (1 / 40) * Real.log (p + (1 / 40) ^ 2) ≤ 8 * (1 / 40) * l2 :=
    mul_le_mul_of_nonneg_left hl2 (by norm_num)
  linarith

/-- V₈ 下界模板（括号非正）。 -/
lemma Vfield8_ge_of_bounds_neg {p slo shi l1 l2 A1 A2 : ℝ} (hp : 0 < p) (hslo : 0 < slo)
    (hs1 : slo ≤ Real.sqrt p) (hs2 : Real.sqrt p ≤ shi) (hl1 : l1 ≤ Real.log (1 + p))
    (hl2 : Real.log (p + (1 / 40) ^ 2) ≤ l2) (hA1 : A1 ≤ Real.arctan (1 / shi))
    (hA2 : Real.arctan ((1 / 40) / slo) ≤ A2)
    (hP : 3.14159265358979323846 + A1 - 8 * A2 ≤ 0) :
    l1 - 8 * (1 / 40) * l2 - 2 + 16 * (1 / 40) + 2 * shi * (3.14159265358979323846 + A1 - 8 * A2) ≤ Vfield8 p := by
  rw [Vfield8_eq hp]
  have hsp : 0 < Real.sqrt p := Real.sqrt_pos.mpr hp
  have hshi : 0 < shi := hsp.trans_le hs2
  have hm1 : Real.arctan (1 / shi) ≤ Real.arctan (1 / Real.sqrt p) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsp hs2)
  have hm2 : Real.arctan ((1 / 40) / Real.sqrt p) ≤ Real.arctan ((1 / 40) / slo) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hslo hs1)
  have hpi := Real.pi_gt_d20
  have hPle : 3.14159265358979323846 + A1 - 8 * A2 ≤
      Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p) := by linarith
  have hprod : 2 * shi * (3.14159265358979323846 + A1 - 8 * A2) ≤
      2 * Real.sqrt p * (Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p)) := by
    calc 2 * shi * (3.14159265358979323846 + A1 - 8 * A2)
        ≤ 2 * Real.sqrt p * (3.14159265358979323846 + A1 - 8 * A2) :=
          mul_le_mul_of_nonpos_right (by linarith) hP
      _ ≤ _ := mul_le_mul_of_nonneg_left hPle (by positivity)
  have hl2' : 8 * (1 / 40) * Real.log (p + (1 / 40) ^ 2) ≤ 8 * (1 / 40) * l2 :=
    mul_le_mul_of_nonneg_left hl2 (by norm_num)
  linarith

end Zeta7
