import Mathlib
import Zeta7.Arith.ClassCount

/-!
# 内区权重 (4.6)–(4.7)-类比及其有效性（镜像 `Apery/Arith/InnerWeights.lean`，b=8）

类常数 `b a = Bse p K N a`、维数 `L`、`top a = L a + (b a − 6)/2`（b=6 为 −4）：
* `w (a, i) = i + (b a − 6)/2`（`a ≠ 0`）；
* `w (0, i) = min (2 i + (b 0 − 6)/2) (min_{c ≠ 0} top c)`。

−6 与 ACI 结论的 `+ 6` 配对（入口界损失 β−6 的吸收，b=6 为 −4/+4）。
若 (P) `top a − 1 ≤ top c`（一切 `a, c ≠ 0`）与 (Z) `top a − 1 ≤ 2 L 0 + (b 0 − 6)/2`
成立，则 `v_p^G(Δ) ≥ 2 ∑ w`；capped 版 `wcap` 只需 (Z)。
-/

open Finset Polynomial

namespace Zeta7

variable {m : ℕ}

/-- `top a = L a + (b a − 6)/2`（b=8）。 -/
noncomputable def topw (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ) (a : Fin (m + 1)) : ℚ :=
  L a + (b a - 6) / 2

/-- 普通类上 `top` 的最小值。 -/
noncomputable def tmin (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ) : ℚ :=
  (Finset.univ.erase (0 : Fin (m + 1))).inf' ⟨⟨1, by omega⟩, by simp [Fin.ext_iff]⟩ (topw L b)

lemma tmin_le (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ) {c : Fin (m + 1)} (hc : c ≠ 0) :
    tmin hm L b ≤ topw L b c :=
  Finset.inf'_le _ (Finset.mem_erase.mpr ⟨hc, Finset.mem_univ _⟩)

/-- 权重。 -/
noncomputable def winner (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ)
    (s : Σ a : Fin (m + 1), Fin (L a)) : ℚ :=
  if s.1 = 0 then min (2 * (s.2 : ℚ) + (b 0 - 6) / 2) (tmin hm L b)
  else (s.2 : ℚ) + (b s.1 - 6) / 2

/-- 抽象类不等式（b=8：`+ 6`）。 -/
theorem winner_ACI (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ)
    (hP : ∀ a c : Fin (m + 1), a ≠ 0 → c ≠ 0 → topw L b a - 1 ≤ topw L b c)
    (hZ : ∀ a : Fin (m + 1), a ≠ 0 → topw L b a - 1 ≤ 2 * L 0 + (b 0 - 6) / 2)
    (s t : Σ a : Fin (m + 1), Fin (L a)) (a : Fin (m + 1)) :
    winner hm L b s + winner hm L b t + 6 ≤
      b a + (if a = 0 then 2 else 1) * ((nu L s a : ℚ) + nu L t a) := by
  -- basic facts
  have F1 : ∀ u : Σ a : Fin (m + 1), Fin (L a), u.1 ≠ 0 →
      winner hm L b u ≤ topw L b u.1 - 1 := by
    intro u hu
    unfold winner topw; rw [if_neg hu]
    have this : (u.2 : ℚ) ≤ L u.1 - 1 := by
      have this := u.2.isLt; have this : (u.2 : ℕ) + 1 ≤ L u.1 := this
      have this : ((u.2 : ℕ) : ℚ) + 1 ≤ L u.1 := by exact_mod_cast this
      linarith
    linarith
  have F3 : ∀ u : Σ a : Fin (m + 1), Fin (L a), ∀ c : Fin (m + 1), c ≠ 0 →
      winner hm L b u ≤ topw L b c := by
    intro u c hc
    by_cases hu : u.1 = 0
    · unfold winner; rw [if_pos hu]
      exact (min_le_right _ _).trans (tmin_le hm L b hc)
    · linarith [F1 u hu, hP u.1 c hu hc]
  have Fz : ∀ u : Σ a : Fin (m + 1), Fin (L a),
      winner hm L b u ≤ (if u.1 = 0 then 2 * (u.2 : ℚ) else 2 * (L 0 : ℚ)) + (b 0 - 6) / 2 := by
    intro u
    by_cases hu : u.1 = 0
    · unfold winner; rw [if_pos hu, if_pos hu]; exact min_le_left _ _
    · rw [if_neg hu]; linarith [F1 u hu, hZ u.1 hu]
  unfold nu
  by_cases ha : a = 0
  · subst ha
    rw [if_pos rfl, show (((0 : Fin (m + 1)) : ℕ)) = 0 from rfl]
    have h1 := Fz s; have h2 := Fz t
    by_cases hs : s.1 = 0 <;> by_cases ht : t.1 = 0
    · rw [if_pos hs.symm, if_pos ht.symm]; rw [if_pos hs] at h1; rw [if_pos ht] at h2; linarith
    · rw [if_pos hs.symm, if_neg (Ne.symm ht)]; rw [if_pos hs] at h1; rw [if_neg ht] at h2
      linarith
    · rw [if_neg (Ne.symm hs), if_pos ht.symm]; rw [if_neg hs] at h1; rw [if_pos ht] at h2
      linarith
    · rw [if_neg (Ne.symm hs), if_neg (Ne.symm ht)]; rw [if_neg hs] at h1; rw [if_neg ht] at h2
      linarith
  · rw [if_neg ha, one_mul]
    have htop : b a - 6 = 2 * (topw L b a - L a) := by unfold topw; ring
    by_cases hs : a = s.1 <;> by_cases ht : a = t.1
    · rw [if_pos hs, if_pos ht]
      have e1 : winner hm L b s = (s.2 : ℚ) + (b a - 6) / 2 := by
        unfold winner; rw [if_neg (hs ▸ ha)]; simp only [hs]
      have e2 : winner hm L b t = (t.2 : ℚ) + (b a - 6) / 2 := by
        unfold winner; rw [if_neg (ht ▸ ha)]; simp only [ht]
      rw [e1, e2]; linarith
    · rw [if_pos hs, if_neg ht]
      have e1 : winner hm L b s = (s.2 : ℚ) + (b a - 6) / 2 := by
        unfold winner; rw [if_neg (hs ▸ ha)]; simp only [hs]
      have this := F3 t a ha
      rw [e1]; unfold topw at this; linarith
    · rw [if_neg hs, if_pos ht]
      have e2 : winner hm L b t = (t.2 : ℚ) + (b a - 6) / 2 := by
        unfold winner; rw [if_neg (ht ▸ ha)]; simp only [ht]
      have this := F3 s a ha
      rw [e2]; unfold topw at this; linarith
    · rw [if_neg hs, if_neg ht]
      have h1 := F3 s a ha; have h2 := F3 t a ha
      unfold topw at h1 h2; linarith

