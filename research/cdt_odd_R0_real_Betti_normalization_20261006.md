# R₀ 实结构、合法 Betti 归一化及仍存的一维真实周期成本

日期：2026-10-06。NEW 全尺度纸面证明。旧/同行 MD、PY、JSON、manifest 只读，未执行或import数学producer。实际读main §§73–78及delivery元数据：基线337份冻结输入、85份证明/审阅、4399归档PDF页、1081本地链接。只读delivery JSON，没有运行audit脚本。

本稿证明actualcompact AJ lift可与复共轭相容，并保持真实vanishing normalization。actualrank-four sector内，允许的real-compatible rational Tate shifts先降至二维，再降至一维。随后构造剩余方向的实际闭cycle，计算它的strictlypositive limiting period及origin的transcendental Nilsson coefficient。没有新的特殊值无理性或integral saturation结论。

## 1. Linear Betti involution、antilinear实结构和cup方向

取关于 \(x\mapsto\bar x\) 稳定的小disk \(D\)，real部分在 \(0<x<1\)，固定 \(\sqrt{x}>0\)。compact family及pair定义于 \(\mathbf Q\)，有anti-holomorphic \(c_x:X_x\to X_{\bar x}\)。在real fibre，记
\[
 B=c_x^*:H^3(X_x,\mathbf Q)\to H^3(X_x,\mathbf Q),\qquad
 C=BK,\quad C\alpha=c_x^*\overline\alpha,
 \tag{R1}
\]
其中 \(K\) 仅conjugate Betti complex coefficients。\(B\) 是rational **linear** involution；\(C\) 是 **antilinear** involution。family section的准确公式为
\[
 (\mathfrak Cr)_x=c_x^*\overline{r_{\bar x}}.
 \tag{R2}
\]
它把holomorphic section变holomorphic section，与real Gauss–Manin connection相容。

complex dimension3的conjugation翻转三个imaginary real coordinates，degree为−1。固定 \(Q(\alpha,\beta)=\int_X\alpha\wedge\beta\)，因此
\[
 Q(B\alpha,B\beta)=-Q(\alpha,\beta),\qquad
 Q(C\alpha,C\beta)=-\overline{Q(\alpha,\beta)}.
 \tag{R3}
\]
\(B\) 是anti-symplectic。令 \(a=2\pi i\)，则 \(a^4=16\pi^4\) real，而 \(a^3\) imaginary；\(Q_{\rm dR}=a^{-3}Q\) 满足
\[
 Q_{\rm dR}(C\alpha,C\beta)=\overline{Q_{\rm dR}(\alpha,\beta)}.
 \tag{R4}
\]
raw orientation sign与Tate-three conjugation sign相消。

## 2. 指定 \(\Xi\) 的actualAJ类及合法real average

指定唯一 \(\Xi\in CH^4(Y,4)_{\mathbf Q}\) 的open restriction为四个定义于 \(\mathbf Q\) 的units \(v_j\) 的product。KLM principal negative-cut unit triple满足
\[
 c^*\overline{\log^-v}=\log^-v,\quad
 c^*\overline{d\log v}=d\log v,\quad
 c^*\delta_T=-\delta_T,\quad\bar a=-a.
 \tag{R5}
\]
后两sign相消，故 \((a\delta_T,d\log v,\log^-v)\) 在 \(C\) 下不变。KLM actualunit product/ring map于是给specifiedfour-unit Deligne class不变性。可先在universal torus证明，再用derived pullback；不假设principal cuts未经moving在每个fibretransverse。

冻结compact derivative已实际证明
\[
 H^3(X,\mathbf C/a^4\mathbf Q)\hookrightarrow
 H^3(U,\mathbf C/a^4\mathbf Q).
 \tag{R6}
\]
该restriction与conjugation相容，故上述openunit身份严格推出
\[
 \boxed{\mathfrak C AJ(\Xi)=AJ(\Xi).}
 \tag{R7}
\]
这是本例的actualclass证明，亦与 \(\Xi\) 定义于 \(\mathbf Q\) 和regulator自然性一致；不依赖未完成的compact literalgraph admissibility。

