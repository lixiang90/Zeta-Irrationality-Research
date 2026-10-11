# 第253轮：固定RV五列的实际系数、倒数变换与常数保留

2026-10-10，C独立纸证。固定n≥2、r=0,…,4的实际包，不换列池。本稿给出同一Q的全n系数恒等式，并证明前四列在Q[z]/(z⁴+1)中满秩。因此常数目标没有被移位或倒数对称排除；可以选择整数向量保留非零常数余数。没有证明数值关系点无限非零、primitive费用或复积分strict余量。数学程序、CAS、参数/素数/n头扫描均0。

## 1. 完整归一化与实际双residue

采用Rhin–Viola原文(2.1)–(2.4)、Theorem2.1的完整定义：
\[
 I_z=I_z^{(0)}-(\log z)I_z^{(1)},\qquad
 Q=d_Hd_K z^\alpha(z-1)^\beta I_z^{(2)}.
\]
其双contour的内圈是y=x/(x−z)，外圈是x=z，两个均为正向。原文物理PDF4–6完整读域和252完整模型的身份见[记录](../literature/rv_chi8_sources_round253_20261010/dual_reading_scope.md)。不把未修正的I⁽⁰⁾当作纯Li₂源。

本包参数为
\[
 (h,j,k,l,m)=(10n+r,8n,8n,5n,10n),\quad
 H=13n+r,\quad K=12n+r,\quad
 \alpha=\delta=16n,\quad\beta=3n-r.
\]
由于n≥2、r≤4，β≥0且δ确为16n。令
\[
 \Lambda_n=d_{13n+4}d_{12n+4},\qquad
 F_{n,r}=\Lambda_n z^{16n}(z-1)^{3n}I_z=P_{n,r}-Q_{n,r}\operatorname{Li}_2(1/z).
\]
这里d_a=lcm(1,…,a)。同一完整Q为
\[
 Q_{n,r}(z)=\Lambda_n z^{16n}(z-1)^{3n}I_z^{(2)}.
 \tag{C1}
\]
与个别定理的Q相差整数LCM比及(z−1)ʳ；故P、Q仍在Z[z]。h移位不能省掉这项归一化。

记N=10n+r。双residue的integrand为
\[
 z^{-15n}\frac{x^{8n}(1-x)^N y^{8n}(1-y)^{5n}}
 {[x+(z-x)y]^{6n+1}}\,dy\,dx.
\]
在y₀=−x/(z−x)取6n阶系数。用y₀、1−y₀=z/(z−x)，并令u是落在y⁸ⁿ上的微分数，内residue为
\[
 \sum_{u=n}^{6n}\binom{8n}{u}\binom{5n}{6n-u}
 \frac{x^{8n-u}z^{u-n}}{(z-x)^{13n+1}}.
\]
内层符号是(−1)¹⁴ⁿ=1。外residue使用
(z−x)⁻¹³ⁿ⁻¹=(−1)ⁿ⁺¹(x−z)⁻¹³ⁿ⁻¹，得到
\[
 Q_{n,r}
 =(-1)^{n+1}\Lambda_n(z-1)^{3n}
 \sum_{u=n}^{6n}\binom{8n}{u}\binom{5n}{6n-u}
 \frac{z^u}{(13n)!}
 \left.\partial_x^{13n}\{x^{16n-u}(1-x)^N\}\right|_{x=z}.
 \tag{C2}
\]
展开(1−x)ᴺ，得同一系数公式
\[
 Q_{n,r}(z)=(-1)^{n+1}\Lambda_n z^{3n}(z-1)^{3n}
 \sum_{v=0}^{N}(-1)^v\binom Nv A_n(v)z^v,
 \tag{C3}
\]
\[
 A_n(v)=\sum_{u=n}^{6n}
 \binom{8n}{u}\binom{5n}{6n-u}\binom{16n-u+v}{13n}.
 \tag{C4}
\]
广义binomial作为v的多项式；v≥0时也就是普通binomial，顶端不足时取0。这里A_n完全独立r，h移位只改变N和binomial行。

