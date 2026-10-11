# 原配对矩阵的部分子式：有限处转移、无限非零与复Gram解析接口

2026-10-07，NEW，root。当前authority为main §§156–160及delivery_shallow_joint快照222765c5；548冻结记录仅读。本文纯纸证，不执行/import/rerun数学producer，不扩辅助素数表。原B6/k3/s5、degree<3n、rank2n饱和配对格和真实源ξ=αζ4+βζ5（β≠0）保留。取得的是同一原矩阵部分子式的明确接口和6r子式的无限非零，尚非新特殊值无理性结论。

## P1. 原矩阵与全有限处的部分子式整模型

实际全文读取冻结[lattice I1–I25](cdt_odd_paired_head_free_integral_lattice_20261006.md)、[local Gram G1–G15](cdt_odd_paired_actual_local_gram_layers_20261006.md)、[source S1–S14](cdt_odd_paired_source_radical_response_20261007.md)、[coupled C1–C23](cdt_odd_paired_coupled_gram_decay_20261007.md)及[shallow T1–T7](cdt_odd_paired_source_shallow_rank_20261007.md)。合并读coupled后半有总输出截断，随后单独补完整后半；不将截断当全文。CDT作者2026有效holonomy原件本轮实际PDF3–5三页，实际函数独立秩和分母/单值叶条件仍须另接。

令m=2n，S为原饱和整数值格的完整整数基，B_n(X)=SᵀH_N(X)S，而D_A(X)=detB_n(X)。I_d(B)为全部d阶minors生成的分式理想，C_d(B)为按同一d-subsets排列的compound矩阵。对固定整数α、β，β≠0，实际entries由冻结G3给

\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
U_j=-8\alpha H_j^{(3)}-6\beta H_j^{(4)},\quad
V_j=C_jU_j+24(X-\alpha H_j^{(4)}-\beta H_j^{(5)}).
\tag{P1}
\]

置E_p=floor(log_p(8n))。整数值P在整数节点取整值，Newton微分式使v_pP'≥−E_p；harmonic阶e的valuation≥−eE_p。因此U·(PQ)'和V·PQ皆≥−5E_p。S的整数系数不使该界变差。

对p>6n，Newton导数、U及短harmonics皆整；唯一长harmonic H_(2n+j)若含p，则2n+j≥p且j<p、2n<p，binom(2n+j,j)^3含至少p³，清除C_j的至多一个p⁻¹。故B_n(X)在p>6n属Mat_m(Z_p[X])。全部2、3和小prime亦由E_p界覆盖。于是对任何1≤d≤m，

\[
Q_{n,d}:=\prod_{p\le6n}p^{-5dE_p},\qquad
C_d(B_n(X))/Q_{n,d}\in\operatorname{Mat}_{\binom md}(\mathbf Z[X]).
\tag{P2}
\]

这是同一所有minors的保守完整整模型，未使用完整det的较好40.3145预算。若固定c∈Q、M为其分母，entries affine inX使每个minor degree≤d，故M^d C_d(B_n(c))/Q_(n,d)整数。固定有理sources先清同一个固定分母，费用O(d)，不随n变源。

由θ(t)∼t，Σ_(p≤6n)floor(log_p(8n))logp=6n+o(n)（第二及更高prime powers为o(n)），因此d/n→λ时

\[
-\log Q_{n,d}/n^2\longrightarrow30\lambda.
\tag{P3}
\]

这是粗safe upper fee：6r阶为45、7r阶为105/2，不是最小费用、成本下界或方法no-go。仍可用真实residue/Plücker支持改善。

## P2. 真实归一化向原7r子式转移，支付strong/weak权重

取n=4r、p=18r+1素数，避固定source分母及β，α,c∈Z_p。冻结实际局部GL基满足

\[
p^5B_n(X)=D_pN(X)D_p,\quad
D_p=\operatorname{diag}(1^{5r},p^{3r}).
\tag{P4}
\]

I_d在左右Z_p-GL变换下保持，因此这里的原B理想就是固定整数basis的理想。对每个d-row/column集合I、J，令w(I)为其中weak坐标数；准确

\[
\det(p^5B)_{I,J}=p^{w(I)+w(J)}\det N_{I,J}.
\tag{P5}
\]

若d=7r，则2r≤w(I),w(J)≤3r。对每个源a不在冻结T3明确的≤rankG_K个例外剩余类中，T6给η=v_p I_7r(N)=(k−r)^+。全部N-minors皆≥η，且至少一个达到η，所以

\[
\boxed{\eta-31r\le v_p I_{7r}(B_n(c))\le\eta-29r.}
\tag{P6}
\]

下界保证全部minors的局部整化，upper保证至少一个原7r minor非零；不能将其相等化，也不能声称minimal N-minor必只选2r weak方向。P6只改变该单一p≈n处O(nlogn)定标，未产生n²新算术信用。

## P3. 较低6r外幂自动给固定源的无限非零

另取d=6r。leading N=6βA5有rank8r−k≥6r，故对所有α,c∈Z_p都有v_p I_6r(N)=0。此时r≤w(I),w(J)≤3r，P5给