actualholomorphiccompact lift \(r\) 的已证derivative为
\[
 \nabla_\theta r=16\sqrt{x}\omega,\quad
 \omega=16\sqrt{x}\rho_{256x},\quad\theta=x\partial_x.
 \tag{R8}
\]
LEFT residue及square-root branch是real-compatible，所以 \(\mathfrak C\omega=\omega\)。R7和相同derivative给
\[
 r-\mathfrak Cr=a^4q,\qquad q\text{ flat rational compact},
 \quad\mathfrak Cq=-q.
 \tag{R9}
\]
因此
\[
 \boxed{r_{\mathbf R}:=\tfrac12(r+\mathfrak Cr)
 =r-\tfrac12a^4q,\quad \mathfrak Cr_{\mathbf R}=r_{\mathbf R},
 \quad\nabla_\theta r_{\mathbf R}=16\sqrt{x}\omega.}
 \tag{R10}
\]
\(1/2\)是本项目 \(\mathbf Q\)-class的合法Tate shift，未声称integral lift。这里 \(q\) 来自两个**compact** lifts；没有从open Tate class免费推出它compact。

## 3. Actualsector及scalar实值性

actualrational rank-four sector \(V_{\mathbf Q}\) 的complexification由
\(\omega,E_1,E_2,E_3\) 生成，\(E_j=\nabla_\theta^j\omega\)。这些forms被R2固定，所以 \(C\) 保持 \(V_{\mathbf C}\)；\(V\) rational使 \(K\) 也保持它。因此 \(B=CK\) 保持 \(V_{\mathbf Q}\)。R3使orthogonal complement同样保持，actualorthogonal projector \(\Pi\) 与 \(B,C\) 相容。不假设整个compact/open \(H^3\) rank four。

R3给real \(x\) 上
\[
 \nu_{\mathbf R}=Q(r_{\mathbf R},\omega)
 =-\overline{\nu_{\mathbf R}},\qquad
 \boxed{\widehat\nu_{\mathbf R}=-\nu_{\mathbf R}/(16a^3)\in\mathbf R.}
 \tag{R11}
\]
rawscalar纯虚，normalizedscalar实，且 \(P\widehat\nu_{\mathbf R}=\sqrt{x}/16\)，
\(P=\theta^4-x(\theta+\tfrac12)^4\)。这只是固定raw规范中的reality，不是免费的rational arithmetic gauge。

## 4. 真正cycle的conjugation和PDsign

对任一cycle \(\gamma\)，R3和 \(\int_\gamma\alpha=Q(PD\gamma,\alpha)\) 给
\[
 \boxed{B\,PD\gamma=-PD(c_*\gamma).}
 \tag{R12}
\]
具体地 \(Q(BPD\gamma,\alpha)=-Q(PD\gamma,B\alpha)=-\int_{c_*\gamma}\alpha\)。

真实 \(\delta\) 在 \(x>1\) 为real Morse sphere，conjugation逐点固定并保留outward sphere orientation。在 \(x<1\) 的canonicalreal branch，用real-coefficient holomorphic Morse coordinates取imaginary sphere
\(z=i\sqrt{|\tau|}\,y\)，\(y\in S^3\)；conjugation是 \(y\mapsto-y\)，degree \((-1)^4=+1\)。故两侧
\[
 c_*\delta=\delta,\qquad BPD\delta=-PD\delta.
 \tag{R13}
\]
这不与ambientdegree−1矛盾。

actual \(\Gamma\) 是三个symmetricCCW contours上的graph
\[
 u_3=\frac{i\sqrt{1-xT}}
 {\sqrt{x}\sqrt{1-u_0^2}\sqrt{1-u_1^2}\sqrt{1-u_2^2}}.
 \tag{R14}
\]
每个root upper shore为正、lower shore为负，故沿contour
\(\sqrt{1-\bar u_j^2}=-\overline{\sqrt{1-u_j^2}}\)。
三个负号与 \(i\) 的conjugation使graph映到自身；三个CCW contours均变CW，productorientation为−。所以
\[
 c_*\Gamma=-\Gamma,\qquad BPD\Gamma=+PD\Gamma,
 \quad B\Pi PD\Gamma=+\Pi PD\Gamma.
 \tag{R15}
\]
这是actualcycle geometry，而非凭单一imaginaryperiod猜sign。与
\(\int_\Gamma\omega=-4i\pi^3y_0\) 一致。

