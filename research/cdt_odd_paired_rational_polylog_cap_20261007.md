# 真正 Q(x) 变基后的 polylog 分母：抵消响应、prefix 下界与实际 compound 门槛

2026-10-07，NEW，source_pencil_finalize。authority 为 main §§166–170 与 delivery_hasse_bridge SHA94eec763 快照；564冻结记录（559数学、5guard）全部只读。原 B6/k3/s5、完整 S、degree<3n 与固定有理源 ξ=αζ(4)+βζ(5)，β≠0 保留。本文纯纸证，不创建、执行、import、rerun任何数学 producer，不扩prime表。

本文补上前轮 B21 的真实 Q(x) 变基缺口。关键是把最高次数与低一次项可能发生的同阶抵消写成一个具体响应，而不是重用 fixed-polynomial 的 shifted-index 论证。结果仍限于规范 Ξ=αLi4+βLi5 的有限 polynomial module、CDT 的固定 finite-LCM/N^e 类型及标准 slit leaf；不是其他 period 实现或所有方法的排除定理。

## 1. 实际模块、固定量词与必要回读

本轮实际全文回读冻结 [bridge B1–B21](cdt_odd_paired_compound_period_module_bridge_20261007.md)、其[root独审全稿](cdt_odd_paired_compound_period_module_bridge_independent_review_20261007.md)、[Hasse H1–H17](cdt_odd_paired_hasse_jet_mixed_gram_20261007.md)，以及authority §§166–170。最新audit仅完整syntax parse并读取metadata/current progress，SHA匹配94eec763；不冒称本人逐条重核全部564冻结记录。

对固定实际 n、1≤d≤2n，令 Q_a(T) 为 C_d(B_n(T)) 的全部实际 minors，q为其 polynomial coefficient matrix 的 Q-rank。冻结B6给

\[
\Xi(x)=\sum_{N\ge1}\frac{\alpha N+\beta}{N^5}x^N,
\quad\Xi(1)=\xi,\quad
1,\Xi,\ldots,\Xi^d\text{ 在 }\mathbf C(x)\text{ 上独立}.
\tag{R1}
\]

这里 Ξ(1) 指实 x↑1 的绝对收敛端点。记

\[
\mathcal W_{n,d}=\operatorname{span}_{\mathbf Q(x)}\{Q_a(\Xi(x))\},
\quad\dim\mathcal W_{n,d}=q.
\tag{R2}
\]

任何真正 rational-function 变基以 U(x)∈GL_q(Q(x)) 作用于一个已选basis。每个新row唯一写为

\[
F(x)=\sum_{\ell=0}^{j}a_\ell(x)\Xi(x)^\ell,
\quad a_\ell\in\mathbf Q(x),\quad a_j\ne0,
\quad F\in\mathbf Q[[x]].
\tag{R3}
\]

允许 a_ℓ 在0有有限pole，并允许它们的组合F在0正则；不能先假定每个a_ℓ都是polynomial。本文的row theorem也适用于任意这样的finite expression，不只来自实际minors。

先固定 n,d,U、源、F与各cap，再让 Taylor index N和prime p增长；U不能依p改变。若要保留原period投影，另须核 U在1正则及其端点值，例如 U(1)=I精确保留每个原endpoint，U(1)∈GL_q(Q)给明确可逆的有理period投影。分母定理不自动提供这些端点条件；它对更广泛的R3仍成立。

## 2. Rational Laurent coefficients 的全tail p-integrality

对任何固定 a(x)∈Q(x)，可写

\[
a(x)=x^h A(x)/B(x),\quad A,B\in\mathbf Z[x],\quad B(0)\ne0,
\quad a(x)=\sum_{s\ge h}a_sx^s.
\tag{R4}
\]

必要的固定有理scaling吸收到A/B，h∈Z。避开B(0)及固定scaling的有限primes后，B的formal inverse属于Z_p[[x]]，由递推系数即得 **所有** a_s∈Z_p。这是对无限正tail的uniform assertion，不只对选定有限coefficients的检查。对R3的全部a_ℓ选同一个有限exception set，并记h_*为它们最低Laurent orders的一个共同lower bound。

还避开源α、β的固定分母及β的numerator。对所有positive k<p²，

\[
v_p[x^k]\Xi=
\begin{cases}-5,&p\mid k,\\\ge0,&p\nmid k,\end{cases}
\qquad p^5[x^p]\Xi\equiv\beta\pmod p.
\tag{R5}
\]

在 N=kp+s、k和s固定时，R3任一非零convolution涉及的positive Ξ indices总和≤N−h_*，故p充分大时每个index<p²。正infinite rational tail不使这个上界变差，因为它从固定h_*开始。任意有k个p-divisible indices的sum至少kp；若其sum为(k+t)p、t≥1，则为满足index N，剩余rational Laurent index和非p indices之和必须≤s−tp，最终低于固定negative-tail lower bound。这就准确排除了额外整倍p的同层组合；不能把finite negative tail当作没有pole。

## 3. 两个真正 rational rows 的精确prime见证

