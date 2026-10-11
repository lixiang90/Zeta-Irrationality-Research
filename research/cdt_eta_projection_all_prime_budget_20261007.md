# Even-node η(s) 真实 Hermite 投影的全素数预算

2026-10-07。固定整数 \(r\ge2,n\ge1,H=rn,s=r+1\)。本稿独立重推实际单周期身份、全部素数及其高幂的完整多项式整模型、首层共轭及 near-n graded 零行、逐列和尾 rank 费用。得到 leading 预算 \(C_\eta(4)=9389/630\)、\(C_\eta(6)=503807/20020\)，已收到 root 独立全文数学审查 PASS。本稿没有非零性或新无理性定理；同对象实处界另在[解析稿](cdt_eta_projection_real_energy_20261007.md)给出。

## 1. 同一完整 Hermite P 与真实正内核

令 \(J=\{0,\ldots,n-1\}\)、\(I=\{n,\ldots,H-1\}\)，定义

\[
D(z)=\prod_{u=0}^{H-1}(z-u),\quad B_k(z)=\prod_{v\in J,v\ne k}(z-v),\quad Q_I(z)=\prod_{u\in I}(z-u),
\]
\[
\Phi_k=Q_I/B_k^{r-1},\quad T_k=[\Phi_k]_{k,<r},\quad
N_k=B_k^rT_k,\quad P_{ku}=N_k(u)/D'(u).
\tag{Y1}
\]

这是原完整 Hermite 行，\(\deg N_k\le H-1\)。在低节点取同一多项式极限得 \(P_{kv}=\delta_{kv}\)；\(F_k=N_k/D\) 在每个 \(v\in J\) 的 regular part 的前 \(r-1\) 项为零，因此

\[
F_k(z)=\sum_uP_{ku}/(z-u),\qquad
\sum_{u\ne v}\frac{P_{ku}}{(u-v)^\ell}=0
\quad(v\in J,1\le\ell\le r-1).
\tag{Y2}
\]

本轮实际全文读原 exact-arithmetic 稿全部12节/E1–E37，其中 factorial base 的完整整数二项式身份给

\[
D_{H-1}^{r-1}P_{ku}\in\mathbb Z,
\quad D_m:=\operatorname{lcm}(1,\ldots,m),\quad D_0=1.
\tag{Y3}
\]

具体理由为 \(P_{ku}=b_{ku}\sum_{a<r}h_{ka}(u-k)^a\)，\(|b_{ku}|=\binom uk^{r-1}\binom{H-1-k}{u-k}\binom{u-k-1}{u-n}^{r}\in\mathbb Z\)，而 \(D_{H-1}^a h_{ka}\) 为整数。这个证明同时覆盖2和全部高幂，没有额外 factorial 分母。

定义实际对象

\[
C_\eta(u,v)=\sum_{a\ge1}\frac{(-1)^{a-1}}{(a+2u)(a+2v)^r}
=\int_0^1\!\int_0^1\frac{x^{2u}y^{2v}}{1+xy}
\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy.
\tag{Y4}
\]

级数绝对收敛，逐项积分的绝对和也有限，因为项为 \(O(a^{-r-1})\)。因此这是同一正实积分的合法表示，不是仅形式的 η 参数化。

## 2. 完整低周期消去与准确 qη

记

\[
A_{u,b}^\eta=\sum_{a=1}^{2u}\frac{(-1)^{a-1}}{a^b},\qquad A_{0,b}^\eta=0.
\tag{Y5}
\]

由 Y2，对任意 \(v\in J\)，

\[
\frac{F_k(z)}{(z-v)^r}
=\frac{\delta_{kv}}{(z-v)^{r+1}}+\sum_u\frac{c_{kvu}}{z-u},
\quad c_{kvu}=\frac{P_{ku}}{(u-v)^r}\ (u\ne v),
\quad c_{kvv}=-\sum_{u\ne v}c_{kvu}.
\tag{Y6}
\]

最高阶极点来自低节点 delta，所有2至r阶极点由完整 regular-part 条件消去，simple residues 之和为零。令 \(z=-a/2\)，再对 \((-1)^{a-1}\) 求和。因为移位是 \(2u\) 偶数，\(\sum_{a\ge1}(-1)^{a-1}/(a+2u)=\eta(1)-A^\eta_{u,1}\)。这些 simple sums 可先合成绝对收敛差；不能靠独立拆分条件收敛项掩盖端点。最终准确身份为

