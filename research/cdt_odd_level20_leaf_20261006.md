# Level 20 的实际椭圆叶、共同覆盖与原点导数限制

日期：2026-10-06。本稿接续 [level-20 两共轭周期报告](cdt_odd_conjugate_projection_20261005.md)。本稿新增的是三个其它 elliptic branch 的实际加性 cusp 周期、共同解析覆盖的条件和一个明确合法的共同 map；没有新增数值无理性定理。

## 1. 几何输入与四个实际 elliptic lifts

采用根分支当前建立的商坐标
\[
 h=\frac{\eta(4\tau)^2\eta(5\tau)^2}
          {\eta(\tau)^2\eta(20\tau)^2},\qquad
 t=\frac1{h+1},
\]
及 double-cover 方程
\[
 \Delta(t)=1-12t+28t^2-32t^3+16t^4.
\]
本稿把 [根分支完整模型](cdt_odd_level20_model_20261006.md) 的 Hauptmodul、整数 q↔t 反演及全局 double-cover 识别视为明确输入；不以有限 eta jet 重新证明它们。其四个分支值为
\[
 \alpha=\frac12-\sqrt{\frac{\sqrt5-1}{8}},\quad
 \beta=\frac12+\sqrt{\frac{\sqrt5-1}{8}},\quad
 \gamma_\pm=\frac12\pm i\sqrt{\frac{1+\sqrt5}{8}}.
\tag{1}
\]
三个 cusp pairs 到 t=0,1,∞；c=4,5 的 pair 对应 t=1。

对 a,b,d 为整数、ad−20b²=1，令
\[
 g=\begin{pmatrix}a&b\\20b&d\end{pmatrix},\qquad
 s=W_{20}g=\begin{pmatrix}-20b&-d\\20a&20b\end{pmatrix}.
\]
其固定点和 shifted involution 分别为
\[
 \tau_*=-\frac ba+\frac{i}{a\sqrt{20}},\qquad
 s\left(-\frac ba+z\right)=-\frac ba-\frac1{20a^2z}.
\tag{2}
\]
四个代表如下。这里 canonical continuation 指从 q=0 的原始 Taylor 芽沿 q 的固定辐角径向延拓到相应 τ*；两 embedding 使用同一组路径。

|branch|a,b,d|χ₅(d)|additive cusp −b/a|effective level|
|---|---|---:|---:|---:|
|α|1,0,1|1|0|20|
|γ−|3,1,7|−1|−1/3|180|
|γ+|3,2,27|−1|−2/3|180|
|β|9,2,9|1|−2/9|1620|

代表的矩阵和平方 s²=−20I 是精确整数身份。分支标签还经带明确尾界的 interval eta 乘积隔离：q 的模小于 9/10，截断 n≤600 后 log-tail 绝对值至多
\[
 L=\frac{8(9/10)^{601}}{(1-9/10)(1-(9/10)^{601})}.
\]
区间计算中 |h₆₀₀|<10、|h₆₀₀+1|>1，因此最终 t 的误差小于 40L<10⁻¹⁸。结合 Δ(t(τ*))=0，这严格区分 (1) 的四个根；不是只用浮点近似命名分支。

## 2. 三个其它分支的完整端点周期

仍记 κ=5√5/4、Θ=−5√5L(3,χ₅)/16，并使用前稿的 f−、f+。在 |q|<1，实际原函数可以重组为
\[
 f_\mp(q)=\sum_{m\ge1\atop m\text{ odd}}
  \frac{G_\chi(q^m)-\tfrac12G_\chi(q^{2m})}{m^3}
 \ \mp\kappa\sum_{n\ge1}\frac{\chi(n)}{n^3}
  \left(\frac{q^n}{1+q^n}-\frac12\frac{q^{2n}}{1+q^{2n}}\right),
\tag{3}
\]
其中 Gχ(z)=z(1−z²)/Φ₅(z)，负下标取后项减号。这是 oldform 的第三原函数所需的全部 2⁻³、4⁻³ 因子，不是形式反演。

