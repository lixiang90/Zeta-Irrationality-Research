# Supported jet 与 weighted dual 转移：独立全文审阅

2026-10-06 研究轮，2026-10-07 完成。NEW，审阅人 `/root/conifold_arithmetic_hypothesis`。baseline487及全部旧、同行数学 producer 和冻结收据只读。本审阅没有执行、import或重跑任何数学 producer；作者本轮另一份 Racah 机制 FIRST1 与本审阅分开记录。本文件按已经发生的读取和纸面核查冻结，不等待未来收据，不与同行最终收据形成 hash 循环。

## V1. 实际全文、源码与保存 JSON 的准确范围

实际全文读 quarter 的 `research/cdt_odd_paired_selected_jet_primitive_support_20261006.md`，全部 P1–P8 sections、P1–P15 equations，无截断；物理 SHA256：

`35ed9d8e9b3f1f5ea70c4e742d1e26c262d6d529823987bdc0478128fdd35880`。

同 stem `_verify.py` 全部静态读，SHA `1aec5fd218fdb9ba920eb579b5d1d09318c3828c0cb6d30ab9b632caafb79b2e`。成功 JSON SHA `07d7dd36f8b0c094676532ba8b86d36e7c7a882b2b11b37b1e18897c4d1f57bc`：完整 syntax parse，全部 metadata、36 个旧 affine faces、12 个错误 global-f 的反例，以及全部 6 cases/30 profiles 的每字段和每条 selected-node/type label 实际读取。首次组合输出截断，随后独立以明确 `v=value`、`d=scaled_derivative` 编码完整补读全部记录；没有把截断输出算作完整读取，没有手工重新计算全部17059asserts。

实际全文读 toric 的 `research/cdt_odd_paired_supported_weighted_dual_transfer_20261006.md`，最终全部 T1–T9 sections、T1–T18 equations，无截断，SHA：

`3a4b58d6d0fbad83e13268e4b30d73030caf8461c99a4db0acb5681ba1625334`。

同 stem `_verify.py` 全部静态读，SHA `92b737b19375e973c97b67830477b10313b365f617df6dc5e0f193e74bd0aa94`。成功 JSON SHA `a37ce3e552a6ded9efaa48f07ca268ec207000d4a165cc4e072ba52dc31f1694`：完整 syntax parse，全部 metadata 和全部98条 merged rows 的每字段实际读取，包括区间、Q/h/a、旧界、新 winner、新界、gain 和 exact area。首次合并输出截断，随后独立完整补读所有98行；213 arrangement cells 是内部检查计数，结果没有逐条保存213 cells，本审阅不声称读过这些未保存记录。12141 assertions 未逐条人工重新计算。

另只读冻结 `research/cdt_odd_paired_weighted_jet_global_optimization_20261006_verify.json`，SHA `5bb704e25707379253bb7733d86c44a354c917bc4c12b96fcd34dfda70bf2863`。本轮实际读取 metadata，以及全部113行的 lo/hi、Q/h/a2、combined label 和 combined slope/intercept，核对新 certificate 使用的 literal baseline；不声称本轮全文读其所有其他字段，不执行旧模型。较早 verbose 输出截断后，独立完整补读这些明确字段。

来源元数据实际全文读域是当时候选快照：quarter `literature/manifest_cdt_odd_paired_selected_jet_primitive_support_20261006.json` SHA `a5f6ffe119d306c77f45c0a6f16c3a15a37cb6ca7f321379e80c0a108c647786`，toric `literature/manifest_cdt_odd_paired_supported_weighted_dual_transfer_20261006.json` SHA `633f6bc78ad2b42b8c7d1cca3a8ee2fdcfdcc676a63bcff64601667cb97f20b2`。不提前声称读未来 final 版本。本项独审没有新增 PDF 下载或 primary PDF 页阅读；Racah 主稿的来源阅读另有独立记录，不挪作本审阅输入。

## V2. 真正支撑的 coefficient source 与 rank：通过

两稿保留同一原饱和整数格、完整基 S、B6/k3/s5、degree<3n、rank2n 和原 whole-X 行列式。有限处使用整数值 psi 基的局部 GL，不替换 S 的实处范数。冻结 primitive split surjection 与 psi 整模型是明确前提；本轮两篇新 rank 证明不重新声称计算了该完整格。

