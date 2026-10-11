# 实际 Gamma 系统的二次 Taylor 周期：完整反射列、零不变量与齐次张量的界限

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority为主报告 §§181–185 与 delivery_balanced_gamma_direction SHA b3a9c11266257168b103c14a13541b503dc53df1d7ad56c327c8ea83a5c43d50，588冻结记录（583数学、5guards）只读。唯一NEW纯纸面主稿。旧/同行数学producer、results、guards及prime表不执行、import或rerun，未创建数学producer、未扩素数表、无Lean。本稿构造同一齐次系统的真正Q-Taylor二次与Wronskian族，求完整反射列和jump，证明它们的实际函数rank；所得界限只约束原三点齐次张量场，不约束新非齐次/relative extensions。

## 1. 原rank9模型与低权校准对象

本轮actual FULL读最新Gamma G1–G19/all7节及其冻结root独审R1–R7/全部七节；authority §§181–185实际完整读取。588 audit完整JSONparse、顶级schema/current_progress及物理SHA，不称人工全文或本人逐物理审计588条。直接使用原参数
\[
a=(\tfrac12^5,\tfrac15,\tfrac25,\tfrac35,\tfrac45),\quad
r=9,\quad\Lambda=2^{10}5^5,\quad c=\Lambda^{-1},
\]
\[
L=D^r-\Lambda tP(D),\qquad
P(X)=\prod_{i=1}^r(X+a_i),\quad D=t\partial_t .
\tag{T1}
\]
本稿不把该齐次L改成原ordinary endpoint quasi-period。完整Frobenius与正则部分保持
\[
\Phi(s,t)=t^s A(s,t),\quad
A(s,t)=\sum_{n\ge0}\Lambda^n
\frac{\prod_i(a_i+s)_n}{(1+s)_n^r}t^n,\quad
\phi_j=[s^j]\Phi,\quad\eta_j=[s^j]A,\quad0\le j<r.
\tag{T2}
\]
\(L\Phi=s^rt^s,\ \eta_0(0)=1,\eta_j(0)=0\ (j>0)\)。
取q=2πi，MUM全部作用为
\[
T_0\phi_j=\sum_{b=0}^j\frac{q^b}{b!}\phi_{j-b},\qquad
N\phi_j=\phi_{j-1},\quad\phi_{-1}=0 .
\tag{T3}
\]
T0=exp(qN)，N为单Jordan块。

低权校准另取r=3或5、a_i=1/2全部r次、Λ=2^(2r)；同样T1–T3，
\(h_n=\binom{2n}{n}^r\in\mathbf Z\)。
这些低权模型是明确校准族，不冒称它们等于rank9原source、也不把Apéry第三阶方程当此超几何方程。

## 2. 自对偶 concomitant 完全固定 Frobenius bilinear form

相对dt/t作formal adjoint，D*=-D、P(-D)t=tP(-D-1)。
三组参数都在a↦1−a下不变，r奇数，故
\[
\boxed{L^*=-L.}
\tag{T4}
\]
写L=Σ_(k=0)^r a_k(t)D^k，其中a_r=1−Λt、k<r的a_k为−Λt乘rational常数。一个实际Lagrange concomitant为
\[
C_L(f,g)=\sum_{k=1}^r\sum_{j=0}^{k-1}
(-1)^jD^j(a_k f)D^{k-1-j}g,\qquad
DC_L=fLg-gL^*f .
\tag{T5}
\]
将C_L(f,g)与C_L(g,f)平均，得symmetric bilinear form
\(\mathcal B(f,g)=\mathbf j(f)^tS(t)\mathbf j(g)\)，
\(\mathbf j(f)=(f,Df,\ldots,D^{r-1}f)^t\)。
所有S entries在Q(t)，且
\[
D\mathcal B=fLg+gLf,\quad
S_{ij}=0\ (i+j>r-1),\quad
S_{i,r-1-i}=(-1)^i(1-\Lambda t).
\tag{T6}
\]
T5逐项求D时相邻summands抵消，证明identity；最高anti-diagonal只来自k=r的最高derivative，r−1偶数保证平均后sign不改。
因此
\[
\boxed{\det S=(1-\Lambda t)^r,\quad
S(0)=J,\quad J_{ij}=(-1)^i\delta_{i+j,r-1},\quad J^{-1}=J.}
\tag{T7}
\]
detJ=1；anti-triangular determinant不受低于anti-diagonal的entries影响。

