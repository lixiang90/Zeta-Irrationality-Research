# 当前研究状态（自动生成）

> 权威账：`program.json`。由 `python scripts/research_state.py render` 生成；不要手改本文件。

修订 32 · 更新 2026-11-25 · goal `specified_zeta_l_irrationality` · 研究账状态 `active`

最终目标：取得至少一项明确指定ζ/L特殊值的新无理性或有理线性无关结论，付清同对象完整证明与独立复核。
数值目标已实现：否。诊断资产与组织维护不能替代此项。

## 当前窗口

- 任务：`round291_specified_zeta7_review`；轮次 291；状态 `completed`；主路线 `pure_shifted_mellin`。
- 入口：[research/zeta7_opportunities_round291.md](../research/zeta7_opportunities_round291.md)。
- 本阶段交付：完成指定 ζ(7) 的全路线比较；给出最优有理根与显式平方各自的实际误差和分母判据，推导全带的八层精确算术。
- 首问题：能否控制 2n<p<4n 中 T_(n,p) 三阶整除的加权占比，或沿无界子列使完整显式分母的线性指数低于 C*？
- 通过：已给每阶纯线性正误差、有理根大起点等参数排除、显式平方的准确实率、全带完整局部深度及跨奇权最高层判据。
- 停止：本轮按任务书正式复盘。两种逼近均缺成功无界子列。单独延长有限扫描或优化实处常数不足以支付尚缺的算术成本。
- 持久窗口 `zeta7_fixed_n_shift_291`：已完成 1/1 轮；整理和task改名不计新窗口。

## 宏观复盘

- 完成研究轮 291；最近正式复盘 291；其后 0 轮。
- 连续未改善可行性 3 轮；现在须复盘：否。
- 正式复盘已处理至第291轮；计数不清零，其后有新完成轮且连续未改善达到2即提前复盘。
- 默认复盘 295；最迟 299；两轮核心停滞提前。

## 下一动作

1. 对 n=3d、2n<p<4n 的 P14，研究 p³|T_(n,p) 的逐阶 log p 加权占比。若全序列上极限≤1−C*/12（7.5613641…%），即可排除显式平方的严格指数。也可用 P12 的权无关标量统一控制最高层。
2. 正向需证明同一显式分母的下极限指数小于 11.09263630…（精确值 C*），包括全部较小素数。最优根需另查 q_out，等斜率的22个块仍以 d* 的 log1024 判据单算。
3. 备选相邻 Mellin 行须在同一无界子列证明 ζ(7) 系数和实际余项非零，再付本原费用。一般正平方格可凭全模数高度受控的短解重开。

## 全路线状态

