# 原行列式的正定X斜率与低阶Hasse jets：无限非零、预算继承和混合Gram

2026-10-07，NEW，root。当前authority为main §§161–165及delivery_partial_global快照f72fe28c；556既存冻结记录全部只读。原B6/k3/s5、degree<3n、rank2n饱和整数值格S和真实源ξ=aζ4+bζ5（b≠0）保留。本稿纯纸证：不创建、execute、import或rerun任何数学producer，不扩辅助prime表。取得的是实际原行列式低阶导数的完整接口，尚非特殊值无理性定理。

## 1. 实际X斜率是正定整数矩阵

本轮实际FULL读冻结[local Gram G1–G15](cdt_odd_paired_actual_local_gram_layers_20261006.md)、[partial P1–P14](cdt_odd_paired_partial_compound_transfer_20261007.md)、[coupled C1–C23](cdt_odd_paired_coupled_gram_decay_20261007.md)、[supported T1–T18](cdt_odd_paired_supported_weighted_dual_transfer_20261006.md)及[low-price L1–L18](cdt_odd_paired_low_price_support_domination_20261007.md)。没有运行其旧证书。a,b先取固定整数；固定有理源清同一分母只改变O(n)费用。

令m=2n，g_1,…,g_m是原S的实际整数值多项式基。原B_n(X)实对称，关于X affine。冻结G3的真实权重为

\[
W_j=\binom{6n}{j}^{2}\binom{2n+j}{j}^{3}>0,\quad0\le j\le6n,
\qquad B_n(X)=A_n+X V_n,
\]
\[
\boxed{V_n=\partial_XB_n(X)
=24\sum_{j=0}^{6n}W_j\,v_jv_j^t,
\quad v_j=(g_i(-j))_{i=1}^{m}\in\mathbf Z^m.}
\tag{H1}
\]

所以V_n为整数矩阵，而且严格正定：若u≠0，原basis独立使g_u=Σu_i g_i非零，其degree<3n；不可能在6n+1个不同的-j全部为0。因此u^tV_nu>0。这个正性来自真实square/cube权重，不是对complex轮廓Gram的正性假设；若把W_j错误换成带符号的权重，以下结论不能免费保留。

令D_n(X)=detB_n(X)，则

\[
\boxed{\deg D_n=m=2n,\quad [X^m]D_n=\det V_n\in\mathbf Z_{>0}.}
\tag{H2}
\]

这证明whole-X多项式非恒零，不证明D_n(ξ)无限非零。

## 2. 所有根为实数，零点重数恰为实际亏秩

对每个固定实c，V_n^{-1/2}B_n(c)V_n^{-1/2}是实对称矩阵。其特征值λ_1,…,λ_m全实，且

\[
D_n(c+t)=\det V_n\prod_{i=1}^{m}(\lambda_i+t).
\tag{H3}
\]

取c=0已说明D_n的所有复根都在实轴；对任意实c，其在c处的零阶准确为

\[
\boxed{\operatorname{ord}_{X=c}D_n=m-\operatorname{rank}_{\mathbf R}B_n(c).}
\tag{H4}
\]

这里实对称加正定斜率排除了零特征值的非半单问题。若只知道任意非对称矩阵的rank，则一般不能推出H4。

定义Hasse derivative

\[
J_{n,k}(X)=\frac{D_n^{(k)}(X)}{k!}
=[t^k]D_n(X+t),\qquad0\le k\le m.
\tag{H5}
\]

若ν=m−rankB_n(c)，则J_{n,k}(c)=0（k<ν），J_{n,ν}(c)≠0。选kerB_n(c)及其正交补的实orthonormal bases时，还准确有J_{n,ν}(c)=det(B_n(c)|_{ker^⊥})det(V_n|_{ker})；cross项在这个首次非零阶不贡献。

## 3. 无限非零可由原部分rank转到至多n/2阶jets

冻结P7对每个固定有理a,b,c、b≠0，用无限p≡1 mod18证明：在无限n=4r上，原B_n(c)的rank至少6r。源和c不随p改变。由H4–H5立刻得到

\[
\boxed{\text{无限 }n=4r\text{ 上，存在 }0\le k\le2r=n/2
\text{ 使 }J_{n,k}(c)\ne0.}
\tag{H6}
\]

