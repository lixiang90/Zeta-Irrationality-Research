# 第272轮：固定 Abel 来源的完整安全预算与到期结算

2026-10-20。执行[272一轮任务](abel_beta45_budget_charter_round272_20261020.md)，对象始终是[271.2–271.7](global_budget_review_round271.md)的唯一Hermite来源和 \(Y=4\beta(5)-3\beta(4)\)。上一goal turn已完成271证明、状态修订及云端发布，属实际进展；本轮从实际active状态和干净工作树恢复，没有重做旧263窗口。

**结论：已付指数级整数值来源、全部有理头/素数幂安全清整及确切本原桥。指定未经内容约分的实际安全族具有正二次增长下界。最优内容与负本原净预算仍未证，本一轮窗口到期结束，不准入数值实施。** 没有新无理性定理，也没有最优方法no-go。

## 1. 同一来源：整数值与整系数分开

[独立来源证明H1–H14](abel_beta45_hermite_structure_round272.md)给原基的闭式与连续节点Hermite表达。记

\[
n=2m-1,\quad d=6m-2,\quad D=12m-7,\quad
L_0=d_{4m-3},\quad L=d_{4m},
\]

其中 \(d_N=\operatorname{lcm}(1,\ldots,N)\)，m≥1。设 \(P_i(t)=p_i((t+m)^2)\)，\(f_i(q)=p_i((q+1/2)^2)\)，则

\[
C f_i\in\operatorname{Int}(\mathbf Z),\qquad C=8L_0^2,
\]
\[
K P_i\in\operatorname{Int}(\mathbf Z),\qquad K=C4^d,\qquad \log K=O(m).
\tag{272.1}
\]

这是全尺度来源改善，但整数值多项式不等于单项式整系数。H10的精确三jet表达使用连续节点Lagrange整数值基；H6在q坐标消掉表面x倒数。没有运行参数、m、prime或CAS扫描。

为完整安全清头，本轮明确支付较粗的整系数倍数

\[
T=C\,d!\,2^d.
\tag{272.2}
\]

由Newton整数展开，\(C f_i=\sum_{r\le d}a_{ir}\binom qr\)，\(a_{ir}\in\mathbf Z\)，所以 \(Cd!f_i\in\mathbf Z[q]\)。由于

\[
q=\frac{u+2m-1}{2}\quad(t=u/2),
\]

得到 \(T P_i(u/2)\in\mathbf Z[u]\)，特别 \(TP_i(t)\in\mathbf Z[t]\)。再平移整数m并利用关于 \(t+m\) 的偶性，得到

\[
T p_i(w)\in\mathbf Z[w].
\tag{272.3}
\]

这里阶乘费用真实保留，未把它说成最优费用下界，也未把272.1冒充完整有理核商部的清整。

## 2. 全部多项式Euler头及有限调和头

对 \(F_{ij}=R_mP_iP_j\) 写唯一分解 \(F_{ij}=H_{ij}+F_{ij}^{\mathrm{proper}}\)，其中H为多项式。每个P的次数≤d，R的degree为−3，故deg H≤2d−3=D。缩放u=2t后

\[
R_m(u/2)=
8\,\frac{\prod_{j=1}^{n}(u+2j)^3}
{\prod_{k=0}^{n}(u+2k+1)^3}.
\tag{272.4}
\]

分母为首一整系数多项式，272.2使完整分子为8倍整系数。首一长除法因此给

\[
T^2H_{ij}(t)\in8\mathbf Z[t].
\tag{272.5}
\]

这支付整个商部，不只最高项；不需再按原R重复加一笔dyadic费用。

在完整Abel身份中，常数栏包括 \(\mathcal E(H_{ij}'')\) 及全部有限调和头，\(\mathcal E\)从t=0取交错Abel值。整数单项式的Euler值满足

\[
\mathcal E(t^r)=
\sum_{j=0}^{r}\left\{\begin{matrix}r\\j\end{matrix}\right\}
j!\frac{(-1)^j}{2^{j+1}}.
\]

实际272.4的长除法更精确给 \(T^2H_{ij}(t)=8V_{ij}(2t)\)，\(V_{ij}\in\mathbf Z[u]\)。对于每个次数j≥2的单项式，\(8\cdot2^j j(j-1)\mathcal E(t^{j-2})\) 已为整数；次数0、1二导数为零。因此

