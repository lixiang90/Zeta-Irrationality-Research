# 实际二次拉回的反不变强迫：九维非分裂商、完整九周期比较与第二反射

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority 为当前主报告 §195 及 delivery_carry_cartier_split_algebraic，SHA44521a432fd71bdfef7e10a0d3ac63d636878b32aabfad5b293d8276a9fdf4a7。604 冻结记录（599 数学、5 guards）、旧与同行 producer/results/guards、prime 表全部只读；本轮数学 producer 新建/execute/import/rerun、prime 扩表、Lean、数学运行均0。

本文改变上一轮 forcing x，而非继续优化已排除的 rank2/cap9 maps。双 MUM 端点消失的实际 polynomial forcing 有一个准确九维 nonsplit quotient；全部九个比较积分的 kernel 恰为 rational split image，因而一个实际 9×9 complex period comparison matrix 非退化。最低次 forcing x(1−x)(1−2x) 去掉 log9，却仍有可证明非零的 canonical log8 与第二 conifold residual。后两项解释为什么端点取零不等于全 jump 填洞。比较非退化不是九个数的 Q-linear independence，亦不是新的数值无理性。

## 1. 固定原周期、二次 cover 与全部路径约定

**A1（实际对象）。** 本轮实际 FULL 重新读冻结 Gamma G1–G19/七节、dual D1–D17/公式 D1–D30/七节、split U1–U34/十节及 authority §195；不继承以前的原件阅读或执行证据。固定
\[
 a=(\tfrac12^\times5,\tfrac15,\tfrac25,\tfrac35,\tfrac45),\quad
 \Lambda=3200000,\quad c=\Lambda^{-1},\quad D=t\partial_t,
\]
\[
 L=D^9-\Lambda t\prod_i(D+a_i),\qquad
 f_0=\sum_{n\ge0}h_nt^n,\quad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbf Z.
 \tag{A1}
\]
原 finite singularities 为0,c，∞ regular singular；普通 ∂t leading coefficient 为 t9(1−Λt)。φ0,…,φ8 是完整 MUM Frobenius basis，leading term (log t)^j/j!，不是 analytic parts ηj。正实 0<t<c 上 log t 取实值。完整 c reflection 为
\[
 \psi=(T_c-I)f_0,\qquad
 (T_c-I)\phi_j=\kappa_j\psi,\qquad
 \kappa(s)=\frac{\Gamma(1+s)^{15}}{\Gamma(1+2s)^5\Gamma(1+5s)},\quad
 \kappa_0=1 .
 \tag{A2}
\]
其 exponents 为0..7、7/2，T_c²=I，ψ≠0。本轮实际原件 GM PDF1–3 中 PDF2 的 irreducibility criterion 适用：D9 roots0与第二多项式 roots−a_i 无共同整数余类。

**A2（cover 和 bridge）。** 令
\[
 t=x(1-x),\quad w=1-2x,\quad b=\tfrac14,\quad
 \sigma(x)=1-x,\quad w^2=1-4t,
\]
\[
 \delta=\frac{1-x}{1-2x}D_x,\quad D_x=x\partial_x,\qquad
 L_{\rm pb}=\delta^9-\Lambda x(1-x)\prod_i(\delta+a_i).
 \tag{A3}
\]
δ 就是 D_t 的 chain rule，所有 powers/products 按 differential composition，不把其 rational coefficient 当 commuting scalar。MUM preimages 是0、1；conifold preimages
\[
 r_\pm=(1\pm\sqrt{1-4c})/2;
 \tag{A4}
\]
x=1/2 是原 ordinary b 的 critical preimage/apparent scalar singularity；∞ 是原∞的 degree2 preimage。

下面所有 comparison 固定一个明确 bridge。原 t 路径 γ 从0沿正轴出发，在 c 上半平面作小半圆 detour，沿 c<t<b 的 upper boundary 到 b；之后取 detour 半径趋零。w(t)=sqrt(1−4t) 在0取+1，γ 上保持这支。左 inverse X(t)=(1−w)/2 将 γ 提为 x0→1/2、绕 r−上侧的路径。穿过 x1/2 的实际 analytic germ 后，右半 bridge 是反射的逆路径：1−X(t)，t 沿 γ 的逆向从 b 回0；它绕 r+下侧到 x1。这样右端与左端的 φ basis 都按同一 γ 识别，不省略 continuation matrix。

