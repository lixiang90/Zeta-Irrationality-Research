# 第241轮：K5完整系数的prime-edge Gauss费用

2026-10-09，A独立纸面推导与核读；文件标签沿用20261008。本人数学程序0。
固定240对象 X=3ζ(3)+ζ(5)，保留完整Bernoulli商部及全部调和头。
本轮已有实际无限非零；新增费用结论仅在n=p−1的这个辅助素数处精确，
不是全素数净费用或新的数值无理性定理。

## 1. 原源能复用的接口与不能复用的尺度

记D_m(t)=∏_(j=1)^m(t+j)，R_n=D_n⁴/D_(5n)，h=3n。
Bernoulli泛函B⁺取B_1⁺=1/2。若G=P+Σ_j c_j/(t+j)，定义
\[
 V_r(G)=B^+(P^{(r)})+(r+1)!\sum_jc_jH_j^{(r+2)},\qquad r=1,3.
 \tag{A1}
\]
真实完整entry为
\[
 U_T(f)=\tfrac32V_1(tf)+\tfrac1{24}V_3(tf)-T\sum_jc_j,\qquad
 Q_n(T)=\det[U_T(t^{i+j}R_n)]_{i,j<h},
 \tag{A2}
\]
其中c_j是tf的残数；T=X时等于240的实际泛函。对简单极点，
U_T((t+j)⁻¹)=jT−j(3H_j³+H_j⁵)，包含全部heads。

本轮FULL读固定commit的Arith/Local Entry、Val、Binom和PrimeEdge
Basis、Local、Index、EntryBounds、Valuation、Reduction；另FULL读
PoleFun及既存LocalShape、Gram。原源的class-wise division、CRT unit
basis、Gauss系数determinant bound及primitive reduction可按定义复用。
原K3 entry的β−2、同类base(−5,−3,−2)和旧固定块不能复用：
三阶导数给p⁻⁴与H⁵，须重新付β−4及新块。
这不是Lean执行或全仓库证明认证。

## 2. 独立all-entry引理：β−4和target系数β+1

设p≥7，5n<p²，G=A/D_(5n)，degA≤10n−1。对每个整数m，
假设A(m+pu)的全部系数valuation至少E_[m]；ℓ_c为同类负整数
极点的个数。令β=min_c(E_c−ℓ_c)。
则G的简单残数满足v_p(c_j)≥E_[-j]−ℓ_[-j]+1≥β+1：
同类任意两个不同极点之差恰含一个p，其它差是单位。
所以A2的target系数至少β+1，H³/H⁵部分分别至少β−2、β−4。
以下付清商部，不能只给残数bound。

写G=P+Σ c_r/(t−r)。固定整数m，分极点为同类C和其它类O；
也用C、O表示对应首一乘积。令
I=Σ_(r同类)c_r∏_(s同类,s≠r)(t−s)，
H=P O+Σ_(r异类)c_r∏_(s异类,s≠r)(t−s)。
部分分式恒等式是A=C H+O I。替换t=m+pu后，OI的每一项至少
(E_[m]−ℓ_[m]+1)+(ℓ_[m]−1)=E_[m]，所以CH至少E_[m]。
C(m+pu)=p^ℓ乘以具有整数根的首一多项式。p-整多项式的首一除法
保整，故H(m+pu)至少E_[m]−ℓ_[m]。O(m)是单位，异类残数除以
m−r也都是单位分母，于是P(m)至少β。这包括m正好是极点，
并未在极点处评价原有理函数。

