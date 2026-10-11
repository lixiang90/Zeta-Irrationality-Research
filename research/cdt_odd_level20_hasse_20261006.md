# level 20 的 Hasse 适配微分关系与最高分母层整格

日期：2026-10-06。本稿继续研究 L(3,χ₅) 的真实 rank4 系统。新结果是一个对所有合适素数成立的 Hasse 关系，以及有限前缀的局部整格指数界。它不把固定换基的三层下界推广到随 p 改变的整格，也不把局部改进直接记成 CDT 的新 τ。仍未得到新的数值无理性定理。

## 1. 输入、规范和这次改变的对象

使用 [完整 level20 模型](cdt_odd_level20_model_20261006.md)、[真实叶](cdt_odd_level20_leaf_20261006.md) 和 [算术账本](cdt_odd_level20_arithmetic_20261006.md)。令 K=Q(r)、r²=5，c=L(3,χ₅)，反证假设 c∈Q。以下只排除固定整数规范、c 的分母以及 2、3、5 所涉及的有限素数。取 p≥7，及 K 中 p 上的任一素理想 𝔭；k=O_K/𝔭 的大小是 p^f。

θ_q=q d/dq；本稿的 ϑ=t d/dt 是另一算子，不能混用。实际函数为

\[
H_-=A_-(f_- -\Theta),\qquad
H_+=A_+(f_+ +\Theta),\qquad \Theta=-5rc/16.
\]

其中 f_±=u∓rv，u、v 的 q⁰ 项为零，且 θ_q³ f_±=V_±。
E₂−4rF₂(4τ)=A_-，A_+ 为明确系数共轭。E₂ 的常数项是 −1/5。
令

\[
B=\eta(2\tau)^2\eta(10\tau)^2,
\quad N_-=1-(6+r)t+(1+r)t^2,
\quad C_-=1-(6-2r)t+(6-2r)t^2,
\]

并将 r 换成 −r 定义 N_+、C_+。完整模型已证明

\[
\left(\frac{A_\pm}{B}\right)^2
=\frac{N_\pm^2 C_\pm}{25t^2(1-t)^2}.                 \tag{1}
\]

下述算子随 p 改变，次数约为 p；它们不是新增的固定低秩辅助函数。旧稿“固定 Q(t)/K(t) mixed 行保留三层”与本稿没有矛盾。

## 2. Hasse 商确实在同一个 t 上下降

记 E_{p−1}^{std} 为常数项 1 的 level1 Eisenstein 系列。von Staudt–Clausen 给非恒定 Fourier 系数 p-integral 且被 p 整除，因此其 mod p q-expansion 是 1。它的 reduction 是 Hasse 不变量。原始来源是 [Katz §2.0–2.1](../literature/katz1973_padic_modular_forms.pdf)，simple-zero 输入在该书 §4.3；后者只在证书识别平方自由部分时需要，下面一般的 radical 次数上界只需要平方在非分歧处具有偶数重数。

在 X₀(20) 的好约化上定义

\[
\mathcal H_p=\frac{(E_{p-1}^{std})^2}{B^{p-1}}.
\]

它权为 0。Fricke 变换给 B(−1/(20τ))=−20τ²B(τ)，而 E_{p−1}^{std}(−1/(20τ))=(20τ)^{p−1}E_{p−1}^{std}(20τ)。二者的商在 W₂₀ 下的比例是 20^{p−1}；mod p 后该比例为 1，并且 E_{p−1}^{std}(20τ)≡E_{p−1}^{std}(τ)≡1。q-expansion principle 因而给真正的 W₂₀ 不变性，不只是某个有限 jet 的偶然相等。

所以 𝓗_p∈k(t)，下降到原稿的 genus0 商。X₀(20) 在 p∤20 时好约化，W₂₀ 为 tame 二阶商；原稿 quartic Δ 的判别式只有 2、5 的素因子。六个 cusp 被配成 t=0、1、∞，商在 cusp 未分歧，B 在每个原 cusp 恰有一阶零，Hasse 在 cusp 不为零。因此三个商 cusp 的 pole 均恰为 p−1：

