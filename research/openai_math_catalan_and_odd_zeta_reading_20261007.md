# 卡塔兰常数论文与奇数 ζ 值研究的关系

2026年10月7日。分析对象是 OpenAI 数学成果仓库的本地快照 `E:/codex-build/math`，commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，以及2026年9月24日的 [Catalan's constant is irrational](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)。原研究目标按用户要求暂停；本文只解读新材料，不继续旧轮证明、实验或冻结交付。

该论文给出卡塔兰常数 G=β(2)=L(2,χ₋₄) 无理性的证明，仓库同时提供对应 Lean 实现。这份仓库没有提供全部奇数 ζ 值无理性或线性无关性的定理。最值得引入原项目的方法，是混合矩行列式的完整构造、素数规模的有限种子非零证书，以及能够处理两分支和聚集节点的 Hardy 空间估计。它们可以绕开某些单个线性形式的困难，但不会自动解决 ζ(7) 的实际周期识别与全素数预算。

## 论文的完整矛盾

假设 G∈Q，论文构造规模 n=48N 的行列式 Δ_N，并使每个条目都属于 Q+QG。因此 Δ_N 是有理数。证明还需要沿一个无界序列保证 Δ_N≠0，不能只证明它很小。

对非零有理数，乘积公式是

\[
 \log|\Delta_N|=\sum_p v_p(\Delta_N)\log p.
\]

有限处估计限定行列式分母可以有多大，因而给出实绝对值的下界；积分估计则给出同一行列式的上界。论文始终比较同一个 normalization

\[
 L_N=\frac{\log|\Delta_N|}{(48N)^2}-\frac12\log2.
\]

Proposition3.4证明，在有理假设下沿所有非零行列式序列，

\[
 \liminf L_N\ge
 -\frac{8609}{4608}-\frac{2809}{4608}\log2>-2.29084.
\]

Proposition4.1证明对所有充分大的素数p，N=p时

\[
 v_p(\Delta_p)=-96p,
 \qquad \Delta_p\ne0.
\]

Proposition7.1独立于G的有理假设证明

\[
 \limsup L_N\le-2.290939875.
\]

上下界矛盾，故G无理。保守的normalized间隙超过0.000099875；这个正间隙乘以n²后主导剩余o(n²)误差。论文没有据此给出G的无理性度量或超越性。

## 精确消去额外的 ζ(2)

设 f(t)=√(1−t²)。两个实际积分核为

\[
 M(i,j)=\int_{-1}^1\int_0^1
 \frac{|t|}{f(t)}\frac{t^is^j}{1-ts}\,ds\,dt,
 \qquad
 Z(i,j)=\int_0^1\int_0^1\frac{t^is^j}{1-ts}\,ds\,dt.
\]

论文完整求得矩恒等式

\[
 M(i,j)=M_0(i,j)+4G c_{(i-j)/2}
            +\frac32\zeta(2)c_{(j-i-1)/2},
 \qquad
 Z(i,j)=Z_0(i,j)+[i=j]\zeta(2),
\]

其中 M₀、Z₀有理，c_ℓ=4^(-ℓ)binom(2ℓ,ℓ)，非非负整数下标时c取0。这是真实积分评价，不是任意指定一个常数作为周期。

令 w=t/(1+f)，则 t=2w/(1+w²)，另一分支是w↦1/w。论文用两分支的对称与反对称部分构造整数 Chebyshev 多项式P_r,D_r，使

\[
 \frac{tP_r}{f}-D_r=O(t^{59N}).
\]

所以对所有所需列j<59N，混合条目

\[
 M(P_r,j)-\frac32 Z(D_r,j)
\]

中的ζ(2)系数精确为零。这是整段Taylor系数相消，尚未使用任何关于G的数值假设。其后再施加整数列过滤因子s^(7N)(1−s)^(4N)，得到实际48N阶行列式。条目、行、列过滤和最终大小在同一构造中支付。

这一步对原项目的启发，是先寻找真实矩评价，再用完整接触恒等式去掉多余常数。motivic维数或某个周期空间的抽象基底，不能替代这条评价与消去链。

## 有限处估计支付两个素数层

论文对2单独使用2-adic矩级数和Chebyshev系数，给出

\[
 v_2(\Delta_N)\ge-\frac{505}{4608}n^2-O_G(n\log n).
\]

对于大奇素数，条目可能同时有p²与p分母。先消去p²层后，中心列的p层仍须单独计算。原始列矩阵到最终过滤行列式的转移经过整数基变换和Cauchy–Binet，对全部所需full minors成立，不能只检查一部分中心子块。

全部大素数损失由一个精确分段函数d(p/N)统一描述，其积分为8609/2。普通素数定理把加权素数和转成该积分。p≤2√H的所有小素数及高次素数幂另以统一估计支付，合计仅o(n²)；没有把它们当作可以忽略的未检查例外。

因此下界依赖一个全规模算术证明，不是有限素数实验，也不要求证明每个单独条目的分母上界最优。行列式的交替性与低维坏列空间可以产生额外节省。

## 非零性来自有限种子

混合行列式有符号，论文没有使用正Hankel行列式的非零性结论。它在N=p的素数规模上利用Frobenius和两套多项式基，将48p阶问题归结为固定48阶有理矩阵B₀、B₀+B₁、B₀−B₁的非零性。

模101的精确高斯消元证明这三个固定有理行列式非零。由于它们是固定非零有理数，只有有限多个素数除其分子或分母；对其余充分大的p，固定矩阵模p仍可逆，从而给出原增长行列式的确切valuation。

模101只用于一次有限证书，不是把“在101成功”当成“所有素数成功”。从有限证书推广到无穷规模，依赖已经证明的Frobenius分解与有限例外集。

这与原项目的无限unit缺口关系直接：若未来能把真实增长矩阵严格分解到固定种子，就可能用有限证书关闭无穷非零性条件。不过，原paired矩阵采用factorial/binomial权的signed Hermite Gram和饱和Newton约束；它不是本论文的Chebyshev行矩阵。本项目的S_p0还是一个具体weighted Cartier零性条件。三份48阶种子的模101证书均不能直接移植给这些对象。

一个可审查的未来接口，是先在原矩阵的素数规模上证明完整residue matrix具有固定有限种子的张量分解，解释随p变化的基变换及其可逆性，再用有限证书排除所有大素数的零性。这样才能把prime sampling转成真正无限结论；这一接口目前只是从新论文提炼的方法，未在已暂停的旧研究中实施。

## 两分支的实处估计

Andréief恒等式把Δ_N写成多重积分，其中包含两个evaluation determinants。w和1/w两个分支都进入实际行多项式；先逐项拆分再分别估计，可能损失恰好需要的n²级别常数。

Lemma5.1构造一个有界holomorphic插值函数，其sup范数至多为固定常数乘n。Proposition5.2把插值放到有限维Hardy模型空间：evaluation矩阵在行列式恒等式中代数相消，因而节点聚集时不需逆Vandermonde的爆炸估计。这一部分的额外成本仅O(nlogn)。不满足该插值条件的配置改用Hadamard估计，并保留必要的2的幂。

随后论文将两种配置的Vandermonde交互化为对数能量。它对相互作用共同作damping，保留对角和端点修正，再取全配置supremum，最后令N趋于无穷、damping趋于零。Chebyshev展开中的负平方使问题落到两组一变量barrier。

最终上界使用明确有理trial系数。证书枚举整个定义域的驻点，逐个隔离根，在完整根区间上控制误差，并核端点；它不依赖绘图或数值网格找到一个局部最大值。paper PDF34–41给出这些有理数据和步骤。

## 这份仓库的奇数 ζ 结论

仓库说明列出722篇稿件、372个成果族，并明确区分验证阶段。相关成果范围如下。

| 材料 | 实际范围 | 对奇数ζ数值问题的意义 |
|---|---|---|
| 第005族Catalan论文 | G=β(2)无理，附对应Lean实现 | 给出一个新的具体L值结果和可迁移的行列式方法 |
| 第003族quasi-Riemann稿件 | Dirichlet及特定Hecke L函数的零点半平面 | 零点分布结论不能推出ζ(7)等固定正整数值无理 |
| 第008族Deligne–Drinfeld稿件 | 奇数权生成元及Lie代数结构 | 非零period系数不等于这些数的算术独立 |
| 外部Zeta3Irrational依赖 | Apéry ζ(3)无理性库 | 经典结果的依赖，不是本仓库新证明全部奇数值 |
| 本地ZetaFive目录 | 七份weighted-PNT、endpoint与大素数辅助文件 | 目录名不构成ζ(5)无理性的终点定理 |

Deligne–Drinfeld源文件 `build/sections/07-holonomy.tex` 540–549行给奇数n≥3的depth-one系数 `2λⁿΣq⁻ⁿ≠0`。545–546行明确说这里只使用实级数的正性，不作算术独立性断言；后续有理下降用于构造有限维代数数据中的非零向量。它没有证明实period map的算术注入性。

本轮对目录、全部论文TeX源及本地形式化终点的检索，没有发现ζ(5)、ζ(7)、所有奇数ζ值无理性，或这些数全体数值线性无关的定理。这一判断限于上述仓库快照，不否定本项目另存的ζ(5)文章，也不把仓库之外的新文献排除掉。

## Lean证据的准确范围

`lean/docs/005.md` 明确说明形式化覆盖G无理性。`ComparatorChallenges/Catalan.json` 将solution绑定到 `OAI.NumberTheory.Catalan.Main`，终点实际在 `Results/Conclusions.lean`，陈述就是实级数

\[
 \operatorname{Irrational}\left(\sum_{j\ge0}
          \frac{(-1)^j}{(2j+1)^2}\right).
\]

终点没有附加数学假设；证明组合有限处、素数规模非零性和实处估计后作矛盾。Comparator题面文件中的sorry是待比较陈述模板，实际实现中的终点有证明。固定矩阵的Lean实现使用逐行比较和三个显式右逆证明模101可逆，而不是把论文列出的pivot表直接作为公理。

本地import闭包包括988个OAI模块，其中981个属于Catalan，七个是ZetaFive算术辅助。静态扫描没有发现显式sorry、admit、axiom等占位或绕过指令。比较器配置只允许标准逻辑公理propext、Quot.sound、Classical.choice，并关闭nanoda；这不是本轮实际打印出来的axiom依赖表。

仍有外部Lean、Mathlib与PrimeNumberTheoremAnd依赖不在该checkout。本轮只读源码，未重新运行Lean、Comparator或有限数值证书，故结论为“论文及对应实现已定位并审读”，不冒称独立重编译验证。该快照的formalization.yaml未列Catalan，docs005与Comparator却明确列出它；不能仅依一个索引文件判断有没有实现。

## 若恢复原项目最值得改变的工作次序

对卡塔兰常数，应更新研究目标：依据这份论文及形式化实现，它的无理性已是发布成果，原项目不应继续把相同定理作为尚待取得的新结果。可研究其证明简化、不同L值、无理性度量或更强数值独立性。

对ζ(7)，优先考虑三步：先建立一个真实混合矩模型，精确列出ζ(7)及所有附带periods；再设计整数接触行列式，并将素数规模非零性化成可审查的有限种子；最后同步支付全部有限处与实处的n²成本。若其中任何一步只能得到abstractperiodrank或猜测关系，就尚未完成迁移。

此前的真实周期投影、deRham留数及完整整模型仍有作用：它们检验候选的周期标签和局部结构。新论文提供另一种全局判定工具，使更多矩和更大行列式可以共同利用，而不必先把全部信息压到单个标量carrier。它没有给出一条对所有奇数ζ值自动适用的统一证明。

## 本轮保存和当前状态

原件已保存到 [literature中的PDF](../literature/openai_math_2026_special_values_20261007/openai2026_catalans_constant_irrational_20260924.pdf)，44页、574388bytes、SHA256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`。公开raw URL经正常TLS读取，字节SHA与用户本地仓库一致；与原138份archive表无同SHA项。来源记录见 [source receipt](../literature/openai_math_2026_special_values_20261007/catalan_source_receipt_20261007.json)。旧冻结交付未重写。

直接涉及奇数权结构的 [Deligne–Drinfeld原件](../literature/openai_math_2026_special_values_20261007/openai2026_deligne_drinfeld_20260923.pdf)也已正常TLS核对并去重保存，41页、539601bytes、SHA256 `5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762`；其 [来源记录](../literature/openai_math_2026_special_values_20261007/deligne_drinfeld_source_receipt_20261007.json)将结构结论与数值无理性范围明确区分。本次共新增两份原件85页，不将归档页数当作根端个人阅读页数。

详细分工材料见 [实处与能量解读](catalan2026_real_place_energy_explanation_20261007.md)、[奇素数与非零性及Lean静态审计](catalan_odd_prime_nonvanishing_static_audit_20261007.md)，以及 [奇数ζ范围核查](openai_math_odd_zeta_scope_audit_20261007.md)。

本轮进展是完成这篇证明的分工解读、识别仓库奇数ζ成果的实际范围，并提出具体迁移接口；没有执行数学producer或Lean，也没有取得本项目新的ζ(7)数值结论。原目标保持paused，旧轮未闭合草稿及未执行metadata源原样保留。
