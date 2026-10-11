import Mathlib
import Zeta7.PrimeSum

/-!
# 带权函数的素数和（b-无关）

`psum f a b K = ∑_{K/b < p ≤ K/a} p f(K/p) log p`。若 `f ≤ v_j` 于各 cell
`[c_j, c_{j+1}]`，则 `psum f a b K ≤ ∑_j v_j wsum (K/c_{j+1}) (K/c_j)`，
右端为 `K² ∑_j v_j (1/c_j² - 1/c_{j+1}²)/2 + o(K²)`。
镜像 `Apery/PrimeSumStep.lean`。
-/

open Finset Filter Topology Set

namespace Zeta7

/-- `∑_{K/b < p ≤ K/a} p f(K/p) log p`。 -/
noncomputable def psum (f : ℝ → ℝ) (a b K : ℝ) : ℝ :=
  ∑ k ∈ Ioc ⌊K / b⌋₊ ⌊K / a⌋₊, (k : ℝ) * cPrime k * f (K / k)

lemma cPrime_nonneg (k : ℕ) : 0 ≤ cPrime k := by
  unfold cPrime
  split_ifs with h
  · exact Real.log_nonneg (by exact_mod_cast h.one_lt.le)
  · exact le_rfl

/-- 中间点拆分。 -/
lemma psum_split (f : ℝ → ℝ) {a c b K : ℝ} (ha : 0 < a) (hac : a ≤ c) (hcb : c ≤ b) (hK : 0 ≤ K) :
    psum f a b K = psum f a c K + psum f c b K := by
  unfold psum
  rw [add_comm, Finset.sum_Ioc_consecutive _
    (Nat.floor_le_floor (div_le_div_of_nonneg_left hK (by linarith) hcb))
    (Nat.floor_le_floor (div_le_div_of_nonneg_left hK ha hac))]

