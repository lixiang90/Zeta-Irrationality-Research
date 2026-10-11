# 原配对行列式的多根势能：全尺度转移与有限原子严格改进

日期：2026-10-07。NEW 纯纸面证明。原 B6/κ3/s5、degree<3n、饱和整数值格 S、whole-X D_A(X) 全部保持。此前518冻结记录只读；本文没有执行、导入或重跑数学 producer，没有辅助单位素数扩表。下述结论是解析上界的改进机制，不是新的无理性或线性无关性定理。正式独审与最终收据另行保存。

## P1. 精确接口与优化量

使用已经证明的 [coupled-Gram C2–C7](cdt_odd_paired_coupled_gram_decay_20261007.md)，记 c_n=2n+1/2、N=floor(n/2)。任何 degree(q)≤n 且全部真实 head 上 q 非零的多项式，通过沿原高列的 determinant1 剪切，保持 D_A(X) 完全相同。其 C9 的全 n 界仍有原高 Gram、真实 mirror coefficient/Hardy sum 和 Γ_n，均只支付一次。

本文使用有限原子概率测度

\[
\rho=\sum_{i=1}^d\omega_i\delta_{s_i},\quad
s_i>0\text{ 互异},\quad\omega_i>0,\quad\sum_i\omega_i=1.
\tag{P1}
\]

取非负整数 N_i，ΣN_i=N，且 N_i/N=ω_i+O(1/N)；只在 N>0 时定义这些比值。固定 d 的舍入总能满足该条件。令

\[
q_{n,\rho}(z)=\prod_i((z-c_n)^2+n^2s_i)^{N_i}.
\tag{P2}
\]

degree(q)=2N≤n，真实 head 上 q>0。若所有 s_i 有理，则 q 的系数有理，但即使先用实 s_i，剪切的 determinant 恒等式也不改变原整数模型的费用。这里没有把新列声称为免费整数基。

冻结的真实竖线包络为

\[
W_n(ny)\le Cn^{4n+C}(1+|y|)^C e^{nQ(y)},
\]
\[
Q(y)=12\log6-6\log2-6+7J_2(y)-2J_8(y)-2\pi|y|,
\quad J_A(y)=\int_0^A\log\sqrt{v^2+y^2}\,dv.
\tag{P3}
\]

设

\[
I(s)=\int_0^1\log(s+t^2)\,dt
=\log(s+1)-2+2\sqrt s\arctan(1/\sqrt s),
\]
\[
J(\rho)=\sum_i\omega_i I(s_i),\quad
F_\rho(y)=Q(y)+\sum_i\omega_i\log|y^2-s_i|-J(\rho),
\]
\[
V(\rho)=\sup_{y\ge0}F_\rho(y),\quad
M_0=\sup_y Q(y),\quad\varepsilon(\rho)=M_0-V(\rho).
\tag{P4}
\]

根处按 −∞ 解释。Q 是偶函数，所以正半轴足够。注意 J(ρ) 随根的分布变化；不能只优化分子而忽略真实 head 分母。单原子 ρ=δ_s 时准确恢复 ε(s)=M_0−sup_y[Q(y)+log|s−y²|]+I(s)。

## P2. 全 n 费用转移，不使用有限采样

对充分大的 n，ρ_n=Σ(N_i/N)δ_{s_i} 的全部权重≥ω_i/2。记 θ_n=2N/n，M(ρ)=V(ρ)+J(ρ)。沿竖线有

\[
|q_{n,\rho}(c_n+iny)|^2
=n^{4N}\prod_i|s_i-y^2|^{2N_i}.
\]

点态凸组合（包括根处的 −∞）给

\[
\sup_y\left[Q(y)+\theta_n\sum_i\frac{N_i}{N}\log|s_i-y^2|\right]
\le(1-\theta_n)M_0+\theta_n M(\rho_n).
\tag{P5}
\]

Q(y)=−2π|y|−2log|y|+O(1)，而根势为 2log|y|+O(1/y²)。故 θ∈[0,1]、这些固定根和权重下，尾部统一 ≤−π|y|，在足够大的固定区间之外成立。P3 中的 polynomial prefactor 由指数尾部支配。于是实际 C9 的 A_n(q)=sup_x W_n(x)|q(c_n+ix)|² 满足

