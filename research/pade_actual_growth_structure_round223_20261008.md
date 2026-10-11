# 第223轮：固定交错三周期包的真实指数衰减

2026-10-08。只研究222已固定的 R_n、I_n 和相邻三行外积；不改目标、参数或冻结稿。本轮付清一个新的解析接口：对偶数 n≥2，实际交错一阶导数和满足

\[
|I_n|=O\!\left(n^{-5}\log n\,\vartheta^n\right),\qquad
\vartheta=\frac{2^{42}}{3^{27}}=
\left(\frac{2^{14}}{3^9}\right)^3<1.\tag{G1}
\]

证明保留轮廓移位越过的全部有限项，不假定它们消失。它不证明 I_n 的渐近等式或非零性，也尚未支付 A₃、A₅、A₇ 的实际主增长、Δ 的无限非零或完整源的严格过收敛。本轮没有新的数值无理性定理。

## 1. 同一个对象与文献族的边界

沿用[222实际分式稿](relation_source_architecture_global_round222_20261008.md)的全部归一化：

\[
R_n(t)=\frac{\prod_{j=1}^n[(t-j)(t+n+j)]^3}
{\prod_{k=0}^n(t+k)^6},\qquad
I_n=\sum_{m\ge1}(-1)^mR_n'(m),\qquad n\ge0\text{ 偶数}.\tag{G2}
\]

在 m=1,…,n 处，三阶零使 R_n'(m)=0。固定 n 时 R_n(t)=O(t⁻⁶)、R_n'(t)=O(t⁻⁷)，故实际和绝对收敛。其周期分解仍是

\[
I_n=A_{3,n}\zeta(3)+A_{5,n}\zeta(5)+A_{7,n}\zeta(7)+C_n.
\]

n=0 的纯 ζ(7) 身份不在G1的范围内。

实际完整选读 Zudilin2003 作者PDF页23–25：[作者原件](https://www.math.ru.nl/~zudilin/PS/z234.pdf)。页23–24的完整§7有两个相邻但不同的族：式(62)的 F₇,ₙ 使用一次分子、八次分母、n!⁶ 及 2t+n，且非交错；另一族是 (1/2)Σ d²[(2t+n)R_n(t)]/dt²，同样非交错。原文两组四阶特征多项式分别为

\[
\lambda^4-828\lambda^3-132246\lambda^2+260604\lambda-27,
\]

\[
\lambda^4+9264\lambda^3-12116166\lambda^2-752300\lambda-19683.
\]

它们不是G2的递推或增长证书。本稿不移用其根、算术除子或多重积分结论。页25的式(69)明确带 h₀+2μ 因子；读了该定义所在完整页，但下一页的 Theorem5 条件未读、未采用。因此不声称已核一个可直接适用的 Andrews／very-well-poised 积分定理。

## 2. 实际超几何身份：参数导数仍需保留

这不是增长定理，但给出可复核的精确输入。对足够小的复数 ε，设

\[
B_n(\varepsilon)=
\frac{\Gamma(n+1+\varepsilon)^9\Gamma(3n+2+\varepsilon)^3}
{\Gamma(1+\varepsilon)^3\Gamma(2n+2+\varepsilon)^9}.
\]

上标“×j”表示参数重复j次。由逐项 Γ 比值得到

\[
S_n(\varepsilon)=B_n(\varepsilon)\,
{}_{13}F_{12}\!\left(
\begin{matrix}
1,(n+1+\varepsilon)^{\times9},(3n+2+\varepsilon)^{\times3}\\
(1+\varepsilon)^{\times3},(2n+2+\varepsilon)^{\times9}
\end{matrix};-1\right)
=\sum_{k\ge0}(-1)^k R_n(n+1+k+\varepsilon).\tag{G3}
\]

额外的上参数1抵消超几何定义中的 k!。固定 n 的有理函数在 ε 的一个小闭盘内满足 R_n(n+1+k+ε)=O(k⁻⁶)，其 t 导数为 O(k⁻⁷)，常数可依赖 n。因此级数及导数一致绝对收敛；对偶数 n，

\[
I_n=-S_n'(0).\tag{G4}
\]

ε=0时可约去一个上、下参数1，留下 {}₁₂F₁₁。取 h₀=3n+2，其余上参数为两份 h₀ 和九份 n+1，下参数恰为两份1和九份 2n+2=1+h₀-(n+1)，故此值有 ordinary well-poised 配对。它没有产生 very-well-poised 所需的额外线性因子 h₀+2k=2t+n，而且实际参数导数G4必须保留。这里的 −1 参数也不能免费改成上述文献族的非交错参数。本轮没有用形式标签推出G1；下一节直接证明它。

## 3. 移位轮廓与必须支付的有限头

以下证明对所有整数 n≥2 的交错和成立，最后仅采用偶数 n 的周期投影。置

\[
c=2n+\tfrac12,\qquad K(t)=\frac{\pi}{\sin\pi t},
\quad
P_n=\sum_{m=n+1}^{2n}(-1)^mR_n'(m),\quad
T_n=\sum_{m=2n+1}^{\infty}(-1)^mR_n'(m).
\]

则实际 I_n=P_n+T_n。K 在整数 m 的留数为 (−1)^m。沿 Re t=c 的向上竖线向右闭合矩形，正方向为顺时针。右边取趋于无穷的半整数，横边取 Im t=±Y 后令Y趋于无穷：固定 n 的有理函数界与 csc 的指数衰减使三条外边贡献消失。Re t>c 内 R_n 没有极点。因此留数定理给

\[
T_n=-\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}K(t)R_n'(t)\,dt
=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}K'(t)R_n(t)\,dt.\tag{G5}
\]

