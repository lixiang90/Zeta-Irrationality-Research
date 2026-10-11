# 奇权 rank8＋对数模块：任意固定混合基的全尺度算术过滤

日期：2026-10-05。本稿新建；前轮 `cdt_odd_holonomy_budget_20261005.md` 及所有旧稿保持冻结。本文补上其 §5.4 明确未覆盖的 mixed Q(t) gauge，证明任意固定混合基的 flat 成本仍严格大于 43/10。尚未证明 ζ(7) 无理，结论限同一 t 变量、同一增广空间和固定 CDT 类型；不跨新覆盖或不同周期投影。

## 1. 精确对象、目标商与适用范围

采用已建立并独立审过的 [level12 整模型](cdt_odd_level12_model_20261005.md)：

\[
 A=E_6(\tau)-1728E_6(12\tau),\qquad
 f_7(q)=\sum_{n\ge1}a_nq^n/n^7,\qquad
 H_c=A(f_7-c),\quad c\in\mathbf Q.
\]

实际 ζ(7) 目标的规范是 c=209ζ(7)/432。系数 a_n 整，所有充分大素数 p 有 a_p≡4 (mod p)，A_0=−1727、A_1=−504。Fricke 商坐标 t=q+Z[[q]] 的反演 q=t+Z[[t]] 同样整。

\[
 \mathcal W=\langle1,H_c,\theta H_c,\ldots,\theta^6H_c\rangle_{\mathbf Q(t)},
 \quad\theta=t\partial_t,\quad\dim\mathcal W=8.
\]

其齐次七阶模块 \(\mathcal S\) 为非平凡不可约 Sym6(SL2)。目标系数映射给完整正合列

\[
 0\longrightarrow\mathbf Q(t)\cdot1\longrightarrow\mathcal W
 \xrightarrow{\pi}\mathcal S\longrightarrow0,
 \qquad \pi(PH_c)=P(A),\quad\pi(1)=0.                       \tag{1}
\]

这是完整 rank8 模型中的真实模块，不是形式计算未知常数的系数。尤其非零 P(A) 不能是有理函数：否则其微分张成中有一个 trivial submodule，与 Sym6 不可约性矛盾。模块及实际秩的输入已由同一模型的七阶非齐次方程和非零 log⁷ 尖点项证明，本文不将模形式的 q 展开裸当作 D-finite。

令 L=−log(1−t)，T_j=L^j/j!，并置

\[
 \mathcal U_r=\mathbf Q(t)[L]_{\le r},\qquad
 \mathcal V_r=\mathcal W+\mathcal U_r\quad(r\ge0).
\]

U_r 为 rank r+1 的 unipotent 对数模块。W 的 composition factors 恰为一个 trivial factor 与非平凡 Sym6，故 W∩U_r=Q(t)·1。于是 V_r 实际秩 m=r+8，π 延拓为 V_r→S，且

\[
 \ker\pi=\mathcal U_r.                                      \tag{2}
\]

以下允许 **V_r 的任意固定 Q(t) 基**，每行需为原点正则的 Q 系数芽，且给定合法 CDT 分母型

\[
 d\, n^{e_i}\prod_j L_{\lfloor b_{i,j}n+c_{i,j}\rfloor}
 \quad\text{清第 }n\text{ 个系数},
\]

其中 d 为固定整数、e_i 非负整数、列 b 为零前缀与固定常数尾，全部 offsets 和参数固定，σ_i=Σ_j b_{i,j}。不允许随 N 或 p 变化的 gauge、基或 scales。某个固定有理 gauge 在有限坏素数处可能产生指数分母；本文不把该成本免掉，只在确有上述合法类型时给必要下界。所有好素数外的成本只能额外增加，不能削弱这里的下界。

## 2. 两种不同位置的精确 packet

### 2.1 n=p+s 的目标七层不被对数混合消去

固定有理函数 R(t) 的 Laurent 系数，在除去有限素数后全部 p 整。证明只需把分母写成 t^vB(t)，B(0)≠0，清固定系数分母并排除 B(0) 的素因子，再用逆级数递推。固定有理微分算子也只引入有限 Laurent offsets；微分本身不添系数分母。

对每个固定整数 s，n=p+s<p²，且 n 加这些有限 offsets 仍小于 2p。T_j 的展开是 j 个正整数指标的乘积；在这些指标的和小于 2p 时至多一个指标含 p。因此任意固定

\[
 u=\sum_{j=0}^r Q_j(t)T_j\in\mathcal U_r
\]

在 n=p+s 处的系数赋值至少 −1。这包括大于 7 的固定 j，也包括有理 Laurent 乘子。只有一层的位置与约 7p 的七层位置不能混同。

另一方面，Frobenius 给 q(t)^p≡t^p (mod p,t^{2p})。H_c 的最高 p⁻⁷ 层仅来自 f_7 的 k=p 项，故对任意固定 P∈Q(t)[θ]，

\[
 p^7[t^{p+s}]P(H_c)\equiv4[t^s]P(A)\pmod p.                 \tag{3}
\]