\[
\log A_n(q_{n,\rho})
\le(4n+4N+C)\log n
+n[(1-\theta_n)M_0+\theta_n M(\rho_n)]+O(1).
\tag{P6}
\]

每个 mirror pair 的两真实距离为 2n+1/2−m 和 m−1/2，任意实际选择 a_m 均有 |c_n−a_m|≥m−1/2。因 s_i>0，故对每个 mirror choice 分别有

\[
\sum_{m=1}^n\log q_{n,\rho}(a_m)
\ge2Nn\log n+
\sum_iN_i\sum_{m=1}^n\log\left(s_i+\left(\frac{m-1/2}{n}\right)^2\right).
\tag{P7}
\]

固定 s_i 的 log(s_i+t²) 在 [0,1] 上 Lipschitz。midpoint Riemann 误差为 O(1)，常数只依赖这些固定根。因此 P7 ≥2Nnlog n+NnJ(ρ_n)−O(N)。没有假设镜像 q 值相等。

将 P6/P7 放进同一个 C9，整个低块共同因子（即 A_n(q)^n 和所有 head 分母的平方）相对于旧 4n²log n+n²M_0 准确多出

\[
-2Nn\,[M_0-M(\rho_n)+J(\rho_n)]+O(n\log n).
\tag{P8}
\]

下面说明 ε(ρ_n)=ε(ρ)+O(1/n)，不把含 log 奇点的 supremum 连续性当成免费步骤。所有权重在固定正数区间内时：尾部统一向 −∞；每个固定根附近的对应 log 项及正权重使 F 一致向 −∞；选一个避开所有根的固定点给统一有限下界。故所有最大点处在一个固定紧集，且与全部根保持固定正距离。在该集上每个 log 项有界，舍入权重的 O(1/n) 扰动直接给 |V(ρ_n)−V(ρ)|=O(1/n)，J 的误差亦为 O(1/n)。又 2Nn=n² 或 n²−n，得到全尺度额外主率 ε(ρ)。有限个初始 n（包括 n=1、某 N_i=0）可单独增加上界常数。

若冻结的旧 mirror 主率记为 β_mirror，则同一个旧高块、镜像与 Γ_n 付费后有

\[
\log|D_{A,n}(\xi)|
\le-[\beta_{\rm mirror}+\varepsilon(\rho)]n^2
-2\log\Gamma_n+O(n\log n),
\tag{P9}
\]

其中可取任何已证旧 mirror 下率；不为 Γ_n 擅自引入未证 O(nlog n) 误差。用已有 β_mirror>9.09188285412558、liminf n⁻²log Γ_n≥1.455845，得到

\[
\boxed{\limsup_{n\to\infty}n^{-2}\log|D_{A,n}(\xi)|
<-12.00357285412558-\varepsilon(\rho).}
\tag{P10}
\]

log0=−∞。P9/P10 不证明 D_A(ξ) 非零；新 q 剪切也不改变算术安全费用上界或实际最小分母。

## P3. 有限原子测度永远可被更多根严格改进

