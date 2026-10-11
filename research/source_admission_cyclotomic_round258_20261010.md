# 第258轮：两个真实 cyclotomic polylog 通道的来源准入

2026-10-10。作者：`source258_cyclotomic`。本稿固定三次根与四次根的经典 polylog 源，证明其真实端点关系不能消掉指定 cyclotomic branchpoints 的完整非单值障碍。结算是**这一固定来源不准入**，不是新的 ζ/L 数值无理性定理，也不是所有 cyclotomic/CDT 来源的 no-go。

## 1. 固定函数、真实共轭、目标和域

令 ω=exp(2πi/3)，A={ω,ω²,i,−i}，首先固定整数权重 s=2。对 α∈A 定义实际 Taylor germ

\[
 F_{\alpha,k}(z)=\operatorname{Li}_k(\alpha z)
 =\sum_{n\ge1}\frac{\alpha^n z^n}{n^k},\qquad k\ge1.
 \tag{C1}
\]

系数属于 E=Q(ω,i)=Q(ζ₁₂)，不是以 ζ/L 数值作自由 Taylor starts。真实共轭指 F_{bar α,k}(z)=overline{F_{α,k}(bar z)}；不是只在 z=1 把数值拆成实虚部。四个通道全部保留。

初始 branches 固定为 C1 延拓到

\[
 D=\mathbb C\setminus\bigcup_{\alpha\in A}
 \{r\alpha^{-1}:r\ge1\}.
 \tag{C2}
\]

D 包含 0 和整段 [0,1]，每个 C1 的 principal branch 在 D 全纯。四个有限分支点是

| α | pα=α⁻¹ | 与其配对的共轭点 |
|---|---|---|
| ω | ω² | ω |
| ω² | ω | ω² |
| i | −i | i |
| −i | i | −i |

本轮先检验 pω=ω² 和 pi=−i，再包括其真实共轭。固定 Uα={|z−pα|<1/10}；这些盘不含 0、互不相交。要领取的域增益明确为将 D 扩大到 D∪Uα 或 D∪(所有 Uα)，同时让**完整函数族**在新增盘中单值亚纯。换一个不经过分支点的 cut、使用 universal cover、只从一个扇区继续，都不是本稿所称的补点增益。

固定有理数 a,b,c,d，目标关系为

\[
 R=a+b\zeta(2)+cL(2,\chi_{-3})+d\beta(2)=0.
 \tag{C3}
\]

χ−3 的值在模3余类1、2、0分别为1、−1、0；β(2)=Σ_{n≥0}(−1)ⁿ/(2n+1)²。绝对收敛级数直接给

\[
\begin{aligned}
 F_{\omega,2}(1)&=-\zeta(2)/3+i\sqrt3\,L(2,\chi_{-3})/2,\\
 F_{\omega^2,2}(1)&=-\zeta(2)/3-i\sqrt3\,L(2,\chi_{-3})/2,\\
 F_{i,2}(1)&=-\zeta(2)/8+i\beta(2),\\
 F_{-i,2}(1)&=-\zeta(2)/8-i\beta(2).
\end{aligned}\tag{C4}
\]

例如 ω-pair 的 cosine 在3∣n时为1，其余为−1/2，所以实部为 ζ(2)/9−(ζ(2)−ζ(2)/9)/2=−ζ(2)/3；sine 为 (√3/2)χ−3(n)。i-pair 的实部为 Li₂(−1)/4=−ζ(2)/8，虚部为 β(2)。这些是端点等式，无数值无关假设。

采用一个已固定、没有自由参数的真实 endpoint lift：

\[
\begin{aligned}
 H_R(z)=a
 &-\frac{3b}{2}(F_{\omega,2}+F_{\omega^2,2})\\
 &+\frac{c}{i\sqrt3}(F_{\omega,2}-F_{\omega^2,2})
 +\frac{d}{2i}(F_{i,2}-F_{-i,2}).
\end{aligned}\tag{C5}
\]

