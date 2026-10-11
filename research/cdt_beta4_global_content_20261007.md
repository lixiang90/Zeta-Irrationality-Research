# β(4) 单周期模型：首层对角格、全素数费用与局部 graded 块

2026-10-07。本稿研究同一 r=3、H=3n 的真实矩阵 E=q+β(4)I，不改变周期投影。新增纸面结果是：首层 p≤n 的费用可以从每维6层降到每维4层，付款对象是完整 determinant polynomial；实际 q 的个别 entries 仍可能有6层分母。结合已付清其它素数的原稿，中间全素数费用由771/40降到691/40=17.275。首层 graded determinant 的低维 residue-class 块又在12n/13<p≤n产生可完全证明的零行内容，最终安全费用为4489/260≈17.265384615。

这些结果尚未给出 β(4) 无理性。17.265384615 仍大于同轮[带权实处界](cdt_beta4_weighted_energy_20261007.md)的约2.137834；本文的有限满秩样本也不是所有尺度的费用下界。作者另实际全文读完该带权稿七节 W1–W33，只用于这个当前状态比较，不把其解析证明当作有限处费用的输入。

直接输入已实际全文读取：

- [精确算术与原列池 Schur 身份](cdt_beta4_projection_exact_arithmetic_20261007.md)，18981 bytes，SHA256 53b425c356f83c23d9be021f70873b84c441eb8debbdac485c1cf4582228f277；全文十二节与 E1–E37。
- [原单周期积分模型](cdt_beta_single_period_confluent_integral_model_20261007.md)，11668 bytes，SHA256 a008a54d3307f151911ad0fc1dfa3587e05fd54eb89bd0172be364d162d64f2c；全文八节与 B1–B29。

## 1. 对象与首层范围

令 J={0,…,n−1}，I={n,…,3n−1}，D(z)=∏_{u=0}^{3n−1}(z−u)，B_k(z)=∏_{v∈J,v≠k}(z−v)，Q_I(z)=∏_{u∈I}(z−u)。原实际行是

