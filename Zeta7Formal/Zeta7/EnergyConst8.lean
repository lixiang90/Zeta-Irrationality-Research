import Mathlib
import Zeta7.Constants
import Zeta7.Measure7
import Apery.EnergyConst

/-! # (6.4)-类比（b=8）：`λ M₀ - I(ρ) + C* ≤ U` 的数值认证

镜像 `Apery.EnergyConst`（b=6）。16 个原子 `(bρ8 j − aρ8 j)/4` 的 log 下界由
`Apery.log_ge_of_pow_two`（artanh 部分和 + 2 的幂值域归约）认证，证书值由
`research/gen_energy_const8.py` 以精确有理算术向下舍入生成，`norm_num` 逐项核验。
-/

open Finset

namespace Zeta7

/-- **(6.4)-类比**（b=8, (K:N:h) = 40:1:39）：`lam8 * M0_8 - Irho8 + Cstar8 ≤ U`。 -/
theorem energy_const8 : lam8 * M0_8 - Irho8 + Cstar8 ≤ (U : ℝ) := by
  have h1 : (-31593116867661 / 5000000000000 : ℝ) ≤ Real.log ((bρ8 1 - aρ8 1) / 4) := by
    have e : ((bρ8 1 - aρ8 1) / 4) = (7209692267 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 10 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h2 : (-12743377324391 / 2500000000000 : ℝ) ≤ Real.log ((bρ8 2 - aρ8 2) / 4) := by
    have e : ((bρ8 2 - aρ8 2) / 4) = (24451674793 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 8 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h3 : (-43167278353653 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 3 - aρ8 3) / 4) := by
    have e : ((bρ8 3 - aρ8 3) / 4) = (5337389701 / 400000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 7 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h4 : (-2367653940109 / 625000000000 : ℝ) ≤ Real.log ((bρ8 4 - aρ8 4) / 4) := by
    have e : ((bρ8 4 - aρ8 4) / 4) = (1810820997 / 80000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 6 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h5 : (-34183172205281 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 5 - aρ8 5) / 4) := by
    have e : ((bρ8 5 - aρ8 5) / 4) = (6553505827 / 200000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 5 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h6 : (-962555263383 / 312500000000 : ℝ) ≤ Real.log ((bρ8 6 - aρ8 6) / 4) := by
    have e : ((bρ8 6 - aρ8 6) / 4) = (22975564929 / 500000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 5 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h7 : (-14009490496473 / 5000000000000 : ℝ) ≤ Real.log ((bρ8 7 - aρ8 7) / 4) := by
    have e : ((bρ8 7 - aρ8 7) / 4) = (242778994539 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 5 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h8 : (-6426082056949 / 2500000000000 : ℝ) ≤ Real.log ((bρ8 8 - aρ8 8) / 4) := by
    have e : ((bρ8 8 - aρ8 8) / 4) = (306009705351 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 4 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h9 : (-23928119089803 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 9 - aρ8 9) / 4) := by
    have e : ((bρ8 9 - aρ8 9) / 4) = (365489566181 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 4 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h10 : (-11195902276957 / 5000000000000 : ℝ) ≤ Real.log ((bρ8 10 - aρ8 10) / 4) := by
    have e : ((bρ8 10 - aρ8 10) / 4) = (85236630189 / 800000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 4 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h11 : (-21168348393697 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 11 - aρ8 11) / 4) := by
    have e : ((bρ8 11 - aρ8 11) / 4) = (481648599601 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 4 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h12 : (-813310067301 / 400000000000 : ℝ) ≤ Real.log ((bρ8 12 - aρ8 12) / 4) := by
    have e : ((bρ8 12 - aρ8 12) / 4) = (523624315781 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 3 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h13 : (-9556748444273 / 5000000000000 : ℝ) ≤ Real.log ((bρ8 13 - aρ8 13) / 4) := by
    have e : ((bρ8 13 - aρ8 13) / 4) = (14788065907 / 100000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 3 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h14 : (-8386512296897 / 5000000000000 : ℝ) ≤ Real.log ((bρ8 14 - aρ8 14) / 4) := by
    have e : ((bρ8 14 - aρ8 14) / 4) = (149501925001 / 800000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 3 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h15 : (-16363480580947 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 15 - aρ8 15) / 4) := by
    have e : ((bρ8 15 - aρ8 15) / 4) = (778758965509 / 4000000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 3 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have h16 : (-10574663501989 / 10000000000000 : ℝ) ≤ Real.log ((bρ8 16 - aρ8 16) / 4) := by
    have e : ((bρ8 16 - aρ8 16) / 4) = (138933888459 / 400000000000 : ℝ) := by
      simp [aρ8, bρ8, table7]; norm_num
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 2 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have hα8 : (-36888794555543 / 10000000000000 : ℝ) ≤ Real.log alph8 := by
    have e : alph8 = (1 / 40 : ℝ) := by norm_num [alph8]
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 6 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have hl8 : (6678293725707 / 10000000000000 : ℝ) ≤ Real.log (2 * lam8) := by
    have e : (2 * lam8) = (39 / 20 : ℝ) := by norm_num [lam8]
    rw [e]
    refine le_trans ?_ (Apery.log_ge_of_pow_two (by norm_num) 0 10 (by norm_num))
    simp only [Finset.sum_range_succ, Finset.sum_range_zero]
    norm_num
  have hS0 : Sρ8 0 = (0 : ℝ) := by simp [Sρ8]
  have hS1 : Sρ8 1 = (44179822243 / 500000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS2 : Sρ8 2 = (46870183857 / 250000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS3 : Sρ8 3 = (147361167157 / 500000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS4 : Sρ8 4 = (94209431019 / 250000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS5 : Sρ8 5 = (90858423633 / 200000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS6 : Sρ8 6 = (543904614771 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS7 : Sρ8 7 = (622004328707 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS8 : Sρ8 8 = (694202178109 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS9 : Sρ8 9 = (150170590771 / 200000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS10 : Sρ8 10 = (202376757729 / 250000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS11 : Sρ8 11 = (848433383887 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS12 : Sρ8 12 = (44250764857 / 50000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS13 : Sρ8 13 = (947968255719 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS14 : Sρ8 14 = (948101511311 / 1000000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS15 : Sρ8 15 = (482164553429 / 500000000000 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hS16 : Sρ8 16 = (39 / 40 : ℝ) := by
    simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num
  have hI : Irho8 = ((1951856693423077551049 / 250000000000000000000000 : ℝ)) * Real.log ((bρ8 1 - aρ8 1) / 4) + ((6835399845732856034747 / 250000000000000000000000 : ℝ)) * Real.log ((bρ8 2 - aρ8 2) / 4) + ((12928057046717361876853 / 250000000000000000000000 : ℝ)) * Real.log ((bρ8 3 - aρ8 3) / 4) + ((2757270797164316410159 / 50000000000000000000000 : ℝ)) * Real.log ((bρ8 4 - aρ8 4) / 4) + ((64374658340062812913449 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 5 - aρ8 5) / 4) + ((5590681333896724275951 / 62500000000000000000000 : ℝ)) * Real.log ((bρ8 6 - aρ8 6) / 4) + ((2845536092532993528419 / 31250000000000000000000 : ℝ)) * Real.log ((bρ8 7 - aρ8 7) / 4) + ((742400618445578550969 / 7812500000000000000000 : ℝ)) * Real.log ((bρ8 8 - aρ8 8) / 4) + ((10232936777687375068143 / 125000000000000000000000 : ℝ)) * Real.log ((bρ8 9 - aρ8 9) / 4) + ((91521474789659020438031 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 10 - aρ8 10) / 4) + ((64537573791507731429713 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 11 - aρ8 11) / 4) + ((63412869277856980950831 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 12 - aρ8 12) / 4) + ((115391737679120884027361 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 13 - aρ8 13) / 4) + ((3158273740986059147 / 12500000000000000000000 : ℝ)) * Real.log ((bρ8 14 - aρ8 14) / 4) + ((31034150583345721693443 / 1000000000000000000000000 : ℝ)) * Real.log ((bρ8 15 - aρ8 15) / 4) + ((5173593416613004341959 / 250000000000000000000000 : ℝ)) * Real.log ((bρ8 16 - aρ8 16) / 4) := by
    simp only [Irho8, Finset.sum_Icc_succ_top (show 1 ≤ 16 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 15 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 14 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 13 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 12 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 11 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 10 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 9 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 8 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 7 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 6 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 5 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 4 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 3 by norm_num),
    Finset.sum_Icc_succ_top (show 1 ≤ 2 by norm_num), Finset.Icc_self, Finset.sum_singleton]
    simp only [hS0, hS1, hS2, hS3, hS4, hS5, hS6, hS7, hS8, hS9, hS10, hS11, hS12, hS13, hS14, hS15, hS16]
    norm_num
  rw [hI]
  unfold Cstar8
  norm_num [U, M0_8, lam8, alph8] at *
  linarith

end Zeta7
