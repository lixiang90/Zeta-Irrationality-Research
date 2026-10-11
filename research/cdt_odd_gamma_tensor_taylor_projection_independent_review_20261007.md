# Gamma 二次 Taylor 周期主稿的独立全文纸面审阅

2026-10-07，审阅者 /root/source_pencil_finalize。对象为 `research/cdt_odd_gamma_tensor_taylor_projection_20261007.md`，作者最终候选 SHA256 `0a9eb062f5ca02f3337a9532457a01b6b8904e064b2ff1ebf187b302388adc9e`，18617 bytes。本人实际 FULL 阅读该指纹的全部十节、T1–T28、两张完整表及证据边界，另阅读全文冻结 Gamma G1–G19/period E1–E24。结论 **PASS；没有正文修订请求**。这表示下面纸面证明通过审查，不是 Lean 或新数值无理性证书。

旧588记录、旧及同行数学 producer、guards、prime表只读；本审阅没有创建/执行/import/rerun数学producer、数学失败、prime扩表或Lean。PDF文本读取和SHA不算数学producer。

## R1. Skew-adjoint、实际 Frobenius form 与零 scalar metric

T4 的次序正确：对 dt/t，D*=-D；移动 t 后是 P(−D−1)，不是 P(−D)。a↦1−a、r奇数给 L*=-L。T5 逐summand求D的相邻抵消严证 D C_L=fLg−gL*f。平均后仍给相同 identity，因此 T6 的对称 pairing 确实 constant on solutions。

jet form 高于 i+j=r−1 的 entries 为0；anti-diagonal 为(−1)^i(1−Λt)。反转 permutation 的sign与各(−1)^i乘积相消，得 detS=(1−Λt)^r，不遗落sign。t→0时实际 φ_j 的 log-polynomial basis给 exp(logt N)，满足 NᵀJ+JN=0。所有 correction是t乘有限log幂，故 YᵀSY=J，而不是一个未知 comparison form。

由YJYᵀ=S−1，S的末row仅有S_(r−1,0)=1−Λt，故(S−1)00=0；T9的零 contraction成立。T10的含derivative contraction则是具体Q(t) rows，未被误称全部恒零。此处“orthogonal invariant”为 formal metric tensor；其scalar evaluation为0，不能拿 formal invariant维数当新的functionrank。

## R2. 完整反射列及全部 normalization

反射−1 eigenline与+1 hyperplane kerκ正交，J非退化，故 Jw∥κ。以κᵀw=−2固定scale后得w=−2Jκ/(κᵀJκ)。同一推导也保证分母非零。本人以当前实际rank9 Γeven项独核：κᵀJκ=16π8/5=(2πi)8/80，故T14的−160/q8准确，与本轮另行Green推导的−5/(8π8)相同。

rank3 κ2=−3ζ2，K2=−6ζ2=q2/4；rank5 κ2=−5ζ2、κ3=10ζ3、κ4=55ζ4/4，K4=2κ4+κ2²=90ζ4=q4/16。所有低权列的scale/sign准确。三组Γ公式均为整数坐标中已支付Λ−s后的式子。κ5/κ7的数值假设没有改变T1的monodromy parameters。

本人本轮实际 FULL读Bloch–Vlasenko v2 PDF15–20，核Definition22/Example23/Proposition26；特别19–20的contiguity步骤使nonnegative special exponent同样适用，不需要强加Lemma24的blow-up条件。未将PDF20开始的数值examples用作这里的定理。

## R3. 真正 Taylor tensor 与 full jump

T15的t^s、t−s准确抵消，是Q[[t]] germ。kerN的anti-diagonal recurrence在Sym²中只留even sums0..r−1，在Λ²中只留odd sums1..r−2；超过边界的anti-diagonal首项被迫0，随后全部0。故形式kernel维数和basis完整。

T17按D(t^±sA(±s))展开，确有+2sA(−s)A(s)。J1(0)=2与实际 2W(φ0,φ1) 的常数吻合，不能漏掉此项。T18的两个cross sums在h even时相同，留下2ψ项及ψ²K_h；T19在h odd时用Wronskian反对称性使两个cross sums相同，ψ²项为0。这给全部jump，不是只检查一个Γcoefficient或最高log。T9零row对应T18右端恒零，与T12的完整列一致。

## R4. O(r) 定理 hypotheses、actual function rank 和1的加入

