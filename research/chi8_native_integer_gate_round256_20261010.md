# 第256轮：native χ−8 全前缀整数模型与完整投影费用

2026-10-10。本稿只处理255冻结的固定对象：a=1/√2、参数绕+1的同一实际继续叶T、3+T、N(i,j)=a^i\bar M(i,j)，以及所给n行整数contact prototype、整个raw pool j<2n与selected-even列。不换参数、向量、sheet、列池或数值目标。255 Root/A/B数学稿和报告已实际FULL读取，并逐文件验证255 manifest的bytes/hash相符；具体读域见 integer_reading_scope.md。

**结论：完整Z-prefix首关的算术部分通过。** 一个明确的、非最优但全prime-powers有效的清整因子是

\[
 d_m=\operatorname{lcm}(1,\ldots,m),\quad d_0=1,
 \qquad \boxed{q_H=2^{2H+1}d_{H+1}^{3}}\quad(H\ge0).
 \tag{I1}
\]

它同时清整所有0≤i,j≤H的完整rational heads与两period系数，并清整ordinary Z heads；不是只清目标period coefficient或某个有限n。下面给出全部估值、行高度、整数filter及selected-even determinant费用。共同actual contour的解析匹配由另一分工处理；本稿不把形式递推单独叫作该匹配证明。没有新的数值无理性/线性无关性定理、实际关系点无界非零或strict净能量。

## 1. 完整数组及所有强制头

保留255的实际period分解，c_l=4^{-l}binom(2l,l)，非法下标取0：

\[
 N(i,j)=R_{ij}+B_{ij}Y+C_{ij}\zeta(2),\quad Y=L(2,\chi_{-8}),
\]
\[
 B_{ij}=16a^{i-j}c_{(i-j)/2},\qquad
 C_{ij}=9a^{i-j+1}c_{(j-i-1)/2},\qquad R_{ij}\in\mathbb Q.
 \tag{I2}
\]

这是指定的完整系数分解，不以Y与ζ(2)未知的线性无关为前提。置μ_i=a^im_i、U_i=a^i\bar S_i。完整forcing为

\[
 \mu_{2l}=\frac{2^{l+1}(l!)^2}{(2l+1)!},\quad \mu_{2l+1}=0,
 \qquad U_i=-4\sum_{k<i}\mu_k,
 \tag{I3}
\]

其中U_0=0。两个边界rational heads A_d^-=R_{d0}、A_d^+=R_{0d}满足

\[
 A_0^-=0,\quad A_1^-=8,\qquad
 A_d^-=\frac{d-1}{2d}A_{d-2}^-+
 \frac{U_{d-2}/2-U_d}{d}\quad(d\ge2),
 \tag{I4}
\]
\[
 A_0^+=A_1^+=0,\qquad
 A_d^+=\frac{2(d-2)}{d-1}A_{d-2}^+
 +\frac{16}{(d-1)^2}\quad(d\ge2).
 \tag{I5}
\]

全数组还包含以下完整有限头，未舍弃任何raw列：i≥j、d=i−j时

\[
 R_{ij}=A_d^- -4\sum_{k=1}^j\frac{\mu_{d+k-1}}k;
 \tag{I6}
\]

i<j、d=j−i时

\[
 R_{ij}=A_d^+ -4\sum_{k=d+1}^j\frac{\mu_{k-d-1}}k.
 \tag{I7}
\]

0≤i,j≤H时，这些μ下标至多H−1、divisor k至多H；边界(I4)使用U_d至多H。所有后续清整包括这些完整sums。

## 2. moment清整：所有prime powers一次支付

对任意prime p及b=p^e，用l=qb+r、0≤r<b得

\[
 \left\lfloor\frac{2l+1}{b}\right\rfloor
 -2\left\lfloor\frac lb\right\rfloor
 =\left\lfloor\frac{2r+1}{b}\right\rfloor\in\{0,1\}.
 \tag{I8}
\]

因此Legendre估值公式给

\[
 v_p(\mu_{2l})=(l+1)v_p(2)
 -\sum_{e\ge1}\left(
 \left\lfloor\frac{2l+1}{p^e}\right\rfloor
 -2\left\lfloor\frac l{p^e}\right\rfloor\right)
 \ge-\lfloor\log_p(2l+1)\rfloor.
 \tag{I9}
\]

