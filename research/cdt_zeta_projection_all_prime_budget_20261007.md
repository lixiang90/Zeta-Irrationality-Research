# 真实 ζ(s) 单周期投影的全素数 determinant 预算

2026-10-07。固定 r≥2、s=r+1，使用 H=rn 的原 Hermite 投影，构造真实 E_n^ζ=q_n^ζ+ζ(s)I_n。本稿给出包括小素数及全部高次幂的显式整模型，付款对象是完整 monic polynomial det(q_n^ζ+TI_n)，不假设任何较低 ζ 值有理。

最终安全费用常数为
\[
C_r^\zeta=2r+\left(r-\tfrac12\right)(\mathcal H_{r-1}-1)
-\frac1{2(r+1)},\qquad
\mathcal H_m=\sum_{j=1}^{m}\frac1j.
\]
特别地 ζ(5) 为649/60≈10.816667，ζ(7) 为15949/840≈18.986905。它们是可证明的费用上界，不是必要费用、最优费用或新的无理性结论。

直接输入在本轮均实际全文读取：[统一 ζ/β 构造](cdt_beta4_large_prime_tail_content_20261007.md)的六节/L1–L23，[原投影模型](cdt_beta_single_period_confluent_integral_model_20261007.md)的八节/B1–B29，以及[精确算术稿](cdt_beta4_projection_exact_arithmetic_20261007.md)的十二节/E1–E37。下文重证所有新 ζ 费用，不把 β(4) 的数值常数、非零种子或解析界迁移过来。

## 1. 同一真实 ζ 对象

