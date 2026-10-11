# 第221轮：CDT 实际 trace 的收益与 χ4 关系保持入口

2026-10-08。NEW 有限文献/纸面接口稿。输入为第220轮完整 cross-target 和 global 报告；目标仍是新 ζ/L 数值结论，**本稿没有新的无理性或数值线性独立定理**。只使用一项 primary：已有218页 CDT fixed v2，不重复下载。新阅读页段与阅读账保存在 `literature/trace_sources_round221_20261008/`。不改旧稿、main、manifest；数学程序0。

## 1. 实际 χ−3 证明：先有关系芽，再有 trace

CDT 先从真实 Zagier/Eichler 函数构造

\[
H=aH_A+bH_B+cH_C,
\quad a+bL(2,\chi_{-3})/2+c\zeta(2)/4=0,
\tag{T1}
\]

而不是从一个大导数图反推目标。\(H_B-(L/2)H_A\)、\(H_C-(\zeta(2)/4)H_A\) 的实际 radius 从1/9扩到1；有理关系使 H 属于 Q[[x]] 且具有 \(d_n^2\) 类型。trace 随后取

\[
w(x)=\frac{x}{x-1},\qquad y=x+w(x)=\frac{x^2}{x-1},
\quad G_H(y)=H(x)+H(w(x)).
\tag{T2}
\]

