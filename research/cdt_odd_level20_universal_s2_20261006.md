# 通用二层行的次数下界与实际源的短关系

日期：2026-10-06。本稿限定两个问题。第一，对所有 Frobenius 源成立的全形式 order≤2 primitive 二层行，其最高系数必须含 Hasse 双根平方，故次数领先项不能小于3p。第二，实际 odd Eichler packet 没有统一固定次数的一阶短关系；固定 p=7,11,13 的最短一阶关系也已核验。两者均不排除实际 packet 的特殊消除、随p增长的关系、有限jet方案或tensor构造；未得到新数值无理性结论。

## 1. 明确的通用族

使用 [Hasse稿](cdt_odd_level20_hasse_20261006.md)、[Frobenius稿](cdt_odd_level20_frobenius_20261006.md) 及 [低次数平方提升](cdt_odd_level20_square_lift_20261006.md)。取p≥7的好place，系数DVR为O_{K,𝔭}，residue field为k。ϑ=t d/dt，s=t(q(t)^p)，且

\[
\vartheta s=psb,\quad b=S(s)/S(t),\quad S=g_s\Phi,
\quad A=-k_A S/5,\quad k_A=N/[(1-t)\sqrt{C_o}].
\]

此处 k_A 是gauge，字母k是residue field。记

\[
a=\vartheta\log k_A,\quad z_S=\vartheta\log S,
\quad\alpha=\vartheta\log A=a+z_S.
\]

考虑p-integral polynomial row

\[
L=c_2(t)\vartheta^2+c_1(t)\vartheta+c_0(t)
\]

并要求 **对每个 W(z)∈O_{K,𝔭}[[z]]，全形式级数** L[A(t)W(s(t))]∈p²O[[t]]。primitive指c_i不全在p中。即使只要求所有zero-constant W，下述结论仍成立。这里不讨论只对某一个实际W或有限前缀成立的行。

## 2. 两个必要 rational identities

令W_j=ϑ_z^jW。展开并除以unit A：

\[
L[AW(s)]/A=K_0W(s)+K_1W_1(s)+c_2p^2b^2W_2(s),
\]

\[
K_0=c_0+c_1\alpha+c_2(\vartheta\alpha+\alpha^2),\qquad
K_1=pb[c_1+c_2(\vartheta\log b+2\alpha)].
\]

用W=1,z，或在zero-constant族中用W=z,z²，得到K₀≡K₁≡0modp²。s=t^p·unit是nonzero divisor，故全形式下可除去其幂。又

\[
\vartheta\log b=pbz_S(s)-z_S\equiv-z_S\pmod p.
\]

因此必要条件为

\[
\boxed{\bar c_1=-\bar c_2(2a+z_S),\qquad
\bar c_0=\bar c_2(a\alpha-\vartheta\alpha).} \tag{1}
\]

等式在k(t)中成立：所有原点分母为unit，清分母可把全形式恒等式injectively转换成rational identity。若\(\bar c_2=0\)，两条迫使\(\bar c_1=\bar c_0=0\)，违反primitive。因此通用primitive二层行必有非零order2 leading coefficient；order≤1不能承担这种通用二层任务。

## 3. 每个 generic double root 强制平方

令P=P_p，H=gcd(P,P′)monic，B=P/H²；此处H为polynomial。Hasse除子给

\[
H\text{ squarefree},\quad B\mid\Delta,\quad
2\deg H+\deg B=3(p-1),\quad\deg B=b\le4.
\]

取H的任一几何根ξ，u=t−ξ。它避开cusp、Δ=0。modp下z_S的logarithmic residue为2。若N也在ξ为零，记其重数m∈{0,1,2}；固定gauge的其它因子在该处为unit。所以

\[
a=m\xi/u+O(1),\quad z_S=2\xi/u+O(1),
\quad\alpha=(m+2)\xi/u+O(1),
\]

\[
a\alpha-\vartheta\alpha
=\frac{(m+2)(m+1)\xi^2}{u^2}+O(u^{-1}).
\]

ξ≠0，而p≥7使2、6、12均非零。(1)中的\(\bar c_0\)是polynomial，故\(\bar c_2\)在ξ至少二阶零。包含N∩H的情况，无需排除这些根。得到

