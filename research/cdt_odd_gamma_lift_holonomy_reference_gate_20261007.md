# 真实 inverse-L 周期提升的完整函数秩与对数参考族 holonomy 门槛

2026-10-07，作者 /root。本稿为唯一 NEW 纸面推导；基线 delivery_balanced_gamma_direction SHA b3a9c11266257168b103c14a13541b503dc53df1d7ad56c327c8ea83a5c43d50，588 冻结记录只读。本轮没有执行/import/rerun旧或同行数学producer、guard、prime表，也未建立数学producer。以下是实际 inverse-L lift 的后续计算，不重新命名原 paired source ξ=αζ(4)+βζ(5)。本稿不宣称新数值无理性或Lean验证。

## 1. 新候选确实越过了上一轮的 Taylor/完整填洞接口

保留 [Gamma实际模型](cdt_odd_gamma_connection_projection_20261007.md) G1–G19：

\[
 L=D^9-\Lambda t\prod_{i=1}^9(D+a_i),\quad D=t\partial_t,
 \quad\Lambda=2^{10}5^5,
 \quad a=(1/2^{\times5},1/5,2/5,3/5,4/5),
\]
\[
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}\in\mathbb Z,
 \quad f_0=\sum_{n\ge0}h_nt^n,
 \quad c=1/\Lambda.
 \tag{H1}
\]

原齐次系统在 C(t) 上不可约，且 c 为指数0,…,7,7/2的反射点；ψ=Δ_cf0≠0。本轮 source 新 [dual/relative extension稿](cdt_odd_gamma_dual_relation_extension_20261007.md) 的实际构造如下，本文保留全部归一化，独立推其后续 rank/leaf 条件。

\[
 N=380928,\qquad A=-2^{20},\qquad \mu=1/A=-2^{-20},
\]
\[
 P(X)=5532X^4-5600X^3+2275X^2-425X+30,
 \quad r_5(t)=-N^{-1}P(D)\frac{At}{1-At}.
 \tag{H2}
\]

规范解 B5(0)=0 的精确系数为

\[
 B_5(t)=\sum_{n\ge1}h_n\!\left\{
 -\frac1N\sum_{m=1}^n\frac{P(m)A^m}{m^9h_m}\right\}t^n,
 \qquad LB_5=r_5.
 \tag{H3}
\]

这不是 ηj 的有理变基。因为 |A|<Λ，原 Au v4 Example X 的已证 ζ5 级数恰给

\[
 -\frac1N\sum_{m\ge1}\frac{P(m)A^m}{m^9h_m}=\zeta(5).
 \tag{H4}
\]

用尾和得 (ζ5 f0−B5) 的 Taylor radius 至少 |μ|，而 |μ|>c；故是完整函数 germ 身份

\[
 \Delta_cB_5=\zeta(5)\psi,\qquad
 F_u:=B_5-u f_0,\quad
 \Delta_cF_u=(\zeta(5)-u)\psi.
 \tag{H5}
\]

当 u=ζ5∈Q 的假设成立，F_u 有 Q[[t]] 起点且在这一实际 c 分支 holomorphic。这个同时成立的接口是本轮新增进展；H4 本身只是已知 ζ5 的级数评价，不是它的新无理性证明。整体 filled leaf 的所有 transported c 分支另受 μ 的九维齐次跳跃制约，本文不把一个填洞 disk 当作全部 Riemann leaf。

## 2. 同一 Taylor 整模型可由 D5n 改进到 Dn

**H6（全部有限处的 ratio cap）。** 令 Dn=lcm(1,…,n)。对所有 1≤m≤n，

\[
 D_n^9\frac{h_n}{m^9h_m}\in\mathbb Z.
 \tag{H6}
\]

证明逐 prime p 与 q=p^k。h_v 的第 q 层 factorial valuation 为

\[
 C_q(v)=5\lfloor2v/q\rfloor+\lfloor5v/q\rfloor
 -15\lfloor v/q\rfloor
 =5\lfloor2\{v/q\}\rfloor+\lfloor5\{v/q\}\rfloor\in[0,9].
\]

若 q≤n 且 q|m，C_q(m)=0，该层 C_q(n)−C_q(m)−9≥−9；若 q∤m，该层 C_q(n)−C_q(m)≥−9。若 q>n≥m，两者的 floor(v/q)=0，C_q(v)=5floor(2v/q)+floor(5v/q) 对v单调，所以该层非负，且 q不整除m。于是总亏损不超过9floor(log_p n)，正是 Dn9 所清的量。不能把 m9 与同层 carries 的两个 worst cases重复相加；也不能将 h_n/h_m 未经证明当作整数。

