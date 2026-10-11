# 真实 ζ 单周期投影的非交错能量与完整实处归一化

2026-10-07。本稿针对 [统一真实对象](cdt_beta4_large_prime_tail_content_20261007.md) 第六节 L15–L23 中的 ζ 投影。作者实际全文读取该稿六节 L1–L23、[原一般 r Hermite 模型](cdt_beta_single_period_confluent_integral_model_20261007.md) 八节 B1–B29，以及 [精确算术](cdt_beta4_projection_exact_arithmetic_20261007.md) 十二节 E1–E37；此前亦实际全文读取原 β4 sec 能量稿及本轮带权稿。本文从 ζ 的正项求和重新推导，不继承 β4 的 sec 衰减、固定23非零性或旧有限处费用。

核心区别是：ζ 的真实离散测度没有交错符号，Cauchy 外积后没有 sec 的指数尾。保留全部权重仍可得到明确的一般 r≥4 的二次尺度上界，并支付所有 n²logn。该上界在 r=4、6 时具有**正**的系数，因而不能作为 ζ5、ζ7 的衰减或无理性判据。正上界不证明真实 determinant 必然增长，也不证明改进后的方法不可能成功。

## 1. 对象与已消除的全部较低周期

固定整数 r≥4，n≥1，H=rn，J={0,…,n−1}，I={n,…,rn−1}。真实内核及投影为

\[
 C_r^\zeta(u,v)=\int_0^1\int_0^1
 \frac{x^uy^v}{1-xy}\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
 =\sum_{a=1}^{\infty}\frac1{(a+u)(a+v)^r},
 \qquad E_n^\zeta=P C_r^\zeta.
 \tag{Z1}
\]

所有原级数为正项且通项 O(a^{-r-1})。定义

\[
 D(z)=\prod_{u=0}^{rn-1}(z-u),\quad
 P_J(z)=\prod_{k=0}^{n-1}(z-k),\quad
 B_k(z)=P_J(z)/(z-k),\quad Q_I(z)=\prod_{u=n}^{rn-1}(z-u),
\]

\[
 N_k(z)=B_k(z)^r
 \left[\frac{Q_I(z)}{B_k(z)^{r-1}}\right]_{k,<r},
 \qquad P_{ku}=N_k(u)/D'(u),\qquad
 F_k(z)=N_k(z)/D(z)=\sum_u\frac{P_{ku}}{z-u}.
 \tag{Z2}
\]

原完整 regular-part 身份给矩阵低节点块 (P_{kv})_{k,v∈J}=I_n 及 Σ_{u≠v}P_{ku}/(u−v)^ℓ=0，1≤ℓ≤r−1。故实际较低 ζ(2),…,ζ(r) 的全部系数消去，一阶两项先合成收敛 harmonic 差，不输入 ζ(1)。准确地，令 A_{u,a}=Σ_{j=1}^u j^{-a}，有

\[
 E_n^\zeta=q^\zeta+\zeta(r+1)I_n,
 \qquad
 q^\zeta_{kv}=(-1)^{r-1}\sum_{u\ne v}
 \frac{P_{ku}(A_{u,1}-A_{v,1})}{(u-v)^r}
 -\delta_{kv}A_{v,r+1}\in\mathbb Q.
 \tag{Z3}
\]

这些是同一实际矩阵的身份，不依赖低阶 ζ 值有理。本文始终使用 Z1–Z3 的行、列及归一化。

## 2. 公共因子与固定阶 Cauchy 外积费用

写

\[
 \frac{Q_I(k+w)}{B_k(k+w)^{r-1}}
 =a_k\sum_{\ell\ge0}h_{k,\ell}w^\ell,
 \qquad h_{k,0}=1.
\]

对 a>0，定义正的公共因子与行函数

\[
 W_n(a)=\frac{\prod_{k<n}(a+k)^{r-1}}{\prod_{u=n}^{rn-1}(a+u)},\qquad
 G_k(a)=\sum_{\ell=0}^{r-1}
 \frac{(-1)^\ell h_{k,\ell}}{(a+k)^{r-\ell}}.
 \tag{Z4}
\]

Z2 直接代入给 F_k(−a)=(−1)^r a_kW_n(a)G_k(a)，因而

