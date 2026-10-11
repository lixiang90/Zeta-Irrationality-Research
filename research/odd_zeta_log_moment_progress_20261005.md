# 对数矩路线：真实振荡指数、统一非零接口与剩余算术缺口

日期：2026-10-05。承接冻结的[上一轮进展](odd_zeta_explicit_relative_progress_20261004.md)。
本轮围绕 \(q=7\) 具体候选推进，而非再次作参数搜索。
已补上实际端点渐近和无穷非零要求；同时核清它在深数学中的真实位置：
合流 Jacobi–Piñeiro 多重正交与标准 polylog Padé。

**尚无 ζ(7)、Catalan 或固定混合值的新无理性证明；没有新增 Lean 形式化。**
下面区分已经证明的全尺度结果、固定反例和仍未证明的本原预算输入。
新报告另存，先前报告、证书与论文原件保持冻结。

## 1. 已证：q=7 的原始端点不是趋零族

保留显式整数候选
\[
R_{n,q}(u)=\sum_{r=0}^{qn}(-1)^r
\binom{qn}{r}\binom{n+r}{n}^{q}u^r,
\qquad
I_k(R)=\frac1{(k-1)!}\int_0^1
\frac{(-\log u)^{k-1}R(u)}{1+u}\,du.
\]
原矩恒等式没有改变。新[围道报告](odd_zeta_log_saddle_20261005.md)
从其精确 Mellin 函数推导
\[
I_k(R_{n,q})=\frac1{(k-1)!\,2\pi i}
\int M_{n,q}(z)\frac{d^{k-1}}{dz^{k-1}}
[\pi\csc(\pi z)]\,dz.
\]
\(q\ge k\) 时原矩零点消去 \(1,\ldots,n\) 的核极点。
对 \(q=k=7\)，用避开实轴剩余极点的弯折围道，
完整核统一 Gamma 估计、连接段与无穷尾部。

实际主项由一对共轭复 saddle 决定。精确代数零点 \(w_*\) 满足
\[
w_*^8+(w_*-1)^7(w_*+7)=0,\qquad
w_*\simeq1.1128731934+1.5247965276i.
\]
有理 Rouché 圆盘和外包球运算认证其存在、分支、唯一全局主峰及非退化振幅。
定义
\[
\Lambda=-\left(\frac{7(w_*-1)}{w_*+7}\right)^7,\qquad
A=\log|\Lambda|\simeq1.8178582154>1.817.
\]
则已经证明
\[
\boxed{I_7(R_{n,7})=
n^{-7/2}\operatorname{Re}(D\Lambda^n)
+O(n^{-9/2}|\Lambda|^n),\quad D\ne0.}
\]
因此
\[
\boxed{\limsup_{n\to\infty}\frac1n\log|I_7(R_{n,7})|=A>0.}
\]
而且每个充分大的相邻两项块中，至少一项非零且指数大。
这里没有假定相位是 π 的无理倍，也没有用数值拟合代替渐近证明。

这明确否定了本候选“消去最高 log 矩就使原始端点全部趋零”的设想。
但完整本原化可能带来额外节省，故**尚不能只凭原始积分增长判定本原形式失败**。
也没有证明每个单项非零或其绝对值 liminf 的准确指数。

## 2. 已证：无需预设目标无理的统一非零接口

[非零特例报告](odd_zeta_log_nonzero_20261005.md)先精确证明
\[
I_7(R_{1,7})<0,\qquad I_7(R_{8,7})>0.
\]
证书用 η(7) 的正项 Euler 展开和完全有理尾界，
没有调用 ζ(7) 的近似小数。
Euler–Rodrigues 伴随核也在两指定有理点变号。
因此普通 Rodrigues 的正核论证不能照搬到本族。

更有用的是[统一端点非零报告](odd_zeta_uniform_endpoint_nonzero_20261005.md)的简单引理：

> 对任意固定实数 \(\theta\)，若纯目标形式 \(a_n\theta+b_n\) 的候选有理根
> \(\alpha_n=-b_n/a_n\) 在无限子序列上各有一个互异素数 \(p_n\) 满足
> \(v_{p_n}(\alpha_n)<0\)，则该子序列只有有限个零项。

证明不预设 \(\theta\) 无理：一旦有零项，\(\theta\) 就是一个固定有理数；
它的分母只有有限素因子，不能与无穷互异的 \(p_n\) 相容。

整数除法 \(R=(1+u)Q+B\) 给 \(B=R(-1)>0\)。
逐素数分析已经把引理落实到两个接口：

