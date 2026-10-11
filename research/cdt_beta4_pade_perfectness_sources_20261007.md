# 单 β(4) Hermite 投影：合流 Cauchy 完整行列式、精确费用接口与 Padé 文献适用域

日期：2026-10-07。状态：唯一新纸面稿，已收 scaled 正式独立全文纸审并完成最后作者全文回读；没有证明新的数值无理性或线性无关性。

本文针对实际单周期模型，不替换其积分核、目标或有理行。所得新接口是一个完全显式的合流 Cauchy 行列式与原投影的 Schur 补身份，并由此把已付费但粗的 β(4) 二次分母常数从 69 改为 57+6log2−9log3。非零性仍是独立假设。直接多重正交完美性不能补上它：实际 n=2 行空间在正积分区间和负有理变换轴上都不是 Chebyshev 空间。

没有创建、执行、import 或 rerun 数学 producer；没有执行 prime 表、guard、Lean 或官方仓库证书。620 旧冻结记录及旧稿保持只读。PDF 读取、渲染、正常 TLS 下载和文件哈希只用于文献核验。

## 1. 实际矩阵与低周期约束

**P1.** 采用 [单周期模型 B1–B29](cdt_beta_single_period_confluent_integral_model_20261007.md) 的 r=3、s=4：

\[
H=3n,\quad J=\{0,\ldots,n-1\},\quad I=\{n,\ldots,3n-1\},
\]
\[
C(u,v)=\int_0^1\!\int_0^1
\frac{x^{4u}y^{4v}}{1+x^2y^2}\frac{(-\log y)^2}{2}\,dx\,dy
=\sum_{j\ge0}\frac{(-1)^j}{(2j+4u+1)(2j+4v+1)^3}.
\tag{P1}
\]

行索引 u∈J∪I，列索引 v∈J。原模型已严格构造 p∈M_{n,H}(Q)，满足

\[
p_J=I_n,\quad
\sum_{u\ne v}\frac{p_{k,u}}{(u-v)^\ell}=0
\quad(v\in J,\ \ell=1,2),\qquad
E=pC=q+\beta(4)I_n.
\tag{P2}
\]

这里 q=pA，A 是原模型 B8 的完整有理部分，含对角 A(u,u)=−T_{u,4}。本文没有重新选择 p。

**P2.** 按顺序 (v,ℓ)=(0,1),(0,2),…,(n−1,1),(n−1,2)，定义实际 H×2n 有理矩阵

\[
\mathcal L_{u,(v,\ell)}
=\begin{cases}(u-v)^{-\ell},&u\ne v,\\0,&u=v.\end{cases}
\tag{P3}
\]

其 J、I 行块分别记为 L_J,L_I。P2 等价于 pL=0。特别地，对角定义 0 是原 regular-part 约束；不能将它换成无限大的 Cauchy 取值。

记 J_0=[I_n;0]。部分分式 P1 给完整矩阵身份

\[
C=A+\beta(4)J_0+
\sum_{v\in J}\left(\frac{\beta(3)}4\mathcal L_{\bullet,(v,1)}
-\frac{\beta(2)}{16}\mathcal L_{\bullet,(v,2)}\right)e_v^T.
\tag{P4}
\]

这是每个列 v 的身份，包括 u=v。它只使用有理尾和，不要求 β(2) 或 β(3) 满足任何数值关系。

## 2. 合流 Cauchy 约束的精确有限完美性

**P3. 合流 Cauchy 行列式。** 对升序节点 a_1<…<a_{2n}，以及升序节点 b_1<…<b_n，假设 a_i>b_v。按 P3 的列顺序取

\[
\mathscr C_{i,(v,1)}=(a_i-b_v)^{-1},\qquad
\mathscr C_{i,(v,2)}=(a_i-b_v)^{-2}.
\]

则

\[
\det\mathscr C=(-1)^n
\frac{V(a)V(b)^4}{\prod_{i,v}(a_i-b_v)^2},
\qquad V(a)=\prod_{i<j}(a_j-a_i).
\tag{P5}
\]

证明从普通 Cauchy determinant 开始，后一个节点组为
(b_1,b_1+ε_1,…,b_n,b_n+ε_n)。每个第二列减第一列并除 ε_v，取 ε_v→0，得到 ∂_{b_v}(a_i−b_v)^{-1}=(a_i−b_v)^{-2}。每对内部的 Vandermonde 因子除 ε_v 后趋于 1；两组不同 b 节点之间的四个差趋于 (b_w−b_v)^4。普通差型 Cauchy 的符号是 (−1)^{binom(2n,2)}=(−1)^n。分母全部正且不为零，故该极限合法。这一证明也明确没有额外的 2 或阶乘。

