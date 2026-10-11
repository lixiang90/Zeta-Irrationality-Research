import Mathlib
import Zeta7.Andreief
import Zeta7.Positivity

/-!
# Hankel 行列式的多重积分表示，(6.10)

`Δ_K(ζ(7)) = (1/h!) ∫_{(0,∞)^h} det(V(y))² ∏ᵢ ν(yᵢ) dy`，其中 `V(y)` 是
`y₁², …, y_h²` 的 Vandermonde 矩阵，`ν(y) = D_n(y²)⁸ / D_{40n}(y²) · w(y)`（b=8 故幂次 8；(K:N:h) = 40:1:39）。
-/

open MeasureTheory Set Finset Polynomial

namespace Zeta7

/-- `(0, ∞)` 上的测度 `dy`。 -/
noncomputable abbrev μpos : Measure ℝ := volume.restrict (Ioi 0)

/-- **(6.10)**：Hankel 行列式的多重积分表示。 -/
theorem Δ_eq_integral (n : ℕ) :
    aeval zeta7 (Δ n) = (1 / ((39 * n).factorial : ℝ)) *
      ∫ x : Fin (39 * n) → ℝ, (Matrix.vandermonde fun j => x j ^ 2).det ^ 2 * ∏ j, ν n (x j)
        ∂(Measure.pi fun _ : Fin (39 * n) => μpos) := by
  -- 矩阵 `G_K(ζ(7))` 的条目为 `∫ (y²)^i · ((y²)^j ν(y)) dy`
  have hdet : aeval zeta7 (Δ n) = ((G n).map (aeval zeta7)).det := by
    have := RingHom.map_det (aeval zeta7 : ℚ[X] →ₐ[ℚ] ℝ).toRingHom (G n)
    simpa [Δ, RingHom.mapMatrix_apply] using this
  set f : Fin (39 * n) → ℝ → ℝ := fun i y => (y ^ 2) ^ (i : ℕ) with hf
  set g : Fin (39 * n) → ℝ → ℝ := fun j y => (y ^ 2) ^ (j : ℕ) * ν n y with hg
  have hentry : (G n).map (aeval zeta7) = Matrix.of fun i j => ∫ y, f i y * g j y ∂μpos := by
    ext i j
    simp only [Matrix.map_apply, Matrix.of_apply, G, hf, hg]
    rw [(moment_rep _ _).2]
    refine setIntegral_congr_fun measurableSet_Ioi fun y _ => ?_
    rw [integrand_eq]; ring
  have hfg : ∀ i j, Integrable (fun y => f i y * g j y) μpos := by
    intro i j
    have := (moment_rep (40 * n) (D n ^ 8 * X ^ ((i : ℕ) + (j : ℕ)))).1
    refine this.congr_fun (fun y _ => ?_) measurableSet_Ioi
    simp only [hf, hg]; rw [integrand_eq]; ring
  rw [hdet, hentry, andreief f g hfg]
  congr 1
  refine integral_congr_ae (Filter.Eventually.of_forall fun x => ?_)
  -- `det (f i (x j)) = det Vᵀ` 且 `det (g i (x j)) = (∏ ν) det Vᵀ`
  have h1 : (Matrix.of fun i j => f i (x j)).det = (Matrix.vandermonde fun j => x j ^ 2).det := by
    rw [← Matrix.det_transpose (Matrix.vandermonde _)]
    refine congrArg Matrix.det ?_
    ext i j; simp [hf, Matrix.vandermonde, Matrix.transpose_apply]
  have h2 : (Matrix.of fun i j => g i (x j)).det =
      (∏ j, ν n (x j)) * (Matrix.vandermonde fun j => x j ^ 2).det := by
    have : (Matrix.of fun i j => g i (x j)) =
        Matrix.of fun i j => ν n (x j) * (Matrix.of fun i j => f i (x j)) i j := by
      ext i j; simp [hf, hg]; ring
    rw [this, Matrix.det_mul_row, h1]
  show (Matrix.of fun i j => f i (x j)).det * (Matrix.of fun i j => g i (x j)).det =
    (Matrix.vandermonde fun j => x j ^ 2).det ^ 2 * ∏ j, ν n (x j)
  rw [h1, h2]; ring

end Zeta7
