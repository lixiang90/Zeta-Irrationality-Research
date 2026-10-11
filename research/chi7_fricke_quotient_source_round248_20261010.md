# 第248轮：χ−7 Fricke 商的实际 Hauptmodul 与二阶有理 forcing

2026-10-10，A。本文支付一个真正的 genus-zero 商坐标、完整 divisor/character、有限公式定义的二阶方程及实际三行秩。所有推导为纸证，数学程序 0。没有支付全部 transported leaves、数域全部嵌入的关系补点或严格 CDT 预算，没有新的数值无理性/线性无关性定理。

## 1. 固定数值响应与一个真正的商坐标

实际全文复用 A247、Root mixed247、C247 的冻结终稿。置 χ=χ−7、s=√2、K=Q(s)、q=e^{2πiτ}、Θ=q∂q、ηδ=η(δτ)，A₁=A(τ)、A₂=A(2τ)、δu=u∂u。原 level7 身份为
\[
u=(\eta_7/\eta_1)^4,\quad P(u)=1+13u+49u^2,\quad
f_1=\eta_1^3\eta_7^3=uA_1^3/P(u),\quad \Theta\log u=A_1^2,
\]
\[
\delta_u^2A_1=V(u)A_1,\qquad
V(u)=2u(1+16u+49u^2)/P(u)^2 .                 \tag{Q1}
\]
实际 primitive 及响应为
\[
I_\pm=R\pm(2s/7)D,\quad h_\pm=\Theta^2I_\pm,
\quad g_\pm=Y/2\pm s\pi^2/28,\quad Y=L(2,\chi).
\]
A247 已证明全函数 Fricke 身份
\[
A_\pm(W_{14}\tau)=\mp i\sqrt{14}\tau A_\pm(\tau),\qquad
I_\pm(W_{14}\tau)-g_\pm
=\frac{\pm i}{\sqrt{14}\tau}(I_\pm(\tau)-g_\pm),
\quad A_\pm=A_1\pm sA_2.                         \tag{Q2}
\]
以下只主写加号，减号为代数系数共轭。

定义
\[
\boxed{t=(\eta_1\eta_{14}/(\eta_2\eta_7))^4
=q\prod_{j\ge1}\frac{(1+q^{7j})^4}{(1+q^j)^4}.} \tag{Q3}
\]
eta 指数按 1、2、7、14 为 (4,−4,−4,4)，weight0，两 congruence sums 均为24，字符参数 ∏δ^{rδ}=1。完整 eta statement 因而给 trivial character 与 cusp orders
\[
\begin{array}{c|rrrr} \text{cusp}&\infty&0&1/2&1/7\\\hline
\operatorname{ord}(t)&1&1&-1&-1
\end{array} .                                      \tag{Q4}
\]
主平方根 eta S 变换直接给 t(W₁₄τ)=t(τ)。W₁₄ 交换前两个及后两个 cusp，非恒等；t 在 X₀(14) 上 degree2，故经 degree2 商后的 t 恰 degree1。于是
\[
\boxed{X_0(14)/\langle W_{14}\rangle\simeq\mathbf P^1_t}
\]
且此商在 Q 上有定义。另由 index24、cusps4、无 order2/3 elliptic points，genus formula 给 g(X₀(14))=1。式(Q4)同时证明旧 Z+1/(8Z) 的两个 quotient poles 不能给 degree-one 坐标。本式不是将该旧 invariant 改名为 Hauptmodul。

## 2. 实际 period 零点与 degree-two 曲线

令 f₁₄=η₁η₂η₇η₁₄。其 weight2、character trivial，H 中无零，四个 cusps orders 都为1；f₁₄(Wτ)=−14τ²f₁₄。A₁、A₂ 均为 Γ₀(14) 的 holomorphic weight1、χ(d) 形式，矩阵 (a,2b;c/2,d) 支付第二项字符。A±²/f₁₄ 是 Γ₀(14) 与 W 的 invariant；其 H 无 pole，商上仅 t=0、∞ 至多 simple poles。因此先有 Laurent degree bound，再比较三个头项，得到全函数身份
\[
a_\pm=3\pm2s,\quad Q_\pm(t)=1-(7\mp4s)t+t^2,
\qquad \boxed{A_\pm^2/f_{14}=a_\pm Q_\pm(t)/t.} \tag{Q5}
\]
例如 A₁=1+2q+4q²+…、A₂=1+2q²+…、f₁₄=q−q²−2q³+…，以及
t⁻¹=q⁻¹+4+10q+…，加号比值为
(3+2s)q⁻¹+(7+6s)+(33+22s)q+…，唯一给 (Q5)。有限头仅决定已付三维空间的系数，不是猜测全身份。

