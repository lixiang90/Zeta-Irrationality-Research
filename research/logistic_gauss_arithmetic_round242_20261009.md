# 第242轮：K5全系数GreedyBound与小素数净费用

2026-10-09，A。固定X=3ζ(3)+ζ(5)和完整3n列池，不改变241对象。
本人数学程序、参数扫描、Lean执行均0。本稿给全prime费用的可核上界机制；
没有证明该上界低于6，也没有新的数值无理性定理。

## 1. 固定模型与待付预算

设h=3n，
\[
 D_m(t)=\prod_{j=1}^m(t+j),\quad R_n=D_n^4/D_{5n},\quad
 Q_n(T)=\det[U_T(t^{i+j}R_n)]_{i,j<h},
\]
\[
 S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{h-1}(i!)^2,\quad
 \widetilde Q_n=S_n^hQ_n/F_n. \tag{G1}
\]
U_T保留B⁺((tf)′)、B⁺((tf)‴)、全部简单残数与调和头；系数3/2、
1/24，target T=X。若G=tf=P+Σ c_j/(t+j)，则
\[
 U_T(f)=\tfrac32B^+(P')+\tfrac1{24}B^+(P''')
       +\sum_jc_j(3H_j^{(3)}+H_j^{(5)})-T\sum_jc_j. \tag{G2}
\]
令g_p(A)=min_k v_p([T^k]A)为完整polynomial的Gauss valuation。
以下primitive费用只在Q_n≠0时定义：P_n=d_n Qtilde_n∈Z[T]，
所有整数系数的gcd为1，d_n>0。因此v_p(d_n)=−g_p(Qtilde_n)。

241已付n=p−1的actual有理关系点无界非零。本轮的问题是
log d_n的全prime累计，不是逐entry安全分母。本稿保留S_n和F_n，
并分别处理5n<p²的大prime与其它prime。

## 2. 大prime的完整CRT分配与基单位

取p≥7且5n<p²。对b=0,…,p−1定义
\[
 N_b=\#\{1\le j\le n:j\equiv b\pmod p\},\quad
 C_b=\#\{1\le j\le5n:j\equiv b\pmod p\},
\]
\[
 e_b=4N_b+[b=0],\qquad c_b=e_b-C_b-4,\qquad
 \rho_{b,i}=c_b/2+i\quad(i=0,1,\ldots). \tag{G3}
\]
这里C_b是全部极点数，不能只保留j=p。选择所有p个递增slot列中
最低h个ρ；相等时固定按b排序。各列选出的slot必是prefix
i=0,…,k_b−1，Σ_b k_b=h。令M为最大的已选slot，则
\[
 c_b/2+k_b\ge M\ge\rho_{a,i}\quad(i<k_a),\ \text{每个 }b. \tag{G4}
\]
这是后续所有pair比较所需的确切greedy条件，不是连续松弛。

定义h个完整基向量
\[
 \phi_{b,i}(t)=(t+b)^i\prod_{d\ne b}(t+d)^{k_d},
 \qquad 0\le i<k_b. \tag{G5}
\]
每个degree=h−k_b+i<h。模p对不同中心−b作CRT，
局部模(t+b)^(k_b)时其它簇向量为0，本簇向量是
(t+b)^i乘以同一个常数项非零的unit polynomial。
因而局部系数表为可逆三角矩阵。总degree<h的模p空间尺寸h，
所以G5的h×h monomial系数变换Δ在p处是unit。
这里使用Taylor系数与商环，未使用含i!的ordinary derivative jets，
故无需假设k_b<p。

双线性展开给det Gram(G5)=det(Δ)² Q_n。
于是该基上的全系数Gauss下界直接给原完整Q_n的同一下界；
并未取子矩阵或丢target方向。

## 3. 所有pair与其它盘的权重

