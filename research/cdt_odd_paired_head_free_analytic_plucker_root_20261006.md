# 配对消头行列式的真实解析接口与加权 Plücker 预算

日期：2026-10-06。NEW 纸面证明，root。本文只为原三重零点布局的配对空间建立解析接口，不把恢复四重零点布局的平衡测度预算移给此空间。旧及同行数学 producer 未执行、import 或重跑；本文没有自有数学 producer、数值拟合或 Lean 执行。

## R1. 同一个实际整格、泛函和目标

记 h=3n、r=2n，取

\[
R_n(t)=\frac{(6n)!^2}{(2n)!^3}\frac{S_{2n}(t)^3}{(t)_{6n+1}^2},\qquad
S_{2n}(t)=\prod_{m=1}^{2n}(t-m),\quad f_i(t)=\binom{t-1}{i}.
\tag{R1}
\]

固定 a,b∈Z、b≠0，目标 ξ=aζ(4)+bζ(5)。令 Λ_X 为冻结 arithmetic 稿 A3–A4 的 s=5、B=6、κ=3 有理系数泛函；它在 degree<6n 上定义。令 A_Z 为同轮 integral-lattice 稿 I2 的整数值饱和格，实际基

\[
G_m=p_mL_m+q_mL_{2n+1-m}\quad(1\le m\le n),\qquad
f_{2n},\ldots,f_{3n-1},
\tag{R2}
\]

其中 d_j=(j)_{6n+1}、g_m=gcd(d_m,d_{2n+1-m})、p_m=d_m/g_m、q_m=d_{2n+1-m}/g_m，L_m 是实际整数值 cardinal polynomial。记这些基为 g_1,…,g_r，其 f_i 系数列矩阵为 S∈Mat_{h×r}(Z)。于是

\[
D_{A,n}(X)=\det[\Lambda_X(g_i g_j)]_{i,j=1}^{r}
=\det(S^{\mathsf T}H_n(X)S)\in\mathbf Q[X].
\tag{R3}
\]

这里 H_n(X)_{ij}=Λ_X(f_i f_j)。没有再除一个 first-r factorial；R3 已按真正的整数值格取 determinant。它与 original rank-3n determinant 是不同对象。

X 的系数矩阵为 24 Σ_{j=0}^{6n}W_j ev_{-j}⊗ev_{-j}。W_j>0，任何非零 degree<3n polynomial 不会在全部6n+1个节点消失，所以此矩阵在 A_Z⊗R 上正定。因此 D_A 的次数准确为 r，最高系数正。这只证明 polynomial 非零，不证明每个有理候选的无限次非零求值。

## R2. 正确的右轮廓和完整积分

设 q(z)=πcot(πz)，K(z)=−4a q''(z)−b q'''(z)，c_n=2n+1/2。冻结解析稿 D7/D14 与 lattice 稿 P13–P15 给：对 P,Q∈A_n，原 head correction 为

\[
-b\sum_{m=1}^{2n}R_n'''(m)P(m)Q(m)=0.
\tag{R4}
\]