**定理。** 对每个 P1 的有限原子 ρ，存在另一个有限原子概率测度 ρ'（所有根仍严格正），使 V(ρ')<V(ρ)，亦即 ε(ρ')>ε(ρ)。若希望 q 全为有理系数，可以选择 ρ' 的全部根位置和权重均为正有理数。

**证明最大点只有有限多个且都在正半轴。** F_ρ 上半连续、根处为 −∞、无穷远为 −2πy+O(1)，故有限 supremum 实现。对 y>0 有

\[
Q'(y)=7\arctan(2/y)-2\arctan(8/y)-2\pi,
\quad
F'_\rho(y)=Q'(y)+\sum_i\frac{2\omega_i y}{y^2-s_i}.
\tag{P11}
\]

F'_ρ(0+)=π/2>0，所以0不是最大点。每个根的两侧，含该正权重的 pole 主导导数，附近没有临界点；无穷远导数→−2π，附近也没有临界点。在避开这些边界的每段固定紧区间上，导数实解析，且不可能恒等为0：有根边界的段可用 pole 排除，首段亦可用0处正导数，末段可用无穷远极限。非零实解析函数的零点在其域内的紧集上有限。因此全部全局最大点为 y_1,…,y_h，均>0，且都不等于旧根的平方根。

令 σ=h⁻¹Σ_jδ_(y_j²)，B=V(σ)<∞。在每个 y_j 附近，F_σ−F_ρ→−∞，因为新根的 log 项而 F_ρ 在那里光滑。故可取有界开邻域 U 覆盖所有最大点、避开旧根，并使 F_σ−F_ρ≤−1 于 U。U 的补集上没有最大点；由上半连续性与无穷远衰减，存在 η>0 使 F_ρ≤V(ρ)−η。

对 0<t<1，ρ_t=(1−t)ρ+tσ。P4 的全部项对测度线性，故在有限值处 F_(ρ_t)=(1−t)F_ρ+tF_σ；旧/新根处按照 −∞ 解释，同样满足下面上界。U 上 F_(ρ_t)≤V(ρ)−t。U 外有

\[
F_{\rho_t}\le(1-t)[V(\rho)-\eta]+tB.
\]

取 t 足够小使右端≤V(ρ)−η/2，即得

\[
\boxed{V(\rho_t)\le V(\rho)-\min(t,\eta/2)<V(\rho).}
\tag{P12}
\]

这不是有限网格搜索，而是覆盖所有最大点及其补集的严格全域估计。

**有理参数的稳定性。** 在固定有限正原子配置附近，根保持在固定有界正区间、权重保持正。无穷远 F 的衰减统一。若参数趋于该配置，最大点的一个子列处于固定紧集并趋于 y；log|y²−s| 的联合上半连续性（根处值 −∞），I(s) 的连续性及权重正性给 limsup V(邻近配置)≤V(该配置)。也可用避根固定点给最大值统一下界，排除最大点趋于根。因 P12 有严格缺口，充分接近 ρ_t 的正有理位置与权重仍保持 V<V(ρ)。正有理权重和为1的集合稠密，可用最后一个权重补足；位置互异亦可保持。定理证毕。

## P4. 这改变了下一步，而没有自动完成无理性证明

P3 特别说明：即使一个单根尺度族的全局最佳 s 已严谨求出，它也不是全部 q 的最佳选择。任何固定有限根型均可再严格改善。正确的进一步问题是根的分布和带有 J(ρ) 的变分问题，而非继续只调一个尺度。

本定理没有证明连续测度最优解存在、无原子、唯一或其值，也没有证明无穷根优化能取得算术所需的 strict margin。不能由“每步严格改善”推出改善无界；P4a 反而给当前特定优化量的统一有限上界。它更不提供 actual D_A(ξ) 无限非零、H|kerC 正常性、actual residual pencil regularity或同一 fixed rational source 无限成功。

实际下一接口仍应共同处理：根势分子、真实 head 分母、mirror 的选择相关性、正 Gram Schur 投影，及真正 complex phase 的 singular-value 主率。P7 的逐 pair 距离下界保守；其保守性不等于实际最佳衰减率的上限。本文也不把 safeA≈40.314517426 的上界当作 actual 费用下界或 no-go。

### P4a. 当前变分量的粗对偶上界，排除“严格改善即无界”

对 y∈[0,1] 均匀平均（不是有限原子采样），令

\[
h(s)=\int_0^1\log|y^2-s|\,dy-I(s).
\]

若 0<s≤1，置 a=√s，直接积分给

\[
\int_0^1\log|y^2-s|\,dy
=(1-a)\log(1-a)+(1+a)\log(1+a)-2\ge-2.
\]

0log0 按极限解释；两个 log 项之和在 a=0 为0、导数 log((1+a)/(1−a))≥0。又 I(s)≤log2，故 h(s)≥−2−log2。若 s≥1，逐点有 log[(s−y²)/(s+y²)]≥log[(1−y²)/(1+y²)]，从而 h(s)≥h(1)=log2−π/2>−2。所有有限根型因此满足

\[
V(\rho)\ge\int_0^1 F_\rho(y)\,dy
\ge\int_0^1Q(y)\,dy-2-\log2.
\tag{P13}
\]

这些 log 奇点可积，有限和的交换合法。这个不等式是直接平均，未使用未经证明的 minimax 交换。

冻结 C14/C5a 已给 Q 在 [1,∞) 严格下降，并且在 [0,1] 有 Q''≤−51/20，而显式公式另给 Q''≥−7/2。Q'(0+)=π/2，所以

\[
M_0\le Q(0)+\frac{\pi^2}{8(51/20)}<Q(0)+\frac{40}{51},
\]
\[
\int_0^1Q(y)\,dy
\ge Q(0)+\pi/4-7/12>Q(0)+1/6,
\]

仅用 elementary 3<π<4。再用 log2<1，得对所有 P1 的有限原子分布

\[
\boxed{\varepsilon(\rho)
\le M_0-\int_0^1Q(y)\,dy+2+\log2
<\frac{123}{34}<4.}
\tag{P14}
\]

这是 P4 中特定 V（含逐 pair head 距离下界）的解析信用上界。它不是 |D_A| 实际衰减率的上界，也不是所有 q、真实 mirror 相关性、exact Schur 或 complex phase 方法的 no-go；更不能与算术安全费用上界作下界比较。P12 和 P14 一起说明：有限根型确实总有严格改进空间，而单靠当前粗包络优化不会产生无界信用。下一步应改善保守接口本身。

## P5. 一手文献与实读范围

已存原件 [E. B. Saff, Logarithmic Potential Theory with Applications to Approximation Theory](../literature/saff2010_logarithmic_potential_arxiv1010_3760v1_20261006.pdf)，官方 [arXiv:1010.3760](https://arxiv.org/abs/1010.3760)，36页，SHA256 cfbeaad8cf695fc1b5528fd56295d7e3053056634c6841765a434ce9b074d862。本轮 root 实际完整读取 PDF1、32、33、34共4distinct页；未宣称全文验证。

PDF32–34 的 admissible weight、weighted Chebyshev 和 equilibrium 视角提示“优化根分布”。但标准 weighted Chebyshev 使用 monic normalization；本题 J(ρ) 是随根测度变化的真实 head normalization。因此不能直接把该文的标准 weighted equilibrium measure 当作当前 V 的最优解，P2/P3 均在这里独立证明。含 log 奇点的 minimax 交换也未证明，不能直接引用一个形式对偶式来给最优值。

本轮同伴新存 Mhaskar–Saff, *Weighted Analogues of Capacity, Transfinite Diameter, and Chebyshev Constant*, Constructive Approximation 8 (1992), 105–124：[作者原件](https://www.math.vanderbilt.edu/saffeb/texts/125.pdf)/[本地](../literature/cdt_paired_scaled_root_sources_20261007/mhaskar_saff1992_weighted_capacity_author_125.pdf)，20页，SHA256 66d00d46fb0e2f4da7b4c23e98dcc39b5687587e179a77813b27caa859968aa5。root 本轮实际完整读取 PDF1–4，4distinct页；Eq2.7–2.8 的 monic 约束及 Definition2.4 的 admissibility 明确了上述不能直接套用的接口。root 没有重复下载；本轮 web 对作者125原件的独立 fetch超时，已有本地合法原件正常可读。

本轮曾尝试作者站 https://www.math.vanderbilt.edu/saffeb/texts/230.pdf：web fetch超时，随后正常 verified TLS 下载遇 hostname mismatch，未保存 PDF、未关闭证书检查；后来定位上述已有 arXiv 原件，未重复下载。该失败是文献访问失败，不是数学 producer 失败。新增数学执行0、失败0、重跑0、旧/同行执行/import0、Lean0。

本稿是新的全尺度转移和有限根严格改进证明；最终独审及其已查范围由另存正式 review 和来源收据记录，不改动任何此前冻结证据。
