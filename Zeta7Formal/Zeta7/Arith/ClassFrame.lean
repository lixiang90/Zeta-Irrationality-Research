import Mathlib
import Zeta7.Arith.TEntry
import Zeta7.Arith.Unimodular

/-!
# 类基框架（镜像 `Apery/Arith/ClassFrame.lean`，b=8）

类 `a = 0, …, m`（`p = 2m + 1`），维数 `L a`（`∑ L = h`），基多项式
`E_{a,i} = ∏_{c ≠ a} (t + c²)^{L_c} (t + a²)^i`（`i < L a`）。
若权重 `w` 满足每类入口不等式，则 `v_p^G(Δ) ≥ 2 ∑ w`（`class_frame`）。

b=8 差异：`entryRoots` 的 `D_N` 幂 6→8（nsmul 系数）、`classCount` 的
零点类贡献 5→7、`class_frame` 的入口平移 +4→+6（配 `μX_tpol_bound` 的 β−6）。
-/

open Finset Polynomial

namespace Zeta7

/-- 基多项式 `E_{a,i}` 的 `t`-根。 -/
def classRoots {m : ℕ} (L : Fin (m + 1) → ℕ) (a : Fin (m + 1)) (i : ℕ) : Multiset ℤ :=
  (∑ c ∈ Finset.univ.erase a, Multiset.replicate (L c) ((c : ℕ) : ℤ)) +
    Multiset.replicate i ((a : ℕ) : ℤ)

lemma card_classRoots {m : ℕ} (L : Fin (m + 1) → ℕ) (a : Fin (m + 1)) (i : ℕ) :
    (classRoots L a i).card = ∑ c ∈ Finset.univ.erase a, L c + i := by
  simp [classRoots, Multiset.card_sum]

/-- `ℤ` 上的 `∏_{γ ∈ M} (t + γ²)`。 -/
noncomputable def tpolZ (M : Multiset ℤ) : ℤ[X] := (M.map fun γ : ℤ => X + C (γ ^ 2)).prod

lemma tpolZ_map_Q (M : Multiset ℤ) : (tpolZ M).map (Int.castRingHom ℚ) = tpol M := by
  simp [tpolZ, tpol, Polynomial.map_multiset_prod, Multiset.map_map, Function.comp]

lemma natDegree_tpolZ (M : Multiset ℤ) : (tpolZ M).natDegree ≤ M.card := by
  unfold tpolZ
  refine (natDegree_multiset_prod_le _).trans ?_
  rw [Multiset.map_map]
  have this : ∀ γ ∈ M, (natDegree ∘ fun γ : ℤ => X + C (γ ^ 2)) γ = 1 := fun γ _ =>
    natDegree_X_add_C _
  rw [Multiset.map_congr rfl this, Multiset.map_const', Multiset.sum_replicate, smul_eq_mul,
    mul_one]

lemma prod_map_sum_replicate {α β : Type*} [CommMonoid β] (s : Finset α) (L : α → ℕ) (v : α → ℤ)
    (g : ℤ → β) :
    ((∑ c ∈ s, Multiset.replicate (L c) (v c)).map g).prod = ∏ c ∈ s, g (v c) ^ L c := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [Finset.sum_insert ha, Multiset.map_add, Multiset.prod_add, ih, Finset.prod_insert ha,
      Multiset.map_replicate, Multiset.prod_replicate]

lemma tpolZ_map_ZMod (p : ℕ) {m : ℕ} (L : Fin (m + 1) → ℕ) (a : Fin (m + 1)) (i : ℕ) :
    (tpolZ (classRoots L a i)).map (Int.castRingHom (ZMod p)) =
      (∏ c ∈ Finset.univ.erase a, (X - C (-(((c : ℕ) : ZMod p) ^ 2))) ^ L c) *
        (X - C (-(((a : ℕ) : ZMod p) ^ 2))) ^ i := by
  unfold tpolZ classRoots
  rw [Polynomial.map_multiset_prod, Multiset.map_map, Multiset.map_add, Multiset.prod_add,
    prod_map_sum_replicate, Multiset.map_replicate, Multiset.prod_replicate]
  simp [Function.comp, sub_eq_add_neg]

