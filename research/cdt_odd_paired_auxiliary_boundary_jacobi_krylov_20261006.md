# 真实 middle 边界自伴 Jacobi 算子、critical Krylov 基与无 norm 除法的递推

2026-10-06，NEW 独立数学稿，当前待实际独审。439旧数学输入、上一轮452d论文/f050 receipt、所有旧和同行 producers 全部只读。本轮自有 NEW producer 首次且唯一运行1次 PASS；没有旧/同行 execute、import、rerun。

本稿没有证明原 G0、M5 在无穷辅助素数上同时为 unit。新增的是一个对所有辅助素数成立的共同自伴差分算子、保留原 critical profile 的明确单位三角 Krylov 基、真实两块 Jacobi continuant/resolvent 与 target 八源矩的 exact recurrence。另证明这些真实块的 endpoint Weyl functional 所有首 Hankel norms 都是显式 units，并精确说明为何不能直接移植给原 target。

## 1. 不删 middle 的实际输入

取 p=18r+1 为素数、r≥1、a=5r、N=5r+1，F=Fp。冻结 dcc6 U14–U28 给

\[
P(u)=u\prod_{k=1}^{a}(u-k^2),\quad
S(u)=\prod_{k=a+1}^{9r}(u-k^2),\quad
PS=u^{9r+1}-u.
\tag{K1}
\]

本轮重新实际读取 dcc6 U23–U35 与来源范围，特别未删端点 flux、middle projector 或 actual half jet；452d 的 module defect 结果继续作为冻结输入。令 Sy(x)=S(x²)，χ在 |x|<r 为1、r≤|x|≤a为0。设

\[
\widetilde w(x)=\frac{\kappa(x)}2 Sy(x)^{-5},\qquad
\kappa=1+\chi,\qquad \alpha=\frac{5-\chi}{1+\chi}
=\begin{cases}2,&|x|<r,\\5,&r\le|x|\le a.\end{cases}
\tag{K2}
\]

该权重只支撑 [-a,a]⊂Fp，其他点定义为0。令 R(x)=Sy(x)^4，在实际支撑上是 unit。Scalar/matrix forms 精确为

\[
\langle T,V\rangle_G=\sum_{x=-a}^{a}\widetilde w(x)T(x^2)V(x^2),
\]
\[
\langle(T,Q),(V,Z)\rangle_M
=\sum_{x=-a}^{a}\widetilde w(x)
\{TV+\alpha R(TZ+QV)+R^2QZ\}(x).
\tag{K3}
\]

对 deg T,V<r、deg Q,Z<3r，单项式基中的矩阵恰是原 G0、M5，没有新整体 scalar。特别 folded k=0 的权重是 Sy(0)^−5；0<k<r 是2Sy(k)^−5；r≤k≤a是Sy(k)^−5。K2的α=2/5完整保留实际 half jet。

Wilson/冻结 U8 给相邻支撑点

\[
\frac{Sy(x+1)}{Sy(x)}
=-\frac{a-x}{a+x+1}.
\tag{K4}
\]

本式只用于两个点都在实际支撑的内部；未将其错误称为全体 rational functions 的 identity。

## 2. 真正自伴并消除全部 flux 的 scalar 算子

定义

\[
F_r(x)=(x+r)(x+1-r),\quad
A_0(x)=(x+\tfrac12)(a-x)(x+a+1)^6F_r(x),
\]
\[
D_0 f(x)=A_0(x)[f(x+1)-f(x)]
+A_0(-x)[f(x-1)-f(x)].
\tag{K5}
\]

**Lemma K6。** D0对K2的实际 finite functional 自伴，且在支撑的函数空间与χ通勤。它保持 even polynomials。

证明：F_r(−x−1)=F_r(x)，所以
\[
A_0(-x-1)=-(x+\tfrac12)(a+x+1)(a-x)^6F_r(x).
\]
在非跳边由 K4 得逐边 detailed balance
\[
\widetilde w(x)A_0(x)=
\widetilde w(x+1)A_0(-x-1).
\tag{K6}
\]
跳边 x=−r,r−1 时双方 coefficient 都为0，故κ的非平凡2或1/2比率不产生遗漏项。支撑上边 x=a 有A0(a)=0，下边 x=−a−1 有A0(−a−1)=0，故无外部 flux。其他外部边双方权重皆0。按边重排有限和即得自伴，没有正定性或 nonzero OP norm 假设。

