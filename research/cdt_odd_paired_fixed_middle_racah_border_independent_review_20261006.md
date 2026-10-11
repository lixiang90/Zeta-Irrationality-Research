# 固定真实 middle Racah 与 bordered gate：独立实际审阅

2026-10-06，toric_chow_completion。NEW，全部487旧数学输入、同行producer和冻结收据只读。本审阅没有execute/import/rerun任何数学producer；本轮作者自身的另一个NEW affine FIRST1不属于本审阅的验证。本记录按实际已读域冻结，不等待未来peer finalreceipt，不引入互相依赖的hash循环。

## V1. 实际全文与物理 pins

实际完整读取作者主稿 `research/cdt_odd_paired_fixed_middle_racah_border_20261006.md` 十一节、R1–R30，全输出无截断，读取内容后的物理SHA256核对为

`2e04fe760174e006b697de7e8756cce85734f695010ac43c0f74e0fbc20e2f24`。

实际完整静态读同stem `_verify.py`，SHA
`f36a0ca4740926620306db99be3c4e07bc04c97d52ef4b67b498de410518395d`；完整读取成功JSON所有metadata和全部r1/r2/r4三cases的每字段，SHA
`c99024507adc6419cde98bef171c63c44aa4090e30075bbe4c13edb3b03f5a62`。仅静态核guard exclusive-create在数学之前、literal重建实际权重/degree profiles、Racah norms、已知D消元和真实M5det/corank机制；**未运行或import同行程序**，不将其937asserts冒称逐条人工重新运算。

实际全文读作者candidate来源receipt `literature/manifest_cdt_odd_paired_fixed_middle_racah_border_20261006.json`，当时SHA
`00f7a8ab04a4b1bd68a0872c55a651a27c431dceffe39338ac03f9f00cdd804b`；准确读域是当时candidate，未提前声称读未来final。主稿/源/JSON/三个PDF的物理hash均与这份receipt一致。本轮另实际完整回读冻结f988的十一节Z1–Z23，确认真实λ2、两个cutoffs、halfjet、第五幂种子定义和cross双端点来源。

## V2. Primary实际读取，10 distinct pages

没有新增下载/归档；以下均是作者本轮已存原件，本审阅实际完整文本读取：

- Koekoek–Swarttouw《The Askey-scheme …》，PDF28–30（printed26–28），3页：Eq1.2.1定义、Eq1.2.2权重/M/norm、Eq1.2.3/4递推及Eq1.2.5差分方程。PDF SHA `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`。
- Mañas等《Pearson Equations … I》，PDF1–3、8–9，5页：完整Gram factorization的principal minors非零前提、full N0 support、Theorem1的θ(0)=0及证明中的端点项。PDF SHA `43393a73930abe79405729233b4374dafca777dc26dd7279184083dfa48aa769`。
- Li–Long–Tu《A Whipple 7F6 Formula Revisited》，PDF1–2，2页：primitive条件、hypergeometric classical/finite-period/Galois对象区分及Katz theorem的具体输入。PDF SHA `e6ed59bdac95b1f9345520a9354847052fa222de71256dea73ef636ecf54603e`。

这10页全部在作者22页读域之内，不增加team union pages。未称读完233页归档原件。KS第一次只读PDF提取遇GBK编码中断，随后使用UTF8完整读取28–30三页；这是文本读取修复，非失败数学producer或数学rerun。没用Whipple/printedPearson定理推actual fixed-target普通性。

## V3. Halfjet、有理极限与完整单位块：通过

KS权重的含g因子对k>0严格有
\((g)_k(1+g/2)_k/(g/2)_k\to2k!\)，而k0恒1，故folded权重准确为w0=1、wk=2(-a)_k³/(a+1)_k³。不能把k0也替换成2。KS的M在α+1=−a分支专门化为(3a)!(a!)³/((2a)!)³；三个norm numerator factors准确为(-2a)_n³，与作者R8/R9相符。R7 highest coefficient的两个(-1)^j抵消，κn符号正确。

对0≤n≤a=5r，全部分子/分母因素的绝对值≤15r<p=18r+1且非零；n0空积单独合法。因此**完整**cubic profiles的norm和leading coefficients为units，R10/R11通过。这没有使用实际H0、中间M5 profile或G0的normality。完整D的已付费可逆性是真消元输入。

## V4. 同一个 actual middle 与2r门槛：通过

R15的e0=s0³/2、其余ek=S_y(k)³严格恢复R2的middle双和。真实更新VEVᵗ秩r：V有独立columns，Vᵗ满射，E可逆，故乘积秩确r，不把signed权重当positive。

R17的det/corank等式和corankH≤r只除已证单位D、E。R18 border先消−E⁻¹给(−1)^r detE⁻¹·detM5，再消D给detD·detN，因而R20的(−1)^r detE detD prefactor和corank等式均正确。R21的q=−D⁻¹(Cᵗt+Vz)、z=EVᵗq两个符号严格重建原M5核。

没有除实际H0/G0；允许这些矩阵及任意中间profiles奇异。只剩N的r×r左上块含两种实际第五幂种子A0/A1，故在它们上combineddegree≤r；没有把实际B0变成独立可调参数。R20是**同一真实目标**的等价2r门槛，不是其单位性证明。完整CD核与monic telescoping的符号、ρ_(d−1)归一化和diagonal可去极限亦通过纸面核对；不把未程序assert的diagonal公式归入有限937checks。

## V5. 真边界位移与kernel范围：通过

KS Eq1.2.5的g→0专门化在k0给B0=−a³、L0=0；直接代k>0公式会少因子2，作者未犯此误。真实ek detailed balance包含e0halfweight。Green求和保留右flux，得到R24的ωr(x_i y_j−y_i x_j)与[J,Hhat]一致。x/y独立来自R0=1与R1的unit leading coefficient、2r−1 unit，故commutator rank准确2。

λi−λj=(i−j)(i+j−15r−1)全部为units，J simple spectrum。若Hhat核含非零J-invariant子空间，存在coordinate εn；commutator迫Rn在r−1、r两点都零。r1与Rn(0)=1矛盾，r≥2用unit Lk逐级递推亦矛盾。因此R26通过。它**只排除谱不变核**，不排除混合channels的一般核，不给H0或M5unit。

## V6. 双侧Pearson与保留缺口：通过

逐entries以S(k+1)/S(k)=(k−a)/(k+a+1)检查R28，四个多项式因子准确匹配；同一变换对Z亦成立，故R30留下χ的两个真实rank1 jumps。full endpointk=a仍跨first denominator pole，必须保留冻结Z11 flux，不能用θ(0)=0或印刷factorization theorem删掉实际boundary。

整份全尺度证明在所声明范围通过。源和JSON仅验证旧r1/r2/r4机制，没有assert M5unit或增加auxiliary prime表；有限PASS不提升无限nonzero。未证明实际2r门槛在无穷prime上单位、两第五幂种子防相消、actualhigherSmith替代、足够strictmargin或新ζ/L特殊值定理。本正式审阅无未来补节计划；之后若读取peer finalreceipt，由作者NEW最终收据或root记录另外登记，保持本记录冻结只读。
