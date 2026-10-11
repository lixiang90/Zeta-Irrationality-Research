# level 20 的凸性界：独立 Jensen 下界与精确 Möbius 检验

日期：2026-10-06。本文接续 [level 20 算术账本](cdt_odd_level20_arithmetic_20261006.md) 和 [真实解析叶](cdt_odd_level20_leaf_20261006.md)。目标仍是奇权 ζ/L 的新数值无理性或线性无关性；本文证明的是几种明确 holonomy 公式的限制，不宣称整个 CDT 方法无效。

核心结果：普通 Bost–Charles numerator、CDT §7.1 的合法凸性修正 numerator、§7.6.4 的非负驻点权重 numerator，以及 Theorem 7.1.13 的合法 binomial numerator，都有**各自证明**的下界
\[
\mathcal C_m(\varphi)\ge \rho,\qquad
\rho=\log|\varphi'(0)|.
\]
于是当前 \(K\)-rank \(7\)、成本 \(18/7\) 的表需要平均 \(\rho>3\)，
\(\mathbb Q\)-rank \(10\)、成本 \(279/100\) 的表需要 \(\rho>31/10\)。
若同一合法 holomorphic map 必须省略真 logarithmic cusp \(1\)，并保持
\(\varphi^{-1}(0)=\{0\}\)，Carathéodory 给 \(\rho\le\log16<3\)，这些公式均不能给所需严格矛盾。

该结论不从普通 Jensen 下界直接外推至凸性。下面逐条处理真实修正项。

## 1. 原文与统一记号

原始文献：[CDT, *The linear independence of \(1,\zeta(2),L(2,\chi_{-3})\)*，固定 v2](../literature/cdt2024_l2_chi_minus3.pdf)。相关位置为 PDF/印刷第 89–94 页的 Theorems 7.0.1、7.1.6、7.1.10；第 113–116 页的式 (7.6.2) 与 Theorem 7.6.4。本文已直接读这些完整相关页。

