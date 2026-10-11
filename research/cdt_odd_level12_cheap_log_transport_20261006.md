# D12 两个固定多log数组的精确联合transport成本

日期：2026-10-06。本文接 [已冻结cheap-log证明](cdt_odd_level12_cheap_log_packet_20261006.md)，只计算预先固定的k2/k3数组。没有改动既有producer，没有搜索prime或更多degree。结论是其column安全upper均能在每个threshold由一个共同coupling达到，故是真正的τflatflat：366/169与1146/529。此前348/169与1078/529仍仅是comonotone下界，没有~0.1的额外成本折扣。

实际rank13/23、全素数packing分母、三个log同一fullleaf的合法性、target交常数及数域闭合系统接口，均引用列明已冻结证明；本文不代替它们。原始定义为 [CDT固定218页原文](../literature/cdt2024_l2_chi_minus3.pdf) (8.0.2)，PDF122–123页。没有计算actual radius/J，也没有证明L(3,χ12)无理。

## 1. 每个threshold各自优化，不要求全x共享coupling

令u∈[0,1]为均匀normalized grade，x=k/N为固定threshold。将同数组的monomials按degree聚成species classes，k2质量是(1,3,6,3)/13，k3是(1,3,6,10,3)/23；class顺序为constant、degree1、degree2、degree3（仅k3）、target。每class内部等分回每条actual row，正好保持每species质量1/m。

使用四个grade区域

\[
[0,x),\ [x,\min(2x,1)),\ [\min(2x,1),\min(3x,1)),\ [\min(3x,1),1].
\tag{T1}
\]

它们的mass p(x)分别在以下三段是

\[
\begin{array}{c|c}
0\le x\le1/3&(x,x,x,1-3x)\\
1/3\le x\le1/2&(x,x,1-2x,0)\\
1/2\le x\le1&(x,1-x,0,0).
\end{array}
\tag{T2}
\]

每条class在(T1)上的payoff rows为

\[
c_0=(0,0,0,0),\quad c_1=(0,1,1,1),\quad
c_2=(0,1,2,2),\quad c_3=(0,1,2,3),\quad c_H=(0,3,3,3).
\tag{T3}
\]

这直接数本row active LCM列；x>1时全为0。设M_k(x)是以这些row/column marginal为约束的transport最大payoff。原文(8.0.2)的max位于对threshold的求和内部，因此每个x可有不同最优coupling；无需一个全x共同最优的species/grade配对。于是原τ的候选精确值是2∫0¹M_k(x)dx，§4证明它确实等于原离散定义。

## 2. 完备的有限整数dual与端点primal证书

transport dual取row potentials u_i、column potentials v_j，约束u_i+v_j≥c_i,j，目标最小化Σr_i u_i+Σp_j(x)v_j。因为所有payoff整数、约束矩阵为bipartite incidence的符号变体（固定一个potential后totally unimodular），存在integer optimal potentials。

每个row payoff随column非降。把v_j替换为min_{h≥j}v_h仍合法，且不增加dual目标：对每个h≥j，u_i+v_h≥c_i,h≥c_i,j。因此可先使v非降，再平移使v0=0；此时第一column的payoff0强迫u_i≥0。将大于3的v_j截到3仍合法，因为c_i,j≤3、u_i≥0，并再次不增加目标。最后取u_i=max_j(c_i,j−v_j)。因此最优一定在完整有限族

\[
v=(0,v_1,v_2,v_3),\quad
0\le v_1\le v_2\le v_3\le3,\quad v_j\in\mathbb Z
\tag{T4}
\]

中，恰20种。这是所有dual的一份数学完备约简，不是对参数的经验扫描。固定(T2)一段后，每种dual目标都是有理affine line A+Bx；20条线的lower envelope以有理intersection给全部精确分段。

[新独立JSON](cdt_odd_level12_cheap_log_transport_20261006_verify.json)逐段保留同一integer dual、两端点的精确Fraction flow。每端点flow非负、row/column masses准确，且只用complementary-slack edges u_i+v_j=c_i,j，primal value等于dual value。两端flow线性插值在整段保持非负和所有marginals，因为(T2)该段的marginals是affine；它也保持complementarity。故端点证书证明整个连续区间的最优性，没有浮点拟合。

## 3. 精确M(x)及其积分

k2的row-potential顺序为(0,d1,d2,H)。表中的grade resource分界1/3保留两端primal，但M表达式可合并。

|x区间|M2(x)|row u|column v|
|---|---|---|---|
|[0,1/13]|24/13|(0,1,2,3)|(0,0,0,0)|
|[1/13,7/26]|25/13−x|(0,0,1,2)|(0,1,1,1)|
|[7/26,1/2]|32/13−3x|(0,0,0,2)|(0,1,2,2)|
|[1/2,10/13]|19/13−x|(0,0,0,2)|(0,1,2,2)|
|[10/13,1]|3−3x|(0,0,0,0)|(0,3,3,3)|