\[
 E_{kv}^\zeta=(-1)^{r+1}a_k
 \sum_{a=1}^{\infty}W_n(a)G_k(a)(a+v)^{-r}.
 \tag{Z5}
\]

这就是实际非交错离散测度的精确表示。没有把它换成 β 的 sec 轮廓。

行归一化的准确绝对值与全部乘积为

\[
 |a_k|=\frac{(rn-1-k)!}{(k!)^{r-1}((n-1-k)!)^r},\qquad
 \mathcal A_{r,n}:=\left(\prod_{k<n}|a_k|\right)V_n^2
 =\frac{V_{rn}}{V_{(r-1)n}V_n^{2r-3}},
 \tag{Z6}
\]

其中 V_m=∏_{j=1}^{m-1}j!。符号 a_k=(−1)^{(r−1)(k+1)}|a_k| 在 Z5 已保留；上界才取绝对值。

为保留外积，用 Δ(a)=∏_{i<j}(a_j−a_i) 表示 Vandermonde。基本 Cauchy determinant 是 V_nΔ(a)/∏_{i,k}(a_i+k)。取每个行变元 x_k 在 k 的复圆盘半径 ρ=1/4，a_i≥1，分母无零。逐因子比较移位的 V(J) 及 Cauchy 分母，得到损失

\[
 \sum_{d=1}^{n-1}(n-d)\log(1+2\rho/d)
 +n\sum_{k=0}^{n-1}-\log(1-\rho/(1+k))
 =O(n\log(n+2)).
 \tag{Z7}
\]

行算子准确为

\[
 G_k(a)=(-1)^{r-1}
 \sum_{\ell=0}^{r-1}\frac{h_{k,\ell}}{(r-1-\ell)!}
 \partial_{x_k}^{r-1-\ell}\frac1{a+x_k}\Big|_{x_k=k}.
 \tag{Z8}
\]

h_{k,ℓ} 在求导时是该行的固定系数。它们由有限个 (1+w/(k−u)) 与 (1+w/(k−v))^{−r+1} 相乘得到；固定 ℓ≤r−1，其绝对值≤C_r(1+log(n+2))^ℓ。可用各非零差的绝对倒数调和和 O_r(log(n+2)) 及固定阶乘法逐项证明。多变量 Cauchy 导数费用每个行至多固定 r−1 阶，故由 Z7–Z8 有

\[
 |\det[G_k(a_i)]|,
 \quad |\det[(a_i+v)^{-r}]|
 \le e^{O_r(n\log(n+2))}
 \frac{V_n|\Delta(a)|}{\prod_{i,k}(a_i+k)}.
 \tag{Z9}
\]

第二式只用 (r−1) 阶行导数及固定 factorial。归一化、导数及所有 Taylor 系数都已付费，没有另借任何 ζ/β 行的小量。

对 Z5 用离散 Andreief identity，再用 Z9。两个 Cauchy 分母只消去 W 中的 P_J²，留下真实 numerator 权重

\[
 w_{r,n}(a)=\frac{\prod_{k<n}(a+k)^{r-3}}{\prod_{u=n}^{rn-1}(a+u)}.
 \tag{Z10}
\]

准确上界为

\[
 |\det E_n^\zeta|\le
 e^{O_r(n\log(n+2))}\mathcal A_{r,n}\frac1{n!}
 \sum_{a_1,\ldots,a_n\ge1}\Delta(a)^2\prod_iw_{r,n}(a_i).
 \tag{Z11}
\]

重复节点项为零。所有级数交换可先作有限截断再取极限；原 Z5 每个 entry 绝对收敛，且 Z11 右端有限，因为 w(a)=O_n(a^{-2n})，Δ(a)²≤∏_i(1+a_i)^{2(n−1)}，每个变量剩下 O_n(a_i^{-2})。因此没有隐藏非绝对的积分交换。

## 3. 整数网格到实半线及 n²logn 的准确取消

对有序不同正整数 a_i，取互不重叠的盒 t_i∈[a_i−1/4,a_i+1/4]。排序后 |a_j−a_i|≥j−i，故

\[
 \log\frac{\Delta(a)^2}{\Delta(t)^2}
 \le 2\sum_{i<j}-\log\left(1-\frac1{2(j-i)}\right)
 =O(n\log(n+2)).
 \tag{Z12}
\]

