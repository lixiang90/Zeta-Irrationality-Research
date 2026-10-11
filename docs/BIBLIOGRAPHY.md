# 文献库阅读导航

[literature/](../literature/) 保留论文原件、作者稿、网页快照、固定版本清单和阅读范围记录。它是研究证据库；收录一份声称证明的文章，不表示项目认可该证明。原文件名和原字节保留，身份与用途以对应 manifest、阅读地图及后续审计为准。

## 建议阅读次序

| 目的 | 入口 | 阅读要点 |
| --- | --- | --- |
| 建立奇数 ζ、L、周期研究背景 | [总体阅读地图](../literature/reading_map_20261004.md)、[全局清单](../literature/manifest_global_20261004.json) | 区分单值无理、窗口至少一个无理、无理值个数与有理线性空间维数 |
| 理解 ζ(5) 形式化基线 | [Fauzan 论文](../literature/fauzan_zeta5.pdf)、[mo271 说明](../Zeta5-mo271/README.md) | 论文与 Lean 的构造差异、完整整数化及正的小值判据 |
| 追溯 Padé、端点与对数矩路线 | [显式端点地图](../literature/explicit_relative_reading_map_20261004.md)、[对数矩地图](../literature/log_moment_reading_map_20261005.md) | 真实余项、非零性、振荡渐近与分母成本的适用条件 |
| 检查局部算术与本原分母 | [本原路线地图](../literature/primitive_routes_reading_map_20261005.md) | Greene、Lucas、Dwork 输入与项目实际对象是否匹配 |
| 理解 CDT 的既有定理及本项目推论 | [周期与 holonomy 地图](../literature/period_holonomy_reading_map_20261005.md)、[奇数权地图](../literature/cdt_odd_reading_map_20261005.md) | 真实周期投影、关系触发、共同解析域与整模型 |
| 了解研究停止判断的最终依据 | [第260轮清单](../literature/manifest_global_review_round260_20261010.json)、[第261轮清单](../literature/manifest_refined_budget_round261_20261010.json) | 阅读范围和所用精确版本；不要把局部入口排除扩张为整个方法不可能 |
| 核查第262轮的精确解析界与指定目标 | [新增原件与读取范围](../literature/next_route_round262_20261012/README.md)、[数值目标检索](../research/next_route_novelty_20261012.md) | 双穿孔度量的曲率规范；有界检索未发现适用定理不等于已确认开放 |

K₂、覆盖与新周期方向另见 [K₂地图](../literature/k2_gap_reading_map_20261004.md)、[新路线地图](../literature/next_route_reading_map_20261004.md)及[桥梁地图](../literature/bridge_reading_map_20261004.md)。每张地图都说明文献能提供什么，以及仍需本项目自行证明什么。

## 必须随文献一起保留的更正

- **Ghosh–Ward**：库中旧 v2 仅供历史审计。后续 v4 撤稿记录及“Errors in paper uncorrected”已随 [本原路线地图](../literature/primitive_routes_reading_map_20261005.md) 保存，项目未采用其定理。
- **ζ(7) 外部声称**：Zenodo 22920911 的决定性外区表格问题见 [独立审阅](../research/zenodo_22920911/review.md)；可保留的相对范数估计不等于原证明成立。
- **Zudilin 文件身份**：`zudilin2002_irrationality_values.pdf` 实际是 very-well-poised 超几何级数多重积分论文，不能按旧文件名当作窗口定理来源。更正见 [文献目录](../literature/README.md)。
- **Ball–Rivoal**：本库保存 Rivoal 学位论文等公开材料；未取得的 2001 年期刊原文不能用占位文件替代。
- **CDT 版本**：218 页 arXiv v2 与作者站 220 页快照分开保存；证明编号及适用条件应注明所用版本，不能默认两者逐页一致。
- **错误归属**：本项目 Hankel 矩脚本、测度优化约束和 μ/τ 翻译的错误属于本地实现或移植问题；归因需引用 [重启审计](../research/restart_analysis.md) 和具体源码，不能一概指称原论文有误。

“集合中至少一个无理”无法指定 ζ(7)，分别无理无法推出指定线性组合无理；p-adic 结论也不能直接移给实数特殊值。引用时保留完整量词与适用假设，并明确本项目成果是独立证明、已有定理的推论，还是尚未闭合的候选。

## 归档与引用

优先采用原件对应 manifest 中的作者、题名、固定版本、来源 URL、页数与 SHA-256。文件签名、摘要和首页核对只能确认身份，不能认证数学正确性。后续轮次的 `*_reading_scope.md` 记录实际阅读范围，不应将只读了某节表述为全文审定。

本次整理保留整个文献库；旧归档生产脚本移入历史包后，不再默认执行或自动替换来源。论文与网页按原来源的版权、许可和版本要求引用，代码的 Apache-2.0 不覆盖这些原件。新增文献应另存快照与清单，不覆盖已引用版本。
