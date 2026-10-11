# 原模型的源例外多项式与至少7r个浅Smith方向

2026-10-07，NEW，root。540历史冻结记录和delivery7141快照只读。纯纸证，数学producer执行/import/rerun0，辅助素数扩表0。保留原B6/κ3/s5、degree<3n、rank2n饱和格S及whole-X D_A。以下是实际局部矩阵的秩与Fitting理想结果，尚不是新的特殊值无理性定理或已闭合的CDT全局holonomy估计。

## T1. 实际输入与源的量词

取n=4r、p=18r+1素数，β∈Zp×固定，F=Fp；原源ξ=αζ4+βζ5。实际局部单位基与weak归一化为

\[
p^5 B_{\alpha,\beta,X}=D_pN_{\alpha,\beta}(X)D_p,
\quad D_p=\operatorname{diag}(1^{5r},p^{3r}),
\quad\overline N=6\bar\beta A_5.
\tag{T1}
\]

实际全文回读冻结[source稿](cdt_odd_paired_source_radical_response_20261007.md)S1–S14、[restricted-H稿](cdt_odd_paired_restricted_H_normality_20261007.md)H1–H27；实际全文读取并独立核查新[双曲单射稿](cdt_odd_paired_invisible_subform_arithmetic_20261007.md)I1–I14，候选SHA6e87aa88。其新结论已由本轮[root正式审阅](cdt_odd_paired_invisible_subform_arithmetic_independent_review_20261007.md)核对。后者若在最终冻结前变动，须按当前最终版补充审阅；本稿不从未读的未来receipt继承证明。

令K=kerA5、k=dimK≤2r，实际完成后的第一Schur剩余矩阵在K上满足

\[
\overline R_\alpha=A+8\bar\alpha G,
\quad G=G_K,\quad g=\operatorname{rank}G,
\quad\delta=k-g\le\min(k,2r-k).
\tag{T2}
\]

A保留真实β源、lift边界和modp²进位；未自由化。T2的rank下界来自实际M=(Θ;P)的2r维双曲单射，不需要A或G单位。normalized X perturbation至少p³，故第一剩余项对每个X∈Zp都相同；下面所有源例外集合都独立于X。

## T2. 明确存在的源例外多项式

在K上仅作与α、X无关的F-GL变换，把对称G分成已知非退化部分G0（g阶）及radG（δ阶）：

\[
G\sim\begin{pmatrix}G_0&0\\0&0\end{pmatrix},
\qquad A\sim\begin{pmatrix}A_{00}&A_{01}\\A_{10}&A_{11}\end{pmatrix}.
\]

只用有限域对称form的非退化补空间；p≠2保证这一步可行。它不求任何未知A块的逆。定义

\[
\boxed{f_p(a)=\det(A_{00}+8aG_0)\in F[a].}
\tag{T3}
\]

g=0时取空det=1。其他情况下degree恰g，最高系数8^g detG0非零。因此坏集合B_p={a:f_p(a)=0}有大小≤g≤2r。对每个a∉B_p，实际Rbar_a有一个明确的g阶单位主块，故rankRbar_a≥g。

T3并未假设actual整个Rbar或A11单位；f_p的选择可以依p、K和G变化。它给具体单位子块及至多g个例外，不给fixed rational α无限避免这些例外的结论。

## T3. 第一剩余秩准确控制0/1层

取与α、X无关的局部整GL基，先分开leading N的已知单位补空间（m=8r−k）及K，矩阵形状为

\[
N\sim\begin{pmatrix}U&pV\\pV^t&pW\end{pmatrix},
\quad\overline U\in\operatorname{GL}_m(F),
\quad\overline W=\overline R_a.
\tag{T4}
\]

只消去实际已知单位U，得到diag(U,pS)，其中S=W−pVᵀU⁻¹V、Smodp=Rbar_a。于是N的Smith指数（允许∞表示零方向）中，0恰m个，1恰rankRbar_a个，余下指数至少2或∞。这适用于每个X∈Zp，不能把只含modp的矩阵直接除p来计算W；T4始终沿用实际完成后的carry。

对每个a∉B_p，深方向数因而满足

\[
\boxed{\#\{\text{Smith指数}\ge2\text{或}\infty\}
\le k-g=\delta\le\min(k,2r-k)\le r.}
\tag{T5}
\]

