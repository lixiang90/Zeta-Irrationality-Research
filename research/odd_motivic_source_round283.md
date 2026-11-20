# 第283轮独审　奇权动机、实数关系与公共分母

2026-11-20。取 \(z_i=\zeta(2i+1)\)，\(i\ge1\)。欲证任给 \(i\) 及 \(u/v\in\mathbf Q\)、\(v>0\)，都有 \(z_i\ne u/v\)。对其他权重没有假设。[本轮任务](odd_weight_family_scope_round283.md)

## 已经成立的全权结构

对奇数 \(w\ge3\)，\(K_{2w-1}(\mathbf Z)\otimes\mathbf Q\) 的维数为 1。在 \(\mathrm{MT}(\mathbf Z)\) 中，相应的 \(\operatorname{Ext}^1(\mathbf Q(-w),\mathbf Q(0))\) 也是一维。Dupont 给出了统一的奇 zeta 动机，其周期矩阵首行含 \(1,\zeta(3),\zeta(5),\ldots\)。单个非平凡扩张可取周期矩阵
\[
\begin{pmatrix}1&\zeta(w)\\0&(2\pi i)^w\end{pmatrix}.
\]
Hodge 实现中对应的扩张类位于 \(\mathbf C/(2\pi i)^w\mathbf Q\)。当 \(w\) 是奇数，分母子空间在虚轴上。因此，即使首行右项假设为非零有理数，这个类依然非零。扩张的非平凡性已由现有定理支付，实际数值的无理性还需额外论证。[Borel 原文](https://www.numdam.org/item/ASENS_1974_4_7_2_235_0/) · [Deligne–Goncharov](https://arxiv.org/abs/math/0302267) · [Dupont，式 (5)、(6)、(13)、(14) 和定理 1.3–1.4](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1112/S0010437X17007588/Dupont_Odd_zeta_motive_and_linear_forms_in_odd_zeta_values_cleaned.pdf)

记 \(Z_i=\zeta^{\mathfrak m}(2i+1)\)。Brown 证明 \(Z_i\) 在动机多重 zeta 代数中代数独立，并给出
\(\Delta Z_i=1\otimes Z_i+Z_i^{\mathfrak a}\otimes1\)，其中非零的 \(Z_i^{\mathfrak a}\) 可对应到权 \(2i+1\) 的单字母。周期映射 \(\mathrm{per}(Z_i)=z_i\)。其在整个动机周期环上单射是猜想。若只要求它分别在每个二维空间 \(\mathbf Q1+\mathbf Q Z_i\) 上单射，展开定义就得到原待证命题。把该单射写成假设不产生独立证据。[Brown，引理 3.2、式 (3.6)、(3.9)](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf) · [Brown，周期猜想 3.3–3.5](https://www.imj-prg.fr/wp-content/uploads/2020/prix/brown2014.pdf)

## 一条足够的数值对称性

在动机多项式环 \(\mathbf Q[Z_1,Z_2,\ldots]\) 上，所有 \(Z_i\) 同时取负定义了对合 \(\sigma\)。它来自多重 zeta 通常所用权重的奇偶性。复共轭固定每个实数 \(z_i\)。在数值侧，所需的对合是否存在，可化成以下确切的二次扩域问题。令
\[
F=\mathbf Q(z_1^2,z_1 z_2,z_1 z_3,\ldots),\qquad K=\mathbf Q(z_1,z_2,\ldots).
\]
以下三件事等价。

1. 所有 \(Z_i\) 同时取负保持这个多项式环上 \(\ker(\mathrm{per})\) 稳定。
2. \(K\) 有一个 \(\mathbf Q\)-自同构将每个 \(z_i\) 送到 \(-z_i\)。
3. \(z_1\notin F\)，即 \([K:F]=2\)。

由核稳定可在商环取对合并延拓到分式域。反过来，可从自同构作用于任意数值多项式关系恢复核稳定。每个 \(z_i/z_1=(z_1z_i)/z_1^2\) 都在 \(F\)，所以 \(K=F(z_1)\)，次数至多为 2。次数为 2 时，非恒同共轭把 \(z_1\) 送到 \(-z_1\)，再由上述比值同时作用于全部 \(z_i\)。若第 2 项成立，该自同构固定 \(F\) 而移动 \(z_1\)，即得第 3 项。

三者任一成立就推出所有 \(z_i\) 无理，因为每个 \(z_i>0\)，每个有理数则被自同构固定。此条件只要求关系在同时变号下稳定，能容许非零的多项式关系，如代数模型 \(\mathbf Q(\sqrt2)\) 中的 \(X^2-2=0\)。反方向在一般数域中不成立，如 \(x=\sqrt[3]{2}\) 无理但 \(x=(x^2)^2/2\)。对实 zeta 值，第 3 项仍是待证条件，要求对每个有限子域 \(\mathbf Q(z_1^2,z_1z_2,\ldots,z_1z_m)\) 均能排除 \(z_1\) 属于其中。即使 \(m=1\)，Apéry 的无理性也不足以证明这项不包含关系。

## 文献中的数值量词

Apéry 证明 \(\zeta(3)\) 无理。Fauzan 于 2026-09-17 发表 \(\zeta(5)\) 的预印本，固定权的 Hankel 整数多项式具有负二次净率。上游 Lean 项目证明了同一数值定理，并列出对原清整常数的调整。本次核查读了定理与上游公理说明，沿用仓库已有的固定形式化基线。[Apéry 原文](https://numdam.org/item/AST_1979__61__11_0.pdf) · [Fauzan 原件](https://zenodo.org/records/22826419) · [mo271/Zeta5 的定理与公理](https://github.com/mo271/Zeta5/blob/main/README.md)

截至本轮对实奇值的一手文献核查，最先未获可信单值证明的权重是 7。Anand 的 2026-09-23 版本在 \(y=3/2\) 的外区被积函数，按式 (71)–(73) 为 \(7/20\)，按表 5 为 \(-299/20\)。两者在整段开区间的差异影响净率。[原件的本地存档](zenodo_22920911/Zeta7_Anand_2026.pdf) · [逐段复算](zenodo_22920911/review.md)

2026-11-12 的 Fischler–Lai–Sprang–Zudilin 预印本定理 1.1 记 \(N_s=\#\{3\le w\le s:w\text{ 奇},\ \zeta(w)\notin\mathbf Q\}\)。对每个 \(\epsilon>0\) 和充分大的奇数 \(s\)，
\[
N_s\ \ge\left(\sqrt{4\zeta(2)\zeta(3)/\zeta(6)}-\epsilon\right)
       \sqrt{\frac{s\log\log s}{\log s}}.
\]
括号中的主常数约为 \(2.788258\)。删去任何一个固定权重，仍与这种增长量级相容。本文核查了该文 §1 的量词与反证设计，未对其全部证明或所有近期投稿作新颖性审计。[作者原文，定理 1.1](https://arxiv.org/html/2611.16156v1#S1)

## 公共分母母函数估计的独立复核

取 \(\alpha_h=\zeta(2h+3)\)，\(F_0(z)=\sum_{h\ge0}\alpha_hz^h\)，固定 \(0<r<1\)。记 \(M_r(q)=\inf_A\max_{|z|\le r}|qF_0(z)-A(z)|\)，其中 \(q\) 是正整数，\(A\) 在闭圆盘的邻域全纯，全部 Taylor 系数均为整数。已有生成函数及 WZ 加速恒等式见 Hessami Pilehrood 二人论文。下述估计直接从 Dirichlet 级数给出，文献核查范围仅及所列生成函数，未核其在整系数逼近文献中的首创性。[生成函数原文](https://arxiv.org/abs/0801.1591)

令 \(S\alpha_h=\alpha_{h+1}\)、\(T_K=\prod_{j=1}^K(1-j^2S)\)，\(K\ge1\)。因为 \(\alpha_h=\sum_{k\ge1}k^{-3}(k^{-2})^h\)，\(b_h=T_K\alpha_h\) 中首次保留的原子是 \(k=K+1\)，且各保留项为正。故对 \(\lambda=(K+1)^{-2}\)，
\[
c_K\lambda^h\le b_h\le\zeta(3)\lambda^h,\qquad
c_K=\frac{(2K+1)!}{(K+1)^{2K+4}} .
\]
取 \(h=\lfloor\log q/\log(1/\lambda)\rfloor+2\)。有 \(c_K\lambda^2\le q b_h<\zeta(3)\lambda<1/2\)，后式只用 \(\zeta(3)<2\)、\(\lambda\le1/4\)。若 \(a_h=[z^h]A\)，则 \(T_K a_h\in\mathbf Z\)。对有限差分中的每个系数用 Cauchy 估计，得到
\[
M_r(q)\ge
\frac{c_K\lambda^2 r^2}{\prod_{j=1}^K(1+j^2/r)}
q^{\log r/(2\log(K+1))}.
\]
对任意 \(\epsilon>0\) 先固定足够大的 \(K\)，即得 \(M_r(q)\ge C_{r,\epsilon}q^{-\epsilon}\)。还可选择 \(K=\lfloor\log q/(\log\log q)^3\rfloor\)（\(q\) 充分大）。由阶乘公式 \(\log c_K=-O(K+\log(K+1))\)，算子分母对数为 \(O_r(K\log(K+1))\)。于是
\[
\liminf_{q\to\infty}\frac{\log\log q}{\log q}\log M_r(q)
\ \ge\ \frac{\log r}{2}.
\]
这种一致误差确实可以沿子列趋零。取 \(H\ge1,\ Q=\lceil r^{-H}\rceil\)，将 \(j(\alpha_0,\ldots,\alpha_{H-1})\) 的分数部分（\(0\le j\le Q^H\)）放入 \(Q^H\) 个等立方盒。两个落在同一盒，给出 \(1\le q_H\le Q^H\)，使前 \(H\) 个 \(q_H\alpha_h\) 离某整数至多 \(1/Q\)。其余系数取最近整数，误差至多 \(1/2\)。对每个固定的 \(q_H\)，所得整系数有界，故相应级数在单位开圆盘全纯。于是
\[
M_r(q_H)\ \le\ \frac{Q^{-1}+r^H/2}{1-r}
\ \le\ \frac{3r^H}{2(1-r)}.
\]
每个固定 \(q\) 的 \(M_r(q)>0\)，故 \(q_H\to\infty\)。由 \(\log q_H\le|\log r|H^2+O_r(1)\)，可取无界子列使 \(M_r(q_H)\le C_r\exp(-\sqrt{|\log r|\log q_H})\)。此法只保证各系数逼近整数，无法保证任给的指定系数误差非零。上下界共同约束固定圆盘上的完整整系数序列。各权分别使用分母、只控制有限 Taylor 系数、改变圆盘半径时，须另算对应误差。它们本身不给任何新单值的无理性结论。

## 正积分与短向量候选的独审

固定 \(w\ge3\) 为奇数，沿用[全权矩公式](odd_markov_all_weights_round283.md)中的概率测度 \(\mu_w\) 和 \(\nu_w=\mu_w/(1+x)\)，其总质量 \(\eta(w)\) 小于 1。取 \(P_i=x^d(1-x)^dx^i\)（\(0\le i<d\)）、\(P=\sum_i u_iP_i\)，\(u_i\in\mathbf Z,\ |u_i|\le2^d\)。写
\[
W=\frac{P(x)^2-P(-1)^2}{1+x}\in\mathbf Z[x],\qquad
B=\int W\,d\mu_w=\sum_{k=1}^{6d-2}\frac{[x^{k-1}]W}{k^w},
\qquad I=\int P^2\,d\nu_w=P(-1)^2\eta(w)+B.
\]
因 \(\deg W\le6d-3\)，\(D=\operatorname{lcm}(1,\ldots,6d-2)^w\) 使 \(DB\) 为整数。若 \(u\ne0\)，则 \(0<I\le\eta(w)d^2\,4^{-d}<1\)。若完整同余 \(DB\equiv0\bmod D\) 成立，\(P(-1)=0\) 将使 \(I\) 成为这个开区间中的整数。因此目标系数必非零。对无界的 \(d\) 若能取得这种整解，则 \(\eta(w)\in\mathbf Q\) 的任一固定分母乘 \(I\) 会得到趋零的正整数。

逐项要求 \(k^w\mid[x^{k-1}]W\) 已可对每个 \(d\ge1\) 排除。由 \(x^{2d}\mid P^2\)，当 \(1\le k\le2d\) 时，该系数为 \((-1)^kP(-1)^2\)。所以 \(\operatorname{lcm}(1,\ldots,2d)^{w/2}\le|P(-1)|\le d4^d\)。对 \(n=2d-1\)，整数 \((n+1)\binom nj\) 的每一素数幂阶乘层至多为 1，故都整除 \(\operatorname{lcm}(1,\ldots,n+1)\)。取最大二项系数便有 \(\operatorname{lcm}(1,\ldots,2d)\ge2^{2d-1}\)，已在 \(d\ge4\) 时与上述上界矛盾。\(d=2,3\) 分别用 LCM \(12,60\)。\(d=1\) 时 \(W\) 的三次系数为 \(u_0^2\)，无法被 \(4^w\) 整除。此项排除只涉及逐系数清整。

在实际总和上可以同时消掉一段素数。\(d\ge2\)，固定 \(u_{d-1}=1\)，取 \(5d-1\le p\le6d-2\) 内所有素数。分母底数中只有 \(k=p\) 是 \(p\) 的倍数，故该处整性的充分必要条件为 \(p^w\mid[x^{p-1}]W\)。令 \(W_{ij}=(P_iP_j-P_i(-1)P_j(-1))/(1+x)\)。由最高项可知，若 \(4d+i+j<p\)，则 \([x^{p-1}]W_{ij}=0\)，等号时该系数为 1。按 \(p\) 递减，给它分配坐标 \(j=p-5d+1\)。因 \(6d-2\) 是偶数，\(0\le j\le d-2\)。本步的 \([x^{p-1}]W\) 只依赖于 \(u_j\) 和更高坐标，对 \(u_j\) 的唯一贡献为 \(2u_j u_{d-1}=2u_j\)，故可依次满足全部同余。其余自由坐标取零。在每一步的解类中选一个绝对值不超过 \(p^w\) 的偶代表，可使 \(P(-1)/(-2)^d\) 为奇数，保证只消去该素数段时目标系数也确非零。

所得向量对固定 \(w\) 满足 \(\|u\|_\infty=O_w(d^w)\)，故充分大时符合 \(2^d\) 高度限制，且 \(0<I\ll_w d^{2w+2}16^{-d}\)。同一满次数对象的完整有理项 \(B\) 可用 \(D/\prod_{5d-1\le p\le6d-2}p^w\) 清整。素数定理给此显式分母的对数为 \((5w+o(1))d\)，原满次数通用分母对应 \(6wd+o(d)\)。余下的安全净率 \(5w-\log16\) 为正。作为比较，取较低次数 \(P=[x(1-x)]^d\) 时原始分母已可用 \(\operatorname{lcm}(1,\ldots,4d)^w\)，对数为 \(4wd+o(d)\)。素数带结果证明满次数的同时消元能力，全部短整解的存在性仍待判定。
