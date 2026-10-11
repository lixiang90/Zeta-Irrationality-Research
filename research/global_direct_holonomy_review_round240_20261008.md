# 第240轮：直接 holonomy 复盘与两个真实周期准入对象

2026-10-08，NEW。数学程序、Lean执行、素数/参数扫描均为0。本稿实际FULL读取237–239三份最终主稿；当前CDT作者220页PDF只实际读取下述完整选页，不称全文审阅。结论是暂停当前三维源的同源素数/图优化，保留其全阶资产；它不是最优整格或原数值目标的no-go。新优先候选是完整 logistic 泛函的 **X=3ζ(3)+ζ(5)**；另保留低权混合周期 **K=2G−(π/2)log2** 的有界直接CDT接口。

## 1. 237–239到底支付了什么

固定真实填点值g₀=2I(1/4)，在g₀∈Q假设下，源为(1,uE,b_gJ_g₀)。本轮FULL输入身份：

|主稿|bytes|SHA256|
|---|---:|---|
|joint_lattice_metric_bridge_round237_20261008.md|9821|cf2550e55910f6feceff0652aa38b5a102749aed7479c67540a4a80bc7e190a8|
|actual_flag_determinant_round238_20261008.md|8061|799156d8cc6e030e77622cfe5eeeb7fa0ad5a4a61b80e8fb95e8851101f14954|
|actual_cofactor_arithmetic_round239_20261008.md|9483|25ec2e97a75e477e305d37aa1c59044155c41499e2a00240cddfb31561151262|

237给出同一BC度量、同一普通整数Taylor目标的degree-D联合格桥，以及精确 graded finite credit 与source index的抵消。因此内在费用是
\[
 A_D=-\log|\det T_{\mathrm{actual\ jumps}}|,                 \tag{R1}
\]
不是任意CRT整数化格的raw index。238给出真实填点源的全阶one-hole单射，N=3D+3，以及最大**非零关系下标**h*所选cofactor；不能改用最大绝对值minor或平方和。239给出完整全素数/幂CRT的Q_m及所有h的2、3内容C_m，从而
\[
 \limsup A_D/D^2\le a_{\rm paid}:=21/2-\log12.              \tag{R2}
\]
它是实际selected determinant的有效费用upper，不是最优费用lower。另已付lower仅为3log(4/3)，两者未吻合。

同一源的紧全图upper由已冻结239稿所用234解析结论给出
\[
 C_E=\frac{2\pi}{3}K(1/9)K(8/9)
 \le C_{\rm tight}:=\frac{\pi^3}{2^{7/4}}.
\]
这里K(x)=∫₀^{π/2}(1−x sin²θ)^−1/2dθ，是参数记法。Cauchy–Schwarz给K(x)²≤π²/(4√(1−x))，故此tight upper可自核。
在237的单图BC判据及J≥λ校准下，必要窗口为a<3log C_tight；现有upper R2高于这个门槛。由此只得到“**现有证书尚不能给strict余量，继续同源微调的投资依据不足**”。没有证明实际a≥门槛、没有求最优全部prime层、没有关闭新metric/源或别的合法整格。

## 2. 当前primary提供的转向依据及去重

实际选读当前作者PDF物理29–34、175–180、190–199页。其§2.11真实混合周期例子用相同平方根齐次解的局部反号来消去分支；§14以Hadamard乘积把完整数值关系变成有理系数、真正overconvergent的G函数。§15.1.10还明确提醒：由逼近序列生成函数不自动成为G函数；§15.2的localized integral-module finiteness是问题而非可直接套用的已证通用结论。[当前CDT作者PDF](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)

已发表的近参数两log乘积Theorem C，以及§2.11的1、π/√3、3L(2,χ₋₃)−(π/√3)log3的Q-LI，均不得包装成新目标。当前作者PDF220页与arXiv v2登记的218页是两个阅读身份；本稿选页来自已固定220页作者件。新检索未找到下面两个**精确混合值**的既有结论，只能记作限定检索结果，不证明全球首次性。个别ζ值或G分别无理，逻辑上不推出这些混合值无理；Baker的log线性形式定理也不涵盖它们。

## 3. 优先候选X：完整泛函确实只含一个指定数值方向

采用Root新固定的作者源码，commit
669c92bf7a3728e0de9ad80c373bc29fb5ca3d58。本稿实际FULL读Family.lean、Analytic/Logistic.lean、Analytic/Contour/Moments.lean及README；没有运行Lean，没有审核完整依赖或认领作者的数值定理。下述是在其真实logistic矩公式上的纸面扩展。

