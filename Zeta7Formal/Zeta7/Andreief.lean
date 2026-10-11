import Mathlib

/-!
# Andréief 恒等式

对可积的 `f i, g j : ℝ → ℝ`，
`det (∫ f i g j dμ) = (1/n!) ∫ det (f i (x j)) det (g i (x j)) dμⁿ(x)`。
即论文 (6.10) 的 Hankel 行列式形式。镜像 `Apery/Andreief.lean`（b-无关）。
-/

open MeasureTheory Finset Equiv

namespace Zeta7

variable {n : ℕ} {μ : Measure ℝ} [SigmaFinite μ]

/-- 坐标重排 `x ↦ (i ↦ x (τ i))` 的可测等价。 -/
noncomputable def permEquiv (τ : Perm (Fin n)) : (Fin n → ℝ) ≃ᵐ (Fin n → ℝ) :=
  MeasurableEquiv.arrowCongr' τ.symm (MeasurableEquiv.refl ℝ)

lemma permEquiv_apply (τ : Perm (Fin n)) (x : Fin n → ℝ) (i : Fin n) :
    permEquiv τ x i = x (τ i) := by
  simp [permEquiv, MeasurableEquiv.arrowCongr', Equiv.arrowCongr']

lemma measurePreserving_permEquiv (τ : Perm (Fin n)) :
    MeasurePreserving (permEquiv τ) (Measure.pi fun _ : Fin n => μ) (Measure.pi fun _ : Fin n => μ) :=
  measurePreserving_arrowCongr' (fun _ : Fin n => μ) (fun _ : Fin n => μ) τ.symm (MeasurableEquiv.refl ℝ)
    (fun _ => ⟨(MeasurableEquiv.refl ℝ).measurable, Measure.map_id⟩)

/-- 基本积分 `I(ρ) = ∫ ∏ᵢ f (ρ i) (xᵢ) g i (xᵢ)`。 -/
noncomputable def andreiefI (f g : Fin n → ℝ → ℝ) (ρ : Perm (Fin n)) : ℝ :=
  ∫ x : Fin n → ℝ, ∏ i, f (ρ i) (x i) * g i (x i) ∂(Measure.pi fun _ : Fin n => μ)

lemma integral_prod_prod_eq (f g : Fin n → ℝ → ℝ) (σ τ : Perm (Fin n)) :
    ∫ x : Fin n → ℝ, (∏ i, f (σ i) (x i)) * (∏ i, g (τ i) (x i)) ∂(Measure.pi fun _ : Fin n => μ) =
      andreiefI (μ := μ) f g (σ * τ⁻¹) := by
  unfold andreiefI
  have hpt : ∀ x : Fin n → ℝ, (∏ i, f (σ i) (x i)) * (∏ i, g (τ i) (x i)) =
      (fun y : Fin n → ℝ => ∏ k, f ((σ * τ⁻¹) k) (y k) * g k (y k)) (permEquiv τ⁻¹ x) := by
    intro x
    simp only [permEquiv_apply, ← Finset.prod_mul_distrib]
    rw [← Equiv.prod_comp τ (fun k => f ((σ * τ⁻¹) k) (x (τ⁻¹ k)) * g k (x (τ⁻¹ k)))]
    refine Finset.prod_congr rfl fun i _ => ?_
    simp [Perm.mul_apply]
  simp_rw [hpt]
  exact (measurePreserving_permEquiv (μ := μ) τ⁻¹).integral_comp (permEquiv τ⁻¹).measurableEmbedding
    (fun y : Fin n → ℝ => ∏ k, f ((σ * τ⁻¹) k) (y k) * g k (y k))

