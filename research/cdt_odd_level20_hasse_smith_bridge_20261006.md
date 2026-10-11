# Hasse packet 到一变量评价高度：换格抵消与固定原格的 Smith 余量

日期：2026-10-06。本稿是对 [Hasse 适配稿 §§4–5](cdt_odd_level20_hasse_20261006.md) 的独立只读审阅及一个限定桥梁。它不修改根稿、不修改冻结预算、不宣布新的 τ 或数值无理性定理。下面给出局部线性代数证明、实际 closed 系统的线性 leading-order 覆盖，以及两张固定原格的一变量完整高度账。level20 调用仍待根任务独审这些接口；balanced tensor 情形尚未建立。

原始依据是 [CDT 固定 v2](../literature/cdt2024_l2_chi_minus3.pdf)：PDF94–97页的 degree、局部 norm、primitive filtration 与 slopes inequality，PDF99–102页的源格 (7.3.6)、评价过滤及粗非arch估计 (7.3.10)。本稿已直接核读这些页。

## 1. 根 Hasse 稿的最终审核

§4 的完整前缀 packet 与 §5 的格指数、CRT 论证通过本次独立审核。

对好素数 p、任一 𝔭∣p，令 k=O_K/𝔭。若 p<N<p²，H、ϑH、ϑ²H 在前 N 项经 p³ 清除后均 𝔭-integral。根稿的有限截断 F_{p,±} 是 p-integral，式

\[
p^3H_\pm(t)=A_\pm(t)F_{p,\pm}(t^p)
\pmod{\mathfrak p,t^{p^2}}
\]

使用整数双向 q↔t 坐标、两种 divisor sums 的精确 χ₅(p) 因子；它没有对含 p-denominator 的整个 Eichler 芽作 reduction。ϑF(t^p)=0，故两条 polynomial syzygies 真正取消全部前缀的最高层，而非仅 p+1 一项。所得 gain 仅是一层 valuation，不能写成三层同时取消。

核逆像 Λ⊂E 的指数等于 Norm(𝔭)^{rank M} 是一般 DVR 线性代数：E/Λ 识别为模 𝔭 映射的像。好素数在 K=Q(√5) 中未分歧，所以 pO_{K,𝔭}=𝔭O_{K,𝔭}；根稿用 p² 与 p³ 表示 valuation 层合法。有限多个素理想的条件经 CRT 定义真实 O_K 子格，指数相乘。无需选择有利 split primes。

根稿的 denominator D_{p,±}(0) 非零：N_±(0)=C_±(0)=1，P_p(0)=1 又保证其 radical 不在0处消失。故 §5 用 D_p² 作为形式单位分母的 rational numerator 次数界也成立。

## 2. 直接换格确实精确抵消

以下按一个好素理想的 DVR R_𝔭 证明；q=Norm(𝔭)。设 E 是秩 R 的源格，V^n 是由特征零 Taylor vanishing order 定义的完整旗标。取

\[
E^n=E\cap V^n,\qquad
\Lambda^n=\Lambda\cap V^n,
\]

其中 Λ⊂E 为有限指数子格。每个非零 graded quotient 的秩是1；交于 rational subspace 的过滤是 saturated，所以各 quotient 在 DVR 上自由。自然映射 gr_n Λ→gr_n E 是单射。写

\[
a_n=\operatorname{length}_{R_{\mathfrak p}}
      (\operatorname{gr}_n E/\operatorname{gr}_n\Lambda).
\]

过滤的 determinant additivity 给

\[
\sum_n a_n=\operatorname{length}_{R_{\mathfrak p}}(E/\Lambda)=r.
\tag{1}
\]

保持原 archimedean metric，换格引起 normalized degree 的局部变化为 −r log q。对原文真正使用的 quotient norm，leading evaluation 的局部高度则逐级变化

\[
h_{\mathfrak p}^{\Lambda}(\psi^n)
 =h_{\mathfrak p}^{E}(\psi^n)-a_n\log q.
\tag{2}
\]

于是 slopes inequality 的 RHS−LHS 变化为

\[
-\sum_na_n\log q+r\log q=0.
\tag{3}
\]

各 archimedean rational subspace 及其 quotient norm 没有变化。CRT 只把这些有限地方的等式相加。因此，仅将根稿 Λ 的 index 记成评价高度的下降，并漏掉源格 degree 的下降，必然制造虚假的净收益。相反方向的有限指数 enlargement 也服从同一记账恒等式。

