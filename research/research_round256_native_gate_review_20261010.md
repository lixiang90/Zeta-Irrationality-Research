# 第256轮唯一独立审查：native χ−8 全芽、整数首关与正式报告

2026-10-10。审阅者B。结论 **PASS，无必要数学修订**。本收据只认证下列实际阅读全文与逐式纸核的范围；不把系数det非零、hash或作者消息当作数值证明。B自己的作者稿由Root独立核，本文不自审。

## 1. 实际最终版本

收到最终冻结通知后，本人实际 FULL 复读Root/A/C三稿、正式报告和Root scope，工具输出无截断；此前也实际 FULL 读A/C scope。最后已读文件身份与通知一致：

| 最终文件 | bytes | SHA256 | 本审查角色 |
|---|---:|---|---|
| research/chi8_native_sensitivity_gate_round256_20261010.md | 5652 | 46cb484affbd555ba890762fff10869ff0b1c6c1c8155ee4a73762cdd9f85f86 | 独审全文5节S1–S7 |
| research/chi8_native_contour_gate_round256_20261010.md | 12037 | 7f697bd08576d4c24fcf7db1258da740503a312a62eb0290c8a2307566b84720 | 独审全文6节及全部公式 |
| research/chi8_native_integer_gate_round256_20261010.md | 12234 | 6abcbfc48af2cf3553c953c03a527059e78ede541d6526cc4806f4eb18de3877 | 独审全文7节I1–I30 |
| research/research_global_review_round256_20261010.md | 12994 | 6c83de1508263d6487df740a76c145d787a281e0a31334b7ad29d751bd9530d5 | 仅绑定B作者稿；独审者为Root |
| research/research_native_chi8_progress_round256_20261010.md | 7975 | 22fe7f3b33784d3ce11af4e77ac101acfc1f84c7dfc6c1f422359910d124cc31 | 独审完整6节报告 |

scope实际读域：Root `root_reading_scope.md` 3620 / b8113d54b8566f51406d9b98204cc01b7aaec6d702a9390a127f4b10fba79be7；A `contour_reading_scope.md` 2985 / 474538ac54027aef2a55fce05b8954ca68ff444e57c6ccf4ca5b5c297f416ba0；C `integer_reading_scope.md` 2934 / 7ad5ef3c5927842629c819ba6d4876386e8ac5a12f063b056cad80f31e5e86df；B作者 `global_reading_scope.md` 5248 / 65e3c10979b095e8a5dd755795944f08f03823489d2213026c5a6fe7c3a7bce0。以上位于 literature/native_chi8_sources_round256_20261010/。Root scope第6项明确其对B全文G1–G12的独立数学核验，不能用B作者复读代替。

## 2. 共同实际生成芽：全部indices与polar-divisor通过

独立从原积分核做partial fraction，得到A(2.1)的Stieltjes除差；r=us、r=sinθ的两个换元完整保留u因子，给(2.2)。原始绝对收敛先付实际芽，再继续，未在原实积分上非法穿越1−uts=0。

显式φ路径绕u=+1恰一次、避0与−1，初末为π/4及3π/4，参数返回同一a。固定Ω内 sinθ=uz只可能出现小根α；分子在α为0且denominator单零，导数商精确为2(1+αtanα)/[cosα(u−wuz)]，在α=0正常。其它sin解在Ω外；u−w sinθ非零；换元核无遗留1/cosθ，跨π/2合法。固定紧子域的一致控制让继续、求导和Cauchy取系数对全i,j同时交换，不需逐指标另选sheet。

实际period starts也逐式核：Abel傅里叶有可积logθ支配；old M00=4Y−πlog(1+√2)/√2，新old差为2πlog(1+√2)/a，因此3+T的N00恰16Y。plus start由φ²/u²给3π²/2，Stieltjes两值π、−3π使bar S0=0。完整diagonal reduction和两个boundary递推使全部finite heads匹配，单值 rational项被3+T乘4，未错当幂等projection。

ordinary Z的角点核可积、完整diag/offdiag harmonic heads正确，且支持[0,1]²与native [−a,a]保持分离。所有raw j<2n由同一N/Z芽有限行操作取得，π²系数完整为(3/2)[x^j](xP/√(1−2x²)−D)，故contact真消整列池。它没有支付new sheet正性、增长范数或实际det非零。

