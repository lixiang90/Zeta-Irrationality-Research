# 奇权 CDT 系统：纯 Tate 增秩、完整分母和 level12 接口

日期：2026-10-05。目标仍是尚未闭合的奇数 ζ/L 值新无理性或线性无关性，不以已知 ζ(3) 或偶权结果替代。本文新证的是全尺度算术和特定模板的明确限制；尚未达到该目标。所有前轮报告保持冻结。

本轮先读并核对了冻结 `odd_zeta_bb_fine_budget_20261004.md` 与 `odd_zeta_cover_budget_20261004.md`：前者是原 ζ(7) 八维自然基的七层移位分母，后者是 Catalan 特定四次覆盖的自然四行预算。本文不重复这些扫描，不把它们推广成所有 arithmetic holonomy 方法的不可能定理。

新的结果有四项。第一，任意次数纯对数幂的所有必要 lcm scales 可以逐素数证明，不能把其 rank 当成免费辅助量。第二，在纯 Li3 或真正 ζ(3) 尾提升中，追加任意有限个连续纯 Tate 对数幂仍不能救原 slit 模板；这是带实际函数秩的全尺度结论。第三，level12 真 ζ(7) 候选的权六乘子在整数模坐标反演下仍保留七层移位 packet，而标准 Fricke 型 trace 确能消掉最高层，故必须独立核算真正下降，不能把 q 坐标障碍直接跨 trace。第四，在真实 level12 rank8 系统追加任意数量的连续纯对数幂后，精细成本仅 flat 部分仍严格大于 43/10；这没有假设全部解析映射的容量上界。

## 1. 精确的纯对数幂算术

置 L(z)=−log(1−z)，Tℓ=L^ℓ/ℓ!，ℓ≥1。固定 ℓ，允许先乘一个固定整数清常数因子。定义 L_N=lcm(1,...,N)。这里下标 N 与函数 L(z) 无关。

### 1.1 每一个 scale 的必要下界

对每个 p>ℓ 的素数及 1≤j≤ℓ−1，取

\[
 n=jp+\ell-j.
\]

把 L^ℓ 的系数写为 ℓ 个正整数序号之和 n 的乘积求和。由于 n<p²，单个因子的 p 分母层至多为 1；若有 j 个因子含 p，则这些因子至少都为 p。最低赋值 −j 的唯一多重集是 j 个 p 和 ℓ−j 个 1，故

\[
 v_p([z^{jp+\ell-j}]T_\ell)=-j,
 \qquad
 p^j[z^{jp+\ell-j}]T_\ell\equiv\frac1{j!(\ell-j)!}\pmod p.       \tag{1}
\]

若存在超过 j 个 p 因子，其序号和至少为 (j+1)p>n，故没有更低层。其余只有 j 个 p 因子的项要么不存在，要么不能改变上述唯一最低多重集。由于 p∤n，任意固定 n^e 都不能供应 (1) 的 j 层。

在任意固定有限类型 n^e∏_a L_{floor(b_a n+c_a)} 中，每个固定 b_a 至多给一次 p；若 b_a<1/j，则其 endpoint 最终小于 p。因此把活动 scales 按降序排列，必有

\[
 b_{(j)}\ge\frac1j\quad(1\le j\le\ell-1),
 \qquad\sigma=\sum_a b_a\ge H_{\ell-1}.                       \tag{2}
\]

若 e=0，再取 n=ℓp。唯一最低项为 ℓ 个 p，赋值 −ℓ；故还需 b_(ℓ)≥1/ℓ，得到 σ≥Hℓ。固定 offsets 与固定坏素数不能改变这些结论。

### 1.2 完整安全类型达到这些行下界

由经典系数恒等式（也可直接对 log 递推）

\[
 [z^n]T_\ell=\frac1n\,
 e_{\ell-1}\left(1,\frac12,\ldots,\frac1{n-1}\right),             \tag{3}
\]

其中 e_d 是 elementary symmetric polynomial。对任意 ℓ−1 个不同整数 ≤n−1，按 p 赋值降序排，其第 j 大赋值至少为 a 就需 j 个不同 p^a 倍数；于是 jp^a≤n−1。故其分母整除 ∏_{j=1}^{ℓ−1} L_floor((n−1)/j)。因此

\[
 n\prod_{j=1}^{\ell-1}L_{\lfloor(n-1)/j\rfloor}
 \quad\text{清 }[z^n]T_\ell.                                  \tag{4}
\]

