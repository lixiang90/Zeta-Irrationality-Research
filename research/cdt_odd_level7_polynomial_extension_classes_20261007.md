# Level 7 的第二条真实扩张：多项式 forcing 全分类、低分母整模型与完整 Mellin 连接常数

日期：2026-10-07。作者：`/root`。本轮 authority 为 `cdt_odd_delivery_paired_anti_modular_slopes_20261007.json`，SHA `47e298629fba798cc2d11a1e711219e61746c617f25f308919d9e1c6f6a7ecab`，612 frozen（607 mathematical、5 guards）。旧冻结文件只读。本稿为纸面证明；数学 producer 新建、执行、导入、重跑、prime 扩表与 Lean 均为0。

本稿得到一个确切的新对象，而不声称新的特殊值无理性定理。对实际 level 7 算子，全部多项式 forcing modulo rational splitting 恰有两维：已知 CM cusp form 的 class 和 `t³` 的 class。第二个 class 的真实解 `B₃` 仍有全素数 `D_n²` 整模型，其完整反射连接常数可写为一个正的、收敛的 Mellin 周期 `C₃`。它不属于原有完整周期／相对解与 Kummer 对数生成的 Picard–Vessiot 场。这个构造补上“独立载体 + 整模型 + 完整连接常数”的一组缺口；将 `C₃` 识别为所需数值、以及取得严格 CDT margin，仍未完成。

## 1. 固定真实模型与约定

采用冻结 `cdt_odd_gamma_modular_relative_target_20261007.md` M1–M25 的原坐标和分支，不替换原 ξ、ζ(7) 或 Catalan 项目的数据。`θ=t∂t`，

\[
 L=p(t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),\quad
 p(t)=(1-t)^2(1-28t),\quad r_B=t(1-t),\quad \sigma=1/28. \tag{E1}
\]

Yang fixed v1 PDF5–6、15–16 给实际齐次 basis `A,τA`，以及

\[
 t(q)=\left(\frac{\eta(\tau)^4}{\eta(7\tau)^4}+14+
              49\frac{\eta(7\tau)^4}{\eta(\tau)^4}\right)^{-1}
       =q-10q^2+\cdots\in q\mathbb Z[[q]],
\]
\[
 A(q)=1+2\sum_{n\ge1}\chi_{-7}(n)\frac{q^n}{1-q^n}
       \in1+q\mathbb Z[[q]],\quad
 f(q)=\eta(\tau)^3\eta(7\tau)^3\in q\mathbb Z[[q]],
 \quad q=e^{2\pi i\tau}.                                    \tag{E2}
\]

`q(t)∈tZ[[t]]` 是同一 integer inverse，故 `A(t)∈Z[[t]]`。实际 `B` 满足 `LB=r_B`、`B(0)=0`，且

\[
 B(t(q))=A(q)\sum_{n\ge1}c_nq^n/n^2,\quad f=\sum c_nq^n,
 \quad \kappa=L(f,2),\quad B-\kappa A\text{ 在 }\sigma\text{ 全 germ analytic}. \tag{E3}
\]

`ΔσA=ψ≠0`；以下采用 E3 同一 based loop、同一真实 branch。Ordinary derivative 的三个系数是

\[
 p_2=t^2(1-t)^2(1-28t),\quad p_1=t(1-t)^2(1-42t),\quad
 p_0=-2t-4t^2.                                               \tag{E4}
\]

finite exponents 分别为0处 `(0,0)`、σ处 `(0,1/2)`、1处 `(1/3,2/3)`；∞处以 `z=1/t` 计为 `(0,1/2)`。真实齐次 monodromy 的 connected closure 为 `SL₂`，所以其二维 representation `V` irreducible。以上固定事实在冻结 M 稿已有完整证明，本稿仍将所用 normalization 明列，以便核查新构造。

## 2. 全部多项式 forcing 恰有两条非拆分 class

对 `R∈tQ[t]`，记 `B_R` 为唯一 `LB_R=R`、`B_R(0)=0` 的 analytic germ。系数 recurrence 的 leading term 是 `n²`，所有其它项只用更低系数，故 `B_R∈Q[[t]]` 且唯一。新对象为

\[
 LB_3=t^3,\qquad B_3(0)=0.                                  \tag{E5}
\]

**命题 E1（forcing 商空间）。**

