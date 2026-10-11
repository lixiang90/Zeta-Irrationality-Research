# 二阶 outer-log 的真实 Chebyshev 全列池：边界核、缩小模型与目标秩

2026-10-07。本稿固定原 Catalan 论文的实际 Chebyshev/contact 行列池，取最小新 jet 阶数 \(\ell=2\)，目标为 \(\theta=\beta(4)-G/3\)。得到一个可以完全计算的最高边界周期核：原 raw pool 中其秩是 \(40N-1\)，整核恰为低次数坐标；加入原 endpoint filter 后只剩 \(8N+1\) 个可用方向。由此，上一稿 H28/H29 的周期认证投影不能在原 \(48N\) 行规模上成功。另一方面，缩小到 \(8N+1\) 行列后，可以显式保留满秩的已标识 \(\beta(4)\) 系数，且行列变换高度可支付。尚未消除其余实际周期，也没有新的数值无理性或线性无关性定理。

## 1. 固定对象与证明范围

实际全文读 [higher-jet 稿](cdt_catalan_higher_jet_holonomy_bridge_20261007.md) H1–H30，以及源仓库 Catalan `build/sections/foundations.tex` 全部434行。沿用其参数

\[
n=48N,\quad b=7N,\quad q=g=4N,\quad h=2N,
\quad L=59N,\quad C=63N,\quad H=65N,\quad A=19N.
\tag{P1}
\]

令 \(f(t)=\sqrt{1-t^2}\)，\(a(t)=\operatorname{artanh}t\)，\(d_*:=n-1-g=44N-1\)。原整数行是

\[
P_r=(1-t)^h t^{C-1}T_{|r-g|}(1/t),\qquad
D_r=\operatorname{sgn}(r-g)(1-t)^h t^{C-1}U_{|r-g|-1}(1/t),
\tag{P2}
\]

\(0\le r<n\)，且 \(D_g=0\)。原 contact 是

\[
\frac{tP_r}{f}-D_r=O(t^L).
\tag{P3}
\]

取上一稿真实参数积分 \(M_z,Z_z\)，并设

\[
M^{(2)}=\frac{[z^2]M_z}{3},\quad Z^{(2)}=\frac{[z^2]Z_z}{3},
\quad F_j(r)=M^{(2)}(P_r,j)-\frac32 Z^{(2)}(D_r,j),
\quad b\le j<L.
\tag{P4}
\]

raw pool 是 \(R=L-b=52N\) 列。允许的原 endpoint 列空间为

\[
W_N=\{s^b(1-s)^q Q(s):\deg Q<n\}\subset\mathbb Q^R.
\tag{P5}
\]

以下 coefficient 核是**实际积分的固定周期表示**中的核：使用已经证明的 \(T_0=4G\)、\(T_2=12\beta(4)\) 等身份；其余 seed 值暂保留为实际积分生成元。没有假定这些数值线性无关。消去这些生成元的形式系数，是无条件充分的周期认证方法；它不是数值消去方法的必要条件，因为未来可能发现新的实际周期关系。本稿的 obstruction 精确针对这个已固定、未追加未知身份的模型。

## 2. 最高 plus-boundary 周期的实际系数

按上一稿记 \(T=M_z(0,0)\)、\(U=M_z(0,1)\)、\(V=Z_z(0,0)\)。定义真实值

\[
\mathfrak u=\frac{[z^2]U}{3},\qquad
\mathfrak v=\frac{[z^2]V}{3},\qquad
\Omega=\mathfrak u-\frac32\mathfrak v.
\tag{P6}
\]

它们是收敛积分；例如 \(\mathfrak u=M^{(2)}(0,1)\)、\(\mathfrak v=Z^{(2)}(0,0)\)。下文还将证明 \(\Omega>0\)，但不声称它无理或与目标线性无关。

令 \(c_l=4^{-l}\binom{2l}{l}\)，下标不为非负整数时取零。完整 H13/H14 递推给出两个最高 seed 的系数

\[
\operatorname{coeff}_{\mathfrak u}M^{(2)}(i,j)=c_{(j-i-1)/2},
\qquad
\operatorname{coeff}_{\mathfrak v}Z^{(2)}(i,j)=[i=j].
\tag{P7}
\]