一个两维例子使区别明确：在原源格 E=Z_p² 上，两个 leading coefficients 为 p⁻³、p⁻²。实际高度和为5log p，而共用 p³ 清除给出的粗上界为6log p。取 Λ=pZ_p⊕Z_p，评价高度和降成4log p，源 degree 同时下降 log p；真正的 slopes gap 仍是5log p。余量 log p 已经存在于原格，它不是换格产生的收益。

## 3. 保持原格不变的 Smith 缺秩引理

设 E_𝔭 是秩 R 的原源格，ψ 为特征零的 injective formal evaluation。令 V_D 为它的全部 leading orders，假定选定前缀 N 满足

\[
\max V_D<N.\tag{4}
\]

进一步假定 Ψ=p³eval_{<N} 在 E_𝔭 上 integral，且它的 reduction 的秩为 r。保持 E_𝔭 与所有原 metric 不变，则

\[
\boxed{\sum_{n\in V_D}h_{\mathfrak p}(\psi^n)
 \le\{3R-(R-r)\}\log q.}\tag{5}
\]

证明：primitive complete Taylor filtration 允许选择 E_𝔭 的 adapted integral basis e₁,…,e_R。令对应 leading orders 为 n₁<⋯<n_R。以这 R 个 jets 为行，以 e_j 为列，Ψ 的 R×R 子矩阵下三角，且其非零对角项为 p³c_j，其中 c_j 是 ψ^n 在原 rank1 graded unit generator 上的值。

这是真正的原 source quotient norm：adapted basis 的变换属于 GL_R(R_𝔭)，保持 unit ball。矩阵 reduction 的秩不超过 r，故 Smith normal form 保证至少 R−r 个 invariant factors 被 p 整除。因此

\[
3R+\sum_jv_{\mathfrak p}(c_j)
 =v_{\mathfrak p}(\det\Psi_{\{n_j\}})\ge R-r.
\]

而 h_𝔭(ψ^{n_j})=−v_𝔭(c_j)log q，得到(5)。矩阵因其非零 leading diagonal 在特征零下可逆；有限 N 的覆盖条件(4)是不可省略的输入。原 source lattice 没有改变，故这里不会出现(3)的换格抵消。

这个引理识别原文 ultrametric triangle estimate 未记录的 aggregate slack；它不是宣称每个 leading order 都改进一层，更不是将几个 mod p 关系当成新的特征零函数。

## 4. 一个明确的一变量 source prototype

先完全去掉 balanced tensors。使用 rank4 四元组

\[
1,\quad \Delta^2H,\quad \Delta^2\vartheta H,
\quad \Delta^2\vartheta^2H.\tag{6}
\]

固定 Δ² 清掉根几何稿已列出的 finite branch poles；它的整数系数、常数项1保持全前缀 LCM³ 型。三个 target highest packets 同乘 Δ²，故根 Hasse 稿的两条 syzygies v₀、v₁ 原样作用于(6)，不增加其次数 δ_p。这里没有把 ϑ^j(Δ²H) 与 Δ²ϑ^jH 混用。

调用 CDT(7.3.6) 的三个 unit columns，均从第一个 target 行开启；u_h=1、y_h=1、e=0。令 L_D=lcm(1,…,D)。原 coefficient lattice 在乘 t^D 转换 Laurent sections 后为

\[
E_D=L_D^{-3}O_K[t]_{\le D}
       \ \oplus\ O_K[t]_{\le D}^{\oplus3}.\tag{7}
\]

这一步须携带原 O(D) arch metric，不能把普通 polynomial coefficient norm 擅作替代。其 rank 是 R=4(D+1)。源格及其 Hilbert–Samuel degree 全程保持为原 CDT 的(7)；没有引入 Λ 作为新源格。

假定一个线性 cutoff

\[
N_D=4(D+1)+O(1)\quad\text{覆盖全部 }V_D.\tag{8}
\]

对 √N_D<p≤D，L_D 在 p 的 valuation 恰为1。故 Ψ_D=p³eval_{<N_D} 的 constant source block 及三个 target blocks 的前 N_D 项均 integral。原(7.3.10)对这些 p 给每个 leading grade 的粗上界3log q。

若 D≥δ_p，两条 syzygies 乘次数≤D−δ_p 的 polynomials，在原 E_D reduction 中给

\[
s_{p,D}=2(D-\delta_p+1)\tag{9}
\]

