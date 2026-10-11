# 原有理核的primitive商判别量：首次jet、Plücker高度与真实相位

2026-10-07，NEW，root。Authority为main §§166–170及delivery_hasse_bridge快照 `94eec763f855689bda6ecfb6fd3e4c0af2fef50fcff2e357fc032c720d04d2d3`；564旧冻结记录全部只读，根端本轮已逐项物理SHA核对不变。本文纯纸证，不创建、执行、import或rerun数学producer，不扩prime表。原B6/k3/s5、rank2n整数值饱和基及ξ=αζ(4)+βζ(5)，β≠0保留。

本轮实际FULL读旧lattice I1–I25、partial P1–P14、coupled C1–C23、Hasse H1–H17、partial/mixed analytic A1–A27、node N1–N17。以下新恒等式自证；不继承旧producer执行次数。研究的是有理性假设下的真实核及商，不构造任意自由kernel，也不将矩阵rank当CDT function rank。

## 1. 真实有理核及一个不依赖补基的非零量

先给一般矩阵命题。设B∈Mat_m(Q)实对称、rank d≥1、ν=m−d，V∈Mat_m(Z)严格正定。令

\[
\mathcal K=\ker B\cap\mathbf Z^m,
\qquad K\in\operatorname{Mat}_{m\times\nu}(\mathbf Z)
\text{ 为其完整primitive整数基}.
\tag{K1}
\]

K格是饱和的：若整向量u的非零整数倍在kerB，则u也在kerB。因此可补成U=[L,K]∈GL_m(Z)。此处L是商Z^m/𝒦的整数lift，不能任意取一个高height有理补空间并跳过其index。ν0时约定空det=1、U=L。

由于BK=0，

\[
U^tBU=\begin{pmatrix}C&0\\0&0\end{pmatrix},
\quad C=L^tBL\in\operatorname{Mat}_d(\mathbf Q),
\quad q(B):=\det C\ne0.
\tag{K2}
\]

若换完整K基及unimodular补基，则Lnew=LR+KS、R∈GL_d(Z)，所以Cnew=R^tCR、detCnew=detC。q(B)是原整数格商上的带符号判别量；其绝对值生成一个分式理想，不是挑选某个原坐标minor。

置E为U^−t的前d个columns，p_I=detE_I。E是完整primitive整数矩阵，其最大minors的gcd为1。由B=ECE^t，

\[
\boxed{C_d(B)=q(B)\,p p^t,
\qquad I_d(B)=q(B)\mathbf Z.}
\tag{K3}
\]

第二式因为gcd{p_I p_J}=1；任一prime若整除所有产品，必整除所有p_I，矛盾。这也可从整数unimodular compound变换和K2的唯一非零top block得出。这里d必须是actual rank；若只取低于actual rank的6r外幂，其compound不必rank1，不能借K3。

## 2. 首次Hasse jet的精确因子化及不能免费除去的整数因子

将同一V按U分块为V_LL,V_LK,V_KK，记

\[
a_V(K)=\det(K^tVK)\in\mathbf Z_{>0},
\quad S_V=V_{LL}-V_{LK}V_{KK}^{-1}V_{KL}>0.
\tag{K4}
\]

对t≠0作literal Schur消元再按polynomial identity延至t0，得到

\[
\boxed{\det(B+tV)=t^\nu a_V(K)\det(C+tS_V),
\quad [t^\nu]\det(B+tV)=q(B)a_V(K)\ne0.}
\tag{K5}
\]

所以最先非零jet中的ν个离散source方向实际上全在真实kernel上。K5不需选坐标jet，也不先要求完整detB非零。S_V为同一原V的Schur complement，不能当成免费的独立斜率。

尽管a_V是正整数，**whole-X signed尺度不能免费传给q**。反例：B=diag(1/2,0)、V=diag(1,2)，det(B+tV)=t+2t²∈Z[t]，首次jet为1，而primitive商q=1/2，a_V=2。完整jet整性除以a_V后已丢失。因此q必须使用其自身K3的rank-minor完整整模型，而非直接除原40.3145预算。

## 3. 核高度是精确的compound因子，不是选择补基的height费

在固定原坐标Euclidean规范中定义

\[
\mathfrak h(K)^2=\det(K^tK),\qquad \mathfrak h(K)\ge1.
\tag{K6}
\]

它是primitive核格的covolume，与K基无关。因为det(U^tU)=1，block逆公式给

\[
\det(E^tE)=\det(K^tK).
\]

由Cauchy–Binet，Σ_I p_I²=det(E^tE)。结合K3，得到两个精确norm身份

\[
\boxed{\|C_d(B)\|_{op}=\|C_d(B)\|_F
=|q(B)|\,\mathfrak h(K)^2.}
\tag{K7}
\]

因此actual rank外幂中，primitive商判别量比最大的整体compound norm小一个**核Plücker高度平方**；它不是原饱和paired格自身的covolume。两者坐标空间、对象均不同，不能移用旧lattice I19的lower。

## 4. 同一周期Gram的精确商估计及复数conjugation