这对p=2同样成立；未遗漏2的高次幂。故在i≤H的整个prefix上

\[
 d_{H+1}\mu_i\in\mathbb Z,\qquad
 d_{H+1}U_i\in\mathbb Z.
 \tag{I10}
\]

它利用inverse-central-binomial的floor结构，没有把(l!)²或(2l+1)!各自当不可约分母，也没有使用H!。

## 3. 两边界的任意transition及其全部估值

完全展开(I4)/(I5)，每个forcing从同奇偶的k传播到d，出现

\[
 P^-_{d,k}=\prod_{h=k+2,k+4,\ldots,d}\frac{h-1}{2h},
 \qquad
 P^+_{d,k}=\prod_{h=k+2,k+4,\ldots,d}\frac{2(h-2)}{h-1}.
 \tag{I11}
\]

空积为1；plus展开的forcing起点k≥2，故其transition不含零分子。minus的initial8使用k=1。对odd p及每一b=p^e，两个分子/分母进程都是同长度、公差2的连续进程。因为2可逆，每个进程中b倍数的个数为该长度除以b的floor或ceil，故计数之差至少−1。全部出现的整数至多H；b>H时贡献0。因此

\[
 v_p(P^\pm_{d,k})\ge-\lfloor\log_p H\rfloor\quad(p\text{ odd}).
 \tag{I12}
\]

不是只检查p的一阶，而是逐个p^e证明后求和。2处直接写四种进程：k=2s,d=2l时

\[
 P^-_{d,k}=\prod_{h=s+1}^l\frac{2h-1}{4h},\qquad
 P^+_{d,k}=\prod_{h=s+1}^l\frac{4(h-1)}{2h-1};
\]

k=2s+1,d=2l+1时

\[
 P^-_{d,k}=\prod_{h=s+1}^l\frac h{2h+1},\qquad
 P^+_{d,k}=\prod_{h=s+1}^l\frac{2h-1}h.
 \tag{I13}
\]

minus-even估值为−2(l−s)−v_2(l!/s!)≥−3l≥−2H；minus-odd、plus-even估值非负；plus-odd≥−v_2(l!)≥−l≥−H。因此统一安全支付为

\[
 \boxed{2^{2H}d_H P^\pm_{d,k}\in\mathbb Z}\quad(0\le k\le d\le H).
 \tag{I14}
\]

此处plus只对其实际非零transition使用；不需要假定一个零transition可取逆。

令D=d_{H+1}。由(I10)，minus forcing的分母由2D d_H清整；plus forcing由d_H²清整。再乘(I14)，并支付minus initial8，得到

\[
 2^{2H+1}D^3 A_d^\pm\in\mathbb Z\quad(d\le H).
 \tag{I15}
\]

(I6)/(I7)的每个finite-head term由D d_H清整，故同一q_H清整全部R_{ij}。每一forcing term都使用同一个LCD；求和不会再乘forcing个数的阶乘。

## 4. 两period coefficients与ordinary Z全头

非零Y系数对应i−j=2l≥0，此时

\[
 B_{ij}=16\binom{2l}{l}/8^l.
\]

非零ζ(2)系数对应j−i=2l+1，此时

\[
 C_{ij}=9\binom{2l}{l}/2^l.
 \tag{I16}
\]

前者的dyadic分母指数≤3floor(H/2)，后者≤floor((H−1)/2)，均由2^{2H+1}覆盖。若用π²作period基，系数C/6=3binom(2l,l)/2^{l+1}也由同q_H覆盖。

ordinary Z的完整partial fractions为

\[
 Z(i,j)=Z^0_{ij}+\delta_{ij}\zeta(2),\qquad
 Z^0_{ii}=-\sum_{k=1}^i\frac1{k^2},
\]
\[
 Z^0_{ij}=\frac{H_i-H_j}{i-j}\quad(i\ne j),\qquad
 H_i=\sum_{k=1}^i\frac1k.
 \tag{I17}
\]

对0≤i,j≤H，d_H²同时清整diag和offdiag heads，period coefficient为0或1。因此(I1)严格给

\[
 \boxed{q_H R_{ij},\ q_H B_{ij},\ q_H C_{ij},\ q_H Z^0_{ij}\in\mathbb Z
 \quad(0\le i,j\le H).}
 \tag{I18}
\]

