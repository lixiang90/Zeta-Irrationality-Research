# beta(4) 同一真实行列式的带权平衡测度与改进实处界

日期：2026-10-07。对象仍是 [原 sec 轮廓稿](cdt_beta4_real_determinant_energy_20261007.md) 的 r=3、H=3n、E_n=pC_3=q+β(4)I_n；本文不改变行、周期投影、行归一化或整数格。作者实际全文读完该稿七节 R1–R29 后，保留 R19 所舍弃的 Q_I 随虚部变化的权重。以下给出自足的对数势论证明，不以浮点计算、Catalan 旧常数或通用 log-gas 极限定理作为证书。

## 1. 主结论与准确常数

沿用 κ=1/2+(3/2)log3−2log2。置

\[
 c=2\pi,\qquad
 a=\sqrt{\frac{5-\sqrt{13}}6},\qquad
 \alpha(x)=\frac12\int_1^3\log(1+x^2/y^2)\,dy,
 \qquad V(x)=c|x|+\alpha(x).
 \tag{W1}
\]

在 (−a,a) 定义正密度

\[
 \rho(x)=\frac{c}{\pi^2}
 \log\frac{a+\sqrt{a^2-x^2}}{|x|}
 +\frac{\sqrt{a^2-x^2}}{2\pi}
 \int_1^3\frac{y\,dy}{(x^2+y^2)\sqrt{a^2+y^2}},
 \tag{W2}
\]

其值在 x=0 可视为 +∞，不影响积分；在其余实轴上置零。令 μ(dx)=ρ(x)dx，并定义

\[
 U_0=-\frac{ca}{\pi}
 +\frac12\int_1^3\bigl(\log y-\operatorname{arsinh}(y/a)\bigr)\,dy,
 \qquad
 J=U_0-\frac12\int_{-a}^{a}V(x)\rho(x)\,dx,
 \qquad \gamma_{\rm w}=-\kappa-J.
 \tag{W3}
\]

**已证。** 约定 log0=−∞，对同一实际 E_n 无条件有

\[
 \boxed{\ \log|\det E_n|
 \le-\gamma_{\rm w}n^2+O(n\log(n+2)).\ }
 \tag{W4}
\]

全部常数由 W1–W3 的定积分精确定义。并且严格有

\[
 \gamma_{\rm w}\ge
 \log4+\frac32-\kappa
 +\frac{a^2}{6}
 \left(\arctan\frac3a-\arctan\frac1a\right)
 >\log4+\frac32-\kappa.
 \tag{W5}
\]

后者已经超过原 Cayley 界的常数 −κ−log(M/(4π))。60 位 mpmath 数值积分只用于说明大小：a≈0.4820872542973956，J≈−2.899458284795456，γ_w≈2.137834212913182。W4、W5 的证明不使用这些小数。

## 2. 保留全部 Q_I 权重，尺度与 factorial 完整支付

原稿 R3–R18 的 sec 轮廓、两个行导数 Cauchy determinant、Andreief 恒等式及 P_J² 精确取消保持原样。记 A_n=(∏_k a_k)V_n²=V_{3n}/(V_{2n}V_n³)，L_n=∏_{u=n}^{3n-1}u。未执行 R19 的粗界时，得到

\[
 |\det E_n|\le e^{O(n\log(n+2))}A_n\frac1{n!}
 \int_{\mathbb R^n}V(t)^2
 \prod_i\frac{e^{-c|t_i|}}{|Q_I(-1/8-it_i)|}\,dt_i.
 \tag{W6}
\]

这里积分中的 V(t) 是 Vandermonde，势函数 V(x) 由 W1 定义；两者仅记号沿用，意义由自变量及上下文区分。原稿已经支付 a_k 的全部乘积、σ_k/h_{k,2} 系数、两个至多二阶行导数、多圆盘移位及 4^{-4n} 的费用。本文没有在这些项目后再次加费或移除因子。

