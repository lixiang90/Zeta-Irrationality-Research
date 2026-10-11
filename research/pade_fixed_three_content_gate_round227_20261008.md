# 第227轮：原A₇的精确固定3内容与亚纯圆盘上限

2026-10-08，A。固定222–226实际Padé包与所有初值，不改冻结文件。本稿支付一个实际无限fixed-prime theorem：
\[
 v_3(A_{7,\,2\cdot3^e})=6\quad(e\ge0),\qquad
 R_3\!\left(\sum_{r\ge0}A_{7,2r}z^r\right)=1.
\]
再用实际生成微分方程证明：这个原生芽不能亚纯延到任何以0为中心、半径大于1的rigid圆盘。它排除保留该背景行的positive affine 3-place入口；**不自动继承到原 \(\Delta,\Xi,H_g=g\Delta+\Xi\)**。数学程序0，无新数值ζ/L无理性定理。

## 1. 同一原系数与历史范围

记最高部分分式系数及最高周期行
\[
 c_{6,k,n}=
 \binom nk^{6}\binom{n+k}{n}^{3}\binom{2n-k}{n}^{3},\qquad
 S_n=\sum_{k=0}^n(-1)^kc_{6,k,n},\qquad
 A_{7,n}=\frac{189}{32}S_n.
 \tag{F1}
\]
这是222实际正则化部分分式公式，最高pole层是整数；没有以异族超几何或新归一化替换它。\(189=3^3\cdot7\)，故 \(v_3(A_{7,n})\ge3\) 对全部整数 \(n\ge0\) 成立。我们只取原偶序列 \(n=2r\)。

实际FULL读226最终报告8332B／f0d977e7cde11c6247c675356bdddc20f7065e967c1ed09560ce217198734c68；226 manifest54068B／3499c408deda00975b3f434cb8f9eab7c797a3fb9d1c0ded89277ae5d4359305仅核身份，不称FULL全部附件。223全幂safe模型、224原递推、225 leading及完整模式、226生成operator复用作者/独审确切final身份。历史rg定位没有发现本包已付的固定3无限内容定理；226(V7)/(V15)只有必要接口，224无穷素数残差是可变素数结论，均不能代替本稿(F4)。

## 2. 自含稀疏块：全部 \(e\) 的确切估值

令 \(q=3^e,n=2q\)。在 \(\mathbf F_3[X]\) 中，反复立方给
\[
 (1+X)^{2q}\equiv(1+X^q)^2
 =1+2X^q+X^{2q}\pmod3.
 \tag{F2}
\]
因此除 \(k=0,q,2q\) 外，\(\binom{2q}{k}\) 均被3整除；其六次幂使(F1)的整项被 \(3^6\) 整除。这不需要采样 \(e\) 或引用更强的Jacobsthal congruence。

令 \(B_q=\binom{4q}{2q}\)。用 \(v_3(m!)=\sum_{\ell\ge1}\lfloor m/3^\ell\rfloor\) 直接求和：
\[
 v_3((4q)!)=2q-1,\quad v_3((2q)!)=q-1,
 \quad v_3(B_q)=1.
\]
另有
\[
 v_3\binom{3q}{2q}
 =\frac{3q-1}{2}-(q-1)-\frac{q-1}{2}=1.
 \tag{F3}
\]
中点 \(k=q\) 的两个后三次幂binomials都为 \(\binom{3q}{2q}\)，故该项也被 \(3^6\) 整除。端点 \(k=0,2q\) 的两项均为 \(B_q^3\)，且 \(2q\) 偶，两个符号都是正。于是精确地
\[
 S_{2q}=2B_q^3+3^6Z_e,\quad Z_e\in\mathbf Z,
 \qquad v_3(S_{2q})=3.
\]
第一项估值3，余项至少6，不会发生同层消去。因而
\[
 \boxed{\ v_3(A_{7,\,2\cdot3^e})=6\quad\text{对每个 }e\ge0.\ }
 \tag{F4}
\]
也包括 \(e=0\)。这是无限固定素数结论，不依赖222有限producer的 \(n=2\) 校准。

可选的同源unit精化亦为纸证。设
\[
 U_m=\prod_{j=0}^{m-1}(3j+1)(3j+2).
\]
每对因子模9为2，故 \(U_m\equiv2^m\pmod9\)，且阶乘分解给
\[
 \frac{B_{3q}}{B_q}=\frac{U_{4q}}{U_{2q}^2}\equiv1\pmod9.
\]
从 \(B_1=6\) 归纳得 \(B_q/3\equiv2\pmod9\)。结合上一整项恒等式，
\[
 \frac{S_{2q}}{27}\equiv16\pmod{27},\qquad
 \frac{A_{7,2q}}{3^6}\equiv\frac72\pmod{27}.
 \tag{F5}
\]
分母2、32是3-adic units。这是准确的normalized unit block，不把未知harmonic低jet或有限tail丢弃后声称整个源有同样整性。

