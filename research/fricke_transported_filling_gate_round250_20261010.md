# 第250轮：全部二阶运输稳定子与共轭源的全有限点非补支

2026-10-10，C。固定 A248 的 t、K=Q(√2) rank3 源，假设数值 g+=Y/2+√2π²/28 属于 K。本文证明其**实际系数共轭源在 E 四根的每一个运输到达叶均有非零完整 odd 通道**。由此任意合法负地方多叶图均提升同一椭圆曲线，取得 |φ−′(0)|<20。数学程序0。此界只管负地方；正地方及两图都多叶的严格预算没有在这里关闭，也没有证明新数值无理性。

## 1. 全有限运输叶的稳定子分类

沿用
\[
\chi=\chi_{-7},\quad s=\sqrt2,\quad
A_-=A(\tau)-sA(2\tau),\quad I_-=R-(2s/7)D,\quad
g_\pm=Y/2\pm s\pi^2/28 .
\]
A248 实际商为
\[
t=\left(\frac{\eta_1\eta_{14}}{\eta_2\eta_7}\right)^4,\quad
X_0(14)/\langle W\rangle=\mathbf P^1_t,\quad
W\tau=-1/(14\tau),
\]
\[
y^2=E(t)=t^4-14t^3+19t^2-14t+1,\quad
Q_\pm=1-(7\mp4s)t+t^2 .
\]
Γ=Γ₀(14) 无 elliptic torsion，且 W normalize Γ。因此 H 的商 orbifold group Γ⁺=Γ∪ΓW，有限 ramification 恰 E 四根，对应 Γ⁺ 的 order2 fixed points。

具体说，沿任意 ordinary path 从 native 芽运输到某个 E 根，可提升到 H；端点 τ_* 的 stabilizer 不能在 torsion-free Γ 中，故为 γW。局部返回对 τ 的 action 是该 stabilizer；R,D,A− 本身在 H 单值全纯，所以相同 τ 提升没有另外未命名的 additive branch。其它到达叶只是不同的 H 提升，必须逐个保留其 γ，不需要、也不采用四个指定矩阵生成整个群的未证 statement。

写 γ=(a b;c d)∈Γ。γW 的 determinant-one normalization 的 trace 为 √14 b−c/√14。order2 强制 trace0，故 c=14b、ad−14b²=1。取同一 PSL class 的符号使 d>0，则所有稳定子均为
\[
\gamma=\begin{pmatrix}a&b\\14b&d\end{pmatrix},\quad
r_\gamma=\gamma W,\quad
\tau_\gamma=\frac bd+\frac{i}{\sqrt{14}\,d},\quad ad-14b^2=1. \tag{T1}
\]
d 不可能0；其正因子 1+14b² 是奇数、且 mod7 为1，所以 d 奇、(d,7)=1；并有 (b,d)=1。这个分类覆盖所有 E 根的所有运输叶，而不是仅 d=1,3,9 三个分母。

## 2. 全函数 affine 返回与完整 odd 条件

实际 weight1/χ 与 Fricke 身份给
\[
A_-(r_\gamma\tau)=j_\gamma(\tau)A_-(\tau),\qquad
j_\gamma(\tau)=i\sqrt{14}\chi(d)(d\tau-b).
\]
Θ²I−=h− 的 factor 为同一 jγ³。两次链式微分因此使
\[
P_\gamma(\tau)=j_\gamma(\tau)I_-(r_\gamma\tau)-I_-(\tau)
\]
为 affine polynomial。rγ²=id、jγ(rγτ)jγ(τ)=1，又迫
\(j_\gamma P_\gamma(r_\gamma\tau)+P_\gamma(\tau)=0\)。
在 affine polynomials 的二维空间中该 involution 的 −1 eigenspace 恰一维；非零 jγ−1 已在此空间，所以存在唯一常数 ρ_γ 满足完整身份
\[
\boxed{I_-(r_\gamma\tau)-\rho_\gamma
=j_\gamma(\tau)^{-1}[I_-(\tau)-\rho_\gamma].}           \tag{T2}
\]
此处不是以一个点值为整个 cocycle 命名：以下严格 radial limit 唯一算出这个 affine 常数。取
\(\tau=b/d+i/(14d^2\varepsilon)\)，则 rγτ=b/d+iε，
I−(τ)→0、|jγ(τ)|→∞。故
\[
\rho_\gamma=\lim_{\varepsilon\downarrow0}
 I_-(e^{2\pi ib/d-2\pi\varepsilon}).                  \tag{T3}
\]

