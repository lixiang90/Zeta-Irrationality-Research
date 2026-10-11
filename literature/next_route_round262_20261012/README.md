# 第262轮：来源与实际读取范围

2026-10-12。本目录新增保存本轮覆盖半径证明所用的固定原件，不覆盖旧快照。散列确认文件身份，不认证数学正确性。

| 原件 | 版本与来源 | 身份 |
| --- | --- | --- |
| [ASVV 双穿孔度量论文](asvv_0903.1761v2.pdf) | Anderson、Sugawa、Vamanamurthy、Vuorinen；[arXiv:0903.1761v2](https://arxiv.org/abs/0903.1761v2)，2009-03-21 | 13页，181061字节；SHA-256 `6e7d2945d2b7387a19ae8ac674d6f5fc638354ff084c0997aee9770799979cde` |

下载地址为 `https://arxiv.org/pdf/0903.1761v2`，获取日期2026-10-12。网页工具读取该固定PDF文本；PowerShell随后保存原件并计算SHA-256。

主代理实际读取原件的物理1–3页中曲率规范、(2.1)、(3.1)及其参数约定；物理5–6页中度量构造、Theorem4.7与证明。载体审阅者另读取物理1–2、6页并独立复核相应公式。没有将13页整篇标作全文审定，也未重新证明论文全部定理。

另外实际核看了 [DLMF19.4.1](https://dlmf.nist.gov/19.4#E1) 的完整积分导数和 [19.7.1](https://dlmf.nist.gov/19.7#E1) 的 Legendre 关系，modulus `k`转成 parameter `m=k²`。本轮证明的严格 Cauchy–Schwarz上界、双穿孔基点结算和指数截断比较由项目自行推导。

算术分支复用固定 [CDT v2节选](../refined_budget_round261_20261010/arithmetic_cdt_v2_physical119_124.txt)、[66–67页](../refined_budget_round261_20261010/arithmetic_cdt_v2_physical066_067.txt)及[原件定位文本](../trace_sources_round221_20261008/cdt_fixed_v2_locator.txt)的§6.2、§6.6相关段。它们的旧字节保留。最新数值目标检索的具体论文、陈述、版本与未覆盖范围见[新颖性审查](../../research/next_route_novelty_20261012.md)。

本轮研究总入口：[第262轮结算](../../research/research_next_route_progress_round262_20261012.md)。
