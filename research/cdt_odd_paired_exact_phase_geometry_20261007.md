# 原核商的精确相位：主角、去核谱与真实振荡势

2026-10-07，NEW，作者 /root。Authority 为 main §§171–175 和 [delivery kernel profiles](cdt_odd_delivery_kernel_profiles_20261007.json)，SHA `313ad01a4abe88dd8a8193561b30232dfa131c8832d126af18390eafc8514e72`。本轮已完整 JSONparse、读 header/current_progress，并逐项物理 SHA 核572旧冻结记录不变；不是人工全文重读全部历史证明。567数学记录、5 guards只读。本轮纯纸证，不创建、execute、import或rerun数学producer，不扩prime。

本人本轮实际 FULL 读 [coupled C1–C23](cdt_odd_paired_coupled_gram_decay_20261007.md) 和 [primitive kernel K1–K18](cdt_odd_paired_primitive_kernel_quotient_20261007.md)，以及总稿 §§171–175。真实源仍 ξ=αζ(4)+βζ(5)，固定有理α、β，β≠0。本文先证明一般 finite complex Gram 身份，再识别同一原轮廓的具体主相位；并不把新身份或振荡存在当作已经足够的 n² 衰减。

## 1. 精确核商相位身份

取原 B=B_n(ξ)，P>0 为原total-variation Hermitian Gram，m=2n。假设ξ=c∈Q时 B实对称有理、actual rank d≥1，ν=m−d。沿冻结K1–K3取真实完整primitive整数核基K、unimodular U=[L,K]、C=LᵀBL和q=detC≠0，E=U^−t前d列。准确有B=ECEᵀ。

记P_K=KᵀPK、P_Q=P_LL−P_LK P_KK^−1 P_KL。空核时detP_K=1、P_Q=P。全程P按RᵀP overline(R)约定变换，K、L、E实；P_Q是冻结K8的正确complex剪切商Gram。令

\[
T=P^{-1/2}B(P^{-1/2})^t,
\quad F=P^{-1/2}E,
\quad G=F^*F=E^tP^{-1}E.
\tag{F1}
\]

T complex symmetric、rank d，原真实Gram的Cauchy–Schwarz给||T||≤1。G>0。Jacobi互补块式给

\[
G=P_Q^{-1},\qquad
\det G=\frac{\det P_K}{\det P}.
\tag{F2}
\]

证明：UᵀPU的inverse前d块恰为EᵀP^−1E，而inverse的这一块恰P_Q^−1；det(UᵀPU)=detP，因为detU=±1。全部量均属于同一原basis，未支付或忽略一个任选补基height。

令w_I=detF_I。Cauchy–Binet与actual rank d使

\[
C_d(T)=q\,w w^t,\quad
\|C_d(T)\|=|q|\sum_I|w_I|^2
=|q|\det G.
\tag{F3}
\]

complex rank-one矩阵w wᵀ的唯一singular value是||w||²；不能用wᵀw替代。外幂norm同时恰为T的非零d个singular values之积Θ_d。因此得到比前轮不等式更精确的恒等式

\[
\boxed{\Theta_d=|q|\frac{\det P_K}{\det P},
\qquad |q|=\frac{\det P}{\det P_K}\Theta_d.}
\tag{F4}
\]

只排除ν个真实零singular values，Θ_d>0。detT=0时仍可用F4；没有以零作为算术非零证书。

## 2. 全部非零singular values都来自真实商压缩

置Q_F=F G^−1/2，则Q_F^*Q_F=I_d、Q_Fᵀoverline(Q_F)=I_d，且

\[
T=Q_F\,T_Q\,Q_F^t,
\quad T_Q=G^{1/2}C(G^{1/2})^t
=P_Q^{-1/2}C(P_Q^{-1/2})^t.
\tag{F5}
\]

左乘column isometry、右乘其transpose coisometry不改变非零singular values，故T_Q的d个singular values恰为T的全部非零singular values。特别||T_Q||≤1，|detT_Q|=Θ_d。该谱识别不是只在determinant层面作粗bound，也不要求原full determinant非零。

对于原首次jet，冻结K5给J_ν(c)=q a_V、a_V=det(KᵀVK)>0。于是

\[
\boxed{|J_\nu(c)|
=\frac{\det P\det(K^tVK)}{\det(K^tPK)}\Theta_d.}
\tag{F6}
\]

F6完整保留离散source核因子；不能免费除掉a_V后继续使用原jet整模型。对q采用合法rank-minor整模型、对J采用其完整jet整模型，两种算术比较不可混写。任何声称的改进必须估F4或F6中实际相同的核方向和相位。

## 3. Antiunitary压缩与真实主角

令H=L²(dν)、dν=|dμ|，inner product采用linear-first约定⟨f,h⟩=∫f overline(h)dν。τ=dμ/dν、|τ|=1 a.e.。定义

\[
\mathcal A f=\overline\tau\,\overline f.
\tag{F7}
\]