\[
\boxed{\mathcal H_p(t)=
 \frac{P_p(t)}{[t(1-t)]^{p-1}},\quad
 P_p(0)=1,\quad\deg P_p=3(p-1).}                    \tag{2}
\]

在四个 Fricke branch 以外，P_p 的每个根重数至少为2；branch 至多贡献四个奇数重数根。设 Q_p=rad(P_p)，便有

\[
\boxed{\deg Q_p\le(3p+1)/2.}                        \tag{3}
\]

Hasse 在原 modular curve 上的简单零还说明 P_p 的实际重数只可能为1或2。这使配套脚本可用 polynomial gcd 而无需任何浮点根近似。

## 3. 低次数的 prime-dependent 一阶算子

由 mod p E_{p−1}^{std}≡1，式(2)的 q-expansion 是 B^{1−p}，所以在 k((t)) 中

\[
B'/B=\mathcal H_p'/\mathcal H_p
 =P_p'/P_p+1/t-1/(1-t).
\]

对(1)取对数微分，两个 cusp 项恰抵消，得到

\[
\boxed{A_\pm'/A_\pm
 =N_\pm'/N_\pm+\tfrac12 C_\pm'/C_\pm+P_p'/P_p
 \quad\text{mod }\mathfrak p.}                      \tag{4}
\]

令 V_p=Q_p P_p'/P_p∈k[t]。取

