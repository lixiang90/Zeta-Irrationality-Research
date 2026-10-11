# 第237轮独立纸证：联合整格的 BC 过滤桥与真实算术不变量

2026-10-08，Dual/C。结论有两层：普通 **Taylor 系数** 的完整整值条件足以建立直接 BC 判据，费用上界确为 2κ/m²；但同一个有理 vanishing flag 下，改变有限指数源格的指数与有限处 leading heights 精确抵消。真正需要控制的是实际 pivot 行列式，不能仅以 raw index 变小或变大宣称净收益。没有新的数值无理性结论，数学程序0。

## 1. 同一源、完整截止与 Laurent 识别

实际 FULL 读236最终稿11134 B / b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70及其scope4736 B；采用冻结的同一 rank3 源

\[
f=(1,uE,b_gJ_g),\quad E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
S=\sqrt{1-4u},\quad J_g=S(g-2I),\ I'=E/S,\ I(0)=0.
\tag{G1}
\]

固定 g∈Q，b_g 为固定正整数且 b_gg∈Z。令 L_D=Z[u]≤D³、M=3(D+1)，评价 ψ(P)=ΣP_if_i。其 Q(u)-rank3 与导数闭合是冻结输入；闭合公式为

\[
(uE)'=\frac1{2(1-3u)}+\frac{uE}{2u},\qquad
J_g'=-2(uE)/u-2J_g/(1-4u).
\]

当前 CDT Theorem3.2.8 适用：存在固定 C(g)，全部 M 个不同的 order jumps ν 满足 ν≤3(D+1)+C(g)。取 N=3D+C₀，C₀≥3+C(g)，才保证 T_N 单射且覆盖全部 jumps；没有领取 N=3D+2 精确单射。

以下一般写 rank m、M=m(D+1)。假设 jumps≤m(D+1)+O(1)，则

\[
\sum_{\nu\in V_D}\nu=\frac{m^2}{2}D^2+O(D).
\tag{G2}
\]

因为 M 个不同非负整数在 0,…,M+O(1) 中只漏固定数目，比较 0,…,M−1 即得。令 Γ_D⊂L_D 为满秩子格，T_N(Γ_D)⊂Z^(N+1)，I_D=log[L_D:Γ_D]。

CDT 的 line bundle 是 O(D[0])，基为 1,u⁻¹,…,u⁻ᴰ；我们的正多项式 source 通过 P↦u⁻ᴰP 识别到这个模块。基反序为 Z-模同构，不改变指数；评价变为 u⁻ᴰψ(P)。作为 O(D[0]) 的 section，它的 order 仍是 ν，leading coefficient 仍是 [u^ν]ψ(P)。不能把 Laurent 函数的 ν−D 错当作 filtration index ν，漏掉 D 次 line bundle 权重。

## 2. 逐层饱和与整数 leading，而非整数基高度

置 V_D^n={P∈L_D⊗Q:ord ψ(P)≥n}，Γ_D^n=Γ_D∩V_D^n。每个 Γ_D^n 在 Γ_D 中饱和：若 kP∈V_D^n，则 P∈V_D^n。因此 Γ_D^n/Γ_D^(n+1) 无扭，非零时 rank1；Γ_D 本身不必在 L_D 中饱和。用未取饱和的任意“vanishing generators”作商，不能替代这个格。

对 jump ν，leading map ℓ_ν:P↦[u^ν]ψ(P) 诱导 rank1 商到 Q，image 为 a_Γ,ν Z，a_Γ,ν∈Q× 可取正。完整 Taylor 整值及 ν≤N 给 a_Γ,ν∈Z。以 target Z、∞范数1及标准 p-adic范数定义 quotient evaluation，则

\[
h_p(\psi_\Gamma^{(\nu)})=\log|a_{\Gamma,\nu}|_p
=-v_p(a_{\Gamma,\nu})\log p\le0.
\tag{G3}
\]

这是商范数结论；不要求 CRT 或 Smith 基的 coefficients 小。整数 leading 的绝对值≥1在这里进入 product formula/filtered slopes。若“整数 jets”仅指普通导数 ψ(P)^(n)(0)∈Z，则不够：e^u 的所有导数整，但 [u^n]e^u=1/n!。G3要求 T_N 中采用 Taylor 系数，而非未除 n! 的导数。

## 3. 实际 BC metric：degree、极点和统一误差

固定合法图 φ:(D,0)→(C,0)，明确要求 φ 在闭单位盘的某邻域 holomorphic，φ'(0)≠0，全部 f_i∘φ 在开单位盘 meromorphic。置 λ=log|φ'(0)|，

\[
\mathcal J(r)=\iint_{\mathbb T^2}
\log|\phi(z)-\phi(rw)|\,d\mu(z)d\mu(w).
\tag{G4}
\]