商部degree d≤5n−1，d+1<p²。整数值的前向差分给Newton展开
P(t)=Σ_(k=0)^d z_k binom(t,k)，每个z_k至少β。由
\[
 \partial_t\binom tk
 =\sum_{j=1}^k\frac{(-1)^{j-1}}j\binom t{k-j},
 \qquad B^-\!\left(\binom tk\right)=\frac{(-1)^k}{k+1},
 \quad B^+=B^-+[t^1],
 \tag{A3}
\]
每次微分最多损一个p，B⁻最多再损一个p；[t¹]P^(r)等于
P^(r+1)(0)，也最多再损一个p。因此
\[
 v_p(B^+(P'))\ge\beta-2,\quad
 v_p(B^+(P'''))\ge\beta-4,\quad
 v_p^{\rm Gauss}U_T(G/t)\ge\beta-4.
 \tag{A4}
\]
固定3/2、1/24在p≥7处是单位。A3微分式来自
(1+z)^t log(1+z)的系数比较；Bernoulli式来自其生成函数。
这是完整entry的引理，不是安全LCD或有理点抽样。

## 3. actual n=p−1的新归一化与单位块

完整CRT列池为
\[
 \phi_{b,i}=(t+b)^i\prod_{d\ne b}(t+d)^{m_d},\quad
 m_0=4,\quad m_b=3\ (1\le b\le p-5),\quad
 m_b=2\ (p-4\le b<p),\quad 0\le i<m_b.
 \tag{A5}
\]
尺寸3p−3，基变换det是p-unit。local numerator E_d为
e_d+z_a(d)+z_c(d)，e_0=1、其它e_d=4。三阶最高层的base是
c'_b=e_b−ℓ_b−4=(−7,−5,−4)，ρ_(b,i)=c'_b/2+i。
完整greedy class比较给β_ac≥ρ_a+ρ_c+4。
A4给所有entry系数至少ρ_a+ρ_c，而target系数至少
ρ_a+ρ_c+5，独立核对Root完整证书的这一系数层。

单靠A4尚不能确定常数项unit。本人已FULL逐式核
[Root完整证书](logistic_prime_edge_full_certificate_round241_20261008.md)
五节：先精确保留商部，再对每个near/far极点截断，误差至少β；
同类主项是p⁻⁴V₃/24，其它阶与Taylor correction至少多一个p；
异类归一化余量至少1/2。所有far调和头均进入证明。
没有把仅多项式的Bernoulli multiplication当完整distribution。

三个新固定块的主函数分别为
u/∏_(j=1)^4(u+j)、u³/∏_(j=1)^4(u+j)、u³/∏_(j=1)^3(u+j)，
sizes4、3、2。本人FULL读C的D1–D11及Root唯一producer/output：
\[
 \det M_0=541936393813/62208,\quad
 \det M_L=-100344353231/3888,\quad
 \det M_H=-210779/4.
 \tag{A6}
\]
未除24的约定一致；前两个块右下角商部贡献6不可丢。
我用有限节点公式核C的分解，未重跑程序。排除
E={2,3,5,19,59,131,1609,2953,7477,706337,3110519}后，
全部固定块是单位。Root程序只算这三个固定矩阵，不是prime扫描。

## 4. 完整polynomial Gauss valuation与无限非零

给row/column同时乘p⁻ρ，剩余域矩阵是与T无关的unit block直和；
每个target系数至少含p⁵。可在Q_p(√p)中归一化，最终系数仍在Q_p；
或直接对每个determinant permutation使用有理halfweight下界。
交叉项的正半层不能进入leading reduction。总指数为
\[
 \Lambda=2\sum\rho
 =4(-7)+12+(p-5)(-15+6)+4(-8+2)=5-9p.
 \tag{A7}
\]
因此p≥7且p∉E时，
\[
 v_p([T^0]Q_{p-1})=5-9p,\qquad
 v_p([T^k]Q_{p-1})\ge5-9p+5k.
 \tag{A8}
\]
这是整个有理系数polynomial的Gauss证书。设P_n=d_n Qtilde_n
为primitive整数polynomial。primitive的系数在每个p处的最小
valuation是0，故P_(p−1)常数项是单位，其[T^k]至少含p^(5k)。
每个固定q∈Q只需另排p|den(q)，P_(p−1)(q)就为p-unit。
坏素数集合有限，因此同一实际关系点在无限无界n=p−1上非零；
不以formal determinant或有限头代替非零。

## 5. S_n、F_n必须共同计费

沿用实际对象
\[
 S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{3n-1}(i!)^2,\qquad
 \widetilde Q_n=S_n^{3n}Q_n/F_n.
 \tag{A9}
\]
p≥7,n=p−1时所有阶乘参数小于p²，因此
\[
 v_pS_n=4,\quad
 v_pF_n=2\sum_{i=0}^{3p-4}\lfloor i/p\rfloor=6p-12.
\]
归一化scalar的valuation是4(3p−3)−(6p−12)=6p。故
\[
 \boxed{v_p^{\rm Gauss}\widetilde Q_{p-1}=5-3p},\quad
 v_p([T^k]\widetilde Q_{p-1})\ge5-3p+5k,\quad
 \boxed{v_p(d_{p-1})=3p-5}.
 \tag{A10}
\]
最后d是使A9成为primitive整数polynomial的有理scalar，
不是任意安全清分母因子。原K3相同归一化的该处Gauss
valuation为3p−1；三阶改变恰−6(p−1)，不能沿用旧费用。

该prime贡献(3p−5)log p=O(n log n)=o(n²)。其它素数处的primitive
scalar可能有正负valuation；A10甚至不单独给全局log|d_n|下界。
全部prime/window、p²及更高层、固定2/3、完整coefficient content和
F_n的联合累计尚未付。不能把安全24·S_n·d_(5n)^5或本轮一个
exact auxiliary prime当作全局净费用。

## 6. 本轮范围与后续唯一费用门槛

支付了新β−4完整entry引理，核清实际单位块与全distribution输入，
得到actual全系数A8、primitive关系点无界非零及A10单prime精确费用。
接下来只处理同一Qtilde的全prime Gauss累计，随后才与同对象实界
比较；240移植的−6仍以原完整能量证书为条件。
没有新数值无理性或线性无关性定理，也不重新开启scalar参数扫描。

输入身份和最终delta在[scope](../literature/logistic_prime_edge_round241_20261008/alternative_reading_scope.md)登记。
C固定块稿7192 B /
4df224c01c24a18121b50810b910fdabba1e10d523e8c499e1bdd05395205b5d；
唯一producer3992 B /
881a02e507ca7505c877f3f57d64ab8412363491355810bee660fe59ef8bd8fe；
JSON1921 B /
42c02ce2ead856b0787b892ff3bd10b4b502cd5947ee27bd61d5022e707ef590。
本人程序0；只阅读Root既有一次exact check，未重跑，未构建Lean。
只新增本稿与本人来源记录；最终保存后全文自读，另报bytes/hash。
