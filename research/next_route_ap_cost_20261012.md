# AP 过滤费用的有界审查：自然平衡费用为 32/27，仍不能开启当前数值出口

2026-10-12。固定第259–261轮的普通 Taylor 坐标 `s`、真实 bare rank3 模块和同一全纯图接口。本稿只作纸面分析，不进行参数、素数、地图、CAS 或 Padé 扫描；没有新数值无理性/线性无关定理，也没有声称已证明一个适用于 AP 分母的新 holonomy 定理。

**结论有四层，不能合并：**

1. 对 `b=0,c=±d` 的特殊关系，两非恒定行的实际最小前缀分母率是 `γ=4/3`。下文把原来的 row 障碍加强到每个素数类的首次存活指数，得到任意固定有理换基非有理行的真实前缀率下界 `liminf ≥4/3`。
2. 对 CDT Theorem8.0.1定义式(8.0.2)的自然 AP 扩展——仍取 balanced species、近均匀 degree，并用逐行标量前缀分母的 worst-case product/LCM——最优基底费用**恰为 `32/27`**。这是这个明确定义的算术 cap 的精确计算，不是已经适用的 CDT 定理中的新 `τ`。
3. 本轮进一步核到同源全部合法图的强界 `λ<log3<10/9`。所以自然 AP 费用 `32/27` 连正分母都不能满足，差距超过 `2/27`。
4. 若利用 CDT Remark6.6.15 所指出的辅助 index `k` 分布，对正确的 coefficient index `n−k` 重作标量前缀 cap，该 cap 仍有下界 `8/9`。它不再直接阻断正分母，但当前 rank3 的 Bost–Charles 接口必需 `λ>3τ/2≥4/3`，仍与强界冲突。这个 `8/9` 只作下界，不认领精确新费用或实际 coefficient 分母下界。

## 1. 对象、目标和已付输入

固定

$$
H=A(a+bB_3+cC_3+dB_4),\qquad
V=\langle1,H,\theta_sH\rangle_{\mathbb Q(s)},\qquad \dim V=3.
$$

取固定整数 `C₀` 清掉有理关系系数，令

$$
J=C_0H=A(A_c+B B_3+C C_3+D B_4),\qquad D\ne0,
$$

其中 `θ_s=s∂_s`，`A(s)=1+3s+…∈Z[[s]]`，`q(s),s(q)` 双向整数且线性项为1。四个素数类为

$$
\mathcal R=\{1,5,7,11\}\pmod {12},\qquad
\epsilon_3(r)=\chi_{-3}(r),\quad\epsilon_4(r)=\chi_{-4}(r).
$$

令 `T_r(k)` 为第261轮真实最高 `p⁻²` packet 的第 `k` 个系数，其首次非零下标为

$$
k_r=\begin{cases}
1,&B\epsilon_3(r)+C+D\epsilon_4(r)\ne0,\\
2,&B\epsilon_3(r)+C+D\epsilon_4(r)=0,\ B\ne0,\\
3,&B\epsilon_3(r)+C+D\epsilon_4(r)=0,\ B=0.
\end{cases}
\tag{1}
$$

对于 `B=0,C=±D`，恰有两个类 `k_r=1`、两个类 `k_r=3`。这是指定目标 `ζ(2)±2G` 的完整反证系数类：真实端点周期为

$$
a+bL(2,\chi_{-3})/2+c\zeta(2)/4+dG/2.
$$

本稿不判断这两个目标的全球已知状态；新颖性需另外审查。算术结论仅说明这两个反证类具有同一个较低前缀率，不推出任何数值结果。

已付真实前缀上界为

$$
M_N=\prod_{p\le\max(3,\sqrt N)}p^{2\lfloor\log_pN\rfloor}
\prod_{r\in\mathcal R}\prod_{\substack{p>\max(3,\sqrt N)\\p\equiv r\ (12),\ k_rp\le N}}p^2,
\quad N\ge1,\qquad M_0=1.
\tag{2}
$$

它清除 `J,θ_sJ` 的完整前缀，保留小素数全部幂。固定模数 PNT_AP 及第261轮双边证书给

