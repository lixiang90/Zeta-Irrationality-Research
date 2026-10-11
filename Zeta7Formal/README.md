# Zeta7Formal：ζ(7) 无理性的 Lean 形式化

> **2026-09-28 状态更正：尚未证明 ζ(7) 无理，当前完整工程的算术参数未统一。**
> 下文的“只剩一个 sorry”“方案已闭合”是旧阶段记录，不能代表当前状态。
> 最新审计、精确变分障碍、Hankel 实验修正及新方向见
> [research/restart_analysis.md](../research/restart_analysis.md)。旧自由测度乐观值与该下界矛盾。
> 后续的增强整除性、局部基证明及联合构造实验见
> [research/joint_divisibility.md](../research/joint_divisibility.md)。已有实质改进，尚未闭合无理性证明。
> 继续研究的投影秩定理、局部证书及新增内区收益见
> [research/layer_analysis.md](../research/layer_analysis.md)。
> 最新的高层矩整除定理、模 p⁶ 引擎、零点分布与扩维实验见
> [research/distribution_analysis.md](../research/distribution_analysis.md)。这些新引理已有书面证明与精确核验，尚未 Lean 形式化，也未给出新的整体渐近收益。
> 完整矩阵耦合消元、886 组有限参数证书及局部退化机制见
> [research/coupled_analysis.md](../research/coupled_analysis.md)。Smith 等式猜想已被反例否定；较弱的行列式下界仍待统一证明，未更新全局算术常数。
> 对外部文章《ζ(7) is irrational》（Zenodo 22920911）的独立审阅见
> [research/zenodo_22920911/review.md](../research/zenodo_22920911/review.md)：发现决定性外区表格错误，同时提炼了可保留的相对范数估计与衰减一致性条件。
> 结合上述方法的新进展见 [research/stability_parameter_analysis.md](../research/stability_parameter_analysis.md)：改进相对范数上界，认证 11 组固定整数参数下的双变量整除性，并给出参数最高次系数的统一降维恒等式；ζ(7) 无理性仍未证明。
> 上轮的显式核因子、第一层列整除证明和第三层留数配对模型见 [research/boundary_kernel_analysis.md](../research/boundary_kernel_analysis.md)。其中保留了模 p³ 提升核验及异常参数反例；后续统一归一化进展见下一项。
> 后续 [research/normalization_hensel_analysis.md](../research/normalization_hensel_analysis.md) 已补上统一归一化证明，得到六极点窗口第一层下界及 α=1/8 下的局部积分改善 11/1152，并构造两次显式提升的有限证书。真实深层障碍的统一识别仍待证明；ζ(7) 无理性尚未完成。
> 最新 [research/two_sided_analysis.md](../research/two_sided_analysis.md) 通过显式双侧核配对，将统一局部下界提高到 45N−23p+21+a；α=1/8 指定窗口相对旧界的累计改善为 1/96。证明允许特殊化发生额外退化，并解释了 p=53、83 的配对消失。第三层接口、完整全局比较及 Lean 形式化仍未完成。
> **2026-09-29 新进展：** [research/third_layer_analysis.md](../research/third_layer_analysis.md) 用 Hermite 局部分解和第二次配对公式补出第三层书面证明，得到 48N−24p+22+a−b 的完整窗口界；α=1/8 指定窗口累计改善为 127/11520。附局部修正及模 p³ 证书；完整全局比较、独立审阅与新引理的 Lean 形式化尚未完成，ζ(7) 无理性仍未证明。
> **2026-09-29 后续全局比较：** [research/global_envelope_analysis.md](../research/global_envelope_analysis.md) 已将上述窗口界接入同一 α 下的完整算术包络，得到一般参数的增益闭式，并认证 18 组同参数实侧障碍。α=1/40、1/8 的缺口分别仍大于 0.588539、0.771278；由最高次系数的收益上限，α=1/8 即使理想化解决整个六极点窗口，仍有超过 0.505392 的缺口。下一步需研究其他素数区间或改变联合构造；新引理尚未 Lean 形式化，ζ(7) 无理性仍未证明。
> **2026-09-29 剩余内区与联合子空间：** [research/inner_subspace_analysis.md](../research/inner_subspace_analysis.md) 给出八/九极点窗口的下界猜想 `59N−7K+23`，完成 95 组完整多项式局部证书（含 K=400）及固定权重的两层核检查；统一证明尚缺，未扣入全局常数。另证明混合次数/部分零点子空间的正性，完成 184 项计算，所测新子空间均未优于对应对照。ζ(7) 无理性仍未证明。
> **2026-09-29 相邻内区与配对模型：** [research/inner_window_extension_analysis.md](../research/inner_window_extension_analysis.md) 证明一般移位零点抵消引理，建立固定九节点有理模型及“取值 + Laurent 留数”配对候选；22 组完整配对和显式二阶核证书通过，保留 4 组消元退化。扩大窗口后需扣除次数越界损失，79 组下半带完整多项式证书中 78 组等号。α=1/40 的整个下半带条件收益约 0.002618；一般行列式局部化尚未证明，未更新全局常数，ζ(7) 无理性仍未证明。
> **2026-09-29 非有理权与非显式构造：** [research/filtered_determinant_existence_analysis.md](../research/filtered_determinant_existence_analysis.md) 构造保持正性、有理矩和单一 ζ(7) 极点值的双曲函数／频率筛选测度族，并证明保留第一频率的固定周期筛选不能改变实侧 K² 主项。38 项完整 content 比较中的 30 项非退化调整均未优于基线；λ=1/64 是本原多项式恒为 1 的退化点。另得到三个固定有理局部块模型和 113 个逐项证书，提出有高度预算的非显式存在性路线；统一局部化及无理性证明仍未完成。
> **2026-09-29 算术子空间存在性：** [research/arithmetic_subspace_existence_analysis.md](../research/arithmetic_subspace_existence_analysis.md) 给出保持本原性的仿射超平面存在性判据、精确最大统一除数及通用体积法的限制。提取伴随矩阵 content 后，K=24 的模 3、7、17 条件各降为一个线性方程，联合使统一除数增加 357 倍，存在性指标从 0.875486 降至 0.865340，仍高于原构造的 0.747564。54 个参数族和 138 条多项式记录经过独立核验，保留 33 条饱和后条件失效的候选；未更新全局常数，ζ(7) 无理性仍未证明。
> **2026-09-30 高阶约束与实际子空间改善：** [research/padic_isotropic_subspace_analysis.md](../research/padic_isotropic_subspace_analysis.md) 用共同全各向同性空间降低部分提升成本，并给出 p=17 第三层不存在非零共同二次零点的精确证书。联合高阶条件选出法向量 `(1,4,1,0,…)`，对应在 t=−4 增加零点；导出的 `D_N⁶D_{2N}²` 构造在 K=24、48、72、96 的同维数及同次数对照中均改善，K=24 指标从 0.747564 降到 0.714384。整族存在性上界改善至 0.851366，仍为正；统一渐近算术预算尚待证明，未更改 Lean 定理或全局常数，ζ(7) 无理性仍未证明。
> **2026-09-30 双前缀全系数下界与维数优化：** [research/two_prefix_divisibility_analysis.md](../research/two_prefix_divisibility_analysis.md) 给出 `D_N⁶D_M²` 在指定外区素数上的统一全系数赋值下界，并保留沿用旧矩修正秩会失效的反例。取 `h=K−M` 可保持原最高矩次数且去掉 Schur 尾块；M≈3N–4N 的有限候选进一步改善，K=96 指标降至 0.818017，同维数同次数原权重对照为 0.897270。72 条记录、1048 项素数检查、24 组局部换基及四个完整多项式的独立认证通过；内区与实侧渐近预算仍未完成，未更新全局常数或 Lean 定理，ζ(7) 无理性仍未证明。
> **2026-09-30 内区预算与受约束存在性：** [research/two_prefix_inner_budget_analysis.md](../research/two_prefix_inner_budget_analysis.md) 给出一般剩余类计数下的内区排序分配界，推广 CRT 界并补上双前缀小素数尾界。9 组完整同参数预算中，α=1/24、M=4N 的比较测度方法缺口仍大于 0.661179；该值不是实际本原多项式的下界。2130 项全系数素数检查、24 组局部基及 2781 个积分片段通过。另检验保持剩余类计数的零点重排：两个非前缀候选总指标变差；在 K=96,N=4,M=16 固定 p=17,19,23,29,31 的计数后，精确分离证书证明前缀已是连续松弛中的唯一解。新书面结果尚未 Lean 形式化，既有 Lean 全局常数未改动，ζ(7) 无理性仍未证明。