确切理由是 m 与 m'=2n+1−m 的 factorial numerator 相同、sign 相反，而 P(m)/d_m=P(m')/d_{m'}，Q 亦如此。故实际 ζ 目标处有

\[
\Lambda_\xi(PQ)=\frac1{2\pi i}\int_{c_n-i\infty}^{c_n+i\infty}
R_n(z)K(z)P(z)Q(z)\,dz.
\tag{R5}
\]

这里是实际 ξ 的恒等式；若 ξ=c∈Q 是被反证的候选，才能将同一积分识别为 D_A(c)。任何基多项式 degree≤3n−1，所以 degree(R_n g_i g_j)≤−4。竖线避开全部 poles，K 按 exp(−2π|x|) 衰减。因此以下有限维 Fubini、行列式展开和全直线积分都绝对收敛。

设 z(x)=c_n+ix，复测度 dμ_n(x)=R_n(z(x))K(z(x))dx/(2π)。Heine–Andreief 的有限展开直接给

\[
D_A(\xi)=\frac1{r!}\int_{\mathbf R^r}
\det[g_i(z(x_j))]_{i,j=1}^r{}^2\prod_{j=1}^r d\mu_n(x_j).
\tag{R6}
\]

可以先在有限区间逐项展开，再用上述绝对收敛取极限；不用正性，也没有把 squared determinant 错换成 ordinary rank-r Vandermonde。

## R3. 真实正 Gram 包络不提供目标非零性

令 dν_n=|dμ_n|，以及

\[
M_{ij}=\int_{\mathbf R}f_i(z(x))\overline{f_j(z(x))}\,d\nu_n(x)
\quad(0\le i,j<h).
\tag{R7}
\]

ν_n 是正的有限测度，任意多项式乘积在其下可积。由 R6 的三角不等式及 Hermitian Andreief 恒等式，

\[
\boxed{|D_A(\xi)|\le\det(S^{\mathsf T}M\overline S)=\det(S^{\mathsf T}MS).}
\tag{R8}
\]

M Hermitian positive definite，因为 K 非恒零、R 没有整条直线的零，非零 polynomial 的零有限，故其 norm 严格正；S 的列独立。因此右边严格正。它是 actual complex bilinear determinant 的 upper bound，**其正性不推出左边非零**。例如 rank1 的复/符号测度可有总积分0，但 total-variation Gram>0。

Brown 2026 的正性非零定理要求 real-valued generators 和非负真实积分形式。此处 z(x) 为复点、μ_n 一般不是正测度，因此这些条件未满足。不能以 R7 的人工包络取代原形式并套用其非零结论。

## R4. 精确的 Plücker 支持、加权预算与有限 n 上界

R2 的前 n 列 degree<2n，后 n 列是高 Newton unit vectors。因此在 low-2n/high-n 行块中

\[
S=\begin{pmatrix}A&0\\0&I_n\end{pmatrix},\qquad A\in\operatorname{Mat}_{2n\times n}(\mathbf Z).
\tag{R9}
\]

一个非零 r 阶 Plücker coordinate u_I=det(S_I) 必须含全部 indices 2n,…,3n−1，再取 low indices 0,…,2n−1 中的 n 个。记这些 subsets 为 ℐ_n；其数量为 binom(2n,n)。S 的真实饱和性给所有 u_I 的 gcd 为1，并有

\[
\sum_{I\in\mathcal I_n}|u_I|^2=\det(S^{\mathsf T}S)
=\operatorname{covol}_{N,2}(A_Z)^2.
\tag{R10}
\]

设 V_I(x)=det[f_i(z(x_j))]_{i∈I,1≤j≤r}。矩形 Cauchy–Binet 是确切恒等式

\[
\det[g_i(z(x_j))]=\sum_{I\in\mathcal I_n}u_I V_I(x),
\quad
\frac1{r!}\int|V_I|^2\,d\nu_n^{\otimes r}=\det M_{I,I}.
\tag{R11}
\]

在 L²(ν_n^{⊗r}/r!) 中用 triangle inequality，得到比统一 height 更精确的全 n 界

\[
\boxed{|D_A(\xi)|\le
\left(\sum_{I\in\mathcal I_n}|u_I|\sqrt{\det M_{I,I}}\right)^2.}
\tag{R12}
\]

再用 Cauchy–Schwarz 或 finite maximum，分别得到

\[
|D_A(\xi)|\le\operatorname{covol}_{N,2}(A_Z)^2
\sum_{I\in\mathcal I_n}\det M_{I,I},
\tag{R13}
\]
\[
\log|D_A(\xi)|\le
\max_{I\in\mathcal I_n}\{2\log|u_I|+\log\det M_{I,I}\}
+2\log\binom{2n}{n},
\tag{R14}
\]

zero u_I 省去，D_A(ξ)=0 时按 log0=−∞。组合项是 O(n)，所以真正 n² 主项可以按每个实际 Plücker coordinate 与其解析 minor 配对优化，而不是把最大整格高度与最坏解析 minor 分别最大化后强行相加。

同轮 I13 给 coarse 全尺度费用

\[
\log\operatorname{covol}_{N,2}(A_Z)^2
\le(36\log2-12\log3)n^2+o(n^2).
\tag{R15}
\]

这是 R13 内确实对应原 Newton 系数规范的 upper fee；evaluation 规范的另一个 covolume 不能免费代入。R12–R14 是尚未算出 strict margin 的可执行接口，并非已证衰减指数。

## R5. 为什么 ordinary Vandermonde 与完整 det 预算不能继承

对 I={i_1<…<i_r}，V_I 是 alternating polynomial，故可写为 Δ(z)×一个 symmetric polynomial。因为 f_i 的最高项为 z^i/i!，后者的最高总次数准确为

\[
\sum_{i\in I}i-r(r-1)/2.
\tag{R16}
\]

对 ℐ_n，这个次数介于 n² 与 2n²；其 lower-degree terms 仍在，不声称每项都具有最低次数 n²。于是 R11 中的附加 symmetric factors 可改变 n² 能量，绝不是 fixed kernel 的 O(n) 改动。以 ordinary rank-2n Δ² 直接替换 R6 会漏掉它们。

同时一个 rank-3n positive Gram 的完整 determinant 衰减不控制其 rank-2n minors。简单 diagonal matrices diag(ε,…,ε,1,…,1) 的 full determinant 可任意小，而一个避开 ε 的 smaller minor 等于1。故旧 full-space exponent 或恢复 k=4 布局的新 exponent 都不能作为 R3 的 decay constant。

## R6. 与算术、文献和下一步的准确连接

同轮 integral-lattice 稿 I23–I25 已给 R3 的全 finite-place 安全 minor transfer。那里必须扣掉 largest-r factorial valuations，即两侧 indices n,…,3n−1 的费用；first-r indices 的归一化不属于本对象。R9 的 mandatory high indices 给精细化机会，但 primitive Plücker gcd1 只排除额外格饱和指数，不等于 restricted form 自身不退化。

同轮 auxiliary-prime 稿正在单独研究这一 restricted form 的无限非零条件。负节点 evaluation rank 为 floor(5m/2)，n=2m、p=9m+1，低于 full rank3m；原 unit blocks 无法直接继承。R8 的正 Gram 也不解决此 gate。

Brown 的广义 module-Vandermonde 视角启发 R11–R14，但本文已对这个 unbounded complex contour 用实际收敛条件和有限展开自证所需恒等式；没有直接引用其 compact-positive estimate。其正文 §7.3 只先给 period span dimension≥2，不是自动证明指定数值或任意多项线性无关。Monien 的 discrete Dirichlet Hankel/正系数表示同样没有投影成仅含1与本ξ，不能把其正性与快速衰减替代此接口。

本轮 root 实际阅读范围：Brown arXiv2604.20741v1 PDF1–10、21–24；Saff arXiv1010.3760v1 PDF32–36 §6；Monien arXiv0901.1883v1 PDF1–6；Lai PDF23–25（本轮新增读取3页，累计root1–14、18–25）。三篇新PDF均按正常 TLS 验证归档；保存页数不作为全文阅读页数。完整source hashes、阅读范围与 frozen input pins 另存本轮 NEW receipt。

本轮完成的是实际解析 representation、正 Gram upper bound、准确 Plücker 支持和同一格规范的全 n 费用接口。没有证明 restricted actual determinant 的无限非零、最佳解析能量、strict arithmetic/analytic margin，亦没有新的数值无理性、线性无关性或 Lean 定理。后续可对 R12 的实际 minor 和 u_I 作匹配优化，或改用具备真实正性且有目标投影的新多参数 Mellin packet；不能只增加参数而忽略额外 periods 与全部整模型。