证明不需要猜 period evaluation：最高 \(U_2\) 在 H13 的 plus-boundary 齐次递推中只能乘零阶传播 \(f^{-1}\)，且只在 \(i<j\) 分支出现；所有 \(zK\) 项降低 seed jet 阶。最高 \(V_2\) 在 minus/plus 的零阶 H14 递推中只有 \(d=0\) 的起点；\(d=2\) 的系数 \(d-2=0\) 截断其向两边传播，因此只留在主对角。外矩及 diagonal tails 都不包含这两个最高 seed。

由 P3 和 \(j<L\)，

\[
\sum_i[t^i]P_r\,c_{(j-i-1)/2}
=[t^j]\frac{tP_r}{f}=[t^j]D_r.
\tag{P8}
\]

所以这两个实际 seed 在整个 mixed raw pool 中**精确合并**为

\[
\Omega\,\mathcal D_N,\qquad
(\mathcal D_N)_{r,j}=[t^j]D_r,
\quad 0\le r<n,\ b\le j<L.
\tag{P9}
\]

原 \(\ell=0\) 时 \(U_0=\tfrac32V_0\) 的身份不能直接继承到 P9：现在留下尚未求值的 \(\Omega\) 系数项，不能仅凭零阶身份断言它消失。若未来求出 \(\Omega\) 属于 \(\mathbb Q+\mathbb Q\theta\) 或可与其他 seed 合并，必须先把这项实际身份写出，再重算系数核。

事实上，可以不猜任何高权周期身份就证明这一边界值非零。令 \(u=\operatorname{artanh}t\)，则直接积分 \(s\) 并合并 \(\pm t\) 给

\[
U(z)=2\int_0^\infty
\frac{(u-\tanh u)\sinh(zu)+\log(\cosh u)\cosh(zu)}{\sinh u}\,du,
\]
\[
V(z)=2\int_0^\infty
\frac{e^{zu}(u+\log(\cosh u))}{\sinh(2u)}\,du.
\tag{P9a}
\]

两式在 \(|\Re z|<1\) 内满足固定阶微分的可积支配。置

\[
\mathcal K(u)=\frac{(2\cosh u-\tfrac32)\log(\cosh u)-\tfrac32u}{\sinh(2u)}.
\]

由 P6 和 P9a，

\[
\Omega=\frac13\int_0^\infty u^2\mathcal K(u)\,du,
\qquad \int_0^\infty\mathcal K(u)\,du
=\frac12(U(0)-\tfrac32V(0))=0.
\tag{P9b}
\]

第二条使用源文已经证明的实际 \(U(0)=\pi^2/4\)、\(V(0)=\zeta(2)\) 和 \(\pi^2/4=\tfrac32\zeta(2)\)。函数

\[
\mathcal R(u)=(2\cosh u-\tfrac32)\frac{\log(\cosh u)}u
\tag{P9c}
\]

严格递增并从0趋向无穷：第一因子正且递增；第二因子的导数分子 \(u\tanh u-\log(\cosh u)\) 在0为零，其导数为 \(u\operatorname{sech}^2u>0\)。故恰有一点 \(u_0>0\) 使 \(\mathcal R(u_0)=3/2\)，且 \(\mathcal K\) 在它之前为负、之后为正。\(\mathcal K\) 在0有有限极限，在无穷按 \(O(u e^{-u})\) 衰减，因而所有显示积分绝对收敛。最终

\[
\boxed{\quad
3\Omega=\int_0^\infty (u^2-u_0^2)\mathcal K(u)\,du>0.
\quad}
\tag{P9d}
\]

这是一个实际严格符号证书，说明零阶边界消除确实没有在二阶继续成立；它没有证明 \(\Omega\notin\mathbb Q+\mathbb Q\theta\)，也不能把 \(\Omega\) 的形式系数消除宣称为所有数值消除方法的必要条件。

## 3. 全列池边界核的精确秩和 primitive 整核

**命题 P10。** 对每个 \(N\ge1\)，

\[
\operatorname{rank}_{\mathbb Q}\mathcal D_N=40N-1,
\qquad
\ker_{\mathbb Q}\mathcal D_N
=\operatorname{span}_{\mathbb Q}\{s^j:b\le j\le A\}.
\tag{P10}
\]

证明：P2 中 \(U_{d-1}\) 的最高系数是 \(2^{d-1}\)。对正侧行 \(r=g+d\)、\(1\le d\le d_*\)，

