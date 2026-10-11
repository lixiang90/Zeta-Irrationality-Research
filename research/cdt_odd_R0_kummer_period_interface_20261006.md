# R₀ 的真实有理周期、Kummer forcing 与局部扩张区别

日期：2026-10-06。NEW 全尺度证明和一手文献核查。只读冻结 H、P₄、M₄ 输入；未执行或 import 冻结/同行数学 producer。本文没有数值无理性、完整整 Betti 格或 Lean 定理。

## 1. 固定对象与本轮结果

固定 θ=x d/dx，P₄=θ⁴−x(θ+1/2)⁴，以及冻结的实际函数

\[
 H(x)=\pi^2\sum_{n\ge1}\frac{\Gamma(n)^4}{\Gamma(n+3/2)^4}x^n,
 \quad ((\theta+1/2)^4-x\theta^4)H=16x.
 \tag{R1}
\]

令

\[
 r(x)=\sum_{n\ge0}\frac{\Gamma(n+1)^4}{\Gamma(n+3/2)^4}x^n,
 \qquad B(x)=\frac{\pi^2}{16}r(x)
 ={}_5F_4(1,1,1,1,1;3/2,3/2,3/2,3/2;x).
 \tag{R2}
\]

B 的系数 bₙ=[(1)ₙ/(3/2)ₙ]⁴∈Q，b₀=1。本文证明：

\[
 \boxed{B(x)=1+\frac{\theta^4H(x)}{16},\quad
 K_BB=\frac1{16},\quad K_B=(\theta+1/2)^4-x(\theta+1)^4.}
 \tag{R3}
\]

在正实分支定义 W=√x B、ν=√x r，则

\[
 \boxed{P_4W=\frac{\sqrt x}{16},\quad
 P_4\nu=\frac{\sqrt x}{\pi^2},\quad
 (\theta-1/2)P_4W=0.}
 \tag{R4}
\]

端点 r(1)=R₀；故 B(1)=π²R₀/16。本轮的新内容是正确的全函数扩张接口及局部障碍，不重复先前 M₁–M₃ 校准。

## 2. 全尺度递推及原 H 接口

Gamma recurrence 给 n≥1

\[
 (n+1/2)^4b_n=n^4b_{n-1}.
\]

K_B 的非首项逐项消去，首项 (1/2)⁴b₀=1/16，得到 R3 第二式。并且对 n≥1，R1 的 hₙ 与 bₙ 满足 n⁴hₙ=16bₙ，故直接逐系数得到 R3 第一式。亦可先用 R1 得 [(θ+1/2)⁴H]/x=16+θ⁴H，再辨认其系数。式中除以 x 在 x=0 可去，未改变实际 germ。

乘 √x 的共轭恒等式为 P₄(√x f)=√x K_B f，故 R4 精确成立。这不是用端点的 M₄=56π⁴M₀−24π⁴R₀ 猜测全函数相等；B 与 H 的关系是实际 differential contiguity，而 ν 与 Z₄ 是不同的扩张。

## 3. 收敛有理积分，保留 π 的规范

对 m≥1，Euler beta 积分及 t=1−u² 的代换给

\[
 \frac{\Gamma(m)}{\Gamma(m+1/2)}
 =\frac2{\sqrt\pi}\int_0^1(1-u^2)^{m-1}\,du.
\]

正项求和可用 Tonelli/单调收敛，|x|<1 则可用一致可和的几何级数。因此

\[
 \boxed{B(x)=\int_{[0,1]^4}
 \frac{du_1du_2du_3du_4}{1-x\prod_{j=1}^4(1-u_j^2)},\quad
 B(1)=\frac{\pi^2R_0}{16}.}
 \tag{R5}
\]

