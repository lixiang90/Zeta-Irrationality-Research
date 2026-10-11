# 周期扩张与真实填洞稿：独立全文纸面审阅

2026-10-07，审阅者 /root。最终被审稿 [period extension relation leaf](cdt_odd_period_extension_relation_leaf_20261007.md)，SHA `30efdfedb6d4058dbf5cb0b70686f3d419a705704e1a6bb9ad70af73c850a962`。本轮实际 FULL 读全部六节、E1–E24，包括最终澄清的 holomorphic map 与 meromorphic function pullbacks。结论：在明确的同对象、已知校准、候选实现及条件性几何解释范围内纸面 PASS。没有新的ζ/L/Catalan数值无理性、线性无关性或Lean结论。

## V1. 实际审阅域与完整跳跃

本轮根端实际 FULL 读冻结 coupled C1–C23、primitive kernel K1–K18、lattice I1–I25及Hasse arithmetic J1–J18；authority实际范围为总稿§§171–175。完整JSONparse旧audit313ad、header/current_progress及572物理SHA检查不是人工全文重读全部572历史证明。5个guards实际全文读且未执行。本轮数学producer创建、execute、import、rerun、prime扩表均0。

E1的固定connection identity与指定branch足以给E2：将F_c写成V+(c−κ)A，V在该点holomorphic，所以全部local germ jump恰为(c−κ)ΔA。ΔA非零时消去整个跳跃确需c=κ。单值性与holomorphy的额外pole条件保留；多个log chains必须逐项处理。普通端点F_c(t0)=0不能推E1。有限覆盖不能消去一个非零log链。

## V2. 实际Apéry正规函数及完整整数模块

实际读GKS v3 PDF1–2、27–30六页；PDF28 literal V12的V、积分系数、LV=−12t及V0/V1准确支持E3–E5归一化。解析解在0的唯一性由递推n³的非零系数与指定constant决定，故V/12=(ζ3/6)A−B不是任意附加常数。

实际全文读Apéry1979 PDF1–4；因提取的整数模块公式模糊，另渲染并目读PDF4，确认2t_(k,n)属于由1/j³生成的整数模块，v1=6以及同一recurrence。整数正系数组合给2D_n³v_n整性，v_n=6b_n，所以保守12D_n³b_n的全prime尺度确实足够。E7支付fixed12d与constant coefficient，没有免费强化为D_n³b_n整性。

独立纸核E8：固定a=xy后z最大值为1/(1+√a)；(1−x)(1−y)≤(1−√xy)²，再对s(1−s)/(1+s)求最大，确在s=√2−1、最大平方ρ=(√2−1)^4。积分I0有限，E9逐n给I_n>0及ρ^n上界，真实holomorphic disk确扩大到ρ^−1。

E3的leading coefficient与simple-root indicial式给0、1、1/2，局部是反射而非unipotent transvection。a_n的Stirling单项与至多n+1项上界给准确radiusρ；若ΔA=0，非负指数排除pole后可穿过唯一同模singularity，与radius矛盾。因此E10是完整jump校准。固定12d、logD_n=n+o(n)与logρ^−1>3恢复已知正整数趋0矛盾；不把已知ζ3当新研究目标结果。

有理particular的所有有限pole由indicial式排除，剩余多项式最高degree经t²(θ+1)³不能等于−t，故{1,F_c}的Q(t) rank2成立。filled disk中CDT需要logr>9/2，而logρ^−1<4，说明这个简单map不足；稿中没有将scalar成功移作CDT成功。

## V3. 原ξ九阶实现的准确端点与文献假设

实际完整文本读Kerr2026 PDF1–11、19–25共18页；Kerr2020 PDF1–5五页。Kerr2026 Theorem4.11(ii)的Hodge/cycle defined overQ条件及前段motivic-generator假设明确保留；不能因几何解释而无条件推出全部奇ζ结果。

