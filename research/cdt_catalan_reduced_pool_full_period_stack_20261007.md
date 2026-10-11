# Catalan 二阶 jet 缩小列池的完整实际周期 stack

2026-10-07。固定 P21 的 \(m=8N+1\) 行与 P15 的 \(m\) 列，不改混合积分或真实 Chebyshev 配对。本稿完整生成剩余周期系数，证明一个对所有 \(N\ge1\) 有效的新障碍：真实 \(T_1\) 系数矩阵的 rank 至少 \(m-1=8N\)，所以整个单目标认证核至多一维；当前 \(m\times m\) 版本 H29 不可能成功。对 \(N=1,2\)，全部系数的精确有理数重建给出认证核为零、目标像为零。一般 \(N\) 的核是否也为零仍未证明。本稿不给出新的数值无理性、线性无关性或形式化验证结论。

## 1. 真实对象、已证身份与认证范围

实际全文读 [higher-jet 稿](cdt_catalan_higher_jet_holonomy_bridge_20261007.md) H1–H30、[全列池稿](cdt_catalan_jet_pool_projection_rank_20261007.md) P1–P28/P9a–P9d，以及 [真实边界求值稿](cdt_catalan_jet_boundary_evaluation_20261007.md) O1–O26。沿用

\[
f(t)=\sqrt{1-t^2},\quad a(t)=\operatorname{artanh}t,\quad
b=7N,\ q=4N,\ h=2N,\ A=19N,\ C=63N,\ H=65N,
\]
\[
K=8N,\quad m=K+1,\quad d_*=44N-1.
\tag{R1}
\]

真实参数积分及缩小行列为

\[
M_z(u,j)=\int_{-1}^1\int_0^1
\frac{|t|t^u s^j e^{za(t)}}{f(t)(1-ts)}\,ds\,dt,\qquad
Z_z(u,j)=\int_0^1\int_0^1
\frac{t^u s^j e^{za(t)}}{1-ts}\,ds\,dt,
\]
\[
P_i(t)=(1-t)^{2N}t^{19N+i},\qquad
v_k(s)=s^{7N+k}(1-s)^{4N},\quad 0\le i,k\le K.
\tag{R2}
\]

\(D_i\) 必须是给出 \(P_i\) 的同一个原 Chebyshev 行组合，不能另选只满足低阶 contact 的多项式。以下矩阵正是

\[
F_N(i,k)=\frac13[z^2]M_z(P_i,v_k)
-\frac12[z^2]Z_z(D_i,v_k).
\tag{R3}
\]

记 \(T=M_z(0,0)\)、\(U=M_z(0,1)\)、\(V=Z_z(0,0)\)、\(W=Z_z(1,0)\)、\(X=Z_z(0,1)\)，并用未正规化 Hasse jets \(T_1=[z]T,\ W_1=[z]W,\ W_2=[z^2]W\)。已证身份包括

\[
T_0=4G,\quad T_2=12\beta(4),\quad
U_0=\tfrac32V_0,\quad V_0=\zeta(2)=2\eta(2),\quad
W_0=X_0=1.
\tag{R4}
\]

最后一条也直接由
\(Z_0(1,0)=\sum_{\nu\ge0}((\nu+2)(\nu+1))^{-1}=1\)
及 \(Z_0\) 的两变量对称性得到。记 \(\eta_1=\eta(1)=\log2,\ \eta_2=\eta(2)\)。

O6 已给出真实 \(\Omega=([z^2]U-\tfrac32[z^2]V)/3\) 的 weight-four MPL 身份。本稿不遗漏该身份：P15 已使其完整系数严格为零，所以用 O6 替换 \(\Omega\) 后，各个新 MPL/ζ-product 的该项系数仍为零。其余真实 seed 不能由这条身份自动消去。

所有系数计算只使用已证明的真实身份。其余数值保留为生成元，**不假定数值线性无关**；将它们的形式系数置零是一个充分的周期认证方法。下文也完整代入本轮新 seed 表；障碍针对这个已固定、未追加未知周期降深身份的认证模型，不能解释为所有可能数值消元方法的必要障碍。