端点的唯一实立方体奇点是原点。写 A=∏(1−uⱼ²)，则 1−A≥max uⱼ²≥(Σuⱼ²)/4；4/(Σuⱼ²) 在四维原点可积，故 R5 在 x=1 是真正有限的 period integral。对 x∈(0,1]∩Qbar，B(x) 是代数有理微分形式在代数半区间上的绝对收敛积分。本文只把 B(1) 称为这种周期；R₀ 包含除 π² 的规范，不能仅由 R5 宣称其未归一化数值也是通常意义的 Kontsevich–Zagier period。

等价的 inverse-binomial 规范为

\[
 \pi^2R_0=\sum_{m\ge1}\frac{256^m}{m^4\binom{2m}{m}^4}.
 \tag{R6}
\]

这来自 Γ(m)/Γ(m+1/2)=4ᵐ/[m√π binom(2m,m)]。它不同于三变量 Mahler measure 的一般 5F₄ 对数公式，不能只凭级数阶数相同套用。

## 4. actual rank5 与非分裂

本节使用冻结 [spin 主稿](cdt_odd_classical_spin_pullback_20261006.md) §3 的绝对不可约 rank4 输入（已校准的 Sp₄ 齐次系统），不重跑其 producer。K_B 与 P₄ 相差 √x 的 rank1 twist，故其齐次四维层也绝对不可约。

K_B f=1/16 没有 rational particular f∈C(x)。证明：x=0 的齐次 indicial 为 (ρ+1/2)⁴，x=1 与 P₄ 同为 exponents 0,1,1,2，其他有限点 ordinary；若 rational particular 有有限极点，其最负幂必产生非零最负阶 homogeneous indicial 系数，不能匹配常数 forcing。因此 f 没有有限极点，只能是 polynomial。最高项 a_d xᵈ 在 K_B f 中产生 −(d+1)⁴a_d xᵈ⁺¹，永不消失，矛盾。

所以 θK_B 的实际扩张不分裂：若分裂存在一个全局常数 quotient 的 flat lift，它给一个单值 particular。Fuchsian 方程的单值 moderate-growth 解在全部 punctures 都 meromorphic，因而是 rational，已排除。此处使用的只是 regular singular 解的有限幂/log 展开，未把所有解析 particular 当作 rational。

实际 B 的最小标量阶数也恰为5。其 continued branches 的差属于 K_B 的四维 homogeneous 层；若所有差皆零，上述单值论证使 B rational，矛盾。因此出现一个非零 homogeneous 差；绝对不可约性使这些差的 monodromy span 等于整个四维层，再加 particular B 得5维。θK_B 给阶数≤5，于是等号成立。同理 W 的最小阶数为5，R4 扩张不分裂。没有把一个端点闭式或候选 regulator 关系换算成 rank 下降。

## 5. 局部 monodromy：不能从 M₄ 端点移植扩张

K_B 在 x=0 的 homogeneous 根为 −1/2 四重，canonical logarithmic chain 给 J₄(−1)；B 的实际 Taylor particular 是单值。因此 θK_B 的 local0 monodromy 为

\[
 T_0(B\text{ extension})\simeq J_4(-1)\oplus(1).
\]

乘 √x 后，P₄ 的四维 homogeneous block 为 J₄(1)，W 的 √x Taylor particular 自身绕0变号，不带额外 log，故

\[
 \boxed{T_0(W\text{ extension})\simeq J_4(1)\oplus(-1).}
 \tag{R7}
\]

冻结的 Z₄ 满足 P₄Z₄=24π²，其 θP₄ 扩张在0为 J₅(1)。两者即使都取秩5，也不可能作为这个基上的 local systems 同构；特征值及 Jordan length 都不同。双覆盖 x=u² 后，R7 变 J₄(1)⊕(1)，Z₄ 仍 J₅(1)，所以仅加该平方根覆盖也不能识别扩张。全局非分裂与 local0 分裂完全可以同时成立。

