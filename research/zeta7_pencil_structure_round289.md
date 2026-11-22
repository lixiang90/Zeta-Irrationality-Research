# 第289轮独审 · 权七矩阵铅笔的平方根秩亏界

写 \(P_h(T)=\det(A_h+TB_h)\)，两矩阵的 \(i,j\) 条目分别为 \(A_{k,k}/k\) 和 \(30(-1)^k\binom{2k}k/k\)，\(k=i+j+1\)，\(0\le i,j<h\)。对每个外带素数 \(p>\max(13,4h-2)\)，有
\[
 \operatorname{corank}_{\mathbb F_p(T)}(A_h+TB_h)
 \ \le\ \operatorname{corank}_{\mathbb F_p} B_h
 \ \le\ \lfloor\sqrt{h/2}\rfloor .                              \tag{Q1}
\]
首个不等式对任一非零的最高次子式成立。下面证明第二个不等式，给出整个模 \(p^8\) 条件的小矩阵判别，再对 \(1\le h\le240\) 证明全部外带素数都保留八层。[本轮实际对象](zeta7_polynomial_content_charter_round289.md) · [上轮的块递降 M11](zeta7_shifted_mellin_round288.md)

## 用两种首一 Chebyshev 基表示领系数矩阵

先剥去 \(30\) 和行列符号，写 \(C_{ij}=\binom{2k}{k}/k\)。它是 \([0,4]\) 上 \(\tau([x,4])\,dx\) 的矩矩阵，其中 \(d\tau(x)=dx/[\pi\sqrt{x(4-x)}]\)。置 \(x=2+2\cos\theta\) 时尾概率为 \(\theta/\pi\)。分别取
\[
 f_j(x)=\frac{\cos((j+1/2)\theta)}{\cos(\theta/2)},\qquad
 g_i(x)=\frac{\sin((i+1/2)\theta)}{\sin(\theta/2)} .
\]
两者的首项为 1，第一阶为 \(x-3,x-1\)，此处“首项”指零阶多项式。其余阶由同一递推 \(u_{j+1}=(x-2)u_j-u_{j-1}\) 给出，故各为首一整系数基。积分中 \(\sin\theta=2\sin(\theta/2)\cos(\theta/2)\)。利用 \(\int_0^\pi \theta\sin(v\theta)\,d\theta=-(-1)^v\pi/v\)（\(v\ne0\) 的整数）得到
\[
 \int_0^4 g_i(x)f_j(x)\tau([x,4])\,dx
   =2(-1)^{i+j}\left(\frac1{i+j+1}-\frac1{i-j}\right),         \tag{Q2}
\]
其中 \(1/0\) 按零处理，来自 \(\sin0=0\)。行列两组基变换均在整数上可逆。[第三、四类 Chebyshev 的三角表示](https://dlmf.nist.gov/18.5)

在 \(\mathbb F_p\) 上取 \(N=2h\) 个节点 \(I=\{\pm(i+1/2):0\le i<h\}\)。设 \(D_{uv}=(u-v)^{-1}\ (u\ne v),\ D_{uu}=0\)。由于 \(N<p\)，节点互异。\(D\) 为反对称矩阵，且节点反射反交换 \(D\)。在反射的偶、奇坐标下只有两个非对角块，互为负转置。偶坐标映入奇坐标的块为
\[
 K_{ij}=\frac1{i-j}+\frac1{i+j+1},
\]
第一项沿对角线仍取零。Q2 等价于 \(2K^{\mathsf T}\) 的行列符号变换，所以
\[
   \dim\ker D=2\dim\ker B_h.                                   \tag{Q3}
\]

## 全有限域的微分矩阵证明

用全体 \(v\in\mathbb F_p\) 的 Lagrange 基 \(1-(x-v)^{p-1}\) 表示次数 \(<p\) 的多项式。其导数在 \(u\ne v\) 处为 \(1/(u-v)\)，在 \(u=v\) 处为零。因此 \(\ker D\) 对应的空间正是
\[
 \mathcal V=\{f\in\mathbb F_p[x]:\deg f<p,\ f|_{\mathbb F_p\setminus I}=0,\quad f'|_I=0\}.
\]
若 \(R=\dim \mathcal V>0\)，取其 Wronskian \(W\)。选次数互异的基，最高项系数除各首项外为次数的 Vandermonde 行列式。次数互异且均在 \([0,p-1]\)，故 \(W\ne0\)。各基向量次数总和不超过最大的 \(R\) 个可用次数之和，导数再减去 \(R(R-1)/2\)，得到 \(\deg W\le R(p-R)\)。

在 \(u\notin I\)，选定消失阶依次递增的基，最小可能序列为 \(1,2,\ldots,R\)，故 \(\operatorname{ord}_u W\ge R\)。在 \(u\in I\)，所有导数消失，阶 1 被排除，最小序列为 \(0,2,3,\ldots,R\)，从而 \(\operatorname{ord}_u W\ge R-1\)。在 \(p\) 点求和得
\[
        Rp-2h\le\deg W\le R(p-R),\qquad R^2\le2h.
\]
与 Q3 合并即得 Q1。

同一界还有一个独立的线性代数证明。取 \(X=\operatorname{diag}(u)_{u\in I}\)，有 \([X,D]+I_N=\mathbf1\mathbf1^{\mathsf T}\)。于是对任何与 \(D\) 交换的 \(Z\)，皆有 \(\operatorname{tr}Z=\mathbf1^{\mathsf T}Z\mathbf1\)。在 \(D\) 的广义零特征空间写 Jordan 模块 \(M_i=\mathbb F_p[t]/(t^{s_i})\)，将其余主分量取为补空间。记 \(\mathbf1\) 在模块中的投影为 \(y_i\)，行泛函的限制为 \(w_i\)。对投影取迹得 \(w_i(y_i)=s_i\ne0\)，因为 \(s_i\le2h<p\)。设 \(y_i\) 的 \(t\) 阶为 \(a_i\)。若 \(i\ne j\)，任意模块同态 \(M_i\to M_j\) 延拓为异块矩阵后迹为零，故 \(w_j\) 消灭整个理想 \(t^{a_i+\max(s_j-s_i,0)}M_j\)。由于 \(w_j(y_j)\ne0\)，该指数必须大于 \(a_j\)。当 \(s_i\le s_j\) 时，两个方向给 \(1\le a_j-a_i\le s_j-s_i-1\)。块长依次至少为 \(1,3,\ldots,2R-1\)，总和至少为 \(R^2\)。复数域的同特征值块长间距性质已由 Wilson 研究，此处的迹证明直接给出所需的有限特征版本。[Wilson, *Collisions of Calogero–Moser particles and an adelic Grassmannian*](https://doi.org/10.1007/s002220050237)

## 有限前缀的正常阶和零块

独立保留一个直接从生成函数得出的界，以说明正常阶与秩亏的关系。写 \(\gamma_k=\binom{2k}{k}/k,\ F(z)=\sum_{k\ge1}\gamma_kz^k\)。只在 \(k\le2h-1<p\) 取模。由 \(zF'(z)+1=(1-4z)^{-1/2}\) 得
\[
 z(1-4z)F''+(1-6z)F'=2.
\]
若 \(\deg P,\deg Q\le d<h,\ Q(0)=1\) 且 \(F-P/Q=O(z^J)\) 在有效前缀内，则 \(J\le3d+1\)。确实，把 \(P/Q\) 代入上式的残差乘 \(Q^3\)，分子次数至多 \(3d\)，零阶至少 \(J-1\)。若分子恒零，\(G=z(P/Q)'+1\) 满足 \((1-4z)G'=2G\)，且 \(G(0)=1\)。看 \(z=1/4\) 的首项可知 \(v_{1/4}G\equiv(p-1)/2\bmod p\)，与 \(|v_{1/4}G|\le2d<(p-1)/2\) 冲突。

定义 \(\mathcal L(t^j)=\gamma_{j+1}\)。若 \(h\) 奇异，设 \(d<h\) 为前一非奇异的 Hankel 阶，\(Q_d(t)\) 为由该阶非奇异性给出的首一正交多项式。写 \(\lambda_j=\mathcal L(t^jQ_d)\)，则 \(\lambda_0,\ldots,\lambda_{d-1}=0\)。设首个非零为 \(\lambda_{D-1}\)；可任意延拓有限矩序列使该指标存在。对 \(d<k\le D\)，在 \(1,\ldots,t^{d-1},Q_d,\ldots,t^{k-d-1}Q_d\) 的基下，左上块非奇异，两侧交叉块为零，右下块的 \(i,j\) 元为 \(\lambda_{d+i+j}\) 加上低编号项。在 \(i+j<D-d-1\) 时为零，等号时是同一非零数。故下个正常阶为 \(D\)，而 \(h\) 的秩亏恰为 \(r=\min(h-d,D-h)\)。此结论对任何域的同一 Hankel 铅笔都适用。[正式幂级数正常指标与 Hankel 行列式](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8922.pdf)

用 \(z^dQ_d(1/z)\) 作分母，\(z^k\ (k\ge d+1)\) 的乘积系数是 \(\lambda_{k-d-1}\)。于是 \(F\) 与某个分子分母次数均至多 \(d\) 的分式有至少 \(d+h+r\) 阶接触。证据只用到 \(d+h+r\le2h\) 的精度，与延拓无关。上面的微分界给 \(h+r\le2d+1\)，再用 \(d\le h-r\)，得 \(3r\le h+1\)。Q1 更给出每个允许的完整零块长度至多 \(2\sqrt{h/2}+O(1)\)，这里 \(h\) 取块的中点。实际铅笔域 \(\mathbb F_p(T)\) 上在中点取秩亏也满足 Q1。

## 模八层的低维精确判别

记 \(r=\operatorname{corank}_{\mathbb F_p}B_h\)。在 \(B_h\) 中取一个阶 \(h-r\) 的单位主子式 \(B_0\)。对称矩阵满秩部分总有这样的主子式，例如先写成 \(VJV^{\mathsf T}\)，其中 \(V\) 列满秩、\(J\) 非奇异，再在 \(V\) 中取满秩的方形行子阵。用该主子阵作对称消元，使
\[
 B_h\sim\begin{pmatrix}B_0&0\\0&D_0\end{pmatrix},\qquad
 A_h\sim\begin{pmatrix}A_0&C\\ C^{\mathsf T}&A_1\end{pmatrix},\qquad D_0\equiv0\bmod p .
\]
两处都作同一 \(\mathbb Z_{(p)}\) 可逆合同变换。用反向变量 \(S\) 将多项式写成 \(\det(B_h+SA_h)\)。因 \(\det(B_0+SA_0)\) 在形式幂级数环中是单位，完全消去这个块后得到等价条件
\[
 P_h\equiv0\bmod p^8\quad\Longleftrightarrow\quad
 \det\!\left(D_0+S A_1-S^2 C^{\mathsf T}(B_0+S A_0)^{-1}C\right)
 \equiv0\bmod(p^8,S^{h+1}).                                    \tag{Q4}
\]
左侧为所有系数消零。只需截断至 \(h\) 次，因为原多项式次数为 \(h\)。Q4 的行列式阶数 \(r\le\sqrt{h/2}\)。特别若 \(r=1\)，右边等价于 \(D_0,A_1\) 和 \(C^{\mathsf T}(B_0^{-1}A_0)^jB_0^{-1}C\ (0\le j\le h-2)\) 在模 \(p^8\) 下全为零。这个判别使用了真实有理项。

## 两个系数排除无上界的所有外带素数

置 \(b_h=[T^h]P_h,\ c_h=[T^{h-1}]P_h\)，均指既约有理数。对每个 \(1\le h\le240\)，精确结果为
\[
 \text{将 }\gcd(|\operatorname{num}b_h|,|\operatorname{num}c_h|)
 \text{ 中所有不超过 }\max(13,4h-2)\text{ 的素因子剥去，结果为 }1. \tag{Q5}
\]
因此这些 \(h\) 没有任何外带素数能令 \(P_h\) 模 \(p\) 消零。这里的素数没有数值搜索上限。对 \(h=2\)，无符号的中心二项式矩行列式为 \(13/3\)，说明只取领系数本身可能遇到零因子。

核验 Q5 时，把 \(B_h\) 定义的泛函记为 \(\mathcal B\)，另一项为 \(\mathcal A\)。在实数处，\(B_h\) 经对角符号变换及乘以负常数后正定，故其首一正交多项式 \(q_j\) 逐阶存在，范数 \(n_j=\mathcal B(q_j^2)\ne0\)。行列式导数给
\[
 b_h=\prod_{j=0}^{h-1}n_j,\qquad
 c_h/b_h=\operatorname{tr}(B_h^{-1}A_h)
        =\sum_{j=0}^{h-1}\mathcal A(q_j^2)/n_j .
\]
下面的 Python 程序使用仓库的有理项求和和 python-flint 的整系数、分式多项式。最终 \(b_h\) 的分子位长在这段内的最大值为 114419。全程保留既约分数。

~~~python
from math import comb, lcm
from sys import path
from flint import fmpq as Q, fmpz as Z, fmpq_poly as Poly

path.insert(0, "research")
from verify_zeta7_contact_round288 import rational_part

H = 240
A = [rational_part(k, k) / k for k in range(1, 2*H + 1)]
B = [Q(30*(-1)**k*comb(2*k, k), k) for k in range(1, 2*H + 1)]
da = lcm(*(x.denominator for x in A))
db = lcm(*(int(x.denominator) for x in B))
aa = [Z(a.numerator)*(da//a.denominator) for a in A]
bb = [Z(b.numerator)*(db//int(b.denominator)) for b in B]
q, prev, x = Poly([1]), Poly(), Poly([0, 1])
leading, trace, previous_norm = Q(1), Q(0), Q(1)
for h in range(1, H+1):
    sq = q*q
    co = sq.numer().coeffs()
    def pairing(v, den):
        return Q(sum(a*b for a,b in zip(v, co)), den*sq.denom())
    norm, xnorm, other = pairing(bb, db), pairing(bb[1:], db), pairing(aa, da)
    leading *= norm
    trace += other/norm
    second = leading*trace
    common = abs(leading.numerator.gcd(second.numerator))
    for k in range(2, max(13, 4*h-2)+1):
        while common > 1 and common % k == 0:
            common //= k
    assert common == 1, h
    q, prev = (x-xnorm/norm)*q-(norm/previous_norm)*prev, q
    previous_norm = norm
~~~

Q1 与 Q4 对无界 \(h\) 成立。秩亏小仍允许单个剩余方向具有很高的 \(p\) 进阶，Q5 只裁到指定的有限阶数。逐个素数的实际丢层总量仍要通过 Q4 或完整行列式的其他系数来控制。