## 2. 同一 Chebyshev 组合的完整 \(D_i\)

令 \(c_\ell=4^{-\ell}\binom{2\ell}{\ell}\)。有精确多项式身份

\[
\boxed{\quad
D_i(t)=(1-t)^{2N}t^{19N+i+1}
\sum_{\ell=0}^{L_i}c_\ell t^{2\ell},\qquad
L_i=\left\lfloor\frac{d_*-i-1}{2}\right\rfloor .
\quad}
\tag{R5}
\]

证明：令 \(x=1/t\)，将 \(x^{d_*-i}\) 按 P25 展开成 \(T_d(x)\) 的非负有理组合；对应 \(D\) 是同一系数的 \(U_{d-1}(x)\) 组合，\(T_0\) 对应零。对 \(d\ge1\)，
\(T_d(x)/\sqrt{x^2-1}-U_{d-1}(x)\)
在 \(x=\infty\) 的 Laurent 展开只有负幂：写
\(w=x+\sqrt{x^2-1}\)，差为 \(w^{-d}/\sqrt{x^2-1}\)。
\(T_0/\sqrt{x^2-1}\) 也没有多项式部分。故这个同系数组合就是
\(x^{d_*-i}/\sqrt{x^2-1}\)
的多项式部分，即
\(\sum_{\ell=0}^{L_i}c_\ell x^{d_*-i-1-2\ell}\)。
乘原行因子 \((1-t)^{2N}t^{C-1}\) 得 R5。

特别地

\[
\operatorname{ord}_0P_i=A+i,\qquad
\operatorname{ord}_0D_i=A+i+1,\qquad
\deg D_i\le H-1,\qquad \deg v_k\le A.
\tag{R6}
\]

所以 R3 每个 \(M_z(u,j)\) 都满足 \(u\ge j\)，每个 \(Z_z(u,j)\) 都满足 \(u>j\)。只访问 **minus boundary**；所有 plus-boundary 的 \(U/X\) jets 实际系数均为零。这是完整多项式比较，不只是低阶 contact 比较。

## 3. 完整剩余周期的可审查生成公式

在 \(z^3=0\) 的 Hasse-jet 计算中，完整外矩起点是

\[
\mu_{-1}=4Gz,\qquad \mu_0=2+4Gz^2,\qquad
B_0=1+\eta_1z+\tfrac12\eta_2z^2,\qquad
B_1=(1+zB_0)/2,
\]
\[
(i+1)\mu_i=i\mu_{i-2}+z\mu_{i-1}\quad(i\ge1),\qquad
(i+1)B_i=(i-1)B_{i-2}+zB_{i-1}\quad(i\ge2).
\tag{R7}
\]

这里 \(\mu_{-1}\) 的表达来自 H6–H7 的真实
\(A_0(z)-A_0(-z)\)：到二阶只留 \(4Gz\)，没有额外 \(\pi\) 或 \(\beta(3)\) 项。归纳可见所有 \(\mu_i\) 到二阶只含 \(1,G\)。

完整 minus seeds 和递推为

\[
K_0=4G+T_1z+12\beta(4)z^2,\qquad
K_1=zK_0+\mu_{-1}+\mu_0,
\]
\[
dK_d=(d-1)K_{d-2}+zK_{d-1}+\mu_{d-2}+\mu_{d-1}\quad(d\ge2),
\]
\[
L_0=V_0+V_1z+V_2z^2,\qquad
L_1=1+W_1z+W_2z^2,
\]
\[
dL_d=(d-2)L_{d-2}+zL_{d-1}+B_{d-2}+B_{d-1}\quad(d\ge2).
\tag{R8}
\]

R8 在此仍完整保留 \(V_1,V_2\)；但 \(d=2\) 时 \(d-2=0\)，所以所有 \(L_d,\ d\ge1\) 都完全不依赖 \(L_0\)。由 R6，R3 不访问 \(d=0\) 的 Z boundary，因此 **\(V_0,V_1,V_2\) 的全部系数也为零**。这并不是把 V jets 假定有理。

