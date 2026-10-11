# 四项 Steinberg 链、整数 T=0 与完整 Catalan primitive

日期：2026-10-04。继续冻结的 [椭圆商稿](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004.md)、[K₂ 下降稿](E:/kimi-build/zeta5/research/odd_zeta_k2_descent_20261004.md) 和 [端点 Bloch 稿](E:/kimi-build/zeta5/research/odd_zeta_bloch_boundary_20261004.md)，不修改旧文件。

本轮给出实际四项链 ε₀，直接证明 δε₀=w；并将旧稿的 `4T=0` 加强为 **整系数 T=0**。端点差用八个明确五项关系化为 −4[i]，不再需要非显式 transfer、对称平均或 Borel 调节子注入来完成该识别。还给原复杂积分的分支兼容 Li₂ primitive。所有结论为固定身份；没有无理性证明或随尺度变化的近似族。

## 1. 有理商上的两个参数

设 a=√2，K=Q(i,a)，C 为 `Y²=s⁸−14s⁴+1` 的光滑模型。保留旧函数

\[
x_\pm=s\pm s^{-1},\quad y=Y/s^2,
\]
\[
u_+=\frac{x+a}{x-a},\quad r_+=\frac{i}{a}x(6-x^2),\quad
F_+=\frac{y-r_+}{y+r_+};
\]
\[
u_-=\frac{x-ia}{x+ia},\quad r_-=\frac{x(x^2+6)}a,\quad
F_-=\frac{y-r_-}{y+r_-}.
\]

在有理商上记

\[
R=s^2+s^{-2},\quad W=Y/s^2,\quad
W^2=R^2-16,\quad t=(R+W)/4,
\]
\[
R=2(t+t^{-1}),\quad W=2(t-t^{-1}).
\]

引入与原 r± 不同的参数

\[
\rho_+=\frac{W-i(R-4)}{W+i(R-4)}
=-i\frac{t+i}{t-i},\qquad
\rho_-=\frac{W-i(R+4)}{W+i(R+4)}
=-i\frac{t-i}{t+i}. \tag{1}
\]

于是

\[
\boxed{\rho_+\rho_-=-1.} \tag{2}
\]

实际函数满足两组关键恒等式：

\[
\boxed{F_\pm=-\frac{u_\pm-\rho_\pm}{1-\rho_\pm u_\pm},\qquad
c_\pm:=(1-\rho_\pm/u_\pm)(1-\rho_\pm u_\pm)=-2\rho_\pm.} \tag{3}
\]

推导可以完全手算。将 u 写成 `(x+k)/(x−k)`，正商 k=a，负商 k=−ia；若 r=xH(x²)，则 ρ=(y+kH)/(y−kH) 给 (3) 第一式。共同 conic 上 x₊²=R+2、x₋²=R−2，故

\[
u_++u_+^{-1}=2(R+4)/R,\quad
u_-+u_-^{-1}=2(R-4)/R.
\]

代入 `c=1−ρ(u+u⁻¹)+ρ²` 与 (1) 即得第二式。ρ 属于 K(t)，但 u 一般不属于 K(t)。

## 2. 实际四项链

采用有理 pre-Bloch 群及 `δ[h]=h∧(1−h)`。对一般满足 `F=−(u−ρ)/(1−ρu)` 的函数，置 A₁=1−ρ/u、B₁=1−ρu。直接在有理 exterior 中展开：

\[
u\wedge F=u\wedge A_1-u\wedge B_1,
\]
\[
\delta[\rho/u]=\rho\wedge A_1-u\wedge A_1,
\qquad
\delta[\rho u]=\rho\wedge B_1+u\wedge B_1.
\]

所以

\[
u\wedge F=\rho\wedge c
-\delta[\rho/u]-\delta[\rho u]. \tag{4}
\]

本族剩余项直接相消：

\[
\rho_+\wedge c_++\rho_-\wedge c_-
=(\rho_+\rho_-)\wedge2=(-1)\wedge2=0
\quad\text{于有理 exterior}. \tag{5}
\]

因此实际有限链为

\[
\boxed{\varepsilon_0=-[\rho_+/u_+]-[\rho_+u_+]
-[\rho_-/u_-]-[\rho_-u_-],\qquad
\delta\varepsilon_0=w=u_+\wedge F_++u_-\wedge F_-.} \tag{6}
\]

