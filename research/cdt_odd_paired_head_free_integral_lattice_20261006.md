# 配对消头空间的真实整数基、饱和性、指数与范数

日期：2026-10-06。NEW 纸面证明，quarter_actual_rank。所有旧/同行数学 MD、PY、JSON、manifest 仅读；没有数学 producer 执行、import、重跑，没有外部 Lean。本文补冻结 P15 空间的实际整数接口，不继承完整3n矩阵的无穷非零或解析预算。

## I1. 输入与实际格

本轮实际完整重读冻结 `cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md` P1–P9，SHA93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8，全文无截断。它的P15规定

\[
\mathcal A_n=\{P\in\mathbf Q[t]_{<3n}:P(m)/d_m=P(m')/d_{m'},\ 1\le m\le n\},
\quad m'=2n+1-m,
\quad d_j=(j)_{6n+1}=\frac{(6n+j)!}{(j-1)!}.
\tag{I1}
\]

取实际整数值格

\[
\mathcal M_{3n}=\bigoplus_{i=0}^{3n-1}\mathbf Z f_i,
\qquad f_i(t)=\binom{t-1}{i},
\qquad A_{n,\mathbf Z}=\mathcal A_n\cap\mathcal M_{3n}.
\tag{I2}
\]

整数平移的Vandermonde恒等式说明f_i与旧binom(t,i)基的变换是整数unitriangular、逆亦整数，所以这是同一个原整数值格，没有暗换局部模型。以下显式界皆按指定基范数定义，不能把一种规范的height免费代入另一种解析estimate。

## I2. 连续整数节点给split evaluation

Evaluation E:M3n→Z2n，P↦(P(1),…,P(2n))。前2n个f_i的矩阵

\[
E_{j,i}=\binom{j-1}{i},\quad 1\le j\le2n,\ 0\le i<2n
\tag{I3}
\]

是lowertriangular、diagonal1，故整数unimodular。后n个f_i，i≥2n，全部在这些节点为0。特别E是split surjective，kernel的实际整数基正是f_{2n},…,f_{3n−1}；不需先乘(2n)!清分母。

Cardinal interpolation polynomials为

\[
L_j(t)=\binom{t-1}{j-1}\binom{2n-t}{2n-j},\quad1\le j\le2n.
\tag{I4}
\]

它们integer-valued，degree2n−1，并满足L_j(l)=δjl：l<j时第一factor为0，l>j时第二为0，l=j时两factor均1。其实际Newton展开是

\[
L_j=\sum_{i=j-1}^{2n-1}(-1)^{i-j+1}\binom{i}{j-1}f_i.
\tag{I5}
\]

证明在l≤2n评价，用binom(l−1,i)binom(i,j−1)=binom(l−1,j−1)binom(l−j,i−j+1)与(1−1)^{l−j}即可；degree相同故多项式身份成立。因此(L_1,…,L_{2n},f_{2n},…,f_{3n−1})亦是M3n的unimodular整数基。

## I3. 去掉实际gcd后，A_Z是饱和且有显式完整基

定义

