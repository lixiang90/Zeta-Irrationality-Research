# 一个实际 level‑7 低维相对解析扩张：完整局部分支、全有限处整性与跨权重目标的缺口

日期：2026‑10‑07。作者：`/root/masked_racah_finalize`。本稿仅作纸面证明，数学 producer 新建、执行、导入、重跑均为0，素数表扩展0。旧604个冻结记录不修改。上一轮 authority 为 [carry–Cartier–split–algebraic audit](cdt_odd_delivery_carry_cartier_split_algebraic_20261007.json)，SHA `44521a432fd71bdfef7e10a0d3ac63d636878b32aabfad5b293d8276a9fdf4a7`；本文没有逐页继承该 audit 的阅读声明，也没有独立重复其604项核验。

本轮结论分三层：Yang 的 level‑7 模型给真实二阶非齐次方程和一个完整的局部分支消去；本文证明其整数坐标中的全 prime `D_n²` 模型、实际三维函数空间，以及保留同一整性的三次覆盖；进一步证明在同一载体中简单乘上 logarithm 无法实现跨权重 relation 的完整跳跃。该模型的标量常数本身已由 CM 椭圆周期理论证明超越，所以不是新的无理性目标。没有把这个解析扩张宣称为已有 higher Chow cycle 的 normal function。

## 1. 固定模型与已证比较

置 `q=exp(2πiτ)`、`θ=t d/dt`、`D_n=lcm(1,…,n)`，`D_0=1`。全部函数先取 `q=0` 对应的实际 branch。Yang 原件 PDF15–16 的 Example2/Theorem2 给

\[
 f(\tau)=\eta(\tau)^3\eta(7\tau)^3=\sum_{j\ge1}c_jq^j,
 \qquad \kappa=L(f,2),                                      \tag{M1}
\]
\[
 t(q)=\left(\frac{\eta(\tau)^4}{\eta(7\tau)^4}+14+
 49\frac{\eta(7\tau)^4}{\eta(\tau)^4}\right)^{-1},\qquad
 A(q)=1+2\sum_{j\ge1}\left(\frac j7\right)\frac{q^j}{1-q^j}.
                                                               \tag{M2}
\]

`t=q−10q²+49q³−184q⁴+…`，`A(t)=1+2t+24t²+…`。固定未约分的实际算子

\[
 L=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2).
                                                               \tag{M3}
\]

原件的 forcing 和初值是

\[
 LA=0,\quad LB=t(1-t),\quad
 B(0)=0,\quad [t]B=1,\quad[t^2]B=45/4.                         \tag{M4}
\]

Yang Lemma1/2，PDF5–6，说明同一 germ 的实际 Euler–Eichler 表达是

\[
 B(t(q))=A(q)E(q),\qquad E(q)=\sum_{j\ge1}\frac{c_j}{j^2}q^j.
                                                               \tag{M5}
\]

这里 Lemma1 中首项为1的 normalized operator 的 forcing 是 `g=t/[(1−t)(1−28t)]`；乘上 M3 的首系数得 `(1−t)²(1−28t)g=t(1−t)`，没有把两种 forcing 混用。M4 在 `t`、`t²` 的系数也直接给 `b_1=1`、`4b_2−46b_1=−1`，与 `45/4` 一致。

最重要的比较是 Yang 在 Example2 明确证明的完整解析声明：

\[
 B-\kappa A\ \text{在}\ \sigma=1/28\ \text{可解析延拓为单值全纯 germ}.
                                                               \tag{M6}
\]

本文使用 M6 的全部 germ 意义；没有仅由 `b_n/a_n→κ` 反推 M6。在小穿孔圆盘上记一次正向 continuation 为 `T_σ`，则对于任意常数 `u`

\[
 (T_\sigma-I)(B-uA)=(\kappa-u)(T_\sigma-I)A.                   \tag{M7}
\]

M7 是完整跳跃，而非领先系数或有限个 jets 的相等。原件给 `t` 在三个 elliptic points 的值分别为 `σ,1,∞`，在唯一 cusp 的值为0。齐次奇点确为 `{0,σ,1,∞}`。

## 2. 同一 t 坐标中的全有限处整模型

以下证明不使用递推中逐步除 `n²` 的粗 factorial 预算。写