同样，只有 middle/outer 接触边被K5切断，所以D0不能跨χ的sector，χD0=D0χ。x↦−x交换 forward/back，故even f仍even。

该算子是degree10的二阶difference operator，未声称标准degree2的 Hahn/classical operator。冻结 class7 最小性不被推翻。

## 3. 保留第二源的 polynomial covariant 算子

设
\[
B_0(x)=(x+\tfrac12)(a-x)^5(x+a+1)^2F_r(x),
\]
\[
D_4 q(x)=B_0(x)q(x+1)+B_0(-x)q(x-1)
-[A_0(x)+A_0(-x)]q(x).
\tag{K7}
\]

**Lemma K8。** 在实际支撑的点值函数上
\[
D_4=R^{-1}D_0R.
\tag{K8}
\]
同时K7是明确的polynomial operator，不需对Sy作全局 rational gauge 或除待证determinant。

证明：K4的四次幂给
A0(x)R(x+1)/R(x)=B0(x)，back方向同理。端点及middle跳边的A0、B0均零，故不用定义支撑外R的inverse，不产生额外项。对角项保持−A0−A0(−x)。K7的多项式定义对所有polynomials有效，even也保持even。

**Lemma K9。** diag(D0,D4)对原matrix form K3自伴。

证明：将(T,Q)映为(T,RQ)。K3变成以标量权重 \(\widetilde w\) 和sector常值 symmetric matrix
\(\left(\begin{smallmatrix}1&\alpha\\\alpha&1\end{smallmatrix}\right)\)
定义的form；K8把operator变为diag(D0,D0)。K6自伴，且与α=5−3χ通勤，所以整个symmetric matrix可穿过D0。该matrix在每个sector的det为−3或−24，均非零；但证明没有由其ambient unit推target unit。

## 4. 两种 leading coefficient 的全尺度计算

对f=x^j，两个operators的degree至多j+8，even j时结果even。直接最高三项展开给

\[
[x^{j+8}]D_0x^j=-j(j+10a+14),
\]
\[
[x^{j+8}]D_4x^j
=-(j-8a-4)(j+2a+10).
\tag{K10}
\]

证明细节：A0最高两项为
−x^10−(5a+15/2)x^9，B0为−x^10+(3a−7/2)x^9。其x^8 coefficient之差是
8a²+44a+20；共同diagonal使x^{j+10}与x^{j+9}抵消。于是D0最高剩项为
−j(j−1)−(10a+15)j；D4为
−j(j−1)+(6a−7)j+2(8a²+44a+20)，精确等于K10。

因为 a=5r、18r=−1于Fp，
10a+14=101/9，
−8a−4=−16/9，
2a+10=85/9。
取共同 potential
\[
\gamma=-98/27,\qquad
E_0=D_0+\gamma x^8,\quad E_4=D_4+\gamma x^8.
\tag{K11}
\]
它不改form，对scalar/matrix仍自伴、仍与χ通勤；K8亦保持。对u^d=x^{2d}，最高系数成为

\[
\lambda_0(d)=-(2d+\tfrac13)(2d+\tfrac{98}9),
\quad
\lambda_4(d)=-(2d-\tfrac{13}9)(2d+\tfrac{82}9).
\tag{K12}
\]

这是同一γ的真实匹配，不是给两个channels免费选独立potential。

## 5. 原critical profile上的全部 leading units

**Theorem K13。** 对每个p=18r+1：
\[
\lambda_0(d)\ne0\quad(0\le d<r),\qquad
\lambda_4(d)\ne0\quad(0\le d<3r).
\tag{K13}
\]

证明：2、3是p-units。第一个λ0 factor等价于6d+1，在0≤d<r范围中正且小于p。第二factor等价于18d+98；若它是kp，则k≡8(mod18)，最小可能正k=8，首次d=8r−5≥r。故无零。