Q± 各有两个 simple roots，discriminants 为 77∓56s≠0，四根互异。在任一这样的点 f₁₄≠0，A± 全纯，而其平方在商坐标有 simple zero。因此 degree2 的 t-map 必 ramify；四点即 Riemann–Hurwitz 所容许的全部 ramification，且 A+ 在 Q+ 两点各有一个 simple zero，A− 同理。这个零点账保留实际字符；没有将 weight1 形式当成单值 scalar function。

定义 y=Θt/f₁₄，native y(0)=1。它是 Γ₀(14) weight-zero function，W 下 anti；在两 poles 的 y 有 order2 poles，无其它 pole，且在四个 branchpoints simple zeros。故
\[
\boxed{y^2=E(t)=Q_+Q_-=1-14t+19t^2-14t^3+t^4.} \tag{Q6}
\]
constant term1 固定倍数。由 y anti、t degree2 可得完整函数域 Q(X₀(14))=Q(t,y)。令
\[
Q_0=t^2-t+1,\quad Q_A=3t^2-5t+3,\quad
T=t^3-8t^2-8t+1 .
\]
(Q5) 加减及 native sign 给
\[
A_1A_2/f_{14}=Q_0/t,\quad
(A_1^2-2A_2^2)/f_{14}=-y/t,\quad
A_1^2/f_{14}=(Q_A-y)/(2t),\quad
\rho=A_2/A_1=2Q_0/(Q_A-y).                         \tag{Q7}
\]
第二式的平方由 Q_A²−8Q₀²=E 固定，native 首项给负号。

以下公式把原 forcing 全部放到这一显式 quadratic field，避免只声称代数存在：
\[
\boxed{u=\frac{T+(t-1)y}{98t^2},\quad v=u(2\tau)=ut,\quad
Z=f_1(2\tau)/f_1(\tau)
=\frac{8t^3P(u)^2}{u^2(Q_A-y)^3}.}                 \tag{Q8}
\]
验证 u 的有限证书为
T²−(t−1)²E=196t³ 及
\[
\delta\log u=(Q_A-y)/(2y),\qquad\delta=t\partial_t,
\quad u=t+8t^2+\cdots .                            \tag{Q9}
\]
微分恒等式将 δy=tE′/(2y) 代入即可逐项核定；原 Θlogu=A₁² 和 (Q7) 给相同微分式及 native leading，因此 (Q8) 是实际 u。v=ut 是 eta product 恒等式；Z 式由 f₁₄³=f₁f₁(2τ) 和 (Q1) 得出。

特别要保留
\[
G_0=\Theta\log t=f_{14}y/t,\qquad
G_0/A_+^2=y/(a_+Q_+).                              \tag{Q10}
\]
右边 W-anti，不能直接冒认 K(t) 的 rational function。

## 3. 有限公式定义的实际二阶方程与 forcing

取 d=(Q_A−y)/(2y)、k=1+sρ、ℓ=δk/k。A+=kA₁。拉回 (Q1) 并作这个实际 gauge 得
\[
\mathcal L_+=\delta^2+p_1\delta+p_0,\qquad
p_1=-\delta\log Q_++\tfrac12\delta\log E,
\]
\[
\boxed{p_0=-d^2V(u)+(\delta d/d)\ell+\ell^2-\delta\ell.} \tag{Q11}
\]
式中 u、ρ、δy 都已经由 (Q6)–(Q9) 给出，所以这是有界代数运算的 exact certificate，不是经验猜递推或待计算的 operator。直接 gauge 的一次项是 −δlogd−2ℓ；它等于显示的 p₁，因为两齐次解 A+、τA+ 的 δ-Wronskian 为
\[
\mathcal W=A_+^2\delta\tau=a_+Q_+/(2\pi i y).
\]

