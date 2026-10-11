# 六积分的大素数前缀核：先匹配 sharp 基线，再计算第一层信用

日期：2026-10-06。本文新建，不改冻结稿、不执行producer或素数扫描。只处理 [固定 rank19 unit source](cdt_odd_level20_cartier_rank19_budget_20261006.md) 和 [六积分 packet](cdt_odd_level20_cartier_packet_matrix_20261006.md)。结论是一个全尺度的第一层维数账本：p>D 时，无条件前缀支持核达到 raw source floor 与原逐行分母 factor 的较大者，没有超过这两项的第一层缺陷。超出它们的量可以写成明确的 Hecke/前缀 rank defect，仍未证明其正 D²累计。这里没有把维数的 max 等同于完整CDT累计高度，更没有认领可追加到 near-balanced sharp 成本的信用。此结论不排除第二层以上、新整格或其它系统。

## 1. 固定 source、row band 与已有序号分母

设 L=D+1、R=19L，实际 tuple 为 P10、三个旧 gH/gϑH/gϑ²H、六个正规积分Iⱼ。使用原 pure整数多项式source：每一种species的坐标degree≤D。按原CDT用polynomials in 1/t时，共同乘t^D后将t^(−j)置换为t^(D−j)，得到这里的0,…,D shifts。source整数坐标只是置换；Laurent leadingflag的grade平移D而leading coefficient保持相同。因此此记号变化没有引入新的source格或finite metric信用，并非声称t^D在O[[t]]中是unit。

固定unit类型是

\[
\sigma=(0^2,1^2,2^6,3^9),\quad
\nu=\sigma+e=(0,1,2^3,3^8,4^6).
\tag{1}
\]

最后六行正是I；其余13行ν≤3。因此p⁴eval中这13L个source columns的全部prefix输出都在p内。旧source的baseline first-threshold count为13L；更高thresholds的5L、2L、L仍完整保留。

取好未分歧place、p>D、p≥7、p∤109以及固定周期/规范分母，且N≤p²。N是完整leading cutoff，闭合actualrank19系统允许N=R+C，C≥0固定。完整prefix用0≤n<N；实际primitive Taylor flag V_D是其中R个rows，至多删C个rows。

对output coefficient n，source shift a∈[0,D]使用原函数的coefficient m=n−a。由于p>D，区间[n−D,n]至多含一个p-multiple；因为m<p²，所有unitLCM列的p-valuation至多1，序号因子m的valuation也至多1。m=0的常数项排除固定规范分母后integral。

因此原安全row分母指数是

\[
c_p(n)=\begin{cases}
0,&n<p,\\
3+\mathbf1_{\{n=mp+a,\ m\ge1,\ 0\le a\le D\}},&n\ge p.
\end{cases}
\tag{2}
\]

式(2)中的额外1恰是CDT (8.2.35)的interval index成本：在[max(n−D,1),n]找到p-multiple。这不是新增的目标分母，也不是另一个可扣除的收益。对该固定tuple使用的Euler导数与polynomial gauge不会扩大D_n³；若另选带固定index offsets的安全型，只需把O(1)端点误差保留，不能用它制造D²信用。

令

\[
r_a=\left\lfloor\frac{N-1-a}{p}\right\rfloor,
\qquad W=\sum_{a=0}^D r_a
 =\sum_{m\ge1}\min(L,(N-mp)_+).
\tag{3}
\]

这里N>D，所以r_a非负。W是complete prefix中c=4的sharp-index band rows数；这些bands互不重叠。p>D还给所有r_a只差至多1。

## 2. 唯一零常数 primitive 与前六行 unit

对target ε=χ(p)，[packet稿 P9](cdt_odd_level20_cartier_packet_matrix_20261006.md) 给六积分完整n<p²身份

\[
p^4I_j=\sum_i\overline M_{p,ij}\,\overline\Xi_i(t^p)
 \pmod{\mathfrak p,t^{p^2}}.
\tag{4}
\]

Ξ_i是完整Af primitive，保持真实ΘA载体；此处只用其degree<p实际Taylor前缀，没有把它当成共同full-leaf函数。定义V_r为Ξ_i的前r个positive coefficients的r×6矩阵。零积分常数已固定。

f^(ε)的第一系数为ηε=1−ε5√5/4，A_target(0)=−1/5、D_target(0)=1，故

\[
\Xi_i(t)=-\frac{\eta_\varepsilon}{5(i+1)}t^{i+1}
 +O(t^{i+2}),\qquad 0\le i\le5.
\tag{5}
\]

Norm(ηε)=−109/16，p≥7时1,…,6可逆。因此前六positive rows的6×6矩阵triangular unit；对所有0≤r≤p−1，

\[
\boxed{\operatorname{rank}V_r=\min(6,r).}
\tag{6}
\]

若r≥6，V_r是injective map，rank(V_rMₚ)=rankMₚ。若Mₚmod𝔭可逆，则对所有r，rank(V_rMₚ)=min(6,r)。这里的ordinary是明确的matrix-unit条件，未假定所有p满足，也未假定nonordinary密度。

## 3. 整个 degree-D 六积分的 exact residue 分离

因为p>D，t^aI_j的最高packet只在n=mp+a出现。不同a的source columns与output rows在modp下完全分离。完整prefix六积分evaluation因此是各a的direct sum blocks V_{r_a}Mₚ，其kernel维数准确为

\[
\boxed{K_I=\sum_{a=0}^D
 [6-\operatorname{rank}(V_{r_a}\overline M_p)].}
\tag{7}
\]

这包含constant-coefficient kernel和它的shifts，也包含有限prefix的额外kernel；不能再把它们另加一次。在matrix-unit primes上，(6)给

\[
K_I=\sum_a(6-r_a)_+=(6L-W)_+.
\tag{8}
\]

