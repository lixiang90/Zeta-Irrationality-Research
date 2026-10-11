# level20 excellent Frobenius：原文条件与 weighted Smith 的独立审核

日期：2026-10-06。本文只读审阅 [Frobenius 新稿](cdt_odd_level20_frobenius_20261006.md) 和 [Hasse 主稿 §4.1](cdt_odd_level20_hasse_20261006.md)，不修改其 producer，不修改冻结的 [原 Smith bridge](cdt_odd_level20_hasse_smith_bridge_20261006.md)。结论是新模 p³ 比值与两层算术关系成立；weighted Smith 的限定一变量合并也成立。它们不提供新的数值无理性结论，不自动给出 balanced tensor theorem。

已直接核读 [Beukers 固定 v3](../literature/beukers2025_supercongruences_modular_v3.pdf) 的 p7 Assumption II、pp15–18 Lemmas3.1/3.2/3.7及 Proposition4.2证明、pp20–21式(6)/Proposition5.1/weight2证明。下面明确哪些内容重新证明，避免扩大原文定理的字面适用范围。

## 1. 不能直接引用的原定理，以及合法的新命题

Assumption II(3)明确要求唯一零轨道位于 t 的极点，且零阶 r≤1。Proposition5.1(iv)和 Theorem1.13中 degree≤p−1 的结论使用此限制。新 Φ 的零阶 r=3，故不能说它满足 Assumption II，也不能直接说 Φ/Φ^σ等于通常 p 项截断。

新稿真正证明的是另一命题：完整 norm polynomial 的系数 G_p∈Z[t]、degree≤3p满足

\[
\frac{\Phi(t)}{\Phi(s(t))}\equiv G_p(t)\pmod{p^3},
\qquad s(t)=t(q(t)^p).
\tag{R1}
\]

这一命题不需要 r≤1；r=3只导致 pole/degree成本增加。其证明如下。A_± 本身带非平凡 Γ₀(20) character并有多个零轨道，不能用于下面的 Lemma3.7输入；换成 Φ 是实质必要步骤。

## 2. Φ 的整性、字符、除子与 norm polynomial

Φ=B/[t(1−t)] 的 eta exponents按 d=(1,2,4,5,10,20)依次为

\[
e=(-4,10,-4,-4,10,-4).
\]

逐项检查给

\[
\sum e_d=4,\quad \sum d e_d=0,
\quad\sum(20/d)e_d=0,\quad
\prod d^{e_d}=400=20^2.
\tag{R2}
\]

所以它是权2、Γ₀(20) character平凡的 eta form。整数 powers（含负数）及零 q-exponent给 Φ∈1+qZ[[q]]，其 inverse也在 Z[[q]]。整数双向 q↔t坐标进一步给 Φ(t)∈1+tZ[[t]]。

用 eta cusp order公式

\[
\operatorname{ord}_{1/c}\Phi=
\frac{20}{24\gcd(c^2,20)}
  \sum_{d\mid20}e_d\frac{\gcd(c,d)^2}{d},
\]

在 c=(1,2,4,5,10,20)得到(0,3,0,0,3,0)。上半平面没有 eta zeros；所有 cusp orders非负。因此 Φ为 holomorphic form，两个零 cusp由 W₂₀配成同一个 t=∞轨道，各阶3。对 Fricke，直接 eta transformation给 Φ(W₂₀τ)=−20τ²Φ(τ)，故 weight2 slash multiplier是−1。这个 multiplier在 Γ₀(20)上平凡，正满足 Lemma3.7所需假设；不是要求整个 extension character都平凡。

对 p∤20的 determinant-p representatives

\[
\gamma_\infty=\begin{pmatrix}p&0\\0&1\end{pmatrix},
\qquad
\gamma_k=\begin{pmatrix}1&k\\0&p\end{pmatrix},
\]

weight2 slash factors为

\[
\Phi|_2\gamma_\infty=p\Phi(p\tau),
\qquad
\Phi|_2\gamma_k=p^{-1}\Phi((\tau+k)/p).
\tag{R3}
\]

所以新稿 T_p正是

\[
p^{2p}\prod_{[\gamma]}
 \left(1-\frac{\Phi|_2\gamma}{p\Phi}X\right).
\]