设 p>5、p≤2n、p²>8n，写2n=ap+r2、3n=Qp+R、6n=hp+r6。每 residue 的底Q层各自自由，最高层是一个 degree<R low-digit polynomial。因此 B 上完整 coefficient source 的维数准确是

\[
Q|B|+\min(R,|B|).
\]

这里 B 是所选行数 r_rho>Q 的 residue 集合。只有支撑在 B 的 primitive head constraints 可以减少这个源空间：unit/nonunit 高 carry 方向强迫 unit-side head value 为零，unit/unit 两端都在 B 才计 actual pair。真实反射 sigma(rho)=V−1−rho，实际 head residue 是 m≡−rho；方向和原 d_m factorial valuation 一致。

对 C=B∩U，真实 independent constraints 的数目是

\[
f_B=a|C\setminus\sigma U|+\frac a2|C\cap\sigma C|.
\]

固定真正 ragged top 后，Q≥a 的底层在每 residue 的a个互异 head psi-values 上满射；不同 primitive pairs 的 head coordinates 不交，故上述约束仍独立。reflection loop 没有 fixed integer head site；V odd 迫a even，a/2贡献为整数。没有把同一 loop 计成两个 offcenter pairs。

于是，先限制 big coefficient source，再对 selected rows 作 observation，严格得到

\[
\operatorname{rank}Y_I\le\sum_\rho\min(r_\rho,Q)+\min(R,|B|)-f_B.
\]

这个 upper rank 不要求 selected Hermite jets injective，也不要求 derivative-only 能恢复常数项；observation 只会进一步降低秩。它改进的是 coefficient-source cap，不能在一个已经扣除了 observation kernel 的其他 cap 上再重复减 f_B。更不能任意减完整 global f。保存反例的 scope 正确：如 (n,p)=(19,13) 的真实原 S selected value minor，rank38、旧 cap38、global f1、f_B0；错误全减会断言rank≤37。有限反例支持这个区分，全部尺度 rank theorem 由上面的插值与约束独立证明负责。

## V3. Whole-X 两侧匹配与 graph 删除：通过

原 p^5 B_A(X)=Y^t A(X)Y 的 node block 仍是

\[
A_j=W_j\begin{pmatrix}p^5V_j(X)&p^4U_j\\p^4U_j&0\end{pmatrix}.
\]

在一个非零 A-minor 中，每个 node 的左右 row counts 必须相同；counts0/1/2均如此，左右 value/derivative types 可以不同。因此两个 selected Y-minors 的 residue r、B 和 f_B 相同。两次 Cauchy–Binet 加两个整数 minor 秩缺陷，严格给额外2 f_B、原 ragged 项和原 node valuation 项；证明逐 X 系数成立，并非只在一个 specialization 成立。

两稿的全尺度接口准确为

\[
v_p^{\rm Gauss}D_A(X)\ge-10n+\Omega_p^{\rm support},
\]

\[
\Omega_p^{\rm support}=\min_{\substack{\sum r=2n\\0\le r_\rho\le2q_\rho+2}}
\left[\sum_\rho\{w_\rho r_\rho+4(r_\rho-2q_\rho)_++2(r_\rho-Q)_+\}
-2\min(R,|B|)+2f_B\right].
\]

这里只用整数 minors 的下界，没有宣称 actual Smith 或 exact Gram valuation。零多项式也满足该下界；它不证明目标 nonzero。fixed rational sources 的同一个固定分母按原对象先清，只付O(n)，没有免费变为整数 source。

完整 unit packet 有 f=a min(u,V/2) 条 head relations；删除 s=|U\B| 个 residues 至多移去 as 条，于是 f_B≥(f−as)_+。一个 pair 两端都被删可以在这个上界中重复计损失，方向使界更安全。该删除不等式不是完整图 exact optimum。

## V4. Weight gap 真正支付缺失约束：通过

对lambda3,…,11、eta0,1,2，unit sector q=h、w0；h≥2Q、h≥3a。对完整整数 prefix 独立手核 priced minimum，得到

\[
\alpha_U=(2-\lambda)2h-2Q-\eta-2(\lambda-6)_+.
\]

unit block 若不 big，minimum 是−lambda Q，故它的真实 priced gap

\[
G=(\lambda-2)(2h-Q)+\eta+2(\lambda-6)_+\ge2a.
\]

