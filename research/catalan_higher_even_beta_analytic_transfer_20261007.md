# Catalan 两分支 Hardy 方法向高偶数 beta 值的解析迁移

日期：2026-10-07。作者：本轮解析分工。状态：纯纸面新稿，已收独立审阅并完成范围修订；未证明任何新的数值无理性。

本稿的直接原件是本地 OpenAI Catalan 论文的 build/sections 中 foundations、real-place、energy、certificate、nonvanishing、conclusion 六个章节。只读取这些文字和已有证书陈述，没有执行原代码、Lean、数值证书、素数表或任何数学 producer；没有修改旧研究稿、guard 或审计。

本轮确实取得两个可以完整核查的结果：固定阶对数权重保留原来所有 Hardy/Cauchy 压缩及实处的二次指数上界；另一个对称的 t 权重准确把起始周期改成 4β(2m)。后者比仅在 s 上加权更接近目标，但尚未完成其余周期的有理投影、有限处预算和非零性桥接。

## 1. 原实际对象和新对象

**A1.** 固定整数 N≥1，保持原文全部参数：

\[
n=48N,\quad a=11N,\quad b=7N,\quad q=g=4N,\quad h=2N,
\quad L=59N,\quad C=63N,\quad H=65N,\quad A=19N.
\]

记 f(t)=√(1−t²)，在 (−1,1) 取正分支，w=t/(1+f)。原行

\[
R_r=(1-t)^ht^{C-1}w^{r-g},\qquad
P_r=(R_r+R_r^*)/2,\qquad D_r=t(R_r^*-R_r)/(2f),\quad 0\le r<n
\]

其中 P_r、D_r 是由整数 Chebyshev 系数构成的实际多项式；R_r 是原代数曲线上的行。多项式的支持和接触为

\[
\operatorname{supp}P_r\subset[A,H-1],\quad
\operatorname{supp}D_r\subset[A+1,H-1],\qquad
tP_r/f-D_r=O(t^L).
\tag{A1}
\]

取 dμ(t)=|t|dt/f(t)，以及 ψ_k(s)=s^{b+k}(1−s)^q。实际行函数

\[
A_r(t)=P_r(t)-\frac32{\bf1}_{t>0}\frac{f(t)}tD_r(t)
\tag{A2}
\]

连续且有界，包括 t=0 处的连续延拓。原矩阵是

\[
F_{rk}=\int_{-1}^{1}\int_0^1
 A_r(t)\frac{\psi_k(s)}{1-ts}\,d\mu(t)\,ds.
\tag{A3}
\]

下文始终同时改变 M 和 Z 的相应积分测度，使 (A2) 的相对系数和真实行不变。只改 M 而继续使用原 Z 会得到另一个对象，不能使用本稿的同对象 Hardy 结论。

**A2.** 对非负可测密度 ρ(t)、v(s)，假定

\[
0<K_t=\int_{-1}^{1}\rho(t)\,d\mu(t)<\infty,\qquad
0<K_s=\int_0^1v(s)\,ds<\infty.
\tag{A4}
\]

定义完整的加权矩阵和行列式

\[
F^{\rho,v}_{rk}=\int\!\!\int A_r(t)\frac{\psi_k(s)}{1-ts}
\rho(t)\,d\mu(t)\,v(s)\,ds,\qquad
\Delta_N^{\rho,v}=\det F^{\rho,v}.
\tag{A5}
\]

密度固定，独立于 N。这里不是将某个新实 Gram 的费用接到旧整基上，而是把同一行、同一列、同一 Cauchy 核的实际所有积分一起改写。

## 2. 完整端点支付和 Hardy 压缩不变

**A3. 绝对可积性。** 对 −1≤t≤1、0<s<1，

\[
0<(1-ts)^{-1}\le(1-s)^{-1}.
\]

因为 q=4N≥1，

\[
\frac{|\psi_k(s)|}{1-ts}\le (1-s)^{q-1}\le1.
\tag{A6}
\]