个独立 kernel directions；constant block 取0。这些方向的独立性由第二 syzygy 的第三 target 坐标非零直接证明。因此(5)在**原粗上界**之上给至少 s_{p,D}log q 的严格 aggregate improvement。全部较小 primes、剩余 valuation 层、未适配 primes 均继续用原 CDT 的上界，不作免费扣除。

## 5. 明确的正主项，以及它所依赖的条件

由 δ_p≤(3p+9)/2，可保守取

\[
G_D=\sum_{\substack{p>\sqrt{N_D}\\p\text{ good}}}
       (2D-3p-7)_+\log p.\tag{10}
\]

positive 的整数项自动满足 D≥δ_p：p 为奇数，使该整数为偶数，positive 时至少为2。possible zero endpoint 不需要构造任何方向。若(8)成立，PNT与 partial summation 给下式，其中 θ(x)=Σ_{p≤x}log p 是 Chebyshev 函数：

\[
\begin{aligned}
G_D
&=2D\,\theta(2D/3)
 -3\sum_{p\le2D/3}p\log p+o(D^2)\\
&=\left(\frac23+o(1)\right)D^2.\tag{11}
\end{aligned}
\]

常数7、有限坏 primes、以及去掉 p≤√N_D 的损失都是 o(D²)。数域 degree 归一化后仍是同一值：对好 p，Σ_{𝔭∣p}f_𝔭=[K:Q]，且所有 𝔭 上有同一 δ_p 上界。

这是一个条件明确的候选正项：它应从**固定原 source**的累计 finite evaluation height 上界中扣除。它不来自 Λ 的 covolume，不需要在 archimedean 端构造 p-dependent global polynomial basis。因此显式 CRT representatives 的系数高度不会被暗中忽略；根本没有用这些 representatives 改动原 source 或其 arch metric。

不过，不能仅见(11)就宣布新 holonomy theorem。至少须完成根任务独审：

1. 对(6)的实际 closed rank4 系统，精确调用 Shidlovsky order lemma，证明(8)的 N_D 覆盖全部 primitive leading flag；有限 p² jet 检查不能替代它。
2. 确认 quotient metrics、乘 t^D 的 target identification 与 CDT(7.2.12)–(7.3.10)完全一致；本文的局部 adapted basis 本身不是改变 metric。
3. 按 prime 分开原 finite-height estimate。只有 √N_D<p≤D 且原 bound 确为3log q 的区域扣除(10)；所有其它区域保持原 bounds。坏 primes 与小 primes 的总量须在同一渐近中仍为 o(D²)。
4. 在同一共同 cover 上使用清pole后的实际函数，完成各 embedding 的 archimedean height 与 normalized degree 记账。圆盘径向缩小可以处理 fixed-function boundary growth，但不能改其 source metric。

在这四项获得独立确认之前，本稿只给桥梁与必要条件，不替换旧报告的 τ。即便一变量桥梁完成，balanced d-variable tensor 的 source types、species 配额、leading jets 与 primitive saturation 仍须另证明；一变量的(11)不能自动代入 Theorem8.0.1 的 τ-double。

下面 §§7–9 补上第1项的实际系统和第3–4项的完整渐近账本。它们继续使用固定原格；根任务的独立确认与高维 tensor 扩展仍是不同工作。

## 6. 结论范围

根 Hasse §§4–5 的原论证通过最终审核。直接换格的 index gain 精确抵消；但固定原格的模素数缺秩提供了比逐项 LCM triangle bound 更强的 aggregate Smith 信息。本文给出其局部 determinant 证明，以及在明确 source prototype 和线性 N 覆盖假设下的正主项(11)。

没有证明新的 ζ/L 数值结论，没有建立新的全局 τ 公式，也没有排除所有 adapted lattices 或所有 holonomy metrics。下一步应核完整 primitive leading flag 与全局 tensor 兼容性，随后才评估同一真实解析 cover 上是否产生足够的最终收益。

## 7. 全部 leading orders 的线性覆盖

### 7.1 实际 rank4 的封闭导数矩阵

记 g=Δ²，并令 g_j=gϑ^jH，j=0,1,2。完整模型给出最小非齐次方程