先取缩图 φ_ρ(z)=φ(ρz)，ρ<1。固定 f、g、ρ 时，闭单位盘邻域仅有有限个 pullback poles，可选固定 h_ρ∈C[z]、h_ρ(0)=1 清除全部极点。它与 D、Γ_D、具体 lattice basis 无关；乘 h_ρ 不改 leading coefficient，只贡献固定的 boundary 项。不是把“meromorphic”偷改为“holomorphic”。

用当前 CDT §7.3.1–7.3.3 的固定原图 BC line metric L=O(1)_φ 与固定 smooth probability measure ν₀，给三行 section 空间正交和 L² metric。Hilbert–Samuel (7.3.4)、intersection (7.3.5) 精确给

\[
\widehat{\deg}\overline{\Gamma_D}
=\frac m2\mathcal J(1)D^2-I_D+o(D^2).
\tag{G5}
\]

Γ_D 的所有实向量空间、metric 与 L_D 相同，有限指数改变 covolume 只加 I_D。无需也没有从指数推导低高度整数基。

当前 Lemma7.4.1（r=ρ）及其完整 pole-clearing 证明给

\[
h_\infty(\psi_\Gamma^{(n)})
\le-n\lambda_\rho+D\mathcal J(\rho)+o_\rho(D).
\tag{G6}
\]

同一个 quotient metric 只依实 vanishing 子空间，因此这个估计不依 Γ_D 的 basis。误差依固定 f、φ、ρ，不依 n≤mD+O(1)，故对 M=O(D) 个 jumps 求和仍为 oρ(D²)。最后才令 ρ↑1，直接用原文 Lemma7.4.1 明示的 mixed intersection 极限 J(ρ)→J(1)、λρ→λ；不另假设 shrunk self-energy 连续，也不对 ρ(D) 声称统一误差。对一般没有读过/验证的奇异 boundary metric，不自动领取该极限。

## 4. 已付的直接判据及 2κ/m²

用 CDT Lemma7.2.13，target rank1最大 slope为0。G3–G6给

\[
\frac m2\mathcal J(1)D^2-I_D+o(D^2)
\le-\frac{m^2}{2}\lambda D^2
+m\mathcal J(1)D^2+o(D^2).
\]

若 I_D≤κD²+o(D²)，必要条件为

\[
\boxed{m^2\lambda\le m\mathcal J(1)+2\kappa.}
\tag{G7}
\]

所以严格反向不等式会排除该 rank m 的合法共同源。等价地，若 λ>2κ/m²，则

\[
m\le\frac{\mathcal J(1)}{\lambda-2\kappa/m^2}.
\]

因此 τ_eff=2κ/m² 是**同一 BC source 的合法充分费用上界**，不是将 covolume 直接改名，也不需要原多变量 balanced auxiliary 的小高度桥。它不自动重证原 Lemma6.2.6：该 lemma要求 balanced species、discrepancy support及整数 coefficient exp(εdD)，而 Γ_D 混合 species 后的 tensor restriction 尚无这些性质。这里选择不同的、已在§7公开证明的单变量 filtered route。

对236已付 Γ，κ=45/4、m=3，τ_upper=5/2。这完整安全模型没有改善既有7/3 upper；但不能从这个较差安全 upper 断言最优实际联合费用不能改善。

## 5. 新精确式：指数与有限评价费用抵消

这是同一个 flag、固定 target Z 下的代数恒等式，不以一般 motivic conjecture 为输入。记 L_D^n=L_D∩V_D^n。两个满秩格在同一 rational flag 上的非零 graded image ideals 满足

\[
a_{\Gamma,\nu}=s_\nu a_{L,\nu},\quad s_\nu\in Z_{>0},\qquad
\prod_{\nu\in V_D}s_\nu=[L_D:\Gamma_D].
\tag{G8}
\]

证明：各 L_D^n/L_D^(n+1) 为自由 rank1，逐层选择可提升的生成元，构成 flag-adapted Z 基；同理对 Γ_D。两基之间的整数矩阵为三角矩阵，diagonal绝对值为 s_ν，故 determinant/index 为其乘积。缺失的 jumps 为 rank0，贡献1；不要求标准 monomial 基适配 flag，也不要求 Γ_D⊂L_D 原始。每个 rank1 的 p 商范数取 primitive graded generator，因此

\[
h_p(\psi_\Gamma^{(\nu)})
=h_p(\psi_L^{(\nu)})-v_p(s_\nu)\log p,\qquad
h_\infty(\psi_\Gamma^{(\nu)})=h_\infty(\psi_L^{(\nu)}).
\]

求和得 exact identity