\[
T^2\mathcal E(H_{ij}'')\in\mathbf Z.
\]

不需再付保守的 \(2^{D+1}\)。没有丢掉多项式头或起点t=0；这里的dyadic信用来自同一u缩放及完整商部，而不是凭Euler最高项猜约分。

271的完整乘积jet给右半极点主部 \(a_{3,k},3a_{3,k},0\)，左半部由反射确定；交叉项所有主部为零。由

\[
a_{3,k}=\left(4^{-n}\binom{2k}{k}
\binom{2(n-k)}{n-k}\right)^3
\]

可知所有主部系数由 \(2^{6n}\) 清整。T²含 \(2^{2d}\)，且 \(2d=12m-4\ge6n=12m-6\)，所以T²已清这笔费用。除整体正负符号外，有限头清整问题化为271 A2中的完整和

\[
\sum_{k=0}^{n}\sum_{s=1}^{3}(-1)^k2^{s+2}s(s+1)A_{s,k}
\sum_{v=0}^{k-1}\frac{(-1)^v}{(2v+1)^{s+2}}.
\tag{272.6}
\]

实际 \(A_{1,k}=0\)；保守统一用最高幂5。所有非零奇分母≤2n−1=4m−3，故L⁵清全部这些头，覆盖所有素数幂。2处已由上式单独支付；没有把原packet的大素数引理免费移交给新来源。

因此对于271中带σ符号的实际 \(M_m=A_m+YB_m\)，有完整安全证书

\[
\boxed{S_mA_m,\ S_mB_m\in M_m(\mathbf Z),\qquad
S_m=T^2L^5
=2^{12m+2}(d!)^2L_0^4L^5.}
\tag{272.7}
\]

这是明确安全倍数，不是最小矩阵分母或最小Q清整。

## 3. 首一归一和本原内容必须一起记账

令

\[
\Lambda_m=|\det(S_mB_m)|,\qquad
F_m(Z)=\operatorname{sgn}(\det(S_mB_m))
\det(S_mA_m+ZS_mB_m).
\]

则 \(F_m=\Lambda_mQ_m\in\mathbf Z[Z]\)，首项为Λm。设 \(g_m=\operatorname{content}(F_m)>0\)，则gm整除Λm，并且

\[
\boxed{\lambda_m=\Lambda_m/g_m,\quad
F_m/g_m=\lambda_mQ_m\ \text{本原}.}
\tag{272.8}
\]

若有更小清整，它与本原整多项式成有理比例，首项和Gauss引理迫同一最小倍数；或直接用各系数分母的最小公倍数。没有额外再清Q，也没有把来源费用与直接多项式费用重复领取。

实际评价的精确等式是

\[
|F_m(Y)|=S_m^m\det M_m,\qquad
|\lambda_mQ_m(Y)|=\frac{S_m^m\det M_m}{g_m}.
\tag{272.9}
\]

全部Y=u/v反证仍给 \(0<|v^mF_m(Y)/g_m|\in\mathbf Z\)。B一般不定，但归一化保留其det的绝对值和符号，实际M为正定；没有假设所有非实际有理参数都非零。

## 4. 同一实际安全族的增长证书

[实处证明](abel_beta45_gram_bounds_round272.md)独证整个实轴的实际上界

\[
\log\det M_m\le(2+12\log6)m^2
+12m\log m+39m\log2.
\tag{272.10}
\]

它是正上界，不能被说成实际增长。该稿另按下述论证核实整数来源的Gram下界，二者分开。

设

\[
c_*=\frac{8\pi^2e^{-18}}{(\sinh\pi)^3}>0.
\]

对 \(|y|\le1\)，乘积逐项给

\[
U_m(y)\ge
4\prod_{j=1}^{m-1}\left(\frac j{j+1/2}\right)^2
\exp\left(-\sum_{j=0}^{m-1}(j+1/2)^{-2}\right)
\ge\frac{2e^{-6}}m.
\tag{272.11}
\]

