# 纯 L(3,χ₅) 的 level-20 完整代数模型与真实秩

日期：2026-10-06。本文接续[两个共轭真实周期](cdt_odd_conjugate_projection_20261005.md)，闭合商曲线、整数坐标、明确微分系统和实际秩。结论是可用于 CDT 的函数模型；没有完成严格 holonomy 矛盾，没有新的数值无理性定理。

上一研究回合保存了两个 embedding 同时 Fricke 正则化的实际身份，本回合因此属于进展：不再需要 level-10 的未知中间 Tate 周期抵消。以下从当前保存的形式出发，并以全局除子和局部指数约束有限系数识别。

## 1. 固定实际函数与假设的精确作用

记 r=√5，K=Q(r)，χ=χ₅，q=e^(2πiτ)，θ=q d/dq。E_k,F_k 及常数 E₂(∞)=−1/5、E₄(∞)=1 按前稿。取

\[
 V_-=E_4-5E_4(2\tau)+4E_4(4\tau)
 -\frac{5r}{4}\{F_4-20F_4(2\tau)+64F_4(4\tau)\},
 \quad A_-=E_2-4rF_2(4\tau),
\]

V₊,A₊ 是上述代数 q 系数的共轭。固定 θ³f±=V±、f±(∞)=0，令

\[
 \Theta=-\frac{5r}{16}L(3,\chi),\qquad
 H_-=A_-(f_--\Theta),\quad H_+=A_+(f_++\Theta).
\]

前稿证明真实身份 f−+20τ²f−(W₂₀τ)=Θ(1+20τ²)、f+−20τ²f+(W₂₀τ)=−Θ(1−20τ²)，且 A± 分别配对同号 Fricke 因子。因此 H± 在正虚轴 Fricke 固定点的二次商上确实正则。

两个函数本身无条件存在。只有假设 L(3,χ)∈Q 时，H± 才是系数共轭的 K[[q]] 芽；以下使用实际函数，而非赋予未知周期任意 Galois 作用。L(3,χ)∈K 不能替代这个假设。

## 2. η 商给出 genus-zero Fricke 商及整数坐标

令 η_j=η(jτ)，定义

\[
 h=\frac{\eta_4^2\eta_5^2}{\eta_1^2\eta_{20}^2},\qquad
 u=\frac{\eta_2^4\eta_{10}^4}{\eta_1^3\eta_4\eta_5\eta_{20}^3},\qquad
 B=\eta_2^2\eta_{10}^2.
\]

Γ₀(20) 的 cusp 分母为 1,2,4,5,10,20，width 为 20,5,5,4,1,1。η 商的 cusp 阶矩阵为

\[
 O_{c,d}=\frac{20\gcd(c,d)^2}{24\gcd(c,20/c)cd}.
\]

h、u 的指数向量分别为 (−2,0,2,2,0,−2)、(−3,4,−1,−1,4,−3)。权为零，两条 η 同余均满足，∏d^(r_d)=1 为平方，故字符平凡。其 cusp 除子分别是

\[
 (-1,0,1,1,0,-1),\qquad (-1,1,0,0,1,-1).
\]

指数在 d↔20/d 下对称，η 变换的常数因子为 +1，所以 h,u 都 W₂₀ 不变。Γ₀(20) 指数36，六 cusp，无 elliptic points，故 X₀(20) genus1。两个函数只有共同的两个简单极点，Riemann–Roch 给该极点除子空间维数2；由 h=q⁻¹+2+…、u=q⁻¹+3+… 得到全局身份

\[
 \boxed{u=h+1}.
\]

这是全局维数和两个首项确定的恒等式，不是以有限 jet 猜测。h 的 degree 是2；W₂₀ 非平凡且 h 不变，故 X₀(20)/W₂₀→P¹_h 的 degree1，Fricke 商确为 genus0。

采用

\[
 t=\frac1{h+1}
 =q-3q^2+4q^3-7q^4+13q^5-20q^6+\cdots,
\]