\[
\boxed{\mathcal A_D:=
I_D+\sum_{\nu\in V_D}h_{\rm fin}(\psi_\Gamma^{(\nu)})
=\sum_{\nu\in V_D}h_{\rm fin}(\psi_L^{(\nu)}).}
\tag{G9}
\]

源 degree 下移 I_D，与右边 finite heights 下移 I_D 精确抵消。对每个 D 成立，故允许 D-dependent Γ；固定基、非正态坐标或 skipped jumps 没有例外。若改变 rational source subspace、flag、target integral lattice或∞metric，这个不变量比较须重新建立，不能跨对象套用。

选全部实际 jump rows ν，令

\[
\mathcal T_D=\big([u^\nu](u^kf_i)\big)_
{\nu\in V_D,\ (i,k),\ 1\le i\le m,\ 0\le k\le D}.
\]

它是非零 M×M 有理 square Taylor matrix。上述适配基的 evaluation matrix 为三角，diagonal 为 a_L,ν，基变换 unimodular，所以

\[
\boxed{\mathcal A_D=-\log|\det\mathcal T_D|.}
\tag{G10}
\]

这里有限处 product formula 给 Σ_p log|a_L,ν|_p=−log|a_L,ν|∞。该量可为负，不是总非负“LCD费用”；真实 numerator content 已包括在内。普通整值 Γ 只给 \mathcal A_D≤I_D，因为其 finite sum≤0。丢掉这些可能很负的 heights 才产生 G7 的安全 upper。

最小精确反例：rank1 leading map ℓ(e)=1/p，L=Ze、Γ=pZe。index=p，L finite height=log p，Γ finite height=0，付清总量仍为log p；按指数宣称免费整化是错的。再取 ℓ(e)=p，则 L finite height=−log p，Γ=pZe 的 finite height=−2log p，总量仍为−log p。新格变小/变大不创造真实算术改善；改进的是对 invariant 的可证明 upper。

因此236 window exact rank仍有价值：它能给一个更好的完整 upper与局部结构，却不单独证明 relative κ saving 就是净 holonomy saving。下一步应直接付 G10 的全尺度估计，不能盲目优化 Smith determinant。

## 6. 凸 BC refinement 的准确边界

若使用同一 base BC metric，固定有限半径集 R⊂(0,1]、1∈R，定义

\[
B_R(t)=\min_{r\in R}\{\mathcal J(r)-t\log r\},\qquad
C_R=m\mathcal J(1)-\int_0^m B_R(t)\,dt\ge0.
\]

Lemma7.4.1 加 G2的 jump分布（O(1) holes）给

\[
\liminf_{D\to\infty}\frac{\mathcal A_D}{D^2}
\ge\frac{m^2}2\lambda-\frac m2\mathcal J(1)+C_R.
\tag{G11}
\]

与原文§7.4的 piecewise-slope saving一致。若 limsup \mathcal A_D/D²≤a，严格反向即矛盾；可用 a≤κ 的安全估计。对本源 m=3，真实未付接口为

\[
a<\frac92\lambda-\frac32\mathcal J(1)+C_R.
\tag{G12}
\]

原生基本 r=1 判据里 Jensen给 \mathcal J(1)≥λ，所以 κ<3λ≤3log C* 是用 κ 证明矛盾的必要门槛。它仅约束这个 basic numerator，不是所有 convex BC metric、所有联合多图的全称 cap。G11包含整个 \mathcal J(r) 曲线；仅知道 derivative cap C* 和 \mathcal J(r)≥λ不能删去 C_R。本文没有付任意更优 metric或多图的 universal upper，也没有把 safeκ>3logC*升级为 actual invariant no-go。

## 7. 有界结论与原文采用范围

完整 Taylor jets + 已付 O(1)零估计足以承接直接 filtered BC，而不用补 balanced tensor。Pole clearing、graded saturation、source degree和 quotient∞height 均有明确公式。拟议2κ/9经过纸证成立，限定为此 Γ 的充分 upper。

真正下一道门是同一 g、同一全部跳跃 pivot matrix 的 \mathcal A_D 全尺度主项，并与同一合法图的 basic/convex energy严格比较；不是另构 raw lattice 便领取新的费用，也不是计算有限几阶 pivot 就证明渐近。尚无这个界、严格余量或新的 ζ/L 数值结论。

本稿实际采用当前220页 CDT PDF的完整50–54、95–110，以及完整71–77用于区分辅助多项式路径。没有把目录、关键词locator或其他代理的 primary阅读当全文。95–105中 arithmetic Hilbert–Samuel及BC理论按作者所引定理采用，不宣称独立重证其原始全部 Arakelov理论。具体 source身份与运行账见同轮 dual_reading_scope.md；数学0、扫描0、旧文件修改0。