## 2. 系数多项式的全n因式分解

定义
\[
 T_n(v)=
 \prod_{a=2n+1}^{10n}(v+a)
 \prod_{a=3n+1}^{8n}(v+a).
\]
则精确地
\[
 \boxed{A_n(v)=\frac{T_n(v)}{(6n)!(7n)!}.}
 \tag{C5}
\]
以下直接证明，不借有限样本或未读的超几何公式。A_n的degree为13n；Vandermonde给其leading coefficient
\[
 \frac1{(13n)!}\sum_u\binom{8n}{u}\binom{5n}{6n-u}
 =\frac{\binom{13n}{6n}}{(13n)!}
 =\frac1{(6n)!(7n)!}.
\]
当2n+1≤s≤10n、n≤u≤6n时，
0≤16n−u−s≤13n−1。因此C4每项在v=−s均为0，给8n个根。

在3n+1≤s≤8n，还可证明这些根至少二重。若a=16n−u−s，则
\[
 \left.\frac{d}{dv}\binom{16n-u+v}{13n}\right|_{v=-s}
 =(-1)^{u+s-3n-1}\int_0^1 x^a(1-x)^{13n-1-a}\,dx.
\]
有限和与积分交换，并用Leibniz–Rodrigues身份
\[
 \frac{\partial_x^{6n}\{x^{8n}(1-x)^{5n}\}}{(6n)!}
 =\sum_u(-1)^u\binom{8n}{u}\binom{5n}{6n-u}
 x^{8n-u}(1-x)^{u-n},
\]
得到
\[
 A_n'(-s)=\frac{(-1)^{s-3n-1}}{(6n)!}
 \int_0^1
 x^{8n-s}(1-x)^{s-2n-1}
 \partial_x^{6n}\{x^{8n}(1-x)^{5n}\}\,dx.
 \tag{C6}
\]
测试多项式degree恰为6n−1，其0端指数≥0，1端指数≥n。连续分部积分6n次的全部boundary项为0：在0，核的最高6n−1阶导数仍有零；在1，若测试导数阶j≤n−1则测试仍有零，若j≥n则核导数阶6n−1−j≤5n−1仍有零。最终测试的6n阶导数为0，故C6为0。

由8n个根及重叠区额外5n个根、degree与leading coefficient，C5成立。这是全n系数恒等式，归一化中的Λ及两个factorials没有被丢掉。

令θ=z∂z，代入C3得到
\[
 \boxed{
 Q_{n,r}(z)=
 \frac{(-1)^{n+1}\Lambda_n}{(6n)!(7n)!}
 z^{3n}(z-1)^{3n}\,
 T_n(\theta)(1-z)^{10n+r}.}
 \tag{C7}
\]
它直接给出实际五列，不是formal dimension计数。

## 3. 前四列在Φ₈商中满秩

写$Q_{n,r}\bmod\Phi_8=\sum_{j=0}^3q_{j,r}z^j$，其中$q_{j,r}\in\mathbb Z$。

对实系数非零多项式f及正整数a，算子θ+a不减少正实零点总数，按重数计。因为
\[
 (\theta+a)f=z^{1-a}\partial_z(z^a f).
\]
zᵃf有0处零点及f全部正根。Rolle定理在0到第一个正根、相邻正根之间各给一个根，加上每个重根保留的重数，总数至少等于f的正根数。leading coefficient被乘以deg(f)+a>0，所以degree不变；算子在R[z]上也可逆。

若前四列模Φ₈=z⁴+1存在非零有理线性关系，取w₀,…,w₃非全0，则C7中的输入是
\[
 (1-z)^{10n}p(z),\qquad
 p(z)=\sum_{r=0}^{3}w_r(1-z)^r\ne0,\quad\deg p\le3.
\]
它至少有10n个正根，degree≤10n+3。T_n(θ)是13n个θ+a、a>0的乘积，因此输出仍非零，至少有10n个正根，degree≤10n+3。若它可被Φ₈整除，还必须有四个互异非实根，总根数≥10n+4，矛盾。