### 3.1 最高系数非恒定

若R3的a_j(x)非恒定，则其Laurent expansion有某个固定 s≠0、a_(j,s)≠0。取N_p=jp+s，p充分大并另避该非零coefficient的固定numerator/denominator。

达到j个p-divisible indices的唯一贡献是全部j个indices=p、rational index=s。它给 a_(j,s)([x^p]Ξ)^j。最高次数其余terms至多j−1个p-divisible indices；所有低次数亦至多j−1个。R4保证各rational coefficients uniformly p-integral；R5以及finite negative-tail界排除额外p倍数。于是

\[
p^{5j}[x^{jp+s}]F\equiv\beta^j a_{j,s}\not\equiv0\pmod p,
\quad\boxed{v_p[x^{jp+s}]F=-5j},\quad p\nmid(jp+s).
\tag{R6}
\]

s可以为负，N_p最终仍为正；p>|s|时因s≠0而p∤N_p。无限其他terms虽可能相互抵消，却不能取消这个唯一最低层。

### 3.2 最高系数恒定，且j≥2

现在a_j是非零有理常数。此前B10的旧最低层会与a_(j−1)(x)的coefficients发生同阶抵消，故必须完整保留。定义实际响应

\[
\mathscr H(x):=j a_j\Xi(x)+a_{j-1}(x).
\tag{R7}
\]

Ξ不是rational function，由R1或非零translation monodromy已证明。因此H不可能是常数，且有某个固定 s≠0 的Laurent coefficient H_s≠0。取N_p=(j−1)p+s，p充分大，另避j、H_s和固定scalings的有限primes。

最高j次的j−1个p-divisible indices贡献，只有(p,…,p,s)的j个排列；s≤0时这些positive-index terms不存在，对应[x^s]Ξ=0。低j−1次的同层贡献准确是a_(j−1,s)([x^p]Ξ)^(j−1)。finite negative-tail界排除其中任一pole index为2p等额外p倍数；所有更低次数及其他terms至多j−2个p-divisible indices。因此两层合计恰给

\[
p^{5(j-1)}[x^{(j-1)p+s}]F
\equiv\beta^{j-1}\{j a_j[x^s]\Xi+a_{j-1,s}\}
=\beta^{j-1}\mathscr H_s\not\equiv0\pmod p,
\tag{R8}
\]
\[
\boxed{v_p[x^{(j-1)p+s}]F=-5(j-1)},
\qquad p\nmid((j-1)p+s).
\tag{R9}
\]

这不是声称每个原t0都能避开抵消，而是证明实际H存在一个固定offzero response。它不依赖数值period无理性：Ξ的函数非rational已由monodromy严格证明。

### 3.3 一次的恒定最高系数是明确例外

若j=1、a_1为非零常数，则F=a_1Ξ+a_0(x)。R4使a_0的第p coefficient在除有限primes后p-integral，故

\[
\boxed{v_p[x^p]F=-5.}
\tag{R10}
\]

但固定s≠0的index p+s处，Ξ和a_0的coefficients都p-integral，不能声称也有−5的shifted witness。这个例外在允许N^e时确实重要，不由R9的j≥2结论覆盖。

## 4. Basis不变的prefix下界和CDT row费用

对R3的每个nonrational F（即j≥1），R6、R9或R10都给固定整数k≥1、固定s∈Z，使除有限primes外

\[
v_p[x^{kp+s}]F=-5k.
\tag{R11}
\]

设δ_F(N)为前N coefficients的最小正共同分母。对p≤(N−s)/k的大primes，δ_F至少含p^(5k)。由PNT，

\[
\boxed{\liminf_{N\to\infty}\frac{\log\delta_F(N)}N\ge5.}
\tag{R12}
\]

这是任意真实Q(x)row的prefix必要下界。没有宣称δ_F的upper也为5，更没有把prefix指数5直接等同CDT的weighted τ。坏finiteprimes的rational coefficients可能另有费用；它们不破坏这个lower。

本轮实际重新完整文本读 [固定CDT v2](../literature/cdt2024_l2_chi_minus3.pdf) PDF66–69四页，使用6.0.3–6.0.9、Remark6.0.12、Corollary6.0.14及BasicRemark6.0.17。固定218页、SHA84c672bd；不继承上轮PDF页数或混用作者220页长稿。设一个row经一次固定integer scaling后具有该版type

\[
F(x)=u_0+\sum_{N\ge1}
\frac{u_Nx^N}{N^e\prod_{\ell=1}^R K_{b_\ell,c_\ell}(N)},
\quad K_{b,c}(N)=\operatorname{lcm}(1,\ldots,\lfloor bN+c\rfloor),
\quad u_N\in\mathbf Z.
\tag{R13}
\]

e、R、全部b≥0和offset c均先固定。空LCM为1，finite exceptional-prime localization也不能抵消大p见证。R6/R9中的N_p不被p整除，故N_p^e不贡献p；每个LCM factor最终至多贡献一个p。若N_p=kp+s，贡献者必有b≥1/k。准确−5k因此强迫至少5k个这样的factors，给

