# 第271轮独立一手来源核查

2026-10-20。子代理 `new_primary_271`；不改状态账，不运行数学扫描或外部 Lean 构建。本稿只记录实际读到的新来源及版本纠正，不认证完整外部证明。

准入目标仍是**新的明确指定实 ζ/Dirichlet L 值或组合**，不是既有 ζ(5)/Catalan 基线或“集合中至少一个”。开始时 goal 工具返回 null；`research_state.py show` 显示271宏观窗口进行中，初始 `git status --short` 为空。

## 1. Lai v2 是旧源版本核对

[arXiv:2610.06838v2](https://arxiv.org/html/2610.06838v2) 于10月15日修订；[v1](https://arxiv.org/html/2610.06838v1) 已在项目240、244及10月6日 H9 独审中出现。定点核对(2.2)–(2.12)、Prop3.1、(4.8)–(4.22)、Prop5.5和§6，原对象及辅助素数块未变：

\[
 R_n=\frac{(6n)!^2}{(2n)!^3}\frac{(t-2n)_{2n}^3}{(t)_{6n+1}^2},\quad
 \mathcal L_n(P)=-3a\sum(R_nP)'(m)+b\sum(R_nP)''(m).
\]

原生向量为 \((1,\zeta(3),\zeta(4))\)。\(\sum A_{1,k}=0\) 消低权；假设 \(a\zeta(3)+b\zeta(4)=c\) 后完整调和头有理。Prop3.1 的无限非零依赖 \(b\ne0\)、\(q\equiv1\pmod9\) 及二维块行列式 \(-4b^2b_j^2\)。全素数合计下界仍为 \(-30.83n^2+o(n^2)\)。

版本差别不能说成完全无文字数学修订：v1 Prop6.6 陈述写31，引言写31.6，而证明已给 \(c_3=31.614437\ldots\)；v2把陈述统一为31.61，并把Prop5.5的任意 \(\varepsilon\) 具体化为30.84。\(c_3\) 的两种表达由互补反正切及对数恒等式相同，未产生新机制。

项目已有H9覆盖固定高权的无限非零；所以升到 \((1,\zeta(4),\zeta(5))\) 不能再登记为新来源或新非零首证书。仍欠该实际高权对象的全素数 minor/content 费用及同归一化实衰减，不能转移30.83/31.61的差额。

## 2. 实际新检出来源：β(2)以外的有限集合

作者 [Hexagon 2610.00285v2](https://hexagonmath.org/pdf/2610.00285v2)，2026-10-16，34页。实际定点读§§1–3、Lemma4.6/Prop4.8、Cor5.9、Prop6.6、Cor7.13、§§8–10；没有逐项复核全部算术/鞍点证书。

完整向量为 \((1,\beta(4),\beta(6),\ldots,\beta(36))\)。\(n\in480\mathbf N\)，二阶导数删去β(2)，对称性删去奇权。论文的 \(D_n\in\mathbf Q_{>0}\) 允许负素数指数；不是未经约分的整数LCM。它将全部常数栏及周期系数清成整数。所报预算为

\[
 \log D_n\le G\log(n!)+(A+20\log2+o(1))n,
 \quad\log|L_n|\le-G\log(n!)+(-29.76+o(1))n,
\]
\[
 G=179/10,\quad A=15.8256549806\ldots,\quad Q=-0.0714014\ldots<0.
\]

非零来自鞍点相位，Cor7.13说充分大时相邻 \(L_n,L_{n+480}\) 不同时零。Lemma4.6 的真实算术机制是 \(R_n''(-\ell)=0\) 将常数头尾互换；\(p>n\) 不能同时污染两侧，故整性覆盖有理头。这是完整packet机制，未给单值隔离。

作者实际有理函数是
\[
R_n(t)=\frac{(2t+n+1)\prod_{\ell=-(1+r)n-1}^{rn}(t-\ell)^3}
 {\prod_j\prod_{k=\delta_jn}^{(1-\delta_j)n}(t+k+1/2)^{m_j}},
\quad r=7/6,
\]
其中 \((\delta_j,m_j)=(0,8)\)，另有 \((\kappa/160,1)\)，\(\kappa=1,\ldots,8,10,12,\ldots,46\)。总multiplicity为35，\(R_n(-n-1-t)=R_n(t)\)。原文Remark2.3仅讨论一般布局的奇偶条件；本文全部预算只实施这组参数，未给可随意取最高权4的定理。

固定 formal 身份已通过 GitHub connector 读取：[commit f8df497467901e09fa497553f00d8ffa4480a46d](https://github.com/telaviv/beta-irrationality/commit/f8df497467901e09fa497553f00d8ffa4480a46d)。实际全文读该commit的 `Defs.lean`、`Statement.lean`、`I3/MainCond.lean`、`I3/MainUnconditional.lean`。最后声明精确为

\[
 \exists j\in\{2,\ldots,18\},\quad\operatorname{Irrational}(\beta(2j)).
\]

未构建依赖，也未独立验证作者的kernel/axiom声明。读取定义与最终定理足以确认：它没有声明指定β(4)或指定固定组合无理。

**准入判断：不准入数值实施。** 要用于当前目标，尚须对同一packet给固定目标投影、消元后的全部清整、实际无限非零及保留严格负净率；原集合反证中的一个共同分母不能支付这些接口。发现新论文或一组β值有负率，都不授权重开旧窗口。

### 2a. 我们纸面可迁移的部分及低阶布局边界

以下是本次独立推导，不归给作者的β(36)结论。设proper rational \(R\) 的极点仅为 \(-k-1/2\)，\(0\le k\le n\)，其partial fraction系数 \(a_{i,k}\) 在奇素数 \(p>n\) 时均p整，且 \(R''(-\ell)=0\) 对 \(1\le\ell\le n\) 成立。定义
\[
T(\ell,k)=\sum_i a_{i,k}i(i+1)(k-\ell+1/2)^{-i-2}.
\]
则 \(\sum_{k\ge\ell}T(\ell,k)=-\sum_{k<\ell}T(\ell,k)\)。若两侧分别有p坏分母，便有两个不同 \(k_1,k_2\in[0,n]\) 满足 \(p\mid k_1-k_2\)，与奇素数 \(p>n\) 矛盾。因此两侧均p整。这一引理不内在要求最大pole order35；2处不由该论证支付。

若最大pole order≤3，且 \(R(-n-1-t)=\varepsilon R(t)\)、\(\varepsilon=(-1)^n\)，反射给 \(a_{i,n-k}=\varepsilon(-1)^ia_{i,k}\)。二阶导天然没有β(2)，而奇i周期栏相消，只余 \((1,\beta(4))\)。例如
\[
R_n^0(t)=\frac{\prod_{j=1}^n(t+j)^3}{\prod_{k=0}^n(t+k+1/2)^3}
\]
在奇n时有degree −3及所需反射sign；偶n时乘 \(2t+n+1\) 得degree −2及所需sign。这只付精确投影与上述 \(p>n\) 有理头整性，未付非零和严格预算。

还有一个限制同一literal polynomial-Hankel接口的全尺度度数障碍：若保留每个 \(-1,\ldots,-n\) 的三重零、极点仍限于上述n+1个位置且每个order≤3，则分子degree≥3n，分母degree≤3(n+1)，所以 \(\deg R\ge-3\)。大小h的monomial Hankel需要最高矩 \(t^{2h-2}R\)，其degree≥2h−5。为了 \(\sum_{t\ge0}(-1)^t(t^{2h-2}R)''(t)\) 的项趋0，其多项式商部必须degree≤1，故h≤3。

此外，scalar的反射投影不能自动传给 \(t^{i+j}R\)：一般monomial会恢复奇权栏。若用中心 \(x=t+(n+1)/2\) 的偶多项式池保持 \(PQ\) 反射偶，最高degree为 \(4(h-1)\)，同一度数论证进一步给h≤2。因而简单把作者35改3不能保留h随n增长。这个限定障碍不覆盖正规化泛函、多项式商部的新评价规则或其它有理基池；这些接口均需另付，本文来源没有替它们付预算。

## 3. 其它实际读域与结论

[Sun 2609.04176v1](https://arxiv.org/html/2609.04176v1) 仍仅列9月3日版本；定点读其§§6、9和[Wachs 2609.22339v1](https://arxiv.org/html/2609.22339v1) §§1–3。Wachs的精确分解保留 \(v_2(F_{2B})\log2=(2\log2)B^2+O(B\log B)\)，并明确有限计算本身不反驳渐近命题。这里只确认该特定Sun预算仍有未付接口，不将质疑转移到另一个独立Catalan来源。

定向检索覆盖2026年实奇ζ、固定组合、Dirichlet L及Hankel来源；没有发现超出上述范围且可付指定数值预算的新候选。这是有界实际检索结论，不是全球文献穷尽或所有方法no-go。未重读269已审VM/Eskandari/GKS/GZ/KZ，也未把p-adic Hurwitz新题目当实同值桥。