$$
\log L_J(N)=\gamma N+o(N),\qquad
\log L_{\theta_sJ}(N)=\gamma N+o(N),\qquad
\gamma=\frac12\sum_{r\in\mathcal R}\frac1{k_r}.
\tag{3}
$$

对当前特殊类 `γ=4/3`。`L_f(N)` 指清除 `f` 的系数 `0,…,N` 的最小正整数，不能直接认作 holonomy 费用。

来源：[261算术稿](refined_budget_arithmetic_round261_20261010.md) R2–R5；[261联合停止证书](refined_budget_gate_round261_20261010.md)。

## 2. 新的逐类 row 障碍：换基不能降低标量前缀率

取任意固定有理 Laurent 行

$$
g=u(s)J+v(s)\theta_sJ+w(s),\qquad
u,v,w\in\mathbb Q(s),\quad(u,v)\ne(0,0),
\tag{4}
$$

只讨论 `g` 本身在原点为普通 Taylor 芽的情况。设三个系数的最大 Laurent 负阶为 `L`。除一个固定有限坏素数集，它们的全部 Laurent 系数均 `p` 整。

对每个 `r`，第261轮 divisor-sum 身份给，在次数小于 `(k_r+1)p` 的范围内，

$$
p^2J\equiv T_r(k_r)s^{k_rp}A(s)\pmod p,
\qquad
p^2\theta_sJ\equiv T_r(k_r)s^{k_rp}\theta_sA(s)\pmod p.
\tag{5}
$$

这里 `p` 足够大且 `p≡r mod12`。理由是：该范围只会出现一次 `p`，低于 `k_rp` 的最高平方分母 packet 完全为零；`q(s)^p≡q(s^p)`，所以 `q(s)^{k_rp}` 的首项为 `s^{k_rp}`，下一项至少到 `(k_r+1)p`；其 `θ_s` 导数模 `p` 为零。乘 Laurent 系数只把有效范围缩短固定的 `L`。

令

$$
W=uA+v\theta_sA.
$$

已付的 period rank2 不可约性保证 `W∉Q(s)`：`W=0` 违背两行独立，非零有理 `W` 的导数闭包则给出有理 rank1 子模块。因此其 Laurent 展开有某个固定正下标 `κ≥1`、非零有理系数 `W_κ`；若所有正次项均为零，它会是有理 Laurent 多项式。

排除 `T_r(k_r)W_κ` 的有限分子/分母素数，并取 `p>κ+L`，从(5)得到对**每个类的所有充分大素数**

$$
\boxed{v_p(g_{k_rp+\kappa})=-2,\qquad
p\nmid(k_rp+\kappa).}
\tag{6}
$$

这比只用存活 `k_r=1` 类的旧 row 论证更精细。没有通过素数样本外推；`κ` 依赖固定 row，但不依赖 `p` 或其类。

于是

$$
\log L_g(N)\ge
2\sum_{r\in\mathcal R}\vartheta((N-\kappa)/k_r;12,r)-O(\log N),
$$

故

$$
\boxed{\liminf_{N\to\infty}\frac{\log L_g(N)}N\ge\gamma.}
\tag{7}
$$

固定坏素数可能因有理 prefactor 的 Taylor 展开产生额外线性成本，所以任意换基只可领取下界(7)，不能声称其前缀率仍恰为 `γ`。原行 `J,θ_sJ` 则由(3)达到等号。

同样，如果提出带 `n^e`、固定 index shifts 的有限 classwise filtered-LCM row type，(6)中的 `n=k_rp+κ` 使 `n^e` 为 `p` 单位。对每个类 `r`，至少两个 factor slopes 必须满足 `b_h^(r)≥1/k_r`；固定 shifts 不改变这个必要条件。这只是所提出 row type 的必要条件，并非评价行列式全部内容的下界。

## 3. 定义式(8.0.2)的自然 AP cap：精确计算 32/27

