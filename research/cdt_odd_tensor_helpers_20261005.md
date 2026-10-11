# 平方根积分的真正张量背景：独立秩、完整分母与嵌套预算

日期：2026-10-05。本文新建，旧稿冻结。目标仍是奇数 ζ/L 值的新无理性或线性无关性；本文提供新的实际背景及一张合法预算表，未得到新的数值结论，也未证明该背景族的全部类型不可行。

## 1. 规范与两个独立概念

采用 [已审的辅助函数定义](cdt_odd_algebraic_helpers_20261005.md)：
\[
 L=-\log(1-t),\quad T_j=L^j/j!,\quad
 K_m=\frac1{\sqrt{1-t}}\int_0^t
 \frac{T_{m-1}(u)}{u\sqrt{1-u}}\,du,\qquad m\ge2.
\]
其精确一阶式为
\[
 K_m'=\frac{K_m}{2(1-t)}+\frac{T_{m-1}}{t(1-t)}.       \tag{1}
\]
本稿始终计实际芽在 \(\mathbf Q(t)\) 上的独立性及其导数闭包。单个三阶微分方程的全部 monodromy 解，不等于 \(1,L,K_2\) 这组实际芽；以下证明不混同两者。

## 2. 全部有限偶 \(K_m\) 与 \(L\) 的代数独立性

取二次覆盖 \(z=\sqrt{1-t}\)，原点附近 \(z\to1\)，并定义
\[
 \ell=\log z,\quad
 M=\log\frac{1+z}{1-z},\quad
 B_m=zK_m.
\]
由积分换元直接得到
\[
 B_m'=
 c_m\,\ell^{m-1}M',\qquad
 c_m=-\frac{(-2)^{m-1}}{(m-1)!},\qquad
 M'=\frac2{1-z^2}.                                      \tag{2}
\]
各 \(B_m\) 取从 \(z=1\) 积分的实规范。对 \(m\ge2\)，\(\ell^{m-1}\) 在1为零，故 (2) 在1的简单极点实际可消，原分支的 \(B_m\) 绕1没有 monodromy。

