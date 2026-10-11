# 第243轮：固定 K5 完整余项的预算接口

2026-10-09，B。固定240–242的同一 \(3n\) 全列池、泛函与
\(\widetilde Q_n=S_n^{3n}Q_n/F_n\)。数学程序、CAS/区间运算、素数或参数扫描均0。
本稿纸证整数greedy在 \(2n<p<3n\) 并不优于242完整class界；支付唯一商部危险次数带来的精确余项秩及其完整归一化收益。这个rank收益只有 \(1/24\)，不能被放大成实际费用下界或全路线反证。

## 1. 同一净费用与精确整数allocation

记 \(h=3n\)、\(R_n=D_n^4/D_{5n}\)、\(S_n=(5n)!/(n!)^4\)、
\(F_n=\prod_{i=0}^{h-1}(i!)^2\)，
\[
 g_p=\min_kv_p([T^k]\widetilde Q_n),\qquad
 \log d_n=\sum_p(-g_p)\log p
 \quad(d_n\widetilde Q_n\text{ primitive}).
 \tag{S1}
\]
只在 \(Q_n\ne0\) 的尺度上定义 \(d_n\)；241已经给每个固定有理关系点的无界非零尺度。
不取局部负费用的正部。

对 \(p\ge11,2n<p<3n\)，所有 factorial 参数均小于 \(p^2\)。
242的完整CRT bound采用
\[
 c_b=4N_b-C_b+[b=0]-4,\qquad
 G=\sum_b\{k_bc_b+k_b(k_b-1)\},
\]
从 \(c_b,c_b+2,\ldots\) 取最低 \(h\) 个整数slot。下面包括零类，并非continuous relaxation。

若 \(2n<p<5n/2\)，置 \(\tau=5n-2p\)，\(0\le\tau<n\)。
非零类分三组：
\[
 b\le\tau:c_b=-3;\quad \tau<b\le n:c_b=-2;\quad n<b<p:c_b=-6.
\]
零类 \(c_0=-5\)。最优选择为最后一组全部 \(-6,-4\)，
第一组全部 \(-3\)，零类 \(-5,-3\)。
总数 \(2(p-n-1)+\tau+2=3n\)，下一未选slot至少 \(-2\)，故
\[
 G=-5n-4p+2,\qquad
 \mathcal N_p=hv_p(S_n)-v_p(F_n)=2p,
\]
\[
 -g_p\le5n+2p-2.
 \tag{S2}
\]
若 \(5n/2<p<3n\)，置 \(\tau=5n-p>n\)。
非零类 \(b\le n,n<b\le\tau,\tau<b<p\) 的 \(c_b\) 分别为
\(-2,-6,-5\)，零类为 \(-4\)。
选择中组的 \(-6,-4\)、最后一组的 \(-5\) 和零类的 \(-4\)；
总数 \(2(\tau-n)+(p-1-\tau)+1=3n\)。于是
\[
 G=-15n+1,\qquad \mathcal N_p=2p-3n,\qquad
 -g_p\le18n-2p-1.
 \tag{S3}
\]
阈值相等的有限小尺度直接用原整数slot，不影响leading积分。

242完整class upper在这两个窗口分别为 \(4n+p+O(1)\) 与
\(29n-8p+O(1)\)。整数greedy的leading费用分别高出
\((1+p/n)n\)、\((6p/n-11)n\)，在全 \(2<p/n<3\) 都严格为正。
因此精确整数allocation不提供这个窗口的新宏观节省；这是比较两项已付upper，不是actual费用的比较。

## 2. 唯一商部危险次数给全系数余项秩

