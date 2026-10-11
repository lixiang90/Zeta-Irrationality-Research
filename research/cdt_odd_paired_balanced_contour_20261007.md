# 原配对周期的平衡绕数、轮廓变形与核商相位证书

2026-10-07，作者 /root，NEW 纯纸面稿。Authority 为总报告 §§176–180 与 `cdt_odd_delivery_phase_kernel_content_20261007.json`，SHA `959e24af83f2124da40079aa70fade144425f6d15e5e990e455f1ec5a088264d`。580 旧冻结记录只读；不执行、import 或 rerun 旧数学 producer，不扩 prime。目标仍是原 ξ=αζ(4)+βζ(5)，固定 α,β∈Q、β≠0。本稿证明实际棘手的 cot 极点如何允许轮廓移动；尚未给出跨过算术费用的最优轮廓或新特殊值无理性。

本轮本人实际 FULL 读 [原饱和格 I1–I25](cdt_odd_paired_head_free_integral_lattice_20261006.md)、[原耦合积分 C1–C23](cdt_odd_paired_coupled_gram_decay_20261007.md)、[精确相位 F1–F18](cdt_odd_paired_exact_phase_geometry_20261007.md)及其[正式独审](cdt_odd_paired_exact_phase_geometry_independent_review_20261007.md)。相对谱稿初次合并输出有截断，相关页域另读；不把该首次输出称全文。以下残数和轮廓结果直接自证，不借未完成的 Riemann–Hilbert 渐近识别。

## 1. 同一真实空间与正常化

记

\[
S(z)=\prod_{j=1}^{2n}(z-j),\quad D(z)=(z)_{6n+1},\quad
C_n=\frac{(6n)!^2}{(2n)!^3},\quad R(z)=C_n\frac{S(z)^3}{D(z)^2},
\]
\[
K(z)=-4\alpha(\pi\cot\pi z)''-\beta(\pi\cot\pi z)''',\quad
m'=2n+1-m,\quad d_j=D(j).
\tag{D1}
\]

原空间是

\[
\mathcal A=\{p\in\mathbf Q[z]_{<3n}:p(m)/d_m=p(m')/d_{m'},\quad1\le m\le n\}.
\tag{D2}
\]

取原完整饱和整数基 g=(G_1,…,G_n,f_{2n},…,f_{3n−1})。原竖线 Γ_R 为 z=2n+1/2+ix、自下而上；定义

\[
\mathscr B_\Gamma(p,q)=\frac1{2\pi i}\int_\Gamma R(z)K(z)p(z)q(z)\,dz.
\tag{D3}
\]

在 Γ_R 上 dz=i dx，所以 D3 恰是原 B 的正常化，不差 i 或 2π。只在 ξ=c∈Q 的假设下，原真实 period B_n(ξ) 才与有理矩阵 B_n(c) 识别；本文不把任意 X 的数值都赋予这个积分。

## 2. 每个 head 的准确残数

在正整数 j≤2n，令 w=z−j。cot 的 Laurent 展开给

\[
(\pi\cot\pi z)''=2w^{-3}+O(w),\qquad
(\pi\cot\pi z)'''=-6w^{-4}+O(1),
\]
\[
K(z)=6\beta w^{-4}-8\alpha w^{-3}+O(1),\qquad
R(z)=C_n S'(j)^3d_j^{-2}w^3+O(w^4).
\tag{D4}
\]

因此原低列虽然可写成 S 乘有极点的 rational function，不能把所有 g 都误称被 S 整除。正确结论是 R 自己有三阶零；β 项留下至多一个 simple pole，α 项在这些 head 正则。对所有 p,q∈A，

