# Li2 背景、平方根积分的一次新扩张与限定预算障碍

日期：2026-10-06。本稿新建，既有报告冻结。本文给出实际闭合的十维背景、一个积分商的结构证明，以及三个明确类型族的预算下界。没有证明任何新的数值无理性，也没有排除任意换基、Hasse 格、所有背景或所有 arithmetic holonomy 方法。

## 1. 原始来源与固定规范

固定原件为 [CDT 作者版](../literature/cdt_l2_chi_minus3_author_20261005.pdf)，220页。§10.3、PDF pp157–158 给出八个实际独立的 multiple polylogarithm；§10.1、pp155–157 给出在它们之外的平方根积分。§5、pp63–66 与 Definition6.0.1 给出积分的分母成本，不能把增秩当成免费。

置
\[
 L=-\log(1-t),\qquad T_j=L^j/j!,\qquad Q=\operatorname{Li}_2(t),
\]
\[
 Z=\operatorname{Li}_3(t),\qquad
 M=\operatorname{Li}_{1,2}(t)=\sum_{n\ge1}\frac{t^n}{n}
       \sum_{k=1}^{n-1}\frac1{k^2},\qquad R=LQ,
\]
\[
 K=K_2=\frac1{\sqrt{1-t}}\int_0^t
                  \frac{L(u)}{u\sqrt{1-u}}\,du,
 \qquad I=\int_0^t\frac{K(u)}u\,du.
\]
每个函数取0处实的正则芽，积分常数为0。平方根取值1。K 的完整整性及最高素数 packet 已在
[平方根积分报告](cdt_odd_algebraic_helpers_20261005.md) §§3、5 严证；本文不以有限数值取代该输入。

## 2. 十维实际闭包，而非形式解空间

设
\[
 \mathcal P_{10}=\langle 1,L,T_2,Q,T_3,R,M,Z,K,I\rangle_{\mathbf C(t)}.
\]
其连接方程为
\[
\begin{array}{lll}
 L'=1/(1-t),&T_2'=L/(1-t),&Q'=L/t,\\
 T_3'=T_2/(1-t),&R'=Q/(1-t)+2T_2/t,&M'=Q/(1-t),\\
 Z'=Q/t,&K'=K/[2(1-t)]+L/[t(1-t)],&I'=K/t.
\end{array}                                                    \tag{1}
\]
故这是完整微分闭包，所有有限奇点均在0、1；不是仅写下某个高阶方程就计满其全部解。

CDT (10.3.2) 的八个函数正是 \(1,L,T_2,Q,T_3,R,M,Z\)，在 \(\mathbf C(t)\) 上实际独立。这个八维系统的连接是严格三角的，其全部 composition factors 为 trivial。\(\langle1,L,K\rangle\) 的真实 sign 商具有齐次解 \((1-t)^{-1/2}\)，其最小秩为3（已审平方根报告§4）；因此 K 不在该八维 trivial 系统中。这也对应 CDT §10.3 明言的第九个独立函数。

**I 给一个真正的新方向。** 若 I 在前九个函数的有理函数域 span 中，则可写
\(I=r(t)K+P(t)\)，其中 P 在八维 MPL 系统中。微分并比较实际独立的 K 系数，得到
\[
 r'+\frac r{2(1-t)}=\frac1t.                            \tag{2}
\]
任何 r 在0的极点都会使左边出现至少二阶最高极点；r 正则时左边正则。二者均与右边非零简单残数不符。因此 (2) 没有有理解，I 确实增加一维。结论为
\[
 \boxed{\dim\mathcal P_{10}=10.}                       \tag{3}
\]
\(\mathcal P_{10}\) 只含 trivial/sign factors。以已证 [level20 模型](cdt_odd_level20_model_20261006.md) 的单个目标 \(\mathcal W\) 为输入，其秩为4、模常数商是不可约 rank3 twisted Sym²。该不可约三维因子不可能来自本背景；故
\[
 \mathcal W\cap\mathcal P_{10}=\mathbf C(t)\cdot1,
 \qquad \dim(\mathcal W+\mathcal P_{10})=13.            \tag{4}
\]
两次 embedding 各自适用同一秩证明。本文不把两个目标的合并 rank7 与单目标的这张成本表混用。

