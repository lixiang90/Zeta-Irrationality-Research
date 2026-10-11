# Catalan 曲线的端点 Bloch 类：有限平均、数域下降与近似缺口

日期：2026-10-04。本稿继续[上一轮椭圆商构造](odd_zeta_cover_elliptic_quotients_20261004.md)，使用本轮已证的[整数关系 \(4T=0\)](odd_zeta_k2_descent_20261004.md)及[开放路径恒等式](odd_zeta_k2_regulator_20261004.md)。这是该具体构造的书面推导；没有新增 Lean 定理，没有证明 Catalan 或 ζ(7) 无理。

经有限平均得到的端点差，在数域 Bloch 群有理化中恰为 \(-4[i]\)。这个结构识别将候选绝对椭圆类转回经典端点类；尚未给出有限五项式分解的显式清单，也未产生新的无理性定理。

## 1. Bloch 群与非零经典输入

对域 \(M\)，令 \(\mathcal P_2(M)\) 为由 \([z]\), \(z\ne0,1\)，模标准五项关系生成的 pre-Bloch 群。使用有理复形

\[
\mathcal P_2(M)_{\mathbb Q}
 \xrightarrow{\delta}\bigwedge^2(M^\times\otimes\mathbb Q)
 \longrightarrow K_2^M(M)_{\mathbb Q}\longrightarrow0,
\qquad \delta[z]=z\wedge(1-z).
\tag{1.1}
\]

它在中间项正合，来自 Milnor \(K_2\) 的 Steinberg 表示。记
\(B(M)_{\mathbb Q}=\ker\delta\)。不同整数 Bloch 定义的有限挠差别在有理化后消失；本稿主识别是**有理类等式**。

为另行说明整数 cycle，采用 Suslin 的 antisymmetric tensor 目标，
其关系为 \(a\otimes b+b\otimes a=0\)，不混用整数 exterior 归一化。
在 \(F=\mathbb Q(i)\) 上，

\[
\delta(4[i])=4\,i\otimes(1-i)=i^4\otimes(1-i)=0.
\tag{1.2}
\]

因此 \(4[i]\) 是整数 Bloch cycle，而 \([i]\) 在有理化后是 cycle。
Bloch–Wigner 的约定为

\[
D(z)=\operatorname{Im}\operatorname{Li}_2(z)+\log|z|\arg(1-z),
\quad dD(z)=\eta(z,1-z),
\quad \eta(f,g)=\log|f|d\arg g-\log|g|d\arg f.
\tag{1.3}
\]

由 \(|i|=1\) 与绝对收敛级数，

\[
D(i)=\sum_{m\ge0}\frac{(-1)^m}{(2m+1)^2}=G>\frac89.
\tag{1.4}
\]

故 \(4[i]\) 非挠。这是经典事实，不是本项目的新发现。
定义与 \(K_3^{\rm ind}\) 的关系见
[Suslin 原件](../literature/suslin1991_k3_field_bloch_group_english.pdf) Theorem 5.2；
实函数与数域总调节子见
[Zagier–Gangl](../literature/zagier_gangl2000_classical_elliptic_polylogarithms.pdf) §1，
及[Neumann–Yang](../literature/neumann_yang1997_rationality_k_theory_v1.pdf) §2。
这些结果没有断言 \(D(i)\) 无理。

## 2. 零 \(K_2\) 类产生有限 Bloch 链

设 \(K=F(a)\), \(a=\sqrt2\)，
\(C:Y^2=s^8-14s^4+1\)。将上一轮 \(u_\pm,F_\pm\) 拉回 \(C\)，仍用原名称，令

\[
w=u_+\wedge F_+ +u_-\wedge F_-
\in\bigwedge^2(K(C)^\times\otimes\mathbb Q).
\tag{2.1}
\]

由 \(T_{\mathbb Q}=0\) 与 (1.1)，存在一个**有限**链
\(\varepsilon_0=\sum_jq_j[h_j]\)，\(\delta\varepsilon_0=w\)。
目前未列出其具体 \(q_j,h_j\)。

在有限 formal chain 本身做平均，再取五项关系商。定义

\[
\sigma(s,Y)=(-s,Y),\quad
\tau(s,Y)=(s^{-1},Y/s^4),\quad
\alpha(a)=-a,\quad\alpha(i)=i,
\tag{2.2}
\]

其中 \(\alpha\) 固定 \(s,Y\)。三者两两交换，且

\[
\sigma w=\tau w=\alpha w=w.
\tag{2.3}
\]

\(\sigma\) 同时反演每个商的 \(u,F\)；
\(\tau\) 固定正商、同时反演负商的 \(u,F\)；
\(\alpha\) 同时反演两个商的 \(u,F\)。
这些等式已在 wedge 中成立。因此

\[
\varepsilon=\frac18
 \sum_{g\in\langle\sigma,\tau,\alpha\rangle}g\varepsilon_0
\tag{2.4}
\]

