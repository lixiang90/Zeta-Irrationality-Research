# 第225轮：真实分歧点、域上分离与univalent入口的边界

2026-10-08，Root。采用本轮[实际三模态证明](pade_actual_fourier_modes_round225_20261008.md)最终11160B/`37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`，实际FULL七节G1–G21，另独立纸核其轮廓、Stirling sector、远尾与常数。本稿支付实际径向分支的非亚纯性、原有理函数域中的分离和一个明确受限的CDT入口上限。数学程序0。

## 1. 实际对象与已付输入

令D(z)=ΣΔ_r z^r、X(z)=ΣΞ_r z^r，仍用222原三列及完整C，不换对象。令

`a=(1+cbrt(2))/(cbrt(2)−1), b=3+2√3, M=(3ab)^9, R=1/M, z₀=−R`。

C的实际主渐近给

\[
 \Delta_r=(-1)^r d r^{-33/2}M^r(1+O(r^{-1})),\qquad d>0.
\tag{S1}
\]

因此D的实际收敛半径恰R。J的实际指数上界比M严格小，且 `Ξ=−ζ(7)Δ+J`，所以X同样半径R。对H_g=gD+X，若ζ(7)=g，则它在半径严格大于R的圆盘内全纯。本稿先用C已付的223 I界即可，不依赖A尚待独审的stable改善。

这些是实际原系数列的statement；M为正实代数数，B坐标含π²而其det恒等式已经转回Δ。没有用三频率免费宣布Q上的rank3。

## 2. 径向非亚纯点：比只说不可去奇点更明确

置F(t)=D(−t/M)，则F的系数

`f_r=(−1)^rΔ_r/M^r=d r^(−33/2)(1+O(1/r))`。

有限前缀不影响以下结果。Σ|f_r|收敛，故F(t)在t↑1时有有限极限。对0<t<1逐项作16阶普通导数，

\[
 F^{(16)}(t)=\sum_{r\ge16}r^{\underline{16}}f_r t^{r-16},\qquad
 r^{\underline{16}}f_r=d r^{-1/2}(1+O(r^{-1})),
\tag{S2}
\]

其中r^{\underline{16}}=r(r−1)…(r−15)是下降阶乘。后者最终正且误差的绝对和有界。自足的Abelian估计为

\[
 \sum_{r\ge1}r^{-1/2}e^{-sr}\sim\sqrt\pi s^{-1/2}\quad(s\downarrow0).
\]

证明：乘s^(1/2)，是可积函数u^(−1/2)e^(−u)在步长s上的Riemann和；近0和远∞分别以单调积分控制，compact中一致收敛；积分为Γ(1/2)=√π。用s=−log t及t^−16→1，得到

\[
 F^{(16)}(t)\sim d\sqrt\pi(1-t)^{-1/2}.
\tag{S3}
\]

故原0芽沿负实径向到z₀不能全纯延拓。它也不能在此径向分支上亚纯延拓：若亚纯，其有限径向极限排除pole，便应是可去点而全纯，与S3矛盾。这里没有声称已经证明完整局部Puiseux展开、唯一全局奇点或所有经不同路径得到的branches都奇异。

X与gD+X在g≠ζ(7)时的同一结论，由其非零S1首项及严格小指数J直接给出。在g=ζ(7)的目标关系中，H_g于z₀全纯。这正是一个真实分歧点的选择性取消，未使用两个安全半径下界的比较。

## 3. 原Q(z)域中的确定分离与尚缺的一步

在假设ζ(7)=g∈Q时，若有 `P(z)D(z)+Q(z)H_g(z)+T(z)=0`，P,Q,T∈Q(z)，且P不恒零，则右边给P D在z₀附近亚纯。非零有理P的有限零/pole不能免除这个障碍：D=(P D)/P也亚纯，矛盾。因此任意这样的域上线性关系必有P=0。

所以D确实不能由1和H_g的Q(z)-span生成。这是field上的分离，不只是三个函数常数域上线性独立。不过

`dim_Q(z) span{1,D,H_g}=3 ⇔ H_g∉Q(z)`。

H_g非多项式尚不等于非有理；例如具有pole的有理函数也有无限非零系数。若其他稿付H_g无限非零，只能结合其完整denominator给有限radius，不能免费补上非有理或最小cyclic rank。这个尚缺接口应成为下一窗口具体任务。

## 4. 包含原D的univalent共同图受到实际上限

设φ:D_unit→C是univalent，φ(0)=0，而且原芽D∘φ延成整个unit disk上的亚纯函数。其逆函数便给原D芽在Ω=φ(D_unit)上的一个亚纯分支。若 |φ′(0)|>4R，Koebe quarter theorem保证Ω包含半径大于R的完整圆盘；它包含0到z₀的整条径向以及z₀邻域。这个分支因而必须延拓S2所用的原径向分支，违反S3。因此

\[
 |\phi'(0)|\le4R=4/M<1.
\tag{S4}
\]

这一证明**不假设Ω只要包含z₀便必然遇到同一径向分支**。当domain经过不同绕行时，不能由单一branch奇异性免费排除所有branches；Koebe提供完整圆盘后才允许本论证。

CDT固定原件Th2.5.1/Th2.7.1的holonomic入口需要 `log|φ′(0)|>τ(b)`，τ(b)≥0，并要求指定Q(z)-独立行在同一φ上亚纯。S4连最初的positive conformal条件也排除：**原变量下、保留D这一行的univalent普通图不能直接通过该入口**。不必假定flat(0,12,26)最优，也不必把difference20当微分秩。[CDT原件](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)

这不是目标ζ值无理性的反面结论，也不排除关系H_g自己的图、支付完整费用后的变量变换/代数shear、ramified/multivalent图或更精细holonomy模板。它说明下一步不能直接把“相对半径ratio很大”当作CDT的 |φ′(0)|，并继续代入166/9；共同亚纯图、arithmetical normalization和函数域rank必须真实构造。

## 5. 来源和运行边界

实际FULL读C的11160B最终数学稿及3038B来源记录；独立纸核所有必要新analytic输入，同行收据另存。Root没有执行root solver、matrix/CAS、积分、参数/素数/order扫描、PSLQ、Lean或任何producer。本稿S1的输入是C完整actual theorem，S2–S4及field分离是本稿自足推导。

实际选读固定CDT原件的完整Th2.5.1全部条件、Th2.7.1全部条件与跨页证明、Basic Remark2.11.1完整Koebe及其应用段。选段从此前冻结862628B locator提取为[完整选段](../literature/pade_singular_bridge_sources_round225_20261008/root_cdt_fixed_v2_theorems2_5_1_2_7_1_remark2_11_1.txt)，并与本轮official web原件相应段核对，不宣称全文读取220页/证明Th2.5.1整章。初次截取用不匹配的marker失败，无文件；已修复为实际marker，保存选段全文读。

另actual web读DLMF5.11固定sector/E1/E3/complex remainder条件，核C的uniform Stirling，未重复下载其已保存HTML。DLMF16.11(iii)的large-parameter E10要求特定配对shift；本对象13F12具有9n/3n参数斜率、重复参数及参数导数，不直接满足该template，故未采用其现成渐近。2.4仅打开overview，不用未读定理。16.11 HTML下载遇HTTP403，没有保存或登记新HTML FULL；这不阻碍选段和自含证明。

保存后实际全文作者复读。只新增NEW225文件，冻结旧稿/main/manifest不动。此scope以原径向分支为边界，不认证all-path singularity、最小微分秩或任何数值无理性新结论。
