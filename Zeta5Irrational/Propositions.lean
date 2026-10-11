import Mathlib
import Zeta5Irrational.Params
import Zeta5Irrational.Functional
import Zeta5Irrational.Numerics

/-!
# 中间结果陈述（论文 §2.3–§7 与 Appendix C）

所有定理按论文章节编号陈述；大部分证明为占位（sorry），对应论文相应章节。
式 (2.9) 的 `delta_leading_coeff`/`delta_natDegree` 已完整证明（见下方 PF_decomp 起
的一组私有引理）。
-/

namespace Zeta5Irrational

open scoped Polynomial

/-- ζ(5)（mathlib 的 `riemannZeta`，取实部；ζ(5) 为实数）。 -/
noncomputable def zeta5 : ℝ := (riemannZeta 5).re

/-- 有理函数在实点的求值（骨架用具：分子/分母分别求值）。 -/
noncomputable def RatFunc.evalReal (R : RatFunc ℚ) (x : ℝ) : ℝ :=
  Polynomial.eval x (R.num.map (algebraMap ℚ ℝ)) /
    Polynomial.eval x (R.denom.map (algebraMap ℚ ℝ))

/-- 权函数 w(y) = (2π)⁴y⁵/12 · ∑_{ℓ≥1} ℓ⁴ e^{−2πℓy}（论文式 (2.10)）。 -/
noncomputable def zetaWeight (y : ℝ) : ℝ :=
  (2 * Real.pi) ^ 4 / 12 * y ^ 5 * ∑' ℓ : ℕ, (ℓ : ℝ) ^ 4 * Real.exp (-2 * Real.pi * ℓ * y)

/-- μ_X 定义域内的有理函数：多项式部分加单极点部分（极点在 −j²，j ≥ 1）
    （论文 §2.1："rational functions with simple poles among the negative integer squares"）。 -/