\[
\boxed{H^2\mid\bar c_2,\qquad
\max_i\deg c_i\ge\deg\bar c_2\ge3(p-1)-b\ge3p-7.} \tag{2}
\]

现有平方提升二层行的上界3p+b+16与此下界仅差2b+19≤27。故其领先次数3p在本通用全形式、order≤2族中已最优。式(2)不能用于否定实际special W或finitejet的更小行。

## 4. 实际 f_± 没有 characteristic-zero 一阶标量线

实际源为\(F_{p,\pm}(z)=(u\mp\sqrt5\chi(p)v)\circ q(z)\)的degree<p截断。它随χ(p)仅取两个固定characteristic-zero families f_−、f_+。

由 [真实周期稿](cdt_odd_conjugate_projection_20261005.md) 及 [canonical α continuation](cdt_odd_level20_leaf_20261006.md)，同一个实际芽满足

\[
f_-+20\tau^2 f_-(W_{20}\tau)=\Theta(1+20\tau^2),
\]

\[
f_+-20\tau^2 f_+(W_{20}\tau)=-\Theta(1-20\tau^2),
\quad\Theta=-5\sqrt5L(3,\chi_5)/16\ne0.
\]

两者在τ→i∞时都趋0，且不是零函数。若某f满足C(t)上一阶scalar differential equation，沿t-return的canonical α loop，monodromy只能给f(W₂₀τ)=λf(τ)，λ∈C×。上式分别迫使

\[
f_-={\Theta(1+20\tau^2)\over1+20\lambda\tau^2},\qquad
f_+=-{\Theta(1-20\tau^2)\over1-20\lambda\tau^2}.
\]

τ→i∞的极限为Θ/λ、−Θ/λ，均非零，矛盾。因此任何固定degree的一阶polynomial relation在characteristic zero都不存在。

## 5. 固定degree的modp源关系只能发生有限素数

固定d。无characteristic-zero一阶关系意味着有限列 \(t^jf_\pm,t^j\vartheta f_\pm\)（0≤j≤d）具有full column rank的某个有限Taylor matrix，存在非零K-valued minor。排除该minor和有限系数分母所涉及的有限place后，reduction仍full rank。

当p大于这个固定jet cutoff，degree<p的真实源截断保留全部这些jets；χ(p)只切换上述两个fixed families。因此对每个固定d，只有有限好素数可能有degree≤d的非零一阶source polynomial relation。**不能令d或jet cutoff随p改变，再套此论证。**

每个具体packet仍有自动的一阶关系。令g=gcd(F,ϑ_zF)，则最短primitive row为

\[
(F/g)\vartheta_z-(\vartheta_zF/g),
\quad\delta_F=\deg F-\deg g.
\]

对非零packet，degF<p使ϑF在原点的零阶与F相同，故F/g常数为unit。直接使用其log derivative并拉回s≡t^p modp时，reduced denominator degree是pδ_F；Bézout identity保证代换后仍coprime。上述固定d结论表明δ_F不能统一有界，所以这种直接完整log derivative的清分母不会保持O(p)。这只描述该直接方案；未排除与Hasse因子、不同packets的特殊抵消。

## 6. 既定source检查及开放范围

[精确脚本](cdt_odd_level20_universal_s2_20261006_verify.py) 在既有t坐标重新构造完整degree<p source，固定p=7、11、13，检查两families及每个residue place，没有扫描参数。

|p|最短一阶source coefficient degree δ_F|直接pullback denominator degree|
|---|---:|---:|
|7|5|35|
|11|8或9|88或99|
|13|11|143|

p11其中两组有一个额外重复根，已用实际gcd计算保留，而未假定所有packet squarefree。共43项精确检查。有限数据仅核查这些实际短关系；(2)及固定d有限例外结论来自上述证明。

下一缺口被限定到实际packet特有的增长degree关系、跨packet抵消、finitejet构造、balanced tensor或不同large-prime窗口。本稿不能把通用行的领先最优性升级为全部无理性方法的障碍。

helper_tensor_budget 已独立重推 §§1–3（包含N与H相交）及 §§4–5 的fixed-degree一阶排除；其意见明确依赖此前已证canonical α loop和真实周期，且不外推到随p增长的关系。本稿脚本由作者执行。
