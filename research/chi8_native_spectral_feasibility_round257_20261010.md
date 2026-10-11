# 第257轮：固定native χ₋₈ prototype的混合行交替式、精确边框与谱预算结算

2026-10-10。沿用第255–256轮冻结的 `Y=L(2,χ₋₈)`、`a=1/√2`、绕参数 `+1` 的单圈 `T`、`3+T`、完整native N与ordinary Z，以及整数接触行和selected-even列。本稿只检验同一prototype的actual Y净可行性，不替换参数、sheet、行向量或列池。原数值ζ/L目标仍active；没有新的数值无理性、线性无关性或Lean认证。

本身份逐份实际FULL读取256 sensitivity、256 contour、257 actual energy、257 primitive feasibility和256 progress五稿。精确读域及当前bytes/hash见 `literature/native_chi8_sources_round257_20261010/spectral_reading_scope.md`；未继承前一个执行身份的FULL标签。以下新增推导自含，不调用未读取的primary材料，也不把已读稿中的历史审计当成本身份审计。

**结算：** actual混合行交替式没有全node Vandermonde因子；相邻尺寸也不是固定nested principal minors，而是一个明确的有理rank-one修改后的border。两者都没有给出actual无界非零或所需负二次净指数。257的完整内容改进是真实资产，但与目前actual upper合并仍未形成净可行性证书。按256停止规则，本257结算当前默认prototype窗口；不是一般χ₋₈ no-go。

## 1. 同一完整矩阵的上三角Toeplitz行变换

为避免将monodromy T与矩阵记号混同，以下 `T_n(g)` 只表示归一化矩阵。令

\[
b_\ell=2^{-\ell}\binom{2\ell}{\ell},\qquad
(U_n)_{r,k}=\begin{cases}b_{k-r},&k\ge r,\\0,&k<r,\end{cases}
\quad 0\le r,k<n.
\tag{B1}
\]

U_n为上三角unit Toeplitz，`b₀=b₁=1`，det U_n=1。冻结行是

\[
P_r=2^nx^{2r},\qquad
D_r=2^n\sum_{k=r}^{n-1}b_{k-r}x^{2k+1}.
\]

仅在256明确的全period分解中替换Y-start为g，记N^[g]；这不宣称g具有actual contour。定义

\[
\begin{aligned}
\mathcal N_n(g)_{r,s}&=N^{[g]}(2r,2s),\\
\mathcal Z_n{}_{k,s}&=Z(2k+1,2s),\\
T_n(g)&=2^{-n}F_n(g)=\mathcal N_n(g)-9U_n\mathcal Z_n,\\
p_n(g)&=\det T_n(g)=2^{-n^2}\Delta_n(g).
\end{aligned}
\tag{B2}
\]

由于odd index `2k+1` 不等于even index `2s`，这里所有Z entries均为有理数，完整值为 `(H_{2k+1}−H_{2s})/(2k+1−2s)`，含全部harmonic heads。完整N的even-even entries没有π²项，所以T_n(g)属于M_n(Q[g])。`2^{-n}`是本稿显示原det尺度的逐行归一化；它不改变primitive多项式，也不另领算术内容。

## 2. actual共同测度上的两个不成比例的行族

257 actual energy稿已经由同一实际monodromy推导三个不交标签分量。为明确本稿使用的对象，在其共同空间Ξ上保留以下全部数据：

| 分量 | 支持及正测度ν | t与列节点η | 行向量f(ξ) |
|---|---|---|---|
| O | `[0,a]×[0,1]`，`16x dxdy/[√(1−2x²)(1−x²y²)]` | `t=x²`，`η=y²` | `v(t)` |
| J | `[a,1]`，`4π dx/√(2x²−1)` | `t=x²`，`η=x⁻²` | `v(t)` |
| Z | `[0,1]²`，`9 dxdy/(1−xy)` | `t=x²`，`η=y²` | `−√t U_n v(t)` |

这里

\[
v(t)=(1,t,\ldots,t^{n-1})^{\mathsf t},\qquad
g_s(\xi)=\eta(\xi)^s,\quad 0\le\eta\le2.
\tag{B3}
\]

在actual g=Y处，完整矩阵恰为 `T_n(Y)_{r,s}=∫_Ξ f_r g_s dν`，并有

