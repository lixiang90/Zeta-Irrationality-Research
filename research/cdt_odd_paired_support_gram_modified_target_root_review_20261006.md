# 支撑相关 Gram 费用与实际 modified target 的联合审阅

2026-10-06，root，NEW 审阅。455既存冻结数学文件及所有旧/同行数学producer只读；本审阅不执行/import任何producer。本轮root另一个自有weighted程序恰首次1PASS，与本审阅执行0分开记。以下结论为纸面核查，不把finite samples当全尺度proof。

## R1. 实际全文和静态来源范围

实际完整读四份NEW主稿：

- quarter [support-correlated](cdt_odd_paired_support_correlated_budget_20261006.md)，SHA150bb58d8d5a0463bb8747bf1e9e8a549727973b89d133b620b5d3535fd1601e，C1–C10/C1–C21。
- toric [actual local Gram](cdt_odd_paired_actual_local_gram_layers_20261006.md)，SHA2856a47ab3aa407f1eb7477a57e1e44bd010a7dd95b8cb055a603b68ea091094，G1–G15；实际初稿全文及最终全文分别读，最终新增GL自核、收益/执行史已读。
- arithmetic [modified target](cdt_odd_paired_jacobi_modified_target_normality_20261006.md)，SHAc4dcee183239be55ab6c4e06d4b1abb1979657838f02a5c64104c45cc1fed9c4，13sections/T1–T27。
- root [weighted joint support](cdt_odd_paired_weighted_jet_support_budget_20261006.md)，SHAb9535b241ef67af5d5ce82aaa8bd5073e844dd5a9b5701f12669b1cc9a5211cb，W1–W10/W1–W14；root为作者，**不把本稿称其独立审阅**。独立性由实际完整读的quarter [正式独审](cdt_odd_paired_weighted_jet_support_budget_independent_review_20261006.md)（SHA5278b427215c223f5e545d93d24cc22cec5151f55227212a572337acae2a4faa）提供。

四份PY均实际完整静态读取，无截断；执行/import均0（root自有首次执行已另计）。成功JSON均完整syntax parse：toric全部45cases所有字段/两sources/13affine记录实读，arithmetic全部3cases/metadata实读；quarter全部metadata及first/last完整affine记录实读，471条不称逐条人工回算；root三case全部allocation/成本/rank及rowlabels首尾实读，quarter独审读所有labels。四程序均恰自有FIRST1 PASS，source/JSON不重跑、不改。

NEW原件：root实际Grinberg–Petrov PDF1–4、10–14、31–33共12页；Krattenthaler PDF1–3共3页；Álvarez-Fernández等PDF8–9、15–16共4页。Root本轮总新primary实读19页，不称全文94archive页。最后两份作者更大scope不冒记为root读域。普通verified TLS，无证书bypass。

## R2. 同一个真实格的 DND 估计通过

C/G都保留original B6/k3/s5、rank2n saturated integer-valued paired格、degree<3n和形式变量X。ψ-basis degree i，leading比i!/(i0!i1!p^i1)为p-unit，finite differences给整coefficients，故是原ambient的真实GL(Zp)，未增加jet自由度。

完整Q层各residue Q个自由coefficients，top层仅R个low-digit参数。unit-W residues计数u=min(6n modp+1,p−(2n modp))（n<p≤2n时后一项为2p−2n）。unit-tail每residue至少Q+1个不同ψ值，故values全0强迫local polynomial恒0，再使p-scaled derivative全0。ambient实际image rank=Qu+min(R,u)；限制到actualpaired只给rank upper，不假设实际每个局部参数独立。

modp kernel basis必须在原S坐标lift，才在char0中精确满足paired条件。toric G5给这个construction，不用自由modp polynomial作actual lift。p^5 scaled node blocks在unit-tail整、nonunit-tail≥p²、head≥p⁴，因此strong/weak≥p、weak/weak≥p²，真实GL basis上的DND给whole-X v≥−10n+2k。C/G均未由此声称exact Gram Smith、target nonzero或免费的global/arch basis。

## R3. 付费比较及三项信用合并通过

quarter C6的actual floors与连续模型只差u里的≤1，Q≤12给uniform误差，包括p|2n/3n/6n；471interval certificate插入所有possible affine branch交点，随后midpoint只选已分割区间内的固定branch。C8的47合并段和C19/PNT计算是完整有限模型，不是采样外推。实际新增ΔC=20948066064530861/14991578506784880，且只兑现[1/4,1]；其余place旧界保留。