**P4. 实际约束块的非退化性与唯一性。** P5 适用于 a=I、b=J，给出

\[
\boxed{\ \delta_n:=\det L_I=(-1)^n
\frac{V(I)V(J)^4}{\prod_{u\in I,v\in J}(u-v)^2}\ne0.\ }
\tag{P6}
\]

因此实际 p 唯一，并且

\[
\boxed{\ p=[\,I_n,\ -L_JL_I^{-1}\,].\ }
\tag{P7}
\]

证明 p_J=I 后，pL=0 就是 L_J+p_I L_I=0。P7 既与原 Hermite 插值公式相同，也给出一个不依赖数值周期的完整正规性证明。它证明的是 finite regular-part 约束的可逆性；没有证明周期积分 E 可逆。

P6 的节点有限，不能据此宣称满足具有无限支撑 generating measures 的 Nikishin 定义。但可以把它作为本模型里确实成立、可逐素数付款的有限 Hermite 插值引理。

**P5. 精确全素数账本。** 对每个素数 p，不排除小素数，

\[
v_p(\delta_n)=
\sum_{d=1}^{2n-1}(2n-d)v_p(d)
+4\sum_{d=1}^{n-1}(n-d)v_p(d)
-2\sum_{\substack{u\in I\\v\in J}}v_p(u-v).
\tag{P8}
\]

各和有限，n=1 时空 Vandermonde 乘积为 1。所有差≤3n−1，因此 p>3n 时 P8 为零。P8 是一条确切 valuation 身份，而非仅按行数清分母的估计。

## 3. 原投影的完整 Schur 补与费用改善

**P6. 保留原对象的 determinant quotient。** 对不定元 T，定义

\[
\mathcal K_n(T)=
\begin{pmatrix}
A_J+TI_n&L_J\\
A_I&L_I
\end{pmatrix}.
\tag{P9}
\]

P7 与 Schur complement 给

\[
\boxed{\ \det\mathcal K_n(T)
=\delta_n\det(q+TI_n).\ }
\tag{P10}
\]

也可以左乘 [[I,−L_JL_I^{-1}],[0,I]] 直接证明，其 determinant 恰为 1。列顺序是目标列在前、约束列在后，没有隐藏的置换符号。

此外，由 P4 对前 n 列加上后 2n 列的常数线性组合，得到

\[
\det[\,C,\mathcal L\,]
=\det\mathcal K_n(\beta(4))
=\delta_n\det E.
\tag{P11}
\]

这个恒等式是真实低周期消去的完整外幂版本。β(2)、β(3) 从 determinant 中消失，是列加法的结果；不要求它们有理。

**P7. 全素数整模型。** 记 d_M=lcm(1,…,M)。原 B25 给 d_{4H}^4 A∈M_{H,n}(Z)。P3 每个 ℓ 列由 d_H^ℓ 清分母，J_0 为整数。因此

\[
d_{4H}^{4n}d_H^{3n}\det\mathcal K_n(T)\in\mathbb Z[T].
\tag{P12}
\]

若 β(4)=a/b∈Q、b≥1，则

\[
\boxed{\ b^n d_{4H}^{4n}d_H^{3n}\delta_n\det E\in\mathbb Z.\ }
\tag{P13}
\]

证明将前 n 列乘 b d_{4H}^4，后面的每个 ℓ 列乘 d_H^ℓ。所得整矩阵的 determinant 正是 P13。该证明支付了整个约束块，不能把 L_I^{-1} 当作免费的 integral/unimodular 行投影。

只有当 det E≠0 时，P13 才给出

\[
\log|\det E|\ge
-n\log b-4n\log d_{12n}-3n\log d_{3n}-\log|\delta_n|.
\tag{P14}
\]

特别地，它没有由 monic polynomial 推出其真实代入非零。

**P8. 精确 constraint determinant 的实数主率。** 由

\[
\log V(\{0,\ldots,m-1\})
=\sum_{d=1}^{m-1}(m-d)\log d
=\frac{m^2}{2}\log m-\frac{3m^2}{4}
+O(m\log(m+2)),
\tag{P15}
\]

以及

