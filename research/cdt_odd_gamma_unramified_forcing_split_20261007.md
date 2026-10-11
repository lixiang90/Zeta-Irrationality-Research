# 原九阶系统的无新增跳跃有理强迫必拆分：全部极点、投影与有理 pullback 校准

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority为当前主报告§190和delivery_relative_lift_tensor_reference，SHA61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd；596冻结记录（591数学、5guards）只读。唯一NEW纸面主稿，不创建/执行/import/rerun数学producer、不扩prime表、不改冻结稿。本轮actual FULL重新读冻结Gamma G1–G19、dual/lift D1–D17/公式D1–D30全部七节、tensor T1–T28/全部十节，以及authority§190；audit完整JSONparse/current_progress与物理SHA，不称本人全文人工重审596 records。

本文证明准确的splitting theorem而非所有period方法no-go：原L中的有理强迫若所有新增ordinary-point完整jump都为零，连接常数C_R必有理。高阶pole、无穷远、Galois有理性和所有branch均覆盖。另给actual rational pullback的nonsplit polynomial forcing、真实Taylor方程和重新证明的全primecap；它越出该splitting假设，尚未产生新数值无理性。

## 1. 固定实际L、Taylor particular与完整连接常数

令
\[
 a=(\tfrac12^\times5,\tfrac15,\tfrac25,\tfrac35,\tfrac45),\qquad
 \Lambda=3200000,\quad c=\Lambda^{-1},\quad D=t\partial_t,
\]
\[
 L=D^9-\Lambda t\prod_i(D+a_i),\qquad
 f_0(t)=\sum_{n\ge0}h_nt^n,\quad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbf Z.
 \tag{U1}
\]
L的finite singularities恰0,c，∞亦为原base singularity；普通∂t坐标的leading coefficient
\[
 \ell_9(t)=t^9(1-\Lambda t).
 \tag{U2}
\]
原系统不可约，MUM的analytic homogeneous solution恰Cf0，且ψ=Δ_cf0≠0；本轮primary GM PDF1–3实际读，其PDF2的无共同根modZ判据适用：0与−a_i差值全非整数。固定与冻结稿相同0<t<c路径和log分支。

对
\[
 R\in\mathbf Q(t)\cap t\mathbf Q[[t]],\qquad \operatorname{radius}_0(R)>c,
\]
唯一actual Taylor particular B_R(0)=0、LB_R=R由
\[
 b_n=h_n\sum_{m=1}^n\frac{R_m}{m^9h_m},
 \qquad R_m=[t^m]R
 \tag{U3}
\]
确定。本轮FULL读冻结dual D6并重新核其tail证明：h_n=HΛ^n n^(−9/2)(1+O(1/n))；任意c<q<radius(R)给R_m/(m⁹h_m)=O((Λq)^(−m)m^(−9/2))。故
\[
 C_R=\sum_{m\ge1}\frac{R_m}{m^9h_m},\qquad
 A_R=C_Rf_0-B_R
 \tag{U4}
\]
绝对收敛，A_R的n阶系数O(q^(−n)n^(−9))，实际holomorphic于|t|<q。因此完整
\[
 \boxed{\Delta_cB_R=C_R\psi.}
 \tag{U5}
\]
这包括完整germ而非leading branch coefficient，不能只由一个endpoint零值代替。

## 2. 普通点任意高阶pole：完整jump与唯一代数极部

