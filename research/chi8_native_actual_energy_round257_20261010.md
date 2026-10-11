# 第257轮：固定native χ₋₈实际Y双sheet矩阵的全n实表示与有限范围结算

2026-10-10。固定第255–256轮的 `Y=L(2,χ₋₈)`、`a=1/√2`、参数绕+1的单圈T、3+T、完整P/D prototype和selected-even determinant。本文没有改变参数、行、列池、sheet word或period分解；没有新数值无理性/线性无关性定理。

本轮实际FULL读取冻结256 A contour、C integer、Root global、progress report，以及Root sensitivity稿。NEW逐字来源与读域见 `literature/native_chi8_sources_round257_20261010/contour_reading_scope.md`。下文自含推导，不借Catalan的energy/prime-edge非零。数学程序、finite-n头、CAS、prime/参数/map/word扫描及外Git写均0。

**结算：** 得到实际Y处、保留全部heads与ordinary Z的ALL-n三分量实积分矩阵及Andreief公式，并将旧的系数高度upper改进为

\[
\boxed{|2^{-n^2}\Delta_n(Y)|\le M^n n^{n/2}2^{2n-1}
=\exp(O(n\log n))\quad(n\ge1),}
\tag{E0}
\]

其中M是下文明确的固定常数。这个actual upper没有负的n²项，也不给无界实际非零，故未通过257目标特定净可行性要求。表示及安全upper保留为资产；不能据此续开当前默认prototype窗口，也不能将证书不足解释成全部χ₋₈方法no-go。

## 1. 同一实际monodromy jump的实折叠

沿用256实际全芽的核

\[
H_{old/new}(z,w)=\int_0^{\phi_{old/new}}
\frac{azS(az)\cos\theta-2\theta}
 {(a-w\sin\theta)(az-\sin\theta)}d\theta,
\quad \phi_{old}=\pi/4,\quad\phi_{new}=3\pi/4.
\]

在256证明的固定小双圆盘内，所有表面极点共同可去/域外，核实际解析。新旧差的 `π/4..3π/4` 段，把θ与π−θ配对；两项的 `azS(az)cosθ` 精确抵消，线性θ项合成−2π，故

\[
H_{new}-H_{old}=-2\pi\int_{\pi/4}^{\pi/2}
\frac{d\theta}{(a-w\sin\theta)(az-\sin\theta)}.
\tag{E1}
\]

这不是形式start差；它来自同一实际Y contour。`sinθ≥a`，因此在该小芽域共同绝对展开，任意i,j同时有

\[
[z^iw^j](H_{new}-H_{old})
=\frac{2\pi}{a}a^{i-j}\int_{\pi/4}^{\pi/2}
\sin^{j-i-1}\theta\,d\theta.
\]

置 `x=a/sinθ`，则 `dθ/sinθ=−dx/√(x²−a²)`，得到全数组的实际实表示

\[
\boxed{N(i,j)=4N_{old}(i,j)+
4\pi\int_a^1\frac{x^{i-j}}{\sqrt{2x^2-1}}dx,
\quad N_{old}(i,j)=a^iM_a(i,j).}
\tag{E2}
\]

此等式对全部非负i,j成立，并保留actual period starts与全部rational heads。附加积分的负幂正常：其支持远离0。不需要指标相关的继续路径或有限截断校验。

## 2. selected-even完整矩阵及三个实际支持

固定 `n≥1,0≤r,s<n`，

\[
P_r=2^nx^{2r},\qquad D_r=2^nx^{2r+1}C_{n-r-1}(x^2),
\]
\[
C_m(z)=\sum_{\ell=0}^m b_\ell z^\ell,
\qquad b_\ell=2^{-\ell}\binom{2\ell}{\ell}=2^\ell c_\ell.
\]

设 `F_{rs}=N(P_r,2s)−9Z(D_r,2s)`，`Δ_n(Y)=det F`，以及仅用于同一det尺度记账的 `T_{rs}=2^{-n}F_{rs}`。原native旧支持 `[-a,a]` 的偶次折叠给

\[
4N_{old}(2r,2s)=16\int_0^a\int_0^1
\frac{x^{2r+1}y^{2s}}{\sqrt{1-2x^2}(1-x^2y^2)}dy\,dx.
\]

结合(E2)及完整ordinary Z伴随，实际矩阵为

