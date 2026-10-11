import Mathlib
import Zeta7.Arith.InnerWeights

/-!
# 内区分配（water filling）（镜像 `Apery/Arith/InnerAlloc.lean`，b=8）

类 `c ≠ 0` 带整数偏移 `β c`（类 `c` 的行权重为 `i + β c / 2`）。
在水平 `k`（权重 `< k/2`）下，类 `c` 获得 `lrow k (β c) = ⌈(k − β c)/2⌉⁺` 行。
取最大可行水平 `kf ∈ [klo, ktop]`（至多使用 `h − L0min` 行），其余行归入零类。则

* 分配对 `inner_bound_cap` 有效（零类条件）；
* `∑ wcap ≥ Φ(kf) − B₀`，`Φ(k) = h k/2 − ∑_c ψ(k, β c)` 关于 `k` 凹；
* `Φ(kf) ≥ Φ(k) − (k − klo) L0min / 2` 对一切 `k ∈ [klo, ktop]`。

b=8 差异：`hβ : b c = (β c : ℚ) + 6`（b=6 为 +4，与权重位移 −6 配对）、
零类赤字的 `(b 0 − 6)/2`（b=6 为 −4）。
-/

open Finset

namespace Zeta7

/-- 水平 `k` 下偏移 `β` 的行数：`⌈(k − β)/2⌉⁺`。 -/
def lrow (k β : ℤ) : ℕ := ((k - β + 1) / 2).toNat

lemma lrow_ge (k β : ℤ) : ((k : ℚ) - β) / 2 ≤ lrow k β := by
  unfold lrow
  have h1 : (k - β + 1) / 2 ≤ ((k - β + 1) / 2).toNat := Int.self_le_toNat _
  have h2 : k - β ≤ 2 * ((k - β + 1) / 2) := by omega
  have h3 : ((k - β : ℤ) : ℚ) ≤ 2 * (((k - β + 1) / 2).toNat : ℤ) := by
    exact_mod_cast h2.trans (by omega)
  push_cast at h3
  linarith

lemma lrow_lt {k β : ℤ} {i : ℕ} (hi : i < lrow k β) : 2 * (i : ℚ) + β < k := by
  unfold lrow at hi
  have this : 2 * (i : ℤ) + β < k := by omega
  exact_mod_cast this

lemma lrow_le_max (k β : ℤ) : (lrow k β : ℚ) + β / 2 ≤ max (β : ℚ) (k + 1) / 2 := by
  unfold lrow
  rcases le_or_gt (k - β + 1) 0 with h | h
  · have this : ((k - β + 1) / 2).toNat = 0 := by omega
    rw [this]; push_cast
    have this := le_max_left (β : ℚ) (k + 1); linarith
  · have e : (((k - β + 1) / 2).toNat : ℤ) ≤ (k - β + 1) / 2 := by omega
    have e2 : 2 * ((k - β + 1) / 2) ≤ k - β + 1 := by omega
    have e3 : ((((k - β + 1) / 2).toNat : ℤ) : ℚ) * 2 ≤ ((k - β + 1 : ℤ) : ℚ) := by
      exact_mod_cast (by omega : (((k - β + 1) / 2).toNat : ℤ) * 2 ≤ k - β + 1)
    push_cast at e3
    have this := le_max_right (β : ℚ) (k + 1); linarith

lemma lrow_mono {k k' : ℤ} (h : k ≤ k') (β : ℤ) : lrow k β ≤ lrow k' β := by
  unfold lrow; omega

lemma lrow_succ (k β : ℤ) :
    lrow (k + 1) β = lrow k β ∨ (lrow (k + 1) β = lrow k β + 1 ∧ 2 * (lrow k β : ℤ) + β = k) := by
  unfold lrow; omega

/-- `ψ(k, β) = ∑_{i < lrow} (k/2 − i − β/2)`。 -/
noncomputable def psiR (k β : ℤ) : ℚ := ∑ i ∈ range (lrow k β), (((k : ℚ) - 2 * i - β) / 2)

