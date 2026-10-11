# Θ 的实际共同解析叶、Möbius quotient 与一个更大的 nonunivalent CDT map

2026-10-07。独立 NEW 研究记录。FULL 读取同目录 `cdt_weight4_space_germ_bridge_20261007.md`（S1–S40）；本稿只写此新稿，不改 main、manifest、旧 producer 或原仓库。所有证明均为纸面证明；没有新数值无理性、LI 或形式化验证结论。

本稿的实质新构造是

\[
 g(z)=\frac{(2\pi/3)z}{1-(2/3)z+z^2},\qquad
 \varphi_\rho(z)=\tan g(\rho z),\quad 0<\rho<1.
 \tag{G1}
\]

仅在 Θ=u∈Q 的同一个假设下，S39–S40 六项实际函数的共同 pullback 在半径 1/ρ 的整个 disk 全纯；|φρ′(0)|=ρ·2π/3，可严格超过旧 β slit 的尺度 2。对每一个有限 ρ 均有同一个 map 的严格估计

\[
 \log(\rho 2\pi/3)\le J(\varphi_\rho)
 \le \frac\pi{\sqrt2}-\log2.
 \tag{G2}
\]

下面另给 J 的有限零点精确公式，而不把右界称为精确值。证明不使用只在 ρ→1 才成立的积分界。还证明 2π/3 是所有 **injective arctan lift** 的 sharp derivative bound；不声称该子类已经覆盖所有共同 meromorphic maps。

## 1. 真实函数与 meromorphic pullback 的局部必要条件

沿用 S37–S40 的实际芽：

\[
 q(x)=\frac{1+x^2}{1+x},\quad R=\log q,
 \quad H=\theta^2D,\quad Q=\theta D,
\]
\[
 H'=-\frac{R}{1-x^2},\quad Q'=\frac Hx,
 \quad D'=\frac Qx,\quad F_u'=\frac{D-u}{1-x}.
 \tag{G3}
\]

R(0)=H(0)=Q(0)=D(0)=F_u(0)=0，且 θ³D=−xR/(1−x²)。在原枝 x=1，R(1)=0，所以 H、Q、D 完整全纯；D(1)=Θ。在 Θ=u 的关系下 F_u 也完整全纯。下文的 continuation 总从这些芽出发。

设 φ 是非恒定 map，φ(0)=0，且所有 G3 成员的共同 pullbacks meromorphic。由实际 R 而非其抽象 scalar ODE 得到：φ 必须 omit −1、i、−i。若 φ 在 z0 命中这些点，q(φ(z)) 有非零阶 zero 或 pole，于是任何 R 分支都有

\[
 R(\varphi(z))=k\log(z-z_0)+\text{holomorphic},\qquad k\ne0.
\]

这不可能 meromorphic：其导数的 residue 是 k，而任一 meromorphic function 的导数 residue 为0。若允许 φ 本身 meromorphic，则其 pole 同样使 q(φ) 产生非零阶 pole，亦被 R 排除。因此共同条件不能把 infinity 当成免费可过的点。

在 φ(z0)=1 的 transported sheet 上，log q 的值可能是 2πin。把 φ−1 的 zero order 记作 k，G3 的 H pullback 导数 residue 为 kR(1)/2。故必须 R(1)=0；随后 F_u 的 pullback 要求该 **同一 sheet** 的 D(1)=u。仅原枝 Θ=u 并不自动给其它 sheet 的这两个条件。

在 φ(z0)=0 的 transported sheet 上，R 已局部全纯，H 也局部全纯。Q pullback 的导数 residue 是 kH(0)，D pullback 的导数 residue 是 kQ(0)，所以必须 H(0)=Q(0)=0。D(0) 本身的非零 constant 不妨碍 meromorphic；不能额外把它误列为普遍必要的零值。

这些 residue 判断也说明有限 ramification 不能消除非零 logarithmic coefficient：它只把 residue 乘以一个正整数。它们没有证明所有共同 maps 必须落在某个预先指定的 slit plane。