\[
\operatorname{ord}_{t=0}D_{g+d}=C-d,\qquad
[t^{C-d}]D_{g+d}=2^{d-1}.
\tag{P11}
\]

所有行都没有次数 \(\le A\) 的项。正侧 \(d\le g\) 的最低次数 \(C-d\ge L\)，在 raw pool 上为零；\(d=g+1,\ldots,d_*\) 的最低次数遍历 \(L-1,\ldots,A+1\)。取这 \(40N-1\) 行、列 \(A+1,\ldots,L-1\)，按最低次数递增排列行，得到上三角非零对角块，故该高列块可逆。

低列 \(b,\ldots,A\) 全为零，高列块可逆，P10 的核因此不是一个有潜在巨大 Smith 高度的抽象格：

\[
\ker_{\mathbb Z}\mathcal D_N
=\bigoplus_{j=b}^{A}\mathbb Z\,s^j.
\tag{P12}
\]

这是 saturated primitive 坐标格，基向量 sup 高度和 \(\ell^1\) 高度均为1。三角对角中的大 dyadic 数不引入 kernel-basis 分母。

维数是 \(12N+1\)。仅消去 \(\Omega\) 这一项，就已经不可能在原 \(48N\) 行规模上取出 \(48N\) 个独立的认证 columns；任何这样的 \(48N\times48N\) 原 raw 投影都零行列式。这是实际 coefficient 矩阵计算，而不是“周期类型数有限”的坏秩论证。

## 4. 原 endpoint filter 下只剩 \(8N+1\) 列

对 P5 的列多项式 \(v=s^b(1-s)^qQ\)，P10 等价于 \(\deg v\le A\)。非零时最高项不能抵消，故

\[
v\in W_N\cap\ker\mathcal D_N
\Longleftrightarrow
\deg Q\le A-b-q=8N.
\tag{P13}
\]

因此

\[
\dim(W_N\cap\ker\mathcal D_N)=8N+1=:m,
\quad
\operatorname{rank}(\mathcal D_N\mathcal T)=40N-1.
\tag{P14}
\]

原 \(\mathcal T\) 是原稿的 binomial filter。实际整数核的基可以不调用 Siegel lemma 直接写成

\[
v_k(s)=s^{b+k}(1-s)^q,\qquad 0\le k\le8N.
\tag{P15}
\]

它们组成 \((W_N\cap\ker\mathcal D_N)\cap\mathbb Z^R\) 的 primitive 整基。证明：若整数列属于 P13，先除去 \(s^b\)，再乘 \((1-s)^{-q}\) 的整数幂级数，所得 \(Q\) 的系数仍为整数；P13 又保证其为次数不超过 \(8N\) 的多项式。每个 P15 基向量满足

\[
\|v_k\|_1=2^q,\qquad
\|v_k\|_\infty\le2^q.
\tag{P16}
\]

这是已有 endpoint factor 的明确高度，不能称为免费投影；但没有另一层未知整核 index。

## 5. 单目标接口和一个保留满秩的缩小模型

先只用已证实际周期身份，把 P4 写成

\[
\mathcal F=C_0+\beta(4)C_4+G C_G+\Omega\mathcal D_N+\sum_\nu p_\nu C_\nu.
\tag{P17}
\]

取 \(\theta=\beta(4)-G/3\)，于是坏系数的 stack 是

\[
B_N=\begin{pmatrix}
\mathcal D_N\\ C_G+C_4/3\\ (C_\nu)_\nu
\end{pmatrix},\qquad K_N=\ker B_N.
\tag{P18}
\]

在任一实际 allowed space \(W\) 上，选基矩阵 \(E_W\)，目标像秩可完全有限地计算为

\[
\operatorname{rank}(C_4|_{K_N\cap W})
=\operatorname{rank}\begin{pmatrix}B_NE_W\\C_4E_W\end{pmatrix}
-\operatorname{rank}(B_NE_W).
\tag{P19}
\]

P10/P14 已证明原 full pool 的该秩最多 \(12N+1\)，原 endpoint pool 中最多 \(8N+1\)，故原 \(n=48N\) 的 H29 不能成功。即使允许 row restriction 或重新组合，也无法从这个固定 kernel 得到原规模的非零 determinant。