## 5. \(\pm\) eigenspace、δnormalization及剩余Q-line

令 \(V_{\mathbf Q}^{\pm}=\ker(B\mp1)\)。R3使各自isotropic，nondegenerate \(Q|_V\) 给两者之间perfectpairing，故
\[
 \boxed{\dim_{\mathbf Q}V_{\mathbf Q}^{+}
 =\dim_{\mathbf Q}V_{\mathbf Q}^{-}=2.}
 \tag{R16}
\]
这是linear \(B\) 的Q维数；antilinear \(C\) 的fixed set是四实维。

实际localunit evaluation
\[
 A_\delta(t)=16\pi^2\int_0^t\frac{v(s)}{\sqrt{1-s}}ds,\qquad
 g=\int_\delta\omega=-\pi^2v(t)
\]
为real。已核localAJ compatibility给
\(\int_\delta r_{\mathbf R}=A_\delta+a^4q_0\)，\(q_0\in\mathbf Q\)。
真实 \(\delta\cdot\Gamma=8\) 与R15因此允许
\[
 \boxed{r_{\mathbf R,\delta}=\Pi r_{\mathbf R}
 -q_0a^4\Pi PD\Gamma/8.}
 \tag{R17}
\]
它保持projectedactualAJ class、reality和derivative，δevaluation恰为 \(A_\delta\)；若需要fullcompactlift，先对full \(r_{\mathbf R}\) 作同一projectedshift，再取 \(\Pi\)。未知 \(q_0\)不能默认1。

前轮actualvanishing theorem遂给
\[
 \nu_{\mathbf R,\delta}-\nu_{\rm corr}\in\ker P\cap\mathcal O_{t=0},
 \quad\nu_{\rm corr}=-16a^3\Psi.
 \tag{R18}
\]
normalized差在real \(t\) 实值，所以三个holomorphicTaylorcoefficients为real。没有推出它们0或代数；三维complexanalytic空间只限制到三实维。

加 \(a^4q\)、\(q\in V_{\mathbf Q}\) 仍real-compatible恰当且仅当 \(Bq=q\)。再保持δevaluation需 \(Q(PD\delta,q)=0\)；这个functional在plus-space非零（在 \(\Pi PD\Gamma\) 上为8）。故
\[
 \boxed{L_{\mathbf Q}=\{q\in V_{\mathbf Q}^+:
 Q(PD\delta,q)=0\}\text{ 一维。}}
 \tag{R19}
\]
旧反例 \(a^4PD\delta\) 是minus-space shift，破坏reality；不能再用它反驳已施reality条件。以下给真正仍相容的替代。

## 6. Physical、signed、sqrt-cover monodromy必须分开

设 \(M_0\) 是compactcycles绕actual \(x=0\) 一圈anticlockwise monodromy。\(P\)-periods使用 \(\omega=\sqrt{x}\eta\)，而 \(\eta=\omega/\sqrt{x}\) single-valued algebraic。实际η-periodoperator为
\[
 \widetilde P=(\theta+\tfrac12)^4-x(\theta+1)^4.
 \tag{R20}
\]
originexponents \(-1/2\) 四次，infinitylocal exponents1四次，所以
\[
 \operatorname{tr}M_0=-4,\qquad\operatorname{tr}M_\infty=+4.
 \tag{R21}
\]
originJordan恰4，下面explicitFrobeniusbasis也证明它。

令
\[
 U_0=-M_0.
 \tag{R22}
\]
这是有负号补偿的**signed actualintegralcycle transport**，不是另一个physicalone-turn monodromy。它unipotent、symplectic、singleJordan4；其period作用才是 \(P\) 的 \(\log x\mapsto\log x+a\)。sqrt-cover真实双圈是 \(M_0^2=U_0^2\)。