Lemma3.7使其 coefficients真正 Γ-invariant。分子 slash forms在各 cusp及上半平面均 holomorphic；唯一 possible poles来自 Φ的唯一零轨道。X^m coefficient在此轨道 pole order至多3m。t是该 genus0商的 Hauptmodul、在此轨道有 simple pole，因此该 coefficient是 degree≤3m的 polynomial in t。

其整性也不使用 r≤1。展开 T_p时，fractional-q terms的 elementary symmetric sums由 translation k↦k+1强制整指数；cyclotomic Galois invariance及 algebraic integrality强制各 coefficient在 Z[[q]]。Φ^{-1}也是 integer unit series。再用 integer q(t)反演，polynomial in t的每个 coefficient实际是整数。所以 T_p∈Z[t,X]。

eta norm phase是

\[
\exp\left(\frac{2\pi i(p-1)}{48}\sum d e_d\right)=1.
\]

Lemma3.2于是给精确恒等式

\[
\Phi(p\tau)\prod_{k=0}^{p-1}\Phi((\tau+k)/p)
 =\Phi(\tau)^{p+1}.
\tag{R4}
\]

奇 p时 T_p的 leading coefficient为1，degree为 p+1。其根是 x₀=Φ/Φ(pτ)与 p个 x_k=p²Φ/Φ((τ+k)/p)。因此

\[
G_p=-[X^p]T_p=\sum x_i\in Z[t],\qquad\deg G_p\le3p.
\tag{R5}
\]

使用安全3p上界已经充分。原 eta cusp argument还会给 strict degree<3p，但本审阅不把有限样本的 reduction degree3p−3升级成未证明的全素数更细界。

## 3. trace 权重与全级数模 p³比值

令 1/Φ(q)=Σb_nq^n∈Z[[q]]。完整 root sum给

\[
\begin{aligned}
G_p(t(q))
 &=\frac{\Phi(q)}{\Phi(q^p)}
  +p^2\Phi(q)\sum_{k=0}^{p-1}
       \frac1{\Phi(\zeta_p^kq^{1/p})}\\
 &=\frac{\Phi(q)}{\Phi(q^p)}
    +p^3\Phi(q)\sum_{j\ge0}b_{pj}q^j.
\end{aligned}
\tag{R6}
\]

p²来自权2 slash normalization，另一个 p来自 roots-of-unity trace；不能丢掉其中一个因子，也不能使用权1的 root权重。trace后的 inverse coefficients是整数，所以余项真的属于 p³Z[[q]]。整数 q(t)把它转换成全级数(R1)，而不只是 degree<p前缀。G_p(0)=1+p³保证 its rational inverse在原点是 p-integral unit。

模 p下，s(t)≡t^p且 Φ(s)≡Φ(t)^p，故 G_p≡Φ^{1−p}。结合冻结 Hasse关系 B^{1−p}=P_p/[t(1−t)]^{p−1}，得到 G_p≡P_p。这里不是从有限 jet猜测 polynomial相等。

## 4. Hasse §4.1的真正 source packet

早稿中的 actual definitions是

\[
E_k=C_k+\sum_{d\ge1}\chi(d)d^{k-1}\frac{q^d}{1-q^d},
\qquad
F_k=\sum_{m,n\ge1}\chi(n)m^{k-1}q^{mn}.
\tag{R7}
\]

对1≤j<p，divisors分成含p与不含p，给权4 nonconstant coefficients的精确分裂

\[
a_{pj}=(1+\chi(p)p^3)a_j,
\qquad b_{pj}=(\chi(p)+p^3)b_j.
\tag{R8}
\]

oldform scales2、4与p互素，故相同因子保留。对指数pj，θ_q^{-3}除以p³j³；乘p³后 j³是 unit，(R8)分别模p³归为 u_j与χ(p)v_j。对p不整除的指数，乘p³后其 coefficient属于p³。于是整个 n<p²前缀有

\[
p^3 f_\pm(q)
 \equiv (u\mp\sqrt5\chi(p)v)_{<p}(q^p)
 \pmod{\mathfrak p^3,q^{p^2}}.
\tag{R9}
\]