对 \(u\ge j\)，真实 diagonal reductions 是

\[
M_z(u,j)=K_{u-j}-\sum_{r=0}^{j-1}
\frac{\mu_{u-j+r}}{r+1},\qquad
Z_z(u,j)=L_{u-j}-\sum_{r=0}^{j-1}
\frac{B_{u-j+r}}{r+1}.
\tag{R9}
\]

它们由真实 diagonal shift 沿 \((u-j,0)\) 到 \((u,j)\) 逐步相加得到，空和为零。定义

\[
p_i(u)=(-1)^{u-A-i}\binom{2N}{u-A-i}
\quad(A+i\le u\le A+i+2N),
\]
\[
v_k(j)=(-1)^{j-b-k}\binom{4N}{j-b-k}
\quad(b+k\le j\le b+k+4N),\qquad d_i(u)=[t^u]D_i .
\tag{R10}
\]

未显示范围内取零。于是全部有限矩阵由同一个公式生成：

\[
\begin{aligned}
F_N(i,k)={}&\frac13\sum_{u,j}p_i(u)v_k(j)
[z^2]\left(K_{u-j}-\sum_{r<j}\frac{\mu_{u-j+r}}{r+1}\right)\\
&-\frac12\sum_{u,j}d_i(u)v_k(j)
[z^2]\left(L_{u-j}-\sum_{r<j}\frac{B_{u-j+r}}{r+1}\right).
\end{aligned}
\tag{R11}
\]

R5/R7–R11 无歧义生成 **全部** 剩余周期系数；\(u\le H-1\) 足以界定计算范围，所有分母来自这些显示的有理数递推与二项式系数。最终完整表示是

\[
\boxed{\quad
F_N=C_0+GC_G+\beta(4)C_4+T_1C_{T_1}
+\eta_1C_{\eta_1}+\eta_2C_{\eta_2}+W_1C_{W_1}+W_2C_{W_2}.
\quad}
\tag{R12}
\]

它没有删掉一个尚非零的 \(U/V/W/X\) lower jet；U/X 因 R6 没有分支入口，V 因 R8 的截断没有传播，\(W_0=1\) 已并入 \(C_0\)。M/Z 原完整有限 module 中的其他生成元到二阶也都通过 R7/R4 得到零系数或已有身份。R12 不宣称是数值最小基。

随后实际全文读 [新实际 seed 稿](cdt_catalan_actual_seed_relations_20261007.md) 全7节/R1–R24。其已证身份为
\(T_1=8\beta(3)-4G\log2+4\mathcal C\)、
\(W_1=\log2+\zeta(2)/2-(\log2)^2/2\)、
\(W_2=13\zeta(3)/16+\zeta(2)(1-\log2)/4\)，
其中 \(\mathcal C=-\Im(\mathcal L_{2,1}(i,1)+\mathcal L_{2,1}(i,-1))\) 是该稿定义的实际绝对收敛 MPL 值。
令 \(l=\log2\)，将它们和 \(\eta_2=\zeta(2)/2\) **实际代入** R12，得到新十五项生成系统中的完整缩小表示（四项系数为零）：

\[
\begin{aligned}
F_N={}&C_0+GC_G+\beta(4)C_4
+8\beta(3)C_{T_1}-4GlC_{T_1}+4\mathcal C C_{T_1}\\
&+l(C_{\eta_1}+C_{W_1})
+\zeta(2)(C_{\eta_2}/2+C_{W_1}/2+C_{W_2}/4)\\
&+\tfrac{13}{16}\zeta(3)C_{W_2}
-\tfrac12 l^2 C_{W_1}-\tfrac14\zeta(2)l C_{W_2}.
\end{aligned}
\tag{R12a}
\]

