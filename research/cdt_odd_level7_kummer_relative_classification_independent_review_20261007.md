# Level 7 完整 PV–Kummer 域分类：独立纸证复核

日期：2026-10-07。复核者：`/root`。被审主稿：`research/cdt_odd_level7_kummer_relative_classification_20261007.md`，作者 `/root/source_pencil_finalize`，本次 actual FULL 读取 SHA `bec6b922b3fabd9e424c88329c8111bf3656f4da2c23faff9fadbfb197dd1148`，18785bytes，八节 K1–K27。authority仍为612 frozen 的 `cdt_odd_delivery_paired_anti_modular_slopes_20261007.json`，旧稿只读。数学 producer 新建／执行／导入／重跑、prime 扩表与 Lean 均0。本 review 为独立推导核查，不只是 hash 或摘要阅读。

## V1. 实际输入、齐次群和 rational splitting

逐式核 K2、K5 的 Euler/ordinary coefficients：`p₁/p₂=(1−42t)/(t(1−28t))=1/t−14/(1−28t)`，所以 K8 的 `W=1/(t√(1−28t))` 与 `S=A log t+η` 的 `W~1/t` normalization一致。有限点 indicial没有负整数root，rational particular不能在普通点或0、σ、1有pole。positive degree d 的 `LT` leading项确为 `−14d(2d+1)t^(d+3)`；constant给 `L1=−2t−4t²`，不可能等于 `r_B=t−t²`。齐次 rational kernel也为0。K11通过。

实际 level 7 modular basis和noncommutingunipotents由被冻结M稿付清；本次actual FULL重读M1–M25，并核Yang原件PDF5–6、15–16。Wronskian algebraic只限制connecteddeterminant，主稿保留fullgroup finitecomponents。regular-singular条件与SingerPDF19–20Schlesinger吻合，故 `G_h⁰=SL₂`。未把abstractsymplecticrank替代真monodromy。

## V2. affine kernel不是未经证明的假设

PV restriction onto homogeneous field surjective；closed translationkernelN是V的algebraicsubgroup，char0 additive subgroup为vectorsubspace；SL₂ irreducibility只留下0或V。若N=0，restrictionclosedimmersion且surjective成为groupisomorphism，connectedgroupsemisimple。三维stablemodule `V+CB` 的trivialquotient有invariantliftT；`LT=r_B`。所有fullcomponentdifference `gT−T∈V` 仍被identitycomponent固定，因 `V^SL₂=0` 必为0；T因此是fullPVfixedfield的rationalfunction，矛盾V1。此处必须处理finitecomponents，主稿确已处理。

于是N=V；对每个homogeneousgroup元素，先选lift再减其Btranslation，实际包含block-diagonalcopy，`G_B=V⋊G_h`。K12通过。这里没有把nonreductiveaffinegroup整体当成completelyreduciblegroup。

## V3. ordinary µ确实支付独立 Kummer 因子

`µ=−1/28` 对原二阶方程及rB系统ordinary。完整jets均被其local loop固定，只有ℓ增2πi。其integerpowers在Ga中Zariskidense，给 `1×Ga`；PVrestrictiononto G_B再给wholeproduct。K13–K14严谨，并非只凭ℓ(σ)=log2声称independence。这个Ga动作是函数层面的，不蕴含κ与log2数值独立。

## V4. 全部 rational/tensor/jet expression 分类

对F∈E且LF∈C(t)，automorphismdifference落在固定二维V，所以 `W_F=V+CF` 是dimension≤3的stablealgebraicrepresentation。PVfield上的finite-dimensionalstable空间确给rationalrepresentation，grouptranslation消去可能局部matrixcoefficientpole；作为finite representation可使用Lieaction。若F∈V直接处理，余下trivialquotientdimension1。

亲核Casimir `h²+2h+4fe`：在standardbasis，h=diag(1,−1)，fe=diag(0,1)，故为3I；在trivialquotient为0，并与e、f、h commute。其image在V，`C²=3C`；`F₀=(1−C/3)F` 给H-invariantlift。只在H=SL₂上用该split，逻辑正确。

