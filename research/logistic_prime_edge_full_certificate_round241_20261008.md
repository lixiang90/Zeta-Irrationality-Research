# 第241轮：K5完整素数边缘非零证书

2026-10-09，Root。延续240固定对象；轮次文件仍沿用20261008标签。以下是自含纸面证明，不是Lean核验证。三个固定常数另由C纸证、Root一次精确有理数运算核对；并未通过枚举素数推断全尺度结论。

## 1. 对象与结论

固定n=p−1，p≥7为素数，h=3n，D_m(t)=∏_{j=1}^m(t+j)，R_n=D_n⁴/D_(5n)。令B⁺为Bernoulli泛函，B⁺(t^e)=B_e⁺，B_1⁺=1/2。对具有有理商部、简单负整数极点的G定义有理泛函

\[
 V_r(G)=B^+(P^{(r)})+(r+1)!\sum_j c_jH_j^{(r+2)},
 \quad G=P+\sum_j\frac{c_j}{t+j},\qquad r=1,3.
 \tag{1}
\]

V_r在局部变量u上用同一公式，允许极点0，H_0=0。真实数值泛函在240稿已付；本轮用(1)处理其完整有理部分。对f=t^eR_n，设G=tf，a(f)=−Σ_jc_j，定义

\[
 U_T(f)=\tfrac32 V_1(tf)+\tfrac1{24}V_3(tf)+a(f)T,
 \quad Q_n(T)=\det[U_T(t^{i+j}R_n)]_{0\le i,j<h}.
 \tag{2}
\]

在真实T=X=3ζ(3)+ζ(5)处，(2)等于240的完整logistic moment矩阵。这里没有删除商部或任一调和头。

令
\[
 \mathcal E=\{2,3,5,19,59,131,1609,2953,7477,706337,3110519\}.
\]
本稿证明，对p≥7且p∉E：

1. 所有系数满足v_p([T^k]Q_(p−1))≥5−9p+5k，常数系数恰为5−9p。
2. Q_n的primitive整数多项式P_n具有p-单位常数项，且v_p([T^k]P_n)≥5k（k≥1）。特别P_n模p是非零常数。
3. 对任意固定q∈Q，所有上述p并满足p∤den(q)时P_(p−1)(q)≠0。因此实际有理关系点的非零在无限多个无界尺度上成立。
4. 归一化Qtilde=S_n^(3n)Q_n/F_n的完整系数Gauss valuation恰5−3p；其primitive比例的该素数费用是3p−5。

这些结论不证明X无理。所需全部素数、全部n的净primitive费用仍未付；同对象实界−6的完整认证也未付。

## 2. 保留完整商部与调和头的分解

写M_b={m≥0: 1≤b+pm≤5n}，N_b(u)=∏_(m∈M_b)(u+m)，ℓ_b=|M_b|，b=0,…,p−1。M_b⊂{0,1,2,3,4}，其中零类是{1,2,3,4}；低类1≤b≤p−5是{0,…,4}，四个高类p−4≤b≤p−1是{0,…,3}。

对G=A(t)/D_(5n)(t)，令
\[
 g_b(u)=G(pu-b),\quad L=10n+2,\quad
 g_{b,L}(u)=\frac{[u^{<L}](N_b(u)g_b(u))}{N_b(u)}.
 \tag{3}
\]
截断是far单位分母在0的形式Taylor展开。对本列池degA≤10n−1，G的商部次数≤5n−1，故多项式商部乘N_b后次数<L。(3)精确保留该部分；一个near简单极点也精确保留，因为N_b/(u+m)的次数<L。

多项式满足完整分布恒等式
\[
 V_r(P)=p^{-(r+1)}\sum_{b=0}^{p-1}V_r(P(pu-b)). \tag{4}
\]
证明可用B⁺(e^{zt})=z/(1−e^(−z))：Σ_b e^(−bz) B⁺(e^(pzu))=p B⁺(e^(zt))，随后比较系数并付链式微分的p^r。这里只对多项式使用生成函数，不给无限形式级数套未证明的泛函连续性。

