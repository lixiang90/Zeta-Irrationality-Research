# 奇 ζ 值、Catalan 常数与 Dirichlet L 值的统一研究框架

检索与版本核对日期：2026-10-04。本文以原始论文、作者公开稿、期刊页面和 NIST DLMF 为依据；不把新预印本的摘要声称视为已审计的定理，不进行新的数值参数搜索。

最有用的统一对象是**相反奇偶性的 Dirichlet L 值及其 cyclotomic / Artin–Tate 周期结构**。奇 ζ 值对应偶平凡特征，Catalan 常数对应奇特征 χ₋₄。共同瓶颈是：怎样把目标周期从其他周期中准确隔离，并让同一组实际有理系数在全部素数处的本原化成本小于实侧衰减。几何构造、微分方程或递推的存在本身，都没有自动解决这个不等式。

## 1. 奇偶性：哪些值已经是代数数乘 π 的幂

设 χ 为导子 f 的本原 Dirichlet 特征，`χ(−1)=(−1)^a`，`a∈{0,1}`。对整数 `s≥2`，称 `s≡a mod 2` 为奇偶匹配，另一种为相反奇偶。广义 Bernoulli 数是

\[
B_{s,\chi}=f^{s-1}\sum_{r=1}^{f}\chi(r)B_s(r/f),
\qquad L(1-s,\chi)=-B_{s,\chi}/s.
\]

用 `τ(χ)=∑_{r=1}^f χ(r)e^{2πir/f}` 记 Gauss 和。奇偶匹配时，由 Bernoulli 多项式的 Fourier 展开得到

\[
L(s,\chi)=
-\frac{(2\pi i)^s}{2f^{s-1}s!\,\tau(\overline\chi)}
B_{s,\overline\chi}.
\]

