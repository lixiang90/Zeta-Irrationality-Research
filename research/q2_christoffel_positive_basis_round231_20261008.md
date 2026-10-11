# 第231轮：正则化完整基、真实Christoffel点值与耦合非零缺口

2026-10-08，A。本文保留230的同一W_d(Θ)=det[B;Nᵀ]。纸面数学，程序0。新结论是一个真正可逆的完整正则化矩阵及原W的精确点值因子；另证明signed单块在无界尺度实数非零。**完整W的无界非零仍未证。**

## 1. 原对象和正则化：仅此变换还不能支付非零

设d≥0、m=d+1、a=1/4、dν=dx/[π√(x(1−x))]。沿230规范，

\[
b_s(x)=2x^s\log(x/a),\qquad
f_s(x)=\frac{\pi}{4}x^{d+1/2}
\sum_{n\ge0}\frac{x^n}{(n+d-s+1/2)^2},\quad0\le s<m.
\tag{C1}
\]

B、Nᵀ分别是这些函数对x^r、0≤r<2m的矩。定义

\[
h_a(x)=\frac{\log(x/a)}{x-a}>0,\qquad
g_a(x)=h_a(x)^{-1}=\int_0^1a^{1-t}x^t\,dt.
\tag{C2}
\]

在x=a以连续值1/a定义h_a；b_s=2(x−a)x^sh_a。νh_a是正有限测度，f_s也有有限ν矩。新矩阵Γ_d的自然行序为h_a x^s（s=0,…,d），随后f_s（同一自然s序），列仍为x^r、r<2m。下一节证明Γ_d实际可逆；不会把它与原signed矩混同。

## 2. 完整正基的Chebyshev性质：自含同号证明

把各列函数共同除以h_a>0。第一组变成1,x,…,x^d；第二组为

\[
\frac{f_s}{h_a}=\frac{\pi}{4}\sum_{n\ge0}
\frac{F_n(x)}{(n+d-s+1/2)^2},\qquad
F_n(x)=\int_0^1a^{1-t}x^{d+1/2+n+t}\,dt.               \tag{C3}
\]

取任意n₁<⋯<n_m。系数矩阵的m阶minor是

\[
\det\left(\frac1{(n_i+d-s+1/2)^2}\right)_{i=1,\ldots,m;\ s=0,\ldots,d}.
\]

它的符号为σ=(−1)^(m(m−1)/2)，严格非零。确切理由是1/(n+β)²=∫₀¹y^(n+β−1)(−log y)dy；反序s后指数d−s成为0,…,d。Andreief公式把minor写成两个严格同号的广义Vandermonde对正权y^(−1/2)(−log y)的积分。

再取0<x₁<⋯<x_(2m)<1。将F_(n_i)的m个积分分别展开为独立t_i∈(0,1)。幂指数依次为

\[
0,\ldots,d,\quad d+1/2+n_1+t_1,\ldots,d+1/2+n_m+t_m.
\]

它们严格递增：整数n相差至少1，而各t窗口长度为1。其函数行列式严格正。这里的幂函数结论可自含推出：x=e^u后，重复Rolle给不同指数的指数和至多2m−1个零点；相邻节点合流时Wronskian的指数Vandermonde严格正，故整个有序节点区域的符号为正。正t_i积分仍严格正。

对(C3)作有限截断的Cauchy–Binet展开，每个m指标集的项都有同一符号σ，且至少一个严格非零。系数为O(n^(−2))，F_n在[0,1]一致有界；因此函数级数及有限行列式一致收敛，极限保持严格符号。x=0的N/h值为0，首行1可先展开；x=1亦由绝对收敛覆盖。得到**这个指定2m维完整行族**的Chebyshev性质，不是所有自由multi-indices的完美性。

对ν作Andreief矩公式（或对h_aν作同一正基公式），节点Vandermonde与函数行列式乘积保持严格同号，故

\[
\det\Gamma_d\ne0,\qquad \operatorname{sgn}\det\Gamma_d=\sigma.
\tag{C4}
\]

自然f_s序的σ必须保留；反序f_s后才为严格正。端点支配由各行有限矩保证，不要求在原ν权下h_a有界。

## 3. 正基新增π周期，但不是非算术模型

Root提供的K(a)身份可独立用正积分验证。由(C2)的等价Stieltjes表示及正Fubini，

\[
K(a):=\int_0^1h_a\,d\nu
=\int_0^\infty\frac{dt}{(a+t)\sqrt{t(t+1)}}.
\]

ν的Stieltjes积分∫dν/(x+t)=1/√(t(t+1))可令x=sin²θ、再u=tanθ直接得到。外积分令t=sinh²v，再u=tanh v，

\[
K(a)=2\int_0^1\frac{du}{a+(1-a)u^2}
=\frac{2\arccos\sqrt a}{\sqrt{a(1-a)}},\qquad
K(1/4)=\frac{8\pi}{3\sqrt3}.                           \tag{C5}
\]

无PV需要。以下取a=1/4；多项式除法还给每个n≥0的完整矩

\[
\int x^nh_a\,d\nu
=a^nK(a)+\frac12\sum_{j=0}^{n-1}a^{n-1-j}B_j,
\quad B_j=\int2x^j\log(4x)\,d\nu=4c_jh_j\in\mathbb Q.
\tag{C6}
\]

空和包含n=0。Γ因此有准确的Q、K、G、Θ周期分解；K是Q(√3)倍π，且h行的K系数a^(s+r)为rank1。没有假设这些实际周期独立，也未证明完整primitive费用或strict预算。旧signed矩的整化不能免费等同新正基的整化。

## 4. 原W恰为一个单首分量的点值

由(C4)，存在唯一单首degree-m多项式

