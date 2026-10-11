# 显式 Catalan 符号的退化：有理商迫使 4T=0

日期：2026-10-04。独立承接冻结的 [椭圆商报告](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004.md)，旧报告未修改。结论是函数域 Milnor K₂ 的整系数定理，不使用周期猜想，也不进行参数扫描。

**本轮已证：原显式符号 T 在 K₂ᴹ(K(C)) 中满足 4T=0，因而 T⊗Q=0。** 旧报告只提出候选并明确未证明非零；本轮完成了那项审查。它不能成为非零的有理椭圆 K₂ 调节子输入。此结论不说 T 整系数恒等于零，不说 Catalan 常数的真实指定路径积分为零，也不证明其无理性。

## 1. 对象与全部水平 tame 的范围

设 a=√2，K=Q(i,a)，C 为 `Y²=s⁸−14s⁴+1` 的光滑射影模型。两商映射及其符号为

\[
x_+=s+s^{-1},\quad x_-=s-s^{-1},\quad y_+=y_-=Y/s^2,
\]
\[
u_+=\frac{x+a}{x-a},\quad
r_+=\frac{i}{a}x(6-x^2),\quad
F_+=\frac{y-r_+}{y+r_+},
\]
\[
u_-=\frac{x-ia}{x+ia},\quad
r_-=\frac{x(x^2+6)}a,\quad
F_-=\frac{y-r_-}{y+r_-}.
\]

在 E± 上写 S±={u±,F±}，在 C 上写

\[
T=\pi_+^*S_++\pi_-^*S_-\in K_2^M(K(C)). \tag{1}
\]

加法用于 K₂，tame 的目标 K₁=κ(P)× 用乘法。旧证书已计算所有单商非平凡 tame：E₊ 的 x=±a、y=4i 给 2，y=−4i 给 1/2；E₋ 的 x=±ia 给相反值。其余水平点 tame=1，理由可由

\[
y^2-r_+^2=\tfrac12(x^2-2)^2(x^2-6),\quad
y^2-r_-^2=-\tfrac12(x^2+2)^2(x^2+6)
\]

穷尽：剩余简单分支点 F 趋 1，无穷远 u 趋 1、F 趋 −1。

拉回到 C 时，可能非平凡点恰为 s⁴=−1。在那里 x₊²=2、x₋²=−2，两商 y 相同；`dx₊/ds=1−s⁻²` 和 `dx₋/ds=1+s⁻²` 都非零。因此无分歧倍率，两个 tame 互逆。于是

\[
\partial_P T=1\quad\text{对 C 的每个水平闭点 P}. \tag{2}
\]

这里包括全部代数共轭闭点，非仅 K 有理点；在代数闭包中相消也给原剩余域中的相消。本证明只使用 (2) 的函数域陈述，未预先假定算术整模型或垂直 tame 已通过。

## 2. Milnor 符号确实被整个 V₄ 固定

令

\[
\sigma(s,Y)=(-s,Y),\qquad
\tau(s,Y)=(s^{-1},Y/s^4).
\]

σ 将两商 x 都取负，y 不变。于是对每一商，u、F 同时变逆。Milnor K₂ 的整系数双线性给

\[
\{u^{-1},F^{-1}\}=\{u,F\}, \tag{3}
\]

所以 σ 固定每个拉回 S±。τ 固定 E₊ 坐标，在 E₋ 上将 x 取负、y 不变，也固定两个符号。故

\[
\boxed{\sigma T=T,\quad\tau T=T.} \tag{4}
\]

这是符号的整系数相等，不依赖对数分支；把 `log(u⁻¹)` 写成 `−log u` 时会有分支常数，那属于实际积分的另一个问题。

还可核四阶自同构 δ(s,Y)=(is,Y)：它使拉回 S₊、S₋ 互换，故 δT=T。超椭圆对合 ι(s,Y)=(s,−Y) 则使 u 不变、F 变逆，故 ιT=−T。δ 的额外对称不是证明所必需；V₄ 已足够。

## 3. V₄ 固定域为实际有理函数域

在 K(C) 中置

\[
R=s^2+s^{-2},\qquad W=Y/s^2.
\]

二者被 V₄ 固定，满足

