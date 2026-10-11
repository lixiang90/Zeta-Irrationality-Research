# 第237轮：联合jet格的直接BC桥与精确费用抵消

2026-10-08，Packet/B，数学程序0。直接桥成立：rank m的index upper κ对应这套BC模型的费用2κ/m²，rank3为2κ/9。但exact graded有限费用与index同时改变，彼此恰抵消；因此index本身不是模型的intrinsic费用。下一接口应算实际jump Taylor子式，而非继续把raw整格省费当净收益。本文无新数值无理性定理。

## 1. 明确模型与原文依据

实际FULL读236最终联合格稿11134 B / SHA256 b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70。先陈述一般rank m版本；本源代入

\[
f=(1,uE,b_gJ_g),\qquad
E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
J_g=\sqrt{1-4u}\left(g-2\int_0^u\frac{E(s)}{\sqrt{1-4s}}\,ds\right).
\tag{B1}
\]

g∈Q固定，b_g正整数且b_gg∈Z。实际Q(u)-rank3和微分闭合采用已付234–236结果。

一般假设：f_i∈Q[[u]]是Q(u)-独立的m个原生芽；其vanishing jumps满足max V_D≤mD+O_f(1)。本源由236明确closure及当前CDT Theorem3.2.8（Shidlovsky）取得这一点，而不是本文重证零估计。令

\[
\mathscr L_D=\mathbb Z[u]_{\le D}^{m},\quad
\Psi(P)=\sum_iP_if_i,\quad M=m(D+1),\quad
T_N(P)=[\Psi(P)]_{0,\ldots,N}.
\tag{B2}
\]

取固定C₀使N_D=mD+C₀覆盖全部jumps。Γ_D⊂𝓛_D为任意full-rank格，满足T_(N_D)(Γ_D)⊂Z^(N_D+1)。236完整CRT格就是一个实例；不要求选择低height的CRT基，也不要求tensor构造。

实处图限定当前CDT §7使用的版本：φ在闭单位圆盘的邻域holomorphic，φ(0)=0、φ′(0)≠0；每个原生f_i∘φ延拓为开单位圆盘上的meromorphic函数。图本身不是任意meromorphic P¹图；原文7.1.2脚注说明后者须另加polar counting，本稿不免费推广。写

\[
\lambda=\log|\phi'(0)|,\qquad
\mathcal J=(\overline{\mathcal O(1)}_\phi\cdot
\overline{\mathcal O(1)}_\phi)
=\iint_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w).
\tag{B3}
\]

采用当前220页作者PDF完整选页90–108：Euclidean degree定义(7.2.3)、完整filtered slopes Lemma7.2.13、BC metric及Hilbert–Samuel(7.3.4–5)、arch evaluation(7.3.9)/(7.3.14)、完整Lemma7.4.1证明。95页degree负号与104页slopes式另实际视觉核PNG。未FULL读220页，也未独立重证BC Hilbert–Samuel或Bost原定理。

## 2. 同一Hermitian度确实减一个logindex

原文Γ(P¹_Z,O(D))写成Z[1/u]≤D。对我们的P_i∈Z[u]≤D，用Q_i=u^(−D)P_i作reverse-basis同构；这只是monomial基的逆序，不产生有限分母。formal section为u^(−D)Ψ(P)，其graded指数n仍是原生function Ψ(P)的ord₀，而不是n−D被错当新的Taylor下标。

在𝓛_D⊗R上，给每个Q_i原文BC L²范数，并作m个summand的orthogonal direct sum。Γ_D使用这一范数的限制；其rational和real向量空间与𝓛_D完全相同。Hilbert–Samuel给

\[
\widehat{\deg}\mathscr L_D
=\frac m2\mathcal J D^2+o(D^2).
\tag{B4}
\]

若t_D=[𝓛_D:Γ_D]，任取Γ_D的Z基，其基变换det绝对值为t_D；Gram determinant因而乘t_D²。由degree=−(1/2)logdet，严格得到

\[
\boxed{\widehat{\deg}\Gamma_D
=\widehat{\deg}\mathscr L_D-\log t_D.}
\tag{B5}
\]

