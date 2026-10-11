import Mathlib.LinearAlgebra.Matrix.Polynomial

/-!
Algebraic core of the stable-pencil certificate. Over any commutative coefficient
ring, B = A H gives det(A + X B) = det(A) Q(X) with Q(0) = 1.
For the application the coefficient ring is the p-integral rationals. The
Smith bounds proving that H is p-integral are not formalized in this file.
-/
namespace Zeta7.PencilFactorization

open Matrix Polynomial

variable {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]

theorem pencil_factor (A H : Matrix n n R) :
    det ((X : R[X]) • (A * H).map C + A.map C) =
      C (det A) * det ((X : R[X]) • H.map C + (1 : Matrix n n R).map C) := by
  have hmap : (A * H).map C = A.map C * H.map C := Matrix.map_mul
  have hone : (1 : Matrix n n R).map C = (1 : Matrix n n R[X]) := by simp
  rw [hmap, hone]
  rw [show (X : R[X]) • (A.map C * H.map C) + A.map C =
      A.map C * ((X : R[X]) • H.map C + 1) by
    rw [Matrix.mul_add, Matrix.mul_smul, Matrix.mul_one]]
  have hdet : det (A.map C) = C (det A) := (Polynomial.C.map_det A).symm
  rw [Matrix.det_mul, hdet]

theorem pencil_factor_constant_one (H : Matrix n n R) :
    (det ((X : R[X]) • H.map C + (1 : Matrix n n R).map C)).coeff 0 = 1 := by
  rw [Polynomial.coeff_det_X_add_C_zero, Matrix.det_one]

#print axioms pencil_factor
#print axioms pencil_factor_constant_one

end Zeta7.PencilFactorization