四个系数都是 −1。每个 argument 是实际 K(C) 函数，既非恒等 0 也非恒等 1；后者也直接由 `c=−2ρ≠0` 排除。

这里无需平均：σ:s↦−s 在每个商交换两项，τ:s↦1/s 固定正商两项、交换负商两项；a↦−a 也交换每一商的两项。ρ± 被这三个动作固定。因此 (6) 已在有限 formal chain 层面 literal invariant，没有额外分母 8。

## 3. 更强的整数 Milnor K₂ 结论

以下完全在整系数 Milnor 群中。使用一般恒等式 `{v,−v}=0` 和 Steinberg 关系，

\[
\begin{aligned}
\{u,F\}
&=\{u,-u\}+\{u,1-\rho/u\}-\{u,1-\rho u\}\\
&=\{\rho,1-\rho/u\}+\{\rho,1-\rho u\}\\
&=\{\rho,c\}=\{\rho,-2\rho\}=\{\rho,2\}.
\end{aligned} \tag{7}
\]

第二行分别用 `{ρ/u,1−ρ/u}=0`、`{ρu,1−ρu}=0`。由 (2)，

\[
\boxed{T=\{\rho_+,2\}+\{\rho_-,2\}
=\{-1,2\}=\{-1,1-(-1)\}=0.} \tag{8}
\]

这排除了原来尚不能排除的四阶扭残余。证明没有使用 transfer、水平 tame 或算术模型。它立即使 T 在任意离散 valuation 的 tame 都为 1；旧整模型报告的证明仍正确，但对这个固定 T 现在有更短理由。函数域零类也不自动指定任何全局 Quillen K₂ lift 或相对端点 trivialization。

为参考，`{v,−v}=0` 本身由 `{v,1−v}=0`、`{1/v,1−1/v}=0` 与双线性推出，未用猜想或只在有理化后成立的反演关系。

## 4. 显式端点类与八个五项关系

令 L=K(b)，b=√3，P₀=(0,1)，B=(a(b−1)/2,0)，并记 A=2+b。P₀ 上 t→∞，B 上 t=1。用 (1) 的正则表达取值：

\[
\begin{array}{c|cccc}
&u_+&\rho_+&u_-&\rho_-\\\hline
P_0&1&-i&1&-i\\
B&A&1&i&-1.
\end{array} \tag{9}
\]

ρ₊ 在 B 的 `(W,R)` 表达表面为 0/0，但其 t 表达在 t=1 正则。四项 argument 两端都是单位，取值均不在 {0,1,∞}。所以普通逐项端点差为

\[
\varepsilon_0(P_0)=-4[-i],\qquad
\varepsilon_0(B)=-[A^{-1}]-[A]-[i]-[-i],
\]
\[
\beta=\varepsilon_0(B)-\varepsilon_0(P_0)
=-[A]-[A^{-1}]-[i]+3[-i]. \tag{10}
\]

这不是依赖某个未知链的数域类。

明确采用 Suslin 五项表达

\[
\mathcal R(x,y)=[x]-[y]+[y/x]
-\left[\frac{1-x^{-1}}{1-y^{-1}}\right]
+\left[\frac{1-x}{1-y}\right]. \tag{11}
\]

置 I(z)=[z]+[1/z]。对本稿用到的 z=A、i、−1，全部 arguments 非退化，并有自由链恒等式

\[
\mathcal S(z):=\mathcal R(2,2z)+\mathcal R(1/2,1/(2z))
+\mathcal R(2z,2)+\mathcal R(1/(2z),1/2)=2I(z). \tag{12}
\]

第一对合为 `I(2)−I(2z)+I(z)`，第二对合为 `I(2z)−I(2)+I(1/z)`，所以 (12) 可逐项检查。因而

\[
\beta+4[i]=-I(A)+3I(i)
=-\tfrac12\mathcal S(A)+\tfrac32\mathcal S(i)=0
\quad\text{于 }\mathcal P_2(L)_\mathbf Q. \tag{13}
\]

这是八个明确五项关系，直接给

\[
\boxed{\beta=-4\,\operatorname{res}_{L/\mathbf Q(i)}[i]
\quad\text{于 }B(L)_\mathbf Q.} \tag{14}
\]

整数细节也可核清。采用 Suslin antisymmetric tensor 目标，有 `δI(z)=z⊗(−z)`。在本 L 内，

