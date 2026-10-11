# 第256轮：完整目标行列式的关系敏感性与primitive判据

2026-10-10。正式全局回顾的Root数学稿。第255轮已完成真实新nativeQ全数组投影与全尺度目标秩；本稿不将该秩当作实际目标处的非零。对象固定为a=1/√2、参数+1单圈T、3+T、N(i,j)=a^i(3+T)M(i,j)、整数接触prototype及选列j=2s。不改参数、向量或sheet。

## 1. 同一完整数组的自由start差

设Y=L(2,χ−8)。第255轮全数组分解

\[
N(i,j)=R_{ij}+16Y a^{i-j}c_{(i-j)/2}
+\frac32\pi^2a^{i-j+1}c_{(j-i-1)/2},\qquad R_{ij}\in Q
\]

含全部finite heads，c非法指标为0。仅把这个明确分解的Y-start换成任意g，记N^[g]，不把它声明为同一个canonical contour的值。作为0附近双变量芽，B提出而Root独立核对：

\[
\boxed{\ \sum_{i,j\ge0}(N^{[g]}(i,j)-N^{[Y]}(i,j))z^iw^j
=\frac{16(g-Y)}{(1-zw)\sqrt{1-z^2/2}}.\ }
\tag{S1}
\]

证明非零项恰i=j+2l，a^{2l}=2^{−l}，再用Σc_lx^l=(1−x)^−1/2。两个求和在充分小闭双圆盘绝对收敛。此式包括全部indices，不是低区row-add；清整和目标系数秩对其它g亦有形式版本，而实际同contour能量不可因此外借。

## 2. 精确谱模型

固定n≥1，r,s=0,…,n−1，令

\[
P_r=2^nx^{2r},\quad D_r=\operatorname{jet}_{<2n}\frac{xP_r}{\sqrt{1-2x^2}},
\qquad F_{r,s}(g)=N^{[g]}(P_r,2s)-9Z(D_r,2s).
\]

完整接触消π²，故F_n(g)=R_n+gB_n，R_n有理矩阵。其目标系数矩阵为

\[
B_n=16\cdot2^n L_n,\qquad
(L_n)_{r,s}=\begin{cases}8^{-(r-s)}\binom{2(r-s)}{r-s},&r\ge s,\\0,&r<s.\end{cases}
\tag{S2}
\]

L_n是对角1的下三角Toeplitz矩阵。其inverse的系数由sqrt(1−z/2)给出：d0=1，d_l=−binom(2l,l)/(8^l(2l−1))，l≥1。有限Toeplitz卷积仍精确，detL_n=1。因此

\[
K_n=-\frac1{16\cdot2^n}L_n^{-1}R_n\in M_n(Q),\quad
\Delta_n(g)=\det F_n(g)=(16\cdot2^n)^n\det(gI-K_n).
\tag{S3}
\]

这是完整实际对象的换写，未截R_n、未丢finite heads；λ_j(K_n)可复数并按重数计。未证明该矩阵正、谱实、谱点与Y分离或接近。

## 3. 关系盲uniform二次能量不能成立

先剥除已知P_r的共同2^n行倍数：q_n(g)=2^{−n²}Δ_n(g)。这只是为了陈述规范化不依赖的代数事实，不领免费的算术内容。q_n的degree恰n，leading coefficient16^n。

对任何固定ε>0、任何中心g0∈R，Chebyshev交错法自含给

\[
\sup_{|g-g_0|\le\varepsilon}|q_n(g)|
\ge\frac{16^n\varepsilon^n}{2^{n-1}}=2(8\varepsilon)^n.
\tag{S4}
\]

证明T_n的leading coefficient为2^{n−1}（n≥1，n=1同式），在[−1,1]的n+1个标准极值点交错±1。若sup严格小于右侧，将q_n减去具有同leading coefficient的倍数T_n((g−g0)/ε)，所得degree≤n−1却在这些点间有n次变号，矛盾。等号以极限处理。

故对任何γ>0，不可能在一个固定非退化g区间上uniform有|q_n(g)|≤exp(−γn²+o(n²))。这是一个确定的whole-polynomial障碍，不是actualY处大小的下界，也不排除target-specific strict energy。

还有不借Remez定理的更精确sublevel证据。由(S3)，q_n(g)=16^n∏(g−λ_j)。若|q_n(g)|≤e^{−γn²}，则至少一个|g−λ_j|≤e^{−γn}/16，否则乘积严格更大。根可以非实，实轴与半径r的复圆盘交集长度至多2r。因此

\[
\operatorname{meas}\{g\in R:|q_n(g)|\le e^{-\gamma n^2}\}
\le\frac n8e^{-\gamma n}.
\tag{S5}
\]

这些长度可和，故对Lebesgue几乎所有固定实g，该小量事件仅发生有限次。证明只需尾并集长度≤尾和→0。它对有理数集合不提供排除：有理数本身measure0，不能把almost-everywhere结论偷换成所有有理g。尤其它未证明Y无理。

## 4. 真正的primitive数值判据

令t_n>0为唯一有理数，使P_n(T)=t_nΔ_n(T)成为positive-leading的primitive Z[T]多项式，记ℓ_n=t_n(16·2^n)^n∈Z_{>0}。于是

\[
\boxed{\ P_n(Y)=\ell_n\prod_{j=1}^n(Y-\lambda_j(K_n)).\ }
\tag{S6}
\]

同一个det进行任意非零有理行/列/整体常数缩放，只乘一个非零有理常数，primitive P_n完全不变（若不规范正号，则至多差号）。所以去掉2^n、选择行单位或消一个人工共同分母，本身不创造primitive净收益。

若Y=u/v既约、v>0，P_n(Y)≠0，则v^nP_n(Y)为非零整数，故|P_n(Y)|≥v^{−n}。若能在一个无界n子列同时证明P_n(Y)≠0与

\[
\limsup\frac1{n^2}\left(\log\ell_n+\sum_{j=1}^n\log|Y-\lambda_j(K_n)|\right)<0,
\tag{S7}
\]

即矛盾，得到Y无理。这是明确充分判据，不是已满足的定理。actual∞nonzero和同对象strict两个条件都不能由(S2)满秩领到。

本轮完整Z-prefix会给ℓ_n的安全upper和一些确切共同内容；它不支付(S7)。如果未来能量证书只在generic自由g上uniform成立，须先面对(S4)。真正首证书必须来自actualY的完整两sheet积分或同一谱积，包含所有行尺度及完整primitive内容。

## 5. 正式回顾后的唯一有界任务

若本轮actual共同生成芽/contour和logq_H=O(H)的全prefixZ模型通过，第257轮只作一次同一prototype的target-specific净能量可行性检验：完整两sheet表示/实际谱积与全primitive费用同尺度比较。可以新增足够强全局内容恒等式或同对象严格能量，但不先开prime/Frobenius/参数/sheet优化前线。若只能得到局部秩或沿用同一不够的safe-upper，结束该默认prototype窗口，保留全carrier资产；不宣告所有χ−8方法不可能。

formal256完成后计数0、下一260、最迟264；连续两轮核心停滞提前回顾。没有新数值无理性、线性无关性或Lean认证。原总目标active。
