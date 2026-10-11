import Mathlib
import Apery.Main
import Zeta5Irrational.Params
import Zeta5Irrational.Functional
import Zeta5Irrational.Propositions
import Zeta5Irrational.Numerics

/-!
# 主要结果（论文 Theorem 2.1、Theorem 1.1、Corollary 1.2）

- `theorem_2_1`：Theorem 2.1 的陈述（sorry，对应论文 §2–§7 的全部估计）。
- `zeta5_irrational`：Theorem 1.1，**完整证明**——由 Theorem 2.1（M = 200 情形）
  的经典归约：b^{37n}·Q_n(a/b) 为正整数却趋于 0。
- `corollary_1_2`：Corollary 1.2 的陈述（sorry，证明见论文 Appendix C）。
-/

open scoped Polynomial

namespace Zeta5Irrational

/-- Theorem 2.1（论文 §2.2）：对每个整数 M ≥ 40 与 K = 40n ≥ 200M²，
    Q_{K,M} ∈ ℤ[X]（以整数多项式在 ℚ[X] 中的像呈现），次数为 h = 37n，
    且 Q_{K,M}(ζ(5)) > 0。由 prop_5_1（整性）、delta_natDegree（次数）与
    prop_6_3（正性）组装。 -/
theorem theorem_2_1 (M : ℕ) (hM : 40 ≤ M) (n : ℕ) (hn : 200 * M ^ 2 ≤ Kparam n) :
    (∃ P : ℤ[X], Polynomial.map (Int.castRingHom ℚ) P = QKM n M)
    ∧ (QKM n M).natDegree = hparam n
    ∧ 0 < (QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5 := by
  have hnpos : 0 < n := by
    rcases Nat.eq_zero_or_pos n with hn0 | hnpos
    · exfalso
      have h0 : Kparam 0 = 0 := rfl
      rw [hn0, h0] at hn
      have h1 : 200 * M ^ 2 = 0 := Nat.eq_zero_of_le_zero hn
      have h2 : M = 0 := by
        have h3 : M ^ 2 = 0 := (Nat.mul_eq_zero.mp h1).resolve_left (by norm_num)
        exact (pow_eq_zero_iff (by norm_num : (2 : ℕ) ≠ 0)).mp h3
      omega
    · exact hnpos
  have hdK : (deltaK n).natDegree = hparam n := delta_natDegree n hnpos
  have hdK0 : deltaK n ≠ 0 := fun h0 => by
    rw [h0, Polynomial.natDegree_zero] at hdK
    dsimp [hparam] at hdK
    omega
  have hSK0 : SK n ≠ 0 := by
    have h1 : (0 : ℚ) < SK n := by
      rw [SK]
      apply div_pos
      · apply mul_pos
        · exact pow_pos (Nat.cast_pos.mpr (Nat.factorial_pos _)) _
        · exact zpow_pos (by norm_num) _
      · apply mul_pos
        · exact pow_pos (Nat.cast_pos.mpr (Nat.factorial_pos _)) _
        · apply Finset.prod_pos
          intro i _
          exact pow_pos (Nat.cast_pos.mpr (Nat.factorial_pos _)) _
    exact ne_of_gt h1
  refine ⟨prop_5_1 n M hM hn, ?_, ?_⟩
  · rw [QKM, FK, Polynomial.natDegree_mul (Polynomial.C_ne_zero.mpr (ne_of_gt (mKM_pos n M)))
      (mul_ne_zero (Polynomial.C_ne_zero.mpr hSK0) hdK0),
      Polynomial.natDegree_mul (Polynomial.C_ne_zero.mpr hSK0) hdK0,
      Polynomial.natDegree_C, Polynomial.natDegree_C, hdK]
    omega
  · rw [QKM, Polynomial.eval₂_mul, Polynomial.eval₂_C]
    exact mul_pos (by
      show (0 : ℝ) < ((mKM n M : ℚ) : ℝ)
      exact_mod_cast mKM_pos n M) (prop_6_3 n hnpos).1

/-- 衰减估计的公共推导：由 (7.1)（`hl`）与余量（`hmargin`）推出
    0 < Q_{40n,M}(ζ(5)) < exp(−r n²) 对充分大的 n。
    有界性 `hbdd` 用"反证 + `Real.sInf_empty`"从 (7.1) 的负上界推出：
    若 log Q/K² 无界，则其 limsup 为 `sInf ∅ = 0`，与 (7.1) 给出的负值矛盾。 -/
private theorem theorem_2_1_decay_of (M : ℕ) (hM : 40 ≤ M) (r : ℝ) (hr : 0 < r)
    (hmargin : -1600 * ((AM M : ℝ) + (Ubar : ℝ)) - r > 0)
    (hl : Filter.limsup
      (fun n : ℕ => Real.log ((QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5) / (Kparam n : ℝ) ^ 2)
      Filter.atTop ≤ (AM M : ℝ) + (Ubar : ℝ)) :
    ∀ᶠ n in Filter.atTop,
      0 < (QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5
      ∧ (QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5 < Real.exp (-r * (n : ℝ) ^ 2) := by
  set g : ℕ → ℝ := fun n => Real.log ((QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5)
    / (Kparam n : ℝ) ^ 2 with hg
  have hbdd : Filter.IsBoundedUnder (· ≤ ·) Filter.atTop g := by
    by_contra hcon
    have key : Filter.limsup g Filter.atTop = sInf {a : ℝ | ∀ᶠ n in Filter.atTop, g n ≤ a} := rfl
    have hempty : {a : ℝ | ∀ᶠ n in Filter.atTop, g n ≤ a} = ∅ := by
      ext a
      simp only [Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false]
      exact fun h => hcon ⟨a, h⟩
    rw [key, hempty, Real.sInf_empty] at hl
    linarith
  have hlim : Filter.limsup g Filter.atTop < -r / 1600 := by
    have he : -r / 1600 = (AM M : ℝ) + (Ubar : ℝ) + (-1600 * ((AM M : ℝ) + (Ubar : ℝ)) - r) / 1600 :=
      by ring
    rw [he]
    exact lt_of_le_of_lt hl (by have := hmargin; linarith)
  obtain ⟨N, hN⟩ := Filter.eventually_atTop.1 (Filter.eventually_lt_of_limsup_lt hlim hbdd)
  filter_upwards [Filter.eventually_atTop.2 ⟨max N 1, fun n hn => hN n ((le_max_left N 1).trans hn)⟩,
    Filter.eventually_ge_atTop 1] with n hn hn1
  have hQpos : (0 : ℝ) < (QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5 := by
    rw [QKM, Polynomial.eval₂_mul, Polynomial.eval₂_C]
    exact mul_pos (by
      show (0 : ℝ) < ((mKM n M : ℚ) : ℝ)
      exact_mod_cast mKM_pos n M) (prop_6_3 n hn1).1
  refine ⟨hQpos, ?_⟩
  have hK0 : (Kparam n : ℝ) ≠ 0 := by
    have h1 : 0 < (Kparam n : ℝ) := by
      exact_mod_cast Nat.mul_pos (by norm_num) hn1
    exact ne_of_gt h1
  have hgK : Real.log ((QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5) = g n * (Kparam n : ℝ) ^ 2 := by
    rw [hg, div_mul_cancel₀ _ (pow_ne_zero 2 hK0)]
  have hKn : (Kparam n : ℝ) ^ 2 = 1600 * (n : ℝ) ^ 2 := by
    have e1 : (Kparam n : ℝ) = 40 * (n : ℝ) := by
      show ((40 * n : ℕ) : ℝ) = 40 * (n : ℝ)
      push_cast
      ring
    rw [e1]
    ring
  have hQexp : (QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5
      = Real.exp (Real.log ((QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5)) := (Real.exp_log hQpos).symm
  rw [hQexp, hgK, hKn]
  apply (Real.exp_lt_exp).2
  have hn2 : (0 : ℝ) < 1600 * (n : ℝ) ^ 2 := by positivity
  have := mul_lt_mul_of_pos_right hn hn2
  linarith

/-- Theorem 2.1 的衰减估计（论文式 (2.7)，M = 200）：对充分大的 n，
    0 < Q_{40n,200}(ζ(5)) < exp(−(139/5)n²)。 -/
theorem theorem_2_1_decay_200 : ∀ᶠ n in Filter.atTop,
    0 < (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5
    ∧ (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5 < Real.exp (-(139 / 5 : ℝ) * (n : ℝ) ^ 2) :=
  theorem_2_1_decay_of 200 (by norm_num) (139 / 5) (by norm_num)
    (by have h2 := congrArg (fun q : ℚ => (q : ℝ)) margin_200_sub
        push_cast at h2
        have h3 : (0:ℝ) < 3089837638249482469 / 58872425992515135000 := by norm_num
        linarith)
    (eq_7_1 200 (by norm_num))

/-- Theorem 2.1 的衰减估计（论文式 (2.8) 的修正版，M = 100000）。

    **陈述修正**：论文式 (2.8) 原文下标为 M = 10000，但其系数 7907/100 与
    Appendix B.3 的实际余量不符（审计：M = 10000 只给出衰减系数 ≈ 78.146 < 79.07；
    M = 100000 才达到 7907/100 ≈ 79.078，且 Appendix C.2 实际使用的就是 M = 100000）。
    此处将 (2.8) 修正为 M = 100000（数值余量 `margin_100000` 已精确验证）。 -/
theorem theorem_2_1_decay_100000 : ∀ᶠ n in Filter.atTop,
    0 < (QKM n 100000).eval₂ (algebraMap ℚ ℝ) zeta5
    ∧ (QKM n 100000).eval₂ (algebraMap ℚ ℝ) zeta5
      < Real.exp (-(7907 / 100 : ℝ) * (n : ℝ) ^ 2) :=
  theorem_2_1_decay_of 100000 (by norm_num) (7907 / 100) (by norm_num)
    (by have h2 := congrArg (fun q : ℚ => (q : ℝ)) margin_100000_sub
        push_cast at h2
        have h3 : (0:ℝ) < 29873543950273155160680943 / 3679526624532195937500000000 := by norm_num
        linarith)
    (eq_7_1 100000 (by norm_num))

/-! ## 归约定理（Theorem 1.1）的完整证明 -/

/-- (algebraMap ℚ ℝ) ∘ (Int.castRingHom ℚ) = Int.castHom ℝ 到 ℝ 的整数嵌入。 -/
theorem comp_algebraMap_castRingHom :
    (algebraMap ℚ ℝ).comp (Int.castRingHom ℚ) = Int.castRingHom ℝ := by
  apply DFunLike.ext
  intro z
  show ((z : ℚ) : ℝ) = ((z : ℤ) : ℝ)
  exact Rat.cast_intCast z

/-- ℤ[X] 经 ℚ[X] 到 ℝ 的求值与直接求值一致。 -/
theorem eval₂_map_eq (P : ℤ[X]) (x : ℝ) :
    (P.map (Int.castRingHom ℚ)).eval₂ (algebraMap ℚ ℝ) x
      = P.eval₂ (Int.castRingHom ℝ) x := by
  rw [Polynomial.eval₂_map, comp_algebraMap_castRingHom]

/-- ℤ[X] 在 ℚ 点的求值经 ℝ 提升后与直接求实求值一致。 -/
theorem eval₂_castRingHom_real (P : ℤ[X]) (x : ℚ) :
    ((P.eval₂ (Int.castRingHom ℚ) x : ℚ) : ℝ)
      = P.eval₂ (Int.castRingHom ℝ) (x : ℝ) := by
  rw [Polynomial.eval₂_eq_sum_range, Polynomial.eval₂_eq_sum_range]
  push_cast
  refine Finset.sum_congr rfl fun i _ => ?_
  simp

/-- 核心整性引理：对 P : ℤ[X]，b ≥ 1 与 d ≥ deg P，b^d · P(a/b) 是整数。 -/
theorem pow_mul_eval_int (P : ℤ[X]) (a : ℤ) (b : ℕ) (d : ℕ) (hd : P.natDegree ≤ d)
    (hb : 0 < b) :
    ∃ z : ℤ, (b : ℚ) ^ d * P.eval₂ (Int.castRingHom ℚ) ((a : ℚ) / b) = z := by
  classical
  refine ⟨∑ i ∈ Finset.range (P.natDegree + 1), P.coeff i * a ^ i * b ^ (d - i), ?_⟩
  rw [Polynomial.eval₂_eq_sum_range, Finset.mul_sum]
  push_cast
  refine Finset.sum_congr rfl fun i hi => ?_
  have hi' : i ≤ d := by
    have h := Finset.mem_range.mp hi
    omega
  have hb' : (b : ℚ) ≠ 0 := by positivity
  rw [div_pow]
  rw [show (b : ℚ) ^ d = (b : ℚ) ^ (d - i) * (b : ℚ) ^ i by
    rw [← pow_add]; congr 1; omega]
  push_cast [Int.coe_castRingHom]
  field_simp

/-- **Theorem 1.1**（论文 §1）：ζ(5) 无理。证明：设 ζ(5) = a/b，取 Theorem 2.1
    的多项式列 Q_n = Q_{40n,200}，则 b^{37n}·Q_n(a/b) ∈ ℤ_{>0}（Q_n ∈ ℤ[X]、
    deg = 37n、且 Q_n(a/b) = Q_n(ζ(5)) > 0），但它 < exp(37n log b − (139/5)n²)，
    n 充分大时 < 1，矛盾。 -/
theorem zeta5_irrational : Irrational zeta5 := by
  rintro ⟨q, hq⟩
  set b := q.den with hb_def
  set a := q.num with ha_def
  have hb0 : 0 < b := q.pos
  have hb1 : 1 ≤ b := hb0
  have hab : ((a : ℚ) / (b : ℚ)) = q := Rat.num_div_den q
  have habR : ((a : ℝ) / (b : ℝ)) = zeta5 := by
    have hq' : ((q : ℚ) : ℝ) = zeta5 := hq
    rw [← hab] at hq'
    push_cast at hq'
    exact hq'
  -- 取充分大的 n
  obtain ⟨N₀, hN₀⟩ := Filter.eventually_atTop.1 theorem_2_1_decay_200
  obtain ⟨N₁, hN₁⟩ := exists_nat_gt ((185 / 139 : ℝ) * Real.log b)
  set n := max N₀ (max N₁ (max 1 200000)) with hn_def
  have hn0 : N₀ ≤ n := le_max_left _ _
  have hn1 : N₁ ≤ n := (le_max_left _ _).trans (le_max_right _ _)
  have hn1' : 200000 ≤ n := by
    rw [hn_def]
    exact (le_max_right 1 200000).trans ((le_max_right N₁ _).trans (le_max_right N₀ _))
  have hnN : 200 * 200 ^ 2 ≤ Kparam n := by
    calc 200 * 200 ^ 2 = 40 * 200000 := by norm_num
      _ ≤ 40 * n := Nat.mul_le_mul_left 40 hn1'
      _ = Kparam n := rfl
  have hn_pos : 0 < n := Nat.pos_of_ne_zero fun h => by
    have : 200000 ≤ 0 := hn1'.trans h.le
    norm_num at this
  -- Theorem 2.1（M = 200）
  have hT := theorem_2_1 200 (by norm_num) n hnN
  obtain ⟨P, hP⟩ := hT.1
  have hdegQ := hT.2.1
  have hposQ := hT.2.2
  -- 次数：deg P = 37n
  have hinj : Function.Injective (Int.castRingHom ℚ) := by
    intro x y h
    simp only [Int.coe_castRingHom] at h
    exact_mod_cast h
  have hdegP : P.natDegree = 37 * n := by
    have h1 : (P.map (Int.castRingHom ℚ)).natDegree = P.natDegree :=
      Polynomial.natDegree_map_eq_of_injective hinj P
    rw [← h1, hP, hdegQ]
    show 37 * n = 37 * n
    rfl
  -- 求值相容：P 在 ζ(5) 的值 = Q_{40n,200} 在 ζ(5) 的值
  have key : P.eval₂ (Int.castRingHom ℝ) zeta5
      = (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5 := by
    rw [← hP, eval₂_map_eq]
  -- 整性：z := b^{37n} · P(a/b) ∈ ℤ
  obtain ⟨z, hz⟩ := pow_mul_eval_int P a b (37 * n) hdegP.le hb0
  have hzR : (z : ℝ) = (b : ℝ) ^ (37 * n) * (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5 := by
    have h := congrArg (fun q : ℚ => (q : ℝ)) hz
    push_cast at h
    rw [eval₂_castRingHom_real] at h
    push_cast at h
    rw [h.symm, habR, key]
  -- 上界：b^{37n} · Q_n(ζ(5)) < 1
  have hbR : (0 : ℝ) < b := by exact_mod_cast hb0
  have hlog : Real.log b < 139 / 185 * (n : ℝ) := by
    have h1 : (185 / 139 : ℝ) * Real.log b < (n : ℝ) := hN₁.trans_le (by exact_mod_cast hn1)
    have h2 : Real.log b = (139 / 185 : ℝ) * ((185 / 139 : ℝ) * Real.log b) := by ring
    rw [h2]
    exact mul_lt_mul_of_pos_left h1 (by norm_num)
  have hnR : (0 : ℝ) < n := by exact_mod_cast hn_pos
  have hneg : 37 * (n : ℝ) * Real.log b - 139 / 5 * (n : ℝ) ^ 2 < 0 := by
    have hstep : 37 * (n : ℝ) * Real.log b < 139 / 5 * (n : ℝ) ^ 2 := by
      calc 37 * (n : ℝ) * Real.log b < 37 * (n : ℝ) * (139 / 185 * (n : ℝ)) :=
            mul_lt_mul_of_pos_left hlog (by positivity)
        _ = 139 / 5 * (n : ℝ) ^ 2 := by ring
    linarith
  have hexp : Real.exp (37 * (n : ℝ) * Real.log b - 139 / 5 * (n : ℝ) ^ 2) < 1 := by
    rw [show (1 : ℝ) = Real.exp 0 by rw [Real.exp_zero]]
    exact Real.exp_lt_exp.2 hneg
  have hupper : (b : ℝ) ^ (37 * n) * (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5 < 1 := by
    calc (b : ℝ) ^ (37 * n) * (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5
        = Real.exp (((37 * n : ℕ) : ℝ) * Real.log b) *
            (QKM n 200).eval₂ (algebraMap ℚ ℝ) zeta5 := by
          rw [Real.exp_nat_mul, Real.exp_log hbR]
      _ < Real.exp (((37 * n : ℕ) : ℝ) * Real.log b) * Real.exp (-(139 / 5 : ℝ) * (n : ℝ) ^ 2) :=
          mul_lt_mul_of_pos_left (hN₀ n hn0).2 (Real.exp_pos _)
      _ = Real.exp (37 * (n : ℝ) * Real.log b - 139 / 5 * (n : ℝ) ^ 2) := by
          rw [← Real.exp_add]
          congr 1
          push_cast
          ring
      _ < 1 := hexp
  -- 矛盾：0 < z < 1
  have hzpos : (0 : ℝ) < z := by rw [hzR]; positivity
  have hzlt : (z : ℝ) < 1 := by rw [hzR]; exact hupper
  have hz0 : 0 < z := by exact_mod_cast hzpos
  have hz1 : z < 1 := by exact_mod_cast hzlt
  omega

/-- 论文 Corollary 1.2（式 (1.1)）：存在 b₀ ∈ ℤ_{>0}，使对所有 a ∈ ℤ 与 b ∈ ℤ（b ≥ b₀）：
    |ζ(5) − a/b| > b^{−260}。证明：由 prop_C_2，对充分大的 b 与任意 a，
    0 < b^{37⌈c log b/40⌉} Q_{⌈c log b/40⌉,100000}(a/b) < 1（c = 75/4）；
    而由 theorem_2_1（整性 + 次数）与 `pow_mul_eval_int`，
    b^{37⌈c log b/40⌉} Q_{⌈c log b/40⌉,100000}(a/b) ∈ ℤ，矛盾。 -/
theorem corollary_1_2 : ∃ b₀ : ℤ, 0 < b₀ ∧ ∀ a : ℤ, ∀ b : ℤ, b₀ ≤ b →
    |zeta5 - (a : ℝ) / b| > (b : ℝ) ^ (-260 : ℤ) := by
  obtain ⟨B, hB⟩ := Filter.eventually_atTop.1 prop_C_2
  set c₀ : ℝ := (200 * 100000 ^ 2 : ℝ) * 4 / 75 with hc₀
  obtain ⟨B2, hB2⟩ := exists_nat_gt (Real.exp c₀)
  set bmax : ℕ := max B (max B2 2) with hbmax
  have hbmax2 : 2 ≤ bmax :=
    le_trans (le_max_right B2 2) (le_max_right B (max B2 2))
  refine ⟨(bmax : ℤ), by omega, fun a b hb => ?_⟩
  have hb2 : 2 ≤ b := by
    have h1 : (2 : ℤ) ≤ (bmax : ℤ) := by
      exact_mod_cast (le_trans (le_max_right B2 2) (le_max_right B (max B2 2)))
    omega
  set bp : ℕ := b.toNat with hbp
  have hbpz : (bp : ℤ) = b := Int.toNat_of_nonneg (by omega)
  have hbpB : B ≤ bp := by
    have h1 : (B : ℤ) ≤ b := le_trans (by
      exact_mod_cast (le_max_left B (max B2 2))) hb
    omega
  have hbpB2 : B2 ≤ bp := by
    have h1 : (B2 : ℤ) ≤ b := le_trans (by
      exact_mod_cast (le_trans (le_max_left B2 2) (le_max_right B (max B2 2)))) hb
    omega
  have hlog : c₀ ≤ Real.log bp := by
    have h1 : Real.exp c₀ < (bp : ℝ) := by
      have h2 : (Real.exp c₀ : ℝ) < (B2 : ℝ) := by exact_mod_cast hB2
      have h3 : (B2 : ℝ) ≤ (bp : ℝ) := by exact_mod_cast hbpB2
      linarith
    have h4 : Real.log (Real.exp c₀) ≤ Real.log bp :=
      Real.log_le_log (Real.exp_pos c₀) (le_of_lt h1)
    rwa [Real.log_exp] at h4
  obtain hBound := hB bp hbpB a
  set nb : ℕ := ⌈(75 / 4 : ℝ) * Real.log bp / 40⌉₊ with hnb
  have hnbK : 200 * 100000 ^ 2 ≤ Kparam nb := by
    have h1 : (75 / 4 : ℝ) * Real.log bp / 40 ≤ (nb : ℝ) := Nat.le_ceil _
    have h2 : (200 * 100000 ^ 2 : ℝ) ≤ (75 / 4 : ℝ) * Real.log bp := by
      have h3 : (200 * 100000 ^ 2 : ℝ) = (75 / 4) * c₀ := by
        rw [hc₀]
        ring
      rw [h3]
      exact mul_le_mul_of_nonneg_left hlog (by norm_num)
    have h5 : (75 / 4 : ℝ) * Real.log bp ≤ (40 : ℝ) * (nb : ℝ) := by
      have h1' : (40 : ℝ) * ((75 / 4 : ℝ) * Real.log bp / 40) ≤ (40 : ℝ) * (nb : ℝ) :=
        mul_le_mul_of_nonneg_left h1 (by norm_num)
      have e1 : (40 : ℝ) * ((75 / 4 : ℝ) * Real.log bp / 40) = (75 / 4 : ℝ) * Real.log bp := by ring
      rwa [e1] at h1'
    have h6 : (200 * 100000 ^ 2 : ℝ) ≤ (40 * nb : ℝ) := by
      calc (200 * 100000 ^ 2 : ℝ) ≤ (75 / 4 : ℝ) * Real.log bp := h2
        _ ≤ (40 : ℝ) * (nb : ℝ) := h5
    exact_mod_cast h6
  obtain ⟨hT1, hT2, _⟩ := theorem_2_1 100000 (by norm_num) nb hnbK
  obtain ⟨P, hPmap⟩ := hT1
  have hdegP : P.natDegree = 37 * nb := by
    have hinj : Function.Injective (Int.castRingHom ℚ) := by
      intro x y h
      simp only [Int.coe_castRingHom] at h
      exact_mod_cast h
    have h1 : (P.map (Int.castRingHom ℚ)).natDegree = P.natDegree :=
      Polynomial.natDegree_map_eq_of_injective hinj P
    rw [hPmap] at h1
    rw [← h1, hT2]
    rfl
  obtain ⟨z, hz⟩ := pow_mul_eval_int P a bp (37 * nb) hdegP.le (by omega)
  have hzR : (z : ℝ) = (bp : ℝ) ^ (37 * nb)
      * (QKM nb 100000).eval₂ (algebraMap ℚ ℝ) ((a : ℝ) / (bp : ℝ)) := by
    have hzR0 := congrArg (fun q : ℚ => (q : ℝ)) hz
    push_cast at hzR0
    rw [eval₂_castRingHom_real, ← eval₂_map_eq, hPmap] at hzR0
    push_cast at hzR0
    exact hzR0.symm
  have hzpos : (0 : ℝ) < z := by rw [hzR]; exact hBound.1
  have hzlt : (z : ℝ) < 1 := by rw [hzR]; exact hBound.2
  have hzpos' : (0 : ℤ) < z := by exact_mod_cast hzpos
  have hzlt' : z < 1 := by exact_mod_cast hzlt
  omega

/-- **Theorem 1.1（绝对版）**：ζ(5) 无理——经由 mo271/Zeta5 的完整形式化
    （Apache-2.0，其 `Apery.irrational_five` 无 sorry，公理仅
    propext/Classical.choice/Quot.sound）。我们的 `zeta5` 定义为 `(riemannZeta 5).re`，
    Apery.zeta5 定义为 ∑' 1/n⁵；桥接用 `Apery.riemannZeta_five`。 -/
theorem zeta5_irrational_absolute : Irrational zeta5 := by
  have hre : zeta5 = Apery.zeta5 := by
    rw [zeta5, Apery.riemannZeta_five]
    exact Complex.ofReal_re Apery.zeta5
  rw [hre]
  exact Apery.irrational_zeta5

end Zeta5Irrational