\[
 \frac{\eta(\tau)^4}{\eta(7\tau)^4}=q^{-1}U(q),\qquad
 U(q)=\prod_{j\ge1}\frac{(1-q^j)^4}{(1-q^{7j})^4}
       \in1+q\mathbb Z[[q]].
                                                               \tag{M8}
\]

因 constant term 为1，`U⁻¹∈1+qZ[[q]]`。于是

\[
 t(q)=\frac{q}{U(q)+14q+49q^2U(q)^{-1}}
       \in q+q^2\mathbb Z[[q]],\qquad
 q(t)\in t+t^2\mathbb Z[[t]].                                 \tag{M9}
\]

逆式的整性可逐系数证明：若 `t(q)=q+Σ_{j≥2}t_jq^j`，求逆式的第 `n` 项时，未知 `q_n` 的系数恰为1，其余项是此前整数系数的整数多项式，所以 `q_n∈Z`。这只要求首系数1，没有引入额外固定或随 `n` 增长的分母。

Eta product M1 的 leading exponent 为 `(3+21)/24=1`，每个 Euler factor 的指数为整数，故 `c_j∈Z`；M2 同样给 `A(q)∈Z[[q]]`。从 M5、M9，`[t^n]B` 只用到 `c_j/j²`，`1≤j≤n`，乘 `D_n²` 后每项均为整数。因此

\[
 A(t)\in\mathbb Z[[t]],\qquad
 D_n^2[t^n]B(t)\in\mathbb Z\quad(n\ge0).                     \tag{M10}
\]

M10 包括所有 primes 和所有 prime powers，完全由 `j²|D_n²` 支付；没有 good‑prime 例外。对于 `u=a/M∈Q`、任何固定非负整数 `j`

\[
 M D_n^2[t^n]\theta^j(B-uA)\in\mathbb Z.                     \tag{M11}
\]

由于 `θ^j` 在第 `n` 项只乘 `n^j`，M11 没有 ordinary derivative 的 factorial 漏项。本文仅把它作为安全 cap2，既不声称最小分母恰为 `D_n²`，也不声称任意带有 rational gauge 的普通导数仍免费。

## 3. 实际 rank3：非齐次解不是有理函数

将 M3 写成 ordinary derivative 形式：

\[
 Ly=p_2y''+p_1y'+p_0y,\quad
 p_2=t^2(1-t)^2(1-28t),\quad
 p_1=t(1-t)^2(1-42t),\quad p_0=-2t-4t^2.                    \tag{M12}
\]

由 M12 直接计算 local exponents：`t=0` 是 `(0,0)`；`t=σ` 是 `(0,1/2)`；`t=1` 是 `(1/3,2/3)`；在 infinity 的局部坐标 `z=1/t` 是 `(0,1/2)`。例如 `t=1+s` 时，indicial polynomial 是 `−27α(α−1)−6`；`t=σ+s` 时，`lim s p_1/p_2=1/2`、`lim s²p_0/p_2=0`。这些是同一未改 gauge 算子的指数。

**无有理 particular solution。** 若 `Ly=t(1−t)` 的 `y∈C(t)` 在 ordinary finite point 有极点，最高阶 `p_2y''` 不能与较低阶项抵消。在上述三个 finite singular points，pole exponent `α=−N<0` 都不是 indicial root，所以也不可能有极点。故 `y` 必为 polynomial。若其 degree `d≥1`，M3 最高项为

\[
 -14d(2d+1)[t^d]y\ t^{d+3},                                 \tag{M13}
\]

不能等于 degree2 的 forcing。若 `y=c`，则 `Ly=−2ct−4ct²`，同时要求 `−2c=1`、`−4c=−1` 也不可能。因此没有有理 particular；换 forcing 的整体符号结论相同。

齐次 actual solution basis 是 `A,τA`，由 Yang Lemma1 的 variation proof 给出。其 monodromy 在 modular uniformization 上是 weight1 的标准二维表示乘有限角色；在 `Γ_0(7)` 中含 `[[1,1],[0,1]]` 和 `[[1,0],[7,1]]` 两个不同 invariant lines 的 unipotents，角色在二者均为1。因此齐次 monodromy irreducible，其 connected Zariski closure 是 `SL₂`。这里真正使用了 modular solution basis，并非将形式 order2 自动称为 actual rank2。

