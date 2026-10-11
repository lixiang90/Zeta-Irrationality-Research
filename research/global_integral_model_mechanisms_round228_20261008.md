# 第228轮：整周期模型、Euler过滤与保留目标的成本

2026-10-08。本稿研究一个完整可计算的受限机制，不优化已停用的222–226包，不提出新的数值无理性定理。结论是：**有限 Euler/Frobenius式过滤能保留字符L值关系并令指定素数处积分，却不降低完整前缀的指数分母费用；可逆代数换坐标也不能把非globally bounded相对周期变成全整 diagonal。** 真正的下一项任务须改变实际相对周期格/投影，并同时保留全部共轭关系。

## 1. 全整背景不等于全整相对周期

**M1（定义及 elementary diagonal 整性）。** 对数域K中有正收敛半径的芽f，称其globally bounded（GB），若存在正整数A,C，使Af(Cz)属于O_K[[z]]。对Q系数就是Z[[z]]；常数项由A清除。若R=P/Q是原点regular的多变量有理函数，Q(0)非零，则其普通 diagonal GB：把Q归一成常数项1，取整数c清全部非恒定系数分母，另取A清P的恒定分母，便有AR(cX)属于Z[[X]]。d变量 diagonal 的第n项被c^(dn)整化，故AD(c^d z)积分。这里没有使用Christol反向猜想，也没有对任意Laurent展开/relative链积分自动应用此结论。

例如

\[
F(z)=\sum_{n\ge0}\binom{2n}{n}^{2}z^n
=\operatorname{Diag}\frac1{(1-X_1-X_2)(1-X_3-X_4)}
\]

是完整整数背景。但实际相对反导数

\[
E(z)=\sum_{n\ge1}\binom{2n}{n}^{2}\frac{z^n}{n^2},
\qquad\Theta^2E=F-1,\quad\Theta=z\partial_z,
\tag{M1}
\]

不GB：对每个奇素数p，(1+X)^(2p)模p等于(1+X^p)^2，故binom(2p,p)模p等于2，[z^p]E的p估值恰−2。任何固定A,C都遗漏无限个这样的p。background diagonal、integral connection或unit-root quotient不能据名称清掉这一relative行。

**M2（明确的整反导数入口）。** 若a_n均为整数且Σa_n z^n有正收敛半径，H_s=Σ_{n≥1}a_n z^n/n^s且s正整数，则H_s GB当且仅当存在有限素数集S，使

\[
v_p(a_n)\ge s\,v_p(n)\quad\text{对所有 }p\notin S,n\ge1.
\tag{M2}
\]

必要性取p不整除固定AC；充分性取C=∏_{p∈S}p^s，利用v_p(n)≤n，逐项清掉S处剩余分母。正收敛半径从a_n的指数界保留。这是真实Taylor系数/全prime-power条件，比“背景具有Frobenius”更强。若要用integral de Rham实现它，必须识别同一relative horizontal section及其实际输出，不是只识别齐次商。

## 2. 代数拉回不能制造GB

**M3（自含Eisenstein界）。** 任意代数芽u属于K[[z]]都GB。取其最小多项式P(z,y)，令ν=ord_z P_y(z,u)有限（char0）。取N>ν及前N项u_<N，写u=u_<N+z^Nw。Taylor展开显示

\[
Q(z,w)=z^{-N-\nu}P(z,u_{<N}+z^Nw)\in K[z,w],
\qquad Q(0,w)=a+bw,\quad b\ne0.
\]

常数项的整除性由P(z,u)=0给出；二次以上项有z^(N−ν)因子，线性项的首系数仍非零。平移w的常数项并清有限系数分母，可设Q属于O_K[z,v]、Q(0,v)=bv且v(0)=0。取正整数d满足d/b属于O_K。则

\[
\frac{Q(d^2t,dw)}{bd}\in O_K[t,w],\qquad\text{在 }t=0\text{时等于 }w.
\]

其余项都含t，系数有d/b因子；逐次隐式递推无需除非unit，故w属于O_K[[t]]。于是v(d²t)积分，有限前缀另用固定A,C清除。隐式函数定理给每个复嵌入下的正收敛半径。这里同时证明有限坏素数与指数深度，未从未读算法推断整数性。

