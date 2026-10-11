# 固定一变量原源格的三层算术收益上限

日期：2026-10-06。独立核算对象仅为 [全局稿](cdt_odd_level20_hasse_global_20261006.md) 的实际 rank4、rank7 系统及原格 E₄,D、E₇,D。结论是：**当前账本不能给出绝对排除；即使保留全部 p>D 的原成本，理想三层消除的可验证粗上限仍容许跨过 Jensen 的必要门槛。** 本文没有证明这一上限可达到，没有新的无理性结论，也不推广到 tensor、任意 source 或其它解析 metric。

## 1. 严格区分“三层消除”与全部 Smith 余量

沿用 K=Q(√5)、反证假设 c=L(3,χ₅)∈Q，固定 m=4 或7、R=m(D+1)。Shidlovsky 给 N_D=m(D+1)+O(1)，实际消失阶集 V_D 有 R 个元素且包含0,…,D。

对好素数 p>√N_D，Ψ=p³ eval 的全部 n<N_D 系数在原 source 上整。令实际 leading minor 的 Smith 指数为 a₁≤⋯≤a_R。按原 primitive quotient 的有限度量，实际累计有限高度为

\[
 (3R-\sum_i a_i)\log\operatorname{Norm}(\mathfrak p).
\]

定义仅计算三层的成本

\[
 C^{[3]}_{p,D}=\sum_i(3-\min(a_i,3)).                 \tag{1}
\]

它非负，但实际成本可比它更低：a_i>3 是超出清除三层分母的正 Smith 整除性。**LCM 型本身不给这部分任何绝对上限。** 以下上限均指(1)对应的三层收益，不能当作任意算术方法的绝对 no-go。

原粗成本记作 B_p=Σ_{n∈V_D}c_p(n)。对于 p²>N_D，每个 LCM 的 p-指数只有0或1。令

\[
 k_p=\begin{cases}3\,1_{p\le D}&m=4,\\
 1_{p\le D}+1_{p\le2D}+1_{p\le4D}&m=7.
 \end{cases}
\]

原安全型给 c_p(n)=k_p 当 n<p，c_p(n)=3 当 n≥p。Ψ 的该行被 p^{3-c_p(n)} 整除。这也保证 C^{[3]}_{p,D}≤B_p：对任意阶数的 minor，行因子给前 k 个 Smith 指数之和至少为前 k 个排序后行指数之和；再用 Σmin(a_i,3)=min_k(Σ_{i≤k}a_i+3(R-k))。定义三层收益为 B_p−C^{[3]}_{p,D}。

## 2. 不依赖具体算子族的强制 minor

原 constant block 在 Ψ 中给单位倍的 p^{3-k_p}t^j，0≤j≤D。另一方面，冻结 packet 证明给

\[
 p^3gH\equiv t^p\cdot\text{unit}+O(t^{p+1})\pmod p,
 \qquad g=\Delta^2.
\]

首系数是 A(0)(1∓(5√5/4)χ(p))；范数只引入固定例外109，因而可纳入固定坏素数。并未要求新算子，也未假设行仅使用三个 target blocks。

当 √N_D<p≤D 时，constant block 的0,…,D阶与 target shifts 的 D+1,…,D+p阶一起给 mod p rank 至少 D+p+1。实际 minor 仅删去 N_D−R=O(1) 个 prefix rows，故其 rank 仍至少 D+p+1−O(1)。因此

\[
 C^{[3]}_{p,D}\ge3(D+p)+O(1),\qquad
 B_p-C^{[3]}_{p,D}\le3((m-1)D-p)+O(1).             \tag{2}
\]

当 D<p<N_D 时，令 r_p=min(D+1,N_D−p)。选 constant 的低阶 rows 与 target shifts 的 p,…,p+r_p−1阶，所得 block triangular minor 的 determinant valuation 为 (3-k_p)(D+1)。删去 O(1) 个 rows 只改变 O(1) 项。其 determinantal ideal 给

\[
 C^{[3]}_{p,D}\ge k_pD+3\min(D,N_D-p)+O(1).        \tag{3}
\]

