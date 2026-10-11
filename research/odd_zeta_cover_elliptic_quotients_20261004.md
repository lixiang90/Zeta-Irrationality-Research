# Catalan 覆盖的椭圆商与显式长度二对数核

日期：2026-10-04。承接冻结的 [覆盖报告](E:/kimi-build/zeta5/research/odd_zeta_cover_catalan_20261004.md)，不修改旧稿。以下均为固定几何与实际函数身份，不作参数搜索，不证明 Catalan 常数无理。

本轮推进不止于“genus 3 不能由 P¹ 参数化”：三个次数二椭圆商给 Jacobian 的实际分解；目标导数进一步下推为两个商上的 `log u · dlog F`。两个单商符号具有非平凡 tame symbols，而它们在 genus 3 曲线上拉回后恰好相消。这个结果给出明确的函数域 K₂ 候选及后续整性接口，尚不等于算术整模型上的类或已识别的调节子。

## 1. 三个商确实都是次数二的 genus 1 曲线

设 C 为

\[
Y^2=Q(s)=s^8-14s^4+1
\]

的光滑射影模型。Q 无重根，C 的 genus 为 3。两个定义于 Q 的对合

\[
\sigma(s,Y)=(-s,Y),\qquad
\tau(s,Y)=(s^{-1},Y/s^4)
\]

可交换且都不恒等，生成 V₄。反演写成函数域自同构后，在光滑射影曲线上唯一延伸，所以 0、∞ 不构成映射缺口。

三个商的显式映射如下：

| 商 | 映射坐标 | 商曲线 |
|---|---|---|
| C/⟨σ⟩=E₀ | x=s²，y=Y | y²=x⁴−14x²+1 |
| C/⟨τ⟩=E₊ | x=s+1/s，y=Y/s² | y²=x⁴−4x²−12=(x²−2)²−16 |
| C/⟨στ⟩=E₋ | x=s−1/s，y=Y/s² | y²=x⁴+4x²−12=(x²+2)²−16 |

每行坐标都被相应对合固定；反向 s 分别满足 `s²=x`、`s²−xs+1=0`、`s²−xs−1=0`。相应对合非平凡，所以函数域次数恰为 2，写出的域就是固定域。三个四次式都无重根，双覆盖 P¹ 有四个简单分支点，因此光滑模型 genus 1。四次式首项为平方，两个无穷远点均有理；选其一为原点即可视为 Q 上椭圆曲线。

也可直接核 Riemann–Hurwitz：σ 在 s=0、∞ 各固定两点；τ 在 s=±1 各固定两点；στ 在 s=±i 各固定两点。三个对合各有四个固定点，故每个商的 genus 都是 1。

## 2. Jacobian 分解、j 与固定整格范围

C 的一类微分基为

\[
\omega_0=ds/Y,\quad\omega_1=s\,ds/Y,\quad\omega_2=s^2ds/Y.
\]

三个商的微分拉回为

\[
\pi_0^*(dx/y)=2\omega_1,\quad
\pi_+^*(dx/y)=\omega_2-\omega_0,\quad
\pi_-^*(dx/y)=\omega_2+\omega_0. \tag{1}
\]

它们相对于上述基的矩阵行列式为 4。因此由商映射诱导的

\[
\Psi:\operatorname{Jac}(C)\longrightarrow E_0\times E_+\times E_-
\]

在余切空间上是同构。两边都是维数 3 的阿贝尔簇，char 0 下其核有限、像满维，故 Ψ 为 Q 上 isogeny：

\[
\boxed{\operatorname{Jac}(C)\sim_{\mathbf Q}E_0\times E_+\times E_-.} \tag{2}
\]