CDT Theorem8.0.1的定义式(8.0.2)用 balanced labels `i` 和近均匀 degrees `n`，对每个 threshold 分别取最大贡献。其 normalized factor2 来源于总消失阶标尺 `α≈dN/2`，不能删掉。本段保留这个结构，只把标准 LCM 的素数集合改成(2)的真实 AP 前缀集合。

更明确地，对于固定基底 `𝔅=(g₁,g₂,g₃)`，定义标量前缀 cap

$$
R_{N,d}(\mathcal B;\eta,\varepsilon)
=\operatorname{lcm}_{\substack{\mathbf n\in P^d_\varepsilon(N)\\
\mathbf i\in V^d_3(\eta)}}
\left\{\prod_{j=1}^d L_{g_{i_j}}(n_j)\right\},
$$

$$
\tau_{\rm prefix}(\mathcal B)
=\limsup_{\eta,\varepsilon\downarrow0}\limsup_{d\to\infty}
\limsup_{N\to\infty}\frac{2}{dN}\log R_{N,d}(\mathcal B;\eta,\varepsilon).
\tag{8}
$$

`V` 与 `P` 是原定义式的同一 balanced species 与 normalized discrepancy 条件。这个 cap 可清除所有 coefficient-product 的分母，因为各实际系数下标不超过相应 `n_j`；它忽略辅助多项式的 degree shifts 及 actual coefficient supports。

对原基底 `𝔅₀=(1,J,θ_sJ)`，有 `2/3` 的 labels 非恒定。大素数 `p≡r mod12`，在 `t=p/N` 处，逐 prime 最大平方分母计数为

$$
2d\min\{2/3,(1-k_rt)_+\}+o(d).
\tag{9}
$$

上界来自：非恒定 species 数量最多 `2d/3`，近均匀 degree 中大于 `k_rp` 的数量最多 `(1-k_rt)_+d`。两种界同时可达：把两个非恒定 species 放到最大的 `2/3` degrees。所有类的最佳安排相同，不需要不同素数采用不相容 species 排列。

小素数全部幂的 contribution 是 `O(d√N logN)`，在原顺序先取 `N→∞`（固定 `d`）后不影响 normalized rate。每个 prime class 的 PNT 密度为 `1/4`，所以

$$
\begin{aligned}
\tau_{\rm prefix}(\mathcal B_0)
&=4\sum_{r\in\mathcal R}\frac14
\int_0^{1/k_r}\min\{2/3,1-k_rt\}\,dt\\
&=4\sum_r\frac14\frac4{9k_r}
=\frac49\sum_r\frac1{k_r}
=\frac89\gamma.
\end{aligned}
\tag{10}
$$

相同结果也可由排序直接看出：非恒定 degree 占区间 `[1/3,1]`，所以 normalized prefix product cost 为

$$
2\gamma\int_{1/3}^{1}x\,dx=\frac89\gamma.
$$

对任意固定 `Q(s)` 基底，至多一行属于 `Q(s)`，至少两行受(7)约束。取完全 balanced labels 并把这两行放在最大的 `2/3` degrees，仅这一 admissible product 就给

$$
\tau_{\rm prefix}(\mathcal B)\ge\frac89\gamma.
\tag{11}
$$

因此原基底达到这个标量 prefix-cap 模型的基底最小值；对当前特殊类

$$
\boxed{\inf_{\mathcal B}\tau_{\rm prefix}(\mathcal B)
=\tau_{\rm prefix}(1,J,\theta_sJ)=\frac{32}{27}.}
\tag{12}
$$

这是由具体 primewise profile、balanced maximization 和原归一化推得的等式；不能仅把原 `16/9` 乘一个未经证明的“节省比例”。四类关系在同一 cap 模型的值如下：

| 关系类型 | `γ` | 自然 `τ_prefix=(8/9)γ` |
|---|---:|---:|
| 四类均在 degree1 存活 | `2` | `16/9` |
| 一类延迟到 degree2 | `7/4` | `14/9` |
| 两类延迟到 degree2 | `3/2` | `4/3` |
| `B=0,C=±D`，两类延迟到 degree3 | `4/3` | `32/27` |

## 4. 为什么(12)不是所有实际有限处费用的下界