有理乘子的 finite Laurent offsets 不改变这个恒等式；θ(t^pB)≡t^pθB (mod p)。固定 c 项在好素数处整，乘 p⁷ 后为零。

若 h=P(H_c)+u 且 π(h)=P(A)≠0，由 (1) P(A) 非有理，尤其不是常数。它的 Laurent 展开必有一个固定 s≠0 的非零有理系数。排除该系数的有限素因子后，(3) 加上 u 至多一层给

\[
 v_p([t^{p+s}]h)=-7\quad\text{对所有充分大 }p.              \tag{4}
\]

因为 p∤(p+s)，任何固定 n^e 都不能支付这些层；每列有限 b 在 n≈p 处至多给一次 p，b<1 的列最终没有 p。因此

\[
 \boxed{\pi(h)\ne0\Longrightarrow\sigma(h)\ge7.}             \tag{5}
\]

这一结论允许全 mixed 基，不局限自然目标行。高次对数的 p⁻⁷ 项确可能存在，但首次约在 7p，无法取消 (4) 的 p+s packet。

### 2.2 n=ap+s 的纯对数完整过滤

令非零 u∈U_r 的最高对数 degree 为 ℓ，即

\[
 u=\sum_{j=0}^{\ell}Q_j(t)T_j,\qquad Q_\ell\ne0.
\]

对任意固定 1≤a≤ℓ 和整数 s，所有充分大 p>r 有

\[
 p^a[t^{ap+s}]u\equiv\frac1{a!}[t^s]
       \sum_{j=a}^{\ell}Q_j(t)T_{j-a}\pmod p.               \tag{6}
\]

自足证明：在和为 ap+s 加有限 Laurent offsets 的指标中，至多 a 个含 p；若有 a 个，最低总和 ap 迫使它们全等于 p，其余指标的和以及乘子的指数都是固定的。展开 T_j 时选择这 a 个因子的组合数与 j! 正好给 1/a! 乘 T_{j-a}。少于 a 个 p 因子贡献在乘 p^a 后消失。有限 offset 的尾部还不足以容纳 a+1 个 p 因子；p² 大于所有相关指标。分母 j!、a! 以及固定有理乘子的坏素数被有限排除。这也解释为什么需要完整 packet 函数，而不是仅检查最早的一个系数。

当 1≤a≤ℓ−1 时，右侧的对数多项式最高 degree 为 ℓ−a，最高系数 Q_ℓ 非零。L 对 Q(t) 超越：绕 t=1 重复 monodromy 将 L 变成 L+2πik，一个非零最高 degree 的有理系数多项式不可能对全部整数 k 相消。因此该函数不是常数。其 Laurent 级数有某个固定 s≠0 的非零系数；(6) 因而给精确赋值 −a，且序号 ap+s 为 p-unit。每个固定 scale 在该序号至多给一次 p，而 b<1/a 最终没有 p。所以 ℓ≥1 时，活动 scales 降序排列后满足

\[
 b_{(a)}\ge1/a\quad(1\le a\le\ell-1),\qquad
 \boxed{\sigma(u)\ge H_{\ell-1}.}                          \tag{7}
\]

若 e=0，再用 a=ℓ；Q_ℓ 非常数时选 s≠0，常数时选 s=0，均还要第 ℓ 层，得到 σ≥H_ℓ。对下文所有 fixed e 的统一 flat 下界，(7) 已足够。纯有理行 ℓ=0 只需使用 σ≥0。

每个 r 和固定基各有自己的有限坏素数集合；定理不要求一个与 r 无关的集合，也没有从少量素数样本推密度。

## 3. 可用于全部混合基的成本子级过滤

令 U_d=Q(t)[L]_{≤d}，其实际维数 d+1。由 (2)、(5)、(7)：

* 任何 σ<7 的行都在 U_r；
* 如果 H_d<7，任何 σ<H_d 的行都在 U_d；
* 任何 σ<23/5 的行都在 U_56，因为 H56>23/5，而非零目标行成本至少 7。

这些是 **函数子空间中的包含关系**，不是原 basis 的标签。一个独立基中落在维数 d+1 子空间的行至多 d+1。因此即使把 target 与所有对数行任意混合，也不能让太多行同时廉价。

将合法 CDT 的行和排序为 σ1≤...≤σm（nested 列本来就保证非递减）。若 r≤235，由 H235<7，得到

\[
 \sigma_i\ge H_{i-2}\quad(2\le i\le r+1),\qquad
 \sigma_i\ge7\quad(r+2\le i\le r+8).                        \tag{8}
\]

第一个界在 i=2 为零，显然成立；i≥3 时，假设 σ_i<H_(i−2)，前 i 行全在 U_(i−2)，该空间仅维数 i−1，矛盾。第二个界因为 σ<7 行全在维数 r+1 的 U_r。

当 r≥236 时同理，至多 57 行的 σ 可小于 23/5，即

\[
 \sigma_i\ge23/5\quad(i\ge58).                              \tag{9}
\]

