# 原混合jet节点熵稿：实际全文独立纸面审阅

2026-10-07，审阅者 /root/masked_racah_finalize。被审最终候选为 research/cdt_odd_paired_mixed_node_entropy_20261007.md，SHA256 f0216126342b46e507e172f422f8e3adee3832f95691cb040dbfed94fd1c4bf8。实际FULL读取全部10节、S1–S27，并逐式检查下列证明。结论：在本文明确的原格、原源、正Gram包络范围内通过；无数学修改请求。未创建、执行、导入或重跑数学producer，未扩prime表，新增原始PDF实际读页0。

## V1. 实际输入读域与对象一致性

本轮实际全文读取冻结 A1–A27、H1–H17、lattice I1–I25、actual-local G1–G15、coupled C1–C23、energy E1–E26、primitive-gcd G1–G13，分别对应：

| 冻结输入 | SHA256 |
|---|---|
| cdt_odd_paired_compound_mixed_jet_analytic_20261007.md | 9123629b3115383dc148dd76bfd638ea786df1899d66577af4dce6ca9937104f |
| cdt_odd_paired_hasse_jet_mixed_gram_20261007.md | c178bf8540ff8a0697260ff3d5d137039d92b6288affc29f432934b100704112 |
| cdt_odd_paired_head_free_integral_lattice_20261006.md | 5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b |
| cdt_odd_paired_actual_local_gram_layers_20261006.md | 2856a47ab3aa407f1eb7477a57e1e44bd010a7dd95b8cb055a603b68ea091094 |
| cdt_odd_paired_coupled_gram_decay_20261007.md | 03a4d165d6cc80027a81fb362aab559779fc22ea5122dc1a1ece1af27830c965 |
| cdt_odd_paired_plucker_energy_rate_20261006.md | 01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a |
| cdt_odd_paired_primitive_gcd_rate_20261006.md | 77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2 |

上述7份文件本轮物理SHA复核一致。总稿读域为 §§166–170；audit hasse_bridge 完整JSONparse及头部/字段检查，不冒称逐条人工全文阅读或本人对564记录全量物理复核。G11的γ下界作为冻结纸稿输入使用，不把其旧数值认证视作本轮运行。

S1–S3严格保留 rank2n、degree<3n 的原饱和整数值基，以及同一原 continuous-total-variation Gram P 和整数离散斜率 V。J为原 B_n(ξ+t)的系数，H为同基正包络 det(P+tV)的系数。冻结H13/A19的 |J|≤H 在此对象上使用正确。

## V2. 全节点熵与有理常数

S7的binomial entropy界由二项分布单项≤1得到，0和端点亦成立；E对第二变量非降，故i<3n的全部high斜率对角元受K3控制，无丢弃j=0或j=6n。

独立求导得到S9的 F''<−2/(6−x)−2/x≤−4/3，唯一内部最大及二次上包络正确。S10有限正项尾界能够给S11各个有理夹界：log2用z=1/3三项，log(3/2)用z=1/5两项，log(5/4)用z=1/9两项，其余首项及几何尾。S12两项精确展开与各自导数系数均核对。导数范围(−2/5,0)、(−1/10,0)和3/8平方修正分别给K2<1612633/60000、K3<11557/400。所有常数只是有限有理纸核，无采样sup或新认证程序。

## V3. 左Hardy点值、Loewner与原low

S14保留准确cardinal/κ及β。F在左闭半平面无pole且O(1/z)，左半圆Cauchy公式的直线方向给S15的1/(2π)；核的L²平方积分为π/(j+1/2)，故点值系数恰1/[4π(j+1/2)]。弧上integrand为O(|z|⁻²)，j=0同样适用。

乘真实ω_j并对有限j求和，直接给同基Hermitian Loewner S17。不存在把离散测度免费替换成连续测度的步骤。S18中 |S(−j)|=(2n)!binom(j+2n,2n)，(2n)!²、全W_j及节点数均保留；4nlogn项正确。

每个pair选择中的heads互异，左距离排序δ_i≥i−1/2。准确Cauchy determinant的每个两两因子为[(δ_j−δ_i)/(δ_j+δ_i)]²。置r=δ_i/δ_j∈(0,1)，有2log((1−r)/(1+r))≤−4r≤−2δ_i/n，其中δ_j≤2n。又Σ_(i<j)δ_i≥Σ_(i=1)^(a−1)(a−i)(i−1/2)=a(a−1)(2a−1)/12，故两两因子之和≤−a(a−1)(2a−1)/(6n)，给S19准确系数。对a=0,1也有效；有限pair选择只产生O(n)。由determinant monotonicity、κ的uniform Stirling与R_n^a相消n²logn，得到S20中的 −a³/(3n)，以及恰该low subset的 −2Σlogβ，没有删除头部阶乘或源费用。此处已按root独审提示澄清精确不等式；先前仅写log(1−u²)的缩略解释不足以单独推出该系数，主稿S19本身不变。

## V4. 必要的真实常数排序

S21沿冻结强凹head估计，系数11、15、−3和3/8均正确；S11给2g*<295919/30000<10，继而Λ<2204471/60000<37。

关键S22比较的是实际K2、K3和g*，不是相减两个独立upper。F2'(4)=log(243/128)>0，严格凹保证最大点x2>4；因此K3−K2>2log2。结合2g*<10得
δH−(δL+1)>2log2−1>0。这个严格排序确实使本稿包络中source-high成为较昂贵的分配方向。

## V5. 混合系数、互补Γ和全部κ

S23使用同基positive Gram的准确mixed-minor上界。I的source-low/high数a,b对应P互补中的n−a,n−b，冻结A15/A12与S8/S20给S24各项的系数。两侧low subsets互补，β平方覆盖全部pairs恰一次；原high factorial保留。组合数及平方根求和后平方只增O(n)。

展开 [(n−a)³+a³]/(3n)=n²/3−na+a²，可重新得到S24的base −22n²/3、(δL+1)an−a²与δHbn。固定k的a导数是n(δL+1−δH)−2a<0，所以k≤n的最大上包络分配a=0；k>n则a=k−n。S4与S25均包括k=0,n,2n边界，且仅是安全上界，不声称实际最大minor达到它。

S26的全u,v方形最大化给φ分段函数及正部项。提取k≤κn必须支付τκn²。κ∈[0,1]下τ<δH区间的目标非增，τ≥δH时φ为0、目标非减，故包络可在τ=δH取付费最优。该结论没有提升为实际谱、真实Ψ或通用方法的最优性。

## V6. 改善幅度与结论边界

κ=1/2时由S4得到Θ/2−37/12−2γ，S13严格给27271/2400−2γ。用冻结γ≥291169/200000，最后与1691/200之差为283/75000，S5核对通过。对旧A27同对象upper的严格减少69521/12000>5.79亦通过。

本文并未给负的充分衰减，也未跨完整finite-place费用；没有把k=0更强whole-determinant upper免费搬到k>0，没有使用partial41作为jet费用。算术κ-profile尚需独立审阅后方能合并。此稿不产生新的ζ/L/Catalan无理性、线性无关性或Lean结论。

## V7. 最终审阅状态

全部S1–S27在明确scope内通过，无修改请求。审阅结论基于本轮实际FULL读取和逐式纸面检查，不继承别人读取原始PDF的页数或旧producer运行。新增数学producer创建/执行/导入/重跑0，prime扩表0，新增PDF/HTML/code下载0，新增原始PDF实际读页0。作者还需收审后最终全文回读及独立单向FINAL收据；此review不预先宣称作者闭合完成。
