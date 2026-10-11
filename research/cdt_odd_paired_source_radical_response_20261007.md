# 原配对格的偶源第一高层、实际质量 Gram 与系数非零判据

2026-10-07，root，NEW。Baseline504记录（503数学文件加1入口guard）全部只读；不执行、import或重跑旧及同行数学程序，不扩辅助单位素数表。保留原B6/k3/s5、degree<3n、饱和rank2n配对格和whole-X行列式。本文尚未得到新的特殊值定理。

## S1. 同一对象与两种源

用α、β表示目标ξ=αζ(4)+βζ(5)的有理系数，β非零，避开固定分母及β的有限例外素数。取n=2m、m=2r、p=9m+1=18r+1素数。以下F=F_p，实际局部基与weak归一化D_p沿用[单bordered稿B1–B4](cdt_odd_paired_single_bordered_nonzero_gate_20261006.md)：

\[
p^5B_{\alpha,\beta,X}=D_pN_{\alpha,\beta}(X)D_p,
\quad D_p=\operatorname{diag}(1^{5r},p^{3r}). \tag{S1}
\]

令a_l=−l（0≤l<3m）、A(t)=∏_l(t+l)、S(t)=∏_{z=1}^{4m}(t−z)、c=4m+1。L、Z、J、D是上述B1–B2的真实negative-image定义：LZ=0，Z满columnrank5r，J_{l,j}=A'(a_l)Q_j(a_l)，Q为degree<3m的reflection-even空间。χ为共享节点指标，η=χ/2，D=diag(W_{p+l})，均在F中。Z和Q的实际lift存在且可取

\[
P_Q=AQ+(p/2)(A/I)I'Q+O(p^2),\quad
P_Q(-p-l)/p\equiv(\eta_l-1)J_{l,Q},\quad
P_Q'(-p-l)\equiv J_{l,Q}. \tag{S2}
\]

这里I是模p共同节点因子，第二式含真实−p平移，不能用ηJ代替(η−1)J。修正为char0精确配对多项式的O(p²)项不改变本文第一源响应。strong lift只需其节点值Z；其导数在本精度不贡献。辅助域degree<6m<p，故Newton基所有factorial分母是p单位，导数为p整数。

## S2. 偶源恰在第一高层进入

实际form见[局部Gram稿G3](cdt_odd_paired_actual_local_gram_layers_20261006.md)。对α的偏导系数为

\[
U_\alpha=-8H_j^{(3)},\quad
V_\alpha=-8C_jH_j^{(3)}-24H_j^{(4)},\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j}. \tag{S3}
\]

全部tail为j=p+l，0≤l<3m；它们W_j是unit，三个harmonic端点都小于2p。直接数唯一p极点给pC_j≡2、p³H_j^(3)≡p⁴H_j^(4)≡1。因此

\[
p^5U_\alpha\equiv-8p^2\pmod {p^3},\quad
p^5V_\alpha\equiv-40p\pmod {p^2}. \tag{S4}
\]

对weak×weak需要更高的表面精度，但S2各个值先有p，故S4余项在两侧除D_p并再除p后均消失。head j<p的U_α整，V_α至多p⁻¹；p⁵缩放后至少p⁴，两侧除D_p再除p仍至少p。nonunit head还带至少p²的W，没有未付的head项。本辅助域不存在nonunit tail。

定义对任意s∈F的真实节点矩阵

\[
K_s=s-(s+1)\eta,\quad
d_s=1-\eta^2-s(1-\eta)^2,
\]
\[
\mathcal A_s=\begin{pmatrix}
-(s+1)Z^tDZ&Z^tDK_sJ\\
J^tK_sDZ&J^tD\operatorname{diag}(d_s)J
\end{pmatrix}. \tag{S5}
\]

当s+1≠0时d_s=(1−K_s²)/(s+1)，但仿射定义S5也适用于s=−1。

**定理S6（实际源响应）。** 在同一个实际局部基上，

\[
\partial_\alpha N_{\alpha,\beta}(X)\in p\operatorname{Mat}_{8r}(Z_p),\quad
(\partial_\alpha N/p)\bmod p=8\mathcal A_4,\quad
N_{\alpha,\beta}(X)\bmod p=6\beta\mathcal A_5. \tag{S6}
\]