因此 Gs+2 f_B≥2f；ragged不等式 −2min(R,|B|)+eta|B|≥−(2−eta)R 的两个分支均方向正确。27个 bounds

\[
v_p^{\rm Gauss}D_A(X)\ge-10n+\Phi_p(\lambda,\eta)+2f
\]

均合法。没有把完整 f 免费加到旧 global Omega；not-big blocks 的价格确实支付看不到的约束。也没有假定新 supported model 的36个旧 vertices 仍是其精确 dual。

在2n/3<p<17n/24，a2/Q4/h8、u=V=3p−2n，unit packet 反射闭合。lambda3/eta2价格：unit big/nonbig minima−26/−12；双 big mirror pair 加4后至少−48，big loop 加2后至少−24。所有非unit priced minima至少0，故严格 finite-n v_p D_A≥44n−72p。相对487此前已付 max(48−78x,10−24x)，交点19/27，新增面积准确

\[
1/243+1/1944=1/216.
\]

这个面积已经包括在 toric 的 common max 中，不可再加一次。T18在a1即n<p≤2n域的lambda2/eta2特殊 gap2，亦可支付2a；此附加纸面接口通过，但未进入成功源的27candidates和保存的本轮 rate，不计未兑现额外面积。

## V5. 取整跳点、certificate 与全素数转移：通过

最终 toric T6 的限定是必要的：uniform1116误差仅在固定 floor parameters 的开 cells 内。例如x1/4准确a8/h24/Q12，右开段a7/h23/Q11，不能把右 affine 值当成该 prime 的准确整数模型。有限 rational 集合 J 包含全部 floor/domain/certificate cuts；p/n∈J时用准确整数T11或原合法 fallback。每n至多O(1)个此类 primes，估值量级O(n)，付logp后总计O(n log n)=o(n²)。保留全部跳点 primes；闭 affine 端点比较仅证明积分延拓支配，不证明所有 jump primes 的 uniformO(1)。

成功源只更新[1/4,2]，其它 finite places全部继承同一487合法界。静态读源确认 literal 旧 cover、27个候选、分点和内部 intersections；affine endpoint dominance 是整段支配的精确证书。保存98 merged rows 的lo/hi/winner/gain/area和总数与源 scope 相符；213未逐存。没有重跑旧36vertex、旧prime模型或同行成功程序。

精确新主率为

\[
\Delta=\frac{589881521281691}{20345444272717200},\qquad
A_{new}=\frac{800671681093752110193539327219}
{19860629178118281482813083200}
=40.314517426059346\ldots.
\]

共同 max 的积分方向正确：提高每prime合法 valuation lower bound，降低 signed rational normalization Q_n 的安全费用。在同一 S、same whole-X source 下 D_A/Q_n∈Z[X]，主率结论是 log|Q_n^{-1}|≤A_new n²+o(n²)。正 content 可以降低这个有理尺度费用；该安全上界不是 raw最小整数 denominator 的 lower bound，不是 actual cost 下界，也不是方法 no-go。PNT 在 fixed open cells 给主率，跳点额外o(n²)已真实支付。所声明全素数费用范围通过。

## V6. 执行与读取的界限

quarter自身 DISTINCT FIRST1 为1PASS17059checks；toric自身 DISTINCT FIRST1 为1PASS12141checks。两成功源和保存 JSON 未改字节。本独审 execute/import/rerun0，external Lean0，新 primary archive/read0。仅静态读源、解析和显示已保存JSON作为资料读取，不重新产生数学验证结果。

6原S cases/30profiles/12反例是有限机制证据，不升为全尺度实际秩等式；98affine rows可结合纸面 affine 支配核全尺度积分，不替代 actual primitive 支撑、missing-constraint gap 和 whole-X 的纸面证明。没有扩大辅助 prime unit 表。

## V7. 最终判断

两份最终数学稿及其声明范围独立纸面核查通过。新证明是真实 big coefficient source 的 supported constraints、任意 selected row rank cap、左右 whole-X匹配的双份约束费、gap支付删除关系、全素数安全 same-S主率40.314517426059346。取整跳点的独立费用限定完整保留。

仍未证明 selected arbitrary-support exact image/Smith、全 mirrorgraph精确最优、无穷实际目标非零或足够解析–算术strictmargin，没有新增zeta/L/Catalan无理性或线性无关性定理。本稿正式冻结后不补未来receipt，也不将peer未来状态误写为已经实际读取。
