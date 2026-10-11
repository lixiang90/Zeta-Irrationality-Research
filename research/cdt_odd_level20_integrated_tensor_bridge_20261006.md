# 含序号分母的 balanced Smith 接口：先固定 cutoff，再作优化

日期：2026-10-06。本文另建，所有既有报告冻结。新结论是 CDT §8.2 的近似均衡张量兼容性在一个明确小素数窗口内也能处理 e_i>0。必须先固定积分 cutoff ξ，再扣已证 Smith 收益，最后统一优化；不能把已最小化的 τsharp 与另一 ξ 下的收益直接相减。本文以一个实际 rank8 的 I_K 元组作全尺度验证，并核三个既有规定类型族的乐观下界。没有证明新的数值无理性，没有声称最优整格、最优背景或所有方法不可能。

## 1. 输入、真实 source 与限定范围

原件为 [CDT 固定218页版本](../literature/cdt2024_l2_chi_minus3.pdf)：Definition6.0.1、(6.0.5)在第66页；真实近似均衡 source (8.2.2)在第129页；积分 cutoff 估计 (8.2.35)–(8.2.40)在第142–143页。

复用 [已冻结 e=0 张量接口](cdt_odd_level20_balanced_smith_bridge_20261006.md) 的真实整数 source、DVR引理(B3)、leading inclusion、严格内窗极限及 HS/arch 归一；复用 [平方提升](cdt_odd_level20_square_lift_20261006.md) 的实际目标三 rows S1/S2 输入。只考虑一个真实不可约三维目标 quotient，而不是 Q-joint 的六行。设完整 actual tuple 秩 m，至少有常数1；三个目标 rows e=0，LCM类型为三个单位列，其余额外列为0。各背景行的完整类型为

\[
 C_i n^{e_i}\prod_h D_{\lfloor b_{i,h}n\rfloor},
 \qquad D_n=\operatorname{lcm}(1,\ldots,n),
\tag{I1}
\]

明确沿用CDT的条件e_i∈Z≥0、b_i,h∈R≥0；因此下列ν_i与s为非负整数，p^s是合法整数缩放。固定 C_i 只排有限坏 primes。固定 offsets可用严格内窗和最后极限吸收。设

\[
 q_i=\#\{h:b_{i,h}>0\},\quad \nu_i=q_i+e_i,
 \quad s=\max_i\nu_i\ge3,\quad E=\sum_i e_i,
 \quad e_*=\max_i e_i.
\]

θ_i=max_{b_i,h>0}(1/b_i,h)，没有positive列时取0。将θ非降序排序，θ_(1)=0，并设

\[
 a_0=\min_{i\ge2,\theta_{(i)}>0}\frac{i-1}{\theta_{(i)}}.
\tag{I2}
\]

若全无positive列，可取a₀=∞；本目标含单位列。序号因子不进入(I2)，它在原sharp粗界中另计。没有zero θ row时不跳过第一个positive θ，只能用a₀=0。本稿保留第八节 near-balanced species、每coordinate polynomial degree≤D；不处理第六节 exact-balanced 或新的 degree filters。

## 2. 原积分估计在每个固定 ξ 下的接合

先固定 ξ∈[0,m]，不作最小化。CDT (8.2.40) 的 normalized累计有限高度上界，合并(8.2.34)，为

\[
 \frac{m}{2}\tau^{\flat\flat}(b)
       +\frac{\xi E+e_* I_m(\xi)}m,
 \qquad I_m(\xi):=I^m_\xi(\xi).
\tag{I3}
\]

原证明确把 p≤ξD 的序号分母用近似均衡 species 的 dE/m 粗界计入；p≥ξD 用区间 LCM 的 I_m(ξ)。粗界不必是某个共同transport的实际最优值，以下扣除来自真实累计 determinant 的另一安全界。

令

\[
 a(\xi)=\min\{a_0,\xi,1\}.
\tag{I4}
\]