\[
D_{p,\pm}=N_\pm C_\pm Q_p,
\]
\[
M_{p,\pm}=t\left(N_\pm'C_\pm Q_p+
 \tfrac12N_\pm C_\pm'Q_p+N_\pm C_\pm V_p\right).
\]

式(4)给

\[
\boxed{\mathscr D_{p,\pm}=D_{p,\pm}\,\vartheta-M_{p,\pm},
\qquad \mathscr D_{p,\pm}A_\pm=0\quad\text{mod }\mathfrak p.} \tag{5}
\]

两条多项式的次数均不超过

\[
\delta_p=\deg D_{p,\pm}\le(3p+9)/2.
\]

固定因子或 gcd 可以进一步降低次数，本稿无需它。这里 ϑ 是 Euler t 算子，所以 ϑD、ϑM 不增加次数。
在三元组 (H,ϑH,ϑ²H) 中，两条算子对应

\[
v_0=(-M,D,0),\qquad
v_1=(-\vartheta M,\vartheta D-M,D).                   \tag{6}
\]

它们在 k[t] 上独立：v₁ 的第三坐标是非零 D，而 v₀ 的第三坐标为0。
这不是特征零下的实际函数关系；原实际 rank4 的不可约商仍为 rank3。

## 4. 完整最高 packet，而非单个 p+1 系数

源 u 来自 E₄ 的 oldform 组合，v 来自 F₄ 的 oldform 组合。对 p∤10、1≤j<p，divisor sum 中包含 p 的项具有 d³ 因子，故

\[
[q^{pj}]\theta_q^3 u\equiv[q^j]\theta_q^3u,
\qquad [q^{pj}]\theta_q^3v\equiv\chi_5(p)[q^j]\theta_q^3v\pmod p.
\]

指数 pj<p² 时最多有一层 p，所以乘 p³ 后所有源系数都是 𝔭-integral；指数不被 p 整除的项 reduction 为0。
记 F_{p,\pm}(z) 为将 (u∓rχ₅(p)v)∘q(z) 截断到 z-degree<p 后的 reduction。该有限截断是 p-integral，不能将含 p-denominator 的整个 f_± 直接 reduction。整数 q↔t 坐标给 q(t)^p≡q(t^p)，于是

\[
\boxed{p^3H_\pm(t)
 \equiv A_\pm(t)F_{p,\pm}(t^p)
 \pmod{\mathfrak p,\ t^{p^2}}.}                      \tag{7}
\]

假定有理的周期常数在乘 p³ 后 reduction 为0；没有假设未知周期存在 Galois 作用。
因 ϑF(t^p)=0，(5)真正消掉整个最高 packet：

\[
p^3\mathscr D_{p,\pm}H_\pm\equiv0,
\qquad p^3\vartheta\mathscr D_{p,\pm}H_\pm\equiv0
\pmod{\mathfrak p,\ t^{p^2}}.                        \tag{8}
\]

因此这些前缀的 coefficient valuation 从至少 −3 提升到至少 −2。
本稿没有证明第二、第三层也同时取消，也没有把 (8) 扩为 mod p³ 的关系。

### 4.1. 源 packet 的模 p³ 加强与精确 Frobenius lift

源 packet 本身可加强到模𝔭³；它与算子(8)的消层强度不同。对 j<p，E₄ 的 divisor sum 给 a_{pj}≡a_j modp³，F₄ 给 b_{pj}≡χ₅(p)b_j modp³。各 oldform 的尺度只含2、4，故对好 p 保持这两个同余。指数不被 p 整除时，p³ θ_q^{-3} 的系数在𝔭³中；指数为 pj 时只需除 j³，仍是𝔭-unit。

令 \(\widetilde F_{p,\pm}(s)\) 为 \((u\mp r\chi_5(p)v)\circ q(s)\) 的 degree<p 实际截断，其系数在 O_{K,𝔭}。取精确整数坐标 lift
\[
t_p^{\mathrm{Fr}}(t)=t\big(q(t)^p\big)\in\mathbf Z[[t]],
\qquad\operatorname{ord}_t t_p^{\mathrm{Fr}}=p.
\]
整数反演的真实恒等式是 q(t_p^{Fr}(t))=q(t)^p，不能在模p³中把它换成 q(tᵖ)。因而
\[
\boxed{p^3H_\pm(t)\equiv
A_\pm(t)\widetilde F_{p,\pm}\big(t_p^{\mathrm{Fr}}(t)\big)
\pmod{\mathfrak p^3,t^{p^2}}.}\tag{8a}
\]
假设有理的周期常数在好𝔭处整，所以乘p³后在𝔭³中。截断外的 s^p 项经 lift 后从 t^{p²} 开始，不影响任何保留系数。

式(8a)是全前缀源项的加强，不会自动把原 Hasse 算子升级到模p²或p³：\(\vartheta t_p^{Fr}\) 通常只被p整除。后续须结合 excellent Frobenius quotient 与适配 connection 才能获得更多算子消层；它们另稿证明。

## 5. 一个可 CRT 拼接的局部整格界

固定 𝔭、D≥0、p<N<p²。令 E_D=O_{K,𝔭}[t]_{≤D}^{⊕3}，考虑线性映射

\[
M_{p,D,N}:(k[t]_{\le D})^3\longrightarrow k[t]/(t^N),
\quad (P_0,P_1,P_2)\mapsto
p^3(P_0H+P_1\vartheta H+P_2\vartheta^2H)\bmod\mathfrak p.
\]

设它的秩为 r_{p,D,N}。它的 kernel 的逆像 Λ_{𝔭,D,N} 正是使该三元组组合在前 N 项仅需 p² 清除的格。
因 pE_D⊂Λ⊂E_D，有精确公式

\[
\boxed{[E_D:\Lambda_{\mathfrak p,D,N}]
 =\operatorname{Norm}(\mathfrak p)^{r_{p,D,N}}.}        \tag{9}
\]

式(7)的最高 packet 从 t^p 开始，给 r≤N−p。
由(4)，ϑA/A 是分母 D、分子次数≤δ 的有理函数；ϑ²A/A 具有分母 D²、分子次数≤2δ。因此整个三元组组合的 rational numerator 次数≤D+2δ，给 r≤D+2δ+1。
特别在 D≥δ 时，(6)及各自次数≤D−δ 的 polynomial multiples 显式给至少 2(D−δ+1) 个独立 kernel 方向。总之

\[
\boxed{r_{p,D,N}\le
 \min\{3(D+1),\ N-p,\ D+2\delta_p+1\}.}              \tag{10}
\]

与最粗的 pE_D 相比，局部指数可节省至少 2(D−δ+1) 个 Norm(𝔭) 因子（D≥δ）。有限多个 𝔭 的这些条件可通过 CRT 同时定义一个真实 O_K 子格；不同素理想的指数相乘。
这证明“随 p 改变的换基”确有可用的整格信息，而非把两个形式方向免费加入函数数目。

## 6. 如何继续接到 CDT，以及尚未跨越的步骤

目前原文的 τ 来自 balanced d-variable tensor evaluation、高阶 Taylor 过滤、全部 n/p valuations 与 Hilbert–Samuel/斜率估计。式(9)只是一个有限一变量 coefficient lattice 的准确指数。
后续 [一变量全局稿](cdt_odd_level20_hasse_global_20261006.md) 已用实际 closed system 的 Shidlovsky 消失阶界与固定原格的 Smith determinant 补齐第1项，并在明确的 rank4/rank7 一变量源格上给出新的特殊全局界。局部指数本身仍不能直接当收益：换格与 source degree 的变化精确抵消。尚未建立 balanced tensor 版本；更一般的后续仍需处理：

1. 在同一原点 Taylor filtration 上，适配子格的 determinant 与分次评价高度如何共同变化；不能只减非arch高度、漏掉源格 degree。
2. p²、p¹ 两个剩余层、p≤√N 的高幂层及固定坏素数的完整贡献。
3. 与 CDT 的 balanced tensor species 和 uniform exponent 分布兼容的体积估计，以及 primitive saturation 或更小 μ-basis 的可能额外收益。
4. 在同一实际共同覆盖上得到新 τ 与解析 numerator 的严格最终不等式。

本稿提供真实局部输入；一变量的特殊全局界已另稿证明，但其收益仍不足以产生数值矛盾。没有将新的局部 index 直接代入 balanced tensor 的旧 τ 公式。
可读的原始路线来源为 [Beukers 的 modular supercongruences](../literature/beukers2025_supercongruences_modular_v3.pdf)、[Beukers–Tsai–Ye 的 Lucas congruences](../literature/beukers_tsai_ye2024_lucas_modular_v2.pdf) 和 [Katz 的周期微分方程/Frobenius](../literature/katz1968_period_matrices.pdf)。本稿式(2)–(10)的具体 level20 推导如上，不将一般文献的超同余结论直接套成未知 c 的数值结论。

## 7. 证书与审阅范围

[精确脚本](cdt_odd_level20_hasse_20261006_verify.py) 只取预先固定 p=7、11、13。
在每个 p 完整计算所有指数 n<p² 的 t/q 反演、E/F packets、两个 embedding 的 polynomial Hasse 算子及最高层消除。
P_p 的次数及 radical 次数分别为 (18,9)、(30,17)、(36,20)；两个算子的次数分别为13、21、24。
有限核验用于发现规范或截断错误；全素数结论的依据是 §§2–5 的几何、divisor sum 与线性代数证明。

固定执行原有79项检查，并在4.1的源 packet 加强后加入6项模p³检查，总计85项。原有限格样本为：p7 的 coefficient degree15、ambient48、实际rank40；p11 的degree23、ambient72、实际rank57（两个split residues均检查）；p13 的degree26、ambient81、实际rank67。它们用于核对局部关系，不能替代全尺度消失阶或全局高度证明。

helper_tensor_budget 与 low_period_closure 已分别按实际正文独立重推 Hasse 的 W 下降、cusp 除子、radical bound、式(4)的 cusp 抵消、全部 n<p² 的 packet 及局部格指数接口；[书面独立审阅](cdt_odd_level20_hasse_review_20261006.md) 已保存。新的全局一变量界及其独立审核见 [全局稿](cdt_odd_level20_hasse_global_20261006.md) 与 [Smith 审阅](cdt_odd_level20_hasse_smith_audit_20261006.md)。4.1的模p³加强由上面的divisor-sum证明及固定精确执行核对。
