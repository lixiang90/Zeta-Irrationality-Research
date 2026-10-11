# 同一配对格的支撑相关预算与直接Gram层：正式独立复核

2026-10-06，/root/conifold_arithmetic_hypothesis。NEW正式独审。本审旧及同行数学producer执行、import、rerun均0；没有为复核新建或执行数学producer。自有本轮modified-target程序的首次1次PASS属于另一主稿，不计为本审执行。所有被审数学文件只读。

## V1. 实际完整读取与指纹

已实际完整读quarter稿research/cdt_odd_paired_support_correlated_budget_20261006.md，SHA150bb58d8d5a0463bb8747bf1e9e8a549727973b89d133b620b5d3535fd1601e。读域为sections C1–C10、equations C1–C21、全部47合并gain rows；输出无截断。

已实际完整读toric稿research/cdt_odd_paired_actual_local_gram_layers_20261006.md，SHA2856a47ab3aa407f1eb7477a57e1e44bd010a7dd95b8cb055a603b68ea091094。全文G1–G15标记、全部公式/表/执行史完整输出无截断。另完整回读冻结dual稿research/cdt_odd_paired_dual_plucker_carry_rate_20261006.md，SHA0fb995f69cefcd4e6c92f7ffa42a8e595add4dda9a94951ed27a4693fb127047，sections D1–D10及eqD1–D21，独核本次n<p基线确含已付mixedcarry tents。

两候选来源receipt均实际全文读取并物理hash核：quarter literature/manifest_cdt_odd_paired_support_correlated_budget_20261006.json，SHA6c24614353318e8d4a9dfa328cf0947c792e8bc8ae271befd74c4dd866478fd2；toric literature/manifest_cdt_odd_paired_actual_local_gram_layers_20261006.json，SHA87be20e0a07495bd81899101f3215d50df9cea276b86a3911c00dc10fba2b237。这是本审实际读过的候选快照，未冒记未来final receipt读取；最终metadata由root独立pin。

## V2. 同一对象、真实ψ基与ragged顶层

两文均保持原B6/k3/s5、ambient degree<3n、actual saturated rank2n integer-valued paired lattice和原S基。固定有理sources共同分母的determinant费用2n次幂/O(n)仍保留；whole-X控制不依赖有理specialization非零。

独核b_i=binom(t,i0)binom(ψ(t),i1)、i=i0+pi1<3n、ψ=(t^p−t)/p确给原Newton格的GL(Zp)变换：p²>8n保证i<p²且i0!,i1!为units，整数值的有限差分系数在Zp，最高系数比i!/(i0!i1!p^i1)的valuation为0；与t→t−1整unitriangular变换合并不改变格。完整层Q个、top R维，top residue依赖保持degree<R，不能自由补成p维。

每个unit residue实际tail有h个不同ψ-values，h≥Q+1且h<p。因此degree≤Q局部polynomial在所有tail values为0，严格推出它全为0，并推出其ψ-derivative为0；p乘low-digit导数也为0。这才合法推出pP'消失，不能由单节点value消失直接推导。支撑ambient rank准确为Qu+min(R,u)，限制到actual2n空间仅作秩上界；没有把ambient自由basis冒认成真实paired lifts。

## V3. actual weak lifts与完整whole-X DND