## 3. 原A₇的精确Taylor半径与有限LCM阻碍

置 \(F_7(z)=\sum_{r\ge0}A_{7,2r}z^r\)，标准化 \(v_3(3)=1\)。全部系数估值至少3，而 \(r=3^e\) 的估值恒为6。因此
\[
 \limsup_{r\to\infty}|A_{7,2r}|_3^{1/r}=1,\qquad
 \boxed{R_3(F_7)=1.}
 \tag{F6}
\]
若原 \(F_7(z/c)\) 被要求有有限固定LCM-type系数，其中某3-place的 \(v_3(c)=\rho>0\)，则 \(r=3^e\) 的系数估值恰为 \(6-\rho3^e\)。有限LCM列在固定3只提供 \(O(\log r)\)；任何固定行常数也不能清除该线性负项。因此**含原A₇行的完整literal模型不能用正3深度的尺度 \(c\)**。自然尺度的12或 \(21/2\) 亦不例外，但其目标-only行与原A₇行不能混为一物。

同样，对任意固定非零 \(P\in\mathbf Q[T]\)，\(P(\theta)F_7\) 的Taylor半径仍为1。写 \(P(T)=T^hQ(T)\)、\(Q(0)\ne0\)，对足够大 \(e\)
\[
 v_3(P(3^e)A_{7,2\cdot3^e})=he+v_3(Q(0))+6=O(e).
 \tag{F7}
\]
其全部系数仍有固定下界，故(F6)的论证适用。这里只支付固定 \(\theta\)-polynomial行的内容；没有从它读出任意degree-\(D\)多项式联合格的最优index或实际CDT秩。

## 4. 实际ODE的3-place有限谱与亚纯去pole引理

226的实际生成方程对原 \(F_7\) 为
\[
 \mathcal LF_7=b_7(z),\quad \deg b_7\le5,\quad
 \mathcal L=\sum_{j=0}^6z^{6-j}p_j(\theta-j),
 \quad N=\deg p_j=10989.
\]
其ordinary最高系数是
\[
 a_N(z)=z^N d_6z^6\chi(1/z),\quad d_6\ne0,
 \tag{F8}
\]
所有ordinary系数与右端都是多项式。最高系数的有限零点只有0及 \(\rho=1/\mu\)，其中 \(\mu\) 遍历225确切 \(\chi\) 的六根。

把确切因子写为
\[
 \chi(u)=(u+3^9)
 (u^2+3^7\cdot9010u-3^9)
 (u^3+3^4\cdot3505753u^2+3^7\cdot1513u+3^9).
 \tag{F9}
\]
9010、3505753、1513都是3-adic units。二次因子根的估值只能为 \(9/2\)：若小于该数，平方项估值唯一最小；若大于该数，常数项唯一最小，均不能为0。三次因子置 \(u=27t\)，除以 \(3^9\) 后为
\[
 t^3+3\cdot3505753t^2+3\cdot1513t+1.
\]
\(v_3(t)>0\) 时常数项唯一最小，\(v_3(t)<0\) 时三次项唯一最小，因此其三根估值都是0。线性根估值9。即
\[
 v_3(\mu)=(3,3,3,9/2,9/2,9),\qquad
 |\rho|_3\ge27.
 \tag{F10}
\]
这可以叫Newton slopes，但本稿已用逐项dominance自证。它仅定位实际ODE的ordinary区域，**不把这些正斜率当原序列的指数内容**。事实上(F4)直接显示那种推断对本包原A₇是错的；archimedean \(C(r)=C_\infty+O(1/r)\) 在固定3整数方向不成为小扰动。

这里使用CDT的标准rigid盘 \(O(D),M(D)\)，即同一个全盘convergent-series/meromorphic quotient结构，而非把ultrametric拓扑的各个小球任意拼接。所需一元去pole事实如下：若 \(F=G/H\in M(D(R))\)，在一个较小closed盘无pole，则 \(F\) 在该closed盘analytic。Weierstrass factorization把 \(H\) 分为盘内有限零点的多项式与analytic unit；无pole使 \(G\) 有全部相同零点重数，可逐一除去。