\(\zeta(4),\zeta(3)l,\mathcal A,\mathcal B\) 在当前缩小模型中系数均为零；它们原来只来自已经零系数的 U/V jets。特别是 \(\mathcal C\) 只来自 \(T_1\)，所以 \(C_{\mathcal C}=4C_{T_1}\)。新固定生成系统逐项消除的单目标认证核，恰等于下文 R19 的核：新 \(\mathcal C,\zeta(3),l^2\) 三项分别强迫 \(C_{T_1}v=C_{W_2}v=C_{W_1}v=0\)，随后新 \(l,\zeta(2)\) 两项分别强迫旧 \(C_{\eta_1}v=C_{\eta_2}v=0\)；反向直接代入亦成立。此为形式系数的严格代数比较，无需假定这十五个实际数值独立。因此 R16–R22 的 rank/核障碍在新实际 seed 关系代入后仍然成立。

## 4. 一个全 \(N\) 的高秩真实干扰：\(T_1\)

令 \(h(x,z)=(1-x^2)^{-1/2}e^{za(x)}\)，并定义

\[
a_d=[z][x^d]h(x,z)=
\begin{cases}
\displaystyle\sum_{\ell=0}^{(d-1)/2}\frac{c_\ell}{d-2\ell},&d\text{ 奇},\\
0,&d\text{ 偶}.
\end{cases}
\tag{R13}
\]

对 \(d\ge0\)，H26 的 moment 身份及偶数两边都为零给

\[
a_d=\frac1\pi\int_{-1}^1\frac{t^d a(t)}{f(t)}\,dt.
\tag{R14}
\]

\(T_1\) 在 R8 的 M 齐次传播中只乘 \(h\)，故其二阶系数是 \(a_d\)；外矩和 Z 不含 \(T_1\)。反转列 \(k=K-j\) 后得到完整闭式

\[
\boxed{\quad
\widehat C_{T_1}(i,j)
=C_{T_1}(i,K-j)
=\frac1{3\pi}\int_{-1}^1
\frac{(1-t)^{6N}t^{i+j}a(t)}{f(t)}\,dt
=\frac13\sum_{e=0}^{6N}(-1)^e\binom{6N}{e}a_{i+j+e}.
\quad}
\tag{R15}
\]

这不是一个正 Gram，不能因 \(a(t)\) 在正半轴为正就声称它正定。正确的全 \(N\) 定理为

\[
\boxed{\quad
\operatorname{rank}_{\mathbb Q}C_{T_1}\ge m-1=8N.
\quad}
\tag{R16}
\]

证明：在 \(t=0\) 以连续值1定义 \(a(t)/t\)，令

\[
d\nu_N(t)=\frac{(1-t)^{6N}}{3\pi f(t)}
\frac{a(t)}t\,dt .
\tag{R17}
\]

这是 \((-1,1)\) 上严格正、具有所有有限矩、无限支撑的 measure。端点 logarithm 与 \(f^{-1}\) 的乘积可积。R15 等于
\(\int t^{i+j+1}d\nu_N\)。将次数 \(\le K\) 的 monomial basis 换成该正 measure 的正交正规基 \(p_0,\ldots,p_K\)，该矩阵合同于压缩乘法算子 \(Q\mapsto tQ\) 的 Jacobi 矩阵 \(J_N\)。

具体地，次数及正交性使 \(J_N\) 对称三对角；相邻项
\(\int tp_jp_{j+1}d\nu_N\) 是两个正 leading coefficients 的比，严格正。若 \(J_Nx=0\)，第一行确定 \(x_1\) 为 \(x_0\) 的倍数，随后每行用非零相邻项确定下一个分量；若 \(x_0=0\)，全部分量为零。所以 \(\dim\ker J_N\le1\)。合同和列反转不改变 rank，且 R13–R15 条目均有理，实 rank 与有理 rank 一致，得 R16。

更精确地，令 \(\pi_m\) 为 \(\nu_N\) 的次数 \(m\) monic orthogonal polynomial，三项递推的 determinant 展开给
\(\det(\lambda I-J_N)=\pi_m(\lambda)\)。因此

\[
C_{T_1}\text{ 可逆}\quad\Longleftrightarrow\quad \pi_m(0)\ne0.
\tag{R18}
\]

本稿**没有证明 R18 右侧对所有 \(N\) 成立**；测得 \(N=1,2\) 成立不能代替该一般证明。