加入 T4、T5 仍闭合。其新增独立性不只是“weight不同”：在 \(\mathcal P_{10}\) 中给定芽绕1重复 monodromy，差分对绕行次数至多三次多项式乘至多二阶符号周期；T4、T5 分别提供次数4、5。先取偶数绕行排掉 sign，再对最高次数作有限差分，即逐个排掉新增项。亦可在更大的 unipotent MPL 系统中使用 iterated-integral 的独立性。因此背景秩为11、12，与单目标结合后为14、15。

## 3. 全部素数的完整安全类型

记 \(D_n=\operatorname{lcm}(1,\ldots,n)\)，\(D_0=1\)。固定阶乘或固定有理规范的清因子不影响 CDT 的主成本。以下是所有 n、全部素数（包括2）的安全类型：

| 函数 | 不使用序号因子的类型 | 使用序号因子的类型 |
|---|---|---|
| L | \(D_n\) | \(n\) |
| Tj | \(j!\prod_{h=1}^jD_{\lfloor n/h\rfloor}\) | \(n\prod_{h=1}^{j-1}D_{\lfloor(n-1)/h\rfloor}\) |
| Q | \(D_n^2\) | \(nD_n\) 或 \(n^2\) |
| Z | \(D_n^3\) | \(nD_n^2,n^2D_n,n^3\) |
| R、M | \(D_n^2D_{\lfloor n/2\rfloor}\) | \(nD_n^2\) |
| K | \(D_n^2\) | 无需增添序号因子 |
| I | \(D_n^3\) | \(nD_n^2\) |

Tj 的两种类型及全部尺度的必要性已在
[纯 Tate 算术](cdt_odd_holonomy_budget_20261005.md) §1 证明，来自不同整数的 elementary symmetric polynomial 与 prime-power packing。Q、Z 的类型由系数 \(n^{-2},n^{-3}\) 直接给出。

R 的精确系数恒等式是
\[
 [t^n]R=\frac{2H_{n-1}}{n^2}+\frac{H^{(2)}_{n-1}}n,
 \quad H_N=\sum_{k\le N}1/k,\quad H_N^{(2)}=\sum_{k\le N}1/k^2.\tag{5}
\]
因此 nD_n² 清其全部系数。其 e=0 的较细型亦可不靠 (5) 证明：卷积一项为 \(1/[k(n-k)^2]\)。对任何 p^a，该层至多贡献两次；要贡献三次，两个指标都必须至少 p^a，故 \(n\ge2p^a\)。逐层相加便得 D_n²D_floor(n/2)。

M 的系数是 \(H_{n-1}^{(2)}/n\)。每一项 \(1/(nk^2)\) 在 p^a 层若贡献三次，则 p^a 同时整除 n、k 且 k<n，仍有 \(n\ge2p^a\)。这给同样的 e=0 细型。它不能粗写为“每行需要3个单位尺度”：安全型的总尺度仅5/2。

I 的系数为 K_n/n，故 nD_n² 及 D_n³ 都安全。这不是整数系数函数；所有安全型均须完整计入。

新行还保留明确的充分大素数下界：
\[
 p^2R_{p+1}\equiv1,\quad p^3R_{2p}\equiv1,
 \quad p^2M_{p+1}\equiv1,\quad p^3M_{2p}\equiv1/2\pmod p. \tag{6}
\]
R 在前者只有 Li2 的第 p 项能给两层，后者只有卷积指标 (p,p) 能给三层；M 在相应 harmonic sum 中只有 k=p 给两层。因此 e=0 时至少需要两条 b≥1 以及第三条 b≥1/2；任意 e≥1 时仍需两条 b≥1。

