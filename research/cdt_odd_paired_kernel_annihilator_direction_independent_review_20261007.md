# 原 annihilator 方向稿的独立全文审查

2026-10-07，审阅者 /root/masked_racah_finalize。唯一 NEW 正式 reciprocal review。审查对象为 cdt_odd_paired_kernel_annihilator_direction_20261007.md，稳定 SHA d958096383ae2745cd5102655690bbdfba855c5da80afd0aff70fbd4d2328086、17344 bytes、D1–D29/全部9节。已实际完整读取，不用聊天摘要代替论文全文；下列步骤独立纸面核验。结论 PASS，无正文修改请求，未以条件门槛宣称特殊值无理性。

## V1. 输入与实际读域

本轮实际 FULL 读最终主稿 D1–D29，以及六份直接冻结输入：relative-spectrum R1–R29（41b309）；exact-phase F1–F18（735150）；primitive-kernel K1–K18（996e26）；coupled C1–C23（03a4d1）；mixed-node entropy S1–S27（f02161）；Hasse arithmetic J1–J18（8676d1）。另为本人本轮算术研究 FULL 读 content Q1–Q22、lattice I1–I25、actual-local G1–G15，但不将这些未被本主稿正式引用的新算术结果偷偷作为解析结论依据。

一次随后重复的 combined read 在总工具返回预算处截断了 coupled 的中间段；coupled 和 entropy 都已以独立完整命令、充足总输出预算全部补读。这里完整读域来自实际全部显示的文本，不计省略段为 FULL。原全局 numerical JSON、producer、guards、prime tables 本轮没有执行、import、rerun 或扩展。Authority §§176–180 完整读；audit syntaxparse/header/schema/580计数/物理SHA，非人工全文重读全部580记录。

新增数学 producer 创建/执行/import/rerun0，prime实验/扩表0，Lean0；新增 primary PDF/HTML 阅读及下载0。不继承被引用旧稿作者或root的原件阅读页数、旧 FIRST1 运行或旧数值认证。

## V2. 原反射、实正 Gram 与 selfadjoint phase involution

D2 保留原 R_n、cot导数、竖线、common S_n、固定有理 α/β及全部source W_j/24。逐式检查 D4–D6：实 rational/cot coefficients 使竖线两侧密度共轭，w even；原 g_i 在 x反射下亦共轭。P_ij 在 x↦−x 后等于自身共轭，所以 P 是 real symmetric SPD，而 B real symmetric。Cauchy–Schwarz 的原 contraction 于是 T=P^−1/2BP^−1/2 real selfadjoint。没有将 real symmetry 误当 low/high 正交或高B块正定。

独立对 cot 求导得到 second derivative −2iπ³ sech²(πx)tanh(πx)，third derivative 2π⁴ sech²(πx)(3tanh²(πx)−1)。乘实际源系数后准确得到 D5 的 8iα 与 2β，β非零仅保证非恒零；可能零点按零测集处理合法。

对 linear-first L² convention，J0f(x)=overline(f(−x)) 与 Af=overline(τ)overline(f) 都是 conjugation。U=AJ0 是 linear unitary，D4使 U²=I，所以 selfadjoint。此一步确实用反射条件，不借“一般两conjugation乘积是involution”的错误命题。J0固定全部 real-coefficient g_i；P实使正交化frame仍J0固定。〈e_i,Ue_j〉=T_ij，而operator coefficient本来为其共轭；T实准确消除此共轭。D8的W故为实际全部moments annihilator，不只点值测试。

由W上的 compression为0，〈h,Uk〉=0 对全部 h,k∈W；Π±=(I±U)/2 给 D9 的两个投影Gram恰为原Gram的一半。√2Π± 的 ν维isometric images结论成立。D10 为 real kernel polynomial 的真实函数公式，但两投影一般不在 polynomial span，正文禁止对其免费施加负整数source evaluation；此范围准确。

## V3. Phase block graph 的条件、范数与奇异分支

P-orthogonal 的 E_n⊕H_n 两空间维数各n；high span恰原 S_n乘degree<n polynomials。对它们选J0固定frames合法，所有P/B/V必须同时变换；原primitive商算术仍在原格计费。

C_HH可逆时，下块解为 h_H=−C_HH^−1C_HE e=Ge，上块准确给Z=ker(C_EE−C_EHC_HH^−1C_HE)。这逐式证明D13的actual W graph与continuous norm I+G*G。没有把一个自由graph赋予BK=0，也未在高phase singular时删除η。

