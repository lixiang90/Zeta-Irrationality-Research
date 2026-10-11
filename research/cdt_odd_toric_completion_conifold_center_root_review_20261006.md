# Toric completion 与 conifold 算术中心的 root 核读收尾

日期：2026-10-06。NEW 审阅与交付范围记录。本文独立核几何作者稿；对 root 自己的 conifold 稿，独审由 quarter_actual_rank 单列，本文不冒认自审为独审。仍无新的数值无理性、线性无关性或 Lean 定理。

## G1. 全局几何与 boundary strata

root 实际全文读 [toric completion](cdt_odd_R0_toric_completion_20261006.md) 初稿，再全文回读补强的 §§1–9。严格区分此前 all-divisorial field tame vanishing 与本轮实际 CH⁴ completion。

φ 的 divisor 是2Σ[-1]−Σ([0]+[∞])，S 是(P1)⁴的split三点网格。graph blowup 的局部 ideal 为(z^e+,z^e−)，unit 不改变 ideal；normalized graph 的 cones 经 ℓ=0 切开后 map 已 regular。进一步 projective toroidal regular subdivision 始终使用原整数 lattice，且 refinement 留在已有 half-cone 内，故不会重新引入 map indeterminacy。所引用 Ab–de Jong Thm0.4 确是 strict toroidal resolution；没有使用 arbitrary resolution，亦未用 KKMSIII 允许更改 denominator 的 Theorem4.1 冒充 fixed-lattice 结论。

每个 fixed-grid stratum 用一个全局参数 chart 覆盖完整 U^(4−s)，monomial modification 是 toric modification ×U^(4−s)。cone 的 minimum support 迫每个 fixed z_i 在该 orbit 上为0，因此 chart 删除的非零点不会删掉 orbit。这个论证足以给全局 product，而非仅 étale torus bundle。horizontal cone 的 interior vector 同时有正/负 e，使 s≥2；spanτ⊂kerℓ给r≤s−1。因而实际 strata 恰为
\[
 U^{4-s}\times\mathbf G_m^{s-r},\qquad
 D^{2,*}\text{ 的 components 为 }U\times\mathbf G_m\text{ 或 }\mathbf G_m^2.
\]
ℓ 中至少一个−1 coefficient，故 quotient character primitive；不存在要开平方的 λ-cover。f 在 boundary strata 上是一个 split torus coordinate，故 smooth；torus interior 的唯一 critical point 为v_j=1、λ=256。新模型总空间光滑，f proper，所有 λ∈Gm\{256} 的 fibre 光滑；这没有构造 singular fibre 的 integral specialization。

## G2. 真正 CH residue 与实际 d₂ 消失

每个 horizontal divisor 的 original center 含某 v_j=−1；v_j 在含整个 divisor 的一个 neighborhood 上为 regular unit。localization 的 product compatibility 将整 stratum residue 写成 {-1} times 其它 residue，在 rational CH 中为零。因此 d₁=0 发生在 CH³(E°,3)，而不只是 generic function field 的 Milnor K₃。

root 独立给出本文所需的低权 vanishing，不依赖未实际读到的任意 smooth Z 的 general CH¹ theorem：

* DK出版 PDF26 说明 field Beilinson–Soulé vanishing 对 n≤3 已知，给 CH¹(Q,2)=CH¹(Q,3)=0（均 rational）；CH⁰(Q,q>0)=0 也可直接从 normalized codimension-zero cycle complex 得到。
* projective bundle 公式给 CH¹(P1,2/3)=0。删有限 rational points 的 localization 右端为 CH⁰(Q,1/2)=0，所以对 A=U 或Gm，CH¹(A,2)=CH¹(A,3)=0。
* DK 同页 Borel/Suslin 给 CH²(Q,3)_Q=0。先在 Z=SpecQ，再在 Z=U 或Gm 上分别应用 projective bundle 加 localization：CH²(Z×P1,3)=CH²(Z,3)⊕CH¹(Z,3)，右端 residue 是若干 CH¹(Z,2)。两项都零。因此 CH²(U×Gm,3)=CH²(Gm²,3)=0。