在奇数导子 c、5∤c 的根 ρ=exp(2πix/c) 处，全部有理核沿有限条径向射线均不命中其极点，所以 (3) 由 Σn⁻³ 支配并具有实际 Abel 极限。令
\[
 D_n=-\frac15\sum_{j=0}^4j\chi(n+cj),\qquad
 B_3(y)=y^3-\frac32y^2+\frac12y,
\]
\[
 E(x,c)=\sum_{n=1}^{c}D_n\left[
  B_3(\{xn/c\})-\frac58B_3(\{2xn/c\})
                 +\frac1{16}B_3(\{4xn/c\})\right],
\]
\[
 F(x,c)=\frac12\sum_{k=1}^{c-1}\sum_{u=1}^{4}
    (-1)^{k+1}\chi(u) B_3(\{xk/c+u/5\}),\qquad
 F_{20}=F(x,c)-\frac12F(2x,c).
\tag{4}
\]
实际 Fourier–Bernoulli identity 及 χ₅ 的 Gauss 和给出
\[
 \lambda_-:=f_-(x/c+i0)=\Theta+i\pi^3\left(\frac23E-\frac56F_{20}\right),
\]
\[
 \lambda_+:=f_+(x/c+i0)=-\Theta+i\pi^3\left(\frac23E+\frac56F_{20}\right).
\tag{5}
\]
有限和的完整精确值为

|branch|E|F₂₀|λ−−Θ|λ++Θ|
|---|---:|---:|---:|---:|
|α|0|0|0|0|
|γ−|−1/8|−4/25|iπ³/20|−13iπ³/60|
|γ+|1/8|4/25|−iπ³/20|13iπ³/60|
|β|−43/216|19/135|−iπ³/4|−5iπ³/324|

## 3. 这证明了什么样的 branch 障碍

在 (2) 的局部坐标 z=τ+b/a、N=20a² 中，V−、A− 的反演符号均为 ε−=−χ(d)，V+、A+ 的符号均为 ε+=χ(d)。实际 Eichler 恒等式为
\[
 f(\tau)-\varepsilon Nz^2f(s\tau)=P(z),\qquad
 P(z)=\lambda(1-\varepsilon Nz^2)+(2\pi iz)L_{\rm twist}(2).
\tag{6}
\]
ε=−1 时中间临界值因函数方程而为零。令 H=A(f−c₀)，其中 c₀=Θ 或 −Θ，则
\[
 H(\tau)-H(s\tau)
 =A(\tau)\left[P(z)-c_0(1-\varepsilon Nz^2)\right].
\tag{7}
\]
因此该 canonical leaf 要在 coarse t 分支点 holomorphic，必要条件就是 λ=c₀。表中三个其它 branch 的两个 embedding 都不满足这个必要条件，且 A 非恒零，所以 (7) 非恒零。这严格证明了这六条标准延拓的非平凡二阶分支。并不需要猜测尚未计算的 L_twist(2) 来判定它们。

另一方面，任何到这些 elliptic points 的实际延拓在 τ 局部都是 holomorphic，s²=−20I 在半平面的 Möbius 作用为恒等。故绕 coarse branch 两周后全部原函数和周期误差均返回，**局部 monodromy 阶数至多为二**。这些点没有不可消除的 logarithmic monodromy；偶数 ramification 可以把它们的实际拉回变成 holomorphic。

这里没有分类通过其它全局 cusp loops 产生的所有叶，也没有证明三个 branch 在所有可能叶上都不正则。需要更换叶时必须重算其 Eichler cocycle。下文共同 cover 保留 canonical α 叶，并对其余 branch 使用避开或偶数 ramification，因而不依赖这个尚未证明的全叶分类。

## 4. 与 CDT Corollary 9.0.19 的精确匹配

参见 [固定 CDT 原文](../literature/cdt2024_l2_chi_minus3.pdf)，§9，PDF 146–151 页，特别是 Definition 9.0.12、Lemma 9.0.13 和 Corollary 9.0.19。其 h₂(q)=−256q∏(1+qⁿ)²⁴ 是两 cusp、一个 order-2 elliptic point y=4 的 orbifold cover。它不会自动变成 level 20 三 cusp、四 elliptic points 的 cover。

若 y=4t/β，使用
\[
 \varphi_t=\frac\beta4 h_2\circ\psi,\qquad
 \psi:D\to D,\quad\psi^{-1}(0)=\{0\},
\tag{8}
\]
则 β 的全部 fibers 自动具有偶数 ramification。按照原文 descent datum 和单 elliptic corollary 的 **affine C 域证明**，一组充分条件是：