现在仅在真实X=ξ处使用原轮廓：B_ij=∫g_i g_j dμ，P_ij=∫g_i overline(g_j)d|μ|，P>0。若ξ=c∈Q，B为上述真实有理B，K确是这个B的核。K对应polynomials的μ-bilinear moments对全部原span消失，Hermitian norm并不消失。

记P按实U=[L,K]分块。为最小化商的正Gram，允许沿实际kernel作complex剪切，令

\[
Z=\overline{P_{KK}^{-1}P_{KL}},\quad \widetilde L=L-KZ.
\]

正Gram约定为\widetilde L^tP\overline{\widetilde L}；上述conjugation不能删除。BK=0使\widetilde L^tB\widetilde L=C完全相同，而正Gram恰为

\[
P_Q=P_{LL}-P_{LK}P_{KK}^{-1}P_{KL}>0.
\tag{K8}
\]

有限complex Gram的Andreief三角界给|detC|≤detP_Q。又det(U^tPU)=detP，所以

\[
\boxed{|q(B)|\le\frac{\det P}{\det(K^tPK)}
\le\frac{\lambda_1(P)\cdots\lambda_d(P)}{\mathfrak h(K)^2}
\le\frac{e_d(P)}{\mathfrak h(K)^2}.}
\tag{K9}
\]

λ按降序。第二步可令K=QR、Q^tQ=I，使用Hermitian compression eigenvalue interlacing，det(Q^tPQ)至少为P最小ν个eigenvalues的乘积，det(R)^2=𝔥²。第三步为positive elementary symmetric sum。也可直接从冻结partial P11与K7得后两项；前一项保留实际kernel的方向，可能严格更强。

K9没有补基L的height损失，因为complex剪切沿BK=0而q不变。它也没有免费新算术基；完整有理商q的finite-place整性仍由K3判断。

任意integer unimodular ambient变基R会同时改变B,P和Knew=R^−1K；精确detP/detP_K不变，但原坐标𝔥和e_d(P)分别可大变。故不能用大shear人为放大𝔥并保留旧e_d费用。比如B=diag(1,0)、P=I₂、R=[[1,N],[0,1]]，新核(-N,1)的𝔥²=N²+1，新的e1(P)=N²+2；没有创造衰减。本文固定已被真实解析界覆盖的原basis。

## 5. 真实非零相位乘积，不再要求top determinant非零

采用冻结coupled C23的实际phase compression

\[
T=P^{-1/2}B(P^{-1/2})^t,
\quad \|T\|_{op}\le1,
\quad B=P^{1/2}T(P^{1/2})^t.
\tag{K10}
\]

它保留μ/|μ|的复phase，不把complex measure换成positive measure。rankT=d，故非零singular values σ1,…,σd皆在(0,1]；后ν个为0。定义**非零**相位乘积Θ_d=∏_(i≤d)σ_i(T)>0，不将全detT=0当可用nonzero scalar。

compound multiplicativity与operator norm给

\[
\boxed{|q(B)|\le
\frac{\lambda_1(P)\cdots\lambda_d(P)}{\mathfrak h(K)^2}\,
\Theta_d
\le\frac{e_d(P)}{\mathfrak h(K)^2}\,\Theta_d.}
\tag{K11}
\]

因为||C_d(T)||=Θ_d，其他两个sqrtP因子的norm乘积为最大的d个λ之积。K7使左边恰为actual rank-one compound norm。这个phase接口不需完整D_n(c)非零；只需已成立的actual rank。仍未证明−logΘ_d有正n²主率，仅O(n)方向上的固定小于1不能自动提供n²增益。

## 6. 覆盖全部可能actual rank的原子式整模型

假设ξ=c∈Q，冻结partial P7给无限n=4r上actual rank d_n∈[3n/2,2n]。原node N4–N9的共同lower其实可严格扩到整个整数区间：3n<p≤4n有u=p−2n>n、d≤2n<2u，因此unit-tail的−5/−3足够，weight3-tail的−2不进入；4n<p≤6n没有这种tail，剩余head的0槽数大于4n，足够任何d≤2n。

因此对所有3n/2≤d≤2n，精确有限u=min(6n−p+1,p−2n)与共同lower仍为

\[
\ell_{p,n,d}=-5\min(d,u)-3\min((d-u)^+,u)
-\min((d-2u)^+,u),\quad3n<p\le6n.
\tag{K12}
\]

nonprincipal node-minor须逐block匹配row/column数、双Cauchy–Binet只需evaluation p整，这些证明均保持。p≤3n沿原−5dE_p，p>6n沿原integrality，2、3、长harmonic和所有fixed denominators没有遗漏。令Q_(n,d)为这些全prime lower的正rational product。

写λ=d/n∈[3/2,2]，令a(x)=min(6−x,x−2)。对3<x<4，coarse下界−5λ的增益为2(λ−(x−2))_+，积分为(λ−1)²。对4<x<6，以u=6−x积分，三段增益面积依次为7λ²/6、λ²/4、λ²/4。于是

\[
G(\lambda)=(\lambda-1)^2+5\lambda^2/3,
\qquad
\boxed{A_{\rm rank}(\lambda)=30\lambda-G(\lambda)
=32\lambda-1-\frac83\lambda^2.}
\tag{K13}
\]

