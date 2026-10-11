# 新真实周期系统：Borwein–Bradley 的纯 ζ(7) 与二项式尾提升

日期：2026-10-04。旧报告冻结；本文件只记录本轮新输入、完整中间证明及其适用边界。结论不是 ζ(7) 的无理性证明。

本轮得到一个可完整认证的纯目标系统：经典逆二项式 ζ(7) 恒等式的尾和，经中央二项式 Hadamard 提升，产生在原点正则、仅依赖 `1+ζ(7)` 的芽；真值处 `z=1/4` 的平方根 monodromy 完全相消。其闭合系统有 **8 个实际线性独立函数**，标量最小齐次微分方程阶数恰为 8，对所有复参数成立，不预设 ζ(7) 无理。与此同时，本文件证明该具体族的公共前缀分母指数至少为 6；其固定解析域的共形半径只有 4，因此当前 scalar/common-prefix holonomy 判据不能由此族直接得出无理性。

这里的“新”指本项目本轮明确构造与认证的新输入；基础级数恒等式是经典文献定理，不主张全球文献首创。

## 1. 原始文献及本轮选择

| 原始来源、版本 | 已证机制与本轮用途 |
|---|---|
| [Beukers 1979，BLMS 11，268–272](https://doi.org/10.1112/blms/11.3.268) | 用真实多重积分重现 Apéry 的 ζ(2)、ζ(3) 证明。其纯目标、正积分与算术同时成立；高权照搬必须重新核纯度。 |
| [Brown，arXiv:1412.6508v1，2014-12-19](https://arxiv.org/pdf/1412.6508v1)；[作者稿](https://www.ihes.fr/~brown/IrratModuliMotivesv8.pdf) | Cellular 积分统一 Apéry 与较高权多重 ζ 线性形式；一般高权输入包含多个周期，不自动给纯 ζ(7)。 |
| [Dupont，arXiv:1601.00950v3，2018-06-10](https://arxiv.org/pdf/1601.00950v3)，Compositio 154 (2018)，342–379 | Theorems 1.1–1.4 / 4.9 给实际相对周期及有理 de Rham 坐标；奇偶 involution 消掉一整类权重。它没有自动消掉 ζ(3)、ζ(5)，也没有由动机独立性推出数值独立性。 |
| [Fischler–Rivoal，arXiv:1309.2534v1，2013-09-10](https://arxiv.org/pdf/1309.2534v1) | 用 Sorokin 型 Padé / 多重 polylog 求解 Vasilyev 奇权积分。Theorem 1 与 Proposition 1 给真实积分及奇 ζ 展开；权 7 一般仍含低奇值。 |
| [Sorokin，Hermite–Padé approximants of polylogarithms，1994](https://www.mathnet.ru/php/archive.phtml?jrnid=ivm&option_lang=eng&paperid=4220&wshow=paper) | 提供真实函数近似问题，而不是只在一个数值点作形式消元。 |
| [Lairez，arXiv:1404.5069v3，2015-08-31](https://arxiv.org/pdf/1404.5069v3)，Math. Comp. 85 (2016)，1719–1752 | Griffiths–Dwork 扩展算法给周期族的 Picard–Fuchs 方程。方程的阶数仍须与实际函数秩区别。 |
| [Borwein–Bradley，arXiv:math/0505124v1，2005-05-07 上传](https://arxiv.org/pdf/math/0505124v1)，对应 Exp. Math. 6 (1997)，181–194 | 本轮纯目标身份来源，公式 (1.4)/(2.1)。该 arXiv PDF 正文仍标 conjectured，不能单独把它当证明。 |
| [Almkvist–Granville，Exp. Math. 8:2 (1999)，197–203，作者存档 PDF](https://carmamaths.org/jon/Preprints/Papers/Published-InPress/AperyTwo/Related/almkvist-granville.pdf) | 正式证明 Borwein–Bradley 的参数恒等式，补全前一行的逻辑依据。 |

本轮优先用最后两篇得到纯目标身份，再通过实际积分和微分系统证明域相消；没有用动机投影代替数值周期，也没有将普通 `Li_7−ζ(7)` 宣称为新的全纯域。文献下载与归档由根任务统一完成，本文件未下载 PDF 或修改 literature 索引。

## 2. 纯 ζ(7) 的经典连接常数

记

\[
C_n=\binom{2n}{n},\qquad H_{n-1}^{(4)}=\sum_{j=1}^{n-1}j^{-4},
\quad t_n=\frac{(-1)^{n-1}}{n^3C_n}
 \left(\frac1{n^4}+5H_{n-1}^{(4)}\right).
\]

Borwein–Bradley / Almkvist–Granville 定理给出

\[
\boxed{\zeta(7)=\frac52\sum_{n\ge1}t_n.}\tag{2.1}
\]

等式为精确已证身份，既不含 ζ(3)、ζ(5) 干扰，也不假定 ζ(7) 的算术性质。严谨证明引用 Almkvist–Granville 1999 **Corollary 1**；2005 上传的 BB 正文没有更新其 conjecture 标签。

令

\[
H(z)=\frac52\sum_{n\ge1}t_nz^n,\qquad
s_n=\frac52\sum_{k=1}^nt_k,\quad s_0=0.
\]

### 2.1 `H` 的全局 slit 域有实际积分证明

采用一变量多重 polylog 约定

\[
\operatorname{Li}_{a,b}(x)=\sum_{n>j\ge1}\frac{x^n}{n^aj^b}.
\]

置 `Q(z)=Li_7(-z)+5Li_{3,4}(-z)`。它由 `dz/z`、`dz/(1+z)` 的迭代积分构成，在 `C\(-∞,-1]` 有原点正则的标准分支。Beta 恒等式

\[
\int_0^1[t(1-t)]^n\,dt=\frac1{(2n+1)C_n}
\]

逐项给出实际函数等式

\[
\boxed{H(z)=-\frac52\int_0^1
(2\theta+1)Q\bigl(zt(1-t)\bigr)\,dt,\quad
\theta=u\frac d{du}\text{ 在 }Q(u)\text{ 上作用}.}\tag{2.2}
\]

若 `z∈U_4=C\(-∞,-4]`，则所有 `zt(1−t)` 都避开 `Q` 的 cut，因为 `0≤t(1−t)≤1/4`。对任意紧子集，其像也是避开 cut 的紧集，故参数积分全纯。于是 `H` 在 `U_4` 全纯，`H(0)=0`，且由 (2.1) 得 `H(1)=ζ(7)`。

这一步使用真实积分及其延拓，不只是级数半径推测。

## 3. 一般二项式尾提升引理

**引理。** 设 `H(z)=Σ_{n≥1}h_nz^n∈Q[[z]]` 在
`U_R=C\(-∞,-R]` 全纯，`R>0`，记 `ξ=H(1)`、`s_n=Σ_{k≤n}h_k`。定义原点芽

\[
f_c(z)=\sum_{n\ge0}C_n(c-s_n)z^n.\tag{3.1}
\]

则真值芽有实际延拓

\[
\boxed{f_\xi(z)=\frac1\pi\int_0^1
\frac{J(4zt)}{\sqrt{t(1-t)}}\,dt,
\quad J(u)=\frac{\xi-H(u)}{1-u},}\tag{3.2}
\]

在 `U_{R/4}` 全纯；其中 `J(1)` 取可去奇点值。一般参数满足

\[
\boxed{f_c=f_\xi+(c-\xi)(1-4z)^{-1/2}.}\tag{3.3}
\]

**证明。** 尾和生成恒等式给 `J=Σ(ξ−s_n)u^n`。`H(1)=ξ` 使 `J` 在 1 可去，其余点均在原域全纯。Arcsine 矩

\[
\frac1\pi\int_0^1\frac{t^n}{\sqrt{t(1-t)}}\,dt
=\frac{C_n}{4^n}
\]

证明 (3.2) 在原点等于 (3.1)。若 `z∈U_{R/4}`，所有 `4zt` 避开 `J` 的负 cut；紧集上一致界与可积的 arcsine 权重允许求导。最后用 `ΣC_nz^n=(1−4z)^{-1/2}` 得 (3.3)。证毕。

这是真实分支相消：在 `z=1/4` 附近环行一周，

\[
M_{1/4}f_c-f_c=-2(c-\xi)(1-4z)^{-1/2}.
\]

真值函数在包含 `1/4` 的域上全纯；其他参数有非零平方根 monodromy。对 `c∈Q`，所有 Taylor 系数均为有理数，且 `f_c(0)=c`。引理不对 `ξ` 的有理性作任何先验假设。

一般引理本身不保证特殊点所需函数秩或足够小的分母；下面对 ζ(7) 分别证明这些事项。

## 4. ζ(7) 的八维闭合系统

对第 2 节的 `s_n` 应用引理，得 `f_{ζ(7)}` 在

\[
\boxed{U_1=\mathbf C\setminus(-\infty,-1]}\tag{4.1}
\]

全纯，并在 `z=1/4` 具有上述真实 monodromy 相消。令

\[
L_j=\operatorname{Li}_j(-z)\quad(1\le j\le4),\qquad
U=\operatorname{Li}_5(-z)+5\operatorname{Li}_{1,4}(-z),
\quad V=\operatorname{Li}_6(-z)+5\operatorname{Li}_{2,4}(-z).
\]

八个函数 `1,L1,L2,L3,L4,U,V,f_c` 对 `θ=z d/dz` 封闭：

\[
\begin{aligned}
\theta1&=0,&\theta L_1&=-\frac z{1+z},&
\theta L_j&=L_{j-1}\quad(2\le j\le4),\\
\theta U&=\frac{1-4z}{1+z}L_4,&\theta V&=U,&
\boxed{\theta f_c}&=\boxed{\frac{2zf_c+(5/2)V}{1-4z}}.
\end{aligned}\tag{4.2}
\]

多重 polylog 的微分规则给前两行。最后一式可完全在有理系数上检查：若 `d_n=C_n(c−s_n)`，则

\[
nd_n-(4n-2)d_{n-1}=\frac52\,v_n,\quad
v_n=(-1)^n\left(n^{-6}+5H_{n-1}^{(4)}n^{-2}\right).
\tag{4.3}
\]

因为 `C_n/C_{n-1}=(4n−2)/n`，左端恰为 `−(5/2)n C_n t_n`。

`θU` 的因子 `1−4z` 是精确函数身份。它显示低权驱动在目标分支点有额外消失，不能由一个局部数值消元代替。

### 4.1 前七个函数实际独立：不需要泛用 symbol 独立性假设

沿正实轴 `z→+∞`，用微分递推逐项积分得到

\[
L_j=-\frac{(\log z)^j}{j!}+O((\log z)^{j-1}),
\quad
U=\frac{4(\log z)^5}{5!}+O((\log z)^4),
\quad
V=\frac{4(\log z)^6}{6!}+O((\log z)^5).
\tag{4.4}
\]

其中 `θLi_{1,4}(-z)=−z/(1+z)L4`，故它的最高对数项为 `+(log z)^5/5!`；再积分一次得 `Li_{2,4}` 的最高六次项。所有七个函数增长至多为其所示对数幂。

若 `Σ r_j(z)F_j(z)=0`，其中 `r_j∈C(z)`，先取非零 `r_j` 在无穷远的最高 Laurent 幂 `z^m`，再在达到该幂的项中取最高对数次数。其非零系数没有另一项可以消掉；较低 `z` 幂乘任何有限对数幂都不能补偿。因此前七个函数在 `C(z)` 上线性独立。

这只是函数独立性，不声称其某个数值点的七个值独立。

### 4.2 `f_c` 对所有复 `c` 都增加一维

假设 `f_c` 在前七个函数的 `C(z)`-span 中。由已证独立性比较 (4.2) 的 `V` 系数，它的有理函数系数 `q(z)` 必须满足

\[
\theta q-\frac{2z}{1-4z}q=\frac{5/2}{1-4z}.\tag{4.5}
\]

若 `q` 在 0 有极点，左侧最低负 Laurent 项来自 `θq`，无法由其余项或右侧消掉，所以 `q` 在 0 正则。但正则时左侧在 0 的常数项为 0，右侧为 `5/2`，矛盾。因此无这样的有理解。

**结论：八个实际函数对所有 `c∈C` 独立，包括 `c=ζ(7)`，完全没有使用 ζ(7) 无理。**

### 4.3 标量实际阶数恰为 8

将基排序为 `(f_c,V,U,L4,L3,L2,L1,1)`。对 `f_c,θf_c,…,θ^7f_c` 的系数矩阵，其每行只到下一层，因而为三角矩阵。对角项相乘给

\[
\boxed{D(z)=-\frac{5^7z}{2^7(1-4z)^2(1+z)^6}\ne0.}\tag{4.6}
\]

实际函数基已证独立，故前八个导数独立，且九个导数因系统封闭而相关。`f_c` 的最小齐次标量微分方程阶数因此恰为 8，而不是某个算法产生的上界。

这里清分母只使用 `z` 的多项式，与参数 `c` 无关，不会由参数因子引入伪根。报告没有混用原逆二项式系统的阶数或分母预算。

## 5. 完整的公共分母下界：为什么本族尚不能证明无理性

以下只讨论 `c∈Q` 的有理 Taylor 系数，包括在反证中假设 `ζ(7)∈Q` 后的真值芽。记 `δ_f(N)` 为 `d_0,…,d_N` 的最小公共分母，`δ_V(N)` 类似。

先证一个全前缀精确等式。对任意素数幂 `q=p^a≤N`，`H_{q-1}^{(4)}` 中各项的 `p` 赋值至少为 `−4(a−1)`。因此

\[
\operatorname{ord}_p([z^q]V)
=\operatorname{ord}_p\left((-1)^q[q^{-6}+5H_{q-1}^{(4)}q^{-2}]\right)=-6a.
\tag{5.1}
\]

第一项赋值为 `−6a`，第二项至少为 `−6a+4`，所以不会相消。另一方面，`n^{-6}` 和 `n^{-2}H_{n-1}^{(4)}` 的分母都整除 `L_N^6`，其中 `L_N=lcm(1,…,N)`。取每个素数的最大幂即得

\[
\boxed{\delta_V(N)=L_N^6\quad\text{对所有 }N\ge1.}
\]

由 (4.3)，`5δ_f(N)` 能清掉 `V` 的前缀系数，故

\[
\boxed{\liminf_{N\to\infty}\frac{\log\delta_f(N)}N\ge6.}\tag{5.2}
\]

这是所有固定有理 `c` 的一般下界，不是几个有限分母的拟合。PNT 用于 `log L_N=N+o(N)`。此处下界是公共前缀口径，不自动构成精细多类型 `τ` 的下界。

也有同一族的严格上界。令 `q_c` 清掉 `c` 的分母，固定 `k≤n`、素数 `p`，设 `r=floor(log_p n)`、`a=ord_p k`。中央二项式的 Legendre 公式为各层 carry 之和：

`ord_p C_m=Σ_{j≥1}(floor(2m/p^j)−2floor(m/p^j))`，每层为 0 或 1。

对 `j≤a`，`C_k` 的 carry 为 0；对 `j>r`，因为 `k≤n<p^j`，`C_n` 的 carry 至少与 `C_k` 一样大。只有 `a<j≤r` 可贡献负差，所以

\[
\operatorname{ord}_p(C_n/C_k)\ge-(r-a).
\]

因此纯 `k^{-7}` 项的赋值至少为 `−r−6a≥−7r`；`H_{k-1}^{(4)}k^{-3}` 项的赋值至少为 `−5r−2a≥−7r`。于是 `L_n^7 C_n Σ_{k≤n}t_k` 整数，固定的 `5/2` 只需另清 2。最终

\[
\boxed{\delta_f(N)\mid2q_cL_N^7},
\quad \limsup\frac{\log\delta_f(N)}N\le7.\tag{5.3}
\]

分子高度亦为至多指数增长，(4.2) 给 holonomicity，所以每个有理 `c` 的芽是 G-function。`6≤` 与 `≤7` 是同一八维提升族的前缀分母口径，未声称 `f_c` 指数的精确值为 6 或 7；`V` 的前缀等式则确为精确的。

固定域 (4.1) 的原点共形半径为 4：`φ_0(w)=4w/(1−w)^2` 把单位盘映到该 slit 域。任何 `φ:D→U_1`、`φ(0)=0` 经其逆映射及 Schwarz 引理给 `|φ'(0)|≤4`。因此

\[
\log|\phi'(0)|-\sigma\le\log4-6<0.
\tag{5.4}
\]

故本族无法通过当前 **scalar/common-prefix** CDT holonomy 的正分母门槛。该结论不排除更细的多类型算术估计、变换后的新几何、真正更低高度的另一族或其他无理性方法；也没有证明 `U_1` 为这个特定解的最大可能延拓域。

## 6. 跨权参数族的闭合桥梁

此处参数 `w` 是权重生成参数，`z` 是函数变量；两者不能混用。

### 6.1 Borwein–Bradley 覆盖 `ζ(4m+3)`

设

\[
a_n(w)=\frac{(-1)^{n-1}}{n^3C_n}
\frac1{1-w/n^4}\prod_{j<n}\frac{1+4w/j^4}{1-w/j^4},
\quad A(z,w)=\sum_{n\ge1}a_n(w)z^n.
\]

经典参数定理给 `(5/2)A(1,w)=Σ_{m≥0}ζ(4m+3)w^m`。直接由相邻项比值，不依赖周期猜想，得到

\[
\boxed{[2(\theta-1)(2\theta-1)(\theta^4-w)
+z(\theta+1)^2(\theta^4+4w)]A=0.}\tag{6.1}
\]

取 `A_m=[w^m]A`，令 `P_0`、`P_1` 分别为括号中 `w^0,w^1` 部分，即

\[
P_0A_0=0,\quad P_0A_m=-P_1A_{m-1}.
\]

所以固定 `m` 的权重截断有 `6(m+1)` 维的显式上界闭合系统。这是上界，不宣称每一块实际独立；第 4 节对 `m=1` 的具体尾提升另证实际 rank 8。

### 6.2 Koecher 提供全部 `ζ(2m+3)` 的真实纯连接

Koecher 恒等式可由 Borwein–Bradley 原稿 §9、公式 (9.1) 核对；该文引用原始 `Math. Intelligencer 2 (1980),62–64`。令

\[
b_n(w)=\frac{(-1)^{n-1}}{n^3C_n}
\frac{\prod_{j<n}(1-w/j^2)}{1-w/n^2},\qquad B(z,w)=\sum b_n(w)z^n.
\]

则

\[
K(z,w)=\tfrac52B(z,w)-\tfrac w2\theta^{-2}B(z,w),
\quad K(1,w)=\sum_{m\ge0}\zeta(2m+3)w^m,
\tag{6.2}
\]

其中 `θ^{-1}` 是取原点常数项为 0 的正则积分。相邻项比值给

\[
\boxed{[2(\theta-1)(2\theta-1)(\theta^2-w)
+z(\theta^2-w)^2]B=0.}\tag{6.3}
\]

固定权重截断因而有有限有理闭合系统；对每个指定 `K_m`，另加 `B_{m-1}` 的两个正则 Euler 积分就得到 (6.2)，`m=0` 不需这些额外项。其参数导数块只可能在 `0,−4,∞` 有奇点，原点指定正则解，故每个固定权 `K_m(z)` 在 `U_4` 全纯。对 `K_m(1)=ζ(2m+3)` 可应用第 3 节的同一真实分支提升。

**此显式全部奇权族的算术边界也可跨权证明。** 对 `r=2m+3≥5`，在项指标 `n=p` 处，`[w^m]` 的唯一最高 `p` 分母来自
`(5-w/p²)/(2(1-w/p²))` 的系数 `2/p^{2m}`；所有 `j<p` 因子在 `p` 处整。乘尾递推的 `pC_p` 后，forcing 的赋值为 `−(r−1)`，除素数 2 外无例外。`r=3` 的常数 `5/2` 仅再排除素数 5。于是各固定有理参数芽的公共前缀分母指数至少为 `r−1`。其共同已证 slit 域仍为 `U_1`，所以该族从 ζ(3) 起即未通过 `log4−(r−1)>0` 的 scalar 门槛。Apéry 成功使用了另一近似族，此边界绝不扩展成“ζ(3) 无法证明”。

## 7. ζ(7) 与 Catalan 的相同桥梁、不同输入

第 3 节是任意普通点周期值的桥梁，因此形式上也适用 Catalan。一个明确纯值输入为

\[
H_G(z)=\sum_{n\ge0}\frac{(-1)^nz^{n+1}}{(2n+1)^2}
=\frac{\sqrt z}{2i}
[\operatorname{Li}_2(i\sqrt z)-\operatorname{Li}_2(-i\sqrt z)],
\quad H_G(1)=G.
\]

该芽在 `C\(-∞,-1]` 正则单值；标准 β(2) 级数与平方根表示在原点一致。二项式尾提升会在 `1/4` 真正消掉平方根 monodromy，但外部已证 cut 从 `−1` 缩至 `−1/4`，共形半径仅为 1。这个通用示例本身没有预算优势，故无需继续数值扫描。

第 4 节的 rank 8、`θU` 的 `1−4z` 因子与分母指数下界 6 不应移植到 Catalan。其输入涉及 `χ_{−4}`、四次单位根及不同权重；BB 逆二项式恒等式是在 ζ 的另一周期系统内。根任务已有更具几何内容的 Catalan 正积分连接族，可作为另一个真实输入；两者可以共同用秩／分母／域测试，但不能共用未经证明的数值独立性或目标纯度。

## 8. 独立精确核验与下一入口

[核验脚本](E:/kimi-build/zeta5/research/odd_zeta_new_period_systems_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_new_period_systems_20261004_verify.json) 不调用数值 ζ，不做参数扫描，检查：

- `n=1,…,12` 的完整有理参数尾递推 (4.3)；
- 相同范围的 `θU`、`θV` Taylor 身份；
- 全部八层 cyclic 系数矩阵的精确三角结构及 (4.6)；
- `p=2,3,5,7,11` 的 forcing 赋值 `−6`；
- `q=4,8,9` 的素数幂赋值及 `N=1,…,12` 的 `δ_V=L_N^6`、目标常数部分分母整除 `2L_N^7`；
- BB 与 Koecher 参数 recurrence 在权参数阶 `0,1,2`、项指标 `2,…,8` 的精确核验。

运行状态：`exact_identities_passed_not_irrationality_proof`。连接身份来自文献定理，解析域与实际函数独立性来自上述证明；有限脚本不替代它们。`paper_mechanism` 分支已独立审阅纯身份、两个实际积分域、真值相消、rank 8 证明、cyclic determinant、跨权 recurrence 及算术层证明，未发现实质错误。

实际新入口已从“能否得到纯值及真实分支相消”推进到“如何改变这个已证 8 维局部系统的算术分母、或寻找具有更好域／分母比的新真实周期”。若仍保留这个公共前缀 forcing，调首一解、局部矩阵或有理参数无法绕过 (5.2)。未来有效改动需改变 forcing 的全算术，或采用适用条件不同的多类型 holonomy；仅提升或制造分支本身不产生所需负预算。
