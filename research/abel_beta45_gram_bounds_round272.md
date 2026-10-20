# 第272轮：固定 Abel Gram 的实际上界与指定安全族下界

2026-10-20，`intrinsic_budget_271`。只研究[272任务](abel_beta45_budget_charter_round272_20261020.md)固定的[271.2–271.7](global_budget_review_round271.md)对象；没有改变目标、n/m、Hermite数据或实际来源。G1–G5给全体 m≥1 的实际实处 **upper**；G6–G7独核根提出的整数来源/Legendre方法，给指定安全清整族的严格正二次率 **lower**。后者只结束该安全族，未证明实际首一Q_m(Y)的全序列非负二次率，也未排除最优primitive倍率产生的严格负预算。

实际读恢复状态、272任务、271全文及[独立来源B1–B7](abel_beta45_jet_projection_independent_round271.md)。本代理端goal工具为null，根端确认的active授权及权威研究账适用；没有改账。数学程序、CAS、m/prime/参数扫描、Lean均0。以下常数由纸面初等不等式给出。

## G1. 对象和结论

始终固定 n=2m−1、c=−m、Y=4β(5)−3β(4)，原唯一 Hermite p_i∈Q[w]_<3m，及实际正矩阵

\[
(M_m)_{ij}=\int_{\mathbf R}p_i(-y^2)p_j(-y^2)\omega_m(y)\,dy,
\]
\[
\omega_m(y)=\frac{\pi^2}{2}y^3U_m(y)^3
\operatorname{csch}(\pi y)(1+2\operatorname{csch}^2(\pi y)),
\qquad
U_m(y)=\frac{\prod_{r=1}^{m-1}(y^2+r^2)}
{\prod_{r=0}^{m-1}(y^2+(r+1/2)^2)}.
\tag{G1}
\]

零处按连续延拓。令 B_m 为271的实际目标系数矩阵，Q_m(Z)=det(A_m+ZB_m)/det B_m。本稿证明

\[
\boxed{\log\det M_m\le(2+12\log6)m^2
+12m\log m+39m\log2}
\quad(m\ge1),
\tag{G2}
\]
\[
\boxed{\log|Q_m(Y)|\le(2+12\log6)m^2
+18m\log m+(39\log2-\log3)m}
\quad(m\ge1).
\tag{G3}
\]

因此实际归一值具有显式 exp(O(m²)) 安全上界。这里常数为正，不能据此判断实际主率的符号。

## G2. 实际来源数据的初等界

沿用原右极点参数 x_k=m−k−1/2≥1/2，g_k=a_{2,k}/a_{3,k}、h_k=a_{1,k}/a_{3,k}，以及

\[
\alpha_k=\frac{3-g_k}{4x_k},\qquad
\gamma_k=-\alpha_k^2-
\frac{h_k+4x_kg_k\alpha_k+2\alpha_k}{4x_k^2}.
\]

B7的确切表达为

