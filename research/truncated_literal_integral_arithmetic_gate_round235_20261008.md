# 第235轮：literal积分类型不能降低完整三维源的算术费用

2026-10-08，Packet/B。只检验一个有界接口：当前CDT Definition6.0.1的literal nᵉ与任意LCM矩阵，能否降低冻结234完整源V=span_Q(u){1,E,J_g}的费用。g∈Q、u坐标、basis及e均固定。旧234及manifest不改，数学程序0。

## 1. 实际原文与合法类型

复用当前作者220页PDF，3628820 B / SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c。实际FULL读取物理66–71：Definition6.0.1在67，Theorem6.0.2完整67–68，Corollary6.0.14在69；另FULL读123–125的Theorem8.0.1、(8.0.2)及Remark8.0.6。67–68另渲染后实际视读公式。这里没有FULL认证220页证明，也没有冒称已审§7各负能量修正的全部条件。

原文(6.0.9)的literal类型是

\[
f_i(u)=a_{i,0}+
\sum_{n\ge1}\frac{a_{i,n}u^n}
 {n^{e_i}\prod_h d_{\lfloor b_{i,h}n\rfloor}},
\quad a_{i,n}\in\mathbb Z,\quad e_i\in\mathbb N.
\tag{C1}
\]

τ=τ♭(b)+τ♯(e)，其中τ♯=(2/m²)min_(ξ∈[0,m]){ξΣe_i+(max e_i)I_ξ^m(ξ)}；Definition6.0.1的每个积分项非负，故τ♯≥0。Theorem6.0.2限制各列为leading zeros后接共同正数；Theorem8.0.1允许任意非负矩阵，并用τ♭♭(b)替代τ♭。Remark6.0.12允许固定cutoff shifts，只影响有限头及极限过程。

对旧完整tuple(1,uE,b_gJ_g)，合法e=0、两列(0,2,2)、(0,0,1)达到τ=7/3。本轮证明固定literal e以及任意矩阵都不能让这个完整V的算术项低于7/3；不是把安全upper当最优联合格lower。

## 2. 为什么乘n不能删掉J的双层

沿用冻结234完整公式

\[
S=\sqrt{1-4u}\in\mathbb Z[[u]],\quad
E=\sum_{j\ge0}\frac{3^j}{2j+1}u^j,\quad
J_g=S(g-2I),
\quad
I_n=\frac1n\sum_{j=0}^{n-1}
\frac{3^j}{2j+1}\binom{2(n-1-j)}{n-1-j}.
\tag{C2}
\]

对p>3、p∤den(g)，k=(p−1)/2，已付p²I_p≡(−3)ᵏ。对任意固定整数t≥0、充分大p，区间ℓ≤p+t的外分母仅ℓ=p含p；内奇分母仅p含p，且无p²或3p。故完整卷积的唯一p²源为I_p，给

\[
p^2J_{g,p+t}\equiv-2(-3)^k [u^t]S\pmod p.
\tag{C3}
\]

下标<p时p²归约为0。特别s₁=−2，所以p²J_(p+1)≡4(−3)ᵏ≠0。无论固定e多大，(p+1)ᵉ仍为p单位。因此候选nᵉd_(2n)均不能清J的全部系数：在n=p+1，d_(2n)仅含一个p，缺第二层。这个障碍保留全部finite heads，不只考察n=p。

## 3. 任意固定有理基仍有p单位的双层见证

令f=aJ_g+bE+c∈V∩Q[[u]]，a,b,c∈Q(u)固定，可各有有限Laurent负阶。除有限prime外，全部Laurent系数p整。若a≠0，则aS不可能仅含常数项：否则a=const/S非Q(u)，与a有理矛盾。选一个固定h≠0，使q_h=[u^h](aS)∈Q×。

取n=p+h。C3及p前系数的估值给

\[
p^2[u^{p+h}]f\equiv-2(-3)^kq_h\ne0\pmod p.
\tag{C4}
\]

bE只到p+O_f(1)，最多simple p极点；c p整。Laurent卷积中i≤h贡献s_(h−i)，其余项只碰到p前系数，所以C4对正、负h都成立；p充分大时n>0。排除p|h后，n≡h为p单位。于是对于任意固定e≥0，

\[
p^2(p+h)^e[u^{p+h}]f
\equiv-2h^e(-3)^kq_h\ne0\pmod p.
\tag{C5}
\]

所有充分大p≤N−C_f在带literal权重nᵉ的完整prefix继续强迫p²。

## 4. p/2见证也不能由literal nᵉ清掉

冻结234已付完整残差：当N+C_f<p≤2N−C_f时，所有Laurent卷积所需原下标<p，且

\[
pE\equiv3^ku^k,\quad
pJ_g\equiv3^ku^{k+1}A,\qquad
uA'+\left(\frac12+\frac{2u}{1-4u}\right)A=-2,\quad A_0=-4.
\tag{C6}
\]

这些模p式仅断言所需完整截断。A非rational：除以u后的系数1/(2u)+2/(1−4u)在∞为O(u⁻²)，rational解的导数主项无法匹配−2/u。所需A_j满足2j+1<p，归约无隐含p分母。

若a≠0，a uA+b≠0，令其首个固定Laurent项为d₀u^j₀。取n=k+j₀，pf_n≡3ᵏd₀为单位，而
2n≡2j₀−1≠0 modp，除有限prime；j₀为整数，2j₀−1不可能为0。因此固定nᵉ仍保留这个simple p层。

