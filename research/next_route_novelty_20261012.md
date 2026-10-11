# 下一路线的新颖性审查：ζ(2) ± 2G

审查日期：2026-10-12。这里 $G=\beta(2)=L(2,\chi_{-4})$，令 $\alpha_+=\zeta(2)+2G$、$\alpha_-=\zeta(2)-2G$。本轮只核一手文献的陈述、适用条件和相关构造；没有复核所有证明、运行数学搜索或重新构建 Lean。

**判断：在下列实际核读的一手来源中，没有找到直接证明某个指定 $\alpha_\pm$ 无理，或同时证明两者无理的适用定理。两者可以保留为进一步核查的具体数值目标，但尚不能据此宣称它们是已确认的开放问题，也不能仅凭新颖性检索便批准实现一条研究路线。** 若后续能证明每个指定符号的无理性，结果不会被本次核读的 CDT 定理、单独 $G$ 的无理性陈述或 $L$ 值家族定理直接覆盖。

## 1. 先固定所需量词

由 $\alpha_++\alpha_-=2\zeta(2)=\pi^2/3$，两者**至少一个无理**已经是初等推论；这个结论不能算新出口。这里真正要审查的是“$\alpha_+$ 无理”与“$\alpha_-$ 无理”这两个分别指定常数的命题。

即便接受单独 $G$ 无理的证明，仍不能推出上述任一命题。例如，假设 $\alpha_+=r\in\mathbb Q$，则

$$
G=\frac r2-\frac{\zeta(2)}2=\frac r2-\frac{\pi^2}{12};
$$

这个表达式恰使 $G$ 超越，完全与 $G$ 无理相容。负号同理。因而必须排除**含任意有理常数项的仿射关系**，不能只引用两个常数各自无理，也不能只排除 $G/\pi^2\in\mathbb Q$。后一个齐次结论仍容许非零有理常数项的关系。

直接分拆定义级数可得

$$
A:=\zeta(2,1/4)=\pi^2+8G,\qquad
B:=\zeta(2,3/4)=\pi^2-8G,
$$
$$
\alpha_+=\frac{5A-B}{24},\qquad
\alpha_-=\frac{-A+5B}{24}.
$$

所以目标也不是简单引用“某个四分点 trigamma 值无理”。$1,A,B$ 的 $\mathbb Q$ 线性无关是充分的更强结论；证明两个指定组合分别无理则只排除两类特定关系，不能反过来宣称已证明整个三维空间线性无关。上述判断与公式是本次审查的逻辑推导，不冒充文献中的新定理。

## 2. CDT 最新版本：导子 3 的结论不能换成导子 4