令Y=(D^iφ_j)_(0≤i,j<r)。T5–T6给YᵀSY constant。
沿t↓0的固定正实log支，Y=exp((logt)N)+O(t(1+|logt|)^C)，
S=J+O(t)。因为NᵀJ+JN=0，且t任意固定log幂趋0，准确
\[
\boxed{Y^tS(t)Y=J,\quad
YJY^t=S(t)^{-1}.}
\tag{T8}
\]
这一步确定实际Frobenius basis的form，不只是声称存在某个未知orthogonal comparison。

S的最后row只含S_(r−1,0)=1−Λt。解Sx=e0迫x0=0，r≥3，故
\[
\boxed{\sum_{i=0}^{r-1}(-1)^i\phi_i\phi_{r-1-i}=0.}
\tag{T9}
\]
它是唯一orthogonal scalar二次不变量的**恒等零投影**。不能把它当新非零period、目标常数或新irrationality证书。
含导数的同一不变量也完全明确：
\[
\boxed{\sum_{i=0}^{r-1}(-1)^i
D^a\phi_i\,D^b\phi_{r-1-i}=(S^{-1})_{ab}\in\mathbf Q(t)
\quad(0\le a,b<r).}
\tag{T10}
\]
它们可以非零，但只是原base-field rational rows，并非依赖κ5或κ7的填洞。

## 3. 完整实际反射列与低权 normalization

Γ稿及本轮actual PDF读取Bloch–Vlasenko Proposition26给
\[
(T_c-I)\phi_j=\kappa_j\psi,\quad
\psi=(T_c-I)\phi_0\ne0,\quad\kappa_0=1,\quad\kappa_1=0,
\]
\[
\kappa(s)=
\frac{\Gamma(1+s)^{15}}{\Gamma(1+2s)^5\Gamma(1+5s)}
\quad(r=9),
\qquad
\kappa^{(r)}(s)=\frac{\Gamma(1+s)^{2r}}{\Gamma(1+2s)^r}
\quad(r=3,5).
\tag{T11}
\]
有限local exponents为0,…,r−2与r/2−1，最后为非整数半数，故Tc为rank-one involutive reflection。
若ψ=Σw_iφ_i，则Tc=I+wκᵀ、κᵀw=−2。
T8使TcᵀJTc=J。其−1 eigenline与+1 hyperplane kerκᵀ正交，故
\[
\boxed{\mathcal K_{r-1}:=\kappa^tJ\kappa
=\sum_i(-1)^i\kappa_i\kappa_{r-1-i}\ne0,\quad
w=-2J\kappa/\mathcal K_{r-1}.}
\tag{T12}
\]
非零性亦由nondegenerate invariant form与reflection的正交eigenspace分解保证。因此本稿补足原仅知connection行的实际反射列，未假设其它未知connection rows。

对rank9，\(\mathcal K_8=[s^8]\kappa(s)\kappa(-s)\)，odd log-Gamma项全部抵消。已读G8的even项给
\[
\mathcal K_8=-\tfrac{195945}{2}\zeta(8)
+159300\zeta(2)\zeta(6)+\tfrac{119025}{2}\zeta(4)^2
-155250\zeta(2)^2\zeta(4)+33750\zeta(2)^4
=30240\zeta(8)=q^8/80.
\tag{T13}
\]
最后只用ζ(2)ζ(6)/ζ(8)=5/3、ζ(4)²/ζ(8)=7/6、ζ(2)²ζ(4)/ζ(8)=35/12、ζ(2)^4/ζ(8)=175/24；逐项清分母可纸核，没有常数程序。
得到完整实际jump generator
\[
\boxed{\psi=-\frac{160}{q^8}
\sum_{i=0}^8(-1)^i\kappa_{8-i}\phi_i.}
\tag{T14}
\]
这个q^−8在此是明确的connection列常数，不是把Tate-normalized basis冒作Q-Taylor。