实际完整文本读Au v4 PDF1–2、8–9、19、25–29共10 distinct页，检查ExampleX所述ζ5恒等式与ExampleXV的最终组合及boundary讨论。这里使用文献已证identity，没有执行WZ notebook，也没有声称机器验证整篇论文或所有附属公式。

E11的n1确为2500/3，recurrence给radius1。E12与Au ExampleX的多项式P、w0及380928系数吻合。128/45·(π/4)^4=π⁴/90准确，选定real endpoint arctan branch使E13恰为ξ−c；没有额外ζ3或log2项。w0为ordinary point，R的branchpoints±iw0不在endpoint；此端点为零尚不提供填洞。

## V4. 指定particular的log⁹及真正有理函数rank

参数tuple关于1/2对称，E14的n≥2 recurrence及n1强迫项均正确。w=1/u、θw=−D与order9的负号给E15右端1。Frobenius family满足P9Φ=s⁹u^s，0到8阶导数为log-degree0到8的独立齐次链；9阶导数给particular，其最高log⁹系数1/9!不可被齐次解改变。

P(0)=30保持最高项，θ的正次幂只降log degree。因此G的最高系数为−30/(380928·9!)。R在infinity的固定branch为常数加analytic u-series；arctan的常数允许任一固定odd multiple of π/2，最终稿已补齐这一措辞，不能消去β非零的log⁹。有限覆盖只乘h⁹，有理非零乘子只改变Laurent阶，单值性仍失败。由此F_c非有理，{1,F_c} rank2和E18的c-independent complete module均严格成立。

有理变基保持全部function pullbacks meromorphic的module性质，scalar正阶系数和monodromy也不随c改变。common-reference障碍只属此完整实现及同一CDT数据；没有扩大到其他周期系统、子包或所有holonomy方法。

## V5. 全prime cap、缩放和CDT常数

E19的Pochhammer multiplication给3200000^n/(n⁹ binom(2n,n)^5 multinomial(5n;n^5))。逐prime逐层−5floor(2x)−floor(5x)≥−9，p^k>5n时归零，所以n⁹D_(5n)^9清分母，包括2、5。P(n)为整数；fixed380928、45及source分母必须另付，已由M支付。

arctan(w/w0)的dyadic 2^(10n)不能由fixedscale或该LCM免费吸收。最终w=1024s明确消去这项；arctan⁴的四个indices分别整除D_n，D_n⁴清每个卷积项。与U cap共同给E22，constant−c亦付M。endpoint、1/1024与±i/3125 singular positions同时改变。

实际完整文本读CDT固定v2 PDF66–69四页，直接核Theorem6.0.2与Cor.6.0.14：九列(0,5)给flat135/4；e=(0,9)由Basic Remark6.0.17的3/4按正比例乘9，给sharp27/4、总81/2。R、G及其和均holonomic，允许用该条件降低conformal-size前提，但仍要求holomorphic φ本身以及其function pullbacks meromorphic。

原稿E24的“meromorphic pullback φ”术语已在未冻结稿中改清楚；最终30ef的E18/E24明确φ为holomorphic map。缩放φ=ψ/1024使derivative-log与double integral分子同减log1024，E24支付这一费用。没有已找到的strict余量；81/2是此safe cap参数，非optimal lower或所有方法障碍。

## V6. 本轮审查结果和个人primary读域

全部E1–E24/六节在上述scope内PASS，最终术语与branch常数措辞修订后实际全文再读，hash30ef核一致。本文使用primary页共47 distinct：GKS6、Apéry4、Kerr2020五、Kerr2026十八、Au十、CDT四。根端相位主稿另外Deaño7、AMS5十二页，与这47页不重复，所以根端本轮primary合计59页。归档整本数不等于实际阅读；没有继承同行页域。

仍缺把原ξ实现为控制完整connection jump的κ，或在原Gram路线证明足够真实核/phase n²增益。Apéry是已知成功校准，九阶ξ实现是一项完整候选及其局限性证明，均不替代新数值结果。本文全文自读及作者收审后最终回读由最终单向收据闭合；不pin未来audit、未来收据或mutable main。
