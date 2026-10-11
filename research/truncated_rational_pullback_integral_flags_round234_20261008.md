# 第234轮：新有理拉回源的完整LCM标志与真实前缀费用

2026-10-08，Packet/B。以实际FULL读取的233 normalized最终稿5162 B / SHA256 9bea4ac690ca0ec4d65824b1568a1e57f61ea73e1655f5b9c4c314ab7e9936b7为输入。新增纸证：完整Taylor安全模型可从d_(2N)²改善为d_Nd_(2N−1)；正确移位后合法三行LCM数组给τ=7/3。两个非恒定行的真实前缀率分别为2、3，亦有具体素数层强迫；不把这些率当最优联合τ。数学程序0，无扫描/旧producer，不修改233或恢复已停W。

## 1. 固定实际新目标与拉回

原native源C(z)=(1−z)⁻¹ᐟ²、P(z)=Σρ_lzˡ满足
2(1−z)P′−P=r(z)，其中
r_l=∫₀¹(1−3t²/4)ˡdt。
新的目标是

\[
\mathfrak t=\frac52L(2,\chi_{-3})-\frac{\pi\log3}{3\sqrt3}.
\]

它不同于V∈Q及T∈Q的假设。固定g=a_g/b_g∈Q，b_g>0约分，记

\[
Z(u)=\frac{4u}{4u-1},\quad
S(u)=C(Z(u))=\sqrt{1-4u},\quad
J_g(u)=P(Z(u))+gS(u).
\tag{A1}
\]

所有native分支在0归一化。此前只支付g=𝔱时canonical路径上u=1/4局部填点，未支付全部到达叶或共同图。这里固定使用新u坐标；不能去掉y坐标的3ⁿ费用后沿用其位置、导数或实处预算。

r的完整拉回可以直接在积分中计算：

\[
r(Z(u))=(1-4u)E(u),\qquad
E(u)=\int_0^1\frac{dt}{1-3ut^2}
=\sum_{n\ge0}\frac{3^n}{2n+1}u^n
=\frac{\operatorname{atanh}\sqrt{3u}}{\sqrt{3u}} .
\tag{A2}
\]

常数项为1。求导Z′=−4/(1−4u)²给精确ODE

\[
J_g'+\frac2{1-4u}J_g=-2E,\quad J_g(0)=g,
\qquad
2uE'+E=\frac1{1-3u}.
\tag{A3}
\]

所以这个完整源包含常数1、E和J，而不是只记某个有限残差或丢掉r的非齐次通道。

## 2. 完整积分公式与所有prime powers的安全模型

写S(u)=Σs_nuⁿ、S⁻¹(u)=ΣB_nuⁿ。有

\[
s_0=1,\quad s_n=-2\,\mathrm{Cat}_{n-1}\in\mathbb Z\ (n\ge1),
\qquad B_n=\binom{2n}n\in\mathbb Z .
\]

Catalan整性可由
Catₙ₋₁=binom(2n−2,n−1)−binom(2n−2,n)
直接核。故S及S⁻¹均为Z[[u]]的常数项1单位，没有隐藏的2或3分母。

ODE给同一完整源的公式

\[
J_g=S(g-2I),\quad
I(u)=\int_0^u\frac{E(v)}{S(v)}\,dv
=\sum_{n\ge1}\frac{u^n}{n}
\sum_{j=0}^{n-1}\frac{3^j}{2j+1}B_{n-1-j}.
\tag{A4}
\]

积分从0开始，无省略常数或有限头。明确的第n项为

\[
[u^n]J_g=g\,s_n
-2\sum_{\ell=1}^n\frac{s_{n-\ell}}{\ell}
\sum_{j=0}^{\ell-1}\frac{3^j}{2j+1}B_{\ell-1-j}.
\]

令d_N=lcm(1,…,N)，d₀=1。以下N≥1；N=0的系数由b_gJ_g(0)=a_g已清整。对于n≤N，外分母ℓ≤N、内奇分母2j+1≤2N−1；全部项的乘积分母均被d_Nd_(2N−1)清掉。因此

\[
b_gd_Nd_{2N-1}\,[u^n]J_g\in\mathbb Z
\quad(0\le n\le N).
\tag{A5}
\]

