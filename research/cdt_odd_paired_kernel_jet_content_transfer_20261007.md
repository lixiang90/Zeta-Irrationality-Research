# 真实核商的节点源多项式内容：完整费用由41降至635/16

2026-10-07，NEW，作者 /root/masked_racah_finalize。Authority为main §§171–175及 delivery_kernel_profiles JSON，SHA 313ad01a4abe88dd8a8193561b30232dfa131c8832d126af18390eafc8514e72；572冻结记录（567数学、5guards）只读。唯一NEW研究主稿，纯纸证；数学producer创建/execute/import/rerun0，prime实验/辅助单位表扩展0。原B6/κ3/s5、degree<3n、rank2n原饱和整数值基及固定源保留。

## 1. 同一真实核商与新结论

取n=4r、m=2n，g_1,…,g_m为冻结lattice I8的完整基。原 affine form与整数斜率为
\[
B_n(X)=\sum_{j=0}^{6n}W_j\{T_j(X)v_jv_j^t+U_j(v_jd_j^t+d_jv_j^t)\},
\quad V_n=24\sum_{j=0}^{6n}W_jv_jv_j^t,
\tag{Q1}
\]
其中v_j=(g_i(-j))、d_j=(g_i'(-j))，W_j=binom(6n,j)^2 binom(2n+j,j)^3>0，U_j和T_j准确沿冻结J1/N2；先取整数源α、β，β≠0。任意固定有理c处，记actual rank d、ν=m−d及完整primitive核基
\[
K\in\operatorname{Mat}_{m\times\nu}(\mathbf Z),\qquad
\mathcal K=\ker B_n(c)\cap\mathbf Z^m.
\]
冻结kernel K1–K5给U=[L,K]∈GL_m(Z)与不依赖补基的
\[
q=q(B_n(c))=\det(L^tB_n(c)L)\ne0,\qquad
J_{n,\nu}(c)=q\,a_V,\quad a_V=\det(K^tV_nK)\in\mathbf Z_{>0}.
\tag{Q2}
\]
ν=0时取空det=1。这个q属于原有理数c处的实际商，以下没有重新选自由kernel。

**新定理。** 对全部actual 3n/2≤d≤2n，本稿第4节的完整有限处尺度Q^q_(n,d)满足
\[
\boxed{(DM)^d q(B_n(c))/Q^q_{n,d}\in\mathbf Z\setminus\{0\},}
\tag{Q3}
\]
其中D清固定有理α、β，c=a/M固定，D、M>0。令λ=d/n∈[3/2,2]，uniform尺度主率为
\[
\boxed{\log Q^q_{n,d}=-A_q(\lambda)n^2+o(n^2),\qquad
A_q(\lambda)=32\lambda-1-\frac{13}{4}\lambda^2.}
\tag{Q4}
\]
相对冻结all-rank safe费用A_rank=32λ−1−8λ²/3，真实新增收益为7λ²/12。λ=3/2给A_q=635/16=39.6875，旧41降低21/16；λ=2给此模型50，full-rank q=detB仍可另用更好的原whole-X40.3145，本文不称顶阶最优。

数值a_V仍不能免费除。本证明利用同一原节点源的**多变量first-jet内容**，以控制的内容因子替代可能额外相消的a_V。

## 2. 原格的primitive负节点评价与精确内容身份

令N=3n，f_i(z)=binom(z−1,i)，0≤i<N，S∈Mat_(N×m)(Z)为原g基在此Newton基中的矩阵。冻结I7–I8使S为direct summand；K为Z^m中的direct summand，所以SK亦为Z^N中的direct summand。具体把K补为[L,K]，再将S补成完整GL_N(Z)基，所得[SL,SK,H]仍unimodular。因此SK所有ν阶minors的gcd为1，不仅是在Q上满rank。

前N个连续负点的准确evaluation矩阵为
\[
\mathcal E^-_{j,i}=\binom{-j-1}{i},\qquad0\le j,i<N.
\]
其entries为整数。多项式leading coefficients为1/i!，在−j的Vandermonde det为符号乘∏_(i=0)^(N−1)i!，故
\[
\boxed{\det\mathcal E^-=\pm1,\qquad\mathcal E^-SK
\text{ 的全部ν阶minors gcd为1}.}
\tag{Q5}
\]
这个算术身份没有说每个minor是unit；仅确保对每个p至少存在一个unit minor，而且选择可依p。

给原节点独立变量z=(z_0,…,z_(6n))，仅作算术证明用，置
\[
V_n(z)=24\sum_{j=0}^{6n}W_jz_jv_jv_j^t,\qquad
\mathcal F_{n,k}(X,z)=[t^k]\det(B_n(X)+tV_n(z)).
\tag{Q6}
\]
z全1时就是原J_nk(X)，而degree_X F_nk≤m−k。对X=c及k=ν，unimodular U分块后B的核块为0。首阶必须从ν个核方向取ν个source，交叉source项不能在首阶代替任何核source。因此准确有
\[
\boxed{\mathcal F_{n,\nu}(c,z)=q\,\mathcal G_K(z),\quad
\mathcal G_K(z)=\det(K^tV_n(z)K).}
\tag{Q7}
\]
亦可先在kernel source block可逆的z取值作Schur factorization，再以polynomial identity延至全部z；z全1给严格正定，从而可逆开集非空。没有给新源特殊值赋予解析意义。

令R_K的第j行是v_j^tK，真实整数评价。Cauchy–Binet给
\[
\boxed{\mathcal G_K(z)=24^\nu
\sum_{|J|=\nu}\left(\prod_{j\in J}W_j\right)
\det(R_{K,J})^2\prod_{j\in J}z_j.}
\tag{Q8}
\]
distinct node subsets对应distinct monomials，故系数之间没有相消，也没有ν!因子。ν0时G_K=1。设g_K>0为此整数多项式全部系数的gcd，则准确分式内容身份为
\[
\operatorname{cont}_{\mathbf Z}\mathcal F_{n,\nu}(c,z)
=q\,g_K\mathbf Z,\qquad
v_p g_K=\nu v_p24+
\min_{|J|=\nu}\left\{\sum_{j\in J}v_pW_j+2v_p\det(R_{K,J})\right\}.
\tag{Q9}
\]
零minor估值∞。G_K(1)=a_V仅是一次整数specialization，可能有额外p相消；本稿使用g_K，不把v_pa_V等同v_pg_K。

## 3. 5n<p≤6n：全节点系数lower与可支付的内容因子

固定5n<p≤6n。n≥4使p>5、p²>8n、p>3n，原basis monomial/Taylor coefficients均p整。置e=6n−p、u=e+1、T=p−2n>3n；全部residue分为u个unit head/tail pairs、2p−8n−1个weight2单head、2n个weight5单head。原literal block变为
\[
A_j(X,t,z_j)=W_j
\begin{pmatrix}T_j(X)+24tz_j&U_j\\U_j&0\end{pmatrix},
\qquad\det A_j=-(W_jU_j)^2.
\tag{Q10}
\]
独立z_j没有改变任何node支持、真实derivative项或二阶det的source-free身份。unit-head U≥0、T≥−1；unit-tail U≥−4、T≥−5；weight2 head的全部harmonic短于p；weight5 head U整、T≥−1。左右evaluation wedges沿冻结J8：两values至少p，两values加derivative至少p²，全部四rows至少p⁴。证明仅用ordinary Taylor、节点间距p，并准确除回四row步骤的一次非unit scaling，与是否共享z无关。

对每个非零A-minor，两侧node counts相等，两次Cauchy–Binet后所选residue rows总数m。冻结J表在每个source monomial上仍成立；忽略source次数、对同一r取其所有h的最小lower，得到完整安全表：

|residue类型|r=0|r=1|r=2|r=3|r=4|
|---|---:|---:|---:|---:|---:|
|unit两node|0|−5|−8|−5|0|
|weight2单head|0|2|4|不可选|不可选|
|weight5单head|0|4|10|不可选|不可选|

特别r3的含source lower−4高于−5，r2双source lower2高于−8；其余含source分支亦更整。二阶同node无source保持，零系数只加强共同lower。于是对unit两node总有c(r)−2r≥−12，全部single-head总有c(r)−2r≥0。逐residue求和给整个多变量pencil的逐系数界
\[
\boxed{v_p^{Gauss}_{X,t,z}\det(B_n(X)+tV_n(z))
\ge2m-12u=12p-68n-12.}
\tag{Q11}
\]
Gauss含每个X,t,z系数，故对任何k的F_nk亦成立。这里重新纸证实际window bound，不从旧global saved rows或预算数字猜其向独立源的延伸。

另一方面Q5可选前3n负nodes中的一个p-unit νminor。对全部0≤j<3n，有j<p、2n+j<p，因此binom(2n+j,j)为p-unit，binom(6n,j)估值至多1。故
\[
v_pW_j\le2\quad(0\le j<3n),\qquad p\nmid24,
\qquad\boxed{v_p g_K\le2\nu.}
\tag{Q12}
\]
unit-minor的existence使用两层primitive和完整连续evaluation；不要求核上的V_n模p非退化。Q9/Q11因此在固定整数source、c=a/M时给
\[
\boxed{v_p\{M^dq(B_n(c))\}\ge12p-68n-12-2\nu.}
\tag{Q13}
\]
M^d支付F_nν的全部X-specialization系数。Q12是源内容的安全upper，不是a_V估值upper；a_V可有额外相消。

## 4. 固定源分母与全部有限处的完整q模型

固定有理α、β，D清二者，widehat B(Y)=B_(Dα,Dβ)(Y)，节点source斜率仍是同一V_n(z)。准确widehat B(DX)=D B_n(X)，从m−k个B因子、k个整数source因子得到
\[
\widehat{\mathcal F}_{n,k}(DX,z)=D^{m-k}\mathcal F_{n,k}(X,z).
\tag{Q14}
\]
integer-source Q11作用widehat F，再代入DX和c=a/M，给Q13中M^d替为(DM)^d。没有k!分母，也没有给source factors错误付D。

冻结kernel K12–K15已严格覆盖3n/2≤d≤2n的原全部actual-rank minors。其完整signed lower记
\[
\ell^{rank}_{n,d,p}=
\begin{cases}
-5dE_p,&p\le3n,\\
-5\min(d,u_p)-3\min((d-u_p)^+,u_p)
-\min((d-2u_p)^+,u_p),&3n<p\le6n,\\
0,&p>6n,
\end{cases}
\tag{Q15}
\]
其中E_p=floor(log_p8n)，u_p=min(6n−p+1,p−2n)。真实rank-one compound、primitive Plücker gcd1把共同minor lower传给(DM)^dq。小prime2、3及全部长harmonics沿原entry proof；p>6n沿原整性。这些places完全保留，没有仅给有利window就称完整模型。

定义逐n、d、p的精确整数safe lower
\[
\ell^q_{n,d,p}=
\begin{cases}
\max\{\ell^{rank}_{n,d,p},\,12p-68n-12-2(2n-d)\},
&5n<p\le6n,\\
\ell^{rank}_{n,d,p},&\text{其他p},
\end{cases}
\qquad Q^q_{n,d}=\prod_{p\le6n}p^{\ell^q_{n,d,p}}.
\tag{Q16}
\]
Q9/Q12消去的是多变量内容因子，已完整支付其≤2ν；其他p仍用独立rank-minor proof，不除任何未知a_V。所有p给Q3，零minor/零coefficient与ν0边界均覆盖。signed正信用保留。固定(DM)^d只付O(n)，格和real坐标未改变。

## 5. 精确新增面积、全尺度费用与uniform actual rank

令λ=d/n∈[3/2,2]。在5<x=p/n<6，设
\[
b=6-\lambda/2,\qquad c_*=6-\lambda/3,\qquad 5\le b<c_*<6.
\]
冻结rank模型的连续函数及本稿新函数准确为
\[
g_{rank}(x,\lambda)=
\begin{cases}
2x-12-3\lambda,&5<x\le b,\\
6x-36-\lambda,&b<x\le c_*,\\
9x-54,&c_*<x<6,
\end{cases}
\qquad h(x,\lambda)=12x-72+2\lambda.
\tag{Q17}
\]
新函数和g_rank之差分别为10(x−b)、6(x−b)、3x−18+2λ。因此真实共同max的新增信用为0于(5,b)，为6(x−b)于(b,c_*)，为3x−18+2λ于(c_*,6)。后段两端高度是λ、2λ，故
\[
\boxed{\int_5^6(h-g_{rank})_+dx
=3(c_*-b)^2+\frac{\lambda+2\lambda}{2}(6-c_*)
=\frac{\lambda^2}{12}+\frac{\lambda^2}{2}
=\frac7{12}\lambda^2.}
\tag{Q18}
\]
这是相对旧all-rank整模型的实际增益，不是裸node面积或重复whole-det费用。ν=0与λ=2的b=5端点仍成立。

u_p含+1和Q11的−12均仅造成uniform O(1)每prime误差。所有min/max/positive-part函数在compact λ区间统一Lipschitz；PNT θ(t)∼t对bounded piecewise affine test作step上下逼近，再取有限λ-mesh，得到uniform于全部整数3n/2≤d≤2n的
\[
\log Q^q_{n,d}=
-\left(A_{rank}(d/n)-\frac7{12}(d/n)^2\right)n^2+o(n^2).
\tag{Q19}
\]
旧smallprime、固定floor endpoints与p>6n没有遗漏。这证明Q4，是这个显式signed尺度的主率；不声称actual q content达到它或该模型最优。

在λ3/2，收益7(9/4)/12=21/16、A_q=635/16；在λ2，收益7/3、A_q=50。full rank可结合旧whole-X尺度，因为此时ν0、q=detB；ν>0不能因此免费搬原40.3145给q。未知actual d_n可变化，Q19保证adaptive rank不需新分母。

## 6. 精确Smith解释及数值first jet仍未解决的相消

取任一prime，选择整数s_p≥0使A=p^(s_p)B_n(c)为Z_p矩阵。设其非零Smith diagonal entries的估值为a_1≤…≤a_d；d是actual rank，余ν个Smith diagonal entries为0（不是估值为0）。实际top determinantal ideal沿冻结K3等于q(B)Z_p，故
\[
\boxed{v_pq(B_n(c))=\sum_{i=1}^d a_i-ds_p,\qquad
v_pJ_{n,\nu}(c)=v_pq+v_pa_V.}
\tag{Q20}
\]
这区分实际q的Smith内容与source restriction discriminant；V_n在全格p-unimodular也不一般使a_V为unit。

一般反例可完全纸证：取odd p且−1在F_p有square root，对任意N迭代a_(s+1)=a_s+k p^s、选择2a_s k使1+a_(s+1)^2≡0 modp^(s+1)，取得整数a且p^N|1+a²。置
\[
B=\begin{pmatrix}a^2&-a\\-a&1\end{pmatrix},\quad
K=(1,a)^t,\quad L=(0,1)^t,\quad V=I_2.
\]
U=[L,K] unimodular，q=1、a_V=1+a²任意高p整除；first jet的额外divisibility不传给q。若给两个坐标独立source，G_K(z)=z_1+a²z_2的content恰1。这不是原模型prime表或新unit实验，仅反驳一般的免费除法。

Q9的weighted evaluation内容是本稿的具体可用替代。未来若原真实K满足更便宜的weighted unit-minor支持，可把Q12的2ν再降；本文没有宣称该支持已证明，也没有由small-solution upper推出kernel-height lower。

## 7. 同一q的解析接口及还缺的strict余量

只有假设真实ξ=αζ4+βζ5等于c∈Q，才可把Q3与原轮廓解析q估计比较。冻结kernel K11/K16给
\[
|q|\le e_d(P)\Theta_d/\mathfrak h(K)^2,\quad
\log e_d(P)\le-b(\lambda)n^2+O(n\log n),\quad
b(\lambda)=17\lambda/2-29/3+2\gamma.
\]
记η_n=2log𝔥(K_n)/n²、ω_n=−logΘ_(d_n)/n²，新的同对象充分条件为
\[
\boxed{\liminf_n\{b(d_n/n)+\eta_n+\omega_n-A_q(d_n/n)\}>0.}
\tag{Q21}
\]
新须补的差值减少7λ²/12，准确为
\[
\boxed{A_q(\lambda)-b(\lambda)=
\frac{47}{2}\lambda+\frac{26}{3}-\frac{13}{4}\lambda^2-2\gamma.}
\tag{Q22}
\]
但尚未证明真实η、ω或det(KᵀPK)的充分n² lower。特别d3n/2的原解析保证衰减率仅>5.99，新safe39.6875仍未被跨越；不是移用完整det的>12.6234。actual nonzero q在冻结H6适用的无限n上存在，rank可变化、kernel亦可为空。矩阵rank不等于CDT function rank。

独立node变量仅用来证明这个原q的算术内容，不替换数值目标、原B_n(c)、原P_n、原V_n或原kernel，不把该多变量family的任意值当无穷非零period证书。没有新的ζ/L/Catalan无理性、线性无关性或Lean结论。

## 8. 实际读域、来源与冻结状态

本轮实际FULL：最终kernel K1–K18/8节及独审；lattice I1–I25；node N1–N17；Hasse arithmetic J1–J18；all-prime B1–B22；Hasse bridge H1–H17。另实际FULL读supported T1–T18与global O1–O20作为背景，新增window Q11自证，不需要借旧saved113 rows或重算其积分。初次合并输出截断后，J/N/B以充足独立预算完整补读；不把截断片段算FULL。main actual §§171–175及audit完整JSONparse/顶级字段/头部与物理SHA，不冒称人工全文读572记录或本人全baseline物理审计。

新关键证明均由primitive嵌入、连续整数evaluation、multivariate Cauchy–Binet内容、literal node coefficient表与价格2、逐prime共同max及PNT面积在正文自证。无需新外部数学定理；新增PDF/HTML/code归档0、原始PDF实际新页0，不继承Zhang–Cheng或其他人原件页数。旧、成功/失败、同行producer和guards只读；本轮数学producer创建/execute/import/rerun0、失败0、prime扩表0。

本稿是唯一NEW完整候选，待actual FULL正式独审、收审后最终作者FULL回读及单向FINAL来源收据。572旧记录不动，safe费用upper不是actual cost lower、content等号、optimality或普遍no-go；不预先宣布闭合或strict margin。
