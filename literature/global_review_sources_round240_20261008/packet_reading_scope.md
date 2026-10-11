# B240实际阅读与执行域

2026-10-08。对应NEW research/global_direct_holonomy_review_round240_20261008.md。数学程序、素数/参数扫描、Lean/CAS/PSLQ、旧producer执行均0；新操作只有文件读取、pdftotext选页提取、网页阅读、写NEW稿及hash。旧239/main/policy/manifest未改。

## FULL冻结研究输入

本轮实际FULL读取：

- research/joint_lattice_metric_bridge_round237_20261008.md：9821 B，SHA256 cf2550e55910f6feceff0652aa38b5a102749aed7479c67540a4a80bc7e190a8。
- research/actual_flag_determinant_round238_20261008.md：8061 B，799156d8cc6e030e77622cfe5eeeb7fa0ad5a4a61b80e8fb95e8851101f14954。
- research/actual_cofactor_arithmetic_round239_20261008.md：9483 B，25ec2e97a75e477e305d37aa1c59044155c41499e2a00240cddfb31561151262。

第一次三稿批次的aggregate输出曾截掉239的一段，随后将239整稿单独重新FULL读取，完整无截断。未称本轮重审每份旧primary、所有审阅收据或全部archive。

## 当前CDT作者件：只读完整选页

复用既有 literature/global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf：3628820 B，SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c，220物理页。新鲜打开作者URL <https://math.uchicago.edu/~fcale/papers/L2chi.pdf>也返回220页，实际web初始文字覆盖intro pp1–5；未重新下载并比较fresh件hash。另实际读取arXiv metadata <https://arxiv.org/abs/2408.15403>：v2日期2024-09-16、登记218页。因此不混称220页作者件为arXiv218页同一byte版本。

实际完整读取当前220页PDF新提取选页：

|NEW文本|完整实际范围|bytes|SHA256|
|---|---|---:|---|
|packet_cdt_current_pdf29_34.txt|物理29–34，§2.11 maps/mixed periods/完整Lemma2.11.13与Theorem2.11.17|22592|ec8418f934c08a9f70f27b05e469a1f8ce28d2c37f5a6f5ae9d081d62d59009d|
|packet_cdt_current_pdf175_180.txt|物理175–180，§14开篇/14.1完整Hadamard关系泛函构造；不含后续14.2–14.5全部证明|21335|94b843702197d6fdc719619067c3d2689e0d0047dd27c6206aec19939b884437|
|packet_cdt_current_pdf190_199.txt|物理190–199，§15.1–15.5及15.6开始；15.6续页/15.7未读|37783|f0310bf198a942c1b2d5c33171b7a41d307db555fbeef5b91a18edcb2371a04c|

还实际FULL读取既有235 currentPDF1、2页toc提取文本，仅用于定位。上述pdftotext均exit0，系统打印MiKTeX Windows旧版本提示，不是数学运行。没有本轮PDF截图视觉阅读或全220页claim。

## 新固定Tang作者源码

Root保存的primary在本目录root_zeta23/。本稿实际FULL读取以下原文件：

|相对路径|bytes|SHA256|
|---|---:|---|
|Zeta32/Family.lean|6874|59d46a8462ac426bd393864d849bf4cd0f906399c4c583c9736b10835e289dbd|
|Zeta32/Analytic/Logistic.lean|10769|84390d945a8a9fc78d611c53abf4ee5816f28f87d082909a3d9207769b67d44c|
|Zeta32/Analytic/Contour/Moments.lean|11604|4102b948659135c2a29e08c9a5f8ed0a2051d797f9e0c8d100d09153b5fb9ffc|
|README.md|7228|ca99b77622320db0b0772baa4f72852a240de1c8163e1e81f9208ea1b37dadbf|

公开pin：<https://github.com/dtq1997/zeta2-zeta3-linear-independence/tree/669c92bf7a3728e0de9ad80c373bc29fb5ca3d58>。web打开pin失败Cache miss；本地Root保存primary阅读仍完成。commit.json大输出曾截断，因此仅另解析SHA、html_url、日期字段，不称FULL metadata：669c92bf7a3728e0de9ad80c373bc29fb5ca3d58，2026-09-30T07:11:28Z。

未FULL读取Interfaces/Criterion/Assembly/PrimeObstruction及全部import依赖，也未验证Lean kernel。主稿R3采用实际读到的一般inverse-power theorem及其纸面telescope条件；R4–R9是本稿另行纸推，不认领README数值结论或所有仓库proof。Root消息提供的新泛函草图是协作输入，不替代上述实际read。

## 定向网页/novelty范围

实际打开DLMF24.10，数学采用仅§24.10(i) eq24.10.1及分母解释：<https://dlmf.nist.gov/24.10#i>。已存packet_dlmf24_10_selected_reading.md为窄读记录，不是整网页快照或完整参考书阅读。

定向primary-domain搜索只围绕Catalan+πlog2及ζ3/ζ5精确混合值。结果含Fischler arXiv2109.10136与Krattenthaler–Rivoal math/0311114 abstract；没有阅读它们全文，不从搜索页导入数值定理，不采用搜索返回的可疑ζ3/π³声称。检索未发现精确两候选既有定理，**不等于证明全球新颖性或全部文献未解**。本地rg定位旧mixed-period记录，未将hit片段当FULL旧稿阅读。

数学新资产限于：完整logistic selector/核符号、R7安全全系数清分母、R9 all-scale局部period秩；K的实际积分身份、native fill与all-prime-power R12–13。Root独审后只补R12的p>N/a=0平凡边界，再实际FULL复读最终稿；数学结论不变。primitive费用、target∞nonzero、CDT map/strict margin和新数值无理性均未完成。