固定周期在反证假设 c∈Q后是好𝔭处的 integral constant，故乘p³也在𝔭³中。Hasse主稿 §4.1因而成立。它用 degree<p的 p-integral source截断；没有 reduction含 p-denominator的完整 Eichler series。

令 s(t)=t(q(t)^p)，真实 identity q(s(t))=q(t)^p；ord_t s=p，integer反演保持前缀理想。因此

\[
p^3H_\pm(t)\equiv
A_\pm(t)\widetilde F_{p,\pm}(s(t))
\pmod{\mathfrak p^3,t^{p^2}}.
\tag{R10}
\]

将 s换成 t^p只能在模p下使用，在模p³中不合法。p³H仅在所保留前缀保证 integral，(R10)不声称所有高指数也已由p³整化。

## 5. 两种 connection与 polynomial rows

实际 A_±=−R_±Φ/5，R_±=N_±√C_±，分支在原点取1。θ_qt=B√Δ给 S=θ_q log t=(1−t)√Δ·Φ。取 g_s=(1−t)√Δ，则

\[
\vartheta s=psb,\quad b=S(s)/S(t),
\quad b\equiv\frac{g_s(s)}{g_s(t)G_p(t)}\pmod{p^3}.
\tag{R11}
\]

由(R10)、(R1)，Y=p³H满足 Y≡gW(s)mod(p³,t^{p²})，g=RG_p、W=−ΦF/5。设 k=R/g_s、a₀=ϑlogg、a₁=ϑlogk、∇ᵢ=ϑ−aᵢ。Euler derivative保持t^{p²}理想，所有 aᵢ、b是原点的p-integral rational/series，因此

\[
\nabla_0Y\equiv p k g_s(s)\vartheta_zW(s),
\]

再用 ∇₁k=0与(R11)，得到

\[
\nabla_1\nabla_0Y\equiv
p^2kb\{(\vartheta g_s)(s)\vartheta_zW(s)
             +g_s(s)\vartheta_z^2W(s)\}.
\tag{R12}
\]

所以 ∇₀Y在p中，∇₁∇₀Y在p²中，均针对全部n<p²前缀。第二次 connection不同，不能把它解释成同一个一阶 Hasse算子免费提升到模p²。

新稿的 D₀=NCG_p、D₁=N(1−t)C_o都在原点为 unit。取Mᵢ=Dᵢaᵢ，重推 operator composition给

\[
(D_1D_0\vartheta-D_1\vartheta D_0-D_0M_1)
 (D_0\vartheta-M_0)
 =D_1D_0^2\nabla_1\nabla_0.
\tag{R13}
\]

该 row coefficient最大 degree≤2(3p+4)+5=6p+13。第三 coefficient为 D₁D₀²，mod𝔭不为零，因为 G_p≡P_p非零、N、C、C_o、1−t也非零。它不证明第三valuation层；也不证明 coefficient row已 primitive/saturated。

新稿§5另研究全形式级数、一阶 primitive模p² logarithmic-lift障碍。本审阅的核心范围是该稿§§1–4；以下 weighted Smith证明完全不使用§5障碍。即使该障碍另经独立核验，它的范围也不能扩大到有限 jets、(R12)的不同第二connection或高维tensor新构造。

## 6. 真正 weighted Smith：两组方向可以重叠

此节在完整 leading-order cutoff已经由 actual closed系统证明的限定一变量原格中使用；沿用原 bridge的 Ψ=p³eval_{<N} integral。任一完整 leading minor B为 R×R integral matrix，特征零可逆，其 Smith exponents为 a_i≥0。取

\[
S_j=\{v\in E:Bv\in p^jF\},\qquad j\ge1.
\]

Smith normal form逐坐标证明

\[
\dim_k\operatorname{image}(S_j\longrightarrow E/pE)
 =\#\{i:a_i\ge j\}.
\tag{R14}
\]

原因是 Smith coordinate满足 p^{a_i}v_i∈p^j；当a_i<j时 v_i被p整除，其modp像为0；当a_i≥j时该coordinate任意。整变换属于GL_R(O_{K,𝔭})，保持 image维数和原局部norm。

对p>√N、p≤D，Hasse两条 modp polynomial rows提供