最后等号使用r_a至多相差1：它们不可能同时出现≤5和≥7。完整polynomial source的kernel起点是某个r_a≤5，即p>(N−1−D)/6；对N≈19D是约3D，早于constant核的约19D/6，但仍远在冻结budget的ξ≤9/7 cutoff之外。

其它13L个source columns在raw p⁴evaluation中modp全为零，所以整个pure source的first-Smith threshold count是

\[
A_1=R-\sum_a\operatorname{rank}(V_{r_a}\overline M_p)
\tag{9}
\]

（完整prefix）；换成actual V_D的square leading minor只改变O(C)。这是rank-nullity，不是假定它的matrix units已知。

在matrix-unit primes，(8)–(9)化成

\[
\boxed{A_1=\max\{13L,R-W\}.}
\tag{10}
\]

13L是已有ν≤3的source floor1；R−W是(2)逐行提出p-factor后已有的row floor1。源列整性可在原整数species坐标中直接提出至少p；逐行整性也是原坐标中的因子，而不是把一个changed source格的index当成收益。modp rank计算同时核对了这两种整性；这里只取first-Smith threshold维数的max，未以两种determinant factor的总数相加。所以新出现的支持kernel恰好填满两项中较大的既有基线，没有超额。W<6L时，所谓新增积分kernel=6L−W与13L相加只是R−W；W>6L时没有支持kernel，13L source floor已经更强。不能把(8)再加在(10)外面。

## 4. 净determinant公式与唯一可新增的第一层量

令M_V是raw p⁴evaluation在actual leading rows上的R×R整矩阵。先提出原row分母因子

\[
M_V=\operatorname{diag}_{n\in V_D}(p^{4-c_p(n)})\,\widetilde M_V.
\tag{11}
\]

沿已有primitive-flag determinant接口，累计有限高度在该place准确是

\[
\left(\sum_{n\in V_D}c_p(n)-\Gamma_p\right)
  \log\operatorname{Norm}\mathfrak p,
\quad\Gamma_p=v_{\mathfrak p}(\det\widetilde M_V)\ge0.
\tag{12}
\]

高于cap4的正Smith阶没有被(12)排除。不能把rawkernel数目A₁当成Γ。

可以明确隔离actual packet超过unit情况的rank loss：

\[
\lambda_p=\sum_a\left[
\min(6,r_a)-\operatorname{rank}(V_{r_a}\overline M_p)\right]\ge0.
\tag{13}
\]

那么完整prefix的第一层公式是

\[
\boxed{A_1=\max(13L,R-W)+\lambda_p.}
\tag{14}
\]

actualflag仍只差O(C)。在c=4的rows上，(11)没有提出p；这些rows的nonI列全为0，其rank是Σrank(V_{r_a}Mₚ)。其它rows至多补满其row数，所以

\[
\boxed{\Gamma_p\ge
 \big((W-6L)_++\lambda_p-C\big)_+.}
\tag{15}
\]

这里(W−6L)+仅是已有13L source columns的第一层整性在较粗row账本中的体现；λₚ才是actual Hecke/前缀在本第一层接口中超过两种基线的新信息。式(15)是相对于(2)的粗unit row账本的净界；不能未经新的matching把它自动追加到已有更细balanced transportation成本上。

在支持核产生的W≤6L区域，单凭P12a/P12b的维数界没有正的λ下界；matrix-unit的情况完全符合全部既有输入且λ=0。若Mₚ退化，对r_a≥6有λ贡献dimkerMₚ；对r_a<6则要看V_{r_a}与其image的实际位置。固定Eisenstein block为unit、old/new退化的条件谱账本可提供相应数据，但未证明其正密度或全p累计。

## 5. 与sharp tail及CDT剩余接口的范围

原sharp尾项的区间恰是(2)的bands；ordinary全prefix支持核的first-threshold信息已被(10)匹配。固定C造成的每prime O(1)缺口，经p≤N和素数定理累计仅O(D)，不产生D²主项。p≥N时W=0、raw四层整性本来覆盖所有rows；其深度一kernel也没有新信用。

数域按[K:Q]归一化；好未分歧rational p的全部places权重之和仍是logp，不能因split有两places再乘2。此处“sharp匹配”指原(8.2.35)逐coordinate的index interval与(2)相同，以及第一层floor不重复；并未把one-variable粗row成本认作完整near-balanced transportation在此large-prime window的实际最优值。

因此，当前无条件支持核不能证明一个可追加到冻结rank19 κ(ξ)上的正large-prime γ。该表的optimal ξ∈[19/15,9/7]之外仍保留原I₁₉(ξ) sharp尾成本；不能以“six integral kernel从约3D起出现”把该尾成本抹去。更强的积分coefficients/higher thresholds可能给新增信用，但需要证明(11)归一化后的determinantal divisibility、或者(13)的真实正全prime平均，并且接到同一个near-balanced source及其metric。

本文结论限于固定rank19 unit表、p>D的第一层、同一个pure polynomial source与实际leadingflag。没有证明所有ordinary primes的Γ=0、没有排除其更高层positive Smith slack，也没有排除nonordinary或真实p·旧H混合primitive产生新收益。它只给出现在这条支持kernel路线所需的不可相加公式和最小净量。

## 6. 独立审阅范围

helper_tensor_budget已实际只读§§1、3–5并通过：固定pure source的安全row bound及(8.2.35) index bands、residue直和的raw first-threshold非加法公式、提出row factors后的Γ下界，以及尚未对接near-balanced sharp最优成本的限制。该审阅没有执行producer，也没有将未读§2的全部packet输入算作重新证明。随后补充的Laurent grade平移和两种floor只在first-threshold取max的说明仅澄清同一证明的坐标范围。