def IsAdmissible (R : RatFunc ℚ) : Prop :=
  ∃ (P : ℚ[X]) (c : ℕ → ℚ) (s : Finset ℕ), (∀ j ∈ s, 0 < j) ∧
    R = (P : RatFunc ℚ) + ∑ j ∈ s, RatFunc.C (c j) * (RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹

/-- 有理函数沿仿射变换 x ↦ a x + b 的复合（骨架用具，论文式 (3.1)–(3.3) 的代换）。 -/
noncomputable def RatFunc.substAffine (g : RatFunc ℚ) (a b : ℚ) : RatFunc ℚ :=
  (g.num.comp (Polynomial.C a * Polynomial.X + Polynomial.C b) : RatFunc ℚ) /
    (g.denom.comp (Polynomial.C a * Polynomial.X + Polynomial.C b) : RatFunc ℚ)

/-! ## §2.3–§2.4：次数与正积分表示 -/

/-- μ 取值的计算部件（论文式 (2.9) 证明的组件，§2.3）。 -/

theorem muPole_eq (j : ℕ) : muPole j = Polynomial.C ((j : ℚ) ^ 4) * Polynomial.X
    - Polynomial.C ((j : ℚ) ^ 4 * harm5 j) + Polynomial.C (-(1 / 4 : ℚ) + 1 / (2 * j)) := by
  rw [muPole, mul_sub, ← Polynomial.C_mul]

theorem coeff_muPole_one (j : ℕ) : (muPole j).coeff 1 = (j : ℚ) ^ 4 := by
  rw [muPole_eq, Polynomial.coeff_add, Polynomial.coeff_sub, Polynomial.coeff_C_mul,
    Polynomial.coeff_X, Polynomial.coeff_C, Polynomial.coeff_C]
  simp

theorem natDegree_prod_fin_le (m : ℕ) (p : Fin m → ℚ[X]) (hp : ∀ i, (p i).natDegree ≤ 1) :
    (∏ i, p i).natDegree ≤ m := by
  induction m with
  | zero => simp

  | succ m ih =>
    rw [Fin.prod_univ_castSucc]
    exact Polynomial.natDegree_mul_le.trans (add_le_add (ih _ (fun i => hp i.castSucc)) (hp _))

theorem coeff_prod_fin (m : ℕ) (p : Fin m → ℚ[X]) (hp : ∀ i, (p i).natDegree ≤ 1) :
    (∏ i, p i).coeff m = ∏ i, (p i).coeff 1 := by
  induction m with
  | zero => rw [Fin.prod_univ_zero, Fin.prod_univ_zero]; simp
  | succ m ih =>
    rw [Fin.prod_univ_castSucc, Polynomial.coeff_mul, Fin.prod_univ_castSucc,
      Finset.sum_eq_single_of_mem (m, 1) (by simp [Finset.mem_antidiagonal])]
    · rw [ih _ (fun i => hp i.castSucc)]
    · intro p hp' hne
      obtain ⟨k, j⟩ := p
      simp at hp'
      have hk : (k, j) = (m, 1) ∨ m < k ∨ 1 < j := by
        rcases lt_trichotomy k m with h | h | h
        · right; right; omega
        · subst h
          rcases lt_trichotomy j 1 with h2 | h2 | h2
          · omega
          · left; exact Prod.ext rfl h2
          · right; right; omega
        · right; left; exact h
      rcases hk with heq | hk | hj
      · exfalso; exact hne heq
      · rw [Polynomial.coeff_eq_zero_of_natDegree_lt
          (lt_of_le_of_lt (natDegree_prod_fin_le m _ (fun i => hp i.castSucc)) hk), zero_mul]
      · rw [Polynomial.coeff_eq_zero_of_natDegree_lt (lt_of_le_of_lt (hp _) hj), mul_zero]

theorem coeff_muMonomial_one (e : ℕ) : (muMonomial e).coeff 1 = 0 := by
  simp [muMonomial]

theorem muX_poly_coeff_one (P : ℚ[X]) : (muX (P : RatFunc ℚ)).coeff 1 = 0 := by
  have hcoe : ⇑(algebraMap ℚ[X] (RatFunc ℚ)) = fun p : ℚ[X] => (p : RatFunc ℚ) :=
    funext fun p => rfl
  rw [P.as_sum_range]
  have hsum : ((∑ e ∈ Finset.range (P.natDegree + 1), Polynomial.monomial e (P.coeff e) : ℚ[X]) : RatFunc ℚ)
      = ∑ e ∈ Finset.range (P.natDegree + 1), RatFunc.C (P.coeff e) * RatFunc.X ^ e := by
    have h1 := congrFun hcoe
      (∑ e ∈ Finset.range (P.natDegree + 1), Polynomial.monomial e (P.coeff e))
    rw [← h1, map_sum]
    refine Finset.sum_congr rfl fun e _ => ?_
    rw [← Polynomial.C_mul_X_pow_eq_monomial, map_mul, map_pow, RatFunc.algebraMap_C, RatFunc.algebraMap_X]
  rw [hsum]
  show (muLin (∑ e ∈ Finset.range (P.natDegree + 1), RatFunc.C (P.coeff e) * RatFunc.X ^ e)).coeff 1 = 0
  rw [map_sum, Polynomial.finsetSum_coeff]
  refine Finset.sum_eq_zero fun e _ => ?_
  show (muX (RatFunc.C (P.coeff e) * RatFunc.X ^ e)).coeff 1 = 0
  rw [muX_spec.map_smul, Polynomial.coeff_C_mul, muX_monomial, coeff_muMonomial_one, mul_zero]


/-- D m 首一。 -/
private theorem D_monic (m : ℕ) : (D m).Monic := by
  rw [D]
  exact Polynomial.monic_prod_of_monic _ _ fun j _ => Polynomial.monic_X_add_C _

/-- D m 在 −r² 处的求值（积形式）。 -/
private theorem D_eval (m r : ℕ) : Polynomial.eval (-((r : ℚ) ^ 2)) (D m)
    = ∏ j ∈ Finset.Icc 1 m, (-((r : ℚ) ^ 2) + (j : ℚ) ^ 2) := by
  rw [D, Polynomial.eval_prod]
  refine Finset.prod_congr rfl fun j _ => ?_
  rw [Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C]

/-- D m 在自己的根 −r² 处为零。 -/
private theorem D_eval_self (m r : ℕ) (hr : r ∈ Finset.Icc 1 m) :
    Polynomial.eval (-((r : ℚ) ^ 2)) (D m) = 0 := by
  rw [D_eval, Finset.prod_eq_zero hr]
  simp

/-- 无重根因子的积在 −s² 处非零（s ∈ Icc 1 K，erase 积）。 -/
private theorem D_erase_prod_ne_zero {K s : ℕ} (hs : s ∈ Finset.Icc 1 K) :
    (∏ t ∈ (Finset.Icc 1 K).erase s, (-((s : ℚ) ^ 2) + (t : ℚ) ^ 2)) ≠ 0 := by
  apply Finset.prod_ne_zero_iff.2
  intro t ht
  have hts : t ≠ s := (Finset.mem_erase.1 ht).1
  have hts' : (t : ℚ) ^ 2 ≠ (s : ℚ) ^ 2 := by
    intro h
    have h2 : t ^ 2 = s ^ 2 := by exact_mod_cast h
    exact hts ((Nat.pow_left_inj (by norm_num : 2 ≠ 0)).1 h2)
  intro h0
  apply hts'
  linarith

/-- 互异常数的一次二项式互素。 -/
private theorem isCoprime_X_add_C_of_ne {a b : ℚ} (h : a ≠ b) :
    IsCoprime (Polynomial.X + Polynomial.C a) (Polynomial.X + Polynomial.C b) := by
  have hu : ((a - b)⁻¹ * (a - b) : ℚ) = 1 := inv_mul_cancel₀ (sub_ne_zero.2 h)
  have hcalc : Polynomial.C (a - b)⁻¹ * (Polynomial.X + Polynomial.C a)
      + Polynomial.C (-(a - b)⁻¹) * (Polynomial.X + Polynomial.C b)
      = Polynomial.C ((a - b)⁻¹ * (a - b)) := by
    rw [Polynomial.C_neg, Polynomial.C_mul, Polynomial.C_sub]
    ring
  refine ⟨Polynomial.C ((a - b)⁻¹), Polynomial.C (-(a - b)⁻¹), ?_⟩
  rw [hcalc, hu, Polynomial.C_1]

/-- 集合上的两两互素（_Icc 1 K 版本）。 -/
private theorem pairwise_coprime_D (K : ℕ) :
    Set.Pairwise (↑(Finset.Icc 1 K) : Set ℕ)
      (fun i j => IsCoprime (Polynomial.X + Polynomial.C ((i : ℚ) ^ 2))
        (Polynomial.X + Polynomial.C ((j : ℚ) ^ 2))) := by
  intro x hx y hy hxy
  exact isCoprime_X_add_C_of_ne (by
    intro h
    have h2 : x ^ 2 = y ^ 2 := by exact_mod_cast h
    exact hxy ((Nat.pow_left_inj (by norm_num : 2 ≠ 0)).1 h2))

/-- 部分分式分解（带显式系数公式）。 -/
private theorem PF_decomp (F : ℚ[X]) (K : ℕ) :
    ∃ q : ℚ[X], ∃ c : ℕ → ℚ,
      ((F : RatFunc ℚ) / (D K : RatFunc ℚ))
        = (((F / D K) + q : ℚ[X]) : RatFunc ℚ)
          + ∑ r ∈ Finset.Icc 1 K, RatFunc.C (c r) * (RatFunc.X + RatFunc.C ((r : ℚ) ^ 2))⁻¹
      ∧ ∀ s ∈ Finset.Icc 1 K,
        c s * (∏ t ∈ (Finset.Icc 1 K).erase s, (-((s : ℚ) ^ 2) + (t : ℚ) ^ 2))
          = Polynomial.eval (-((s : ℚ) ^ 2)) F := by
  classical
  haveI : FaithfulSMul ℚ[X] (RatFunc ℚ) :=
    (faithfulSMul_iff_algebraMap_injective _ _).mpr (RatFunc.algebraMap_injective ℚ)
  have hG0 : (D K : ℚ[X]) ≠ 0 := (D_monic K).ne_zero
  have hG0' : ((D K : ℚ[X]) : RatFunc ℚ) ≠ 0 := by
    simpa using (RatFunc.algebraMap_ne_zero hG0)
  have hdiv : F = D K * (F / D K) + F % D K :=
    (EuclideanDomain.div_add_mod F (D K)).symm
  obtain ⟨q, rval, hrval, hdec⟩ := Polynomial.div_prod_eq_quo_add_sum_rem_div (RatFunc ℚ) (F % D K)
    (s := Finset.Icc 1 K) (g := fun r : ℕ => Polynomial.X + Polynomial.C ((r : ℚ) ^ 2))
    (fun r _ => Polynomial.monic_X_add_C _) (pairwise_coprime_D K)
  have hdec' : ((F % D K : ℚ[X]) : RatFunc ℚ) / ((D K : ℚ[X]) : RatFunc ℚ)
      = ((q : ℚ[X]) : RatFunc ℚ)
        + ∑ r ∈ Finset.Icc 1 K, ((rval r : ℚ[X]) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((r : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) := by
    have e : ((D K : ℚ[X]) : RatFunc ℚ)
        = ∏ r ∈ Finset.Icc 1 K, ((Polynomial.X + Polynomial.C ((r : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) := by
      have e1 : (D K : ℚ[X]) = ∏ r ∈ Finset.Icc 1 K, (Polynomial.X + Polynomial.C ((r : ℚ) ^ 2)) := rfl
      rw [e1]
      simpa using map_prod (algebraMap ℚ[X] (RatFunc ℚ))
        (fun r => Polynomial.X + Polynomial.C ((r : ℚ) ^ 2)) (Finset.Icc 1 K)
    rw [e]
    exact hdec
  have hrvalC : ∀ r ∈ Finset.Icc 1 K, rval r = Polynomial.C ((rval r).coeff 0) := by
    intro r hr
    by_cases h0 : rval r = 0
    · rw [h0]; simp
    · have hd1 : (rval r).degree < 1 := by
        have h := hrval r hr
        rwa [Polynomial.degree_X_add_C] at h
      have hn : (rval r).natDegree < 1 := (Polynomial.natDegree_lt_iff_degree_lt h0).2 hd1
      have hn0 : (rval r).natDegree = 0 := Nat.lt_one_iff.1 hn
      obtain ⟨x, hx⟩ := Polynomial.natDegree_eq_zero.1 hn0
      rw [← hx]
      simp
  set c : ℕ → ℚ := fun r => if r ∈ Finset.Icc 1 K then (rval r).coeff 0 else 0 with hc
  have e5 : ∀ a : ℚ, ((Polynomial.C a : ℚ[X]) : RatFunc ℚ) = RatFunc.C a := fun a => by
    simpa using RatFunc.algebraMap_C (K := ℚ) a
  have e6 : ∀ b : ℚ, ((Polynomial.X + Polynomial.C b : ℚ[X]) : RatFunc ℚ)
      = RatFunc.X + RatFunc.C b := fun b => by
    have h3 := map_add (algebraMap ℚ[X] (RatFunc ℚ)) Polynomial.X (Polynomial.C b)
    rw [RatFunc.algebraMap_X, RatFunc.algebraMap_C] at h3
    simpa using h3
  refine ⟨q, c, ?_, ?_⟩
  · have hstep1 : ((F : RatFunc ℚ) / (D K : RatFunc ℚ))
        = ((F / D K : ℚ[X]) : RatFunc ℚ) + ((F % D K : ℚ[X]) : RatFunc ℚ) / (D K : RatFunc ℚ) := by
      calc ((F : RatFunc ℚ) / (D K : RatFunc ℚ))
          = ((D K * (F / D K) + F % D K : ℚ[X]) : RatFunc ℚ) / ((D K : ℚ[X]) : RatFunc ℚ) :=
            congrArg (fun x : RatFunc ℚ => x / ((D K : ℚ[X]) : RatFunc ℚ))
              (by simpa using congrArg (fun p : ℚ[X] => (p : RatFunc ℚ)) hdiv)
        _ = (((D K * (F / D K) : ℚ[X]) : RatFunc ℚ) + ((F % D K : ℚ[X]) : RatFunc ℚ))
            / ((D K : ℚ[X]) : RatFunc ℚ) := by
            have hm := map_add (algebraMap ℚ[X] (RatFunc ℚ)) (D K * (F / D K)) (F % D K)
            simpa using congrArg (· / ((D K : ℚ[X]) : RatFunc ℚ)) hm
        _ = ((D K * (F / D K) : ℚ[X]) : RatFunc ℚ) / ((D K : ℚ[X]) : RatFunc ℚ)
            + ((F % D K : ℚ[X]) : RatFunc ℚ) / ((D K : ℚ[X]) : RatFunc ℚ) := add_div _ _ _
        _ = ((F / D K : ℚ[X]) : RatFunc ℚ) + ((F % D K : ℚ[X]) : RatFunc ℚ) / ((D K : ℚ[X]) : RatFunc ℚ) := by
            congr 1
            have e3 : ((D K * (F / D K) : ℚ[X]) : RatFunc ℚ)
                = ((D K : ℚ[X]) : RatFunc ℚ) * ((F / D K : ℚ[X]) : RatFunc ℚ) := by
              simpa using map_mul (algebraMap ℚ[X] (RatFunc ℚ)) (D K) (F / D K)
            rw [e3, mul_div_cancel_left₀ _ hG0']
    rw [hstep1, hdec', ← add_assoc]
    congr 1
    · have hm := map_add (algebraMap ℚ[X] (RatFunc ℚ)) (F / D K) q
      simpa using hm.symm
    · refine Finset.sum_congr rfl fun r hr => ?_
      rw [hrvalC r hr, show c r = (rval r).coeff 0 from dif_pos hr, div_eq_mul_inv, e5, e6]
  · intro s hs
    have he' : ∀ r ∈ Finset.Icc 1 K, ⇑(algebraMap ℚ[X] (RatFunc ℚ)) (D K)
        = ⇑(algebraMap ℚ[X] (RatFunc ℚ)) (Polynomial.X + Polynomial.C ((r : ℚ) ^ 2))
          * ⇑(algebraMap ℚ[X] (RatFunc ℚ))
            (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) := by
      intro r hr
      rw [show D K = (Polynomial.X + Polynomial.C ((r : ℚ) ^ 2))
          * (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2)))
        from by rw [show D K = ∏ x ∈ Finset.Icc 1 K, (Polynomial.X + Polynomial.C ((x : ℚ) ^ 2)) from rfl,
          ← Finset.prod_erase_mul _ _ hr, mul_comm], map_mul]
    have hQ : (F % D K : ℚ[X]) = q * D K + ∑ r ∈ Finset.Icc 1 K,
        Polynomial.C (c r) * (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) := by
      apply (FaithfulSMul.algebraMap_injective ℚ[X] (RatFunc ℚ))
      have hmul := congrArg (fun x : RatFunc ℚ => x * ((D K : ℚ[X]) : RatFunc ℚ)) hdec'
      rw [div_mul_cancel₀ _ hG0'] at hmul
      rw [add_mul, Finset.sum_mul] at hmul
      have hmul2 : ((F % D K : ℚ[X]) : RatFunc ℚ)
          = ((q : ℚ[X]) : RatFunc ℚ) * ((D K : ℚ[X]) : RatFunc ℚ)
            + ∑ r ∈ Finset.Icc 1 K, ((Polynomial.C (c r)
                * (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) : ℚ[X]) : RatFunc ℚ) := by
        rw [hmul]
        congr 1
        refine Finset.sum_congr rfl fun r hr => ?_
        have e4 : ((Polynomial.C (c r)
              * (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) : ℚ[X]) : RatFunc ℚ)
            = ((rval r : ℚ[X]) : RatFunc ℚ)
              / ((Polynomial.X + Polynomial.C ((r : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ)
              * ((D K : ℚ[X]) : RatFunc ℚ) := by
          have hy : ((Polynomial.X + Polynomial.C ((r : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) ≠ 0 :=
            RatFunc.algebraMap_ne_zero (Polynomial.X_add_C_ne_zero _)
          have he'' : ((D K : ℚ[X]) : RatFunc ℚ)
              = ((Polynomial.X + Polynomial.C ((r : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ)
                * ((∏ t ∈ (Finset.Icc 1 K).erase r,
                    (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2)) : ℚ[X]) : RatFunc ℚ) :=
            he' r hr
          have e7 : ((Polynomial.C ((rval r).coeff 0)
                * (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) : ℚ[X]) : RatFunc ℚ)
              = RatFunc.C ((rval r).coeff 0)
                * ((∏ t ∈ (Finset.Icc 1 K).erase r,
                    (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2)) : ℚ[X]) : RatFunc ℚ) := by
            simpa using map_mul (algebraMap ℚ[X] (RatFunc ℚ)) _ _
          rw [he'', hrvalC r hr, show c r = (rval r).coeff 0 from dif_pos hr, div_eq_mul_inv, e5, e7,
            mul_assoc, inv_mul_cancel_left₀ hy]
        rw [e4]
      rw [map_add, map_mul, map_sum]
      simpa using hmul2
    have hval := congrArg (Polynomial.eval (-((s : ℚ) ^ 2))) hQ
    rw [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_finsetSum, D_eval_self _ _ hs,
      mul_zero, zero_add] at hval
    have hvalL : Polynomial.eval (-((s : ℚ) ^ 2)) (F % D K) = Polynomial.eval (-((s : ℚ) ^ 2)) F := by
      have hv := congrArg (Polynomial.eval (-((s : ℚ) ^ 2))) hdiv
      rw [Polynomial.eval_add, Polynomial.eval_mul, D_eval_self _ _ hs, zero_mul, zero_add] at hv
      exact hv.symm
    rw [hvalL] at hval
    rw [Finset.sum_eq_single s (fun r hr hrs => by
      have hsv : Polynomial.eval (-((s : ℚ) ^ 2))
          (∏ t ∈ (Finset.Icc 1 K).erase r, (Polynomial.X + Polynomial.C ((t : ℚ) ^ 2))) = 0 := by
        rw [Polynomial.eval_prod]
        exact Finset.prod_eq_zero (Finset.mem_erase.2 ⟨hrs.symm, hs⟩) (by simp)
      rw [Polynomial.eval_mul, Polynomial.eval_C, hsv, mul_zero]) (fun habs => (habs hs).elim)] at hval
    rw [Polynomial.eval_mul, Polynomial.eval_prod] at hval
    simp only [Polynomial.eval_C, Polynomial.eval_add, Polynomial.eval_X] at hval
    exact hval.symm

/-- μ 对有限和的线性性。 -/
private theorem muX_sum : ∀ (s : Finset ℕ) (f : ℕ → RatFunc ℚ),
    muX (∑ r ∈ s, f r) = ∑ r ∈ s, muX (f r) := by
  intro s f
  refine Finset.induction_on s ?_ fun a s ha ih => ?_
  · simp [muX_spec.map_zero]
  · rw [Finset.sum_insert ha, Finset.sum_insert ha, muX_spec.map_add, ih]

/-- Gentry 项的部分分式展开（PF_decomp 的装配）。 -/
private theorem Gentry_decomp (n i j : ℕ) :
    ∃ q : ℚ[X], ∃ c : ℕ → ℚ,
      (Gentry n i j : ℚ[X])
        = muX (((D (Nparam n)) ^ 6 * Polynomial.X ^ (i + j) / D (Kparam n)
            + q : ℚ[X]) : RatFunc ℚ)
          + ∑ r ∈ Finset.Icc 1 (Kparam n),
            muX (RatFunc.C (c r) * (RatFunc.X + RatFunc.C ((r : ℚ) ^ 2))⁻¹)
        ∧ ∀ s ∈ Finset.Icc 1 (Kparam n),
          c s * ∏ t ∈ (Finset.Icc 1 (Kparam n)).erase s,
              (-((s : ℚ) ^ 2) + (t : ℚ) ^ 2)
            = Polynomial.eval (-((s : ℚ) ^ 2)) ((D (Nparam n)) ^ 6 * Polynomial.X ^ (i + j)) := by
  obtain ⟨q, c, hdec, hc⟩ := PF_decomp ((D (Nparam n)) ^ 6 * Polynomial.X ^ (i + j)) (Kparam n)
  refine ⟨q, c, ?_, hc⟩
  rw [Gentry]
  have hnum : ((D (Nparam n) : RatFunc ℚ) ^ 6 * RatFunc.X ^ (i + j))
      = (((D (Nparam n)) ^ 6 * Polynomial.X ^ (i + j) : ℚ[X]) : RatFunc ℚ) := by
    simp [map_mul, map_pow, RatFunc.algebraMap_X]
  rw [hnum, hdec, muX_spec.map_add, muX_sum]

/-- Gentry 项的 [X] 系数（显式求和形式）。 -/
private theorem Gentry_coeff_one (n i j : ℕ) (hn : 0 < n) :
    (Gentry n i j).coeff 1
      = ∑ r ∈ Finset.Icc (Nparam n + 1) (Kparam n),
          (Polynomial.eval (-((r : ℚ) ^ 2)) (D (Nparam n))) ^ 6
            * (-((r : ℚ) ^ 2)) ^ (i + j)
            / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase r, (-((r : ℚ) ^ 2) + (t : ℚ) ^ 2))
            * (r : ℚ) ^ 4 := by
  classical
  have hN1 : 1 ≤ Nparam n := by dsimp [Nparam]; omega
  obtain ⟨q, c, hG, hc⟩ := Gentry_decomp n i j
  have hcoeff1 : (Gentry n i j).coeff 1
      = ∑ r ∈ Finset.Icc 1 (Kparam n), c r * (r : ℚ) ^ 4 := by
    rw [hG, Polynomial.coeff_add, muX_poly_coeff_one, zero_add, Polynomial.finsetSum_coeff]
    refine Finset.sum_congr rfl fun r hr => ?_
    rw [muX_spec.map_smul, muX_pole, Polynomial.coeff_C_mul, coeff_muPole_one]
  have hev : ∀ r : ℕ, Polynomial.eval (-((r : ℚ) ^ 2))
        ((D (Nparam n)) ^ 6 * Polynomial.X ^ (i + j))
      = (Polynomial.eval (-((r : ℚ) ^ 2)) (D (Nparam n))) ^ 6 * (-((r : ℚ) ^ 2)) ^ (i + j) := by
    intro r
    simp
  have hcr : ∀ r ∈ Finset.Icc 1 (Kparam n), c r
      = (Polynomial.eval (-((r : ℚ) ^ 2)) (D (Nparam n))) ^ 6 * (-((r : ℚ) ^ 2)) ^ (i + j)
        / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase r, (-((r : ℚ) ^ 2) + (t : ℚ) ^ 2)) := by
    intro r hr
    rw [eq_div_iff (D_erase_prod_ne_zero hr), ← hev]
    exact hc r hr
  have hsub : Finset.Icc (Nparam n + 1) (Kparam n) ⊆ Finset.Icc 1 (Kparam n) := by
    intro x hx
    have h := Finset.mem_Icc.1 hx
    exact Finset.mem_Icc.2 ⟨by omega, h.2⟩
  have hvani : ∀ x ∈ Finset.Icc 1 (Kparam n), x ∉ Finset.Icc (Nparam n + 1) (Kparam n) →
      c x * (x : ℚ) ^ 4 = 0 := by
    intro x hx hxn
    have hxi := Finset.mem_Icc.1 hx
    have hxN : x ≤ Nparam n := by
      by_contra hc
      push_neg at hc
      exact hxn (Finset.mem_Icc.2 ⟨Nat.succ_le_iff.2 hc, hxi.2⟩)
    have hx1N : x ∈ Finset.Icc 1 (Nparam n) := Finset.mem_Icc.2 ⟨hxi.1, hxN⟩
    have he := hc x hx
    rw [hev, D_eval_self _ _ hx1N, zero_pow (by norm_num : (6 : ℕ) ≠ 0), zero_mul] at he
    rw [(mul_eq_zero.1 he).resolve_right (D_erase_prod_ne_zero hx), zero_mul]
  rw [hcoeff1, ← Finset.sum_subset hsub hvani]
  refine Finset.sum_congr rfl fun r hr => ?_
  have hr1 : r ∈ Finset.Icc 1 (Kparam n) := by
    have h := Finset.mem_Icc.1 hr
    exact Finset.mem_Icc.2 ⟨by omega, h.2⟩
  rw [hcr r hr1]

/-- μ 作用于多项式（经 coe 提升到 RatFunc）的次数 ≤ 0（值为常数）。 -/
private theorem muX_poly_natDegree_le (P : ℚ[X]) : (muX (P : RatFunc ℚ)).natDegree ≤ 0 := by
  have hcoe : ⇑(algebraMap ℚ[X] (RatFunc ℚ)) = fun p : ℚ[X] => (p : RatFunc ℚ) := funext fun p => rfl
  rw [P.as_sum_range]
  have hsum : ((∑ e ∈ Finset.range (P.natDegree + 1), Polynomial.monomial e (P.coeff e) : ℚ[X]) : RatFunc ℚ)
      = ∑ e ∈ Finset.range (P.natDegree + 1), RatFunc.C (P.coeff e) * RatFunc.X ^ e := by
    have h1 := congrFun hcoe
      (∑ e ∈ Finset.range (P.natDegree + 1), Polynomial.monomial e (P.coeff e))
    rw [← h1, map_sum]
    refine Finset.sum_congr rfl fun e _ => ?_
    rw [← Polynomial.C_mul_X_pow_eq_monomial, map_mul, map_pow, RatFunc.algebraMap_C, RatFunc.algebraMap_X]
  rw [hsum, muX_sum]
  have hstep : ∀ e : ℕ, muX (RatFunc.C (P.coeff e) * RatFunc.X ^ e)
      = Polynomial.C (P.coeff e * (((-1 : ℚ) ^ e) * (bernoulli (2 * e + 2)) * (2 * e + 3)
          * (2 * e + 4) * (2 * e + 5) / 24)) := fun e => by
    rw [muX_spec.map_smul, muX_monomial, muMonomial, Polynomial.C_mul]
  rw [Finset.sum_congr rfl fun e _ => hstep e]
  have key : ∀ (s : Finset ℕ) (g : ℕ → ℚ), (∑ e ∈ s, Polynomial.C (g e)).natDegree ≤ 0 := by
    intro s g
    induction s using Finset.induction with
    | empty => simp
    | insert a s ha ih =>
      rw [Finset.sum_insert ha]
      exact (Polynomial.natDegree_add_le _ _).trans
        (max_le (by rw [Polynomial.natDegree_C]) ih)
  exact key _ _

/-- μ_Pole 的次数 ≤ 1。 -/
private theorem muPole_natDegree_le (j : ℕ) : (muPole j).natDegree ≤ 1 := by
  rw [muPole_eq]
  have e1 : (Polynomial.C ((j : ℚ) ^ 4) * Polynomial.X).natDegree ≤ 1 :=
    Polynomial.natDegree_mul_le.trans
      (add_le_add (le_of_eq (Polynomial.natDegree_C _))
        (le_of_eq Polynomial.natDegree_X))
  have e2 : (Polynomial.C ((j : ℚ) ^ 4 * harm5 j)).natDegree ≤ 1 :=
    (le_of_eq (Polynomial.natDegree_C _)).trans zero_le_one
  have e3 : (Polynomial.C (-(1 / 4 : ℚ) + 1 / (2 * j))).natDegree ≤ 1 :=
    (le_of_eq (Polynomial.natDegree_C _)).trans zero_le_one
  have hsub : (Polynomial.C ((j : ℚ) ^ 4) * Polynomial.X
      - Polynomial.C ((j : ℚ) ^ 4 * harm5 j)).natDegree ≤ 1 :=
    (Polynomial.natDegree_sub_le _ _).trans (max_le e1 e2)
  exact (Polynomial.natDegree_add_le _ _).trans (max_le hsub e3)

/-- Gentry 项的次数 ≤ 1。 -/
private theorem Gentry_natDegree_le (n i j : ℕ) : (Gentry n i j).natDegree ≤ 1 := by
  obtain ⟨q, c, hG, _⟩ := Gentry_decomp n i j
  rw [hG]
  have key : ∀ (s : Finset ℕ) (g : ℕ → ℚ[X]), (∀ e, (g e).natDegree ≤ 1) →
      (∑ e ∈ s, g e).natDegree ≤ 1 := by
    intro s g hg
    induction s using Finset.induction with
    | empty => simp
    | insert a s ha ih =>
      rw [Finset.sum_insert ha]
      exact (Polynomial.natDegree_add_le _ _).trans (max_le (hg a) ih)
  have hg : ∀ r : ℕ, (muX (RatFunc.C (c r) * (RatFunc.X + RatFunc.C ((r : ℚ) ^ 2))⁻¹)).natDegree ≤ 1 := by
    intro r
    rw [muX_spec.map_smul, muX_pole]
    exact Polynomial.natDegree_mul_le.trans
      (add_le_add (le_of_eq (Polynomial.natDegree_C _)) (muPole_natDegree_le r))
  exact (Polynomial.natDegree_add_le _ _).trans (max_le
    ((muX_poly_natDegree_le _).trans (by norm_num))
    (key _ _ hg))

/-- det B ≠ 0：B 是 Vandermonde 加对角因子的分解。 -/
private theorem det_B_ne_zero (n : ℕ) (hn : 0 < n) :
    Matrix.det (Matrix.of fun i j : Fin (hparam n) => (Gentry n i j).coeff 1) ≠ 0 := by
  classical
  have hN : Nparam n + hparam n = Kparam n := by dsimp [Nparam, hparam, Kparam]; omega
  have hrin : ∀ k : Fin (hparam n), Nparam n + 1 + k.1 ∈ Finset.Icc 1 (Kparam n) := by
    intro k
    exact Finset.mem_Icc.2 ⟨by omega, by have := k.2; omega⟩
  set v : Fin (hparam n) → ℚ := fun k => (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) with hv
  set w : Fin (hparam n) → ℚ := fun k =>
    ((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 4
      * (Polynomial.eval (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
      / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + k.1),
          (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2))) with hw
  have hB : (Matrix.of fun i j : Fin (hparam n) => (Gentry n i j).coeff 1)
      = Matrix.transpose (Matrix.vandermonde v)
        * (Matrix.diagonal w * Matrix.transpose (Matrix.transpose (Matrix.vandermonde v))) := by
    ext i j
    simp only [Matrix.of_apply, hv, hw]
    rw [Gentry_coeff_one n i j hn]
    have key : ∀ i j : Fin (hparam n),
        (∑ r ∈ Finset.Icc (Nparam n + 1) (Kparam n),
          (Polynomial.eval (-((r : ℚ) ^ 2)) (D (Nparam n))) ^ 6
            * (-((r : ℚ) ^ 2)) ^ (i.1 + j.1)
            / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase r, (-((r : ℚ) ^ 2) + (t : ℚ) ^ 2))
            * (r : ℚ) ^ 4)
        = ∑ x ∈ Finset.range (hparam n),
          (Polynomial.eval (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
            * (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2)) ^ (i.1 + j.1)
            / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + x),
                (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2))
            * ((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 4) := by
      intro i j
      have h2 : (Finset.Icc (Nparam n + 1) (Kparam n))
          = (Finset.range (hparam n)).image (fun x => Nparam n + 1 + x) := by
        ext y
        simp only [Finset.mem_Icc, Finset.mem_image, Finset.mem_range]
        constructor
        · rintro ⟨h1, h2⟩
          exact ⟨y - (Nparam n + 1), by omega, by omega⟩
        · rintro ⟨x, hx, rfl⟩
          exact ⟨by omega, by omega⟩
      rw [h2, Finset.sum_image (fun x _ y _ h => by omega)]
    rw [key i j, ← Fin.sum_univ_eq_sum_range (fun x =>
      (Polynomial.eval (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
        * (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2)) ^ (i.1 + j.1)
        / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + x),
            (-((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2))
        * ((((Nparam n + 1 + x : ℕ) : ℚ)) ^ 4)) (hparam n)]
    rw [Matrix.mul_apply]
    simp only [Matrix.diagonal_mul]
    simp only [Matrix.transpose_transpose, Matrix.transpose, Matrix.vandermonde,
      Matrix.of_apply]
    refine Finset.sum_congr rfl fun k _ => ?_
    show ((Polynomial.eval (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
          * (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) ^ (i.1 + j.1)
          / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + k.1),
              (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2)))
        * ((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 4)
      = (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) ^ i.1
        * ((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 4
            * (Polynomial.eval (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
            / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + k.1),
                (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2))
          * (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) ^ j.1)
    ring
  rw [hB, Matrix.det_mul, Matrix.det_mul]
  simp only [Matrix.det_transpose, Matrix.det_diagonal]
  have hinj : Function.Injective (fun k : Fin (hparam n) =>
      (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2))) := by
    intro a b h
    have h1 : (((Nparam n + 1 + a.1 : ℕ) : ℚ)) ^ 2 = (((Nparam n + 1 + b.1 : ℕ) : ℚ)) ^ 2 :=
      neg_inj.1 h
    have h2 : (Nparam n + 1 + a.1) ^ 2 = (Nparam n + 1 + b.1) ^ 2 := by exact_mod_cast h1
    have h3 := (Nat.pow_left_inj (by norm_num : 2 ≠ 0)).1 h2
    have h4 : a.1 = b.1 := by omega
    exact Fin.ext h4
  have hwne : ∀ k : Fin (hparam n),
      ((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 4
        * (Polynomial.eval (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) (D (Nparam n))) ^ 6
        / (∏ t ∈ (Finset.Icc 1 (Kparam n)).erase (Nparam n + 1 + k.1),
            (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2) + (t : ℚ) ^ 2))) ≠ 0 := by
    intro k
    have hc0 : (((Nparam n + 1 + k.1 : ℕ) : ℚ)) ≠ 0 := by
      norm_cast
      omega
    have he0 : Polynomial.eval (-((((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2)) (D (Nparam n)) ≠ 0 := by
      rw [D_eval]
      apply Finset.prod_ne_zero_iff.2
      intro j hj
      have hj' := Finset.mem_Icc.1 hj
      intro h0
      have h1 : ((j : ℚ)) ^ 2 = (((Nparam n + 1 + k.1 : ℕ) : ℚ)) ^ 2 := by linarith
      have h2 : j ^ 2 = (Nparam n + 1 + k.1) ^ 2 := by exact_mod_cast h1
      have h3 := (Nat.pow_left_inj (by norm_num : 2 ≠ 0)).1 h2
      omega
    exact div_ne_zero (mul_ne_zero (pow_ne_zero 4 hc0) (pow_ne_zero 6 he0))
      (D_erase_prod_ne_zero (hrin k))
  apply mul_ne_zero
  · rw [Matrix.det_vandermonde_ne_zero_iff]; exact hinj
  apply mul_ne_zero
  · exact Finset.prod_ne_zero_iff.2 fun k _ => hwne k
  · rw [Matrix.det_vandermonde_ne_zero_iff]; exact hinj

/-- Δ_K 的首项系数 = det B。 -/
private theorem deltaK_coeff_eq_det (n : ℕ) (hn : 0 < n) :
    (deltaK n).coeff (hparam n)
      = Matrix.det (Matrix.of fun i j : Fin (hparam n) => (Gentry n i j).coeff 1) := by
  rw [deltaK, Matrix.det_apply, Matrix.det_apply, Polynomial.finsetSum_coeff]
  simp only [Matrix.of_apply]
  refine Finset.sum_congr rfl fun σ _ => ?_
  rw [Polynomial.coeff_smul, coeff_prod_fin (hparam n) (fun i => Gentry n (σ i) i)
    (fun i => Gentry_natDegree_le n (σ i) i)]

/-- Δ_K 的次数 ≤ h。 -/
private theorem deltaK_natDegree_le (n : ℕ) : (deltaK n).natDegree ≤ hparam n := by
  rw [deltaK, Matrix.det_apply]
  simp only [Matrix.of_apply]
  have key : ∀ (s : Finset (Equiv.Perm (Fin (hparam n))))
      (g : Equiv.Perm (Fin (hparam n)) → ℚ[X]),
      (∀ σ, (g σ).natDegree ≤ hparam n) → (∑ σ ∈ s, g σ).natDegree ≤ hparam n := by
    intro s g hg
    induction s using Finset.induction with
    | empty => simp
    | insert a s ha ih =>
      rw [Finset.sum_insert ha]
      exact (Polynomial.natDegree_add_le _ _).trans (max_le (hg a) ih)
  refine key _ _ fun σ => ?_
  exact (Polynomial.natDegree_smul_le _ _).trans
    (natDegree_prod_fin_le (hparam n) (fun i => Gentry n (σ i) i)
      (fun i => Gentry_natDegree_le n (σ i) i))

/-- 论文式 (2.9)：Δ_K 的 X^h 系数非零（首项）。
    证明路线（§2.3，组件见上方 `muPole_eq`/`coeff_muPole_one`/`muX_poly_coeff_one`/
    `natDegree_prod_fin_le`/`coeff_prod_fin` 与下方 `PF_decomp`/`Gentry_decomp`/
    `Gentry_coeff_one`/`Gentry_natDegree_le`/`det_B_ne_zero`）：
    1. 部分分式：F := D_N⁶X^{i+j} = G·(F/G) + F%G（G = D_K 首一），
       `Polynomial.div_prod_eq_quo_add_sum_rem_div` 给出 (F%G)/G = q + ∑_r C c_r/(X + r²)；
    2. 两边乘 G 代入 t = −r²（c_r 之外的项消失）得 c_r = F(−r²)/∏_{s≠r}(s²−r²)
       = D_N(−r²)⁶(−r²)^{i+j}/∏_{s≠r}(s²−r²)（r ≤ N 时为 0）；
    3. μ 线性展开：`muX_poly_coeff_one`（多项式部分贡献常数）+
       `muX_spec.map_smul` + `coeff_muPole_one` 得 [X](Gentry n i j) = B_{ij}；
    4. `Matrix.det_apply` + `coeff_prod_fin` 得 (Δ_K).coeff h = det B；
    5. B = Vᵀ ⬝ (D ⬝ (Vᵀ)ᵀ)（Vandermonde，节点 −r²，r ∈ Icc (N+1) K，共 h 个），
       `Matrix.det_vandermonde` + `Matrix.det_diagonal` 得 det B ≠ 0。 -/
theorem delta_leading_coeff (n : ℕ) (hn : 0 < n) : (deltaK n).coeff (hparam n) ≠ 0 := by
  rw [deltaK_coeff_eq_det n hn]; exact det_B_ne_zero n hn

/-- 论文式 (2.9) 推论：deg Δ_K = h。
    由 `delta_leading_coeff`（coeff h ≠ 0）与上界：
    `Matrix.det_apply` 展开后每项为 h 个一次多项式之积，`natDegree_prod_fin_le`
    给 deg ≤ h；`Polynomial.le_natDegree_of_ne_zero` 给出等式。 -/
theorem delta_natDegree (n : ℕ) (hn : 0 < n) : (deltaK n).natDegree = hparam n :=
  le_antisymm (deltaK_natDegree_le n)
    (Polynomial.le_natDegree_of_ne_zero (delta_leading_coeff n hn))

/-- 论文 Proposition 2.2（§2.4，式 (2.10)）：正积分表示
    μ_{ζ(5)}(R) = ∫₀^∞ R(y²) w(y) dy。 -/
theorem prop_2_2 (R : RatFunc ℚ) (hR : IsAdmissible R)
    (hint : MeasureTheory.IntegrableOn (fun y => RatFunc.evalReal R (y ^ 2) * zetaWeight y)
      (Set.Ioi 0)) :
    (muX R).eval₂ (algebraMap ℚ ℝ) zeta5
      = ∫ y in Set.Ioi 0, RatFunc.evalReal R (y ^ 2) * zetaWeight y := sorry

/-- 论文 Proposition 2.2 末段：G_K(ζ(5)) 正定。 -/
theorem prop_2_2_posdef (n : ℕ) (hn : 0 < n) :
    Matrix.PosDef (Matrix.of fun i j : Fin (hparam n) =>
      (Gentry n i j).eval₂ (algebraMap ℚ ℝ) zeta5) := sorry

/-! ## §3：局部有理泛函 -/

/-- 论文式 (3.1) 与 §2.1 末段：μ_X 由多项式除法与部分分式唯一延拓——
    μ 在可接受函数上的值由其多项式部分与单极点部分决定。 -/
theorem eq_3_1 (R : RatFunc ℚ) (hR : IsAdmissible R) :
    ∃ (P : ℚ[X]) (c : ℕ → ℚ) (s : Finset ℕ), (∀ j ∈ s, 0 < j) ∧
      R = (P : RatFunc ℚ) + ∑ j ∈ s, RatFunc.C (c j) * (RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹ ∧
      muX R = muX (P : RatFunc ℚ) +
        ∑ j ∈ s, Polynomial.C (c j) * muX ((RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹) := by
  obtain ⟨P, c, s, hs, hR'⟩ := hR
  refine ⟨P, c, s, hs, hR', ?_⟩
  rw [hR']
  rw [muX_spec.map_add]
  congr 1
  clear hs hR'
  induction s using Finset.induction_on with
  | empty => simp only [Finset.sum_empty, muX_spec.map_zero]
  | insert a s' has ih =>
      rw [Finset.sum_insert has, Finset.sum_insert has, muX_spec.map_add, ih]
      congr 1
      exact muX_spec.map_smul _ _

/-- 原论文式 (3.3) 的移植版对有理函数**不成立**，反例 g = RatFunc.X：
    g(x+1) − g(x) = 1，μ_X(1) = muMonomial 0 = C(5/12) ≠ 0 = C(g⁽⁴⁾(0)/24)。
    原因：论文 (3.2)/(3.3) 属于 τ-泛函（x-世界，整数极点），骨架的 μ 生活在
    t-世界（极点在负整数平方）；两个恒等式已重述为多项式版 `eq_3_2_poly`/`eq_3_3_poly`。 -/
theorem eq_3_3_false :
    muX (RatFunc.substAffine RatFunc.X 1 1 - RatFunc.X) ≠
      Polynomial.C ((Polynomial.derivative^[4] (RatFunc.X : RatFunc ℚ).num).eval 0 / 24) := by
  have coe_poly_one : ((1 : ℚ[X]) : RatFunc ℚ) = 1 := map_one _
  rw [RatFunc.substAffine, RatFunc.num_X, RatFunc.denom_X, Polynomial.X_comp, Polynomial.one_comp,
    coe_poly_one, div_one,
    show (Polynomial.C (1 : ℚ) * Polynomial.X + Polynomial.C 1) = (Polynomial.X + 1 : ℚ[X]) by
      rw [Polynomial.C_1, one_mul],
    ← RatFunc.algebraMap_X]
  show muX ((algebraMap ℚ[X] (RatFunc ℚ)) (Polynomial.X + 1)
      - (algebraMap ℚ[X] (RatFunc ℚ)) Polynomial.X) ≠ _
  rw [← map_sub (algebraMap ℚ[X] (RatFunc ℚ)),
    show (Polynomial.X + 1 - Polynomial.X : ℚ[X]) = 1 by ring, map_one,
    show (1 : RatFunc ℚ) = RatFunc.X ^ 0 by simp, muX_monomial]
  norm_num [muMonomial, bernoulli]

/-- 论文式 (3.2) 的多项式版：μ_X(P(−1−X)) = −μ_X(P)。
    原陈述（对任意有理函数 g）不成立——域不匹配，见 `eq_3_3_false`。
    证明是 Bernoulli 反射恒等式（生成函数），超出骨架范围，sorry。 -/
theorem eq_3_2_poly (P : ℚ[X]) :
    muX (RatFunc.substAffine (P : RatFunc ℚ) (-1) (-1)) = - muX (P : RatFunc ℚ) := sorry

/-- 论文式 (3.3) 的多项式版：μ_X(P(X+1) − P(X)) = C(P⁽⁴⁾(0)/24)。
    即 Bernoulli 差分恒等式 ∑ₖ C(e,k)(−1)^k B_{2k+2}(2k+3)(2k+4)(2k+5)/24 = δ_{e≥4}·C(e,4)
    （生成函数证明），超出骨架范围，sorry；原陈述见 `eq_3_3_false`。 -/
theorem eq_3_3_poly (P : ℚ[X]) :
    muX (RatFunc.substAffine (P : RatFunc ℚ) 1 1 - (P : RatFunc ℚ)) =
      Polynomial.C ((Polynomial.derivative^[4] P).eval 0 / 24) := sorry

/-- 论文 Lemma 3.1（§3.1，式 (3.4)）：p-adic 完备化整性。
    设 T(z) = ∏_{ν=1}^t (z − r_ν)，r_ν 为互异整数且模 p 两两不同，Y ∈ ℤ[X]，
    U_j ∈ ℤ[z] 且 deg U₀ ≤ p + 1，则 τ_Y^ext(∑_{j≥0} p^j U_j / T) ∈ ℤ_p[X]。
    骨架：以有限和与 Gauss 赋值非负呈现（p-adic 收敛性由 §3.1 构造保证）。 -/
theorem lemma_3_1 (p : ℕ) (hp : p.Prime) (hp7 : 7 ≤ p) (t J : ℕ) (hJ : 0 < J)
    (r : Fin t → ℤ)
    (hrr : ∀ i j, i ≠ j → ((r i - r j : ℤ) : ZMod p) ≠ 0)
    (Y : ℤ[X]) (U : Fin J → ℤ[X]) (hU0 : (U ⟨0, hJ⟩).natDegree ≤ p + 1) :
    0 ≤ vpGauss p hp
      (muX
        ((∑ j : Fin J, (p : ℚ) ^ j.val • ((U j).map (algebraMap ℤ ℚ) : RatFunc ℚ)) /
          ((∏ ν : Fin t, (Polynomial.X - Polynomial.C (r ν)) : ℤ[X]).map
            (algebraMap ℤ ℚ) : RatFunc ℚ))) := sorry

/-- 论文 Lemma 3.2（§3.2，式 (3.7)）：分布公式
    τ_X(g) = p^{−4} ∑_{a=0}^{p−1} τ_Y^ext(g(a + p x))，Y = p⁵X + C_p（式 (3.6)）。
    骨架以 μ 为载体并略去 Y 下标。 -/
theorem lemma_3_2 (p : ℕ) (hp : p.Prime) (g : RatFunc ℚ) (hg : IsAdmissible g) :
    muX g = ∑ a ∈ Finset.range p,
      (p : ℚ) ^ (-4 : ℤ) • muX (RatFunc.substAffine g (p : ℚ) (a : ℚ)) := sorry

/-- 论文 Lemma 3.3（§3.3，式 (3.10)）：小素数赋值界
    v_p^G(τ_X(g)) ≥ −6⌊log_p max(2K, d+1)⌋ − v_p(24)，
    g(x) = A(x)/∏_{−K≤r≤K, r≠0}(x − r)，A 为 ℤ 上 ≤ d 次整值多项式。 -/
theorem lemma_3_3 (n : ℕ) (p : ℕ) (hp : p.Prime) (A : ℤ[X]) (d : ℕ)
    (hd : A.natDegree ≤ d)
    (hval : ∀ x : ℤ, ∃ m : ℤ, A.eval₂ (algebraMap ℤ ℚ) (x : ℚ) = m) :
    vpGauss p hp
        (muX ((A.map (algebraMap ℤ ℚ) : RatFunc ℚ) /
          ((∏ r ∈ (Finset.Icc (-(Kparam n : ℤ)) (Kparam n : ℤ)).erase (0 : ℤ),
            (Polynomial.X - Polynomial.C ((r : ℤ) : ℚ)) : ℚ[X]) : RatFunc ℚ)))
      ≥ -6 * (Nat.log p (max (2 * Kparam n) (d + 1)) : ℤ) - vp p hp 24 := sorry

/-- 论文式 (3.12)：v_p^G(F_K) ≥ −6h⌊log_p(5K)⌋ − h·v_p(24)（每个素数 p）。 -/
theorem eq_3_12 (n : ℕ) (p : ℕ) (hp : p.Prime) :
    vpGauss p hp (FK n) ≥
      -6 * (hparam n : ℤ) * (Nat.log p (5 * Kparam n) : ℤ) - hparam n * vp p hp 24 := sorry

/-- 论文式 (5.3)：v_p(S_K) 的 Legendre 展开。 -/
theorem vpSK_formula (n : ℕ) (p : ℕ) (hp : p.Prime) :
    vpSK n p hp
      = 2 * (hparam n : ℤ) *
          (∑ a ∈ Finset.Icc 1 (Nat.log p (Kparam n)), ((Kparam n / p ^ a : ℕ) : ℤ))
        - 12 * (hparam n : ℤ) *
          (∑ a ∈ Finset.Icc 1 (Nat.log p (Nparam n)), ((Nparam n / p ^ a : ℕ) : ℤ))
        - 2 * ∑ i ∈ Finset.Icc 1 (hparam n - 1),
            ∑ a ∈ Finset.Icc 1 (Nat.log p (2 * i)), (((2 * i) / p ^ a : ℕ) : ℤ)
        + ((hparam n : ℤ) - 1) * vp p hp 4 := by
  haveI : Fact p.Prime := ⟨hp⟩
  -- 阶乘赋值的 Legendre 展开，截断到 Icc 1 (log_p m)
  -- （Nat 上 Icc 1 (log p m) = Ico 1 (log p m + 1)，无需分情形讨论 m = 0）
  have hfac : ∀ m : ℕ, padicValNat p (Nat.factorial m)
      = ∑ a ∈ Finset.Icc 1 (Nat.log p m), m / p ^ a := by
    intro m
    rw [padicValNat_factorial (Nat.lt_succ_self _)]
    refine Finset.sum_congr ?_ fun a _ => rfl
    ext a
    simp only [Finset.mem_Ico, Finset.mem_Icc]
    omega
  -- 乘积的赋值：∏ (2i)!² 的赋值为赋值之和
  have hpow_pos : ∀ i : ℕ, (0 : ℚ) < (Nat.factorial (2 * i)) ^ 2 :=
    fun i => pow_pos (Nat.cast_pos.2 (Nat.factorial_pos _)) 2
  have hprod : ∀ s : Finset ℕ, padicValRat p (∏ i ∈ s, ((Nat.factorial (2 * i)) ^ 2 : ℚ))
      = ∑ i ∈ s, (2 : ℤ) * (padicValNat p (Nat.factorial (2 * i)) : ℤ) := by
    intro s
    induction s using Finset.induction_on with
    | empty => rw [Finset.prod_empty, Finset.sum_empty, padicValRat.one]
    | insert a s has ih =>
        rw [Finset.prod_insert has, Finset.sum_insert has, padicValRat.mul, ih,
          padicValRat.pow, padicValRat.of_nat]
        · push_cast
          ring
        · exact ne_of_gt (hpow_pos a)
        · exact ne_of_gt (Finset.prod_pos fun i _ => hpow_pos i)
  -- 各因子非零
  have hA : ((Nat.factorial (Kparam n)) ^ (2 * hparam n) : ℚ) ≠ 0 :=
    pow_ne_zero _ (Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _))
  have hB : (4 : ℚ) ^ ((hparam n : ℤ) - 1) ≠ 0 := zpow_ne_zero _ (by norm_num)
  have hN : ((Nat.factorial (Nparam n)) ^ (12 * hparam n) : ℚ) ≠ 0 :=
    pow_ne_zero _ (Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _))
  have hD : (∏ i ∈ Finset.Icc 1 (hparam n - 1), ((Nat.factorial (2 * i)) ^ 2 : ℚ)) ≠ 0 :=
    ne_of_gt (Finset.prod_pos fun i _ => hpow_pos i)
  have hC : ((Nat.factorial (Nparam n)) ^ (12 * hparam n) *
      (∏ i ∈ Finset.Icc 1 (hparam n - 1), ((Nat.factorial (2 * i)) ^ 2 : ℚ)) : ℚ) ≠ 0 :=
    mul_ne_zero hN hD
  -- 主计算：把 padicValRat 分配到乘、除、幂上，再展开阶乘赋值
  have hvp : vpSK n p hp = padicValRat p (SK n) := rfl
  rw [hvp]
  show padicValRat p
      ((Nat.factorial (Kparam n)) ^ (2 * hparam n) *
        (4 : ℚ) ^ ((hparam n : ℤ) - 1) /
        ((Nat.factorial (Nparam n)) ^ (12 * hparam n) *
          (∏ i ∈ Finset.Icc 1 (hparam n - 1), ((Nat.factorial (2 * i)) ^ 2 : ℚ))))
      = 2 * (hparam n : ℤ) *
          (∑ a ∈ Finset.Icc 1 (Nat.log p (Kparam n)), ((Kparam n / p ^ a : ℕ) : ℤ))
        - 12 * (hparam n : ℤ) *
          (∑ a ∈ Finset.Icc 1 (Nat.log p (Nparam n)), ((Nparam n / p ^ a : ℕ) : ℤ))
        - 2 * ∑ i ∈ Finset.Icc 1 (hparam n - 1),
            ∑ a ∈ Finset.Icc 1 (Nat.log p (2 * i)), (((2 * i) / p ^ a : ℕ) : ℤ)
        + ((hparam n : ℤ) - 1) * padicValRat p 4
  rw [padicValRat.div (mul_ne_zero hA hB) hC, padicValRat.mul hA hB,
    padicValRat.mul hN hD, padicValRat.pow, padicValRat.pow, hprod, padicValRat.zpow,
    padicValRat.of_nat, padicValRat.of_nat]
  simp only [hfac]
  push_cast
  rw [← Finset.mul_sum]
  ring

/-- 桥梁引理（边界审计结论）：论文式 (5.3) 的 (h−1) 是普通整数减法。论文的全部
    使用范围是 n ≥ 1（Theorem 2.1 实际要求 K = 40n ≥ 200M²；M = 200 时 n ≥ 200000），
    此时 h = 37n ≥ 37 ≥ 1，整数减法与自然数减法一致。
    （骨架早期版本曾把该末项译为 ℕ 截断减法 `(hparam n - 1 : ℕ)`，它对 n = 0、p = 2
    是假命题——那是形式化翻译引入的缺陷；审计论文同类表达（(2.5)、(4.4)、C.3 的
    阶乘范围、C.2 的取整等）在其使用范围内均无歧义，论文本身没有 bug。） -/
theorem hparam_sub_one_bridge (n : ℕ) (hn : 1 ≤ n) :
    ((hparam n : ℤ) - 1) = ((hparam n - 1 : ℕ) : ℤ) := by
  show ((37 * n : ℤ) - 1) = ((37 * n - 1 : ℕ) : ℤ)
  omega

/-! ## §4：行列式的局部估计 -/

/-- 论文 Proposition 4.1（§4.1，式 (4.8)）：内区估值 v_p^G(Δ_K) ≥ γ_p^in，
    条件为 K/M < p ≤ K/3（论文式 (4.1)）。 -/
theorem prop_4_1 (n M : ℕ) (hM : 40 ≤ M) (hn : 200 * M ^ 2 ≤ Kparam n) (p : ℕ)
    (hp : p.Prime) (h1 : Kparam n < p * M) (h2 : 3 * p ≤ Kparam n) :
    (vpGauss p hp (deltaK n) : ℚ) ≥ ((gammaIn n M p : ℤ) : ℚ) := sorry

/-- 论文 Lemma 4.2（§4.2，式 (4.13)）：低秩修正行列式估值。
    设 A、L 为 h×h 矩阵，v(A_ij) ≥ w_i + w_j（w_i 非正半整数），L 整且秩 ≤ r，
    恰好 z 个权重为 0，则 v det(A + p^{−1}L) ≥ 2∑w_i − min(r, z)。 -/
theorem lemma_4_2 {ι : Type*} [Fintype ι] [DecidableEq ι] (A L : Matrix ι ι ℚ)
    (p : ℕ) (hp : p.Prime) (w : ι → ℚ) (hw : ∀ i j, w i + w j ≤ (vp p hp (A i j) : ℚ))
    (hL : ∀ i j, 0 ≤ vp p hp (L i j)) (r : ℕ) (hr : Matrix.rank L ≤ r)
    (z : ℕ) (hz : ((Finset.univ : Finset ι).filter fun i => w i = 0).card = z) :
    ((2 * ∑ i, w i - min r z : ℚ)) ≤ (vp p hp (Matrix.det (A + (p : ℚ)⁻¹ • L)) : ℚ) := sorry

/-- 论文 Proposition 4.3（§4.2 末，条件 (4.9)）：外区估值 v_p^G(Δ_K) ≥ γ_p^out。 -/
theorem prop_4_3_outer (n M : ℕ) (p : ℕ) (hp : p.Prime)
    (h1 : 7 ≤ p) (h2 : p ≤ Kparam n) (h3 : Kparam n < 3 * p) (h4 : 2 * Kparam n < p ^ 2)
    (h5 : 2 * Nparam n < p) (h6 : 5 * Nparam n ≤ 2 * p - 2) :
    vpGauss p hp (deltaK n) ≥ gammaOut n M p := sorry

/-- 论文 Proposition 4.3 第二断言：p > K 时 v_p^G(Δ_K) ≥ 0。 -/
theorem prop_4_3_large (n : ℕ) (p : ℕ) (hp : p.Prime) (hK : Kparam n < p) :
    0 ≤ vpGauss p hp (deltaK n) := sorry

/-! ## §5：规范化与素数和 -/

/-- 论文 Proposition 5.1（§5）：Q_{K,M} = m_{K,M} F_K ∈ ℤ[X]。 -/
theorem prop_5_1 (n M : ℕ) (hM : 40 ≤ M) (hn : 200 * M ^ 2 ≤ Kparam n) :
    ∃ P : ℤ[X], Polynomial.map (Int.castRingHom ℚ) P = QKM n M := sorry

/-- 论文 Proposition 5.2（§5，式 (5.11)/(5.21)）：固定 M ≥ 40，
    limsup_{K→∞, 40|K} K^{−2} log m_{K,M} ≤ A_M。 -/
theorem prop_5_2 (M : ℕ) (hM : 40 ≤ M) :
    Filter.limsup (fun n : ℕ => Real.log (mKM n M) / (Kparam n : ℝ) ^ 2) Filter.atTop
      ≤ (AM M : ℝ) := sorry

/-! ## §6：实行列式 -/

/-- 外场 V(t) = 2π√t + ∫₀¹ log(t+u²)du − 6∫₀^α log(t+u²)du（论文式 (6.1)）。 -/
noncomputable def externalField (t : ℝ) : ℝ :=
  2 * Real.pi * Real.sqrt t + ∫ u in (0 : ℝ)..1, Real.log (t + u ^ 2)
    - 6 * ∫ u in (0 : ℝ)..(3 / 40 : ℝ), Real.log (t + u ^ 2)

/-- 对数势 U^ρ(t) = ∫ log|t − x| dρ(x)（论文式 (6.1) 后）。 -/
noncomputable def logPotential (ρ : MeasureTheory.Measure ℝ) (t : ℝ) : ℝ :=
  ∫ x, Real.log |t - x| ∂ρ

/-- 对数能量 I(ρ) = ∬ log|x − y| dρ(x)dρ(y)（论文式 (6.1) 后）。 -/
noncomputable def logEnergy (ρ : MeasureTheory.Measure ℝ) : ℝ :=
  ∫ x, ∫ y, Real.log |x - y| ∂ρ ∂ρ

/-- 论文 Lemma 6.1（§6，式 (6.2)–(6.4)）：比较测度 ρ——16 个嵌套区间上 arcsine 测度
    的正倍数之和（Table 1），质量 λ = 37/40，支撑于 (0,2)，每区间长度 > 1/225，
    2U^ρ(t) − V(t) ≤ M₀ = −1329/200（t ≥ 0），且 λM₀ − I(ρ) + C_* ≤ Ū。 -/
theorem lemma_6_1 : ∃ ρ : MeasureTheory.Measure ℝ,
    MeasureTheory.IsFiniteMeasure ρ ∧ ρ (Set.Ioo 0 2)ᶜ = 0 ∧
    ρ Set.univ = ENNReal.ofReal (lambdaP : ℝ) ∧
    (∀ t : ℝ, 0 ≤ t → 2 * logPotential ρ t - externalField t ≤ (M₀ : ℝ)) ∧
    ((lambdaP : ℝ) * (M₀ : ℝ) - logEnergy ρ + Cstar ≤ (Ubar : ℝ)) := sorry

/-- 论文 Lemma 6.2（§6.1，式 (6.5)，零质量对数能量）：设 μ₁、μ₂ 为 ℂ 上有限测度
    且 μ₁(ℂ) = μ₂(ℂ)，对数核关于 (μ₁+μ₂)⊗(μ₁+μ₂) 可积，则签名测度 μ₁ − μ₂ 的
    对数能量 I(μ₁) − 2I(μ₂,μ₁) + I(μ₂) ≤ 0。 -/
theorem lemma_6_2 (μ₁ μ₂ : MeasureTheory.Measure ℂ)
    [MeasureTheory.IsFiniteMeasure μ₁] [MeasureTheory.IsFiniteMeasure μ₂]
    (hmass : μ₁ Set.univ = μ₂ Set.univ)
    (hint : MeasureTheory.Integrable (fun p : ℂ × ℂ => Real.log ‖p.1 - p.2‖)
      ((μ₁ + μ₂).prod (μ₁ + μ₂))) :
    (∫ x, ∫ y, Real.log ‖x - y‖ ∂μ₁ ∂μ₁)
      - 2 * ∫ x, ∫ y, Real.log ‖x - y‖ ∂μ₂ ∂μ₁
      + ∫ x, ∫ y, Real.log ‖x - y‖ ∂μ₂ ∂μ₂ ≤ 0 := sorry

/-- 论文 Proposition 6.3（§6.2，式 (6.16)）：对每个 K = 40n（n ≥ 1），
    0 < F_K(ζ(5)) 且 log F_K(ζ(5)) ≤ ŪK² + 24K log K + 200K。 -/
theorem prop_6_3 (n : ℕ) (hn : 0 < n) :
    0 < (FK n).eval₂ (algebraMap ℚ ℝ) zeta5 ∧
      Real.log ((FK n).eval₂ (algebraMap ℚ ℝ) zeta5)
        ≤ (Ubar : ℝ) * (Kparam n : ℝ) ^ 2 + 24 * (Kparam n : ℝ) * Real.log (Kparam n)
          + 200 * (Kparam n : ℝ) := sorry

/-! ## §7：完成 -/

/-- 论文式 (7.1)：limsup_{K→∞, 40|K} K^{−2} log Q_{K,M}(ζ(5)) ≤ A_M + Ū（M ≥ 40）。
    由 log Q = log m + log F（`prop_5_2` + `prop_6_3` 经 limsup 次可加性）得出。
    占位说明：mathlib 的 `Filter.limsup_add_le`（ℝ 上）要求两列都 Eventually 有界；
    `log m_{K,M}/K²` 的常数界是论文 §5（式 5.21 一阶）的量级内容，超出当前骨架的
    sorry-前提可推导范围，故此处保留 sorry（其余装配链见 Main.lean）。 -/
theorem eq_7_1 (M : ℕ) (hM : 40 ≤ M) :
    Filter.limsup
      (fun n : ℕ => Real.log ((QKM n M).eval₂ (algebraMap ℚ ℝ) zeta5) / (Kparam n : ℝ) ^ 2)
      Filter.atTop ≤ (AM M : ℝ) + (Ubar : ℝ) := sorry

/-! ## Appendix C：有理逼近与系数高度 -/

/-- G_K(ζ(5)) 的实矩阵（论文 Appendix C.1）。 -/
noncomputable def GR (n : ℕ) : Matrix (Fin (hparam n)) (Fin (hparam n)) ℝ :=
  Matrix.of fun i j => (Gentry n i j).eval₂ (algebraMap ℚ ℝ) zeta5

/-- M_K = [X]G_K(X) 的实矩阵（X 的一次项系数矩阵，论文 Appendix C.1）。 -/
noncomputable def MR (n : ℕ) : Matrix (Fin (hparam n)) (Fin (hparam n)) ℝ :=
  Matrix.of fun i j => ((Gentry n i j).coeff 1 : ℝ)

/-- 论文 Proposition C.1（Appendix C.1，式 (C.1)）：对所有充分大的 K ∈ 40ℤ_{>0}，
    ‖B_K‖ ≤ e^{ϱK}，ϱ = 6933/500（B_K = G^{−1/2} M_K G^{−1/2} 的欧氏算子范数）。 -/
theorem prop_C_1 : ∀ᶠ n in Filter.atTop,
    ∃ B : Matrix (Fin (hparam n)) (Fin (hparam n)) ℝ,
      (∀ x : Fin (hparam n) → ℝ, ‖B.mulVec x‖ ≤ Real.exp ((rhoC : ℝ) * Kparam n) * ‖x‖) := sorry

/-- 论文 Appendix C.2：取 M = 100000、c = 75/4、K = 40⌈c log b / 40⌉，
    则对充分大的 b 与任意 a ∈ ℤ：0 < b^h Q_{K,100000}(a/b) < 1，
    与整性矛盾，从而证明 Corollary 1.2。所需常数恒等式见 Numerics.lean。 -/
theorem prop_C_2 : ∀ᶠ b : ℕ in Filter.atTop, ∀ a : ℤ,
    (0 : ℝ) < (b : ℝ) ^ (37 * ⌈(75 / 4 : ℝ) * Real.log b / 40⌉₊) *
        (QKM ⌈(75 / 4 : ℝ) * Real.log b / 40⌉₊ 100000).eval₂ (algebraMap ℚ ℝ) ((a : ℝ) / b)
    ∧ (b : ℝ) ^ (37 * ⌈(75 / 4 : ℝ) * Real.log b / 40⌉₊) *
        (QKM ⌈(75 / 4 : ℝ) * Real.log b / 40⌉₊ 100000).eval₂ (algebraMap ℚ ℝ) ((a : ℝ) / b)
      < 1 := sorry

end Zeta5Irrational