k允许依n、c改变；不声称某固定k或k=0无限适用。若实际ξ被假设等于有理c，才把H6用于ξ。这个定理保留original determinant polynomial，而不挑一个尚未证明非零的完整D_n(c)。

也可避免选择k，设K_n=n/2（n=4r），

\[
F_n(X)=\sum_{k=0}^{K_n}J_{n,k}(X)^2.
\tag{H7}
\]

则对每个固定有理c，F_n(c)>0在无限适用n上成立。它是一个canonical实非负scalar certificate；没有把平方和的正性当作真实D_n(ξ)的非零。

## 4. 所有jets直接继承whole-X的完整signed整化预算

冻结supported T13–T17在同一原S和全部有限处证明存在正有理signed尺度Q_n，

\[
D_n(X)/Q_n\in\mathbf Z[X],\qquad
\liminf n^{-2}\log Q_n\ge-A_{\rm full},
\]
\[
A_{\rm full}=
\frac{800671681093752110193539327219}{19860629178118281482813083200}
<40.314517427.
\tag{H8}
\]

该值只是safe upper fee，不是最小分母或费用lower。若D_n(X)/Q_n=Σd_iX^i，则

\[
\boxed{J_{n,k}(X)/Q_n=
\sum_{i\ge k}\binom ik d_iX^{i-k}\in\mathbf Z[X].}
\tag{H9}
\]

Hasse的k!不引入新分母，因为binom(i,k)整数。对c=u/M，M>0，

\[
M^{m-k}J_{n,k}(c)/Q_n\in\mathbf Z,
\quad J_{n,k}(c)\ne0\Longrightarrow
|J_{n,k}(c)|\ge Q_n/M^{m-k}\ge Q_n/M^m.
\tag{H10}
\]

所以H6的adaptive低阶jet共享同一40.3145预算，优于上一轮全部6r-minors的粗45预算；不从X处原matrix entries声称同样预算。Q_n^{-2}F_n(X)∈Z[X]，且M^{2m}F_n(c)/Q_n²为非负整数，H7非零时F_n(c)≥Q_n²/M^{2m}。fixed source分母和M均只付O(n)。

## 5. 每个jet的真实解析对象是混合轮廓—离散Gram

只在X=ξ使用冻结C23/P8的实际复Gram，记

\[
B_n(\xi)_{ij}=\int_\Gamma g_i(z)g_j(z)d\mu_n(z),\qquad
P_{n,ij}=\int_\Gamma g_i(z)\overline{g_j(z)}d\nu_n(z),\quad d\nu_n=|d\mu_n|.
\]

P_n是严格正定Hermitian Gram，指数tail保证所有积分绝对收敛。另定义实际有限正离散measure

\[
d\sigma_n=24\sum_{j=0}^{6n}W_j\delta_{-j}.
\tag{H11}
\]

g_i在其real节点实值，所以关于σ的bilinear和Hermitian Gram都恰为V_n。由affine matrix identity，D_n(ξ+t)是measure μ_n+tσ_n的bilinear Gram determinant；没有声称ξ+t仍由原cot轮廓alone表示，也没有改变目标ξ。

对m−k个轮廓variables z及k个discrete variables s，把两集合并记w。有限Andreief直接给

\[
J_{n,k}(\xi)=\frac1{(m-k)!k!}
\int_{\Gamma^{m-k}\times\mathbf R^k}
\det[g_i(w_l)]^2\prod d\mu_n(z)\prod d\sigma_n(s).
\tag{H12}
\]

重复discrete节点时det为0；无需额外选择node支撑。取total variation后得到准确coefficientwise bound

\[
\boxed{|J_{n,k}(\xi)|\le H_{n,k}:=[t^k]\det(P_n+tV_n)
=\frac1{(m-k)!k!}\int|\det[g_i(w_l)]|^2
\prod d\nu_n(z)\prod d\sigma_n(s).}
\tag{H13}
\]

所有H_{n,k}>0。也可由det(P_n+tV_n)=detP_n·det(I+tP_n^{-1/2}V_nP_n^{-1/2})看出其非负系数。k=0回到|D_n(ξ)|≤detP_n；k>0必须支付k个真实discrete observations，不能借用k=0的衰减率。

## 6. det1剪切对整个pencil和全部jets依旧精确不变

若T_n为与X独立的真实可逆实basis变换、detT_n=1，则

