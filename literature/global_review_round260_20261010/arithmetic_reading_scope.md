# 第260轮 arithmetic 子任务阅读范围、原件 pins 与运行边界

2026-10-10；同一唯一mixed来源的宏观纯族/算术复盘。不写259旧稿，不归档，不改manifest/main/policy；Root另负责这些总账。本文scope仅说明本子任务亲自读取的内容，不继承其他agent的FULL。

## 1. 实际FULL的数学与旧边界

* research/source_selection_mixed_field_round259_20261010.md：最终17525 B / fad9d69a943026d1b6941e9af71b8786cc6643d31007a11ebce0f12df98e0517，260实际全文读，17.5k文本未截断。使用其最终F2–F10的实际field/rank/type证明，非旧16403 B版本。
* literature/source_selection_round259_20261010/field_reading_scope.md：6647 B / 3ffda140355086a345f10f3cb69b2858245b63ebb5c93c1ba863168fc9ea4771，260实际全文读。
* literature/manifest_source_selection_round259_20261010.json：仅解析读取files之外全部字段；193-file数组与全部逐pin对应物未由本子任务重审，**PARTIAL**。Root已独核PASS不转作本子任务FULL。
* research/source_selection_mixed12_round259_20261010.md：本子任务259写作者的冻结资产；260不重写，不将本次未重读的自身旧稿列作260FULL。

## 2. CDT 固定原件：范围严格限所列页

原件 literature/cdt2024_l2_chi_minus3.pdf，固定 arXiv:2408.15403v2（2024-09-16），218物理页，4517169 B / 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。260使用已有PDF；文档工具提取，不下载、不改原件。218页整体是**PARTIAL**，仅以下页的文本实际FULL。没有声称逐页视觉/版面检查。

|260实际FULL文本节选|物理页|bytes|SHA256|
|---|---|---:|---|
|arithmetic_cdt_v2_pdf146_149.txt|146–149，9.0.3、9.0.13及univalent叶条件|10344|cfa59e0b712749e084b2ef179f92b05035ecd97cae7e6cc124222304393239f5|
|arithmetic_cdt_v2_pdf153_158.txt|153–158，pure7、逐行类型、17与14实际比较|15088|87f8c518e32c3ae24ebe260e03928f27f84edc95484b3bfe25a68c0507cb4dba|
|arithmetic_cdt_v2_pdf164.txt|164，原三period关系、G的sym定义、order4|2698|06bf248563889acb9f962bc850f5e45aab63fbfdb9f584416fafcb81a7046fe0|
|arithmetic_cdt_v2_pdf165_174.txt|165–174，actual pure7与14独立性、第四积分反例、14真实type/预算|22589|7c2cf26d9f774d0b21e2e3f6e184857670a93651d85f6ca0286343865120ac5f|
|arithmetic_cdt_holonomic_physical089_090.txt|89–90，Theorem7.0.1的holomorphic φ、λ>τ及strict bound|5908|8083235335c31b62694b5483d0cc54bcbd4d1936bdebd07018752d0b19a307c2|
|arithmetic_cdt_types_physical122_124.txt|122–124，Theorem8.0.1、Remark8.0.6 nested-column formula|9277|b37afdb257f65a8978a2f8b7e6c083ed7b785a3afa6bb2c6ed0ab6c80a3b4557|

前四份由原件在本轮直接定页提取。后两份是259 field 的定页节选逐字节复制为本轮arithmetic_*，本子任务本轮已实际全文读对应所选页；复制不是新原件GET，也不是把其他agent的scope当成阅读。物理页为PDF页索引+1，恰与该CDT稿印刷页一致。

从这些原件获得的事实：原14行=7 pure+7原G-derived，依赖原三period反证关系及order4；第4 primitive有确实依赖；17行原方案较差；原14的16603/3920包含原integrated类型，不能借入当前integer pullback。原9.0.3自身也明确分母下标与quotient coordinate费用同步改变。

## 3. Landau primary：实际读selected两页

原件 literature/global_review_round260_20261010/analytic_kim_ma_ma_2015_two_punctures.pdf，由Root/analytic来源已保存，175296 B / 369b5fd36e1cf736cfbb6ace50d1eab6068c7241b19a18d8c9e15e3cc7616576；Kim、Ma、Ma，Estimates of the hyperbolic metric on the twice punctured plane，2015，doi:10.5186/aasfm.2015.4058。整篇13页本子任务**PARTIAL**。

本子任务实际全文读物理1–2页selected文本，保存逐字节副本 arithmetic_kim_ma_ma_physical01_02.txt，5892 B / 0e2b28083478dc40535ffe410585f62206aa74c476d8ec4e395282919c8a64f7。不是依赖Root消息或失联agent结论。实际核(1.2) K=Γ(1/4)^4/(4π²)、(1.3)及紧接的holomorphic-map Landau不等式；第一页面明确curvature−1规范、disk密度2/(1−|z|²)。没读取/采用该文后续更精细新bound或数值表。

Gamma的K<16/3本子任务另给积分严格Cauchy–Schwarz纸证；没有Gamma数值调用、CAS或优化。pure-only omission点α=(1−√3)/2、β=(1+√3)/2来自当前t(s)的精确rational fibers；不继承H坏芽或原CDT map。

## 4. 本轮数学证书与精确准入/停止范围

260新稿 research/global_review_mixed_arithmetic_round260_20261010.md 的A4–A7是本子任务新纸证：

* Pure7在实际K=C(s)上独立：first5等价ℓ、Li2、J，commutator差为非零constant与非零constant·√(1−t)，而该sqrt不在K；后两primitive的obstruction在任意有限代数场仍是非零residue。
* 与259rank3相交仅1：pure module在有限代数扩张后unipotent，mixed quotient标准SL2；actual普通tuple rank9。
* Y(s)order2整数composition的全部N、全部prime powers type；e全0，三nested列b=(1,1,1/2)、u=(1,2,7)，safe τ精确173/81。没有声称该type最优。
* 同holomorphic φ必须省略至少上述两实点；Landau给φ′<11/2，而expτ>exp2>19/3。固定safe9的未精化Theorem7/8入口连λ>τ都不达，停止。

停止仅限**固定9行 + 当前安全e=0类型 + CDT所选holomorphic-map未精化入口**。不移交原14 rank/type/map，不否定其它refined type、convexity修正、允许meromorphic φ的不同criterion，或全体统一框架。另构造更多pure rows/primitive在本子任务范围外；未付完整joint leaf/所有返回支路，不冒称数值4LI。

## 5. 运行、检索与文件边界

数学程序=0；CAS=0；prime/参数/map scans=0；Padé/matrix=0；旧producer=0；Lean=0；数学数值积分/优化=0；归档=0；新PDF/网页GET=0（本子任务），下载字节=0。仅使用已有原件、固定页文本提取、文本全文读取、hash、复制节选、写新260文稿。有限rg仅列本轮literature目录实际文件以定位已有Landau selected primary；不做候选keyword扩张或旧来源去重扫描。

原件FILE整体的hash固定与FULL所选范围分别登记；hash不会把PARTIAL升级成FULL。新数学稿与本scope在本轮已经实际全文读核，原件/节选与数学稿bytes/SHA256由外部receipt刷新；Root另独核数学证书。scope的hash由外部receipt记录，避免自引用。
