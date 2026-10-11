import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Degree.Support
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.RingTheory.PowerSeries.WellKnown
import Mathlib.RingTheory.PowerSeries.Exp
import Mathlib.RingTheory.PowerSeries.NoZeroDivisors
import Mathlib.Tactic
import Zeta7.Tau

/-!
# ζ(7) 形式化：b=8 分布恒等式（多项式版，构造适用形）

研究侧推导见 `research/b8_arithmetic.md` §B2（严格证明 + `b8_distribution.py`
精确有理验证 3200 例零违规）。要点：
- **命题 1**（生成函数）：Σ_{a=0}^{p−1} e^{at}F₀(pt) = p⁶F₀(t)（F₀ 为 B₁=−1/2
  的 EGF），对任意正整数 p 由几何和恒等式严格推出。
- **命题 2**（系数比较）：τ⁻(g) = p^{−6}Σ_a τ⁻(g(a+pX)) 对一切 g ∈ ℚ[X] 成立。
- **推论**（构造适用版）：奇 g（pullback 像 x⁷R(−x²) 全在此列）的 τ 值
  约定无关，故 p⁶·τ(g) = Σ_a τ⁻(g(a+pX))（RHS 用 minus 约定）。
  【约定陷阱】plus 约定的修正项 c6(g) − Σ_{n≥6}C(n,6)S_{n−6}(p)c_n(g)
  对奇 g 一般不消失（g = x⁷, p = 2 给 −7），分布步骤必须钉死 minus 约定。
-/

namespace Zeta7

open BigOperators
open scoped Polynomial

/-- minus 约定的 κ：κ⁻_m = κ⁺_m − [m=6]（κ⁺ 即 `kappa`，B₁=+1/2）。 -/
def kappaMinus (m : ℕ) : ℚ := kappa m - (if m = 6 then 1 else 0)

/-- τ₈ 在 ℚ[X] 上的线性扩张（plus 约定；与 `kappa` 一致）。 -/
def tauPoly (g : ℚ[X]) : ℚ := ∑ i ∈ g.support, g.coeff i * kappa i

/-- τ₈ 在 ℚ[X] 上的线性扩张（minus 约定，分布步骤用）。 -/
def tauPolyMinus (g : ℚ[X]) : ℚ := ∑ i ∈ g.support, g.coeff i * kappaMinus i

/-- 自代数映射是恒等（`algebraMap ℚ ℚ x = x`，定义上成立）。 -/
theorem algebraMap_rat_rat (x : ℚ) : algebraMap ℚ ℚ x = x := rfl

open scoped PowerSeries

/-- **minus 约定函数方程**：`B⁻(t) := Σ κ⁻_m tᵐ/m!` 满足
`720 · B⁻ · (e^t − 1) = t⁶`。由 plus 约定 `kappa_egf_mul_exp`
（720·F⁺(e^t−1) = t⁶e^t）与 κ⁻ = κ⁺ − [·=6]t⁶/720 的平移消去 e^t 项。 -/
theorem kappaMinus_egf_mul_exp : PowerSeries.C (720 : ℚ) *
    (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial) *
      (PowerSeries.exp ℚ - 1))
    = (PowerSeries.X : ℚ⟦X⟧) ^ 6 := by
  have hsplit : PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)
      = PowerSeries.mk (fun m => (kappa m : ℚ) / m.factorial)
        - PowerSeries.C (1 / 720 : ℚ) * (PowerSeries.X : ℚ⟦X⟧) ^ 6 := by
    ext m
    rw [PowerSeries.coeff_mk, map_sub, PowerSeries.coeff_mk,
      PowerSeries.coeff_C_mul, PowerSeries.coeff_X_pow, mul_ite, mul_one, mul_zero]
    by_cases hm : m = 6
    · subst hm
      unfold kappaMinus
      rw [if_pos rfl, if_pos rfl, sub_div]
      norm_num
    · unfold kappaMinus
      rw [if_neg hm, if_neg hm, sub_zero, sub_zero]
  rw [hsplit, sub_mul, mul_sub,
    ← mul_assoc (PowerSeries.C (720 : ℚ))
      (PowerSeries.C (1 / 720 : ℚ) * (PowerSeries.X : ℚ⟦X⟧) ^ 6),
    ← mul_assoc (PowerSeries.C (720 : ℚ)) (PowerSeries.C (1 / 720 : ℚ))]
  have e1 : PowerSeries.C (720 : ℚ) * PowerSeries.C (1 / 720 : ℚ) = 1 := by
    rw [← map_mul, show (720 : ℚ) * (1 / 720) = 1 by norm_num, map_one]
  rw [e1, one_mul, kappa_egf_mul_exp]
  have e2 : (PowerSeries.X : ℚ⟦X⟧) ^ 5 * (PowerSeries.X * PowerSeries.exp ℚ)
      = (PowerSeries.X : ℚ⟦X⟧) ^ 6 * PowerSeries.exp ℚ := by
    rw [← mul_assoc, ← pow_succ]
  rw [e2, ← mul_sub, sub_sub_self, mul_one]

