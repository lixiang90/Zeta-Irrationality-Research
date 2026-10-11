# 原6r部分外幂的完整节点整模型：安全费用45降至41

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。本轮 authority 为 main §§161–165及 `cdt_odd_delivery_partial_global_20261007.json`，SHA `f72fe28cbb874cedbb3e1e20b840d86f2ebd9e37ff7da1632364b9e04cb6729c`；556既存冻结记录保持只读。实际已读这些进展段落，完整 JSONparse审计并读其头部，不宣称逐条人工全文读556记录。实际 FULL 回读 partial P1–P14、lattice I1–I25、all-prime B1–B22、mixed arithmetic A1–A14含A30a及 actual-local G1–G15。所有 producer只读，不创建、execute、import或rerun；新prime/辅助单位表扩展0。

唯一新研究主稿保留原B6/k3/s5、原饱和整数值格、degree<3n、原 B_n(X)及同一固定源。新结论是全部6r阶子式的完整整化模型及安全n²费用upper41；不是完整det费用的移植，不使用 normalized矩阵的免费定标，也不是实际最小费用或其lower。

## 1. 原对象、全部子式与新整化结论

取 n=4r，r≥1，d=6r=3n/2。原空间 A_(n,Z)的rank2n完整整数基仍为
\[
G_m=p_mL_m+q_mL_{2n+1-m}\quad(1\le m\le n),
\qquad f_i(t)=\binom{t-1}{i}\quad(2n\le i<3n),
\tag{N1}
\]
其中 primitive pair和cardinal L_j准确沿冻结 lattice I4–I8。记这些basis polynomials为P_1,…,P_(2n)，S为它们在原Newton基中的整数矩阵。原矩阵
\[
B_n(X)=[B_X(P_i,P_j)]_{i,j=1}^{2n},
\quad B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-8\alpha H_j^{(3)}-6\beta H_j^{(4)},\quad
V_j(X)=C_jU_j+24\{X-\alpha H_j^{(4)}-\beta H_j^{(5)}\}.
\tag{N2}
\]
先取固定整数α、β，β≠0，X为形式变量。v_p指Q[X]的Gauss valuation；I_d为原全部d阶minors的分式理想，C_d为同一d-subsets排列的compound矩阵。

**Theorem N3。** 下文N11定义的全部素数尺度 Q_(n,d)满足每个r≥1的
\[
\boxed{C_d(B_n(X))/Q_{n,d}\in
\operatorname{Mat}_{\binom{2n}{d}}(\mathbf Z[X]),
\qquad\lim_{r\to\infty}\frac{\log Q_{4r,6r}}{(4r)^2}=-41.}
\tag{N3}
\]
这是该显式安全尺度的准确主率，未宣称实际 I_d内容等于它。固定有理α、β,c的完整分母和非零lower另在第6节支付。原6r无限非零沿冻结partial P7保留，不需每prime改源。

## 2. 只有p>3n才使用原basis的p整节点分解

冻结 partial P1–P3已证明：E_p=floor(log_p(8n))时，所有entries的Gauss valuation≥−5E_p，p>6n时全部entries为p整。它们覆盖全部小prime、2、3及长harmonic分母；本文在p≤3n和p>6n完全保留这些已证界。

现在固定3n<p≤6n。n=4r≥4使p>5、p²>8n。每个P_i degree<3n<p；原Newton所有i!为p-unit，而S为整数矩阵。因此原basis的monomial coefficients、任意整数节点的values及ordinary first derivatives皆属于Z_p。没有使用monomial变换时尚未付的factorial，也没有切换格。

定义2n×2(6n+1)的真实节点矩阵Y，其第j对columns为P_i(−j)、P_i′(−j)，并置
\[
A_j(X)=
\begin{pmatrix}W_jV_j(X)&W_jU_j\\W_jU_j&0\end{pmatrix},
\qquad A(X)=\operatorname{diag}(A_0,\ldots,A_{6n}).
\]
\[
\boxed{B_n(X)=Y A(X)Y^t,\qquad Y\in\operatorname{Mat}(\mathbf Z_p).}
\tag{N4}
\]
这是同一个实际form的literal身份。两个普通Cauchy–Binet展开保证：若全部d阶A-minors有共同Gauss lower ℓ，则原全部d阶B-minors也≥ℓ。Y可以退化；论证不假设某个评价minor为unit或非零。

## 3. 每个真实2×2节点block的全部阶估值

