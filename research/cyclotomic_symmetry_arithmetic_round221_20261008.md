# 第221轮：实际双悬挂的 parity 商与完整算术类型

2026-10-08。NEW 有限纸面推导。输入是已冻结220实际 Catalan suspension，完整系数式与 chi4 的奇支撑。本稿支付 x²商上的实际函数、秩和全部 prime-power系数类型；偶投影没有降低其已计费类型，奇投影的第三 lcm宽度可由1降到2/3。该改善有限，未证明严格 holonomy矛盾或新的数值定理。没有扫描，不否定全部 trace、投影或新坐标方法。

## 1. 实际完整输入与双悬挂

已实际 FULL读取 [cross_target_strategy_global_round220_20261008.md](cross_target_strategy_global_round220_20261008.md) 的全部八节、S1–S15、表格、出处与执行账本：18626 bytes，SHA256 93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42。这是本次源稿FULL阅读，不是重新FULL审其中每项文献。

采用同一初始分支

\[
A(x)=\sum_{j\ge0}\frac{(-1)^jx^{2j+1}}{2j+1},\qquad
B(x)=\sum_{j\ge0}\frac{(-1)^jx^{2j+1}}{(2j+1)^2},
\quad A'=\frac1{1+x^2},\quad B'=\frac Ax.
\tag{P1}
\]

设 G=g∈Q 为拟反证假设，取固定整数 c_g>0使 c_gg∈Z。令

\[
S_+(x)=\int_0^x\frac{B(v)-g}{1-v}\,dv,\qquad
S_-(x)=S_+(-x)=\int_0^x\frac{B(v)+g}{1+v}\,dv.
\tag{P2}
\]

后一等式由B奇性及实际换元得到，不把积分方向漏掉。初始分支 B(1)=G、B(-1)=-G，所以该假设分别填补 S_+在1、S_-在-1的引入奇点；两函数都可沿实初始分支经过±1。这是具体分支的补点，不是任意共同图或任意继续分支的亚纯性。

置

\[
E=(S_++S_-)/2,\quad O=(S_+-S_-)/2,\quad t=x^2,
\]

\[
a(t)=A(x)/x,\quad b(t)=B(x)/x,\quad
e(t)=E(x),\quad o(t)=O(x)/x.
\tag{P3}
\]

这些是原点全纯Q[[t]]芽；除以x的零点可去。直接求导给出

\[
E'=\frac{B-gx}{1-x^2},\qquad
O'=\frac{xB-g}{1-x^2},
\]

\[
2t a'+a=\frac1{1+t},\quad
2t b'+b=a,\quad
e'=\frac{b-g}{2(1-t)},\quad
2t o'+o=\frac{tb-g}{1-t}.
\tag{P4}
\]

因此完整五行(1,a,b,e,o)有显式Q(t)连接，两个四行(1,a,b,e)、(1,a,b,o)各在微分下闭合，均holonomic。初始 t=1分支有b(1)=g；P4的两悬挂右端可去。t=0方程中的表面极点不破坏所指定的全纯芽；别的继续分支仍须实际核验。

令 H_n=sum_(0<=j<n)(-1)^j/(2j+1)^2，H_0=0。220完整系数式给出

\[
a_n=\frac{(-1)^n}{2n+1},\quad b_n=\frac{(-1)^n}{(2n+1)^2},
\]

\[
e_0=0,\quad e_n=\frac{H_n-g}{2n}\ (n\ge1),\qquad
o_n=\frac{H_n-g}{2n+1}\ (n\ge0).
\tag{P5}
\]

并有(2theta_t+1)o=2theta_t e-g。这是微分关系，不是可以免费删掉一行的Q(t)线性关系。

## 2. 完整秩没有因 parity 自动减少

先独立核输入所需的四行秩。绕i的实际单值化给Delta A=pi、Delta B=pi log x+C。对1,A,B的有理关系作单值化，B项非零会使log x有理；故三行C(x)独立。若 S_+=r0+r1A+r2B，微分比较B系数将给r2'=1/(1-x)，有理函数导数无简单极点残数，矛盾。故1,A,B,S_+秩四，此证明不依赖g是否等于G。

若完整双悬挂只有秩四，可解出

\[
S_-=r_0+r_1A+r_2B+c(x)S_+,\qquad r_j,c\in C(x).
\]

求导，左端及S_+'都在前三行内；已有四行独立迫c'=0。比较B系数于是给

