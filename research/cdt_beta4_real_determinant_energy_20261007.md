# beta(4) 真实投影行列式的 sec 轮廓与二次尺度衰减

日期：2026-10-07。本文针对同一个 r=3、H=3n、E_n=pC_3=q+β(4)I_n，不重新选择行或重定义整数格。实际全文读取了 [单周期模型](cdt_beta_single_period_confluent_integral_model_20261007.md)、[精确算术模型](cdt_beta4_projection_exact_arithmetic_20261007.md) 和 [Mellin 振荡与微分表示](cdt_beta_projection_mellin_oscillation_20261007.md)，并先检索已有 energy 稿，未发现这个真实 beta(4) 投影的已存二次尺度实处定理。

**已证主结论。** 约定 log 0=−∞，令

\[
 M=\max_{s>0}\frac{\log(1+s^2)}s,
 \qquad \kappa=\frac12+\frac32\log3-2\log2.
 \tag{R1}
\]

则对实际投影行列式，无条件有

\[
 \boxed{\quad
 \limsup_{n\to\infty}\frac{\log|\det E_n|}{n^2}
 \le \kappa+\log\frac{M}{4\pi}
 =-1.98663329925155\ldots<0.
 \quad}
 \tag{R2}
\]

精确上界由 R1 给出；小数仅说明其大小。一个不需优化 M 的较弱已证上界是 κ−log(4π)=−1.769400175…，因为 M≤1。所有巨大行归一化和至多二阶的 Cauchy 导数成本都保留在证明中；没有引用 Catalan 的 −2.290939875。R2 不证明 det E_n 非零，也不证明实处最优指数。它与现有有限处上界 771/40=19.275 尚不形成无理性差额。

## 1. 实际行与公共因子

以下 J={0,…,n−1}，I={n,…,3n−1}，并沿用

\[
 P_J(z)=\prod_{k\in J}(z-k),\quad
 Q_I(z)=\prod_{u\in I}(z-u),\quad
 B_k(z)=P_J(z)/(z-k),
\]

\[
 D=P_JQ_I,\quad
 N_k=B_k^3[Q_I/B_k^2]_{k,<3},\quad
 F_k(z)=N_k(z)/D(z)=\sum_{u=0}^{3n-1}\frac{p_{k,u}}{z-u}.
 \tag{R3}
\]

写

\[
 \frac{Q_I(k+w)}{B_k(k+w)^2}
 =a_k(1+\sigma_kw+h_{k,2}w^2+\cdots),
 \qquad h_{k,2}=\frac{\sigma_k^2+\tau_k}{2}.
 \tag{R4}
\]

原精确算术公式给

\[
 a_k=\frac{(3n-1-k)!}{(k!)^2((n-1-k)!)^3}>0,
\]

\[
 \sigma_k=\sum_{u\in I}\frac1{k-u}
 -2\sum_{v\in J\setminus\{k\}}\frac1{k-v},\qquad
 \tau_k=-\sum_{u\in I}\frac1{(k-u)^2}
 +2\sum_{v\in J\setminus\{k\}}\frac1{(k-v)^2}.
 \tag{R5}
\]

对 Re a>0，定义

\[
 W_n(a)=\frac{P_J(-a)^2}{Q_I(-a)},\qquad
 G_k(a)=\frac1{(a+k)^3}-\frac{\sigma_k}{(a+k)^2}
 +\frac{h_{k,2}}{a+k}.
\]

直接代入 R3–R4，得到准确的公共因子分解

\[
 \boxed{\ F_k(-a)=-a_kW_n(a)G_k(a).\ }
 \tag{R6}
\]

这里 a_k 不能视为一个有界常数。令 V_m=∏_{0≤j<k<m}(k−j)=∏_{j=1}^{m-1}j!，则全部行归一化的精确乘积是

\[
 \boxed{\ (\prod_{k=0}^{n-1}a_k)V_n^2
 =\frac{V_{3n}}{V_{2n}V_n^3}.\ }
 \tag{R7}
\]

这是逐个 factorial 相乘所得的恒等式。

## 2. 保留交错抵消的竖直 sec 轮廓

置 a_j=(2j+1)/4。实际内核的级数展开和 R3 给

\[
 E_{kv}=-4^{-4}\sum_{j\ge0}
 \frac{(-1)^jF_k(-a_j)}{(a_j+v)^3}.
 \tag{R8}
\]

此式对每个固定 n 绝对收敛，因为 F_k(-a)=O(a^{-1})。固定 c=1/8，令 a=c+it。若 h(a) 是 Re a≥c 上无极点的有理函数且 h(a)=O(a^{-2})，则