令t=1/2+iy，ρ(y)=(π/2)sech²(πy)，B(G)=∫G(t)ρ(y)dy。已读Moments的完整恒等式是
\[
 B((t+j)^{-k})=k\{\zeta(k+1)-H_j^{(k+1)}\},\quad k\ge1,j\ge0,
 \qquad B(t^e)=B'_e\in Q,                                \tag{R3}
\]
其中B'₁=+1/2；逆幂的telescope及j→∞余项衰减条件均在该实际文件中给出。不是仅据ζ2、ζ3两式猜一般k。

对任意有限有理c₂及奇k≥3的c_k，设
\[
 X=c_2\zeta(2)+\sum_{k\ {\rm odd}}c_k\zeta(k),\quad
 {\cal L}=-c_2+\sum_{k\ {\rm odd}}\frac{c_k}{(k-1)!}\partial_t^{\,k-2},
 \quad U_X(G)=B({\cal L}G).
\]
当G_j=t/(t+j)时，q=k−2为奇数且
G_j^(q)=j q!/(t+j)^(q+1)。所以完整恒等式为
\[
 U_X(G_j)=jX-j\left(c_2H_j^{(2)}
          +\sum_{k\ {\rm odd}}c_kH_j^{(k)}\right)-c_2.     \tag{R4}
\]
尤其不能漏掉−jc₂H_j^(2)。多项式G的U_X(G)为明确有理Bernoulli导数组合。

设R_n(t)=D_n(t)^4/D_(5n)(t)，D_n=∏₁ⁿ(t+j)，写**完整**部分分式
\[
 t^eR_n=P_{n,e}(t)+\sum_{j=1}^{5n}\lambda_{n,e,j}/(t+j).
\]
则
\[
 U_X(t^{e+1}R_n)=X\,b_{n,e}+a_{X,n,e},\quad
 b_{n,e}=\sum_j j\lambda_{n,e,j},                         \tag{R5}
\]
且a包含全部polynomialPart和全部有限调和头，是有理数。令M=3n、e=i+k，矩阵(Xb_(i+k)+a_(i+k))的**所有entries**在X∈Q时有理化；没有遗留单独ζ3或ζ5通道。这给X=3ζ3+ζ5的真实whole-functional selector，不是只评价一个entry。

分部积分的精确核为
\[
 W_X=-c_2\rho+\sum_{k\ {\rm odd}}
       \frac{c_k\,i^{k-2}}{(k-1)!}\rho^{(k-2)}.            \tag{R6}
\]
因为d_yG=i∂_tG，每次IBP的系数是i而非−i。所有ρ^(q)是ρ乘tanh(πy)的固定多项式，故|W_X|≤C_Xρ；任意固定阶导数与这里的有理G沿直线至多多项式增长，边界均指数趋零。因此同一Heine绝对上界只多C_X^M=exp(O_X(n))，不会免费产生新的负N²能量，也不证明值非零。

## 4. X的全系数整化与“非rank-one”的all-scale起步