λ4第一factor18d−13在d=0时为−13，绝对值<p；其后若为kp，则k≡5(mod18)，首次d=5r+1>3r−1。第二factor18d+82需要k≡10(mod18)，首次d=10r−4≥3r。结论含r=1。这里没有以generic nonzero代替actual prime arithmetic，也没有依赖所有中间Hankel minors正常。

对m=r或3r，以i=0或4相应定义
\[
f_{i,d}=E_i^{\,\lfloor d/4\rfloor}u^{d\bmod4},
\qquad 0\le d<m.
\tag{K14}
\]
其degree恰d，leading coefficient为
\[
\eta_{i,d}=\prod_{h=0}^{\lfloor d/4\rfloor-1}
\lambda_i(d\bmod4+4h)\in F^\times.
\]
所以按d排序，它们是原degree<m空间的单位三角意义的basis；determinant
\(\Delta_i(m)=\prod_{d<m}\eta_{i,d}\)
为明确unit，不用Gram–Schmidt。

**Corollary K15（exact target normalization）。**
\[
\det G_0^{K}=\Delta_0(r)^2\det G_0,\qquad
\det M_5^{K}=[\Delta_0(r)\Delta_4(3r)]^2\det M_5.
\tag{K15}
\]
故新Krylov Gram非零与原target精确等价。

这是auxiliary p-local basis change：operators的coefficients在Z[1/6]，本profile的leading系数模p为units，所以同尺度basis change可lift为GL(Zp)。不能由此免费改全素数或archimedean模型；若把该basis作为global integer basis，反复potential的2/3分母、coefficients和leadingproducts仍需另付。本稿没有宣称新的费用改善。

## 6. 真folded Jacobi矩阵与两个不可约链

在k=0,…,a的even node函数空间，E0矩阵记J。其
\[
d_k=-A_0(k)-A_0(-k)+\gamma k^8,
\]
\[
J_{0,1}=2A_0(0),\quad
J_{k,k+1}=A_0(k)\ (k\ge1),\quad
J_{k,k-1}=A_0(-k)\ (k\ge1).
\tag{K16}
\]
端点省略不存在的entries。Folded权重w_k为K3所列，K6给
w_k J_{k,k+1}=w_{k+1}J_{k+1,k}。

恰在r−1/r之间两个offdiag都为0，所以
\[
J=J_{\rm mid}\oplus J_{\rm out},\quad
\dim J_{\rm mid}=r,\quad \dim J_{\rm out}=4r+1.
\tag{K17}
\]
每个块的内部super/subdiagonal均unit。理由：head range0≤k≤5r严格小于(p−1)/2=9r，故k+1/2和其反射无零；a−k及a+k+1不在内边为零；F只在middle cut产生零。起点0的fold2也是unit。所有边界项已明确支付，未把middle projection当小rank可忽略。

第二channel的点值matrix为R_diag^−1 J R_diag。整个actualmatrix form在(T,RQ)坐标下用同一个J作用于两channels；不是把两个独立period packet合并。

## 7. Norm-free continuant、proper endpoint pair 与显式inverse

对任一K17块，按local indices0,…,m−1写diag d_i、super a_i、sub b_i（b_i在row i、column i−1，i≥1）。a_i,b_{i+1}全unit。定义prefix polynomials
\[
\theta_0=1,\quad\theta_1=z-d_0,\quad
\theta_{j+1}=(z-d_j)\theta_j-a_{j-1}b_j\theta_{j-1}.
\tag{K18}
\]
末尾suffix \(\phi_m=1,\phi_{m-1}=z-d_{m-1}\)用反向相同recurrence。

**Lemma K19。** θ_j为monic degree j的真实principal characteristic polynomial；相邻θ互素，并且Euclidean remainder每次恰drop1。这由det expansion与unit a b直接给出；共同因子逐步向θ0=1回推。无需任何未知Hankel norm或distinct eigenvalues。相邻properness在这里是已证事实，并非套p37反例已否定的原u-moment perfectness。