\[
\boxed{\deg_\Xi F\ge2\Longrightarrow\sigma(F):=\sum b_\ell\ge5,}
\quad\text{任意固定 }e\text{ 均不改变此界}.
\tag{R14}
\]

同样适用于degree1但a_1非恒定的row。若degree1且a_1恒定，R10仅给σ≥max(0,5−e)，不强制σ≥5。

## 5. 实际 full Q(x) compound basis 的完整障碍与monodromy

对W_(n,d)的任何actual Q(x)-full basis F_1,…,F_q，每row都满足R3且要求在0holomorphic。无需其coefficients固定polynomial。由R1的unique powers，degree≤1的ambient Q(x)-空间只有维数2，因此q≥3时至多两条independent rows不受R14的degree≥2界。

CDT cap array的column-step条件使σ_i非降，τ^flat=q^(−2)Σ_(i=1)^q(2i−1)σ_i。若σ_i<5，之前所有σ也<5，对应rows皆degree≤1，所以这种初段长度至多2。因此

\[
q\ge3\Longrightarrow\tau^\flat\ge5(1-4/q^2)\ge25/9.
\tag{R15}
\]

同一actual V_n=∂_TB_n由冻结H1严格正定。每个d-principal polynomial最高coefficient det(V_(I,I))>0，所以W_(n,d)有degree恰d的元素。若一个full Q(x) basis所有rows degree<d，则任何rational-coefficient组合亦degree<d，与此矛盾。因此d≥2时至少一row受R14约束；q1/q2分别给5及15/4。合并得到本轮主要结论

\[
\boxed{d\ge2,\ \{F_i\}\text{ 是实际 }\mathcal W_{n,d}\text{ 的 full }\mathbf Q(x)\text{ basis}
\ \Longrightarrow
\tau(b;e)\ge
\begin{cases}5,&q=1,\\15/4,&q=2,\\5(1-4/q^2),&q\ge3,\end{cases}
\quad>\log4.}
\tag{R16}
\]

τ^sharp≥0按同版定义，完整保留。标准D=C\[1,∞)的conformal radius4，使所有holomorphic φ:unit disk→D、φ(0)=0都有|φ′(0)|≤4。所以任何上述真正Q(x)变基仍不能满足选定CDT定理的正分母门槛。R16补上旧B21只限fixed-polynomial basis的缺口；没有排除新realization、Hadamard/trace、别的actual meromorphic leaf、子空间或别的分母定理。

Monodromy的结论亦在真正Q(x)变基下保持：绕1而不绕0时Ξ↦Ξ+v，v非零且在该loop不变，全部rational a_ℓ单值。若Σa_ℓΞ^ℓ invariant，对任意整数次continuation的最高系数即迫使所有ℓ≥1项为零。因此ambient module ⊕_(ℓ=0)^d Q(x)Ξ^ℓ 中的invariant part恰为Q(x)；实际W_(n,d)中的invariant part是W_(n,d)∩Q(x)，维数至多1，不保证它非零。假设ξ=c后减去任何rational function也不能消去nonrational row的branch。

需要区分这件事和φ pullback：某个新φ可能避开或以真实路径抵消这些loops，所以这里不证明所有possible meromorphic pullbacks都失败。R16的费用比较仍限定标准slit image；polynomial degree、matrixrank和actual meromorphic continuation从未合并为一个自动条件。

## 6. 确实改善flat cap的校准row、端点与当前进展

degree1例外有明确且保留原endpoint的Q(x)变换：

\[
F_0(x)=x\Xi(x),\quad F_1(x)=x^{-1}F_0(x)=\Xi(x),
\quad\lim_{x\uparrow1}F_0(x)=\lim_{x\uparrow1}F_1(x)=\xi.
\tag{R17}
\]

两者均在0holomorphic，1/x在1的值为1。F0在N=p+1有−5的精确witness，故即使有任意固定N^e，其flat row σ至少5。F1经固定清源分母后真实coefficients的type却是纯N^5，可取σ0、e5。这是一个确实降低flat cap的真实basis操作，不是把目标换成另一period。

但不能把e5删除：同版m1定义给I_ξ^1(ξ)=(1−ξ)²/2，因而τ^sharp(e)=2min_(0≤ξ≤1){eξ+e(1−ξ)²/2}=e。这个例子的single-row total cost仍5；m2校准basis(1,Ξ)的e=(0,5)，由BasicRemark6.0.17及homogeneity其τ^sharp=15/4。没有把flat cap的真实改善冒称整体strict margin，亦不将degree1例外外推到R16的d≥2 actual compound。

本轮取得的是R6/R8/R9的真实rational-coefficient抵消响应、R12的uniform prefix必要下界、R14/R16对真正Q(x)变基的CDT费用结论，以及R17的真实端点校准。仍未构造旧B18–B20所需的实际新过收敛period system，也未证明root低jet路线的strict analytic margin。没有新的单个ζ/L/Catalan无理性、数值线性无关性或Lean结论；独立全文审查与最后单向来源另存。
