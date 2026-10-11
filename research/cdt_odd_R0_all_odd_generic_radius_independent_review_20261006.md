# Actual R0 全奇素数收敛与完整算术前缀：独立审阅

日期：2026-10-06。审阅者：toric_chow_completion。NEW 只读独审记录；所有旧/同行数学 MD、PY、JSON、manifest 未执行、import、重跑或修改。本记录依据实际全文阅读、原始文献阅读及纸面验算，不以作者运行记录代替证明。

## I1. 被审终稿与范围

实际完整阅读同轮新稿：

- research/cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.md，SHA256 **439a21b2bdf35eeffcbf46e016b35e6ad3b11b635baa8e4148d6533741f6dc5a**。全文 A1–A9，包括新增 A14a/A14b 的逐整数整除和 literal ε-columns，最后完整回读。
- literature/manifest_cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.json，SHA256 **775149ca7c34a3f80fedf8a0a59e65bfa08edf76273ce0562b0f42486aeccb88**，实际全文读。

作者的「Bhatt–de Jong 本轮实际读 PDF1–9」记录保持其原范围；本审阅者另外确实读完 PDF1–10，包括末页参考文献。不将我们的阅读范围改写进作者收据。

被审稿在明确输入 S2–S8、冻结 actual cohomological PF 和 root 全尺度 dyadic 结论之后，A2/A3 全 n 界、A12/A13 全部 prefix、A15 完整算术 holonomy 费用均通过独立核验。这里的解除条件只发生在本轮 NEW 接口，不修改冻结 S9/root D14 的历史条件段。

## I2. 原件实际阅读记录

1. Matthew Morrow，《A note on higher direct images in crystalline cohomology》，literature/morrow_higher_direct_images_crystalline_author_20261006.pdf，338397 bytes，12页，SHA256 **9d7bb24587a99edbdfa707c62c2590d0e469e931c937cb99fbe3f14af2f0c009**。本轮实际全文 PDF1–12。特别核 PDF2 Proposition2.1、PDF3–5 rational finite projectivity 与 Tor/isogeny、PDF6 Proposition3.2、PDF10 Proposition6.1、PDF11 Corollary6.2。原始作者链接：https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow%2C%20M.%2C%20Higher%20direct%20images%20in%20crystalline%20cohomology.pdf 。

2. Bhargav Bhatt、Aise Johan de Jong，《Crystalline cohomology and de Rham cohomology》，literature/bhatt_dejong2011_crystalline_derham_author_20261006.pdf，251479 bytes，10页，SHA256 **6c66ed20334f5ce8d96c9af9c0523d69c9f50f776b8b5169300b461f0558e669**。本轮实际全文 PDF1–10；先读1–2、6–10，再补全文3–5。特别核 PDF3 Lemma2.4、PDF4–6 Theorem2.12、Lemmas2.13–2.17、Example2.16、PDF8 Theorem3.6、PDF9 Corollary3.8、Corollary3.10 及 Tor 反例。原始作者链接：https://www.math.columbia.edu/~dejong/papers/crystalline-comparison.pdf 。

3. Fischler–Rivoal，《Denominators of the coefficients of G-functions》，literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf，12页，SHA256 **c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68**。本轮实际读 PDF6–8，末次再次读 PDF7–8 定理全部四条件、normalized Levelt factor 和 T(n) 的精确定义。一次 GBK stdout 在首行中断，随后 UTF-8 完整补读；不计中断为已读。PDF8 的估计确为所有 n≥0，T(0)=1，T(n)=p^{floor(log_p n)}。

4. Katz，《Travaux de Dwork》，literature/katz1972_travaux_de_dwork_author_20261006.pdf，35页，SHA256 **b885d13a652d87763c5864eb22238f0695613a3dab774507e2ba570a487eca1a**。本轮早段实际读 PDF23–24 §7；此前相关定义/收敛页的阅读沿用旧记录。本审阅不冒记重读作者本轮所列其余 Katz 页。§7 确有 de Rham locally free 假设；p>i 是随后 Mazur divisibility 的额外范围。新的 rational Morrow 路线替代该 integral 假设，而非删除原文假设。

未下载新 PDF；本审阅没有证书验证绕过。PDF提取、指纹和元数据读取只是来源处理，不属于数学 producer 执行。

## I3. 数学输入的真实范围