对任意 c，记 B_c=A−(I−−c)。由(T2)
\[
B_c(r_\gamma\tau)-B_c(\tau)
=(\rho_\gamma-c)(j_\gamma(\tau)-1)A_-(\tau).          \tag{T4}
\]
令 ζ=(τ−τγ)/(τ−barτγ)，则 rγζ=−ζ、
\[
j_\gamma=\sigma\frac{1+\zeta}{1-\zeta},\quad
\sigma=-\chi(d),\qquad \widetilde A=A_-/(1-\zeta),\quad
\widetilde A(-\zeta)=\sigma\widetilde A(\zeta).
\]
于是完整 odd germ 恰为
\[
\boxed{\frac{B_c(\zeta)-B_c(-\zeta)}2=
\begin{cases}
-(\rho_\gamma-c)\zeta\widetilde A(\zeta),&\sigma=+1,\\
(\rho_\gamma-c)\widetilde A(\zeta),&\sigma=-1.
\end{cases}}                                         \tag{T5}
\]
σ=+1 时 ã(0)≠0；σ=−1 时 ã 有 simple zero。这由 A248 的完整 A− 零点 divisor/Q− simple roots 支付。t−tγ 是非零 ζ²·unit；所以 **这一叶完整补支 iff c=ργ**，不是只取消一个 ordinary 点值或首项。这也保留了 weight1 gauge；没有错将 A− 本身当成纯 odd/even scalar。

## 3. 奇分母处严格 Abel 极限及 denominator7

令 ζ_d=e^{2πi/d}，且 d 奇、(d,7)=1。实际级数为
\[
R(q)=\sum_{m\ge1}\frac{\chi(m)}{m^2}\frac{q^m}{1+q^m},\quad
C(q)=\sum_{k\ge1}\frac{T(q^k)}{k^2},\quad D=C(q)-\tfrac14C(q^2),
\]
\[
T(z)=\frac{z+2z^2+z^3+2z^4+z^5}{S_7(z)},\quad
S_7=1+z+\cdots+z^6,\quad T(1)=1 .
\]
对 ζ_d 的有限 phase classes，1+ζ_d^j r 在0≤r≤1无零；S₇(ζ_d^j r)也无零（z=1已 removable）。因此两个 kernels 有统一界，m⁻²、k⁻² 支配，(T3)的 R,C,D 极限确实存在。没有将条件发散的 Σχ(m) 作普通和。

在整数 group algebra Z[z]/(z^d−1)，乘 S₇ 的整数矩阵 determinant 恰为
\[
\prod_{\zeta^d=1}S_7(\zeta)
=7\prod_{\substack{\zeta^d=1\\\zeta\ne1}}
 \frac{\zeta^7-1}{\zeta-1}=7,                        \tag{T6}
\]
因为 ζ↦ζ⁷ 置换所有非单位 d 次 roots。其 adjugate 是整数，所以存在唯一
\[
T(z)\equiv\sum_{a=0}^{d-1}c_a z^a\pmod{z^d-1},
\qquad c_a\in(1/7)\mathbf Z .
\]
T(z⁻¹)=T(z) 给 c_a=c_{d-a}；代 z=1 给 Σc_a=1。这里(T6)是对全部 d 的 determinant identity，不是小 d 样本、只算某个 resultant 值或未认证的有限循环。

采用 NIST DLMF24.8.1 的完整 n=1 Fourier statement
\(\sum_{k\ge1}\cos(2\pi kx)/k^2=\pi^2B_2(x)\)，
0≤x≤1（含整数端点）。有限重排与上述对称性给
\[
\frac{C(\zeta_d^b)}{\pi^2}
=\sum_a c_a B_2(\{ba/d\}).
\]
记
\[
D_{b/d}:=\frac{D(\zeta_d^b)}{\pi^2}\in\mathbf Q,\qquad
M_{b/d}=\sum_a c_a\min(ba\bmod d,\ d-(ba\bmod d)).
\]
直接在 0≤x≤1 分成 x≤1/2、x≥1/2 核
\[
B_2(x)-\tfrac14B_2(\{2x\})=\tfrac18-\tfrac12\operatorname{dist}(x,\mathbf Z).
\]
因此
\[
\boxed{D_{b/d}=\frac18-\frac{M_{b/d}}{2d},\qquad
M_{b/d}\in(1/7)\mathbf Z,\qquad D_{b/d}\ne-\frac18 .} \tag{T7}
\]
最后一式：等于−1/8将迫 M=d/2，因7M整数而 7d 奇数，矛盾。包括 d=1，没有遗漏 finite boundary class。

## 4. 目标假设下，每个共轭叶都不可补支

对单位圆上的 ξ≠−1，Re[ξ/(1+ξ)]=1/2。因此严格支配逐项极限给
\[
R(\zeta_d^b)=Y/2+i v_{b/d},\qquad v_{b/d}\in\mathbf R,
\]
从而实际 affine 常数为
\[
\rho_\gamma=Y/2-(2s/7)\pi^2D_{b/d}+iv_{b/d}.          \tag{T8}
\]
这里不需要先认证所有 Γ cocycles 的虚部都是 π² 乘代数数：虚部若非零，就直接不能等于 real \bar g。

现在假设 g=g+∈K；实际共轭源是 B_{\bar g}=A−(I−−bar g)，bar g∈K⊂R。若某运输叶补支，(T5)迫 ργ=bar g；(T8)先迫 v_{b/d}=0，再得
\[
g-\bar g=\frac{s}{28}(1+8D_{b/d})\pi^2 .             \tag{T9}
\]
(T7)使右边系数为非零代数数。若 g−bar g=0，(T9)立即矛盾；若不为0，则 π²为代数数，同样矛盾。因此所有 γ 的 ργ−bar g 都非零，(T5)在每处给非零 first odd coefficient及完整 odd germ。