这里给可直接证伪/细化的完整安全起点。S_n=(5n)!/(n!)⁴是整数，P_(n,e)∈Z[t]由monic division给出，而
\[
 S_n\lambda_{n,e,j}
 =(-j)^e(-1)^{j-1}j\binom{5n}{j}\binom{j-1}{n}^{4}\in Z. \tag{R7}
\]
j≤n时binomial为0，覆盖全部有限头。取X=3ζ3+ζ5，则
L=(3/2)∂+(1/24)∂³。对0≤e≤6n−2，tP_(n,e)的degree≤5n−1。von Staudt–Clausen使相关B'_l的分母整除d_(5n)，包括B'₁；全部H_j^(3)、H_j^(5)由d_(5n)^5清除。因此
\[
 q_n=24S_nd_{5n}^{\,5}                                   \tag{R8}
\]
同时清除所有a、b以及完整多项式det(XB+A)经q_n^(3n)后的每一系数。这包含2、3、5及全部prime powers，固定有理目标分母另乘一个固定常数即可。它**不是**primitive Gauss内容费用，也没有把其粗值当净N²判据。[DLMF24.10(i)](https://dlmf.nist.gov/24.10#i)

有一个无需有限probe的结构区别。n≥2时，e≤n−3给t^eR_n=O(t^−3)，e=n−2给t^eR_n=t^−2+O(t^−3)。比较完整部分分式的t^−2系数：
\[
 b_{n,e}=0\ (e<n-2),\qquad b_{n,n-2}=-1.
\]
故B的前(n−1)×(n−1) Hankel子块为anti-triangular，反对角线−1，
\[
 \det(b_{n,i+j})_{0\le i,j<n-1}
       =(-1)^{(n-1)+(n-1)(n-2)/2}\ne0.                  \tag{R9}
\]
所以rank B≥n−1。对n≥3，这个实际period coefficient matrix不能满足228的rank-one common-period Gram假设；该旧cap不适用。R9不证明完整3n秩、target determinant∞非零或primitive整化。

**首个准入lemma必须仍是同一个完整det多项式：** 在固定X=3ζ3+ζ5下证明其primitive全部系数Gauss成本与实际prime-edge∞非零，并同当前绝对Heine率组成strict比较。若只能给R8的粗上界，或只能给R9的局部秩而无完整内容/非零证书，就停止迁移，不继承Tang原r参数的有限常数、Frobenius边界或正性。不能把det序列自动视为LCM-controlled CDT G函数。

## 5. 次选K：低权真填点及完整LCM证明

G=L(2,χ₋₄)，K=2G−(π/2)log2。定义
\[
 F(x)=(1-4x)^{-1/2}\in Z[[x]],\quad \ell(x)=\log(1-2x),
\]
\[
 H(x)=F(x)\int_0^x\frac{2\ell(t)}{(1-2t)\sqrt{1-4t}}dt.
                                                                    \tag{R10}
\]
这是当前§2.11平方根混合周期机制的具体a=2、坐标x↦2x变体。取y=√(1−4t)，再取y=tanθ，严格求端点积分：
\[
 \int_0^{1/4}\frac{2\log(1-2t)}{(1-2t)\sqrt{1-4t}}dt
 =2\int_0^1\frac{\log((1+y^2)/2)}{1+y^2}dy
 =\frac\pi2\log2-2G=-K.                                \tag{R11}
\]
最后一步用G=−∫₀^{π/4}log(tanθ)dθ及
∫₀^{π/4}log cosθ dθ=−(π/4)log2+G/2；可由Abel Fourier后L¹极限纸证。
所以若K=g∈Q，H_g=H+gF的native sqrt coefficient在x=1/4恰为0。其剩余局部部分确实holomorphic：以y为参数，积分从y=0起是odd analytic函数，除y为even analytic函数。这是消**非亚纯分支**，不是只填CDT本来容许的pole。

完整算术也可付。F整数，且
\[
 \frac{2\ell(x)}{1-2x}=-\sum_{j\ge1}2^{j+1}H_jx^j .
\]
被积函数的第j系数由d_j清除；一次积分后第q系数由q d_(q−1)清除，再乘F整数保持全prefix结论。对每个prime p，
\[
 \max_{1\le q\le N}\{v_p(q)+v_p(d_{q-1})\}
 \le v_p(d_N)+v_p(d_{\lfloor N/2\rfloor}).               \tag{R12}
\]
证明：p>N时没有任何p分母，两边均0。其余记p^a≤N<p^(a+1)，a≥1。若N≥2p^a，两边upper为2a；若N<2p^a，则q=p^a给a+(a−1)，其它q≥p^a只能v_p(q)≤a−1；q<p^a更小。p=2同样有效，d₀=1。故固定b_g g∈Z时
\[
 b_gd_Nd_{\lfloor N/2\rfloor}[x^n]H_g\in Z
       \quad(0\le n\le N).                              \tag{R13}
\]
没有额外2^N费用：坐标已取HA=F的完整整数模型。此为合法safe类型，不声称prefix最优或最优联合格。

H_g在x=1/2的log²首项为(1/2)log²(1−2x)，与g无关，故1、H_g在Q(x)上独立；原始native fill确有关系敏感性。raw两行类型(0;1,1/2)给τ=9/8。可用三行(1,ℓ,H_g)，费用τ=(3·1+5·3/2)/9=7/6；ℓ在1/2的一级log与H_g的二级log确保函数独立。其微分闭包还含F，不能把“raw三行”误称deRham rank3。

## 6. K最早不能跳过的门槛

不能将F免费添为背景：它保留x=1/4的平方根分支，立即失去假设产生的补点。也不能把native填点推广到所有transported叶；log(1−2x)的回路会改变积分常数。
下一lemma必须给(1,ℓ,H_g)的**同一真实共同map**及全部δ-preimages的叶条件，并满足
\[
 3\{\log|\phi'(0)|-7/6\}>J(\phi).                       \tag{R14}
\]
因J≥log|φ′₀|，必要为|φ′₀|>exp(7/4)。当前§2.11 explicit bivalent map缩放1/2只有导数4；其quadrivalent缩放导数4√2亦小于exp(7/4)。所以二者不能认证R14，不能仅靠较低τ就宣称成功。更大map若多出δ-preimages，须重新支付真实叶补点；若此首lemma失败，K只保留为明确period selector资产。

## 7. 本轮选择与范围

优先有界验证R5–R9的X完整primitive算术/prime-edge节点；K仅是一个低权可证伪备用接口。两者均不由LW/Baker或单个周期无理性推出；本稿不宣布任何新数值无理性/LI，不声称全面文献首次性，不认领README、有限秩或源码阅读等同kernel验证。旧三维源已付资产保留；240不继续其prime、map参数优化。

实际阅读域、来源URL、所有新选页和FULL输入身份见
[packet_reading_scope](../literature/global_review_sources_round240_20261008/packet_reading_scope.md)。