第二式为沿同一竖线分部积分，K(t)R_n(t)在两端趋于0。只把G5当成整个 I_n 会漏掉P_n；以下分别控制两部分。

## 4. 竖线全高度估计

对 y≥0，直接对原有限乘积的模求导，得到

\[
\frac{d}{dy}\log|R_n(c+iy)|=
3\sum_{j=1}^n\frac{y}{(c-j)^2+y^2}
+3\sum_{j=1}^n\frac{y}{(c+n+j)^2+y^2}
-6\sum_{k=0}^n\frac{y}{(c+k)^2+y^2}.
\tag{G6}
\]

最后一项非正，可以舍去作上界。函数 y/(x²+y²) 对正x递减。前两个整数等距和分别不超过

\[
\int_{n-1/2}^{2n-1/2}\frac{y\,dx}{x^2+y^2},\qquad
\int_{3n+1/2}^{4n+1/2}\frac{y\,dx}{x^2+y^2}.
\]

这是对每个取样点d使用区间[d−1,d]所得，并没有把和当成未经认证的Riemann近似。对0<a<b，

\[
\sup_{y\ge0}\int_a^b\frac{y\,dx}{x^2+y^2}
=\arcsin\frac{b-a}{b+a}.
\tag{G7}
\]

证明：积分为 arctan(b/y)−arctan(a/y)，其导数变号点 y=√(ab) 是唯一最大点；代入并用 sin 差角公式即得G7。端点y=0、∞均为0。

第一段的比率 n/(3n−1)≤2/5，第二段 n/(7n+1)<1/7。又因0≤u<1时 arcsin u≤u/√(1−u²)，

\[
\arcsin(2/5)\le2/\sqrt{21}<1/2,\qquad
\arcsin(1/7)\le1/\sqrt{48}<1/6.
\]

故G6的右侧小于2。积分并利用复共轭，得到全部真实竖线上的统一界

\[
|R_n(c+iy)|\le R_n(c)e^{2|y|},\qquad y\in\mathbb R.\tag{G8}
\]

因为c为半整数，

\[
|K'(c+iy)|=
\pi^2\frac{|\sinh\pi y|}{\cosh^2\pi y}
\le2\pi^2e^{-\pi|y|}.
\]

