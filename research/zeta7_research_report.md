# ζ(7) 无理性研究项目——结题研究报告

> 2026-09-28 重启审计：本文为历史记录，其中“自由测度可行”“h=K−N 被强制”及
> 旧 Hankel 观测的结论需修正。新的精确障碍、脚本修复和实验见
> [restart_analysis.md](restart_analysis.md)。本项目仍未证明 ζ(7) 无理。

日期：2026-09-26。状态：**停止并交付部分成果**（用户裁决）。
本文档汇总整个 ζ(7) 无理性攻关的形式化成果、精确算术核算与遇到的障碍，作为结题交付。

---

## 1. 背景与动机

- 起点是论文 `ZETA5_IS_IRRATIONAL.pdf`（Fauzan 型路线）的审查与 Lean 形式化
  （工作目录 `E:\kimi-build\zeta5\`，项目 `Zeta7Formal/`）。
- ζ(5) 的无理性已由 Apéry 定理确立，且社区已完成可信的形式化
  （`github.com/mo271/Zeta5`，镜像于 `Zeta7Formal/Apery/`）。本项目尝试将同一路线
  提升一档（b=6 → b=8）以攻击 ζ(7) 的无理性。
- 已知文献界：Zudilin 证明了 {ζ(5),ζ(7),ζ(9),ζ(11)} 中至少一个无理；
  单个奇数 ζ(7) 的无理性是公开问题。本路线若闭合将是该问题的一个完整初等证明。

## 2. 方法概述（b=8 Fauzan 路线）

与 mo271/Zeta5 的 b=6 结构完全同构，镜像其在 `Zeta7Formal/Zeta7/` 下的整个
Lean 库（Construction / Degree / Positivity / DetIntegral / Hermite 核 /
Moments / ZeroMass / Potential / Table 证书 / Energy 链 / Stirling / RealBound /
Main）。核心逻辑：

1. 构造行列式序列 Δₙ（b=8 的 Hermite 型核），证其为非零有理数且其绝对值
   受几何衰减控制（`log_Δ_le` 类比论文 (6.14)）；
2. 算术侧：精确估值机器给出 Δₙ 分母/分子的增长常数 **A_eff**；
3. 实侧：比较测度 ρ 的能量不等式给出 **U < 0** 型的位势下界；
4. 无理性判据：需存在 U 使 **f(ρ) ≤ U 且 U < −A_eff**（即 A_eff + U < 0），
   则由 Δₙ → 0 的整数序列矛盾推出 ζ(7) 无理（`Main.lean:184 zeta7_irrational`）。

调谐参数 (K:N:h) 决定场 V（α = N/K，λ = 1−α = h/K），全链常数随之缩放。

## 3. 已完成的成果（全部经 Lean 编译验证）

### 3.1 实侧能量链全链闭合，零 sorry

调谐 **(K:N:h) = (40:1:39)**（α = 1/40，λ = 39/40）下，以下模块编译通过：

- 21 个基础模块：Construction、Degree、Positivity、DetIntegral、EnergyRaw8、
  EnergyAtoms8、EnergyBlocks8、Field8、Gaussian、Hermite*、Kernel、Moments、
  ZeroMass、Potential8、PotentialIneq8、Phi8、Table7（位势证书表）；
- `EnergyFinal8` / `EnergyBound8`（`log_Δ_le'8`，系数 28·39n·log K + 66·39n）；
- `Measure7`、`Stirling.log_S_le8`（6·39n·log K + 3·39n）；
- `EnergyConst8.energy_const8`（U = −43/20 的精确有理证书，f_cert = −2.1546046860）；
- **`Zeta7.RealBound.real_bound`**（原目标中"最后一个 sorry"，已填完整证明，
  低阶项 1326·n·log K + 2691·n 用 `Real.tendsto_pow_log_div_mul_add_atTop` 吸收）；
