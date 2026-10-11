import Mathlib
import Zeta7.Constants

/-!
# b=8 比较测度（Appendix A 类比）与 §6 常数

镜像 `Apery.Measure`（mo271 的 b=6 文件，本工程原样保留）。结构对应：
`lam`/`alph`（重调谐后 α = 3/100、λ = 97/100——见 `research/b8_verdict.md` 附录的
必要性判定）、`Cstar8`（式 (6.3) 类比，`research/NOTES.md` §3 的
C_*₈ = −2λ + 16αλ(1−log α) + 3λ² − 2λ²·log(2λ)）、`M₀` 证书界、Table 1 类比
（16 个嵌套 arcsine 分量，×10¹² 有理数据，由 `research/gen_measure8.py` 生成，
当前为占位，优化输出见 `research/measure8_v2.txt`）、`Sρ`/`Irho`（(A.2) 类比）。

数据流：gen_measure8.py（研究侧，已验证数学）⇒ table7（本文件，占位待填）⇒
ArcsinePotential7（U^ρ 公式 (A.1) 类比，待建）⇒ Table2 分割证书（gen_table2.py
的 b=8 类比）⇒ 位势不等式 2U^ρ − V ≤ M₀（镜像 `Apery.PotentialIneq` 链）。
-/

open Finset

namespace Zeta7

/-- b=8 重调谐比例：α = N/K = 3/100（K = 100n, N = 3n, h = 97n）。
【门控】依赖 (K:N:h) 重调谐裁决（`research/b8_verdict.md` 附录：
α = 0.075 下 |U| ≤ 1.63 < Aeff 不可行；α = 3/100 实侧最优 −3.54）。 -/
noncomputable abbrev alph8 : ℝ := 1 / 40
/-- λ = h/K = 39/40（h = K − N 强制；最小重调谐 (K:N:h) = 40:1:39）。 -/
noncomputable abbrev lam8 : ℝ := 39 / 40

/-- b=8 常数 C*（式 (6.3) 类比，`research/NOTES.md` §3 公式，
系数 16α = 2·8α 对应 D_N⁸ 分子）。 -/
noncomputable def Cstar8 : ℝ :=
  -2 * lam8 + 16 * alph8 * lam8 * (1 - Real.log alph8) + 3 * lam8 ^ 2
    - 2 * lam8 ^ 2 * Real.log (2 * lam8)

/-- M₀ = −6.35：发射器逐 cell 认证 max_{t∈(0,2]}(2U^ρ₈−V₈) ≤ −6.35
（真峰 −6.3678 @ t≈0.0113 + 细分松弛 0.013；809 cell，`research/gen_table7.py`）。 -/
noncomputable abbrev M0_8 : ℝ := -6.35

/-- Table 1 类比：`10¹² a_j`、`10¹² b_j`、`10¹² c_j`（16 个嵌套 arcsine 分量）。
【占位】数据由 `research/gen_measure8.py`（v2，多初值 + 深光滑阶梯）生成；
填入前本文件的定义均可编译，但 Sρ_sixteen 等引理暂不可证。 -/
def table7 : List (ℕ × ℕ × ℕ) :=
  [(23805751, 7233498018, 88359644486),
   (23805236, 24475480029, 99121090942),
   (13780926, 53387677936, 107241598886),
   (4483874, 90545533724, 82115389762),
   (4483625, 131074600165, 77454394089),
   (3851833, 183808371265, 89612496606),
   (1564143, 242780558682, 78099713936),
   (1360324, 306011065675, 72197849402),
   (745743, 365490311924, 56650775746),
   (383988, 426183534933, 58654077061),
   (247221, 481648846822, 38926352971),
   (159595, 523624475376, 36581913253),
   (111989, 591522748269, 62952958579),
   (54900, 747509679905, 133255592),
   (50233, 778759015742, 16227595547),
   (36652, 1389338921242, 10670893142)]

/-- `a_j`、`b_j`、`c_j`（1-索引；表外为 0）。 -/
noncomputable def aρ8 (j : ℕ) : ℝ := ((table7.getD (j - 1) (0, 0, 0)).1 : ℝ) / 10 ^ 12
noncomputable def bρ8 (j : ℕ) : ℝ := ((table7.getD (j - 1) (0, 0, 0)).2.1 : ℝ) / 10 ^ 12
noncomputable def cρ8 (j : ℕ) : ℝ := ((table7.getD (j - 1) (0, 0, 0)).2.2 : ℝ) / 10 ^ 12

/-- 部分和 S_j = ∑_{i ≤ j} c_i（A.1 类比）。 -/
noncomputable def Sρ8 (j : ℕ) : ℝ := ∑ i ∈ Icc 1 j, cρ8 i

/-- 对数能量 I(ρ)，公式 (A.2) 类比。 -/
noncomputable def Irho8 : ℝ :=
  ∑ j ∈ Icc 1 16, (Sρ8 j ^ 2 - Sρ8 (j - 1) ^ 2) * Real.log ((bρ8 j - aρ8 j) / 4)

/-- ρ 的总质量为 λ（A.1 末段类比）。
【占位引理】table7 填入后 `simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]; norm_num`。 -/
lemma Sρ8_sixteen : Sρ8 16 = lam8 := by
  simp [Sρ8, cρ8, table7, Finset.sum_Icc_succ_top]
  norm_num

end Zeta7
