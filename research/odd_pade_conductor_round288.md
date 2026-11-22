# 第288轮基线复核 · 七层素数带的二次特征导子

2026-11-22。记 \(m_d=2d-1,\ Z_d=A_d/B_d\)（既约，\(B_d>0\)），\(\Delta_d=m_d^2-Z_d<0\)。对充分大的每个 \(d\)，虚二次域 \(\mathbb Q(\sqrt{\Delta_d})\) 的基本判别式 \(D_d\) 满足 \(|D_d|>(4d)^\eta\)，其中 \(\eta>0\) 是有效绝对常数。这个全阶约束同时适用于指定射线 \(d=2^s-262135\) 的两个奇偶分支。仅知道上带完全分裂和二进平方类，即便再给出亚指数导子上界，也容许下带每一个素数都分裂。[上轮 F3 及数值门槛](odd_pade_single_ray_round287.md) · [原对象的 R1–R4](odd_pade_ray_band_round287.md)

## 本原特征与实际坏素数

以 \(\operatorname{sf}(n)\) 记正整数 \(n\) 的平方自由核。因 \(\gcd(A_d-m_d^2B_d,B_d)=1\)，有
\[
 k_d=\operatorname{sf}(A_d-m_d^2 B_d)\operatorname{sf}(B_d),\qquad
 D_d=\begin{cases}-k_d&k_d\equiv3\bmod4,\\-4k_d&\text{其余情形}.\end{cases}
\]
这里 \(k_d>0\)，且 \(\Delta_d\) 与 \(-k_d\) 同有理平方类。令 \(q_d=|D_d|\)，\(\psi_d(n)=(D_d/n)\) 为本原二次特征。R4 给 \(A_d\) 奇、\(B_d\) 偶。

对 \(p\mid P_d=\prod_{2d<p<3d,\ p>127}p\)，\(B_d\) 是 \(p\)-单位。若 \(p\mid G_d=\gcd(A_d,P_d)\)，则 \(\Delta_d\equiv m_d^2\not\equiv0\bmod p\)，所以 \(\psi_d(p)=1\)。于是原标量中保留七层的重量 \(T_d\) 满足
\[
 T_d\ \ge\ \sum_{\substack{p\mid P_d\\\psi_d(p)\ne 1}}\log p
 =\frac{\log P_d-\sum_{p\mid P_d}\psi_d(p)\log p
              +\sum_{p\mid P_d,\ p\mid D_d}\log p}{2}.                 \tag{C1}
\]
F3 中有理数的勒让德符号在 \(\nu_p(\Delta_d)>0\) 时为零。如果该赋值为正偶数，本原特征在该素数处可以取任一非零符号。因此 C1 直接由坏素数蕴含分裂导出。上带 \(3d<p<4d\) 中 R3 让 \(p\mid A_d\)，所以每个这样的 \(p\) 都满足 \(\psi_d(p)=1\)，在该域中完全分裂。

## 原射线的完整二进平方类

对 \(d_s=2^s-C,\ C=262135,\ s\ge19\)，有下表。记 \(k_{\rm odd}=k_d/2^{\nu_2(k_d)}\)。

| 指数 | \(k_{\rm odd}\bmod8\) | \(\Delta_d\) 在 \(\mathbb Q_2^\times/\mathbb Q_2^{\times2}\) 中的代表 | \(\nu_2(q_d)\) |
|---|---:|---:|---:|
| \(s=19\) | 5 | \(-5\) | 2 |
| \(s=20\) | 3 | \(-3\) | 0 |
| \(s=21\) | 1 | \(-2\) | 3 |
| 偶 \(s\ge22\) | 5 | \(-5\) | 2 |
| 奇 \(s\ge23\) | 5 | \(-10\) | 3 |

