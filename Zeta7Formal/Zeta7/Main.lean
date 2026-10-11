import Mathlib
import Zeta7.Construction
import Zeta7.Tau
import Zeta7.Harmonic
import Zeta7.Zeta7Def
import Zeta7.MainEstimate
import Apery.Criterion

/-!
# ζ(7) 判定层：陈述、证据映射与主定理骨架

本文件把 `research/` 中已完成的数学验证转写为 Lean 目标，按依赖链排列。
每条 sorry 的 doc comment 给出证明路线与对应的机器验证文件——
"一边研究一边形式化"的落点：研究产出 ⇒ 在此登记陈述与证据 ⇒ 逐条消灭 sorry。
-/

namespace Zeta7

open Polynomial BigOperators
open scoped Polynomial

/-! ## 一、已完成的数学验证对应的陈述（证据：research/*.py，60 位/精确有理） -/

/-- **极点值精确闭式**（式 (2.3)-类比，`research/zeta7_pole_values.py` 60 位验证）。
【2026-09-25 已证，纯代数路线】`μX j (D j / (X + j²)) = poleValue j`：被积多项式
`P = D j / (X + C j²) = D (j−1)` 次数低于 `D j`（商部为零），且在极点 `−i²`
处：i < j 时分子分母同为 0（ℚ 中 0/0 = 0，该项消失）；i = j 时
`D j = (X + j²)·D (j−1)` 求值得 `(D j)'(−j²) = D (j−1)(−j²)`，
残差恰为 1。矩表示（μmono/Euler 消 π 的奇迹）由 `μX` 构造的定义层承担
（与 `Apery.μX` 同构的做法），本引理是判定层入口。 -/
theorem pole_value_exact (j : ℕ) (hj : 1 ≤ j) :
    μX j (D j / (X + C ((j : ℚ) ^ 2))) = poleValue j := by
  have hjs : j - 1 + 1 = j := Nat.sub_add_cancel hj
  -- 0. `Icc 1 j = insert j (Icc 1 (j−1))`
  have hIcc : Finset.Icc 1 j = insert j (Finset.Icc 1 (j - 1)) := by
    ext x
    simp only [Finset.mem_Icc, Finset.mem_insert]
    constructor
    · rintro ⟨h1, h2⟩
      by_cases hxj : x = j
      · exact Or.inl hxj
      · exact Or.inr ⟨h1, Nat.le_sub_one_of_lt (lt_of_le_of_ne h2 hxj)⟩
    · rintro (rfl | ⟨h1, h2⟩)
      · exact ⟨hj, le_rfl⟩
      · exact ⟨h1, by omega⟩
  -- 1. `D j = (X + j²) * D (j−1)`
  have hD : D j = (X + C ((j : ℚ) ^ 2)) * D (j - 1) := by
    conv_lhs => rw [D, hIcc, Finset.prod_insert (by simp only [Finset.mem_Icc]; omega)]
    conv_rhs => rw [D]
  -- 2. 商：`D j / (X + j²) = D (j−1)`
  have hP : D j / (X + C ((j : ℚ) ^ 2)) = D (j - 1) := by
    rw [← divByMonic_eq_div _ (monic_X_add_C _), hD]
    exact mul_divByMonic_cancel_left _ (monic_X_add_C _)
  -- 3. Monic 与次数
  have hDmonic : ∀ m, Monic (D m) := fun m =>
    monic_prod_of_monic _ _ fun i _ => monic_X_add_C _
  have hdeg : ∀ m, (D m).natDegree = m := by
    intro m
    rw [D, natDegree_prod_of_monic _ _ (fun i _ => monic_X_add_C _),
      Finset.sum_congr rfl (fun i _ => natDegree_X_add_C _), Finset.sum_const,
      Nat.card_Icc, smul_eq_mul, mul_one]
    omega
  -- 4. 商部为零：`D (j−1) /ₘ D j = 0`
  have hquot : D (j - 1) /ₘ D j = 0 := by
    rw [divByMonic_eq_zero_iff (hDmonic j)]
    rw [degree_eq_natDegree (hDmonic (j - 1)).ne_zero,
      degree_eq_natDegree (hDmonic j).ne_zero, hdeg, hdeg]
    exact_mod_cast Nat.sub_lt (by omega) one_pos
  -- 5. 分子求值：`D (j−1)(−i²) = ∏_{v≤j−1} (v² − i²)`
  have heval : ∀ i : ℕ,
      (D (j - 1)).eval (-(i : ℚ) ^ 2)
        = ∏ v ∈ Finset.Icc 1 (j - 1), ((v : ℚ) ^ 2 - (i : ℚ) ^ 2) := by
    intro i
    rw [D, Polynomial.eval_prod]
    refine Finset.prod_congr rfl fun v _ => ?_
    simp only [Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C]
    ring
  -- 6. 导数：`(D j)'(−j²) = D (j−1)(−j²)`
  have hder : (derivative (D j)).eval (-(j : ℚ) ^ 2)
      = (D (j - 1)).eval (-(j : ℚ) ^ 2) := by
    have hQ0 : (X + C ((j : ℚ) ^ 2)).eval (-(j : ℚ) ^ 2) = 0 := by
      simp only [Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C]
      ring
    have hdQ : derivative (X + C ((j : ℚ) ^ 2)) = 1 := by
      rw [Polynomial.derivative_add, Polynomial.derivative_X, Polynomial.derivative_C, add_zero]
    rw [hD, Polynomial.derivative_mul, Polynomial.eval_add, Polynomial.eval_mul,
      Polynomial.eval_mul, hdQ, Polynomial.eval_one, one_mul, hQ0, zero_mul, add_zero]
  -- 7. 分子在 `−j²` 处非零
  have hne : (D (j - 1)).eval (-(j : ℚ) ^ 2) ≠ 0 := by
    rw [heval]
    refine Finset.prod_ne_zero_iff.mpr fun v hv => ?_
    rw [Finset.mem_Icc] at hv
    have hvj : (v : ℚ) < (j : ℚ) :=
      by exact_mod_cast (hv.2.trans_lt (Nat.sub_lt hj one_pos))
    have hvj2 : (v : ℚ) ^ 2 < (j : ℚ) ^ 2 := by
      rw [sq_lt_sq, abs_of_nonneg (by positivity), abs_of_nonneg (by positivity)]
      exact hvj
    exact sub_ne_zero_of_ne hvj2.ne
  -- 8. 残差逐项：`i = j` 时为 1，否则 0
  have hres : ∀ i ∈ Finset.Icc 1 j,
      (D (j - 1)).eval (-(i : ℚ) ^ 2) / (derivative (D j)).eval (-(i : ℚ) ^ 2)
        = if i = j then 1 else 0 := by
    intro i hi
    rw [Finset.mem_Icc] at hi
    by_cases hij : i = j
    · subst hij
      rw [if_pos rfl, hder, div_self hne]
    · rw [if_neg hij]
      have himem : i ∈ Finset.Icc 1 (j - 1) :=
        Finset.mem_Icc.mpr ⟨hi.1, Nat.le_sub_one_of_lt (lt_of_le_of_ne hi.2 hij)⟩
      have hnum : (D (j - 1)).eval (-(i : ℚ) ^ 2) = 0 := by
        rw [D, Polynomial.eval_prod]
        exact Finset.prod_eq_zero himem (by
          simp only [Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C]
          ring)
      rw [hnum, zero_div]
  -- 9. 求和坍缩
  have hsum : (∑ i ∈ Finset.Icc 1 j,
      C ((D (j - 1)).eval (-(i : ℚ) ^ 2) / (derivative (D j)).eval (-(i : ℚ) ^ 2)) *
        poleValue i) = poleValue j := by
    have h1 : (∑ i ∈ Finset.Icc 1 j,
        C ((D (j - 1)).eval (-(i : ℚ) ^ 2) / (derivative (D j)).eval (-(i : ℚ) ^ 2)) *
          poleValue i)
        = ∑ i ∈ Finset.Icc 1 j, C ((if i = j then 1 else 0 : ℚ)) * poleValue i := by
      refine Finset.sum_congr rfl fun i hi => ?_
      rw [hres i hi]
    rw [h1, hIcc, Finset.sum_insert (by simp only [Finset.mem_Icc]; omega), if_pos rfl,
      Polynomial.C_1, one_mul, Finset.sum_eq_zero (fun i hi => by
        rw [Finset.mem_Icc] at hi
        rw [if_neg (by omega), Polynomial.C_0, zero_mul]), add_zero]
  -- 10. 展开 `μX` 并组装
  have hμ0 : μpoly 0 = 0 := by simp [μpoly]
  rw [μX, hP, hquot, hμ0, Polynomial.C_0, zero_add, hsum]

