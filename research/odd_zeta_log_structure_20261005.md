# 对数矩族的合流多重正交、Cauchy 系统与可移植定理范围

日期：2026-10-05。只新增本稿及固定精确证书，不修改冻结的 2026-10-04 报告或 PDF。研究对象是

\[
R_{n,q}(u)=\sum_{r=0}^{qn}(-1)^r
 \binom{qn}{r}\binom{n+r}{n}^{q}u^r,\qquad n,q\ge1.
\]

本轮找到直接覆盖它的合流 Jacobi–Piñeiro 原始定理，并证明两个具体函数结构：全部 Cauchy 分量是标准 polylog 的有理变换；最高分量的实际最小微分阶数恰为 `q+1`。另给一个共同 hypergeometric 方程的对数归一化基本解组。对 `q=7`，这核清了真实秩 8 的来源，但没有取得新的解析域、monodromy 消去或整数化预算优势。本文没有证明 ζ(7) 无理，也没有把 polynomial 实根或多重正交正常性替代指定余项非零。

## 1. 直接适用的合流 Jacobi–Piñeiro 定理

Smet–Van Assche 作者稿 *Mellin transforms for multiple Jacobi-Piñeiro polynomials*，首页 2008-08-06，25 页，Theorem 2.4（印刷页 6）明确处理权

\[
u^\alpha,\quad u^\alpha(-\log u),\quad\ldots,
u^\alpha\frac{(-\log u)^{q-1}}{(q-1)!},\qquad \alpha>-1,
\]