\[
p_n(Y)=\frac1{n!}\int_{\Xi^n}
\det[f_r(\xi_k)]\det[\eta(\xi_k)^s]
\prod_k d\nu(\xi_k).
\tag{B4}
\]

三个分量都参与此式。它不是自由g的共同正测度实现；ν正也不把不同的f、g变成同函数Gram矩阵。

对n≥2和t>0，v(t)与U_nv(t)不成比例。直接取底两行，

\[
\det\begin{pmatrix}
t^{n-2}&t^{n-2}+t^{n-1}\\
t^{n-1}&t^{n-1}
\end{pmatrix}=-t^{2n-2}\ne0.
\tag{B5}
\]

关键是同一正node在不同标签上也不使两个行列式columns比例。actual Z column另乘非零scalar `−√t`，故该底minor变为 `t^{2n-3/2}`，仍非零。

## 3. 全node Vandermonde不能从mixed alternant中提取

上述底minor可提升为所有n≥2的完整mixed determinant证据，而非只查看一个低阶矩阵。置m=n−2，取固定不同正数 `α₁<⋯<α_m`，`τ_j=εα_j`；m=0时空列与空Vandermonde均按通常约定处理。由multilinearity，最低总次数来自v(τ)的powers `0,…,m−1`；其系数恰为

\[
V_m(\tau)=\prod_{1\le i<j\le m}(\tau_j-\tau_i).
\]

所有更高总次数在除以V_m后随ε→0消失。因此，e_r表示第r个coordinate vector时，

\[
\begin{aligned}
&\lim_{\varepsilon\to0^+}
\frac{\det[v(\tau_1),\ldots,v(\tau_m),v(t),U_nv(t)]}
{V_m(\tau)}\\
&\qquad=\det[e_0,\ldots,e_{n-3},v(t),U_nv(t)]
=-t^{2n-2}.
\end{aligned}
\tag{B6}
\]

最后等式就是(B5)，因为前m列在前m行是identity、在底两行为0。这是一般n的合流恒等式，没有finite-n计算或CAS。

现在固定任意 `0<t<1/2`。对充分小ε，所有τ_j都在O内部node区间，另一个O node取t，一个Z node也取t。把末列换成actual `−√t U_nv(t)`后，(B6)极限为 `t^{2n-3/2}>0`；故充分小ε时完整actual row alternant非零。然而全部n个row nodes含两次t，所以全Vandermonde `V_n(τ₁,…,τ_m,t,t)`精确为0。O/Z的y坐标可分别选择，使全部列节点η互异且在(0,1)，此时column Vandermonde也非零。

因此完整mixed row alternant不被全部unlabelled nodes的Vandermonde整除；它也不可能满足有限常数乘全Vandermonde的uniform absolute bound。此缺口并非仅出现在测度零的精确重合处：在这些内部点的邻域，row alternant持续非零，而两node之差可任意趋零，故除全Vandermonde后的比值无界。

若所有row columns都来自O/J，row alternant确为V_n(t)。若全部来自Z，则

\[
\det[-\sqrt{t_k}U_nv(t_k)]
=(-1)^n\Big(\prod_k\sqrt{t_k}\Big)V_n(t),
\tag{B7}
\]

因为det U_n=1。这些pure sector可用两个Vandermonde的区间容量估计；(B6)说明该行因子不能外借给(B4)所有mixed terms。一个统一左乘U_n^{-1}也只把O/J改成U_n^{-1}v，把Z改成−√t v；可逆变换保留同node两族的不成比例性，并不修复全node因子。这里否决的只是这条直接双容量捷径，不是否定所有可能的signed、biorthogonal或target-specific估计。

## 4. 相邻尺寸的精确有理rank-one修改与bordered-adjugate式

`T_{n+1}(g)`的前n×n block并不是T_n(g)。增加contact degree后，每个旧r行新增一项 `b_{n-r}x^{2n+1}`。令

\[
\beta_r=b_{n-r}=2^{-(n-r)}\binom{2(n-r)}{n-r},\qquad
z_s=Z(2n+1,2s)\in\mathbb Q,\quad 0\le r,s<n.
\tag{B8}
\]

逐entry的完整恒等式为

\[
(T_{n+1})_{0\le r,s<n}=T_n-9\beta z^{\mathsf t}.
\tag{B9}
\]

