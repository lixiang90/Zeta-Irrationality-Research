# 第242轮：固定K5外层素数的完整秩一内容界

2026-10-09，C。固定240的完整对象，不改变列池或泛函。本稿证明 p>n 的全部系数 Gauss 下界，尤其把3n<p≤5n的重复调和头变成有限秩一更新。数学程序0；没有素数、参数或小阶矩阵扫描。下界仍是费用 upper，未证明全预算<6，未把不足的 upper 当作 no-go。

## 1. 对象与完整有理矩

写 D_m(t)=∏_(j=1)^m(t+j)，R_n=D_n⁴/D_(5n)，h=3n，S_n=(5n)!/(n!)⁴，F_n=∏_(i=0)^(3n−1)(i!)²。泛函固定为
\[
 U_T(f)=\tfrac32V_1(tf)+\tfrac1{24}V_3(tf)+a(f)T,
 \quad V_r(P+\sum c_j/(t+j))=B^+(P^{(r)})+(r+1)!\sum c_jH_j^{(r+2)},
\]
其中 a(f)=−Σc_j。定义 M_n(T)=[U_T(t^(i+k)R_n)]_(0≤i,k<h)，Q_n=det M_n，Qtilde_n=S_n^h Q_n/F_n。这正是241已证无限关系点非零的同一完整多项式；本轮不重算该证书。

令 λ_j=Res_(t=−j)R_n，t^eR_n=q_e(t)+Σ_j λ_j(−j)^e/(t+j)。q_e∈Z[t]，且 deg(tq_e)≤5n−1（完整池 e≤6n−2）。tf的部分分式常数项 Σ_jλ_j(−j)^e被 V_1、V_3 消掉，但多项式 tq_e 的全部导数矩仍保留。故
\[
 U_T(t^eR_n)=L_e+\sum_{j=1}^{5n}j\lambda_j(-j)^e(T-3H_j^{(3)}-H_j^{(5)}),
 \quad L_e=\tfrac32B^+((tq_e)')+\tfrac1{24}B^+((tq_e)'''). \tag{O1}
\]
整数首一除法及完整残数公式给
\[
 \omega_j:=S_nj\lambda_j
 =(-1)^{j-1}j^2\binom{5n}{j}\binom{j-1}{n}^{4}\in Z. \tag{O2}
\]
j≤n时残数为0。下面不删任何 j>p 的头，也不只保留 j=p。

## 2. 所有p>n的精确共同头分解

固定素数 p≥7、n<p≤5n。令 s=⌊5n/p⌋∈{1,2,3,4}，τ=5n−sp，0≤τ<p。由于5n<5p<p²，v_p(S_n)=s。von Staudt–Clausen给每个 Bernoulli 数的 valuation≥−1；固定2、24为p单位，所以 S_nL_e∈Z_p，即使商部的 Bernoulli 指数超过p−1。这一步不假设 V_3 杀掉整个商部。