故 (A5) 的每个矩阵元绝对可积。两次 Andréief 展开的全部有限置换项也绝对可积：每个 s_j 恰出现于一个 Cauchy 因子，且仍带有 (1−s_j)^q，逐项应用 (A6)。行函数在紧区间上有界，剩余测度总质量为 K_t^nK_s^n。这一论证没有遗漏 t=1,s=1 的联合端点，不要求节点相离，也不把密度的点态上确界当作有限量。

**A4. 真实双 Andréief。** 因此

\[
\Delta_N^{\rho,v}=\frac1{(n!)^2}\int
\det[A_r(t_i)]\,\det[(1-t_is_j)^{-1}]\,\det[\psi_k(s_j)]
\prod_i\rho(t_i)d\mu(t_i)\prod_jv(s_j)ds_j.
\tag{A7}
\]

同时保持

\[
\det[(1-t_is_j)^{-1}]
=\frac{V(t)V(s)}{\prod_{i,j}(1-t_is_j)},\qquad
\det[\psi_k(s_j)]=V(s)\prod_js_j^b(1-s_j)^q.
\tag{A8}
\]

我们只对绝对连续测度使用配置公式；重合节点和实际端点是零测度集合。原文的统一估计也允许取其极限。无需为原 Hardy 插值证明新增节点分离假设。

**A5. 两分支对象逐式相同。** 令 x=t/(1+√(1−t²))。原行代数给出的混合行列式仍为

\[
\mathcal R_n(x)=
\det[\xi_{\rm far}(x_i)x_i^{g-r}+\xi_{\rm near}(x_i)x_i^{r-g}],
\tag{A9}
\]

负半轴的两系数为 (1/2,1/2)，正半轴为 (−1/4,5/4)。ρ 和 v 没有进入这个行列式，也没有进入原 Blaschke 插值、多项式反射、Hardy 压缩或 Cauchy 交互核。

原文分两种实际配置：符合

\[
\sum_i\frac{1-x_i^2}{1+x_i^2}\le n-1-2g
\tag{A10}
\]

者使用统一插值，其他配置使用圆周 Vandermonde/Hadamard 后备界。前者的压缩是 L=I+Π_QM_{h_*}R，且 ‖L‖≤1+10e^{12}n；Vandermonde 商恰为 det L，而非评价矩阵逆的范数。后者保留原来的 2^{−binom(n,2)} 主因子。所有这些是节点的代数或点态不等式，所以对 (A7) 原样成立。

**A6. 测度支付定理。** 记原文两种非负 majorant 为 \(\mathcal I_{\kappa,n}\)，κ=2,1。把原证明最后的积分取上确界步骤写成

\[
|\Delta_N^{\rho,v}|
\le \exp(O(n\log(n+2)))\,K_t^nK_s^n
\max_{\kappa=1,2}\sup_{\mathrm{case}\ \kappa}\mathcal I_{\kappa,n}.
\tag{A11}
\]

O 常数来自原 Hardy/后备界及阶乘，不来自新增密度。K_t、K_s 固定，只增加 n log(K_tK_s)，没有新增 n² 费用。特别地，权重在端点可能无界，仍不影响此结论；这是有限测度论证，而非未经证明的密度上确界论证。

## 3. 二次能量与 O(n log n) 的精确含义

**A7.** 原文的完整二次能量保持不变。使用

\[
\alpha=11/48,\quad\beta=7/48,\quad\gamma=1/12,\quad\eta=1/24,
\]

以及

\[
\begin{aligned}
W_\kappa(x)&=(\alpha+2\gamma)\log|x|+2\eta\log(1-x)
-(\kappa/2+\alpha+\eta+\gamma)\log(1+x^2),\\
W_s(s)&=\beta\log s+\gamma\log(1-s),\qquad
D(x)=2\gamma-\frac{2x^2}{1+x^2},
\end{aligned}
\]

每一对固定、实、指数衰减的试验序列 p,v 都给出原来的界