令 \(c=2\pi i\)。绕0的 continuation \(\sigma_0\) 使 \(\ell\mapsto\ell+c\) 而固定 \(M\)；绕1的 \(\sigma_1\) 固定 \(\ell\)，使 \(M\mapsto M-c\)，并固定每个原规范 \(B_m\)。为计算 conjugation，置 \(I_d=\int_1^z\ell^dM'\,dz\)（\(d\ge1\)），以及 \(I_0=M-M(z_*)\)，其中 \(z_*\in(0,1)\) 是共同普通基点。基点常数不影响以下差分。对任意整数 \(h\)，从导数得
\[
 \sigma_0^h I_d
 =\sum_{j=0}^d\binom dj(hc)^{d-j}I_j+\text{常数},\quad
 \sigma_1 I_0=I_0-c,\quad \sigma_1 I_d=I_d\ (d\ge1).
\]
因此 commutator
\[
 \gamma_h=\sigma_0^h\sigma_1\sigma_0^{-h}\sigma_1^{-1}
\]
固定 \(z,\ell,M\)，并有
\[
 \gamma_h I_d=I_d-c(-hc)^d,\qquad
 \boxed{\gamma_h B_m=B_m-c_m c(-hc)^{m-1}.}             \tag{3}
\]
中间 continuation 的附加基点常数在 conjugation 差中消失；(3) 也可直接由 conjugated loop 在1的残数计算。

对于不同偶指标 \(m_i=2k_i\)，平移矩阵是非零列倍数乘
\[
 \bigl(h^{2k_i-1}\bigr)_{h=1,\ldots,s;\ i=1,\ldots,s}.    \tag{4}
\]
它可逆：矩阵为实，若不可逆则有一个非零实核向量。相应非零实奇多项式 \(\sum_i a_i u^{2k_i-1}\) 在 \(s\) 个正数 \(1,\ldots,s\) 上为零；除以 \(u\)、置 \(v=u^2\) 后得到至多 \(s\) 项稀疏多项式的 \(s\) 个正根，违背 Descartes 符号法则至多 \(s-1\) 个正根。连续指标 \(k_i=i\) 时就是 \(\prod h\prod_{i<j}(j^2-i^2)\) 的普通 Vandermonde。

**代数独立定理。** 任意有限不同偶 \(m_i\ge2\) 的
\[
 L,\ K_{m_1},\ldots,K_{m_s}
\]
在 \(\mathbf C(z)\) 上代数独立，因而在 \(\mathbf Q(t)\) 上也代数独立。

证明：若有关于 \(B_{m_i},\ell\) 的多项式关系，重复 (3) 的 \(s\) 个满秩平移，关系在一个满秩整数格的全部点成立。对每一格方向作多项式有限差分，迫使关于所有 \(B_{m_i}\) 的系数分别为零。剩下的非零有理系数 \(\ell\) 多项式又在 \(\ell+hc\) 的全部整数平移下为零，亦不可能。变换 \(K_m=B_m/z\)、\(L=-2\ell\) 不改变此结论。

这给出可用于产品的真正独立性；shuffle 的不同表达式不会增加 rank。只计最终不同单项式。这里的 loops 都在 \(z\) 覆盖上闭合，故对应返回同一 \(t\) 的实际 continuation。

## 3. 真实张量闭包及与奇权模型的交

先取 \(K=K_2\)，定义
\[
 F_{a,b}=K^aT_b/a!,\qquad a,b\ge0.
\]
由 (1)
\[
 F_{a,b}'=\frac a{2(1-t)}F_{a,b}
 +\frac{b+1}{t(1-t)}F_{a-1,b+1}
 +\frac1{1-t}F_{a,b-1},                                \tag{5}
\]
越界项为0。因此
\[
 \mathcal P_s=\langle F_{a,b}:a+b\le s\rangle_{\mathbf Q(t)}
\]
是实际 rank \(\binom{s+2}{2}\) 的微分闭包；rank 来自 §2，不来自形式 tensor 维数。按 \(a\) 过滤后，composition factors 为 trivial 与 sign，一阶齐次因子是 \((1-t)^{-a/2}\)。

更一般，置 \(\mathrm{wt}(L)=1\)、\(\mathrm{wt}(K_m)=m-1\)。全部满足
\[
 b+\sum_i(m_i-1)a_i\le R
\]
的单项式给闭合独立空间。其实际 rank 是
\[
 \sum_{d=0}^R[u^d]\frac1{(1-u)\prod_i(1-u^{m_i-1})}.       \tag{6}
\]
过滤后的全部 factors 仍为 trivial/sign。没有把同一 shuffle 对象重复计数，也未将每个导数免费当作新函数。

当前 [level12 奇权模型](cdt_odd_level12_model_20261005.md) 的 \(\mathcal W\) 实际 rank8，非平凡商为不可约 rank7 Sym6，核为常数。若上述背景空间记 \(\mathcal P\)，则其与 \(\mathcal W\) 的交先映入 Sym6；由于背景的 composition factors 全部 trivial/sign，像只能为零。常数确在交中，故
\[
 \mathcal W\cap\mathcal P=\mathbf Q(t)\cdot1,\qquad
 \dim(\mathcal W+\mathcal P)=7+\dim\mathcal P.             \tag{7}
\]
对已有 rank4、非平凡商 rank3 Sym2 的真实模型，同一理由给 \(3+\dim\mathcal P\)。此结论以实际目标模型已核实为前提，不从“weight”推定 irreducibility。

## 4. \(K_2\) 张量的全部素数安全分母

已审的偶函数定理给 \(L_N^2[t^N]K\in\mathbf Z\)，而 \(L\) 的第 \(n\) 项分母为 \(n\)。设
\[
 \boxed{D_{a,b}(N)=a!\,b!\,
 \prod_{h=1}^aL_{\lfloor N/h\rfloor}^{\,2}
 \prod_{h=a+1}^{a+b}L_{\lfloor N/h\rfloor}.}              \tag{8}
\]
则对全部 \(N\ge0\) 和所有素数，包括2，
\[
 D_{a,b}(N)[t^N]F_{a,b}\in\mathbf Z.
\]
它亦清全部前缀系数。

逐素数证明：在一个 convolution 项中有 \(a\) 个 K 指标及 \(b\) 个 log 指标，总和为 \(N\)，全部正。固定 \(p^v\)，令 \(M=\lfloor N/p^v\rfloor\)。至多 \(M\) 个指标可不小于 \(p^v\)。每个 K 指标最多给两层，每个 log 指标最多一层；总 contribution 至多
\[
 2\min(a,M)+\min\{b,(M-a)_+\}.
\]
这恰是 (8) 中相应 prime-power 层的 multiplicity。对 \(v\) 求和即得结论；求和卷积项不增加分母，\(a!b!\) 只清固定归一化因子。由此安全 scale 和是
\[
 \boxed{\sigma^{\rm safe}_{a,b}=H_a+H_{a+b}.}             \tag{9}
\]
这是明确安全上界，未称所有 gauge 或 integrated 型的最小值。高次张量无需支付粗糙的 \(2a+b\)。

对任意固定有限偶 \(K_{m_i}\) 的产品，设总 K 数为 \(a\)、最大 \(m_i=2k\)、log 数为 \(b\)。旧稿细型与按 K 指标排序给一个普遍安全型
\[
 C\prod_{j=1}^a\left(
 L_{\lfloor N/j\rfloor}^2
 \prod_{h=1}^{k-1}L_{\lfloor N/(2hj)\rfloor}^2\right)
 \prod_{j=1}^bL_{\lfloor N/j\rfloor},                    \tag{10}
\]
其中 \(C\) 是固定 factorial 归一化清因子。其和为 \((2+H_{k-1})H_a+H_b\)。(10) 对各因子用最坏的 \(k\)，仅作合法通用上界；\(K_2\) 的加权 packing (8) 明显更细。

## 5. 比追加纯 log 更有利的一张合法 rank8 预算表

为避免分数列不兼容，选一个明确闭包
\[
 \mathcal V_r=\langle1,T_1,\ldots,T_{r+1},
 K T_0,\ldots,K T_r\rangle,\qquad r\ge0.
\]
由 (5) 及 §2，它实际 rank \(2r+3\)。所有函数在原点正则，直接叶除1外没有有限分支点；作为共同解析背景仍须与目标的全部返回路径核对。

采用以下固定行序：
\[
 1,\ T_1,\ K,\ T_2,\ KT_1,\ T_3,\ KT_2,\ldots,
 T_{r+1},KT_r,\quad H,\theta H,\ldots,\theta^6H.            \tag{11}
\]
全部 \(e_i=0\)。列规则如下，每列确为零前缀、固定常数尾：

* 一个 \(b=1\) 列从 \(T_1\) 开启；
* 第二个 \(b=1\) 列从 \(K\) 开启；
* 对每 \(h=2,\ldots,r+1\)，一个 \(b=1/h\) 列从 \(KT_{h-1}\) 开启；
* 五个新的 \(b=1\) 列在第一个目标行同时开启，保留全部前面 fractional 列。

固定 factorial 与假定有理目标的分母由一个共同常数清除。\(KT_{j-1}\) 的安全型为 \(L_N^2\prod_{h=2}^jL_{\lfloor N/h\rfloor}\)，和 \(1+H_j\)。其之前的 \(T_j\) 已由 \(L_N^2\prod_{h=2}^{j-1}L_{\lfloor N/h\rfloor}\) 清掉：按降序对比，它支配纯 log 型的 \(1,1/2,\ldots,1/j\)。因此该行和为 \(1+H_{j-1}\)，不需另开列。

七个目标行需要七个 \(b=1\) 列；已经有两个，故再开五个。**它们也必须保留 fractional 列**，实际行和为 \(6+H_{r+1}\)，不能误记为7或 \(5+H_{r+1}\)。

令 \(R=r+1\)，实际总 rank \(m=2R+8\)。CDT 全成本为 \(\tau=\tau^\flat\)，因为 \(e_i=0\) 给 \(\tau^\sharp=0\)。精确求和得
\[
 \boxed{\tau^{\rm safe}_{q=7}(R)
 =H_R+\frac{R^2+85R+189}{2(R+4)^2}.}                     \tag{12}
\]
例如预先固定 \(r=24\)：
\[
 m=58,\qquad
 \tau^{\rm safe}=\frac{41751570293347}{7504844146800}
 \approx5.563283.
\]
这是完整合法表，比旧稿已列 rank8+纯 log 的单位列安全值 \(1056/169\approx6.249\) 更低。它不能与旧稿的放宽下界冒充同一量，也未称全体嵌套表最优。

本张表对全部 \(R\ge1\) 仍有 \(\tau^{\rm safe}>51/10\)。一个纯有理证明：式(12)的有理附加项严格递减且大于1/2；在区间 \(1\!:\!3,4\!:\!8,9\!:\!14,15\!:\!24,25\!:\!40,41\!:\!56\) 用左端 \(H\) 与右端附加项，六个下界都严格大于51/10；\(R\ge57\) 用 \(H_{57}>23/5\)。证书核这六个 exact endpoints。因而现指定导数收益小于41/10的 \(Y_0(2)\) 覆盖不能用于这张表；这不是该背景全部其它类型的不可行定理。

一般非平凡目标商 rank 为 \(q\) 时，在第一个目标行再开 \(q-2\) 个 unit 列（此句限 \(q\ge2\)），得到
\[
 \tau^{\rm safe}_{q}(R)=H_R+
 \frac{2R(R+1)+(q-1)q(4R+q+2)}{(2R+q+1)^2}.              \tag{13}
\]
对 rank4 目标 \(q=3\)，式(13)严格随 \(R\ge1\) 增大；差的共同正分子是 \(2R^4+11R^3+34R^2+70R+53\)。最小 \(R=1\) 为 \(47/18\)，就是只加 \(L,K\) 的背景。因此当前自然张量链未改善该目标的最小表。

## 6. 旧偶 \(K\) 证明独立审核及剩余缺口

独立复核旧稿的全 prime-prefix 证明，未发现反例：binomial carry 逐层覆盖2；不同 harmonic indices 的顺序统计给每层 \(L_{\lfloor n/h\rfloor}\)；Pochhammer block 在固定低次数上的 Wilson 同余确支持 shifted packet。旧稿 gauge 延伸需要的全前缀消失，依 \(N=Hp+s\)、\(H<j\) 与 source degree \(d>H\) 的逐块界确已写出，不能只用正 offsets 递推。本稿不修改或重运行旧 producer。

新贡献是产品的真实代数独立性、加权闭包 rank、全素数 packing 型，以及一张低于先前已列纯 log 安全值的完整 nested 表。下一步若使用多 \(K_{\rm even}\) 乘积，须从 (6)/(10) 建新合法表，或寻找能降低 denominator types 的真实积分/gauge；单用 (9) 的 row sums 排序不能自动得合法嵌套列。解析端仍需同一合法映射的全部叶和 capacity 商严格小于实际 rank。

配套 [脚本](cdt_odd_tensor_helpers_20261005_verify.py) 与 [证书](cdt_odd_tensor_helpers_20261005_verify.json) 仅核固定 algebraic identities、rank计数、前缀安全型和预算；不以有限实例证明全尺度，不计算 ζ/L 小数，不搜索 n/p 参数。主要方法来源为库内 [CDT 原文](../literature/cdt2024_l2_chi_minus3.pdf) Remark10.1.8 及 Definition6.0.1；新的 monodromy/packing 推导完整写于本文，不声称已证明新数值无理性。