设μ为R的finite pole，μ≠0,c。因R rational，μ∈Qbar；令x=t−μ，pole order为p≥1。
在μ邻域把L改写为ordinary first-order companion system y'=M(x)y+v(x)R，M,v analytic、代数Taylor系数，fundamental matrixY analytic invertible。Variation of constants gives y=Y(C+∫Y^-1vR dx)。integrand meromorphic，只含有限principal part和analytic part，其antiderivative为有限Laurent、analytic与constant-vector log。因此actual scalar
\[
 \boxed{B_R(x)=M_\mu(x)+H_\mu(x)\log x,\quad
 M_\mu\text{ meromorphic},\quad H_\mu\text{ analytic},\quad LH_\mu=0.}
 \tag{U6}
\]
全部jump为χμ=2πiHμ。Hμ=0恰等价于B_R在μ meromorphic；不以最高log项或某个单分量为零替代。任何两个particular branches的差属于L的齐次解，齐次解在ordinary μ analytic，故同一μ邻域的Laurent负部与Hμ不随particular branch改变。将local jump沿不同路径送回原基点时，其coordinate vector可经invertible homogeneous continuation改变，但零与非零保持，零jump条件亦不依赖该选择。

若B_R的Laurent负部首项q_-m x^-m，m≥1，则L首项为
\[
 -\ell_9(\mu)\,m(m+1)\cdots(m+8)\,q_{-m}x^{-m-9}.
 \tag{U7}
\]
它非零且pole order≥10；Hμlogx的L-image最多pole9。因此m=p−9（若负部存在），特别p≤9时不可能有负部。

从R的x^-p coefficient与U7先解q_-(p−9)，再按pole order p−1,…,10解其余q_-m。每一步只除以μ∈Qbar中非零数，所用L/R local coefficients也在Qbar，故
\[
 \boxed{Q_\mu(x):=\operatorname{pp}_\mu B_R
 =\sum_{m=1}^{\max(p-9,0)}q_{-m}x^{-m}
 \in\overline{\mathbf Q}[x^{-1}],}
 \tag{U8}
\]
准确唯一。p>9时最高coefficient由非零r_-p确定，必非零，degree恰p−9，其余coefficients可为零；p≤9时负部为空。以上确定的是所有principal coefficients，不是仅leading coefficient；没有把homogeneous比较常数当代数数。

从U6更有
\[
 \boxed{\chi_\mu=0\quad\Longleftrightarrow\quad
 \operatorname{pp}_\mu(R-LQ_\mu)=0.}
 \tag{U9}
\]
向右：B_R−Qμ analytic，L作用仍analytic。向左：ordinary ODE有analytic particular解R−LQμ，任何其它solution与它差analytic homogeneous，故B_R−Qμ analytic。高阶pole中未由U7的triangular equations自动支付的正是orders9,…,1的九个compatibility条件。

## 3. 九个full-residue条件及低阶pole必留jump

实际selfdual L*=−L（dt/t adjoint）有冻结dual D4–D6的非退化Green pairing ℬ，满足Dℬ(f,g)=fLg+(Lf)g。取μ-local homogeneous basisv_i，以∂t^jv_i(μ)=δ_ij正规化，0≤i,j≤8；它们的所有Taylor coefficients在Qbar。沿小正向loop积分得
\[
 \mathcal B(v_i,\chi_\mu)
 =2\pi i\operatorname{Res}_{t=\mu}v_i(t)R(t)\frac{dt}{t}.
 \tag{U10}
\]
ordinary μ使ℬ非退化，所以
\[
 \boxed{\chi_\mu=0\Longleftrightarrow
 \operatorname{Res}_\mu v_iR\,dt/t=0\quad(i=0,\ldots,8).}
 \tag{U11}
\]
每个residue只需v_i的有限jet，故九个条件确为代数线性条件。用原Frobenius φ_i写同式会出现实际period derivatives；local canonical basis指出vanishing条件本身不需要未知的comparison matrix。U9与U11是同一完整条件的两种可核表示，本轮不执行这些tests。

对pole order1≤p≤9，U8为0，而R pole非零，U9迫χμ≠0。更精确，令R=r_-p x^-p+O(x^(-p+1))，k=9−p，则
\[
 \boxed{H_\mu(x)=
 \frac{r_{-p}}{\ell_9(\mu)(-1)^{p-1}k!(p-1)!}x^k+O(x^{k+1}),\quad
 k=9-p.}
 \tag{U12}
\]
证明∂t⁹(x^klogx)=(-1)^(p−1)k!(p−1)!x^-p；L低阶项和higher H coefficients不改最早pole。非零homogeneous解在ordinary点vanishing order≤8，故k准确。冻结ζ5 forcing pole5即k4，是此全低阶结论的实际实例。