仍有 \(\delta\varepsilon=w\)，并在三者作用下逐项形式地不变。
分母 \(8\) 是固定代价，不能误写为随逼近尺度增长的整性节省。

## 3. 端点评价局部引理

设点 \(P\) 的残域为 \(M\)。对所选 finite chain 定义普通点值

\[
{\rm ev}_P[h]=
\begin{cases}
[h(P)],&h(P)\notin\{0,1,\infty\},\\
0,&h(P)\in\{0,1,\infty\}.
\end{cases}
\tag{3.1}
\]

这不是把有零、极的 \([h]\) 替换为 \([{\rm lead}(h)]\)。
取局部参数 \(t\)，写 \(h=t^mu\)，用乘法映射
\(\ell_t(h)=\bar u\) 仅验证 boundary：

- \(m>0\) 时，\(\ell_t(1-h)=1\)，wedge 为零；
- \(m<0\) 时，\(\ell_t(1-h)=-\ell_t(h)\)，wedge 在有理化后为零；
- \(m=0,\bar u=1\) 时，\(\ell_t(h)=1\)，仍为零；
- \(h(P)\ne0,1,\infty\) 时，两函数为单位，得到 \(\delta[h(P)]\)。

若 \(w\) 的函数在 \(P\) 都是单位，则

\[
\delta({\rm ev}_P\varepsilon)
   =(\ell_t\wedge\ell_t)w.
\tag{3.2}
\]

特别地，右侧为零就得到 \(B(M)_{\mathbb Q}\) 中的端点类。
式 (3.1) 不依赖参数，与域及曲线同构等变。
这里只证明所需 finite-chain 评价性质，未宣称 naive 点值是整个整数 pre-Bloch 群的无条件 specialization。

取

\[
P_0=(0,1),\qquad B=(s_0,0),\qquad
s_0=\frac{\sqrt6-\sqrt2}{2}=\sqrt{2-\sqrt3}.
\tag{3.3}
\]

在 \(P_0\)，\(u_\pm=1,F_\pm=-1\)，故 \(w(P_0)=0\)。
在 \(B\)，

\[
(u_+,F_+)=(2+\sqrt3,1),\qquad
(u_-,F_-)=(i,-1),
\tag{3.4}
\]

故 \(w(B)=0\) 在有理 wedge 中成立。
\(F_+(B)=1\) 是实际正则函数值：在正商 \((x,y)=(\sqrt6,0)\)，
\(y\) 是局部参数，\(x-\sqrt6\) 为二阶，\(r_+=O(y^2)\)，
故 \((y-r_+)/(y+r_+)\to1\)。不能直接代入 \(0/0\)。
两端全部 \(u,F\) 都是局部单位。

令 \(L=F(a,b)\), \(b=\sqrt3\)。由局部引理得到

\[
\beta_0={\rm ev}_{P_0}\varepsilon\in B(K)_{\mathbb Q},\quad
\beta_B={\rm ev}_{B}\varepsilon\in B(L)_{\mathbb Q},\quad
\beta=\beta_B-{\rm res}_{L/K}\beta_0\in B(L)_{\mathbb Q}.
\tag{3.5}
\]

\(D\) 在 \(0,1,\infty\) 连续取零，端点评价与实函数极限一致。
沿原实路径 \(\gamma:P_0\to B\)，在有限 support 之外
\(dD(\varepsilon)=\eta_T\)。分段积分并用连续性消去中间端点，得到

\[
D(\beta)=\int_\gamma\eta_T=-4G.
\tag{3.6}
\]

它来自具体 \(w\) 的零类，而非任意把 \([i]\) 插入链中。

## 4. 四个嵌入给精确识别与下降

\({\rm Gal}(L/F)\cong(\mathbb Z/2)^2\)，生成元为
\(\alpha:a\mapsto-a\)、\(\nu:b\mapsto-b\)。
由 (3.3)，

\[
\alpha(B)=\sigma B,\qquad \nu(B)=\sigma\tau B.
\tag{4.1}
\]

前者是 \(s_0\mapsto-s_0\)，后者是
\(s_0\mapsto-(\sqrt6+\sqrt2)/2=-1/s_0\)。
链的系数与函数仅在 \(K(C)\)，所以 \(\nu\) 对链不动；
其余不变性来自 (2.4)。普通端点评价的等变性遂给
\(\alpha\beta_B=\nu\beta_B=\beta_B\)。
在 \(P_0\)，\(\alpha\) 固定点且固定平均链，\(\nu\) 固定 \(K\)，
所以 \({\rm res}\beta_0\) 也不变。
因此 \(\beta\in B(L)_{\mathbb Q}^{{\rm Gal}(L/F)}\)。