**M4（包括ramified的代数坐标不变性）。** 对非恒定代数芽φ∈K[[z]]，φ(0)=0，及有正半径的f∈K[[z]]，

\[
f\text{ GB}\quad\Longleftrightarrow\quad f\circ\phi\text{ GB}.
\tag{M3}
\]

GB芽对和、积、组成封闭：若Af(Cz)积分，代数/GB的ψ(0)=0，可取整数B使ψ(Bz)属于C O_K[[z]]，再直接组成。具体若Dψ(Ez)积分，则B=ECD足够，因为第n项的(D C)^n/D含C，n≥1。

反向若φ的阶为e，取首项系数的e次根所在有限扩域，并令h(z)=z(φ(z)/z^e)^(1/e)。它是代数且首项非零，故其形式逆ψ亦代数，φ(ψ(w))=w^e。M3整化ψ，组成得到f(w^e) GB，再抽取e倍指标得到f GB。原系数为Q时，O_K∩Q=Z，故可降回Q。这不是只限linear scale的论证。

同理，代数meromorphic矩阵及其逆在0只有有限Laurent头，除去该头后均GB。可逆矩阵变换和M4坐标运输不能令一个含非GB行的**完整可恢复tuple**全部GB。因此(M1)的全源不能由这种变换变成普通有理diagonal整数模型。允许新的非可逆projection或新的生成载体；其目标/关系是否保留须另证，不能把此限定扩张成所有Apéry构造失败。

## 3. 一个实际保留Catalan关系的Frobenius式过滤

以下G仅作精确机制例子，不提出Catalan的新颖性。设χ=χ₄，χ(偶数)=0、χ(1 mod4)=1、χ(3 mod4)=−1，

\[
T(z)=\sum_{n\ge1}\frac{\chi(n)z^n}{n^2},\quad
T(1)=G,\quad\Theta^2T=\frac{z}{1+z^2}.
\tag{M4}
\]

**M5（有限Euler depletion）。** 取固定有限奇素数集P、Q=∏_{p∈P}p、ψ_p f(z)=f(z^p)。这些pullback相互交换，故

\[
T_Q=\prod_{p\mid Q}(1-\chi(p)p^{-2}\psi_p)T
=\sum_{d\mid Q}\frac{\mu(d)\chi(d)}{d^2}T(z^d)
=\sum_{\substack{n\ge1\\(n,Q)=1}}\frac{\chi(n)z^n}{n^2}.
\tag{M5}
\]

逐项看p|n时χ(p)p^-2χ(n/p)/(n/p)²=χ(n)/n²，精确相消；p不整除n时第二项为0。因此T_Q在每个选定p处**所有系数**积分。这是自证的Euler/Frobenius式系数操作，不宣称已构造某个Dwork crystal或integral de Rham comparison。

令

\[
c_Q=\prod_{p\mid Q}(1-\chi(p)/p^2)\in\mathbb Q_{>0}.
\]

原点branch在1为普通点，M5有限求和给T_Q(1)=c_QG。因此

\[
A_Q=\frac{T_Q}{1-z},\quad B=\frac1{1-z},\quad
H_{g,Q}=A_Q-c_QgB=\frac{T_Q-c_Qg}{1-z}.
\tag{M6}
\]

在假设G=g∈Q时，这是同一实际目标的Q系数holonomic芽；1处pole真正可去。系数含n0：a_0=0、a_n=Σ_{1≤k≤n,(k,Q)=1}χ(k)/k²，h_n=a_n−c_Qg，n≥0。没有把局部p整化的目标改成无关值。

**M6（完整精确LCD）。** δ_f(N)记含0到N的最小共同正分母。对所有N≥0，

\[
D_{Q,N}=\prod_{\substack{p\le N\\p\ \mathrm{odd},\ p\nmid Q}}
p^{\lfloor\log_pN\rfloor},\qquad D_{Q,0}=1,
\]

\[
\boxed{\delta_{T_Q}(N)=\delta_{A_Q}(N)=D_{Q,N}^{2},\qquad
\delta_{H_{g,Q}}(N)=\operatorname{lcm}(D_{Q,N}^{2},\operatorname{den}(c_Qg)).}
\tag{M7}
\]

