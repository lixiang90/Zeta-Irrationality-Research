# 实际九阶对偶反射列与有理强迫提升：完整 ζ(5) 填洞、第二跳跃和全 prime 费用

2026-10-07，作者 /root/source_pencil_finalize。唯一 NEW 纸面主稿。Authority 为总稿 §§181–185 及 `cdt_odd_delivery_balanced_gamma_direction_20261007.json`；588 冻结记录（583 数学、5 guards）、旧及同行 producer、素数表只读。本轮数学 producer 新建/执行/import/rerun、guard 执行、prime 扩表均为0。文献提取、目读和 SHA 属 documentary 操作。

本稿实际全文重读冻结 Gamma G1–G19、period-extension E1–E24 与 authority §§181–185。原 source 仍为 ξ=αζ(4)+βζ(5)，β≠0；以下 ζ(5) 单项只校准同一实际 U，未把原 source 免费换成 κ5、κ7 或其他数。本稿给出两个实质接口：补出 rank-nine 反射的缺列；通过逆系数强迫把已知 ζ(5) endpoint 真正提升成完整 conifold connection coefficient。后者同时保留 Q[[t]] 起点，但引入另一处确切 log 分支和付费 cap；没有新的无理性结论。

## 1. 固定同一齐次系统并求出完整反射矩阵

**D1（对象和路径）。** 沿冻结 G3 的 0<t<c 实路径、同一 log t 分支，取

\[
a=(\tfrac12^\times5,\tfrac15,\tfrac25,\tfrac35,\tfrac45),\quad
\Lambda=3200000,\quad c=\Lambda^{-1},\quad D=t\partial_t,
\]
\[
L=D^9-\Lambda t\prod_i(D+a_i),\qquad
f_0=\sum_{n\ge0}h_nt^n,\quad
h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbb Z.
\tag{D1}
\]

完整 Frobenius 解 φ_j（j0..8）仍是冻结 G3 的 [s^j]t^sΣ A_n(s)t^n，不是正则部分 η_j。记 ψ=Δ_cφ0≠0。所用 Bloch–Vlasenko Proposition26 已在冻结 G4–G7 支付变量缩放，给

\[
\Delta_c\phi_j=\kappa_j\psi,\quad
\kappa(s)=\frac{\Gamma(1+s)^{15}}{\Gamma(1+2s)^5\Gamma(1+5s)},
\quad\kappa_0=1.
\tag{D2}
\]

conifold 指数为0..7、7/2；全局 monodromy irreducible。以下仅补出这个实际反射矩阵，不称为所有0-to-infinity Barnes连接矩阵。

**D2（实际 adjoint 与 Green pairing）。** adjoint 相对于 dt/t 定义，D*=-D。a 关于1/2对称，且移动 t 时必须保留 D 的次序。因此

\[
L^*=-D^9-\Lambda\prod_i(-D+a_i)t
=-D^9+\Lambda t\prod_i(D+1-a_i)=-L.
\tag{D3}
\]

写 L=Σ_{k=0}^9 A_k(t)D^k，A9=1−Λt，低阶 A_k=O(t)。令

\[
J(f,g)=\sum_{k=1}^9\sum_{r=0}^{k-1}
 (-1)^r D^r(A_k f)D^{k-1-r}g,
\quad\mathscr B(f,g)=\tfrac12(J(f,g)+J(g,f)).
\tag{D4}
\]

逐项 telescoping 给 D J=fLg−(L*f)g=fLg+(Lf)g；故同样有

\[
D\mathscr B(f,g)=fLg+(Lf)g.
\tag{D5}
\]

齐次解上的 pairing 恒定、对称且由此保存于 monodromy。t→0 的低阶 O(t) 项消失；φ_i=(log t)^i/i!+O(t polynomial(log t))。D9 的 concomitant 对两个 degree≤8 的多项式恒定，在 log t=0 求值即

\[
S_{ij}:=\mathscr B(\phi_i,\phi_j)=(-1)^i\delta_{i+j,8},
\qquad S^{\mathsf T}=S,\quad S^{-1}=S.
\tag{D6}
\]