- `Legendre.vS_eq/S_eq_div` 与 `Arith.BasisChange` 已重标定至 39n。

`grep ":= sorry" Zeta7Formal/Zeta7/` **零命中**（2026-09-26 复核）。
实侧 30+ 文件、从 Andreief 表示到 real_bound 的整条不等式链在 Lean 层面完备。

### 3.2 证书生成管道（可复用）

- `Zeta7Formal/scripts/growth/`：`table_b8_39.py`、`gen_pieces_b8_39.py`、
  `outer_gen_b8_39.py`、`tail_b8_39.py`、`aeff_scan.py`（源自 mo271 并做了 b=8 适配）；
- `research/`：`gen_energy_const8.py`、`gen_measure8{,_v3,_sweep}.py`、
  `gen_phi8_cert.py`、`gen_table7.py`、`b8_tablegen_39.py`、`verify_measure8.py` 等。

## 4. 遇到的障碍：数学门控死局

### 4.1 U 的存在性门控

无理性判据要求实侧系数 f（由测度 ρ 决定）与算术常数 A_eff 满足
f ≤ U < −A_eff。调谐 (40:1:39) 下精确核算（两条独立管道逐位一致）：

| 量 | 值 | 来源 |
|---|---|---|
| A_eff | **3.424178395**（= 5715056524986876059171/1669030017063552000000） | 算术链精确分数（内区 1.251953 + 外区 2.209174 + 尾段 −0.056448 + 小素数 0.019500） |
| 实侧 f（锁定 table7 嵌套 arcsine 16 原子测度） | **−2.1546**（NM/L-BFGS-B 族内最优 −2.1784） | `gen_measure8*.py`，f_cert 经 `gen_energy_const8.py` 有理认证 |
| 所需 U | ≥ −2.1546 且 < −3.4242 | — |

**U 不存在，判据不可证。**

### 4.2 结构原因（为何无法补救）

- 外区 Ê_out 的 max 项系数被秩损失钉死：c ≥ (2h−(K−8N))/K = 46/40 = **23/20**。
- **即使内区贡献取 0**，outer + tail + small = 2.209174 − 0.056448 + 0.019500 =
  **2.172226 > 2.15**——任何内区表的改进都无法过门；外区界本身已超预算。
- 内区膨胀机理：α = 1/40 时 Ê_in ≈ xF(x) + 43/16，F 在 [3,20] 上均值 ≈ +2.34
  （旧调谐 −16λ{3x/40} 项的强负贡献消失），∫ 由 0.17 升至 1.25。

### 4.3 全调谐扫描：gap 是结构性的

对嵌套 arcsine 族（唯一有现成位势证书管道的测度族）做 A_eff(α) 扫描并与
f_nested(α) 合并（`research/aeff_scan.json`、`b8_phaseB_gate.md` 终局附录）：

| α | f_nested(α) | A_eff(α) | gap = f + A_eff |
|---|---|---|---|
| 0.075 | −1.633* | 1.963060 | +0.330 |
| 0.06 | −1.107442 | 2.311929 | +1.205 |
| 0.05 | −1.374712 | 2.583485 | +1.208 |
| 0.045 | −1.519276 | 2.728753 | +1.210 |
| 0.04 | −1.664923 | 2.881108 | +1.216 |
| 0.03 | −1.984075 | 3.220702 | +1.237 |
| 0.025 | −2.178400 | 3.424178 | +1.246 |

*0.075 处还是自由测度的值，嵌套族只会更弱。

两条曲线反向走势：A_eff 在 α ≈ 0.07 附近取最小 ≈ 1.9，恰是嵌套族 f 最弱
（≈ −1.6）的区域。**gap ≈ +1.2 在整个扫描区间几乎恒定——这是族选择层面的
结构性差距，不是调谐问题。** 扫描中出现的 f ≈ −2.6…−3.8 属于直方图 + SLSQP
**自由测度**（见 `NOTES.md`"直方图+SLSQP"），而该族没有位势证书的表示与
证明管道，无法进入形式化。

