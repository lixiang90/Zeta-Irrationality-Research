# β(4) 大素数尾残数、完整系数内容与统一首层格

2026-10-07。本文实际全文读取了[精确算术模型](cdt_beta4_projection_exact_arithmetic_20261007.md)、[素数 Newton 多边形](cdt_beta4_prime_newton_polygon_20261007.md)及[同对象实处估计](cdt_beta4_real_determinant_energy_20261007.md)。前五节始终是原 r=3、H=3n 的 β(4) Hermite 投影，不换目标或行格；第六节另完整构造一般 r 的真实 ζ/β 对象，证明相同首层格机制而不继承 β(4) 的解析或非零定理。新增结论包括 p>4n 的可计算尾残数矩阵、完整多项式分母的精确有限证书与统一对角格原则。没有证明新的数值无理性或大素数满秩的渐近定理。

## 1. 唯一非整 harmonic 项给出同一矩阵

记 J={0,…,n−1}、I={n,…,3n−1}，原投影为 P=(p_{k,u})，P_J=I_n，并满足完整 regular-part 条件。原有理矩阵准确为

\[
q_{kv}=\frac1{64}\sum_{u\ne v}
 \frac{p_{k,u}(T_{u,1}-T_{v,1})}{(u-v)^3}
 -\delta_{kv}T_{v,4},\qquad
T_{u,a}=\sum_{h=0}^{2u-1}\frac{(-1)^h}{(2h+1)^a}.
\tag{L1}
\]

令 p 为满足 p>4n 的素数。则 p>3n，所有原投影系数和非零节点差都 p 整，节点差还是 p 单位。T_{v,1}、T_{v,4} 对 v<n 全部 p 整。在 T_{u,1} 的奇数分母中，只有 p 本身可能是 p 的倍数：最大分母为 4u−1≤12n−5<3p。该项存在恰当且仅当

\[
u\ge m_p:=\left\lceil\frac{p+1}{4}\right\rceil,
\qquad \varepsilon_p=(-1)^{(p-1)/2}.
\tag{L2}
\]

所以，不仅 p>8n，而是整个 p>4n 范围都有

\[
p q\bmod p=\frac{\varepsilon_p}{64}\,R_{n,p},\qquad
R_{n,p}(k,v)=\sum_{u=m_p}^{3n-1}
 \overline{p}_{k,u}(u-v)^{-3}\in\mathbf F_p.
\tag{L3}
\]

空和给零矩阵。L3 已包含所有原 u，不另清投影或 Schur 分母；低索引 u<n 因 m_p>n 不再出现。它是原 q 的真实残数，而非一个形式近似。

## 2. 内容付款与满秩时的精确性

设

\[
\mathcal D_n(T)=\det(q+TI_n)=\sum_{j=0}^n c_jT^j,
\qquad r_p=\operatorname{rank}_{\mathbf F_p}R_{n,p}.
\tag{L4}
\]

**L1（全部系数的安全界）。** 对 p>4n，

\[
v_p(c_j)\ge-r_p\quad(0\le j\le n),\qquad
r_p\le\min\{n,(3n-m_p)_+\}.
\tag{L5}
\]

证明：p(q+TI) 是 Z_p[T] 矩阵，其模 p 约化是 L3 的常矩阵。用常数 GL_n(Z_p) 左右变换使最后 n−r_p 行的模 p 约化为零；这些行的每个多项式系数均被 p 整除。故 det(p(q+TI)) 的全部系数均含 p^{n-r_p}，除以 p^n 即得第一界。第二界来自 L3 的实际 n×|U| 乘 |U|×n 因子分解。这不需要假设目标 β(4) 有理。

**L2（满秩时不可再免费降低此处付款）。** 若 det R_{n,p}≠0，则

\[
v_p(c_0)=-n.
\tag{L6}
\]

此外，对任意 T∈Z_p，det(q+TI) 非零且估值恰为 −n。证明：p(q+TI) 的模 p determinant 是 (ε_p/64)^n det R，与 T 无关且为单位。这里不把未知实数周期放进 Q_p；应用于 β(4) 时仅在其有理且分母不含 p 的反证假设下合法。

