# Level‑7 真周期域中的 Kummer 相对载体分类：有限 tensor／有理投影不能制造独立的 log2 连接常数

日期：2026‑10‑07。作者：`/root/source_pencil_finalize`。本轮 authority 为 `cdt_odd_delivery_paired_anti_modular_slopes_20261007.json`，SHA `47e298629fba798cc2d11a1e711219e61746c617f25f308919d9e1c6f6a7ecab`。612 个冻结记录（607 mathematical、5 guards）只读。本稿纯纸证；数学 producer 新建、执行、导入、重跑，prime 表扩展和 Lean 执行均为0。

本文给一个可以完整核查的新分类，而非宣称已经找到新的特殊值无理性定理。固定已有真实 level‑7 周期 `A`、相对解 `B`，再加入实际 Kummer germ `ℓ=log(1+28t)`。允许对其完整齐次 fundamental matrix、`B`、`ℓ` 做有限次 tensor 乘积、普通求导和有理运算。若最后的 scalar `F` 确实满足同一个 `L F∈Q(t)`，而且起点为 `Q[[t]]`，则严格有

\[
 F=T+cA+dB,\qquad T\in\mathbb Q(t),\quad c,d\in\mathbb Q.       \tag{K1}
\]

因此其完整反射跳跃系数只能是 `c+dκ`。在这个整个有理函数域中构造 `ΔσF=log2 ΔσA`，已经等价于原先尚未证明的数值 relation `log2=c+dκ`；把 logarithm 放入更高 tensor 或分式并不能绕开这一点。分类不涵盖真正新加入的 Green 积分或 Kummer convolution，它们会增加 Picard–Vessiot 扩张，必须另付完整连接常数和算术费用。

## 1. 真实算子、分支和字段

采用冻结 [modular 记录](cdt_odd_gamma_modular_relative_target_20261007.md) M1–M25 的同一坐标与 normalization，未替换原 `ξ` 项目源，也未把 ζ(7) 或 Catalan 免费移植为此模型的周期。记 `θ=t∂t`，

\[
 L=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),
 \quad r_B=t(1-t),\quad \sigma=1/28,\quad \mu=-1/28.           \tag{K2}
\]

`A(0)=1`、`LA=0`，`B(0)=0`、`LB=r_B`，实际 Taylor 前项为 `A=1+2t+24t²+…`、`B=t+45t²/4+…`。Yang fixed v1 PDF15–16 的 Example2 给同一实际解

\[
 B(t(q))=A(q)\sum_{n\ge1} c_nq^n/n^2,\quad
 f(q)=\eta(\tau)^3\eta(7\tau)^3=\sum c_nq^n,
 \quad\kappa=L(f,2),                                       \tag{K3}
\]

以及完整 analytic germ `B−κA` 在 `σ` 无奇性。因此以下 `Δσ` 始终沿 M6 的实际 branch 和同一个 based loop，

\[
 \psi:=\Delta_\sigma A\ne0,\qquad
 \Delta_\sigma B=\kappa\psi.                                \tag{K4}
\]

固定 `ℓ(0)=0` 的 `log(1+28t)`。它在 `σ` analytic，值为 `log2`；在 `μ` 的正向 loop 增加 `2πi`。`μ` 对 `L` 以及实际 `LB=r_B` 系统是 ordinary point，所有它们的 local branches 在这里 analytic。

用 ordinary derivative 写 `L=p₂∂²+p₁∂+p₀`，

\[
 p_2=t^2(1-t)^2(1-28t),\quad
 p_1=t(1-t)^2(1-42t),\quad p_0=-2t-4t^2.                    \tag{K5}
\]

在0选第二齐次解 `S=A log t+η`，`η∈tQ[[t]]`；实际 Frobenius recursion 给其存在与收敛。记 `V=span_C{A,S}`。在离 punctures 的固定 ordinary basepoint 上取 germs；所有字段均以 `C(t)` 为 base，常数字段为 `C`：