T_c 取正向小 loop；在 c<t<b 的 upper boundary，本约定给 ψ=f0^-−f0^+。其余 loop 的正向亦为 complex orientation。σ 为 holomorphic coordinate change，保持小 loop 方向；右 conifold 的 coefficient 将在上述 reflected basis 中报告。改 bridge 会改变 comparison vector；本文关于 log8 和第二 residual 的数值式、符号和 positivity 均明确限于这个 canonical bridge。

## 2. 双 MUM 消失的 polynomial forcing 有准确九维商

**A3（invariant/anti-invariant decomposition）。** 任意 R(x)∈Q[x] 唯一写成
\[
 R(x)=A(t)+wP(t),\qquad A,P\in\mathbf Q[t].
 \tag{A5}
\]
可先把 x=(1−w)/2 代入，再用 w²=1−4t 降幂。R(0)=R(1)=0 等价于 A(0)=P(0)=0。invariant A∈tQ[t] 全部 split：原一步 recurrence 给
\[
 B_{t^m}=\frac{f_0-\sum_{n=0}^{m-1}h_nt^n}{m^9h_m},
 \tag{A6}
\]
故存在 rational polynomial particular。反不变部分 wP 才是此次新增对象。

**A4（所有 rational anti-particular 的局部约束）。** 考虑 P∈tC[t]。若 T(x)∈C(x)、L_pb T=wP，则在 C(x)=C(t)⊕wC(t) 中 T=r(t)+wq(t)。invariant part 满足 Lr=0；它只能为0。无需猜测 period：rational r 在∞若 leading t^d、d∈Z，Lr 的最高项为 −Λ∏(d+a_i)t^(d+1)，非零，因为全部 a_i 非整数。因此
\[
 T=wq(t),\qquad q\in\mathbf C(t).
 \tag{A7}
\]
在 finite ordinary t≠b，q 的 pole 会使 L(wq) 有 pole order 增9，与 wP analytic 矛盾。0处 negative integer exponent 的 D9 coefficient 非零；c处 negative integer exponent 不在 indicial roots0..7、7/2，也不能有 pole。在 b，令 ord_bq=h∈Z，则 wq 的 leading exponent h+1/2。L ordinary ninth derivative 的 coefficient和 falling factorial (h+1/2)_falling,9 全非零；其它项较低阶，不能取消首项。若 ord_bP=p≥0，
\[
 h+\tfrac12-9=p+\tfrac12,\qquad
 \boxed{\operatorname{ord}_bq=p+9.}
 \tag{A8}
\]
故 q 没有 finite poles，且至少在 b 消失9阶：
\[
 \boxed{q\in(1-4t)^9\mathbf C[t].}
 \tag{A9}
\]
P=0 时同一 half-integer leading argument 迫 q=0。

**A5（充分性和准确 operator）。** 定义实际 conjugate
\[
 L^-:=w^{-1}Lw
 =\left(D-\frac{2t}{1-4t}\right)^9
 -\Lambda t\prod_i\left(D-\frac{2t}{1-4t}+a_i\right).
 \tag{A10}
\]
这是 noncommutative expression。若 q∈(1−4t)^9C[t]，wq 在 b 的 exponent 至少19/2，施行至多9次 ∂t 后除 w 仍 analytic；其它 finite points 无 pole，所以 L^-q 是 polynomial。在0，L(wq) 的 constant 为0，故 L^-q∈tC[t]。从而
\[
 \boxed{wP\in L_{\rm pb}(\mathbf C(x))
 \iff P\in L^-((1-4t)^9\mathbf C[t]).}
 \tag{A11}
\]
若 P rational，triangular leading coefficient 的唯一解也 rational，因此同式可把 C 换成 Q。