\[
\begin{aligned}
\mathcal E_\kappa={}&(-1+\alpha+\gamma)\log2+
\kappa\|p\|_*^2+\tfrac12\|v\|_*^2\\
&+\sup_x\{W_\kappa+\lambda D-2\kappa T(p,x)-S(v,x)\}
+\sup_s\{W_s+2T(v,s)\},
\end{aligned}
\tag{A12}
\]

其中 κ=2 时 λ=0，κ=1 时 λ≥0。新增密度没有改变两负平方

\[
-\kappa\sum_{k\ge1}A_k^2/k,\qquad
-\tfrac12\sum_{k\ge1}(B_k-2C_k)^2/k.
\]

它也没有改变对角支付 −〈log(1−x)〉/(2n) 和 −〈log(1−s)〉/n，或原点的正系数 19/48、7/48。仍需保留这些支付后才能取全配置上确界。

**A8. 定量版本。** 原能量证明中的 O_ε(1/n) 在本问题可具体控制为

\[
O\!\left(\varepsilon+\frac{1+|\log\varepsilon|}{n}\right).
\tag{A13}
\]

理由如下。核比较项是 O(ε)；x 的余弦对角由 1−(1−ε)² 控制；负 x 的幂对角由 ε 控制；s 的余弦对角由 ε√(1−s) 控制。去掉已显示的端点项以后，所有对角只损失 O((1+|log ε|)/n)。试验序列的三种阻尼切线与原切线的统一差为 O(ε)，其常数由 Σ|p_k|、Σ|v_k| 控制。

余下的一元函数有正的原点系数和至少 1/24 的端点系数，故其最大化点位于独立于 n≥24、0<ε<1/8 的共同紧集；固定比较点 x=−1/2、s=1/2 提供共同有限下界。该紧集上的有限大小系数误差为 O(1/n)。因此允许在全部这些已付款的不等式中选择 ε=1/n，得到

\[
\log|\Delta_N^{\rho,v}|
\le \left(\tfrac12\log2+\max_\kappa\mathcal E_\kappa\right)n^2
+O_{\rho,v,\mathrm{trial},\lambda}(n\log(n+2)).
\tag{A14}
\]

这是从原证明的显式对角界提取出的定量结论；没有在未经统一估计的原始 Fourier 级数中换极限。

**A9. 原证书的解析推论。** 原 certificate 章节的两组试验序列给出的最大界为 −2.290939875。因此对上述固定有限密度，

\[
\boxed{\ 
\log|\Delta_N^{\rho,v}|
\le(\tfrac12\log2-2.290939875)n^2
+O_{\rho,v}(n\log(n+2)).
\ }
\tag{A15}
\]

这里引用已保存的原件试验界，未重新计算其根括区、符号变化表或五十个有理对数区间，也未产生新数值证书。若只采用原 energy 章节而暂不采用其具体数值证书，(A14) 对每一对合法试验序列仍是完整纸面定理。

这个实处结论没有使用 G 或任何高 beta 值有理的假设，也没有给新的有限处下界。

## 4. s 对数权重：完全解析迁移，但目标周期不相同

**A10.** 固定 m≥1，设

\[
\ell=2m-2,\qquad d=\ell+1=2m-1,\qquad
v_m(s)=\frac{(-\log s)^\ell}{\ell!}.
\tag{A16}
\]

令 u=−log s 后，∫v_m(s)ds=∫_0^∞u^\ell e^{-u}du/ℓ!=1，后一个等式由 ℓ 次分部积分得到。因此取 ρ=1,v=v_m 时，K_t=2,K_s=1，直接适用 (A15)。这个权重在 s=0 的无界性已经包含在概率测度中。

**A11. 不应使用的点态断言。** 当 ℓ>0，\(\sum_j\log v_m(s_j)\) 并非对全部配置统一 O_m(n log n)。例如全取 \(s_j=\exp(-\exp(n^2))\)，则此和为 ℓn³−n log(ℓ!)。但原正外场 bΣlog s_j 的负损失更大，且 (A11) 不需对密度取点态上确界。

若坚持把权重放在 Lebesgue 积分的被积函数中，任意固定 δ>0 有