这也是本系统 self-dual 的具体有理 de Rham pairing；不声称该 φ basis 就是一个已支付的 integral Betti lattice。

**D3（完整缺列）。** 写 ψ=Σ w_iφ_i，则 T_c=I+wκ^t，κ^tw=−2。对 v∈kerκ，T_c 固定 v；T_c 为 pairing-preserving 反射，因而 Sw 是 κ 的倍数。于是

\[
w=-\frac{2S\kappa}{\kappa^{\mathsf T}S\kappa},\qquad
\kappa^{\mathsf T}S\kappa=[s^8]\kappa(s)\kappa(-s).
\tag{D7}
\]

最后常数可以有限纸面核算。若以 π^{2j}s^{2j} 为单位，log κ(s)κ(−s) 至8阶的系数为

\[
a_2=-5,\quad a_4=-23/6,\quad a_6=-118/21,\quad
a_8=-13063/1260.
\]

指数展开的8阶系数为

\[
a_8+a_2a_6+a_4^2/2+a_2^2a_4/2+a_2^4/24
=\frac{-26126+70800+18515-120750+65625}{2520}=\frac{16}{5}.
\]

因此完整实际列和矩阵是

\[
\boxed{w_i=-\frac{5(-1)^i\kappa_{8-i}}{8\pi^8},\qquad
T_c=I+w\kappa^{\mathsf T}.}
\tag{D8}
\]

κ^tw=−2、T_c²=I 和 T_c^t S T_c=S 均随 D7 直接成立。特别 w8=−5/(8π8)≠0；即使假设 κ5 或 κ7 有理，也不消掉 ψ 的最高 log8 起点。实际对偶周期并未凭 adjoint 自动成为 Q-Taylor。

## 2. 有理起点的逆系数提升与 polynomial forcing 的确切局限

**D4（唯一实际 analytic particular）。** 对 R=Σ_{m≥1}R_m t^m∈Q[[t]]，正规化 B_R(0)=0，由 L B_R=R 得

\[
n^9b_n-\Lambda\prod_i(n-1+a_i)b_{n-1}=R_n,
\quad
\boxed{b_n=h_n\sum_{m=1}^n\frac{R_m}{m^9h_m}.}
\tag{D9}
\]

常数项必为 R0=0，因为 L 对所有 analytic germ 的常数项为0。每个 n≥1 的递推系数 n9 非零，故 B0=0 固定后唯一；不是自由选一个有利的 particular。

**D5（全部 polynomial forcing 都 split）。** 对 R=t^m（m≥1），D9 直接给

\[
\boxed{B_{t^m}=\frac{f_0-\sum_{n=0}^{m-1}h_nt^n}{m^9h_m}.}
\tag{D10}
\]

故任意 R∈tQ[t] 的 B_R=C_R f0−Q_R(t)，其中 C_R=Σ R_m/(m9h_m)∈Q、Q_R∈Q[t]，且 Δ_cB_R=C_Rψ。若 κ5 或 κ7 碰巧等于某个这个有理 C_R，所得 branch-fill 仅是早已有的多项式；该 fixed polynomial-forcing family 不能提供新的 irrational connection coefficient。这个结论不排除 rational/nonpolynomial forcing。

**D6（真正的 connection-functional）。** 若 R 的实际 Taylor radius R_* 满足 R_*>c，令

\[
\boxed{C_R=\sum_{m\ge1}\frac{R_m}{m^9h_m}.}
\tag{D11}
\]

它绝对收敛。Stirling 给 h_n=HΛ^n n^{−9/2}(1+O(1/n))，H>0。固定 c<q<R_*，Cauchy estimate |R_m|≤M_q q^{−m}，故 R_m/(m9h_m)=O((Λq)^{−m}m^{−9/2})。因此

\[
A_R:=C_Rf_0-B_R
=C_R+\sum_{n\ge1}h_n\left(\sum_{m>n}\frac{R_m}{m^9h_m}\right)t^n
\tag{D12}
\]

在 |t|<q holomorphic：系数至多 O(q^{−n}n^{−9})，有限初项不影响。这给出同一函数的完整 connection 身份

