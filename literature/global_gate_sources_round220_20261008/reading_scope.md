# 第220轮文献与实际阅读范围

2026-10-08。来源 PDF 的精确身份见 [download_receipt.json](download_receipt.json)，研究主结论见[全局复盘](../../research/research_global_review_round220_20261008.md)。本账本分别记录下载、选读、完整研究稿审阅；不把全文下载或全文文本搜索称为 FULL 文献阅读。

## 1. 新增八份 primary PDF

八次 PDF 下载均成功；没有失败下载未报。下载由 Root 执行，只作归档/版本验证。文献内容的实际阅读另列如下。

|归档|精确来源|本轮实际内容阅读|
|---|---|---|
|[Hain](hain2015_hodge_derham_modular_arxiv1403_6443v3.pdf)|https://arxiv.org/pdf/1403.6443v3|接口稿作者选读 §13.2–13.3、18.3–18.4及 §9 的 elliptic cohomology framing/tangent-basepoint comparison；§9 是 M1,1 上的框架，未识别本实际 Legendre 模型的 canonical 比较。另读 v2 HTML Theorem8.1–8.2，两版本不混为同一阅读。Root 新增阅读仅 arXiv metadata，未 FULL 全文。|
|[BFNP](brosnan_etal2008_normal_functions_arxiv0711_0964v2.pdf)|https://arxiv.org/pdf/0711.0964v2|接口稿作者选读 intro 中定义段落、§2.5、Fact2.6、Lemma2.8、Corollary2.9、Theorem2.11；未 FULL 读取 intro。Root 只作 arXiv metadata/归档。|
|[Wildeshaus](wildeshaus2000_elliptic_symbols_arxiv_math_0006170v1.pdf)|https://arxiv.org/pdf/math/0006170v1|接口稿作者选读 intro 及 symbol/differential/residue 段落。Root abs 入口 cache miss，不称其已读；实际 PDF 成功归档。|
|[Fischler–Rivoal](fischler_rivoal2016_G_denominators_arxiv1606_00706v1.pdf)|https://arxiv.org/pdf/1606.00706v1|实处稿作者及独审选读第1页 G-function 定义(i)–(iii)。Root metadata/归档，无 FULL 全文。|
|[McMullen](mcmullen2010_complex_analysis_course_author.pdf)|https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/10/html/home/course/course.pdf|实处稿作者及独审读取 printed page64 的完整 Theorem4.20及证明。Root 归档，无 FULL 全文。|
|[DG 91页作者稿](deligne_goncharov2005_Tate_author_91pages.pdf)|https://www.math.ias.edu/files/deligne/Tate.pdf|跨目标稿作者及独审读取 §5.1–5.2及相邻路径/比较段落。Root 页数/哈希归档，无 FULL 全文。|
|[Brown–Hain](brown_hain2017_weakly_holomorphic_arxiv1708_00652.pdf)|https://arxiv.org/pdf/1708.00652|跨目标稿作者及独审选读 intro Theorem1.2、Corollary1.3–1.4及 Proposition2.2/Bol proof；独审用途限比较与 level1 范围。Root 页数/哈希归档，无 FULL 全文。|
|[MMV 49页作者稿](brown_multiple_modular_values_author_49pages.pdf)|https://www.ihes.fr/~brown/MMVarchiveV1.pdf|跨目标稿作者及独审读取 §7.3 Lemma7.1、(7.3)及 coboundary 解释。Root 页数/哈希归档，无 FULL 全文。|

作者或独审者的选读是相应 agent 实际执行的记录，不升级为 Root 本人 FULL 读过这些论文。对 normal function、regulator 的后续几何实现没有完成 theorem-level 全链审计；本轮只将它们作为可选更强接口，直接 CDT 不要求它们。

## 2. 复用精确文献

