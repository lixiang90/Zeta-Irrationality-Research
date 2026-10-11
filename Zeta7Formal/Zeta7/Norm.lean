import Mathlib
import Zeta7.Arith.DirectBound
import Zeta7.Arith.SmallPrimeF
import Zeta7.Arith.InnerAlloc
import Zeta7.Arith.OuterEntryMain
import Zeta7.Construction
import Zeta7.Legendre

/-!
# 实归一化层骨架（镜像 `Apery/Norm.lean`，b=8）

mo271 的 `Norm.lean` 定义真正用于证明的归一化 `mN`：每个素数 `p ≤ 2h` 的局部
指数取 `Arith` 中**已证**的 `v_p^G(F_K)` 下界（小素数 (3.12) / 内区 water-filling /
外区界），并证 `integral_mN`：`mN n · F n` 是整系数多项式（Proposition 5.1）。

**b=8 状态（2026-09-25，进展 23）**：
* 已落地部件：`GV_F_of_Δ`（Δ→F 赋值平移）、`vSK_big`（大素数 v_p(S_K)=0，
  走本库 `Legendre.vS_eq`）、`rat_int_of_VG`（处处 p-integral 的有理数是整数）；
* **小素数 (3.12)**：`GV_F_Lsmall` 已证（`−8h⌊log_p 200n⌋ − h·v_p(720)`，
  全链 `Arith/{SmallPrime,…,SmallPrimeF}` + `GV.det_GV`）；
* **内区 water-filling（进展 22）**：`betaI/kloI/ktopI/L0I/allocI/InnerOK/WI`
  实例化 + `Sep_PlK` + `GV_F_inner`；
* **外区（进展 23）**：`OuterOK/WO`（秩项 `22n`→`16n`）+ `GV_F_outer`
  （`Arith/OuterEntry*` 五文件机器）+ `OuterOK_big`/`WO_big` + **`GV_F_big`
  已灭**；`Lp` 四分支（小素数/内区/外区/回退）+ `GV_F_Lp` 全分支已证；
  `mN`/`mN_pos`/`padicValRat_mN`/`integral_mN`（Proposition 5.1-类比）已证；
* γ 常数（kloI/ktopI/L0I 的 magic number）按 `b8_verdict.md` 需研究侧
  再工程，当前沿用 mo271 数值——Lean 陈述对取值不敏感（InnerOK 门控）。
-/

open Finset Polynomial

namespace Zeta7

/-- 分离小素数区与内区区的截断 `M`。 -/
def Mcut : ℕ := 400

/-- `v_p(S_K)`。 -/
noncomputable def vSK (n p : ℕ) : ℤ := padicValRat p (S n)

/-- 小素数指数 (3.12)-类比（路线 B 活常数，§C7/D 钉死）：
`−(8·h·⌊log_p 200n⌋ + h·v_p(720))`（b=6 为 6 与 24）。
注：组装系数 8 = 7+1——每行调和 `H⁽⁷⁾` 损失 7 份 log（`SmallPrime.VG_H7_log`）+
残差因子 1 份 log（`SmallPrimeTau.VG_res_factor`），与 §E "8 = 7+1" 的调和/极点
拆分一致；`tau8_bound` 的多项式部分（6 份 log）单调汇入。常数项只有 v_p(720)
（von Staudt −1 已被 Lb 项吸收，见 `b8_arithmetic.md` §C8 常数修正）。 -/
noncomputable def Lsmall (n p : ℕ) : ℤ :=
  -(8 * (37 * n : ℕ) * (Nat.log p (200 * n) : ℤ) + (37 * n : ℕ) * (padicValNat p 720 : ℤ))

/-! ### Δ → F 的赋值平移与本原部件 -/

variable {p : ℕ} [hp : Fact p.Prime]

lemma GV_F_of_Δ {n : ℕ} {r : ℚ} (h : GV p (Δ n) r) : GV p (F n) ((vSK n p : ℚ) + r) := by
  unfold F
  have hS : VG p (S n) (vSK n p) := by
    unfold vSK; right; exact le_refl _
  exact GV.C_mul hS h

