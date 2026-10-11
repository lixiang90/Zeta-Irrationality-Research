# 真配对格的 unit-tail 支撑相关整化与新的实付算术主率

2026-10-06；quarter_actual_rank。NEW 数学稿，供全文独审，尚未提前冻结。旧455数学输入及全部旧/同行 producer 仅读，不执行、import 或重跑。本文固定原 B6/k3/s5、degree<3n、rank2n 的实际配对饱和整数值格；不借恢复四重零点布局或原 full3n determinant。

## C1. 对象、已有费用与本轮定理

令 f_i(t)=binom(t−1,i)、0≤i<3n，M_{3n}=⊕Zf_i。A_Z⊂M_{3n} 为冻结稿中的真实 rank2n 饱和配对格，完整基为 G_1,…,G_n,f_{2n},…,f_{3n−1}。其配对条件仍是 P(m)/d_m=P(2n+1−m)/d_{2n+1−m}，d_m=(m)_{6n+1}；没有改格。对固定 a,b∈Z、b≠0，令

\[
D_A(X)=\det[\Lambda_X(g_i g_j)]_{1\le i,j\le2n}\in\mathbf Q[X],
\tag{C1}
\]

Λ_X 是冻结 arithmetic A3–A4 的 s5/B6/k3 部分分式泛函。固定有理 sources 先清公共分母，有限/实处同付 O(n)，不改变 n² 主率。X 是形式变量，以下控制其全部系数。

当前冻结安全费用为

\[
A_{\rm old}^{safe}=\frac{790225879771}{17925027120}.
\tag{C2}
\]

本稿实际完整回读冻结 credit-cap S1–S10/S1–S17（8b736…37b0）、budget B1–B22（55278…12dc）、arithmetic A1–A14（含A30a）。首次合并读取的 analytic/CRT 输出发生总量截断，已分别重新完整读取 analytic R1–R6 与 CRT sections1–6/R1–R21（3265…bd33）；不将截断输出称完整阅读。没有运行其 producer。

设 p≤n 为 prime 且 p²>8n，写

\[
3n=Qp+R,\quad 0\le R<p,
\qquad r_2=2n\bmod p,\quad r_6=6n\bmod p,
\]
\[
u_p=\min(r_6+1,p-r_2),\qquad
k_p^0=[2n-Q u_p-\min(R,u_p)]_+.
\tag{C3}
\]

则在同一个实际 determinant 上有全 n、全 X 定理

\[
\boxed{v_p^{Gauss}D_A(X)\ge-10n+2k_p^0.}
\tag{C4}
\]

这是 support-dependent 的真实改善：unit-W tail 所见的 polynomial 维数与 ragged layer 一起进入格，而不是先独立取共同 monomial-minor 最坏值和最大 factorial 费用。下文自证 C4 所需输入。两侧 weak-jet 格因式分解是本轮 toric 同伴所推进的共同 DND 接口；本稿不冒认其 n<p≤2n 的配对精确核结论，只处理 p≤n 的 degree/support 上界和费用。未用其尚未读到的新稿作为定理来源。

仅在 p/n∈[1/4,1] 兑现 C4，其他 places 保留冻结合法界，得到

\[
\boxed{\Delta A_C=\frac{20948066064530861}{14991578506784880}>1.397,}
\]
\[
\boxed{A_C^{safe}=\frac{45711182732576087}{1070827036198920}<42.689.}
\tag{C5}
\]

它是新的安全费用上界，非 actual content 等式或 actual cost 下界。无限 rational-target nonzero、strict margin 和特殊值结论尚未成立。

## C2. 保留实际 degree cutoff 的整数值 ψ 基

取 ψ(t)=(t^p−t)/p。对 i=i_0+pi_1<3n，0≤i_0<p，定义

\[
b_i(t)=\binom t{i_0}\binom{\psi(t)}{i_1}.
\tag{C6}
\]

因为 i<p²、i_1<p，ψ(Z_p)⊂Z_p，而 i_0!,i_1! 都是 units，b_i 在 Z_p 上整数值。有限差分在 0,…,i 上展开到 binom(t,j)，系数全属 Z_p。最高项与 binom(t,i) 的比为 i!/(i_0!i_1!p^{i_1})，其 valuation=floor(i/p)−i_1=0。故 degree<3n 的整个基变换是 GL_{3n}(Z_p)，再与 t→t−1 的整数 unitriangular 变换合并，正是原 M_{3n}⊗Z_p。它不是普通 integer-coefficient CRT image，也不是增加高 jet 的格。

模 p 可把一个多项式写成局部 low-digit/ψ 表达

\[
P=\sum_{\ell=0}^{Q-1}F_\ell(t)\binom\psi\ell
 +F_Q(t)\binom\psi Q,
\quad \deg F_\ell<p,\quad\deg F_Q<R.
\tag{C7}
\]