- 将 yα=4α/β 放入 Σ⁰，在含 0 与 yα 的 contractible U 上选择已证 holomorphic 的 canonical 两个周期误差；全部 α fibers 必须在原点的同一 univalent leaf 内。
- 将 4/β、4γ−/β、4γ+/β 放入 Σ¹，要求 φ_t 避开 cusp 1 和两个复 elliptic values。
- 保留原点唯一 preimage；∞ 是原文 Y₀(2) 的另一 cusp，φ_t 为 holomorphic 故本身不取 ∞。

这可以使 H−、H+ 同时拉回。其 t 导数及 t 有理系数微分组合一般拉回为 meromorphic；finite poles 可按原文用固定多项式清除，不能由此删除 cusp 的 log 分支。

原文 p150 展示的 analytic-path 删除集合没有打印 ∞，但 §9 的 Y₀(2)=P¹∖{0,∞} 和 p148 的 descent datum 明确保留该 cusp。本稿的 H 在 ∞ 有 log³ 项，不能按 p150 的显示集合字面宣称在 ∞ holomorphic。这里使用同一证明在 affine C 上、显式不取 ∞ 的版本；第5节及后面的完整共同空间另有直接解析证明，不依靠省略这一条件。

更一般的实际 orbifold cover 可以对 β、γ−、γ+ 全部 fibers 施加偶数 ramification，而无需避开它们。局部拉回证明正是上节的二周返回。此时仍须避开 cusp 1、控制返回 t=0 的全部 fibers，并把 α 的所有 fibers 放在正确的 canonical univalent leaf。只给 map 的 derivative，未核验这些条件，不能应用 CDT。

## 5. 一个明确合法的共同 cover

令 Ω 为圆盘 |t+2|<103/40，取
\[
 \boxed{\varphi(z)=\frac{4209z}{4120+3200z}}.
\tag{9}
\]
这是 D 到 Ω 的 conformal isomorphism，φ(0)=0、φ′(0)=4209/4120>1，φ⁻¹(0)={0}。Ω 包含 0 与 α，避开 β、γ±、cusp 1 和 ∞。例如
\[
 |\gamma_\pm+2|^2=\frac{51+\sqrt5}{8}>
 \left(\frac{103}{40}\right)^2;
\]
复根的严格比较可用 √5>11/5；α、β 及 cusp 1 的其余比较由 2<√5<3 给出。原点芽在 α 的 local monodromy 为恒等，在 Ω 内没有其余实际 singular values，因此 monodromy theorem 给两个周期误差在 Ω 上的共同 holomorphic 叶。

这已经是一个完整合法的 CDT 解析输入；导数收益只有 log(4209/4120)，没有接近需要的算术预算。若要求 (8) 的表示，由 Ω 避开 β，h₂ 的 canonical inverse 可在 4Ω/β 上整体提升，给 ψ:D→D；(9) 的 injectivity 又保证所有 α fibers 在同一 univalent leaf。该 map 不是新的数值定理，也不主张为最优 cover。

## 6. 大 cover 的两个真实限制

CDT §2.8，PDF 第24页，使用 Carathéodory 定理：若 holomorphic φ:D→C∖{1} 满足 φ⁻¹(0)={0}，则 |φ′(0)|≤16。对省略的任意非零 a 缩放同样得到 |φ′(0)|≤16|a|。

因此，按 (8) 直接匹配单 elliptic corollary 并避开 γ± 时，必有
\[
 |\varphi_t'(0)|\le16|\gamma_\pm|
   =16\sqrt{\frac{3+\sqrt5}{8}}<13,
 \qquad \log|\varphi_t'(0)|<\frac{13}{5}.
\tag{10}
\]
所以只引用 |h₂′(0)|=256 得到的 64β≈57.16 是没有支付 ψ 的避点限制的名义上界，不能视为已存在 map 的解析收益。

