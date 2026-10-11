# 真实 paired 辅助素数矩阵：反射商、CRT 与带 middle 的 Padé normality

日期：2026-10-06。NEW 独立研究稿；所有既有冻结稿、旧及同行 producer 均只读。本稿的全尺度恒等式是纸面证明。自有 NEW 有限探针仅首次执行一次，范围见 §10；它不证明无穷 unit 条件。

## 1. 问题与本轮结论的准确范围

冻结输入是 `research/cdt_odd_paired_head_free_auxiliary_prime_20261006.md`，SHA256 `4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b`，本轮实际全文读取。沿用其真实 half jet、A30/A31 middle correction 和饱和 paired 空间。本文不更换成 restored-zero family。

设

\[
m=2r,\quad n=4r,\quad p=18r+1\text{ 为素数},\quad a=5r.
\tag{U1}
\]

原辅助条件 (p=9m+1>2) 强制 (m) 偶数，所以 U1 覆盖该条件下全部尺度。在 \(\mathbf F_p\) 内证明如下结果：

1. 真正 (G_0,M_5) 精确等于平方节点上的矩矩阵，所有 middle multiplicity 与 half-jet cross weight 保留。
2. 节点多项式 \(P\) 与 head 多项式 \(S\) 满足 \(PS=u^{9r+1}-u\)。由此得到显式 CRT projector、Stieltjes 分子及矩分子的逆。
3. \(\det G_0\) 和 \(\det M_5\) 精确等于指定高阶余式映射的行列式；无穷 unit 缺口被转成明确的 scalar 与 matrix Padé normality。
4. middle 在 \(G_0\) 上满秩，真实权重的全局 pointwise Pearson 最小 class 为 7（\(r\ge2\)）；端点和跳变不是可免费删除的修正。

没有证明全部或无穷多个 U1 素数上的 normality，没有取得新的全素数费用改善，也没有推出任何新的无理性结论。CRT 的环境可逆性与截断 Padé 可逆性须严格区分。

## 2. 精确反射商与 Wilson 权重

原变量 \(t\) 的反射中心为 \((4m+1)/2\equiv-5r\pmod p\)。令 \(y=t+5r\)。负节点 \(t=-\ell,0\le\ell<3m\) 变成

\[
y=-r+1,-r+2,\ldots,5r.
\tag{U2}
\]

原 head 多项式变为

\[
S_y(y)=\prod_{j=5r+1}^{9r}(y^2-j^2)=S(u),\qquad u=y^2,\quad\deg S=4r.
\tag{U3}
\]

证明：原 head 根 \(t=1,\ldots,8r\) 对应 \(y=5r+1,\ldots,13r\)。其中 \(9r+1,\ldots,13r\) 模 \(p\) 正好是 \(-(9r),\ldots,-(5r+1)\)。首一多项式因此正好为 U3，没有额外 scalar。

反射偶的 \(T\) 和 \(Q\) 分别写为 \(T(u),Q(u)\)，且

\[
\deg T<r,\qquad\deg Q<3r.
\tag{U4}
\]

平方节点 \(u_k=k^2\), \(0\le k\le5r\), 互异：若 \(k^2=l^2\)，则 \(k=l\) 或 \(k+l=p\)；后者不可能，因为 \(k+l\le10r<p\)。折叠 U2 后定义

\[
\mu_0=1,\quad\mu_k=2\ (1\le k<r),\quad\mu_k=1\ (r\le k\le5r),
\]
\[
\gamma_0=2,\quad\gamma_k=4\ (1\le k<r),\quad\gamma_k=5\ (r\le k\le5r).
\tag{U5}
\]

于是冻结稿的真实形式是

