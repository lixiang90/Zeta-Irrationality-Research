# 全部奇数 ζ 无理性：分析与丢番图路线的文献复核

检索日期：2026-10-04。本文核对原始论文的定理、量词、方法和当前版本；不进行新参数扫描。ζ(5) 的基准采用项目已审阅的 Fauzan 论文及形式化证明端点。其余文献的“定理”指原文作为定理发表的结果，并不表示本轮重新形式化了整篇证明。新预印本的摘要声称与计算 Claim 单独标明。

最重要的发现是：**单目标整数多项式的通用无理性判据已经存在，缺的是对每个奇数权重构造满足该判据的输入。** Zudilin 2017 年已把单目标正矩近似提升为正 Hankel 行列式，并以二次尺度衰减战胜分母增长。ζ(5) 新论文在特定权重上完成了更精细的正性、完整泛函算术与实侧能量配合；不能把这一步自动推广为全部奇 ζ 的输入存在定理。见下文第 4–7 节。

## 1. 先分清四种结论

记

\[
d(S)=\dim_{\mathbb Q}\operatorname{span}_{\mathbb Q}
\{1,\zeta(3),\zeta(5),\ldots,\zeta(S)\},
\quad
N(S)=\#\{j\in[3,S]:j\text{ 为奇数且 }\zeta(j)\notin\mathbb Q\}.
\]

|结论|准确含义|对 ζ(7) 或固定组合的作用|
|---|---|---|
|指定单值|证明某个明确的 ζ(r) 无理|ζ(3)、本项目基准 ζ(5) 属于这一类|
|至少一个／若干个|某个有限集合中有无理数|一般不能确定是哪一个成员|
|无限多个／个数下界|N(S) 随 S 增长|不能指定一个固定 r，也不能指定一组固定系数|
|维数下界|d(S) 随 S 增长|强于相应的个数结论，但远小于满维时仍不能选择指定成员|

“所有奇 ζ 分别无理”和“1 与所有奇 ζ 线性独立”也不同。两个无理数可有有理线性组合：若 x 无理、y=1−3x，则 y 无理而 3x+y=1。故 ζ(3)、ζ(5) 分别无理并不直接证明 3ζ(3)+ζ(5) 无理。

## 2. 原始结果与当前进展

下表中的“充分大”都有相应阈值；含 ε 的阈值通常依赖 ε。所有对数为自然对数。