\[
\boxed{E_\eta:=PC_\eta=q_\eta+\eta(r+1)I_n,}
\]
\[
\boxed{(q_\eta)_{kv}=(-1)^{r-1}2^{-r}
\sum_{u\ne v}\frac{P_{ku}(A^\eta_{u,1}-A^\eta_{v,1})}{(u-v)^r}
-\delta_{kv}A^\eta_{v,r+1}.}
\tag{Y7}
\]

可以直接核符号：Y6 在 \(z=-a/2\) 的 simple 部分乘 \((-1)^r2^{-r}\)，再用 \(\eta(1)-A_u\) 及 residue sum0，恰得 \((-1)^{r-1}2^{-r}\)。没有假定 \(\eta(2),\ldots,\eta(r)\) 有理；它们及其有限高阶尾都已真正消去。

## 3. 全素数、高 p-power 和 n=1 的 fallback

令 \(L_m(p)=\max\{e\ge0:p^e\le m\}\)，\(m<1\) 时为0。Y3、节点差不超过 \(H-1\)、simple harmonic 分母不超过 \(2H-2\)，共同给每个 entry 的全素数估计

\[
v_p((q_\eta)_{kv})\ge-a_p^0,
\quad a_p^0=r\mathbf1_{p=2}+(2r-1)L_{H-1}(p)+L_{2H-2}(p).
\tag{Y8}
\]

对角的 \(A_{v,r+1}\) 也由此覆盖：\(2v\le2n-2\le H-1\)，而 \(r+1\le2r-1\)。不是把对角和 off-diagonal 的两份费用相加。于是

\[
M_{r,n}=2^rD_{H-1}^{2r-1}D_{2H-2},\qquad
M_{r,n}^n\mathcal D_{r,n}(T)\in\mathbb Z[T],
\quad \mathcal D_{r,n}(T)=\det(q_\eta+TI_n).
\tag{Y9}
\]

这完整支付全部 p-power，包括2；\(p>2H-2\) 无分母（\(r\ge2\) 时常数2已在范围内）。n=1时 \(B_0=1\)，\(\deg Q_I=r-1\)，所以 Taylor 保留整个 Q，\(F_0=1/z\)、\(P_{0u}=\delta_{0u}\)，从而 \(q_\eta=0\)、\(E_\eta=[\eta(s)]\)、\(\mathcal D_{r,1}(T)=T\)。D0约定也处理此时空 harmonic 尾；Y9虽不必最小，仍无例外成立。

## 4. 首层 p≤n 的同一共轭格

以下设奇素数 \(p^2>2H\)。所有实际节点差和 harmonic 分母都只有至多一层 p。对每个 residue \(a\)，记

\[
d_a=\#J(a),\quad e_a=\#I(a),\quad t_a=d_a+e_a,
\quad h_a=(r-1)d_a-e_a=rd_a-t_a,
\quad S=\operatorname{diag}(p^{h_{k\bmod p}}).
\tag{Y10}
\]

对 \(c=k\bmod p\)，写 \(\Phi_k(k+w)=\sum_{\ell\ge0}\alpha_\ell w^\ell\)。分子和 inverse powers 按 Taylor 次数逐项计数得

\[
v_p(\alpha_\ell)\ge e_c-(r-1)(d_c-1)-\ell.
\]