\[
A=\left(\frac{a(b+1)}2\right)^2,
\qquad i=\zeta_8^2,\quad\zeta_8=(1+i)/a.
\]

square 使 `δI(A)=δI(i)=0`：若 z=v²，则 `z⊗(−z)=2v⊗(−1)+4v⊗v=0`。又 `4δ[i]=0`，所以 (10) 本身是这个特定 L 上的整数 Bloch cycle。(12) 给 `2(β+4[i])=0`；没有在整数群中未经证明就消掉可能的二阶扭。主精确识别 (14) 仍在有理系数。此论证只核本族的全部端点函数及 square 条件，未宣称一般 naive integer specialization 总能成立。

## 5. real primitive 的完全显式式子

记 D 为 Bloch–Wigner dilogarithm，`dD(h)=η(h,1−h)`。由 (6)，

\[
\boxed{\Psi=-D(\rho_+/u_+)-D(\rho_+u_+)
-D(\rho_-/u_-)-D(\rho_-u_-),\qquad d\Psi=\eta_T.} \tag{15}
\]

D 在 0、1、∞ 连续取 0，所以此表达可在 finite divisor 处连续延拓。端点直接为

\[
\Psi(P_0)=-4D(-i)=4G,\qquad\Psi(B)=0,
\]

因正实 A、A⁻¹ 的 D 为 0，且 `D(i)+D(−i)=0`。因此

\[
\int_{P_0}^{B}\eta_T=\Psi(B)-\Psi(P_0)=-4G. \tag{16}
\]

这是原 [real regulator 稿](E:/kimi-build/zeta5/research/odd_zeta_k2_regulator_20261004.md) 的积分身份的实际 primitive，不靠绝对 K₂ 非零性。规范化的全局实 primitive 为 Φ=Ψ−4G。

## 6. 原复积分也有分支兼容 Li₂ primitive

本节不把复 primitive 与 real regulator 混同。沿旧原实路径 `s∈[0,s₀],Y≥0`，t 从 ∞ 走到 1。每商置

\[
U=\log u,\quad V=\log\rho,\quad
L_A=\log(1-\rho/u),\quad L_B=\log(1-\rho u),
\quad\lambda=\log2+i\pi.
\]

从 P₀ 连续延拓，初值取

\[
U=0,\quad V=-i\pi/2,\quad L_A=L_B=\log(1+i).
\]

由 (3)，乘积的连续对数满足

\[
L_A+L_B=V+\lambda. \tag{17}
\]

Li₂ 两项初值均取主值 Li₂(−i)，再沿实际 argument 路径继续。定义

\[
\boxed{\mathcal H(u,\rho)=\tfrac12U^2+U(L_A-L_B)
-\operatorname{Li}_2(\rho/u)-\operatorname{Li}_2(\rho u)
-\tfrac12V^2-\lambda V.} \tag{18}
\]

利用 `dLi₂(h)=−log(1−h)dlog h`，展开 (18) 后得到

\[
d\mathcal H=U(dU+dL_A-dL_B)
+(L_A+L_B-V-\lambda)dV
=\log u\,d\log F. \tag{19}
\]

故旧函数有实际复表达

\[
g_c(s)=c-\frac i4\sum_{\pm}
\bigl(\mathcal H_\pm(s)-\mathcal H_\pm(P_0)\bigr). \tag{20}
\]

这里必须保留指定初值。任意改变 log 分支并保留旧常数会破坏 (20)。

端点可全部手算。两个基点值相同：

\[
\mathcal H_\pm(P_0)=-2\operatorname{Li}_2(-i)
-3\pi^2/8+(i\pi/2)\log2. \tag{21}
\]

正商在 B 上 U=log A，V=0，`L_A−L_B=−log A−iπ`；`ρu` 从下半平面抵达 A>1，故要取 Li₂(A−i0)，而不是随意的 cut 值。反演恒等式给

\[
\operatorname{Li}_2(A-i0)+\operatorname{Li}_2(A^{-1})
=\pi^2/3-\tfrac12\log^2A-i\pi\log A,
\quad \mathcal H_+(B)=-\pi^2/3. \tag{22}
\]

