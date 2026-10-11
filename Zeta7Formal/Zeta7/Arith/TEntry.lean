import Mathlib
import Zeta7.Arith.Pullback
import Zeta7.Arith.DirectBound

/-!
# 分子 `∏ (t + γ²)` 的入口界（镜像 `Apery/Arith/TEntry.lean`，b=8）

对整数多重集 `M`，`tpol M = ∏_{γ ∈ M} (t + γ²)`。其 pullback 为
`pull8 K (tpol M) = ± x⁷ ∏_{γ ∈ M} (x − γ)(x + γ)`（b=6 为 x⁵），
故直接界适用于 `μ_X(tpol M / D_K)`。
-/

open Finset Polynomial

namespace Zeta7

/-- `∏_{γ ∈ M} (t + γ²)`。 -/
noncomputable def tpol (M : Multiset ℤ) : ℚ[X] :=
  (M.map fun γ : ℤ => X + C ((γ : ℚ) ^ 2)).prod

lemma tpol_add (M M' : Multiset ℤ) : tpol (M + M') = tpol M * tpol M' := by
  simp [tpol, Multiset.map_add, Multiset.prod_add]

/-- `tpol M` 的 pullback 的 `x`-根（b=8：`X⁷` 贡献 7 个 0 根）。 -/
def xroots (M : Multiset ℤ) : Multiset ℤ :=
  Multiset.replicate 7 0 + M + M.map (fun γ => -γ)

lemma pull_tpol8 (K : ℕ) (M : Multiset ℤ) :
    pull8 K (tpol M) = numOf ((-1 : ℚ) ^ (K + M.card)) (xroots M) := by
  unfold pull8 tpol numOf xroots
  rw [multiset_prod_comp, Multiset.map_map]
  simp only [Multiset.map_add, Multiset.prod_add, Multiset.map_replicate, Multiset.prod_replicate]
  have h1 : ∀ γ : ℤ, ((fun q : ℚ[X] => q.comp (-X ^ 2)) ∘ fun γ : ℤ => X + C ((γ : ℚ) ^ 2)) γ =
      C (-1 : ℚ) * ((X - C (γ : ℚ)) * (X - C ((-γ : ℤ) : ℚ))) := by
    intro γ
    simp only [Function.comp, add_comp, X_comp, C_comp]
    push_cast
    rw [map_neg, map_one, C_neg, C_pow]; ring
  rw [Multiset.map_congr rfl fun γ _ => h1 γ, Multiset.prod_map_mul, Multiset.prod_map_mul]
  simp only [Multiset.map_const', Multiset.prod_replicate, Multiset.map_map, Function.comp]
  simp only [Int.cast_zero, map_zero, sub_zero]
  rw [pow_add, map_mul, map_pow, map_pow]
  ring

/-- `x`-根在 mod p 类 `c` 中的数目。 -/
lemma cnt_xroots (p : ℕ) (M : Multiset ℤ) (c : ZMod p) :
    cnt p (xroots M) c = (if c = 0 then 7 else 0) +
      (M.filter fun γ : ℤ => (γ : ZMod p) = c).card +
      (M.filter fun γ : ℤ => (γ : ZMod p) = -c).card := by
  unfold cnt xroots
  rw [Multiset.filter_add, Multiset.filter_add, Multiset.card_add, Multiset.card_add]
  congr 1
  · congr 1
    by_cases h : (0 : ZMod p) = c
    · rw [if_pos h.symm, Multiset.filter_eq_self.mpr (fun a ha => by
        rw [Multiset.eq_of_mem_replicate ha]; simpa using h)]
      simp
    · rw [if_neg (Ne.symm h), Multiset.filter_eq_nil.mpr (fun a ha => by
        rw [Multiset.eq_of_mem_replicate ha]; simpa using h)]
      simp
  · rw [Multiset.filter_map, Multiset.card_map]
    congr 1
    refine Multiset.filter_congr fun γ _ => ?_
    simp only [Function.comp, Int.cast_neg]
    constructor <;> intro h <;> [rw [← h]; rw [h]] <;> ring

/-- **`μ_X(tpol M / D_K)` 的入口界（b=8）**：`v_p^G ≥ β − 6`
（b=6 为 `μX_tpol_bound` 的 β − 4；次数条件 `7 + 2·M.card − 2K + 1 < p²`
来自 `xroots` 的 7 + 2·M.card 个根）。 -/
theorem μX_tpol_bound {p : ℕ} [Fact p.Prime] (hp7 : 7 ≤ p) (K : ℕ) (M : Multiset ℤ)
    (hsep : Sep p (PlK K)) (hK : K < p ^ 2) (hdeg : 7 + 2 * M.card - 2 * K + 1 < p ^ 2) (β : ℚ)
    (hβ : ∀ c : ZMod p, β ≤ ((if c = 0 then 7 else 0) +
      (M.filter fun γ : ℤ => (γ : ZMod p) = c).card +
      (M.filter fun γ : ℤ => (γ : ZMod p) = -c).card : ℕ) - (plc p (PlK K) c).card) :
    GV p (μX K (tpol M)) (β - 6) := by
  rw [μX_eq_tauX8, pull_tpol8]
  have hκ : VG p ((-1 : ℚ) ^ (K + M.card)) 0 := by
    rcases neg_one_pow_eq_or ℚ (K + M.card) with h | h <;> rw [h]
    · exact VG.one
    · exact VG.one.neg
  refine tauX8_direct hp7 _ hκ _ _ hsep ?_ ?_ β ?_
  · intro r hr
    rw [PlK, Finset.mem_union, Finset.mem_image, Finset.mem_image] at hr
    rcases hr with ⟨j, hj, rfl⟩ | ⟨j, hj, rfl⟩
    · rw [dd_nat]; have this := (Finset.mem_Icc.mp hj).2; omega
    · rw [dd_neg (Finset.mem_Icc.mp hj).1]; have this := (Finset.mem_Icc.mp hj).2; omega
  · have this : (xroots M).card = 7 + 2 * M.card := by
      simp [xroots]; ring
    rw [this, card_PlK]; exact hdeg
  · intro c
    rw [cnt_xroots]; exact hβ c

end Zeta7
