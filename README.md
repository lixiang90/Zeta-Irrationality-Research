# Zeta Irrationality Research

ζ 与 Dirichlet L 函数特殊值无理性的研究档案，包含方法总结、证明尝试、计算证书、原始文献和 Lean 形式化资产。

**当前结论：ζ(5) 的绝对版沿用固定上游形式化并完成本地桥接；本项目尚未得到 ζ(7)、3ζ(3)+ζ(5) 或后续指定 ζ/L 值的新无理性定理。** 已有成果包括已知定理的具体数值推论、全尺度结构引理、有限尺度的完整参数族排除，以及范围明确的算术和解析障碍。

研究记录更新至第266轮（2026-10-13）：在原canonical分量识别下建立M₀,₈完整两坐标的Barnes全素数幂安全界，记录原下降式归一化纠错；补齐群的全部幂次仅增加次线性信用，仍未通过数值净预算。限期来源核查已结束，下一轮作宏观准入复盘。文献和形式化资产继续保留。

## 从哪里开始

| 阅读目标 | 入口 |
| --- | --- |
| 各方向已经证明什么、还缺什么 | [研究方向与成果](docs/RESEARCH_DIRECTIONS.md) |
| 尝试为什么成功或失败 | [成败教训](docs/LESSONS.md) |
| 方法演变与当前停止条件 | [研究历程](docs/HISTORY.md) |
| Lean 证明的实际状态 | [形式化资产](docs/FORMALIZATION.md) |
| 数据恢复、证书复核与 Lean 构建 | [复现指南](docs/REPRODUCIBILITY.md) |
| 原始论文、版本与阅读地图 | [文献指南](docs/BIBLIOGRAPHY.md) · [文献库](literature/README.md) |
| 恢复当前目标、路线与下一命题 | [当前STATE](research/STATE.md) · [长期goal](docs/RESEARCH_GOAL.md) |
| 最新研究结算与宏观选择 | [第266轮完整向量核查](research/m08_target_vector_round266.md) · [第265轮正式来源选择](research/source_selection_round265.md) |
| 其他长期研究也可复用的组织方法 | [持久工作协议](docs/LONG_RESEARCH_WORKFLOW.md) |

## 研究成果概览

| 方向 | 已有成果 | 主要限制 |
| --- | --- | --- |
| ζ(5) 基线 | 固定上游绝对版桥接；论文镜像的部分中间证明 | 镜像仍有占位证明，与绝对版分开核算 |
| ζ(7) Gram 与整数格 | 正性、局部整除、饱和格和部分完整参数族排除 | 没有同一整数输出的无界负净指数 |
| 固定混合值 3ζ(3)+ζ(5) | 正 Gram、完整 content、部分子空间族统一下界 | 有限尺度排除不覆盖全部构造 |
| 对数矩与 Padé | 真实渐近、无穷非零接口、完整 gcd 与正测度接口 | 未闭合完整本原算术成本与解析衰减 |
| 二重对数与积分族 | CDT 定理的具体无理性、独立性和关系分类推论 | 未确认全球首次性，不指定新的单个 L 值 |
| 奇数权 ζ/L 与 holonomy | 真实周期触发、整数坐标、函数秩、全前缀预算和域障碍 | 同一函数族的严格数值矛盾尚缺 |
| CM、Fricke、χ−8 与混合周期 | 真实投影、全叶审查、整模型、内容减费和停止证书 | 各自仍缺净余量、适用定理或实际非零性 |
| 动机、K₂ 与相对周期 | 结构辨识及固定投影机制的严格排除 | 尚未转化为完整数值分离证书 |

## 仓库结构

```text
docs/                 阅读总览、成果、教训与复现说明
research/             技术证明、审阅、数学脚本和计算证书
literature/           原始论文、网页快照、阅读范围与历史清单
Zeta5Irrational/      本地 ζ(5) 论文镜像与绝对版桥接
Zeta5-mo271/          固定上游参考源码及原许可证
Zeta7Formal/          ζ(7) 形式化探索及保留的 Apery 资产
archives/             可恢复历史记录及原始资产清单
scripts/              数据恢复、公理检查和完整性检查工具
lakefile.toml         根 Lean 项目配置
lake-manifest.json    固定依赖版本
```

技术稿保留原有路径，便于追溯证书。旧稿属于历史证据；判断现状时优先读总结及稿件开头的状态更正。[研究目录](research/README.md)按路线提供技术入口。

## 快速检查与复现

仓库检查只需要 Python 3 标准库：

```bash
python scripts/check_repository.py
python scripts/research_state.py check
```

较大的计算 JSON 以同路径 `.json.gz` 保存，原路径、字节数与 SHA-256 见 [资产清单](archives/asset-manifest.json)。运行依赖这些数据的旧验证器前按需恢复：

```bash
python scripts/restore_assets.py --path research/zeta35_plucker_p12_certificate.json
# 或恢复全部大数据
python scripts/restore_assets.py --all
```

根项目固定 Lean `v4.33.1`。已安装 elan/lake 时：

```bash
lake exe cache get
lake build
lake env lean scripts/FormalizationAudit.lean
```

最后一条检查绝对版桥接的公理依赖；镜像中的 `sorry` 不代表绝对版目标依赖它。本次整理未重新全量构建 Lean。ζ(7) 的完整工程尚未闭合，参数问题与构建范围见 [形式化说明](docs/FORMALIZATION.md)。

## 证据与后续投入

数值定理、全尺度书面证明、有限精确证书、条件判据和探索实验分别记录。函数独立性不直接给端点数值独立性；安全费用上界不足不等于方法不可能；一个来源的实侧或非零资产不能免费移给另一个来源。

当前目标、稳定窗口、停止范围与复盘计数只在 `research/program.json` 维护，STATE由工具生成。上下文压缩后先读STATE，再沿命题证据恢复；组织和局部no-go不能替代新的数值定理。

263–264实际评价格窗口已经结束。265选择M₀,₈中对指定3ζ(3)+ζ(5)的完整primitive pair核查；266给直接安全模型并明确其费用不足，结束这一轮来源核查。没有证明actual primitive费用下界，重开仍须有改变完整预算的新内容机制，见[最新结算](research/m08_target_vector_round266.md)。

## 来源与许可

上游源码、第三方文献与项目原创笔记的权属分别保留。本仓库不以统一许可证重新授权全部论文。引用与再分发前请查看 [来源说明](docs/THIRD_PARTY_NOTICES.md)及原件许可。归档、散列核验与数学审定是不同事项。