P(m)、A^m 整，故

\[
 ND_n^9[t^n]B_5\in\mathbb Z.
 \tag{H7}
\]

对固定 u∈Q，设 d 为其分母，则 Nd Dn9 [t^n]F_u 整，包含 n0常数−u。所有 D^jF_u 只把正指标系数乘 n^j；同一个 Nd Dn9 cap 因此覆盖全部 j≥0。H6–H7 是 safe upper，不证明最小公共分母率为9，也不移植原 paired q 的39.6875费用。

## 3. μ 的不可去对数与任何 admissible map 的共同参考函数

**H8（每一分支都有实际 y4 logy）。** μ 是 L 的 ordinary point，因为 μ≠0,c。令 y=t−μ。L 的最高普通导数系数为

\[
 a_9(t)=(1-\Lambda t)t^9,\quad a_9(\mu)\ne0.
\]

At/(1−At)=−1−μ/y，P 的 degree 准确为4，故 r5 的 pole 准确为5，leading coefficient

\[
 r_5(t)=\frac{24\cdot5532\mu^5}{N}y^{-5}+O(y^{-4}).
 \tag{H8}
\]

九次普通求导的准确身份为 ∂y9(y4logy)=24² y−5。由 ordinary-point variation of constants，任何 particular 的第一个不可去 log 项于是为

\[
 F_u(t)=\lambda_\mu y^4\log y+
 \{\text{analytic terms and higher }y\text{-order log terms}\},
 \quad
 \lambda_\mu=\frac{5532}{24N(1-\Lambda\mu)\mu^4}\ne0.
 \tag{H9}
\]

可直接把有理 forcing 与 ordinary homogeneous analytic fundamental matrix 代入逐次积分；pole≤5在第九次积分后仅产生y4及更高阶的log，没有低于y4的log或negative Laurent项。不同分支之差、以及−u f0，都是 μ 邻域的 holomorphic homogeneous solution，不能改变λμ。特别 χμ:=ΔμF_u=2πiλμ y4+O(y5) 是非零 L-solution，与u无关。没有把它的九个普通点 connection constants视为已求值。

若实际 holomorphic φ:(D,0)→(C,0) 使 F_u∘φ 的指定起点 germ 延拓成meromorphic函数，则 φ 必须 omit μ。否则在φ(z0)=μ的有限order h处，H9变成非零(z−z0)4h·hlog(z−z0)，仍非meromorphic。任意分支也不能避开此障碍。

因此沿每个这样的 φ，参考函数

\[
 \ell(t)=\log(1-At),\qquad\ell(0)=0,
 \tag{H10}
\]

的pullback都有全盘holomorphic lift，因为1−Aφ在单连通盘中无零。这里不限制φ为univalent；omit一个点并不给一般holomorphic map的有限导数上界，例如φ(z)=μ(1−exp(Mz))的导数可任意大。必须同时计算J分子，不能套用Koebe四分之一作一般半径bound。

## 4. 新真实周期的全 jet 函数秩恰为10

**H11（完整 rank）。** 对任意 u∈C，

\[
 \{1,F_u,DF_u,\ldots,D^8F_u\}
 \text{ 在 C(t) 上线性无关，实际秩为10。}
 \tag{H11}
\]

证明：若 r_*(t)+Q(t,D)F_u=0，order Q≤8，绕μ并使用有理coefficients单值，得 Qχμ=0。χμ非零且 L irreducible rank9；其minimal annihilator overC(t)是L，因此低于9阶的Q只能为0，随后r*=0。这个证明检查实际 scalar functions，不用 finite minors或矩阵秩替代。

LF_u=r5；因1−Λt非零有理函数，D9F_u可表达为有理函数与D0…D8F_u，故该十维span对D闭合。F_u有一个十阶homogeneous annihilator (D−Dr5/r5)L，且前述 monodromy argument排除阶≤9的annihilator：若Q9 annihilateF，则Q9右除L的余数必须为0，Q9=v(t)L，而v r5≠0。所以真实最小阶亦为10。

