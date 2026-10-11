# 第260轮全局复盘：mixed 来源扩充纯族的秩收益与完整算术、共同域费用

2026-10-10；同一唯一来源的纸面复盘。目标仍为 (1,ζ(2),L(2,χ−3),G) 的 Q 线性无关；本稿没有得到新的数值无理性或线性无关性定理，没有修改259稿，没有执行数学程序、CAS、Padé、prime/map/参数扫描或旧 producer。

本稿结论：CDT 的七条纯函数可以沿当前 degree4 整数坐标拉回，与259的真实 rank3 关系模块组成真实 rank9。其逐个 N、全部 prime powers 的安全类型重新算得 τ=173/81，而非 CDT 原14行的16603/3920。可是这七条纯函数强迫共同 holomorphic 图省略至少两个有限点；两穿孔平面 Landau 定理给 |φ′(0)|<11/2，严格小于 exp(173/81)。因此**这一固定9行、安全 e=0 类型、CDT未精化 holomorphic-map 入口应停止**。这不是对原14行、全部精细类型、meromorphic-map 版本或所有统一框架的否定。

## A1. 本轮实际边界与原件

实际全文读259 field 最终17525 B稿及6647 B scope，旧稿只读不写；解析259manifest时读取了 files 之外的全部字段，未重审其193-file集合。本稿以259已付的最小 genus0 forcing 场、rank3与完整整模型为起点，不重新要求无界多处 determinant 非零。