现在 \([L:\mathbb Q]=8\)、\(r_2(L)=4\)。选择四个固定 \(i\) 的复嵌入
\(\iota_1,\ldots,\iota_4\)，Borel–Suslin 总调节子

\[
\mathcal R_L:B(L)_{\mathbb Q}\longrightarrow\mathbb R^4,\quad
z\longmapsto(D(\iota_1z),\ldots,D(\iota_4z))
\tag{4.2}
\]

为单射。准确的数域版本见
[Neumann–Yang](../literature/neumann_yang1997_rationality_k_theory_v1.pdf) §2 的 Borel theorem；
其 Proposition 2.1 也给有理 Galois 下降。
\(\beta\) 的不变性给

\[
\mathcal R_L(\beta)=(-4G,-4G,-4G,-4G),\qquad
\mathcal R_L(4[i])=(4G,4G,4G,4G).
\tag{4.3}
\]

全部坐标相消，故

\[
\boxed{\ \beta=-4\,{\rm res}_{L/F}[i]
\quad\text{在 }B(L)_{\mathbb Q}\text{ 中}.\ }
\tag{4.4}
\]

这同时证明 \(\beta\) 来自 \(B(F)_{\mathbb Q}\)，无需选择整数 Bloch transfer
归一化，也没有仅凭单个实坐标识别高秩 \(B(L)\)。
任何最初链 \(\varepsilon_0\) 经同样平均后都得到 (4.4)，故该端点差与最初选择无关；
未平均的一般端点类不在此结论范围。

这是本 Catalan 开路径在经典数域 Bloch 端点类中的识别，不否定曲线存在其他真正的
非零椭圆 \(K_2\) 类，也不推广到任意路径、任意迭代积分。

## 5. 固定调节子整格的近似障碍

非零类已经明确，但“非零、整性、下降”不能自动给无理性。
设固定整数类群 \(\Gamma\) 的调节子像为离散格
\(\Lambda\subset\mathbb R^d\)。
则所有非零完整调节子向量均满足

\[
\|{\rm reg}(\xi)\|\ge
\min\{\|\lambda\|:\lambda\in\Lambda,\lambda\ne0\}>0.
\tag{5.1}
\]

因此固定整格内的非零完整向量不可能趋于零。
秩一 \(B(F)\) 的像形如 \(\lambda\mathbb Z\)，非零值至少为 \(|\lambda|\)。
高秩群的单坐标投影可以稠密，式 (5.1) 不能排除该投影的逼近。
若允许的格或分母随 \(n\) 改变，本引理也不能直接套用。

目标形式却需要

\[
L_n=q_nG-p_n,\quad p_n,q_n\in\mathbb Z,\quad
0<|L_n|\to0.
\tag{5.2}
\]

固定 \(B(F)\) 中的 \(k_n[i]\) 只给 \(k_nG\)；
五项关系及有限平均没有提供有理方向 \(p_n\)。
非零秩一实格容许生成元是有理数，所以格非零不排除 \(G\in\mathbb Q\)。

奇数 ζ 的高权 Borel 周期同样需要目标与有理方向之间的定量分离。
这不是所有高深方法的不可行性定理；这里只排除在固定完整整格中
直接寻找非零小调节子向量的操作。

## 6. 已填补的缺口与可检验接口

本轮补上了绝对候选类的退化判定、端点类存在、有限平均下降及经典 Catalan 类识别。
[垂直 tame 报告](odd_zeta_k2_vertical_20261004.md)另证明所选适当正则模型上全部
水平、垂直 tame 为一；因 \(4T=0\)，不能把它升级为非挠性。

下一步相对 Bloch 链参数族必须交付：

1. 实际有限 \(\varepsilon_n\) 及 boundary、端点、分支恒等式；
2. 从端点式提取 \(q_nG-p_n\) 或 ζ(7) 的纯目标线性型，并证明真实整数结构；
3. 非零性，以及衰减胜过清分母成本：若原余项为
   \(e^{-\rho n+o(n)}\)、整数化倍率为 \(e^{dn+o(n)}\)，必须有 \(\rho>d\)。

目前尚无满足三项的参数族。显式化 \(\varepsilon_0\) 可帮助发现端点操作，
单独重写 \(-4[i]\) 不会增加周期的算术信息。
对 ζ(7)，应把“退化预检—相对边界—整数预算”的顺序用于真正高权构造，
不能将本权二 Bloch 证明直接称作 ζ(7) 高权公式。

## 7. 复核范围

[精确证书](odd_zeta_bloch_boundary_20261004_verify.json)核查数域次数、
四个端点共轭、两个商端点值、正商局部阶数以及四个固定 \(i\) 的嵌入。
局部引理、Steinberg 正合性及 Borel 单射由上述书面证明与原件支持；
有限计算不替代它们。关键平均、普通端点评价及全部嵌入识别已经独立复核；
证书不宣称证明无理性或新增 Lean 形式化。