取a=(b,i)、c=(b′,j)。在盘t=pu−d，基φ_a的p因子数是
z_a(d)=i若d=b，否则k_d。完整numerator
A=tφ_aφ_cD_n⁴在该盘的Gauss valuation至少
\[
 E_d=e_d+z_a(d)+z_c(d),\qquad
 \beta_{ac}=\min_d(E_d-C_d). \tag{G6}
\]
所有other-class因子在该盘为unit；same-class根因子各贡献p。
改换同一class的整数中心只是u的整数平移，所以G6也满足241
class-wise numerator假设。degree A≤10n−1，且同类不同极点差
恰含一个p。241完整entry引理因此给
\[
 g_p(U_T(\phi_a\phi_cR_n))\ge\beta_{ac}-4,\qquad
 v_p([T^1]U_T(\phi_a\phi_cR_n))\ge\beta_{ac}+1. \tag{G7}
\]

逐盘比较G6−4：

1. a,c同簇，自己的盘是c_b+i+j=ρ_a+ρ_c。
   任一其它盘d是c_d+2k_d=2(c_d/2+k_d)≥2M≥ρ_a+ρ_c。
2. a,c不同簇，在a盘是c_b+i+k_b。
   减去ρ_a+ρ_c后是c_b/2+k_b−ρ_c≥0；在c盘同理。
3. 在既非a亦非c的其它盘，仍是2(c_d/2+k_d)≥ρ_a+ρ_c。
   k_d=0的空簇也满足G4，不能从minimum中删掉。

故所有pair都有β_ac−4≥ρ_a+ρ_c。完整entry商部和调和头包含在
G7，而非仅局部最高项；本轮不要求leading blocks非退化或严格cross余量。

定义确切整数分配成本
\[
 G_p(n)=2\sum_{\text{selected}}\rho_{b,i}
       =\sum_{b=0}^{p-1}\{k_b c_b+k_b(k_b-1)\}. \tag{G8}
\]
每个determinant permutation的Gauss valuation至少2Σρ=G_p，
每个polynomial coefficient也满足该界。因此
\[
 \boxed{g_p(Q_n)\ge G_p(n)},\qquad
 \boxed{g_p(\widetilde Q_n)\ge
 G_p(n)+h\,v_p(S_n)-v_p(F_n)}. \tag{G9}
\]
halfweights只参与不等式，G8为整数；无需实际引入√p。
这支付任意n的完整K5 GreedyBound。新c_b中的−4已由商部、
三次微分和H⁵共同证明，不能凭旧K3的−2口头平移。

n=p−1时G3的三类c分别−7、−5、−4，最低h个slot给
k=(4,3,2)。G8为5−9p，与241exact值相容；
任意n的G9是下界，不声称处处恰等或给actual内容下界。

## 4. 小prime：binomial完整基原地保留F_n

直接对monomial entries套240安全LCD再除F_n，可能留下n²级甚至
更大的factorial费用，不能以“小prime数量少”将其抹掉。
改取完整有理基ψ_i(t)=binom(t,i)，i=0,…,h−1。
其monomial系数表三角，det为∏_(i=0)^(h−1)(i!)⁻¹。
于是有确切polynomial恒等式
\[
 \widetilde Q_n=\det[S_n U_T(\psi_i\psi_jR_n)]_{i,j<h}. \tag{G10}
\]
这不是换了数值对象；F_n恰为两个基变换的共同因子。

现在p可为任意素数，设κ_p=floor(log_p(10n))。
对f=ψ_iψ_jR_n，tf的商部P degree d≤5n−1。
由240完整残数公式，S_n res(R_n,−j)为整数，而
ψ_i(−j)、ψ_j(−j)、−j均为整数。因此
\[
 S_n c_j\in Z\quad(1\le j\le5n). \tag{G11}
\]
特别target coefficient S_n(−Σ c_j)是整数。

