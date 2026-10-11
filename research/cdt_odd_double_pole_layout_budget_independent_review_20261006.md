# 双极点新布局、全素数预算与解析界：独立实际审阅

日期：2026-10-06。审阅任务 quarter_actual_rank。本文为 NEW 独审，所有旧及同行数学文件只读；没有执行、import 或重跑数学 producer，没有外部 Lean 执行。审阅通过以下明确范围，没有取得新的特殊值无理性或线性无关性定理。

## J1. 实际读取、修订历史与最终 pins

实际完整阅读 root 新稿 `cdt_odd_double_pole_layout_budget_root_20261006.md` R1–R9：初稿 SHA b28d8305e5bd20a56cbadf5a865cefbb96d478d80f8dd3d4d0adbb6215bcef30；发现 R4 的 `2Bn<2p` 不成立，作者在未冻结稿修为正确的 `Bn<2p`。之后实际完整重读最终稿，SHA **644f7dbf8e01ec85f938c49435becded48533c88577f712999b6eecb0ae7c3c5**。该修订历史保留，没有修改冻结旧稿或任何 producer。

实际完整阅读算术稿 `cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md` A1–A14：初稿1cb5ea3fd7ee2e007ae248252adc63bdac19c07b5da9dabbea0e55fb8ce45203及加入A30a后的最终 **452b9202ab3460f95e1ac5500092146cbe2ba0f9ed1e0a22bf5acb0a291fe985**，均完整纸面核验。实际完整阅读解析稿 `cdt_odd_mixed_double_pole_analytic_decay_20261006.md` A1–A9、D1–D31，最终 SHA **c4e8f04f0debe34cf896780424e6ceb256747eaca0d3ed3b9698802757447218**；包括新增的一般恢复零阶布局及三个s5严格正解析候选。

自身 NEW 整格稿 `cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md` 全文最终回读，SHA **93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8**。本文对它的引用是作者证明输入，独立外审由另外两位同行保存，不伪称自身独审自身。

本轮实际全文重读冻结 mixed H1–H9（e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463）及前轮独审 J1–J7（dfa064d0ddf9361ae48da4fd95e7b8c7816f3d459b4ccb861a679ac53291fe79）。Lai 原PDF SHA838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，本轮实际读取 **PDF7–14、17–22，共14页**；不称独立全文25页验证。7–14核binomial/residue/prime，17–19核triple-zero contour，20–22核tangent、Heine/reference与实际31的命题。读取的是完整原页文本，不借同行阅读范围冒认自身读取。没有新PDF下载。

实际完整读取新来源收据并核 SHA：

| 收据 | 最终 SHA256 |
|---|---|
| `literature/manifest_cdt_odd_mixed_double_pole_arithmetic_cost_20261006.json` | 6a78cda6cf7517cdf47a83548a7974a305dc561b46b99176d0cf8a325dfaaa88 |
| `literature/manifest_cdt_odd_mixed_double_pole_analytic_decay_20261006.json` | 3fa8dfa9dfdb0fd1cbcabc3ecd29def1a3f8b9402b127079fedfa8ca6eca0b25 |
| `literature/manifest_cdt_odd_mixed_double_pole_primitive_lattice_20261006.json` | 1cd31148e2b10f5f0878e697681b202f5d33e7ca77b6bb272c4059e5dff8b0e3 |

各稿自身source scopes与本审的14页不同，明确分开。来源收据固定的是读取/执行范围，不能替代纸面证明。

## J2. 单目标与通用无穷非零的真正比较条件

R3/A2 的U,V定义的是一个形式X多项式。只有候选有理关系成立时，X=c的实际值才等于完整解析导数和。ΣA1=0严格来自无穷远无t⁻¹项，不能略过这一步后误含较低ζ值。对degP,Q<h，新R的degree−2h−2给degreeRPQ≤−4，全部级数绝对收敛。

R4/A11 的辅助素数 proof 手核通过：n2m、p=(B+k)m+1、q=(B−k)m，q<p，N=Bn<2p且2n+N<2p。Lucas两个binomials分别降为binom(q−1,l)及binom(4m+l,l)，后者upper<p来自k>2。所有tail W unit，C leading2/p。未缩放Hermite基是Zp-unimodular；scaled基det指数3q。每个2×2 block的det为负的unit平方，整个形式X的reduction是非零常数。Dirichlet得到真正无限子列，不依赖有限参数搜索。

新增A30a保留真实normalization，准确