于是 H_R(1)=R，H_R 是实际 E-Taylor germ。以下先检查这个 lift，再证明任意固定顶权线性组合和完整最小微分族的结论。

## 2. 局部完整分支项：自行证明

在 Uα 中取解析坐标 t=log(αz)，满足 t(pα)=0、t′(pα)=α≠0。选择由 D 中初始 branch 到达的 slit disc。因为

\[
 \operatorname{Li}_1(e^t)=-\log(1-e^t)
 =-\log(-t)-\log\!\left(\frac{e^t-1}{t}\right),
 \tag{C6}
\]

第二项在 t=0 解析。由 C1 逐项微分得到 d/dt Li_k(eᵗ)=Li_{k−1}(eᵗ)，k≥2；这在解析延拓后仍成立。对 C6 逐次积分，解析部分的 primitive 仍解析，而积分 −t^{k−2}log(−t)/(k−2)! 的非解析部分恰为 −t^{k−1}log(−t)/(k−1)!，剩余项解析。因此对每个整数 k≥1，存在 A_k(t) 在0解析，使

\[
 F_{\alpha,k}(z)
 =A_k(t)-\frac{t^{k-1}}{(k-1)!}\log(-t).
 \tag{C7}
\]

这是整个非解析项的分解，不是只算一个渐近首项。沿 pα 的正向局部小环，t 绕0一次，log(−t)增加2πi，t 本身单值，故

\[
 \Delta_{p_\alpha}F_{\alpha,k}
 =-\frac{2\pi i}{(k-1)!}\bigl(\log(\alpha z)\bigr)^{k-1}.
 \tag{C8}
\]

对 β≠α，βpα=β/α≠1，F_{β,k} 在 Uα 由初始 branch 到达的 branch 全纯，局部 ΔpαFβ,k=0。于是每个分支点只支持自己的通道。

这里须区分两句话：C8 的 jump 在 pα 附近是全纯函数；**原函数**因 jump 非零而不能单值亚纯延拓到 Uα。k≥2 时 jump 在 pα 的零阶是 k−1，但不是零函数。一个有限阶零点并不取消 log 分支。

