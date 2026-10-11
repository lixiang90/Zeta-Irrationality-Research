# 真实 value-Gram 的 p⁵ 精度和四层非零门槛：独立审阅

2026-10-06，NEW，quarter_actual_rank。487 项基线及全部旧/同行数学 producer 只读；本文没有执行/import/rerun 任何同行或旧 producer。结论是 root 新稿的条件接口通过纸面独核；不是无限实际目标非零或新特殊值无理性证明。

## R1. 实际读取和指纹

完整无截断读取 [root 数学稿](cdt_odd_paired_value_gram_depth4_nonzero_20261006.md)，V1–V8、equations V1–V14，实际读取 SHA
`57f9aa8cb6335556399cb624316401f419b3174d8137ea3138e5ae2a51877ec7`。

完整静态读取其 [NEW source](cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.py)，SHA
`bc3a54157f1d36c892ecbbf1f4209737244ecdfe5533bec49da95e52b4e24785`；完整实际读取保存的 [JSON](cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.json)，SHA
`f50b9b63458365a81381d0ed4b6ef12c3a627a9e7782da815820a2764d348908`，全部 metadata、三个 original-S cases 的每个字段、全部 toys/ladder/p5 perturbation fields。没有运行 source，不称66037 assertions逐条人工重算。

本轮已完整回读冻结 e483 actual-unit-sector U1–U10/U1–U21 和 b953 weighted W1–W10/W1–W14；它们明确原 integer-valued 格、完整 S、split primitive constraints、ψ GL、actual node block。没有本轮新 primary PDF 阅读、下载或外部源码；不借 root 的阅读记录当成独审人已读。

## R2. 全 large-prime unit 节点的弱取值

实际检验 p>5、p²>8n、p≤6n 的整个域，包含 a=0、Q=0。factorial endpoints≤8n 保证权重仅有 carry2/3/5；unit residue为0≤ρ<min(r6+1,p−r2)，ρ0和余数等号正确。

真实 ψ basis 的 degree cutoff 给每个 residue local Φ degree≤Q。尾部 j=ρ+lp，l1..h 的 ψ-values互异，因为 h<p。h=floor6n/p≥2Q；Q≥1时 h≥Q+1；Q0时 p≤6n给h≥1。因此全部unit尾部 values为0迫Φ恒0，随后 scaled derivative、同residue的head value也为0。

这不是只知道 derivative 为0或一个 value 为0的推断。即使 top coefficient在多个residues共享，本步骤只用 degree 上界，故无需多给自由top。原 S 坐标上的 kernel向量用同坐标 exactlift，primitive paired equations保持准确，Z_p补基合法。

## R3. normalized X 系数没有丢两层 p

actual ∂_X B=24ΣW_jP(−j)Q(−j) 与 b953 W1一致。设 weak basis indices δ_i1、strong0。在unit节点，actual weak values均被p整除；nonunit W至少p²，而δ_i+δ_l≤2。故每个
\[
W_jP_i(-j)P_l(-j)/p^{\delta_i+\delta_l}\in Z_p
\]
逐项整，不需取值求和消去。实际 DND 整性另由 jet nodeblock 确保；它不能替代本 value-Gram 证明。两侧除Dp后仍有
\[
N_X=24p^5H,\quad H\in\operatorname{Mat}_{2n}(Z_p).
\]
因此冻结旧p³只是保守界，新p⁵精度成立，不假设未知 M5/G0 正常或actual anchor可逆。

## R4. whole-X constant reduction 的条件范围

对可逆 integral anchor N(c)，Smith最大指数≤4意味着 p⁵N(c)⁻¹的每个entry被p整除，不依赖eigenvalues。故
\[
\det N(X)/\det N(c)\in1+p(X-c)Z_p[X].
\]
这同时给全Z_p specialization非零、同valuation以及逐X系数的非零常数 reduction。原S与adaptedbasis间detτ是unit，det关系准确为
\[
\det N=p^{5d-2k}\tau^2D_A,
\]
所以 root V10中的指数5d−2k−t与unitτ⁻²都正确。允许signed rational scale；固定有理target必须避其有限分母例外。

阈值5 toy的 H=−diag(1,0)/24在p>5时integral，并准确使N(c+1) singular。它只说明p⁵一般扰动信息不能允许指数5，不是actual higherSmith反例。指数≤4尚未对本题无限子列证明；有限value-Gram的满秩不等于anchor N(c)满秩。

## R5. 四层 radical/Schur ladder

在p odd，symmetric modp form的非退化补空间可lift成unitblock A_j。仅对该已识别unitblock求逆，integral congruence给 A_j⊕pN^(j+1)；无未知Gram逆。递归Smith exponents每步加1，故r_j恰为original anchor中指数j的重数，k5=0准确等价anchor可逆且最大指数≤4。

当k5=0，t=Σj·r_j=Σ_{j=1}^4k_j正确。N(c)modp⁵足以决定stage0..4，各stage保留相应p^{5−j}精度；选择unit补块不改变最终指数重数。此algorithm明确了要证明的actual residual tests，不把algorithm存在当作其终止已证。single-bordered leading identity只识别k1，higherresidual还缺。

## R6. 静态有限机制与交付边界

source只import stdlib，exclusive-create输出先于数学运算，旧/同行数据读取0。root执行史按source/JSON记录FIRST1成功1、失败0、重跑0、66037checks；审阅人执行它0。

实际case r1/2/4只literal原S取值、primitivegcd和unit-tail value kernel，source未另外算scaled derivatives；R2的localΦ证明确保这个value kernel与定义的Hermite kernel相同。三个saved image ranks5/10/20、weak3/6/12、normalized value-Gram ranks8/16/32实际读到，root明确未计算actual anchor higherSmith。toy congruence例子是另一个一般symmetricmatrix；不拿其完美ladder当actual target证据。

结论：V1–V14的全尺度p⁵精度、depth≤4条件constant gate、无未知inverse的higher-layer接口通过独核，未发现数学修正项。它不提高n² paid预算，不改变原S实处费，也未完成无限nonzero或strict margin。本文NEW独审待最终数学稿pin确认后冻结，不改任何基线文件。