toric G12/G13实际与已付carry/Plücker模型取max，七个正段及13closed pieces完整。七项面积和是16469/23100≈0.712944；早期“约0.813”口头相加错误已经更正，未改成功数学source/JSON或七项paper。该window1<x<2与quarter不交。没有裸积分被cap隐藏的tent。

root W3是指定jet-row rank上界，W6使A-minor左右每node数匹配。rank credit和0/2/3/5权重保留同一support，得到全p whole-X Ω模型。W3的“整矩阵”在W2/W4的语境中指**Z_p整矩阵**；pP'可能有其他素数分母，不主张它是全局Z矩阵。proof和finite检查均用Zp，没把p-scaled derivative当plain整数。

quarter正式独审已经全文核W3–W14，包括shared ragged信用不能免费独立、−32实际边界及新window相对新DND的1/84。其窗口与quarter重叠，合并先取max，严格额外收益才是1/84。C/G两窗口不交，于是现在可合法定义
\[
A_{\rm joint}^{safe}
=\frac{45711182732576087}{1070827036198920}
 -\frac{16469}{23100}-\frac1{84}.
\tag{R1}
\]
它约41.963，较上轮约44.085下降；仍是安全费用upper，非actual content等式/cost lower/no-go。

## R4. 固定middle值和norm-free目标公式通过

arithmetic T3/T4在λ2准确返回原G0/M5。T5的plus系数3、middle-minusλ−3、outer-minus−2直接展开正确；λ为诊断参数，不能选择generic λ后称完成原特殊值目标。

T7 slope L^tDL rank恰r，detMλ degree≤r；T8仅除已知−I_r，T9 bordered compound identity先在formal invertible A上推再升为polynomial identity，没有用未知M3/G0/M5 inverse。T10系数归一化(detVmid)²方向正确，其kerL的3r restriction仍可能奇异。

T12先用middle Vandermonde和cardinal X，得到明确detGλ=cG det(λI+K)。T14 Loewner负号由Z'的负reciprocal square得出，未知现在是固定−2 eigenvalue排除，而非generic family正常性。没有删middle、halfjet或原r/3r degree限制。

## R5. 实际Q全阶单位、connection和有限Christoffel通过

λ4(d)两首次共振d=5r+1、10r−4都在N=5r+1 cutoff之外（r1等号也不在d<N）。因此actual四Q源unequal Krylov profile覆盖degree<N。T17用真实χfold权重、Vandermonde和Δ4(N)得一个全N阶unit，实际QQ infiniteblock Hankel rank恰N，minimal realization N。该结论与原短3r、(r,3r) critical profile正常性有区别，作者保留此gap。

θ_j(J)e0=B_j e_j归纳及T19完整connection公式正确，h_j=v_startΠa b是明确单位。T22/T23是保留source profile的Cauchy–Binet/compound identity；所有λ2系数为units也不能排除有限域sum相消。

T24自证finite-support模板：j≥m的monic p_j含characteristic θ_m，functional上恒零，允许其norm0。n≤m<p确保n! unit，Vandermonde按monic OP展开只有低degree組 survives，confluent时用Hasse而不是免费除p-factorial。该模板适用于single-chain modified minors；原四/八源须用compound公式。实际原文Kratt PDF2要求char0/allnorm、matrix PDF8–9/15–16要求所有leading块及Π非零，不能直接套来证明当前未知。

p19手算Gλ=3λ+14、detMλ=λ+13；λ8使G退化、λ6使M退化，均非0/3，ambient及共同J/raising/fullQvisibility继续正常。真正λ2仍G1/M15；这是诊断family反例，**没有发现actualλ2反例**。它严格排除“endpoint proper+raising+fullsource unit自动下传critical”这条错误推论。

## R6. 审阅结论和剩余工作

上述peer全尺度推导通过，有限source/JSON scope与正文对应；root weighted依正式独立review通过。本轮同一对象的实付finite-place费用已经推进，目标normality也有更明确且无循环分母的判据。

仍缺真实λ2在无穷辅助p上的两个critical simultaneous units/目标无限nonzero，以及同一个determinant的strict arithmetic–analytic margin。当前已证解析率>12.003572854与R1未匹配；不得由safe upper宣布方法不可能。没有新的ζ/L/Catalan无理性/线性无关性定理，没有Lean执行或形式化定理。

最终其他两份正式cross-review/source receipts另由root实际读取并在main/delivery准确登记；本审阅不冒认未来尚未读的文件。全文自读后冻结，旧/同行execute/import/rerun0。
