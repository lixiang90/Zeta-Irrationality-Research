# Catalan 全部偶阶边界周期与参数函数的真实结构

2026-10-07。原 Catalan 行列池的二阶边界障碍可以统一到每个偶阶，而不是逐个阶数重新试验。边界值有一个正测度表示，归一化后的全部偶阶值组成严格正定的 Hankel 矩系统；同一参数函数则在所有正奇整数处有真实双极点。这些结果决定了当前构造应先处理实际周期关系，再谈整列投影与 CDT 函数秩。它们没有证明数值无理性或线性无关性。

## 1. 同一个实际边界函数

沿用 [完整参数模型](cdt_catalan_higher_jet_holonomy_bridge_20261007.md) H2、H13、H14 和 [二阶原列池](cdt_catalan_jet_pool_projection_rank_20261007.md) P1–P9d。参数是实际积分中的 z，空间变量仍另记 x 或 t。令

\[
U(z)=M_z(0,1),\qquad V(z)=Z_z(0,0),\qquad
\mathcal K(u)=\frac{(2\cosh u-3/2)\log\cosh u-(3/2)u}{\sinh(2u)}.
\tag{A1}
\]

在 |Re z|<1 内，直接积分 s 并配对 ±t 给

\[
\frac{U(z)+U(-z)}2-\frac34\bigl(V(z)+V(-z)\bigr)
=2\int_0^\infty\mathcal K(u)\cosh(zu)\,du=:F(z).
\tag{A2}
\]

这是原真实 seed 的组合，没有引入新的形式周期。P9a 的两个积分可独立检查 A2：U 的 sinh 项在偶化中消失，V 的 exp 项变成 cosh。

零阶身份 U(0)=π²/4、V(0)=ζ(2) 给 ∫K=0。又 K 在唯一 u₀>0 前为负、其后为正：

\[
R(u)=(2\cosh u-3/2)\frac{\log\cosh u}{u}
\tag{A3}
\]

严格从0增长到∞，因为两因子均为正且严格递增，第二因子导数的分子 u tanh u−log cosh u 的导数是 u sech²u>0。K 在0有限，在∞为 O((1+u)e^{-u})，故以下所有固定阶矩绝对收敛。

## 2. 全部偶阶均为正与正测度模型

对偶数 ℓ≥2，定义同样的 Hasse 归一化

\[
\Omega_\ell=\frac{[z^\ell]U-(3/2)[z^\ell]V}{\ell+1}
=\frac{2}{(\ell+1)!}\int_0^\infty u^\ell\mathcal K(u)\,du.
\tag{A4}
\]

ℓ=2 时这就是上一稿 Ω。由 ∫K=0，

\[
\int_0^\infty u^\ell K(u)du
=\int_0^\infty(u^\ell-u_0^\ell)K(u)du>0.
\tag{A5}
\]

因此 **所有 ℓ≥2 的偶阶 Ωℓ 都严格为正**。这里的正性没有推出 Ωℓ 与 β(ℓ+2) 或其他 seed 数值独立。

置真实尾函数

\[
H(u)=\int_u^\infty K(v)dv.
\tag{A6}
\]

对 u≥u₀，H 是非空正尾；对 0<u<u₀，H(u)=−∫₀ᵘK(v)dv>0。因此 H 在整个正轴严格正，H(0)=0，且 H(u)=O((1+u)e^{-u})。分部积分及 t=u² 给

\[
b_m:=\frac{(2m+3)!}{2m+2}\Omega_{2m+2}
=\int_0^\infty t^m H(\sqrt t)dt,\qquad m\ge0.
\tag{A7}
\]

两端积分边界确为零；在∞指数衰减，在0有 H(u)=O(u)。故对任意 d≥1 和非零实多项式 P，有

\[
\sum_{i,j=0}^{d-1}p_i p_j b_{i+j}
=\int_0^\infty P(t)^2H(\sqrt t)dt>0.
\tag{A8}
\]