若 u∈Q，H11也是Q(t)-rank；各行有 H7 的同一cap。选前m行（2≤m≤10），CDT v2 Definition6.0.1/Theorem6.0.2的九列width1数组，只有第一行0、其余行全部激活，e=0，准确

\[
 \sigma^T=(0,9,\ldots,9),\qquad
 \tau_T(m)=9\frac{m^2-1}{m^2}.
 \tag{H12}
\]

特别 rank2给27/4、rank10给891/100=8.91。把 f0 加进filled family会重新引入c跳跃，不能免费提高rank；H11则使用F本身的完整derivative族，c填洞后各行一同holomorphic。

## 5. 同叶对数参考族严禁当前账本产生 CDT 秩矛盾

**H13（m个已知参考函数）。** 对同一μ与任意m≥2，

\[
 \mathcal R_m=\{1,\ell,\ell^2,\ldots,\ell^{m-1}\}
 \tag{H13}
\]

在C(t)、从而Q(t)上线性无关；沿μ反复monodromy使ℓ→ℓ+2πiN，在一个普通点有无穷值，证明ℓ对C(t)超越。所有rows holonomic；D_n^j[t^n]ℓ^j整来自每个composition项恰j个分母≤n，且A为整数。因此可用m−1列width1的nested LCM array，e=0，

\[
 \sigma^R=(0,1,2,\ldots,m-1),\qquad
 \tau_R(m)=\frac1{m^2}\sum_{j=1}^{m-1}(2j+1)j
 =\frac{(m-1)(4m+1)}{6m}.
 \tag{H14}
\]

H10证明这些函数沿每一个target-admissible φ都holomorphic，满足同一CDT解析条件。由CDT Cor6.0.14，在ρ=log|φ′(0)|>τR时，准确

\[
 m\le\frac{J(\varphi)}{\rho-\tau_R(m)}.
 \tag{H15}
\]

**H14（严格账本比较）。** 对2≤m≤10，τT(m)>τR(m)。可约去(m−1)/m，变成54(m+1)>m(4m+1)，即4m²−53m−54<0；该二次函数在[2,10]的端点均负且凸，故全区间负。

如果ρ>τT，H15的右侧positive，得到

\[
 \frac{J(\varphi)}{\rho-\tau_T(m)}
 \ge\frac{J(\varphi)}{\rho-\tau_R(m)}\ge m.
 \tag{H16}
\]

因此使用 H12 当前array、同一actual φ 与ordinary double Jensen分子的任一rank2到rank10包，均不可能得到CDT contradiction要求的m>J/(ρ−τT)。这不是“暂未找好map”，而是对这个cap/leaf接口的全map比较证据。若ρ≤τT，target derivative gate本来就不成立。

结论同样适用于CDT Theorem6.0.2的多map版本：同一分割γ、同一分子和γ² log derivative gap terms只依赖m和maps；当最末ρ>τT>τR时，reference theorem给该分子≥m(ρ−τR)，仍排除target严格余量。必须保持所有maps和完整rearrangement分子相同，不能只比较largest derivative。

H16只排除本稿明确的uniform cap9、有限rank≤10、同map CDT数据，不证明所有ζ5方法无效、不证明最优整化率为9，也不限制其他更深holonomy定理或新extension。若仍保持全rank10且均匀row type (0,s,…,s)，要逃开本参考比较至少需

\[
 s(1-10^{-2})<123/20,
 \quad\text{即 }s<205/33\simeq6.2121;
 \tag{H17}
\]

这是摆脱当前比较的必要账本条件，绝不是达到数值无理性strict margin的充分条件。可以另行改进mixed array、构造去掉μ完整jump的实际relative chain、或提高真实独立函数数量并支付其费用；这些改变都须重新证明。

## 6. 实际 p9 首层反转成同一个正向 Ramanujan 截断和

**H15（一个准确的改费算术入口）。** 写 b_n=[t^n]B5。对任一 prime p>31，N与A为p单位，H7保证 Np9 b_p 可模p约化。准确

\[
 \boxed{Np^9b_p\equiv
 -A\sum_{k=0}^{\lfloor p/5\rfloor}
 P(-k)h_k A^{-k}\pmod p.}
 \tag{H18}
\]

证明：m=p的一项在Np9b_p中贡献−P(p)A^p≡−30A。对1≤m<p，p²>5p使h_m只有p这一层valuation，恰C_p(m)。只有4p/5<m<p达到9，其余terms乘p9后全部为0 modp。令m=p−k，1≤k≤floor(p/5)。Lucas给h_p≡2^5·5!=3840；Wilson给

