# 第259轮 mixed 作者实际读域与执行范围

2026-10-10，对应research/source_selection_mixed12_round259_20261010.md。文件标识mixed12沿用任务名，实际候选level24；只此一个candidate。本人完成覆盖曲面上的完整cusp0 relation-lift，末段另交叉独核同轮field稿的最低场与单关系bare rank3；全部合法解析图和strict预算仍未付，未获实现准入，未证明四项数值LI。

## 1. 实际读域，不继承别人的FULL

|输入|本人实际范围|bytes / SHA256|
|---|---|---|
|literature/manifest_source_admission_round258_20261010.json|PARTIAL：全部头部至new_main、尾部file list；第一次长输出中段截断。只读258边界/clock/禁止窗口，未声称全文数学审阅|40150 / 9d4cc7d8abc31bbbfefb2f04b1696789765bcd135567531f1368bdfa86ea2aca|
|research/research_source_admission_progress_round258_20261010.md|FULL六节、6972 bytes实际读，原258边界保持|6972 / 7dec44c0b57fec181fa39482f1f20c2096c5d0721343621cd2a434aa5d64ae70|
|research/eisenstein_lambert_period_carrier_round218_20261008.md|FULL八节，尤其§6 eq13–17的Mellin contour与conditional kernel。复用已付reciprocity，不计本轮新结果|14236 / 08de641c84b6342a6202d1a671477f8d9e9dbaeea1413a06a840780ec630e7fc|
|research/eisenstein_legendre_catalan_connection_round219_20261008.md|FULL七节；旧FK的准确log²污染，与本轮dyadic源不同|13940 / 67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39|
|research/cdt_odd_level12_paired_coordinate_20261006.md|FULL八节；旧χ12/L3/weight4对照，未把其坐标借给新候选|17353 / 7d4551bd7019f8751ec81e9100484224d5c0cd807b5afe170eee5945e6c85075|
|research/cross_target_strategy_global_round220_20261008.md|PARTIAL：Get-Content首85行，§1–3全部、§4至S6/rank4论证；后续未读|18626 / 93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42|
|research/cdt_mixed_catalan_pi2_geometry_20261007.md|PARTIAL：首75行，§1全部、§2开头；旧arctan/Ti₂来源对照|21079 / 158a2f428d44d37bc717605c52dce2ae097755456757e9dba05ecf52a6997434|
|literature/source_admission_round258_20261010/cdt_reading_scope.md|PARTIAL：首75行，旧primary定位和范围，不继承其FULL标签|旧scope作者的数学阅读不计本人读取|
|literature/cdt2024_l2_chi_minus3.pdf|PARTIAL：固定v2的physical159–163五页全部以新text selection实际读；不是218页整本FULL|4517169 / 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771|
|mixed_cdt_v2_pdf159_163.txt|FULL五页选段已读取；physical160定义，161Lemma11.1.4，162Proposition11.1.8，163 integral remarks|12884 / 2a9ce34c0d0839bd26b1ab7eba2494c53fd0d0e211607d6b5774d249022f1217|
|research/source_selection_mixed_field_round259_20261010.md|FULL F1–F11，独立于该稿作者，先读旧16403后再实际FULL读取最终17525版。交叉核F2–F9全部数学链、F10全prefix和conditional Jensen门槛。τflat一般定义本轮未重读，不声称重证CDT算术定理|17525 / fad9d69a943026d1b6941e9af71b8786cc6643d31007a11ebce0f12df98e0517|

本人本轮读取PDF技能C:/Users/A/.codex/plugins/cache/openai-primary-runtime/pdf/26.1007.11041/skills/pdf/SKILL.md全文，实施只读选段提取；没有创作或编辑PDF。没有声称PDF版式/视觉全页认证。

## 2. 有界去重与primary检索

本地rg固定关键词是mixed12、X0(12)、A3B4、H4、dyadic χ₋₄，以及B4/B_4、A3/A_3、X0(24)、χ₋₄等。初始broad regex和带tag的输出发生截断；不声称完成corpus FULL。随后固定字串X0(24)、A3 B4、A_3B_4、L(2,χ−3),G、θ−3(q)、χ−4(n)q^n、chi_{-4}(n)精确搜索0匹配。对实际匹配到的旧level12与Lambert/Legendre/Catalan混合稿按上表核对象。有限0匹配不证明全球新颖性。

一次web.open调用，三个URL：NIST DLMF25.15#E5、25.4#E2、arXiv2408.15403v2 metadata。本人实际读primitive-character qualifier/25.15.5–6、ζ reflection25.4.2及固定v2 metadata；DLMF整个chapter、Apostol整书、CDT整本均非FULL。没有search_query，没有其它候选检索。

保存mixed_primary_selected_formulas.md为已核公式locator，1105 bytes / fbb42c692ba8a93804d44af7758158122fd1f6924e16c6accbb60bbee3588172。它不是原HTML副本。一次urllib GET DLMF25.15返回HTTP403；无HTML保存、无失败响应数学采用。之前该同一文档命令的PDF extraction成功保存，不重跑/伪称wholepaper。

## 3. 数学与运行范围

本人M1–M15纸面推导：固定滤波精确恒等式、右半平面解析延拓、二维Poisson完整theta transform、q₀ cusp上的全部dual series、共同坏芽、q₀³非零及旧底精确ramification index4、全prefix d_N²。既存CDT Lemma11.1.4用来复用B₃/C₃已有完整坏芽，不把它称为本轮新数值结果。

数学程序/CAS/finite-n numerical/interval：0。参数、素数、映射、word扫描：0。Padé/matrix实现：0。Lean：0。旧producer：0。外仓库访问与外Git写：0。文件hash、读取、primary网页和一次PDF选段属于文档操作。没有归档、改旧稿、main、policy或manifest。本人末段实际FULL交叉读了field稿，精确独核范围见上表；global map成果仍未付。

field交叉独核的补充纸证包括：Euler product E(−q)=E₂³/(E₁E₄)、完整eta divisors确定x₆(s)和h(s)、q₀³强制fielddegree4、ψ真character及精确半平移共轭、全阶整数反演、Bol forcing、negative-weight最大值排除H代数和SL₂不可约证明单关系bare rank3。作者自己提出其中两个rational identities作为核算方向，但field稿全体不是本人撰写；对其余非本人数学链的交叉独核已经明确告知Root。本人mixed M1–M15的独立审阅则由Root完成，不能以本人自读替代。

新数学稿保存后实际全文作者复读；作者自读不是独立审阅。最终pin交给Root后冻结，独立审阅由Root/其它审阅者另记。本文不会将来源首证书与实现准入、严格预算、数值结论混同。