lemma psiR_succ (k β : ℤ) : psiR (k + 1) β = psiR k β + (lrow (k + 1) β : ℚ) / 2 := by
  unfold psiR
  rcases lrow_succ k β with h | ⟨h, h2⟩
  · rw [h, show (lrow k β : ℚ) / 2 = ∑ _i ∈ range (lrow k β), (1 / 2 : ℚ) by simp; ring,
      ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_; push_cast; ring
  · rw [h, Finset.sum_range_succ]
    have h2' : 2 * ((lrow k β : ℕ) : ℚ) + β = k := by exact_mod_cast h2
    rw [show ((lrow k β + 1 : ℕ) : ℚ) / 2 = ∑ _i ∈ range (lrow k β), (1 / 2 : ℚ) + 1 / 2 by
      simp; ring]
    have this : ∑ i ∈ range (lrow k β), (((k + 1 : ℤ) : ℚ) - 2 * i - β) / 2 =
        ∑ i ∈ range (lrow k β), ((((k : ℚ) - 2 * i - β) / 2) + 1 / 2) := by
      refine Finset.sum_congr rfl fun i _ => ?_; push_cast; ring
    rw [this, Finset.sum_add_distrib]
    push_cast
    linarith

variable {m : ℕ}

/-- 水平 `k` 使用的行数。 -/
def rowsK (β : Fin (m + 1) → ℤ) (k : ℤ) : ℕ :=
  ∑ c ∈ univ.erase (0 : Fin (m + 1)), lrow k (β c)

/-- `Φ(k) = h k / 2 − ∑ ψ`。 -/
noncomputable def PhiK (β : Fin (m + 1) → ℤ) (h : ℕ) (k : ℤ) : ℚ :=
  (h : ℚ) * k / 2 - ∑ c ∈ univ.erase (0 : Fin (m + 1)), psiR k (β c)

lemma PhiK_succ (β : Fin (m + 1) → ℤ) (h : ℕ) (k : ℤ) :
    PhiK β h (k + 1) = PhiK β h k + ((h : ℚ) - rowsK β (k + 1)) / 2 := by
  unfold PhiK rowsK
  simp only [psiR_succ, Finset.sum_add_distrib, ← Finset.sum_div]
  push_cast
  ring

lemma rowsK_mono (β : Fin (m + 1) → ℤ) {k k' : ℤ} (h : k ≤ k') :
    rowsK β k ≤ rowsK β k' :=
  Finset.sum_le_sum fun c _ => lrow_mono h _

/-- 选取的水平。 -/
noncomputable def kfSel (β : Fin (m + 1) → ℤ) (h L0min : ℕ) (klo ktop : ℤ) : ℤ :=
  klo + (Nat.findGreatest (fun j : ℕ => rowsK β (klo + j) + L0min ≤ h) (ktop - klo).toNat : ℤ)

section
variable (β : Fin (m + 1) → ℤ) (h L0min : ℕ) (klo ktop : ℤ)

lemma kfSel_feasible (hlo : rowsK β klo + L0min ≤ h) :
    rowsK β (kfSel β h L0min klo ktop) + L0min ≤ h := by
  unfold kfSel
  have this := Nat.findGreatest_spec (P := fun j : ℕ => rowsK β (klo + j) + L0min ≤ h)
    (n := (ktop - klo).toNat) (Nat.zero_le _) (by simpa using hlo)
  exact this

lemma kfSel_ge : klo ≤ kfSel β h L0min klo ktop := by unfold kfSel; omega

lemma kfSel_le (hk : klo ≤ ktop) : kfSel β h L0min klo ktop ≤ ktop := by
  unfold kfSel
  have this := Nat.findGreatest_le (P := fun j : ℕ => rowsK β (klo + j) + L0min ≤ h)
    (n := (ktop - klo).toNat)
  omega

lemma kfSel_max {k : ℤ} (hk1 : kfSel β h L0min klo ktop < k) (hk2 : k ≤ ktop) :
    h < rowsK β k + L0min := by
  unfold kfSel at hk1
  have hj := Nat.findGreatest_is_greatest (P := fun j : ℕ => rowsK β (klo + j) + L0min ≤ h)
    (n := (ktop - klo).toNat) (k := (k - klo).toNat) (by omega) (by omega)
  simp only [not_le] at hj
  rwa [show klo + ((k - klo).toNat : ℤ) = k by omega] at hj

/-- **凹性比较**：`[klo, ktop]` 上 `Φ(k) ≤ Φ(kf) + (k − klo) L0min / 2`。 -/
theorem PhiK_le_kf (hlo : rowsK β klo + L0min ≤ h) {k : ℤ} (hk1 : klo ≤ k) (hk2 : k ≤ ktop) :
    PhiK β h k ≤ PhiK β h (kfSel β h L0min klo ktop) + ((k - klo : ℤ) : ℚ) * L0min / 2 := by
  have hfeas := kfSel_feasible β h L0min klo ktop hlo
  have hge := kfSel_ge β h L0min klo ktop
  have hmax : ∀ k', kfSel β h L0min klo ktop < k' → k' ≤ ktop →
      h < rowsK β k' + L0min :=
    fun k' h1 h2 => kfSel_max β h L0min klo ktop h1 h2
  generalize kfSel β h L0min klo ktop = kf at *
  have hL0 : (0 : ℚ) ≤ L0min := by positivity
  rcases le_or_gt k kf with hle | hgt
  · -- `kf` 以下每步非负
    obtain ⟨t, rfl⟩ : ∃ t : ℕ, kf = k + t := ⟨(kf - k).toNat, by omega⟩
    have this : ∀ s : ℕ, s ≤ t → PhiK β h k ≤ PhiK β h (k + s) := by
      intro s
      induction s with
      | zero => intro _; simp
      | succ s ih =>
        intro hs
        have this := ih (by omega)
        rw [show k + ((s + 1 : ℕ) : ℤ) = (k + s) + 1 by push_cast; ring, PhiK_succ]
        have hr : rowsK β (k + s + 1) ≤ rowsK β (k + t) := rowsK_mono β (by omega)
        have this : ((rowsK β (k + s + 1) : ℕ) : ℚ) ≤ h := by
          exact_mod_cast (by omega : rowsK β (k + s + 1) ≤ h)
        linarith
    have h1 := this t le_rfl
    have this : (0 : ℚ) ≤ ((k - klo : ℤ) : ℚ) := by exact_mod_cast (by omega : (0 : ℤ) ≤ k - klo)
    nlinarith
  · -- `kf` 以上每步小于 `L0min / 2`
    obtain ⟨t, rfl⟩ : ∃ t : ℕ, k = kf + t := ⟨(k - kf).toNat, by omega⟩
    have this : ∀ s : ℕ, s ≤ t →
        PhiK β h (kf + s) ≤ PhiK β h kf + (s : ℚ) * L0min / 2 := by
      intro s
      induction s with
      | zero => intro _; simp
      | succ s ih =>
        intro hs
        have this := ih (by omega)
        rw [show kf + ((s + 1 : ℕ) : ℤ) = (kf + s) + 1 by push_cast; ring, PhiK_succ]
        have hr := hmax (kf + s + 1) (by omega) (by omega)
        have this : (h : ℚ) < rowsK β (kf + s + 1) + L0min := by exact_mod_cast hr
        push_cast
        linarith
    have h1 := this t le_rfl
    have this : (t : ℚ) ≤ ((kf + t - klo : ℤ) : ℚ) := by
      have this : ((t : ℤ) : ℚ) ≤ ((kf + t - klo : ℤ) : ℚ) := by exact_mod_cast (by omega)
      simpa using this
    nlinarith
end

/-- 分配。 -/
noncomputable def allocK (β : Fin (m + 1) → ℤ) (h : ℕ) (kf : ℤ) (c : Fin (m + 1)) : ℕ :=
  if c = 0 then h - rowsK β kf else lrow kf (β c)

lemma sum_allocK (β : Fin (m + 1) → ℤ) (h : ℕ) (kf : ℤ) (hkf : rowsK β kf ≤ h) :
    ∑ c, allocK β h kf c = h := by
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : Fin (m + 1)))]
  unfold allocK
  rw [if_pos rfl, Finset.sum_congr rfl (fun c hc => if_neg (Finset.mem_erase.mp hc).1)]
  unfold rowsK at hkf ⊢
  omega

