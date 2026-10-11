# 两个真实 inverse-L 周期的完整消跳：有理比例、任意次数 scalar invariant 与正则扩张边界

2026-10-07，NEW，作者 /root/source_pencil_finalize。Authority 为主报告当前 header/§195 与 research/cdt_odd_delivery_carry_cartier_split_algebraic_20261007.json，SHA44521a432fd71bdfef7e10a0d3ac63d636878b32aabfad5b293d8276a9fdf4a7，604冻结记录（599数学、5guards）全部只读。本轮实际完整读冻结 dual/lift f8e36、tensor0a9 与 unramified split611485 的全部章节；audit 仅核完整JSONparse/current_progress/物理SHA，不称人工全文重审604记录。本文唯一NEW纸面主稿，不创建或执行/import/rerun任何数学producer，不运行guards，不扩prime表，不改旧稿。

新增结论有两部分。第一，在实际有理普通点μ，两个有理强迫的非零完整jump若成比例，比例必有理；对这类真实配对，任意次数、含quotient的scalar有理表达式的μ-invariant域可以准确求出。第二，给出两条真实nonsplit周期消μ后留下非有理整数Taylor scalar的明确例子，并证明这一保留量只是原齐次周期；若再用完整有理数值关系填conifold，配对的所有μ-invariant scalar表达式立即变为有理函数。另将全部有限loop-fixed的边界扩到有限rational forcing的完整regular-singular extension及其tensor/jet/PV field。本文不声称仅一个μ-loop的full-jet invariant已被分类，也未证明任何新数值无理性。

## 1. 同一实际九阶对象、全部jump和允许的配对

保持原对象
\[
 D=t\partial_t,\qquad
 a=(\tfrac12^{\times5},\tfrac15,\tfrac25,\tfrac35,\tfrac45),\qquad
 \Lambda=3200000,\quad c=\Lambda^{-1},
\]
\[
 L=D^9-\Lambda t\prod_i(D+a_i),\qquad
 f_0(t)=\sum_{n\ge0}h_nt^n,\quad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbf Z,\quad h_1=3840.
 \tag{P1}
\]
本L在C(t)不可约，0是MUM，0处analytic homogeneous solution仅Cf0；有限奇点只有0,c。取与冻结稿相同基点、路径和分支，ψ=Δ_cf0≠0。不可约判据本轮实际FULL读Golyshev–Mellit PDF1–3，PDF2的上下参数modZ无共同根条件在此成立。Green pairing、真实ordinary jump及Taylor normalisation依赖冻结dual和split的完整证明，不从unscaled Gamma analytic parts免费转移。

对
\[
 R\in\mathbf Q(t)\cap t\mathbf Q[[t]],\qquad
 \operatorname{radius}_0R>c,
\]
唯一B_R(0)=0、LB_R=R的actual Taylor germ为
\[
 B_R(t)=\sum_{n\ge1}h_n
 \left(\sum_{m=1}^n\frac{R_m}{m^9h_m}\right)t^n,\qquad
 C_R=\sum_{m\ge1}\frac{R_m}{m^9h_m}.
 \tag{P2}
\]
冻结dual D6与split U3–U5给完整germ identity
\[
 \Delta_cB_R=C_R\psi.
 \tag{P3}
\]
这里C_Rf0−B_R在超过c的disc中holomorphic；不是只把某个endpoint值置零。

本稿精确local paired theorem限定：R1,R2的所有finite poles均位于同一个实际有理ordinary点μ，μ≠0,c；可以有任意polynomial part和pole阶。R1,R2仍满足P2；χ_i=Δ_μB_i按同一ordinary loop/返回路径比较，并假设
\[
 \chi_1\ne0,\qquad \chi_2=\lambda\chi_1,\quad \lambda\in\mathbf C.
 \tag{P4}
\]
λ=0亦允许，一般两条genuine nonsplit extensions时λ≠0。所有“消μ”均指χ完整analytic homogeneous solution，不仅最早log coefficient。第7节另给不要求P4的全有限loop边界。

## 2. 完整ordinary jump的有理初值，比例不能隐藏超越常数