\[
W^2=R^2-16.
\]

这条光滑射影 conic 具有显式参数

\[
t=(R+W)/4,\qquad
R=2(t+t^{-1}),\quad W=2(t-t^{-1}). \tag{5}
\]

反向 s 满足 `s⁴−Rs²+1=0`，且 Y=Ws²，因此 `[K(C):K(R,W)]≤4`。四个不同的 V₄ 自同构已固定该子域，故次数恰为 4。这同时证明

\[
K(C)^{V_4}=K(R,W)=K(t),\qquad
K(C)/K(t)\text{ 为 V₄ Galois 扩张}. \tag{6}
\]

证明用的是整个固定域，不能从三个 genus 1 子商直接跳到此结论。

## 4. transfer、常数核与基点特化给整系数 4T=0

记 L=K(C)、F=K(t)，取 Milnor K₂ 的 integral corestriction N=N_{L/F}。所用现成定理仅为以下三条。

1. 有限 Galois 扩张的 base change：`res Nα=Σ_{g∈Gal(L/F)}gα`。
2. 对几何离散 valuation，tame 与 corestriction 相容：`∂_v Nα=∏_{w|v}N_{κ(w)/κ(v)}(∂_wα)`。这里没有额外分歧指数；分歧指数出现在 restriction 的残差公式。
3. 有理函数域的整系数 Milnor/Bass–Tate 正合列给 `ker(⊕_{p finite}∂_p)=image K₂ᴹ(K)`，并且 constants 的 restriction 单射。

前两条与 Milnor K 理论的适用性见 [Rost，Chow Groups with Coefficients](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)，R1c、R3b（印刷 p.329）、Theorem 1.4（p.331）；Remark 1.8（p.333）说明所需整闭包有限条件对几何 valuation 成立。第三条与下述特化见 [Weibel 作者稿，The K-book](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf)，III.7.3–7.4（印刷 pp.246–247；2013-08-29 稿）。Rost 使用与旧稿相反的 tame 约定；tame=1 及本证明不受此反转影响。

由 (2) 与 tame/corestriction 相容，N(T) 在 F 的全部有限闭点 tame=1。因此存在唯一

\[
\kappa\in K_2^M(K),\qquad N(T)=\operatorname{res}_{F/K}\kappa. \tag{7}
\]

由 (4) 和 Galois base change，

\[
\operatorname{res}_{L/K}\kappa=4T. \tag{8}
\]

取 C 的 K 有理点 P₀=(0,1)。虽然商坐标 x± 有极点，u±、F± 在 P₀ 的局部环中都是单位。直接消掉商坐标极点后，

\[
u_+(P_0)=u_-(P_0)=1,\qquad F_+(P_0)=F_-(P_0)=-1. \tag{9}
\]

Milnor specialization λ_{P₀}:K₂ᴹ(L)→K₂ᴹ(K) 在单位符号上是剩余域取值，在 constants 上为恒等。对 (8) 特化便得

\[
\kappa=4\bigl(\{1,-1\}+\{1,-1\}\bigr)=0.
\]

代回 (8)：

\[
\boxed{4T=0\text{ 于 }K_2^M(K(C)),\qquad T\otimes\mathbf Q=0.} \tag{10}
\]

P₀ 在 conic 商上是无穷远点，并不造成问题：这里只在 C 对已经证明是常数的 κ 特化。λ_{P₀} 可先选择 uniformizer s 定义；(9) 中所有函数都是单位，故本计算不依赖该选择。不需要任何 mixed characteristic Gersten 命题。

## 5. 可复用的对称退化引理

**引理。** 设 k 为 char 0 域，X 为光滑射影几何整曲线，H 是其有限自同构群，`k(X)^H≅k(t)`，d=|H|。设 α∈K₂ᴹ(k(X)) 在每个水平闭点 tame=1，且被 H 固定。若 X 有 k 有理点 P₀，记 β=λ_{P₀}(α)，则

\[
d\bigl(\alpha-\operatorname{res}_{k(X)/k}\beta\bigr)=0. \tag{11}
\]

特别地，β=0 时 dα=0。

