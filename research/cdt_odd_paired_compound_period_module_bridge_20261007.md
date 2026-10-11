# 实际部分外幂的周期函数接口：精确独立秩、全素数分母与单值叶门槛

2026-10-07，NEW，source_pencil_finalize。authority 为 main §§161–165 与 delivery_partial_global f72fe28c 快照；556 冻结记录（551 数学、5 guard）只读。本文纯纸证，不创建、执行、import 或 rerun 数学 producer，不扩素数表。保留原 B6/k3/s5、完整 S、degree<3n 和同一固定有理源 ξ=αζ(4)+βζ(5)，β≠0。

新结论是一个真正的函数/周期接口及其必要算术费用：实际 compound 的 polynomial coefficient rank 精确给一种规范真实函数提升的独立秩；每个非恒定 polynomial row 有严格的素数分母见证。二次及更高 polynomial rows 的这个见证还避开 coefficient-index N^e 的清分母作用。因此，规范提升在标准割线叶上无法凭增加 minors 得到大秩 CDT 矛盾。范围限于本文的明确提升和叶，不是所有奇 ζ 或所有 holonomy 方法的 no-go。

## 1. 固定真实对象与两种秩

本轮实际全文读取冻结 [partial P1–P14](cdt_odd_paired_partial_compound_transfer_20261007.md)、[CDT mechanism 全稿](period_holonomy_cdt_mechanism_20261005.md)、[target projection 全稿](period_holonomy_target_projection_20261005.md)。target 首次合并输出中段截断后，已逐段补读整个文件，未把截断当全文。

令 m=2n，B_n(T) 为原完整整数 basis 的真实配对矩阵。冻结 P1 给它的 entries 在 T 上 affine。对 1≤d≤m，把同一 compound C_d(B_n(T)) 的全部 minors 依次记为

\[
Q_a(T)=\det B_n(T)_{I_a,J_a}\in\mathbf Q[T],\qquad
\deg Q_a\le d.
\tag{B1}
\]

固定 n、d、α、β 后，定义

\[
V_{n,d}=\operatorname{span}_{\mathbf Q}\{Q_a(T)\},\qquad
q=\dim_{\mathbf Q}V_{n,d}
=\operatorname{rank}_{\mathbf Q}[\,[T^j]Q_a\,]_{a,0\le j\le d}\le d+1.
\tag{B2}
\]

这个 q 与 rank B_n(c)、rank C_d(B_n(c)) 是不同的数学对象。冻结 P7 已证明：对每个固定有理 α、β,c，β≠0，无限 n=4r 上 rank B_n(c)≥6r，故 d=6r 时至少一个 Q_a(c)≠0，从而 q≥1。它尚不提供 q≥6r。所有这些 n 保持同一固定源；本文没有换成 ζ(7)、Catalan 或每个 prime 选择新源。

本文的 Taylor coefficient index 用 N；它与固定的矩阵参数 n 无关。以下素数分母证明均先固定 n、d、具体 polynomial、其 degree 及 q，再让 p、N 增长。

## 2. 规范的真实周期提升及精确函数秩

定义真正的 holomorphic germ

\[
\Xi(x)=\alpha\operatorname{Li}_4(x)+\beta\operatorname{Li}_5(x)
=\sum_{N\ge1}\frac{\alpha N+\beta}{N^5}x^N.
\tag{B3}
\]

在主支 D=\mathbf C\setminus[1,\infty) 上取从 0 延拓的这个函数。因为两个级数在 x=1 绝对收敛，对实 x↑1 有 Ξ(x)→ξ。于是

\[
\mathcal E:Q(T)\longmapsto Q(\Xi(x)),\qquad
\lim_{x\uparrow1}\mathcal E(Q)(x)=Q(\xi).
\tag{B4}
\]

这是保留真实 endpoint period 的一种规范提升。它不是由 Gram 轮廓自动产生的唯一 Gauss–Manin 系统；我们明确选择它并逐项证明其性质。

