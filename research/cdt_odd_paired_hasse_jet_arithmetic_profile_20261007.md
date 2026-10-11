# 原低阶Hasse系数的算术费用profile：源占位与合流节点

2026-10-07，NEW，作者 /root/masked_racah_finalize。Authority为main §§166–170及audit cdt_odd_delivery_hasse_bridge_20261007.json，SHA 94eec763f855689bda6ecfb6fd3e4c0af2fef50fcff2e357fc032c720d04d2d3；564冻结、559数学文件及5guard只读。实际读进展段落，完整JSONparse及header，不称逐条人工全文读564记录。唯一新研究主稿，纯纸证；数学producer创建/execute/import/rerun0，辅助prime扩表0。

## 1. 原对象和严格新费用

取n=4r、m=2n。g_1,…,g_m仍是原饱和整数值配对格完整基，degree<3n。先取固定整数α、β，β≠0。原form准确为
\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+T_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-8\alpha H_j^{(3)}-6\beta H_j^{(4)},\quad
T_j(X)=C_jU_j+24(X-\alpha H_j^{(4)}-\beta H_j^{(5)}).
\tag{J1}
\]
\[
B_n(X+t)=B_n(X)+tV_n,\quad V_n=24\sum_jW_jv_jv_j^t\in\operatorname{Mat}_m(\mathbf Z),
\quad v_j=(g_i(-j))_i.
\]
\[
D_n(X)=\det B_n(X),\qquad J_{n,k}(X)=[t^k]D_n(X+t).
\tag{J2}
\]
估值指Q[X]的Gauss valuation，含所有X系数。冻结whole-X已证完整signed bound-model的逐prime整数lower记b_(n,p)，其尺度Q_n^b=∏p p^b_(n,p)满足
\[
D_n(X)/Q_n^b\in\mathbf Z[X],\qquad
A_{\rm full}=\frac{800671681093752110193539327219}{19860629178118281482813083200}<40.314517427.
\tag{J3}
\]
这是supported T13–T17的安全模型；5<x<6的已付branch准确g_b(x)=12x−68，见第5节。不将它等同actual content。

**新定理。** 第5节的全部prime尺度Q_(n,k)逐n、逐k给J_(n,k)(X)/Q_(n,k)∈Z[X]。若0≤k_n≤n/2、k_n/n→κ，则
\[
\boxed{\liminf n^{-2}\log Q_{n,k_n}\ge-A_{\rm full}+\frac54\kappa^2,\qquad
A_{\rm jet}(\kappa)=A_{\rm full}-\frac54\kappa^2.}
\tag{J4}
\]
κ=1/2新增5/16，安全费用upper<40.002017427；κ=0不免费改善。该费用只是合法整模型upper，非最小actual费或lower，也未给充分strict矛盾。

## 2. 整节点分解及真实源占位

固定5n<p≤6n。n≥4使p>5、p²>8n；原Newton degree<3n<p的分母i!为p-unit，原整数S不引入分母。原basis的monomial coefficients、ordinary derivatives在Z_p。令Y第j对columns为g_i(−j)、g_i′(−j)，则literal
\[
B_n(X+t)=Y A(X,t)Y^t,\quad Y\in\operatorname{Mat}(\mathbf Z_p),\quad
A=\operatorname{diag}(A_j),
\]
\[
A_j=W_j\begin{pmatrix}T_j(X)+24t&U_j\\U_j&0\end{pmatrix},
\qquad\boxed{\det A_j=-(W_jU_j)^2}.
\tag{J5}
\]
单个源24tW_j只能出现在该node的1×1 value/value diagonal minor；2×2 determinant与t无关，一个node不能有两个源。

两次Cauchy–Binet展开原m×m determinant。非零A-minor逐node必须选相同数量rows、cols，否则每个permutation跨零block；相符时按node、residue factor。抽取t^k后每项准确满足
\[
\sum_\rho r_\rho=m,\qquad\sum_\rho h_\rho=k.
\tag{J6}
\]
r为所选residue rows数，也等于cols数；h为该residue的源次数。余下相消只加强共同lower。未假设Y-minor或actual block单位。

## 3. 两点合流wedge的完整估值

置e=6n−p<n、T=p−2n>3n。Legendre第一层给j=ρ或p+ρ的
\[
w_\rho=v_pW_j=2\mathbf1_{\rho>e}+3\mathbf1_{\rho\ge T}.
\tag{J7}
\]
residue全部类型如下，准确保留+1：

|residue|数量|nodes|weight|
|---|---:|---|---:|
|0≤ρ≤e|u=e+1=6n−p+1|head、tail各一|0|
|e<ρ<T|T−e−1=2p−8n−1|仅head|2|
|T≤ρ<p|2n|仅head|5|

unit-head的U≥0、T_j(X)≥−1；unit-tail的U≥−4、T_j(X)≥−5。weight2单head的H_j、H_(2n+j)、H_(6n−j)全短于p，故U、T均p整。weight5单head的U整、T≥−1。source lower为w。包含形式X及sources额外divisibility，不要求α、β为p-units。

