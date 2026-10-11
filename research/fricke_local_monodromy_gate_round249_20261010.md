# 第249轮：Fricke 商源的局部返回与两实嵌入单叶门槛

2026-10-10，C。固定 A248 的同一坐标 t、同一 rank3 源及其 K=Q(√2) 系数共轭。本文支付二阶方程的有限有理证书、四有限点的收敛局部型、全部无穷远返回叶的非零 log²，及两个单叶图导数乘积≤16。数学执行0。该结论关闭当前两地方单叶基本入口，不排除多叶图、不同整数模型或其它周期源；没有新数值无理性定理。

## 1. 固定实际对象与有限有理系数

实际 FULL 读 research/chi7_fricke_quotient_source_round248_20261010.md，六节 Q1–Q18，12413 B，SHA256 a95eda931df3fcf8042376b5a49d66bb60f8622f2772e3548178a176a853912b。以下从其已付 eta divisor、全函数 Fricke/Eichler 身份推导，不把作者所读 primary 范围冒成本人 FULL。

置 s=√2、ε∈{+1,−1}，
\[
a_\epsilon=3+2\epsilon s,\quad
Q_\epsilon=1-(7-4\epsilon s)t+t^2,\quad
E=Q_+Q_-,\quad y^2=E,\quad y(0)=1,\quad\delta=t\partial_t .
\]
并取 Aε=A₁+εsA₂、Iε=R+ε(2s/7)D、
\[
g_\epsilon=Y/2+\epsilon s\pi^2/28,\qquad
B_{\epsilon,c}=A_\epsilon(I_\epsilon-c).
\]
这里 Y=L(2,χ−7)。系数共轭是 B_{+,g}↦B_{−,\bar g}，不能将未知 \bar g 换成指定数值 g−。

为使系数完全可复核，记
\[
Q_A=3t^2-5t+3,\ Q_0=t^2-t+1,\ T=t^3-8t^2-8t+1,\quad
u=\frac{T+(t-1)y}{98t^2},\quad P(u)=1+13u+49u^2,
\]
\[
d=\frac{Q_A-y}{2y},\quad
k_\epsilon=1+\epsilon s\,\frac{2Q_0}{Q_A-y},\quad
\ell_\epsilon=\delta k_\epsilon/k_\epsilon,\quad
V(u)=\frac{2u(1+16u+49u^2)}{P(u)^2}.
\]
所有 δ 运算使用 δy=tE′/(2y)。对 K(t,y) 中的式子定义
\(\operatorname{tr}_0 H=(H(t,y)+H(t,-y))/2\)，随后用 y²=E 化简。这是两次有界有理运算，非待猜的递推。实际方程为
\[
\mathcal L_\epsilon=\delta^2+p_{1,\epsilon}\delta+p_{0,\epsilon},
\quad p_{1,\epsilon}=\frac12\delta\log(Q_{-\epsilon}/Q_\epsilon),
\]
\[
p_{0,\epsilon}=\operatorname{tr}_0\!
 \left[-d^2V+(\delta d/d)\ell_\epsilon+\ell_\epsilon^2-\delta\ell_\epsilon\right].
                                                        \tag{M1}
\]
独立推导：δA₁=dδuA₁，所以
δ²A₁=(δd/d)δA₁+d²VA₁；乘实际 gauge kε 后一次系数为 −δd/d−2ℓε，零次系数恰(M1)。两个实际齐次解为 Aε、τAε，其 δ-Wronskian 为 aεQε/(2πiy)，给显示的一次系数。Γ₀(14) 与 Fricke 的常矩阵返回先使唯一 monic operator 在 y↦−y 下固定，故取 trace 保留原方程；没有用 trace 强行改变 operator。