DK PDF29 的 general spectral sequence 对 ξ∈CH⁴(Y*,4) 的 d_r target 是 CH^(4−r)(D^{r,*},3) 的 subquotient；r=2 的 group 本身零，r=3 的 Gm components 的 CH¹(...,3) 零，r=4 无 horizontal stratum。故 ξ survive 到 E∞，严格给
\[
 \boxed{\exists\Xi\in CH^4(Y,4)_\mathbf Q,
 \qquad \Xi|_{Y^*}=\{v_0,v_1,v_2,v_3\}.}
\]
这是 existence proof，不是已写完 boundary precycle 的显式 chain-level representative；rational lift 也不是 integral saturation 已完成。

## G3. 一手页码的实际 root 核读

本轮 root 实际提取阅读 DK PDF25–29，确认 symbol graph、localization、Borel/Suslin和每个 d_r target；另读 PDF79–80，确认 Lemma4.1 的 published版本只陈述ℓ=2,3，不能直接消去本例ℓ=4、非regular boundary的current问题。Ab–de Jong原件实际读 PDF2–3，Thm0.4在PDF3；不声称 root 实际读到 KKMSII p94。

Levine原始87页 PDF 的 projective bundle Cor5.4 位于 PDF84–85（印刷317–318）。root 使用 Poppler 渲染并实际视觉阅读两页，确认对smooth quasi-projective X与 rank2 trivial bundle，CH^q(X×P1,p)_Q=CH^q(X,p)_Q⊕CH^(q−1)(X,p)_Q。两张原页图保存在 [PDF84](artifacts/cdt_odd_toric_center_root_review_20261006/levine-84.png) 与 [PDF85](artifacts/cdt_odd_toric_center_root_review_20261006/levine-85.png)。Poppler报告两条display-font警告，但实际图像文本和公式可读；不把工具警告视为数学结论。

KKMSIII原件的视读由几何作者记录；root只读manifest/哈希而未认领全部scan页的视觉阅读。可选的一般motivic weight-one文献和背景文献以各代理实际阅读范围登记，不扩大为本root核读。

## G4. 新中心与执行边界

root 的 [conifold arithmetic center](cdt_odd_conifold_arithmetic_center_20261006.md) 由 [独立全文审阅](cdt_odd_conifold_arithmetic_center_independent_review_20261006.md) 核准。root 实际全文回读独审 §§1–5，特别是 finite Qbar log-cancellation constraints 定义四维holomorphic G-subspace，再用(c0,c1,c2,β) Qbar初值矩阵规范化；无超越 connection coefficients 被偷换为代数常数。

三个实际 jets α0,α1,α2均属于某 number field 的条件下，geometric L=(θ−1/2)P，μ=5、b=1 给 D_(n+b0)^4 C^(n+1) 整化。P 的conifold indicial为ρ(ρ−1)²(ρ−2)，L多一根3；不是regular ordinary point。fixed bad-prime support 的 C^(n+1) 是真实指数成本，最小 C尚未有效计算。单个endpoint α0代数或有理不足以得到三个jets的条件。

root只首次运行自己的 NEW symbolic verifier，operator/indicial/五个 all-symbolic-n recurrence coefficients 和首项通过。mixed arithmetic 的52项由作者首次执行，root实际读PY/JSON，未重跑；其全尺度 proof/费用另见 [root quarter审阅](cdt_odd_quarter_actual_rank_mixed_independent_review_20261006.md)。本轮其它数学 producer 均未执行/import。来源审计只读/哈希，不计为数学producer或证明。

## G5. 仍需继续的两个具体比较

1. 由实际 regulator current 计算 ∇AJ，处理 boundary-supported lift ambiguity、compact pure-sector projection和Tate factors，再与8C−TΓ比较。几何稿候选 ∇θAJ=−16√x[ω] 有明确问号，root实际原页核读后保留问号；没有认定其conifold special value已经为R0−M0。
2. 在三个jet条件下的新算术中心，推导good-prime block和最小坏素数C，计算真正标记周期的解析稳定子/叶与相应全place费用。actual rank19和quarter新费用已经核证，但现有预算无数值矛盾；不能以更大函数数或motivicity自动推出独立性。

本轮分类为实质进展；goal保持active，新的奇ζ/L/Catalan数值定理仍未完成。