令 g_n 为清除全部 c_j 分母的最小正整数，即 g_n=lcm_j den(c_j)。则 L6 强制 v_p(g_n)=n。任何声称 G_n D_n(T)∈Z[T] 的完整模型在该素数处都至少支付 n；改变有理基、对角共轭等保持 D_n 的操作不能改变这个结论。该陈述只针对同一 monic determinant 多项式，不排除改变行池或采用不同对象。

## 3. 可逐项复核的满秩与秩亏证书

本轮用新的内联精确分数运算，按原 E10、L1 独立构造 n=2、3 的 P、q，再核验有限域残数。以下每个数均可从 L1–L3 和所显示小矩阵直接检查；没有使用浮点特征值。

对 n=2，两个 pq mod p 分别为

\[
p=11:\ \begin{pmatrix}9&5\\6&5\end{pmatrix},\qquad
p=13:\ \begin{pmatrix}8&11\\1&0\end{pmatrix}.
\tag{L7}
\]

det 分别为 4 mod 11 与 2 mod 13，均为单位。det(XI+pq) mod p 分别为

\[
X^2+3X+4\quad(p=11),\qquad
X^2+8X+2\quad(p=13).
\tag{L8}
\]

独立重构所得精确多项式与既存 Newton 稿一致：

\[
\mathcal D_2(T)=T^2-
 \frac{91207004}{93532725}T-
 \frac{4018152773}{288903880980}.
\tag{L9}
\]

两个素数处按升幂排列的系数估值均为 (−2,−1,0)，显示 L6 的付款确实取到。

对 n=3，p=13 与 p=19 则得到

\[
p=13:\ A=\begin{pmatrix}6&1&3\\6&11&12\\12&4&0\end{pmatrix},\qquad
p=19:\ A=\begin{pmatrix}16&0&5\\14&8&9\\11&13&16\end{pmatrix}.
\tag{L10}
\]

两个 det A 都为零，左上二阶子式分别为 8 mod 13、14 mod 19，故 rank A=2。完整特征多项式为

\[
\det(XI+A)=X^3+4X^2+2X\ (p=13),\qquad
X^3+2X^2+17X\ (p=19).
\tag{L11}
\]

因 X 项分别为单位，p^2 c_1 是单位；L5 又保证全部系数付款至多 2。因此这两个素数恰有 v_p(g_3)=2，而非粗逐列预算的 3。这里 rank 亏损是真实的完整系数内容节省，不靠目标特殊化。L11 本身不确定 c_0 的精确估值，也不声称 rank r 永远使最小分母恰为 r。

作为满秩对照，n=3、p=17 有

\[
A=\begin{pmatrix}11&13&0\\14&14&6\\15&16&12\end{pmatrix},
\quad\det(XI+A)=X^3+3X^2+6X+16\pmod{17}.
\tag{L12}
\]

所以 v_17(g_3)=3。这几个证书同时排除“所有 p>4n 自动满秩”与“这一段普遍有秩亏”的简单推广。

## 4. 真正二次尺度问题的定量门槛

旧安全费用在 4n<p≤8n 使用 n 层，按 PNT 贡献 4n²+o(n²)。这一项是上界，单独不能称为必要费用。但设某个无限 n 序列上的满秩素数满足

\[
\sum_{\substack{4n<p\le8n\\\det R_{n,p}\ne0}}\log p
 =4n-o(n),
\tag{L13}
\]

则 L6 严格推出

\[
\log g_n\ge4n^2-o(n^2).
\tag{L14}
\]

L13 尚未证明，本文没有把有限实验提升为该渐近输入。L14 也仅说该完整 monic 模型的分母费用下界；它不证明目标有理或无理，不证明实际 determinant 衰减不可能强于 4，也不排除不同整模型或非 determinant 的 holonomy 路线。本轮[完整权重能量稿](cdt_beta4_weighted_energy_20261007.md)将同对象上界提高到 γ_w≈2.13783，即使配合 L13，也不能给出矛盾；上界不等于实处最优值。

