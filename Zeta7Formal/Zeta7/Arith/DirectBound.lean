import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Div
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Log
import Mathlib.Data.Nat.MaxPowDiv
import Mathlib.Order.Interval.Finset.Nat
import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.LinearAlgebra.Lagrange
import Mathlib.Algebra.Group.ForwardDiff
import Mathlib.RingTheory.Polynomial.Pochhammer
import Mathlib.NumberTheory.Bernoulli
import Mathlib.Algebra.Polynomial.Degree.Support
import Mathlib.Data.Nat.Factorial.BigOperators
import Zeta7.Construction
import Zeta7.Harmonic
import Zeta7.Tau
import Zeta7.Distribution

/-!
# b=8 直接赋值界骨架：`τ₈` 在整极点有理函数上的 p-进下界

mo271 `Apery/Arith/{Val,DirectBound,DirectPoly}.lean`（b=6，ζ(3)）的 b=8 平移。
研究侧依据：`research/b8_arithmetic.md` §C7（逐项损耗表，2026-09-25 钉死）——

对 `g = κ∏_{ζ∈Z}(x−ζ) / ∏_{r∈Pl}(x−r)`，极点两两同类相差恰好一个 p 幂
（`Sep`）、调和指标 `< p²`、分子次数 `< p²−1`：

  `v_p^G(τ₈,X(g)) ≥ min_c (e_c − ℓ_c) − 6`，   −6 = −7（调和）+ 1（留数）

其中 `e_c`（resp. `ℓ_c`）为 mod p 类 `c` 中零点（resp. 极点）数。
−6 是 b=6 的 −4 = −5+1 的平移（8 = 7+1 模式，§C7 损耗表）。

**本文件状态**（一边研究一边形式化）：
- b-无关部分完整证明：`VG`/`GV` 代数、`VG_res`（留数界 `e_c−ℓ_c+1`）、
  `partial_fractionsP`（部分分式）、`factor_roots`（整数根分解）、
  DirectPoly 复合引理组（`GV_numOf_comp` 等）；
- b-相关核心 `VG_H7`（调和界 −7）已证（由 `harmonic7_val_aux` 一步推出）；
- **`VG_polyPart_eval8`（多项式部分的值界）已证**（2026-09-25 自
  DirectPoly.lean 完整移植）；
- 合成链剩余两项目标陈述为 sorry（附证明路线）：`tauPoly8_bound`
  （b=8 版 tau_bound）、`tauX8_direct`（合成界 `β − 6`）。
-/

open Finset Polynomial

namespace Zeta7

variable {p : ℕ} [hp : Fact p.Prime]

/-! ## 一、极点函数定义（镜像 `Apery/Arith/PoleFun.lean`）-/

/-- `∏_{r ∈ Pl} (x − r)`。 -/
noncomputable def piPl (Pl : Finset ℤ) : ℚ[X] := ∏ r ∈ Pl, (X - C (r : ℚ))

lemma piPl_monic (Pl : Finset ℤ) : (piPl Pl).Monic :=
  monic_prod_of_monic _ _ fun r _ => monic_X_sub_C _

lemma natDegree_piPl (Pl : Finset ℤ) : (piPl Pl).natDegree = Pl.card := by
  unfold piPl
  rw [natDegree_prod_of_monic _ _ fun r _ => monic_X_sub_C _]
  rw [Finset.sum_congr rfl fun (r : ℤ) _ => natDegree_X_sub_C ((r : ℤ) : ℚ)]
  simp

/-- 多项式部分 `A /ₘ ∏(x−r)`。 -/
noncomputable def polyPart (A : ℚ[X]) (Pl : Finset ℤ) : ℚ[X] := A /ₘ piPl Pl

/-- `r` 处留数 `A(r)/∏_{s≠r}(r−s)`。 -/
noncomputable def resP (A : ℚ[X]) (Pl : Finset ℤ) (r : ℤ) : ℚ :=
  A.eval (r : ℚ) / ∏ s ∈ Pl.erase r, ((r : ℚ) - s)

/-- 调和指标 `d(r)`：非负取 `r`，负取 `−r−1`。 -/
def dd (r : ℤ) : ℕ := if 0 ≤ r then r.toNat else (-r - 1).toNat

/-- 分子 `κ ∏(x − ζ)`。 -/
noncomputable def numOf (κ : ℚ) (Z : Multiset ℤ) : ℚ[X] :=
  C κ * (Z.map fun ζ : ℤ => X - C (ζ : ℚ)).prod

/-- mod p 类 `c` 中零点数 `e_c`。 -/
def cnt (p : ℕ) (Z : Multiset ℤ) (c : ZMod p) : ℕ := (Z.filter fun ζ : ℤ => (ζ : ZMod p) = c).card

/-- mod p 类 `c` 中的极点集。 -/
def plc (p : ℕ) (Pl : Finset ℤ) (c : ZMod p) : Finset ℤ := Pl.filter fun r : ℤ => (r : ZMod p) = c

/-- 同类极点两两相差恰好一个 p 幂（不被子 p² 整除）。 -/
def Sep (p : ℕ) (Pl : Finset ℤ) : Prop :=
  ∀ r ∈ Pl, ∀ s ∈ Pl, r ≠ s → (r : ZMod p) = s → ¬ (p : ℤ) ^ 2 ∣ r - s

lemma lagrange_basis_eq (Pl : Finset ℤ) (r : ℤ) :
    Lagrange.basis Pl (fun s : ℤ => (s : ℚ)) r =
      C (∏ s ∈ Pl.erase r, ((r : ℚ) - s))⁻¹ * ∏ s ∈ Pl.erase r, (X - C (s : ℚ)) := by
  unfold Lagrange.basis Lagrange.basisDivisor
  rw [Finset.prod_mul_distrib, ← map_prod, Finset.prod_inv_distrib]

/-- **部分分式**：`A = (polyPart)·∏(x−r) + Σ_r res_r·∏_{s≠r}(x−s)`。 -/
theorem partial_fractionsP (A : ℚ[X]) (Pl : Finset ℤ) :
    A = polyPart A Pl * piPl Pl +
      ∑ r ∈ Pl, C (resP A Pl r) * ∏ s ∈ Pl.erase r, (X - C (s : ℚ)) := by
  have hinj : Set.InjOn (fun s : ℤ => (s : ℚ)) Pl := fun a _ b _ h => by
    simpa using h
  have hmod : A %ₘ piPl Pl = ∑ r ∈ Pl, C (resP A Pl r) * ∏ s ∈ Pl.erase r, (X - C (s : ℚ)) := by
    rw [Lagrange.eq_interpolate_of_eval_eq (f := A %ₘ piPl Pl) (fun r : ℤ => A.eval (r : ℚ)) hinj
      (by
        have this := degree_modByMonic_lt A (piPl_monic Pl)
        rwa [degree_eq_natDegree (piPl_monic Pl).ne_zero, natDegree_piPl] at this)
      (fun r hr => by
        have h1 := modByMonic_add_div A (piPl Pl)
        have h2 : (piPl Pl).eval (r : ℚ) = 0 := by
          unfold piPl; rw [eval_prod]
          exact Finset.prod_eq_zero hr (by simp)
        conv_rhs => rw [← h1]
        rw [eval_add, eval_mul, h2, zero_mul, add_zero])]
    simp only [Lagrange.interpolate_apply]
    refine Finset.sum_congr rfl fun r _ => ?_
    rw [lagrange_basis_eq, resP, div_eq_mul_inv, C_mul, mul_assoc]
  conv_lhs => rw [← modByMonic_add_div A (piPl Pl)]
  rw [hmod, polyPart, add_comm, mul_comm]

lemma natDegree_polyPart_le (A : ℚ[X]) (Pl : Finset ℤ) :
    (polyPart A Pl).natDegree ≤ A.natDegree - Pl.card := by
  unfold polyPart
  rw [natDegree_divByMonic A (piPl_monic Pl), natDegree_piPl]

lemma natDegree_numOf_le (κ : ℚ) (Z : Multiset ℤ) : (numOf κ Z).natDegree ≤ Z.card := by
  unfold numOf
  refine (natDegree_C_mul_le _ _).trans ?_
  refine (natDegree_multiset_prod_le (t := Z.map fun ζ : ℤ => X - C (ζ : ℚ))).trans ?_
  rw [Multiset.map_map]
  have : ∀ ζ ∈ Z, ((natDegree ∘ fun ζ : ℤ => X - C (ζ : ℚ)) ζ) = 1 := fun ζ _ =>
    natDegree_X_sub_C ((ζ : ℤ) : ℚ)
  rw [Multiset.map_congr rfl this, Multiset.map_const', Multiset.sum_replicate, smul_eq_mul,
    mul_one]

/-! ## 二、`p`-进赋值工具箱（移植 `Apery/Arith/Val.lean`，b-无关）-/

/-- `v_p(q) ≥ r`（`q = 0` 时 vacuous）。 -/
def VG (p : ℕ) (q : ℚ) (r : ℚ) : Prop := q = 0 ∨ r ≤ (padicValRat p q : ℚ)

namespace VG

lemma zero (r : ℚ) : VG p 0 r := Or.inl rfl

lemma mono {q r s : ℚ} (h : VG p q r) (hs : s ≤ r) : VG p q s :=
  h.imp id fun h => hs.trans h

lemma neg {q r : ℚ} (h : VG p q r) : VG p (-q) r := by
  rcases h with h | h
  · left; simp [h]
  · right; rwa [padicValRat.neg]