> **2026-10-01 整值块与无限参数存在性：** [research/integer_block_existence_analysis.md](../research/integer_block_existence_analysis.md) 以连续二项式块补上任意零点重排的小素数缺口，完成 659 条块构造和 47 条整数线性组合记录，所测候选均未优于相应前缀。两宏观平移块的负整数线性组合所产生的正实零点满足 t∼常数·K³，在 K² 尺度仍有右移块的主外场。另用有限差分精确求出无限参数族的最大统一除数；K=24 下 u∈3103900800Z 可恢复前缀统一 content，但所有非零参数的实侧均更大，故仅凭该统一除数不能改善，特殊参数的额外 content 未被排除。10520 项素数检查、145 次独立整数行列式验证及 2296 个积分片段通过。新结果尚未 Lean 形式化，既有全局常数未改动，ζ(7) 无理性仍未证明。

> **2026-10-01 完整整值空间与分数节点：** [research/growing_space_nodes_analysis.md](../research/growing_space_nodes_analysis.md) 给出平方整值多项式的完整整数基，使自由维数 L 随 K 增长；在 L=3、6、12 下认证实侧整数点存在性，并严格隔离出相应数量的正实根。实侧改善仍被 content 损失抵消，729 点坐标盒、同余格及保留部分零点的候选尚未优于前缀。52 条节点记录显示半整数方案的主要算术损失不局限于 p=2；新外区下界 `4p−8K+3` 在 68 项有限检查中取等号，一般等号未证明。另证明纯互补分数节点在平方权重下的额外常数系数型正半定，无法通过非平凡子空间消去。书面结果和有限证书尚未 Lean 形式化，既有全局常数未改动，ζ(7) 无理性仍未证明。