\[
g_k=6\sum_{j=1}^{n}(2j-2k-1)^{-1}
-3\sum_{\substack{0\le r\le n\\r\ne k}}(r-k)^{-1},
\]
\[
g'_k=-12\sum_{j=1}^{n}(2j-2k-1)^{-2}
+3\sum_{r\ne k}(r-k)^{-2},\qquad
h_k=(g_k^2+g'_k)/2.
\]

每个和有n项，所有分母为非零整数，所以

\[
|g_k|\le9n\le18m,\quad |g'_k|\le15n\le30m,
\quad |h_k|\le177m^2.
\]

由x_k≥1/2，逐项估计得

\[
|\alpha_k|\le11m,\qquad
|\gamma_k|\le121m^2+177m^2+396m^2+22m\le800m^2.
\tag{G4}
\]

这些只是实际数据的绝对值界，没有把它们当作整数性或分母界。

## G3. 原 Hermite 多项式在负半轴的全尺度界

令

\[
\ell_i(w)=\prod_{j\ne i}\frac{w-w_j}{w_i-w_j},\qquad
s=w-w_i,\qquad h_i^*=\ell_i'(w_i).
\]

唯一Hermite解可明确写成

\[
p_i(w)=\ell_i(w)^3(1+c_{1,i}s+c_{2,i}s^2),
\]
\[
c_{1,i}=\alpha_i-3h_i^*,\qquad
c_{2,i}=\gamma_i/2-3h_i^*\alpha_i+6(h_i^*)^2
-\tfrac32\ell_i''(w_i).
\tag{G5}
\]

因为其余节点均有三重零，而在w_i处逐阶核对恰给原 value、first derivative、second derivative。它没有改选另一来源行。

节点集合为{(j+1/2)²:0≤j<m}。任意节点差为非零整数；故

\[
|h_i^*|\le m,\qquad
|\ell_i''(w_i)|\le m^2+m\le2m^2.
\]

结合(G4)，有 |c_{1,i}|≤14m、|c_{2,i}|≤442m²≤450m²。

下面只为计算节点差乘积，把同一节点暂标为ν_j=(j+1/2)²。直接相乘给

\[
\left|\prod_{r\ne j}(\nu_j-\nu_r)\right|
=\frac{(m-1-j)!(m+j)!}{2j+1}
\ge\frac{(m-1)!m!}{2m}
\ge\tfrac12e^{-2m}m^{2m-2}.
\tag{G6}
\]

第一个下界用固定总和2m−1时 factorial product 在(m−1,m)处最小；第二个用m!≥(m/e)^m和(m−1)!=m!/m。m=1也成立。

对w=−y²，所有节点均小于m²，故(G6)推出

\[
|\ell_i(-y^2)|\le2e^{2m}(1+(y/m)^2)^{m-1}.
\]

同时 |s|≤m²(1+(y/m)²)，所以

\[
|1+c_{1,i}s+c_{2,i}s^2|
\le465m^6(1+(y/m)^2)^2.
\]

最终得到同一实际 p_i 的统一界

\[
\boxed{|p_i(-y^2)|\le2^{12}m^6e^{6m}
(1+(y/m)^2)^{3m-1}}
\quad(0\le i<m,\ y\in\mathbf R).
\tag{G7}
\]

## G4. 实际密度和积分的完整上界

原乘积逐因子给 U_m(y)≤(y²+1/4)^−1。对0<y≤1，用sinh(πy)≥πy，有

\[
\omega_m(y)\le32\pi y^2+64/\pi<150.
\]

对y≥1，使用 y³U_m(y)³≤1、csch(πy)≤3e^−πy及csch(πy)≤1/(πy)，得

\[
\omega_m(y)\le3\pi^2e^{-\pi y}<48e^{-\pi y}.
\]

由3<π<4、e<3，可在整个实轴统一为

\[
0<\omega_m(y)\le2^{14}e^{-\pi|y|}.
\tag{G8}
\]

小区间所需常数满足150e^π<150e⁴<150·81<2¹⁴。零处延拓亦遵守该界。

由(G7)及1+t²≤(1+t)²，

\[
(M_m)_{ii}\le2^{39}m^{12}e^{12m}
\int_0^\infty e^{-\pi y}(1+y/m)^{12m}\,dy.
\]

利用π>3，保留一份e^−y可积因子，且

\[
\sup_{t\ge0}\{12\log(1+t)-2t\}=12\log6-10,
\]

得到

\[
\int_0^\infty e^{-\pi y}(1+y/m)^{12m}\,dy
\le e^{(12\log6-10)m}.
\tag{G9}
\]

原实际M_m正定，Hadamard因而给(G2)。这是同一矩阵整个实轴积分的upper，未截尾、未改测度、未删任何多项式头；头部已通过271的确切积分桥包含在该矩阵内。

## G5. det B 归一及未完成的预算

原精确a3公式及中央二项式界给 a_{3,k}≥(2m)^−6。因此

\[
|\det B_m|=192^m\prod_{k=0}^{m-1}a_{3,k}
\ge[192(2m)^{-6}]^m.
\tag{G10}
\]

将其与(G2)、|Q_m(Y)|=detM_m/|detB_m|合并，准确得到(G3)。没有漏掉detB，也没有把不定B当作单位阵。

本稿没有证明全m的 liminf m^−2 log|Q_m(Y)|≥0，也没有给实际最优λ_m的完整费用率。仅有(G3)的正上界不排除实际衰减或一个严格负的无界子列；不论清行还是直接清Q，有限处与primitive内容均须同对象支付，不能双领。

尝试过的裸评价lower接口是最高m个w系数的外积；其全尺度非零及足够lower尚未证明，故不登记为成果或后续新窗口准入。下面改用已经清行的整数多项式：其lower含有T的费用，不能偷换成不含T的裸评价lower。

## G6. 已清行整数多项式的实际 Gram 下界

本节设T为任意正整数，满足 **原同一** Tp_i∈Z[w]；并不假定T最小。根的完整来源证书提供一个具体T，本文不把其整性证明登记为本代理的独立贡献。以下下界对任何这样的T均成立，不需要其大小的估计。

先在|y|≤1付实际密度lower。零处

\[
U_m(0)=\frac{((m-1)!)^2}{((1/2)_m)^2}\ge\frac4{2m-1}.
\]

证明：m=1等号；逐阶比值为m²/(m+1/2)²，且此比值至少为(2m−1)/(2m+1)。又

\[
\frac{U_m(y)}{U_m(0)}
=\frac{\prod_{r=1}^{m-1}(1+y^2/r^2)}
{\prod_{r=0}^{m-1}(1+y^2/(r+1/2)^2)}\ge e^{-6}.
\]

最后一步只用log(1+u)≤u及
Σ_{r≥0}(r+1/2)^−2≤6：r=0贡献4，其余项用区间[r−1/2,r+1/2]上t^−2的积分控制，总计≤2。因此

\[
U_m(y)\ge2e^{-6}/m\qquad(|y|\le1).
\]

sinh的凸性给sinh(πy)≤y sinhπ（0≤y≤1），故

\[
y^3\operatorname{csch}(\pi y)(1+2\operatorname{csch}^2(\pi y))
\ge\frac2{(\sinh\pi)^3}.
\]

与(G1)相乘，得到精确正数

\[
c_*:=\frac{8\pi^2e^{-18}}{(\sinh\pi)^3}>0,\qquad
\omega_m(y)\ge c_*m^{-3}\quad(|y|\le1).
\tag{G11}
\]

令P_i(z)=Tp_i(−z)∈Z[z]，H_m=(∫_0^1P_i(z)P_j(z)dz)。所有P_i仍独立、degree≤3m−1，因此H_m严格正定。对任意实系数向量先作二次型比较，再用z=y²和z^−1/2≥1，得

\[
M_m\succeq c_*m^{-3}T^{-2}H_m,
\qquad
T^{2m}\det M_m\ge(c_*m^{-3})^m\det H_m.
\tag{G12}
\]

这里比较的是两个真正的正Gram，不是把不定B_m或抽象minor当作正矩阵。

为下界detH_m，写P_i(z)=Σ_{d=0}^{3m-1}C_{i,d}z^d，C为满行秩整数矩阵。选按递增下标排列、**字典序最高**的非零m×m系数minor I=(d_1<⋯<d_m)；其det为非零整数，绝对值至少1。

令q_d为[0,1]的首一shifted Legendre多项式。自含规范可取

\[
L_d(z)=\frac1{d!}\frac{d^d}{dz^d}[z^d(z-1)^d],\qquad
q_d=L_d/\binom{2d}{d}.
\]

分部积分d次给对低次多项式的正交性，且

\[
h_d:=\int_0^1q_d(z)^2dz
=\frac1{(2d+1)\binom{2d}{d}^2}
\ge\frac1{(2d+1)16^d}.
\tag{G13}
\]

精确norm来自∫L_d²=binom(2d,d)∫z^d(1−z)^d=1/(2d+1)。换到q_d系数得到C̃=C U，其中U_{d,j}=0（j>d）、U_{d,d}=1。对minor I作Cauchy–Binet，只有J_r≥I_r逐项成立的J可贡献；若J≠I则字典序更高，其原系数minor为0。因此det C̃_I=det C_I，仍有绝对值≥1。不能对任意预指定高次minor作这个断言。

对正Gram再次作有限Cauchy–Binet，有

\[
\det H_m=\sum_{|J|=m}(\det\widetilde C_J)^2\prod_{d\in J}h_d
\ge\prod_{d\in I}h_d.
\]

这些d在0,…,3m−1中互异，所以Σd≤(5m²−m)/2、2d+1<6m。由(G12)–(G13)，

\[
\boxed{\ T^{2m}\det M_m\ge
\left(\frac{c_*}{6m^4}\right)^m
16^{-(5m^2-m)/2}\ }
\quad(m\ge1).
\tag{G14}
\]

这是含清行倍数T的实际全尺度下界；它不依赖任何固定高系数block的未证非零。

## G7. 根所指定完整安全族的增长范围

记d_N=lcm(1,…,N)。根最终固定的安全倍数为

\[
L_m=d_{4m},\qquad S_m=T^2L_m^{\,5}.
\tag{G15}
\]

其完整清整证明由根的有限处/全部头证书负责；本次精简使用实际u长除法及Euler头整性，不再另乘先前的2^(D+1)。这里独立核对的是该**同一最终指定**倍数的实际增长。将(G15)乘入(G14)，得到

\[
\boxed{\ S_m^m\det M_m\ge
\left(\frac{c_*}{6m^4}\right)^m
L_m^{\,5m}\,2^{-10m^2+2m}\ }.
\tag{G16}
\]

不必借素数渐近即可证明该下界的二次率严格为正。对每个0≤k≤N，Legendre公式的每一层

\[
\left\lfloor\frac N{p^e}\right\rfloor-
\left\lfloor\frac k{p^e}\right\rfloor-
\left\lfloor\frac{N-k}{p^e}\right\rfloor\in\{0,1\}
\]

只有p^e≤N时可能非零，故binom(N,k)整除d_N。由二项式和，某个binom(N,k)≥2^N/(N+1)，所以

\[
d_N\ge\frac{2^N}{N+1}.
\]

取N=4m并投入(G16)，可得更明确的全m有限下界

\[
S_m^m\det M_m\ge
\left(\frac{c_*}{6m^4}\right)^m
(4m+1)^{-5m}\,2^{10m^2+2m}.
\]

因此完全初等地已有

\[
\boxed{\ \liminf_{m\to\infty}m^{-2}
\log(S_m^m\det M_m)\ge\kappa_0:=10\log2>0.\ }
\tag{G17}
\]

若另采用标准logd_N=N+o(N)，由(G16)得到较强lower κ=20−10log2>0。该加强不参与(G17)的初等严格正性；两个常数均已删除先前额外Euler费用的信用。

一旦完整证书确认S_mA_m、S_mB_m均整，F_m(Z)=det(S_mA_m+ZS_mB_m)就是整数多项式，|F_m(Y)|=S_m^m detM_m。若c_m=content(F_m)，则

\[
\lambda_m=\frac{S_m^m|\det B_m|}{c_m},\qquad
|\lambda_mQ_m(Y)|=\frac{S_m^m\det M_m}{c_m}.
\tag{G18}
\]

所以(G17)结束的是**未除去实际内容的最终指定安全族**，包括该族的任何无界子列。它不排除最优primitive内容。量词明确如下：若事先指定的无界子列ℳ和某δ>0满足

\[
\limsup_{\substack{m\to\infty\\m\in\mathcal M}}
m^{-2}\log|\lambda_mQ_m(Y)|\le-\delta,
\]

则由(G17)及(G18)必有

\[
\liminf_{\substack{m\to\infty\\m\in\mathcal M}}
m^{-2}\log c_m\ge\kappa_0+\delta>\kappa_0.
\]

使用上述素数渐近时可将κ0替成κ=20−10log2。若只声明严格负limsup，可先取小于其绝对值的固定δ。该必要内容门槛只在同一预定子列上主张，不扩大到子列外；本稿未付这项信用，也没有证明该信用不可能。

G16不是裸Q_m(Y)的增长下界，更不是Y不可能无理。指定一轮来源窗口的结束决定由根按272任务结算；本稿不凭缺口或新的局部lower申请续期。