这已经将CRT基可能很高的arch坐标完整记入同一covolume；不需另声称有免费低height基。该式也不允许更换实处norm后继续沿用相同degree。

## 3. 全部graded有限norm≤1及pole clearing

定义Γ_D^(n)={P∈Γ_D:ord₀Ψ(P)≥n}。它是Γ_D中primitive submodule，因为核条件为Q-linear；各非零graded piece自由rank1。相应ordinary target为Z·u^n（以formal section写为Z·u^(n−D)），实处norm为1，有限处为标准绝对值。

N_D覆盖全部jumps，所以每个非零graded map都由

\[
\psi^{(n)}:\Gamma_D^{(n)}/\Gamma_D^{(n+1)}
\longrightarrow\mathbb Z,\qquad P\longmapsto[u^n]\Psi(P)
\tag{B6}
\]

给出。完整jet整性使B6是Z-hom。完备化及quotient lattice范数因此给所有p的operator norm≤1，即h_p(ψ^(n))≤0。这里必须保留全部0,…,N_D输出；只清某个row、某个窗口或某个非零minor不足以支付此断言。

arch quotient metric只由Γ_D^(n)⊗R及同一ambient norm决定。因Γ_D full-rank，它与𝓛_D对应rational/real过滤子空间相同；arch graded height与原文未改格的值相同。

为严谨处理只在开盘meromorphic的pullbacks，固定ρ<1，使用φ_ρ(z)=φ(ρz)。各f_i∘φ_ρ在闭盘邻域只有有限poles，选择固定polynomial h_ρ，h_ρ(0)=1，清除全部这些poles。它仅用于实处Poisson–Jensen，不改变native source或有限格；每个graded的leading coefficient不变。h_ρ与D无关，因此其费用为O_ρ(1)每层，合计O_ρ(D)=o(D²)。

令𝓛_φ及𝓛_(φρ)为原文两BC line metrics，记𝓘_ρ=𝓛_φ·𝓛_(φρ)、λ_ρ=λ+logρ。完整Lemma7.4.1在固定原metric下给

\[
h_\infty(\psi^{(n)})
\le -n\lambda_\rho+D\mathcal I_\rho+o_\rho(D),
\quad n\in V_D.
\tag{B7}
\]

同一uniform误差适用于n=O(D)。它来自原文的metric/Green-function比较，不另要求Γ整数基小。先固定ρ作D→∞，再ρ→1⁻；原文Lemma7.4.1明确给𝓘_ρ→𝓙及λ_ρ→λ。不能交换这两limit后忽略h_ρ可能变大的常数。

V_D有M个distinct非负整数且包含于[0,mD+O(1)]，故Σ_(n∈V_D)n=(m²/2)D²+O(D)。由B7与有限height≤0，Bost slopes得到

\[
\frac m2\mathcal J D^2-\log t_D+o(D^2)
\le\left(-\frac{m^2}{2}\lambda_\rho+
m\mathcal I_\rho\right)D^2+o_\rho(D^2).
\tag{B8}
\]

若limsup log t_D/D²≤κ<∞，按上述两limit得到

\[
\boxed{m\lambda\le\mathcal J+\frac{2\kappa}{m};\qquad
m\le\frac{\mathcal J}{\lambda-2\kappa/m^2}
\quad\text{当分母}>0.}
\tag{B9}
\]

这是从已读原文逐项重作的直接桥，不是直接调用仍带旧LCM类型的Theorem7.0.1。实际functions已holonomic，所以没有额外借该定理的logc>σ条件来支付零估计。

## 4. 第二lemma：exact有限height恰抵消index

现在先不把B6的有限height放松到0。设L=𝓛_D、Γ=Γ_D使用同一real metric、同一rational过滤和同一ordinary Z target。对每个jump定义
s_n=[Gr_n L:Gr_n Γ]，
在同一个rational graded line内比较；因Γ⊂L，s_n为正整数。

过滤是saturated，Gr_n Γ→Gr_n L单射。逐层exact sequence给
[L^(n):Γ^(n)]=[Gr_n L:Gr_n Γ]·[L^(n+1):Γ^(n+1)]，
于是

