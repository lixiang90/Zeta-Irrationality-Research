# 第258轮：唯一 DD/KZ 候选的完整族准入否决

2026-10-10。固定唯一候选为 OpenAI 数学仓库当前 `The-Deligne-Drinfeld-conjecture-September-23-2026` 的 KZ/regularized holonomy 机制，weight 截断固定为 ≤7，数值目标固定为 ζ(7) 的无理性。假设关系固定为 ζ(7)=r∈Q；不更换目标、参数、sheet word、基向量窗口或截断权重。本轮只作有限来源 gate，不构造 Padé/determinant producer。原 goal 保持 active，newnumeric=false。

**决定：拒绝该候选作为258数值出口。** 真实 endpoint period 已识别；函数独立性和一个全前缀算术模型可明确支付，但假设 ζ(7)∈Q 不改变所固定完整族在0/1处的任何完整非meromorphic residue 跳跃，不能扩大该族共同单值 meromorphic 域。DD 的 rational descent 是有限有理方程空间的换标量，不是原 period 值的有理化。此结论不宣称全 KZ 方法、其它实际 quotient 或 ζ(7) 的一切路线不可能。

本轮直接重读当前 primary，未继承255的 FULL 标签。一般性的“DD Lie freeness 不等于数值独立”属于已有警告的重证，不能记新进展。本稿新增的可复用数学资产只限于下面的完整有限族、有限分歧不消跳跃引理及其针对固定 ζ(7) 的明确 gate；它们不是新数值结果。

## 1. 原文究竟交付什么

当前 primary 路径：

- `E:/codex-build/math/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/build/sections/01-introduction.tex`；
- 同目录 `07-holonomy.tex`、`08-induction.tex`；
- 同目录 `06-category.tex` 的 Lemma “Rational finite data” 完整命题和证明，lines190–238（含前文所需评价接口174–188）。