\[
k_1=2(D-\delta_p+1)_+,
\qquad\delta_p\le(3p+9)/2,
\]

个modp独立向量在S₁。Frobenius order2 row的 coefficients degree≤6p+13，且第三 coefficient modp非零；其次数≤D−(6p+13)的 polynomial multiples因此给

\[
k_2=(D-6p-12)_+
\tag{R15}
\]

个modp独立的实际 integral向量在S₂。它们的第三 coordinates是非零 polynomial乘各 monomials，故独立性是k[t]整域上的确切结论。

这些向量可以同时位于S₁，也可以落在已有Hasse span中。**不需要两组的联合modp独立性**；由(R14)

\[
\boxed{v_{\mathfrak p}(\det B)
 =\sum_i a_i
 \ge\#\{a_i\ge1\}+\#\{a_i\ge2\}
 \ge k_1+k_2.}
\tag{R16}
\]

这正是不同 valuation阈值的加权收益，不能说新 row是额外两个普通kernel。

原实际 pole-cleared basis是 Δ²H、Δ²ϑH、Δ²ϑ²H。将 coefficient row作用于这三个函数只把 output共同乘Δ²，保持(R12)和modp独立性；没有把 ϑ^j(Δ²H)冒充这些函数，所以 row度数不增加。constant及廉价背景source blocks都可以取0，故(R16)同时用于原 bare rank4及已核rank7原格。所有 source、metric和degree仍保持原样，未使用换格index作为净收益。

## 7. 主项及限定一变量最终账本

全部小素数和坏素数仍使用原LCM³上界。只在p>√N的合法窗口扣除(R16)。PNT给

\[
\sum_p(2D-3p-7)_+\log p
 =\left(\frac23+o(1)\right)D^2,
\]

\[
\sum_p(D-6p-12)_+\log p
 =\left(\frac1{12}+o(1)\right)D^2.
\tag{R17}
\]

其中移除p≤√N和有限坏p只损失o(D²)。总原格 determinant收益为 γD²，γ=3/4。归一化数域 places仍同值，因为所有𝔭∣p适用同一界、Σf_𝔭=[K:Q]。

沿用 [原一变量全账](cdt_odd_level20_hasse_global_20261006.md) 中相同 primitive quotient metrics、actual合法map、normalized averagesρ̄/J̄：

|实际固定源格|source degree / D²|arch evaluation / D²|finite evaluation / D²|
|---|---|---|---|
|bare rank4|2J̄+3|−8ρ̄+4J̄|51/2−3/4=99/4|
|rank7、unit背景1,L,T₂,K₂|7J̄/2+21|−49ρ̄/2+7J̄|84−3/4=333/4|

slopes inequality因此分别给限定一变量界

\[
\boxed{4\bar\rho-\bar J\le87/8},
\qquad
\boxed{7\bar\rho-\bar J\le249/14}.
\tag{R18}
\]

若把 RHS除以实际rank书写为该**一变量特殊界**的常数，它们是87/32与249/98。这些数不取代 Theorem8.0.1任意矩阵/balanced tensor成本。

Jensen floor J̄≥ρ̄使产生矛盾至少分别需要ρ̄>29/8、ρ̄>83/28。两者都大于log16，而 genuine cusp1及唯一原点原像给ρ̄≤log16。因此这两个固定一变量表仍不能证明目标常数无理。它们确实比前一层原格账更强，但结论仍是新的算术输入和经过完整记账的结构进展。

## 8. 核验边界

本审阅没有重跑104check producer；固定 p=7,11,13的有限证书属于新稿作者的执行记录。本审阅依据上述全素数eta/modular divisor、trace、divisor-sum、链式法则和DVR Smith证明。

已只读核对 root全局稿§6.1的实际正文：其 k₁/k₂次数、Smith阈值、额外1/12与总3/4主项、finite99/4及333/4，以及式(17)的87/32及249/98与(R14)–(R18)完全匹配。原一变量 metric/field接口已有前轮独审；balanced tensors的source species、primitive leading jets和valuation分布须另证。

本稿不修改任何已冻结报告，不宣称第三层节省、不宣称原 Theorem1.13适用于r=3，也不将有限同余当作新数值无理性证明。