lemma padicValNat_factorial_lt {k : ℕ} (hk : k < p) : padicValNat p k.factorial = 0 :=
  padicValNat.eq_zero_of_not_dvd (fun h => by
    have := (Nat.Prime.dvd_factorial hp.out).mp h; omega)

/-- 大素数（`p > 2h`）时 `v_p(S_K) = 0`（b=8：16h 幂次下同样归零）。 -/
lemma vSK_big {n : ℕ} (hn : 1 ≤ n) (hbig : 2 * (37 * n) < p) : vSK n p = 0 := by
  have h := vS_eq (by omega : 0 < n) hp.out
  have e : vSK n p = (InnerData.mk n 200 p).vS := rfl
  rw [e, h, padicValNat_factorial_lt (by omega : 40 * n < p),
    padicValNat_factorial_lt (by omega : 3 * n < p)]
  have h4 : padicValNat p 4 = 0 :=
    padicValNat.eq_zero_of_not_dvd (fun hd => by have := Nat.le_of_dvd (by norm_num) hd; omega)
  rw [h4, Finset.sum_eq_zero (fun i hi => by
    rw [padicValNat_factorial_lt (by have := Finset.mem_Icc.mp hi; omega)]; rfl)]
  simp

/-- 处处 `p`-integral 的有理数是整数（镜像 `Apery.Norm.rat_int_of_VG`，b-无关）。 -/
lemma rat_int_of_VG {q : ℚ} (h : ∀ p : ℕ, ∀ _ : Fact p.Prime, VG p q 0) : ∃ z : ℤ, q = z := by
  by_contra hne
  have hden : q.den ≠ 1 := fun h1 => hne ⟨q.num, (Rat.coe_int_num_of_den_eq_one h1).symm⟩
  set p := q.den.minFac with hpdef
  have hpp : p.Prime := Nat.minFac_prime hden
  have := Fact.mk hpp
  have hdvd : p ∣ q.den := Nat.minFac_dvd _
  rcases h p ‹_› with h0 | hv
  · exact hne ⟨0, by simp [h0]⟩
  · have hnum : ¬ (p : ℤ) ∣ q.num := by
      intro hd
      have hc := q.reduced
      have this : p ∣ Nat.gcd q.num.natAbs q.den :=
        Nat.dvd_gcd (Int.natCast_dvd.mp hd) hdvd
      rw [hc] at this
      exact hpp.one_lt.ne' (Nat.dvd_one.mp this)
    have h1 : padicValInt p q.num = 0 := padicValInt.eq_zero_of_not_dvd hnum
    have h2 : 1 ≤ padicValNat p q.den := one_le_padicValNat_of_dvd q.den_ne_zero hdvd
    have e : padicValRat p q = padicValInt p q.num - padicValNat p q.den := rfl
    have hlt : padicValRat p q < 0 := by rw [e, h1]; omega
    have this : (padicValRat p q : ℚ) < 0 := by exact_mod_cast hlt
    linarith

/-! ### 目标陈述：(3.12)-类比组装版 -/

/-- **(3.12)-类比（路线 B 组装版，已证）**：
`GV p (F n) (Lsmall n p)`，即 `v_p^G(F_K) ≥ −8h⌊log_p 200n⌋ − h·v_p(720)`。
证明：镜像 mo271 `Arith/SmallPrimeF.lean` 全链（`Zeta7/Arith/SmallPrimeF.lean`）——
qP 行基 + `BasisChange` 行列式基变换 + `crude_tauX8`（每行损耗 8⌊log⌋ + v_p(720)，
8 = 7+1：调和 H⁽⁷⁾ 每行 −7⌊log⌋、残差因子 −1⌊log⌋，`SmallPrimeTau`；
多项式部分走 `DirectBound.tau8_bound` 单调汇合）+ `GV.det_GV` 合成。 -/
theorem GV_F_Lsmall {n : ℕ} (hn : 1 ≤ n) : GV p (F n) (Lsmall n p) := by
  have h := small_prime_bound (p := p) hn
  rw [show (Lsmall n p : ℚ) =
      -(8 * (37 * n : ℕ) * (Nat.log p (200 * n) : ℚ) + (37 * n : ℕ) * padicValNat p 720) by
    unfold Lsmall
    push_cast
    rw [show ((720 : ℚ) = ((720 : ℕ) : ℚ)) by norm_num, padicValRat.of_nat, Int.cast_natCast]]
  exact h