/-- **Andréief 恒等式**。 -/
theorem andreief (f g : Fin n → ℝ → ℝ) (hfg : ∀ i j, Integrable (fun x => f i x * g j x) μ) :
    (Matrix.of fun i j => ∫ x, f i x * g j x ∂μ).det =
      (1 / (n.factorial : ℝ)) * ∫ x : Fin n → ℝ,
        (Matrix.of fun i j => f i (x j)).det * (Matrix.of fun i j => g i (x j)).det
          ∂(Measure.pi fun _ : Fin n => μ) := by
  -- 左端写成基本积分的置换和
  have hL : (Matrix.of fun i j => ∫ x, f i x * g j x ∂μ).det =
      ∑ ρ : Perm (Fin n), (Perm.sign ρ : ℝ) * andreiefI (μ := μ) f g ρ := by
    rw [Matrix.det_apply']
    refine Finset.sum_congr rfl fun ρ _ => ?_
    simp only [Matrix.of_apply, andreiefI]
    rw [integral_fintype_prod_eq_prod (fun i x => f (ρ i) x * g i x)]
  -- 右端
  have hint : ∀ σ τ : Perm (Fin n), Integrable
      (fun x : Fin n → ℝ => (Perm.sign σ : ℝ) * (Perm.sign τ : ℝ) *
        ((∏ i, f (σ i) (x i)) * (∏ i, g (τ i) (x i)))) (Measure.pi fun _ : Fin n => μ) := by
    intro σ τ
    have : (fun x : Fin n → ℝ => (∏ i, f (σ i) (x i)) * (∏ i, g (τ i) (x i))) =
        fun x => ∏ i, (fun i y => f (σ i) y * g (τ i) y) i (x i) := by
      funext x; simp only [← Finset.prod_mul_distrib]
    refine Integrable.const_mul ?_ _
    rw [this]
    exact Integrable.fintype_prod fun i => hfg (σ i) (τ i)
  have hR : ∫ x : Fin n → ℝ,
      (Matrix.of fun i j => f i (x j)).det * (Matrix.of fun i j => g i (x j)).det
        ∂(Measure.pi fun _ : Fin n => μ) =
      ∑ τ : Perm (Fin n), ∑ σ : Perm (Fin n), (Perm.sign σ : ℝ) * (Perm.sign τ : ℝ) *
        andreiefI (μ := μ) f g (σ * τ⁻¹) := by
    have hpt : ∀ x : Fin n → ℝ,
        (Matrix.of fun i j => f i (x j)).det * (Matrix.of fun i j => g i (x j)).det =
        ∑ τ : Perm (Fin n), ∑ σ : Perm (Fin n), (Perm.sign σ : ℝ) * (Perm.sign τ : ℝ) *
          ((∏ i, f (σ i) (x i)) * (∏ i, g (τ i) (x i))) := by
      intro x
      rw [Matrix.det_apply', Matrix.det_apply', Finset.sum_mul_sum, Finset.sum_comm]
      refine Finset.sum_congr rfl fun τ _ => Finset.sum_congr rfl fun σ _ => ?_
      simp only [Matrix.of_apply]
      ring
    simp_rw [hpt]
    rw [integral_finsetSum _ (fun τ _ => integrable_finsetSum _ (fun σ _ => hint σ τ))]
    refine Finset.sum_congr rfl fun τ _ => ?_
    rw [integral_finsetSum _ (fun σ _ => hint σ τ)]
    refine Finset.sum_congr rfl fun σ _ => ?_
    rw [integral_const_mul, integral_prod_prod_eq]
  -- 每个内和等于左端
  have hsign : ∀ σ τ : Perm (Fin n),
      (Perm.sign (σ * τ⁻¹) : ℝ) = (Perm.sign σ : ℝ) * (Perm.sign τ : ℝ) := by
    intro σ τ
    rw [Perm.sign_mul, Perm.sign_inv]
    push_cast
    ring
  have hinner : ∀ τ : Perm (Fin n), ∑ σ : Perm (Fin n), (Perm.sign σ : ℝ) * (Perm.sign τ : ℝ) *
      andreiefI (μ := μ) f g (σ * τ⁻¹) =
      ∑ ρ : Perm (Fin n), (Perm.sign ρ : ℝ) * andreiefI (μ := μ) f g ρ := by
    intro τ
    conv_rhs => rw [← Equiv.sum_comp (Equiv.mulRight τ⁻¹)]
    refine Finset.sum_congr rfl fun σ _ => ?_
    simp only [Equiv.coe_mulRight]
    rw [hsign]
  rw [hR]
  simp_rw [hinner]
  rw [Finset.sum_const, Finset.card_univ, Fintype.card_perm, Fintype.card_fin, nsmul_eq_mul, hL]
  have : (n.factorial : ℝ) ≠ 0 := by positivity
  field_simp
  try ring

end Zeta7