|文献|已证结论及量词|作用范围|
|---|---|---|
|Apéry，1979|ζ(3) 无理；同篇也处理 ζ(2)|指定单值。[原文](https://numdam.org/item/AST_1979__61__11_0.pdf)|
|Beukers，1979|用双重／三重积分证明 ζ(2)、ζ(3) 无理|为正积分和整数线性形式提供范例。[原文 DOI](https://doi.org/10.1112/blms/11.3.268)|
|Rivoal 2000；Ball–Rivoal 2001|每个 ε>0，对充分大的奇 S，d(S)≥(1−ε)log S/(1+log 2)|无限多个奇 ζ 无理；不是每个指定值。[Rivoal 原稿](https://arxiv.org/abs/math/0008051)、[Ball–Rivoal 原文](https://doi.org/10.1007/s002220100168)|
|Zudilin，2001|ζ(5)、ζ(7)、ζ(9)、ζ(11) 至少一个无理|四个数的选择结论；ζ(5) 已知后不再给 ζ(7) 新信息。[原文](https://www.mathnet.ru/eng/rm427)|
|Zudilin，2001/2002|每个奇整数 b≥1，ζ(b+2)、ζ(b+4)、…、ζ(8b−1) 至少一个无理|随起点移动的窗口，不是固定长度窗口或指定成员。[原始预印本](https://arxiv.org/abs/math/0104249)|
|Fischler，2017|每个奇 d≥1，有奇 σ₁、σ₂，d+2≤σ₁<σ₂≤151d，使 1、ζ(σ₁)、ζ(σ₂) 线性独立|两个未知位置的成员；论文另给相隔较远的大族。[原文](https://www.numdam.org/articles/10.24033/bsmf.2741/)|
|Fischler–Sprang–Zudilin，2019|每个 ε>0，对充分大的 S，N(S)≥2^((1−ε)log S/log log S)|无理数个数，不能替换为同样的维数下界。[原稿](https://arxiv.org/abs/1803.08905)|
|Lai–Yu，2020|每个 ε>0，对充分大的奇 S，N(S)≥(c₀−ε)√(S/log S)，c₀=1.192507…|改进个数增长量级。[原稿](https://arxiv.org/abs/1911.08458)|
|Lai–Zhou，2021|ζ(5)、ζ(7)、…、ζ(35) 至少两个无理|与 ζ(5) 已知无理合用，可得 ζ(7)、ζ(9)、…、ζ(35) 至少一个无理；仍未指定 ζ(7)。[原稿 v2](https://arxiv.org/abs/2103.00904)|
|Lai，2025|Theorem 1.1：对充分大的正整数 S，N(S)≥1.284579√(S/log S)|仍是个数；摘要的 1.284 是较粗常数。[原文 v2](https://arxiv.org/html/2501.05321v2)|
|Fischler，2026|对充分大的奇 S，d(S)≥0.21√(S/log S)|这是维数，不能因常数小于 1.284579 就判断它较弱。[原文 v3](https://arxiv.org/html/2109.10136v3)、[期刊 DOI](https://doi.org/10.1112/jlms.70535)|
|Fauzan，2026|指定 ζ(5) 无理；本项目使用其已核对的形式化端点|不包含 ζ(7)、固定组合、超越性或线性独立性结论。[原始记录](https://zenodo.org/records/22826419)|

上述维数下界仍为 o(S)，而奇数成员总数约为 S/2；无论从“无限多个”还是这些下界出发，都不能剔除某个固定权重作为例外。

**2026 年 9 月的一项版本细节。** Lai《Small improvements to the Ball–Rivoal theorem and its p-adic variant》v3（2026-09-25）将无需程序的 1.009 倍 Ball–Rivoal 常数写为 Theorem 1.3；1.119356 倍以及 d(75)≥3 分别写为计算 Claim 1.5、1.6，作者明确说明其计算未要求审稿人检查。摘要的 1.119 不能不加说明地当作与 Theorem 1.3 同一验证状态。其大 S 实数维数结果已被 Fischler 的平方根下界包含，但 Φₙ 算术机制仍值得借鉴。[当前 v3](https://arxiv.org/html/2407.14236v3)

Suman《At least one of the three numbers ζ(5), ζ(7), and ζ(9) is irrational》是 2026-09-15 的 math.GM 预印本；本轮未独立审计，未列入上表的已证基准。即使该声称成立，在 ζ(5) 已知后也不能推出 ζ(7)。[预印本 v1](https://arxiv.org/abs/2609.22316)

## 3. 多权重线性形式：它们解决了什么，还缺什么

Ball–Rivoal 路线从具有对称性的有理函数出发，部分分式求和得到

\[
L_n=\rho_{0,n}+\sum_{\substack{3\leq j\leq S\\j\text{ 奇}}}
\rho_{j,n}\zeta(j).
\]

控制整数系数增长及 Lₙ 的渐近大小，再用线性独立性判据得到维数下界。其输入本来就是一个多权重族；只有“不全有理”假设时，它已能产生整数矛盾，不必将 ζ(7) 单独隔离。[Ball–Rivoal 原文](https://doi.org/10.1007/s002220100168)

Zudilin 的 Φₙ 因子从整组部分分式系数的素数整除性节省共同分母；Krattenthaler–Rivoal 对特定超几何族证明分母猜想。这些是实际算术增益，但不是“任意超几何输入在任意权重都具有足够分母节省”的定理。[Zudilin 2004 原文](https://doi.org/10.5802/jtnb.447)、[Krattenthaler–Rivoal 作者原稿页](https://mat.univie.ac.at/~kratt/artikel/kratriv.html)

FSZ 的 Hurwitz ζ 分布关系产生若干系数相关的线性形式。假设无理权重的个数太少，可选择消元系数抵消那些位置，留下有理组合并获得矛盾。Lai–Yu 改进零点配置，Lai 2025 进一步结合 Φₙ。这种“假设例外集合太小再消去例外”的逻辑，不保证消去所有非目标权重后仍有足够好的 ζ(7) 形式。[FSZ 原稿](https://arxiv.org/abs/1803.08905)、[Lai–Yu 原稿](https://arxiv.org/abs/1911.08458)、[Lai 2025 原文](https://arxiv.org/html/2501.05321v2)

Fischler 2026 的改变更深：用 Siegel 引理构造**非显式、较低高度**的有理函数，再由广义 Shidlovsky 重数估计和改进的 Siegel 线性独立性判据认证足够多的形式。计算在 z=−1 进行，利用 Liⱼ(−1)=(2^(1−j)−1)ζ(j)，避开 z=1 的微分系统奇点。当前 v3 不再要求系数矩阵总是达到旧稿所声称的最大秩，而使用足够的较弱秩结论；旧稿的满秩推断不能直接移植。[当前原文](https://arxiv.org/html/2109.10136v3)

**对项目的推论。** 非显式低高度构造值得取代“最小首一分子不断扫描”。不过，普通 Siegel 引理只保证约束格中有短非零向量；它不自动保证向量没有同时杀死目标斜率、不自动落入正 Gram 的区域，也不提供本原多项式的负二次预算。要用于指定 ζ(7)，需针对目标投影证明额外的非退化性和高度—正性相容性。

## 4. 单目标整数多项式判据已经存在

Zudilin《A determinantal approach to irrationality》，Constr. Approx. 45 (2017), 301–310，arXiv:1507.05697v2，给出以下输入。设 ξ∈ℝ，有有理数 aₙ、bₙ 和正整数 δₙ，使

\[
r_n=a_n\xi-b_n,
\qquad 0<r_n\leq C_1\varepsilon^n,
\qquad \delta_na_n,\delta_nb_n\in\mathbb Z,
\qquad \delta_n\leq C_2\Delta^n.
\]

另要求 δₙ∣δₙ₊₁，以及共同正矩表示

\[
r_n=\int_\gamma z(x)^n\,\omega(x),
\]

其中 γ⊂ℝᵐ 是积分域，z 是其上的非负、连续、非常值函数，ω 是正微分形式，相关积分有限。Proposition 2 证明

\[
\boxed{\varepsilon\Delta^{3/2}/4<1\quad\Longrightarrow\quad \xi\notin\mathbb Q.}
\]

其正 Hankel 行列式 Hₙ=det(rᵢ₊ⱼ) 是 ξ 的至多 n 次有理多项式；δₙ₋₁⋯δ₂ₙ₋₂Hₙ 是整数多项式。Vandermonde 能量给 Hₙ≤(ε/4)^(n²+o(n²))，分母代价为 Δ^((3/2)n²+O(n))。若 ξ=a/b，有理分母只再增加 bⁿ。正性排除零值，严格负的二次项给矛盾。[原始 PDF，Proposition 2 与证明](https://arxiv.org/pdf/1507.05697v2)

这里正矩条件实质性地保证高阶行列式不消失。一般正数列即使指数变小，也可能全部高阶 Hankel 行列式为零。对本项目，不能删掉“共同正矩”而仅保留几项数值为正。

Haynes–Zudilin《Hankel determinants of zeta values》也较早证明了 ζ 值算术级数的正 Hankel 行列式及其极强衰减。但其结果是：相应级数中无限多个值无理，**或**剩余有理值的共同分母无法有统一指数上界；并非每个 ζ 值无理。该行列式本来含多个 ζ 值，只有某一个 ζ 值有理时不会变成整数。[原始 PDF](https://sigma-journal.com/2015/101/sigma15-101.pdf)

因此，正行列式和二次衰减均有先例；ζ(5) 新论文的贡献应在**特定单目标输入的完整配合**上定位。

## 5. ζ(5) 新论文与 cellular、Padé、G-functions 路线

### 5.1 ζ(5)：同一输入同时完成三个条件

Fauzan 论文得到，对所有充分大的 n，

\[
Q_n=Q_{40n,200}\in\mathbb Z[X],\qquad
\deg Q_n=37n,\qquad
0<Q_n(\zeta(5))<\exp(-139n^2/5).
\]

每个矩阵条目只对 X 仿射；在 X=ζ(5) 处是正矩矩阵。算术估计保留多项式商与简单极点项，涵盖整个泛函及行列式全部系数；不同素数区间的消失基和秩界，使整数化成本小于实侧势能衰减。最后的研究说明明确把更高奇权重的相容正性与分母估计列为未完成部分，并未声称已得到推广。[原始论文记录](https://zenodo.org/records/22826419)

上述输出无需多项式高度估计便能排除有理数；论文关于无理性指数的附录另外需要控制邻近有理点处的正性。不能把用于近似指数的附加条件误认为无理性主证明的前提。

项目形式化基准可由 [danromik 的形式化仓库](https://github.com/danromik/zeta5-irrationality) 与 [mo271 的 Mathlib 端点](https://github.com/mo271/Zeta5) 定位。完整无理性端点与只有若干局部引理的仓库应分开记录。

### 5.2 Brown–Zudilin：合法纯目标投影仍不保证预算

Brown–Zudilin《On cellular rational approximations to ζ(5)》v3（2026-01）构造有效的无限组有理近似

\[
0<|\zeta(5)-p/q|<q^{-0.86}.
\]

五重 cellular 积分涉及 ζ(5)、ζ(2)ζ(3) 等周期；论文用真实的上同调构造取得纯目标周期 I′=Qζ(5)−P。0.86 的指数仍不足以证明无理性：在 ξ=a/b 的假设下，非零有理近似只需满足 |ξ−p/q|≥1/(bq)。不能把形式上的动机商误当成数值 π² 项可任意置零。[原文 v3](https://arxiv.org/pdf/2210.03391v3)

这提供了目标隔离的几何机制，但不替代完整的丢番图预算。该动机分支的更详细讨论见项目另一份周期结构报告。

### 5.3 Padé 与 G-functions：函数结构和数值算术要分开

Fischler–Rivoal 对多重 ζ 的 Padé 问题以及 Vasilyev 积分证明了有理线性组合结构：相应奇权重积分落在 1、ζ(3)、ζ(5)、… 的有理张成空间中。唯一的 Padé 解和已知微分方程并不自动使分解只含指定 ζ(r)，也不自动让整数化后的数值趋零。[原始 PDF](https://www.imo.universite-paris-saclay.fr/~fischler/padezetaimp.pdf)

Fischler–Rivoal 的 G-functions 定理研究固定非多项式 G-function F(z)=ΣAₖzᵏ 的带权积分族 Fₙ^[s]，在固定代数点 α、0<|α|<R 下，相关值的数域维数具有对数型下界。第二篇可越过收敛圆，但要求 α 属于适当解析延拓域且不是所用微分算子的奇点。它们给出一个族中的独立值，未给“任意 G-function 的每个特殊值无理”；因此不能直接在产生 polylog 族的 F(z)=1/(1−z) 的奇点 z=1 套用一般值定理。[第一篇](https://arxiv.org/abs/1701.09051)、[第二篇](https://arxiv.org/abs/1811.08758)

Prévost 的 Hurwitz ζ Padé 余项及 2026 年 Hurwitz–Lerch 有理近似是新的近似输入来源；其近似构造／收敛本身没有宣布指定 ζ(7) 无理性定理。使用时还需证明对应整系数、非零及足够快的清分母后衰减。[2017/2019 原稿](https://arxiv.org/abs/1709.05389)、[2026 原稿](https://arxiv.org/abs/2606.15132)

### 5.4 固定线性组合也不能靠移动组合定理指定

Fischler 2017 对任意固定实系数 λ₀,…,λ_d（不全零），证明了随奇 s 移动的一族二项式加权组合

\[
\lambda_0\zeta(s)+\sum_{j=1}^d
\lambda_j\binom{s+2j-1}{2j}\zeta(s+2j)
\]

有无限多个无理成员。取 d=1、λ₀=3、λ₁=1/6，s=3 时的成员正是 3ζ(3)+ζ(5)；“无限多个 s”并不保证 s=3 是其中之一。[原文，Theorem 1.7 与 Corollary 1.8](https://arxiv.org/html/1310.1685)

## 6. 真正缺哪一种一般定理

以下是本轮从文献与项目障碍得到的研究判断，不是对已有论文的结论转述。

### 6.1 所需的权重统一不必有绝对统一常数

要证明“每个奇 r≥3 的 ζ(r) 都无理”，可以对每个固定 r 分别证明常数 C_r、c_r 和阈值 K₀(r) 存在。无需 C_r、c_r、K₀ 都独立于 r。缺的是涵盖全部 r 的构造与证明规则，而不是一个漂亮但过强的统一数值常数。

一个够用的多项式输出定理是：对每个奇 r≥3，有 C_r,c_r>0 及整数多项式 P_{r,K}，使对所有充分大 K，

\[
\deg P_{r,K}\leq C_rK,
\qquad
0<|P_{r,K}(\zeta(r))|\leq e^{-c_rK^2}.
\tag{U}
\]

证明其充分性很短：若 ζ(r)=a/b，则非零整数 b^deg(P)P(a/b) 的绝对值至少 1，但 (U) 使它至多 exp(C_rK log b−c_rK²)→0。更一般，只需 log|P(ζ(r))|/deg P→−∞。二次尺度是方便的强输出，不是唯一可能尺度。

线性形式路线所需输出更直接：对每个 r，构造整数 A_{r,n}、B_{r,n}，使非零 |A_{r,n}+B_{r,n}ζ(r)|→0。无理性本身不需要先证明系数高度界；高度界的用途是建立这一衰减或进一步给近似指数。

### 6.2 需要的是相容的输入存在定理

适合本项目的目标可分为三项，必须由同一输入同时完成：

1. **准确单目标隔离。** 所有条目／积分／线性形式最终只含有理数与 ζ(r)，并涵盖全部低阶 ζ 和乘积周期。若只是多变量小多项式，单独假设 ζ(r) 有理不会把其他周期变为整数。
2. **无限族的非零。** 最好由正测度 Gram 认证；截断正性也可以，但要对无穷多尺度给证明。有限主元或少数参数的正性不能提供 (U) 的量词。
3. **完整本原算术胜过实侧衰减。** 设有理行列式为 Δ_K(X)，要控制整数多项式 Δ_K/cont_Q(Δ_K) 的实际值。极点与多项式商、目标斜率与常数列，以及全部素数贡献都要进入同一预算。

理想的新定理是：在指定奇权重的目标隔离约束格中，存在一个高度可控、目标不退化、具有所需 Gram 正性且允许足够 content 节省的无限分子族。Plain Siegel 引理只保证短非零格向量，不能补齐后面三个限定；广义 Shidlovsky 的多权重维数结论也没有给出这一存在定理。

### 6.3 ζ(7) 项目中的障碍属于输入，不属于判据

项目已证明的共同分子、连续单项式 Gram、h≥K 退化结果只约束该特定极点／输入空间，不能据此宣布全部 Padé、稀疏指数、不同节点、cellular 积分或其他基础核都不可能成功。反过来，h<K 中出现纯 ζ(7) 条目和有限正定候选，也还未证明最终本原值有负二次指数。

从 ζ(5) 升至 ζ(7)，Bernoulli 坏矩更早并在多层出现，较高阶极点带来额外 ζ 消元约束；短分子不自动降低完整行列式 content 成本。项目的头块障碍还说明，某些统一端点上界已被头块本原值支配；仅继续改善同类舍入或端点正性，没有额外的无理性出口。

## 7. 建议将研究问题改写为可证明的结构目标

|下一步结构问题|借鉴来源|必须交付的数学结论|
|---|---|---|
|取消固定首一分子的偏好，研究整个约束格|Fischler 的非显式辅助函数|格行列式／短向量界；目标斜率不随短向量一起消失；正性区域中确实有可控向量|
|设计系数相关的多组输入，而不是孤立优化单个核|FSZ 的 Hurwitz 分布消元|消去所有非目标项后的净分母成本、剩余目标非零和统一衰减；不能只算消元维数|
|寻找真实周期或积分上的目标投影|Brown–Zudilin cellular 方法|实际积分恒等式与单目标分解；分母与衰减需另证，不能把形式商当数值去项|
|让局部条件与实侧核共同设计|Φₙ、ζ(5) 全泛函算术、Zudilin 正矩判据|完整 content 下界及能量上界给同一族严格负的 K² 预算|
|研究稀疏／非坐标输入空间或新的正核|项目已证限制仅适用于特定空间|新的正性恒等式与独立秩界；重新核算全部目标 content，而非只证明矩阵正定|

这些目标比扩大参数扫描更有区分力。若只能证明 N(S) 或 d(S) 的增长，应将结论保留在其实际量词下；若要攻指定 ζ(7)，从一开始就应以单目标输出 (U) 或整数线性形式输出作为完整验收条件。

## 8. 版本核对与可供 literature 保存的原始 PDF

本轮不重复下载文件、不改 literature 索引。下列是原作者、arXiv、期刊的公开稿链接；DOI 页不一定允许匿名取得 PDF。

|资料|本轮核对的版本／PDF|
|---|---|
|Apéry 1979|[Numdam PDF](https://numdam.org/item/AST_1979__61__11_0.pdf)|
|Beukers 1979|[期刊 PDF](https://academic.oup.com/blms/article-pdf/11/3/268/6691411/11-3-268.pdf)，可能受订阅限制|
|Rivoal 2000|[arXiv 原稿 PDF](https://arxiv.org/pdf/math/0008051)|
|Zudilin 2001/2002 长文|[作者 PDF](https://www.math.ru.nl/~wzudilin/PS/zete_main.pdf)；[早期 arXiv PDF](https://arxiv.org/pdf/math/0104249)|
|Zudilin 2004 算术|[arXiv PDF](https://arxiv.org/pdf/math/0206176)|
|Fischler 2017 分布|[作者 PDF](https://www.imo.universite-paris-saclay.fr/~stephane.fischler/distrib.pdf)|
|FSZ 2019|[arXiv PDF](https://arxiv.org/pdf/1803.08905)|
|Lai–Yu 2020|[arXiv PDF](https://arxiv.org/pdf/1911.08458)|
|Lai–Zhou 2021|[v2 PDF](https://arxiv.org/pdf/2103.00904v2)|
|Lai 2025 II|[v2 PDF](https://arxiv.org/pdf/2501.05321v2)|
|Fischler 2026 Siegel|[arXiv v3 PDF](https://arxiv.org/pdf/2109.10136v3)；[作者当前 PDF](https://www.imo.universite-paris-saclay.fr/~stephane.fischler/siegel.pdf)|
|Lai 2026 更新|[v3 PDF，2026-09-25](https://arxiv.org/pdf/2407.14236v3)|
|Zudilin 2017 行列式判据|[v2 PDF](https://arxiv.org/pdf/1507.05697v2)|
|Haynes–Zudilin 2015|[SIGMA 原始 PDF](https://sigma-journal.com/2015/101/sigma15-101.pdf)|
|Fischler–Rivoal Padé|[作者原始 PDF](https://www.imo.universite-paris-saclay.fr/~fischler/padezetaimp.pdf)|
|Fischler–Rivoal G-functions I、II|[I PDF](https://arxiv.org/pdf/1701.09051)、[II PDF](https://arxiv.org/pdf/1811.08758)|
|Brown–Zudilin 2026|[v3 PDF，arXiv 2026-01-29](https://arxiv.org/pdf/2210.03391v3)|
|Prévost Hurwitz–Lerch 2026|[v1 PDF，2026-06-13](https://arxiv.org/pdf/2606.15132v1)|
|Fauzan ζ(5) 2026|[原始记录 PDF](https://zenodo.org/records/22826419/files/ZETA5_IS_IRRATIONAL.pdf?download=1)|

**本地 Fischler 文件。** `literature/fischler_siegel_odd_zeta.pdf` 为 44 页、609475 字节，PDF 元数据指向 arXiv:2109.10136v3，正文日期 December 1, 2025；SHA256 为 `39fa3b82b09ad56dbc8364acd6b27e5fb5683f548f62583e82e78b1500ddffaa`。当前 arXiv HTML 的版本标识仍为 v3、提交日期 2025-11-27，但正文显示 August 24, 2026；期刊为 JLMS 113(4) (2026), e70535。本地稿已含改进的较弱秩判据，不能当旧稿错误的最大秩证明使用；仅凭同一 v3 标识不能断言与当前公开 PDF 字节相同，本轮未重新下载作逐字节比较。

**本地 Brown–Zudilin 文件。** `literature/brown_zudilin_cellular.pdf` 为 32 页、1271148 字节，元数据指向 arXiv:2210.03391v3，正文修订日期 January 26, 2026；SHA256 为 `5a2e45566925a2de55067ca40b599bb4e8f89475a1ffc5cd506dbe896c3a1636`。现存文件已经是当前 v3 的版本序号，无需按“2022 原稿”处理；本轮同样未重新下载证明字节同一。

另两项书目纠正：Fischler《Distribution of irrational zeta values》只有 Fischler 一位作者；《At least two…ζ(35)…》作者是 Li Lai 与 Li Zhou。现存文件名 `zudilin2002_irrationality_values.pdf` 的实际内容是 arXiv:math/0206177 的多重积分论文，不能以文件名代替《Irrationality of values of the Riemann zeta function》的文献核对。

本轮可核对的原始资料中未找到指定 ζ(7) 的完整无理性证明。最可落实的新方向，是把低高度存在、目标非退化、正性和完整本原预算连接成一个真正覆盖奇权重的输入构造定理；判据本身已有成熟原型。
