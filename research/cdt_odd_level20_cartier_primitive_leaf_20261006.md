# 固定 Cartier 核的原函数：合法 H 方向与不可删除的周期载体

日期：2026-10-06。本文新建，既有稿保持冻结。只读独立核验 [Cartier–Hecke 稿](cdt_odd_level20_cartier_kernel_20261006.md) §§1、3–4 后，继续分析其固定核空间在真实 filled leaf 上的原函数。正结论是六个固定核的 **H 部分**确实有同一个全盘全纯原函数；负结论是完整实际 packet 原函数仍含 ΘA，任意非零同号核的该载体都不能在当前 coarse Fricke 点下降。本文没有新增 primitive S3/S4、预算扫描或数值无理性定理。

## 1. 审阅范围及固定符号

沿用 [完整模型](cdt_odd_level20_model_20261006.md) 和 [共同叶 §8](cdt_odd_level20_leaf_20261006.md)。记 r=√5、K=Q(r)、ε∈{1,−1}；ε=1 时取 A−、H−，ε=−1 时取 A+、H+。因此

\[
N^{(\varepsilon)}=1-(6+\varepsilon r)t+(1+\varepsilon r)t^2,
\qquad
C^{(\varepsilon)}=1-(6-2\varepsilon r)t+(6-2\varepsilon r)t^2.
\tag{1}
\]

C^(ε) 是 A 的 own C；尤其 ε=1 对应 C−，并非 C+。令

\[
A^{(\varepsilon)}=-N^{(\varepsilon)}\sqrt{C^{(\varepsilon)}}\Phi/5,
\quad S=(1-t)\sqrt\Delta\,\Phi,
\quad H^{(\varepsilon)}=A^{(\varepsilon)}(f^{(\varepsilon)}-\varepsilon\Theta).
\tag{2}
\]

Θ=−5r L(3,χ₅)/16。函数无条件存在；系数在 K 的陈述使用反证假设 L(3,χ₅)∈Q。没有给未知周期任意 Galois 作用。

实读 Cartier 稿 §§1、3–4 的符号、除子和整性证明通过：S 是 Fricke+ 的 weight2 形式，A^(ε) 是 Fricke −ε 的 weight2 χ₅ 形式。Tₚ(A−S) 与 A^(χ(p))S 同字符、同权、同 Fricke 符号；商属于 K(t)。分母形式的 X₀(20) 零阶总数为 N 的4、own C 的4、other C 的2、t1 cusps 的2，合12。Φ 在 t∞ 两 cusps 各零阶3，恰抵消其它因子的极点，故商在∞有限。

所以对所有好 p，原稿的

\[
R_p=P_p/D^{(\varepsilon)},\quad
D^{(\varepsilon)}=(1-t)N^{(\varepsilon)}C^{(\varepsilon)},
\quad\deg P_p\le5,
\quad P_p\in O_{K,\mathfrak p}[t]
\tag{3}
\]

成立，D(0)=1，Pₚ(0)=1+εp³。此审阅未运行其 producer 或证书；也没有把 (3) 当成新增 Smith 方向。relative Cartier 的 Frobenius-twisted 约定按原稿保留。

## 2. 固定核空间及三种不同的正规原函数

以下固定 ε，取任意 P∈K[t]、degP≤5，令 Q=P/D^(ε)。必须区分

\[
\begin{aligned}
J_{Q,H}(t)&=\int_0^t[Q(v)H^{(\varepsilon)}(v)-Q(0)H^{(\varepsilon)}(0)]\,dv/v,\\
U_{Q,A}(t)&=\int_0^t[Q(v)A^{(\varepsilon)}(v)-Q(0)A^{(\varepsilon)}(0)]\,dv/v,\\
K_Q(t)&=\int_0^t Q(v)A^{(\varepsilon)}(v)f^{(\varepsilon)}(v)\,dv/v.
\end{aligned}
\tag{4}
\]

在原点取实际 Taylor 芽，三个积分常数均为0。A(0)=−1/5、f(0)=0、H(0)=εΘ/5，所以完整源 A f 在0已经为零，而且有确切身份

\[
\boxed{K_Q=J_{Q,H}+\varepsilon\Theta U_{Q,A}.}
\tag{5}
\]

(5) 保留 Cartier 稿 C17 的真实污染项，不能以 J 替代 K。单独的 ∫Qdt/t 还需要减 Q(0)，不能把原点的 logt 混入正规芽。

固定六个核

\[
Q_j=t^j/D^{(\varepsilon)},\qquad 0\le j\le5
\tag{6}
\]

张成全部 Q。它们独立于 p；Pₚ 的系数只在随后某个好 place 的局部归约中形成六核的线性组合。这里没有把随 p 变化的函数当成一个固定 CDT source。

## 3. 全部 interior fibers：H 部分的极点实际全部抵消