**A6（quotient 和实际 basis）。** q degree d≥9 时，wq 在∞ leading t^(d+1/2)，故
\[
 \deg L^-q=d+1,\qquad
 [t^{d+1}]L^-q=-\Lambda\prod_i(d+\tfrac12+a_i)[t^d]q\ne0.
 \tag{A12}
\]
因此 degree≤M 的 target tC[t] 有维数M；其 split image 维数 max(M−9,0)。依次用 q=(1−4t)^9t^j，j≥0，消去 P 的 degree≥10，留下唯一 degree≤9 representative。得到
\[
 \boxed{\mathcal H^-:=
 t\mathbf C[t]/L^-((1-4t)^9\mathbf C[t])
 \text{ 维数恰9，basis }[t],[t^2],\ldots,[t^9].}
 \tag{A13}
\]
同一结论 over Q。原双 MUM-zero polynomial forcing 的 rational-split quotient 亦为这九维空间，因为 invariant part 已由 A6 全消去。最低次 nonsplit actual carrier 是
\[
 R_1(x)=w t=x(1-x)(1-2x).
 \tag{A14}
\]
不是因为“多了一个 conifold”便宣布 nonsplit；A8–A13 给了完整 rational image 的精确证明。

## 3. 唯一 Q-Taylor particular、真实连接常数和全 finite-place cap

**A7（actual Taylor construction）。** 对 P∈tQ[t]，0附近固定 w=+sqrt(1−4t)，令 R_P(t)=w(t)P(t)。唯一 normalized
\[
 LB_P=R_P,\quad B_P(0)=0,\qquad
 b_n=h_n\sum_{m=1}^n\frac{[t^m](wP)}{m^9h_m}.
 \tag{A15}
\]
由于
\[
 w=1-2\sum_{m\ge1}\operatorname{Cat}_{m-1}t^m\in\mathbf Z[[t]],
 \tag{A16}
\]
R_P 在 radius b>c 内 analytic，Taylor coefficients rational；若 P integer，它们全 integer。实际 x-function 是 B(x)=B_P(x(1−x))，满足 L_pb B=wP 且 B0=0。不是把旧 forcing x 的系数移植过来。

**A8（first conifold 完整 fill）。** radius b>c 和原 inverse-coefficient tail estimate 给
\[
 C_P=\sum_{m\ge1}\frac{[t^m](wP)}{m^9h_m},\qquad
 F_P=B_P-C_P f_0
 \tag{A17}
\]
绝对收敛，F_P 实际 holomorphic 于 |t|<b；具体固定 c<q<b 时 coefficient O(q^(-n)n^(-9))。因此
\[
 \boxed{\Delta_{r_-}B=C_P\psi(t(x)),\quad
 \Delta_{r_-}(B-u f_0)= (C_P-u)\psi.}
 \tag{A18}
\]
这是完整 germ，而非只让一个点值或最高 fractional term 为0。C_P 的 ζ/L evaluation 与有理性未知；此处没有声称它是 κ5 或 κ7。

**A9（所有 primes 与 fixed jets）。** 冻结 dual D26–D28 本轮 FULL 回读，并在此重述核心 carry 支付。对 q=p^k，C_q(s)=5floor(2{s/q})+floor(5{s/q})∈[0,9]；h_n/(m9h_m) 的 q-layer 是 C_q(n)−C_q(m)−9·1_(q|m)。q≤n 时至少−9（q|m 时 C_q(m)=0），q>n≥m 时 floor 表达随 s 单调且 q∤m，因此至少0。于是
\[
 D_n^9\,\frac{h_n}{m^9h_m}\in\mathbf Z\quad(1\le m\le n).
 \tag{A19}
\]
integer P 结合 A15–A16 给 D_n9 b_n 整；rational P 只需 fixed denominator M。x(1−x) 是 integer polynomial、贡献 indices≤n 且 D_m|D_n，故
\[
 \boxed{M D_n^9[x^n]B\in\mathbf Z,\qquad
 M_uD_n^9[x^n]\delta^j(B-u f_0(t(x)))\in\mathbf Z}
 \tag{A20}
\]
对每个 fixed j≥0、u∈Q、n≥0 成立，M_u 为 fixed positive integer。δ multiplier (1−x)/(1−2x) 有 integer Taylor coefficients，D_x 只乘 index 整数，因此 finite iterations 不新增 width 或随 n 的 exponential denominator。全部 primes2、5及其它 primes 均包含，不另借素数表。

## 4. apparent point 的真实 analytic lift 和全九项 involution defect

