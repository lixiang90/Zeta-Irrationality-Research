# 原混合低阶jets的节点熵与左右Hardy支撑：全尺度解析改善

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority为main §§166–170与audit hasse_bridge SHA94eec763f855689bda6ecfb6fd3e4c0af2fef50fcff2e357fc032c720d04d2d3；564冻结记录（559数学、5guards）全部只读。唯一NEW主稿，数学producer创建/execute/import/rerun0，旧成功及同行运行0，prime扩表0，Lean0。保留原B6/κ3/s5、degree<3n、rank2n饱和整数值基；不单独改变P而把离散斜率V留在旧基。

## 1. 同一对象、读域与新结论

本轮实际FULL读前解析A1–A27/10节、Hasse桥接H1–H17/8节、lattice I1–I25、actual-local G1–G15、coupled C1–C23、energy E1–E26及primitive-gcd G1–G13。输出均完整；不继承这些稿的旧producer执行或原始PDF读页。总稿实际读§§166–170；audit完整JSONparse/header/current_progress/564/559/5计数字段，非全部记录逐条人工全文读或本agent全564物理SHA重核。

原basis及实际common因子记为
\[
g=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\quad
f_i(z)=\binom{z-1}{i},\quad
G_m=(b_mL_m+b_{m'}L_{m'})/\beta_m,
\]
\[
m'=2n+1-m,\quad b_a=\binom{6n+a}{a-1},\quad
\beta_m=\gcd(b_m,b_{m'}),\quad
\Gamma_n=\prod_{m=1}^n\beta_m,\quad
S_n(z)=\prod_{a=1}^{2n}(z-a).
\tag{S1}
\]
P_n为X=ξ=αζ(4)+βζ(5)、β≠0处原continuous total-variation Gram，V_n为原X斜率，
\[
V_n=24\sum_{j=0}^{6n}W_jg(-j)g(-j)^t,\quad
W_j=\binom{6n}{j}^{2}\binom{2n+j}{j}^{3},\quad
H_{n,k}=[t^k]\det(P_n+tV_n).
\tag{S2}
\]
两者都在S1的同一原basis。冻结H13/A19给
\[
|J_{n,k}(\xi)|\le H_{n,k},\qquad
J_{n,k}(\xi)=[t^k]\det B_n(\xi+t).
\tag{S3}
\]

定义下节的精确节点熵常数Θ=K_3。**新主定理**对每个n和0≤k≤n有
\[
\boxed{\log H_{n,k}\le-\frac{22}{3}n^2-2\log\Gamma_n+
(\Theta+\tfrac{17}{2})nk+C n\log(n+2),\quad
\Theta<\frac{11557}{400}.}
\tag{S4}
\]
因此n=4r、adaptive k≤n/2时
\[
\boxed{\limsup n^{-2}\log\max_{0\le k\le n/2}H_{n,k}
\le\frac{\Theta}{2}-\frac{37}{12}-2\gamma
<\frac{27271}{2400}-2\gamma<\frac{1691}{200}=8.455,}
\quad \gamma=\lim n^{-2}\log\Gamma_n\ge1.455845.
\tag{S5}
\]
相对冻结A27的同一upper常数，新常数减少超过5.79。它仍未给负衰减保证，更未跨whole-X safe费用40.3145；不证明实际jet增长、实际最优衰减upper或no-go。

## 2. 全部真实节点的精确二项式熵

对x,t≥0置0log0=0，并定义
\[
E(x,t)=(x+t)\log(x+t)-x\log x-t\log t,
\]
\[
w(x)=2E(x,6-x)+3E(x,2),\qquad
K_t=\max_{0\le x\le6}\{w(x)+2E(x,t)\},\quad t=2,3.
\tag{S6}
\]
binom(N,l)≤exp[NlogN−llogl−(N−l)log(N−l)]直接来自二项分布某一项≤1；l=0,N单独为1。所以每个真实j=0,…,6n、x=j/n都满足
\[
W_j\le e^{nw(x)},\qquad
|f_i(-j)|=\binom{j+i}{i}\le e^{nE(x,i/n)}.
\tag{S7}
\]
E(x,t)对t非降，因此全部原high i=2n,…,3n−1得到无漏节点的
\[
\boxed{(V_n)_{n+1+l,n+1+l}
\le24(6n+1)e^{nK_3},\qquad0\le l<n.}
\tag{S8}
\]
这取代A22的54nlog2；没有把连续cot衰减套在负整数源节点，也没有换high factorial。

## 3. K_2、K_3的严格纸面全域界

令F_t(x)=w(x)+2E(x,t)。在0<x<6，
\[
F_t'(x)=2\log(6-x)+3\log(x+2)+2\log(x+t)-7\log x,
\]
\[
F_t''(x)=-\frac2{6-x}-\frac7x+\frac3{x+2}+\frac2{x+t}
<-\frac2{6-x}-\frac2x\le-\frac43.
\tag{S9}
\]
故F_t严格凹，唯一max在内部；任何x_0都给
K_t≤F_t(x_0)+(3/8)F_t'(x_0)^2。端点由连续性覆盖，无sampling。

取x_0=9/2。下列有理log界来自
\[
\log\frac{1+z}{1-z}=2\sum_{q=0}^{N-1}\frac{z^{2q+1}}{2q+1}+R_N,\qquad
0<R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\tag{S10}
\]
z=1/3取N=3，z=1/5取N=2，z=1/9取N=2；z=1/25、1/4取首项与geometric upper。直接清分母给
\[
\frac{693}{1000}<\log2<\frac{1733}{2500},\quad
\frac{4053}{10000}<\log\frac32<\frac{811}{2000},
\]
\[
\frac2{25}<\log\frac{13}{12}<\frac{25}{312},\quad
\frac{2231}{10000}<\log\frac54<\frac{279}{1250},\quad
\log\frac53<\frac8{15}.
\tag{S11}
\]
全为纸证，不创建或执行常数认证程序。

准确展开为
\[
F_2(9/2)=\frac{95}{2}\log2-\frac{43}{2}\log\frac32+
\frac{65}{2}\log\frac{13}{12}<\frac{1609033}{60000},
\]
\[
F_3(9/2)=\frac{99}{2}\log2-\frac{51}{2}\log\frac32+
\frac{39}{2}\log\frac{13}{12}+15\log\frac54<\frac{23111}{800}.
\tag{S12}
\]
其derivatives分别是3log2−7log(3/2)+5log(13/12)，以及3log2−7log(3/2)+3log(13/12)+2log(5/4)。S11夹住
−2/5<F_2'(9/2)<0、−1/10<F_3'(9/2)<0。因此S9给
\[
\boxed{K_2<\frac{1612633}{60000}<27,\qquad
\Theta=K_3<\frac{11557}{400}<29.}
\tag{S13}
\]
27与第一upper的余量7367/60000；29与第二upper的余量43/400。两侧0、6和全部内部点都被严格凹全域上界控制，未把几个节点检查冒称sup证明。

## 4. 原low的真实离散Gram由左Hardy支撑控制

准确cardinal/κ公式沿coupled C2给
\[
\frac{G_m(z)}{S_n(z)}
=\frac{\kappa_m}{z-m}+\frac{\kappa_{m'}}{z-m'},\qquad
\widetilde\kappa_a=\beta_m\kappa_a
=\frac{(-1)^a(6n+a)!}{(6n+1)!(a-1)!^2(2n-a)!}.
\tag{S14}
\]
对任何low subset J及任意complex系数u_m，F(z)=Σ_(m∈J)u_mG_m(z)/S_n(z)在Re z≤1/2无pole且F(z)=O(1/z)。在boundary z=1/2+iy的L²范数记为||F||_L²。

对实w=−j，左半平面Cauchy公式给
\[
F(-j)=\frac1{2\pi}\int_{\mathbf R}
\frac{F(1/2+iy)}{j+1/2+iy}\,dy,
\]
\[
\boxed{|F(-j)|^2\le\frac{\|F\|_L^2}{4\pi(j+1/2)}.}
\tag{S15}
\]
闭合左半圆时integrand为O(|z|^{-2})，弧积分趋0；boundary核的平方积分恰π/(j+1/2)，故常数准确。不需要调用未经核scope的Carleson或采样定理。

定义真实positive离散mass与scalar
\[
\omega_j=24W_j|S_n(-j)|^2,\qquad
R_n=\frac1{4\pi}\sum_{j=0}^{6n}\frac{\omega_j}{j+1/2}.
\tag{S16}
\]
S15乘每个ω_j并相加，得对原low subset的Hermitian Loewner inequality
\[
\boxed{(V_n)_{J,J}\preceq R_n\,\mathcal G_{L,J},\qquad
\mathcal G_{L,J}=\left[\int_{\mathbf R}
\frac{G_m(1/2+iy)}{S_n(1/2+iy)}
\overline{\frac{G_l(1/2+iy)}{S_n(1/2+iy)}}dy\right]_{m,l\in J}.}
\tag{S17}
\]
这里是同一原basis上的估计，不是令P换新基而V仍旧基；原pairκ和β完整留在两边。只用finite support实际0,…,6n，没有把discrete measure免费替成连续measure。

## 5. source-low的熵、Hardy排斥与Γ

真实负节点有
\[
|S_n(-j)|=(2n)!\binom{j+2n}{2n}.
\]
S7给W_j binom(j+2n,2n)^2≤e^{nK_2}。于是S16的全部节点有限sum满足
\[
\log R_n\le4n\log n+
n(K_2+4\log2-4)+O(\log(n+2)).
\tag{S18}
\]
可用Σ1/(j+1/2)≤2(6n+1)直接上界，真正harmonic上界只更强；(2n)!²的Stirling以及j=0均已支付。

对a=|J|个真实pairs作same L² determinant triangle，选择数2^a只付O(n)。每个选择恰取互不重叠pair中的一个head；左Hardy距离δ_L=a_head−1/2∈{1/2,…,2n−1/2}。Cauchy determinant与排序δ_i≥i−1/2给
\[
\log\mathcal H_{L,a}
\le a\log(2\pi)-\frac{a(a-1)(2a-1)}{6n}
=-\frac{a^3}{3n}+O(n).
\tag{S19}
\]
这与原右线δ_R=2n+1/2−a_head的Hardy支撑不同，但保留同一pair/κ数据，uniform cubic适用两侧。S17 determinant monotonicity、S14/S18及冻结准确uniform Stirling
log|κtilde_head|=−(2n−1)logn+nh(head/n)+O(logn)
相消全部n²logn后给
\[
\boxed{\log\det(V_n)_{J,J}
\le\Lambda\,a n-\frac{a^3}{3n}
-2\sum_{m\in J}\log\beta_m+O(n\log(n+2)),}
\]
\[
\Lambda=K_2+2g_*,\qquad
g_*=\max_{0\le t\le2}\{h(t)+2\log2-2\},\qquad
h(t)=(6+t)\log(6+t)-2t\log t-(2-t)\log(2-t)-6\log6+2.
\tag{S20}
\]
两个(j−1)!与整个common (2n)!²均保留；a=0,1边界由同一常数覆盖。相比仅估source diagonals，本式新增真实−a³/(3n)。

## 6. head熵与真正最坏分配的反转

冻结A9–A10的强凹纸证在t=3/2给
\[
2g_*\le11\log2+15\log\frac54-3\log\frac32+
\frac38\log^2\frac53<\frac{295919}{30000}<10.
\]
\[
\boxed{\Lambda<\frac{2204471}{60000}<37.}
\tag{S21}
\]
head fee未被删除；它与source-low/continuous-low的互补Γ在下面一起计。

还需要精确constants的相对次序，而非仅相减两个upper。F_2'(4)=log(243/128)>0，S9严格凹且F_2'(6−)=−∞，所以K_2的唯一maximizer x_2>4。故
\[
\Theta-K_2\ge2[E(x_2,3)-E(x_2,2)]
=2\int_2^3\log(1+x_2/t)\,dt>2\log2.
\]
\[
\delta_L=\Lambda-\tfrac32,\quad
\delta_H=\Theta+\tfrac{17}{2},\qquad
\boxed{\delta_H>\delta_L+1.}
\tag{S22}
\]
最后由2g_*<10及2log2>1即得。新的支撑比较表明：在这组合法共同upper中，分配给source-high的代价更高；旧A23仅用54/72log2时的“最坏全部source-low”不再适用。

## 7. 原mixed coefficient：互补Γ和两项cubic

沿冻结A20的准确mixed-minor展开
\[
H_{n,k}\le
\left(\sum_{|I|=k}
\sqrt{\det P_{I^c,I^c}\det(V_n)_{I,I}}\right)^2.
\tag{S23}
\]
I中source-low/high数为a,b，a+b=k；互补P有n−a个low和n−b个high。冻结A15给continuous-low的(3/2)(n−a)n−(n−a)^3/(3n)，A12给每个原high−17n/2。S8/S20与block Fischer/Hadamard给
\[
\log[\det P_{I^c,I^c}\det(V_n)_{I,I}]
\le-7n^2-2\log\Gamma_n+\delta_Lan+\delta_Hbn
-\frac{(n-a)^3+a^3}{3n}+O(n\log(n+2)).
\tag{S24}
\]
两侧low subsets恰互补，所以β平方准确覆盖每个pair一次；没有按质量分摊Γ、重复Γ信用或另扣遗漏head fee。high保留原factorial。组合计数与sqrt/sum/平方只付O(n)。

固定k下，S24的a导数是n(δ_L−δ_H+1)−2a<0。故在允许a∈[max(0,k−n),min(k,n)]中，最大取最小a。k≤n取a=0,b=k，直接证明S4。k>n取a=k−n,b=n，可写完整续式
\[
\log H_{n,k}\le-\frac{22}{3}n^2-2\log\Gamma_n+
\delta_Hn^2+(\delta_L+1)n(k-n)-(k-n)^2
+O(n\log(n+2)).
\tag{S25}
\]
这个最大化是所有原subsets的安全upper，不声称真的最大minor按该分配或实际coefficients达到此指数。

## 8. 完整weighted接口与提取费用的精确优化

对固定τ≥0，把全部2n+1个非负coefficients同时估计。S24令u=a/n、v=b/n，得到
\[
\log\det(P_n+e^{-\tau n}V_n)
\le-\frac{22}{3}n^2-2\log\Gamma_n+
n^2\{\phi(\delta_L+1-\tau)+(\delta_H-\tau)_+\}
+O(n\log(n+2)),
\]
\[
\boxed{\phi(z)=\max_{0\le u\le1}(zu-u^2)
=\begin{cases}0&z\le0,\\ z^2/4&0<z<2,\\z-1&z\ge2.\end{cases}}
\tag{S26}
\]
两项cubic的和准确等于1−3u+3u²；u,v的full square覆盖全部分配。没有独立无偿换基，所有Γ/source/head项都在S26。

若控制k≤κn，0≤κ≤1，提取付τκn²。τ<δ_H时
φ(δ_L+1−τ)+(δ_H−τ)+κτ随τ非增；τ≥δ_H时S22使φ=0，剩κτ非减。因此这个**已证正包络upper**的付费τ-optimum可取τ=δ_H，给S4的κ-profile
−22/3−2γ+κδ_H。κ=1/2给S5，不把很小t导致的改善当免费信用。该优化不是实际Ψ、真实phase、所有basis或无理性方法的全局optimum/no-go。

## 9. 改善幅度、完整算术比较与剩余目标

冻结A27的同一adaptive低jet upper为36log2−187/24−2γ。S13后的新upper是27271/2400−2γ，其减少严格大于
\[
36\cdot\frac{693}{1000}-\frac{45971}{2400}
=\frac{69521}{12000}>\frac{579}{100}=5.79.
\tag{S27}
\]
S5的最后比较沿同一已冻结Γ率：
27271/2400−2·1.455845<1691/200，差为
1691/200−27271/2400+291169/100000=283/75000>0。
没有执行新的小数实验，S10–S13/S21所有常数由有限有理纸核承担。

Hasse H6/H8–H17保留同一个固定源、无限适用n上的adaptive k≤n/2非零及whole-X safe费用upper40.314517426059346。必须证明同一所有低jets的upper小于其完整arithmetic lower；S5仍不能达到。任何新k-profile算术费用必须另按同一J_nk实际独审后比较，不能把partial41移入jets，也不能让κ0免费获得κ>0信用。

k0已有q-optimized full determinant更强保证；本文不声称改善它，亦不将它搬给k>0。可继续用同时变换P与V的真实q剪切、离散source Schur投影或相对谱/复相位；这些应提供真正新界，且支付source values与Γ。当前结果不证明足够strict margin或新的ζ/L/Catalan无理性、LI、Lean。

## 10. 本轮来源与闭合状态

全部新关键步骤自证：二项分布entropy upper、全域严格凹与log-series有限尾、左半平面Cauchy点值和同一原low Loewner比较、左右Hardy cubic、真实互补mixed coefficient与付费最大化。新增PDF/HTML/外部code下载0，本轮原始PDF实际新读页0；不继承旧coupled/Hasse作者原文页数。旧成功producer及数值JSON只读政策保留，不执行/import/rerun，也不将冻结结果描述为本轮新认证。

本稿为唯一NEW完整候选；待实际FULL独审、作者收审后最终全文回读及单向FINAL来源收据。564旧记录不变，不预先称strict gap或正式闭合完成。