为明确整个半径未丢失，若 \(G(a)=0, |a|_3\le r\)，\(G(z)=\sum g_kz^k\) 在closed \(D(r)\) 收敛，除去 \(z-a\) 后的系数可写成
\[
 h_n=\sum_{k\ge n+1}g_ka^{k-n-1},\quad
 |h_n|_3r^n\le r^{-1}\sup_{k\ge n+1}|g_k|_3r^k\longrightarrow0.
 \tag{F11}
\]
\(a=0\) 直接移位。analytic unit的逆同盘收敛。因此全部有限零因子消去后确在closed盘analytic；对所有较小closed盘即可得到open盘analytic。这一步区分Taylor radius与meromorphic radius。

## 5. 实际meromorphic圆盘cap与affine准入

假设原生 \(F_7\) 在某个center0 rigid open盘 \(D_3(R)\)、\(R>1\) 有单值meromorphic延拓。选
\[
 1<R_0<\min(R,27).
\]
原ODE作为meromorphic身份在此盘成立：在原点成立的series身份，乘共同analytic分母后仍是全盘analytic身份。盘内除0外最高 \(a_N\) 无零。若ordinary点 \(a\ne0\) 有阶 \(m>0\) 的pole，则 \(a_NF_7^{(N)}\) 具有唯一的最高pole阶 \(m+N\)，其leading coefficient含
\[
 a_N(a)c_{-m}(-m)(-m-1)\cdots(-m-N+1)\ne0
\]
（底域char0）；所有较低derivatives与多项式右端均不能消去它。这不因那些非零整数被3整除而改变pole order。0则由原生analytic芽排除pole。故全 \(D_3(R_0)\) 无pole，由(F11)与factorization为analytic，其原Taylor半径至少 \(R_0>1\)，与(F6)矛盾。因此
\[
 \boxed{\text{原生 }F_7\text{不能meromorphic延到任何center0盘 }R>1.}
 \tag{F12}
\]

特别，任何包含这一个真实背景行、并在3处采用 \(\phi_3(z)=az\) 的common-map模型都必须有 \(|a|_3\le1\)。对归一化行 \(F_{7,c}(z)=F_7(z/c)\)，同一论证给
\[
 F_{7,c}(az)\in M(D_3(1))\ \Longrightarrow\
 |a/c|_3\le1,\quad |a|_3\le|c|_3.
 \tag{F13}
\]
这是真实affine finite-place meromorphic界，不是只把Taylor radius1换个名称。若完整source经已付的有理gauge还能恢复原 \(F_7\)，也继承(F13)。本稿没有支付任意nonlinear有限处图的descent，亦不把它作为所有p-adic maps上限。

## 6. Δ/Ξ/H的未付接口与停止判断

\(\Delta_r,\Xi_r\) 是原四解的相邻三行exterior系数，\(H_{g,r}=g\Delta_r+\Xi_r\)。**(F4)不推出它们在 \(r=3^e\) 的内容**：相邻原指标 \(2r,2r+2,2r+4\) 的低pole jets、harmonic有限tail、跨行消去仍须一起处理。尤其反证下真实实处relation并不自动给一个3-adic relation。外幂leading slopes的平均 \(27/2\) 也不是这些实际系数的内容下界。

一项能真正支付原target scaled内容的证书须落在实际20-state recurrence \(W_{r+1}=C_\wedge(r)W_r\) 与其完整初值。具体的充分接口是：给 \(G(r)\in GL_{20}(K(r))\)、有限起点 \(R\) 和实际尺度 \(c\)，证明对**每个**整数 \(r\ge R\)
\[
 c^{-1}G(r+1)C_\wedge(r)G(r)^{-1}\in
 \operatorname{Mat}_{20}(O_{K,v}),\qquad
 c^{-R}G(R)W_R\in O_{K,v}^{20}
 \tag{F14}
\]
（可先乘一个固定整数）。还须支付全部整数异常，并明确输出行与 \(G(r)^{-1}\) 的 \(O(\log r)\) 估值损失。归纳才给实际输出 \(v_3(f_r)\ge r\,v_3(c)-O(\log r)\)。即使获得此固定place模型，其余places和完整合法数组的费用仍需登记。只有leading \(\chi\)、formal Galois projector或未知初值不能代替(F14)。

当前停止范围明确：**保留原A₇背景的正3-affine入口已排除；原三行 \((1,D,H_g)\) 和target-only的positive3入口未排除、也未认证。** 若继续它们，下一项必须是其自身的(F14)或一个实际fixed3非消去unit block，不能靠升阶或搬leading slopes。此稿对完整背景路线给出了新的实际障碍，对纯目标路线保留缺口；不把partial theorem冒称数值目标完成。

实际primary条件、文件身份、数学0与选读账见 [A227 scope](../literature/pade_fixed_prime_sources_round227_20261008/lambert_reading_scope.md)。主稿与scope保存后须实际FULL作者复读报final身份，作者复读不替代独审。