\[
r_2'=\frac1{1+x}-\frac{c}{1-x},
\tag{P6}
\]

其-1处残数为1，仍不可能是有理函数导数。完整(1,A,B,S_+,S_-)秩五。

P3的变换在C(x)中可逆，且C(t)⊂C(x)。所以(1,a,b,e,o)在C(t)上也独立，完整双悬挂秩五；分别删除e或o的四行均秩四。这是实际函数身份，不是某个截断矩阵的满秩猜测，也没有依赖待证的G无理性。

下面的“完整源”分别指(Z[t]_(<=D))^4或五行版本；所有方向及全部0,...,N系数保留，不宣称有限jet单射或数值行列式非零。

## 3. 奇支撑的准确lcm与全部prime powers

写 d_M=lcm(1,...,M)，

\[
q_M=\operatorname{lcm}\{k\le M:k>0\ {\rm odd}\}
=d_M/2^{\lfloor\log_2M\rfloor},\quad q_0=d_0=1.
\tag{P7}
\]

所有odd prime powers仍在q_M中。去掉偶指标只去掉2的部分，log q_M=M+o(M)，与log d_M只差O(log M)，不是将宽度M减半。

偶投影的安全全部幂包为

\[
q_{2n}^2 d_n\, [t^n](2c_ge)\in Z\quad(n\ge1).
\tag{P8}
\]

证明：系数是c_g(H_n-g)/n。对oddp令h=max{j:p^j<=2n}。若2n>=2p^h，则d_n含p^h，三层总指数3h覆盖n k²的分母。若2n<2p^h，则d_n至少含p^(h-1)（p>=3）；偶数2n不可能等于odd p^h，所以v_p(n)<=h-1，而k<=2n-1有v_p(k)<=h，得到总指数<=3h-1。固定g项由c_g及d_n清除。p>2n没有分母。

在2，每个H_n的分母为奇数，c_g(H_n-g)是2整；P8的d_n清除外层n的全部2幂。未乘固定2时e还需2n；这个固定因子已显式支付。

奇投影可有较窄的第三层。以下lemma是本轮实际改善：

**Odd outer-index lemma.** 若M为正奇数，k<M也为正奇数，则

\[
M k^2\ \mid\ q_M^2q_{\lfloor M/3\rfloor}.
\tag{P9}
\]

按oddp全部幂证明。令h=max{j:p^j<=M}；p>M时无需清除。若M>=3p^h，则第三层含p^h，足够3h。若M<3p^h，第三层至少含p^(h-1)，因为p>=3且M>=p^h。如果v_p(M)=h，奇性排除M=2p^h，故M=p^h、v_p(k)<=h-1，总分母指数<=3h-2；否则外层指数<=h-1，总分母指数<=3h-1。两种都被2h+(h-1)覆盖。M=1及第三层为0的初始情形直接成立。2根本不出现在Mk²。

取M=2n+1，由P5逐项及固定c_g得到

\[
\boxed{q_{2n+1}^2q_{\lfloor(2n+1)/3\rfloor}\,
[t^n](c_go)\in Z.}
\tag{P10}
\]

固定g/M项只需q_M，已包含。a,b也无2分母；c_go是2整。P8/P10覆盖所有素数和高幂，不只覆盖large-prime窗口，也不要求项间相消。

完整四/五行的全jet均可由

\[
M_N=q_{2N+1}^2d_N
\tag{P11}
\]

清除，行列表为(1,a,b,2c_ge,c_go)。对odd四行可用更小的q_(2N+1)^2q_floor((2N+1)/3)。这些乘数也清除完整多项式源的系数输出：每个移位只读取更小的索引，乘数单调；没有漏掉源方向或借助截断取消。

## 4. 全系数分母主项：可证明的必要性

令 Den_f(N)为f系数0,...,N的最小正公分母。a,b的分母是精确的：

\[
Den_a(N)=q_{2N+1},\quad Den_b(N)=q_{2N+1}^2,
\quad\log Den_a=2N+o(N),\quad\log Den_b=4N+o(N).
\tag{P12}
\]

所以(2n+1)^2不能误写成literal n²。对任意固定整数C及固定e，取oddp不除C并令n=(p-1)/2：p不除n，而C n^e b_n仍有p深度二。不存在固定倍数将这一行转成只有n^e分母的类型。