**A10（b 的 ordinary inverse，而非略去 critical point）。** 设 p=ord_bP。original L 在 b ordinary，R_P 为 (t−b)^(p+1/2)analytic。ordinary first-order variation of constants 的 fundamental matrix 和其 inverse analytic；对 half-integer forcing 积分只给 analytic 与 half-integer terms，不给 log。若 particular fractional 首项指数 α，则 ninth derivative 使 α−9=p+1/2；falling factorial 非零。因此
\[
 \boxed{B_P(t)=E_P(t)+(t-b)^{p+19/2}A_P(t),\quad
 LE_P=0,\quad E_P,A_P\text{ analytic at }b.}
 \tag{A21}
\]
也可从 scalar ordinary Green kernel 的 diagonal leading (t−s)^8/8! 积分直接得到该指数，后续 terms 为整数递增。t−b=−(x−1/2)² 后全部 terms 成为 integer x-powers，故 B 的 canonical continuation 在 x1/2 analytic，半整数项为 odd x-series，其 vanishing order 至少19。δ^jB 在 b、j≤8 的 finite limit全部来自 E_P。

**A11（defect 是实际 homogeneous function）。** 在该 critical-neighborhood 的同一个 analytic x-germ 中定义
\[
 H_P(t)=B(x)+B(1-x)=2E_P(t).
 \tag{A22}
\]
L_pb 在 σ 下不变，forcing wP 反号，所以 LH_P=0。继续回 γ 得完整 homogeneous comparison，而不是直觉投影：
\[
 B^\sigma=H_P-B,\qquad
 H_{P,u}:=(B-u f_0)+(B^\sigma-u f_0)=H_P-2u f_0.
 \tag{A23}
\]
σ 作用在 specified continued germ；不把任意 branch 的 H 都当同一 constants。

**A12（actual Green normalization）。** 使用本轮 FULL 回读 dual D3–D8 中的 selfadjoint identity L*=-L（dt/t adjoint）和实际 symmetric concomitant
\[
 D\mathscr B(f,g)=fLg+(Lf)g,\quad
 \mathscr B(\phi_i,\phi_j)=S_{ij}=(-1)^i\delta_{i+j,8},\quad S^{-1}=S.
 \tag{A24}
\]
κ^tSκ=d=16π8/5，ψ column v=−2Sκ/d，故
\[
 \mathscr B(\psi,\psi)=4/d,\qquad
 \mathscr B(\psi,f_0)=-2/d .
 \tag{A25}
\]
这些明确 constants 对应原 unscaled actual basis；没有免费 Tate-normalization 或未知 Betti lattice。

**A13（全部九个 comparison entries）。** 定义 convergent improper integrals
\[
 I_i(P)=\int_\gamma\phi_i(t)P(t)w(t)\frac{dt}{t},\quad i=0,\ldots,8.
 \tag{A26}
\]
0处 P/t analytic、φ_i 至多 log^i；c处 fractional exponent7/2使φ_i bounded；b处 w~(b−t)^1/2，故三个端点都可积，c半圆贡献趋0。Green 从0积分到 b：B=O(t) 使起点 pairing 为0；A21 的 fractional jets 至8全趋0，得到
\[
 \boxed{\mathscr B(\phi_i,H_P)=2I_i(P),\qquad
 H_P=\sum_{j=0}^8 h_j(P)\phi_j,\quad
 h_j(P)=2(-1)^j I_{8-j}(P).}
 \tag{A27}
\]
这支付真正的全九维 comparison column，包括 log8、全部低 log 与 constant homogeneous term；不能用 C_P 单一数值替代。

## 5. 两个 MUM 与两 conifold 的完整 jumps

**A14（log9 去掉后还有完整 MUM gate）。** near x1 的 forcing 是 −w(t)P(t)，constant0，因此存在 analytic particular −B_P(t)。A23 给实际 right germ
\[
 B^\sigma=H_P-B_P,\quad
 \text{highest log degree}\le8,\quad
 [(\log t)^8/8!]B^\sigma=h_8=2I_0(P).
 \tag{A28}
\]
所以 R(1)=0 的作用是去掉 log9；log8 可由 continuation 积分重新出现。MUM monodromy 单一 Jordan block，analytic homogeneous subspace 恰 C f0，故 canonical x1 full jump 为0准确等价于
\[
 \boxed{H_P\in\mathbf C f_0
 \iff I_0(P)=\cdots=I_7(P)=0.}
 \tag{A29}
\]
减 u f0 不改变这些八个 gates。x0 normalized germ 实际 analytic，x1 gate 由全 homogeneous column 决定，不由 endpoint forcing值猜测。

