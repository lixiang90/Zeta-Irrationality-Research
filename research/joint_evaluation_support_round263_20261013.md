# 第263轮：真实 AP support、Frobenius 联合行及其准确 degree 门槛

2026-10-13。固定普通 `s` 坐标、实际 `V={1,J,θ_sJ}`、两指定目标 `ζ(2)±2G` 的完整反证类 `b=0,c=±d≠0`。本轮不用有限头、素数扫描、CAS、参数或地图实验；只写本稿。没有新数值无理性定理，没有把标量 prefix cap 当作实际评价分母下界。

**本轮有一项可以改变联合评价格的真实机制：**实际 elliptic period 的 all-prime Lucas 身份给一个 degree 恰为 `4p`、随素数变化的 polynomial Frobenius 行。它能消去完整最高 `p⁻²` packet；不能由固定 `Q(s)` 不可约性否定，也不能免费塞进 degree 小于 `4p` 的 source。

同时，首个 AP block 的逐 coefficient 平方分母 support 被精确化；一个全素数递推证明 native support 无12个连续空洞。它不证明每个系数都有 `p²` 分母，也不排除散布的正密度零。真正 joint finite credit 仍需短 jet 窗口、第二层与同一 source/metric 的预算桥。

## S1. 真实最高 packet 的全 range 公式

沿第261轮的整数归一化，写

$$
J=A(A_c+S),\qquad S=C C_3+D_\chi B_4,
\quad C=\pm D_\chi,\quad D_\chi\ne0,
$$

`A∈1+3s+s²Z[[s]]`、`q(s),s(q)` 是双向整数 unit-linear composition；`θ_s=s∂_s`。为区分素数类与函数 `r=1−2s`，以下用 `ρ∈{1,5,7,11} mod12` 标素数类。令

$$
T_\rho(\ell)=C[q^\ell]C_3+D_\chi\chi_{-4}(\rho)[q^\ell]B_4.
$$

除固定有限坏素数（包括关系系数与首项7的因子），其首个非零下标为

$$
k_\rho=1\quad\text{或}\quad3,
$$

各有两个类；`C=Dχ` 时 `χ−4(ρ)=+1` 的两类在1存活，另一两类在3存活，另一符号交换它们。`Tρ(1)=C+Dχχ−4(ρ)`，延迟类的 `Tρ(3)=7Dχχ−4(ρ)/9`。

对每个好素数 `p≥5`，`p≡ρ mod12`，全部 `q` 系数下标小于 `p²` 时只含至多一次 `p`。第261轮的完整 divisor identity 因而给

$$
p^2S(q)\equiv\sum_{\ell=1}^{p-1}\overline{T_\rho(\ell)}q^{\ell p}
\pmod{(p,q^{p^2})}.
\tag{1}
$$

`ℓ<p` 保证这些有理系数 `p` 整。定义真正拉回的有限芽

$$
Z_{\rho,p}(z)=\sum_{\ell=1}^{p-1}\overline{T_\rho(\ell)}q(z)^\ell
\pmod {z^p}\in\mathbb F_p[z]/(z^p).
$$

它的 order 恰为 `kρ`。整数 composition 的 Frobenius 身份 `q(s)^p≡q(s^p)` 给

$$
\boxed{p^2J(s)\equiv A(s)Z_{\rho,p}(s^p),\qquad
p^2\theta_sJ(s)\equiv\theta_sA(s)Z_{\rho,p}(s^p)
\pmod{(p,s^{p^2})}.}
\tag{2}
$$

常数 `A_c` 在乘 `p²` 后消失。这里是整个 range 的公式，不只一个 prime head；`N≥p²` 时必须另计高幂，不能把(2)越界使用。

首个 block `n=kρp+u`、`0≤u<p` 因而满足

$$
p^2J_{k_\rho p+u}\equiv T_\rho(k_\rho)A_u,
\qquad
p^2(\theta_sJ)_{k_\rho p+u}\equiv uT_\rho(k_\rho)A_u\pmod p.
\tag{3}
$$