/-- **标度版函数方程**（rescale 环同态纯运算推出，无需代入理论）：
`720 · B⁻(pt) · (e^{pt} − 1) = (pt)⁶`。 -/
theorem kappaMinus_egf_mul_exp_scaled (p : ℕ) :
    PowerSeries.C (720 : ℚ) *
      (PowerSeries.rescale (p : ℚ)
          (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
        ((PowerSeries.exp ℚ) ^ p - 1))
    = (PowerSeries.C (p : ℚ) * (PowerSeries.X : ℚ⟦X⟧)) ^ 6 := by
  have rC : ∀ c : ℚ, PowerSeries.rescale (p : ℚ) (PowerSeries.C c)
      = PowerSeries.C c := by
    intro c
    ext n
    simp only [PowerSeries.coeff_rescale, PowerSeries.coeff_C, mul_ite, mul_zero]
    rcases n with _ | n <;> simp
  have h := congr_arg (PowerSeries.rescale (p : ℚ)) kappaMinus_egf_mul_exp
  rw [map_mul, map_mul, map_sub, map_one, map_pow, rC,
    (PowerSeries.exp_pow_eq_rescale_exp p).symm, PowerSeries.rescale_X] at h
  exact h

/-- **级数分布恒等式**：`B⁻(pt) · Σ_{a<p} e^{at} = p⁶ · B⁻`。
证明：两边乘 (e^t−1)，LHS 用几何和坍缩为 B⁻(pt)(e^{pt}−1)（标度方程），
RHS 用 minus 函数方程；再在整环 ℚ⟦X⟧ 中消去 C 720 与 (e^t−1)。 -/
theorem distribution_series (p : ℕ) (hp : 0 < p) :
    PowerSeries.rescale (p : ℚ)
        (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
      (∑ a ∈ Finset.range p, (PowerSeries.exp ℚ) ^ a)
    = PowerSeries.C ((p : ℚ) ^ 6) *
      PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial) := by
  have hgeom : (∑ a ∈ Finset.range p, (PowerSeries.exp ℚ) ^ a) * (PowerSeries.exp ℚ - 1)
      = (PowerSeries.exp ℚ) ^ p - 1 := by
    rw [geom_sum_mul]
  have hexp1 : (PowerSeries.exp ℚ - 1) ≠ 0 := by
    intro h
    have hc := congr_arg (PowerSeries.coeff 1) h
    rw [map_sub, PowerSeries.coeff_exp, algebraMap_rat_rat] at hc
    simp at hc
  have e2 : PowerSeries.C (720 : ℚ) *
      (PowerSeries.rescale (p : ℚ)
          (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
        ((PowerSeries.exp ℚ) ^ p - 1))
    = PowerSeries.C (720 : ℚ) *
      (PowerSeries.C ((p : ℚ) ^ 6) *
        (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial) *
          (PowerSeries.exp ℚ - 1))) := by
    rw [kappaMinus_egf_mul_exp_scaled]
    have h3 : (PowerSeries.C (p : ℚ) * (PowerSeries.X : ℚ⟦X⟧)) ^ 6
        = PowerSeries.C ((p : ℚ) ^ 6) * (PowerSeries.X : ℚ⟦X⟧) ^ 6 := by
      rw [mul_pow, ← map_pow]
    rw [h3, ← kappaMinus_egf_mul_exp]
    ring
  have h720 : (PowerSeries.C (720 : ℚ) : ℚ⟦X⟧) ≠ 0 := by
    intro h
    have hc := congr_arg PowerSeries.constantCoeff h
    rw [PowerSeries.constantCoeff_C, PowerSeries.constantCoeff_zero] at hc
    norm_num at hc
  have e3 : PowerSeries.rescale (p : ℚ)
        (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
      ((PowerSeries.exp ℚ) ^ p - 1)
    = PowerSeries.C ((p : ℚ) ^ 6) *
      (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial) *
        (PowerSeries.exp ℚ - 1)) :=
    mul_left_cancel₀ h720 e2
  have e4 : (PowerSeries.rescale (p : ℚ)
        (PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
      (∑ a ∈ Finset.range p, (PowerSeries.exp ℚ) ^ a)) * (PowerSeries.exp ℚ - 1)
    = (PowerSeries.C ((p : ℚ) ^ 6) *
        PowerSeries.mk (fun m => (kappaMinus m : ℚ) / m.factorial)) *
      (PowerSeries.exp ℚ - 1) := by
    rw [mul_assoc, hgeom, e3, ← mul_assoc]
  exact mul_right_cancel₀ hexp1 e4

/-- **幂和分布恒等式**（系数比较）：记 `S_p(k) = Σ_{a<p} a^k`（S_p(0) = p），
`Σ_{j≤m} C(m,j) p^j κ⁻_j S_p(m−j) = p⁶ κ⁻_m`。
证明：`distribution_series` 取系数 m，逐项用 `C(m,j)·j!·(m−j)! = m!`
归并阶乘。 -/
theorem distribution_power_sum (p : ℕ) (hp : 0 < p) (m : ℕ) :
    (∑ j ∈ Finset.range (m + 1), (Nat.choose m j : ℚ) * ((p : ℚ) ^ j * kappaMinus j)
      * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j)))
    = (p : ℚ) ^ 6 * kappaMinus m := by
  have hser := congr_arg (PowerSeries.coeff m) (distribution_series p hp)
  rw [PowerSeries.coeff_mul, PowerSeries.coeff_C_mul, PowerSeries.coeff_mk,
    Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk] at hser
  simp only [PowerSeries.coeff_rescale, PowerSeries.coeff_mk,
    PowerSeries.exp_pow_eq_rescale_exp, PowerSeries.coeff_exp, algebraMap_rat_rat,
    map_sum] at hser
  have hm0 : (m.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero m
  have key : ∀ j ∈ Finset.range (m + 1),
      ((Nat.choose m j : ℚ) * ((p : ℚ) ^ j * kappaMinus j)
        * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j)))
      = (((p : ℚ) ^ j * (kappaMinus j / j.factorial))
        * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j) * (1 / (m - j).factorial)))
        * (m.factorial : ℚ) := by
    intro j hj
    rw [Finset.mem_range] at hj
    have hjm : j ≤ m := Nat.lt_succ_iff.mp hj
    have hchooseq : ((Nat.choose m j : ℕ) : ℚ) * (j.factorial : ℚ)
        * ((m - j).factorial : ℚ) = (m.factorial : ℚ) := by
      exact_mod_cast Nat.choose_mul_factorial_mul_factorial hjm
    have hf1 : (j.factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero j
    have hf2 : ((m - j).factorial : ℚ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero _
    rw [hchooseq.symm]
    have hS : (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j) * (1 / (m - j).factorial))
        = (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j)) * (1 / (m - j).factorial) := by
      rw [Finset.sum_mul]
    rw [hS]
    field_simp
  calc (∑ j ∈ Finset.range (m + 1), (Nat.choose m j : ℚ) * ((p : ℚ) ^ j * kappaMinus j)
        * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j)))
      = ∑ j ∈ Finset.range (m + 1),
        (((p : ℚ) ^ j * (kappaMinus j / j.factorial))
          * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j) * (1 / (m - j).factorial)))
          * (m.factorial : ℚ) := Finset.sum_congr rfl key
    _ = (∑ j ∈ Finset.range (m + 1),
          ((p : ℚ) ^ j * (kappaMinus j / j.factorial))
            * (∑ a ∈ Finset.range p, (a : ℚ) ^ (m - j) * (1 / (m - j).factorial)))
        * (m.factorial : ℚ) := (Finset.sum_mul _ _ _).symm
    _ = ((p : ℚ) ^ 6 * (kappaMinus m / m.factorial)) * (m.factorial : ℚ) := by rw [hser]
    _ = (p : ℚ) ^ 6 * kappaMinus m := by rw [mul_assoc, div_mul_cancel₀ _ hm0]