\[
\boxed{\begin{aligned}
T_{rs}={}&16\int_0^a\int_0^1
\frac{x^{2r+1}y^{2s}}{\sqrt{1-2x^2}(1-x^2y^2)}dy\,dx\\
&+4\pi\int_a^1\frac{x^{2r-2s}}{\sqrt{2x^2-1}}dx\\
&-9\int_0^1\int_0^1
\frac{x^{2r+1}C_{n-r-1}(x^2)y^{2s}}{1-xy}dy\,dx .
\end{aligned}}
\tag{E3}
\]

尤其最后一项不是可忽略的rational correction：它是整个D polynomial在 `[0,1]²` 的实际值。它的degree截断恰为既定prototype，未换新P/D。这个矩阵已经包含所有finite heads，并非只保留Y coefficient rank的模型。

定义三个不相交、带标签的实测度分量：

| 分量 | 支持与正测度ν | 行函数f_r | 列函数g_s |
|---|---|---|---|
| O，旧sheet偶次折叠 | `[0,a]×[0,1]`，`16x dxdy/[√(1−2x²)(1−x²y²)]` | `x^{2r}` | `y^{2s}` |
| J，实际单圈jump | `[a,1]`，`4π dx/√(2x²−1)` | `x^{2r}` | `x^{−2s}` |
| Z，普通伴随 | `[0,1]²`，`9 dxdy/(1−xy)` | `−x^{2r+1}C_{n-r-1}(x²)` | `y^{2s}` |

令U为此不交并、ν为三正测度之和。则(E3)严格是 `T_{rs}=∫_U f_r(ξ)g_s(ξ)dν(ξ)`。符号留在Z行函数中；行列函数不是同一族，ν正不能推出Gram正定。

三个测度均有限。O的分母 `1−x²y²≥1/2`，且 `∫₀^a x/√(1−2x²)dx=1/2`，故其质量≤16。J的质量为 `2√2π log(1+√2)`。Z的质量为 `9ζ(2)=3π²/2`（角点(1,1)仍可积）。因此固定

\[
\nu(U)\le M:=16+2\sqrt2\pi\log(1+\sqrt2)+\frac32\pi^2<\infty.
\tag{E4}
\]

支持区别已保留：J不是将ordinary Z的 `(a,1]` 区间改造成原conic正测度；O、J、Z的kernel及列函数各不相同。

## 3. ALL-n实际Andreief，以及Gram捷径的具体缺口

每个n的f、g有界、ν有限。展开两det为有限Leibniz和、绝对Fubini，再按置换对称性整理，直接证明

\[
\boxed{\det T=\frac1{n!}\int_{U^n}
\det[f_r(\xi_k)]_{r,k=0}^{n-1}
\det[g_s(\xi_k)]_{s,k=0}^{n-1}
\prod_{k=0}^{n-1}d\nu(\xi_k).}
\tag{E5}
\]

这是完整actual Y determinant的同一表示，对所有n成立，不是一个单独分量det代替原det。

若所有ξ_k在J分量，令 `z_k=x_k²`。两det为 `V(z)` 与 `V(z⁻¹)`，而

\[
V(z^{-1})=(-1)^{n(n-1)/2}V(z)
\prod_k z_k^{-(n-1)}.
\tag{E6}
\]

因此仅J分量的积分项是固定符号 `(-1)^{n(n−1)/2}`，其绝对值严格正（V在不同点非零且权正）。它对n≡2,3(mod4)是负项。此全n恒等式指出行列逆序的实际方向，不能用“jump系数皆正”领取非负Gram integrand。完整(E5)还包含各分量混合，以及带负号且r相关截断的Z行函数；它们没有被证明同号。

本段没有从单独J非零推出Δ_n(Y)非零，没有说任意更深的signed/biorthogonal方法均不可能，也没有推导actual det下界。它准确否决的只是把(E3)直接当作一个正测度同函数Gram矩阵的捷径。若以后出现同对象完整非零证书，仍须控制(E5)全部项的取消。

## 4. 实际Y处的全n上界：列Vandermonde与行高度恰抵消

在U各分量上统一有 `g_s(ξ)=η(ξ)^s`，其中O/Z的 `η=y²∈[0,1]`，J的 `η=x⁻²∈[1,2]`。所以列det恰为η的Vandermonde，全部节点在 `[0,2]`。