Theorem8.0.1的原文只涵盖有限 literal LCM arrays。`τ_prefix` 是本稿明确另定义的 cap；不能将(12)直接代入已发表 Theorem8.0.1。这里(8.0.2)是该定理中的定义公式，并非另一个名为Definition8.0.2的陈述。

CDT §6.6 的模板分母计算允许所有符合类型的 formal functions，并用各变量前缀 cap 作 worst-case product。其 Remark 6.6.15 明确指出：该处理忽略辅助指数 `k` 的均匀分布，可重新考虑更精细的 limiting formula，也可考虑受限素数区间等 denominator shapes。

本稿没有排除这些更细对象：

- 实际 row coefficients 的 `p⁻²` support 与前缀 support 不同；(6)只保证某些指定 coefficient witnesses，并不证明区间中每个系数都带平方分母。
- 实际领先项的 coefficient degree 是 `n_j-k_j`，其中辅助 `k_j` 也受分布限制；(8)用 `L(n_j)` 包住它，未利用该限制。
- 实际联合评价行列式可能有 scalar prefix product 看不到的完整 p-adic 内容或多行相消。若更改 source lattice，还须把 index、box principle、balanced tensor 与同一 archimedean metric 一起结算。

所以(11)是**所有固定基底的标量前缀 cap 下界**，不是 arbitrary filtered evaluation lattice、实际 primitive determinant 或全部 arithmetic holonomy 方法的下界。继续 AP 路线所需的新定理若只重做(8)的清整和原高度论证，将至多得到(12)这一自然费用，不能期待固定换基再压低它。

## 5. 新的两省略值全图界：自然 AP 模型连正分母都失败

第261轮已证所有合法全纯图必须省略 `s_a=(1−√3)/2`、`s_b=(1+√3)/2`。令

$$
x=\frac{\sqrt3-1}{2\sqrt3},\qquad x(1-x)=\frac16,
\qquad f=\frac{\phi-s_a}{\sqrt3}.
$$

则 `f:D→C\{0,1}`、`f(0)=x`、`|φ′(0)|=√3|f′(0)|`。用**参数**定义

$$
K(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}}.
$$

既有 modularλ 通用覆盖的逆值 `τ(x)=iK(1−x)/K(x)` 满足

$$
\tau'(x)=-\frac{i\pi}{4x(1-x)K(x)^2}.
$$

本分支独立核其规范：两个 hypergeometric 解的 Wronskian 为 `−π/[4x(1−x)]`，单位盘到上半平面在 `τ(x)` 的最大导数为 `2Imτ(x)`；所以没有丢失 curvature−1 的 factor2，通用覆盖导数恰为

$$
R(x)=\frac{8x(1-x)}\pi K(x)K(1-x),\qquad
|\phi'(0)|\le\frac{4\sqrt3}{3\pi}K(x)K(1-x).
\tag{13}
$$

Cauchy–Schwarz 与 `y=tanθ` 的积分给自含估计

$$
K(m)^2\le\frac\pi2\int_0^{\pi/2}\frac{d\theta}{1-m\sin^2\theta}
=\frac{\pi^2}{4\sqrt{1-m}}.
$$

代回(13)，

$$
|\phi'(0)|\le\frac{\pi6^{1/4}}{\sqrt3}
<\frac{(22/7)(8/5)}{12/7}=\frac{44}{15}<3.
$$

此处 `6^(1/4)<8/5`、`√3>12/7` 皆是整次幂有理比较；`π<22/7` 为经典严格界。再由

$$
\sum_{h=0}^4\frac{(10/9)^h}{h!}
=\frac{59453}{19683}>3
$$

（与3的差为 `404/19683`），得到