| 路线 | 状态 | 当前完整证明缺口 |
| --- | --- | --- |
| ζ(5)形式化基线 | `completed_baseline` | 不是本项目新数值目标；镜像占位与绝对版分开。 |
| ζ(7)Gram与整数格 | `parked` | 同一整数输出的无界非零及负本原二次指数未闭合。 |
| 3ζ(3)+ζ(5)与K5 | `parked` | 完整内容改进与实能量未给严格净余量。 |
| 对数矩与Padé | `parked` | 真实约分根/本原费用尚未跨解析门槛。 |
| 已知周期分类推论 | `completed_known_corollaries` | 没有隔离新的指定值；不计作新宏观成功。 |
| 奇权、CM与χ−7Fricke | `parked` | 强制恢复背景、全叶奇点与所审费用/能量障碍。 |
| χ−8 RV与原生增长行列式 | `parked` | 实际无界非零与严格净指数仍缺；安全上界失败非全方法否定。 |
| 混合rank3标准/标量AP入口 | `closed_implementation` | 自然cap32/27及仅辅助分布cap≥8/9均不足；c≠0极点出口关闭。 |
| 实际联合评价格/Frobenius首证书 | `closed_implementation` | 264证明单变量completejet index-only入口失败；balanced leading-box可证但高度保证仍不足。两轮窗口结束，intrinsic费用及全部tensor未被否定。 |
| 未准入来源的定期宏观比较 | `unadmitted_candidates` | 291按已跟踪文库和21条路线，比较固定阶数移位、一般整数平方格、等斜率全维行列式、相邻 Mellin 投影和已有纠错。需对同一纯目标有理数得到无界非零及严格的完整分母收益。 |
| M₀,₈固定3:1完整向量（仅来源核查） | `closed_implementation` | 266在原canonical graded识别下付直接Barnes完整安全界，未付actual primitive净信用；全群小素数/高次幂补齐仅o(n)，一轮源核查结束。下降常数桥和作者实际率仍未独证。 |
| 非显式Siegel固定目标商（仅来源核查） | `closed_implementation` | 268构造同原χ/统一余项坏族，普遍目标保证失败；实际全行15.6信用投入完整cofactor upper仍不足，q≥180。一轮到期结束；存在好族及两个低费输出仍未付。 |
| 增长极点的纯目标正Gram（仅预算核查） | `closed_implementation` | 276新增完整内容率2及真实实处upper改善9log2−1，净upper=46+46log2+32h>0；裸非负lower/R全m PSD/负净率未付。一轮到期关闭，安全增长不等于最优no-go。 |
| 固定Y的Abel正配对（仅预算核查） | `closed_implementation` | 274完整新内容信用30log2使净upper再改善，但仍为86+18log2+12log6>0；裸Q全序列lower仅−16−10log2，未裁全部负子列。一轮重开到期结束，最优负预算未付。 |
| 单正测度Markov的实际标量边界 | `parked` | 完整实际c_s总费用未控；277自然Möbius在完整反证下第二moment仍无理，增长端点按实际总degree无新实率；未否定全部Markov机制。 |
| χ−8 WZ双镜像的同步截断 | `closed_implementation` | 来源恒等式仍为一手输入；纯尾非零/裸率已付，逐项族全N增长且actual prefix全N/有界间隔负率被排，稀疏子列内容未付。 |
| χ−8四分点连续双Hahn平方余项（仅完整费用核查） | `closed_implementation` | 278完整线性奇整数对已付，实际d=M/g；安全净率8+12log2>0，足额全g率未付。一轮到期，非最优费用全子列no-go。 |
| 单值复Beta非对角固定9jet（仅最小来源核查） | `closed_implementation` | 280独证实际K=B vvᵀ，固定9jet m≥8秩恰8/惯性(4,4,m−8)，m≥9det恒0，目标rank1；非零接口失败，一轮关闭。 |
| χ−8 双余类 Markov 逼近的完整分母 | `closed_implementation` | 实际c_s恒奇。扣除全部二处及已证奇素数内容后，完整剩余分母的对数二次率仍为11log2，目标尺度的线性上界未付。 |
| 全奇权对角Padé正平方的实际分母 | `parked` | 权七至X的可能例外至多O((log X)²)。旧指定射线已排除，真实判别式的奇导子按幂增长。仅以奇素数带控制所有剩余阶数仍缺原Z_d的带内公因数。 |
| 四阶极点导数的纯权七矩及其既约分母 | `parked` | 显式平方的实际实率为 −C*，完整分母乘误差上界率 24.0352…>0。最高带平均约分深度能否在无界子列超过 8−C*/2 未定；最优根另有 p>4n 的行列式因子。旧等斜率的22个公共块公因数仍无上极限估计。 |

## 恢复所需证据

- [research/zeta7_opportunities_round291.md](../research/zeta7_opportunities_round291.md)
- [research/zeta7_shift_window_round291.md](../research/zeta7_shift_window_round291.md)
- [research/zeta7_shift_christoffel_round291.md](../research/zeta7_shift_christoffel_round291.md)
- [research/zeta7_shift_primitive_round291.md](../research/zeta7_shift_primitive_round291.md)
- [research/zeta7_route_audit_round291.md](../research/zeta7_route_audit_round291.md)
- [长期goal](../docs/RESEARCH_GOAL.md) · [恢复协议](../AGENTS.md) · [通用组织方法](../docs/LONG_RESEARCH_WORKFLOW.md)

状态检查核引用、依赖、计数和摘要一致性；不认证数学，也不替goal工具改变运行状态。恢复时另核工具的暂停/限额状态。
