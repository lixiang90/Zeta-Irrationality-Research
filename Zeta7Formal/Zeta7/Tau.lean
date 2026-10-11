import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.NumberTheory.Bernoulli
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.RingTheory.PowerSeries.WellKnown
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# τ₈ 泛函（b=8 的 x-世界机器，论文 §3 的类比层）

数学事实（`research/b8_machinery.py` 全部数值验证，`research/b8_arithmetic.md` §A–B）：
- κ(m) = (m)₅·B̃_{m−5}/720，B̃ 为经典约定（B̃₁ = +1/2）。
- 生成函数：Σ κ(m) t^m/m! = t⁶/(720(e^t−1)) + t⁶/720（B̃₁=+1/2）。
- 差分恒等式：∑_{k<e} C(e,k)κ(k) = [e≥6]·e!/(e−6)!/720。
- von Staudt 型赋值界：v_p(κ d) ≥ −1（p ≥ 7）。d ≤ p+4 时为整。

约定陷阱（`research/NOTES.md` §2）：构造 pullback 像只用偶数指标 Bernoulli
（约定无关）；本文件的显式 B̃ 仅供恒等式陈述与证明。

【2026-09-24 进展】`kappa_difference` 与 `kappa_val` 已完整证明（无 sorry）：
- 差分恒等式走 `sum_bernoulli'`（mathlib 的 Bernoulli 二项和恒等式）+
  `(k)₅·C(e,k) = (e)₅·C(e−5,k−5)` 折叠，比生成函数系数比较更短；
- 赋值界走 mathlib 的 von Staudt–Clausen 定理 `Bernoulli.vonStaudt_clausen`。
【2026-09-24 进展 2】`kappa_egf` 已重述为 ℚ⟦X⟧ 形式幂级数版并完整证明：
`C 720 · F = X⁵ · bernoulli'PowerSeries`（逐项系数比较，`factorial_five`），
另得乘法形式 `kappa_egf_mul_exp`：`720·F·(e^t−1) = t⁶·e^t`，
即解析闭式 `t⁶/(720(e^t−1)) + t⁶/720` 的有理重写。
-/

namespace Zeta7

open BigOperators
open scoped PowerSeries

/-- 经典约定的 Bernoulli 数：与 mathlib `bernoulli` 仅在 1 处不同（B̃₁ = +1/2）。 -/
def bernClassic : ℕ → ℚ
  | 0 => 1
  | 1 => 1 / 2
  | n => _root_.bernoulli n