这是覆盖全部系数、2、3及所有prime powers的完整prefix upper，不是只处理首次增长素数。外层ℓ依赖卷积下标，不能把d_N改说成单个第n项的literal n因子。用d_(2N)而非d_(2N−1)只作合法宽松上界。

## 3. +1必须付清：正确完整tuple与τ

原生E的第N项为3ᴺ/(2N+1)。若2N+1=p>3为素数，它有真实p极点而d₂ₙ无p。因此不能以“+1只改O(logN)”直接声称E具有精确slope2型。

取明确新tuple

\[
f_1=1,\qquad f_2=uE(u),\qquad f_3=b_gJ_g(u).
\tag{A6}
\]

f₂的第n≥1项为3ⁿ⁻¹/(2n−1)，常数项0，故d₂ₙ清其每项。f₃由A5被d₂ₙdₙ清。常数项f₃(0)=a_g已整。因此CDT合法矩阵的两列恰为

\[
b=\begin{pmatrix}0&0\\2&0\\2&1\end{pmatrix},
\quad \sigma=(0,2,3),\qquad
\tau(b)=\frac{1\cdot0+3\cdot2+5\cdot3}{9}=\frac73 .
\tag{A7}
\]

这两列都是LCM slopes，不是literal n或n²。旧安全表两列(0,2,2)、(0,0,2)的26/9，现已被同一完整源的7/3安全表改善。

从r(Z)换成E使用1−4u的正逆，它们都在Z[[u]]且常数项1；uE又是明确的一项移位。它们是可逆Q(u)换源，共同meromorphic图类及Q(u)-rank保持（源native芽均解析），但数组必须按A6重新付，而不是免费更名。固定b_g的常数清分母不改变slopes；去掉固定3是从y=3u的完整坐标变换所得，仍不能沿用旧y图。

## 4. 单行真实prefix费用是sharp：2与3

记δ_F(N)为含0,…,N的最小共同分母。对f₂=uE，有精确式

\[
\delta_{uE}(N)=
\frac{D_{\rm odd}(2N-1)}{3^{\lfloor\log_3(2N-1)\rfloor}}
\quad(N\ge1).
\tag{A8}
\]

每个奇p≠3的最高幂pᵃ≤2N−1，在n=(pᵃ+1)/2处出现分母pᵃ且分子是p单位，给下界；上界逐项显然。3处没有分母，因为v₃(2j+1)≤j（2j+1≤3ʲ，j≥1），分子3ʲ支付全部深度；2处所有分母奇数。故logδ_(uE)(N)=2N+o(N)。

对J先取任意p>3、p∤b_g，n=p，k=(p−1)/2。A4里唯一inner p极点是j=k，且

\[
B_{p-1-k}=B_k=\binom{p-1}k\equiv(-1)^k,\qquad
p^2I_p\equiv(-3)^k,\qquad
p^2J_{g,p}\equiv-2(-3)^k\ne0\pmod p.
\tag{A9}
\]

其它I_ℓ、ℓ<p最多只有简单p极点，S全整；g项亦p整，所以卷积不能消去这一个p²主项。该第p项真实估值恰−2。

再取N<p≤2N−1、p>3、p∤b_g，h=(p+1)/2≤N。此前系数p整，第一inner p极点在j=h−1；故

\[
pJ_{g,h}\equiv-\frac{2}{h}3^{h-1}
\equiv-4\cdot3^{(p-1)/2}\ne0\pmod p .
\tag{A10}
\]

从A9–A10得到
logδ_J(N)≥2θ(N)+θ(2N−1)−θ(N)−O_g(1)
=3N+o(N)；
A5及PNT给相同upper。因此

\[
\log\delta_{J_g}(N)=3N+o(N)
\quad\text{对每个固定 }g\in\mathbb Q.
\tag{A11}
\]

有限g坏prime不改主率。此处lower只用p和p²，upper则已覆盖全部powers；没有假称每个pᵃ的深度都已最优。

固定2还可精确核：因B_m在m≥1时偶、E_j的2-adic值为单位，A4中每个I_n的内和为2单位。因此v₂(−2I_n)=1−v₂(n)。乘S及其整数逆保持整个prefix LCD，故v₂δ_J(N)=max{v₂(b_g),⌊log₂N⌋−1,0}。固定3没有从E的整性免费消失：例如直接递推给J_{g,3}=52/15−4g，g为3整数时此项恰有简单3极点；所有更深幂仍由A5安全支付，而未作最优断言。

