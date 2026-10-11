# 真实 moment-annihilator 排除便宜节点：关键窗口的源内容恰为 p^(2ν)

2026-10-07，NEW，作者 /root/masked_racah_finalize。Authority 为主报告 §§176–180 与 `cdt_odd_delivery_phase_kernel_content_20261007.json`，SHA `959e24af83f2124da40079aa70fade144425f6d15e5e990e455f1ec5a088264d`；580 冻结文件（575 数学、5 guards）只读。唯一 NEW 纯纸面研究主稿；不创建、执行、import 或 rerun 数学 producer，不扩素数表。原 B6/k3/s5、degree<3n、rank2n 饱和 paired 格及固定源保留。

## 1. 同一原核与本轮严格结论

取 n=4r≥4、m=2n。原整数值 paired 格的完整基为
\[
g=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\qquad
f_i(z)=\binom{z-1}{i},
\]
其中 G_m=p_mL_m+q_mL_{2n+1-m}、g 所在格是 ambient Newton 格的 direct summand，均按冻结 lattice I1–I25。原形式准确为
\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+T_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^{2}\binom{2n+j}{j}^{3},\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-8\alpha H_j^{(3)}-6\beta H_j^{(4)},\qquad
T_j(X)=C_jU_j+24\{X-\alpha H_j^{(4)}-\beta H_j^{(5)}\}.
\tag{A1}
\]
固定 α,β,c∈Q、β≠0，在原基中记 B=B_n(c)、actual rank d、ν=m−d。K 是实际完整 primitive 格 kerB∩Z^m 的整数基，故 BK=0；不是自由选取的低成本核。取原节点独立源
\[
V(z)=24\sum_{j=0}^{6n}W_jz_jv_jv_j^t,\quad
v_j=(g_i(-j))_i,\quad R_{K,j}=v_j^tK,
\]
\[
\mathcal G_K(z)=\det(K^tV(z)K),\qquad
g_K=\gcd\{\text{全部整数系数 of }\mathcal G_K\}>0.
\tag{A2}
\]
ν=0 时取空 det=1、g_K=1。冻结 content Q7–Q9 已证明
\[
[t^\nu]\det(B+tV(z))=q(B)\mathcal G_K(z),\qquad
v_pg_K=\nu v_p24+\min_{|J|=\nu}
\left(\sum_{j\in J}v_pW_j+2v_p\det R_{K,J}\right).
\tag{A3}
\]
这是多变量的 coefficient content，数值 a_V=G_K(1) 可能有额外相消。

**本轮定理。** 对全部 prime 5n<p≤6n，若 α,β,c∈Z_p 且 β∈Z_p^×，则
\[
\boxed{R_{K,j}\in p\mathbf Z_p^\nu\quad
\text{对全部 }v_pW_j=0\text{ 的原节点 }j,}
\tag{A4}
\]
\[
\boxed{v_pg_K=2\nu.}
\tag{A5}
\]
每个 source monomial 至少付 2ν，且存在一个恰付 2ν 的系数。不是先假设限制 Gram 的单位性或由数值 a_V 反推内容。

因此前轮在此窗口支付的 2ν 已是**真实原核多变量内容的准确值**。仅在同一 source polynomial 内寻找更便宜的 weighted minor，不能再减少这项支付。结论不表示 q 的全算术费用最优、不排除更强原 coefficient lower 或其他 prime 信用；也不提供连续 P-norm、relative-kernel compression 或 phase 的充分解析估计。

## 2. 原节点权重与准确 p^(-5) leading layer

置 e=6n−p、u=e+1、T=p−2n。由 5n<p≤6n，0≤e<n、1≤u≤n、T>3n，且 p>3n、p>5、p²>8n。原基所有 Newton denominator i!（i<3n）是 p-unit，故每个 g_i 的 monomial coefficients 与 ordinary derivatives 均 p 整。