\[
 q=t+3t^2+14t^3+82t^4+539t^5+3793t^6+\cdots.
\]

η 积的整数系数及首项 q 保证两个方向的全部级数均为整数。三个 cusp 对为：t=0 对应0、∞；t=1 对应1/4、1/5；t=∞ 对应1/2、1/10。

## 3. 椭圆 double cover 和四个分支点

B 是权2 cusp form，其六个 cusp 阶均为1，内部不为零，所以 B dτ 是 genus1 曲线上的处处非零全纯微分。η 变换给 B(W₂₀τ)=−20τ²B(τ)。因此

\[
 y=\frac{\theta h}{B},\quad y(W_{20}\tau)=-y(\tau),
\]

且 y² 是 h 的四次多项式：dh 在两个简单极点各有二阶极点，除此以外无极点。这一全局 degree bound 后，五个有理首项确定

\[
 \boxed{y^2=h^4-8h^3-2h^2-8h+1}.
\]

令 Z=θt/B，便有

\[
 Z^2=\Delta(t)=1-12t+28t^2-32t^3+16t^4=C_+(t)C_-(t),
\]

\[
 C_\pm=1-(6\pm2r)t+(6\pm2r)t^2.
\]

分支值为

\[
 \alpha,\beta=\frac{1\mp\sqrt{(r-1)/2}}2,
 \quad\gamma_\pm=\frac{1\pm i\sqrt{(1+r)/2}}2.
\]

α≈0.106924311、β≈0.893075689、γ±≈0.5±0.636009825i。正实 q 的固定点 τ=i/√20 对应 α。四个点均为简单 branch，三个 cusp 对均未分支。

## 4. 明确二阶统一化方程及两个代数 gauge

令 S=θlog t，Y=√S（q=0 的常数项1），以 t 微分记撇号。Y 与 τY 的 Wronskian 是 (2πit)⁻¹，所以它们满足

\[
 Y''+\frac1tY'+Q(t)Y=0.
\]

Q 是商曲线上的单值 projective connection。四 branch 处局部指数1/4、3/4，Q 的二阶主部3/16；t1 cusp 指数1/2、1/2，主部1/4；t0 最多简单极点；t∞ 满足 Q=O(t⁻³)。因此

\[
 Q=\frac{Q_8(t)}{t(1-t)^2\Delta^2},\quad\deg Q_8\le8,
\]

\[
 Q_8=\frac14(256t^8-1344t^7+3200t^6-4176t^5+3104t^4
 -1316t^3+320t^2-49t+6).
\tag{1}
\]

全局 pole bound 使九个 exact jets 足以证明该式；证书另核更长余项和全部二阶主部。

A±/B 仍带字符 χ，不能直接当 X₀(20) 上的有理函数；但其平方字符平凡、W 不变。B 的 divisor 使平方仅在三个 cusp 值有二阶极点，故其有理分子 degree≤6。七个首项确定

\[
 (A_-/B)^2=
 \frac{[h^2-(4+r)h-4]^2[h^2-(4-2r)h+1]}{25h^2(h+1)^2}.
\]

于是以下是实际 q=0 分支（平方根常数项1）：

\[
 R_-=\frac{A_-}{S}
 =-\frac{N_-(t)}{5(1-t)\sqrt{C_+(t)}},\quad
 N_-=1-(6+r)t+(1+r)t^2,
 \quad R_+=\sigma R_-.
\tag{2}
\]

两者不是可免费删除的字符：R−/R+ 的平方是一个有理平方乘 C−/C+，在四个 branch 值有奇数阶零/极点。

## 5. 完整四维非齐次 connection

设 P=1/t，ρ±=R±′/R±∈K(t)，定义