对 t=nx，因为 f_x(y)=(1/2)log(1+x²/y²) 关于 y>0 递减，左 Riemann 和给**准确的不等式**

\[
\begin{aligned}
 |Q_I(-1/8-it)|
 &\ge\prod_{u=n}^{3n-1}\sqrt{u^2+t^2}\\
 &=L_n\exp\left(\sum_{u=n}^{3n-1} f_x(u/n)\right)
 \ge L_n e^{n\alpha(x)}.
\end{aligned}
 \tag{W7}
\]

它对所有实 x 及所有 n≥1 一致成立，无 x→∞ 的 Riemann 余项。定义

\[
 \mathcal Z_n=\frac1{n!}
 \int_{\mathbb R^n}\prod_{i<j}(x_i-x_j)^2
 e^{-n\sum_iV(x_i)}\,dx_1\cdots dx_n.
 \tag{W8}
\]

将 t_i=nx_i 代入 W6，Vandermonde² 与 Jacobian 合计 n^{n(n−1)+n}=n^{n²}，因此

\[
 |\det E_n|\le e^{O(n\log(n+2))}
 \frac{A_n}{L_n^n}\,n^{n^2}\mathcal Z_n.
 \tag{W9}
\]

原稿的 factorial 计算 R21 原封不动给

\[
 \log(A_n/L_n^n)=-n^2\log n+\kappa n^2+O(n\log(n+2)).
 \tag{W10}
\]

所以剩下只需证明 log𝒵_n≤Jn²+O(nlogn)。这里没有未付的 n²logn，也没有把归一化后的大行误作小行。

## 3. 直接构造概率平衡测度

令 ω_a(dx)=dx/(π√(a²−x²)) 为 [−a,a] 上的 arcsine 概率测度。对 y>0，定义另一概率测度

\[
 \nu_y(dx)=\frac{y\sqrt{y^2+a^2}}{x^2+y^2}\,\omega_a(dx).
 \tag{W11}
\]

它的质量由 ∫ω_a(dx)/(x²+y²)=1/(y√(y²+a²)) 给出。再令

\[
 d\lambda_a(x)=\frac{c}{\pi^2}
 \log\frac{a+\sqrt{a^2-x^2}}{|x|}\,dx
 =\frac c\pi\int_0^a d\omega_s(x)\,ds.
 \tag{W12}
\]

后一等式从 ∫_{|x|}^a ds/√(s²−x²)=arcosh(a/|x|) 直接得到；λ_a 质量为 ca/π。考察有限符号组合

\[
 \mu=\lambda_a+\frac12\int_1^3\nu_y\,dy-\frac{ca}{\pi}\omega_a.
 \tag{W13}
\]

其质量准确为 ca/π+1−ca/π=1。选 a 满足

\[
 \frac{ca}{\pi}=
 \frac12\int_1^3\frac{y\,dy}{\sqrt{y^2+a^2}}
 =\frac12\left(\sqrt{9+a^2}-\sqrt{1+a^2}\right).
 \tag{W14}
\]

当 c=2π 时，W14 是 4a=√(9+a²)−√(1+a²)。其唯一正解满足 a²=(5−√13)/6：平方化简给 3a⁴−5a²+1=0，小根满足未平方的正号条件，大根不满足 √(1+a²)=1/a−2a>0。原差函数严格递减，4a 严格递增，也独立证明唯一性。

把 W14 代入 W13，用

\[
 \frac{y\sqrt{y^2+a^2}}{x^2+y^2}
 -\frac y{\sqrt{y^2+a^2}}
 =\frac{y(a^2-x^2)}{(x^2+y^2)\sqrt{y^2+a^2}},
 \tag{W15}
\]

即得到 W2 的正密度。因此 μ 是概率测度，且 ρ(x)≤C(1+|log|x||)，对数能量有限。W13 中的负 arcsine 项不能单独丢弃；它已经由 W14、W15 准确并入正密度。

