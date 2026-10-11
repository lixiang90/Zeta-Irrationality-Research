# 真实辅助素数 Padé 模块的辛自对偶、两整数缺陷与 principal subresultant

2026-10-06，NEW 独立数学稿。冻结 dcc6 稿与旧/同行数学 producers 仅读，无执行、import 或重跑。本稿的全尺度证明为纸面推导。一个自有 NEW first-only 程序只在五个以前已经考察的尺度上检验模块机制，没有扩充辅助素数表。

## 1. 本轮范围与真实输入

本轮实际读取冻结 research/cdt_odd_paired_auxiliary_units_structure_20261006.md 的 U14–U28、完整相关 Pearson/来源范围；SHA dcc6d4d670dbcc3960936d3ee1b21a877f73c03e2ba65c479c9d550e0624a8a5。首次与网络检索结果批量输出的末尾有组合截断，不将截断后的末节算作本轮重新全文阅读。冻结全文已在前轮真实读过，本轮的新证明只使用明确的 U14–U28。

设 \(p=18r+1\) 为素数，\(r\ge1\)，\(N=5r+1\)，

\[
P(u)=u\prod_{k=1}^{5r}(u-k^2),\qquad
S(u)=\prod_{k=5r+1}^{9r}(u-k^2),\qquad
PS=u^{9r+1}-u.
\tag{D1}
\]

令 \(\chi\in\mathbf F_p[u]/P\) 是 middle 节点 \(0^2,\ldots,(r-1)^2\) 的 CRT projector，\(\chi^2=\chi\)。所有下式取 degree \(<N\) 的唯一余式代表：

\[
g=-\tfrac12(1+\chi)S^{-6},\quad
c=-\tfrac12(5-\chi)S^{-2},\quad
h=-\tfrac12(1+\chi)S^2,\qquad
\mathcal N=\begin{pmatrix}g&c\\c&h\end{pmatrix}.
\tag{D2}
\]

这就是冻结稿实际 half jet 和 middle 修正的矩分子，\(\mathcal N^{\mathsf T}=\mathcal N\)。原 unit 目标是 degree profile \(\deg T<r,\deg Q<3r\) 的 \(G_0\) 与 \(M_5\) 非零。

本轮证明：

- 两个真实 kernel 分别等于 rank2/rank4 多项式 graph 模块的严格负 shifted-degree 部分。
- 临界 shift 下，rank4 约化次数必为 \((-d_2,-d_1,d_1,d_2)\)，亏秩恰为 \(d_1+d_2\)；scalar 次数为 \((-d,d)\)，亏秩为 \(d\)。这些整数不依赖约化路径。
- Scalar 目标 determinant 精确是 index \(4r+1\) 的 padded principal subresultant，归一化与符号全部固定。
- 实际 \(p=37,r=2\) 数据已经不是 perfect Padé/OP 系统：首 Hankel determinant 为零，但原目标 \(G_0\) 的 size2 determinant 是4。这排除一个真实而非 toy 的过强 normality 推理。

未证明 \(d=d_1=d_2=0\) 在无穷辅助素数上成立；未得到实际 target determinant 的 factorial product 或新的费用/无理性结论。

## 2. 真实 graph lattice 和临界 index

全程在 \(F=\mathbf F_p\)、\(F[u]\) 上研究多项式模块；这里的 rank2/rank4 不是 CDT differential rank，也不是免费新增 arithmetic packet。

Scalar 模块定义为

\[
\mathscr E_g=\{(T,A)\in F[u]^2:A\equiv gT\pmod P\}.
\tag{D3}
\]

其 row basis 是

\[
B_{g,0}=\begin{pmatrix}1&g\\0&P\end{pmatrix},\qquad\det B_{g,0}=P.
\tag{D4}
\]

Matrix 模块定义为 row vectors

\[
\mathscr E_{\mathcal N}
=\{(T,Q,A,B)\in F[u]^4:(A,B)\equiv(T,Q)\mathcal N\pmod P\},
\]
\[
B_{\mathcal N,0}=
\begin{pmatrix}I_2&\mathcal N\\0&P I_2\end{pmatrix},\qquad
\det B_{\mathcal N,0}=P^2.
\tag{D5}
\]

证明：任意模块向量减去其前面两个分量乘 D5 的头两行，后两分量是 \(P\) 的倍数，恰由末两行生成。线性独立由非零 determinant 给出。D3 同理。因此 graph index 是 \(P\) 或 \(P^2\)，无须假设 ambient numerator 是 unit。