另一方面，把 L^ℓ 直接展开，对和为 n 的 ℓ 个正整数，按 p 赋值排序也有 jp^a≤n；所以乘固定 ℓ! 后，∏_{j=1}^ℓ L_floor(n/j) 就清所有项。由 (1)–(4)，自然行的最小总 scale 为

\[
 \boxed{\sigma_\ell^{\min}=H_\ell\ (e=0),\qquad
 \sigma_\ell^{\min}=H_{\ell-1}\ (e\ge1).}                     \tag{5}
\]

e>1 不再降低 (2) 的任何层，只会增加 CDT 的积分成本，故最低成本只需考 e=0 或 1。这是任意 ℓ、所有充分大素数的定理，不是有限的 gcd 猜测。

## 2. 实际 Li3 系统与任意数量的 Tate 辅助函数

对任意 r≥1，取真正的函数族

\[
 \mathcal V_r=(1,\operatorname{Li}_1,\operatorname{Li}_2,
 \operatorname{Li}_3,T_2,\ldots,T_r),\qquad m=r+3.              \tag{6}
\]

当 r=1 时无额外 T 行。其实际 C(z) 秩恰为 m。证明：绕 z=1 重复 monodromy，Li_j 的单值差对绕行次数是一次多项式，而 Tℓ 是次数 ℓ 的多项式。对最高 ℓ≥2 作 ℓ 阶有限差分，排掉其有理系数，再逐级排掉全部 T 行。余下关系绕 1 一次给一个 log z 的多项式；log z 对 C(z) 超越，故全部 Li_j 系数都为零，最后常数也为零。这同时证明函数独立性，不借用 ζ(3) 的任何算术结论。

每行都 holonomic。Li_j 的第 p 项赋值 −j，因而给固定类型的必要条件 σ≥max(0,j−e_j)。必要活动列的 b 都至少为 1；安全类型 n^{e_j}L_n^{j−e_j} 达到它，e_j 只需取 0,...,j。T 行使用 (5)。对固定 e 选择，允许嵌套列的总行和非递减；将各行的独立必要下界排序计算 weighted sum 是对真实可行表的**放宽**，故给严格有效的成本下界。不同 T/Li 行的最小 scale 向量可能不能同时嵌套，所以不把这个放宽值误称全族最优。

精细成本始终是 CDT Definition 6.0.1 / Theorem 6.0.2 的

\[
 \tau^\flat=\frac1{m^2}\sum_{i=1}^m(2i-1)\sigma_i,
 \qquad
 \tau^\sharp=\frac2{m^2}\min_{0\le\xi\le m}
 \{\xi\sum e_i+(\max e_i)I^m_\xi(\xi)\}.                     \tag{7}
\]

这里 e_i 是该定理所要求的非负整数，列的 b 是非负实数；固定 offsets 可以按 Remark 6.0.12 加入。这些函数均已实际证明 holonomic，所以正门槛使用 log|φ′(0)|>τ，而不是误套非 holonomic 版本额外的 σ_max 条件。

### 2.1 有限低秩部分的完整精确分类

对 r=1,...,5，必要的 e 配置恰为 2·3·4·2^{r−1} 个，总共 744 个。这里遍历的是已经数学证明充分覆盖的有限离散类型集合，既不扫描 n/p，也不做数值参数搜索。

原定义的积分可统一化为有理分段：当 ξ≤1，

\[
 I=C_m-m\xi+\xi^2/2,\quad
 C_m=3/2+(m-1)H_{m-2}+H_{m-1}/2;
\]

当 1≤ξ≤m，

\[
 I=\sum_{h=1}^{m-1}\frac{(m-1-h\xi)_+}{h}
  +\sum_{k=1}^{m-1}\frac{\min\{1,(m-k\xi)_+\}^2}{2k}.          \tag{8}
\]

断点只有 1,m,(m−1)/k,m/k。逐段 objective 为有理二次式，其最小值由端点及有理驻点严格取得。配套证书给全部有限类型的放宽成本最小值：

| r | 实际秩 m | 全部类型数 | 最小放宽成本 |
|---|---:|---:|---:|
|1|4|24|61/32|
|2|5|48|39/20|
|3|6|96|4357/2160|
|4|7|192|59/28|
|5|8|384|521/240|

所有值严格大于 7/5>log 4。例如 r=1 的 61/32 确为自然四行可达到的最优值：e=(0,1,2,2)、仅 Li3 行一列 b=1，τflat=7/16、τsharp=47/32。纯 e=(0,1,2,3) 的值 63/32 稍差。log4<7/5 可由 e^{7/5} 的正 Taylor 项截断已超过 4 严格证明。

