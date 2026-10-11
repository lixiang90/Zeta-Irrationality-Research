# 六积分最高 packet 的精确原生前缀秩

日期：2026-10-06。本文新增一个全好素数的精确秩接口，不修改冻结稿。输入是已审的 [完整六矩阵 packet](cdt_odd_level20_cartier_packet_matrix_20261006.md)。新结论将该稿的前缀维数下界在明确窗口中提升为等式，并处理 degree≤D 多项式源在 p>D 时的完整 residue 分解。本文不将原生前缀核直接认领为全局净 Smith 收益，不假设普通或非普通素数的密度。

## 1. 前六个慢变量系数已经给出一个单位三角矩阵

沿用 packet 稿的符号：ε=χ₅(p)，target sign δ′=−ε，Q_i=t^i/D_{δ′}，i=0,…,5；

\[
 \Xi_i(s)=\int_0^s Q_i(v)A_{\delta'}(v)f^{(\varepsilon)}(v)\,dv/v,
 \qquad \Xi_i(0)=0.
\tag{N1}
\]

反证假设仍为 L(3,χ₅)∈Q。取未分歧好 place 𝔭|p，排除此前固定规范和周期分母，并要求 p≥7、p≠109。原模型给

\[
 D_{\delta'}(0)=1,\quad A_{\delta'}(0)=-1/5,
 \quad f^{(\varepsilon)}(s)=\eta_\varepsilon s+O(s^2),
 \quad\eta_\varepsilon=1-\varepsilon\,5\sqrt5/4.
\tag{N2}
\]

Norm(ηε)=−109/16，故 ηε 在这些 place 为单位。积分直接给

\[
 \Xi_i(s)=-\frac{\eta_\varepsilon}{5(i+1)}s^{i+1}
             +O(s^{i+2}),\qquad 0\le i\le5.
\tag{N3}
\]

令 V_r 是 residue field k 上的 r×6 矩阵，行 m=1,…,r 为 [s^m]Ξ_i mod𝔭；0≤r<p。r≤6 时前 r 列构成单位三角矩阵，r≥6 时前六行可逆。因此

\[
 \boxed{\operatorname{rank}V_r=\min(r,6).}
\tag{N4}
\]

特别地，V_r 在 r≥6 时是从 k⁶ 到 kʳ 的单射。这个证明只用真实首项、零积分常数和 1,…,6 的单位性，不用有限素数扫描或 characteristic-zero 函数秩代替模p前缀秩。

## 2. 常数系数源：什么时候核恰等于 Hecke 核

令 Z_j=p⁴I_j，p<N≤p²。已证整个 fast prefix 身份为

\[
 \overline Z_j(t)=\sum_i\overline M_{p,ij}
                         \overline\Xi_i(t^p)\pmod{t^N}.
\tag{N5}
\]

原生常数源评价 E_{p,N}:O_{K,𝔭}⁶→O_{K,𝔭}[t]/tᴺ 为 c↦Σc_jZ_j。置 r=floor((N−1)/p)，则其 residue 矩阵为 V_r M̄_p；其余 coefficient rows 全零。

若 N≥6p+1，则 r≥6，(N4) 给出精确等式

\[
 \boxed{\ker\overline E_{p,N}=\ker\overline M_p,\qquad
        \operatorname{rank}\overline E_{p,N}
               =\operatorname{rank}\overline M_p.}
\tag{N6}
\]

因此这个窗口里没有未计入的慢变量 finite-jet kernel。若 M̄_p 可逆，则在所有 p<N≤p² 的窗口中都有

\[
 \boxed{\dim\ker\overline E_{p,N}=(6-r)_+.}
\tag{N7}
\]

当 r<6 且 M̄_p 退化时，仍需使用 6−rank(V_r M̄_p)，不能把 Hecke 核和短前缀核相加。上述等式不需要固定谱 projectors；若以旧/新 cusp 两个标量描述 detM_p，则需另外排 packet 稿 §5 的固定坏素数。

## 3. p>D 时，完整多项式源按 residue 精确分块

定义不更换原始坐标的完整原生源

\[
 \mathcal E_{p,N,D}:O_{K,\mathfrak p}[t]_{\le D}^{\,6}
       \longrightarrow O_{K,\mathfrak p}[t]/t^N,
 \quad(P_j)\longmapsto\sum_jP_j(t)Z_j(t).
\tag{N8}
\]

在 p>D、p<N≤p² 下，写 P_j=Σ_{a=0}^D c_{j,a}tᵃ。不同 a 的输出只支持在不同 residue classes n≡a modp，因而不发生交叉抵消。令

\[
 r_a=\left\lfloor\frac{N-1-a}{p}\right\rfloor.
\tag{N9}
\]

按 coefficient rows 的 residue 及 monomial columns 重新排序，整个 residue 矩阵精确为各 V_{r_a}M̄_p 的直和。因此

\[
 \boxed{\dim\ker\overline{\mathcal E}_{p,N,D}
       =\sum_{a=0}^D[6-\operatorname{rank}(V_{r_a}\overline M_p)].}
\tag{N10}
\]

这不是只用同一个常数核乘 tᵃ 的下界：高 monomial shift 留下的 slow prefix 更短，(N10) 完整计入这些额外核。

如果 N−1−D≥6p，则全部 r_a≥6，故

\[
 \boxed{\ker\overline{\mathcal E}_{p,N,D}
   =\bigoplus_{a=0}^Dt^a\ker\overline M_p,
 \quad\dim\ker=(D+1)\dim\ker\overline M_p.}
\tag{N11}
\]

这里等式只描述该原生源 residue space。若 M̄_p 可逆，则全窗口给精确闭式

\[
 \begin{split}
 K_{p,N,D}&:=\dim\ker\overline{\mathcal E}_{p,N,D}
       =\sum_{a=0}^D(6-r_a)_+\\
       &=\boxed{\sum_{h=1}^6
            \min\{D+1,(D+1-N+hp)_+\}.}
 \end{split}
\tag{N12}
\]

证明第二个等式：把 (6−r_a)_+ 写成 Σ_{h=1}⁶1_{r_a<h}；整数不等式 r_a<h 等价于 a≥N−hp。然后准确计数 0≤a≤D 的整数，不涉及 leading Taylor flag 的选择。

## 4. rank19 前缀的真实大素数启动位置

由 (N12)，可逆 M̄_p 的多项式源有非零核当且仅当

\[
 \boxed{p>(N-1-D)/6.}
\tag{N13}
\]

对实际 rank19 系统，完整 leading flag 的安全长度 N_D=19(D+1)+O(1)。故 polynomial-prefix kernel 启动于 p/D>3；原常数核的长度效应启动于 p/D>19/6。两者的不同来自 shift 后的截断长度，不是新增算术周期。

若 p/D→x>1、N_D/D→19，则可逆矩阵情形的精确原生核有极限

\[
 \boxed{\frac{K_{p,N_D,D}}{D+1}\longrightarrow
   k_{19}(x)=\sum_{h=1}^6\min\{1,(hx-18)_+\}.}
\tag{N14}
\]

其六个斜坡分别在 [18/h,19/h]，h=1,…,6。形式的累计 raw kernel 面积为

\[
 \int_1^{19}k_{19}(x)\,dx
   =\sum_{h=1}^6\left(19-\frac{37}{2h}\right)
   =114-\frac{37}{2}H_6=\frac{2747}{40}.
\tag{N15}
\]

(N15) 仅是 (N14) 的面积，未声称全部 place 满足 detM unit，也未把 raw rank defect 当成可直接扣除的全局净高度。实际 Smith 信用必须先减去各 grade/species 既有 row/column 因子，处理相同 cutoff 的 sharp 尾部及 near-balanced 交集。

## 5. 对下一步的精确约束与核验范围

在目前 [rank19 固定合法账本](cdt_odd_level20_cartier_rank19_budget_20261006.md) 的 ξ∈[19/15,9/7] 附近，N≥6p+1。常数系数新 S1 方向恰由 M̄_p 的退化提供，不存在免费的有限前缀增核。对 p>D 的 portion 更有 (N11)，而纯长度核直到 p≈3D 才开始。

这些是整个指定 coefficient prefix 的精确 residue 线性代数，不是某几个 minors 的实验。本文没有新 producer，没有重跑任何冻结脚本。完整 packet、实际六个积分、真实首系数及合法 N_D 分别引用已审报告；新增 (N3)–(N15) 的证明全部在正文。没有证明新的奇数 ζ/L 数值无理性，未外推 p≤D 的 polynomial residue 重叠情形或 mod𝔭² 提升。

conjugate_projection 已实际只读独审 (N1)–(N15) 全链：重推首六项单位三角性、p>D residue 直和、整数不等式 a≥N−hp 的精确计数、严格启动位置、归一极限及 2747/40 面积，全部通过。未运行 producer；N_D 的统一消失阶界沿用已审 rank19 输入，本次审阅未重证它，也未将原生核转为全局 metric 收益。
