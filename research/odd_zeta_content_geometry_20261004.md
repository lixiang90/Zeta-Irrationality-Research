# 实际周期 content：固定对称的上限与随尺度整数滤波

日期：2026-10-04。本文新增推导，旧研究报告保持冻结；没有参数扫描，也没有得到 Catalan、ζ(7) 或固定奇 ζ 组合的无理性证明。

本轮取得两类可证明结果。首先，对旧 Catalan 简单极点序列，实际本原系数的 2 进公因子只有多项式级增长，不能提供指数救济。其次，对一个已具完整整性证书的矩序列，随尺度增长的整数滤波确实可以产生指数级共同因子；它与固定有限群平均的成本是不同机制。新近原始预印本正使用了后一机制，改善 Catalan 逼近，但没有达到无理性门槛。

## 1. content 应定义在同一个已认证的系数向量上

设固定实际周期行为 \(\boldsymbol\eta=(1,\eta_1,\ldots,\eta_r)\)，一个形式有经过证明的表示

\[
L_N=\langle\mathbf a_N,\boldsymbol\eta\rangle,
\qquad \mathbf a_N\in\mathbb Q^{r+1}\setminus\{0\}.
\tag{1}
\]

这些坐标应来自固定上同调基、明确 residue / 边界计算或其他完整系数证书。未知数值周期之间是否独立，不妨碍使用这样一个已指定的向量；却不能仅从两个数值表达式相等，就断言各坐标相等。

令 \(c(\mathbf a_N)>0\) 为加法子群 \(\sum_j\mathbb Za_{N,j}\subset\mathbb Q\) 的生成元。若整数 \(D_N\) 清掉全部坐标的分母，则

\[
h_N=\gcd_j|D_Na_{N,j}|,
\quad c(\mathbf a_N)=h_N/D_N,
\quad P_N=L_N/c(\mathbf a_N)=D_NL_N/h_N.
\tag{2}
\]

\(P_N\) 的整数系数互素。改用任何其他共同清分母因子，得到同一个 \(P_N\)。整体有理缩放只改变符号；固定周期行下的本原评价不因任意放大清分母因子而改善。

固定 \(S\in\operatorname{GL}_{r+1}(\mathbb Q)\) 对 content 的影响也只有常数因子。取正整数 A、B，使 AS、\(BS^{-1}\) 均为整数矩阵，则

\[
1/A\le\frac{c(S\mathbf a)}{c(\mathbf a)}\le B.
\tag{3}
\]

证明：若 t 是此比值，则 At 为正整数，B/t 也为正整数，直接给出两界。周期行须同时按 \(S^{-1}\) 变换，以保留实际评价。该结论只适用于固定有限维基变换；N 依赖的矩阵需重新计入其分母和高度。

### 同一形式的最低余量

若 \(D_N=\exp(\lambda N+o(N))\)，正评价有下界 \(L_N\ge\exp(-\alpha N+o(N))\)，则

\[
\log P_N\ge(\lambda-\alpha)N-\log h_N+o(N).
\tag{4}
\]

所以 \(P_N\to0\) 必须有 \(\liminf\log h_N/N\ge\lambda-\alpha\)。若要求 \(P_N\le e^{-\varepsilon N}\)，则右侧再加 \(\varepsilon\)。这是必要条件，并非达到它就足够；若另有 \(\log L_N=-\tau N+o(N)\)、\(\log h_N=\kappa N+o(N)\)，净指数才恰为 \(\lambda-\tau-\kappa\)。

对 Catalan 的非负、旋转不变、简单极点整分子，已证明的实际正积分下界与原统一 \(D_N\) 给 \(\lambda-\alpha=\gamma=3/2-\log2\)。这里 N 是**分子的总次数**，不能直接换成其他族的下标。参见 [已冻结的正积分证明](odd_zeta_bridge_positive_integral_20261004.md)。

## 2. 固定有限群不能自动供应随次数增长的统一 content

设有限群 H（阶 m 固定）保持随次数变化的输入整格 \(\Lambda_N\)。取不变格 \(\Lambda_N^H\)，范数像

\[
\Lambda_N^{\mathrm{norm}}=\Bigl(\sum_{g\in H}g\Bigr)\Lambda_N.
\]

有

\[
m\Lambda_N^H\subseteq\Lambda_N^{\mathrm{norm}}\subseteq\Lambda_N^H.
\tag{5}
\]