这明确限制下一步：本 R₀ 的 √x forcing 有 Kummer quotient；必须找与该 quotient、实际源规范和 boundary cycle 相匹配的 geometric normal function。BGK 的 pure/mixed period 矩阵或 Z₄ 的 constant forcing 不自动给此数据。本文尚未证明 W 来自哪条具体 algebraic cycle，故只称它为 normal-function comparison interface，未称为已构造的 admissible geometric normal function。

## 6. 有理端点假设不允许填 conifold

一致 Stirling 给 rₙ=Γ(n+1)⁴/Γ(n+3/2)⁴=n⁻²+O(n⁻³)。设 sₙ=(n+1)⁻²，则 Σ n|rₙ−sₙ|<∞，因此 r(x)−Li₂(x)/x 的一阶导数在实 x→1⁻ 有有限极限。直接微分 Li₂(x)/x 得

\[
 r'(x)=-\log(1-x)+O(1),\quad
 B'(x)=-\frac{\pi^2}{16}\log(1-x)+O(1).
 \tag{R8}
\]

积分得到 t=1−x→0⁺ 时 r(1−t)=R₀+t log t+O(t)。即使 B(1) 或某个已归一化端点是假设有理，减去该常数仍保留 R8 的非零发散，不能成为 x=1 的 holomorphic germ。因而 rational endpoint 本身不赋予 CDT 解析叶一个可填 conifold；需要真正取消整个 vanishing/log branch 的 homogeneous correction，并逐周期核算其系数及完整整格。

### 6.1. 正的完整 log 投影：实际 holomorphic correction

冻结 spin 主稿 §3 的四阶 Levelt 矩阵给 T₁=A⁻¹B，T₁−I 非零秩1、平方为0；这是四阶 conifold 的 transvection 输入，不与 primitive 五阶的 Jordan(2,2,1) 混用。定义 y₀=Σ[(1/2)ₙ/n!]⁴xⁿ，M₀=π²y₀(1)。则有真正的全 branch 结果

\[
 \boxed{\nu(x)-\pi^2y_0(x)\ \text{在 canonical }x=1\text{ 分支全纯},
 \quad [\nu-\pi^2y_0](1)=R_0-M_0.}
 \tag{R9}
\]

证明 local forcing 没有新 log 层：P₄ f=√x/π² 在1的 source 全纯。以 t=x−1 写 P₄，作用于 t^ρ 的最低项为 −ρ(ρ−1)²(ρ−2)t^(ρ−3)；取 f 的0、1、2阶系数全为0，便可从 n=3 起逐项递推 source 的每个非负次幂，因为 −n(n−1)²(n−2)≠0。regular singular Frobenius 的收敛性给一个真正 holomorphic local particular f（起于 t³），不只是 formal 级数。故 ν−f 属于 P₄ 齐次四维层；其所有非全纯项都在同一个 rank1 conifold log block，且其余 local exponents 非负，不含 poles。

再由 aₙ=[(1/2)ₙ/n!]⁴=1/(π²n²)+O(n⁻³)，同 R8 的可和导数比较得 y₀ 在实 t=1−x→0⁺ 的 t log t 系数为1/π²。ν 的系数则为1。y₀ 的 log 投影非零；rank1 transvection 使 ν 与 y₀ 的全部 log 部分之比由这个首个非零系数确定为 π²。于是 R9 取消的是整个 local log series，不只是首项。取合法边界值给第二式。

在 rational-Taylor 规范中，R9 是

\[
 W(x)-\frac{\pi^4}{16}y_0(x)\quad\text{在1全纯},
 \qquad [W-\pi^4y_0/16](1)=\frac{\pi^2}{16}(R_0-M_0).
 \tag{R10}
\]

这个正接口比减常数更强，但 homogeneous coefficient 为 π⁴/16∉Q（π 的超越性已知），未得到 rational-initial full model；不能把该 correction 的解析改善免费记入原 CDT 模型。R9/R10 给下一步 regulator/chain 规范一个明确的目标，尚未证明其端点是某个 modular L-value 或几何 cycle 的 regulator。