低权的全部必要normalization如下：

|r|实际Γ行的重要项|\(\mathcal K_{r-1}\)|完整列系数 \(w_i/((-1)^i\kappa_{r-1-i})\)|
|---:|---|---|---|
|3|κ2=−3ζ2|−6ζ2=q²/4|−8/q²|
|5|κ2=−5ζ2，κ3=10ζ3，κ4=55ζ4/4|90ζ4=q⁴/16|−32/q⁴|
|9|原κ0…κ8全部依T11|30240ζ8=q⁸/80|−160/q⁸|

例如r5的κ3确为10ζ3，但同rank5系统的二次不变量仍在T9中恒等为0；这不是ζ3无理性的新证明。r3齐次Γ行只到weight2，不能从不存在的rank3 κ3齐次列免费取得Apéry的ζ3目标。

## 4. 真实log-canceling Taylor basis与全部conifold jump

对任意even h≤r−1定义
\[
I_h=\sum_{i=0}^h(-1)^i\phi_i\phi_{h-i}
=[s^h]\Phi(-s,t)\Phi(s,t)
=[s^h]A(-s,t)A(s,t)\in\mathbf Q[[t]].
\tag{T15}
\]
指数t^s与t^−s准确相消，没有取real part、删去unknown log term或交换analytic parts。
MUM-fixed Sym²V的完整constant tensor basis为
\[
I_0,I_2,\ldots,I_{r-1}\quad\text{在投影前的formal tensor层面};
\qquad I_{r-1}=0\quad\text{在实际scalar层面}.
\tag{T16}
\]
证明完整性：N降低索引sum一阶，每条anti-diagonal的系数recurrence是a_(i+1)=−a_i。对sum≤r−1，commutative对称性只允许even sum；sum≥r时边界先迫端系数0，再迫全部0。因此kerN维数(r+1)/2。零关系只删去最后一行；实际rank在下一节证明。

令 \(\mathcal W(f,g)=fDg-gDf\)。对odd h≤r−2定义
\[
J_h=\sum_{i=0}^h(-1)^i\mathcal W(\phi_i,\phi_{h-i}).
\]
准确Taylor表达为
\[
\boxed{J_h=[s^h]\{A(-s)DA(s)-DA(-s)A(s)
+2sA(-s)A(s)\}\in\mathbf Q[[t]].}
\tag{T17}
\]
例如J1=2(η0Dη1−η1Dη0+η0²)，J1(0)=2，其它J_h(0)=0。derivative作用在t^s带来的2s不可删除。
在Λ²V的formal tensor层面，kerN完整basis为odd anti-diagonals h1,3,…,r−2，维数(r−1)/2；recurrence同T16，但alternating性只允许odd sum。Wronskianmap的injectivity在下一节证明。

以上basis的**全部**reflection jump为
\[
\boxed{\Delta_c I_h=
2\psi\sum_{i=0}^h(-1)^i\kappa_i\phi_{h-i}
+\psi^2\mathcal K_h,\quad
\mathcal K_h=[s^h]\kappa(s)\kappa(-s),}
\tag{T18}
\]
\[
\boxed{\Delta_c J_h=
2\sum_{i=0}^h(-1)^i\kappa_i
\mathcal W(\psi,\phi_{h-i}).}
\tag{T19}
\]
T18由Tcφ=φ+κψ逐项展开；T19的ψ² alternating项为0，两个cross sums因h odd合并成factor2。ψ在T12–T14已明确为原φbasis的完整列，κ全部由T11决定；这里没有丢掉κ0源项、剩余log、Dψ或未知列。
对I_(r−1)，T12使T18右端恰0，与T9一致。

