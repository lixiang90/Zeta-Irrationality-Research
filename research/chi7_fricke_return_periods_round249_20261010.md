# 第249轮：Fricke 商四个指定返回的完整周期常数

2026-10-10，A。实际 FULL 读 A248 final12413/a95eda…及独审收据后，本文在同一实际源上支付四个 order2 stabilizer、native 到达路径、完整 affine Eichler 常数及 exact odd 层。一个固定 exact Fraction 程序执行1次；无数值/素数/图/参数扫描。没有从四条指定到达叶推出所有到达叶永久不填，也没有新的数值定理。

## 1. 四个实际局部生成元与商分支点

沿用 A248 的 χ=χ−7、s=√2、K=Q(s)、t、y²=E(t)、A+=A₁+sA₂，I=R+(2s/7)D，B_g=A+(I−g)。固定 Wτ=−1/(14τ)，以及
\[
\gamma(a,b,d)=\begin{pmatrix}a&b\\14b&d\end{pmatrix},
\quad ad-14b^2=1,\quad
r=\gamma W=\begin{pmatrix}14b&-a\\14d&-14b\end{pmatrix}.
\tag{R1}
\]
r²=−14I，故在 PSL₂(R) order2，H 中固定点为
\[
\tau_r=b/d+i/(\sqrt{14}d),\qquad
j_r(\tau)=-i\sqrt{14}\chi(d)(d\tau-b),
\quad A_+(r\tau)=j_r(\tau)A_+(\tau).               \tag{R2}
\]
取以下四个确定输入，不搜索其它矩阵：
\[
\begin{array}{c|rrr|c|c|c}
 r&a&b&d&\tau_r&\chi(d)&\text{reduced form}\\ \hline
 r_0&1&0&1&i/\sqrt{14}&+1&(1,0,14)\\
 r_1&5&1&3&1/3+i/(3\sqrt{14})&-1&(3,2,5)\\
 r_2&5&-1&3&-1/3+i/(3\sqrt{14})&-1&(3,-2,5)\\
 r_3&25&4&9&4/9+i/(9\sqrt{14})&+1&(2,0,7)
\end{array}.                                      \tag{R3}
\]
固定点二元型为 (14d,−28b,a)，discriminant−56。JSON 保留逐次 integral translations/swap 的全部约化；上表四个 reduced points 均严格处于标准 SL₂(Z) fundamental domain 内部，互不等价。因此更不 Γ₀(14)-等价。这个区别不依赖实验 CM 数值。标准 domain 内部唯一性亦可直接证：非零 c 的 |cτ+d|>1，若两个内部点等价，正逆变换都严格降低 imaginary part，矛盾；c=0 只剩唯一整数 translation。

在固定点，j_r=χ(d)。A− 的 factor 为 −j_r，故 χ(d)=−1 的两点是 A+ simple zeros，即 Q+ 的两个 roots；χ(d)=+1 的两点是 A− simple zeros，即 Q− 的两个 roots。A248 已付四根互异与全部 ramification，故 (R3) 穷尽四个 stabilizer classes。

令
\[
r=\frac{7+4s-\sqrt{77+56s}}2,\quad R=1/r,
\quad \alpha=t(\tau_{r_1}),\quad\bar\alpha=t(\tau_{r_2}).
\]
两 α 正是 Q+ 的非实 roots，值由所给 native infinite product/路径明确固定；不额外猜其 radical imaginary sign。r₀ 对应小 root r，r₃ 对应大 root R。小 root 的实际路径在§4证明。

具体 native 到达可从 τ_b=iM（M 足够大）先水平到 Reτ_r+iM，再垂直到 τ_r；在 compact 路段对离散的其它 branch/zero/pole preimages 作小 detours，保持端点。R、D、A± 在整个 H 是实际单值全纯函数，故这些 detours 不改变端点或下面的 matrix-return identity。t-像下的局部半周返回从 τ_b 到 rτ_b，给以 r 为 stabilizer 的明确返回。四矩阵是四个局部 elliptic 类的生成元；不另声称它们单独生成整个 Γ₀(14)+W，两个 cusp/parabolic 返回仍须保留。

## 2. involution 支付全 affine 常数，不只固定点值

h=Θ²I 已付 weight3/χ 模性及 W factor；结合 (R1) 给 h(rτ)=j_r(τ)³h(τ)。两次链式微分因此表明
\[
P_r(\tau)=j_r(\tau)I(r\tau)-I(\tau),\quad P_r''=0.
\]
j_r(rτ)j_r(τ)=1，involution 给 j_rP_r(rτ)+P_r(τ)=0。对 affine polynomial 解这个2×2线性等式，其空间恰一维，basis 为 j_r−1。因此存在唯一实际常数 g_r，且对全部 H 有
\[
\boxed{I(r\tau)-g_r=j_r(\tau)^{-1}(I(\tau)-g_r),\quad
P_r=g_r(j_r-1).}                                  \tag{R4}
\]
这不是把未算 CM 值命名为常数：常数可以严格由一个 rational cusp 极限求出。置 τ=b/d+i/(14d²ε)，则 rτ=b/d+iε；τ→i∞ 时 I(τ)→0，|j_r(τ)|→∞。故
\[
\boxed{g_r=\lim_{\epsilon\downarrow0}
 I(e^{2\pi ib/d-2\pi\epsilon}).}                  \tag{R5}
\]
该到达恰为 radial，未偷用未付的 non-tangential finite part。对四个规定的 b/d，d 为1、3、3、9，均奇且与7互素。R 的 logistic denominator 在这些有限 phase classes 无零，允许 ∑m⁻² 支配；D 的 T(q^k) representation 同样有 bounded finite phases。故下节 Abel 极限严格成立。

