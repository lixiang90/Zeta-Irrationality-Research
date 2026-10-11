# Level 7 的低成本新周期族：普通点全跳跃、正 Stieltjes 比较与两类矩递推

日期：2026-10-07。作者：`/root`。本轮只读 authority 为 `cdt_odd_delivery_real_gates_kummer_cauchy_extensions_20261007.json`，SHA `7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a`；620 frozen（615 mathematical、5 guards）均不得修改或运行。本文是纯纸证，数学 producer 创建／执行／导入／重跑、prime 扩表、guard 与 Lean 均0。

本文构造无限个真正新 Green 扩张，给它们同一全素数 `D_n²` 整模型及完整的 σ 连接常数。同时证明每个新增普通点都是所有访问分支都无法填掉的真实对数奇点。周期族有正 Stieltjes 表示，而其多项式矩全部落在 `Q+Qκ+QC₃`，并满足一个精确全阶递推。这些是新的函数／周期结构结果，尚不是新数值无理性或线性无关性定理。

## 1. 实际模型与一族新增 rational forcing

固定已审 [多项式两类主稿](cdt_odd_level7_polynomial_extension_classes_20261007.md) E1–E29 和 [完整旧域分类](cdt_odd_level7_kummer_relative_classification_20261007.md) K1–K27 的同一 normalization：

\[
 \theta=t\partial_t,\quad p=(1-t)^2(1-28t),\quad
 L=p\theta^2-14t(1-t)^2\theta-(2t+4t^2),\quad
 r_B=t(1-t),\quad \sigma=1/28.                         \tag{P1}
\]

`A(0)=1, LA=0`；`B(0)=0, LB=r_B`；`B₃(0)=0, LB₃=t³`。`κ=L(η³η(7·)³,2)`，`C₃` 是前稿给出的真实正路径周期。齐次 germ 空间 `V` 二维，其 connected monodromy closure 为 `SL₂`；ordinary Wronskian为 `1/(t√(1−28t))`。没有更换坐标、周期标签或 Betti normalization。

对任意整数 `a≥1` 定义

\[
 R_a(t)=\frac{t(1-t)}{1+at},\qquad
 LB_a=R_a,\quad B_a(0)=0,\qquad \mu_a=-1/a.             \tag{P2}
\]

0 的 analytic Frobenius recurrence逐项给唯一 `B_a∈tQ[[t]]`。在其它 ordinary 点通过真实方程解析延拓；以下所有 jumps 都指这些 germs，而不是只比较一个数值极限。

## 2. 同一整数坐标支付所有素数及固定 jets

复用 Yang fixed v1 的实际 modular 参数

\[
 r=(\eta(\tau)/\eta(7\tau))^4,\quad t=r/(r+7)^2,
 \quad q=e^{2\pi i\tau},\quad
 S=q t_q/t\in1+qZ[[q]],\quad A\in1+qZ[[q]].             \tag{P3}
\]

整数 `t=q+…∈qZ[[q]]` 的 inverse `q(t)` 也为整数。Yang variation of constants 在非 monic `L` 上必须除以 `p`，给

\[
 f_a(q)=\frac{R_a(t(q))S(q)^2}{p(t(q))A(q)}
       =\frac{f(q)}{1+a t(q)},\qquad f=\eta^3\eta(7\cdot)^3,
 \quad B_a(t(q))=A(q)\sum_{n\ge1}\frac{[q^n]f_a}{n^2}q^n.
                                                               \tag{P4}
\]

等式右边使用已审 `r_B S²/(pA)=f`。`1+a t(q)` 是整数 unit，所有其它分母也是整数 unit，故 `f_a∈qZ[[q]]`。对一个 fixed Taylor index `n`，P4 的所有贡献只使用 `j≤n`，`j²|D_n²`；composition 和整数 multiplication 不增分母。因此

\[
 D_n^2[t^n]B_a\in Z,\qquad
 D_n^2[t^n]\theta^jB_a\in Z\quad(j\text{ fixed},\ n\ge1).
                                                               \tag{P5}
\]

这是全 `n`、全 primes/powers 证明。不是小样本，也没有将 `1/(2−t)` 那种非整数 unit rational gauge 免费纳入本整模型。有限多个整数 `a` 与 fixed rational linear combinations 共用一个 fixed multiplier。

## 3. 正路径积分给完整 σ 连接常数

在 imaginary axis 上 `f(iy)>0`，`0<t(iy)≤σ`。Fricke `wτ=−1/(7τ)` 满足 `t(wτ)=t(τ)`，且 `f_a(wτ)=i7^(3/2)τ³ f_a(τ)`；`f_a` 在两端具有 cusp decay。分母 `1+a t` 沿该路径非零，也在每个路径点的复邻域非零。定义真实 convergent constant