**A15（second reflection 与路径费）。** 对任何 homogeneous H，A24–A25 的 reflection formula 是
\[
 (T_c-I)H=\eta(H)\psi,\qquad
 \eta(H)=\kappa^{\mathsf T}h
 =-\frac{2\mathscr B(\psi,H)}{\mathscr B(\psi,\psi)}.
 \tag{A30}
\]
对 H_P，A27 给
\[
 \eta_P=\kappa^t h(P)
 =-d\int_\gamma \psi(t)P(t)w(t)\frac{dt}{t}.
 \tag{A31}
\]
因此 canonical reflected r+ 的完整 jump 为
\[
 \boxed{\Delta_{r_+}B=(\eta_P-C_P)\psi,\qquad
 \Delta_{r_+}(B-u f_0)=(\eta_P-C_P-u)\psi.}
 \tag{A32}
\]
这里 right basis 是 A2 bridge 的 left φ continuation 经 σ 的识别。小 loop方向保持；没有把两个 conifold coefficients 误认为自动相同。

**A16（精确 residual integral）。** F_P=B_P−C_Pf0 在 c analytic。ℬ(ψ,F_P) 满足 derivative ψR/t；右边在c为 half-integer analytic、可积。其 primitive 为 constant 加 vanishing half-integer term，而 pairing 本身经 c reflection 反号（ψ反号、F_P不变），故 constant0，即 ℬ(ψ,F_P)(c)=0。0处 A25 给 ℬ(ψ,F_P)(0)=2C_P/d。因此
\[
 C_P=-\frac d2\int_0^c\psi(t)P(t)w(t)\frac{dt}{t}.
 \tag{A33}
\]
结合 A31，
\[
 \boxed{\eta_P-2C_P
 =-d\int_c^b\psi^+(t)P(t)w(t)\frac{dt}{t}.}
 \tag{A34}
\]
所以即使 u=C_P 恰填第一 conifold，第二完整 residual 仍是 A34，而非未付的“另一个未知连接常数”。这是真实9维 source 的独立周期 gate；d=16π8/5 与 canonical boundary choice 均明列。

## 6. 全九周期 gate 的 kernel 恰为 rational split：付清全局路径与∞

**A17（comparison map）。** 在 complex polynomial space 定义
\[
 \mathcal J(P)=\left(I_0(P),\ldots,I_7(P),\
 J_c(P)\right),\qquad
 J_c(P)=\int_c^b\psi^+(t)P(t)w(t)\frac{dt}{t}.
 \tag{A35}
\]
下面证明
\[
 \boxed{\ker\mathcal J=L^-((1-4t)^9\mathbf C[t]).}
 \tag{A36}
\]
这不是凭九个首项给 global fill；证明同时使用实际 bridge、全部有限 generators 和∞增长。

**A18（九 gate 零先给 exact anti-involution）。** 若 J(P)=0，A29 给 H_P=λf0，而 η_P=λ，因为κ0=1。A34 的 last gate0给 λ=2C_P。因此
\[
 H_{P,C_P}=0,\qquad F_P^\sigma=-F_P.
 \tag{A37}
\]
F_P 在 left0实际 analytic、r−由 A17 完整 analytic、critical x1/2由 A21 analytic。A37 将这同一 germs 送到 right1与r+，亦全部 analytic。因此沿 canonical bridge 的四个 finite true singularities0,r−,r+,1的实际 full jumps全零；apparent1/2也填入。

**A19（finite generators，不遗漏其它 branches）。** 取 basepoint ε∈(0,r−)。A2 的 x-bridge 是一条 simple arc：先从 ε 绕 r−上侧到1/2，再绕 r+下侧到1。用该 arc 的各段作去四个 punctures0,r−,r+,1的小-loop access paths，附加去1/2的 path。可在 arc 外侧分别取互不交叉的短支段；它们构成这些 finite punctures 的标准 tree-based generating loops。A18证明的是沿这些具体 access paths 得到的 local germs analytic，而非仅有某条无关 path 的 germ fixed。因此所有这些 generators都固定原 F_P。π1(C_x\{0,r−,1/2,r+,1}) 由它们生成，任意 word也固定 F_P；ODE continuation及 monodromy theorem 给一个 single-valued holomorphic function on此 punctured plane，五处的实际 germs均 analytic，故
\[
 \boxed{F_P\text{ 是整个 }\mathbf C_x\text{ 上的 entire function}.}
 \tag{A38}
\]
∞尚未删除，下一步明确支付。