P19 的满秩 target coefficient 是特定目标像接口；一般无理性证明只需 \(C_0+\theta C_4\) 的真实 determinant 非零，未必要求 \(C_4\) 本身满秩。这里排除原规模 determinant 的理由是 \(K_N\) 的列空间维数本身不足，而不是单凭 top coefficient rank 不足。

缩小模型仍有一个正面结果。原正侧 Chebyshev 行的 \(P\)-span 恰是

\[
(1-t)^h t^A\,\mathbb Q[t]_{\le d_*}.
\tag{P20}
\]

因为 \(T_d\) 的次数逐级递增，构成多项式基。于是对 \(0\le i\le8N\)，可选真实原行的有理组合，使

\[
\widetilde P_i(t)=(1-t)^h t^{A+i},
\tag{P21}
\]

其 \(\widetilde D_i\) 是同一个原行组合，并保留 contact。配上 P15 columns，已经消掉 \(\Omega\)。

已标识的 \(\beta(4)\) 系数为

\[
C_4(r,j)=4\sum_u[t^u]P_r\,c_{(u-j)/2}.
\tag{P22}
\]

理由是 \(T_2=12\beta(4)\)，外矩到二阶不含 \(\beta(4)\)，最高 \(T_2\) 在 minus-boundary 的零阶传播是 \(c\)；plus-boundary 和 Z 的其他 seed 没有被未经证明地并入 \(\beta(4)\)。

由于 P21 的最低次数为 \(A+i\)，而 P15 columns 的最高次数不超过 \(A\)，P22 全部指数非负。使用

\[
c_{k/2}=\frac1\pi\int_{-1}^1\frac{t^k}{f(t)}dt
\quad(k\ge0)
\]

以及 \(q\) 偶数，得到缩小矩阵

\[
\widetilde C_4(i,k)=\frac4\pi\int_{-1}^1
\frac{(1-t)^{h+q}t^{A-b-q+i-k}}{f(t)}dt.
\tag{P23}
\]

令 \(K=8N=A-b-q\)，反转列 \(k=K-j\) 后，

\[
\widetilde C_4(i,K-j)=\frac4\pi\int_{-1}^1
\frac{(1-t)^{6N}t^{i+j}}{\sqrt{1-t^2}}dt,
\quad0\le i,j\le K.
\tag{P24}
\]

这是正 measure 下的 monomial Gram：对非零实多项式 \(Q\)，积分 \(\int Q(t)^2(1-t)^{6N}dt/f(t)\) 严格正。因此 \(\operatorname{rank}\widetilde C_4=m=8N+1\)。它说明消去 \(\Omega\) 后可以显式保留非退化的已标识 top-beta 系数；它**没有**证明 P18 其余坏系数同时消失，也不是完整 H29 在缩小空间上已经成立。

## 6. Chebyshev 整行组合的显式高度

P21 对应 \(x^{d_*-i}\) 的 Chebyshev 展开。对 \(d\ge1\)，

\[
x^d=2^{-d}\left(
[d\text{ even}]\binom d{d/2}T_0(x)
+2\sum_{k=0}^{\lfloor(d-1)/2\rfloor}\binom dk T_{d-2k}(x)
\right).
\tag{P25}
\]

这里 \(d=d_*-i\ge36N-1>0\)。系数非负，且把 \(x=1\) 代入可见其和为1。故统一乘 \(2^{d_*}\)，即可将每个 P21 与对应 \(D\) 都写成原整数 Chebyshev 行的整数组合；每行变换的 \(\ell^1\) 高度恰为 \(2^{d_*}\)。

因此整模型可明确采用

\[
P_i^*=2^{d_*}\widetilde P_i,\qquad D_i^*=2^{d_*}\widetilde D_i,
\tag{P26}
\]

配 P15，整个 construction 没有未支付的 Smith 核高度。其 row/column coefficient \(\ell^1\) 输入上界为

\[
\log\Bigl(\prod_i\|\text{row}_i\|_1\prod_k\|v_k\|_1\Bigr)
=m(d_*+q)\log2=(8N+1)(48N-1)\log2.
\tag{P27}
\]

