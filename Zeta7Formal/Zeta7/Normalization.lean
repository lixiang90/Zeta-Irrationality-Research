import Mathlib
import Zeta7.Construction

/-!
# §5 归一化 `m_{K,M}` 的参照定义（b=8 镜像）

镜像 `Apery/Normalization.lean`（mo271，Apache-2.0）。**本文件是参照层**：
mo271 原文档已声明，证明实际使用的是 `Apery.mN`（`Apery/Norm.lean`，局部指数为
`Apery/Arith` 中**已证**的下界），本文件的论文式定义仅供参照与 `vS` 使用
（`Apery.Legendre` 经由 `InnerData.vS` 消费）。

b=8 状态（2026-09-25，`research/b8_verdict.md` 双轨判定）：
* `(3.12)` 分支已换 b=8 常数（`8·h·⌊log_p 5K⌋`、`v_p(720)`，§C7/D 钉死；
  本库 `Zeta7.Arith.DirectBound` 已证其单步核 `GV ≥ min_c(e_c−ℓ_c) − 6`）；
* **γ 机器（`gammaIn` (4.8) / `gammaOut` (4.14)）保持论文 b=6 数值**：
  判定指出论文 γ-轨对 b=8 不可行、需 mo271 式再工程（mo271 对 b=6 亦修正
  γ 机器三处），b=8 类比常数待 `Norm.lean` 镜像时按已证界重建，届时本文件的
  对应定义将同步替换。凡含此类常数处均以 `-- REF(b=6)` 标注。
-/

open Finset Polynomial

namespace Zeta7

/-- `ℓ_A(a) = #{1 ≤ j ≤ A : j ≡ ±a (mod p)}`。 -/
def ellA (p A a : ℕ) : ℕ := ((Icc 1 A).filter fun j => j % p = a % p ∨ (j + a) % p = 0).card

/-- §4.1 参数组（`K = 40n`、`N = 3n`、`h = 37n`，截断 `M`，素数 `p`）。 -/
structure InnerData where
  n : ℕ
  M : ℕ
  p : ℕ

namespace InnerData

variable (D : InnerData)

def K : ℕ := 40 * D.n
def N : ℕ := 3 * D.n
def h : ℕ := 37 * D.n
/-- REF(b=6)：内区零块长度 `4M + 10`；b=8 类比（6M + 14 型）随 γ 机器再工程定稿。 -/
def L0 : ℕ := 4 * D.M + 10
/-- `m = (p - 1)/2`。 -/
def m : ℕ := (D.p - 1) / 2
def mN : ℕ := D.N / D.p
def mK : ℕ := D.K / D.p
def ellK (a : ℕ) : ℕ := ellA D.p D.K a
def ellN (a : ℕ) : ℕ := ellA D.p D.N a
/-- `b_a = 3 ℓ_N(a)`。 -/
def b (a : ℕ) : ℕ := 3 * D.ellN a
/-- 普通行总数 `h - L₀ + 3(N - m_N)`（整数）。 -/
def total : ℤ := (D.h : ℤ) - D.L0 + 3 * ((D.N : ℤ) - D.mN)
/-- `T`（(4.4)）。 -/
def T : ℤ := D.total / D.m
/-- `E`（(4.4)）。 -/
def E : ℤ := D.total % D.m
/-- 类 `a` 按 `ℓ_K` 降序的排名（并列按指标）。 -/
def rank (a : ℕ) : ℕ :=
  ((Icc 1 D.m).filter fun c => D.ellK c > D.ellK a ∨ (D.ellK c = D.ellK a ∧ c < a)).card
/-- `ε_a = 1`（`ℓ_K` 降序前 `E` 个类）。 -/
def eps (a : ℕ) : ℤ := if (D.rank a : ℤ) < D.E then 1 else 0
/-- `L_a = T - b_a + ε_a`。 -/
def L (a : ℕ) : ℤ := D.T - D.b a + D.eps a
/-- `Z_a = T + ε_a`。 -/
def Z (a : ℕ) : ℤ := D.T + D.eps a
/-- 行权 (4.6)（`a > 0`，有理半整数）。
REF(b=6)：尾部常数 `+4 = 2s − 6`（s=5）；b=8（s=7）应为 `+6`，随再工程定稿。 -/
def w (a : ℕ) (i : ℤ) : ℚ := i + D.b a - ((D.ellK a : ℚ) + 4) / 2
/-- (4.7) 中普通类上的最小值。 -/
def w0min : ℚ :=
  if hm : 1 ≤ D.m then
    ((Icc 1 D.m).image fun c => (D.Z c : ℚ) - ((D.ellK c : ℚ) + 4) / 2).min'
      (by simpa using hm)
  else 0
