# beta(4) 完整周期投影的精确算术与原列池 Schur 身份

2026-10-07。本轮唯一新稿，纯纸面推导。直接输入是已保存的 cdt_beta_single_period_confluent_integral_model_20261007.md，SHA256 a008a54d3307f151911ad0fc1dfa3587e05fd54eb89bd0172be364d162d64f2c，11668 bytes，已实际全文读取全部八节与 B1–B29。没有修改该输入或旧冻结稿。

本稿不证明 beta(4) 无理。已证进展是：原投影的 factorial 基数恰为整数二项式乘积；原列池有完整 Schur 身份；投影后高阶有限尾同时消去；保留大素数处的 Taylor 三阶消失、逐列费用与残数秩，同一真实 determinant 的全素数费用上界从旧粗常数69降为771/40=19.275。该项只在 determinant 非零和目标有理的假设下给出下界，未证明无穷非零序列或严格实处差额。28是下文首先证明的中间安全预算。

## 1. 同一实际单周期模型

**E1.** 令 s=r+1≥2，n≥1，H=rn，J={0,…,n−1}，I={n,…,H−1}。原实际内核为

\[
C_r(u,v)=\int_0^1\int_0^1
\frac{x^{4u}y^{4v}}{1+x^2y^2}
\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
=\sum_{j\ge0}\frac{(-1)^j}{(2j+4u+1)(2j+4v+1)^r}.
\tag{E1}
\]

记 T_{u,a}=Σ_{j=0}^{2u−1}(−1)^j/(2j+1)^a，T_{0,a}=0。实际有理投影行由