这些两个实际解在 Γ₀(14) 及 W 下通过常数 2×2 矩阵返回：Γ 下来自 χ(d)(cτ+d)，W 下来自 (Q2)。故唯一 monic 二阶方程 invariant，(Q11) 的 p₀ 在 y↦−y 下固定。因此 p₀∈K(t)；若需只使用 rational operations 的表达，可用 (p₀(t,y)+p₀(t,−y))/2，再用 y²=E 消去 y。这个 involution 证明先于取 trace，不能以取 trace 强行改变方程。

置 κ=2s/7，并定义实际 rational-field expression
\[
\mathcal H=(1+8u)-8Z(1+8ut)
+\kappa[-7-8/(7u)+Z(7+8/(7ut))].                    \tag{Q12}
\]
A247 的全模驱动身份给 h+=f₁𝓗。对 B_g=A+(I+−g)，g 为任一常数，乘积微分的交叉项由 p₁=δlogG₀−2δlogA+ 完整相消。因此
\[
\boxed{\mathcal L_+B_g=\mathcal R_+(t),\qquad
\mathcal R_+=\frac{u(Q_A-y)(Q_A-y+2sQ_0)}{4P(u)E(t)}\mathcal H.} \tag{Q13}
\]
原式为 A+h+/G₀²。h+ 的 W factor 是 +14i√14τ³，与 A+³ 相同；乘 A+、除 G₀² 后因子恰1。Γ 字符亦 χ²=1。因此 (Q13) 在 y↦−y 下固定，属于 K(t)，可按 (Q11) 同一有限 trace 规则完全 rationalize。native 𝓡+=(1+s)(1+κ)t+O(t²)≠0。g 不改变 forcing。已付的是 actual differential equation；无需、也没有声称 B_g 在整个 modular group 下 invariant。

## 4. 全 Γ Eichler cocycle、实际 rank3 与非恢复

对 γ=(a b;c d)∈Γ₀(14)，令
\[
P_\gamma(\tau)=\chi(d)^{-1}(c\tau+d)I_+(\gamma\tau)-I_+(\tau).
\]
Bol 的两次链式微分直接给 Pγ″=0，因为 Θ²I+=h+ 的 weight3、χ 变换已经付清。因此 Pγ=αγτ+βγ，是由实际 primitive 唯一决定的 affine polynomial；并有完整函数身份
\[
B_0(\gamma\tau)=B_0(\tau)+A_+(\tau)P_\gamma(\tau). \tag{Q14}
\]
对 B_g，右边再加 g[A+(τ)−A+(γτ)]，仍在 homogeneous solution span。式(Q14)不宣称 αγ、βγ 都零，更不从一个 W identity 推出全部 Γ 返回无 jump。γ 返回可选择避开有限 elliptic/zero/pole orbit 的实际路径；矩阵返回与上述原函数 identity 相符。

T=(1 1;0 1)、U₁₄=(1 0;14 1) 在 Γ₀(14)，χ(d)=1，作用于 A+、τA+ 给两个没有共同 invariant line 的上下 unipotents。因此 𝓛+ 在 C(t)[δ] 不可约，齐次实际 derivative module rank2。

另一方面，在 cusp1/2、q=−e⁻ᵃ，已有完整 regular-singular 展开给
R∼−7L(3,χ)/(8a)、D→π²/8、A₁∼π/(√7a)。A₂ 由 q²=e⁻²ᵃ 及 level7 Fricke 给同一 leading π/(√7a)。故对每个固定 g∈C，
\[
B_g\sim-\frac{7\pi(1+s)}{8\sqrt7}L(3,\chi)a^{-2}\ne0. \tag{Q15}
\]
该 cusp 在 t=∞ 有 simple pole，故 a⁻² 是非零 log² 层。t-rational functions 是 local Laurent powers，不能有此 log²；齐次 period 解至多一级 log。由 (Q13)，
V=C(t)+C(t)B_g+C(t)δB_g 微分稳定，V/C(t) 是非零、被不可约 𝓛+ 杀的 cyclic quotient，因此
\[
\boxed{(1,B_g,\delta B_g)\text{ 对 }C(t)\text{ 实际独立，rank=3}.} \tag{Q16}
\]
它不依赖 g 是否是数值目标。还可证 A+∉V：其简单二维 module 与 C(t) 交为0（A+ 有实际 log）。若它包含于 V，维数迫 V=C(t)⊕M_A。微分稳定投影写 B_g=r+z，则 𝓛+z=0、𝓛+r=𝓡+；齐次 z 至多 log，r 亚纯，不能产生 (Q15) 的 log²。这个非恢复结论针对同一个完整三行源，不是一般方法的先决假设或 no-go。