/-- `D_m` 作为 `tpol`。 -/
lemma D_eq_tpol (m : ℕ) : D m = tpol ((Icc 1 m).val.map fun j : ℕ => (j : ℤ)) := by
  unfold D tpol
  rw [Multiset.map_map, Finset.prod_eq_multiset_prod]
  congr 1

lemma tpol_nsmul (k : ℕ) (M : Multiset ℤ) : tpol (k • M) = tpol M ^ k := by
  induction k with
  | zero => simp [tpol]
  | succ k ih => rw [succ_nsmul, tpol_add, ih, pow_succ]

/-- `0, …, m` 的平方在模 `p = 2m + 1` 下互异。 -/
lemma sq_injective {p m : ℕ} [hp : Fact p.Prime] (hm : 2 * m + 1 = p) :
    Function.Injective fun c : Fin (m + 1) => -(((c : ℕ) : ZMod p) ^ 2) := by
  intro c c' h
  simp only [neg_inj] at h
  have h2 : (p : ℤ) ∣ ((c : ℕ) - (c' : ℕ) : ℤ) * ((c : ℕ) + (c' : ℕ) : ℤ) := by
    rw [← ZMod.intCast_zmod_eq_zero_iff_dvd]; push_cast
    linear_combination h
  have hc := c.isLt; have hc' := c'.isLt
  rcases (Int.Prime.dvd_mul' hp.out h2) with h3 | h3
  · have this := Int.eq_zero_of_abs_lt_dvd h3 (by rw [abs_lt]; constructor <;> push_cast <;> omega)
    exact Fin.ext (by omega)
  · have this := Int.eq_zero_of_abs_lt_dvd h3 (by rw [abs_lt]; constructor <;> push_cast <;> omega)
    exact Fin.ext (by omega)

/-- 分子 `D_N⁸ E_s E_t` 的 `t`-根（b=8：`8 •`，b=6 为 `6 •`）。 -/
def entryRoots {m : ℕ} (N : ℕ) (L : Fin (m + 1) → ℕ) (s t : Σ a : Fin (m + 1), Fin (L a)) :
    Multiset ℤ :=
  8 • ((Icc 1 N).val.map fun j : ℕ => (j : ℤ)) + classRoots L s.1 s.2 + classRoots L t.1 t.2

/-- 入口界中出现的每类计数（b=8：零点类贡献 7，b=6 为 5）。 -/
noncomputable def classCount (p : ℕ) (K : ℕ) (M : Multiset ℤ) (c : ZMod p) : ℚ :=
  (((if c = 0 then 7 else 0) + (M.filter fun γ : ℤ => (γ : ZMod p) = c).card +
    (M.filter fun γ : ℤ => (γ : ZMod p) = -c).card : ℕ) : ℚ) - (plc p (PlK K) c).card

/-- **类基框架（b=8）**：`v_p^G(Δ) ≥ 2 ∑ w`。 -/
theorem class_frame {p : ℕ} [hp : Fact p.Prime] (hp7 : 7 ≤ p) {m : ℕ} (hm : 2 * m + 1 = p)
    (n : ℕ) (L : Fin (m + 1) → ℕ) (hL : ∑ c, L c = 37 * n)
    (w : (Σ a : Fin (m + 1), Fin (L a)) → ℚ)
    (hsep : Sep p (PlK (40 * n))) (hK : 40 * n < p ^ 2)
    (hdeg : 7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2)
    (hentry : ∀ s t : (Σ a : Fin (m + 1), Fin (L a)), ∀ c : ZMod p,
      w s + w t + 6 ≤ classCount p (40 * n) (entryRoots (3 * n) L s t) c) :
    GV p (Δ n) (2 * ∑ s, w s) := by
  classical
  have hcard : Fintype.card (Σ a : Fin (m + 1), Fin (L a)) = 37 * n := by
    rw [Fintype.card_sigma]; simpa using hL
  set e : (Σ a : Fin (m + 1), Fin (L a)) ≃ Fin (37 * n) := Fintype.equivFinOfCardEq hcard
  set R : Fin (37 * n) → Multiset ℤ := fun k => classRoots L (e.symm k).1 (e.symm k).2
  have hRcard : ∀ k, (R k).card < 37 * n := by
    intro k
    rw [card_classRoots]
    have h1 := Finset.add_sum_erase Finset.univ L (Finset.mem_univ (e.symm k).1)
    have this := (e.symm k).2.isLt
    omega
  set E : Fin (37 * n) → ℚ[X] := fun k => tpol (R k)
  set Ez : Fin (37 * n) → ℤ[X] := fun k => tpolZ (R k)
  have hEz : ∀ k, (Ez k).map (Int.castRingHom ℚ) = E k := fun k => tpolZ_map_Q _
  have hdegZ : ∀ k, (Ez k).natDegree < 37 * n := fun k => (natDegree_tpolZ _).trans_lt (hRcard k)
  have hdegE : ∀ k, (E k).natDegree < 37 * n := fun k => by
    rw [← hEz]; exact (natDegree_map_le).trans_lt (hdegZ k)
  -- 单模性
  have hunit := coeffMat_det_unit (p := p) Ez hdegZ
    (fun c : Fin (m + 1) => -(((c : ℕ) : ZMod p) ^ 2))
    (sq_injective hm) L (fun k => (e.symm k).1) (fun k => (e.symm k).2)
    (fun k => (e.symm k).2.isLt)
    (fun k k' h1 h2 => by
      apply e.symm.injective
      exact Sigma.ext h1 (by
        rw [Fin.heq_ext_iff (by rw [h1])]; exact h2))
    (fun k => tpolZ_map_ZMod p L _ _)
  have hcoef : coeffMat E = coeffMat fun k => (Ez k).map (Int.castRingHom ℚ) := by
    simp only [hEz]
  rw [← hcoef] at hunit
  set dC := (coeffMat E).det with hdC
  -- 基变换
  have hbc := det_basis_change n E hdegE
  -- 入口界
  have hentries : ∀ k l, GV p ((Matrix.of fun a b => μX (40 * n) (D (3 * n) ^ 8 * E a * E b)) k l)
      (w (e.symm k) + w (e.symm l)) := by
    intro k l
    rw [Matrix.of_apply]
    have hM : D (3 * n) ^ 8 * E k * E l = tpol (entryRoots (3 * n) L (e.symm k) (e.symm l)) := by
      simp only [E, R, entryRoots, tpol_add, tpol_nsmul, D_eq_tpol]
    rw [hM]
    have hcardM : (entryRoots (3 * n) L (e.symm k) (e.symm l)).card ≤ 24 * n + 2 * (37 * n) := by
      simp only [entryRoots, Multiset.card_add, Multiset.card_nsmul, Multiset.card_map,
        Finset.card_val, Nat.card_Icc]
      have h1 := hRcard k; have h2 := hRcard l
      simp only [R] at h1 h2
      omega
    have this := μX_tpol_bound hp7 (40 * n) (entryRoots (3 * n) L (e.symm k) (e.symm l)) hsep hK
      (by omega) (w (e.symm k) + w (e.symm l) + 6) (fun c => hentry _ _ c)
    simpa using this
  have hdet := GV.det_GV _ (fun k => w (e.symm k)) (fun k => w (e.symm k)) hentries
  rw [hbc] at hdet
  have hsum : ∑ k, w (e.symm k) + ∑ k, w (e.symm k) = 2 * ∑ s, w s := by
    rw [Equiv.sum_comp e.symm w]; ring
  rw [hsum] at hdet
  -- 除以单位 `dC²`
  have hΔ : Δ n = C ((dC ^ 2)⁻¹) * (C (dC ^ 2) * Δ n) := by
    rw [← mul_assoc, ← C_mul, inv_mul_cancel₀ (pow_ne_zero _ hunit.1), C_1, one_mul]
  rw [hΔ]
  have hu : VG p ((dC ^ 2)⁻¹) 0 := by
    refine (VG.inv (p := p) (r := 0) (pow_ne_zero _ hunit.1) ?_).mono (by norm_num)
    rw [padicValRat.pow, hunit.2]; simp
  simpa using GV.C_mul hu hdet

end Zeta7