## 2. q 的对称 principal-log 叶及其精确 conformal radius

令 a=√2−1、c=2a、k=√c。Möbius involution

\[
 \sigma(x)=\frac{1-x}{1+x}
\]

满足 q∘σ=q，交换 0、1，交换 −1、∞，交换 ±i。q 的两个 critical points 是 a、−1−√2，其 critical values 是 c、−2(1+√2)。准确地

\[
 q-c=\frac{(x-a)^2}{x+1}.
 \tag{G4}
\]

principal-log cut 的完整 preimage 是

\[
 \Gamma=q^{-1}(( -\infty,0])\cup\{-1\}
 =(-\infty,-1]\ \cup
 \{\,|x+1|=\sqrt2:\ \arg(x+1)\in[\pi/4,7\pi/4]\,\}.
 \tag{G5}
\]

这里把 pole −1 明确加入cut；等价地取球面闭cut ((−∞,0]∪{∞}) 的preimage再交finite plane。证明：若 x=s+it，则 Im q=t(1−2/|x+1|²)。real axis 上 q<0 恰在 s<−1；该圆上 q=2√2 cosθ−2≤0 恰为 G5 所列长弧。它们在 −1−√2 交叉，连同 infinity 形成嵌入球面的有限 tree，故 Ωq=C\Γ 是单连通域，含0和1，且 σ-invariant。

R=principal log q 在 Ωq 全纯且 R(1)=0。G3 的第一个 RHS 在1完整可去，下一两个 RHS 在0由 H(0)=Q(0)=0 可去，故依次取全纯原函数得到 R、H、Q、D 在 Ωq 全纯。在 Θ=u 下 F_u 亦在全域全纯。这是实际函数的共同叶，而非只对 log 或 scalar ODE 的域。

该叶可以完全 uniformize。取 Re√q>0 并定义

\[
 U(x)=\frac{\sqrt{q(x)}-k}{\sqrt{q(x)}+k},\qquad V(x)^2=U(x),
\]
\[
 V(x)=\frac{x-a}{\sqrt{x+1}\,\bigl(\sqrt{q(x)}+k\bigr)}.
 \tag{G6}
\]

这里 √(x+1) 为从0取值1的枝，G4 保证两个定义一致。q:Ωq→C\(−∞,0] 是 degree-two proper map，且仅有内部 branch point a；√q 和后续 Möbius map 把后一个域送到 unit disk。于是 U 是仅在 a 有二重零点的 degree-two proper disk map，V 是 degree-one proper disk map，即 conformal bijection Ωq→D。

写 β=√((1−k)/(1+k))。则 V(0)=−β、V(1)=β，且