\[
 p^{-9}h_{p-k}\equiv
 -24\frac{((k-1)!)^{15}}
 {((2k-1)!)^5(5k-1)!}\pmod p.
\]

这里两个分子 factorial ((2m)!)5、(5m)!分别有5和4次p因子；缩放后符号为−，multiples给4!=24，所有k≤floor(p/5)的remaining factorial均<p。于是

\[
 h_p\frac{p^9}{(p-k)^9h_{p-k}}\equiv h_k\pmod p,
\]

因为 ((2k−1)!)5(5k−1)!/((k−1)!)15=h_k k9/160。再用P(p−k)≡P(−k)、A^(p−k)≡A A^−k，并补k0，得H18。全部范围、p单位和负号已支付，未执行finite prime验证。

**H16（确切 scope）。** 令 S_p 为H18截断和。则

\[
 S_p\not\equiv0\pmod p\Longrightarrow v_p(b_p)=-9,
 \qquad S_p\equiv0\pmod p\Longleftrightarrow v_p(b_p)\ge-8.
 \tag{H19}
\]

对固定有理u及p不整除其分母，F_u第p系数有同一首层，因为u h_p为p整。H19只检查一个真实coefficient及首层，不是所有n、所有prime powers的整化改善；它没有证明Dn8 cap，也没有证明最小CDT成本为9。更不能由一次modp抵消直接领取四层改善。

**H17（文献与候选超同余准确连接）。** 对floor(p/5)<k<p，h_k有正p valuation，因此

\[
 S_p\equiv\sum_{k=0}^{p-1}P(-k)h_k A^{-k}\pmod p.
 \tag{H20}
\]

这恰为同参数正向Ramanujan截断和：以未缩放z=Λt写，hypergeometric coefficient为h_k/Λ^k，而该正向special point z0=Λ/A=−5^5/2^10，polynomial为P(−k)=5532k4+5600k3+2275k2+425k+30。其未截断正向实级数的ratio绝对值Λ/|A|>1，通常发散；本文只使用有限sum，不假定收敛的1/π4评价。Guillera1908.05123v1 PDF17 Table5第三项正是这一组；本人实际渲染目读该表以核指数，不从混乱text table猜测。

该论文PDF3–4的Zudilin-type general pattern会为此组建议 full truncatedsum≡30p4 modp9，但这里它是猜想接口，不是已经支付的定理。原件的“few proved”不表示表5第三项已获证；1910.01961v1的p-adic expansions也明确为heuristic/conjectural，本稿不把其中ζp/Lp数字当作无条件finite-place比较。

下一算术问题因此具体为：证明H18真实reciprocal截断在更高p^k层的反转与所需partial blocks抵消，然后对全部n与所有prime powers建立更好的mixed denominator array。即使另外证明正向模p9猜想，仍不能不经higher-layer反转就宣布本lift cap降成Dn5。这个新入口是真实b_p的必要抵消条件，未开启素数扩表或数学producer。

## 7. 本轮结果及证据范围

本轮新增实际inverse-L lift首次同时满足Q Taylor与ζ5关系依赖的完整c填洞；其局部μ对数、真实rank10、全部有限处Dn9改进与共同log参考族的精确holonomy门槛已逐式纸证。缺口从“根本没有接口”推进为“接口存在，但新增μ的完整jump和当前算术账本阻止CDT余量”。它仍不是ζ7、Catalan或其他新数值结论。

实际原件阅读：固定CDT v2 PDF66–69全文，支持全部array、single/multi-map与holonomic门槛；Au2312.14051v4 PDF2、19、25–26全文，支持Pdegree4、N、已证级数及WZ评价来源。新增正常TLS归档Guillera1908.05123v1（18页），实际全文读PDF1–4、16–18七页，另render/目读PDF17；Guillera1910.01961v1（5页）全部全文读。这两篇正常TLS保存于literature/cdt_gamma_lift_arithmetic_sources_20261007，不禁用证书验证；归档23页与实际12页不同。个人本轮distinct primary PDF共20页。已有PDF不重复下载；文献提取、渲染与SHA检查不是数学producer。初始已有period稿只读前210行，未把该partial计为全文读。本稿完整Gamma G1–G19及主记录§§181–185实际全文读；所有588旧冻结记录物理SHA核通过，不冒称人工重读全部历史证明。