/-- `f ≤ v` 于 `[a, b)` 时 `psum f a b K ≤ v * wsum (K/b) (K/a)`。 -/
lemma psum_le_of_le {f : ℝ → ℝ} {a b v K : ℝ} (ha : 0 < a) (hab : a ≤ b) (hK : 0 < K)
    (hf : ∀ x ∈ Ico a b, f x ≤ v) :
    psum f a b K ≤ v * wsum (K / b) (K / a) := by
  unfold psum wsum
  rw [Finset.mul_sum]
  refine Finset.sum_le_sum fun k hk => ?_
  rw [Finset.mem_Ioc] at hk
  have hb : 0 < b := ha.trans_le hab
  have hk0 : 0 < k := by
    have this := hk.1; omega
  have hk0' : (0 : ℝ) < k := by exact_mod_cast hk0
  have hx1 : a ≤ K / k := by
    rw [le_div_iff₀ hk0']
    have h1 : (k : ℝ) ≤ K / a := by
      have this := Nat.floor_le (div_nonneg hK.le ha.le) |>.trans' (Nat.cast_le.mpr hk.2)
      exact this
    rw [le_div_iff₀ ha] at h1
    linarith
  have hx2 : K / k < b := by
    rw [div_lt_iff₀ hk0']
    have h1 : K / b < k := by
      have this := Nat.lt_floor_add_one (K / b)
      have h2 : (⌊K / b⌋₊ : ℝ) + 1 ≤ k := by exact_mod_cast hk.1
      linarith
    rw [div_lt_iff₀ hb] at h1
    linarith
  have hc := cPrime_nonneg k
  have this := hf (K / k) ⟨hx1, hx2⟩
  calc (k : ℝ) * cPrime k * f (K / k) ≤ (k : ℝ) * cPrime k * v :=
        mul_le_mul_of_nonneg_left this (by positivity)
    _ = v * ((k : ℝ) * cPrime k) := by ring

/-- 分割 `c 0 < c 1 < ⋯ < c r` 上的阶梯和。 -/
noncomputable def stepSum (c v : ℕ → ℝ) (r : ℕ) (K : ℝ) : ℝ :=
  ∑ j ∈ range r, v j * wsum (K / c (j + 1)) (K / c j)

lemma c_zero_le {c : ℕ → ℝ} {r : ℕ} (h : ∀ j < r, c j ≤ c (j + 1)) : c 0 ≤ c r := by
  induction r with
  | zero => exact le_rfl
  | succ r ih => exact (ih fun j hj => h j (by omega)).trans (h r (by omega))

/-- `psum` 在分割上的上界（阶梯和）。 -/
lemma psum_le_stepSum {f : ℝ → ℝ} {c v : ℕ → ℝ} (r : ℕ) (hc0 : 0 < c 0)
    (hmono : ∀ j < r, c j ≤ c (j + 1)) (hf : ∀ j < r, ∀ x ∈ Ico (c j) (c (j + 1)), f x ≤ v j)
    {K : ℝ} (hK : 0 < K) :
    psum f (c 0) (c r) K ≤ stepSum c v r K := by
  induction r with
  | zero => simp [psum, stepSum]
  | succ r ih =>
    have hcr : c 0 ≤ c r := c_zero_le fun j hj => hmono j (by omega)
    rw [psum_split f hc0 hcr (hmono r (by omega)) hK.le, stepSum, Finset.sum_range_succ]
    exact add_le_add (ih (fun j hj => hmono j (by omega)) (fun j hj => hf j (by omega)))
      (psum_le_of_le (hc0.trans_le hcr) (hmono r (by omega)) hK (hf r (by omega)))

/-- 归一化阶梯和的极限。 -/
lemma stepSum_tendsto {c v : ℕ → ℝ} (r : ℕ) (hc0 : 0 < c 0) (hmono : ∀ j < r, c j < c (j + 1)) :
    Tendsto (fun K : ℝ => stepSum c v r K / K ^ 2) atTop
      (𝓝 (∑ j ∈ range r, v j * ((1 / c j ^ 2 - 1 / c (j + 1) ^ 2) / 2))) := by
  have hpos : ∀ j ≤ r, 0 < c j := by
    intro j hj
    induction j with
    | zero => exact hc0
    | succ j ih => exact (ih (by omega)).trans (hmono j (by omega))
  have e : (fun K : ℝ => stepSum c v r K / K ^ 2) =
      fun K => ∑ j ∈ range r, v j * (wsum (K / c (j + 1)) (K / c j) / K ^ 2) := by
    funext K
    unfold stepSum
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl fun j _ => ?_
    ring
  rw [e]
  refine tendsto_finsetSum _ fun j hj => ?_
  have hj := Finset.mem_range.mp hj
  exact (wsum_tendsto (hpos j hj.le) (hmono j hj)).const_mul _

/-- 最终 `psum f a b K / K² ≤ (Darboux 上和) + ε`。 -/
theorem psum_eventually_le {f : ℝ → ℝ} {c v : ℕ → ℝ} (r : ℕ) (hc0 : 0 < c 0)
    (hmono : ∀ j < r, c j < c (j + 1)) (hf : ∀ j < r, ∀ x ∈ Ico (c j) (c (j + 1)), f x ≤ v j)
    {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ K : ℝ in atTop, psum f (c 0) (c r) K / K ^ 2 ≤
      (∑ j ∈ range r, v j * ((1 / c j ^ 2 - 1 / c (j + 1) ^ 2) / 2)) + ε := by
  have h := (stepSum_tendsto (v := v) r hc0 hmono).eventually (eventually_le_nhds (by linarith :
    (∑ j ∈ range r, v j * ((1 / c j ^ 2 - 1 / c (j + 1) ^ 2) / 2)) <
      (∑ j ∈ range r, v j * ((1 / c j ^ 2 - 1 / c (j + 1) ^ 2) / 2)) + ε))
  filter_upwards [h, eventually_gt_atTop 0] with K hK hK0
  have this := psum_le_stepSum (f := f) r hc0 (fun j hj => (hmono j hj).le) hf hK0
  calc psum f (c 0) (c r) K / K ^ 2 ≤ stepSum c v r K / K ^ 2 :=
        div_le_div_of_nonneg_right this (by positivity)
    _ ≤ _ := hK

end Zeta7
