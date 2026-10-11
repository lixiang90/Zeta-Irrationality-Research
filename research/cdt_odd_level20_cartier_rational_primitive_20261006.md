# level20 零 Cartier 核的有界有理原函数与第二层 off-p 消除

日期：2026-10-06。本稿新增，不改冻结输入。正结论是一个全合适素数的特征p接口：完整Hecke矩阵核中的任意c₀给出正规有理u=J/P_Hasse，degree≤3p−3，满足ϑ(uA₋)=Q_cA₋。因此其第二层非p倍次数项可以用真实旧H最高packet消去；剩余slow-variable余核仍需解决。本稿没有宣称成功的mixed S2行、净Smith收益、nonordinary密度或数值无理性。

## 1. 固定输入、好素数与主结论

使用 [Hasse稿](cdt_odd_level20_hasse_20261006.md) §§2–3、[完整矩阵packet](cdt_odd_level20_cartier_packet_matrix_20261006.md) 和 [native第二层](cdt_odd_level20_cartier_packet_s2_20261006.md)。取K=Q(r)、r²=5、未分歧place𝔭|p、k=O_K/𝔭，p≥7。暂排固定碰撞素数29、1049；完整列表与原因在§5。单独的特征p定理不使用L(3,χ₅)的有理性，也不需排109。随后H packet的算术应用采用原反证假设及固定周期分母条件。

源固定为minus，写

\[
 N=1-(6+r)t+(1+r)t^2,\quad
 C=1-(6-2r)t+(6-2r)t^2,
 \quad D=(1-t)NC,
\tag{R1}
\]

\[
 A=A_-=-N\sqrt C\,\Phi/5,\qquad
 H_p=P_{\mathrm{Hasse}}=\Phi^{1-p}\in\mathbf F_p[t].
\tag{R2}
\]

Hasse的全尺度cusp除子证明给

\[
 \deg H_p=3(p-1)=:h,\quad H_p(0)=1,
 \quad H_p(1)\ne0,\quad[t^h]H_p\ne0.
\tag{R3}
\]

后两个unit来自Hasse在三个cusps均不消失，不能由有限p的coefficients猜测。H_p与N或C可有共同根，不予排除。

令Mₚ是源六basis Bⱼ⁻到匹配target六basis的完整Hecke矩阵。取

\[
 c_0\in\ker\overline M_p,\quad
 P_c=\sum_{j=0}^5(c_0)_jt^j,\quad Q=P_c/D.
\tag{R4}
\]

主要结论为

\[
 \boxed{P_c(0)=P_c(1)=0,\quad\deg P_c\le4,}
\tag{R5}
\]

并存在唯一满足下述有界类与原点规范的rational primitive

\[
 \boxed{u=J/H_p\in k(t),\quad\deg J\le h,
 \quad J(0)=u(0)=0,\quad\vartheta(uA)=QA
 \text{ in }k[[t]].}
\tag{R6}
\]

唯一性指§4给定的pole-bounded primitive类；一般rational primitive仍可加任意相应p-th-power homogeneous项。这里是特征p actual reduction的关系，绝非characteristic-zero actual de Rham exactness。两者并不矛盾。

## 2. p-th powers与relative Cartier：inert place也不能漏项

冻结的坐标Cartier身份给

\[
 \mathfrak C_t(QA)=\sum_i(\overline M_pc_0)_i
                     Q_i^{target}A^{target}=0.
\tag{R7}
\]

𝔠ₜ是k-linear coefficient extraction，作用于dt/t的一形式；absolute Cartier还要取coefficients的p-root。这里先使用relative规范。

由p奇且5∈Fₚ^×，(−1/5)^(p−1)=1。设

\[
 E=N^{p-1}C^{(p-1)/2},\qquad
 \Lambda=A^{p-1}=E/H_p\in k(t),
 \quad\Lambda(0)=1.
\tag{R8}
\]

于是QA=Aᵖ·b，其中

\[
 b:=Q/\Lambda
 =\frac{P_cH_p}{(1-t)N^p C^{(p+1)/2}}\in k(t).
\tag{R9}
\]

如果σₚ表示对formal coefficients施加x↦xᵖ，则Aᵖ(t)=σₚ(A)(tᵖ)。relative抽取的确切规则是

\[
 \boxed{\mathfrak C_t(A^p b)
         =\sigma_p(A)(t)\mathfrak C_t(b).}
\tag{R10}
\]

inert k=Fₚ²时一般σₚ(A)≠A，不能把这个因子错写成A；但它是nonzero unit，因此R7迫𝔠ₜ(b)=0。equivalently，absolute Cartier满足C_abs(Aᵖω)=A·C_abs(ω)，也给同一zero结论。没有在k-linear extraction上重复施加Frobenius。

该推导在formal origin即可完成，R9又是rational function，所以随后可在k(t)中做exactness，不要求给未知周期一个Galois动作。

## 3. rational Cartier zero确为exact，不是只有formal primitive