在窗口 p≤aD，flat transport恰为d∑q_i/m：依θ顺序把species i配到 normalized exponent 的[i−1,i]，全部positive列均active；原小prime sharp bound是dE/m。因此(I3)在这段采用的合计baseline是d∑ν_i/m。ξ=0或a=0时不扣收益。

对好 place 及 p²>max(1,max b_i,h)N_D，整个所需一变量 prefix 每项序号 n与每个LCM列的p-valuation都至多1，故实际 pure 整数source的矩阵 p^s eval是整的。完整背景 block 的 image含p^(s−ν_i)。目标全部blocks的baseline是p^(s−3)，实际primitive关系额外给 thresholds s−2与s−1，数量为

\[
 k_1=2\bigl(D-\delta_H+1\bigr)_+,
 \quad \delta_H\le(3p+9)/2,
 \qquad k_2=(D-3p-19)_+.
\tag{I5}
\]

背景支持与目标支持分离，故 certified capped floors 的和至少为

\[
 [sm-\textstyle\sum_i\nu_i](D+1)+k_1+k_2,
 \qquad\text{每个floor}\le s.
\tag{I6}
\]

此处S1/S2可以重叠；k₂仅增加第二阈值的一层，不另计一组普通kernel。将冻结DVR引理的cap改为s、codimension损失改为sdc，真实balanced leading minor的累计高度上界减去dR^(d−1)(k₁+k₂)logNorm𝔭。baseline恰等于上面的d∑ν_i/m；near-balanced与full tensor的baseline差为O(ηdR^d)，d→∞消失。先取固定严格内窗p≤(a−δ)D，再令species/degree discrepancies足够小；D→∞、d→∞、各tolerance→0、最后δ→0。p²不足的小prime、高幂及固定坏place照原(I3)处理，只删o(D²)的新收益。

因此原(I3)在相同ξ下改善为

\[
 \frac m2\tau^{\flat\flat}(b)
 +\frac{\xi E+e_*I_m(\xi)-\gamma(a(\xi))}m,
\tag{I7}
\]

其中素数定理给全尺度函数

\[
 \gamma(a)=2\int_0^{\min(a,2/3)}(1-3x/2)dx
       +\int_0^{\min(a,1/3)}(1-3x)dx
 =\begin{cases}
 3a-3a^2,&0\le a\le1/3,\\
 2a-3a^2/2+1/6,&1/3\le a\le2/3,\\
 5/6,&a\ge2/3.
 \end{cases}
\tag{I8}
\]

和e=0接口相同，累计finite的归一收益是γ(a)/m，斜率最后归一后的成本收益才是2γ(a)/m²。这里没有变换source或减少其Arakelov degree。

## 3. 真正的逐尺度 κ 及统一优化

原 HS/archmetics保留，所得限定公式为

\[
 \boxed{\kappa(\xi)=\tau^{\flat\flat}(b)
  +\frac2{m^2}\bigl[\xi E+e_*I_m(\xi)
                   -\gamma(\min(a_0,\xi,1))\bigr].}
\tag{I9}
\]

每个固定ξ给m(ρ−κ(ξ))≤J；共同number-field embeddings取原归一平均。实际tuple已微分闭合，保留已证明的number-field closed-system分支，无需自动holonomicity较强门槛。原(8.0.4)、(8.0.5)两种convexity只有metric改变，finite同(I7)，所以保留各自合法原numerator。这一步不允许省略8.0.5的新HS项，证明已在冻结接口§5。

可最后取min_{ξ∈[0,m]}κ(ξ)。如果只知道某个relaxed原成本下界B，则简单但严格的乐观估计是

\[
 \min_\xi\kappa(\xi)\ge
 \tau^{\flat\flat}(b)+\tau^\sharp(e)-\frac5{3m^2}
 \ge B-\frac5{3m^2}.
\tag{I10}
\]