\[
 C_a=4\pi^2\int_0^\infty y\frac{f(iy)}{1+a t(iy)}\,dy.
                                                               \tag{P6}
\]

令 `E_a=B_a/A`。P4 给 `E_a''(τ)=−4π² f_a(τ)`；归一化为 cusp i∞ 处 `E_a,E_a'→0`。与前稿 E12–E19 同一 Fricke primitive 计算适用：只用 imaginary axis 及其邻域上的 holomorphicity、两端 decay 与 Fricke 变换，没有声称 `f_a` 在整个 H pole-free。写 `j=−i√7τ`，得到

\[
 j(E_a\circ w-C_a)=E_a-C_a.                              \tag{P7}
\]

`A(wτ)=j A(τ)`，所以 `B_a−C_a A` 在 Fricke fixed point 附近 invariant。实际 `t−σ` 是这里的二次 quotient parameter，故下降成完整 analytic t-germ：

\[
 B_a-C_a A\text{ analytic at }\sigma,\qquad
 \Delta_\sigma B_a=C_a\Delta_\sigma A.                    \tag{P8}
\]

P8是整个 germ 的跳跃关系，不能把它解读成所有 transported σ accesses 都填好。在0选的实际沿正轴 access下，假设 `C_a=u∈Q` 才会让 `B_a−uA` 填这个 σ germ。

## 4. 新普通点的全分支对数不能被常数投影填掉

ordinary 写法 `L=p₂∂²+p₁∂+p₀`，其中 `p₂=t²(1−t)²(1−28t)`。在 `µ=µ_a`，

\[
 \operatorname{Res}_\mu R_a=-\frac{a+1}{a^3},\qquad
 p_2(\mu)=\frac{(a+1)^2(a+28)}{a^5},\qquad
 \gamma_a=-\frac{a^2}{(a+1)(a+28)}\ne0.                  \tag{P9}
\]

取唯一 homogeneous solution `v_µ` 满足 `v_µ(µ)=0,v_µ'(µ)=1`。令 `s=t−µ`，直接交换子计算

\[
 L(v_\mu\log s)=2p_2v_\mu'/s-p_2v_\mu/s^2+p_1v_\mu/s,
 \qquad \operatorname{Res}_\mu L(v_\mu\log s)=p_2(\mu).
                                                               \tag{P10}
\]

其它 terms holomorphic，因为 `v_µ=s+O(s²)`，而 `Lv_µ=0`。减去 P9 的倍数后 RHS holomorphic；ordinary inhomogeneous equation 有 analytic particular。因此**每一个** local branch 恰有

\[
 B_a=\gamma_a v_\mu\log(t-\mu)+\text{analytic},\qquad
 (T_\mu-I)B_a=2\pi i\gamma_a v_\mu\ne0.                 \tag{P11}
\]

不同 branches 之差 homogeneous，在这个 ordinary 点 analytic，故不能改变该 coefficient。`A`、旧 `B`、`B₃` 及任何 rational meromorphic gauge 都无此 local jump。于是任意 `u∈C` 也有 `(T_µ−I)(B_a−uA)=2πiγ_a v_µ`。这比只证明某个 transported branch 不填更强，但范围只限本新增普通点。

有限 cover `s=z^k` 下变成 `kγ_a v_µ(z^k)log z`；其 coefficient虽在 z=0 消失有限阶，仍不是 meromorphic germ。没有 finite ramification 或 rational scalar projection 可以把这个完整 log 当成已填点。

在原1、∞，`R_a` 不引入新 ordinary pole。1处 local particular analytic，齐次 exponents `(1/3,2/3)`；∞以 z=1/t 看，`z³R_a=O(z²)`，不遇0-exponent resonance，local particular无 log，齐次 exponents `(0,1/2)`。因此这些 finite-order gates 可以在相应3／2 cover上处理，但所有原0及σ accesses和新增µ仍需逐一支付。此处不提供完整全局 CDT map。

## 5. 全旧域逃逸与任意有限族的实际 rank

若 rational `T` 在 ordinary µ 有 pole order k≥1，`LT` 的 leading pole order是 k+2≥3；如果 T无 pole，则 LT在µ analytic。因此任何 rational T都不能使 `LT` 具有 µ的唯一 simple pole。旧 `r_B,t³` 在µ analytic，故

\[
 R_a\notin L(Q(t))+Q r_B+Q t^3.                          \tag{P12}
\]

