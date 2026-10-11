# 第221轮合并阅读与执行范围

2026-10-08。这里登记本轮实际阅读，配合 [trace作者的选页说明](reading_scope.md)，不把选页阅读写成整篇审读。

## 文献

唯一primary是复用的 [CDT固定v2 PDF](../cdt2024_l2_chi_minus3.pdf)：218页，4517169 bytes，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。本轮新下载PDF、HTML、TEX、README均0。

Root本轮实际完整读PDF一基页122–123、149–150、153、157、172–173，共八页。122–123核任意prime-array平衡费用及基本/细化能量式；149–150、153核粗trace及实际leaf条件；157核plus/minus对literal n分母的差别；172–173核χ−3证明实际十四行及16603/3920费用。149–150是选页，不能写成Root完整读Corollary9.0.19全部证明。Root复用此前已读的66–70等页，不登记为本轮新读。

trace作者及其独立审阅者本轮实际完整读取146–174、67–68、203–205页段，具体范围见原选页说明与 [独立收据](../../research/research_round221_actual_trace_review_20261008.md)。算术作者本轮完整重读122–123，复用此前66–70页；其独立审阅者本轮完整核122–123及67–68相关页。未重新执行原论文的有限线性代数或数值附录，未声称完整读218页。

本文件夹保存的全PDF文本locator仅用于定位；选页TXT是文献文本。Root本轮完整读取两份reading_scope及各最终研究稿/收据，但未声称完整读locator或全部选页TXT。

## 本轮研究文件

Root实际完整读取最终保存的五份数学稿：

- [有限有理微分投影](../../research/cyclotomic_relation_differential_projection_round221_20261008.md)，5368 bytes。
- [真实奇偶与反射分析](../../research/cyclotomic_symmetry_analytic_round221_20261008.md)，16171 bytes。
- [全素数幂算术费用](../../research/cyclotomic_symmetry_arithmetic_round221_20261008.md)，13880 bytes；已采纳有限坏素数p=3的边界修正。
- [CDT真实trace迁移](../../research/cdt_actual_trace_transfer_round221_20261008.md)，13182 bytes；T10系数式限定n≥1，并明确三个零次系数均0。
- [平方商所有共同映射的上界](../../research/cyclotomic_quotient_global_map_obstruction_round221_20261008.md)，7527 bytes。

各稿均有另一研究者实际完整阅读最终稿的独立收据；Root也完整读五份收据。身份/hash及报告独审另在 [本轮清单](../manifest_cdt_cyclotomic_symmetry_round221_20261008.json) 登记。Root本轮另完整读220全局报告、220跨目标稿及旧repository-carriers稿，后者只作为历史分析，不能冒称本轮已复核云端最新仓库。

## 执行与结论边界

数学程序、CAS、prime/参数扫描、矩阵执行、数值积分、PSLQ、Lean、Git均0。工具只用于文献文本、Markdown、metadata/hash/link/control及追加边界核验。新上界与分母lemma是纸笔推导并独审，不是Lean验证；尚无新的数值无理性或线性无关性定理。

本轮没有更新或重新调查OpenAI仓库，没有新目标的最新文献/novelty核查。Catalan源用于方法基准；新证明限制当前已付费用及普通单图能量判据，不排除新函数源、优化联合整格或其他细化能量式。