对整数0≤m≤d，有
\[
 S_nR_n(m)=
 \frac{\binom{m+n}{n}^{4}}{\binom{m+5n}{5n}}. \tag{G12}
\]
m+5n≤10n−1。Legendre公式中
floor((m+5n)/p^a)−floor(m/p^a)−floor(5n/p^a)每项是0或1，
非零项至多κ_p个，因此分母binomial的p估值至多κ_p。
ψ_i(m)、ψ_j(m)、m是整数，所以v_p(S_n tf(m))≥−κ_p。
G11的pole terms分母m+j在1至10n−1，也最多损κ_p。
故完整商部S_n P(m)≥−κ_p，覆盖Newton所需全部m=0,…,d。

其前向差分系数在binomial展开中也至少−κ_p。
微分公式241 A3每次最多损κ_p，B⁻最多再损κ_p；
B⁺=B⁻+[t¹]的后一项由下一次微分在0评价同样控制。
所以B⁺((S_nP)‴)至少−5κ_p，一阶更强。
G11乘H_j⁵至少−5κ_p，H_j³更强；固定1/24在p处最多损v_p(24)。
完整有理部分和target部分因此给
\[
 g_p(S_n U_T(\psi_i\psi_jR_n))
       \ge-5\kappa_p-v_p(24),\qquad
 \boxed{g_p(\widetilde Q_n)\ge-h(5\kappa_p+v_p(24))}. \tag{G13}
\]
包括固定2、3和全部prime powers，没有“单pole代表全部”的步骤。
G13不是最优，但可用于小prime。

## 5. whole-prime primitive费用上界

对n足够大，p≤√(5n)全部用G13。每个κ_p log p≤log(10n)，
只用prime数量≤√(5n)，已得
\[
 \sum_{p\le\sqrt{5n}}v_p(d_n)\log p
 \le 15n\sqrt{5n}\log(10n)+3n\log24=o(n^2). \tag{G14}
\]
固定2、3的单独贡献上界为O(n log n)。右侧是费用upper；
即使某些v_p(d_n)为负，仍可合法上估。

p>5n时，完整残数、harmonic heads和Bernoulli分母均p-整，
且p不除S_n,F_n、24；故g_p(Qtilde_n)≥0，v_p(d_n)≤0。
丢掉这些负或零贡献是合法upper，不能把它们改写成positive费用。
其余prime满足5n<p²，可以用G9。因此对于Q_n≠0，
\[
 \boxed{\log d_n\le
 \sum_{\sqrt{5n}<p\le5n}
 \big[v_p(F_n)-h\,v_p(S_n)-G_p(n)\big]\log p+o(n^2)}. \tag{G15}
\]
有限小n不影响asymptotic；其中large p自动≥7。
各large-prime的normalization可显式写成
\[
 v_p(S_n)=\lfloor5n/p\rfloor-4\lfloor n/p\rfloor,\qquad
 v_p(F_n)=2\sum_{i=0}^{h-1}\lfloor i/p\rfloor. \tag{G16}
\]
因为所有factorial参数<p²，没有遗漏更高幂。sum括号可能为负，
无需取正部；G15只是一条primitive净费用上界。
若其它自含lemma提供更强的all-coefficient Gauss下界，可在对应
prime window将G9替换，取同对象两下界的max，而不是累加节省两次。

## 6. 该机制支付什么

G3–G9付完整单位CRT与所有pair/其它盘的K5 greedy bound；
G10–G14付保留F_n的小prime o(n²)，并明确固定2、3。
G15是全prime费用的可核mechanism，不是宏观积分率或最优内容。
241的无界关系点非零保持；本稿不重新证明它，不扫描prime。

B负责同一G15的macroscopic积分，C负责outer window的额外内容。
只有实际完整Gauss预算低于已认证同对象实界后才可作数值结论；
240的−6原完整FstarInput仍未认证，不因本稿得到费用upper而自动完成。
本人数学程序0，新增primary只有固定commit Greedy一份且实际FULL读。
其它原源复用241既有FULL范围。本人保存后全文复读，身份另报，
独立审阅与作者自读分别登记。见[scope](../literature/logistic_gauss_budget_round242_20261009/alternative_reading_scope.md)。