## 4. 实轴上的势恒等式及严格外部不等式

记 U_η(z)=∫log|z−x|dη(x)。arcsine 的 Cauchy transform 是 1/√(z²−a²)，平方根取 z→∞ 时渐近 z 的分支。由 W11 的部分分式和 W12 的 arcsine 积分，准确得到

\[
 G_{\lambda_a}(z)=\frac c\pi\arcsin(a/z),
 \qquad
 G_{\nu_y}(z)=
 \frac{z+y\sqrt{y^2+a^2}/\sqrt{z^2-a^2}}{z^2+y^2}.
 \tag{W16}
\]

前式也可逐个使用 ∫_0^a ds/√(z²−s²)。后式中的 z=±iy 是可去奇点，身份在其余点成立后由连续性延拓。

在 (−a,a) 的实轴内，ω_a 的 principal-value transform 为零；ν_y 的实部 transform 为 x/(x²+y²)；λ_a 的 real principal value 为 (c/2)signx（把 W12 中 0<s<|x| 的实部积分计算即可）。故在 x≠0 的内部，

\[
 2U_\mu'(x)=c\operatorname{sign}x+
 \int_1^3\frac{x\,dy}{x^2+y^2}=V'(x).
 \tag{W17}
\]

μ 和 V 偶对称，其势连续，所以两侧区间的常数相同，x=0 也由连续性连接。

对 x>a，W13、W16 给

\[
\begin{aligned}
 (2U_\mu-V)'(x)
 &=c\left(\frac2\pi\arcsin(a/x)-1\right)\\
 &\quad+\frac1{\sqrt{x^2-a^2}}
 \left[\int_1^3\frac{y\sqrt{y^2+a^2}}{x^2+y^2}\,dy
 -\frac{2ca}{\pi}\right]<0.
\end{aligned}
 \tag{W18}
\]

第一项严格负。第二项括号在 x=a 时由 W14 为零，随 x>a 严格下降。负半轴由偶对称处理。因此存在 ℓ 使

\[
 2U_\mu(x)-V(x)=\ell\quad(|x|\le a),
 \qquad 2U_\mu(x)-V(x)<\ell\quad(|x|>a).
 \tag{W19}
\]

现在计算常数。由 W12，U_{λ_a}(0)=(ca/π)(log(a/2)−1)，U_{ω_a}(0)=log(a/2)。直接以 x=a sinθ 计算 W11 的 log|x| 积分，或积分 W16 在 imaginary axis 上的 transform，得到

\[
 U_{\nu_y}(0)=\log y-
 \log\frac{y+\sqrt{y^2+a^2}}a
 =\log y-\operatorname{arsinh}(y/a).
 \tag{W20}
\]

一种不需要求奇异 log 积分的核验如下：设 R_y=(y+√(y²+a²))/a，对 s>0，由 W16 积分且按 s→∞ 取 log s 的渐近，可得

\[
 U_{\nu_y}(is)=
 \log\frac{s+\sqrt{s^2+a^2}}2
 +\log\left(1-\frac1{R_s^2R_y^2}\right).
 \tag{W21}
\]

对 s 求导正好是 iG_{ν_y}(is)；两边在无穷远的常数同为零。令 s↓0，并使用 y=(a/2)(R_y−R_y^{-1})，即得 W20。W13 因而给 U_μ(0)=U_0，且 V(0)=0，所以 ℓ=2U_0。

对 W19 按 μ 积分，记 I(μ)=∬log|x−y|dμ(x)dμ(y)，有 2I(μ)−∫Vdμ=ℓ，于是

\[
 I(\mu)-\int V\,d\mu=
 \ell/2-\frac12\int V\,d\mu=J.
 \tag{W22}
\]

这证明 W3 所定义 J 正是该候选的带权能量；下一节还会直接证明它给出所需有限 n 上界。

## 5. 从势恒等式到有限 n 积分上界

