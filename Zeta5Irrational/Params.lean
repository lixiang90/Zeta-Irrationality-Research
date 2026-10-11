import Mathlib

/-!
# 参数与基础定义（论文 §2.1）

对应论文 *ZETA5 IS IRRATIONAL* 式 (2.1)–(2.3)。
-/

open scoped Polynomial

namespace Zeta5Irrational

/-- K = 40n（论文式 (2.1)）。 -/
def Kparam (n : ℕ) : ℕ := 40 * n

/-- N = 3n（论文式 (2.1)）。 -/
def Nparam (n : ℕ) : ℕ := 3 * n

/-- h = 37n（论文式 (2.1)）。 -/
def hparam (n : ℕ) : ℕ := 37 * n

/-- α = 3/40（论文式 (2.1)）。 -/
def alphaP : ℚ := 3 / 40

/-- λ = 37/40（论文式 (2.1)）。 -/
def lambdaP : ℚ := 37 / 40

/-- H = 1 + 2α = 23/20（论文式 (2.1)）。 -/
def Hparam : ℚ := 23 / 20

/-- D_m(t) = ∏_{j=1}^{m} (t + j²)，D_0 = 1（论文式 (2.2)，作为 ℚ 上多项式）。 -/
noncomputable def D (m : ℕ) : ℚ[X] :=
  (Finset.Icc 1 m).prod fun j => Polynomial.X + Polynomial.C ((j : ℚ) ^ 2)

/-- H_j⁽⁵⁾ = ∑_{v=1}^{j} 1/v⁵，H_0 = 0（论文式 (2.2)）。 -/
def harm5 (j : ℕ) : ℚ :=
  (Finset.Icc 1 j).sum fun v => (1 : ℚ) / (v : ℚ) ^ 5

/-- H_0⁽⁵⁾ = 0。 -/
theorem harm5_zero : harm5 0 = 0 := by simp [harm5]

/-- Bernoulli 数约定 B₁ = −1/2（与 mathlib 的 `bernoulli` 约定一致，论文 §2.1）。 -/
theorem bernoulli_one_eq : bernoulli 1 = -1 / 2 := by
  norm_num [bernoulli]

/-- S_K = (K!)^{2h} 4^{h−1} / [ (N!)^{12h} ∏_{i=1}^{h−1} ((2i)!)² ]（论文式 (2.5)）。

注意 4^{h−1} 以 ℚ 上整数幂（zpow）写出，h = 0 时为占位值；所有定理均设 n ≥ 1。 -/
def SK (n : ℕ) : ℚ :=
  (Nat.factorial (Kparam n)) ^ (2 * hparam n) *
    (4 : ℚ) ^ ((hparam n : ℤ) - 1) /
      ((Nat.factorial (Nparam n)) ^ (12 * hparam n) *
        (∏ i ∈ Finset.Icc 1 (hparam n - 1), ((Nat.factorial (2 * i)) ^ 2 : ℚ)))

/-- I_out = 127751/96000（论文式 (5.10)，Table 4 仿射分段积分之和）。 -/
def Iout : ℚ := 127751 / 96000

/-- A_*（论文式 (5.19)）。 -/
def Astar : ℚ := 9928298118277006344769 / 7535670527041937280000

/-- A_M = A_* + 7λ/M − (2923/240 − 1/4)/M² + 32/M³（论文式 (5.20)）。 -/
def AM (M : ℕ) : ℚ :=
  Astar + 7 * lambdaP / (M : ℚ) - (2923 / 240 - 1 / 4) / (M : ℚ) ^ 2 +
    32 / (M : ℚ) ^ 3

/-- Ū = −2733991/2000000（论文式 (6.4)）。 -/
def Ubar : ℚ := -2733991 / 2000000

/-- M₀ = −1329/200（论文式 (6.2)）。 -/
def M₀ : ℚ := -1329 / 200

/-- C_* = −2λ + 12αλ(1 − log α) + 3λ² − 2λ² log(2λ)（论文式 (6.3)，实数形式）。 -/
noncomputable def Cstar : ℝ :=
  -2 * (lambdaP : ℝ) + 12 * (alphaP : ℝ) * (lambdaP : ℝ) * (1 - Real.log alphaP) +
    3 * (lambdaP : ℝ) ^ 2 - 2 * (lambdaP : ℝ) ^ 2 * Real.log (2 * (lambdaP : ℝ))

/-- ϱ = 6933/500（论文式 (C.1)）。 -/
def rhoC : ℚ := 6933 / 500

/-- ε = 79/1600（论文式 (C.7)）。 -/
def epsC : ℚ := 79 / 1600

/-- c = 75/4（论文 Appendix C.2）。 -/
def cC : ℚ := 75 / 4

end Zeta5Irrational