另一方面在 t≥3/4，

\[
 |(\log w_{r,n})'(t)|
 \le(r-3)\sum_{k<n}(3/4+k)^{-1}
 +\sum_{u=n}^{rn-1}(3/4+u)^{-1}
 =O_r(\log(n+2)).
 \tag{Z13}
\]

每盒体积为 2^{-n}。Z12–Z13 一致控制每个不同整数组合，并把 disjoint boxes 的积分和延拓到 (0,∞)^n，得到

\[
 \frac1{n!}\sum_{a_i\ge1}\Delta(a)^2\prod_iw(a_i)
 \le e^{O_r(n\log(n+2))}\frac1{n!}
 \int_{(0,\infty)^n}\Delta(t)^2\prod_iw(t_i)\,dt.
 \tag{Z14}
\]

实际盒下端≥3/4，所以没有使用原点处分母的导数界，也没有把无限节点数误作一个有限 n 次费用。

定义半线势

\[
 V_r(x)=\int_1^r\log(x+y)\,dy-(r-3)\int_0^1\log(x+y)\,dy,
 \qquad x\ge0.
 \tag{Z15}
\]

它在 x=0 连续，V_r(0)=rlogr−2；无穷远为 2logx+O_r(x^{-1})。关于 y 的 log(x+y) 递增，左 Riemann 和给

\[
 \sum_{k=0}^{n-1}\log(x+k/n)\le n\int_0^1\log(x+y)\,dy,
\]

\[
 \sum_{u=n}^{rn-1}\log(x+u/n)
 \ge n\int_1^r\log(x+y)\,dy
 -\log\frac{x+r}{x+1}.
\]

因此对所有 x>0，r≥4，有一致、准确的

\[
 w_{r,n}(nx)\le r\,n^{-2n}e^{-nV_r(x)}.
 \tag{Z16}
\]

换元 t_i=nx_i，Vandermonde²/Jacobian 为 n^{n²}，权重为 n^{-2n²}，故 Z11–Z16 只余 n^{-n²}。同时由 Z6 的 factorial identity 及 Stirling 求和，

\[
 \log\mathcal A_{r,n}=n^2\log n+\kappa_r n^2+O_r(n\log(n+2)),
 \quad
 \kappa_r=\frac{r^2}{2}\log r-\frac{(r-1)^2}{2}\log(r-1)-\frac32.
 \tag{Z17}
\]

所有 n²logn 精确取消。因此若

\[
 \mathcal Z_{r,n}=\frac1{n!}\int_{(0,\infty)^n}
 \Delta(x)^2e^{-n\sum_iV_r(x_i)}\,dx,
 \tag{Z18}
\]

则已严格证明

\[
 \log|\det E_n^\zeta|
 \le\kappa_r n^2+\log\mathcal Z_{r,n}+O_r(n\log(n+2)).
 \tag{Z19}
\]

这里 log0=−∞。没有先假定投影非零。

## 4. 显式半线平衡测度，包含 r4、r6

令 d=r−3，

\[
 A_r=\frac{(r-1)^2(r-4)^2}{8(r-3)(r-2)},\qquad
 b_0=\sqrt{A_r},\quad b_1=\sqrt{A_r+1},\quad b_r=\sqrt{A_r+r}.
 \tag{Z20}
\]

直接平方核验

\[
 b_r+d b_0=(r-2)b_1,
 \qquad
 \int_1^r\frac{dy}{\sqrt{A_r+y}}
 =d\int_0^1\frac{dy}{\sqrt{A_r+y}}.
 \tag{Z21}
\]

例如共同分母 √(8(r−3)(r−2)) 下，b_0、b_1、b_r 的分子分别为 (r−1)(r−4)、r²−5r+8、r²−r−4，全部非负。r=4 时 A_4=0；r=6 时 A_6=25/24。

对 y>0，在 [A_r,∞) 定义概率测度

\[
 \nu_y(dx)=\frac{\sqrt{A_r+y}}{\pi(x+y)\sqrt{x-A_r}}\,dx,
 \qquad
 \mu_r=\frac12\int_1^r\nu_y\,dy-
 \frac d2\int_0^1\nu_y\,dy.
 \tag{Z22}
\]