\[
H'''+a_2H''+a_1H'+a_0H=U,
\qquad a_i,U\in K(t),\quad U\ne0.
\tag{12}
\]

rank3 商不可约及非分裂性给实际四个函数 1,g₀,g₁,g₂ 在 K(t) 上独立。这里使用实际函数，不使用三个额外 homogeneous monodromy solutions 来增加 rank。逐项微分得

\[
\begin{aligned}
1'&=0,\\
g_0'&=(g'/g)g_0+g_1/t,\\
g_1'&=(g'/g)g_1+g_2/t,\\
g_2'&=gt^2U-t^2a_0g_0
 +\frac{ta_2-t^2a_1-2}{t}g_1
 +\left(\frac{g'}g+\frac{3-ta_2}{t}\right)g_2.
\end{aligned}
\tag{13}
\]

所以这些实际函数本身构成一个固定 4×4 K(t) first-order closed 系统。乘 g 只是一个固定 rational gauge，保持实际 rank 与封闭性；g(0)=1，所有函数仍是原点的 formal power series。

CDT Theorem3.2.8（PDF52页）正是需要的 Shidlovsky order lemma：对 derivation-closed、实际 rank=m 的固定系统，degree<D 的 polynomial evaluation 的全部 leading jumps 都 ≤mD+C，且恰有 mD 个。对本稿 degree≤D 改用 D+1，取整后可选固定 C₄≥0，使

\[
\boxed{\max V_D\le4(D+1)+C_4,
\quad\#V_D=4(D+1),
\quad N_D=4(D+1)+C_4+1.}
\tag{14}
\]

乘 t^D 后的 polynomial evaluation 与原 Laurent-section evaluation 有完全相同的 graded index n；原 target generator 是 t^{n−D}，乘 t^D 后是 t^n。故(14)覆盖的是本稿实际使用的全部 primitive leading flag，不只是某种选出的 Padé basis。原 source 的非零 rational scalar factors不改变特征零的空间或 leading orders。

CDT 将定理写成 Q(t) 形式，但所引用 Shidlovsky lemma 是特征零的解析微分方程结论；例如 [Fischler 的一般版本，§1、§3](https://arxiv.org/pdf/1609.09770) 明确以 A∈M_m(C(t)) 和 complex polynomial coefficients 表述。这里无须 restriction of scalars 增秩：K(t)-独立也给 C(t)-独立。否则将一个 C(t) 关系清成有限 degree polynomial 关系；其系数矩阵的所有 entries在 K 中，rank 在域扩张 K⊂C 后不变，于是同一有限系统已有非零 K 系数 kernel，矛盾。对(13)按任一 embedding调用同一个特征零 lemma即可；两 embedding仅可能改变一个固定常数，取最大值不改变斜率4。

### 7.2 有效常数的范围

原文含有效 multiplicity estimate：Theorem3.2.10 对一个已验证 Fuchsian first-order system，给

\[
C\le(\#S-2)\binom m2+mh,
\tag{15}
\]

其中 S 是该矩阵的 pole set，h 由该系统在这些 singular points 的最小 exponent 的负数之和定义。Theorem3.2.8 后的说明还列出一般系统的 Bertrand–Beukers、Bertrand–Chirskii–Yebbou 有效方法。

本稿只需要存在固定 C₄，不需要它的数值。但不能把 regular-singular differential module 与某个 displayed matrix 只有 simple poles 混为一谈：由(13)直接数其 poles，再把未核验的 exponents 代进(15)，不能得到已证明的数值 C₄。若要对有限 D 输出实际 cutoff，应先给一个合法 Fuchsian gauge 和该 gauge 的局部 exponent 数据，或真正执行一般有效方法。有限 p=7,11,13 的 jet checks 不能替代(14)，也不能确定 C₄。

### 7.3 包含背景的实际 rank7

取实际七元组

\[
1,L,T_2,K_2,g_0,g_1,g_2,
\quad L=-\log(1-t),\quad T_2=L^2/2.
\tag{16}
\]

背景部分的 exact closure 为

\[
L'=\frac1{1-t},\quad
T_2'=\frac L{1-t},\quad
K_2'=\frac{K_2}{2(1-t)}+\frac L{t(1-t)}.
\tag{17}
\]

四个背景实际 rank4 及 trivial/sign composition factors由 [真实 tensor-helper 稿 §§2–3](cdt_odd_tensor_helpers_20261005.md) 给出；target 的 rank3 商为不可约 Sym² 模块，故两个实际闭包交于公共 constant line，得到实际 rank7。它不是将两个完整 ODE solution bases 拼成七个函数。使用(13)、(17)给一个固定 7×7 K(t) closed system，因此同理有固定 C₇≥0：

\[
\boxed{\max V_D\le7(D+1)+C_7,
\quad\#V_D=7(D+1),
\quad N_D=7(D+1)+C_7+1.}
\tag{18}
\]

更一般地，只要追加背景的实际闭包与 target 的 intersection 已被证明，实际 rank=m 的 closed tuple 都有 m(D+1)+O(1) 的同类覆盖。不能凭单纯列出 m 个 germ 假定这一前提。

## 8. bare rank4：全部 graded 高度及最终一变量不等式

用两个 embedding 的合法共同解析叶，记

\[
\bar\rho=\frac1{[K:\mathbf Q]}
  \sum_{\sigma:K\hookrightarrow\mathbf C}
       \log|\varphi_\sigma'(0)|,
\qquad
\bar J=\frac1{[K:\mathbf Q]}
  \sum_\sigma\iint_{\mathbf T^2}
       \log|\varphi_\sigma(z)-\varphi_\sigma(w)|\,dz\,dw.
\tag{19}
\]

可先将每个 map 缩到一个严格较小圆盘，应用 CDT 的 archimedean metric 和 fixed-function growth estimate，再在合法时取径向极限。本稿不把 coefficient sup norm 替换原 O(1)_φ metric。下面的 bars 总是 normalized field averages。

### 8.1 每个 graded 的原始 nonarch 上界

对好 p>√N_D，由 unit-row source(7)，原 CDT(7.3.10)的三个 unit LCM columns直接给

\[
\frac{h_{\mathfrak p}(\psi_D^{(n)})}{\log\operatorname{Norm}\mathfrak p}
\le
\begin{cases}
3,&p\le D,\\
3,&D<p\le n,\\
0,&p>\max\{D,n\}.
\end{cases}
\quad(n\in V_D).
\tag{20}
\]

这些只是统一上界，不断言所有 graded 实际具有此 valuation。它们允许某些真实高度为负。对 √N_D<p≤D 再用(5)、(9)，得到更强的总和

\[
\sum_{n\in V_D}h_{\mathfrak p}(\psi_D^{(n)})
\le[3R-s_{p,D}]\log\operatorname{Norm}\mathfrak p
\quad(D\ge\delta_p),\qquad R=4(D+1).
\tag{21}
\]

对 D<p≤N_D，因为 V_D⊂{0,…,N_D−1}，有

\[
\#(V_D\cap[p,N_D))\le N_D-p;
\tag{22}
\]

这给原高度和上界3(N_D−p)log Norm(𝔭)。对 p>N_D，所有本稿列出的 source scalars 及 target jets 都 integral，所以好素数贡献的上界为0。

剩下 p≤√N_D 的 higher prime powers仍按原完整 LCM³ 型记账。每个 graded 在一个此类 p 的高度上界为 O(log N_D)，故总量至多 O(D√D log D)=o(D²)。有限多个坏素数用相同 LCM valuation及 fixed rational normalization处理，总计 O(D log D)=o(D²)。本稿不从这些地方扣除免费收益。

### 8.2 normalized D² 常数

记 θ(x)=Σ_{p≤x}log p。先不使用 Smith gain，(20)–(22)给

\[
\begin{aligned}
\sum_{n\in V_D}h_{\mathrm{fin}}(\psi_D^{(n)})
&\le3R\theta(D)
 +3\sum_{D<p\le N_D}(N_D-p)\log p+o(D^2)\\
&=\left(12+\frac{27}2+o(1)\right)D^2
 =\left(\frac{51}2+o(1)\right)D^2.
\end{aligned}
\tag{23}
\]

归一化数域 places 后值相同，因为对每个好 p 的所有 𝔭 有 Σf_𝔭=[K:Q]。扣除真正固定原格的(11)，而非换格 index，得到

\[
\boxed{\sum_{n\in V_D}h_{\mathrm{fin}}(\psi_D^{(n)})
\le\left(\frac{149}6+o(1)\right)D^2.}
\tag{24}
\]

Shidlovsky覆盖及 #V_D=R给

\[
\sum_{n\in V_D}n=\frac{R(R-1)}2+O(D)=8D^2+O(D).
\tag{25}
\]

这对两种符号的 ρ 都有效：不是仅用 Σn≥R(R−1)/2 后乘一个可能为负的数。CDT(7.3.9)及其 normalized field版本给

\[
\sum_{n\in V_D}h_\infty(\psi_D^{(n)})
\le(-8\bar\rho+4\bar J)D^2+o(D^2).
\tag{26}
\]

原 source 的 Hilbert–Samuel degree由 CDT(7.3.7)，m=4、Σu_hy_h=3，给

\[
\widehat\deg E_D=(2\bar J+3)D^2+o(D^2).
\tag{27}
\]

因此若原 primitive quotient metrics、field slopes inequality、共同合法 map 的接口被独立确认，将(24)、(26)、(27)放入同一个 slopes inequality得到

\[
2\bar J+3\le-8\bar\rho+4\bar J+\frac{149}6,
\quad\text{即}\quad
\boxed{4\bar\rho-\bar J\le\frac{131}{12}.}
\tag{28}
\]

这是具体的一变量固定原格 candidate inequality，显示 G_D 怎样作用于最终账本；它不命名新的 τ-double，也不替换已冻结表。原粗账给4ρ−J≤45/4，而(28)的 RHS低1/3。其几何收益仍不足：同一 map 的 Jensen floor给 J_σ≥ρ_σ，故若要矛盾至少需

\[
\bar\rho>\frac{131}{36}>\log16.
\tag{29}
\]

真实叶的 genuine cusp1与原点唯一 preimage 条件给ρ_σ≤log16。因此这一个 bare rank4 candidate本身不能得到 L(3,χ₅)的新数值结论，即使全部一变量接口都通过。

## 9. rank7 固定背景：同类全账及其限制

仍只取(16)，其合法 unit-column types为σ=(0,1,2,2,3,3,3)、e=0，u=y=(1,2,4)。乘 t^D 后原源格具体为

\[
\frac{O_K[t]_{\le D}}{L_DL_{2D}L_{4D}}
\oplus\frac{O_K[t]_{\le D}}{L_{2D}L_{4D}}
\oplus\left(\frac{O_K[t]_{\le D}}{L_{4D}}\right)^{\!\oplus2}
\oplus O_K[t]_{\le D}^{\oplus3}.
\tag{30}
\]

此处 L、T₂、K₂ 的分母均含在已证明的完整 types中。共同 map 还须对背景的实际函数合法；full G target cover 并不自动清除任意新增 helper 的所有分支，调用(30)必须保留这一检查。

对 p>√N_D，每个 graded 的安全上界是

\[
\frac{h_{\mathfrak p}(\psi_D^{(n)})}{\log\operatorname{Norm}\mathfrak p}
\le\sum_{a\in\{1,2,4\}}\mathbf1_{p\le\max\{n,aD\}}.
\tag{31}
\]

对 √N_D<p≤D 所有列已经开启，原粗 bound仍是3log Norm(𝔭)，而 target-only syzygy directions仍给至少(9)的 kernel。增加背景没有使这两条 relation成为新的独立函数，也没有改变δ_p；故至少可扣除同一 G_D=(2/3+o(1))D²。其余 primes保留(31)。

由N_D=7D+O(1)，原 finite-height主常数是

\[
\sum_{a\in\{1,2,4\}}\int_0^7\max(s,a)\,ds
 =\frac{3\cdot49+1^2+2^2+4^2}{2}=84.
\tag{32}
\]

于是该固定原格的一变量账为

\[
\begin{aligned}
\widehat\deg E_D
 &=\left(\frac72\bar J+21\right)D^2+o(D^2),\\
\sum h_\infty&\le\left(-\frac{49}2\bar\rho+7\bar J\right)D^2+o(D^2),\\
\sum h_{\rm fin}&\le\left(\frac{250}3+o(1)\right)D^2.
\end{aligned}
\tag{33}
\]

以同样限定接口应用 slopes inequality，candidate结论为

\[
\boxed{7\bar\rho-\bar J\le\frac{374}{21}.}
\tag{34}
\]

即使共同背景 map合法，由Jensen floor也至少需ρ>187/63才能造成矛盾；187/63>log16，所以这一固定背景表的一变量 gain仍不足。此结论没有对其他真实 helpers、fractional列、balanced tensors、更强的算术 Smith 信息或 multi-map heights作全族排除。

## 10. 本轮独立核验与冻结边界

low_period_closure 已独立审核 §§3–5 的原格 Smith lemma、syzygy kernel维数、归一化2/3主项，并独立重算 bare rank4 的149/6、131/12及 Jensen gate。其反馈也独立确认 actual closed rank4可调用 Shidlovsky3.2.8。本文 §§7–9 写出的矩阵、rank7 source和常数仍提交根任务独审。

没有重跑或修改根 Hasse producer，也没有修改已冻结 arithmetic、tensor-helper或 convexity稿。本稿是单独的数学 bridge报告；局部有限脚本的通过不能代替上述全部证明，也不意味着目标常数无理性已被证明。