原行该 range 的赋值至少 `−2`，所以 `1≤u<p` 的两行平方分母 support **恰好相同**，由 `A_u≠0 modp` 决定。`u=0` 的 `J` 有最高平方层，`θJ` 因 index 含 `p` 少一层。不能把 derivative 行当成有独立支持的另一份收益。

## S2. 本 period 的真实 Lucas 身份：不是移借 Legendre 源

实际 `t=x₆` 的 period 满足

$$
\mathcal L_tA=0,\qquad
\mathcal L_t=p(t)\partial_t^2+p'(t)\partial_t+3(-1+3t),
\quad p(t)=t(1-t)(1-9t).
$$

写 `A(t)=Σ a_n t^n`，得到

$$
(n+1)^2a_{n+1}=(10n^2+10n+3)a_n-9n^2a_{n-1},
\quad a_0=1,\ a_1=3.
\tag{4}
$$

这正是 Zagier 原文的 **Sequence C**；它与本项目 weight1 函数 `A` 的名字不同，不能按字母错配。该原件§4给

$$
a_n=\sum_{k=0}^n\binom nk^2\binom{2k}k
=\sum_{i+j+k=n}\binom n{i,j,k}^{\!2}
=\operatorname{CT}_{x,y}P(x,y)^n,
$$

$$
P=(1+x+y)(1+x^{-1}+y^{-1}).
\tag{5}
$$

第二等号是按一项计数合并，最后等号直接展开两个 multinomial。以下 Lucas 证明为本稿自含推导：若 `n=n₀+pn₁`、`0≤n₀<p`，则

$$
P^{n_0+pn_1}\equiv P^{n_0}P(x^p,y^p)^{n_1}\pmod p.
$$

`P^{n₀}` 的每个单变量 exponent 都在 `[−n₀,n₀]⊂(−p,p)`；能与第二因子的 `p` 倍 exponents 合成常数的项，只能是第一因子的真正常数项。因此

$$
a_{n_0+pn_1}\equiv a_{n_0}a_{n_1}\pmod p.
$$

迭代即得全 digit Lucas；令

$$
F_p(t)=\sum_{n=0}^{p-1}\bar a_n t^n,
$$

则对每个素数

$$
\boxed{A(t)\equiv F_p(t)A(t^p)\pmod p.}
\tag{6}
$$

这是本具体 `A(t)` 的恒等式，未用其他椭圆族的 Hasse polynomial 代替它。

## S3. degree 恰4p、平方自由的真实 Frobenius polynomial

令

$$
\nu(s)=s-3s^2+4s^3-2s^4=\frac{1-(1-2s)^4}{8},
\qquad\Delta(s)=1+\nu(s)=\frac{9-(1-2s)^4}{8}.
$$

第259轮的完整 rational identity 正是 `t(s)=ν(s)/Δ(s)`。它不只是有限 Taylor 匹配。由(6)和整数系数 Frobenius，定义

$$
P_p(s)=\sum_{n=0}^{p-1}\bar a_n\nu(s)^n\Delta(s)^{p-1-n},
\qquad\mathscr H_p(s)=\Delta(s)P_p(s).
\tag{7}
$$

因为 `Δ(s)^p=Δ(s^p)`，得到

$$
\boxed{A(s)\equiv\mathscr H_p(s)
\left(\frac{A(s)}{\Delta(s)}\right)^p\pmod p,\qquad
\frac{\theta_sA}{A}\equiv\frac{\theta_s\mathscr H_p}{\mathscr H_p}.}
\tag{8}
$$

其 degree 不仅有 `≤4p` 的安全界，还可精确确定。

首先，`binom(p−1,k)²≡1`，并且 `k>(p−1)/2` 时 `binom(2k,k)≡0`。用 `binom(2k,k)≡(−4)^k binom((p−1)/2,k)` 得

$$
\bar a_{p-1}=\sum_{k=0}^{p-1}\binom{2k}k
\equiv(-3)^{(p-1)/2}=\chi_{-3}(p)\ne0.
\tag{9}
$$