公共因子z³ⁿ(z−1)³ⁿ在Q[z]/(Φ₈)中是单位；外面的非零scalar亦不改变秩。因此
\[
 \boxed{\operatorname{rank}_{\mathbb Q}
 (q_{j,r})_{0\le j\le3,\ 0\le r\le3}=4
 \quad\text{对所有n≥2}.}
 \tag{C8}
\]
这同时证明五列的rank为4、去常数行rank为3，严格大于关系成立全n，强于无界n。

更具体地，设E_n=(q_{j,r})₀≤j,r≤3∈Mat₄(Z)，取
\[
 (v_0,v_1,v_2,v_3)^t=\operatorname{adj}(E_n)e_0,\qquad v_4=0.
\]
则Σv_r Q_{n,r}≡c_n modΦ₈，c_n=det E_n≠0为整数。采用252已付的完整Gauss trace，得到
\[
 \tau_\chi^{-1}\sum_{a=1,3,5,7}\chi(a)
 \sum_r v_r F_{n,r}(\zeta^{-a})
 =A_n^{\rm rat}-c_nL(2,\chi_{-8}),
 \qquad A_n^{\rm rat}\in\mathbb Z.
 \tag{C9}
\]
这里ζ=e^{πi/4}、τχ=i√8；A_n^{rat}与C4的系数多项式A_n不同。adj高度、共同primitive content和数值左端非零没有免费支付。

## 4. 倒数对称与h移位的准确含义

C5给T_n(v)>0且严格递增v≥0。C7去掉公共因子后的多项式
\[
 B_N(z)=T_n(\theta)(1-z)^N
 =\sum_{v=0}^N(-1)^v\binom Nv T_n(v)z^v
\]
常数为T_n(0)，最高系数为(−1)ᴺT_n(N)，其绝对值严格不同。因此B_N不是正负palindromic polynomial。实际Q的最低非零次数是3n，最高是16n+r；任何多项式倒数特征式zᴸQ(1/z)=εQ(z)都迫使L=19n+r及ε=±1，首尾大小不同又排除它。个别RV定理归一化的Q除以(z−1)ʳ后，L应为19n，同样排除。此处没有把倒数变换的degree错取成最高degree。

θ与乘z不交换，故不能把h移位当作单纯乘(1−z)ʳ：
\[
 B_{N+r}(z)=
 \sum_{j=0}^{r}(-1)^j\binom rj z^j
 T_n(\theta+j)(1-z)^N.
 \tag{C10}
\]
把个别β归一化补成公共(z−1)³ⁿ，正好得到C7；不会取消C10中的移位算子。

在cyclotomic商K=Q[z]/(Φ₈)，倒数共轭是
\[
 (q_0,q_1,q_2,q_3)\longmapsto(q_0,-q_3,-q_2,-q_1).
\]
公共M=z³ⁿ(z−1)³ⁿ满足
\[
 M(1/z)=(-1)^n z^{-9n}M(z)
 =(-1)^n z^{-n}M(z)\quad\text{于K}.
\]
这只给公共因子的相位，不给B_N的相位。更强的是C8已经排除整个列空间落入同一real或imaginary特征空间以及排除常数的任何线性超平面；常数目标确实在实际列空间中。

若用core列复核余数，必须保留目标向量M⁻¹，而不是把core的常数当原Q的常数：
\[
 M^{-1}=(-1)^n2^{-3n}z^{-3n}(1+z+z^2+z^3)^{3n}\quad\text{于K}.
\]
该等式由(z−1)⁻¹=−(1+z+z²+z³)/2得出；2幂及adj尺度仍属于后续完整高度账。

## 5. 已关闭的首关与保留的未付接口

本稿实际证明固定包的全n常数余数保留，不借维数、泛型、有限n头或另一源。它没有证明C9在每个固定有理假设点无限非零，也没有证明v_n及全部系数的primitive费用或四个复杂积分的统一strict预算。因此首关成功只允许下一项同对象准入，不构成新L值无理性定理，不自动开启地图、prime或参数优化。
