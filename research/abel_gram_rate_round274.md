# 第274轮：实际 Abel Gram 的全尺度有限下界及剩余外积缺口

2026-10-20，子代理 `abel_gram_274`。开始时 goal 工具为 null，工作树干净，实际读取 STATE、长期 goal、AGENTS、274任务、273差商主稿及独审、272两份 Gram/Hermite 稿、271 B1–B7。固定原 \(Y=4\beta(5)-3\beta(4)\)、\(n=2m-1\)、全部实际有理反证和唯一 \(p_i,M_m,B_m,Q_m\)。只写本稿，不改账及旧证据；没有数学扫描、CAS、参数变化或数值程序。

**结论：可证裸实际 \(Q_m(Y)\) 的全尺度有限二次下界，但本稿没有证得其二次 liminf 非负，也没有严格负的实际 upper。** 下界是

\[
\boxed{\liminf_{m\to\infty}m^{-2}\log|Q_m(Y)|
\ge-16-10\log2.}
\tag{R1}
\]

这里使用标准 \(\log d_N=N+o(N)\)；下文 R12 是不依赖素数渐近的有限 m 证书。R1 允许严格负率子列，不能据此关闭最优本原预算，也不提供续期理由。它未包含安全矩阵清整 \(\widehat S_m\)；不是把272的安全族增长 lower 改名成裸 Q lower。

## 1. 原权与 sech 权只差次二次费用

沿272 G1，写

\[
U_m(y)=\frac{\prod_{r=1}^{m-1}(y^2+r^2)}
{\prod_{r=0}^{m-1}(y^2+(r+1/2)^2)}.
\]

Gamma 的递推式及
\(|\Gamma(1+iy)|^2=\pi y/\sinh\pi y\)、
\(|\Gamma(1/2+iy)|^2=\pi/\cosh\pi y\) 给精确恒等式

\[
U_m(y)=\left|\frac{\Gamma(m+iy)}{\Gamma(m+1/2+iy)}\right|^2
\frac{\tanh\pi y}{y}.
\tag{R2}
\]

零点按连续延拓。故同一个实际全轴密度恰为

\[
\boxed{\omega_m(y)=\frac{\pi^2}{2}
\left|\frac{\Gamma(m+iy)}{\Gamma(m+1/2+iy)}\right|^6
\{\operatorname{sech}(\pi y)+\operatorname{sech}^3(\pi y)\}.}
\tag{R3}
\]

没有改变积分域的二倍因子。R2 中 Gamma 是书写原有限乘积的一种方式；所需统一界可由 Euler 积直接验证。置

\[
A_m(y)=\left|\frac{\Gamma(m+iy)}{\Gamma(m+1/2+iy)}\right|^2
=\lim_{N\to\infty}\frac1N
\prod_{r=m}^{N-1}\frac{(r+1/2)^2+y^2}{r^2+y^2}.
\]

令 \(f(t)=2t/(t^2+y^2)\)。其在 \([m,\infty)\) 上的总变差至多 \(4/m\)：若 \(|y|\le m\) 它单调下降；否则先增后减且最大值 \(1/|y|\le1/m\)。逐个单位区间比较前半积分与总积分的一半，可得

\[
\left|\sum_{r=m}^{N-1}\int_r^{r+1/2}f(t)dt
-\frac12\int_m^Nf(t)dt\right|
\le\frac12\int_m^N|f'(t)|dt\le\frac2m.
\]

让 N 趋于无穷，因此

\[
e^{-2/m}(m^2+y^2)^{-1/2}\le A_m(y)
\le e^{2/m}(m^2+y^2)^{-1/2}.
\tag{R4}
\]

对 \(t\ge0\)，\((1+t^2)^{3/2}\le(1+t)^3<4e^t\)；又
\(e^{-t}\operatorname{sech}(\pi mt)\ge\tfrac12\operatorname{sech}((\pi m+1)t)\)。由 R3–R4，取固定

\[
c_0=\frac{\pi^2e^{-6}}{16}>0,\qquad a_m=\pi+1/m,
\]

即得到原权的全实轴下界

