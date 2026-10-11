# 原配对行列式的单一 bordered 非零门槛与退化强块的 Smith 型

2026-10-06，root，NEW 全尺度推导。471既存数学文件、成功或失败producer、JSON及最终来源收据全部冻结只读；本文不执行/import任何旧或同行数学producer。保留原 B6/k3/s5、actual saturated rank2n integer-valued paired格与真实 half jet。本文推进原目标非零性，未证明新ζ/L无理性定理。

## B1. 实际输入、尺度与不能省略的提升

本轮实际全文重读 [auxiliary原稿](cdt_odd_paired_head_free_auxiliary_prime_20261006.md) A1–A13、[modified target稿](cdt_odd_paired_jacobi_modified_target_normality_20261006.md)13sections/T1–T27、[weighted稿](cdt_odd_paired_weighted_jet_support_budget_20261006.md)W1–W10。原auxiliary稿A2–A7的modp²实际paired lifts及各阶误差是本稿输入；以下另给无需G0逆的完整线性代数证明。

取n=2m，p=9m+1为素数，故m=2r、n=4r、p=18r+1。记负节点a_l=−l，0≤l<3m，A(t)=(t)_{3m}，S(t)=∏_{z=1}^{4m}(t−z)，reflection c−t、c=4m+1。令V=F_p^{3m}，T为degree<m reflection-even polynomials（维t=m/2），Q为degree<3m reflection-even polynomials（维q=3m/2）。