由于C selfadjoint且C²≤I，HH块给 C_HE C_EH+C_HH²≤I。置s=σ_min(C_HH)>0，则 I−C_HH²≤(1−s²)I，故 ε²≤1−s²、||G||≤ε/s≤√(1−s²)/s。D14是安全bound，s≤1由contraction自动成立；固定s不足以压制指数昂贵source的提示正确。正文给 Moore–Penrose 解及残余η/compatibility的奇异分支，未跨用D13。

## V4. 同原 source 完成平方与实际 generalized compression

D15的v(h)仅对原polynomial使用，完整保留24ΣW_j|h(−j)|²。Source R_HH SPD使 G_V=−R_HH^−1R_HE与S_E>0合法；展开完成平方逐项回到原source quadratic form，D17无遗漏cross项。

将实际phase graph代入，残差必须是Δ=G−G_V。N_Z是S_E+Δ*R_HHΔ在Z的真实压缩；A_Z是I+G*G的真实continuous压缩。令Z的orthonormal frameQ，kernelmap(I;G)Q的两个Gram分别为N_Z、A_Z；continuous正交化后所得R_K准确 unitary-similar于A_Z^−1/2N_Z A_Z^−1/2。因此D19的det ratio成立，并与primitive K的两个Gram同时乘|det|²不变。没有隐藏新的 lattice index、补基height或单改P的source转移。

D20–D21从N_Z≤b_n I、A_Z≥I给R_K≤b_n I；保留的det bound是νlog b_n−logdet A_Z。第二项的符号正确，且ν0空det边界合法。正文明确未估原σ_E或weightedδ，不把unweightedΔ norm视为δ。

独立检查D22：positive source cross项由Cauchy–Schwarz控制，实际graph vector对应u=||Ge||/||e||≤t。函数(√r_E+√r_Hu)²/(1+u²)的导数符号为√r_H−√r_Eu，故最大点u=√(r_H/r_E)，正文两分支与连接点正确。这是丢掉Schur相消的较粗bound，不能与D21扣两遍信用。

## V5. 原指数通道、n²目标与限定反例

冻结relative R4–R5在原P/V同规范证明至少n个 eigenvalues≥a_n、a_*>13/4；本稿未将存在large channels当kernel自动避开它们。对ν≤n，eν(R)≥a_n^ν，与D19–D21给D25：
−log L_K≥νlog(a_n/b_n)+logdet A_Z。右侧可以为负，正文保留通用0下界，不宣称已有positive rate。

在ν/n→κ>0、logb_n≤bn+o(n)、b<a_*及实际C_HH可逆的明确条件下，νlog(a_n/b_n)/n² liminf≥κ(a_*−b)，continuous det A_Z≥1，D26成立。ν=o(n)与κ0不凭同一固定指数差获得n²保证；max(b_s,2b_δ)的weighted-defect指数和平方费用准确。

D27–D28为限定finite Hilbert例子：U把核v与额外w互换、固定d个u，是selfadjoint involution，J0实conjugation与U commute；C=diag(I_d,0ν)、W=spanv、两个±通道各半范数，高空间可选在u中且C_HH=I。R=M_n I的source Schur仍M_nI、Δ0、L_K=binom(m,ν)^−1，所以 −logL≤2nlog2=o(n²)。即使 high phase单位和指数relative channels都满足也无一般n²信用。例子不含原cot/W/paired arithmetic，正文精确限制其用途，不扩大为原研究方法no-go。

## V6. 同对象全prime费用与剩余条件

D29逐式比较 exact |Jν|=Hν L_K Θ_d、entropy S4原Hν upper及Hasse J16/J18原Jν lower，−A_full+(5/4)κ²+22/3+2γ−κ(Θ+17/2)符号全部一致。固定(DM)^(2n−ν)只贡献O(n)但明确保留；原Γ只付一次，adaptive κ0、half阶与source变量不被混用。

真实 q 的费用不能因Jν=q a_V而免费继承jet费用。本轮另一算术稿的node整除和actual a_V lower也不能直接给continuous P_K lower或R_K upper；作者当前主稿没有将聊天lemma当冻结依据，范围正确。本文提出的三个实际门槛——C_HH conditioning、P-orthogonal低source Schur与phase/source weighted graph缺陷——均尚未估足。结论属于实际新反射约束和精确conditional direction reduction，不是已达成特殊值无理性/LI/Lean。

## V7. 最终审查结论

实际全文独审 D1–D29/all9节及必要冻结输入，纸核 PASS，无实质纠错或正文修改请求。独审文件完成后审阅者实际全文自读与物理SHA核对另行完成；待作者实际收读本review及收审后最终全文回读，再创建单向FINAL来源收据。不pin未来/root receipt，不修改580旧冻结文件。
