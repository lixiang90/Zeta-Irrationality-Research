import Mathlib

/-!
# 论文数值常数（b=8）

`U`（(6.4) 类比）、`A*`（(5.19) 类比）、`A_M`（(5.20) 类比）、`A₂₀₀`（附录 B.3 类比）、
(5.20) 类比在 `M = 200` 处的恒等式与 margin（(7.2) 类比），均由 `norm_num` 核验。

**门控说明**：`U` 必须满足双侧门控：(i) 实侧能量证书 `λM₀ − I(ρ) + C* ≤ U`
（`Zeta7.EnergyConst8.energy_const8`，对当前 table7 测度的认证值为
`f = −2.15460…`，见 `research/gen_energy_const8.py`）；(ii) 算术侧 margin
`Aeff + U < 0`（Aeff = 1.98）。取 `U = −43/20 = −2.15`：f ≤ U 余量 0.0046，
Aeff + U = −0.17 < 0。注意：研究侧扫描（`b8_verdict.md` 附录）对 λ = 39/40 的
"实侧最优 f = −3.809" 是 SLSQP 优化测度的值；形式化锁定的 table7 嵌套 arcsine
测度只达到 f = −2.1546，故 U 不能取 −159/50。（若 Phase B 的 Aeff 重算后
> 2.15，需回头用 `measure8_v2` 重优化测度并重发射 Table7 证书。） -/

namespace Zeta7

/-- 常数 `U`（引理 6.1 类比 / (6.4) 类比）：实侧能量证书与算术 margin 的门控值。 -/
def U : ℚ := -43 / 20

/-- 常数 `A*`（(5.19) 类比，b=8 表数据积分）。 -/
def Astar : ℚ := 137743476530383649272771363 / 70835302954194210432000000

/-- `A_M`（(5.20) 类比，`λ = 37/40`，b=8 的 `P̄ = 11729/720`）。 -/
def A (M : ℚ) : ℚ := Astar + 7 * (37 / 40) / M - (11729 / 720 - 1 / 4) / M ^ 2 + 32 / M ^ 3

/-- `A₂₀₀`（附录 B.3 类比展示值，b=8）。 -/
def A200 : ℚ := 140008647356341045663172731 / 70835302954194210432000000

lemma A_200_eq : A 200 = A200 := by
  unfold A Astar A200; norm_num

/-- 有理 margin（(7.2) 类比）：`−1600 (A₂₀₀ + U) > 139 / 5`。 -/
lemma margin : (139 : ℚ) / 5 < -1600 * (A200 + U) := by
  unfold A200 U; norm_num

/-- 本库证明的归一化常数（`Zeta7.Growth`）：`limsup K⁻² log m_K ≤ A_eff`。
弱于展示值 `A₂₀₀`，但仍满足 `A_eff + U < 0`（margin ≈ −1.2）。 -/
def Aeff : ℚ := 198 / 100

/-- 无理性判据用的 margin：`A_eff + U < 0`。 -/
lemma Aeff_margin : Aeff + U < 0 := by
  unfold Aeff U; norm_num

/-- `K = 40 n` 的实数形。 -/
noncomputable abbrev Kr (n : ℕ) : ℝ := 40 * (n : ℝ)

end Zeta7
