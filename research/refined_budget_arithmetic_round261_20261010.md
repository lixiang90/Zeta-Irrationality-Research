# 第261轮：固定mixed关系的全前缀分母与标准LCM精化障碍

2026-10-10；一次有界纸面预算审核。目标仍为1、ζ(2)、L(2,χ−3)、G的Q线性无关；本稿无新数值无理性/线性无关定理。固定259的来源、普通Taylor坐标s与bare rank3模块；不加primitive、pure函数、参数或新候选，不修改260/main/policy/manifest，不归档。数学程序、CAS、finite_n/prime/map/参数/Padé扫描均0。

新结论有两层，必须分开：某些特殊有理系数组合确有ALL-N的素数类窗口消去，且普通前缀最小分母的真实leading可以严格计算；但CDT原文的literal LCM类型，即使允许任意固定Q(s)换基、n^e与固定index shifts，也不能获得费用小于16/9。结合当前bare关系的实两点坏芽，这个**标准literal LCM、rank3、holomorphic图的精化入口关闭**。非literal素数类过滤模型没有匹配的CDT theorem/完整严格预算，本轮不准入其实现，不将前缀leading直接当成τ。

## R1. 实际读取与对象

实际全文读260 analytic、arithmetic、architecture最终稿，以及259 field最终17525 B稿。260三稿是本轮边界，不修改。固定CDT v2 [arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2) 本轮实际全文读物理66–67、119–124、159–163的定页文本；物理69只在定位6.0.2时读到，未用于新定理。原件218页整体不是本轮FULL。

设δ=q∂q，A=(θ−3(q)+θ−3(q²))/2∈1+3q+q²Z[[q]]。来源仍为

\[
B_\chi(q)=\sum_{n\ge1}\frac{\chi(n)q^n}{n^2(1+q^n)},\quad
C_3(q)=\sum_{n\ge1}\chi_3(n)\{Li_2(q^n)-\tfrac14Li_2(q^{2n})\}.
\]

χ3=χ−3、χ4=χ−4，B3=Bχ3、B4=Bχ4。反证关系H=A(a+bB3+cC3+dB4)，a,b,c,d∈Q，d≠0。选固定C0清四系数为整数，并记

\[
J=C_0H=A(A_c+S),\quad S=B B_3+C C_3+D B_4,\quad
(A_c,B,C,D)=C_0(a,b,c,d)\in Z^4,\quad D\ne0.
\]

这是固定scalar，不改变rank、解析关系或渐近费用。259已付s=q+q²Z[[q]]、q(s)∈s+s²Z[[s]]、Q(t,h)=Q(s)degree4、bare tuple {1,J,θsJ} rank3，其period quotient是irreducible标准SL2 rank2。θs=s∂s。以下始终讨论普通s-Taylor系数，未借Eichler积分的q系数类型作免费降费。

## R2. prefix分母在整数unit和整数互逆坐标下完全不变

对rational Taylor芽F，记L_F(N)为清除全部系数0≤j≤N的最小正整数。若U∈1+sZ[[s]]，U与U⁻¹都是integer unit；截断乘法矩阵为integer unitriangular且逆也integer，所以L_UF(N)=L_F(N)。若Q(s)=s+s²Z[[s]]且formal inverse也integer，两种截断composition同样integer unitriangular，故L_F(Q(s))(N)=L_F(q)(N)。

因此，在固定C0归一化后，

\[
\boxed{L_J^{\,s}(N)=L_J^{\,q}(N)=L_S^{\,q}(N).}
\]

常数A_c∈Z不会改变最小分母。这个等式对每个N成立，包含全部prime powers；它不只比较某个系数，也不是有限头观察。θsJ由系数乘j，故L_{θsJ}(N)整除L_J(N)，但不能据此免费给它一整列更低类型；R4、R6将给实际障碍。

## R3. Eisenstein两个取向：所有p、k的精确分解

由literal divisor sum，

\[
[q^j]B_\chi=\sum_{n\mid j}\frac{\chi(n)(-1)^{j/n-1}}{n^2},
\quad
[q^j]C_3=\frac1{j^2}\left(\sum_{n\mid j}\chi_3(n)n^2
-1_{2\mid j}\sum_{n\mid j/2}\chi_3(n)n^2\right).
\]