\[
 \boxed{\quad
 \sum_{j\ge0}(-1)^jh(a_j)
 =\int_{-\infty}^{\infty}
 h(c+it)\sec(2\pi(c+it))\,dt.
 \quad}
 \tag{R9}
\]

证明：sec(2πa) 在 a_j 的留数为 (−1)^{j+1}/(2π)。在左边 Re a=c、右边 Re a=R 的矩形上用留数定理，其中 R 取正整数。先令上下边高度趋于无穷；sec 的指数衰减使水平边积分趋零。右边有 |sec(2π(R+it))|=sech(2πt)，其积分乘 O(R^{-2}) 后趋零。左边沿向下方向给 −i 倍 R9 右侧，留数和给 −i 倍左侧，故相等。所有极点 a=−u、−v 都在左边之外；c<1/4 保证最小 sec 极点在右侧。对 R8 取 h=F_k(-a)/(a+v)^3，其衰减为 O(a^{-4})，完全符合条件。

由 R6、R8、R9，真实矩阵正好是

\[
 E_{kv}=4^{-4}a_k\int_{\mathbb R}
 W_n(a)G_k(a)(a+v)^{-3}
 \sec(2\pi a)\,dt,\qquad a=c+it.
 \tag{R10}
\]

这是同一 E 的精确身份，未先对交错级数逐项取绝对值。指数尾部来自

\[
 |\sec(2\pi(c+it))|
 \le\sqrt2\,\operatorname{sech}(2\pi t)
 \le2\sqrt2 e^{-2\pi|t|}.
 \tag{R11}
\]

## 3. Cauchy 行导数只付 o(n²)，保留两个 Vandermonde

取 ρ=1/16<c。对任意 a_i=c+it_i，基本 Cauchy 行列式为

\[
 \mathcal C(x;a)=\det_{k,i}\frac1{x_k+a_i},\qquad
 |\mathcal C(J;a)|=
 \frac{V_n|V(a)|}{\prod_{i,k}|a_i+k|}.
 \tag{R12}
\]

对全部 |ζ_k|≤ρ，在 x_k=k+ζ_k 的多圆盘中分母不为零。Cauchy double alternant 逐因子比较给

\[
 \sup_{|\zeta_k|\le\rho}|\mathcal C(J+\zeta;a)|
 \le e^{r_n}\frac{V_n|V(a)|}{\prod_{i,k}|a_i+k|},
 \tag{R13}
\]

其中可直接取

\[
 r_n=\sum_{d=1}^{n-1}(n-d)\log(1+2\rho/d)
 +n\sum_{k=0}^{n-1}-\log(1-\rho/(c+k))
 =O(n\log(n+2)).
 \tag{R14}
\]

第一项来自移位后的 V(J)；第二项来自 |a_i+k|≥c+k。k=0 只付 n log2，其余调和和仍为 O(n log n)。若 a_i 重合，两侧均因 V(a)=0 而为零，界仍成立。

精确行微分算子是

\[
 G_k(a)=\left(\frac12\partial_{x_k}^2
 +\sigma_k\partial_{x_k}+h_{k,2}\right)
 \frac1{a+x_k}\Big|_{x_k=k}.
 \tag{R15}
\]

对行列式的每一行分别应用这个算子；其 σ_k、h_{k,2} 在求导时是该行的固定系数。多变量 Cauchy 导数界及 R13 给

\[
 |\det_{k,i}G_k(a_i)|
 \le e^{r_n}\prod_k
 (|h_{k,2}|+|\sigma_k|\rho^{-1}+\rho^{-2})
 \frac{V_n|V(a)|}{\prod_{i,k}|a_i+k|}.
 \tag{R16}
\]

二阶项中的 2! 与算子 1/2 正好相消。R5 的有限调和和给 |σ_k|=O(log(n+2))、|τ_k|=O(1)，故上述系数乘积的对数为 O(n log log(n+2))，可包含在 O(n log(n+2)) 中。

另一个行列式逐行对 v 求两次导数，同样有

\[
 |\det_{v,i}(a_i+v)^{-3}|
 \le e^{r_n}\rho^{-2n}
 \frac{V_n|V(a)|}{\prod_{i,v}|a_i+v|}.
 \tag{R17}
\]

这里保留下来的 |V(a)|²=V(t)² 才是二次尺度压缩的来源。若把每个行列式先用独立的 entry 界估计，就会损失这两个 Vandermonde。

## 4. 同一 determinant 的全部因子取消

对 R10 用复测度版本的 Andreief 恒等式；它只是展开两个 determinant 并用 Fubini，所有积分由 R11 的指数尾部绝对可积。将 R16、R17 代入后，两个 Cauchy 分母与 W_n 的 P_J² **精确相消**：