现在令 `F_u=B-uA`，其中 `u` 可为任意复常数。各 loop 的 `Δ_gF_u` 都是齐次解。若这些差全为0，regular singularity 及 rational forcing 保证各 branch 只有 finite power/logarithmic growth；单值者在各 puncture 延拓为 meromorphic germ，于 infinity 也如此，遂 `F_u∈C(t)`，与 M13 矛盾。差的空间 `W=span_C{Δ_gF_u}` 非零。Cocycle identity

\[
 \Delta_{gh}F_u=\Delta_gF_u+\rho(g)\Delta_hF_u
                                                               \tag{M14}
\]

使 `W` 在齐次 monodromy 下 invariant，故 `W` 为全部二维齐次解空间。若 `R F_u+S θF_u+T=0`，`R,S,T∈C(t)`，对所有 continuation 作差，可得 `R y+S θy=0` 对两独立齐次解同时成立；Wronskian 非零，强制 `R=S=0`，继而 `T=0`。因此

\[
 \dim_{\mathbb Q(t)}\operatorname{span}\{1,F_u,\theta F_u\}=3
 \quad(u\in\mathbb Q),                                      \tag{M15}
\]

事实上该三元组在 `C(t)` 上也 independent。这里 `F_u` 非齐次、rank3 和 whole M11 都已同时支付。

同理 `1,A,θA` 在 `C(t)` 上 independent：标准 irreducible 表示的 orbit differences `(ρ(g)−I)A` 张成二维齐次解空间，再用同一个 Wronskian 论证。此事实在 §6 用于检验 logarithmic product 的 forcing。

## 4. 不损失全 prime cap 的三次覆盖

采用一个明确的整数 polynomial 覆盖

\[
 t=1-(1+x)^3=-3x-3x^2-x^3,\qquad t(0)=0.                    \tag{M16}
\]

因为 `t(x)∈xZ[x]`，第 `x^n` 项只涉及 `t^j` 的 `j≤n`，`D_j²|D_n²`；所以 M10–M11 在 `x` 和 `θ_x=x d/dx` 的所有 fixed jets 中保持原 cap2。首导数 `−3` 无须倒置；本文从整数 polynomial composition 向这个方向证明，而不是从一个有分母的 inverse map 免费返回。

在 `t=1`，两个 homogeneous branches 为 `s^(1/3) a(s)`、`s^(2/3)b(s)`，无 logarithm，因为指数差不是整数。非齐次方程也有唯一 analytic particular `v(s)`：其 Taylor recursion 的 indicial value `−27n(n−1)−6` 在所有整数 `n≥0` 都非零，forcing analytic；regular‑singular Frobenius construction 保证收敛。M16 将 `s=−(1+x)³`，上述三种 branches 全变成 analytic functions of `x+1`。所以 `x=−1` 对全部实际 branches 的 affine monodromy 都消去，独立于 `u`：

\[
 T_{x=-1}(F_u\circ t)=F_u\circ t.                            \tag{M17}
\]

这不是只消去 leading fractional term，而是完整有限阶 local monodromy。另一个 point `σ` 的三个 preimages 是

\[
 x_j=\omega^j a-1,\quad a=(27/28)^{1/3},\quad\omega^3=1,
                                                               \tag{M18}
\]

全 unramified。只有沿 `0→a−1` 的实际 continuation 可直接使用 M6；不能把另外两点也标为 relation‑filled。`t=0` 的另外两个 preimages `ω−1,ω²−1` 仍可能有 cusp logarithms，infinity 也保留。

覆盖上的 actual rank3 仍成立。齐次 monodromy restriction 为有限指数 subgroup，仍含上述两 unipotents 的正幂，故 irreducible。若 pullback 的 particular 在 `C(x)` 有理，取 finite separable extension `C(x)/C(t)` 的 normalized trace；derivation `∂_t` 与 trace commute，于是产生 base 上的 rational particular，矛盾 M13。再作 M14–M15 的 cocycle/Wronskian 论证，即得

\[
 \dim_{\mathbb Q(x)}\operatorname{span}
 \{1,F_u(t(x)),\theta_xF_u(t(x))\}=3.                         \tag{M19}
\]

## 5. 标量 κ 是已知超越数；该模型不提供新的无理性定理

现有 archive 中 Rogers–Wan–Zucker，arXiv:1303.2259v2，PDF9–10 Theorems4–5，对完全相同的 `η³η(7·)³` 给