ν_y 的质量用 x=A_r+t² 化为半 Cauchy 积分 2b/(π(t²+b²))，准确为1；y=0 的端点按 improper integral 理解。μ_r 的质量为 ((r−1)−d)/2=1。

Z21 使 μ_r 实际为正测度。其密度为

\[
 \rho_r(x)=\frac1{2\pi\sqrt{x-A_r}}
 \left[\int_1^r\frac{\sqrt{A_r+y}}{x+y}\,dy
 -d\int_0^1\frac{\sqrt{A_r+y}}{x+y}\,dy\right],\qquad x>A_r.
 \tag{Z23}
\]

将括号写作权重 dy/√(A_r+y) 乘 (A_r+y)/(x+y)。两边权重质量由 Z21 相等，而该乘子关于 y 严格递增，正 charge 的 y≥1、负 charge 的 y≤1，故括号严格正。更显式地，积分 2b²/(t²+b²)db 得

\[
 \rho_r(x)=\frac1\pi\left[
 (r-2)\arctan\frac{b_1}{\sqrt{x-A_r}}
 -\arctan\frac{b_r}{\sqrt{x-A_r}}
 -d\arctan\frac{b_0}{\sqrt{x-A_r}}\right].
 \tag{Z24}
\]

这也可直接用 arctan 在正半轴的严格凹性及 Z21 证明正性。

r=4 的原点不是坏的 log 密度：

\[
 \rho_4(x)=\frac{2\arctan(1/\sqrt x)-\arctan(2/\sqrt x)}\pi
 \longrightarrow\frac12\quad(x\downarrow0).
 \tag{Z25}
\]

r>4 时 A_r>0，Z24 在 x↓A_r 为 O_r(√(x−A_r))；其 π/2 常数项消去。无穷远的 t^{-1} 项由 Z21 消去，故统一尾为 O_r(x^{-3/2})。因此 μ_r 有有限 log 矩及有限对数能量。它不必有有限一阶矩；后续不使用该额外假设。

## 5. 势身份及全部能量常数

记 U_η(z)=∫log|z−x|dη(x)。Z22 的半 Cauchy 换元直接给

\[
 U_{\nu_y}(z)=2\Re\log\left(\sqrt{A_r+y}+\sqrt{A_r-z}\right),
 \tag{Z26}
\]

平方根取 Re√(A_r−z)>0 的分支；在 cut 上取连续边界值。一个自足核验是：ν_y 的 Cauchy transform 经部分分式积分为 −1/[h(b+h)]，h=√(A_r−z)、b=√(A_r+y)，恰为 2log(b+h) 的导数；z→∞ 的 log|z| 常数同为零。故 x≥A_r 时 U_{ν_y}(x)=log(x+y)，而 x<A_r 时为 2log(b+√(A_r−x))。

于是

\[
 2U_{\mu_r}(x)-V_r(x)=0\quad(x\ge A_r),
 \qquad 2U_{\mu_r}(x)-V_r(x)<0\quad(0\le x<A_r).
 \tag{Z27}
\]

第二式在 A_r=0 时为空。A_r>0 时置 h=√(A_r−x)，各 ν_y 的差为 2artanh(h/√(A_r+y))。按相同的 dy/√(A_r+y) 权重，乘子 2b·artanh(h/b) 关于 b>h 严格递减：其 derivative 是 2(artanh q−q/(1−q²))<0，q=h/b∈(0,1)。Z21 的等质量和两个 y 区间给正 charge 平均严格小于负 charge 平均，因此 Z27 成立；x=0,y=0 的 improper log 奇异可积，不改变不等式。

令 w_r(y)=−d（0<y<1）或1（1<y<r），定义精确常数

\[
 J_r=-\frac12\int_0^r\int_0^r
 w_r(y)w_r(z)
 \log\left(\sqrt{A_r+y}+\sqrt{A_r+z}\right)\,dy\,dz,
 \qquad K_r=\kappa_r+J_r.
 \tag{Z28}
\]

这是有限实定积分，即使 A_4=0 的角点 log 奇异也可积。由 Z26，
∫log(x+z)dν_y(x)=U_{ν_y}(−z)=2log(√(A_r+y)+√(A_r+z))。
逐个正 measure 及有限 signed combination 的 Fubini 合法，故

