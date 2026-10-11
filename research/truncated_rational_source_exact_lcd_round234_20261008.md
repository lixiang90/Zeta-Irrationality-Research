# 第234轮Root：有理源的完整积分模型与精确分母增长

2026-10-08。以本轮实际FULL读取的233规范化源为起点，纸面推导；数学程序0。新的标量目标仍是
\[
t=\frac52L(2,\chi_{-3})-\frac{\pi}{3\sqrt3}\log3.
\]
尚未证明t无理，以下只支付同一函数源的确切算术和一个基本CDT证书的准入检验。

## 1. 比Fourier通用上界更短的完整模型

记原生r(z)=Σr_lz^l，P(z)=Σρ_lz^l，C(z)=(1−z)^(-1/2)，
H_g=P+gC；g=a_g/b_g为固定有理数。原实际递推给
\[
2(1-z)H_g'-H_g=r(z),\qquad
r(z)=\int_0^1\frac{dv}{1-z+(3z/4)v^2}.
\]
取Z(u)=4u/(4u−1)，J_g=H_g∘Z。直接代入完整积分，得到
\[
r(Z(u))=(1-4u)E(u),\qquad
E(u)=\int_0^1\frac{dv}{1-3uv^2}
=\sum_{j\ge0}\frac{3^j}{2j+1}u^j.
\tag{R1}
\]
由于Z'=-4/(1−4u)^2、1−Z=1/(1−4u)，
\[
J_g'+\frac2{1-4u}J_g=-2E.
\]
令B(u)=√(1−4u)，B(0)=1，积分因子给
\[
J_g=B\left(g-2I\right),\qquad
I(u)=\int_0^u\frac{E(s)}{B(s)}\,ds.
\tag{R2}
\]
这保留完整log/周期身份，没有删有限头；g=t时的canonical u=1/4填点仍沿233证明，尚未升格到所有路径。

B与1/B都在Z[[u]]：1/B=Σ binom(2k,k)u^k；B的n≥1项是−2Cat_(n−1)，为整数。因此乘B或1/B不扩大任何prefix的整数清分母。

## 2. 完整安全LCD：只需D_N D_(2N−1)

设D_N=lcm(1,…,N)。从R2逐系数得
\[
I_n=\frac1n\sum_{j=0}^{n-1}
\frac{3^j}{2j+1}\binom{2(n-1-j)}{n-1-j},\qquad n\ge1.
\tag{R3}
\]
外分母n≤N，内奇分母2j+1≤2N−1；所有分子均整。因此
\[
b_gD_ND_{2N-1}
\]
清J_g的整个prefix 0,…,N。这里包括所有素数及其全部幂。
相比233的b_gD_(2N)^2，PNT给安全对数增长从4N降为3N。
这是从新源的完整积分模型直接推出，不是把一次积分的外分母也扩大到2N。

若用函数组(1,uE,b_gJ_g)，uE的第n≥1项为3^(n−1)/(2n−1)，由D_(2n)清。
J_g第n项由D_n D_(2n−1)清，因而D_nD_(2n)也清。
CDT基本数组可逐n取两列
\[
(0,2,2)^T,\qquad (0,0,1)^T,
\tag{R4}
\]
即σ=(0,2,3)、τ=(3·2+5·3)/9=7/3。
不能直接对未移位E写D_(2n)：在p=2n+1时它确有新分母。uE与E在Q(u)上只差有理因子，meromorphic适用性不改变；原点处仍为Taylor芽。
R4是一个已经付清的安全函数组类型，不是最优联合整格的证明。

## 3. 同一标量prefix的增长3是精确的

令δ_g(N)为使J_g的前N+1个系数都成为整数的最小正整数。排除有限素数2、3及b_g的因子。以下对每一个剩余素数成立，不使用好素数密度假设。