\[
\boxed{\omega_m(y)\ge c_0m^{-3}\operatorname{sech}(a_my)
\quad(m\ge1,\ y\in\mathbf R).}
\tag{R5}
\]

这一比较的全部损失在 m 阶行列式上是 \(O(m\log m)\)，不会改变二次主率。

## 2. 原反射整数值格的精确三角基

272 H11 已付

\[
C_mp_i((q+1/2)^2)\in\operatorname{Int}(\mathbf Z),
\qquad C_m=8d_{4m-3}^{\,2}.
\tag{R6}
\]

定义同一 w 坐标中的多项式

\[
\chi_d(w)=\frac1{(2d)!}\prod_{r=0}^{d-1}
\{w-(r+1/2)^2\},\qquad \chi_0=1.
\tag{R7}
\]

直接分解得 \(\chi_d((q+1/2)^2)=\binom{q+d}{2d}\)，故在全部整数 q 取整数；在 \(q=0,\ldots,d-1\) 为零，在 \(q=d\) 为1。对任何满足相同整数值条件的次数至多 K 的 w 多项式，按 q=0,1,…,K 的值递归消去，得到唯一的整数 \(\chi_d\) 系数。因此原多项式精确具有

\[
C_mp_i(w)=\sum_{d=0}^{3m-1}c_{i,d}\chi_d(w),
\qquad c_{i,d}\in\mathbf Z.
\tag{R8}
\]

这是原唯一 \(p_i\) 的坐标表达；没有改成别的 source。矩阵 \((c_{i,d})\) 行秩为 m。选递增下标表示的字典序最高非零 m 阶 minor，记 \(I=(d_1<\cdots<d_m)\)。其行列式是非零整数，绝对值至少1。

## 3. sech 的偶阶首一正交范数与裸实际下界

对权 \(\operatorname{sech}(\pi y)dy\)，可用生成函数

\[
G(t,y)=(1-it)^{-1/2+iy}(1+it)^{-1/2-iy}
=\sum_{j\ge0}P_j(y)t^j.
\]

在原点附近实 t,s，有
\(G(t,y)=(1+t^2)^{-1/2}e^{2y\arctan t}\)。由 Euler beta 积分
\(\int_{\mathbf R}e^{uy}\operatorname{sech}(\pi y)dy=1/\cos(u/2)\)，从而

\[
\int_{\mathbf R}G(t,y)G(s,y)\operatorname{sech}(\pi y)dy
=\frac1{1-ts}.
\]

逐系数即 \(\int P_jP_k\operatorname{sech}(\pi y)dy=\delta_{jk}\)。其最高系数为 \(2^j/j!\)，且 \(P_j(-y)=(-1)^jP_j(y)\)。所以以 \(w=-y^2\) 表示的次数 d 首一偶正交多项式，其精确范数为

\[
h_d=\frac{((2d)!)^2}{16^d}.
\tag{R9}
\]

缩放到 \(\operatorname{sech}(a_my)dy\)，令
\(s_m=a_m/\pi=1+1/(\pi m)\)，则

\[
h_{d,m}=s_m^{-(4d+1)}\frac{((2d)!)^2}{16^d}.
\tag{R10}
\]

从 R8 换到这组首一正交多项式，转换是按次数的三角矩阵，对角线为 \(1/(2d)!\)。由 I 的最高非零性，Cauchy–Binet 中所有其它可能贡献的 index 都逐项不小于 I；较高者的原 minor 为零。因此新系数矩阵在 I 的 minor 绝对值至少
\(C_m^{-m}\prod_{d\in I}(2d)!^{-1}\)。对正 Gram 的 Cauchy–Binet 再应用一次，并由 R5 作二次型比较，得到实际原矩阵

\[
\det M_m\ge(c_0m^{-3})^m C_m^{-2m}s_m^{-m}
(16s_m^4)^{-\sum_{d\in I}d}.
\tag{R11}
\]

全部 d 在 \(0,\ldots,3m-1\) 中互异，故总和至多 \((5m^2-m)/2\)。另外271 B1给 \(a_{3,k}\le1\)，所以 \(|\det B_m|\le192^m\)。于是有全 m 的裸实际有限证书

