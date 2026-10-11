# 第225轮：固定三频率的实际渐近与关系的严格半径增益

2026-10-08，C。保持222–224的同一 R_n、A3/A5/A7、完整 C、Δ/Ξ/J。本文证明三个实际 cosine 幅度的主渐近，完整支付 entire contour、两侧远尾、uniform Stirling 和 Gaussian connection。由此得到实际 Δ 增长以及 relation-driven 严格半径增益；**不认证最小微分秩、完整共同亚纯图、CDT 算术 strict gate 或数值无理性**。数学程序0，无参数或频率扫描。

## 1. 实际整个函数和待证定理

沿224最终 Fourier 稿的归一化，置

\[
A_{2r}(z)=(\sin\pi z/\pi)^6R_{2r}(-z),\qquad
\mathscr A_r(x)=A_{2r}(r+x)
=\frac{\Gamma(3r+1+x)^3\Gamma(3r+1-x)^3}
{\Gamma(r+1+x)^9\Gamma(r+1-x)^9}.
\tag{G1}
\]

这是整个函数，不是裸 Gamma contour。等价的有限乘积身份为

\[
\mathscr A_r(x)=\left(\frac{\sin\pi x}{\pi}\right)^6
\frac{\prod_{a=r+1}^{3r}(a^2-x^2)^3}
{x^6\prod_{a=1}^{r}(a^2-x^2)^6}.
\tag{G2}
\]

右边的所有表面 poles 可去。定义负号、未归一化 Fourier 积分

\[
F_{j,r}=\int_{\mathbb R}\mathscr A_r(x)e^{-ij\pi x}\,dx,
\qquad B_{j,2r}=2(-1)^r F_{j,r},\quad j=1,3,5.
\tag{G3}
\]

第二式的相位来自 A_{2r} 的中心平移 r；j 都为奇数。B 是完整 cosine 幅度，不是单侧 Fourier coefficient。

令 φ(y)=18 arctan y−6 arctan(y/3)。对 j=1,3,5，唯一 y_j>0 满足 φ(y_j)=jπ。置

\[
v_j=\frac{9+y_j^2}{1+y_j^2},\quad \lambda_j=v_j^9,\quad
c_j=\frac{(2\pi)^{-11/2}}6
       \frac{(9+y_j^2)^2}{(1+y_j^2)^4}>0.
\tag{G4}
\]

**实际渐近定理：**

\[
B_{j,2r}=(-1)^r c_j r^{-11/2}\lambda_j^r
               (1+O_j(r^{-1})),\qquad r\longrightarrow\infty.
\tag{G5}
\]

三个 growth 确实严格分离：λ1>λ3>λ5>1。这里只使用自然三个固定频率。

## 2. 合法 contour 和 compact Stirling

固定 r≥1 与 y>0，将 G3 的 contour 下移到 x=r(u−iy)，u∈R。G1整个；固定 r 的 G2 在 |Re x|→∞、−ry≤Im x≤0 上为 O_r,y(|x|^−6)，指数因子有界。有限高度矩形的两条竖边趋0，故

\[
F_{j,r}=r\int_{\mathbb R}
\mathscr A_r(r(u-iy))e^{-ij\pi r(u-iy)}\,du.
\tag{G6}
\]

先令矩形宽度趋∞，再研究 r→∞；没有把依赖 r 的竖边常数冒称 uniform。

