# 第242轮C：完整余项分级整内容与Root强证明独审

2026-10-09。本新伴随稿不修改已经冻结的9354-byte外层基线或其scope。**实际FULL独审 Root 强证明 PASS，无必要数学修订**；下文给独立纸证及全宏观profile核对。数学程序0，无新搜索或下载。全素数预算<6与实处−6完整认证仍未付。

## 1. 读取身份与固定对象

已实际 FULL 读 research/logistic_gauss_graded_head_round242_20261009.md：**9113 bytes**，SHA256 **1daeea8510afa88179d877bbd1a68481ea225d06b4020156411120fd09d46ca5**，全部六节及H1–H15、九段profile。本文独立核其完整余项整性、rank限制、全系数预算和范围。不以代理消息或本文作者读冒充该FULL独审。

采用同一 R_n=D_n⁴/D_(5n)、h=3n、S_n=(5n)!/(n!)⁴、F_n=∏_(i<h)(i!)²及完整K5泛函。以λ_j=Res_(−j)R_n、ω_j=S_njλ_j，完整池的有理矩是
\[
 U_T(t^eR_n)=L_e+\sum_jj\lambda_j(-j)^e(T-3H_j^{(3)}-H_j^{(5)}),
\]
\[
 L_e=\tfrac32B^+((tq_e)')+\tfrac1{24}B^+((tq_e)'''),
 \quad t^eR_n=q_e+\sum_j\lambda_j(-j)^e/(t+j),\quad q_e\in Z[t].
\]
所有商部和全部调和头均保留。固定 p≥11、n<p≤5n，s=⌊5n/p⌋≤4、τ=5n−sp、R_s=max(1,s−1)，则 v_p(S_n)=s。基线O4中的完整余项为
\[
 W_{ik}(T)=S_nL_{i+k}+\sum_j\omega_j(-j)^{i+k}(T-3\eta_{3,j}-\eta_{5,j}),
 \quad\eta_{r,j}=\sum_{1\le u\le j,p\nmid u}u^{-r}.
\]
本稿证明 **全部系数** W(T)∈p^(R_s)M_h(Z_p[T])，不只证明某个T的值。

## 2. 所有残数矩的整性支付类内分级

R_n=t^(−n)乘Z[[t^(−1)]]中的级数，因为整数首一分母的形式反演保留整数系数。有限部分分式在∞展开后，对于每个e≥0都有
\[
 a_e=\sum_jj\lambda_j(-j)^e=-[t^{-2}]t^eR_n\in Z.
\]
商部不贡献负次幂。因此对每个P∈Z[t]，Σ_jω_jP(j)∈S_nZ。这里允许任意次数P，是有限代数恒等式，不扩大实际列池，也不产生额外函数源或basis费用。

固定残数类b，取 E_b(t)=1−(t−b)^(φ(p^s))。φ(p^s)≥s；Euler定理给它在整数j上恰为模p^s的class indicator。对 E_b(t)(t−b)^ℓ应用上式：
\[
 p^\ell\sum_{j=pm+b}\omega_jm^\ell\equiv0\pmod{p^s},
 \qquad v_p\left(\sum_{j=pm+b}\omega_jm^\ell\right)\ge s-\ell. \tag{C1}
\]
类内求和包含实际全部节点：b=0不省略，b>n时m=0的低节点也不省略。ℓ≥s的弱界仍成立；高次系数自身含p^s，最终只需ℓ<s。高次数indicator仅用于证明已存在内容，不是对实际矩阵作付费变基。

## 3. 全部非p调和头的分级抵消

写j=pm+b，0≤b<p。严格有限求和给
\[
 \eta_{r,pm+b}=\sum_{a=0}^{m-1}\sum_{u=1}^{p-1}(pa+u)^{-r}
       +\sum_{u=1}^{b}(pm+u)^{-r}.
\]
对单位u展开到k=s−1，余项逐节点含p^s：
\[
 \eta_{r,pm+b}\equiv\sum_{k<s}p^k\binom{-r}{k}
       \left[S_{r+k}\sum_{a=0}^{m-1}a^k+H_b^{(r+k)}m^k\right]\pmod{p^s},
 \quad S_v=\sum_{u=1}^{p-1}u^{-v}. \tag{C2}
\]
r=3或5、k≤3，所以3≤r+k≤8<p−1，有限域单位逆幂和给 S_(r+k)∈pZ_p。可以不借原论文的局部深度：若0<v<p−1，某个c∈F_p×满足c^v≠1（多项式次数v的根不足p−1），乘法置换单位求和即得S_v=0 modp。

k=0,1,2,3的 Faulhaber 多项式依次是m、m(m−1)/2、m(m−1)(2m−1)/6、m²(m−1)²/4，故分母全是p单位。完整循环项的前因子至少p^(k+1)，多项式次数至多k+1；部分循环项次数k、系数至少p^k。因此(C2)的m^ℓ系数至少p^ℓ。(-pm−b)^e的m^ℓ系数也至少p^ℓ；两个这种分级多项式相乘仍满足同一条件，不论e的大小。

乘上ω_j、分残数类求和，逐个m^ℓ项用(C1)，每项至少p^s。≥s次项及(C2)余项直接含p^s，乘整数ω_j与j^e不损层。因此
\[
 \boxed{\sum_j\omega_j(-j)^e\eta_{r,j}\in p^sZ_p,
       \qquad r=3,5,\ e\ge0.} \tag{C3}
\]
目标T系数Σ_jω_j(-j)^e=S_na_e同样含p^s。此处抵消的是完整非p调和头的加权和，不是假设每个ω_j或每个η_j都具有额外深度。