## 4. 全有限极部的Galois下降，而非branch实性猜测

对每个μ解U7–U8的unique principal part。L、R在Q(t)，任意σ∈Gal(Qbar/Q)把μ和R local expansion送到σμ，并把triangular system送到该点的同一system。唯一性给
\[
 \sigma\bigl(Q_\mu(t-\mu)\bigr)=Q_{\sigma\mu}(t-\sigma\mu).
 \tag{U13}
\]
定义proper partial-fraction sum
\[
 Q(t)=\sum_{\mu\in\operatorname{Poles}(R)}Q_\mu(t-\mu).
 \tag{U14}
\]
有限pole集Galois-stable；U13使Q在Qbar(t)被全Galois固定，故
\[
 \boxed{Q(t)\in\mathbf Q(t).}
 \tag{U15}
\]
Q只在R新增ordinary poles有pole，并在0、c analytic；它在∞是proper rational function，Q(0)∈Q。这证明每个individual Laurent coefficient代数、所有共轭pole合成有理；不要求每个μ或其individual coefficient本身有理，也不对实际B_R的全部Taylor/connection constants作Galois操作。

## 5. 全部新增ordinary jumps为零的准确splitting theorem

假设所有μ∈Poles(R)都有χμ=0。U9使
\[
 S(t)=R(t)-LQ(t)
 \tag{U16}
\]
没有任何ordinary finite pole。Q在0,c analytic，L在普通D形式有polynomial coefficients，所以S在0,c也analytic。因此S∈Q[t]，且R(0)=0、(LQ)(0)=0给
\[
 \boxed{S\in t\mathbf Q[t].}
 \tag{U17}
\]
这一步保留了∞：finite-pole-free rational function就是polynomial，可有任意finite polynomial degree，不假设S在∞衰减或没有pole。

写S=Σ_(m1..M)S_mt^m，定义准确
\[
 C_S=\sum_{m=1}^M\frac{S_m}{m^9h_m}\in\mathbf Q,\qquad
 Q_S(t)=\sum_{m=1}^M\frac{S_m}{m^9h_m}
 \sum_{n=0}^{m-1}h_nt^n\in\mathbf Q[t].
 \tag{U18}
\]
实际polynomial-forcing解B_S=C_Sf0−Q_S，且Q_S(0)=C_S。B_R−Q在0 analytic、constant −Q(0)，同一S的analytic解只差f0倍数。因此
\[
 \boxed{B_R=T+C f_0,\quad
 T=Q-Q_S\in\mathbf Q(t),\quad C=C_S-Q(0)=-T(0)\in\mathbf Q.}
 \tag{U19}
\]
T在0,c analytic。由U5和ψ≠0，
\[
 \boxed{C_R=C=-T(0)\in\mathbf Q,\qquad R=LT.}
 \tag{U20}
\]
这给出所需**完整splitting theorem**：本实际L、rational R、radius>c和所有新增ordinary full jumps为零，不能产生nonrational C_R。

反向也准确：若R=LT、T∈Q(t)且0,c analytic，则B_R=T−T(0)f0，全部新增ordinary jumps为零；U4给C_R=−T(0)。由L无非零rational homogeneous solution，T唯一。实际可写成等价条件
\[
 \boxed{\text{所有新增ordinary jump为零}
 \iff R\in L(\mathbf Q(t)),\qquad C_R=-T(0).}
 \tag{U21}
\]
U21的右边在本R约束下自动迫T在0,c analytic：0处pole被D9首项保持；c处负整数pole指数不在0..7,7/2中，leading indicial coefficient非零，与R analytic冲突。ordinary其它点则由U7控制。