以下固定 y>0 和 M<∞。在 |u|≤M，四个量 3±(u−iy)、1±(u−iy) 距零至少 y，且其 principal arguments 落在一个 |arg|≤π−δ_M,y 的固定 sector。由 [DLMF5.11.E1/E3](https://dlmf.nist.gov/5.11) 及 §5.11(ii) 第一段 complex remainder bound，Γ(w+1)=sqrt(2π)w^(w+1/2)e^−w(1+O(1/|w|)) 在这个 sector uniform。它作用于 w=r(3±z)、r(1±z)，不是把 E7 中固定正 a 任意改成 complex a。

于是 uniformly on this compact line，

\[
\mathscr A_r(rz)=(2\pi)^{-6}r^{-6}a(z)e^{rg(z)}(1+O(r^{-1})),
\tag{G7}
\]

\[
g(z)=3[(3+z)\log(3+z)+(3-z)\log(3-z)]
 -9[(1+z)\log(1+z)+(1-z)\log(1-z)],
\]

\[
a(z)=\frac{(3+z)^{3/2}(3-z)^{3/2}}
{(1+z)^{9/2}(1-z)^{9/2}}.
\tag{G8}
\]

各因子的 log 和 power 分别用 principal branch；四个 arguments 在所选 line 不接触 cut。不得在全部 complex z 免费改为某个 product 的 principal power。r log r 和线性 r 项因 balanced 权数精确相消，剩余 r^−6。

## 3. 全水平轮廓的唯一实际最大点

有

\[
g'(-iy)=i\phi(y),\quad
\phi'(y)=\frac{144}{(1+y^2)(9+y^2)}>0,
\quad\phi(0)=0,\quad\phi(\infty)=6\pi.
\tag{G9}
\]

故三个 y_j 存在且唯一。记 f_y(u)=Re g(u−iy)，它为偶函数。对 u>0，

\[
f_y'(u)=\frac32\log
\frac{(u+3)^2+y^2}{(u-3)^2+y^2}
-\frac92\log
\frac{(u+1)^2+y^2}{(u-1)^2+y^2}.
\tag{G10}
\]

设 A=u²+y²+1、B=A+8，判断此导数的符号等价于比较 (B+6u)/(B−6u) 与 [(A+2u)/(A−2u)]³。所有分母为正，交叉相减精确为

\[
(B+6u)(A-2u)^3-(B-6u)(A+2u)^3
=-32u[-u^4+2u^2(y^2+3)+3(y^2+1)^2].
\tag{G11}
\]

括号对 u² 只有一个正根。因此 f_y 从中心严格下降到一个 minimum，再严格上升至无穷极限。用 principal logs 的大 u 展开，balanced 项消去后 f_y(∞)=6πy。中心值为

\[
f_y(0)=9\log\frac{9+y^2}{1+y^2}+y\phi(y).
\]

它比 plateau 严格大：

\[
\delta(y)=f_y(0)-6\pi y
=9\log\frac{9+y^2}{1+y^2}-y(6\pi-\phi(y))
=\int_y^\infty(6\pi-\phi(t))\,dt>0.
\tag{G12}
\]

最后身份可由 δ′=φ−6π、δ(∞)=0 验证；φ′=O(t^−4) 支付积分和极限。于是 **整条水平 line 的唯一全局最大点是 u=0**，不是只找到一个 local saddle。任意固定 ε>0 的 compact ε≤|u|≤M 与中心有正 gap。

在 y=y_j，h_j(z)=g(z)−ijπz 满足 h_j′(−iy_j)=0，并且

\[
h_j(-iy_j)=\log\lambda_j,\qquad
h_j''(-iy_j)=-\kappa_j,
\quad\kappa_j=\frac{144}{(1+y_j^2)(9+y_j^2)}>0.
\tag{G13}
\]

## 4. 远尾实际乘积界，不在∞滥用 Stirling

对 |u|≥M>3、z=u−iy，G2 的每个 numerator 因子满足
| (a/r)²−z² |≤|z|²(1+9/M²)，每个 denominator 因子满足
| (a/r)²−z² |≥|z|²(1−1/M²)。由于 numerator 与 denominator 的总 product degree 精确相消，且 |sin πrz|≤e^(πry)，

\[
|\mathscr A_r(rz)|
\le \pi^{-6}r^{-6}|z|^{-6}
\exp\{r[6\pi y+\epsilon_M]\},\quad
\epsilon_M=6\log\frac{1+9/M^2}{1-1/M^2}\longrightarrow0.
\tag{G14}
\]

乘 Fourier factor，再对 |u|≥M 积分，远尾为

\[
O_{M,y}(r^{-5}e^{r[(6-j)\pi y+\epsilon_M]}).
\tag{G15}
\]

在 y=y_j，中心指数 log λ_j 与 (6−j)πy_j 的差恰为 δ(y_j)>0。选择一个固定 M 使 ε_M<δ(y_j)/2，G15 相比中心主项指数更小。不存在遗漏的∞ endpoint 或其他 branch contribution；compact 与远尾分别控制全部原 line。

## 5. Gaussian connection、常数和 algebraic modes

在中心邻域，以 u=s/sqrt(r) 缩放。h_j 的二阶项为 −κ_j s²/2；Re h_j 的局部负二次界给可积 Gaussian majorant。a(−iy_j)=(9+y_j²)^(3/2)/(1+y_j²)^(9/2)>0。G7、G12–G15 因此给

\[
F_{j,r}=(2\pi)^{-6}a(-iy_j)
\sqrt{\frac{2\pi}{\kappa_j}}
r^{-11/2}\lambda_j^r(1+O(r^{-1})).
\tag{G16}
\]

为明确 relative error：取对称局部区间 |u|≤r^−2/5；|s|≤r^1/10。Taylor 展开至 cubic 与 amplitude 一次项，首个 r^−1/2 correction 为 odd polynomial 乘 Gaussian，积分为0。余项由 O((s²+s⁴+s⁶)/r) 乘固定 Gaussian 控制；局部外缘为 e^−c r^1/5，compact 外缘与 G15 有固定指数 gap。G7 的 uniform O(1/r) 同样可积。故误差确为 O(1/r)，不只是形式 stationary expansion。乘 G3 的2与相位，化简常数即 G4–G5。

增长可写成完全确定的 algebraic 数：

\[
v_1=\frac{1+\sqrt[3]2}{\sqrt[3]2-1},\qquad
v_3=3+2\sqrt3,\qquad v_5=3.
\tag{G17}
\]

其中 y1²=4 cubeRoot(2)−5、y3²=2sqrt(3)−3、y5²=3。核对方式是 tan(φ(y)/6)=8y/(3−6y²−y⁴)，再用 φ 的严格单调性指定正确 angle，不能只对平方方程任意选根。y1 的 denominator 正，φ/6=π/6；y3 的 denominator为0，φ/6=π/2；y5 由 arctan√3=π/3、arctan(1/√3)=π/6 得 φ=5π。v1 满足 v³−9v²+3v−3=0。实际 r-mode 是 μ_j=−λ_j，而非只有形式 polynomial candidate。

## 6. 原实际 Δ、两列 minor 与严格 relation 半径

用224精确坐标身份及固定三行 r,r+1,r+2，G5 给

\[
\Delta_r=(-1)^r d_\Delta r^{-33/2}
 (\lambda_1\lambda_3\lambda_5)^r(1+O(r^{-1})),
\tag{G18}
\]

\[
d_\Delta=\frac{8505\pi^6}{4}c_1c_3c_5
(\lambda_1-\lambda_3)(\lambda_1-\lambda_5)(\lambda_3-\lambda_5)>0.
\]

三行相位给 (−1)^(r+1)，升序频率的 Vandermonde 为负，故最终是 (−1)^r。独立的列缩放后，误差 O(1/r) 在三个 distinct modes 的有限 Vandermonde 中保持；没有在原 A 列的巨大共同 mode 误差里提取 subdominant 项。

再令 α_j=8/15−j²/2+j⁴/24、β_j=1−j²/2。精确有 A3=κ3π⁴Σα_jB_j、A5=κ5π²Σβ_jB_j，且 α1β3−α3β1=1/30。因此连续两行实际 minor

\[
W_r=\det\begin{pmatrix}A_{3,2r}&A_{5,2r}\\ A_{3,2r+2}&A_{5,2r+2}\end{pmatrix}
=d_W r^{-11}(\lambda_1\lambda_3)^r(1+O(r^{-1})),
\tag{G19}
\]

其中 d_W=κ3κ5π⁶ c1c3(λ1−λ3)/30>0。其他 pair 的 bases 严格更小。这给实际 W 的非退化与 mode separation，不用一个 A7 非零代替三列结论。

令 ρ=2^42/3^27<1，复用223同一实际 I_n=O(n^−5 log n ρ^n)。按精确两列展开，

\[
J_r=\kappa_3\kappa_5\pi^6\sum_{i<j}
(\alpha_i\beta_j-\alpha_j\beta_i)\det(B_i,B_j,I)_r,
\]

每个 determinant 用三行 r,r+1,r+2。G5 与实际 I 界给

\[
J_r=O(r^{-16}\log r\,(\lambda_1\lambda_3\rho^2)^r).
\tag{G20}
\]

没有证明 J 具有这个 exact growth，或证明其无限非零。由 exact J=ζ(7)Δ+Ξ 得 Ξ/Δ→−ζ(7)，error 为 O(r^1/2 log r (ρ²/λ5)^r)。故 Δ 与 Ξ 的真实 radius 均为

R_gen=(λ1λ3λ5)^−1。

此时是 actual growth，不是两个 radius 下界的比较。其不可去主点确在 z=−R_gen：对 Δ(−w) 的16阶导数，边界项最终同号且与 r^−1/2 比例，w→R_gen 从下趋近时和发散；analytic 延拓到该点将使导数有界，矛盾。Ξ 同理，因 ζ(7)>0 且 G20 指数更小。

对于 H_g=Σ(gΔ_r+Ξ_r)z^r，若 g≠ζ(7)，实际 leading term为 (g−ζ(7))G18，亦有相同 radius 与不可去点。**在目标关系 ζ(7)=g∈Q 下**，H_g=ΣJ_rz^r，且

\[
R(H_g)\ge(\lambda_1\lambda_3\rho^2)^{-1}
>R_{\rm gen},\quad\lambda_5>1>\rho^2.
\tag{G21}
\]

这是本轮实际支付的严格相对解析增益。尚不能把它自动升为 CDT 完整 source 的共同 meromorphic 图、最小 micro rank 或算术 strict inequality。两个 B 坐标含 π²，本文只在原实际有理 Δ/Ξ/H 上转回 radius；不免费改派分母费用。223安全指数12/26保留，绝对算术衰减亦仍须单独比较。

## 7. 实际来源、执行和剩余缺口

本轮实际 FULL 复用/读取224本人的最终 Fourier 稿12032B / `16e84deee6e12c94da29cee38171b0f65fabb765b31bb5ac06dd7f9edf6b3530`，全部Q1–Q16；该稿此前B独审4324B / `f87001259756b43cc0ddf866491d4d1247882ebacc0e6248a0c665fa3e412199` PASS。G1–G3的归一化沿冻结实际身份；新 asymptotic proof 在本文完整支付。223实际 I 界为本人已保存并独审通过的同一对象，不移用异族四阶 characteristic。

新 primary 只选读官方 DLMF5.11 的 E1/E3、g0=1、固定 sector 条件与 §ii 首个完整 remainder paragraph；另 FULL 读223已存167-byte E1 TEX。保存官方 HTML 原件一份，不宣称 FULL 所有413行，也未读其引用 Olver/Boyd 等整本书或论文。准确 URL、读取范围及新原件身份另存 [来源记录](../literature/pade_actual_modes_sources_round225_20261008/dual_reading_scope.md)。未引用未读的 steepest descent theorem；Gaussian 与 tails 均自含证明。

数学程序实际 **0**：无CAS、积分执行、root solver、matrix程序、recurrence guessing、参数/频率/素数扫描、PSLQ、Lean、旧证书复跑或Git。工具仅官方网页选读、下载、文档写读及metadata。尚未证明 I/J actual small leading mode、J/H_g 非多项式、共同微分最小模型与完整CDT gate；不取 U≥0 作 K≥0 的根据。相关其他225稿须各自证明和独审。

只写本NEW225稿和来源记录，冻结/main/manifest不改。保存后实际FULL作者复读并登记bytes/hash；作者自读不代替独立审查。