\[
 t\mathbb Q[t]/L(\mathbb Q[t])
       =\mathbb Q[r_B]\oplus\mathbb Q[t^3].                 \tag{E6}
\]

此处方括号是 vector-space class，而非 polynomial ring。证明：`L1=-2t-4t²`。若 `T` degree `d≥1`，则最高项为

\[
 -14d(2d+1)[t^d]T\ t^{d+3}.                                 \tag{E7}
\]

因此从 degree≥4 的 forcing 逐次减去 rational multiple 的 `L(t^{n-3})`，唯一降到 `span{t,t²,t³}`；在该三维空间里 `L(Q[t])` 只有 `Q L1`。`r_B=t-t²` 与 `L1` 独立，E6 得证。这里是所有 degree 的纸面 triangular reduction，不依赖有限 coefficient search。

这也正是 rational splitting 商空间。若 `LT` 为 polynomial 而 `T∈C(t)` 在 ordinary point 有 pole，则 `p₂T''` 的最高 pole 无法消去；在0、σ、1，负整数 pole exponent 都不是 E4 的 indicial root，同样不能消去。因此 `T` 无 finite pole，必为 polynomial。结合 E7 和 `L1`，

\[
 a r_B+b t^3\in L(C(t)),\ a,b\in C\quad\Longleftrightarrow\quad a=b=0. \tag{E8}
\]

故对每个 `R∈tQ[t]` 存在唯一 `a,b∈Q` 和 `T∈Q[t]`，使

\[
 R=a r_B+b t^3+LT,\qquad
 B_R=aB+bB_3+T-T(0)A.                                      \tag{E9}
\]

唯一性还用 `L` 无 rational homogeneous solution：相同 pole argument 与 E7 后，只余 constant，而 `L1≠0`。第二个 equality 由 zero constant analytic uniqueness 给出。

## 3. 每条多项式 class 都有同一个全素数 cap

设 `S(q)=q t'(q)/t(q)`，其中 prime 在本节为 q derivative。写 `t=qV(q)`，`V∈1+qZ[[q]]`，便有

\[
 S=1+qV'/V\in1+q\mathbb Z[[q]].                            \tag{E10}
\]

`θ_q=Sθ_t`。因 `A` 和 `τA` 同为 homogeneous solution，对任意 scalar `E(q)` 直接展开两次导数，`E` 和 `θ_qE` 项都为0，得到

\[
 L(AE)=p(t)A S^{-2}\theta_q^2E.                             \tag{E11}
\]

前者来自 `LA=0`，后者可令 `E=τ=(log q)/(2πi)` 核验；最高项给 E11 的 coefficient，没有假设额外 modular transformation。

因此对 integer polynomial `R∈tZ[t]`，

\[
 f_R(q)=\frac{R(t(q))S(q)^2}{p(t(q))A(q)}\in q\mathbb Z[[q]],
 \quad B_R(t(q))=A(q)\sum_{n\ge1}\frac{[q^n]f_R}{n^2}q^n.   \tag{E12}
\]

所有 denominator factors 在 q=0 都是 integral unit。第 n 个 Taylor coefficient 的 denominator 只来自 `1²,…,n²`；再与 integral `A` 相乘、用 integral `q(t)` 复合，第 n coefficient仍只用前 n 项。记 `D_n=lcm(1,…,n)`、`D_0=1`，便得全部 primes、全部 prime powers、全部 n 的 exact safe statement

\[
 D_n^2[t^n]B_R\in\mathbb Z.                                \tag{E13}
\]

`R∈tQ[t]` 只需一个 fixed multiplier `M`，所有 fixed `θ`-jets 同 cap。E13 没有把 degree-dependent factorial 当整模型，没有用 experimentally guessed denominator，也没有宣称这是 prefix sharp cap。

对新 E5，E3 和 E12 给

\[
 f_3=f\frac{t^2}{1-t},\qquad
 B_3=A\sum_{n\ge1}\frac{[q^n]f_3}{n^2}q^n,\qquad
 D_n^2[t^n]B_3\in Z.                                       \tag{E14}
\]

`f₃` 是 weight3 meromorphic modular form，而非处处 holomorphic cusp form。其 modular poles 不允许被忽略；§5 将用实际收敛的路径积分定义连接常数，不把这个 formal q-series 免费称为普通 Dirichlet L-series。

## 4. ∞的真实 logarithm、旧场逃逸与实际秩

令 `z=1/t`、`ϑ=z∂z`。代入 E1 后，