rank9实际候选为
\[
\boxed{\mathcal I=(I_0,I_2,I_4,I_6),\qquad
\mathcal J=(J_1,J_3,J_5,J_7).}
\tag{T20}
\]
它们确实超出了旧linear analytic-part η package，但同一个数值假设κ5=u或κ7=u并不自动使T18/T19消失。下一节对全部rational-function变基给严格结论，而非仅查看个别公式的一项。

## 5. 实际O(r) monodromy与函数rank，不能借tensor维数代替

三组超几何parameters均满足a_i−1非整数，所以monodromy irreducible。
其selfdual multiplicative参数在inversion下不变，reflection special eigenvalue为−1。
regular单Jordan unipotent T0还排除imprimitivity：若它循环ℓ>1个非零blocks，block-cycle characteristic polynomial会含全部ℓ次单位根，违反unipotent；若它逐block固定，每block至少有一个fixed vector，违反dimker(T0−I)=1。因此完整hypergeometric group primitive。T0在projective群中的无穷阶亦排除scalar shift of finite group。

本轮实际FULL读Beukers–Heckman PDF21–23的Proposition6.1与Theorem6.5，所有hypotheses已逐项满足，且无需scalar shift（取d=1）。于是
\[
\boxed{\overline{\operatorname{Mon}}^{\,Zar}=O(r,\mathbf C)
\quad(r=3,5,9).}
\tag{T21}
\]
这里使用已有monodromy分类定理，不宣称自证其分类。regular-singular differential Galois group等于monodromy Zariski closure的使用范围见同原件PDF2/20。原κ_j数值是否有理不改变T1参数与这一定理的hypotheses。

在O(r)上Sym²V是1维metric与irreducible traceless部分之和；Λ²V是irreducible（r3、5、9的so(r) adjoint）。可用coordinate rotations自证：所有off-diagonal symmetric matrices及traceless diagonals相互生成，skew matrices同理由rotations生成。实际scalar product map Sym²V→germs的kernel是monodromy invariant。metric被T9杀掉，φ0²非零使traceless部分不能全被杀，所以kernel恰metric。同理Wronskianmap Λ²V→germs非零，因W(φ0,φ1)→1，故其kernel为0。因此
\[
\boxed{\operatorname{rank}_{\mathbf C(t)}
\{\phi_i\phi_j:0\le i\le j<r\}
=r(r+1)/2-1,\quad
\operatorname{rank}_{\mathbf C(t)}
\{\mathcal W(\phi_i,\phi_j):i<j\}
=r(r-1)/2.}
\tag{T22}
\]
证明这里实际是function rank：选上述irreducible image的constant basis，若Σr_a(t)f_a=0、r_a∈C(t)，在普通t取非零value向量，continuation的monodromy orbit张成整个irreducible image；single-valued coefficients迫r(t)消去这个全orbit，故r_a(t)=0。非零value在普通开集存在，得到r_a恒0。这不是从formal tensor维数直接假设scalar functions独立。

特别T20中各四行在C(t)、从而Q(t)上独立；没有nonzero rational function落在任一nontrivial irreducible image内。于是
\[
\boxed{\operatorname{rank}_{\mathbf Q(t)}(1,\mathcal I)
=\operatorname{rank}_{\mathbf Q(t)}(1,\mathcal J)=5
\quad(r=9).}
\tag{T23}
\]
r3/5对应ranks分别2与3；完整scalar-product ranks5与14，完整Wronskian ranks3与10。r9完整ranks44与36，均不同于原rank9，也不同于所选Taylor package rank5。

## 6. 关系假设仍不能填洞：完整三点齐次field的精确范围

任一 \(\sum_h r_h(t)I_h\) 或 \(\sum_h r_h(t)J_h\)，r_h∈C(t)，在MUM loop已fixed，因为T15/T17是真Taylor族。若它在conifold loop也fixed，则在原三点sphere的monodromy generators T0、Tc都fixed；整个monodromy fixed。由T21及Picard–Vessiot fixed-field property，它属于C(t)。T22–T23因此强制所有nonrational-package coefficients为0。
\[
\boxed{\text{在任一T20 package及其C(t)linear变基内，
唯一conifold-invariant行是另外加入的rational rows。}}
\tag{T24}
\]
这对实际κ5=u或κ7=u的数值假设仍成立；hypothesis不会改变原L的Galois group或真实function ranks。
所以这些显式二次族没有得到一个nontrivial Q-Taylor、relation-filled row。它们的jump不能只被口头压成κ5−u或κ7−u而删掉T18/T19的其它部分。