K 的旧精确 packet 给 \(p^2K_p\equiv1\)、\(p^2K_{p+1}\equiv1/2\)。故
\[
 p^3I_p\equiv1,\qquad p^2I_{p+1}\equiv1/2\pmod p.     \tag{7}
\]
所以 I 的 e=0 行至少有三条单位尺度；序号因子能消去第 p 项的一层，却不能消去 p+1 的两层。有限坏素数与固定 offsets 不改变这些渐近结论。

## 4. 对 K 的有理积分只能在这一层新增一次

这一结构结论限定于有理积分核的极点支撑 \(S=\{0,1,\infty\}\)，以及如下明确定义的0处 regularized holomorphic primitives。将 \(r(t)K(t)\) 的有限负次 Laurent 部分写为 \(\sum_{j\ge1}a_jt^{-j}\)，定义
\[
 F_r(t)=\int_0^t\left(r(u)K(u)-\sum_{j\ge1}a_ju^{-j}\right)du.\tag{8a}
\]
这里明确减掉 integrand 的 1/t 残数；等价地，原不定积分减掉有理 pole 部分及 \(a_1\log t\) 的积分奇部。任意原始 \(\int rK\) 不必在0正则：例如 r=1/t²、K=t+… 就有 log t。置
\[
 \mathcal R=\mathbf C[t,t^{-1},(1-t)^{-1}],\qquad
 \mathcal D=\partial_t+\frac1{2(1-t)}.
\]
则
\[
 \boxed{\mathcal R/\mathcal D\mathcal R
       =\mathbf C\cdot[1/t].}                         \tag{8}
\]
初等证明：0处 \(t^{-k}\)、k≥2，用 \(\mathcal D(t^{-k+1})\) 的非零最高系数 −k+1 消去；1处 \((1-t)^{-k}\)、k≥1，用 \(\mathcal D((1-t)^{-k+1})\) 的非零系数 k−1/2 消去；∞处次数 d≥0 的多项式，用 \(\mathcal D(t^{d+1})\) 的非零最高系数 d+1/2 消去。先减去∞多项式与0高阶极点，再处理留下的1处极点，不会重新产生其它高阶极点。只剩 c/t。其非零类由 (2) 的原点残数证明。

写 r=\(\mathcal Dg+c/t\)，由 (1)
\[
 \int rK\,dt=gK+cI-\int\frac{gL}{t(1-t)}\,dt.         \tag{9}
\]
式 (9) 先作为 punctured 原点域的不定积分身份，允许出现 log t。最后一项是有理核乘 L 的积分。减去有理导数后，简单核仅剩 1/t、1/(1−t)，给 Q、T2；其它项只给有理函数乘 L、常数和两种对数。按 (8a) 再减去有限积分奇部后，F_r 在0正则，而所有其它成员在0亚纯且无 log t，故 log t 的净系数必为零。因此 F_r 属于
\[
 \langle1,L,T_2,Q,K,I\rangle_{\mathbf C(t)}.
\]
被减去的 integrand 有限 Laurent 主部，其积分只给有理函数和 log t，故不增加新类。若原核已经满足 residue(rK)=0，则无需减 log t；不能把这个条件默认给任意 r。

两个透明的恒等式为
\[
 \int_0^t K(u)\,du=-2(1-t)K(t)+2Q(t),                 \tag{10}
\]
\[
 \int_0^t\frac{K(u)}{1-u}\,du=2K(t)-2Q(t)-L(t)^2.    \tag{11}
\]
所以在这一层，换一个有理积分核不能反复产生新的廉价 rank。结论不涵盖 K 的乘积、其它代数字符、对 I 再积分、额外 punctures 或非线性构造。

## 5. 共同解析叶确实保留