/-! ### 内区 water-filling 实例化（进展 22，镜像 mo271 `Norm.lean` 中部）-/

/-- 内区类偏移 `β_c = 8 ℓ_N(c) − ℓ_K(c) − 6`（b=8；b=6 为 `6·… − … − 4`）。
与 `InnerAlloc` 的 `hβ : Bse c = (β c : ℚ) + 6`（c ≠ 0）配对：
`Bse = 8 S_N − S_K`（非零类）恰好 = `β + 6`。 -/
noncomputable def betaI (n p : ℕ) {m : ℕ} (c : Fin (m + 1)) : ℤ :=
  8 * (SX p (3 * n) (((c : ℕ) : ℤ) : ZMod p) : ℤ) -
    (SX p (40 * n) (((c : ℕ) : ℤ) : ZMod p) : ℤ) - 6

/-- water-filling 参数（`b8_verdict.md` 再工程待研究侧）。b=8 必改常数：
`kloI = −2q − 8`（b=6 的 `−2q − 6` 在 b=8 **失效**——min β = 16q'−2q−6+8·0−2
= −2q−8 可在 q'=0、a'=0、a=2 时取到，如 n=33、p=233、c=100；此为水填充可行性
`rowsK β klo = 0` 的硬约束，非 magic number）；`ktopI/L0I` 沿用 mo271 数值
（`InnerOK` 门控其可行性）。 -/
def kloI (n p : ℕ) : ℤ := -2 * ((40 * n / p : ℕ) : ℤ) - 8
def ktopI (n p : ℕ) : ℤ := 8 * ((40 * n / p : ℕ) : ℤ) + 20
def L0I (n p : ℕ) : ℕ := 3 * (40 * n / p) + 6

/-- 内区分配。 -/
noncomputable def allocI (n p m : ℕ) : Fin (m + 1) → ℕ :=
  allocK (betaI n p (m := m)) (37 * n)
    (kfSel (betaI n p (m := m)) (37 * n) (L0I n p) (kloI n p) (ktopI n p))

/-- 内区界的边条件（b=8：`7 ≤ p`、hdeg 的 `7 + 2(24n + 74n)`、hZ 的 `(b 0 − 6)/2`）。 -/
def InnerOK (n p : ℕ) : Prop :=
  ∃ hm : 2 * (p / 2) + 1 = p, ∃ hm1 : 1 ≤ p / 2, 7 ≤ p ∧ Sep p (PlK (40 * n)) ∧
    40 * n < p ^ 2 ∧
    7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2 ∧
    ∑ c, allocI n p (p / 2) c = 37 * n ∧
    tmin hm1 (allocI n p (p / 2)) (Bse p (40 * n) (3 * n)) ≤
      2 * (allocI n p (p / 2) 0 : ℚ) + (Bse p (40 * n) (3 * n) 0 - 6) / 2

/-- 内区权重和（`m = p / 2`）。 -/
noncomputable def WI (n p : ℕ) : ℚ :=
  if hm1 : 1 ≤ p / 2 then ∑ s, wcap hm1 (allocI n p (p / 2)) (Bse p (40 * n) (3 * n)) s else 0

/-- 外区界的边条件。 -/
def OuterOK (n p : ℕ) : Prop :=
  2 * (p / 2) + 1 = p ∧ 7 ≤ p ∧ 40 * n < 3 * p ∧ 2 * (40 * n) < p ^ 2 ∧ 3 * n < p