CDT物理160页的两个Eisenstein取向正是这个区别；不能将C3的最高平方分母也误乘χ3(p)。对任意p≥5、p∤k，分divisors含p或不含p，得到精确等式

\[
[q^{pk}]B_\chi=(1+\chi(p)/p^2)[q^k]B_\chi,\qquad
[q^{pk}]C_3=(\chi_3(p)+1/p^2)[q^k]C_3.
\]

更一般p^e同样分层：Bχ的因子是Σ_{j=0}^eχ(p)^j/p^{2j}，C3是Σ_{j=0}^eχ3(p)^j/p^{2(e−j)}。因此最高p^{-2e}部分由

\[
T_{r,e}(k)=B\,\chi_3(r)^e [q^k]B_3
 +C[q^k]C_3+D\,\chi_4(r)^e[q^k]B_4
\]

控制。奇e取实际两character；偶e两character均+1。若T_{r,e}(1)≠0且p不除其固定numerator，则[q^{p^e}]S精确v_p=−2e，较低degree只可能有p^{−2(e−1)}。R2移交该首项给J(s)，Frobenius Q(s)^{p^e}≡Q(s^{p^e}) modp再给

\[
v_p([s^{p^e}]J)=-2e,\qquad
v_p([s^{p^e+1}]\theta_sJ)=-2e
\]

（除固定有限bad primes；第二式用A(s)=1+3s+…）。若该parity的numerator为0，本节不假称这个最高次prime-power下界仍成立。ALL-N安全模型仍保留小素数的完整d_N²；未删未审prime powers。

## R4. 真正ALL-N的素数类窗口消去

令r∈{1,5,7,11}，ε3=χ3(r)、ε4=χ4(r)，并定义

\[
F_r=B\epsilon_3+C+D\epsilon_4,\qquad
T_r(k)=B\epsilon_3[q^k]B_3+C[q^k]C_3+D\epsilon_4[q^k]B_4.
\]

四个F分别为B+C+D、−B+C+D、B+C−D、−B+C−D。D≠0保证至少两者非零。由固定divisor公式纸算

\[
(B3_1,C3_1,B4_1)=(1,1,1),\quad
(B3_2,C3_2,B4_2)=(-5/4,-1,-1),\quad
(B3_3,C3_3,B4_3)=(1,1/9,8/9).
\]

这三个symbolic identity用于所有素数，不是扫描prime头。由此T_r的首个非零degree严格为

\[
k_r=\begin{cases}
1,&F_r\ne0,\\
2,&F_r=0,\ B\ne0,\quad T_r(2)=-B\epsilon_3/4,\\
3,&F_r=0,\ B=0,\quad T_r(3)=7D\epsilon_4/9.
\end{cases}
\]

对每个N≥1，设m(N)=max(3,√N)，以下整数清除J与θsJ的**全部**ordinary Taylor prefix；另定义M0=1处理常数prefix：

\[
\boxed{M_N=
\prod_{p\le m(N)}p^{\,2\lfloor\log_pN\rfloor}
\prod_{\substack{p>m(N)\\p\equiv r\ (12)\\k_rp\le N}}p^2.}
\]

证明：小p直接保留d_N²；大p满足p²>N，所以每个j≤N最多含一次p，且j=kp时k<p。R3的p^{-2}部分恰T_r(k)。当p>N/k_r时所有可能k<k_r，T_r(k)精确为0，剩余都是p-integral；当p≤N/k_r，安全保留p²。j非p倍数原source无p分母。integer unit/互逆坐标把整个prefix移交J，θs乘index不增加分母。因此M_N是一个真正逐N整模型，未丢prime powers，未假设有利稀疏子列。

除固定有限bad primes，J在s^{k_rp}有exact v_p=−2，θsJ在s^{k_rp+1}也有exact v_p=−2。因为此前p²部分全0，而q(s)^{k_rp}模p以s^{k_rp}起始且到下一p倍数前不加项；A(s)首3s在下一degree给非零3T_r(k_r)，theta乘k_rp+1为p-unit。因此两条row在同一全尺度上受相同平方prime障碍，不能仅凭θ在degree p乘p就降一列。