式(I10)只是对已证S1/S2收益的最大信用，不声称minimum由同一ξ实现，也不把B当真实transport值。严格matching窗口不满足时，本稿实际信用可能更小；因此乐观下界仍合法。不同来源的新局部关系、更高Smith阈值或改变geometry均不在此上界信用内。

## 4. 一个实际 rank8 的 I_K 元组

取

\[
 \mathcal F_8=(1,L,T_2,K_2,I_K,gH,g\vartheta H,
                                      g\vartheta^2H),
 \quad I_K=\int_0^tK_2(u)du/u,\quad g=\Delta^2.
\tag{I11}
\]

反证假设与真实目标按[level20模型](cdt_odd_level20_model_20261006.md)。背景的实际闭包方程为L′=1/(1−t)、T₂′=L/(1−t)、K₂′=K₂/[2(1−t)]+L/[t(1−t)]、I_K′=K₂/t。前三个unipotent方向与K₂的sign方向独立；若I_K=rK₂+P属于其有理span，比较K₂系数强迫r′+r/[2(1−t)]=1/t，无有理解，因0处最高pole或简单残数矛盾。背景rank5；它仅含trivial/sign composition factors，故与目标不可约rank3 quotient的交为常数。合并实际rank恰8，不计整个ODE所有solutions。

这些事实和全部素数类型来自[完整低成本polylog报告](cdt_odd_low_cost_polylog_20261006.md) §§2–3。为验证新接口，固定以下简单安全型，不在此选择更多背景或扫描参数：

|row|完整类型|e|flat row sum|
|---|---|---:|---:|
|1|1|0|0|
|L|D_n|0|1|
|T₂|固定常数·D_n²|0|2|
|K₂|D_n²|0|2|
|I_K|nD_n²|1|2|
|三个target|固定常数·D_n³|0|3各一行|

列可取三个嵌套单位列，故真实τflatflat就是CDT单位表的值，并不是comonotone放宽：

\[
 \tau^{\flat\flat}=\frac{162}{64}=\frac{81}{32},
 \quad E=e_*=1,\quad a_0=1,
 \quad\nu=(0,1,2,2,3,3,3,3).
\tag{I12}
\]

三个baseline threshold counts是4(D+1)、2(D+1)、D+1；另分别加k₁、k₂，floor和为7(D+1)+k₁+k₂，且3−7/8=∑ν_i/8=17/8，与(I7)baseline一致。共同实际解析cover仍合法：L与square root沿省去1的disk有全局分支；I_K的pulled-back积分源K₂(φ)φ′/φ在唯一零点0可去，在其它点无pole。固定g清目标branchpoles；不是从Taylor半径推cover。

## 5. 不引用旧最小值的独立全 ξ 核算

由原Definition6.0.1直接交换有限和/积分得，对0≤ξ≤1，

\[
 I_m(\xi)=C_m-m\xi+\xi^2/2,
 \quad C_m=3/2+(m-1)H_{m-2}+H_{m-1}/2.
\tag{I13}
\]

例如第二积分中harmonic项贡献∑_{h=1}^{m−2}(m−h−1)/h；第三积分贡献(m−1)+H_{m−1}/2，第一积分贡献(1−ξ)²/2。对1≤ξ≤m，第二积分第h项从t=1+hξ起，第三积分第k段只有t∈(kξ,kξ+1)正值，因此

\[
 I_m(\xi)=\sum_{h=1}^{m-1}\frac{(m-1-h\xi)_+}{h}
 +\sum_{k=1}^{m-1}\frac{\min(1,(m-k\xi)_+)^2}{2k}.
\tag{I14}
\]

这是所有ξ的精确式，不依赖数值样本。m=8时C₈=1117/56，令P(ξ)=ξ+I₈(ξ)。在[0,1]，P′=ξ−7<0；在[1,7/2)，(I14)第一sum至少有两项，故P′≤−1。对[7/2,4]，P′=−(8−2ξ)≤0；在[4,7]，P=7+(1/2)=15/2；在[7,8]，P=ξ+(8−ξ)²/2，P′=ξ−7≥0。端点连续，因此