/-- 外区权重和减秩损失（`m = p / 2`；秩项 `22n` → `16n`，与 `outer_frame` 一致）。 -/
noncomputable def WO (n p : ℕ) : ℚ :=
  if hpp : p.Prime then
    if hm : 2 * (p / 2) + 1 = p then
      haveI : Fact p.Prime := ⟨hpp⟩
      2 * ∑ c, ∑ i ∈ range (LoC hm n c), wO hm n c i -
        ((37 * n - ((2 * p + 16 * n - 3) - (37 * n - 1)) : ℕ) : ℚ)
    else 0
  else 0

/-- `2K < p²` 时极点集 `PlK K` 模 p 分离（b-无关，镜像 mo271 `Sep_PlK`）。 -/
lemma Sep_PlK {K : ℕ} (hK : 2 * K < p ^ 2) : Sep p (PlK K) := by
  intro r hr s hs hrs _ hdvd
  obtain ⟨j, hj, ε, hε, rfl⟩ := mem_PlK_iff hr
  obtain ⟨j', hj', ε', hε', rfl⟩ := mem_PlK_iff hs
  have h1 := Finset.mem_Icc.mp hj
  have h2 := Finset.mem_Icc.mp hj'
  have hlt : |ε * (j : ℤ) - ε' * j'| < (p : ℤ) ^ 2 := by
    rcases hε with rfl | rfl <;> rcases hε' with rfl | rfl <;> rw [abs_lt] <;> constructor <;>
      push_cast <;> nlinarith
  have this := Int.eq_zero_of_abs_lt_dvd hdvd hlt
  exact hrs (by linarith)

/-- **内区界**：`InnerOK` 时 `v_p^G(F_K) ≥ vSK + ⌊2·WI⌋`（镜像 mo271 `GV_F_inner`）。 -/
lemma GV_F_inner {n : ℕ} (h : InnerOK n p) : GV p (F n) (vSK n p + ⌊2 * WI n p⌋) := by
  obtain ⟨hm, hm1, hp7, hsep, hK, hdeg, hsum, hZ⟩ := h
  have hΔ := inner_bound_cap hp7 hm hm1 n (allocI n p (p / 2)) hsum hsep hK hdeg hZ
  have hW : WI n p = ∑ s, wcap hm1 (allocI n p (p / 2)) (Bse p (40 * n) (3 * n)) s := by
    unfold WI; rw [dif_pos hm1]
  rw [← hW] at hΔ
  have this := GV_F_of_Δ hΔ
  push_cast
  exact this.mono (by have := Int.floor_le (2 * WI n p); linarith)

/-- **外区界**：`OuterOK` 时 `v_p^G(F_K) ≥ vSK + ⌊WO⌋`（镜像 mo271 `GV_F_outer`；
秩项 `16n` 与 `outer_frame`/`WO` 一致）。 -/
lemma GV_F_outer {n : ℕ} (h : OuterOK n p) : GV p (F n) (vSK n p + ⌊WO n p⌋) := by
  obtain ⟨hm, hp7, hK3, hK, hpN⟩ := h
  have hΔ := outer_bound hm n hp7 hK3 hK hpN
  have hW : WO n p = 2 * ∑ c, ∑ i ∈ range (LoC hm n c), wO hm n c i -
      ((37 * n - ((2 * p + 16 * n - 3) - (37 * n - 1)) : ℕ) : ℚ) := by
    unfold WO; rw [dif_pos hp.out, dif_pos hm]
  rw [← hW] at hΔ
  have this := GV_F_of_Δ hΔ
  push_cast
  exact this.mono (by have := Int.floor_le (WO n p); linarith)