\[
 \kappa=\frac{8}{\sqrt{7^3}}k_{1/7}k'_{1/7}K(k_{1/7})^2
 =\frac{\Gamma(1/7)^2\Gamma(2/7)^2\Gamma(4/7)^2}{224\pi^2}.
                                                               \tag{M20}
\]

第一式取其 Theorem4 的 `r=1,s=7`；singular moduli `k_{1/7},k'_{1/7}` 非零 algebraic。不能把原件 PDF13 的 alternating lattice sum `Γproduct/(56π²)` 误当成 κ；κ 的 normalization 是224。该原件 authors 确为 Zucker，并非此处另一个常见姓名 Zudilin。

`K(k_{1/7})` 的非零 algebraic multiple 是 algebraic elliptic curve 的 period。Schneider 的 unconditional period transcendence，本文通过 Bertolin–Waldschmidt primary author manuscript PDF5–6，Theorem2.5/Cor2.6 的准确陈述支付：取 period 的非零 torsion division point，它的 `℘` 值 algebraic，而 Cor2.6 强制其 elliptic logarithm transcendental。因此非零 period、`K` 都 transcendental。如果 `κ` algebraic，M20 会使 `K²` algebraic，继而 `K` algebraic，矛盾。所以 κ 已知超越。这不是本轮的新数论结论。

从安全 CDT 账本也不能立即制造另一份新证明。M15 的三元组有一行整数常数和两行 cap2，即 `b` 是两个 `(0,1,1)^t` columns、`e=0`，所以原 CDT PDF66–69 的 `τ^♭=16/9`；二元组 `{1,F_u}` 则为 `τ^♭=3/2`。若只采用同一实际 branch 的 round‑disc map `φ(z)=Rz`，rank3 contradiction 要求 `log R>8/3`，rank2 要求 `log R>3`，来自 `m≤log R/(log R−τ)`。

即使形式上假设 `u=κ∈Q` 并使用 M6、M17，native branch 不能成为 entire function：其 infinity 为 regular singular，entire solution 会是 polynomial，与 M13 矛盾。native 唯一剩余 finite puncture 是 `t=1`，故 round-disc radius 至多1。覆盖上如全部 finite preimages 都 filled，regular singularity 同样会使 pullback rational，与 normalized trace 论证矛盾。因此至少一个未 filled preimage 在 M18 的另两点或 `ω−1,ω²−1`；其 modulus 均≤`√3`。所以覆盖的这个 round-disc 方案也达不到 `log R>8/3`。这只评价明确给出的 round discs，完全没有证明所有 uniformizing maps、多个 maps 或改进 §7–8 holonomy bounds 的一般 no‑go。

## 6. 跨权重 log2：一个有理 Taylor 但未 full‑filled 的具体反例

更有意义的 prospective scalar target 是 `1,κ,log2`。本文不声称它们已证明 independent，也不从 κ 与 log2 分别 transcendental 推 independent；更不把文献检索无结果当成未知性的证明。

最自然的试验是在同一 homogeneous carrier 上取

\[
 \ell(t)=\log(1+28t),\quad
 G_{u,v}(t)=B(t)-(u+v\ell(t))A(t),\quad u,v\in\mathbb Q.
                                                               \tag{M21}
\]

选择 `ℓ(0)=0` 的 branch。`ℓ` 的第 `n` coefficient 是 `(-1)^(n+1)28^n/n`，故这个试验确有 Q Taylor，且同 M10 的整数 convolution 给固定 common rational multiplier 下的全 `D_n²` 模型；还没有解释新的 puncture `t=−1/28`，不能把它从 continuation surface 删除。

在 `σ` 的小圆盘，`ℓ` analytic，`ℓ(σ)=log2`。M7 精确给

\[
 \Delta_\sigma G_{u,v}
 =(\kappa-u-v\ell(t))\Delta_\sigma A.                        \tag{M22}
\]

`Δ_σA` 非零：modular weight1 continuation 的 `W_7` 行为将 `A` 送到一个非零 constant multiple of `τA`，不能 identically 等于 `A`。M12 的 exponents `(0,1/2)` 于是给 `Δ_σA=s^(1/2)c(s)`、`c(0)≠0`。即使假设真正 scalar relation `κ=u+v log2`，若 `v≠0`，M22 仍为