悬挂行也有精确主项，虽不在此求有限最小分母。以下prime论证都排除有限集p|6c_g；它只影响o(N)。特别在odd下界选M=3p时排除p=3，使外层p-depth恰为1。

对even，n=p时H_p内唯一的odd p倍数是p，其chi4系数为±1，故v_p(H_p-g)=-2，再由外层n得v_p([t^p](2c_ge))=-3。对N<p<=2N-1，取n=(p+1)/2<=N，H_n仍仅有一个p项，外层n为unit，深度二。因此P8/P11上界与weighted PNT下界匹配：

\[
\boxed{\log Den_{2c_ge}(N)=5N+o(N).}
\tag{P13}
\]

具体下界是3theta(N)+2(theta(2N-1)-theta(N))+o(N)=5N+o(N)。所以奇支撑没有使even完整系数包主项便宜。

对odd，p<=(2N+1)/3取2n+1=3p。内层只含p、不含3p，偶2p不在支撑；外层再给一个p，深度三。对(2N+1)/3<p<=2N-1，取n=(p+1)/2，内层p深度二、外层p+2为unit。P10给匹配上界：

\[
\boxed{\log Den_{c_go}(N)=\tfrac{14}{3}N+o(N).}
\tag{P14}
\]

这里没有prime scan，使用的是每个oddp的显式索引选择及PNT。p-power的上界已经在§3完整支付；下界只用prime就足够确定主项。完整五行的最小共同系数分母主项仍为5N，因为even行在其中。P13/P14是逐行全jet分母结论，不是最优联合source lattice指数或最优CDT费用定理。

## 5. 合法CDT类型与实际改善的大小

固定c_g、2的整行倍数不改变秩，只给固定有限常数；没有按n变化的免费倍数。CDT固定v2 Remark6.0.12容许lcm中的固定cutoff平移，因此2n+1及floor((2n+1)/3)可以按宽度2、2/3登记。这个平移不是把2n+1替换成literal n。

偶四行(1,a,b,2c_ge)有两种安全登记：

|类型|row sums sigma|literal vector e|费用|
|---|---|---|---:|
|两列width2，保留外层n|(0,2,4,4)|(0,0,0,1)|27/8+7/16=61/16|
|三列width2,2,1|(0,2,4,5)|0|61/16|

第二表由P8得到；第一表来自n q_(2n-1)^2。单literal n的7/16仍必须支付。偶投影没有由此获得较低CDT费用；更精细联合格不在此否定。

奇四行(1,a,b,c_go)由P10有合法staircase三列

\[
b=\begin{pmatrix}
0&0&0\\2&0&0\\2&2&0\\2&2&2/3
\end{pmatrix},\quad e=0,\quad
\boxed{\tau=\frac{3\cdot2+5\cdot4+7\cdot(14/3)}{16}
=\frac{11}{3}.}
\tag{P15}
\]

与安全半宽61/16相比，改善为7/48。这是真正全系数类型改善，未声称这是奇四行的最优费用或已通过解析门槛。

改善的来源是P9的odd outer-index，而非平方坐标本身。在原x坐标完整四行(1,A,B,c_gO)中，O的偶系数为0，奇指标M的分母已由q_M²q_floor(M/3)全部支付。因此同一论证给合法三列widths1,1,1/3、sigma=(0,1,2,7/3)，

\[
\tau_x=\frac{3+10+7(7/3)}{16}=\frac{11}{6}.
\]

相对于220原x源已付的半宽表61/32，这里降低7/96。下降到t=x²后各width乘2，P15的11/3及降低7/48也恰乘2；这不是可以保留旧x解析容量的免费gain。

完整五行最简单的普通staircase cap仍可用sigma=(0,2,4,5,5)、e=0，费用106/25。不能把排序row sums(0,2,4,14/3,5)重组为普通staircase widths2,2,2/3,1/3：even行需要d_n，而d_n不被d_floor(2n/3)d_floor(n/3)逐素数覆盖，特别漏掉p∈(2n/3,n]。row sums不是完整prime-power产品身份。

如果明确改用CDT Theorem8.0.1的arbitrary-array版本，还能保留真实的非staircase矩阵

\[
b_*=\begin{pmatrix}
0&0&0\\2&0&0\\2&2&0\\2&2&1\\2&2&2/3
\end{pmatrix},\quad e=0.
\tag{P16}
\]

本次实际重读固定PDF pp122–123的完整定义/定理。由其balanced计数定义，可以纸面给出