当 R=0 时最后项不存在。F_ℓ 可取 low binomial basis；degree<p 的这些函数在全部 p 个 residues 上的 evaluation 为 Vandermonde GL_p(F_p)。顶层只在 degree<R 空间中取值，不能把每个 residue 都独立补一个顶层参数。

饱和 A_Z 是 M_{3n} 的 direct summand，因此 A_Z/pA_Z 实际单射到这个 ambient mod-p 空间，维数准确为2n。以下只给其特定支撑 restriction 的秩上界，未假定配对条件在 ψ 坐标下无代价。

## C3. valuation-leading unit-W residues 的准确集合

实际系数是

\[
W_j=\binom{6n}j^2\binom{2n+j}j^3,\quad
U_j=-8a H_j^{(3)}-6bH_j^{(4)},
\]
\[
V_j(X)=C_jU_j+24\{X-aH_j^{(4)}-bH_j^{(5)}\},
\quad C_j=5H_j-3H_{2n+j}-2H_{6n-j}.
\tag{C8}
\]

For j=ρ+lp、0≤ρ<p，large-prime Legendre identity 给

\[
w_\rho=v_p(W_j)
=2\mathbf1_{\rho>r_6}+3\mathbf1_{\rho\ge p-r_2}
\in\{0,2,3,5\}.
\tag{C9}
\]

这里 r_2=0 时第二个条件没有解。于是 unit-W residues 准确为

\[
\mathcal U_p=\{0,\ldots,\min(r_6,p-r_2-1)\},
\quad|\mathcal U_p|=u_p.
\tag{C10}
\]

ρ=0 与 r_6=0 的端点已包含，不能把 u_p 换成连续长度后遗漏一个 actual residue。每个 unit residue 的 tail 节点为 j=ρ+lp，1≤l≤h=floor(6n/p)，而 h≥2Q≥Q+1，因为 Q≥3。p²>8n 又保证 h<p，所以这些 l 在 F_p 中确实互异。

## C4. unit-tail 全局支撑与 ragged 顶层的准确 image cap

对 a∈Z、Y∈Z_p，直接二项展开给

\[
\psi(a+pY)\equiv\psi(a)-Y\pmod p,
\qquad p\psi'(t)\equiv-1\pmod p.
\tag{C11}
\]

在 t=−ρ−lp 处，C7 的局部 ψ polynomial 度数≤Q，在 h≥Q+1 个不同的 ψ-values 上取值。故全部 unit-tail evaluations 模 p 为0，当且仅当每个 ρ∈U_p 的完整局部 polynomial 为0。此时其 ψ-derivative 亦0；low-digit factors 的导数乘 p 为0，故 pP' 在同一 tail 节点也为0。这里并未以单点 eval 为0推出导数为0，而是用实际度数和足够多不同 lift 节点。

每个完整低 layer 的 restriction 在 u_p 个不同 residues 上秩 u_p；共 Q layers。顶层 evaluation 在 degree<R polynomials 中秩 min(R,u_p)，因为相应 Vandermonde 的任意合法阶 minor 是 p-unit。不同 ψ powers 独立。因此 ambient unit-tail restriction 的秩准确为

\[
d_p^{amb}=Q u_p+\min(R,u_p).
\tag{C12}
\]

由 actual rank2n 子空间的基本线性代数，其 restriction 核维数 k_p≥k_p^0。并且这个核也是 whole unit-tail jet map

