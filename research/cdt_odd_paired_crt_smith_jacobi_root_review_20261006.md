# 全 prime 整 CRT、可支付 Smith 层与真实 Jacobi 接口的 root 综合独审

2026-10-06，NEW 综合审阅。全部439份既有冻结数学输入和所有同行数学 producer 仅读；本审阅没有执行或 import 它们。root 自有 NEW CRT verifier 的首次一次成功与本审阅分开记账。以下“通过”指本项目内纸面独立核对，不是外部审稿、Lean 验证或特殊值无理性证明。

## V1. 本轮实际读取对象

root 实际完整读 toric 的 [第二 Smith 层稿](cdt_odd_paired_second_smith_layer_20261006.md)，最终 SHA d4572c11e52ebdc05ad5338bfe4340e98b696252a5fff6250e1a78b3448a346d，S1–S17；实际完整读 arithmetic 的 [boundary Jacobi/Krylov 稿](cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.md)，SHA 09b9e74683f4767c2a69eb5a7d67893fda1c6d6bb738d2b245f8f692fc20d17f，全部12节/K1–K26。quarter 的 [credit-cap 稿](cdt_odd_paired_smith_credit_cap_transfer_20261006.md)先完整读5548版S1–S10，再完整补读8b7368457b4e147e16a3de12e62db330ebaccc3b7da0faaa6e725842885d37b0版S8的证明归属升级与uniform rounding段；正文其他数学未变。最终完整回读另记来源收据。

root [CRT主稿](cdt_odd_paired_residue_crt_integral_model_20261006.md)最终3265da7c600ef8c1624f4208448ec35d75e32d71d92d78f4576b2cfdd5cfbd33，实际完整自读；由quarter的 [NEW正式独审](cdt_odd_paired_residue_crt_integral_model_independent_review_20261006.md)独立全文核查R1–R21。root实际完整读取该独审I1–I8；它不被当作root自己原稿的独立证明。

## V2. 相同的实际对象与精确第二层

四份稿均保留原B6/k3/s5、ambient degree<3n、actual saturated rank2n paired lattice；约束低块是C!:C diag(j!)，没有再约除新的gcd或改成更强的整数值subring。falling-to-monomial转换是整unitriangular。CRT把degree<2n的实际integer-coefficient polynomial格整同构到每个实际residue cluster的degree<L_r空间；monic resultants是p-units，因而这里没有local index。

root原稿证明全部p的权重p^j j!、mirror direct sum和actual Schur层递归。toric在n/2<p≤n、p²>8n、p>17进一步证明精确Smith multiset

\[
0^{p-M},\quad1^{n-p+M-M_4},\quad2^{M_4},
\qquad \delta_p=n-p+M+M_4.
\]

独核same-carry L2/L3/L4和loop L2/L4的最低minor：Wilson的H≤12，所有指定线性因子≤17且非零，故p>17确实足够。未知stripped单位的高阶修正不能改变已经提出column p权重后的最低determinant项。不是从mod-p rank直接猜整个Smith。

mixed L4最需要上界。实际归一化columns是1、pl、−pΓ、p²l(l−1)、−p²(3−l)Γ等。其reduction γ的二阶差为unit，所以1,l,γ独立。消unit再除p后rank恰2，三条positive指数中恰一条至少2，给lower4。若l²补rank，取高二阶column给valuation4；否则γ是非仿射quadratic，(3−l)γ的cubic项非零，改取真实low first-jet column也给valuation4。两种actual columns都在degree cutoff内，因此upper=lower，精确(0,1,1,2)。不需额外排除43/179，且不使用目标Gram unit。

## V3. 可兑现信用与安全费用方向

quarter首先不靠高层units证明rank(C! modp)≤p−M，故δ≥n−p+M。冻结weighted Plücker identity

\[
T_p=\sum_{i<3n}v_p(i!)-\delta_p
\]

把这份信用转到原whole polynomial D_A(X)；相对largest2n安全factorial费用只减δ−δ0，其中δ0=Σ_{i<n}v_p(i!)。同一个Gauss估值下界取

\[
\max\{-10n,\Lambda_p-2T_p^{safe}+2M\}.
\]

独核完整12个原raw affine段、9个paid gain段及PNT方向：先加信用，再与合法entry cap取max。可支付面积为

\[
\frac{16}{58905}+\frac{43}{2090}
+\frac1{8092}+\frac{23}{10404}+\frac1{252}
=\frac{121537}{4476780}.
\]

与前轮不交prime windows在同一对象上接合，得

\[
A_{new}^{safe}
=\frac{4624049789}{104824720}-\frac{121537}{4476780}
=\frac{790225879771}{17925027120}
\in(44.085,44.086).
\]