/-- `tauPolyMinus (X^j) = κ⁻_j`。 -/
lemma tauPolyMinus_X_pow (j : ℕ) :
    tauPolyMinus (Polynomial.X ^ j : ℚ[X]) = kappaMinus j := by
  rw [tauPolyMinus, Polynomial.support_X_pow, Finset.sum_singleton,
    Polynomial.coeff_X_pow_self, one_mul]

/-- `tauPolyMinus (C c * P) = c * tauPolyMinus P`。 -/
lemma tauPolyMinus_C_mul (c : ℚ) (P : ℚ[X]) :
    tauPolyMinus (Polynomial.C c * P) = c * tauPolyMinus P := by
  rw [tauPolyMinus, tauPolyMinus, Finset.mul_sum]
  have hsub : (Polynomial.C c * P).support ⊆ P.support := by
    intro i hi
    rw [Polynomial.mem_support_iff] at hi
    rw [Polynomial.mem_support_iff]
    intro h'
    apply hi
    rw [Polynomial.coeff_C_mul, h', mul_zero]
  rw [Finset.sum_subset hsub (fun i _ hi => by
    rw [Polynomial.notMem_support_iff] at hi
    rw [hi, zero_mul])]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Polynomial.coeff_C_mul]
  ring

/-- `tauPolyMinus (P + Q) = tauPolyMinus P + tauPolyMinus Q`。 -/
lemma tauPolyMinus_add (P Q : ℚ[X]) :
    tauPolyMinus (P + Q) = tauPolyMinus P + tauPolyMinus Q := by
  classical
  have hPQ : (∑ i ∈ (P + Q).support, (P + Q).coeff i * kappaMinus i)
      = ∑ i ∈ P.support ∪ Q.support, (P + Q).coeff i * kappaMinus i :=
    Finset.sum_subset Polynomial.support_add
      (fun i _ hi => by rw [Polynomial.notMem_support_iff] at hi; rw [hi, zero_mul])
  rw [tauPolyMinus, tauPolyMinus, tauPolyMinus, hPQ]
  have hp : (∑ i ∈ P.support, P.coeff i * kappaMinus i)
      = ∑ i ∈ P.support ∪ Q.support, P.coeff i * kappaMinus i :=
    Finset.sum_subset Finset.subset_union_left
      (fun i _ hi => by rw [Polynomial.notMem_support_iff] at hi; rw [hi, zero_mul])
  have hq : (∑ i ∈ Q.support, Q.coeff i * kappaMinus i)
      = ∑ i ∈ P.support ∪ Q.support, Q.coeff i * kappaMinus i :=
    Finset.sum_subset Finset.subset_union_right
      (fun i _ hi => by rw [Polynomial.notMem_support_iff] at hi; rw [hi, zero_mul])
  rw [hp, hq, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Polynomial.coeff_add]
  ring