等价地，原8r阶normalizedN至少有7r个指数≤1的方向。旧leading单位结论只保证8r−k≥6r个0层方向；本定理补上至少一半最坏缺失方向。对g0分支，k≤r，所有a适用；对k=2r分支，δ=0，T5接回已证的完整first-residual单位结论。

## T4. 7r阶Fitting理想的准确局部估值

令I_d(N)为全部d×d minors生成的理想，d=7r。DVR上的Smith说明minors共同最小估值是前d个Smith指数之和。T4–T5给对每个a∉B_p、每个X∈Zp，

\[
\boxed{v_p I_{7r}(N_{\alpha,\beta}(X))=(k-r)^+.}
\tag{T6}
\]

若k≤r，m≥7r，首7r个指数全0。若k>r，则m<7r，尚需k−r个1，而g≥2k−2r≥k−r保证足够。因此T6是准确共同最小值，不只是rank下界。某个7r阶minor非零；不必是原固定坐标内的principal minor，也不挑选尚未证明单位的原完整determinant。

也可把α、X视为形式变量，采用Qp(α,X)的p-Gauss DVR（ residue field F(α,X)）。f_p作为非零多项式是Gauss单位，T4成立，故T5/T6对这个formal源自动成立。它意味着原实际B经可逆局部规范后，至少7r阶的某个minor作为源/X有理函数不恒为零。**Formal源非零与fixed rational源无限非零是不同量词。**

T6只针对normalizedN。原B包含p^(-5)与Dp的不同strong/weak指数；GL单位基与D的行列分配不能被免费删掉。本文没有将T6写成原7r minors的精确费用，也没有把原2n行列式的解析界直接借给7r minor。

## T5. 实际leading亏秩与第四Φ亏秩不能同时极大

第四Racah已知单位的泛函为L(f)=D(mf)，其中m(u)=∏_(b<r)(u−b²)，目标完整Φ(f)=D(m²f)=L(mf)。它与真实r阶Dhigh压缩不同。记

\[
\mathscr W=\langle p_{2r}^{L},\ldots,p_{3r-1}^{L}\rangle,
\quad E_{mid}:\mathscr W\to F^r,
\quad d_\Phi=\operatorname{corank}\Phi^{[2r]}.
\]

由于L的全部所需leading norms单位，W恰为degree<3r中对全部degree<2r多项式L正交的r维空间。若q∈ker(E_mid|W)，distinct middle roots及monic m给q=mf且degf<2r；正交条件成为Φ(fR)=0（所有degR<2r）。反向每个Φ^[2r]的radical f都以mf落入W并在middle消失。因此有准确核同构

\[
\ker(E_{mid}|\mathscr W)\simeq\operatorname{rad}\Phi^{[2r]},
\quad\operatorname{rank}(E_{mid}|\mathscr W)=r-d_\Phi.
\]

新双曲单射稿I14把实际q(K0)限制在W内，I3证明E_mid在kerH上单射。因此h=dimK0≤r−dΦ，而τ=rankΘ≤r、k=h+τ，得到新的同对象缺陷相容性

\[
\boxed{k+d_\Phi\le2r.}\tag{T7}
\]

特别k=2r时，完整Φ^[2r]必为单位；这个分支也已由双曲单射给G_K单位。没有声称该分支实际发生或无限发生，没有据此推出Dhigh单位或一般source-pencil regular。T7不除Φ或off-support求值矩阵，只用已知第四norm和准确kernel identity。

## T6. 对真正研究目标的作用和限制

新增实际成果是全辅助域源例外多项式、uniform7r浅层定理、准确7r Fitting估值及T7两个实际缺陷的相容界。未解决的深方向至多r，接下来可以在这个剩余空间研究actual第一pencil的完整staircase或真实higher jets；不得把至多r自动当作这些方向可补秩。

一个p≈n的改进仍至多影响O(nlogn)局部定标，不给n²费用新信用。要转为CDT的全局holonomy或新的无理性结论，仍需同一fixed rational源的无限有效性、相应非零minor的全有限处整模型与独立解析估计，并证明严格余量。原whole-X无限非零、一般source-pencil regular、目标高压缩正常性、fixed source无限成功和特殊值无理性/线性无关性均未被T5/T6证明。

本轮root新增数学程序执行0、失败0、重跑0、旧/同行execute-import0、辅助单位素数扩表0、Lean0。本稿纯有限维纸证，无新文献下载或PDF阅读。正式独审、作者最后全文回读及一向来源收据另存；未提前声明未来核查完成。