这个不等式只利用原格的明确列和最高 packet 的非零首项，故适用于任意 primitive Smith 行族；同时它只给粗上限，未声称 minor 已达到整个矩阵的 Smith 最小值。

## 3. 全素数主项：高幂与固定坏素数不形成 D² 障碍

每个 rational p 的素理想贡献按[K:Q]平均后恰为 log p。令 x=p/D。PNT 将(2)、(3)求和变成积分。原全部有限预算为 rank4 的51/2、rank7 的84（单位均为 D²）。

若只优化 √N_D<p≤D，而**全部 p>D 保留原成本**，该窗口原成本为3mD²，(2)给强制三层成本至少9D²/2。所以可验证的收益粗上限为

| 固定 source | 三层收益上限 | 剩余有限预算下限 | 乐观有效成本下限 | Jensen 所需ρ的乐观下限 |
|---|---:|---:|---:|---:|
| rank4 |15/2|18|15/8|5/2|
| rank7 |33/2|135/2|93/49|31/14|

这里有效成本仍按原源 degree 的常数项3、21及原 arch 系数计算。下限不是已达到的成本；最后一列低于 log16 只说明这个粗 ceiling 没有排除成功。

若允许全部 √N_D<p<N_D 的三层窗口，用(3)还可算得更宽的粗上限。rank4 的强制成本函数为：0<x≤1 时3(1+x)，1<x≤3 时3，3<x≤4 时3(4-x)；积分为12。rank7 的函数为：0<x≤1 时3(1+x)，1<x≤2 时5，2<x≤4 时4，4<x≤6 时3，6<x≤7 时3(7-x)；积分为25。因此

\[
 G^{[3]}_{4,D}\le(27/2+o(1))D^2,\qquad
 G^{[3]}_{7,D}\le(59+o(1))D^2.                     \tag{4}
\]

相应乐观有效成本下限仅为9/8、8/49。它们也不是可达到性断言。特别是 **p>D 不是已证明的不可去除成本**；它只是当前全局稿保留的主要未处理预算（rank4 为27D²/2，rank7 为63D²）。

小素数 p≤√N_D 的一次幂原成本为 O(D^{3/2})；所有 k≥2 的 prime powers 由 ψ(CD)−θ(CD)=O(√D log D) 给 O(D^{3/2}log D)。每个固定坏 p 的全部高幂及原分母贡献为 O(D log D)。固定 D_c 只有 O(D)。这些全部保留，却都是 o(D²)；不能用它们制造一个正的 D² 成本下限。

## 4. 当前仍有的算术窗口

若从原有限预算分别扣除 G D²，原 source 与 metric 不变，则普通 Jensen 冲突在 ρ≤log16 下至少要求

\[
 G>45/2-6\log16=5.8644676665\ldots\quad(m=4),
\]
\[
 G>63-21\log16=4.7756368329\ldots\quad(m=7).       \tag{5}
\]

原已审两层收益是 G=3/4。root/conjugate 正在独立核验的平方提升与 degree≤3p+20 二阶行将第二层收益从1/12提高至1/6，预期总 G=5/6；即使采用这一新数，两者距离(5)仍大。本稿的 ceiling 不依赖该新行。只用 p≤D 的粗 ceiling 已分别为7.5与16.5，均高于(5)。因此**无法据固定账本宣告“三层再怎么改也不够”**；真正未决的是可构造的 primitive 行、它们的次数损耗与相对于完整 source 的 Smith 斜率。rank4 的窗口较窄：保留全部 p>D 成本时，上限与所需收益只差1.6355323334…；rank7 的粗窗口较宽。

精确达到 log16 或 J=ρ 也没有证明；真实 covering 的可用解析值可能低得多。(5)只是用最有利解析端筛选算术路线的必要条件，不是充分条件。

本稿的计算依据为冻结原格、全前缀 packet、实际 leading-order 覆盖、Smith determinantal ideals 与 PNT；常数另用有理算术核对。helper_tensor_budget 独立认可(2)的 rank 输入及15/2、33/2积分，并提醒实际剩余 graded 高度可以为负；此提醒已体现于§1的严格 scope。没有改动任何冻结研究稿。
