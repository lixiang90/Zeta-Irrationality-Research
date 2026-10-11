import Mathlib
import Zeta5Irrational.Params

/-!
# μ 泛函、Hankel 矩阵与规范化多项式（论文 §2、§5）

- μ_X：ℚ-线性泛函，取值 ℚ[X]（论文式 (2.2)–(2.3)）。
- G_K、Δ_K、F_K（论文式 (2.4)–(2.5)）。
- m_{K,M} 与 Q_{K,M}（论文式 (5.1)–(5.2) 与 (2.6)）。
-/

open scoped Polynomial

namespace Zeta5Irrational

/-- μ_X(t^e) = (−1)^e B_{2e+2}(2e+3)(2e+4)(2e+5)/24（论文式 (2.2)）。 -/
noncomputable def muMonomial (e : ℕ) : ℚ[X] :=
  Polynomial.C (((-1 : ℚ) ^ e) * (bernoulli (2 * e + 2)) * (2 * e + 3) * (2 * e + 4) *
    (2 * e + 5) / 24)

/-- μ_X(1/(t+j²)) = j⁴(X − H_j⁽⁵⁾) − 1/4 + 1/(2j)（论文式 (2.3)）。 -/
noncomputable def muPole (j : ℕ) : ℚ[X] :=
  Polynomial.C ((j : ℚ) ^ 4) * (Polynomial.X - Polynomial.C (harm5 j)) +
    Polynomial.C (-(1 / 4 : ℚ) + 1 / (2 * j))

/-- μ_X 的定义性数据（论文 §2.1 末段）：ℚ-线性、由多项式除法与部分分式延拓，
    且仅单极点值依赖 X（仿射）。 -/
