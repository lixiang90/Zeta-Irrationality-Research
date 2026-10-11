# level20 有界 Cartier 核的实际 de Rham 类与六个新积分方向

日期：2026-10-06。本稿新建，不改此前冻结报告。输入是 [有界 Cartier 核](cdt_odd_level20_cartier_kernel_20261006.md) 的固定六维空间，不把有限素数实验当成全素数定理。结论是一个实际函数模的归约结果：该空间的每个非零核都给非 exact 类；正规 H 积分可在原共同解析叶上实现，并确实增加六个函数方向。完整 Cartier primitive 仍带真实的 ΘA 项，不能因本结果而删除；没有证明新的 primitive S3、Smith 收益或数值无理性结论。

## 1. 两种实际积分必须分开

记 r=√5、K=Q(r)。使用原核稿的 ε 下标：ε=1 取 A₋、H₋、N₋、C₋，ε=−1 取 A₊、H₊、N₊、C₊。特别是这里 C^(ε) 是 A 的 own-zero 因子，A/S gauge 分母含另一个 C，不能混用。

定义

\[
 D_\varepsilon=(1-t)N^{(\varepsilon)}C^{(\varepsilon)},\quad
 \mathcal R_\varepsilon=\{P/D_\varepsilon:\ P\in K[t],\ \deg P\le5\}.
\tag{D1}
\]

这是六维 K 空间，Dε(0)=1、degree5。以 Rⱼ=tʲ/Dε（j=0,…,5）为固定基。真实周期取 Θ=−5rL(3,χ₅)/16，真实函数是

\[
 F_\varepsilon:=A^{(\varepsilon)}f^{(\varepsilon)}
 =H^{(\varepsilon)}+\varepsilon\Theta A^{(\varepsilon)},
 \quad F_\varepsilon(0)=0.
\tag{D2}
\]

先在原点考虑实际 primitive

\[
 J_R^F=\int_0^t R(v)F_\varepsilon(v)\frac{dv}{v}.
\tag{D3}
\]

它无需减 residue，因为 Fε(0)=0。另定义正规 H 与 A primitive

\[
 J_R^H=\int_0^t\{R(v)H^{(\varepsilon)}(v)-R(0)H^{(\varepsilon)}(0)\}\frac{dv}{v},
\]
\[
 J_R^A=\int_0^t\{R(v)A^{(\varepsilon)}(v)-R(0)A^{(\varepsilon)}(0)\}\frac{dv}{v}.
\tag{D4}
\]

Hε(0)+εΘAε(0)=0，故完全真实的分解是

\[
 \boxed{J_R^F=J_R^H+\varepsilon\Theta J_R^A.}
\tag{D5}
\]

以下关于有理 exactness 的结果同时适用于 F 与正规 H。关于原共同叶的结果则适用于 Jᴴ；Jᶠ 的 carrier 不能省略。

函数模先在 C(t) 上理解，因此实际周期无需任何有理性假设。若按原反证路线假设 L(3,χ₅)∈Q，所有 H、Jᴴ 的原点系数属于 K，结果亦给 K(t) 模。不是给未知实际周期任意规定 Galois 共轭。

## 2. 完整四阶实际模中的 Hermite 归约

使用 [完整模型](cdt_odd_level20_model_20261006.md) 的三阶单首项算子

\[
 \mathcal L_\varepsilon=\partial^3+a_2\partial^2+a_1\partial+a_0,
 \qquad \mathcal L_\varepsilon H^{(\varepsilon)}=U_\varepsilon\in K(t).
\tag{D6}
\]

齐次解为 A、τA、τ²A，故 LεFε=Uε 也成立。H 与 F 各自的实际函数模

\[
 W_H=\langle1,H,H',H''\rangle,\qquad
 W_F=\langle1,F,F',F''\rangle
\tag{D7}
\]

均为 rank4：上界来自 D6；未消 cusp t=∞ 的 H 含非零 log³ 项，而 F−H=εΘA 最多含 log²，故 F 亦保留该 log³，下界与旧模型相同。不得将三个 homogeneous solutions 直接当成 W_H 的实际函数基。

若 Jᴳ∈W_G（G=H 或 F），展开

\[
 J=bG''+cG'+dG+e,\qquad b,c,d,e\in\mathbf C(t).
\]

