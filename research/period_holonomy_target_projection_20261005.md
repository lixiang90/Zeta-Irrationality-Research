# 实际 trigamma / Lerch 周期的有限投影、整格与 holonomy 接口

日期：2026-10-05。旧报告冻结。本稿提供一个可以闭合的扩大目标族：所有 \(\psi_1(n/6)\)、其有限有理线性组合，以及这些目标之间的全部有理关系。所用数值独立性是 CDT 已证的 Theorem A；下文分类是其有效推论，不声称为新的全球无理性定理。

另给出两种不同的实际函数结构：原 normalized Lerch 系统中，含 \(t\) 个非零残数的常数滤波行有实际 cyclic rank \(2t+1\)；覆盖后重新选择 periodic polylog 行则在任意模数下有统一的权重 \(s+1\) 维闭合系统。后者能真实删掉平均值为零的角色在 1 的 monodromy，但不能自动当作有理 Betti 商。完整前缀整格可用同余 Smith 数据计算；固定投影的有限指标不能代替随尺度变化的全部 content。原 normalized 模型的自然 LCM 账本在通常割平面上不能通过 CDT 的严格门槛；这是该账本的结论，不是最优分母或所有改造的排除定理。

## 1. CDT 的固定版本与应用链

本轮读的是 [CDT arXiv:2408.15403v2，2024-09-16](https://arxiv.org/abs/2408.15403v2)，[固定本地 PDF](../literature/cdt2024_l2_chi_minus3.pdf)，218 页，SHA-256 为 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。PDF 首页的 v2 标记与归档 manifest 一致。Theorem A 在 PDF 第 3 页，Corollary B 在第 4 页。

这里的 §7 是长稿的 Bost 斜率与凸性 holonomy 界；真正将这些界接到 \(1,\zeta(2),L(2,\chi_{-3})\) 的证明在 §13。其实际链条为：假设一个数值有理关系，Proposition 11.1.8 构造 \(\mathbb Q[[x]]\) 中的真实芽；§11.2 对称化；Lemma 12.1.1 保证 14 个实际函数的 \(\mathbb Q(y)\) 独立；Lemma 10.2.2 提供全部分母表；再使用 §7 的严格秩上界。§13 的分母成本为

\[
\tau=\frac{191}{49}+\frac{27}{80}=\frac{16603}{3920}.
\tag{1}
\]

§13 通过 Theorem 7.0.1 得到小于 14 的上界；Theorem 7.1.6 的凸性加强给出更大余量。这里没有把函数独立性直接特化为数值独立性。

另一个固定文件 [arXiv:2510.04156v1，2025-10-05](https://arxiv.org/abs/2510.04156v1)，[本地 PDF](../literature/cdt2025_arithmetic_holonomy.pdf)，只有 20 页和 §§1–5。其 §5 是有效逼近应用；不能将长稿 §7 的编号移植给短稿。

本稿连接已有 [真实商周期拉回与整格报告](odd_zeta_bridge_projection_20261004.md)，但这里所有数值投影都由收敛级数 / 实积分证明，不使用形式 Tate 商。已有 [新周期系统](odd_zeta_new_period_systems_20261004.md) 的 actual rank 与 [Catalan 相对端点](odd_zeta_k2_regulator_20261004.md) 的真实边界修正也说明：数值身份、实际函数秩和整数成本必须逐项认证。

## 2. 一个真实的有限投影：六个残数到两个周期

记

\[
P=\zeta(2),\qquad L=L(2,\chi_{-3}),\qquad
S_r=\sum_{n\ge0}\frac1{(6n+r)^2},\quad 1\le r\le6.
\tag{2}
\]

由绝对收敛可任意按剩余类重排。设

\[
a=(12,4,3,4,12,1),\qquad b=(5,1,0,-1,-5,0).
\]

则实际数值等式是

\[
S_r=\frac{a_r}{36}P+\frac{b_r}{8}L,
\qquad
\psi_1(r/6)=a_rP+\frac92 b_rL.
\tag{3}
\]

可不借反射公式推导 (3)：模 3 的两非零残数之和为 \((1-3^{-2})P=8P/9\)，之差为 \(L\)；偶数子列缩放因子为 \(1/4\)，且 \(\chi_{-3}(2)=-1\)。再加入倍数 3 和倍数 6 的子列即得六项。

例如

\[
\psi_1(1/6)=12P+\frac{45}{2}L,
\quad \psi_1(1/3)=4P+\frac92L,
\quad \psi_1(1/2)=3P.
\tag{4}
\]

这正包含 CDT Corollary B 的值，但此处进一步保留所有组合的整数格。投影没有删去 \(P\)；它与 \(L\) 同时保留，因而可直接使用已证 \(1,P,L\) 的数值独立性。

一般模数也有同样真实的 Fourier 接口。对 \(s\ge2\)，令

\[
H_{m,a}^{(s)}=\sum_{n\ge0}(mn+a)^{-s},\qquad \xi=e^{2\pi i/m}.
\]

在单位圆上仍由绝对收敛得到

\[
\operatorname{Li}_s(\xi^k)=\sum_{a=1}^{m}\xi^{ka}H_{m,a}^{(s)},\qquad
H_{m,a}^{(s)}=\frac1m\sum_{k=0}^{m-1}\xi^{-ka}\operatorname{Li}_s(\xi^k),
\tag{5}
\]

以及 \(L(s,\chi)=\sum_a\chi(a)H_{m,a}^{(s)}\)。实二次角色有整数权 \(0,\pm1\)，可直接滤波；非实角色必须保留系数域及完整 Galois 轨道。式 (5) 是实际数值身份，不是对超越数实施未经定义的 Galois 共轭。仅在单位群上做角色 Fourier 变换不能恢复非单位残数；它们还需按 gcd 降模数。

## 3. 全部有理组合的无理性与独立性分类

写唯一分解 \(n=r+6q\)，其中 \(1\le r\le6\)、\(q\ge0\)。由 trigamma 级数直接相消，

\[
T_n:=\psi_1(n/6)=C_n+a_rP+\frac92 b_rL,
\qquad
C_n=-36\sum_{j=0}^{q-1}\frac1{(r+6j)^2}\in\mathbb Q.
\tag{6}
\]

递推亦见 [NIST DLMF 5.15.1、5.15.5](https://dlmf.nist.gov/5.15)，本轮核对网页版本 1.2.8，2026-09-15。这里 (6) 的证明只用绝对收敛级数。

**闭合分类推论。** 任取有限有理权 \(c_0,c_1,\ldots,c_d\) 和正整数 \(n_i\)，置

\[
T=c_0+\sum_i c_iT_{n_i}=C+AP+BL,
\quad
(C,A,B)=\Bigl(c_0+\sum_i c_iC_{n_i},\sum_i c_i a_{r_i},\frac92\sum_i c_i b_{r_i}\Bigr).
\tag{7}
\]

则 \(T\in\mathbb Q\) 当且仅当 \(A=B=0\)；否则 \(T\) 无理。给定目标列表 \(T^{(1)},\ldots,T^{(d)}\)，

\[
\dim_{\mathbb Q}\langle1,T^{(1)},\ldots,T^{(d)}\rangle
=1+\operatorname{rank}_{\mathbb Q}
\begin{pmatrix}A_1&\cdots&A_d\\B_1&\cdots&B_d\end{pmatrix}.
\tag{8}
\]

**证明。** CDT Theorem A 给出 \(1,P,L\) 的数值 \(\mathbb Q\)-独立。故 (7) 有理当且仅当两个非有理坐标都消失；(8) 是在这个实际独立基中取坐标的线性代数。证毕。

例如 \(1,T_1,T_2\) 独立，因其 \((A,B)\) 行列式为 \(-36\)。但 \(T_1-5T_2+8T_6=0\)，而且

\[
T_7=T_1-36,\qquad49T_{13}-49T_1+1800=0.
\tag{9}
\]

因此扩大的是可分类目标集合，不是已证周期空间的维数。

## 4. 饱和整数格、完整 content 与增长的边界分母

式 (3) 对 \(2T_r\) 的整数投影矩阵为

\[
M=\begin{pmatrix}24&8&6&8&24&2\\45&9&0&-9&-45&0\end{pmatrix}
=\operatorname{diag}(2,9)
\begin{pmatrix}12&4&3&4&12&1\\5&1&0&-1&-5&0\end{pmatrix}.
\tag{10}
\]

右侧第二矩阵 \(N\) 满射到 \(\mathbb Z^2\)：第六列为 \((1,0)\)，第二列减去四倍第六列为 \((0,1)\)。因此

\[
M\mathbb Z^6=2\mathbb Z\oplus9\mathbb Z,
\quad \operatorname{SNF}(M)=(1,18).
\tag{11}
\]

其饱和核的整数基为

\[
e_1-5e_2+8e_6,\quad e_3-3e_6,\quad
e_4+e_2-8e_6,\quad e_5+5e_2-32e_6.
\tag{12}
\]

连同 \(e_6\) 和 \(e_2-4e_6\) 组成 \(\mathbb Z^6\) 的 unimodular 基。这是全整数核，而不只是有理 nullspace 的任意清分母基。

原始残数 \(S_r\) 的周期格恰为

\[
\sum_r\mathbb ZS_r=\frac1{36}\mathbb ZP\oplus\frac18\mathbb ZL.
\tag{13}
\]

特别地，消去 \(P\) 的整数滤波格对 \(L\) 的像为 \(\frac18\mathbb ZL\)，例如 \(S_2-4S_6=L/8\)。对称滤波 \(S_2-S_4=L/4\) 则有正系数的差分表达及正积分。只有一个非零残数不可能产生纯 \(L\)，因为全部 \(a_r\ne0\)；两个残数足以做到。

给定整数滤波权 \(c\)，投影后的全部整数 content 为

\[
\operatorname{cont}(Mc)=\gcd(2a\cdot c,9b\cdot c),
\tag{14}
\]

不能以 \(\gcd(c_1,\ldots,c_6)\) 代替。例如

\[
c=(1,-5,0,0,0,p+8)
\quad\Longrightarrow\quad \gcd(c)=1,\quad Mc=(2p,0).
\tag{15}
\]

故 fixed finite projection 的指标 18 不限制其非单射像上的单行 content 增长。一般固定方阵 \(A\in M_d(\mathbb Z)\)、\(\det A\ne0\) 则由 adjugate 得

\[
\operatorname{cont}(v)\mid\operatorname{cont}(Av),\qquad
\operatorname{cont}(Av)\mid |\det A|\operatorname{cont}(v).
\tag{16}
\]

非单射投影不满足这样的统一单行界，(15) 已给反例。这与已有报告的固定整格指标界没有冲突。

对 (7) 的实际完整行，取 \(D\) 为 \(C,A,B\) 的公共分母，令

\[
(u,v,w)=D(C,A,B),\quad h=\gcd(u,v,w),\qquad
\frac D h T=\frac u h+\frac v hP+\frac w hL.
\tag{17}
\]

这是相对于已证独立基 \((1,P,L)\) 的完整 primitive 行。缩放 \(D/h\) 可以是非整数；例如 \(T_1\) 的 primitive 行为 \((0,8,15)\)，等于 \((2/3)T_1\)。因此它是同一有理周期直线的 primitive 代表，不能不记缩放就充当原目标的整数倍。若整个行为零，直接记录零关系，不除以零 content。多个目标的全部整数关系是其三坐标矩阵的整数核；清公共分母后用 Smith/Hermite 数据求饱和核。

随参数增长的 \(C_n\) 不能用固定坏素数消除：对任意素数 \(p>3\)，在 \(C_{p+6}\) 的和中，唯一被 \(p\) 整除的分母底数为 \(p\)。其他底数均小于 \(p\)，而 36 是 \(p\)-单位，故

\[
v_p(C_{p+6})=-2.
\tag{18}
\]

因此实际端点平移修正会引入所有大素数。数值分类已闭合，不意味着这整个增长族的整数逼近成本是常数。

## 5. 任意模数的实际 Lerch 系统与 cyclic rank

对整数 \(m\ge1\)、\(1\le a\le m\)、\(j=1,2\)，定义真实解析芽

\[
F_{a,j}(z)=\sum_{n\ge0}\frac{z^n}{(mn+a)^j}.
\tag{19}
\]

它们有实际积分表达（\(j=2\)）：

\[
F_{a,2}(z)=\int_0^1\frac{t^{a-1}(-\log t)}{1-zt^m}\,dt.
\tag{20}
\]

在 \(|z|<1\) 由逐项积分证明；随后给出 \(\mathbb C\setminus[1,\infty)\) 上的解析延拓。\(F_{a,2}(1)=H_{m,a}^{(2)}\) 存在，因 \(-\log t\) 在 1 端消去分母的一阶零。\(F_{a,1}\) 一般在 1 端对数发散，不能把整个系统的每行都当作有限端点值。

记 \(\theta=z\,d/dz\)，则包括常数 1 的闭合有理系统为

\[
(m\theta+a)F_{a,1}=\frac1{1-z},\qquad
(m\theta+a)F_{a,2}=F_{a,1},\qquad \theta1=0.
\tag{21}
\]

**实际秩引理。** \(1,F_{a,1},F_{a,2}\;(1\le a\le m)\) 在 \(\mathbb Q(z)\) 上独立。任取非零常数滤波 \(f=\sum_{a\in A}c_aF_{a,2}\)，其中所有 \(c_a\ne0\)，\(|A|=t\)，则 \(f\) 的实际微分 cyclic space 维数恰为 \(2t+1\)。

**独立性证明。** 令 \(z=x^m\)，有

\[
x^aF_{a,j}(x^m)=\frac1m\sum_{k=0}^{m-1}\xi^{-ak}\operatorname{Li}_j(\xi^kx).
\tag{22}
\]

在 \(x=\xi^{-k}\) 周围，\(\operatorname{Li}_1(\xi^kx)\) 的单值差是非零常数，\(\operatorname{Li}_2(\xi^kx)\) 的单值差是非零常数乘 \(\log x+\gamma_k\)。对任何有理函数关系取该 monodromy 差，由 \(\log x\notin\mathbb C(x)\) 先得到第二层系数的 Fourier 和全为零；Fourier 矩阵可逆，第二层全零。再取差得到第一层全零，最后常数全零。这样甚至证明相应 \(x\)-函数的 \(\mathbb C(x)\) 独立，故得到所需 \(\mathbb Q(z)\) 独立。分支常数 \(\gamma_k\) 不影响 \(\log x\) 的系数。

**cyclic 证明。** 模掉有理常数行后，(21) 是特征值 \(\lambda_a=-a/m\) 各有大小 2 的 Jordan 块。\(\theta^\nu f\) 对每个块的系数为

\[
c_a\lambda_a^\nu,\qquad \frac{c_a}{m}\nu\lambda_a^{\nu-1}.
\]

取 \(\nu=0,\ldots,2t-1\) 的 confluent Vandermonde 行列式为

\[
\prod_{a\in A}\frac{c_a^2}{m}
\prod_{a<b}(\lambda_b-\lambda_a)^4\ne0.
\tag{23}
\]

所以已得到模常数的全部 \(2t\) 维。再令

\[
Q_A(\theta)=\prod_{a\in A}(m\theta+a)^2,
\quad Q_A(\theta)f=R_c(z)\in\mathbb Q(z).
\tag{24}
\]

其 \(z^n\) 系数为多项式

\[
\sum_{a\in A}c_a\prod_{b\ne a}(mn+b)^2.
\tag{25}
\]

在 \(n=-a/m\) 代入，只有对应项保留且非零。因此 \(R_c\not\equiv0\)，常数行也进入 cyclic space。标量算子

\[
\left(\theta-\frac{\theta R_c}{R_c}\right)Q_A(\theta)
\tag{26}
\]

给出阶 \(2t+1\) 的闭合方程；所有分母只依赖 \(z\) 和已经固定的有理权。证毕。

例如 \(F_{1,2}-F_{2,2}\)（\(m=3\)）的端点为 \(L\)，实际 rank 是 5；不是仅有 \(1,L\) 的两维系统。另取 \(m=6\)、\(c=(1,-5,0,0,0,8)\)，端点恰为零，但 actual rank 为 7。这是“实际函数独立”不能自动推出“目标数值非零”的精确例子。

若所有选定的 \(a\) 与 \(m\) 有共同因子 \(g\)，应先用 \(F_{m,a,j}=g^{-j}F_{m/g,a/g,j}\) 降模数；这是固定有理缩放，不应重复支付虚假的大模数成本。

还可证明一个真实的局部相消障碍。在 1 的实邻域取 \(\log1=0\) 的分支，并从 \((0,1)\) 沿标准路径取绕 1 的正向局部小环。由 (22) 中唯一在 \(x=1\) 有分支的项得

\[
\Delta_1F_{a,1}=-\frac{2\pi i}{m}z^{-a/m},\qquad
\Delta_1F_{a,2}=-\frac{2\pi i}{m^2}z^{-a/m}\log z.
\tag{26a}
\]

因 \(\log z\) 超越于代数函数域，而 \(z^{-a/m}\;(1\le a\le m)\) 在 \(\mathbb Q(z)\) 上独立，(26a) 表明整个系统的 \(\mathbb Q(z)\) 线性空间中，局部 monodromy 为零的部分恰为有理函数行。换言之，任何非有理的有理函数滤波都不能真正删掉 1 的分支；可以提高局部消失阶，不能使完整单值差恒零。这里仅论这个实际函数空间，未论添加新周期函数、覆盖或 CDT 的 Hadamard 系统。尤其减去一个端点值即使变成有理常数，也不能改变 (26a)。

### 5.1 覆盖后重新选择实际行：跨模数与权重的闭合系统

上一障碍确实依赖于所固定的函数空间，不能误扩展到改变输入后的系统。令 \(c(n)\) 为任意非零有理周期序列，周期 \(m\)，并定义

\[
G_j(x)=\sum_{n\ge1}\frac{c(n)x^n}{n^j},\quad 1\le j\le s,\qquad
G_0(x)=\frac{\sum_{a=1}^m c(a)x^a}{1-x^m}.
\tag{26b}
\]

它们满足 \(\theta_xG_j=G_{j-1}\)。这是先取实际覆盖 \(z=x^m\)，再选行

\[
G_j(x)=\sum_{a=1}^m c(a)x^aF_{a,j}(x^m).
\tag{26c}
\]

在 (26c) 中出现的 \(x^a\) 是覆盖后的真实函数系数，不是原来 \(\mathbb Q(z)\) 中的常数滤波。因此 (26a) 不适用于这个新选行。对 \(j>2\)，\(F_{a,j}\) 用 (19) 同一定义；(26b) 仍直接由级数成立。

**跨模数实际秩引理。** 对每个 \(s\ge1\)，\(1,G_1,\ldots,G_s\) 在 \(\mathbb C(x)\) 上独立；\(G_s\) 的 cyclic rank 恰为 \(s+1\)，与周期 \(m\) 无关。

证明：\(G_1'=G_0/x\) 的非零有理函数有至少一个简单极点 \(\xi^m=1\)。因为其分子次数至多 \(m-1\)，不可能消去全部 \(m\) 个简单极点。取非零残数的那个极点，\(\Delta G_1=v\ne0\)。递推 \(\theta_x\Delta G_j=\Delta G_{j-1}\) 使 \(\Delta G_j\) 为 \(\log x\) 的 \(j-1\) 次多项式，最高系数 \(v/(j-1)!\)。对有理函数关系取这个 monodromy 差，按最高 log 次数下降，全部 \(G_j\) 系数只能为零，随后常数也为零。最后 \(\theta_x^sG_s=G_0\ne0\) 给出常数行，并有阶 \(s+1\) 算子 \((\theta_x-\theta_xG_0/G_0)\theta_x^s\)。这是实际函数独立性，不是假设目标周期无理。证毕。

若 \(\sum_ac(a)=0\)，则分子在 1 真正消去分母，\(G_1'\) 在 1 正则；从递推可知所有 \(G_j\) 在 1 正则。因此这是一个真实的局部 monodromy 相消，而非仅提高消失阶。完整残余分支位于未被分子消去的其他单位根，不能顺便删掉。

对模 6 的纯 \(L\) 目标，须同时要求 \(a\cdot c=0\) 与 \(\sum c_r=0\)。其饱和整数核的基可取

\[
e_2-e_4,\quad e_1-5e_2+2e_3+2e_6,\quad
e_2-3e_3+e_4+e_6,\quad5e_2-13e_3+e_5+7e_6.
\tag{26d}
\]

后三项的 \(b\) 坐标为零，第一项为 2。因此这个**同时纯目标且删 1 分支**的格对周期的像恰为 \(\mathbb ZL/4\)，而没有域要求时是 (13) 的 \(\mathbb ZL/8\)。也可由模 2 看出：\(a\cdot c=0\) 给 \(c_3+c_6\equiv0\)，再结合 \(\sum c=0\) 得 \(b\cdot c\equiv0\)；第一项达到 2。完整饱和性可用 §4 的 unimodular 参数化推出：纯目标格中的平均值方程为 \(-3B+4t_1-2t_2-6t_3-26t_4=0\)，故 \(B\) 偶数且四个剩余整数参数自由。

最简单的实际正路径模型是 \(m=3,c=(1,-1,0)\)：

\[
G_0(x)=\frac{x}{1+x+x^2},\quad
G_2(1)=L=\int_0^1\frac{-\log x}{1+x+x^2}\,dx.
\tag{26e}
\]

这一输入的 rank 为 3。清固定权分母后，所有前缀的安全分母为 \(L_N^s\)，实际最小值仍用 (27) 的全部系数 gcd；联合格仍用 (28)–(29)。这里证明的是实际函数 / de Rham 闭合系统与全素数 Taylor 系数模型，不据其 \(s+1\) 维函数秩断言存在同维有理 Betti quotient 或完整坏素数整动机格。原点模 3 的特例额外构造了真实 Betti 整格；其精确 \((L_N/3^{v_3(L_N)})^j\) 及自然行 fine 最优成本 \(25/18\) 见 [独立整数模型报告 §§4–6](period_holonomy_integral_models_20261005.md)。它们证明这个 cover/选行是合法改善输入，而不自动构成新的 CDT 矛盾；还缺数值有理关系产生新正则芽与严格 domain/holonomy 余量的接口。

## 6. 这个函数模型的完整前缀整数格

对单行 \(f=\sum_ac_aF_{a,2}\)，先清固定有理权的分母，使 \(c_a\in\mathbb Z\)。其 \(z^n\) 系数为 \(d_n=\sum_ac_a/(mn+a)^2\)。对前缀 \(0\le n\le N\)，安全整数化取

\[
D_N=\operatorname{lcm}(1,\ldots,m(N+1))^2,
\quad B_n=D_Nd_n\in\mathbb Z.
\]

**精确全部 content 公式**为

\[
\delta_f(N)=\frac{D_N}{\gcd(D_N,B_0,\ldots,B_N)}
=\operatorname{lcm}_{0\le n\le N}\operatorname{den}(d_n).
\tag{27}
\]

证明逐素数比较：清分母所需的最大负赋值恰为 \(v_p(D_N)-\min(v_p(D_N),v_p(B_0),\ldots)\)。这是实际混合后的前缀分母，不能把每个 summand 的 safe LCM 当作已证最小分母。

多个行 \(f_i\) 则不能只各除一次行 gcd。设其前缀系数矩阵为 \(C_N\in\mathbb Q^{r\times(N+1)}\)，共同分母 \(D\)，置 \(B=DC_N\)。全部可积整数滤波格是

\[
\Lambda_N=\{v\in\mathbb Z^r:vB\equiv0\pmod D\}.
\tag{28}
\]

若 \(s=N+1\)，矩阵 \([B^t\mid D I_s]\) 的 Smith 非零因子为 \(d_1,\ldots,d_s\)，则

\[
[\mathbb Z^r:\Lambda_N]=\frac{D^s}{d_1\cdots d_s}.
\tag{29}
\]

这是因为像群为 \((B^t\mathbb Z^r+D\mathbb Z^s)/D\mathbb Z^s\)。要同时消去污染周期，还须与 §4 的饱和纯目标核相交；先独立约掉每一行 content，再取行列式，会漏掉 (28) 的整格关系。

一个完整小例是 \(m=3,N=2\) 的两行 \(F_{1,2},F_{3,2}\)。其各自前缀分母为 784、324，但联合可积滤波格的基为

\[
\binom{784}{0},\qquad\binom{-196}{81},
\quad [\mathbb Z^2:\Lambda_2]=63504=\frac{784\cdot324}{4}.
\tag{29a}
\]

第二个整数滤波的前三系数正好为 \((-187,-10,-3)\)；整格收益来自真实交叉相消，不能从各行 denominator product 自动读出。

## 7. 自然模型连接 CDT 后为何仍不够

这里专论原来的 normalized Lerch 系统 (21)，不将它的账本移植给 §5.1 的覆盖后新选行。系统 (21) 中的常数行无需分母，\(t\) 个第一层行可用 \(\operatorname{lcm}(1,\ldots,mN+O(1))\)，\(t\) 个第二层行可用该 LCM 的平方。固定偏移使用 CDT Remark 6.0.12 的 shifted-denominator 规则；有限常数项可另乘固定整数，不把偏移区间中的大素数当成固定分母。按 CDT 的升序行成本记账，在 \(2t+1\) 维下得到这个**明确可用但未证最优**的 coarse 类型

\[
\tau_{m,t}=\frac{m(7t^2+6t)}{(2t+1)^2}.
\tag{30}
\]

自然公共单值域为 \(\Omega=\mathbb C\setminus[1,\infty)\)。其在 0 的 conformal radius 为 4；任何 \(\varphi:\mathbb D\to\Omega\)、\(\varphi(0)=0\) 由 Schwarz 得 \(|\varphi'(0)|\le4\)。由于 \(m\ge t\ge1\)，

\[
\tau_{m,t}\ge\frac{t(7t^2+6t)}{(2t+1)^2}\ge\frac{13}{9}>\log4.
\tag{31}
\]

第二个不等式等价于 \((t-1)(63t^2+65t+13)\ge0\)。故这个自然粗分母模型不满足 §7.0.1 的严格 conformal-size 前提。没有构造出更细的 staircase、换成真实覆盖上的不同系统或证明额外 domain 相消之前，单靠有限端点纯化不能给新的 holonomy 反证。

这不排除某个实际组合的更细前缀 / fine 类型，也不排除仿 CDT 的不同几何系统。CDT 的已证 \(L\) 结果恰说明原始 Lerch 模型的不足不是数值结论的反证：其反证模型是 §1 的真实 symmetrized 14 维系统，而不是直接给 (19) 附上一个数值关系。

本报告因而给出两个可直接使用的接口：已证三周期基上的所有目标可完全分类；新模数、新角色或椭圆周期则须另构造“数值关系 \(\Rightarrow\) 有理芽 + 实际独立系统 + 完整整数类型 + 严格 domain 余量”的链条。式 (5) 本身只给真实污染坐标，不能把未控 \(L(2,\chi_{-4})\) 等坐标从数值上删去。

## 8. 精确证书与审阅范围

[独立验证脚本](period_holonomy_target_projection_20261005_verify.py) 和 [JSON](period_holonomy_target_projection_20261005_verify.json) 不调用任何 \(\zeta\)、Dirichlet \(L\) 或 trigamma 数值。固定精确证书包含：六残数 SNF 与 unimodular 核；同时 pure-L / mean-zero 的完整饱和核及指数 2；(9) 的有理行身份；完整 primitive 坐标；一个联合前缀同余格；三个标量前缀分母的 complete gcd；rank 5 / 7 的 confluent determinant 与 forcing polynomial；periodic 模型权重 1–3 的循环行列式及字符前缀分母；(1)、(31) 的有理预算；三个素数平移例。

通用证明覆盖全部模数 / 全部尺度；有限证书只核符号实现和选定小例，不承担 CDT 的数值独立性定理。root 已独立审阅 §§2–7，特别是新增 §5.1 的 uniform actual rank、覆盖后新选行、mean-zero 相消及完整饱和核；无必要纠错。paper_mechanism 已独立审阅原 §§5–7 的实际秩、联合整格与 coarse 预算证明，新增 (26a)，以及 §4 的 primitive 缩放说明和 content 界；这些范围全部通过。本轮作者逐项核对 §1 固定 PDF、页码与归档版本，不把其他代理数学审阅扩写为其文献版本审计。旧文件和文献字节均未修改。本轮只使用已归档的两份 CDT PDF，无新增 PDF 下载需求。DLMF 5.15 是新核对的官方网页参考，可由根统一按需归档元数据。以上正文与证书在最终重跑后冻结。