对全局单极点1/(t+j)，唯一near盘b=j modp给g_b=p^(−1)/(u+⌊j/p⌋)。它的分布项为
\[
 (r+1)!p^{-(r+2)}H_{\lfloor j/p\rfloor}^{(r+2)}.
\]
与全局(r+1)!H_j^(r+2)相比，含p的全部调和项精确取消，余下求和只含p-单位分母。这包括j>p的所有heads。

在任何far盘w=j−b是p-单位。F(u)=1/(w+pu)=Σ_e a_eu^e，其中v_p(a_e)=e。设M=ℓ_b，K=L−M，q_K=[u^{<K}]F。因为deg(N_bq_K)<L，
\[
 g_{b,L}-q_K=\frac{[u^{<L}](N_b(F-q_K))}{N_b}.
 \tag{5}
\]
右侧分子所有系数valuation≥K。整数首一除法与Lagrange残数（节点差绝对值≤4）证明：对任何p-整分子S，v_p(V_r(S/N_b))≥−1。商部Bernoulli分母至多损1；全部near调和分母均p-整。因此(5)经V_r后valuation≥K−1≥r。

另一方面V_r(q_K)的非零项从e=r开始，a_e贡献e；e=r,r+1分别涉及B_0、B_1，其余项至少e−1≥r+1。故v_p(V_r(g_(b,L)))≥r。乘p^(−r−1)后每个far项至多损1。因此单极点的完整分布误差valuation≥−1；这是全部near/far项的证明，不是仅保留j=p。

若每个局部numerator A(pu−b)的Gauss valuation≥E_b，记β=min_b(E_b−ℓ_b)。因为5n<p²，每个同类不同极点差恰含一个p，其余差都是p-单位，故全局残数c_j满足
\[
 v_p(c_j)\ge E_{j\bmod p}-\ell_{j\bmod p}+1\ge\beta+1.
 \tag{6}
\]
按完整部分分式线性相加，并用(4)精确处理商部，得到
\[
 v_p\left(V_r(G)-p^{-(r+1)}\sum_bV_r(g_{b,L})\right)\ge\beta,
 \qquad r=1,3. \tag{7}
\]
因此(2)的有理截距与
\[
 \frac1{24}p^{-4}\sum_b\big(V_3(g_{b,L})+36p^2V_1(g_{b,L})\big)
 \tag{8}
\]
之差valuation≥β。目标T的系数−Σc_j也由(6)有valuation≥β+1。(7)是本轮新的完整高阶分布引理；没有继承原K3的误差或−2尺度。

## 3. 完整CRT基与所有交叉圆盘

取m_0=4，低类m_b=3，高类m_b=2；Σm_b=3p−3。完整基为
\[
 \phi_{b,i}(t)=(t+b)^i\prod_{d\ne b}(t+d)^{m_d},\quad 0\le i<m_b.
 \tag{9}
\]
次数<h。模p时，各类中心不同；在每个中心依次取jet得到可逆三角系数表，所以基系数矩阵T是p-单位。对任意线性泛函，双线性展开给detGram=det(T)²Q_n；这一步不依赖原K3泛函。