置 L_s=Li_s(x)，θ=x∂_x，则 θL_s=L_(s−1)，L_0=x/(1−x)。对给定 d，所有 L_1,…,L_5 的 total degree≤d 的 monomials 在 θ 下生成一个有限维 Q(x)-空间，维数至多 binom(d+5,5)。因为 θL_1 是有理函数，求导不会增加 total degree。这直接证明每个 Q(Ξ) 是 holonomic。这里仅用一个 finite connection 的上界，不把这个上界当作所列 functions 的独立秩。

在 (0,1) 上选一个 basepoint，绕 1 逆时针一周而不绕 0。由 Li_1=−log(1−x)、θLi_s=Li_(s−1)，以及 s≥2 的 monodromy 在 x→1 时趋零，得到

\[
\Delta_1\operatorname{Li}_s(x)
=-2\pi i\frac{(\log x)^{s-1}}{(s-1)!},
\quad
v(x):=\Delta_1\Xi(x)
=-2\pi i\left(\alpha\frac{\log^3x}{3!}
+\beta\frac{\log^4x}{4!}\right)\not\equiv0.
\tag{B5}
\]

该 loop 下 log x 保持原支，v 不变，所以第 k 次 continuation 为 Ξ+kv，k∈Z。若 Σ_(j=0)^d a_j(x)Ξ^j=0，a_j∈C(x)，对所有 k continuation 给一个在 k 上恒零的 polynomial；其最高系数为 a_d v^d。先消去最高项再下降，可得所有 a_j=0。因此

\[
1,\Xi,\ldots,\Xi^d\text{ 在 }\mathbf C(x)\text{ 上线性无关};
\qquad
\boxed{\dim_{\mathbf Q(x)}\operatorname{span}\{Q_a(\Xi)\}=q.}
\tag{B6}
\]

最后一个等式来自 (B2) 的有理 coefficient matrix；其 rank 在扩域 Q→Q(x) 后不变。给定实际 polynomial coefficient matrix，q 是这一提升的完整、可用的函数秩，而无需猜测任何未知 period 的 algebraic independence。

若假设 ξ=c∈Q，endpoint evaluation V_(n,d)→Q 的 rank 在至少一个 Q_a(c)≠0 时恰为 1；其 kernel 是 V_(n,d)∩(T−c)Q[T]。这不会改变 (B6) 的函数秩，也不会自动使函数过收敛。矩阵非零与函数独立性因此已经接到明确的、互不混淆的映射。

## 3. 全素数的原源分母，以及 polynomial rows 的精确见证

先证明实际 Ξ 的完整 prefix denominator。取正整数 H，使 A=Hα、B=Hβ∈Z，B≠0；记 L_N=lcm(1,…,N)，δ_f(N) 为 f 的前 N 个 coefficients 的最小正共同分母。

对 p∤B，a=floor(log_pN)，在 index p^a 处 HΞ 的 coefficient (Ap^a+B)/p^(5a) 有 valuation −5a，全部前 N coefficients 又皆≥−5a。因此 v_pδ_(HΞ)(N)=5a。对 p|B，令 b=v_pB。若 a+v_pA>b（A=0 时作∞），这个 coefficient 的 valuation 是 b−5a；其余情况 a≤b，故分母 exponent 与 5a 的差至多 5b。结合 δ_(HΞ)|δ_Ξ|Hδ_(HΞ)，严格有

\[
\frac{L_N^5}{|B|^5}\le\delta_\Xi(N)\le H L_N^5,
\quad
\log\delta_\Xi(N)=5\log L_N+O_{\alpha,\beta}(1)
=5N+o(N).
\tag{B7}
\]

最后一步采用经典 prime number theorem log L_N=N+o(N)；没有新素数实验。这里是一个真实 all-prime prefix 结论，固定清分母常数明确保留。