因此 `L(s,χ)/π^s` 是非零代数数；`s≥2` 的非零性由 Euler 乘积保证。这些 L 值本身因 π 超越而超越。非本原特征先还原到本原特征，再乘有限个非零代数 Euler 因子。公式中的特征共轭和 Gauss 和不能随意省略。定义与函数方程见 [NIST DLMF §25.15](https://dlmf.nist.gov/25.15)；Bernoulli 定义及负整数值见 [Stanford 的原始讲义](https://virtualmath1.stanford.edu/~conrad/DarmonCM/2011Notes/dirichlet.pdf)。

|特征|匹配的正整数|匹配值|相反奇偶的目标|
|---|---|---|---|
|平凡特征，χ(−1)=1|正偶数|ζ(2m) 是非零有理数乘 π²ᵐ|ζ(3),ζ(5),ζ(7),…|
|χ₋₄，χ(−1)=−1|正奇数|β(2m+1) 是非零有理数乘 π²ᵐ⁺¹|G=β(2),β(4),β(6),…|

对 β 的匹配值，若 `sech z=∑ E_n z^n/n!`，则

\[
\beta(2m+1)=\frac{(-1)^mE_{2m}}{2^{2m+2}(2m)!}\pi^{2m+1}.
\]

特别地 `β(1)=π/4,β(3)=π³/32`。这与 G 的问题不同。参见 [Rivoal–Zudilin 2003，§1](https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf)。

相反奇偶时 `B_{s,χ}=0`，函数方程中的三角因子也为零，故直接代入只得到平凡零。应继续看**导数**，而非把目标 L 值误判为零。由 DLMF 的函数方程对 s 求导，可直接推出

\[
L(s,\overline\chi)=
\frac{(2\pi)^s e^{\pi i s/2}}
{\pi i f^{s-1}(s-1)!\tau(\chi)}
L'(1-s,\chi)
\quad\bigl(\chi(-1)=(-1)^{s+1}\bigr).
\]

例如

\[
\zeta(3)=-4\pi^2\zeta'(-2),\qquad
G=\frac\pi2\beta'(-1).
\]

这是对已核对函数方程的推导，不是新的无理性结论。它把目标转到平凡零处的导数 / regulator 周期；不能把这个未知导数当作已知代数数。相反奇偶并不证明“代数数乘 π 的幂”的关系绝不可能，只说明上述 Bernoulli 消元公式没有提供这种关系。

## 2. 偶 β 值已知什么，不能推出什么

经典已发表结果应准确分成两级：

- Rivoal–Zudilin 2003 证明 `dim_Q Span{1,β(2),…,β(A)}≥(1+o(1))log A/(2+log 2)`，因而有无限多个偶 β 值无理；同文的有限集合结果是 `β(2),β(4),…,β(14)` 中至少一个无理。不是每个值都无理。[原论文，Theorems 1–2](https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf)。
- Zudilin 2019 把有限集合缩小到 `β(2),β(4),…,β(12)` 六个数中至少一个无理，未指定 G。[原文最新 v2](https://arxiv.org/abs/1804.09922v2)，[已发表期刊](https://link.springer.com/article/10.1007/s12188-019-00203-w)。
- Lai–Zhou 的最新预印本 v2（2021-10-18；2022 年发表）进一步证明 `β(2),β(4),β(6),β(8),β(10)` 五个数中至少一个无理。其 Theorem 6.1 沿用 Zudilin 的构造，但改变有理函数归一化，把适用的 lcm 尺度从 M 改为更小的 M̃；这是实际整数化预算的改进，仍未单独锁定 G。[原文 §6](https://arxiv.org/html/2103.00904v2)，[期刊页面](https://publi.math.unideb.hu/paper/4068)。项目已有 [本地 PDF](E:/kimi-build/zeta5/literature/lai2021_at_least_two.pdf)。

更一般地，Fischler 对任意非零周期函数 f 和任一固定奇偶 p 证明：当 A 足够大时，`L(f,s)=∑ f(n)/n^s`、`2≤s≤A,s≡p mod2` 的 Q 张成空间维数至少为 `(1−ε)log A/(1+log2)`。还证明这些值中至少 `2^{(1−ε)log A/loglog A}` 个不落在任意预先固定的有限维 Q 向量空间 E 中。取 `f=χ₋₄,p=0,E=Q` 即适用偶 β 值。证明结合 Padé 构造、推广的 Shidlovsky 引理与线性无关判据；这**不是**对 E 函数值直接套 Siegel–Shidlovsky 定理。[Fischler 原文，Theorems 1–2](https://arxiv.org/html/1904.02402v1)，[JLMS 2020](https://doi.org/10.1112/jlms.12290)。

这些是强的族结论，却不能从“无限多个”或“五个中至少一个”锁定指定的 G，也不能锁定指定的 ζ(7)。用不同权重增加线性空间维数，与消除其他全部未知周期、留下单个指定值，是两种难度。

## 3. 2026 年 Catalan 证明声称的核对状态

孙智伟的 [arXiv:2609.04176v1](https://arxiv.org/html/2609.04176v1) 于 2026-09-03 提交，当前主页面仅列 v1。该文从加权交错尾项、有限残差矩阵及其非零子式构造有理多项式 scalar `q̂_B(G)`；在假设 `G=a/q` 后使用同一 scalar 的整数化 `q^S H_B^min q̂_B`，并声称其实绝对值以负的 B² 指数趋零。关键总账为 Proposition 9.5 / Theorem 9.1，声称余量超过 `0.0096624 B²`。本文已核对这条论证链的定位，但没有完成整篇证明的形式化审计。

Dane Wachs 的 [arXiv:2609.22339v1](https://arxiv.org/html/2609.22339v1) 于 2026-09-16 提交，当前也仅列 v1。其原始审计指出：秩证明的移位有可修补的问题；测试中的分母层界仍成立且接近锐；重要缺口在 Sections 6–9 的渐近总账。它用精确恒等式追踪到 scalar 实值中 `F_D` 的残余 2 幂产生约 `2 log2·B²` 的项，而展示的账本没有说明如何抵消它。作者明确限定：这些计算说明**展示的推导不足以证明所声称估计**，没有证明该渐近不等式本身必假，也没有对 G 的有理性下结论。

因此本项目当前不能把孙文的无理性声称作为可调用定理。也不宜忽略新文献而只写“从未有过证明声称”。后续同一 scalar 的全素数赋值和实侧估计，尤其 p=2，必须同时保留。2026-09-22 的独立周期论文仍将 G 的无理性称为似乎未解决，见 [Eskandari 2609.26308v1，§1](https://arxiv.org/html/2609.26308v1)。

## 4. Catalan 超几何逼近为什么还缺一步

Zudilin 的 Apéry 型二阶递推提供有理解 `u_n,v_n`，且 `v_n/u_n→G`。其特征根是 `(11±5√5)/2`；小解 `u_nG−v_n` 的 n 次根为 `φ^(−5)`，其中 `φ=(1+√5)/2`。2003 文中明确给出了整数化因子，却指出整数系数线性形式未趋于零；快收敛与新的连分数因而不是无理性证明。[原文最新 v3，Theorem 1](https://arxiv.org/html/math/0201024v3)。

后续改进证明了可用的共同整数化因子 `2^{4n+o(n)}D_{2n−1}²`，`D_m=lcm(1,…,m)`。这个已认证因子的指数成本是 `4 log2+4`，大于衰减指数 `5 logφ≈2.40606`，所以这组已知分母界没有提供负净指数。这里不能把一个不够好的分母**上界**反过来当作所有实际本原形式都不可能趋零的证明。后文还有以几何递推性质推出 G 无理性的猜想；该猜想不是定理。[Zudilin 2002，Theorem 1 与最后一节](https://arxiv.org/html/math/0210423v1)。

这给当前研究一个具体检查标准：有递推、解的比例极限和小特征根还不够，必须证明**同一实际解的共同分母 / 全 content** 的长期增长率。ζ(7) 行列式修正中得到很小实值却丢失 content，也正是在这一环节失败。

## 5. 最直接的共同语言：cyclotomic G 函数与周期

对本原 χ，有 Gauss 投影公式

\[
L(s,\chi)=\frac1{\tau(\overline\chi)}
\sum_{r=1}^{f}\overline\chi(r)\operatorname{Li}_s(e^{2\pi ir/f}).
\]

这是从有限 Fourier 和直接推得的等式。于是 `ζ(s)=Li_s(1)`，而

\[
\beta(s)=\frac{\operatorname{Li}_s(i)-\operatorname{Li}_s(-i)}{2i},
\qquad G=\operatorname{Im}\operatorname{Li}_2(i).
\]

令 `Φ_{s,χ}(z)=∑_{n≥1}χ(n)z^n/n^s`，则

\[
\theta\Phi_{s,\chi}=\Phi_{s-1,\chi},\qquad
\theta^s\Phi_{s,\chi}
=\frac{\sum_{r=1}^{f}\chi(r)z^r}{1-z^f},\quad \theta=z\frac d{dz}.
\]

这是统一的有理微分系统：奇 ζ 与 Catalan 仅改变特征投影、奇异点及实结构。它自然位于 `P¹\{0,μ_f,∞}` 的 cyclotomic 迭代积分环境。另有统一的 Mellin 积分

\[
L(s,\chi)=\frac1{(s-1)!}
\int_0^1(-\log t)^{s-1}
\frac{\sum_{r=1}^{f}\chi(r)t^{r-1}}{1-t^f}\,dt.
\]

平凡特征的核为 `1/(1−t)`，χ₋₄ 的核化为 `1/(1+t²)`。两者都是实正核；但一般特征投影未必保留正性，不能把 ζ 的 Gram 正定论证原样移植到全部 χ。

`Li_s(z)` 和这些固定 s 的周期级数是 G 函数：系数分母被 `D_n^s` 控制，具有指数增长上界，且满足有理系数线性微分方程。G 函数、Picard–Fuchs 与周期的关系见 [André 2025 原始综述](https://arxiv.org/abs/2501.09867)。注意“所有 G 算子都来自几何”的广义 Bombieri–Dwork 方向仍需额外输入，不能把它当成已经对所有 G 函数成立的构造定理。

研究不应限定为所有好构造必须是某个标准超几何族的拉回：Fresán–Lam–Qin 已给出几何来源的秩二局部系统，不能通过所讨论的超几何拉回 / 多项式表达来囊括。其反例针对的是特定超几何化命题，不能误读成推翻“几何来源”本身。[原文 2502.02147v1](https://arxiv.org/abs/2502.02147)。这为寻找 ζ(7) 与 Catalan 的新周期局部系统留下具体空间。

## 6. 为什么 E 函数定理不能直接解决 Li_s、ζ 与 G

Siegel–Shidlovsky 处理满足合适微分系统的 **E 函数**，在允许的非零代数点将函数间的代数关系与数值关系联系起来；Beukers 的精化给出更准确的关系提升。[Beukers 原始论文及期刊摘要](https://annals.math.princeton.edu/2006/163-1/p08)。

`Li_s(z)=∑z^n/n^s` 若强行按 E 函数写作 `∑a_nz^n/n!`，则 `a_n=n!/n^s`，不满足 E 函数系数的指数增长条件；此外它在 z=1 有非平凡解析分支，不是整函数。它属于 G 类。ζ(s) 又是 z=1 的边界 / 奇异点周期；Catalan 可在 Li₂ 的正则代数点 i 取值，但“点正则”并未把函数变成 E 函数。

更根本地，对 G 函数的普遍 Siegel–Shidlovsky 类比是假的。Rivoal 构造了函数上代数独立、却在指定非奇异代数点集具有代数值的 G 函数系统；所以即使排除奇异点，函数独立也不能自动推出 G 值独立。[Rivoal 2015 原始论文，Proposition 1](https://hrj.episciences.org/1357/pdf)。因此需要目标局部系统特有的几何、算术和全局解析估计。

## 7. motives、regulators 与模形式分别能提供什么

奇 ζ 的几何结构已有较明确的模板。Dupont 构造的 odd zeta motive 将 Ball–Rivoal 形式等纳入同一混合 Tate 结构，解释某一奇偶系数为何消失：Theorem 1.2 的反演 `(x₁,…,xₙ)↦(x₁⁻¹,…,xₙ⁻¹)` 使不变形式的偶权系数消失，反不变形式的奇权系数消失；它尚未消去所有其他奇权。这提供“纯目标 / 允许权重”的代数条件，而非单个指定值的自动无理性。本报告使用**最新 v3，2018-06-10**，该版修正 Proposition 3.12 的证明，并与已发表版一致。[Dupont v3，Theorems 1.1–1.2、Proposition 4.11](https://arxiv.org/html/1601.00950v3)。Brown 的 motivic 理论描述混合 Tate 周期空间，但把 motivic 非平凡性转为全部数值代数独立，仍需未证明的周期映射性质。[Brown 的原始综述](https://arxiv.org/abs/1407.5165)。

Catalan 不能简单放进“Q 上纯粹 mixed Tate、偶权扩张一律相同”的模板。Eskandari–Murty–Nemoto 的**最新 v3，2026-08-29** 构造一个 Q 上二维混合 motive，周期矩阵为

\[
\begin{pmatrix}1&G\\0&\pi^2i\end{pmatrix}.
\]

它在 Q 上不是 mixed Tate，扩域到 Q(i) 后才成为 `Q(−2)` 被 `Q(0)` 扩张的 mixed Tate 对象；Q 上更合适的语言是 mixed Artin–Tate。特征 / 复共轭数据必须保留。[原文 v3，§§1,6](https://arxiv.org/html/2510.20648v3)。

该文给出可计算的纯 `a_F+b_FG` 二重周期积分族：对适当旋转不变 F 和极点阶 t，在三角形 Δ 上积分 `F dxdy/(1−x²−y²)^{t+1}`。简单极点时，若 `N=deg F`，v3 的共同分母界是 `2^{N+2}D_ND_{N/2}`；**v1 写的是 `2^{N+3}`**，本报告按 v3 核对。此改动只改常数因子，没有改变主指数。文中将简单极点路线归结到二元整数 Chebyshev 问题，要求常数小于 `1/(2e^{3/2})`；没有证明这个输入，作者也明确表示现有统一分母界不够。这正是应单独攻克的中间问题，而不是已完成的 G 无理性证明。[v3，Theorem 8.3.1 / Remark 8.3.4](https://arxiv.org/html/2510.20648v3)。

2026 年 Eskandari 又证明：其中两个特殊二维参数子族，与旧超几何子族在显式有理 Gamma 因子下相等；证明通过 relative de Rham / Stokes 递推完成。故“新的 motive 表述”不必然带来新的实际逼近指数，必须核对有理因子和完整内容。[2609.26308v1，Theorem 1.1](https://arxiv.org/html/2609.26308v1)。

模形式 / Eisenstein 上同调是另一种周期坐标：迭代 Eisenstein 积分能表达 motivic 多重 ζ 值；这提供模变换、解析延拓和周期关系的工具。[Saad 原始论文](https://arxiv.org/abs/2009.09885)。拓扑 polylogarithm 的整数 Eisenstein 类还可给出 L 值的整性与 p-adic 插值；已证明范围须按原文限定，不能从 totally real 的结果直接声称解决 G。[Beilinson–Kings–Levin 原始论文](https://arxiv.org/abs/1410.4741)。Regulator 解释相反奇偶值为何涉及导数与扩张周期，却没有自动给出足够小的整数线性形式。

实与 p-adic 情形必须分开。CDT 的原始 holonomy 论文 §5.2 明确展示同一 Catalan 微分方程在实侧出现

\[
D=B-(G/2)A-(\pi^2/16)C,
\]

而 2-adic 侧为 `D=B−(G₂/2)A`；后者可产生 2-adic Apéry 极限，不能直接证明实 G 无理。这里额外 Tate 周期和实解析正则性恰好是缺失输入。[CDT 原文，(5.10)–(5.11)](https://arxiv.org/html/2510.04156v1)。这类个别构造的障碍不等于所有 holonomy 路线都失败。

## 8. 一个同时容纳奇 ζ 和 Catalan 的中间命题

以下是本报告建议采用的**充分判据 / 研究目标**，不是文献中已证明的统一构造定理。

固定实 Dirichlet 特征 χ 与 `s≥2`、`χ(−1)=(−1)^{s+1}`，令 `ξ=L(s,χ)`。若从 χ 投影的周期或 Padé 数据构造有理多项式 `Q_n(X)`，并存在趋于无穷的尺度 `T_n`，满足：

1. `Q_n` 的系数均已精确落在 Q，实际评价只含目标 ξ；其他 ζ、L、log 或 Tate 周期的消去有严格证明。
2. 令 `c_n>0` 为 **Q_n 全部系数的有理 content**（通分后的整数系数 gcd 除以共同分母），则 `P_n=Q_n/c_n∈Z[X]` 为本原多项式。必须同时追踪所有素数，包括整模型的坏素数及 `p|2f`。
3. `d_n=deg P_n=o(T_n)`，并严格证明 `P_n(ξ)≠0`。
4. 对无限多个 n，有同一 scalar 的净估计
   \[
   \log|Q_n(\xi)|-\log c_n\le-\varepsilon T_n,
   \qquad\varepsilon>0.
   \]

则 ξ 无理。

证明很短：若 `ξ=a/q` 为有理数，则 `q^{d_n}P_n(a/q)` 是非零整数，但其对数绝对值不超过 `d_n log q−εT_n→−∞`，矛盾。线性形式是 `d_n=1` 的特例，增长维数的 Hankel / Gram 行列式也可以容纳；但必须证明其次数小于净衰减尺度，而不是只说“有限行列式”。

等价的可操作预算是：实侧证明 `log|Q_n(ξ)|≤−τT_n+o(T_n)`，算术侧证明 `−log c_n≤σT_n+o(T_n)`，并得到 `τ>σ`。任何权重、换基、变量重标度或 Gamma 因子，必须在这**同一个 Q_n** 中同时计入。这个判据不要求假定所有周期映射单射，也没有把“存在 motive”偷换成“ξ 无理”。

尚缺的统一输入是：目标 χ–s 块的可计算隔离；同一整模型下跨尺度 content 的足够强估计；兼容坏素数和全局解析域的净指数；以及实际评价的非零性。对一般非实 χ，系数场与各共轭的范数预算还需扩大，不能把上述 Q 上实目标判据不加修改地搬过去。

## 9. 对后续 ζ(7) 研究的具体启发

- 把 odd ζ 与 Catalan 看作同一相反奇偶周期问题的不同特征分量，先研究字符投影和边界项如何隔离目标；避免从较高维周期系统未经证明地删掉额外 π² / log 周期。
- 采用 motive / relative de Rham 降极点与 Padé–G 系统两套坐标，先证明它们生成的**实际形式**及有理归一化相同，再比较净指数。2026 Catalan 两族的比较正是可参考的严格模板。
- 允许寻找不属于原超几何族的几何局部系统。新族的价值应由目标纯性、整格和真实解析尺度决定，不能仅由“阶二递推”或“Picard–Fuchs 来源”决定。
- 把已有小素数全部单位的 content 理想证书视为第 8 节算术输入的一部分；下一步需要随尺度增长的版本。固定 `K40N3h37` 的证书不会自动给出 uniform 的 τ−σ。

本文没有把新预印本声称、motivically 非平凡、p-adic 无理性、族中无限多个无理，混同为指定实 ζ(7) 或 G 的无理性。它们各自提供不同的已证模块；值得推进的是把这些模块连接到同一实际本原周期形式的严格净指数。

## 10. 本轮主要原始资料与版本

|资料|核对版本 / 出版|用途|
|---|---|---|
|[Rivoal–Zudilin，Catalan relatives](https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf)|作者公开稿；Math. Ann.326(2003),705–721|偶 β 无限多个无理、七数至少一个|
|[Zudilin，Arithmetic of Catalan](https://arxiv.org/abs/1804.09922v2)|v2，2019-05-31；Hamburg89(2019),45–53|六数至少一个|
|[Lai–Zhou，At least two](https://arxiv.org/abs/2103.00904v2)|v2，2021-10-18；Publ. Math. Debrecen101(2022),353–372|§6 五个偶 β 值中至少一个无理|
|[Fischler，Dirichlet irrationality](https://arxiv.org/abs/1904.02402v1)|v1，2019；JLMS2020|周期函数 / L 值的统一族定理|
|[Zudilin，Apéry-like equation](https://arxiv.org/abs/math/0201024v3)|v3，2002-10-28；EJC10(2003),R14|递推、小解及分母障碍|
|[Zudilin，Few remarks](https://arxiv.org/abs/math/0210423v1)|v1，2002-10-28|改进整性与未证递推猜想|
|[Eskandari–Murty–Nemoto，Catalan motive](https://arxiv.org/abs/2510.20648v3)|v3，2026-08-29|二维 Artin–Tate 周期块、显式线性形式|
|[Eskandari，Two period families](https://arxiv.org/abs/2609.26308v1)|v1，2026-09-22|新几何族与旧超几何族的比较|
|[Sun，Catalan irrationality claim](https://arxiv.org/abs/2609.04176v1)|v1，2026-09-03；证明声称|同一 scalar 总账的待审计构造|
|[Wachs，Catalan claim critique](https://arxiv.org/abs/2609.22339v1)|v1，2026-09-16；批评预印本|展示推导的缺口及原始可复现材料|
|[Rivoal，G 函数类比不可能](https://hrj.episciences.org/1357)|Hardy–Ramanujan J.38(2015),29–35|E/G 定理适用边界|
|[Dupont，Odd zeta motive](https://arxiv.org/abs/1601.00950v3)|v3，2018-06-10；Compositio154(2018),342–379|奇偶消元的几何解释；修正 Prop.3.12 证明|
|[Fresán–Lam–Qin，G 函数问题](https://arxiv.org/abs/2502.02147v1)|v1，2025-02-04|超几何拉回之外的几何局部系统|

公开 PDF 的统一下载与索引由根任务维护；本报告未自行下载、未修改 literature 索引或旧研究文件。