\[
 \widetilde L:=z^3L=(z-1)^2((z-28)\vartheta^2+14\vartheta)
                     -4z-2z^2.                            \tag{E15}
\]

indicial 是 `-14α(2α-1)`。取真实 local homogeneous basis `v₀=1+O(z)`、`v_{1/2}=z^{1/2}(1+O(z))`。`v₀ log z` 经 `\widetilde L` 的 logarithm 项因 `\widetilde L v₀=0` 消失，analytic output 的 constant 为14。而 `\widetilde L B₃=1`。减去 `(1/14)v₀ log z` 后，forcing constant 为0，integer `n≥1` 的 indicial coefficient 都非零，所以可逐项构造 analytic particular。收敛由 regular-singular Frobenius theorem。故完整 local germ 必有

\[
 B_3=\frac1{14}v_0\log z+u(z)+a v_0+b v_{1/2},\quad u\in zC\{z\}. \tag{E16}
\]

反之 `\widetilde L B=z²-z`，constant 为0，`B` 在此只有 analytic 与 half-power 项，无 logarithm。所有 homogeneous branches 也无 logarithm。明确令 `T∞` 是正向绕 `z=0` 的 monodromy；两次 loop 因此满足

\[
 (T_\infty^2-I)B_3=(2\pi i/7)v_0\ne0,\qquad
 T_\infty^2|_{E_B}=I,                                      \tag{E17}
\]

其中 `E_B=C(t)(V,V',B,B')` 为原 affine 系统的完整 PV field。E17 在任意 added homogeneous branch 下不变，也不能被 finite ramified cover 消去 logarithm。于是 `B₃∉E_B`。

再令实际 `ℓ=log(1+28t)`、`μ=-1/28`。`μ` 对 polynomial-forcing B₃、原系统均 ordinary，µ-loop 固定它们而令 `ℓ→ℓ+2πi`。若 `B₃∈E_B(ℓ)`，一个 rational function in `ℓ` 被所有 integer translations固定，必与 `ℓ` 无关：非constant rational function 的 finite poles不能在无限 translations下稳定，polynomial 的最高 degree 也不能稳定。故 `B₃∈E_B`，与 E17 矛盾。因此

\[
 B_3\notin E_B(\ell).                                      \tag{E18}
\]

**命题 E2（actual joint rank）。** `1,B,θB,B₃,θB₃` 在 `C(t)` 上线性无关，实际 full-jet rank 为5。证明：任意 rational row relation，施加 E17 与其 conjugates `gT∞²g⁻¹`。这些 conjugates固定整个 `E_B`，且对 `B₃` 的 jump 是 nonzero constant times `g v₀`；因为 E17 在 homogeneous `V` 上恒等，affine coboundary 在 conjugation中消去。irreducible V 意味这些 vectors span V。故 B₃、θB₃ 的两个 row coefficients经 homogeneous Wronskian 被迫为0。剩下 `1,B,θB` actual rank3：其 nonzero affine translation kernel为全部 V（E8、irreducible SL₂ 与 reductive splitting；详见本轮 Kummer 分类 K12），再同一 Wronskian argument 即得。五个 entries 的 derivative闭合由 E1、E5给出，所以恰为5，而非仅 formalupperbound。

同理，对 `(a,b)≠(0,0)`、任意 `u∈C`，`G=aB+bB₃-uA` 的 forcing E8 非拆分，`1,G,θG` actual rank3。这里 rank statement 与 G 的 numerical connection constant 是否 rational 无关；不能把一个数值假设免费降成rank2。

## 5. 新连接常数的完整 Mellin 识别

记 `wτ=-1/(7τ)`、`j(τ)=-i√7τ`，沿上半平面选 standard eta branch。E2 给 `t(wτ)=t(τ)`；Dedekind eta inversion 直接给

\[
 f(w\tau)=i7^{3/2}\tau^3f(\tau).                            \tag{E19}
\]

不需要另猜 A 的 multiplier。对 E12 的 R=r_B，有

\[
 f=g(t)S^2/A,\quad g(t)=t/((1-t)(1-28t)).
\]

由 invariant t 求导得 `S(wτ)=7τ²S(τ)`，结合 E19，作为 meromorphic identity得到

\[
 A(w\tau)=j(\tau)A(\tau).                                  \tag{E20}
\]