[完整 Hecke 叶报告](cdt_odd_level20_leaf_20261006.md) §8 已给共同映射
\(\Phi:(\mathbf D,0)\to\mathbf C\setminus\{1\}\)，唯一零点0，两个目标的 pullback holomorphic，且 \(1<|\Phi'(0)|\le16\)。这是本文解析输入，不从 endpoint cancellation 推出。

以上背景能共用该映射。L 的 pullback 由 D 上的 log(1−Φ) 定义；sqrt(1−Φ) 也有全局非零分支。Q、Z、M、I 等由 (1) 按顺序在 D 积分：含 Φ'/Φ 的源在0以源函数的零点消去，D 内没有其它 Φ 的零点，含 1/(1−Φ) 的源无极点。因此各 pullback 真正在整个 D holomorphic。闭圆盘邻域使用 Φ(rz)、r<1；有理函数系数造成的有限极点可用固定多项式清除。

此论证没有引入新 punctures。若加入 log(1−t^m) 等新字符，虽可能便宜增秩，却必须重新付对应根单位 punctures 的解析代价；当前 G cover 不会自动保留它们。

## 6. 三个明确类型族的精确预算仍不足

令 \(\lambda=\log|\Phi'(0)|\)，双重 Jensen 积分为 J。唯一零点与 Jensen 给 J≥λ；普通 holonomy 商 \(J/(\lambda-\tau)\) 若要严格小于 m，必要条件为
\[
 \lambda>\frac{m\tau}{m-1}.                          \tag{12}
\]
当前 Φ 省去1，且只有一个零点；CDT p24 的 Carathéodory 界给 λ≤log16。

最直接的 unit 类型表有：不含 I 的背景9与 target3 合为m12，其合法成本 \(54689/20160\)，门槛 \(54689/18480\)；加 I 后 m13 的合法成本 \(25477/9464\)，门槛 \(25477/8736\)。两者均超过29/10，失败。

我们进一步核对包含精细半尺度的明确 finite 自然类型族：L、Tj、Q、Z、R、M、I 可分别选上表的 integrated/flat 类型；K 取已证 D_n²；三个目标行保留已证的3个单位尺度。加入 T4、T5 后，同样纳入其两种完整类型。对每一配置，按各行的总尺度排序，用
\[
 \tau^{\flat\flat}(b)\ \ge\ \frac1{m^2}
          \sum_{i=1}^m(2i-1)\sigma_{(i)}              \tag{13}
\]
作合法放宽下界，再加完整的 CDT 积分成本 τsharp。式 (13) 是选择 comonotone 的 admissible 分布所得下界；不是把半尺度数组误当成 §6 的嵌套 binary 列。即使放宽后的值失败，真实 §8 transportation 成本也必失败。

独立 [成本证书](cdt_odd_level20_pure_budget_20261006_verify.json) 给出：

| 最大 log degree | 实际合并 rank m | 明确类型数 | 最小成本下界 | 必要 λ 下界 |
|---|---:|---:|---:|---:|
|3|13|768|1345/507|1345/468|
|4|14|1536|2577/980|2577/910|
|5|15|3072|1769/675|1769/630|

全部必要 λ 下界严格大于14/5，而 log16<14/5（e^(14/5) 的前11个正 Taylor 项已经超过16）。因此**这三个规定类型族不能用当前普通 Jensen 商完成 rank 矛盾**，已包括 Li2 和真正新增的 I，并没有漏记 integral 的序号成本。

这里没有声称任意 mixed gauge 的最优值，也不把指定族的有限精确分类推广成无限 log degree、所有 iterated integrals、convexity 或多映射的不可能定理。r6及以后并未完成本轮分类。

## 7. 下一输入与证书范围

可复用的新输入是实际十维模块 (1)–(4)、R/M 的完整5/2尺度型、I 的 shifted packet，以及一维有理积分商 (8)。后续有实质意义的改变须发生在实际整格/gauge、其它代数字符、更深的迭代扩张、convexity/多 map 或目标的 quotient，而不是只把本层 K 的不同积分再次计新维数。

[_verify.py](cdt_odd_low_cost_polylog_20261006_verify.py) 使用 Fraction 精确核全部连接方程、(5)、(10)–(11)、n≤84 的整个整数分母（包括2）、T1至T7 的两种类型，以及六个预先固定素数的 (6)–(7)。它另外逐项核成本证书的最终有理数及 log16 严格比较。所有全尺度与独立性证明在本文；有限检查不证明新数值无理性。成本 producer 由独立 agent 完成，文件链接为
[pure budget verify](cdt_odd_level20_pure_budget_20261006_verify.py)。