以下写出所用能量与平滑事实，避免把“存在平衡测度”当作未验证的黑箱。

**零质量能量事实。** 对紧支撑、总质量零、有限对数能量的实符号测度 σ 在复平面上，有

\[
 I(\sigma)=\iint\log|z-w|\,d\sigma(z)d\sigma(w)\le0.
 \tag{W23}
\]

对光滑密度，令 U_σ=∫log|z−w|dσ(w)，则 ΔU_σ=2πσ。总质量零保证 U_σ=O(|z|^{-1})、∇U_σ=O(|z|^{-2}) 在无穷远成立，Green 公式给 I(σ)=−(1/(2π))∫|∇U_σ|²。一般情形用小圆盘卷积平滑并令半径趋零；本文涉及的 μ、圆周测度及它们的有限和具有可积的 log 奇异，卷积后的能量收敛到原能量。具体地，半径 δ 的两次均匀圆盘卷积所得核 K_δ(z−w) 由 subharmonic mean inequality 满足 log|z−w|≤K_δ(z−w)≤log(|z−w|+2δ)，且在 z≠w 时趋于 log|z−w|。各正测度互积上的 log 负部可积，因此 dominated convergence 逐个证明互能量收敛，再组合成符号测度能量。ρ≤C(1+|log|x||) 与圆周的弧长密度保证本文各互积的这一可积性。

**一致势连续性。** 对本文 μ 和 0<ε<1/4，有

\[
 \sup_{x\in\mathbb R,\ |h|\le\varepsilon}
 |U_\mu(x+h)-U_\mu(x)|
 \le C\varepsilon\bigl(1+|\log\varepsilon|\bigr)^2,
 \qquad h\in\mathbb C.
 \tag{W24}
\]

证明可完全由密度上界得到：任何长度 d≤1 的实区间质量≤Cd(1+|log d|)。分开 |x−u|≤2ε 与其补集。在近区，两个 log 奇异的 layer-cake 积分均≤Cε(1+|logε|)²；复数移位的距离至少等于对应实部距离，且在近区距离≤3ε，故同一估计适用。远区用 |log|1+h/(x−u)||≤2ε/|x−u|，再按 ε<|x−u|≤1 的二进壳层求和，得到相同阶；更远部分为 O(ε)。所有界关于实 x 一致。

V 是全局 Lipschitz 函数，且 V(x)≥c|x|。令 λ_n=1−1/n，n≥2。由 W19 及 U_μ(x)≤log(|x|+a) 对 |x|>a，存在与 n 无关的 R、C，使

\[
 \sup_{x\in\mathbb R}
 \bigl(2U_\mu(x)-\lambda_nV(x)\bigr)
 \le\ell+C/n.
 \tag{W25}
\]

具体地，取 R 足够大使 2log(|x|+a)−V(x)/2≤ℓ 对 |x|≥R 成立；这在 λ_n≥1/2 时控制外部。内部 |x|≤R 用 W19 及 V(x)/n≤max_{[-R,R]}V/n 即可。这一步留下了一整份 V 来支付最后的无限区间积分。

任取实点 x_1,…,x_n；重复点使 Vandermonde 为零，可直接跳过。把每个点用半径 ε=(n+1)^{-2} 的均匀圆周替换，令 ν_ε 为这些圆周概率测度的平均。圆周 log 势是 log max(|z−x_i|,ε)。两次应用 subharmonic mean inequality，不同中心圆周的互能量至少为 log|x_i−x_j|；同中心的自能量准确为 logε。因此

\[
 2\sum_{i<j}\log|x_i-x_j|
 \le n^2 I(\nu_\varepsilon)-n\log\varepsilon.
 \tag{W26}
\]

使用 σ=ν_ε−μ 的 W23，并把 V 延拓为 V(Re z)，展开平方能量，W24、W25 给