确切小数窗口由正分母交叉相乘即可核对。它是使liminf n^−2 logQ_n≥−A_new的安全费用上界，不是实际费用的等式或下界。固定rational a,b,X的specialization只付O(n)，但仍须另证明D_A(X)非零；费用估计不承担非零。

完整M4上层信用在1/2<x<2/3的三种head supports上，raw+4d的最高值为−280/27、−314/25、−330/23，均低于−10。root全primecapacity的额外信用Σ_mixed floor(L/2)在x∈[1/4,1/2]同样隐藏；x≤1/4用credit≤n/2与原raw≤−4/x+2+x/4完整封住tail。此结论只针对指定common-minor/cap bound-model，不是actual content或未来构造的no-go。

正常rounding、p|6n+1、p|n和endpoint均有uniform O(1)支付；p²≤8n保留旧合法all-n界，其总贡献o(n²)。Γ的解析平方信用不在finite places再次扣除。

## V4. 保留χ的共同自伴算子与Krylov真实性

回读冻结结构稿U18/U31：K3的scalar weight和matrix cross term准确是原G0、M5，不缺1/2或0-node folded factor。K5两处middle切边和两端flux确实全消，内部详细平衡来自真实Sy相邻点比，未把点值关系冒充全局rational identity。R=Sy^4在实际support为unit；B0系数给真正R^−1D0R，diag(D0,D4)通过sector常值α=2/5对原matrix form自伴。

独核最高系数、共同γ=−98/27及λ0/λ4因式：不能为两个channels分别选免费potential。整数同余把可能的零推到critical ranges之外，含r=1；degree<r和degree<3r内的四条raising chains therefore有明确单位leading coefficients，degree排序得到真正原空间的GL(Fp) basis。det平方因子准确，既不除中间norm，也不由basisunit推Gramunit。该basis仅auxiliary p-local免费，不自动给global或archimedean费用改善。

## V5. Endpoint单位机制与dense target缺口

folded Jacobi矩阵只有r−1/r切口，两个实际块维数r、4r+1，内部上下diagonal都是units。continuant递推给monic characteristic polynomials、相邻互素和每步exact degree drop1；无需simple eigenvalues。K20 resolvent的path产品与prefix/suffix cofactor符号正确，两channels共用同一C(z)，所以八源矩的recurrence阶数是N=5r+1，不是C²；阶数随r增长，未被解释成固定跨prime阶数。

K25的endpoint Hankel单位乘积由endpoint Krylov triangular matrix与详细平衡直接证明，含非正定有限域；它没有预先假设targetunit。K26证明endpoint connection degree的机制也正确：最后node非零只可能由degree m−1的最后Krylov column给出。真实outer seeds u^t、Ru^t末node均非零，connection degree恰4r。故endpoint的normality不能直接传到原dense multiseed unequal profile。此前p37的原u首Hankel为零不与这个新endpointfunctional矛盾。

严格剩余问题已具体化为K22八源Stieltjes matrix在K14真实chain lengths的modified moment minor非零。共同自伴和ambient nondegenerate都不足以证明截断非退化；不能把上述recurrence当成critical balancing定理。

## V6. 程序、文献读域与研究边界

三位同行NEW源码全部实际全文静态读取；全部JSON仅解析既存证书，不执行数学producer。toric JSON的216case全部fields先因组合输出截断、后compact完整补读；quarter全部94graph cases和76closed affine pieces逐字段compact显示并实际全读；arithmetic全部3cases/364checks与两个块的characteristic arrays完整读。没有手动重算数千matrix entries。root自有CRT JSON63cases/所有orbits也先截断后完整补读，首次成功1run，25capacity cases、9378exact identity checks；此后不重跑。

root本轮新增归档Miller–Stanton author原件16页，实际读PDF1–4、15–16六页；另实际读Costas-Santos–Johnson PDF1–4四页、Durán–Sánchez-Canales PDF1–3三页，总13页，非三份50页全文。前者给独立OP/Smith背景，第二篇的proper tridiagonal pair范围支持K18–20的一般域论证，第三篇明确quasi-definite/degree2/1等输入，不能套给本degree增4的finite-fieldtarget。本文所有新关键数学均另自足核对。

本轮补了整模型、指定窗口完整Smith和可支付费用，并建立真实norm-free算子/递推接口；仍未证明无穷辅助素数上G0、M5同时unit、actual D_A无限非零或同对象严格positive margin。当前解析已证率>12.00357285412558尚未压过safeA44.085–44.086。此比较失败不是actual最优费用下界。没有新的ζ/L/Catalan无理性、线性无关性或Lean证明；完整研究goal继续active。