给出本题所需的elementary证明。F=k(t)具有p-basis t，因k perfect，

\[
 F=\bigoplus_{i=0}^{p-1}F^p t^i.
\]

任意b∈F唯一写为Σvᵢ(t)ᵖtⁱ。对一形式b dt/t，absolute Cartier只保留i=0部分，即v₀ dt/t；relative形式只改变其coefficients的Frobenius识别。formal Cartier zero因此迫v₀=0，且

\[
 v=\sum_{i=1}^{p-1}\frac{v_i(t)^p t^i}{i}\in k(t)
 \quad\text{满足}\quad\vartheta v=b.
\tag{R11}
\]

这证明rational differential\(\omega_b=b\,dt/t\)确为exact。它的所有geometric simple-pole residues因此为0，包括0、1、∞。下面利用这个事实与全部pole order严格控制v的选择；不能从formal termwise积分无条件推出rational或有界primitive。

由R9，0处residue=P_c(0)。1处只有simplepole，residue是P_c(1)乘nonzero因子：H_p(1)、N(1)=−4、C(1)=1都为unit。故P_c(0)=P_c(1)=0。

在∞，R9的denominator degree3p+2，numerator degree≤3p+2。若P_c有非零degree5项，则b∞为nonzero constant，因为H_p的leading及N、C的leading全非零；ω_b在∞便有nonzero residue。exactness迫此项为0，故degP_c≤4。这严格证明R5，没有用old/new spectral decomposition或猜测Hecke核的维数。

R5还说明这个source核包含于固定三维cusp-numerator空间\(t(1-t)k[t]_{\le2}\)。这不是说每个cusp-numerator自动在Hecke核里；剩余Cartier条件仍可能严格限制该空间。

## 4. 从有限pole orders得到u=J/H_p与linear degree界

R5消去0、1的simplepole，并使ω_b在∞全纯。剩余pole只可能在N的两个根与C的两个根。它们在本good范围各自simple且互不相交：

* N root处ω_b的pole order至多p；
* C root处pole order至多(p+1)/2；
* Hasse/N或Hasse/C相交只降低这些pole，不产生新pole。

在分裂域中做partial fractions。simplepole的coefficient为residue，已为0；对pole orderm≥2的项a/(t−a₀)^m，用\(-a/[(m-1)(t-a_0)^{m-1}]\)积分。所有m−1在1,…,p−1中，故division合法。∞没有polynomial part。得到一个∞有限的rational primitivev，pole orders分别至多p−1与(p−1)/2，并加constant使v(0)=0。

该bounded primitive唯一：两个之差导数为0，在algebraic closure rational field中是p-th power；若非constant，其pole重数至少p。但允许的finite poles都严格小于p，且∞不许pole，因此差只能为constant，原点规范再消去。Galois作用保留pole bounds与规范，故这个唯一v下降到k(t)，不用在可能含p的extension degree上作不合法平均。

于是

\[
 v=J/E,\quad J\in k[t],\quad\deg J\le\deg E=h,
 \quad J(0)=0.
\tag{R12}
\]

令u=Λv=J/H_p。由于uA=Aᵖv且ϑ(Aᵖ)=0，

\[
 \vartheta(uA)=A^p\vartheta v
             =A^p(Q/\Lambda)=QA,
\]

证R6。u在∞有限，pole只可能在H_p的根，重数至多该Hasse多项式的原重数；没有独立的N/C denominator。若N/C恰与H_p根相交，仍允许该位置出现由H_p控制的pole。

还有一个可以逐项验证的完整polynomial identity。旧Hasse关系给

\[
 \vartheta A/A=\vartheta N/N+\tfrac12\vartheta C/C
                              +\vartheta H_p/H_p\pmod p.
\]

对u=J/H_p求导后H_p的log derivative恰消，故

\[
 \boxed{NC\vartheta J+
       t(N'C+\tfrac12NC')J
       =\frac{P_c}{1-t}H_p.}
\tag{R13}
\]

右边是polynomial，因为R5。R13与J(0)=0可作为本p有界primitive的exact certificate；不能只检查几个Taylor terms来代替完整身份。其homogeneous bounded解是constant·E，原点规范令其constant为0，与上述唯一性一致。

经实际integer坐标dt/t=S dq/q，R6亦给

\[
 \boxed{\theta_q(uA)=QAS=B_c\pmod p,
        \quad u(0)=0.}
\tag{R14}
\]

这是同一个actual reduction身份。√5、5及χ(p)规范未额外改动；f的首项Norm−109/16不是本primitive构造所需unit条件。

## 5. 固定坏碰撞与全部p的scope

因子norm可精确列出：

\[
 \operatorname{disc}N=37+8r,\quad
 \operatorname{Norm}(\operatorname{disc}N)=1049,
\]
\[
 \operatorname{disc}C=32-16r,\quad
 \operatorname{Norm}(\operatorname{disc}C)=-256,
\]
\[
 \operatorname{Res}(N,C)=-80+60r,\quad
 \operatorname{Norm}\operatorname{Res}(N,C)
 =-11600=-2^4\,5^2\,29.
\tag{R15}
\]