当 \(u\equiv k\) 时，\((u-k)^\ell\) 补回 \(\ell\) 层，结合 \(B_k(u)^r,D'(u)\) 的层数，得到 \(v_p(P_{ku})\ge0\)。当 \(a=u\bmod p\ne c\)，最高允许 Taylor 次数为 \(r-1\)，得到

\[
v_p(P_{ku})\ge h_a-h_c+1\quad(u\in I,a\ne c).
\tag{Y11}
\]

连续节点使 \(\max h-\min h\le r\)：若 \(n=Ap+b\)、\(rb=cp+b_r\)，则 \(h_a=r\mathbf1_{a<b}-c-\mathbf1_{a<b_r}\)。按 \(b_r\le b\) 或 \(b_r>b\) 分开，其振幅均至多r，而不是粗估r+1。

对 Y7 每项一次加入共轭因子 \(p^{h_k-h_v}\)：若 \(u\equiv v\)，r次差损失r层，harmonic差最多1层；当 \(u\not\equiv k\) 时 Y11 多保护1层。若 \(u\not\equiv v\)，差为单位；Y11 与共轭抵消 k 的层，只剩 \(h_u-h_v\) 及至多1层 harmonic。\(u=k\) 的唯一低节点另按 \(P=1\) 处理。对角尾最多损失s层，\(2^{-r}\) 对该奇p为单位。由振幅≤r，得到

\[
\boxed{p^sSq_\eta S^{-1}\in M_n(\mathbb Z_p),\qquad
p^{sn}\mathcal D_{r,n}(T)\in\mathbb Z_p[T].}
\tag{Y12}
\]

S不是免费整数变基；使用的准确事实是 \(\det(S(q+TI)S^{-1})=\det(q+TI)\)，其左右 determinant 层精确抵消。Y12是完整系数付款，不只控制一个目标特殊值。

## 5. near-n 的真实 graded 零行

进一步设 \(p\le n\) 且 \((2r+1)p>2rn\)。则 \(n=p+b\)、\(rb<p/2\)，\(H=rp+rb\)。residue 权重恰为

\[
h_a=\begin{cases}r-1,&0\le a<b,\\-1,&b\le a<rb,\\0,&rb\le a<p.\end{cases}
\tag{Y13}
\]

对整数 \(k=a\in[rb,\lceil p/2\rceil)\)，该 residue 在 J 中只有一个节点k，在全节点中恰有r个，因此 \(B_k(k)\) 为p单位且 \(v_p(D'(u))=r-1\) 对同 residue 的高节点成立。这里 \(\Phi_k(k+w)\in\mathbb Z_p[[w]]\)，在 \(u\in I,u\equiv k\) 处 \(\Phi_k(u)=0\)。完整 Taylor 余项至少p^r，故

\[
v_p(T_k(u))\ge r,\qquad v_p(P_{ku})\ge1.
\tag{Y14}
\]

这是真实零行所需的额外一层，不可仅用 Y11 的同 residue 粗界0代替。对该行，\(2k<p\)，对角 harmonic 尾为整；若 \(u\equiv v\equiv k\)，Y14消去最坏的第s层；若 \(u\equiv v\not\equiv k\)，Y11仍多保护一层；其余项由 \(h_k=0\)、\(h_v\le r-1\) 或 \(h_u-h_v\ge-r\) 估计。每种情况的共轭 q entry 都至少 \(-r\)，所以

\[
p^sS(q_\eta+TI)S^{-1}
\quad\text{在上述每个k行的全部多项式系数均被p整除。}
\tag{Y15}
\]

行数及完整内容付款为

\[
z_p=\max(0,\lceil p/2\rceil-r(n-p)),\qquad
p^{sn-z_p}\mathcal D_{r,n}(T)\in\mathbb Z_p[T].
\tag{Y16}
\]

Y16仅在本节窗口且 \(p^2>2H\) 使用；其他首层 \(p\le n\) 仍用Y12。这不借用目标的未知有理性或非零性。

## 6. n<p≤H 的完整逐列预算，以及 H<p 的尾 rank

仍设 \(p^2>2H\)。若 \(p>n\)，每个 \(B_k(k)\) 为p单位，所以原未正规化的 Taylor 系数均p整。记

\[
\eta_{p,a}=\left\lfloor\frac{H-1-a}{p}\right\rfloor
\quad(0\le a<p),\qquad
v_p(D'(u))=\eta_{p,u\bmod p}.
\tag{Y17}
\]

对 \(u\in I,u\equiv v\pmod p\)，\(v\in J\)，当 \(v\ne k\) 时 \(B_k(u)^r\) 已含p^r；当v=k时用 \(\Phi_k(u)=0\) 的同一 Taylor 余项p^r。因此

\[
v_p(P_{ku})\ge r-\eta_{p,v}\qquad(u\equiv v,\ v\in J).
\tag{Y18}
\]

其它节点若 residue \(a\notin J\)，只有 \(v_p(P_{ku})\ge-\eta_{p,a}\)，但此时 \(a\ge n>v\)，所以 \(\eta_{p,a}\le\eta_{p,v}\)。若 residue 属J，Y18更强；低节点仍为delta。由此对每列v，一次取max得到

\[
c_{p,v}=\max\left(\eta_{p,v}+1,\ s\mathbf1_{2v\ge p}\right),
\qquad
p^{\sum_v c_{p,v}}\mathcal D_{r,n}(T)\in\mathbb Z_p[T]
\quad(n<p\le H).
\tag{Y19}
\]

确切理由：matching差的r层由Y18抵消，最多只剩 \(\eta_{p,v}+1\)；nonmatching差为单位，用Y17–Y18及至多1层 harmonic；对角 \(A_{v,s}\) 仅当 \(2v\ge p\) 有p分母，因为 \(2v<2p\)。没有另外增加投影或Schur分母。

若 \(H<p\le2H-2\)，P与所有非零节点差都p整且后者为单位。低节点的所有 harmonic 尾也p整；高节点的 \(A_{u,1}\) 唯一非整项是分母p，存在恰当且仅当 \(u\ge m_p:=\lceil p/2\rceil\)，符号为 \((-1)^{p-1}=1\)。因此

\[
pq_\eta\bmod p=(-1)^{r-1}2^{-r}
\left(\sum_{u=m_p}^{H-1}\overline P_{ku}(u-v)^{-r}\right)_{k,v}.
\tag{Y20}
\]

其真实因子分解是n×(H−m)乘(H−m)×n，故rank≤ \(R_p=\min(n,(H-\lceil p/2\rceil)_+)\)。将 \(p(q+TI)\) 的模p常数矩阵用p整单位左右变换化成rank块，至少n−R行所有系数含p，得到

\[
\boxed{p^{R_p}\mathcal D_{r,n}(T)\in\mathbb Z_p[T]\quad(H<p\le2H-2).}
\tag{Y21}
\]

此为完整多项式内容的实际rank节省，不将单个 entry 或 period 类型数当成rank。\(p>2H-2\) 完全整。

## 7. 全 n 的有限 G 与 leading 常数

对所有 \(p\le2H-2\) 设

\[
g_p=\begin{cases}
na_p^0,&p=2\ \text{或}\ p^2\le2H,\\
sn-z_p,&p^2>2H,\ p\le n,\ (2r+1)p>2rn,\\
sn,&p^2>2H,\ p\le n,\ (2r+1)p\le2rn,\\
\sum_{v<n}c_{p,v},&p^2>2H,\ n<p\le H,\\
R_p,&p^2>2H,\ H<p\le2H-2.
\end{cases}
\quad G_{r,n}=\prod_{p\le2H-2}p^{g_p}.
\tag{Y22}
\]

由Y8/Y12/Y16/Y19/Y21，

\[
\boxed{G_{r,n}\mathcal D_{r,n}(T)\in\mathbb Z[T]\quad(r\ge2,n\ge1).}
\tag{Y23}
\]

small primes 包括全部高p-power：\(a_p^0\log p=O_r(\log(n+2))\)，\(p\le\sqrt{2H}\) 的总付款为 \(O_r(n^{3/2}\log(n+2))=o(n^2)\)；2另可看作 \(O_r(n\log n)\)。没有首层表遗漏的高幂。

以下r固定，使用 \(\vartheta(x)=\sum_{p\le x}\log p=x+o(x)\) 和 partial summation。首层p≤n的基本费用为s，near-n节省为

\[
\int_{2r/(2r+1)}^1\left((r+\tfrac12)x-r\right)dx
=\frac1{4(2r+1)}.
\]

对 \(x=p/n\in(1,r)\)、\(y=v/n\in[0,1]\)，非边界列的 baseline 为
\(1+\lfloor(r-y)/x\rfloor\)。其积分从1到r为 \((r-1/2)H_{r-1}\)：展开 floor 为 \(\sum_{m=1}^{r-1}\mathbf1_{y<r-mx}\)，每个m的长度积分为 \((r-1/2)/m-1\)，再与baseline的r−1抵消。对1<x<2，对角s覆盖 \(y\ge x/2\)，额外费用为

\[
\frac r4-\sum_{m=1}^{r-1}\int_1^2
\max\bigl(0,\min(1,r-mx)-x/2\bigr)dx.
\]

尾区x∈(r,2r)的实际rank density为 \(\min(1,r-x/2)\)，积分r−1。于是完整leading为

\[
\boxed{\log G_{r,n}\le C_\eta(r)n^2+o_r(n^2),}
\]
\[
\boxed{C_\eta(r)=2r+(r-\tfrac12)H_{r-1}+\frac r4
-\sum_{m=1}^{r-1}\int_1^2\max(0,\min(1,r-mx)-x/2)dx
-\frac1{4(2r+1)}.}
\tag{Y24}
\]

floor/ceil 仅影响固定r下O(1)个边界列，所有prime求和付款O_r(n)，不改变leading。r4的三个积分是1/4、1/5、1/28，故 \(C_\eta(4)=9389/630\approx14.9031746032\)。r6的五个积分是1/4、1/4、19/84、1/8、1/44，故 \(C_\eta(6)=503807/20020\approx25.1651848152\)。这些是安全费用上界，不称最优费用或必要下界。

若 \(\eta(s)=a/b\in\mathbb Q\)，则 \(b^nG_{r,n}\det E_\eta\in\mathbb Z\)；仅在 \(\det E_\eta\ne0\) 时，得到 \(\log|\det E_\eta|\ge-C_\eta(r)n^2-o_r(n^2)-n\log b\)。\(\eta(r+1)=(1-2^{-r})\zeta(r+1)\) 是固定有理缩放，单一目标关系明确；不借用 β4 对象的能量或无限非零性。

## 8. 两个固定小矩阵的准确证书

本轮仅1段全新内联 Fraction 运算，固定n2/r4及n2/r6；逐项从Y1构造P、核PJ=I和Y2全部ℓ1至r−1条件，再构造Y7的q与完整monic多项式，核Y9及Y23。没有扩旧prime表。

对 n2/r4，准确 q 为

\[
\begin{pmatrix}
-665483531/3632428800&1568219/148262400\\
-1146214049/3632428800&-504691199/518918400
\end{pmatrix},
\]

\[
\mathcal D_{4,2}(T)=T^2-\frac{1049580481}{908107200}T
+\frac{3509281871273069}{19332657856512000}.
\]

对n2/r6，准确 q 为

\[
\begin{pmatrix}
-1986768092538737/2287343768371200&520861911901/257449947955200\\
-4989639226274767/3964729198510080&-382896773977247/386174921932800
\end{pmatrix},
\]

\[
\mathcal D_{6,2}(T)=T^2-\frac{1707130765409}{917761388544}T
+\frac{39674759936467785079305812679043}{45932369661579685742216478720000}.
\tag{Y25}
\]

下表是两个固定多项式全部系数的分母估值核查，分别显示实际需要层数和完整Y22安全层数；它不预测更大n的rank或内容。

|r|p|实际系数分母层数|Y22付款|
|---:|---:|---:|---:|
|4|2|17|42|
|4|3|7|18|
|4|5|3|4|
|4|7|3|3|
|4|11|2|2|
|4|13|1|1|
|6|2|34|86|
|6|3|12|48|
|6|5|4|6|
|6|7|3|4|
|6|11|3|3|
|6|13|2|2|
|6|17|2|2|
|6|19|2|2|

运算同时准确确认上述所有完整系数乘 \(G_{r,n}\) 为整数；没有用实际目标值的浮点 determinant 判断非零。

## 9. 阅读、运行和结论的准确边界

本轮实际全文读取 [exact arithmetic](cdt_beta4_projection_exact_arithmetic_20261007.md) 全12节/E1–E37 与 [large-prime tail](cdt_beta4_large_prime_tail_content_20261007.md) 全6节/L1–L23。新对象Y4/Y7及本稿Y8–Y24逐项纸推，固定两实例的准确 Fraction 程序只是有限核查。新PDF阅读0页，新增网页数学输入0，新文献下载0；未修改原仓库或旧研究记录，未执行旧producer、guard、prime表、Lean、PSLQ或未知常数拟合。

Y23是全部p-power、完整polynomial content的实际整模型。Y24是同一模型的leading费用，不提供无限n上的 \(\mathcal D_{r,n}(\eta(s))\ne0\)。原 β4 的其他模型已证非零种子或能量不能继承。尚无 ζ5、ζ7 或新 η/L 值无理性结论。

作者另实际全文读[同对象 η 实处稿](cdt_eta_projection_real_energy_20261007.md)全8节/A1–A26，核其A2/A3/A4分别与本稿Y1/Y4/Y7为同一个P、实际C和准确q，没有移植别的实现。该稿A1/A22给有限n带权上界，A24给 \(\gamma_4^\eta>1\) 的符号证书，A25/A26给 \(\gamma_6^\eta>9/100\) 的严格复球下界证书；这些已认证的收缩下界尚未超过本稿的安全费用常数，因此现有两侧结论不足以形成 strict margin。本稿没有执行或复算其复球程序，也不把实处数值说明当成新的严格区间。root 通知该实处稿已独审；本段交叉链接只标明同对象与各项证据的来源，不扩张本稿的程序核查范围。

root 已实际全文读本稿全9节/Y1–Y25，独立逐项核Y7真实符号/收敛、Y8全部高powers fallback、Y11/Y12共轭、Y14 Taylor额外层及Y15整行消失、Y19 matching/nonJ保护、Y20/Y21完整tailrank、Y22全n覆盖、Y24逐段PNT积分，明确纸面数学 PASS，无修正请求。root 另以1段全新内联Fraction，从Φ归一化逐因子重新构造n2/r4及n2/r6全部P，独核PJ=I、所有regular-part、q的每个分数及det全部三个系数，与Y25逐位一致；逐piece积分独算9389/630、503807/20020及本稿所列各积分值。root 没有额外重算本稿的有限G估值表，作者也未扩大固定两实例范围。作者收讫后补入实际独审记录、交叉链接，并完成最终全文回读。