### 4.4 调谐历史（决策回链）

1. 论文原始 (40:3:37)（α = 0.075）：Aeff = 1.98 > |U| 上限 1.63，不可行；
2. 扫描后选 (40:1:39)（α = 0.025 → 实锁 1/40）：期望 U = −2.15 过门，实侧全链
   随之重标定并闭合；
3. Phase B 算术链重算：Aeff 从期望的 ≈ 1.94 膨胀至 3.424（外区系数与内区
   积分双膨胀），门控翻转；
4. 全 α 扫描确认无解 → 用户裁决停止。

## 5. 剩余缺口（如实登记）

- `lake build Zeta7` 仍失败于 `Zeta7/Arith/ClassFrame.lean:140` 与
  `SmallPrimeF.lean:196/216` 等约 20 个算术链文件——它们滞留旧的 37n 标定。
  **按 §4 的判定，修复它们也无法闭合证明（U 门控不过），故未投入。**
- `#print axioms Zeta7.zeta7_irrational` 尚不可执行到终态（依赖未闭合的算术链）；
  已证成分的 axiom 审计需算术链接入后才有意义。
- 完成判据三检验（`lake build Zeta7` 零错误 / grep sorry 零命中 / axioms 恰为
  [propext, Classical.choice, Quot.sound]）中仅第二项达成。

## 6. 可能的后续出路（未执行，按风险排序）

1. **自由测度（直方图/SLSQP）的证书化**（α = 0.03 处余量 ≈ 0.32）：需要新的
   测度表示 + 位势论证书管道（类比 mo271 Table 1/2 的有理区间机制），数周级
   研究风险，是唯一在 b=8 框架内已见正余量的方向。
2. **(100:3:97) 大调谐重建**：K = 100n 结构性重建（扫描 f ≈ −3.541），算术链
   参数化管道已备，但 27+ 文件的 hdeg/秩项/表重生成工作量巨大且此前已被
   (40:1:39) 方案取代。
3. **降低 b 或改方法**：b=8 的能量/Vandermonde 代价随 b 增长很快，回退方向
   等价于放弃 ζ(7)。

若重启路线 1：从 `research/b8_phaseB_gate.md` §3 的 22 文件改法路线图、
`agent-11`（持有全部管道上下文）与 `measure8_v2/v3` 测度数据续起。

## 7. 交付物索引

| 类别 | 位置 |
|---|---|
| Lean 形式化（实侧全链，零 sorry） | `Zeta7Formal/Zeta7/`（Main.lean:184 `zeta7_irrational`） |
| Apery ζ(5) 镜像库（未改动） | `Zeta7Formal/Apery/` |
| 门控核定与终局扫描 | `research/b8_phaseB_gate.md`、`research/b8_verdict.md`（附录 2/3） |
| 算术推导 | `research/b8_arithmetic.md`、`research/NOTES.md` |
| 测度/证书数据 | `research/measure8_*.txt`、`table7_*.txt`、`aeff_scan.json`、`partition7.json` |
| 复现脚本 | `research/*.py`、`Zeta7Formal/scripts/growth/*.py` |

## 8. 诚实声明

1. 实侧能量链的证明是完整、编译验证过的；但其中锁定的比较测度（table7）
   不是使无理性判据成立的最优测度——判据失败的根源在测度族的证书可达性，
   不在任何 Lean 论证。
2. A_eff 的全部数值为精确有理分数，经两条独立实现逐位交叉核验；f_nested 为
   数值优化值（L-BFGS-B + Nelder–Mead 多初值），f_cert 的锁定值经有理证书认证。
3. 本项目**未证明也未反驳** ζ(7) 的无理性；它证明的是：b=8 Fauzan 路线的
   嵌套 arcsine 可证书化版本，在 λ = 1−α 的全部扫描调谐上判据不可闭合。