| 固定参数／真实目标 | 无穷素数子序列 | 已证候选根估值 |
|---|---|---|
| 任意固定 \(q\ge2,k\ge2\)，\(I_k=B(1-2^{1-k})\zeta(k)+S_k\) | \(p=qn-1\) 为素数，删除明确的固定有限例外 | \(v_p[-S_k/(B(1-2^{1-k}))]=-k\) |
| 任意固定 \(q\ge2\)，\(J_G=\int_0^1(-\log t)R(t^2)/(1+t^2)\,dt=BG+S_G\) | \(p=2qn-1\) 为素数，\(n\ge2\) | \(v_p(-S_G/B)=-2-v_p(B)<0\) |

Dirichlet 定理保证这些等差素数无穷。
因此对所有这些固定权目标，指定子序列都最终非零；
阈值通常非有效，不能改称所有 \(n\) 非零。
ζ(7) 特例 \(p=7n-1\) 的局部最高分母层和完整 gcd 亦已精确证明。

这填补的是一个可统一处理的非零要求。
单项素数只支付 \(O(\log n)\) 的分母成本，仍不能直接得无理性。

## 3. 已证：真实高度、完整 gcd 与必须保留的共同因子

[算术报告](odd_zeta_log_arithmetic_20261005.md)给出目标整数系数的准确主项
\[
\boxed{B_{n,7}\sim C_7 n^{-7/2}e^{\beta_7n},
\qquad \beta_7\simeq23.1794439658.}
\]
其唯一实 saddle 来自
\((7-t)(1+t)^7=t^8\)，不是有限系数增长拟合。
于是归一化逼近误差 \(I_7/B\) 的 limsup 指数为
\(A-\beta_7\simeq-21.3615857504\)，
但同时目标系数本身指数大；归一化误差小还没有支付整数化成本。

写真实有理部分 \(S=s/M\) 已约分，则本原形式准确为
\[
\ell_n=\frac{64M}{h}I_7,\qquad
h=\gcd(63MB,64s).
\]
已经证明逐素数完整公式，并在奇素数上化简为
\[
h_{\rm odd}=\gcd(63B,s)_{\rm odd}.
\]
任何实际分母素数 \(p\mid M\)、\(p\ne2\) 都不被这个 gcd 再约掉。
这比仅检查整数分子 polynomial 的 gcd 更接近真实预算。

对于 \(n<p\le7n\)，Lucas 分块提取实际共同因子 \(C_{n,p}\)；
删去固定坏素数后
\[
C_{n,p}\not\equiv0\pmod p
\quad\Longleftrightarrow\quad v_p(M)=7
\quad\Longleftrightarrow\quad p\nmid B.
\]
单位条件不能省略。
新报告证明了无限反射族 \(p\equiv3\pmod{16},\ n=(3p-1)/8\) 上
\(C_{n,p}=0\pmod p\)；指定例 \((n,p)=(7,19)\) 有
\(v_{19}(B)=2,\ v_{19}(M)=5\)。
虽然 \(S\) 的分母少了两层，\(S/B\) 的分母仍含 \(19^7\)；
不能将局部抵消机械当成本原形式的同幅节省。

这个反射族每个尺度只强制一个异常素数，
没有证明异常集合有正比例重量，也没有否定它可能是稀薄的。

## 4. 当前缺口已经变成一个明确的素数分布输入

定义加权异常量
\[
E_n=\sum_{\substack{n<p\le7n\\C_{n,p}\equiv0\ (p)}}\log p,\qquad
e=\limsup E_n/n,
\]
固定坏素数不影响指数。
算术报告的全尺度有限不等式、真实 \(B\) 指数和围道报告的大值子序列合并给
\[
\boxed{\limsup_{n\to\infty}\frac1n\log|\ell_n|
\ge A+42-\beta_7-7e.}
\]
认证界 \(A>1.817,\ \beta_7<23.19\) 说明：
**如果 \(e\le2.94\)，至少无穷多个本原整数形式指数增长。**
这是当前具体族的条件失败判据；
\(e\le2.94\) 尚未证明，不是已得的本原排除定理。

反过来，若想沿全部尺度用此族构造趋零本原形式，就必须克服这一异常量／content 约束。
非正下界也不表示成功；特殊子序列与尺度组合仍需另核。
现在无需继续猜测是否“可能存在大 gcd”，
可直接研究明确有限和 \(C_{n,p}\) 的单位分布或实际 \(M,h\) 的指数。

## 5. 深数学定位：已接上多重正交，但仍在标准 polylog 系统