给定任意已经清分母的整数系数映射 \(\Phi_N:\Lambda_N^H\to\mathbb Z^{r+1}\)，令 \(g_N^{\mathrm{inv}}\)、\(g_N^{\mathrm{norm}}\) 分别为其两种像的全部坐标所生成整数理想的正生成元。若像非零，(5) 给

\[
g_N^{\mathrm{inv}}\mid g_N^{\mathrm{norm}}
\mid m g_N^{\mathrm{inv}}.
\tag{6}
\]

故由“改用整数范数而不用饱和不变格”额外得到的**全输入共同因子**，最多为 m，与输入格秩增长无关。证明只需对包含关系应用 \(\Phi_N\)，再取所有坐标的 gcd。

这不禁止特选向量产生巨大 gcd：一个原本原始的输入可以模很多素数靠近 \(\ker\Phi_N\)，投影后变得高度可除。它也不禁止上同调约化映射本身随 N 变化而产生新的 content。被排除的是把固定群的阶数、平均分母或格指标当成这种指数机制。

若 \(\Phi_N\) 的整数矩阵具有 Smith 形 \(U\Phi_NV=\operatorname{diag}(d_1,\ldots,d_s)\)，则全输入共同 content 是第一个不变因子 \(d_1\)，而不是像格指标 \(\prod_i d_i\)。单个输入 v 的 content 是 \(\gcd_i(d_i(V^{-1}v)_i)\)。很大的行列式/格指标因此不自动给每个实际线性形式很大的 gcd。

以上与 [真实商拉回及整格报告](odd_zeta_bridge_projection_20261004.md) 相容：固定商投影控制有限成本，次数增长的形式约化仍须另证。固定良约化几何不限制所有增长型分母素数，该报告的 \((\mathbb A^1,\{0,1\})\) 反例继续适用。

## 3. 新的逐项结果：旧 Catalan I_n 没有指数级 2 进本原救济

设

\[
I_n=\int_\Delta\frac{(x^2y^2)^n}{1-x^2-y^2}\,dx\,dy,
\quad \widetilde I_n=16^nI_n=\widetilde a_n+B_nG,
\quad B_n=\binom{2n}{n}.
\tag{7}
\]

精确递推的有限解为

\[
\widetilde a_n=-B_n\sum_{k=0}^{n-1}t_k,
\qquad
t_k=\frac{16^k(6k+5)(2k)!(k!)^2}{(4k+3)!}.
\tag{8}
\]