在F(z)上，resolvent的explicit entries为
\[
[(zI-J_B)^{-1}]_{ij}=
\begin{cases}
(\prod_{h=i}^{j-1}a_h)\theta_i\phi_{j+1}/\theta_m,&i\le j,\\
(\prod_{h=j+1}^{i}b_h)\theta_j\phi_{i+1}/\theta_m,&i>j.
\end{cases}
\tag{K20}
\]
证明：cofactor删行/列的tridiagonal forced path给products，剩下prefix/suffix determinants；adjugate sign与path中−a/−b抵消。或者直接乘zI−J由K18得到identity。θ_m monic且非零，故F(z) inverse合法；没有假定某个特定z值unit。

## 8. 原target的4/8-seed确切矩递推

Scalar选4seed u^t，t=0,…,3。Matrix选8seed
\((u^t,0)\)、\((0,u^t)\)，t=0,…,3；小profile无须的seed/链直接omit。对应K14的链长仍分别由d<r和d<3r确定。

共同selfadjoint operatorE=diag(E0,E4)给
\[
\langle E^j v_s,E^k v_t\rangle
=\langle v_s,E^{j+k}v_t\rangle=:m_{s,t;j+k}.
\tag{K21}
\]
所以K15的真实Gram成为确定的4seed或8seed block moment minor，而非新full-block uniform profile。

变换后的node seed分别是(u^t,0)、(0,Ru^t)。令V收集这些columns，
\[
\widehat W=
\begin{pmatrix}D_w&D_{w\alpha}\\D_{w\alpha}&D_w\end{pmatrix},
\quad \widehat J=J\oplus J.
\]
实际Stieltjes matrix满足
\[
\mathcal H(z)=V^{\mathsf T}\widehat W
(zI-\widehat J)^{-1}V
=\sum_{j\ge0}m_jz^{-j-1}.
\tag{K22}
\]
Scalar用单channel相同式。由K20，每个entry都有同一个已知分母
\[
C(z)=\theta_{\rm mid,r}(z)\theta_{\rm out,4r+1}(z)
=z^N+\sum_{h=0}^{N-1}c_hz^h,
\tag{K23}
\]
numerator degree<N。这里尽管widehatJ characteristic是C²，entry分母只需C，因为两channels都是同一J；不是免费降低differential rank。

因此所有实际source矩满足全尺度exact recurrence
\[
\boxed{m_{s,t;j+N}+\sum_{h=0}^{N-1}c_hm_{s,t;j+h}=0
\quad(j\ge0).}
\tag{K24}
\]
还可以按middle/out分别用degree r和4r+1的各自continuant递推。初始矩、connection vectors全部由K2/K16明定，未知norm不出现在任何denominator。Actual χ和halfjet留在w、α、R和两个sector，不是从full trace独立推回去。

K24是原target可用的exact recurrence和determinant representation，不承诺该block minor非零。其order随r增加；本稿没有将其写成固定阶跨素数recurrence。

## 9. 一个真实全尺度unit机制，以及不能免费移植的证明

对一个实际块B，取起点e0，定义endpoint functional
\[
L_B(z^j)=w_{\rm start}(J_B^j)_{00}.
\]
其首k阶Hankel determinant精确是
\[
\boxed{\det H_{B,k}
=w_{\rm start}^{\,k}
\prod_{h=1}^{k-1}(a_{h-1}b_h)^{k-h}\in F^\times,
\qquad1\le k\le m.}
\tag{K25}
\]

证明：列e0,J e0,…,J^{k−1}e0只支撑前k nodes，最高新node的系数是b1⋯bj。此k×k三角matrix determinant为这些products；其weighted Gram determinant是平方乘∏w_i。Detailed balance w_i b_i=w_{i-1}a_{i-1}消去后恰为K25。没有正定性、未知norm、simple spectrum或某个targetunit输入。该Weyl functional确实来自真实middle/outer Jacobi blocks，对每个辅助p均成立。

**Lemma K26（真实connection最高degree）。** Endpoint是cyclic，任一node vector v唯一写成f_v(J)e0、deg f_v<m。如果最后node值v_{m-1}非零，则
\[
\deg f_v=m-1,\qquad
[z^{m-1}]f_v=v_{m-1}/(b_1\cdots b_{m-1}).
\tag{K26}
\]
证明仍是tridiagonal support与最后一列最高node；unit products给唯一解，不需要Gram inverse。