## 3. 全闭式 period table 与一次固定 exact certificate

记 ζ_d=e^{2πi/d}、B₂(x)=x²−x+1/6，并将实参数取 fractional part。原 T 函数可写成
\[
T(z)=\frac{z+2z^2+z^3+2z^4+z^5}{1+z+\cdots+z^6}.
\]
在 z^d=1 的 finite group algebra，d=1、3、9 的唯一 reciprocal polynomial 分别为
\[
1,\qquad -1+z+z^2,\qquad 1+z^2-z^3-z^6+z^7.       \tag{R6}
\]
它们乘 denominator 后精确等于 numerator modulo z^d−1，包括 z=1 removable value1。令这些 rational coefficients 为 c_a=c_{d-a}。DLMF24.8.1 的完整 n=1 Fourier formula 与绝对收敛给
\[
\frac{C(\zeta_d^b)}{\pi^2}=\sum_{a=0}^{d-1}c_aB_2(\{ba/d\}),\quad
\frac{D(\zeta_d^b)}{\pi^2}
=\sum_a c_a[B_2(\{ba/d\})-\tfrac14B_2(\{2ba/d\})]. \tag{R7}
\]
没有把条件发散的 ∑χ(m) 当普通求和。

R 的逐项 real part 恰 Y/2。odd d 的精确 logistic polynomial 是
z/(1+z)≡1/2+∑_{a=1}^{d-1}(−1)^{a+1}z^a/2 modulo z^d−1。
Gauss sum Gχ=i√7：character orthogonality 给 |Gχ|²=7，χ 奇给 pure imaginary，有限 sine 和的正号决定 +i√7。由 χ(m)=Gχ⁻¹∑χ(a)e^{2πiam/7} 及同一 Fourier formula，得完整有限 rational expression
\[
\frac{\operatorname{Im}R(\zeta_d^b)}{\pi^2\sqrt7}
=-\frac17\sum_{j=1}^{d-1}\frac{(-1)^{j+1}}2
\sum_{a=1}^6\chi(a)B_2(\{a/7+bj/d\}).             \tag{R8}
\]
其 fixed finite sum 在 d=3,b=1 时内总和为 −4/21；d=9,b=4 时为 −44/63。程序用 exact Fraction 验证 (R6)–(R8)，矩阵 r²/character 和固定四个 form reductions，没有浮点或样本外推。d=3 的 R 虚部亦为 √3 L(2,χ₂₁)/2，是 same-parity π² 周期，并非新的数值目标。

结果是
\[
\begin{array}{c|c|c|c}
b/d&C/\pi^2&D/\pi^2&\operatorname{Im}R/(\pi^2\sqrt7)\\ \hline
0&1/6&1/8&0\\
1/3&-5/18&-5/24&4/147\\
-1/3&-5/18&-5/24&-4/147\\
4/9&67/162&25/72&44/441
\end{array}.
\]
例如 d9 的 doubled C 值43/162，故 D=(67−43/4)π²/162=25π²/72。完整返回常数最终为
\[
\boxed{\begin{aligned}
g_0&=Y/2+s\pi^2/28=g_+,\\
g_1&=Y/2-5s\pi^2/84+4i\sqrt7\pi^2/147,\\
g_2&=Y/2-5s\pi^2/84-4i\sqrt7\pi^2/147,\\
g_3&=Y/2+25s\pi^2/252+44i\sqrt7\pi^2/441.
\end{aligned}}                                    \tag{R9}
\]
这些常数支付 (R4) 的两个 affine coefficients，α_r=−i√14χ(d)d g_r、β_r=(+i√14χ(d)b−1)g_r；不是只支付端点值。

## 4. complete odd layer、native 小 root 与共轭叶