\[
\boxed{\Delta_c B_R=C_R\psi.}
\tag{D13}
\]

若 C_R=u∈Q，F_u=B_R−u f0∈Q[[t]] 且真正 holomorphic 穿过 c。这同时保留起点、全部跳跃和同一原 L，跨出了冻结 η-package 的 obstruction；并非只使普通点取值为0。

**D7（κ5/κ7 的剩余确切方程）。** 对冻结 G9 的 κ5=654ζ5−750ζ2ζ3 和 κ7=11250ζ7−9810ζ2ζ5+(10875/2)ζ3ζ4，D6 将新候选问题精确化为

\[
R\in t\mathbb Q(t),\quad\operatorname{radius}(R)>c,\qquad
\sum_{m\ge1}\frac{[t^m]R}{m^9h_m}=\kappa_j.
\tag{D14}
\]

满足 D14 的 R 还必须支付全部 pole jumps、caps 和 endpoint normalization。本稿未找到给 κ5/κ7 的这条恒等式；求出 D8 不等于求出它。以下 ζ5 则能由同一 U 的已知 analytic identity 精确校准。

## 3. 同一实际 ζ(5) endpoint 被提升为完整 conifold coefficient

**D8（所有常数明确的 rational forcing）。** 冻结 period E11/E12 和 Au v4 Example X 给

\[
U(w)=\sum_{m\ge1}\frac{(m!)^9}{m^9\prod_i(a_i)_m}w^m,
\quad w_0=-1024/3125,
\]
\[
P(T)=5532T^4-5600T^3+2275T^2-425T+30,
\qquad -P(\theta_w)U(w_0)/380928=\zeta(5).
\tag{D15}
\]

该已知 analytic identity 已由 primary Au 校准，不以 Kerr 一般 geometric theorem 的 Hodge/cycle 条件替代它。h_m=Λ^m∏(a_i)_m/(m!)9。设

\[
a=\Lambda w_0=-2^{20}=-1048576,
\quad\mu=a^{-1}=-2^{-20},\qquad
\boxed{R_5(t)=-\frac1{380928}P(D)\frac{at}{1-at}.}
\tag{D16}
\]

R5∈tQ(t)，R_m=−P(m)a^m/380928；radius |μ|=2^{−20}>c。注意 P 的 degree 恰4，不是5。D11/D15 因而给确切

\[
\boxed{C_{R_5}=\zeta(5),\qquad L B_5=R_5,\quad B_5(0)=0,\quad
\Delta_cB_5=\zeta(5)\psi.}
\tag{D17}
\]

B5 的所有 Taylor coefficients 由 D9 唯一指定。原 ordinary-point quasi-period 经过一个真实 inverse-L construction 成了原 fundamental period 的完整反射系数；不引入未知 ζ3、log2 或未写出的 connection 常数。

**D9（真实 relation-dependent leaf）。** 对固定 u∈Q，定义

\[
F_u=B_5-u f_0,\quad
\boxed{\Delta_cF_u=(\zeta(5)-u)\psi.}
\tag{D18}
\]

在 ζ5=u 的假设下，D12 已给 |t|<|μ| 的 holomorphic 延拓，包含 c；再沿原 L 的 ordinary points 继续。L 的唯一有限 singularities 是0、c；R5 的唯一有限 pole 是μ。Fu 在0实际 analytic，在c的 full jump消失且实际 exponents 非负。故指定 germ 在

\[
\boxed{\Omega=\mathbb C\setminus(-\infty,\mu]}
\tag{D19}
\]

具有单值 holomorphic 延拓。具体说 Ω 去掉 {0,c} 后的两个基本 loops 均对 Fu 平凡，填入0、c后 monodromy theorem 给 Ω 上函数。Fu 本身从Q[[t]]开始，且此处没有把含 log 的 φ5 当成 Taylor function。D19 是一个有效 filled leaf，不声称是最大 leaf 或所有允许 maps 的范围。

## 4. 第二极点的完整跳跃与不平凡 rank-ten 扩张