Scalar 和 matrix 的 degree bounds 分别是

\[
b_g=(r,\,4r+1),\qquad
b_{\mathcal N}=(r,\,3r,\,4r+1,\,2r+1).
\tag{D6}
\]

把四个界写成严格 \(\deg f_i<b_i\)，D6 正好等于冻结 U23 与 U27 的所有 degree cutoffs。分别有 \(\sum b_g=N\)、\(\sum b_{\mathcal N}=2N\)。并且 scalar 两分量、matrix 成对的 \(T/A,Q/B\) bounds 满足 \(b_i+b_{i+\nu}=N\)，其中 \(\nu=1,2\)。

## 3. 不依赖 normality 的约化和 predictable degree

取 shift \(s=-b\)，对非零 row vector \(v\) 定义

\[
\operatorname{sdeg}v=\max_i(\deg v_i-b_i).
\tag{D7}
\]

Leading position 取达到最大值的最大 coordinate index。若一组 polynomial row basis 的 leading positions 互异，称其 shifted weak-Popov basis。本节只用这个明确定义，不偷用未知的 perfectness。

**Lemma D8（存在且可逐点构造）。** 任意 nonsingular square polynomial row basis 可经 unimodular row operations 约化为上述形态。

证明：两行 leading position 相同时，选择 shifted degree 较高的一行，用较低行乘一个 monomial 与非零 field coefficient 消去其 leading term。同 position 的 raw degree 差等于 shifted-degree 差，所以所需 monomial 次数非负。被改行的新 shifted degree 更小，或 degree 相同但 leading position 更小。取 \((2\nu)\operatorname{sdeg}+\operatorname{LP}\) 为整数 measure，每次严格下降；它由固定 shift 下界约束，故有限次停止。每步是 row addition，basis determinant 保持非零，不能产生零行。过程不除待证 Gram determinant，只除已出现的非零 field leading coefficient。

**Lemma D9（predictable degree 和 index）。** 对 shifted weak-Popov rows \(v_i\)，令 \(\delta_i=\operatorname{sdeg}v_i\)。任意 polynomial combination 满足

\[
\operatorname{sdeg}\Big(\sum_i q_i v_i\Big)
=\max_{q_i\ne0}(\deg q_i+\delta_i).
\tag{D9}
\]

证明：在达到最大值的项中，取最大 leading position 的行；其他同值行的最高 shifted-degree coefficient 不含更大 position，也不能消去此最大 position，较低值行不能参与此 leading term。故没有该 degree 的整体消去。

把 rows 按 leading position 排列，它们的 shifted leading-coefficient matrix 为三角且 diagonal 非零。乘各 column 的 \(u^{-b_j}\)，在 Laurent ring 中比较 determinant 的最高次数，得到

\[
\deg\det B=\sum_i\delta_i+\sum_j b_j.
\tag{D10}
\]

由 D4–D6 与 unimodular determinant 不变，

\[
\boxed{\sum_i\delta_i=0.}
\tag{D11}
\]

严格 negative 部分的 vector-space dimension 为

\[
\boxed{\dim_F\mathscr E_{<0}=\sum_i\max(0,-\delta_i).}
\tag{D12}
\]

因为 D9 说明 \(\sum q_i v_i\) shifted degree \(<0\) 当且仅当每个非零 \(q_i\) degree \(<-\delta_i\)；basis 展开唯一。更一般，degree \(\le j\) 部分的维数是 \(\sum_i\max(0,j-\delta_i+1)\)。这个 Hilbert function 的 successive differences 恢复全部 \(\delta_i\)，故 degree multiset 不依赖约化路径或 basis normalization。

## 4. 辛自对偶迫使两整数 defect

令

\[
J_\nu=\begin{pmatrix}0&I_\nu\\-I_\nu&0\end{pmatrix}.
\]

由于 D2 对称，直接 block multiplication 给出

\[
\boxed{B_0J_\nu B_0^{\mathsf T}=P J_\nu}
\tag{D13}
\]

对 D4、D5 都成立。于是

\[
\beta(v,w)=vJ_\nu w^{\mathsf T}/P
\tag{D14}
\]