A是antilinear isometry，A²=I。取e=P^−1/2g，原Gram约定使e_i orthonormal；F_n=span_C(e_i)，Π其正交投影。准确有T_ij=⟨e_i,A e_j⟩。A e_j亦为orthonormal frame，因此T的singular values就是F_n与A F_n的主角余弦。

实函数kernel在此对应finite bilinear radical，维数ν；它是F_n∩(A F_n)^⊥。这ν个直角必须先删除。ΠA|F_n是antilinear压缩；在此inner-product约定中其坐标为overline(T) overline(x)，不是未经核对的T overline(x)。它的平方与ΠΠ_(A F_n)|F_n一致，坐标为T* T。因此

\[
D=I_m-T^*T\succeq0,
\quad\operatorname{spec}D=
\{1\text{ repeated }\nu,\ 1-\sigma_i^2\ (1\le i\le d)\}.
\tag{F8}
\]

这里只用finite Hilbert Gram和isometry自证主角解释，不假定原pair空间是标准Hardy model space，也不从C-symmetry本身推出指数小singular values。

## 4. 去核log级数、谱计数与n²所需尺度

对δ_i=1−σ_i²∈[0,1)，逐项展开−log(1−δ_i)，finite d和正项求和给准确

\[
\boxed{-\log\Theta_d
=\frac12\sum_{r=1}^{\infty}
\frac{\operatorname{Tr}D^r-\nu}{r}.}
\tag{F9}
\]

ν在每一项都必须减；遗漏它会对真实零方向制造虚假的无限phase信用。任意有限R的合法moment下界M_R为F9的前R项，满足

\[
0\le M_R\le\frac d2 H_R\le\frac d2(1+\log R).
\tag{F10}
\]

因此m=2n时，任何R(n)至多polynomial(n)的这种截断，只能产生O(nlogn)=o(n²)的下界；即使所有有限trace估得完美，也不能由这个截断免费得到正n²主率。该结论只限制这一具体log-series截断证书的保证能力，不是实际phase损失的upper或一般方法no-go。无穷级数、指数尺度R、直接logdet或谱尾估计仍可不同。

另令N_n(s)=#{i≤d:σ_i≤e^−s}，不含ν个零方向。由layer-cake identity（端点不影响积分）

\[
\boxed{-\log\Theta_d=\int_0^\infty N_n(s)ds,
\qquad\frac{-\log\Theta_d}{n^2}
=\int_0^\infty\frac{N_n(nt)}n\,dt.}
\tag{F11}
\]

可用的一个严格充分谱门槛是：实际(kerT)^⊥中存在ℓ_n维子空间，在其上||T u||≤e^−bn||u||，且liminfℓ_n/n≥a>0、b>0。min-max给至少ℓ_n个非零singular values≤e^−bn，故liminf−logΘ_d/n²≥ab。这与仅cn个σ≤ρ<1的O(n)信用不同；本文尚未对原T构造这样的子空间。

## 5. 原轮廓的主相位，不替换period源

本节从本轮实际FULL读coupled C1/C5直接使用原