\[
 I(\mu_r)=\frac12\iint w_r(y)w_r(z)\log(b_y+b_z)\,dy\,dz,
 \quad
 \int V_r\,d\mu_r=\iint w_r(y)w_r(z)\log(b_y+b_z)\,dy\,dz,
\]

\[
 I(\mu_r)-\int V_r\,d\mu_r=J_r.
 \tag{Z29}
\]

所有 constants 均来自实际 ζ 测度与 Z6 归一化，不从 β 的指数尾猜取。

## 6. 临界无穷远的准确紧化及有限 n 上界

势只有 2logx 增长，不能把半线当作已具有线性尾的 log-gas。取

\[
 x=\frac{s}{1-s},\quad0<s<1,\qquad
 U_r(s)=\int_1^r\log(y+(1-y)s)\,dy
 -d\int_0^1\log(y+(1-y)s)\,dy.
 \tag{Z30}
\]

U_r 连续延拓至 [0,1]，U_r(1)=0，U_r(0)=rlogr−2。准确地，V_r(x)=U_r(s)−2log(1−s)。另一方面 Δ(x)²=Δ(s)²∏(1−s_i)^{-2(n−1)}，dx_i=(1−s_i)^{-2}ds_i。因此 endpoint 权重**逐点完全相消**：

\[
 \mathcal Z_{r,n}=\frac1{n!}\int_{(0,1)^n}
 \Delta(s)^2e^{-n\sum_iU_r(s_i)}\,ds.
 \tag{Z31}
\]

没有遗漏从无穷远来的 Jacobian 或 endpoint 指数。

令 θ_r 为 μ_r 在 s=x/(1+x) 下的推前测度。它是 [0,1] 上紧支撑概率，尾部估计给密度≤C_r(1−s)^{-1/2}；r4 的 s0端由 Z25 有界，r>4 的左端由 Z24 也有界。任意长度 δ 的区间质量因此≤C_r√δ。θ_r 有有限 log 能量，且 c_r=∫log(1−s)dθ_r(s) 有限。

变换 logarithmic distance 得

\[
 I(\theta_r)-\int U_r\,d\theta_r=J_r,
 \quad
 2U_{\theta_r}(s)-U_r(s)\le\ell_r:=2c_r\quad(0\le s\le1),
 \tag{Z32}
\]

并在 support 上等号成立。这是 Z27 的准确紧化，log 矩的转换费用已经包括在 ℓ_r；不能默认为零。

以下直接证明有限 n 上界。对紧支撑、零总质量、各互能量有限的 real signed measure σ（允许支撑在复平面），
I(σ)=∬log|z−w|dσ(z)dσ(w)≤0。
光滑情形是 Green identity I(σ)=−(1/(2π))∫|∇U_σ|²；一般情形用小圆盘卷积，其核满足 log|d|≤K_ε(d)≤log(|d|+2ε)，在 d≠0 收敛，逐个有限互能量的 dominated convergence 保持该不等式。此处所有 circle/θ_r 互能量都有限，没有原子自能量输入。

区间质量界 C_r√δ 给 θ_r 的统一势模量

\[
 \sup_{s\in\mathbb R,\ |h|\le\varepsilon}
 |U_{\theta_r}(s+h)-U_{\theta_r}(s)|
 \le C_r\sqrt\varepsilon(1+|\log\varepsilon|),
 \quad h\in\mathbb C.
 \tag{Z33}
\]

证明分开 |s−t|≤2ε 的 layer-cake log 积分及其补集，补集用 |log|1+h/(s−t)||≤2ε/|s−t|，再二进分层；区间质量界控制全部实 s。U_r 的势模量另有 C_rε(1+|logε|)：positive charge 区间 y≥1 的 derivative 有界，negative charge 的 derivative 绝对值至多 C_r(1+|log s|)；后者直接从 ∫_0^1(1−y)/(y+(1−y)s)dy 得到。两个 endpoint 都由这些界处理。

任取 s_1,…,s_n∈[0,1]，用半径 ε=(n+1)^{-6} 的均匀复圆周替换各点，平均为 θ_ε。不同圆周互能量至少 log|s_i−s_j|；同圆周自能量准确为 logε。因此