\[
\Phi_k(z)=\frac{Q_I(z)}{B_k(z)^2},\qquad
T_k(z)=[\Phi_k(z)]_{k,<3},\qquad
P_{ku}=\frac{B_k(u)^3T_k(u)}{D'(u)}.
\tag{C1}
\]

其中 P_{kv}=δ_{kv} 对 v∈J。正规化二次 Taylor 公式与整数 factorial 基数均由输入原稿逐式证明。完整投影后有理部分为

\[
q_{kv}=\frac1{64}\sum_{\substack{0\le u<3n\\u\ne v}}
\frac{P_{ku}(T_{u,1}-T_{v,1})}{(u-v)^3}
-\delta_{kv}T_{v,4},\qquad
T_{u,r}=\sum_{j=0}^{2u-1}\frac{(-1)^j}{(2j+1)^r}.
\tag{C2}
\]

本文所有局部新论断取素数

\[
\sqrt{12n}<p\le n.
\tag{C3}
\]

因而 p 为奇数，p²>12n>3n；节点差和奇数尾的每个分母只可能有一层 p。小素数及全部高次幂仍用原 E16 支付，并未删除。

对 a∈{0,…,p−1} 置

\[
d_a=\#\{v\in J:v\equiv a\bmod p\},\qquad
q_a^{\,I}=\#\{u\in I:u\equiv a\bmod p\},\qquad
h_a=2d_a-q_a^{\,I},\qquad t_a=d_a+q_a^{\,I}.
\tag{C4}
\]

q_a^{I} 是节点计数，区别于矩阵 q。这里 p≤n 保证每个 d_a≥1。

## 2. 全部实际 Taylor 系数的估值

**C1. Taylor 系数界。** 写 Φ_k(k+w)=Σ_{ℓ≥0}α_{k,ℓ}w^ℓ，c=k mod p，则

\[
v_p(\alpha_{k,\ell})\ge q_c^{\,I}-2(d_c-1)-\ell.
\tag{C5}
\]

证明：Q_I(k+w) 中恰有 q_c^{I} 个常数项有估值1的线性因子，其余常数项为单位。取 ℓ 次项至多消去 ℓ 个这些 p 因子，故分子 ℓ 次系数估值至少 q_c^{I}−ℓ（负数下界也合法）。B_k(k+w) 中恰有 d_c−1 个估值1的常数项。每个逆平方因子的展开为 a^{-2}Σ_{j≥0}(−1)^j(j+1)(w/a)^j，其 j 次项估值至少 −2v_p(a)−jv_p(a)。所有分母因子乘积的 ℓ 次系数至少 −2(d_c−1)−ℓ。把分子、分母各次数相加，得到 C5。这个证明没有假设正规化 h_{k,ℓ} 是单位，也没有把 a_k 的费用免费忽略。

**C2. 同 residue-class 的投影整性。** 若 u∈I、u≡k mod p，则

\[
v_p(P_{ku})\ge0.
\tag{C6}
\]

u−k 有估值1，故 T_k(u) 的每一 Taylor 项由 C5 至少有估值 q_c^{I}−2(d_c−1)。B_k(u) 中恰有 d_c−1 个一层 p 因子，D'(u) 中恰有 t_c−1 个。因此

\[
v_p(P_{ku})\ge3(d_c-1)+q_c^{\,I}-2(d_c-1)-(d_c+q_c^{\,I}-1)=0.
\]

不要求截断 T_k(u) 本身为零，也不需要 Taylor 余项进一步相消。

**C3. 异 residue-class 的投影界。** 若 u∈I、a=u mod p≠c=k mod p，则

\[
\boxed{\quad v_p(P_{ku})\ge h_a-h_c+1.\quad}
\tag{C7}
\]

此时 u−k 为单位；T_k(u) 的三项由 C5 至少有估值 q_c^{I}−2d_c。B_k(u) 中恰有 d_a 个一层 p 因子，D'(u) 中有 t_a−1 个。于是

\[
v_p(P_{ku})\ge3d_a+q_c^{\,I}-2d_c-(d_a+q_a^{\,I}-1)
=h_a-h_c+1.
\]

C6、C7 对实际完整 P 的所有高行成立；低行是已知 δ，不需另作估计。

## 3. 连续节点的权重振幅

**C4.** 对所有 n、p≤n，

\[
\max_a h_a-\min_a h_a\le3.
\tag{C8}
\]

证明写 n=Ap+b，0≤b<p，3b=cp+r，c∈{0,1,2}，0≤r<p。完整连续节点给

\[
d_a=A+\mathbf1_{a<b},\qquad
t_a=3A+c+\mathbf1_{a<r},\qquad
h_a=3\mathbf1_{a<b}-c-\mathbf1_{a<r}.
\tag{C9}
\]

若 r≥b，则 a<b 的权重是2−c，其余可能是−1−c或−c；振幅至多3。若 r≤b，则 a<b 的权重可能是2−c或3−c，其余是−c；振幅仍至多3。空区间和 b=0 只会减小振幅。这也给出完全显式的格，不用数值求最优行列权重。

## 4. 四层 determinant 整格

令 S_p=diag(p^{h_{k\bmod p}})_{k∈J}，其 entries 允许为有理 p 次幂。置 q^{(p)}=S_pqS_p^{-1}。

**C5. 完整局部整数模型。**

\[
\boxed{\quad p^4q^{(p)}\in M_n(\mathbb Z_p),\qquad
p^{4n}\det(q+TI_n)\in\mathbb Z_p[T].\quad}
\tag{C10}
\]

证明第一式逐项处理 C2，不把不同项的费用相加。所有 T_{u,1}−T_{v,1} 估值至少−1，T_{v,4} 至少−4，1/64 是 p 单位。

- 若 u≡v mod p，则 u−v 恰有一层 p。u≡k 时 C6（或低行 δ）给 P 整，且 h_k=h_v，所以共轭后该项估值至少−4。u≢k 时 C7 给 P 至少 h_v−h_k+1，共轭后的该项至少−3。
- 若 u≢v mod p，差为单位。u∈I 且 u≢k 时 C7 给共轭后该项至少 h_u−h_v≥−3。u≡k 时 C6 给至少−1+h_k−h_v≥−4。低行唯一非零项 u=k 也满足后一界。
- 对角有限尾在共轭下不变，至少−4。

第二式来自

\[
\det\!\left(p^4(q^{(p)}+TI_n)\right)
=p^{4n}\det(q+TI_n),
\tag{C11}
\]

左侧每个系数都整。S_p 可不是 Z_p-unimodular，但这是共轭，左右 determinant 的费用精确抵消；不能把清 S_p 或清 P 的费用再加到 C11。等价地，格 L_p=⊕_{k∈J}p^{-h_k}Z_p e_k 满足 qL_p⊂p^{-4}L_p，而 T·I 保存同一格。

## 5. 首层 graded 块的精确身份

记 M_p=p⁴q^{(p)} mod p。

**C6. 只允许单向异类项。** 若 k mod p≠v mod p，则

\[
(M_p)_{kv}=0\quad\text{除非}\quad h_v-h_k=3.
\tag{C12}
\]

证明：上一节中 u≡v 的异类项共轭后估值至少−3；u∈I、u不属 k 类亦至少−3。唯一可能达到−4的是 u属 k 类、u≢v，其下界为−1+h_k−h_v，而 C8 使其只在 h_v−h_k=3 时可达到。低行 u=k 同理。没有异类对角尾。故按 h 非降序排列 residue classes 后 M_p 是 block 上三角，所有同权重异类块为零。

下面给出每个对角块而不猜测其 rank。固定 residue a，低节点按 a+jp（0≤j<d_a）排列，全部节点按 a+lp（0≤l<t_a）排列。以 d=d_a、t=t_a 定义压缩投影

\[
\begin{aligned}
B_j^*(z)&=\prod_{\substack{0\le i<d\\i\ne j}}(z-i),&
Q^*(z)&=\prod_{i=d}^{t-1}(z-i),&
D^*(z)&=\prod_{i=0}^{t-1}(z-i),\\
\Pi_{j l}^{(d,t)}
&=\frac{B_j^*(l)^3}{(D^*)'(l)}
\left[\frac{Q^*(z)}{B_j^*(z)^2}\right]_{j,<3}(l),
&& l\ge d,\qquad
\Pi_{ji}^{(d,t)}=\delta_{ji}\quad(i<d).
\end{aligned}
\tag{C13}
\]

t 不要求等于3d；当压缩分子次数大于 t−1 时，本文只使用 C13 的逐点残数公式，不声称它仍有原尺度的全部 degree 条件。

**C7. matching residue 投影压缩。**

\[
P_{a+jp,a+lp}\bmod p
=\Pi_{jl}^{(d_a,t_a)}\bmod p.
\tag{C14}
\]

证明对于高节点 l≥d，将原 Φ 在 z=a+pz' 中分解。类内 numerator 给 p^{q_a^{I}}Q^*(z')，类内 denominator 给 p^{2(d_a−1)}B_j^*(z')²。类外因子都是单位；在 z' 关于 j 的展开中，其归一化单位 series 模 p 仅有常数项，因为每个正次系数含 p。取低于3阶 Taylor 后，除去 p^{q_a^{I}−2(d_a−1)}，便得到一个共同单位倍数的压缩 Taylor。B_k(u)^3/D'(u) 提供相反的 p 次幂；其类外单位与 Taylor 的类外单位相消，因为 B 类外的三次乘 Q 类外/B 类外²恰为 D' 的类外乘积。类内剩下 C13。C3 保证所有类内不同 ordinal 的差均小于 p，所以这些压缩有理数的分母是 p 单位。低节点身份由 δ 直接成立。

令 ε_p=(−1)^{(p−1)/2}，χ₄(l)=1（l≡1 mod4）或−1（l≡3 mod4），并置

\[
\ell_a=\left\lfloor\frac{4a-1}{p}\right\rfloor,\qquad
H^{(r)}_j(a)=
\sum_{\substack{l\ge1\ {\rm odd}\\l\le4j+\ell_a}}
\frac{\chi_4(l)}{l^r}.
\tag{C15}
\]

空和为零。所有被求和 l<p，因为4(a+jp)−1<12n<p²。

**C8. 对角 graded 块。** residue a 的 d_a×d_a 对角块为

\[
\boxed{\quad
(M_p)_a(j,i)=\varepsilon_p
\left[
\frac1{64}\sum_{\substack{0\le l<t_a\\l\ne i}}
\frac{\Pi_{jl}^{(d_a,t_a)}
\bigl(H_l^{(1)}(a)-H_i^{(1)}(a)\bigr)}{(l-i)^3}
-\delta_{ji}H_i^{(4)}(a)
\right]\bmod p.
\quad}
\tag{C16}
\]

证明原尾中一层 p 分母项恰是 2h+1=pl。其符号
(−1)^h=ε_pχ₄(l)，故 pT_{a+jp,1} mod p=ε_pH_j^{(1)}(a)，p⁴T_{a+jp,4} mod p=ε_pH_j^{(4)}(a)。同一 residue 块中共轭因子抵消，u−v=p(l−i)，C14 给 matching 项。其它 residue 的项在 C5 的证明中估值至少−3，乘 p⁴即消失。C16 因而包括全部项，不是只取猜测的 leading tail。

由 C12，

\[
\det M_p=\prod_{a=0}^{p-1}\det(M_p)_a.
\tag{C17}
\]

这提供进一步研究内容与 rank 的有限块接口；不能预先把任何一个块的 determinant 当作单位或零。C17 是 determinant 乘积身份，不能把总 rank 直接等同于各对角块 rank 的和；异类上三角块仍可能影响 rank 和下一层 Smith 消元。

## 6. 全素数安全费用

记原 E16 的完整所有 p-power 预算为 a_p(n)，原 E32 的 p>n 逐列预算为 c_{p,v}，原 E20 的 p>8n rank 预算为 R_p。对 n<13 继续取原完整 \(\widehat G_n\)。对 n≥13 定义

\[
G_n^{\rm new}=
\left(\prod_{p\le\sqrt{12n}}p^{na_p(n)}\right)
\left(\prod_{\sqrt{12n}<p\le n}p^{4n}\right)
\left(\prod_{n<p\le8n}p^{\sum_{v<n}c_{p,v}}\right)
\left(\prod_{8n<p\le12n}p^{R_p}\right).
\tag{C18}
\]

**C9.** 对全部 n≥1，

\[
\boxed{\quad G_n^{\rm new}\det(q+TI_n)\in\mathbb Z[T],\qquad
\log G_n^{\rm new}\le\frac{691}{40}n^2+o(n^2).\quad}
\tag{C19}
\]

完整整性在首层新范围由 C10，其余范围逐项沿用已全文读取且完整证明的 E16/E21/E33/E34。没有并入另一模型的内容费用。小 prime 区域原 E15 的 O(n^{3/2}log n)=o(n²) 覆盖所有 power；p=2 单独仍为 O(nlog n)。首层 p≤n 的6改4，PNT 给节省2nΣ_{√12n<p≤n}log p=2n²+o(n²)。其它分段原 integral 未变，因此771/40−2=691/40。这里是安全上界，未声称最小分母。

若 β(4)=A/B∈Q，B≥1，则

\[
B^nG_n^{\rm new}\det E_n\in\mathbb Z,\qquad
\det E_n\ne0\ \Longrightarrow\
\log|\det E_n|\ge-\frac{691}{40}n^2-o(n^2)-n\log B.
\tag{C20}
\]

固定 B 只付 O(n)。已有固定23无限非零性可以为有理假设下的大 n=23^j提供非零接口，但不会把 C19 的 n²费用另行降低。

## 7. 一个固定尺度的全精确证据

本轮只选 n=23、p=19 一个新样本；不是旧 prime table 的扩展。三个新的 inline Python/Fraction 计算分别检查投影下界与原 q，求同一共轭 leading rank，再独立按压缩公式生成对角块。输入、窗口均固定；没有浮点数。

此样本 d_a=2（a=0,…,3）或1，q_a^{I}=2（a=0,…,3及12,…,18）或3，故
h=(2,2,2,2,−1,−1,−1,−1,−1,−1,−1,−1,0,0,0,0,0,0,0)。
全部 C6/C7 逐项检查无失败。原 q 的最低估值为−6，在(k,v)=(0,4)达到；共轭 q^(p) 的最低估值为−4，在(0,0)达到。因此“实际 q 全部 entries 只有四层分母”是错误命题。

全原矩阵的 M_p mod19 精确消元 rank=23。C16 另给紧凑证书：

| residue a | (d_a,t_a,ell_a) | 对角块 mod19 | determinant mod19 |
|---|---|---|---|
| 0 | (2,4,−1) | [[15,4],[13,11]] | 18 |
| 1,…,3 | (2,4,0) | [[15,4],[13,11]] | 18 |
| 4 | (1,4,0) | [3] | 3 |
| 5,…,9 | (1,4,1) | [9] | 9 |
| 10,…,11 | (1,4,2) | [9] | 9 |
| 12,…,14 | (1,3,2) | [1] | 1 |
| 15,…,18 | (1,3,3) | [16] | 16 |

由 C12/C17，det M_p=18⁴·3·9⁷·1³·16⁴≡3 mod19，所以

\[
v_{19}(\det q_{23})=-4\cdot23=-92.
\tag{C21}
\]

这一有限结论同时给出此处完整 polynomial 的最低分母确实需要19^{92}，因为常数项已达到。它排除自动将 p=n 的某个 rank 缺陷推广到 n>p，但不构成一个 n² leading 最小费用的渐近定理。未执行 producer 文件，没有扩大 prime 扫描，也没有复跑旧 scripts、guards或Lean。

## 8. 接近 n 的素数：完整零行内容

再限定素数同时满足 C3 及 12n/13<p≤n。写 b=n−p，所以0≤b<p/12，令

\[
m_p=\left\lceil\frac{p+1}{4}\right\rceil,\qquad
Z_p=\{a:3b\le a<m_p\},\qquad
z_p=|Z_p|=\max(0,m_p-3(n-p)).
\tag{C22}
\]

**C10. 真实 graded 零行。** 对每个 a∈Z_p，M_p 中对应这个 residue 的整个行与整个列均为零。

证明 n=p+b，3b<p，故 C9 的节点计数为 d_a=1+1_{a<b}，t_a=3+1_{a<3b}，h_a=3·1_{a<b}−1_{a<3b}。当 a≥3b 时 d_a=1、t_a=3、h_a=0。此时压缩 B_0^*=1、Q^*(z)=(z−1)(z−2) 恰为完整二次多项式，其 Taylor 截断不改变它，所以压缩高节点残数全零，即 Π=(1,0,0)。又 a<m_p 对奇素数 p 保证 4a−1<p，故 ell_a≤0，H_0^{(4)}(a)=0；C16 给出这个1×1对角块为零。全部节点权重只可能是2、−1或0，而 C12 的异类非零项需要权重差3，所以权重0的这些类与所有异类的行、列也都为零：

\[
(M_p)_{a,v}=0=(M_p)_{k,a}\quad(a\in Z_p,\ k,v\in J).
\tag{C23}
\]

这里 a<n，所以每个 a 确实是对应的唯一低节点。C23 使用了整个异类块的控制，不是把对角块 rank 直接相加。

**C11. 全部系数同时节省。** 由 C10 的 p 整矩阵 A_p=p⁴q^(p)，这 z_p 个行在模 p 下全零。A_p+p⁴TI 的同一批行，其每个多项式系数仍可被 p 整除。提取这些行的 p 因子，得到

\[
\boxed{\quad p^{4n-z_p}\det(q+TI_n)\in\mathbb Z_p[T].\quad}
\tag{C24}
\]

令 G_n^{\rm final}=G_n^{\rm new}∏ p^{-z_p}，此处乘积只取 C3 且12n/13<p≤n的素数；其它素数不变。这个 G_n^{final} 是正整数：被替换的原局部指数恰为4n，而0≤z_p≤n。不存在未付的分母或负指数素数模型。对全部 n，

\[
\boxed{\quad G_n^{\rm final}\det(q+TI_n)\in\mathbb Z[T],\qquad
\log G_n^{\rm final}\le
\left(\frac{691}{40}-\frac1{104}\right)n^2+o(n^2)
=\frac{4489}{260}n^2+o(n^2).\quad}
\tag{C25}
\]

证明全系数整性逐素数使用 C24 与 C19。ceil只造成 z_p=(13p/4−3n)+O(1)，均匀误差 O(1)。对足够大 n，新区间全部自动满足 p>sqrt(12n)，有限例外不影响渐近。PNT 与 partial summation 给
Σz_p log p=n²∫_{12/13}^1(13x/4−3)dx+o(n²)=n²/104+o(n²)；
O(1)误差的总贡献为 O(n)。小 prime 高次幂仍完全保持 C18 的旧付款。

若 β(4)=A/B∈Q 且 det E_n≠0，最终条件下界为

\[
B^nG_n^{\rm final}\det E_n\in\mathbb Z,\qquad
\log|\det E_n|\ge-\frac{4489}{260}n^2-o(n^2)-n\log B.
\tag{C26}
\]

这一节没有新增 prime 计算；root 与作者分别从已证 C16 推出同一零行窗口。它是完整纸面内容节省，不是固定样本外推。

## 9. 状态与下一步

本稿新增的可审查成果是 C5 的合法共轭整格、C6–C8 的首层局部块接口、C9 的中间17.275安全费用，以及 C10–C11 的接近 n 零行内容和最终4489/260费用。作者已完成各证明的逐式检查及上述单样本全精确计算。weighted_energy 代理先独立全文读取原八节/C1–C21及旧算术十二节/E1–E37，逐式纸审通过；另以两段新的 inline Fraction 独立复核全部19个压缩对角块和乘积3，并直接由未正规化Φ复核 q_(0,4) 的估值−6及 numerator unit15。加入第八节后，该代理再次实际全文读取最终九节/C1–C26，新增零行内容及1/104费用补审通过。root亦独立全文读取最终九节/C1–C26，逐式复核全部 Taylor、共轭格、压缩块、有限样本及最终费用，正式纸审通过。两份审阅均无数学修正请求。作者收审并更新这个审读记录后，完成最后实际全文回读；未新增 PDF 下载或 PDF 页阅读，没有形式化验证。纸审与计算均不称为形式化验证。

最需要继续研究的是 C16 的 compressed-block determinant/rank 在随 n 增长的全部素数范围中的统一规律，以及 p>n 的真实 residue 尾内容。新费用仍不足以与同轮带权实处约2.137834衰减形成矛盾，本文没有新数值无理性或线性无关性结论，也没有声称这一框架存在费用不可改进的障碍。