**A20（∞ regular singular 导致 entire particular 为 polynomial）。** 在 |x|大时，δ=b_x D_x，b_x=(1−x)/(1−2x)=1/2+O(1/x)。将 L_pb 左乘1/(1−Λt)，得到 normalized Euler operator \(\widehat L\)，其 Dx各阶 coefficients都在1/x附近 analytic，最高 coefficient→(1/2)^9≠0：δ的lower composition terms及 ratios Λt/(1−Λt) 都有同一有界性质。令
\[
 Q(x)=\frac{wP(t)}{1-\Lambda t}.
\]
P≠0时 Q nonzero rational，D_xQ/Q 在∞ analytic且有 finite limit。于是
\[
 \bigl(D_x-D_xQ/Q\bigr)\widehat L\,F_P=0
 \tag{A39}
\]
是∞ regular-singular 的 order10 Euler equation，最高 coefficient非零。其 Dx-jet first-order system D_xY=M(x)Y 在 |x|大有 bounded M(x)。若 Y 对应 A38 的 single-valued entire F_P，则在固定大圆上所有 derivatives 有 uniform bound；沿每条 radial ray 的 differential inequality给 |Y(re^{iθ})|≤C r^N，C,N不依赖θ，因为 M bounded uniformly。故 |F_P(x)|≤C(1+|x|)^N on全plane；Cauchy estimate迫高于N的 Taylor coefficients0，F_P 为 polynomial。P=0时结论直接成立。

L_pbF_P=wP，结合 A11，P属于 split image，证明 A36 的正向。这一步保留 forcing 的任意高 polynomial degree 和∞ pole；未假设 particular 在∞ bounded，更未仅以“没有新增finite pole”断言 rationality。

**A21（split 反向和 comparison 非退化）。** 若 P=L^-q、q∈(1−4t)^9C[t]，T=wq polynomial x、LT=wP。normalized B=T−T(0)f0，且 A17 在c的完整反射迫 C_P=−T(0)。T 在critical是 odd、至少19阶，故 H_P=−2T(0)f0=2C_Pf0。A27与A34给 I0..I7=J_c=0，反向成立。

A36、A13 因而给一个真正 isomorphism
\[
 \boxed{\overline{\mathcal J}:\mathcal H^-\xrightarrow{\ \sim\ }\mathbf C^9.}
 \tag{A40}
\]
特别列 indexed j1..9、前八 rows i0..7、last row J_c 的实际 matrix
\[
 \mathcal M_{ij}=\int_\gamma\phi_i(t)t^{j-1}w(t)\,dt\quad(0\le i\le7),
 \qquad
 \mathcal M_{8j}=\int_c^b\psi^+(t)t^{j-1}w(t)\,dt
 \tag{A41}
\]
满足 detM≠0。全证明没有 numeric determinant recognition。它是复线性 deRham/continuation comparison 的非退化；不推出 entries、C_(t^j) 或九个数对Q线性无关。一个 nonsplit P若由减一个 C_P f0填 firstc，必至少留下 A29的MUM gates或 A34的 second gate；但不排除允许遗漏某些点的 leaf 或不同 projection。

## 7. 正 forcing 的两个实际 residual 必非零

**A22（八重 Euler representation，自行支付 hypotheses）。** 从 a-list选一个1/2作为 ninth kernel exponent，其余八个 α_i 是四个1/2及1/5,2/5,3/5,4/5。令 U=∏_(i1..8)u_i，probability measure
\[
 d\nu=\prod_{i=1}^8
 \frac{u_i^{\alpha_i-1}(1-u_i)^{-\alpha_i}}
 {B(\alpha_i,1-\alpha_i)}\,du_i .
\]
全部0<α_i<1，Beta integrals convergent。|t|<c 时逐项 absolute expansion和 Beta moments 给
\[
 \boxed{f_0(t)=\int_{[0,1]^8}(1-\Lambda tU)^{-1/2}\,d\nu.}
 \tag{A42}
\]
其 coefficient Λn(1/2)_n/n!∏(α_i)_n/n!恰 h_n；这是实际9F8的 representation，而非借另一参数的 positivity。