把G8代入G5并实际积分 e^{-(π−2)|y|}，可得

\[
|T_n|\le\frac{2\pi}{\pi-2}R_n(c).\tag{G9}
\]

π−2>0，常数不依赖n。这同时支付任意高度的尾部，而非仅局部saddle邻域。

## 5. 有限头、精确 Γ 比值与指数底数

令u=t+n/2，a_j=n/2+j，b_j=n/2−j+1。对t>n，

\[
q_j(t)=\frac{u^2-a_j^2}{u^2-b_j^2}\in(0,1),\qquad
R_n(t)=\frac{\prod_{j=1}^n q_j(t)^3}{t^3(t+n)^3}.\tag{G10}
\]

后一身份使用
∏(u²−b_j²)=t(t+n)∏_{j=1}^{n−1}(t+j)²。
因为 a_j²−b_j²=(2j−1)(n+1)>0，q_j'(t)>0。在整数 n+1≤m≤2n<c 上，因此

\[
R_n(m)\le R_n(c)
\left(\frac{c(c+n)}{m(m+n)}\right)^3
\le64R_n(c).\tag{G11}
\]

最后一个粗常数来自n≥2时 c/n≤9/4、(c+n)/n≤13/4、m(m+n)≥2n²，故括号≤117/32<4。

原乘积的 logarithmic derivative 恰为

