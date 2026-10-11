# 第245轮 C：CM 原文评价与全整类型实际读取范围

2026-10-10。只复用存件，不 GET、不改244。数学程序、CAS、prime/map扫描、历史producer、Lean、外仓库写0。Python仅做文档截取、HTML alttext提取与读取，不计算数学。新来源文件是已存官方原件的精确选段，不算新论文下载。

## 1. 原件和实际 FULL 范围

唯一 Sun–Zhou 原件仍为 ../global_review_sources_round244_20261009/alternative_sun_zhou_2602_12091v2.html，1295974 B / 45dac041f91f907b566863b6aaa56ff1bf251c0c899b7882460503bc9caa2e2d，对应 https://arxiv.org/html/2602.12091v2。原件未变。

本轮实际 FULL 读此前保存的引言/完整 Theorem1.1 statement/Table1 TXT13189 B / b4109e83c58a0685fdac5040d2b7d4600db808c3071f3e8fae2abb4f7dd6ae0f；本轮新增并实际 FULL 读以下完整选段（公式逐一保留原 math alttext；HTML保持原MathML）：

| 选段及完整界 | HTML字节 / SHA256 | TXT字节 / SHA256 |
|---|---|---|
| dual_sun_zhou_section21，S2.SS1至S2.SS2之前；完整§2.1、Lemma2.1 statement/proof | 89360 / 967ea14e275d8b9589a4a3791fc5b3c763b67d11947eca25d64940d5db439e14 | 11043 / 4dd1cdc075ee8dc0771c723f3ac33e0e760a96dba0a38f8dbbadbe5905fc6b66 |
| dual_sun_zhou_section22，S2.SS2至S2.SS3之前；完整§2.2、Prop2.2 statement/proof、Theorem1.1(a)(b) proof | 197879 / 41c7798615a21f1187fa1383a7e9a84af010c363d0c1c23ea573986fbda6c6cf | 17075 / 8a428a7fb787aa7965f01056a74432abeefbac361f8fcb73018f849d21843f32 |
| dual_sun_zhou_section23，S2.SS3至S3之前；完整§2.3、Prop2.3/2.4全部statement/proof | 138418 / 37cabc46598693dd75ef27655554f34bd23d3a3f73dd93f4852379bef06e3f57 | 10951 / 34c6054b62802b5b701fcceb8279ff9c041e656a6847498ccab765b2e8a61d63 |
| dual_sun_zhou_upstream_refs，仅原文[12],[14],[37],[69],[72],[75]完整bibliography entries | 3090 / 5c3124edd89aa0da21c8de753176d931681a726eb8877b97c6abbf0fb2cea501 | 1107 / 295e9624b83bda26e36a95eb54ad157e969e5236f6ca82e072c7e38ae074e860 |

实际全文读取是上述TXT正文/数学及必要原HTML定点核对，不冒称逐字 FULL 阅读约1.3MB的原始HTML标记。提取完整范围和原件身份保存在 dual_extraction_record.json，2174 B / 9711fc322a580523799a0c6cb62f4bd15ef52d2c01dfc395708652a9e1eed5b2。

定点另读原件 S2.E63/E67/E68 的原始 TeX annotation，确认最后 Eichler项缺Im τ因子；原件不改。数学稿以完整定义(1.26)补正(2.67)，且限定只是存HTML display，未读PDF断言同误。Math alttext的字体合并由稿内 E₄/𝓔₄定义区分。

没有读三阶调和数§3、讨论§4、全文全部参考文献或全部模形式源码。已抽取六个bibliography entries不等于读其原著；[69]一般CM λ理论、[72]/[75]所有upstream证明没有 FULL 认证。稿内另外自含核所需两个 χ₋₇ Epstein格值，不能升为所有CM表认证。

## 2. 数学目标及独立审阅的实际 FULL 对象

- research/global_cm_log_trigger_round244_20261009.md，6783 B / 187cbbd9bda470a07691dc2c962dd5054144e6c65a6542491498bb9342456d9c，完整6节/C1–C7及新增G-function/native盘段，冻结原件未改。
- research/cm_complete_denominator_types_round245_20261010.md，最终6406 B / bb935f5caedd0a34d58221638d263a5d92c308a51f8137b6e3be1a1e3efef459，实际重新 FULL 读完整6节/D1–D10，独立纸核全primepowers、全部prefix、七/八字面类型及条件严格预算。此前实际 FULL 读6405 B / ef42c711678a1598acc01a39a903cece98b271e69df056ef23de5fcdf474f9dc；作者仅修裸quad为\quad，数学未改。收据另存 research/research_round245_complete_types_review_20261010.md。
- 已存 CDT ICM PDF3–5 TXT17482 B / 08be95e4026ee04ec428af0703f4bcfa439334c813e119d383bfc6df27dd1ad9，本轮实际 FULL 重读。不是20页PDF全部，也不领取主文§6–8全部proof。
- 已存 literature/cdt_weight4_space_germ_sources_20261007/cdt2025_effective_holonomy_arxiv2510_04156v1.html，775388 B / b255b9a303fc0db1972ff1e874c02a172c1f5f8c9acb80f676db50ce1e411769，仅实际读tau定义与Eq(2.2)完整alttext，明确∫_(T²)无额外2；未称FULL该HTML。

## 3. 本轮新结论与范围

作者评价C1证明链正确接通，但中间display需按定义补因子。P8–P12给同一F/G的一条Fricke transported叶响应>1、native响应≤2/63，故同一关系不取消那条叶的log。这个实际反例不排除绕开坏叶的大图；有限ramification不取消这一个log。没有从变参数/Eichler名字或七行闭包领取actualrank。

全整数模型 Root稿是独立审阅的输入；只认证0/2/3与conditional七/八类型，不领取最优fee或strict map。245–246有界准入、248formal复盘、数值目标active。数学稿、scope及新收据各自最终保存后实际 FULL 作者复读；不借别人的primary读域、archive核验或Lean结果。