同一证明可将Q换成任意number fieldE，得到T∈E(t)、C_R∈E；必须同时保留R、L的coefficients在E。不允许把transcendental normalization免费归入该结论。

## 6. 高阶pole、∞和所有branches的边界实例

高阶pole确可没有log，并不是“R有pole⇒必jump”的过强说法。取
\[
 T(t)=(1-t)^{-1},\quad R=LT\in\mathbf Q(t)\cap t\mathbf Q[[t]],
 \quad B_R=(1-t)^{-1}-f_0,\quad C_R=-1.
 \tag{U22}
\]
μ1为ordinary点，R pole order10，B_R pole order1，全部ordinary jump为零；radius(R)=1>c。此例全式直接验证，未运行程序。它说明B_R本身仍可非rational，因f0≠rational；split结论是C_R有理和T有理，不是所有B_R必有理。

∞仍为原base singularity。U19已包含B_R在∞可能来自C f0的branch，以及T的rational poles。若额外要求整个∞full jump也零，则C=0：f0在0已fixed，若在∞也fixed，原三点loop relation便迫在c也fixed，违反ψ≠0。所以
\[
 \boxed{\chi_\mu=0\text{ 对全部新增ordinary }\mu
 \text{且 }\Delta_\infty B_R=0
 \ \Longrightarrow\ B_R=T\in\mathbf Q(t),\ C_R=0.}
 \tag{U23}
\]
不以∞“没有新增ordinary pole”偷换成“没有base branch”；若未加∞fixed，本稿只声称U19–U21。branch/path变更只给homogeneous difference，普通点的principal parts和零jump保持；没有遗漏其它particular branches。

## 7. 真正消掉非零μ jump的rational differential projection只能输出rational

令χμ≠0为某个新增ordinary full jump，且
\[
 \mathcal A\in\mathbf Q(t)\langle D\rangle,\qquad
 \mathcal A\chi_\mu=0.
 \tag{U24}
\]
由于Lχμ=0、原L irreducible，χμ的monodromy orbit张成全部9维L-solutions。rational coefficients single-valued，因此A杀其全部orbit，即杀全部L-solutions。对A以L作right Euclidean division，余项order<9若杀九维ordinary solutions只能为0。unique rational division gives
\[
 \boxed{\mathcal A=\mathcal U L,\quad
 \mathcal U\in\mathbf Q(t)\langle D\rangle,\quad
 \mathcal A B_R=\mathcal U R\in\mathbf Q(t).}
 \tag{U25}
\]
同理A(B_R−u f0)=U R。这里是完整jump为零的结论；只消最高log系数、把χ映成另一系统、非rational projector或χ本来为0，均不在hypotheses内。U22中χ=0但identity的output仍非rational，正说明非零条件不可删。

若A=Q(D)、Q∈Q[X]为非零constant-coefficient Euler polynomial，则甚至不存在U24：在c≠0，Q(D)是ordinary scalar ODE，所有齐次solutions在c analytic；若它杀χμ，前述irreducibility迫它杀f0，而f0在c有ψ≠0，矛盾。因此提高Q degree也不提供这个完整kill，不能把阶≥9当逃逸。零operator只给零rational row。

## 8. 确切逃逸条件：新base singularities和多conifold的角色

U20依赖两个实际事实：ordinary-point Laurent负部的唯一代数下降，以及finite pole消去后只剩polynomial forcing，而本L的polynomial forcing都split。要得到nonrational C且消新增ordinary jumps，至少应改变其中一项。

1. 若强迫的pole位于新的**base singularity**，ordinary triangular U7不适用；regular-singular indicial kernel/resonance可以给非trivial extension。
2. 若base具有多个finite conifolds和多步coefficient recurrence，扣去普通极部后的polynomial particular不必split。已知Apéry L_A leading1−34t+t²有两finite点，L_A B_A=6t是具体成功的非齐次校准；它不是本L的免费例外。本轮actual FULL读冻结tensor T1–T28/全部十节，其中T28给同一校准；本文不复证其数值无理性，也不继承上轮Apéry原件读页。原L的一步h_n recurrence使每个t^m强迫都等于一个f0减有限截断，正是U18的特殊splitting机制。
3. 若forcing itself为真正harmonic/log-period，R不在Q(t)，U17的finite-pole-free rational→polynomial下降不能使用。但保留一个omittedpoint仍可能受同叶参考族约束，不能只把阶数升高当成功。本文不另发展独立harmonic rank/cap支线。

