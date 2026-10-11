# 第250轮：全负叶椭圆提升、整数背景能量与剩余多叶预算

2026-10-10，B。固定第248–249轮的 Fricke 商坐标 \(t\)、\(K=\mathbb Q(\sqrt2)\) 和真实假设
\[
g=g_+=Y/2+\sqrt2\,\pi^2/28\in K.
\]
本文没有新的数值无理性定理。新结论是：对当前完整安全三行源的 arch-only basic CDT 入口，**正处 univalent、负处任意 multivalent 的组合也被排除**；两处都 multivalent 尚未排除。证明采用实际全负到达叶、重新支付的 \(t\)-坐标提升、整数背景的 rank-2 能量和自含 \(1/8\) Bloch 界，不把旧 \(x\)-坐标结论搬过来。

## 1. 固定源、类型和全负叶输入

置 \(s=\sqrt2\)、\(Q_\pm=1-(7\mp4s)t+t^2\)、\(E=Q_+Q_-\)。两处的实际源分别是
\[
B_{+,g}=A_+(I_+-g),\qquad B_{-,\bar g}=A_-(I_--\bar g).
\]
完整 frame 为 \((1,7bB,7bE\delta B)\)，其中 \(b>0\) 固定且 \(bg\in\mathcal O_K\)、\(\delta=t\partial_t\)。实际 \(K(t)\)-rank 是3；固定清分母不贡献指数率。全文前缀 \(7b d_N^2\) 对应 **\(3\times2\)** 数组，两列均为 \((0,1,1)^T\)，故
\[
\tau=\frac{2(3+5)}9=\frac{16}9.
\tag{B1}
\]
不是把 row-sum \((0,2,2)\) 当成另一种单列数组。

本轮实际 FULL 读取并独立纸核 A250 冻结稿的 A1–A13。以下是所用全量词的数学链。令
\[
\Gamma^*=\Gamma_0(14)\sqcup\Gamma_0(14)W_{14}.
\]
\(\Gamma_0(14)\) 无椭圆元。写 \(\gamma=(a,b;14c,d)\)，则 \(\gamma W\) 的 determinant 为14、trace 为 \(14(b-c)\)。椭圆要求 \(|\mathrm{tr}|<2\sqrt{14}\)，所以全部 order-2 返回均为
\[
r=(14b,-a;14d,-14b),\quad ad-14b^2=1,\quad r^2=-14I.
\tag{B2}
\]
可选 \(d>0\)，且 \(d\) 奇、\(7\nmid d\)、\((b,d)=1\)。ordinary locus 的 regular cover 中，每一到达叶由 \(N\in\Gamma^*\) 运输；其局部返回为 \(NrN^{-1}\)，仍在上述全部参数族内。这里用的是已付 regular cover，不声称它是去掉椭圆点前的普通 universal cover，也不需要先给一个有限 generator 清单。

A250 的完整 affine cocycle 和权1 gauge 给出：任一实际叶在任一有限 \(E\)-根补支，当且仅当该叶的常数等于相应返回常数。返回常数的实部为
\[
\Re g_{r,\epsilon}=Y/2+\epsilon(2s/7)\pi^2D_{b,d},
\quad
D_{b,d}=\frac18-\frac{M_{b,d}}{2d},\quad M_{b,d}\in\tfrac17\mathbb Z.
\tag{B3}
\]
\(D\) 的公式来自完整 dyadic Bernoulli 和，并保留有符号的周期系数；不借正性。其分母结论由 \(\mathbb Q[z]/(z^d-1)\) 中乘法 \(S_7(z)=1+\cdots+z^6\) 的 determinant 恰为7支付。因为 \(d\) 奇，
\[
D_{b,d}=-\tfrac18\Longrightarrow M_{b,d}=d/2,
\]
与 \(7M\in\mathbb Z\) 矛盾。

若负处某一到达叶补支，实际 \(\bar g\) 为实数先迫该返回常数的虚部为0；于是
\[
g-\bar g=\frac{s\pi^2}{28}(1+8D_{b,d}).
\tag{B4}
\]
左边代数，右边为非零代数数乘 \(\pi^2\)，矛盾。此反证不需要假设未知 \(Y\) 的 Galois 行为，也不需要另证 \(\Im R\) 是代数倍 \(\pi^2\)。因此负处 **四个 \(E\)-根的每一个 transported 到达叶** 都保留非零平方根项。正处只知道准确填点条件 \(q_{b,d}=0,D_{b,d}=1/8\)；不领取所有正叶坏或另一个正处遗漏点。

## 2. 任意负处合法图的实际椭圆提升