在μ处取canonical homogeneous solutionsv_i，其∂t^jv_i(μ)=δij，0≤i,j≤8。因L普通leading coefficientμ⁹(1−Λμ)≠0，ODE递推给v_i全部Taylor coefficients在Q。固定selfdual Green formℬ的系数在Q(t)，普通点非退化；其初值矩阵
\[
 G_\mu=(\mathcal B(v_i,v_j))_{0\le i,j\le8}
 \in\operatorname{GL}_9(\mathbf Q).
 \tag{P5}
\]
本轮FULL读split U10–U11，完整residue identity为
\[
 \mathcal B(v_i,\chi_R)
 =2\pi i\,\operatorname{Res}_{t=\mu}v_iR\,dt/t.
 \tag{P6}
\]
右侧除2πi后的residue是Q中的数：有理R仅有限principal part，每个residue仅用v_i有限有理jet。把χ_R/(2πi)=Σz_jv_j代入P6并以P5求逆，得到
\[
 \boxed{(\partial_t^j(\chi_R/(2\pi i))(\mu))_{j=0}^8
 \in\mathbf Q^9.}
 \tag{P7}
\]
这只宣称local初值有理；把该向量继续到MUM Frobenius basis可能含真实period/comparison constants，不宣称该comparison有理。若μ∈Qbar，同一论证给Q(μ)^9；多个共轭pole必须分别比较，不能凭此使用一个未支付的全局比例。

P4中χ1非零，所以P7的第一个向量至少有一个非零coordinate；该coordinate的比给
\[
 \boxed{\lambda\in\mathbf Q.}
 \tag{P8}
\]
因两个local solutions继续返回同一基点时都经过同一可逆homogeneous continuation，比例不变。因此P8也覆盖实际在基点比较的P4，而非仅local选基时的偶然比例。

还有一个更强的linear-row限定。若非零homogeneous solutionsχ1,χ2满足χ2=q(t)χ1，q∈Q(t)，则q必constant：χ1的monodromy orbit因不可约性张成整个9维solution spaceV；q单值使乘法q送V到V。故q^jχ1∈V对全部j≥0成立，finite-dimensionality给非零constant polynomialQ使Q(q)χ1=0。χ1非零，连通germ中Q(q)=0迫q为constant。q∈Q(t)再给q∈Q。于是
\[
 a(t)\chi_1+b(t)\chi_2=0,\quad
 a,b\in\mathbf Q(t),\ b\ne0
 \quad\Longrightarrow\quad
 \chi_2=\lambda\chi_1,\ \lambda\in\mathbf Q.
 \tag{P9}
\]
χ2=0时仍是λ0；若a=0且χ2≠0，等式本来不可能。这里只消scalar完整jump，不把不同分量jet向量或非rational projector混为该等式。

## 3. 真实配对关系及任意次数rational invariant的精确固定域

令Z=B2−λB1，P8使其forcingR2−λR1在Q(t)。P4取消唯一新增ordinary fulljump；冻结split U19–U21适用，给唯一
\[
 \boxed{Z=T+a f_0,\qquad
 T\in\mathbf Q(t),\quad a=-T(0)\in\mathbf Q,}
 \tag{P10}
\]
T在0,c analytic。特别完整连接常数满足
\[
 \boxed{C_2-\lambda C_1=a\in\mathbf Q.}
 \tag{P11}
\]
本文不把P10称为新splitting theorem；新步骤是利用这个实际identity求全部scalar rational invariants。

设K是由实际scalar germs生成的域
\[
 K=\mathbf Q(t)(B_1,B_2)=k(B_1),\qquad
 k=\mathbf Q(t)(Z)
 =\begin{cases}
 \mathbf Q(t)(f_0),&a\ne0,\\
 \mathbf Q(t),&a=0.
 \end{cases}
 \tag{P12}
\]
所有域均嵌入一个包含原齐次fundamental solutions及particulars的meromorphic germ/PV field。无需假设B1,B2为两个代数独立变量。μ-loop固定k和χ1，并将B1送B1+χ1。T_μ未必把K送入K，所以下面的“μ-invariant among K”仅指
 \(\{F\in K:T_\mu F=F\}\)，不偷设T_μ是K本身的automorphism。

B1在k上必transcendental。否则非零polynomialp∈k[X]满足p(B1)=0；其coefficients被Tμ固定，重复loop给p(B1+nχ1)=0对所有n∈Z。χ1≠0使这些是共同meromorphic germ field中无限个不同roots，违反有限degree。这也说明本例原function rank的新增维度确实来自particular，而非从矩阵size领取。

