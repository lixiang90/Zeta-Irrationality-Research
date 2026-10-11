# 第257轮：同一native χ−8 prototype的完整宏观内容改进

2026-10-10。实际FULL读并核冻结256的C整数稿、Root sensitivity稿、A共同contour稿及报告，四项bytes/hash均匹配256 manifest。沿用a=1/√2、3+T、N(i,j)=a^i\bar M(i,j)、同一n行P_r,D_r、全raw j<2n和selected-even列；没有替换参数、sheet、vector或对象。详细读域见 integer_reading_scope.md。

**本轮得到一个真正的全尺度内容定理，改变同一个实际det的有限处安全预算。** 令d_m=lcm(1,…,m)，旧q_H=2^{2H+1}d_{H+1}³。新的完整prefix因子是

\[
 \boxed{\widetilde q_H=2^{3\lfloor H/2\rfloor+1}d_{H+1}^{2}}.
 \tag{P1}
\]

它清整所有0≤i,j≤H的完整R_{ij}、Y/ζ(2)系数及ordinary Z heads，含2与全部odd prime powers。对H=2n−1、κ_n=2^{n(n+1)/2}，256的既有完整整数多项式

\[
 C_n^{old}(T)=\frac{q_{2n-1}^n}{\kappa_n}\Delta_n(T)
\]

的**所有coefficients**都被

\[
 \boxed{M_n=[2^{n+1}d_{2n}]^n}
 \tag{P2}
\]

整除。证明不只检查leading coefficient、局部prime或有限n；κ只扣一次。有理row/column缩放不用于制造saving。按标准ψ(2n)=2n+o(n)换算，primitive leading coefficient的完整安全费从6+(9/2)log2降至4+(7/2)log2，每n²省2+log2。

这是真正的费用改进，**还没有actual关系点无界非零、同对象strict净能量或新的数值无理性定理**。是否足以延续固定prototype，由本轮同尺度actual energy结算决定，不因费数字变小自动续窗。

## 1. 完整对象与三种边界头

保留256的全部分解及有限头：

\[
 N(i,j)=R_{ij}+16Y a^{i-j}c_{(i-j)/2}
 +9\zeta(2)a^{i-j+1}c_{(j-i-1)/2},
 \tag{P3}
\]

c_l=4^{-l}binom(2l,l)，非法下标取0，Y=L(2,χ−8)。令

\[
 b_l=\binom{2l}{l}/8^l=a^{2l}c_l,
 \qquad t_l=\binom{2l}{l}/2^l,
\]
\[
 A_d^-=R_{d0},\qquad A_d^+=R_{0d}.
 \tag{P4}
\]

完整forcing是μ_i=a^im_i、U_i=−4Σ_{k<i}μ_k，μ_{2l}=2^{l+1}(l!)²/(2l+1)!、μ_odd=0。边界递推与starts精确为

\[
 A_0^-=0,\quad A_1^-=8,\qquad
 A_d^-=\frac{d-1}{2d}A_{d-2}^-+
 \frac{U_{d-2}/2-U_d}{d},
 \tag{P5}
\]
\[
 A_0^+=A_1^+=0,\qquad
 A_d^+=\frac{2(d-2)}{d-1}A_{d-2}^+
 +\frac{16}{(d-1)^2}\quad(d\ge2).
 \tag{P6}
\]

本稿改进的是这些全头的估值。实际两sheet载体已在256匹配，下面的generating series推导只改写同一个完整对象，不自由更换period start。

## 2. minus完整头的binomial双重和

设

\[
 C(z)=\sum_{d\ge0}N(d,0)z^d,\quad
 A(z)=(1-z^2/2)^{-1/2}=\sum_{l\ge0}b_lz^{2l},
\]
\[
 \mathcal M(z)=\sum_{i\ge0}\mu_i z^i
 =\frac{2\arcsin(az)}{az}A(z),\quad
 U(z)=\sum_{i\ge0}U_i z^i=-\frac{4z}{1-z}\mathcal M(z).
 \tag{P7}
\]

M式来自256实际Stieltjes函数在az的芽，也可由moment系数逐项验证。用(P5)所对应的完整N递推求和，d=1的8z与U_1z=−8z恰抵消，得

\[
 z(1-z^2/2)C'(z)=(z^2/2)C(z)+(z^2/2-1)U(z).
\]

因此