给出自含Chebyshev-Hadamard bound。令 `p₀=1`、`p_s(η)=2^{1-s}T_s(η−1)` (`s≥1`)，其中 `T₀=1,T₁=t,T_{s+1}=2tT_s−T_{s−1}`；同一递推给 `T_s(cosθ)=cos(sθ)`，于是p_s单首且在 `[0,2]` 的sup≤`2^{1-s}`。换成这组monic行不改变Vandermonde；每行的Euclidean范数至多√n乘其sup。故

\[
|\det[g_s(\xi_k)]|\le
n^{n/2}2^{n-1-n(n-1)/2}.
\tag{E7}
\]

另一方面，O/J上 `|f_r|≤1`。Z上 `x≤1`，且 `b_ℓ≤2^ℓ`，所以

\[
|f_r|\le\sum_{\ell=0}^{n-r-1}2^\ell
=2^{n-r}-1<2^{n-r}.
\]

有限Leibniz直接给

\[
|\det[f_r(\xi_k)]|\le n!\prod_{r=0}^{n-1}2^{n-r}
=n!2^{n(n+1)/2}.
\tag{E8}
\]

将(E4),(E7),(E8)代入完整(E5)，n!抵消，精确得到(E0)。row-height的正 `+(1/2)log2·n²` 与column Vandermonde的负 `−(1/2)log2·n²` 恰好抵消，剩余 `O(n log n)`。还原原矩阵每行的既定2^n倍数，

\[
\boxed{|\Delta_n(Y)|\le
2^{n^2}M^n n^{n/2}2^{2n-1}.}
\tag{E9}
\]

此upper依赖真正Y的实际三分量模型，没有被声明对任意free start g的canonical contour成立。它也没有证明大小为这个upper、或actual energy lower为0；可能存在更强target-specific取消，这里未控制。

## 5. 必须还原完整primitive费用；本窗口不续

冻结256算术证书给 `q=q_{2n−1}=2^{4n−1}d_{2n}³`、已付共同整数row content `κ_n=2^{n(n+1)/2}`，以及 `(q^n/κ_n)Δ_n(T)∈Z[T]`。令Π_n为同一det的positive-leading primitive整多项式，那么Π_n是该整多项式除以其整数content，因此

\[
|\Pi_n(Y)|\le\frac{q^n}{\kappa_n}|\Delta_n(Y)|
\le\frac{q^n}{\kappa_n}2^{n^2}M^n n^{n/2}2^{2n-1}.
\tag{E10}
\]

它只是一份安全upper；不是primitive最优费或实际error下界。精确已知leading记账为

\[
\log\frac{q^n}{\kappa_n}+n^2\log2
=3n\psi(2n)+\Big(\frac92n^2-\frac32n\Big)\log2,
\tag{E11}
\]

其中 `ψ(m)=log d_m`。若仅沿用256的标准PNT换算作比较标尺，(E11)leading为 `6+(9/2)log2`，仍为正。本轮解析推导不依赖PNT，也没有凭此upper断言真实primitive净指数为正。与256通用coefficient-height界相比，这里省去一个 `log2·n²` 的安全height项，却没有出现所需的actual负二次项。

任何本轮另经完整证明的更小整数scalar A_n也只能使(E10)中的 `q^n/κ_n` 换成A_n；是否严格仍必须把 `log A_n+n²log2` 连同更强actual估计一起比较，不能免费删除2^n行尺度。本文没有以未FULL读取的其它257子稿或消息代替该算术证明。

若Y有理且Π_n(Y)≠0，才有 `|Π_n(Y)|≥v^{-n}`。本轮没有证明无界n子列上该值非零，也没有证明 `log|Π_n(Y)|/n²` 的负limsup。因此无法从(E10)推出矛盾，不能以系数rank、J-only非零或free-start子水平集合估计代领。

本窗口的最终数学输出是(E2)–(E5)完整actual表示及(E0)/(E9)安全全n upper。它们不提供所要求的净可行性证书。按256冻结的停止规则，第257轮结算当前默认prototype投入；表示资产保留，不能以新增局部lemma、可算finite heads、prime saving或更多sheet/参数搜索为同一窗口的续轮理由。原总goal仍active，且仍无新数值定理；本稿不宣告所有χ₋₈或统一框架不可行。
