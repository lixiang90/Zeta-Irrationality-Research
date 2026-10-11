# 第258轮 cyclotomic 候选：实际阅读和执行范围

2026-10-10。执行身份 `source258_cyclotomic`。本文是本身份的 scope，不继承其他作者的 FULL 或独审标签。

## 1. 本轮 NEW primary sources

| 本轮新保存路径 | 原始URL | Bytes | SHA256 | 实际阅读范围 |
|---|---|---:|---|---|
| `cyclotomic_hain_classical_polylogarithms_1992.pdf` | https://arxiv.org/pdf/alg-geom/9202022 | 342785 | `9E1287AE90DF7ACD877801B88DDC02BBB87195182C7389060F73644C0F7095BE` | PARTIAL：web PDF文本 §2，Propositions 2.1–2.2 的公式、正向绕0/1的继续、归纳积分证明；实际相关显示为 PDF页索引3–6（印刷页4–7），web文本行218–438。find结果还显示 §3 的 single-valued real-analytic 说明和其它搜索命中，未作为本稿的证明输入。未宣称FULL。 |
| `cyclotomic_perez_marco_monodromies.pdf` | https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/enemonodromy11.pdf | 366940 | `FAF179B0EAD39005689E05B1403B5D54C9C4732196969F5755BC19ED915EBE12` | PARTIAL：web PDF文本 Definition1.1–1.4/Prop1.3（PDF页索引3，印刷页4，行162–196）；§6.1 Cor6.1及其证明（PDF页索引18，印刷页19，行1344–1413）；find的邻近公式有显示但未借作新论证。未宣称FULL。 |

两份PDF由直接 primary URL 的 Invoke-WebRequest 新建保存，工具实测 bytes/hash 如上，不覆盖旧路径。Hain arXiv页面和初始web搜索仅用于定位与题名核验。没有把下载整份PDF、find命中或hash当成全文阅读。

DLMF §25.12（https://dlmf.nist.gov/25.12）的搜索返回实际显示 Li₂ 的定义/积分/branchpoint、一般 Li_s 级数和部分公式。它仅作入口校验；本稿的主要文献交叉核验采用上述两份作者primary论文，端点公式及monodromy/函数rank均另给自足证明。没有依赖搜索返回对 Li_n endpoint 的数值无理性结论。

## 2. 旧本地材料：精确 PARTIAL 边界

定位使用 `rg --files` 仅列文件名，不算正文阅读。检查了 `E:\AGENTS.md`、`E:\kimi-build\AGENTS.md`、workspace根、research和literature的 `AGENTS.md`；这些精确路径均不存在。

实际一次 `Get-Content -TotalCount 100` 请求读取下列三份旧稿；合并工具输出随后有截断，所以本scope统一只记 PARTIAL，不领取FULL标签。第一份的前100行和第二份的正文在可见输出中用于概念口径核验；第三份的准入文字另行在无截断调用中重新读取行91–101。实际结论只依赖这些有限范围，未用hash代替读正文。

| 旧稿 | 实测Bytes | 实测SHA256 | 采用范围/用途 |
|---|---:|---|---|
| `research/cyclotomic_symmetry_analytic_round221_20261008.md` | 16171 | `BA26CAB8550AAFC5EA1CF177C50A1F302E415E2CB9B1265305592D17DEE55AA0` | PARTIAL 前100行请求及可见正文：真实初始branches、完整背景、foreign leaf与rank的口径。未读取后续完整共同图证明。 |
| `research/cyclotomic_relation_differential_projection_round221_20261008.md` | 5368 | `9586ADB394CF371588E204077EDA32DDC129E4066A85711FC44F0522AB80C03F` | PARTIAL 前100行请求及可见正文：局部单值化、微分最小性和“删方向即删目标机制”的界限。即使该短稿在请求中可能已完整返回，也不申请本次FULL标签。 |
| `research/research_round257_net_feasibility_review_20261010.md` | 10535 | `7CF4076D6244197DEEBE372F0ACF8070324F2988B42B3353F8188E397F64499D` | PARTIAL：前100行请求有合并截断；本次重新无截断实际读行91–101，用其第258轮有界来源准入/执行界限。未本身份独审257数学链。 |

这三份是本身份读取时的当前文件身份，不继承它们内部记载的其它旧稿阅读、归档、证书或独审。

## 3. 新稿的数学和执行范围

新正文：`research/source_admission_cyclotomic_round258_20261010.md`。

- 固定两个不同 cyclotomic channels及全部真实共轭、s=2 endpoint lift、四branchpoint局部盘和principal共同域。
- 自证局部完整log分解、四support隔离、顶权meromorphic系数消支的必要充分条件、端点零关系不蕴涵函数关系。
- 自证整数s≥2的 log超越性、最小有理微分族rank1+4s，明确 endpoint/monodromy/derivative/联合closure不同rank。
- 只否决固定来源在指定branchpoints的全消支准入；无新数值ζ/L无理性、无全球cyclotomic/CDT no-go。

数学程序、CAS、finite-n/interval计算、PSLQ、Padé/prime/参数/map/word扫描、Lean、旧producer和外Git写均0。工具仅本地定位/读取/文件身份、web primary检索和新PDF下载、允许文档保存及复读。文档hash不计为数学程序。未改main、policy、manifest或任何旧文件；未运行archive或创建新thread。下一窗口不自动续。

作者保存后的全文复读仅为作者自审，不称独立审核。本稿身份和最终复读收据将向Root单独报告，避免scope自引用hash。