在 t upper half-plane，该 kernel取0的principalbranch，dominated continuation给同一 f0。对 real c<t<b，threshold U=c/t∈(0,1)；其两侧均有 positive measure，局部 density 连续且正（可用 u_i=e^{-v_i} 后 positive beta densities 的 convolution），|U−c/t|^-1/2 locally integrable。upper boundary有
\[
 \operatorname{Re}f_0^+(t)>0,\quad
 \operatorname{Im}f_0^+(t)>0,\quad
 \psi^+(t)=f_0^-(t)-f_0^+(t)
 =-2i\,\operatorname{Im}f_0^+(t).
 \tag{A43}
\]
前两项分别由 kernel 的正实部分区间与正虚部分区间积分给出；最后一式使用本 bridge 的正向reflection和 real coefficients。0<t<c时f0>0。

**A23（完整结论及范围）。** 若 P real polynomial、P0=0且 P≥0 on[0,b]、P≠0，则
\[
 \operatorname{Re}I_0(P)>0,\qquad
 J_c(P)\in-i\mathbf R_{>0}.
 \tag{A44}
\]
所以 canonical h8=2I0≠0，nearx1 exact最高log degree8；同时η−2C=−dJ_c≠0，first fill不能填第二 conifold。它覆盖 P=t,t²,…及任意此正锥，不仅一个数值样本。它不是任意 path、任意 map或任意 signed P 的 no-go；comparison仍需逐branch支付，signed P也不能由此直接取得Q coefficient的八fold cancellation。

## 8. 最低次实际 carrier、positive连接常数与 fulljet rank

**A24（concrete C）。** 对 P=t，
\[
 [t]R=1,\quad[t^m]R=-2\operatorname{Cat}_{m-2}\ (m\ge2),
\]
\[
 \boxed{C_t=\frac1{3840}
 -2\sum_{m\ge2}\frac{\operatorname{Cat}_{m-2}}{m^9h_m}.}
 \tag{A45}
\]
h1=3840，h_m/h_(m−1)=Λ∏(1−(1−a_i)/m) 随 m递增，故 h_m≥3840^m。Cat_(m−2)≤4^(m−2)、m9≥1，因而
\[
 C_t\ge\frac1{3840}-\frac2{3840(3840-4)}
 =\frac{3840-6}{3840(3840-4)}>0.
 \tag{A46}
\]
此为 exact all-series lower，没有执行计算或数值猜识。C_t 的有理性及 ζ/L评价仍未知。A28/A44显示 log9确被去掉、log8确非零；A32/A34支付第二 conifold，A21支付apparent；全有限处 A20维持 cap9。

**A25（pullback 不可约，不免费借 finite-index theorem）。** 原基 U=P1_t\{0,c,b,∞}，删掉ordinary b使 quadratic cover unramified；其 subgroupH⊂π1(U) index2，parity由绕b/∞决定。original homogeneous monodromy aroundb为I。对任意 odd parity loop g，乘一个b-loop可变为H中的loop且 monodromy matrix不变。因此
\[
 \rho(H)=\rho(\pi_1(U)).
 \tag{A47}
\]
原 GM irreducibility使此 image在9维solution space不可约，所以实际 L_pb likewise irreducible overC(x)。这个论证支付 branchpoints，也不把一般 irreducibility在任意finitecover无条件沿用。

**A26（实际十行rank）。** P=t的 canonical x1 jump χ1≠0，由A44的log8给出；polynomial forcing single-valued故L_pbχ1=0。对每个固定u∈C，F_u=B−u f0(t(x))的同一 χ1不变，因为 f0沿γ后γinverse回到MUM0的analytic branch。若
\[
 r_*+\sum_{j=0}^8 r_j(x)\delta^jF_u=0,\qquad r_*,r_j\in\mathbf C(x),
\]
continuation差给 order≤8 rational differential operator killingχ1。沿所有loops继续，A47使χ1的orbit张成全部9维L_pb解；一个order≤8 operator不能杀九维ordinarysolutions。因此allr_j=0，再r*=0，故
\[
 \boxed{\operatorname{rank}_{\mathbf C(x)}
 \{1,F_u,\delta F_u,\ldots,\delta^8F_u\}=10.}
 \tag{A48}
\]
不是拿一个order10方程自动当十个function的rank。实际annihilator (D_x−D_xR1/R1)L_pb阶10；上述rank亦迫minimalorder10。对u∈Q，十行有Q Taylor、fixed multiplication后A20的sameallprimecap9。