令 Q(T)∈Q[T] 固定、degree j≥1、leading coefficient a_j≠0。除掉源、Q 的 coefficients、a_j 和固定 scaling 的有限 primes。对 p>j，所有 1≤k≤jp 都小于 p²，所以 Ξ 的第 k coefficient 在 p|k 时恰为 valuation −5，否则 p-integral。在 [x^(jp)]Ξ^j 的 convolution 中，达到 j 个 p-divisible indices 的唯一 composition 为 (p,…,p)；其余 terms 至多 j−1 个这种 indices。低次数 Ξ^ℓ，ℓ<j，同样至多 ℓ 个。因此

\[
\boxed{v_p[x^{jp}]Q(\Xi)=-5j.}
\tag{B8}
\]

没有用数值近似或 coefficient 试算。B8 给具体 prime witness，不声称它已经确定所有 product rows 的最优 denominator type。安全上界亦完整：若 Q degree j，固定一次 clearing multiplier 后，前 N coefficients 的 denominator 都整除 L_N^(5j)，因为每个 convolution index≤N。

还能避开 coefficient-index N^e。令 t_0 为 Ξ 的首个非零 Taylor index。由 (B3)，α+β≠0 时 t_0=1；否则 α=−β≠0，第二 coefficient=−β/32，故 t_0=2。对固定 j≥2，取

\[
N_p=(j-1)p+t_0,
\quad p>\max(j,t_0),\quad
p\text{ 另避 }j\text{ 及 }[x^{t_0}]\Xi\text{ 的固定 primes}.
\tag{B9}
\]

此时 N_p<jp<p² 且 p∤N_p。最高 j 次 convolution 中，达到 j−1 个 p-divisible indices 的非零 compositions 必须是 (p,…,p,t_0) 的 j 个排列：p-divisible positive indices 至少为 p，而剩余非零 index 至少 t_0，已耗尽 N_p。其和为 j([x^p]Ξ)^(j−1)[x^(t_0)]Ξ，valuation 恰 −5(j−1)。其他最高次数 terms 至多 j−2 个 p-divisible indices；低次数 ℓ≤j−1 因 N_p 非 p 倍数，也至多 j−2 个。故

\[
\boxed{v_p[x^{N_p}]Q(\Xi)=-5(j-1),\qquad p\nmid N_p.}
\tag{B10}
\]

这个 shifted-index 加强是对实际 Q 和实际 Ξ 的精确 coefficient 证明，不替换源，也没有把未知 lifts 当作自由参数。

## 4. CDT 阶梯类型的必要费用与标准割线叶的确切障碍