这些是绕过本文定理hypotheses的具体入口，并非已经给新ζ/L定理。加入更多ordinary poles、升高pole阶、合并rational forcing来取消全部μ-jumps，仍落入U20；κ5或κ7作为C_R的另一rational-forcingidentity若真有nonrational值，至少留一个ordinary jump。

## 9. Actual quadratic pullback：两conifold与nonsplit polynomial forcing

具体取
\[
 t=x(1-x),\quad D_x=x\partial_x,\quad
 \delta=\frac{1-x}{1-2x}D_x,
\]
\[
 \boxed{L_{\mathrm{pb}}=\delta^9-\Lambda x(1-x)\prod_i(\delta+a_i).}
 \tag{U26}
\]
这是实际rational pullback，不把δ^9展开后当作commuting coefficients；δ就是D_t在cover上的chain rule。两conifold preimages准确
\[
 r_\pm=\frac{1\pm\sqrt{1-4c}}2.
 \tag{U27}
\]
此外x0、1是原MUM preimages，x1/2是ordinary critical preimage的apparent scalar singularity，∞是原∞的degree2 preimage。它们全部保留；并不是仅多了两个任意ordinary poles。

考虑真实polynomial-forcing问题
\[
 \boxed{L_{\mathrm{pb}} B=x,\qquad B(0)=0,\quad B\in\mathbf Q[[x]].}
 \tag{U28}
\]
在0，δ=D_x+O(x)且t=x+O(x²)，故实际rational operator可唯一展开
L_pb=D_x⁹+Σ_(ℓ≥1)x^ℓQ_ℓ(D_x)，Q_ℓ∈Q[X]、degree≤9。
这里Q_ℓ按U26的noncommutative operator准确取coefficient定义，不用旧t的h_n直接充作x的homogeneouscoefficients。所需完整Taylor方程为
\[
 \boxed{b_0=0,\qquad
 n^9b_n=\mathbf1_{n=1}-\sum_{\ell=1}^nQ_\ell(n-\ell)b_{n-\ell}
 \quad(n\ge1).}
 \tag{U29}
\]
这证明存在唯一Q-Taylor germ，b1=1；可以纯纸面复核，未执行producer。

该forcing确**nonsplit over C(x)**：若某rational T满足L_pbT=x，则在x1用u=x−1，δ=u∂u+O(u²)∂u，t=−u+O(u²)。若T pole orderm≥1，δ⁹的leading coefficient(−m)⁹≠0，t乘项pole低一阶，不能与analytic RHS相合。故T analytic于1；而所有δ-derivatives在1为0、t项也0，迫(L_pbT)(1)=0，违反RHS x在1等于1。因此
\[
 \boxed{x\notin L_{\mathrm{pb}}(\mathbf C(x)).}
 \tag{U30}
\]
特别B不能是rational function，也不能是rational T加任何homogeneous solution。{1,B}实际Q(x)rank2；未把可能的whole scalar order当function rank。