\[
 \prod_i|W_n(a_i)|
 \left(\prod_{i,k}|a_i+k|^{-1}\right)^2
 =\prod_i|Q_I(-a_i)|^{-1}.
 \tag{R18}
\]

并且

\[
 |Q_I(-c-it)|=\prod_{u=n}^{3n-1}\sqrt{(u+c)^2+t^2}
 \ge\prod_{u=n}^{3n-1}u=:L_n.
 \tag{R19}
\]

所有 4^{-4n}、(2√2)^n、导数和 R13 的因子并入 exp(O(n log(n+2)))。于是得到准确归一化后的统一上界

\[
 \boxed{\quad
 |\det E_n|\le e^{O(n\log(n+2))}
 \frac{(\prod_ka_k)V_n^2}{L_n^n}\,
 \frac1{n!}\int_{\mathbb R^n}
 V(t)^2\prod_i e^{-2\pi|t_i|}\,dt_i.
 \quad}
 \tag{R20}
\]

这不是把清格后的行当作小行。R7 支付了原 a_k 的全部乘积；σ_k、h_{k,2} 和两个二阶导数的费用也已单列支付。

用 log V_m=(m²/2)log m−3m²/4+O(m log(m+2)) 及 log L_n=2n log n+(3 log3−2)n+O(log(n+2))，R7 给

\[
 \log\frac{(\prod_ka_k)V_n^2}{L_n^n}
 =-n^2\log n+\kappa n^2+O(n\log(n+2)).
 \tag{R21}
\]

以上 factorial 渐近也可直接对每个 log(j!) 使用积分比较或 Stirling 公式并求和；没有 n² log n 的未支付余项。

## 5. Cayley 圆与明确的 log-gas 上界

设 b>0，取 z_i=(t_i−ib)/(t_i+ib)，则 |z_i|=1，且

\[
 |V(t)|^2=(2b)^{-n(n-1)}|V(z)|^2
 \prod_i(b^2+t_i^2)^{n-1}.
 \tag{R22}
\]

圆上 Vandermonde 矩阵的每一行范数为 √n；Hadamard 不等式给 |V(z)|²≤n^n。因此 R20 最后的积分记作 Z_n 时，

\[
 Z_n\le\frac{n^n}{n!}(2b)^{-n(n-1)}
 \left[\int_{\mathbb R}(b^2+t^2)^{n-1}e^{-2\pi|t|}\,dt\right]^n.
 \tag{R23}
\]

按 R1，log(1+s²)≤Ms 对全部 s≥0。选择 b=nM/(2π)，变量代换 t=bs 后，

\[
\begin{aligned}
 \int_{\mathbb R}(b^2+t^2)^{n-1}e^{-2\pi|t|}\,dt
 &=b^{2n-1}\int_{\mathbb R}(1+s^2)^{n-1}e^{-nM|s|}\,ds\\
 &\le b^{2n-1}\int_{\mathbb R}(1+s^2)^{-1}\,ds
 =\pi b^{2n-1}.
\end{aligned}
 \tag{R24}
\]

最高点处的等号不造成积分困难，因保留了指数 n−1 与 n 的差；不需要添加一个未核的截断。故

\[
 Z_n\le\frac{n^n\pi^n}{n!}\,2^{-n(n-1)}b^{n^2},
\]

\[
 \log Z_n\le n^2\log n+
 \log\frac{M}{4\pi}\,n^2+O(n\log(n+2)).
 \tag{R25}
\]

R20、R21、R25 合并即证明 R2，并给更明确的 finite-n 形式

\[
 \log|\det E_n|
 \le\left(\kappa+\log\frac{M}{4\pi}\right)n^2
 +O(n\log(n+2)).
 \tag{R26}
\]

M 的唯一最大点 s_* 可自足确定：令 x_*=1+s_*²，则 x_*>2 是 log x=2−2/x 的唯一解。函数 2−2/x−log x 在 (1,2) 递增、在 (2,∞) 递减，先正后负，因此这个正最大点唯一；M=log x_*/√(x_*−1)。此外 s−log(1+s²) 的导数为 (s−1)²/(1+s²)≥0，所以 M<1。R2 的负号已经由这个简单界严格保证，不依赖小数舍入。

## 6. 单行增长与 determinant 衰减的区别

巨大归一化确实存在。例如固定 a>0、k/n→y∈(0,1)，由 gamma 比和 R6 得