式中 possible isolated zeros 由 analytic continuation处理。`h(τ):=f₃(τ)=f(τ)t(τ)²/(1-t(τ))` 同样满足 E19；在 imaginary axis 上无 pole。事实上令 `r=η(iy)^4/η(7iy)^4>0`，AM–GM 给

\[
 0<t(iy)=1/(r+14+49/r)\le1/28=\sigma,\quad h(iy)>0.         \tag{E21}
\]

在 y→∞ 有 cusp exponential decay，在 y→0 由 E19 有同类 decay乘有限 power。因此以下 actual integrals均收敛：

\[
 C_3=4\pi^2\int_0^\infty y h(iy)\,dy,\quad
 D=4\pi^2\int_0^\infty h(iy)\,dy.                            \tag{E22}
\]

用 y=1/(7v) 和 `h(i/(7v))=7^{3/2}v³h(iv)`，得到 `D=√7 C₃`。

定义 imaginary-axis continuation 的 actual primitive

\[
 E_h(\tau)=-4\pi^2\int_{i\infty}^{\tau}(\tau-z)h(z)\,dz,
 \quad E_h(iy)=4\pi^2\int_y^\infty(v-y)h(iv)\,dv.             \tag{E23}
\]

在 sufficiently high imaginary neighbourhood它等于 E14 的 q-primitive，`E_h''=-4π²h`；沿 axis和其无pole邻域实际 continuation给 `B₃=A E_h`。令 `Q(τ)=j(τ)E_h(wτ)-E_h(τ)`。因为 `w'=1/(7τ²)`、`w''=-2/(7τ³)`、`j'=-i√7`，二阶求导的 `E_h'` coefficient `2j'w'+jw''` 恰为0，而