对0附近的inverse branch
\[
 X(t)=\frac{1-\sqrt{1-4t}}2
 =\sum_{m\ge1}\operatorname{Cat}_{m-1}t^m,\quad
 \operatorname{Cat}_{m-1}=\frac1m\binom{2m-2}{m-1}\in\mathbf Z,
\]
定义L\widetilde B=X(t)、tildeB0=0。U3的recurrence对任意analytic forcing都适用，故实际
\[
 \widetilde b_n=h_n\sum_{m=1}^n
 \frac{\operatorname{Cat}_{m-1}}{m^9h_m},\qquad
 B(x)=\widetilde B(x(1-x)).
 \tag{U31}
\]
这是在重新写明nonrational algebraic forcing之后推导的身份，不把old rational C_R formula免费移给new model。X radius1/4>c，重新应用U4的analytic tail proof，给第一conifold完整jump
Δ_(r_-)B=C_X ψ(x(1−x))，C_X=Σ Cat_(m−1)/(m⁹h_m)>0；其evaluation或irrationality未知，第二conifold的独立path/comparison和full jump未算出。

全finite-place费用也可以重新证明：本轮FULL读dual D26–D28所证D_n⁹ h_n/(m⁹h_m)整，Catalan整数使D_n⁹ tildeb_n整；composition x(1−x)的coefficients整数，且贡献indices m≤n满足D_m|D_n。因此
\[
 \boxed{D_n^9[x^n]B\in\mathbf Z\quad(n\ge1).}
 \tag{U32}
\]
δ=(1−x)/(1−2x)D_x的multiplier亦有整数Taylor coefficients，D_x只乘index整数，所需旧indices均≤n；因此任何fixed δ^jB使用同一D_n⁹ cap，但实际多行rank须另证，不能直接领取整个jet rank。没有free algebraic-coordinate denominator或archimedean scale：实际x取原integer polynomial，全部finite singular positions亦按U27同时改变。此cap只为这些实际coefficients所证，不移给旧原ξ。

新增base MUM x1的障碍准确可见。该点在原t的另一inverse branchforcing为1−X(t)=1+O(t)，而原Frobenius family[s⁹]Φ满足Lφ9=1，其leadinglog⁹/9!。减去它后forcing无constant，存在analytic particular；剩余homogeneous最高log≤8。因此
\[
 \boxed{B(x)=\frac{(\log t(x))^9}{9!}
 \quad\text{mod lower log degree and positive-}t\text{ terms near }x=1.}
 \tag{U33}
\]
无论路径的homogeneous comparison如何，最高log coefficient不变。故其x1fulljump非零且不能由u f0(t(x))消掉。x1/2反而可填：原t1/4是L ordinary点，forcingX局部analytic加(t−1/4)^1/2analytic；ordinary inverse给analytic加(t−1/4)^19/2analytic，无log。pullback t−1/4=−(x−1/2)²后成为analytic x-series，homogeneous solutions亦analytic。这支付apparentcritical，不将其遗漏。

所以U26–U33给一条真实两conifold、polynomialforcing nonsplit的新model和准确Q-Taylor/cap接口；同时证明了还必须处理x1、第二conifold、全部comparison和CDT同叶参考。它尚未给一个数字等于C_X的ζ/L identity，也未取得strict margin，不能把“有两个conifolds”自动当成功。

**U34（当前rank2接口的全map门槛）。** x1的log⁹项使每个target-admissible holomorphic map φ:(D,0)→(C,0) omit1：若φ(z0)=1，finite local multiplicity把U33最高log项变成非零log⁹(z−z0)，仍不能meromorphic。取参考coordinate z=x/4及
\[
 g(z)=\sqrt{1-4z}
 =1-2\sum_{n\ge1}\operatorname{Cat}_{n-1}z^n\in\mathbf Z[[z]].
\]
{1,g}在Q(z)上线性无关，因为1−4z的simplezero使其不是Q(z)中的square；g algebraic且holonomic。对同一φ，ψ=φ/4 omit1/4，1−4ψ=1−φ在单连通disc中无零，因此指定square-root germ g∘ψ在全disc holomorphic。这个参考的全部finite-place费用为0；target B没有被rescale，其U32费用仍原cap9。