证明：unit-tail的strong×strong由−40ZᵗDZ给出；strong×weak由−40(η−1)−8=8(4−5η)给出；weak×weak由−40(η−1)²−16(η−1)=8(1−η²−4(1−η)²)给出。head已逐项支付，返回S1。β式是冻结B4，X式为[真实value-Gram稿V8](cdt_odd_paired_value_gram_depth4_nonzero_20261006.md)的24p⁵H。这里偶源不是形式上自由加入的新低层参数，而是原αζ4源的实际第一高层。

## S3. 第一响应在真实radical上是明确Gram

令

\[
\mathcal E=[Z,-\operatorname{diag}(1-\eta)J],\quad
\mathcal K=\ker\mathcal A_5. \tag{S7}
\]

S5逐block准确给出

\[
\partial_s\mathcal A_s=-\mathcal E^tD\mathcal E,\quad
\mathcal A_4-\mathcal A_5=\mathcal E^tD\mathcal E. \tag{S8}
\]

因此对任意真实radical基T（8r×k，k=dimK），

\[
T^t\mathcal A_4T=T^t\mathcal E^tD\mathcal ET. \tag{S9}
\]

由[实际Racah压缩R20](cdt_odd_paired_fixed_middle_racah_border_20261006.md)及冻结bordered corank恒等式，k≤2r。D在ambient上单位，**不能据此断言S9非退化**，也不能将E在K上injective当restricted Gram非退化。实际mixed-kernel的待证内容现被明确压到S9。

## S3b. 实际质量map单射及完整交叉配对重建

本轮[第二cross-Racah稿C3–C11](cdt_odd_paired_cross_racah_injectivity_20261007.md)从完整权重S_y⁻¹给全部leading profiles单位。这里把它精确接回物理L/Z/J，而非将actual cross满行秩笼统套用。

置G*=LD⁻¹Lᵗ、C*=LK5J、H*=JᵗDJ、F*=L diag(1−η)J。对v=(z,q)∈K，first block给唯一θ使
\[
-6DZz+DK_5Jq=L^t\theta.
\]
代入及用LZ=0，准确得
\[
G_*\theta=C_*q,\quad H_*q=C_*^t\theta,
\quad\mathcal Ev=-(Jq+D^{-1}L^t\theta)/6. \tag{S12}
\]
反向由这两kernel方程，(K5Jq−D⁻¹Lᵗθ)/6属于kerL=imZ，唯一重建z，所以这是actual kernel的完整等价，不除G*或H*。

物理F*确为complete cross：在F中c/2=13r+1，因此负节点a_l的centered y=5r−l。节点覆盖y=−r+1,…,5r；middle pair出现两次，η=1/2；其余出现一次，η=0。S(t)=S_y(t−c/2)且T、Q为even-polynomials。故
\[
\boxed{(F_*)_{ij}=\tfrac12\sum_{y=-5r}^{5r}
S_y(y)^{-1}T_i(y^2)Q_j(y^2).} \tag{S13}
\]
原点只半权重，不是完整去掉原点的和。第二Racah单位的首r阶profile证明F*满rowrank r。

对另一个w=(z',q')∈K及其θ'，展开S12并利用两kernel方程和C*+LJ=6F*，得到
\[
\boxed{(\mathcal Ev)^tD\mathcal Ew
=(\theta^tF_*q'+\theta'^tF_*q)/6.} \tag{S14}
\]
若Ev=0，则Jq=−D⁻¹Lᵗθ，H*q=−(LJ)ᵗθ；同时H*q=C*ᵗθ，所以6F*ᵗθ=0。F*满rowrank给θ0，J满columnrank给q0，Z满columnrank给z0。因此**E在实际leading radical上单射**，没有依赖未证actual H或C-small单位。

这仍不是G_K单位：有限域ambient的单位metric在一个单射子空间上可以退化。进一步令τ为θ:K→F^r的rank，S14给rankG_K≤2τ；若k>2τ，源斜率G_K自身不可能满秩。这并不排除R0+8αG_K为单位，因为R0可能补足斜率缺少的方向。此范围限制和单射互不矛盾。S12–14是新增全尺度纸证，首次成功程序仅核S6/S8，未冒称已程序覆盖S12–14或已求实际G_K。

## S4. 实际第一Schur residual的α依赖

固定β∈Z_p^×，在K的补空间取已知modp非退化块，lift为Z_p-GL基；所有选择与α无关，因为S6的leading matrix与α无关。按[四层ladder V11–V12](cdt_odd_paired_value_gram_depth4_nonzero_20261006.md)只除这个unit block，除p得第一residual R_α。写G_K=TᵗEᵗDET，则