取任意F=p(B1)/q(B1)∈K，p,q∈k[X]，q(B1)≠0，并假设TμF=F。每个重复loop都给
\[
 p(B_1+n\chi_1)-Fq(B_1+n\chi_1)=0.
 \tag{P13}
\]
analytic continuation是ambient field的automorphism，故这些denominators不成为零germ。P13使polynomialp(X)−Fq(X)在ambient germ field中有无限不同roots，只能为zero polynomial。选择q某个非零coefficient，得F等于p/q的该coordinate ratio，属于k。反向k的全部元素均μ-fixed。因此
\[
 \boxed{\{F\in\mathbf Q(t)(B_1,B_2):\Delta_\mu F=0\}
 =\begin{cases}
 \mathbf Q(t)(f_0),&a\ne0,\\
 \mathbf Q(t),&a=0.
 \end{cases}}
 \tag{P14}
\]
这准确覆盖任意finite degree的products、polynomials、quotients与rational t-dependent coefficients，不仅constant linear cancellation。它只分类undifferentiated两个scalar生成的域；不声称单个μ-loop已分类所有D^jB_i、Green bilinear/tensor coordinates或其它relative system。

## 4. 明确候选：两条真正nonsplit周期留下零费用非有理Taylor scalar

用冻结dual所证明的真实ζ5 forcing，不重新宣称其数值证明：
\[
 A=-2^{20},\quad\mu=A^{-1},\quad N=380928,\qquad
 P(X)=5532X^4-5600X^3+2275X^2-425X+30,
\]
\[
 R_5=-N^{-1}P(D)\frac{At}{1-At},\qquad LB_5=R_5,\quad B_5(0)=0.
 \tag{P15}
\]
完整ΔcB5=ζ5ψ、μ-fulljumpχ5≠0，普通pole5给leading local (t−μ)^4log(t−μ)；这些均使用FULL已读冻结dual D7–D25。这里ζ5是用于检查新接口的已知rank9calibration；没有把原ξ=αζ4+βζ5的actual whole carrier改成免费ζ5-source，也未把u ζ5改名为ζ7。

取实际
\[
 R_1=R_5,\qquad R_2=R_5-h_1t,\qquad
 B_1=B_5,\quad B_2=B_5+1-f_0.
 \tag{P16}
\]
因为L1=−h1t、Lf0=0，P16逐项验证LB2=R2及B2(0)=0。两条forcing只有同一个ordinaryμ pole5，且两条particular的fulljump均χ5≠0；所以两条都是真正nonsplit。完整连接为
\[
 C_1=\zeta(5),\qquad C_2=\zeta(5)-1,\qquad
 \boxed{B_1-B_2=f_0-1\in t\mathbf Z[[t]].}
 \tag{P17}
\]
ψ≠0证明f0−1非rational；它在μ holomorphic，真实Q(t)rank{1,f0−1}=2，allfiniteplace cap为0。B1在Q(t)(f0)上transcendental使{1,B1,B2}的Q(t)rank恰3。该非有理μ-filled scalar因此确实存在，绝非“取消jump必全rational”的过强断言。

但P17仍有Δc(f0−1)=ψ，与ζ5是否被假设有理完全无关。它只恢复原齐次周期，没有任何ζ5 relation-dependent conifold filling；P11的连接差准确为−1，原ζ5部分已消掉。它也没有剥掉f0的其它base branches。

费用逐对象支付：冻结dual D26–D28的实际integer cap为
\[
 N D_n^9[t^n]B_5\in\mathbf Z,\qquad D_n=\operatorname{lcm}(1,\ldots,n).
 \tag{P18}
\]
P16的整数1−f0使同一NDn9支付B2；P17输出为整数Taylor无需这九列。固定有理u的subtraction u f0仅加固定denominator。任意F∈Q(t)(f0)的quotient则不自动继承零cap或Dn9：它可增pole、改变Taylor denominator增长和endpoint。本文只给P17的准确零费用，不为全固定域免费领取integral lattice、holonomic scalar property或CDT可用array。

## 5. 有理数值关系下的完整conifold filling：配对invariant直接有理

对固定u1,u2∈Q，令
\[
 F_i=B_i-u_if_0,\qquad
 Z_u=F_2-\lambda F_1
 =T+a_u f_0,\quad a_u=a-u_2+\lambda u_1.
 \tag{P19}
\]
F1在μ仍有非零χ1，same-loop证明可逐字应用，k_u=Q(t)(Z_u)。如果要求两条真实scalar的完整conifold jump都消失，由P3及ψ≠0必有ui=Ci。P11于是给
\[
 u_2=\lambda u_1+a,\qquad a_u=0,\qquad Z_u=T.
 \tag{P20}
\]
因此在该实际有理数值假设下
\[
 \boxed{\{F\in\mathbf Q(t)(F_1,F_2):\Delta_\mu F=0\}
 =\mathbf Q(t).}
 \tag{P21}
\]
这里只需scalar配对identity及单个μ-loop，不需另假设F的Taylor或引用原O9分类。它准确阻止“先用两条同jump inverse-L填conifold，再用非线性scalar quotient消μ，同时保留非rational carrier”这一方案。并不阻止原系数hypothesis产生矛盾的其它方法；它说明这一步输出不再提供所期待的额外nonrational function rank。

