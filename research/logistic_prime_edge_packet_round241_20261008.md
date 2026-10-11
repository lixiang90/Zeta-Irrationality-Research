# 第241轮：新 logistic 泛函的完整 prime-edge 包

2026-10-09，B。文件按既定轮次保留20261008后缀。固定源为第240轮的 \(X=3\zeta(3)+\zeta(5)\)、\(R_n=D_n^4/D_{5n}\) 和完整 \(3n\) 列池。本人没有运行数学程序、素数扫描或 Lean。已读的固定块 producer/output 是本轮另一代理的一次有界精确核验，不是变动素数的证据。

## 1. 完整泛函与命题

设 \(D_j(t)=\prod_{\ell=1}^j(t+\ell)\)，\(M=3n\)。第240轮完整身份给
\[
 U(f)=B\!\left(\tfrac32(tf)'+\tfrac1{24}(tf)'''\right),
 \qquad B(t^e)=B_e^+,\quad B_1^+=\tfrac12.
 \tag{P1}
\]
定义有理线性泛函 \(V_h^\circ\)，仅用于奇数 \(h=1,3\)：
\[
 V_h^\circ(t^e)=(e)_h B_{e-h}^+\ (e\ge h),\qquad
 V_h^\circ((t+j)^{-1})=(h+1)!H_j^{(h+2)}.
 \tag{P2}
\]
低于 \(h\) 的多项式取0；\(H_0^{(k)}=0\)。若
\[
 G(t)=t f(t)=P(t)+\sum_{j=1}^{5n}\frac{c_j}{t+j},
\]
则保留商部、全部残数和全部调和头的条目多项式是
\[
 {\cal F}_T(f)=\tfrac32V_1^\circ(G)+\tfrac1{24}V_3^\circ(G)-T\sum_jc_j.
 \tag{P3}
\]
在 \(T=X\) 它恰是 P1；因为 \(c_j=-j\lambda_j\)，参数系数亦为 \(\sum j\lambda_j\)。令
\[
 Q_n(T)=\det[{\cal F}_T(t^{i+k}R_n)]_{0\le i,k<M}.
 \tag{P4}
\]
令 \(\mathcal E\) 是2、3及三个非零整数
\[
 541936393813,\quad100344353231,\quad210779
 \tag{P5}
\]
的素因子集合。下文证明：对每个 \(p\ge7,\ p\notin\mathcal E,\ n=p-1\)，
\[
 v_p^{\rm Gauss}(Q_n)=5-9p,\qquad
 p^{9p-5}Q_n(T)\equiv c_p\pmod {p^5},\quad c_p\in\mathbb Z_p^\times.
 \tag{P6}
\]
这里 congruence 指所有非恒定系数被 \(p^5\) 整除；恒定系数就是某个单位 \(c_p\)。因此其任一 primitive 整数比例 \(P_{p-1}\) 模 \(p\) 是非零常数，非恒定系数亦被 \(p^5\) 整除。对任一固定 \(q\in\mathbb Q\)，除去分母坏素数后，所有这些 \(p\) 都有 \(P_{p-1}(q)\ne0\)。这支付无界尺度关系点非零；不支付全素数 primitive 费用、实处严格余额或新的数值无理性。

## 2. 实际 CRT 基与全部盘指数

固定 \(p\ge7,n=p-1\)。对 \(b=0,\ldots,p-1\) 取
\[
 m_b=\begin{cases}4&b=0,\\3&1\le b\le p-5,\\2&p-4\le b<p,\end{cases}
 \qquad
 \phi_{b,i}(t)=(t+b)^i\prod_{d\ne b}(t+d)^{m_d},\quad0\le i<m_b.
 \tag{P7}
\]
总数为 \(3p-3=M\)，所有次数小于 \(M\)。模 \(p\) 在每个不同中心 \(-b\) 取模 \((t+b)^{m_b}\)，同簇各项构成单位上三角的局部基，其它簇为0。因此它是完整次数 \(<M\) 空间的基，系数变换 determinant 为 \(p\)-单位；不是某个子矩阵。