本人本轮实际 FULL读Beukers–Heckman1989 PDF2、20–23（5页）。PDF21 Proposition6.1核selfduality，PDF23 Theorem6.5核infinite primitive、非scalar-shift finite、d=1、special eigenvalue−1。这三个模型的a−β全非整数，MUM是单Jordan块；若T0循环多block，则block-cycle谱包含非平凡单位根，不能unipotent；若逐block固定，则fixed空间至少block数维，不能等于1。故primitive。其projective无限阶排除finite scalar shift。所用Theorem6.5结论确为O(r)，非只得到某个未识别proper subgroup。PDF2与20给regular-singular differential-Galois/Zariski-monodromy的使用范围。

Sym²分解为metric⊕traceless irreducible，Λ²在r3/5/9也irreducible。scalar-product/Wronskian maps的kernel monodromy-invariant；前者杀metric而不全杀traceless，后者在W(φ0,φ1)非零，故kernels恰如正文。其constant image维数只是第一步。

T22的rational-function rank提升也成立：在一个普通t0取非零evaluation vector v，任一C(t)关系的coefficient vector在t0须同时消去全部monodromy orbit Mv。irreducibility迫orbit span为全image，所以coefficient vector为0；在普通开集如此，故全部coefficients恒0。

加入1的T23可用同一论证精确检查：若r0+Σr_af_a=0，则r(t0)消去所有差(M−I)v。非trivial irreducible表示中的这些差张成全image（否则商中出现trivial quotient，违反irreducibility）；因此r_a=0，再r0=0。这补足“rational row不在nontrivial image”在C(t)关系层面的含义。所选rank9 packages实际rank5，不能由formal Sym²/Λ² dimensions免费拿44或36个Taylor rows。

## R5. 三点齐次field限制的准确量词

T20的rows固定T0。若其rational combination还固定实际Tc，则固定生成原三点monodromy的两个loops；属于原Picard–Vessiot field时，Zariski density与fixed-field theorem使其在C(t)。R4的实际rank与加入1的独立性再迫所有nonrational-package coefficients0。因此T24及更广finite tensor/rational differential expression statement在限定field内成立。

这项结果并不排除附加forcing singularity、非齐次inverse-L extension或另一connection。它也不把某一次沿不同Riemann path的局部branch-fill等同于固定原全部generators。本文明确保留这些范围，原source未被换成low-rank校准对象，未宣称普遍odd ζ no-go。

## R6. Caps、CDT数组及 Apéry 区分

T25沿实际coefficient formula消费j个reciprocals；rank9均≤5n，half模型≤2n。T15的convolution共消费h个，T17的D仅乘整数index，2s项消费h−1个也被更宽h cap包含。故T26全prime safe upper成立，包含constant coefficients和2/5，不只对某个progression成立。

本人以已实际 FULL读的CDT固定v2 PDF66–69定义重核六个τ：r3的0、3/2；r5的20/9、4；r9的92/5、116/5。每个basis实际rank已证明，排序与nested columns合法，e0故τsharp0。没有把Tate comparison常数作为Q-Taylor coefficients，也没有把safe cap称最优费用或严格余量。

本人另实际 FULL读Apéry1979 PDF4，核两组初值(1,5)及(0,6)和其三项recurrence。由生成函数t1 coefficient=6、后续coefficients被recurrence消去，T28确为L_A B_A=6t。第二sequence共享后续递推并不使B_A成为齐次solution。原ApéryL的两finite根和不同forcing均保留，不能套三点field T24误否定已知Apéry扩张。

## R7. 实读与裁定

本正式review本人本轮实际新增primary读域：BH PDF2、20–23共5页；BV PDF15–20共6页；Apéry PDF4共1页，共12页。CDT66–69在本轮自身main前已实际 FULL读4页，此处不重复加；BV24–26等自身main读域也不继承作者/同伴作为个人域。本分支本轮main25页加review新增12页，共 **37 distinct primary PDF页**；无新下载PDF/HTML/code。Au PDF26已实际目读既有渲染，不把目读重复加页。

最终裁定PASS，无修订请求。actual FULL阅读、数学纸核与文件来源scope各自明确；没有替新无理性/LI结论背书。本review待作者实际全文收读并最终main回读；来源收据只能pin已稳定文件，不pin未来audit或循环receipt。