沿用242完整恒等式
\[
 S_nM_n=W_p(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\qquad
 \gamma_j=-p^{-5}\omega_j
 (H_{\lfloor j/p\rfloor}^{(5)}+3p^2H_{\lfloor j/p\rfloor}^{(3)}),
 \tag{S4}
\]
其中 \(\omega_j=S_nj\operatorname{Res}_{t=-j}R_n\in\mathbb Z\)、
\(v_j=((-j)^i)_{i<h}\)。所有商部、残数、调和头与 \(T\) 均保留。

现在限定 \(2n<p<5n/2\)，所以 \(v_p(S_n)=2\)。
242的全integer residue moments和完整unit-cycle证书使 \(W_p\) 的非 \(p\) 调和头、
以及全部 \(T\) 系数含 \(p^2\)。商部只需逐个monomial核 Bernoulli分母。
写
\[
 R_n=t^{-n}\sum_{\ell\ge0}q_\ell t^{-\ell},\qquad
 q_\ell\in\mathbb Z,\ q_0=1.
\]
完整商部degree不超过 \(5n-1<3p-2\)。
一阶 \(dB_{d-1}^+\) 的 \(d=p\) 分母被 \(d\) 清掉，
在此范围唯一未清掉的可能次数是 \(d=2p-1\)；
三阶首次未清掉的次数 \(4p-1\) 不在范围。
von Staudt–Clausen给 \(pB_{2p-2}^+\equiv-1\pmod p\)，
\((2p-1)\equiv-1\pmod p\)，所以
\[
 (W_p/p)_{ik}\equiv
 u_p\,q_{\,i+k-(n+2p-2)}\pmod p,\quad
 u_p=\tfrac32(S_n/p^2)\in\mathbb F_p^\times,
 \tag{S5}
\]
约定负下标系数0。多项式除法与 partial fractions中的额外常数不影响正次数 \(2p-1\)。
S5是完整多项式矩阵的约化；\(T\) 已消失于这层，不是选某个关系值后才成立。

置 \(r=\tau+1=5n-2p+1\)。S5只有最后 \(r\) 行列可能非零，
该 \(r\times r\) 块为 \(q_{a+b-\tau}\)、
\(0\le a,b\le\tau\)，反对角线全部为 \(q_0=1\)，其上为0。
因此
\[
 \operatorname{rank}_{\mathbb F_p(T)}(W_p/p\bmod p)=r.
 \tag{S6}
\]
这不证明任何完整determinant本身的mod-\(p\)非零。

在 \(\mathbb Q_p(T)\) 的Gauss valuation环中，用这块单位minor消元，
\(W_p/p\) 有 \(r\) 个单位pivot，其余pivot至少含 \(p\)。
所以任意 \(k\)-阶 \(W_p\) minor的所有系数满足
\[
 v_p^{\rm Gauss}(\text{minor})\ge k+(k-r)_+.
 \tag{S7}
\]
这一quotient环的估值结论等价于所有有理polynomial coefficients的minimum估值，不偷换成某个 \(T\) 的数值估值。

## 3. zero slots如何限制rank收益

将S7接入完整双minor展开。该项使用 \(t=\sum_bk_b\) 个atoms，
余项阶数为 \(h-t\)。完整Gauss下界是
\[
 g_p(\det(S_nM_n))\ge h+
 \min_{\substack{0\le k_b\le C_b\\ \sum k_b\le h}}
 \left\{\sum_b[k_b(\nu_b-6)+k_b(k_b-1)]
              +(h-t-r)_+\right\}.
 \tag{S8}
\]
同类双Vandermonde仍给 \(k_b(k_b-1)\)。这是全系数bound，未把不同类的实际evaluation限制免费加入。

此窗口slot列表包括零类，精确为：

| 类 | 数量 | 每类atoms对应slot |
|---|---:|---|
| \(b>n\) | \(p-n-1\) | \(-5\) |
| \(1\le b\le\tau\) | \(\tau\) | \(-2,0\) |
| \(\tau<b\le n\) | \(n-\tau\) | \(-1\) |
| \(b=0\) | 1 | \(-4,-2\) |

负slot共 \(p+1\)，另有 \(\tau\) 个zero slots。全部atoms
\[
 t_{\max}=p+1+\tau=5n-p+1\le h.
\]
每个slot非正，而且多取atom不会增大 \((h-t-r)_+\)，故S8的
**这个放松模型**恰在选全部atoms时最小。
不能跳过zero slots直接取 \(h-p-r\) 为额外收益。

原negative-slot和是 \(-(3p+n+1)\)，
\(v_p(F_n)=6n-2p\)。因此完整费用upper改善为
\[
 \boxed{-g_p\le4n+p+1-(3p-7n-2)_+.}
 \tag{S9}
\]
leading改善仅为 \((3x-7)_+\)、\(x=p/n\)，
发生在 \(7/3<x<5/2\)。PNT给其宏观节省
\[
 \int_{7/3}^{5/2}(3x-7)\,dx=\frac1{24}.
 \tag{S10}
\]
这准确支付余项mod-\(p\)rank输入本身的收益；未排除实际evaluation-annihilator、
更深内容或全过滤determinant还能给更多。

## 4. 当前certificate的精确必要收益接口

这一节只研究242已经选定的upper函数，绝不下估actual primitive费用。
记 \(P(x)=\psi(x)+6\)，\(\Phi\) 是242强余项九段表。
在 \(1<x<7/3\)，用242明确公式展开得

| 区间 | \(P(x)\) |
|---|---|
| \(1<x<5/4\) | \(49/4-3x-25/(4x)\) |
| \(5/4<x<4/3\) | \(91/4-9x-25/(4x)\) |
| \(4/3<x<3/2\) | \(59/4-3x-25/(4x)\) |
| \(3/2<x<5/3\) | \(35/4+x-25/(4x)\) |
| \(5/3<x<2\) | \(77/4-7x/2-25/(4x)\) |
| \(2<x<7/3\) | \(45/4+x/2-25/(4x)\) |

逐段 \(P-\Phi\) 的分子（统一分母 \(4x>0\)）是
\[
 -(16x-25)(x-1),\quad
 8x^2+11x-25,\quad
 -4x^2+27x-25,\quad
 -4x^2+27x-25,\quad
 14x^2-3x-25,\quad
 -2x^2+29x-25.
\]
第一项直接为正；其余在相应左端点为正且在该段递增。
因此242逐prime取优的宏观upper实际上在全部 \(1<x<5\) 都等于 \(\Phi\)。
置
\[
 I_{\rm in}=\int_0^1P(x)\,dx,\qquad
 12/5\le I_{\rm in}\le529/40.
\]
则当前certificate常数及 \(2<x<3\) 以外的贡献精确为
\[
 C_{242}=I_{\rm in}+12,\qquad
 C_{\rm outside}=I_{\rm in}+43/8,
 \tag{S11}
\]
因为窗口 \(2<x<3\) 的面积为 \(53/8\)，\(3<x<5\) 的signed面积为0。

若下一项全过滤证书只改进 \(2<x<3\)，给新的signed窗口upper \(B_{\rm new}\)，
采用其余同一bounds认证严格 \(<6\) 的准确接口是
\[
 \boxed{B_{\rm new}<5/8-I_{\rm in},\quad\text{等价于总节省}>I_{\rm in}+6.}
 \tag{S12}
\]
单从当前已付 \(I_{\rm in}\ge12/5\)，可知该certificate必须有
\(B_{\rm new}<-71/40\)，总节省 \(>42/5\)；
若只用安全 \(I_{\rm in}\le529/40\) 来直接保证成功，则
\(B_{\rm new}<-63/5\) 是一个充分条件。负费用credit合法，
所以节省不被旧面积 \(53/8\) 封顶。
这些条件是所选certificate的预算接口，不能外推为actual费用的必要条件或source no-go。

S9单独给新窗口面积 \(53/8-1/24=79/12\)，以及
\[
 \log d_n\le(1511/60+o(1))n^2
 \quad(Q_n\ne0).
 \tag{S13}
\]
该有限upper继承242全部小素数/primepowers控制及其余宏观窗口；
只减掉S10一次，不重复扣rank或 \(F_n\)。
它没有支付所需严格 \(<6\)，也没有支付原实处 \(-6\) 的完整独立认证。

## 5. 唯一继续门槛

243的余项rank本身只能支付S10；整数greedy在该窗口也不更便宜。
本轮另实际 FULL 核 Root的s=1目标载体稿：原 \(W_p/p\) 的目标系数秩为 \(h-1\)，
故不能继承s=2全余项低秩；在真实高头annihilator子空间上目标系数秩降为
\(2p-5n-1\)（零次数情形为0），但完整常数系数尚未由该结论控制。
这一载体身份不作为S13的额外Gauss节省。
真正可能改变预算的是保留商部、全部harmonic heads与目标列的同一剩余
过滤行列式全系数内容，以及其实际evaluation-annihilator限制。
任何新增输入须接到S8的同一完整normalized费用，不能把低rank当作免费更深determinant内容，
不能用finite prime样本或某个 \(T\) 值代替全coefficient证书。
244正式全局复盘仍固定；本稿不扩目标、权重或列池，不修改242及旧日志/manifest。

实际读取域和当前输入身份见
[本轮记录](../literature/logistic_residual_filter_sources_round243_20261009/packet_reading_scope.md)。