这里 \(\sum_{j\ge0}(j+1/2)^{-2}\le4+\int_0^\infty(x+1/2)^{-2}dx=6\)，且
\((j/(j+1/2))^2\ge(j-1/2)/(j+1/2)\)，后者乘积为1/(2m−1)。再用sinh(πy)/y≤sinhπ，得到实际密度在 \(|y|\le1\) 上满足 \(\omega_m(y)\ge c_*/m^3\)；没有对整个实轴作这项常数下界。

全实轴限制到[−1,1]，再令z=y²，便有Loewner下界

\[
M_m\succeq \frac{c_*}{m^3}
\left[\int_0^1p_i(-z)p_j(-z)\,dz\right]_{ij}.
\]

由272.3，整数多项式 \(Tp_i(-z)\) 独立且degree<3m。选其系数矩阵按次数最高的非零Plücker minor：它是非零整数，绝对值≥1。在首一正交Legendre基中，单位三角换基保持这一最高minor；外积范数平方至少该项。其pivot次数r1<…<rm满足

\[
\sum r_i\le(5m^2-m)/2,\qquad
h_r=\frac1{(2r+1)\binom{2r}{r}^2}\ge\frac1{(2r+1)16^r}.
\]

因此全m成立

\[
\boxed{T^{2m}\det M_m\ge
\left(\frac{c_*}{6m^4}\right)^m
16^{-(5m^2-m)/2}.}
\tag{272.12}
\]

结合精确272.7–272.9，得到指定未经内容约分的实际族

\[
\boxed{S_m^m\det M_m\ge
\left(\frac{c_*}{6m^4}\right)^m
L^{5m}2^{-10m^2+2m}.}
\tag{272.13}
\]

不需素数定理也可证明正二次率：每个 \(\binom Nk\) 的p估值是至多 \(\lfloor\log_pN\rfloor\) 个0/1的和，故整除dN；由二项式和，\(d_N\ge2^N/(N+1)\)。把N=4m代入272.13，全序列liminf二次率至少10log2>0。采用标准 \(\log d_N=N+o(N)\)，则进一步

\[
\liminf_{m\to\infty}m^{-2}\log|F_m(Y)|
\ge\kappa:=20-10\log2>0.
\tag{272.14}
\]

271.9的严格负**本原**预算若成立，必要有

\[
\boxed{\liminf m^{-2}\log g_m>\kappa.}
\tag{272.15}
\]

这是同一S所定义内容的必要条件，非充分条件；没要求任何率极限存在。若只用初等下界，必要门槛为10log2。对预定无界子列上的严格负预算，272.15只在同一子列取liminf，不能由此声称全序列内容足够。改变安全S时内容g也改变，κ不是不依赖归一化的绝对费用。对所选安全族的所有无界子列，272.14均有效；它没有给 \(|Q_m(Y)|\) 的全m非负二次率，也没有给最优λ的下界。

完整安全upper则是272.10加 \(m\log S_m\)；阶乘造成的 \(O(m^2\log m)\) 成本仍保留。不能因为整数值来源仅exp(O(m))，就把这笔完整商部/整系数安全成本宣布消失。

## 5. 短结算与下一决定

本轮新实际资产：原Hermite基的整数值来源、完整全素数幂清头、确切本原桥、实际Gram安全upper及选定安全族的全尺度增长lower。独审未取得原首问题 \(\liminf m^{-2}\log|Q_m(Y)|\ge0\)，也没有证明实际g足够大；最高系数minor的猜测未当证据或新窗口理由。

**一轮到期，关闭这个固定实现的默认投入。** 停止的是n=2m−1、271唯一基、上述安全清整证书的继续优化；不否定Y无理、最优本原化、全部Abel方法或其它真实来源。只有改变同一实际本原内容/实处预算的新全尺度机制，才可登记重开；更多样本、正性、局部minor或改标签不够。

本轮是结构与安全预算进展，没有数值可行准入，连续核心停滞保留为12。下一轮作[273提前正式资源比较](source_gate_charter_round273_20261020.md)，最多一轮；旧数学窗口关闭范围不变。总goal保持active及原成功标准。

根与三位代理纸面推导和独立反证审查，贡献者不把自己的复读计作独审；实际读域和分工见两份技术证书。没有数学扫描、CAS或Lean执行；仓库/状态核验不认证数学。