\[
\frac{R_n'(t)}{R_n(t)}=
3\sum_{j=1}^n\left(\frac1{t-j}+\frac1{t+n+j}\right)
-6\sum_{k=0}^n\frac1{t+k}.
\]

对实t>n，逐项绝对值的总和≤(12n+6)/(t−n)。令 h_n=Σ_{j=1}^n1/j≤1+log n，由G11得

\[
|P_n|\le64(12n+6)h_nR_n(c).\tag{G12}
\]

该估计允许有限头中的全部项，不利用它们的交错消去。由G9、G12，得到一个直接可审查的精确上界

\[
\boxed{|I_n|\le
\left(64(12n+6)h_n+\frac{2\pi}{\pi-2}\right)R_n(2n+1/2).}\tag{G13}
\]

对Re t>n，原分式还有精确恒等式

\[
R_n(t)=\frac{\Gamma(t)^9\Gamma(t+2n+1)^3}
{\Gamma(t-n)^3\Gamma(t+n+1)^9},
\]

所以

\[
R_n(2n+1/2)=
\frac{\Gamma(2n+1/2)^9\Gamma(4n+3/2)^3}
{\Gamma(n+1/2)^3\Gamma(3n+3/2)^9}
=\frac{64}{19683}n^{-6}\vartheta^n(1+O(n^{-1})).\tag{G14}
\]

这里仅用正实轴上的固定 a>0、固定 b 的 Stirling Γ(an+b) 公式；实际核读 [DLMF5.11.E1](https://dlmf.nist.gov/5.11.E1) 与 [E7](https://dlmf.nist.gov/5.11.E7)及其适用条件。n的线性项准确为2⁴²ⁿ/3²⁷ⁿ，幂次为n⁻⁶，常数为2⁶/3⁹。由于2¹⁴=16384<19683=3⁹，θ<1是精确整数比较，不是数值拟合。G13、G14证明G1。

## 6. 与实际外积、同源分母的合并范围

继续使用222的实际三行定义

\[
J_r=\det(A_{3,2r+2h},A_{5,2r+2h},I_{2r+2h})_{h=0,1,2},
\quad J_r=\Delta_r\zeta(7)+\Xi_r.
\]

222的P6、P7、P15已经给出 |A_{s,n}|+|C_n|≤poly(n)2¹⁵ⁿ；本轮实际FULL复读该冻稿。沿J的第三列展开并用G1，存在固定B使

\[
|J_r|=O\!\left(r^B(1+\log r)
\left(2^{60}\vartheta^2\right)^r\right)\quad(r\to\infty).\tag{G15}
\]

固定相邻移位+2、+4只改变常数及多项式。r=0的含n=0项是一个有限例外，不影响级数半径。在假设 ζ(7)=g∈Q 时，真实关系芽 H_g(z)=ΣJ_rz^r因此满足

\[
R(H_g)\ge(2^{60}\vartheta^2)^{-1}.\tag{G16}
\]

这严格提高了旧的 **保证半径下界**2⁻⁶⁰，但不是与generic背景实际半径的严格比较。Δ、Ξ目前仍只有R≥2⁻⁹⁰的保证；不能比较两个下界就宣布关系取消了一个真实主奇点。2⁶⁰θ²>1也仍意味着G15不是J_r绝对衰减的证书；它不排除另有完整holonomy源通过相对解析收益奏效。

本轮另实际FULL读并独立纸核[同一分式的新分母证明](pade_integer_valued_denominators_round223_20261008.md)D1–D7。d_n的整数值多项式normalized jets和Q_n的正则jets给 d_n^(6−j)c_(j,k,n)∈Z，全部有限tail给d_n⁷C_n∈Z；没有删掉低权列或有限项。合并范围如下：

| 同一actual对象 | 已证明的新界 | 本稿不升级为 |
|---|---|---|
| I_n，偶n≥2 | G13与G1的真实指数上界 | 非零、精确主渐近 |
| A₃,A₅,A₇,C | 仍沿用poly(n)2¹⁵ⁿ上界；r前缀分母safe(8,4,0,14) | generic实际指数或最优共同格 |
| Δ_r | 64³d_(2r+4)⁶Δ_r∈Z，safe指数12 | 无限非零或不可去主奇点 |
| Ξ_r及gΔ_r+Ξ_r | 64³d_(2r+4)¹³Ξ_r∈Z；条件芽另乘固定c_g，safe指数26 | CDT实际τ已最优、完整rank已付 |
| H_g=ΣJ_rz^r | G16的更好半径下界，全部系数仍是真实外积 | R(H_g)>R(generic)、严格gate |

用普通flat(0,12,26)所得166/9仅为完整模型独立等假设下的费用诊断；不把它与一个未付的共同图拼成成功判据。没有Betti/Hodge硬门槛的额外假设：剩余工作是这同一包的非退化、递推/完整cyclic源、实际背景主增长与关系取消，再作全部算术—解析严格比较。

本轮真正新增的是G1与同源d_n改进能够同时用于固定实际packet；已知异族递推、仅有ordinary well-poised标签或旧μ₇正性不承担缺失的接口。若后续无法认证同一完整源的严格解析收益，就把本包降级为校准，而不转入参数、素数或能量扫描。

## 7. 实际读取与运行账

本稿数学G1–G16全部为纸面推导；数学程序、CAS、数值积分、矩阵计算、PSLQ、Lean、prime/parameter/grid扫描均0。工具只做web primary读取、已存文本读取/复制、两个DLMF公式TEX下载、文档写入与metadata/hash。没有重复下载共享Zudilin PDF，没有运行222 producer，也没有Git操作。

作者本轮实际FULL读222分式稿11908B/SHA256 `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`；实际FULL读新分母稿最终6110B/SHA256 `cea842775409706034017f9f1dbc7cbcde39ed6d331691dfa3d80588ab79c648`，此前5822B版本也实际FULL读过。它们的作者读与本稿作者读分别登记，不冒充自己稿的独审。

primary是选择范围完整读：Zudilin作者PDF的页23–25全部对应文本，§7在页23–24完整；页25式(69)定义完整，但跨页Theorem5的完整条件不在阅读范围。未FULL读33页论文，未采用Theorem5或未读Andrews原定理。DLMF实际web读E1、E7及完整相关固定参数/扇形条件，保存并完整读两个公式TEX。真实源identity和操作范围另存 [dual来源记录](../literature/pade_structure_sources_round223_20261008/dual_source_reading_record_round223_20261008.md)。本稿最终保存后需实际全文作者复读，saved bytes/SHA256另行报告；不会以该动作代替同行独立审阅。