open Classical in
/-- **局部指数 `Lp`（b=8）**：小素数 `Lsmall` / 内区 `vSK + ⌊2·WI⌋`
（`InnerOK` 门控，否则回退）/ 外区 `vSK + ⌊WO⌋`（`OuterOK` 门控，否则回退）。 -/
noncomputable def Lp (n p : ℕ) : ℤ :=
  if p * Mcut ≤ 40 * n then Lsmall n p
  else if 3 * p ≤ 40 * n then
    (if InnerOK n p then vSK n p + ⌊2 * WI n p⌋ else Lsmall n p)
  else (if OuterOK n p then vSK n p + ⌊WO n p⌋ else Lsmall n p)

/-- **每个局部指数都有效**。 -/
theorem GV_F_Lp {n : ℕ} (hn : 1 ≤ n) : GV p (F n) (Lp n p) := by
  unfold Lp
  split_ifs with h1 h2 h3 h4
  · exact GV_F_Lsmall hn
  · exact_mod_cast GV_F_inner h3
  · exact GV_F_Lsmall hn
  · exact_mod_cast GV_F_outer h4
  · exact GV_F_Lsmall hn

/-! ### 整性（Proposition 5.1-类比）-/

/-- **归一化子** `m_K = ∏_{p ≤ 2h} p^{−L_p}`。 -/
noncomputable def mN (n : ℕ) : ℚ :=
  ∏ p ∈ (range (2 * (37 * n) + 1)).filter Nat.Prime, (p : ℚ) ^ (-Lp n p)

lemma mN_pos (n : ℕ) : 0 < mN n := by
  unfold mN
  apply Finset.prod_pos
  intro p hp
  have this : 0 < p := (Finset.mem_filter.mp hp).2.pos
  exact zpow_pos (by exact_mod_cast this) _