全部节点只有 head j=ρ（0≤ρ<p）和 tail j=p+ρ（0≤ρ≤e）。Legendre 第一层给
\[
v_pW_j=2\mathbf1_{\rho>e}+3\mathbf1_{\rho\ge T},
\quad
\begin{array}{c|c|c}
\rho&\text{原节点}&v_pW_j\\ \hline
0\le\rho\le e&\rho,\ p+\rho&0\\
e<\rho<T&\rho&2\\
T\le\rho<p&\rho&5
\end{array}
\tag{A6}
\]
这里 tail 必是 unit-W 节点；没有额外非unit tail。T>3n 同时使前3n个负节点的 noncheap heads 全部恰为 weight2。

对 tail j=p+ρ（0≤ρ≤e），三个长度分别满足
\[
p\le j<2p,\qquad p<2n+j<2p,\qquad 0\le6n-j=e-\rho<p.
\]
每个跨 p 的 harmonic 仅含一个 p 倍数。把其他项写成 Z_p 元素，得到
\[
pC_{p+\rho}\equiv5-3=2\pmod p,
\quad p^4U_{p+\rho}\equiv-6\beta\pmod p,
\]
\[
\boxed{p^5T_{p+\rho}(c)\equiv
2(-6\beta)-24\beta=-36\beta\pmod p.}
\tag{A7}
\]
α 的 H^(3) 与 H^(4) 项分别多一个 p，c 项多五个 p；没有把它们视为新的单位项。此式的 −36 不来自旧 normalized matrix。

head j<p 的 U_j 为 p 整，T_j(c) 的估值至少 −1，因此 p^5T_head≡0、p^5U_head≡0。tail ordinary derivative 项亦有 p^5U_tail∈pZ_p，因此整个 derivative 双线性项 mod p 消失。对所有 P,Q∈原格⊗Z_p，准确
\[
\boxed{p^5B(P,Q)\bmod p
=-36\beta\sum_{\rho=0}^{u-1}
\overline W_{p+\rho}\,\overline{P(-\rho)}\,\overline{Q(-\rho)}.}
\tag{A8}
\]
用了 P(−p−ρ)≡P(−ρ) modp，这来自 p-integral monomial coefficients。各 W_tail 是单位；β 的 unit 假设及 p>5 确保 −36β 也是单位。形式在全原格上，不是只测试几个核点。

## 3. Paired 格仍有满射 cheap evaluation；实际核恰落其 radical

令 E_u 的第ρ行是 v_ρ^t，ρ0..u−1，即原 paired 格到这 u 个 cheap head values 的 evaluation。原格包含全部 n 个 high Newton 列；取其中前 u 个，去掉列 sign 后矩阵为
\[
Y_{\rho k}=\binom{2n+k+\rho}{\rho},\quad0\le\rho,k<u.
\tag{A9}
\]
这里 u≤n 保证所取 high 列确实存在。Vandermonde 恒等式自证整数分解
\[
Y=AB,\quad A_{\rho l}=\binom{2n+\rho}{\rho-l}\ (l\le\rho),
\quad B_{lk}=\binom{k}{l}\ (l\le k),
\tag{A10}
\]
其余 entries 为0。A lower triangular、B upper triangular、diagonal全1，所以 detY=1；原 high evaluation 带列 signs，det仅为±1。因而
\[
\boxed{E_u:\mathbf Z_p^m\twoheadrightarrow\mathbf Z_p^u,
\qquad\operatorname{rank}_{\mathbf F_p}\overline E_u=u.}
\tag{A11}
\]
这是 source evaluation 的真单位 minor，不是原 B 的 high block 正规性。paired G_m 中巨大的整数无需可逆；high 列已独立完成满射。

置 Δ=diag(overline W_(p+ρ))。A8 在原 g 坐标中的实际 reduction 为
\[
\boxed{\overline{p^5B}=-36\overline\beta\,
\overline E_u^{\,t}\Delta\overline E_u.}
\tag{A12}
\]
E_u^t 为 injective、Δ invertible、E_u surjective。因此
\[
\operatorname{rank}\overline{p^5B}=u,\qquad
\ker\overline{p^5B}=\ker\overline E_u.
\tag{A13}
\]
非退化 Δ 即使存在 isotropic vectors 也不改变此 radical 结论；不可用一个向量自配对为0替代整段 annihilator。