\[
\sum_{u=n}^{3n-1}\sum_{v=0}^{n-1}\log(u-v)
=2n^2\log n+
n^2\int_1^3\!\!\int_0^1\log(x-y)\,dy\,dx
+O(n\log(n+2)),
\tag{P16}
\]

得到

\[
\boxed{\ \log|\delta_n|
=(6\log2-9\log3)n^2+O(n\log(n+2)).\ }
\tag{P17}
\]

P15 的误差可用 log(d/m) 的单调 Riemann 和，或逐段积分取得；d=1 的端点只付 O(m log(m+2))。P16 中唯一可触及的零差是连续积分角点 (1,1)，离散差实际≥1。把距该角点≤1/n 的部分独立积分，其误差为 O(log(n+2))；其余单元上按 log(x−y) 的导数比较，全部误差为 O(n log(n+2))。这没有在非可积奇性上调用光滑 Riemann 公式。

具体地，若 F(t)=t²log(t)/2−3t²/4、F(0)=0，则双积分为

\[
F(3)-F(2)-F(1)
=\frac92\log3-2\log2-3.
\]

代入 log V(2n)+4log V(n)−2倍 P16，即得 P17；所有 n²log n 项准确相消。

**P9. 同一 β(4) 模型的条件性费用改进。** 使用 log d_M=M+o(M)，P14–P17 给

\[
\boxed{\ \log|\det E|
\ge-\bigl(57+6\log2-9\log3\bigr)n^2+o(n^2)\ }
\tag{P18}
\]

其中 β(4)=a/b 必须是同一个固定有理数，且所考察 n 必须另有 det E≠0。原 B27 的对应常数为 69。P18 的严格减小来自以完整约束矩阵支付投影，而非优化后换了积分对象；仍是 safe upper cost，不称固有最优费用或精确最终算术常数。

P8 还给更细的入口：若对每个 p 在整块 K_n 中证明 determinant divisibility，其增益可直接加到 P14，不需把每个 p_{k,u} 的粗分母重复乘 n 次。尚未得到这种新的全层秩证明。

## 4. 原核的正性，以及投影后它究竟缺少什么

**P10. 原积分矩阵严格符号正则。** 对升序 x_i,y_j∈(0,1)，

\[
\det[(1+x_i^2y_j^2)^{-1}]
=(-1)^{\binom n2}
\frac{V(x^2)V(y^2)}{\prod_{i,j}(1+x_i^2y_j^2)}.
\tag{P19}
\]

任意升序 u_1<…<u_n 的 monomial determinant det[x_j^{4u_i}]>0；保留列 v=0,…,n−1 的 determinant 为 V(y^4)>0。各测度内部严格正；核有界、log 权重可积。两次 Andréief 的绝对可积性因此没有端点问题，原 C 的所有该大小行子式都具有同一非零符号 (−1)^{binom(n,2)}。

这就是 Bertola–Gekhtman–Szmigielski 总正 bimoment 机制的差型/逆序版本。本文直接用 P19 证明，不未经核验地将其 Hilbert setup 全部套入新核。

**P11. 一个严格但尚未满足的非零判据。** 令 R_k(t)=Σ_u p_{k,u}t^u；实际积分行是 R_k(x^4)。若存在固定 ε_n∈{±1}，使

\[
\epsilon_n\det[R_k(t_i)]_{k=0}^{n-1}\ge0
\quad(0<t_1<\cdots<t_n<1),
\tag{P20}
\]

且它在正测度配置集合上严格正，则同一双 Andréief 加 P19 证明 det E≠0。这是 actual row evaluation determinant 的判据；并不只要求每个行函数有一个符号。

另一个有限矩阵充分条件是 p 的全部 n×n 行子式具有同一个弱符号，并至少一个严格非零；Cauchy–Binet 和 P10 即可使用。p_J=I 给至少一个非零子式，但没有给其余子式的符号。此条件不与 P20 声称等价。

P20 可以在原 row basis 上检查；任何固定 real GL_n 换基只把 evaluation determinant 乘一个常数 determinant，不能修复配置之间的符号相消。

**P12. 直接 Chebyshev 完美性实际失败。** n=2 的原 Hermite 公式给

\[
\begin{aligned}
R_0(t)&=1-\frac{196}3t^2+990t^3-2736t^4+\frac{5800}3t^5,\\
R_1(t)&=t-\frac{266}3t^2+1476t^3-4248t^4+\frac{9200}3t^5.
\end{aligned}
\tag{P21}
\]