H=0时直接由starts核验。p>H+1不能产生任何未付分母。此为完整系数prefix，覆盖2和所有odd prime powers；并非primitive最小LCD或digit flags的优化结论。

### 自含的O(H)而非O(H log H)成本

ψ(m)=log d_m。对m≥1，d_{2m}/d_m整除binom(2m,m)：若一个prime增加LCM指数，其新prime power在(m,2m]内，对相应floor层binomial估值为1，其它层非负。于是ψ(2^t)≤(2^{t+1}−2)log2。取不小于m的最小2^t<2m，得ψ(m)≤4m log2。因此

\[
 \log q_H=(2H+1)\log2+3\psi(H+1)
 \le(14H+13)\log2=O(H).
 \tag{I19}
\]

这份初等bound足以支付quadratic增长的准入；不依赖prime扫描。若只作标准PNT换算，ψ(m)=m+o(m)给logq_H=(3+2log2)H+o(H)，但O(H)结论不依赖此换算。

## 5. 固定prototype、全raw pool与完整row heights

保留原行，不重选：n≥1、0≤r<n，

\[
 P_r=2^n x^{2r},\qquad
 D_r=\sum_{l=0}^{n-r-1}2^{n-l}\binom{2l}{l}x^{2r+1+2l}.
 \tag{I20}
\]

因为binom(2l,l)≤4^l，所有coefficients为整数，且

\[
 \|P_r\|_1=2^n,\qquad
 \|D_r\|_1\le(n-r)2^{2n-r-1}\le n2^{2n-1}.
 \tag{I21}
\]

xP_r/√(1−2x²)−D_r的阶至少2n+1，所以完整j=0,…,2n−1都接触消掉ζ(2)。取H=2n−1，(I18)覆盖P、D全部degrees与每个raw j；写

\[
 F_{rj}=N(P_r,j)-9Z(D_r,j)=\mathcal A_{rj}+\mathcal B_{rj}Y,
\]
\[
 q_{2n-1}\mathcal A_{rj},\quad q_{2n-1}\mathcal B_{rj}\in\mathbb Z
 \quad(0\le r<n,\ 0\le j<2n).
 \tag{I22}
\]

为完整计coeff heights，用0≤μ_i≤2、|U_i|≤8i。minus forcing在(I4)中绝对值≤12，且homogeneous multiplier<1/2，故|A_d^-|≤24。plus multiplier<2、forcing≤16、每次degree增加2，故

\[
 |A_d^+|\le16(2^{\lfloor d/2\rfloor}-1).
\]

finite heads逐项≤8/k，其总和≤8H。于是

\[
 |R_{ij}|\le24+16\cdot2^{\lfloor H/2\rfloor}+8H,
 \quad |B_{ij}|\le16,
 \quad |Z^0_{ij}|\le2.
 \tag{I23}
\]

最后一项由(I17)给：diag的平方调和和≤2，offdiag是连续若干倒数的平均≤1。代H=2n−1及(I21)，所有raw entries的两系数同时满足

\[
 \boxed{|\mathcal A_{rj}|+|\mathcal B_{rj}|
 \le S_n:=32(n+1)4^n.}
 \tag{I24}
\]

具体未舍项的bound为(16n+32)2^n+(8+9n)4^n≤(17n+24)4^n≤S_n。行的所有低degree forcing、ordinary Z companion以及2^n prototype高度均已计价。

### native a^i尺度的准确位置

实际第一summand为2^na^{2r}\bar M(2r,j)=2^{n-r}\bar M(2r,j)，所以同一行有exact identity

\[
 F_{rj}=2^{n-r}\left[
 \bar M(2r,j)-9\sum_{l=0}^{n-r-1}
 2^{r-l}\binom{2l}{l}Z(2r+1+2l,j)\right].
 \tag{I25}
\]

selected determinant的该显式row-scale乘积是2^{n(n+1)/2}。括号中的companion系数可为dyadic有理数；其绝对和≤(n−r)2^{n-1}，但绝不能在未清整它们时免费去掉外row scale。native a^i已通过(I3)、(I13)、(I16)、(I21)/(I25)计入算术及系数高度。对actual new-sheet contour上t^{2r}的几何范数仍须由共同contour分工另证；本稿不把上述coefficient height当成两sheet实能量。

## 6. 整数filter、selected-even determinant与已知content