这给的是直接证明，无需把 Kani–Rosen 当黑箱。标准 Jacobian 与余切空间解释可参见 [Milne 作者稿，Jacobian Varieties](https://www.jmilne.org/math/articles/1986c.pdf)。

进一步，V₄ 的平均 `1+σ+τ+στ` 在 H⁰(C,Ω¹) 上为 0，所以它在 Jacobian 上为零。若 Φ 是三个 pullback 的和，则

\[
\Phi\Psi=(1+\sigma)+(1+\tau)+(1+\sigma\tau)=[2]. \tag{3}
\]

于是这个固定分解的核被 2 杀掉。它本身只引入固定格成本；不能由此推出随近似次数指数增长的 gcd，参见 [content 报告的固定群结论](E:/kimi-build/zeta5/research/odd_zeta_content_geometry_20261004.md)。更不能由 (2) 推出某个迭代积分值的无理性。

对于 `y²=x⁴+ax²+b`，实际双有理 Weierstrass 变换为

\[
X=2(y+x^2)+a,\quad Z=2xX,\qquad
Z^2=X\bigl(X^2-2aX+a^2-4b\bigr).
\]

由其 c₄、Δ 得

\[
j=\frac{16(a^2+12b)^3}{b(a^2-4b)^2}.
\]

因此

\[
\boxed{j(E_0)=35152/9,\qquad j(E_+)=j(E_-)=2048/3.} \tag{4}
\]

三个值都是非整数有理数。CM 椭圆曲线的 j 必须是代数整数，所以三者均无 CM；所用标准定理有 [Sutherland，MIT 18.783 2025 Lecture 20，Corollary 20.13](https://ocw.mit.edu/courses/18-783-elliptic-curves-fall-2025/mit18_783_f25_lec20.pdf) 的完整证明。E₊、E₋ 通过 `(x,y)↦(ix,y)` 在 Q(i) 上同构，故“有三个商”不意味着三个几何互不相同的椭圆因子。无 CM 本身也不提供本项目所需的整性或无理性结论。

## 3. 目标实际导数下推为两个椭圆商上的迭代 dlog

沿 C 原点 `(s,Y)=(0,1)` 取正则分支。冻结覆盖报告中

\[
A=\int_0^s\frac{du}{1+u^4},\quad
B=\int_0^s\frac{u^2du}{1+u^4},\quad
b_s=(1+s^4)/Y,\quad g_c=v_c/b_s
\]

满足 `g_c(0)=c` 和

\[
dg_c=A\eta_A+B\eta_B,
\quad
\eta_A=\frac{4s^2(s^4-7)}{1+s^4}\frac{ds}{Y},\quad
\eta_B=\frac{4(1-7s^4)}{1+s^4}\frac{ds}{Y}. \tag{5}
\]

定义 E₊、E₋ 上的一阶外核

\[
\eta_+=\frac{4(x^2+6)}{x^2-2}\frac{dx}{y},\qquad
\eta_-=\frac{4(x^2-6)}{x^2+2}\frac{dx}{y}.
\]

直接因式分解给

\[
\pi_+^*\eta_+=\eta_A-\eta_B,\quad
\pi_-^*\eta_-=\eta_A+\eta_B,
\]

而内层也下推：

\[
d(A-B)=\pi_+^*\frac{-dx}{x^2-2},\qquad
d(A+B)=\pi_-^*\frac{dx}{x^2+2}. \tag{6}
\]

两商均以 π±(0,1) 的无穷远点为基点。置 `a=√2`，取在该点等于 0 的对数原函数：

\[
u_+=\frac{x+a}{x-a},\quad
u_-=\frac{x-ia}{x+ia},\qquad
A-B=\pi_+^*\frac{\log u_+}{2a},\quad
A+B=\pi_-^*\frac{\log u_-}{2ia}. \tag{7}
\]

外层还能精确写成 dlog。令

\[
r_+=\frac{i}{a}x(6-x^2),\quad
F_+=\frac{y-r_+}{y+r_+};\qquad
r_-=\frac{x(x^2+6)}a,\quad
F_- =\frac{y-r_-}{y+r_-}.
\]

它们满足

\[
y^2-r_+^2=\tfrac12(x^2-2)^2(x^2-6),\quad
y^2-r_-^2=-\tfrac12(x^2+2)^2(x^2+6),
\]

\[
\boxed{d\log F_+=(i/a)\eta_+,\qquad d\log F_-=(1/a)\eta_-.} \tag{8}
\]

例如 `dlog((y−r)/(y+r))=(r f′−2fr′)/[(f−r²)y] dx`，其中 `y²=f(x)`；代入即可核 (8)。故最终的目标核是

\[
\boxed{dg_c=-\frac i4\left[
\pi_+^*(\log u_+\,d\log F_+)
+\pi_-^*(\log u_-\,d\log F_-)
\right].} \tag{9}
\]

两个对数在基点消失，积分等式 `g_c=c−(i/4)(I₊+I₋)` 有明确初值；I± 是从指定无穷远点沿 π± 所投影路径的实际积分。F± 在无穷远趋 −1，外核正则，故基点没有积分发散。

这不是普通椭圆一类周期。一个直接障碍是：在 C 上任取 α⁴=−1，A、B 的对数增量分别为 `2πi/(4α³)`、`2πi/(4α)`。所以绕相应点后

\[
\Delta(dg_c)=\frac{2\pi i}{4\alpha^3}
(\eta_A+\alpha^2\eta_B)\ne0. \tag{10}
\]

括号中分子的导数在 s=α 为 `8α`，故虽在那里消掉极点，仍是非零代数微分。单个 Abelian integral 的导数则为单值代数微分。因此目标的真实函数不能靠 (2) 就改写为一个普通 Abelian integral；有限覆盖也不能杀掉这个非零加性对数 monodromy。此论证不排除某个特殊数值发生额外简化。

已证真值相消给一个有用的端点接口：`s₀²=2−√3`、`Y(s₀)=0` 的内侧点满足 `g_G(s₀)=0`，其两商坐标分别为 `(√6,0)`、`(−√2,0)`。于是沿原已认证的实路径

\[
G=\frac i4\left[I_+(\sqrt6,0)+I_-(-\sqrt2,0)\right]. \tag{11}
\]

端点是简单分支点，(9) 的积分可积；(11) 仅利用已有真实相消，没有调用 G 无理性。它仍是长度二积分值，而非已识别的 Bloch–Beilinson 调节子值。

## 4. tame symbols 的实算：单商不无分歧，拉回和才相消

所有显式函数定义在 `K=Q(i,√2)` 上。先在函数域 Milnor K₂ 中考虑

\[
S_+=\{u_+,F_+\},\qquad S_-=\{u_-,F_-\}.
\]

采用局部 tame 约定

\[
\partial_P\{u,F\}=(-1)^{v_P(u)v_P(F)}
\left(u^{v_P(F)}/F^{v_P(u)}\right)(P).
\]

E₊ 上全部四个可能的非平凡点为：

| P | ord u₊ | ord F₊ | tame S₊ |
|---|---:|---:|---:|
| (a,4i) | −1 | 2 | 2 |
| (a,−4i) | −1 | −2 | 1/2 |
| (−a,4i) | 1 | −2 | 2 |
| (−a,−4i) | 1 | 2 | 1/2 |

例如在 `(a,4i)`，以 `t=x−a` 为参数，有 `u₊~2a/t`、`F₊~t²/4`，故 `u₊²F₊→2`。E₋ 在 x=±ia 的四点给完全相反的 y 字符：`y=4i` 时 tame 为 1/2，`y=−4i` 时为 2。无穷远 `u→1,F→−1`；范数因式中的其余简单分支点，F 的分子分母同阶相消、趋 1。因此没有漏掉其他水平零极点。

所以 **S± 单独不是光滑射影 E± 上 tame 全为 1 的符号**。但两商 y 坐标同为 Y/s²，且 C 上这些点均无商映射分歧。于是

\[
T=\pi_+^*S_++\pi_-^*S_-\in K_2^M(K(C))
\]

在 C 的全部几何点 tame 都为 1。这可称“函数域符号通过光滑射影曲线的水平 tame 检验”；不由此称它为算术整模型上的无分歧类。两点须特别区分：

- K₂ 符号的 tame 相消没有证明 T 非零，也没有证明 (11) 是其特定调节子分量。
- 本计算未检查任何整模型的垂直除子、坏素数、所有共轭及所需的算术下降。固定曲线只有有限坏约化素数，不意味着近似系数只出现有限分母素数。

还有一个下降量词的限制。`a↦−a` 使 u±、F± 同时变逆，因此 S± 不变；`i↦−i` 使 S± 均变负。因此 T 的 K/Q(i) 字符平凡、Q(i)/Q 字符为反不变，与 χ₋₄ 型目标一致。其 Q-trace 在有理化的 K₂ 中为零；整系数 trace 还可能有 torsion，不能省略这个范围。它不能直接当作 Q 上的 rational regulator 输入。

[Goncharov–Levin，alg-geom/9508008v4，Theorem 1.2](https://arxiv.org/pdf/alg-geom/9508008v4)／[本地存档](E:/kimi-build/zeta5/literature/goncharov_levin1997_zagier_elliptic_k2_v4.pdf) 给椭圆 K₂ 与调节子的相关框架。本报告没有把其 Q-rational 条件或非零结论套到上述 K 上符号。

## 5. 已完成的桥梁与下一项可证问题

本轮固定身份已把目标落实为两个显式椭圆商、两组 log 参数以及四点 tame 表，避免只说“使用椭圆几何”。可继续的具体问题是：对 T 作 Q(i) 的 transfer/descent，分清恒等为零、decomposable 与非平凡类；随后在指定整模型中核垂直 tame，最后证明 (11) 与某个调节子分量的精确关系。即便这些步骤成立，还要另构造随尺度增长的整数周期近似及完整 content／实衰减预算。Jacobian 分解或 K₂ 类存在本身不提供这个最后桥梁。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004_verify.py) 和 [JSON](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004_verify.json) 已运行通过。它们检查商方程、四次式无重根、(1) 的行列式、V₄ 平均、实际 Weierstrass 变换、j、(6)–(8)、所有四点局部 leading jets 与 tame 值，以及 E± 的 Q(i) 同构；不检查 T 非零、调节子识别或算术整性。