\[
\boxed{\tau_{\flat\flat}(b_*)\le21/5,}
\tag{P17}
\]

不冒称sharp值。证明：按列分别上界总计数，前两width2列贡献48/25+42/25=18/5。第三列只有两个各占1/5的类别。写threshold为s=k/N，其计数比例至多

\[
C(s)=\min\{2/5,\ (1-s)_+,\ 1/5+(1-3s/2)_+\}.
\]

三项分别来自类别总quota、所有命中索引必须n/N>=s、以及width1类别quota加width2/3可命中索引。balanced/discrepancy误差在定义的极限中消失。C(s)依次为2/5（0至8/15）、6/5-3s/2（8/15至2/3）、1/5（2/3至4/5）、1-s（4/5至1），之后为0。故2∫C(s)ds=3/5。逐列max的和只作upper bound，不要求不同列的最优排列同时达到；加总给21/5。

前两列的48/25+42/25也可同时达到：把零类别放在最早的1/5索引、仅第一列非零类别放在随后1/5、其余三类别放在末尾3/5（整除误差消失）。第三列非负，所以同一计数定义给18/5<=tau_flatflat(b_*)<=21/5。这里只确定区间，未求sharp third-column值；21/5上界本身不能推出holonomy gate失败。

固定cutoff偏移可按b_*+epsilon处理：每项threshold最多移动epsilon，因为0<=n/N<=1，积分计数上界每列最多增加2epsilon。有限初始系数统一缩放后，再令epsilon趋0，不改变P17的费用上界。P17使用的定理与普通staircase不同，不能用其row sums直接计算flat。它仍要求共同meromorphic pullback、函数独立及严格holonomy quotient；本稿只支付其中的算术类型和秩。

## 6. x²及后续缩放不能免费改变比较对象

t=x²商把t-coefficient index N对应到x中的2N或2N+1；次数D的t-polynomials对应次数2D的even x-polynomials。原点x->t有分歧，不能仅将旧x图平方就称为有非零原点导数的t图，也不能保留旧图导数却使用新的t分母。P12的2N、4N正是完整系数索引变化的实际成本。

若再取t=kappa v，kappa=A0/B0∈Q^*既约，f(kappa v)的n项乘kappa^n。安全全jet乘数需附加B0^N；此项包含每个p|B0的全部指数，特别不得遗漏2。kappa为整数时没有此新分母，但finite-prime收益和实处改变仍须配套；共同图在v坐标的导数为旧t导数/kappa。把t源列改成v^k、jet重新缩放也会改变行列基，不能只保留有利的一边。

例如t=2v确能清除even行余下的dyadic n分母（固定2c_g已支付，n>=1有2^n/n在2整），但移除的dyadic全jet部分仅O(log N)，不改变P13的5N主项；图导数同时减半。没有由此获得免费指数优势。

本稿未求所有t图的导数上界或能量。初始t=1补点、有限分母改善、任意继续分支下的共同meromorphic拉回，以及严格rank quotient是四项不同要求。geometry由另稿实际核验，本稿不预借该结论。

## 7. 当前有限结论与阅读/执行范围

even四行保持rank4，61/16费用表未降，逐行全jet分母主项5N也未降。odd四行同样rank4，但odd outer-index lemma支付原x源11/6、下降t源11/3的合法费用表；完整double suspension需要rank5，普通cap106/25，明确换用arbitrary-array版本可得18/5至21/5的区间。这些是有限、同源的算术改进与必要性lemma，不是所有trace失败或新数值证明。

除§1的cross220 FULL读取外，CDT source是已固定的 literature/cdt2024_l2_chi_minus3.pdf，218页、4517169 bytes、SHA256 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。本轮完整重读pp122–123的Theorem8.0.1/定义，复用上一轮已完整读取的pp16–18、66–70及固定shift Remark6.0.12；不是FULL文献审阅。没有使用20页短稿代替固定主文。P1–P17及P13/P14的PNT使用均为有限纸面推导。

数学程序、CAS、矩阵执行、prime/parameter扫描、PSLQ、数值积分、Lean、Git均为零。工具只用于实际文档FULL读取、PDF选页文本、NEW稿保存和SHA256。没有改旧数学稿、main或manifest。保存后将实际FULL作者复读最终七节文件并在外部报告bytes/SHA256；作者复读不替代独立审阅。