没有截掉新finite heads。设其余border为

\[
\begin{aligned}
c_r&=N^{[g]}(2r,2n)-9\sum_{k=r}^{n}b_{k-r}Z(2k+1,2n),\\
h_s&=N^{[g]}(2n,2s)-9Z(2n+1,2s),\\
d&=N^{[g]}(2n,2n)-9Z(2n+1,2n).
\end{aligned}
\tag{B10}
\]

c为Q-vector；h、d为Q[g]且d的g系数为16。于是对actual Y和formal g均有

\[
T_{n+1}=\begin{pmatrix}A-9\beta z^{\mathsf t}&c\\h^{\mathsf t}&d\end{pmatrix},
\qquad A=T_n,
\qquad B=\begin{pmatrix}A&c\\h^{\mathsf t}&d\end{pmatrix}.
\tag{B11}
\]

令 `\widehat\beta=(\beta,0)^{\mathsf t}`、`\widehat z=(z,0)^{\mathsf t}`。rank-one determinant lemma由列multilinearity直接给出：含两个update columns的项因比例而为0。因此完全不要求可逆，

\[
\boxed{p_{n+1}
=d\det A-h^{\mathsf t}\operatorname{adj}(A)c
-9\widehat z^{\mathsf t}\operatorname{adj}(B)\widehat\beta.}
\tag{B12}
\]

为显式分离旧n阶block及二阶cofactor，定义一个始终是polynomial的border determinant

\[
\mathcal E_A=\det\begin{pmatrix}
A&\beta&c\\
z^{\mathsf t}&0&0\\
h^{\mathsf t}&0&0
\end{pmatrix}.
\tag{B13}
\]

则同一精确式还可写为

\[
\boxed{p_{n+1}
=d\det A-h^{\mathsf t}\operatorname{adj}(A)c
-9d\,z^{\mathsf t}\operatorname{adj}(A)\beta
+9\mathcal E_A.}
\tag{B14}
\]

核对符号：在det A≠0处，Schur complement给

\[
\mathcal E_A=
\frac{(z^{\mathsf t}\operatorname{adj}A\,\beta)
(h^{\mathsf t}\operatorname{adj}A\,c)
-(z^{\mathsf t}\operatorname{adj}A\,c)
(h^{\mathsf t}\operatorname{adj}A\,\beta)}{\det A}.
\tag{B15}
\]

rank-one更新的adjugate为

\[
\operatorname{adj}(A-9\beta z^{\mathsf t})
=\operatorname{adj}A-
\frac9{\det A}\left[
(z^{\mathsf t}\operatorname{adj}A\,\beta)\operatorname{adj}A
-\operatorname{adj}A\,\beta z^{\mathsf t}\operatorname{adj}A\right].
\]

代入border determinant即得(B14)与(B15)。双方原式均为entries的polynomials，故等式延拓到所有singular A；n=1时(B13)自动为0。actual `p_n(Y)=0` 时使用(B12)/(B14)而不是(B15)的除法。这是完整border恒等式，不是未支付的nonzero递推。

由于(B9)，不能把这些矩阵当作同一固定正Gram operator的nested principal minors，直接外借Sylvester正性或交错谱。即使忽略这一点，(B12)/(B14)在actual点仍含可能取消的完整adjugate与border项；没有已证明的符号或不消失条件让它产生无界nonzero。

## 5. formal满秩、actual谱积与完整primitive账

256已付全period系数为

\[
T_n(g)=\widetilde R_n+16gL_n,\qquad
(L_n)_{r,s}=\begin{cases}8^{-(r-s)}\binom{2(r-s)}{r-s},&r\ge s,\\0,&r<s,\end{cases}
\]

L_n为对角1的下三角Toeplitz，与(B1)的上三角U_n不是同一矩阵。对完整有理heads定义

\[
K_n=-\frac1{16}L_n^{-1}\widetilde R_n\in M_n(\mathbb Q),\qquad
p_n(g)=16^n\det(gI-K_n).
\tag{B16}
\]

故formal polynomial degree恰n、leading恰16^n。它只保证polynomial不是恒零；不保证实际g=Y的值非零，也不保证任意无界子列非零。未证明K_n谱实、交错、目标分离或根距离strict decay。exact border新增的是完整代数接口，没有把formal rank变成actual∞nonzero。