- 本审阅者自己完整撰写、回读并冻结 research/cdt_odd_R0_toric_odd_prime_smooth_model_20261006.md，SHA256 **bde766ee2c7825c9b7a3de7bb77ee4a2b42983a51ab2fc8f6bd28c9cb16e323d**。其 S2–S8 证明同一整数 fixed fan 下 proper smooth family 及全部奇素数/角点，不是 characteristic-zero smoothness 的类比。S9 保留当时尚未比较的条件范围。
- 本轮实际全文回读冻结 Yukawa 稿，SHA256 **172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15**；Y8a–Y10 是 actual compact cohomological Pω=0、cyclic rank4，而非一个 scalar period 的猜测。
- 本轮实际完整读 root 有效分母稿，SHA256 **fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8**；D1–D11 矩阵和递推已纸面核过。正式独审由 quarter 记录，本稿不重复新建该 theorem 的审计项，只使用其冻结结果并核新接口。
- 冻结 exterior 稿，SHA256 **b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef**，前轮已实际全文独审；本轮真实回读 E1–E3、E7/E7a、E10/E11，确认本轮 A7 使用实际 paired 四行和保留五行 mixed。
- 冻结 holonomy 稿，SHA256 **af728ecbebe3ac4827f7388706d4c5892896437e625e1bf4a0671b949bff28b5**，本轮已实际全文独审并保存另稿。species、τ、all-embedding 和 q=0 common-domain 限制沿用该证明。

## I4. Morrow 的准确条件：rational Tor 不可误作 integral free

对每个 odd p，S模型给 smooth base 与 proper smooth special-fibre morphism；可以在含 generic residue ξbar 的 perfect field 上 base change。Morrow Proposition2.1 的 rational higher direct image isocrystal、Proposition3.2 的 rational base change/Frobenius 和 Corollary6.2 的 convergent F-isocrystal 正好适用。

Morrow PDF4–5 实际通过 finite resolution、逆 p 后 projectivity、清 p 分母，处理 Tor 与 base-change obstruction。其结论未要求 integral crystalline torsion-free、integral de Rham 各 H^i locally free，也未要求 p>3。A2 没有从 rational finite projectivity 偷推出这些更强性质。

因此 p=3 的可能 integral torsion 不会阻断本轮 rational differential-module 收敛结论。这个理由也不能用于任何未逆 p 的整系数 comparison；本稿没有该声明。

## I5. relative-A comparison 的独立核验

Bhatt–de Jong 印刷 Theorem3.6/Corollary3.8 的底为 Σ=Spec Z_p，并未直接写本例 relative-A theorem。A3 明确把相对扩展当作本轮自证，范围正确。

取 p-complete formally smooth flat lift A/W(k)。在 smooth relative affine chart B/A，q次 self-intersection 的 p-completed PD hull D(q) 是 relative diagonal 的 PD polynomial extension；q=0 时 compatible canonical (p)-PD 已存在，D(0)=B。étale chart 由唯一 lifting 从 polynomial chart继承。smooth lifting 给 filtered union of PD objects 的 effective epimorphism，affine quasi-coherent acyclicity 和逐 p^e surjective transition 给 Čech–Alexander 计算与 R^1lim=0。

PD Poincaré 收缩使用 d z^[n+1]=z^[n]dz，逆向将 z^[n]dz 送到 z^[n+1]，不除 n；这是 p-adically bounded 的 module map。多变量 tensor、p-completion 与 relative forms 都保留它。BdJ Example2.16 的 cut-slot cosimplicial homotopy 是有限逐项组合公式，与系数底环无关；Lemmas2.15–2.17 的 exterior-power/coefficient-crystal 步骤因此在 relative-A 同样成立。两谱序列、étale/Zariski descent、有限 affine Čech 和 proper formal functions 给 A4 的 **derived** 比较。

这里比较先发生在复形层，再取 H^3、逆 p 并使用 Morrow 的 rational realization。未交换「取 integral H^3」与任意非平坦底变换，也未删除导出 Tor。因此 BdJ PDF9 Corollary3.10 的 torsion 警示不与该证明冲突。

A3 中连接的比较可以进一步在一阶底对角直接验算。以下说明也固定了其 I 的含义：I 是底对角 A(1)→A 的增广核；不是 canonical p-PD 理想。I/I^[2] 识别 Ω^1_{A/W}。