所有 Hankel 矩阵 (bᵢ₊ⱼ) 和移位矩阵 (bᵢ₊ⱼ₊₁) 都严格正定，特别 bₘbₘ₊₂>bₘ₊₁²。它们的严格满秩来自一个实际正测度，不来自猜测周期基。

这排除归一化序列 bₘ 最终满足任何非零常系数线性递推：若阶 d 递推在 m≥M 成立，取关系系数的多项式 P，再把其中 d+1 个相继关系乘相应系数求和，将得到 ∫tᴹP(t)²H(√t)dt=0，矛盾。复系数关系先取非零的实部或虚部即可。它不排除变系数递推，更不推出各个 bₘ 的有理线性无关性。

## 3. 最高周期系数与原列池的统一核

固定原参数 n=48N、b=7N、q=g=4N、h=2N、L=59N、C=63N、A=19N；行 Pᵣ,Dᵣ 与 contact tPᵣ/f−Dᵣ=O(tᴸ) 都保持原定义。对任一固定偶 ℓ≥2，在有限 jet 的已认证 seed 表示中，最高 [z^ℓ]U 和 [z^ℓ]V 只能按零阶齐次部分传播，因为 H13/H14 每个 zK 项都降一阶 seed。这给

\[
\operatorname{coeff}_{[z^\ell]U/(\ell+1)}M^{(\ell)}(i,j)
=c_{(j-i-1)/2},\qquad
\operatorname{coeff}_{[z^\ell]V/(\ell+1)}Z^{(\ell)}(i,j)=[i=j].
\tag{A9}
\]

这里 M^(ℓ)=[z^ℓ]M_z/(ℓ+1)，同样定义 Z，cₖ=4⁻ᵏbinom(2k,k)，不合法下标取零。外矩及 diagonal tail 没有这两个 seed。contact 因此把整个 mixed raw pool 的两个最高 seed 项准确合并为

\[
\Omega_\ell\mathcal D_N,\qquad
(\mathcal D_N)_{r,j}=[t^j]D_r,\quad b\le j<L.
\tag{A10}
\]

这就是同一整数矩阵，与 ℓ 无关。为明确秩证明，正侧 r=g+d 中 Dᵣ 的最低项为 2^(d−1)t^(C−d)。取 d=g+1,…,44N−1，最低次数恰遍历 L−1,…,A+1，形成可逆三角高列块；所有低列 b,…,A 均为零。因此

\[
\operatorname{rank}\mathcal D_N=40N-1,\quad
\ker_\mathbb Z\mathcal D_N=\bigoplus_{j=b}^A\mathbb Zs^j.
\tag{A11}
\]

原 endpoint 空间 W=sᵇ(1−s)^qQ[s]₍<48N₎ 与该核相交，等价于 deg Q≤A−b−q=8N；primitive 整基仍是 s^(b+k)(1−s)^q，0≤k≤8N，高度 ∥·∥₁=2^(4N)。故在 **把各 seed 暂作为自由生成元的认证模型** 中，每个高偶阶都只留下8N+1个允许方向，不能保持原48N阶 determinant。

A4/A5 证明最高边界值确实不为零，但不是它不能与其他周期合并的证明。追加任何实际恒等式后，应先合并表示，再重算核。A11 不排除在新表示中恢复完整列池，或在改变真实行列模型后证明无理性。

## 4. 参数 z 上的真实无限极点

A2 还说明不能把所有阶值一并装进这个参数函数，就自动获得一个先验 holonomic germ。对 u≥1，几何级数一致绝对收敛，且

\[
K(u)=\frac{\log\cosh u}{\sinh u}
-\frac32\frac{u+\log\cosh u}{\sinh(2u)},
\quad \log\cosh u=u-\log2+\log(1+e^{-2u}).
\tag{A12}
\]

展开两种 sinh 倒数和最后的 log，得到