**D10（强迫 pole 和首项）。** μ 是 L 的 ordinary point，因为 μ≠0,c。令 x=t−μ，则 at/(1−at)=−μ/x−1。D4geo 的 leading term 为−24μ5x−5，故

\[
R_5=r_{-5}x^{-5}+O(x^{-4}),\qquad
r_{-5}=\frac{24\cdot5532\mu^5}{380928}\ne0.
\tag{D20}
\]

L 在普通 ∂t 坐标的9阶首系数为 μ9(1−Λμ)≠0。ordinary inverse 对 pole5 积分9次，给

\[
B_5=A(x)+H(x)\log x,\quad A,H\text{ analytic},\quad LH=0,
\]
\[
\boxed{H(x)=\frac{5532}{24\cdot380928\mu^4(1-\Lambda\mu)}x^4+O(x^5).}
\tag{D21}
\]

理由可由 ordinary variation-of-constants 严证：fundamental inverse matrix analytic，积分 meromorphic functions 只产生有限 Laurent part和 log；若存在负 Laurent 首项，其 L 首项有 pole≥10，不能匹配 pole5，而 log项的最早 pole通过九次积分恰为5。也可逐阶先以 analytic homogeneous H 配出全部 principal part，再解 analytic remainder。∂t9(x4logx)=576x−5，给 D21 的系数；local H 的 vanishing order 恰4。因此

\[
\chi_5:=\Delta_\mu B_5=2\pi iH\ne0,
\qquad\Delta_\mu F_u=\chi_5\quad\text{对所有 }u.
\tag{D22}
\]

conifold 的填洞并没有消掉这个独立的第二跳跃。

**D11（不是仅列最高项：完整 jump vector）。** 在从原0基点到 μ 邻域的固定解析路径上继续 φ basis，取绕 μ 的正向小 loop（不绕0、c）。D5 积分给全部实际九个常数

\[
\mathscr B(\phi_i,\chi_5)
=2\pi i\operatorname{Res}_{t=\mu}\phi_iR_5\frac{dt}{t}.
\tag{D23}
\]

dt/t 下 residue integration-by-parts 使 D 移到 φ时成为−D；geo 的 residue 是−1。于是

\[
\operatorname{Res}_{\mu}\phi_iR_5\frac{dt}{t}
=\frac{[P(-D)\phi_i](\mu)}{380928},
\]
\[
\boxed{\chi_5(t)=\frac{2\pi i}{380928}\sum_{j=0}^8
(-1)^j[P(-D)\phi_{8-j}](\mu)\phi_j(t).}
\tag{D24}
\]

D24 保留了整个 ordinary-point comparison 的9个 derivatives；它们是指定周期的具体值，不自动是Q常数，也没有被某一个 ζ5 关系支付。更改去 μ 的路径相应 conjugate 这个 vector，不能忽略路径而把它称为一个有理 Betti column。

**D12（真实函数秩和 module 秩分开）。** Fu 不可能为 rational function：若在 μ 有 pole h≥1，L Fu 的 leading pole为 h+9≥10；若在 μ analytic，L Fu analytic。两种情形都与 D20 的 pole5冲突。故

\[
\boxed{\operatorname{rank}_{\mathbb Q(t)}\{1,F_u\}=2.}
\tag{D25}
\]

R5 非零，(D−D R5/R5)L 是实际 order10 homogeneous annihilator。D22 的非零 χ5 属 irreducible rank9 的 L-solution space；它的 monodromy orbit 张成全部9维。B5 的 continuations 的 span 包含 χ5 和其全 orbit，另有 L B5≠0 的 B5 自身，因此维数10。每个 rational-coefficient scalar annihilator 的 solution space 必包含这个 orbit，阶数至少10。因此 B5 和 Fu 的 minimal homogeneous order 恰10 over C(t)，从而 over Q(t)。

这说明是一个不 split 的 rational differential extension，非 polynomial forcing 的 D10 情形；也意味着 {1,Fu,DFu,…,D8Fu} 没有 order≤9 的 rational homogeneous relation。这里可严证 full-jet rank10：若 r*+Σ_{j=0}8 r_jD^jFu=0，则 monodromy difference annihilate χ5，由 irreducibility 会 annihilate L 全solution；但 operator阶≤8，只能全r_j=0，再r*=0。仅选择 pair 时 rank仍是2，不拿 minimal order10冒充 pair的函数rank。所有这些不等同于已证 integral/motivic/admissible higher normal function。