\[
 2\sum_{i<j}\log|s_i-s_j|
 \le n^2I(\theta_\varepsilon)-n\log\varepsilon.
 \tag{Z34}
\]

把外势在复平面定义为 U_r(clamp(Re z,0,1))。每个 circle 点到其 clamp 点距离≤2ε，用 Z32–Z33 及 U_r 模量，展开 I(θ_ε−θ_r)≤0，得

\[
 I(\theta_\varepsilon)-\int U_r(\operatorname{clamp}(\Re z,0,1))d\theta_\varepsilon
 \le J_r+O_r(\sqrt\varepsilon(1+|\log\varepsilon|)).
 \tag{Z35}
\]

准确展开为 J_r+∫(2U_{θ_r}−U_r)dθ_ε−ℓ_r+I(θ_ε−θ_r)，所以不是只引用一个弱收敛变分极限。circle 平均外势与 (1/n)ΣU_r(s_i) 的差≤C_rε(1+|logε|)。Z34–Z35 给关于全部点一致的

\[
 2\sum_{i<j}\log|s_i-s_j|-n\sum_iU_r(s_i)
 \le J_rn^2+O_r(n\log(n+2)).
 \tag{Z36}
\]

有限盒 [0,1]^n 的体积为1，故 Z31 直接积分，得到

\[
 \log\mathcal Z_{r,n}\le J_r n^2+O_r(n\log(n+2)).
 \tag{Z37}
\]

无穷 endpoint 已在 Z31 精确紧化，平滑圈可越过实区间 endpoint 但 clamp 与统一模量支付了全部误差。

Z19 与 Z37 合并证明本稿的一般 r≥4 定理：

\[
 \boxed{\quad \log|\det E_n^\zeta|
 \le K_r n^2+O_r(n\log(n+2)),\quad
 K_r=\kappa_r+J_r\text{ 由 Z17、Z20、Z28 精确定义。}\quad}
 \tag{Z38}
\]

## 7. r4、r6 的准确比较与有限探索

Z28 的 50 dps 数值积分仅说明：

| r / 目标 | A_r | J_r | κ_r | K_r |
|---|---:|---:|---:|---:|
| 4 / ζ5 | 0 | −2.842333153533425 | 4.646599589952631 | +1.804266436419207 |
| 6 / ζ7 | 25/24 | −3.937924819686713 | 10.633696540678735 | +6.695771720992023 |

**正号也有独立纯符号证明。** Z32 与零质量能量说明 θ_r 是该 compact energy 的 maximizer。取原 x 半线上 [0,r] 的 uniform probability 作为有限能量 trial，则其 energy 是 logr−3/2。V_r 的 derivative 为 log((x+r)x^{r−3}/(x+1)^{r−2})，second derivative 为 (r(r−3)−2x)/(x(x+1)(x+r))。前者先从 −∞ 严格上升再下降至0的正侧，故 V_r 只有一个 minimum，[0,r] 的最大值在两个端点。于是

\[
 K_r\ge\kappa_r+\log r-3/2
 -\max\{V_r(0),V_r(r)\}.
 \tag{Z39}
\]

原势的 closed form 为
V_r(x)=(x+r)log(x+r)−(r−2)(x+1)log(x+1)+(r−3)xlogx−2。
r=4 时，Z39 减去两个 endpoint 的值分别是

\[
 10\log2-\frac92\log3-1,
 \qquad 10\log5-14\log2-\frac92\log3-1.
 \tag{Z40}
\]

r=6 时分别是

\[
 13(\log2+\log3)-\frac{25}2\log5-1,
 \qquad
 -23\log2-11\log3-\frac{25}2\log5+28\log7-1.
 \tag{Z41}
\]

用 69/100<log2<7/10、109/100<log3<11/10、8/5<log5<161/100、97/50<log7，Z40 的两项分别大于19/20、1/4，Z41 的两项分别大于403/200、999/200。因此 K_4>1/4、K_6>403/200，不依赖任何数值积分。所用 log 有理界可统一由 q=(m−1)/(m+1)、S=2Σ_{j=0}^{19}q^{2j+1}/(2j+1) 及
S<logm<S+2q^{41}/(41(1−q²))
直接有理运算核验（m=2,3,5,7）。