\[
 E_h=C(t)(A,S,A',S',W^{-1}),\quad
 E_B=E_h(B,B'),\quad E=E_B(\ell),\quad W=AS'-A'S.             \tag{K6}
\]

`E_B` 是真实 affine 系统的 PV field：其 fundamental matrix 可写

\[
 \begin{pmatrix}A&S&B\\ A'&S'&B'\\0&0&1\end{pmatrix},
 \quad y''=-\frac{p_1}{p_2}y'-\frac{p_0}{p_2}y+
 \frac{r_B}{p_2}z,\quad z'=0.                               \tag{K7}
\]

`E` 是 K7 与 `ℓ'=28/(1+28t)` 的 PV compositum。它包含这些对象的所有 fixed derivatives 和一切有限 rational expressions。有限 tensor product 的 matrix coefficients，以及从其系数做 rational row projection 得到的 scalar，仍属于 `E`。本文没有把通过新积分得到的 convolution 函数也算入这个有限 rational field。

## 2. 真齐次 SL₂ 与非平凡的 affine kernel

先补足这里使用的实际群条件。Yang PDF5–6 的 variation proof 给齐次 basis `A,τA`；冻结 M13–M15 已说明 finite-character modular monodromy 含两个角色为1、不同 invariant lines 的 unipotents。其 connected Zariski closure 包含 `SL₂`。另一方面 K5 给

\[
 \frac{p_1}{p_2}=\frac1t-\frac{14}{1-28t},\qquad
 W=\frac1{t\sqrt{1-28t}},                                  \tag{K8}
\]

因为 `W∼1/t` 于0。Wronskian 是 algebraic，故齐次 PV group 的 identity component determinant 为1。齐次 equation 全部 singular points regular；Singer Proposition1.3.27 的 monodromy density 遂给

\[
 G_h^0=SL(V)\simeq SL_2.                                   \tag{K9}
\]

完整 `G_h` 可能包含有限角色；以下从不把它未经说明地替换成 connected `SL₂`。K8 事实上把 determinant 限在 `{±1}`，只需要 K9 和 full group 的 finite-component 性质。

还需实际非齐次 class 非零。K5 的 finite local exponents 为0处 `(0,0)`、σ处 `(0,1/2)`、1处 `(1/3,2/3)`。若 `T∈C(t)` 满足 `LT=r_B`，ordinary point 的 pole 无法抵消 leading derivative；上述 singular points 的负整数 pole exponent 也都不是 indicial root。故 `T` polynomial。degree `d≥1` 的 leading output 是

\[
 -14d(2d+1)[t^d]T\,t^{d+3},                                \tag{K10}
\]

不能等于 degree2 的 `r_B`。常数 `T=a` 则要求 `−2a=1`、`−4a=−1`，同样不可能。齐次 rational solution 也没有：同一 pole 论证后，K10 排除正 degree，constant 由 `p₀≠0` 排除。于是

\[
 \ker(L:C(t)\to C(t))=0,\qquad r_B\notin L(C(t)).            \tag{K11}
\]

设 `G_B=DGal(E_B/C(t))`。对每个 `g∈G_B`，`gB−B∈V`，restriction onto `G_h` surjective（PV fundamental theorem）。所以 `G_B` 是 affine group `V⋊G_h` 的 closed subgroup，投影 onto `G_h`，kernel 为 closed additive subgroup `N⊂V`。char0 commutative unipotent subgroup 是 vector subspace（Milne Cor14.33）；conjugation 使 `N` 在 `SL₂` 下 invariant。standard representation irreducible，故 `N=0` 或 `N=V`。

排除 `N=0` 的步骤也保留 finite components。此时 restriction 为 algebraic group isomorphism（Milne Cor3.35 与 surjectivity）；`G_B^0≃SL₂`。representation `V+CB` 的 trivial quotient 有 invariant complement。可直接使用 §4 的显式 Casimir，得到 `T=B−v`，`v∈V`，且 `G_B^0` 固定 `T`、`LT=r_B`。任意 full component `g` 仍有 `gT−T∈V`；因 identity component normal，`gT−T` 又被 `G_B^0` 固定。`V^{SL₂}=0`，所以 full group 也固定 `T`。Singer Cor1.3.10 得 `T∈C(t)`，矛盾 K11。故严格有

\[
 N=V,\qquad G_B=V\rtimes G_h,\qquad G_B^0=V\rtimes SL_2.    \tag{K12}
\]

最后一个 equality 不是抽象 Levi 存在猜想：因为 kernel 已为全部 translations，给定任何 `h∈G_h` 的一个 lift，再乘适当 translation，可令该 lift 固定所选实际 `B`。因此实际 group 包含 block-diagonal subgroup `H=SL₂`，其在 `V` 上 standard、在 `B` 上 trivial。`N` 的元素 `n` 满足 `nB=B+n`。

## 3. 支付 ordinary puncture：Kummer 因子真正独立

考察 `G=DGal(E/C(t))⊂G_B×Ga`；Ga 坐标是 `gℓ−ℓ`。在 `μ` 的实际 loop 只作用为

\[
 (g|_{E_B},g\ell-\ell)=(1,2\pi i).                          \tag{K13}
\]

所有 integer powers 也在 `G`，Ga 中的 infinite arithmetic progression Zariski dense，故 `G` 包含 `1×Ga`。restriction `G→G_B` surjective。任意一个 `b` 的 lift `(b,a₀)` 再乘 `(1,a−a₀)`，即给所有 `(b,a)`；于是

\[
 G=(V\rtimes G_h)\times Ga,
 \qquad G^0=(V\rtimes SL_2)\times Ga.                        \tag{K14}
\]

这一步不能用 `ℓ(σ)=log2` 代替：真实 added ordinary puncture 和完整 `2πi` translation 是独立性的证据。也没有假设任何普通点 jump 可以产生任意复数；这里仅使用确实存在的 `2πi`。

## 4. 对全部有限 rational/tensor 表达的分类

**定理。** 若 `F∈E` 且 `LF=r∈C(t)`，则

\[
 F=T+dB+v,\qquad T\in C(t),\quad d\in C,\quad v\in V.        \tag{K15}
\]

特别地，`ℓ` 完全从结果中消失。证明如下。所有 automorphisms 固定 `r`，所以 `gF−F∈V`；`W_F=V+CF` 是 finite-dimensional stable representation，quotient trivial。PV action 在这一有限 stable space 上是 algebraic：field coaction 先给 rational matrix coefficients，group translations 将其定义的 identity-neighborhood 移到每个点，得到 regular representation。若 `F∈V`，K15 已成立；其余情况下 quotient dimension1。

给 `H=SL₂` 的 Lie generators 记为 `e,f,h`，满足 `[h,e]=2e`、`[h,f]=−2f`、`[e,f]=h`。在 standard `V` 上显式 Casimir

\[
 \mathcal C=h^2+2h+4fe=3I_V                                \tag{K16}
\]

而在 trivial quotient 上为0。逐项 commutator 检查 `C` 与 `e,f,h` commute，因而与 connected `H` commute。`C(W_F)⊂V`、`C²=3C`，所以

\[
 F_0=(I-\mathcal C/3)F,
 \quad F-F_0\in V,\quad F_0\in W_F^H.                       \tag{K17}
\]

这里 `ker C` 是一维 invariant complement，且 quotient trivial，故它被 `H` 固定；未对整个非 reductive `G` 错用完全可约定理。

Ga Kummer 因子与 `H` commute，且固定 `V`。因此任意 `a∈Ga` 的 `aF₀−F₀∈V` 又被 `H` 固定，必为0。这已证明 Kummer 因子不作用于 `F₀`。

对 `N=V`，映射 `n↦nF₀−F₀` 是 algebraic additive homomorphism `V→V`，因此 char0 下 C-linear。`H`-invariance 给

\[
 (hnh^{-1})F_0-F_0=h(nF_0-F_0).                             \tag{K18}
\]

它是 standard representation 的 equivariant endomorphism，故为 `d I`。这一 Schur 结论也可直接由 diagonal torus 迫 matrix diagonal、上下 unipotents 迫两个 diagonal entries 相等。实际 `B` 被所选 `H` 固定，且 `nB−B=n`；遂 `z=F₀−dB` 被 `N,H,Ga` 全部固定，即被 `G⁰` 固定。

再处理 full components：`Lz=r−d r_B∈C(t)`，所以任意 `g∈G` 有 `gz−z∈V`。由 `G⁰` normal 且固定 `z`，该 difference 也被 `G⁰` 固定。`V^{G⁰}=0`，故 `gz=z`。PV fixed-field theorem 得 `z=T∈C(t)`，K15 完成。

这个 proof 同时覆盖 arbitrary quotient denominators、高 tensor degree 以及 fixed derivatives；没有假设 `F` polynomial in `ℓ`，也没有漏掉 finite-character algebraic subfield。它只限制最终满足同一个 rational inhomogeneous equation 的 scalar，不把所有 field elements 都称为 order2 functions。

## 5. Q forcing、Q Taylor 的确切下降

现在加实际 M25 所需的 `r∈Q(t)` 和 `F∈Q[[t]]`。由 K15

\[
 LT+d r_B=r.                                                \tag{K19}
\]

先证明 `(T,d)` 唯一。两组之差若 `d≠0`，会给 rational particular of `r_B`，矛盾 K11；若 `d=0`，rational homogeneous kernel 为0。所以 solution pair 至多一个。

其次 uniqueness 没有自动让所有 complex coefficients rational，需一个真实 Q-linear system。`T` 的 finite poles 只能在 `p₂` 的 zeros 或 `r` 的 poles：在其它点 leading `p₂T''` 无法被 analytic RHS 或较低 derivatives 抵消。这个 finite set 是 Q-defined。若 `r` 的 denominator 为 `a(t)∈Q[t]`，选 sufficiently large integer `M`，以 `b(t)=(a p₂)^M` 同时覆盖实际 `T` 的所有 finite pole orders，再取 sufficiently large `N`，则

\[
 T\in\operatorname{span}_C\{t^j/b(t):0\le j\le N\}.          \tag{K20}
\]

在这个 fixed finite Q-space 中代入 K19，clearing denominators 后是有限 rational-coefficient affine linear system，包含一个 complex solution。Gaussian elimination over Q 给一个 Q solution；由上面的 uniqueness，它恰是 actual pair。所以 `T∈Q(t)`、`d∈Q`。本稿只纸面使用 linear algebra，没有执行求解代码。

最后0的 homogeneous exponents `(0,0)` 意味 `v` 没有负幂 pole，且其唯一 logarithm-free analytic line 是 `CA`。`F,B` holomorphic 于0，故 `T` 不能在0有 pole；`v=F−T−dB` 也 holomorphic，遂 `v=cA`。取 constant coefficient，`c=F(0)−T(0)∈Q`。因此 K1 无任何隐藏 complex normalization。

反过来每个 K1 表达且 `T` 在0 regular 都确实为 Q Taylor，并满足 rational forcing `LT+d r_B`。若强制 normalized `F(0)=0`，则更精确

\[
 F=dB+T-T(0)A,\qquad d\in Q,\quad T\in Q(t)\cap Q[[t]].      \tag{K21}
\]

从而整个已生成 field 中 same-L rational forcing 的 image 正好是 `L(Q(t))+Q r_B`；对 Q-Taylor germ 另保留0的 regularity。这是 forcing-space 的真分类，不能把它扩为所有 relative extensions 的分类。

## 6. 完整 σ jump、算术费用与跨权重目标

Rational `T` 没有 branch jump（即使在σ有 pole，它仍是 single-valued meromorphic）；K4、K1 因此给实际完整 germ

\[
 \Delta_\sigma F=(c+d\kappa)\psi.                           \tag{K22}
\]

若额外要求实际 `F` 在σ的 permissible germ 类型，以及 M25 的 `ΔσF=log2 ψ`，则因 `ψ≠0`

\[
 \log2=c+d\kappa.                                          \tag{K23}
\]

`d=0` 已由已知 log2 transcendence 排除；`d≠0` 正是原来想检验的未证 mixed numerical relation，而非一个免费构造结果。本文不证明 K23 不成立，也不从分别 transcendental 推出 `1,κ,log2` independent。若某天 K23 被证明，则 `cA+dB` 确实已经满足所需 σ jump；分类说明一个声称 independent carrier 的有限 Kummer/tensor ansatz 实际没有增加对象。

冻结 M10–M11 的实际整模型仍可使用：`A∈Z[[t]]`，`D_n²[t^n]B∈Z`，每个 fixed θ-jet 同 cap。因此当 K1 中 `T∈Q[t]` 时，一个固定 common rational multiplier 给所有 coefficients 的 `D_n²` 安全 cap。但 arbitrary `T∈Q(t)` 不能免费纳入同一 cap。例如

\[
 T=\frac1{2-t}-\frac12=\sum_{n\ge1}\frac{t^n}{2^{n+1}},        \tag{K24}
\]

满足 rational forcing `LT`、Q Taylor、zero σ jump；任何固定 multiplier 乘 `D_n²` 都不能消去所有2-adic denominators，因为 `2v₂(D_n)=2 floor(log₂ n)` 而实际 denominator exponent 为 `n+1`。如用 coordinate rescaling 或额外 exponential factors 支付，它的 endpoint、domain 与 CDT 几何分子也须同步改变。分类不是 integrality theorem for arbitrary rational gauge。

还必须保留 M25 的其它 conditions：full local jumps at0、1、∞及任何 added poles；同对象的 Betti/de Rham normalization；真正 holomorphic maps whose function pullbacks are meromorphic；CDT 全部 arithmetic rows、endpoint constants 和 geometric lift。本文的 classification 在已固定真实 period field 中成立，没有借虚构 period rank、数值近似或无证明的 normal-function existence 来支付这些 conditions。

## 7. 明确的真正逃逸接口：新 Green 扩张，而非旧 field 的新写法

给 `r∈Q(t)∩tQ[[t]]`，K8 使 variation of constants 的 actual normalized candidate 完全可写：

\[
 q_r(t)=\frac{r(t)}{p_2(t)W(t)}
       =\frac{r(t)}{t(1-t)^2\sqrt{1-28t}},
\]
\[
 C_r(t)=-A(t)\int_0^t S(u)q_r(u)\,du
       +S(t)\int_0^t A(u)q_r(u)\,du.                        \tag{K25}
\]

`q_r` analytic 于0，两个 integrals 的 logarithms 在该 bilinear combination 中消去。K25 由 Wronskian 逐项验证 `LC_r=r`、`C_r(0)=0`；同一 Frobenius recurrence 给 `C_r∈Q[[t]]`。它不自动给任何 all-prime cap，也不自动使 actual σ coefficient 为 log2。

如果

\[
 r\notin L(Q(t))+Q r_B,                                    \tag{K26}
\]

则 K1 严格迫 `C_r∉E_B(ℓ)`。K26 是独立 relative class 的必要逃逸证书，也给一个可以审查的反向接口：先证明 rational forcing class 不在旧 image，才能把新增 Green carrier 当作独立新对象。反之，当 `r` 落在该 image 且 normalized Q-Taylor solution 存在时，K21 与 uniqueness at0 直接给旧 field 表达。

K25 与 toy primitive `∫A/(t+a)` 有本质上的具体差别：若擅自令 `q_r=1/(t+a)`，其 forcing 是

\[
 r=\frac{t(1-t)^2\sqrt{1-28t}}{t+a},                       \tag{K27}
\]

一般是 algebraic 而非 rational，已经改变 M25 的 input。仅对 primitive 求导以修回 half-integer exponent 也不会产生 `log2` 常数。本稿不给此 toy ansatz 免费的 same-L 身份。

若 `r` 在σ analytic，local inhomogeneous equation 确有 analytic particular，其他 local component在同一一维 half-integer homogeneous line；其完整 jump 为一个 constant times `ψ`。这个 constant 来自 K25 的真实 continuation integrals。求出它等于 `log2`、支付其它 puncture 全部 jumps 与全有限处模型，仍是新工作的实质。本文仅提供旧 field 的完整排除分类和新 extension 的确切 membership gate，没有宣称已经实现 M25。

## 8. 实际来源、阅读域与本轮边界

本轮实际完整回读冻结 modular main M1–M25/all8sections；current main 只读取 header 与 §§196–200，不称全文。authority JSON 只核 current progress 与物理 SHA，不称重复612项历史 proof audit。所有以下 primary 为已有 archive，未重复下载，未新建 PDF。

- [Yang, fixed v1](https://arxiv.org/abs/0709.1968v1)，本轮 actual FULL PDF5–6、15–16，4个 distinct pages，用于实际 variation、operator、forcing 与全部 σ germ。复用 `literature/yang2007_apery_limits_v1_20261006.pdf`。
- [Singer author lectures](https://singer.math.ncsu.edu/papers/LMSlectures.pdf)，复用 `literature/singer2009_differential_galois_lms_author_20261006.pdf`；actual FULL PDF13–14、19–20，4页。Theorem1.3.9、Cor1.3.10、analytic monodromy inclusion 与 Proposition1.3.27。网页 open 本轮为 internal error，未把此当正常下载成功；使用的是已有完整本地 PDF。
- [Milne, corrected2022 author book](https://www.jmilne.org/math/Books/iAG2022.pdf)，复用 `literature/milne2022_algebraic_groups_author_20261006.pdf`；actual FULL physical PDF86、300、489–490，4页。对应 printed75、289、478–479 的 Cor3.35、Cor14.33、Prop22.41、Theorem22.42/Cor22.43。网页检索也核对 official2022原件；不依赖搜索中的非primary讨论。

本轮个人 primary actual reading 共12个 distinct PDF pages（4+4+4），无 render；第一次 PDF 输出遇 encoding error，未把失败输出计入阅读，随后用 UTF‑8 全页重新读完。全部 Casimir、finite-component、Q-descent 与 whole-jump 步骤为本文纸证；已有 primary 的 general theory 与本文具体模型推论明确区分。

可交付的新结论为 K12（真实 affine kernel 为全部V）、K14（已支付普通点后的独立 Kummer 因子）、K15/K1（整个 finite rational/tensor/jet 域内的相对解分类）、K22–K23（完整连接系数的精确限制）、K26（真正新 Green class 的必要 field escape）。仍未得到新的特殊值无理性、LI 或形式验证定理；也未对所有 possible motivic/Kummer-convolution constructions 给 universal no-go。