\[
\widetilde B_n(X)=T_n^tB_n(X)T_n,
\quad\widetilde V_n=T_n^tV_nT_n,
\quad\widetilde P_n=T_n^tP_nT_n.
\]
\[
\boxed{\det\widetilde B_n(X)=D_n(X),\quad
[t^k]\det(\widetilde P_n+t\widetilde V_n)=H_{n,k}.}
\tag{H14}
\]

因此已有real/rational q剪切可以用于同一个混合determinant；所有jets共享恒等式和原whole-X整化，不付partial inverse-compound norm。一般complex变换的Hermitian Gram须使用T^tP overline(T)，而非把它误写为T^tPT；当前真实q配置全实，H14足够。

这项便利不能被理解成删除q的实际head values、discrete Gram或Γ计费。优化后H13右侧中的V同样被变换，不能让V保持旧基又让P单独采用新基。partial6r minors则依旧需要冻结P13的inverse剪切费用；它们是不同的解析对象。

## 7. 低阶jet的同对象严格比较门槛

因H_{n,k}≥0，对每个0<R≤1，

\[
\boxed{\max_{0\le k\le K_n}|J_{n,k}(\xi)|
\le R^{-K_n}\det(P_n+RV_n),\qquad K_n=n/2.}
\tag{H15}
\]

这是coefficients非负后的合法比较，不是由一个pointwise determinant上界免费比较每个coefficient。取R_n=e^{-τn}，τ≥0固定，设

\[
\Psi(\tau)=\limsup_{n\to\infty,\ 4\mid n}
n^{-2}\log\det(P_n+e^{-\tau n}V_n).
\tag{H16}
\]

于是准确有limsup n^(-2)log(max_{k≤K_n}|J_{n,k}(ξ)|)≤Ψ(τ)+τ/2。若真实地证明某τ满足

\[
\boxed{\Psi(\tau)+\tau/2<-A_{\rm full},}
\tag{H17}
\]

就证明ξ无理：假设ξ=c∈Q，H6在无限n给nonzero低jet，H10/H8给其绝对值至少exp(−A_full n²−o(n²))，而H15–H17给同一所有低jets严格更快下降，矛盾。也可用F_n：F_n(ξ)≤(K_n+1)R_n^{-2K_n}det(P_n+R_nV_n)²，与H7/H10的平方整模型产生相同门槛。

无限适用n只由P7证明，不声称所有n非零。这里不需要把matrix rank6r当CDT函数独立秩；它是直接同对象整数–解析矛盾接口。若另用CDT，应独立构造真实function/period系统并验证其秩、分母和单值leaf。

## 8. 本轮研究结论、来源及未闭合项

新增结论是：actual X斜率整数SPD、D_n的全部实根和准确zero multiplicity；fixed rational source的至多n/2阶Hasse jet无限非零；所有jets与canonical square certificate的原40.3145完整signed预算；准确mixed measure积分、coefficientwise解析界及det1不变性；明确H17严格门槛。它把上一轮partial逆剪切和较粗45费用的困难，转为真实mixed discrete/contour分析，未把困难消除或宣称已跨过余量。

H17目前未证明。原full det的>12.62342839512558保守衰减只涉及k0，不能直接用于n/2阶jet。V_n是整数SPD而非小量；必须估计其与P_n的真实相对谱、混合支撑和Γ/head/剪切成本。也可改善真实复相位或实际高压缩，不能只选一个很小R却漏R^{-K_n}。

一手背景为Borodin, *Biorthogonal ensembles*, [arXiv math/9804027v1](https://arxiv.org/abs/math/9804027v1)，既存原件`literature/cdt_paired_complex_gram_sources_20261007/borodin1998_biorthogonal_ensembles_math9804027v1.pdf`，归档26页、234234bytes、SHAc89a7cc9334e434531769f6a9202edd0ae58c2f4fa7da3490fc5f89ea88c75f0。本轮实际完整文本读取PDF2–7六页，其中5–7包含finite moment Gram和2.8–2.14 general biorthogonal形式；没有新下载或render。本文有限mixed Andreief证明直接在H12–H13写出，不套其Jacobi/Laguerre/Hermite asymptotic model，不继承旧coupled作者的34页或称整PDF已读。

数学producer新建/执行/import/rerun0、失败0、辅助素数扩表0、Lean0。无新的ζ/L/Catalan无理性或线性无关性结论。正式独审、作者最后FULL回读及一向FINAL来源另存；当前本文待独审，不提前宣布闭合。