公开载体为 [DD preprint source](https://github.com/openai/math/tree/main/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026)。本轮证据来自本地当前源码，网页未作为阅读全文替代物。

原文的真实数值 identity（`eq:holonomy-zeta-integral`、`eq:holonomy-nonzero-odd`）在 λ=(2πi)^{-1}、dg=Ωg 的次序约定下是

\[
[x^6y]\Phi=-\lambda^7\zeta(7),\qquad
[x^6y]\delta_7(\alpha)=2\lambda^7\zeta(7)\ne0. \tag{A1}
\]

它来自真实收敛 integral

\[
-\frac{\lambda^7}{6!}\int_0^1\frac{(-\log t)^6}{1-t}\,dt
=-\lambda^7\zeta(7). \tag{A2}
\]

positivity 只给非零；原文在该命题证明的末段明确说不使用 arithmetic independence。`06-category` 的 descent 给

\[
\mathcal D_7(\mathbb C)=\mathcal D_7(\mathbb Q)\otimes_{\mathbb Q}\mathbb C.
\]

若一个 Q-linear functional 在某个 complex vector 上非零，就在某个 Q-vector 上非零。这不要求、也不证明这个 Q-vector 与 δ₇ 的 functional 数值相同。写 δ₇=Σc_jv_j 只知某个 functional(v_j)≠0，不知 functional(δ₇)∈Q。对(A1)尤其如此：2λ⁷ζ(7)是非零纯虚数，根本不可能等于某个非零 Q-coefficient。即便假设 ζ(7)=r∈Q，λ⁷r 仍不是被原文“descent”变成同一数值的有理数。

`08-induction` 的 saturated Z_(2)-lattice、mod2 Hall-word independence、全 weight Lie generation 针对 formal vectors。它未给所有有限 primes 和 archimedean heights 的完整数值 LCM 数组，也未声称 ζ(7) 的无理性。数学的 braid holonomy isomorphism 与 CDT 的 arithmetic holonomy rank inequality 是不同接口。

## 2. 固定完整载体和拟扩大域

完整 primary transport 固定为

\[
\mathcal A_7=\mathbb C\langle x,y\rangle/(\text{words of weight}>7),
\quad\dim\mathcal A_7=1+2+\cdots+2^7=255,
\]

\[
dg=\lambda\left(x\frac{dz}{z}+y\frac{dz}{z-1}\right)g. \tag{A3}
\]

包含全部255个 word coordinates，不只保留被提取的 x⁶y coefficient。0/1处 local residues 是 N₀=λL_x、N₁=λL_y（L 为左乘算子）。两者均 nilpotent，且非零，因为 L_x(1)=x、L_y(1)=y。这是固定 weight≤7 的全部系统，不靠增 weight 领取新 rank。

起始共同单值域可取

\[
D_0=\mathbb C\setminus\bigl(( -\infty,0]\cup[1,\infty)\bigr)
\]

及其正实路径 tangential endpoint normalizations。拟扩大域明确要求填入 z=1 的一个 punctured disk，或在 z−1=t^e 的某个有限 cover 上使全部 coordinates meromorphic 穿过 t=0；0处同理。单纯沿 slit 解析继续、改画 branch cut 或改用 universal cover 不算此种共同单值 meromorphic 域增益。

为了不以255个 universal coordinates 冒充目标的“最小族”，另固定真正承载(A2)的最小 scalar 微分和 monodromy 族

\[
\mathcal B_7=\{1,\ L^j/j!:1\le j\le6,\ \operatorname{Li}_k(z):1\le k\le7\},
\qquad L=\log z. \tag{A4}
\]

其 rank 恰14。这里用 λ^{-weight} 还原 word coordinates 的尺度，故 [x⁶y] 的 unscaled function 是 −Li₇(z)，其真实 endpoint value 是 −ζ(7)。没有删去低 weight boundary channels；完整 Li₁,…,Li₇ 和六个 log channels 都保留。这个 scalar carrier 与完整 universal carrier 的层次区别固定，不互换算术结论。

## 3. 自含引理：可逆换基和有限分歧不消完整 nilpotent 跳跃

**引理A。** 设一个 regular-singular complex system 的某处 local monodromy 共轭于 exp(2πiN)，其中 N 是非零 nilpotent 算子。任意可逆 constant 换基、单值可逆 meromorphic gauge 和有限局部 ramification z−a=t^e（整数e≥1），都不能使其完整 fundamental matrix 在该处单值 meromorphic。

**证明。** 换基只把 local monodromy 共轭。单值 gauge 的绕行前后值相同，故亦只共轭。在 e-fold ramification 后，local monodromy 是 T^e，亦即共轭于 exp(2πieN)。nilpotent exponential 和 unipotent logarithm 是有限多项式且互逆；若 exp(2πieN)=I，则 log 给 2πieN=0，在 characteristic0 与 e≥1 下推出 N=0，矛盾。完整 meromorphic fundamental matrix 是单值的，必有 identity monodromy。证毕。

对(A3)，T₀、T₁分别共轭于 exp(2πiN₀)=exp(L_x)、exp(2πiN₁)=exp(L_y)，故此引理直接适用。这里可直接核local normal form：写connection为N/u+A(u)，寻H(u)u^N时，H的第k阶递推算子为kI−ad_N；ad_N nilpotent，故所有k≥1的算子可逆，且其有限Neumann公式对大k为O(1/k)，给收敛holomorphic invertible H。因而没有免费假设resonant gauge。endpoint associator Φ 及其 rational/complex 可逆 basis 变化不改变这个 conjugacy invariant。**只在 endpoint 标量之间假设 ζ(7)=r，并没有修改(A3)的 residues。** 把同一系统写到另一 rational basis 不可能消掉非零 N。

该引理不排除真正 quotient：若 quotient 上 N 为零，该 quotient 可填该点。然而准入者必须证明 actual period projection、完整微分/monodromy 闭包以及目标 ζ(7)仍留在 quotient 中。直接令y=0会丢掉 x⁶y；它不能作为当前目标的无费用修复。

## 4. 同一真实 scalar 目标的反证、独立性和极小性

在 D₀ 上取标准 Li_k germs。它们满足

\[
\operatorname{Li}_1=-\log(1-z),\quad
\operatorname{Li}_k'=\operatorname{Li}_{k-1}/z\ (k\ge2),\quad
(L^j/j!)'=L^{j-1}/((j-1)!z). \tag{A5}
\]

绕1一圈（正向，不绕0）时

\[
\Delta_1\operatorname{Li}_k=-2\pi i\frac{L^{k-1}}{(k-1)!},\qquad
\Delta_1L=0. \tag{A6}
\]

由 Li₁ 的 logarithm 先得 k=1；(A5)逐层积分给(A6)，k≥2时以 z→1 的 jump 趋0确定 integration constant。没有丢任意 endpoint constant。

特别是固定假设 ζ(7)=r∈Q 所制造的唯一直接目标函数

\[
H_r(z)=\operatorname{Li}_7(z)-r
\]

仍有

\[
\Delta_1H_r=-2\pi i\frac{L^6}{6!}\ne0. \tag{A7}
\]

该函数在1附近含非零 (z−1)⁶log(1−z) 型项；减去 endpoint constant 仅改变 regular constant term。有限分歧绕行 e 次将(A7)乘e，仍不为零。绕0时log channels发生 L→L+2πi；同样无法由 r 消去。因此(A4)的共同 nonmeromorphic local monodromy 未变，拟填入的 puncture 不准入。即使只看目标 H_r 而不看完整族，(A7)也已拒绝这个具体 subtraction。

**函数独立性。** 若一个 C(z)-linear relation 连结(A4)，绕1取差，(A6)给有理函数系数的 L 多项式等于0。L的各次幂在 C(z) 上独立：绕0任意整数次将 L 平移2πik，在一个普通点得到无穷多个根；故 polynomial coefficients全为0。因而 relation 的所有 Li coefficients全为0，再由同一论证去掉全部log coefficients。故 rank=14。这只是函数独立，未推出 endpoint 数值独立。

**极小性。** 任何包含 Li₇、对 C(z)-微分和全部 local monodromy 封闭的空间，由(A5)必须包含 Li₆,…,Li₁,1；由(A6)必须包含L⁶，逐次微分又包含L⁵,…,L。因此必须包含(A4)全部14个独立元素。(A4)本身在(A5)、(A6)与0处 L 平移下封闭，所以是该目标的最小完整 scalar carrier。这个证明使“只留 Li₇ endpoint 值而省去其 monodromy closure”不再可行。

## 5. 全前缀算术费用：已付与不能偷付的部分

设 d_H=lcm(1,…,H)，ψ(H)=log d_H，H≥1。在 origin 的完整 regular-singular formal model Q[[z]][L] 中，(A4)的所有 z^m L^j coefficients（0≤m≤H）由

\[
q_H^{\mathrm{min}}=\operatorname{lcm}(6!,d_H^7) \tag{A8}
\]

同时且精确清整。理由是 Li_k=Σ_{m≥1}z^m/m^k；Li₇已强制 lcm(m⁷:m≤H)=d_H⁷，而 L^j/j! 的全部 denominators强制6!。所以对所有 primes包括2和所有 prime powers，

\[
v_p(q_H^{\mathrm{min}})=\max\{v_p(720),\ 7\lfloor\log_p H\rfloor\},
\quad
\log q_H^{\mathrm{min}}=7\psi(H)+O(1). \tag{A9}
\]

这是每个完整 prefix 的证书，不是只清第H个 coefficient。H≥5时 q_H^{min}=d_H⁷。若只为标准比较用PNT，则 leading 是7H+o(H)，无需PNT也有(A8)–(A9)的精确费用。

对全部255-word universal carrier，在 λ^{-weight} 的 unscaled formal model 中，安全全前缀模型为

\[
q_H^{\mathrm{full}}=7!d_H^7. \tag{A10}
\]

一个 word 若右端是y，其 Taylor coefficient是相应 multiple-polylog finite nested sum；每个 denominator中的整数≤m≤H，分母总次幂≤7，故 d_H⁷清整。含右端x的word，以shuffle移去末端x，化为这些analytic words与 L^j/j! 的整数组合；任一所产生的 factorial产品总weight≤7，均整除7!。纯x word亦包含。由此(A10)覆盖全部词、全部有限头和全部prime powers，而不是只覆盖depth-one coefficient。没有声称该安全模型最优。

这里要区分两个未付接口：

1. **log-Taylor model不是CDT的普通 Q[[u]] germ。** L 在0不全纯。把完整族搬到普通点 z₀≠0,1 后，展开常数含 logz₀、Li_k(z₀)与其它真实 iterated-integral periods；假设 ζ(7)=r没有使它们全部有理。若提出新的 rational relation敏感germ，必须实际证明其全部coefficients和每个prefix的算术模型，不能把(A8)原封贴过去。
2. **完整 endpoint 矩阵不因一个关系成为Q矩阵。** origin formal coefficients有理与regularized endpoint periods有理不同；完整carrier还保留其它weights/depths的数值。DD 的 Z_(2)-lattice只支付formal vector的2-local saturation，没有给同一数值评价的全处product-formula费用。

最小族的analytic部分 {1,Li₁,…,Li₇}（8个普通Q[[z]] germs）可用共享 d_H⁷ prefix数组；它仍保留Li₁在1的非meromorphic logarithm，因此亦无关系敏感填点。它不是拿来替换完整14族领取新的map/rank，而是说明即便普通Taylor算术已经存在，ζ(7)=r仍不产生所需域增益。

## 6. 所需 strict、Catalan 的不同机制与最终 gate

若后续提出真正 ordinary Q[[u]] 的完整关系族，CDT准入仍须在同一对象上支付线性独立、完整LCM数组和合法共同meromorphic pullback φ。记 λ_map=log|φ′(0)|、J为原双圆周均值、τ为完整数组的加权type，必须有

\[
\lambda_{\rm map}>\tau,
\qquad m(\lambda_{\rm map}-\tau)>J \tag{A11}
\]

才能与rank bound矛盾。不能只给 λ_map−τ>0 或Lie-theoretic nonzero。共享 d_H⁷数组的安全type是7；该数组下需要 λ_map>7 且 m(λ_map−7)>J，最佳flags若降低τ须另付。当前完整14族在0连ordinary-germ入口都未付，不用m=14套(A11)。同一prefix clear-model若构造r_det阶非零 rational determinant并按 q_H^{r_det}整化，则须有真实archimedean decay超过7r_detψ(H)+O(r_det)，留严格正余量；关系自身固定denominator亦须按实际次数另计。本轮没有构造这种量或领取非零。这是特定clear-model的要求，不是所有KZ方法的下界。

本次假设关系的实际 local domain gain 是0；未给任何新 φ、τ改进或J预算。不得把(A11)缺口用抽象Q-vector、增weight、universal cover或其它目标填补。

直接重读的 Catalan `foundations.tex`、`conclusion.tex` 提供了**不同**出口：固定n=48N及完整rows/filter后，contact取消ζ(2)，完整moment pool落 Q+QG；G∈Q使同一Δ_N∈Q。其rational hypothesis未改变 f(t)=√(1−t²)的branches或integral carrier，只为valuation/product formula打开入口。当前primary有限处接口为

\[
\liminf\left(\frac{\log|\Delta_N|}{n^2}-\tfrac12\log2\right)
\ge-\frac{8609}{4608}-\left(\frac12+\frac{505}{4608}\right)\log2
>-2.29084;
\]

conclusion在同一nonzero prime sequence调用真实upper <−2.2909，strict安全差大于0.00006。这个strict属于原G=β(2)的固定完整determinant及其全素点损失；本轮只读接口，未重新认证其fixed matrices、odd-prime全证明或energy数值表。不能将其移植到ζ(7)、β(4),β(6),…，也不能把claimed Catalan theorem当所有β偶值的结论。

**有限 gate 汇总：** (A1)–(A2)真实period通过；(A4)完整最小族与function independence通过；(A8)–(A10)origin的全部log-Taylor prefix费用通过；“一个数值有理关系使全部非meromorphic local monodromy消失”由(A7)/引理A明确失败；共同单值meromorphic域增益失败；ordinary-germ/全数值处算术/CDT strict未付。故不准入，停止该唯一候选，不以本稿作为再开DD/KZ窗口理由。

本轮不重开257 χ−8 monomial prototype，不运行数学程序、Lean、有限n证书、参数/maps/primes/sheetwords扫描或旧producer。未fetch/reset/checkout/写外部数学仓库；未修改main、policy、manifest、旧研究稿或goal状态。
