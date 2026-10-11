# 真实商周期的拉回、整格饱和与非分裂障碍

日期：2026-10-04。本文承接 [统一研究方案](odd_zeta_global_strategy_20261004.md)、[动机专题](odd_zeta_global_motives_20261004.md) 和 [holonomy 专题](odd_zeta_global_holonomy_20261004.md)。不进行参数扫描，不调用周期猜想，也没有证明 ζ(7)、Catalan 或 3ζ(3)+ζ(5) 无理。

本轮将“真实周期投影”分解成可分别核验的步骤，并证明其整格成本的一条通用界。最关键的区别是：**商对象上的真实投影可以拉回为子对象，即使该投影不能提升到整个非分裂扩张。** 固定有限群的投影成本可以由有限 Smith 数据控制；随次数增长的微分形式约化分母仍是另一个问题。Catalan 的四弧模型给出一个完整的小例子：范数算子的像已经饱和，而不变线到绝对上同调的积分指标仍为 4。

下文的引理是对明确列出的代数数据的无条件结论，不把尚未计算的几何整格数据当作已知。本报告没有声称这些初等引理在文献中首次出现。

## 1. 原始文献给出的真实接口

Eskandari–Murty–Nemoto 的 Catalan 构造在商对象上取旋转不变部分，然后拉回至原相对上同调。旋转不保持原相对边界，所以没有直接作用在整个原对象上；微分形式的对称性到子对象成员关系还需要原文的边界与正则性证明。参见 [v3 §6、Proposition 7.3.1](https://arxiv.org/html/2510.20648v3)，[本地原件](../literature/eskandari_murty_nemoto2025_catalan_motive.pdf)。

Dupont 对奇 ζ 的构造同样在一个商的对合特征空间上拉回；得到含所有允许奇权的对象和相应周期行。这已经是真实范畴操作，但不自动给指定权所需的可积形式族、完整分母与衰减。参见 [v3 Definition 4.10、Proposition 4.11](https://arxiv.org/html/1601.00950v3)，[本地原件](../literature/dupont2018_odd_zeta_motive.pdf)。

Brown–Zudilin 的胞腔 ζ(5) 讨论还说明，选取有理 Betti 行可以消去不需要的周期。行选择不等于在非分裂秩二对象上寻找一个投影。本文只用它说明这两类操作必须区分，不把其全部参数族的几何设想当作已完成的整模型定理。参见 [v3 §4、式 (21)–(22)](https://arxiv.org/html/2210.03391v3)。

## 2. 桥梁引理一：商上的幂等元足以给出真实周期拉回

在一个有理阿贝尔动机范畴中，假定 Betti 与 de Rham 实现正合，并有函子性的比较同构。给定正合列

\[
0\longrightarrow A\longrightarrow M\xrightarrow{\pi}T\longrightarrow0,
\tag{1}
\]

以及一个**实际动机态射** \(e:T\to T\)，满足 \(e^2=e\)。置

\[
T_e=\operatorname{im}e=\ker(1-e),\qquad
C=\ker((1-e)\pi)=M\times_TT_e.
\tag{2}
\]

则有真实子对象 \(C\subset M\) 及正合列

\[
0\longrightarrow A\longrightarrow C\longrightarrow T_e\longrightarrow0.
\tag{3}
\]

若 \(\omega\in M_{\mathrm{dR}}\) 满足

\[
(1-e_{\mathrm{dR}})\pi_{\mathrm{dR}}(\omega)=0,
\tag{4}
\]

则 \(\omega\in C_{\mathrm{dR}}\)。对任何 \(b\in M_B^\vee\)，有实际数值等式

\[
\langle b,\operatorname{comp}_M\omega\rangle
=\langle b|_{C_B},\operatorname{comp}_C\omega\rangle.
\tag{5}
\]

**证明。** 在阿贝尔范畴中幂等元分裂，故 (2) 的像、核及拉回存在；对 (1) 拉回得到 (3)。实现正合使 (4) 恰为 \(C_{\mathrm{dR}}\) 的成员条件。比较同构与包含态射交换，给出 (5)。整个证明不使用数值周期映射单射。证毕。

这解决一个真实但有限的缺口：**不必把商上的群作用提升到 M。** 必须实际证明的是投影的范畴来源、式 (4) 的成员关系，以及保留下来的周期行。仅在 de Rham 向量空间写一个矩阵幂等元，不能保证它是动机态射；仅在形式周期环令 Tate 坐标等于零，也不能推出 (5)。同样，积分分子不变不能代替边界与 residue 兼容的证明。

## 3. 桥梁引理二：拉回整格的指标与全部素数

以下是与动机猜想无关的有理线性代数命题。设 \(\pi:V_M\twoheadrightarrow V_T\) 为满射，取自由有限秩满整格 \(\Lambda_M\subset V_M\)、\(\Lambda_T\subset V_T\)，使

\[
R:=\pi\Lambda_M\subseteq\Lambda_T.
\]

R 在 \(\Lambda_T\) 中有限指数。令 \(\kappa\ge1\) 满足

\[
\kappa\Lambda_T\subseteq R.
\tag{6}
\]

可取 \(\Lambda_T/R\) 的指数，即 Smith 标准形中最大的非零不变因子；这里“指数”指有限群的 exponent，不是其 cardinality。

设 \(e\in\operatorname{End}_{\mathbb Q}(V_T)\) 为幂等元，\(W=\operatorname{im}e\)，\(r=\dim W\)，并有整数 \(m\ge1\) 使

\[
me\Lambda_T\subseteq\Lambda_T.
\tag{7}
\]

定义真正的交整格和一个无需除法的原始拉回格：

\[
\Lambda_C=\Lambda_M\cap\pi^{-1}W,
\qquad
\Gamma_C=\{v\in\Lambda_M:\pi v\in\kappa me\Lambda_T\}.
\tag{8}
\]

则 \(\Gamma_C\subseteq\Lambda_C\)，并且

\[
\Lambda_C/\Gamma_C
\cong (R\cap W)/(\kappa me\Lambda_T),
\qquad
[\Lambda_C:\Gamma_C]\le(\kappa m)^r.
\tag{9}
\]

该商被 \(\kappa m\) 消去，故逐素数有

\[
v_p[\Lambda_C:\Gamma_C]
\le r\bigl(v_p\kappa+v_pm\bigr).
\tag{10}
\]

尤其当 \(p\nmid\kappa m\) 时，两格的 \(\mathbb Z_p\) 化相同。

**证明。** 由 (6)–(7)，\(\kappa me\Lambda_T\subseteq R\cap W\)。\(\pi:\Lambda_C\to R\cap W\) 满射，而 \(\Gamma_C\) 是右侧子格的原像，故得到商同构。若 \(v\in R\cap W\)，则 \(ev=v\)，从而

\[
\kappa m(R\cap W)\subseteq\kappa me\Lambda_T.
\]

因此商是秩 r 整格模 \(\kappa m\) 的一个商，(9)–(10) 成立。证毕。

另有一个直接的整数对偶结论：\(\Lambda_C\) 在 \(\Lambda_M\) 中饱和。若 \(nv\in\Lambda_C\)、\(v\in\Lambda_M\)、\(n\ne0\)，则 \(n\pi v\in W\)；因 W 是 Q 子空间，\(\pi v\in W\)，所以 \(v\in\Lambda_C\)。于是 \(\Lambda_M/\Lambda_C\) 自由，且

\[
\operatorname{Hom}_{\mathbb Z}(\Lambda_M,\mathbb Z)
\twoheadrightarrow
\operatorname{Hom}_{\mathbb Z}(\Lambda_C,\mathbb Z).
\tag{10a}
\]

因此从父 Betti 对偶格限制到真实交格不增加分母；一个交格上的整数泛函也可整数延拓，延拓不必唯一或具有动机意义。若用未饱和的 \(\Gamma_C\) 代替 \(\Lambda_C\)，则不能省略 (9) 的指标。

此界的作用是**保证成本有限并列出必须检查的素数**，不是把平均分母 \(m\) 宣称为必需成本。实际指标可能远小于界，甚至为 1。若 \(\pi\) 的整数 cokernel、商作用或格基归一化没有核验，不能设 \(\kappa=1\)。

在应用中需对 Betti 与 de Rham 侧分别执行本引理。Betti 侧先取无挠商并记录长正合列中的 torsion；de Rham 侧先指定一个固定满 Q 整格，或一个已证明有限自由的 \(\mathbb Z[1/S]\) 模型。局部化模型只控制 \(p\notin S\)，S 内的成本必须另列。抽象有理实现的正合性不蕴含所选整数格的正合性。

## 4. 共轭不能省略：有理中心特征投影

若有限群 H（\(|H|=m\)）通过真实态射作用在 T 上，而且保持 \(\Lambda_T\)，不变投影为

\[
e_H=\frac1m\sum_{g\in H}g.
\tag{11}
\]

更一般地，取复不可约特征 \(\chi\)（次数 d），令 \(\Omega\) 是它在全部有理 Galois 共轭下的轨道。中心幂等元为

\[
e_\Omega=
\frac d m\sum_{g\in H}
\left(\sum_{\psi\in\Omega}\psi(g^{-1})\right)g.
\tag{12}
\]

括号中的轨道和既是有理数，又是代数整数，所以属于 Z；因此 \(me_\Omega\in\mathbb Z[H]\)，可直接代入 (7)。这保留**整个特征轨道**，其秩 r 也必须按整个轨道计算。即使存在 Schur 指标，中心轨道投影仍满足这个结论；它没有进一步断言某个复不可约分量本身已在 Q 上分裂。

若只保留单个 \(\chi\)，则工作通常转到特征域 K，必须保留所有 K 嵌入、系数整数环及回到 Q 的格成本。这里的共轭是系数与实现的共轭，不能给实际超越周期任意定义代数 Galois 共轭，再声称目标有理使它们相同。

若 H 没有保持原选格，可先取 \(\sum_{g\in H}g\Lambda_T\) 得 H 稳定格；与原格的有限交换成本也要进入账本。几何上的 Q 作用不自动保持任意选定的整数基。

所以固定有限群投影只引入有限的固定坏素数集合；\(\pi\) 的 cokernel、系数域和微分形式约化可能引入其他素数。**“所有投影坏素数都固定”不等于“整个积分族的所有分母素数都固定”。**

## 5. 完整计算：Catalan 商对象的四弧整数模型

令 \(A:x^2+y^2=1\)，标记点 \(\{(\pm1,0),(0,\pm1)\}\)。在复数上以 \(z=x+iy\) 将 A 识别为 \(\mathbb C^*\)，标记点为 \(\mu_4\)，旋转 \(\sigma(x,y)=(-y,x)\) 为 \(z\mapsto iz\)。该空间对径向收缩至 \((S^1,\mu_4)\)。以下是本轮独立完成的整数 Betti 计算，Tate twist 不改变这些格指标。

取四个相邻、同向四分之一圆弧 \(a_0,\ldots,a_3\)。相对胞腔链复形的边界落在已取商的四个顶点上，故

\[
H_1(S^1,\mu_4;\mathbb Z)=\bigoplus_{j=0}^3\mathbb Za_j.
\]

令 \(f_j\) 为对偶基。旋转循环置换这四个基，因而

\[
\Lambda_T^\sigma=\mathbb Zf,
\qquad f=f_0+f_1+f_2+f_3.
\tag{13}
\]

这条不变线在 \(\Lambda_T\) 中饱和。整数范数算子 \(N_\sigma=1+\sigma+\sigma^2+\sigma^3\) 满足

\[
N_\sigma f_j=f,
\qquad N_\sigma\Lambda_T=\Lambda_T^\sigma.
\tag{14}
\]

所以范数像的饱和指标为 **1**；不能把平均 \(e=N_\sigma/4\) 的分母 4 当作这个指标。另一方面，绝对圈生成元为 \(u=\sum_j a_j\)。若 \(v\in H^1(S^1;\mathbb Z)\) 满足 \(v(u)=1\)，则自然映射

\[
H^1(S^1,\mu_4;\mathbb Z)\longrightarrow H^1(S^1;\mathbb Z)
\]

把每个 \(f_j\) 送到 v，因此把 f 送到 4v。故

\[
[\mathbb Zv:\operatorname{im}(\Lambda_T^\sigma)]=4.
\tag{15}
\]

结论很具体：原文的不变部分到绝对上同调的 **Q 同构**，在自然整数格上于素数 2 具有指标 4；不变范数像却已经饱和。这两个整数问题不同。

原文所选 de Rham Q 基中投影可以写成只保留第一基向量的矩阵，这说明某个人为选取的基的 Z 张成格稳定，不能证明它就是相对几何的自然积分格。本计算也没有确定原五维对象 \(M\to T\) 的整数 cokernel，或其 de Rham 侧的 \(\kappa\)。这些仍需实际边界、residue、Tate 归一化矩阵的 Smith 证书，不能从 (13)–(15) 推定全部成本只有 4。

## 6. 桥梁引理三：固定纯周期行能把整类变成整数线性形式

假定已给定一个固定二维真实对象 C、一个 de Rham Q 基 \(u_0,u_1\)，和一个固定 \(b\in C_B^\vee\)，并且已证明实际比较等式

\[
\langle b,\operatorname{comp}u_0\rangle=1,
\qquad
\langle b,\operatorname{comp}u_1\rangle=\eta\in\mathbb R.
\tag{16}
\]

设 \(C\subset M\)，固定满整格 \(\Lambda_M\subset M_{\mathrm{dR}}\)，取饱和交格 \(\Lambda_C=\Lambda_M\cap C_{\mathrm{dR}}\)。取固定正整数 \(\delta\)，使

\[
\delta\Lambda_C\subseteq\mathbb Zu_0+\mathbb Zu_1.
\tag{17}
\]

若实际形式族 \(\omega_N\in C_{\mathrm{dR}}\) 和正整数 \(D_N\) 满足

\[
D_N\omega_N\in\Lambda_M,
\qquad I_N=\langle b,\operatorname{comp}\omega_N\rangle,
\tag{18}
\]

则

\[
\delta D_N I_N=A_N+B_N\eta,
\qquad A_N,B_N\in\mathbb Z.
\tag{19}
\]

若此外 \(I_N\ne0\)、\(D_N|I_N|\to0\)，则 \(\eta\) 无理。

**证明。** (18) 与子空间成员关系使 \(D_N\omega_N\in\Lambda_C\)。由 (17) 写出其整数坐标，(16) 给 (19)。若 \(\eta=a/q\) 为有理，\(q\delta D_N I_N\) 是非零整数，却趋零，矛盾。证毕。

该引理不需要周期猜想，因为纯行 (16) 是输入的实际等式。它也不凭抽象的扩张维数提供 (16)：额外周期是否消掉、所用 Betti 类是否有理、规范化是否引入未知数，都必须单独证明。

只要 C 与格固定，\(\delta\) 是常数，对指数预算无影响。但 (18) 中的 \(D_N\) 要针对**整个实际上同调类的坐标约化**证明，不能只说分子多项式的系数是整数。若对象、基或格随 N 改变，就应使用 \(\delta_N\) 并计入其增长。对 h 阶行列式，固定换基/双侧缩放产生的成本必须按 h 计入；若 \(h=O(K)\) 且对象固定，这通常仅为 \(O(K)\) 对数成本，不能由此推断净 \(K^2\) 指数为负。

实际本原化仍需取 \(h_N=\gcd(|A_N|,|B_N|)\)，并估计同一数值 \(\delta D_N I_N/h_N\)。有限投影格指标不是随 N 增长的全系数 content 公式。

## 7. 严格障碍一：非分裂秩二扩张没有选择性幂等元

设 A、B 是互不同构的秩一简单对象，\(\operatorname{End}(A)=\operatorname{End}(B)=\mathbb Q\)，且 \(\operatorname{Hom}(A,B)=\operatorname{Hom}(B,A)=0\)。对一个非分裂扩张

\[
0\longrightarrow A\xrightarrow{i}E\xrightarrow{p}B\longrightarrow0,
\qquad [E]\ne0\in\operatorname{Ext}^1(B,A),
\tag{20}
\]

有

\[
\operatorname{End}(E)=\mathbb Q\operatorname{id}_E.
\tag{21}
\]

**证明。** 任意 f 保持 A，因为 \(pfi\in\operatorname{Hom}(A,B)=0\)。它在 A 和 B 上诱导标量 a、b。扩张的函子性给 \(a[E]=b[E]\)；有理 Ext 空间中 \([E]\ne0\) 故 a=b。\(f-a\operatorname{id}\) 在 A 上为零，故经 B 分解；其在 B 上也为零，故进一步经 A 分解。这给一个 \(B\to A\) 态射，必为零。证毕。

因此这种秩二扩张只有 0 和 1 两个幂等元。特别对不同权的秩一 Tate 或一维 Artin–Tate 层，不能在 E 上找一个真实投影，既消掉一层又保留非平凡扩张周期。

**范围必须保留：**这没有禁止选择 Betti 行与 de Rham 列，使一个矩阵系数等于目标周期；也没有禁止先在较大商 T 上投影、再按 §2 拉回。后者保留扩张的上下两层，前者保留一个数值配对，均与 (21) 相容。对不满足简单性、Hom 消失或非分裂假设的对象，不能套用本障碍。

## 8. 严格障碍二：固定良约化几何不限制增长分母的素数

考虑定义在 Z 上的固定对 \((\mathbb A^1,\{0,1\})\)。其有理相对 de Rham \(H^1\) 为一维，取 \([dx]\) 为基。对整数系数形式 \(x^Ndx\)，有

\[
\int_0^1x^Ndx=\frac1{N+1},
\qquad
[x^Ndx]=\frac1{N+1}[dx]
\quad\text{于 }H^1_{\mathrm{dR}}(\mathbb A^1,\{0,1\};\mathbb Q).
\tag{22}
\]

类等式也可直接证明：\(x^Ndx-dx/(N+1)=d((x^{N+1}-x)/(N+1))\)，右侧原函数在两个边界点均为零，故在相对复形中为恰当项。

取 \(N=p-1\)，约化分母含任意大的素数 p，尽管原几何对固定并具有此处所需的良整数模型。因此不能由“几何坏素数只有有限个”推出“整数系数微分形式的有理上同调坐标只有这些分母素数”，也不能保证一个固定有限生成格含所有次数的这些类。对于这类非真代数空间，整数 de Rham 复形中的 torsion、有限生成性与基变化必须实查。

这给 §6 的具体警告：固定动机、固定有限群及固定 \(\kappa\) 只控制对象之间的线性代数变换；\(D_N\) 的增长来自形式约化，不能删掉。项目 ζ(7) 的较大素数坏矩同样不能仅凭固定几何模型来消除；若要断言二者的精确对应，还需实际 realization 计算，本文没有作此断言。

## 9. 可执行的下一步：做整格证书，避免新的循环

对一个已给出的真实周期族，以下四项足以把“投影可行”改成可复核的算术问题。

| 需证明的数据 | 可检查的结果 | 不能用来替代它的事实 |
|---|---|---|
| \(\pi\) 与商上 e 的真实范畴来源，形式的 residue / 边界成员关系 | §2 的实际子对象与数值配对等式 | de Rham 任意矩阵投影、形式删 Tate 项 |
| Betti 自由格、torsion、\(\pi\) 的整矩阵及其 Smith 形 | \(\kappa_B\)、实际饱和指标、全部坏素数 | 有理正合性、平均分母 |
| 固定 de Rham 格及每个形式的完整约化坐标 | \(\kappa_{\mathrm{dR}}\)、\(\delta\)、逐 N 的 \(D_N\) / 全 content | 几何良约化、分子系数整数 |
| 保留的实际纯周期行与非零评价 | §6 的整数形式；同一形式的净衰减或 holonomy 秩输入 | 扩张非零、调节子非零、纯动机维数 |

Catalan 商上四弧部分已经由 §5 完成；真正剩余的有限任务是 \(M\to T\) 的整数 maps 与 de Rham 格识别。即使这些有限任务完成，简单极点、非负旋转不变整数分子仍受到 [实际正积分全族下界](odd_zeta_bridge_positive_integral_20261004.md) 约束：用原统一 \(D_N\) 时整数化积分增长，若要本原值趋零，content 的必要指数至少为 \(3/2-\log2\)。真实投影只去掉额外周期，不能使该下界失效；提高极点阶须重新核算算术成本，带符号形式须重新证明非零性。

对 ζ(7) 或全部奇 ζ，§2–4 是可复用的有限代数接口，尚缺一个跨权提供可用形式族及同一完整预算的定理。对 \(3\zeta(3)+\zeta(5)\)，也不能通过“按权分别去掉层”取得该实际组合：不同权 Tate 线之间没有任意混合的动机态射，组合可在数值配对中出现，其对象与周期行须直接构造。该区别不禁止研究组合目标，却防止把普通 Q 向量空间换基误认为动机投影。

本轮实际推进是：证明真实商拉回与整格指标界，计算 Catalan 商的两个不同整数指标，并给出两个可证明的操作障碍。尚未取得的输入仍是增长型形式约化、足够大的实际 content、非零性与解析净余量；它们没有被周期猜想的改写或抽象秩二对象的存在替代。

## 10. 原始资料与版本边界

- [Eskandari–Murty–Nemoto，2510.20648v3](https://arxiv.org/html/2510.20648v3)，2026-08-29；§6 是商不变部分的拉回，§7.3 是形式成员关系，§8.3.1 是简单极点算术输入。本文引用其已证明结构，整数四弧指标是本轮自行推导。
- [Dupont，1601.00950v3](https://arxiv.org/html/1601.00950v3)，2018-06-10；§4.4 的商奇偶分解及奇 ζ 拉回。指定权可用的无限形式族与净预算并非本文从中取得的定理。
- [Brown–Zudilin，2210.03391v3](https://arxiv.org/html/2210.03391v3)，2026-01-29；§4 提供真实 Betti 行选择与纯目标讨论；不以动机直觉替代全参数几何或整格证明。
- [Brown，模空间与无理性作者稿](https://www.ihes.fr/~brown/IrratModuliMotivesv8.pdf)，§8、Corollary 11.3；作为相对周期对象与经典秩二例子的原始背景，作者稿页码与本地 arXiv v1 不混用。
- [Kerr，1708.03836v2](https://arxiv.org/abs/1708.03836v2)，2020-06-12；本轮核对其 normal function 几何条件的研究方向，没有将其条件定理套到指定 ζ(7) 或 G。

文献下载和 manifest 由根任务统一维护；文件名年份只助识别，版本以归档 manifest 和明确的 arXiv 版本为准。