\[
R_n(z)=\frac{(6n)!^2}{(2n)!^3}\frac{S_n(z)^3}{(z)_{6n+1}^2},
\quad c_n=2n+\tfrac12,
\quad K(z)=-4\alpha(\pi\cot\pi z)''-\beta(\pi\cot\pi z)'''.
\tag{F12}
\]

所有原basis polynomial g_i都有common S_n。写g_i=S_n u_i后，双线性measure成为dω_n=R_n K S_n² dx/(2π)，positive weight为W_n=|R_nK| |S_n|²/(2π)。这个共同因子转移是Hilbert isometry f↦S_n f，故同一B、P及T都保持；不是免费更换目标period。

令z=c_n+iny，y>0。全部S和rising factors实部为正，可选择连续argument。除K的零点以外，实际phase准确为exp(iΨ_n(y))，其中

\[
\Psi_n(y)=5\sum_{r=0}^{2n-1}
\arctan\frac{y}{(r+1/2)/n}
-2\sum_{j=0}^{6n}
\arctan\frac{y}{2+(j+1/2)/n}
+\arg K(c_n+iny).
\tag{F13}
\]

cot周期使K(c_n+ix)=K(1/2+ix)。置t=tanh(πx)、s=sech²(πx)，直接解析求导得到

\[
K(c_n+ix)=s\{8i\alpha\pi^3t+2\beta\pi^4(1-3t^2)\}.
\tag{F14}
\]

β≠0保证非恒零；α=0时可能的两个实zero仅在固定x位置，不能忽略，但不落入固定y≥ε>0的大n区间。选principal argK∈[−π,π]。对任何固定0<ε≤y≤M，midpoint Riemann sums的uniform smoothness以及rising sum的额外末项给

\[
\frac{\Psi_n(y)}n=\Phi(y)+O_{\epsilon,M}(1/n),
\quad
\boxed{\Phi(y)=5\int_0^2\arctan\frac yt\,dt
-2\int_2^8\arctan\frac yt\,dt.}
\tag{F15}
\]

负半轴由factor conjugation覆盖，K相位可能相差固定π；该差除n趋零。这里识别的是ω-density的实际主相位，不含任一被选择的basis vector自身的argument。

## 6. 主相位唯一正stationary point及不能直接迁移的振荡估计

对y>0在F15下求导，准确有

\[
\Phi'(y)=\frac72\log(4+y^2)-\frac52\log(y^2)-\log(64+y^2),
\]
\[
\boxed{\Phi''(y)=\frac{100y^2-1280}{y(y^2+4)(y^2+64)}.}
\tag{F16}
\]

Φ'在(0,8/√5)下降，之后上升并从负值趋0：∞展开Φ'=−50/y²+O(y^−4)。在y↓0时Φ'→+∞。在y²=2和3时，可通过整数比较分别得6^7>2^5·66²及7^7<3^5·67²，所以Φ'分别正和负。故唯一正stationary point y_*满足

\[
\boxed{\sqrt2<y_*<\sqrt3,\qquad
(y_*^2+4)^7=(y_*^2)^5(y_*^2+64)^2.}
\tag{F17}
\]

无需数值root程序或素数实验。这给出了原phase实际随n变化的非线性振荡势。它不等同原正weight envelope Q的最大点，也不证明每个moment或singular value都指数小：u_i本身是n-dependent rational/polynomial函数，可能携带同阶phase；n² determinant估计需要同时控制完整空间、尾部及complex contour，而不只是密度的stationary point。

## 7. Primary读域、适用条件与下一步

本轮正常TLS保存两份新的原件在literature/cdt_paired_phase_geometry_sources_20261007；既有库检索未见这两篇，未重复已有原件：

1. Deaño, *Large degree asymptotics of orthogonal polynomials with respect to an oscillatory weight on a bounded interval*，[arXiv1402.2085v1](https://arxiv.org/abs/1402.2085v1)，[固定PDF](../literature/cdt_paired_phase_geometry_sources_20261007/deano2014_oscillatory_orthogonality_arxiv1402_2085v1.pdf)，34页，859662bytes，SHA `f1e9a0bd9ae868488a6ed05347e7efe2f51b4aa54f34b57af341ffeff0e1a844`。本人实际完整文本读PDF1–7七页。PDF页眉v1/2014与文内生成日期December6,2024分别保留；不据文内日期猜另一arXiv版本。Theorems2.1–2.4处理[-1,1]、linear potential和0≤λ<λ0，Remark2.5明确没有在该稿列出Hankel determinant asymptotics。本文不引用一个不存在的n² determinant定理，也不把原全实轴/rational-pair/cot weight套进该特殊模型。
2. Garcia–Putinar, *Complex symmetric operators and applications*，[AMS原件](https://www.ams.org/journals/tran/2006-358-03/S0002-9947-05-03742-6/S0002-9947-05-03742-6.pdf)，[固定PDF](../literature/cdt_paired_phase_geometry_sources_20261007/garcia_putinar2006_complex_symmetric_operators_AMS.pdf)，31页，380198bytes，SHA `0695fd5e982a6603d2941ed95f3354220090dd02d11eb462dcf23c3506dd777d`。本人实际完整文本读PDF1–5五页，重点§2.1的conjugation及§2.2的bilinear reproducing-kernel约定。原web fetch一次403，正常TLS文件下载成功；没有绕TLS。本文finite phase身份及主角自证，不假定其标准model spaces等于原paired空间。

本轮root primary distinct为12页，不把34/31归档整本页数当全文阅读，也不继承上轮CDT/Bombieri–Vaaler页域。没有执行文献算法或旧数学producer。

可比较的完整q判据现在可直接写为

\[
\boxed{\limsup\frac1{n^2}
\left\{\log\det P-\log\det P_K+\log\Theta_d-\log Q_{n,d}
+d\log(DM)\right\}<0,}
\tag{F18}
\]

在同一有理性假设、无限actual-rank子列、已证完整q整模型下给整数矛盾。F18不是已经成立的结论；fixed(DM)^d保留。新算术模型若确立，应替换Q而不重复扣旧重叠信用。可按F11直接估指数尺度谱尾，或从原F13–F17建立同时处理rational pairs、n-dependent complex potential、cot奇点及unbounded tails的Riemann–Hilbert/向量平衡系统。正文没有完成这项asymptotic识别。

本轮新数学为F4–F6的精确商相位与非零全谱身份、F7–F11的去核principal-angle与尺度证书、F13–F17的原轮廓实际主相位及stationary point纸证。尚未证明足够Θ_d损失、真实kernel Gram方向增益或新数值ζ/L/Catalan无理性、LI、Lean。唯一新主稿待正式FULL独审、收审后最终FULL回读与单向来源收据；572旧冻结记录不改。
