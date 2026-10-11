# 同一真实配对格的局部 Hermite 弱层与直接 Gram 内容

2026-10-06，NEW，/root/toric_chow_completion。455项冻结数学输入、旧及同行所有producers只读，不execute/import/rerun。本稿保留原B6/k3/s5、ambient degree<3n、rank2n饱和整数值格；C!的Smith与本稿Gram层是两个不同对象。

## G1. 当前结论与同一对象

取整数a,b，b≠0、形式变量X。固定有理sources先清同一个固定分母，determinant付其2n次幂，费用O(n)。令f_i(t)=binom(t−1,i)，0≤i<3n，M_Z为其整数格。对c=2n+1和d_m=(m)_{6n+1}，原actual paired格是

\[
U_Z=\{P\in M_Z:q_mP(m)-p_mP(c-m)=0, 1\le m\le n\},
\]

其中p_m=d_m/g_m,q_m=d_{c-m}/g_m,g_m=gcd(d_m,d_{c-m})。冻结lattice I1–I25给完整整数基S（G_m=p_mL_m+q_mL_{c-m}及全部high f_i），U_Z为rank2n饱和direct summand。本文的对象仍为

\[
D_A(X)=\det(S^{\mathsf T}H_N(X)S),\qquad H_N(X)_{ij}=B_X(f_i,f_j).
\tag{G1}
\]

没有first2n factorial，没有quartic zeros，没有再次扣primitive gcd。本文证明直接局部Gram的whole-X界

\[
\boxed{v_p^{\rm Gauss}D_A(X)\ge-10n+2k},
\tag{G2}
\]

k为下面真实Hermite map的kernel dimension。对n<p≤2n另给显式下界并兑现超过现行entry/common-minor/Plücker预算的正measure n²收益。

## G3. actual coefficients与缩放恒等式

原form是
\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^{2}\binom{2n+j}{j}^{3},\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-8aH_j^{(3)}-6bH_j^{(4)},\quad
V_j(X)=C_jU_j+24\{X-aH_j^{(4)}-bH_j^{(5)}\}.
\tag{G3}
\]

固定p>5、p²>8n。Newton导数identity f_i'=Σ_{r=1}^i(−1)^{r−1}f_{i-r}/r给P(z),pP'(z)∈Z_p，对全部P∈M_Z⊗Z_p及z∈Z_p成立，因为i<3n<p²。对Q亦然。写

\[
\widehat U_j=p^4U_j,\quad\widehat V_j=p^5V_j,\qquad
p^5B_X(P,Q)=\sum_jW_j\{\widehat U_j[P(pQ')+Q(pP')]+\widehat V_jPQ\}_{t=-j}.
\tag{G4}
\]

所有hat系数属于Z_p[X]。tail j≥p有vU≥−4,vV≥−5；head j<p有U integral、V whole-X≥−1，故两个hat均被p⁴整除。长harmonic 2n+j的可能p分母已含在Vhead≥−1中，未删除它。X项是24p⁵X；a的高层terms与任意b的额外divisibility保留，未要求sources是p-units。

在该large-p域，Legendre给W_j的valuation为0、2、3或5，随residue固定；非unitW因此至少p²。这是本稿二阶弱整除所需，不能以W≥p的任意weight替代。

## G5. actual Hermite kernel与exact characteristic-zero lifts

令J_p={j:p≤j≤6n,v_pW_j=0}。U=U_Z⊗Z_p是M_Z⊗Z_p的真实rank2n direct summand。定义