/-- 零类赤字：`∑_{i<L} (D − 2i)⁺ ≤ D⁺ (D⁺/2 + 1)`。 -/
lemma sum_deficit_le (D : ℚ) (L : ℕ) :
    ∑ i ∈ range L, max 0 (D - 2 * i) ≤ max 0 D * (max 0 D / 2 + 1) := by
  set E := max 0 D with hE
  have hE0 : 0 ≤ E := le_max_left _ _
  set N0 := ⌊E / 2⌋₊ + 1 with hN0
  have hz : ∀ i, N0 ≤ i → max 0 (D - 2 * i) = 0 := by
    intro i hi
    have this : E / 2 < (N0 : ℚ) := by rw [hN0]; push_cast; exact Nat.lt_floor_add_one _
    have this : (N0 : ℚ) ≤ i := by exact_mod_cast hi
    apply max_eq_left
    have this := le_max_right 0 D; linarith
  have h1 : ∑ i ∈ range L, max 0 (D - 2 * i) ≤ ∑ i ∈ range N0, max 0 (D - 2 * i) := by
    rw [← Finset.sum_range_add_sum_Ico _ (show min L N0 ≤ L from min_le_left _ _),
      ← Finset.sum_range_add_sum_Ico _ (show min L N0 ≤ N0 from min_le_right _ _)]
    have hA : ∑ i ∈ Ico (min L N0) L, max 0 (D - 2 * (i : ℚ)) = 0 := by
      refine Finset.sum_eq_zero fun i hi => hz i ?_
      have this := Finset.mem_Ico.mp hi; omega
    have hB : 0 ≤ ∑ i ∈ Ico (min L N0) N0, max 0 (D - 2 * (i : ℚ)) :=
      Finset.sum_nonneg fun _ _ => le_max_left _ _
    linarith
  have h2 : ∑ i ∈ range N0, max 0 (D - 2 * (i : ℚ)) ≤ ∑ _i ∈ range N0, E :=
    Finset.sum_le_sum fun i _ => max_le hE0 (by
      have h1 := le_max_right (0 : ℚ) D
      have h2 : (0 : ℚ) ≤ (i : ℚ) := by positivity
      rw [hE]; linarith)
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul] at h2
  have h3 : (N0 : ℚ) ≤ E / 2 + 1 := by
    rw [hN0]; push_cast; have this := Nat.floor_le (show 0 ≤ E / 2 by positivity); linarith
  nlinarith