由 BK=0，乘 p^5 后并 reduce 得 E_u K≡0。tail values 与 head values modp 相同，因此
\[
\boxed{R_{K,\rho},\ R_{K,p+\rho}\in p\mathbf Z_p^\nu
\quad(0\le\rho<u).}
\tag{A14}
\]
这证明 A4。它利用实际 B 的 annihilator 及 literal β-leading term，比 SK saturation 单独提供更多条件。

## 4. 每项下界与达到下界的原 unit minor：精确内容

取任意 ν 节点 subset J。令 r 为其中 unit-W 节点数。A14 使相应 r 个整 evaluation rows 各有一个 p 因子，无论这些节点是 head 还是 tail，故
\[
v_p\det R_{K,J}\ge r.
\]
其余 ν−r 个节点按 A6 各至少有 W-valuation2。因此逐 monomial
\[
\sum_{j\in J}v_pW_j+2v_p\det R_{K,J}
\ge2(\nu-r)+2r=2\nu.
\tag{A15}
\]
W-valuation5 节点只加强这个 lower。p∤24，A3 严格给 v_pg_K≥2ν，零 minors 的估值为∞，无额外相消。

为证明达到 lower，令 S 是原 g 在 ambient N=3n Newton 基中的整数矩阵。原格 S 为 direct summand，K 是 Z^m 的完整 primitive kernel 基，故 SK 是 Z^N 的 direct summand：把 K 补为 GL_m(Z)，再把 S 补为 GL_N(Z) 即可。前 N 个连续负节点的 evaluation
\[
\mathcal E^-_{j,i}=\binom{-j-1}{i},\quad0\le j,i<N,
\qquad\det\mathcal E^-=\pm1.
\tag{A16}
\]
det 的绝对值由 leading coefficients 1/i! 与连续节点 Vandermonde ∏i! 消去；entries 皆整。故 E^-SK 全部 ν 阶 minors 的 gcd 为1，任一 p 可选一个 p-unit minor。

前 N 个节点中 j0..u−1 的 rows 已由 A14 全为 p 倍数，所以这个 unit minor 必须完全避开它们。其余 u≤j<3n 全满足 j<p、2n+j<p、j>e。准确
\[
v_pW_j=2\quad(u\le j<3n).
\tag{A17}
\]
于是所选 unit νminor 的 source coefficient valuation 恰为2ν。ν=0 时选空 minor，仍恰为0。A15 与这个系数合并证明
\[
\boxed{v_pg_K=2\nu,\qquad
\operatorname{rank}_{\mathbf F_p}
(R_{K,j})_{u\le j<3n}=\nu.}
\tag{A18}
\]
不能把“前3n有unit minor”描述为它可能使用 unit-W 节点；真实 annihilator 已严格排除这些节点。全部层级的 rational kernel、ambient saturation、ordinary reduction 与 source weights 在这里是同一原对象。

## 5. 饱和性单独能实现更便宜内容：原 high 子格的准确校准

以下不是实际 kerB，而是同一原 paired 格中的自由 primitive high 子格，用来准确区分 A14 的作用。取 0≤ν≤n，令 K_free 的 columns 是原基坐标中 f_(2n),…,f_(2n+ν−1)。这是原 Z^m 的 direct summand，保持原 degree 范围、节点和 W。

对任何这样的或其他 ν-column evaluation matrix，全部 unit-W head/tail rows modp 只有 u 个不同残差节点，所以这部分 row rank 至多 u。若某个 νminor 选 r 个 cheap rows，Z_p-unit row operations 可把这 r 行中至少 (r−u)^+ 行变为 p 倍数，故
\[
v_p\det R_J\ge(r-u)^+,\qquad
\sum_{j\in J}v_pW_j+2v_p\det R_J
\ge2(\nu-r)+2(r-u)^+
\ge2(\nu-u)^+.
\tag{A19}
\]
这里不是把 modp rank deficiency 仅记一个 p：各独立 deficient rows 都给一个 p，det 最少有对应次幂。