由 (R4)，实际 entire-return identity 为
\[
\boxed{B_g(r\tau)-B_g(\tau)=(g_r-g)(j_r(\tau)-1)A_+(\tau).} \tag{R10}
\]
取 disk local coordinate ζ=(τ−τ_r)/(τ−barτ_r)，rζ=−ζ，j_r=χ(d)(1+ζ)/(1−ζ)。权1 gauge 必保留：
\[
\widetilde A=A_+/(1-\zeta),\qquad
\widetilde A(-\zeta)=\chi(d)\widetilde A(\zeta).
\]
因此 B_g 的 exact odd part，而不只是 leading coefficient，为
\[
\boxed{\frac{B_g(\zeta)-B_g(-\zeta)}2
=\begin{cases}
-(g_r-g)\zeta\widetilde A(\zeta),&\chi(d)=+1,\\
 (g_r-g)\widetilde A(\zeta),&\chi(d)=-1.
\end{cases}}                                      \tag{R11}
\]
前者 ã(0)≠0，后者 ã 有 simple zero，均为非零 first odd coefficient iff g≠g_r。t−t(τ_r) 的 leading 是非零 ζ²；所以这一指定返回全纯补点 iff g=g_r。δB_g 同时补点。当 g=g+ 时，(R9)只有 r₀ 被消去，其它三个 native returns 具有明确非零 imaginary period，任何 real g 都不能消去它们。

小 Q− root 的 native 路径也可独立严格核定。τ=iy、y>1/√14 时，ImWτ=1/(14y)<y。任何 γ∈Γ₀(14) 的 d≠0，故 |cWτ+d|²≥d²≥1，ImγWτ≤ImWτ；不可能 γWτ=τ。因此正 q 路径在 τ*以前无 degree2 branch。t、f₁₄ 都正，native yquartic 从1连续且无零，使 Θt=f₁₄ yquartic>0。τ*必先到小 root r，不可能越过 r 到 R；四个 branch classes 不同，故 r₃ 到 R。由此 [0,r] 的实际 continuation 固定为该 native imag-axis 叶。

在假设 g=g+∈K 下，系数共轭 source 是
\[
\bar B=A_-(I_- -\bar g),\quad
I_-=R-(2s/7)D,\quad g_-=Y/2-s\pi^2/28.
\]
在 r₀ 的同一 ζ 坐标，A−/(1−ζ) 是 odd simple zero，并有 exact
\[
\boxed{\bar B_{\rm odd}=(g_--\bar g)\,A_-/(1-\zeta)\ne0.} \tag{R12}
\]
否则 g−bar g=sπ²/14 将使 π² algebraic。这个非零 square-root 来自原生叶，不假定未知周期可数域共轭。若另限定合法 φ 为 univalent，Koebe quarter theorem 在 |φ′(0)|>4r 时迫 image 包含直段[0,r]；实际 inverse path于是强制此native叶，而φ在内点无 ramification，不能把 (R12) 变为meromorphic。因此此限定模型的共轭图有 |φ′(0)|≤4r。该结论不适用于任意 multivalent maps，后者可保留偶 ramification。

## 5. 全叶范围与唯一未付接口

(R9)是四个规定 matrix returns 的 complete periods；(R10)–(R12)支付其完整 local functions。它不是“同一basepoint所有到达叶永久不填”的声明。例如 r₃ 的 reflected representative −4/9+i/(9√14) 是同一 Q− class，但 native periods 为相应复共轭；source 的 Γ affine transport必须保留。本文没有把四个矩阵仅有的 local data冒认为整个group无jump，也不从非零 odd part推出所有CDT地图遗漏这些points。

最强实质进展是明确区分：真实g+取消一个native return，另三个含已闭算的π² imaginary channel；它们不再是未知CM/Eichler常数。剩余准入应支付所选合法图强制哪些具体路径，及完整 Γ transported返回与另一数域嵌入的同对象预算。不能以只补W点启动素数/地图扫描，更不能把这个restricted return证书升级为数值无理性。

## 6. 实际来源、精确执行与冻结边界

本轮实际 FULL 读 research/chi7_fricke_quotient_source_round248_20261010.md，12413 B/SHA256 a95eda931df3fcf8042376b5a49d66bb60f8622f2772e3548178a176a853912b；并 FULL 读 B独审 research/research_round248_elliptic_quotient_review_20261010.md，当前完整7723 B/88cc45c474283714c6851735043ab69d265f2a72e0b5551e97e77900b6756cac（含后来追加的248报告范围节，非初始6230版）。这里只复用其实际 curve/PF/character，与A247身份，不重新认证历史归档。

新增官方 NIST DLMF24.8.1 的完整条件/公式选读，https://dlmf.nist.gov/24.8.E1；另实际核25.15(i)的L/Gauss定义，不声称阅读上游Apostol证明。Gauss sign、period algebra及矩阵均自含有限推导。来源HTML、规范化选段及准确读域在 literature/fricke_admission_sources_round249_20261010/alternative_reading_scope.md。

唯一数学运行：research/chi7_fricke_return_fixed_certificate_round249_20261010.py → 同名JSON，exit0、PASS。只核四个预先规定matrix/form与 d1/3/3/9 exact Bernoulli expressions；浮点、数值积分、外推、素数/参数/map扫描、旧producer复跑、Lean/git mutation均0。paper之外未执行其它数学。脚本/JSON及本文实际FULL保存复读后分别报告身份；主稿、scope与证书是本人独占NEW249文件，不改248/main/policy/manifest或同伴稿。