\[
\begin{aligned}
D(z)&=\prod_{u=0}^{H-1}(z-u),\quad Q_I(z)=\prod_{u\in I}(z-u),\\
B_k(z)&=\prod_{v\in J,\ v\ne k}(z-v),\\
N_k(z)&=B_k(z)^r\left[\frac{Q_I(z)}{B_k(z)^{r-1}}\right]_{k,<r},
\qquad p_{k,u}=\frac{N_k(u)}{D'(u)}
\end{aligned}
\tag{E2}
\]

给出。这里 Taylor 截断保留0至r−1阶。deg N_k≤H−1，所以

\[
F_k(z)=N_k(z)/D(z)=\sum_u p_{k,u}/(z-u).
\tag{E3}
\]

原模型已完整证明、亦可直接由 (E2) 复核：

\[
p_{k,v}=\delta_{kv},\qquad
\sum_{u\ne v}\frac{p_{k,u}}{(u-v)^\ell}=0
\quad(v\in J,\ 1\le\ell\le r-1).
\tag{E4}
\]

实际积分矩阵为 E=pC，故

\[
E=q+\beta(s)I_n,\qquad q\in M_n(\mathbb Q).
\tag{E5}
\]

以下所有费用都针对这个 E；没有改变行再使用旧格，也没有假设任何较低 beta 值有理。

## 2. factorial 基数的精确整数身份

**E2.** 置

\[
a_k=Q_I(k)/B_k(k)^{r-1},\qquad
\frac{Q_I(k+z)}{B_k(k+z)^{r-1}}
=a_k\sum_{a\ge0}h_{k,a}z^a.
\]

对 u∈I，

\[
p_{k,u}=b_{k,u}\sum_{a=0}^{r-1}h_{k,a}(u-k)^a,\qquad
b_{k,u}=\frac{B_k(u)^ra_k}{D'(u)}.
\tag{E6}
\]

令 d=u−k、j=u−n、h=n−1−k，则 j,h≥0且j+h=d−1。旧输入 B22 中的绝对值可以精确重写为

\[
\boxed{\ 
|b_{k,u}|=
\binom uk^{r-1}\binom{H-1-k}{d}
\binom{d-1}{j}^{r}\in\mathbb Z.
\ }
\tag{E7}
\]

证明把 u!^{r-1}/k!^{r-1} 写为 binom(u,k)^{r-1}(d!)^{r-1}，把 (H−1−k)!/(H−1−u)! 写为 binom(H−1−k,d)d!。余下

\[
\frac{(d!)^r}{d^r(j!h!)^r}
=\binom{d-1}{j}^r
\]

恰好消去原估计中损失的 d^r。没有 floor 余项，也没有素数例外。

符号由原各差乘积给出：

\[
\operatorname{sgn}b_{k,u}
=(-1)^{(r-1)(k+1)+H-1-u}.
\tag{E8}
\]

因此 r=3 时仅为 (−1)^{H−1−u}。不能由“绝对基数整数”推出投影小子式有一致正号。

**E3. 全素数投影整格。** 记 D_M=lcm(1,…,M)，并令 D_0=1。正规化 h_{k,a} 是有限个
(1+z/(k−u)) 与 (1+z/(k−v))^{−r+1}
的系数，每项总分母次数为a，差的绝对值≤H−1。因此

\[
D_{H-1}^{a}h_{k,a}\in\mathbb Z,\qquad
\boxed{\ D_{H-1}^{r-1}p_{k,u}\in\mathbb Z.\ }
\tag{E9}
\]

对 u∈I 应用 (E6)–(E7)，对 u∈J 使用0或1系数，即得所有素数、所有 p-power 的结论。r=1时仍直接p=[I]。原 d_H^{3r−2} 是安全但粗的上界，(E9) 不依赖其旧 factorial-floor 费用。

## 3. r=3 的实际闭式与一个精确特殊尺度

**E4.** 对 r=3，定义

\[
\sigma_k=\sum_{u\in I}\frac1{k-u}
-2\sum_{\substack{v\in J\\v\ne k}}\frac1{k-v},\qquad
\tau_k=-\sum_{u\in I}\frac1{(k-u)^2}
+2\sum_{\substack{v\in J\\v\ne k}}\frac1{(k-v)^2}.
\]

Taylor系数恰为 h_0=1、h_1=σ_k、h_2=(σ_k²+τ_k)/2，所以

\[
\boxed{\ 
p_{k,u}=(-1)^{H-1-u}
\binom uk^2\binom{H-1-k}{u-k}
\binom{u-k-1}{u-n}^{3}
\left(1+\sigma_k(u-k)+\frac{\sigma_k^2+\tau_k}{2}(u-k)^2\right)
\ }\quad(u\in I).
\tag{E10}
\]

其 /2 并不额外损失一个2层：正规化二次系数的整数 binomial 证明 (E9) 已支付全部2-adic情况。式 (E10) 是精确同一 p，不是另一个正系数近似。

**E5.** n=1时 B_0=1，Q_I的次数为r−1，Taylor截断保留它的全部项。于是 N_0=Q_I、F_0=1/z、p_{0,u}=δ_{0u}，E=[β(s)]。这个特例确实非零，但不产生无穷尺度非零性；也不能从它推断一般投影的正性。对 n>1 (E10) 的括号与交替基数都必须保留。

## 4. 完整原列池的 Schur complement

**E6.** 以下取r=3，H=3n。定义 H×2n 的完整低周期列池 K：

\[
K_{u,(v,\ell)}=
\begin{cases}(u-v)^{-\ell},&u\ne v,\\0,&u=v,\end{cases}
\qquad v\in J,\quad\ell=1,2.
\tag{E11}
\]

按u先J后I排原行，按v递增并每v先ℓ1后ℓ2排K列。令 A=K_I，为2n×2n。它的确切 confluent Cauchy determinant 为

\[
\boxed{\ 
\det A=(-1)^{\binom{2n}{2}}
\frac{V(I)\prod_{v<w\in J}(w-v)^4}
{\prod_{u\in I,v\in J}(u-v)^2}\ne0.
\ }
\tag{E12}
\]

证明从普通 Cauchy det[1/(u−y)] 的 double alternant 开始，把两个相邻列点取 y=v,v+ε，列差除ε，令ε→0。第二列趋于∂_v1/(u−v)=1/(u−v)²；每个内部 V(y) 的因子贡献ε，跨组因子贡献(w−v)^4。所有分母在极限非零。普通减法Cauchy的符号是 (−1)^{binom(2n,2)}，所以n=1的A为[[1,1],[1/2,1/4]]，其符号为负，亦与公式一致。这个示例仅是手核两阶符号，不是数值试验。

**E7.** 由 p_J=I_n 和 pK=0，

\[
\boxed{\ p=[\,I_n,\,-K_JA^{-1}\,].\ }
\tag{E13}
\]

这既证明与 (E2) 的投影相同，也证明在完整列池中唯一性；没有只对某个删去的低周期子池求逆。

令 C为原H×n实际积分矩阵，按列先C后K排扩展方阵。精确 block Schur 身份为

\[
\boxed{\ \det[C\mid K]=\det A\,\det E.\ }
\tag{E14}
\]

按同一行列顺序无需额外符号。对下方块消元得到
det A·det(C_J−K_JA^{−1}C_I)，后者恰E。此式可能用于直接研究原列池的内容，但不能把清det[C|K]的分母、清det A的分母以及清p的分母全部另加给E。下一节从同一 q 的准确简化建立一次性的整数模型，避开该 double payment。

## 5. 投影后只剩一阶有限尾

**E8.** 此身份适用于全部r。原u≠v有理部分包含 T_{v,a}，a=2,…,r。它们的系数为 Σ_{u≠v}p_{k,u}/(u−v)^{r-a+1}，由 (E4) 完全消失。因此

\[
\boxed{\ 
q_{kv}=
\frac{(-1)^{r-1}}{4^r}
\sum_{u\ne v}\frac{p_{k,u}(T_{u,1}-T_{v,1})}{(u-v)^r}
-\delta_{kv}T_{v,r+1}.
\ }
\tag{E15}
\]

该式消的是有限尾系数，不只是低阶beta符号；原所有u∈J,I均包括在和中。对于 r=3，前面的符号为正，分母常数为64。

**E9. 另一份全极点核对。** 由完整 regular-part 条件，

\[
\frac{F_k(z)}{(z-v)^r}
=\frac{\delta_{kv}}{(z-v)^{r+1}}
+\sum_{u=0}^{H-1}\frac{c_{kvu}}{z-u},
\]

其中 u≠v时 c_{kvu}=p_{k,u}/(u−v)^r，而
\(c_{kvv}=-\sum_{u\ne v}p_{k,u}/(u-v)^r\)。
高阶2至r的全部极点项为零，simple residues之和为零。代入z=−(2j+1)/4并对交错j求和，就只剩simple harmonic尾差和目标(r+1)阶对角尾，给 (E15)。这说明简化来自完整投影，不是局部留数的猜测。

## 6. beta(4) 全素数、全 p-power 的一次付款

**E10.** 以下固定r=3、H=3n。对素数p记

\[
L_M(p)=\max\{e\ge0:p^e\le M\},\qquad
L_M^{\rm odd}(p)=
\begin{cases}L_M(p),&p\ne2,\\0,&p=2.\end{cases}
\]

M<1时两个L为0。T_{u,1} 的奇数分母≤4u−1<4H，目标 T_{v,4} 的分母≤4v−1<4n。令

\[
\boxed{\ 
a_p(n)=
\max\{5L_{H-1}(p)+L_{4H-3}^{\rm odd}(p),\
4L_{4n-3}^{\rm odd}(p)\}
+6{\bf1}_{p=2}.
\ }
\tag{E16}
\]

则全部 q_{kv} 满足 v_p(q_{kv})≥−a_p(n)。

证明：(E9) 的 p最多损失2L_{H−1}；(u−v)^3最多损失3L_{H−1}；simple harmonic差最多损失Lodd_{4H−3}。常数1/64只在p=2损失6。单独目标尾损失4Lodd_{4n−3}，最后取max而非把两类损失相加。所有有限求和由超度量不等式付款，含u=k≠v的低行项。此证覆盖小素数及全部power；没有只看大prime首层。

**E11. 首层分段。** 对 p>√(4H)，p≠2，可安全取

\[
a_p(n)\le
\begin{cases}
6,&p\le H,\\
4,&H<p\le4n,\\
1,&4n<p\le4H,\\
0,&p>4H.
\end{cases}
\tag{E17}
\]

只按每entry清分母得到det费用

\[
[6\cdot3+4\cdot1+1\cdot8]\,n^2+o(n^2)=30n^2+o(n^2).
\tag{E18}
\]

这已经是原q的联合一次付款；不另加投影D_H²或Schur分母。把奇数lcm当成“只有一半素数费用”是不正确的：去掉2只省O(log H)，其leading仍由几乎全部odd primes产生。

## 7. p>8n 的实际秩节省

**E12.** 若 p>8n，则p>H，所有p_{ku}和(u−v)^{−3}都p整，且该差为p单位。每个 T_{u,1} 只有可能含单个非整项 j=(p−1)/2；3p>4H，不能有第二个odd multiple。该项出现当且仅当

\[
u\ge\left\lceil\frac{p+1}{4}\right\rceil.
\]

全部v∈J的T_{v,1}和T_{v,4}都是p整。因此

\[
pq_{kv}\equiv
\frac{(-1)^{(p-1)/2}}{64}
\sum_{u\in U_p}\overline p_{ku}(u-v)^{-3}\pmod p,
\quad
U_p=\left\{u<H:\ u\ge\left\lceil\frac{p+1}{4}\right\rceil\right\}.
\tag{E19}
\]

这是真实n×|U_p|乘|U_p|×n因子分解；高节点全在I。故

\[
\operatorname{rank}_{\mathbb F_p}(pq\bmod p)
\le R_p:=\max\left(0,H-\left\lceil\frac{p+1}{4}\right\rceil\right).
\tag{E20}
\]

p>8n时R_p≤n；p>4H时为0。

**E13. 全系数内容，而非单个有理目标值。** 令
\(\mathcal D_n(T)=\det(q+TI_n)\in\mathbb Q[T]\)。
它是monic n次，故形式上非零。对8n<p≤4H，

\[
\boxed{\ 
v_p([T^j]\mathcal D_n(T))\ge-R_p,\qquad0\le j\le n.
\ }
\tag{E21}
\]

证明 p(q+TI) 在模p上与pq同一常数矩阵，rank≤R_p。以常数p整可逆左右矩阵，将这个模p矩阵化为rank块；剩余至少n−R_p行的全部多项式系数可被p整除。因而 det(p(q+TI)) 的每个系数可被p^{n−R_p}整除。该det为p^n\(\mathcal D_n(T)\)，左右det为p单位，故 (E21)。这不是只验证某个β值的数值rank，也没有假设β4的分母不含p。

## 8. 全整 determinant 与 leading 28

**E14.** 定义有限整数

\[
G_n=\prod_{p\le8n}p^{na_p(n)}
\prod_{8n<p\le4H}p^{R_p}.
\tag{E22}
\]

由 (E16)、(E21) 以及p>4H的整性，

\[
\boxed{\ G_n\mathcal D_n(T)\in\mathbb Z[T].\ }
\tag{E23}
\]

这是同一实际全det的完整有限处格，含全部p-power和p=2，不另清p或A。G_n是安全内容上界，未声称最小分母或最优profile。

**E15. 小素数完整误差。** 对p≤√(4H)，a_p log p=O(log(n+2))，包括所有power。素数个数粗界O(√n)足够，所以这部分对logG贡献O(n^{3/2}log(n+2))=o(n²)。p=2可单独付O(nlogn)。没有把高power或input例外藏进错误的n²常数。

对其余大prime用 (E17)，先得p≤3n贡献18n²，3n<p≤4n贡献4n²，4n<p≤8n贡献4n²。PNT及partial summation还给

\[
\sum_{8n<p\le12n}R_p\log p
=n^2\int_8^{12}(3-x/4)\,dx+o(n^2)
=2n^2+o(n^2).
\tag{E24}
\]

ceil的O(1)误差只损失O(n)。故

\[
\boxed{\ \log G_n\le28n^2+o(n^2).\ }
\tag{E25}
\]

用于PNT的标准形式是θ(x)=Σ_{p≤x}logp=x+o(x)；partial summation给Σ_{p≤cn}p logp=(c²/2)n²+o(n²)。没有用素数表或数值integration。

**E16. 条件有理下界。** 若β4=a/b∈Q，b≥1，则无条件有

\[
b^nG_n\det E\in\mathbb Z.
\tag{E26}
\]

只在detE≠0时，

\[
\boxed{\ \log|\det E|\ge-28n^2-o(n^2)-n\log b.\ }
\tag{E27}
\]

固定b付款为O(n)，没有任何“其它beta值也有理”的输入。尚未证明无限n序列上的detE非零，因此 (E27) 当前是带明确非零条件的下界。

## 9. 大于n的素数处：原Taylor三阶消失

**E17.** 以下n≥13，p>n。于是p为奇素数且p²>12n；本节无需忽略任何该范围内的高power。写

\[
\Phi_k(z)=Q_I(z)/B_k(z)^2,\qquad
T_k(z)=[\Phi_k(z)]_{k,<3},\qquad N_k=B_k^3T_k.
\tag{E28}
\]

所有非零k−v满足绝对值<n<p，故B_k(k)是p单位。因此未正规化的Taylor系数满足
\(\Phi_k(k+w)\in\mathbb Z_p[[w]]\)，特别T_k∈Z_p[z]。这里不能仅说正规化h系数p整后把a_k当成单位；真正使用的是原Phi的整系数展开。

设a为u模p的标准代表0≤a<p。由于p²>H，

\[
v_p(D'(u))=
\left\lfloor\frac{u}{p}\right\rfloor+
\left\lfloor\frac{H-1-u}{p}\right\rfloor
=\left\lfloor\frac{H-1-a}{p}\right\rfloor .
\tag{E29}
\]

**E18. 原matching节点统一保护。** 对v∈J、u∈I且u≡v modp，令
\(\eta_{p,v}=\lfloor(3n-1-v)/p\rfloor\)。
若v≠k，B_k(u)含因子u−v，所以N_k(u)∈p³Z_p。若v=k，则B_k(u)是p单位、Q_I(u)=0，故Phi_k(u)=0；又u−k∈pZ_p，Taylor余项收敛并属于p³Z_p，因而
\(T_k(u)=-\sum_{a\ge3}[w^a]\Phi_k(k+w)(u-k)^a\in p^3Z_p\)。
两种情况给同一个全部k结论：

\[
\boxed{\quad v_p(p_{k,u})\ge3-\eta_{p,v}
\quad(u\in I,\ u\equiv v\!\!\pmod p,\ v\in J).\quad}
\tag{E30}
\]

其中eta≤2；p≥2n时eta≤1。不能漏掉u≡k这一支，也不能把有限二阶Taylor截断本身在这些点误认为零；正确的是它因全Phi在u处为零而具有至少p³的余项。

**E19. 其它节点的全局安全估计。** 若a∉J，则a≥n，由(E29)
\(v_p(D'(u))\le1\)；p≥2n时该估值为0。N_k(u)始终p整。若a∈J且u∈I，(E30)更强；若u∈J，p_{k,u}为0或1。因此

\[
v_p(p_{k,u})\ge
\begin{cases}-1,&n<p<2n,\\0,&p\ge2n.\end{cases}
\tag{E31}
\]

这是原完整p而非重新缩放后的投影估计。所有u,v差小于H，p²>H；若u≡v modp且u≠v，则u−v的估值恰为1。

## 10. 精确逐列付款与771/40

**E20.** 对n<p≤8n，置b_p=2（p<2n）或b_p=1（p≥2n），以及

\[
c_{p,v}=
\max\left\{b_p,\ \eta_{p,v}+1,\
4\,{\bf1}_{\,v\ge\lceil(p+1)/4\rceil}\right\},
\quad 0\le v<n.
\tag{E32}
\]

则原q的第v列所有entries估值≥−c_{p,v}。证明分开而联合取max：u−v为p单位时(E31)最多损失1或0，simple harmonic差最多再损失1；u−v为p倍数时(E30)抵消其cube分母，最多损失eta+1；对角T_{v,4}只有当v≥ceil((p+1)/4)时才含p分母，损失最多4。所有求和使用超度量不等式。q+TI的新增对角T是整系数，故同一逐列预算也给其完整det多项式：

\[
v_p([T^j]\mathcal D_n(T))\ge-\sum_{v=0}^{n-1}c_{p,v}
\quad(0\le j\le n).
\tag{E33}
\]

**E21.** 对所有n定义

\[
\widehat G_n=
\begin{cases}
G_n,&1\le n<13,\\
\displaystyle\left(\prod_{p\le n}p^{na_p(n)}\right)
\left(\prod_{n<p\le8n}p^{\sum_vc_{p,v}}\right)
\left(\prod_{8n<p\le12n}p^{R_p}\right),&n\ge13.
\end{cases}
\tag{E34}
\]

由(E16)、(E21)、(E33)以及大于12n的整性，
\(\widehat G_n\mathcal D_n(T)\in\mathbb Z[T]\)。
小n保留已经证明的完整G_n而不冒用p²>12n，有限例外不影响leading。所有小素数、高power和2仍由(E16)支付。

**E22. 分段费用的完整长度证明。** 令x=p/n。在p>n、n≥13处，ceil与floor只造成O(1)个边界列。对每个非边界x，列变量y=v/n∈[0,1)：

* 1<x<3/2：eta=2当y<3−2x，eta=1在其余列；baseline为2，而对角4出现在y≥x/4。
* 3/2≤x<2：全部eta=1，baseline为2，对角4仍在y≥x/4。
* 2≤x<3：eta=1当y<3−x，其余eta=0；baseline为1，对角4在y≥x/4。
* 3≤x<4：只有对角4区域与baseline1。
* 4≤x≤8：全部列仅需baseline1。

因此1<x<3/2时费用为
2+min(3−2x,x/4)+2(1−x/4)，交点x=4/3；2≤x<3时费用为
1+min(3−x,x/4)+3(1−x/4)，交点x=12/5。其余直接计算，连同p≤n的原6层、p>8n的(E20)残数秩，得到完整leading密度

\[
f(x)=
\begin{cases}
6,&0<x\le1,\\
4-x/4,&1<x\le4/3,\\
7-5x/2,&4/3<x\le3/2,\\
4-x/2,&3/2<x\le12/5,\\
7-7x/4,&12/5<x\le3,\\
4-3x/4,&3<x\le4,\\
1,&4<x\le8,\\
3-x/4,&8<x\le12,\\
0,&x>12.
\end{cases}
\tag{E35}
\]

对1<x≤8有sum_v c_{p,v}=nf(x)+O(1)，8<x≤12则R_p=nf(x)+O(1)，均匀常数可取固定值。0<x≤1的6层只在p>sqrt(12n)使用，以下小prime部分由E15全power误差处理。各piece边界只影响O(1)个prime或O(1)列，不改变leading。

PNT及partial summation给

\[
\begin{aligned}
\log\widehat G_n
&\le n^2\int_0^{12}f(x)\,dx+o(n^2)\\
&=\left(6+\frac{89}{72}+\frac{83}{144}
+\frac{1089}{400}+\frac{273}{200}
+\frac{11}{8}+4+2\right)n^2+o(n^2)\\
&=\boxed{\frac{771}{40}n^2+o(n^2)}.
\end{aligned}
\tag{E36}
\]

每个O(1)列边界的prime求和误差为O(n)；小prime及其所有power为O(n^{3/2}logn)。本式不是从素数首层实验外推。

**E23. 最终同对象条件下界。** 若beta4=a/b∈Q，b≥1，则
\[
b^n\widehat G_n\det E\in\mathbb Z,\qquad
\det E\ne0\ \Longrightarrow\
\log|\det E|\ge-\frac{771}{40}n^2-o(n^2)-n\log b.
\tag{E37}
\]
不另加投影或Schur分母，且固定b仍只支付O(n)。这个费用上界未声称最优；尚未证明其足以与真实实处估计产生strictmargin。

## 11. 能与不能据此得出的结论

**E24.** 旧粗常数69来自投影7层乘H和原A_r全4H的4层。首先(E7)将投影7层降到2层；进一步(E15)同时去掉高阶有限尾，(E16)联合取max得到30；实际高节点rank节省得到28；最后原Taylor三阶消失与逐列联合付款得到771/40。最后结果不把这几个费用另相加，也不以某个entry的rank代替全det。

**E25.** 全Schur列池有detA≠0，形式\(\mathcal D_n\) monic，投影多项式行Σ_u p_{k,u}x^{4u}由低系数块I_n可知独立；但这些不证明\(\mathcal D_n(\beta4)\ne0\)。原积分矩阵的符号正则性不能在尚未控制投影子式符号时免费转成投影后非零性。n=1的精确退化只是标量beta，不是无穷尺度证据。

**E26.** 本稿也没有可比较的实处收缩界。新行(E10)并非原Catalan Chebyshev两branch，不能引用其−2.290939875作为这里的衰减；本稿的leading费用771/40本身不宣布strictmargin。下一步应研究完整原列池Schur的真实解析能量或合法符号/seed，且与(E34)的完整整格同对象连接。

## 12. 实际核查记录

**E27.** 本稿纸面逐式证明(E1)–(E37)，定理标号E1–E27。证明的直接输入只全文读取a008全部八节/B1–B29；未执行其相关代码或同行producer；本稿没有借用旧费用或旧Frobenius种子作新模型证明。普通及confluent Cauchy身份已在本文证明；PNT仅用其标准定理陈述。parent提出原列池Schur及进一步原Taylor/列profile，本文逐式独立复核并证明完整all-n整格。本稿数学证明没有PDF输入；本轮交叉审阅source稿另有32个distinct PDF页、两个页图和官方文本的实际读取域，精确记录在[对应独审](cdt_beta4_pade_perfectness_sources_independent_review_20261007.md)，不能继承为本文证明来源。无新增下载。

数学producer创建/执行/import/rerun=0；prime/Lean/guard=0。未修改原仓库、旧8稿、620冻结记录或任何旧审计。本稿已收到root的[独立全文纸审](cdt_beta4_projection_exact_arithmetic_independent_review_20261007.md)，数学通过且无实质修正请求；作者完成收审后的最后全文回读。元数据hash或纸审通过都不称为形式化验证。