公式由 [Eskandari 2609.26308v1 Proposition 5.1](https://arxiv.org/html/2609.26308v1) 的递推解出；完整分母约化与 (8) 的推导见 [冻结的 bridge 报告 §6.1](odd_zeta_bridge_catalan_20261004.md)。本节在它们之上计算实际本原公因子，不进行有限样本推测。

记二进制数位和为 \(s_2\)。factorial 赋值公式给

\[
v_2(t_k)=4k-1-2s_2(k),\qquad v_2(B_n)=s_2(n).
\tag{9}
\]

\(t_0=5/6\) 的赋值为 −1；所有 \(k\ge1\) 的赋值至少为 1，因为 \(s_2(k)\le k\)。故有限和中有**唯一最低赋值项**，不会抵消。因此对每个 \(n\ge1\)，

\[
\boxed{v_2(\widetilde a_n)=s_2(n)-1.}
\tag{10}
\]

写最低项 \(\widetilde a_n=A_n/d_n\)，\(d_n>0\)、\(\gcd(A_n,d_n)=1\)。由 (10)，\(d_n\) 为奇数。令

\[
g_n=\gcd(|A_n|,B_n).
\]

真实本原评价为

\[
P_n=\frac{d_n}{g_n}\widetilde I_n
=\frac{A_n}{g_n}+\frac{d_nB_n}{g_n}G,
\tag{11}
\]

因为 \(\gcd(A_n,d_nB_n)=\gcd(A_n,B_n)\)。于是得到有限精确结论

\[
\boxed{v_2(g_n)=s_2(n)-1,\quad
v_2(A_n/g_n)=0,\quad v_2(d_nB_n/g_n)=1.}
\tag{12}
\]

即本原常数系数恒为奇数，本原 G 系数恒可被 2 整除而不能被 4 整除。由于 \(s_2(n)\le\lfloor\log_2n\rfloor+1\)，g 的 2 部分至多为 n；其对数除以 n 趋零。

若按原统一清分母因子

\[
D_{4n}=2^{4n+2}L_{4n}L_{2n}
\]

计算总 content \(h_n\)，则由 (7)、(11) 有

\[
h_n=\frac{4L_{4n}L_{2n}}{d_n}g_n,
\quad
v_2(h_n)=1+\lfloor\log_2(4n)\rfloor
+\lfloor\log_2(2n)\rfloor+s_2(n)=O(\log n).
\tag{13}
\]

整除的合法性由 \(d_n\mid O_{4n-1}O_n\mid L_{4n}L_{2n}\) 保证；\(O_m\) 是不超过 m 的正奇数之 lcm。这说明旧 I_n 若要取得正积分障碍所需的指数 content，必须来自奇素数部分；2 进规范化或固定旋转平均不会供应它。

### 不能从前缀结果推出逐项障碍

正测度的最大权重为 \(x^2y^2=1/16\)，故 \(\widetilde I_n^{1/n}\to1\)：上界直接取最大值，下界取任意靠近最大值、正测度的邻域再令邻域缩小。由 (11)，逐项指数预算为

\[
\frac{\log P_n}{n}
=\frac{\log d_n-\log g_n}{n}+o(1).
\tag{14}
\]

又 \(g_n\le B_n\)，所以 \(\limsup\log g_n/n\le\log4\)。但目前前缀分母的下指数 4，不是每个 \(d_n\) 的下指数 4；不能将二者交换量词，宣称 (14) 已排除整个旧序列。尚缺的精确问题是逐项奇素数的 \(d_n\) 与 \(g_n\) 比较。

对这个特定 I_n，实际根极限还给出 \(\log(D_{4n}I_n)/n\to6\)。因此若按 (13) 的原统一因子本原化并要求趋零，就必须 \(\liminf\log h_n/n\ge6\)，即每总次数的必要 content 指数至少为 3/2；这比整族通用下界 \(\gamma\) 更强。这里没有创造额外收益：它只是把已知实际积分根极限放进同一预算，而 (12) 表明这个所需救济必须几乎全部由奇素数贡献。

## 4. 随尺度滤波可以产生真正的指数共同因子

以下引理只使用同一系数向量的整性。设 \(\mathbf v_j\in\mathbb Q^{r+1}\)，且已知

\[
p^{\rho j}E_j\mathbf v_j\in\mathbb Z^{r+1},
\]

其中 \(\rho\in\mathbb Z_{\ge0}\)，\(E_j\) 是正整数。令 \(E\) 是 \(E_n,\ldots,E_{n+m}\) 的共同倍数，取整数 \(c_i\) 满足 \(p^{\rho i}\mid c_i\)。则

\[
p^{\rho n}E\sum_{i=0}^mc_i\mathbf v_{n+i}
\in\mathbb Z^{r+1}.
\tag{15}
\]

证明：第 i 项的前因子除以已知清分母因子后为整数
\((c_i/p^{\rho i})(E/E_{n+i})\)，逐项相加即可。相对朴素因子 \(p^{\rho(n+m)}E\)，新组合的全部坐标 content 至少含 \(p^{\rho m}\)。\(m\asymp n\) 时这是指数收益。

这不是无代价构造。系数 \(c_i\) 的实高度和实际积分大小必须在同一个组合上计算；也不能把 (15) 之后未证明的额外 gcd 当成已知。

### Catalan 的真实实例

用不同记号避免与 (7) 混淆，设

\[
J_j=\int_{[0,1]^2}
\frac{x^{j-1/2}y^j(1-x)^j(1-y)^{j-1/2}}
{(1-xy)^{j+1}}\,dx\,dy=u_jG-v_j.
\tag{16}
\]

原始超几何工作给完整整性 \(16^ju_j\in\mathbb Z\)、\(16^jL_{2j}^2v_j\in\mathbb Z\)；参见 [Krattenthaler–Zudilin 1802.08856v1 §2](https://arxiv.org/pdf/1802.08856v1)，以及 [Eskandari 2609.26354v1 式 (1.4)、(2.9)](https://arxiv.org/html/2609.26354v1)。早期 2002 稿仅证明 \(2^{4j+o(j)}\) 的版本，不能把早期定理误写成无附加因子的精确式。

取

\[
\widetilde J_{n,m}=\sum_{i=0}^m(-16)^i\binom miJ_{n+i}.
\tag{17}
\]

对 (15) 取 \(p=2,\rho=4,E=L_{2n+2m}^2\)，得

\[
16^nL_{2n+2m}^2\widetilde J_{n,m}
\in\mathbb ZG+\mathbb Z.
\tag{18}
\]

相对朴素因子 \(16^{n+m}L_{2n+2m}^2\)，这里有保证的真实共同因子 \(16^m\)。因子已在 (18) 中除去，不能在随后预算再除一次。它可能尚不是实际最大 content。

最新预印本通过该滤波及实侧估计给出有效逼近指数至少 0.62，改善原族的 0.52，但仍低于无理性所需的 1。本文核验上述整性逻辑，不声称已经审定其全部渐近优化或形式化证明。[2609.26354v1 Theorem 1.1](https://arxiv.org/html/2609.26354v1)。

## 5. 该滤波有明确的高极点几何表达式

置

\[
f=x^2y^2,\qquad g=1-x^2-y^2,
\qquad h=g^2-4f.
\]

几何族

\[
K_j=\int_\Delta\frac{f^jh^j}{g^{2j+1}}\,dx\,dy
\]

与 (16) 满足实际精确等式 \(J_j=2^{2j+3}K_j\)。这是 [2609.26308v1 Theorem 1.1(a)](https://arxiv.org/html/2609.26308v1) 的对角特例；所有外部有理因子须保留。

将它代入 (17)，对整数 \(n,m\ge0\)，有限二项式展开给出本轮直接推导的表达式

\[
\boxed{\widetilde J_{n,m}=2^{2n+3}
\int_\Delta
\frac{f^nh^n\bigl(g^2-64fh\bigr)^m}
{g^{2n+2m+1}}\,dx\,dy.}
\tag{19}
\]

证明：\((-16)^i2^{2i}=(-64)^i\)，统一最高极点后，分子为
\(f^nh^n\sum_i\binom mi(-64fh)^ig^{2m-2i}\)，即 (19)。因而这里没有借未知的 G 无理性比较两个系数向量。

每个原 K 项已收敛，有限和的函数绝对值被这些正可积项之和控制，故 (19) 收敛。若 m 为偶数，\(f,h\ge0\) 于 Δ，分子非负且在开集非零，所以实际积分严格正。旋转不变性也直接成立。纯 G 性由同一已认证的有限线性组合获得；不能仅因提高极点后积分收敛，就跳过相对边界与成员关系的检查。

另一种写法是令 \(\rho=4fh/g^2\)，则

\[
J_j=8\int_\Delta\rho^j\frac{dx\,dy}{g},
\quad
\widetilde J_{n,m}=8\int_\Delta\rho^n(1-16\rho)^m\frac{dx\,dy}{g}.
\tag{20}
\]

这把几何改进化为一维正推前测度上的整数多项式滤波。它仍有明确的高极点与增长参数 m，不能套用简单极点原 \(D_N\)。总分子次数为 \(8(n+m)\)，所以如用旧正积分的纯实下界，次数也必须相应转换。当前改善是确实改变算术与实侧的同一个族，而不是同一函数空间内固定换基。

## 6. Rhin–Viola 型变换的收益取决于随 N 的归一化

固定 120 元参数群与固定群平均不是同一算术操作。Zudilin 的 Thomae/Whipple 变换保持经 Gamma 因子归一化的超几何函数；参数随 N 增长，Gamma 比值也随 N 变化。参见 [math/0210423v1 §3、Theorem 3](https://arxiv.org/pdf/math/0210423v1) 和 [1802.08856v1 的参数群正常形](https://arxiv.org/pdf/1802.08856v1)。这解释为何固定阶数的群仍可能带来指数算术收益，而不违反 (6)。

其可检验的一般版本如下。假定有**系数向量级**证书

\[
\mathbf v_N=r_{t,N}\mathbf v_{t,N},\qquad
D_{t,N}\mathbf v_{t,N}\in\mathbb Z^{r+1},
\quad r_{t,N}\in\mathbb Q^\times.
\tag{21}
\]

令 \(a_{t,N}=D_{t,N}/r_{t,N}\)，并取有限有理数所生成理想的正生成元

\[
d_N=\gcd_{\mathbb Q,t}(a_{t,N}).
\]

有理 Bézout 组合给 \(d_N\mathbf v_N\in\mathbb Z^{r+1}\)。若原因子 D₀ 是其中一个，则保证 content 至少为 \(D_0/d_N\)，且

\[
v_p(D_0/d_N)
=v_pD_0-\min_t\bigl(v_pD_{t,N}-v_pr_{t,N}\bigr).
\tag{22}
\]

若只知道数值积分相等，而没有 (21)，不能以未知的周期独立性逐项比较系数来证明 (22)。需要实际变换的类关系、formal partial fraction 关系或独立的完整坐标计算。新归一化的全部素数与高度也必须包含在 \(r_{t,N}\) 中。

一个无需优化扫描的增长充分条件是：证明某个固定 \(0<a<b\) 上，每个充分大 N 与每个素数 \(aN<p\le bN\) 都使 (22) 至少为 1。则由素数定理，保证 content 的下指数至少为 \(b-a\)。factorial / 半整数 Gamma 比值的 Legendre 赋值可把这项任务化为有限的 floor 区间检查。**尚未得到新的 Catalan 或 ζ(7) 参数族满足足够大区间余量；这只是明确可证的接口与合格证书形式。**

## 7. 后续研究的具体缩减

| 对象 | 本轮已成立 | 尚缺的数学输入 |
|---|---|---|
| 固定旋转、固定周期基 | 额外全族 content 因子有固定上限 | 特选分子同时模大量素数落入约化核的结构，及高度 / 正性代价 |
| 旧简单极点 I_n | 本原系数精确 2 进模式；无指数级 2 救济 | 逐项奇素数 \(d_n/g_n\) 定理，不能用前缀量词替代 |
| 高极点滤波 (19) | 可积、偶 m 正、纯目标；有保证的 \(16^m\) 节省 | 除 (18) 后的全 content 和同族净实指数；0.62 不足以证明无理 |
| 变换群归一化 | 有理理想/Bézout、逐 p 的 (22) | 系数向量级证书及足够大的 prime 区间收益 |
| ζ(7) 或全部奇权 | 上述整格与滤波引理可复用 | 提供纯目标输入族的真实存在定理与完整指数预算 |

最有价值的下一步不是寻找更大的固定投影群，而是证明：某个可积纯周期族在一段随 N 增长的素数区间，两个实际系数同时具有额外可除性；或构造类似 (17) 的 p 进匹配滤波，并以同一个积分给实侧上界。任何收益都需超过 (4) 的同族必要余量。

本轮新中间结果是 (6)、(12)–(13)、一般滤波引理及 (19) 的明确几何表达式。它们既显示固定投影本身为何不够，也展示真正可随尺度增长的整性机制，没有把几何好坏素数或形式周期投影当成无理性结论。

## 8. 本轮原始文献

- [Eskandari，On two families of period integrals related to Catalan’s constant，2609.26308v1](https://arxiv.org/html/2609.26308v1)，2026-09-22；实际三参数几何族与超几何族的联系，含 (19) 所需对角恒等式。
- [Eskandari，Improved rational approximations to Catalan’s constant，2609.26354v1](https://arxiv.org/html/2609.26354v1)，2026-09-22；整数滤波、2 进节省与 0.62 定理。属于近期预印本，本项目未完成全证明形式化。
- [Zudilin，A few remarks on linear forms involving Catalan’s constant，math/0210423v1](https://arxiv.org/pdf/math/0210423v1)，2002-10-28；早期整性与参数群，所证明的 2 进界含次线性项。
- [Krattenthaler–Zudilin，Hypergeometry inspired by irrationality questions，1802.08856v1](https://arxiv.org/pdf/1802.08856v1)，2018-02-24；超几何恒等式与改进的完整整性。

文献归档由根任务统一完成；本文不修改索引或 manifest。[固定精确恒等式脚本](odd_zeta_content_geometry_20261004_verify.py) 与 [JSON 证书](odd_zeta_content_geometry_20261004_verify.json) 已运行通过：核对符号递推因子、m=2 的几何滤波恒等式及指定 n=3 的系数规范。它们不做参数扫描，不代替本文的无限阶 content 证明。