section
variable (hm1 : 1 ≤ m) (b : ℕ → ℚ) (β : Fin (m + 1) → ℤ)
  (hβ : ∀ c : Fin (m + 1), c ≠ 0 → b c = (β c : ℚ) + 6)

include hβ in
lemma tmin_allocK_ge (h : ℕ) (kf : ℤ) : (kf : ℚ) / 2 ≤ tmin hm1 (allocK β h kf) b := by
  unfold tmin
  refine Finset.le_inf' _ _ fun c hc => ?_
  have hc0 := (Finset.mem_erase.mp hc).1
  unfold topw allocK
  rw [if_neg hc0, hβ c hc0]
  have this := lrow_ge kf (β c)
  linarith

include hβ in
lemma tmin_allocK_le (h : ℕ) (kf : ℤ) :
    tmin hm1 (allocK β h kf) b ≤ max (β ⟨1, by omega⟩ : ℚ) (kf + 1) / 2 := by
  have hc : (⟨1, by omega⟩ : Fin (m + 1)) ≠ 0 := by simp [Fin.ext_iff]
  refine (tmin_le hm1 _ b hc).trans ?_
  unfold topw allocK
  rw [if_neg hc, hβ _ hc]
  have this := lrow_le_max kf (β ⟨1, by omega⟩)
  linarith