\[
G_0(T,T')=\sum_{k=0}^{5r}\mu_k\frac{T(u_k)T'(u_k)}{S(u_k)^5},
\]
\[
H_0(Q,Q')=\sum_{k=0}^{5r}\mu_k S(u_k)^3Q(u_k)Q'(u_k),
\]
\[
C_5(T,Q)=\sum_{k=0}^{5r}\gamma_k\frac{T(u_k)Q(u_k)}{S(u_k)},
\qquad M_5=\begin{pmatrix}G_0&C_5\\ C_5^{\mathsf T}&H_0\end{pmatrix},
\tag{U6}
\]

其中矩阵次序是先 \(T=1,u,\ldots,u^{r-1}\)，后 \(Q=1,u,\ldots,u^{3r-1}\)。若将 cross 写为行 \(Q\)、列 \(T\)，则 U6 的右上块取其转置；本稿行列式不受该记号变化影响。middle 节点的 cross 係数 \(2\) 来源于真实 \(s-(s+1)\eta=5-6/2=2\)，不是可另选的 half jet。

对于 \(-5r\le k\le5r\)，普通整数阶乘再模 \(p\) 给出

\[
S_y(k)=\frac{(9r-k)!(9r+k)!}{(5r-k)!(5r+k)!}
=\frac{(-1)^{r+k+1}}{(5r-k)!(5r+k)!}\quad(\mathbf F_p).
\tag{U7}
\]

第一等式由逐项积得出；第二等式用 \(p-1=18r\) 和 Wilson 恒等式。所用阶乘指标均在 \([0,p-1]\)，所以全部是 unit。对内部相邻节点有

\[
\frac{S_y(k+1)^{-5}}{S_y(k)^{-5}}
=-\left(\frac{5r+k+1}{5r-k}\right)^5.
\tag{U8}
\]

U8 只是内部比值，不能把零延拓的端点边界项自动删除。

## 3. Full 与 middle：真实修正的秩

设 \(\nu_0=1\), \(\nu_k=2\) 对 \(k>0\)，并令 \(\chi_k=1\) 对 \(k<r\)，否则为零。对 \(j=-5,-1,3\) 定义

\[
F_j(f)=\sum_{y=-5r}^{5r}f(y^2)S_y(y)^j
=\sum_{k=0}^{5r}\nu_k f(u_k)S(u_k)^j,
\]
\[
I_j(f)=\sum_{|y|<r}f(y^2)S_y(y)^j
=\sum_{k=0}^{r-1}\nu_k f(u_k)S(u_k)^j.
\tag{U9}
\]

逐节点核对 U5，得到保留冻结 A30/A31 的精确式

\[
G_0=\tfrac12(F_{-5}+I_{-5}),\quad
C_5=\tfrac12(5F_{-1}-I_{-1}),\quad
H_0=\tfrac12(F_3+I_3).
\tag{U10}
\]

**Lemma U11（middle 满秩）。** \(I_{-5}\) 在 \(\mathbf F_p[u]_{<r}\) 上非退化；它的秩等于 \(r\)。

证明：评价矩阵 \(V=(u_k^i)_{0\le k,i<r}\) 为可逆 Vandermonde，而权重 \(\nu_k S(u_k)^{-5}\) 全部非零。因此 Gram 矩阵 \(V^{\mathsf T}\operatorname{diag}(\nu_k S(u_k)^{-5})V\) 行列式为非零的权重积乘 Vandermonde 平方。这不是随尺度保持有界秩的扰动。

令 \(E=T+S^4Q\)、\(D=T-S^4Q\)，在节点上解释乘积；不改变 U4 的空间。真实联合形式精确分解为

\[
M_5((T,Q),(T',Q'))
=\tfrac12\{3F_{-5}(EE')-2F_{-5}(DD')+I_{-5}(DD')\}.
\tag{U12}
\]

证明：展开 \(3EE'-2DD'\) 得 \(TT'+5S^4(TQ'+QT')+S^8QQ'\)；\(DD'\) 给出 middle 的负 cross。U12 的 middle 部分秩也等于 \(r\)：映射 \((T,Q)\mapsto (T-S^4Q)(u_k)_{k<r}\) 已由 \(Q=0\) 时的 \(T\) 评价满射。故不能以 full 矩阵的乘积公式代替真实矩阵，再把 middle 视作无费用误差。

## 4. 节点多项式的 Fermat 因式与 CRT projector

定义

\[
P(u)=u\prod_{k=1}^{5r}(u-k^2),\quad N=\deg P=5r+1;
\quad M(u)=\prod_{k=0}^{r-1}(u-k^2),\quad O=P/M.
\tag{U13}
\]

**Lemma U14（全尺度 exact factorization）。**

\[
\boxed{P(u)S(u)=u^{9r+1}-u.}
\tag{U14}
\]

证明：\(1^2,\ldots,(9r)^2\) 是 \(\mathbf F_p^\times\) 的全部不同平方元，共 \((p-1)/2=9r\) 个，正好是 \(u^{9r}-1\) 的根。乘上 \(u\) 后，U13 与 U3 把根完整分割，首一性给出等式。因此 \(P,S\) 均 squarefree 且互素。

在节点上微分 U14 得

\[
P'(u_k)S(u_k)=-1/\nu_k.
\tag{U15}
\]

对 \(k=0\)，右侧是 \(-1\)。对 \(k>0\)，\(u_k^{9r}=1\)，左側等于 \(9r+1-1=9r\equiv-1/2\pmod p\)。

令 \(\chi(u)\) 是唯一的 degree \(<N\) 多项式，满足

\[
\chi\equiv1\pmod M,\quad\chi\equiv0\pmod O;
\qquad \chi=\operatorname{rem}_P\bigl(O\,(O^{-1}\bmod M)\bigr).
\tag{U16}
\]

于是 \(\chi(u_k)=\chi_k\), \(\chi^2\equiv\chi\pmod P\)。这给出保留全部 middle 节点的精确 CRT projector。下文 \(S^{-j}\) 只表示 \(\mathbf F_p[u]/P\) 中的 inverse power；所有余式均取唯一 degree \(<N\) 的代表。

## 5. Stieltjes 分子及环境矩阵的显式逆

对任意权重 \(w_k\)，函数

\[
\sum_k\frac{w_k}{z-u_k}=\frac{q(z)}{P(z)},\quad\deg q<N
\tag{U17}
\]

的分子由 \(q(u_k)=w_kP'(u_k)\) 唯一决定。应用 U15 到 U9，\(F_j\) 的分子是 \(-S^{j-1}\bmod P\)，\(I_j\) 的分子是前者乘 \(\chi\)。因此真正三个矩序列的分子为

\[
g=-\tfrac12(1+\chi)S^{-6},\quad
c=-\tfrac12(5-\chi)S^{-2},\quad
h=-\tfrac12(1+\chi)S^2\qquad(\bmod P).
\tag{U18}
\]

特别 \(g\) 是 unit，且

\[
g^{-1}=-(2-\chi)S^6\quad(\bmod P).
\tag{U19}
\]

**Lemma U20（真正 matrix numerator 的全尺度可逆性）。**

\[
\mathcal N=\begin{pmatrix}g&c\\c&h\end{pmatrix},\qquad
\boxed{\det\mathcal N=-3(2-\chi)S^{-4}\pmod P},
\]
\[
\boxed{\mathcal N^{-1}=\tfrac1{12}
\begin{pmatrix}
(1+3\chi)S^6&-(5+3\chi)S^2\\
-(5+3\chi)S^2&(1+3\chi)S^{-2}
\end{pmatrix}\pmod P.}
\tag{U20}
\]

证明：用 \(\chi^2=\chi\) 展开 determinant，得到 \(\tfrac14((1+\chi)^2-(5-\chi)^2)S^{-4}=-3(2-\chi)S^{-4}\)。各节点 \(2-\chi_k=1\) 或 \(2\)，而 \(p>3\)，故它是 unit。矩阵逆式逐节点在 \(\chi=0,1\) 两种情形检验，或直接相乘得到恒等。

这是整个 CRT 代数上的可逆性。它证明 ambient residue pairing 的 perfectness，尚不证明 U4 的截断空间上 perfectness。

## 6. 无穷 unit 条件的精确余式／Padé 等价

以下论证不引用任何未证明的 orthogonal-polynomial normality。

**Lemma U21（高余式行列式恒等式）。** 若 \(P\) 首一 degree \(N\)，\(q\) degree \(<N\)，\(q/P=\sum_{j\ge0}\ell_jz^{-j-1}\)，则對 \(d\le N\)，矩阵 \((\ell_{i+j})_{0\le i,j<d}\) 的 determinant 等于如下 \(d\times d\) 余式矩阵的 determinant：第 \(j\) 列取 \(\operatorname{rem}_P(q u^j)\)，行按 descending 次序取 coefficient \(u^{N-1},u^{N-2},\ldots,u^{N-d}\)。

证明：\(qT/P\) 的负 Laurent 部分与 \(\operatorname{rem}_P(qT)/P\) 相同。另一方面，U17 的部分分式说明该负部分第 \(i\) 行是 \(\sum w_kT(u_k)u_k^i\)，即 Hankel 乘 \(T\) 系数。首一 \(P\) 的 \(1/P\) 在无穷远展开把 descending 高 coefficient 行变成 Laurent 行，其变换矩阵下三角且 diagonal 全为 \(1\)。行列式因而精确相等。若改成 ascending coefficient 行，则另有反序符号；本稿固定 descending。

令 \(\mathcal A_r\) 是 U21 对 \(q=g,d=r\) 的矩阵。于是

\[
\boxed{\det G_0=\det\mathcal A_r.}
\tag{U22}
\]

且有以下完全等价的失败条件：

\[
\det G_0=0
\iff\exists\,0\ne T,\ \deg T<r,
\quad \deg\operatorname{rem}_P(gT)\le N-r-1=4r.
\tag{U23}
\]

也等价于存在 \(A\), degree \(\le4r\)，使

\[
T\equiv-(2-\chi)S^6A\pmod P,
\qquad 0\ne T,\quad\deg T<r.
\tag{U24}
\]

这给出一个具体的 scalar Padé normality 问题：实际 Stieltjes 函数 \(g/P\) 在 profile \(r\) 上首 \(r\) 个矩条件无非零低度 annihilator。

**Lemma U25（真实 matrix profile）。** 令 \(\mathcal B_{r,3r}\) 为线性映射

\[
(T,Q)\longmapsto
\left(\begin{array}{l}
\text{descending top }r\text{ coefficients of }\operatorname{rem}_P(gT+cQ)\\
\text{descending top }3r\text{ coefficients of }\operatorname{rem}_P(cT+hQ)
\end{array}\right)
\tag{U25}
\]

在 U4 的单项式基下的 \(4r\times4r\) 矩阵。则

\[
\boxed{\det M_5=\det\mathcal B_{r,3r}.}
\tag{U26}
\]

证明：分别对两行组用 U21 的单位下三角 Laurent 变换。部分分式乘 \(T,Q\) 的负部分精确等于 U6 的 Gram 行；两个行组变换 determinant 均为 \(1\)。没有新增 scalar、指数、Tate 或 basis normalization。

因此 \(\det M_5=0\) 当且仅当存在非零 \( (T,Q)\) 满足 U4，及

\[
A=\operatorname{rem}_P(gT+cQ),\quad\deg A\le4r;
\qquad B=\operatorname{rem}_P(cT+hQ),\quad\deg B\le2r.
\tag{U27}
\]

利用 U20，此失败条件等价于显式 congruences

\[
12T\equiv(1+3\chi)S^6A-(5+3\chi)S^2B\pmod P,
\]
\[
12Q\equiv-(5+3\chi)S^2A+(1+3\chi)S^{-2}B\pmod P,
\tag{U28}
\]

连同 U4、U27 的 degree profile。这个 matrix Padé 问题同时保留 middle 与实际 half jet；不是未经证明的标准 Selberg determinant。

**环境 unit 不足以推截断 unit。** 例如 \(P=z^2-1\)、\(q=1\) 在 \(\mathbf F_p\), \(p>2\)，互素且 \(q\) 是 CRT unit。但 \(q/P\) 从 \(z^{-2}\) 开始，首矩为 \(0\)，\(d=1\) Hankel determinant 为零。因此 U20 本身不填补 U22/U26 的 normality 缺口。

## 7. 全有限域 residual identity 与 \(H_0\) coefficient

对 \(f(y)=T(y^2)T'(y^2)\)，degree \(\le4r-4\)，有

\[
F_{-5}(TT')
=-\sum_{S_y(z)=0}[v^5]\frac{f(z+v)}{S_z(z+v)^5},
\qquad S_z(y)=S_y(y)/(y-z).
\tag{U29}
\]

证明：考察 rational differential \(f(y)\,dy/(S_y(y)^5(y^p-y))\)。非 head 的 \(\mathbf F_p\) 点 residue 是 \(-f(y)/S_y(y)^5\)。在 head 点 \(z\)，令 \(v=y-z\)，则 \(y^p-y=v^p-v\)，局部展开为

\[
-v^{-6}\frac{f(z+v)}{S_z(z+v)^5}(1+v^{p-1}+\cdots)\,dv.
\]

因为 \(p-1>5\)，其 residue 是 \(-[v^5]f(z+v)/S_z(z+v)^5\)。无穷远没有 residue，由总 residue 和为零得到 U29，包含正确负号。它是 full 部分的恒等式；真实 \(G_0\) 还须依 U10 保留 \(I_{-5}\)。

对 \(Q,Q'\) degree \(<3r\)，

\[
F_3(QQ')=-[y^{p-1}]S_y(y)^3Q(y^2)Q'(y^2)
=-[u^{9r}]S(u)^3Q(u)Q'(u).
\tag{U30}
\]

证明：该 polynomial degree 至多 \(36r-4<2(p-1)\)。有限域 power sum 只有 exponent \(p-1\) 给出 \(-1\)，exponent \(0\) 的和是 \(p=0\)，其余指数在这个范围贡献零。U30 同样不删除 \(I_3\)。这些恒等式可以改变 normality 的计算方式，但单独不是 nonzero proof。

## 8. Pearson：端点与 middle 跳变的精确最低次数

本节定义的是有限域**逐点** Pearson 关系，不假设特征零的正定性或 quasi-definiteness。令 \(x\) 取 \(\mathbf F_p\) 的循环点，\(w(x)=S_y(x)^{-5}\) 在整数代表 \(-a\le x\le a\) 上，其他点为零。令

\[
\widetilde w(x)=\tfrac12\kappa(x)w(x),\qquad
\kappa(x)=2\ (|x|<r),\quad1\ (r\le|x|\le a).
\tag{U31}
\]

于是 \(\widetilde w\) 正好实现 U6 的 scalar \(G_0\) 权重。对 polynomial pair \(\sigma,\tau\)，关系定义为

\[
\sigma(x+1)w(x+1)-\sigma(x)w(x)=\tau(x)w(x)
\tag{U32}
\]

在每个 finite-field 点成立；\(\widetilde w\) 的关系同理。定义 pair 的 class 为 \(\max(\deg\sigma-2,\deg\tau-1)\)，只考虑非零 pair。

**Lemma U33（full 权重）。** 对 \(r\ge2\)，U32 的最小 class 为 \(5\)。一对精确实现为

\[
\sigma_f=(x+a)(a+1-x)^6,
\]
\[
\tau_f=-(x+a+1)^6(a-x)-(x+a)(a+1-x)^6.
\tag{U33}
\]

其中 degree 分别为 \(7,6\)。

存在性的证明：内部应用 U8，\(\sigma_f(x+1)w(x+1)/w(x)=-(x+a+1)^6(a-x)\)。上端点 \(x=a\) 第一项为零；下端点之前的 \(x=-a-1\)，\(\sigma_f(-a)=0\) 消除 flux；其他外部点双方皆零。\(\tau_f\) 的最高次 coefficient 是 \(10a+12=50r+12\equiv83/9\pmod p\)，不会为零：\(p=83\) 不是 U1 的形状。

最低次数的证明：若 \(\deg\sigma\le6,\deg\tau\le5\)，在 \(10r\) 个内部点交叉乘得

\[
(a-x)^5(\tau+\sigma)+(x+a+1)^5\sigma(x+1)=0.
\tag{U34}
\]

左侧 degree \(\le11\)，而 \(10r>11\)，故是 polynomial identity。互素性迫 \(\sigma(x+1)=(a-x)^5V(x)\)。真实上端点 U32 还迫 \(\tau(a)+\sigma(a)=0\)；代回 U34 得 \(V(a)=0\)，所以 \(a+1\) 是 \(\sigma\) 至少六重根。下端点之前 U32 迫 \(\sigma(-a)=0\)，且这个根与 \(a+1\) 不同。因此非零 \(\sigma\) degree 至少 \(7\)，矛盾。如果 \(\sigma=0\)，U34 同时迫 \(\tau=0\)，也不是非零 pair。

**Lemma U35（实际 middle 权重）。** 对 \(r\ge2\)，\(\widetilde w\) 的最小 class 为 \(7\)。一对精确实现为

\[
\sigma_a=(x+a)(a+1-x)^6(x+r-1)(x-r),
\]
\[
\tau_a=-(x+a+1)^6(a-x)(x+r)(x+1-r)
 -(x+a)(a+1-x)^6(x+r-1)(x-r).
\tag{U35}
\]

degree 分别 \(9,8\)。存在性：除了 U33 的端点外，\(\kappa(x+1)/\kappa(x)\) 只在 \(x=-r\) 和 \(x=r-1\) 跳变；此处 \(\sigma_a(x+1)=0\)，从而跳变项消失。其他内部点直接用 U8。\(\tau_a\) 的最高 coefficient 是 \(10a+14\equiv101/9\)，同样非零，因为 \(101\) 不是 U1 素数。

最低次数：假设 \(\deg\sigma\le8,\deg\tau\le7\)。除两个跳变点外的 \(10r-2\) 个内部点给出 U34；其 degree \(\le13\)，而 \(10r-2>13\) 对 \(r\ge2\) 成立，故仍是 polynomial identity。两个端点照 U33 迫 root \(a+1\) multiplicity 至少 \(6\)、root \(-a\) 至少 \(1\)。在 \(x=-r\) 和 \(x=r-1\)，将真实关系与 U34 比较，\(\kappa\) 的非平凡比率 \(2\) 或 \(1/2\) 迫 \(\sigma(-r+1)=0\)、\(\sigma(r)=0\)。这四个根互异，且全部有关比值的分母非零。因此 \(\deg\sigma\ge6+1+1+1=9\)，矛盾。

U33/U35 的 explicit pair 在 \(r=1\) 也成立，但本稿没有证明该小尺度的最低次数。这里的 no-go 范围是当前真实 measure、homogeneous \(x\)-lattice、degree-bounded pointwise polynomial Pearson pair；没有声称排除 arbitrary rational gauge、其他 lattice、matrix-valued OP 或新的独立周期。内部 U8 给出的低次数 pair 不能越过端点 flux 与 middle jumps。

## 9. 一手文献的实际可用范围

本轮归档并实际读取三篇独立 primary source，URL、SHA、页数与准确阅读页见独立 receipt。所读结论与真实 U6 比较如下。

- Dominici 的 [Hankel determinants, Hahn polynomials, and a formula of Krattenthaler](https://www.mat.univie.ac.at/~slc/wpapers/s81dominici.pdf)，实际 PDF1–8：Vandermonde/Cauchy–Binet 可用于一般有限权重；Hahn 的 product formula 使用其具体 binomial/Pochhammer 权重。Heilermann/LDL 论证需要相应 nonzero norm，不能将待证 normality 作为输入。U8 的 reciprocal-binomial fifth power 和 U31 的 middle jump 不能直接代入该 Hahn 权重。
- Rimányi–Varchenko 的 [The Fp-Selberg integral](https://arxiv.org/pdf/2011.14248v2)，实际 PDF1–8：所读 Theorem4.1 是指定 exponent range 内的 coefficient 型 beta/Vandermonde master polynomial integral。U6 是带 \(S^{-5}\) 的 actual node functional，middle 仍在，未证明它等于该 master polynomial。不能只因两边含有限域 Vandermonde 就移植 factorial product。
- Rosengren 的 [Determinantal elliptic Selberg integrals](https://arxiv.org/pdf/1803.05186v2)，实际全 PDF1–10：Heine determinant identity 适用于 linear functional，但所读 discrete Selberg 求值带明确 balanced 参数。没有构造从 U6 到其 balanced weights 且保留 middle 的合法变换。

U22/U26 已由纸面 Laurent/余式推导证明，不依赖称其为哪一种标准 subresultant 的 convention。下一步可以研究此确定余式映射的 principal minor 或 matrix Padé 解；本文不以未核的 subresultant 符号归一化替代 actual identity。

## 10. NEW 首次探针的准确范围与执行历史

自有 NEW `research/cdt_odd_paired_auxiliary_units_structure_20261006_verify.py` 首次且仅首次执行一次；没有 import/execute/rerun 任何旧或同行 producer。命令是 `python research/cdt_odd_paired_auxiliary_units_structure_20261006_verify.py`，退出码 \(0\)。程序有输出已存在即拒绝重跑的 guard。

它在 \(1\le r\le90\) 中选全部 U1 素数，构造 U5/U6 的 exact folded matrices，逐节点核 U7，再做 finite-field Gaussian rank/determinant。共 \(40\) 个素数，\(19\le p\le1621\)，最大 \(M_5\) 尺度 \(360\)。每个 \(G_0\) rank \(r\)、每个 \(M_5\) rank \(4r\)，全部 determinant 非零。JSON 保留每个案例的 actual determinant 和失败时 null-vector 栏位。

这不验证或证明本稿所有 CRT、余式、Pearson、residue 纸面 lemma；不证明无限 unit、任意 \(r\)、全素数费用或新无理性。saved PY 与 saved JSON 已实际完整静态回读；程序未重跑。

## 11. 实际下一数学缺口

本轮把两个原先未求值的矩阵，变成全尺度、完全指定的 modular multiplication maps U22/U25。真正需要证明的是：在无穷多个 \(p=18r+1\) 上，U23 没有非零 \(T\)，并且 U27/U28 没有非零 \( (T,Q)\)。CRT ambient perfectness U20 不是这个结论；middle 满秩 U11 也不能以 rank-one perturbation 处理。

一个可检验的新证明入口是利用 U14 的 Fermat 因式和 U16 的 middle CRT projector，直接证明 profile \( (r,3r)\) 的 remainder-map normality，或者求其 explicit determinant。另一入口是为真实 class7 measure 建立不循环依赖 nonzero norms 的 finite-field orthogonal-polynomial 递推，并证明有关递推係数在 U1 素数上的 units。两条入口均须保留 U16，不应先把 \(\chi\) 设零。

若将来证得无穷 unit，冻结 aux 稿的 conditional Smith/primitive nonzero gate 才可解除。本轮未重算或削减其 all-prime/archimedean 费用，单个辅助素数的费用或有限 nonzero 不能变成 \(n^2\) 级别节省。是否同时形成 strict margin 仍是独立的 arithmetic–analytic matching 问题。