用 R4 的记号 \(b=\lfloor d/2\rfloor,\ M_0=2d-1,\ h_k\) 与 \(H_d\)。下面证明在整条射线上
\[
 \frac{4^d H_d}{(-1)^b\binom{M_0}{b}}\equiv1\pmod8.                \tag{C1a}
\]
R4 已将左侧写成 \((k,l)\) 双和，\(k=l=0\) 项恰为 1。在 \(k>l,\ t=k+l\) 时，合并 \((l,k)\) 后各项二阶至少为 \(1+\lceil t/2\rceil\)。在 \(k=l\ge4\) 时二阶至少为 \(k-1\ge3\)。在 \(k=l=3\) 时，R4 下界 \(k-1\) 之外还有 \(\binom{d+3}{3}^2\)，其二阶至少为 2，因为 \(d\) 为奇数。于是模 8 仅须再核 \((1,0),(2,0),(1,1),(2,2)\)。其相对于基准项的完整倍数为
\[
 (1+\mathbf1_{k\ne l})h_kh_l
 \sum_{\substack{0\le j\le t+1\\d-t-j\ {\rm even}}}
 (-1)^u\binom{t+1}{j}
 \frac{b^{\underline u}(M_0-b)^{\underline{t-u}}}{M_0^{\underline t}},
 \qquad u=(t+j-1)/2 .
\]
此处 \(d\ge9\)，各保留的 \(j\) 都使 \(d-t-j\ge0\)。在 \(d\equiv9\bmod2^{18}\) 上可用 \(d=9\) 求这四个倍数的模 8 值。确实，代入前后所有整数多项式分子分母至少同余模 \(2^{17}\)，其中 \(b=(d-1)/2\) 只损失一位。分母的偶因子来自 \(M_0^{\underline t}\) 和 \(k!l!\)，各完整分母的二阶至多 \(5+2=7\)，故有理差仍为 8 的倍数。在 \(d=9\) 处这四个数依次是
\[
 3240/323,\quad -95040/2261,\quad -291600/6137,\quad
 363813120/2104991.
\]
它们都属于 \(8\mathbb Z_{(2)}\)，证明了 C1a。[有完整项估值的 R4 证明](odd_pade_ray_band_round287.md)

因为 \(-\Delta_d=K_d^2 H_d-m_d^2\)，且 \(\nu_2(Z_d)=-6d+s_2(3d)<-3\)，去掉二幂后，\(-\Delta_d\) 的单位模 8 等于 \(4^d H_d\) 的单位模 8。又 \(b\) 偶，故只需计算 \(\binom{M_0}b\) 的奇单位。记 \(V(n)=n!/2^{\nu_2(n!)}\bmod8\)，则
\[
 V(n)=\prod_{i\ge0}g\bigl(\lfloor n/2^i\rfloor\bmod8\bigr),
 \qquad (g(0),\ldots,g(7))=(1,1,1,3,3,7,7,1).
\]
这是把奇数因子按八个数分块后的阶乘递推。所有奇数模 8 都是自身的逆，所求余数恰为 \(V(M_0)V(b)V(M_0-b)\)。三项自变量依次是
\[
 2^{s+1}-524271,\qquad 2^{s-1}-131068,\qquad
 3\cdot2^{s-1}-393203.
\]
对 \(s=19,20,21,22\)，三元组依次为 \((1,1,5),(5,5,3),(5,5,1),(5,5,5)\)。这些有限乘积还决定此后全部 \(s\)。在 \(A2^j-L,\ 0<L\le2^v,\ j\ge v+2\) 中，末 \(v\) 位是 \(L-1\) 的定长反码，高处是 \(A-1\)，中间有 \(j-v\ge2\) 个连续 1。增大 \(j\) 仅多出一个全为 1 的三位窗口，其因子 \(g(7)=1\)。三个 \(L\) 可分别取 \(v=19,17,19\)，故三项在 \(s\ge22\) 全都稳定。最后 \(\nu_2(k_d)\equiv 6d-s_2(3d)\bmod 2\)，在 \(s=19\) 为偶，在 \(s\ge20\) 同 \(s\) 奇偶。这给出表中完整的二进分类。

## 上带迫使导子的奇部增长