是 graph 模块上的 polynomial-valued unimodular alternating form。任意另一 basis \(B=U B_0\)，\(U\in GL_{2\nu}(F[u])\)，其 form matrix 为 \(U J_\nu U^{\mathsf T}\)，determinant 是非零常数。

对 weak-Popov rows，用 D6 的 paired bounds 有

\[
\deg\beta(v_i,v_j)\le\delta_i+\delta_j.
\tag{D15}
\]

证明：未除 \(P\) 的各项如 \(T_i A_j-A_i T_j\) 次数至多 \(\delta_i+\delta_j+b_T+b_A=\delta_i+\delta_j+N\)；其他 pair 同理。可被 \(P\) 整除由 D13 或 graph congruence 保证。若右侧为负，该 entry 必为零。

**Theorem D16（真实 defect 配对）。** Degree multiset 关于零对称。Scalar 存在唯一 \(d\ge0\)，matrix 存在唯一 \(0\le d_1\le d_2\)，使

\[
\delta_g=(-d,d),\qquad
\delta_{\mathcal N}=(-d_2,-d_1,d_1,d_2).
\tag{D16}
\]

证明：unimodular form matrix determinant 非零，故其 determinant 展开至少有一个非零 product，对应 permutation \(\sigma\)。每个非零 entry 的 polynomial degree 非负，结合 D15 迫 \(\delta_i+\delta_{\sigma(i)}\ge0\)。而其和为 \(2\sum_i\delta_i=0\)。所以每个 paired sum 都恰为零，存在 matching \(\delta_{\sigma(i)}=-\delta_i\)。排序后得到 D16。唯一性已由 D12 的 Hilbert function 证明。这里没有用 ambient unit 推截断 unit。

## 5. Defect 与实际 Gram kernel 的全尺度等价

**Theorem D17。**

\[
\boxed{\operatorname{corank}G_0=d,\qquad
\operatorname{corank}M_5=d_1+d_2.}
\tag{D17}
\]

特别两 unit 条件精确等价于 \(d=0,d_1=d_2=0\)。

证明：冻结 U23 说明 \(T\) 属于 kernel 当且仅当余式 \(A=\operatorname{rem}_P(gT)\) degree \(\le4r\)。这正好是 D3、D6 的 strictly negative shifted-degree 向量。这里 \(A\) degree \(<N\)，故从 \(T\) 恢复 \(A\) 唯一；\(T=0\) 时只能 \(A=0\)。因此两个 vector spaces 同构。Matrix 用冻结 U27：\(A,B\) 的 degree bounds 分别 \(4r,2r\)，都是 \(<N\)，故从 \((T,Q)\) 唯一恢复，亦没有 \((T,Q)=0\) 而后面分量非零的 bounded 向量。结合 D12、D16 得 D17。

此结果还给 kernel 的 explicit polynomial basis：取每个负 \(\delta_i\) 对应 row \(v_i\)，保留其前 \(\nu\) 个 coordinates，并乘 \(1,u,\ldots,u^{-\delta_i-1}\)。它们是全部 actual kernel 的基，不是只做 rank-count 的 formal certificate。

这是两 unit 问题的新有限 rank polynomial 接口。欲得无穷非零，仍须证明真实 \(\chi\)、D2、D6 下的三个 defect 在无穷 \(p=18r+1\) 上为零。

## 6. Scalar determinant 的 fixed principal subresultant

本节给 exact normalization，不依赖任何未核 subresultant convention。对任意 monic \(P\) degree \(N\)、\(g\) degree \(<N\)，把 \(g\) 的系数 padded 到 degree \(N-1\)。设 \(1\le e\le N\)。定义 \((2e-1)\times(2e-1)\) matrix \(\mathcal S_e(P,g)\)：

- rows 依次为 \(u^{e-2}P,\ldots,P\)，共 \(e-1\) 行；然后 \(u^{e-1}g,\ldots,g\)，共 \(e\) 行；
- columns 按 descending 次序取 \(u^{N+e-2},\ldots,u^{N-e}\) 的 coefficients。

令 \(\operatorname{psc}_{N-e}(P,g)=\det\mathcal S_e(P,g)\)。这与本轮实际读 D'Andrea–Krick–Szanto PDF3 的 padded definition 所取 principal coefficient 一致；即使 \(g\) 的 actual degree 较低，定义仍有效。

**Theorem D18（Hankel／PSC exact sign）。** 若 \(g/P\) 的负 Laurent coefficients 为 \(\ell_j\)，则