\[
 I(\nu_\varepsilon)-\lambda_n\int V(\Re z)\,d\nu_\varepsilon(z)
 \le J+C/n+C\varepsilon(1+|\log\varepsilon|)^2.
 \tag{W27}
\]

细节是展开后等于 J+∫(2U_μ−λ_nV)dν_ε−ℓ+I(σ)：因为 I(μ)−λ_n∫Vdμ 与减去 ∫(2U_μ−λ_nV)dμ 正好合成 −I(μ)，没有漏掉 (1−λ_n)∫Vdμ。实轴上的 supremum 用 W25，离实轴的 U_μ 差用 W24。V 的 Lipschitz 性另给 ∫V(Re z)dν_ε=(1/n)∑V(x_i)+O(ε)。合并 W26、W27 后得到关于所有点一致的

\[
 2\sum_{i<j}\log|x_i-x_j|-(n-1)\sum_iV(x_i)
 \le Jn^2+O(n\log(n+2)).
 \tag{W28}
\]

最后把 n∑V 分成 (n−1)∑V+∑V，在 W8 中积分：

\[
 \mathcal Z_n\le\frac1{n!}
 e^{Jn^2+O(n\log(n+2))}
 \left(\int_{\mathbb R}e^{-V(x)}\,dx\right)^n
 \le\frac1{n!}e^{Jn^2+O(n\log(n+2))}(2/c)^n.
 \tag{W29}
\]

因此 log𝒵_n≤Jn²+O(nlog(n+2))。将 W29、W10 代入 W9，即证明 W4。n=1 的有限项可并入 O(nlog(n+2))，不影响结论。

## 6. 严格改进、数值说明与作用范围

先只取 V_0(x)=c|x|。上述构造去掉 W13 的 charge 项，并选 a_0=π/c=1/2，得到概率密度 (c/π²)log((a_0+√(a_0²−x²))/|x|)。其内部势常数和外部严格不等式由 W16–W18 的线性部分直接得到；U_{μ_0}(0)=log(a_0/2)−1，且 ∫c|x|dμ_0=1（W12 中 arcsine 的绝对一阶矩是 2s/π）。因此线性势的最大能量为

\[
 J_0=\log(a_0/2)-3/2=-\log4-3/2.
 \tag{W30}
\]

此处“最大”不另引存在定理：对任意有限能量紧支撑概率 η，展开 I(η−μ_0) 并用 W23、该测度的 W19 即得 I(η)−∫V_0dη≤J_0。特别适用于本文 μ，所以

\[
 J=I(\mu)-\int V_0\,d\mu-\int\alpha\,d\mu
 \le J_0-\int\alpha\,d\mu.
 \tag{W31}
\]

μ 的密度 W2≥λ_a 的密度；λ_a 的二阶矩由 W12 为 (c/π)∫_0^a(s²/2)ds=a³/3。又对 |x|≤a 用 log(1+u)≥u/(1+u) 得

\[
 \alpha(x)\ge\frac{x^2}{2}\int_1^3\frac{dy}{y^2+a^2}
 =\frac{x^2}{2a}\left(\arctan\frac3a-\arctan\frac1a\right).
 \tag{W32}
\]

W31、W32 即证明 W5，且正的增益由精确符号表达式保证。本稿保留真实势并以确切的线性势能量取代原 R23–R25 的 Hadamard 界；小数展示仅便于比较。纯符号比较旧优化常数时，log4+3/2+log(M/(4π))>0 等价 M>πe^{-3/2}。取 s=2 得 M≥log5/2；再用 π<22/7、e^{3/2}>22/5、log5>8/5，得到 πe^{-3/2}<5/7<4/5<log5/2。后两项指数/对数有理界可分别由 e^{3/2} 的前六个 Taylor 项之和 5711/1280>22/5，以及 log5=2∑_{j≥0}(2/3)^{2j+1}/(2j+1) 的前四项之和 122492/76545>8/5 核验。