置e=6n−p，0≤e<p，写j=ρ或p+ρ。Legendre第一层给
\[
v_pW_j=2\mathbf1_{\rho>e}+3\mathbf1_{\rho\ge p-2n}.
\tag{N5}
\]
tail只有p+ρ、0≤ρ≤e。因此其weight只能是0或3；unit-tail数及unit-head数恰同为
\[
u=\min(e+1,p-2n),\qquad v=e+1-u
\tag{N6}
\]
其中v是weight3-tail数。

tail j≥p时，所有harmonic下标≤8n<p²，所以v_pU_j≥−4、v_pC_j≥−1、v_pV_j≥−5。head j<p时，U_j和H_j^(4/5)为p整，C_j≥−1、V_j≥−1。C的两个可能长harmonics均保留；未假设它们的分母自动消失。

关键二阶身份是
\[
\boxed{\det A_j(X)=-(W_jU_j)^2.}
\tag{N7}
\]
它恒成立，不除V_j、不要求U_j单位。若U_j=0则det为0，valuation∞，同一下界仍成立。由N5–N7得到对每个block的0/1/2阶所有minors的共同lower：

|节点类型|数量|0阶|1阶lower|2阶lower|离散marginals|
|---|---:|---:|---:|---:|---|
|unit-tail|u|0|−5|−8|−5,−3|
|weight3-tail|v|0|−2|−2|−2,0|
|unit-head|u|0|−1|0|−1,+1|
|其余head|p−u|0|0|0|0,0|

其余head实际weight≥2，所以1阶≥1、2阶≥4；表中用0安全放宽。head0的U0=0也没有被误称正常2阶块。所有节点类型都在表中；没有尚未证明的actual unit假设。各行marginals非递减，故prefix allocation合法。

## 4. block支持、贪心分配与精确有限p下界

A为literal block diagonal。其非零d-minor必须在每个node block选择相同数量m_j的rows/columns，否则所有permutation项都为0；每个m_j∈{0,1,2}。相符时minor为相应block minors的乘积。于是它的valuation至少上述lower之和，Σm_j=d。离散凸性允许从全部marginals排序取d个最小值，并在平局时取每个block前缀。

这个allocation给**共同估值下界**，不声称最小模型项确非零，也不由block预算推出任何实际minor的unit。再用N4，得到原全部d-minors的同一共同lower。

若3n<p≤4n，则u=p−2n>n，d=3n/2<2u；weight3-tail的−2在unit-tail全部−3之后，故不会被选到。若4n<p≤6n，则u=6n−p+1且v=0。两种情形统一给
\[
\boxed{\ell^{\rm node}_{n,p}=
-5\min(d,u)-3\min((d-u)^+,u)-\min((d-2u)^+,u).}
\tag{N8}
\]
对p≤4n，第三项为0，第二项只用unit-tail；对p>4n，负marginals按−5、−3、−1取完后可用其余head的0填充。其余head至少p−u>2n，提供的2(p−u)个0槽数足够。容量可能来自实际零minor，但作为放宽的共同lower始终合法。

等价的有限表为
\[
\ell^{\rm node}_{n,p}=
\begin{cases}
-5d,&d\le u,\\
-3d-2u,&u<d\le2u,\\
-d-6u,&2u<d\le3u,\\
-9u,&3u<d,
\end{cases}
\tag{N9}
\]
后两行只在p>4n出现，那里没有漏掉−2-tail。所有等号边界两式相同；u含+1精确保留，不以连续u代替有限整模型。N8≥−5d，与此范围E_p=1的原entry界相容。

## 5. 完整尺度、PNT转移与费用恰为41

定义每个n=4r、每个prime的整数lower
\[
\ell_{n,p}=
\begin{cases}
-5dE_p,&p\le3n,\\
\ell^{\rm node}_{n,p},&3n<p\le6n,\\
0,&p>6n,
\end{cases}
\quad E_p=\lfloor\log_p(8n)\rfloor.
\tag{N10}
\]
coarse段覆盖所有小prime和全部有限r；大prime段完全来自原node minors，p>6n整性独立沿冻结P1。于是N4及各prime共同lower给
\[
Q_{n,d}=\prod_{p\le6n}p^{\ell_{n,p}},\qquad
C_d(B_n(X))/Q_{n,d}\in\operatorname{Mat}(\mathbf Z[X]).
\tag{N11}
\]
每个minor仍degree≤d。正scale不是actual primitive content的精确等式。

令x=p/n。N8中u/n=min(6−x,x−2)+O(1/n)，误差uniform；连续下界g(x)=lim ℓnode/n为

|x区间|g(x)|相对coarse −15/2 的增益|
|---|---|---|
|(3,7/2)|−2x−1/2|7−2x|
|(7/2,9/2)|−15/2|0|
|(9/2,21/4)|2x−33/2|2x−9|
|(21/4,11/2)|6x−75/2|6x−30|
|(11/2,6)|9x−54|9x−93/2|