\[
g_m=\gcd(d_m,d_{m'}),\quad p_m=d_m/g_m,\quad q_m=d_{m'}/g_m,
\quad\gcd(p_m,q_m)=1.
\tag{I6}
\]

I1的raw row变为primitive约束q_mP(m)−p_mP(m')=0。在evaluation坐标中各pair完全分离，约束mapC:Z2n→Zn的第m项是q_my_m−p_my_m'。由gcd1每项surjective，故C满射。因而

\[
\mathcal M_{3n}/A_{n,\mathbf Z}\simeq\mathbf Z^n,
\tag{I7}
\]

没有torsion，A_Z已饱和，其到自身saturation的index为1。准确整数基是

\[
\boxed{G_m=p_mL_m+q_mL_{m'},\ 1\le m\le n;
\qquad f_i,\ 2n\le i<3n.}
\tag{I8}
\]

证明：每个pair的整数解是(y_m,y_m')=(p_mz_m,q_mz_m)，z_m∈Z。先用Σz_mG_m取得所有节点值，再减去它，只余kernel，I2给完整整数基。故rank2n，无漏掉的finite-place index。

更明确地，可取整数x_m,y_m使p_my_m−q_mx_m=1，令H_m=x_mL_m+y_mL_m'。则(G_m,H_m)在该pair的2×2坐标det1。所有G,H加n个kernel向量给M3n的完整GL3n(Z)基。可选|x_m|≤p_m、|y_m|≤q_m（先在模q_m解y_m，特殊p=q=1另取x=0,y=1）。因此不需一个未计算的巨大有限素数complement index；其archimedean大小仍须付。

## I4. Raw约束与raw pair基的准确指数

Raw约束mapC_raw的像是⊕m g_mZ，因为每个primitive pair map满射。其cokernel为⊕m Z/g_mZ；raw rows在primitive row lattice中的index正是∏g_m，Smith factors是diag(g_m)的Smith factors（无需宣称g_m本身已按整除次序排好）。

Raw pair基\widetilde G_m=d_mL_m+d_m'L_m'=g_mG_m。若加同一个完整kernel格，所得子格\widetilde A满足

\[
\boxed{[A_{n,\mathbf Z}:\widetilde A]=\prod_{m=1}^ng_m.}
\tag{I9}
\]

实际factorial identity

\[
d_j=(6n+1)!\,b_j,\qquad b_j=\binom{6n+j}{j-1},
\quad g_m=(6n+1)!\gcd(b_m,b_{m'}).
\tag{I10}
\]

故∏g_m≥((6n+1)!)^n，log指数至少6n²logn+O(n²)。这补了此前raw-row费用中的巨大gcd，不能再按raw height当saturated basis的费用。另一方面对同一个restricted form，raw Gram determinant严格等于(∏g_m)^2乘saturated Gram determinant。换到primitive basis同时改变real大小与finite-place content，I9本身不创造正margin。

## I5. Newton范数下，实际基费至多n²而非n²logn

设||P||_{N,1}为I2 Newton系数的ℓ1norm，||P||_{N,2}为Euclidean norm。由I5及hockey-stick恒等式，

\[
\|L_j\|_{N,1}=\sum_{i=j-1}^{2n-1}\binom{i}{j-1}=\binom{2n}{j}\le4^n.
\tag{I11}
\]

正整数b_j随j严格增加（相邻ratio(6n+j+1)/j>1）。所以

\[
1\le p_m,q_m\le C_n:=\binom{8n}{2n-1},\quad
\|G_m\|_{N,2}\le\|G_m\|_{N,1}\le2C_n4^n,
\quad\|f_i\|_{N,2}=1.
\tag{I12}
\]

在M3n的Newton-Euclidean规范下，定义A_Z的rank2n covolume为I8基平行多面体在其real span中的volume。Hadamard给全n明确bound

\[
\boxed{\operatorname{covol}_{N,2}(A_Z)\le(2C_n4^n)^n,}
\]
\[
\log\operatorname{covol}_{N,2}(A_Z)
\le(18\log2-6\log3)n^2+o(n^2).
\tag{I13}
\]

这里logC_n=(16log2−6log3)n+o(n)，直接来自阶乘Stirling。相同显式界控制GL3n(Z)complement的单列norm。I13是实际规范下的安全upper fee，非最佳值；它不能免费代替右轮廓上的polynomial values或Vandermonde energy。

## I6. 同一Newton规范下的准确covolume与Plücker数据

令e_j为Newton评价row，其i项binom(j−1,i)，i0..3n−1。Primitive约束矩阵的n个rows为

\[
\mathsf C_m=q_me_m-p_me_{m'}.
\tag{I14}
\]

它是整数满射，全部n阶minors的gcd为1。其kernel正是A_Z。标准Euclidean exterior Hodge star将primitive row wedge对应到primitive kernel wedge；或用I3的unimodular补全与Cauchy–Binet证明，得到准确身份

\[
\boxed{\operatorname{covol}_{N,2}(A_Z)^2=\det(\mathsf C\mathsf C^{\mathsf T}).}
\tag{I15}
\]

此式是可执行的n×n整数determinant，不留未知saturation常数。所用node inner products亦完全明确：

\[
e_je_l^{\mathsf T}=\sum_i\binom{j-1}{i}\binom{l-1}{i}
=\binom{j+l-2}{j-1}.
\tag{I16}
\]

因此I15每个entry是四个上述binomial，分别乘q_mq_l、−q_mp_l、−p_mq_l、p_mp_l。I8的maximal minors同样给全部primitive Plücker坐标；有限素数的min valuation皆0，因为A_Z是完整direct summand。**这不表示restricted Gram form的Smith或Gauss valuation皆0**：Gram仍取决于actual U,V/W及其在该subspace的退化。

## I7. 另一个自然规范的精确n²费用与不能混同的界

在unimodular基(L_1,…,L_{2n},f_{2n},…,f_{3n−1})中取系数Euclidean规范||·||_E。这是evaluation加kernel坐标的规范。I8此时具有互不相交pair supports，故

\[
\operatorname{covol}_{E}(A_Z)
=\prod_{m=1}^n\sqrt{p_m^2+q_m^2}.
\tag{I17}
\]

因为q_m/p_m=d_m'/d_m>1且p_m≥1，logcovolE≥Σlog(d_m'/d_m)。相邻d_{j+1}/d_j=(6n+j+1)/j，严格求和给

\[
\sum_{m=1}^n\log\frac{d_{m'}}{d_m}
=\sum_{j=1}^{2n-1}\min(j,2n-j)\log\frac{6n+j+1}{j}.
\tag{I18}
\]

除以n²，Riemann极限存在：xlog(1/x)的0端可积，有限小段直接夹逼。因此

\[
\log\operatorname{covol}_E(A_Z)
\ge I n^2+o(n^2),\qquad
I=112\log2+18\log3-49\log7>0.
\tag{I19}
\]

I是∫₀¹xlog((6+x)/x)dx+∫₁²(2−x)log((6+x)/x)dx，正性由integrand直接给出。计算用F''(z)=logz，F(z)=z²logz/2−3z²/4：I=F8−2F7+F6−F2+2F1。I19是指定evaluation规范下的真lower bound，**不是原Newton规范covolume、restricted解析det或actual arithmetic cost的lower bound**。Norm转换本身是n-dependent unimodular矩阵，finite index1不令其real norm为1。

还可给任何Newton整数basis的真实高度障碍：第一pair有p1=1、q1=C_n。Basis的pair-coordinate gcd为1，所以至少一个basis vectorP在t=2n的非零值绝对值≥C_n。因|P(2n)|≤2^{2n−1}max_i|Newtoncoeff_i P|，任意整数basis至少一个vector满足

\[
\max_i|a_i|\ge C_n/2^{2n-1},
\quad\log\max_i|a_i|\ge(14\log2-6\log3)n+o(n).
\tag{I20}
\]

常数正由2^14>3^6。它证明无法找所有列固定高度的整数basis，不把一个列height偷换成n²总费用下界。

## I8. 辅助素数restriction的准确结构，不继承full unit blocks

这一节是独立局部lemma，非无穷nonzero结论。取n=2r、p=9r+1 prime，正节点z1..4r。全部d_z=(z)12r+1恰vp1；令H(t)=(t)3r，Wilson给

\[
d_z/p\equiv-H(z)\pmod p.
\tag{I21}
\]

因为(z+12r)!上限<2p、z−1<p，除去唯一p后其factorial reduction是−(3r+z−1)!/(z−1)!。H(z)在这些正节点为unit。由于vp(g_m)=1，primitive pair约束modp等价P(z)/H(z)=P(z')/H(z')，z'=4r+1−z。I3确保A_Z/p仍准确维数4r，没有modp saturation损失。

在negative nodes0,−1,…,−(3r−1)评价的kernel中，P=HQ，degQ<3r。约束化为Q(z)=Q(4r+1−z)。差polynomial在4r个不同正节点消失而degree<3r，故identically zero。p为奇素数，因此反射even Q的dimension为ceil(3r/2)。准确negative-evaluation rank是

\[
\boxed{4r-\lceil3r/2\rceil=\lfloor5r/2\rfloor,}
\tag{I22}
\]

小于full3r evaluation rank。这说明将原完整Hermite unit determinant直接限制到A_n并宣称constant-unit reduction是不合法的。Actual leading diagonal form在image上是否nondegenerate、weak jet block的实际指数与最终目标specialization无限nonzero，需另证；本文未把I22当这些结论的替代。

## I9. 实际basis到全部finite-place安全minors的桥

本节先选固定正整数D清冻结P1中r的分母，将原form乘D；其a=−Dr、b=D均整数，形式X系数也是整数倍。令B_N(X)为这个3n维form在Newton整数值基中的矩阵，S为I8的3n×2n整数basis矩阵。相比未清r分母的actual scalar，以下det多乘D^{2n}，在arithmetic和analytic两处都必须计，只贡献O(n)。实际新多项式是

\[
J_A(X)=\det(S^{\mathsf T}B_N(X)S).
\tag{I23}
\]

它不是旧3n determinant的scalar multiple。由I8的direct-summand性质，S全部2n阶minors的gcd为1；由两次Cauchy–Binet，任何prime上J_A的Gauss valuation至少为B_N全部2n阶minors的共同valuation lower bound。此桥没有隐藏的basis denominator或finite index，但不保证det的nonzero specialization。

转回monomial formB_M时，整数平移f_i(t)=binom(t−1,i)相对binom(t,i)是GL3n(Z)。先用binom(t,i)=(t)_falling_i/i!；其numerator到monomial是整数unitriangular。任意2n-row、2n-column minor因此必须付相应row/column factorials。一个无需知道实际Plücker支持的安全扣除是

\[
E_p^{\max}=2\sum_{i=n}^{3n-1}v_p(i!),
\tag{I24}
\]

因为v_p(i!)递增，这正是最大的2n项，而不是first2n项。若B_M全部2n阶minors的共同界为λp，则严格vpGauss J_A≥λp−Emax。原degree仍<3n，不能免费换成degree<2n恢复零阶layout的first2n factorial费用。

特别，对sqrt(8n)<p≤6n，冻结P5的实际F_s,ρ(m)界给可用有限模型

\[
v_p^{\mathrm{Gauss}}J_A\ge
\min_{\substack{\sum_\rho m_\rho=2n\\0\le m_\rho\le2q_\rho+2}}
\sum_\rho F_{s,\rho}(m_\rho)-E_p^{\max}.
\tag{I25}
\]

证明是对每个2n阶monomial minor按residue form分解做行/列Laplace展开，再用P5所有阶minors的统一界；随后用I24及I23。它是安全Gauss bound，非actual content equality，也没有继承旧优化的数值常数。

所有小prime另有直接全n界vpGauss J_A≥−2ns floor(log_p(8n))：整数值Newton基的导数lcm只用i≤3n−1，harmonics最多8n，原fixed-s form的每个entry有该安全界，S整数不使其变差。对p>6n整个B_N积分性由较长H_(2n+j)的可能单p分母被W_j中binomial三次幂清除，J_A亦integral。故本lemma已经给全finite-place可整化接口，尚未计算足够便宜的signed-content主率。

## I10. 本轮完成范围与剩余gate

已补成可使用的实际构造：完整整数基I8，所有有限素数饱和/direct-summand结论，raw row/pair的精确指数I9，指定Newton规范下明确的全尺度upper fee与exact integer Gram/Plücker计算，另一规范下真实n²lower fee与任意Newton基的单列高度障碍。I8保持既存paired-head cancellation与维数2n，未加入虚构数值关系。

I23–25进一步补了实际新basis到全部finite-place安全整化的桥，明确largest2n factorial gate。还没有补：该restricted形式在每个有理目标的无限nonzero、足够便宜的signed Gauss预算主率、与I8相容的right-contour解析determinant能量及strict margin。I22给新的真实局部结构供后续nonzero证明使用。没有新的ζ/L/Catalan无理性、线性无关性或Lean定理。

本文全部新推导为纸面证明；没有自有数学producer，同行producer也未运行。无需新文献定理：整数插值、Bezout、Cauchy–Binet、Wilson、Stirling均在正文给出用于本命题的实际步骤。来源收据另NEW保存，旧稿及历史收据不改。正文完成后作者全文回读并交同行独审，最终冻结另报告。