> **2026-10-01 方向同余格与重叠零点：** [research/directional_lattice_overlap_analysis.md](../research/directional_lattice_overlap_analysis.md) 用两次完整 12,341 点 Newton 单纯形求出无限三维格的最大统一除数，认证 79 个方向格的迹方法障碍，并给出取值约束遗漏重根信息的精确反例。特殊点 `Q=(t+4)²(t+9)` 导出重叠前缀族 `D_N⁴D_A²D_B²`；在同次数同维数下，K=24、48、72、96 的最佳指标分别降至 0.649465、0.756949、0.780951、0.779561。一般重数分配界与小素数接口已有书面推导，497 项局部界、597 项小素数界、8000 项 CRT 元素检查及 62 次独立整数行列式核验通过。完整渐近比较与新引理 Lean 形式化仍未完成，既有全局常数未改动，ζ(7) 无理性仍未证明。

> **2026-10-01 重叠前缀的截断外区与完整预算：** [research/overlap_truncated_budget_analysis.md](../research/overlap_truncated_budget_analysis.md) 用带权混合子式补上 h 小于存活极点数的 CRT 下界，并证明最小权重投影子式可取 p 单位。606 项素数检查、30,906 项 CRT 系数检查和 49 个投影子式核验通过；11 组完整渐近预算及 4335 个包络片段经过独立验证。α=1/24、A/N=9/4 的当前算术预算与比较测度方法缺口仍大于 0.627359411723；它不是实际本原行列式的下界。K=192 的有限常数项证书确定 60 个素数的真实 content，已查区间剩余收益至多 0.00418260，但未作渐近外推。新结果尚未 Lean 形式化，既有全局常数未改动，ζ(7) 无理性仍未证明。