本轮新内联 Python mpmath 60 dps 积分返回：μ 质量显示 1；U_0≈−2.4055652877766554；∫Vdμ≈0.9877859940376004；∫αdμ≈0.01281055364085406；J≈−2.8994582847954556。它们是数值说明，不是区间证书；W1–W32 的证明及 W5 的严格正增益完全独立于实验。没有执行旧 producer、prime、guard 或 Lean，也未下载新 PDF。

本稿证明的是同一 E_n 的更锐实处**上界**，没有证明该行列式的实际极限等于 κ+J；轮廓积分中仍可能有额外振荡抵消。因此 γ_w 不是模型最优常数或 no-go 结论。原 [固定23幂三层非零定理](cdt_beta4_fixed23_carry_transfer_20261007.md) 仍在 β4 有理假设下供应无限非零性。同轮的 [完整共轭格与全素数费用稿](cdt_beta4_global_content_20261007.md) 在原 [精确算术模型](cdt_beta4_projection_exact_arithmetic_20261007.md) 基础上先把安全全素数费用从19.275降至17.275，再以接近 n 素数处的真实 graded 零行内容节省1/104，最终降至4489/260≈17.265384615；本稿作者已实际全文审读最终九节 C1–C26及其原输入通过。它是同一 q 的相似共轭和完整 determinant polynomial 内容付款，不能另加共轭格或旧费用。本稿自身不减少有限处费用，且4489/260仍大于这里的实处收缩常数，尚未得到 β4 的无理性。

## 7. 一般方法接口及不能免费外推的地方

W23–W29 的有限 n 能量引理适用于其他真实 determinant 所产生的势：只需独立验证一个紧支撑概率 μ、有限对数能量及一致势连续性、Frostman 的实轴身份/不等式、势的线性增长和 Lipschitz 性。它给出严格二次尺度上界，不需要黑箱 log-gas 极限定理，也不要求行 entry 衰减。

然而实际单周期模型从 r=3 改到一般 r 时，公共因子为 P_J^{r−1}/Q_I；两个 Cauchy 外积只取消 P_J²，留下 P_J^{r−3}。因此 r>3 会引入额外、真实的 numerator 权重。不能保留本文 α、a 或 γ_w，也不能继承 r=3 的原整数格费用。若把 H=rn 的该模型重新完整推导，形式上的连续势包含

\[
 2\pi|x|+\frac12\int_1^r\log(y^2+x^2)\,dy
 -\frac{r-3}{2}\int_0^1\log(y^2+x^2)\,dy,
 \tag{W33}
\]

并需重付行 factorial、尺度、离散积分余项和固定阶 Cauchy 导数费用。W33 在本文仅指明待核查接口；本文未宣布一般 r 的 determinant 定理。负 charge 项还可能改变支撑形状，必须重新验证正密度与外部势不等式。当前 β4 结论 W4 已完成，不依赖该推广。

对数势论的背景参考是 E. B. Saff, [Logarithmic Potential Theory with Applications to Approximation Theory](https://arxiv.org/abs/1010.3760)，其 PDF 已存在于 [literature](../literature/saff2010_logarithmic_potential_arxiv1010_3760v1_20261006.pdf)。本轮仅核实该文 abstract 与本地文件存在；未宣称全文阅读。本文所用 W23、候选测度、势身份和有限 n 离散化均已在正文实际证明。

本稿七节 W1–W33 已由 root 实际全文读取并独立纸面审查通过，没有数学修正请求。审读覆盖概率测度及端点、Cauchy transform 与常数、Frostman 内外条件、零质量卷积能量、原点 log 密度的一致势模量、全尾控制、W27 完整展开、非紧积分的剩余势、factorial 支付及严格改进。作者在收审和补交叉链接后完成最后全文回读。另有独立 exact inline 检查端点多项式及 W5 比较中的两项有理级数。纸审、路径、SHA 和浮点数均不称为形式化验证。
