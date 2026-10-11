# Level 12 的纯 ζ(7) Eichler 触发器：变换已闭合，holonomy 尚未闭合

日期：2026-10-05。本文是新建的数学接口报告，旧研究记录与论文保持冻结。本文没有证明 ζ(7) 无理，也不以该假设检验计算。得到的是一条可以实际审计的 CDT 型触发器：某个有理系数组合能跨越指定 Fricke 分支点，当且仅当其系数满足含真实 ζ(7) 的数值关系。

## 1. 与 CDT 的对应关系及证据范围

CDT 固定版本 [arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2) 的 §11–13 不是从一般的端点归零推出无理性。其关系假设使一个有理系数芽同时成为过度延拓的真实周期误差，随后才核算整个函数空间的整型与解析能力。§15.1.10（印刷 pp.192–193）建议从特殊 Hermite–Padé／holonomic 线性形式的生成函数继续寻找这样的接口，并强调普通近似指数不能代替 holonomy 预算。

这里使用另一条原始来源：[Beukers, *Irrationality proofs using modular forms*, 1987](https://www.numdam.org/article/AST_1987__147-148__271_0.pdf)，Proposition 1.2（印刷 p.273）的 Eichler–Fricke 周期多项式。其 Theorem 1（pp.275–276）已用权 4 模形式重证 ζ(3) 无理。下面的 level 12 权 8 实例是项目内的显式推导；未检索到完全相同的原始表达不等于全球首次，本文不作新颖性断言。

关键限制先列清楚：下面的 q 级数是实际解析函数，但 **q 变量中的模形式级数不能自动称为 holonomic/G-function**。要应用 CDT，仍需明确模函数坐标、完整下降后的微分系统、全部分支及实际函数独立秩。这些由另一篇 [level 12 模型报告](cdt_odd_level12_model_20261005.md) 独立处理；本文不将尚未完成的接口写成已完成的 holonomy 证明。

## 2. 固定 F₈、A₆ 及其所有 Fourier 分母

令 q=exp(2πiτ)，τ 位于上半平面。使用标准正规化

\[
 E_8(\tau)=1+480\sum_{n\ge1}\sigma_7(n)q^n,
 \qquad E_6(\tau)=1-504\sum_{n\ge1}\sigma_5(n)q^n.
\]

定义

\[
\begin{split}
F(\tau)=\frac1{480}\{&4E_8(\tau)-2288E_8(2\tau)+46332E_8(3\tau)\\
 &-146432E_8(4\tau)+185328E_8(6\tau)-82944E_8(12\tau)\},\tag{1}
\end{split}
\]

\[
A(\tau)=E_6(\tau)-1728E_6(12\tau),\qquad
f(\tau)=\sum_{n\ge1}\frac{a_n}{n^7}q^n,
\quad F(\tau)=\sum_{n\ge1}a_nq^n.\tag{2}
\]

写 D=(1,2,3,4,6,12)，u=(4,−2288,46332,−146432,185328,−82944)，则

\[
a_n=\sum_{\delta\in D,\,\delta\mid n}u_\delta\sigma_7(n/\delta)\in\mathbb Z,
\quad a_1=4,\qquad
A(q)\in\mathbb Z[[q]],\quad A_0=-1727, A_1=-504.\tag{3}
\]

常数项之和为零，所以 (1) 确实没有常数项；除以 480 没有产生任何 Fourier 系数分母。所有级数在 |q|<1 绝对收敛，且 θ⁷f=F，θ=q∂q。

令 L_n=lcm(1,…,n)。对每个 n，**所有素数**的安全前缀分母是

\[
L_n^7 f_0,\ldots,L_n^7 f_n\in\mathbb Z,
\qquad L_n^7 [q^j](Af)\in\mathbb Z\quad(0\le j\le n).\tag{4}
\]

这里没有漏掉 2、3、480 的因子。f 的实际前缀最小分母为

\[
\delta_f(n)=\operatorname{lcm}_{1\le j\le n}
\frac{j^7}{\gcd(j^7,a_j)}.\tag{5}
\]

对 B=Af，取 b_j=[q^j]B，实际共同分母也可完整写成

\[
\delta_B(n)=\frac{L_n^7}
{\gcd(L_n^7,L_n^7b_0,\ldots,L_n^7b_n)}.\tag{6}
\]

这两式包含坏素数处的真实 content；有限证书不把 (4) 的上界误报为每个 n 的最小分母。

## 3. Fricke 变换、非尖点性与整个 Mellin 函数

置 Wτ=−1/(12τ)。标准 E₈ 变换给

\[
F(W\tau)=-12^4\tau^8F(\tau),\qquad
A(W\tau)=-12^3\tau^6A(\tau).\tag{7}
\]

这是精确恒等式。一个简洁的核验是把 F 写成

\[
F=\frac1{480}\{4(e_1-e_{12})-143(e_2-e_6)+572(e_3-e_4)\},
\quad e_\delta=\delta^4E_8(\delta\tau).
\]

因 eδ(Wτ)=12⁴τ⁸e₁₂/δ(τ)，每个括号都为 Fricke 反特征。A 的核验完全相同。

**F 不是全尖点形式。** 对 γc=(1 0;c 1)，F|₈γc 的常数为

\[
\frac1{480}\sum_{\delta\in D}u_\delta
\left(\frac{\gcd(c,\delta)}{\delta}\right)^8.
\]

在 c=1,2,3,4,6,12 六个 cusp 依次为

\[
0,\quad-476/81,\quad6273/64,\quad-2788/9,\quad476,\quad0.\tag{8}
\]

因此其它四个 cusp 不能自动删去。但 F 在这次 Fricke 配对的 ∞、0 两个 cusp 都消失：F(iy) 在 y→∞ 指数衰减，(7) 使它在 y→0 也为 y⁻⁸ 乘指数衰减。故

\[
\Lambda(s)=\int_0^\infty F(iy)y^{s-1}\,dy
\]

对所有 s 为整函数，并满足

\[
\Lambda(s)=-12^{4-s}\Lambda(8-s).\tag{9}
\]

这一步使用实际收敛积分，**无需任意的 Eisenstein 正则化**。在 Re s>8 逐项积分得

\[
\Lambda(s)=\frac{\Gamma(s)}{(2\pi)^s}L(F,s),
\quad L(F,s)=P(s)\zeta(s)\zeta(s-7),\tag{10}
\]

\[
P(s)=4-2288\,2^{-s}+46332\,3^{-s}-146432\,4^{-s}
      +185328\,6^{-s}-82944\,12^{-s}.\tag{11}
\]

后面的临界值一律指 (10) 的解析延拓，不把发散的原 Dirichlet 级数当作已收敛的和。

## 4. 完整临界值和 L(F,1) 的零乘极点

固定系数精确给出

\[
P(0)=P(8)=P(2)=P(4)=P(6)=0,
\quad P(3)=-44,\quad P(5)=11/3,
\quad P(7)=-209/216,\quad P(1)=1672.\tag{12}
\]

所以

\[
L(F,2)=\cdots=L(F,6)=0,\qquad
\Theta:=L(F,7)=\frac{209}{432}\zeta(7).\tag{13}
\]

在 s=3、5，不是 P(s) 消失，而是 ζ(s−7) 的平凡零使乘积消失。s=1 完全不同：ζ(s) 的简单极点与 ζ(s−7) 的简单零相消，留下

\[
L(F,1)=1672\zeta'(-6)
       =-\frac{9405}{\pi^6}\zeta(7).\tag{14}
\]

第二个等号由 Riemann ζ 功能方程在 −6 的导数得到。它也与 (9) 在 s=1,7 的配对精确一致。这一非零最高周期项不能丢掉；“全部中间临界值为零”不等于“周期多项式只有常数”。

## 5. 直接积分证明 Eichler 恒等式

记 C=(2πi)⁷/6!。由 Fourier 级数或七次微分，实际 f 满足

\[
f(\tau)=C\int_{i\infty}^{\tau}(\tau-z)^6F(z)\,dz.\tag{15}
\]

将 f(Wτ) 的积分用 z=Ww 换元；利用 (7)，得到

\[
12^3\tau^6f(W\tau)=-C\int_0^\tau(\tau-w)^6F(w)\,dw.
\]

两式相加，右端是从 i∞ 到 0 的固定路径积分。展开核并使用第3节实际收敛的 Mellin 积分：

\[
f(\tau)+12^3\tau^6f(W\tau)
=\sum_{r=0}^6\frac{L(F,7-r)}{r!}(2\pi i\tau)^r.\tag{16}
\]

这是 Beukers Proposition 1.2 在 k=8、ε=−1 的具体实例；ε=−1 来自 (−i√12τ)⁸=12⁴τ⁸，不能和 k=6 的符号混用。

代入 (13)、(14)：常数项为 Θ，而最高项为

\[
\frac{L(F,1)}{6!}(2\pi i\tau)^6=12^3\Theta\tau^6.
\]

因此完整周期多项式以及最终变换是

\[
f(\tau)+12^3\tau^6f(W\tau)=\Theta(1+12^3\tau^6),\tag{17}
\]

\[
h=f-\Theta,\qquad
h(W\tau)=-\frac{h(\tau)}{12^3\tau^6},\qquad
H=A(f-\Theta),\quad H(W\tau)=H(\tau).\tag{18}
\]

没有额外 ζ(3)、ζ(5)、π 的常数或未固定的积分常数。q→0 的正规化 f→0 已固定 (15)。此外，沿正虚轴 τ→0，(17) 给 f(τ)→Θ：这是实际 Abel 边界周期，不是对发散 Dirichlet 级数的形式赋值。

## 6. 真正的分支触发器及其充要关系

Fricke 的固定点是 τ₀=i/√12。取局部坐标

\[
w=\frac{\tau-\tau_0}{\tau+\tau_0},\qquad W:w\mapsto-w,
\quad t=w^2.
\]

A、f 在 τ₀ 都是实际解析函数，故 (18) 使 H 的 w 级数只含偶次幂，从而 H 是 t 的普通解析芽，真正跨越这个商分支点。

把 B=Af，则 (17) 给

\[
B(W\tau)=B(\tau)-\Theta(1+12^3\tau^6)A(\tau).
\]

于是对常数 a,b，有精确的单值差

\[
(aA+bB)(W\tau)-(aA+bB)(\tau)
=-(a+b\Theta)(1+12^3\tau^6)A(\tau).\tag{19}
\]

A 非零（A₀=−1727），另一个因子也非恒零。因此 aA+bB 能跨此分支点 **当且仅当** a+bΘ=0。若 a,b∈Q 不全为零，则必 b≠0，这正等价于 ζ(7)∈Q。

由 (3)，A、B 在 q=0 是 Q 系数芽；H 的常数项为 1727Θ。因此 H∈Q[[q]] 当且仅当 Θ∈Q。即真实周期误差本来有正确解析性，而假定数值有理性才使它进入有理系数空间。这不是简单的减常数：H 是 B−ΘA，A 本身是有非平凡变换的实际模形式。

**下降范围。** (18) 是 Fricke 变换下的实际局部下降。它不证明 H 对整个 Γ₀(12) 单值，也不证明所有共轭 Fricke 椭圆点或全部其它 cusp 的障碍都消失。要在 Hauptmodul 坐标下作 CDT 的 analytic map，仍须逐个核对其它 cusp、叶、单值化及返回原点的分支；(8) 已提示不能只保留一个奇点。

特别地，若使用上述模型报告的 h(Wτ)=12/h(τ)、t=1/(h+12/h+8)，正实 q 路径上的 τ₀ 对应 h=+√12，t=α=(2−√3)/4。这是本证明解除的分支。另一个固定值 h=−√12 对应 β=(2+√3)/4；它涉及共轭的 Fricke 路径，不能自动使用 (18) 删去。本文不把这两个分支混在一起。

## 7. 完整前缀指数与自然行精细类型的七层障碍

对 p≥5，n=pᵃ 时所有 δ∈D 除 δ=1 外都不整除 n，因此

\[
a_{p^a}=4\sigma_7(p^a)\equiv4\pmod p.
\]

(5) 因此在所有 p≥5 精确支付 7⌊logp n⌋ 层；2、3 的差最多为 O(log n)。所以

\[
\lim_{n\to\infty}\frac{\log\delta_f(n)}n=7.\tag{20}
\]

对 B，在第 pᵃ 系数中，唯一带 p^{7a} 最高分母的项是 A₀a_{pᵃ}/p^{7a}，其余 j<pᵃ 至多带 p^{7(a−1)}。因此除固定素数 2,3,11,157 外同样强制七倍最高层，给

\[
\lim_{n\to\infty}\frac{\log\delta_B(n)}n=7.\tag{21}
\]

若 Θ 假定有理，H=B−ΘA 只额外排除其固定分母素数，实际前缀指数仍为7。

还有一个比前缀指数更强的 **全尺度逐素数结论**。对所有充分大的 p，在 b_{p+1} 中只有 j=p 的 f 系数带 p 分母，故

\[
p^7b_{p+1}\equiv A_1a_p\equiv-2016\pmod p,
\quad v_p(b_{p+1})=-7.\tag{22}
\]

这里 p=7 及有限个小素数可以排除；它们不影响全尺度结论。Θ 有理时 H 同样满足 (22)。由于 p∤p+1，任何固定序号因子 (p+1)^e 都不能支付这些七层。

即使换到任意整数单位坐标 q(x)=x+q₂x²+⋯∈xZ[[x]]，第 p+1 系数也为

\[
[x^{p+1}]B(q(x))=b_{p+1}+p q_2b_p+\text{p 整数},
\]

而 p q₂b_p 的赋值至少为 −6；所以 −7 层不变。对假定有理的 H 也成立。因此在这条固定自然行和这些坐标下，任意固定有限 CDT 型

\[
M n^e\prod_{\ell}L_{\lfloor b_\ell n+c_\ell\rfloor}
\]

都至少含 **七个** bℓ≥1 的 active 列：每个固定列在 n=p+1 处至多提供一个 p 层，bℓ<1 的列在 p 大时完全不能提供 p。这是所有充分大素数的证明，不是有限抽样猜测。

限制仍重要：这没有排除新的有理 gauge、更多实际独立行、非整数坐标、额外的算术 content 或其它模数；更没有把单行7层成本偷换为整个系统的梯形 τ。根任务须按真实完整模块重新预算。

## 8. 下一接口与证书范围

本轮已经严格完成：整 Fourier F₈/A₆；非尖点但 paired cusp 的真实 Mellin 收敛；全部临界值与 L1 残差；完整周期多项式；Fricke 分支处数值关系的充要触发器；所有 Fourier 素数的安全型、真实前缀指数及七层自然行障碍。

本文未单独证明：具体 Hauptmodul 的实际有理系数下降、其 holonomic 标量/矩阵系统、Betti/整模型、完整函数独立秩、其它 cusp 分支、CDT conformal map 与严格余量。前几项在上述模型报告另行核验，是否已经完成以该稿的明确证明范围为准；本文不重复署名这些结论。目前尚无严格 holonomy 矛盾，因而没有新的 ζ(7) 无理性定理。若上述七层账本使余量失败，也不能据此宣称所有奇权 modular 路线不可能。

配套 `cdt_odd_period_trigger_20261005_verify.py/json` 只做固定精确恒等式与有界证书：系数配对、critical P 值、全部六个 cusp 常数、L1 的最高多项式系数、Fricke/B/H 代数关系、一个固定 N=30 的 Fourier 内容、五个预定素数的 p+1 packet 以及一个固定整数单位坐标。没有参数扫描，没有数值 ζ(7) 输入，有限检查不替代正文全尺度证明。