\[
K(u)=\sum_{a\ge1}(A_a u+B_a)e^{-au},\quad
A_{2k+1}=2,\quad A_{4k+2}=-6,\quad A_{4k}=0,
\tag{A13}
\]

其中 Bₐ 是有限个交错 harmonic 和及 log2 的组合，满足 |Bₐ|=O(log(a+2))。这一估计由每个指数所需的有限卷积 Σₖ≤a1/k 直接给出。

将 F 的积分在1处分开。[0,1] 的部分在全平面 entire。其余积分可在每个紧集、避开 ±a 后正常收敛地逐项继续：尾项由 O((1+|z|+log(a+2))e^{-a+|Re z|}) 控制，分母 |a±z| 在大 a 时有一致线性下界。由

\[
\int_1^\infty u e^{-wu}du=e^{-w}(w^{-2}+w^{-1}),\quad
\int_1^\infty e^{-wu}du=e^{-w}/w
\tag{A14}
\]

得到全平面亚纯 F。在每个正奇整数 a 处，只有该指数的 exp(zu) 项可能有极点，其 Laurent 最高系数为 Aₐ=2，因而

\[
F(z)=\frac{2}{(a-z)^2}+\frac{B_a}{a-z}+O(1),
\qquad a=1,3,5,\ldots.
\tag{A15}
\]

由于 e⁻ʷ(w⁻²+w⁻¹) 的单极点项相消，A15 的简单项确为 Bₐ。没有别的指数或 finite interval 可以抵消这个双极点。

因此 F 不满足任何非零的 C(z) 系数齐次线性微分方程。否则取最高非零导数系数，在除去有限个有理系数极点/最高系数零点后，方程是普通解析线性方程，其解在每个普通点局部解析；这与 A15 的无限极点矛盾。实际半轴母函数 A₀(z)=2Σₖ≥0(−1)ᵏ/(2k+1−z) 同样具有无限极点，亦不能作为这个参数上的 holonomic 统一对象；将相邻项配对后，尾项为 O(k⁻²)，在避开奇整数的紧集上正常收敛，故这些真实极点没有因继续方式而消失。

这个结论仅涉及参数 z。固定 ℓ 的空间变量 x 上，H17–H20 仍给有限 Kummer-jet holonomic arrays，不与 A15 冲突。CDT [有效版本§2.1，Theorem2.1](https://arxiv.org/html/2510.04156v1#S2)所需的有理 Taylor 系数、共同亚纯 map 和完整 denominator types，仍须对所选择的空间变量另证。F 的系数是实际周期，其有理性不会从仅一个 β 值的有理假设自动产生；本文没有应用任何数值 holonomy 矛盾。

## 5. 研究接口与核查范围

统一结果把两条任务分开：真正降低坏周期成本需要新的实际边界身份；直接换更高偶 jet 或对 F 在参数上不停求导，不能提供所需的有理 holonomic 空间。正测度 H 可用于构造有控制的边界矩阵、符号证书或多周期目标，但其算术化与解析比较仍要独立完成。

本文独立全文读取两份上列本地数学稿；参数模型的前半部分与后半部分通过两次互补读取覆盖全数学正文。复核了 CDT HTML§2.1 的定理条件，并在已同步源仓库的目录与 foundations 行137–165中核对零阶来源。没有新PDF读取/下载，没有执行旧研究程序、prime table 或 Lean。A1–A15是纸面推导，没有新数值实验，也没有全球首创性主张。

两份独立全文纸审已通过：全素数分工实际全文阅读本稿五节/A1–A15及两份完整数学输入，重推正尾、Hasse归一化、最高seed传播、原核和无限极点；边界求值分工另实际全文阅读本稿五节/A1–A15并独立核对相同核心。两位审阅者均无数学修正要求。作者补入复系数递推与A₀正常收敛的说明；本稿不把纸审称为形式化验证。