**证明。** Norm α 的水平 tame 都为 1，故它来自 κ∈K₂ᴹ(k)。Galois base change 给 resκ=dα；在 P₀ 特化给 κ=dβ，于是 (11)。α 无分歧时特化不受 uniformizer 影响；若只需 β=0 的情形，也可直接要求 α 在该点由取值为零的单位符号和表示。

这是完整的全族阻碍，而非有限素数或有限数值证据。它说明寻找非恒定的有理 K₂ 类时，应先检查候选是否被某个有理商的整个群固定；若固定且有零特化，计算垂直整性之前就已没有非零的有理调节子输入。非平凡群字符只能避开这项必要障碍，本身不证明非零。

## 6. 到 Q(i) 的 transfer 没有留下非零有理类

令 k=Q(i)，K=k(a)，二次常数扩张的自同构 a↦−a 将每个 u±、F± 同时变逆，故 T 被固定。取

\[
T_k=N_{K(C)/k(C)}T.
\]

则 `res T_k=2T`；由 (10) 直接应用 norm 得

\[
4T_k=0,\qquad T_k\otimes\mathbf Q=0. \tag{12}
\]

没有必要、也没有依据由此把整系数阶数进一步降成 2。复共轭 i↦−i 的反字符仍是正确的符号身份，但此处相应有理类已经为零；字符符合 χ₋₄ 不代表存在非零 χ₋₄ 调节子。E± 在 Q(i) 上同构也不能改变 (10)。

若某个整模型存在 T 的延拓，(10) 只直接约束其函数域像；不能未经 injectivity 证明就断言所有模型 K₂ 类被 4 杀掉。另一个独立而简单的推论是：对任意离散 valuation v，`(∂_vT)^4=1`。若剩余域 char 2，乘法群没有非平凡四次单位根，所以其 tame 必为 1。此推论仍不把 tame 检验自动提升为算术模型中的特定类。

## 7. 实际长度二积分仍需要相对而非绝对输入

旧稿的认证函数身份是

\[
dg_c=-\frac i4\sum_{\pm}\pi_\pm^*(\log u_\pm\,d\log F_\pm).
\]

从 P₀ 到指定分支端点 P₁ 的路径及对数分支给 Catalan 常数的真实积分。此项在旧稿没有被认作 T 的调节子；本轮结果进一步说明不能补上“非零绝对 K₂ 调节子”这一认定。凡从 T 出发并取有理/实向量空间值的同态都因 (10) 而为零。

普通开路径积分还包含基点、端点和分支数据。对固定连续对数，有纯分析身份

\[
\int_{P_0}^{P_1}\log u\,d\log F
=\frac12\int_{P_0}^{P_1}(\log u\,d\log F-\log F\,d\log u)
+\frac12[\log u\log F]_{P_0}^{P_1}. \tag{13}
\]

这些开路径与边界数据并未仅由函数域 Milnor 符号决定。因而 (10) 不会把该路径值逼成零，也不推出它是有理数或 π² 的有理倍数。

下一项应改变为一个具体的相对问题：在带有 P₀、P₁ 及对数除子的曲线上，明确给出实际积分对应的相对周期类和边界项，再核其是否退化。若要使用 Bloch 群或调节子，必须先给精确函数身份、分支与端点，证明它确实计算这个值；不能把已经为零的绝对类重新命名后继续用其非零性。[Goncharov–Levin v4 的 Theorem 1.2](https://arxiv.org/pdf/alg-geom/9508008v4)／[本地原件](E:/kimi-build/zeta5/literature/goncharov_levin1997_zagier_elliptic_k2_v4.pdf) 为椭圆调节子背景，但不提供此处尚缺的相对识别。

## 8. 证书范围

[脚本](E:/kimi-build/zeta5/research/odd_zeta_k2_descent_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_k2_descent_20261004_verify.json) 已运行通过。它们精确核 V₄、δ、ι 对函数的作用，conic 方程及有理参数逆式，四次 s 方程，水平相消点的无分歧条件，以及 P₀ 的单位取值。Milnor 双线性、transfer、正合列与 specialization 属于上面的数学证明及原始定理，未伪装成电脑验证。没有参数扫描，没有声称 T 整系数为零，没有数值无理性结论。
