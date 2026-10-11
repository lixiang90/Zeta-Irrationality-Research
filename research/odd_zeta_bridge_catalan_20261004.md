# Catalan 完整周期系统：正则芽、单值化与实际整性之间的桥梁

检索及版本核对：2026-10-04。本文续接 [Dirichlet 统一框架](E:/kimi-build/zeta5/research/odd_zeta_global_dirichlet_20261004.md)，仅使用原始论文与官方公式。以下无条件引理是从这些公式推出的结果；没有进行参数扫描，也没有证明 G 或 ζ(7) 无理。

本轮得到两个明确的限制，以及一个可直接使用的解析桥梁。CDT 的 Catalan 系统中，单值代数系数微分算子消去 C 时必然同时消去 A，不能留下纯 G 芽。另一方面，Catalan motive 的简单极点、非负整数分子及原统一清分母因子，不能单靠缩小积分证明无理性：实际整数化积分存在正指数下界。真正的纯 G、Q 系数正则芽和 Apéry 极限已经可以从另一族正积分无条件构造，剩余问题是其实际本原整性。

## 1. CDT 的额外周期不能被保留目标的代数微分投影消掉

使用 [CDT 2510.04156v1，§5.2，(5.9)–(5.11)](https://arxiv.org/html/2510.04156v1)。设

\[
\mathcal L=x(1+16x)^2\partial_x^2+(1+16x)^2\partial_x-4,
\]

\[
A=\sqrt{1+16x}\,{}_2F_1(1/2,1/2;1;-16x),\qquad
C=\sqrt{1+16x}\,{}_2F_1(1/2,1/2;1;1+16x).
\]

有 `ℒA=ℒC=0`，而 `ℒB=ℒD=1+16x`。B 是 `B(0)=0,B′(0)=1` 的 Q 系数正则解，实侧的另一个解满足

\[
D=B-\frac G2 A-\frac{\pi^2}{16}C.
\tag{1}
\]

这是完整实周期关系，不能把末项按形式 Tate 商直接设为零。CDT 所讨论的 2-adic 正则化与实侧正则化不同。

令 `z=−16x`。对零平衡超几何函数，[NIST DLMF (15.8.10)](https://dlmf.nist.gov/15.8#E10) 在 `a=b=1/2,m=0` 时给出

\[
{}_2F_1(1/2,1/2;1;1-z)
=-\frac1\pi{}_2F_1(1/2,1/2;1;z)\log z+H_0(z),
\]

其中 H₀ 在 z=0 正则。因此 `C=−A log z/π+H(z)`，原点正向绕行的 monodromy 为

\[
M_0A=A,\qquad M_0C=C-2iA.
\tag{2}
\]

**引理 1（消 C 同时消 A）。** 若 P 是单值亚纯系数的有限阶线性微分算子，且 `PC=0`，则 `PA=0`。尤其适用于 `P∈Q(x)[∂x]`。

证明：P 与绕行延拓交换，所以 `0=P(M₀C−C)=−2iPA`。该论证只要求系数单值；原点允许有极点。若系数为有限代数扩张中的代数函数，绕行有限次使系数返回原支，再用 `M₀^rC−C=−2irA`，结论仍成立。对 `θ=x∂x`，同样有 `PθC=0⇒PθA=0`。

所以在 (1) 中利用这样的 P 得到 `PD=PB−(G/2)PA` 时，消掉 C 的同时也会消掉 G 系数。此时 `PD=PB`，没有留下无理性目标。这个结论无需先调用超几何不可约分类。

还可以核对全局不可约性：z=1 的绕行使 `M₁C=−C,M₁A=−A+2iC`，其中负号来自 `√(1−z)`。M₀ 的唯一特征直线是 A，M₁ 的唯一特征直线是 C，两者不同；故齐次二阶系统没有共同不变直线。C 的最小单值系数算子不能是一阶，否则绕行后仍只能在 C 的一维解空间内，而 (2) 与此矛盾。

直接正则化当然可以写作 `D+(π²/16)C=B−(G/2)A`，但其常数项是 `−G/2`。它落在 Q[[x]] 与 G 有理等价，不能把这种条件正则芽误称为已给出的 Q 系数芽。允许含 C 的对数或周期的超越系数算子可以绕过引理，但其系数整性与解析域需要重新证明。

## 2. Bloch–Wigner 能消去分支歧义，却不自动给出 holomorphic Q 芽

记 Bloch–Wigner 函数为

\[
\mathscr D(w)=\operatorname{Im}\bigl(\operatorname{Li}_2(w)+\log|w|\log(1-w)\bigr).
\]

它是单值实解析函数，`𝒟(i)=G`，但不是非恒定的 holomorphic 函数。Brown 的单值周期构造及 Zagier 的原始说明均保留这一差别。[Brown 1309.5309v1，§1](https://arxiv.org/html/1309.5309v1)；[Zagier，1990 原文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01453591/fulltext.pdf)。在实 x 区间上直接对 CDT 关系取虚部会同时丢掉实的 G 项，不能作为保留目标的投影。

不过可给出一个有用的**显式桥梁**。对实 u>0，令

\[
w(u)=\frac{1+iu}{1-iu},\qquad
S(u)=\frac{\mathscr D(w(u))+\mathscr D(w(1/u))}{2}.
\]

利用单位圆上的 dilogarithm 导数或直接微分其定义，得

\[
S'(u)=-\frac{\log u}{1+u^2},\qquad S(1)=G,\qquad S(0)=0.
\]

于是对 u>0，

\[
S(u)=-\int_0^u\frac{\log t}{1+t^2}\,dt
=\operatorname{Ti}_2(u)-\arctan(u)\log u,
\tag{3}
\]

\[
\operatorname{Ti}_2(u)
=\int_0^u\frac{\arctan t}{t}\,dt
=\sum_{n\ge0}\frac{(-1)^n u^{2n+1}}{(2n+1)^2}
=\frac{\operatorname{Li}_2(iu)-\operatorname{Li}_2(-iu)}{2i}.
\tag{4}
\]

这是从单值周期到 Q 系数 holomorphic G 函数的无条件变换，且 `Ti₂(1)=G`。S 本身在 u=0 有 `u log u` 项；补回明确的低权乘积 `arctan(u)log u` 才恢复正则幂级数。不能省略这个修复项。它改变了完整解析函数，不是把 CDT 的 C 形式除掉；(4) 在 ±i 仍有非平凡 monodromy。奇 ζ 的边界周期与 Catalan 的正则代数点周期因此有共同 G 函数语言，仍需不同的解析域与整格预算。

## 3. Catalan motive 的对称投影为什么是真实周期消元

使用 [Eskandari–Murty–Nemoto 最新 v3](https://arxiv.org/html/2510.20648v3)。设

\[
\Delta=\{x\ge0,y\ge0,x+y\le1\},\qquad
g=1-x^2-y^2,\qquad \sigma(x,y)=(-y,x).
\]

其完整五维周期系统含 log2 及 Tate 周期。原文 Proposition 7.3.1 / Theorem 7.2.4 证明：对可积的 σ 不变分子 F，实际 de Rham 类落到二维 Catalan 子对象，从而

\[
I(F,t)=\int_\Delta\frac{F\,dxdy}{g^{t+1}}=a(F,t)+b(F,t)G,
\qquad a(F,t),b(F,t)\in\mathbb Q.
\tag{5}
\]

这里有几何上的限制：σ 不保持原相对边界 B，不能简单断言它已经作用于整个原 motive 再取平均。原文通过扩大吹起空间和 residue 结构证明 (5)。这是完整周期消元的依据，而不只是 (1) 的形式商。

简单极点 t=0 时，每个多项式分子均可积；无除法的整数轨道平方和 `F=Σ_{j=0}^3σ^j(R²)` 保证 σ 不变、非负与非零积分。高极点时必须额外证明全部相关边界上的可积性；不能凭平方和自动保留该条件。换位 `(x,y)↦(y,x)` 的反不变部分在可积且 σ 不变时 de Rham 类为零，计算可据此简化。

## 4. 整数 Chebyshev 阈值有明确的无条件下界

原文 Remark 8.3.4 的区域

\[
S=\bigcup_{j=0}^3\sigma^j\Delta
=\{|x|+|y|\le1\}
\]

包含正方形 `Q=[−1/2,1/2]^2`。以下论证不需要知道二元整数 Chebyshev 常数的精确值。

**引理 2。** 对任意非零 `P∈Z[x,y]`，实际总次数 N，有

\[
\|P\|_S\ge\|P\|_Q\ge4^{-N}.
\tag{6}
\]

证明：展开 `P=Σ c_{mn}T_m(2x)T_n(2y)`，总次数最高的一项满足 `m+n=N`。设 k 为 m,n 中正数的个数。`T_m(2x)T_n(2y)` 的最高系数是 `4^N/2^k`，而 P 的相应单项系数是非零整数，因此 `|c_mn|≥2^k4^{-N}`。Chebyshev 正交积分给 `|c_mn|≤2^k||P||Q`。合并即得 (6)。标准归一化参见 [NIST DLMF §§18.3、18.5](https://dlmf.nist.gov/18.5)。

按总次数定义的二元整数 Chebyshev 常数因此满足 `t_Z(S)≥1/4`。它严格大于原文要求的 `1/(2e^{3/2})`。所以该特定阈值条件**不可能满足**；此结论加强了原文“未知且似乎不可能足够小”的定性判断。定义与总次数约定核对 [Borwein–Pritsker 原论文，Definition 1.1](https://www.cecm.sfu.ca/~pborwein/PAPERS/P217.pdf)。本结论没有计算常数的精确值，也没有排除改善实际 content 或采用其他周期族。

## 5. 对实际正积分的加强：必须有指数级共同因子救济

**引理 3。** 若非零 `F∈Z[x,y]` 为 σ 不变，在 Δ 上非负，实际总次数为 N，则

\[
I(F,0)\ge\frac{4^{-N}}{4(N+1)^2}.
\tag{7}
\]

证明：F 在整个 S 非负。取其最高总次数的非零整数单项 `x^m y^n,m+n=N`。在 Q 上 Legendre 基 `P_m(2x)P_n(2y)` 的相应系数 ℓ_mn 满足

\[
|\ell_{mn}|\ge\frac1{\binom{2m}{m}\binom{2n}{n}}\ge4^{-N},
\]

因为 `P_m(2x)` 的最高系数是 `binom(2m,m)`。正交性、`|P_j|≤1` 及 F≥0 给

\[
|\ell_{mn}|\le(2m+1)(2n+1)\int_Q F
\le(N+1)^2\int_Q F.
\]

又 `∫S F=4∫Δ F`，且 Δ 内 `0<g≤1`，所以
`I(F,0)≥∫ΔF≥(1/4)∫QF`。即得 (7)。这是实际积分下界，不依赖由 sup 范数猜测积分大小。

v3 Theorem 8.3.1 给出统一整数化因子

\[
D_N=2^{N+2}L_NL_{N/2},\qquad L_m=\operatorname{lcm}(1,\ldots,m),
\]

其中 σ 不变使 N 为偶数。故

\[
D_NI(F,0)\ge\frac{L_NL_{N/2}}{2^N(N+1)^2}
=\exp\bigl((3/2-\log2)N+o(N)\bigr).
\tag{8}
\]

N 趋于无穷时，这一固定统一因子整数化的正积分发散。原文的同一因子因此不能通过任意非负、σ 不变整数分子的设计而产生趋零形式。

这并不排除**本原化**。在 (5) 中令

\[
h_F=\gcd(D_Na_F,D_Nb_F)>0.
\]

本原值是 `D_N I(F,0)/h_F`。若沿某族它趋零，由 (8) 必须

\[
\liminf_{N\to\infty}\frac{\log h_F}{N}\ge3/2-\log2.
\tag{9}
\]

若要求本原值以 `e^{−εN}` 衰减，则必要下界增加 ε。这个条件给出了下一步实际共同因子的最低指数目标。它只覆盖非负、σ 不变、简单极点及所指定 D_N；带符号消去、更高极点、不同整模型或经证明更好的共同因子仍可研究。对指数预算而言，统一分母上界不佳与实际本原 content 不够是不同命题。

## 6. 一个纯 G 的 Q 系数正则芽与解析延拓桥梁

考虑最简单的 σ 不变正分子 `F_n=(x²y²)^n`，令

\[
I_n=\int_\Delta\frac{(x^2y^2)^n}{g}\,dxdy.
\]

[Eskandari 2609.26308v1，Proposition 5.1](https://arxiv.org/html/2609.26308v1) 证明

\[
8(n+1)I_{n+1}=(2n+1)I_n-r_n,\quad I_0=G,\qquad
r_n=\frac{(6n+5)(2n)!(2n+1)!}{(4n+3)!}.
\tag{10}
\]

这给 `I_n=a_n+b_nG`，其中 `a_n∈Q`、

\[
b_n=\frac{\binom{2n}{n}}{16^n}.
\]

以下生成函数包装是对 (10) 的直接推导。定义

\[
J(z)=\sum_{n\ge0}I_nz^n
=\int_\Delta\frac{dxdy}{g(1-zx^2y^2)},\quad
b(z)=(1-z/4)^{-1/2},\quad \mathcal R(z)=\sum_{n\ge0}r_nz^n.
\tag{11}
\]

J 是有限正测度的 Stieltjes 型变换，在 `C∖[16,∞)` 上 holomorphic；尤其 |z|<16 正则。理由是 Δ 上 `0≤x²y²≤1/16`，且 `dxdy/g` 的总质量是 G。ℛ 是有理系数超几何型级数，在 |z|<16 正则。

将 (10) 求和得

\[
(8-2z)J'(z)-J(z)=-\mathcal R(z).
\tag{12}
\]

因此在 |z|<4，

\[
J(z)=a(z)+G b(z),\qquad
a(z)=-\frac{b(z)}8\int_0^z\frac{\mathcal R(t)}{\sqrt{1-t/4}}\,dt
\in\mathbb Q[[z]].
\tag{13}
\]

这是**完整实解析函数**的等式，没有额外 π²C 项，也没有形式 Tate 商。a 与 b 在 z=0 均为 Q 系数正则芽，而其特殊组合 J 无条件越过 z=4。b 在 z=4 的平方根奇点和 a 的对应奇点，恰由真实连接常数 G 抵消。也有

\[
G=\frac18\int_0^4\frac{\mathcal R(t)}{\sqrt{1-t/4}}\,dt,
\qquad -\frac{a_n}{b_n}\longrightarrow G.
\tag{14}
\]

后一极限由 `0<I_n≤G16^{−n}` 和 `I_n/b_n≤G/binom(2n,n)→0` 即得。它是纯 G 的 Apéry 型极限；该族与旧超几何族之间的关系已在 2026 原文证明，不是新的无理性定理。

这个桥梁说明，去掉其他周期后仍需整性输入。原统一因子 `D_{4n}=2^{4n+2}L_{4n}L_{2n}` 的 n 次根是 `16e^6`，而正测度的最大实际权重给 `I_n^{1/n}→1/16`。所以使用这一因子时 `(D_{4n}I_n)^{1/n}→e^6`。下面可直接从 (10) 给出更好的、完整证明的安全分母类型；它仍没有满足净预算。

### 6.1. 精确系数及指数成本 5 的安全奇分母类型

令 `Ĩ_n=16^nI_n=ã_n+b̃_nG`，则

\[
\widetilde b_n=\binom{2n}{n},\qquad
\widetilde a_n=-\binom{2n}{n}\sum_{k=0}^{n-1}t_k,
\quad t_k=\frac{16^k(6k+5)(2k)!(k!)^2}{(4k+3)!}.
\tag{15}
\]

这是 (10) 的有限精确解。记 `O_m=lcm{j≤m:j 为正奇数}`。

**引理 4。** 对 n≥1，

\[
\operatorname{den}(\widetilde a_n)\mid O_{4n-1}O_n,
\qquad v_2(\widetilde a_n)=s_2(n)-1\ge0,
\tag{16}
\]

其中 s₂(n) 为 n 的二进制数位和。

证明奇素数部分：取 `q=p^j,p` 为奇素数。忽略分子中的 `6k+5` 只会扩大分母上界。t_k 在 q 层的分母差为

\[
d_k(q)=\lfloor(4k+3)/q\rfloor-\lfloor2k/q\rfloor-2\lfloor k/q\rfloor\le2.
\]

由 `k=mq+r,0≤r<q`，此差等于 `floor((4r+3)/q)−floor(2r/q)`，直接验证上界 2。乘上 central binomial 后要扣掉其非负 carry

\[
c_n(q)=\lfloor2n/q\rfloor-2\lfloor n/q\rfloor\in\{0,1\}.
\]

若 q>n 且 q≤2n，则 c_n(q)=1，所以 `d_k−c_n≤1`；若 q>2n，则 k≤n−1 给 `4k+3<2q`，同样有 `d_k−c_n≤1`。若 q>4n−1，则差为零。因此逐层有

\[
d_k(q)-c_n(q)\le\mathbf1_{q\le4n-1}+\mathbf1_{q\le n}.
\]

对各 j 求和，(15) 的每个项的分母均被 `O_{4n−1}O_n` 控制，有限求和也如此。

证明 p=2 部分：由 factorial 的数位和公式，`v₂(t_k)=4k−1−2s₂(k)`。k=0 的项赋值 −1，所有 k≥1 的项赋值至少 1；又 `v₂(b̃_n)=s₂(n)`。所以 (15) 的 k=0 项是唯一最低赋值项，不能抵消，得到 (16) 的精确赋值。

单次 `O_{4n−1}` 不够。这有一个小而确切的反例，而非参数扫描：

\[
\widetilde a_1=-5/3,\quad \widetilde a_2=-569/105,\quad
\widetilde a_3=-189946/10395.
\]

最后一分母是 `3³·5·7·11`，分子不被 3 整除，但 O₁₁ 的 3 赋值只有 2。只看 r_n 的分母而忽略递推中除以 n+1，会漏掉这个额外层。

因 O_m 的对数为 `m+o(m)`，(16) 同时控制至第 n 项的共同分母，给出指数成本 **5n** 的实际安全类型，而非原粗界 6n。对 t=z/16 的规范变量，`J̃(t)=J(16t)` 的系数就是 Ĩ_n；在假设 G 为任一固定有理数时，共同分母至多再乘固定常数，其已证指数成本为 5。用这个明确因子整数化，正值的 n 次根趋于 e⁵，仍不趋零。

变量归一化必须同时记入算术和解析两侧：

|完整芽|规范解析域|本轮已证分母指数成本|标准 slit 映射的扩张|
|---|---|---|---|
|J(z)|C∖[16,∞)|log16+5|`φ_r(w)=64rw/(1+rw)²`，`φ′_r(0)=64r`|
|J̃(t)=J(16t)|C∖[1,∞)|5|`ψ_r(w)=4rw/(1+rw)²`，`ψ′_r(0)=4r`|

这里 0<r<1。由 Jensen 公式，其边界平均对数扩张分别为 log(64r)、log(4r)。两种变量下最基本的“扩张减已证分母成本”都为 `log(4r)−5<0`。因此这个已证安全类型尚不足以接上所需 holonomy 预算；不能把原变量的 log64 扩张与规范变量成本 5 混在同一账本。

上述 5 是已证明的**上界类型**，不是实际最小分母增长率的下界；ã_n、b̃_n 的额外共同因子，以及在假设 G 有理时组合系数的局部抵消，仍需分析。明确取 `E_n=O_{4n−1}O_n`、`h_n=gcd(E_nã_n,E_nb̃_n)`，则本原值为 `E_nĨ_n/h_n`。它要趋零，必须有 `liminf log(h_n)/n≥5`；若需负的固定指数，还要严格超过 5。这给这条具体桥梁一个清楚的下一步算术目标。

## 7. 下一步可证明的中间目标

当前不应再尝试在 CDT 同一二阶系统内通过代数微分算子“杀 C 保 A”，也不应继续寻找满足已被 (6) 排除的原整数 Chebyshev 阈值。

更具体的研究目标有三项：

1. 对 (5) 的精确 `(a,b)` 证明随次数 / 极点阶增长的全素数 content 公式或下界，并用 (9) 判断共同因子是否达到必要指数。固定低次数样本的大 gcd 不足以提供跨尺度结论。
2. 从 (13) 这样的完整纯 G 芽出发，证明它在足够大的复解析域中正则，同时建立其实际分母类型；这样可以把几何投影真正接到 arithmetic holonomy 或整数线性形式判据。已有解析延拓和已有粗整性分别成立，还没有满足所需的同一预算。
3. 允许高极点或带符号的几何族，但明确证明边界可积性、纯目标性及实际评价非零性。平方和保正性便利，却使简单极点族受到 (8) 的强约束；带符号后不能继续引用正积分下界或非零性。

本轮桥梁只说明哪些模块已经存在、哪些特定拼接无法成功。它没有排除所有 Catalan motive、单值周期或 holonomy 路线，也没有把系数为 Q 的正则芽本身视为无理性证明。

## 8. 原始资料与核对范围

|原始资料|版本 / 来源|本轮用途|
|---|---|---|
|[CDT arithmetic holonomy](https://arxiv.org/html/2510.04156v1)|v1，2025-10-05|§5.2 完整 Catalan ODE 与实 / 2-adic 区别|
|[NIST DLMF §15.8](https://dlmf.nist.gov/15.8)|官方公式 (15.8.10)|对数连接系数及 monodromy|
|[Brown 单值周期](https://arxiv.org/html/1309.5309v1)|v1，2013-09-20|Bloch–Wigner 与单值周期的适用范围|
|[Zagier 原始单值 polylog 论文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01453591/fulltext.pdf)|Math. Ann.286(1990),613–624|实解析单值化；不自动 holomorphic|
|[Eskandari–Murty–Nemoto](https://arxiv.org/html/2510.20648v3)|v3，2026-08-29|对称纯周期、统一整数化、Chebyshev 条件|
|[Eskandari 两周期族比较](https://arxiv.org/html/2609.26308v1)|v1，2026-09-22|正积分递推、与旧超几何族的精确比较|
|[Borwein–Pritsker 多元整数 Chebyshev](https://www.cecm.sfu.ca/~pborwein/PAPERS/P217.pdf)|Constructive Approximation30(2009),299–310|总次数定义与常数约定|
|[NIST DLMF §18.3](https://dlmf.nist.gov/18.3)、[§18.5](https://dlmf.nist.gov/18.5)|官方正交多项式资料|Chebyshev / Legendre 归一化|

本报告未下载文献或修改文献库；归档由根任务统一处理。