## 5. 全 prefix、共轭 response 与首个真实准入关

(Q3) 为 qZ[[q]] 首项1，其逆 q(t) 在 tZ[[t]]；A₁、A₂ 整数级数。A247 的 d_N² 全 prefix 清除 R、D，故对 g∈K、固定正整数 b 使 bg∈O_K=Z[s]，
\[
7b\,d_N^2[t^j]B_g\in O_K\quad(0\le j\le N),
\qquad [t^j]A_+\in O_K.                           \tag{Q17}
\]
同一清分母适用于任意固定 δ-jet；普通完整 ∂t-jets 必保留 shifted cutoff。固定7来自 κ，固定 b 不能遗失。所有 primes/powers 都包括；安全 prefix 不是 primitive 内容、joint degree-D 格或全数域净费用。有限 forcing 与正收敛半径已经付，未因数域有两个 real places 免费放弃另一 place。

代数共轭将本源变为
\[
\sigma(B_g)=A_-\bigl(I_--\sigma(g)\bigr),\qquad
Q_+\mapsto Q_-,\quad a_+\mapsto a_- .             \tag{Q18}
\]
这里是 **系数共轭后的实际解析函数**，不是对未知实周期任意施加 field automorphism。目标 g+=Y/2+sπ²/28 属于 K 的假设，只有 g=g+；它不付 σ(g)=g−。如果两个指定 canonical cusp 返叶都用 (Q2) 补点，则必须同时有 g=g+、σ(g)=g−，从而
\[
\pi^2=(14/s)(g-\sigma(g))\in\overline{\mathbb Q},
\]
与 π² 的 transcendence 矛盾。这只禁止把单 embedding 假设偷换成双方免费补点；不禁止另一 place 使用其它合法图，也不声称已经排除 g+∈K。

本轮实际进展是：一个 Q-Hauptmodul、完整 branch/character 与 K(t) rank3、非恢复、二阶 rational forcing 及全 prefix；它改变了旧 degree-three algebraic forcing 的 source species。首关必须针对此新坐标、原目标 g+ 及实际共轭分别给共同合法拉回/全部返回叶，并同对象比较有限处与实处费用。旧 genus1 坐标 cap 不能直接搬到 t，也不能只凭商 genus0 宣称有正容量。到此停止，不开始图、素数或参数扫描。

## 6. 实际读域与来源边界

本轮实际 FULL 读 A247 9308 B/SHA256 ed85200e7b75f24d0f7e7ffa523ba16a3196fd199012657567e15f8d90d04017，Root mixed247 6993 B/15605545624b79b8f6b692d7c4451ec949daee3f349f6dac14876f58a243043f，C247 12786 B/2cc22522b952f4b9c6587c9ebdf0e25d4a2a078afcf6221ff8dbf6f9b8c6079c；并实际完整读存件 Loeffler PDF3–5、8–10 的所选文本，以及 Darmon 等 PDF14 eta-units statement 与 Magma eta-products 选段。前者用于曲线/degree/genus 一般条件，后两者仅作为已存 standard statement 校对；未冒称原著全文或重新证明一般模性定理。

本轮新增一手保存 Arnold-Roksandich–James–Keaton，*Counting eta-quotients of prime level*, Involve11(2018)827–844，DOI10.2140/involve.2018.11.827，[出版社 PDF](https://msp.org/involve/2018/11-5/involve-v11-n5-p08-p.pdf)。完整实际读物理 PDF11（印页835）的 Theorems2.4/2.5，采用其明确转载的 Ono standard eta-character/cusp-order statements；不冒称阅读上游 Ono 证明或本论文其余全部页。有限检索不能证明新颖性。新下载仅此1PDF；pdftotext 仅提取所读页，不是数学执行。具体文件身份见同目录 alternative_reading_scope.md。

数学程序/CAS/数值/prime/parameter/map/Lean执行0，外 Git mutation0；旧稿/Root稿/同伴稿/main/manifest/policy写入0。本文与本人来源记录保存后实际 FULL 作者自读，再登记 final bytes/SHA。