这仅证明 Z38 的已付费上界系数为正，不能从上界反推真实 determinant 的增长或不可能衰减。也没有证明 K_r 是实际 determinant 的最优常数。

本轮另用全新 inline Fraction 从原一般 r 基数与 Taylor 系数构造 q，再以 mpmath 220 dps 计算 q+ζ(r+1)I。固定尺度探索如下：

| r | n | sign(det E) | log\|det E\|/n² |
|---:|---:|---:|---:|
| 4 | 2 | − | 0.0766935088996190 |
| 4 | 4 | + | 0.4993563317682434 |
| 4 | 8 | + | 0.9386672961251922 |
| 6 | 2 | − | 1.4276260201008630 |
| 6 | 4 | + | 2.9380893384946310 |
| 6 | 8 | + | 4.3685283004007450 |

未作第二精度复核或区间认证，故表格只是探索，不是非零、sign-regularity、n→∞ 增长或无理性的证书。数学 Z38、Z40–Z41 不使用它。本稿没有执行旧 scripts、producer 文件、prime table、guards 或 Lean，没有新增 PDF 下载/读取。

## 8. 有限处接口与研究含义

统一稿 L19 给同一 ζ 实对象在 √(4rn)<p≤n 的 s=r+1 层相似共轭整格；它只是一段局部费用。本轮的 [完整 ζ 全素数预算](cdt_zeta_projection_all_prime_budget_20261007.md) 又针对同一实际 Z1–Z3 对象证明全部素数/高 power 的付款：C_r^ζ=2r+(r−1/2)(H_{r−1}−1)−1/(2(r+1))，其中 H_m=Σ_{j=1}^m1/j。本稿作者已实际全文读取该预算最终八节 Z1–Z25；预算的独立纸审由 root 完成，不将本次读取冒称第二次全数学独审。

具体地，ζ5 费用649/60，ζ7费用15949/840。若目标有理且真实 determinant 非零，预算给下界 −C_r^ζ n²−o_r(n²)−O(n)；本稿给上界 K_r n²+O_r(nlogn)。严格乘积公式矛盾需要 K_r<−C_r^ζ，而当前 r4/r6 的 K_r 已严格为正，所以这两项结果没有构成无理性差额。这个结论只评价已证明的上界，不声称任何模型最优性或必要费用。无限真实 determinant 非零仍待独立证明；β4 的 fixed23 种子不能迁移到 ζ5/ζ7。

这里已填补的缺口是：真实 ζ 的整个解析对象、离散测度、行导数、factorial 归一化、整数网格、临界无穷尾及准确二次尺度能量，都成为可逐式核验的同对象接口。它也明确指出 r>3 的 P_J^{r−3} 权重不能在解析付款中消失。继续寻找更小整数线性形式、不同真实列池或函数 holonomy 的方法时，应重新计算这些因素，而不是引用 β4 的 sec 或 Catalan 的旧衰减。

本稿没有证明新的 ζ 或 L 值无理性，没有证明真实投影普遍非零或正性，没有宣布整个统一框架无效。Z38 可用于核验后续对象修改是否真正取得解析压缩；若对象改变，旧费用与旧平衡测度都不能免费继承。

本稿八节 Z1–Z41 已由 root 实际全文读取并独立纸面数学审查 PASS，无实质修正请求。审读覆盖 F_k(−a) 符号、Z6 factorial 比值、两个 Cauchy 外积与真实 numerator 权重、整数 boxes、Riemann 误差及 n²logn 完整取消、ν势与平衡密度正性、外部 Frostman 条件、compact endpoint 准确相消、θ势模量、circle 有限 n 的 O(nlogn) 付款，以及 trial/endpoint 表达和四个严格粗 log 正下界。root 又以一段全新 exact inline Fraction 独立核验 m=2、3、5、7 各20项 q 展开及准确 tail，全部 log 有理界通过；四个 endpoint 严格下界亦准确复核为19/20、1/4、403/200、999/200。该独立小证书不覆盖作者六个220dps固定尺度探索或两项50dps能量积分，后者未被冒称独立复算。作者补审读记录及全素数交叉链接后完成最后实际全文回读。纸面审查、精确有限实验及文件 SHA 均不称为形式化验证。