普通导数形式因此精确为
\[
t^{-2}\mathcal L_\epsilon=\partial_t^2+
 \left[\frac1t+\frac12\left(\frac{Q_{-\epsilon}'}{Q_{-\epsilon}}
                         -\frac{Q_\epsilon'}{Q_\epsilon}\right)\right]\partial_t
 +\frac{p_{0,\epsilon}}{t^2}.                            \tag{M2}
\]
forcing 同样有有限 rational certificate。令
\[
Z=\frac{8t^3P(u)^2}{u^2(Q_A-y)^3},\quad
\mathcal H_\epsilon=1+8u-8Z(1+8ut)
+\epsilon\frac{2s}{7}\left[-7-\frac8{7u}+Z\left(7+\frac8{7ut}\right)\right].
\]
则对每个常数 c，
\[
\mathcal L_\epsilon B_{\epsilon,c}=\mathcal R_\epsilon,\qquad
\mathcal R_\epsilon=\operatorname{tr}_0
 \frac{u(Q_A-y)(Q_A-y+2\epsilon sQ_0)}{4P(u)E}\mathcal H_\epsilon\in K(t).
                                                        \tag{M3}
\]
乘积微分中 δI 交叉项由 p₁=δlogG₀−2δlogAε 消去，G₀=Θlogt=f₁₄y/t，故 RHS=Aεhε/G₀²。实际模变换使它先 invariant 再取 trace。c 不改变 forcing。

## 2. 全部有限点、四处指数及收敛 analytic particular

商映射 X₀(14)→P¹_t 的全部临界值恰 E 的四简单根。f₁₄ 在 H 无零，Aε 的 H 零点恰 Qε 两根的曲线前像。因此在 t≠0,∞、E(t)≠0 的任何小盘，Aε、τAε 的 Wronskian 非零，原模驱动也全纯；(M1)–(M3) 中 u、P(u) 或 gauge 的表面分母全部相消。**有限 operator/forcing 的可能极点仅为 0 及 E 四根**，不能从未展开的分母多领 apparent points。

在 E 的一个根 t_e，取曲线参数 z，t−t_e=z²、τ=τ_e+c₁z+O(z²)，c₁≠0。

- 若 Qε(t_e)=0，Aε 有简单 z 零点。Aε 与 (τ−τ_e)Aε 的最低阶为 z、z²，所以齐次指数为 (1/2,1)。在(M2)中一次系数 residue −1/2、零次 double-pole coefficient 1/2。
- 若 Q−ε(t_e)=0，Aε 非零，齐次解最低阶为 1、z，所以指数为 (0,1/2)。一次系数 residue +1/2、零次 double-pole coefficient 0。

这是实际两解给出的局部指数，不是只由 formal indicial roots 推没有 log。两指数差均非整数，局部返回是 involution；齐次非亚纯通道恰一维。

在 fixed-point stabilizer 的实际局部 trivialization 中，hε 与 Aε³ 有相同 weight/character multiplier。自己 Qε 的点，Aε 的 fixed multiplier 为 −1，故 hε 至少也有一个 z 零点；另一 Q 的点 hε 有界。G₀ 有简单 z 零点。由 RHS=Aεhε/G₀² 得
\[
\mathcal R_\epsilon\text{ 在自己 Q 点全纯；在另一 Q 点至多 simple pole}. \tag{M4}
\]

由上述有限阶、native O(t) 和 ∞ bounded（Aε、hε、G₀ 的 cusp weights 为1、3、2，乘除后恰抵消），Q−ε𝓡ε 是 degree≤2 的 polynomial 且 constant0。因此还能将(M3)完全化为
\[
\boxed{\mathcal R_\epsilon(t)=
\frac{t[11+9\epsilon s-8(1+\epsilon s)t]}{7Q_{-\epsilon}(t)}.} \tag{M3a}
\]
其有限两头独立纸核如下：hR=q−3q²、hD=q+4q²，Aε=(1+εs)+2q+O(q²)、G₀=1−4q+O(q²)，故 Aεhε/G₀² 的 q、q² 系数分别是 (11+9εs)/7、(97+63εs)/7。q=t+4t²+O(t³) 将第二项变为 (141+99εs)/7；乘 Q−ε 后 numerator 第二项为 −8(1+εs)/7。这是已付 degree bound 内的完整身份，未用有限头猜未知函数。特别 𝓡ε(∞)=−8(1+εs)/7≠0。

给出收敛 particular 的自含补丁。令 h=t−t_e，将(M2)乘 h²写为
\[
h^2v''+a(h)hv'+b(h)v=c(h),
\]
a,b,c analytic。自己 Q 点 c=O(h²)，取 v=Σ_{k≥2}v_kh^k；indicial I(k)=(k−1/2)(k−1)，对 k≥2 非零。另一 Q 点 c=O(h)，取 v=Σ_{k≥1}v_kh^k；I(k)=k(k−1/2)，对 k≥1 非零。系数递推
\[
I(k)v_k=c_k-\sum_{j=1}^{k}
 [a_j(k-j)+b_j]v_{k-j}
\]
中低阶未定义 v 均取0。若 |a_j|+|b_j|+|c_j|≤MR^{-j}，且 |I(k)|≥c_0k²（k充分大），取 B>R^{-1}，卷积被
MCB^k(k+1)Σ_{j≥1}(BR)^{-j} 控制。除以 c₀k² 后对大 k 小于 CB^k/2，forcing 同样被余下半份控制；有限个 k 增大 C、B 即可。故此递推收敛，支付 analytic particular，而非形式级数。

因此每个实际 B 分支在四点都是
\[
\text{analytic germ}+\kappa_e h^{1/2}\text{analytic germ}.       \tag{M5}
\]
补点条件是完整半整数通道 κ_e=0；局部 analytic particular 与 analytic homogeneous 通道不产生额外 log。对自己 Q 点，native κ_e 的首项正比 Iε(τ_e)−c；若它为0，唯一 fractional channel 全部消失。另一 Q 点须核完整 local jump coefficient，不能仅用普通点值为零代替。

在 t=0、∞，齐次两解经对应 cusp 的模参数写成 analytic q_c germ 与该 germ乘 logq_c 的常矩阵组合；t 在每个相应 cusp 是 simple zero/pole。因此两点齐次指数均为(0,0)，至多一级 log。四有限指数并不强制任意合法拉回同时恢复 Aε 或 y：下面 native B_{−,g−} 在 r 全 analytic 而 A− 有 sqrt，就是同一实际源的例子。没有以“局部 order2”冒称全部返回叶都非平凡或全球有限 monodromy。

## 3. 无穷远每个返回叶的非零 log²

采用 A248 Q15 的完整 cusp1/2 展开（L(3,χ−7)>0 由其绝对收敛 Euler product）：
\[
R\sim-\frac7{8a}L(3,\chi),\quad D\to\pi^2/8,\quad
A_1,A_2\sim\frac{\pi}{\sqrt7\,a},\quad q=-e^{-a},\quad a\downarrow0.
\]
于是每个固定 c∈C 都有
\[
B_{\epsilon,c}\sim-\frac{7\pi(1+\epsilon s)}{8\sqrt7}
 L(3,\chi)a^{-2}\ne0.                                  \tag{M6}
\]
该 cusp 的 t 是 simple pole，logt 为非零常数乘 a⁻¹加有界项；故这正是非零 log² 层，不是 Laurent pole。

由于 forcing 是单值 rational，任意 continuation 后的 B 与原 B 之差都是同一二阶方程的 homogeneous solution。第2节已付 ∞ homogeneous 至多 log；所以 **每个 transported ∞ leaf 的非零 log² 系数相同，均不能由更换 c 或加齐次解消掉**。围绕 ∞ 的返回在任何这类叶上都非恒等：log² 的差有非零 log 项。这一量词来自同一 rational inhomogeneous equation，不是从一个径向叶推所有 finite leaves。

## 4. 共轭 native r 点的准确非补支证书

令
\[
r=\frac{7+4s-\sqrt{77+56s}}2\in(0,1).
\]
Q− 的根为 r、1/r；Q+ 的系数 7−4s 在(−2,2)，所以其两根模长1。全部有限非零奇点均在 |t|≤1/r。

τ₀=i/√14 为 W₁₄ fixed point。全 Fricke 身份在此给
\[
A_-(\tau_0)=-A_-(\tau_0),\qquad
I_-(\tau_0)-g_-=-[I_-(\tau_0)-g_-],
\]
所以 A−(τ₀)=0、I−(τ₀)=g−。从 native imaginary axis 的 eta product，
\[
0<t(\tau_0)=q\prod_{j\ge1}
 \frac{(1+q^{7j})^4}{(1+q^j)^4}<q<1
\]
（0<q<1），故 t(τ₀) 必为 r。还须确认这就是 native 正实返叶：整个 imaginary ray Imτ≥1/√14 上都有 0<t<1，故可能的临界值只剩 r。r 在 X₀(14) 上有唯一曲线前像，其 H 提升均为 γτ₀，γ∈Γ₀(14)。若 c=14k，则
\[
\operatorname{Im}(\gamma\tau_0)=
\frac{1/\sqrt{14}}{d^2+14k^2}\le1/\sqrt{14};
\]
分母不能0，且为正整数。因此该 ray 在到达 τ₀ 前没有临界点，native t 从0单调到r（其初始导数为正）。A− 在该点 simple zero；B_{−,g−} 由 Fricke 全函数身份 invariant，因此在商坐标 r 处 analytic。

假设目标 g+=g∈K。实际共轭源是
\[
\overline{B_{+,g}}=B_{-,\bar g}
=B_{-,g_-}-\Delta A_-,\qquad \Delta=\bar g-g_- .          \tag{M7}
\]
若 Δ=0，则 π²=(14/s)(g−\bar g) 为代数数，矛盾。因此 Δ≠0，而 A− 的 sqrt 首项非零，故 **共轭 native branch 在 r 有非零 sqrt**。这只证明这一真实返叶，未把 \bar g 设成 g−，也没有通过假设任意域自同构作用于未知周期来论证。

## 5. 两地方单叶导数 cap 与当前基本入口

设 φ±:(D,0)→(C,0) holomorphic、univalent，且分别使完整三行
(1,B_{+,g},δB_{+,g}) 与其系数共轭 meromorphic。置 c±=|φ±′(0)|。使用标准 Koebe quarter theorem：φ±(D) 包含 |t|<c±/4；其 inverse 单值且无 ramification。

(M7)的 native sqrt 已足够给
\[
c_-\le4r.                                               \tag{M8}
\]
否则像内含 0 到 r 的线段及 r 邻域，meromorphic pullback 经 inverse 会给实际 native B 在 r meromorphic，矛盾。

另一方面若 c+>4/r，选择 1/r<R<c+/4。盘 |t|<R 包含 0 和 E 的全部四点，且整个圆 |t|=R 在 φ+(D) 内。meromorphic pullback经inverse给同一 B 在该盘单值 meromorphic，外圆返回因而为恒等。该圆环绕全部有限 operator/forcing 奇点，等价于反向 ∞ loop；第3节证明每个可能到达的 ∞ 叶都有非恒等 log² 返回，矛盾。因此
\[
c_+\le4/r,\qquad c_+c_-\le16,\qquad
\lambda:=\frac12(\log c_++\log c_-)\le\log4.              \tag{M9}
\]
这里没有先假定任意 Ω 含某点就所有叶奇异：减号仅用 inverse 固定的 native 路径，加号使用全 finite loop 与已付的全 ∞ 叶证书。

同一三行源的已付 7b d_N² full-prefix type 是 **两个列均为(0,1,1)**，不是一个宽度2的列。row sums (0,2,2)，CDT基本τ为
\[
\tau=\frac{1\cdot0+3\cdot2+5\cdot2}{3^2}=\frac{16}{9}.
\]
固定 7b 不改领先费用。两嵌入的当前基本正分母关要求 λ>τ；而 log4<3/2<16/9：严格凸函数1/x的梯形上界给 log2<3/4。因此这个必要关已经失败，毋须图或素数扫描。本人实际读了已存固定 v2 的完整物理16–20页 Theorems2.5.1/2.7.1，以及当前版完整物理144页 Remark8.2.42 的数域延伸 statement；本段只比较当前基本数组的必要正分母，没有宣称重证全部更强数域判据。

这一结论不证明 g+∉K。CDT 允许非单叶图；它可以通过有限点 even ramification，且没有全局 inverse，故(M8)–(M9)不能搬过去。更优实际联合整型、更强 filtered/multiplace 判据或另一完整 source 也未被排除。局部固定空间依然很大，所有 finite leaves 非补支或 Abel lift 的量词均未支付。当前唯一具体关闭的是 **同 t、同 rank3、当前完整两列型、两个实嵌入都 univalent 的基本入口**。

## 6. 读域、执行账与保存边界

完整个人读域及全部 SHA 在 literature/fricke_admission_sources_round249_20261010/dual_reading_scope.md。本轮新增数学为(M2)、(M4)–(M9)的同对象局部/全∞量词与两单叶必要界；(M1)/(M3)独立纸推 A248 已给的 finite rational certificate，未重命名为新的坐标/source。没有重新审旧 Fourier/Bernoulli seeds，也没有新 primary GET。

数学程序/CAS/数值/prime/parameter/map/Lean 执行0；文件读取、hash与写本文不是数学运行。外 Git mutation0；旧稿/peer/Root/main/manifest/policy写0。只写本文与本人NEW scope，写前核两目标均不存在。最终保存后实际 FULL 作者自读并向 Root 报 bytes/SHA；作者自读不等于独立 PASS。