两个对应已补点1/9和−1/8在 quotient 中合并为−1/72；4是二阶 elliptic branch point。trace 没有创造原先不存在的 overconvergence。[CDT §§11.1–11.2、13，printed/PDF pp159–164、171–173](https://arxiv.org/pdf/2408.15403v2)

实际 proof 的包是 **14行：7个 pure functions + 7个由非平凡关系产生的函数**，完整函数独立性由 Lemmas12.0.1、12.1.1 支付。它不是 Theorem C 的17行包。§13 的费用为 \(16603/3920\)，最终 strict quotient 小于14；本稿没有重跑作者的数值积分或 appendix 的排除前像计算。这里引用已证明的 χ−3 theorem 解释机制，不把它计为本项目新成果。

因此可迁移的结构条件是：有理关系先进入一个实际 Q-germ；其初始 leaf 上确有延拓改善；投影不杀掉关系诱导的新函数；完整 projected source 的函数秩、分母和共同图均另付。

## 2. 粗 trace 没有净指数红利，fine trace 才可能有

Lemma9.0.3 的具体算术证明使用整数多项式

\[
P_k(y)=x^k+w(x)^k,\quad
P_k=yP_{k-1}-yP_{k-2},\quad
\operatorname{ord}_0P_k=\lceil k/2\rceil.
\tag{T3}
\]

因此 y 的第n项接收 x 的 k∈[n,2n] 项。\(d_{cn}\) 变为 \(d_{2cn}\)，不是减半。对 **w-stable** 完整 Q(x)-module，Galois descent 保持其 Q(x)-秩为 quotient 的 Q(y)-秩；不能对任意单函数 trace 宣称保秩。Basic Remark9.0.20 证明配套图的能量、log导数、粗费用都乘2，普通粗 holonomy quotient 完全等价。

实际优势在 §10.3：plus projection 保留 literal 外层 n 的 integrated type；minus projection一般会把该因子损坏成额外 lcm layer。故原域17行与 descended14行并非“秩越大越好”：14行的细费用/几何约束更强。这里的 n 必须仍通过 \(\tau_\sharp\) 支付，trace 不使它免费。固定 lcm cutoff shift 可按 Remark6.0.12 处理，但该 remark 不是任意 shifted literal denominator 的免单定理。

CDT 的 odd/even 对称性另有具体限制：\(\lambda(-q)=w(\lambda(q))\)，对称 inner map 才满足 descent 的图对称；Remark10.1.8 也只为特定 even-depth J-functions 陈述2-adic单位盘性质。不能把 these facts 扩成所有 odd-support germs 的全源整性。

## 3. 分支、elliptic fiber 与关系保留不是形式标签

Lemma9.0.13 和 Corollary9.0.19 实际要求：contractible target neighborhood、其 univalent leaf 包住所有已补点前像、其余 singularities 被图避开、原点前像约束，以及4-fiber的 even ramification。plus/minus 的形式恒等式本身没有付这些条件。

χ−3 proof 的 \(\Sigma^0=\{-1/72\}\) 位于实际小线段 leaf，\(\Sigma^1=\varnothing\)。Appendix A.4 给所构造图的唯一−1/72前像；A.5 使用它的真实能量。**一个 canonical 初始值关系不必在所有其他前像的 continuation leaf 上仍使同一分子为零。** 下文 χ4 的图专门证明唯一前像和正确 branch；不把全部 universal cover 当自动 admissible。

## 4. χ4：普通偶 trace 会丢目标，悬挂偶投影可保留

复用第220轮实际

\[
A(x)=\arctan x,\quad B(x)=\operatorname{Ti}_2(x),\quad B(1)=G,
\quad S_g(x)=\int_0^x\frac{B(t)-g}{1-t}\,dt.
\tag{T4}
\]

A、B 都为 odd-support Q-series。**B 的普通偶 trace为0**，所以“留下偶项降低费用”会直接杀掉目标。T2 的 w-trace 与此 x↦−x 的 character trace也不是同一个算术/解析对象。

一个实际保留目标的有限迁移是

\[
y=x^2,\quad a(y)=\frac{A(x)}x,\quad b(y)=\frac{B(x)}x,
\quad T_g(y)=\frac{S_g(x)+S_g(-x)}2.
\tag{T5}
\]

在0由 even germs 唯一定义这些 Q[[y]] 函数。直接微分得到

\[
a'=\frac{(1+y)^{-1}-a}{2y},\qquad
b'=\frac{a-b}{2y},\qquad
T_g'=\frac{b-g}{2(1-y)}.
\tag{T6}
\]

因此 \(b(1)=G\) 被保留；假设 G=g 时实际初始1点可去。取完整行

\[
1,\quad J_1(y)=ya(y),\quad J_2(y)=yb(y),\quad T_g(y)
\tag{T7}
\]

有显式有理 connection：\(J_1'=J_1/(2y)+1/[2(1+y)]\)、\(J_2'=(J_1+J_2)/(2y)\)、\(T_g'=(J_2/y-g)/[2(1-y)]\)，常数行导数0。

其 C(y)-秩为4，不借 motivic rank。前三行若相关，拉回 x 并乘x，得到 1,A,B 的 C(x)-关系，违背第220轮已付的 actual monodromy 证书。若 \(T_g=r_0+r_1a+r_2b\)，按独立函数比较导数给

\[
r_2'-\frac{r_2}{2y}=\frac1{2(1-y)}.
\tag{T8}
\]

有理 r2若在1有极点，左侧 derivative 的最高极阶无法抵消；若无极点，左侧在1全纯。两种情况都不能等于右侧简单极点，故 r2不存在。这个秩证明对任意常数g成立。

这是重新选择并证明一个保留目标的 projected source；**不是**把原来不在 x↦−x 下稳定的四行 module 直接套入 CDT 的保秩 descent。

## 5. 实际图与预算：保留桥，但未优于220最好基线

令 \(\alpha=3\pi/8\)、\(\phi(z)=\tan(\alpha z)\)，复用220的完整实际图。它 odd，避开±i，只有一个0前像，±1各有一个实前像±2/3。故

\[
\Psi(z)=\phi(\sqrt z)^2=\tan^2(\alpha\sqrt z)
\tag{T9}
\]

在闭盘邻域全纯，\(\Psi'(0)=\alpha^2\)，唯一1前像为4/9。a、b的拉回都是对应 odd 函数除以 odd \(\phi(\sqrt z)\) 后的 even analytic function；T的拉回是 S 两个实际 branches 的 even平均。G=g 时两者到达初始 ±1 leaf并补点，因此全部四行在同一实际图下全纯。不是只核一个形式局部展开。

零次系数 \([y^0]J_1=[y^0]J_2=[y^0]T_g=0\)；对 \(n\ge1\)，其余全系数为

\[
[y^n]J_1=\frac{(-1)^{n-1}}{2n-1},\quad
[y^n]J_2=\frac{(-1)^{n-1}}{(2n-1)^2},
\]
\[
[y^n]T_g=\frac1{2n}
\left(\sum_{k=0}^{n-1}\frac{(-1)^k}{(2k+1)^2}-g\right).
\tag{T10}
\]

对固定g，清除固定整体分母与2后，合法类型为

\[
\sigma=(0,2,4,4),\quad e=(0,0,0,1),\qquad
\tau=\frac{27}{8}+\frac7{16}=\frac{61}{16}.
\tag{T11}
\]

内层 odd denominators 2n−1 不能假装是 theorem 的 literal n：其大素因子可落在(n,2n)，根本不由 n 清除。T10真正的外层n仍计 \(7/16\)。2-adic integer numerator / odd support 对前三行真实成立，但这个好处在220的A、B中已经存在，不能再次计作新信用。

对任意已付 odd 配套图，平方 quotient 给 \(\log|\Psi'(0)|=2\log|\phi'(0)|\)。因
\(\phi(v)^2-\phi(t)^2=(\phi(v)-\phi(t))(\phi(v)-\phi(-t))\)，Haar对称性给 \(J(\Psi)=2J(\phi)\)。因此 T11 相比220较粗的 \(17/8\) 表机械加倍省下7/16；但它恰等于 **220已付较好半宽表61/32的两倍**，尚未改善最好基线。

220已证明所有原四行 actual共同图须避开±i，\(|\phi'(0)|\le\rho=\pi F(1/2)^2<e^{3/2}\)。对本节的 odd配套/可提升图族，故 \(\log|\Psi'(0)|<3<61/16\)，没有普通 fine CDT 的正分母；当然也没有 strict quotient<4。这个范围不扩大成所有未知 y域 multivalent图的导数上限，也不排除新的联合 prime flags。现有“去掉一半项”没有兑现净 arithmetic holonomy 红利。

### 5.1 本轮新 odd 源：支撑确有改善，坐标本身没有

另稿 [cyclotomic_symmetry_arithmetic_round221_20261008.md](cyclotomic_symmetry_arithmetic_round221_20261008.md) 已支付不同的实际行：\(O(x)=(S_g(x)-S_g(-x))/2\)，以及 \(o(t)=O(x)/x,t=x^2\)。本 agent 对该稿全7节/P1–P17实际FULL阅读，当时读取身份12848 B、SHA256 `6e4319d07558b35beccc7f0c6addb9c73de981a77db15d239aab922aca59c644`；这是新增输入阅读，不冒充该稿独审或声称FULL读取其后来修改版本。其 odd outer-index lemma：正奇数 M、正奇数 k<M 时，\(Mk^2\mid q_M^2q_{\lfloor M/3\rfloor}\)，其中q仅取奇数lcm。全部odd prime powers的理由是：若M<3p^h，奇性禁止M=2p^h；若外层有最高h幂，则M=p^h、内层最多h−1幂，否则外层最多h−1。2不出现。

由此实际x四行 \((1,A,B,O)\) 的合法宽度为 \((0,1,2,7/3)\)，e=0，费用 **11/6**；t四行 \((1,a,b,o)\) 的费用 **11/3**。这是相比220最好已付61/32降低 **7/96** 的真实支撑改进。odd支撑不是简单将q_M宽度减半；\(\log q_M=M+o(M)\)，新的信用来自外层与内层皆为奇数时第三层可缩到M/3。

但是这两张新表配套的 \(J\)、log导数、费用恰好都加倍，秩同为4，故同一源的x/t holonomy quotient仍完全相等。下降坐标没有再次创造7/96信用。实际tan图的o拉回由odd \(O\circ\phi\) 除以odd \(\phi\) 可去，目标±1 branches与T9同样付清；已有 \(\log\rho<3/2<11/6\) 仍排除该x源普通single-map的正分母，对配套t图则 \(2\log\rho<3<11/3\)。这是有限的新进展但未过gate，不是所有character trace方案的no-go。

## 6. 可继续的精确条件与暂不兑现的入口

下一步若沿T5继续，必须支付至少一项真实改变：odd-shift分母的**完整联合 source**成本严格优于T11 / 220半宽基线，或者构造不只是上述平方配套图的新 geometry并核所有0/1前像的实际 leaf。同时证明完整函数秩与最终 quotient<4；不能只比较正分母、motivic维数或若干局部 entries。

CDT自身还记录 \(B_5(4)=8G\)、该 pure函数的具体 factorial/odd-shift分母及有限二阶 elliptic monodromy。B5已出现在既有 mechanism稿的pure-function包，本轮不是首次发现或新付清carrier，也不重启旧同源的“再加积分行”。这里只登记条件障碍：在实际初始4-leaf上悬挂 \(\int(B_5-8g)/(y-4)\,dy\)，G=g可取消 constant residue，剩余 Puiseux 项可在二重覆盖下解析。但其他4-fibers的continuation值、全局finite2 monodromy、共同leaf、y/4缩放的同源分母/实处、完整函数秩和严格能量均**未付**；本稿不推进成新主线。不能因为原B5可以通过even ramification，就自动对其新悬挂使用同一Corollary9.0.19。

对一般非主实 Dirichlet even L值，正确的 character component先决定应取 invariant还是twisted projection；投影可能湮灭目标，也可能将多个 target values混成 trace。须给出实际 endpoint relation的系数矩阵、证明被保留的目标关系非零，再付对应puncture/branch源。这里没有用抽象 motive splitting 代替它，也没有宣称已找到普遍便宜载体。

判断：T5已新增一个**实际保目标、完整rank4与合法分母的纸面trace接口**；该even接口相对粗表的收益解释了fine trace的作用，却未优于220最好已付方案，只保留为benchmark。另稿odd源已降低费用7/96，须准确计为支撑收益；坐标下降自身无净收益，该新表仍未过gate。停止在固定T11或固定odd表的平方图族中微调。Ti2(1/2) novelty未在本任务核；本稿没有引入其已有或未有无理性结论。

## 7. 最终身份、文献范围和程序账

输入实际FULL：global220全部6节，9404 B，SHA256 `965cf97700f9a0cf86ea3fb4dd4ea334f78331897d5b8ffc36d6fce62e0c7ff4`。cross220为既有最终作者FULL/已独审版本，18626 B，SHA256 `93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42`；本轮再次核身份并复用实际已付公式。

CDT fixed v2源：`literature/cdt2024_l2_chi_minus3.pdf`，4517169 B，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`，218页。实际本轮读取 **printed/PDF pages146–174全页连续范围、67–68全页、203–205全页**：完整§9（末尾在153），§10.1–10.3、§11、§12、§13及相关跨页；67–68含Remark6.0.12完整内容；203–205含实际A.4图、唯一前像lemma和A.5预算。174末Theorem C开头虽实读，不扩张为该proof FULL阅读。没有FULL218页。

新文件夹保存 locator及上述页段文本、reading_scope；**全文PDF下载/文本提取不等于全文阅读**。本轮只有一个primary，未新增其他external论文；既有CDT未重复下载。source的数值计算只作为已发表proof事实，未在本轮独立执行或复证所有appendix数值。

数学程序0；CAS0；矩阵执行0；prime/parameter grid0；PSLQ0；Lean0；Git0；数值积分0。工具为 documentary rg、PDF→text提取、页段读取/归档、metadata/SHA256和本NEW Markdown保存/作者FULL复读。T5–T11为有限纸面推导；没有数学软件验证。保存稿final作者FULL阅读与bytes/hash在handoff单独登记，不在正文自指写hash。
