# 实际 compound 的周期函数接口：独立全文审阅

2026-10-07，NEW，审阅者 /root。正式对象为 [bridge 主稿](cdt_odd_paired_compound_period_module_bridge_20261007.md)，最终 SHA256 `e9e1ad8bd1553b53b7a0f901f33a9dec1fb1bedc5c51b6d2c9205d61defccc83`。根端实际 FULL 读最终六节 B1–B21；早先4c789候选的完整读取不代替这次最终读取。逐项独立纸核，结论 PASS，无实质修改请求。

## R1. 实际输入、原件与量词

本轮根端实际 FULL 读冻结 partial P1–P14、local Gram G1–G15、coupled C1–C23，以及自己稳定 Hasse 主稿 c178 的 H1–H17；这些提供同一原 B、实际整数基、正斜率和既有 fixed-source 无限6r非零。本文不宣称本轮 FULL 读 bridge 作者另列的 mechanism/target 两份旧稿，下面新证明不依赖其未展示的结论。

根端实际完整文本读三个固定存档原件：CDT2026作者20页快照 PDF3–7，CDT固定218页v2 PDF66–70，以及 Borodin26页原件 PDF2–7。针对本稿，直接核 Theorem2.1/Remark2.5、Definition6.0.1/(6.0.4–6)、Remark6.0.12 与 Corollary6.0.14。没有把归档整本页数、别版分子或同行页域当作根端实际读域。

本稿固定 n,d,α,β、每个 polynomial 和 cap 后再让 coefficient index N 与 prime p 增长；矩阵参数 n 不等于 Taylor index N。全部对象仍是 ξ=αζ(4)+βζ(5)，β≠0，不据此换源 ζ(7) 或 Catalan。

## R2. 真实周期映射、holonomicity 与函数独立秩

B1–B4的 Q_a∈Q[T]、coefficient matrix rank q≤d+1 和 Ξ=αLi4+βLi5 均准确。实 x↑1 的绝对收敛给 Q_a(ξ)；这是真实 endpoint 映射，但不自动给特殊值独立性。

绕1且不绕0的 loop 下 log x 不变，polylog monodromy 是 −2πi log^(s−1)x/(s−1)!；β≠0使 v 不恒零。对所有整数次数 k continuation，把任何 C(x)-relation变成 k 上恒零的 polynomial，最高系数 a_d v^d 消去最高项再下降。因此 1,Ξ,…,Ξ^d 在 C(x) 上独立，实际 coefficient matrix 扩域后的 rank 不变，B6恰给 q。

θ 对 total-degree≤d 的 Li1,…,Li5 monomials 保持有限 Q(x)-span，θLi1=x/(1−x)；这里仅证明每个固定 polynomial lift holonomic。随 n 增长的 determinant 序列没有因此获得一个固定有限微分系统。假设 ξ=c 有理时 endpoint 映射 rank1与真实函数秩 q 也未混淆。

## R3. 全素数 prefix 与两个精确 coefficient 见证

H清源分母后 B=Hβ≠0。p∤B 时 index p^a 的分母指数准确5a；p|B时其缺失最多5v_pB，固定 H 只增加固定费用。故 B7两侧的 L_N^5/|B|^5 与 H L_N^5有效，PNT给实际 prefix 主率5。

固定 degree j、排除有限 coefficient/leading/source primes 后，N=jp<p² 的最高 convolution 只有 (p,…,p) 能有 j 个 p-divisible indices；其余次数/terms均至少差5 valuation。因此 B8 的 −5j 是实际精确值，不只是一个下界。

首个非零 Taylor index t0∈{1,2}。j≥2 时 Np=(j−1)p+t0 不被p整除；最高次数的最低 valuation 只有 j 个 (p,…,p,t0) 排列，其 leading sum的 j和首系数均p-unit。其余 terms及全部低次数至多 j−2 个p-divisible indices。因此 B10准确为 −5(j−1)，并确实避开任意固定 N^e 的清分母作用。

## R4. 必要 cap 费用与标准 slit leaf

对固定有限斜率 b及offset，每个 LCM factor 在上述 index处最终只有0或1个p；低于阈值1/j或1/(j−1)的factor最终不含p。因此 B12非恒定 polynomial row要求σ≥5，B13 degree≥2时即使有固定N^e仍要求σ≥5。没有借此断言所有其他 period realization的必要费用。

column-step array的σ非降，degree0空间至多1维、degree≤1空间至多2维，故 B15、B16带权和分别是5(1−q^−2)、5(1−4q^−2)。固定v2定义的τsharp是非负积分与非负指数项的minimum，不能抵消这些τflat。

φ0(z)=4z/(1+z)^2确为单位盘到 C\[1,∞) 的双全纯映射；逆映射加Schwarz给所有该leaf的φ以 |φ′(0)|≤4。主稿的 log4<2<25/9比较严格。因此其明确 fixed-polynomial/finiteLCM模型中不满足CDT正分母门槛。

B21进一步使用同一实际 V_n SPD：所有d-principal minor的最高系数 detV_I>0，故实际全部minor空间maxdegree=d；full polynomial basis至少一条degree d。d≥2、q1时σ≥5；q2时至少最后σ2≥5而τflat≥15/4；q≥3沿B16。这样在允许固定N^e的模型中补齐实际 full compound 的全部q≥1。该推论不涉及丢弃高次rows的子空间、任意Q(x)换基、别的leaf或新的period实现。

## R5. Monodromy不变部分与替代过收敛接口

相同 translation argument 给 M_d 的 invariant部分恰 C(x)，而 Q-span中的constant-polynomial部分至多1维。Q(Ξ)−Q(c)保留 nonzero branch defect；B17的Hasse展开准确，所以端点归零不等于实际过收敛。

B18–B19明确是尚未构造的真实 regular-singular period system的充分接口。若实际 continuation上所有loops的branch sum均消失，拉回函数单值；regular-singular moderate growth在每个孤立preimage使其乘足够整数幂后有可去奇点，故只可能有pole。所需endpoint projection包括全部constants，不能用formal weight或residue代替。

## R6. 固定版 CDT 的严格比较与边界处理

最终 B20明确取固定v2 Corollary6.0.14/PDF68的 Jmax=双重Haar积分 log max(|φ(z)|,|φ(w)|)，而非ICM另一版的 log|φ(z)−φ(w)|。实际函数数ρ、同版(b;e)和τflat+τsharp保留；regular-singular输入提供先验holonomic条件，正分母采用该Corollary的相应relaxation。一次固定scale清rational coefficients不改变独立秩。

当φ在闭盘邻域holomorphic且φ′≠0时，边界零点孤立，Jmax有限；B20恰为该rank upper的严格反面。对仅开盘holomorphic的φ，先用φr并保留 log r费用；要么有一个实际r严格成功，要么先证合法boundary limit与uniform strict margin，不能直接用形式边界表达式。本稿没有给一个已成功的新候选。

## R7. 审查结论与证据范围

最终 e9e1 B1–B21全部纸面审查通过。新贡献为实际规范周期提升的精确函数秩、全素数与shifted-index见证、该明确CDT实现的费用障碍，以及可供另构造系统使用的完整条件接口。没有新的数值ζ/L/Catalan无理性、线性无关性或Lean结论。

数学producer创建/执行/import/rerun0、旧及同行数学运行0、辅助prime扩表0、PDF新下载0。根端全556 baseline物理SHA已另外metadata核对不变；不把哈希检查当数学验证。本审稿实际 FULL 自读后给稳定SHA，作者再实际读本审并最终FULL回读主稿，一向FINAL receipt随后建立，不pin未来receipt形成循环。