## 5. 完整 stack 与目标像：一般结论和有限证书

对 \(\theta=\beta(4)-G/3\)，先把 R12 改写为
\(C_0+\theta C_4+G(C_G+C_4/3)+\cdots\)。完整坏系数 stack 是

\[
B_N=
\begin{pmatrix}
C_G+C_4/3\\ C_{T_1}\\ C_{\eta_1}\\ C_{\eta_2}\\ C_{W_1}\\ C_{W_2}
\end{pmatrix},\qquad
\mathcal K_N=\ker_{\mathbb Q}B_N\subset\mathbb Q^m .
\tag{R19}
\]

所有 R19 columns 都是 P15 所给实际 allowed endpoint 核基中的坐标。由 R16，

\[
\boxed{\quad
\dim_{\mathbb Q}\mathcal K_N\le1\qquad(N\ge1).
\quad}
\tag{R20}
\]

P24 已证明同一 \(C_4\) 可逆；因此 \(C_4|_{\mathcal K_N}\) 单射，目标像 rank 恰为 \(\dim\mathcal K_N\)，只能为0或1。也可按 P19 精确计算

\[
\operatorname{rank}(C_4|_{\mathcal K_N})
=\operatorname{rank}\begin{pmatrix}B_N\\C_4\end{pmatrix}
-\operatorname{rank}B_N=m-\operatorname{rank}B_N.
\tag{R21}
\]

R20 已足够排除当前 \(m\times m\) 版本 H29：\(m=8N+1\ge9\)，认证核不可能提供 \(m\) 个独立列。一个非零 determinant 也至少需要 \(m\) 个独立输入 columns，因此不是只对 target coefficient leading term 的障碍。R20 不排除重建规模为1的对象，也不排除以后用新实际 seed 身份更改 R19。

新内联 Fraction 程序从 R5/R7–R11 重建 \(N=1,2\) 的全部8种完整有理系数矩阵。固定素数 \(p=1000003\)，全部计算后的有理分母均为 \(p\)-units。下表给出**反转列之后**各矩阵行列式的非零模 \(p\) 值：

| coefficient | \(N=1,\ m=9\) | \(N=2,\ m=17\) |
|---|---:|---:|
| \(C_0\) | 756222 | 356552 |
| \(C_G\) | 258665 | 751030 |
| \(C_4\) | 933313 | 702257 |
| \(C_{T_1}\) | 77590 | 486160 |
| \(C_{\eta_1}\) | 159518 | 432880 |
| \(C_{\eta_2}\) | 936937 | 875227 |
| \(C_{W_1}\) | 798870 | 627195 |
| \(C_{W_2}\) | 957110 | 92560 |
| \(C_G+C_4/3\) | 354523 | 177706 |

\[
\boxed{\quad
\mathcal K_1=\mathcal K_2=0,\qquad
\operatorname{rank}(C_4|_{\mathcal K_1})
=\operatorname{rank}(C_4|_{\mathcal K_2})=0 .
\quad}
\tag{R22}
\]

完整 stack 的有限域 rank 分别为9、17。模素数非零 determinant 是有限有理矩阵的非零证书：条目分母为 units，所以有理 determinant 为零会迫使 reduction 为零。上表不是一般 \(N\) 的经验性费用或无理性论据，也不宣称这些实际周期数值独立。

另一个独立闭式程序只由 R13/R15 重建整个 \(T_1\) 矩阵，复得两个相同的 determinant residues；并精确计算其有理 determinant，\(N=1\) 为正（分子154 bit、分母255 bit），\(N=2\) 为负（分子734 bit、分母1087 bit）。符号变化特别说明这里不能套用正 Gram 理由。可直接用于再核的首条目是
\(\widehat C_{T_1}(0,0)=-1627/180\) 和 \(-46522243/95040\)。

## 6. 另两种真实 W 干扰的闭式，而非漏掉 lower jets

R8 的 \(W\)-齐次传播生成函数严格为

\[
g(x,z)=\sum_{d\ge1}\operatorname{coeff}_W(L_d)x^d
=\frac{e^{za(x)}-1}{z}.
\tag{R23}
\]