在 relative étale charts 选提升底导数 ∂t 的导子 D_i。一阶底对角 ε²=0 的 locally lifted transport 为 b↦b+εD_i(b)，对 forms 诱导 Lie_{D_i}。重叠上 D_i−D_j 是竖直向量场 V_ij，而 Cartan identity
\[
 \operatorname{Lie}_{V_{ij}}=d\,\iota_{V_{ij}}+\iota_{V_{ij}}\,d
\]
给同一 Čech–de Rham 复形中的 chain homotopy；这些重叠修正恰与 absolute Ω_{X/W} 按底 differential degree 过滤的连接映射一致。改变提升增加竖直 Cartan 同伦与 Čech coboundary，因此 cohomology 上差的算子唯一，正是 relative Gauss–Manin。

PD/Čech 比较对两底投影 functorial，故其一阶 stratification 的差与上述算子相同；晶体 cocycle 给 integrability。这补核了「是 actual GM」而非仅同秩 module，且没有调用 integral H^3 free。A3 通过。

## I6. actual cyclic sector、Kummer twist 和 generic radius

A4 的中心不是 t=0 退化点，而是 residue ξbar 超越的 generic disk t=ξ+s、|s|<1、|ξ|=|1−ξ|=1。convergent realization 的底对角 Taylor transport在该 disk 的每个 radius r<1 给中心归一化水平基本解；这只是 convergent 性，未声称 overconvergence。

sqrt x 在每个 odd p 上是 finite étale。相应局部 square root 的 binomial coefficients p-integral，半径至少1。因此 actual compact η 的 Kummer twist 同样 generic solvable。已证 cohomological cyclic rank4 的 scalar solutions 是该 module 的 dual；水平 trivialization 使 submodule/quotient 为中心 fibre 的固定子空间，故继承收敛。

characteristic-zero rational cohomological identity 张量 Q_p 即可使用，不要求 mirror degree-one maps 有独立的每素数整模型。这里 good-reduction 几何来自本轮 S模型的 actual X。

rational comparison gauge 的分母去除固定 p 幂后 reduction 非零，ξbar 超越使它在整 generic residue disk 无零；determinant 同理，故 gauge/inverse analytic。若写在 sqrt cover 中，取对应 finite étale residue extension；非零函数仍在 generic point 非零，论证相同。固定 p 幂改变 norm/lattice，不改变 radius。因此 exact G4 满足 FR(iv)。其 G4 矩阵在 Z[1/2]、仅 t=1 有非零有限 pole、nilpotent residue 也确实支付 FR(i)–(iii)。

## I7. source h 必须另付 μ5，但 generic radius 可自证

A5 的 exact G5 是已冻结 source u=w^(-7/2) extension。手核 trace(G4/t)=6/w，所以 normalized detY4=((1−ξ)/(1−ξ−s))^6 无零，Y4逆矩阵收敛半径至少1。u 的 normalized binomial factor同样在每 odd p收敛。

变分常数上右块的积分 integrand 是 Y4^{-1}(0,0,1,ξ+z)^T U1(z)/16。若其系数 a_n 的 limsup |a_n|_p^(1/n)≤1，积分系数 a_n/(n+1) 仍满足该式，因为 |n+1|_p^{-1} 的 n次根趋1。故 normalized G5 fundamental matrix收敛半径至少1；它不依赖 normal function 的 integral Frobenius，也不把源 h 当 homogeneous rank4 解。A5 通过。

## I8. FR 的精确小素数与整初值

FR PDF7 的四条件已逐项支付；PDF8 的 bound 是 normalized holomorphic Levelt factor U(t)、U(0)=I 的全 n 界。G4/G5 residue square-zero，actual 初值向量都在 residue kernel，因此 U(t)乘该向量确实给无 log solution。

- μ4：Π_j binom(4,j)=96。p=3 的指数为3+1+1=5；p≥5 为3。于是 g 的 odd-LCM baseline3另付 3^{2 floor(log_3 n)}。
- μ5：Π_j binom(5,j)=2500。p=3 指数4+1+0=5；p=5 为4+0+4=8；p≥7 为4。于是 h 的 baseline4另付 3^{floor(log_3 n)}5^{4 floor(log_5 n)}。
- G4 三 holomorphic 初值为(1,0,0,0)、(0,1,0,0)、(0,0,2,0)；G5源初值(0,0,0,0,1)。均整且在 residue kernel，没有额外未付 shearing factor。