对于 j≤5n，m_j=⌊j/p⌋≤4，有严格恒等式
\[
 H_j^{(r)}=p^{-r}H_{m_j}^{(r)}+\eta_{j,r},\qquad\eta_{j,r}\in Z_p,\quad r=3,5. \tag{O3}
\]
它来自分开求和中的全部 p 的倍数；因 j<p²，没有更深的倍数。设 v_j=((−j)^i)_(0≤i<h)，以及
\[
 W(T)=[S_nL_{i+k}]_{i,k}+\sum_{j=1}^{5n}\omega_j
       (T-3\eta_{j,3}-\eta_{j,5})v_jv_j^t\in M_h(Z_p[T]).
\]
那么完整矩阵精确等于
\[
 S_nM_n(T)=W(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,
 \quad\gamma_j=-p^{-5}\omega_j
       (H_{m_j}^{(5)}+3p^2H_{m_j}^{(3)}). \tag{O4}
\]
此式同时保留商部与全部 T 系数；不需要无穷形式级数的泛函连续性。m_j≤4使括号p整，故 v_p(γ_j)≥v_p(ω_j)−5。

在残数类 a∈{0,…,p−1} 中写 j=mp+a、m≥1。由 factorial valuation（所有 factorial 的参数<p²）可直接得到
\[
 v_p\binom{5n}{mp+a}=[a>\tau],\qquad
 v_p\binom{mp+a-1}{n}=[1\le a\le n],
\]
\[
 \nu_a:=v_p(\omega_{mp+a})
   =2[a=0]+[a>\tau]+4[1\le a\le n]. \tag{O5}
\]
这里 a=0 时 j=mp 只含一层p，且 binom(mp−1,n)为单位。每类高头节点数
\[
 C_a=\begin{cases}s&a\le\tau,\\s-1&a>\tau.\end{cases} \tag{O6}
\]
特别(O5)不随同类的 m 变化。括号中的有限调和数可能增加 valuation；本稿不假设它一定为单位。

## 3. 完整 determinant 的类内平方Vandermonde界

以下纸面引理适用于任意 h 与整系数 W(T)。若 H=W+Σ_jγ_jv(x_j)v(x_j)^t，同类节点差都含 p，同类 C 个 γ 满足 valuation≥w，则该类在全系数 determinant 中的最低贡献为
\[
 \min_{0\le t\le C}\{tw+t(t-1)\}
   =\sum_{k=0}^{C-1}\min(w+2k,0). \tag{O7}
\]
证明：对行列式先按秩一更新作双 minor 展开。重复使用同一更新时两列相同，项为0，所以每个节点最多使用一次。使用 t 个同类节点的每个广义 Vandermonde minor，在整数多项式环中都被类内 ∏_(i<j)(x_j−x_i)整除：交替性逐个给首一差因子，整数除法保留整数商。两个 minors 合计至少 t(t−1) 层p；余下 W-minor 是 Z_p[T] 整的。每一项因此有上述 coefficient-level Gauss 下界，再用非阿基米德三角不等式。允许独立最小化各类，忽略总选择数≤h只会使下界更安全。递增差 w+2k 给右边等式。这个证明不要求 W 对称或正定，也不把有限域秩当真实 determinant 非零。

将(O4)–(O6)代入，定义
\[
 C_p= -\sum_{a=0}^{p-1}\sum_{k=0}^{C_a-1}\min(\nu_a-5+2k,0)\ge0.
\]
则对全部 T 系数，
\[
 v_p^{Gauss}(\det(S_nM_n))\ge-C_p. \tag{O8}
\]
所有 m、所有调和头在此界内；没有继承原K3每列−2。

归一化必须再减 F_n。因为 n<p、3n<3p，精确值是
\[
 v_p(F_n)=2\big((3n-p)_++(3n-2p)_+\big),
\]
\[
 \boxed{v_p^{Gauss}(\widetilde Q_n)\ge
   -C_p-2\big((3n-p)_++(3n-2p)_+\big).} \tag{O9}
\]
对于 p>5n，S_n、F_n都是单位；所有残数与调和头均p整，商部导数矩的 Bernoulli 指数<p−1，故整个 Qtilde 的系数p整。因此(O9)与该末端事实覆盖所有 p>n、p≥7。

## 4. 3n<p≤5n的额外简化与真实未消失层

这里 s=1、τ=5n−p，所有高头 m_j=1。式(O4)变成
\[
 S_nM_n=W(T)-(p^{-5}+3p^{-3})\sum_{a=0}^{\tau}\omega_{p+a}v_{p+a}v_{p+a}^t.
\]
节点在模p时两两不同，故每个外积至多贡献一次，无类内重复；ν_0=2、ν_(1…min(n,τ))=4，其余 ν=0。F_n是单位，于是
\[
 \boxed{v_p^{Gauss}(\widetilde Q_n)\ge
  -5(4n-p)_+-\min(n,5n-p)-3.} \tag{O10}
\]
具体为3n<p<4n时5p−21n−3，4n<p≤5n时p−5n−3。此处额外常数−3来自真实 j=p 的 j² 因子，未当O(n)列费用重复支付。

这些非整层并非仅 safe 表的幻影。若3n<p<4n，令 b=4n−p>0，则 p⁵S_nM_n模p仅剩 a=n+1,…,τ 的 b 个单位外积，其秩恰b：前b行的 Vandermonde可逆，系数全为单位，左右因子分别单射/满射。若4n<p≤5n，p³S_nM_n模p恰剩 a=0 的一个非零外积，其秩为1。这说明“V_3杀低次数”不能把完整高头都删掉。

还可精确隔离缺口。在这个窗口，所有 τ+1 个节点的前τ+1行 Vandermonde是Z_p单位，且τ+1≤h。补成单位基后，矩阵是具有负 valuation 对角 γ_j 的块加上 Gauss整 W(T)。在 Q_p(T) 的 Gauss valuation 环中有限消元，其负 pivot 的 valuation 分别为−5（b次）、−3（一次）、−1（min(n,τ)次）；余 Schur complement Gauss整。因每个负 pivot 的主项为单位、整误差更深，这些负层是实际存在的。但 determinant 可从余 Schur complement得到额外正内容。因此(O10)不是 actual Gauss equality或费用 lower，更不能据它证明全路线不可能。要进一步降低这部分全系数费用，须证明这个同对象剩余 determinant 的内容，而不是再次删除H5或只测试T=0。

## 5. 供预算使用的非最优profile与范围

由(O5)–(O9)可以手工得到下表：除断点的O(1)计数外，费用 upper E_p:=C_p+v_p(F_n)=nφ(p/n)+O(1)。表内已包含 F_n；不能再加一次S或漏掉F。

| x=p/n | φ(x) | 该段积分 |
|---|---|---|
| 1<x<5/4 | 11−4x | 13/8 |
| 5/4<x<4/3 | 19−9x | 59/96 |
| 4/3<x<3/2 | 11−3x | 9/8 |
| 3/2<x<5/3 | 5+x | 79/72 |
| 5/3<x<2 | 19−6x | 8/3 |
| 2<x<5/2 | 7 | 7/2 |
| 5/2<x<3 | 27−7x | 31/8 |
| 3<x<4 | 21−5x | 7/2 |
| 4<x<5 | 5−x | 1/2 |

复核方法完全有限：ν−5=−5给5、8、9三种负和（C=1、2、≥3）；ν−5=−4给0、4、6（C=0、1、≥2）；ν−5=−1给1；零类 ν−5=−3给3或4，其总额为O(1)。数出 a≤min(n,τ)、n<a≤τ、a>max(n,τ) 后加(O9)的F项即得表。端点直接用(O5)–(O9)，不以这张 leading 表替代精确公式。

逐段整数/有理积分后，用分母288相加的九项分子为468、177、324、316、768、1008、1116、1008、144，故
\[
 \int_1^5\phi(x)dx=\frac{5329}{288}. \tag{O11}
\]
通常素数定理 θ(t)=Σ_(p≤t)log p=t+o(t) 即足以支付加权求和：在每个固定分段，令θ_n(x)=θ(nx)/n，则θ_n在[1,5]一致趋于x；Stieltjes分部积分给 nΣ_(n<p≤5n)φ(p/n)log p=n²∫φ+o(n²)。O(1)计数误差只贡献 O(θ(5n))=O(n)，有限分段端点也只贡献O(n log n)。因此
\[
 \sum_{p>n}v_p(d_n)\log p\le
   \left(\frac{5329}{288}+o(1)\right)n^2,
 \qquad d_n\widetilde Q_n=P_n\in Z[T]\text{ primitive}. \tag{O12}
\]
这里在 Q_n≠0 的尺度上定义 primitive P_n 与 d_n；本稿不另证每个n的Q_n非零，241已付无限prime-edge尺度足以使用该条件。v_p(d_n)=−v_p^Gauss(Qtilde_n)，可能为负；(O12)是同对象外层贡献的 upper，不是所有prime的总预算，也不把每处费用强制非负。若不愿采用PNT，(O9)仍独立给逐素数完整界（零多项式下界视为无穷），(O11)只是其显式积分。

本表可与同一对象已证明的 general greedy 界逐素数取较好者；这里未独审A/B最终242预算稿，也不登记未经读取的全部prime总率。对3<x<5，本表面积恰4。额外正内容仍可能使真实费用更小；5329/288大于6不构成费用 lower或no-go。

本轮来源：固定commit 669c92bf7a3728e0de9ad80c373bc29fb5ca3d58 的 Outer/RankOne、Outer/Moments 已保存并实际 FULL 读；另 FULL 复读240完整桥及现有 Local/Entry、Local/Val。实际身份和下载账见同目录 dual_reading_scope.md。新Lean源码仅2份，不读全部依赖、不核Lean；数学运行0。真实关系点无限非零已由241完整证书付清，本稿不重开该证明。全prime费用<6与同对象实处−6完整认证均仍未付，数值目标没有完成。