更广但仍准确的范围是：原齐次系统的Picard–Vessiot field内，任何有限tensor/rational differential expression，若真正在0、c两完整loops都fixed，必在C(t)；这些loops生成原全部三点monodromy。metric或higher invariant contractions可以给rational rows，不能给nonrational独立CDT rows。此statement不声称所有invariant值恒零，T10已给非零rational例子。

此限制没有涵盖：新增forcing奇点的inverse-L solution、非齐次relative extension、不同connection、额外singularities，或只填某一leaf而保留另一个实际generator。也不说所有tensor对象无用；它们可以用来比较nonzero periods、识别rank、构造cap或构造一个新的extension。不能据T24宣布一般period方法或odd ζ研究no-go。

## 7. 全有限处Taylor cap与CDT数组的完整支付

令D_N=lcm(1,…,N)，n0时D0=1。本轮FULL读ΓG15–G17并在T2直接检查：每个s-degree-j coefficient共消费j个reciprocals，rank9全部分母≤5n；低权全half模型≤2n。因此
\[
D_{bn}^{\,j}[t^n]\eta_j\in\mathbf Z,\quad
b=5\ (r9),\quad b=2\ (r3/5).
\tag{T25}
\]
对T15每个t^n convolution的两个索引l,n−l用D_(bl)、D_(b(n−l))均整除D_(bn)，总s-index恰h。对T17，D乘每个Taylor coefficient整数索引n，另外2s项index少1；故安全全prime结论为
\[
\boxed{D_{bn}^{\,h}[t^n]I_h\in\mathbf Z,\quad
D_{bn}^{\,h}[t^n]J_h\in\mathbf Z.}
\tag{T26}
\]
包含prime2、5和所有其它prime，n0 constants合法；没有乘导数factorial的遗漏，不声称这些caps最优。真正basis均holonomic，因为同一finite differential module的tensor/derivative constructions保持holonomic。

沿已读ΓG17的CDT flat array规则，row sum σ_i在位置i从0起的weight为2i+1，τ=Σ(2i+1)σ_i/m²。给每个所需s-index一个width-b嵌套LCM column，完整支付所选package：

|模型|实际Q-Taylor basis含1|m|σ|τ^flat|
|---|---|---:|---|---:|
|r3 half，二次|1,I0|2|(0,0)|0|
|r3 half，Wronskian|1,J1|2|(0,2)|3/2|
|r5 half，二次|1,I0,I2|3|(0,0,4)|20/9|
|r5 half，Wronskian|1,J1,J3|3|(0,2,6)|4|
|原r9，二次|1,I0,I2,I4,I6|5|(0,0,10,20,30)|92/5|
|原r9，Wronskian|1,J1,J3,J5,J7|5|(0,5,15,25,35)|116/5|

以上不是只按矩阵rank9领取cap，而是在真实函数rank上重新计算整个数组。q^−8 reflection列不被当Q-Taylor coefficients；T15/T17的actual coefficients是Q，不需给其额外领取Tate常数整性。τ明确不等于已获CDT严格余量：T24的单值填洞尚未成立，也没有可用mapping/capacity估计。低于旧array的某一数字不能忽略这个缺口。

## 8. Apéry校准：成功对象包含真正非齐次forcing

