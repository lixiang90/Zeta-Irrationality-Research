# 实际单关系的空间 logarithmic suspension：β(4)、G、ζ(3)、Ω 与新目标 Θ

2026-10-07。NEW。本稿只新增此稿及本轮 primary 网页归档；不改 root 主进展、旧研究稿、原仓库或旧 producer/guard。跳出前轮 plain-ζ Hermite determinant 的实处能量，直接构造 CDT 所需的实际有限空间变量芽。

新结果是一个完整可检验载体：仅一个目标关系使其进入 Q[[x]]，同时完整消去 x=1 的 logarithmic monodromy；给显式 holonomic 方程、真实函数秩、全部有限处分母、共同单值叶、精确双边界积分和任意 full Q(x) basis 的一个必要费用。它适用于 β(4)、β(4)−G/3、以及 aβ(4)+bG+cζ(3)。标准叶的费用仍不足，故没有新的数值无理性或 LI 结论。另把既有 Ω 身份提升成实际 16 维空间系统，准确证明仅 Ω 有理并不能完整填入 x=1；从其中的真实取消方向得到一个正周期新项目目标 Θ 和可完整填入1的单关系germ。

## 1. 一个真正单关系、完整填入普通点的 germ

固定整数 s≥2，定义实际 inverse-tangent polylogarithm

\[
 T_s(x)=\sum_{k\ge0}\frac{(-1)^k x^{2k+1}}{(2k+1)^s}
 =\frac{\operatorname{Li}_s(ix)-\operatorname{Li}_s(-ix)}{2i},
 \qquad T_0(x)=\frac{x}{1+x^2}.
 \tag{S1}
\]

θ=x∂x，故 θT_j=T_(j−1)，T_1=arctan x。这里 x 是真正空间变量，s 已固定；没有使用 higher-jet 稿中非 D-finite 的参数 z 生成函数。S1 的 series、导数链及真实 beta endpoint 都可直接逐项核验：

\[
 T_s(1)=\beta(s),\qquad
 \mathcal D_\beta=\mathbb C\setminus
 \bigl(i[1,\infty)\cup-i[1,\infty)\bigr).
 \tag{S2}
\]

指定从 x=0 出发的枝在 Dβ 上单值全纯；先由 T1 的 logarithm 表示，再逐次取 T_j(t)/t 的全纯原函数证明。x=0 的分子零阶使 t^−1 removable。因 x=1 是 Dβ 内的普通点，所有 T_j 在它的邻域真正全纯，而不只是端点连续。

定义 B_s(0)=0 的实际芽及任意 u∈C 的函数

\[
 B_s(x)=\int_0^x\frac{T_s(t)}{1-t}\,dt,
 \qquad F_{s,u}(x)=B_s(x)+u\log(1-x),
 \quad F_{s,u}'=\frac{T_s-u}{1-x}.
 \tag{S3}
\]

在 x=1 的实际局部邻域中，T_s−β(s) 可被 1−x 整除，因而

\[
 B_s=-\beta(s)\log(1-x)+H_s(x),
 \qquad F_{s,u}=(u-\beta(s))\log(1-x)+H_s(x),
 \tag{S4}
\]

H_s 是全纯函数。S4 是完整 germ identity，全部 local monodromy 恰为 2πi(u−β(s))；没有仅令最高项或一个点值为零。于是

\[
 \boxed{\beta(s)=u\in\mathbb Q
 \ \Longrightarrow\ F_{s,u}\in\mathbb Q[[x]]
 \text{ 且在整个 }\mathcal D_\beta\text{ 单值全纯}.}
 \tag{S5}
\]

后一结论由 S3 的右侧在 Dβ 上全纯和该域单连通得到。B_s 自身在 x=1 有真正 log 分支；此项不是人工可去 pole，也不是本来已允许的 meromorphic pole。关系只有一个，没有假设 β(s−2)、π 或其他 seed 有理。

对 s=4 可选 β(4)。也可令

\[
 \Psi_{a,b}=aT_4+bT_2,\quad
 \vartheta_{a,b}=a\beta(4)+bG,\quad a,b\in\mathbb Q, a\ne0,
\]
\[
 B_{a,b}=\int_0^x\frac{\Psi_{a,b}(t)}{1-t}dt,
 \quad F_{a,b,u}=B_{a,b}+u\log(1-x).
 \tag{S6}
\]