令 J={0,…,n−1}、I={n,…,H−1}、H=rn。使用实际积分
\[
C_r^\zeta(u,v)=\int_0^1\!\int_0^1
\frac{x^u y^v}{1-xy}\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
=\sum_{j\ge0}\frac1{(j+u+1)(j+v+1)^r}.
\tag{Z1}
\]
正项级数绝对收敛。置
\[
D(z)=\prod_{u=0}^{H-1}(z-u),\quad
B_k(z)=\prod_{\substack{v\in J\\v\ne k}}(z-v),\quad
Q_I(z)=\prod_{u\in I}(z-u),\quad
P_{ku}=\frac{B_k(u)^r}{D'(u)}
\left[\frac{Q_I(z)}{B_k(z)^{r-1}}\right]_{k,<r}(u).
\tag{Z2}
\]
原完整 regular-part 身份是 P_{kv}=δ_{kv}（v∈J）和
Σ_{u≠v}P_{ku}/(u−v)^a=0（1≤a≤r−1）。令
A_{u,a}=Σ_{j=1}^u j^{-a}，A_{0,a}=0，则实际矩阵为
\[
E_n^\zeta=PC_r^\zeta=q^\zeta+\zeta(s)I_n,\qquad
q^\zeta_{kv}=(-1)^{r-1}
\sum_{u\ne v}\frac{P_{ku}(A_{u,1}-A_{v,1})}{(u-v)^r}
-\delta_{kv}A_{v,s}.
\tag{Z3}
\]
证明部分分式的一阶项先合成收敛差 A_{u,1}−A_{v,1}；不把 ζ(1) 当作数值。较低 ζ(a) 和高阶有限尾的系数，再由全部 regular-part 条件同时消去。Z3 的和包括所有低、高原行，不是删去若干周期后的近似。记
\[
\mathcal D_{r,n}^\zeta(T)=\det(q^\zeta+TI_n)\in\mathbb Q[T].
\tag{Z4}
\]
它为 monic n 次；这不证明在真实 ζ(s) 处非零。

## 2. 小素数与全部高次幂的完整 fallback

记 D_M=lcm(1,…,M)，D_0=1，L_M(p)=max{e≥0:p^e≤M}。原 factorial 基数对全部 r 精确为
\[
\left|\frac{B_k(u)^rQ_I(k)}{D'(u)B_k(k)^{r-1}}\right|
=\binom uk^{r-1}\binom{H-1-k}{u-k}
\binom{u-k-1}{u-n}^{r}\in\mathbb Z\quad(u\in I).
\tag{Z5}
\]
正规化 Taylor 的 ℓ 次系数是若干非零节点差倒数的总次数 ℓ 乘积，展开中的 binomial 系数为整数；所以
\[
D_{H-1}^{\,r-1}P_{ku}\in\mathbb Z
\quad(0\le k<n,\ 0\le u<H).
\tag{Z6}
\]
这同时支付所有 p-power 以及 Taylor 中写成导数/ℓ! 时可能出现的因子，不能另推一个未付的 factorial。

从 Z3，投影、差的 r 次幂与一阶 harmonic 尾总共最多损失
(r−1+r+1)L_{H-1}=2rL_{H-1}。对角 A_{v,s} 至多损失
sL_{n-1}≤2rL_{H-1}。两种项取最大而非费用相加，故全部素数有
\[
v_p(q^\zeta_{kv})\ge-2rL_{H-1}(p),\qquad
p^{\,2rnL_{H-1}(p)}\mathcal D_{r,n}^\zeta(T)\in\mathbb Z_p[T].
\tag{Z7}
\]
ζ 的比例系数只有±1，没有 β 内核的4^{-r}或奇分母例外。p>H−1 时所有 q entries 已为 p 整；该范围的 harmonic 尾和节点差都不存在 p 分母。不存在 β 情形延伸到4H的尾区间。

## 3. p≤n 的一次共轭付款

以下首层统一取 p²>H=rn。与原统一稿的 p²>4rn 相比，这里使用 ζ 尾最大 H−1 的真实范围，不涉及 β 尾。若同时 p≤n，该范围自动排除 p=2。

对 residue a∈{0,…,p−1}，置 d_a=#J(a)、e_a=#I(a)、t_a=d_a+e_a，
\[
h_a=(r-1)d_a-e_a=r d_a-t_a,\qquad
S_p=\operatorname{diag}(p^{h_{k\bmod p}})_{k\in J}.
\tag{Z8}
\]
写 Φ_k(k+w)=Σα_{k,ℓ}w^ℓ，Φ_k=Q_I/B_k^{r-1}，c=k mod p。各分子线性因子和逆幂因子逐次数展开，给
\[
v_p(\alpha_{k,\ell})\ge e_c-(r-1)(d_c-1)-\ell.
\tag{Z9}
\]
对 u∈I、u≡k，u−k 的各次幂补回相应次数，且 B_k(u)^r 与 D'(u) 的一层计数分别是 r(d_c−1)与t_c−1；故 P 整。对 u属异类 a，Taylor 最高允许次数 r−1 给出
\[
v_p(P_{ku})\ge0\ (u\equiv k),\qquad
v_p(P_{ku})\ge h_a-h_c+1\ (u\not\equiv k).
\tag{Z10}
\]
写 n=Ap+b、rb=cp+b_r、0≤b,b_r<p，则
h_a=r·1_{a<b}−c−1_{a<b_r}，振幅至多 r（根据 b_r≥b 或 b_r≤b 分组即得）。

现在对 Z3 的各项计入 S 的左右因子。u≡v 时，差的 r 次幂损失 r、harmonic 损失1：u≡k 时权重相同且 P 整，最多 r+1；u≢k 时 Z10 抵消一层，最多 r。u≢v 且 u≢k 时，合计下界 h_u−h_v≥−r；u≡k（含唯一非零低行 u=k）时至少 h_k−h_v−1≥−(r+1)。对角尾最多 r+1。因此
\[
\boxed{\quad
p^{r+1}S_pq^\zeta S_p^{-1}\in M_n(\mathbb Z_p),\qquad
p^{(r+1)n}\mathcal D_{r,n}^\zeta(T)\in\mathbb Z_p[T].
\quad}
\tag{Z11}
\]
这是真实共轭格；S_p 本身不一定为 Z_p-unimodular。但 det 的左右 S 因子恰相消，所以 Z11 已支付全部系数，没有另加清 S 或清 P 的费用。

## 4. ζ 的局部压缩及接近 n 的零行内容

记 M_p=p^{r+1}S_pq^\zeta S_p^{-1} mod p。与 Z11 的逐项计数一样，异 residue-class 的项只有在 h_v−h_k=r 时可能非零；其它至少多一层 p。按 h 非降序排列，M_p 因而 block 上三角。

对 residue a，把类内节点写成 a+jp，低节点 j=0,…,d_a−1，全部节点 j=0,…,t_a−1。定义压缩投影
\[
\Pi_{jl}^{(d,t)}
=\frac{\left(\prod_{i<d,i\ne j}(l-i)\right)^r}
{\left(\prod_{i<t}(z-i)\right)'_{z=l}}
\left[\frac{\prod_{i=d}^{t-1}(z-i)}
{\left(\prod_{i<d,i\ne j}(z-i)\right)^{r-1}}\right]_{j,<r}(l)
\quad(l\ge d),\qquad
\Pi_{ji}^{(d,t)}=\delta_{ji}\ (i<d).
\tag{Z12}
\]
t 不必是 rd；不据此声称压缩分子的 degree 条件与原对象相同。matching residue 的 P mod p 恰为 Π：代入 z=a+pz' 后，类内 Φ 提供 p^{e_a−(r−1)(d_a−1)}，B^r/D' 提供相反的幂；类外单位 series 模 p 只有常数项，且 B^r·Q/B^{r−1} 的类外因子与 D' 相消。所有类内 ordinal 差小于 p，故压缩分母为单位。

令 \(\mathcal H_j^{(b)}=\sum_{l=1}^j l^{-b}\)，空和零。真实 A_{a+jp,b} 中一层 p 的倍数正好是 p,2p,…,jp，所以 p^bA_{a+jp,b} mod p=\(\mathcal H_j^{(b)}\)。没有 β 的季度相位。对角 graded 块精确为
\[
(M_p)_a(j,i)=(-1)^{r-1}
\sum_{\substack{0\le l<t_a\\l\ne i}}
\frac{\Pi_{jl}^{(d_a,t_a)}
(\mathcal H_l^{(1)}-\mathcal H_i^{(1)})}{(l-i)^r}
-\delta_{ji}\mathcal H_i^{(s)}
\pmod p.
\tag{Z13}
\]
异类 terms 在同类块中的估值至少−r，乘 p^{r+1} 消失；因此该式包括全部原项。det M 是各对角块 det 的乘积，但 rank 不能直接相加。

若同时 rn/(r+1)<p≤n，写 b=n−p<p/r。此时
d_a=1+1_{a<b}、t_a=r+1_{a<rb}、h_a=r·1_{a<b}−1_{a<rb}。
每个 a≥rb 都有 d=1,t=r,h=0；其压缩 Φ 为完整 r−1 次 Q，Taylor 截断无损，所以 Π=(1,0,…,0)，且 \(\mathcal H_0^{(s)}=0\)。Z13 的对角块为零。所有 h 只可能是 r−1、−1或0，权重0不能与其它类形成差 r，故对应的整个行、列均为零。这样的低节点有
\[
z_{r,n,p}=p-r(n-p)=(r+1)p-rn>0.
\tag{Z14}
\]
在完整整多项式矩阵 p^{r+1}(SqS^{-1}+TI) 中，这 z 个行的每个系数均被 p 整除，故
\[
\boxed{\quad p^{(r+1)n-z_{r,n,p}}\mathcal D_{r,n}^\zeta(T)
\in\mathbb Z_p[T].\quad}
\tag{Z15}
\]
窗口外置 z=0。这里是整零行内容，不是对角块 rank 的猜测。

## 5. p>n：匹配保护与最后一个窗口

仍取 p²>H，现在 p>n。全部 k−v 的非零差是 p 单位，因此未正规化 Φ_k(k+w) 的系数都为 p 整。令
\[
\eta_{p,v}=\left\lfloor\frac{H-1-v}{p}\right\rfloor,\qquad
\eta_p^{\rm out}=\left\lfloor\frac{H-1-n}{p}\right\rfloor.
\tag{Z16}
\]
在 matching 高节点 u≡v mod p，若 v≠k，B_k(u)^r 直接有 p^r；若 v=k，原 Φ(u)=0，且 Taylor 截断的余项从 r 次开始，u−k∈pZ_p，给同一个 p^r 因子。D'(u) 恰有 η_{p,v} 层，所以
\[
v_p(P_{ku})\ge r-\eta_{p,v}\quad(u\in I,\ u\equiv v,\ v<n).
\tag{Z17}
\]
其它 residue a≥n 的 D'(u) 估值至多 η_p^{out}，而 numerator 为整；故 P 至少−η_p^{out}。低节点仍为 δ。u−v为单位时再付 harmonic 一层；matching 高节点在差的 r 次幂和 harmonic 后最多损失 η_{p,v}+1。由于 v<n 导致 η_{p,v}≥η_p^{out}，对 n<p<(r−1)n 的第 v 列可安全付 η_{p,v}+1。目标 A_{v,s} 全为 p 整。这个预算覆盖每个系数和全部原行。

在 (r−1)n≤p≤H−1 的末窗口，可再合法改进。令 R=H−p≤n。每个高节点 u≥p 都是 p+v（0≤v<R），属于一个低 residue；由 Z17 其 P 至少有 r−1 层 p。对 u≠v mod p 的项，harmonic 只损失1，所以至少 r−2≥0。u<p 时没有 harmonic 分母；非 matching 的所有节点及 P 在这里亦整，因为 η_p^{out}=0。因而只有 v<R 的列可能非整，且仅 matching u=p+v 的项最多两层：
\[
p^2q^\zeta_{\bullet v}\in\mathbb Z_p^n\ (v<R),\qquad
q^\zeta_{\bullet v}\in\mathbb Z_p^n\ (v\ge R),\qquad
p^{2R}\mathcal D_{r,n}^\zeta(T)\in\mathbb Z_p[T].
\tag{Z18}
\]
其 leading 残数为
\(p^2q^\zeta_{kv}\equiv(-1)^{r-1}P_{k,p+v}/p^{r-1}\) mod p（v<R），因为 p(A_{p+v,1}−A_{v,1})≡1；其它列零。rank至多R，但不预设满秩。若对应 R×R 首行块是单位，则唯一最高分母的 R 阶主子式使 [T^{n-R}]D 的估值恰为−2R；这种附加单位条件需单独验证。

## 6. 全部 n、全部 prime-power 的一个显式模型

对所有 n≥1，定义有限非负整数指数
\[
b_{r,n}(p)=
\begin{cases}
2rnL_{H-1}(p),&p\le\sqrt H,\\
(r+1)n-z_{r,n,p},&\sqrt H<p\le n,\\
\sum_{v=0}^{n-1}(\eta_{p,v}+1),&
p>\max(n,\sqrt H),\quad p<(r-1)n,\\
2(H-p),&
p>\max(n,\sqrt H),\quad (r-1)n\le p\le H-1,\\
0,&p>H-1,
\end{cases}
\qquad
G_{r,n}^\zeta=\prod_p p^{b_{r,n}(p)}.
\tag{Z19}
\]
在第二行，仅窗口 Z14 内取 z，外面取0。各区间按上述顺序覆盖全部素数；当 r=2 时第三段为空，第四段从 p>n 开始。小 n 仍按 p≤sqrt H 的 fallback 付款，没有假设 n大于r。若 p>H−1 则 L_{H−1}=0；交叠的零边界只给同一个零费用。由 Z7、Z15、Z17、Z18，严格有
\[
\boxed{\quad G_{r,n}^\zeta\mathcal D_{r,n}^\zeta(T)\in\mathbb Z[T].\quad}
\tag{Z20}
\]
小素数含全部高 powers；第一段中 b log p≤2rn log(H−1)，粗素数个数O_r(sqrt n)给总贡献O_r(n^{3/2}log(n+2))=o(n²)。p=2不需额外固定因子。这是一次完整 determinant 付款，不再另加投影、Schur或共轭的分母。

## 7. 一般 leading 常数及 ζ(5)、ζ(7) 接口

固定 r。p≤n 的首层先付(r+1)n²，Z14 的零行内容按 PNT/partial summation节省
\[
n^2\int_{r/(r+1)}^1((r+1)x-r)\,dx+o(n^2)
=\frac{n^2}{2(r+1)}+o(n^2).
\tag{Z21}
\]
对 n<p<(r−1)n，令x=p/n、y=v/n，费用密度为
\(1+\int_0^1\lfloor(r-y)/x\rfloor\,dy\)，误差O_r(1)每prime。除有限边界外，写 floor 为Σ_{m=1}^{r-1}1_{mx≤r−y}后，逐个积分：
m=1贡献r−2；m≥2的满高矩形贡献(r−1)/m−1、宽1/m的三角形贡献1/(2m)。因此
\[
\int_1^{r-1}\int_0^1\left\lfloor\frac{r-y}{x}\right\rfloor dy\,dx
=\left(r-\tfrac12\right)(\mathcal H_{r-1}-1).
\tag{Z22}
\]
r=2 时此积分为0。中间段的baseline贡献r−2，末段 Z18 贡献
∫_{r−1}^r2(r−x)dx=1。相加得到
\[
\boxed{\quad
\log G_{r,n}^\zeta\le C_r^\zeta n^2+o_r(n^2),\qquad
C_r^\zeta=2r+\left(r-\tfrac12\right)(\mathcal H_{r-1}-1)
-\frac1{2(r+1)}.
\quad}
\tag{Z23}
\]
每个 floor/节点端点只影响O_r(1)列或少数边界素数，总误差O_r(n)；小 prime高powers的误差已由上一节支付。这不是从 prime 表拟合的常数。

| 目标 | r | 全素数安全费用 C_r^ζ |
|---|---:|---:|
| ζ(3) | 2 | 23/6 |
| ζ(5) | 4 | 649/60≈10.816666667 |
| ζ(7) | 6 | 15949/840≈18.986904762 |

全部 r 的 crude entry 预算 Z7 若全范围使用，给2r²的leading；Z23 把它降到O(r log r)。这是同一真实 ζ 投影的预算改进；没有声称与其它文献方法相比最优。

若反证假设 ζ(s)=A/B∈Q，B≥1，只有在 det E_n^ζ≠0 时才有
\[
B^nG_{r,n}^\zeta\det E_n^\zeta\in\mathbb Z,\qquad
\log|\det E_n^\zeta|\ge-C_r^\zeta n^2-o_r(n^2)-n\log B.
\tag{Z24}
\]
无限非零性与同一 ζ 模型的实处上界均需另证；β(4) 的23幂种子、sec轮廓及2.137834常数没有自动迁移。

## 8. 固定窗口的全精确证据与审核状态

本轮执行两段新的 inline Python/Fraction，输入只含四个固定矩阵，没有旧 prime table 扩展、数学 producer 文件、旧 scripts、guard或Lean执行，也没有新PDF下载或页阅读。

第一段在 n=2 的末窗口分别取(r,p)=(4,7)、(6,11)，从原整数binomial基数和全部Taylor系数直接构造 P、q。得到
\[
q_{4,2}^\zeta=
\begin{pmatrix}
-1693289/264600&-11239/10800\\
-2709851/264600&-14963/5400
\end{pmatrix},\qquad
q_{6,2}^\zeta=
\begin{pmatrix}
-74127583290329/276623424000&-54533917747/1524096000\\
-67422781896527/184415616000&-111743442799/2286144000
\end{pmatrix}.
\tag{Z25}
\]
两者 R=1、逐列估值分别是(−2,0)，末窗口 leading 第一列分别为(6,1) mod7、(10,1) mod11；全部 monic polynomial 系数按升幂估值均为(−2,−2,0)。所以这里2R费用确实达到，不能无条件改成一层R。此有限反例不证明渐近最低费用。

第二段直接构造较大的两个固定首层矩阵：
r=4,n=23,p=19 的原 entries 最低估值−8，共轭后最低−5；M的全部零行恰为16,17,18，对应整列亦零，匹配 Z14 的z=3。
r=6,n=25,p=23 的原 entries 最低−12，共轭后最低−7；M的全部零行恰为12,…,22，对应整列亦零，匹配z=11。
这同时排除“原q的entries只有r+1层”的误读，证明共轭格确有必要；纸面Z23不以这些样本为证明。

root 已实际全文读取全部八节/Z1–Z25，独立重推 Z9–Z15 的 Taylor/共轭/graded 零行内容、Z17–Z18 的末窗口及 Z21–Z23 的一般 leading 常数，正式纸面数学审查 PASS，无数学修正请求。root 另以全新的 inline Fraction 独立复算 r=4,n=2,p=7 与 r=6,n=2,p=11 的完整 q，Z25 每个分数均一致；两个 monic polynomial 的三个系数升幂估值均为(−2,−2,0)，两个一般费用常数亦分别复核为649/60和15949/840。较大 n 的两个首层窗口样本未作第二次独立重算，仅为作者精确探索证据，不提升为额外定理。作者收审后更新本记录并完成最终实际全文回读。本文未作机器形式化验证；新结果是完整全素数预算及真实压缩/尾窗口接口，没有新数值无理性或线性无关性结论。

