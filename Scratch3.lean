import Mathlib
import Zeta5Irrational.Params
import Zeta5Irrational.Functional

open scoped Polynomial

namespace Zeta5Irrational

/-- 论文 §3 的线性泛函 L 的多项式核：L(x^k) = B_k（Bernoulli 数，B₁ = −1/2 约定）。
    x-世界（整数极点）τ-泛函的组成部分。 -/
noncomputable def bernoulliL (P : ℚ[X]) : ℚ :=
  ∑ k ∈ Finset.range (P.natDegree + 1), P.coeff k * bernoulli k

/-- 论文 §3 的 τ-泛函（多项式部分）：τ(P) = L(P‴)/24（论文："Let L(x^k) = B_k and
    τ(P) = L(P''')/24"）。对多项式取值为有理数。 -/
noncomputable def tauPoly (P : ℚ[X]) : ℚ := bernoulliL (Polynomial.derivative^[3] P) / 24

/-- 把 L 的求和扩展到任意足够大的范围。 -/
theorem bernoulliL_eq_sum_of_lt (P : ℚ[X]) {N : ℕ} (h : P.natDegree < N) :
    bernoulliL P = ∑ k ∈ Finset.range N, P.coeff k * bernoulli k := by
  unfold bernoulliL
  rw [Finset.sum_subset (Finset.range_mono (Nat.succ_le_of_lt h))
    (fun k _ hk => by
      have hk' : P.natDegree < k := by
        rw [Finset.mem_range] at hk
        omega
      rw [Polynomial.coeff_eq_zero_of_natDegree_lt hk', zero_mul])]

theorem bernoulliL_add (P Q : ℚ[X]) : bernoulliL (P + Q) = bernoulliL P + bernoulliL Q := by
  have hd : (P + Q).natDegree < max P.natDegree Q.natDegree + 1 :=
    lt_of_le_of_lt (Polynomial.natDegree_add_le P Q) (by omega)
  rw [bernoulliL_eq_sum_of_lt _ hd,
    bernoulliL_eq_sum_of_lt P (show P.natDegree < max P.natDegree Q.natDegree + 1 by omega),
    bernoulliL_eq_sum_of_lt Q (show Q.natDegree < max P.natDegree Q.natDegree + 1 by omega),
    Polynomial.coeff_add, add_mul, Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [add_mul]

theorem bernoulliL_smul (a : ℚ) (P : ℚ[X]) : bernoulliL (a • P) = a * bernoulliL P := by
  rw [bernoulliL_eq_sum_of_lt _ (lt_of_le_of_lt (Polynomial.natDegree_smul_le a P)
      (Nat.lt_succ_self _)), bernoulliL_eq_sum_of_lt _ (Nat.lt_succ_self _), Finset.mul_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Polynomial.coeff_smul, smul_eq_mul, mul_assoc]

theorem bernoulliL_sum (s : Finset ι) (f : ι → ℚ[X]) :
    bernoulliL (∑ i ∈ s, f i) = ∑ i ∈ s, bernoulliL (f i) := by
  classical
  induction s using Finset.induction with
  | empty => simp [bernoulliL]
  | insert a s ha ih => rw [Finset.sum_insert ha, Finset.sum_insert ha, bernoulliL_add, ih]

theorem bernoulliL_neg (P : ℚ[X]) : bernoulliL (-P) = -bernoulliL P := by
  have h : (-P : ℚ[X]) = (-1 : ℚ) • P := by simp
  rw [h, bernoulliL_smul, neg_one_mul]

theorem bernoulliL_sub (P Q : ℚ[X]) : bernoulliL (P - Q) = bernoulliL P - bernoulliL Q := by
  rw [sub_eq_add_neg, bernoulliL_add, bernoulliL_neg, ← sub_eq_add_neg]

theorem bernoulliL_C_mul (a : ℚ) (P : ℚ[X]) : bernoulliL (Polynomial.C a * P) = a * bernoulliL P := by
  rw [← Polynomial.smul_eq_C_mul, bernoulliL_smul]

theorem bernoulliL_X_pow (e : ℕ) : bernoulliL (Polynomial.X ^ e : ℚ[X]) = bernoulli e := by
  rw [bernoulliL, Polynomial.natDegree_X_pow, Finset.sum_eq_single e
    (fun b _ hbe => by simp [hbe])
    (fun h => absurd (Finset.mem_range.2 (by omega)) h)]
  simp

/-- umbral 求和：L((x+1)^m) = B_m + [m=1]（mathlib `sum_bernoulli`）。 -/
theorem bernoulliL_X_add_one_pow (m : ℕ) :
    bernoulliL ((Polynomial.X + 1 : ℚ[X]) ^ m) = bernoulli m + (if m = 1 then 1 else 0) := by
  rw [show (Polynomial.X + 1 : ℚ[X]) = Polynomial.X + Polynomial.C 1 by rw [Polynomial.C_1],
    add_pow, bernoulliL_sum]
  have hterm : ∀ k ∈ Finset.range (m + 1),
      bernoulliL ((Polynomial.X : ℚ[X]) ^ k * (Polynomial.C 1) ^ (m - k)
        * ((m.choose k : ℕ) : ℚ[X]))
        = ((m.choose k : ℕ) : ℚ) * bernoulli k := by
    intro k _
    have h1 : ((Polynomial.C 1 : ℚ[X]) ^ (m - k)) = 1 := by rw [Polynomial.C_1, one_pow]
    rw [h1, mul_one, mul_comm ((Polynomial.X : ℚ[X]) ^ k) ((m.choose k : ℕ) : ℚ[X]),
      ← Polynomial.C_eq_natCast, bernoulliL_C_mul, bernoulliL_X_pow]
  rw [Finset.sum_congr rfl hterm, Finset.sum_range_succ, sum_bernoulli]
  by_cases hm : m = 1
  · subst hm
    norm_num [bernoulli_one]
  · simp [hm]

/-- 复合求导（内函数导数为 1 的情形）。 -/
theorem derivative_comp_deriv_eq_one (q : ℚ[X]) (hq : Polynomial.derivative q = 1)
    (f : ℚ[X]) :
    Polynomial.derivative (f.comp q) = (Polynomial.derivative f).comp q := by
  rw [Polynomial.derivative_comp, hq, one_mul]

/-- (f(x+1))‴ = f‴(x+1)。 -/
theorem derivative_cube_comp_X_add_one (f : ℚ[X]) :
    Polynomial.derivative^[3] (f.comp (Polynomial.X + 1 : ℚ[X]))
      = (Polynomial.derivative^[3] f).comp (Polynomial.X + 1 : ℚ[X]) := by
  have hq : Polynomial.derivative (Polynomial.X + 1 : ℚ[X]) = 1 := by
    rw [show (Polynomial.X + 1 : ℚ[X]) = Polynomial.X + Polynomial.C 1 by rw [Polynomial.C_1],
      Polynomial.derivative_X_add_C]
  have h : ∀ g : ℚ[X],
      Polynomial.derivative (g.comp (Polynomial.X + 1 : ℚ[X]))
        = (Polynomial.derivative g).comp (Polynomial.X + 1 : ℚ[X]) :=
    fun g => derivative_comp_deriv_eq_one _ hq g
  simp only [Function.iterate_succ_apply, Function.iterate_zero, h]

/-- X^e 的 k 阶导数：下降阶乘系数。 -/
theorem iterate_derivative_X_pow (k e : ℕ) :
    Polynomial.derivative^[k] (Polynomial.X ^ e : ℚ[X])
      = Polynomial.C ((∏ i ∈ Finset.range k, (e - i) : ℕ) : ℚ) * Polynomial.X ^ (e - k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply', ← ih, Polynomial.derivative_C_mul,
      Polynomial.derivative_X_pow, ← Polynomial.C_mul, Finset.prod_range_succ, Nat.cast_mul]
    congr 1
    · rfl
    · congr 1
      omega

/-- 单项式版的式 (3.3)：τ((x+1)^e − x^e) = (x^e)⁗(0)/24 = [e=4]。 -/
theorem tauPoly_X_add_one_pow_sub (e : ℕ) :
    tauPoly ((Polynomial.X + 1 : ℚ[X]) ^ e - Polynomial.X ^ e)
      = (Polynomial.derivative^[4] (Polynomial.X ^ e : ℚ[X])).eval 0 / 24 := by
  rw [tauPoly, Polynomial.iterate_derivative_sub]
  have hcomp : ((Polynomial.X + 1 : ℚ[X]) ^ e) = (Polynomial.X ^ e).comp (Polynomial.X + 1) := by
    rw [Polynomial.pow_comp, Polynomial.X_comp]
  rw [hcomp, derivative_cube_comp_X_add_one, iterate_derivative_X_pow, Polynomial.mul_comp,
    Polynomial.C_comp, Polynomial.pow_comp, Polynomial.X_comp, iterate_derivative_X_pow,
    bernoulliL_sub, bernoulliL_C_mul, bernoulliL_C_mul, bernoulliL_X_add_one_pow,
    bernoulliL_X_pow, iterate_derivative_X_pow, Polynomial.eval_mul, Polynomial.eval_C,
    Polynomial.eval_pow, Polynomial.eval_X]
  by_cases he4 : e = 4
  · subst he4
    norm_num [bernoulli_one]
  · rw [if_neg (by omega : e - 3 ≠ 1), if_neg he4, add_zero, sub_self, zero_div, mul_zero]
    rcases Nat.lt_or_ge e 4 with h | h
    · rw [show ((∏ i ∈ Finset.range 4, (e - i) : ℕ) : ℚ) = 0 by
        have hz : (∏ i ∈ Finset.range 4, (e - i) : ℕ) = 0 := by
          interval_cases e <;> norm_num [Finset.prod_range_succ]
        exact Nat.cast_eq_zero.2 hz, mul_zero, zero_div]
    · rw [zero_pow (by omega : e - 4 ≠ 0), mul_zero, zero_div]

/-- 单项式版的式 (3.2)：τ((−1−x)^e) = −τ(x^e)。 -/
theorem tauPoly_neg_one_mul_X_add_one_pow (e : ℕ) :
    tauPoly ((Polynomial.C (-1) * (Polynomial.X + 1) : ℚ[X]) ^ e) = - tauPoly (Polynomial.X ^ e) := by
  rw [tauPoly, tauPoly, mul_pow, Polynomial.C_pow, ← Polynomial.smul_eq_C_mul,
    Polynomial.iterate_derivative_smul, bernoulliL_smul,
    show ((Polynomial.X + 1 : ℚ[X]) ^ e) = (Polynomial.X ^ e).comp (Polynomial.X + 1) by
      rw [Polynomial.pow_comp, Polynomial.X_comp],
    derivative_cube_comp_X_add_one, iterate_derivative_X_pow, Polynomial.mul_comp,
    Polynomial.C_comp, Polynomial.pow_comp, Polynomial.X_comp, iterate_derivative_X_pow,
    bernoulliL_C_mul, bernoulliL_X_add_one_pow, bernoulliL_C_mul, bernoulliL_X_pow]
  rcases Nat.lt_or_ge e 3 with h3 | h3
  · rw [show ((∏ i ∈ Finset.range 3, (e - i) : ℕ) : ℚ) = 0 by
      have hz : (∏ i ∈ Finset.range 3, (e - i) : ℕ) = 0 := by
        interval_cases e <;> norm_num [Finset.prod_range_succ]
      exact Nat.cast_eq_zero.2 hz, zero_mul, mul_zero, mul_zero, zero_div, neg_zero]
  · rcases Nat.lt_or_ge e 5 with h5 | h5
    · interval_cases e
      · norm_num [bernoulli_zero]
      · norm_num [bernoulli_one]
    · rw [if_neg (by omega : e ≠ 4), if_neg (by omega : e - 3 ≠ 1), add_zero]
      rcases Nat.even_or_odd e with he | ho
      · rw [he.neg_one_pow]
        have hb : bernoulli (e - 3) = 0 :=
          bernoulli_eq_zero_of_odd (by obtain ⟨k, hk⟩ := he; exact ⟨k - 2, by omega⟩)
            (by omega)
        rw [hb]
        ring
      · rw [ho.neg_one_pow]
        ring

theorem tauPoly_C_mul (a : ℚ) (P : ℚ[X]) : tauPoly (Polynomial.C a * P) = a * tauPoly P := by
  rw [tauPoly, Polynomial.iterate_derivative_C_mul, bernoulliL_C_mul, tauPoly, mul_div_assoc]

theorem tauPoly_sum (s : Finset ι) (f : ι → ℚ[X]) :
    tauPoly (∑ i ∈ s, f i) = ∑ i ∈ s, tauPoly (f i) := by
  rw [tauPoly, Polynomial.iterate_derivative_sum, bernoulliL_sum, Finset.sum_div]

/-- 论文式 (3.3) 的多项式版（τ-泛函；μ-版不成立，见 `eq_3_3_false` 与 doc）：
    τ(P(x+1) − P(x)) = P⁗(0)/24。 -/
theorem eq_3_3_poly (P : ℚ[X]) :
    tauPoly (P.comp (Polynomial.X + 1) - P) = (Polynomial.derivative^[4] P).eval 0 / 24 := by
  classical
  have hsplit : (∑ e ∈ Finset.range (P.natDegree + 1), Polynomial.C (P.coeff e)
        * Polynomial.X ^ e : ℚ[X]).comp (Polynomial.X + 1) - P
      = ∑ e ∈ Finset.range (P.natDegree + 1),
        (Polynomial.C (P.coeff e) * (Polynomial.X + 1) ^ e
          - Polynomial.C (P.coeff e) * Polynomial.X ^ e) := by
    rw [P.as_sum_range, Polynomial.sum_comp, Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun e _ => ?_
    simp only [Polynomial.mul_comp, Polynomial.C_comp, Polynomial.pow_comp, Polynomial.X_comp]
  rw [P.as_sum_range, hsplit, tauPoly_sum, Polynomial.iterate_derivative_sum,
    Polynomial.eval_finsetSum, Finset.sum_div]
  refine Finset.sum_congr rfl fun e _ => ?_
  rw [mul_sub, tauPoly_C_mul, tauPoly_C_mul, tauPoly_X_add_one_pow_sub, mul_div_assoc]

/-- 论文式 (3.2) 的多项式版（τ-泛函；μ-版不成立，见 doc）：
    τ(P(−1−x)) = −τ(P)。 -/
theorem eq_3_2_poly (P : ℚ[X]) :
    tauPoly (P.comp (Polynomial.C (-1) * Polynomial.X + Polynomial.C (-1))) = - tauPoly P := by
  classical
  rw [P.as_sum_range, Polynomial.sum_comp, tauPoly_sum, tauPoly_sum,
    ← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun e _ => ?_
  simp only [Polynomial.mul_comp, Polynomial.C_comp, Polynomial.pow_comp, Polynomial.X_comp]
  rw [show (Polynomial.C (-1) * Polynomial.X + Polynomial.C (-1) : ℚ[X])
      = Polynomial.C (-1) * (Polynomial.X + 1) by ring, tauPoly_C_mul, tauPoly_C_mul,
    tauPoly_neg_one_mul_X_add_one_pow]

end Zeta5Irrational