对盘 \(t=pu-d\)，近极点集为
\[
 M_0=\{1,2,3,4\},\quad M_L=\{0,1,2,3,4\},\quad
 M_H=\{0,1,2,3\},\qquad \ell_d=|M_d|.
 \tag{P8}
\]
记 \(N_d(u)=\prod_{m\in M_d}(u+m)\)，远因子 \(F_d(u)\) 是剩余 \((j-d)+pu\) 的乘积，常数项是单位。对任意两个基指标 \(a=(b,i),c=(b',k)\)，
\[
 G_{ac}=t\phi_a\phi_cD_n^4,\qquad
 G_{ac}(pu-d)=p^{E_d}u^{E_d}K_d(u),
\]
\[
 e_d=\begin{cases}1&d=0,\\4&d\ne0,\end{cases}\quad
 z_a(d)=\begin{cases}i&d=b,\\m_d&d\ne b,\end{cases}\quad
 E_d=e_d+z_a(d)+z_c(d).
 \tag{P9}
\]
每个 \(K_d\) 的常数为单位，其 \(u^q\) 系数估值至少 \(q\)；除以 \(F_d\) 后仍如此。所有 \(E_d\le10\)。这计数的是完整分子，包含前面的 \(t\)。

定义
\[
 c'_d=e_d-\ell_d-4=(-7,-5,-4),\quad
 \rho'_a=c'_b/2+i,\quad
 \beta_{ac}=\min_d(E_d-\ell_d).
 \tag{P10}
\]
零、低、高簇的最大 \(\rho'\) 为 \(-1/2,-1/2,-1\)，并且
\[
 c'_d/2+m_d=(1/2,1/2,0).
 \tag{P11}
\]
同簇自盘 \(E_b-\ell_b-4=\rho'_a+\rho'_c\)；异盘的该指数是 \(1,1,0\)，故至少高一阶。不同簇时，盘 \(b\) 的指数相对行权和的余量是
\[
 c'_b/2+m_b-\rho'_c\ge1/2.
 \tag{P12}
\]
只有高簇对零/低簇可能达到半阶；相反盘和其余盘同理。因此
\[
 \beta_{ac}\ge\rho'_a+\rho'_c+4.
 \tag{P13}
\]
异簇严格多出至少半阶。原重数 \(4,3,2\) 仍够，但不能将所有交叉项写成额外一整阶。

## 3. 三阶局部估值及截断

von Staudt–Clausen 给 \(v_p(B_k^+)\ge-1\)，除正的 \((p-1)\) 倍数外为 \(p\)-整。对于
\[
 V_3^\circ(u^e)=(e)_3B_{e-3}^+,
 \tag{P14}
\]
可能有分母的次数是 \(e=q(p-1)+3\)。\(q=1,2,3\) 时，\((e)_3\) 至少有一个因子被 \(p\) 整除；第一处未由此取消的可能次数为 \(4p-1\)。所以 \(e\le4p-2\) 时是整的，全次数至少 \(-1\)。同理 \(V_1^\circ(u^e)\) 在 \(e\le2p-2\) 是整的，全次数至少 \(-1\)。

首一除法把 \(u^e/N_d\) 分成整系数商部和简单极点。节点及其差在0至4内，所有 Lagrange 残数和 P2 调和值都 \(p\)-整。因此
\[
 v_pV_3^\circ(u^e/N_d)\ge0\quad(e\le\ell_d+4p-2),
 \qquad v_pV_3^\circ(u^e/N_d)\ge-1\quad(\text{全部 }e).
 \tag{P15}
\]
一阶版本把 \(4p-2\) 换成 \(2p-2\)。若有限分子 \(S=\sum s_eu^e\) 在 \(e<E\) 为0，且 \(v_p(s_e)\ge e\)，\(E\le\ell_d+4p-2\)，逐项 P15 给 \(v_pV_3^\circ(S/N_d)\ge E\)：超过整性区的首个次数至少 \(E+1\)，足以付掉唯一一阶损失。

取 \(K=10n+2\)，令 \(S_d\) 是 \(G_{ac}(pu-d)/F_d(u)\) 截至次数 \(<K\) 的分子。自盘
\[
 S_b=p^{E_b}u^{E_b}w_b+\text{余项},\qquad v_p(w_b)=0,
 \tag{P16}
\]
同簇 \(w_b\) 不依赖 \(i,k\)。所有 \(E_d,E_d+1\le11\)；\(p\ge7\) 时它们同时落在一阶、三阶整性范围内。因此
\[
 p^{-4-\ell_b}\left(\tfrac1{24}V_3^\circ+\tfrac32p^2V_1^\circ\right)(S_b/N_b)
 =p^{\rho'_a+\rho'_c}w_bV_3(u^{i+k}r_b)
       +O_p(p^{\rho'_a+\rho'_c+1}),
 \tag{P17}
\]
其中 \(V_3=V_3^\circ/24\)，
\[
 r_0=\frac u{\prod_{1}^{4}(u+j)},\quad
 r_L=\frac{u^3}{\prod_{1}^{4}(u+j)},\quad
 r_H=\frac{u^3}{\prod_{1}^{3}(u+j)}.
 \tag{P18}
\]
一阶部分实际高至少两阶。同簇其它盘的估值至少 \(1,1,0\)，全部高一阶；异簇按 P12 高至少半阶。这是同一个完整 tuple 的估值。

## 4. 完整分布：商部与全部调和头

设 \(G=P+\sum c_j/(t+j)\)。由于 \(5n<p^2\)，每个同类不同极点的差的 \(p\) 估值恰为1，其余为0；完整分子因子 P9 给
\[
 v_p(c_j)\ge E_{j\bmod p}-(\ell_{j\bmod p}-1)\ge\beta_{ac}+1.
 \tag{P19}
\]
零残数同样满足此式。Bernoulli 分布多项式身份为
\[
 V_h^\circ(P)=p^{-(h+1)}
 \sum_{b=0}^{p-1}V_h^\circ(P(pu-b)),\qquad h=1,3.
 \tag{P20}
\]
它来自 \(B(P)=p^{-1}\sum_bB(P(pu-b))\) 和微分链式因子。这里 \(\deg P\le5n-1\)；每盘乘 \(N_b\) 后次数仍小于 \(K\)，对商部截断是精确的。

单个极点 \(c_j/(t+j)\) 的唯一近盘给
\[
 p^{-(h+2)}c_j(h+1)!H_{\lfloor j/p\rfloor}^{(h+2)}.
 \tag{P21}
\]
它恰是完整 \(c_j(h+1)!H_j^{(h+2)}\) 的全部 \(p\) 倍数部分；剩余调和头估值至少 \(v_p(c_j)\)。

远盘的 \(w=j-b\) 是单位，展开为
\[
 \frac{c_j}{w+pu}=\sum_{e\ge0}\frac{c_j(-p)^e}{w^{e+1}}u^e.
 \tag{P22}
\]
多项式泛函在 \(e<h\) 为0，\(e=h,h+1\) 的 Bernoulli 值是整的，其余至多损一阶，所以任意多项式截断的值估值至少 \(v_p(c_j)+h\)。实际操作是先乘 \(N_b\)、截到 \(<K\)、再除 \(N_b\)。它与先截 P22 到 \(<K-\ell_b\) 的差，分子系数估值至少 \(v_p(c_j)+K-\ell_b\)；全次数 P15 至多损一阶。经 \(p^{-(h+1)}\) 后，差估值至少
\[
 v_p(c_j)+K-\ell_b-h-2\ge v_p(c_j)-1.
 \tag{P23}
\]
主截断亦至少 \(v_p(c_j)-1\)。所以每个完整极点的分布误差至少 \(v_p(c_j)-1\)，P19 给全部极点和误差至少 \(\beta_{ac}\)。

组合 \(h=1,3\)，外因子分别是 \(p^{-2},p^{-4}\)，正是 P17 的 \(\tfrac32p^2,\tfrac1{24}\)。参数项 \(-T\sum c_j\) 估值至少 \(\beta_{ac}+1\)。由 P13，完整误差比行权和高至少4阶，参数项高至少5阶。没有继承旧 \(K_3\) 的 \(-2\)、旧局部矩，也没有删除非近极点。

## 5. 固定块及 primitive 常数约化

P2 对 P18 首一除法加全部残数，给 \(V_3^\circ\) 的连续矩：
\[
 \begin{array}{c|c|l}
 \text{簇}&\text{大小}&\text{连续矩（共同分母）}\\ \hline
 0&4&(907,-100,386392,-3869944,25158952,-135458680,658340584)/15552\\
 L&3&(48299,-483743,3144869,-16932335,82292573)/1944\\
 H&2&(-3587,14937,-53739)/24
 \end{array}
 \tag{P24}
\]
Hankel determinant 为
\[
 \det G_0^\circ=\frac{541936393813}{62208},\quad
 \det G_L^\circ=-\frac{100344353231}{3888},\quad
 \det G_H^\circ=-\frac{210779}{4}.
 \tag{P25}
\]
固定块 producer 对这三个固定有理矩阵做精确核验，未代入变化的 \(p\)。归一化 \(V_3=V_3^\circ/24\) 的 determinant 分别再除 \(24^4,24^3,24^2\)，P5 之外仍全是单位。

在 \(\mathbb Q_p(\sqrt p)\) 用 \(p^{-\rho'_a}\) 同时缩放行列。P17、P12及完整误差证明，归一化矩阵模极大理想是常数块对角矩阵
\[
 w_0G_0\oplus
 \bigoplus_{b=1}^{p-5}w_bG_L\oplus
 \bigoplus_{b=p-4}^{p-1}w_bG_H.
 \tag{P26}
\]
所有 \(w_b\) 和块 determinant 是单位。半阶交叉项仅用于严格消失；最终有理 determinant 系数的估值是整数。直接相加给
\[
 2\sum_a\rho'_a=5-9p.
 \tag{P27}
\]
CRT 变换 determinant 是单位，因此这证明原 monomial 完整 determinant 的 P6。每个包含 \(T\) 的 determinant 项至少有一个归一化估值≥5的参数条目，其余条目整；每个非恒定系数因此高至少5阶。primitive 比例的 \(p\) 估值必须抵消 P27，故保持相同常数约化。

采用第240轮相同 \(\widetilde Q_n=S_n^M Q_n/F_n\)，在 \(n=p-1\)
\[
 v_p(S_n)=4,\quad v_p(F_n)=6p-12,\quad
 v_p^{\rm Gauss}(\widetilde Q_n)=5-3p.
 \tag{P28}
\]
所以 primitive 比例 \(d_n\) 的该辅助素数估值恰为 \(3p-5\)。这不是 \(\log d_n\) 的全素数 \(n^2\) 预算。

## 6. 范围

在固定原源上已付三阶局部整性、完整分布误差、全部 CRT 盘隔离和所有大素数尺度的 primitive 常数约化；关系点无界非零不再是本源的未付接口。仍缺同一 primitive 模型的全素数费用和可用实处证书。没有证明 \(3\zeta(3)+\zeta(5)\) 无理，也没有证明全 \(n\) 非零。

实际阅读域和程序数见 [packet_reading_scope.md](../literature/logistic_prime_edge_round241_20261008/packet_reading_scope.md)。没有 FULL 读整个仓库、全部导入依赖或 Lean kernel；旧稿和主日志未改。