本轮另在 n=2,3,4,5,6,8,12,16,23 及各自 4n<p≤8n 的全部素数作精确有限域探测。满秩数依次为 2/2、2/4、4/5、4/4、6/6、7/7、9/9、13/13、18/18；秩亏仅见 (n,p)=(3,13),(3,19),(4,19)。该限定样本支持优先研究真实符号/因子结构的方向，既不是 L13 的证书，也不是对未来素数分布或秩的证明。旧 prime table、producer、guard 和 Lean 均未执行。

## 5. 与 holonomy 和下一步的连接

尾残数给出的是有限处行列式信息，不能直接替代 CDT 的 Q(x) 函数秩。CDT 的有效版本仍需实际有理 germ、分母类型和共同亚纯延拓；本轮重新核对其 [§2.1–2.2](https://arxiv.org/html/2510.04156v1#S2)，没有将其中的多处估计当作自动识别不同实现的同一周期。

下一步有两个可验证任务：用完整 P 的 residue cluster 结构证明大素数 R 的全局内容分布，或改变原列池以真正减少坏周期成本。有限单元只能提供反例和接口；固定23的无限非零定理解决的是另一项必要条件，不支付 L13 的二次尺度费用。

前五节 L1–L14 已收到 jet 分工的独立全文纸审 PASS；审阅者以全新内联 Fraction 独立重构五个小矩阵和特征多项式，均一致。较大 n 的有限探测表未作第二次独立重算，仅作为探索。第六节新增后，jet 分工又实际全文读六节 L1–L23 并独立纸审 PASS；global 分工另实际阅读 §6 并重推一般 r 公式，亦通过。全文纸审和精确有限计算均不称为形式化验证。

## 6. 同一首层格原则同时适用于 ζ(s) 与 β(s)

这一节把本轮对角格机制放回真实的 ζ/L 值投影；不继承 β(4) 的非零种子或解析常数。固定整数 r≥1，s=r+1，H=rn，J={0,…,n−1}。使用原通用 Hermite 行

\[
D(z)=\prod_{u=0}^{H-1}(z-u),\quad
P_{ku}=\frac{B_k(u)^r}{D'(u)}
 \left[\frac{Q_I(z)}{B_k(z)^{r-1}}\right]_{k,<r}(u),
\tag{L15}
\]

其中 B_k=∏_{v∈J,v≠k}(z−v)，Q_I=∏_{u=n}^{H-1}(z−u)。低节点处由连续延拓原分子公式得到 P_{kv}=δ_{kv}；当 r=1，I 为空且 P=I。

β 的真实 C_r 仍是原 B1/B2 的内核。另定义实际 ζ 内核

\[
C_r^\zeta(u,v)=\int_0^1\!\int_0^1
 \frac{x^u y^v}{1-xy}\frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
 =\sum_{j\ge0}\frac1{(j+u+1)(j+v+1)^r}.
\tag{L16}
\]

正项级数收敛为 O(j^{-r-1})，所以 Tonelli/Fubini 合法。对 ζ 令 A_{u,a}=∑_{j=1}^u j^{-a}；对 β 令 A_{u,a}=T_{u,a}。部分分式及原 Hermite 的全部 regular-part 消去，给真实单目标身份

\[
P C_r^\Theta=q^\Theta+\Theta(s)I_n,\qquad
q^\Theta_{kv}=\eta_r
 \sum_{u\ne v}\frac{P_{ku}(A_{u,1}-A_{v,1})}{(u-v)^r}
 -\delta_{kv}A_{v,s},
\tag{L17}
\]

其中 Θ=ζ 时 η_r=(−1)^{r−1}，Θ=β 时 η_r=(−1)^{r−1}4^{-r}。ζ(1) 不作为一个数值输入：部分分式的两个一阶项先合成收敛差，恰为有限 harmonic 差。ζ(2),…,ζ(r) 或 β(2),…,β(r) 的全部系数再由 ∑_{u≠v}P_{ku}/(u−v)^l=0（1≤l≤r−1）消去。这不假设任何较低值有理。

**L3（统一首层整格）。** 对素数 √(4rn)<p≤n，设 d_a=#J(a)，e_a=#I(a)，t_a=d_a+e_a，

\[
h_a=(r-1)d_a-e_a=r d_a-t_a,
\quad S=\operatorname{diag}(p^{h_{k\bmod p}})_{k\in J}.
\tag{L18}
\]

则对 Θ=ζ、β 都有

\[
\boxed{\quad p^{r+1}S q^\Theta S^{-1}\in M_n(\mathbb Z_p),\qquad
p^{(r+1)n}\det(q^\Theta+TI_n)\in\mathbb Z_p[T].\quad}
\tag{L19}
\]

证明如下，不能把 S 当作无费用的整数变基。所有非零节点差及 finite harmonic 分母都小于 p²，因此仅有一层 p。令 c=k mod p，写 Φ_k(k+w)=∑α_l w^l，Φ_k=Q_I/B_k^{r-1}；分子因子和逆幂展开逐次数计数给

\[
v_p(\alpha_l)\ge e_c-(r-1)(d_c-1)-l.
\tag{L20}
\]

对 u∈I、u≡k，u−k 的每次幂补回该次数分母。B_k(u)^r 与 D'(u) 的一层计数分别为 r(d_c−1)、t_c−1，所以 v_p(P_{ku})≥0。对 u∈I、a=u mod p≠c，u−k 为单位；在 Taylor 的最高允许次数 r−1 使用 L20，再计 B_k(u)^r 的 r d_a 层和 D'(u) 的 t_a−1 层，得到

\[
v_p(P_{ku})\ge h_a-h_c+1.
\tag{L21}
\]

连续节点的权重振幅至多 r：写 n=Ap+b、rb=cp+b_r、0≤b,b_r<p，则

\[
h_a=r\mathbf1_{a<b}-c-\mathbf1_{a<b_r},
\qquad\max h_a-\min h_a\le r.
\tag{L22}
\]

对 L17 的每个项，现在一次性计入共轭因子 p^{h_k-h_v}。若 u≡v，差的 r 次幂损失 r 层；u≡k 时 P 整且 h_k=h_v，再支付 harmonic 差一层，最多损失 r+1。u≢k 时 L21 给一层额外保护，最多损失 r。若 u≢v，差为单位；u∈I 且 u≢k 时，P 与共轭的合计下界为 h_u−h_v+1，支付 harmonic 一层后至少 −r。u≡k 或唯一低节点 u=k，则至少 h_k−h_v−1≥−(r+1)。对角 A_{v,s} 最多损失 s=r+1 层且共轭不变。η_r 对该奇素数是单位。以上覆盖所有原项，证明 L19 第一式。

最后 det(S(q+TI)S^{-1})=det(q+TI) 精确抵消 S 的左右费用，p^{r+1} 倍矩阵是 Z_p[T] 矩阵，证明完整多项式的第二式。r 固定时，PNT 还给这一区间的安全付款

\[
\sum_{\sqrt{4rn}<p\le n}(r+1)n\log p
=(r+1)n^2+o(n^2).
\tag{L23}
\]

它只是一段有限处费用，不是全素数预算；其它素数、高 p-power、实际无限非零性和相应实处能量仍须分别证明。具体而言，这给 ζ(7) 的同类真实投影七层局部模型，也给 β(6)、β(8) 等 s 层模型。没有因此得到这些值无理性，更没有将有限矩阵格替代 CDT 的 Q(x) 函数秩、全部分母类型及共同亚纯延拓。新增 ζ 内核/一般 r 的费用明确针对新的实际对象，未借用 r=3 的 sec 衰减定理。

独立审读覆盖全部实际对象与费用；仅本文首次的大素数探测及五个有限证书执行三段新内联精确计算，jet 独审再执行一段独立 Fraction 复核，一般 r 的定理是纸面证明。没有新数学 producer 文件、旧脚本/prime table/guard/Lean 执行，没有新增或下载 PDF。作者在收到上述独审后完成最终全文回读。