所以 `deg F_p=p−1`。从(6)及 characteristic `p` 中 `∂_tA(t^p)=0`，又有 `L_tF_p=0`。在 `t=1/9,1`，`p(t)` 的根简单；若 `F_p` 在此有 multiplicity `1≤m<p`，最低项系数是 `p′(t₀)m²`，非零，矛盾。在 ordinary root 若 multiplicity `2≤m<p`，最低项系数 `p(t₀)m(m−1)` 非零，亦矛盾。`F_p(0)=1`。因此 `F_p` 平方自由，且不在两个有限非零 cusp 消失。

`ν′(s)=(1−2s)³`，故拉回只有 finite critical point `s=1/2→t=1/9`；无穷远映到 `t=1`。两点都不是 `F_p` 的零，故 `P_p` 的全部根简单。它在 `Δ=0` 处等于非零 `a_{p−1}ν^{p−1}`；且 `F_p(1)≠0` 保证

$$
\deg P_p=4(p-1).
$$

`Δ` 平方自由（在其唯一 derivative 零点 `s=1/2` 的值为 `9/8≠0`），且与 `P_p` 互素。由 `H_p(0)=1`，每个 `H_p` 根又都不为0。因此对每个 `p≥5`

$$
\boxed{\deg\mathscr H_p=4p,\quad\mathscr H_p(0)=1,\quad
\gcd(\mathscr H_p,\theta_s\mathscr H_p)=1.}
\tag{10}
$$

不能借 primitive gcd 把这份 rational logarithmic derivative 的最小 polynomial pair degree 降到 `p` 或 `2p`。

## S4. 首块不是“全系数都有p²”：可证 support 范围

由(8)，令

$$
\Psi_{\rho,p}(z)=\overline{A(z)/\Delta(z)}\,Z_{\rho,p}(z)\pmod {z^p},
\qquad\operatorname{ord}\Psi_{\rho,p}=k_\rho.
$$

(2)强化为

$$
p^2J(s)\equiv\mathscr H_p(s)\Psi_{\rho,p}(s^p)
\pmod{(p,s^{p^2})}.
\tag{11}
$$

若 `H_{p,j}` 表示 `H_p` 系数、`ψ_{ρ,p,j}` 表示 `Ψ` 系数，对 `n=ap+u<p²`、`0≤u<p`，

$$
\boxed{p^2J_{ap+u}\equiv
\sum_{j=0}^{4}H_{p,jp+u}\psi_{\rho,p,a-j}\pmod p,}
\tag{12}
$$

越界系数记0；`u>0` 时 `j=4` 项本来为0。θ行再乘 `u`。它把全部 block 的 actual support 接到至多五份有限 Hasse coefficient strings，未只保留首项。

但 Hasse polynomial 的**根平方自由**不表示它的**系数逐个非零**。首块依然由 `A_u=H_{p,u}`、`u<p` 决定；没有理由把两个性质混同。

有一个不靠扫描的 support 下界。把 period ODE 拉回并清分母，原系数有共同因子 `r⁶`（`r=1−2s`），在原点为unit可除。使用 `1−8ν=r⁴`、`ν′=r³`、`ν″=−6r²`，primitive polynomial coefficients可取

$$
a(s)=\Delta^2\nu r,
$$
$$
b(s)=\Delta(1-10\nu-2\nu^2),
$$
$$
c(s)=3(2\nu-1)r^3,
\qquad aA''+bA'+cA=0.
\tag{13}
$$

共同因子约去时的中间括号严格为 `r⁶[(1−16ν−8ν²)+6ν(1+ν)]=r⁶(1−10ν−2ν²)`。直接按 factored coefficients 核算：`deg(a,b,c)=(13,12,7)`、`a₁=b₀=1`、`a₁₃=b₁₂=16`。因此其 coefficient recurrence 的最前项为 `(n+1)²A_{n+1}`，最后项为 `16(n−11)²A_{n−11}`，中间只涉及该12步区间。

若 `A_j,…,A_{j+11}` 全为0 mod `p`，其中 `1≤j≤p−12`，当 `j≥2` 时取 recurrence 的 `n=j+10`，非零尾系数迫 `A_{j−1}=0`。可逐步反向直至包含 `A₁=3` 的零块，矛盾；`j=1` 本来就矛盾。所以