截至审查日，[arXiv:2408.15403 的版本记录](https://arxiv.org/abs/2408.15403)仍只有 v1 和 **v2（2024-09-16，218 页）**。同时核看了作者网站当日可访问的 [220 页 PDF](https://www.math.uchicago.edu/~fcale/papers/L2chi.pdf)；它与 arXiv 的固定版本须分开标识，页数差异不意味着 arXiv 出现了新的版本。

固定 [v2 PDF](https://arxiv.org/pdf/2408.15403v2) 的 **Theorem A，印刷第 3 页**证明 $1,\pi^2,L(2,\chi_{-3})$ 在 $\mathbb Q$ 上线性无关。**Corollary B，第 4 页**覆盖 $\psi_1(n/6)$，其分拆使用的是 $\chi_{-3}$。这些结论中的字符、导子和分点都不能替换为 $\chi_{-4}$、四分点或 $\alpha_\pm$。作者网站版本的上述两个陈述也没有改变这一适用范围。

此外，**Remark 11.1.17，v2 第 163–164 页**明确讨论了两类传统 Catalan 逼近及它们的分母障碍；作者网站版本的对应讨论从第 165 页开始。它只说明该方法沿那两类特定逼近尚需新想法，既不是本目标的无理性定理，也不是全部 Catalan 路线的不可能性证明。不能因论文出现 $G$ 或 Catalan 逼近，就把 Theorem A 的结论扩充到 $G$。[具体讨论](https://arxiv.org/pdf/2408.15403v2#page=163)

## 3. 项目相关文献逐项核对

以下列出本轮实际核读的定理陈述与必要上下文，不表示已独立验证相应全篇证明。

| 一手来源与具体定位 | 已陈述的成果 | 对 $\alpha_\pm$ 的限制 |
|---|---|---|
| [OpenAI，2026-09-24 原仓库论文](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)，Theorem 1.1；[当前引言原稿](https://raw.githubusercontent.com/openai/math/main/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/introduction.tex) | 单个 $G$ 无理。原仓库 [Lean 说明 005](https://raw.githubusercontent.com/openai/math/main/lean/docs/005.md)的目标也为 $G$ 无理。 | 不是 $1,\zeta(2),G$ 线性无关定理，也没有陈述两个指定组合无理。本轮不声称重新完成其 Lean 或全部证书验证。 |
| [Sun，2609.04176v1](https://arxiv.org/abs/2609.04176v1)，Theorem 1.1；[Wachs，2609.22339v1](https://arxiv.org/html/2609.22339v1)，§3.4、Corollary 3.5 | Sun 声称 $G$ 无理；当前 arXiv 记录仍为 v1。Wachs 指出其所展示的分母与渐近账本未证明所需估计，结论为该证明不完整。 | Sun 的陈述本来也只涉及 $G$。这份具体批评不判断 $G$ 的真假，且不能转嫁为对后来 OpenAI 论文的反驳。 |
| [Lai–Zhou，2103.00904v2](https://arxiv.org/pdf/2103.00904v2#page=12)，Theorem 6.1，第 12 页 | $\beta(2),\beta(4),\beta(6),\beta(8),\beta(10)$ 中至少一个无理。 | 存在性量词不能指定 $\beta(2)$，更不能指定 $\zeta(2)\pm2\beta(2)$。 |
| [Fischler，1904.02402v1](https://arxiv.org/pdf/1904.02402v1#page=3)，Theorems 1–2、Corollary 1，第 3 页 | 周期系数 $L(f,s)$ 家族随上界增大有维数下界，并有多个值不落入任意固定有限维 $\mathbb Q$ 空间。 | 虽然 $f(n)=1\pm2\chi_{-4}(n)$ 给出 $L(f,2)=\alpha_\pm$，定理的大参数家族结论仍不指定 $s=2$。 |
| [Lai–Li，2505.12687v2](https://arxiv.org/html/2505.12687v2#S1)，§1、Theorem 1.5（2026-04-09） | 固定 $k\ge2$，奇部分 Chowla–Milnor 空间的维数随 $q\to\infty$ 至少按 $(1/\log2-o(1))\log q$ 增长。 | 不能把渐近结论代入固定 $q=4$。§1 的其他情形“开放”表述是作者当时的认识，不作为 2026-10-12 穷尽检索的证书。 |
| [Gun–Kandhil–Philippon，2212.00366v1](https://arxiv.org/pdf/2212.00366v1#page=2)，Theorem 4，第 2 页 | 同奇偶性的偶字符、偶权 $L$ 值与 $\zeta(2k)$ 的独立性结论。 | $\chi_{-4}(-1)=-1$，在权 2 属相反奇偶性，不能加入该定理的偶字符集合。 |
| [Mistiaen，2512.02612v1](https://arxiv.org/html/2512.02612v1)，Théorème 1.0.5、Remarque 3 | 在 $4\nmid N$ 等条件下给出大权范围的 $L$ 值维数下界。 | Remarque 3 明确排除导子 4 的 Dirichlet beta 情形；仍非指定权 2 的结论。 |
| [Eskandari–Murty–Nemoto，2510.20648v3](https://arxiv.org/html/2510.20648v3)，Theorem 1.1.1、§6（2026-08-29） | 构造 Catalan 动机，并在对称性、整除条件下给出 $1,G$ 的有理线性形式。 | 周期矩阵含 $\pi^2 i$ 是结构信息；没有据此陈述实数 $1,\pi^2,G$ 的数值线性无关定理。 |
| [Eskandari，2609.26354v1](https://arxiv.org/html/2609.26354v1#S1)，Theorem 1.1 | 有效构造 $0<|G-p_n/q_n|\le q_n^{-0.62}$ 的逼近。 | 此小于 1 的误差指数本身不足以使清分母后的整数形式趋零，更没有给混合目标。 |
| [CDT，2510.04156v1](https://arxiv.org/html/2510.04156v1#S5.SS2)，§5.2、脚注 2、式 (5.10)–(5.11) | 解释相关实周期恒等式含额外 $\pi^2$ 项，而对应 2-adic 恒等式没有该项。 | 2-adic Catalan 或 $\zeta_2(5)$ 的无理性不能替代这两个实组合的结论。 |
| [Viola–Zudilin，MPIM 14-26](https://archive.mpim-bonn.mpg.de/1914/1/preprint_2014_26.pdf#page=7)，Main theorem，印刷第 3 页 | 对特定实有理参数给出 $1,\operatorname{Li}_1(1/z),\operatorname{Li}_2(1/z),\operatorname{Li}_2(1/(1-z))$ 的独立性。 | 参数条件不允许把实有理点换成 $i$，所以不能借 $\operatorname{Li}_2(i)$ 含 $G$ 的恒等式转用结论。 |

OpenAI 构造的适用范围值得特别注意。[当前 foundations 原稿的 “Moment evaluation and cancellation” 小节](https://raw.githubusercontent.com/openai/math/main/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex)先将矩写成 $1,G,\zeta(2)$ 的组合，再以接触条件消掉 $\zeta(2)$。因此在反证假设 $G\in\mathbb Q$ 下得到有理行列式。改成 $\alpha_\pm\in\mathbb Q$ 不会让既有行列式自动有理；必须重新设计消去条件，并重新证明整数性、非零性与两端估计。这是一个可探究的改造问题，不是现成定理的直接推论。

## 4. 作为项目下一出口的价值与准入条件

按[第 261 轮 gate](refined_budget_gate_round261_20261010.md)采用的真实周期归一化

$$
a+\frac b2 L(2,\chi_{-3})+\frac c4\zeta(2)+\frac d2G,
$$

两个目标的完整反证关系分别是 $b=0,c=d\ne0$ 与 $b=0,c=-d\ne0$。它们确实全部落在该轮 **AP 过滤前缀分母 leading rate 为 $4/3$** 的特殊范围中。这比试图覆盖整个四项关系空间更贴合已有资产：有明确常数、明确系数类和明确待补定理，值得保留为候选。

这一段只回顾第 261 轮背景：“前缀分母改进”还不是 CDT balanced-height 的 $\tau$；在当时未精化式及两种已审凸性精化下，rank 3 严格矛盾仍必要 $\tau<7/6$。该轮没有证明 $32/27$ 是新费用。**当前裁决应以第 262 轮的两个新证书为准。**

[本轮 AP 费用稿](next_route_ap_cost_20261012.md)另定义了保留 balanced labels、近均匀次数及逐行标量前缀分母的 cap，并证明其最优基底费用恰为 $32/27$。这不是已经适用的新 holonomy 定理，也不是实际联合评价整数格的最小分母费用。[双穿孔覆盖稿](next_route_cover_bound_20261012.md)对同一载体的全部合法全纯图给出 $\lambda<\log3<10/9$；因此即便将来把原 $\lambda-\tau$ 接口推广到这个自然 cap，仍有

$$
\lambda-\frac{32}{27}<-\frac{2}{27}<0.
$$

AP 稿还按真实 coefficient index $n-k$ 核了合法辅助索引排列；仅将这一分布加入标量前缀 cap，其费用下界仍为 $8/9$。这个下界不能单独关闭正分母，却已与所选 rank 3 BC 接口的必要条件 $\lambda>3\tau/2\ge4/3$ 冲突。不能把 cap 的下界转写成所有 actual coefficient 或所有 AP 整数格的下界。

[无穷远芽证书](next_route_carrier_20261012.md)又对这两个目标完整反证类所共有的 $c\ne0$ 证明：合法亚纯地图没有极点，故不能以允许旧坐标地图有极点绕过上述界。这里不包括 $c=0$ 的其他关系或不同载体。

因此当前应**停止自然 AP 标量前缀模型，以及仅增加辅助 $k$ 分布的同类 cap 在此载体上的实现投入**。两个指定组合仍是值得保留的具体数值目标；这份新颖性审查没有为上述已失败模型续发准入。重开需要改变实际评价整数格费用、完整强制坏芽或已陈述解析接口的真实机制。任何候选仍须覆盖选定符号的**所有有理反证常数项**；再次获得 $4/3$ 的 leading rate、证明“两者至少一个无理”、或重述单独 $G$ 无理，都不能替代这一要求。

## 5. 检索边界与可更新记录

本轮联网核查了上述论文固定版本、CDT 当前 arXiv 版本记录及作者 PDF、OpenAI 当前原仓库文本；复用了项目文献库，并对照了[2026-10-07 的较广混合目标审查](../literature/catalan_pi2_mixed_novelty_source_scope_20261007.md)。另作了关于 “Catalan / ζ(2) / π² / 2G / linear combination / linear independence” 的精确词组与 arXiv 域名检索。搜索摘要、维基百科、博客和转载页面没有用作定理证据。

该范围没有穷尽所有语言、期刊、作者网页与未公开手稿；相关证明的全部中间推论也未逐一筛查。因此准确记录是“**本次核读未发现适用定理**”，不是“**已证明无人证明过**”。若未来找到一个新陈述，须逐项核对字符、权、实/非阿基米德取值、常数项与量词，再更新此记录。本轮没有形成新的无理性证明，也没有执行重型数学或 Lean 验证。
