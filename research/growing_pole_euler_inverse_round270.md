# 第270轮独立子证书：固定Euler jet的显式逆与来源高度

2026-10-20。只研究[269](global_source_review_round269.md)的(G4)–(G5)，固定m≥1、n=8m、同一组唯一p_i；不改变比例、纯化空间或目标，不执行样本、CAS或参数扫描。本证书给实际系数的全尺度公式与完整有限处分母上界，**不给Q_m最小清整或负净预算**。

## 1. 把实际逆写成连续整数节点的Hermite插值

记
$$
N=8m-1,\quad M=4m-1,\quad s=2m,\quad
b_r(\alpha)=(-1)^r\binom{\alpha}{r},\qquad b_0=1.
$$
写u_i=z^{4m}v_i、deg v_i≤M，并设
$$
H_i(\alpha)=[z^M]v_i(z)(1-z)^\alpha,\qquad
F_i(x)=H_i((x-1)/2),\qquad R=N-i.
$$
这里的H_i、F_i都是次数≤M的有理多项式。以下式子直接由(G5)变换而来，并未另选一组基底。

对0≤k<m，四族z^j{1,a−1,L,aL}先作整数二项式三角换基，成为w^k、w^{k−1/2}及它们的log w倍，w=1−z。在{1,a}栏，(G5)的特殊δ项同时出现在两个value栏；log栏没有该项。因此恰有
$$
H_i(k)=\frac12b_i(k),\qquad
H_i(k-\tfrac12)=\frac12\{b_i(k)-b_R(k-\tfrac12)\},
$$
$$
H_i'(k)= -\frac12 b_R'(k),\qquad
H_i'(k-\tfrac12)= -\frac12 b_R'(k-\tfrac12).
\tag{E1}
$$
例如log栏的右侧是\(-\tfrac12[z^R](1-z)^\alpha\log(1-z)\)，故导数符号不能省略。换到x后，节点恰为0,…,s−1。令
$$
\lambda_j=(j-1)/2,\qquad
c_{2k}=b_i(k)-b_R(k-\tfrac12),\quad c_{2k+1}=b_i(k).
$$
完整插值数据为
$$
F_i(j)=c_j/2,\qquad F_i'(j)=-b_R'(\lambda_j)/4.
\tag{E2}
$$
第二式的1/4包含x=2α+1的导数费用。