任取整数column filter E∈Mat_{2n×m}(Z)，全输入列仍是(I22)范围，定义W_s=max(1,Σ_{j<2n}|E_{js}|)。filtered entries仍由同q清整，且其两系数l1≤W_s S_n。取任何n个filtered columns、形成n阶formal-Y determinant Δ_{n,E}(T)，Leibniz及多项式l1范数给

\[
 q^n\Delta_{n,E}(T)\in\mathbb Z[T],\qquad
 \|\Delta_{n,E}\|_1\le n!S_n^n\prod_sW_s,
 \quad q=q_{2n-1}.
 \tag{I26}
\]

故column filter的全部费用为Σ_s logW_s；没有给未知大filter免费高度。selected-even是E_{j,s}=[j=2s]，所有W_s=1。

在固定行(I20)中，每一P_r、D_r系数显然被h_r=2^{r+1}整除。因此不是另换prototype，而是同一对象的已付整数content identity：

\[
 \kappa_n=\prod_{r<n}h_r=2^{n(n+1)/2},\qquad
 \boxed{\frac{q^n}{\kappa_n}\Delta_{n,E}(T)\in\mathbb Z[T].}
 \tag{I27}
\]

证明是P_r/h_r、D_r/h_r仍为整数polynomials，(I18)逐row适用，filter仍整数。这里没有宣称h_r为最大primitive content；不能把(I25)括号的dyadic rational coefficients当成(I27)的证明。两identity出现相同乘积κ_n，但逐row因子不同。

对selected-even columns记Δ_n(T)。其目标coeff矩阵为

\[
 \mathcal B_{r,2s}=16\cdot2^n\cdot2^{-(r-s)}c_{r-s} (r\ge s),
 \qquad \mathcal B_{r,2s}=0 (r<s).
\]

故[T^n]Δ_n=(16·2^n)^n≠0，对ALL n≥1。它是degree-n polynomial非零，不能推出Δ_n(Y)实际非零。

完整已知清整与coefficient-height账为

\[
 \log\frac{q^n}{\kappa_n}
 =n\big[(4n-1)\log2+3\psi(2n)\big]
 -\frac{n(n+1)}2\log2,
 \tag{I28}
\]
\[
 \log\left\|\frac{q^n}{\kappa_n}\Delta_{n,E}\right\|_1
 \le n\log q-\log\kappa_n+n\log S_n
 +\log(n!)+\sum_s\log W_s.
 \tag{I29}
\]

全prefix elementary bound给右侧O(n²)+ΣlogW_s，区别于泛用factorial清整导致的O(n² logn)。log(n!)=O(n logn)只是det展开的实高度，不是清整账。若作标准PNT换算，(I28)leading为(6+(7/2)log2)n²；(I29)leading为(6+(11/2)log2)n²，余项o(n²)+O(n logn)+ΣlogW_s。这些是选定安全证书的upper，不能称实际primitive最优cost或actual-energy lower。

若Y=u/v∈Q、v≥1，则同一完整filtered值满足

\[
 \frac{v^nq^n}{\kappa_n}\Delta_{n,E}(Y)\in\mathbb Z.
 \tag{I30}
\]

**仅在另已证明该值非零时**才能得|Δ_{n,E}(Y)|≥κ_n/(v^nq^n)。本稿不从目标leading coefficient、正核、known rowcontent或上述integrality领取非零；也不从一个upper的大小宣判全部χ−8方法不可能。

## 7. 本轮首关结算

本稿支付同一native源的完整rational coefficient prefix、所有prime powers、含ordinary Z的全raw pool、固定row高度与a^i尺度、整数filter高度及selected-even determinant的完整安全quadratic清整费。无须finite-n头程序、CAS或prime扫描。它满足256算术首关要求的logq_H=O(H)，不是净strict已付。

整体是否通过唯一首关仍需共同actual生成芽/合法contour逐项匹配。本稿没有新数值定理；关系点det的真实无界非零、优化finite successor/digit flags与同一个两sheet对象的统一实能量均未证明。旧Catalan48N矩阵、固定seed、prime表或strict能量数字均未继承；本轮不重开已停止的RV、Fricke或截区窗口。

执行范围：新数学程序、finite-n/CAS/prime/参数/map/word扫描、Lean、外Git写、旧archive producer全部0。工具仅做文档FULL读取、已有manifest pin验证、新稿保存及最终FULL复读/hash。