比较实际独立的 G''、G'、G、1 系数，因 J'=RG/t（H 时另减原点常数/t），得到

\[
 c=a_2b-b',\qquad
 d=a_1b-c'=b''-a_2b'+(a_1-a_2')b,
\]
\[
 \boxed{d'-a_0b=-\mathcal L_\varepsilon^*b=R/t.}
\tag{D8}
\]

这里

\[
 \mathcal L^*b=-b'''+a_2b''+(2a_2'-a_1)b'
                 +(a_2''-a_1'+a_0)b.
\tag{D9}
\]

constant 方程是 e'=−Ub，或 H 情形 e'=−Ub−R(0)H(0)/t。后者只改 constant 方程，不能救 D8 的无解。D8 是实际函数匹配所得的必要条件，不是只在抽象解空间上做一次形式计数。

## 3. 伴随有理解的局部除子障碍

完整模型给 gauge

\[
 \rho=R_A'/R_A=N'/N+\frac1{1-t}-\frac{C_{other}'}{2C_{other}},
 \quad R_A=A/S.
\]

Q 的 branch 二阶主部是3/16，t1 cusp 的二阶主部是1/4；N 的两个根普通且与 Δ、0、1不交。由模型公式或实际 A、τA、τ²A 的局部阶可得下面精确指数。表中 ownC 是 C^(ε)，otherC 是另一因子。

|点|L 的局部指数|L* 的局部指数|R/t 的最多 pole|
|---|---|---|---|
|t=0|0,0,0|2,2,2|1|
|t=1|0,0,0|2,2,2|1|
|ownC 两根|1/2,1,3/2|1/2,1,3/2|1|
|otherC 两根|0,1/2,1|1,3/2,2|0|
|N 两根|1,2,3|−1,0,1|1|
|其余 ordinary 点|0,1,2|0,1,2|0|

单首项三阶算子的 formal adjoint 指数是2−λ。要核其符号，若 L 的 indicial polynomial 为 I(λ)，L* 的 indicial polynomial 是 I(2−λ)，最高项为−λ³。符号不影响根，但不能漏掉 a₁' 的二倍 pole 导数。

设 b 是 D8 的非零 rational solution。在有限点以局部坐标 x=t−a 写 b=b₀xᵐ+…，m 是整数，b₀≠0。若 m 不是该点的 adjoint indicial root，L*b 的首项阶恰为 m−3。因此：

* 在0、1，m≤1不是 indicial root，且 m−3≤−2，超过允许的 simple pole，故 m≥2。
* 在全部四个 Δ 根，m≤0不是 indicial root，m−3≤−3，超过允许 pole，故 m≥1。
* 在 N 根，m≤−2不是 indicial root且给至少五阶 pole，故 m≥−1。
* 其余 finite ordinary 点不可有 pole。

于是 b 只能有 N 的简单极点，且至少含零 divisor 2[0]+2[1]+div(Δ)。N 无重根且与这些零不交，因此

\[
 \boxed{b=\frac{t^2(1-t)^2\Delta(t)}{N(t)}B(t),\quad B\in\mathbf C[t].}
\tag{D10}
\]

非零 b 在∞的 growth degree 至少8−2=6。

另一方面，Q=O(t⁻³)、ρ=O(t⁻²)，模型给

\[
 a_2=3/t+O(t^{-2}),\quad a_1=1/t^2+O(t^{-3}),\quad a_0=O(t^{-4}).
\]

故对 b=b∞tᵈ+…，

\[
 \mathcal L^*b=-(d-2)^3 b_\infty t^{d-3}+O(t^{d-4}).
\tag{D11}
\]

R∞有限，故 D8 右边 O(t⁻¹)。若 d>2，D11 的系数不为零且阶≥0，矛盾。因此 d≤2，与 D10 迫 d≥6 冲突。

结论为

\[
 \boxed{\text{对每个非零 }R\in\mathcal R_\varepsilon,
 \quad-\mathcal L_\varepsilon^*b=R/t
 \text{在 }\mathbf C(t)\text{ 中无解。}}
\tag{D12}
\]

这完整排除了在原 rank4 模内的 rational Hermite reduction，不仅排固定次数的试探 ansatz。它没有排除在更大的真实积分模块中归约，也没有排除 finite jets 上的短模p关系。

## 4. 六个实际类独立；不是只做形式升阶

在 actual rational de Rham quotient

\[
 W_G\,dt\big/\{v'\,dt:\ v\in W_G\}
\]

中，R↦[(R/t)Gdt]（H 时正规减 constant/t）在六维 constant 核空间上 injective，由 D12 立即得出。因此不存在非零 constant 组合的六个 primitive 落回 W_G。

还需将此结论升级成 C(t) 函数独立性。以下基本引理足够：若 M 是 actual differential module、Jⱼ'=vⱼ∈M，而有 rational relation ∑rⱼJⱼ∈M，取非零项数最少的关系，将一项归一为 coefficient1。微分后 ∑rⱼ'Jⱼ∈M 消掉该归一项；最少性迫其余 rⱼ'=0。于是原关系来自 constant coefficients。这个论证等价于 trivial differential module 的子模有 constant basis，但直接应用在实际函数上。

对基 Rⱼ 应用该引理及 D12 得

\[
 \boxed{\dim_{\mathbf C(t)}\bigl(W_G+\sum_{j=0}^5\mathbf C(t)J_{R_j}^G\bigr)=10.}
\tag{D13}
\]

这里 G=H 或 F 可分别使用。这个增秩由实际函数关系证明，不是因为引入六个形式积分符号。两个十维模块也不能自动当同一个系统：它们的差仍是 D5 的 period carrier。

更进一步，令 B 是已经证明 W_H∩B=C(t)·1 的 closed actual background。若一个 constant 组合 ∑cⱼJᴴⱼ 属于 W_H+B，展开为 bH''+cH'+dH+u_B，微分后 B 保持在 B；H、H'、H'' 在商模(W_H+B)/B中实际独立。因此同样的系数匹配仍迫 D8，无解。再用最少项引理排所有 rational 组合。故

\[
 \dim(W_H+B+\sum_j\mathbf C(t)J_{R_j}^H)
 =\dim(W_H+B)+6.
\tag{D14}
\]

对 [已证的 P10 背景](cdt_odd_low_cost_polylog_20261006.md)，其 actual rank10、与 W_H 的交为常数，D14 给单 sign 的实际 rank19=10+4−1+6。这里用直接 H 系数匹配；不把单个 I_H 的 local N⁴ 论证盲目外推至所有新积分。rank19 本身没有给出低成本整模型，也不等于 holonomy 上界已小于19。

## 5. 正规 H 类的共同叶与完整 F 的 carrier 障碍

使用 [已证 full common leaf](cdt_odd_level20_leaf_20261006.md) §8 的 filled G=⟨T,W₂₀⟩ coarse surface。t 内部没有1或∞，只有 filled cusp 的一个 simplezero0。H 本身在该 surface 全纯。正规 D4 的 H 一形式在原点减去 residue。

R 其余内部 pole 只在 N 与 ownC。N 根处 A 实际有一阶零，f−εΘ在上半平面解析，所以 RH 不产生 pole。非 coarse-elliptic 的 ownC lifts，以 τ-local 坐标 x 有 t−a~x²、A~x、dt~x dx，R 的 t-simplepole是 x⁻²，故 RHdt/t全纯。canonical coarse-elliptic α 只可能属于 A₊ 的 ownC；真实 W-period 给 A₊与 f₊+Θ各至少一阶零，H₊至少二阶零，故 RH 在 coarse t 坐标仍正则。此项使用真实周期，不能从抽象 W-invariance 代替。

因此每个 Jᴴ_R 都是同一个 filled simply connected surface 上的全纯 primitive，不新增坏 leaf。详见独立的 [primitive leaf 证明](cdt_odd_level20_cartier_primitive_leaf_20261006.md)，其数学范围与本稿 adjoint exactness 互补。

完整 Jᶠ_R 则不能由此降到同一 G 函数 leaf。已有关系 A₋(Wτ)=−20τ²A₋、A₊(Wτ)=20τ²A₊，统一为 A^(ε)(Wτ)=−ε20τ²A^(ε)(τ)。由于 R、t、H 都 W-invariant，完整的一形式有

\[
 W^*\omega_F-\omega_F
 =-\Theta R(t)(20\tau^2+\varepsilon)A^{(\varepsilon)}\frac{dt}{t}.
\tag{D15}
\]

Θ≠0，对任意非零 R 右边不恒等于0。若 Jᶠ_R 是 G-invariant实际函数，其微分必须 invariant，与 D15 矛盾。原点 primitive 确实存在，但不能将其冒充此前 full common cover 上的 weight0 函数；消去 carrier 或改变 cover 仍须真实新证明。这个障碍的范围是未修改的 D3，不排加入适当 period correction 后的别种 primitive。

## 6. 完整分母、有限维意义与仍待闭合的算术接口

在反证假设 L(3,χ₅)=a/b∈Q 下，旧完整模型给 H 前缀固定因子乘 Dₙ³安全分母，Dₙ=lcm(1,…,n)。Rⱼ 的 t-series在 O_K 中 integral：Dε∈O_K[t]且 Dε(0)=1。乘 Rⱼ 不额外增加 LCM 次数。因此

\[
 \boxed{\text{所有 }J_{R_j}^H\text{ 的 coefficient }t^n
 \text{有安全分母 }C\,nD_n^3,}
\tag{D16}
\]

其中固定 C可由旧 H 规范取80b。原点 residue已被完整减去，不含 hidden logt。粗界 nDₙ³|Dₙ⁴合法；若要使用更精细的 CDT integration index e=1，仍须和整个系统、度数窗口、整格选择一起核准，不能只凭 D16 给新函数免费低预算。原旧 species 的 g=Δ² 导数块与本稿 primitive 行也不是同一行；新增积分无需乘 g 来定义，但任何混合消元须重新计极点与 coefficient height。

D12–D14 的有限 de Rham 意义是这个**具体六维 constant 空间**完整注入实际 quotient；没有宣称计算出整个有理 de Rham cohomology 的所有类。真实 Hecke ratios R_p可能落在更小的全p稳定子空间，需要另证，不由一个 T₃ 的 Krylov rank自动决定。本稿覆盖全六维，所以若将来证明其实际子空间维数d，则同样得该子空间的d个非 exact 类。

下一算术问题仍是如何把真实 slow-variable primitive 的 D5 全部项在同一 finite prefix 中消去，以及新的 integral species 能否产生 primitive S2/S3/S4 方向和可接受的成本。本稿没有证明 modp²/³提升，没有把新增函数数目当成免费 Smith rank增益。

## 7. 证书与审阅范围

[最小独立脚本](cdt_odd_level20_cartier_cohomology_20261006_verify.py) 与 [JSON](cdt_odd_level20_cartier_cohomology_20261006_verify.json) 固定核验36项代数身份：Q 的 branch/cusp主部、所有因子分离、两 sign gauge∞项、六类点的 homogeneous/adjoint indicial、实际 coefficient cancellation、∞首系数及 divisor degree矛盾。没有扫描素数，没有 import 或重跑冻结 producer。monodromy、真实函数 rank、完整共同 leaf 与最少项引理依赖正文数学证明，不能由这36个 algebra checks单独代替。

low_period_closure 先独立重推局部指数、finitezero8/pole2、∞growth矛盾及正规 H 的必要 D8，随后实际只读审阅本稿 §§2–4与§5的 primitive-leaf 应用，全部通过。其实际审阅包括最少项归一微分引理、closed B 中 H三系数匹配以及 rank19；未运行证书或 producer。root 亦实际通读 §§1–7，独推 D8/D9、局部表、最少项引理和 background matching，通过。两次审阅都没有把数学身份核验记成算术收益核验。

helper_tensor_budget 实际只读独审 §§2–4，逐点从 Sym²加 gauge 重推三阶/伴随指数、D8系数匹配、两端growth矛盾、最少项微分和 closed background 的 quotient matching，rank10/19范围通过；未覆盖§5完整leaf，未执行36check producer。此独审与 low 的 analytic-leaf 范围分开记录。

本作者另实际只读独审 low_period_closure 的 primitive_leaf §§3–4与§6(18)，重推 fullleaf 抵消、Cayley 的非零 odd primitive 项及 Hecke kernel 的全局 O_K 整性通过；未审该稿§5边界计算或运行其 producer。旧 cartier_kernel §§1/3/4 的实际正文审核另已通过，旧冻结三hash保持不动。本稿最终固定版本的 SHA256 随交付消息记录，不以正文自包含hash。