\[
\boxed{\prod_{n\in V_D}s_n=[L:\Gamma].}
\tag{B10}
\]

若Gr_n L的Z生成元在ordinary target中为q_n≠0，Gr_n Γ的生成元在同Qline中就是s_n倍。有限source lattice norm给
h_p(ψ_Γ^(n))=log|s_nq_n|_p
=h_p(ψ_L^(n))−v_p(s_n)logp。
arch quotient norm和rational map不变，故h_∞(ψ_Γ^(n))=h_∞(ψ_L^(n))。求和得到严格恒等式

\[
\boxed{\sum_n h_{\rm fin}(\psi_\Gamma^{(n)})
=\sum_n h_{\rm fin}(\psi_L^{(n)})-\log[L:\Gamma].}
\tag{B11}
\]

结合B5，exact slopes两边的logindex全cancel。因此内在有限费用是

\[
\boxed{\mathcal A_D:=\log[L:\Gamma]
+\sum_nh_{\rm fin}(\psi_\Gamma^{(n)})
=\sum_nh_{\rm fin}(\psi_L^{(n)}),}
\tag{B12}
\]

不依赖所选同metric整格Γ。完整jet整数化只给𝓐_D≤log[L:Γ]这个upper；忽略negative graded finite credit会放宽判据。236的raw index改进仍是一个可认证upper的改进，不是证明intrinsic exact费用随之下降。

## 5. 费用的具体同对象接口：actual-jump Taylor子式

在L的每个primitive rank1 quotient选择生成元，逐层lift，得到兼容完整过滤的Z基。其相对于原monomial tuple基的矩阵是unimodular。令n₁<⋯<n_M为actual jumps，T_(V_D)为全部M列、这些M个Taylor行形成的square matrix。兼容基下它为triangular，diag就是上面的q_(n_j)，故det非零，绝对值为∏|q_(n_j)|。

对这些非零rational数应用product formula，严格得到

\[
\boxed{\mathcal A_D=-\log|\det T_{V_D}|.}
\tag{B13}
\]

因此真正待付量是完整native函数、真实jumps所定义的这个rational子式；不能换成某一窗口残差的rank、row prefix LCD或任选一次有限minor。N=mD+O(1)的零估计保证它在已付完整截断内，但没有给出精确jumps或其det的算术增长。

若a=limsup𝓐_D/D²已得一个finite upper，则同一证明将B9的κ替为a；有效费用为2a/m²。可由整格index upper认证a≤κ，也可直接支付负graded credit。单纯改变同metric Γ没有改变B13。

## 6. 本源的严格范围与下一有界准入

本源m=3。236全prime hybrid给κ≤45/4，从B9只得到费用5/2，未胜旧7/3；这既不证明a=45/4，也不排除本模型可有更小a。没有新的数值定理。

若欲令这个**单BC图、未另加convexity修正**的rank bound严格小于3，必须
3(λ−2a/9)>𝓙，
即

\[
a<\frac{9\lambda-3\mathcal J}{2}.
\tag{B14}
\]

对这类holomorphic图，Poisson–Jensen给𝓙≥λ；冻结共同图cap λ≤log C*，C*=3π³√2/8。因此该显示入口有必要条件a<3log C*。这是对intrinsic𝓐_D的必要门槛，不能把某个safe upper超出门槛当no-go。

B14不自动覆盖convexity、多图、binomial/其他metrics或改变ordinary target的all-place构造；这些方案要重付相应arch graded总和和度。235已付其固定类型显示入口的排除，不由本文扩成全部degree-D联合模型的排除。

238首接口应直接估计B13的全部n/全部prime费用，或等价地完整graded有限height；不只求更小κ。严格收益仍须同一图的真实𝓙/λ与目标关系假设，不能只比较capacity或两个upper。本文保留这个有界诊断，不恢复旧W或参数扫描。

实际来源读域在 literature/joint_lattice_metric_sources_round237_20261008/packet_reading_scope.md。数学程序0、prime/parameter scans0、旧producer0；仅NEW237数学稿和来源选页/记录，不改旧稿、main、manifest。保存后实际FULL作者复读并另报bytes/SHA。