负商 U=iπ/2，V=−iπ，`L_A−L_B=−iπ/2`；其两项抵达 i、−i，路径避开 Li₂ 的正实 cut。由 `Li₂(i)+Li₂(−i)=½Li₂(−1)=−π²/24`，

\[
\mathcal H_-(B)=-\pi^2/3+i\pi\log2. \tag{23}
\]

由单位圆上的绝对收敛级数，`Li₂(−i)=−π²/48−iG`。于是

\[
\boxed{\sum_{\pm}\bigl(\mathcal H_\pm(B)-\mathcal H_\pm(P_0)\bigr)
=4\operatorname{Li}_2(-i)+\pi^2/12=-4iG.} \tag{24}
\]

(22) 的分支版可通过求导并在 z=−1 核常数来证明；(23) 的二倍角式直接来自级数。不依赖周期猜想、Borel 注入或数值识别。

## 7. 可选的整数十三项链

在 antisymmetric tensor 目标中，双线性给

\[
\delta([z]+[1/z])=z\otimes(-z).
\]

因此也有实际整数链

\[
\varepsilon_{\rm int}=
\sum_{\pm}\bigl([u_\pm]+[1/u_\pm]+[\rho_\pm]+[1/\rho_\pm]
-[\rho_\pm/u_\pm]-[\rho_\pm u_\pm]\bigr)+[-1],
\quad\delta\varepsilon_{\rm int}=u_+\otimes F_++u_-\otimes F_-. \tag{25}
\]

单商展开的剩余为 `−ρ⊗2`；两项合为 `−(−1)⊗2`，恰由 `δ[-1]` 补回。整数端点为

\[
\varepsilon_{\rm int}(P_0)=2[i]-2[-i]+[-1],\quad
\varepsilon_{\rm int}(B)=3[-1],
\]
\[
\beta_{\rm int}=2[-1]-2[i]+2[-i]. \tag{26}
\]

其 boundary 是 `−(−1)⊗2`；在本 L 中 `2=a²`，所以这个 tensor 已为零，甚至在 full tensor 中就有
`(−1)⊗a²=2((−1)⊗a)=((−1)²)⊗a=0`。故 (26) 也是本具体数域的整数 cycle。这个 square 条件不可省去或推成任意数域的结论。两端仅出现值 1 的省略项；其 first tensor 为 1，本 finite-chain 整数评价没有一般零极特化的缺口。实调节子仍为 −4G；整数类的未消扭信息不用于无理性结论。

## 8. 真正推进与仍缺输入

已完成的是四项实际链、整系数 T=0、有限五项端点证书，以及原积分的完整 real/complex primitive。原先“有限链存在但未显式”这项缺口已补齐。

有理商只给 ρ± 与 c±；四个 dilogarithm arguments 仍在 K(C)，一般不在 K(t)。literal V₄ 不变性本身不证明链来自 `P₂(K(t))`，本稿没有作此压缩声明。所得式子是有限普通 Li₂ 的**代数函数 arguments**，并非已证明所有 arguments 都能改为有理 t 函数。

这些恒等式又明确说明：本构造没有新非零绝对椭圆 K₂ 类，端点信息就是经典 Catalan 类。四项固定表达、fixed square 条件或 fixed 五项关系并不提供随次数指数增长的 content，也不产生非零整数小线性型。下一轮若要推进无理性，仍须交付尺度参数、实际目标系数和完整清分母／衰减预算。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_explicit_steinberg_20261004_verify.py)／[JSON](E:/kimi-build/zeta5/research/odd_zeta_explicit_steinberg_20261004_verify.json) 已运行通过（45 项固定检查）。它们核 (1)–(3)、有理 wedge 的自由展开、literal 动作、所有端点、(12) 的 formal cancellation 与非退化性，以及 (18)–(24) 的形式微分和端点代数。Milnor 群及 Bloch 五项关系的解释由书面证明承担；没有把有限算术检查伪装成全局无理性或 Lean 验证。

直接依据仅需已归档的 [Suslin Theorem 5.2 原件](E:/kimi-build/zeta5/literature/suslin1991_k3_field_bloch_group_english.pdf) 和 [Neumann–Yang v1 pp.3–4](E:/kimi-build/zeta5/literature/neumann_yang1997_rationality_k_theory_v1.pdf) 的正确 Suslin 五项约定；后者明确纠正其发表版的 misprint。本稿的具体身份是上述直接代数推导，没有新增待归档文献。