对a=(b,i),c=(b',k)，设z_a(d)=i若d=b，否则m_d；定义
\[
 e_d=\begin{cases}1&d=0\\4&d\ne0,\end{cases}\qquad
 E_d=e_d+z_a(d)+z_c(d).
\]
实际G=tφ_aφ_cD_n⁴/D_(5n)的盘d局部式严格是
\[
 g_d= p^{E_d-\ell_d}\frac{u^{E_d}K_d(u)}{N_d(u)},
 \quad v_p([u^r]K_d)\ge r,\quad K_d(0)\text{是p-单位}. \tag{10}
\]
这是逐个整数根因子在t=pu−d处展开；所有other-class差的常数项都是单位，far分母逆的第r项至少含p^r，故(10)不是猜测的局部模型。因E_d≤10，且E_d+1−ℓ_d≤6，V_3(u^E/N_d)与V_3(u^(E+1)/N_d)均p-整：商部最高次数≤6，三次微分只涉及B_0,…,B_3，分母只含2、3；残数的H_m⁵亦p-整。更高项用普遍valuation≥−1与额外p^r（r≥2）。因此K_d−K_d(0)导致额外至少一个p。V_1整体至多损1，(8)中的36p²保证其相对最高阶项额外至少一个p。

令c'_b=e_b−ℓ_b−4，零/低/高分别−7,−5,−4，ρ_(b,i)=c'_b/2+i。最大ρ为−1/2。给每行列乘p^(−ρ)；可在Q_p(√p)中操作，所有最终determinant和系数都仍在Q_p。

同类自身盘：E_b=e_b+i+k；抽出(pu)^(i+k)后，两基向量的余因子相同，所以K_b及w_b=K_b(0)不随i,k变化。主项valuation c'_b+i+k=ρ_a+ρ_c，归一化后为单位w_b/24乘固定V_3块。所有其它盘E_d=e_d+2m_d，E_d−ℓ_d−4分别1、1、0；归一化后excess≥1。

异类盘：在a类的excess为c'_a/2+m_a−ρ_c，c'/2+m分别1/2、1/2、0，故excess≥1/2；c类同理。其余盘excess≥1。所有交叉盘在剩余域中消失。上述逐盘同样证明
\[
 \beta_{ac}=\min_d(E_d-\ell_d)\ge\rho_a+\rho_c+4. \tag{11}
\]
(7)的完整分布误差归一化后valuation≥4；T系数由(6),(11)归一化后valuation≥5。因此整个归一化矩阵在剩余域中，是与T无关的三个类型固定块的直和。并且每个T系数在p⁵内。

## 4. 固定块与真正的无限非零

取
\[
 r_0=\frac u{(u+1)(u+2)(u+3)(u+4)},\quad
 r_L=\frac{u^3}{(u+1)(u+2)(u+3)(u+4)},\quad
 r_H=\frac{u^3}{(u+1)(u+2)(u+3)}.
\]
固定块分别[V_3(u^(i+j)r_type)]，sizes4、3、2。C独立纸推得到
\[
 \det M_0=\frac{541936393813}{62208},\quad
 \det M_L=-\frac{100344353231}{3888},\quad
 \det M_H=-\frac{210779}{4}. \tag{12}
\]
其完整计算使用多项式商部和全部局部残数，零/低块右下角的商部三阶微分项6不可漏。Root唯一精确运行以integer monic division独立重新计算(12)，一致；没有计算随p增长的矩阵或枚举素数。分子因子分别59·2953·3110519、19·7477·706337、131·1609，分母只含2、3。因此p≥7且p∉E时，每个块和每个w_b/24都是单位。

归一化后的determinant常数项是单位，所有[T^k]系数valuation≥5k。归一化总指数
\[
 \Lambda=2\sum_a\rho_a
 =4(-7)+4\cdot3+(p-5)(3(-5)+3\cdot2)+4(2(-4)+2)
 =5-9p. \tag{13}
\]
det(T)²为单位，故第1节第一项成立。primitive化时标量valuation恰−Λ，使常数项为p-单位，其余系数valuation≥5k。对于p∤den(q)，P_n(q)模p即这个非零常数；排除固定有限E及固定den(q)只去掉有限个素数，Euclid定理给无限多个p。至此证明的是实际完整P_(p−1)(q)非零，不是generic determinant或有限头的非零。

最后vp(S_(p−1))=4，vp(F_(p−1))=2Σ_(i=0)^(3p−4)⌊i/p⌋=6p−12，因此scale的valuation为6p。结合(13)，Qtilde的Gauss valuation=5−3p；其primitive比例在这个p处的valuation=3p−5。单个素数边缘费用O(n logn)不能代表全素数累计n²费用。

## 5. 进展与下一项门槛

已付完整投影、完整安全整模型、实际关系点的无限非零；新增auxiliary prime处精确Gauss费用。仍未付全素数primitive净费用低于同对象实界，也未完整认证原能量证书。没有得到新的数值无理性定理。

下一輪不延长本轮已经完成的prime-edge证明或增加样本。只检验该同一完整Qtilde在全部prime/window下的Gauss净费用是否能越过实界；必须包括F_n和最高阶引入的深度。241–244主窗口不变；正式复盘仍从240计数，默认246，允许244–248。