对所定义 K_free，前ν个负节点的 evaluation 正是 A9–A10 的 ν×ν 截断，det±1。其中 min(ν,u) 个 W-unit heads，余下 (ν−u)^+ 个 weight2 heads，因此存在系数恰付2(ν−u)^+。于是
\[
\boxed{v_p g_{K_{free}}=2(\nu-u)^+,
\quad\text{而 actual }v_pg_K=2\nu.}
\tag{A20}
\]
原应用中 ν≤n/2，亦在此范围。ν≤u 时自由饱和子格内容是 p-unit，但真 annihilator 的内容为 p^(2ν)；ν>u 时二者差2u。这个校准精确说明“饱和性 alone 不可改善支付”与“真实 annihilator 更便宜”是不同命题：实际 BK=0 使本窗口内容更贵，而非免费提供低成本 source directions。若 ν>0，所示 K_free 不满足 BK=0；其 cheap evaluation 在 A9 上有单位 minor，已与 A14 冲突。不把它冒作实际核反例或建立另一个数值目标。

## 6. 局部 Smith、数值 source 与固定 prime 例外的边界

因 p^5B 为 Z_p 矩阵而其 modp rank 恰 u，非零 Smith diagonal entries 中准确 u 个 valuation0，其余 d−u 个至少1；有 ν 个零 diagonal entries。这里只断言第一层，未推其余完整 Smith profile、q 最佳 valuation 或 source Gram 单位性。特别 d≥u 是自动结果，但不代替冻结的无限 n actual-rank lower。

数值 specialization 确实满足
\[
\boxed{v_p a_V=v_p\mathcal G_K(1)\ge2\nu,\qquad
v_p J_\nu=v_pq+v_pa_V.}
\tag{A21}
\]
content 的 exact2ν 不给 a_V 的 upper，后者是多项式 coefficients 的一次和，模 p 仍可相消。这个固定 local factor也不能免费从 original whole-jet 整性除去。可控 transfer 使用 coefficient content A3，仍应准确扣2ν。

这还给出同一数值 a_V 的真实全尺度 lower。取 D>0 清 α,β，c=a/M、M>0，令固定有限例外集合 \(\mathcal E\) 为整非零数 DM(Dβ) 的 prime divisors，并置
\[
\Pi_n=\prod_{\substack{5n<p\le6n\\p\notin\mathcal E}}p.
\]
原 V 与 K 都整、V 严格正定，因此 a_V 是正整数。A21 对每个 good prime 给
\[
\boxed{\Pi_n^{\,2\nu}\mid a_V,\qquad
\log a_V\ge2\nu\log\Pi_n
=2(\nu/n)n^2+o(n^2)\quad\text{uniform 于 }0\le\nu\le2n.}
\tag{A21a}
\]
准确地，PNT 给 \(\log\Pi_n=\theta(6n)-\theta(5n)-O_{\mathcal E}(1)=n+o(n)\)。相乘误差为 \(2\nu\,o(n)=o(n^2)\)，因 ν≤2n 而统一；可等价写 lower \(2(\nu/n)n^2-o(n^2)\)。固定有限 prime 例外没有藏入 n²主率，ν0 时双方为0。没有从 small-solution upper 反推 height lower：这里实际正整数判别量的整除性直接给 lower。A21a 属于原离散 kernel source 的 determinant，不是 continuous \(a_P=\det(K^tPK)\) 的 lower 或 relative \(a_V/a_P\) 的 upper；尚未提供 analytic strict margin。

等价地，定义 A14 的 cheap row除 p 后的整向量 a_j，其余 nodes 取 a_j=R_K,j。则
\[
p^{-2\nu}\mathcal G_K(z)
=24^\nu\det\!\left(\sum_j z_j\omega_j a_j^ta_j\right),\quad
\omega_j=\begin{cases}W_j,&j\text{ cheap},\\W_j/p^2,&j\text{ noncheap},\end{cases}
\tag{A22}
\]
等式是 Z_p[z] 中的准确身份。因为 cheap R_K,j=p a_j，整体源 kernel Gram 先除 p²；weight5 的 ω_j 被 p³整除。A18 说明此 normalized polynomial 的 coefficient content 为 p-unit，但 det 在 z全1处未必是 p-unit。A22 只是局部 kernel source factor的准确描述，不是把 normalized basis 的便宜费用免费移给原 q/P/B。