standardnoncrossing real-basedloop被conjugation变inverse，故
\[
 c_*M_0c_*=M_0^{-1},\qquad c_*U_0c_*=U_0^{-1}.
 \tag{R23}
\]
conifoldphysicalmonodromy仍是已证
\[
 M_1\gamma=\gamma+(\gamma\cdot\delta)\delta.
 \tag{R24}
\]
loop product与infinityinverse共轭，\(\operatorname{tr}(M_0M_1)=4\)。记 \(k_0=\delta\cdot M_0\delta\)，rank-one trace为
\[
 \operatorname{tr}(M_0M_1)=-4+(M_0\delta\cdot\delta)=-4-k_0.
\]
所以
\[
 \boxed{\delta\cdot M_0\delta=-8,\qquad\delta\cdot U_0\delta=8.}
 \tag{R25}
\]
这是actualrank-four cycle sector中的intersection，δ本身是actualintegralcycle。

## 7. 具体实际闭cycle生成剩余compatible方向

取actualclosedintegralcycle
\[
 \boxed{\gamma_L=(U_0-U_0^{-1})\delta-2\Gamma
 =-(M_0-M_0^{-1})\delta-2\Gamma.}
 \tag{R26}
\]
各term均是带明确orientation的actualcycle transport。R13、R15、R23给 \(c_*\gamma_L=-\gamma_L\)；symplectictransport给
\[
 \delta\cdot\gamma_L=8-(-8)-16=0.
 \tag{R27}
\]
故 \(q_L=\Pi PD\gamma_L\in L_{\mathbf Q}\)。

它非零。令 \(\Gamma_V\) 为Γ的rational \(V\)-homologyprojection、\(N=\log U_0\)。
singleJordan4给 \(\ker N=\operatorname{im}N^3=\mathbf Q\Gamma_V\)；\(\Gamma_V\) fixed由真实η-period \(x^{-1/2}y_0\) 给。
symplectic Lie relation \(N^*=-N\) 给
\(\ker N^3=(\mathbf Q\Gamma_V)^\perp\)。
\(\delta\cdot\Gamma_V=8\ne0\) 故 \(N^3\delta\ne0\)，\(N^2\delta\ne0\)。于是
\[
 (\gamma_L)_V=(2N+N^3/3)\delta-2\Gamma_V,\qquad
 N(\gamma_L)_V=2N^2\delta\ne0.
 \tag{R28}
\]
\(q_L\) 非零生成R19的Q-line。actualγL integral，**projected** \(q_L\) 目前只证明rational，不推projector integral或primitivegenerator。

合法shift \(r_{\mathbf R,\delta}\mapsto r_{\mathbf R,\delta}+a^4q_L\) 的normalizedscalar改变量为
\[
 p_L(x)=-a\int_{\gamma_L}\omega/16.
 \tag{R29}
\]
它real、homogeneous、conifoldholomorphic且非零。

## 8. Frobenius、真实intersection及connectioncoefficients

定义
\[
 A_n(\rho)=\left(\frac{(\rho+1/2)_n}{(\rho+1)_n}\right)^4,\quad
 F_\rho=x^\rho\sum_{n\ge0}A_n(\rho)x^n,\quad
 f_j=\partial_\rho^jF_\rho|_0/j!\ (0\le j\le3).
 \tag{R30}
\]
exactrecurrence给 \(PF_\rho=\rho^4x^\rho\)，故 \(f_j\) 是四个homogeneousbasis，highestlog为 \((\log x)^j/j!\)。这证明actual \(U_0\) singleJordan4。concomitant在originlimit给
\[
 C_0(f_0,f_3)=-1,\qquad C_0(f_1,f_2)=1,
 \quad\text{其余independent pairs为0}.
 \tag{R31}
\]
higher \(x\log^m x\) 项在limit消失；这是全branchconstantmatrix。