omit hp in
lemma padicValRat_mN (n : ℕ) (p : ℕ) [Fact p.Prime] :
    padicValRat p (mN n) = if p ≤ 2 * (37 * n) then -Lp n p else 0 := by
  unfold mN
  rw [padicValRat_finset_prod _ _ (fun q hq => by
    have this := (Finset.mem_filter.mp hq).2.pos
    exact zpow_ne_zero _ (by exact_mod_cast this.ne'))]
  simp only [padicValRat.zpow, padicValRat.of_nat]
  have hval : ∀ q ∈ (range (2 * (37 * n) + 1)).filter Nat.Prime,
      (padicValNat p q : ℤ) = if q = p then 1 else 0 := by
    intro q hq
    have hq' : q.Prime := (Finset.mem_filter.mp hq).2
    have this := Fact.mk hq'
    split_ifs with h
    · subst h; simp [padicValNat.self (Fact.out : q.Prime).one_lt]
    · rw [padicValNat_primes (Ne.symm h)]; rfl
  rw [Finset.sum_congr rfl (fun q hq => by rw [hval q hq])]
  simp only [mul_ite, mul_one, mul_zero]
  rw [Finset.sum_ite_eq']
  by_cases h : p ≤ 2 * (37 * n)
  · rw [if_pos (Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), Fact.out⟩), if_pos h]
  · rw [if_neg (fun hm => h (by have this := Finset.mem_range.mp (Finset.mem_filter.mp hm).1; omega)),
      if_neg h]

/-- 大素数（`p > 2h`）时外区边条件自动成立（镜像 mo271 `OuterOK_big`）。 -/
lemma OuterOK_big {n : ℕ} (hn : 1 ≤ n) (hbig : 2 * (37 * n) < p) : OuterOK n p := by
  have hodd : 2 * (p / 2) + 1 = p := by
    have this := hp.out.eq_one_or_self_of_dvd 2
    rcases Nat.even_or_odd p with ⟨k, hk⟩ | ⟨k, hk⟩
    · have := this ⟨k, by omega⟩; omega
    · omega
  refine ⟨hodd, by omega, by omega, by nlinarith, by omega⟩

/-- 大素数时外区权重和非负（镜像 mo271 `WO_big`；秩项 `22n` → `16n`）。 -/
lemma WO_big {n : ℕ} (hbig : 2 * (37 * n) < p) : 0 ≤ WO n p := by
  unfold WO
  rw [dif_pos hp.out]
  split_ifs with hm
  · have hsum : ∑ c, ∑ i ∈ range (LoC hm n c), wO hm n c i = 0 := by
      refine Finset.sum_eq_zero fun c _ => Finset.sum_eq_zero fun i hi => ?_
      by_cases hc : c = 0
      · exfalso
        subst hc
        have hL : LoC hm n 0 = 0 := by
          unfold LoC tailC
          rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
          intro j hj hj0
          have hj' := Finset.mem_Icc.mp hj
          have hd : p ∣ j := by exact_mod_cast (jc_eq_zero_iff hm j).mp hj0
          have this := Nat.le_of_dvd (by omega) hd
          omega
        rw [hL] at hi; simp at hi
      · have hnb : nbC hm n c = 0 := by
          unfold nbC bigC
          rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
          intro j hj
          have this := Finset.mem_Icc.mp (Finset.mem_filter.mp hj).1
          omega
        unfold wO
        rw [if_neg hc, hnb, if_neg (by omega)]
    rw [hsum, show 37 * n - ((2 * p + 16 * n - 3) - (37 * n - 1)) = 0 by omega]
    simp
  · exact le_refl _

/-- **大素数界（已灭，进展 23）**：`p > 2h` 时 `v_p^G(F_K) ≥ 0`。
证法 = `GV_F_outer (OuterOK_big …)` + `vSK_big` + `WO_big`（镜像 mo271 `GV_F_big`）。 -/
theorem GV_F_big {n : ℕ} (hn : 1 ≤ n) (hbig : 2 * (37 * n) < p) : GV p (F n) 0 := by
  have h := GV_F_outer (OuterOK_big hn hbig)
  rw [vSK_big hn hbig] at h
  refine h.mono ?_
  have this := WO_big (n := n) hbig
  have h0 : (0 : ℤ) ≤ ⌊WO n p⌋ := Int.floor_nonneg.mpr this
  have h0' : (0 : ℚ) ≤ (⌊WO n p⌋ : ℚ) := by exact_mod_cast h0
  push_cast
  linarith

/-- **整性（Proposition 5.1-类比，已证）**：`mN n · F n` 是整系数多项式。
证法 = `rat_int_of_VG` + `padicValRat_mN` + `GV_F_Lp`/`GV_F_big` 分支合成
（镜像 mo271 `integral_mN`；大素数分支走 `GV_F_big` 目标）。 -/
theorem integral_mN {n : ℕ} (hn : 1 ≤ n) :
    ∃ Q : ℤ[X], Q.map (Int.castRingHom ℚ) = C (mN n) * F n := by
  have hall : ∀ p : ℕ, ∀ _ : Fact p.Prime, GV p (C (mN n) * F n) 0 := by
    intro p _
    have hm : VG p (mN n) (if p ≤ 2 * (37 * n) then -Lp n p else 0 : ℤ) := by
      right; rw [padicValRat_mN]
    by_cases hbig : p ≤ 2 * (37 * n)
    · rw [if_pos hbig] at hm
      have this := GV.C_mul hm (GV_F_Lp (p := p) hn)
      refine this.mono ?_
      push_cast; linarith
    · rw [if_neg hbig] at hm
      have this := GV.C_mul hm (GV_F_big (p := p) hn (by omega))
      simpa using this
  have hcoef : ∀ k, ∃ z : ℤ, (C (mN n) * F n).coeff k = z := fun k =>
    rat_int_of_VG fun p hp => hall p hp k
  have hlift : C (mN n) * F n ∈ lifts (Int.castRingHom ℚ) := by
    rw [lifts_iff_coeff_lifts]
    intro k
    obtain ⟨z, hz⟩ := hcoef k
    exact ⟨z, by simp [hz]⟩
  obtain ⟨Q, hQ⟩ := hlift
  exact ⟨Q, hQ⟩

end Zeta7
