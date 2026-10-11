# 第238轮：实际 flag 的多项式扰动、统一截止与一个真实 one-hole 模型

2026-10-08，Dual/C。同源纸证给三项可核资产：每个固定有理g的统一安全截止N=3D+10；真实填点值g₀的全部flag只漏一行，且pivot可由有限组固定多项式minor精确选择；该filled对象的实际费用有一个小的quadratic lower。没有取得满足holonomy预算的费用upper或严格余量，不能以generic g、positive moments或辅助零估计代替新数值结论。数学程序0。

## 1. 对象与实际系数，不借别的周期费用

实际FULL读237最终独立桥10822 B / 4af1493bec05bd98ce370ebbfca6c502566779ca05f789700b36b0c5b794dc9c，以及234实际源9529 B / ca350ab2f584583fe0146684afb112867280d73dc92b44036037945051dc2f03。固定

\[
F=uE,\quad E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
J_g=S(g-2I),\ S=\sqrt{1-4u},\ I'=E/S,\ I(0)=0.
\tag{F1}
\]

源为(1,F,b_gJ_g)，g∈Q固定、b_g>0且b_gg∈Z。记D=m−1≥0，原source dimension为3m。写j_n(g)=[uⁿ]J_g，则

\[
j_n(g)=a_n+g s_n,\quad s_0=1,\quad
s_n=-2\operatorname{Cat}_{n-1}\ (n\ge1),
\]
\[
j_1=-2-2g,\quad j_2=1-2g,\quad j_3=52/15-4g.
\tag{F2}
\]

234完整卷积给a_n∈Q，D_ND_(2N−1)清a_0,…,a_N。这里没有把236的residue A₁=16/3混成actual j₂；早期协调消息曾误报D0校准，立即纠正为下面的3，未据错误常数写稿。

## 2. 全部固定有理g的显式统一 O(1) 截止

忽略固定b_g行尺度，实际system为

\[
\frac d{du}\begin{pmatrix}1\\F\\J_g\end{pmatrix}
=\begin{pmatrix}
0&0&0\\
[2(1-3u)]^{-1}&(2u)^{-1}&0\\
0&-2/u&-2/(1-4u)
\end{pmatrix}
\begin{pmatrix}1\\F\\J_g\end{pmatrix}.
\tag{F3}
\]

它不依g。234(A13)的∞resonance排除J_g=qE+r，对每个g∈Q给实际rank3，不是假设generic rank。连接的安全奇点集为0,1/3,1/4,∞，全部Fuchsian。finite residues的谱分别为{0,0,1/2}、{0,0,0}、{0,0,1/2}；∞ residue为

\[
\begin{pmatrix}0&0&0\\1/6&-1/2&0\\0&2&-1/2\end{pmatrix}.
\]

有限点所有分支指数≥0，∞≥−1/2；logs不降低这些最小幂。也可从F的arctanh与J的integrating factor直接看：0处为常数或u^1/2乘analytic项，1/3是log，1/4是analytic与√(1−4u)，∞至多√u·log u。因此当前CDT Theorem3.2.10中的h≤1/2。该完整主陈述和ε_s定义已实际重读PDF50–54；没有重证Chudnovsky原定理。

用degree<D′的原文约定D′=D+1，保守计四个连接奇点，得到

\[
\nu_{\max}\le3(D+1)+2\binom32+3/2=3D+21/2.
\]

故 **N=3D+10覆盖全部actual jumps，对每个固定有理g成立**。如只计更少奇点或实际leading exponent消失，这一安全upper只会更宽。它支付统一有限截止，不证明critical N=3D+2正好单射。

## 3. 同一 actual Taylor square 变成混合 Hankel

先用常数行的m个monomial columns消掉Taylor0,…,D，再分别反序F/J的m列。两次反序总符号为(−1)^(m(m−1))=1。tail row n=D+1+i、column j=0,…,m−1恰为

\[
K_D(g)_{i,\cdot}=
\big(\mu_{i+j},\ j_{i+j+1}(g)\big)_{j=0}^{m-1},
\quad \mu_k=\frac{3^k}{2k+1}.
\tag{F4}
\]

对任意2m个tail row组成的I，置Δ_(I,D)(g)=det K_D(g)_I。则Δ∈Q[g]、degree≤m；每个J column都必须保留完整a_n，不能只取gS。实际jump row集I_D(g)满足

\[
\boxed{\det T_{\rm actual\ jumps}
=b_g^m\Delta_{I_D(g),D}(g),\qquad
\mathcal A_D=-m\log b_g-\log|\Delta_{I_D(g),D}(g)|.}
\tag{F5}
\]