及有序 multi-index `n₁≥⋯≥n_q`。这不是仅把非合流 theorem 的参数形式置相等。取 `α=0`、`n₁=⋯=n_q=n`，将文中的 Mellin 变量 `s` 平移为 `z−1`，准确得到本候选的矩零点。[作者固定 PDF](https://wis.kuleuven.be/analyse/members/walter/mellin.pdf)。

令 `N=qn`。本候选的整数归一化是 `R(0)=1`，而 type-II 首一归一化为

\[
P_{n\mathbf1}(u)=\frac{R_{n,q}(u)}{c_N},\qquad
c_N=(-1)^N\binom{(q+1)n}{n}^{q}.
\]

不能混用两种归一化的高度。独立留数计算给

\[
M(w):=\int_0^1u^{w-1}R(u)\,du
=C\frac{\prod_{j=1}^n(w-j)^q}{\prod_{r=0}^{N}(w+r)},
\quad C=\frac{(-1)^N N!}{(n!)^q}. \tag{1}
\]

于是 `∫u^m(−logu)^j Rdu=0` 对 `0≤m<n、0≤j<q` 成立；这个具体矩问题是一维，已由旧候选稿的分子次数论证证明。

上述 log 权的矩测试空间在 `t=−logu` 下变成 `e^(−mt)t^j`。实指数的重复指数多项式构成扩展 Chebyshev 系统。因此 type-II polynomial 的 `N` 个零点全部单纯且位于 `(0,1)`；独立 Rolle/符号变化证明见[本轮非零报告](E:/kimi-build/zeta5/research/odd_zeta_log_nonzero_20261005.md)。它仅证明多项式实根与正常性。

## 2. 精确 Cauchy 身份：标准 polylog 的有理变换

令 `Ω=C\[0,1]`，对于 `1≤j≤q` 定义实际收敛 Cauchy 函数

\[
f_j(z)=\int_0^1\frac{R(u)}{z-u}
 \frac{(-\log u)^{j-1}}{(j-1)!}\,du.
\]

写 `R(u)=Σ_(r=0)^N c_ru^r`，定义有理系数 polynomial

\[
S_j(z)=\sum_{r=1}^N c_r\sum_{\ell=1}^{r}\frac{z^{r-\ell}}{\ell^j}.
\]

则准确有

\[
\boxed{f_j(z)=R(z)\operatorname{Li}_j(1/z)-S_j(z).} \tag{2}
\]

证明：在 `|z|>1` 逐项展开 `1/(z−u)`。单项积分是

\[
\sum_{m\ge0}\frac{z^{-m-1}}{(m+r+1)^j}
=z^r\left[\operatorname{Li}_j(1/z)
 -\sum_{\ell=1}^{r}\frac{z^{-\ell}}{\ell^j}\right].
\]

有限求和得到 (2)，再由解析延拓推广到 `Ω`。这里的分支由 `|z|>1` 的实 Cauchy germ 确定。

在目标点 `z=−1`，有

\[
f_q(-1)=-I_q(R),\qquad
I_q(R)=R(-1)\eta(q)+S_q(-1),
\quad \eta(q)=\sum_{m\ge1}\frac{(-1)^{m-1}}{m^q}. \tag{3}
\]

`q=1` 时 `η(1)=log2`；对 `q≥2` 才用 `η(q)=(1−2^(1−q))ζ(q)`。`S_q(−1)` 与整数除法 `R=(1+u)Q+R(−1)` 的 rational boundary 完全相同。`q=7` 时 ζ(7) 系数是 `63R(−1)/64`。

式 (2) 给出具体同时 Padé 解释：`R` 是共同 denominator，`S_j` 是 `R Li_j(1/z)` 的 polynomial part，每个 remainder `f_j` 在无穷远消前 `n` 项。它不是一个只在形式动机商里执行的目标投影。

但 (2) 也说明，这个函数族仍处于标准 polylog 的同一解析域。次数增加改变的是 rational gauge、height 和 endpoint remainder，没有改变标准 polylog connection 的几何。

## 3. 实际函数秩、闭合系统与可检验的 cyclic determinant

**命题。** 对每个固定 `n,q`，`1,f₁,…,f_q` 在 `C(z)` 上线性独立，并形成一个 `q+1` 维的有理闭合一阶系统；单个 `f_q` 的最小齐次微分方程阶数准确为 `q+1`。

证明首先从标准向量 `Y=(1,Li₁(1/z),…,Li_q(1/z))ᵀ` 出发。其系统为

\[
\frac d{dz}\operatorname{Li}_1(1/z)=-\frac1{z(z-1)},
\qquad
\frac d{dz}\operatorname{Li}_j(1/z)=-\frac1z\operatorname{Li}_{j-1}(1/z)
\quad(j\ge2).
\]

它在 `C(z)` 上独立：绕 `z=1` 的 monodromy 将第 j 个 polylog 增加非零固定常数乘 `(-logz)^(j−1)/(j−1)!`。任何 rational-coefficient 关系因而给 `logz` 的 rational-coefficient polynomial 关系。`logz` 的无限加性 monodromy 迫使这些系数逐个为零，剩余常数方向也为零。这个论证没有假定 ζ(7) 或任何端点值无理。

由 (2)，从 `Y` 到 `F=(1,f₁,…,f_q)ᵀ` 的 rational gauge `T` 的对角为 `1,R,…,R`，第 j 行首项为 `−S_j`，故 `detT=R^q≠0`。这证明函数独立。置 `r_R=R′/R`，其闭合系统准确为

\[
f_1'=r_R f_1+
 \left(r_RS_1-S_1'-\frac{R}{z(z-1)}\right),
\]
\[
f_j'=r_R f_j-\frac{f_{j-1}}z+
 \left(r_RS_j-S_j'-\frac{S_{j-1}}z\right),\qquad2\le j\le q. \tag{4}
\]

新增 `R` 的零点是 rational gauge 的 apparent singularities；它们全部在已排除的 `[0,1]` 上。这没有给外域扩张。清 gauge 分母也依赖 `R`，不能作为免费的低高度变换。

为证明单目标 cyclic rank，令 `θ=z d/dz`、`b=S_q/R`。对 `j<q` 有

\[
\theta^j(f_q/R)=(-1)^j\operatorname{Li}_{q-j}(1/z)-\theta^j b,
\]

而

\[
H:=\theta^q(f_q/R)=\frac{(-1)^q}{z-1}-\theta^q b\ne0. \tag{5}
\]

非零理由是 (1) 的 `w→∞` 项给

\[
R(1)=C=\frac{(-1)^N N!}{(n!)^q}\ne0.
\]

所以 `b` 在 `z=1` 正则；(5) 的 simple pole 无法被抵消。前 q 个导数逐次给全部 q 个 polylog 方向，第 q 阶给非零 rational 方向。因此 `f_q` 在 (4) 中是 cyclic，最小阶数为 `q+1`。

更具体地，以列基 `1,Li₁,…,Li_q` 表示行 `D^j f_q`，`0≤j≤q`，其 determinant 准确为

\[
\boxed{\det\mathcal C_q(z)
=\frac{R(z)^{q+1}}{z^{q(q+1)/2}}
 \left[\frac1{z-1}-(-1)^q\theta^q\left(\frac{S_q}{R}\right)\right].} \tag{6}
\]

证明：先对 `f_q/R` 使用 θ-jets，矩阵反向三角，det 为 `(-1)^q H`；再乘回 R，行变换为三角且对角全为 R；从 θ-jets 换成 D-jets 再除 `z^[q(q+1)/2]`。证毕。

对 `q=7`，这是真实函数秩与单目标微分阶数 8。它来自标准 Li 系统的有理变换，与前轮 BB/Hadamard 新芽的 8 维系统是不同构造；两者的域、denominator sequence 和整数化表不能混用。这里也没有从函数秩推出数值 `1,ζ(7)` 独立。

## 4. 一个共同 hypergeometric 标量方程及完整对数解组

由系数准确写成

\[
R(z)={}_{q+1}F_q\left(
 \begin{matrix}-qn,n+1,\ldots,n+1\\1,\ldots,1\end{matrix};z\right).
\]

因而满足

\[
\boxed{\mathcal L_{n,q}R=0,\qquad
\mathcal L_{n,q}=\theta^{q+1}-z(\theta-qn)(\theta+n+1)^q.} \tag{7}
\]

非合流 Jacobi–Piñeiro 的相应 scalar equation 与经过 `z^(−α_j)` 归一化的 second-kind 函数关系已见 Lysov 2019 §2，Eq.(8)–(10)；其随后 Theorem 1 的双积分式限于两个权。[出版原件](https://www.mathnet.ru/php/getFT.phtml?jrnid=pa&option_lang=eng&paperid=274&what=fullt)。下面直接证明本合流族的完整归一化，避免在 α 相等处套非合流基底。

取一个固定 `logz` 分支，令

\[
G_\varepsilon(z)=z^{-\varepsilon}
 \int_0^1\frac{u^\varepsilon R(u)}{z-u}\,du,
\qquad g_j(z)=[\varepsilon^j]G_\varepsilon(z),\quad 0\le j<q.
\]

则

\[
\boxed{g_j=(-1)^j\sum_{\ell=0}^{j}
 \frac{(\log z)^{j-\ell}}{(j-\ell)!} f_{\ell+1},
\qquad \mathcal L_{n,q}g_j=0.} \tag{8}
\]

证明：连续 Mellin 递推由 (1) 直接得

\[
(w+qn+1)(w-n)^qM(w+1)=w^{q+1}M(w). \tag{9}
\]

在 `|z|>1` 展开
`Gε=Σ_(m≥0)M(ε+m+1)z^(−ε−m−1)`，(9) 消去 (7) 作用后的全部内部系数；唯一外边界 source 是

\[
\mathcal L_{n,q}G_\varepsilon
=(\varepsilon+qn+1)(n-\varepsilon)^q
 M(1+\varepsilon)z^{-\varepsilon}. \tag{10}
\]

`M(1+ε)` 有 q 阶零，故 ε 的前 q 个系数给 (8)。

矩消元又使 `Gε` 的前 n 个 Laurent 系数在 ε 的前 q 阶全为零；首个非零项来自 `M(n+1)≠0`。于是 `g_j` 在无穷远的首项为 `z^(−n−1)` 乘 degree j 的 `logz` polynomial，其最高系数为 `(-1)^j M(n+1)/j!`。R 的首项则是 `c_Nz^N`。这些不同 log 阶及幂次证明 `R,g₀,…,g_(q−1)` 为 (7) 的基本解组。

需要区分两套结构：基本解组是同一个 scalar equation 的不同解；(4) 是具体函数向量的一阶闭合系统。单独 `f_q` 一般不满足 (7)，它是 (8) 基本解的 log 混合。它仍由 §3 证明有最小阶数 `q+1`，但那个标量算子可不同。不能把某个 `g_j` 的强渐近主项直接当作 `f_q(−1)` 的主项；在 `z=−1` 上 `logz=±iπ`，多个分量可能发生真实相消。

## 5. 真正强渐近文献的参数匹配与缺口

本轮已读下列 primary 版本。表中“不能直接套”是核具体 theorem 假设的结论，不宣称所有文献均不存在所需结果。

归档原件：[Smet–Van Assche](E:/kimi-build/zeta5/literature/smet_vanassche2008_mellin_author.pdf)、[Lysov](E:/kimi-build/zeta5/literature/lysov2019_jacobi_pineiro_integral_representations.pdf)、[Neuschel–Van Assche](E:/kimi-build/zeta5/literature/neuschel_vanassche2016_zero_distribution_v2.pdf)、[Kalmykov–Lysov–Shukla](E:/kimi-build/zeta5/literature/kalmykov_lysov_shukla2026_jacobi_pineiro_asymptotics_v1.pdf)、[Wolfs](E:/kimi-build/zeta5/literature/wolfs2024_multiple_orthogonal_hypergeometric_v2.pdf)、[Fidalgo Prieto–López Lagomasino](E:/kimi-build/zeta5/literature/fidalgo_lopez2010_nikishin_perfect_v1.pdf)。精确版本、来源与原字节 SHA-256 见[归档 manifest](E:/kimi-build/zeta5/literature/manifest_log_moment_20261005.json)。

| 原始 theorem / 输入 | 已证明对象与假设 | 本候选的匹配结果 |
|---|---|---|
| Smet–Van Assche 2008, Th.2.4 | 合流 log 权、α>−1、有序指标；type-II Mellin 因式 | 完全匹配 `(n,…,n),α=0`；没有给指定 Cauchy 端点的强渐近或非零 |
| Lysov 2019, Th.1；§3 Eq.(11)–(14) | 两权、`α₁−α₂∈(0,1)` 的 second-kind 分离及 contour/负实轴积分；辅助解域排除 `(−∞,0]` | 提供正确的解组分离模板；q=7、参数合流需另证，目标 −1 位于辅助负轴上 |
| Neuschel–Van Assche, 1509.04542v2, Th.1.1 | 一般 r 的 diagonal type-II 零点分布；正常性/nearest-neighbor recurrence 的非整数参数差设置 | 即使补合流极限，也只是 polynomial 零点分布，不给最高 Cauchy component 的相消或固定端点非零 |
| Kalmykov–Lysov–Shukla, 2608.20594v1, Th.7.1 | 两权，非整数 α 差，β=0，固定 `θ=n₂/(n₁+n₂)∈(0,1/2)`；polynomial 外域强渐近 | 三个不同缺口：r=7、α 合流、diagonal θ=1/2；不能仅连续代入，更未核最高 Cauchy 混合 |
| Wolfs, 2401.08312v2, Th.5.9–5.10 | explicit hypergeometric Hermite–Padé 的数值 Q 独立，严格 `p<q` 的 factorial 余裕 | 本 polylog 接口是 `p=q`，该文 §5.2 明确排除直接推移；失去 factorial 余裕，需要重新分析几何指数与算术 |

[Neuschel–Van Assche 固定 v2](https://arxiv.org/pdf/1509.04542v2)，[Kalmykov–Lysov–Shukla 固定 v1](https://arxiv.org/pdf/2608.20594v1)，[Wolfs 固定 v2](https://arxiv.org/pdf/2401.08312v2)。

Wolfs 的 polylog 边界说明尤其直接：Theorem 5.10 在 `p<q` 下包含重复零参数，但令 `p=q,z=−1` 虽会形式输出 log2 和各 ζ 值，原证明已不成立。不能将其 E-function 范围的 Q 独立改成 ζ(7) 的指定单值结论。这里引用的是作者明确限定的范围。

同样，外域 polynomial 强渐近或 weak root asymptotics 可计算目标系数 `R(−1)` 的增长，却不能单独计算 (3) 的 rational boundary 与目标值之间的微小或振荡相消。

## 6. Nikishin 与正 Cauchy 余项：为何原假设不能省略

Fidalgo Prieto–López Lagomasino *Nikishin systems are perfect*，固定 `1001.0554v1`：Th.1.5 要求实际 Nikishin generating measures、正则性、quasi-regular 支持及指定指标比例，给 logarithmic asymptotics；Th.1.6 的 ratio asymptotics 还有其真实支持/外域条件。不能仅因为一个测试空间是 AT-system 就调用这些 Nikishin 渐近结论。[原件](https://arxiv.org/pdf/1001.0554v1)。

本 log 权各自为正，仍不自动等于所需的 successive Nikishin product。一个具体问题是

\[
-\log x=\int_0^\infty
 \left(\frac1{x+t}-\frac1{1+t}\right)dt.
\]

它是经过常数减除的无限质量负轴 Markov 表达；必须证明 admissible measure、有限矩和端点/无穷远预算，不能省去减除项。更高 log 权的 literal ratio 也没有固定 Pick 符号：例如

\[
\operatorname{Im}\frac{(-\log z)^2}{2}
=\arg z\,\log|z|,\qquad0<\arg z<\pi,
\]

在上半平面随着 `|z|` 跨 1 变号；它不能直接是非零固定符号实测度的单个 Cauchy transform 加实常数。这只排除该 literal 识别，不排除重新排序、变换后的 Nikishin 实现。

在已知两权分离中，新增支持位于 `(−∞,0]`，目标 `−1` 在其上。相应辅助 second-kind 分量的外域结论不能当作这个点的 nonoscillatory 结论。Lysov 的 Eq.(11) 明确引入不同的分离余项，也不能把它与原某一个 remainder 混同。

本轮非零分支已经严格认证 `I₇(R₁,₇)<0`、`I₇(R₈,₇)>0`，并证明 Euler 伴随核变号。因此“所有 polynomial 实根在 (0,1)，故最高 Cauchy 余项固定号”的推理已有实际反例。该分支另证明 `7n−1` 为素数的无穷子序列中至多有限个端点为零；它是算术局部论证，本文已独立核通过，不能反过来冒称文献中的正 Cauchy theorem。[本轮报告](E:/kimi-build/zeta5/research/odd_zeta_log_nonzero_20261005.md)。

## 7. Meijer G 表达与 saddle 曲线的真实作用

每个基础 log 权都有正 Mellin 表达

\[
\int_0^1u^{w-1}\frac{(-\log u)^{j-1}}{(j-1)!}du
=w^{-j}=\frac{\Gamma(w)^j}{\Gamma(w+1)^j}.
\]

它也是 j 个 uniform `[0,1]` 权的 Mellin convolution。反之，本 polynomial 的 Mellin 因式可写为

\[
M(w)=C\frac{\Gamma(w)^{q+1}}
 {\Gamma(w-n)^q\Gamma(w+qn+1)}. \tag{11}
\]

因此用 Mellin inversion/解析延拓可作一个 `G_(q+1,q+1)^(q+1,0)` 表达，upper parameters 为 `−n` 重复 q 次及 `qn+1`，lower parameters 全为 0。负 upper shift 与实际 polynomial 变号不能被误判为 positive beta convolution。式 (11) 提供 contour/saddle 分析的输入，没有单独给正核、非零或小整数型。

对 (7) 作尺度主符号 `θ≈ny`，得到代数曲线

\[
\boxed{y^{q+1}=z(y-q)(y+1)^q.} \tag{12}
\]

在 `z=−1` 的唯一正解 `t∈(0,q)` 满足
`(q−t)(1+t)^q=t^(q+1)`。它与正项 sum `B_n=R(−1)` 的唯一实 entropy saddle 相同。具体而言

\[
F_q(t)=q\log q-t\log t-(q-t)\log(q-t)
 +q[(1+t)\log(1+t)-t\log t],
\]

`F_q′=log[(q−t)(1+t)^q/t^(q+1)]`，`F_q″<0`，在 saddle 上
`F_q(t)=q log[q(1+t)/(q−t)]`。本轮算术报告证明这个正项 sum 的真实增长及常数；本文只核其与 (12) 的关系，未将 B 的指数当作 `I₇` 的余项指数。[算术报告](E:/kimi-build/zeta5/research/odd_zeta_log_arithmetic_20261005.md)。

对于最高 Cauchy component，多个复 saddle 或 log-normalized 解的系数可能相消。需要根分支的实际 Mellin–Barnes contour、相位和尾部分析，不能只选 (12) 的一个 real branch。

## 8. 新的可直接使用输入、证书与归档范围

本稿可直接交付的是 (2)–(10)：完整 Cauchy/polylog 身份、有理一阶系统、函数独立、单目标最小阶数和 cyclic determinant，以及 hypergeometric 基本解组。这些是针对实际候选的全 n,q 命题，不是只有“存在某个完美系统”的充分判据；也不声称全局新颖。

固定[脚本](E:/kimi-build/zeta5/research/odd_zeta_log_structure_20261005_verify.py)／[JSON](E:/kimi-build/zeta5/research/odd_zeta_log_structure_20261005_verify.json) 已通过 `(n,q)=(1,2),(1,3),(1,7)` 三个指定例：polynomial ODE、Mellin 递推、source 的准确 q 阶零、Sturm 实根、完整 rational gauge 及目标有理项；前两例还核全部 g_j 的 scalar ODE 和实际 cyclic determinant 的符号/常数。没有 ζ 值调用、参数扫描或用样本代替函数独立证明。

新增 primary 原件已给根任务，由根统一归档；本分支不另下载或修改 literature 索引：

- Smet–Van Assche：作者 `mellin.pdf`，首页 2008-08-06，25 页；发表版本为 J.Approx.Theory 162(2010),782–806，标题另含 *and a q-analogue*。作者稿与发表版本不能混为同一版本。[作者 PDF](https://wis.kuleuven.be/analyse/members/walter/mellin.pdf)。
- Lysov：出版原件 2019，13 页，Probl.Anal.Issues Anal.8(26):3,83–95，DOI `10.15393/j3.art.2019.6830`。[PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=pa&option_lang=eng&paperid=274&what=fullt)。
- Neuschel–Van Assche：`1509.04542v2`，arXiv 页记录 2016-01-07，19 页；PDF 首页另显示作者稿 2018-08-15，归档时两项时间戳均应保留，不能自行断言哪项是另一次 arXiv 修订。[PDF](https://arxiv.org/pdf/1509.04542v2)。
- Kalmykov–Lysov–Shukla：`2608.20594v1`，2026-08-20，56 页；已核 Th.7.1 的具体非合流两权范围。[PDF](https://arxiv.org/pdf/2608.20594v1)。
- Wolfs：`2401.08312v2`，2024-04-16，39 页；Th.5.10 的 `p<q` 必须保留。[PDF](https://arxiv.org/pdf/2401.08312v2)。
- Fidalgo Prieto–López Lagomasino：`1001.0554v1`，2010-01-04，39 页；本轮核其 Th.1.5 的实际 generating measures/regularity 条件。[PDF](https://arxiv.org/pdf/1001.0554v1)。

没有发现可直接覆盖本 `q=7,α=0,diagonal,z=−1` 最高 Cauchy component 的现成 nonoscillatory strong-asymptotics theorem。这个陈述限于本轮明确审阅的来源。指定余项的实际渐近与整数化成本由另外分支独立推进。