k3的row順序为(0,d1,d2,d3,H)：

|x区间|M3(x)|row u|column v|
|---|---|---|---|
|[0,1/23]|54/23|(0,1,2,3,3)|(0,0,0,0)|
|[1/23,7/46]|55/23−x|(0,0,1,2,2)|(0,1,1,1)|
|[7/46,13/69]|62/23−3x|(0,0,0,1,2)|(0,1,2,2)|
|[13/69,1/3]|75/23−6x|(0,0,0,0,2)|(0,1,2,3)|
|[1/3,1/2]|52/23−3x|(0,0,0,0,2)|(0,1,2,3)|
|[1/2,20/23]|29/23−x|(0,0,0,0,2)|(0,1,2,3)|
|[20/23,1]|3−3x|(0,0,0,0,0)|(0,3,3,3)|

在全部x，这些M正好等于已冻结稿的三column maxima之和。JSON的endpoint primal给共同coupling，证明此处各column maxima确可同时达到；这没有说所有任意矩阵都具有该性质。积分给

\[
\boxed{\tau_2^{\flat\flat}=2\int_0^1M_2(x)dx=366/169,
\qquad\tau_3^{\flat\flat}=2\int_0^1M_3(x)dx=1146/529.}
\tag{T5}
\]

原comonotone成本下界与真值差分别18/169、68/529。它们来自允许各threshold换coupling的真实max，不是因分母证明或实际rank失效。

## 4. 连续transport与原species/discrepancy极限

首先对任意原文balanced species i及good-discrepancy grades n_j/N，将其经验耦合聚成(T3)的classes与(T1)的四intervals。species平衡误差给row-mass误差O_m(ϵ)，grade discrepancy给每column质量误差O(ε+1/N)。每格payoff≤3；修正marginals的运输质量只需同阶误差，故payoff/d≤M_k(x)+O_m(ϵ+ε+1/N)，在x统一有界。最大、threshold Riemann sum及原顺序极限于是给τflatflat≤2∫M。

反向取d为m的倍数，选近乎等间距的grades n_j/N=floor(N(j−1/2)/d)/N。其discrepancy≤1/d+1/N，且每actual species可分配恰d/m个coordinates。对每个threshold x，将上面optimal continuous flow乘d并按格round down；调整有限个row/column deficits，最多损失O_m(1)个coordinates的payoff，然后用任意剩余species填满其余grade格。各class内部再等分到actual species，不改变payoff，保持原species平衡。

这一步对每个x独立进行，正合原Σ_threshold max；不要求同一个n/i同时给全x的最优flow。每格threshold的ties或grade rounding只影响O_m(1)项。故max payoff/d≥M_k(x)−O_m(1/d+1/N)。先N→∞，再d→∞及ϵ,ε→0，threshold sum是有界分段连续M的Riemann sum，得到反向τflatflat≥2∫M。结合upper证实(T5)。

因此(T5)不是只对某个finite degree或某次flow求解成立，而是原文第八节的完整固定数组成本。所有数学限制仍为既有k2/k3数组和同一actual两地图。

## 5. 核验与剩余研究口

[NEW脚本](cdt_odd_level12_cheap_log_transport_20261006_verify.py)不读取任何旧producer，作者首次、单次执行，184项固定精确检查全部通过。它枚举(T4)的完整20dual族，算有理lower-envelope分界，在每个endpoint用确定性Fraction maxflow验证primal/dual equality、nonnegative及marginals。k2保存6个certificate pieces（含grade资源的1/3分界），k3保存7个。有限证书配合§2的完备dual约简和§4极限证明，才给(T5)；不计算map radius/J或数值L值。

成本相较此前safe upper没有继续下降；两安全账本的plain Jensen尺度现在可准确标为61/26与573/253。它们仍小于几何cap，但cap不等于实际ρ。下一瓶颈是同一合法地图的实际ρ和J（或另一个已经实际认证的更大period群），不是继续把comonotone lower当预算或增加degree扫描。当前没有新的数值无理性定理，也没有Smith折扣输入。

最终限定只读独审：root实际完整阅读本MD及新PY，通过全部§§1–4的grade/species payoff、integer dual的TU完备约简及monotone replacement/clip≤3、endpoint exact-flow插值、全threshold独立coupling及discrepancy双向极限；未执行producer。作者随后只读JSON确认all_passed=true、passed_count=184、两个exact_tau分别366/169和1146/529。记录该范围后本文三件冻结，不再运行producer；既有cheap-log和budget三件保持其冻结状态。