P16校准在假设ζ5=u∈Q时选u1=u、u2=u−1，给
\[
 F_2=F_1+1,\qquad
 \{1,F_1,F_2\}\text{ 的Q(t)rank}=2,
 \quad\mu\text{-fixed scalar expressions全在Q(t).}
 \tag{P22}
\]
μ nonzerojump保证F1非rational。P17中的非rationalf0−1此时不属于该relation-filled二scalar域：P22的域为Q(t)(F1)，其μ固定域只为Q(t)；不能同时保留未填conifold的f0作为免费第三reference row，再声称所有rows在conifold meromorphic。

## 6. 未提前配齐source constants时：Q-Taylor+c-fixed同样迫有理

若a_u≠0或未先施P20，P14/P19仅使μ-invariant F属于Q(t)(f0)。要求F为genuineholomorphic Q-Taylor germ于0时，完整0-loop固定F；再要求完整c-loop固定F，原三点homogeneous PV field的T0,Tc生成全monodromy。冻结tensor T24已证明这一固定域为C(t)。∞不被遗漏：其loop是其它两者product inverse。

从C(t)下降到Q(t)可以直接自证，避免把Q-coefficients与C(x)-module混淆。令F=Σa_nt^n∈Q[[t]]亦在C(t)。选某complex polynomial denominatorq、q(0)≠0，degq≤d，使qF为degree≤M的polynomial。向量(q0,…,qd)满足所有n>M的rational linear equations
\[
 \sum_{j=0}^dq_j a_{n-j}=0
 \quad(a_k=0\text{ if }k<0).
 \tag{P23}
\]
这些方程的row space有限维，有限个rows已经张成全部，所以全部solution kernel定义在Q上。现存complex kernel vector的q0非零，故存在rational kernel vectorq0亦非零。对应q∈Q[t]使qF∈Q[t]，得
\[
 \boxed{\mathbf C(t)\cap\mathbf Q[[t]]
 =\mathbf Q(t)\cap\mathbf Q[[t]],\qquad
 \Delta_\mu F=\Delta_cF=0,\ F\text{ genuineQ-Taylor}
 \Longrightarrow F\in\mathbf Q(t)}
 \tag{P24}
\]
第二implication限定P12/P19的actual scalar field。F可能在其它点有meromorphic poles，固定与meromorphic不等于holomorphic；rational outputs仍可含这些poles，其endpoint/cap亦须独立支付。

## 7. 新的全有限loop边界：rational extensions及其完整tensor/jet

P14不分类仅μ-fixed的fulljet invariant。可以证明另一条较强、条件也较强的全局定理。对任意finite number的rational forcingR_i，考虑真正的rank9+s companion extension（普通∂t coordinate）
\[
 y'=M(t)y+\sum_{i=1}^s b_i(t)e_i,\qquad e_i'=0.
 \tag{P25}
\]
b_i由原L及R_i的ordinary companion form确定，在C(t)；fundamental matrix包含原9条homogeneous列及各particular完整jet列。PV fieldE含这些actual germs。假设R_i在0,c analytic并0constant为0；允许有限多个ordinary poles及任意polynomial part，含实际P15。P25不仅形式上把scalar阶数加s，而是具体原system的extension。

**完整extension仍regular-singular。** 在任一局部坐标x（∞用x=1/t），原homogeneous block因regular-singular存在meromorphic invertible gauge，使z'=A(x)z/x且A analytic。该gauge把每个b_i变成meromorphic列β_i(x)，仅有有限poleorder。选择非负integerM≥max_i poleorder(β_i)−1，并将常数coordinates改为\(\tilde e_i=x^{-M}e_i\)。则
\[
 z'=\frac{A(x)}x z+\sum_i x^M\beta_i(x)\tilde e_i,\qquad
 \tilde e_i'=-\frac Mx\tilde e_i.
 \tag{P26}
\]
x^Mβ_i至多simplepole，全部matrix Fuchsian。该local meromorphic gauge同时支付ordinary high poles、原c/MUM0及∞；它不假设R_i衰减，不把mere endpoint zero当regularity证明，也不声称integer lattice在此gauge下免费保持。

