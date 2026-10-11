# 第258轮 CDT 子任务：本人原文读域、执行范围与 pins

2026-10-10。对应 [数学稿](source_admission_cdt_round258_20261010.md)。本 scope 只声明本人本轮确实读取的范围，不继承其它稿的 FULL 标记，也不把 PDF extraction 等同于完整原文阅读。结论为 fixed level14 source duplicate-rejected；不准入实现，不重开同源续窗。

## 1. 原始源及版本 pins

|本地文件（literature/ 下）|页数|SHA256|版本/可靠定位|
|---|---:|---|---|
|cdt2024_l2_chi_minus3.pdf|218|84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771|arXiv2408.15403v2，2024-09-16；本稿固定源|
|cdt2026_effective_holonomy_author_20261006.pdf|20|368cc0af5584049a76c7cef0fd78886524143ee3935f56cfc2e35fb9bee22796|作者 ICM 稿，另核 arXiv2510.04156v1|
|zagier2009_apery_like_recurrences.pdf|15|9fe93aadda4a5dc0297c7b5d835d8c3026ebf026f5dc139eefc0ff7856f4fc97|Zagier 作者原始 PDF|
|beukers1987_modular_irrationality.pdf|14|fc28f8db316015fb349a47cf456e3037bb8fdabc3e92914eaad12e3f68176c38|Astérisque147–148，pp271–283，原始 archive|
|source_admission_round258_20261010/cdt_colo2022_thesis_primary.pdf|281|90264d1d1eb5e6da8fc9f6bb555e73db37840a063bd4ecf3e5b1f3e77269559d|Colò Aix-Marseille PhD，2022-11-18，官方 theses.fr 原文，本轮新增|

在线 primary locators：