/-- `bernClassic` 逐点等于 mathlib 的 `bernoulli'`（同为 B₁ = +1/2 约定）。 -/
theorem bernClassic_eq_bernoulli' (n : ℕ) : bernClassic n = bernoulli' n := by
  cases n with
  | zero => simp [bernClassic, bernoulli']
  | succ n =>
    cases n with
    | zero => simp [bernClassic, bernoulli'_one]
    | succ n =>
      show _root_.bernoulli (n + 2) = bernoulli' (n + 2)
      exact bernoulli_eq_bernoulli'_of_ne_one (Nat.succ_succ_ne_one n)

/-- `bernoulli'` 的 if-形式桥（约定分歧只发生在指标 1 处）。 -/
theorem bernoulli'_eq_ite (n : ℕ) :
    bernoulli' n = (if n = 1 then 1 / 2 else _root_.bernoulli n) := by
  rcases Nat.lt_trichotomy n 1 with h | h | h
  · have h0 : n = 0 := by omega
    rw [h0]
    simp
  · rw [if_pos h, h, bernoulli'_one]
  · rw [if_neg (by omega), (bernoulli_eq_bernoulli'_of_ne_one (by omega)).symm]

/-- κ(m) = m(m−1)(m−2)(m−3)(m−4)·B̃_{m−5}/720（m ≥ 5；m < 5 时为 0）。 -/
def kappa (m : ℕ) : ℚ :=
  (∏ i ∈ Finset.Ico (m - 4) (m + 1), (i : ℚ)) * bernClassic (m - 5) / 720

/-- `kappa m = 0`（m < 5）：下降阶乘乘积含因子 0。 -/
theorem kappa_eq_zero_of_lt_five {m : ℕ} (hm : m < 5) : kappa m = 0 := by
  unfold kappa
  have h0 : (0 : ℕ) ∈ Finset.Ico (m - 4) (m + 1) :=
    Finset.mem_Ico.mpr ⟨by omega, by omega⟩
  rw [Finset.prod_eq_zero h0 (by norm_num), zero_mul, zero_div]

/-- 五连阶乘的显式展开（ℚ）：(j+5)! = (j+1)(j+2)(j+3)(j+4)(j+5)·j!。 -/
theorem factorial_five (j : ℕ) :
    ((j + 5).factorial : ℚ)
      = ((j + 1 : ℕ) : ℚ) * ((j + 2 : ℕ) : ℚ) * ((j + 3 : ℕ) : ℚ)
        * ((j + 4 : ℕ) : ℚ) * ((j + 5 : ℕ) : ℚ) * (j.factorial : ℚ) := by
  have e1 : j + 5 = (j + 4) + 1 := by omega
  have e2 : j + 4 = (j + 3) + 1 := by omega
  have e3 : j + 3 = (j + 2) + 1 := by omega
  have e4 : j + 2 = (j + 1) + 1 := by omega
  rw [e1, Nat.factorial_succ, e2, Nat.factorial_succ, e3, Nat.factorial_succ, e4,
    Nat.factorial_succ, Nat.factorial_succ]
  push_cast
  ring

/-- 五连乘积的显式展开（ℚ）：∏_{i=j+1}^{j+5} i = (j+1)(j+2)(j+3)(j+4)(j+5)。 -/
theorem prod_Ico_five (j : ℕ) :
    (∏ i ∈ Finset.Ico (j + 1) (j + 6), (i : ℚ))
      = ((j + 1 : ℕ) : ℚ) * ((j + 2 : ℕ) : ℚ) * ((j + 3 : ℕ) : ℚ)
        * ((j + 4 : ℕ) : ℚ) * ((j + 5 : ℕ) : ℚ) := by
  rw [Finset.prod_Ico_eq_prod_range, show j + 6 - (j + 1) = 5 by omega]
  simp [Finset.prod_range_succ]
  push_cast
  ring

/-- bernoulli'PowerSeries 的有理系数引理（mathlib 只给出
`mk fun n => algebraMap ℚ A (B̃_n / n!)` 的定义，这里取 A = ℚ）。 -/
theorem coeff_bernoulli'PowerSeries_rat (n : ℕ) :
    PowerSeries.coeff n (bernoulli'PowerSeries ℚ)
      = bernoulli' n / n.factorial := by
  simp [bernoulli'PowerSeries, PowerSeries.coeff_mk]

/-- **κ 的指数生成函数恒等式**（B̃₁=+1/2；`research/b8_machinery.py` §1 验证）。
形式幂级数版（已证）：`C 720 · (Σ κ(m)/m! · tᵐ) = t⁵ · Σ B̃_n/n! · tⁿ`，
即 Σ κ(m) tᵐ/m! = t⁵/720 · B̃PS。由 `(m)₅/m! = 1/(m−5)!`（factorial_five）
逐项比较系数即得；m < 5 时 κ(m) = 0 且 t⁵ 消去低次项。
解析版闭式 `t⁶/(720(e^t−1)) + t⁶/720` 由 `kappa_egf_mul_exp` 给出
（两边乘 (e^t−1) 后用 `bernoulli'PowerSeries_mul_exp_sub_one`）。 -/
theorem kappa_egf : PowerSeries.C (720 : ℚ) *
    PowerSeries.mk (fun m => (kappa m : ℚ) / m.factorial)
    = (PowerSeries.X : ℚ⟦X⟧) ^ 5 * bernoulli'PowerSeries ℚ := by
  ext m
  rw [PowerSeries.coeff_C_mul, PowerSeries.coeff_X_pow_mul']
  simp only [PowerSeries.coeff_mk]
  split_ifs with h5
  · obtain ⟨j, hj⟩ : ∃ j, m = j + 5 := ⟨m - 5, by omega⟩
    subst hj
    rw [show j + 5 - 5 = j by omega, coeff_bernoulli'PowerSeries_rat]
    have hs : kappa (j + 5)
        = (((j + 1 : ℕ) : ℚ) * ((j + 2 : ℕ) : ℚ) * ((j + 3 : ℕ) : ℚ)
            * ((j + 4 : ℕ) : ℚ) * ((j + 5 : ℕ) : ℚ)) * bernoulli' j / 720 := by
      unfold kappa
      rw [show j + 5 - 4 = j + 1 by omega, show j + 5 + 1 = j + 6 by omega,
        show j + 5 - 5 = j by omega, bernClassic_eq_bernoulli', prod_Ico_five]
    rw [hs]
    have h720 : (720 : ℚ) ≠ 0 := by norm_num
    have hf1 : (((j + 5).factorial : ℕ) : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero _
    have hf2 : ((j.factorial : ℕ) : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero _
    field_simp
    rw [factorial_five]
    ring
  · have hm : m < 5 := by omega
    rw [kappa_eq_zero_of_lt_five hm, zero_div, mul_zero]

/-- **EGF 乘法形式**（解析闭式 `t⁶/(720(e^t−1)) + t⁶/720` 的有理重写）：
`720 · F · (e^t − 1) = t⁵ · (t·e^t) = t⁶·e^t`，即
`F = t⁶·e^t/(720·(e^t−1)) = t⁶/(720(e^t−1)) + t⁶/720`。 -/
theorem kappa_egf_mul_exp : PowerSeries.C (720 : ℚ) *
    (PowerSeries.mk (fun m => (kappa m : ℚ) / m.factorial) *
      (PowerSeries.exp ℚ - 1))
    = (PowerSeries.X : ℚ⟦X⟧) ^ 5 * ((PowerSeries.X : ℚ⟦X⟧) * PowerSeries.exp ℚ) := by
  calc PowerSeries.C (720 : ℚ) *
        (PowerSeries.mk (fun m => (kappa m : ℚ) / m.factorial) *
          (PowerSeries.exp ℚ - 1))
      = (PowerSeries.C (720 : ℚ) *
          PowerSeries.mk (fun m => (kappa m : ℚ) / m.factorial)) *
        (PowerSeries.exp ℚ - 1) := by rw [mul_assoc]
    _ = ((PowerSeries.X : ℚ⟦X⟧) ^ 5 * bernoulli'PowerSeries ℚ) *
        (PowerSeries.exp ℚ - 1) := by rw [kappa_egf]
    _ = (PowerSeries.X : ℚ⟦X⟧) ^ 5 *
          (bernoulli'PowerSeries ℚ * (PowerSeries.exp ℚ - 1)) := by rw [mul_assoc]
    _ = (PowerSeries.X : ℚ⟦X⟧) ^ 5 * ((PowerSeries.X : ℚ⟦X⟧) * PowerSeries.exp ℚ) := by
        rw [bernoulli'PowerSeries_mul_exp_sub_one]

/-- **二项折叠引理**：对 e ≥ 5，
∑_{k<e} C(e,k)·κ(k) = e!/(e−5)!/720 · ∑_{j<e−5} C(e−5,j)·B̃_j。
证：k < 5 的项为 0；k = j+5 的重索引下，
C(e,j+5)·(j+1)…(j+5) = (e)₅·C(e−5,j)（`choose_mul_factorial_mul_factorial` 两条 +
`factorial_five`/`prod_Ico_five`）。 -/
theorem sum_range_choose_mul_kappa (e : ℕ) (he : 5 ≤ e) :
    (∑ k ∈ Finset.range e, (Nat.choose e k : ℚ) * kappa k)
      = ((Nat.factorial e : ℚ) / Nat.factorial (e - 5) / 720) *
        (∑ j ∈ Finset.range (e - 5), (Nat.choose (e - 5) j : ℚ) * bernoulli' j) := by
  have hsplit : (∑ k ∈ Finset.range e, (Nat.choose e k : ℚ) * kappa k)
      = ∑ k ∈ Finset.Ico 5 e, (Nat.choose e k : ℚ) * kappa k := by
    rw [Finset.range_eq_Ico, ← Finset.sum_Ico_consecutive (fun k => (Nat.choose e k : ℚ) * kappa k)
      (Nat.zero_le 5) he,
      Finset.sum_eq_zero (fun k hk => by
        rw [Finset.mem_Ico] at hk
        exact mul_eq_zero_of_right _ (kappa_eq_zero_of_lt_five (by omega))), zero_add]
  rw [hsplit, Finset.sum_Ico_eq_sum_range, Finset.mul_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  rw [show 5 + j = j + 5 by omega]
  rw [Finset.mem_range] at hj
  have hjl : j + 5 ≤ e := by omega
  have h2 := Nat.choose_mul_factorial_mul_factorial (n := e) (k := j + 5) hjl
  have h3 := Nat.choose_mul_factorial_mul_factorial (n := e - 5) (k := j) (by omega)
  have heq : e - (j + 5) = (e - 5) - j := by omega
  have h2q : (Nat.choose e (j + 5) : ℚ) * ((j + 5).factorial : ℚ)
      * ((e - (j + 5)).factorial : ℚ) = (e.factorial : ℚ) := by exact_mod_cast h2
  have h3q : (Nat.choose (e - 5) j : ℚ) * (j.factorial : ℚ)
      * (((e - 5) - j).factorial : ℚ) = ((e - 5).factorial : ℚ) := by exact_mod_cast h3
  unfold kappa
  rw [show j + 5 - 4 = j + 1 by omega, show j + 5 + 1 = j + 6 by omega,
    show j + 5 - 5 = j by omega, bernClassic_eq_bernoulli', prod_Ico_five]
  have h2' : (e.factorial : ℚ) = (Nat.choose e (j + 5) : ℚ)
      * ((((j + 1 : ℕ) : ℚ) * ((j + 2 : ℕ) : ℚ) * ((j + 3 : ℕ) : ℚ) * ((j + 4 : ℕ) : ℚ)
        * ((j + 5 : ℕ) : ℚ)) * (j.factorial : ℚ)) * (((e - 5) - j).factorial : ℚ) := by
    rw [← h2q, heq, factorial_five]
  have h3' : ((e - 5).factorial : ℚ) = (Nat.choose (e - 5) j : ℚ) * (j.factorial : ℚ)
      * (((e - 5) - j).factorial : ℚ) := by rw [← h3q]
  rw [h2', h3']
  have hc0 : (Nat.choose (e - 5) j : ℚ) ≠ 0 := by
    have hpos : 0 < Nat.choose (e - 5) j := Nat.choose_pos (by omega)
    exact_mod_cast (Nat.pos_iff_ne_zero.mp hpos)
  have hf0 : (j.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero j
  have hg0 : (((e - 5) - j).factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero _
  field_simp

/-- 差分恒等式（`research/b8_machinery.py` §2 验证：e = 1,5,6,7,8,11 全部精确）。
陈述：∑_{k<e} C(e,k)κ(k) = [e≥6]·e!/(e−6)!/720。
证明：e < 6 时各项 κ(k) = 0（k ≤ 5）；e ≥ 6 时由 `sum_range_choose_mul_kappa`
与 mathlib 的 Bernoulli 二项和 `sum_bernoulli'`（= e−5）组合。 -/
theorem kappa_difference (e : ℕ) :
    (∑ k ∈ Finset.range e, (Nat.choose e k : ℚ) * kappa k) =
      (if 6 ≤ e then (Nat.factorial e : ℚ) / Nat.factorial (e - 6) / 720 else 0) := by
  rcases Nat.lt_or_ge e 6 with he | he
  · rw [if_neg (Nat.not_le.mpr he)]
    exact Finset.sum_eq_zero fun k hk => by
      rw [Finset.mem_range] at hk
      exact mul_eq_zero_of_right _ (kappa_eq_zero_of_lt_five (by omega))
  · rw [if_pos he, sum_range_choose_mul_kappa e (by omega)]
    have hs := sum_bernoulli' (e - 5)
    rw [hs]
    have h5f : ((e - 5).factorial : ℚ) = ((e - 5 : ℕ) : ℚ) * ((e - 6).factorial : ℚ) := by
      have h : e - 5 = (e - 6) + 1 := by omega
      rw [h, Nat.factorial_succ]
      push_cast
      ring
    have h1 : ((e - 5 : ℕ) : ℚ) ≠ 0 := by exact_mod_cast (by omega : e - 5 ≠ 0)
    have h2 : ((e - 6).factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero _
    rw [h5f]
    field_simp

set_option maxHeartbeats 400000 in
/-- von Staudt 型赋值界（`b8_machinery.py` §5：7≤p≤59、5≤d≤79 零违规）。
v_p(κ d) ≥ −1（p ≥ 7）。证明：v_p((d)₅) ≥ 0、v_p(720) = 0（p ≥ 7），
v_p(B̃_{d−5}) ≥ −1 由 mathlib 的 von Staudt–Clausen 定理给出
（奇指标 > 1 为零；偶指标 B_{2k} + Σ1/p ∈ ℤ，而修正和每项 v_p ≥ −1
——取 1/p 时为 −1、取 1/q（q ≠ p 素数）时为 0——故 v_p(B) ≥ −1）。 -/
theorem kappa_val (p d : ℕ) (hp : p.Prime) (hp7 : 7 ≤ p) (hd : 5 ≤ d) :
    padicValRat p (kappa d) ≥ -1 := by
  haveI : Fact p.Prime := ⟨hp⟩
  have h720 : padicValRat p (720 : ℚ) = 0 := by
    have h720n : padicValNat p 720 = 0 := by
      refine padicValNat.eq_zero_of_not_dvd (fun h => ?_)
      have e720 : 720 = 2 ^ 4 * 3 ^ 2 * 5 := by norm_num
      rw [e720] at h
      rcases hp.dvd_mul.mp h with h1 | h2
      · rcases hp.dvd_mul.mp h1 with h3 | h4
        · have h23 : 2 = p := (Nat.prime_two.dvd_iff_eq hp.one_lt.ne').mp (hp.dvd_of_dvd_pow h3)
          omega
        · have h23 : 3 = p := (Nat.prime_three.dvd_iff_eq hp.one_lt.ne').mp (hp.dvd_of_dvd_pow h4)
          omega
      · have h5 : 5 = p := (Nat.prime_five.dvd_iff_eq hp.one_lt.ne').mp h2
        omega
    have e : (720 : ℚ) = ((720 : ℕ) : ℚ) := by norm_num
    rw [e, padicValRat.of_nat, h720n, Nat.cast_zero]
  have hApos : 0 < (∏ i ∈ Finset.Ico (d - 4) (d + 1), (i : ℚ)) := by
    refine Finset.prod_pos fun i hi => ?_
    rw [Finset.mem_Ico] at hi
    have : 0 < i := by omega
    exact_mod_cast this
  have hB : -1 ≤ padicValRat p (bernoulli' (d - 5)) := by
    set m := d - 5 with hm
    rcases Nat.even_or_odd m with hev | hod
    · rcases hev with ⟨k, hk⟩
      rcases Nat.lt_or_ge k 1 with hk0 | hk1
      · have hm0 : m = 0 := by omega
        rw [hm0, bernoulli'_zero, padicValRat.one]
        norm_num
      · have hk2 : m = 2 * k := by omega
        have hne : 2 * k ≠ 1 := by omega
        rw [hk2, ← bernoulli_eq_bernoulli'_of_ne_one hne]
        have hvs := Bernoulli.vonStaudt_clausen k
        rw [Set.mem_range] at hvs
        obtain ⟨z, hz⟩ := hvs
        have hz' : bernoulli (2 * k) = (z : ℚ) - ∑ q ∈ (Finset.range (2 * k + 2)).filter
            (fun q => q.Prime ∧ (q - 1) ∣ 2 * k), (1 : ℚ) / q := by
          rw [hz]
          ring
        set idx := (Finset.range (2 * k + 2)).filter
          (fun q => q.Prime ∧ (q - 1) ∣ 2 * k) with hidx
        set S : ℚ := ∑ q ∈ idx, (1 : ℚ) / q with hSdef
        have hterm : ∀ q ∈ idx, -1 ≤ padicValRat p ((1 : ℚ) / q) := by
          intro q hq
          rw [hidx, Finset.mem_filter] at hq
          obtain ⟨hqr, hqp⟩ := hq
          rw [Finset.mem_range] at hqr
          have hq0 : (q : ℚ) ≠ 0 := by exact_mod_cast hqp.1.ne_zero
          rcases eq_or_ne q p with rfl | hne
          · rw [padicValRat.div (p := q) one_ne_zero (by exact_mod_cast hp.ne_zero), padicValRat.one,
              padicValRat.self (p := q) hp.one_lt]
            norm_num
          · rw [padicValRat.div (p := p) one_ne_zero hq0, padicValRat.one, padicValRat.of_nat,
              padicValNat.eq_zero_of_not_dvd
                (fun hd => hne ((hqp.1.dvd_iff_eq hp.one_lt.ne').mp hd)),
              Nat.cast_zero, sub_zero]
            norm_num
        have hS : -1 ≤ padicValRat p S := by
          have key : ∀ s : Finset ℕ, s ⊆ idx →
              -1 ≤ padicValRat p (∑ q ∈ s, (1 : ℚ) / q) := by
            intro s
            refine Finset.induction_on s (fun _ => ?_) (fun q s' hqs' ih hsub => ?_)
            · rw [Finset.sum_empty, padicValRat.zero]
              norm_num
            · rw [Finset.sum_insert hqs']
              have hv := hterm q (hsub (Finset.mem_insert_self q s'))
              have hr := ih fun x hx => hsub (Finset.mem_insert_of_mem hx)
              have hpos : 0 < (1 : ℚ) / q + ∑ x ∈ s', (1 : ℚ) / x := by
                have hq' := hsub (Finset.mem_insert_self q s')
                rw [hidx, Finset.mem_filter] at hq'
                have h1 : (0 : ℚ) < 1 / q := div_pos one_pos (by exact_mod_cast hq'.2.1.pos)
                have h2 : (0 : ℚ) ≤ ∑ x ∈ s', (1 : ℚ) / x :=
                  Finset.sum_nonneg fun x _ => div_nonneg zero_le_one (Nat.cast_nonneg x)
                linarith
              exact (le_min hv hr).trans (padicValRat.min_le_padicValRat_add (p := p) (ne_of_gt hpos))
          exact key idx Finset.Subset.rfl
        have hznn : 0 ≤ padicValRat p (z : ℚ) := by
          rw [padicValRat.of_int]
          exact Nat.cast_nonneg _
        have hBnn : -1 ≤ padicValRat p (bernoulli (2 * k)) := by
          rw [hz', sub_eq_add_neg]
          rcases eq_or_ne ((z : ℚ) + -S) 0 with hz0 | hz0
          · rw [hz0, padicValRat.zero]
            norm_num
          · have hmin := padicValRat.min_le_padicValRat_add (p := p) hz0
            rw [padicValRat.neg] at hmin
            have hm2 : -1 ≤ min (padicValRat p (z : ℚ)) (padicValRat p S) :=
              le_min (by omega : -1 ≤ padicValRat p (z : ℚ)) hS
            exact le_trans hm2 hmin
        exact hBnn
    · rcases Nat.lt_or_ge m 3 with hm3 | hm3
      · rcases hod with ⟨t, ht⟩
        have hm1 : m = 1 := by omega
        rw [hm1, bernoulli'_one]
        have e2 : (2 : ℚ) = ((2 : ℕ) : ℚ) := by norm_num
        rw [e2, padicValRat.div (p := p) one_ne_zero (by norm_num : ((2 : ℕ) : ℚ) ≠ 0), padicValRat.one,
          padicValRat.of_nat,
          padicValNat.eq_zero_of_not_dvd
            (fun h => by have := (Nat.prime_two.dvd_iff_eq hp.one_lt.ne').mp h; omega),
          Nat.cast_zero, sub_zero]
        norm_num
      · rw [bernoulli'_eq_zero_of_odd hod (by omega : 1 < m), padicValRat.zero]
        norm_num
  rcases eq_or_ne (bernoulli' (d - 5)) 0 with hB0 | hB0
  · have hk : kappa d = 0 := by
      unfold kappa
      rw [bernClassic_eq_bernoulli', hB0, mul_zero, zero_div]
    rw [hk, padicValRat.zero]
    norm_num
  · have hq0 : (∏ i ∈ Finset.Ico (d - 4) (d + 1), (i : ℚ)) * bernoulli' (d - 5) ≠ 0 :=
      mul_ne_zero (ne_of_gt hApos) hB0
    unfold kappa
    rw [bernClassic_eq_bernoulli', padicValRat.div (p := p) hq0 (by norm_num : (720 : ℚ) ≠ 0), h720,
      sub_zero, padicValRat.mul (p := p) (ne_of_gt hApos) hB0]
    have hA : 0 ≤ padicValRat p (∏ i ∈ Finset.Ico (d - 4) (d + 1), (i : ℚ)) := by
      have e : (∏ i ∈ Finset.Ico (d - 4) (d + 1), (i : ℚ))
          = (↑(∏ i ∈ Finset.Ico (d - 4) (d + 1), i) : ℚ) :=
        (Nat.cast_prod (fun i => i) _).symm
      rw [e]
      exact zero_le_padicValRat_of_nat _
    linarith

end Zeta7