\[
P_m(x)=x^m+\sum_{j=0}^{m-1}\alpha_jx^j
\]

和唯一β_s，使线性形式

\[
h_a(x)P_m(x)+\sum_{s=0}^{d}\beta_sf_s(x)
\]

对全部x^r、r<2m的ν矩为0。这是**单首、齐次的type-I第一分量构造**。它不自动支付通常type-I最后一个矩归一为1，也不支付扩展index (m+1,1,…,1)的normality。

将原上m行写成2(h_ax^(s+1)−a h_ax^s)，在f行模掉上述唯一关系。上块的有限系数矩阵为companion移位减aI，其行列式是(−1)^mP_m(a)。因此，在同一自然行序有

\[
\boxed{\mathcal W_d(\Theta)=(-2)^m\det\Gamma_d\,P_m(1/4).}
\tag{C7}
\]

这是原实际signed对象的精确恒等式，不是上界比较。它把完整非零问题精确变为P_m(1/4)在无界m不为0。正基可逆仅允许定义P_m，**不证明这个点值**。

扩展第一组到1,…,x^m时，(C3)中n=0的尾指数d+1/2+t会穿过m=d+1，刚才的同号指数排序不再成立。因此不能以“多加一行也Chebyshev”支付扩展normality或交错。跨d也不是直接沿固定measure的标量OP链：对s≤d，

\[
f_{d+1,s}=f_{d,s}
-\frac{\pi}{4}\frac{x^{d+1/2}}{(d-s+1/2)^2}.
\tag{C8}
\]

还会增加一个新s行。不过这些行不是任意变化的函数族，确实来自同一个固定Stieltjes核的Padé尾。设

\[
\mathscr F_n(x)=\int_0^1
\frac{y^{n-1/2}(-\log y)}{1-xy}\,dy .
\]

在0≤x≤1用正积分，或在|x|<1用绝对收敛展开，均有

\[
x\mathscr F_{n+1}=\mathscr F_n-\frac1{(n+1/2)^2},
\quad
x^n\mathscr F_n=\mathscr F_0-
\sum_{j=0}^{n-1}\frac{x^j}{(j+1/2)^2},
\]

\[
f_{d,s}(x)=\frac{\pi}{4}x^{s+1/2}
\left(\mathscr F_0(x)-
\sum_{j=0}^{d-s-1}\frac{x^j}{(j+1/2)^2}\right).
\tag{C8'}
\]

空和包含s=d；这里x幂和求和指标都由真实一次尾移位确定。这给一个精确后续接口：尝试把**同一个**(C7)的W或点值P_m(a)写成固定标量/矩阵生成函数的Hankel minor族，并证明其最终消失会强迫有限Hankel秩。只有完成这个归约及相应Kronecker条件，非有理生成函数才可能支付无界非零；目前没有该same-object证书。也没有已付的固定三项递推或跨m交错阻止P_m(a)最终为0。本文不宣称它最终为0。

## 5. signed单块确有无界实数非零，但不能传给W

设D_m为固定正测度μ=h_aν的m阶Hankel determinant，D_m>0；q_m为其单首标量正交多项式。标准Christoffel行消元（同(C7)的单组版本）直接给

\[
\det(B_{s,r})_{0\le s,r<m}=(-2)^mD_mq_m(a).           \tag{C9}
\]

三项递推q_(m+1)=(x−α_m)q_m−β_mq_(m−1)，其中β_m=||q_m||²/||q_(m−1)||²>0，来自对正测度逐次数正交展开。若q_m(a)及q_(m+1)(a)同时为0，递推向下会迫使q_0(a)=1为0，矛盾。因此每两个相邻m至少一个(C9)非零，signed单块在无界尺度的**实数非零**已付。

q_m是固定μ的标量OP，P_m是含全部N行的耦合分量，二者不同。这个结论既不证明W的无界非零，也不证明p=4d+1时detB的分子是p单位，更不能证明数值目标独立。

## 6. Primary接口、实际范围与停止判断

定向primary [Kozhan–Vaktnäs 2503.15122v1](https://arxiv.org/pdf/2503.15122v1) 的§3.1/§3.3给normality矩及AT→normality；Theorem4.8把type-I分量点值与只变一个measure的Christoffel normality相连。§4.3明确AT本身不保证type-I分量实根；Theorem5.5的交错还要求相关indices normal、平方变换normal及实根。当前未支付这些跨尺度条件，故不调用其结论证明(C7)点值非零。本文(C2)–(C9)为自含证明，尤其不假定扩展normality。

另实际完整选读Root已存Magnus作者稿PDF10–11的§5.3：合流Jacobi–Piñeiro模板只给对数权的部分正交，不能代替当前arcsine/Stieltjes完整条件。其显示的递推不是P_m的递推，相关渐近未移植为本对象定理。没有导入RH渐近、周期单射或文献中未核的非零结论。

本轮正收益是完整正基真可逆、原W的确切点值因子、新π通道的完整矩身份、固定核的真实尾移位，以及signed单块无界实数非零。**P_m(1/4)的无界非零、完整净费用、ζ/L真实周期隔离都仍未付。** 后续只优先检验(C8')是否给出同一W的固定Hankel归约；无该证书便停止以正性或经典标量交错代替耦合问题，并与Root/B有限域结构合并后决定是否提前复盘。

实际FULL读230解析稿6942B及最终报告6229B。新下载primary PDF1份（2503.15122v1，19页）；实际完整选读仅PDF6–8、10–11、15–16，共7页，不称全文审稿。Magnus复用Root PDF，仅实际FULL选读10–11。五次文档提取得五份非空TXT并完整读取；数学程序/扫描/CAS/旧producer/Git0。精确source身份见同目录lambert_reading_scope.md；本文和scope保存后实际FULL作者复读，不代替独审。