右式在 \(z=0\) 可去。求导得
\((1-x^2)g'=1+zg\)，其 Taylor 系数正是
\(g_1=1,\ d g_d=(d-2)g_{d-2}+zg_{d-1}\)，因此 R23 包含完整齐次递推，不能把它与 M 的 \(h\) 传播混用。

令 \(S_i(t)=\sum_{\ell=0}^{L_i}c_\ell t^{2\ell}\)；R23 的 \(W_2\) 系数为
\([x^d]a(x)=[d\text{ 奇}]/d=\tfrac12\int_{-1}^1t^{d-1}dt\)。
同一 \(W_1\) 系数为 \([x^d]a(x)^2/2\)，并满足
\([x^d]a(x)^2/2=\tfrac12\int_{-1}^1t^{d-1}a(t)dt\)：
奇数 \(d\) 两边都为零，\(d=2l\) 时两边都等于
\((2l)^{-1}\sum_{r=0}^{l-1}(2r+1)^{-1}\)，可由 artanh 幂级数逐项积分验证。

利用 R5/R10，反转列的完整系数为

\[
\boxed{\begin{aligned}
\widehat C_{W_2}(i,j)
&=-\frac14\int_{-1}^1(1-t)^{6N}t^{i+j}S_i(t)\,dt,\\
\widehat C_{W_1}(i,j)
&=-\frac14\int_{-1}^1(1-t)^{6N}t^{i+j}S_i(t)a(t)\,dt .
\end{aligned}}
\tag{R24}
\]

这些式子有所有 matching \(D_i\) 的 Taylor 截断，不能把 \(S_i\) 免费换成 \(f^{-1}\)。特别是 \(S_i\) 随行改变，第一式也不能自动称为对称正 Gram。初次完整 Fraction 程序另由 R24 第一式的有理 moments 重建 \(N=1,2\) 全部 \(W_2\) 条目，逐分数与 R11 一致。R24 没有单独证明这两个矩阵对所有 \(N\) 可逆。

## 7. 一个确实绕开 \(T_1\) 的行列改动

R15 的根源是 signed measure \(a(t)/f(t)\)。可以利用 parity 构造新的、仍处于原实际 P-span 与 endpoint 核中的子池，保留 target Gram 并精确消去这一项。对 \(0\le a,b\le2N\)，选

\[
P'_a(t)=(1-t^2)^{2N}t^{19N+2a},\qquad
v'_b(s)=s^{11N-2b}(1-s^2)^{4N}.
\tag{R25}
\]

P′ 属于 P20：
除去原 \((1-t)^{2N}t^{19N}\) 后为
\(t^{2a}(1+t)^{2N}\)，次数 \(\le6N<d_*\)。
v′ 属于 P15 的 allowed column 空间：
除去 \(s^{7N}(1-s)^{4N}\) 后为
\(s^{4N-2b}(1+s)^{4N}\)，次数 \(\le8N\)。
且 \(\deg v'_b\le19N\)，故原 \(\Omega\) 系数仍为零。必须取给出 P′ 的同一个原 Chebyshev 行组合的 \(D'_a\)；本稿没有替换它。

最高 T2 和 lower T1 都只看 P′，相同的非负指数 moment 计算给

\[
C'_{T_1}(a,b)=\frac1{3\pi}\int_{-1}^1
(1-t^2)^{6N-1/2}t^{2a+2b}a(t)\,dt=0,
\]
\[
\boxed{\quad
C'_4(a,b)=\frac4\pi\int_{-1}^1
(1-t^2)^{6N-1/2}t^{2a+2b}\,dt
\text{ 严格正定，rank }2N+1.
\quad}
\tag{R26}
\]

第一式是严格奇函数积分；第二式对非零 \(Q\) 给
\(\int Q(t^2)^2(1-t^2)^{6N-1/2}dt>0\)。
所以这确实给出一条有实际 coefficient 支持的模型改进，尚没有把其余五种 nuisance 消掉。

尤其 \(D'_a\) 一般是 R5 行的真实有限组合；
\((1+t)^{2N}\) 与行依赖 cutoff 不交换。不能从 P′ 为偶 filter 就断言 \(D'_a\) 也有同样 parity，更不能声称 R24 的 \(W_1\) 同时消掉。下一步应在 R25 模型中重新应用 R7–R11，计算 \(G+C'_4/3,\eta_1,\eta_2,W_1,W_2\) 的完整 stack；若再成功才有 H28/H29 的新输入。另一路是求出 W/T1 的真实 period 身份并在原完整表示中合并，不能先假定其为已有目标。

整高度也能显示支付：把每个 P′ 对应的非负 Chebyshev 系数统一乘 \(2^{d_*}\)，得到整原行组合；系数 \(\ell^1\) 高度为 \(2^{d_*+2N}\)，因为 \(t^{2a}(1+t)^{2N}\) 的系数和为 \(2^{2N}\)，每个归一化 monomial-to-Chebyshev 展开系数和为1。v′ 的整数系数 \(\ell^1\) 高度为 \(2^{4N}\)。本稿只给输入组合高度，没有为该新模型建立完整 determinant energy、全素数最优内容、非零性或 strict holonomy ratio。

## 8. 结论、验证记录与尚待审查范围

本轮的全 \(N\) 结论是 R5/R12 的完整实际模型和 R16/R20 的 rank/认证核上界；当前固定 \(m\times m\) 单目标列投影失败。有限 \(N=1,2\) 的 R22 给完整认证核严格为零。R25–R26 是一条明确的新行列方向：精确消 \(T_1\)、保留正定 target coefficient，但其余 seed 尚未消除。R18 的一般非零、全 \(N\) stack 零核、新子池完整算术/解析比较，都没有被称为已证。

本稿使用4次全新内联数学调用：
一次 Fraction 完整重建两个有限模型及 W2 闭式逐条比较；
一次只为判断 signed-Gram 一般猜测是否可靠的 Jacobi/三阶符号探测；
一次独立 T1 闭式核算因符号库 fmpq 返回类型读取错误结束；
修正该返回类型后一次调用完成独立 T1 全矩阵、mod determinant 与精确 determinant 的核算。
最后两次中的错误没有数学结果被采用。没有运行旧 producer、guard、620、prime table、旧研究脚本、Lean；没有新增 PDF、网页或数值拟合。有限计算结果与全 \(N\) 纸面定理分开标注。

实际全文读三份指定 H/P/O 输入，以及新实际 seed 稿全部7节/R1–R24；当前 H/P 又分别完整回读以核对真实递推和 normalization。R12a 是实际纸面 substitution，不另声称新十五项完整系数全部再次执行机器重建。源仓库只读文件无新增访问、Git 操作或改动。本稿是唯一新保存的数学文件，不修改父任务进展稿或其他作者稿。

root 已实际全文读本稿全部8节/R1–R26，独立重核同 Chebyshev polynomial-part 的完整 D、minus-only 入口与 d=2 截断、Jacobi 不可约合同的 rank≥m−1、R24 两种 W moment 与 matching cutoff、R25–R26 的指数/正 Gram，明确纸面数学 PASS。审读后依其建议加入已全文读取的新 seed 身份实际代入 R12a，及其认证核等价说明；root 随后实际读取 R12a 整段，逐项独立核对全部11个非零系数及新旧认证核等价，补审 PASS。

root 另以1段全新内联 Fraction 程序仅从 R13/R15 的闭式、独立于作者完整递推程序，重建 \(N=1,2\) 的全部 \(T_1\) 矩阵：模 \(1000003\) 的 determinant 分别为 \(77590,486160\)，首条目分别为 \(-1627/180,-46522243/95040\)，与上文逐项证书一致。root 未重复计算其余系数矩阵或完整 stack；这些有限全 stack 结果仍准确标注为作者的完整精确重建，不能把纸审或单个 \(T_1\) 复核称为全 stack 程序重复。作者收讫以上实际审查记录后完成最终全文回读并报告 bytes/SHA。未有新的数值无理性或 LI 定理，未有形式化验证。