\[
 j(w')^2 E_h''(w\tau)=E_h''(\tau)
\]

由 E19 直接核验，故 `Q''=0`。在 τ=iy、y→∞，E23给 `E_h(iy)→0`、`E_h(i/(7y))=C₃-D/(7y)+o(1/y)`，于是

\[
 Q(\tau)=C_3(j(\tau)-1),\qquad
 j(\tau)(E_h(w\tau)-C_3)=E_h(\tau)-C_3.                    \tag{E24}
\]

这里 asymptotics同时确定affine function的两个 coefficients；没有只在fixed point比一个数值。

在 `τ_c=i/√7`，t=σ 是真实 order2 elliptic point，`t-σ` 为 nonzero quadratic local coordinate，w是local involution。E20、E24得

\[
 (B_3-C_3A)(w\tau)=(B_3-C_3A)(\tau).                       \tag{E25}
\]

`h,A,E_h` 在τ_c analytic；invariant analytic germ 下降为t-coordinate 的analytic germ，故

\[
 B_3-C_3A\text{ 在 }\sigma\text{ 全 germ analytic},\qquad
 \Delta_\sigma B_3=C_3\Delta_\sigma A.                       \tag{E26}
\]

这付清完整 fractional germ jump，强于只知道 `B₃/A` 的边界值。E9 因此给全部 polynomial forcing 的完整连接系数

\[
 C_R=a\kappa+bC_3-T(0).                                    \tag{E27}
\]

数值范围也严格可证。由 `t²/(1-t)` 在 `(0,σ]` increasing、最大值 `1/756`，`f(iy)>0`，以及 classical Mellin identity `κ=4π²∫₀∞ y f(iy)dy`，

\[
 0<C_3<\kappa/756.                                         \tag{E28}
\]

严格性来自t在两端趋0，而不是只用其最大值。E22是 meromorphic modular form 的路径 Mellin 周期；由于离路径的 interior modular poles，Fourier coefficients未必只有 polynomial growth，不能未经证明把 `Σ[qⁿ]h/n²` 在q=1的值定义为普通 L(h,2)。本文也未识别 `C₃` 为log2、ζ奇数值、Catalan、某个已知 Dirichlet L-value，未从正性或小上界推断无理性。

## 6. 完整整模型之后，CDT margin 仍须另付

E13 给 actual joint five entries `1,B,θB,B₃,θB₃` 两条相同 b=2、e=0 的 denominator columns：sorted row widths为 `(0,1,1,1,1)`。CDT fixed PDF66–69 中 Theorem6.0.2 的(6.0.4)、Remark6.0.11与Corollary6.0.14 的 flat arithmetic cost，逐列计算为

\[
 \tau_{\rm flat}=2(3+5+7+9)/5^2=48/25.                     \tag{E29}
\]

单一 G 在 `a,b,u∈Q`、`(a,b)≠(0,0)` 时，有fixed multiplier M下的cap D_n²，actual rank3对应 widths `(0,1,1)`，cost `2(3+5)/9=16/9`。§4的rank3对complex参数也成立，但此算术cap只对上述Q参数适用。这些是 safe upper arithmetic budgets，本文没有证明其 sharp，也没有得到新的 geometric lift或严格 `ρ>τ`。在σ填掉一个完整half-power jump并不填掉0、1、∞；尤其 E16的 logarithm 是新class的确切额外成本接口。新B₃虽然在旧field之外且不增加单列cap指数，actualjointrank、所有puncture和解析domain仍需同时支付。

不能将“第二条independent extension”误写为 `1,κ,C₃` 数值线性无关。PV field和forcing quotient的独立是函数层面的定理；specialization到一个realperiod需要额外的arithmetic holonomy margin和非零germ证书。若假设 `C₃=u∈Q`，E26填σ，但G=B₃-uA仍actualrank3，∞仍有E16。本文没有从该假设导出矛盾。

## 7. 更深数学的真实接口与不能免费使用的结论

本轮新归档 Brown–Fonseca v2 的69页原件，实际 FULL PDF1–4、41–43、49–50用于解释新meromorphic modular period的框架，未用它替代上面的explicit proofs。

其relative/punctured modular cohomology把 endpoints、poles与所附elliptic fibers纳入同一mixed object（§8.1–8.2，PDF41–43）；这与E14的meromorphic source方向一致。但其 Theorem8.4有 cusp-cohomology vanishing等条件，真实level7已有非零f cusp class，不能直接套用。Theorem8.6的CM Tate结论针对 even k=2m；本稿weight3对应k=1，不能自动给Kummer/logarithm class。PDF49对odd k=1的elliptic Rankin–Selberg periods提出expected/conjectural比较，不是本稿可以调用的无条件special-value formula。PDF50的mixed-Tate Ext¹=K×⊗Q也不证明E5属于mixed-Tate范畴。

因此下一步应对E14的实际pole divisors和relativeclass做独立识别，或为E26找更强analytic domain与不同算术模型。仅以“CM”“motivic”“single-valued”命名不会把E22化为log2。本文没有证明所有level7 relativeextensions都只两维；E6仅为polynomial forcing modulo rational split的完整分类，带新增poles的rationalforcing仍可能引入新classes。

## 8. 本轮实际读取与交付边界

root actual FULL本轮冻结M1–M25/all8sections与本轮Kummer分类K1–K27/all8sections；current progress只读header及§§196–200，未称旧全main已全文重读。对原件本轮fresh读取：

- Yang fixed v1：`literature/yang2007_apery_limits_v1_20261006.pdf`，actual FULL PDF5–6、15–16，4 distinct pages，[primary](https://arxiv.org/abs/0709.1968v1)。
- CDT：`literature/cdt2024_l2_chi_minus3.pdf`，actual FULL PDF66–69，4 distinct pages，[fixed v2 primary](https://arxiv.org/abs/2408.15403v2)。
- Brown–Fonseca v2：`literature/cdt_gamma_level7_punctured_sources_20261007/brown_fonseca2025_single_valued_meromorphic_arxiv2508_04844v2.pdf`，SHA `17f8556f14261236af621695799387065cd70dae4295b52f3ee6e82d28593a66`，1034906bytes，69 archive pages，actual FULL PDF1–4、41–43、49–50，9 distinct pages，[primary](https://arxiv.org/abs/2508.04844)。完整priorarchive identifier/SHA preflight未见该version，normal verified-TLS HTTP200保存；未重复保存其v1。

本稿作者主证明域实际primary17 distinct pages（4+4+9），render0。后续正式independent review读取域在其review/receipt单列，不能反向当成本稿完成前的阅读。normal documentary extraction、hash、metadata不算数学producer；本稿没有创建或执行系数、rank、prime、数值实验代码。

本轮新定理是E6/E8/E9的完整polynomial class分类，E13的全部素数cap，E16/E18的真实logarithm及旧PV–Kummer field逃逸，actualjointrank5，以及E22/E26/E27的完整Mellin连接常数与E28界。特殊值无理性、数值LI、Lean formalization和新的strictCDT margin目前均未得到；原项目guard保持原冻结状态。
