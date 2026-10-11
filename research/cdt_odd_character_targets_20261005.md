# 奇数权角色目标：真实反演、导子族秩与完整整数接口

日期：2026-10-05。旧报告冻结。本稿不作参数或素数扫描。

本轮得到的是三个可证明的结构结果：偶角色、奇数权的**实际数值反演**；任意导子下有理周期滤波系统的**实际函数秩及饱和整数滤波格**；以及保留全部低权初值时的**真实 reciprocal 商系统和全尺度整数模型**。它们说明了一个具体剩余缺口：对指定 (L(3,\chi_5))、(L(5,\chi_5))，去除已知偶权周期还不够，较低奇权周期仍进入正则芽；把全部初值去掉又会使有理芽无条件成立，失去“目标有理才产生额外解析延拓”的触发器。本稿未证明新的指定奇权 (L) 值无理性或数值线性无关性。

以下“实际秩”均指所写解析函数在 (\mathbb C(x))（因此也在 (\mathbb Q(x))）上的线性秩；不指端点数值秩，也不自动给出有理 Betti 商。

## 1. 文献中的两种变量与正确奇偶性

对整数 (s>1)，匹配奇偶性的 Dirichlet 值满足

\[
\chi(-1)=(-1)^s\quad\Longrightarrow\quad
L(s,\chi)\in\overline{\mathbb Q}\pi^s.
\tag{1}
\]

因此奇数权 3、5 的困难角色是**偶角色**，而非奇角色。例如 
\(\chi_5=(0,1,-1,-1,1)\) 是偶的实二次角色，
\(L(3,\chi_5)\)、\(L(5,\chi_5)\) 属于本稿要保留的困难目标。
已有匹配奇偶性定理不能用来宣称它们无理或独立。