同样仅 ϑ_(a,b)=u∈Q 就给 S5 的全部结论。a=1、b=−1/3 准确对应既有 H10 的真实 M^(2)(1,1)/4=β(4)−G/3；没有把它当作纯 β(4) 或免费消去 G。S6 的所有低 T_j 本来就是 Q-Taylor 芽，故不需额外数值关系。

## 2. 有理 Taylor 系数、显式方程与全部实际秩

令 χ4(n)=0（n 偶）、(−1)^((n−1)/2)（n 奇）。由 S3 的局部绝对收敛展开，

\[
 [x^N]F_{s,u}=\frac1N
 \left(\sum_{j=1}^{N-1}\frac{\chi_4(j)}{j^s}-u\right),
 \quad N\ge1,\qquad F_{s,u}(0)=0.
 \tag{S7}
\]

S7 把单关系下的 Q[[x]] 有理化逐项闭合，而不是从一个 period endpoint 猜测其余 Taylor coefficients。S6 将 inner summand 换成 aχ4(j)/j^4+bχ4(j)/j^2。

整个实际 differential space 是

\[
 \mathscr V_{s,u}=\operatorname{span}_{\mathbb C(x)}
 \{1,T_1,\ldots,T_s,F_{s,u}\}.
 \tag{S8}
\]

其导数闭合由 S3 和 θT_j=T_(j−1) 给出。更直接，令 r(x)=x/(1+x²)，则实际 scalar homogeneous operator