/-- 零块权 (4.7)。
REF(b=6)：常数 `2i + 6mN − mK + 1/2` 为 b=6 值；`w0min` 内 `+4` 同上。 -/
def w0 (i : ℤ) : ℚ := min (2 * i + 6 * (D.mN : ℚ) - D.mK + 1 / 2) D.w0min
/-- 内区指数 `γ_p^in`（(4.8)，整数；取有理和的下整）。
REF(b=6)：权结构同上，常数随再工程定稿。 -/
def gammaIn : ℤ :=
  ⌊2 * ((∑ i ∈ range D.L0, D.w0 i) + ∑ a ∈ Icc 1 D.m, ∑ i ∈ range (D.L a).toNat, D.w a i)⌋

/-! ### 外区 (4.14)（REF(b=6)：整套常数待再工程） -/

/-- `v = K - p ⌊K/p⌋`。 -/
def v : ℕ := D.K % D.p
def u : ℤ := max 0 ((D.N : ℤ) + D.v - D.p + 1)
def tp : ℤ := min (D.N : ℤ) D.v + D.u
def rp : ℤ := max 0 ((D.K : ℤ) + 4 * D.N - 2 * D.p + 2)
/-- 外区指数 `γ_p^out`（(4.14)，`p > K` 时为 `0`）。
REF(b=6)：系数 `7`、`6`、`12`、`5`、`3` 系 s=5 极点结构（j⁴、−1/4、1/(2j)）；
b=8（j⁶、−1/6、1/(2j)）的类比按 `b8_verdict.md` 需再工程，此处保留论文原值。 -/
def gammaOut : ℤ :=
  if D.K < D.p then 0
  else if D.K < 2 * D.p then
    -7 * ((D.K : ℤ) - D.p) + 6 * D.tp - 1 - min D.rp ((D.p : ℤ) - 1 - D.N + D.u)
  else -7 * ((D.K : ℤ) - D.p) + 3 + 12 * D.N + 5 * D.tp - min D.rp ((D.p : ℤ) + D.u)

/-- `v_p(S_K)`（b=8 的 `S` 见 `Zeta7.Construction`，`(N!)^{16h}` 结构）。 -/
noncomputable def vS : ℤ := padicValRat D.p (S D.n)

/-- 局部指数 `L_p(K, M)`（(5.1)）。
**b=8 活常数**：第一分支 = (3.12)-类比（§C7/D 钉死：`8 = 7+1` 的 1 并入 log 系数，
`v_p(720)` 替换 `v_p(24)`；与 `Zeta7.Arith.DirectBound` 的已证界同构）。
第二、三分支的 `γ` 机器为 REF(b=6)。 -/
noncomputable def Lp : ℤ :=
  if D.p * D.M ≤ D.K then -8 * (D.h : ℤ) * Nat.log D.p (5 * D.K) - D.h * padicValNat D.p 720
  else if 3 * D.p ≤ D.K then D.vS + D.gammaIn
  else D.vS + D.gammaOut

end InnerData

/-- 归一化因子 `m_{K,M} = ∏_{p ≤ 2h} p^{-L_p(K,M)}`（(5.2)）。 -/
noncomputable def mKM (n M : ℕ) : ℚ :=
  ∏ p ∈ (range (2 * (37 * n) + 1)).filter Nat.Prime,
    (p : ℚ) ^ (-(InnerData.mk n M p).Lp)

lemma mKM_pos (n M : ℕ) : 0 < mKM n M := by
  unfold mKM
  apply Finset.prod_pos
  intro p hp
  have : 0 < p := (Finset.mem_filter.mp hp).2.pos
  exact zpow_pos (by exact_mod_cast this) _

end Zeta7