\[
\boxed{\operatorname{Res}_{z=j}RKpq
=6\beta C_n S'(j)^3\frac{p(j)q(j)}{d_j^2}.}
\tag{D5}
\]

只有这一个首项贡献 residual；不用 p'、q'、D'，没有遗漏 cot 的高阶极点。

准确有

\[
S'(j)=(-1)^{2n-j}(j-1)!(2n-j)!,\qquad S'(m')=-S'(m).
\tag{D6}
\]

记 t_m(p)=p(m)/d_m=p(m')/d_{m'}。令 a_m=6βC_n S'(m)^3≠0，则 pair 残数是

\[
\operatorname{Res}_{m}RKpq=a_mt_m(p)t_m(q),\qquad
\operatorname{Res}_{m'}RKpq=-a_mt_m(p)t_m(q).
\tag{D7}
\]

这是真实 bilinear period 的成对抵消；单个 head 通常仍是极点。例如原 G_m 的 t_m=1/gcd(d_m,d_m') 非零，所以不能把各 head 各自填洞。

## 3. Head-only 变形的必要且充分绕数条件

取与 Γ_R 两端相同的 piecewise smooth Γ；要求两条曲线避开所有极点，并且差 Γ−Γ_R 是紧支闭 cycle，其非零极点绕数仅在 heads 1,…,2n 上。记该 cycle 对 head j 的整数绕数 w_j。允许 finite union 或带符号 cycle；不预设每个绕数都是0/1。

残数定理准确给

\[
\boxed{\mathscr B_\Gamma(p,q)-\mathscr B_{\Gamma_R}(p,q)
=\sum_{m=1}^na_m(w_m-w_{m'})t_m(p)t_m(q).}
\tag{D8}
\]

原 D2 允许各 t_m 独立取值：用 d_mL_m+d_{m'}L_{m'} 就能使其中一个 t_m=1、其他为0，degree≤2n−1。由于 a_m≠0，D8 因而证明

\[
\boxed{\mathscr B_\Gamma=\mathscr B_{\Gamma_R}\text{ 在整个 }\mathcal A\times\mathcal A\text{ 上}
\iff w_m=w_{m'}\quad(1\le m\le n).}
\tag{D9}
\]

这是原 source 的完整 head-only admissibility 条件，既有充分性也有必要性。对某一个向量，额外残数可能偶然抵消；这不保证整个矩阵不变。若变形绕到 nonhead positive cot pole 或 negative denominator pole，D9 不再是充分条件，必须另加那些真实 residual。本稿不允许免费穿越它们。

## 4. 左右竖线确实同 period；尾部不能略过

令 Γ_L 为 z=1/2+ix、自下而上。两条无限竖线并非紧支同尾，但在 Re z∈[1/2,2n+1/2] 的有限宽 rectangle 中，cot 二、三导数 uniformly O(e^{−2π|Im z|})。固定 n 时，R(z)=O(|z|^{−6n−2})，pq degree≤6n−2，故 RKpq=O(|z|^{−4}e^{−2π|Im z|}) 在上下 horizontal edges 一致成立。

horizontal integrals 趋0，两条 vertical integrals 都绝对收敛；rectangle 内只有全部 heads，每个 winding 相同。由 D7 得

\[
\boxed{\mathscr B_{\Gamma_L}(p,q)=\mathscr B_{\Gamma_R}(p,q)\qquad(p,q\in\mathcal A).}
\tag{D10}
\]

原 P_R 的更强 n-dependent bounds 并不自动转给 P_L。D10 是 exact same-period 身份，不是左 contour 已经更好的主率。接近任何 singularity 的曲线也必须重新付 positive variation norm；不以 closed-cycle integral 为0 推出 total variation 为0。

## 5. Nonhead 跨越的可见费用

对正整数 j>2n，R,p,q 在 j 都正则。写 h=Rpq；由 D4 的 cot 主部直接有

\[
\boxed{\operatorname{Res}_{z=j}K(z)h(z)=\beta h'''(j)-4\alpha h''(j).}
\tag{D11}
\]

因为 w^{−4} 取 h'''/3!，w^{−3} 取 h''/2!。D11 一般包含 value/derivative 的整个 jet，没有 head 的 simple paired cancellation。negative j∈{0,−1,…,−6n} 另有 R 的 double pole，必须计算至更高 Laurent jet，不能用 D11 当完整公式。

这区分了两种很不同的变形：在 heads 上按 D9 成对穿越可 exact 保留 B；越过非配对周期 poles 会改变 B，并可能改变原 ζ/L 投影。仅仅把 cot 看成 exponentially decaying smooth weight 然后任选 steepest contour，会漏掉这些费用。

## 6. 同一算术核商在新 contour 上的精确相位证书

令 Γ 为 D9 允许的曲线，或有完整边界消失证明的 D10 型曲线。要求它包含非平凡弧段，且所有 integral finite。沿 Γ 的 complex density 是 R(z)K(z)dz/(2πi)，定义真实 positive Hermitian Gram

\[
(P_\Gamma)_{ij}=\frac1{2\pi}\int_\Gamma g_i(z)\overline{g_j(z)}|R(z)K(z)|\,|dz|.
\tag{D12}
\]

polynomials 线性独立、density 除 discrete zeros 外非零，故 PΓ>0。原 B 不变。假设 ξ=c∈Q，沿已冻结定义取 actual rank d、ν=2n−d、primitive integer kernel K_0、unimodular U=[L,K_0]，q=det(LᵀBL)≠0。K_0 记号避免与 cot K(z) 混淆。记

\[
Q_\Gamma=\frac{\det P_\Gamma}{\det(K_0^tP_\Gamma K_0)}>0,
\quad T_\Gamma=P_\Gamma^{-1/2}B(P_\Gamma^{-1/2})^t,
\quad\Theta_{\Gamma,d}=\prod_{i=1}^d\sigma_i(T_\Gamma).
\tag{D13}
\]

每个合法 complex measure 的 Cauchy–Schwarz 同样给 ||TΓ||≤1；重复冻结 F1–F4 的 finite compound/Jacobi 证明，无需额外整数换基，得

\[
\boxed{|q|=Q_\Gamma\Theta_{\Gamma,d}\le Q_\Gamma.}
\tag{D14}
\]

因为 B、原整数格和 K_0 完全相同，算术整化费用仍是原 q 的费用；新 PΓ 必须完整重估。固定相同 determinant1 补基即可，quotient determinant QΓ 与该补基的 choice 无关。空核 ν0 用 denominator1。

对原 Γ_R，D14 精确给 |q|=Q_RΘ_R。于是任何一个真正计算过的新 contour 提供

\[
\boxed{\Theta_R\le Q_\Gamma/Q_R,\qquad
-\log\Theta_R\ge\log Q_R-\log Q_\Gamma.}
\tag{D15}
\]

右侧可为负，此时只是一条无增益的 lower。它是原非零 phase 的合法证书；若实际 log quotient improvement 有 cn² 主率，才能给 cn² phase 信用。不要再把同一 improvement 作为独立 kernel credit 扣第二次。此接口绕过仅取 polynomial-order trace 截断的 O(nlogn) 限制，尚未证明所需改善存在。

## 7. 凸合并 contour 不免费改善商 Gram

若合法曲线 Γ₁,…,Γ_r 都给同一 B，a_j≥0、Σa_j=1，则带标签 disjoint union measure 仍给 B，positive Gram 为 \bar P=Σa_jP_j。但这种合并本身不比最佳单曲线的 determinant bound 好。

证明用指定 U 的 Schur quotient P_Q。对每个 x∈C^d，

\[
x^*P_Q(P)x=\inf_{y\in\mathbf C^\nu}(x,y)^*(U^tPU)(x,y).
\tag{D16}
\]

固定 x 后 infimum 是 P 的 concave 函数，因此

\[
P_Q(\bar P)\succeq\sum_j a_jP_Q(P_j).
\]

log det 在正矩阵上 monotone 且 concave，得到

\[
\boxed{\log Q(\bar P)\ge\sum_j a_j\log Q(P_j)\ge\min_j\log Q(P_j).}
\tag{D17}
\]

这里 det U=±1，所以 Q(P)=det P_Q(P)；ν0 亦一致。故只把若干 total-variation Grams 凸平均，不能产生比全部单曲线更小的 q 上界。D17 限定这一具体 positive-bound 操作；保留复 interference、不同各行 representation 或完整 RHP 渐近不在该结论内。

## 8. 与完整费用比较；尚未闭合的真正任务

在原有理性假设、无限适用 actual-rank 子列，冻结完整整模型给固定 D,M 及尺度 Q^q_{n,d}，使

\[
(DM)^d q/Q^q_{n,d}\in\mathbf Z\setminus\{0\}.
\]

记这里 Q^q 是算术尺度，QΓ 是解析商 determinant，二者不可混同。由 D14 的真正充分条件是

\[
\boxed{\limsup n^{-2}\{\log Q_\Gamma-\log Q^q_{n,d}+d\log(DM)\}<0.}
\tag{D18}
\]

也可保留 ΘΓ 再加 logΘΓ。算术主费安全 upper A_q(λ)=32λ−1−13λ²/4，λ=d/n；D18 仍未成立。本稿不将 39.6875 称 actual 最优费用或 no-go lower。

下一项具体分析任务是：在 D9 的实际平衡绕数类中构造曲线，控制 n-dependent basis 的 entire quotient Gram，包括 head 邻域、tails、K zeros 与 denominator poles；或者建立同类适用的 non-Hermitian/vector RHP。D10 给一个实际可用的另一条曲线但没有费率改进；D17 排除了仅靠正 Gram 平均的便宜捷径。

## 9. 一手文献与本轮边界

正常 TLS 新存 Vartanian–Zhou, *Riemann–Hilbert Characterisation of Rational Functions with a General Distribution of Poles on the Extended Real Line Orthogonal with Respect to Varying Exponential Weights: Multi-Point Padé Approximants and Asymptotics*，[固定 arXiv1912.00500v1](https://arxiv.org/abs/1912.00500v1)，[库中PDF](../literature/cdt_paired_contour_deformation_sources_20261007/vartanian_zhou2019_rational_rhp_arxiv1912_00500v1.pdf)，343页，4728476bytes，SHA `0729a0ef7aaf008d7854c365afc8669ccef8330bfd66511aa05def8d40c7df4f`。arXiv页眉 December1 与文内 December3,2019 分别保留。本人实际完整文本读 PDF1–8；初次组合输出的4–5页省略段另实际补读才计全文。

PDF1、3、7–8明确采用正实测度、有限固定 K 个 real poles 循环、real analytic external field 及各极点处足够强的增长条件。当前原 complex cot period、成对 residue 约束、随 n 增长的 pole 数及非正 phase不属于其已核条件。这里只以该文作为有理函数/极点 RHP 的 primary 接口，未套用它的渐近定理、未执行其算法，也不称已读343页全文。

本轮新纸证是 D5–D10 的准确成对 residue 与必要充分绕数类，D11 的非 head 跨越费用，D14–D15 的同一算术核商/原 phase 轮廓证书，以及 D17 的凸平均界。无新数学 producer、prime实验、Lean，未证明新 ζ/L/Catalan 数值无理性或线性无关性。唯一新稿交 FULL 正式独审，作者收审后最终 FULL 回读再单向冻结。