结合所有 rational c_n 的 dyadic 界，对所有有限素数 integral，便给 A2/A3 全 n 整数界。n=0 按 T(0)=1 处理正确。

## I9. 实际 paired 前缀、固定 B25 与 p3 polynomial4

原 four Z 的公式使用 F_i=−1/16∫g_i/√w 和两 g jets，五 mixed 使用 √w乘实际保留 minors。没有换成未证明 rank 的更便宜 packet，亦没有将 Betti constants 塞进 coefficients。θ_x^j 的固定三阶 jet只有整组合和有限 index shift，两因子最大总 shift6。

odd-LCM 次数：F_i 的一次 integration 从3升到4，Z乘 g 得7；mixed gg 得6。两 g 的额外 p3 polynomial费用合计 exponent4。故统一 P3(N)=3^{4 floor(log_3(N+6))} 必须保留，不能把它无条件视作 n^4 的整除因子。

dyadic b 的 superadditivity 手核如下：b(a+b)−b(a)−b(b)=2v2 binom(a+b,a)−c，c∈{0,1}；c=1 恰 a,b均 odd，此时 binomial even。sqrt coefficient 费用2n受 b(n)覆盖；积分除 n及16由 b增量与 fixed2^4安全覆盖。所以 b(n+6)+4≤(7/2)n+25≤4n+25，B25 足够。共同使用 D_{N+6} 含2只再增保守费用，不危害结论。

因此对全部 N≥0、全部 0≤n≤N 和全部 number-field places，A12/A13 的 **16^N** 完整 prefix通过；并非先有逐项 16^n 后假定无需共同分母。fixed d0仅清 q；packet 本身无需 h 的 μ5 bounds。A3 保持独立正结果。

## I10. ε 转换是 literal arithmetic hypothesis，不能把费用口头删去

独立核 A14a 的逐整数整除。若 n≥2/ε，floor(εn)≥εn/2 且 n+6≤7n，所需3-adic floorlog差至多 ceil(log_3(14/ε))；较小 n 由同一固定3幂覆盖，D0=1。这里比较的是 3-adic exponent，未使用错误的「P3|n^4」。

n≥6/ε 时 n+6≤floor((1+ε)n)，故 D_{n+6} 整除后一 LCM；有限余项由固定 D_{ceil(6/ε)+6}^7清。fixed dε对于每个 ε 保持与 Taylor degree无关。

于是六个 nonconstant cutoff1、一个 pure cutoff6 的原species付 b=1+ε，四个新增 nonconstant cutoff1付 b=ε。其
\[
 \tau_\varepsilon=(1+\varepsilon)\frac{329}{50}
                   +4\varepsilon\left(1-\frac1{100}\right)
\]
确实趋 τ=329/50。系数改为 f_i(16s)只在全部 places同步支付 rational scale16；fixed2^25d0dε不产生 degree平方主项。

对 strict L>τ先选 ε使 L>τε，再逐 ε应用 literal theorem/相应 all-place proof并取极限。因此 A15 不以忽略 P3来套原定理。作者另一种 lattice perturbation解释的 O(D logD)与此独立整除证明一致；本审阅通过 literal ε路线，不需依赖未量化误差的宣称。

## I11. 通过结论与剩余缺口

通过范围是：

1. 本轮实际 proper smooth全奇素数模型与 rational convergent crystalline 的比较，给 **actual G4/G5 在全部奇素数 generic radius至少1**。
2. A2/A3 所列 homogeneous/source **全 n** 整数界，包括 p=3,5 费用。
3. actual九行 complete prefix **C16、fixed B25、P3(N)**，以及支付其全部费用后的 τ=329/50 量化 holonomy接口。
4. 没有要求 integral crystalline H^3无挠或 locally free；没有为 normal function凭空添加 integral Frobenius。

这真正关闭冻结稿中「odd-prime generic radius未核」的接口，但没有证明特殊值无理性。相同完整模型仍适用于 q=0 的 actual rank10 rational reference，故共同 analytic domain不能区分目标 q。目标 q=π²(R0−M0)/16 的代数性也不等价于 R0−M0 的无理性。未给出新ζ奇数值、卡塔兰常数的无理性/线性无关性结论或任何 Lean verification。

本 NEW审阅文稿实际全文回读后冻结。数学 producer执行数0；所有旧/同行producer执行/import/rerun数0。