固定 CDT [arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2)，218页 PDF；本轮实际全文读物理146–149、153–158、164–174、89–90、122–124的文本节选。关键页：9.0.3与9.0.13，物理146–149；纯族与类型，154–156；原14行独立性，165–171；实际14行的类型与预算，172–174；Theorem7.0.1与8.0.1，89–90、122–124。另实际全文读 Kim–Ma–Ma [2015 原件](https://doi.org/10.5186/aasfm.2015.4058) 的物理1–2页，尤其 (1.2)、(1.3) 与紧接的 Landau 不等式。全文限所列节选，不称整篇218页或13页 PDF FULL。节选保存 literature/global_review_round260_20261010/arithmetic_*；详细 pin 与 FULL/PARTIAL 范围见 arithmetic_reading_scope.md。

## A2. CDT 原14行的机制，哪些不能移交

CDT 令 y=t²/(t−1)，ι(t)=t/(t−1)。原三周期反证关系使 H(t) 的指定1/9芽可填；G_CDT(y)=H(t)+H(ι(t)) 的指定−1/72芽可填。其14行不是14条常数，也不是14个任意积分：

* 七条 genuine 纯函数 B1,…,B7，见10.1.2、10.1.3、10.2.1；
* G_CDT、G_CDT′、G_CDT″、G_CDT‴与三条具体 primitive，见Lemma12.1.1。

后七条的独立性依赖原 symmetrized homogeneous order4 模块的 irreducibility、指定绕行使 G_CDT 改变而纯族不变，以及三条 primitive 的 rational-adjoint/Frobenius 证明。第四条 primitive 反而有明确线性关系，物理171页；原文也展示17行方案的分母精细类型与图损失可以让它比14行方案差，物理157–158页。两者均说明“增加行数”本身不是准入证书。

当前 mixed forcing 的 h∉Q(t)，Q(t,h)=Q(s) degree4。不能把其 H 的对称和称为原 G_CDT，借用原 order4、14行 rank、τsharp 或旧 map。即便形式上作 H(t)+H(ι(t))，其 actual differential module、完整 character 场、图与返回支路都要重付。本轮只核原 genuine pure7 的实际移交，不另构造 mixed primitives 或新的对称实现。

## A3. 固定坐标、模块与纯族

采用259已付

\[
r=1-2s,\qquad t(s)=\frac{1-r^4}{9-r^4},\qquad
h(s)=\frac{2(1-r^2)r^3}{(3-r^2)^3},\quad K=C(s).
\]

s=q+q²Z[[q]]，q(s)∈s+s²Z[[s]]；t(s)∈s+s²Z[[s]]。反证中的单一 H=A(a+bB3+cC3+dB4)，d≠0，满足实际 rank3 的导数闭包 V_m=K⟨1,H,θ_sH⟩，θ_s=s∂_s；V_m/K·1 是有限指数 modular monodromy 的 irreducible rank2 标准 SL2 模块。这里 modular B3/B4 与下面 pure B_i 是不同函数；仅沿用 CDT 对纯族的字母，不能混淆。

令 Y(s)=t(s)²/(t(s)−1)，degree8，Y(s)=−s²+s³Z[[s]]。下文写 P_i(s)=B_i(Y(s)) 以避免重名：

\[
B_1=1,\quad B_2=2y-2\sqrt{y(4-y)}\arcsin(\sqrt y/2),\quad
B_3=2\arcsin(\sqrt y/2)^2,
\]
\[
B_4=(t-ι(t))(Li_2(t)-Li_2(ι(t))),\quad
B_5=y\,{}_3F_2(\tfrac12,1,1;\tfrac32,\tfrac32;y/4),
\quad B_6=\int B_3(y)\frac{dy}{y},\quad B_7=\int B_4(y)\frac{dy}{y}.
\]

全部取原点的指定 Taylor 芽、primitive 常数0。B5(4)=8G 是原文已有端点公式；没有从这个公式推得新的常数独立性。

## A4. 实际 pure7 在 K 上仍独立：不能只说有限拉回自动保秩

一般有限代数拉回会降低函数独立性，如1、√t在加入√t的场中变得相关。所以本节给本对象的实际证书。

令 ℓ=log(1−t)，a_0=√(1−t)，J=t·{}_3F_2(1/2,1,1;3/2,3/2;Y/4)。指定芽有

\[
B_2(Y)=2Y-\frac{t(2-t)}{1-t}\ell,\quad B_3(Y)=-\tfrac12\ell^2,
\]
\[
B_4(Y)=\frac{t(2-t)}{1-t}\bigl(2Li_2(t)+\tfrac12\ell^2\bigr),
\qquad B_5(Y)=\frac{t}{t-1}J(t).
\]

这里用 Li2(ι(t))=−Li2(t)−ℓ²/2 的指定芽恒等式；亦可逐项微分并用原点常数定它。矩阵可逆于C(t)，所以 P1,…,P5 的独立性等价于1,ℓ,ℓ²,Li2(t),J(t)在K上独立。

CDT物理165页采用绕t=1、t=0的 commutator γ。它固定ℓ与a0，且

\[
\Delta_\gamma Li_2=c\ne0,\qquad \Delta_\gamma J=c' a_0\ne0.
\]

第一式由 Li2′=−ℓ/t，conjugated t=0 loop 上的 ℓ-shift=±2πi 给非零 residue。第二式由原文10.1.6

\[
J'-\frac{J}{2(t-1)}=-\frac\ell t,\qquad
d(J/a_0)=-\frac\ell{t a_0}\,dt
\]

给出：同一conjugated loop上a0只变符号、ℓ加±2πi，故积分有非零 residue；整条 commutator 后 ℓ,a0 回到原支，差为非零 constant·a0。两者在γ的正整数次幂下分别乘该整数，没有有限幂杀掉的伪 monodromy。degree4拉回取闭合幂γ^N，K 中系数完全返回。

若 K 系数的五行关系存在，沿γ^N取差，得到 c r3+c′r4 a0=0。可是 a0∉K：1−t(s)=8/(9−r⁴) 在四个不同有限 t=∞ fiber 有简单极点，而K中的 square不可能有奇数阶极点。故 r3=r4=0；其余1,ℓ,ℓ²独立，因为 ℓ在t=1或任一 t∞ fiber 的无限 logarithmic monodromy 使它超越于K。

对 P6,P7，P1,…,P5 的 K-span V5 由 CDT12.0.4 四条微分公式闭合于∂s。假如两条新primitive与V5相关，把两个系数清成 polynomial s，并按其最高degree重复∂s；因为 P6′、P7′∈V5，得到非零常数组合 a6 P6+a7 P7∈V5。按∂Y微分并比较已经独立的P3/P4系数，严格得到

\[
\frac{a_6}{Y}=\partial_Y b_3,\qquad
\frac{a_7}{Y}=\partial_Y b_4+\frac{2-Y}{Y(4-Y)}b_4,\quad b_i\in K.
\]

第一式迫 b3=a6 logY+constant，不是代数函数，故a6=0。记 R=√(Y(4−Y))；第二式等价 d(b4R)=a7(R/Y)dY。右方在曲线R²=Y(4−Y)的两个∞处有 residues ±2i，因为 R/Y=±i(1−2/Y+…)。任何有限拉回把非零 residue乘正整数；而 meromorphic function 的精确微分 residues全0。因此它不可能有代数primitive，a7=0。这里明确允许K系数，未把原文只在Q(y)的证明免费搬来。

于是 **P1,…,P7 在K上实际独立**。

## A5. 与 mixed 模块交叉：实际 rank9，非“7+3自动相加”

CDT12.0.4与P6′=P3 Y′/Y、P7′=P4 Y′/Y 给 actual rank7 微分模块 V_p。其对角 integrating factors 只有1、R、√Y。在有限代数扩张 K(R,√Y)上，把P2/P4除R、P5除√Y后，整个connection是严格下三角；故其 differential Galois/monodromy 为 unipotent，原K上至多 virtually solvable。没有 SL2 irreducible rank2 subquotient。

交集 W=V_p∩V_m 闭合于导数且含K·1。W/K·1是 V_m/K·1 的子模块。后者不可约，所以若交集大于K·1，W就是全部V_m，迫V_p有该 SL2 rank2 subquotient，矛盾。故交集恰K·1，联合维数7+3−1=9。明确的 actual 普通 Taylor tuple 为

\[
\boxed{(P_1,P_2,P_3,P_4,P_5,C_0H,C_0\theta_sH,P_6,P_7).}
\]

C0是259清关系系数的固定整数。其独立性不要求再造Δ_n证书，也不意味着目标四常数已经独立；H仍是反证中假定存在的关系函数。

## A6. 全prefix、全prime-powers 类型：τ=173/81

CDT10.2.2 给 pure B1..B7 的每个 y^n 系数分母分别整除

\[
1,\ d_{2n},\ d_{2n}n,\ d_{2n}^2,\ d_{2n}(2n-1),\ d_{2n}n^2,\ d_{2n}^2 n.
\]

Y∈s²Z[[s]]，所以贡献到s^j的 index满足2n≤j。对于所有j≤N，n≤floor(N/2)，故逐项整数composition给下面 literal全prefix bound；d_N=lcm(1,…,N)，不丢任何prime powers：

|行|全prefix分母的已证除数|本稿采用的安全除数|
|---|---|---|
|P1|1|1|
|P2|d_N|d_N|
|P3|d_N d_floor(N/2)|d_N²|
|P4,P5|d_N²|d_N²|
|C0H,C0θsH|d_N²|d_N²|
|P6|d_N d_floor(N/2)²|d_N² d_floor(N/2)|
|P7|d_N² d_floor(N/2)|d_N² d_floor(N/2)|

注意 n^e 在integer composition后只能安全嵌入 d_floor(N/2)^e，不能凭原函数含primitive就断言新s-coefficient仍由N^e清分母。本稿不使用原CDT τsharp，e全0。原factorial prime-window的进一步细化未审，不借其可能改进。

按A5给定九行顺序，三列是 b=(1,1,1/2)，zero-prefix分别u=(1,2,7)，各列在本prefix之后恒等于其b_h。CDT v2 Remark8.0.6的实际 standing nested-column型给

\[
\tau=\tau^{\flat\flat}=\tau^{\flat}
=\frac{80}{81}+\frac{77}{81}+\frac{16}{81}
=\boxed{173/81},\qquad \tau^\sharp=0.
\]

这是本对象当前safe array的精确值，并非所有更精细分母描述的最优值。仅为比较：bare rank3的当前safe τ=16/9；若只用J≥λ，strict rank3矛盾必要λ>8/3，而当前rank9必要λ>173/72，数值门槛有所降低。下一节证明真实共同域损失已足以否决这个安全入口。

## A7. 相同图的不可省略费用：pure-only两穿孔证书

CDT Theorem7.0.1/8.0.1 的当前入口明确要求 φ:(D,0)→(C,0) **holomorphic**，各普通 Taylor 芽的同一pullback在disk上meromorphic。本文结论只限这个入口；若φ只meromorphic且容许pole，两个有限omissions不足以套此Landau定理，不能外推。

P2的A4公式 rational恢复ℓ。若φ hit任一 t(s)=∞的有限simple pole ξ，则ℓ∘φ=log(1−t(φ))具有非零 logarithmic monodromy；任意有限ramification把该log系数乘正整数，仍不能meromorphic。P2∘φ若meromorphic，就由该rational公式迫ℓ∘φ meromorphic，矛盾。因此真实同φ必须省略四个有限点

\[
s=(1\pm\sqrt3)/2,\quad (1\pm i\sqrt3)/2.
\]

只取实两点 α=(1−√3)/2，β=(1+√3)/2 已足够。令 f=(φ−α)/(β−α)，则 f:D→C\{0,1} holomorphic，|f(0)|=(√3−1)/(2√3)。Kim–Ma–Ma 原件(1.2)、(1.3)给

\[
|\phi'(0)|\le(\sqrt3-1)\{\log(3+\sqrt3)+K_L\},\quad
K_L=\frac{\Gamma(1/4)^4}{4\pi^2}.
\]

无数值计算的严格bound如下。Gamma积分的严格 Cauchy–Schwarz 给 Γ(5/4)²<Γ(1)Γ(3/2)=√π/2，所以 Γ(1/4)^4<64π，K_L<16/π<16/3。√3<7/4，故√3−1<3/4；3+√3<5且exp2>1+2+2=5，故log(3+√3)<2。因此

\[
\boxed{|\phi'(0)|<\tfrac34(2+16/3)=11/2.}
\]

另一方面 τ=173/81>2，而exp2>1+2+2+4/3=19/3>11/2。因此

\[
\boxed{\lambda=\log|\phi'(0)|<173/81=\tau.}
\]

连 Theorem7.0.1/8.0.1 的 holonomic λ>τ 条件都达不到；无需任何map扫描、实际能量积分或额外H bad-germ证书，即已停止A5–A6这一固定safe9入口。全部其它cusps、返回支路、H坏芽与joint univalent leaf只会额外限制同图，不会解除这两点的省略。

y=4沿t有e2，所以 pure local Z/2 monodromy可以在t=2处合法消失；不能把这处有限monodromy障碍额外收费。相反t∞处log是无限monodromy，必须收费。指定s=1/2的filled mixed芽对应Y=−1/72，pure族在该点原本regular，但这也没有支付其它fiber或任意返回支路。integer s坐标、field genus0与rank9均不是全局univalent叶的证书。

## A8. 全局路线结论与唯一下一证书

本轮已付：pure7真实有限拉回独立性；与mixed rank3的交叉只含1；actual rank9；全部N和prime powers的安全整模型；τ=173/81；同holomorphic图的两个不可填punctures；独立于H的严格 derivative upper bound，及当前safe9入口的纸面停止。

本轮未付也未宣称：原14行在mixed来源上的rank/type；s-primitives的精细n^e类型；更强CDT convexity修正；meromorphic-map criterion；完整joint域、所有返回支路、或任何新数值无理性定理。

继续同mixed扩充路线，唯一值得先索取的证书是：**一个从当前固定来源逐N证明的实际 refined joint type/criterion，连同这些不可填pure punctures所允许的同一图，给出严格可突破的预算**。在这一证书之前不继续添加pure行、primitive、参数或运行实现。单独把173/81替换成猜测的旧τsharp不算证书；若新类型/criterion仍不能突破上述同图上界，则停止该同源扩充窗口。其余架构如何优先，由Root的第260轮全局复盘统一决定。