这些系数可以直接由 B11 的两次 Taylor 展开核对，未执行系数生成器。令 W=R_0R_1′−R_0′R_1，则

\[
W(0)=1,\qquad
(R_0,R_1,R_0',R_1')(1)=(123,207,1562,2593),\qquad
W(1)=-4395.
\tag{P22}
\]

故靠近 0 与靠近 1 的相邻点 evaluation determinants 有相反符号。升序双点配置空间是连通的，因此至少一个内部双点配置 determinant 为零。R_0,R_1 在 (0,1) 不是 Chebyshev 系统。x↦x^4 是递增双射，同样结论适用于实际积分行。

此反例只否定对该 n 直接调用 P20/AT 的方法。积分对不同配置仍可能有不为零的净值；没有推出 det E=0。

## 5. 负轴 rational transform 也不能免费恢复 AT

**P13.** 同一模型定义

\[
F_k(z)=\frac{N_k(z)}{D(z)}
=\sum_{u=0}^{H-1}\frac{p_{k,u}}{z-u}.
\tag{P23}
\]

将 P1 的 u 求和，可精确写成

\[
E_{k,v}=-\frac14\sum_{j\ge0}
\frac{(-1)^jF_k(-(2j+1)/4)}{(2j+4v+1)^3}.
\tag{P24}
\]

有限行求和不会改变绝对收敛性。P24 的 alternating lattice 不等于正 Stieltjes 测度；即使 −F_k(z)>0 对每个 z<0 成立，也不产生 total positivity。

**P14. 一个独立可核的 n=2 负轴障碍。** 此时

\[
\begin{aligned}
N_0(z)&=120(z-1)^3\left(1+\frac{43}{60}z+\frac{41}{40}z^2\right),\\
N_1(z)&=24z^3\left(1-\frac{49}{12}(z-1)+\frac{69}{8}(z-1)^2\right).
\end{aligned}
\tag{P25}
\]

两个 quadratic 的 discriminants 分别为 −12911/3600、−2567/144，首项正，故它们在整个实轴为正。D(z)=∏_{u=0}^5(z−u)>0 对 z<0，因此 F_0,F_1<0 且没有负轴零点。

但 P21–P23 的 infinity moments 给

\[
\frac{F_0(z)}{F_1(z)}
=\frac{123}{207}+\frac{4395}{207^2z}+O(z^{-2})
\quad(z\to-\infty).
\tag{P26}
\]

其导数在足够负处为负。在 z→0−，P25 给 F_0(z)∼1/z、F_1(z)∼−329z²/120，故

\[
\frac{F_0(z)}{F_1(z)}\sim-\frac{120}{329z^3},
\qquad
\left(\frac{F_0}{F_1}\right)'(z)\sim\frac{360}{329z^4}>0.
\tag{P27}
\]

该连续比例先在某区间严格减小、又在另一处严格增加，所以不单调；存在两个不同负节点具有相同比例。F_0,F_1 因而也不是负轴 Chebyshev 系统。对单个行的正性、共同分母和 log 权重的正性，均不能修复这个 rank-two evaluation 障碍。

P14 由 root 提出的精确反例进一步逐式核证；没有把它夸大为所有 n 或所有 integrated pairing 的 no-go。

## 6. 主文献的严格适用条件与我方接口