/-- **τ₈ 差分恒等式**（式 (3.3)-类比，`research/b8_machinery.py` 验证通过）。
κ(m) = (m)₅·B̃_{m−5}/720，其中 B̃ 取经典约定 B₁ = +1/2（`research/NOTES.md`
§2 的约定陷阱：构造只用偶数指标，此约定只影响恒等式的陈述形式）。
恒等式：κ((x+1)^e − x^e 的系数和) = ∑_{k<e} C(e,k)·κ(k) = [e≥6]·e!/(e−6)!/720。
【2026-09-24 更正】原陈述带 `- κ e` 尾项，**为假**（e = 6：LHS = 1 − 1/2 = 1/2 ≠ 1；
与 zeta5 骨架 `eq_3_3_false` 同类：差分 (x+1)^e − x^e 的 x^e 项相互抵消，
求和本就不含 κ(e)）。已按数值验证的恒等式重述（`b8_machinery.py` §2 全次数精确）。
证明：`Zeta7/Tau.lean` 的 `kappa_difference`（生成函数系数比较，
`bernoulli'PowerSeries_mul_exp_sub_one`）。 -/
theorem tau8_difference (e : ℕ) (κ : ℕ → ℚ)
    (hκ : ∀ m, κ m = (∏ i ∈ Finset.Ico (m - 4) (m + 1), (i : ℚ)) *
      (if m - 5 = 1 then 1 / 2 else _root_.bernoulli (m - 5)) / 720) :
    (∑ k ∈ Finset.range e, (Nat.choose e k : ℚ) * κ k) =
      (if 6 ≤ e then (Nat.factorial e : ℚ) / Nat.factorial (e - 6) / 720 else 0) := by
  have hκ' : κ = kappa := by
    funext m
    rw [hκ, kappa, ← bernoulli'_eq_ite, bernClassic_eq_bernoulli']
  rw [hκ']
  exact kappa_difference e

/-- **von Staudt 赋值界**（式 (3.10)/(3.12)-类比的分量，`b8_machinery.py` §5
零违规验证）：素数 p ≥ 7、d ≥ 5 时 v_p(κ_d) ≥ −1。
【2026-09-24 已证】`Zeta7/Tau.lean` 的 `kappa_val`（mathlib von Staudt–Clausen
定理 + p-进赋值超度量不等式）。 -/
theorem kappa_valuation (p d : ℕ) (hp : p.Prime) (hp7 : 7 ≤ p) (hd : 5 ≤ d) :
    padicValRat p ((∏ i ∈ Finset.Ico (d - 4) (d + 1), (i : ℚ)) *
      (if d - 5 = 1 then 1 / 2 else _root_.bernoulli (d - 5)) / 720) ≥ -1 := by
  rw [← bernoulli'_eq_ite, ← bernClassic_eq_bernoulli']
  change padicValRat p (kappa d) ≥ -1
  exact kappa_val p d hp hp7 hd

/-- **H⁽⁷⁾ 调和损失界**（式 (3.10) 分量，`b8_machinery.py` §6 零违规验证）：
v_p(H_j⁽⁷⁾) ≥ −7⌊log_p j⌋。
【2026-09-24 已证】`Zeta7/Harmonic.lean` 的 `harmonic7_val_aux`
（对 j 归纳：单项界 `p^padicValNat ∣ j+1` + mathlib `Nat.le_log_iff_pow_le`
+ `padicValRat.min_le_padicValRat_add` 超度量合并）。 -/
theorem harmonic7_valuation (p j : ℕ) (hp : p.Prime) :
    padicValRat p (∑ v ∈ Finset.Icc 1 j, (1 : ℚ) / (v : ℚ) ^ 7) ≥ -7 * (Nat.log p j : ℤ) :=
  harmonic7_val_aux p j hp

/-! ## 二、判定层（证据：`research/b8_verdict.md` + `b8_final.py`） -/

-- 注：`main_estimate`（Theorem 2.1 类比）本身在 `Zeta7.MainEstimate` 中
-- （归一化 ✅ growth_mN/integral_mN + 实侧界 `Zeta7.RealBound.real_bound`
-- 〔能量链，唯一 sorry〕+ `Aeff_margin`：decay 率 c = 800·(−(Aeff+U)) > 0），
-- 本文件经 `import Zeta7.MainEstimate` 引入，下方 `zeta7_irrational` 直接使用。

/-- **Theorem 1.1（ζ(7)）**：由 main_estimate 经多项式障碍判据
（直接复用 `Apery.irrational_of_eventually_exists_int_poly`，b 无关）得出。 -/
theorem zeta7_irrational : Irrational zeta7 := by
  obtain ⟨c, hc, h⟩ := main_estimate
  exact Apery.irrational_of_eventually_exists_int_poly zeta7 (fun n => 37 * n)
    (fun n => Real.exp (-c * (n : ℝ) ^ 2))
    (Apery.tendsto_pow_mul_exp_neg_sq_of_pos hc)
    (h.mono fun _ ⟨Q, hdeg, hpos, hle⟩ => ⟨Q, hdeg.le, hpos, hle⟩)

/-- **绝对版**：与 mathlib `riemannZeta` 连接（`Apery.irrational_five` 的 b=8 类比）。 -/
theorem irrational_seven : ∃ x : ℝ, Irrational x ∧ riemannZeta 7 = x :=
  ⟨zeta7, zeta7_irrational, riemannZeta_seven⟩

end Zeta7