\[
 a_2=3P-3\rho,
\]
\[
 a_1=3(\rho^2-\rho')-6P\rho+P'+4Q+2P^2,
\]
\[
 a_0=-\rho^3+3\rho\rho'-\rho''+3P(\rho^2-\rho')
 -(P'+4Q+2P^2)\rho+2Q'+4PQ.
\]

这是二阶方程(1)的 Sym² 经 gauge R± 后的三阶算子
\(\mathcal L_\pm=\partial^3+a_2\partial^2+a_1\partial+a_0\)，齐次解析解为 A±、τA±、τ²A±。对实际 H± 有

\[
 \boxed{\mathcal L_\pm H_\pm=U_\pm(t)
 =\frac{A_\pm V_\pm}{(\theta t)^3}\in K(t).}
\tag{3}
\]

forcing 的字符 χ²=1、权6被分母消掉、Fricke 符号为+，因此确实下降。t0 至多二阶极点，t1 至多三阶，t∞为 O(t⁻³)；四 branch 处 AV 因 weight6 的局部奇偶性至少消失一阶，故 U 最多简单极点。这给全局分子 degree≤6 的界。写 U−=(U₀+rU₁)/[t²(1−t)³Δ]，其中

\[
 U_0=\frac{68}5t^6-\frac{148}5t^5+\frac{247}5t^4-10t^3
 -\frac{51}5t^2+4t-\frac15,
\]
\[
 U_1=-22t^5+44t^4-44t^3+27t^2-\frac{21}4t+\frac14.
\tag{4}
\]

U+ 是系数共轭，二者不为零。实际四维 connection 可直接用 (H,H′,H″,1)：第三行导数是 −a₀H−a₁H′−a₂H″+U，第四行导数为零。故全部矩阵条目属于 K(t)，没有隐藏的额外分支函数。A 的零点或 U 的零点造成的 scalar ODE apparent singularities 不代表实际函数在这些位置奇异。

## 6. 实际 rank4、非分裂与联合 rank7

式(3)给出每个循环模 rank≤4。另一方面，未消 cusp t∞ 的 log(t)³ 系数为 −17/120，t1 的 log(t−1)³ 系数为 −17/6；这些值来自前稿全部 cusp 常数，且不依赖 Θ。四次 monodromy translate 的最高对数次数3保证四个实际解 C-线性独立，故任何有理系数 homogeneous ODE 阶≥4。于是

\[
 \boxed{\dim_{K(t)}W_-=\dim_{K(t)}W_+=4}.
\]

这里 W± 是 H± 及其导数的实际函数模，1∈W± 由(3)给出。不能将齐次解 Aτʲ 直接当成 W± 的函数基；它们是对应 homogeneous solution representation。

W±/K(t)·1 是(1)的 Sym² 表示的对偶、再经 R± 二次 twist。Γ₀(20) Zariski-dense 的 projective monodromy 保证其 rank3 irreducible；有限字符 twist 不改变 irreducibility。两个 twist 不同：R−/R+ 非平凡二次 monodromy，而 rank3 为奇数，其 determinant 即检测该字符，所以两个 quotient 不同构。若交在两个 rank3 quotient 中有非恒定像，irreducibility 会强迫这两个 quotient 同构。因此

\[
 W_-\cap W_+=K(t)\cdot1,\qquad
 \boxed{\dim_{K(t)}(W_-+W_+)=7}.
\tag{5}
\]

每个 extension 都非分裂：若拆成 rank3 homogeneous quotient 与常数，cusp monodromy 的最大 Jordan block 只能是3；实际 log³ 强制 block4。

## 7. 返回 Q 系数的实际 trace，而非盲目乘域次数

定义

\[
 T=H_-+H_+,\qquad J=(H_--H_+)/r.
\]

若 L(3,χ)∈Q，T,J∈Q[[t]]。令各 a_i=a_{i,0}+r a_{i,1}，forcing U=\mathsf U₀+r\mathsf U₁（此处包含(4)的共同分母），则完整有理方程为

\[
 T'''=-\sum_{i=0}^2a_{i,0}T^{(i)}-5\sum_{i=0}^2a_{i,1}J^{(i)}+2\mathsf U_0,
\]
\[
 J'''=-\sum_{i=0}^2a_{i,0}J^{(i)}-\sum_{i=0}^2a_{i,1}T^{(i)}+2\mathsf U_1.
\tag{6}
\]

所以 (1,T,T′,T″,J,J′,J″) 是实际 rank7 的 Q(t) connection。其独立性来自(5)，没有把数域次数2直接乘成8。

T 或 J 单独的 cyclic rank 也为7：其在两个不同 irreducible quotient 上的投影都非零，故生成整个 rank6 quotient；若常数方向未生成，则出现 rank6 complement，使 joint extension 分裂，继而各 W± 分裂，与 cusp log³ 矛盾。

trace 不删除目标：若 A_E=E₂、A_F=F₂(4τ)，其 L3 部分分别是 −(25/2)L3·A_F 与 +(5/8)L3·A_E。T(0)=0，J(0)=−L3/8。原始 shifted-prime 三层 packet 的 trace 为2、difference/r 为 −(5/2)χ(p)，均非零。

## 8. 整模型与明确剩余条件

E、F 的整数 q 系数、θ⁻³ 的 n⁻³ 和 q↔t 整数转换，给原始 H 行全部前缀的固定因子乘 L_N³ 安全分母。若 L3=a/b∈Q，可取80bL_N³ 同时清掉 H± 两个坐标的所有系数。证书对 raw Af 的固定因子为20（VF 的1/4不可遗漏）。固定求导只产生有限指标偏移，按 CDT Remark6.0.12 处理。

三层最高 packet 已由前稿全尺度证明，但任意 mixed basis 的最优预算需另证。[算术路线](cdt_odd_level20_arithmetic_20261006.md)讨论 trace、数域和辅助背景；[实际解析叶](cdt_odd_level20_leaf_20261006.md)讨论其余三个 branch 的非正则周期及共同覆盖。只有同一合法函数系统、全部整模型和严格解析界达到 holonomy quotient<实际rank，才能推出新的数值定理。

两个 embedding 的正实 α 叶并不意味着其它 branch 也正则；[实际叶报告 §8](cdt_odd_level20_leaf_20261006.md) 已通过共同 Hecke 群 G=⟨T,W₂₀⟩ 的下降与分歧证明完整共同覆盖存在。两个实际 H 芽及其导数在同一覆盖上分别 holomorphic、meromorphic。数域版本则使用 CDT Remark8.2.42 及 [算术稿的限定闭合系统引理](cdt_odd_level20_arithmetic_20261006.md)，须同时计入两处 embedding。

当前缺口是严格成本余量。[凸性审阅](cdt_odd_level20_convexity_20261006.md) 已对列明的 numerator 逐条给出 Jensen 下界；与原点唯一原像、省略 cusp 1 所给的 log16 上界合并，排除了目前列出的几张预算表。该结论不排除新的背景、随 p 改变的整格、不同返回几何或尚未分析的度量。只有后续真实整模型和同一解析覆盖给出严格 holonomy 矛盾，才能推出数值结论；目标保持未完成。

## 9. 核验与独立审阅

[脚本](cdt_odd_level20_model_20261006_verify.py)与[JSON](cdt_odd_level20_model_20261006_verify.json)执行固定 N48 的82项 exact checks：η 全 cusp divisor/字符/Fricke 指数、整数双向坐标、quartic、两个 gauge 平方、Q 的全 pole 候选、forcing 候选、实际三阶身份和安全分母。全局识别依赖本文的 finite degree bounds，rank 依赖本文的 monodromy 与 irreducibility 证明；有限 jet 不代替它们。

low_period_closure 独立重推 quotient 几何、Q/U 的 pole bounds、固定 N48 Fraction 计算中 Q 的 t⁹…t²⁹ 余项和 U 的 t⁷…t²⁸ 余项、cusp log³、rank4 和两个 rank3 twist 区分，并最终审阅§6–7。详见[书面复核](cdt_odd_level20_review_20261006.md)。报告中(4)采用(1−t)³分母，故与采用(t−1)³的独立 numerator 相差整体负号。