/-- **满足 (P)(Z) 的分配的区内行列式界（b=8）。** -/
theorem inner_bound {p : ℕ} [Fact p.Prime] (hp7 : 7 ≤ p) (hm : 2 * m + 1 = p) (hm1 : 1 ≤ m)
    (n : ℕ) (L : Fin (m + 1) → ℕ) (hL : ∑ c, L c = 37 * n)
    (hsep : Sep p (PlK (40 * n))) (hK : 40 * n < p ^ 2)
    (hdeg : 7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2)
    (hP : ∀ a c : Fin (m + 1), a ≠ 0 → c ≠ 0 →
      topw L (Bse p (40 * n) (3 * n)) a - 1 ≤ topw L (Bse p (40 * n) (3 * n)) c)
    (hZ : ∀ a : Fin (m + 1), a ≠ 0 → topw L (Bse p (40 * n) (3 * n)) a - 1 ≤
      2 * L 0 + (Bse p (40 * n) (3 * n) 0 - 6) / 2) :
    GV p (Δ n) (2 * ∑ s, winner hm1 L (Bse p (40 * n) (3 * n)) s) := by
  refine class_frame hp7 hm n L hL _ hsep hK hdeg fun s t c => ?_
  rw [classCount_eq hm]
  exact winner_ACI hm1 L _ hP hZ s t (ccls hm c)

/-! ### Capped 权重：有效性只需零类条件 -/

/-- 未 capped 权重。 -/
noncomputable def wraw (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ) (s : Σ a : Fin (m + 1), Fin (L a)) : ℚ :=
  if s.1 = 0 then 2 * (s.2 : ℚ) + (b 0 - 6) / 2 else (s.2 : ℚ) + (b s.1 - 6) / 2

/-- Capped 权重 `min (wraw) (min_{c ≠ 0} top c)`。 -/
noncomputable def wcap (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ)
    (s : Σ a : Fin (m + 1), Fin (L a)) : ℚ :=
  min (wraw L b s) (tmin hm L b)