固定 α,β,c 的例外 prime 只包括其分母 prime 和 β 分子 prime。若 D 清 α,β、c=a/M，则全部 p∤DM·(Dβ) 自动符合 α,β,c∈Z_p 与 βunit。其他 prime 必须保留前轮实际全prime模型与 fixed(DM)^d，不用 A5 强行推论。对固定源/输入，大 n 的窗口 5n<p≤6n 自动避开这个有限例外集合，因此 A5 在主率窗口全量适用；既不需要扩素数表，也不产生额外面积。

## 7. 已排除的具体优化与仍可推进的 gate

前轮完整模型以全节点系数 lower 12p−68n−12，减去 source content upper2ν。现在 A5 把这项 upper 升为真实 exact value，因此
\[
v_p q\ \text{由该 coefficient lower 可保证的界仍为}
\quad12p-68n-12-2\nu,
\tag{A23}
\]
并与旧 actual-rank 共同 lower 取 max。没有把 arithmetic content lower 误称 q 的 height lower。完整 safe 曲线仍是冻结 Q4 的
\[
\boxed{A_q(\lambda)=32\lambda-1-13\lambda^2/4,
\quad\lambda\in[3/2,2],\quad A_q(3/2)=635/16.}
\tag{A24}
\]
本稿没有继续降低这个费用。它关闭了一个明确局部优化方向：在该真实原 kernel 和该多变量 source polynomial 中，无论 unit 或 nonunit evaluation minors 怎样挑选，都不能使 content 支付少于2ν。

真正尚开放的是：利用 BK=0 的更高 p-adic layers 提升原 F_ν coefficients 的共同 lower；提升 q 的实际非零 Smith diagonal 估值；在其他 prime 窗口得到额外信用；或证明连续 P-normalized kernel determinant/原 nonzero phase 的足够 n²增益。A14 的 p整除只约束整数 evaluation，不给连续 Hermitian norm upper，也不推出相对谱方向便宜。它甚至表明在离散 source 上原 kernel 在最便宜残差节点消失。不能由这一有限处事实宣布 relative kernel compression upper，亦不能免费换坐标放大 Plücker height 后保留原解析费用。

这个 exact 局部内容 theorem 不等于整个研究方法的不可能性定理；还没有新 ζ/L/Catalan 无理性、线性无关性或 Lean 结论。所有实际 rank/nullity 边界，包括 ν0，无非零 kernel 的无限性假设，均保留。

## 8. 实际读域、审阅与冻结状态

本轮 actual FULL 读取以下六份冻结 MD：最新 content Q1–Q22/8节（92a962）；primitive-kernel K1–K18/8节（996e26）；原 lattice I1–I25（5b7947）；actual-local G1–G15（2856a4）；Hasse arithmetic J1–J18/7节（8676d1）；relative-spectrum R1–R29/9节（41b309）。两次组合 read 的输出均完整；没有把截断片段算全文。negative evaluation 的三角分解在本文重新自证，不从 peer norm conclusion 反推单位性。

Authority 主报告 §§176–180 实际完整读取；当前audit完整syntaxparse、顶级 schema 字段、header45行、准确580/575/5计数和物理SHA读取，不声称人工全文读580记录或本agent全量物理审计。原 global saved113、数学 producer/结果/guards、prime tables 本轮没有额外 read/execute/import/rerun；不继承别轮或别人的原件读页。新增下载0，primary PDF/HTML新读0，Lean0，prime实验/扩表0。

唯一 NEW 主稿由 A6–A18 的真实 leading Gram 与双层 primitive content，以及 A19–A20 的同原 high 格校准构成；全部为纸面证明，无自有数学验证程序。正文稳定后 actual FULL 作者回读并交 scaled/root 正式全文独审；最终收审后再作者 FULL 回读和单向 FINAL 来源收据。580旧冻结文件不动，本文候选不预先宣布审查闭合。