\[
 \boxed{\left(\partial_x-\frac{r'}r\right)
 \theta^s(1-x)\partial_x F_{s,u}=0}
 \tag{S9}
\]

的 order 为 s+2，系数全在 Q(x)，且对任意 u 成立。S9 不将 B_s 或 F 与某个其他 hypergeometric particular 混用。S6 亦有 S8 的 s=4 导数闭合，故可用六维 rational first-order system或其 scalar 消元；不把同一函数重复求导算成新秩。

**S10（T tower 的实际独立性）。** 选择绕 x=i 一周、不绕 0、−i 的 based loop，从正实 basepoint 上行接近 i。T1 的 jump 是 π。递推积分并要求高阶 jump 在 i 消失，得到

\[
 \Delta_i T_j=\frac{\pi}{(j-1)!}
 \bigl(\log x-\log i\bigr)^{j-1}.
 \tag{S10}
\]

这也可从 Li1 的 logarithm 和 θ 链独立核回；log i 由该 bridge 固定。若 P0+ΣP_jT_j=0、P∈C(x)，作此 loop 后得到 log x 的 polynomial identity。log x 对 C(x) 超越：绕 0 反复平移 2πi 会给一个非零有限次 polynomial 无穷多个根。因此从最高 degree 逐项得 P_s=…=P1=0，再得 P0=0。这证明 1,T1,…,Ts 的实际 rank=s+1。

**S11（新增 F 的 rank 不会在目标关系下消失）。** 若 u≠β(s)，绕 x=1 的 loop 已给 F 非零 constant jump，而全部 T_j 不变，强制任一 relation 的 F coefficient 为0。若 u=β(s)，canonical loop1 确实平凡，但不能因此声称 F 落入原 T tower。

具体地，先沿 loop i 继续，再绕 0 q 次，得到 T_s 在 1 的值改变量

\[
 \frac\pi{(s-1)!}(2\pi iq-\log i)^{s-1}.
 \tag{S11}
\]

它是 q 的非零 polynomial，故可选某个整数 q 使值非零。所有 transported T_j 在 1 的局部仍全纯（log x 在1正则）。在此 branch 绕1给 F 一个非零 constant jump。最后逆向撤回前面的 i/0 loops，T_j 全回到原 branch，但 F 的该 constant 保留，因为 continuation 对 constant 是恒等。等价地，这是 conjugate loop1 与原 loop1 的差所给的 pure F translation。对任何 rational-function relation 作该 continuation，便迫其 F coefficient 为0。再用 S10。

所以对任意 u，包括 hypothesized rational target，

\[
 \boxed{\dim_{\mathbb C(x)}\mathscr V_{s,u}=s+2.}
 \tag{S12}
\]

S6 中 a≠0 时同一证明成立：transported endpoint 改变量是 π(a y³/6+b y)，y=2πiq−log i 的非零 polynomial；故 rank 精确为6。没有用有限 Wronskian 样本或抽象 period symbols 代替此证明。

## 3. 所有有限处的完整 cap 与 CDT 自然账本

写 D_N=lcm(1,…,N)、D_0=1。对固定 u∈Q 取整数 d>0 使 du∈Z；对 S6 再使 da、db∈Z。S1/S7 精确给

\[
 N^j[x^N]T_j\in\mathbb Z,
 \qquad d\,N D_{N-1}^s[x^N]F_{s,u}\in\mathbb Z.
 \tag{S13}
\]

S6 使用 s=4。S13 包括 p=2、所有奇素数及所有 p^e，没有只检查 large-prime head。固定 d 只是一遍整体 scaling，费用不增长；同一系统无需额外 seed normalization、Gaussian lattice index或π scaling。

将 N^j、N 都吸收到 D_N 可得到完全无 N^e 剩项的有效 CDT array：

\[
 (1,T_1,\ldots,T_s,dF_{s,u}):\quad
 \sigma=(0,1,\ldots,s,s+1),\quad e=0.
 \tag{S14}
\]

采用 s+1 个 width-one LCM columns，第 k 列在 σ<k 的初段取0，其后取1。这满足列阶梯条件，不遗漏额外 integration 的一层。m=s+2，全部安全费用是

\[
 \boxed{\tau_{\rm safe}=
 \frac1{m^2}\sum_{i=1}^m(2i-1)(i-1)
 =\frac{(m-1)(4m+1)}{6m}.}
 \tag{S15}
\]

β(4) 或 β(4)−G/3 的 m=6 费用准确为 125/36；G 的 m=4 费用为17/8。它们是完整 upper caps，不称必要最小费用。保留 exact N powers 可另用

\[
 \sigma=(0,\ldots,0,s),\quad
 e=(0,1,\ldots,s,1),\quad
 \tau^\flat=\frac{s(2s+3)}{(s+2)^2},
 \quad\tau=\tau^\flat+\tau^\sharp(e).
 \tag{S16}
\]

S16 未删除 τsharp(e)，亦没有在本稿重算 CDT 对此 e 的 minimization。S14–S15 已是一份完整无需该 minimization 的账本；下面更强的 necessary flat bound 即使允许任意 e 仍成立，故 β4 的失败判断不依赖遗漏 τsharp。

## 4. 任意真正 Q(x) full basis 的 prime-response 费用

本节固定 s≥2、u∈Q，先固定所有 rational coefficients，再令 Taylor index、p 增长。对每个实际 row

\[
 R(x)=a_F(x)F_{s,u}+a_0(x)+\sum_{j=1}^s a_j(x)T_j(x)
 \in\mathbb Q[[x]],\quad a_\bullet\in\mathbb Q(x),
 \quad a_F\ne0,
 \tag{S17}
\]

允许各 a 在0有有限 pole，其组合只要求 R 正则。写 a=x^h A/B，A,B∈Z[x]、B(0)≠0，并除去固定 scaling 的有限 primes 后，它的整个无限 Laurent tail 均 p-integral。此 assertion 由 formal inverse B^−1 的整数递推得到，不止针对一个有限 prefix。

令 L(x)=−log(1−x)，定义真实 response

\[
 \mathcal H(x)=a_F(x)L(x)+a_s(x).
 \tag{S18}
\]

L 不在 C(x)，所以 a_F≠0 保证 H 非恒定。故其 Laurent expansion 有某个固定 t≠0 的 nonzero rational coefficient H_t。对所有充分大的 odd prime p，避开 H_t 的固定 numerator/denominator及上述 finite exceptions，在 N=p+t 有

\[
 \boxed{p^s[x^{p+t}]R\equiv\chi_4(p)\,H_t\pmod p\ne0,
 \qquad v_p[x^{p+t}]R=-s.}
 \tag{S19}
\]

证明需保留全部 infinite rational tails。记所有 a 的共同 Laurent lower bound 为 h*。convolution 中的正函数 index 至多 p+t−h*<p²，且在 p 充分大时小于2p。Ts 只有 index p 的系数具有 valuation −s，贡献 a_(s,t)χ4(p)。F 的 coefficient index m=p+k、k≥1，从 S7 的 inner index j=p 唯一得到该层；p^s F_(p+k)≡χ4(p)/k mod p。相乘后 k≤t−h*，总和准确等于 [x^t]a_FL。若 m=p，则 inner sum 不含p，outer denominator只给 valuation ≥−1，因 s≥2 不在最低层；其他 inner index 不含p。更低 T_j 的 valuation≥−j≥−s+1；a0 亦 p-integral。负 Laurent shifts 只改变固定 lower bound，不允许额外2p项。于是最低层恰为S18，不能被其余项取消。

单个预设 t 的最低层可能抵消，S18 是对此的完整修正。例如 R=F−xTs 在 t=1 的 response 消失，但 t=2 的 coefficient为1/2，给新的有效 witness；不能无条件重用 p+1。

设 R 经固定 integer scaling 后具有任何 CDT fixed type

\[
 [x^N]R=\frac{z_N}{N^e\prod_\ell D_{\lfloor b_\ell N+c_\ell\rfloor}},
 \quad z_N\in\mathbb Z,\quad e,b_\ell,c_\ell\text{ 全固定},
 \quad b_\ell\ge0.
 \tag{S20}
\]

p∤(p+t)，所以 N^e 不支付 S19 的任何 p 层；每个 fixed LCM factor 最终至多贡献一层p。若 b<1，该 factor 最终不含p；b≥1 才可能贡献。因此至少 s 个 b≥1 factors，给

\[
 \boxed{a_F\ne0\Longrightarrow\sigma(R)=\sum_\ell b_\ell\ge s,}
 \tag{S21}
\]

与任意固定 e 无关。prefix common denominator 亦满足 liminf(log δ_R(N))/N≥s，由除 finite primes 外的 p+t witnesses 和PNT得出；此 prefix 下界不是 τ 的定义。

任何实际 V_(s,u) 的 full Q(x) basis 至少含一行 a_F≠0，否则不能生成 quotient 的 F direction。CDT column-step array 给非降 σ_i；一行 σ≥s 至少迫最后一行≥s，全部其他 σ≥0，故任意此类 full basis

\[
 \boxed{\tau\ge\tau^\flat\ge
 \frac{s(2s+3)}{(s+2)^2}.}
 \tag{S22}
\]

此为真正 Q(x) 变基后的必要 bound，允许 poles与组合 cancellation。对 S6 同样把 H 换成 a a_F L+a_4；a≠0保证非恒定，其他 T2 项仅有更浅层，故 s4 的同一11/9成立。它不排除不同 carrier、子空间、Hadamard lift 或不同 monodromy-compatible map。

## 5. 同一对象的共同 map、精确 J 与可用范围

对0<ρ<1，取

\[
 \varphi_\rho(z)=\frac{2\rho z}{1-\rho^2z^2},\qquad
 |\varphi_\rho'(0)|=2\rho.
 \tag{S23}
\]

φ1 将unit disk conformally映到Dβ；边界 z=e^(it) 给 φ1=i/sin t，两个 boundary poles对应∞。φρ在closed disk邻域全纯，像紧含于Dβ。S5 下所有 S8 函数的实际 pullback 全盘全纯，既满足 canonical branches，也支付 x=1 的填入；不将任意 transported branch 自由当成此叶。

由 conformal inverse 和 Schwarz lemma，任何 holomorphic map到此 Dβ、0固定者的 derivative ≤2，包括该域内的 multivalent maps。此结论仅限定像在Dβ，未证明所有 possible meromorphic pullbacks 的像都必须在此 slit domain。单独说 φ omit±i 也不等于说其像在Dβ；更大映射必须处理 transported branches在0和1的额外门槛。

同一 S23 map 有完全准确的双边界积分。因

\[
 \varphi_\rho(z)-\varphi_\rho(w)=
 \frac{2\rho(z-w)(1+\rho^2zw)}
 {(1-\rho^2z^2)(1-\rho^2w^2)},
\]
\[
 \boxed{J(\varphi_\rho)=
 \iint_{\mathbb T^2}\log|\varphi_\rho(z)-\varphi_\rho(w)|d\mu(z)d\mu(w)
 =\log(2\rho).}
 \tag{S24}
\]

log|z−w|的可积 diagonal 奇性均值为0；其余 three factors 的 Jensen averages为0，因为ρ<1。没有数值 contour quadrature。若正分母条件成立，CDT的rank bound在此 map 成为 m≤L/(L−τ)，L=log(2ρ)；rank矛盾需要 τ<(1−1/m)L。

但 β4、β4−G/3 的任意 S8 full Q(x) basis已有

\[
 \tau\ge11/9>\log2,\qquad
 G\text{ 的对应 bound }7/8>\log2.
 \tag{S25}
\]

所以在此已证共同 canonical leaf 上，连 positive denominator 都没有。τsharp不会修复此缺口。这里 log2<7/10即可严格认证两比较，无浮点；它可由 log2=2Σk≥0 3^(−2k−1)/(2k+1) 的有限截断及几何尾界证明。本稿没有把它说成 β4 方法整体不可能、也没有把 β4 真值的未知无理性预先用来证明 rank。

η tower亦可用相同 suspension：

\[
 E_s(x)=-\operatorname{Li}_s(-x),\quad
 E_s(1)=\eta(s)=(1-2^{1-s})\zeta(s),
 \quad B_s^\eta=\int_0^x E_s(t)/(1-t)dt.
 \tag{S26}
\]

在 η(s)=u∈Q 下，Fη=Bη+u log(1−x) 填1，实际 rank=s+2，finite cap ND_(N−1)^s，S18–S22的witness以(−1)^(p−1)=1替χ4(p)，其他证明相同。canonical leaf是 C\(−∞,−1]，map 4ρz/(1−ρz)^2 的 derivative4ρ、J=log(4ρ)。到此leaf的任何0固定holomorphic map由conformal inverse/Schwarz有 |φ′(0)|≤4。

这里必须比较完整rank门槛，而不止positive denominator。对任何CDT允许的nonconstant φ，在closed unit disk邻域全纯，Jensen先对z、再对w给 J(φ)≥log|φ′(0)|=:L：固定w时 z↦φ(z)−φ(w) 的0点值为−φ(w)，而 w↦φ(w)/w 的0点值为φ′(0)。边界zero只增加可积log奇性；可先在半径<1上取Jensen再取极限。所以任何实际rank矛盾 m>J/(L−τ) 都必须满足 τ<L−J/m≤(1−1/m)L。令m=s+2，与S22合并，必须有

\[
 \frac{s(2s+3)}{(s+2)^2}
 <\frac{s+1}{s+2}\log4,
 \quad\text{即}\quad
 f(s):=\frac{s(2s+3)}{(s+1)(s+2)}<\log4.
\]

但 f′(s)=(3s²+8s+6)/(s²+3s+2)²>0，f(4)=22/15>7/5>log4，后一严格界由S25的log2<7/10。因此对所有整数s≥4，此实际η full space在标准leaf的任意上述map都无法给CDT rank矛盾；任意Q(x)full basis、任意固定N^e以及nonnegative τsharp均不能修复此项。ζ5虽有65/49<log4，却已经不满足完整rank门槛；ζ7的119/81>log4是更强的positive-denominator失败。此结论只限定S26载体和标准leaf，不排除不同period实现或更大的monodromy-compatible maps。它与root新的偶节点η determinant是不同的真实对象，不转移费用或实处界。

## 6. β4/G/ζ3 三周期的一个真正单关系载体

要允许跨 weight 的数值关系，取 a,b,c∈Q，a≠0、c≠0，并定义

\[
 \Psi=aT_4+bT_2+\frac{4c}{3}E_3,
 \quad\Psi(1)=a\beta(4)+bG+c\zeta(3)=:\vartheta,
\]
\[
 F_u(x)=\int_0^x\frac{\Psi(t)}{1-t}dt+u\log(1-x).
 \tag{S27}
\]

E3在x1是普通点，故 ϑ=u∈Q这一单关系完整填1；无须分别假设β4、G或ζ3有理。取负实ray和两imaginary rays之外的共同slit叶

\[
 \mathcal D_{\rm mix}=\mathcal D_\beta\cap
 (\mathbb C\setminus(-\infty,-1]).
 \tag{S28}
\]

其像包含原点，在单连通指定枝上 Ψ、F_u 全纯。Dmix是Dβ的子域，故到Dmix的0固定maps仍有derivative≤2。φρ未必全部落在Dmix，不能把S23免费当成此混合系统的有效map；例如足够小ρ满足max|φρ|<1时可用，但其尺度更小。下面失败判断只用任何此域map的upper≤2，不借无效pullback。

导数闭合实际函数组为

\[
 1,T_1,T_2,T_3,T_4,E_1,E_2,E_3,F_u.
 \tag{S29}
\]

绕i的S10迫Ti系数全零，因为E_j在此普通且不变；绕−1的 E_j jump=2πi(log(−x))^(j−1)/(j−1)!再迫E系数全零，证明前8项独立。针对F的S11 conjugate loop证明由最高aT4的nonzero polynomial保障，E3不改变此i jump；故实际rank精确9。全系统有显式rational first-order matrix：Tj'=T_(j−1)/x，Ej'=E_(j−1)/x，T0=x/(1+x²)，E0=x/(1+x)，F'=(Ψ−u)/(1−x)；holonomic不是猜测。

固定relation coefficients/u的清分母常数后，完全安全e0阵列排序为

\[
 \sigma=(0,1,1,2,2,3,3,4,5),\quad
 \tau_{\rm safe}=257/81.
 \tag{S30}
\]

更强的任意full basis必要bound仍来自最高T4：S18 response变成 a a_F L+a_4；E3仅有p^−3，不能取消p^−4层。m9因此有

\[
 \boxed{\tau\ge\tau^\flat\ge68/81>\log2.}
 \tag{S31}
\]

所以这些新的混合数值目标在同一canonical leaf上也未成功。S27–S31已经给完整单关系germ接口，能够在未来实际更大共同map或新的低费用carrier出现时直接比较；本稿不将目标数值LI、函数rank9及三个常数的形式维数混为一件事。

## 7. Ω 的真实有限空间 lift，以及不能消去的完整局部分支

既有 [边界求值稿 O4–O6](cdt_catalan_jet_boundary_evaluation_20261007.md) 定义 L_(3,1)(z,w)=Σ_(n>k≥1) z^n w^k/(n³k)。以下新lift只用该已证实际身份：

\[
 A(x)=\Re\bigl(\mathcal L_{3,1}(x,i)-\mathcal L_{3,1}(-x,i)\bigr),
 \quad B(x)=\mathcal L_{3,1}(x,-1)-\mathcal L_{3,1}(-x,1),
\]
\[
 \boxed{\Psi_\Omega(x)=\frac{195}{64}\operatorname{Li}_4(x)
 -\frac{91}{96}\operatorname{Li}_3(x)\log(1+x)
 -\frac43A(x)+\frac18B(x).}
 \tag{S32}
\]

Re在这里是对Taylor coefficients的真实conjugate pairing，给全纯实系数函数，不是对任意复x取非holomorphic Re。各series在unit disk绝对收敛；在实x↑1，MPL的absolute convergence和经典endpoint值给 ΨΩ(1)=Ω。产品log(1+x)的endpoint准确是log2，避免在Q-Taylor coefficients中人为放入log2。

对上述双参数约定直接求θ三次：θ³L_(3,1)(z,w)=−z log(1−wz)/(1−z)。于是

\[
 \theta^3A=-\frac{x}{1-x^2}\log(1+x^2),
 \qquad\theta^3B=-\frac{2x}{1-x^2}\log(1+x).
 \tag{S33}
\]

这是实际ODE，非参数z的无限极点function。全系统由以下16个实际Q-Taylor functions给一个closed rational differential space：

\[
 1;\quad \operatorname{Li}_1(x),\ldots,\operatorname{Li}_4(x);
 \quad L=\log(1+x),\ M=\log(1+x^2);
\]
\[
 \operatorname{Li}_1L,\operatorname{Li}_2L,\operatorname{Li}_3L;
 \quad A,\theta A,\theta^2A;
 \quad B,\theta B,\theta^2B.
 \tag{S34}
\]

S33及标准导数链给全部matrix coefficients在Q(x)。本稿仅证明rank≤16，没有证明这些16项独立。按各显式convolution的denominator，192D_N^4清全部 ΨΩ coefficients；S34全组可用相同fixed scaling的D_N^4 cap。产品Li3·L的一项k^3j均由D_N^4支付；MPL的n³k亦如此。为ΨΩ作一次suspension会另增N，须付ND_(N−1)^4，不免费。

**S35（单Ω关系填1的真实障碍）。** 写h=x−1，在1附近选择从0<x<1来的log(1−x)。S33的simple-pole leading terms为

\[
 \theta^3A=\frac{\log2}{2h}+O(1),\quad
 \theta^3B=\frac{\log2}{h}+O(1),\quad
 \theta^3\operatorname{Li}_3=-\frac1h+O(1).
\]

因∂³(h²log(−h))=2/h，θ³与∂³在leading pole处相同，三式分别给 nonanalytic coefficients (log2)/4、(log2)/2、−1/2。Li4从h³log起；L在1全纯且L(1)=log2。因此S32的完整local展开中

\[
 \Psi_\Omega(x)=H(x)+\frac{13}{64}\log2\ h^2\log(1-x)
 +O(h^3\log(1-x)),
 \quad H\text{ 在1全纯},\ H(1)=\Omega.
 \tag{S35}
\]

准确系数是 91/192−1/3+1/16=13/64；不是数值拟合。每个simple-pole的重复积分具有 analytic function乘log的local形状，所以该nonzero coefficient已足以证明非meromorphic。

若仿照S3令 FΩ,u=∫0^x ΨΩ(t)/(1−t)dt+u log(1−x)，即使Ω=u∈Q，constant log确取消，但F'= (ΨΩ−Ω)/(1−x)仍含−(13/64)log2·h log(−h)，从而FΩ,u保留

\[
 -\frac{13}{128}\log2\ h^2\log(1-x).
 \tag{S36}
\]

该项非零，所以仍未填1。有限ramification h=c(z−z0)^k(1+O(z−z0))留下nonzero (z−z0)^(2k)log(z−z0)，也不能使它成为meromorphic。S32–S36是新实际finite-space识别和完整germ反证，不是Ω数值无理性、与β4独立性或所有其他carrier的否证。它指出O6这一个endpoint身份尚不足以给CDT需要的全分支消去。

## 8. 实际取消方向与一个新的项目目标 Θ

root指出S33中还存在一个与单Ω残留不同的真实取消方向。定义

\[
 D(x)=A(x)-\frac12B(x),\qquad
 R(x)=\log\frac{1+x^2}{1+x},\qquad
 \theta^3D=-\frac{x}{1-x^2}R(x).
 \tag{S37}
\]

R指从0正规化为0的log(1+x²)−log(1+x)芽及其延拓，ratio log按这一枝解释，不能在每个复x重新取quotient的principal value。R在x=1的指定枝真正全纯，R(1)=0，所以右侧的全部pole可去。随后三次θ逆积分的系数1/x在1普通，迫此canonical D的完整germ全纯穿过1；不是只消去一个h²log coefficient。全first-order system仍可能有该点的非平凡transported branches，本文只填所指原枝。D(0)=θD(0)=θ²D(0)=0，S37还直接给

\[
 D(x)=-\frac12\int_0^x\log^2(x/t)
 \frac{R(t)}{1-t^2}\,dt\quad(0<x\le1),
\]
\[
 \boxed{\Theta:=A(1)-\frac12B(1)=
 -\frac12\int_0^1\log^2t
 \frac{\log((1+t^2)/(1+t))}{1-t^2}\,dt>0.}
 \tag{S38}
\]

这是实际level-four深度二period组合。R(t)<0于0<t<1，R(t)=O(t)于0、R(t)/(1−t²)在1可去，故积分绝对收敛且严格为正。三次Euler积分的kernel准确是log²(x/t)/2，S38没有额外factorial或端点常数。既有O6相应准确改写为 Ω=195ζ(4)/64−91ζ(3)log2/96−4Θ/3−13B(1)/24，未假设这些值独立或属于某个更小period基。

R'=2x/(1+x²)−1/(1+x)是rational，故

\[
 1,R,\theta^2D,\theta D,D
 \tag{S39}
\]

是实际Q-Taylor的closed rational differential generating system，rank≤5。具体(θ²D)'=−R/(1−x²)、(θD)'=θ²D/x、D'=θD/x；在0各显示分母均由实际Taylor零阶支付。在Dmix上，R的principal logarithms全纯，S37在1可去，三次Euler原函数使原D及θjets在全域单值全纯。

进一步取

\[
 F_{\Theta,u}(x)=\int_0^x\frac{D(t)}{1-t}\,dt+u\log(1-x),
 \qquad F_{\Theta,u}'=\frac{D-u}{1-x}.
 \tag{S40}
\]

仅Θ=u∈Q这一关系给FΘ,u∈Q[[x]]并完整消去1的log分支；依S38，u=Θ>0，且D(0)=0，所以此F不是零函数。六项候选closed system为S39加F，actual rank≤6，尚未独立证明rank=5或6。

完整finite cap可从S32的双和直接核：A和B的nth coefficient为rational colors/(n³k)、k<n；对B/2，color ((−1)^k−(−1)^n)/2仍为整数。故D_N^4支付D，D_N^3支付θD、D_N^2支付θ²D，D_N支付R；192是同时保留全部旧normalization的安全fixed scaling。S40的Nth coefficient为(Σ_(j<N)[x^j]D−u)/N，所以正式系数型为192 N D_(N−1)^4[x^N]F∈Z[u]；在仅Θ=u∈Q的hypothesis下，还需一次固定整数d使du∈Z，得到192d N D_(N−1)^4[x^N]F∈Z。不能以192 alone免费支付任意u的分母。吸收N后候选array的safe e0 row sums仍为(0,1,2,3,4,5)，尚不能把候选六行当成已证独立六行来用CDT。

Θ是本项目真实的新研究目标，不称全球首次出现的常数或新的无理性定理。此方向已经有full-germ消去、Q-Taylor/holonomic表示、正积分与完整finite cap；还缺实际独立rank、同一对象更佳的共同map/J和够用的算术解析差额。它没有自动消去原Catalan full pool其余seed、继承原nonzero certificate或改变S35的单Ω残留结论。

## 9. 进展、primary 文献与实际审计范围

本轮已证S1–S25的单β/混合β germ、真实rank、完整finite cap、rational-basisprime response和标准叶精确J；S26给η/奇ζ的同构接口及准确费用范围；S27–S31给真正跨weight单关系和rank9；S32–S36把Ω变成16维空间system，并定位单Ω关系剩余的nonzero log分支；S37–S40给实际取消方向Θ的完整germ、正period、rank上界与全finite cap。没有新无理性、LI或Lean结论。

下一项有明确可验证的数学目标：对已构造S8/S29，提供更大的、对全部transported germs都meromorphic的共同map并计算同一J；或者构造费用低于S21的不同真实carrier；对S39/S40另需首先证明真实独立rank。仅缩放x、去掉τsharp、增加重复导数、把Ω的一个点值当成全local germ、或继承β sec determinant旧常数，均不能填本稿已明确的缺口。本稿只为这些具体carrier给接口，不把它列成ζ/L研究的整体不可能性。

primary浏览实际打开 [NIST DLMF 25.12](https://dlmf.nist.gov/25.12)、[NIST DLMF 4.23](https://dlmf.nist.gov/4.23)、[CDT 2510.04156v1 §2.1–2.2](https://arxiv.org/html/2510.04156v1#S2)、[Panzer 1403.3385 abstract](https://arxiv.org/abs/1403.3385)。DLMF提供classicalseries/branch背景；CDT网页Theorem2.1和Remark2.5明确完整LCM阶梯、holonomic、共同meromorphic pullback、正门槛及额外N^e费用。本稿应用的S14–S15是其e0有效输入，S16/S22/S31不免费删除e项。Panzer摘要仅作为hyperlogarithm工作背景，不引用未读algorithm正文或independence定理，全部本稿身份和rank自行证明。

本轮在 `literature/cdt_weight4_space_germ_sources_20261007/` 保存DLMF4.23、CDT上述v1 HTML、Panzer摘要HTML与 `receipt.json`，记录URL/bytes/SHA256。既有DLMF25.12来源已在literature，不再次下载。新PDF读取0页，新PDF下载0，没有声称完整阅读Panzer或CDT全文。

输入实际FULL阅读：higher-jet稿八节H1–H30；Ω边界求值稿七节O1–O26；rational-polylog-cap稿六节R1–R17；period_holonomy_cdt_mechanism稿七节及完整账本。其余仅rg索引去重，不计为全文。没有执行旧数学脚本、prime扩表、PSLQ、浮点拟合或Lean。

一段全新内联Fraction小样本：p=7,11,13,17，u=2，准确检查F4在p+1的valuation−4；F4−xT4在p+1先抵消至−3、在p+2重新为−4；β4−G/3的F在p+1为−4；另精确核13/64、125/36、257/81、11/9、68/81。该finite certificate仅核例子与付款分数，S19/S21的全prime证明仍是上述纸证，不能由样本外推。网页保存的download脚本不是数学producer。

作者已实际全文回读原八节/S1–S36，并修正固定清分母整数 d 与关系系数 b 的记号冲突、目标 ϑ 的字形。root随后实际FULL读取八节/S1–S36，并独立重推S10monodromy tower、S11pure F conjugate translation、S19infinite rational tail/fixed t response、LCM必要bound、S24精确J、mixedrank9、S33–S36nonzero Ω log，数学PASS无实质修正。root同时指出S26可用完整rank门槛加强及S37–S40的Θ方向；作者已补独立纸证。root随后另实际读取S26新增完整段与S37–S40全文，独立重推两遍Jensen J≥L、f导数/22/15严格界，D的准确source取消与原枝1全germ、三次Euler的1/2 kernel和正积分、R导数与0-removable closed space、rank仅upper、du固定scaling及safe arrays，补审数学PASS。作者已最后实际FULL回读九节/S1–S40，并补R的ratio log枝约定；本次新增段的PASS来自明确的写后审阅，没有把此前八节审阅外推。所有纸面证明和Fraction有限证书不称形式化验证。