\[
\mathcal H_p:U/pU\to\bigoplus_{j\in J_p}F_p^2,\quad
\overline P\mapsto(P(-j),pP'(-j))\bmod p,\qquad
k=\dim\ker\mathcal H_p.
\tag{G5}
\]

这是well-defined：改变P为P+pQ时value增加pQ，scaled derivative增加p(pQ')，二者modp均0。不用ordinary coefficient reduction代替integer-valued reduction。

选U/pU的basis，最后k列为kerH的basis，将其在**原S坐标**中的Fp系数lift为普通整数，得T∈Mat_{2n}(Z)、detT为p-unit。ST的每列是exact characteristic-zero paired polynomial，所有primitive约束在Q中严格成立；不是只满足modp方程的自由polynomial。这些列组成U的Z_p basis。weak列在J_p的values及scaled derivatives均在pZ_p；strong列均整。

G4的unit-tail项于是strong×weak被p整除，weak×weak被p²整除；head全部p⁴、nonunit-tail全部p²，亦适用所有weak/strong配对。故在这个真实局部basis中

\[
p^5B_X=DND,\quad D=\operatorname{diag}(1^{2n-k},p^k),\quad
N\in Mat_{2n}(Z_p[X]).
\tag{G6}
\]

detT是p-unit，返回原固定S不改变v_p^{Gauss}。G6直接证明G2，且任意r阶minor满足−5r+2(r−2n+k)^+的polygon下界。这不是exact Gram Smith：N可能继续退化，或mixed block产生不同elementary exponents；也不是C!Smith层。D_A=0时结论仍成立，未提供infinite nonzero。

## G7. 真正integer-valued ψ层与ragged degree

现在固定n<p≤2n（仍p>5,p²>8n）。令
\[
3n=Qp+R,\quad0≤R<p,\quad Q∈\{1,2\},\qquad \psi(t)=(t^p-t)/p.
\]

冻结budget B20的真实GL basis为 binom(t,i0)binom(ψ(t),i1)，i0+pi1<3n。这里再自核GL性：i<3n<p²，故i0!,i1!皆为units，ψ(Z_p)⊂Z_p，所有b_i为整数值；其有限差分Newton展开的系数皆在Z_p，highest-coefficient比值为i!/(i0!i1!p^{i1})、valuation=floor(i/p)−i1=0。按degree的变换为unit triangular，再付t→t−1的整unitriangular变换，准确回到原M而非扩大格。

完整i1=0,…,Q−1层各有p维；top i1=Q只有i0<R的R维。对r=t modp的local polynomial Φ_r(Y)，Y=ψ(t)modp，其degree≤Q。底Q个coefficients可为任意residue functions，top coefficient的r依赖是degree<R的polynomial（乘共同unit1/Q!）。不能补成p个自由top coefficients。

若t=z+pY0，则ψ(t)≡ψ(z)−Y0且pψ'(t)≡−1modp；p乘binom(t,i0)导数为0。因此
\[
P(t)\bmod p=\Phi_r(\psi(t)),\qquad
pP'(t)\bmod p=-\partial_Y\Phi_r(\psi(t)).
\tag{G7}
\]

这是原degree3n和integer-valued格的局部关系，不是root ordinary-coefficient CRT所计算的C! image。

## G8. unit-W sector与全部尾部jet约束

写6n=hp+e，0≤e<p。j=ρ+lp的Wvaluation是
\[
w_ρ=2\mathbf1_{ρ>e}+3\mathbf1_{ρ≥2p-2n}.
\tag{G8}
\]
所以unit residues恰ρ=0,…,u−1，其中
\[
\boxed{u=\min(e+1,2p-2n).}
\tag{G9}
\]

在每个unit residue，实际unit-tail节点是j=ρ+lp，l=1,…,h，因为ρ≤e。它们的Y=ψ(−ρ)+l全部互异；h<p由p²>8n保证。h=floor6n/p≥Q+1。因此Φ_{−ρ}(Y)degree≤Q在这些values上vanish，当且仅当它作为完整local polynomial为0。随即scaled derivative也vanish。故G5的Hermite kernel精确是**所有unit-sector local coefficients皆零**的actual paired reduction，而非仅忽略导数的heuristic。

在full ambient M/pM上，unit-sector restriction的rank准确为
\[
\boxed{d_p=Qu+\min(R,u).}
\tag{G10}
\]
证明：每个底层的p个任意residue values在u处独立，共Qu；top polynomial degree<R在u个不同r处评价rank为min(R,u)，Vandermonde为unit。底层可吸收top产生的低Y coefficients，故加和准确。限制到actual U/pU（dimension2n）rank至多d_p，因此
\[
\boxed{k\ge k_0=[2n-Qu-\min(R,u)]_+.}
\tag{G11}
\]

没有假设这些ambient自由coefficients都独立存在于pairedU；G11只用restriction rank upper。paired约束可能给更强kernel。结合G2，same whole-X直接有−10n+2k0，这是新actual Gram整除，未借Gram units。

## G12. uniform连续模型与现行Plücker基线

令x=p/n∈(1,2)、Q=floor3/x、h=floor6/x，
\[
u(x)=\min(6-hx,2x-2),\quad R(x)=3-Qx,
\quad k(x)=[2-Qu(x)-\min(R(x),u(x))]_+.
\tag{G12}
\]
actual u=nu(x)+O(1)，G11的k0=nk(x)+O(1)，误差uniform。n<p,p>5排除p|3n或6n，故Q/h floor对应没有未付的大例外；u中+1仅O(1)。small n未满足p²等条件时保持冻结all-n界，有限例外不影响主率。

直接bound g_D=−10+2k 的各段为

|x区间|g_D|
|---|---|
|(1,8/7)|6−12x|
|(8/7,6/5)|30x−42|
|(6/5,5/4)|6−12x|
|(5/4,4/3)|−4−4x|
|(4/3,3/2)|20x−36|
|(3/2,5/3)|−10|
|(5/3,2)|12x−30|

本轮实际全文回读冻结dual0fb995 D1–D10。n<p≤2n现行model是g_prev=max(−10,g_raw+2d)，d是其D18三个mixedcarry tents；不与原entrycap直接比较而漏已付Plücker信用。原50段JSON本轮实际完整静态读，window中的raw段为4x−12、25x−36、−10、18x−34、−2x−8、8x−24，其切点1,8/7,6/5,4/3,3/2,8/5,2（最后8x−24在7/4才越cap）。p≤n已付信用和3n<p≤6n先前Gram信用与本稿window不交。

## G13. 真正新增paid主率：完整max比较

对g_new=max(g_prev,g_D)，逐段exact affine比较，Δg=g_new−g_prev仅在如下七段非零：

|区间|Δg|
|---|---|
|(1,15/14)|30−28x|
|(6/5,5/4)|28−22x|
|(5/4,14/11)|18−14x|
|(14/11,4/3)|8x−10|
|(4/3,3/2)|2x−2|
|(5/3,7/4)|12x−20|
|(7/4,2)|4x−6|

所有未列区间为0，d的h3支撑仍被cap遮蔽；本稿在其后(5/3,2)得到的是直接Gram信用，未裸积分它。各段面积准确为
\[
\boxed{\Delta A_G=
\frac1{14}+\frac{21}{400}+\frac{15}{1936}+\frac{28}{1089}
+\frac5{36}+\frac1{24}+\frac38
=\frac{16469}{23100}>\frac1{14}>0.}
\tag{G13}
\]

即使仅使用第一段也已是同一对象正measure n²收益；七段给更强严格界。这里是已证safe费用的改善，不是actual cost等式或下界。

## G14. 全n signed整化与PNT

在本窗口满足hypotheses时取 \(\ell'_p=\max(\ell_{{\rm prev},p},-10n+2k_0)\)，其他prime保持当前已证\(\ell_{{\rm prev},p}\)。它们均为integer whole-X lowerbounds，每个n都有D_A/Q'_n∈Z[X]，Q'_n=∏p p^ℓ'_p；fixed rational specialization另付其分母2n次幂，并仍需实际nonzero。

现行连续common-minor/Plücker model的uniform O(1)已在冻结B15/D18证明，G12只增uniform O(1)。bounded piecewise affine Δg用θ(t)∼t，先step functions再Riemann上下逼近，得safe费用从上一轮
\[
A_{455}^{safe}=790225879771/17925027120
\]
再降低至少G13：liminf n^−2logQ'_n≥−A455+ΔA_G。新同轮其他论文若在本window另有改进，必须共同取max，不能把重叠收益直接相加；quarter本轮p≤n收益则与这里不交。

仅本稿窗口的安全上界准确为A455−16469/23100=3887231721011/89625135600，位于(43.372115,43.372116)。这是无需本轮其他改进的单独结论；没有将其他窗口尚未审完的费用混入。

无限nonzero、strict解析/算术余量与数值结果均未解决。当前解析率仍>12.00357，与此safe费用仍有大差距；这不构成方法no-go。

## G15. 来源与后续验证边界

本轮实际全文读取冻结budget55278 B1–B22、lattice5b794 I1–I25、mixedarithmetic452b A1–A14含A30a、oldjet39a0 J1–J23、dual0fb995 D1–D10及旧budget JSON全部50affine行。均仅读，无execute/import/rerun。G3–G11由这些真实定义在本稿自证；本人不将C! exactSmith当GramSmith。

独立NEW `cdt_odd_paired_actual_local_gram_layers_20261006_verify.py` 完整静态读后，首次且唯一执行1次，exit0 PASS；无失败，无rerun。程序以输出文件exclusive-create为guard，在数学执行前落盘，若失败保留失败记录。只import stdlib，不读任何旧/同行数学输入。自有source SHA e9a512a8bb9f40b6c84144eeeaf52eb9761a0ef0699adc4e82af07d8c0c1ebf9，JSON SHA0fd35bb97e6f16a6a7ac273e0bd8baba1b7afc8f91f321c8a038416d4fdd900e。

有限机制枚举n≤18、n<p≤2n、p>5、p²>8n共45 cases。每个case实际构造原S、在原S坐标lift完整Hermite核并逐个验证char0 paired constraints；用原Newton values/p-scaled derivatives、原W和p⁴U/p⁵V模p²计算原Gram，两组(a,b)=(0,1),(1,1)验证strong/weak的p与weak/weak的p²。形式X系数24p⁵W·values⊗values亦逐case单独核；有限表不承担G2/G11的全尺度证明。actual核通常强于ambient k0，但本稿主率只用已证G11，不从有限秩外推exact paired rank。

同一first-only源用Fraction完整构造RAW/DIRECT/三tent affine cover，加入所有branch pair roots，输出13个闭interval的old/direct/delta/area。每段的endpoint inequalities证明固定affine branch覆盖整段；积分准确为G13，并给上面safe A窗口。没有以网格小数验证代替max比较。

首次组合读取NEW JSON与peer稿时总输出截断；随后用只读JSON parser补读全部45 case的所有字段、全部13 affine records和metadata，无截断，未execute/import任何数学源。本人本轮新primary下载/实读0，证明使用已实际读的冻结定义并在这里自证；NEW来源receipt另存literature。root和quarter数学审阅状态与准确scope将在最终receipt登记。