unit两node为a=−ρ、b=a−p。对任意原basis列subset，记value row v(a)、derivative row d(a)，步长s=b−a=−p。Taylor coefficients皆Z_p，故
\[
v(b)=v(a)+s d(a)+s^2R,\qquad d(b)=d(a)+sS.
\tag{J8}
\]
所有相应方形Y-subminor共同lower为：两个values≥1，两个derivatives≥1；三rows有两values、一derivative时≥2，有一value、两derivatives时≥1。以a或b展开都成立。一个site的value、derivative无额外要求。

四rows全部选取的lower≥4：置R0=v(b)−v(a)−s d(a)，S0=d(b)−d(a)。R0≥s²，sS0−2R0≥s³，因为每阶l≥2系数为(l−2)s^l/l!，l2消失。该row替换使wedge乘s，所得wedge至少s^5，原wedge至少s^4。Taylor divided derivatives整性来自原monomial coefficients；这里用于det身份的非unit scaling没有被冒称免费GL换格。zero minor估值∞。

对所选整体Y-minor按residue row-block作Laplace展开，每项是各residue相应subminors乘积。另一侧同样。因此这些有限lower在所有residues相加合法，不需某个subminor非零或下界同时可达。

## 4. 所有(r,h)与合法线性定价

把A coefficient和左右Y合流费用合计为c(r,h)。unit两node的完整安全表：

|r|h|c lower|c+3r−5h|
|---:|---:|---:|---:|
|0|0|0|0|
|1|0|−5|−2|
|2|0|−8|−2|
|3|0|−5|4|
|4|0|0|12|
|1|1|0|−2|
|2|1|−3|−2|
|2|2|2|−2|
|3|1|−4|0|

未列出的(r,h)为0多项式；特别r3,h2及r4,h≥1，因为源只能出singleton而2×2块无t。不是把零当达到有限估值。

逐项检查：r2,h0的同site最坏tail determinant−8；跨site两个value的−6加两侧wedge≥2，或offdiag较高U费用，皆≥−8。r3,h0只有2+1占位：tail2加head value singleton费用−9、两側wedge各2，给−5；head offdiag费用−8、左右wedge2和1，仍−5；交换head/tail更整。r4,h0的A≥−8、两侧四row各≥4，给0。

r1,h1为单个source，lower0。r2,h1必须跨site：head source加tail value费用−5、两侧两个values各≥1，给−3；tail offdiag费用−4时一侧两values付1，另一侧value+derivative付0，同样−3；交换site更整。r2,h2两个sources，两侧两个values各付1，给2。r3,h1只能在singleton取source：head source加tail2费用−8、两侧均有两values各付2，给−4；交换site更整。r0、r1,h0及零分支沿J5。所有offdiag左右方向和ordinary derivative费用均覆盖。

weight2单head表为(0,0)0、(1,0)2、(1,1)2、(2,0)4；weight5单head表为(0,0)0、(1,0)4、(1,1)5、(2,0)10；其余(r,h)为0。源系数整，2×2无源，非unit额外divisibility只加强lower。有限表逐行满足
\[
c+3r-5h\ge-2\quad\text{unit两node},\qquad
c+3r-5h\ge0\quad\text{单head}.
\tag{J9}
\]
由J6、两侧residue Laplace及Cauchy–Binet整体求和，得到准确逐prime、逐n/k的原系数界
\[
\boxed{v_p^{Gauss}J_{n,k}(X)\ge-3m+5k-2u
=2p-18n+5k-2\quad(5n<p\le6n).}
\tag{J10}
\]
不是normalizedN单位或部分minors41预算的移用。

## 5. 全部有限处的signed模型及面积

V_n整数而每个原B entry的Gauss lower≥−5E_p，E_p=floor(log_p8n)。det(B+tV)每个t^k项有m−k个B和k个V因子，故全prime直接有
\[
v_p^{Gauss}J_{n,k}(X)\ge-5(m-k)E_p.
\tag{J11}
\]
J3 whole-X尺度又经整数Hasse二项式继承给每个J_k；p>6n时B、V整。定义
\[
\ell_{n,k,p}=\max\{b_{n,p},-5(m-k)E_p,
\ 2p-18n+5k-2\ \text{若 }5n<p\le6n\}\quad(p\le6n),
\]
\[
\ell_{n,k,p}=0\ (p>6n),\qquad Q_{n,k}=\prod_p p^{\ell_{n,k,p}}.
\tag{J12}
\]
smallprime2/3、全部有限n及所有端点都有entry或baseline准确fallback。positive signed信用保留。J12逐系数证明J_k/Q∈Z[X]，取max是共同lower，不称达到actual content。