## R5. actual prefix leading：与holonomy τ严格区分

从R4的双边逐prime bound，得到

\[
\log L_J(N)=2\sum_{r}\vartheta(N/k_r;12,r)+O(\sqrt N\log N),
\]
\[
\log L_{\theta_sJ}(N)=2\sum_{r}\vartheta(N/k_r;12,r)+O(\sqrt N\log N).
\]

小p的全部prime powers至多2√NlogN；有限bad primes贡献O(logN)。theta witness只把k_rp推迟到k_rp+1，对leading无影响。这里实际提供了upper与lower以及所有prefix，不把“有无穷多个prime系数分母p²”直接冒称leading。

用定模PNT_AP，ϑ(x;12,r)~x/4，故两者真实leading共同为

\[
\boxed{\lim_{N\to\infty}\frac{\log L_J(N)}N
=\lim_{N\to\infty}\frac{\log L_{\theta_sJ}(N)}N
=\frac12\sum_r\frac1{k_r}.}
\]

Primary用Kedlaya作者站点[MIT 2007讲义](https://kskedlaya.org/18.785/dirichlet.pdf)物理1页Theorem1、物理5页Theorem5及weighted theta proof，保存statement公式卡片；不需要uniform modulus或有效error term。PDF本地GET406失败，不称已下载；web原件可读取。经典PNT_AP作为已证定理引用，不声称本轮重证其全部Tauberian过程。

|实际有理系数组合（D≠0）|首非零k_r|共同真实leading|
|---|---|---:|
|全部F_r≠0|四个1|2|
|B≠0，恰一个F_r=0|三个1、一个2|7/4|
|B≠0，两个F_r=0（恰C=0、B=±D）|两个1、两个2|3/2|
|B=0、C=±D|两个1、两个3|4/3|

B=0、C≠±D属于第一行；D≠0下不会有三个F_r为0。这些是∀rational coefficient的代数分类，没有选择参数搜索。数值关系未排除任何一行，不能把generic行或exceptional行单独当成整个目标的证书。

**这个leading是实际普通prefix最小分母，不是CDT determinant费用τ，也不是已获δ。** M_N含residueclass过滤的prime产品，不是原Theorem6.0.2/8.0.1的有限literal LCM数组。即使某行leading下降，也须重证匹配该过滤模型的高维evaluation denominator、balanced分配、全部standing与严格同图预算；本轮没有那份theorem。

## R6. 任意固定rational Laurent换基与n^e都不能免费降literal LCM row

对任意固定Q(s) row

\[
g=u(s)J+v(s)\theta_sJ+w(s),\quad u,v,w\in Q(s),\quad (u,v)\ne(0,0),
\]

仅讨论g本身是原点ordinary Taylor芽且实际声称具有所选literal type的情形。不先乘polynomial清pole后借用原n^e；那会卷积移位n^e，不能免费保留。

u,v,w在0可为Laurent，负阶有限L；除有限bad primes其全部Laurent系数均p-integral。由R3且q(s)^p≡q(s^p) modp，在degree<2p有

\[
p^2J\equiv F_r s^p A(s),\qquad
p^2\theta_sJ\equiv F_r s^p\theta_sA(s)\pmod p.
\]

直接乘rational Laurent系数，congruence在degree<2p−L仍合法：

\[
p^2g\equiv F_r s^p\{uA+v\theta_sA\}\pmod p.
\]

period模块{A,θsA}不可约rank2，故非零uA+vθsA不能属于Q(s)：若有非零rational向量，其导数闭包包含rank1 rational子模块，与不可约矛盾；为0同样与rank2独立矛盾。因此其Laurent展开存在一个固定正degree k≥1、非零rational系数α_k。至少一个class的F_r≠0，Dirichlet定理给该class无穷大素数p；去掉有限bad primes并取p>k+L，得到

\[
\boxed{v_p([s^{p+k}]g)=-2,\qquad p\nmid(p+k).}
\]

若声称g的实际coefficient type为

\[
n^e\prod_{h=1}^{R}d_{\lfloor b_hn+c_h\rfloor},
\quad e\in N,\ b_h\ge0,\ c_h\text{固定},
\]

则n=p+k使n^e为p-unit。对固定b_h<1，大p时floor(b_h(p+k)+c_h)<p；对b_h≥1，至多含一次p，因为b_h(p+k)+c_h<p²。要清exact p²，**该row必须有至少两个b_h≥1**。所有固定shifts和固定scalar均不能改变此结论。此证明直接作用于原g，不对polynomial gauge继承n^e。

## R7. 从row障碍到原Definition8的费用下界，非“prime头等于τ”

同bare rank3空间的任意Q(s) basis最多一条row落在Q(s)，故至少两条nonconstant row满足R6。对其任意真正有效的literal array b，每nonconstant row至少两个entry≥1。

实际FULL读CDT物理122页Definition8.0.2。对任意threshold k、任意degree n_j、任意row标签i_j，若i_j是nonconstant，

\[
\#\{h:k\le b_{i_j,h}n_j\}\ge2\,1_{k\le n_j}.
\]

这个rowwise不等式不要求两row的两个大entry在同一列。求sum(j,h)、再取原balanced i与近uniform n的max，当前Den_N逐点至少是baseline两列(0,1,1)的Den_N。原Definition的所有limits保序，故

\[
\boxed{\tau^{\flat\flat}(b)\ge
4\int_0^1\min\{2/3,1-t\}\,dt=16/9.}
\]

balanced baseline可把一条忽略row分配到最小1/3 degree、两nonconstant row分配到其余2/3；这也正是Remark8.0.6给baseline的等号。原物理66页e∈N^m与6.0.5明确定义τsharp；各integrand非负，故τsharp≥0。因此**全部有效标准literal类型，任何上述固定rational basis、n^e或fixed shifts，都不能把当前16/9降下来**。

这与R5的actual prefix leading下降没有矛盾：R7约束的是所选theorem必须使用的literal array；它没有声称所有真实prime-filtered arithmetic content的leading都≥2，R5已经给反例。将别的原文§8数组值或actual prefix leading直接贴给本对象的τ均不合法。

## R8. selected refined-admission决定与精确未付边界

独核Root提供的bare实两点账如下：r=±√3对应t=∞，R4=(3+r²)³/[32r(1+r²)]取±9√3/16。forcing在u=1/t=0的constant F0=b±9√3 d/16非零（b,d rational，d≠0）。变换CDT算子得

\[
\mathcal D_t=\frac9u(\theta_u-1)^2+\text{terms regular in the indicial expansion}.
\]

double exponent1 Frobenius使每个到达解含(F0/18)u log²u；homogeneous差最多一次log，finite ramification不消去二次log。因此任何同bare basis共同meromorphic的holomorphic φ都必须避α=(1−√3)/2、β=(1+√3)/2；rational换基不逃避它，因为原J是各basis row的rational组合。260已有实两点Landau规范给|φ′(0)|<11/2。

由exp(7/4)的0–4项和34193/6144>33792/6144=11/2，

\[
\lambda<\log(11/2)<7/4<16/9\le\tau^{\flat\flat}+\tau^\sharp.
\]

当前标准LCM原文§6–8 holomorphic入口连positive denominator都没有；只改Bost–Charles numerator/convexity不能重入。必要先有actual新费用降低δ>16/9−log(11/2)>1/36；R7排除了这份费用来自当前任何literal-array换基、n^e或fixedshift。

R4–R5确实支付了一个非literal ALL-N prefix模型，但未支付其matched evaluation/holonomy theorem，而且generic F_r全非零时实际leading仍2。故本轮**不准入**该prime-filtered降费设想的实现，也不借它自动开启素数/图/Padé搜索。停止的是固定bare、标准literal费用及所选holomorphic refined interface；不是全部arithmetic holonomy、不同meromorphic-map定理、其它来源或目标四项独立性的不可能定理。

唯一未付的新接口必须直接把R4实际素数类过滤模型接到同一rank3 evaluation对象，逐N证明完整有限处费用与其balanced leading，并在不可填实两点允许的同图上取得positive denominator和strict净预算；generic与exceptional所有rational关系都须覆盖。本轮没有该证书，selected标准精化窗口已闭，不另提新primitive或候选。