\[
 \min_{[0,8]}P=15/2,\qquad
 \operatorname{argmin}P=[4,7].
\tag{I15}
\]

γ(min(ξ,1))≤5/6，且在[4,7]已等于5/6。这次原minimum与完整收益确实同ξ实现，故逐尺度(I9)的真正minimum为

\[
 \boxed{\min\kappa=\frac{81}{32}
       +\frac1{32}\left(\frac{15}2-\frac56\right)
       =\frac{263}{96}.}
\tag{I16}
\]

J≥ρ的必要尺度为ρ>mκ/(m−1)=263/84。即便使用已证numerator≥ρ的标准convexity变体，必要门槛相同。263/84>14/5>log16，故这个固定真实I_K元组仍不能在当前省去1、唯一零点的cover上得到rank矛盾；并非缺少ξ参数搜索。

## 6. 三个较大规定类型族的乐观下界

只读复用[原指定类型证书](cdt_odd_level20_pure_budget_20261006_verify.json)与[说明](cdt_odd_low_cost_polylog_20261006.md) §6：真实MPL9+I_K背景，分别加T₄、T₅，合并rank m=13、14、15，规定类型数768、1536、3072。原证书的comonotone row-sum lower bound加完整τsharp所给必要尺度下界，分别为1345/468、2577/910、1769/630。它们是完整列transport的放宽下界，不能标成真实τ。

由(I10)，对这三个指定族、任意ξ，甚至乐观给予全部γ=5/6信用，Jensen必要尺度的下界最多降低5/[3m(m−1)]。独立有理计算为

\[
 \frac{1345}{468}-\frac5{468}=\frac{335}{117},\qquad
 \frac{2577}{910}-\frac5{546}=\frac{3853}{1365},\qquad
 \frac{1769}{630}-\frac5{630}=\frac{14}{5}.
\tag{I17}
\]

前两项减14/5分别是37/585与31/1365，第三项等于14/5。并有e^(14/5)>16：仅其前11个正Taylor项的有理和已超过16。所以这些规定族在本文接口的已证S1/S2改善下，任何cutoffξ均不能跨log16；真正matching信用可能更少，只使结论更强。这里没有重跑768/1536/3072 producer、没有新增类型/素数扫描，也不把有限规定族推广到T₆以后、任意换基、任意iterated integral、新target积分或更高层。

## 7. 证书与可执行下一接口

配套独立[脚本](cdt_odd_level20_integrated_tensor_bridge_20261006_verify.py)和[证书](cdt_odd_level20_integrated_tensor_bridge_20261006_verify.json)由作者执行，57项固定精确检查全部通过。脚本只使用Fraction：重建(I13)–(I14)的所有m8精确分段、逐段求P−γ的极小值、核完整baseline/counts、两种归一、三个新有理下界及Taylor比较。它不import或执行旧producer，不以有限检查替代(I1)–(I9)全尺度证明。实际函数rank、全部素数分母、目标S1/S2和共同cover仍引用列明已证输入。

最终限定只读独审：root通过全文公式、真实rank8及§5由原Definition6.0.1直接积分的全ξ极小值；low_period_closure回读原PDF pp129、142–143后通过实际§§1–3的同ξbaseline、pure source、strict window和归一，并独推§5精确分段。low建议显式写e整数、b非负实数，已在§1补充。两位均未执行本文或旧producer；其审阅不另代替列明目标S1/S2输入和冻结metric证明。

最小执行接口为：输入完整(e,b)、同一ξ、θ-matching窗口、真实目标局部thresholds、实际leading set和primitive near-balanced source；输出(I9)，最后才min ξ。新增target积分若改变e或packet thresholds须重新给局部输入；改geometry须重新核全部真实芽的解析pullback。本文填补序号分母与已证张量收益的一处兼容缺口，尚未建立新的数值定理。