有限u的+1损失uniform O(1)，branch/min/positive-part在λ∈[3/2,2]有统一Lipschitz常数；PNT对这族bounded piecewise-affine函数可先有限网格再uniform逼近。因此

\[
\log Q_{n,d}=-A_{\rm rank}(d/n)n^2+o(n^2)
\quad\text{uniform于此全部整数d}.
\tag{K14}
\]

λ3/2回到41，λ2给157/3；后者只是这个all-rank安全模型，原full determinant仍可采用更好的40.3145，不称此次顶阶费用改善。Q是safe尺度，非最小actual content或其lower。

固定D清αβ、固定M清c，全部d-minors满足(DM)^d minor/Q_(n,d)∈Z。K3及primitive p的gcd1严格给

\[
\boxed{(DM)^d q(B_n(c))/Q_{n,d}\in\mathbf Z\setminus\{0\},
\quad |q(B_n(c))|\ge Q_{n,d}/(DM)^d.}
\tag{K15}
\]

fixed费用O(n)，adaptive actual d_n不改变uniform模型。若c是假设ξ的有理值，K15才能与原轮廓K9/K11比较。没有执行新的matrix或prime实验。

## 7. 可比较的同对象判据及尚未证明的高度/相位主率

冻结实际原basis analytic A4对全部n≤d≤2n给

\[
\log e_d(P)\le-b(d/n)n^2+O(n\log n),
\quad b(\lambda)=\frac{17}2\lambda-\frac{29}3+2\gamma,
\quad\gamma=\lim n^{-2}\log\Gamma_n\ge1.455845.
\tag{K16}
\]

这里γ只引用已审冻结定理；不重算原producer/保存区间。设在假设ξ=c的无限适用n上，actual K_n与d_n满足

\[
\eta_n=\frac{2\log\mathfrak h(K_n)}{n^2},\qquad
\omega_n=-\frac{\log\Theta_{d_n}}{n^2}\ge0.
\]

则K11/K15给以下完整充分条件：若在一个无限subsequence上

\[
\boxed{\liminf_n\left[
b(d_n/n)+\eta_n+\omega_n-A_{\rm rank}(d_n/n)
\right]>0,}
\tag{K17}
\]

就产生q的整数–解析矛盾并排除ξ有理。也可直接证明logdetP−logdetP_K−logQ→负的strict n²率，使用K9而不借弱e_d。

此处所需费用差准确为

\[
A_{\rm rank}(\lambda)-b(\lambda)
=\frac{47}2\lambda+\frac{26}3-\frac83\lambda^2-2\gamma.
\tag{K18}
\]

在λ∈[3/2,2]递增；endpoint分别455/12−2γ与45−2γ。若仅知道η+ω>45−2γ的uniform正余量即可充分，但**未证明实际kernel有如此高度或非零phase有如此损失**。ν0时𝔥=1；不能假定所有无限规模都有非平凡核。全秩分支可接原更好full整模型和top解析，但现有这些也未跨strict。

K17不是用原paired格height代替kernel height，也不是Siegel小向量upper反推大height；有理核由实际B_n(c)确定。所有source constants、原basis、actual d及phase必须同一对象。没有以条件判据宣布新特殊值无理性。

## 8. 文献、闭合范围与下一步

本轮正常TLS新增并保存 Zhang–Cheng, *An Efficient Version of the Bombieri–Vaaler Lemma*, [arXiv1707.05941v1](https://arxiv.org/abs/1707.05941v1)，原件 [PDF](../literature/cdt_paired_kernel_height_sources_20261007/zhang_cheng2017_efficient_bombieri_vaaler_arxiv1707_05941v1.pdf)，7页、283961bytes、SHA `eb1ac14a228b64219dfef2814d430524fb6a7fa8846f6c92f4a27b033193656a`。根端实际完整文本读PDF1–7七页；归档v1页眉与文内date按实际快照保留，不猜别版。其normalized lattice观点启发区分primitive kernel、raw rows及minor content，K1–K18则在本文自证。没有执行其算法。

另浏览Bombieri–Vaaler1983 [出版页](https://link.springer.com/article/10.1007/BF01393823)只核bibliography，全文为订阅内容，未下载/称已读。经典small-vector lemma给的是存在小解的upper；它本身不完成K17的大kernel-height或phase条件。

本轮所得是真实kernel的primitive商scalar、exact rank-one Plücker因子、first jet deflation、正确complex商Gram与非零phase接口、覆盖全部actual rank的明确safe费用曲线，以及同对象strict判据。尚无新ζ/L/Catalan无理性或LI/Lean定理，尚无实际η、ω足够的全尺度lower。

优先下一步估真实detP_K或保留非零phase的rank-d压缩，利用actual moment annihilator条件而非任意补空间；若想用kernel高度，须对原basis的真实K证明lower，不能靠换坐标制造。CDT路线仍另需actual function system的rank、monodromy和cap，K3的matrix rank不是其独立函数数。唯一新主稿待独立FULL审查和作者收审后最终FULL回读，一向来源收据另存；564旧冻结不改动。