\[
\boxed{\det(\ell_{i+j})_{0\le i,j<e}
=(-1)^{e(e-1)/2}\operatorname{psc}_{N-e}(P,g).}
\tag{D18}
\]

证明：在 \(\mathcal S_e\) 中，P-row 的前 \(e-1\) columns 是 diagonal1 的三角 block。用这些 rows 消去每个 g-row degree \(\ge N\) 的系数，恰产生 \(\operatorname{rem}_P(u^j g)\)。余下 \(e\) columns 的 descending degree 是 \(N-1,\ldots,N-e\)。g-rows 原来按 \(j=e-1,\ldots,0\) 排列，与冻结 U21 的余式矩阵转置相差一次 row reversal，sign 是 \((-1)^{e(e-1)/2}\)。前面的三角 block determinant 为1，U21 的 Laurent 变换也为1，故 D18 精确成立。

对原 scalar 目标 \(e=r\)，

\[
\boxed{\det G_0=(-1)^{r(r-1)/2}
\operatorname{psc}_{4r+1}(P,g).}
\tag{D19}
\]

这把 scalar unit 变成一个确定的 principal subresultant 非零，不是 general resultant 非零。所读 primary PDF4–5 的 PRS theorem 说明何种 subresultant 可由 Euclidean remainder degrees 追踪，但不承诺 index \(4r+1\) 正常；它是算法和进一步求式的入口。

## 7. 全环境 determinant 的已知 unit 因子

令

\[
R=\operatorname{Res}(P,S)=\prod_{k=0}^{5r}S(k^2).
\tag{D20}
\]

由冻结 Wilson 恒等式，

\[
R=\prod_{k=0}^{5r}
\frac{(-1)^{r+k+1}}{(5r-k)!(5r+k)!}\in F^\times.
\tag{D21}
\]

这是每个 U1 素数都明确的 unit，不存在额外坏分母。对完整 degree \(<N\) 的 scalar moment matrix \(\widehat G\)，Cauchy–Binet/Vandermonde 给

\[
\boxed{\det\widehat G
=(-1)^{N(N-1)/2+N}\,2^{r-N}R^{-6}.}
\tag{D22}
\]

证明：weight 是 \(g(u_k)/P'(u_k)\)，Vandermonde 平方与 \(\prod P'(u_k)\) 的 sign 为 \((-1)^{N(N-1)/2}\)。而 \(\prod g(u_k)=(-1)^N2^{r-N}R^{-6}\)，因为 middle 恰有 \(r\) 个节点。

对完整两个 degree \(<N\) channels 的 \(2N\times2N\) Gram matrix \(\widehat M\)，同理

\[
\boxed{\det\widehat M=\prod_k\det\mathcal N(u_k)
=(-3)^N2^{4r+1}R^{-4}.}
\tag{D23}
\]