| 原始版本 | 本稿实际使用的结论与量词 | 对本项目的范围 |
|---|---|---|
| Lai–Li，[*A partial result towards the Chowla–Milnor conjecture*, arXiv:2505.12687v2](https://arxiv.org/pdf/2505.12687v2)，2026-04-09，39 页，Theorem 1.5，PDF/印刷第 3 页 | 固定 (k\ge2)，(q\to\infty)；(V_k^-(q)=\operatorname{Span}_{\mathbb Q}\{\zeta(k,a/q)-(-1)^k\zeta(k,1-a/q)\}) 的维数至少 ((1/\log2-o(1))\log q)。 | 奇数 (k) 时这是对称和所张成的困难部分。它没有指定一个小导子的某个 (L(3,\chi))，也没有证明与已知 (\pi^k) 部分交为零。 |
| 同文 [v1](https://arxiv.org/pdf/2505.12687v1)，2025-05-19，39 页，Theorem 1.5，第 3 页 | 较早常数是 (1/(k+\log2))。 | 不能把 v2 常数写成 v1 结果。v2 第 38 页利用带嵌套系数除数的判据。 |
| Mistiaen，[*Linear independence of values of Dirichlet (L) functions*, arXiv:2512.02612v1](https://arxiv.org/pdf/2512.02612v1)，2025-12-02，44 页，Théorème 1.0.5，PDF/印刷第 3 页 | 固定模数 (N\ge3,4\nmid N) 和角色 (\chi)，取相反奇偶性 (\varepsilon)。充分大的同奇偶性 (S) 满足 (\dim_{\mathbb Q(\zeta_N)}\operatorname{Span}\{L(i,\chi):2\le i\le S,i\equiv\varepsilon\bmod2\}\ge0.42N^{-3/2}\sqrt{S/\log S})。 | 是固定角色、权重增长的定理；不指定 (L(3,\chi_5)) 或 (L(5,\chi_5))。排除 (4\mid N)，所以不能直接套 Dirichlet beta。 |
| Gun–Kandhil–Philippon，[*On linear independence of Dirichlet (L) values*, arXiv:2212.00366v1](https://arxiv.org/pdf/2212.00366v1)，2022-12-01，19 页，Theorems 3–4，第 2 页 | 匹配奇偶性的角色值，跨两两互素模数，在指定数域交条件下独立。 | 奇权部分使用奇角色，不覆盖本稿的偶角色奇权目标。 |

Lai–Li 与 Mistiaen 的结论是已有定理，不是本项目新证明。前者增长的是导子，后者增长的是权重；这两种增长不能替换为“固定权 3、固定导子 5 的指定值”。角色 Fourier 变换一般含代数系数，也不能未经基域成本分析就把 Hurwitz 的 (\mathbb Q)-维数原样转为 (L) 值的 (\mathbb Q)-维数。

## 2. 导子 5 的真实有限投影和固定指标

记 (T_a=\zeta(s,a/5))，\(S_1=T_1+T_4\)，\(S_2=T_2+T_3\)。逐项分组给出实际数值身份

\[
S_1+S_2=(5^s-1)\zeta(s),\qquad
S_1-S_2=5^s L(s,\chi_5).
\tag{2}
\]

整数坐标变换 \( (S_1,S_2)\mapsto(S_1+S_2,S_1-S_2)\) 的 Smith 因子为 (1,2)。其像是两坐标同奇偶性的子格，指标恰为 2。这个指标是完整有限投影数据，不能代替随逼近尺度增长的全部 content。

式 (2) 没有消去 (\zeta(s))：要研究整个二元困难部分，应该保留两个目标坐标；要研究纯 (L(s,\chi_5))，应该使用均值为零的角色行。已知 (\zeta(3)) 无理至多使某些由它缩放得到的组合无理，不能推出 (1,\zeta(3),L(3,\chi_5)) 独立。

## 3. 一般导子下的实际秩与完整整数滤波格

令 \(q>2\)，\(A_q=\{a:1\le a<q/2,(a,q)=1\}\)，\(r=\varphi(q)/2\)。以整数向量 \(v=(v_a)_{a\in A_q}\) 定义 even、unit-supported 权

\[
c_v(n)=\begin{cases}v_a,&n\equiv\pm a\pmod q,\\0,&(n,q)>1.\end{cases}
\]

这些轨道指标函数支集互不相交，所以它们是完整饱和整数基。平均值为零等价于
\(\sum_{a\in A_q}v_a=0\)；其饱和核为 \(e_a-e_{a_*}\)，秩 \(r-1\)。这是实际删去 1 处极点的条件。

定义实际函数

\[
G_{v,j}(x)=\sum_{n\ge1}\frac{c_v(n)x^n}{n^j},\quad
G_{v,0}(x)=\frac{P_v(x)}{1-x^q},\quad
P_v(x)=\sum_{a=1}^{q-1}c_v(a)x^a,
\quad\theta=x\frac{d}{dx}.
\tag{3}
\]

它们满足 \(\theta G_{v,j}=G_{v,j-1}\)。若 \(v_1,\ldots,v_d\) 在 \(\mathbb Q^r\) 独立，则对任意 \(s\ge1\)

\[
1,\ G_{v_i,j}\quad(1\le i\le d,1\le j\le s)
\quad\text{在 }\mathbb C(x)\text{ 上独立；实际秩为 }1+sd.
\tag{4}
\]

**证明。** 在 \(q\) 次单位根 \(\xi\) 处，令 \(R_i(\xi)\) 是 \(G_{v_i,0}(x)\,dx/x\) 的残数。绕该点的局部 monodromy 对 \(G_{v_i,j}\) 给出非零固定常数乘
\(R_i(\xi)(\log x-\log\xi)^{j-1}/(j-1)!\)。对有理函数关系施加 monodromy，最高 log 次项迫使
\(\sum_i a_{i,s}(x)R_i(\xi)=0\)。评价矩阵 \(P_{v_i}(\xi)\) 是有限 Fourier 矩阵的一部分；因为 \(\deg P_i<q\) 且多项式独立，它的列秩为 \(d\)。故所有最高层系数为零，依次下降各层，最后常数系数也为零。均值为零时所有 \(P_i(1)=0\)，删去 1 的零残数行不影响秩。这里使用的是 log 的函数超越性，不预设任何端点周期无理。∎

因此均值为零的整个有理困难部分有实际系统秩
\(1+s(r-1)\)。该秩不证明同一数目的 \(G_{v,s}(1)\) 数值独立。

前缀 \(1\le n\le N\) 的完整整模型也显式可算。对单轨道基令

\[
\delta_{a,s}(N)=\mathop{\rm lcm}_{\substack{n\le N\\n\equiv\pm a\ (q)}} n^s.
\tag{5}
\]

由于支集不相交，全部整数滤波向量的格恰是
\(\bigoplus_a\delta_{a,s}(N)\mathbb Z e_a\)，不存在跨轨道隐含抵消。所有轨道的公共最小分母恰为

\[
\left(\prod_{p\nmid q}p^{\lfloor\log_pN\rfloor}\right)^s.
\tag{6}
\]

上界由 \(n\) 与 \(q\) 互素得到；下界由每个 \(p\nmid q\) 的最大素数幂 \(p^a\le N\) 本身属于某一个 unit 轨道得到。对混合权 \(v\)，其标量最小分母恰为

\[
\delta_v(N)=\mathop{\rm lcm}_{\substack{n\le N\\(n,q)=1}}
\frac{n^s}{\gcd(n^s,v_{a(n)})}.
\tag{7}
\]

零系数对应分母 1。多个权或多个权重同时整数化时应使用共同系数矩阵的同余整格，而非相乘这些标量分母。式 (5)–(7) 与端点数值是否独立无关。

对于这里的单权重、均值为零空间，完整格还能无需 Smith 运算地显式给出。在饱和坐标基 \(e_a-e_{a_*}\) 中，整滤波条件恰为：各 \(z_a\) 被 \(\delta_{a,s}(N)\) 整除，且 \(\sum_{a\ne a_*}z_a\) 被 \(\delta_{a_*,s}(N)\) 整除。故

\[
[\mathbb Z^{r-1}:\Lambda_N^{\rm mean\,0}]
=\frac{\prod_{a\in A_q}\delta_{a,s}(N)}
{\gcd_{a\in A_q}\delta_{a,s}(N)}.
\tag{7a}
\]

证明是先置 \(z_a=\delta_a t_a\)，再看 \(\sum \delta_a t_a\bmod\delta_{a_*}\) 的像；其大小为 \(\delta_{a_*}/\gcd_a\delta_a\)。这同时记入删平均值约束的全部算术成本。证书用模 5、模 7 两个固定前缀独立 Smith 核验该恒等式。

数值方面也有一个**已有定理的明确推论**。令 \(W_s(q)\) 为这些均值零行的端点值所张成的 \(\mathbb Q\)-空间。所有 unit 对称轨道值之和为 \(\zeta(s)\prod_{p\mid q}(1-p^{-s})\)，所以

\[
\dim_{\mathbb Q}W_s(q)\ge\dim_{\mathbb Q}V_s^-(q)-1
\ge(1/\log2-o(1))\log q-1,\quad q\to\infty
\tag{7b}
\]

对每个固定奇数 \(s\ge3\) 成立。第一步来自把系数空间分为常数权和均值零权，第二步是第 1 节 Lai–Li v2 的应用。它给出同时删掉 \(x=1\) monodromy 的真实固定奇权、高导子数值高秩族；不是本项目的新无理性定理，也不指定其中某个角色或 \(1\) 与整个族的独立性。

## 4. even、mean-zero 权的真实反演定理

本节假设 \(c\) 是非零有理周期权，\(c(0)=0\)、\(c(q-a)=c(a)\)、\(\sum_{a=1}^{q-1}c(a)=0\)。后一条件保证 \(G_0\) 在 1 正则；其对称性还使 \(P'(1)=0\)，故 \(G_0(1)=0\)。这些条件都满足于非主偶实角色 \(\chi_5\)、\(\chi_8\)。

在正实轴上采用从 \(0<x<1\) 延拓的真实分支；\(G_j\) 在该轴无奇点，\(L(j,c)=G_j(1)\)，\(j=1\) 的值由均值为零的收敛和定义。直接计算

\[
G_0(1/x)=-G_0(x).
\tag{8}
\]

对 \(H_s(x)=G_s(x)+(-1)^sG_s(1/x)\)，有
\(\theta H_s=H_{s-1}\)、\(H_1=0\)，且
\(H_{2k}(1)=2L(2k,c)\)、\(H_{2k+1}(1)=0\)。积分得到对所有 \(x>0\) 的实际身份

\[
G_s(x)+(-1)^sG_s(1/x)
=2\sum_{k=1}^{\lfloor s/2\rfloor}
L(2k,c)\frac{(\log x)^{s-2k}}{(s-2k)!}.
\tag{9}
\]

这里没有在周期环中形式地置零；每一个常数和分支都保留。奇数 \(s\) 时定义

\[
K_s(x)=G_s(x)-\sum_{k=1}^{\lfloor s/2\rfloor}
L(2k,c)\frac{(\log x)^{s-2k}}{(s-2k)!}.
\tag{10}
\]

则 \(K_s(x)=K_s(1/x)\)，且 \(K_s(1)=L(s,c)\)。虽然偶权的已知周期已真实相消，令 \(x=e^t\) 后仍有

\[
\begin{aligned}
K_3(e^t)&=L(3,c)+\tfrac12 L(1,c)t^2+\text{有理系数的 }t^4\text{ 及更高偶次项},\\
K_5(e^t)&=L(5,c)+\tfrac12 L(3,c)t^2+\tfrac1{24}L(1,c)t^4
+\text{有理系数的 }t^6\text{ 及更高偶次项}.
\end{aligned}
\tag{11}
\]

高次系数来自 \(\theta^sG_s=G_0\) 的有理函数在 1 的有理导数。这给出明确的低权污染，不允许仅假设 \(L(s,c)\in\mathbb Q\) 就称 \(K_s\) 为有理正则芽。

对 \(\chi_5\)，有特别简单的有理 forcing：

\[
G_0(x)=\frac{x(1-x^2)}{\Phi_5(x)},\qquad
\frac{G_0(x)}{x-x^{-1}}=-\frac1{u^2+5u+5},\quad u=x+x^{-1}-2.
\tag{12}
\]

令 \(x:0\to1\)，则 \(u:\infty\to0\)，逐项或直接积分得到

\[
L(1,\chi_5)=\int_0^\infty\frac{du}{u^2+5u+5}
=\frac2{\sqrt5}\log\frac{1+\sqrt5}{2}.
\tag{13}
\]

这是实际实积分身份。非零代数数的非零对数是超越数，所以该 \(L(1,\chi_5)\) 超越。式 (11) 对权 3、5 都阻止 \(K_s(e^t)\in\mathbb Q[[t]]\)，无论最高周期是否被假设有理。换用 \(u=2\cosh t-2\) 也不能隐藏这一点：它在 \(t^2\) 上具有有理可逆形式幂级数，因而保持“全部系数有理”这一性质。

这个阻碍事实上覆盖**全部非零有理 unit-supported、mean-zero 偶权**，无需指定 \(\chi_5\)。直接使用 Chatterjee–Murty 的原始证明版 [*Non-vanishing of Dirichlet series with periodic coefficients*, arXiv:1405.6982v1](https://arxiv.org/pdf/1405.6982v1)，2014-05-27，22 页，Theorem 3（PDF/印刷第 3 页）：若 \(L(1,c)=0\)，则对每个 unit \(a\)，\(\sum_{b\in M(q)}c(ab)/b=0\)，其中 \(M(q)\) 是由 \(q\) 的素因子生成的幺半群。这里数值域 \(\mathbb Q(c(1),\ldots,c(q))=\mathbb Q\)，所以该文 Okada/BBW 非零接口要求的 \(\Phi_q\) 在该域上不可约条件自动满足。unit 支持使所有 \(b>1\) 的项为零，只剩 \(c(a)=0\)，与 \(c\ne0\) 矛盾。又由该文第 7 页的实际 Fourier–log 身份，\(L(1,c)\) 是代数系数的代数数对数线性形式；第 5 页所述 Baker 定理使这个非零数超越。故对每个奇数 \(s\ge3\)，

\[
[t^{s-1}]K_s(e^t)=\frac{L(1,c)}{(s-1)!}\notin\mathbb Q.
\tag{13a}
\]

这是已有非零/超越理论与式 (9) 的直接应用，不作新数值定理声明。其假设很重要：不把它扩至带非 unit 系数、代数而非有理角色系数或随尺度变化的滤波行。特别是这里没有廉价的非零常数有理滤波可以先删掉 \(L(1,c)\) 再保住纯最高周期；变化权或不同真实周期系统需另外研究。

## 5. 全初值剔除的真实闭合系统及常数平移障碍

可以合法地把所有初值都保留在修正中：

\[
J_j(x)=G_j(x)-\sum_{h=1}^{j}L(h,c)
\frac{(\log x)^{j-h}}{(j-h)!}.
\tag{14}
\]

它们是实际解析函数，满足

\[
J_j(1)=0,\quad \theta J_1=G_0,\quad
\theta J_j=J_{j-1}\ (j\ge2),\quad
J_j(x)+(-1)^jJ_j(1/x)=0.
\tag{15}
\]

在 \(x=1\) 的幂级数系数全部属于 \(\mathbb Q\)，因为初值为零且 forcing 有理。这不是对 \(L(j,c)\) 的算术假设。系统 \(1,J_1,\ldots,J_s\) 的实际秩仍为 \(s+1\)：在任何未消去的单位根处，减去的 log 多项式没有局部 monodromy，而原 \(G_j\) 的不同最高 log 次数仍给独立性。以最高行 \(J_s\) 形成 \(\theta\)-循环行列式，恰为

\[
\det(\theta^kJ_s)_{k=0}^{s}
=(-1)^{s(s+1)/2}G_0(x)
\tag{16}
\]

（相对于 \(1,J_1,\ldots,J_s\) 的坐标行）。

设 \(R_s=L(s,c)+J_s\)。假设 \(L(s,c)\in\mathbb Q\) 确实会使 \(R_s\) 成为有理芽；但它只是在已经有理的系统中对最后一行作有理常数平移。只要系统保留常数行 1，实际秩、非恒定 Taylor 系数、延拓域及曲线上的 meromorphic 性均不因此改变，固定有理分母也不改变指数成本。若同一套 holonomy 数据对该平移系统产生矛盾，它也会对无条件有理的 \(J\) 系统产生矛盾。因此这种构造尚未提供 CDT 所需的额外周期关系触发器。这个结论限于这里的同一个函数系统、同一个常数平移；不排除另一真实 Betti 关系或新的跨系统周期投影。

## 6. 全尺度整数化、全部 content 与安全 CDT 账本

先取整数权 \(c\)。写
\(P(x)=(1-x)C(x)\)、\(B(x)=(1-x^q)/(1-x)\)。由于 \(P(1)=P'(1)=0\)，有 \(C(1)=0\)。令 \(x=1+qy\)，则

\[
\frac{C(1+qy)}q\in\mathbb Z[y],\qquad
\frac{B(1+qy)}q\in\mathbb Z[y],\quad
\left.\frac{B(1+qy)}q\right|_{y=0}=1.
\tag{17}
\]

故 \(G_0(1+qy)\in\mathbb Z[[y]]\)，且
\(q/(1+qy)\in\mathbb Z[[y]]\)。若 \(J_j(1+qy)=\sum_n a_{j,n}y^n\)，递归积分严格给出

\[
n\,L_{n-1}^{j-1}a_{j,n}\in\mathbb Z,\qquad
\delta_{J_j}(N)\mid L_N^j,
\quad L_N=\operatorname{lcm}(1,\ldots,N).
\tag{18}
\]

证明第一式只需注意第 \(n\) 个积分系数使用先前层的指标至多 \(n-1\)；归纳时其分母均整除 \(L_{n-1}^{j-1}\)。对有理权，乘一个固定的共同分母即可，不能省略，但不改变全尺度指数。

标量最小分母须按全部系数算：取合法 \(D_N\)，则

\[
h_N=\gcd(D_N,D_Na_0,\ldots,D_Na_N),\qquad
\delta(N)=D_N/h_N.
\tag{19}
\]

多个行形成 \(B=(D_Na_{i,n})\in\mathbb Z^{d\times(N+1)}\) 时，完整前缀整格为
\(\Lambda_N=\{v\in\mathbb Z^d:vB\equiv0\pmod{D_N}\}\)。若
\([B^t\mid D_N I_{N+1}]\) 的 \(N+1\) 个 Smith 因子是 \(d_1,\ldots,d_{N+1}\)，则

\[
[\mathbb Z^d:\Lambda_N]=D_N^{N+1}/\prod d_i.
\tag{20}
\]

固定 \(\chi_5\)、\(N=16\) 的实算标量最小分母如下。这里只是完整有限证书，不从这五个数字推断指数。

| 行 | \(\delta_{J_j}(16)\) |
|---|---:|
| \(J_1\) | 168 |
| \(J_2\) | 864864 |
| \(J_3\) | 145297152 |
| \(J_4\) | 435891456 |
| \(J_5\) | 3487131648 |

对 \(J_1,J_2,J_3\) 的 \(N=8\) 联合前缀，式 (20) 得指标 338688，而各标量最小分母乘积是 4064256；不能以标量乘积充当共同最优模型。

式 (18) 给合法但不声称最优的自然 fine 类型

\[
m=s+1,\quad e=(0,1,\ldots,1),\quad
\sigma=(0,0,1,\ldots,s-1).
\tag{21}
\]

每个 LCM 柱的参数均为 1。采用 CDT 的相同定义，证书精确计算尖锐积分 \(I_m\) 及 \(\tau_{\rm sharp}=\frac2{m^2}\min_{0\le\xi\le m}(s\xi+I_m(\xi))\)，结果是：

| \(s\) | \(\tau_{\rm flat}\) | \(\tau_{\rm sharp}\) | 合计 | 全 LCM 粗类型 |
|---:|---:|---:|---:|---:|
| 3 | \(19/16\) | \(77/96\)，最优 \(\xi=1\) | \(191/96\) | \(17/8\) |
| 5 | \(5/2\) | \(1507/2160\)，最优 \(\xi=1\) | \(6907/2160\) | \(125/36\) |

这里没有宣称这些是全部有理规范变换的最小成本，也没有指定一个尚未验证的全局延拓域来宣布预算通过或失败。尤其较大的已算 \(h_N\) 不能由有限前缀直接升级为 subexponential content 定理。若涉及未知端点常数的整数行，必须把该常数的假设分母及完整行一起列入式 (19)；本表是已知有理 \(J\) 系数的完整模型。

## 7. 真实 reciprocal 商：闭合、正则与整数模型一并保留

令 \(u=x+x^{-1}-2\)、\(v=x-x^{-1}\)，则 \(v^2=u(u+4)\)。固定域恒等式给

\[
g(u)=G_0(x)/v\in\mathbb Q(u).
\]

对奇数 \(s=2r+1\)，定义
\(F_h=J_{2h+1}\ (0\le h\le r)\)、\(Z_h=J_{2h}/v\ (1\le h\le r)\)。它们是 \(u=0\) 的实际正则芽：\(J_{\rm odd}(e^t)\) 为偶函数，\(J_{\rm even}(e^t)\) 为奇函数，除以 \(v=2\sinh t\) 后仍是偶正则函数。直接微分得到整个有理闭合系统

\[
\frac{dF_0}{du}=g(u),\qquad
\frac{dF_h}{du}=Z_h,\qquad
\frac{dZ_h}{du}=\frac{F_{h-1}-(u+2)Z_h}{u(u+4)}.
\tag{22}
\]

系统 \(1,F_0,\ldots,F_r,Z_1,\ldots,Z_r\) 的实际秩恰是 \(s+1\)。若在 \(\mathbb C(u)\) 有关系，拉回 \(x\) 并把 \(Z_h\) 替换为 \(J_{2h}/v\) 就与第 5 节的独立性矛盾。这里的相消是真实函数下降；并未把较低奇数周期在动机商中置零。

该商也有一套全尺度、安全整数模型。取

\[
u=16q^2 w,\quad w=z^2,\quad
x=(\sqrt{1+4q^2z^2}+2qz)^2.
\tag{23}
\]

有

\[
\frac{x-1}q=4z\sqrt{1+4q^2z^2}+8qz^2\in\mathbb Z[[z]],
\quad v=8qz\sqrt{1+4q^2z^2}.
\]

两个平方根幂级数 \(\sqrt{1+4q^2z^2}\)、\((1+4q^2z^2)^{-1/2}\) 的系数均为整数。在第 6 节的整数权情形，由式 (18) 的整数复合与偶/奇次提取，对商变量 \(w\) 的前缀得到

\[
\begin{aligned}
\delta_{F_h}(N)&\mid L_{2N}^{2h+1},\\
\delta_{Z_h}(N)&\mid 8q\,L_{2N+1}^{2h}.
\end{aligned}
\tag{24}
\]

固定因子 \(8q\) 和导子平方的坐标缩放都已记入；有理权还须乘第 6 节所说的固定共同分母。按共同粗 LCM 模型，所有非恒定行的排序指数为 \(2,4,\ldots,2s\)，其 flat 成本是未取商粗模型的两倍：权 3 为 \(17/4\)，权 5 为 \(125/18\)。这些是安全上界，不是最优算术阻碍。坐标缩放还影响真实解析半径，不能仅引用“取商后分支少”而不支付它。

对 \(\chi_5\)，式 (22) 的 forcing 正是
\(-1/(u^2+5u+5)\)。这是一套显式、跨奇数权的真实函数构造；它仍只解决 de Rham 闭合与局部整数模型。第 5 节的常数平移障碍继续存在，尚无指定最高周期的非平凡 Betti 触发器。

## 8. 证书、审阅范围与下一步真正需要的输入

[精确脚本](cdt_odd_character_targets_20261005_verify.py) 与 [JSON](cdt_odd_character_targets_20261005_verify.json) 共 160 项固定有理/符号检查通过：模数 5、7、8 的反演及整系数归一化；权 3、5 的完整低奇权 jet 污染；循环行列式；\(J_1\) 至 \(J_5\) 的前 20 个 fine 整数系数；完整标量 gcd、一个联合 Smith 格以及式 (7a) 的两个均值零格；reciprocal 商的平方身份及全部闭合方程；式 (21) 的精确预算。没有调用任何 \(\zeta\) 或 \(L\) 数值，也不以目标无理性认证函数秩。

有效的新研究入口应满足下列至少一项：在实际数值上构造能同时处理 \(L(1,c),L(3,c),\ldots\) 的非恒定周期投影；给出由最高周期有理性才产生的额外全局 meromorphic/overconvergent 性；或利用某个新的整数模型和完整 content 定理支付第 6–7 节的全部成本。已知导子/权重维数增长定理可以提供基准与非退化信息，但不能自动填补指定小权角色的这个缺口。与根任务的 modular/Eichler 触发器分支相比，本稿精确说明了普通角色反演本身尚少哪一条假设，避免再次把单目标常数平移当成 holonomy 秩优势。

主文献版本以第 1 节固定 arXiv PDF 为准，由根任务统一归档；本稿未改写旧 PDF、旧报告或 literature 索引。

本轮本地原件：[Lai–Li v2](E:/kimi-build/zeta5/literature/lai_li2026_chowla_milnor_v2.pdf)、[Mistiaen v1](E:/kimi-build/zeta5/literature/mistiaen2025_dirichlet_l_independence_v1.pdf)、[Gun–Kandhil–Philippon v1](E:/kimi-build/zeta5/literature/gun_kandhil_philippon2022_l_values_v1.pdf)、[Chatterjee–Murty v1](E:/kimi-build/zeta5/literature/chatterjee_murty2014_periodic_nonvanishing_v1.pdf)。页码和结论仍以第 1、4 节所列固定版本为准。

独立审阅范围：根分支重推第 4–7 节的主体证明；paper 分支重推第 4–5、7 节；arithmetic 分支重推第 6–7 节（含安全预算与完整格接口），均未发现数学纠错。式 (7a)–(7b)、后加的 (13a) 有单独列出的自足推导/原始定理接口，不把较早的独立审阅范围自动扩大到这些增补。脚本执行与 160 项检查由本文分支完成；不把数学审阅范围扩大到审阅者未读取的文献版本或证书执行。