特别A10在h=(p+1)/2证明：不能把inner奇分母长度2n−1直接降为n，即使乘固定scalar或任意固定literal nᵉ（p∤h）。无界p来自普通素数无穷性，不使用prime扫描或Wieferich条件。

## 5. 一个精确joint首层；不冒称完整D源最优

若N<p≤2N−3且p>3、p∤b_g，则h=(p+1)/2、h+1≤N<p。全部prefix至多simple p极点，且A3给

\[
p[u^h](uE)\equiv3^k,\quad p[u^{h+1}](uE)\equiv0\pmod p,
\]
\[
pJ_{g,h}\equiv-4\cdot3^k,\qquad
pJ_{g,h+1}\equiv\frac{16}{3}\,3^k\ne0\pmod p .
\tag{A12}
\]

第二式可将A3取第h项：4h−2≡0、p r(Z)_(h)=−4·3ᵏ，得到
(h+1)pJ_(h+1)=8·3ᵏ，而h+1≡3/2。因b_g为p单位，两个非恒定行在h、h+1的残差矩为单位。

于是对**常系数、degree0**的完整源格
Λ₀,p={v∈Z_p³: v₁+v₂uE+v₃b_gJ_g 的0,…,N系数全p整}，
恰有Λ₀,p=Z_p×pZ_p×pZ_p，指数p²。该最高层不依赖g的真值；一个首项的比例−4不代表整个prefix只有rank1。

这仅是已付常系数格的精确statement。没有从它外推degreeD多项式源、所有holonomy flags或最优联合τ。A11是单行LCD主率，不等于A7的τ，更不能由它排除新的joint lattice或fine/all-place改进。

## 6. 函数rank与一种会丢掉目标优势的便宜换源

A3给{1,E,J_g}的rational微分闭包，故全部函数holonomic。它们在Q(u)上实际rank3，对每个g成立。证明：E在u=1/3有非零log项，故E非rational；若J_g=qE+r，q,r∈Q(u)，A3迫使

\[
q'+\left(-\frac1{2u}+\frac2{1-4u}\right)q=-2.
\tag{A13}
\]

系数在∞为−1/u+O(u⁻²)。若rational q的∞ degree>1，左侧有非零非常数主项；degree≤0时趋0；degree1时常数主项相消，左侧仍趋0。三者都不能等于−2。因此无q，rank3；A6的移位和常数清分母保持该rank。此为actual函数rank，不代替Betti/Hodge或完整共同图。

虽然S和S⁻¹都是整数Taylor单位，除以S给
J_g/S=g−2I，其第n项看似具有更便宜literal n形式；但是带常数1的family满足
span_{Q(u)}{1,J_g/S}=span{1,I}，不再依赖g的真值。实际g=𝔱时J_g在被填u=1/4叶vanish且analytic；它不是零函数（A3的非零E强迫），故此处有有限整数消失阶，除S会重新引入半整数branch。它不是保持已付共同图的免费Q(u)gauge。本文因此不沿用J的标记来领取这个新family的费用。

## 7. 本轮准入结论与实际scope

新Q系数源已付A5–A7的完整较锐type和actualrank3；不是26/9旧表，也不是只有safeupper和realupper的计划。A9–A12给真正费用强迫及常系数joint首层，均不宣称7/3为最优所有联合模型。

当前CDT仍要针对同一tuple给全transported叶上的共同holomorphic φ，并使pullbacks meromorphic；已付holonomicity下，基本判据要求log|φ′(0)|>7/3及
3[log|φ′(0)|−7/3]>J(φ)才能构成rank矛盾。局部canonical填点、单行prefixLCD或A12都没有支付这两项。不把一个合法safeτ自动当新数值定理，也不以本源安全失败排除目标𝔱/其它源。

实际FULL读取233 normalized5162/9bea4…；CDT primary本轮实际FULL读已有物理PDF16–20选页文本（包含Theorem2.5.1与(2.5.2)完整条件），另读当前保存PDF23–24选段核一般LCM类型语境，不称全文审220页。来源复用记录另存本轮packet scope。A2–A13均为本轮独立纸证；Root另独立给出A4及A9–A10接口后，本人逐项手核。数学程序0，无CAS/PSLQ/prime或参数扫描、无旧producer执行，只NEW234稿及来源记录。保存后实际FULL作者复读，另报bytes/SHA。