\[
v_p^{\mathrm{Gauss}}J=-h(s-1)-2(h-p)_+.
\]

因为h<2p，factorial fee正是2(h−p)₊。不能将scaled block的unit误当原J integral。p>s+1时Schur remainder是正unit `uD/(s+1)`，Smith exponents为q份−s、q份−(s−2)。指定辅助p给O(nlogn)，不是全素数n²实际费用下界。

## J3. 全素数算术框架及严格不等式方向

A3的整数值基导数恒等式、全部小prime ηp、A4 p>N清较长harmonic分母、A5平移基的tail/head ranks与导数额外p费，均实际手核通过。A6的m-minor估计由列展开和rank强迫head列取得s−1改善；δ仅singleton；integer translation/Cauchy–Binet保持共同minor界。

A7的ρ0是integral rank1，U0=0、V0=(s−1)!X，较强F★与capacity2q0+1正确；不把X0专属消失赋给未知有理目标。A10满rank因式分解中detDℓ=−W²U²，confluent differences付8次幂，恰恢复F的满rank值。它不证明整个det全部素数有额外免费content。

A8给所有形式系数的安全signed common multiplier Qn，`J/Qn∈Z[X]`；未证明primitive content精确。若X=u/v，须付v^h。固定a,b或目标的公共分母仅O(n)，与随n变化基格的det费用不同。A9粗费用是upper bound；A15/Fs、R5–R8的优化仍是安全valuation lower bound产生的费用upper bound，不得反向称actual denominator lower bound。

## J4. 连续LP的全尺度证明与尾段

R6离散凸函数的marginal递增（δ的两处调整仍不破坏凸性），排序填充有严格前缀最优性。在x=p/n≥ε的compact区间，q,w及cost有固定上界，每个u段的实际residue数与连续长度差O(1)，factorial与最优resource补偿亦O(1)。因此PNT求和主率由真正连续分段函数给出，不是用有限n观察猜极限。

内部阈值是0、B−Ax、(C+1)x−2、x；floor breakpoints B/j、2/j、d/j与两内部阈值交换(B+2)/j。每个cell所有marginals固定，capacity affine；累计capacity=d的根再次细分后，optimum严格affine。两个源码确实列出全部这些根与breakpoints。quarterpoint断言只是额外check，whole-cell合法性来自此纸面结构。

独立补出R6.3的计算。记f={d/x}、μ=Ew、σ²=Var(w)，忽略非负rank credit/δ，由完成平方得到

\[
g(x)\ge d\mu-ds
-x\{\sigma^2/4+f(1-f)\}
\ge-ds-\frac{(k+2)^2+4}{16}x.
\]

这里factorial项准确是−d²/x+d−xf(1−f)，与minor的d²/x抵消。μ≥0、σ²≤(k+2)²/4。此为严格全x界。

没有免费使用x→0的一致discrete/continuous error：sqrt(M)<p<εn时普适A3已给`vpJ≥−hs`，PNT直接保证该段费用≤dsεn²+o(n²)；p≤sqrtM费用o(n²)。Producer使用更保守的`dsε+[((k+2)^2+4)/32]ε²`尾费因此安全。只有x≥ε部分需要上述O(1)连续化。

## J5. 63/4的独立全尺度核验

旧B6/k3/d3，Fs−F4=−(s−4)min(m,2q)。若A=floor6/x≥2，ceil3/x≤A；各类q≥A−1足够，m≤A的tail increments≤2A−1，head increments≥4A−3。故所需3/x资源有一个只用tail的最优填充，提高s后不改变它，选中tail总量是3。

若3<x<4，三类为q1w0、q1w3、q0w5；若4<x<6，三类为q1w0、q0w2δ1、q0w5。tail increments最高1，head最低2，故仍先用全部可用tail。其weighted容量为12−2x，选中量

\[
T(x)=\min(3,12-2x),\quad
T(x)=3\ (0<x\le9/2),
\]

因而`gs−g4=−(s−4)T`且∫₀⁶T=63/4。该模型损失已严格证明，但不是actual最优算术成本随weight增加的定理。

## J6. 完整解析与恢复零阶的独立核验

D5–D7的clockwise contour与principal-part符号正确；左线完整含所有正整数，不能把右tail冒认full form。D8半整数产品、D9 Euler cosh消去、D11 derivative recurrence与显式C5均正确。D15 generating series正交性由beta integral直接自证，D16 scaling是h²，fixed derivative fee只有O(n)。signed complex measure不用假正性；Heine绝对值用正包络合法。完整旧layout严格βsafe=9log3。