\[
 \frac1n\log|F_k(-a)|\longrightarrow
 \phi(y)=-3\log3+(3-y)\log(3-y)
 -2y\log y-3(1-y)\log(1-y).
 \tag{R27}
\]

在此 r=3 模型，G_k(a)>0 且不贡献指数：原 Mellin 稿给 τ_k>0；若 x=1/(a+k)>0，则 x²−σ_kx+(σ_k²+τ_k)/2≥τ_k/2。对 n≥2，τ_k≥2−∑_{j≥1}j^{-2}>0，因 J\{k} 至少含距离 1 的点。配合 |σ_k|=O(log n)，G_k 的上下界只损失多项式因子。公共因子准确为 W_n(a)=Γ(n+a)^3/[Γ(a)^2Γ(3n+a)]；对 a_kW_n(a) 使用 Stirling 公式并将 G_k 的多项式费用归入 o(n)，即得 R27。

φ'(y)=log((1−y)^3/[y²(3−y)])，故唯一最大点 y=1/3，最大值为

\[
 \max_{0\le y\le1}\phi(y)=3\log(4/3)>0.
 \tag{R28}
\]

R27–R28 证明固定负轴点处的部分有理行指数增长；它们不是 E 的 entry 下界。R2 则已经证明实际 determinant 仍有二次尺度衰减。两个结论相容，因为 R18 保留了全部外积取消和 Vandermonde。

本轮另作有限精度探测以检查这一差别。按精确算术稿 E10、E15 直接构造原 p、q，然后计算 q+β4I；使用 Python mpmath 1.3.0 的 180 与 420 decimal digits，β4 在复核轮用 dirichlet(4,[0,1,0,−1])。这些是新的内联高精度实验，未执行旧 producer、prime、guard 或 Lean。结果只作候选行为，不作证明或非零证书。

| n | 420 dps 的 log\|det E\|/n² | log(max\|E_{kv}\|)/n |
|---:|---:|---:|
| 24 | −2.28321824764928273107 | 0.48194498411125483268 |
| 32 | −2.25857322456289611808 | 0.55951341996898164747 |
| 40 | −2.24280110285844627938 | 0.60861377349228302314 |
| 48 | −2.23185238381966413115 | 0.64397601772838296661 |
| 64 | −2.21765277119653452484 | 0.68965162570771698109 |

n=24、32 的 determinant 在 180 与 420 dps 输出中一致到展示精度；180 dps 的 n=40 determinant 已受抵消影响、符号错误，故舍弃该项而仅保存 420 dps 复核值。420 dps 的 n=48、64 未另加精度认证。这里 entry norm 增长只是有限实验观察，不宣布一般 entry 渐近。R2、R26 的证明完全不使用这张表。

## 7. 接口、费用及剩余问题

R2 是同一单周期 E_n 的无条件实处上界；不依赖其它 beta 值有理，也不依赖行空间 Chebyshev 性。Mellin 零矩所证明的 2k 次变号仍然成立，且不妨碍这里的 Cauchy 外积估计。

若假设 β4=a/b∈Q，则精确算术稿的完整整格给

\[
 b^n\widehat G_n\det E_n\in\mathbb Z,
 \qquad \log\widehat G_n\le\frac{771}{40}n^2+o(n^2).
 \tag{R29}
\]

R29 不应再加 p、Schur 或行归一化的分母。当前可证明的实处衰减常数 γ=−κ−log(M/(4π))≈1.98663，与安全有限处费用 19.275 相比仍差约 17.28837。这个比较表示现有两项上界尚未达到充分判据；它不是有限处最小费用的下界，也不证明该模型不可能成功。

在 β4 有理的反证假设下，同一 det E_n 在 n=23^j 的无限尺度非零性已由 [固定23幂次三层非零定理](cdt_beta4_fixed23_carry_transfer_20261007.md) 建立，并经 root 与本文作者独立审读通过。剩余需要证明或改进的是：真实全素数内容的进一步节省、严格费用差额，或比 R26 更锐的统一实处指数或实际极限。数值约 −2.2 的行为不能外推为最优渐近，更不能用它替换 19.275 的严证预算。本文没有证明 β(4) 无理，没有修改旧620冻结记录、旧8稿或旧算术稿，新增保存对象仅本稿。

本稿七节 R1–R29 已由 root 实际全文读取并逐式独立纸审通过，无数学修正请求；审读覆盖 sec 留数与矩形方向、原行归一化、行变元多圆盘导数费用、两个 Vandermonde 及公共因子取消、factorial 主项、Cayley 变换和 n−1 对 n 的积分差。作者在收审后完成最后全文回读。该审读是数学纸面核验，不将路径、hash 或有限高精度实验称为形式化验证。
