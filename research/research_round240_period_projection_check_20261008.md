# 第240轮C稿独立核对：原Euler接口PASS

2026-10-08，B。实际FULL读取目标全部五节及作者scope，无截断：

- research/global_period_projection_review_round240_20261008.md：9494 B，SHA256 **48e480e4529bc5c7132f20a1b7661056a93c7c63200ebfed77f94ec2310897a1**。
- literature/global_review_sources_round240_20261008/dual_reading_scope.md：5118 B，SHA256 **396f73f1055f60cdcdf46bedae86ede487858b16d60fc809d1adada42e6bc876**。

数学独审范围是Root指定的原对象cubical/Euler链(C5)–(C8)及其排除量词。结论 **PASS，无必要修订**。全文读取不等于本次重审Brown/Tosi全部primary、motivic投影或已有数值定理；本人本次没有另读C列出的Tosi/Brown选页，未继承作者scope为自己的阅读。

独立纸核如下。t_i=∏_(k=i)^7 x_k给正Jacobian
x₂x₃²x₄³x₅⁴x₆⁵x₇⁶。逐个D因子贡献恰为
t₃²t₅²t₇²Q；原ω的剩余monomial确为P=x₂x₄x₆。
F numerator是(t₁⋯t₇)∏(1−x_i)，所以除D后指数正是
(1,2,1,2,1,2,1)。六个q的支撑与(C5)一致。

因此V_a作用在Fⁿω密度上的monomial贡献是
nA+(a₂+a₄+a₆)，加volume divergence Σa_i后为(n+1)A。
单坐标分子给−nΣa_i x_i/(1−x_i)，Q^(−n−1)给
(n+1)Σw_jq_j/(1−q_j)。这完整支付(C6)的三部分，没有遗漏真实P或参数F。

n=0时，六个primitive exponent的1−q_j在Laurent torus中是不同irreducible divisors，generic point可避开其它所有denominator，故常数eigenform逐个强迫w_j=0。
六线性条件给a=(−b,b,−b,0,0,0,0)；此时divergence为−b，P权重为+b，所以A=0、c=0。n≥1时，先在七个不同的1−x_i generic divisors看pole即可迫a_i=0；没有用Q正性或数值有限头。

对a=(1,−1,1,−1,1,−1,1)，A=−2且只有w₂=w₃=w₄=−1，故(C8)各符号正确。唯一保留Q的方向作用在F上的三项符号也正确。该方法排除的是此坐标上的对角Euler contraction常数eigenform（即使逐n另选常数a也一样），不是非对角rational vector field、relative-boundary projector或全n D₃ cancellation的no-go。不存在这种absolute primitive不能推出原relative period禁止通道非零；目标稿已明确保留该边界。

239 tightcap/paid upper只支持暂停当前费用证书的同源优化，不能推出最优费用lower或所有CDT失败；目标稿的措辞未越界。

本次数学程序、Lean、prime/参数扫描、旧producer均0；目标稿、旧239及main/manifest未改。本收据保存后实际FULL复读与最终身份另报。