actual \(C_0(y_0,g)=-1\) 与 \(f_0=y_0\) 给
\[
 g=f_3+b_2f_2+b_1f_1+b_0f_0,\qquad b_j\in\mathbf R.
 \tag{R32}
\]
canonicalpositivebranch上g、f都real；\(f_3\) coefficient恰1。由logshift及R31，
\[
 C_0(g,g_{U_0})=a(2b_1-b_2^2)+a^3/6.
\]
actualdual sign \(\delta\cdot U_0\delta=-C_0(g,g_{U_0})/\kappa\)，
\(\kappa=-a^3/16\)，与R25给
\[
 \boxed{2b_1-b_2^2=a^2/3=-4\pi^2/3.}
 \tag{R33}
\]
Γ-period为 \(a^3f_0/2\)，所以R26/R29精确给
\[
 \boxed{p_L=\frac{\pi^2}{2}
 \{f_2+b_2f_1+(b_2^2/2+2\pi^2/3)f_0\}.}
 \tag{R34}
\]
未知 \(b_0\) 被actualmonodromycycle组合消去，未猜其数值。

令 \(a_n=A_n(0)>0\)，则
\[
 \ell'_n=\partial_\rho\log A_n(0)=8(H_{2n}-H_n),\quad
 \ell''_n=\partial_\rho^2\log A_n(0)
 =-16H_{2n}^{(2)}+8H_n^{(2)}.
 \tag{R35}
\]
R34等价于真实convergentseries
\[
 p_L(x)=\frac{\pi^2}{4}\sum_{n\ge0}a_nx^n
 \{(\log x+b_2+\ell'_n)^2+\ell''_n+4\pi^2/3\}.
 \tag{R36}
\]
elementary harmonic/Wallislimits为
\[
 \ell'_n\to8\log2,\quad \ell''_n\to-4\pi^2/3,\quad
 a_n=\frac1{\pi^2n^2}+O(n^{-3}).
 \tag{R37}
\]
前两由R35和 \(\zeta(2)=\pi^2/6\) 给，第三由centralbinomialasymptotic。

R29在conifoldholomorphic，故R36的first-order \(t\log t\) coefficient为0。其准确值为 \((b_2+8\log2)^2/4\)：固定coefficients leadingterm为
\((b_2+8\log2)^2/(\pi^2n^2)\)，余项 \(O(n^{-3})\) 的series在1有连续firstderivative；\(\log x=O(t)\) 的其它terms只产生higher-orderlog。
\(\sum x^n/n^2\) 的first \(t\log t\) coefficient为1，可积分derivative \(-\log(1-x)/x\) 核准。因此
\[
 \boxed{b_2=-8\log2,\qquad b_1=32\log^22-2\pi^2/3.}
 \tag{R38}
\]
这是actualmonodromy/cup/holomorphy的exactconnection推导，不声称新的文献优先权结论。

## 9. 真正仍相容的endpoint成本与算术限制

R36现在为
\[
 \boxed{p_L(x)=\frac{\pi^2}{4}\sum_{n\ge0}a_nx^n
 \{(\log x+\ell'_n-8\log2)^2+\ell''_n+4\pi^2/3\}.}
 \tag{R39}
\]
每项严格正，因为
\[
 \ell''_n+4\pi^2/3
 =4\sum_{k=n}^\infty
 \left\{\frac1{(k+1/2)^2}-\frac1{(k+1)^2}\right\}>0.
 \tag{R40}
\]
故全部 \(0<x<1\) 上 \(p_L(x)>0\)，并有actualanalyticlimitingperiod
\[
 \boxed{p_L(1)=\frac{\pi^2}{4}\sum_{n\ge0}a_n
 \{(\ell'_n-8\log2)^2+\ell''_n+4\pi^2/3\}
 >16\pi^2\log^22+\pi^4/3>0.}
 \tag{R41}
\]
tail \(O(n^{-4})\)：\(\ell'_n-8\log2=O(n^{-1})\)、R40为 \(O(n^{-2})\)、\(a_n=O(n^{-2})\)。uniformdomination给termwiselimit；不宣称singular-fibre integralcycle/lattice已构造。

originNilsson \((\log x)^2\) coefficient为
\[
 \frac{\pi^2}{4}y_0(x).
 \tag{R42}
\]
其constantcoefficient \(\pi^2/4\) 超越。因此两个合法real-compatible、δ-normalizedlifts若相差R29，不能同时具有originalgebraicNilssonpacket。**不是对conifoldTaylorjets非代数的证明**。

R41还证明这些条件没有固定endpoint。合法 \(q a^4q_L\)、\(q\in\mathbf Q\)，改变endpoint \(q p_L(1)\)。要命中指定endpoint \(A\)，仍须实际证明
\[
 [A-\widehat\nu_{\mathbf R,\delta}(1)]/p_L(1)\in\mathbf Q.
 \tag{R43}
\]
任意realcorrection不是合法rationalTateshift。\(\mathbf Qp_L(1)\) dense，不提供免费canonicalfundamentalinterval；integralprimitiveperiod另需整格工作。未证明R41的值无理或非代数。

若坚持sqrt-cover真实双圈，可取
\[
 \gamma_L^{(2)}=(M_0^2-M_0^{-2})\delta-8\Gamma.
 \tag{R44}
\]
R31–R33给 \(\delta\cdot M_0^2\delta=32\)。originperiodinjectivity给 \(N^3\delta=2\Gamma_V\)，sinh展开使R44的**Vprojection**为2γL的Vprojection；normalizedscalar为2pL，originlog² coefficient \(\pi^2/2\)。不把这个sector身份扩为全部compacthomology；actualΓ可能有其它compactsector。

## 10. Open boundary、原四项comparison的界限

realaverage、Γ/8δnormalization、R26全是compactrationalTateshifts。对固定raw \(R^+\)，若 \(j^*r-[R^+]=a^4a_U\)，改变compactlift仅使 \(a_U\) 加 \(j^*q\)。故其relativeboundary
\(\partial A^{\rm rel}\in H_2(E,\mathbf Q)\) 不变；reality不会免费使openTateclasscompact，也不使fluxzero。

positiveordinaryrepresentative未必 \(C\)-fixed：
\[
 c^*\overline{\log^+v}=\log^+v-a.
 \tag{R45}
\]
unitDeligneclass不变，ordinaryrepresentative可差rationalTatecochain。symmetrizing **open current** 是另一操作，可能改变relativeboundary/supporttrace，不能与compactaverage混用。所有cornercounterterms与flux仍由actualboundary研究负责。

本稿的compact结果是actualreal-compatible、δ-normalized全纯scalarlift的存在；**任意此类lift之间**的allowedrationalsector shifts仍一维，并有actualcycleR26、positivecostR41。对一个仅由这两个条件指定的lift，三个realholomorphiccoefficients未由条件本身核准。这不妨碍另一个explicit graph/corner/relative marking证明某个特定chosen lift恰为 \(\nu_{\rm corr}\)；若该marking证明完成，不能把本稿的choice自由再报告成该chosen comparison尚有缺口。没有新的特殊值无理性、all-placeCDT contradiction、integralnearby marking或Lean。

## 11. 实际来源和执行范围

本轮实际全文读 [compact positive-cut class](cdt_odd_R0_compact_positive_cut_class_20261006.md)；实际读 [relative mirror](cdt_odd_R0_relative_cycle_mirror_20261006.md) §3 全部Γ/root/orientation。compact derivative、Yukawa、vanishing normalization、boundary membrane诸冻结稿前轮已实际全文读/独审；本轮只使用其明确固定输入，不冒认又重读全文。

primary本轮实际KLM published PDF7–8、12、17：principalunit triple、Prop4.2任意degreeproduct、ring及open p=n>m target；SHA256
8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9。
[本地原件](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)；
[DOI](https://doi.org/10.1112/S0010437X05001867)。无新增PDF。

orientation/PDsign、linear与antilinear区别、Frobenius/cupmatrix、signedtrace、positiveperiodcost为独立纸面推导。初步通信曾将signed \(U_0\) 简称T₀；正式落稿前发现half-Kummer sign即通信纠正，最终明确physical \(M_0\)、signed \(-M_0\)、cover \(M_0^2\)，没有错误版本冻结。

数学producer执行/import数0，旧/同行执行/import数0；Python只读抽取PDF，无数值搜索、PSLQ或数学verifier。第一次NEW保存因JavaScript string中的反引号造成parse error，未写入任何文件；此最终稿另用合法rawstring保存。