\[
P\longmapsto(P(-j),pP'(-j))_{j\in\text{unit tails}}
\tag{C13}
\]

的核。没有计算 kernel 的 exact paired dimension，也没有借 ambient kernel 的自由基冒充 actual lifts；只用在原饱和格中的 k_p^0 维真实 mod-p 子空间，再取实际 Z_p 格的 lifts。

## C5. actual weak 格两侧因式分解，控制 whole X

在所有 integer-valued P∈M_{3n}⊗Z_p 上，P(z)、pP'(z)∈Z_p 对整数 z 成立。后者亦可直接从冻结有限差分导数式和 i<3n<p² 得到，不能删去导数的一层 p。

在 tail j=ρ+lp、l≥1，v_p(U_j)≥−4、v_p(V_j)≥−5；在 head j=ρ，U_ρ integral、V_ρ(X)≥−1，逐 X 系数成立。于是 p⁵Λ_X(PQ) 在 jets (P,pP') 中的 node block 是

\[
W_j\begin{pmatrix}p^5V_j(X)&p^4U_j\\p^4U_j&0\end{pmatrix}.
\tag{C14}
\]

unit-tail block integral；nonunit-W tail block 被 p² 整除；全部 head block 被 p⁴ 整除。这是完整 valuation-leading sector，而不是仅考察某个裸 evaluation 或某一个 X specialization。

在 A_Z⊗Z_p 中取 GL_{2n}(Z_p) 基，其最后 k_p^0 个向量模 p 位于 C13 的真实核。因为 A 是饱和格，这些独立 mod-p vectors 可扩成实际局部 unimodular 基，所有 lifts 保留原 degree<3n。弱/强 pair 的 unit-tail 项至少带 p，弱/弱项至少带 p²；nonunit-tail 与 head 即使不靠弱 jets 也满足这些费用。因此此实际基上

\[
p^5 B_A(X)=D\,N(X)\,D,
\quad D=\operatorname{diag}(1^{2n-k_p^0},p^{k_p^0}),
\quad N(X)\in\operatorname{Mat}_{2n}(Z_p[X]).
\tag{C15}
\]

局部 GL 基的 determinant 是 unit，故不会改变原 D_A 的 Gauss valuation。取 determinant 得 C4：p⁵ scaling 的费用为10n、两侧 D 的信用为2k_p^0。未使用 Gram 非退化、任何未知 finite-field unit、exact Smith 或 target nonzero。这是同一个实际整格的 finite-place identity；没有把此 GL 基的实数范数免费换进旧解析界。

## C6. 连续 support 下界与实际 floor 边界

设 x=p/n∈[1/4,1]，令

\[
a=\lfloor2/x\rfloor,\quad h=\lfloor6/x\rfloor,
\quad Q=\lfloor3/x\rfloor,
\]
\[
U(x)=\min(6-hx,(a+1)x-2),\quad R(x)=3-Qx,
\]
\[
\kappa(x)=[2-Q U(x)-\min(R(x),U(x))]_+,
\quad g_C(x)=-10+2\kappa(x).
\tag{C16}
\]

实际 r_6=n(6−hx)、r_2=n(2−ax)，u_p=min(r_6+1,p−r_2)。因此 |u_p−nU(x)|≤1 完整覆盖 p|2n、p|3n、p|6n，不删除 floor 跳点；Q≤12，R actual=nR(x)。C3 与 nκ(x) 的误差≤Q+1≤13 是 uniform。故 C4≥n g_C(p/n)−26。

冻结 g_old 在 [1/4,1/2] 准确为−10；在 (1/2,1)，它为冻结 S6 的12 raw rows加实际第一层 tent 信用后与−10取max。这与普遍 capacity bound 的 paid模型相同，额外 M4/subhalf 信用被隐藏。令

\[
\Delta g_C=\max(g_{old},g_C)-g_{old}\ge0.
\tag{C17}
\]

在每个 finite floor type 的开区间，这些函数都是有限 affine branches 的 min/max；全部可能 branch pair 的 crossing roots 加入后，完整闭 affine cover 可准确积分。这里的单侧 endpoint 值只为证明该 branch 的整个闭 interval；floor 原函数在跳点的另一侧值可不同。实际 prime 的所有边界由上述 uniform 误差处理，PNT 也不依赖 finite 个连续跳点的值。

## C7. 一个无需证书的完整正 window

若 4/7<x<3/5，则 a3、h10、Q5，U=6−10x、R=3−5x=U/2。所以 κ=55x−31，g_C=110x−72。旧 g_old 在这个完整 window 是−10，故

\[
\Delta g_C(x)=110x-62,\qquad
\int_{4/7}^{3/5}\Delta g_C dx=\frac{17}{245}>0.
\tag{C18}
\]

这已独立给全尺度正费用改善，未从有限证书推定定理。C8给同一区域之外的完整计算，收益更大。

## C8. 完整 paid cover 与精确有理面积

合并相邻相同 affine gain 后的全部47段如下；各行表示 gain=A x+B。包含零段，完全覆盖 [1/4,1]，没有选择有限参数 q 后外推。

|left|right|A|B|
|---|---|---:|---:|
|1/4|8/31|−192|52|
|8/31|6/23|552|−140|
|6/23|5/19|−192|52|
|5/19|4/15|−154|42|
|4/15|3/11|506|−134|
|3/11|64/231|0|0|
|64/231|2/7|462|−128|
|2/7|5/17|−154|48|
|5/17|8/27|−120|38|
|8/27|3/10|420|−122|
|3/10|4/13|−140|44|
|4/13|6/19|380|−116|
|6/19|55/171|0|0|
|55/171|1/3|342|−110|
|1/3|8/23|−108|40|
|8/23|6/17|306|−104|
|6/17|5/14|−108|40|
|5/14|4/11|−80|30|
|4/11|3/8|272|−98|
|3/8|23/60|0|0|
|23/60|2/5|240|−92|
|2/5|5/12|−80|36|
|5/12|8/19|−56|26|
|8/19|3/7|210|−86|
|3/7|4/9|−70|32|
|4/9|6/13|182|−80|
|6/13|37/78|0|0|
|37/78|1/2|156|−74|
|1/2|8/15|−48|28|
|8/15|34/63|132|−68|
|34/63|6/11|69|−34|
|6/11|5/9|−48|28|
|5/9|4/7|−30|18|
|4/7|3/5|110|−62|
|3/5|28/45|0|0|
|28/45|2/3|90|−56|
|2/3|7/10|−69|50|
|7/10|5/7|−29|22|
|5/7|8/11|−15|12|
|8/11|14/19|−4|4|
|14/19|3/4|34|−24|
|3/4|4/5|−24|20|
|4/5|23/28|56|−44|
|23/28|14/17|0|2|
|14/17|6/7|34|−26|
|6/7|19/21|0|0|
|19/21|1|42|−38|

由每段 primitive integral A(right²−left²)/2+B(right−left)相加，得到

\[
\int_{1/4}^{1/2}\Delta g_C dx
=\frac{50758917992603}{97347912381720},\qquad
\int_{1/2}^{1}\Delta g_C dx
=\frac{1207739527}{1378848240}.
\tag{C19}
\]

总和正是 C5。与上轮 subhalf capacity 的零收益不同，此处的正收益来自 actual form 支撑与整数值格 degree/ragged layer 同时保留，并没有把旧裸 Smith 信用重复积分。

## C9. 全素数 signed 整化与 PNT，不假设非零

在 p≤n,p²>8n 的 places，把旧全系数整数下界 ℓ_p^{old} 与 C4 取max；其他 primes保持旧下界。其整数 signed ratio Q_n^C 仍满足

\[
D_A(X)/Q_n^C\in Z[X].
\tag{C20}
\]

为 C5 的预算只在 n/4≤p≤n 兑现新界，其他places旧付费不变。冻结旧模型到实际 valuation 的 uniform O(1) 和 C6 的 uniform误差给 local合法下界 n max(g_old,g_C)−C；该window与旧 n<p≤2n、3n<p≤6n的收益不交，所有旧费用完整保留。bounded piecewise affine PNT 测试函数论证于是给

\[
\liminf n^{-2}\log Q_n^C
\ge-A_{old}^{safe}+\int_{1/4}^{1}\Delta g_C dx=-A_C^{safe}.
\tag{C21}
\]

p≤sqrt(8n)处原有限整化付 O(n^{3/2}log n)，p<n/4处保持旧safe界；不需要计算无限 floor tail 的新积分。固定 rational X=c的 denominator付 exp(O(n))。C20–C21本身不推出 D_A(c)无限nonzero或 strict margin。

## C10. FIRST-ONLY 证书、实际读取与下一接口

自有 NEW `cdt_odd_paired_support_correlated_budget_20261006_verify.py` 保存后完整静态读源码，输出不存在检查通过，首次且唯一执行1次，exit0 PASS，无失败或rerun。它只用 stdlib Fraction，literal录入原12 raw rows，不读取/import/执行任何旧或同行 producer或数据文件。source SHA cd659ad52bad2d829bcbe9ec0c54812f3c238b00559f8e4aef6a4df337e31153；JSON SHA6db2c221a8e19496eda0005ce1ac4918d53dfb4e103f46d57f54fee51401f2f0。

程序枚举全部24 floor/base intervals，并对每个 type 生成所有可能 U、ragged、κ、old tent/cap、sector 的 affine branches，插入这些 branch pairs 的全部 crossing roots。得471个闭 affine pieces、4715项 exact endpoint/cover/integral checks，421pieces的积分为正。中点只选择在已完整分割的 interval 上的固定 branch，不作为未知函数外推的证据。它不是finite prime experiment，也不证明 C4 的实际格输入。

成功后实际 parse 整个JSON，读取全部metadata、合并后的47 gain rows和首尾完整records；未声称逐条人工重新计算471个interval。数学proof与实际静态source提供全覆盖依据，JSON保存全部branch字段以供独审。后续不编辑已成功source/JSON，不执行第二次。没有新PDF/外部源码/HTML下载、外部Lean执行。来源NEWreceipt另存；最终author/peer阅读与指纹待独审定稿后冻结。

本轮的具体已证候选是 C4 的 actual whole-X 支撑估值和 C5/C21 的严格paid主率改善。无限nonzero及仍大于解析率的fee缺口保留。下一步可以把 nonunit W=2/3/5 sectors 的层级权重与同一degree/ragged support再一起计入，而不是继续在 Λ_p−2T_p 上独立取最坏值；该高层 weighted optimization由root本轮另外推进，本稿不提前继承其待审费用。