这些branch在内端点连续；x=3的右极限和保留coarse段可有跳点。由min/positive-part的全局Lipschitz性，有限 ℓnode=n g(p/n)+O(1)，不依赖是否恰踩branch边界；所以原u的+1仅付uniform O(1)，没有未计的prime异常。

表中增益的四段面积手工积分准确为
\[
\boxed{\frac14+\frac9{16}+\frac9{16}+\frac{21}{8}=4.}
\tag{N12}
\]
这不是单个辅助prime的O(nlogn)信用，而是全部大prime区间上的正measure收益。

完整尺度可以写成
\[
\log Q_{n,d}=-5d\sum_{p\le6n}E_p\log p
\mathbin{+}\sum_{3n<p\le6n}(\ell^{\rm node}_{n,p}+5d)\log p.
\tag{N13}
\]
第一项归一化趋−45：第一层θ(6n)∼6n，第二及以上prime powers的贡献O(√n log²n)=o(n)。第二项由bounded piecewise affine test和θ(t)∼t趋N12的4；uniform O(1)误差乘Σlogp=O(n)仅付O(n)。可先step functions再Riemann上下逼近，不以sampling替代整个区间。于是
\[
\boxed{\lim_{r\to\infty}(4r)^{-2}\log Q_{4r,6r}=-45+4=-41.}
\tag{N14}
\]
证明使用冻结partial P3已用的同一PNT归一化；未计算或执行新的数值certificate。所有prime均在N10完整覆盖，没有只给有利window就宣称全有限处模型。

## 6. 固定有理源/input和无限非零minor的真实lower

若α、β∈Q固定，选固定正整数D清它们的分母。整个form乘D后相同估值证明适用：D U具有整数sources，D V中的形式X系数为24D，因此全部coefficients仍服从前述bounds。原格、basis和degree不变，准确
\[
D^d C_d(B_n(X))/Q_{n,d}\in\operatorname{Mat}(\mathbf Z[X]).
\tag{N15}
\]
若c=a/M固定有理，M>0，minor degree≤d使
\[
\boxed{(DM)^d C_d(B_n(c))/Q_{n,d}\in\operatorname{Mat}(\mathbf Z).}
\tag{N16}
\]
D及M实际支付O(d)=O(n)，没有免费删除固定分母。

冻结partial P7对同一个固定α、β,c且β≠0已证明无限n=4r上至少一个原d-minor非零。选择该n的任何nonzero coordinate minor，N16给
\[
\boxed{|\det B_n(c)_{I,J}|\ge Q_{n,d}/(DM)^d
=\exp\{-(41+o(1))n^2\}.}
\tag{N17}
\]
没有宣称同一I,J在无限n上被选到，也没有证明7r或顶阶非零。选minor可随n变化，全部minors共同整数模型确保这一变化无需新增分母。

若实际目标ξ=αζ4+βζ5假设等于c∈Q，只有对原同一全部d-minors证明足够解析upper才能与N17比较。旧partial P9–P13指出应估e_d(P)或真实phase compound并支付partial inverse剪切。本文未继承完整det解析率、det1剪切的免费顶阶性质或normalizedN的local费用。

## 7. 与其他路线的关系、已证范围和来源

本轮新收益：原basis在p>3n整节点因子化；真实node2×2 determinant消除V而保留正确derivative费用；完整0/1/2阶支持和贪心共同lower；全部6r minors的全有限处尺度，safe费用从45降到41；加固定有理分母后可接已证fixed-source无限非零。safe41仍为费用upper，不是actual最小分母、content等式、费用lower或原问题no-go。

root并行研究whole determinant的Hasse jets时可以使用另一真实整模型；本文没有将其40.3145顶阶预算搬给partial minors，也没有按minor阶数免费比例缩费用。两种对象的解析转移必须各自对应。同样，本稿没有给H00/Ldeep正常性、whole8r非零、足够strict margin或新ζ/L/Catalan无理性/LI，没有Lean。

所有新关键步骤由literal节点分解、Gauss valuation、block diagonal支持、Cauchy–Binet及上述finite marginal表在正文自证。无需新增外部数学定理；PNT采用已FULL读取的冻结partial/arithmetic预算同一接口。本轮作者新增PDF/HTML/外部代码下载0，实际PDF新读取0，不继承旧或同行原文页数。仅做现有MD、审计JSON和SHA等metadata读取；数学producer创建/执行/import/rerun0，prime扩表0。

状态：唯一NEW完整候选主稿，待root/同行 actual FULL纸核、作者收审后最终FULL回读及一向FINAL来源收据；556既存记录不改动，不提前称审阅完成。