**P15. Nikishin perfectness。** [Fidalgo Prieto–López Lagomasino, arXiv:1001.0554v1](https://arxiv.org/abs/1001.0554v1)，PDF 2–5 页，Definition 1.2、Theorems 1.1–1.2：从有固定符号、无限支撑的实测度生成，邻接支撑区间分离；mixed type 的两条链共享 base measure。所得对应类型的所有 multi-indices normal，相关 Cauchy transforms 在相离区间为 AT。

本模型目前只有有限 regular-part constraints 和正双积分，尚无将完整 [C,L] 识别为该生成链的证明。P12–P14 还直接排除了把现有 R 或 F 当作相同 AT 行的捷径。P4 的有限约束正常性可用；该文的整个 mixed perfectness 暂不能调用。

**P16. Angelesco。** 同一 primary PDF 2 页所述 type-II 证明依靠各固定符号测度的两两分离支撑，零点分别落入各支撑区间。这里三阶 y-log 不是三条分离支撑，所有相关积分的 y 支撑都为 (0,1)。将一个 log 权重拆成三个独立 product variables，不会自动得到 Angelesco 的 three disjoint intervals。因此该 zero-count 证明不适用于实际投影。

**P17. Cauchy biorthogonality。** [Bertola–Gekhtman–Szmigielski, arXiv:0904.2602v1](https://arxiv.org/abs/0904.2602v1)，PDF 6–13 页，Definition 2.5、Theorems 2.1、2.4：正测度与真正 TP 核使 monomial bimoment 的 minors 正，并把单项式列变成 Chebyshev 函数列。其 Hilbert setup 另有 density、bounded/injective pairing 条件。本文借用并直接证明的只是 P10 的有限 determinant mechanism；没有声称 p 投影仍是 TP 变换。

**P18. Confluent Wronskian positivity。** 本轮新归档 [Zhang–Filipuk, SIGMA10(2014),103/arXiv:1402.1569v2](https://arxiv.org/abs/1402.1569v2)，PDF 3–7 页，Theorems 1.1、1.3：先有满足 AT 的实际权重与对应 multiple OP，再沿逐步增加 multi-index 的路径取偶数长度 Wronskian，才得到固定符号；type-I 还需要足够可微且 Wronskian 有定义。

原行 p 的 Hermite cardinal Taylor 条件不是该文的 multiple orthogonality，也没有这样的 AT path。名称中的“合流”不代替这些假设。可用的具体审核模板是：若以后构造 alternative actual normal system，需逐项给权重、每个 path multi-index 的 AT 性、与目标 determinant 的精确变换，以及全部变基分母；届时该文能提供真正非零性。

**P19. Mellin/hypergeometric multiple OP。** [Wolfs 2024，现有固定 v2 原件](../literature/wolfs2024_multiple_orthogonal_hypergeometric_v2.pdf)，PDF 2、4–7 页，Proposition 2.3：near-diagonal indices、参数差和 noncollision/alternative gap 的明确条件；用 Mellin 卷积的有限阶 TP 保持 Chebyshev 性。这里整数移位重复并存在正负交错 lattice，不能忽略 noncollision 条件后套 Jacobi–Piñeiro 完美性。

该文 composition formula 的有效内容已在 P11 用作严格 conditional 机制。没有证明本模型完整 weights 等于该文的 Γ-ratio 权重，也没有以 hypergeometric 名称代替这种身份。

**P20. Apéry 的成功样本包含更强数据。** [Prévost–Sorokin 的已存作者原件](../literature/prevost_sorokin_hermite_pade_apery_author.pdf)，本轮 PDF 1–8 页全文：cycle graph、多个真实端点接触、辅助问题的唯一性和 Legendre remainder product，最后得到正 triple integral 的 exact special-value remainder。Sorokin1994 已存 2 页短文另给 Rodrigues/integral/asymptotic 结构。

这些是模型特定的 remainder 和算术构造。它们不把任意目标行空间的 functional independence 变成 β(4) 的数值独立性。本模型若能把 P11 的 block determinant 化成有固定符号的 actual remainder product，会补上一个具体缺口；目前没有这样的恒等式。

## 7. 修复后的官方仓库：真正能迁移的结构

**P21.** 本轮实际读根 README、相关 CONTENTS 条目、lean/docs/005，以及 Catalan 原件 nonvanishing.tex 全文和 odd-primes.tex 的完整列池/局部消元段。官方 family005 声明范围是 Catalan 的 β(2) 无理性；family003 的 zero-free L 函数结果并非特殊值算术定理。对所有 preprints 的 Nikishin/Angelesco/Hermite–Padé/biorthogonal 关键词只做定位搜索，不能把搜索命中或无命中称为全部论文数学审查。

相关只读文件：

- E:/codex-build/math/lean/docs/005.md；
- E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/nonvanishing.tex；
- 同目录 odd-primes.tex，列池转移段从第 298 行起。

**P22. 可迁移的是 determinant 证明模式。** 官方 odd-primes 的整列池 lemma 证明：对整个 raw pool 作 GL(Z_p) 变换，所有 full minors 的 valuation 界用两次 Cauchy–Binet 传给原 prescribed integer filter。它甚至允许 leading columns 相关。本文 P9–P13 对新的 rational Hermite 行采用对应原则：先保留完整 constraint block，显式 δ quotient，再支付所有列的分母；没有将 paid rational transform 冒充 local unit transform。

**P23. 尚不能迁移的是 fixed seed。** 官方 nonvanishing 的命题先假设 G∈Q，通过真实 p² moment layer、两个不同 extraction shifts 和 palindromic Frobenius basis，将 48p 规模 reduction 分解为三个固定 48 规模矩阵。新 β(4) 核的 log² moments、4u shifts 和 p 行没有这些已证 layers。原 mod101 pivots 不证明 E 的任何 n 非零。本文只 fresh 读证书文本，未重新执行或检验全部 pivots。

**P24. 一个完全显式的可替代局部接口。** 在 β(4)∈Q 的假设下，对任意素数 p，把 P9 的完整 block 当作对象。若给出非零有理 scales S_C,S_1,S_2，分别乘前 n 列和后面每个 ℓ=1、ℓ=2 的 n 列，使 scaled K(β(4)) 为 p-integral 且 determinant reduction 非零，则

\[
v_p(\det E)
=v_p(\det K(\beta(4)))-v_p(\delta_n)
\tag{P28}
\]

给 actual E 的非零性及 exact p-valuation。更明确地，scaled determinant 是 unit 时，

\[
v_p(\det E)
=-n\bigl(v_p(S_C)+v_p(S_1)+v_p(S_2)\bigr)-v_p(\delta_n).
\tag{P29}
\]

β(4) 有理假设的分母 prime 必须排除或单独支付；δ 的 residue 是否为 unit 由 P8 决定，不可免费假定。P28–P29 是新的对象明确的桥接标准；尚没有非零 reduction 证书。

## 8. 确定结论、剩余缺口与本轮来源

**P25.** 本文已经完成：

1. 原 Hermite projection 的约束块完整正规性 P6–P7，而非仅抽象行独立；
2. 全目标/低周期的 paid block determinant identity P10–P13；
3. 全 prime 精确 δ valuation P8，以及同一 β(4) determinant 的条件性费用 P18；
4. 两条静态 AT 捷径的 actual n=2 反例 P12、P14，和可使用但尚未满足的非零标准 P11/P24。

仍未证明 det E 对无限 n 非零，也未给超过 P18 的实际二次解析衰减。因此没有新的 β(4)、β(6) 或 ζ 奇数值无理性定理。任何另造正多重正交系统，都必须同时保留目标投影并支付实际整数模型。

**P26. 本轮真正新增 PDF 与去重。** 文献库中已有 Fidalgo、Bertola 等原件，没有重复下载。新增一份固定 primary：

- literature/cdt_beta4_pade_sources_20261007/zhang_filipuk2014_multiple_orthogonal_wronskians_1402_1569v2.pdf；
- 正常 TLS： https://arxiv.org/pdf/1402.1569v2；
- 524270 bytes；SHA-256 4d8bd906d67975c57d3a0ba81d340568c5af03956f9a3c09caa1b0c0580be2eb；
- 下载前检索已有 manifests/MD 的 identifier，下载后对所有已有 literature PDF 做物理 SHA 去重，没有命中；
- SIGMA 出版站原链接返回 HTTP406，故使用上述固定 arXiv v2；没有禁用 TLS 或更换为非主来源。

**P27. 本人本轮实际 PDF 读取域。** 页号按 PDF 的 1-based 页：

| 原件 | 本轮完整文字读取页 | 已实际目读页图 |
|---|---|---|
| Fidalgo–López 1001.0554v1，39页 | 1–5 | 5 |
| Bertola–Gekhtman–Szmigielski 0904.2602v1，38页 | 6–13 | 8 |
| Zhang–Filipuk 1402.1569v2，19页，新归档 | 1–7 | 4、6 |
| Sorokin1994 English，2页 | 1–2 | 无；OCR 公式不作为本文数值等式来源 |
| Prévost–Sorokin 作者原件，8页 | 1–8 | 无 |
| Wolfs2024 固定v2，39页 | 2、4–7 | 无 |

合计本人本轮完整文字读取 35 个 distinct PDF 页面；页图是这些页的子集，不重复加页数。最初定位的短摘录和被工具截断的输出不计完整页读取。没有继承上一轮页数或同行读取域。另实际全文读本轮 actual single-beta 模型和已存 higher-even analytic-transfer 稿，官方 nonvanishing.tex 全文；odd-primes 只读上述所列段，不称全文。

**P28. 审阅接口。** 请独立审阅 P5 的合流符号、P10 的列/行排列、P13 的全部 prime 付款、P17 的 log n 相消，以及 P22/P25–P27 的精确反例。对文献适用域的结论只表示这些 primary 的已核假设目前未满足；不排除其它真正 cycle/orthogonal remainder 构造。本文所有新增数学由纸面推导而非数学执行得到。