$$
\boxed{\text{每个 }p\ge5,\quad A_1,\ldots,A_{p-1}
\text{ 中没有12个连续零；}
\quad\#\{1\le u<p:A_u\ne0\}\ge\lfloor(p-1)/12\rfloor.}
\tag{14}
$$

在(3)的首个真实 AP block，两行的最高平方 support 因而有同样的正密度下界。它排除长度 `Θ(p)` 的连续空洞；**仍未排除散布的正比例零点，没有证明每个 interior coefficient 都有平方分母。** 单行 support 密度也不证明高维 joint coefficient product 或 evaluation determinant 的费用下界/节省。

## S5. 真正随尺度变化的联合行：能杀全部最高层，但必须付 degree

从(8)与(2)，真正 polynomial row

$$
\boxed{(-\theta_s\mathscr H_p)J+\mathscr H_p\theta_sJ}
\tag{15}
$$

在全部 cutoff `N<p²` 的 ordinary coefficients 上，乘 `p²` 后模 `p` 恒为0。原因是 derivative 不作用于 `Ψ(s^p)`，所以这个 row 杀掉(11)的完整 packet。其剩余分母至多一层 `p`；没有因此领取第二层全部消失。

这确实超出第262轮固定有理换基审查：operator 随 `p` 变，degree 恰为 `4p`；characteristic zero 的 rank2 不可约性并不禁止 characteristic `p` 的 rational logarithmic derivative。

而(10)保证，在 Hasse 最高层模型中，任意 polynomial pair `U,V` 若要求 full formal polynomial syzygy，必满足

$$
\mathscr H_p U+(\theta_s\mathscr H_p)V=0.
$$

其所有解恰为

$$
U=-(\theta_s\mathscr H_p)W,\qquad V=\mathscr H_pW.
\tag{16}
$$

非零 pair 的最小 max degree 为 `4p`。所以这个模型不能在 source degree `D<4p` 时通过换 gcd 免费产生 full polynomial syzygy。真实 `p²J` 的 congruence始终只在 `N<p²` 的 range使用；有限截断可能有额外 kernel，须按下一节的 jet 条件判断，不能从 full syzygy degree 否定所有短 jet 消去。

## S6. 全 jet 到 source index：已闭安全窗口与精确剩余矩阵

取完整 source

$$
L_D=\mathbb Z_p[s]_{\le D}^{\,3},\qquad
F=R+UJ+V\theta_sJ,
$$

保留全部 coefficients `0,…,N`，并假设 `N<p²`。最高平方 residue map 的 kernel 由(11)及原点 unit 给出准确等价

$$
\boxed{p^2[F]_{0,\ldots,N}\equiv0\pmod p
\iff\mathscr H_pU+(\theta_s\mathscr H_p)V
\equiv0\pmod {s^{N-k_\rho p+1}}.}
\tag{17}
$$

`N<kρp` 时整个最高层尚未进入，右端条件按空串处理。常数 polynomial 行 `R` 完全自由。

如果

$$
N\ge k_\rho p+D+4p,
\tag{18}
$$

右侧 polynomial 的 degree至多 `D+4p`，有限 jet 条件就是(16)的全 polynomial 条件。于是 pair kernel dimension 与 residue rank 精确为

$$
\boxed{\dim\ker=(D-4p+1)_+,\qquad
\rho_{p,D,N}=2(D+1)-(D-4p+1)_+.}
\tag{19}
$$

对 `N≈3D`，一个两类统一且有真实 syzygy 的完整宏观窗口为

$$
\boxed{\sqrt N<p\le D/4.}
\tag{20}
$$

其上 `N<p²`，且(18)对 `kρ=1,3` 都成立。在边界固定取整只影响 `O(1)`；小素数的全部幂必须继续保留旧完整账本。

令 `Λ_high` 是(17)的 source-preimage lattice，完整 quotient 的 rank正是(19)，所以

$$
\boxed{[L_D:\Lambda_{\rm high}]=p^{\rho_{p,D,N}}
=p^{D+4p+1}\quad\text{在(20)中。}}
\tag{21}
$$

这是一项真实 joint highest-layer index，不能只称“存在消去行”而忽略 source 代价。相对把两非恒定 polynomial blocks 全部当作独立最高层方向的粗 cap，kernel 的 weighted raw saving 是

$$
\sum_{\sqrt N<p\le D/4}(D-4p+1)\log p
=\left(\frac18+o(1)\right)D^2
\quad(N\sim3D).
\tag{22}
$$

该 leading 用普通 PNT 与 partial summation；不是有限 prime gcd 拟合。它表示本 source 的第一 residue 层确有宏观秩降低，不是已经获得 `δ=1/8` 的 holonomy 减费，更不是最终全分母的准确指数。

对未覆盖的短 jet 窗口，必须研究具体矩阵

$$
(U,V)\longmapsto
[\mathscr H_pU+(\theta_s\mathscr H_p)V]_{0,\ldots,N-k_\rho p}
\tag{23}
$$

的真实 rank/Smith，而非声称它 generic 满秩。短 jet 可能有全 syzygy以外的 Padé kernel；本稿没有求其全素数统一 rank。`N≥p²` 的高幂、(15)剩余一层的 p-adic lift，以及其后的 source index/archimedean metric 也均未付。

## S7. 方向判断：真实机制已准入首证书，但未证明足够净收益

本轮付清了一个上轮尚未具体化的机制：在**本实际 period、同坐标、所有好素数**上，完整 highest-layer 可由 sharp-degree `4p` 的 Frobenius 行消去；第一安全窗口的完整 index与 kernel dimension 有闭式。这改变了“只有 prefix cap”时的研究对象，值得在当前宏观检查中与其它实际载体比较。

但不能立即开矩阵或 prime扫描，也不能将(22)贴成 `τ`。下一项决定性证书必须把(17)–(23)接到同一 complete evaluation/leading coefficient：要么证明短 jet 全宏观窗口与第二层带来足够内容，要么证明一个准确 source-index与 metric桥使已付秩降低产生净收益。实际目标仍要求所选 BC 费用 `τ_eff<(2/3)log3<20/27`；沿第262轮更细 prefix-cap下界 `8/9` 的预算，必要额外净 credit大于 `4/27`。

安全窗口(22)只是 `D²/8` 的 raw 第一层收益，当前没有这个 source 的已证换算定理。若以后一个匹配 theorem采用常见 `2/m²` 的 leading归一化，本项对 `m=3` 的条件性对照只有 `1/36`，小于 `4/27`；这不是可以从另一个 level20 source 直接继承的定理，也不排除其它短 jet窗口和联合层机制给更多收益。必须先完成同对象账本，不能因发现Hasse行自动无限续轮。

## S8. 依据和阅读边界

实际读本对象[第259轮完整 field](source_selection_mixed_field_round259_20261010.md)及[第261轮算术稿](refined_budget_arithmetic_round261_20261010.md)的相关完整公式；复读[第262轮结算](research_next_route_progress_round262_20261012.md)。CDT固定 v2 的物理159–163页选段确认本 `A,t,L_t,B,C` 规范；Zagier 原件已存的物理5–6页表与§4明确 Sequence C 的 `(10,9,3)` 和 binomial identity；本稿没有阅读全文15页或重新证明全部模参数表。

原文载体：[CDT选段](../literature/refined_budget_round261_20261010/arithmetic_cdt_v2_physical159_163.txt)、[Zagier5–12页既存提取](../literature/source_admission_round258_20261010/cdt_zagier2009_pdf05_12.txt)。本轮使用后者的表与§4，不能将整个8页提取登记为本轮全部已读。常数项 Lucas、平方自由/degree、拉回 support recurrence、finite jet kernel及 sourceindex均为本稿纸面推导。

主代理已实际全文独立核对本稿 S1–S8，逐式确认 native constant-term/Lucas、Hasse 平方自由与 exact degree4p、primitive ODE 的12连零排除，以及有限 jet/kernel/sourceindex 的条件与边界。本次收到的复核限于这份数学稿；不继承主代理的网页、PDF 或其它文献阅读标签，也不把该书面复核称为 Lean 认证。

没有新网络检索、数学程序、CAS、有限 n 或 prime执行、地图/参数扫描、Lean、旧producer或Git写入；未更改任何历史文件。成果是实际 support 与 joint 第一层的全尺度证书，目标仍未完成。