定义通常的Lagrange多项式与其节点导数
$$
\ell_j(x)=\prod_{\substack{0\le h<s\\h\ne j}}\frac{x-h}{j-h},
\qquad
\eta_j=\ell_j'(j)=\mathsf H_j-\mathsf H_{s-1-j},
$$
其中\(\mathsf H_t=\sum_{h=1}^t1/h\)、\(\mathsf H_0=0\)。那么实际唯一解为
$$
F_i(x)=\sum_{j=0}^{s-1}\left[
\frac{c_j}{2}\{1-2(x-j)\eta_j\}\ell_j(x)^2
-\frac{b_R'(\lambda_j)}4(x-j)\ell_j(x)^2\right].
\tag{E3}
$$
这不是逆det包络，而是每个实际系数的有限封闭公式。恢复v_i时只需Newton差分：
$$
[z^{M-r}]v_i=(-1)^r\Delta^r H_i(0)
=(-1)^r\sum_{t=0}^r(-1)^{r-t}\binom rt F_i(2t+1),
\quad 0\le r\le M.
\tag{E4}
$$
因为\(H_i(\alpha)=\sum_{r=0}^M[z^{M-r}]v_i\,b_r(\alpha)\)。所有被评价的x=2t+1均为1,…,N间的整数。

## 2. 全部素数幂的共同来源分母

记d_h=lcm(1,…,h)，d_0=1。连续整数节点的一个关键性质是：对每个整数x，
$$
\ell_j(x)=(-1)^{s-1-j}\binom xj\binom{x-j-1}{s-1-j}\in\mathbb Z.
\tag{E5}
$$
广义整数二项式也覆盖x<j的情形。因此整值性本身不给(s−1)!的费用。\(\eta_j\)的分母整除d_{s−1}。

先单独记录一般逆的范围：若原(G4)的任意右端向量为整数，则变换后的α节点value及α导数仍为整数。x导数至多引入1/2，(E3)的value Hermite基在整数x的分母整除d_{s−1}、derivative Hermite基整数值；(E4)保持这些分母。故原\(\mathcal T^{-1}\)的**每个条目分母整除2d_{s−1}**。这不意味着任意输入的幅值很小。

本轮(E2)的特殊数据还能避免把d_{s−1}和d_N重复相乘。对半整数α=k−1/2，
$$
b_r(\alpha)\in4^{-r}\mathbb Z,
$$
由\((1-z)^{k-1/2}=(1-z)^k(1-z)^{-1/2}\)及中心二项式系数即得。对整数节点亦成立。导数的卷积恒等式是
$$
b_r'(\alpha)=-\sum_{h=1}^r\frac{b_{r-h}(\alpha)}h.
\tag{E6}
$$
故在所有本轮整数/半整数节点，
$$
b_r'(\alpha)\in(4^{r-1}d_r)^{-1}\mathbb Z\quad(r\ge1).
$$
这里不能把乘积形式中表面的奇数分母逐个相乘；(E6)已付全部抵消。

现有c_j∈4^{-N}Z。将(E3)分为三项：
$$
\frac{c_j}{2}\ell_j^2,\qquad
-c_j(x-j)\eta_j\ell_j^2,\qquad
-\frac14b_R'(\lambda_j)(x-j)\ell_j^2.
$$
在整数x，它们的分母依次整除\(2\cdot4^N\)、\(4^Nd_{s-1}\)、\(4^Nd_N\)。由于d_{s−1}|d_N，(E4)证明共同来源分母可以取
$$
\boxed{D_m=2\cdot4^{8m-1}d_{8m-1}}.
\tag{E7}
$$
它同时清除全部i、全部p_i的全部系数；z→1+T是整数二项式变换，也不新增分母。每个素数幂明确为
$$
v_p(D_m)=(16m-1)\mathbf1_{p=2}
+\max\{a\ge0:p^a\le8m-1\}.
\tag{E8}
$$
所以没有未支付的高次幂或大于8m−1的奇素数。这是上界证书，不是最小基底分母或Q_m的本原内容公式。

特别地
$$
\log D_m=(16m-1)\log2+\psi(8m-1)=O(m),
$$
其中\(\psi(h)=\log d_h\)；末项可用初等Chebyshev界。若使用标准\(\psi(h)\sim h\)，本来源分母上界的线性率为16log2+8，不能直接把此数当Q_m的二次费用。

## 3. 实际系数幅值也是exp(O(m))

本轮R=N−i≥7m且k≤m−1。整数节点有
$$
|b_i(k)|\le2^{m-1},\qquad
|b_R'(k)|=\frac1{(R-k)\binom Rk}\le1.
$$
半整数节点则由
$$
\frac{|b_R(k-\tfrac12)|}{b_R(-\tfrac12)}
=\prod_{h=1}^k\frac{h-\tfrac12}{R-h+\tfrac12}\le1
$$
得\(|b_R(k-\tfrac12)|\le1\)。对数导数中的半整数距离给
$$
|b_R'(k-\tfrac12)|\le4\mathsf H_{2N+1}.
$$
因此(E2)的value幅值≤2^{m−1}，x导数幅值≤\(\mathsf H_{2N+1}\)。

令
$$
C_m=2^{s-1}\binom N{s-1}.
$$
在1≤x≤N的整数上，(E5)给\(|\ell_j(x)|\le C_m\)：节点区间内为δ；x≥s时用
\(\binom xj\binom{x-j-1}{s-1-j}\le
\binom x{s-1}\binom{s-1}j\)。
再用\(|x-j|\le N\)、\(|\eta_j|\le\mathsf H_{s-1}\)，得到每个实际v_i系数的明确上界
$$
\boxed{
|[z^h]v_i|\le U_m:=
2^M sC_m^2
\left[2^{m-1}(1+2N\mathsf H_{s-1})
+N\mathsf H_{2N+1}\right]}.
\tag{E9}
$$
这同时涵盖全部i与h；不通过任何有限样本外推。Stirling公式给
$$
\limsup_{m\to\infty}m^{-1}\log U_m
\le9\log2+16\,\mathfrak h(1/4),
\quad
\mathfrak h(t)=-t\log t-(1-t)\log(1-t).
\tag{E10}
$$
故在z坐标中，清整后实际整数来源的系数高度≤D_m max(1,U_m)=exp(O(m))。若改写成实际T坐标，二项式展开给每个系数再至多乘(N+1)2^N，仍为exp(O(m))；共同分母不变。小det的−16(log2)m²在本实际逆中没有被当作m²行高度。

## 4. 同对象实处安全界及结论范围

这部分只说明上述证书如何放回实际Gram，不宣称解析界已足够。对z=1+T∈[1,2]，
$$
\frac{p_i(z)}{z^{4m}}=z^{i-4m}+v_i(z),
\quad
\left|\frac{p_i(z)}{z^{4m}}\right|
\le1+4mU_m2^M.
$$
剩余正测度\((-\log T)(2+1/(2\sqrt T))\,dT\)总质量为4。Hadamard因此给同一个M_m
$$
0<\det M_m\le
\left[4(1+4mU_m2^M)^2\right]^m.
\tag{E11}
$$
其上包络的二次率是正数，单凭本证书不能证明(G9)；上界不足亦不是实际det增长的下界。

已付的是固定canonical来源的**显式实际逆、全部基系数与全素数幂共同分母、exp(O(m))幅值**。尚未支付：全部有理头R_m如何在同一Q_m中约分、最小λ_m及本原信用、实际Gram足够强的实处界，以及完整严格净余量。先清来源再清Q和直接清Q必须选一致费用链；本D_m不能再被当独立免费信用。没有新无理性结论。
