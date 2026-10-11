# 第228轮 B：新目标筛选的实际阅读/来源范围

2026-10-08。对应 [数学稿](../../research/global_target_selection_round228_20261008.md)。本文是实际 scope；不替 Root/A/C 登记个人 FULL 阅读，也不把 downloaded PDF 全文件视为读完。

## 1. 最新作者原件与实际选页

本轮 fresh 下载 [CDT，The linear independence of 1, ζ(2), and L(2,χ−3)](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)，保存为 packet_cdt_L2chi_current_author.pdf。

- 3628820 bytes，SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c；实际检查220页、PDF可打开。
- PDF元数据 creator=LaTeX with hyperref、producer=pdfTeX-1.40.26、creation/modification=D:20260902051457-05'00'。这只登记元数据，不把它冒称已定位某个 arXiv 修订号。
- 本人实际 FULL 读取物理第3–5页（同印刷3–5页）的完整提取文本，包括 Theorem A 全部 statement、体积与 canonical height 段、Corollary B、跨页 Theorem C 完整 statement、随后 Apéry 比较段。未 FULL 读220页全文；未重新审其数值定理证明。
- 保存 packet_cdt_pdf3_5.txt，11456 bytes，SHA256 67b95e0c01f166cd590f089f26066d90550681266095ade2d08dbba089672976。pdftotext 有 MiKTeX Windows版本提示，但成功产出完整3页文本；该提示不是数学诊断。原提取文件保留 PDF排版产生的控制字节，本轮新数学稿没有复制这些控制字节。
- web.open 同源 PDF 也返回220页并显示相关段落；实际阅读依据另保存的完整 selected text，不将 tool 全PDF索引当作本人 FULL。

旧 literature/cdt2024_l2_chi_minus3.pdf 是218页 arXiv v2，旧稿记录 SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。本轮 fresh current author220页与它明确分开，旧件未改。本轮只核作者原文明确给出的 Q-field theorem与其应用限制；没有从原文提及的更大体积问题推导“单个 Gieseking V 的全球未解证明”。

## 2. 其它 primary 的窄读取

- [Mistiaen arXiv:2512.02612v1](https://arxiv.org/abs/2512.02612v1)：实际读官方题名、作者、提交历史及**完整 abstract**；未读 PDF/正文定理条件。归档 packet_mistiaen_2512_02612v1_abs.html，39013 bytes，SHA2c4a22fad6f97564121dcafaaa8cfc6a51309c457b99f61a4b5ad95480be5f45。摘要是 fixed character 的 growing-weight dimension bound、系数域为 cyclotomic field，并有4∤N的限制；它不能被本稿当作指定 L(2,χ−8) 的判定。
- [Fischler arXiv:1904.02402v1](https://arxiv.org/abs/1904.02402v1)：实际读官方题名、作者、版本及**完整 abstract**；未读全文/证明。归档 packet_fischler_1904_02402v1_abs.html，41950 bytes，SHA99991bae36c0db6e4ad9423759ac8d790004c1c0880afea01b3b155d1463cde8。只登记其 families of L-values/固定 parity 的增长范围，不从摘要冒称任何 singleton theorem 或不存在定理。

这些官方 HTML 是完整下载文件；个人阅读限上述部分。它们不是全文数学审阅收据。不依据媒体或 MathDB 搜索结果认证无理性 status。

## 3. 当前 math 仓库与去重

Root负责 git 更新；本人不运行 fetch/merge。实际 FULL 读 root_repository_state.json 与 root_openai_history_current.md，并在 web 读取固定 current commit 的 history.md。Root收据给出 local HEAD=origin/main=fresh remote main=fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status clean；旧 adc7f1241b42e322a6451854ab7e4b4c146bf78a 只作为更新前身份。

本人实际读取 E:/codex-build/math/CONTENTS.md 的 catalogue005完整发布段，保存 packet_repository_catalogue_005.txt，437 bytes，SHA6a383c843383a5487299b4658a8d6e26f7b9f4d3941bbefab3bea9e3c863090e。该段仍发布 Catalan 无理的声明；不由 catalogue代替 paper/Lean审计，也不称已 FULL读整个CONTENTS或仓库。history解释三篇Hodge/K3稿撤回；不得将这次撤回扩写为其它目标已被证伪。

去重先用 rg。第一次宽检索输出截断，后续定向检索也不等同 FULL历史审阅。实际完整选读：

- research/period_holonomy_target_projection_20261005.md 的开头及§1（到§2前）与§2的定义/首个残数式：明确 trigamma 分类依赖 CDT A，旧固定PDF218页身份不同；不是新全球 theorem。
- research/period_holonomy_dilog_model_20261005.md 的§6开头完整目标/解释段：近单位两log乘积与四项LI是 CDT C转移，不能再次当新独立方法。
- research/cdt_odd_candidates_5_8_12_20261006.md 的开头与§1：其D8指正判别式 χ8 的权3目标，不能误认本轮 χ−8权2。

没有声称 FULL读以上三份旧长稿。没有修改旧 research/main/manifest，也没有复跑它们的 verify程序。检索范围不足以认证全球首次性。

## 4. 本轮数学与完整源的范围

新纸面推导对象是全部 N×N positive Gram M_N(r,s)，r,s从0到N−1；χ−3周期移位矩是全部 L−h_{3(r+s)}。支付完整 off-diagonal、实际 det>0 everyN、线性目标 coefficient、全部素数/prime powers安全整性、Q(√3)两个实际嵌入，以及 Rodrigues/Chebyshev 的自含评价/确切二次率。

Root新研究 global_rank_one_period_gram_cap_round228_20261008.md 已按授权 actual FULL纸审；最终目标身份和小边界修订见独立短收据。不借其作者审阅充作个人文献 FULL。主稿给 full-polynomial scalar clearing 的必要下界，不把 row-denominator safe24当成 optimal full-lattice lower，也不将 finite Gram 模型称为已经付清 CDT fixed-rank function hypothesis。

次选 χ−8 的角色 rational generating function、原生 atan derivative、b′=a/z、全部前缀 d_N²整性均为本轮纸面推导；没有复用 Catalan prime flags、真实period投影或全图能量。另新建 research/chi_minus8_logarithmic_moment_interface_round228_20261008.md：完整partial-fraction周期选择、正Gram、满秩Hilbert coefficient、全部prime powers d16N³上界，以及Cauchy determinant给出的e^{O(N)}归一化误差，全部为纸面证明。Root另提出 p∈(8N,16N)的明确结构窗口，本人独立核完整support/anti-triangular block/唯一最深coefficient，支付 valuation−q 与 Σqlogp=4N²+o(N²)；这不是执行素数扫描。必要4不来自安全48，限完整polynomial scalar-clearing，已阻止这套integrated Gram继续次主阶 primitive高度计划。没有排除另一源/关系点另付cancellation。下一证书 (S14) 是 N²分支的充分待证命题，不是所有新路线的必要门槛；真正mixed/CDT能量接口也未满足，不宣称新的数值无理性。

数学执行次数 **0**。本轮 Python只读取 PDF元数据/文件hash；pdftotext只提取文献；rg、文件下载、复制、读写/hash不是数学程序。未做 prime/参数扫描、CAS、PSLQ、recurrence guessing 或 archive程序重跑。最后会 actual FULL复读本轮保存的数学稿、scope及短review，登记bytes/SHA，不把摘要HTML下载冒称全文阅读。