## 4. 商部不能删除；s=1的特殊补层

一般Bernoulli valuation≥−1，故S_nL_e至少含p^(s−1)。当s≥2，这就给R_s=s−1。

当s=1，实际商部P=tq_e的次数≤5n−1≤2p−2。一阶单项式矩为dB_(d−1)^+；若正Bernoulli指数为k(p−1)，d=k(p−1)+1。k=1的d=p由微分因子补p，第一个可能未抵消的d=2p−1超出范围。三阶矩为(d)_3 B_(d−3)^+；k=1,2,3分别对应d=p+2、2p+1、3p，falling factorial都含p，第一个可能未抵消的d=4p−1更超出范围。B_0、B_1的分母为p单位。因此L_e本身p整，S_nL_e至少含p。

结合(C3)及目标系数，得到
\[
 \boxed{W(T)\in p^{\max(1,s-1)}M_h(Z_p[T]).} \tag{C4}
\]
这验证Root H3/H10/H11，且解释为什么不能仅以“微分杀degree<3”删除整个商部。p≥11保证循环逆幂和所需的指数范围；不把此强界移到固定小素数7。

## 5. 总rank限制和全系数费用

基线保留的高头更新仍是
\[
 S_nM_n=W(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\qquad
 \gamma_j=-p^{-5}\omega_j(H_{\lfloor j/p\rfloor}^{(5)}+3p^2H_{\lfloor j/p\rfloor}^{(3)}).
\]
同类节点数 C_b=s若b≤τ，否则s−1；其ω valuation精确为ν_b=2[b=0]+[b>τ]+4[1≤b≤n]。使用k_b个同类外积，两个交替minor支付k_b(k_b−1)；余(h−Σk_b)阶W minor由(C4)支付R_s(h−Σk_b)。因此
\[
 g_p(\det(S_nM_n))\ge R_sh+
 \min_{0\le k_b\le C_b,\ \sum k_b\le h}
   \sum_b\{k_b(\nu_b-5-R_s)+k_b(k_b-1)\}. \tag{C5}
\]
这是Root H14的独立证明。各类的递增slot为ν_b−5−R_s+2ℓ；选择全局至多h个最小负slot自动遵守每类prefix。删去Σk_b≤h只会使下界更安全。

保留F_n的精确量 v_p(F_n)=2((3n−p)_++(3n−2p)_+)；在Q_n≠0的尺度定义primitive比例d_n，则
\[
 v_p(d_n)\le v_p(F_n)-R_sh
  -\sum_b\sum_{\ell<C_b}\min(\nu_b-5-R_s+2\ell,0). \tag{C6}
\]
这是全部T系数结论，包含Sn/Fn；负费用必须保留，不能截成每处正LCD。

独立按s=4、3、2、1计数后，负slot数量的leading值分别是(3x−1)n、(4−x)n、(4−x)n或xn、(5−x)n，其中x=p/n；最大≤(11/4)n+O(1)<3n。因此总rank限制对充分大n的宏观leading没有额外改善。特别s=3、3/2<x<5/3时，τ<n，精确leading计数是2(p−n)+2τ+(n−τ)=4n−p；Root消息中5及13−5x的节省无效，最终稿撤回正确。小n可直接保留(C5)；本稿不作样本计算。

全九段费用upper及手算积分核对如下，均已包含F_n与R_sh：

| x | upper/n | 积分 |
|---|---|---|
| 1…5/4 | 2+x | 25/32 |
| 5/4…4/3 | 20−11x | 139/288 |
| 4/3…3/2 | 8−2x | 31/36 |
| 3/2…5/3 | 2+2x | 31/36 |
| 5/3…2 | 20−7x | 43/18 |
| 2…5/2 | 4+x | 25/8 |
| 5/2…3 | 29−8x | 7/2 |
| 3…4 | 23−6x | 2 |
| 4…5 | 7−2x | −2 |

分母288的九项分子为225、139、248、248、688、900、1008、576、−576，合计3456/288=12。3<x<5的净积分是0，确实不同于基线的4。通常PNT加有限分段Stieltjes求和给
\[
 \sum_{p>n}v_p(d_n)\log p\le(12+o(1))n^2 \tag{C7}
\]
（充分大n使p>n时p≥11；p>5n基线已付系数整）。primitive仅在Q_n≠0尺度使用，241的无限prime-edge尺度满足此条件。此处不另声称每个n的Q_n非零。

## 6. 审阅范围及下一缺口

Root H1–H15数学链、全部profile及撤回错误节省均核通过，**PASS**。仍可能存在剩余整Schur determinant的额外内容；(C6)/(C7)都是费用upper，不能把12大于6或某个选定profile不足升为actual费用lower/no-go。

Root/B通信中的全部prime upper1009/40由inner529/40加本外层12而来；本文只独立支付外层12，没有实际FULL审A/B最终小素数、inner或总预算稿，故不以通信值冒称本人完成全prime独审。p≥11范围、固定小素数另付及实处−6未独立认证等边界与Root最终稿一致。没有新数值无理性结论。应研究同一完整商部/剩余过滤determinant的真实内容；不重新扩大241已完成的非零样本。