\[
 \Delta_\sigma G_{u,v}
 =-14v\,c(0)s^{3/2}+O(s^{5/2})\ne0,\qquad s=t-\sigma.
                                                               \tag{M23}
\]

因为 `ℓ'(σ)=14`。因此只消去原 `s^(1/2)` leading term，未付 full local jump。这个结论与有理 Taylor、全有限处 cap 均相容，是一个具体 ansatz 的严格失败，不是不存在任何跨权重 relative period 的 theorem。

同一失败更一般地适用于 `C=A log R`，其中 `R∈C(t)^×` 非constant，`R` 在 `σ` 非零无极点，局部选择 analytic logarithm。要让 `Δ_σC=log R(σ) Δ_σA` 在全部 germ 上成立，需要 `(log R(t)−log R(σ))Δ_σA≡0`，因此 `R` locally constant，矛盾。若 `R'(σ)=0`，只把剩余 fractional exponent 延迟，并不会令它消失。

还可以独立检查 forcing：若 `ℓ=log R`，则

\[
 L(A\ell)=2p_2\ell' A'+(p_2\ell''+p_1\ell')A.              \tag{M24}
\]

因 `ℓ',ℓ''∈C(t)`、§3 已证 `1,A,A'` independent，如果 M24 是 rational function，必有 `2p_2ℓ'=0`，进而 `R` constant。所以这类 nonconstant product 连 same‑L rational inhomogeneous forcing 都没有，不能称其为已经构造好的同载体 algebraic normal function。

## 7. 下一相对周期的精确任务，而非自动几何推论

要在这个低维载体上真正测试 `1,κ,log2`，所需新对象可以清晰写为一个 `C(t)`：其 `t=0` germ 属于 `Q[[t]]`，有已证全有限处 cap；有 rational forcing `LC=r_C∈Q(t)` 和确定初值；且在相同 conifold normalization 下

\[
 \Delta_\sigma C=\log2\,\Delta_\sigma A.                    \tag{M25}
\]

这样 `B-uA-vC` 的完整 σ‑jump 才恰为 `(κ-u-v log2)Δ_σA`。除此之外，仍须证明所有其它 loop 的实际 comparison、允许的 relative cycle 或 normal‑function lift、整数 Betti/de Rham 标记、由新增 forcing/singularities 导致的 holonomy 和 integrality 账本。本文没有给出 `r_C` 或这种 `C`，M25 是具体尚待实现的任务，不是 existence assertion。

GKS 原件 PDF16–17 的 Remark4.7 精确要求 `ANF(H)→Hg(H¹(U,H))`，其 geometric origin 另外要求(4.6–8)的 higher Chow/motivic class；PDF18–22 的 tempered coordinate‑symbol 与 relative cohomology 构造也有独立的 hypotheses。故 M3–M5 的 affine Eichler extension 虽真实存在，有理 differential equation 和 Q Taylor 本身并未证明一个指定 Tate quotient 的 rational Betti/Hodge comparison，更未证明一个 cycle。Paşol–Popa PDF1–4 的 period polynomial/cocycle formalism明确保留 cusp cohomology；不能因 modular parameter 是 genus0 就把实际 cusp period class 抹掉。本文不宣称该 level‑7 carrier 有无某种完整 motivic realization的通用否定结论。

同样，Bertolin–Waldschmidt PDF5 的 semi‑elliptic logarithm algebraic independence 为 **Conjecture2.4**。将它应用于 nonzero period 的 torsion division point与 `log2` 可预期更强结论，但本文不使用该 conjecture 作新 LI 的证明。M20 的 κ 超越只使用标清为 theorem 的 Schneider statement。

本轮的可复用实质是 M10–M11（同 `t` 坐标全部 primes）、M13–M15（真正 rank3）、M16–M19（整数 cover 的完整有限 monodromy 消去与 rank 保持）、M22–M24（具体跨weight product 失败）以及 M25（准确 whole‑jump 下一目标）。没有新的特殊值无理性、LI 或 Lean 定理；没有重复 old level12/20、R0 的 cycle 证明。

## 8. 实际来源与阅读域

网页检索于2026‑10‑07进行，涉及 primary 作者稿/期刊原件的 modular normal functions、Eichler integrals、inhomogeneous Picard–Fuchs、period transcendence 与低weight目标；作者 GitHub 的 `1,ζ2,ζ3` repository 已被本项目旧记录讨论，本文不把它作为本轮新发现。没有用非primary摘要作为技术论据。以下阅读范围仅声明本轮实际全文的相应页，未继承其它 agent 的阅读。

- [Yang, Apéry limits and special values of L-functions, fixed v1](https://arxiv.org/abs/0709.1968v1)：复用 [原件](../literature/yang2007_apery_limits_v1_20261006.pdf)，24物理页；本轮实际全文 PDF1–18，其中5–6和15–16又实际回读。M1–M6采用 actual operator/forcing，未沿用其它例子中 printed recurrence 的系数。本轮发现 Example1、Example3 的 displayed equations 含729、256，而 Theorem1、Theorem3 的 printed last recurrence coefficient 缺相应因子；本稿不依赖那些 printed recurrences，不修改原件。
- [Beukers, A note on the irrationality of ζ(2) and ζ(3)](https://www.numdam.org/article/AST_1987__147-148__271_0.pdf)：复用 [原件](../literature/beukers1987_modular_irrationality.pdf)，14物理页；实际 text PDF1–7，旧扫描的若干公式 OCR 不清，没有声称逐式视觉复核；仅作已有 Apéry/modular mechanisms 的背景去重。
- [Rogers–Wan–Zucker, Moments of elliptic integrals and critical L-values, v2](https://arxiv.org/abs/1303.2259v2)：复用 [原件](../literature/rogers_wan_zucker2013_moments_elliptic_critical_l_values_v2.pdf)，15物理页、211886bytes、SHA `b5d3b4bbbb4fdc926ffe2002d7a50247926ec1336f97de3455d0b061bf0153b8`；实际全文 PDF1、8–14（8个不同页）。Theorems4–5在9–10，lattice normalization 在12–13。
- [Golyshev–Kerr–Sasaki, Apéry extensions, v3](https://arxiv.org/abs/2009.14762v3)：复用 [原件](../literature/golyshev_kerr_sasaki2023_apery_extensions_v3_20261006.pdf)，35物理页；实际全文 PDF1、14–22（10个不同页）。一次对全部 matching pages 的长输出被截断，本文不把截断部分算为 actual FULL 阅读。
- [Paşol–Popa, Modular forms and period polynomials, v5](https://arxiv.org/abs/1202.5802v5)：复用 [原件](../literature/pasol_popa_period_polynomials_20261006.pdf)，32物理页；实际全文 PDF1–4。
- [Kerr, Three vignettes on hypergeometric normal functions, v1](https://arxiv.org/abs/2602.04128v1)：复用 [原件](../literature/cdt_period_extension_sources_20261007/kerr2026_three_vignettes_arxiv2602_04128v1.pdf)，25物理页；本轮只实际全文 PDF1，未将其其它页的几何结论当作新输入。
- [CDT固定原件](../literature/cdt2024_l2_chi_minus3.pdf)：本轮 actual FULL PDF66–69，4页，用于明确 §5 的同对象 denominator rows 与 round‑disc 界，未声称本轮全文218页。
- [Bertolin–Waldschmidt, Variations on Schanuel’s conjecture for elliptic and quasi‑elliptic functions I, author manuscript dated2025‑12‑16](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Semi-Elliptic-Schanuel.pdf)：本轮唯一新归档 [原件](../literature/cdt_gamma_modular_relative_sources_20261007/bertolin_waldschmidt2025_split_semi_elliptic_author.pdf)，20页、478905bytes、SHA `da8859a50282c5e87bd99b5b15ee38c7296d980628fb46a364f03f109b3540e1`；本轮 actual FULL PDF1–6。使用已知 Schneider Theorem2.5/Cor2.6，明确不把 conjectures2.1、2.4、2.8视为 proved。正常 TLS 下载 HTTP200；保存前对 authority 的全部135个 prior PDF records 作 identifiers 和完整 SHA 比较，均无重复。

Schneider1937旧 DigiZeitschriften PDF 地址本轮请求返回404，Springer DOI `10.1007/BF01571618` 为 subscription metadata，没有存为假 PDF，也没有绕过 TLS 或权限。新归档仅1个PDF20页；本稿 own distinct local PDF reading 总计58页（18+7+8+10+4+1+4+6），无 render、数学 producer 或 prime table 执行。主报告旧摘要实际读取范围与后续同行正式独审会另在最终 receipt 如实记录。