若a=0、b≠0，以b的最低Laurent阶β同样取n=k+β；首次E极点给单位，2n≡2β−1也是非零固定整数。所有大p≤2N−C_f均为纯E行的见证。由PNT，带literal权重的最小完整prefix分母满足

\[
\liminf_{N\to\infty}
\frac{\log\operatorname{LCD}\{n^ef_n:1\le n\le N\}}N
\ge
\begin{cases}3,&a\ne0,\\2,&a=0,\ b\ne0.\end{cases}
\tag{C7}
\]

固定g、scalar、Laurent阶及literal e只改变有限badprime与端点常数；没有随N/p更换basis。

## 5. 任意矩阵的费用下界也为7/3

同一批见证还比row-sum下界更强。对每个非rational行，n≈p/2且nᵉf_n有simple p单位残差，C1至少须有一个b_(i,h)≥2：若全部固定b<2，全部cutoff长度都<p，均无p。

对含J的行，C5在n=p+h迫使至少两个列项b_(i,h′)≥1。固定有限slopes使各cutoff长度O(p)<p²，每个LCM只能给一个p；若第二大slope<1，则除最多一列外长度均<p，无法支付双层。固定cutoff shifts不改变这两个必要极限。

完整basis至少两行非rational、至少一行含J。因而逐行把列降序排列，选择J行最后、另一非rational行居中，再补零列后，矩阵entrywise dominates

\[
b_{\min}=\begin{pmatrix}0&0\\2&0\\2&1\end{pmatrix}.
\tag{C8}
\]

这一步不假设原矩阵nested。(8.0.2)只数#{h:k≤b_(i_j,h)n_j}，故逐行独立perm列完全不改Den_N；row perm亦通过balanced label集合的双射保持Den_N。componentwise增加b则逐个count、max及各层limsup单调增加。Remark8.0.6对b_min明确给τ♭♭(b_min)=τ♭(b_min)=7/3。因此

\[
\boxed{\tau^{\flat\flat}(b)+\tau^\sharp(e)\ge\frac73}
\tag{C9}
\]

适用于完整V任意固定Q(u)basis、任意固定literal e、当前Theorem8.0.1的任意有限非负矩阵。e=0的旧合法模型达到该下界。

这不覆盖随截断变动的联合source lattice、其它literal线性因子、algebraic gauge、新变量或新独立函数。尤其除S后得到g−2I允许literal n，但1/S不是Q(u)换基，且该family丢掉J的关系敏感mark；这里不借用它来改写V。

## 6. 哪些解析判据因此失败，哪些仍待付

单图Corollary6.0.14的rearrangement能量对max用Jensen后至少∫T log|φ|≥log c，c=|φ′(0)|。未带负能量修正的(8.0.3)由已付Bost–Charles能量≥log c同样如此。C9给rank3矛盾的必要门槛log c>3τ/2≥7/2；冻结234的全部共同图cap
C₀=3π³√2/8<18<exp(7/2)，已关闭这些入口。

Theorem6.0.2的多图也不靠patching改变此必要门槛。令t_k=γ_k/m、w_k=t_(k+1)−t_k、d_k=log c_k递增。各patch块的平均μ_k=∫T log|φ_k|≥d_k。对max凸函数用conditional Jensen，双积分下界为
Σ_ab w_aw_b max(μ_a,μ_b)≥Σ_k(t_(k+1)²−t_k²)d_k。
原式(6.0.10)的switch系数实际是1/m，故其正项是mΣ_(k≥1)t_k²(d_k−d_(k−1))。将它减小为系数1的项后与上述下界telescopes到d_l；原式还多非负的(m−1)倍项。完整numerator因而≥log c_l。这里按原定理印出的闭盘全纯图域使用边界Jensen。若只给开盘图，先在共同r<1缩盘应用，再取径向积分的limsup；不从点态L¹边界免费断言Jensen，避免丢失边界奇异质量。不误写原正项为1/m²，也不把真正的patching当简单rank界的凸组合。

**没有因此排除(8.0.4)/(8.0.5)的真实convexity负能量修正。** 若把它实际扣除的量记作Δ，则任何此类rank3证书至少须付

\[
\Delta>3\tau-2\log c
\ge7-2\log C_0>0.
\tag{C10}
\]

这个正门槛只是必要条件，不是存在证书；Δ及所有subradii/s*条件应由另一完整证明核定。本文没有用单图J≥log c免费代替已扣Δ的能量，也未认证所有更强CDT机制失败。

## 7. 实际读取与停止范围

本轮新增纸证C3–C10，Root先提出传播主项和任意矩阵候选，本人逐项独立核Laurent量词、全部finite heads、literal p单位、逐行重排与limsup单调性。沿用234本代理实际FULL读取并冻结的完整积分公式、rank及basis残差，不重跑程序或旧归档。

当前primary完整选页和公式视觉身份存literature/refined_arithmetic_sources_round235_20261008/packet_reading_scope.md。当前PDF66–71、123–125实际FULL文本读取；67–68实际整页视觉读取。没有重复下载，也未以原文标题推出未读的§7条件。

停止结论只针对固定完整V的(6.0.9)/(8.0.2)算术入口：literal nᵉ与任意LCM列配对不减费用。真正负能量修正或不同source需要另付；不能把这里的下界转成一般联合格或全部数值方法no-go。数学程序0、扫描0、旧文件修改0；仅NEW235文件，保存后实际FULL作者复读并另报身份。