/-- `tauPolyMinus` 的有限和线性性。 -/
lemma tauPolyMinus_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) :
    tauPolyMinus (∑ i ∈ s, f i) = ∑ i ∈ s, tauPolyMinus (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => rw [Finset.sum_empty, Finset.sum_empty, tauPolyMinus, Polynomial.support_zero,
    Finset.sum_empty]
  | insert a s ha ih =>
    rw [Finset.sum_insert ha, Finset.sum_insert ha, tauPolyMinus_add, ← ih]

/-- 复合与有限和交换（`comp` 对第一个变元加性）。 -/
lemma sum_comp (s : Finset ℕ) (f : ℕ → ℚ[X]) (r : ℚ[X]) :
    (∑ i ∈ s, f i).comp r = ∑ i ∈ s, (f i).comp r := by
  classical
  induction s using Finset.induction_on with
  | empty => rw [Finset.sum_empty, Finset.sum_empty, Polynomial.zero_comp]
  | insert b s hb ih =>
    rw [Finset.sum_insert hb, Finset.sum_insert hb, Polynomial.add_comp, ih]

/-- `(X^i).comp r = r^i`。 -/
lemma X_pow_comp (i : ℕ) (r : ℚ[X]) :
    (Polynomial.X ^ i : ℚ[X]).comp r = r ^ i := by
  induction i with
  | zero => rw [pow_zero, pow_zero, Polynomial.one_comp]
  | succ i ih => rw [pow_succ, pow_succ, Polynomial.mul_comp, ih, Polynomial.X_comp]

/-- **`tauPolyMinus` 的复合展开**：对线性代入 `h = C a + C p·X`，
`tauPolyMinus (g.comp h) = Σ_{i∈supp g} g_i Σ_{j≤i} C(i,j) a^{i−j} p^j κ⁻_j`
（二项展开 + `tauPolyMinus` 线性性 + `tauPolyMinus (X^j) = κ⁻_j`）。 -/
lemma tauPolyMinus_comp_lin (p a : ℕ) (g : ℚ[X]) :
    tauPolyMinus (g.comp (Polynomial.C (a : ℚ) + Polynomial.C (p : ℚ) * Polynomial.X))
    = ∑ i ∈ g.support, g.coeff i * (∑ j ∈ Finset.range (i + 1),
        (Nat.choose i j : ℚ) * ((a : ℚ) ^ (i - j)) * ((p : ℚ) ^ j * kappaMinus j)) := by
  classical
  conv_lhs => rw [Polynomial.as_sum_support_C_mul_X_pow g, sum_comp]
  rw [tauPolyMinus_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Polynomial.C_mul_comp, X_pow_comp, tauPolyMinus_C_mul]
  congr 1
  rw [add_comm (Polynomial.C (a : ℚ)) (Polynomial.C (p : ℚ) * Polynomial.X), add_pow,
    tauPolyMinus_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  rw [Finset.mem_range] at hj
  have e1 : (Polynomial.C (p : ℚ) * Polynomial.X) ^ j * (Polynomial.C (a : ℚ)) ^ (i - j)
      * ((Nat.choose i j : ℕ) : ℚ[X])
    = Polynomial.C (((Nat.choose i j : ℕ) : ℚ)) *
      ((Polynomial.C (p : ℚ) * Polynomial.X) ^ j * (Polynomial.C (a : ℚ)) ^ (i - j)) :=
    mul_comm _ _
  rw [e1, tauPolyMinus_C_mul, ← map_pow (Polynomial.C : ℚ →+* ℚ[X]) (a : ℚ),
    mul_pow (Polynomial.C (p : ℚ)) Polynomial.X j,
    mul_assoc ((Polynomial.C (p : ℚ)) ^ j) (Polynomial.X ^ j)
      (Polynomial.C ((a : ℚ) ^ (i - j))),
    mul_comm (Polynomial.X ^ j) (Polynomial.C ((a : ℚ) ^ (i - j))),
    ← mul_assoc ((Polynomial.C (p : ℚ)) ^ j) (Polynomial.C ((a : ℚ) ^ (i - j)))
      (Polynomial.X ^ j),
    ← map_pow (Polynomial.C : ℚ →+* ℚ[X]) (p : ℚ),
    ← map_mul (Polynomial.C : ℚ →+* ℚ[X]) ((p : ℚ) ^ j) ((a : ℚ) ^ (i - j)),
    tauPolyMinus_C_mul, tauPolyMinus_X_pow]
  ring

/-- **minus 约定的多项式分布恒等式**（对一切 g ∈ ℚ[X] 成立）：
`p⁶ · τ⁻(g) = Σ_{a<p} τ⁻(g(a + pX))`。
证明：复合展开后交换求和次序，内层正是幂和恒等式
`distribution_power_sum`。 -/
theorem distribution_minus (p : ℕ) (hp : 0 < p) (g : ℚ[X]) :
    (p : ℚ) ^ 6 * tauPolyMinus g =
      ∑ a ∈ Finset.range p,
        tauPolyMinus (g.comp (Polynomial.C (a : ℚ) + Polynomial.C (p : ℚ) * Polynomial.X)) := by
  classical
  have hs : (∑ a ∈ Finset.range p,
        tauPolyMinus (g.comp (Polynomial.C (a : ℚ) + Polynomial.C (p : ℚ) * Polynomial.X)))
      = ∑ a ∈ Finset.range p, ∑ i ∈ g.support, g.coeff i * (∑ j ∈ Finset.range (i + 1),
        (Nat.choose i j : ℚ) * ((a : ℚ) ^ (i - j)) * ((p : ℚ) ^ j * kappaMinus j)) :=
    Finset.sum_congr rfl fun a _ => tauPolyMinus_comp_lin p a g
  rw [hs, Finset.sum_comm, tauPolyMinus, Finset.mul_sum]
  refine Finset.sum_congr rfl fun i hi => ?_
  rw [← Finset.mul_sum, Finset.sum_comm]
  have hfac : (∑ j ∈ Finset.range (i + 1), ∑ a ∈ Finset.range p,
        (Nat.choose i j : ℚ) * ((a : ℚ) ^ (i - j)) * ((p : ℚ) ^ j * kappaMinus j))
      = ∑ j ∈ Finset.range (i + 1),
        ((Nat.choose i j : ℚ) * ((p : ℚ) ^ j * kappaMinus j))
          * (∑ a ∈ Finset.range p, (a : ℚ) ^ (i - j)) := by
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => by ring
  rw [hfac, distribution_power_sum p hp i]
  ring

/-- **分布恒等式（构造适用版，已证，2026-09-25）**：奇多项式 g（只含奇次幂，
如 pullback 像 g = x⁷·R(−x²)）满足 p⁶·τ(g) = Σ_{a=0}^{p−1} τ⁻(g(a+pX))，
其中 τ⁻ 为 minus 约定（`tauPolyMinus`）。

证明：`distribution_minus`（minus 约定对一切 g 成立）+ 奇性
`tauPoly g = tauPolyMinus g`（支撑集避开的第 6 项两约定之差
`kappaMinus 6 − kappa 6 = −1` 不参与）。
验证证据：`research/b8_distribution.py` §3（精确有理，p ≤ 13、次数 ≤ 21
随机奇 g，零违规）。 -/
theorem distribution_odd (p : ℕ) (hp : 0 < p) (g : ℚ[X])
    (hg : ∀ n, g.coeff n ≠ 0 → Odd n) :
    (p : ℚ) ^ 6 * tauPoly g =
      ∑ a ∈ Finset.range p,
        tauPolyMinus (g.comp (Polynomial.C (a : ℚ) + Polynomial.C (p : ℚ) * Polynomial.X)) := by
  have h1 : tauPoly g = tauPolyMinus g := by
    rw [tauPoly, tauPolyMinus]
    refine Finset.sum_congr rfl fun i hi => ?_
    rw [Polynomial.mem_support_iff] at hi
    have hodd := hg i hi
    have hne6 : i ≠ 6 := by
      rintro rfl
      obtain ⟨k, hk⟩ := hodd
      omega
    rw [kappaMinus, if_neg hne6, sub_zero]
  rw [h1, distribution_minus p hp g]

end Zeta7