$$
\boxed{\lambda=\log|\phi'(0)|<\log3<10/9.}
\tag{14}
$$

对自然费用(12)，

$$
\boxed{\lambda-32/27<-2/27<0.}
\tag{15}
$$

因此这个 matched AP cap 即使有新 theorem 也无法在当前图类满足正分母；无需靠 numerator 修正作下一轮图优化。完整 cover 源审查与总决定见[本轮全图证书](next_route_cover_bound_20261012.md)。本分支实际核的是逆覆盖导数规范、椭圆积分估计与全部有理常数；未重新证明 modularλ 的整个通用覆盖理论。

## 6. 所选 Bost–Charles 必要门槛与新收益要求

对未精化式及该轮审过的两种合法凸性修正，实际 numerator `J_BC−C` 均不小于 `λ`。因此若要产生严格 rank3 矛盾

$$
\frac{J_{BC}-C}{\lambda-\tau}<3,
$$

除正分母外，还必须

$$
\lambda<3(\lambda-\tau),\qquad
\boxed{\lambda>\frac32\tau.}
\tag{16}
$$

若一个匹配的新 AP theorem 只交付自然值 `τ=32/27`，(16)要求 `λ>16/9`，比已经失败的正分母关更强。旧 `log(11/2)` 上界只阻断这道 rank3 关；新的(14)在它之前阻断正分母。不能在更新解析界后继续声称自然 AP cap 已经解除正分母障碍。

若维持同一图与 numerator 接口，新有效费用至少应满足

$$
\boxed{\tau_{\rm eff}<\frac23\log3<\frac{20}{27}.}
\tag{17}
$$

相对(12)的额外真实 finite credit `δ` 必须

$$
\boxed{\delta>\frac{32}{27}-\frac23\log3>\frac49.}
\tag{18}
$$

`4/9` 是由 `log3<10/9` 得到的较弱必要节省，不是充分成功标准；精确必要门槛为(18)左侧。还须有 matched source/height theorem 以及同一合法图的实际严格能量，不能从(17)或正分母自动得到成功。

## 7. 核查 Remark6.6.15 的辅助 index 机制：更细 cap 的下界为 8/9

原文 Lemma6.2.6 的(6.2.8)、(6.2.9)及 Corollary6.2.11 确认：辅助 monomial vector `k/D` 近均匀分布在 `[0,1]`，leading coefficient vector `n/((m+δ)D)` 近均匀分布在 `[0,1]`。对 `m=3`，以 `N≈3D` 归一化，`k/N` 的极限分布是 `[0,1/3]` 上均匀分布，`n/N` 是 `[0,1]` 上均匀分布。

单个 summand 的真实系数身份为

$$
[x^{\mathbf n}]\left(x^{\mathbf k}\prod_j f_{i_j}(x_j)\right)
=\prod_j f_{i_j,n_j-k_j}.
\tag{19}
$$

所以任一非零 term 必须所有 `n_j≥k_j`。如果 `f₁=1`，标签1更要求 `n_j=k_j`，不能只用 positive part 把负下标当成免费 constant coefficient。

一种未经这个检查的安排会把两个非恒定标签置于最大 `2/3` 的 `n`，并取最小 `2/3` 的 `k`；它给 active residual `10/27`，进而得到 `80/81`。但是剩余 constant coordinates 的总 residual 为 `−1/27`，含负下标且不满足 `n=k`，该 term 为零。**本稿不采用这个 `80/81` witness。**

有一个满足真实必要索引约束的排列。取 `d=3h`、`N=3D`（取整和 `δ→0` 只影响误差）：

- `h` 个 constant coordinates 取 `n_j=k_j=jD/h`，`j=1,…,h`。
- 其余 `2h` 个非恒定 coordinates 的 `n` 取 `(h+1)D/h,…,3hD/h`；`k` 取 `D/h,…,D` 各两份；两种非恒定 labels 各占 `h`。

于是整份 `n` 在 `[0,N]` 近均匀；整份 `k` 在 `[0,D]` 近均匀；labels 完全 balanced；所有非恒定 `n≥D≥k`。constant 行实际满足 `n=k`。active residual 的和精确为 `dD=dN/3`，归一化积分亦为

$$
\int_{1/3}^{1}n\,dn-2\int_0^{1/3}k\,dk
=\frac49-\frac19=\frac13.
$$

因此对仍使用标量 prefix `L_i(n_j−k_j)`、但加入上述辅助 `k` 约束的任何 complete worst-case product/LCM cap，仅这一份 admissible prefix product 已给

$$
\boxed{\tau_{\rm prefix,aux}\ge2\gamma/3=8/9.}
\tag{20}
$$

这里 `n_j−k_j` 是合法非负 coefficient index；(3)给每条原非恒定行的 prefix asymptotic。若换固定基底，(7)仍支持同一下界，把剩余第三行放在固定首个非零 coefficient index（一个固定 shift）即可，leading 不变。若所有三行均非有理，新增费用非负，不能降这个下界。

**(20)只是下界，不是精确费用。** cap 中每个素数的 maximizing joint arrangement 可以不同，primewise LCM 的 leading 可能更大；同样，此 witness 并未证明具体的非恒定 actual coefficients 在每个所选下标均非零或具有 prefix 的完整分母。若利用 actual support、共同内容或首项条件，其模型会超出本段 scalar-prefix cap，必须另证。

对所选 rank3 BC 接口，(20)使(16)必要 `λ>4/3`，而(14)给 `λ<10/9`。因此**仅把辅助 `k` 的均匀分布纳入这个 prefix cap，仍不能救当前入口**；不是连正分母都失败的主张，因为 `8/9<10/9`。相对这个下界，若还要沿该 numerator 接口成功，必须有超出标量 cap 的实际额外 credit 至少

$$
\boxed{8/9-(2/3)\log3>4/27.}
\tag{21}
$$

## 8. 本轮决定与真正值得补的第一证书

**不把“证明自然 AP 版 Theorem 8”或“只利用辅助 `k` 分布的 prefix cap”选为当前实现主线。** 它们可成为一般工具，但所需新数值出口分别已被(15)与(20)–(21)挡住。也不重开固定基底、`n^e`、标准 LCM 参数或地图扫描。

AP 路线若再准入，第一证书应明确超出这些 scalar-prefix caps：对同一 complete evaluation 对象，利用 actual coefficient support、首项的额外约束或完整联合内容，给出达到(17)的全尺度 finite credit；同时说明其 source index 与 analytic metric 为什么不会把 credit 抵消。只有猜测“存在更多 gcd”或列出有限素数例子不能作为这项证书。辅助 `k` 分布本身已经由本轮首证书检验，不能作为未经预算的新机制重开。

另一种合法转向是改变数值载体或已陈述的 analytic/numerator 接口，但必须重付真实目标投影、完整关系消芽、独立秩和全部费用；本稿不将其视作当前 AP 算术的自动延伸。

## 9. 阅读范围与证据边界

本稿实际全文读：`refined_budget_arithmetic_round261_20261010.md`、`refined_budget_gate_round261_20261010.md`、`refined_budget_characteristic_round261_20261010.md`；全文读固定 CDT v2 的已保存物理66–67与119–124页节选；另从固定 v2 locator 阅读 §§6.2.1–6.2.15 的完整定义/lemma/corollary与 §6.6 起至 Remark6.6.15 的完整段落，核原 `α=mdD/2`、真实 `n−k` coefficient identity、两个分布尺度、模板 product、worst-case LCM 与被忽略的 `k` 分布。复读234 all-map稿G4及239 budget稿B8–B9的椭圆覆盖归一化与Cauchy–Schwarz证明，独立核本轮参数替换和有理常数。整体218页原件未全文审查；未读取/审计全部先前来源或全部证明。

定页来源见[261原文摘录](../literature/refined_budget_round261_20261010/arithmetic_cdt_v2_physical119_124.txt)、[66–67页](../literature/refined_budget_round261_20261010/arithmetic_cdt_v2_physical066_067.txt)、[固定v2 locator](../literature/trace_sources_round221_20261008/cdt_fixed_v2_locator.txt)；原文为[arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2)。没有新网络检索、数学程序、有限n证书、CAS、prime/map/参数扫描、Lean或Git写入。新资产是(6)逐类 row witness、(7)基底前缀下界、(8)–(12)指定 cap 的精确费用、(14)–(18)强同图比较及(20)合法辅助-index cap 下界，不是新数值定理。