### 2.2 任意高秩部分无须继续搜索

若 r≥6，即使把原四行全部免费处理，T 行由 (2) 给

\[
 \tau^\flat\ge
 B_r:=\frac1{(r+3)^2}\sum_{\ell=2}^r(2\ell+5)H_{\ell-1}.
\]

在 r=6，B6=199/135>7/5。B_{r+1} 是 B_r 与 H_r 的严格凸平均，因为新行权重为 2m+1，且 H_r 大于旧表所有非零行和；所以 B_r 严格递增。

**自然 Tate 增秩结论。** (6) 中追加任意有限数量的连续对数幂，允许全部固定 n^e/lcm 类型与全部行排序，在原 slit Ω=C\[1,∞) 的任何合法 holomorphic 圆盘映射上都没有正门槛。因为 slit 的 conformal radius 为 4，而 (7) 的成本总是大于 log4。

范围只是 (6)、固定类型、原变量和这个 slit。并未证明全部 multiple polylogarithm 辅助函数、任意 gauge、代数覆盖或 multivalent 映射都无望。

## 3. 有真正奇权 overconvergence 的 ζ(3) 尾系统

为了不把纯 Li3 端点减常数误作 CDT 触发器，另核一个已有真正奇权触发器的体系。经典身份为

\[
 \zeta(3)=\frac52\sum_{k\ge1}\frac{(-1)^{k-1}}{k^3\binom{2k}{k}}.
\]

定义 C_n=binom(2n,n)，c∈Q 固定，

\[
 f_c(z)=\sum_{n\ge0}C_n\left(c-\frac52\sum_{k=1}^n
 \frac{(-1)^{k-1}}{k^3C_k}\right)z^n.                          \tag{9}
\]

从 C_n 的递推直接得

\[
 (1-4z)\theta f_c-2zf_c=\frac52\operatorname{Li}_2(-z),
 \quad\theta=z\partial_z.                                   \tag{10}
\]