实际读取 [CDT 作者 2026 原件](../literature/cdt2026_effective_holonomy_author_20261006.pdf)，PDF1–7，本文直接使用 PDF3–5 的 Theorem2.1、Remark2.5 及 PDF5–7 的 η-filtration 说明；主来源为 [作者原件](https://math.berkeley.edu/~ytang/ICM.pdf)。这是固定20页快照，与2025 arXiv稿不混用。另实际读取固定 [CDT v2 长稿](../literature/cdt2024_l2_chi_minus3.pdf) PDF66–70全文，核 Definition6.0.1、(6.0.4–6)、Remark6.0.12。后者218页固定v2，与作者220页长稿不同。

写 K_b(N)=lcm(1,…,floor(bN))，空集的 lcm 取1。先考虑 Theorem2.1 的固定有限产品 denominator，固定整数倍或 finite exceptional-prime localization 亦不改变以下必要界：

\[
f(x)=Q(\Xi(x))=\sum_{N\ge0}
\frac{u_Nx^N}{\prod_{\ell=1}^R K_{b_\ell}(N)},
\quad u_N\in\mathbf Z,\quad b_\ell\ge0.
\tag{B11}
\]

在 B8 的 N=jp 处，让 p→∞。因 R、所有 b_ℓ 先固定，每个 K_(b_ℓ)(jp) 最终至多含一个 p；若 b_ℓ<1/j，则不含 p。精确 −5j 要求至少 5j 个 b_ℓ≥1/j，因而

\[
\boxed{\sigma:=\sum_\ell b_\ell\ge5
\quad\text{对每个非恒定 polynomial row}.}
\tag{B12}
\]

固定 offsets floor(bN+c) 也不改变这个必要界：b<1/j 的 factors 最终仍不含 p；每个 factor 最终至多含一个 p。边界 b=1/j 是否因 offset 不贡献，只会使清分母更困难。

现在允许 Remark2.5/长稿6.0.9 的 N^e，e∈N 固定。B8 仍给 σ≥max(0,5−e/j)。更强地，对 j≥2，使用 B10，N_p^e 为 p-unit；每个 LCM factor 最终至多一个 p，贡献者必满足 b_ℓ≥1/(j−1)。所以

\[
\boxed{\sigma\ge5\quad(j\ge2),
\text{ 即使额外允许任何固定 }N^e.}
\tag{B13}
\]

CDT 的 q×R cap array 每列只有一次由0跳到固定 b的台阶，故 row sums σ_i 非降，且

\[
\tau^\flat=\frac1{q^2}\sum_{i=1}^q(2i-1)\sigma_i.
\tag{B14}
\]

对 q 个独立 fixed-polynomial rows，degree0 rows 至多一条，因此 pure finite-LCM 模型在 q≥2 时 σ_i≥5（i≥2），

\[
\tau^\flat\ge5(1-q^{-2})\ge15/4.
\tag{B15}
\]

在允许 N^(e_i) 的模型中，degree≤1 的空间维数至多2；其余 rows 受 B13 限制。非降 row sums 给 σ_i≥5（i≥3），故

\[
\boxed{q\ge3\implies
\tau^\flat\ge5(1-4/q^2)\ge25/9.}
\tag{B16}
\]

长稿定义的 τ^sharp(e) 是非负 ξΣe 加非负 integrals 的 minimum 乘正因子，故 τ_total=τ^flat+τ^sharp≥τ^flat。这里没有计算或宣称最优 τ^sharp；q≤2 且允许 N^e 时也未作全排除。

标准 slit domain D 的 conformal radius 在0为4：z↦4z/(1+z)^2 将单位盘双全纯地映到 D。对任何 holomorphic φ:unit disk→D、φ(0)=0，inverse map 后的 Schwarz lemma 给 |φ′(0)|≤4。因此 log|φ′(0)|≤log4<2<25/9。B15–16 使上述 q≥2 pure-LCM 或 q≥3 带 N^e 的规范提升不满足 CDT 的严格正分母条件。

这是该固定-polynomial 提升、该 denominator class 和标准 slit leaf 的真实必要费用障碍。它不排除不同 rational-function basis、其他 genuine meromorphic pullbacks、trace/Hadamard 后的新芽、改进的 denominator estimate 或新的 holonomy 定理。尤其不把 σ≥5 当作所有可能 period realization 的费用下界。

## 5. 实际 monodromy 的不变部分，以及可用的替代接口

在 C(x)-module M_d=⊕_(j=0)^d C(x)Ξ^j 中，绕1的 invariant submodule 恰为 C(x)：若 F=Σa_j(x)Ξ^j invariant，则 F(Ξ+kv)=F(Ξ) 对所有 k 成立，最高 k coefficient 再次迫使全部 j>0 coefficients 为零。相应地，在 Q-span E(V_(n,d)) 中，invariant part 为 E(V_(n,d)∩Q)，维数至多1。这里区分了 rational functions 与常数 polynomials，不将两者混同。

特别对 nonconstant Q，假设 ξ=c∈Q 后的 Q(Ξ)−Q(c) 仍有非零 monodromy，尽管它的 endpoint limit 为0。确切 branch defect 是

\[
Q(\Xi+v)-Q(\Xi)
=\sum_{\ell=1}^{\deg Q}Q^{[\ell]}(\Xi)v^\ell,
\quad Q^{[\ell]}=Q^{(\ell)}/\ell!.
\tag{B17}
\]

所以 endpoint 消失不等于 CDT 成功例中的实际小奇点过收敛。这个结论对任何实际 minor polynomial、任何取自原 det 的固定 n Hasse coefficient polynomial 都适用；不必先知道它们是否互相独立。

给出一个严格、可实际用于下一条路线的 sufficient interface。设实际候选 germs A_(i,ℓ)(x)∈Q[[x]]，0≤ℓ≤d，属于已确认的共同 regular-singular system，定义

\[
g_i(x,\xi)=\sum_{\ell=0}^d\xi^\ell A_{i,\ell}(x).
\tag{B18}
\]

不把这些 A 宣称已构造。若要将实际 compound/jet endpoint 信息移入这个接口，需要明确的真实 period projection（包括所有 constants）识别每个所用 endpoint 与原 Q_i(ξ)。只证明 formal symbolic weight match 不足。

对一个给定 holomorphic φ，令 Z 为其落在实际系统 singular locus 的 preimages。φ非恒定、singular locus有限时，Z 在单位盘内离散。若拉回的实际 g_i 在 punctured disk 上可延拓，并对其所有 loops 满足

\[
\sum_{\ell=0}^d\xi^\ell\Delta_\gamma A_{i,\ell}=0,
\tag{B19}
\]

则 g_i∘φ 单值；regular-singular moderate growth 给每个孤立点至多 pole，故它在全盘 meromorphic。理由是单值 holomorphic punctured germ 的 polynomial/logarithmic growth 在乘足够整数幂后有 removable singularity。必须使用实际 continuation 的 branches 逐 loop 核B19；不只核 formal residues。这里 B19 和 moderate growth 是一套明确 sufficient leaf criterion。

在假设 ξ=c∈Q 下，g_i(x,c) 的 coefficients 才由这组实际 A 的有理性而有理。随后必须对这些相同 functions 证明 actual Q(x)-rank ρ、complete Taylor denominator cap (b;e)、同一 φ 的 meromorphic pullback。此处明确选用固定218页 CDT v2 的 **Corollary6.0.14**（PDF68），包括其对先验 holonomic functions 的 relaxation；不将不同版本的分子混用。b 是这 ρ 个实际 functions 的 column-step cap array，e=(e_1,…,e_ρ)∈N^ρ 是其额外 coefficient-index powers；τ(b;e)=τ^flat(b)+τ^sharp(e)，其中 τ^sharp 严格取同版 Definition6.0.1/(6.0.5)，不删除这项。

先用 φ 在闭单位盘邻域 holomorphic、φ(0)=0、φ′(0)≠0 的充分情形，并定义所用分子

\[
J_{\max}(\varphi):=\int_{\mathbf T}\!\int_{\mathbf T}
\log\max\{|\varphi(z)|,|\varphi(w)|\}\,
d\mu_{\rm Haar}(z)d\mu_{\rm Haar}(w).
\]

这个积分在上述情形有限；要求实际拉回 functions 在开单位盘 meromorphic、所有 coefficients 经一次固定 scaling 后确实满足完整 cap。先验 holonomicity 在 B18 的真实 regular-singular system 中已保证。因此下列 strict criterion 给同一 Corollary 的矛盾：

\[
\boxed{\rho\bigl(\log|\varphi'(0)|-\tau(b;e)\bigr)
>J_{\max}(\varphi),\qquad\log|\varphi'(0)|>\tau(b;e).}
\tag{B20}
\]

若 φ 只在开单位盘 holomorphic，则先对每个 0<r<1 的 φ_r(z)=φ(rz) 用同一明确积分 J_max(φ_r)；只要某个 r 给 B20 即足够。也可证明 r↑1 的 strict margin 有正下界从而获得这样的 r；必须同时保留 log|φ_r′(0)|=log r+log|φ′(0)|。未证明适当的 boundary convergence/strict margin 时，不将 formal boundary expression 当作有限可用的 J。本文没有证明任何新候选 φ 已满足这些条件。

这才是选定 CDT 定理的真正 contradiction 接口。有效 holonomy 原件 PDF5–7 的 η-filtration 中的 powers ξ^ℓ 只是组织实际 A_(i,ℓ) 的参数 filtration；原件仍要求所列 g 的真实函数独立性，不能用 numerical polynomials 的 degree 或 rank B 代替。

## 6. 实际 compound 的所有 q 情形，以及 scalar 路线的边界

可以把 B13 与本轮 [原斜率 H1](cdt_odd_paired_hasse_jet_mixed_gram_20261007.md) 直接合接。该稿稳定 SHA c178bf85 的 H1 已自足证明同一原 V_n=∂_TB_n 为实正定整数矩阵；本文已实际全文读该稿并独立审查 H1–H17，不靠未保存 future lemma。

因此对每个 d-principal minor，最高 coefficient 为 det(V_(n,I,I))>0，degree 恰为 d。这说明实际全部子式空间 V_(n,d) 的 maxdegree 恰为 d；其任何 **fixed-polynomial full basis** 都至少包含一条 degree d 的 row。对 d≥2，B13 强迫至少一条 row 的 σ≥5。结合 column-step 的单调性：q=1 时 τ^flat≥5；q=2 时 σ_2≥5，故 τ^flat≥15/4；q≥3 时采用 B16。于是

\[
\boxed{d\ge2\Longrightarrow
\tau_{\rm total}\ge
\begin{cases}
5,&q=1,\\
15/4,&q=2,\\
5(1-4/q^2),&q\ge3,
\end{cases}
\quad>\log4.}
\tag{B21}
\]

这补上带 N^e 时的一次小秩空档：**实际整个 compound 的规范提升及其 fixed-polynomial full basis**，对所有 q≥1 均不能在标准 slit leaf 跨过已述 CDT 正分母门槛。它不排除丢弃高次数 rows 后的子空间、其他 rational-function basis 或新的过收敛实现；不把独立函数数 q 偷换成矩阵rank。

对原 B_n(c) 的 minors，冻结 P14 的 scalar 矛盾只需同一 nonzero minor sequence、完整整化和其充分解析衰减。若从原 det 的低阶 Hasse jets 得到另一 scalar sequence，则同样应核它自己的非零、signed arithmetic scale 和 analytic bound。两条 scalar 路线都不需要把矩阵rank换成 CDT 函数rank；它们也不会自动给 B18–20。

相反，把随 n 变化的 minors/jet sequence 写成一个 generating series，不能仅由每个固定 n 的 polynomial lift holonomic 就断言其 generating series holonomic：此处 determinant 大小随 n 增长，本文没有给这种无限族一个固定 finite differential system。保留这个未证接口，可避免在 rank 增长处悄悄换对象。

本轮确实推进了三个缺口：B4/B6 给同一实际 period 的规范函数实现及完整独立秩；B7/B8/B10 给 all-prime prefix 与精确 coefficient 见证；B12–16/B21 把这种实现的 denominator 成本接到真实 CDT array，证明实际 compound 的整个规范 polynomial 提升在标准割线叶上不能提供所需预算。B19–20 进一步给出替代路线应证明的明确 monodromy、rank 与严格余量接口。

尚未构造满足 B18–20 的新过收敛系统，尚未得到原 ξ 或其他单个 ζ/L/Catalan 的新无理性、数值线性无关性或 Lean 形式化结论。本文不沿用旧 guard 的检查数作为新增证据；独立全文审查与最终单向来源收据另存。