独核原form的U、V(X)、W和缩放p5：jets(P,pP')的node matrix是W[[p5V,p4U],[p4U,0]]。tail积分估值给p4U、p5V whole-X整；head U整而V≥−1，故head block被p4整除。Legendre双carry使nonunit W的valuation至少2，而非仅至少1，故nonunit tail block被p2整除。固定a,b可被p整除，不需假定为units。

真实weak subspace取自U/pU的unit-tail Hermite kernel。因原U饱和direct summand，可在原S坐标lift/扩成GL(Zp) basis，所有lift仍是characteristic-zero exact paired polynomials。unit-tail的strong/weak项带p、weak/weak带p2；其他nodes自身的p2/p4费用覆盖它们。于是p5B=DND，N∈Mat(Zp[X])，D=diag(1,p)，每个weak方向两侧各付一次p信用。det取回原S只乘p-unit，所以whole-X Gauss下界−10n+2k正确。它不需要target非零或未知Gramunit；也不等同C!Smith。

quarter用k0=[2n−Qu−min(R,u)]+处理p≤n；toric定义actualHermite k后在n<p≤2n以同一ambient cap给k≥k0。两文允许actual核更大，不从有限probe外推exact rank或GramSmith。

## V4. 离散端点、已付cap与两窗口不交

quarter u=min(6n modp+1,p−(2n modp))包含residue0、r6=0及r2=0。x∈[1/4,1]时Q≤12，|u−nU(x)|≤1，所以actualk0与continuousκ误差uniform≤13，Gauss下界仅再付常数26。p|2n、p|3n、p|6n没有作为免费例外删除。

toric n<p≤2n的u=min(e+1,2p−2n)、Q∈{1,2}和ragged R准确。其gprev已取entrycap与oldraw+2d的max；本审回读dualD18–20确认三tent归属，第三tent被旧cap遮蔽。新增信用使用max(gprev,gdirect)−gprev，因此并未再次支付先前Plücker信用。

quarter只在p/n∈[1/4,1]兑现；toric只在(1,2]兑现，两prime windows不交。p=n最多一个边界prime，归quarter，离散/连续误差O(nlogn)不改变主率；不是靠重叠裸积分相加。若与本轮root新的同window weighted界合并，仍需逐prime取max，不能将重叠面积无条件叠加。

## V5. 正面积、完整affine cover与PNT方向

quarter C18可不借任何证书手核：4/7<x<3/5时Q5、h10、a3，U=6−10x、R=U/2，gdirect=110x−72，old=−10，所以gain=110x−62；两端gain6/7与4，宽1/35，面积17/245。这是一条完整positive-measure n²收益。完整47表覆盖[1/4,1]；程序枚举全部floor/raw边界及全部potential affine比较根，中点只在已分割区间选择branch，随后linear endpoint不等式保证整闭区间，不以有限网格推未知函数。正文总paid面积20948066064530861/14991578506784880及safe A45711182732576087/1070827036198920保持上界性质。

toric七个非零gain段与已付baseline逐段吻合。本审纸核面积分别1/14、21/400、15/1936、28/1089、5/36、1/24、3/8，合计16469/23100。特别14/11两侧的分支转换、5/3后直接Gram信用和7/4后oldraw超cap均准确；没有裸积分被cap隐藏的第三tent。standalone safe A=3887231721011/89625135600。

每个prime使用actual integer Gauss下界的max得signedQ_n且D_A/Q_n∈Z[X]。改进是提高ℓ_p，故提高logQ_n、降低正safe费用A。uniformO(1)误差在p~n的总量O(n)，在主n²率中消失；bounded piecewise affine的PNT step上下逼近给liminf n^-2logQ≥−Aold+paidgain，方向正确。小prime/窗口外都保留冻结合法界。有理X分母O(n)保留；没有由整化自动推出无限nonzero、strict margin或数值无理性。

## V6. Source/JSON的静态读域与有限证据边界

quarter PY完整静态读，SHAcd659ad52bad2d829bcbe9ec0c54812f3c238b00559f8e4aef6a4df337e31153；JSON物理SHA6db2c221a8e19496eda0005ce1ac4918d53dfb4e103f46d57f54fee51401f2f0。整个JSON只读syntax parse；全部metadata、首尾两个完整raw records实际读，正文47 merged gain rows实际全读。未声称471 raw records逐字段全部人工读或4715checks手工重算。代码完整算法及正文全尺度推导是本审结论基础，保存471条不替代真实格证明。作者首次1PASS、24floor intervals/471pieces/4715checks是他自身历史，不是本审执行。

toric PY完整静态读，SHAe9a512a8bb9f40b6c84144eeeaf52eb9761a0ef0699adc4e82af07d8c0c1ebf9；JSON物理SHA0fd35bb97e6f16a6a7ac273e0bd8baba1b7afc8f91f321c8a038416d4fdd900e。只读parser后全部45case的每个字段、两sources、全部13affine records/每个字段和metadata实际完整输出读取无截断。源码确在原S上构造exact lifts，以原Newton values/p-scaled derivatives和原W,U,V计算p² Gram，而非换成ambient自由格；形式X项逐case单独处理。作者首次1PASS的有限45cases不承担G2/G11全尺度或GramSmith/nonzero证明。

本审新primary下载/读页均0，没有借用同行primary阅读声称本人读过。上述两proof、两PY、toric全部JSON、quarter明确选择JSON域、两个candidate receipts和dual稿为本人实际scope。

## V7. 正式结论与冻结边界

两文全部声明的全尺度支撑/degree/ragged、actual lift、whole-X DND、已付max费用、uniform离散误差、PNT方向通过独立纸面核查，未发现需修改的数学项。允许按不交p≤n和n<p≤2n窗口合并已证paidgain；与root同窗口weighted界另取共同max。共同对象仍为原D_A。

该通过不扩大为actual content等式、exact GramSmith、无限aux/target nonzero、strict margin或任何新的ζ/L特殊值定理。正式review全文回读后冻结只读；被审receipt今后只能把候选实际读域作为历史，不改写成本审未读过的未来final。