设 \(\varphi(0)=0,\varphi'(0)\ne0\)，并先假定 \(\varphi\) 在闭单位圆盘邻域 holomorphic；对原文允许的径向极限，只要相关 integrals 存在便取极限。若上界为 \(+\infty\)，它当然不能产生严格秩矛盾。
\(\mu\) 是单位圆 Haar 概率测度。记
\[
I(a,b)=\iint_{\mathbb T^2}
\log|\varphi(az)-\varphi(bw)|\,d\mu(z)d\mu(w),\quad0<a,b\le1,
\]
\[
B_0=\int_{\mathbb T}\log|\varphi(w)|\,d\mu(w),\qquad
J=I(1,1),\qquad \widehat T(r)=I(1,r).
\]

原文 Theorem 7.0.1 给 \(m\le J/(\rho-\tau)\)。
它的字面 positivity 条件是 \(\rho>\max(\sigma_m,\tau)\)，但 PDF 第 90 页明确规定：已有 holonomicity 时可放松为 \(\rho>\tau\)。
本项目闭合的真实系统可以使用后者；这里不把 \(\sigma_m=3\) 当成另一条未经区分的排除理由。

## 2. 普通 Jensen 门槛的独立核验

固定 \(w\in\mathbb T\)，对 holomorphic \(z\mapsto\varphi(az)-\varphi(w)\) 用 Jensen：
\[
\int_{\mathbb T}\log|\varphi(az)-\varphi(w)|\,d\mu(z)
\ge\log|\varphi(w)|.
\]
再对 \(w\) 积分，得到对每个 \(0<a\le1\)
\[
\boxed{I(a,1)\ge B_0.} \tag{1}
\]
对 \(\varphi(z)/z\) 再用 Jensen 给
\[
\boxed{B_0\ge\rho.} \tag{2}
\]
边界的孤立零点只引入可积 log 奇点，可用径向极限处理。
若 \(\varphi^{-1}(0)=\{0\}\)，则 \(\varphi(z)/z\) 无零点，\(B_0=\rho\)；额外零点只使 (2) 的下界更强。

所以普通 \(J\ge\rho\)。在 \(\rho>\tau\) 下，要使
\[
\frac{J}{\rho-\tau}<m,
\]
必要条件为
\[
\boxed{\rho>\frac{m}{m-1}\tau.} \tag{3}
\]
这是一个必要门槛，不是充分条件。

## 3. §7.1 的凸性修正仍不低于 \(\rho\)

原文 Lemma 7.1.4 证明 \(\widehat T\) 是 \(\log r\) 的 convex increasing 函数。
取 \(0<r_0<\cdots<r_\ell=1\)，置
\[
\delta_k=\log r_k-\log r_{k-1}>0,\qquad
\alpha_k=\frac{\widehat T(r_k)-\widehat T(r_{k-1})}{\delta_k}.
\]
Theorem 7.1.6 要求最后的 slope \(\alpha_\ell\le m\)。
由凸性，所有 \(0\le\alpha_k\le m\)。修正 numerator 为
\[
\mathcal C_{7.1}=J-\frac1m\sum_{k=1}^{\ell}\alpha_k^2\delta_k.
\]
**直接展开这个修正项**：
\[
\begin{aligned}
\mathcal C_{7.1}
&=\widehat T(r_0)+
  \sum_{k=1}^{\ell}\alpha_k(1-\alpha_k/m)\delta_k\\
&\ge\widehat T(r_0)
\ge B_0
\ge\rho.
\end{aligned} \tag{4}
\]
它允许修正显著降低 \(J\)，却不能在这些 slope 条件下穿过 \(\rho\)。

Theorem 7.1.10 的连续形式同样要求 \(0\le\widehat A(r)\le m\)，并给
\[
\mathcal C_{7.1}^{\rm cont}
=B_0+\int_0^1\widehat A(r)(1-\widehat A(r)/m)\frac{dr}{r}
\ge B_0\ge\rho. \tag{5}
\]
因此 §7.1 两种明确凸性修正保留必要门槛 (3)。
若只选部分 subradii，(4) 仍适用；不需要假定可微性。

## 4. §7.6.4 的非负驻点权重也有直接下界

原文 §7.6 改变 Euclidean metric，令 \(L'=\sum_h s_h L_{r_h}\)，
\(s_h\ge0,\sum_hs_h=1\)。Theorem 7.6.4 进一步要求线性系统 (7.6.5) 有唯一的 nonnegative solution \(s^*\)。
在这个**明确条件**下，原文 numerator 的精确简化形式为
\[
\mathcal C_{7.6}=\sum_{h=0}^{\ell}s_h^* I(r_h,1). \tag{6}
\]
由 (1)–(2)：
\[
\boxed{\mathcal C_{7.6}\ge\sum_hs_h^*B_0=B_0\ge\rho.} \tag{7}
\]
这直接处理了其修正项，不把 \(J\ge\rho\) 当作所有 metric 的自动下界。

所以 Theorem 7.6.4 的非负 stationary-weight 版本也保留门槛 (3)。
原文 Remark 7.6.7 明确说：线性系统在一般情形下是否总给非负解并未知；不能未经证明把这些权重套到任意 map。

对于数域若采用这些 numerator 的逐 embedding 平均，(4)–(7) 逐处成立，所以
\(\overline{\mathcal C}_m\ge\overline\rho\)。本稿没有另证明全部数域版 slopes theorem；它证明的是任何具有该原文 numerator 形式的合法平均版本均受同样门槛限制。

## 5. 当前两张合法预算表的结论

算术成本以 [完整账本](cdt_odd_level20_arithmetic_20261006.md) 的已证表为输入，
不是在本稿重新假设分母可免费下降。

| 明确模型 | \(m\) | \(\tau\) | 必要 \(\rho\)（或平均值） |
|---|---:|---:|---:|
| 单个 \(K\) 模型加已证背景 | 7 | \(18/7\) | \(>3\) |
| \(\mathbb Q\)-trace 联合模型加已证背景 | 10 | \(279/100\) | \(>31/10\) |

真实 cusp \(t=1\) 的 \(\log^3(t-1)\) 项不能用有限 ramification 消去。
因此在目前要求 holomorphic \(\varphi:\mathbb D\to\mathbb C\setminus\{1\}\)、
\(\varphi^{-1}(0)=\{0\}\) 的范围内，原文 PDF 第 24 页的 Carathéodory 定理给
\[
\rho\le\log16<3.
\]
普通 \(J\)、§7.1 离散/连续及 binomial 修正和 §7.6.4 非负驻点权重，均无法在这两张表上给严格秩矛盾。
\(\mathbb Q\)-rank \(10\) 表甚至已满足 \(\log16<279/100\)，连正 denominator 都没有；
\(K\)-rank \(7\) 表允许正 denominator，但完整 numerator 门槛仍失败。

这不排除不同背景、不同真实 period projection、不同返回原点条件或 meromorphic map。
后者需重新计 pole 项及实际 cusp \(\infty\) 的延拓，不在本稿公式范围内。

## 6. 所有 univalent maps 的精确修正量与 Möbius 子类

若 \(\varphi\) 在 \(D\) 上 univalent，实际上有比 Möbius 分解更一般的精确身份。对 \(a<b\)，固定外圆 \(bw\) 后，\(\varphi(az)-\varphi(bw)\) 在 \(|z|<1\) 内无零点，故它的 log Haar 均值恰为 \(\log|\varphi(bw)|\)。又因 \(\varphi(z)/z\) 无零点，对外圆取均值得 \(\rho+\log b\)。\(a=b\) 时用径向极限；交换两变量得到
\[
\boxed{I(a,b)=\rho+\log\max(a,b)\quad\text{(任何 univalent map).}} \tag{8}
\]

置 \(x_h=\log r_h\)、\(S_{k-1}=\sum_{h<k}s_h\)、\(\delta_k=x_k-x_{k-1}\)。对任意非负原始 weights \(\sum_hs_h=1\)，(8) 给
\[
L'\cdot L_1=\rho,\qquad
L'\cdot L'=\rho-\sum_{k=1}^{\ell}S_{k-1}^2\delta_k,
\qquad\beta_k=S_{k-1}.
\]
代入原文未简化的式 (7.6.2)，其除以 \(m\) 后的 numerator 精确为
\[
\boxed{\mathcal C_{7.6}^{\rm raw}
=\rho+(1-1/m)\sum_{k=1}^{\ell}S_{k-1}^2\delta_k\ge\rho
\quad(m>1).} \tag{9}
\]
因此在整个 univalent 类内，即使不用 stationary equations，任意合法非负原始 weights 也不突破下界。\(\widehat T(r)=\rho\)，故 §7.1 全部 slopes 是零。

再对一个具体子类给出纯代数核验：

考虑
\[
\varphi(z)=\frac{cz}{1+bz},\qquad c\ne0,\quad |b|<1.
\]
它是 univalent 的 holomorphic map，\(\varphi'(0)=c\)。直接分解
\[
\varphi(az)-\varphi(dw)
=\frac{c(az-dw)}{(1+baz)(1+bdw)}.
\]
分母的 log Haar 均值为零，且
\(\iint\log|az-dw|=\log\max(a,d)\)，所以
\[
\boxed{I(a,d)=\rho+\log\max(a,d).} \tag{10}
\]
因此 \(\widehat T(r)=\rho\)，§7.1 全部 slopes 是零，修正收益正好为零。

§7.6.4 的方程也可完全解出，而且这个解对所有 univalent maps 都成立：
\[
\frac{I(r_h,r_k)-I(r_h,r_{k-1})}{x_k-x_{k-1}}
=\begin{cases}1,&h<k,\\0,&h\ge k.\end{cases}
\]
所以 stationary equations 变成
\[
(m-1)\sum_{h<k}s_h=0,\qquad\sum_hs_h=1.
\]
对任意 \(m>1\)，唯一解为
\[
s_0=\cdots=s_{\ell-1}=0,\qquad s_\ell=1,\qquad
\mathcal C_{7.6}=\rho.
\]
这里没有浮点积分或参数扫描。

若 Möbius map 还省略 \(1\)，方程 \(\varphi(z)=1\) 的解为
\(z=1/(c-b)\)；故 \(|c-b|\le1\)。与 \(|b|<1\) 合并给
\[
|c|<2,\qquad \rho<\log2.
\]
所以这整个 holomorphic Möbius 类在当前成本下都没有足够的 derivative；
不能靠改变两子半径 metric 救活。

真实叶报告中的合法共同 map
\[
\varphi(z)=\frac{4209z}{4120+3200z}
\]
属于该类，\(c=4209/4120,b=80/103\)，
且 \(c-b=1009/4120<1\)。因此它的三种 numerator 都精确等于
\(\log(4209/4120)\)。这验证它是完整合法解析输入，却无法达到算术门槛。

## 7. Binomial 度量的 rank-one 对照下界

Theorem 7.1.13 的 binomial 公式虽然不是双圆积分，也能证明独立下界。用 \(p>1\) 表示原文 metric 的参数 \(r\)，避免与 subradius 混淆；令
\[
u=\log R,\quad d=\rho-u>0,\quad
x=\chi_0\in[0,1),\quad q=\chi_1\in[x,m].
\]
Theorem 要求 \(\mu\le u<\rho\)，且 \(x<1\)。由原定义
\[
u-\mu=\lambda p x^{p-1},\qquad
\Gamma(u)=\lambda(p-1)x^p,\qquad
T=\Gamma(u)+qd.
\]
其式 (7.1.14) 的完整 numerator 代数化为
\[
\mathcal C_m=\rho+\lambda A_m(x)+d(2q-q^2/m-1),
\]
\[
A_m(x)=\frac2{p+1}-p x^{p-1}
 +2(p-1)x^p-\frac{p(p-1)}{m(p+1)}x^{p+1}. \tag{11}
\]
由于
\[
A_1(1)=0,\qquad A_1'(x)=-p(p-1)x^{p-2}(1-x)^2\le0,
\]
所以 \(A_m\ge A_1\ge0\)（\(m\ge1\)）。若 \(q\ge1\)，则 \(q\le m\) 给 \(2q-q^2/m\ge q\ge1\)，立即得到 \(\mathcal C_m\ge\rho\)。

若 \(q\le1\)，同一 map、同一 \(R,p,\lambda,\mu\) 满足该 theorem 在 \(m=1\) 下的全部特殊条件。现在**另行应用 CDT theorem**，以实际常数函数 \(f_1=1\)、全零分母列和 \(e=0\) 为输入。原文 Theorem 6.0.2 明确允许 \(m\in\mathbb N_{>0}\)，该函数的 \(\sigma_1=\tau=0\)，处处 meromorphic、holonomic，并有任意大 convergence radius。只需 \(\rho>0\)，便满足 Theorem 7.0.1 的严格 positivity。故原 theorem 本身给
\[
1\le\frac{\mathcal C_1}{\rho},\qquad\mathcal C_1\ge\rho.
\]
直接比较分子又有
\[
\mathcal C_m-\mathcal C_1=(1-1/m)
 \left[q^2d+\frac{\lambda p(p-1)}{p+1}x^{p+1}\right]\ge0. \tag{12}
\]
这完成 \(q\le1,\rho>0\) 情形。还可以去掉 \(\rho>0\)：仅为证明 analytic lemma，取辅助缩放
\[
\widetilde\varphi=e^v\varphi,\quad
\widetilde R=e^vR,\quad\widetilde\mu=\mu+v.
\]
\(\Gamma,T,d,x,q\) 不变，\(\widetilde\rho=\rho+v\)，\(\widetilde{\mathcal C}_m=\mathcal C_m+v\)。选 \(v\) 使 \(\widetilde\rho>0\) 并应用已证结果，得 \(\mathcal C_m\ge\rho\)。这不是把实际目标 map 的 cusp 几何免费缩放；辅助函数仍只有常数 \(1\)，它没有避点要求。因此所有合法 binomial 参数都满足
\[
\boxed{\mathcal C_m\ge\rho.} \tag{13}
\]
这不是从普通 Jensen 的修正项猜测，而是 binomial 代数与 CDT 的 rank-one consistency consequence。原 theorem 不要求 \(\varphi^{-1}(0)=\{0\}\)；该条件另用于本模型的 Carathéodory 上界。闭盘邻域的 regularity 若需要，可先用 \(\varphi(rz)\)、\(r<1\)；每个实际用于秩矛盾的 map 必须满足相应原文条件。本项目任何正 denominator 都有 \(\rho>\tau\ge0\)，所以 (13) 覆盖实际所需范围。

同一对照还处理了 raw (7.6.2) 的一部分 nonunivalent 情形。固定同一非负 weights，其 numerator 为
\[
\mathcal C_m^{\rm raw}=2L'\cdot L_1-L'\cdot L'
 -\frac1m\sum_k\beta_k^2\delta_k.
\]
如果 \(\beta_\ell\le1\)，则该 raw proof 在 \(m=1,f_1=1,\tau=0\) 下也合法，给 \(\mathcal C_1^{\rm raw}\ge\rho\)。\(\rho\le0\) 时同样先用辅助缩放 \(\widetilde\varphi=e^v\varphi\)：每个 intersection 增加 \(v\)、\(\beta_k\) 不变，所以 \(\widetilde{\mathcal C}_1^{\rm raw}=\mathcal C_1^{\rm raw}+v\)。因
\[
\mathcal C_m^{\rm raw}-\mathcal C_1^{\rm raw}
=(1-1/m)\sum_k\beta_k^2\delta_k\ge0,
\]
所以 \(\beta_\ell\le1\) 时，无论 map 是否 univalent 都有相同下界。一般 \(1<\beta_\ell\le m\) 的 raw weights 不由这个对照排除。这些独立下界现在可对任意 embedding 逐处应用并取平均；仍未据此声称已另证明全数域版 holonomy theorem。

## 8. 明确保留的开放范围

本文**没有**证明任意 nonunivalent map 上的式 (7.6.2) weights 的原始未简化 numerator 都不低于 \(\rho\)；§6 已另证全部 univalent maps 的 raw weights 下界。
(7) 使用的是 Theorem 7.6.4 的 stationary equations 与非负性。
§7 又处理了 \(\beta_\ell\le1\) 的 nonunivalent raw weights 和合法 binomial metrics。尚未对 \(\beta_\ell>1\) 的一般非驻点 raw weights、不同 maps 的一般混合、或所有 possible Hermitian metrics 建立普遍 lower bound。普通 Jensen 排除不能替代这些缺失证明。

因此新的可能性需要一个具体输入：证明某种未覆盖 metric 的 numerator 可突破当前必要门槛，或改变同一真实函数系统的算术成本/返回几何。上述明确凸性公式和全部 Möbius 测试无法提供这种改进；不把这个限定结论改写成“更深数学也不可能”。

## 9. 精确证书的范围

[脚本](cdt_odd_level20_convexity_20261006_verify.py) 核查修正项的代数恒等式、两张必要门槛、指数下界、Möbius 分解、所有固定 subradius stationary 矩阵，以及已用共同 map 的精确参数。
证明 (1)–(13) 的依据是 Jensen、convexity、binomial 代数和原文 theorem 的实际 rank-one 输入；证书不以有限试验认证一般解析不等式，也不验证未纳入的多 metric 方案。

独立审阅范围：`helper_tensor_budget` 重新核对 §§2–6 的 Jensen、§7.1 telescope、§7.6.4 驻点原式和 univalent raw 身份，均通过。根分支直接重读固定 v2 的 pp92–94、114–116，复核 §7 的 binomial rank-one 所有特殊条件、辅助缩放、\(A_1\) 导数、两种 rank-one numerator 差及 raw \(\beta_\ell\le1\) 的条件，均通过。审阅没有把 \(\beta_\ell>1\) 的一般非驻点 raw weights 或多 map 情形列入结论。本稿和对应证书于这次审阅后冻结，不宣称 Lean 形式化证明或新数值无理性定理。
