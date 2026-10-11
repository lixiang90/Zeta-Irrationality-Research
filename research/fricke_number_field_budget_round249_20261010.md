# 第249轮：Fricke 三行源的数域费用与两嵌入准入

2026-10-10，B。数学程序、CAS、数值/prime/map/parameter/Lean 执行均为0。本稿只研究第248轮已经支付的同一源及当前完整安全数组，不改变旧稿、主日志、政策或manifest。没有新的数值无理性/线性无关性定理。

## 1. 同一真实假设、实际共轭与完整清分母

置 \(s=\sqrt2,\ K=\mathbb Q(s)\)，并采用A248实际源
\[
g_\pm=Y/2\pm s\pi^2/28,\quad
B_g^+=A_+(I_+-g),\quad
Q_\pm=1-(7\mp4s)t+t^2,\quad E=Q_+Q_-.
\]
本关的反证假设仅为 \(g=g_+\in K\)。另一个嵌入的实际函数是
\[
B_{\bar g}^-=A_-(I_--\bar g).
\tag{N1}
\]
这里不对未知实数 \(Y\) 任意施加代数共轭。若同时有 \(\bar g=g_-\)，则
\(\pi^2=(14/s)(g-\bar g)\) 代数，矛盾。因此
\[
\Delta=\bar g-g_-\ne0,\qquad
B_{\bar g}^-=B_{g_-}^- -\Delta A_-.
\tag{N2}
\]
这不是无理性结论；它首先禁止双处免费填同一canonical点。

取固定正整数 \(b\) 使 \(bg\in\mathcal O_K=\mathbb Z[s]\)。A248的完整prefix给
\[
7b\,d_N^2[t^j]B_g^+\in\mathcal O_K\quad(0\le j\le N),
\quad d_N=\operatorname{lcm}(1,\ldots,N).
\tag{N3}
\]
同一 statement 包括共轭、全部素数及素数幂。Euler微分只乘整数 \(j\)，整数多项式 \(E(t)\) 乘法只取 \(j\le n\) 的有限卷积，故完整清分母适用于
\[
f=(1,\ 7b B_g^+,\ 7b E(t)\delta B_g^+),\qquad \delta=t\partial_t.
\tag{N4}
\]
该固定gauge保持 \(K(t)\)-rank3；它不是新的primitive或联合整格优化。固定 \(7b\) 的理想norm虽为平方，按数域度数归一化后的对数仍为 \(\log(7b)\)，不产生两倍的leading费用。

合法literal类型为两列，不是一列行和：
\[
\mathbf b=
\begin{pmatrix}0&0\\1&1\\1&1\end{pmatrix},
\quad e=(0,0,0),\quad \sigma=(0,2,2).
\tag{N5}
\]
两列各有 \(u_j=1,b_j=1\)，因此
\[
\tau^\flat=\tau^{\flat\flat}
=2-\frac{1^2+1^2}{3^2}=\frac{16}{9},
\qquad \tau^\sharp=0.
\tag{N6}
\]
这里只计算已经支付的完整类型；没有证明它是所有可能整模型的最优费用。

## 2. 实际数域定理，而非把两个place当rank6

本轮实际完整读当前220页CDT物理PDF144的Remark8.2.42，以及PDF123–125的完整矩阵定义和Remark8.0.6。前者明确对每个嵌入 \(\sigma:K\hookrightarrow\mathbb C\) 分别选择 \(\phi_\sigma\)，以嵌入平均值归一化：
\[
\bar\lambda=\tfrac12(\lambda_++\lambda_-),\quad
\lambda_\sigma=\log|\phi_\sigma'(0)|,
\]
\[
\bar J=\tfrac12(J_++J_-),\quad
J_\sigma=\iint_{\mathbb T^2}
\log|\phi_\sigma(z)-\phi_\sigma(w)|\,d\mu(z)d\mu(w).
\tag{N7}
\]
当全部pullbacks全纯，且 \(\bar\lambda>\sigma_3=2\)，其显示的结论为
\[
3\le \frac{\bar J}{\bar\lambda-16/9}.
\tag{N8}
\]
这个原文条件不能悄悄改成meromorphic，也不能只因已知holonomicity就声称Remark字面已经放宽至 \(16/9\)。使用在闭盘邻域定义的图；开盘图可先缩盘再取径向极限。

固定三行只有rank3。Hermitian \(\mathcal O_K\)-module在各实嵌入取对应度量，有限处采用
\(|p|_v=p^{-[K_v:\mathbb Q_p]/2}\)，两个实嵌入采用欧氏绝对值的 \(1/2\) 次幂。正交direct sum是构造源度量的方式，不把共轭复制品计作六个独立函数，更不能把重复常数1计成新行。固定有理整数的归一化有限norm为原有理对数，故(N6)不再乘2。