上界逐项显然。每个odd p∤Q在n=p^a≤N处，χ(p^a)=±1，强制2a层，给T_Q下界。A_Q的coefficients是partial sums，与T_Q的coefficients通过整的prefix sum/difference双向变换，故LCD精确相等。H含h0=−c_Qg；h_n−h_(n−1)仍为T_Q第n项，分别强制两部分分母，反向上界即lcm。不能遗漏常数尾。

由PNT，log lcm(1,…,N)=N+o(N)，故

\[
\log\delta_{H_{g,Q}}(N)=2N+o(N).
\tag{M8}
\]

有限P只减少2Σ_{p|2Q}⌊log_pN⌋logp=O_Q(logN)，不是指数费用改进。对任何固定rational/algebraic scalar，未涉及的大p仍有相同负深度；M4还排除由代数坐标把这同一完整relative行变成GB。LCD不是任意primitive联合格费用的下界，逐项类型也不由prefix LCD单独决定。

## 4. 强迫方程、全部叶和完整自然预算

**M7（过滤不能移除原branch障碍）。** 同一实际T_Q满足

\[
\Theta^2T_Q=R_Q(z),\qquad
R_Q=\sum_{d\mid Q}\mu(d)\chi(d)\frac{z^d}{1+z^{2d}}.
\tag{M9}
\]

在ξ=±i，χ(d)ξ^d=ξ（d奇），故每项的residue为μ(d)/(2d)，总residue

\[
r_Q=\frac12\prod_{p\mid Q}(1-1/p)\ne0.
\tag{M10}
\]

局部(zT_Q′)′=R_Q/z，于是任何branch都有

\[
T_Q=B_\xi(z)\log(z-\xi)+A_\xi(z),\quad
B_\xi(z)=\frac{r_Q}{\xi}\log(z/\xi)
=\frac{r_Q}{\xi^2}(z-\xi)+O((z-\xi)^2),
\tag{M11}
\]

A_ξ、B_ξ均在ξ附近analytic，局部log(z/ξ)取值0于ξ。上述精确式由先积分(zT_Q′)′、再分部积分得到；高阶log项保留在B_ξ中。齐次解1、log z在ξ附近analytic，不能改变该强迫系数。任意有限局部次数e的holomorphic拉回仍有非零t^e log t，不能meromorphic。因T_Q=(1-z)H_{g,Q}+c_Qg，任何H的合法共同图都必须omit±i。这里**完整付了所有到达叶**的非零系数，不使用停用包的rank-one reflection猜想。

当Q>1时，ξ_Q=exp(πi/(2Q))处只有d=Q项有pole，非零；又增加了primitive4Q分支点。不能仅以选定p处积分领取一个更大图。没有证明所有全局共同图集合包含关系；foreign0的connection仍需各图单独核。

**M8（当前自然single-arch预算）。** H非rational由M11给出，故{1,H_{g,Q}}的实际Q(z)-rank为2。固定整数整体倍数清den(c_Qg)，literal数组两列均为(0,1)，即σ=(0,2)、e=0，普通CDT费用恰τ=3/2。取所有finite places identity的single-arch框架；这不是所有all-place/primitive模型的最小费用声明。

任意holomorphic共同φ:(D,0)→(C,0)均omit±i。冻结220已付的two-puncture universal-cover界为

\[
|\phi'(0)|\le\rho=\pi\,{}_2F_1(1/2,1/2;1;1/2)^2<e^{3/2}.
\tag{M12}
\]

其中cover i(2λ(i(1+ζ)/(1−ζ))−1)的derivative给ρ，lifting与Schwarz给全图上界。严格纸界使用F(1/2)≤1213/1024、π<22/7、ρ<32370118/7340032<5711/1280<e^(3/2)。这是复用既有geometry，不重报为新定理。

所以在这里的holomorphic φ:D→C图类，此完整自然数组在过滤前后均不能满足log|φ′(0)|>τ，尚未进入energy quotient；ρ不自动给允许φ有pole的meromorphic presentations上界。对显式affine φ_a=aζ、0<|a|<1，全H拉回analytic，真实double boundary energy是log|a|：φ差值为a(z−w)，Jensen给∫∫log|z−w|=0。其rank2 margin为2(log|a|−3/2)−log|a|=log|a|−3<0，前后完全相同。