s5右移的head是exact rank2n，R'''真实非零；D22mixed-Heine的1/(h−|M|)!与atom/mixed Vandermonde全部保留，不能据至少n contourvariables沿用旧31.6。

新k=s−1实际所有head导数为零。D27：increasing g的区间比较留首末各half sample，denominator额外至少log2+log(B+2)；numerator删去0到1/(2n)的integral，ratio≤16n²给log4n+1，全y≥0有效。Stirling n powers准确归为n⁻¹，常数

\[
A_{k,B}=\frac{B}{B+2}\pi^{1-k/2}e^{k/2+1/(6B)}
\]

正确。直接手微分G得到D28；G′单次negative minimum后从负侧趋0，对正λ只一次相交，D29是真正global tangent，不依赖全半轴concavity。与D16结合β=d²log(2κ/π)−dc1与prefactor(4AD/(πn))^{dn}正确。

k4、y*=1时R_B=e⁻ᶜ¹、κ_B、三个整数比较均核准，β5/6/8严格正。它们的X评价、整格/normalization、size必须逐项与算术新布局一致；既存weight4费不继承。

## J7. 三NEW producers的实际只读核查与证书范围

实际完整读下列三PY源码，**没有执行或import**：

| 文件 | SHA256 |
|---|---|
| `cdt_odd_double_pole_residue_lp_20261006.py` | bcfdb805967c864ed7e368d29f0690743d894536acc1e24ddd525e420aecad15 |
| `cdt_odd_restored_zero_layout_lp_20261006.py` | 17d51f0bc2ab2d2260f2589b61eb90f84fede8e91cfaa5aeea050f08e75ea5cd |
| `cdt_odd_double_pole_budget_certificate_verify_20261006.py` | b9b4f929f08a74b8e4864ae121038cb5d295c5e05922376f478d391dcd8843e1 |

两个LP源码的cost、capacity、factorial affine项、cut roots、integral及tail与J4对应。浮点energy/margin只作orientation，不支撑严格数值。第三源码不import producer；只读JSON并用Fraction，检查连续覆盖、exact integral一致、weight penalty及atan/log严格interval。Machin formula π=16atan(1/5)−4atan(1/239)，atan交错下一项包围、log的atanh positive absolute remainder与2^shift有向区间计算正确。root各NEW producer首次运行一次，共3次；本审执行0。

证书pins：

| JSON | SHA256 | 本审实际读取范围 |
|---|---|---|
| `cdt_odd_double_pole_residue_lp_20261006.json` | e8c4b1ee599dad8e13175fbb344dd273ec249d14e2fc0a8b0618c70bfc7f00db | metadata、summary、实际piece counts及首末rows；不称3600rows逐行独立重算 |
| `cdt_odd_restored_zero_layout_lp_20261006.json` | e17fa0dfa150914c2f53386f5efefdb52afa36e3e490a57cb042a5b88e1a38c7 | metadata、三summary及首末rows，实际counts239/239/319；不称全部797rows手算 |
| `cdt_odd_double_pole_budget_certificate_verify_20261006.json` | 58827f5454824a236318f8ab91b7a106a2c0b677e05c606126d1a8d6e18d74e3 | 实际全文，exact checks PASS；没有独审重复执行 |

因此严格区间的数字由root第一次exact certificate执行提供；本审独立验证算法、全尺度适用性及source，不假冒第二次计算。

## J8. 可报告的结论边界

本轮新已证：全形式系数的全部finite-place安全content框架；真实rank2n crossing；恢复零阶且无穷非零的通用布局；准确辅助p Smith/基指数/factorial gate；完整左线解析界、恢复布局明确β、63/4严格模型损失及可审的匹配门槛。

三个s5恢复布局已取得的算术upper bounds17.834/35.939/81.249，分别对照β区间(7.642,7.643)/(17.476,17.477)/(43.029,43.030)，**这些界未取得正margin**。这既不是新的数值定理，也不是实际成本下界或所有改进的no-go。后续需真正改善n²能量/共同content，或对新paired lattice补足basis、saturation、nonzero及所有place费用。纯normalization与同一空间基变换必须共同付费，不能创造净margin。

全文最终作者回读后本文冻结。没有改动任何旧/同行输入，数学producer执行/import/重跑0、外部Lean0、新PDF0。