## 7. 本轮新增一手文献及准确作用域

固定原件、页数、SHA256、实际阅读范围与不适用事项见新 [manifest](../literature/manifest_cdt_odd_R0_normal_function_20261006.json)。三个新 PDF 的下载均使用 curl 的系统 TLS 验证，无证书绕过；未执行其附属外部程序。

1. [Golyshev–Kerr–Sasaki, Apéry extensions, arXiv2009.14762v3](https://arxiv.org/abs/2009.14762v3)，2023-07-10，35页。实际读 PDF1–4、18–21、24–25。PDF4 Theorem1.1 的已证目标是五个 Mukai Fano threefold 的 Apéry constants；PDF19 (4.17) 从 relative integral 到 regulator 配对保留 relative periods 且要求实际 cycle 不碰 fibre，temperedness 才进一步控制纯层。PDF24 Theorem5.1 在真实 admissible NF、指定 Hodge line 和 monodromy 假设下界定 forcing 多项式次数；它没有断言任意 inhomogeneous PF solution 都来自 cycle。PDF25 Problem5.3 要求 normal conifold type、temperedness/相关 conjecture 和唯一 branch 规范。本 R5 的实积分是可用入口，但必须独立构造相应 pair/cohomology、cycle 和恰当 source quotient 后才能套用这些结果；没有完成此工作。
2. [Walcher, Calculations for Mirror Symmetry with D-branes, arXiv0904.4905v1](https://arxiv.org/abs/0904.4905v1)，42页。实际读 PDF4–6、9–19。PDF9–11 的链积分、curve orbit/stabilizer、Griffiths–Dwork residue 与 moving-chain 项一起决定 source；相同 source 仍须 boundary conditions 校准可加 homogeneous periods。PDF13–14 的 bicubic 与 PDF15–19 的 quartic/sextic complete intersections 有具体 curve 与 √z 或 1/3 等源，提供 R4 的几何比较方法；其已读模型不是 half⁴ 四二次曲面，不能自动迁移曲线、缩放或枚举整数。没有认领原42页全文审阅。
3. [Li–Jing–Yang, Open Topological String Amplitudes and BPS Invariants on Complete Intersection Calabi-Yau Threefolds, arXiv2207.11499v2](https://arxiv.org/abs/2207.11499v2)，2022-07-28，39页。实际读 PDF1–3、10–11、16–17、19–24；PDF24 的输出另行完整核对。PDF16 Table1 的四模型为 X₄,₄、X₆,₆、X₃,₄、X₄,₆，均不是 four quadrics；PDF17/20/22 的 √z forcing 有各自 PF 与 geometry。它有这一类 source 的实际实例，却没有给本 R₀ 或 L(f₈,4) 公式，也不证明本 B 的全尺度 OV integrality。

本轮检索在上述实际阅读范围内未找到 R₀ 的已证 L(f₈,4) 闭式；这不是不存在该闭式的数学定理。新的直接研究任务是：以 R5 的具体 relative algebraic integral 和 R7 的 quotient 为约束构造 cycle transport，取消 R8 的 conifold log，随后比较实际 modular/regulator periods 及所有整格费用。没有用 PSLQ 或文献摘要填补这些缺口。

## 8. 审阅与执行记录

本文数学部分为纯证明，未创建或执行有限数学 verifier，也未将 symbolic checks 计作解析证明。实际阅读冻结 M₄ 双边归约、conifold calibration 与原文 manifest，以及 spin 主稿 §§1–5 的 P₄、Levelt 矩阵及 conifold 输入；新 PDF 使用 fitz 只读抽取相应整页，并视觉核 PDF24 的关键源公式。§6.1 为本轮首次稿后的新增纯证明，没有扩充任何旧检查范围。新 manifest 仅记录元数据，不是数学证书。同行实际审阅将另行记录，本文当前不冒认同行已审。