设 \(\psi\bmod q\) 为非平凡实二次特征，\(x=3d\) 或 \(4d\)，\(h=d\)。存在有效绝对常数 \(\eta>0\)，对所有充分大的 \(d\) 和 \(q\le x^\eta\)，都有
\[
 \sum_{\substack{x-h<p\le x\\\psi(p)=-1}}\log p\ \ge\ \frac{3h}{16}. \tag{C2}
\]
用 Thorner–Zaman 定理 1.1 的等差数列素数估计。若无例外零，取全部 \(\psi(a)=-1\) 的可逆类，其主项为 \(h/\varphi(q)\)。若有例外实特征 \(\chi_1\bmod q\)，取 \(\psi(a)=\chi_1(a)=-1\) 的可逆类。相同的两个特征给出 \(\varphi(q)/2\) 个类，不同的两个非主二次特征在线性空间 \(\operatorname{Hom}((\mathbb Z/q)^\times,\{\pm1\})\) 中独立，给出 \(\varphi(q)/4\) 个类。此时定理的主项为 \(\lambda h/\varphi(q)\)，其中
\[
 \lambda=1+\frac{x^{\beta_1}-(x-h)^{\beta_1}}{\beta_1 h}\ \ge1.
\]
定理所需的指数阈值在两种情形均由某个绝对 \(\theta_*<1\) 控制。先固定 \(0<\epsilon<(1-\theta_*)/3\)，再取 \(\eta<\epsilon\)。则 \(\lambda h/\varphi(q)\ge x^{1-\eta}/4\ge x^{\theta_*+\epsilon}\) 对大 \(x\) 成立。由于 \(x/h=3\) 或 \(4\)，相对误差至多为
\[
 C_\epsilon\exp\!\left(-\frac{c_\epsilon\log x}{\log q+o(\log x)}\right),
\]
这里 \(o(\log x)\) 与 \(q,a\) 无关。再缩小固定的 \(\eta>0\)，使该误差在 \(q\le x^\eta\) 时对所有充分大 \(x\) 小于 \(1/4\)。对选中的类求和得到 C2。较小的 \(\eta\) 可以有效选定，此处未给出其数值。[Thorner–Zaman，定理 1.1](https://link.springer.com/article/10.1007/s00209-023-03414-3) · [作者全文](https://arxiv.org/abs/2108.10878)

将 C2 用在 \(x=4d\)，与上带处处 \(\psi_d(p)=1\) 矛盾，故
\[
 q_d>(4d)^\eta,\qquad (q_d)_{\rm odd}>(4d)^\eta/8.                  \tag{C3}
\]
若下带可以使用 C2，\(3/16=0.1875\) 已超过七层重量门槛 \(0.1773720330\ldots\)。C3 表明真实导子超出这项充分条件的适用范围。固定导子、任意固定对数幂的导子上界及 \(d^{o(1)}\) 的导子上界在任何无界阶数子列上均已排除。

## 两带中任意符号表的实现

令 \(\mathcal P=\{p:2d<p<4d\}\)，\(M=\prod_{p\in\mathcal P}p,\ r=|\mathcal P|\)。任给符号表 \(\sigma_p\in\{\pm1\}\) 和一个预定的二进平方类，都存在负基本判别式 \(D\)，使
\[
 (\tfrac Dp)=\sigma_p\quad (p\in\mathcal P),\qquad \log|D|=o(d).     \tag{C4}
\]
小 \(o\) 可对全部符号表及八个二进平方类一致选取。

具体地，取 \(e\in\{0,1\}\)、奇数 \(b\in\{1,3,5,7\}\)，使 \(-2^e b\) 代表所需的二进平方类。固定任意 \(0<\alpha<1\)，令 \(N=\lfloor M^\alpha\rfloor\)，在 \(n=8j+b,\ 1\le j\le N\) 中寻找 \((n/p)=\sigma_p(-2^e/p)\) 的整数。乘以 \(2^r\) 后，满足全部符号的计数是 \(2^r\) 个模 \(M\) 的特征和的带符号和。这些特征在选中的局部因子取勒让德符号，在其余素数取主特征，遇到 \((n,M)>1\) 时每项都为零。主特征项为 \(N(1+o(1))\)，因为每个素数排掉至多 \(N/p+1\) 项，且 \(\sum_{p\in\mathcal P}1/p=O(1/\log d)\)。

对非主特征 \(\chi\bmod M\)，选 \(c\equiv b/8\bmod M\)，可将 \(\chi(8j+b)\) 换成 \(\chi(8)\chi(j+c)\)。Cochrane–Granville–Zheng 的推论 2 给出每个短和 \(O_\alpha(N^{1-\delta_\alpha})\)，\(\delta_\alpha>0\)。具体取其 \(y=M^{\alpha/3},\ \epsilon=1\)，于是 \(N\ge y^2\)，所有整除 \(M\) 的素数幂均小于 \(4d<y\)，且充分大 \(d\) 自动避开定理中仅依 \(\alpha\) 的有限个素数。由素数定理 \(\log M\sim2d,\ r=O(d/\log d)\)，故 \(2^r N^{1-\delta_\alpha}=o(N)\)。所需计数为 \(2^{-r}N(1+o(1))>0\)，误差对各符号一致。取任一这样的 \(n\)，置 \(D=\operatorname{disc}\mathbb Q(\sqrt{-2^e n})\)，则 \(|D|\le8(8N+7)\)。平方自由化保持所有这些奇素数的符号及有理数的二进平方类。对每个 \(d\) 取满足条件的最小 \(|D|\)，再由任意固定 \(\alpha>0\) 得 C4。[Cochrane–Granville–Zheng，推论 2 及其证明，2026 年预印本](https://arxiv.org/html/2601.10927v1)

同一短和估计也可从 Graham–Ringrose 的本原平方自由光滑模数定理得到。设 \(\chi\) 的本原导子为 \(E>1\)，则 \(E\mid M\)。用容斥去掉 \(M/E\) 的素因子，得到至多 \(2^r=M^{o(1)}\) 个长度至多 \(N/f+1\) 的本原特征和，其中 \(f\mid M/E\)。若 \(f>N^{1/2}\)，其平凡界为 \(O(N^{1/2})\)。若 \(E<N^{1/4}\)，完整周期和为零，余段的平凡界为 \(E\)。其余情形的区间长度至少为 \(N^{1/2}-1\ge E^{\alpha/3}\)，且每个 \(p\mid E\) 皆小于 \(4d<E^{\xi(\alpha/3)}\)。本原定理给出相对于长度的固定幂节省，足以吸收 \(2^r\)。这样 C4 亦只需经典短特征和输入。[Graham–Ringrose，定理 5](https://link.springer.com/chapter/10.1007/978-1-4612-3464-7_18) · [该定理的精确表述](https://arxiv.org/html/2601.10927v1#S1)

特别取两带全部 \(\sigma_p=1\)，二进平方类取实际 \(\Delta_d\) 的类。还可在该平方类中选出一个有理数 \(\widetilde\Delta\)，同时复现这两带逐素数的值和原来的实尺度。设该类由负的平方自由整数 \(-k\) 代表，取 \(t=(\nu_2(\Delta_d)-\nu_2(k))/2\)。对每个 \(p\in\mathcal P\)，选单位 \(\omega_p\) 使 \(-k\omega_p^2\equiv m_d^2\bmod p\)。取 \(x=2^tu/3^j\)，并用中国剩余定理要求 \(u\) 为奇数且 \(2^t u/3^j\equiv\omega_p\bmod p\)。对固定 \(j\)，正实轴上这些可取的 \(x\) 相隔 \(2^{t+1}M/3^j\)，故可取 \(j\) 充分大使
\[
 m_d^2+4^{-d}<kx^2<m_d^2+2\cdot4^{-d}.
\]
于是 \(\widetilde\Delta=-kx^2,\ \widetilde Z=m_d^2-\widetilde\Delta\) 有 \(\nu_2(\widetilde\Delta)=\nu_2(\Delta_d)\)，从而也有 R4 规定的精确二进分母。它满足 \(\widetilde Z=2m_d^2+4^{-d+o(d)}\)，在上带和目标带每个素数处都为零。这给出上述算术约束的反例模型。实际 \(Z_d\) 还满足完整的超几何恒等式，原射线的七层素数重量下界仍须使用这项额外信息。