lemma add [Fact p.Prime] {q q' r : ℚ} (h : VG p q r) (h' : VG p q' r) : VG p (q + q') r := by
  by_cases hq : q = 0
  · simpa [hq] using h'
  by_cases hq' : q' = 0
  · simpa [hq'] using h
  by_cases hs : q + q' = 0
  · exact Or.inl hs
  right
  have h1 := h.resolve_left hq
  have h2 := h'.resolve_left hq'
  have this := padicValRat.min_le_padicValRat_add (p := p) hs
  have h3 : (min (padicValRat p q) (padicValRat p q') : ℚ) ≤ padicValRat p (q + q') := by
    exact_mod_cast this
  exact (le_min h1 h2).trans h3

lemma sub [Fact p.Prime] {q q' r : ℚ} (h : VG p q r) (h' : VG p q' r) : VG p (q - q') r := by
  rw [sub_eq_add_neg]; exact h.add h'.neg

lemma mul [Fact p.Prime] {q q' r r' : ℚ} (h : VG p q r) (h' : VG p q' r') : VG p (q * q') (r + r') := by
  by_cases hq : q = 0
  · left; simp [hq]
  by_cases hq' : q' = 0
  · left; simp [hq']
  right
  rw [padicValRat.mul hq hq']
  push_cast
  exact add_le_add (h.resolve_left hq) (h'.resolve_left hq')

lemma sum [Fact p.Prime] {ι : Type*} (s : Finset ι) {f : ι → ℚ} {r : ℚ} (h : ∀ i ∈ s, VG p (f i) r) :
    VG p (∑ i ∈ s, f i) r := by
  classical
  induction s using Finset.induction_on with
  | empty => exact zero r
  | insert a s ha ih =>
    rw [Finset.sum_insert ha]
    exact (h a (Finset.mem_insert_self _ _)).add (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

lemma prod [Fact p.Prime] {ι : Type*} (s : Finset ι) {f : ι → ℚ} {r : ι → ℚ}
    (h : ∀ i ∈ s, VG p (f i) (r i)) :
    VG p (∏ i ∈ s, f i) (∑ i ∈ s, r i) := by
  classical
  induction s using Finset.induction_on with
  | empty => right; simp
  | insert a s ha ih =>
    rw [Finset.prod_insert ha, Finset.sum_insert ha]
    exact (h a (Finset.mem_insert_self _ _)).mul (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

lemma intCast (z : ℤ) : VG p (z : ℚ) 0 := by
  by_cases hz : z = 0
  · left; simp [hz]
  right
  rw [padicValRat.of_int]
  exact_mod_cast Nat.zero_le _

lemma natCast (n : ℕ) : VG p (n : ℚ) 0 := by exact_mod_cast intCast (p := p) (n : ℤ)

lemma one : VG p 1 0 := by exact_mod_cast natCast (p := p) 1

lemma inv [Fact p.Prime] {q r : ℚ} (h : q ≠ 0) (hv : (padicValRat p q : ℚ) ≤ r) : VG p q⁻¹ (-r) := by
  right
  rw [padicValRat.inv]
  push_cast
  linarith

lemma of_eq {q : ℚ} (r : ℚ) (h : q ≠ 0 → r ≤ (padicValRat p q : ℚ)) : VG p q r := by
  by_cases hq : q = 0
  · exact Or.inl hq
  · exact Or.inr (h hq)

/-- `1 ≤ j ≤ n` ⟹ `v_p(1/j) ≥ −⌊log_p n⌋`（移植 `Apery/Arith/Val.lean` 的 `VG.inv_nat`）。 -/
lemma inv_nat [hp : Fact p.Prime] {j n : ℕ} (hj : 1 ≤ j) (hjn : j ≤ n) :
    VG p ((j : ℚ)⁻¹) (-(Nat.log p n : ℚ)) := by
  apply inv (by exact_mod_cast (by omega : j ≠ 0))
  rw [padicValRat.of_nat]
  have h1 : padicValNat p j ≤ Nat.log p j := by
    rcases Nat.eq_zero_or_pos (padicValNat p j) with h | h
    · rw [h]; exact Nat.zero_le _
    · have hdvd : p ^ padicValNat p j ∣ j := pow_padicValNat_dvd
      exact Nat.le_log_of_pow_le hp.out.one_lt (Nat.le_of_dvd (by omega) hdvd)
  have h2 : Nat.log p j ≤ Nat.log p n := Nat.log_mono_right hjn
  exact_mod_cast h1.trans h2

/-- `v_p(p^k) = k`。 -/
lemma primePow [hp : Fact p.Prime] (k : ℤ) : VG p ((p : ℚ) ^ k) k := by
  right
  have : padicValRat p ((p : ℚ) ^ k) = k := by
    rw [padicValRat.zpow _, padicValRat.self hp.out.one_lt, mul_one]
  rw [this]

lemma pow [Fact p.Prime] {q r : ℚ} (h : VG p q r) (n : ℕ) : VG p (q ^ n) (n * r) := by
  induction n with
  | zero => right; simp
  | succ n ih => rw [pow_succ]; convert ih.mul h using 1; push_cast; ring

lemma multiset_prod (s : Multiset ℚ) (b : ℚ → ℚ) (h : ∀ q ∈ s, VG p q (b q)) :
    VG p s.prod (s.map b).sum := by
  induction s using Multiset.induction_on with
  | empty => right; simp
  | cons a s ih =>
    rw [Multiset.prod_cons, Multiset.map_cons, Multiset.sum_cons]
    exact (h a (Multiset.mem_cons_self _ _)).mul (ih fun q hq => h q (Multiset.mem_cons_of_mem hq))

end VG

/-- Gauss 赋值界：`f ∈ ℚ[X]` 的每个系数都满足 `VG p · r`。 -/
def GV (p : ℕ) (f : ℚ[X]) (r : ℚ) : Prop := ∀ n, VG p (f.coeff n) r

namespace GV

lemma zero (r : ℚ) : GV p 0 r := fun n => by simpa using VG.zero (p := p) r

lemma mono {f : ℚ[X]} {r s : ℚ} (h : GV p f r) (hs : s ≤ r) : GV p f s := fun n => (h n).mono hs

lemma add [Fact p.Prime] {f g : ℚ[X]} {r : ℚ} (hf : GV p f r) (hg : GV p g r) : GV p (f + g) r :=
  fun n => by rw [coeff_add]; exact (hf n).add (hg n)

lemma neg {f : ℚ[X]} {r : ℚ} (hf : GV p f r) : GV p (-f) r := fun n => by
  rw [coeff_neg]; exact (hf n).neg

lemma sub [Fact p.Prime] {f g : ℚ[X]} {r : ℚ} (hf : GV p f r) (hg : GV p g r) : GV p (f - g) r :=
  fun n => by rw [coeff_sub]; exact (hf n).sub (hg n)

lemma C {q r : ℚ} (h : VG p q r) : GV p (Polynomial.C q) r := fun n => by
  rw [coeff_C]; split_ifs
  · exact h
  · exact VG.zero r

lemma X : GV p (X : ℚ[X]) 0 := fun n => by
  rw [coeff_X]; split_ifs
  · exact VG.one
  · exact VG.zero 0

lemma mul [Fact p.Prime] {f g : ℚ[X]} {r s : ℚ} (hf : GV p f r) (hg : GV p g s) :
    GV p (f * g) (r + s) := fun n => by
  rw [coeff_mul]
  exact VG.sum _ fun x _ => (hf x.1).mul (hg x.2)

lemma C_mul [Fact p.Prime] {q r s : ℚ} {f : ℚ[X]} (hq : VG p q r) (hf : GV p f s) :
    GV p (Polynomial.C q * f) (r + s) := (C hq).mul hf

lemma prod [Fact p.Prime] {ι : Type*} (s : Finset ι) {f : ι → ℚ[X]} {r : ι → ℚ}
    (h : ∀ i ∈ s, GV p (f i) (r i)) :
    GV p (∏ i ∈ s, f i) (∑ i ∈ s, r i) := by
  classical
  induction s using Finset.induction_on with
  | empty =>
    simp only [Finset.prod_empty, Finset.sum_empty]
    simpa using C (p := p) (VG.one (p := p))
  | insert a s ha ih =>
    rw [Finset.prod_insert ha, Finset.sum_insert ha]
    exact (h a (Finset.mem_insert_self _ _)).mul
      (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

lemma sum [Fact p.Prime] {ι : Type*} (s : Finset ι) {f : ι → ℚ[X]} {r : ℚ}
    (h : ∀ i ∈ s, GV p (f i) r) : GV p (∑ i ∈ s, f i) r := fun n => by
  rw [finsetSum_coeff]; exact VG.sum s fun i hi => h i hi n

lemma pow {F : ℚ[X]} {r : ℚ} (h : GV p F r) (n : ℕ) : GV p (F ^ n) (n * r) := by
  induction n with
  | zero => simpa using GV.C (p := p) (VG.one (p := p))
  | succ n ih => rw [pow_succ]; convert ih.mul h using 1; push_cast; ring

lemma comp {F G : ℚ[X]} (hF : GV p F 0) (hG : GV p G 0) : GV p (F.comp G) 0 := by
  rw [comp_eq_sum_left, Polynomial.sum]
  refine GV.sum _ fun n _ => ?_
  have this := GV.C_mul (hF n) (hG.pow n)
  simpa using this

lemma divByMonic_X_sub_C {F : ℚ[X]} {a : ℚ} (hF : GV p F 0) (ha : VG p a 0) :
    GV p (F /ₘ (Polynomial.X - Polynomial.C a)) 0 := fun n => by
  rw [coeff_divByMonic_X_sub_C]
  refine VG.sum _ fun i _ => ?_
  have this := (ha.pow (i - (n + 1))).mul (hF i)
  simpa using this

/-- Multiset 乘积。 -/
lemma multiset_prod (s : Multiset ℚ[X]) (b : ℚ[X] → ℚ) (h : ∀ f ∈ s, GV p f (b f)) :
    GV p s.prod (s.map b).sum := by
  induction s using Multiset.induction_on with
  | empty => simpa using GV.C (p := p) (VG.one (p := p))
  | cons a s ih =>
    rw [Multiset.prod_cons, Multiset.map_cons, Multiset.sum_cons]
    exact (h a (Multiset.mem_cons_self _ _)).mul
      (ih fun f hf => h f (Multiset.mem_cons_of_mem hf))

/-- **带行列权重的行列式界**（移植 `Apery/Arith/Val.lean` 的 `det_GV`，b-无关）：
若 `M i j` 的 Gauss 赋值 `≥ ρ i + κ j`，则 `det M` 的赋值 `≥ ∑ ρ + ∑ κ`。
(3.12)-类比的最后合成步骤（`Arith/SmallPrimeF`）。 -/
theorem det_GV [Fact p.Prime] {ι : Type*} [Fintype ι] [DecidableEq ι] (M : Matrix ι ι ℚ[X])
    (ρ κ : ι → ℚ) (h : ∀ i j, GV p (M i j) (ρ i + κ j)) :
    GV p M.det (∑ i, ρ i + ∑ j, κ j) := by
  rw [Matrix.det_apply]
  refine GV.sum _ fun σ _ => ?_
  have hprod : GV p (∏ i, M (σ i) i) (∑ i, (ρ (σ i) + κ i)) :=
    GV.prod _ fun i _ => h (σ i) i
  have e : ∑ i, (ρ (σ i) + κ i) = ∑ i, ρ i + ∑ j, κ j := by
    rw [Finset.sum_add_distrib, Equiv.sum_comp σ ρ]
  rw [e] at hprod
  rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with hs | hs
  · rw [hs, one_smul]; exact hprod
  · rw [hs, Units.neg_smul, one_smul]; exact hprod.neg

end GV

namespace VG

/-- 常数项 = 在 0 处求值。 -/
lemma eval_zero {F : ℚ[X]} {r : ℚ} (hF : GV p F r) : VG p (F.eval 0) r := by
  rw [← coeff_zero_eq_eval_zero]; exact hF 0

/-- `p`-整系数多项式在 `p`-整点的值 `p`-整。 -/
lemma eval {F : ℚ[X]} {z : ℚ} (hF : GV p F 0) (hz : VG p z 0) : VG p (F.eval z) 0 := by
  rw [eval_eq_sum, Polynomial.sum]
  refine VG.sum _ fun n _ => ?_
  have := (hF n).mul (hz.pow n)
  simpa using this

end VG

/-- **整数根分解**：`p`-整多项式在 `p`-整互异点处消失 ⟹ 可被 `∏(X−ρ)` 整除
  且商 `p`-整。 -/
theorem factor_roots (ρs : Finset ℚ) (hρ : ∀ ρ ∈ ρs, VG p ρ 0) {F : ℚ[X]} (hF : GV p F 0)
    (hroot : ∀ ρ ∈ ρs, F.eval ρ = 0) :
    ∃ S : ℚ[X], GV p S 0 ∧ F = (∏ ρ ∈ ρs, (X - C ρ)) * S := by
  classical
  induction ρs using Finset.induction_on generalizing F with
  | empty => exact ⟨F, hF, by simp⟩
  | insert a ρs ha ih =>
    have hra : F.IsRoot a := hroot a (Finset.mem_insert_self _ _)
    set F1 := F /ₘ (X - C a) with hF1
    have hFeq : F = (X - C a) * F1 := ((mul_divByMonic_eq_iff_isRoot).mpr hra).symm
    have hF1int : GV p F1 0 := GV.divByMonic_X_sub_C hF (hρ a (Finset.mem_insert_self _ _))
    have hF1root : ∀ ρ ∈ ρs, F1.eval ρ = 0 := by
      intro ρ hρs
      have h1 := hroot ρ (Finset.mem_insert_of_mem hρs)
      rw [hFeq, eval_mul, eval_sub, eval_X, eval_C] at h1
      have hne : ρ - a ≠ 0 := sub_ne_zero.mpr fun h => ha (h ▸ hρs)
      exact (mul_eq_zero.mp h1).resolve_left hne
    obtain ⟨S, hS, hSeq⟩ := ih (fun ρ h => hρ ρ (Finset.mem_insert_of_mem h)) hF1int hF1root
    exact ⟨S, hS, by rw [hFeq, hSeq, Finset.prod_insert ha, mul_assoc]⟩

/-! ## 三、整数赋值与留数界（移植 `Apery/Arith/DirectBound.lean`，b-无关）-/

lemma zmod_eq_iff_dvd {a b : ℤ} : (a : ZMod p) = b ↔ (p : ℤ) ∣ a - b := by
  rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]; push_cast; exact sub_eq_zero.symm

lemma VG_int_one {z : ℤ} (h : (p : ℤ) ∣ z) : VG p (z : ℚ) 1 := by
  by_cases hz : z = 0
  · left; simp [hz]
  right
  rw [padicValRat.of_int]
  have this := (padicValInt_dvd_iff (p := p) 1 z).mp (by simpa using h)
  rcases this with h | h
  · exact absurd h hz
  · exact_mod_cast h

lemma padicValRat_int_eq_zero {z : ℤ} (h : ¬ (p : ℤ) ∣ z) : padicValRat p (z : ℚ) = 0 := by
  rw [padicValRat.of_int]
  have hz : z ≠ 0 := fun h' => h (h' ▸ dvd_zero _)
  by_contra hne
  have h1 : 1 ≤ padicValInt p z := Nat.one_le_iff_ne_zero.mpr (by exact_mod_cast hne)
  exact h (by simpa using (padicValInt_dvd_iff (p := p) 1 z).mpr (Or.inr h1))

lemma padicValRat_int_le_one {z : ℤ} (h2 : ¬ (p : ℤ) ^ 2 ∣ z) : padicValRat p (z : ℚ) ≤ 1 := by
  rw [padicValRat.of_int]
  by_contra hne
  rw [not_le] at hne
  have this : 2 ≤ padicValInt p z := by exact_mod_cast hne
  have hz : z ≠ 0 := by rintro rfl; simp at hne
  exact h2 ((padicValInt_dvd_iff (p := p) 2 z).mpr (Or.inr this))

lemma padicValRat_finset_prod {ι : Type*} (s : Finset ι) (f : ι → ℚ) (hf : ∀ i ∈ s, f i ≠ 0) :
    padicValRat p (∏ i ∈ s, f i) = ∑ i ∈ s, padicValRat p (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [Finset.prod_insert ha, Finset.sum_insert ha, padicValRat.mul (hf a (mem_insert_self _ _))
      (Finset.prod_ne_zero_iff.mpr fun i hi => hf i (mem_insert_of_mem hi)),
      ih fun i hi => hf i (mem_insert_of_mem hi)]

lemma eval_numOf (κ : ℚ) (Z : Multiset ℤ) (x : ℚ) :
    (numOf κ Z).eval x = κ * (Z.map fun ζ : ℤ => x - (ζ : ℚ)).prod := by
  unfold numOf
  rw [eval_mul, eval_C, eval_multiset_prod, Multiset.map_map]
  congr 2
  exact Multiset.map_congr rfl fun ζ _ => by simp

lemma VG_prod_sub (Z : Multiset ℤ) (x : ℤ) :
    VG p ((Z.map fun ζ : ℤ => (x : ℚ) - (ζ : ℚ)).prod) (cnt p Z (x : ZMod p)) := by
  induction Z using Multiset.induction_on with
  | empty => right; simp [cnt]
  | cons a Z ih =>
    rw [Multiset.map_cons, Multiset.prod_cons]
    unfold cnt at ih ⊢
    rw [Multiset.filter_cons]
    split_ifs with h
    · rw [Multiset.card_add, Multiset.card_singleton]
      have h1 : VG p ((x : ℚ) - (a : ℚ)) 1 := by
        have this := VG_int_one (p := p) ((zmod_eq_iff_dvd (p := p)).mp h.symm)
        simpa using this
      convert h1.mul ih using 1; push_cast; ring
    · rw [zero_add]
      have h1 : VG p ((x : ℚ) - (a : ℚ)) 0 := by simpa using VG.intCast (p := p) (x - a)
      simpa using h1.mul ih

lemma VG_eval_numOf (κ : ℚ) (hκ : VG p κ 0) (Z : Multiset ℤ) (x : ℤ) :
    VG p ((numOf κ Z).eval (x : ℚ)) (cnt p Z (x : ZMod p)) := by
  rw [eval_numOf]
  simpa using hκ.mul (VG_prod_sub Z x)

lemma padicValRat_denom_le (Pl : Finset ℤ) (hsep : Sep p Pl) {r : ℤ} (hr : r ∈ Pl) :
    (padicValRat p (∏ s ∈ Pl.erase r, ((r : ℚ) - s)) : ℚ) ≤ (plc p Pl r).card - 1 := by
  rw [padicValRat_finset_prod _ _ (fun s hs => by
    rw [Finset.mem_erase] at hs
    exact sub_ne_zero.mpr (by exact_mod_cast hs.1.symm))]
  have hterm : ∀ s ∈ Pl.erase r, (padicValRat p ((r : ℚ) - s) : ℚ) ≤
      if (s : ZMod p) = r then 1 else 0 := by
    intro s hs
    rw [Finset.mem_erase] at hs
    have e : ((r : ℚ) - s) = ((r - s : ℤ) : ℚ) := by push_cast; ring
    rw [e]
    split_ifs with h
    · exact_mod_cast padicValRat_int_le_one (hsep r hr s hs.2 (Ne.symm hs.1) h.symm)
    · rw [padicValRat_int_eq_zero (fun hd => h ((zmod_eq_iff_dvd (p := p)).mpr
        (by rw [← neg_sub]; exact (dvd_neg).mpr hd)))]
      simp
  push_cast
  refine (Finset.sum_le_sum hterm).trans ?_
  rw [Finset.sum_ite, Finset.sum_const, Finset.sum_const_zero, add_zero, nsmul_eq_mul, mul_one]
  have hcard : ((Pl.erase r).filter fun s : ℤ => (s : ZMod p) = r) = (plc p Pl r).erase r := by
    unfold plc; rw [Finset.filter_erase]
  rw [hcard, Finset.card_erase_of_mem (by unfold plc; simp [hr])]
  have this : 1 ≤ (plc p Pl r).card := Finset.card_pos.mpr ⟨r, by unfold plc; simp [hr]⟩
  push_cast [this]
  linarith

/-- **留数界**：`v_p(res_r) ≥ e_c − ℓ_c + 1`（`c` 为 `r` 的 mod p 类）。 -/
theorem VG_res (κ : ℚ) (hκ : VG p κ 0) (Z : Multiset ℤ) (Pl : Finset ℤ) (hsep : Sep p Pl)
    {r : ℤ} (hr : r ∈ Pl) :
    VG p (resP (numOf κ Z) Pl r) ((cnt p Z r : ℚ) - (plc p Pl r).card + 1) := by
  unfold resP
  rw [div_eq_mul_inv]
  have hD : ∏ s ∈ Pl.erase r, ((r : ℚ) - s) ≠ 0 := Finset.prod_ne_zero_iff.mpr fun s hs => by
    rw [Finset.mem_erase] at hs
    exact sub_ne_zero.mpr (by exact_mod_cast hs.1.symm)
  have h1 := VG_eval_numOf κ hκ Z r
  have h2 := VG.inv (p := p) hD (padicValRat_denom_le Pl hsep hr)
  convert h1.mul h2 using 1
  ring

/-! ## 三之二、复合与分裂引理（移植 `Apery/Arith/DirectPoly.lean` 前半，b-无关）-/

lemma prod_erase_split {f : ℤ → ℚ[X]} (S : Finset ℤ) (q : ℤ → Prop) [DecidablePred q] (r : ℤ) :
    ∏ s ∈ S.erase r, f s = (∏ s ∈ (S.filter q).erase r, f s) * ∏ s ∈ (S.filter (¬ q ·)).erase r, f s := by
  rw [← Finset.filter_erase, ← Finset.filter_erase, Finset.prod_filter_mul_prod_filter_not]

lemma GV_lin_comp_class (m ζ : ℤ) (h : (ζ : ZMod p) = m) :
    GV p ((X - C (ζ : ℚ)).comp (C (m : ℚ) + C (p : ℚ) * X)) 1 := by
  rw [sub_comp, X_comp, C_comp, show C (m : ℚ) + C (p : ℚ) * X - C (ζ : ℚ) =
    C (((m - ζ : ℤ) : ℚ)) + C (p : ℚ) * X by push_cast; rw [C_sub]; ring]
  have h1 : VG p (((m - ζ : ℤ) : ℚ)) 1 := VG_int_one ((zmod_eq_iff_dvd (p := p)).mp h.symm)
  have h2 : VG p (p : ℚ) 1 := by simpa using VG.primePow (p := p) 1
  exact (GV.C h1).add (by simpa using GV.C_mul h2 GV.X)

lemma GV_lin_comp (m ζ : ℤ) :
    GV p ((X - C (ζ : ℚ)).comp (C (m : ℚ) + C (p : ℚ) * X)) 0 := by
  rw [sub_comp, X_comp, C_comp, show C (m : ℚ) + C (p : ℚ) * X - C (ζ : ℚ) =
    C (((m - ζ : ℤ) : ℚ)) + C (p : ℚ) * X by push_cast; rw [C_sub]; ring]
  exact (GV.C (VG.intCast _)).add (by simpa using GV.C_mul (VG.natCast (p := p) p) GV.X)

lemma GV_numOf_comp (κ : ℚ) (hκ : VG p κ 0) (Z : Multiset ℤ) (m : ℤ) :
    GV p ((numOf κ Z).comp (C (m : ℚ) + C (p : ℚ) * X)) (cnt p Z (m : ZMod p)) := by
  unfold numOf
  rw [mul_comp, C_comp, multiset_prod_comp, Multiset.map_map]
  suffices h : GV p ((Z.map ((fun q => q.comp (C (m : ℚ) + C (p : ℚ) * X)) ∘
      fun ζ : ℤ => X - C (ζ : ℚ))).prod) (cnt p Z (m : ZMod p)) by
    simpa using GV.C_mul hκ h
  induction Z using Multiset.induction_on with
  | empty => simpa [cnt] using GV.C (p := p) (VG.one (p := p))
  | cons a Z ih =>
    rw [Multiset.map_cons, Multiset.prod_cons]
    unfold cnt at ih ⊢
    rw [Multiset.filter_cons]
    split_ifs with h
    · rw [Multiset.card_add, Multiset.card_singleton]
      have this := (GV_lin_comp_class m a h).mul ih
      convert this using 1
      · simp [Function.comp]
      · push_cast; ring
    · rw [zero_add]
      simpa using (GV_lin_comp m a).mul ih

/-- `(x − r)(m + p z) = p(z − ρ)`，`ρ = (r − m)/p`（`r ≡ m` mod p）。 -/
lemma lin_comp_eq {m r : ℤ} (h : (p : ℤ) ∣ r - m) :
    (X - C (r : ℚ)).comp (C (m : ℚ) + C (p : ℚ) * X) =
      C (p : ℚ) * (X - C (((r - m) / p : ℤ) : ℚ)) := by
  have hp0 : (p : ℚ) ≠ 0 := by exact_mod_cast hp.out.ne_zero
  have e : (p : ℚ) * (((r - m) / p : ℤ) : ℚ) = (r : ℚ) - m := by
    have this := Int.mul_ediv_cancel' h
    exact_mod_cast this
  rw [sub_comp, X_comp, C_comp, mul_sub, ← C_mul, e, C_sub]; ring

/-! ## 三之三、Bernoulli 泛函与二项基（移植 `Apery/Arith/{BinomBasis,TauBound}.lean`，b-无关）

Lb 用 mathlib `bernoulli`（B₁=−1/2 约定）——这正是 `kappaMinus` 的配对约定
（`kappaMinus m = (m)₅·bernoulli(m−5)/720`，见 §五桥接目标）。-/

/-- 在所有自然数点取值相同的多项式相等。 -/
lemma poly_eq_of_nat {P Q : ℚ[X]} (h : ∀ n : ℕ, P.eval (n : ℚ) = Q.eval (n : ℚ)) : P = Q := by
  apply Polynomial.eq_of_infinite_eval_eq
  apply Set.infinite_of_injective_forall_mem (f := fun n : ℕ => (n : ℚ)) Nat.cast_injective
  intro n
  exact h n

/-- `Lb Q = ∑_n Q_n·B_n`（Bernoulli umbra 泛函，B₁=−1/2）。 -/
noncomputable def Lb (Q : ℚ[X]) : ℚ := Q.sum fun n a => a * _root_.bernoulli n

lemma Lb_add (P Q : ℚ[X]) : Lb (P + Q) = Lb P + Lb Q := by
  unfold Lb
  exact Polynomial.sum_add_index _ _ _ (fun _ => by simp) (fun _ _ _ => by ring)

lemma Lb_smul (c : ℚ) (Q : ℚ[X]) : Lb (c • Q) = c * Lb Q := by
  unfold Lb
  rw [Polynomial.sum_smul_index _ _ _ (fun _ => by simp), Polynomial.sum, Polynomial.sum,
    Finset.mul_sum]
  refine Finset.sum_congr rfl fun n _ => by ring

lemma Lb_C_mul (c : ℚ) (Q : ℚ[X]) : Lb (C c * Q) = c * Lb Q := by
  rw [← smul_eq_C_mul, Lb_smul]

lemma Lb_monomial (n : ℕ) (a : ℚ) : Lb (monomial n a) = a * _root_.bernoulli n := by
  unfold Lb
  rw [Polynomial.sum_monomial_index _ _ (by simp)]

lemma Lb_X_pow (n : ℕ) : Lb (X ^ n) = _root_.bernoulli n := by
  rw [← monomial_one_right_eq_X_pow, Lb_monomial, one_mul]

lemma Lb_sum {ι : Type*} (s : Finset ι) (f : ι → ℚ[X]) : Lb (∑ i ∈ s, f i) = ∑ i ∈ s, Lb (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [Lb]
  | insert a s ha ih =>
    rw [Finset.sum_insert ha, Finset.sum_insert ha, ← ih]
    exact Lb_add _ _

lemma Lb_neg (Q : ℚ[X]) : Lb (-Q) = -Lb Q := by
  rw [show -Q = (-1 : ℚ) • Q by simp, Lb_smul]; ring

lemma Lb_sub (P Q : ℚ[X]) : Lb (P - Q) = Lb P - Lb Q := by
  rw [sub_eq_add_neg, Lb_add, Lb_neg, sub_eq_add_neg]

/-- **b=8 泛函（Lb 形）**：`τ₈(P) = Lb(P⁽⁵⁾)/720`（mo271 `tau` 的 b=8 平移，
  B₁=−1/2 约定，与 `Zeta7.Tau.kappaMinus` 配对；与 `tauPolyMinus` 的桥接恒等式
  见 §五 `tauPolyMinus_eq_tau8`）。

  注：定义置于 Lb 工具之后（Lean 要求先定义后使用）；叙述上属于 §一。 -/
noncomputable def tau8 (P : ℚ[X]) : ℚ := Lb (derivative^[5] P) / 720

/-- **b=8 泛函 `τ₈,X`**：`τ(polyPart) + Σ_r res_r·(H⁽⁷⁾_{d(r)} − X)`。 -/
noncomputable def tauX8 (A : ℚ[X]) (Pl : Finset ℤ) : ℚ[X] :=
  C (tau8 (polyPart A Pl)) + ∑ r ∈ Pl, C (resP A Pl r) * (C (H7 (dd r)) - X)

/-- **平移恒等式**：`Lb (Q(x+1)) − Lb Q = Q'(0)`。 -/
theorem Lb_shift (Q : ℚ[X]) : Lb (Q.comp (X + 1)) - Lb Q = Q.derivative.eval 0 := by
  induction Q using Polynomial.induction_on' with
  | add P Q hP hQ =>
    rw [add_comp, Lb_add, Lb_add, derivative_add, eval_add, ← hP, ← hQ]; ring
  | monomial n a =>
    rw [← C_mul_X_pow_eq_monomial, mul_comp, C_comp, X_pow_comp, Lb_C_mul, Lb_C_mul, Lb_X_pow,
      derivative_C_mul_X_pow, eval_C_mul, eval_pow, eval_X]
    rw [add_pow, Lb_sum]
    simp only [one_pow, mul_one]
    have e : ∀ k ∈ range (n + 1), Lb (X ^ k * (n.choose k : ℚ[X])) = (n.choose k : ℚ) * _root_.bernoulli k := by
      intro k _
      rw [show (X ^ k * (n.choose k : ℚ[X])) = C (n.choose k : ℚ) * X ^ k by
        rw [mul_comm]; simp, Lb_C_mul, Lb_X_pow]
    rw [Finset.sum_congr rfl e, Finset.sum_range_succ, _root_.sum_bernoulli, Nat.choose_self]
    rcases n with _ | n
    · simp
    · rcases n with _ | n
      · simp; ring
      · simp

/-- `bin k = x(x−1)⋯(x−k+1)/k!`。 -/
noncomputable def bin (k : ℕ) : ℚ[X] := C ((k.factorial : ℚ)⁻¹) * descPochhammer ℚ k

lemma bin_eval_nat (k m : ℕ) : (bin k).eval (m : ℚ) = (m.choose k : ℚ) := by
  unfold bin
  rw [eval_mul, eval_C, descPochhammer_eval_eq_descFactorial, Nat.descFactorial_eq_factorial_mul_choose]
  push_cast
  field_simp

lemma bin_zero : bin 0 = 1 := by simp [bin]

lemma bin_eval_zero {k : ℕ} (hk : 1 ≤ k) : (bin k).eval 0 = 0 := by
  have this := bin_eval_nat k 0
  simp only [Nat.cast_zero] at this
  rw [this, Nat.choose_eq_zero_of_lt hk]; simp

/-- **Pascal**：`bin (k+1) (x+1) = bin (k+1) x + bin k x`。 -/
lemma bin_comp_add_one (k : ℕ) : (bin (k + 1)).comp (X + 1) = bin (k + 1) + bin k := by
  apply poly_eq_of_nat
  intro m
  rw [eval_comp, eval_add, eval_X, eval_one, eval_add, show (m : ℚ) + 1 = ((m + 1 : ℕ) : ℚ) by
    push_cast; ring, bin_eval_nat, bin_eval_nat, bin_eval_nat, Nat.choose_succ_succ']
  push_cast; ring

lemma descPochhammer_eval_neg_one (n : ℕ) :
    (descPochhammer ℚ n).eval (-1) = (-1) ^ n * n.factorial := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [descPochhammer_succ_right, eval_mul, ih, eval_sub, eval_X, eval_natCast,
      Nat.factorial_succ]
    push_cast; ring

/-- `bin_k'(0) = (−1)^{k−1}/k`。 -/
lemma bin_derivative_eval_zero (k : ℕ) :
    (bin (k + 1)).derivative.eval 0 = (-1) ^ k / (k + 1 : ℚ) := by
  unfold bin
  rw [derivative_C_mul, eval_mul, eval_C, descPochhammer_succ_left, derivative_mul, derivative_X,
    one_mul, eval_add, eval_mul, eval_X, zero_mul, add_zero, eval_comp, eval_sub, eval_X,
    eval_one, zero_sub, descPochhammer_eval_neg_one, Nat.factorial_succ]
  push_cast
  field_simp

/-- **`Lb (bin k) = (−1)^k/(k+1)`**。 -/
theorem Lb_bin (k : ℕ) : Lb (bin k) = (-1) ^ k / (k + 1 : ℚ) := by
  have h := Lb_shift (bin (k + 1))
  rw [bin_comp_add_one, Lb_add, bin_derivative_eval_zero] at h
  linarith

/-- `x ↦ x+1` 下不变的多项式为常值。 -/
lemma eq_C_of_comp_add_one {Q : ℚ[X]} (h : Q.comp (X + 1) = Q) : Q = C (Q.eval 0) := by
  apply poly_eq_of_nat
  intro m
  rw [eval_C]
  induction m with
  | zero => simp
  | succ m ih =>
    have this := congrArg (eval (m : ℚ)) h
    rw [eval_comp, eval_add, eval_X, eval_one] at this
    push_cast; rw [this, ih]

/-- 导数在二项基下的系数。 -/
noncomputable def dcoef (j : ℕ) : ℚ := (-1) ^ (j - 1) / (j : ℚ)

/-- **二项多项式的导数**：`bin_k' = Σ_{j=1}^k (−1)^{j−1}/j · bin_{k−j}`。 -/
theorem derivative_bin (k : ℕ) :
    (bin k).derivative = ∑ j ∈ Icc 1 k, C (dcoef j) * bin (k - j) := by
  induction k with
  | zero => simp [bin]
  | succ k ih =>
    set D := (bin (k + 1)).derivative - ∑ j ∈ Icc 1 (k + 1), C (dcoef j) * bin (k + 1 - j) with hD
    suffices hD0 : D = 0 by rw [hD] at hD0; exact sub_eq_zero.mp hD0
    have hcomp : D.comp (X + 1) = D := by
      rw [hD, sub_comp, Polynomial.sum_comp]
      have h1 : (bin (k + 1)).derivative.comp (X + 1) = (bin (k + 1)).derivative + (bin k).derivative := by
        have this := congrArg derivative (bin_comp_add_one k)
        rw [derivative_comp, derivative_add, derivative_X, derivative_one, add_zero, one_mul,
          derivative_add] at this
        exact this
      rw [h1, ih]
      have h2 : ∀ j ∈ Icc 1 (k + 1), (C (dcoef j) * bin (k + 1 - j)).comp (X + 1) =
          C (dcoef j) * bin (k + 1 - j) + (if j ≤ k then C (dcoef j) * bin (k - j) else 0) := by
        intro j hj
        rw [mul_comp, C_comp]
        rw [Finset.mem_Icc] at hj
        split_ifs with hjk
        · obtain ⟨i, hi⟩ : ∃ i, k + 1 - j = i + 1 := ⟨k - j, by omega⟩
          rw [hi, bin_comp_add_one, show k - j = i by omega]; ring
        · have this : k + 1 - j = 0 := by omega
          rw [this, bin_zero, one_comp]; simp
      rw [Finset.sum_congr rfl h2, Finset.sum_add_distrib]
      have h3 : ∑ j ∈ Icc 1 (k + 1), (if j ≤ k then C (dcoef j) * bin (k - j) else 0) =
          ∑ j ∈ Icc 1 k, C (dcoef j) * bin (k - j) := by
        rw [Finset.sum_ite, Finset.sum_const_zero, add_zero]
        congr 1
        ext j; simp only [Finset.mem_filter, Finset.mem_Icc]; omega
      rw [h3]; ring
    have h0 : D.eval 0 = 0 := by
      rw [hD, eval_sub, eval_finsetSum, bin_derivative_eval_zero,
        ← Finset.sum_erase_add _ _ (show k + 1 ∈ Icc 1 (k + 1) by simp)]
      rw [Finset.sum_eq_zero]
      · simp [bin_zero, dcoef]
      · intro j hj
        rw [Finset.mem_erase, Finset.mem_Icc] at hj
        rw [eval_mul, bin_eval_zero (by omega), mul_zero]
    rw [eq_C_of_comp_add_one hcomp, h0, C_0]

/-- **Newton 展开**：`P = Σ_{k≤d} Δ^k P(0) · bin k`（`deg P ≤ d`）。 -/
theorem newton (P : ℚ[X]) {d : ℕ} (hd : P.natDegree ≤ d) :
    P = ∑ k ∈ range (d + 1), C ((fwdDiff 1)^[k] P.eval 0) * bin k := by
  apply poly_eq_of_nat
  intro m
  have h := shift_eq_sum_fwdDiff_iter (h := (1 : ℚ)) P.eval m 0
  simp only [zero_add, nsmul_eq_mul, mul_one] at h
  rw [h, eval_finsetSum]
  simp only [eval_mul, eval_C, bin_eval_nat]
  have hz : ∀ k, d < k → (fwdDiff 1)^[k] P.eval 0 = 0 := fun k hk => by
    rw [Polynomial.fwdDiff_iter_eq_zero_of_degree_lt (by omega)]; rfl
  have hz' : ∀ k, m < k → (m.choose k : ℚ) = 0 := fun k hk => by
    rw [Nat.choose_eq_zero_of_lt hk]; simp
  have e1 : ∑ k ∈ range (m + 1), (m.choose k : ℚ) * (fwdDiff 1)^[k] P.eval 0 =
      ∑ k ∈ range (m + d + 1), (m.choose k : ℚ) * (fwdDiff 1)^[k] P.eval 0 := by
    apply Finset.sum_subset (Finset.range_subset_range.mpr (by omega))
    intro k hk hk'
    rw [Finset.mem_range] at hk hk'
    rw [hz' k (by omega), zero_mul]
  have e2 : ∑ k ∈ range (d + 1), (fwdDiff 1)^[k] P.eval 0 * (m.choose k : ℚ) =
      ∑ k ∈ range (m + d + 1), (fwdDiff 1)^[k] P.eval 0 * (m.choose k : ℚ) := by
    apply Finset.sum_subset (Finset.range_subset_range.mpr (by omega))
    intro k hk hk'
    rw [Finset.mem_range] at hk hk'
    rw [hz k (by omega), zero_mul]
  rw [e1, e2]
  exact Finset.sum_congr rfl fun k _ => mul_comm _ _

/-- `Q` 是 `bin 0, …, bin k` 的系数赋值 ≥ r 的组合。 -/
def BinRep (p : ℕ) (k : ℕ) (r : ℚ) (Q : ℚ[X]) : Prop :=
  ∃ e : ℕ → ℚ, Q = ∑ m ∈ range (k + 1), C (e m) * bin m ∧ ∀ m ≤ k, VG p (e m) r

lemma derivative_bin' {k m : ℕ} (hm : m ≤ k) :
    (bin m).derivative = ∑ n ∈ range (k + 1), C (if n < m then dcoef (m - n) else 0) * bin n := by
  rw [derivative_bin]
  symm
  rw [← Finset.sum_filter_add_sum_filter_not (range (k + 1)) (fun n => n < m)]
  rw [Finset.sum_eq_zero (s := (range (k + 1)).filter fun n => ¬ n < m)
    (fun n hn => by rw [Finset.mem_filter] at hn; rw [if_neg hn.2, C_0, zero_mul]), add_zero]
  apply Finset.sum_nbij' (fun n => m - n) (fun j => m - j)
  · intro n hn; simp only [Finset.mem_filter, Finset.mem_range, Finset.coe_filter,
      Set.mem_ofPred_eq] at hn ⊢; simp only [Finset.mem_Icc]; omega
  · intro j hj; simp only [Finset.mem_Icc, Finset.coe_Icc, Set.mem_Icc] at hj ⊢
    simp only [Finset.mem_filter, Finset.mem_range]; omega
  · intro n hn; simp only [Finset.mem_filter, Finset.mem_range, Finset.coe_filter,
      Set.mem_ofPred_eq] at hn; omega
  · intro j hj; simp only [Finset.coe_Icc, Set.mem_Icc, Finset.mem_coe, Finset.mem_Icc] at hj; omega
  · intro n hn
    simp only [Finset.mem_filter, Finset.mem_range, Finset.coe_filter, Set.mem_ofPred_eq] at hn
    rw [if_pos hn.2, show m - (m - n) = n by omega]

lemma VG_dcoef {j k : ℕ} (hj : 1 ≤ j) (hjk : j ≤ k) : VG p (dcoef j) (-(Nat.log p k : ℚ)) := by
  unfold dcoef
  rw [div_eq_mul_inv]
  have h1 : VG p ((-1 : ℚ) ^ (j - 1)) 0 := by
    rcases neg_one_pow_eq_or ℚ (j - 1) with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  simpa using h1.mul (VG.inv_nat hj hjk)

/-- 求导在二项基下至多损失 `⌊log_p k⌋`。 -/
theorem BinRep.derivative {k : ℕ} {r : ℚ} {Q : ℚ[X]} (h : BinRep p k r Q) :
    BinRep p k (r - Nat.log p k) Q.derivative := by
  obtain ⟨e, rfl, he⟩ := h
  refine ⟨fun n => ∑ m ∈ range (k + 1), e m * (if n < m then dcoef (m - n) else 0), ?_, ?_⟩
  · rw [Polynomial.derivative_sum]
    simp_rw [derivative_mul, derivative_C, zero_mul, zero_add]
    rw [Finset.sum_congr rfl fun m hm => by
      rw [derivative_bin' (Nat.lt_succ_iff.mp (Finset.mem_range.mp hm)), Finset.mul_sum]]
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun n _ => ?_
    rw [map_sum, Finset.sum_mul]
    refine Finset.sum_congr rfl fun m _ => ?_
    rw [C_mul]; ring
  · intro n _
    apply VG.sum
    intro m hm
    have hmk : m ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hm)
    split_ifs with hnm
    · have this := (he m hmk).mul (VG_dcoef (p := p) (j := m - n) (k := k) (by omega) (by omega))
      simpa [sub_eq_add_neg] using this
    · rw [mul_zero]; exact VG.zero _

/-- Bernoulli 泛函至多损失 `⌊log_p (k+1)⌋`。 -/
theorem BinRep.Lb {k : ℕ} {r : ℚ} {Q : ℚ[X]} (h : BinRep p k r Q) :
    VG p (Lb Q) (r - Nat.log p (k + 1)) := by
  obtain ⟨e, rfl, he⟩ := h
  rw [Lb_sum]
  apply VG.sum
  intro m hm
  have hmk : m ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hm)
  rw [Lb_C_mul, Lb_bin, div_eq_mul_inv]
  have h1 : VG p ((-1 : ℚ) ^ m) 0 := by
    rcases neg_one_pow_eq_or ℚ m with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  have h2 : VG p (((m : ℚ) + 1)⁻¹) (-(Nat.log p (k + 1) : ℚ)) := by
    have this := VG.inv_nat (p := p) (j := m + 1) (n := k + 1) (by omega) (by omega)
    simpa using this
  have this := (he m hmk).mul (h1.mul h2)
  simpa [sub_eq_add_neg] using this

lemma BinRep.mono {k : ℕ} {r s : ℚ} {Q : ℚ[X]} (h : BinRep p k r Q) (hs : s ≤ r) :
    BinRep p k s Q := by
  obtain ⟨e, he, hv⟩ := h
  exact ⟨e, he, fun m hm => (hv m hm).mono hs⟩

/-- 整数点值 `0,…,d` 给出二项表示。 -/
theorem binRep_of_values {P : ℚ[X]} {d : ℕ} (hd : P.natDegree ≤ d) {β : ℚ}
    (hv : ∀ m ≤ d, VG p (P.eval (m : ℚ)) β) : BinRep p d β P := by
  refine ⟨fun k => (fwdDiff 1)^[k] P.eval 0, newton P hd, fun k hk => ?_⟩
  show VG p ((fwdDiff 1)^[k] P.eval 0) β
  rw [fwdDiff_iter_eq_sum_shift]
  apply VG.sum
  intro j hj
  have hjd : j ≤ d := by have this := Finset.mem_range.mp hj; omega
  rw [zero_add, zsmul_eq_mul, nsmul_eq_mul, mul_one]
  have h1 : VG p (((-1 : ℤ) ^ (k - j) * (k.choose j : ℤ) : ℤ) : ℚ) 0 := VG.intCast _
  have this := h1.mul (hv j hjd)
  simpa using this

lemma VG_inv_720 : VG p ((720 : ℚ)⁻¹) (-(padicValNat p 720 : ℚ)) := by
  apply VG.inv (by norm_num)
  rw [show (720 : ℚ) = ((720 : ℕ) : ℚ) by norm_num, padicValRat.of_nat]
  exact le_refl _

/-! ## 四、b-相关核心：调和界 `VG_H7`（已证）-/

/-- **调和界（b=8）**：`j < p²` 时 `v_p(H⁽⁷⁾_j) ≥ −7`。
由 `harmonic7_val_aux`（`v_p ≥ −7⌊log_p j⌋`）与 `j < p² ⟹ ⌊log_p j⌋ ≤ 1` 合成。
对应 b=6 的 `VG_H5`（−5）；−7 是损耗表 §C7 第 ② 行的常数来源。 -/
lemma VG_H7 {m : ℕ} (hm : m < p ^ 2) : VG p (H7 m) (-7) := by
  have hpm : p.Prime := hp.out
  haveI : Fact p.Prime := ⟨hpm⟩
  apply VG.of_eq
  intro _
  have h := harmonic7_val_aux p m hpm
  have hlog : Nat.log p m ≤ 1 := by
    rcases Nat.eq_zero_or_pos m with h0 | hpos
    · rw [h0, Nat.log_zero_right]; omega
    · exact Nat.lt_succ_iff.mp
        (Nat.log_lt_of_lt_pow (Nat.pos_iff_ne_zero.mp hpos) hm)
  have hQ : (-7 : ℚ) * ((Nat.log p m : ℕ) : ℚ) ≤ (padicValRat p (H7 m) : ℚ) := by
    exact_mod_cast h
  have hlogQ : ((Nat.log p m : ℕ) : ℚ) ≤ 1 := by exact_mod_cast hlog
  have hnn : (0 : ℚ) ≤ ((Nat.log p m : ℕ) : ℚ) := by exact_mod_cast Nat.zero_le _
  linarith

/-- `p ≥ 7` 时 `p ∤ 720 = 2⁴·3²·5`（机器素数区，κ 常数项无 p-进损耗）。 -/
lemma padicValNat_720 (hp7 : 7 ≤ p) : padicValNat p 720 = 0 := by
  apply padicValNat.eq_zero_of_not_dvd
  intro h
  have h1 : p ≤ 720 := Nat.le_of_dvd (by norm_num) h
  have hpr := hp.out
  interval_cases p <;> first | omega | (norm_num at hpr) | (norm_num at h)

/-! ## 五、合成链目标陈述（sorry，附证明路线）-/

/-- **目标 1（b=8 版 `tau_bound`，已证）**：`P` 次数 ≤ d、整数点值 `v_p ≥ β` ⟹
  `v_p(τ₈(P)) ≥ β − 6⌊log_p(d+1)⌋ − v_p(720)`。

  损耗核算（修正此前 `7⌊log_p⌋ + (1 + v_p(720))` 的高估登记）：BinRep 机制
  给出导数链每次至多损失 `⌊log_p k⌋`，五次求导（b=8 用 `derivative^[5]`）合计
  `5⌊log_p(d+1)⌋`，`Lb` 再损失 `⌊log_p(d+1)⌋`，共 `6⌊log_p(d+1)⌋`
  （b=6 为 3+1=4，同构；`1 +` 项并入：von Staudt 的 −1 在 `Lb` 的
  `−⌊log_p(d+1)⌋` 中已被吸收，`Lb (bin 0) = 1` 恒正，故无常数 `+1`）。
  分母损耗即 `v_p(720)`（720 = 2⁴·3²·5，机器素数区 p ≥ 7 时为 0，
  见 `padicValNat_720`）。

  证明：逐行镜像 `Apery/Arith/TauBound.lean` 的 `tau_bound`
  （`binRep_of_values` ⟹ `BinRep.derivative` ×5 ⟹ `BinRep.Lb` ⟹
  `mul (VG_inv_720)` ⟹ `mono`）。 -/
theorem tau8_bound {P : ℚ[X]} {d : ℕ} (hd : P.natDegree ≤ d) {β : ℚ}
    (hv : ∀ m ≤ d, VG p (P.eval (m : ℚ)) β) :
    VG p (tau8 P) (β - 6 * Nat.log p (d + 1) - padicValNat p 720) := by
  have h0 := binRep_of_values hd hv
  have hl : (Nat.log p d : ℚ) ≤ Nat.log p (d + 1) := by
    exact_mod_cast Nat.log_mono_right (Nat.le_succ d)
  have h5 : BinRep p d (β - 5 * Nat.log p (d + 1)) (derivative^[5] P) := by
    have := h0.derivative.derivative.derivative.derivative.derivative
    simp only [Function.iterate_succ, Function.iterate_zero, Function.comp_apply, id]
    exact this.mono (by linarith)
  have := h5.Lb.mul (VG_inv_720 (p := p))
  unfold tau8
  rw [div_eq_mul_inv]
  refine this.mono ?_
  linarith

/-- `derivative^[5]` 保持加性（`derivative` 为线性映射，迭代保持 `map_add`，
  由内向外逐层rewrite）。 -/
lemma iterate_derivative_five_add (P Q : ℚ[X]) :
    derivative^[5] (P + Q) = derivative^[5] P + derivative^[5] Q := by
  simp only [Function.iterate_succ, Function.iterate_zero, Function.comp_apply, id]
  rw [map_add, map_add, map_add, map_add, map_add]

/-- `derivative^[5]` 与常数乘交换。 -/
lemma iterate_derivative_five_C_mul (c : ℚ) (P : ℚ[X]) :
    derivative^[5] (C c * P) = C c * derivative^[5] P := by
  simp only [Function.iterate_succ, Function.iterate_zero, Function.comp_apply, id]
  rw [derivative_C_mul, derivative_C_mul, derivative_C_mul, derivative_C_mul,
    derivative_C_mul]

lemma tau8_zero : tau8 0 = 0 := by
  unfold tau8 Lb
  simp [Function.iterate_succ_apply]

lemma tau8_add (P Q : ℚ[X]) : tau8 (P + Q) = tau8 P + tau8 Q := by
  unfold tau8
  rw [iterate_derivative_five_add, Lb_add, add_div]

lemma tau8_C_mul (c : ℚ) (P : ℚ[X]) : tau8 (C c * P) = c * tau8 P := by
  unfold tau8
  rw [iterate_derivative_five_C_mul, Lb_C_mul, mul_div_assoc]

/-- `tau8` 在单项式展开下逐项取值（线性泛函的 `as_sum_support_C_mul_X_pow` 形式）。 -/
lemma tau8_eq_sum (P : ℚ[X]) :
    tau8 P = ∑ i ∈ P.support, P.coeff i * tau8 (X ^ i) := by
  conv_lhs => rw [Polynomial.as_sum_support_C_mul_X_pow P]
  have hsum : ∀ (s : Finset ℕ) (f : ℕ → ℚ[X]),
      tau8 (∑ i ∈ s, f i) = ∑ i ∈ s, tau8 (f i) := by
    intro s f
    induction s using Finset.induction_on with
    | empty => simp [tau8_zero]
    | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.sum_insert ha, ← ih, tau8_add]
  rw [hsum]
  refine Finset.sum_congr rfl fun i _ => ?_
  exact tau8_C_mul _ _

/-- **单项式核**：`kappaMinus i = tau8 (X^i) = (i)₅·B_{i−5}/720`（B₁=−1/2）。 -/
lemma kappaMinus_eq_tau8_X_pow (i : ℕ) : kappaMinus i = tau8 (X ^ i) := by
  have hτ : tau8 (X ^ i) = ((i.descFactorial 5 : ℕ) : ℚ) * _root_.bernoulli (i - 5) / 720 := by
    unfold tau8
    rw [Polynomial.iterate_derivative_X_pow_eq_natCast_mul, ← C_eq_natCast, Lb_C_mul, Lb_X_pow]
  rw [hτ]
  rcases lt_or_ge i 5 with hi | hi
  · have hdf : i.descFactorial 5 = 0 := Nat.descFactorial_eq_zero_iff_lt.mpr hi
    rw [hdf, Nat.cast_zero, zero_mul, zero_div]
    have hne : i ≠ 6 := by omega
    unfold kappaMinus
    rw [if_neg hne, kappa_eq_zero_of_lt_five hi, sub_zero]
  · unfold kappaMinus
    rcases eq_or_ne i 6 with h6 | h6
    · subst i
      rw [if_pos rfl]
      have hk : kappa 6 = 1 / 2 := by
        norm_num [kappa, bernClassic, Finset.prod_Ico_eq_prod_range,
          Finset.prod_range_succ]
      rw [hk]
      have hdfn : (6 : ℕ).descFactorial 5 = 720 := by decide
      rw [hdfn]
      norm_num [_root_.bernoulli_one]
    · rw [if_neg h6, sub_zero]
      unfold kappa
      rw [bernClassic_eq_bernoulli', bernoulli'_eq_ite,
        if_neg (show i - 5 ≠ 1 by omega)]
      congr 1
      congr 1
      rw [Finset.prod_Ico_eq_prod_range, show i + 1 - (i - 4) = 5 by omega,
        Nat.descFactorial_eq_prod_range]
      conv_rhs => rw [← Finset.prod_range_reflect]
      rw [Nat.cast_prod]
      refine Finset.prod_congr rfl fun x hx => ?_
      rw [Finset.mem_range] at hx
      congr 1
      omega

/-- **桥接恒等式（已证，2026-09-25）**：`tauPolyMinus P = tau8 P`
  （`kappaMinus` 世界与 Lb 世界一致）。

  `Zeta7.Tau.kappaMinus m = kappa m − [m=6]`，其中 `kappa` 用
  `bernoulli'`（B₁ = +1/2）定义。由 `bernoulli'_eq_ite` 知
  `kappaMinus m = (m)₅·B_{m−5}/720` 对 **`_root_.bernoulli`**（B₁ = −1/2）
  全 m 成立：m = 6 情形 `kappa 6 − 1 = 720·(1/2)/720 − 1 = −1/2
  = 720·(−1/2)/720`（`bernoulli_one`）；其余 m 两约定一致。

  证明：`tau8` 对 `as_sum_support_C_mul_X_pow` 逐项取值（线性引理
  `tau8_add`/`tau8_C_mul`），单项式核为 `kappaMinus_eq_tau8_X_pow`
  （`iterate_derivative_X_pow_eq_natCast_mul` + `Lb_C_mul`/`Lb_X_pow`；
  乘积侧 `prod_Ico_eq_prod_range` 对 `descFactorial_eq_prod_range` +
  `prod_range_reflect` 逐项 omega）。 -/
theorem tauPolyMinus_eq_tau8 (P : ℚ[X]) : tauPolyMinus P = tau8 P := by
  rw [tau8_eq_sum]
  unfold tauPolyMinus
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [kappaMinus_eq_tau8_X_pow i]

/-- **多项式部分的值界（已证，2026-09-25 移植完成）**：`P = polyPart` 在
  整数点 `m` 满足 `v_p(P(m)) ≥ β`，只要 `β ≤ e_c − ℓ_c` 对每个 mod p 类成立。

  移植自 `Apery/Arith/DirectPoly.lean` 的 `VG_polyPart_eval`（整条证明
  b-无关）。结构：按模 p 类把极点分裂为同类集 `Plc` 与异类集 `Plo`；
  部分分式给出 `A = Πc·H + Πo·I`（`hAHI`）；在 `x = m` 处直接估
  `P(m) = H(m)/Πo(m) − Σ res_r/(m−r)`（Part A，异类倒数 `p`-整）；
  代换 `x = m + pz` 后 `F := p^{−e}(A∘G − Πo∘G·I∘G)` 为 `p`-整多项式
  且以 `ρ(Plc)` 为根，经 `factor_roots` 分解得 `H(m)` 的赋值
  `≥ e − ℓ`（Part B）；合并（Part C）。关键输入：`GV_numOf_comp`、
  `VG_res`、`lin_comp_eq`、`factor_roots`、`partial_fractionsP`。 -/
theorem VG_polyPart_eval8 (κ : ℚ) (hκ : VG p κ 0) (Z : Multiset ℤ) (Pl : Finset ℤ)
    (hsep : Sep p Pl) (β : ℚ) (hβ : ∀ c : ZMod p, β ≤ (cnt p Z c : ℚ) - (plc p Pl c).card)
    (m : ℤ) :
    VG p ((polyPart (numOf κ Z) Pl).eval (m : ℚ)) β := by
  classical
  set A := numOf κ Z with hA
  set P := polyPart A Pl with hP
  set c : ZMod p := (m : ZMod p) with hc
  set Plc := plc p Pl c with hPlc
  set Plo := Pl.filter fun r : ℤ => ¬ (r : ZMod p) = c with hPlo
  set PiC := ∏ r ∈ Plc, (X - C (r : ℚ)) with hPiC
  set PiO := ∏ r ∈ Plo, (X - C (r : ℚ)) with hPiO
  have hPi : piPl Pl = PiC * PiO := by
    unfold piPl; rw [hPiC, hPiO, hPlc, plc, Finset.prod_filter_mul_prod_filter_not]
  set H := P * PiO + ∑ r ∈ Plo, C (resP A Pl r) * ∏ s ∈ Plo.erase r, (X - C (s : ℚ)) with hH
  set I := ∑ r ∈ Plc, C (resP A Pl r) * ∏ s ∈ Plc.erase r, (X - C (s : ℚ)) with hI
  -- 分裂恒等式
  have hAHI : A = PiC * H + PiO * I := by
    have hpf := partial_fractionsP A Pl
    rw [← Finset.sum_filter_add_sum_filter_not Pl (fun r : ℤ => (r : ZMod p) = c)] at hpf
    have h1 : ∀ r ∈ Pl.filter (fun r : ℤ => (r : ZMod p) = c),
        C (resP A Pl r) * ∏ s ∈ Pl.erase r, (X - C (s : ℚ)) =
          PiO * (C (resP A Pl r) * ∏ s ∈ Plc.erase r, (X - C (s : ℚ))) := by
      intro r hr
      rw [prod_erase_split Pl (fun s : ℤ => (s : ZMod p) = c) r]
      have hro : r ∉ Plo := by
        rw [hPlo, Finset.mem_filter]; rw [Finset.mem_filter] at hr; tauto
      rw [Finset.erase_eq_of_notMem hro]
      rw [hPlc, plc]; ring
    have h2 : ∀ r ∈ Pl.filter (fun r : ℤ => ¬ (r : ZMod p) = c),
        C (resP A Pl r) * ∏ s ∈ Pl.erase r, (X - C (s : ℚ)) =
          PiC * (C (resP A Pl r) * ∏ s ∈ Plo.erase r, (X - C (s : ℚ))) := by
      intro r hr
      rw [prod_erase_split Pl (fun s : ℤ => (s : ZMod p) = c) r]
      have hrc : r ∉ Plc := by
        rw [hPlc, plc, Finset.mem_filter]; rw [Finset.mem_filter] at hr; tauto
      rw [show (Pl.filter fun s : ℤ => (s : ZMod p) = c).erase r = Plc by
        rw [hPlc, plc]; exact Finset.erase_eq_of_notMem hrc]
      rw [hPiC]; ring
    rw [Finset.sum_congr rfl h1, Finset.sum_congr rfl h2, ← Finset.mul_sum, ← Finset.mul_sum,
      hPi] at hpf
    have e1 : (Pl.filter fun r : ℤ => (r : ZMod p) = c) = Plc := by rw [hPlc, plc]
    have e2 : (Pl.filter fun r : ℤ => ¬ (r : ZMod p) = c) = Plo := by rw [hPlo]
    rw [e1, e2] at hpf
    conv_lhs => rw [hpf]
    rw [hH, hI, hP]; ring
  -- 成员事实
  have hmemc : ∀ r ∈ Plc, r ∈ Pl ∧ (r : ZMod p) = c := fun r hr => by
    rw [hPlc, plc, Finset.mem_filter] at hr; exact hr
  have hmemo : ∀ r ∈ Plo, r ∈ Pl ∧ ¬ (r : ZMod p) = c := fun r hr => by
    rw [hPlo, Finset.mem_filter] at hr; exact hr
  have hdiv : ∀ r ∈ Plc, (p : ℤ) ∣ r - m := fun r hr =>
    (zmod_eq_iff_dvd (p := p)).mp (by rw [(hmemc r hr).2, hc])
  have hndiv : ∀ r ∈ Plo, ¬ (p : ℤ) ∣ m - r := fun r hr hd =>
    (hmemo r hr).2 (by rw [hc]; exact ((zmod_eq_iff_dvd (p := p)).mpr hd).symm)
  -- Part A：`P(m) = H(m)/Πo(m) − Σ res_r/(m − r)`
  have hfac : ∀ r ∈ Plo, ((m : ℚ) - r) ≠ 0 := fun r hr h => hndiv r hr (by
    have this : m - r = 0 := by exact_mod_cast h
    rw [this]; exact dvd_zero _)
  have hPiOm : PiO.eval (m : ℚ) = ∏ r ∈ Plo, ((m : ℚ) - r) := by
    rw [hPiO, eval_prod]; simp
  have hPiOne : PiO.eval (m : ℚ) ≠ 0 := by
    rw [hPiOm]; exact Finset.prod_ne_zero_iff.mpr hfac
  have hVGinv : ∀ r ∈ Plo, VG p ((m : ℚ) - r)⁻¹ 0 := fun r hr => by
    refine (VG.inv (p := p) (r := 0) (hfac r hr) ?_).mono (by norm_num)
    rw [show ((m : ℚ) - r) = ((m - r : ℤ) : ℚ) by push_cast; ring,
      padicValRat_int_eq_zero (hndiv r hr)]; simp
  have hVGinvPiO : VG p (PiO.eval (m : ℚ))⁻¹ 0 := by
    refine (VG.inv (p := p) (r := 0) hPiOne ?_).mono (by norm_num)
    rw [hPiOm, padicValRat_finset_prod _ _ hfac]
    push_cast
    rw [Finset.sum_eq_zero fun r hr => by
      rw [show ((m : ℚ) - r) = ((m - r : ℤ) : ℚ) by push_cast; ring,
        padicValRat_int_eq_zero (hndiv r hr)]; simp]
  have hEo : ∀ r ∈ Plo, (∏ s ∈ Plo.erase r, (X - C (s : ℚ))).eval (m : ℚ) =
      PiO.eval (m : ℚ) * ((m : ℚ) - r)⁻¹ := by
    intro r hr
    have h := Finset.mul_prod_erase Plo (fun s : ℤ => X - C (s : ℚ)) hr
    rw [← hPiO] at h
    have h2 := congrArg (eval (m : ℚ)) h
    rw [eval_mul, eval_sub, eval_X, eval_C] at h2
    rw [← h2]; field_simp [hfac r hr]
  have hPm : P.eval (m : ℚ) = H.eval (m : ℚ) * (PiO.eval (m : ℚ))⁻¹ -
      ∑ r ∈ Plo, resP A Pl r * ((m : ℚ) - r)⁻¹ := by
    rw [hH, eval_add, eval_mul, eval_finsetSum]
    simp only [eval_mul, eval_C]
    rw [Finset.sum_congr rfl fun r hr => by rw [hEo r hr]]
    rw [add_mul, Finset.sum_mul]
    field_simp
    ring_nf
  -- Part B：代换 `x = m + pz`
  set G : ℚ[X] := C (m : ℚ) + C (p : ℚ) * X with hG
  set e : ℕ := cnt p Z c with he
  set ℓ : ℕ := Plc.card with hℓ
  set ρ : ℤ → ℚ := fun r => (((r - m) / p : ℤ) : ℚ) with hρ
  set T : ℚ[X] := ∏ r ∈ Plc, (X - C (ρ r)) with hT
  have hp0 : (p : ℚ) ≠ 0 := by exact_mod_cast hp.out.ne_zero
  have hPiCcomp : PiC.comp G = C ((p : ℚ) ^ ℓ) * T := by
    rw [hPiC, Polynomial.prod_comp, Finset.prod_congr rfl fun r hr => lin_comp_eq (hdiv r hr),
      Finset.prod_mul_distrib, Finset.prod_const, ← C_pow]
  have hAcomp : A.comp G = PiC.comp G * H.comp G + PiO.comp G * I.comp G := by
    conv_lhs => rw [hAHI]
    rw [add_comp, mul_comp, mul_comp]
  have hGA : GV p (A.comp G) e := by rw [hA, he, hc]; exact GV_numOf_comp κ hκ Z m
  have hGPiO : GV p (PiO.comp G) 0 := by
    rw [hPiO, Polynomial.prod_comp]
    exact (GV.prod (p := p) Plo (r := fun _ => (0 : ℚ)) fun r _ => GV_lin_comp m r).mono (by simp)
  have hGI : GV p (I.comp G) e := by
    rw [hI, Polynomial.sum_comp]
    refine GV.sum _ fun r hr => ?_
    rw [mul_comp, C_comp, Polynomial.prod_comp]
    have hprod : GV p (∏ s ∈ Plc.erase r, (X - C (s : ℚ)).comp G) ((Plc.erase r).card) := by
      exact (GV.prod (p := p) (Plc.erase r) (r := fun _ => (1 : ℚ)) fun s hs =>
        GV_lin_comp_class m s (by rw [(hmemc s (Finset.mem_of_mem_erase hs)).2, hc])).mono
        (by simp)
    have hres := VG_res κ hκ Z Pl hsep (hmemc r hr).1
    have hrc : (r : ZMod p) = c := (hmemc r hr).2
    rw [hrc, ← hPlc, ← he] at hres
    have this := GV.C_mul hres hprod
    refine this.mono (le_of_eq ?_)
    rw [Finset.card_erase_of_mem hr]
    have this : 1 ≤ Plc.card := Finset.card_pos.mpr ⟨r, hr⟩
    push_cast [this]; ring
  have hRHS : GV p (A.comp G - PiO.comp G * I.comp G) e :=
    hGA.sub ((hGPiO.mul hGI).mono (by simp))
  set F : ℚ[X] := C ((p : ℚ) ^ (-(e : ℤ))) * (A.comp G - PiO.comp G * I.comp G) with hF
  have hFint : GV p F 0 := by
    have this := GV.C_mul (VG.primePow (p := p) (-(e : ℤ))) hRHS
    refine this.mono (le_of_eq ?_); push_cast; ring
  have hFeq : F = T * (C ((p : ℚ) ^ ((ℓ : ℤ) - e)) * H.comp G) := by
    rw [hF, show A.comp G - PiO.comp G * I.comp G = PiC.comp G * H.comp G by rw [hAcomp]; ring,
      hPiCcomp]
    have hz : (p : ℚ) ^ (-(e : ℤ)) * (p : ℚ) ^ ℓ = (p : ℚ) ^ ((ℓ : ℤ) - e) := by
      rw [← zpow_natCast, ← zpow_add₀ hp0]; ring_nf
    rw [← hz, C_mul]; ring
  have hroot : ∀ x ∈ Plc.image ρ, F.eval x = 0 := by
    intro x hx
    rw [Finset.mem_image] at hx
    obtain ⟨r, hr, rfl⟩ := hx
    rw [hFeq, eval_mul, hT, eval_prod]
    rw [Finset.prod_eq_zero hr (by simp), zero_mul]
  have hρint : ∀ x ∈ Plc.image ρ, VG p x 0 := by
    intro x hx
    rw [Finset.mem_image] at hx
    obtain ⟨r, _, rfl⟩ := hx
    exact VG.intCast _
  obtain ⟨S, hS, hFS⟩ := factor_roots (Plc.image ρ) hρint hFint hroot
  have hinj : Set.InjOn ρ Plc := by
    intro r hr s hs h
    have h1 : ((r - m) / p : ℤ) = (s - m) / p := by
      have h' : ((((r - m) / p : ℤ) : ℚ)) = (((s - m) / p : ℤ) : ℚ) := h
      exact_mod_cast h'
    have h2 := Int.ediv_mul_cancel (hdiv r hr)
    have h3 := Int.ediv_mul_cancel (hdiv s hs)
    have this : r - m = s - m := by rw [← h2, ← h3, h1]
    omega
  rw [Finset.prod_image hinj, ← hT] at hFS
  have hT0 : T ≠ 0 := (monic_prod_of_monic _ _ fun r _ => monic_X_sub_C _).ne_zero
  have hcancel : C ((p : ℚ) ^ ((ℓ : ℤ) - e)) * H.comp G = S :=
    mul_left_cancel₀ hT0 (hFeq.symm.trans hFS)
  have hGm : G.eval 0 = (m : ℚ) := by rw [hG]; simp
  have hHm : H.eval (m : ℚ) = (p : ℚ) ^ ((e : ℤ) - ℓ) * S.eval 0 := by
    have this := congrArg (eval 0) hcancel
    rw [eval_mul, eval_C, eval_comp, hGm] at this
    rw [← this, ← mul_assoc, ← zpow_add₀ hp0]; ring_nf; simp
  have hVGH : VG p (H.eval (m : ℚ)) ((e : ℚ) - ℓ) := by
    rw [hHm]
    have this := (VG.primePow (p := p) ((e : ℤ) - ℓ)).mul (VG.eval_zero hS)
    simpa using this
  -- Part C：合并
  rw [hPm]
  have hβc : β ≤ (e : ℚ) - ℓ := hβ c
  refine VG.sub ((hVGH.mul hVGinvPiO).mono (by linarith)) (VG.sum _ fun r hr => ?_)
  have hres := VG_res κ hκ Z Pl hsep (hmemo r hr).1
  have this := hres.mul (hVGinv r hr)
  refine this.mono ?_
  have this := hβ (r : ZMod p)
  linarith

/-- **直接界（b=8，最终目标）**：`v_p^G(τ₈,X(g)) ≥ min_c (e_c − ℓ_c) − 6`。

  组装：目标 1（`tau8_bound`，`padicValNat_720` 消去 720 项）
  + 目标 2（`VG_polyPart_eval8`）+ `VG_H7`（−7）+ `VG_res`（+1），
  完全镜像 `Apery/Arith/DirectPoly.lean` 末尾 `tauX_direct` 的证明
  （那里合成 `β − 4`，此处 `β − 6`）。

  数学内容（§C7）：此即小素数界 (3.12)-类比的单步核；常数行
  `L_p = 1 + v_p(720)`（路线 B）由此界与 κ 条件合成，
  分布公式路线 A 的额外 `v_p(C_p)` 项由 `b8_cp_shift.py` 的 C_p 界
  单独入账（本文件走路线 B，C_p 不出现）。 -/
theorem tauX8_direct (hp7 : 7 ≤ p) (κ : ℚ) (hκ : VG p κ 0) (Z : Multiset ℤ) (Pl : Finset ℤ)
    (hsep : Sep p Pl) (hH : ∀ r ∈ Pl, dd r < p ^ 2) (hdeg : Z.card - Pl.card + 1 < p ^ 2)
    (β : ℚ) (hβ : ∀ c : ZMod p, β ≤ (cnt p Z c : ℚ) - (plc p Pl c).card) :
    GV p (tauX8 (numOf κ Z) Pl) (β - 6) := by
  unfold tauX8
  refine GV.add (GV.C ?_) (GV.sum _ fun r hr => ?_)
  · have hd : (polyPart (numOf κ Z) Pl).natDegree ≤ Z.card - Pl.card :=
      (natDegree_polyPart_le _ _).trans (Nat.sub_le_sub_right (natDegree_numOf_le κ Z) _)
    have h := tau8_bound (p := p) hd (β := β) (fun m _ => by
      have := VG_polyPart_eval8 κ hκ Z Pl hsep β hβ (m : ℤ)
      simpa using this)
    have hlog : Nat.log p (Z.card - Pl.card + 1) ≤ 1 :=
      Nat.lt_succ_iff.mp (Nat.log_lt_of_lt_pow (by omega) hdeg)
    rw [padicValNat_720 hp7] at h
    refine h.mono ?_
    have : (Nat.log p (Z.card - Pl.card + 1) : ℚ) ≤ 1 := by exact_mod_cast hlog
    push_cast; linarith
  · have hres := VG_res κ hκ Z Pl hsep hr
    have hH7 : GV p (C (H7 (dd r)) - X) (-7) :=
      (GV.C (VG_H7 (hH r hr))).sub (GV.X.mono (by norm_num))
    refine (GV.C_mul hres hH7).mono ?_
    have := hβ (r : ZMod p)
    linarith

end Zeta7