文献交叉核验：Hain 的 [Classical Polylogarithms](https://arxiv.org/pdf/alg-geom/9202022)，§2、Proposition 2.2 的正向绕1公式与 C8 一致；Pérez-Marco 的 [Monodromies of singularities of the Hadamard and eñe product](https://webusers.imj-prg.fr/~ricardo.perez-marco/publications/articles/enemonodromy11.pdf)，§6.1、Corollary 6.1 给同一公式。本稿 C6–C8 已自行推导，不借其 monodromy 直接推出任何数值无关性。

## 3. 不同 support 的精确消支分类

设固定整数 s≥2，并考虑

\[
 H=M(z)+\sum_{\alpha\in A}r_\alpha(z)F_{\alpha,s}(z),
 \tag{C9}
\]

其中 M 与各 rα 单值，且在被检验的 Uα 内亚纯。局部展开 C7 给

\[
 \Delta_{p_\alpha}H
 =-\frac{2\pi i}{(s-1)!}
 r_\alpha(z)\bigl(\log(\alpha z)\bigr)^{s-1}.
 \tag{C10}
\]

亚纯 germ 的环绕延拓为零；非零亚纯 germ 与非零解析 germ 的积不是零 germ。因此 H 在 Uα 亚纯延拓的**必要条件**是 rα=0 germ。这个条件也是充分的：剩余通道在 Uα 全纯，M 亚纯。若系数在相应连通域中定义，identity theorem 将零 germ 提升为该系数恒零。

所以一个通道的局部 monodromy 无法由另一个不同 support 的通道取消。把 rα 乘上 (z−pα)ᴺ、加任意有限 jets 或 meromorphic head，只改变分支项的消失阶；所有 N 下非零 jump 仍在。此结论是函数层面的全尺度结论，没有 Padé degree 或截断尺度。

对固定 lift C5，四个顶权系数为

\[
 \left(-\frac{3b}{2}+\frac{c}{i\sqrt3},\quad
 -\frac{3b}{2}-\frac{c}{i\sqrt3},\quad
 \frac{d}{2i},\quad-\frac{d}{2i}\right).
 \tag{C11}
\]

在先选的 ω²、−i 两点，C10 已分别要求 −3b/2+c/(i√3)=0、d=0。因 b,c∈Q⊂R，第一等式的实、虚部分别为零，得到 b=c=0；也可连同真实共轭点把前两个等式相加、相减，完全不用实数假设。因此

\[
 H_R\text{ 在四个 }U_\alpha\text{ 全部亚纯}
 \quad\Longleftrightarrow\quad b=c=d=0.
 \tag{C12}
\]

此时 H_R=a 已是原域内的常数。若还要求 C3，则 a=0。**C12 分类的是同时满足数值关系与全消支的系数组；没有从 H_R(1)=0 推出 C12 左端。** 因而没有证明 1、ζ(2)、L(2,χ−3)、β(2) 的数值线性无关。

已有端点恒等式使这个逻辑差别十分具体。令

\[
 T(z)=3(F_{\omega,2}+F_{\omega^2,2})
 -8(F_{i,2}+F_{-i,2}).
 \tag{C13}
\]

由 C4，T(1)=3(−2ζ(2)/3)−8(−ζ(2)/4)=0，恒成立；但它的四个系数3、3、−8、−8都非零，故四处 jump 全非零。端点零关系甚至可完全已知，却不产生这些 branchpoints 的补点。这也说明不能把函数独立性直接外借为数值独立性。

## 4. 完整最小族：精确说明哪种闭包

仅四个顶权函数加1的 endpoint carrier E_s 在 K=C(z) 上的函数 rank 为5。若来源要求有理微分 closure，必须保留

\[
 V_s=K\cdot1+\sum_{\alpha\in A}\sum_{k=1}^s K F_{\alpha,k}.
 \tag{C14}
\]

取 θ=z d/dz，则 θFα,k=Fα,k−1 (k≥2)，θFα,1=αz/(1−αz)∈K。故 V_s 对 θ 稳定，且任何包含四个顶权函数的 K-微分空间必含所有较低权重以及1。以下证明这些行独立，支付其 minimality，而不是以名义行数作 rank。

先证明 log(αz) 在 C(z) 上超越。若 Σ_{j=0}^m q_j(z)(log(αz))ʲ=0 为一个非零有理系数多项式恒等式，选避开系数极点的 z≠0，沿绕0环继续 N 次。系数返回原值，log(αz)变成 log(αz)+2πiN。这个次数≤m的多项式便有无限不同根，故各 q_j(z)=0；对一般 z 应用 identity theorem，所有 q_j 恒零，矛盾。

现设

\[
 r_0+\sum_{\alpha,k}r_{\alpha,k}F_{\alpha,k}=0,
 \qquad r_0,r_{\alpha,k}\in K.
 \tag{C15}
\]

在 pα 隔离 support 并应用 C8，得到

\[
 \sum_{k=1}^s\frac{r_{\alpha,k}(z)}{(k-1)!}
 \bigl(\log(\alpha z)\bigr)^{k-1}=0.
 \tag{C16}
\]

由刚证的超越性，该通道全部 rα,k=0。对四个 α 重复，最后 r0=0。因此

\[
 \dim_KV_s=1+4s;
 \qquad s=2\text{ 时完整最小微分族 rank}=9.
 \tag{C17}
\]

证明在 K=C(z) 上成立，故允许 ζ/L 数值作为**常数系数**也不改变它。把某个假设数值关系代入后，只要某个系数仍非零，该函数组合不能因为这个关系成为同时消掉四个 supports 的 K-线性组合。若关系使全部非meromorphic方向系数恒零，剩下的是已经 meromorphic 的行；该操作已删除此来源的 polylog 方向，未给原完整族增加共同域。

还须区分有理微分 closure 与 branch saturation。C8 在继续后的 leaf 上产生 log z。若只要求 endpoint carrier 在 monodromy 下饱和，加入1、(log z)ʲ (1≤j≤s−1)，得到 rank s+4 的 U_s；它一般不是微分稳定的。若同时要求微分和 monodromy 都闭合，则为

\[
 W_s=V_s+\sum_{j=1}^{s-1}K(\log z)^j,
 \qquad\dim_KW_s=5s.
 \tag{C18}
\]

独立证明：对 W_s 的有理关系仍可在每个 pα 应用 C8，因为 log z 在此局部全纯；C16 消掉全部 Li 系数，剩余 log 多项式由超越性消掉。闭合性由 θ(log z)ʲ=j(log z)^{j−1} 和 log z 的平移得到。最小性由一个顶权 jump 产生 (log(αz))^{s−1}，绕0的有限差分依次生成全部较低 log powers。s=2 的 E/U/V/W ranks 分别5、6、9、10；这里没有把10称为标准单通道 polylog local system 的 rank。log z 行记录 foreign-leaf continuation，不能冒充0处的初始 Taylor 行。

## 5. 共同域障碍与全部整数权重的范围

无论采用固定顶权族、V_s 或 W_s，族中实际 Fα,s 在 Uα 有 C8 的非零 monodromy。一个共同单值亚纯延拓若存在，其每个分量必在该盘单值亚纯；其中这一分量已矛盾。因此**对任意假设 C3，完整族不能填入任何 Uα**。固定候选在这四个指定补点上的共同域增益为零。固定候选的域并不因数值关系改变。

任何局部亚纯可逆基变换也不能改变这个结论：若变换后全部行亚纯，由亚纯逆矩阵恢复原行，它们也会全部亚纯，与 C8 冲突。删除行、使用非亚纯或不可逆变换，则改变了来源，不能作为这一完整族的免费消支。

C7–C18 对每个整数 s≥2 完整成立：分支点集合不随 s 改变，jump 的零阶增长为 s−1，非零性不变。较高权重在单位圆的真实 Dirichlet endpoint仍由 C1 的 Fourier/余类分解给出；它们的具体数值关系无需预先分类，数值常数只会进入 endpoint选择与单值系数。这里只分类经典**整数**权重族，不冒称已处理全部非整数 polylog 或多变量 multiple polylog。

本证明只否决：相同变量 z、同一组四个 α、经典 Li_s(αz)、全部真实共轭保留、有理或局部单值亚纯系数、并要求数值关系在这四个指定点消掉完整族障碍的来源选择。它不否决真正改变 branch support 的非线性变换、非局部积分的新来源、另证的 ramified descent、非全纯的 single-valued polylog、其它 cyclotomic/CDT 结构或其它数值方法。特别地，关系悬挂在另一个目标点可能有真实局部消支机制，须另固定其完整背景与实际共同域；本稿没有审定那些新对象。

## 6. 准入和执行结算

固定候选的第一个必要准入条件已失败：即使端点关系成立，它也不能使指定 cyclotomic branchpoints 的完整非meromorphic方向全部消失。故不启动新的 Padé、参数/prime/map 扫描或旧 producer；不计算可外借的费用/容量指标。保留的可复用资产是 C7–C18 的自足 local-support 分类与完整函数秩证明，不是原数值目标的完成证书。

NEW primary PDF、旧笔记实际读取区间、文件身份和工具执行范围见本轮 [cyclotomic_reading_scope.md](../literature/source_admission_round258_20261010/cyclotomic_reading_scope.md)。没有全球 novelty 或 primary全文阅读认证。本身份只新增本稿、自己的 scope 和两个新 source PDF；main、policy、manifest、旧稿未改，外 Git 写、Lean、数学程序运行均零。下一窗口不自动续。