证明：两 channels 的 Vandermonde transform 给四次 Vandermonde determinant；local weight blocks 为 \(\mathcal N(u_k)/P'(u_k)\)，两个 derivative products 与 Vandermonde 正好抵消，sign 也平方消失。冻结 U20 给 local determinant \(-3(2-\chi_k)S(u_k)^{-4}\)，nonmiddle 共 \(4r+1\) 个节点。

因此 Jacobi complementary-minor identity 提供 actual determinant 的另一精确式：

\[
\det M_5=(-3)^N2^{4r+1}R^{-4}
\det\bigl((\widehat M^{-1})_{I^c,I^c}\bigr),
\tag{D24}
\]

其中 \(I\) 是第一个 channel 的 degrees0..r-1及第二个的0..3r-1。因 principal minor，不另加 sign。D24 只把 unknown 放到真实 dual complementary profile，未证明该 minor unit；不能删去它，也没有提升成新的 all-finite-place 费用。D22/D23 的 ambient 全部正常与 D17 的 critical profile 正常仍是不同命题。

## 8. 实际数据的 nonperfectness 反例

取 \(r=2,p=37,a=10,N=11\)。从冻结 Wilson 或内部 ratio，\(s_k=S(k^2)^{-1}\) 满足

\[
s_0=4,\qquad s_{k+1}=-s_k(11+k)/(10-k).
\]

逐次 field 运算得到表；所有条目都保留真实 middle multiplicity \(\mu_0=1,\mu_1=2,\mu_k=1\) 对 \(k\ge2\)：

| \(k\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| \(s_k\) | 4 | 3 | 33 | 25 | 24 | 14 | 7 | 35 | 12 | 34 | 23 |
| \(\mu_k s_k^5\) | 25 | 5 | 12 | 30 | 2 | 29 | 9 | 5 | 7 | 16 | 8 |

证明 \(s_0=4\)：\(10!\equiv25\)，\(18!^2\equiv-1\)，故 \(S(0)=-1/(10!)^2=28\)，inverse为4。其余由 displayed ratio 直接核得。权重和是 \(148\equiv0\pmod{37}\)。first \(u\)-moment 是 \(12\)。

于是同一真实 scalar moment sequence 的 size1 determinant 为0，而其原目标 size2 determinant为

\[
\boxed{\det G_0\big|_{r=2,p=37}=-12^2=4\ne0.}
\tag{D25}
\]

这不是改变 \(\chi\) 或新的 toy measure。它明确反驳“实际数据是 perfect／所有低阶 Hankel minors 均 unit”的过强命题。不能用一个依赖所有 intermediate points 正常的 perfect-path OP/Padé theorem，循环证明原目标正常。反例也不反驳原两个 target unit 或无限 subsequence 的可能性。新的 module reduction 可以正确跨过该 singular intermediate profile，而无须把它排除。

## 9. Primary sources 的准确适用范围

NEW 两份原件在 literature/cdt_paired_auxiliary_pade_sources_20261006 正常 verified TLS 归档；没有 certificate bypass。准确URL、哈希、页数、阅读范围在独立receipt。

- Beckermann–Labahn，[Fraction-free computation of matrix rational interpolants and matrix GCDs](https://cs.uwaterloo.ca/~glabahn/Papers/exact.pdf)，31页，实际完整读PDF1–15。PDF9–10区分 normal point 与 controllable data；PDF11–14的 Mahler system/leading-degree equivalence，以及PDF14–15 perfect-path递推，有明确非零前提。论文的一般机制允许处理singular subproblem，不提供本问题的normality定理。本稿D8–17已给field polynomial module的自足证明，未借未知intermediate norm。
- D'Andrea–Krick–Szanto，[Subresultants, Sylvester sums and the rational interpolation problem](https://arxiv.org/pdf/1211.6895v3)，14页，实际完整读PDF1–8。PDF3的monic padded definition和PDF4–5的PRS/重建非零条件，给D18–19的正确convention；没有把gcd(P,g)=1当成所有principal coefficients非零。PDF8的determinantal interpolation还保留非零条件。没有称已读其PDF9以后的证明。

这两篇是求式、跨singular profile和低rank多项式计算的真实参考；没有文献承诺 D17 的三个 defect 在本辅助素数族同时为零。

## 10. NEW first-only 机制探针与下一证明门槛

自有 research/cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006_verify.py 首次且唯一执行一次，退出码0；输出同stem JSON。没有读取/import旧/同行producer，程序只用stdlib pathlib/json/hashlib。执行命令直接调用该NEW脚本；输出存在guard拒绝重跑。

只选以前已研究的 \(r=1,2,4,6,7\)，没有扩大prime表。它重新从真实节点和权重构造g/c/h，验证Fermat因式，实施rank2/rank4 weak-Popov约化，检查graph congruences、symplectic divisibility/degree bounds、corank公式、scalar PSC sign及PRS degree flag。另检查邻近degree profiles，诊断对象均标明actual_profile或非target。共14个scalar profiles、42个matrix profiles；五个actual profiles均balanced；\(p=37\) 的非target scalar size1 profile为 \((-1,1)\)，亏秩1，与D25吻合。

Saved PY和完整JSON已经真实完整静态回读，未重跑。有限机制验证不是D8–24全尺度证明的替代；更不证明无穷primes、全部r或新的数值定理。邻近profile的结果不能免费移回原目标，也没有继承原目标的费用/解析估计。

本轮下一实质门槛已经具体化：求 D19 的 index \(4r+1\) principal coefficient 的无穷非零，或在D2/D6的真rank4 graph module中构造一个适用于无穷 \(p=18r+1\) 的 weak-Popov basis，证明四个shifted row degrees全为0。D13的辛结构将可能失败浓缩成两个非负整数，但不自行使其消失。任何证明必须说明真实 \(\chi\) 和half jet为何强制临界平衡，不能只证明ambient form或index非退化。