第一组m个Taylor rows恒为pivots；F3确保N内还可选全部2m个tail pivots。I_D是实际prefix rank增长选择，不是任选一个nonzero minor或假定generic g。

例如D0有三个2×2tail minors（下标为删掉的row）：

\[
\Delta_{2,0}=3,\quad
\Delta_{1,0}=106/15-2g/5,\quad
\Delta_{0,0}=5/3-2g/5.
\tag{F6}
\]

g=53/3是固定有理数，使Δ₁恰零；actual Δ₂仍非零。故“某多项式不是零多项式”不能证明它在每个固定有理g非零，更不能替代actual pivot。最高g项来自F与S−1的mixed moments；m1时其一阶均值都为1、leading det=0，所以连最高次数也不能免费断言恰m。

## 4. 真实填点值的正 compact moment 与 perturbation

记g₀=2I(1/4)，积分有限。234冻结canonical填点及F1说明g₀=目标𝔱；这里只沿用这一实际身份，不扩大到全部到达叶。对0≤u<1/4，

\[
J_{g_0}=2S(u)\int_u^{1/4}\frac{E(v)}{S(v)}\,dv.
\]

E的正measure为dμ(x)=dx/(2√3√x)，0<x<3。令R=J_(g₀)/(1−4u)。先换w=√(1−4v)，再w=S(u)y，得到正双积分

\[
R(u)=\int_0^3d\mu(t)\int_0^1
\frac{dy}{1-t/4+(t/4)(1-4u)y^2}.
\]

设x=4ty²/(4−t+ty²)，x∈[0,t]。Jacobian连同分母给

\[
R(u)=\int_0^3\frac{w_R(x)\,dx}{1-ux},\quad
w_R(x)=\frac{\int_x^3 dt/[t\sqrt{4-t}]}
{\sqrt3\sqrt{x}\sqrt{4-x}}.
\tag{F7}
\]

写a=atanh(1/2)>0、v(x)=2√(4−x)[atanh(√(4−x)/2)−a]，则w_J=(4−x)w_R>0、w_J=v·dμ/dx。R(0)=g₀，所以

\[
J_{g_0}=g_0-u\int_0^3\frac{w_J(x)\,dx}{1-ux}.
\tag{F8}
\]

所有g的扰动仍完整保留：

\[
j_{n+1}(g)=-\int_0^3x^nw_J(x)\,dx
-(g-g_0)\int_0^4x^n\frac1\pi\sqrt{\frac{4-x}{x}}\,dx.
\tag{F9}
\]

最后一个measure的moments为2Cat_n；可由beta integral直接算出。因此g≠g₀并非同一个compact support[0,3]模型；不能将下面filled零估计免费外推forall rational g。反证目标g₀∈Q时，F8恰是该固定有理源，足够使用其真实flag。

## 5. 不是标准 Nikishin：两个外cuts的符号不同

在Ω=C\\((−∞,0]∪[4,∞))中，v由(0,3)的正值指定。upper boundary为

\[
\Im v(t+i0)=
\begin{cases}
-\pi\sqrt{4-t},&t<0,\\
+2a\sqrt{t-4},&t>4.
\end{cases}
\tag{F10}
\]

右侧必须是正号：√(4−(t+i0))=−i√(t−4)，atanh(−iy/2)=−i atan(y/2)。因此ρ=−Im(v+)/π左正右负。二者的convex hull又是整实轴；ρ本身还以√|t|增长，不是具有所需finite moments的单一constant-sign Nikishin生成测度。

实际完整读缓存Fidalgo Prieto–López Lagomasino 1009.1922v1 PDF1–4：Definition1.2要求constant-sign finite measure、consecutive convex intervals至多端点相触，Theorem1.1还要求指定finite moments。这里不匹配，未借该theorem的perfection。即使两种source moment本身正，也不等于外部Nikishin生成measure满足条件。

Root初拟degree2m除子后的正性proof在这处失效：该Z在两个外cut皆正，ρ/Z仍异号。下面保留正确符号重作，不把撤回的equal-index AT当成资产。

## 6. 一个自足 one-defect zero estimate

设H=A+Bv，A,B∈R[x]、degree≤m−1，不全零。若H有2m+1个不同内zeros，令Z=∏(x−x_j)、degree2m+1。这些zeros取消H/Z的内poles；在∞，

\[
H/Z=O(z^{-m-3/2}).
\]

围绕两个外cuts的contour，对k=0,…,m−1给

\[
\int_{(-\infty,0)\cup(4,\infty)}
\frac{t^kB(t)\rho(t)}{Z(t)}\,dt=0.
\tag{F11}
\]