(8)/(9) 恢复了自然表预算需要的全部维数约束。没有假定高 degree 对数必须单独保留为一个 basis 行，也没有将最高系数函数 PA 与常数 residue 随意混用。

## 4. 任意 fixed mixed 基的全 r flat 定理

CDT 的精细成本是

\[
 \tau^\flat=\frac1{m^2}\sum_{i=1}^m(2i-1)\sigma_i,
 \qquad\tau=\tau^\flat+\tau^\sharp,\quad\tau^\sharp\ge0.
\]

**定理。** 对每个 r≥0，V_r 的任意固定 Q(t) 基，只要具有上文的合法 CDT 类型，就有

\[
 \boxed{\tau^\flat>43/10.}                                  \tag{10}
\]

证明的最后实不等式完全自足如下。r≤235 时由 (8)，

\[
 \tau^\flat\ge F_r:=
 \frac{r(r+2)H_r-r(r+5)/2+7(14r+63)}{(r+8)^2}.
\]

这里 Σ_(j=1)^r (2j+1)H_(j−1)=r(r+2)H_r−r(r+5)/2，交换有限求和次序即可证明。

\[
 (r+8)^2(F_r-43/10)
 =r(r+2)H_r-\frac{24}5r^2+\frac{267}{10}r+\frac{829}5.        \tag{11}
\]

0≤r≤10 只用七个目标尾行就已足够，7(14r+63)/(r+8)^2 严格递减，而 r=10 时仍大于 43/10。在区间 [10,20]、[20,30]、[30,45]、[45,70] 分别用 H10>29/10、H20>359/100、H30>399/100、H45>439/100，(11) 被以下凹二次式严格控制：

\[
 -\frac{19}{10}r^2+\frac{65}2r+\frac{829}5,\quad
 -\frac{121}{100}r^2+\frac{847}{25}r+\frac{829}5,\quad
 -\frac{81}{100}r^2+\frac{867}{25}r+\frac{829}5,\quad
 -\frac{41}{100}r^2+\frac{887}{25}r+\frac{829}5.
\]

各段两个端点均严格正，凹性给全部区间。70≤r≤235 用 H70>483/100，(11) 三个系数都为正。r≥236 则由 (9)

\[
 \tau^\flat\ge\frac{23}5\left(1-\frac{57^2}{(r+8)^2}\right)
 \ge\frac{23}5\left(1-\frac{57^2}{244^2}\right)>43/10.
\]

因此前轮自然元组的全 r 下界，现升级到 **整个 V_r 的全部固定混合基**。升级来自 (3)–(9) 的全尺度 packet/维数过滤，而非重新排列行标签。

对前轮指定覆盖族 φ=(β/4)h_Y0(2)∘ψ、ψ:D→D、ψ(0)=0，β=(2+√3)/4，CDT 标准 h=−256q+... 的导数绝对值为 256，Schwarz 引理给 |φ′(0)|≤64β<60，故 log|φ′(0)|<41/10。合并 (10) 后，这个覆盖族与任意 fixed mixed basis 的 V_r 都无正 CDT 门槛。这里没有证明其它 admissible maps 的统一上界，不排除新覆盖、改变周期商、加入非 unipotent 的真正新背景或非固定 gauge。

## 5. 固定精确证书及尚可改进的方向

配套 [脚本](cdt_odd_mixed_filtration_20261005_verify.py) 与 [JSON](cdt_odd_mixed_filtration_20261005_verify.json) 不导入或运行任何旧 producer，不修改旧稿。它核三个有限实例来检验公式：

1. 使用真实 level12 Fourier 系数与整数 eta 坐标反演，在 p=13 时核 H_(p+1) 七层；
2. 用 mixed 行 (θ−1)^7H+(1+t)t^−8T9−2T2/(1−t)：首个目标 offset 被算子杀掉，但 p+2 仍有精确七层；
3. u=T8−tT7：在 a=7 时最初 offset1 的最高 packet 消失，offset2 仍为 (L−t)/7! 的非零系数，精确七层出现在 7p+2。

另核 (11) 的四段精确有理端点与所有调和数界。有限证书不代替 (3)/(6) 的全素数证明，更未扫描素数或随 n 搜索 gauge。

本轮没有构造降成本反例，反而排除了这一明确混合空间的降成本可能。可继续的方向必须改变本定理的至少一项输入：新的周期商、不属于 U_r 的背景、更好的实际解析覆盖，或随规模变化而需重新建算术账本的格。单纯给既有 target 与纯对数行混合、再把高 p⁻⁷ 项称作抵消，不能解决这一路线的预算缺口。

原始方法来源为 [CDT Definition 6.0.1、Theorem 6.0.2 与 (9.0.1)/(A.0.1)](https://math.berkeley.edu/~ytang/L2chi.pdf)。目标的真实 period、坐标与 rank 输入见本项目已审的 level12 模型；本文的纯对数 packet 与成本过滤是自足推导，不声称全球新颖性或新的 ζ(7) 无理性结果。