## 5. 实际逆系数的全部有限处分母：从 D_(5n) 收紧到 D_n

**D13（所有 n、m 和 prime 的单层估计）。** 设 D_n=lcm(1,…,n)。对1≤m≤n、任意 prime p，Legendre 写成 q=p^k 的 carry layers：

\[
v_p(h_s)=\sum_{k\ge1}C_q(s),\quad
C_q(s)=5\lfloor2\{s/q\}\rfloor+\lfloor5\{s/q\}\rfloor\in[0,9].
\tag{D26}
\]

因此 h_n/(m9h_m) 在 q 层的 contribution 是 C_q(n)−C_q(m)−9·1_(q|m)。若 q≤n：q不整除m时最小−9；q整除m时 C_q(m)=0，仍最小−9。若 q>n≥m：两数都小于q，函数5floor(2s/q)+floor(5s/q) 随 s单调，且q不整除m，因此 contribution≥0。这完整支付包括2、5的所有 primes，给

\[
\boxed{v_p\!\left(\frac{h_n}{m^9h_m}\right)
\ge-9\lfloor\log_pn\rfloor.}
\tag{D27}
\]

不能把 m9 和 h_m 的两个最差 bounds相加成18；q|m 时 carry恰0正是改善原因。该 D_n9 sharpening 由 root 首先提出，本稿独立纸面核查。

**D14（实际 lift cap）。** 因 P(m)、a 均整数，D9/D16/D27 直接给

\[
\boxed{380928D_n^9[t^n]B_5\in\mathbb Z\quad(n\ge1).}
\tag{D28}
\]

若 u=A/M∈Q，M>0，则380928 M D_n9[t^n]Fu整。n0的−u也由同一fixed倍数支付，所有有限 exceptions不另藏；D_n9不含随n的dyadic exponential，因为选用同一个integer t coordinate且 a=−2^20 已是整数。若另改coordinate，必须同时支付所有singular位置、Taylor整性和archimedean scale。

**D15（CDT pair 的准确 paid array）。** 对 fixed multiplier后的{1,Fu}，可用九个 columns (0,1)^t、e=(0,0)，所以 σ=(0,9)、τsharp0。固定 CDT v2 Definition6.0.1、Theorem6.0.2 给

\[
\boxed{\tau^\flat=\frac{3\cdot9}{4}=\frac{27}{4}.}
\tag{D29}
\]

Fu holonomic；因此 Cor6.0.14 可用 |φ'(0)|>exp(27/4)，不须粗门槛exp9。仍须 φ:(D,0)→(C_t,0) 本身 holomorphic、Fu∘φ 实际 meromorphic，并按原boundary/integrability/limiting假设支付