即使新 cover 对三个剩余 elliptic fibers 都偶数分歧，它仍需避开实际 logarithmic cusp 1。在 c=4,5 的局部 q_c 中，两个 H 的最高 log(q_c)³ 系数均为 −17/6，减 ΘA 只影响低阶。这一最高项不因绕 cusp 增添低次周期而消失，也不因有限 ramification 而消失。因此 cusp 1 不能像 elliptic branch 一样用 ramification 处理。在保留 φ⁻¹(0)={0} 的范围内，必有
\[
 \boxed{|\varphi'(0)|\le16.}\tag{11}
\]
这是明确条件下的解析上界，不是对改变返回原点规则、目标商或全 CDT 方法的否定。

作为账本的条件接口：若某完整 rank-4 元组恰为一个免费常数和三条指数 3 的行，flat 成本是 45/16，而
\[
 \log16<\frac{45}{16}.
\]
那么该自然元组连正 holonomy denominator 都没有；需要新的便宜背景、真实分母过滤或不同目标投影。每个误差的实际 cyclic rank 为四、合并 rank 为七，现已由 [根分支完整模型](cdt_odd_level20_model_20261006.md) 另证；这里的条件账本没有替代合并系统及背景的完整成本核查。

## 7. 真正三 elliptic orbifold 的新曲线输入

把 α 从 branch set 中解除后，β、γ± 的共同 order-2 cover 可先通过
\[
 E':\quad v^2=(t-\beta)(t-\gamma_-)(t-\gamma_+)
\tag{12}
\]
提升。这是 genus-1 曲线，另在 ∞ 分支。其 j 恰为
\[
 j(E')=\frac{32}{5}(47+21\sqrt5),\qquad
 N_{\mathbb Q(\sqrt5)/\mathbb Q}(j)=\frac{4096}{25}.
\]
这给出了明确的新 uniformization 输入；不能自动沿用原 level-20 eta 参数来解已解除 α 的 orbifold。还必须处理 t=0、1 的两套 preimages 和 ∞，以及原点的 canonical leaf。这里未建立新曲线的 cusp-filling conformal size 或 capacity 界。

## 8. 已存在的完整共同解析空间：Hecke group

现在可以直接从真实周期建立一个比单叶更强的共同输入。两个 H 都来自 q-series，故对 T:τ↦τ+1 不变；前稿已证它们对 W₂₀ 不变。于是 H−、H+，以及它们的全部 t 导数，均在
\[
 G=\langle T,W_{20}\rangle
\tag{13}
\]
下不变。derivative closure 在 ramification points 允许 finite poles，所以是共同 meromorphic 函数系统。

变量 ζ=√20τ 将 (13) 精确变成 Hecke group
\[
 \zeta\mapsto\zeta+\sqrt{20},\qquad \zeta\mapsto-1/\zeta.
\]
参数 √20>2 的 group 是 discrete、infinite-area，quotient 有一处 cusp、一处 order-2 elliptic point 和一处 funnel；其基本域为 |Re ζ|<√20/2、|ζ|>1。此拓扑事实见 [Soares 原始预印本，Introduction (1)，PDF第1–2页](../literature/soares2020_hecke_triangle_transfer_v1.pdf)，[出版版本](https://link.springer.com/article/10.1007/s00023-021-01117-1)；本地原件及 SHA 见 [新文献 manifest](../literature/manifest_cdt_odd_level20_leaf_20261006.json)。

对这个 geometric finite group，funnel 提供非退化的 conformal boundary circle；coarse quotient 是 genus 0 的 punctured bordered disk。填充唯一 cusp 并在 elliptic point 使用其 coarse coordinate，得到一个具有解析边界的 simply connected bordered disk X_G。它的 interior 因而 conformally 等价于 D。这里不是把四 elliptic 的原 Γ₀(20) orbifold 误当成一个 Hecke triangle group；G 是其 infinite-index subgroup，只有一个 elliptic orbit。

以下逐项说明目标函数如何在 X_G 延拓：

1. 在上半平面，f±、A± 都是实际 holomorphic 函数。H± 的 G 不变性使它们成为 coarse quotient 上的 holomorphic 函数；唯一 elliptic orbit 是 W₂₀ 的 orbit，真实不变性正好保证 local degree-2 quotient 的下降。
2. 唯一 cusp 的 stabilizer 是 ⟨T⟩，所以 q=exp(2πiτ) 是其标准局部坐标。H± 的原始 q Taylor 芽使它们在填充的 cusp 点 P 正则。
3. t 也 G 不变。eta units h、u=h+1 在上半平面无零点或极点，所以 t=1/u 在 interior 是 holomorphic，既不取 0，也不取 1。填充唯一 cusp 后，t=q+O(q²)，只在 P 有一个简单零点。其它 Γ₀(20) cusp 的 preimages 位于 real/conformal boundary，不是 X_G 的 interior 点。

选 Riemann mapping F:(D,0)→(X_G,P)，定义
\[
 \boxed{\Phi=t\circ F:D\longrightarrow\mathbb C\setminus\{1\}.}
\tag{14}
\]
它满足 Φ⁻¹(0)={0}，并真正同时拉回两个 H 为 holomorphic，全部有限 derivative closure 为 meromorphic。对 β、γ± 的每个 interior fiber，G 中没有相应 stabilizer，故 t 的 coarse local degree 是2，(14) 自动具有所需 even ramification。α 的唯一 G-elliptic orbit 在 coarse source 上已解除分歧，H 在那里下降；其它 α fibers 仍由 even ramification 消除。因此不需要未经证明地把全部 α fibers 都放在一个 univalent leaf：这里使用的是 **全局真实 G 下降证明**，而不是声称满足原文单 Σ⁰ corollary 的所有条件。

记
\[
 \rho=|dq(F(z))/dz|_{z=0}=|\Phi'(0)|.
\]
第5节的 Ω 分支在 α 处 lift 到 G 的已填充 coarse point。更明确地说，Ω∖{0,α} 的两个基本 loops 在原始 uniformization 的 monodromy 是 T、W₂₀；两者属于 G，所以这个 initial sheet 在 G quotient 中的 lift monodromy 都是恒等。0 处由标准 q 坐标填充，α 处由 coarse W 坐标填充；t 在这两个 source 坐标中的 local degree 都是1。因此所选 inverse branch 给出 Ω 到 X_G 的 injective holomorphic map（复合 t 后为 Ω 上恒等）。以 (9) 参数化，再与 F⁻¹ 合成，对 D→D 使用 Schwarz 引理得到
\[
 \boxed{\frac{4209}{4120}\le\rho\le16.}\tag{15}
\]
上界是 (11)。这严格证明共同 cover 存在且原点导数大于1；没有宣称 ρ 已超过某个所需指数门槛。为满足 holonomy 定理对闭盘邻域的条件，可使用 Φ(rz)、0<r<1，并在需要时乘固定 polynomial 清 derivative 的 finite poles。

这使剩余问题更具体：完整 G common cover 已经存在，所缺的是其可认证的 conformal size、边界 capacity/重排数据，以及与真实廉价背景兼容的 convexity 或多 map 不等式。普通单 map Jensen bound 可能仍被现有账本阻止，不能因 (14) 的存在就宣称新无理性证明。

## 9. 验证与剩余工作

[精确/interval 脚本](cdt_odd_level20_leaf_20261006_verify.py) 与 [JSON](cdt_odd_level20_leaf_20261006_verify.json) 检查 (1)–(2)、kernel 身份、所有 finite Bernoulli 常数、周期不相等条件、eta 尾界和 root isolation、显式共同 map 的几何比较，以及 (10)–(12) 的精确算术。interval 部分仅负责已有 exact double-cover 下的 branch 标签，不形式化证明整个 modular uniformization。

独立审阅：`low_period_closure` 分支重新推导 §§2–6 的所有 Bernoulli 常数、周期必要条件、local Z2、circle map 及两个 omission 上界，均通过；同时复核原文 p24、p148–151 的条件。根分支另行审阅 §8：从 Hecke 基本域重算一 cusp/一 elliptic/一 funnel 的拓扑，核验真实 G 下降、eta units 的 interior 避点、唯一 q 填充零点、其它 elliptic fibers 的二阶分歧，以及 Ω lift 的 T/W monodromy 消去和 Schwarz 比较，均通过。审阅不提供尚未计算的 conformal size/capacity，也不把有限 jet 当作这些解析论证的 Lean 形式化证明。

当前推进路线已具体化：利用 (14) 已证存在的完整共同 cover，建立可认证的 conformal size/capacity 或多 map/convexity 数据；同时在同一实际函数系统上加入便宜背景并重算账本。只有严格 holonomy 不等式通过后，才能得到新的数值结论。
