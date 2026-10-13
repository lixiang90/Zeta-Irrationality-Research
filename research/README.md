# 研究技术档案

先读[成果地图](../docs/RESEARCH_DIRECTIONS.md)与[成败教训](../docs/LESSONS.md)，再进入具体技术稿。此目录保留证明尝试、完整失败证据、独立审阅、producer、验证器与数据。文件中的结论仅覆盖其声明范围；旧稿的乐观描述应服从后续纠错。

续研和上下文恢复先读[当前STATE](STATE.md)与[长期goal](../docs/RESEARCH_GOAL.md)。STATE由唯一当前账 `program.json`生成；最新阶段稿不是另一份可变状态。

| 路线 | 主要技术入口 |
| --- | --- |
| ζ(5) 方法与原论文重读 | [方法扩展](zeta5_method_research_expansion_20261004.md) |
| ζ(7) 早期纠错 | [重启审计](restart_analysis.md) |
| ζ(7) 端点与整数格 | [成果总稿](zeta7_research_progress_20261004.md) |
| 固定混合方向与 Plücker | [研究总览](research_overview_20261004.md) |
| 全部奇数 ζ 与 L 的统一背景 | [总体策略](odd_zeta_global_strategy_20261004.md) |
| 对数矩与 Padé | [对数矩进展](odd_zeta_log_moment_progress_20261005.md)、[本原缺层与正测度](odd_zeta_primitive_routes_progress_20261005.md) |
| 周期分类与整模型 | [周期研究](period_holonomy_progress_20261005.md) |
| 奇数权 ζ(7) 模源 | [实际模型与预算](cdt_odd_progress_20261005.md) |
| CM、Fricke 与增长行列式 | [跨路线结算](research_global_review_round252_20261010.md) |
| native χ−8 | [完整净结算](research_native_chi8_progress_round257_20261010.md) |
| 多源混合周期 | [来源选择](research_source_selection_progress_round259_20261010.md)、[全局复盘](research_global_review_round260_20261010.md) |
| 标准入口停止与 AP 候选的原始门槛 | [第261轮联合证书](refined_budget_gate_round261_20261010.md)、[进展报告](refined_budget_progress_round261_20261010.md) |
| AP指定组合首证书（262） | [第262轮结算](research_next_route_progress_round262_20261012.md)、[费用证明](next_route_ap_cost_20261012.md)、[全图上界](next_route_cover_bound_20261012.md)、[无穷远与载体](next_route_carrier_20261012.md)、[目标检索](next_route_novelty_20261012.md) |
| 实际联合评价格与宏观goal（263） | [正式复盘](research_global_review_round263_20261013.md)、[support/Frobenius](joint_evaluation_support_round263_20261013.md)、[完整Smith与balanced格](joint_evaluation_lattice_round263_20261013.md) |
| 完整index下界与leading-box裁决（264） | [费用证明](joint_budget_bridge_round264.md)、[轮次结算](research_round264_report_20261013.md) |

## 数据与历史记录

大 JSON 压缩为 `.json.gz`，运行原验证器前用 [恢复工具](../scripts/restore_assets.py)还原。原始字节与散列见[资产清单](../archives/asset-manifest.json)。

累计长日志 `cdt_odd_background_progress_20261006.md`、追加式管理规则与 `archive*.py` 一次性运行器以原路径、原字节保存在[历史包](../archives/history.zip)。它们有重要早期证据，也包含大量逐轮重复摘要，已退出默认阅读路径。可解压到独立目录追溯；不要将它们覆盖到当前仓库或重跑旧归档命令。

历史manifest记录当时字节，不能认证本次新导航。原文献、数学稿、证书和Lean源码的保存核验由[整理清单](../archives/preservation-manifest.json)提供；这项检查只确认文件完整性。