\[
 \boxed{(C/A)'=\frac8a\frac{\arcsin(az)}{z(1-z)}}.
 \tag{P8}
\]

常数(C/A)(0)=16Y。利用

\[
 \frac{\arcsin(az)}a
 =\int_0^z A(v)dv
 =\sum_{h\ge0}\frac{b_h}{2h+1}z^{2h+1},
\]

完整minus rational head对d≥1恰为

\[
 \boxed{A_d^-=8\sum_{l=0}^{\lfloor(d-1)/2\rfloor}
 \frac{b_l}{d-2l}
 \sum_{h=0}^{\lfloor(d-2l-1)/2\rfloor}\frac{b_h}{2h+1}.}
 \tag{P9}
\]

每个term除binomial的2幂外，仅有d−2l及2h+1两个divisors，均≤d；central binomial分子是整数，而其dyadic denominator是8^{l+h}，且l+h≤floor((d−1)/2)。两个divisors中包含的2也由d_d²支付。因此

\[
 \boxed{2^{3\lfloor(d-1)/2\rfloor}d_d^2 A_d^-\in\mathbb Z.}
 \tag{P10}
\]

这不是Toeplitz inverse后领取一个免费rational row scale：它是原A_d^-的完整闭式与完整分母证书。所有U-forcing及d=1边界都参与(P8)，没有舍掉低degree项。A_0^-=0另行覆盖。

## 3. plus-even完整头及逐prime-power二层界

由b_l/b_{l-1}=(2l−1)/(4l)，(P6)的偶数递推直接化为

\[
 l b_l A_{2l}^+=(l-1)b_{l-1}A_{2l-2}^+
 +\frac{4b_{l-1}}{2l-1}.
\]

从A_0^+=0望远镜，ALL l≥1：

\[
 \boxed{A_{2l}^+=\frac4{l b_l}
 \sum_{h=0}^{l-1}\frac{b_h}{2h+1}
 =4\sum_{h=0}^{l-1}
 \frac{8^{l-h}\binom{2h}{h}}
 {l(2h+1)\binom{2l}{l}}.}
 \tag{P11}
\]

给任意prime p及b=p^e，置

\[
 \delta_j(b)=\left\lfloor\frac{2j}b\right\rfloor
 -2\left\lfloor\frac jb\right\rfloor\in\{0,1\}.
 \tag{P12}
\]

若b整除j，则δ_j(b)=0。对(P11)每个term去掉整数4·8^{l−h}，其估值按Legendre逐层为

\[
 \delta_h(b)-\delta_l(b)-[b\mid l]-[b\mid2h+1].
 \tag{P13}
\]

若b|l，则δ_l=0，该层至少−2；若b∤l，则最多由δ_l及[b|2h+1]各扣1，也至少−2。b>2l时该层为0。**包括p=2**，每层都支付，故

\[
 v_p(A_{2l}^+)\ge-2\lfloor\log_p(2l)\rfloor,
 \qquad \boxed{d_{2l}^{2}A_{2l}^+\in\mathbb Z.}
 \tag{P14}
\]

证明先对每个有限sum term给同一个完整LCD再相加；不凭某个prime下的sum cancellation或leading residue。旧三层bound在这里过付，因为p^e|l时inverse-binomial的同层分母贡献δ_l必为0。

## 4. plus-odd完整头与2的全部尺度

t_l/t_{l-1}=(2l−1)/l，所以(P6)在odd sector是

\[
 A_{2l+1}^+=\frac{2l-1}{l}A_{2l-1}^++\frac4{l^2}.
\]

初始A_1^+=0，ALL l≥1完整解为

\[
 \boxed{A_{2l+1}^+=4t_l\sum_{h=1}^l\frac1{h^2t_h}
 =4\sum_{h=1}^l
 \frac{2^{h-l}\binom{2l}{l}}{h^2\binom{2h}{h}}.}
 \tag{P15}
\]

central-binomial/divisor部分的每个p^e层为

\[
 \delta_l(b)-\delta_h(b)-2[b\mid h].
 \tag{P16}
\]

b|h时δ_h=0，层至少−2；否则至少−1，特别也≥−2。b>2l时为0。额外dyadic factor2^{h−l}由2^l完全覆盖。因此所有prime powers（包括2）都有

\[
 \boxed{2^l d_{2l}^{2} A_{2l+1}^+\in\mathbb Z.}
 \tag{P17}
\]

这里未把t_l逆系数的2估值漏掉，也未把odd通道当作selected-even所需之外而删除：完整prefix同时保留该sector。A_0^+=A_1^+=0另覆盖。

## 5. 全数组finite heads、period coefficients及ordinary Z

256已给完整diagonal reductions。i≥j、d=i−j时

\[
 R_{ij}=A_d^- -4\sum_{k=1}^j\mu_{d+k-1}/k;
\]

i<j、d=j−i时

\[
 R_{ij}=A_d^+ -4\sum_{k=d+1}^j\mu_{k-d-1}/k.
 \tag{P18}
\]

0≤i,j≤H中，μ下标≤H−1且k≤H。对任意p^e，

\[
 \left\lfloor\frac{2l+1}{p^e}\right\rfloor
 -2\left\lfloor\frac l{p^e}\right\rfloor\in\{0,1\},
\]

故d_{H+1}清整这些全部μ；再乘d_H付divisor k，每个finite term由d_{H+1}²清整。这包括p=2，不以numerator的额外2信用弥补未知分母。与(P10)/(P14)/(P17)合并，\widetilde q_H清整全部R_{ij}。

Y、ζ(2)的非零系数仍精确为

\[
 B_{ij}=16\binom{2l}{l}/8^l\quad(i-j=2l\ge0),
\]
\[
 C_{ij}=9\binom{2l}{l}/2^l\quad(j-i=2l+1).
 \tag{P19}
\]

dyadic指数分别≤3floor(H/2)、≤floor((H−1)/2)，故(P1)覆盖。用π²代ζ(2)时N的系数C/6=3binom(2l,l)/2^{l+1}也已覆盖；F中的9Z伴随π²系数为3/2，亦由同(P1)覆盖。若单独将未乘9的ordinary Z也记在π²基，其δ/6另需固定因子3；这只增加O(n)费用，并不改变本稿ζ(2)基的完整证书或contact后F的费用。

ordinary Z的完整heads仍是

\[
 Z^0_{ii}=-H_i^{(2)},\qquad
 Z^0_{ij}=(H_i-H_j)/(i-j)\quad(i\ne j),
 \tag{P20}
\]

由d_H²清整，ζ(2)系数δ为整数。因此所有H≥0有

\[
 \boxed{\widetilde q_H R_{ij},\quad\widetilde q_H B_{ij},\quad
 \widetilde q_H C_{ij},\quad\widetilde q_H Z^0_{ij}\in\mathbb Z
 \quad(0\le i,j\le H).}
 \tag{P21}
\]

H=0由starts直接覆盖。p>H+1不出现未付分母。没有只检查period-coefficient或selected block：plus-odd、全部finite heads、Z以及π²/contact伴随均已支付。

\[
 \log\widetilde q_H=(3\lfloor H/2\rfloor+1)\log2+2\psi(H+1)=O(H).
 \tag{P22}
\]

O(H)仍可只用256初等ψ(m)≤4m log2，不需要PNT或任何数学计算。

## 6. 原prototype全部raw、filter与whole-polynomial内容

P_r=2^nx^{2r}，D_r=Σ_{h=0}^{n-r-1}2^{n-h}binom(2h,h)x^{2r+1+2h}，0≤r<n。其contact余项阶≥2n+1，整个0≤j<2n的F_{rj}=N(P_r,j)−9Z(D_r,j)仍在Q+QY。取H=2n−1，(P21)覆盖所有polynomial degrees及全部raw columns。

每行h_r=2^{r+1}已知content只使用一次：P_r/h_r、D_r/h_r均整数，Σ_r logh_r=logκ_n。任意整数column filter E的全输入仍是raw pool，列l1高度W_s=max(1,Σ_j|E_{js}|)仍照256支付。对其任意n阶formal determinant Δ_{n,E}(T)，完整(P21)给

\[
 \boxed{C_{n,E}^{new}(T)
 :=\frac{\widetilde q_{2n-1}^n}{\kappa_n}\Delta_{n,E}(T)\in\mathbb Z[T].}
 \tag{P23}
\]

旧、新q的exact ratio是

\[
 \frac{q_H}{\widetilde q_H}
 =2^{2H-3\lfloor H/2\rfloor}d_{H+1}\in\mathbb Z,
\]
\[
 \frac{q_{2n-1}}{\widetilde q_{2n-1}}=2^{n+1}d_{2n}.
 \tag{P24}
\]

因此对整个formal polynomial的全部coefficients有

\[
 \boxed{C_{n,E}^{old}(T)=M_n C_{n,E}^{new}(T),
 \qquad M_n=[2^{n+1}d_{2n}]^n.}
 \tag{P25}
\]

这是完整旧integer model的真实共同内容因子，ALL n、ALL coefficients、ALL integer filters同时成立；不称M_n是全部primitive content。该改善来自原heads的全局结构与所有prime powers的两层界，不是单纯rational rowscaling或稀疏prime省费。κ在旧、新同一处扣一次；native a^i显式row尺度的同乘积κ不再重复扣。

256完整row-height S_n=32(n+1)4^n及filter height保持不变，故

\[
 \|C_{n,E}^{new}\|_1\le
 \frac{\widetilde q^n}{\kappa_n}\,n!S_n^n\prod_s W_s,
 \quad \widetilde q=\widetilde q_{2n-1}.
 \tag{P26}
\]

这里只改内容/清整fee，未领取actual two-sheet energy或evaluation determinant的小量。

## 7. primitive leading完整费用及其准确限度

对selected-even Δ_n(T)，256已给degree恰n、leading (16·2^n)^n。令g_n=content(C_n^{new})≥1，取primitive正leading多项式Π_n=C_n^{new}/g_n，leading coefficient为

\[
 \ell_n=\frac{\widetilde q^n}{\kappa_n g_n}(16\cdot2^n)^n
 \le\frac{\widetilde q^n}{\kappa_n}(16\cdot2^n)^n.
 \tag{P27}
\]

本稿并未计算g_n或宣称primitive最小费用等于这个upper。准确完整scalar账为

\[
 \log\frac{\widetilde q^n}{\kappa_n}
 =n[(3n-2)\log2+2\psi(2n)]
 -\frac{n(n+1)}2\log2,
 \tag{P28}
\]
\[
 \log\ell_n\le2n\psi(2n)
 +\left(\frac72n^2+\frac32n\right)\log2.
 \tag{P29}
\]

加目标leading所用的(n²+4n)log2不能漏掉。按标准PNT换算，scalar leading为4+(5/2)log2；primitive ℓ leading安全upper为**4+(7/2)log2**。256相应ℓ费为6+(9/2)log2；两证书差正好

\[
 \log M_n=n[(n+1)\log2+\psi(2n)]
 =(2+\log2)n^2+o(n^2).
 \tag{P30}
\]

不用PNT也有exact(P24)/(P25)/(P28)/(P29)，和全系数O(n²)费用。这不是从已选upper推actual費用lower；仅说明本轮给出比原完整证书严格更强的全内容/leading upper。

若Y=u/v既约有理，v>0，则v^nΠ_n(Y)为整数；**另需Π_n(Y)≠0**才可用|Π_n(Y)|≥v^{-n}。谱式仍是同一K_n的

\[
 \Pi_n(Y)=\ell_n\prod_{j=1}^n(Y-\lambda_j(K_n)).
 \tag{P31}
\]

本轮只改变(P31)中完整leading费的证书。全部actual根距离、无界nonzero与同对象strict需由本轮其它工作实际支付，不能将其generic Chebyshev障碍或费upper当成Y处lower。若与实际energy比较后仍没有足够严格宏观余量，本轮固定prototype窗口仍应结算；费用改善本身不自动准入prime、参数、Frobenius或sheet扩展。

## 8. 本轮报告

已证明：同一完整native array的\widetilde q_H全prefix清整，minus双重binomial头、plus even/odd全prime-power两层界，旧完整integer determinant polynomial的ALL n内容因子M_n，以及primitive leading安全fee的真实二次阶改进2+log2。

未证明：最大primitive content、actual Δ_n(Y)无界非零、目标谱积strict decay、优化successor/digit费用或新数值无理性/线性无关性。原goal active；本稿不判定全部χ−8方法no-go，也不自行续开下一轮窗口。

本稿及scope限NEW257；旧稿、main、policy、manifest、archive与外Git不改。数学程序、finite-n/CAS/interval/prime/参数/map/word扫描、Lean、外Git写、旧producer运行均0。工具只做实际FULL文档读、manifest pin核、新稿保存与最终FULL复读/hash。没有新增primary搜索或下载，核心证明自含。
