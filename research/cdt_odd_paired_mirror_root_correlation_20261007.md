# 真实镜像选择与根分母的相关性：新增全尺度衰减与约束势能

日期：2026-10-07，NEW，作者 `/root/scaled_root_finalize`。本轮开始时529冻结记录及 last delivery SHA `75205f58e3cce6660828b8ad28e27f13a4a1f978805b22cd97c1d9e69ae674f1` 保持只读。原 B6/κ3/s5、degree<3n、rank2n、原饱和整数值格 S 与 whole-X D_A(X) 保持不动。唯一 NEW guarded FIRST1 在 root 完整静态预审与具体授权后运行一次，exit0 PASS；没有旧/同行执行/import/rerun，没有辅助素数扩表。本文仍待实际全文独审和最终来源收据。

## C1. 不丢掉实际镜像 q 分母

实际完整回读冻结 [mirror 稿](cdt_odd_paired_mirror_choice_energy_20261006.md) M1–M23 及其独审、[coupled Gram 稿](cdt_odd_paired_coupled_gram_decay_20261007.md) C1–C23。沿用其原格和真实轮廓。c_n=2n+1/2、N=floor(n/2)，镜像 pair {m,m'} 中 m'=2n+1−m，实际距离

\[
\delta_R=m-1/2=nt_m,\quad
\delta_L=2n+1/2-m=n(2-t_m),\quad t_m=(m-1/2)/n.
\tag{C1}
\]

若某 pair 选择左 head m，δ 大；选择右 head m'，δ 小。用一固定有限正原子概率测度 ρ=Σω_iδ_(s_i)、s_i>0，选整数 N_i≥0、ΣN_i=N、N_i/N=ω_i+O(1/n)，取

\[
q_{n,\rho}(z)=\prod_i((z-c_n)^2+n^2s_i)^{N_i},
\quad L_\rho(x)=\sum_i\omega_i\log(s_i+x^2),
\quad I_\rho=\int_0^1L_\rho(t)\,dt.
\tag{C2}
\]

degree(q)=2N≤n；全部实际 head 上 q>0。沿原高列的 determinant1 剪切保持 D_A(X) 对所有 X 完全相同，故原整化费用继续适用；不把新列声称为免费整基。此前 coupled C9 的准确有限 n 界是

\[
|D_A(\xi)|\le\frac{Z_{H,n}A_n(q)^n}{F_n^2\Gamma_n^2}
\left(\sum_{a\in\mathcal A_n}
\prod_m\frac{|\widetilde\kappa_{a_m}|}{q(a_m)}
\sqrt{\mathcal H_n(a)}\right)^2.
\tag{C3}
\]

ξ=aζ(4)+bζ(5)、b≠0；只有假设 ξ 为有理，才能把轮廓值与对应有理 input 的 D_A 值识别。Z_H、F、Γ、κ̃ 和 Hardy determinant 全保持真实原对象。

此前 root 分布稿用 δ_choice≥nt_m，把每个 choice 的分母统一下界为全小距离的值。本文保留选择左 head 时多出的全部费用。定义

\[
\Psi_\rho(t)=L_\rho(2-t)-L_\rho(t)>0\quad(0\le t<1),
\quad R_\rho(\tau)=\int_{1-\tau}^1\Psi_\rho(t)dt.
\tag{C4}
\]

每个 log(s+(2−t)²)−log(s+t²) 严格递减，故 Ψ 严减、Ψ(1)=0；R 连续、R(0)=0、R(τ)>0 对 τ>0。若 k 个 pairs 选左 head、τ=k/n，则从 C1–C2 精确有

\[
2\sum_m\log q(a_m)
=4Nn\log n+2N\sum_mL_{\rho_n}(t_m)
+2N\sum_{m:\,a_m=m}\Psi_{\rho_n}(t_m),
\tag{C5}
\]

其中 ρ_n=Σ(N_i/N)δ_(s_i)，N>0 时定义；n=1 单独有限处理。因为 Ψ 递减，最后 k 项的和对任意实际选择 ≥Σ_(m=n−k+1)^n Ψ(t_m)。midpoint sums 的误差 O(1) 对所有 k uniform，因固定 s_i>0 使 Ψ 在 [0,1] 光滑。故

\[
2\sum_m\log q(a_m)
\ge4Nn\log n+2NnI_\rho+n^2R_\rho(\tau)-O(n).
\tag{C6}
\]

这里奇数 n 的 2N/n=1−1/n 与舍入 ρ_n 的 O(1/n) 误差全部乘回后只付 O(n)；不是把奇数免费当偶数。C6 是逐选择真实分母的全 n bound，没有假设两镜像 q 相同。

## C2. 同一个选择比例同时支付 κ、Hardy 与 q

冻结 mirror M6–M16 已给：对相同 k/τ 的任何实际选择，

\[
\log\left(\prod_m\widetilde\kappa_{a_m}^{\,2}\mathcal H_n(a)\right)
\le2\sum_{j=n+1}^{2n}\log\widetilde\kappa_j
-n^2[c(\tau)+P(\tau)]+O(n\log(n+2)),
\tag{C7}
\]

误差 uniform in k。P 是 κ 的真实镜像损失，c 来自同 k 的实际排序 Hardy ratios。不能让三个不同的 k 分别取各项最优。

为明确数值输入，令 f(z)=z²log z/2−3z²/4，f(0)=0、f'(z)=zlog z−z、f'(0)=0，沿用

\[
c_{LL}(\tau)=f(2-\tau)-4f(1)+3f(\tau)+2(1-\tau)f'(\tau),
\]
\[
c_{HH}(\tau)=f(3+\tau)-2f(3)+f(3-\tau)-2f(1)
+2f(1-\tau)+2\tau f'(1-\tau),
\]
\[
c_{LH}(\tau)=2[f(3-\tau)-2f(2)-f(3-2\tau)
+2f(2-\tau)+f(1+\tau)-f(1)],\quad c=c_{LL}+c_{HH}+c_{LH},
\]
\[
P(\tau)=2[f(7+\tau)+f(7-\tau)-2f(7)
-f(1+\tau)-f(1-\tau)+2f(1)].
\tag{C8}
\]

定义真正共同的下界

\[
d_\rho=\min_{0\le\tau\le1}[c(\tau)+P(\tau)+R_\rho(\tau)].
\tag{C9}
\]

C6–C7 给每个 choice 的准确 fee upper；2^n 个正项的 sum 再平方只付 O(n)。因此 C3 的低块 choice 正和满足

\[
\log T_{n,q}\le2\sum_{j=n+1}^{2n}\log\widetilde\kappa_j
-4Nn\log n-2NnI_\rho-d_\rho n^2+O(n\log(n+2)).
\tag{C10}
\]

**严格改进定理。** 对任何固定有限正根分布 ρ，都有 d_ρ>c_*，其中 c_*=min(c+P) 是冻结 mirror 的已证常数。

证明：各项连续、min 取得，且 R_ρ≥0，故 d_ρ≥c_*。若相等，某 minimizer 必同时满足 c+P=c_*、R=0；C4 迫 τ=0。但 c(0)+P(0)=2log2>1.386，而冻结 saved upper c_*≤0.845115370，矛盾。故严格大于。这个结果已经是全尺度严格加强，不依赖有限采样或新数值执行。它不给无限非零或足够大 margin。

## C3. 显式有理根 4/7 的额外有理信用

固定 s>0、ρ=δ_s，置 u=1−t∈[0,1]。逐项准确

\[
\Psi_s(1-u)=\log\frac{s+(1+u)^2}{s+(1-u)^2}
=2\operatorname{artanh}\frac{2u}{s+1+u^2}
\ge\frac{4u}{s+1+u^2}\ge\frac{4u}{s+2}.
\]

argument<1 来自 s+(1−u)²>0；atanh z≥z 对 0≤z<1 可直接积分 1/(1−z²)≥1 证明。因此

\[
\boxed{R_s(\tau)\ge\frac{2\tau^2}{s+2},\qquad
R_{4/7}(\tau)\ge\frac79\tau^2.}
\tag{C11}
\]

这项与 actual κ/Hardy 仍使用同 τ。NEW 一次证书完整覆盖4096闭区间，以 exact Fraction logarithm remainder 与 signed intervals 证明

\[
d_{4/7}\ge\min_{\tau\in[0,1]}[c(\tau)+P(\tau)+7\tau^2/9]
\ge0.869976088933>43/50.
\tag{C12}
\]

保存的 surrogate 最小值区间为 [869976088933,872133454193]/10¹²，minimum lower cell734。其 upper 是 surrogate 的 sample upper，只用于括住 surrogate min；**不是 actual d_(4/7) 的 upper**，因为真实 R 通常更大。没有把较弱 quadratic penalty 的最优值当真实 correlated optimum。

## C4. 全 n 合回解析包络，只支付一次

令

\[
M_\rho=\sup_y[Q(y)+\sum_i\omega_i\log|s_i-y^2|],\quad
\varepsilon_\rho=M_0-M_\rho+I_\rho.
\tag{C13}
\]

此前已证根分布全尺度 transfer 给

\[
\log A_n(q)\le(4n+4N+C)\log n
+n[(1-2N/n)M_0+(2N/n)M_\rho]+O(1).
\]

舍入权重误差为 O(1/n)，maxima 一致远离正权根的 log poles 及无穷尾部；固定 polynomial prefactor 被统一指数尾部吸收。C10 的 −4Nnlog n 与 nlog A 的对应项准确抵消，I_ρ 与 M_ρ 共同组成同一 ε_ρ。于是旧 high Gram、factorial、Γ 及 baseline 常数全部仍只支付一次，得

\[
\boxed{\log|D_{A,n}(\xi)|\le
-[\beta_0+\tfrac12\log2+d_\rho+\varepsilon_\rho]n^2
-2\log\Gamma_n+O(n\log(n+2)).}
\tag{C14}
\]

这把冻结 mirror formula 的 c_* 替换为同选择计费的 d_ρ。没有从两个不同 choice 的 κ 与 q 收益拼接；P 与 R 的两项各自的最小损失虽均由末 k pairs 实现，C7 的 Hardy bound 对所有同 k choices 都有效，故三项可合法共同相加。

固定 s=4/7，此前 source/result 均冻结的 [scaled-root 稿](cdt_odd_paired_scaled_root_optimum_20261007.md) S10–S18 给 ε_(4/7)>3/5；未重跑该证书。冻结 β0≥7.90523839512558、log2>0.693、liminf n⁻²logΓ≥1.455845。本文对外采用只取 d>43/50 的保守界；C12–C14 因此给

\[
\boxed{\limsup_{n\to\infty}n^{-2}\log|D_{A,n}(\xi)|
<-12.62342839512558.}
\tag{C15}
\]

新 d 的保存下端还给 <−12.63340448405858；若再取此前已保存的全轴下端 ε≥0.611819519300，则可得 <−12.64522400335858。这些只是同一个 C14 的不同保守程度，不以它们重复收费；本轮明确报告的主界为 C15。strict 符号至少由 log2>0.693 提供。log0=−∞，未除 actual determinant。

safe signed rational normalization scale 约40.314517426059346 与这些已证 rates 仍未给 strict margin；safe upper scale 不是 actual minimal denominator 的下界。本文没有 actual M5 单位、infinite nonzero、固定有理 source 无限成功或新数值无理性/LI 定理。此前粗 root-V 的信用上界<123/34也只针对舍弃 mirror gap 的特定 functional，不可拿来否定本相关性或 actual Schur/phase。

## C5. 正 choice 和的准确 joint 变分极限

令

\[
h(t)=(6+t)\log(6+t)-2t\log t-(2-t)\log(2-t)-6\log6+2,
\]
\[
\mathcal C=\{p(x)dx:0\le p\le1,\ p(x)+p(2-x)=1\text{ a.e. on }[0,2]\},
\quad K(x,y)=\log\left|\frac{x-y}{x+y}\right|,
\]
\[
\Phi_\rho(p)=2\int_0^2h(2-x)p(x)dx
+\iint K(x,y)p(x)p(y)dxdy
-\int_0^2L_\rho(x)p(x)dx.
\tag{C16}
\]

若 T_(n,q) 是 C3 中 q 分母保留的真实正选择和平方，则

\[
\boxed{\lim_{n\to\infty}\left[n^{-2}\log T_{n,q}
+(4+4N/n)\log n\right]
=\max_{p\in\mathcal C}\Phi_\rho(p).}
\tag{C17}
\]

证明从冻结 mirror M19 的完整 argument 加一个有界连续线性项即可，但明确核新增 fee：C2 在每个 selected δ=nx 上准确给 log q(a)=2Nlog n+N L_(ρ_n)(x)；平方后的总代价是 4Nnlog n+2Nn∫L_(ρ_n)dλ_n，2N/n→1、L_(ρ_n)→L_ρ uniformly on[0,2]。所以归一化和 C16 的系数准确。

selection empirical λ_n 的任何弱极限属于 C；原 spacing bound 控制 K 的 diagonal/原点 log tail，新增 L 无奇点，故同一 compactness 给 upper。floor-prefix binary mirror recovery 给任意 p 的 lower，并保留新增连续项。2^n 正项 logsum 与最大log项差 O(n)。因此 C17 是所定义正和的 equality，不是 original complex determinant 的 equality，也不是 artificial weighted-Gram supremum 的 equality。

K 严格负定的 frozen square-kernel proof 仍成立，linear L 不改变 strict concavity；故 Φ_ρ 有唯一 maximizer p_ρ。其准确 first variation 在0<x<1为

\[
g_\rho(x)=h(2-x)-h(x)+\tfrac12\Psi_\rho(x)
+\int_0^2[K(x,y)-K(2-x,y)]p_\rho(y)dy.
\tag{C18}
\]

a.e. p=0处 g≤0，p=1处 g≥0，0<p<1处 g=0；这在当前 box/mirror constraints 下由 concavity 也是充分条件。C18 同时含真实 κ、Hardy interaction 和 root head term，提供比单独 minimax root-V 更准确的下一研究目标。

C10 还给此 exact value 一个已经支付的严格 upper：

\[
\max_{p\in\mathcal C}\Phi_\rho(p)
\le2\int_1^2h(t)dt-I_\rho-d_\rho.
\tag{C19}
\]

所以本接口已有 C12 的可认证收益，不只是待解的定义。

## C6. exact joint 优化也严格优于先拆开两项

写 Φ_0 为 C16 不含 L 的 frozen functional，p_sm=1_[0,1]。mirror condition 给

\[
\int_0^2L_\rho p-I_\rho
=\int_0^1[1-p(t)]\Psi_\rho(t)dt\ge0,
\tag{C20}
\]

等号唯一在 p=p_sm（a.e.）。因此 max Φ_ρ≤max Φ_0−I_ρ。以下证明此号实际严格，防止把形式耦合当未证的严格收益。

首先 p_sm 不是 Φ_0 的 maximizer。记

\[
J(x)=\int_0^1K(x,y)dy
=2x\log x+(1-x)\log|1-x|-(1+x)\log(1+x).
\]

其 Φ_0 first-variation g_sm(x)=h(2−x)−h(x)+J(x)−J(2−x)。置 x=1−u、u→0+，令 B(t)=(6+t)log(6+t)−tlog t−6log6，则

\[
h(1+u)-h(1-u)=B(1+u)-B(1-u)=2u\log7+O(u^3),
\]
\[
J(1-u)-J(1+u)=2u[\log u+\log2-1]+O(u^3),
\]
\[
g_{\rm sm}(1-u)=2u[\log u+\log14-1]+O(u^3)<0
\quad\text{for sufficiently small }u>0.
\tag{C21}
\]

这违反 p=1 处必须 g≥0；也可直接在这段低半区减去小正量、反射半区加上，得到可行正的一阶收益。故 p_sm 不是 Φ_0 的唯一 maximizer。若 max Φ_ρ=max Φ_0−I_ρ，某 attained maximizing p 必同时最大化 Φ_0 且在 C20 等号，迫 p=p_sm，矛盾。因此

\[
\boxed{\max\Phi_\rho<\max\Phi_0-I_\rho.}
\tag{C22}
\]

这给每个固定有限正根分布的真实正 choice 和严格 correlated credit；此号的数值大小尚未求解。并且 Ψ_ρ(1−u)=O(u)，故在 Φ_ρ 中给 g_sm 加半个 Ψ 后 C21 的 ulog u 仍主导为负：各个 correlated maximizer p_ρ 也必有正的高半区质量，不能把最优 choice 免费假定为全小距离。

## C7. 唯一首次证书及其准确范围

NEW [source](cdt_odd_paired_mirror_root_correlation_20261007_certify.py) SHA256 `f873b6ea944f0dbb7fe4aafbf8f56d33bf9083a50ef21defc256c75a70bcee42`，由作者和 root 在执行前实际完整静态读取；root 此后具体授权这份 source 恰一次 FIRST1。author 持有 exec session70064，轮询同一 handle 得 terminal exit0 PASS，没有超时重启。source/result/guard 此后冻结。

[result](cdt_odd_paired_mirror_root_correlation_20261007_certify.json) SHA256 `d16792233e987d3777e75cc90b23d2509ee67d4ed2ba03732734422e715b8486`。本人解析完整 JSON，实际读全部 metadata/limitations 和 cells0,1,733,734,735,4094,4095的完整有理区间；没有声称4096条逐条手工读或重新生成。全下界来自完整源码的覆盖论证和唯一执行保存结果，不来自这些选读 cells。

[guard](cdt_odd_paired_mirror_root_correlation_20261007_certify_guard.json) SHA256 `a8a55e407cea1a95cf34f4c08625237205260fbbed908544cfe9b5d64fe6fd77`，exclusive-create、STARTED_FIRST1、rerun_forbidden true；开始历史标签不改为 PASS，成功状态从 result 取得。

源码只 import stdlib，不读取旧/同行 source 或 certificate。log 用24项 positive atanh series，power-of-two reduction 后 x∈[1,2]，余项上界 2z^49/[49(1−z²)]。f、f' 在[0,1]单调减，含0连续值；f' 在[1,4]单调增，因此取其 cell 两端 enclosure 的最大绝对值作 Lipschitz bound，以 midpoint±Lhalfwidth 覆盖整个 f image。P 单调、非负，用完整 cell 的 endpoints；7τ²/9亦单调。所有 signed products 用四角，interval依赖只使 bounds 变宽。

4096个闭区间覆盖全部[0,1]，每个 cell 用整个 lower 而非 sample；minimum lower 的 saved rational floor 给 C12。sample1469/8192只给 surrogate minimum upper。程序不认证 C5–C7 的 all-n bridge、C11 的 atanh 理论、C17 的变分极限、C21–C22 的严格拆分差，也不检验实际 determinant nonzero。这些由纸面证明负责。新增执行1、成功1、失败0、rerun0、旧/同行 execute/import0、prime extension0、Lean0。

## C8. 新一手文献、实际读域与继续问题

本轮先检查 literature 中没有 Dragnev/Saff constrained-energy 原件，再搜索一手来源，保存 Dragnev–Saff, *Constrained energy problems with applications to orthogonal polynomials of a discrete variable*, Journal d'Analyse Mathématique72(1997),223–259：[canonical 作者原件](https://math.vanderbilt.edu/saffeb/texts/168.pdf)/[本地PDF](../literature/cdt_paired_mirror_root_sources_20261007/dragnev_saff1997_constrained_energy_author_168.pdf)。37页、4248097 bytes，SHA256 `29c3c2b7d8595306addf83296980836c23be2e457daa60bfb43dd1c831d135ac`。

实际完整提取阅读 PDF1–5共5 distinct页；PDF5 另 render并目视核 Theorem2.1 的 inequality directions。PDF3 的 admissible upper constraint、PDF4–5 的 Theorem2.1 提供 existence/uniqueness 与 saturated/unsaturated potential conditions。没有称37页全文读完。www 作者URL下载先遇普通 TLS hostname mismatch，无文件；随后 canonical non-www host 使用普通 certificate verification 成功，未关闭检查或 bypass。两个 web open 原件失败，不冒称 web full-PDF 阅读；本地原件正常可读。

该论文处理普通 logarithmic energy 与 μ≤σ 上界。本项目还有 mirror equality，kernel K 含 reflected image 项，是相应 Green/condenser 能量结构。不能直接套其 Theorem2.1 来求本项目最优密度或证明 D_A 非零；C17–C22 的 compactness、negative-definiteness 与 first variation 在实际模型自证。文献提示继续研究受约束势能的 active regions，本文保留实际镜像相关性后才有正确外场。

本轮具体推进：同 τ 的三项全 n 支付、每个固定 root 分布严格加强、显式4/7新增有理信用与 C15更强 rate、正 choice 和的 exact joint limit/unique optimizer及严格优于先拆开的定理。仍须解实际 correlated equilibrium、更强 exact Schur/complex phase、足够同对象算术余量和无限 actual nonzero，才可能得到请求的特殊值数论结论。