Jensen给每个 \(J_\sigma\ge\lambda_\sigma\)。若(N8)右边要严格小于实际rank3，则必有
\[
\bar J<3(\bar\lambda-16/9)
\quad\Longrightarrow\quad
\boxed{\bar\lambda>8/3.}
\tag{N9}
\]
所以潜在strict入口自动满足Remark要求的 \(\bar\lambda>2\)。共同源里仅有一条整数背景行1，它只支持上述rank1/Jensen约束；不能搬用原五行中三条整数field行给出的 \(J\ge3\lambda\)，也没有从本源恢复那三行。

当两图univalent时 \(J_\sigma=\lambda_\sigma\)，故(N9)同时是这个显示公式严格rank<3的精确门槛。仅有正分母的较弱门槛为 \(\bar\lambda>16/9\)。

## 3. 有限点的完整clearing与全叶无穷远障碍

以下使用实际二阶方程和完整Fricke/Γ返回，而不是由某条坏叶推断所有图。普通导数形式的一次项为
\[
\partial_t^2+
\left\{\frac1t+\frac12\left(\frac{Q_-'}{Q_-}
-\frac{Q_+'}{Q_+}\right)\right\}\partial_t+q_+(t).
\tag{N10}
\]
本轮实际 FULL 独核 Root249 的六节完整局部证书
fricke_univalent_product_gate_round249_20261010.md（8502 B，
SHA256 e15164de3d8f00cf4901e81637c3950a44fa70c53991ec1e6d1f0980952ee165）；
以下局部输入和有限forcing同时由该同对象证明支付，不以协作消息代替读取。
唯一有限singular set为 \(\{0\}\cup\{E=0\}\)。在Q+根，齐次指数为 \(1/2,1\)；在Q−根为 \(0,1/2\)；在0及∞为 \(0,0\)。这些指数也可直接由actual modular uniformizer \(w^2=t-e\)、齐次解 \(A_+,\tau A_+\) 及cusps核定，不借一般Fuchs标签代替叶的说明。

在有限E根的每条实际叶，\(B_g\) 在w中收敛，且无负幂：primitive在上半平面全纯，所有返回差属于同一齐次二维空间。因此 \(\delta B_g\) 至多 \(w^{-1}\)，\(E\delta B_g\) 有界。在0，返回叶只增加齐次analytic/log项，不产生负Laurent幂。若拉回本来meromorphic，log项必须消失。故(N4)的任何共同meromorphic拉回，事实上在所有有限原像处removable，成为Remark所要求的全纯拉回。此结论包括图的ramification；不能通过有限ramification消掉非零log。

forcing的完整有限证书为
\[
\mathcal R_+(t)
=\frac{t[11+9s-8(1+s)t]}{7Q_-(t)}.
\tag{N11}
\]
在∞，\(\mathcal R_+\to-8(1+s)/7\ne0\)，δ形式的两个齐次系数均为 \(O(1/t)\)。Frobenius的最高log层因此给
\[
B_g^+=-\frac{4(1+s)}7(\log t)^2+O(\log t)
\quad\text{加收敛的 }t^{-1}\text{ 修正项}.
\tag{N12}
\]
任何两返回叶的差是齐次解，至多一级log，故全部叶都有同一个非零最高log²系数。这个statement针对同一rationalforcing，而不是说某一native展开自动控制任意不同源。

## 4. 两place的univalent乘积cap

令
\[
r=\frac{7+4s-\sqrt{77+56s}}2,\quad 0<r<1.
\]
Q−的两根为r与 \(r^{-1}\)，Q+两根的模为1。native区间 \([0,r]\) 的终点对应W14固定点；A−在那里有非零simple w项。精确取
\(\zeta=(\tau-\tau_*)/(\tau-\bar\tau_*)\)，则W作用为 \(\zeta\mapsto-\zeta\)，
而 \(A_-/(1-\zeta)\) 是odd holomorphic函数，其一阶项非零；
不能把未gauge的weight1函数 \(A_-\) 直接称为odd。
目标 \(B_{g_-}^-\) 由完整Fricke identity为even，故(N2)的actual odd part
精确为 \(-\Delta A_-/(1-\zeta)\ne0\)。
因此实际系数共轭 \(B_{\bar g}^-\) 沿该native路径在r有不可去的平方根分支。

设两place共同合法图分别univalent，\(c_\sigma=|\phi_\sigma'(0)|\)。Koebe四分之一定理使 \(\phi_-(\mathbb D)\) 含中心圆盘半径 \(c_-/4\)。若 \(c_->4r\)，这个圆盘含整个native路径及r；单值meromorphic拉回将给r处meromorphic continuation，矛盾。因此
\[
c_-\le4r.
\tag{N13}
\]
这一论证固定的是native路径，而不是任取一个坏transported leaf。

另一方面，若 \(c_+>4/r\)，Koebe圆盘含全部有限singular points。取半径 \(r^{-1}<R<c_+/4\) 的圆：完整源在image上的单值meromorphic realization使此圆的返回单值。但它围住全部有限singular set，等价于∞返回；与(N12)全部叶的非零log² monodromy矛盾。因此
\[
c_+\le4/r,\qquad c_+c_-\le16,\qquad
\boxed{\bar\lambda\le\log4<16/9<8/3.}
\tag{N14}
\]
当前完整安全类型的所有arch-univalent两嵌入入口由此失配，甚至正分母也无余量。它不证明 \(g_+\notin K\)，不关闭multivalent图，不证明最优费用lower，也不移植原x坐标的旧cap。

## 5. All-place版本保留的确切门槛

本轮实际完整重读官方ICM论文PDF3–8，包括normalized绝对值、完整Theorem2.6条件、direct-sum源及local-height/slopes证明。在已经支付各finite处的解析图、meromorphic与reduction条件时，同一qualitative slopes计算的量是
\[
\lambda_{\rm all}=\bar\lambda+\sum_{v\nmid\infty}
\log|\phi_v'(0)|_v,\qquad
J_{\rm all}=\bar J+\sum_{v\nmid\infty}
\sup_{|z|_v=1}\log|\phi_v(z)|_v.
\tag{N15}
\]
identity图在两个finite项均贡献0；一般图须在闭盘邻域解析，all but finitely many为identity，并须核全部函数的实际meromorphic/reduction数据。上述形式是原proof的qualitative、无approximation correction的slopes接口，不把其quantitative soft-target结论直接改称当前无理性定理。

相同归一化下，在正分母条件 \(\lambda_{\rm all}>16/9\) 下，三行必要不等式为
\[
3\le J_{\rm all}/(\lambda_{\rm all}-16/9).
\tag{N16}
\]
它也能直接从所读proof核量纲：取同一源的
\[
\mathcal E_D=d_D^{-2}\mathcal O_K[1/t]_{\le D}\,f_1
\ \oplus\ \mathcal O_K[1/t]_{\le D}\,f_2
\ \oplus\ \mathcal O_K[1/t]_{\le D}\,f_3 .
\]
对应BC/finite度量的归一化degree为
\((3J_{\rm all}/2+2)D^2+o(D^2)\)；两列的逐层denominator height为
\(2\max(n,D)+o(n+D)\)。采用原文的holonomic zero estimate，实际非零grades有
\(3(D+1)\) 个且落在 \(0\le n\le(3+\varepsilon)D\)，再令 \(\varepsilon\to0\)。
所以其费用总和至多 \(10D^2+o(D^2)\)，derivative项总和为
\(-(9/2)\lambda_{\rm all}D^2+o(D^2)\)，BC评价项为
\(3J_{\rm all}D^2+o(D^2)\)。slopes遂给
\((9/2)\lambda_{\rm all}\le(3/2)J_{\rm all}+8\)，恰为(N16)。
这里采用的是所读primary已经给出的Hilbert–Samuel与zero-estimate条件，未声称本稿重证它们。
finite最大模原理给该处的sup至少derivative对数，故 \(J_{\rm all}\ge\lambda_{\rm all}\)，strict仍需 \(\lambda_{\rm all}>8/3\)。结合(N14)，任何靠新增positive finite charts绕过本univalent cap的方案，至少必须实际支付
\[
\sum_{v\nmid\infty}\log|\phi_v'(0)|_v
>8/3-\log4.
\tag{N17}
\]
仅为正分母则需超过 \(16/9-\log4\)。这些是必要门槛，不是已构造的finite图，也不是所有all-place方案的排除。Taylor半径或安全LCM上界不能替代相应p-adic meromorphic/reduction证明。

本轮的行动结论：停止当前safe类型的arch-univalent双place入口；如果保留本三行源，首个必须改变的证据只能是合法multivalent同对象能量、真正paid positive finite图，或不同完整整模型。不要以某处未填点单独领取全图no-go，也不要开始prime/map参数扫描。实际来源身份与完整读取范围另见本轮packet_reading_scope.md。