structure IsMuFunctional (μ : RatFunc ℚ → ℚ[X]) : Prop where
  map_zero : μ 0 = 0
  map_add : ∀ f g : RatFunc ℚ, μ (f + g) = μ f + μ g
  map_smul : ∀ (q : ℚ) (f : RatFunc ℚ), μ (RatFunc.C q * f) = Polynomial.C q * μ f
  map_monomial : ∀ e : ℕ, μ (RatFunc.X ^ e) = muMonomial e
  map_pole : ∀ j : ℕ, 0 < j → μ ((RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹) = muPole j

/-- μ 泛函构造的候选集：单项式 X^e 与单极点项 (X + j²)⁻¹（论文 §2.1）。 -/
private noncomputable def muCandidate (i : ℕ ⊕ ℕ) : RatFunc ℚ :=
  match i with
  | Sum.inl e => RatFunc.X ^ e
  | Sum.inr j => (RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹

/-- 左/右指标的提取函数（ℕ ⊕ ℕ → ℕ）。 -/
private def muIdxL : ℕ ⊕ ℕ → ℕ
  | Sum.inl e => e
  | Sum.inr _ => 0

/-- 提取函数（ℕ ⊕ ℕ → ℕ），右支。 -/
private def muIdxR : ℕ ⊕ ℕ → ℕ
  | Sum.inl _ => 0
  | Sum.inr j => j

/-- `LinearIndepOn.extend` 在原子集元素上的取值（由 `coe_extend` 给出）。 -/
private theorem extend_apply_mem {K V : Type*} [DivisionRing K] [AddCommGroup V] [Module K V]
    {s : Set V} (hs : LinearIndepOn K id s) {v : V} (hv : v ∈ s) :
    Module.Basis.extend hs ⟨v, Module.Basis.subset_extend hs hv⟩ = v :=
  congrFun (Module.Basis.coe_extend hs) _

/-- Rat.cast 与 `RatFunc.C` 一致（两种 ℚ-代数结构间的桥）。 -/
private theorem RatFunc.ratCast_eq_C (q : ℚ) : (q : RatFunc ℚ) = RatFunc.C q := by
  show ⇑(algebraMap ℚ (RatFunc ℚ)) q = RatFunc.C q
  rw [← RatFunc.algebraMap_C, IsScalarTower.algebraMap_apply ℚ ℚ[X] (RatFunc ℚ)]
  simp

/-- 主 `Algebra ℚ (RatFunc ℚ)` 实例（RatAlgebra）的 algebraMap 等于 `RatFunc.C`。 -/
private theorem RatFunc.algebraMap_rat_eq_C (q : ℚ) :
    ⇑(algebraMap ℚ (RatFunc ℚ)) q = RatFunc.C q :=
  RatFunc.ratCast_eq_C q

/-- 候选集 {X^e : e ∈ ℕ} ∪ {(X + j²)⁻¹ : j ∈ ℕ} 线性无关（论文 §2.1/§3）。
    证明：部分分式分解的唯一性 `Polynomial.quo_add_sum_rem_div_unique`。 -/
private theorem muCandidate_li : LinearIndependent ℚ muCandidate := by
    rw [linearIndependent_iff']
    intro s c hsum i hi
    -- 拆分为左（多项式）右（极点）两部分
    rw [← Finset.sum_filter_add_sum_filter_not (p := (Sum.isLeft ·))] at hsum
    have hsum' : (∑ x ∈ s.filter (Sum.isLeft ·),
          ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x)
        + ∑ x ∈ s.filter fun x => ¬ Sum.isLeft x,
            ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x = 0 := hsum
    set EL : Finset ℕ := (s.filter (Sum.isLeft ·)).image
      muIdxL with hEL
    set EJ : Finset ℕ := (s.filter fun x => ¬ Sum.isLeft x).image
      muIdxR with hEJ
    -- 左半部分：写成单个多项式的像
    have hinjL : ∀ x ∈ s.filter (Sum.isLeft ·), ∀ y ∈ s.filter (Sum.isLeft ·),
        muIdxL x = muIdxL y → x = y := by
      intro x hx y hy
      simp only [Finset.mem_filter] at hx hy
      rcases x with xe | xj
      · rcases y with ye | yj
        · intro h
          have h2 : xe = ye := h
          rw [h2]
        · simp at hy
      · simp at hx
    have hL : (∑ x ∈ s.filter (Sum.isLeft ·), ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x)
        = ((∑ e ∈ EL, Polynomial.C (c (Sum.inl e)) * Polynomial.X ^ e : ℚ[X]) :
          RatFunc ℚ) := by
      have h1 : (∑ x ∈ s.filter (Sum.isLeft ·), ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x)
          = ∑ x ∈ s.filter (Sum.isLeft ·), (fun e => RatFunc.C (c (Sum.inl e))
            * RatFunc.X ^ e)
            (muIdxL x) := by
        refine Finset.sum_congr rfl fun x hx => ?_
        rcases x with e | j
        · rw [RatFunc.algebraMap_rat_eq_C]
          rfl
        · simp at hx
      rw [h1]
      have h3 := (Finset.sum_image hinjL (s := s.filter (Sum.isLeft ·))
        (g := muIdxL)
        (f := fun e => RatFunc.C (c (Sum.inl e)) * RatFunc.X ^ e)).symm
      rw [h3]
      show (∑ e ∈ EL, RatFunc.C (c (Sum.inl e)) * RatFunc.X ^ e)
        = ⇑(algebraMap ℚ[X] (RatFunc ℚ))
          (∑ e ∈ EL, Polynomial.C (c (Sum.inl e)) * Polynomial.X ^ e)
      rw [map_sum (algebraMap ℚ[X] (RatFunc ℚ))]
      refine Finset.sum_congr rfl fun e he => ?_
      rw [map_mul, map_pow, RatFunc.algebraMap_C, RatFunc.algebraMap_X]
    -- 右半部分：写成 C (b j) / (X + j²) 的和
    have hinjR : ∀ x ∈ s.filter fun x => ¬ Sum.isLeft x,
        ∀ y ∈ s.filter fun x => ¬ Sum.isLeft x,
        muIdxR x = muIdxR y → x = y := by
      intro x hx y hy h
      simp only [Finset.mem_filter] at hx hy
      rcases x with xe | xj
      · simp at hx
      · rcases y with ye | yj
        · simp at hy
        · simp only [muIdxR] at h
          exact congrArg Sum.inr h
    have hJ : (∑ x ∈ s.filter fun x => ¬ Sum.isLeft x, ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x)
        = ∑ j ∈ EJ, ((Polynomial.C (c (Sum.inr j)) : ℚ[X]) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) := by
      have h1 : (∑ x ∈ s.filter fun x => ¬ Sum.isLeft x, ⇑(algebraMap ℚ (RatFunc ℚ)) (c x) * muCandidate x)
          = ∑ x ∈ s.filter fun x => ¬ Sum.isLeft x, (fun j => (Polynomial.C (c (Sum.inr j)) :
            RatFunc ℚ) / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ))
            (muIdxR x) := by
        refine Finset.sum_congr rfl fun x hx => ?_
        rcases x with e | j
        · simp at hx
        · show ⇑(algebraMap ℚ (RatFunc ℚ)) (c (Sum.inr j))
            * (RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹
            = ⇑(algebraMap ℚ[X] (RatFunc ℚ)) (Polynomial.C (c (Sum.inr j)))
              / ⇑(algebraMap ℚ[X] (RatFunc ℚ)) (Polynomial.X + Polynomial.C ((j : ℚ) ^ 2))
          rw [RatFunc.algebraMap_rat_eq_C, ← div_eq_mul_inv, map_add, RatFunc.algebraMap_X,
            RatFunc.algebraMap_C, RatFunc.algebraMap_C]
      rw [h1]
      have h3 := (Finset.sum_image hinjR (s := s.filter fun x => ¬ Sum.isLeft x)
        (g := muIdxR)
        (f := fun j => ((Polynomial.C (c (Sum.inr j)) : ℚ[X]) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ))).symm
      rw [h3]
    have hsum2 : ((∑ e ∈ EL, Polynomial.C (c (Sum.inl e)) * Polynomial.X ^ e : ℚ[X]) : RatFunc ℚ)
        + ∑ j ∈ EJ, ((Polynomial.C (c (Sum.inr j)) : ℚ[X]) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) = 0 := by
      rw [← hL, ← hJ]
      exact hsum'
    -- 第二步：部分分式分解的唯一性
    have hcop : Set.Pairwise ↑EJ
        (fun i j : ℕ => IsCoprime (Polynomial.X + Polynomial.C ((i : ℚ) ^ 2))
          (Polynomial.X + Polynomial.C ((j : ℚ) ^ 2))) := by
      intro x hx y hy hxy
      have hsq : ((x : ℚ) ^ 2 - (y : ℚ) ^ 2) ≠ 0 := by
        intro h0
        apply hxy
        have h1 : (x : ℚ) ^ 2 = (y : ℚ) ^ 2 := by linarith
        have h2 : x ^ 2 = y ^ 2 := by exact_mod_cast h1
        exact (Nat.pow_left_inj (by norm_num : 2 ≠ 0)).1 h2
      refine ⟨Polynomial.C (((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹,
        Polynomial.C (-(((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹), ?_⟩
      have hu : (((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹ * ((x : ℚ) ^ 2 - (y : ℚ) ^ 2) = 1 :=
        inv_mul_cancel₀ hsq
      have hcalc : Polynomial.C (((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹
            * (Polynomial.X + Polynomial.C ((x : ℚ) ^ 2))
          + Polynomial.C (-(((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹)
            * (Polynomial.X + Polynomial.C ((y : ℚ) ^ 2))
          = Polynomial.C ((((x : ℚ) ^ 2 - (y : ℚ) ^ 2))⁻¹ * ((x : ℚ) ^ 2 - (y : ℚ) ^ 2)) := by
        rw [Polynomial.C_neg, Polynomial.C_mul, Polynomial.C_sub]
        ring
      rw [hcalc, hu, Polynomial.C_1]
    have hf0 : ((∑ e ∈ EL, Polynomial.C (c (Sum.inl e)) * Polynomial.X ^ e : ℚ[X]) :
          RatFunc ℚ)
        + ∑ j ∈ EJ, ((Polynomial.C (c (Sum.inr j)) : ℚ[X]) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ)
        = ↑((Polynomial.C 0 : ℚ[X])) + ∑ j ∈ EJ, (((Polynomial.C 0 : ℚ[X])) : RatFunc ℚ)
          / ((Polynomial.X + Polynomial.C ((j : ℚ) ^ 2) : ℚ[X]) : RatFunc ℚ) := by
      rw [hsum2]
      simp
    obtain ⟨hP, hb⟩ := Polynomial.quo_add_sum_rem_div_unique
      (g := fun j : ℕ => Polynomial.X + Polynomial.C ((j : ℚ) ^ 2))
      (s := EJ)
      (q₁ := ∑ e ∈ EL, Polynomial.C (c (Sum.inl e)) * Polynomial.X ^ e)
      (r₁ := fun j : ℕ => Polynomial.C (c (Sum.inr j)))
      (q₂ := Polynomial.C 0)
      (r₂ := fun _ : ℕ => Polynomial.C 0)
      (hg := fun j _ => Polynomial.monic_X_add_C _)
      (hcop := hcop)
      (hr₁ := fun j _ => lt_of_le_of_lt Polynomial.degree_C_le
        (by rw [Polynomial.degree_X_add_C]; exact_mod_cast zero_lt_one))
      (hr₂ := fun j _ => lt_of_le_of_lt Polynomial.degree_C_le
        (by rw [Polynomial.degree_X_add_C]; exact_mod_cast zero_lt_one))
      (hf := hf0)
    -- 第三步：读出系数
    rcases i with e | j
    · have he : e ∈ EL := by
        refine Finset.mem_image.2 ⟨Sum.inl e, ?_, rfl⟩
        simp only [Finset.mem_filter]
        exact ⟨hi, Sum.isLeft_inl⟩
      have h1 := congrArg (fun p : ℚ[X] => p.coeff e) hP
      simp only [Polynomial.finsetSum_coeff, Polynomial.coeff_C_mul, Polynomial.coeff_X_pow,
        mul_ite, mul_one, mul_zero, Polynomial.coeff_zero, Polynomial.C_0] at h1
      have h1' := Finset.sum_ite_eq EL e (fun x => c (Sum.inl x))
      rw [if_pos he] at h1'
      rw [← h1']
      exact h1
    · have hj : j ∈ EJ := by
        refine Finset.mem_image.2 ⟨Sum.inr j, ?_, rfl⟩
        simp only [Finset.mem_filter]
        exact ⟨hi, by simp⟩
      have h2 : c (Sum.inr j) = 0 := Polynomial.C_injective (hb j hj)
      exact h2

/-- 候选集上的 LinearIndepOn。 -/
private theorem muHs : LinearIndepOn ℚ id (Set.range muCandidate) :=
  muCandidate_li.linearIndepOn_id

/-- 扩张得到的基。 -/
private noncomputable def muB : Module.Basis ↥(muHs.extend (Set.subset_univ _)) ℚ (RatFunc ℚ) :=
  Module.Basis.extend muHs

/-- 基上的取值表：候选元素取 muMonomial/muPole，其余取 0。 -/
private noncomputable def muVal : ↥(muHs.extend (Set.subset_univ _)) → ℚ[X] := by
  classical
  exact fun x => if h : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x : RatFunc ℚ) then
    (match Classical.choose h with
      | Sum.inl e => muMonomial e
      | Sum.inr j => muPole j)
  else 0

/-- μ 泛函的显式实现（基扩张 + 取值表的线性扩张）。 -/
noncomputable def muLin : RatFunc ℚ →ₗ[ℚ] ℚ[X] := muB.constr ℚ muVal

private theorem muLin_monomial (e : ℕ) : muLin (RatFunc.X ^ e) = muMonomial e := by
  classical
  set x₀ : muHs.extend (Set.subset_univ _)
    := ⟨muCandidate (Sum.inl e), Module.Basis.subset_extend muHs (Set.mem_range_self _)⟩ with hx₀
  have hb : muB x₀ = RatFunc.X ^ e := extend_apply_mem muHs (Set.mem_range_self _)
  rw [← hb]
  show (muB.constr ℚ muVal) (muB x₀) = muMonomial e
  rw [Module.Basis.constr_basis]
  show (if h : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ) then
      (match Classical.choose h with
        | Sum.inl e => muMonomial e
        | Sum.inr j => muPole j)
    else 0) = muMonomial e
  rw [dif_pos (⟨Sum.inl e, rfl⟩ : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ))]
  have hspec : muCandidate (Classical.choose (⟨Sum.inl e, rfl⟩ : ∃ i : ℕ ⊕ ℕ,
      muCandidate i = (x₀ : RatFunc ℚ))) = (x₀ : RatFunc ℚ) :=
    Classical.choose_spec (⟨Sum.inl e, rfl⟩ : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ))
  have hc : Classical.choose (⟨Sum.inl e, rfl⟩ : ∃ i : ℕ ⊕ ℕ,
      muCandidate i = (x₀ : RatFunc ℚ)) = Sum.inl e :=
    muCandidate_li.injective hspec
  rw [hc]

private theorem muLin_pole (j : ℕ) :
    muLin ((RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹) = muPole j := by
  classical
  set x₀ : muHs.extend (Set.subset_univ _)
    := ⟨muCandidate (Sum.inr j), Module.Basis.subset_extend muHs (Set.mem_range_self _)⟩ with hx₀
  have hb : muB x₀
      = (RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹ := extend_apply_mem muHs (Set.mem_range_self _)
  rw [← hb]
  show (muB.constr ℚ muVal) (muB x₀) = muPole j
  rw [Module.Basis.constr_basis]
  show (if h : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ) then
      (match Classical.choose h with
        | Sum.inl e => muMonomial e
        | Sum.inr j => muPole j)
    else 0) = muPole j
  rw [dif_pos (⟨Sum.inr j, rfl⟩ : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ))]
  have hspec : muCandidate (Classical.choose (⟨Sum.inr j, rfl⟩ : ∃ i : ℕ ⊕ ℕ,
      muCandidate i = (x₀ : RatFunc ℚ))) = (x₀ : RatFunc ℚ) :=
    Classical.choose_spec (⟨Sum.inr j, rfl⟩ : ∃ i : ℕ ⊕ ℕ, muCandidate i = (x₀ : RatFunc ℚ))
  have hc : Classical.choose (⟨Sum.inr j, rfl⟩ : ∃ i : ℕ ⊕ ℕ,
      muCandidate i = (x₀ : RatFunc ℚ)) = Sum.inr j :=
    muCandidate_li.injective hspec
  rw [hc]

/-- μ（显式实现）满足定义性性质。 -/
theorem isMuFunctional_muLin : IsMuFunctional muLin :=
  ⟨muLin.map_zero, fun f₁ f₂ => muLin.map_add f₁ f₂, fun q f => by
    have h := muLin.map_smul q f
    rw [Algebra.smul_def, Algebra.smul_def,
      IsScalarTower.algebraMap_apply ℚ ℚ[X] (RatFunc ℚ)] at h
    simp at h
    rw [RatFunc.ratCast_eq_C] at h
    exact h, muLin_monomial, fun j hj => muLin_pole j⟩

/-- μ 泛函存在（论文 §2.1：由式 (2.2)/(2.3) 经多项式除法与部分分式延拓）。
    证明：候选集 {X^e} ∪ {(X+j²)⁻¹} 在 RatFunc ℚ 中线性无关
    （关键：部分分式分解的唯一性 `Polynomial.quo_add_sum_rem_div_unique`），
    将其扩充为基（`Module.Basis.extend`）后按取值表作线性扩张（`Basis.constr`）。 -/
theorem muFunctional_exists : ∃ μ : RatFunc ℚ → ℚ[X], IsMuFunctional μ :=
  ⟨muLin, isMuFunctional_muLin⟩

/-- μ_X 泛函（论文式 (2.2)–(2.3)），显式实现 `muLin`
    （候选集线性无关扩充为基后按取值表线性扩张；存在性见 `muFunctional_exists`）。 -/
noncomputable def muX : RatFunc ℚ → ℚ[X] := muLin

/-- μ_X 满足定义性性质。 -/
theorem muX_spec : IsMuFunctional muX := isMuFunctional_muLin

/-- μ_X(X^e) = muMonomial e（论文式 (2.2)）。 -/
theorem muX_monomial (e : ℕ) : muX (RatFunc.X ^ e) = muMonomial e :=
  muLin_monomial e

/-- μ_X((X + j²)⁻¹) = muPole j（论文式 (2.3)）。 -/
theorem muX_pole (j : ℕ) :
    muX ((RatFunc.X + RatFunc.C ((j : ℚ) ^ 2))⁻¹) = muPole j :=
  muLin_pole j

/-- 矩阵 G_K 的 (i,j) 项：μ_X( D_N(t)⁶ t^{i+j} / D_K(t) )（论文式 (2.4)）。 -/
noncomputable def Gentry (n i j : ℕ) : ℚ[X] :=
  muX (((D (Nparam n) : RatFunc ℚ) ^ 6 * RatFunc.X ^ (i + j)) /
    (D (Kparam n) : RatFunc ℚ))

/-- Δ_K(X) = det G_K(X)（论文式 (2.4)）。 -/
noncomputable def deltaK (n : ℕ) : ℚ[X] :=
  Matrix.det (Matrix.of fun i j : Fin (hparam n) => Gentry n i j)

/-- F_K = S_K Δ_K（论文式 (2.5)）。 -/
noncomputable def FK (n : ℕ) : ℚ[X] := Polynomial.C (SK n) * deltaK n

/-!
## 局部赋值界与规范化因子 m_{K,M}（论文 §5，式 (5.1)–(5.3)）
-/

/-- 素数 p 的有理赋值 v_p（论文记号；mathlib 的 `padicValRat`）。 -/
noncomputable def vp (p : ℕ) (hp : p.Prime) : ℚ → ℤ := by
  letI : Fact p.Prime := ⟨hp⟩
  exact padicValRat p

/-- v_p(S_K)（论文式 (5.3) 记号的骨架实现，直接取 S_K 的 p-adic 赋值；
    其 Legendre 展开见命题 `vpSK_formula`）。 -/
noncomputable def vpSK (n : ℕ) (p : ℕ) (hp : p.Prime) : ℤ := vp p hp (SK n)

/-- 多项式的 Gauss 赋值 v_p^G：系数赋值的最小值（论文 §3 开头）。 -/
noncomputable def vpGauss (p : ℕ) (hp : p.Prime) (P : ℚ[X]) : ℤ :=
  (Finset.range (P.natDegree + 1)).inf' Finset.nonempty_range_add_one
    fun i => vp p hp (P.coeff i)

/-- ℓ_A(a)（论文式 (4.1)）：满足 1 ≤ j ≤ A 且 j ≡ ±a (mod p) 的 j 的个数。 -/
def ellCount (p A a : ℕ) : ℕ :=
  ((Finset.Icc 1 A).filter
    (fun j => j % p = a % p ∨ j % p = (p - a % p) % p)).card

/-- m_A = ⌊A/p⌋（论文式 (4.1)）。 -/
def mFloor (p A : ℕ) : ℕ := A / p

/-- L₀ = 4M + 10（论文式 (4.4) 前）。 -/
def L0 (M : ℕ) : ℕ := 4 * M + 10

/-- m = (p−1)/2（论文式 (4.4) 前）。 -/
def mHalf (p : ℕ) : ℕ := (p - 1) / 2

/-- E（论文式 (4.4)）：h − L₀ + 3(N − m_N) 模 m 的余数；骨架按 0 ≤ E < m 实现。 -/
def Epar (n M p : ℕ) : ℕ :=
  (hparam n - L0 M + 3 * (Nparam n - mFloor p (Nparam n))) % mHalf p

/-- T（论文式 (4.4)）：(h − L₀ + 3(N − m_N)) / m。 -/
def Tpar (n M p : ℕ) : ℕ :=
  (hparam n - L0 M + 3 * (Nparam n - mFloor p (Nparam n))) / mHalf p

/-- ε_a（论文式 (4.4) 的 ε）：前 E 个类（按 ℓ_K 降序）取 1，其余取 0。
    骨架按 a < E 实现（并列次序任意，不影响估值陈述）。 -/
def epsPar (n M p a : ℕ) : ℕ := if a < Epar n M p then 1 else 0

/-- b_a = 3ℓ_N(a)（论文式 (4.4) 前）。 -/
def bPar (n p a : ℕ) : ℕ := 3 * ellCount p (Nparam n) a

/-- L_a = T − b_a + ε_a（论文式 (4.4)）。 -/
def Lpar (n M p a : ℕ) : ℕ := Tpar n M p - bPar n p a + epsPar n M p a

/-- Z_c = L_c + b_c = T + ε_c（论文式 (4.4)）。 -/
def Zpar (n M p c : ℕ) : ℕ := Tpar n M p + epsPar n M p c

/-- 行权重的 2 倍 2w_{a,i}（论文式 (4.6)/(4.7)：w 为半整数，2w ∈ ℤ）。
    内层 min 原文取 1 ≤ c ≤ m；骨架取 0 ≤ c ≤ m（多出的 c = 0 项仅为占位，不影响估值陈述）。 -/
def w2Par (n M p a i : ℕ) : ℤ :=
  if a = 0 then
    min (4 * (i : ℤ) + 12 * (mFloor p (Nparam n) : ℤ) - 2 * (mFloor p (Kparam n) : ℤ) + 1)
      ((Finset.Icc 0 (mHalf p)).inf' (Finset.nonempty_Icc.mpr (Nat.zero_le _))
        fun c => 2 * (Zpar n M p c : ℤ) - (ellCount p (Kparam n) c + 4 : ℤ))
  else
    2 * (i : ℤ) + 2 * (bPar n p a : ℤ) - (ellCount p (Kparam n) a + 4 : ℤ)

/-- γ_p^in = 2∑_{a=0}^{m}∑_{i=0}^{L_a−1} w_{a,i} = ∑∑ 2w_{a,i}（论文式 (4.8)，整数）。 -/
def gammaIn (n M p : ℕ) : ℤ :=
  ∑ a ∈ Finset.range (mHalf p + 1),
    ∑ i ∈ Finset.range (Lpar n M p a), w2Par n M p a i

/-- γ_p^out（论文式 (4.14)）：外区行列式估值整数。 -/
def gammaOut (n M p : ℕ) : ℤ :=
  let v := Kparam n - p * (Kparam n / p)
  let u := max 0 (Nparam n + v - p + 1)
  let t := min (Nparam n) v + u
  let rp : ℕ := max 0 (Kparam n + 4 * Nparam n - 2 * p + 2)
  if Kparam n < 2 * p then
    -7 * ((Kparam n : ℤ) - (p : ℤ)) + 6 * (t : ℤ) - 1 -
      ((min rp (p - 1 - Nparam n + u) : ℕ) : ℤ)
  else
    -7 * ((Kparam n : ℤ) - (p : ℤ)) + 3 + 12 * (Nparam n : ℤ) + 5 * (t : ℤ) -
      ((min rp (p + u) : ℕ) : ℤ)

/-- 局部赋值界 L_p(K, M)（论文式 (5.1)，三个分支：pM ≤ K、pM > K ∧ 3p ≤ K、3p > K）。 -/
noncomputable def Lp (n M p : ℕ) (hp : p.Prime) : ℤ :=
  if p * M ≤ Kparam n then
    -6 * (hparam n : ℤ) * (Nat.log p (5 * Kparam n) : ℤ) - (hparam n : ℤ) * vp p hp 24
  else if 3 * p ≤ Kparam n then
    vpSK n p hp + gammaIn n M p
  else
    vpSK n p hp + gammaOut n M p

/-- m_{K,M} = ∏_{p ≤ 2h} p^{−L_p(K,M)}（论文式 (5.2)），正有理数。
    非素数因子按 1 计。 -/
noncomputable def mKM (n M : ℕ) : ℚ :=
  ∏ p ∈ Finset.range (2 * hparam n + 1),
    if hp : p.Prime then (p : ℚ) ^ (-Lp n M p hp) else 1

/-- m_{K,M} > 0（论文式 (5.2) 后"This is a positive rational number"）。 -/
theorem mKM_pos (n M : ℕ) : 0 < mKM n M := by
  apply Finset.prod_pos
  intro p _
  by_cases hp : p.Prime
  · rw [dif_pos hp]
    exact zpow_pos (by exact_mod_cast hp.pos) _
  · rw [dif_neg hp]
    exact zero_lt_one

/-- Q_{K,M}(X) = m_{K,M} F_K(X)（论文式 (2.6)）。 -/
noncomputable def QKM (n M : ℕ) : ℚ[X] := Polynomial.C (mKM n M) * FK n

end Zeta5Irrational
