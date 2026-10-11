# Gamma 连接投影：根端独立全文审查

2026-10-07，NEW，审查者 /root，作者 /root/source_pencil_finalize。实际 FULL 读候选 `cdt_odd_gamma_connection_projection_20261007.md` G1–G19/全部七节，物理 SHA `0bb53d928dbc925dadce1e7dd2c4a1bdd148af0e7c81be4659070aeb893fff44`。580 旧冻结文件只读。结论 **PASS**：下述连接、函数秩、分母与限制纸面核查通过；未证明任何新数值无理性或 CDT strict margin。

本人本轮实际 FULL 回读上轮 period-extension E1–E24，以及 authority §§176–180。原件实际文本读域：Bloch–Vlasenko v2 PDF1、14–22（10页）；Golyshev–Mellit v1 PDF1–3（3页）；CDT 固定 v2 PDF66–69（4页）。另实际读 NIST DLMF5.7 网页5.7.3/5.7.4，不把网页计PDF页。上述17页与本轮 own contour 的 Vartanian–Zhou PDF1–8不重叠，root个人本轮共25 distinct primary PDF页。定位脚本只列页头的页不额外计全文；未执行任何数学producer或原件算法。

## R1. 真齐次系统、规范 Frobenius 与不可约条件

原 U 的倒数坐标 particular 满足 L_zU=1。其 rank-nine 齐次部分参数确为五个1/2与四个 fifth；z=Λt、Λ=2^10·5^5，有限 reflection 移到 c=1/Λ。multiplication 给 h_n=((2n)!)^5(5n)!/(n!)^15，它是五个 central binomial 与一个 multinomial 的整数乘积。

逐系数 recurrence 验证 L_tΦ=s^9t^s。使用 [s^j] 使 φ_j 最高 log 为(logt)^j/j!；j0..8恰为齐次解，j≥9须视为更高扩张。所有 a_i−1 非整数，满足 Bloch–Vlasenko Proposition26 的实参数不可约条件和 Golyshev–Mellit PDF2 的 root modulo Z 条件。conifold local exponents 为0..7、7/2，反射特征值−1，而不是 unipotent transvection。

BV Lemma24的 scalar blow-up 条件在本模型并不成立（φ0在c可有限）；作者使用的是 Proposition26，其 PDF19–20通过 contiguity 覆盖 γ≥0，适用正确。φ0在0被MUM monodromy固定；若在c也固定，其线被三个 punctures 的全部 monodromy 保持，与rank9不可约矛盾。因此 ψ=Δ_cφ0确非零。局部不变解单值 meromorphic、非负 exponents 排除 finite poles，故真正消去整个 jump 的齐次row在c holomorphic。

## R2. 整数坐标的 Gamma 行与缩放

BV的标准z-Frobenius连接行先归一化κ0=1，生成函数为 Γ(1+s)^9∏Γ(a)/∏Γ(a+s)。本文 t^s=Λ^−s z^s，故连接行必须乘Λ^−s。五个half与四个fifth multiplication 分别带2^10s与5^5s；它们与Λ^−s准确消去。于是

κ(s)=Γ(1+s)^15/[Γ(1+2s)^5Γ(1+5s)]

正确，κ1=0。ψ的规范及固定正实 continuation 路径已经指定；不是把任意一个 period 的端点值当 connection。G7只算完整 conifold reflection 行；未算其列w与整个0-to-infinity矩阵。保留 w、κ^tw=−2 作为反射一致性条件是准确边界。

## R3. 各 weight 展开与 Tate 投影

NIST5.7.4在0积分即给 logΓ(1+s)=−γs+Σ_(m≥2)(−1)^mζ(m)s^m/m，|s|<1。用于Γ(1+5s)可在|s|<1/5统一计算。15−10−5=0消去Euler项；G8全部系数随即成立。

纸面逐项指数展开：κ4=ℓ4+ℓ2²/2；κ5=ℓ5+ℓ2ℓ3；κ6=ℓ6+ℓ2ℓ4+ℓ3²/2+ℓ2³/6；κ7=ℓ7+ℓ2ℓ5+ℓ3ℓ4+ℓ2²ℓ3/2。使用标准even ζ identities，分别得到435ζ4/4、654ζ5−750ζ2ζ3、1250ζ3²−9405ζ6/16，以及11250ζ7−9810ζ2ζ5+10875ζ3ζ4/2。没有数值recognition或数学程序。