尾端integrand为O(|t|^(−5/2))或更快；0处至多log项，小圆O(ε|logε|)，4处sqrt项小圆消失。没有遗漏∞ residue或endpoint项。取这些等式的B线性组合，得∫B²ρ/Z=0。但Z左负右正，故ρ/Z在两cut都严格负；除B≡0外不可能。若B≡0，A也不可能有这么多zeros。因此H至多2m个不同内zeros。

这只比AT所需2m−1多一个，未证明perfection。对filled F4，假设tail rows i=0,…,2m的2m列不满rank，则有非零A,B，使H=A+Bv与x⁰,…,x^(2m)在正μ下全正交。通常sign-change论证迫使至少2m+1个内sign changes：若较少，乘其变号点的多项式会使积分严格同号。H在端点的power/log发展保证可用此论证，且w_J可积。与F11矛盾，所以

\[
\boxed{\operatorname{rank}K_D(g_0)_{0,\ldots,2m}=2m.}
\tag{F12}
\]

## 7. 实际one-hole及确定性pivot规则

前m个tail rows的μ Hankel block正定，所以其prefix rank逐行增加。F12意味着在0,…,2m的2m+1行中恰有一个dependent row h，且m≤h≤2m。令Δ_(h,D)为删除tail rowh的square minor，则

\[
\boxed{h_D=\max\{h:\Delta_{(h,D)}(g_0)\ne0\},\quad
V_D(g_0)=\{0,\ldots,3D+3\}\setminus\{D+1+h_D\}.}
\tag{F13}
\]

证明：signed maximal minors给唯一row relation；其最高非零coefficient的位置就是第一个prefix dependence，以后每行均增rank。该位置以下的rows不能已有另一个relation。因而actual square为F5的Δ_(h_D,D)，没有generic-value选择。

若Δ_(2m,D)非零，critical0,…,3D+2就是actual jumps；若它零，则另一实际row补齐。没有支付Δ_(2m,D)对所有D非零、全部multi-indices normal或exact各minor的sign。F12–13对真实实数g₀成立；假设g₀∈Q后，它是所需rational actualflag，不是对所有g的one-hole theorem。

## 8. 小的真实费用lower、现有upper与未付预算

filled moment中所有supports在[0,3]。取monic shifted Chebyshev q₀=1、q_i=2(3/4)^i T_i(2x/3−1)，i≥1。分别在两column组换monic polynomial basis，det1；全部tail rows作unit lower-triangular monic换基。唯一left kernel的最高支撑是actual missing row h，它是此前rows的组合。因此r>h的monic q_r中即使出现x^h，也只增加较早的selected rows；selected square的变换仍unit triangular、det不变。普通任意deleted h未必有此性质，这里明确使用F13的actual selector。

行degrees sum为m(2m+1)−h，column degrees sum为m(m−1)，共3m²−h。两measure总质量固定有限，Hadamard给

\[
|\Delta_{h_D,D}(g_0)|
\le (3/4)^{3m^2-h_D}\exp(O(m\log m)).
\]

由F5，对固定b_g₀得

\[
\boxed{\mathcal A_D(g_0)\ge
3\log(4/3)D^2-O_{g_0}(D\log D).}
\tag{F14}
\]

这是同对象actualflag的lower，只说明费用不免费；常数不足以排除holonomy margin，也不能将它当upper。

对一般实际I_D(g)，F2/F4给多项式minor分母：
q_E=D_(2N−1)、q_J=D_ND_(2N−1)，则
q_E^m q_J^m Δ_(I,D)(g)∈Z[g]。
固定g=a/b时，b^m再清值分母。因此仅沿nonzero actual minor有
A_D≤15D²+o(D²)；236完整hybrid Γ通过237桥给更好的45D²/4+o(D²) upper。后者仍仅safe upper，F12不会减掉实际prime费用。由固定小圆Cauchy与Hadamard，可得这些polynomial coefficients和清分母numerators高度exp(O(D²))；这是size上界，不是评值在fixedg离roots的下界。

F14与45/4之间尚没有满足基本/凸BC严格预算的费用upper。真正还欠F13实际选中minor的全阶arith/content或value下界，并与同一合法图实能量比较。正moment、one-hole、g-polynomial degree或O(1)零估计均不单独付这项。没有恢复W扫描、继承c4费用或声称新数值定理。

实际读域与来源身份见 literature/actual_flag_sources_round238_20261008/dual_reading_scope.md。数学程序0；本稿与scope保存后实际FULL作者自读，再报bytes/SHA。