这证明 **所有 E 根、所有实际运输到达叶** 的共轭 B 均非 t-meromorphic。它没有把 bar g 设成 g−，不对未知Y任意施加 Galois automorphism，也不依靠四个 native returns 或尚未证生成系。实数值出口仍为 g+=Y/2+sπ²/28∉K 的研究目标；本文只是其假设下合法图的必要结构，不是该数值结论。

## 5. 任意负地方合法多叶图的真实椭圆提升

设 φ−:(D,0)→(C,0) holomorphic、非恒定，完整共轭三行拉回单值 meromorphic。在每个 φ−(z₀)=e、E(e)=0 的点，transport 到达叶由(T1)–(T9)全非补。若 φ−−e 的零阶 k 为奇数，(T5)的非零 sqrt 首项变成非整数 k/2 次幂，不能 meromorphic。因此每个这样的 k 都偶数。

E 的根简单，所以 E(φ−) 的所有零都是偶阶。D simply connected，存在全纯平方根 yφ，选 native yφ(0)=1。于是
\[
\psi(z)=(\phi_-(z),y_\phi(z))
\]
是到同一 smooth affine elliptic curve y²=E(t) 的全纯 map，并延入其 compactification。φ−始终 finite，故 ψ 遗漏两个 t=∞ points。这是本轮全叶量词付清后才取得的 lift；不是从 source 的形式 rank3 或“某叶坏”直接取得代数恢复，也不否定此前微分 module 不恢复 A−。

实际 FULL 读 Root248 research/dyadic_elliptic_uniform_cap_round248_20261010.md，8699 B，SHA256 ae596e99d2d477a766746c0392ff6938070d70fcc5fff85acc066ec5c947d72c。逐项匹配的是其§2–§5的 **同一曲线与微分**
\[
\omega=dt/y=f_{14}\,dq/q,\qquad \omega=(1+O(t))dt\text{ at }(0,1).
\]
不是把旧 x-coordinate 的最终 cap 整句搬过来。该稿的 exact birational Weierstrass identity
Y²=(X−1)(4X²+5X+23)、ω=−dX/Y，及两个实际 closed cycles给 Abel lattice Λ 的 covering radius R₀<5/3；不需要 cycles 是 primitive basis。

D 的 Abel lift Z 选 Z(0)=0，dZ=ψ*ω，则
\[
Z'(0)=\phi_-'(0)/y_\phi(0)=\phi_-'(0).
\]
ψ 遗漏任一 infinity point P，故 Z 遗漏其完整 Abel coset Z_P+Λ。Root248§5自含 Bloch引理适用任意 holomorphic、多叶 Z：image遗漏 covering radius≤R₀ 的 lattice coset ⇒|Z′(0)|≤12R₀。其证明是在局部导数最大点用 Schwarz/Rouché获得 derivative/12 的真实像圆盘，完全不要求单射。于是
\[
\boxed{|\phi_-'(0)|\le12R_0<20.}                    \tag{T10}
\]
这是负地方 all-maps bound；同一 ω 的 native normalization已明确，有限偶数分歧没有改变 Z′(0)。

## 6. 未付范围、来源与执行账

(T7)只排除 D=−1/8。正地方 B_{+,g+} 的对应必要实条件是 D=+1/8，本文未排除；native W 返叶确实填点。因此不把(T10)当两地方基本 strict-budget失败，也不在这里领正地方第三个全叶坏点或正图全 multi cap。更强 Bloch常数或同图整数 subsource 能量应由其完整证明另登记；本文只采用已 FULL 读的 12R₀版本。

CDT当前已付整型为两列均(0,1,1)、τ16/9；negative lift本身没有免费降低 primitive费用，也不替代整个数域所有嵌入的 J/λ 预算。数值目标尚未完成；是否继续须据正地方共同图、同对象全预算，而非重复 finite period/table/prime扫描。

本轮实际 FULL 读 A247两周期稿9308、A249四返回稿11197、Root249单叶稿8502、Root248椭圆稿8699；本稿不借 A249 的唯一 exact run 冒本人执行，未重跑或读其 producer 来认证全d。另实际完整读已存 NIST Fourier selection 的完整所用条件/公式，不冒称本轮人工 FULL HTML或上游证明；精确文件身份/读域另在本人NEW scope。A248及本人C249为冻结数学输入，实际本輪复用的选择/全文范围如实登记。

(T1)–(T10)均纸证。数学程序/CAS/finite samples/prime/parameter/map/Lean执行0，GET0，外 Git mutation0；旧/peer/Root/main/policy/manifest写0。只保存本文与独占NEW dual_reading_scope.md，写前已核两路径不存在。最终保存后作者 actual FULL 复读并报告 bytes/SHA；这不等于独审 PASS。

