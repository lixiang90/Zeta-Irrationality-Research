# 第289轮证明 · 八层共同整除之后的实际约分

沿用[第288轮 M9–M12](zeta7_shifted_mellin_round288.md)。写 \(H_j(T)\) 为原来的 \(j\) 阶矩阵，\(P_j=\det H_j,\ b_j=[T^j]P_j\)。\(d_m^*\) 是首一多项式 \(P_m/b_m\) 各系数的最小公分母。以下固定
\[
 \mathcal I_m=\{p>13:2m<p<4m-1,\ p\text{ 为素数}\},
 \qquad h=(p+1)/2-m,\qquad e=m-h .
\]
每个素数的权为 \(e\log p\)，全带权 \(V_m=\sum_{\mathcal I_m}e\log p=m^2+o(m^2)\)。本文用同一矩阵的局部不变量计算约分在 \(d_m^*\) 中产生的指数。全篇结论均不预设 \(\zeta(7)\) 的有理性。

## 从小矩阵到实际分母

取 \(\mathbb Q_p(T)\) 关于 Gauss 赋值的离散赋值环 \(\mathcal O\)。其均匀化参数为 \(p\)，剩余域为 \(\mathbb F_p(T)\)，多项式的赋值是其全部系数赋值的最小值。将 \(H_m\) 的末 \(e\) 行各乘 \(p^8\)，得到环上的分块矩阵
\[
 \begin{pmatrix}H_h&U\\p^8V&C\end{pmatrix}.
\]
M11 已证明 \(\det C\bmod p=\pm(455/16)^e\ne0\)。故完整的左上 Schur 补和所需的本原分母满足
\[
 S_{m,p}=H_h-p^8UC^{-1}V,\qquad
 v_p(d_m^*)=8e+v_p(b_m)-v(\det S_{m,p}).                    \tag{R1}
\]
这是等式。确实，\(\det C\det S_{m,p}=p^{8e}P_m\)，而 \(\kappa_m P_m\) 为本原整数多项式，故 \(v_p(\kappa_m)=-v(P_m)\)，\(d_m^*=\kappa_m|b_m|\)。在本带 \(b_m\) 是 \(p\)-整的。