**A27（只记录已支付的CDT接口，不再搜旧maps）。** 本轮实际CDT v2 PDF66–69核Definition6.0.1/Theorem6.0.2/Cor6.0.14。对A48的fixed10行，取九个 width1 columns (0,1,…,1)^t、e=0，得
\[
 \sigma=(0,9,\ldots,9),\qquad
 \tau^\flat=9(1-10^{-2})=\frac{891}{100}.
 \tag{A49}
\]
各行holonomic，允许relaxedderivativegate，但所有function pullbacks仍须实际meromorphic；A28、A32等fulljumps不能删去。该paidcap不是最小费用。本稿不优化上一轮rank2/cap9maps，不宣布A49可给strictmargin；原ordinaryμ零费参考族的位置也不直接移给本cover。任何更强reference/holonomy bound必须按这个实际base、整coordinate与wholearray重新支付。

## 9. 真正推进与尚未闭合的数值路线

**A28（新增内容）。** 对双MUM端点为0的actualpolynomialforcing，本轮给出全部rational splitimage、准确九维quotient及explicitrepresentatives；completeinvolutioncolumnA27、full两MUM/两conifoldgatesA29/A32/A34；kernelexactsplitA36和comparisonmatrix非退化A41；正forcingcanonical两残余非零；以及最低次actualnonsplitcarrier的rank10、sameDn9cost。forcing两端消失只削log9的原猜测，已被完整period条件取代。

**A29（下一可审查输入）。** 若要从该九维space得到数值irrationality，必须进一步找到某个**rational**P或另一实际projection，使所需relationdependentleaf少留jump，同时证明C_P的ζ/L评价及更强整化/holonomy。M的complexinverse可随意造complexP满足指定comparison条件，但不提供rationalP，更不提供Q-Taylor；A40不能代替这个算术缺口。单一F_C若同时填全部finitegenerators则必split，因而不是保留nonsplitperiod的办法。可以改变periodgeometry或选取允许部分points的真实leaf，但必须支付剩余fulljumps，不能仅将forcing端点设零或将reflectioninvariantpart投影直觉当证明。

原ξ=αζ4+βζ5、κ5/κ7与Catalan等目标均未由C_t或A41得到新的数值结论。本轮无新irrationality/LI/Lean；已证的是实际扩张与完整comparison结构。A40是复线性同构，不是九标量Q-LI，A46是positive不是irrational。

## 10. 真实来源与闭合范围

本轮ownprimary只复用两份既有文件，无下载/重复归档/网络TLS改动、无render：

- Golyshev–Mellit，[Gamma Structures and Gauss's Contiguity, arXiv0902.2003v1](https://arxiv.org/pdf/0902.2003v1)，literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf，SHA239c64b8bab41b12bc2a41d8eb3630d2935e04365bf6a3b9919193793551fc20，171695bytes、10归档页；本人本轮actualFULLtextPDF1–3，3distinct页。PDF2给originalirreducibility/regularsingular/pseudoreflection，pullbackA47自证。
- 固定CDTv2，literature/cdt2024_l2_chi_minus3.pdf，SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771，4517169bytes、218归档页；本人本轮actualFULLtextPDF66–69，4distinct页，用于A49及wholearray/holonomichypotheses。

ownmainprimary为7distinct页，不继承上轮7/42、同行57或整份原件页数。Gamma κ行与Green constants依据本轮actualFULL冻结G/D正文，不冒称本轮独立重读BV公式来源页。EulerA42由Beta moments自证；splitclassification、桥接Green积分、全部generators与∞growth、capcarry及rank均正文纸证，无数学程序。

authorityaudit完整JSONparse/current_progress和physicalSHA核查，604历史记录只读取其冻结状态，不冒称本人逐式全文再审604份。唯一NEW稿待root与assigned正式FULL独审，收审后作者最后FULL回读及单向FINAL来源收据；不pin未来audit或循环receipt，旧文件字节不变。