\[
\boxed{\overline R_\alpha=\overline R_0+8\bar\alpha G_K.} \tag{S10}
\]

证明：radical-cross及radical-diagonal在原anchor中都被p整除。Schur消去项含两个cross，α变化也有p，因此其α依赖在除p后模p为零。唯有原radical-diagonal的S6导数留下8TᵗA4T，利用S9即得S10。R0包含真实β-source及实际lift的更高项，本文没有将其自由化或删除。

**推论S11。** 若实际G_K非退化，则det(R0+8αG_K)是degree恰k的非零F多项式。至多k个α residue失败；至少p−k≥16r+1个residue使actual anchor的Smith型为0^(8r−k),1^k。对这些α，whole-X归一化为非零常数，而且

\[
v_p D_A(X)=-34r+k\quad(X\in Z_p),\qquad
p^{34r-k}D_A(X)\bmod p\in F^\times. \tag{S11}
\]

k0时空det=1，全部α均适用。S11由真正第一residual unit推出，不需要四层全测，但**条件G_K单位在无限辅助素数上尚未证明**。

## S5. 两个不能跨越的逻辑门槛

S11仅给每个适用prime的source residues；不能让α随n改变再声称同一个数αζ4+βζ5被证明无理。即使每prime只有k≤(p−1)/9个坏residue，也不能仅凭这个密度推出某个fixed rational α无限成功。一个明确的一般反机制：枚举Q为q1,q2,…，令坏集包含前floor((p−1)/9)项中分母为p单位的所有reduced residues；集合大小不超过该界，可作相应根多项式。每个fixed rational最终被包含，所以密度/degree界本身不能提供所需统一性。这不是actual坏集构造或原目标准反例。需要真实fixed-specialization算术，或另一条有明确统一性的选择定理。

单个p~n的响应判据只改变O(nlogn)定标，不降低n²费用；本轮safeA仍为40.314517426059346，当前同一对象解析下界仍不足以证明strict margin。G_K非退化、固定α无限成功、目标无限非零和解析–算术余量是不同条件。

## S6. 新文献、检查计划与范围

正常verified TLS保存De Terán–Dopico《First order spectral perturbation theory of square singular matrix polynomials》（作者稿2008-12-02，18页）[原件](https://gauss.uc3m.es/fdopico/papers/LAA2009-polsing1storder.pdf)/[本地](../literature/cdt_source_radical_pencil_20261007/de_teran_dopico2008_first_order_singular_matrix_polynomials_author.pdf)，SHAc4637952f45e75c0fe34584502861e2b525a8c4c98f40697893e0fcf42f625f9。实际完整读PDF1、4、7、14、15五页，非全文。首次文本输出GBK失败后以UTF8完整补读；下载一次成功，未绕过TLS。该文local Smith、semisimple及核上derivative启发S9–10，但它在C及指定generic perturbations上论述，不证明本文有限域实际G_K或fixed α；S6–11均在这里从实际form自证。

独立NEW [自有源](cdt_odd_paired_source_radical_response_20261007_verify.py)完整静态读取并经过quarter完整静态/纸面预审后，guard在数学运算前exclusive-create，首次且唯一执行1次，exit0 PASS4694checks：旧r1/2/4的实际modp² halfjet代表及原harmonics/weights全部节点，核source α/p与β leading、pencil mass身份；另9个明确一般diagonal residual toy核根数。没有计算actual anchor higher Smith或新的M5单位样本，也没有assert这些代表自身为exact char0 paired lift。O(p²)实际修正不影响身份由S2–6的纸证负责。root实际完整读[结果JSON](cdt_odd_paired_source_radical_response_20261007_verify.json)全部三个case及九toy字段、metadata和入口guard；成功source/JSON/guard永久只读。

source SHA dd457d93d1ce5bc4c80265381d877daf11cabf427b6f4e2100097b6a8e1f06ed；JSON SHA064c740175b4122156c8bc7de242f4ea789ff757606b2ed4c27a96cbf51cdb19；guard SHA50d52715865eeb9cd6929a6b3ae4223c35d44b8294ec6513753860d9ae4656c8。success1、failure0、rerun0、旧/同行execute/import0、Lean0。本文待交叉审阅，尚未冻结；S3b的实际重建与complete cross满秩已独立纸推并经arithmetic和quarter初核，最终审阅仍需完整读最终稿。