\[
\boxed{-28r\le v_p I_{6r}(B_n(c))\le-24r.}
\tag{P7}
\]

**推论。** 对每个固定有理α、β,c且β≠0，存在无限n=4r，使原B_n(c)有一个6r阶minor非零。证明：Dirichlet定理给无限p≡1 mod18；排除β和固定分母的有限prime后均适用P7。局部GL及D_p在Q_p中可逆，故该原矩阵characteristic0的rank≥6r。n随这些prime增长，源α、β和c保持固定，未使用每p改源或新的单位实验。

P7不证明7r、完整8r行列式无限非零；它把较低阶路线的非零缺口确切闭合。若假设实际ξ=c∈Q，才可同时用下文真实轮廓估计这个相同B_n(c)。矩阵rank≥6r也不是CDT定理中的独立函数个数；必须另接实际函数/周期投影，不能把3n/2代入CDT的m。

## P4. 所有部分子式的复Gram上界与精确compound表示

在原实际整数basis中，冻结轮廓式于X=ξ给

\[
B_{ij}=\int g_i(z)g_j(z)d\mu(z),\qquad
P_{ij}=\int g_i(z)\overline{g_j(z)}d\nu(z),\quad d\nu=|d\mu|.
\tag{P8}
\]

原指数tail保证绝对可积，P>0。对每个d-subsets I,J，Andreief展开和Cauchy–Schwarz准确给

\[
\boxed{|\det B_{I,J}|\le\sqrt{\det P_{I,I}\det P_{J,J}}.}
\tag{P9}
\]

证明：混合minor为1/d!的d-fold determinant积分；取total variation后，两个determinants在同一个L²(ν^d/d!)中Cauchy–Schwarz，各平方范数由Hermitian Andreief恰为相应positive principal minor。没有假设complex B或其未知block非退化。

令e_d(P)=Σ_|I|d detP_(I,I)，则

\[
\|C_d(B)\|_F\le e_d(P),\qquad
e_d(P)=\frac1{d!}\int\sum_{|I|=d}|\det[g_i(z_j)]_{i\in I}|^2\prod_jd\nu(z_j).
\tag{P10}
\]

也可用冻结C23的phase compression B=P^(1/2)TP^((1/2)T)、||T||≤1，得到

\[
\|C_d(B)\|_{op}\le\lambda_1(P)\cdots\lambda_d(P)\le e_d(P).
\tag{P11}
\]

其中λ按递减排列。只有d=m时右侧才是detP；d<m须估e_d或最大d个eigenvalues。完整det衰减界不能直接继承给部分子式。

## P5. det1剪切在部分外幂中并不免费

设冻结q剪切T_q满足detT_q=1，\widetilde B=T_qᵀBT_q。Cauchy–Binet给

\[
C_d(B)=C_d(T_q^{-T})C_d(\widetilde B)C_d(T_q^{-1}).
\tag{P12}
\]

从P10–11的同一新positive Gram \widetilde P得到

\[
\max_{I,J}|\det B_{I,J}|
\le\|C_d(T_q^{-1})\|_{op}^2 e_d(\widetilde P).
\tag{P13}
\]

若q为有理配置，在有限处另有v_p I_d(B)≥v_p I_d(\widetilde B)+2min v_pC_d(T_q⁻¹)。detT_q=1只在完整d=m时使这些compound因子都等于1。比如2阶shear [[1,p⁻ᴴ],[0,1]]虽det1，C1的minimum valuation为−H。它说明不能沿完整det剪切恒等式免费移走部分minor的basis费用；未声称实际q剪切必有此大小。

## P6. 无理性矛盾所需的同对象门槛

假定ξ=c∈Q。若在无限适用n上有非零d-minor，并有同一所有minors的signed scale q_(n,d)>0满足M^d C_d(B_n(c))/q_(n,d)整数，则某nonzero minor绝对值≥q_(n,d)/M^d。若同时对全部相同minors证明

\[
\liminf n^{-2}\log q_{n,d}\ge-A_d,
\qquad
\limsup n^{-2}\log\max_{I,J}|\det B_n(\xi)_{I,J}|\le-C_d,
\quad C_d>A_d,
\tag{P14}
\]

就产生严格矛盾。P7已无条件补6r路线的无限非零，P2补粗全有限处整模型；P10–13给其真正应估的解析对象。当前尚未证明这个e_(6r)的充分衰减，更没有strict P14。7r路线仍另需同一固定source的无限避例外。

本轮的新进展是P6/P7对原矩阵的实际valuation区间、较低外幂的fixed-source无限非零、同一全部minors的完整粗整化及真正compound Gram/剪切接口。不是CDT函数独立秩或新的ζ/L/Catalan无理性/LI，未Lean形式化。下一步应保留actual partial low/high结构估P10，或用真实函数投影建立另一有更好阶梯成本的holonomy系统；不能只调finite roots并宣称所有门槛已闭合。正式独审及最终回读另存，不提前声明完成。