特别地由旧域分类 K1，`B_a∉E_B(log(1+28t))`。P12还说明其 rational forcing class 不能被原两个 polynomial classes 吞掉。整数 a=28 时旧 Kummer 也在同一个µ有log，但 K1照样覆盖它；没有把旧 Kummer 的 additive jump 误当作新的 homogeneous-valued jump。

对 distinct `a₁,…,a_k`，based µ_i loop对其它 B_a、V 和1恒等，只对第i解增加P11。对µ_i loop作 based conjugation，actual irreducible homogeneous monodromy使非零v的 orbit span为全V。若存在 C(t)-linear relation

\[
 c_0+\sum_{i=1}^k(c_iB_{a_i}+d_i\theta B_{a_i})=0,       \tag{P13}
\]

沿上述第i组 loops取 difference，给 `c_i v+d_i θv=0` 对所有 `v∈V`。在 ordinary basepoint两个齐次解的 Wronskian非零，遂 `c_i=d_i=0`。最后 `c₀=0`。故真实完整数组

\[
 (1,B_{a_1},\theta B_{a_1},\ldots,B_{a_k},\theta B_{a_k})
 \quad\text{具有实际 rank }m=2k+1.                       \tag{P14}
\]

这里 rank 是 `C(t)` 上函数独立性，绝不等价 `(1,C_{a₁},…,C_{a_k})` 的 Q 数值独立性。单个 `G=B_a−uA` 的同样 loop argument给 `(1,G,θG)` rank3，对任何 u成立，不会因假设 `C_a∈Q` 自动降成rank2。

P5付两条相同 width1、slope1列，其 row sums为 `(0,2,…,2)`。CDT Theorem6.0.2给

\[
 \tau_\flat=2(1-m^{-2}),\qquad m=2k+1;
 \quad\text{单解 rank3 时 }\tau=16/9.                    \tag{P15}
\]

低 arithmetic cost 与更大 joint rank均已付，但新增µ logarithm对可用 domains有真约束。P15并未包含足以得出 numerical theorem的严格几何余量。

## 6. 同一正测度的 Stieltjes 比较和全阶矩

把正测度 `4π² y f(iy)dy` 通过 `x=t(iy)` push forward为ν。它有限，massκ，support为 `[0,σ]`（端点0无 atom、每个内部开区间有正mass）；P6变成

\[
 C(a)=\int\frac{d\nu(x)}{1+ax},\qquad a>-28,
 \quad C(0)=\kappa,\quad C(a)=C_a\ (a\ge1).              \tag{P16}
\]

dominated differentiation 在每个 compact `a>-28` 区间成立。对于 k≥0，

\[
 (-1)^k C^{(k)}(a)=k!\int\frac{x^k}{(1+ax)^{k+1}}d\nu(x)>0;
 \qquad \frac{\kappa}{1+a/28}<C_a<\kappa\quad(a\ge1).
                                                               \tag{P17}
\]

strictness来自support不是单点。这里只是在该实参数区间的 Stieltjes transform，不把 `a`-plane解析延拓或某个 classical L值评价当作已证。

定义 `M_n=∫xⁿdν,n≥0`。forcing `r_B tⁿ` 是 polynomial，前稿的准确 quotient theorem给 `R=b r_B+c t³+LT`，其 σ coefficient为 `bκ+cC₃−T(0)`。所以

\[
 M_n\in Q+Q\kappa+QC_3\quad(n\ge0),\quad M_0=\kappa.
                                                               \tag{P18}
\]

这是每一个真实 moment 的有限纸面 reduction，不是只读数值识别。前两次直接给

\[
 M_1=\frac16-\frac\kappa3-C_3,\qquad
 M_2=\frac5{28}-\frac{8\kappa}{21}-\frac{13C_3}{14}.       \tag{P19}
\]

例如 `L1=−2t−4t²`，`L(t)=t−46t²+81t³−42t⁴`，逐项验证第二式的 forcing decomposition为
`t³−t⁴=−(8/21)r_B−(13/14)t³+L(t/42−5/28)`。没有默认为M_n coefficient的 common denominator已经由B_a的D_n²支付。

还得到一个校准值：`r_B/(1−t)=t=(2/3)r_B+L(−1/6)`，归一化解为 `(2/3)B−1/6+(1/6)A`，因此

\[
 C(-1)=\frac{2\kappa}{3}+\frac16.                       \tag{P20}
\]

P20来自完整连接系数，是已知 period space内的新表示，不是新的 irrationality result。

## 7. 一个 exact 正矩递推，及其算术尚未支付的接口

设 `J_n=∫x^(n−1)/(1−x)dν`，n≥1。因为 `σ<1`，全部 convergentpositive，并满足