对满秩环上方阵 \(M\)，记非降序 Smith 指数为 \(s_i(M)\)，并令 \(r_j(M)=\#\{i:s_i(M)\ge j\}\)。等价地，\(r_j\) 是满足 \(Mx\in p^j\mathcal O^h\) 的向量在剩余域中张成的约化空间的维数。此描述由对角化直接得出。于是
\[
 P_h\equiv0\bmod p^8 \quad\Longleftrightarrow\quad
 \sum_{j=1}^8 r_j(H_h)\ge8,\qquad
 r_j(S_{m,p})=r_j(H_h)\quad(1\le j\le8).                    \tag{R2}
\]
首式允许八层分布在多个方向。在 \(r_8(H_h)=0\) 时，R2 已给出 \(v(\det S_{m,p})=v(P_h)\)，即使这个和本身大于或等于 8，结论仍成立。

若需继续求深度，可取 \(H_h\) 在 \(\mathcal O\) 上的 Smith 基，把 \(s_i(H_h)<8\) 的对角项放在最前面，并对 \(S_{m,p}\) 同时作相同行、列变换。在这些位置，左上块为 \(D+p^8E\)，其中 \(D=\operatorname{diag}(p^{s_i})\)，\(\det(I+p^8D^{-1}E)\) 是单位。交叉块都被 \(p^8\) 整除，消去左上块后，所得矩阵仍可逐项除以 \(p^8\)。把这个商记为 \(Z_{m,p}\)，其阶数是 \(r_8(H_h)\)。消元在环上可逆，因为逆矩阵至多有七层分母，而交叉块含八层。于是
\[
 v(\det S_{m,p})=
       \sum_{j=1}^8 r_j(H_h)+v(\det Z_{m,p}),\qquad
 K_{m,p}:=\max_i (s_i(S_{m,p})-8)_+
          =\max_i s_i(Z_{m,p}).                              \tag{R3}
\]
零阶 \(Z\) 的行列式取 1，最大指数取 0。上述等式也给一个实际判定程序：在取到八层后，须对含有原 \(U,C,V\) 的 \(Z_{m,p}\) 继续消元。只将 \(P_h\) 的内容赋值从 \(8e\) 中减去，在深层分支上会遗漏这一步。[相同对象的低维矩阵判别 Q4](zeta7_pencil_structure_round289.md)

## 成功所需的深度随阶数增长

本轮已证有限特征的全阶界
\[
 r_1(H_h)\ \le\ \operatorname{corank}_{\mathbb F_p}([T]H_h)
 \ \le\ \lfloor\sqrt{h/2}\rfloor .                           \tag{R4}
\]
其证明将目标系数矩阵写成 \(2h\) 个节点的反对称 Cauchy 矩阵的奇偶分块。对在其余节点为零、在这 \(2h\) 个节点导数为零的有限域多项式空间作 Wronskian 次数计数，即得 R4。另一个证明直接利用该矩阵与节点对角矩阵的交换子。[两种证明 Q1–Q3](zeta7_pencil_structure_round289.md)

写 \(L_{m,p}=8e-v_p(d_m^*)\) 为相对于本带八层上限实际少掉的指数。它可以为负，因为整个首一分母还包含领系数的贡献。由 R1–R4，
\[
 L_{m,p}\ \le\ \min\{8e,\sqrt{h/2}\,(8+K_{m,p})\}.         \tag{R5}
\]
这里的八个初始层在全带的总影响至多 \(8\sum_{\mathcal I_m}\sqrt{h/2}\log p=O(m^{3/2})\)。令 \(N_m\) 为带外全部素数对 \(\log d_m^*\) 的贡献，则严格有
\[
 \log d_m^*=8V_m-\sum_{\mathcal I_m}L_{m,p}\log p+N_m,
 \qquad N_m\ge0.                                             \tag{R6}
\]
要把完整分母指数降到 \(\log1024\) 以下，所省的带内重量必须同时支付 \(N_m\)。

对任意 \(k_m\to\infty,\ k_m=o(\sqrt m)\)，令 \(F_m(k_m)\) 为 \(K_{m,p}\ge k_m\) 的素数占 \(V_m\) 的加权比例。在这些素数上有 \(r_8(H_h)\ge1\)，即小矩阵本身已经有同一个剩余方向可提升到八层。对其余素数用 R5，其总损失至多 \(O((8+k_m)m^{3/2})=o(m^2)\)。因此
\[
 \frac{\log d_m^*}{m^2}\ \ge\ 8(1-F_m(k_m))+o(1).           \tag{R7}
\]
若一条无界子列上分母率的上极限严格小于 \(\log1024\)，则该子列上
\[
 \liminf F_m(k_m)>1-\log(1024)/8=0.1335660243\ldots
\]
对每一个这样的 \(k_m\) 都成立。例如可取 \(k_m=\lceil m^{1/3}\rceil\)。这要求充分多的素数在第一次八层消元后还能沿同一方向提升越来越多层。即使小行列式的全部系数都被 \(p^8\) 整除，只要实际余下的最大 Smith 指数一致为 \(o(\sqrt m)\)，就有 \(\liminf\log d_m^*/m^2\ge8\)。

还可取 \(k_m=\lceil\alpha\sqrt m\rceil\)，其中 \(\alpha>0\) 固定。对深层素数先扣除其整个 \(8e\log p\)，其余损失用 R5。素数定理与连续函数的 Riemann 和给出
\[
 \frac{\log d_m^*}{m^2}\ \ge\ 8-8F_m(k_m)-I(\alpha)+o(1),\quad
 I(\alpha)=2\int_0^1\min\{8(1-x),\alpha\sqrt{x/2}\}\,dx .    \tag{R8}
\]
变量是 \(x=h/m\)，此处 \(p=2(m+h)-1\)，故积分带有因子 2。以 \(y>0\) 表示 \(y^2+\alpha y/(8\sqrt2)=1\) 的根，则
\[
 I(\alpha)=\frac{4\alpha}{3\sqrt2}y^3+8(1-y^2)^2 .
\]
在 \(\alpha=1\) 时 \(I(1)=0.8829911455\ldots\)。所以严格成功的子列还须有超过 **2.31921%** 的原带重量在八层之后的实际最大指数至少为 \(\lceil\sqrt m\rceil\)。若所有大阶数上 \(K_{m,p}\le\sqrt m\) 对全带一致成立，则直接对每个 \(p\) 使用 R5 得
\(\liminf\log d_m^*/m^2\ge8-I(1)=7.1170088545\ldots>\log1024\)。
后一命题的假设目前没有无界证明。

## 对增长中的端点阶数直接排除八层共同整除

设 \(J_h=\det(\binom{2k}k/k)/\det(1/k)\)，其中两矩阵的索引均为 \(k=i+j+1\)，\(0\le i,j<h\)。对每个外带素数，\(v_p(b_h)=v_p(J_h)\)。逐素数幂的匹配计数表明倒 Hilbert 行列式清掉每项排列的分母。领系数测度在中心反射后与原测度相加成为 Lebesgue 测度，故两正定矩阵的行列式凹性给出
\[
 J_h\in\mathbb Z,\qquad 1\le J_h\le 2^{2h^2-h}.                 \tag{R9}
\]
再按二的最高幂逐段剥去唯一的反对角匹配，得到 \(v_2(J_h)=h\)。外带的奇素数只能整除 \(J_h/2^h\le2^{2h(h-1)}\)。因此 \(8\log_2p>2h(h-1)\) 时小行列式内容至多为七层，\(\log_2p>2h(h-1)\) 时内容为零。特别地，\(h\le 2\sqrt{\log_2p}\) 已能排除八层例外，允许 \(p,h,m\) 同时增长。在固定 \(m\) 上，这个端点带的总权至多 \(O(m(\log m)^{3/2})=o(m^2)\)。[匹配证明、反射测度与精确二进阶 N6–N8](zeta7_polynomial_census_round289.md)

## 用完整矩阵最高极点的模 \(p\) 系数约束实际约分

记 \(B_m=[T]H_m\)，令 \(k_0=(p+1)/2=m+h\)，再引入
\[
 Q_{m,p}(Y)=p^{8m}P_m(Y/p^8)\bmod p=\det(F+YB_m)
       \quad\text{于 }\mathbb F_p[Y].
\]
这里 \(F\) 为常数矩阵 \(p^8 H_m(0)\bmod p\)，\(B_m\) 也取模 \(p\)。第一条有极点的反对角线在 \(k=k_0\)，故 \(F\) 的非零条目全在右下 \(e\) 阶块 \(D\) 中；\(D\) 关于反对角线的第一项 \(f_0=455/16\) 是单位。令 \(V\) 为 \(B_m\) 的右上块，\(B'\) 为其右下块。提取前 \(h\) 行的因子，再在 \(\mathbb F_p[[Y]]\) 中消元，得到
\[
 Q_{m,p}=Y^h\det(D+YB')\det(B_h-YV(D+YB')^{-1}V^{\mathsf T}).
\]
记 \(r=\dim\ker B_h\)，定义下列在 \(\ker B_h\) 上的对称双线性形式
\[
 \Gamma_{m,p}(u,v)=(V^{\mathsf T}u)^{\mathsf T}D^{-1}(V^{\mathsf T}v).
\]
将 \(B_h\) 按其核和任一非退化补空间写成分块形式。上式的小行列式消去补空间后，核块是 \(-Y\Gamma_{m,p}+O(Y^2)\)。因此
\[
 \operatorname{ord}_{Y=0} Q_{m,p}\ge h+r,\qquad
 [Y^{h+r}]Q_{m,p}\ne0\ \Longleftrightarrow\ \Gamma_{m,p}\text{ 非退化}.  \tag{R10}
\]
对零多项式取无穷阶，对零维形式取行列式 1。当 \(h+r>m\) 时，核形式的秩至多 \(e<r\)，两边也相容。R10 使用完整矩阵的最高极点和目标系数，省去 \(H_h(0)\) 的全部有理项。

若 \(\Gamma_{m,p}\) 非退化，将 R10 中的系数还原到原变量得
\[
 v_p([T^{h+r}]P_m)=-8(e-r),\qquad
 v_p(d_m^*)\ge 8(e-r)+v_p(b_m),\qquad L_{m,p}\le 8r.        \tag{R11}
\]
首式只对非退化分支使用。这个分支在整个素数带上至多损失 \(O(m^{3/2})\) 的对数重量，即使在 R2 中小行列式的全部系数已同被 \(p^8\) 整除也成立。

令 \(F_m^\cap(k)\) 为同时满足 \(\Gamma_{m,p}\) 退化且 \(K_{m,p}\ge k\) 的素数占全带的加权比例。仅对这批素数丢弃其全部 \(8e\log p\)，对非退化分支用 R11，对其余分支用 R5。则 R7、R8 都能把 \(F_m\) 换成较小的 \(F_m^\cap\)。特别地，若一条无界子列能使完整分母率严格低于 \(\log1024\)，则在取到固定正余量的子列上
\[
 \liminf F_m^\cap(\lceil m^{1/3}\rceil)>0.1335660243\ldots,\qquad
 \liminf F_m^\cap(\lceil\sqrt m\rceil)>0.0231921311\ldots .      \tag{R12}
\]
精确门槛分别为 \(1-\log(1024)/8\) 和 \(1-(\log(1024)+I(1))/8\)。两个集合中的每个素数均已满足较小 \(P_h\) 的八层共同整除。R12 是同一个实际分母的必要条件，带外费用仍由 R6 计入。

这个新形式有不涉及大有理数的系数表示。令 \(f_j\) 为第 \(k_0+j\) 个常数矩的最高极点系数，即 \(D_{ab}=f_{a+b-e+1}\)，其中负下标取零。由上轮 M5，把求和指标换为 \(i=k-c\)，有
\[
 f_j=-\frac{35}{x_j}\sum_{i=0}^{2j+1}
                 (2i-x_j)\binom{x_j}{i}^{\!4}\ \in\mathbb F_p,\qquad
 x_j=j+\tfrac12,\qquad 0\le j<e .
\]
分母为单位，因为 \(2j+1<p,\ k_0+j<p\)。写 \(f(z)=\sum_{j=0}^{e-1} f_j z^j\)，将 \(V^{\mathsf T}u\) 的坐标按升幂写成 \(c_u(z)\)。按系数卷积直接解反三角系统 \(Dv=V^{\mathsf T}u\)，得
\[
             \Gamma_{m,p}(u,w)=[z^{e-1}]\,c_u(z)c_w(z)/f(z).
\]
例如 \(m=10,p=29\)，\(h=e=5,\ r=1\)，实算 \([Y^6]Q=4\bmod29\)，故原 \(P_{10}\) 至少有一项的分母含 \(29^{32}\)。另由小 \(P_5\) 的常数项为单位，R1 给出更精确的八层全保留 \(v_{29}(\kappa_{10})=40\)。两个判别检查同一对象的不同系数，可交叉核验。

独立用有限域稠密核与截断逆级数计算了 \(m\le1024\) 的全部 138021 对。在 \(B_h\) 奇异的 99 对中，核维数均为 1，\(\Gamma_{m,p}\) 均非退化。选取包括 \(e=2\) 的五对，用原始有理矩逐项还原 \(F\)，再插值整个 \(Q\)，R10 的最低次数和系数均匹配。以上是有限证书。仍需控制增长中的 \(m,h,p\) 上核形式退化的总权，或证明退化分支的实际深度不足。[有限域证书](verify_zeta7_outer_symbol_round289.py) · [独立核查](zeta7_actual_cost_round289.md)

## 可用纯模 \(p\) 算术检测的连续零系数

若 \(Q_{m,p}\ne0\)，置 \(\tau_{m,p}=\operatorname{ord}_{Y=0}Q_{m,p}-h\in[0,e]\)。若 \(Q_{m,p}=0\)，置 \(\tau_{m,p}=e\)。在前一情形，首个非零系数给
\[
 v_p(d_m^*)\ge8(e-\tau_{m,p})+v_p(b_m).
\]
后一情形直接用 \(v_p(d_m^*)\ge0\)。故对每个外带素数都有 \(L_{m,p}\le 8\tau_{m,p}\)。令 \(\mathcal E_m\) 为 R12 中 \(\Gamma_{m,p}\) 退化且 \(K_{m,p}\ge\lceil m^{1/3}\rceil\) 的素数集合。其补集由 R5、R11 共损失至多 \(O(m^{11/6})=o(m^2)\) 的对数重量。因此
\[
 \frac{\log d_m^*}{m^2}\ \ge\
 8\left(1-\frac{\sum_{p\in\mathcal E_m}\tau_{m,p}\log p}{V_m}\right)+o(1).
                                                                  \tag{R13}
\]
取 \(\eta=1-\log(1024)/8\) 及 \(0\le\lambda<\eta\)，定义 \(F_m(\lambda;\mathcal E_m)\) 为满足 \(p\in\mathcal E_m,\ \tau_{m,p}>\lambda e\) 的素数占全带的 \(e\log p\) 加权比例。R13 的和除以 \(V_m\) 后至多为 \(\lambda+(1-\lambda)F_m(\lambda;\mathcal E_m)\)。由此，任何具有严格正余量的成功子列都须满足
\[
 \liminf F_m(\lambda;\mathcal E_m)>\frac{\eta-\lambda}{1-\lambda}.
\]
例如取 \(\lambda=1/16\)，要求 **超过 \(7.5803759\%\)** 的全带重量同时具有深层约分，并且 \(Q_{m,p}\) 的 \(Y^h,\ldots,Y^{h+\lfloor e/16\rfloor}\) 各项全为零。取 \(\lambda=1/8\)，这个比例仍须超过 \(0.9789742\%\)。单凭这串有限域系数就能排除许多候选：若前一种消零事件在全序列上的加权上极限至多为 \((\eta-1/16)/(1-1/16)\)，便能排除这套等斜率构造的严格指数。这个上极限仍未判定。