include hβ in
/-- **分配的权重和**：`∑ wcap ≥ Φ(kf) − B₀`。 -/
theorem sum_wcap_allocK (h : ℕ) (kf : ℤ) (hkf : rowsK β kf ≤ h) :
    PhiK β h kf - max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2) *
        (max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2) / 2 + 1) ≤
      ∑ s, wcap hm1 (allocK β h kf) b s := by
  set L := allocK β h kf with hL
  set T := tmin hm1 L b with hT
  have hTge : (kf : ℚ) / 2 ≤ T := tmin_allocK_ge hm1 b β hβ h kf
  rw [Fintype.sum_sigma]
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : Fin (m + 1)))]
  -- 非零类
  have hnz : ∀ c ∈ univ.erase (0 : Fin (m + 1)), ∑ i : Fin (L c), wcap hm1 L b ⟨c, i⟩ =
      ∑ i ∈ range (lrow kf (β c)), ((i : ℚ) + (β c : ℚ) / 2) := by
    intro c hc
    have hc0 := (Finset.mem_erase.mp hc).1
    have hLc : L c = lrow kf (β c) := by rw [hL]; unfold allocK; rw [if_neg hc0]
    have hpt : ∀ i : Fin (L c), wcap hm1 L b ⟨c, i⟩ = ((i : ℕ) : ℚ) + (β c : ℚ) / 2 := by
      intro i
      unfold wcap wraw
      simp only
      rw [if_neg hc0, hβ c hc0, show ((β c : ℚ) + 6 - 6) / 2 = (β c : ℚ) / 2 by ring]
      apply min_eq_left
      have hi : (i : ℕ) < lrow kf (β c) := hLc ▸ i.isLt
      have this := lrow_lt hi
      linarith [hTge, hT]
    rw [Finset.sum_congr rfl (fun i _ => hpt i),
      Fin.sum_univ_eq_sum_range (fun i => (i : ℚ) + (β c : ℚ) / 2) (L c), hLc]
  -- 零类
  have hz : ((L 0 : ℕ) : ℚ) * kf / 2 - max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2) *
        (max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2) / 2 + 1) ≤
      ∑ i : Fin (L 0), wcap hm1 L b ⟨0, i⟩ := by
    have hpt : ∀ i : Fin (L 0), (kf : ℚ) / 2 - max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2 - 2 * (i : ℕ)) ≤
        wcap hm1 L b ⟨0, i⟩ := by
      intro i
      unfold wcap wraw
      simp only [ite_true]
      refine le_min ?_ ?_
      · have this := le_max_right (0 : ℚ) ((kf : ℚ) / 2 - (b 0 - 6) / 2 - 2 * (i : ℕ)); linarith
      · have this := le_max_left (0 : ℚ) ((kf : ℚ) / 2 - (b 0 - 6) / 2 - 2 * (i : ℕ))
        linarith [hTge, hT]
    refine le_trans ?_ (Finset.sum_le_sum fun i _ => hpt i)
    rw [Fin.sum_univ_eq_sum_range (fun i => (kf : ℚ) / 2 - max 0 ((kf : ℚ) / 2 - (b 0 - 6) / 2 -
      2 * (i : ℚ))) (L 0), Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
    have this := sum_deficit_le ((kf : ℚ) / 2 - (b 0 - 6) / 2) (L 0)
    linarith
  rw [Finset.sum_congr rfl hnz]
  have hL0 : L 0 = h - rowsK β kf := by rw [hL]; unfold allocK; rw [if_pos rfl]
  have hL0q : ((L 0 : ℕ) : ℚ) = (h : ℚ) - rowsK β kf := by rw [hL0]; push_cast [hkf]; ring
  have hpsi : ∀ c ∈ univ.erase (0 : Fin (m + 1)), psiR kf (β c) =
      (lrow kf (β c) : ℚ) * kf / 2 - ∑ i ∈ range (lrow kf (β c)), ((i : ℚ) + (β c : ℚ) / 2) := by
    intro c _
    unfold psiR
    rw [show (lrow kf (β c) : ℚ) * kf / 2 = ∑ _i ∈ range (lrow kf (β c)), (kf : ℚ) / 2 by
      rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; ring, ← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_; ring
  have hΦ : PhiK β h kf = (h : ℚ) * kf / 2 - ((rowsK β kf : ℕ) : ℚ) * kf / 2 +
      ∑ c ∈ univ.erase (0 : Fin (m + 1)), ∑ i ∈ range (lrow kf (β c)), ((i : ℚ) + (β c : ℚ) / 2) := by
    unfold PhiK
    rw [Finset.sum_congr rfl hpsi, Finset.sum_sub_distrib]
    unfold rowsK
    push_cast
    rw [Finset.sum_mul, Finset.sum_div]
    ring
  rw [hΦ]
  rw [hL0q] at hz
  linarith

end

end Zeta7