\[
\boxed{|Q_m(Y)|\ge
\left(\frac{c_0}{192m^3C_m^2s_m}\right)^m
(16s_m^4)^{-(5m^2-m)/2}.}
\tag{R12}
\]

这里已经除以实际 \(|\det B_m|\)，没有安全清整倍率。采用标准 \(\log d_N=N+o(N)\)，有
\(\log C_m=8m+o(m)\)、\(\log s_m=O(1/m)\)，R12 即给 R1。此下界的常数仍严格负，不能排除所需严格负二次子列。

## 4. 最高 m 个系数的正率出口尚缺什么

沿272 H1–H3，置 \(V_m=\prod_{i<j}|w_j-w_i|\)，并用原
\(u_i=\alpha_i-3d_i\)、
\(v_i=\gamma_i/2-3d_i\alpha_i+(9d_i^2+3e_i)/2\)。从原显式公式直接得

\[
p_i(w)=\frac{D(w)^3}{D'(w_i)^3}
\left\{\frac{v_i}{w-w_i}+
\frac{u_i}{(w-w_i)^2}+\frac1{(w-w_i)^3}\right\}.
\tag{R13}
\]

最高 m 个 w 系数（次数 \(2m,\ldots,3m-1\)）的 minor 绝对值恰为

\[
V_m^{-6}\left|\det_{i,\,0\le k<m}
\left(v_iw_i^k+ku_iw_i^{k-1}
+\tfrac12k(k-1)w_i^{k-2}\right)\right|.
\tag{R14}
\]

负次数项在其前面的 k 因子为零时按零解释。若这个内行列式有
\(V_m\exp(-o(m^2))\) 的全尺度 lower，则 R5、R9–R10、
\(V_m=\prod_{j=0}^{m-1}(2j)!\) 和 Stirling 将给

\[
\liminf m^{-2}\log|Q_m(Y)|\ge18\log(3/2)>0.
\tag{R15：仅条件结论}
\]

R15 的假设尚未支付。可将该假设准确写成一个 m 阶矩阵问题：令 K 为次数小于 m 的插值微分矩阵在 \(D'(w_i)\) 共轭下的形式，

\[
K_{ii}=d_i,\qquad K_{ij}=\frac1{w_i-w_j}\ (i\ne j).
\]

则 R14 内行列式除以带符号 Vandermonde 等于

\[
\det\{\operatorname{diag}(v_i)
+\operatorname{diag}(u_i)K+\tfrac12K^2\}.
\tag{R16}
\]

例如给这个实际矩阵的对称部分一个 \(m^{-O(1)}I\) 下界将足够；本稿未证明该性质。m=1的最高 block 本身退化，不能把“每行非零”或一个样本的非零直接延伸到全尺度外积。R13–R16 只是将准确缺口定位到实际矩阵，没有把缺口改成已审定理。

本分工所得无条件新结论是 R5、R9–R12，作用是把实际裸评价下界也付到有限二次常数。它没有改变274的通过门槛；负本原净率、全 m 非负裸率及其独审仍未完成，窗口是否结束由根按既定一轮停止条件结算。

## 5. 根结算与下一宏观任务的实际复核范围

随后按根指定，实际完整读过 [274结算](abel_primitive_budget_round274.md) 和 [275宏观任务](source_gate_charter_round275_20261020.md) 两稿。复核了同一对象及全部实际有理反证、274.2由 \(s_m-K_m=30m+O(\log m)\) 和整多项式缩放推出内容信用的代数、274.3常数扣除、274.4–274.5与本稿一致性，以及 m=2 的有理上下界仅限单尺度。全序列负 lower 没有被误用为排除全部负子列；最高 block 仍标条件未付；一轮到期关闭、预算改善使停滞计数为0、275由到期主动触发宏观比较的决定相互一致，未发现需修正处。

此项复核只读上述两稿，没有重审新内容证书 C3–C14 的全文，没有执行 producer 或新数学扫描，也没有把这次结算代数核查登记成该内容证书的独立全文审查。没有另开数学窗口或另写文件。