本轮actual FULL读Apéry1979四页，PDF4实际给ζ3的两序列初值a0=1,a1=5与b0=0,b1=6，并给
\[
(n+1)^3u_{n+1}
-(34n^3+51n^2+27n+5)u_n+n^3u_{n-1}=0.
\tag{T27}
\]
对生成函数A_A(t)=Σa_nt^n、B_A(t)=Σb_nt^n，按初值逐项比较而非“两个递推都齐次”的简称，准确
\[
L_A=D^3-t(2D+1)(17D^2+17D+5)+t^2(D+1)^3,
\quad
\boxed{L_A A_A=0,\qquad L_A B_A=6t.}
\tag{T28}
\]
第二式t1 coefficient为6，n≥2 recurrence使其余为0。虽然序列同满足后续homogeneous recurrence，B_A不是同一rank3 homogeneous solution。真实ζ3 approximation目标由这一非齐次Taylor companion构成。原文的分母与增长比较是额外算术/解析工作；本文没有借它替本rank9对象证明新strict inequality。

L_A亦formal skew-adjoint，但leading coefficient为1−34t+t²，具有两个finite反射候选roots17±12√2，而非本稿三点hypergeometric支集。只研究其homogeneous quadratic contraction，同样不能把inverse-L companion免费补出来。T28给可核的区别：成功构造应保留forcing、全部jumps、完整function rank与cap。它没有由一个vanishing orthogonal invariant自动得ζ3新证明。

## 9. 本轮结果、未达成处与下一可检验目标

本轮完成的是原rank9与rank3/5校准的skew-adjoint concomitant、固定Frobenius J-form、唯一scalar orthogonal contraction的恒等零、完整reflection列、真实Q-Taylor二次/Wronskianbasis、全部conifold jump、实际C(t)/Q(t)ranks与全prime cap。T24把旧η-linear obstruction扩展到这两个实际finite tensor packages，并明确限定原三点齐次field。

因此本支路尚未给κ5、κ7或新的ζ/L/Catalan无理性、LI、Lean。它排除了把“log消掉了”或“selfduality有不变量”直接当完整填洞；没有排除真正带source/forcing的新extension。下一目标是给实际inverse-L或relative extension一个完整Taylor companion，而非继续在同一齐次O9 field内改写零contraction。若新增singularity μ，应核其真实homogeneous/affine jump与函数rank，不能只消c而删μ。

## 10. 既有primary的实际页域、保存与闭合

应用PDF技能进行只读文本与三页render核对，没有authoring新PDF或重复下载。全部使用literature已有原件：

1. Beukers–Heckman1989，literature/beukers_heckman1989_hypergeometric_monodromy_20261006.pdf，30页。本人本轮actual FULL文本PDF1、2、13、19–24，9distinct页；PDF23亦actual render/view核Theorem6.5。一次首次读取PDF14遇GBK字符编码错误，该页未完整显示、不计FULL；所用Theorem6.5已在完整PDF23读并render核。PDF13是完整显示的定义/criterion页，不从其未显示后页推结论；primitivity在正文用single-Jordan自证。
2. Bloch–Vlasenko1908.07501v2，literature/cdt_gamma_connection_sources_20261007/bloch_vlasenko2020_gamma_frobenius_arxiv1908_07501v2.pdf，43页，本人本轮actual FULL文本PDF15–20六页，PDF19亦render/view。Definition22、Example23、Proposition26支持T11；未用PDF21的数值examples，也不继承Γ作者的其它页域。
3. Apéry1979，[Numdam原出版页](https://numdam.org/book-part/AST_1979__61__11_0/)，已有literature/apery1979_asterisque.pdf，4页；本人actual FULL文本PDF1–4四页，PDF4亦render/view核recurrence与初值。正文T28在此基础上自证。

本轮个人distinct primary实际文本页数19，render/view3页均在这19内，不把77归档页数当全文；新下载PDF/HTML/code0。只读PDF提取/编码修复/render、metadata/hash不属于数学producer；数学producer创建/execute/import/rerun、数学失败、prime扩表、Lean均0。网页仅检索/核primary bibliographic locator，不重复归档已保存PDF。

本文待actual FULL正式独审、作者收审后最终全文回读与单向FINAL来源收据；588旧冻结字节不改。独审PASS也不会被称为新数值无理性或Lean形式化。