\[
 J_1=\frac{2\kappa}{3}+\frac16,
 \quad J_2=\frac16-\frac\kappa3,
 \quad J_3=C_3,\qquad M_n=J_{n+1}-J_{n+2}.               \tag{P21}
\]

对 `T=tⁿ`，n≥1，polyforcing `LT` 的真连接系数为 `−T(0)=0`；其 Mellin integrand为 `f LT/r_B`。把P1的p展开 `1−30t+57t²−28t³`，直接得到

\[
 n^2J_n-(30n^2+14n+2)J_{n+1}
 +(57n^2+28n-4)J_{n+2}-14n(2n+1)J_{n+3}=0.               \tag{P22}
\]

这是 all n恒等式；n=1恢复P19的第二式。其 limiting characteristic为 `(1−r)²(1−28r)`，但没有仅从该 polynomial声称所有 recurrence solutions的 asymptotics或整性。

实际 `J_n` 的正性及指数支撑给严格 upper `0<J_n≤σ^(n−1)J₁`，且 `lim J_n^(1/n)=σ`：upper显然；每个ε>0在 `(σ−ε,σ]` 有正mass给lower后令ε→0。可以更精确：ordinary Wronskian和finite positiveA atσ给 `τ−τ_c` 为 `(t−σ)^(1/2)` 的非零局部坐标，τ_c=i/√7。于是 `t(iy)=σ−c(y−1/√7)²+O((y−1/√7)³)`，c>0；ν在σ附近的density是 positive constant `(σ−x)^(-1/2)(1+O(√(σ−x)))`。标准局部 Laplace substitution直接给

\[
 J_n\sim c_*\,\sigma^{n-1} n^{-1/2},\qquad c_*>0.       \tag{P23}
\]

不需要执行 asymptotic producer。该 constant只标正，不声称是 algebraic；它涉及真实 period normalization。

另外对任何 d≥0，moment Hankel matrix `(M_{i+j})_(0≤i,j≤d)` positive definite：任意 nonzero real polynomialP有 `∫P(x)²dν>0`，所以

\[
 \det(M_{i+j})_{0\le i,j\le d}>0.                        \tag{P24}
\]

这为 Hermite–Padé／正矩方法提供 genuine nondegeneracy，不是 `1,κ,C₃` 的Q-linear independence。若要把P22–P24变成新的数值结论，必须另证 reduced linear-form coefficient的**实际全素数整数 lattice、增长与非零性下界**。P5是另一组 Taylorcoefficients的cap，不能移用来支付P22的 rational recurrence division。本文没有填此缺口。

## 8. 来源、真实读取范围与交付边界

本轮 actual FULL阅读前稿 E1–E29/all8sections、旧域分类K1–K27/all8sections及其正式reviewV1–V8；mutablemain只读取header与§§201–205，guards全文只读。此前历史阅读不冒充本轮fresh阅读。authority实际解析current_progress及SHA，旧620项的metadata核对另见本轮delivery，不称完整人工重审旧数学。

- [Yang fixed v1 primary](https://arxiv.org/abs/0709.1968v1)，复用 [已有PDF](../literature/yang2007_apery_limits_v1_20261006.pdf)，actual FULL physical PDF5–6、15–16共4页；variation Lemma1/2、Example2、actualt/CMpoints/operator及完整σ比较。
- [CDT primary](https://arxiv.org/abs/2408.15403)，复用 [已有PDF](../literature/cdt2024_l2_chi_minus3.pdf)，actual FULL PDF66–69共4页；Theorem6.0.2、formula6.0.9、fixedoffset Remark6.0.12与全行 arithmetic costs。slope可为非负实数，e必须非负整数。

截至本稿 root个人actualfreshprimary共8 distinct页，无render、无新PDF、无数学运行。P9–P24为本文具体对象的纸面推导，不声称 primary 已证明这些新推论。

本轮新结果是：无限真实 rational-pole Greenfamily；同D_n²的完整all-primecap；每个成员全germ σ连接常数；新增ordinaryµ所有branches不可填的log；任意有限族actualrank2k+1及oldfieldescape；同一个positiveStieltjesmeasure；两类momentreduction、exactrecurrence、recessivepositivebranch及Hankelnondegeneracy。仍未证明任一新增C_a或C₃的无理性、`1,κ,C₃` 或周期族的数值LI；未证明新的ζ7/Catalan/非CMratio结果；无Lean。下一步优先核P22递推的真正整数模型，或为P2完整filledleaf寻找能跨CDTbound的actualmap，不能跳过新增µ。