这是明确的 \(N^2\) 规模，绝非自动 \(O(m\log m)\)。P26 的行缩放使 normalized 实际 determinant 精确乘 \(2^{d_*m}\)；P27 的列高度是 Cauchy–Binet/输入估计可用的上界，若直接积分能量已经保留 endpoint factor，则不能再重复收费。这里没有声称这套 dyadic 缩放最优。

上一稿的全素数输入 cap 在 \(\ell=2\) 为

\[
Q_{2,H}=12\,2^{12(H+6)}D_{H+4}^{6}.
\tag{P28}
\]

由于 P26/P15 都是整数原行列组合，P28 仍清除本 construction 中**固定周期表示的输入系数**。它不清除剩余非有理周期。若改回 normalized P21，需另外支付所用 dyadic row 分母。原 Catalan \(48N\) 行的 Hardy determinant 常数、优化全素数费用、非零种子也不能直接移植到这套 \(8N+1\) 行组合：现在缺的是同一缩小矩阵的解析/算术/非零比较。

## 7. CDT 接口和下一项精确任务

按 PDF 技能实际提取并全文阅读已存 CDT PDF 第89、90页，共2页：Theorem7.0.1 要求实际 \(\mathbb Q[[x]]\) 芽、\(\mathbb Q(x)\)-线性独立、完整 denominator types、共同 map 上的 meromorphic continuation；holonomic 情形仍须 \(\log|\varphi'(0)|>\tau\)。其 rank 上界比较同一 \(\tau\) 与双边界 logarithmic integral。P19/P24 是实际 period coefficient 的有限秩事实，并未提供这些函数条件，不能直接称为算术 holonomy 定理的数值应用。

现在有两个可区分的下一步：

1. 实际计算 \(\Omega\) 的 weight-four period 表达，寻找已证可用身份。如果它能被 \(\mathbb Q+\mathbb Q\theta\) 或其他 seed 合并，应在新 period module 中重算 full pool；不能先假定它为坏方向已消失。
2. 固定 P21/P15 缩小模型，完整计算剩余 \(T_1\)、\(G\)、\(\eta\) 和 seed coefficient stack，检验 P19 是否还有正目标像秩；若成功，再支付其 primitive kernel 高度并证明同一对象的解析界和非零。P24 已经给出可用的 top coefficient 非退化证书。

本稿已证 P7–P16 的最高边界核与整格、P9a–P9d 的实际 \(\Omega>0\)、P19 的完整接口、P24 的缩小 top coefficient Gram 非退化、P25–P28 的明确输入高度。没有 \(\beta(4)\)、\(\beta(4)-G/3\) 或新 ζ/L 值无理性/LI 结论；没有形式化验证。

## 8. 阅读与运行记录

实际全文读两份指定输入：higher-jet 稿全部8节和 foundations.tex 全434行；foundations 又以独立完整输出回读一次，避免合并输出截断。源仓库只读，没有 Git 操作或文件修改。

实际全文阅读 CDT `literature/cdt2024_l2_chi_minus3.pdf` 第89、90页，个人2页，distinct union2页；没有新下载、渲染或改写PDF，没有其他网页数学输入。PDF技能只用于只读文本提取，本文不声称排版视觉审查。

本稿 P1–P28/P9a–P9d 的证明为纸面推导；没有针对这些证明执行数学计算程序。未执行旧620 producer/guard、旧脚本、prime table 扩展、Lean或数值拟合。已收父任务授权在工作区创建新稿，不修改任何冻结稿。

root 已完成本稿全部8节、P1–P28/P9a–P9d 的独立全文数学审查，并重新全文读 H1–H30 和 foundations.tex 全434行，明确 PASS、无需数学修正。其独立重推最高 seed 传播/contact、三角rank/primitive核、endpoint交核、缩小正Gram、dyadic整高度，以及 P9a 两个 u 积分的因子、P9b 零阶积分和一次变号正性。作者收讫后补入本记录并最终全文回读。

另应 root 请求，作者实际全文独审 [大素数尾内容稿](cdt_beta4_large_prime_tail_content_20261007.md) 全5节L1–L14，明确 PASS；定位只读 E10/L1 后，以一段全新内联 Fraction 运算独立重建 n=2、3 的 P/q，五个有限域矩阵、五个 characteristic polynomial 和对应完整系数估值均一致。没有复算其中较大 n 的探测表。该交叉审查不把本稿纸面推导改称机器证明，也没有执行任何旧研究程序。