共同 filled coarse surface X_G 来自 G=⟨T,W₂₀⟩，其 interior 是 disk。t 在其上全纯，省去1与∞，在唯一填入点 P₀有 simple zero。H 的实际 G 不变性保证全盘全纯。t 的 finite noncusp values 都有 fibers：这是 X_G→X₀(20)/W₂₀ 的自然 uniformization 投影，故不能通过忽略 N 或 C 的 roots 消去问题。

分母的因子都是 simple 且互不相交。独立固定符号核算给

\[
\begin{gathered}
\operatorname{disc}N=37+8\varepsilon r,\quad
\operatorname{Res}(N,C)=-80+60\varepsilon r,\\
\operatorname{Res}(N,C^{(-\varepsilon)})=-20-20\varepsilon r,
\quad\operatorname{Res}(C,C^{(-\varepsilon)})=80,\\
N(0)=C(0)=C(1)=1,\qquad N(1)=-4.
\end{gathered}
\tag{7}
\]

这些值均非零。因此所有普通 N roots、四 branch、0、1分开。

**N roots。** t 在这些点无分歧。A 含 N 的 simple zero，f 在相应上半平面 lift 全纯，故 H 至少 simple zero。Q 的 simple pole 被 H 抵消；QH dt/t 全纯。QA dt/t 在原上半平面也全纯。

**Own C roots 的非 G-elliptic fibers。** 取 source 局部坐标 x，有 t−a=x²·unit，A=x·unit，dt=x·unit dx。Q 至多 x⁻²；f 和 H/A 全纯，故 QH dt/t、QA dt/t 的总阶至少0。二阶分歧没有消掉 logarithmic pole；这里没有 logarithmic pole，是 A 的零点与 dt 的零点实际抵消了分母。

**唯一 G-elliptic orbit。** canonical Fricke 固定点 τ*=i/√20 对应 α，α 是 C+ 的 root。ε=1 时 own C=C−，Q 在α无极点。ε=−1 时 own C=C+，A+ 在上半平面局部 simple zero；H+ 在 coarse 坐标 u=x²上全纯且 H+(α)=0，因此 H+=u·holomorphic。Q 至多 u⁻¹，QH+dt/t仍全纯。其它α fibers没有 G stabilizer，适用上一段的二阶分歧计算。

**Filled point。** Q 与 H 在 t=0 全纯，减去 Q(0)H(0) 后被 t 整除，故 (4) 的 J 一形式在唯一填入点可去。

**其它 interior 点。** Q 没有极点，H 全纯。t1 与∞的所有 cusp preimages位于 real/conformal boundary，不是 interior。

于是获得全尺度正结论：

\[
\boxed{J_{Q,H}\text{ 在同一个 filled }X_G\text{ 上有唯一全局全纯正规原函数。}}
\tag{8}
\]

证明是该一形式全纯与 filled disk simply connected；不是以“亚纯函数可以积分”推断无分支。相应 pullback 到已有 Riemann map 的 full disk 全纯；对闭盘邻域仍采用原来的缩盘处理。

## 4. 完整周期载体不能在同一个 coarse leaf 下降

H 在 G 下不变；A 是 weight2 carrier，不能当成 scalar G 函数。实际 Fricke 身份是

\[
A^{(\varepsilon)}(W_{20}\tau)=-\varepsilon20\tau^2A^{(\varepsilon)}(\tau).
\tag{9}
\]

Q(t)、dt/t均不变。完整一形式 ω=Q(H+εΘA)dt/t 满足

\[
\boxed{W_{20}^*\omega-\omega
=-\Theta Q(t)(20\tau^2+\varepsilon)A^{(\varepsilon)}\,dt/t.}
\tag{10}
\]

对任何非零 Q，该差非恒零。Θ也非零：L(3,χ₅)≥1−Σ_{n≥2}n⁻³≥3/4>0。若 K_Q 是同 coarse disk 上的单值 scalar 原函数，其 differential 必须下降，与(10)矛盾。给 U 减去的原点常数项是 invariant form，不能改变这个差。

这个障碍已经能在α的局部看见，不必靠抽象群论。取 Cayley 坐标

\[
w=\frac{\tau-i/\sqrt{20}}{\tau+i/\sqrt{20}},
\quad W_{20}:w\mapsto-w,
\quad t=\alpha+c w^2+O(w^4),\quad c\ne0.
\tag{11}
\]

由(9)，存在原点非零的 holomorphic a、b，使

\[
A_-=(1-w)^2a(w^2),\qquad
A_+=(1-w)^2w b(w^2).
\tag{12}
\]

非零性来自 A−在α非零、A+在α恰 simple zero。令 v=ord_αQ；ε=1时v≥0，ε=−1时v≥−1。写 Qdt/t=w^(2v+1)d(w²)dw，d(0)≠0。于是 QA dt/t 的正规 primitive 含非零 odd 项：

\[
\begin{cases}
[-2a(0)d(0)/(2v+3)]w^{2v+3},&\varepsilon=1,\\
[b(0)d(0)/(2v+3)]w^{2v+3},&\varepsilon=-1.
\end{cases}
\tag{13}
\]