本轮实际FULL读CDT v2 PDF66–69的Definition6.0.1、Theorem6.0.2及Cor6.0.14。写ρ=log|φ′(0)|，J为该corollary的double rearrangement numerator
\[
 J(\varphi)=\iint_{\mathbb T^2}
 \log\max(|\varphi(z)|,|\varphi(w)|)\,d\mu(z)d\mu(w).
\]
若ρ>log4，参考的tau0及rank2给J(ψ)≥2log|ψ′(0)|；精确scaling为J(ψ)=J(φ)−log4，log|ψ′|=ρ−log4，故
\[
 \boxed{J(\varphi)\ge2\rho-\log4.}
 \tag{U34}
\]
对U32实际{1,B}，用九个width1 columns (0,1)^t、e0得到tau_T=27/4。B确holonomic，因为(D_x−1)L_pb B=0，但不由此领取更大functionrank。若ρ≤tau_T，target derivative gate未开；若ρ>tau_T>log4，target严格rank2矛盾需要J(φ)<2(ρ−tau_T)，而U34给相反更强的lower，因为2tau_T>log4。所以当前这一个rank2/cap9接口对全部admissible φ不能取得strict CDT margin。

多map亦有同对象比较：固定同一γ分割[0,2]及相同maps，把每个map都除4。Theorem6.0.2的patched g只减log4，rearrangement double integral亦只减log4；derivative-gap ratios不变，准确完整numerator K_ψ=K_φ−log4，largest ρ只减log4。参考给K_φ≥2ρ−log4，仍排除target的K_φ<2(ρ−27/4)。这不宣布所有pullback/新base方法失败，不把费用9当最优，更不免费沿用原A=-2²⁰的零费用root-power族；此处参考coordinate与scaling已显式支付。新的row、完整周期投影、改进mixed array或其它base geometry仍须重新证明。

简短harmonic校准只用于范围：例如A=−2²⁰时R_H=−log(1−At)/(1−At)=ΣH_mA^mt^m不在Q(t)，ΔμR_H=−2πi/(1−At)≠0，故L(ΔμB_H)≠0；U25的homogeneous-jump hypothesis失效。它逃过rational-forcing假设，仍保留μomission，不能据此宣布逃过同叶参考；本稿不扩写其独立rank/cap研究。

## 10. 本轮成果、来源页域与闭合

本文新增纸证为：任意pole阶ordinary full-jump/代数principal-part等价；全部共轭极部Galois下降；original rational-forcing准确U19–U21拆分与C_R有理；∞附加fixed的精确范围；非零μ-jump的rational differential kill只能输出rational，constant Euler projection甚至不可能；以及实际quadratic pullback、nonsplit polynomial forcing x、真实Taylor/cap方程和不可免费删除的新base MUM。后一项提供一个明确超出splitting hypotheses的model，并以U34支付当前rank2/cap9的全map和multimap参考门槛；尚未完成constant evaluation、全部conifold comparison、有效integral geometry或另一接口的strict holonomy比较。

本轮复用既有primary Golyshev–Mellit0902.2003v1：literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf，归档10页，actual FULL text PDF1–3共3distinct页，重点PDF2不可约与finite pseudoreflection；另CDT v2 literature/cdt2024_l2_chi_minus3.pdf实际FULL text PDF66–69共4页，准确核U34的array、holonomic relaxation和single/multi-map scaling。本文own主稿域7distinct页，不继承此前任何GM/BH/BV/Apéry/CDT读页；assigned Cartier outgoing review的另35distinct页单独记录，不混成本主稿来源。本轮primary新下载0、render0，数学producer新建/execute/import/rerun、数学失败、prime扩表及Lean0。variation-of-constants、triangular/Galois下降、Ore division和pullback/Taylor/base-MUM局部式均在正文自足纸证，不执行原件或辅助数学算法。

当前仍未证明任何新的ζ(7)、ζ/L/Catalan无理性或LI；原ξ=αζ4+βζ5完整carrier亦未解决。本文只约束原L的指定forcing/projection类，并明确留下多conifold、真正新base/relative geometry及更强整化路径。唯一NEW稿待actual FULL正式独审、作者最终FULL回读与单向FINAL来源收据；596旧记录不改。