\[
v_m(s)\le C_{\ell,\delta}s^{-\delta},\qquad
C_{\ell,\delta}=\frac{(\ell/(e\delta))^\ell}{\ell!}\quad(\ell>0),
\tag{A17}
\]

ℓ=0 时 C=1。由最大化 u^\ell e^{-δu} 证明。它只把 W_s 中 β 改成 β−δ/n，增加 n log C。n 大时原点系数至少 β/2，其余端点支付不变，故仍有共同紧集。这给出另一份全端点证明，但概率测度法更直接。

**A12. 加权矩的真实系列。**

\[
M_d(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{(j+u+1)^d},\qquad
Z_d(i,j)=\sum_{u\ge0}\frac1{(i+u+1)(j+u+1)^d},
\tag{A18}
\]

其中原 m_{2k}=2/((2k+1)c_k)，c_k=4^{−k}binom(2k,k)，奇数 m 为零。这是同一几何级数和 (A16) 的 Mellin 积分，收敛绝对。

起始周期为

\[
T_d=M_d(0,0)=\sum_{k\ge0}\frac{2}{(2k+1)^{d+1}c_k}.
\tag{A19}
\]

m=1 时 T_1=4G；m≥2 时它不是 4β(2m)。确切的无数值证明是 m_{2k}≤m_0=2，d≥3，于是

\[
T_d\le2+2\sum_{k\ge1}(2k+1)^{-3}
\le2+2\sum_{j\ge3}j^{-3}<2+2\int_2^\infty x^{-3}dx=\frac94.
\tag{A20}
\]

而交错级数给 β(2m)>1−3^{−2m}≥1−1/81，所以 4β(2m)>4(1−1/81)>9/4。只提高 s 分母的阶数没有把原 Catalan 起始周期提高成同族高 beta 周期。

## 5. s 权重的完整有限周期递推与形式整格

**A13.** 记

\[
K_d^-(a)=M_d(a,0),\quad K_d^+(a)=M_d(0,a),\quad
T_d=K_d^-(0)=K_d^+(0),\quad U_d=K_d^+(1).
\]

仍有完整对角递推

\[
M_d(i,j)-M_d(i+1,j+1)=m_i/(j+1)^d.
\tag{A21}
\]

原 d=1 的两边界递推保持其原件形式，起始为 T_1=4G、U_1=3ζ(2)/2、K_1^-(1)=2。对 d≥2、a≥2，新的确切阶梯递推为

\[
\begin{aligned}
aK_d^-(a)-(a-1)K_d^-(a-2)
 &=K_{d-1}^-(a-2)-K_{d-1}^-(a),\\
(a-1)K_d^+(a)-(a-2)K_d^+(a-2)
 &=K_{d-1}^+(a)-K_{d-1}^+(a-2)+\frac2{(a-1)^d},\\
K_d^-(1)&=U_{d-1}-K_{d-1}^-(1).
\end{aligned}
\tag{A22}
\]

**证明。** 原矩递推 (v+1)m_v=v m_{v-2} 给出

\[
a m_{a+u}-(a-1)m_{a+u-2}
=(u+1)(m_{a+u-2}-m_{a+u}).
\]

除以 (u+1)^d 并求和得到第一式。a=1 时 m_{−1}=0，把首项系列向后移一位得到第三式。第二式把 K_d^+(a) 的系列向后移两位；u≥2 的分子是

\[
(a-1)m_{u-2}-(a-2)m_u=(a+u-1)(m_{u-2}-m_u).
\]

保留 u=0 的边界项后，额外常数恰是 2/(a−1)^d。d≥2 的各系列单独收敛，故不需要将两个发散系列相减。d=1 使用原件的有限 telescoping 证明。证毕。

**A14. 完整周期空间。** 对固定 d，全部 M_d(i,j) 属于

\[
\mathscr P_d^M=\operatorname{span}_{\mathbb Q}\{1,T_h,U_h:1\le h\le d\}.
\tag{A23}
\]

证明按 d 归纳：两起始 T_d,U_d 加上 (A22) 生成边界，(A21) 生成全部数组。这里是一个可能有关系的生成系统，不声称这些周期线性无关。

对 Z_d，若 a=i+1、b=j+1、Δ=a−b≠0，部分分式恒等式为

\[
\frac1{(u+a)(u+b)^d}
=\frac{(-1)^d}{\Delta^d(u+a)}
+\sum_{k=1}^{d}\frac{(-1)^{d-k}}{\Delta^{d-k+1}(u+b)^k}.
\tag{A24}
\]

k=1 项与第一项的 ζ(1) 发散准确相消。于是

\[
Z_d(i,j)\in\operatorname{span}_{\mathbb Q}\{1,\zeta(2),\ldots,\zeta(d)\}
\quad(i\ne j),\qquad
Z_d(i,i)=\zeta(d+1)-H_i^{(d+1)}.
\tag{A25}
\]

这些非对角低阶 ζ 项是真实出现的；原接触只已被证明消除原 d=1 的一个 ζ(2) 核，不能直接声称同时消掉 (A23)–(A25) 的全部新周期。

**A15. 一个完整但粗的形式整模型。** 对 0≤i,j<H，令 F=H!。所有这些矩的系数，在

\[
\{1,T_1,\ldots,T_d,U_1,\ldots,U_d,\zeta(2),\ldots,\zeta(d+1)\}
\tag{A26}
\]

这个形式生成系统中，可以取为 F^{−(d+1)}Z。因此同一整数 Chebyshev 行和整数列 filter 收缩后，F^{d+1}F_{rk}^{1,v_m} 是上述周期生成元的整数线性组合。

证明：m_i=2^{i+1}((i/2)!)²/(i+1)!（偶数 i），故 Fm_i∈Z。d=1 的边界逐个除以 a 或 a−1，每条递推链的分母积整除 F；包含 m 项后 F² 付款足够。假设低阶 d−1 的系数由 F^d 清分母，则 (A22) 的强迫项及起始 K_d^−(1) 也由 F^d 清分母，沿 a 的递推再增加一个 F；对角项 m_i/k^d 同样由 F^{d+1} 清分母。Z 的 (A24) 每项系数与有限 harmonic 分母指数合计至多 d+1，所以更精确的 D_H^{d+1} 已足够，也整除 F^{d+1}。这里 D_H=lcm(1,…,H)。证明适用于形式系数，不使用任何周期的有理性或独立性。

因此 F^{(d+1)n}Δ_N^{1,v_m} 是这些周期的一个整数系数多项式，总次数至多 n；把常数 1 也保留为形式变量时可以写成齐次 n 次式，但尚未证明该形式式或真实 determinant 非零。这是一个全有限处形式整模型，但它并没有使 Δ 在 β(2m) 有理的假设下成为有理数。其 factorial 付款规模可达 O_d(n² log n)，不能与 (A15) 构成所需严格比较。

## 6. 2-adic 平滑确实保留了什么

**A16.** 原 rational m_i 系列在 Q_2 中仍可定义

\[
M_{d,\mathrm{s}}(i,j)=\sum_{u\ge0}\frac{m_{i+u}}{(j+u+1)^d}.
\tag{A27}
\]

对于 0≤i,j<H，原 factorial 估计给每个非零项

\[
v_2\ge i+u+1-(d+1)\log_2(H+u)
\ge i-(d+1)\log_2H-C_d,
\tag{A28}
\]

其中 \(C_d=\sup_{u\ge0}((d+1)\log_2(1+u)-u-1)\) 有限。第一表达式趋向 +∞，所以系列收敛；超度量不等式保持此统一下界。

原 Chebyshev 未卷积系数满足 v_2(p_{r,u})≥u−1，乘上实际支持度 C−1−u+v 后，(A28) 给

\[
v_2(M_{d,\mathrm{s}}(P_r,j))\ge
C-(d+1)\log_2H-C'_d.
\tag{A29}
\]

这是同一实际行的强平滑通道，不只是任意矩的粗入口界。

**A17.** (A21)–(A22) 对 Q_2 平滑矩也成立，理由是同样的有限移位以及趋于零的 2-adic 尾。因此可以定义每阶两个起始 discrepancy。但原 d=1 的恰好两 discrepancy、三种列 S/E/B 及其特定 alternation 二次型，并未扩展为同样三列模型。新阶梯递推把低阶 discrepancy 耦合进来；仅 (A29) 不足以证明原 −505/4608 的 determinant 费用对新有理对象成立。

这清楚区分两件事：固定阶 log 权重只在此单项平滑估计增加 O_d(log H)，并不意味着整个有限处 determinant 费用只增加 O_d(n log n)。

## 7. 准确命中高偶数 beta 的 t 权重修复

**A18.** 取

\[
\Lambda(t)=\log\frac{1+t}{1-t},\qquad
\rho_m(t)=
\frac{\Lambda(t)^{2m-2}}{2^{\,2m-2}(2m-1)!},
\quad -1<t<1.
\tag{A30}
\]

偶指数使 ρ_m 为偶、非负密度；m=1 时 ρ_1=1。此时保持 v=1，定义

\[
\begin{aligned}
M^{(m)}(i,j)&=\int_{-1}^1\int_0^1
\rho_m(t)\frac{|t|}{f(t)}\frac{t^is^j}{1-ts}\,ds\,dt,\\
Z^{(m)}(i,j)&=\int_0^1\int_0^1
\rho_m(t)\frac{t^is^j}{1-ts}\,ds\,dt.
\end{aligned}
\tag{A31}
\]

矩阵为 M^{(m)}(P_r,ψ_k)−3Z^{(m)}(D_r,ψ_k)/2，即 (A5)，不是只改首个 moment 的非实际投影。

**A19. 全端点。** t→0 时 Λ(t)=2t+O(t³)，故 ρ_m(t)|t|/f=O_m(|t|^{2m−1})。t→±1 时 ρ_m=O_m((1+|log(1−|t|)|)^{2m−2})，乘 μ 的奇性只有 (1−|t|)^{−1/2}。所以 K_t(m)=∫ρ_m dμ 有限且为正。

甚至未滤波的所有 (A31) 也绝对可积：对 s 先积分至多增加一个端点 log，仍有

\[
\int_0^\epsilon u^{-1/2}(1+|\log u|)^{2m-1}du<\infty.
\]

Z 的端点更弱。故 (A15) 给新的实际加权 determinant

\[
\log|\Delta_N^{\rho_m,1}|
\le(\tfrac12\log2-2.290939875)n^2+O_m(n\log(n+2)).
\tag{A32}
\]

**A20. 真实目标起始。** 同时

\[
\boxed{\ M^{(m)}(0,0)=4\beta(2m).\ }
\tag{A33}
\]

证明：先对 s 积分，再配对 t 和 −t，得到

\[
M^{(m)}(0,0)=\int_0^1\frac{\rho_m(t)\Lambda(t)}{\sqrt{1-t^2}}dt.
\]

设 u=√((1−t)/(1+t))，则 t=(1−u²)/(1+u²)、dt/f=−2du/(1+u²)、Λ(t)=−2log u。因此上式等于

\[
\frac4{(2m-1)!}\int_0^1\frac{(-\log u)^{2m-1}}{1+u^2}\,du
=4\sum_{k\ge0}\frac{(-1)^k}{(2k+1)^{2m}}.
\]

最后等式由有限几何级数及其余项直接积分；或者用 ∑(2k+1)^{−2m}<∞ 的绝对可积级数。于是目标不是猜测，而是这个新实际 M 的精确值。

**A21. 范围边界。** (A32) 和 (A33) 同时成立，是一个真实的解析 carrier 修复。但其余 M^{(m)}、Z^{(m)} 的矩并非原 rational m_i 数组，原 boundary recurrence 和 ζ(2) 的 c-kernel 分解已不适用。整数 P,D/filter 仍在，但这没有证明全部 entry∈Q+Qβ(2m)；也没有证明在 β(2m)∈Q 的假设下整个 determinant∈Q。需要求完整 logarithmic moment 系统以及真正消掉 nuisance periods 的有理行/列投影。

本稿没有把高 beta 的标量正性变成 determinant 非零性。A_r 有符号，两分支系数亦有符号，正测度不产生 Gram 正定性。

## 8. 能保 Cauchy 的独立变量与 confluence

**A22. 正独立变量实现。** 设 d=2m−1，取 d 个独立变量 u_1,…,u_d∈(0,1)，S=∏u_j。对任意绝对可积测试函数 Φ，

\[
\int_{(0,1)^d}\Phi(S)\,du_1\cdots du_d
=\int_0^1\Phi(s)\frac{(-\log s)^{d-1}}{(d-1)!}ds.
\tag{A34}
\]

证明把 −log u_j 的 d 个指数密度卷积，归纳得到 z^{d−1}e^{−z}/(d−1)!，再 s=e^{−z}。因此可将 higher s moment 实现为真正的正多变量积分，核仍为 (1−tS)^{−1}，列仍为 S^{b+k}(1−S)^q。

每个外部列配置使用自己的一组独立 u 变量，并先合并为 S_j，就仍得到精确 V(S) 和同一 Cauchy 行列式。增加积分变量本身没有增加 n² interaction。这是比直接提高 Cauchy 核幂数更可控的实现；周期障碍 (A19)–(A25) 则完全不变。

**A23. 独立列参数 confluence。** 对每列取独立参数 z_k，令

\[
F_{rk}(\mathbf z)=
\int\!\!\int A_r(t)\frac{s^{b+k+z_k}(1-s)^q}{1-ts}\,d\mu(t)\,ds.
\]

这些函数在 Re z_k>−1 的邻近零区域全纯，固定阶导数由可积 log 密度支配。行列式对列的多线性给出

\[
\Delta_N^{1,v_m}
=\left.
\prod_{k=0}^{n-1}\frac{(-\partial_{z_k})^\ell}{\ell!}
\det F(\mathbf z)\right|_{\mathbf z=0}.
\tag{A35}
\]

只有在独立的每列参数上各取 ℓ 阶，才能准确得到目标。对一个共同参数取 ℓn 阶将混入所有阶数分配，并非 (A35)；对共同参数取 ℓ 阶同样不对。

参数未合流前的列行列式一般不再是单个 V(s)。本稿只在各列导数取完、恢复共同 v_m 密度之后使用 (A7)–(A15)，没有在不同列参数的中间对象上套同一 Hardy/energy 界。固定阶导数也会提高 finite-place denominator 的幂数，所以解析压缩不意味着整费用不变。

**A24. 不宜免费使用的另一种微分。** 对辅助核参数 z 求导，

\[
\partial_z^\ell(1-zts)^{-1}
=\ell!(ts)^\ell(1-zts)^{-\ell-1}.
\tag{A36}
\]

这是另一个核。原 n×n Cauchy 行列式 (A8) 已经改变；真正的 confluent Cauchy 通常是扩大的行/列系统，必须支付额外的同点导数和 Vandermonde 交互。仅凭导数阶固定，不能沿用原 n² energy。正 product-variable 方案 (A34) 或直接有限密度方案才保留了本稿已证明的压缩。

## 9. 非零性与全有限处仍需独立桥接

**A25. 原非零证明实际使用的东西。** 原 nonvanishing 章节在 N=p 时以 p² 缩放每个 entry，借 Chebyshev/Frobenius 的两个真实提取 shift，将 48p 矩阵化为

\[
\mathbf a^T\otimes\mathcal B_0+\mathbf b^T\otimes\mathcal B_1,
\qquad \mathbf b=\mathbf a\Pi,
\]

从而其 determinant 由固定的 \(\mathcal B_0,\mathcal B_0+\mathcal B_1,\mathcal B_0-\mathcal B_1\) 决定。原件列出的模 101 pivots 证明的是原 d=1 rational moment 数组。所有高阶 moment 的新 rational parts、discrepancy 系统和局部 extraction 必须先证明，才能定义相应 seed；原三矩阵并不是参数无关的黑箱。

P,D 的整数 Frobenius 多项式身份本身仍成立，这是可以保留的结构。但它不推出 higher s 或 t-log moment 的 p² 系数层恒等式。

**A26. 一项确切的有限处警示。** 对 s-weight 的 Z_d，形式 rational part 在 i=j=p 处为 −H_p^{(d+1)}，所以任意素数 p 都有

\[
v_p(-H_p^{(d+1)})=-(d+1).
\tag{A37}
\]

因为唯一 j=p 项具有该最低 valuation，其他 j<p 都 p-integral。原 d=1 为 −2，d≥3 已至少 −4。因此不能因为 log 权重对实处是有限测度，就断言原 p²-layer 或原有限处 quadratic budget 不变。实际 mixed row 可能有新相消，但相消必须在完整投影后逐项证明；(A37) 不是对最终 mixed determinant 的费用下界。

**A27.** 要用 (A32) 证明 β(2m) 无理，尚需同一新实际对象上三件事：

1. 在仅 β(2m)∈Q 的假设下，使全部 determinant entry 或整个 determinant 确实有理的完整周期投影。
2. 在这个有理整模型上，全素数、全 p-power 的有限处 determinant 预算，其二次常数跨过 (A32) 的费用门槛。
3. 一个无穷尺度的非零性定理，或新完整 extraction 与经验证非零的 seed。不能用“正测度”“原 seed 非零”或泛型权重非零代替。

本稿已完全完成第一个步骤之前的真实解析 carrier 与端点付款。s-weight 提供完整有限形式 period module；t-weight 提供准确 higher beta 的起始周期。两者都尚未完成上述三个算术桥。

## 10. 本轮交付、来源和下一项可检验问题

**A28. 确定的新结论。**

- 原两 branch Hardy/Vandermonde 商、Cauchy determinant、matched damping 与全部对角/端点支付，对固定有限 s 或 t 密度保持，且实际 weighted determinant 满足 (A14)–(A15)。
- s-log 权重增加固定维的有限 boundary-period 阶梯，但其起始并非 4β(2m)；完整递推、形式整格和真实 2-adic 平滑通道由 (A22)–(A29) 给出。
- 对称 t-log 权重 (A30) 同时保持解析指数并精确给 M^{(m)}(0,0)=4β(2m)，所以有一个准确命中目标的具体新 carrier。
- 独立 product variables 和独立列参数 confluence 保 Cauchy 的条件已经明确；提高核幂数不能免费使用原 energy。

最有针对性的后续纸面问题是：为 (A31) 求完整 logarithmic moment 的递推和 period coefficient kernels，并尝试把原高接触 (A1) 升级为消掉所有 nuisance periods 的有理 Hermite/contact 条件。若新整行数量或二次费用因此改变，须同步重做 Hardy/energy 比较，而不能只保留本稿的数值常数。

**A29. 作者证明实际读取域。** 本稿送审前实际全文读取或回读的原件为

E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex；
real-place.tex；energy.tex；certificate.tex；nonvanishing.tex；conclusion.tex。

其中首次批量输出的 energy 中段被工具截断，已单独重新全文读取；没有把截断输出计为全文。本稿送审前的作者证明域没有新增 PDF 页面视觉/文字读取，没有复制前一轮的 25 页读取数，没有全文读取 odd-primes 章节，也没有核算模 101 pivots、四个导数分子、全部 root-count 或 rational-log 数值。涉及这些部分的原证书结论明确按原件陈述引用。送审后的另项同行正式审阅所读原件另记在该独审和最终来源记录中，不混入此作者证明域。

目标积分、阶梯递推、完整形式分母界、(A28)、概率测度付款和定量阻尼付款均是本稿的纸面推导，不是 producer 输出。数学 producer 创建/执行/import/rerun=0；prime/Lean=0；新外部下载=0。旧文件、620 冻结记录及既有审计未修改。