[结构报告](odd_zeta_log_structure_20261005.md)核到直接匹配的原始定理：
Smet–Van Assche 2008 的 Theorem 2.4 已处理合流 log 权，
取 \(\alpha=0\)、指标 \((n,\ldots,n)\) 即本候选，归一化和 Mellin 变量平移须明确。
这使我们可以使用真实多重正交结构，而非泛用“某系统完美”的假设。

新推导还给完整 Cauchy 身份
\[
f_j(z)=\int_0^1\frac{R(u)}{z-u}
\frac{(-\log u)^{j-1}}{(j-1)!}\,du
=R(z)\operatorname{Li}_j(1/z)-S_j(z).
\]
因此 \(1,f_1,\ldots,f_q\) 有明确的有理一阶闭合系统；
单目标 \(f_q\) 的最小齐次微分阶数确为 \(q+1\)，对 \(q=7\) 为 8。
另有 hypergeometric 标量方程与完整 log-normalized 基本解组，
但裸最高 Cauchy 分量是其 log 混合，不能直接借某个辅助解的渐近代替它。

这一体系仍是标准 polylog connection 的有理 gauge。
矩消元增加改变了高度和余项，没有自动改变解析域或 monodromy。
原始 Nikishin、Riemann–Hilbert 与强渐近论文各有真实测度、权参数、
合流和目标域条件；已读文献不能直接覆盖当前最高端点。
本轮围道分析因此是对实际目标独立完成的输入。

[本轮文献地图](../literature/log_moment_reading_map_20261005.md)保存六份原始 PDF，
逐条标明直接可用的定理与不能移植的假设。
文献识别与本项目具体推导不作为全球新颖性主张。

## 6. 下一阶段的优先任务

1. **先闭合当前族的本原预算。** 研究 \(C_{n,p}\) 的加权异常量，
   或绕过其分布直接控制 \(M/h\)。这是确定的算术问题；
   已有无限反射例必须纳入，不能预设全部大素数都是单位。
2. **若改用尺度组合，直接核整数预算。** 同时消掉共轭振荡的两个实方向，
   验证组合系数高度、残项、实际非零和共同分母；
   消一个 asymptotic 首项通常只节省多项式因子。
3. **把统一非零引理用在真正更强的 mixed 系统。**
   非零要求已有可复用的局部接口；新的关键收益应来自分母成本降低、
   多变量实指数改善或真实端点相消，而非仅增加标准 polylog 的矩阶数。

这一阶段仍同时保留原 ζ(5) 方法的二次尺度路线，
见[此前路线比较](odd_zeta_next_routes_progress_20261004.md)。
本轮没有把线性尺度 Mellin 候选替换成一个已闭合的 ζ(7) 二次尺度证明。

## 7. 交付与审阅

| 研究输入 | 书面证明 | 精确证书 |
|---|---|---|
| 实际 MB 围道、强渐近与本原条件判据 | [围道稿](odd_zeta_log_saddle_20261005.md) | [脚本](odd_zeta_log_saddle_20261005_verify.py)／[JSON](odd_zeta_log_saddle_20261005_verify.json) |
| Euler 伴随、严格变号与 ζ(7) 非零子序列 | [非零稿](odd_zeta_log_nonzero_20261005.md) | [脚本](odd_zeta_log_nonzero_20261005_verify.py)／[JSON](odd_zeta_log_nonzero_20261005_verify.json) |
| 固定权 ζ 与 Catalan 的统一非零接口 | [统一稿](odd_zeta_uniform_endpoint_nonzero_20261005.md) | [脚本](odd_zeta_uniform_endpoint_nonzero_20261005_verify.py)／[JSON](odd_zeta_uniform_endpoint_nonzero_20261005_verify.json) |
| 实际高度、素数块与完整 gcd | [算术稿](odd_zeta_log_arithmetic_20261005.md) | [脚本](odd_zeta_log_arithmetic_20261005_verify.py)／[JSON](odd_zeta_log_arithmetic_20261005_verify.json) |
| Cauchy/polylog 系统、cyclic rank 与文献范围 | [结构稿](odd_zeta_log_structure_20261005.md) | [脚本](odd_zeta_log_structure_20261005_verify.py)／[JSON](odd_zeta_log_structure_20261005_verify.json) |

[独立审阅记录](odd_zeta_log_moment_review_20261005.md)区分本人复核与其他分支复核范围。
[交付检查](odd_zeta_log_moment_delivery_20261005.json)核冻结材料散列、本地链接、
原始 PDF 字节、页数、SHA-256 与首页身份。
有限代数／球证书验证各自注明的输入；
全尺度结论依靠书面证明，尚未由 Lean 形式化。

