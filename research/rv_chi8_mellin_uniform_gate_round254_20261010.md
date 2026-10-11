# 第254轮：同一primitive误差的Mellin压缩、统一解析界与准入结算

2026-10-10，Root纸面推导。保持253同一n≥2包和唯一向量v=adj(首四列R modΦ8)e0、v4=0。数学程序、有限头程序/证书、CAS、参数/prime/map扫描均0。本文给精确全模型与统一解析界，但**没有证明实际误差无界非零或趋零，没有新的数值无理性定理。**

## 1. 同一误差的实际primitive标度

沿253，Φ=t⁴+1、Λ=d_(13n+4)d_(12n+4)，R_r=Q_r/Λ∈Z[t]，δ=det M_R≠0，U=Σv_rR_r≡δ modΦ。

primitive子稿自含支付：令B_n是(8n)!(5n)!/[(6n)!(7n)!]的既约分子，κ_n=2^floor(9n/4)，β_n=κ_n B_n³，则β_n整除每个v_r，直接整除完整整数A、c。这里只除原向量的公共scalar，投影方向不变。令w=v/β、U′=U/β、δ′=δ/β，则U′∈Z[t]、δ′≠0。

定义实际完整Gauss头

\[
S'=(U'-\delta')/\Phi\in\mathbb Z[t],\quad
-\sum_k[S']_k\big((k+1)^{-2}+(k+3)^{-2}\big)=p_n/q_n,
\]

q_n>0、gcd(|p_n|,q_n)=1，p=0时q=1。完整RV Theorem2.1给q_n|Λ*_n=d_(13n+3)d_(12n+3)：第五列为0，首四列多乘的(z−1)^r是整数多项式。不是逐项删分数头的分母。

记d_n=gcd(|p_n|,|δ′|)。实际gcd和primitive形式恰是

\[
g_n=\gcd(|A_n|,|c_n|)=\beta_n(\Lambda_n/q_n)d_n,
\quad(a_n,b_n)=(p_n/d_n,q_n\delta'/d_n),
\]
\[
\ell_n=a_n-b_nY=-\frac{q_n}{d_n}\int_0^1
(-\log t)U'(t)f(t)\,dt,\quad
f(t)=\frac{1+t^2}{1+t^4},\quad Y=L(2,\chi_{-8}). \tag{1}
\]

原Λ不再作为独立最终成本；真正剩余的是q_n/d_n和同一U′的实范数。所有列任意非零有理共同缩放与再取同一adjugate，仅把完整二元组同乘一个scalar，因此不会改变primitive pair。这一projective不变性不允许改变投影方向。

## 2. 比原log正交更强的全区间普通正交

设θ=tD_t，D=(6n)!(7n)!，T为253的正移位算子。逐单项式有

\[
T(\theta)f=t^{-2n}D_t^{8n}\{t^{7n}D_t^{5n}[t^{8n}f]\},
\]
\[
R_r(t)=-\frac{t^n(1-t)^{3n}}{D}
D_t^{8n}\{t^{7n}D_t^{5n}[t^{8n}(1-t)^{10n+r}]\}. \tag{2}
\]

两组operator分别是(t+2n+1)…(t+10n)及(t+3n+1)…(t+8n)，所以(2)不是新核替换。对整数−n≤j<4n，把8n个导数移到测试t^(n+j)(1−t)^(3n)，其degree=4n+j<8n，故导数为0。

边界也付清：内被微分函数G=t^(7n)D^(5n)[t^(8n)(1−t)^(10n+r)]在0至少10n重零，在1至少5n+r重零。8n次IBP的边界项是G^(8n−1−k)乘测试的k阶导数。在0，G每个相关导数仍消失；在1，若G导数不消，则k≤3n−r−1，测试有3n重零，故同样消失。负j区间的测试仍为多项式，原t^jR在0可积。于是每列以及同一U′满足

\[
\int_0^1t^jU'(t)\,dt=0\quad(-n\le j<4n),
\qquad\int_0^1(-\log t)t^jU'(t)\,dt=0\quad(0\le j<2n). \tag{3}
\]

后一组沿253完整∞身份取得。普通正交等价于对正权t^(−n)与0,…,5n−1阶多项式的正交。U′≠0，因为其Φ余数δ′≠0。若其内部变号点少于5n，取这些点的线性因子乘积，可使U′与该测试乘积在(0,1)同号，给非零可积积分，矛盾。故**U′至少有5n个内部变号**。这明确排除把当前线性积分本身当常号载体；不排除其它经过证明的signed变换，也不宣告(1)为零。

## 3. 完整Mellin有理式的整数压缩

记

\[
\mathcal M_n(s)=\int_0^1t^sU'(t)\,dt
=\sum_{k=3n}^{16n+3}\frac{[U']_k}{s+k+1},
\quad\operatorname{Re}s>-3n-1,
\]
\[
D_n(s)=\prod_{k=3n}^{16n+3}(s+k+1),\qquad
G_n(s)=\prod_{j=-n}^{4n-1}(s-j)\prod_{j=0}^{2n-1}(s-j).
\]

D_n长13n+4、D_n M_n∈Z[s]。因U′有(1−t)^(3n)因子，固定n时M_n(s)=O(s^(−3n−1))于实s→+∞，故分子degree≤10n+3。由(3)，−n,…,4n−1都是零点；0,…,2n−1同时M′=0，因此有第二重。它们均避开分母极点，G_n是首一整数多项式，整除整数分子后得到

\[
\boxed{\ \mathcal M_n(s)=\frac{G_n(s)H_n(s)}{D_n(s)},
\quad H_n\in\mathbb Z[s]\setminus\{0\},\quad\deg H_n\le3n+3.\ } \tag{4}
\]

H_n不是免费正多项式；其实际系数由同一adjugate确定。G_n degree7n压缩了完整矩结构，不是给未知H选择新参数。

Gauss核级数f(t)=Σ_(k≥0)χ_(−8)(k+1)t^k给实际primitive误差

\[
\ell_n=\frac{q_n}{d_n}\sum_{k\ge0}\chi_{-8}(k+1)\mathcal M'_n(k). \tag{5}
\]

符号来自M′=∫log(t)t^kU′。绝对交换由∫0¹(−log t)|U′|/(1−t)<∞支付；0端t^(3n)log可积，1端至少(1−t)^(3n)，n≥2。最初2n项为0。但χ有正负、H未知，不能把Mellin零点或有限项的符号当(5)整体非零证书。

## 4. 一项完全统一的解析gain，仍须同对象算术相乘

下面自含导一个不依赖n的解析常数。令ζ=e^(πi/4)、τ=i√8、α_a=ζ^(−a)，a=1,3,5,7，则沿253 f(t)=τ^(−1)Σχ(a)/(α_a−t)。置u_a=2α_a−1。选w_a为w+w^(−1)=2u_a中模>1的根，s_a=(w_a−w_a^(−1))/2≠0。u_a非实，所以根不在单位圆，选择唯一。令ρ=min|w_a|>1。

定义Chebyshev多项式T_k(cosθ)=cos(kθ)；其degree=k且在[−1,1]模≤1。几何级数直接给

\[
\frac1{\alpha_a-t}=\frac2{s_a}\left(1+
2\sum_{k\ge1}w_a^{-k}T_k(2t-1)\right),\quad0\le t\le1.
\]

证明只需把两个几何级数相加，使用1+2Σq^k T_k(x)=(1−q²)/(1−2qx+q²)，q=w_a^(-1)。截断到degree2n−1得到f的多项式近似f_(2n)，尾项满足

\[
\sup_{[0,1]}|f-f_{(2n)}|\le C\rho^{-2n},\quad
C=\frac4{|\tau|}\sum_a\frac1{|s_a|(1-|w_a|^{-1})}, \tag{6}
\]

C有限、正、完全与n无关。由(3)的log正交，实际(1)有

\[
\boxed{\ |\ell_n|\le C\rho^{-2n}V_n,\qquad
V_n=\frac{q_n}{d_n}\int_0^1(-\log t)|U'(t)|\,dt.\ } \tag{7}
\]

所以limsup n^(−1)log V_n<2logρ才由此自动得到统一趋零；实际ℓ非零仍另需证明。这里V_n包含真实q/d与同一选中向量，不是用另一函数的小界代替。普通正交可能进一步改善(6)，但没有在此免费领取。

## 5. 目前已认证的完整upper为何不能通过，及判断的精确边界

不需PNT或素数扫描即可给B_n的upper。其p赋值e_p的每个p^a项是floor(8x)+floor(5x)−floor(6x)−floor(7x)，两对和均13x，故该项在{−1,0,1}；p^a>8n时为0。因此max(0,e_p)≤floor(log_p(8n))，即B_n|d_(8n)。

另自含证明d_N≤4^N：令m=ceil(N/2)，d_N/d_m的每个非平凡p赋值恰为1，因为区间(m,N]最多含一份相邻p幂；其最大p幂项在binom(N,floor(N/2))的Legendre式贡献1，其他项非负。故d_N|d_m binom(N,floor(N/2))。中央二项式≤2^(N−1)（固定坐标的toggle把同一大小子集单射到其补类）。归纳N≥2给d_N≤2^(2N−2)≤4^N。由此B_n³≤2^(48n)，β_n≤2^(201n/4)。

253已认证的||U′||1≤24E_n⁴/β_n，E_n=2^(51n+8)，q_n≤Λ*_n、d_n≥1。把所有已付费用与(7)合在一起，得到当前的明确充分upper

\[
|\ell_n|\le \mathcal B_n:=
\frac{24C\Lambda_n^*E_n^4}{\beta_n}\rho^{-2n}. \tag{8}
\]

|u_a|≤3，|w_a|≤|u_a|+sqrt(|u_a|²+1)≤3+sqrt10<7，故ρ<7。Λ*≥1，加上β upper，**这个认证upper自身**满足

\[
\mathcal B_n\ge24C\,2^{32}
\left(\frac{2^{615/4}}{49}\right)^n\longrightarrow+\infty. \tag{9}
\]

因此(8)不能证明趋零。绝不能把(9)写成实际|ℓ_n|的lower：真实q/d、U′范数、signed cancellation可能远优于这些安全upper。它只是支付了同一完整模型当前证书的准入结算，未排除最优RV、其它向量或其它方法。

κ_n与B_n的真实约分收益、5n变号、Mellin压缩和统一Chebyshev gain均是可复用资产，但尚无证据把它们组合成严格净衰减，更未付(5)无界非零。按253停止条件，**本轮结算当前固定adj实现的默认投入；不因新增子引理自动延长参数、prime、第五列或地图优化。** 下一步应比较能同时支付实际非零与完整费用的新数值出口，保留本稿精确接口作重入依据。