本轮actual FULL读 global O1–O20/全部正文、supported T1–T18、low-price L1–L18。旧global saved113-row cover完整JSONparse，实际末20 records所有字段；最后一条5<x<6的combined slope/intercept准确为12、−68。supported更新域仅[1/4,2]，low-price候选逐有限参数被已有界支配，所以当前paid模型在此窗仍是
\[
\boxed{g_b(x)=12x-68\quad(5<x<6).}
\tag{J13}
\]
不从只读20条推整个budget：全place A_full取实际FULL读T13–T17的已冻全尺度定理，窗口表达式再由旧原模型/saved cover核对；未执行旧global或supported源。

选择旧证明的显式safe bound-model及其uniform O(1)修正、finite floor-jump fallback，PNT归一化为−A_full；该值不等actual内容。若需，仅在本窗取已证floor(n g_b(x)−C) lower替代对应baseline窗口，旧相同bound-model/PNT主率保持；有限endpoint places仍用准确整数fallback，O(nlogn)不改n²率。其余prime保留旧完整证明。

J10的归一化新函数为2x−18+5κ。相对J13的实际新增paid信用
\[
\Delta(x,\kappa)=(50-10x+5\kappa)_+,\qquad5<x<6.
\tag{J14}
\]
0≤κ≤1/2时支撑为5<x<5+κ/2，面积恰
\[
\boxed{\int_5^6\Delta(x,\kappa)dx
=\int_5^{5+\kappa/2}(50-10x+5\kappa)dx=\frac54\kappa^2.}
\tag{J15}
\]
有限u的+1只付−2；k_n/n偏移由positive-part Lipschitz统一控制。θ(t)∼t与bounded piecewise affine test给J4；先取有限κ-mesh再用统一Lipschitz可给uniform o(n²)，故adaptive k_n也有
\[
\boxed{\log Q_{n,k_n}\ge
-\{A_{\rm full}-(5/4)(k_n/n)^2\}n^2-o(n^2).}
\tag{J16}
\]
J11及其他places的max可能再有收益，未计算它们；本稿不声称J16等号或profile最优。新增5/16信用与旧whole已付界比较，不和重叠信用重复相加。

## 6. 固定源/input的准确分母及adaptive非零

固定有理α、β，取D>0清二者。记整数源矩阵widehat B_n(Y)=B_(Dα,Dβ)(Y)，斜率仍是同一V_n，准确
\[
\widehat B_n(DX)=D B_n(X),\quad \widehat D_n(Y)=D^mD_n(Y/D),
\qquad\boxed{\widehat J_{n,k}(DX)=D^{m-k}J_{n,k}(X).}
\tag{J17}
\]
亦等于[t^k]det(DB_n(X)+tV_n)：m−k个B因子付D，k个整数V不付D。上述对整数sources均合法的模型作用widehat J，再代入整数倍DX不降低Gauss估值，故
\[
D^{m-k}J_{n,k}(X)/Q_{n,k}\in\mathbf Z[X].
\]
\[
\boxed{(DM)^{m-k}J_{n,k}(c)/Q_{n,k}\in\mathbf Z,\quad
J_{n,k}(c)\ne0\Rightarrow |J_{n,k}(c)|\ge Q_{n,k}/(DM)^{m-k}}
\tag{J18}
\]
其中c=a/M固定，degree J≤m−k准确支付M；D、M费O(n)完整保留，无k!分母、未改格、未以degree比例免费缩whole费用。

冻结H6使同一固定有理α、β,c、β≠0在无限n=4r存在某k_n≤n/2非零。J16/J18给这些actual adaptive jets的lower。未证明κ_n有正下界，因此不能将κ1/2费用40.002赋给所有低jets；k_n=0时仍只有旧A_full。可取子序列κ_n→κ按相应profile比较。

若对同一J_k证明uniform解析保证率C(κ)，充分矛盾需每个可能κ∈[0,1/2]有C(κ)>A_jet(κ)，或另证非零阶信息排除不利κ。旧k0>12.623及mixed upper未完成这个条件，不免费替代全部J_k。

## 7. 读域、审阅与界限

本轮actual FULL：Hasse H1–H17/8节；all-prime B1–B22；global O1–O20/全部正文；supported T1–T18；low-price L1–L18。literal原form/basis与冻结local/lattice一致，正文重列必要定义并自证新表。旧global JSON完整syntaxparse、实际末20 records所有字段，不称人工全文读113 records。新增PDF/HTML/外部code下载0，实际PDF新页0；不继承旧/同行primary页数或producer执行。

唯一新增数学为J8合流wedge、完整source-count表、逐prime J10、全place J12及实际面积J15、fixed分母J17–J18。safe费用严格改善，但不是actual cost lower或no-go。无新ζ/L/Catalan无理性、LI、Lean，也未称whole8r点值∞非零。

本稿候选待独审；完整作者自读后交root/scaled actual FULL审阅，再收审后最终FULL读及单向FINAL来源收据。564冻结旧记录不改，不预称审阅完成。数学producer创建/execute/import/rerun和prime扩表均0。