q=2πi时，ℓ2/q²=5/8、ℓ4/q⁴=−23/192，去偶exponential的E2=−5/8、E4=121/384。完整反射jump的线性组合给654ζ5/q⁵、11250ζ7/q⁷。作者保留φ1等遗漏卷积项跳跃为0的说明，且weight9会出现odd products，不把weight5/7纯化推广为所有odd coefficients。odd normalized常数纯虚，basis含q^−j及log；其Q-Taylor结构不能免费继承，单纯ζ5∈Q不等价于normalized常数在Q。

## R4. 真填洞与 Taylor 部分的完整 polynomial jump

对j≤8，Δ(φ_j−uφ0)=(κ_j−u)ψ，是完整germ等式。κ_j=u时确填c，而起点0最高log^j与u无关，仍不属Q[[t]]；有限覆盖只乘h^j。作者明确没有把η_j的分母模型移给φ_j。

在conifold小loop上logt无jump。η_j=[s^j]t^−sΦ的逆三角变换给

Δη_j=ψH_j(logt)， H_j(l)=Σ_(k0..j)κ_(j−k)(−l)^k/k!。

最高项(−l)^j/j!来自κ0=1，非零。因此η_j−κ_jη0仍有完整log polynomial jump；不是只检查其在c的leading branch coefficient。这里“logt在c正则”和“logt对C(t)超越”同时成立，没有矛盾。

## R5. C(t) 函数秩与有理 differential projection

任何r_*+Σr_jη_j=0的C(t)-relation，在绕c后给Σr_jH_j(logt)=0。ψ可在meromorphic germ域消去。logt对C(t)超越可由绕0得到无穷logt+2πiN证明；在选定无pole普通点，每个非零有限次多项式只能有有限根。因此从最高degree逐次得r_d=…=r_0=0，r_*=0，实际函数秩d+2通过。

同一论证作用于仅要求Δrow=0的组合，给当前analytic-part package中唯一不变rows是rational-function rows。它覆盖同一package的C(t)变基，但不覆盖另外的relative/dual extension或其它period实现，作者范围准确。

L全局irreducible意味着任一非零齐次解的minimal rational differential annihilator仍是L：较小operator与L的右gcd会给非平凡右因子。故一个rational differential projector若真正annihilate某个φ_j而保留φ0，会违反该条件。作者另保留映到另一系统、或只消去某个leading log而非整解的情形，未将此局部flag障碍扩大成所有投影方法no-go。

## R6. 全prime cap、holonomic与准确 CDT 参数

A_n(s)/h_n的每个 numerator reciprocal是2/(2l+1)或5/(5l+k)，denominator reciprocal是1/l。所有所用分母≤5n；negative-binomial展开系数整数，s-degree-j项准确消耗j个reciprocals。故D_(5n)^j[s^j]A_n(s)整，覆盖2、5和全部finite places；n0的η0=1、ηj=0已单独指定。系数而非导数避免额外j!。由有限triangular differential system得到holonomic性，不能把scalar函数秩等同minimal系统rank。

CDT v2 PDF66的column-step要求由d个width5嵌套columns准确满足。m=d+2、row sums(0,0,5,…,5d)、e0，定义6.0.4给

τ=5Σ_(j1..d)j(2j+3)/(d+2)²=5d(d+1)(4d+11)/[6(d+2)²]。

d5/7/8依次775/49、1820/81、129/5。全族确Q(t) independent且holonomic，但所有选定pullbacks在实际unit disk须meromorphic、map本身holomorphic；Cor6.0.14没有取消这个条件。G18写m>J/(log|φ'|−τ)是为取得矛盾的严格目标，未当已经成立的估计。

## R7. 正式结论与证据边界

本轮确实已把两个混合odd ζ目标放进真实homogeneous connection行；现有Q-Taylor analytic部分则具有明确函数秩、全prime分母和不可消去的polynomial jump。这两个事实之间的接口尚未闭合，不能由其中任一项单独宣布新数值无理性。新增文献BV Proposition26用作已证定理，PDF21–22列的其他families高κ数值例子不用于该模型的证明。

该候选通过本人FULL纸面独审，无实质修订请求。作者收读本审后须实际FULL最终回读并物理核hash，再单向FINAL收据；本文不pin mutable main、未来audit或自身。数学producer/prime实验/Lean均0，580旧文件不改。
