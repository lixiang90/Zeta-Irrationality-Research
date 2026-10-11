import Mathlib

/-!
# ζ(7) 的 b=8 构造（Fauzan 方法在导数阶 8 的推广）

本文件镜像 `Apery/Construction.lean`（mo271 对 Fauzan ζ(5) 论文的形式化，
Apache-2.0），按 `research/` 中已验证的 b=8 推导做如下替换（论文 b=6 → b=8）：

| 对象 | b=6（Apery） | b=8（本文件） |
|---|---|---|
| 权 | `(2π)⁴ y⁵ f⁗ / 12` | `(2π)⁶ y⁷ f⁽⁶⁾ / 360` |
| 多项式矩 (2.2) | `(−1)^e B_{2e+2}(2e+3)(2e+4)(2e+5)/24` | `(−1)^e B_{2e+2}(2e+3)…(2e+7)/720` |
| 极点值 (2.3) | `j⁴(X−H_j⁽⁵⁾) − 1/4 + 1/(2j)` | `j⁶(X−H_j⁽⁷⁾) − 1/6 + 1/(2j)` |
| Hankel 分子 | `D_N(t)⁶ t^{i+j}` | `D_N(t)⁸ t^{i+j}` |
| S_K (2.5) | `(N!)^{12h}` | `(N!)^{16h}` |

数学验证（60 位精度或有理精确）见 `research/zeta7_pole_values.py`、
`research/b8_machinery.py`；可行性判定见 `research/b8_verdict.md`。
约定：mathlib 的 `bernoulli` 用 `B₁ = −1/2`；μ-矩公式只含偶数指标，约定无关
（`research/NOTES.md` §2 的约定陷阱在此被构造性定义绕开）。
-/

namespace Zeta7

open Finset Polynomial BigOperators

open scoped Polynomial

/-- `D_m(t) = ∏_{j=1}^m (t + j²)`，与 `Apery.D` 相同。 -/
noncomputable def D (m : ℕ) : ℚ[X] := ∏ j ∈ Icc 1 m, (X + C ((j : ℚ) ^ 2))

/-- b=8 多项式矩（式 (2.2)-类比）：
`μ₇(t^e) = (−1)^e B_{2e+2} (2e+3)(2e+4)(2e+5)(2e+6)(2e+7) / 720`。
（`research/zeta7_pole_values.py` 60 位验证；矩的精确有理性是"对一切导数阶成立"
的核心奇迹——ζ(2e+2) 经 Euler 公式消去 π。） -/
def μmono (e : ℕ) : ℚ :=
  (-1) ^ e * _root_.bernoulli (2 * e + 2) *
    ((2 * e + 3) * (2 * e + 4) * (2 * e + 5) * (2 * e + 6) * (2 * e + 7)) / 720

/-- `μ₇` 在 `t` 的多项式上按单项式线性延拓。 -/
noncomputable def μpoly (P : ℚ[X]) : ℚ := P.sum fun e c => c * μmono e

/-- 广义调和数 `H_j^{(7)} = ∑_{v=1}^j v⁻⁷`。 -/
def H7 (j : ℕ) : ℚ := ∑ v ∈ Icc 1 j, 1 / (v : ℚ) ^ 7

/-- b=8 极点值（式 (2.3)-类比，精确闭式）：
`μ_{7,X}(1/(t + j²)) = j⁶ (X − H_j^{(7)}) − 1/6 + 1/(2j)`。
推导：六次分部积分（边界干净，u = y⁷/(y²+a²) 在 0 有 7 阶零点）+
DLMF 25.11.29（Hermite 公式）取 s = 7：
`2∫₀^∞ f(y) Im(a−iy)⁻⁷ dy = ζ(7,a) − a⁻⁷/2 − a⁻⁶/6`。
（`research/zeta7_pole_values.py`：60 位验证通过；早前报告的"残差 r(a)"系
Eulerian 分母 bug，已修正。） -/
noncomputable def poleValue (j : ℕ) : ℚ[X] :=
  C ((j : ℚ) ^ 6) * (X - C (H7 j)) - C (1 / 6) + C (1 / (2 * (j : ℚ)))

/-- `μ_{7,X}(P(t) / D_K(t))`：D_K 首一、根 −j² 互异，部分分式
`P/D_K = (P /ₘ D_K) + ∑_j (P(−j²)/D_K'(−j²)) · (t + j²)⁻¹`，逐项代入。
与 `Apery.μX` 同构的构造（无需选择公理）。 -/
noncomputable def μX (K : ℕ) (P : ℚ[X]) : ℚ[X] :=
  C (μpoly (P /ₘ D K)) +
    ∑ j ∈ Icc 1 K,
      C (P.eval (-(j : ℚ) ^ 2) / (derivative (D K)).eval (-(j : ℚ) ^ 2)) * poleValue j

/-- b=8 Hankel 矩阵 `G_K(X)`（式 (2.4)-类比），K = 40n, N = n, h = 39n
（(K:N:h) = 40:1:39 重调谐：α = 1/40 使实侧界可行，`research/b8_verdict.md`；
构造约束 h = K − N 满足 39n = 40n − n）。 -/
noncomputable def G (n : ℕ) : Matrix (Fin (39 * n)) (Fin (39 * n)) ℚ[X] :=
  fun i j => μX (40 * n) (D n ^ 8 * X ^ ((i : ℕ) + (j : ℕ)))

/-- `Δ_K(X) = det G_K(X)`。 -/
noncomputable def Δ (n : ℕ) : ℚ[X] := (G n).det

/-- b=8 标量 `S_K`（式 (2.5)-类比）：`(N!)^{16h}`（b=6 为 12h）。 -/
noncomputable def S (n : ℕ) : ℚ :=
  ((40 * n).factorial : ℚ) ^ (2 * (39 * n)) * 4 ^ (39 * n - 1) /
    ((n.factorial : ℚ) ^ (16 * (39 * n)) *
      ∏ i ∈ Icc 1 (39 * n - 1), ((2 * i).factorial : ℚ) ^ 2)

/-- `F_K = S_K Δ_K`。 -/
noncomputable def F (n : ℕ) : ℚ[X] := C (S n) * Δ n

end Zeta7