## 3. 全prefix整数与完整投影费用通过

C的μ_(2l)公式及每个p^e的floor差均正确，差为0或1，对2也适用；d_(H+1)清全部μ、U。odd prime的两个同长公差2进程，在每个p^e层计数差至少−1；2处四种parity products逐式正确。plus只用实际非零transition，H=0由starts另核，不对零transition取逆。统一2^(2H)d_H支付transition，再乘完整forcing与全部finite heads，得到q_H=2^(2H+1)d_(H+1)^3清整个矩形，未丢ordinary Z或两个period系数。

初等 d_(2m)/d_m | binom(2m,m) 的每个新增primepower层正确；dyadic递推给logq=O(H)，不需H!或prime scan。P、D完整l1高度和selected H=2n−1范围覆盖全部row degrees/raw columns。整数filter费用包含每列l1，Leibniz det界为同对象的全poly upper。

每行2^(r+1)确整除P_r、D_r的所有coefficients，故q^n/κ·Δ∈Z[T]。另一个native row尺度2^(n−r)与此因子只在乘积上相同：前者括号含dyadic rational companion，不能再免费扣一次κ。清整scalar leading6+(7/2)log2、fullpoly l1 leading6+(11/2)log2换算正确。报告将目标leading coefficient计入primitive ℓ后使用6+(9/2)log2，也正确；均为安全upper，未冒称primitive最优费或actual error lower。

## 4. Root关系敏感性、谱与primitive判据通过

S1全free-start差由i=j+2l精确求和；它不将任意g当实际canonical period。S2有限Toeplitz inverse由sqrt(1−z/2)卷积，detL=1；S3用完整R_n定义K_n，复谱按重数计，不假定实谱或正性。

normalized Δ/2^(n²)的leading恰16^n，Chebyshev交错给固定g区间sup≥2(8ε)^n；实sublevel用n个半径e^(−γn)/16根圆盘给长度≤n e^(−γn)/8。尾并集measure argument正确，但对有理点/Y无排除，报告明确保留此限制。

primitive positive-leading Z[T]多项式对非零有理scalar或invertible rational行列缩放不变；Y=u/v且值非零才有v^(−n) lower。S7要求同一无界子列实际非零与strict谱积加ℓ费用，足以矛盾有理性，但本轮没有满足它。target coefficient rank n不是该非零条件。

报告引用B的C_g-at1证书范围也准确：两个8z头抵消给(C_g/A)'=8 arcsin(az)/[a z(1−z)]；native log在1 leading−4π对全部g非零。此链由Root对B独核，本文核报告引用不越界。它只关闭直接零列在1的关系补点，不关闭完整contact/two-sheet determinant或证明其lower。

## 5. 正式报告与投入决定通过

报告将共同真实芽和exp(O(H))全整数前缀认定为本轮实质首关成功，仍明确actual Δ_n(Y)无界非零、最优primitive内容、完整两sheet strict未付。宏观表不拼接不同源预算，不重开K5/Fricke/RV默认窗口；多源Sρ<k仍要求真实代数独立/同一图，不从matrix rank领k。

唯一257是同一prototype actualY谱积或完整两sheet能源与primitive费同尺度的净可行性检查。只有无界非零加strict，或真正改变完整净预算的全尺度新证书，才支持下一有限待证接口；局部rank、旧safe upper或无primitive成本的decay不得自动续prime/map/sheet/向量窗口。投资停止不当作所有χ−8方法no-go。

formal256完成并归档后reset0、next260、latest264；连续两轮corestagnation提前。当前goal active、new numerical theorem false，无Lean认证。Root有限web检索为空且未采用结果，不把它当globalnovelty。报告的执行声明与各scope相容。

本人本轮所用primary仅实际完整保存ICM物理3–4、9–13选段（范围在B scope），未为本独审扩GET、未FULL审全部CDT/Catalan历史primary。新数学程序/finite-n/CAS/prime/map/参数/word扫描/Lean/外Git写/旧producer均0；文档FULL读取与hash不充当程序数学证明。本收据保存后实际FULL复读；只有本唯一review，不append main/policy、不执行archive。