真值 c=ζ(3) 正好消掉 z=1/4 的齐次平方根分支。其实际芽在 C\(−∞,−1] 延拓为 holomorphic；这可由 (10) 的 variation-of-constants 与 (9) 的尾恒等式核对。若反证假设 c∈Q，则该过度延拓芽确为 Q 系数芽，接口是真实的。本文使用这个已知 ζ(3) 身份检查方法，不把已知结果当成本项目的新成功；原始系列及其广义式可参 [Borwein–Bradley](https://arxiv.org/abs/math/0505124)。

### 3.1 移位素数层与精确前缀主指数

对所有充分大奇素数 p（排除 5 和 c 的分母素数），C_p≡2、C_{p+1}≡4 (mod p)。k=p 的和式项有赋值 −3；k<p 的 C_k 最多有一次 carry，故相应项赋值≥−1；k=p+1 项为 p 整。因此

\[
 v_p([z^{p+1}]f_c)=-3.                                      \tag{11}
\]

对 q=p^a，k<q 若 b=v_p(k)，C_k 的 carry 最多 a−b 层，给 −3b−(a−b)≥−3a+2；k=q 有唯一 −3a，k=q+1 为单位项。所以

\[
 v_p([z^{q+1}]f_c)=-3a.                                    \tag{12}
\]

完整安全分母是 2q_c L_N³，其中 q_c 清 c。一个自足证明如下：置 a=floor(log_p N)。若 v_p(k)≤a−1，v_p(C_k)≤a+1−v_p(k)≤3(a−v_p(k))。若 v_p(k)=a，所有较低 carry 都为零，最高可能的 carry 也在 C_N 中出现，所以 v_p(C_k)≤v_p(C_N)。因此每个 C_N/(k³C_k) 项均具有赋值≥−3a；乘固定 5/2 后得到上界。这个证明也覆盖 p=2。合并 (12) 后

\[
 \log\delta_{f_c}(N)=3N+o(N).                              \tag{13}
\]

(11) 的序号 p+1 与 p 互素，迫使目标行在任意 e 下仍有三个 b≥1、σ_f≥3。与旧 ζ(7) 自然目标的七层结论不同，这是最低奇权真正 overconvergence 模型的完整算术检查。

### 3.2 实际增秩和全部自然类型成本

追加 Tℓ(−z) 得

\[
 (1,\operatorname{Li}_1(-z),\operatorname{Li}_2(-z),f_c,
 T_2(-z),\ldots,T_r(-z)),\quad m=r+3.                         \tag{14}
\]

实际秩恰为 m。对数幂/低 Li 的独立性同 §2。若 f_c 有这样的有理表达，最高对数幂系数 Q 满足 θQ−2z/(1−4z) Q=0；其非零齐次解为 const/√(1−4z)，不是有理函数，故逐级排掉各个对数幂。余下 Li2 的有理系数 P 须满足

\[
 P'-\frac2{1-4z}P=\frac5{2z(1-4z)}.
\]

在 z=0，P 的极点会让左侧产生至少二阶极点；所以 P 必正则，而右侧有非零简单残数，矛盾。这证明真实 f 商方向，没有把 c 是否等于 ζ(3) 的未解假设偷进独立性证明。

由于 σ_f≥3 与 e_f 无关，最低成本只需 e_f=0。六个原低类型及每个辅助行 e=0/1 给 186 个有限配置的完整放宽检查：

|r|1|2|3|4|5|
|---|---:|---:|---:|---:|---:|
|最低放宽成本|17/8|103/50|223/108|59/28|521/240|

全部大于 log4。r≥6 再用 B_r。故任意有限数量纯 Tate 对数幂，也不能救这个真正 ζ(3) 尾系统的原 slit 自然模板。这并不否定 ζ(3) 的既有无理性证明，更不否定新的 holonomy 模板；它说明“多积分、多函数”本身不足。

## 4. 多值解析覆盖：哪些障碍不能跨过去

上一节的 4 是 slit 的上界，**不是所有 admissible multivalent maps 的上界**。纯 Li/T 系统可用 modular λ(q)，其 q 展开 λ=16q+...，在 0 之外不取 0 或 1；实际各个 Li/T 原点芽拉回后在圆盘 holomorphic。缩小 q 圆盘到 radius ρ<1，可得到满足闭盘邻域条件的映射 λ(ρq)，导数为 16ρ。因此 pure Li3 的 61/32 成本确可让 log(16ρ)−τ>0。

但一个正门槛只是判据的分母为正，还须证明完整 capacity/rearrangement numerator 的商小于实际秩。更关键的是，纯 Li3 从一开始就有 Q 系数；假设 ζ(3) 或某个 Li3 端点有理并不会改变此元组。减一个有理常数不会改变任何既定 φ 的 meromorphic 拉回，故不能凭这些真实存在的函数产生新的条件性矛盾。

对 (9)，直接用 −λ(q) 则还必须核全部 λ(q)=−1/4 的 preimages 是否落入正确 univalent leaf，是否都对应消掉 1/4 分支的 canonical sheet。单个正实 branch 的消去不保证其他 fibers 上也消去。本文没有断言此拉回已合法。这正是 [CDT Proposition 2.9.3、§9 的 descent datum](https://math.berkeley.edu/~ytang/L2chi.pdf) 必须保留的解析条件。其 §2.8 也明确区分多值的 16 与 univalent 的 4；不能把 §2/§3 的 slit 结论改写为全方法否定。

## 5. level12 ζ(7) 的完整整数 packet 接口

这部分为 root/paper 分支的真实 weight8 Eichler 候选提供算术接口，不替代该分支的 period polynomial、目标纯性或 modular coordinate 构造。一般先假设

\[
 f_7(q)=\sum_{n\ge1}\frac{a_n}{n^7}q^n,\quad a_n\in\mathbf Z,
 \qquad a_p\equiv u\ne0\pmod p
\]

对所有充分大素数成立。当前 level12 F8 候选已由独立几何分支核得 a_p=4(1+p⁷)，故 u=4。令

\[
 A(q)=E_6(\tau)-1728E_6(12\tau)\in\mathbf Z[[q]],
 \quad A_0=-1727,\quad A_1=-504,
\]

并取 H_c=A(f7−c)。真目标归一化 c=209ζ(7)/432；不能漏掉该非零有理系数，也不能将真实 Fricke period polynomial 的其他 Tate项当成零。

### 5.1 原 q 坐标与任意整数模坐标反演

设 q=Q(x)∈xZ[[x]]，Q′(0)=1，且 inverse x(q) 也整。这是本节的明确坐标假设，必须由真实 Hauptmodul 另证。对固定 r∈Z、p 足够大，最高 p⁻⁷ 层只有 f7 的 k=p 项。Frobenius 给

\[
 Q(x)^p\equiv Q(x^p)\equiv x^p\pmod{(p,x^{2p})}.
\]

因此对固定 r≥0，

\[
 p^7[x^{p+r}]H_c(Q(x))\equiv u[x^r]A(Q(x))\pmod p.            \tag{15}
\]

其他 k<p 项全部 p 整；k>p 且 k<p+r 也不含 p 分母。固定 c 项同样 p 整。取 r=1，右侧为 4·(−504)=−2016，于是所有充分大 p 有

\[
 \boxed{v_p([x^{p+1}]H_c(Q(x)))=-7.}                          \tag{16}
\]

故原 q 坐标和任意这样的整数反演，自然目标行都必须有七列 b≥1，无论 e 多大。这是局部类型结论，不把共同前缀指数直接当成 τ。完整安全分母为 q_c L_N⁷，而 (16) 强制实际前缀指数恰为 7。两向整坐标的 unipotent triangular 变换还证明每个 N 的 δ 完全相等。

这说明虽然 f7 本身是纯 n⁷ 类型，乘权六周期后却不能仍以 e=7 免费付费。反之，七列 b=1 只是该行的安全成本；对完整独立系统还需 nested row weights、全部 e 与实际 rank。

### 5.2 固定有理微分操作的条件结构

对固定 P∈Q(x)[θ]，先排除其系数/首项的有限坏素数。允许 Laurent coefficients 时，只会多用有限固定 offsets。最高 packet 的一般形式为

\[
 p^7[x^{p+r}]P(H_c(Q(x)))
   \equiv u[x^r]P(A(Q(x)))\pmod p.                            \tag{17}
\]

理由是 θ(x^p B)≡x^p θB (mod p)，以及固定有理乘子的好素数展开全部 p 整。若 P(A(Q(x))) 有某个非零的 r≠0 Laurent 系数，则 n=p+r 与 p 互素，(17) 给七层不被 n^e 清掉的见证。P 的固定坏素数和 r 的符号不会改变 all-scale 结论。

若 PA=0，H_c 的目标系数 −c PA 同时消失；不能将这种消去当作保留 ζ(7) 的廉价方向。若 PA 是非零常数，则 (17) 只在 r=0 见证，确不能据本论证强制七列，故必须单列此例外。

一个可闭合该例外的充分输入是：A(Q(x)) 的完整 homogeneous differential module 为非平凡不可约 Sym6(SL2)。其在 Γ0(12) 的 monodromy Zariski 稠密条件下自然出现；若实际模块与坐标已核对，则任何 PA≠0 不能是有理函数。否则 PA 属于 A 的完整 differential span，其 C(x) 一维 span 对导数稳定，产生一个非零 trivial submodule，与非平凡不可约性矛盾。P 本身一般不是水平 module morphism，不据此称其像为 quotient。因此每个保留目标的固定 P 都有 r≠0 的 packet。这里明确列出所需模块辨识，不能仅凭“weight6”口号视为已证。

### 5.3 实际 level12 坐标及 rank8 主账本

根分支选定

\[
 h=\frac{\eta(\tau)^3\eta(4\tau)\eta(6\tau)^2}
 {\eta(2\tau)^2\eta(3\tau)\eta(12\tau)^3},\quad
 x=1/h,\qquad t=\frac{x}{1+8x+12x^2}.                         \tag{20}
\]

η 的乘积直接给 x=q+Z[[q]]；有首项 1 的整形式反演递推不引入任何分母，所以 t=q+Z[[q]]、q=t+Z[[t]]。η 的变换还给 h(Wτ)=12/h(τ)、x(Wτ)=1/(12x)，故 t 真为 Fricke invariant。二次 discriminant 为 16t²−16t+1，分支 α=(2−√3)/4、β=(2+√3)/4。其 cusp 原点未 ramified；不能把它误作 §6 从 x² 起步的标准 involution descent。这里的 integrality、Fricke 有理恒等式和 discriminant 均有自足代数核验；(20) 的全 Hauptmodul、其它 cusp 和完整 period 模型由几何分支另证。

**完整 rank8 的预算接口。** 若几何分支已建立

\[
 \mathcal W=\langle1,H,\theta_tH,\ldots,\theta_t^6H\rangle_{\mathbf Q(t)},
 \quad\dim\mathcal W=8,
\]

并证明 A 的 homogeneous 最小模块为上述 rank7 Sym6，则所有固定 Q(t) 基都有

\[
 \boxed{\tau^\flat\ge7\left(1-\frac1{8^2}\right)
 =\frac{441}{64}=6.890625.}                                 \tag{21}
\]

证明：定义 target-coefficient map 1↦0、PH↦PA。rank8 与 rank7 假设使它良定义、满射且核恰为 Q(t)·1。任意固定基中至多一行落入此核。其余至少七行的 PA 都不为零，且不为有理常数，于是 (17) 各给某个固定 r≠0 的七层 packet，强制 σ_i≥7。nested rows 自身非递减，所以 σ2,...,σ8≥7；代入 (7) 得 (21)，而 τsharp≥0。新的有理乘子在其固定坏素数处可能还增加成本，本论证只给好素数下界，没有漏记为免费操作。

Sym6 中“不为零就不能有理”的部分也可直接由 monodromy 证明：对 γ∈Γ0(12)，A 的支为 (cτ+d)^6 A；轨道张成 τ^jA（0≤j≤6），且有限指数 Γ0(12) 在 SL2 中 Zariski 稠密，Sym6 不可约。固定有理微分算子与 monodromy 交换；若 PA≠0，它在这七维空间上的核为零，像仍为非平凡不可约七维表示。单值有理 PA 只张成一维 trivial 表示，矛盾。需要另证的是该轨道与所用 algebraic t-coordinate 的完整 homogeneous 最小模块相符，而不是群表示论本身。

自然七行 θ_t^jH 不增加前缀分母；其已由 (17) 强制指数 7，安全型仍是固定 q_c L_N⁷。七列 b=1 从第二行开始、所有 e=0，确达到自然主表的 τ=441/64。因此不能把 1+七行 σ7 算成单个 σ7，或把纯 n⁷ 源的成本放到这些乘子后的行。

这里的 A 只用于追踪目标系数，**没有免费加入 A 或其导数作为同一解析叶上的辅助芽**。H 在真 Θ 时跨 α，A 本身不跨该 branch，所以把它直接 adjoin 会破坏正在利用的解析改善。若要改变 (21)，应构造实际额外便宜背景、改变 target-coefficient quotient 或新的整 projection，并重新计其完整 rank/types。本文的结论不涉及这些尚未构造的更大系统，也没有算出合法 φ 的最终 capacity 商。

### 5.4 在该奇权八维模型追加任意数量纯 Tate 行

根分支的 [level12 完整模型](cdt_odd_level12_model_20261005.md) 已独立审过 rank8 与 rank7 Sym6 的辨识；本节在这个明确模型上继续计费。置

\[
 \mathcal W_r=\mathcal W+\langle T_1(t),\ldots,T_r(t)\rangle_{\mathbf Q(t)},
 \qquad T_j=(-\log(1-t))^j/j!,\qquad m=8+r.                 \tag{22}
\]

实际秩确为 m：对数模块是 unipotent；W 的 composition factors 为一个 trivial factor 与非平凡不可约 Sym6。因此其与完整 unipotent 对数模块的交至多是一个 trivial factor，而实际常数行已给这个交。所以交恰为 Q(t)·1，新增 r 行实际独立。这个证明使用完整 differential module，未把纯对数幂的形式数量当作 rank。

以下预算是自然元组 (1,H,θ_tH,...,θ_t^6H,T_1,...,T_r) 的全部固定类型与全部行排序；也允许仅在原 W 内作保持目标的固定换基。它没有自动覆盖把对数行与目标行任意混合的 Q(t) gauge。要升级到整个增广空间的任意 mixed basis，尚需额外 packet/filtration 论证；实际秩证明与这种算术升级是两件事。

目标七行仍各要求 σ≥7；新 T_j 行的必要和为 H_j（e=0）或 H_(j−1)（e≥1）。超过 1 的 e 没有进一步降低行和，只增加 sharp，故 e_j∈{0,1} 完整覆盖最小化所需选择。对 r=0,...,10，共 2047 个配置的精确计算同时输出两种不同量：按行必要和排序的**放宽下界**，以及所有列均取 b=1 的**合法嵌套安全上界**。后者用 T_j 的安全 n^{e_j}L_n^{j−e_j}，目标七行用 L_n^7，按整数活动列数排序；每一列为零前缀与常数尾，确符合 CDT 的表结构。固定 j! 清因子不改变预算。并未假定各个 H_j 最优分数列能与目标七列兼容。

|r|实际秩|全部 e 配置|最低放宽成本|合法单位列安全成本|
|---|---:|---:|---:|---:|
|0|8|1|441/64|441/64|
|1|9|2|542/81|542/81|
|2|10|4|259/40|13/2|
|3|11|8|2275/363|769/121|
|4|12|16|10501/1728|301/48|
|5|13|32|4991/845|1056/169|
|6|14|64|3223/560|44/7|
|7|15|128|44273/7875|287/45|
|8|16|256|394561/71680|234133/35840|
|9|17|512|11569/2142|544793/80920|
|10|18|1024|4335421/816480|163441/23328|

这里的安全成本是一个实际可行表给出的上界，不称全部嵌套类型的最优值；放宽成本才是涵盖全部固定类型的下界。r=10 的下界约 5.310，而合法单位列表的最低值在列出的范围内为 r=5 的 1056/169，约 6.249。

**无须扩大有限类型搜索的全 r 下界。** 只用 flat 就有

\[
 \boxed{\tau^\flat(1,H,\ldots,\theta_t^6H,T_1,\ldots,T_r)
 >\frac{43}{10}\quad\text{对所有整数 }r\ge0.}                \tag{23}
\]

证明如下。把全部对数行都放宽为最小 H_(j−1)。若 r≤235，由 H235<7，七个目标行在排序后位于尾部；对数行的位置为 j+1。交换调和数求和次序得到

\[
 \sum_{j=1}^r(2j+1)H_{j-1}
 =r(r+2)H_r-\frac{r(r+5)}2.
\]

所以这个最宽松 flat 下界为

\[
 F_r=\frac{r(r+2)H_r-r(r+5)/2+7(14r+63)}{(r+8)^2},\qquad
 (r+8)^2\left(F_r-\frac{43}{10}\right)
 =r(r+2)H_r-\frac{24}5r^2+\frac{267}{10}r+\frac{829}5.       \tag{24}
\]

在 0≤r≤10，只取目标尾七行就已大于 43/10：其和为 7(14r+63)/(r+8)^2，严格递减，而 r=10 仍大于 43/10。在 10≤r≤20、20≤r≤30、30≤r≤45、45≤r≤70，分别代 H10>29/10、H20>359/100、H30>399/100、H45>439/100；(24) 分子被下述凹二次式严格控制：

\[
 -\frac{19}{10}r^2+\frac{65}2r+\frac{829}5,\qquad
 -\frac{121}{100}r^2+\frac{847}{25}r+\frac{829}5,\qquad
 -\frac{81}{100}r^2+\frac{867}{25}r+\frac{829}5,\qquad
 -\frac{41}{100}r^2+\frac{887}{25}r+\frac{829}5.
\]

各个区间的两个端点都严格为正，凹性给整个区间严格为正。70≤r≤235 用 H70>483/100，(24) 的二次、一次、常数系数都为正。所有这些调和数界都是精确有理数界，配套证书核其值与端点。

最后 r≥236 时不再假设目标是最末七行。由 H56>23/5，除常数及至多 56 个早期对数行外，其余所有行的 σ≥23/5（目标行的 7 更大）。排序后前 57 行可免费放宽，故

\[
 \tau^\flat\ge\frac{23}5\left(1-\frac{57^2}{(r+8)^2}\right)
 \ge\frac{23}5\left(1-\frac{57^2}{244^2}\right)>\frac{43}{10}.
\]

这完成所有 r 的证明。它说明这个具体纯 Tate 背景族不能把算术门槛压到 43/10 或更低；没有给全部 modular 解析映射的 φ′ 或 capacity 上界。

可与一个**明确指定的覆盖族**连接。若使用 [CDT (9.0.1) 与 Appendix (A.0.1)](https://math.berkeley.edu/~ytang/L2chi.pdf) 的 h_Y0(2)=λ²/(λ−1)=−256q+... 标准芽（normalized branch 4、原点导数绝对值 256），令 φ=(β/4)h_Y0(2)∘ψ，其中 ψ:D→D、ψ(0)=0，则 Schwarz 引理给

\[
 |\varphi'(0)|\le64\beta=16(2+\sqrt3)<60,
 \qquad\log|\varphi'(0)|<41/10<43/10.
\]

最后的严格界可由 √3<7/4 与 exp(41/10) 的正 Taylor 截断大于 60 核验。于是对这个覆盖族与上述自然元组的全部 r，连 CDT 的正分母门槛都不能满足；不必继续算 capacity numerator。此推论只使用所指定 h-cover 的导数规范，合法解析叶仍应按几何模型核对。没有把这个界当作其它 admissible multivalent maps 的普遍上界，也未排除更便宜的不同背景、任意 mixed gauge、真正 trace 或改变目标商的投影。

## 6. 真实 trace 确可能改变最高 packet

这节给一个完全精确的可计算基准，强调上一节不跨真正 Fricke projection。取标准 integer involution

\[
 w(x)=x/(x-1),\qquad y=x+w(x)=x^2/(x-1).
\]

以下固定 j≥2；j=1 的 plus trace 恒为零，不适用非零赋值结论。置 T_j^+(y)=Li_j(x)+Li_j(w(x))。两根 x,w 满足 sum=product=y，power sums P_k(y) 满足 P0=2、P1=y、P_k=y(P_{k−1}−P_{k−2})，且

\[
 [y^n]P_k=(-1)^{k-n}\frac{k}{n}\binom n{k-n}\quad(n\le k\le2n).
\]

所以

\[
 \boxed{[y^n]T_j^+=\frac1n\sum_{h=0}^n
   \frac{(-1)^h\binom nh}{(n+h)^{j-1}}.}                     \tag{18}
\]

完整安全类型是 n L_{2n}^{j−1}，不是 blind L_{2n}^j。对每个大奇素数 p，n=(p+1)/2 时唯一 p 分母项为 k=p，binom(n,p−n)=n 是单位；因此

\[
 v_p([y^{(p+1)/2}]T_j^+)=-(j-1).                            \tag{19}
\]

由于 p∤n，任何固定 n^e 不能清 (19)，而 b<2 的有限 scales 都最终到不了 p；故至少 j−1 个 b≥2。对 j=7，自然 trace 行的必要 σ 是至少 12，并有 e=1、六列 b=2 的完整安全类型。这正好体现真实消掉一层，但尺度也翻倍；不能只记层数 7→6。

最高层消去亦可在原 x 看出。若 A∈Z[[x]]，由 w(x)^p≡w(x^p)≡−x^p (mod p,x^{2p})，H=A(Li_j−c) 的 plus trace 最高 packet 比例于 A(x)−A(w(x))，而目标系数是 −c(A(x)+A(w(x)))。当 A 是 w-even，前者为零而后者不为零。因此 **trace 有可能保住目标并消掉算术首层**，不能用 §5 的 fixed-operator 结论将它提前排除。

当前 level12 Fricke 不是未经证明就等于这个标准 w。它原先交换不同 cusps；q(−1/(12τ)) 也不是 q=0 的普通整形式代入。必须先证明实际 invariant coordinate、两 cusp 的规范 expansions 与目标/Tate period polynomial，才可套合适的 trace 整性定理。一般 plus descent 若只知安全 L_n⁷，CDT §9 Lemma 9.0.3 给 L_{2n}⁷；改善到 (18) 类 integrated 类型必须另证，不能从符号 trace 自动获得。

## 7. 尚未闭合的目标与可执行的后续接口

本轮未证明新的奇数 ζ/L 无理性或线性无关性。可证的障碍仅限明确自然族、固定类型与已说明 slit；合法 multivalent cover、完整 Fricke trace、非自然整格、新的 Eichler 周期投影仍可能改善。

level12 ζ(7) 主线需要同时完成：

1. 真 c=209ζ(7)/432 的 period polynomial 与全部 Tate项，证明所选 H 在指定 singular fibers 过度延拓；
2. integer Hauptmodul 与 inverse、真实 Fricke coordinate，以及 trace 后每行的完整分母；
3. target-preserving 完整 module 的实际独立秩，必要时核 Sym6 假设；
4. 对全部 fibers 合法的 univalent leaf / meromorphic pullback，并以同一坐标的完整 capacity integral 给 strictly rank-small holonomy quotient。

§5 把 q→x 这一环的自然行首层预算做实，§6 则精确表明 trace 为什么仍是值得推进的不同环节。它们不以 weight2 转移或已知 ζ(3) 替代 ζ(7) 的成功条件。

## 8. 证书与文献定位

配套 `cdt_odd_holonomy_budget_20261005_verify.py/json` 包含 744+186 个原族穷尽离散类型、2047 个 rank8＋Tate 离散类型的有理二次最小值、一个固定 log packet、一个固定 j=7 trace coefficient、level12 −2016 packet，以及 (23) 的精确调和数/凹二次端点证书。有限实例不替代 (1)、(11)、(15)、(19)、(23) 的全尺度证明；没有 n/p 参数扫描。

本次主要原始来源为 [CDT 主文](https://math.berkeley.edu/~ytang/L2chi.pdf)：§2.8/2.9 的合法 multivalent/overconvergence 接口，Definition6.0.1/Theorem6.0.2 的实际成本，§9 的整数 involution/descent，以及 §10.3 已存在的 multiple-polylogarithm 辅助空间。后者不能直接替代本文不同的完整自然类型分类。真实奇权逆二项式身份见 [Borwein–Bradley 原始预印本](https://arxiv.org/abs/math/0505124) 与其项目内已归档证明来源；新版 arithmetic holonomy 论述见 [CDT arXiv:2510.04156](https://arxiv.org/abs/2510.04156)。本文的 packet 与类型定理有自足证明，不依赖未发表的广泛 conjecture。