在 [mo271/Zeta5](https://github.com/mo271/Zeta5)（Apache-2.0，Lean `v4.33.1` +
mathlib `v4.33.1` + PrimeNumberTheoremAnd）之上构建的 ζ(7) 形式化工程。
`Apery/` 为 mo271 的 b=6（ζ(5)）完整形式化，**原样保留**（ζ(5) 定理
`Apery.irrational_five` 已机器验证）；`Zeta7/` 为 b=8（ζ(7)）层，承载
`../research/` 中已完成的数学研究的形式化。

## 状态

- `Apery.irrational_five`（ζ(5)）：✅ 无 sorry（mo271）。
- `Zeta7.Construction`：✅ 完整定义（b=8 的 μ 泛函、Hankel 矩阵、S_K、F_K；
  镜像 mo271 的构造性定义，无需选择公理）。
- `Zeta7.Main`：陈述层，全部已证（pole_value_exact / tau8_difference /
  kappa_valuation / harmonic7_valuation 的真证明均落地）。
- **【2026-09-25】全项目只剩一个 sorry：`Zeta7.RealBound.real_bound`**（实侧能量链，
  Prop 6.3 类比的 ε-形式接口）。`Zeta7.MainEstimate.main_estimate` 已完整组装
  （归一化 growth_mN/integral_mN + 实侧界 + Aeff_margin，c = 800·(−(Aeff+U)) > 0），
  `zeta7_irrational` / `irrational_seven` 的公理依赖仅剩 sorryAx。
  能量链剩余分解见 `Zeta7/RealBound.lean` 文件头（比较测度 ρ 镜像 `Apery.Measure`、
  energy_ineq 镜像 `Apery.EnergyFinal`、(6.14) 镜像 `Apery.EnergyBound`、
  (6.15) 系数按 `research/NOTES.md` §3 重算）。

## 数学基础（../research/）

| 成果 | 证据文件 | 形式化落点 |
|---|---|---|
| 极点值精确闭式 j⁶(X−H⁽⁷⁾)−1/6+1/(2j) | `zeta7_pole_values.py`（60 位） | `Construction.poleValue`（定义即闭式）；`Main.pole_value_exact` |
| τ₈ 差分/分布恒等式、von Staudt、调和界 | `b8_machinery.py`（全过） | `Main.tau8_difference`、`kappa_valuation`、`harmonic7_valuation` |
| (2.9)/(3.12)-类比、外区/中区赋值观测 | `b8_hankel*.py`、`b8_hankel_all.txt` | Degree/Normalization 层（待建） |
| I_out,8 = 1.536、∫R₈ = 0.193、A_*₈+Ū₈ < 0 | `b8_final.py`、`fit_outer.py`、`fit_inner.py` | Constants/RealBound 层（待建） |
| **可行性判定（best 轨道可行，γ 轨道需再工程）** | `b8_verdict.md` | 本工程的总路线图 |

关键事实：b=8 的**数据层无障碍**（极点值全有理、矩精确、赋值界成立）；
`b8_verdict.md` 的双轨判定表明方案在算术上闭合，剩余为 mo271 式的
估值机器再工程（b=6 已有先例与代码可镜像）。

## 路线图（研究与形式化并行）

1. **Degree/Positivity（b=8）**：镜像 `Apery/Degree.lean`、`Apery/Positivity.lean`。
   Positivity 需要权 `(2π)⁶y⁷f⁽⁶⁾/360` 的正矩表示 + Hermite 公式（DLMF 25.11.29）
   的 s=7 情形（`research/zeta7_pole_values.py` 已给出完整推导链）。
2. **估值机器（γ-再工程）**：`b8_hankel.py` 的观测值给出 best 轨道；
   需按 mo271 `Arith/` 目录的 b=6 做法重做 b=8 版 class-wise 估值证书
   （对应 `research/b8_arithmetic.md` §A–E 的推导）。
3. **常数层**：α 重调谐（判定表明 α ∈ [0.03, 0.05] 优于论文的 3/40；
   `research/scan_output*.txt`）、I_out/∫R 证书化（Table 式有理区间）。
4. **MainEstimate → 完成**：组装出 `main_estimate`，`zeta7_irrational` 立即成立
   （判据链已闭合）。

## 构建

```bash
lake exe cache get   # mathlib v4.33.1 缓存（首次）
lake build           # Apery + Zeta7
```

## 署名与许可

- `Apery/`、构建配置：`Apery` 项目 © Moritz Firsching 等（mo271/Zeta5），Apache-2.0。
- `Zeta7/`、`research/`（上级目录）：本研究工程，Apache-2.0（与上游一致）。
- 数学方法：Fauzan《ZETA5 IS IRRATIONAL》（2026 预印本）的 b=8 推广，
  推导与验证记录见 `../research/`。