\[
J(\phi)=\iint_{\mathbb T^2}\log\max(|\phi(z)|,|\phi(w)|)d\mu_H(z)d\mu_H(w),
\quad 2\le\frac{J(\phi)}{\log|\phi'(0)|-27/4}.
\tag{D30}
\]

D29 是一个明确 safe upper cap，不声称是最小费用。full-jet array需另算，不能把pair27/4直接付给10个functions。本轮 root 独立的 reference-gate manuscript处理 full-jet array与同叶对照，待正式独审后的收据/总报告另连接；本稿不提前引用其未收审 theorem。

## 6. 具体收益与尚缺的可审查方程

**D16（此次确实补上的缺口）。** D8 给出了原 Γ系统此前缺失的 exact reflection column。D16–D18 是一个具体、有理起点、唯一 particular 的 relative lift，其完整 conifold jump coefficient 确为已知ζ5；有理性假设真实改变leaf。D24 支付新增pole的所有9个jump分量，D25/后续证明支付实际functionrank与wholeextensionrank，D28支付全primecap。这比普通endpoint−u或η-package改basis多出实质connection信息。

**D17（没有闭合的数值定理）。** 该构造作为 ζ5 已知 analytic identity 的校准，并非新的 ζ5 irrationality proof。κ5/κ7 实际需要 D14 的另一条 inverse-hypergeometric identity；本稿没有给出。原 ξ=αζ4+βζ5 如要提升，须为两项同时构造 rational forcing、完整pole jumps、同一leaf和allprimecap，而不是把α项直接删掉。更重要的是 μ 的log branch不可被ζ5=u取消；后续CDT余量必须支付它。κ作为Γclass出现也不提供新的irrationality本身。

本模型允许的 holomorphic maps可能在更大的 Riemann leaf上；不能从“omit单点μ”直接援引单叶Koebe给所有maps的derivative上界。D19只是明确合法leaf，D30仍是待比较的真实判据。root研究其同叶reference obstruction；若对本paidarray形成排除，它应只限此cap/functionpackage，不扩大为一切period/normal-function方法no-go。

## 7. Primary 文献核查与实际本轮读域

以下是本人本轮实际读域，不继承冻结稿或同行读页。本稿使用的本轮共享新增 Laporte–Walcher primary 由 /root/masked_racah_finalize 正常TLS归档，避免重复；本分支没有重复下载任何PDF。

- Bloch–Vlasenko v2，[Gamma functions, monodromy and Frobenius constants](https://arxiv.org/pdf/1908.07501v2)：已有 `literature/cdt_gamma_connection_sources_20261007/bloch_vlasenko2020_gamma_frobenius_arxiv1908_07501v2.pdf`，本人本轮实际 FULL PDF24–26，3页。用于 adjoint/concomitant和Frobenius extension接口；Proposition26的实际已付Γ行直接依赖全文重读的冻结G4–G7，不冒称本轮重新读其15–20页。
- Kerr2026 v1，[Three vignettes on hypergeometric normal functions](https://arxiv.org/pdf/2602.04128v1)：既有 `literature/cdt_period_extension_sources_20261007/kerr2026_three_vignettes_arxiv2602_04128v1.pdf`，本轮FULL PDF1–2、8–9，共4页。几何背景的Hodge/cycle假设保留；不拿其有条件的一般ζ理论代替D15的analytic校准。
- Au v4，[Wilf–Zeilberger seeds and non-trivial hypergeometric identities](https://arxiv.org/pdf/2312.14051v4)：既有 `literature/cdt_period_extension_sources_20261007/au2024_wilf_zeilberger_seeds_arxiv2312_14051v4.pdf`，本轮FULL PDF1–2、19、25–26，共5页。PDF26的乱码提取后实际目读既有 `research/cdt_period_extension_reading_20261007/au_pdf26.png`；没有执行WZ notebook，不声称独立重验其整篇proof机器代码。
- Laporte–Walcher v2，[Monodromy of an Inhomogeneous Picard-Fuchs Equation](https://arxiv.org/pdf/1206.1787v2)：本轮共享新增 `literature/cdt_gamma_relative_chain_sources_20261007/laporte_walcher2012_inhomogeneous_picard_fuchs_arxiv1206_1787v2.pdf`，10页；/root/masked_racah_finalize 正常TLS归档，本人本轮FULL PDF1–9，共9页。其6–8页明确区别完整jump vector、comparison matrix和local analytic solution；7、9页给数值continuation/recognition，不能把其regulator constant recognition称为一般已证解析公式。本文D23–D24自行纸证，不套该quintic的integral lattice到当前rank9。
- CDT固定v2，已有 `literature/cdt2024_l2_chi_minus3.pdf`，本人本轮FULL PDF66–69，共4页，实际核Definition6.0.1、Theorem6.0.2、Cor6.0.14的m、σ、τ、holonomic与holomorphic-map条件。

本稿本人 distinct primary PDF页数共 **25**；不是整个BV43/Kerr25/Au30/Laporte10/CDT218页全读。网络仅primary查询/读取，未关TLS验证；新增归档owner页数不当个人读数。正式独审、作者最终FULL回读和单向FINAL来源收据随后完成；旧588记录不变。本轮仍无新数值无理性/LI/Lean结论。