Ga与H commute且固定V，因此 `aF₀−F₀∈V^H=0`。对N=V，`n↦nF₀−F₀` 是additivealgebraichomomorphism，char0下C-linear；H-equivariance迫它为dI（torus和上下unipotents直接核）。所以 `F₀−dB` 被G⁰固定。fullcomponentdifference仍在V且G⁰fixed，消为0，fixedfield得T∈C(t)。K15完成。论证确覆盖finite rationaldenominators、tensorproducts及fixedjets；不涵盖新Greenintegration，scope明示正确。

## V5. Q下降不是抽象常数猜想

从 `LT+d r_B=r∈Q(t)`，若有两组solutionpair，差给rB rationalparticular或rationalhomogeneous，均被V1排除，所以唯一。实际T只在Q-definedfinitepole集合 `zeros(p₂)∪poles(r)` 有pole；选足够大的fixedM,N使它落在Q-basis `{t^j/(a p₂)^M}` 的finiteC-span。cleardenominator后是有限Q-affinelinearsystem，complexsolution存在便有Qsolution；uniqueness识别实际T,d。无需算法执行，也不需要预知polebound的有效数值。

0的homogeneousgerm只有analyticlineCA和logarithmicline；它们没有pole。F、B holomorphic，故T不能在0有pole；v因此为cA，constantterm给c∈Q。K1、K21完整下降通过。没有把arbitrarycomplexhomogeneousnormalization默认为Q。

## V6. whole jump、integrality及具体反例

Tsingle-valuedmeromorphic无branchjump；E3wholegerm relation给K22。`ψ≠0`使desiredcoefficientlog2等价K23，而不是一次independentconstruction。主稿准确保留 `1,κ,log2` 数值LI未证；分别超越不能推它。

polynomialT、Ainteger、BD_n²cap合并成fixedmultipliercap正确。rationalgauge `1/(2−t)−1/2` 的coeffdenominator2^(n+1)，与D_n²的2-adicexponent2floor(log₂n)相比明确exponential不足，K24为真正反例。它不意味着这种gauge不可使用，而意味着必须另付算术／coordinate／endpoint费用。

## V7. 新 Green 接口的范围

Wronskian variation符号为 `−A∫S r/(p₂W)+S∫A r/(p₂W)`，K25正确。r∈tQ[[t]]使q_ranalytic于0；twointegrals的logs在bilinearcombination中消去，normalzero和Q-coefficientrecurrence成立。若forcing不在 `L(Q(t))+Q rB`，classification迫newC_r不在旧E_B(ℓ)，K26是真fieldescapegate。反向需zero-normalizedanalyticgerm存在，主稿有该条件。`q_r=1/(t+a)` toyforcing确多一个√(1−28t)，不能免费算rational，K27准确。

## V8. 实际原件、阅读域与最终 verdict

本次actual FULL读取主稿全部K1–K27、冻结M1–M25全部八节；currentprogress只读取header/§§196–200。复核者root本轮主研究已实际FULLYang PDF5–6、15–16与CDT66–69，未重复计freshpages。为本review新actualFULL以下existingprimary8 distinctpages，documentaryextraction完整输出，无render：

- Singer authorlecture，`literature/singer2009_differential_galois_lms_author_20261006.pdf`，PDF13–14、19–20：Theorem1.3.9、Cor1.3.10、analyticmonodromyinclusion、Prop1.3.27。[primary](https://singer.math.ncsu.edu/papers/LMSlectures.pdf)
- Milne corrected2022 authorbook，`literature/milne2022_algebraic_groups_author_20261006.pdf`，physicalPDF86、300、489–490：Cor3.35、Cor14.33、Prop22.41、Th22.42/Cor22.43。[primary](https://www.jmilne.org/math/Books/iAG2022.pdf)

因此root截至本reviewactualfreshprimary25distinctpages =主研究17+review新增8；主稿作者source自身12pages另记，不能与root混为一个阅读receipt。source既有archive无需新下载；本review不增PDF。

**Verdict：通过。** 无数学修改请求。新结果是整个真实有限PV–Kummerfield的same-Lrelativeclassification、fullGa支付和Q下降，不是特殊值无理性或LI theorem。不得扩张为所有motivicnormalfunctions／convolutions的no-go。B₃之类新Greenclass若在该forcingimage之外，恰是允许的逃逸，不与本classification冲突。此review与被审主稿后续作者finalFULL回读、物理SHA核对共同形成交付，不称本review执行了旧612项的全历史proofaudit。