正规化常数的 primitive 在α是 w 的 even 函数，不影响(13)。J_QH同样是 coarse 单值、因而 even；所以 (5) 的 Θ载体产生实际 half-integer branch，不能由 H 部分取消。任何非零 rational/polynomial t gauge只能移奇次项的有限阶，不能使其 single-valued。高阶 vanishing of P 在α也只推迟该项。

这里仅排除当前单个 ε、非零固定 Q 和 unchanged coarse leaf 上的完整 scalar primitive。没有排除改变 source/automorphic gauge、取新的 cover、不同 carrier 之间的真正 de Rham 组合、或者仅在有限 modp prefix 中产生新关系。

## 5. 边界 cusp 的 logarithmic 项与纯 rational primitive

这些边界障碍不影响(8)的 interior 全纯性，但阻止无条件扩大解析域。原模型的真实 cusp 项为

\[
H=-17\log(t-1)^3/6+\text{较低对数项},\qquad
H=-17\log(t)^3/120+\text{较低对数项}\quad(t\to\infty).
\tag{14}
\]

在t1，D'(1)=4。如果P(1)≠0，J_QH最高项是

\[
-17P(1)\log(t-1)^4/96.
\tag{15}
\]

若P在1消去该 pole，令ord₁Q=k≥0，primitive仍有非零 (t−1)^(k+1)log(t−1)³项。有限阶 vanishing、finite ramification 或 polynomial gauge均不能把它变成 meromorphic cusp；不能把该 cusp当成椭圆 branch解除。

在∞，D的leading coefficient是4(1−εr)。若degP=5且p₅为其最高系数，Q∞=p₅/[4(1−εr)]≠0，primitive最高项为 −17Q∞log(t)^4/480。若degP<5，则出现非零 t^{−(5−degP)}log(t)³项；正规化还可引入 −Q(0)H(0)logt。低次log不能消去前述非零最高log型。故任何非零Q的H primitive均不能简单把∞变成 meromorphic cusp。

另外，对 **纯 rational** 正规 primitive V_Q=∫(Q−Q(0))dt/t，partial fractions精确给

\[
V_Q=\sum_{a\in\{1,N\text{ roots},C\text{ roots}\}}
\frac{P(a)}{aD'(a)}\log(1-t/a).
\tag{16}
\]

simple pole 的非零 residue经过有限分歧仍产生log，不变成 meromorphic。N 与 C fibers在interior存在，所以纯rational primitive在同 full disk 全纯的充要条件是 NC|P。此时Q=(a+bt)/(1−t)，V_Q=−(a+b)log(1−t)，确在省去1的 simply connected filled disk 上全纯。(8)之所以允许全部六核，是H的实际零点，不是普通rational积分自动无分支。

## 6. 六个合法 H 辅助芽的全分母与仍缺的独立性

D∈O_K[t]、D(0)=1，故1/D的全部Taylor coefficients在O_K。对(6)的固定六核，不存在新的指数型分母。旧真实H的固定C₀D_n³安全型与卷积给

\[
\boxed{C_0\,nD_n^3[t^n]J_{Q_j,H}\in O_K,
\qquad 0\le j\le5.}
\tag{17}
\]

一般固定P∈K[t]仅需额外固定清因子C_P。原点正规化仅去常数，不增加分母。新六核因此兼具完整 e=1、三个unitLCM列以及同一个真实全盘leaf。

对实际Hecke核还可加强已有的p-local整性，而不修改冻结原稿：真实q形式满足5A±∈O_K[[q]]、constant−1，且eta对数导数S∈Z[[q]]、constant1。因此5F_old、5F_den全局整，后者constant−1；算术Tₚ的Fourier操作保持全局整性。于是

\[
R_p=T_p(5F_{old})/(5F_{den})\in O_K[[q]],
\qquad P_p=D^{(\varepsilon)}R_p\in O_K[t].
\tag{18}
\]

最后一步仍用(3)的全局degree bound、integerq↔t及D∈O_K[t]。这个加强只使用p∤20的Hecke输入，未推出新的局部Smith层；也未把p-dependent系数变化当作固定CDT函数系统。

这还没有证明六个 primitive都是新独立方向；其中Q=1对应P=D，已经包含之前的I_H。若仅把六个积分放进 connection，rank上界至多4+6=10，等号没有证明。对新增方向须独立给actual rank/与已有背景交、同一个source和预算。完整Cartier packet仍是(5)，并非(8)单独；(10)–(13)说明为什么“合法H原函数已经存在”尚不等于C17 primitive免费合法。

最小下一接口是：在有限六核空间内求真实 rational de Rham 关系，并同时保留ΘU；若要从其modp归约产生新Smith行，仍须核完整prefix、primitive content、degree和加权独立性。本文没有执行这样的扫描或声称完成该接口。

## 7. 核验记录与边界

本文证明使用完整模型的全局除子、真实Fricke身份、已证filledG-disk和最高cusp对数项。新固定symbolic核对只计算(7)的discriminant/resultants及0、1值；未运行任何历史producer、Cartier证书或预算扫描。全尺度结论(8)、(10)与全分母(17)由正文论证，不由有限jet判断。