\[
 V'(0)=\frac{k}{2\beta(1+k)^2},\qquad
 r_{\Omega_q}(0)=\frac{1-\beta^2}{V'(0)}
 =4\beta(1+k)=4(\sqrt2-1).
 \tag{G7}
\]

因此该 q-log leaf 的尺度是 4(√2−1)，不是2或4。它与旧 Dmix 的 cuts 不同，二者并非包含关系；不能称它为旧叶的严格 superdomain。σ 的确给了一个真实 symmetry quotient，但没有免费扩大尺度。其 normalized conformal map经 ρ 收缩后，所有共同函数全纯，且 J=log(ρ·4(√2−1))，理由见第5节的 univalent Jensen identity。

本轮独立发现的 dilogarithm quotient identity 已另载 root 新稿 `cdt_theta_involution_period_projection_20261007.md`，这里仅记录接口：若 K'=R/x、K(0)=0，则

\[
 H+\frac K2=-\frac12\operatorname{Li}_2(1-q),\qquad
 H\circ\sigma=\frac K2+\frac{\zeta(2)}8.
\]

几何证明不把该 endpoint ζ(2)/8 当成有理 normalization。

## 3. 一个超过尺度2的真实共同 map

定义

\[
 W=\mathbb C\setminus
 \bigl(( -\infty,-\pi/4]\cup[\pi/2,\infty)\bigr).
 \tag{G8}
\]

一般 real two-ray domain，端点 A<0<B，令 c=(A+B)/2、d=(B−A)/2。map c+2dt/(1+t²) 把 unit disk conformally 映到该域；boundary t=e^{iα} 给 c+d/cosα，导数在 disk 内非零，且唯一 inverse 在 disk。以 disk automorphism 把0送至 f^{-1}(0)，得到其 normalized radius

\[
 r_W(0)=\frac{2(d^2-c^2)}d
 =\frac{4|AB|}{B-A}.
 \tag{G9}
\]

对 G8，c=π/8、d=3π/8，真实 radius 是 **2π/3**。不能把 G9 误写成 2√(d²−c²)。normalized conformal bijection正是 G1 中的 rational g；其 boundary 为

\[
 g(e^{it})=\frac{2\pi/3}{2(\cos t-1/3)}\in\mathbb R.
 \tag{G10}
\]

现在令 φ=tan g。tan 在 W 内没有 pole；它自动 omit ±i。tan w=−1 的全部解 −π/4+nπ 都落在 G8 cuts，故 φ 还 omit −1。tan w=0 的全部解 nπ，仅0在 W 内；tan w=1 的全部解 π/4+nπ，仅π/4在 W 内。因此 φ 的0前像唯一，1前像唯一。g 的实 bridge 0→π/4 给 φ 的原实 bridge 0→1。

在 disk 上 log q(φ) 有从0正规化为0的全纯 lift。其1前像上的值由该实 bridge 准确等于0，故 H pullback 的导数在此 removable。0的唯一前像是原点，H(0)=Q(0)=0，使后续 Q、D pullback 依次全纯。Θ=u 时，1唯一前像的 D 值由实 bridge 等于Θ=u，故 F_u 亦全纯。整个证明没有用 transported branches 免费填其它0或1前像。

φ 本身并不 injective。例如 W 的 upper half-plane 中存在不同点 w 和 w+π，两者的 tan 相等；g 的两 inverse disk points 因而给 φ 的同值。它却 locally injective，因为 g′ 和 tan′ 在域内均非零。

其未收缩map的完整 plane image 还可准确识别：

\[
 \varphi(\mathbb D)=\mathbb C\setminus
 \bigl(( -\infty,-1]\cup\{i,-i\}\bigr).
 \tag{G10a}
\]

对非real x≠±i，全部 arctan branches 非real，故都在 W；对 real x，tan 的全部 inverse branches real，而 W 的 real interval恰映到(−1,∞)。这证明 G10a。它严格包含旧 Dmix，且非real像点有 infinitely many preimages；0、1各仅一枚。它不是这些函数的全局单值 plane leaf，而是实际 disk leaf 的像，也不需要 map 是整个image的covering。有限ρ的像紧含其中并随ρ↑1穷尽它；不声称任何一个有限ρ像包含无界 Dmix。

对 0<ρ<1，G1 的所有 pullbacks 在 |z|<1/ρ 全纯，故在 closed unit disk 的一个邻域全纯。它们满足 CDT 的共同 meromorphic 要求。φρ′(0)=ρ·2π/3；由于 π>3，取ρ足够近1即可严格超过2。

## 4. 同一个有限ρ map 的 J 上界：两个 singular inner functions

记 ζ=e^{iθ}，cosθ=1/3、sinθ=2√2/3，令

\[
 A=\frac\pi{2\sqrt2},\qquad
 P_\zeta(z)=\frac{\zeta+z}{\zeta-z}.
\]

直接比较 rational functions 的 poles、residues及0值，或直接通分，得到

\[
 g(z)=\frac{iA}{2}(P_\zeta(z)-P_{\bar\zeta}(z)).
 \tag{G11}
\]

因为 Re Pζ>0 于 disk，两个函数

\[
 f(z)=e^{-AP_\zeta(z)},\qquad h(z)=e^{-AP_{\bar\zeta}(z)}
 \tag{G12}
\]

bounded analytic，modulus≤1，且在 circle 几乎处处 modulus=1。f(0)=h(0)=e^{-A}，e^{2ig}=f/h。于是

\[
 \varphi_\rho(z)=-i\frac{f(\rho z)-h(\rho z)}
 {f(\rho z)+h(\rho z)}.
 \tag{G13}
\]

f+h 没有 disk 内 zero，因这种 zero 恰对应 tan g 的 pole。对任何有限ρ，Jensen 完整给

\[
 \int_{\mathbb T}\log|f(\rho z)+h(\rho z)|\,d\mu(z)
 =\log2-A.
 \tag{G14}
\]

令 bounded bidisk analytic function

\[
 E(z,w)=f(z)h(w)-f(w)h(z),\quad
 N_\rho=\iint\log|E(\rho z,\rho w)|\,d\mu(z)d\mu(w).
\]

φρ 的差值的准确 factorization 给

\[
 J(\varphi_\rho)
 =\log2+N_\rho-2(\log2-A)
 =2A-\log2+N_\rho.
 \tag{G15}
\]

这里 |E|≤2。有限ρ的Nρ有直接严格下界：对|w|=1，E(0,ρw)=e^{-A}(h(ρw)−f(ρw))连续且无零，因为φρ仅在0有zero；逐z Jensen给circle mean统一有限下界，结合log|E|≤log2，得Nρ为有限实数。diagonal log zero亦locally integrable。对各变量分别用 subharmonic circle means，Nρ 随ρ nondecreasing。f、h 的 radial boundary values 存在且均 unit modulus。对非负函数 log2−log|E| 用 Fatou，得

\[
 N_\rho\le\lim_{r\uparrow1}N_r
 \le\iint\log|E(z,w)|\,d\mu(z)d\mu(w).
 \tag{G16}
\]

右侧有限性不需先假设：左侧是有限数、被积函数有上界log2，所以 G16 已排除其为−∞。在 boundary 写 ξ=f/h∈T，因 |h|=1，右侧正是 ξ-pushforward probability measure ν 在 circle 上的 logarithmic energy

\[
 I(\nu)=\iint\log|\xi-\eta|\,d\nu(\xi)d\nu(\eta).
\]

这个 energy 总≤0。一个不需 Fourier convergence 假设的完整证明是：对 N 个 circle points，Vandermonde matrix 每列范数为√N，Hadamard 给

\[
 \prod_{j<k}|\xi_j-\xi_k|\le N^{N/2}.
\]

若 I=−∞，结论已成立；若有限，取 N 个独立 ν samples 的期望，得到 (N(N−1)/2)I≤(N/2)log N，故 I≤log N/(N−1)→0。因此 Nρ≤0，于 G15 得

\[
 \boxed{J(\varphi_\rho)\le 2A-\log2
 =\pi/\sqrt2-\log2\quad\text{对每一个 }0<\rho<1.}
 \tag{G17}
\]

G17 是有限ρ的已证 bound；并未声称 Nρ=0，也没有把 boundary limit 直接替代有限ρ。常数π/√2−log2约1.528，不等于 Lρ。

## 5. 精确 J：有限零点公式与 univalent 对照

若任意 holomorphic map ψ 在 closed disk 邻域全纯，ψ(0)=0、ψ′(0)≠0，两次 Jensen 给

\[
 J(\psi)\ge\log|\psi'(0)|.
 \tag{G18}
\]

若 ψ injective，(ψ(z)−ψ(w))/(z−w) 在 bidisk holomorphic 且 zero-free，两次 harmonic mean 给准确 J(ψ)=log|ψ′(0)|。G1 的 φρ 可能 noninjective，因此不免费使用这个 equality。

G1 的 inverse v=g^{-1}:W→D 可明确写为

\[
 v(s)=\frac{2s}{(2/3)s+r+\sqrt{((2/3)s+r)^2-4s^2}},
 \qquad r=2\pi/3,
 \tag{G19}
\]

square root 是从 s=0 取值r的 W 枝；v(0)=0。对固定 boundary w，φρ(z)=φρ(w) 等价于

\[
 g(\rho z)=g(\rho w)+n\pi,\qquad n\in\mathbb Z.
\]

n=0 的解 z=w 在 boundary，对 Jensen 没有 positive zero term。其它全部 inside zeros 正好为

\[
 z_n=\rho^{-1}v(g(\rho w)+n\pi),\quad
 g(\rho w)+n\pi\in W,\quad |v(g(\rho w)+n\pi)|<\rho.
\]

对固定ρ，该 sum 是有限的：令 Mρ=max|g(ρz)|，则 inside 解要求 |n|π≤2Mρ。所有 zeros simple，因为 φρ locally injective。又 φρ 仅在0有一个 simple zero，故第一次 Jensen 后再对w平均给准确恒等式

\[
 \boxed{
 J(\varphi_\rho)=\log(\rho r)
 +\int_{\mathbb T}\!
 \sum_{\substack{n\ne0:\ s_n\in W\\ |v(s_n)|<\rho}}
 \log\frac\rho{|v(s_n)|}\,d\mu(w),
 \quad s_n=g(\rho w)+n\pi.}
 \tag{G20}
\]

boundary zeros 不计正项，遇到临界 crossing 时 log term 连续归零；它们不会造成遗漏费用。G20 是同一 map 的精确有限表达式，完全刻画 cover 的 J penalty。G17 给无需 contour quadrature 的 uniform certified upper bound；G18/G20 给相同 map 的 lower bound。

本稿没有把数值 contour samples 当成 G20 的精确值，也没有证明一个尚未用到的 closed form Jρ。CDT 使用时可保留 G20，或明确以 G17 的 sufficiency bound 代替精确 J。

## 6. injective arctan lift 的 sharp 上界：一个自含两点 omission lemma

先证明两个 disjoint simply connected planar domains U、V，内点 a、b 的 conformal radii 满足

\[
 r_U(a)r_V(b)\le|a-b|^2.
 \tag{G21}
\]

只需先证 bounded smooth domains，再用 bounded subdomain exhaustion。取各 Green function G1、G2，延拓域外为0，令 u=G1−G2，ℓ=log|(z−b)/(z−a)|，v=u−ℓ。写d=|a−b|、r1=rU(a)、r2=rV(b)。v 在a、b正则，值为 log(r1/d)、log(d/r2)。删去两个半径ε的 disk，Green identity 给

\[
 \int|\nabla u|^2=2\pi\log(r_1r_2/\varepsilon^2)+o(1),
 \quad\int|\nabla\ell|^2=4\pi\log(d/\varepsilon)+o(1),
\]
\[
 \int\nabla v\cdot\nabla\ell
 =2\pi(v(a)-v(b))=2\pi\log(r_1r_2/d^2).
\]

所以展开 |∇u|²=|∇ℓ+∇v|² 并消去 logε，得到

\[
 \int_{\mathbb C}|\nabla v|^2=-2\pi\log(r_1r_2/d^2)\ge0,
\]

即 G21。域外的 gradient jumps 合法，因为 Green function 的 zero boundary extension 在其 pole 外属于局部 H¹；smooth exhaustion 同时处理一般边界。这是完整 energy proof，不依赖未读的外部 theorem。

现令 p:D→C injective、p(0)=0，omit real points A<0<B。取

\[
 T=\sqrt{\frac{p-A}{p-B}},\qquad T(0)=i\sqrt{|A|/B}.
\]

T injective，且 T(D) 与 −T(D) disjoint：相交会迫 p 同值，从而同一个 nonzero T 等于其负值。二域的 radii 相同，G21 给 |T′(0)|≤2|T(0)|。对 T 的 logarithmic derivative 求值，得到

\[
 \boxed{|p'(0)|\le\frac{4|AB|}{B-A}.}
 \tag{G22}
\]

G9 的 two-ray Riemann map达到 equality，故 sharp。

任意实际共同φ由 omit±i可取唯一 g=arctanφ lift，g(0)=0、g′(0)=φ′(0)、tan g=φ。若 **这个 g injective**，φ无pole与omit−1迫 g omit π/2、−π/4，G22准确给

\[
 |\varphi'(0)|\le2\pi/3.
 \tag{G23}
\]

G1 的ρ→1达到此supremum；所以 G23 在这个实际 map 子类内 sharp。它不以 φ injective 为前提；新构造本身就是 g injective、φ noninjective。它亦不把 g injective 当成 CDT 的要求；若未来构造更深的 noninjective g cover，G23 不适用。

若采用 companion `cdt_theta_rank_arithmetic_20261007.md` 的 actual rank6 和任意 Q(x) full basis 必要 τ≥97/72，则这个整个子类均没有 positive denominator：log|φ′(0)|≤log(2π/3)<1<97/72。严格 log bound只需 π<22/7、e>1+1+1/2。该费用结论来自 companion；本稿没有另行复写或从一个有限样本推断它。

## 7. 同一构造确实适用于 β_s，并给尺度π

β_s 系统没有 R 的 −1 singularity，故可取更大的 arctan domain

\[
 W_\beta=\mathbb C\setminus
 ((-\infty,-\pi/2]\cup[\pi/2,\infty)),
\]
\[
 g_\beta(z)=\frac{\pi z}{1+z^2},\qquad
 \varphi_{\beta,\rho}(z)=\tan g_\beta(\rho z).
 \tag{G24}
\]

φβρ 无pole、omit±i，tan的0前像在Wβ仅0，1前像仅π/4。T1 pullback恰为gβ(ρz)，Tj 的Euler inverse chain在唯一0前像由canonical zeros依次可去。β(s)=u或既有aβ(4)+bG=u时，F的唯一1前像通过原实bridge完整取消。故它是这些实际系统共同 holomorphic map，而非只对 arctan 的 map。

这里 |φβρ′(0)|=ρπ。第4节的同一 proof 用 ζ=i、A=π/2，得对每个有限ρ

\[
 \log(\rho\pi)\le J(\varphi_{\beta,\rho})\le\pi-\log2.
 \tag{G25}
\]

β 的未收缩map甚至有完整image φβ(D)=C\{i,−i}：real interval(−π/2,π/2) 经tan覆盖全部real axis，任意nonreal inverse branch都在Wβ。有限ρ images穷尽此image；仍只在disk leaf上同时取枝，不声称T_j可在这个punctured plane全局单值。其0、1前像唯一与nonreal点多前像并不矛盾；map不必为全部image的covering。

第5节的 finite-zero formula把g和r换为gβ、π即可，不遗漏 noninjectivity 的J penalty。第6节也给 β 的 injective arctan lift sharp bound |φ′(0)|≤π，因为该 lift omit±π/2。G24 超过旧 canonical β slit 的 derivative2；因此旧 slit 的 Schwarz bound不能外推为全部共同 map 的bound。

这仍未给 β4 的 rank contradiction：S22 已证必要τ≥11/9，而logπ<11/9。对G（m=4），τ≥7/8，且任意map的J≥L，rank contradiction需τ<(3/4)L；同一lift子类L≤logπ<7/6，因此也失败。两个strict log inequalities有完全有理证书：

\[
 e^{11/9}>\sum_{j=0}^4\frac{(11/9)^j}{j!}
 =\frac{530089}{157464}>\frac{22}7>\pi,
\]
\[
 e^{7/6}>\sum_{j=0}^5\frac{(7/6)^j}{j!}
 =\frac{2992597}{933120}>\frac{22}7>\pi.
\]

两个 cross-multiplied positive differences 分别为246415和419539，已用一个新 inline BigInteger 小证书核回。这里不把 β4/G 在这个 map 子类的失败说成其所有载体或所有 CDT maps 的失败。

实际上可以统一为全部整数 s≥2 的 β_s：S22 的 necessary cost与m=s+2、J≥L结合，rank contradiction必须

\[
 \frac{s(2s+3)}{(s+1)(s+2)}<L\le\log\pi.
\]

左侧记作f(s)，f(2)=7/6，且

\[
 f'(s)=\frac{3s^2+8s+6}{(s^2+3s+2)^2}>0.
\]

由已证logπ<7/6，整个 **injective arctan lift** 子类对这些实际 β_s full spaces 均不能给 rank contradiction。它比旧 slit 的范围大，仍不排除更深 arctan covers 或不同载体。

## 8. 新构造实际提供的门槛与剩余方向

同一 G1 map 的 m=6 rank contradiction需 τ<Lρ−Jρ/6。使用G17，充分条件是

\[
 \tau<\log(\rho2\pi/3)
 -\frac16(\pi/\sqrt2-\log2).
 \tag{G26}
\]

这是一条可直接复用的 certified map/J 接口；必要条件由G18为 τ<(5/6)log(ρ2π/3)。对目前 Θ 的 companion necessaryτ≥97/72，positive denominator已经失败，故没有新数值定理。最新有效 e=0 safe cap 见另一新稿 `cdt_new_repository_carriers_20261007.md` N11–N13：原六行的σ=(0,1,3/2,2,3,4)，τsafe=191/72；其半宽付款覆盖所有small primes、全部prime powers及整个prefix，N12只需u∈Q，Θ=u另承担原枝1的解析填点。这个最新safe上界仍不够。本稿原来引用的125/36是桥文旧safe baseline，保留为历史对照；必要下界97/72不变，不能把它与safe上界混为同一种证明。

新的几何 theorem 是：端点取消确实允许一个超过旧尺度2的实际共同 nonunivalent map，而且给有限ρ的完整 J 证书；不是证明所有 maps 都困在 polylog 的旧 slit 上。要越过 G23 的2π/3，未来必须使用 arctan lift 本身 noninjective 的 map，或更换 carrier。这样的 map 必须逐一支付 G3 的 transported0/1 residue条件；abstract D-finite singular point、允许meromorphic pole、或仅Θ原枝关系均不能把这些条件删除。

审计：本稿没有新增网页引用，所以未新增 literature download；所有新 geometry、J bound、two-domain radius lemma由文内纸证给出。G20是精确有限formula，G17/G25是upper bounds，两者明确定义。只新执行上述两个 integer cross-products，不据此外推解析证明。没有运行旧producer、PSLQ、prime扩表、数值J quadrature或Lean。

写后复审：作者实际FULL回读G1–26，随后回读全部增补。独立 `geometry_audit` 实际FULL读取最新G1–26、源稿S1–40和算术companion T1–27；独立重推共同pullbacks/0与1 residues、G11–17的finiteρ factorization/Fatou/Vandermonde、G20全部zeros及Jensen、G21所有Green-energy符号、G22–23 sharp范围、G4–10 q-leaf及exactimage、β全s≥2门槛与两个rational certificates。独立辅助审查复核q-leaf/inverse/β常数。审查提出的G5 pole-cut集合记号已修复，并补Nρ的Jensen统一有限下界；审者随后实际FULL最后回读含exactimage的新稿，最终数学PASS、无剩余修正。这里的PASS是独立纸面审读，不称形式化验证。

**2026-10-07 root 全文独审收据。** root 已实际FULL读取最终G1–G26，独立核G3的transported0/1 residues、q cut与proper degree-two map、G9精确2π/3、g/tan实际共同pullback及两个exact images、G11–17因子分解与每个finiteρ的separate subharmonic monotonicity/Fatou/energy≤0、G20全zero Jensen、G21 Dirichlet energy所有符号、G22两点omission，以及β全部s≥2的完整rank门槛，数学PASS、无新修正。此次root审阅针对同一几何稿的上述实际内容；另稿N13最新safe上界191/72由root另行FULL纸审，本文已经核读其N11–N13具体输入与hypothesis范围后引用。没有新建重复审计任务，也不把任一纸审PASS称为形式化验证或新的数值结论。