- CDT fixed metadata：[arXiv2408.15403v2](https://arxiv.org/abs/2408.15403v2)。作者当前 [L2chi.pdf](https://www.math.uchicago.edu/~fcale/papers/L2chi.pdf) 是220页，此次仅核版本差异，不把其页码混入固定v2。
- ICM：[arXiv2510.04156v1](https://arxiv.org/abs/2510.04156v1)，[作者 ICM.pdf](https://math.uchicago.edu/~fcale/papers/ICM.pdf)。
- Zagier：[作者 PDF](https://people.mpim-bonn.mpg.de/zagier/files/tex/AperylikeRecEqs/fulltext.pdf)。
- Beukers：[原始 archive](https://geodesic.mathdoc.fr/book-part/AST_1987__147-148__271_0/)，archive 的 Numdam 扫描入口。
- Colò：[官方博士论文全文](https://theses.fr/2022AIXM0580.pdf)。下载 3653838 bytes，PDF signature 与281页已核。

Donnelly 的 UGA getd/openscholar 原文入口发生403/redirect或返回HTML，本轮没有保存其内容、没有以它支持任何数学断言。搜索结果中的非 primary 项未作为证明来源。上述是有限检索，不宣称穷尽或全球新颖性。

## 2. CDT 固定v2的实际阅读

物理页=印刷页。定位先使用 `rg --files` 及 `period_holonomy_reading_map_20261005.md`、`cdt_odd_reading_map_20261005.md`。旧 reading map 只当 locator，不继承 FULL 标签。

|对象|本人本轮读域|用于哪项结论|边界|
|---|---|---|---|
|§11，pp159–165|完整关键 section：§11.1、§11.2|x/eta、实际A/B/C、ODE、两积分、关系延拓、symmetrization|完整 section，固定 v2|
|§12，pp165–171|完整关键 section：§12.0、§12.1|七纯函数、返回支路、14独立函数、Frobenius界及 false integral choice|未以有限头替代原文证明|
|§13，pp171–173|完整 section|14×2 array、六积分、shift、τ与strict闭合|不移交 χ−7|
|§10，pp153–158|读取具体definitions、Lemma10.2.2与相关 denominator discussion|B1–B7具体函数及安全types|不另宣称本文完成其全部背景理论|
|§9，pp146–150|definitions、Theorem/Corollary9.0.19及其适用域|univalent leaf、filled singularities的合法性|pp151–153亦extract，长输出局部截断；不宣称§9全proof FULL|
|§7，pp89–90|Theorem7.0.1及其紧随解释完整|strict numerator/denominator及原 standing assumptions|不宣称§7全部proof或§6 standing assumptions已重证|
|Appendix A，pp203–205|LemmaA.4.4及A.5.1完整关键段|唯一小原像、ψ′的exact fraction、strict13.9938<14|pp199–206extract，不宣称全部Appendix A FULL或运行其energy程序|
|pp1–10、29–34|metadata、引言与机制相关选段|校准数值结论、论文身份和早期机制说明|非整本FULL|

保存的文本均在 `literature/source_admission_round258_20261010/`，文件名前缀 `cdt_`：

- cdt_fixed_v2_pdf01_10.txt、cdt_fixed_v2_pdf29_34.txt。
- cdt_fixed_v2_pdf153_174.txt；重复窄窗 cdt_fixed_v2_pdf166_169.txt。
- cdt_fixed_v2_pdf146_153.txt、cdt_fixed_v2_pdf89_92.txt、cdt_fixed_v2_pdf199_206.txt。

渲染保存 cdt_fixed_v2_pdf161.png、162.png、163.png、172.png、205.png；其中161由 view_image 逐页视觉核 normalization/period行。未声称其余图片已逐张视觉看过；对应数学信息来自已读原始text。保存图片不是计算新值。

## 3. 其它原始文献的读取边界

- Zagier：`cdt_zagier2009_pdf05_12.txt`，实际读取 §5 的 pp9–10 与 §6 的 pp10–12，核 primitive/Eichler 与案例 A/C。没有15页整本 FULL 声明。
- Beukers：`cdt_beukers1987_pdf01_08.txt`，实际读取 §1 Proposition1.1/1.2，物理2–4/印刷271–273 的完整关键段，核 modular Apéry limit interface。没有14页整本 FULL 声明。
- ICM：`cdt_icm_author_pdf01_08.txt`，实际读取 §2.1/Theorem2.1 与 §2.2 的定量接口；一般 arithmetic holonomy 仍要求实际 tuple/period 数据。长proof输出截断，未声称20页整本 FULL。
- Colò：`cdt_colo2022_pdf081_083.txt`，完整读取物理82/印刷64页的 X0(14) eta model 及相邻§2.3.1语境；83页的 finite-field 后续example不用于结论。`cdt_colo2022_pdf039_040.txt` 读取§1.3.5物理39/印刷21的genus formula，不宣称40页全部FULL。`cdt_colo2022_pdf082.png` 经 view_image 整页视觉独核。281页整本未读。
- OpenAI double-deletion source：实际读取 `openai_dd_full_source_20261007/sections/07-holonomy.tex` 整section及 paper.tex metadata；发现其为2026-09-23 *The Deligne–Drinfeld conjecture*，不是CDT。只用于排除混名，不把 KZ/depth-one 非零作为本轮 numerical source。

PDF reading skill 实际读取自 `C:/Users/A/.codex/plugins/cache/openai-primary-runtime/pdf/26.1007.11041/skills/pdf/SKILL.md`。采取文本提取+必要公式页视觉核；没有创作或修改PDF。

## 4. 旧247–248资产的本轮去重核读

下列本人本轮重新读取，不继承旧FULL标签；其数学资产仍归旧轮，未称本轮首次支付。

|research/ 文件|本人本轮读域|
|---|---|
|research_global_review_round248_20261010.md|全文重新读取|
|research_round247_dyadic_source_review_20261010.md|全文重新读取|
|dyadic_chi7_eisenstein_source_round247_20261010.md|全文D1–D14重新读取|
|dyadic_field_lift_energy_gate_round248_20261010.md|全文F1–F11重新读取|
|dyadic_elliptic_uniform_cap_round248_20261010.md|全文七section重新读取|
|chi7_dyadic_two_period_source_round247_20261010.md|首次长输出截断后再完整窄读，全篇D1–D16及结尾均重新读取|
|dirichlet_chi7_eisenstein_source_round246_20261010.md|首135行，E1–E10相关定义；只用A0 normalization/旧locator，不宣称全文|
|period_holonomy_cdt_mechanism_20261005.md|先前机制笔记读取作locator；原证明以本轮固定v2为准|

核心 exact去重为 B7=R_old、C7=D_old、H258=(A7/A0)H_old、同完整域 F=Q(X0(14))。T不属于Q(u)的pole-fiber证明不撤销“同源”结论。新底未支付cyclicrank与denominator预算，不能继承旧m=5、τ=32/25；已付 normalized Abel cap<20及三整数场行确可移交。

## 5. 数学程序精确次数与范围

数学 CAS 共 **3次实际 Python/SymPy 进程**。会话唯一ID `01a1231d-2e91-7603-ac9f-c27f98192658`，UTC时间如下（本地Asia/Shanghai加8小时）：

|序号|UTC tool时间|具体操作|
|---:|---|---|
|1|2026-10-10 00:05:19.632|固定 z=27x²(1−x)/(1−3x)³ 的HG拉回；C1/C0两残差、1−z及m(1/9)，单一公式|
|2|2026-10-10 00:12:09.138|固定E上T=x/y的critical polynomial、单一cubic消元与discriminant、δ7代值和critical numerator|
|3|2026-10-10 00:13:18.480|同固定公式复核；F7分子/界恒等式；branch cubic discriminant、δ7 fiber；保存JSON和五原文hash/pages|

第3次保存 `cdt_exact_initial_certificate.json`，是固定 rational identities 和 source pins，**不是** analytic jump/rank/Padé/holonomy准入证书。model的Δ值为exact algebra scalar；证明见数学稿。新底完整坏芽尚未核证，不填假成功项。

为避免压缩上下文导致假“数学程序0”，另用标准 Python JSON读取器审计**本人**会话原始 tool call；恢复上述三个实际含SymPy import的进程。先按本人agentpath定位session元数据，不把其它聊天文本作为证据；该日志读取没有执行 CAS，只输出本人固定公式命令与本scope所列元数据。PDF文本提取/渲染、primary下载、hash和日志计数属于文献/账本操作，不算数学程序。

未做：参数/character/prime/map扫描；旧 producer；Lean；Padé；real-energy或critical-map数值优化；整数relation搜索；实现或bench；main/policy/manifest/git mutation。先后只有这一个 χ−7 comparison carrier，没有隐含候选池。

## 6. 写入范围与最后检查

本子任务只新增/维护：

- `research/source_admission_cdt_round258_20261010.md`。
- `research/source_admission_cdt_round258_reading_scope_20261010.md`。
- `literature/source_admission_round258_20261010/cdt_*` 专属文件。

第257及更早主稿不改；没有修改其它 agent 文稿、policy或manifest。数学稿、scope及更新JSON已由本人完整重读，无截断；两处格式/账本措辞随后修正并复核，终版 SHA256 另回报Root再次全文独核。Root 的归档/冻结状态不由此scope代替。最终结论：重复源拒绝，不重开同源χ−7，不自动开启任何实现，不在无新具体机制时硬指定下一目标/参数。