N(0)=C(0)=C(1)=1、N(1)=−4。leading N=1+r、leading C=6−2r，norm分别−4、16。因此可统一排\(\{2,5,29,1049\}\)，并取p≥7。剩余好p时上述factors不降次数、roots simple且不与0/1相交。没有把无限多个可能的Hasse/N、Hasse/C交点排成“固定坏素数”；它们只是numerator cancellation，全部已允许。

这套固定排除不使用谱projectors的13、17、19、47，也不使用nonordinary密度。109仅在另稿firstfcoefficient的unit/no-S2结论中排除，在R6–R14可保留。若将本文应用于p³H的actual arithmetic prefix，仍需加上原反证period denominator与fixed normalizations的有限bad set。

## 6. 第二层off-p确实可消；slowcoker仍须解决

使用native p⁴六积分Z_j=p⁴I_j。对c₀∈kerMₚ，取integral liftĉ₀。深度一给Zĉ₀∈p·prefix lattice，记

\[
 B=Z_{\hat c_0}/p\pmod p,
 \qquad Y=p^3H_-\pmod p=A\,f_\varepsilon(t^p).
\]

整个n<N≤p²前缀的Euler身份给

\[
 \vartheta B=(QA)f_\varepsilon(t^p).
\]

由R6及ϑf(tᵖ)=0，\(\vartheta(uY)\)等于同一右边。因此

\[
 \boxed{B-uY=\psi(t^p)\pmod{t^N},\qquad\psi(0)=0,}
\tag{R16}
\]

其中ψ是唯一slow截断。R16消除了所有non-p次数，但未消去ψ。Ψ可含选择lift带来的Hecke/kernel correction与genuine coordinate缺陷，不能由Cartierzero而宣称它自动为0。

精确的剩余条件仍是第二层稿的Bockstein/coker条件。令E₀为六积分residue评价、T₀为**实际允许**的旧H common-p⁴ baseline1 columns的first-layer image。则存在允许的补正，使完整chosen prefix成为S2，当且仅当

\[
 [B]\in\operatorname{image}E_0+\operatorname{image}T_0.
\tag{R17}
\]

本稿提供uY的具体off-p解，但u是rational而非任意degree预算内的polynomial coefficient。若必须清成旧g=Δ²的实际species，可选择integer lifts\(\hat g,\hat H_p,\hat J\)，写完整source row

\[
 L=\hat g\hat H_p\,Z_{\hat c_0}
       -\hat J\,(p\hat gY).
\tag{R18}
\]

这里p gY正是commonp⁴下旧gH的baseline1列，J不需再人为带p。modp²除p后，R18的residual为

\[
 \boxed{L/p=gH_p\,\psi(t^p)\pmod p.}
\tag{R19}
\]

source新积分coefficients degree≤h+8，旧gH coefficient J degree≤h。这只是一个可实现的clearing方案，未优化degree。multiply gH_p后的residual不再仅有p倍support；不得从R16的pure slow支持误读成cleared polynomial row已经S2。

给定degree预算与原整格，R18可lift到S2的精确条件是其R19 residual属于该**同一**完整evaluation的modp image；亦可允许另外的baseline1旧columns first-layer corrections，按R17扩充image。没有证明这个image条件满足，没有证明新增方向相对旧Smith过滤独立。原始source新积分block含nonzero gH_p c₀，故rowmodp非零，是primitive；这也不等于输出已多消一层。

## 7. 证书和独立审阅范围

本稿完整结论由rational p-basis exactness、全cusp Hasse输入、全部pole order与actual packet Euler身份证明。另附最小fixed algebra证书只核resultants/norm、degree算式和R13的logderivative cancellation，不扫描素数、不执行冻结producer，也不以有限p样本证明R6或S2成功。

root实际只读审阅本稿§§1–7及20-check JSON，通过R8/R9的Λ与inert relative Frobenius、rational p-basis exactness、0/1/∞残数约束、bounded primitive的唯一性与Galois下降、全polynomial R13、q规范R14及R16–R19的off-p/slowcoker范围。root未要求追加素数实验。

helper_tensor_budget实际只读审阅§§2、4，并结合§3/R5的pole输入，通过相对Cartier的σ_p(A)因子、p-basis exactness、有限pole order与partial-fraction积分、∞有界条件及归一唯一性、u=J/H_p的degree/原点条件和R13 cancellation。其审阅允许Hasse与N/C相交，不把这种相交排除为无限坏素数；未执行producer，未审阅slowcoker求解或净Smith收益。

20项固定代数检查由作者执行。上述独立审阅不扩展成S2已闭合或新数值无理性结论。更低degree的旧三导数representation与mixed算术账本另行证明，不由R18的degree界自动推出。本稿与相应PY/JSON现按最终SHA256冻结，后续进展另稿记录。