实际negative evaluation image E维e=5m/2；其annihilator满秩矩阵L和derivative矩阵J为
\[
L_{i,l}=\frac{T_i(a_l)}{A'(a_l)S(a_l)},\qquad
J_{l,j}=A'(a_l)Q_j(a_l),\qquad E=\ker L.
\tag{B1}
\]
这些是固定真实T/Q基，不增加局部自由度。令
\[
D=\operatorname{diag}(W_{p+l}),\quad
\kappa=\frac{(3m-1)!^2}{(4m)!^3}\in F_p^\times,
\quad W_{p+l}=\kappa S(a_l)^3/A'(a_l)^2.
\tag{B2}
\]
所有分母是unit。χ=1_{I(a)=0}，I=gcd(A(t),A(c−t))，η=χ/2，k=5−6η，d=(1−k²)/6；K=diag(k)，D_d=diag(d)。真实shared节点η=1/2仍保留，k是outer5/middle2，不能改成裸AQ。

选择E基Z、L的右逆F，U=[Z,F]是GL(V)，LF=I。选择actual saturated paired格的strong lifts（image Z）和真实weak lifts
\[
P_Q=AQ+\frac p2(A/I)I'Q+O(p^2\mathbf Z_p[t]_{<6m}).
\tag{B3}
\]
原约束满射保证B3能修正为char0中精确paired polynomial；其与原完整S基的变换行列式τ是p-unit。该步骤不要求G0或任何Gram可逆。

## B2. 完整归一化矩阵，避免先对强块求逆

令u=6b为p-unit（fixed有理sources避开有限分母及b的素因子），M(X)=p^5B_X在上述actual局部基中；D_p=diag(I_e,pI_q)。原A7支付全部head、tail、source及W误差后，
\[
M(X)=D_pN(X)D_p,\qquad N(X)\in\operatorname{Mat}_{4m}(\mathbf Z_p[X]),
\]
\[
\overline N=u\mathcal N,\qquad
\mathcal N=
\begin{pmatrix}
-6Z^tDZ&Z^tDKJ\\
J^tKDZ&J^tDD_dJ
\end{pmatrix}.
\tag{B4}
\]
归一化后strong/weak的p与weak/weak的p²已分别支付。原a-source及X-source不进入B4；它是whole-X常数矩阵。到此没有除强块，所以即使G0奇异，B4仍完全合法。

## B3. 受约束形式的 bordered 恒等式

考虑known-unit ambient块上的完整矩阵
\[
\Psi=
\begin{pmatrix}
-6D&DKJ&L^t\\
J^tKD&J^tDD_dJ&0\\
L&0&0
\end{pmatrix}.
\tag{B5}
\]
先以U=[Z,F]改变V坐标、同时行列重排为(E,Q,F,T)。变成
\[
\begin{pmatrix}\mathcal N&C&0\\C^t&B&I_t\\0&I_t&0\end{pmatrix}.
\]
已知后2t块逆的左上部分为0，故top Schur不改变\(\mathcal N\)。其det是(−1)^t，得到
\[
\boxed{\det\mathcal N=(-1)^t(\det U)^2\det\Psi,\qquad
\operatorname{corank}\mathcal N=\operatorname{corank}\Psi.}
\tag{B6}
\]
同一个congruence将Ψ分成\(\mathcal N\)与已知hyperbolic块，证明corank；没有使用未知restricted form的逆。

现在只除ambient −6D。因为d+k²/6=1/6，Schur余块准确为
\[
\frac16
\begin{pmatrix}
J^tDJ&J^tKL^t\\LKJ&LD^{-1}L^t
\end{pmatrix}
=\frac16
\begin{pmatrix}\kappa H_0&C_5^t\\C_5&\kappa^{-1}G_0\end{pmatrix}.
\tag{B7}
\]
其中G0/H0/C5正是原unfolded真实矩，fold后就是原λ2的M5。右侧仅对原M5作unit左右缩放及同步重排，其det为6^{−2m}κ^m detM5，corank同M5。结合m偶数，得到**不要求G0非零的**恒等式
\[
\boxed{\det\mathcal N
=(-1)^t(\det U)^2 6^m\kappa^m\det D\,\det M_5,
\quad\operatorname{corank}\mathcal N=\operatorname{corank}M_5.}
\tag{B8}
\]
每个外部因子是明确unit。G0的det在旧strong Schur中出现又消失；它不是原whole determinant非零的独立必要条件。

## B4. 原whole polynomial的单一充分必要leading gate

actual基det τ和D_p给
\[
\boxed{p^{17m}D_A(X)\bmod p
=\tau^{-2}u^{4m}(-1)^t(\det U)^2 6^m\kappa^m\det D\,\det M_5.}
\tag{B9}
\]
该缩放whole-X整，右侧为常数。因此原p^{17m}归一化的leading reduction为非零常数，当且仅当detM5≠0；**不再要求detG0≠0**。若M5单位，则Gauss valuation和每个X∈Zp求值valuation都恰−17m；避开fixed有理candidate及a,b分母后适用。

如果原M5在无穷p=18r+1为unit，就严格得到actual D_A每个fixed rational candidate的无限nonzero。这条条件比旧两个simultaneous units弱，但本稿仍未证明这个无穷条件。Dirichlet只给该同余类无穷素数，不能保证M5在其中非零。

单个auxiliary prime只付O(nlogn)，不改变已证safeA约41.963的n²预算；也不改变same-object解析率或strict margin。

## B5. G0退化时实际Smith型：新出现指数1

在M5unit条件下令g=corankG0。非退化ambient D给rad(D|E)=E∩E^⊥，亦为E^⊥的rad；E^⊥由D^{-1}L^t生成，其Gram=κ^{-1}G0，所以strong leading的corank恰g。

先对M的e−g个strong unit方向作Zp整Schur，剩g strong、q weak；归一化N的reduction仍unit，strong/strong reduction为0。其cross g×q矩阵C满row rankg，否则某strong方向会在N中成为radical。剩M整体被p整除，除p后modp是
\[
\begin{pmatrix}A&C\\C^t&0\end{pmatrix},
\]
其中A可任意，rank恰2g：kernel恰(0,kerC)。故M有e−g个Smith指数0、2g个指数1，其余q−g个至少2。B9已证vdetM=2q=3m，剩指数总量只能是2(q−g)，所以全恰2。得到
\[
\boxed{\operatorname{Smith}(p^5B_X):
0^{5m/2-g},\quad1^{2g},\quad2^{3m/2-g}.}
\tag{B10}
\]
原B_X将每个指数减5；总valuation仍−17m。g0恢复旧A28；g>0时旧0/2分布不能继续声称，但whole polynomial常数非零保持。对所有X∈Zp成立，因为leading N与X无关。没有由ambient unit免费推出restricted Gramunit。

## B6. 更弱的p³扰动门槛

在同一实际局部基中，X项是24p^5X times value-Gram。两侧各除D_p最多损失p²，所以
\[
N(X)-N(c)\in p^3(X-c)\operatorname{Mat}_{4m}(\mathbf Z_p)
\quad(c\in\mathbf Z_p).
\tag{B11}
\]
若N(c)可逆且其最大Smith指数ν_max≤2，则p³N(c)^{-1}属于pMat(Zp)。因此
\[
N(X)=N(c)\bigl(I+(X-c)N(c)^{-1}(N(1+c)-N(c))\bigr)
\]
的第二因子在Zp[X]中模p恒I；其det模p恒1。于是whole-X归一化det为非零常数，所有X∈Zp仍nonzero且valuation与anchor相同。此条件允许M5 modp奇异，只要实际higher layers在深度3前补满。

该阈值严格：ν_max=3时N(c)=diag(p³,1)、扰动−p³(X−c)diag(1,0)，X=c+1会精确奇异。不能免费放宽至3。B11也不能证明真实N(c)的ν_max≤2；a-source进入higher layers，须按原actual lifts计算/证明，不能由finite-fieldM5或fullQunit直接推断。

## B7. 结构实例与验证范围

一个明确algebraic例子说明G0singular不阻止whole form非零：F19中D=diag(1,−1)、L=(1,1)、Z=(1,−1)^t、J=(1,0)^t、K=I、D_d=0。G=LD^{-1}L^t=0，C=1，H=1，bordered target[[0,1],[1,1]]unit；restricted \(\mathcal N=[[0,1],[1,0]]\)也是unit。实际Dp \(\mathcal N\) Dp的Smith是1,1。此例只验证一般身份和逻辑，不是原λ2特殊值模型中的退化实例。

NEW [first-only源](cdt_odd_paired_single_bordered_nonzero_gate_20261006_verify.py)已完整静态读后恰首次1次执行，exit0 PASS142checks，失败/重跑/旧同行execute/import均0；source SHA84e3c06bb135ec57235880fa1490afe4a9c17e07fef62541219ce99e329e1cb3。成功源和[JSON](cdt_odd_paired_single_bordered_nonzero_gate_20261006_verify.json)不改、不rerun。实际完整读取全部保存JSON字段，包括3actual cases、19项扰动记录和两个toy scopes。仅用旧已考虑r1,2,4的literal actual定义核B1–B8矩阵、比例因子/corank；不扩auxprime表、不读取旧或同行PY/JSON。三个whole-normalized det（除source unit）为6/10/18，原M5 det为15/16/38，比例unit为8/33/12；逐case吻合。

另核上述Gsingular algebraic实例及B11的depth2/depth3阈值实例；这些不是原λ2 higher-layer证据。本程序不计算actual higher-p-layer、其ν_max或无限target非零。全尺度证明在B1–B6，有限验证不证明无穷M5units或新数值定理。完整来源/执行史另登记，成功数学source/JSON保持首次指纹。

## B8. 一手文献与后续边界

正常verified TLS新增两份独立原件：Xavier Caruso《Computations with p-adic numbers》[原件](https://www.numdam.org/item/10.5802/ccirm.25.pdf)/[本地PDF](../literature/caruso2017_computations_p_adic_numbers_ccirm_20261006.pdf)76归档页，SHAc6124267c5457166cb08b0baf645dfff37a4bcf838f13cb27ad1182dfe6fd0d0，root实际完整读PDF49–53共5页；Elsheikh–Giesbrecht《Relating p-adic eigenvalues and the local Smith normal form》[arXiv v4](https://arxiv.org/abs/1401.1773v4)/[本地PDF](../literature/elsheikh_giesbrecht2015_p_adic_eigenvalues_smith_arxiv1401_1773v4_20261006.pdf)24归档页，SHAa3328c7a8149dca7babb75940d07d122f13a8ef10755e454d7fe8cc47c7d6018，root实际完整读PDF1–5共5页。后者索引v4日期2015-05-07，下载PDF首页还显示2018-10-20，按固定URL及字节保存，不将二者冒认为相同日期。两份合计100archive页，实际root10页，非全文。Caruso PDF52 Prop3.2.4及PDF53的total−max precision公式实际读；PDF49–50的dual lattice/diffused precision也保留坐标相关性。

B6用最大Smith指数控制inverse分母，而非把特征值valuation当Smith指数；两者不是无条件相同。Elsheikh PDF3–4的明确反例保留此区别；PDF5 Theorem2要求p>16(n²+3n)/ε及固定Smith类density，不能证明本题p~n、随r增长的确定性family。上述identity和perturbation lemma均在本稿自证，不依赖generic matrix论断。

尚未取得无穷M5units、真实higher-layerν_max≤2、无限D_A非零、strict arithmetic–analytic margin或ζ/L/Catalan新的无理性/线性无关性结论。研究目标保持原scope；下一步优先原M5的固定middle算术防相消，而非继续证明独立G0gate。