257 primitive稿已完整证明

\[
\widetilde q_H=2^{3\lfloor H/2\rfloor+1}d_{H+1}^2,\quad
\kappa_n=2^{n(n+1)/2},\quad
C_n^{new}(g)=\frac{\widetilde q_{2n-1}^n}{\kappa_n}\Delta_n(g)\in\mathbb Z[g],
\tag{B17}
\]

包括全prefix、所有prime powers、whole-polynomial coefficients；旧整模型的全内容因子是 `[2^{n+1}d_{2n}]^n`。这不是只改善leading，也不是有理行缩放的假saving。设g_n≥1为C_n^{new}的完整content，Π_n为其positive-leading primitive polynomial，则

\[
\Pi_n(Y)=\ell_n\prod_{j=1}^n(Y-\lambda_j(K_n)),\qquad
\ell_n=\frac{\widetilde q_{2n-1}^n}{\kappa_ng_n}(16\cdot2^n)^n.
\tag{B18}
\]

其已付安全leading upper精确为

\[
\log\ell_n\le2n\psi(2n)+
\left(\frac72n^2+\frac32n\right)\log2,
\qquad \psi(m)=\log d_m.
\tag{B19}
\]

按已读稿的标准PNT比较尺度 `ψ(2n)=2n+o(n)`，其leading安全费为 `4+(7/2)log2`。这只是upper，未声称最大primitive content已经计算，或actual费用具有相同lower。

另一方面，actual energy稿的同对象全n估计是

\[
|p_n(Y)|\le M^n n^{n/2}2^{2n-1},\quad
M=16+2\sqrt2\pi\log(1+\sqrt2)+\frac32\pi^2.
\tag{B20}
\]

必须还原 `Δ_n=2^{n²}p_n`，再与(B17)完整费用相乘。因此

\[
|\Pi_n(Y)|\le
\frac{\widetilde q_{2n-1}^n}{\kappa_n}
2^{n^2}M^n n^{n/2}2^{2n-1},
\tag{B21}
\]

即在非零时（零时按log 0=−∞理解）

\[
\log|\Pi_n(Y)|\le2n\psi(2n)+
\left(\frac72n^2-\frac12n-1\right)\log2
+n\log M+\frac n2\log n.
\tag{B22}
\]

比较leading仍是 `4+(7/2)log2>0`。这个正的安全upper不证明真实net指数为正，也不构成actual no-go；它只是没有所需负limsup证书。pure-sector因子不能取代mixed integral，formal满秩与border恒等式也没有弥补actual非零。

若Y=u/v既约有理、v>0，只有在Π_n(Y)≠0时才有 `|Π_n(Y)|≥v^{-n}`。要完成该prototype的数值出口，仍需无界n子列的实际非零以及

\[
\limsup\frac{\log\ell_n+\sum_j\log|Y-\lambda_j(K_n)|}{n^2}<0.
\tag{B23}
\]

本轮这些条件未被证明。256 free-start的generic Chebyshev/sublevel命题也不能排除这个固定Y或其有理假设。

## 6. 有限范围投入决定与执行记录

本稿新增：全部n的mixed alternant合流证据；全node Vandermonde外借失败的明确cross-sector diagonal；完整有理rank-one修改后的border与两种无可逆假设的adjugate恒等式；将257 whole-content定理和actual upper置于同一primitive尺度的精确合账。

保留：完整actual carrier、全prefix指数分母模型及真实宏观内容改善、formal谱模型。未证明：actual无界非零、全部mixed terms的严格能量、最大primitive内容或新数值定理。按256只准入一次257同对象净可行性检验的边界，本257结算停止当前默认prototype投入，不以局部新引理自动续轮，不转入prime/Frobenius/参数/maps/sheetwords或换向量搜索。原总目标仍active；停止一个默认prototype窗口不是所有χ₋₈方法不可能。

本身份只做文档读取、两份NEW257文档保存、最终全文复读及散列。数学程序、finite-n/CAS/区间/prime/参数/map/word扫描、Lean、外Git写和旧producer运行均0。旧256稿、main、policy、manifest与archive未改。本稿由Root另作独立数学核对；尚未发生的审核不记为完成。