| 对象 | 目标关系 | 精确前缀指数 | 当前自然τ | 强制omit |
|---|---|---:|---:|---|
| T,A,H（Q=1） | T(1)=G，H=(T−g)/(1−z) | 2 | 3/2 | ±i |
| 任意固定finite Q | T_Q(1)=c_QG，H_Q=(T_Q−c_Qg)/(1−z) | 2 | 3/2 | ±i及新增primitive4Q点 |
| 所有odd primes的无限filter | T_Q→z，c_QG→1 | rational极限 | rank降1 | 原目标不再作为独立周期 |

最后一行由系数支撑和Σ1/n²可积支配直接得到：n>1的odd n最终被筛掉，n=1保留；T_Q(1)→1。若g=G，H_{g,Q}→(z−1)/(1−z)=−1。无限操作不是一个有限Q、有理且保留非rational目标的transport；它把目标与秩一起消掉。

## 5. 真正可审的下一项：完整共轭relative projection

**M9（新目标的具体共轭警报）。** 对χ=χ₋₃，设F=Σχ(n)z^n/n²、L=F(1)>0，K=Q(√3)。χ非主且Σ_{a mod3}χ(a)=0，Θ²F=(z−z²)/(1−z³)=z/(1+z+z²)，所以原生1为普通点。假设g=√3L∈Q，原生

\[
H_+=\frac{\sqrt3F-g}{1-z}
\]

补1，但对σ(√3)=−√3、σ(g)=g，

\[
\sigma(H_+)=\frac{-\sqrt3F-g}{1-z},\qquad
(-\sqrt3F-g)(1)=-2g\ne0.
\tag{M13}
\]

因此这个原生rational-character载体不能免费声称两个arch places同时获得同一filling。对此χ取P不含3、c_Q^{(-3)}=∏_{p∈P}(1−χ₋₃(p)/p²)，finite Euler过滤把两端同时乘这个有理因子；第二残差仍−2c_Q^{(-3)}g。它和前面χ₄的c_Q是不同对象。一个新period marking、不同endpoint、实际trace或projection可能改变它，但必须证明，而非以目标“只多一个代数因子”跳过。这里不判断该数的新颖性，也不排除其它完整source；现状由本轮B的primary任务另核。

**M10（应证明的命题对象，尚未支付）。** 真正值得提升的整模型命题须给：具体relative周期族和全部embeddings的actual endpoint关系；一个在同一原格上定义的projection/quotient，输出仍保留g及足够函数秩；对完整polynomial-jet lattice的joint Smith/index收益，在p随degree增长的窗口里累计为cD²，c>0；同时证明原图/各处energy的变化不吞掉该收益。有限P的O(logN)清分母不能满足这一要求。

这不是新增motivic splitting theorem，也不要求先证明一般Betti/Hodge conjecture。直接CDT入口仍是actual rational relation产生可延拓的K/Q系列及完整整费用。GB可由M2的真系数条件或一个显式diagonal实现证明；GB⇒diagonal仅是Christol猜想，不使用。若投影只能保留齐次unit-root或仅一共轭补点，应降级。

历史20261006 classical Frobenius/Smith稿已在特定全prefix格里支付过11/150 credit；该“增长素数窗口、同一整格”逻辑不是本轮新发明。本轮新完成的是finite Euler filtering的精确LCD、实际目标关系、强迫的全叶branch及共轭残差诊断。不能把其重新命名为旧源已付的新carrier。

## 6. 证据与运行

新primary仅两篇作者PDF：[Bostan–Salvy–Singer](https://singer.math.ncsu.edu/papers/BSS.pdf)的Eisenstein/GB定义和Conjecture8选段；[Adamczewski–Bell](https://adamczewski.perso.math.cnrs.fr/Diagonals_Final.pdf)的diagonal定义与具体完整周期例子选段。式(M1)–(M13)的实际公式、LCD、branch、关系及变换论证由本稿纸证承担，不借文献算法/CAS或未读motivic theorem。准确saved版本、selected范围及历史去重见[本scope](../literature/global_review_sources_round228_20261008/dual_reading_scope.md)。

数学程序、数学失败运行、扫描、producer重跑、数值积分、PSLQ、Lean、Git修改均0。只NEW本稿、scope及真实primary档；原作者PDF2、selected TXT4，HTML/TEX下载0。文档提取均exit0。最终保存后实际FULL作者复读与identity另报，不冒充独审。