- [CDT 主文固定PDF](../cdt2024_l2_chi_minus3.pdf)：218页，4517169 bytes，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。Root 本轮实际 FULL 读取 PDF页16–18、66–70、193–195。实处稿作者、跨目标作者/独审还核 Theorem7.0.1；接口作者/障碍独审的实际页段记录在其稿/收据，不声称整篇 FULL。细类型定义、literal n 费用和直接定理条件分别核对。
- [CDT 短稿](../cdt2025_arithmetic_holonomy.pdf)：20页，751610 bytes，SHA256 `5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1`；arXiv2510.04156v1。Root 本轮实际 FULL 读取 PDF页1–4；接口作者与障碍独审读取1–6。没有 FULL 20页。
- [CDT effective holonomy 作者稿](../cdt2026_effective_holonomy_author_20261006.pdf)：20页，657333 bytes，SHA256 `368cc0af5584049a76c7cef0fd78886524143ee3935f56cfc2e35fb9bee22796`。Root 本轮只读首页及 metadata，没有 FULL 全文。
- [Brown Annals](../brown2012_mixed_tate_motives.pdf)：28页，513320 bytes，SHA256 `ed36eadb1cdf8150405e9cfa9437caa8a8d88841258d936c6347d1e5877f1085`；来源 https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf 。跨目标作者及独审选读 intro Theorem1.1/Corollary1.2、§2.2 Definition2.1/Remark2.2；Root 仅首页部分文本及版本核验。
- [DG 发表稿](../deligne_goncharov2005_mixed_tate.pdf)：56页，570075 bytes，SHA256 `d6dd951cc307370cb31dfa7a2b02cef07527bf70580d97811e96cb36fcd89ff4`。Root 首页部分文本及版本核验。跨目标稿本轮选读的91页作者稿另存，页码不借用此56页版本。
- DLMF theta、lambda、elliptic 归一化复用219已付的明确公式/版本。本轮未重新下载，也没有新 FULL 全章阅读。实际 lambda 导数与 factor2 已按冻结连接式独立纸面核验。

## 3. OpenAI 仓库及目标状态的边界

Root 本轮仅从 [历史 Catalan PDF](../openai_math_2026_special_values_20261007/openai2026_catalans_constant_irrational_20260924.pdf) 读取首页及 metadata：44页，574388 bytes，SHA256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`。该论文声称 G 无理。本轮没有重新 FULL 审44页、重跑有限证书或编译 Lean。

Root 本轮实际 FULL 读取 [历史 reading manifest](../openai_math_2026_special_values_20261007/reading_analysis_manifest_20261007.json)：3602 bytes，SHA256 `77a837a37ecc478e5e3d6907760fc2bc5f02531c2a8cce6e3744d523d6e5e331`。它记录指定快照 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的既有静态审查，以及未重新机器验证的范围；其 old_research_goal_status 不控制当前 active 目标。本轮没有 Git 或新的全仓调查，也不将历史有界未发现声明解释为最新仓库的穷尽结果。

另有本轮 bounded web 搜索定位 arXiv2605.01830 与 Li2Rational 仓库 README 片段；没有完整读取其 theorem/proof，没有引入其结论。搜索没有命中某个 β(4) 或 Ti₂(1/2) 结果，不构成这些问题未解或新颖性的证明。本轮未报告这些目标的新数值结论。

## 4. 完整研究稿审阅与执行

本轮新增四份数学稿（目标关系障碍、实处零估计、周期/holonomy、跨目标策略），各作者保存后实际 FULL 复读；另外一位 agent/Root 作独立 FULL 审阅。Root 亦实际 FULL 阅读四份稿及四份独审收据。具体身份、角色和最终报告独审收据由本轮 manifest 固定。

全文下载8次；数学程序、CAS、矩阵执行、数值积分、素数/参数扫描、PSLQ、Lean、Git均为零。证明和独审为有限纸面推导，Python只用于 PDF metadata/选页文本、文档、下载和哈希。没有冒称文献下载即数学程序执行或定理验证。本账本保存后 Root 实际 FULL 复读，最终身份由 manifest 登记。