设 \(\phi_-:(\mathbb D,0)\to(\mathbb C,0)\)、\(\phi'_-(0)\ne0\)，完整负处源共同拉回 single-valued meromorphic。有限 \(E\)-点的 \(B\) 在 modular uniformizer 中全纯，无负幂；非零平方根项与 (B4) 使每个 \(E(\phi_-)\) 零点的 multiplicity 都必须为偶数。否则有限阶拉回仍有半整数幂，不能 meromorphic。零点是离散的，\(\mathbb D\) 单连通，故存在唯一满足 \(y_\phi(0)=1\) 的 holomorphic square root：
\[
y_\phi^2=E(\phi_-),\qquad
\psi=(\phi_-,y_\phi):\mathbb D\longrightarrow X,\quad X:y^2=E(t).
\tag{B5}
\]
因为 \(\phi_-\) 有限，\(\psi\) 避开 \(t\) 的两个 infinity 点。不能只从某个坏叶的存在推出 (B5)；所用的是 §1 已付的全部到达叶量词。

在 \(X\) 上 \(\omega=dt/y\) 是全纯非零微分，native \(\omega=dq+\cdots\)、\(t=q+\cdots\)。分支点处若 \(\phi_--e=w^{2k}\cdot\mathrm{unit}\)，则 \(\phi'_-/y_\phi\) 的 order 为 \(k-1\ge0\)。因此 Abel lift \(z:\mathbb D\to\mathbb C\) 满足
\[
z'(0)=\phi'_-(0).
\tag{B6}
\]
已付第248轮的 exact quartic、微分 normalization 和两条真实 closed cycles给出 \(X=\mathbb C/\Lambda\)，并有
\[
R_\Lambda^2\le \frac{a^2+b^2}{4}<\frac{1590}{611}<\frac{25}9.
\tag{B7}
\]
这里只需该显式 sublattice；不要求两周期是 primitive basis。因为 \(\psi\) 避开 \(t=\infty\)，\(z(\mathbb D)\) 避开相应的整个 \(\Lambda\)-coset。第248轮的旧 \(x=u/(1+7u)\) derivative bound 不是本节输入；本节重新核了 \(t\) 的 pole fiber 和 (B6)。

## 3. 自含的 \(1/8\) Bloch–lattice 界

令 \(Z:\mathbb D\to\mathbb C\) holomorphic，且其 image 避开 covering radius 为 \(R\) 的一个 lattice coset。固定 \(0<r<1\)，在 \(|\zeta|\le r\) 取
\[
M=\max (r-|\zeta|)|Z'(\zeta)|=(r-|\zeta_0|)|Z'(\zeta_0)|,\quad
d=r-|\zeta_0|,\quad h(w)=Z(\zeta_0+dw)-Z(\zeta_0).
\]
若 \(Z'(0)\ne0\)，则 \(M>0\)、\(\alpha=h'(0)\)、\(|\alpha|=M\ge r|Z'(0)|\)。maximality 给
\[
|h'(w)|\le M/(1-|w|).
\]
于是 \(F(v)=h'(v/2)/(2\alpha)\) 在 \(\mathbb D\) 映入单位盘，\(F(0)=1/2\)。Schwarz–Pick 的精确差值估计给
\[
|h'(w)-\alpha|\le \frac{3M|w|}{1-|w|},\qquad |w|<1/2.
\]
在 \(|w|=1/4\) 沿径积分得到
\[
|h(w)-\alpha w|\le 3M\left(\log(4/3)-\frac14\right).
\]
Rouché 因而使 \(h(\mathbb D)\) 包含以0为中心、radius \(c_0M\) 的开圆盘，其中
\[
c_0=1-3\log(4/3)>\tfrac18.
\tag{B8}
\]
最后一个严格号自含：\(\log(4/3)<\int_0^{1/3}(1-x+x^2)\,dx=47/162<7/24\)。任何 radius \(>R\) 的圆盘含被遗漏 coset 的一点，所以 \(c_0M\le R\)。令 \(r\uparrow1\)：
\[
|Z'(0)|\le R/c_0<8R.
\]
联 (B6)–(B7)，当前负处任意 multivalent 合法图均满足
\[
\boxed{c_-:=|\phi'_-(0)|<40/3.}
\tag{B9}
\]
此证明只用了 open disc 内的 holomorphic 图；没有把 Koebe 内圆盘结论用于 multivalent \(\phi\)。

## 4. 真正的整数背景行与同一图能量

本源的 \(y(t)\) 是 \(\mathbb Z[[t]]\) 芽。这由实际 eta 乘积完整证明：
\[
t(q)=q\prod_{j\ge1}\left(\frac{1+q^{7j}}{1+q^j}\right)^4\in q\mathbb Z[[q]],
\quad
f_{14}(q)/q=\prod_{j\ge1}(1-q^j)(1-q^{2j})(1-q^{7j})(1-q^{14j})
\in1+q\mathbb Z[[q]].
\]
\((\Theta t)/f_{14}\in1+q\mathbb Z[[q]]\)，而 \(q(t)\in t\mathbb Z[[t]]\) 由 leading coefficient1逐项递推得到。因此
\[
y(t)=\frac{\Theta t(q(t))}{f_{14}(q(t))}\in\mathbb Z[[t]],\quad y^2=E.
\tag{B10}
\]
\(E\) 有四个不同 simple roots，故不是 \(\mathbb Q(t)\) 的平方；\((1,y)\) 的实际 \(\mathbb Q(t)\)-rank 为2。§2使 \(y\circ\phi_-\) holomorphic。对 **这个同一负处图** 以零 denominator array 应用 CDT Theorem2.5.1，若 \(\lambda_-=\log c_->0\) 得
\[
J_-\ge2\lambda_-.
\tag{B11}
\]
若 \(\lambda_-\le0\)，Jensen 给 \(J_-\ge\lambda_-\ge2\lambda_-\)，所以 (B11) 总成立。\(J\) 是原文同一 Bost–Charles double integral；使用其通常径向边界解释，\(J=+\infty\) 不能提供严格入口。这不是把 \(y\) 当作原三行中可免费恢复的一行，而是另一个合法整数背景对同一图的必要能量界。

正处仍仅用 \(J_+\ge\lambda_+\)。不对正处套 (B11)：其填叶可能不迫完整 \(E\) 的偶分歧；单个 \(\sqrt{Q_+}\) 首个 Taylor coefficient 为 \(-7/2+2s\)，也不是免费整数背景。

## 5. 严格数域预算的真实变化

在当前 (B1) 的数域 arch-only 入口，rank 仍为 \(K\)-rank3，两个实嵌入采用
\[
\bar\lambda=(\lambda_++\lambda_-)/2,\qquad \bar J=(J_++J_-)/2.
\]
希望获得 rank3 矛盾所需严格目标是
\[
\bar J<3(\bar\lambda-16/9).
\tag{B12}
\]
这是当前已付 safe array 的准入比较，不是所有整模型或 all-place 判据的必要下界。把 (B11) 和正处 Jensen 代入 (B12)，得新的必要条件
\[
\boxed{\lambda_++\lambda_-/2>16/3,\quad
c_+\sqrt{c_-}>e^{16/3}.}
\tag{B13}
\]
因为 \(40/3<e^{8/3}\)，(B9) 给 \(\lambda_-<8/3\)，所以
\[
\boxed{\lambda_+>4,\quad c_+>e^4,\quad
\delta_+:=3\lambda_+-J_+>32/3-\lambda_->8.}
\tag{B14}
\]
这里 \(e^{8/3}>40/3\) 无数值程序：\(e>8/3\)、\(e^{2/3}>17/9\)，故 \(e^{8/3}>1088/81>40/3\)。\(\delta_+>8\) 和 \(\lambda_+>4\) 都只是必要条件，不认证存在合格图。

若正处图 univalent，第249轮已付的有限奇点和**全部 infinity 叶**非零 log²给 \(c_+\le4/r\)，其中
\[
r=(7+4s-\sqrt{77+56s})/2.
\]
从 \(r^{-1}<7+4s\)、\(s<23/16\)，有 \(c_+<51\)。而 \(e>65/24>27/10\)，所以 \(e^4>(27/10)^4>51\)。这与 (B14) 矛盾。故
\[
\boxed{\text{当前安全基本入口：正 univalent + 负任意 multivalent 均不可行。}}
\tag{B15}
\]
这是比第249轮“两处均 univalent”更强的已付范围。没有继承其 \(c_+c_-\le16\) 到一般 multivalent 情形。

## 6. 部分 genus-0 条件没有免费容量界；唯一剩关

仅知道正处 \(Q_+\circ\phi\) 有 holomorphic square root，不足以限制 derivative。可自含给反例。令
\[
\alpha=(7-4s)/2\in(0,1),\quad \beta=\sqrt{1-\alpha^2}>0,\quad
w_0=\operatorname{arsinh}(\alpha/\beta)+i\pi/2.
\]
对任意 \(M>0\)，
\[
\phi_M(z)=\alpha+i\beta\cosh(w_0+Mz),\qquad
y_M(z)=-i\beta\sinh(w_0+Mz)
\tag{B16}
\]
均 entire，且 \(\phi_M(0)=0,\phi'_M(0)=-M,y_M(0)=1\)、
\(y_M^2=Q_+(\phi_M)\)。这只否定“部分 double-cover 条件自动给 cap”的推论；它们未被认证为实际 \(B_{+,g}\) 的合法图。其它 branchpoints、cusp0 和全部 affine period 返回仍须支付。

因此本轮保留的是**两处均 multivalent 的唯一正处门槛**：在全部 transported 填点条件 \(q_{b,d}=0,D_{b,d}=1/8\) 下，认证一个真正合法的共同正处图，并证明其同源 \(\delta_+>8\) 及与负处实际图组合的 (B12)。或者证明该准入目标结构性不可达。不能靠大的裸 derivative、部分代数覆盖或“存在坏叶”代替此证书。

本轮全负参数化、实际提升及新增整数背景已经实质改变 strict 比较，足以支持由 Root 明确决定的**单个 bounded 第251轮正处填叶/能量关**；不支持延长 finite-prime 前线。第252轮正式复盘不重置。额外 finite-place charts、更优 integral array、其它源及其它几何判据未被排除。数学程序/扫描/Lean/CAS0、新 GET0、外 Git mutation0；作者保存后实际 FULL 复读及来源读域另记。