首先取n=p，k=(p−1)/2。R3的唯一内层p分母来自j=k；所有其它内层分母都为p单位。故
\[
p^2I_p\equiv3^k\binom{p-1}{k}
\equiv(-3)^k=:\eta_p\ne0\pmod p .
\tag{R5}
\]
因为l<p时I_l的外分母为p单位，且内层至多有简单p极点，B(g−2I)的第p项最深层仅来自B_0I_p，给
\[
p^2[J_g]_p\equiv-2\eta_p\ne0\pmod p.
\tag{R6}
\]
因此每个p≤N都强迫δ_g(N)含至少p²。gB是p整，不能在这个最高层相消。

对N<p≤2N−1，设h=(p+1)/2≤N，k=h−1。I_l在l<h时没有内层p分母；在I_h首次出现j=k，二项式为1，外分母h为p单位。因此
\[
p[J_g]_h\equiv-\frac{2\cdot3^k}{h}
\equiv-4\cdot3^k\ne0\pmod p .
\tag{R7}
\]
每个这样的p都强迫至少一个p因子。两窗口合并，固定有限例外不影响线性主项：
\[
\log\delta_g(N)\ge
2\vartheta(N)+\vartheta(2N-1)-\vartheta(N)-O_g(1)
=3N+o(N).
\]
上一节全幂安全LCD同时给反向upper，遂得精确结果
\[
\boxed{\log\delta_g(N)=3N+o(N).}
\tag{R8}
\]
这不是J_g某一个系数分母的结论，而是完整prefix。也不宣称每个小素数的精确幂已算出；它们的总效果已由upper夹住。它关闭“再压低同一标量prefix线性主率”的方向，不能外推到改变函数组或联合整格的最优τ。

## 4. 同一安全类型的基本CDT必要门槛

先自证真实函数秩。E在u=1/3有非零log，故不是有理函数。若J_g=qE+r，q,r为复系数有理函数，利用
\(E'=-E/(2u)+1/[2u(1-3u)]\)与R2比较独立的E及1项，必须有
\[
q'+\left(-\frac1{2u}+\frac2{1-4u}\right)q=-2.
\]
括号系数在∞为−1/u+O(u^(-2))。有理q若在∞次数d>1，左侧首项为(d−1)q_d u^(d−1)，不能是常数；次数≤0时左侧趋0，次数1时最高常数也相消，左侧仍趋0。矛盾。
所以(1,E,J_g)在C(u)上秩3；对有理g亦在Q(u)上秩3。换成uE并乘b_g不改变秩。
两个一阶有理系数非齐次ODE组成一个长度3齐次系统，故所有函数holonomic。这不证明共同解析图条件。

若此函数组在合法φ的全盘上meromorphic，CDT基本界要求
\[
3\le\frac{\mathcal E(\phi)}{\log|\phi'(0)|-\tau},\qquad
\mathcal E(\phi)=\iint\log|\phi(z)-\phi(w)|.
\]
Jensen给\(\mathcal E(\phi)\ge\log|\phi'(0)|\)。
要让该upper严格小于3、与实际rank冲突，使用R4必须至少有
\[
\log|\phi'(0)|>\frac32\tau=\frac72.
\tag{R9}
\]
仅有log|φ'|>τ不足以证明无理性。分母为负时根本不能使用这张界。

若另限定φ遗漏1/3和∞且φ^(-1)(0)={0}，modularλ覆盖模板给|φ'(0)|≤16/3；即使理想能量等于log导数，也达不到R9。这只判这一个unique-origin模板和R4证书不能成功。

A本轮在核含foreign even-origin前像的合法图；那些前像上的E可以有普通pole，仍符合meromorphic条件。不能把unique-origin的upper移植到全部合法图，也不能把R8当所有联合源的费用cap。
另一方面，明确构造univalent p域、φ=(1/3)tanh²√p时，最近的φpole为p=−π²/4，Koebe给该具体域的|p'(0)|≤π²，故|φ'(0)|≤π²/3。此具体图也不够；多值p图的全局能量与最优联合费用未由此关闭。

## 5. 本轮作用

R1–R8是实质新算术证据：完整源更短，且标量LCD主率精确。它改变下一步：停止同一标量LCD压缩，也不以一个填点或positive denominator误认基本CDT准入。
没有新的数值无理性定理；全局解析图、实际rank与文献覆盖由本轮独立任务核对。数学程序0、参数扫描0、旧档不改。
