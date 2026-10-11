# 第240轮 C 实际读取与运行账

2026-10-08。任务：固定原 M₀,₁₀的全n D₃首证书准入，具体检验新 primary 奇维 primitive机制。正文为 research/global_period_projection_review_round240_20261008.md。本scope只登记本人实际读取，不借其他代理的独审替代primary。

## 1. FULL冻结数学输入

以下保存文件本轮实际完整读取全文；FULL不表示重新执行原稿全部证明程序。

| 文件 | bytes | SHA256 |
|---|---:|---|
| research/cellular_projection_bridge_preparation_round237_20261008.md | 8483 | a1ee6f1cc33bac6ccb860b8759320d39186c8e04b27fdcd4237f8193ee30bb40 |
| research/cellular_uniform_projection_gate_round238_20261008.md | 7305 | 0f203220ec292dfd279ac2f1afbe7950732f0189fec33a2eb6a1901e43e513d5 |
| research/actual_cofactor_budget_gate_round239_20261008.md | 10804 | 8c0db240d561764395d958332fd144efb0d1ad6f08ef889c1488805830e31909 |
| research/global_catalan_weight4_review_round236_20261008.md | 13797 | cf93376bf4add588566fc577a3cf3bf682b5164dc9b1e02036e1e588cbfbb6a0 |

236是本人原始源码阅读报告；本轮重读它没有变成一次外仓库freshness检验，也没有重新FULL外repo源码。239只采用门槛稿范围，不声称本轮新FULL其两份算术证明或全部原CRT。

## 2. 复用primary完整选页

本轮对以下TXT实际FULL读取。PDF页号是物理页，不把选页FULL冒充整篇FULL。

| 既存TXT | pages | bytes | SHA256 |
|---|---|---:|---|
| literature/actual_cofactor_arithmetic_sources_round239_20261008/lambert_brown2012_pdf08_11.txt | Brown2012 PDF8–11，printed956–959 | 10769 | 892a7bf77d14a6672784b8ed0b4b11523dfc6a200d82f214b9a0d5c7d655ebf6 |
| literature/joint_lattice_metric_sources_round237_20261008/alternative_brown2014_pdf34_35.txt | Brown2014 PDF34–35 | 7070 | 655ffef8faee0e8b610fb6da4604ef65647fdce73cd5d9d235b0982e3e265a29 |
| literature/joint_lattice_metric_sources_round237_20261008/alternative_bzv3_pdf29_30.txt | BZv3 PDF29–30 | 7371 | 5bb18912a1f3f899c14f98dc8394b722f38f63bd317d364eac71c55b48c60b61 |

具体采用：Brown2012 Theorem2.4、Definition3.1、(3.3)–(3.4)、Lemma3.2及motivic结构；Brown2014 §10.2.6、Theorem11.2、Corollary11.3与高标记点数限制；BZ原F/ω、experimental rank4、结尾次主渐近与有限头范围。没有通过I₀数值等式推断motivic坐标。旧PDF复用，不重复下载。

## 3. 唯一新primary与实际页范围

Tosi, An explicit study of a family of cellular integrals，arXiv:2601.00346v2，首页19 Mar2026，36页。[固定v2](https://arxiv.org/abs/2601.00346v2)，[当前metadata](https://arxiv.org/abs/2601.00346)。当前metadata明确v2修正main result中ψ定义错误；只据此记录版本，不猜错误原因或扩大novelty。

| 新文件，本目录内 | bytes | SHA256 |
|---|---:|---|
| dual_tosi2026_cellular_v2.pdf | 725343 | 91fa8a63db8c51d61e17268d46af2aa8672ea0a79d79072c358c3af44aab135e |
| dual_tosi2026_pdf01_03.txt | 14528 | 3d045b7068c77525c6ffbdc86f6aa51682aa2d2ffee9d5cb7a524ad1bc810f29 |
| dual_tosi2026_pdf06_08.txt | 11706 | a7f58797de638fec643b291b75f811bf38d28e6c78e5922217c8f5cd51577f75 |
| dual_tosi2026_pdf09.txt | 4004 | 81cc6e0c4fee80fab35cc2c8dbfa04804f8427c9fe4fa6ff8adb0af26446dd19 |

三个TXT均实际完整读取：PDF1–3是原件首页/目录/完整Introduction与Theorem1陈述以及§1.1开头；PDF6–9含同一form的homogeneous/simplicial/cubical定义、严格cellular范围、Proposition4、Lemmas6–9及Lemma9完整证明终点；PDF9后半§1.3开头也读到。未读PDF4–5、10–36，未独立审核全部闭式求值证明或其conjectural explanation。本文所用显式primitive已独立纸核Cartan identity，无需采用未读后文。

本轮targeted网页检索定位cellular/coaction/parity原文；先误开v1 HTML后改读v2，v1不作数学输入。arXiv metadata及v2页面/原件为primary。其它检索摘要/secondary页面仅定位，不作证据，也不从search absence声称全局新颖或无定理。新PDF仅一次下载到workspace；没有重复下载旧Brown原件。

## 4. 数学与文档账

数学程序0；数值/prime/参数扫描0；旧producer0；Git mutation/fetch/checkout0；Lean0。新PDF1，新TXT3。MiKTeX pdftotext文档抽取3次，分别1–3、6–8、9页，均exit0（附旧Windows警告）；不是数学执行。

两次早期rg shellglob出现路径语法提示，后续使用准确LiteralPath读取；不是数学运行。若组合tool输出警告truncated，采用的FULL文件另以足够budget重读，其中236报告与Brown2012选段已单独完整重读；没有把搜索/截断输出扩大成全文读域。实际FULL也读既存alternative_reading_scope作为locator，没有继承他人全部primary读域。

本轮只新增本稿、本scope和以上新source副本/选段；旧239/更早稿、main与manifest不改。正文新(C5)–(C8)是原对象cubical与对角Euler排除；D₃全n包含性仍未付，未宣称新的数值定理。最终保存后作者实际FULL复读，身份另发Root；独立审核须另有receipt，不能以作者读冒充。