Outer块的所有实际seed u^t及Ru^t在最后node k=a上非零，因此它们的connection polynomials全部恰degree4r，而不是低degree≤r或3r。Middle块在r≥2同样degree r−1；r=1有u^t(t>0)零vector的小尺度例外，constant和R仍非零。故K25的proper endpoint normality不能直接移给K21的dense multiseed/unequal profile。一个相关actual unit机制现在已明确证明，但originaltarget仍是这些明确connection polynomials的modified moment minor。

若有进一步Christoffel/contiguous identity，必须保留K26的高degree source费用和半jet α；不能将它们当普通低degree spectralmonomials。K25也不推翻p37原u-sequence的首norm0。

## 10. 已证进展和精确剩余门槛

本轮不只重复452d的abstract graph index。现在有了原G/M共同的polynomial selfadjoint差分结构；一个同potential匹配使两个实际critical source ranges的所有raising coefficients皆unit，给真aux-local Krylovbasis。真实边界分块的Jacobi coefficients、resolvent、moment recurrence和endpoint unit products全部明定，并且没有除原targetdeterminant。

下一门槛是证明K22八源Stieltjes matrix在K21的真unequal Krylov chain lengths上normal，或利用K20/K26的explicit connection求这个modified minor的nonzero formula。亦可直接证明对应K14空间的radical不存在，再由K15返回原G0/M5；两者均不需假设原所有intermediate profiles正常。

没有证明无限simultaneousunits，没有新的globalallprime/arch费用改善，没有strict arithmetic–analytic margin或新的ζ/L值无理性。Cartier/Frobenius与hypergeometric检索没有提供可直接满足这些actual hypotheses的定理，不能把PS特殊Fermat形状自动当该结论。

## 11. NEW primary原件与准确读域

正常verified TLS下载两份新独立原件，未bypass证书；独立receipt记录URL/hash/pages。

- Costas-Santos–Johnson，[Spectra of Tridiagonal Matrices over a Field](https://arxiv.org/pdf/1807.08877v1)，18页，实际全文PDF1–18读取。PDF2–4的continuant和Theorem1说明irreducible tridiagonal／proper pair over arbitrary field，PDF3亦允许multiple algebraic eigenvalues。这里K18–20自足证明，只使用这个明确范围；未凭PDF8–13关于特定functional的重建来替代actualsource normality，尤其不套用其quasi-definite输入证明原target。
- Durán–Sánchez-Canales，[Orthogonal matrix polynomials whose differences are also orthogonal](https://idus.us.es/server/api/core/bitstreams/e8f63919-6c4c-4242-83fe-5a5083d4509c/content)，16页，实际完整读PDF1–9。Theorem1/2明确有quasi-definite hypotheses、degree2/1及Hermitian条件；PDF8–9的Lemma4.1还要求degree不增。本稿operatordegree增4，有限域不以positive matrix measure解释，因此没有直接套其OP eigenfunction theorem。其区别Pearson、matrix symmetry和classical normality的范围提示本稿必须另行自证K6–15。

Source archive34页，实际distinct27页；未称读Durán稿PDF10–16，也未将来源称本target infiniteunit定理。

## 12. FIRST-ONLY机制验证与执行边界

NEW research/cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006_verify.py 有输出已存在即拒绝执行guard。首次且唯一运行1次，exit0、PASS3cases/364exactchecks；输出同stemJSON。只选先前已经考察的r=1,2,4，没有扩prime表。只importstdlib pathlib/math/json/hashlib，不读取、import或执行任何旧/同行数学producer。

验证实际weights、K5/K7evenpolynomialdegree/leadingunits、nodalR-conjugacy、folded detailedbalance/cut内部unit、actualKrylovdet平方因子、continuant/gcd和endpoint全部Hankelnormproduct。它没有assert原两个target infinite/all-r非零，也不证明正文allscalelemmas、global费用或特殊值定理。所有目标身份及全尺度论证以正文纸面证明为依据。

本稿及NEWreceipt待root/toric/quarter实际独审后再冻结；程序不重跑，不修改439旧pins。
