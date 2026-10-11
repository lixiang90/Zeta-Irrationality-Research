# 原基部分 compound 与 mixed jets 的独立全文审阅

2026-10-07，NEW，审阅者 `/root/masked_racah_finalize`，作者 `/root/scaled_root_finalize`。实际 FULL 读取 `cdt_odd_paired_compound_mixed_jet_analytic_20261007.md` 的全部10节、A1–A27；审阅对象物理 SHA `9123629b3115383dc148dd76bfd638ea786df1899d66577af4dce6ca9937104f`。没有执行、import、rerun或创建任何数学 producer；不扩prime表，新增原始PDF/HTML下载及实际PDF读页均0。

## V1. 已实际全文读的输入与审阅范围

本轮实际 FULL 读 partial P1–P14（bece2d2f49def7809c5fe386e1bc247e31bd853d0aab3867b5f0ea28d2035866）、coupled C1–C23全部正文（03a4d165d6cc80027a81fb362aab559779fc22ea5122dc1a1ece1af27830c965）、lattice I1–I25（5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b）、local Gram G1–G15（2856a47ab3aa407f1eb7477a57e1e44bd010a7dd95b8cb055a603b68ea091094）、energy E1–E26（01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a）及 primitive-gcd G1–G13全部正文（77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2）。各输出均完整，无截断。

当前 main §§161–165实际读；audit f72fe28cbb874cedbb3e1e20b840d86f2ebd9e37ff7da1632364b9e04cb6729c完整JSONparse与header读域保留，不声称逐条人工全文审556冻结记录。γ≥1.455845引用已冻结 G11 的已审定理及严格包围，不重算它，也不宣称本轮静态全文重审其producer/JSON。下列新不等式则独立逐式纸核。

## V2. 原basis、uniform Stirling与纸面常数

A1中 β_m/primitive pair与lattice一致；低列准确的κ分母保留两个(j−1)!，高列准确除(2n+k)!。A2–A3保持原全部partial minors和同一positive Gram，不借top-det的rate或免费q剪切。

核A6–A10：Q、M0、M1来自同一实际W；旧energy证明两maximizers在(0,1)，故M1≤M0+log2。h''的Cauchy下界严格给h''<−8/3，在t0=3/2的强凹估计产生(3/8)log²(5/3)。展开Q(0)+2h(3/2)确为15log(5/4)+9log(3/2)−9log2。两组log/π有理界的方向正确；A10的13207/624750及high常数的1189/312375均为正余量。0log0、0!端点以及所有j的O(logn)一致误差有效。

## V3. 全部high和partial low的实际费用

A11的|h_k|²≤n^(2k)(1+y²)^k来自每个真实根v−1/2<n；W的4nlogn、高多项式的2klogn和实际factorial的−(4n+2k)logn准确相消。Q+tlog(1+y²)的共同指数尾保证uniform Laplace upper。放宽后括号对t导数为log2−2log(2+t)≤−log2，故A12对所有k有效；没有把稀疏high subset虚称连续Vandermonde。

独立核A13–A15：每个partial pair的两项展开在同一L²中triangle，2^ℓ只付O(n)；选点来自互不重叠的pair，全部δ不同且排序后δ_i≥i−1/2。Hardy ratio上界和log((1−u)/(1+u))≤−2u给精确有限惩罚ℓ(ℓ−1)(2ℓ−1)/(6n)，其主项为ℓ³/(3n)，剩余uniform O(n)。ℓ=0、1边界无遗漏。低weight与κ的nlogn相消后，A9确给(3/2)ℓn，而不是免费省basis增长。

A16中β_m≤b_m≤binom(7n,n)，entropy界及log7<2、6log(7/6)<1使logβ_m<3n。因此删除n−ℓ个pair确付6n(n−ℓ)，未将Γ按列数比例分摊。

## V4. 原6r全部子式的5.99主率

A17的low/high positive Fischer和Hadamard适用同一个P；合并系数准确为4ℓn−(17/2)dn+6n²−ℓ³/(3n)−2logΓ。其ℓ导数4n−ℓ²/n>0，于允许区间最大ℓ=n。全部principal minors的计数只付O(n)，从而A4成立。

d=3n/2的常数确为37/12。37/12+2·1.455845−599/100=1507/300000>0，因此A5的原全部mixed-coordinate minors保证rate>5.99有效。该数是已证衰减的保证下界，不是实际最佳衰减的upper；既存full-det rate>12.623不能搬入此对象。接本轮独立节点整模型的safe费用41仍未产生strict矛盾，未从安全费用upper推方法no-go。

## V5. 真实source斜率、mixed Andreief及互补minor

A18的24ΣWv vᵀ准确从原local G3的X项取出；W>0、原basis独立且degree<3n，在6n+1不同实节点上无非零共同kernel，故C SPD。A19将连续complex measure与离散positive source measure合并作全阶Andreief，每个t^k项取绝对值后由同一positive mixed measure给H_k，组合因子两侧相同。它确为coefficientwise upper。

A20由准确的互补mixed-minor展开、两个Hermitian/positive minor的Cauchy–Schwarz，再用sum层Cauchy–Schwarz得到；没有从pointwise Hadamard非法推系数不等式。实det1 q剪切同时作用P和C，保持整个全阶pencil和所有J_k；此事实不解除partial compound的inverse-shear费用。

## V6. 负node、互补Γ、weighted最大值与jet边界

A21–A22逐项核验：W≤2^(36n)，high value≤2^(9n)；Cardinal准确值为binom(j+2n,2n)·a binom(2n,a)/(j+a)，故≤2^(10n)；b_a≤2^(8n)给|β_mG_m|≤2^(18n+1)。于是C-high的54n和C-low的72n及24/96常数均安全。

A23的P-low与C-low恰覆盖每一个β_m一次，平方后准确为Γ_n^(−2)，无需A16再付删除费。其low/high损失Δ_L=72log2−3/2、Δ_H=54log2+17/2正确。Δ_L−Δ_H=18log2−10>0，固定k时对a的导数还增加(n−a)²/n，故k≤n最坏a=k,b=0；k>n最坏a=n,b=k−n。A24成立。

A25对全部系数同时支付τnk并取u,v∈[0,1]的maximum；分离v与u的函数正确。τ≥Δ_L+1使u=0、v=0最大，因此F=−1/3和A26成立。用weighted-det再控制H_k仍必须付回τnk。

A27在k=n/2代入A24的常数准确是36log2−187/24−2γ；它没有足够的负衰减保证。real symmetric B和SPD C的合同化确保det(B+tC)在0的零阶等于nullity；由冻结fixed-source∞rank≥3n/2得到∞多尺度某个k≤n/2非零。whole-X scale的每个Hasse系数可用固定M^(2n)支付，未直接移用partial尺度或把degree免费比例缩。

## V7. 结论与闭合状态

**PASS，无实质纠错请求。** 本文独立审阅认可A1–A27的全部新纸面推导、全尺度原6r解析保证及真实mixed-jet费用ledger；认可其未宣称strict margin、ζ/L/Catalan新无理性或LI/Lean。原有限处整模型和非零接口仍须按各自对象使用。

审稿实际全文写后回读、SHA核验后冻结；作者需实际全文收审后最终回读与单向FINAL receipt，不能以本审稿自动代替这些动作。不pin未来receipt，556旧记录不改。本审数学producer创建/执行/import/rerun0，newprime0，primary新页0，不继承同行的旧程序执行或原文页数。