theorem wcap_ACI (hm : 1 ≤ m) (L : Fin (m + 1) → ℕ) (b : ℕ → ℚ)
    (hZ : tmin hm L b ≤ 2 * L 0 + (b 0 - 6) / 2)
    (s t : Σ a : Fin (m + 1), Fin (L a)) (a : Fin (m + 1)) :
    wcap hm L b s + wcap hm L b t + 6 ≤
      b a + (if a = 0 then 2 else 1) * ((nu L s a : ℚ) + nu L t a) := by
  have F3 : ∀ u : Σ a : Fin (m + 1), Fin (L a), ∀ c : Fin (m + 1), c ≠ 0 →
      wcap hm L b u ≤ topw L b c := fun u c hc =>
    (min_le_right _ _).trans (tmin_le hm L b hc)
  have Fraw : ∀ u : Σ a : Fin (m + 1), Fin (L a), wcap hm L b u ≤ wraw L b u :=
    fun u => min_le_left _ _
  have Fz : ∀ u : Σ a : Fin (m + 1), Fin (L a),
      wcap hm L b u ≤ (if u.1 = 0 then 2 * (u.2 : ℚ) else 2 * (L 0 : ℚ)) + (b 0 - 6) / 2 := by
    intro u
    by_cases hu : u.1 = 0
    · rw [if_pos hu]; have this := Fraw u; unfold wraw at this; rw [if_pos hu] at this; exact this
    · rw [if_neg hu]; exact (min_le_right _ _).trans hZ
  unfold nu
  by_cases ha : a = 0
  · subst ha
    rw [if_pos rfl, show (((0 : Fin (m + 1)) : ℕ)) = 0 from rfl]
    have h1 := Fz s; have h2 := Fz t
    by_cases hs : s.1 = 0 <;> by_cases ht : t.1 = 0
    · rw [if_pos hs.symm, if_pos ht.symm]; rw [if_pos hs] at h1; rw [if_pos ht] at h2; linarith
    · rw [if_pos hs.symm, if_neg (Ne.symm ht)]; rw [if_pos hs] at h1; rw [if_neg ht] at h2
      linarith
    · rw [if_neg (Ne.symm hs), if_pos ht.symm]; rw [if_neg hs] at h1; rw [if_pos ht] at h2
      linarith
    · rw [if_neg (Ne.symm hs), if_neg (Ne.symm ht)]; rw [if_neg hs] at h1; rw [if_neg ht] at h2
      linarith
  · rw [if_neg ha, one_mul]
    have hraw : ∀ u : Σ a : Fin (m + 1), Fin (L a), a = u.1 →
        wcap hm L b u ≤ (u.2 : ℚ) + (b a - 6) / 2 := by
      intro u hu
      have this := Fraw u
      unfold wraw at this; rw [if_neg (hu ▸ ha)] at this; simpa only [hu] using this
    by_cases hs : a = s.1 <;> by_cases ht : a = t.1
    · rw [if_pos hs, if_pos ht]
      have this := hraw s hs; have this := hraw t ht; linarith
    · rw [if_pos hs, if_neg ht]
      have this := hraw s hs; have h2 := F3 t a ha
      unfold topw at h2; linarith
    · rw [if_neg hs, if_pos ht]
      have this := hraw t ht; have h2 := F3 s a ha
      unfold topw at h2; linarith
    · rw [if_neg hs, if_neg ht]
      have h1 := F3 s a ha; have h2 := F3 t a ha
      unfold topw at h1 h2; linarith

/-- **Capped 权重的区内行列式界（b=8）；只需零类条件 (Z)。** -/
theorem inner_bound_cap {p : ℕ} [Fact p.Prime] (hp7 : 7 ≤ p) (hm : 2 * m + 1 = p) (hm1 : 1 ≤ m)
    (n : ℕ) (L : Fin (m + 1) → ℕ) (hL : ∑ c, L c = 37 * n)
    (hsep : Sep p (PlK (40 * n))) (hK : 40 * n < p ^ 2)
    (hdeg : 7 + 2 * (24 * n + 2 * (37 * n)) - 2 * (40 * n) + 1 < p ^ 2)
    (hZ : tmin hm1 L (Bse p (40 * n) (3 * n)) ≤
      2 * L 0 + (Bse p (40 * n) (3 * n) 0 - 6) / 2) :
    GV p (Δ n) (2 * ∑ s, wcap hm1 L (Bse p (40 * n) (3 * n)) s) := by
  refine class_frame hp7 hm n L hL _ hsep hK hdeg fun s t c => ?_
  rw [classCount_eq hm]
  exact wcap_ACI hm1 L _ hZ s t (ccls hm c)

end Zeta7