本轮actualFULL读Singer author lecture PDF10–20，特别Theorem1.3.9/Cor1.3.10与Proposition1.3.27(Schlesinger)：regular-singular系统的monodromy在differential Galois group中Zariski dense，PV全固定域是C(t)。因P26真正适用，所以任何
\[
 F\in E
 \quad\text{(finite rational/tensor expression，可含全部jets、Green rows、inverse)}
\]
若为genuineQ-Taylor germ，且完整c-loop与**每个新增ordinary-point的generator loop**均固定F，便由0-loop的Taylor fixed及sphere loop relation固定整个monodromy，继而全部Galois group；P23下降给
\[
 \boxed{F\in\mathbf Q(t).}
 \tag{P27}
\]
这里除以表达式的denominator仅要求它非零germ；表达式新产生的ordinary poles是meromorphic，并不额外制造PV connection monodromy。与任意一个point的一条chosen branch比，P27条件是全部finite generator loops，不能仅测试leadinglog、selected projection或一条return path后把其它generators删除。

P27超出旧tensor T24：此前只在原homogeneous三点PV field内固定0,c；现在先支付rational-forcing actual extension的regular-singularity及新增loops，再涵盖其fulljet/tensor PV field。证明没有使用O9最高weight、未见页的分类或数值计算。它也不证明“仅消μ的全部tensor表达式必在原homogeneous field”；这种局部classification是仍待研究的另一问题。

## 8. 精确逃逸条件、来源页域与本轮边界

P14–P22给一个可审查的paired-extension obstruction，P16–P18同时给非rationalQ-Taylor的真实消μ候选。兩者相容：候选留下旧f0；relation-filled两scalar则只留rational。要有新的nonrational carrier，可以改变P4/sharedjump单方向、使用fulljet的未分类local invariants，或改用真正新base/nonrational forcing；这些仍必须支付所有remaining loops、实际Q-Taylor、endpoint constants与arithmetical caps。若它仍属于finite rational regular-singular extension且全部finite monodromy真正取消，P27继续适用，所以仅提高tensor degree不绕过这一全局边界。

新base可有更多conifold generators，允许relation只填其中某些点而保留其它branch，因而不在P27的“全部fixed”hypothesis。例如冻结split的x(1−x) pullback已有具体nonsplitforcing；本轮同行quadratic anti-forcing进一步研究其remainingloops。本文没有对新base作generic impossibility claim，也未借同行未冻结证明支付自己的结论。真实CDT map可能omitremainingpoints，能否在同叶参考和全部费用之后取得strictmargin仍是独立问题。

本稿本轮新增纸证：ordinary localjump除2πi的九维initial vector有理；完整成比例jump的比例有理及t-dependentlinear cancellation仅能constant；真实两个scalar任意次数quotient的精确μ-invariant field；实际两条nonsplitforcing消μ并留下integerf0−1；在conifold relation-filled假设下该field反而全rational；Q-Taylor rational descent；以及finite rationalforcing extension局部Fuchsian gauge与全部loop-fixed的fulljet/PV rationality。没有新的ζ7、κ5/κ7、Catalan或原ξ无理性/LI定理，原ξ=αζ4+βζ5 whole-object projection仍未解决。

本轮个人primary实际FULL读域：

1. Beukers–Heckman1989，literature/beukers_heckman1989_hypergeometric_monodromy_20261006.pdf，PDF1、2、20共3distinct页，核regular-singular monodromy/Galois背景；未声称本轮读PDF23分类定理。原件已有30页，当前不新下载或继承以前页域。
2. Golyshev–Mellit2009，literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf，PDF1–3共3distinct页，核irreducibility无共同根modZ及pseudoreflection。原件已有10页。
3. Michael F. Singer，Introduction to the Galois Theory of Linear Differential Equations，既有author原件 literature/singer2009_differential_galois_lms_author_20261006.pdf，PDF10–20共11distinct页actualFULL text；特别PDF13–14固定域、PDF19–20单值群和Schlesinger命题。Author原链接 https://singer.math.ncsu.edu/papers/LMSlectures.pdf ，本轮web open一次timeout，随后primary author indexed search返回Proposition1.3.27，与实际本地完整读页核对一致；未由失败open增加任何PDF读页或归档。

本主稿个人17distinctPDF页；新primary下载0、render0，数学producer新建/execute/import/rerun0、数学失败0、prime扩表0、Lean0。上述pages为本轮实际页域，不继承他人或以前读页；后续assignedreview若需新页另记。没有外部来源的长段引用。唯一NEW稿等待实际FULL作者自读、正式独审和最终单向来源收据；604旧记录不改。
