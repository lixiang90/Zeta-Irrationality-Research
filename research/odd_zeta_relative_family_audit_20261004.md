# 相对端点的整数 Mellin 族：纯目标、矩消元、非零性与清分母成本

日期：2026-10-04。本稿继续真实端点接口，冻结旧文件。本轮不给 ζ(7) 或 Catalan 无理性结论，也不把有限核验当渐近定理。主要完成一个带普通矩消元的整数 Rodrigues 族：纯目标身份、实际非零性及绝对衰减指数均可完整证明；另独立核根分支的高阶 log-moment 候选，明确其仍未证明的部分。

## 1. 单一 Mellin 核的精确污染表

对 `k≥2`、`P∈Z[t]`，定义实际收敛积分

\[
J_k(P)=\int_0^1\frac{(-\log t)^{k-1}}{(k-1)!}
                  \frac{P(t)}{1+t^2}\,dt.
\]

整数长除法唯一给

\[
P=(1+t^2)Q+A+Bt,\quad Q\in\mathbb Z[t],\quad A,B\in\mathbb Z,
\qquad P(i)=A+iB.
\]

写 `Q=Σq_rt^r`，由单项式矩和几何展开准确得到

\[
\boxed{J_k(P)=\sum_r\frac{q_r}{(r+1)^k}
 +A\beta(k)
 +B\frac{2^{k-1}-1}{2^{2k-1}}\zeta(k).} \tag{1}
\]

因此一般 `k=7` 会同时出现 `β(7)` 和 `ζ(7)`；一般 `k=2` 会同时出现 `G` 和 `ζ(2)`。单靠 integral 为正不能消除这些常数。`P(i)` 的真实整数余类决定污染。

两种保留实区间形状的整数滤波是

\[
P_G(t)=R(t^2),\qquad P_{\zeta,k}(t)=tR(t^2),\qquad R\in\mathbb Z[u].
\]

前者 `P_G(i)=R(−1)` 为实数，故 `J₂(P_G)∈Q+QG`；后者 `Pζ(i)=iR(−1)` 为纯虚数，故 `J_k(Pζ)∈Q+Qζ(k)`。对 ζ(7) 取后者不会带入 `β(7)`。

令

\[
I_k(R)=\int_0^1\frac{(-\log u)^{k-1}}{(k-1)!}\frac{R(u)}{1+u}\,du,
\qquad \eta(k)=(1-2^{1-k})\zeta(k).
\]

变元 `u=t²` 给

\[
J_k(tR(t^2))=2^{-k}I_k(R), \tag{2}
\]

\[
R=(1+u)S+B,\quad B=R(-1),\qquad
I_k(R)=\sum_j\frac{s_j}{(j+1)^k}+B\eta(k). \tag{3}
\]

特别地，`J₇` 的 ζ(7) 系数是 `63B/8192`。一次 parity 化并未把 degree 的清分母成本机械翻倍：对于 `degR=N`，(3) 的单项式分母只到 `N`；(2) 引入的 `2⁻ᵏ` 是固定因子。

直接取 `(P(t)−P(−t))/2` 并不等价于这个正形状滤波。例如二项式 `(1−t)^m` 的镜像是 `(1+t)^m`，可以毁掉原实衰减。应在定义族时就使用 `R(t²)`，或者严格核镜像积分后的实际指数。

## 2. 有理方向确实存在，但其统一成本随权重增长

`∫₀¹u^j(-logu)^(k−1)/(k−1)! du=(j+1)⁻ᵏ` 是 (3) 中 `1` 方向的确切来源。连续分部积分解掉 monomial 的 `k` 层原函数，每层都要再除一次 `j+1`。这是真实边界计算；不需要假定 ζ(k) 无理。

对所有 `S∈Z[u]`、`degS≤N−1` 的 rational moment 部分，最小统一整数倍率准确为

\[
L_N^k,\qquad L_N=\operatorname{lcm}(1,\ldots,N). \tag{4}
\]

证明：该倍率显然够用；反过来逐个取 `S=u^(m−1)`，就要求倍率被 `m^k` 整除，所有 `m≤N` 的最小公倍数是 `L_N^k`。这是“对整个整数 polynomial 空间”的量词，不能改成“每个指定候选的实际最小分母都如此”。

由 (3)，固定安全倍率 `2^(k−1)L_N^k` 把 `I_k(R)` 化成整数 `p+qζ(k)`；由 (2)，`2^(2k−1)L_N^k` 可用于 `J_k(tR(t²))`。若 `R≥0` 且非零，原积分为正，给真实非零性；但安全倍率或 finite division 身份不自动给足够小的整数线性型。

在 period 语言中，`(-logu)^(k−1)/(k−1)!` 可写为 `k−1` 层 `du/u` 的真实迭代积分。因此 (1)–(3) 是长度随 `k` 增长的实际积分身份。然而仅写这个积分，并未交付高权 motivic complex 中的完整 cycle 或一个规范相对 lift。特别不能把权二 Bloch 链的 `[i]` 证明直接升格成 ζ(7) 的高权 chain 证明。对于本 Mellin 接口，可直接控制的算术对象是 (3) 的 rational boundary 和 target remainder，后者由 `B` 保证；其统一 boundary 成本是 (4)，与固定 K₃/Bloch 类非零是两回事。

二项式 `R=u^(an)(1−u)^(bn)` 的实际分母窗口及完整 coefficient gcd 已由 [cyclotomic Mellin 报告](E:/kimi-build/zeta5/research/odd_zeta_cyclotomic_mellin_20261004.md) 独立推进。本稿不重复其 prime-window 主证明，也不将下文的标准倍率预算升级为实际本原预算定理。

## 3. 更有结构的整数 Rodrigues 族：全部普通矩消元与实际非零性

对固定整数 `A≥1`、`n≥1`，定义

\[
\boxed{R_{n,A}(u)=\frac1{n!}\frac{d^n}{du^n}
                  \left[u^{(A+1)n}(1-u)^n\right].} \tag{5}
\]

这是经典 Rodrigues/Jacobi 结构在本相对接口中的一个可完全认证的族；不称它为文献中从未出现的新多项式。展开为

\[
R_{n,A}(u)=\sum_{\ell=0}^n(-1)^\ell
 \binom n\ell\binom{(A+1)n+\ell}n u^{An+\ell}. \tag{6}
\]

由此所有系数为整数、degree 为 `N=(A+1)n`，而

\[
R_{n,A}(-1)=(-1)^{An}\sum_{\ell=0}^n
 \binom n\ell\binom{(A+1)n+\ell}n\ne0. \tag{7}
\]

分部积分给 `n` 个精确普通矩消元

\[
\int_0^1 u^jR_{n,A}(u)\,du=0,\qquad 0\le j<n. \tag{8}
\]

因此它是带符号的整数滤波，不能以 `R≥0` 判断积分。然而真实 target 积分仍可证明非零。

**非零命题。** 固定 `k≥2` 时，对所有 `n,A` 如上，

\[
I_k(R_{n,A})>0,\qquad J_2(R_{n,A}(t^2))>0. \tag{9}
\]

证明：`W_k(u)=(-logu)^(k−1)/[(k−1)!(1+u)]` 在 `0<u<1` 上完全单调，即 `(-1)^rW_k^(r)>0`。这是 `−logu`、`1/(1+u)` 的导数符号，以及正函数乘积的 Leibniz 公式的直接结果。将 (5) 分部积分 `n` 次，得

\[
I_k(R_{n,A})=\int_0^1u^{(A+1)n}(1-u)^n
              \frac{(-1)^nW_k^{(n)}(u)}{n!}\,du>0. \tag{10}
\]

`u=0` 处任一边界项至少含 `u^(An+1)` 乘有限次 log，趋零；`u=1` 处至少含一阶 `(1−u)`，故分部积分合法。对于 G，由变元 `u=t²`，权为 `u^(−1/2)(−logu)/(4(1+u))`，同样完全单调，边界项在 `0` 至少含 `u^(An+1/2)`。所以同样得到严格正性。证毕。

结合 (2)、(3)、(7)，这个族同时交付纯 `1+ζ(7)`、纯 `1+G` 形式及其实际非零性，没有借用两个目标的无理性。

## 4. 普通矩消元并没有改善绝对指数预算：一个可证的全族定理

设 `A≥1` 和 `k≥2` 固定。记

\[
\rho_A=(A+1)\log(A+1)-A\log A.
\]

则这个整族准确满足

\[
\boxed{\lim_{n\to\infty}\frac1n\log I_k(R_{n,A})=-\rho_A.} \tag{11}
\]

它与原二项式 `u^(An)(1−u)^n` 的指数相同。证明必须核高阶导数的成本；不能仅看到 (10) 分子多了 `u^n` 就声称衰减更快。

写 `m=k−1`、`L=−logu`、`g=L^m/m!`。利用生成式 `u^(−α)=exp(αL)` 得精确导数身份

\[
\frac{(-1)^r g^{(r)}(u)}{r!}
=u^{-r}\sum_{j=1}^{\min(r,m)}
 \frac{c(r,j)}{r!}\frac{L^{m-j}}{(m-j)!},\qquad r\ge1, \tag{12}
\]

其中 `c(r,j)` 是无符号第一类 Stirling 数。所有项非负，而且 `c(r,1)=(r−1)!`。因此

\[
\frac{(-1)^nW_k^{(n)}}{n!}
\ge \frac{u^{-n}}{n(1+u)}\frac{L^{m-1}}{(m-1)!}. \tag{13}
\]

它恰好抵消 (10) 分子新增的 `u^n`。

对上界，用

\[
\frac{c(r,j)}{r!}
\le\frac{H_{r-1}^{j-1}}{r(j-1)!},\qquad
H_r=\sum_{j=1}^rj^{-1}.
\]

这是 elementary symmetric sum `e_(j−1)(1,1/2,...,1/(r−1))` 的直接估计。令 `v=u/(1+u)≤1/2`，Leibniz 公式及几何和给

\[
\frac{(-1)^nW_k^{(n)}}{n!}
\le \frac{u^{-n}}{n(1+u)}
 \left[\frac{L^m}{m!}
 +12\frac{(L+H_n)^{m-1}}{(m-1)!}\right]. \tag{14}
\]

例如用 `Σ_(r=1)^n v^(n−r)/r≤12/n`、`v^n≤1/n` 即得此固定常数；分成 `r≥n/2` 的几何尾和其余指数小项即可证明前一不等式。

由 (13) 下界，在 `u*=A/(A+1)` 周围任何小区间的 Laplace 下界给 `liminf≥−ρ_A`。由 (14)，对任意固定小 `ε>0`，有限 log 次数可被 `Cεu^(−ε)(1+H_n)^m` 控制；上界于是为 polynomial-log 因子乘

\[
\int_0^1u^{An-\varepsilon}(1-u)^n du
=B(An-\varepsilon+1,n+1).
\]

Stirling 公式给此 beta integral 的指数准确为 `−ρ_A`，得 (11)。这些上、下界全在 `n→∞` 的固定 `A,k` 量词下成立。

G 权中的 `u^(−1/2)L` 也可用同一论证：其第 `n` 阶带符号导数除 `n!` 是

\[
u^{-n-1/2}\frac{(1/2)_n}{n!}
 \left[L+\sum_{j=0}^{n-1}\frac1{j+1/2}\right],
\]

令 `a_r=(1/2)_r/r!`、`H_r^*=Σ_(j=0)^(r−1)(j+1/2)⁻¹`，其中 `H_0^*=0`。乘上 `1/(1+u)` 后，导数卷积准确为

\[
\frac{(-1)^n}{n!}\frac{d^n}{du^n}
 \frac{u^{-1/2}L}{1+u}
=\frac{u^{-n-1/2}}{1+u}
 \sum_{r=0}^n a_r(L+H_r^*)v^{n-r}.
\]

取 `r=n` 给非负下界；而 `a_r≤1`、`H_r^*≤2(1+log(n+1))`、`Σv^(n−r)≤2` 给只含 polynomial-log 的上界。`a_n=exp(o(n))`，所以 beta integral 的指数仍相同。于是

\[
\lim_{n\to\infty}\frac1n\log J_2(R_{n,A}(t^2))=-\rho_A. \tag{15}
\]

由于 `ρ_A≤(A+1)log2`，安全 multiplier `L_N^k` 后，ζ(k) 族的实际正值指数为 `k(A+1)−ρ_A>0`。G 的安全 `L_(2N+1)^2` 后则为 `4(A+1)−ρ_A>0`。因此标准清分母后的这些正线性型发散。这是固定安全倍率的严格失败；尚未证明该族的实际本原 content 不能产生额外指数节省。

## 5. 小例的精确本原系数：整性与 content 的范围

首例 `n=A=1` 为 `R=2u−3u²`：

\[
I_7(R)=\frac7{128}(91-90\zeta(7))>0,
\qquad J_2(R(t^2))=\frac13(14-15G)>0. \tag{16}
\]

这两个严格非零事实来自 (9)，不是对目标小数值的核验。

有限证书还精确检查以下 `I₇` 的本原整数多项式 `p+qX`：

| `(n,A)` | `N` | `R(−1)` | `p` | `q` | 最小公共分母下 content |
|---|---:|---:|---:|---:|---:|
| `(1,1)` | 2 | −5 | 91 | −90 | 7 |
| `(2,1)` | 4 | 41 | −1458167387 | 1446149376 | 1 |
| `(3,1)` | 6 | −377 | 1047543482818741 | −1038868740000000 | 1 |
| `(2,2)` | 6 | 85 | −6748090147991 | 6692220000000 | 7 |

这里先用这个具体 rational constant 和 target coefficient 的最小公共分母，再取两整数的 gcd；没有把通用 `L_N^7` 的冗余因子误计为新 content。四例不支持任何统一 content 渐近量词。

## 6. 对根分支高阶 log-moment 族的独立核查

更强候选见 [log-moment 报告](E:/kimi-build/zeta5/research/odd_zeta_log_moment_candidate_20261004.md)。对 `q≥1`、`N=qn`，定义

\[
\mathcal R_{n,q}(u)=\sum_{r=0}^{N}(-1)^r
 \binom Nr\binom{n+r}n^q u^r.
\]

其 Mellin rational function 准确为

\[
\int_0^1u^{z-1}\mathcal R_{n,q}(u)du
=\frac{(-1)^{qn}N!}{(n!)^q}
 \frac{\prod_{j=1}^{n}(z-j)^q}{\prod_{r=0}^{N}(z+r)}. \tag{17}
\]

可逐个检查 `z=−r` 的 residue；总 degree 差 `−1` 保证没有遗漏 polynomial part。由 `z=1,...,n` 的 `q` 阶零，确得

\[
\int_0^1u^m(-\log u)^j\mathcal R_{n,q}(u)du=0,
\quad 0\le m<n,\quad0\le j<q. \tag{18}
\]

`R(−1)=Σ binomNr binom(n+r,n)^q>0`，因此 (3) 的目标系数不退化。constant coefficient 恰为 `1`，这是指定整数归一化。

`q=6,k=7` 只消掉 log 次数 `0,...,5`，**没有消掉**原 `I₇` 的 top log 次数 `6`。明确反例在 `n=1`：

\[
\frac1{6!}\int_0^1(-\log u)^6\mathcal R_{1,6}(u)du=\frac17\ne0.
\]

`q=7,k=7` 则由 `1/(1+u)=Σ_(m<n)(−u)^m+(−u)^n/(1+u)` 和 (18) 得

\[
I_7(\mathcal R_{n,7})=(-1)^n\int_0^1u^n\mathcal R_{n,7}(u)W_7(u)du. \tag{19}
\]

式 (19) 是 n 阶精确尾项表达，不是指数衰减定理。事实上

\[
\|\mathcal R_{n,q}\|_{\text{coeff},1}=\mathcal R_{n,q}(-1)
\ge\binom{2n}n^q,
\]

仅用 `u^n` 与 coefficient norm 得到的安全估计是

\[
|I_7(\mathcal R_{n,7})|
\le\mathcal R_{n,7}(-1)(n+1)^{-7},
\]

右边仍指数大。这不能证明实际积分长大，只说明此上界不提供所需的变小结论。

完全性或 AT-system 的一般原理可以帮助证明多重正交多项式的 degree、实零点与 uniqueness；这些条件不自动推出指定 extra kernel `log⁶/(1+u)` 的端点值非零，也不自动给它的清分母后 decay。式 (10) 的普通 Rodrigues 非零证明不能未经证明套到 q 次 Euler/Rodrigues 算子。当前对于这个更强候选，实际 nonzero 与本原净预算保持未证。

## 7. 以目标系数归一化的正 polynomial 几何下界

这里给一个与整数 leading-coefficient 下界不同的几何基准。设任意 real polynomial `R` 的 degree 为 `N≥3`，在 `[0,1]` 非负，`B=R(−1)≠0`。则

\[
\boxed{\frac{I_k(R)}{|B|}
\ge\frac{e^{-3\sqrt2}}{4(k-1)!}
 (N+1)^{-(k+1)}(3+2\sqrt2)^{-N}.} \tag{20}
\]

证明：取 `δ=1/(N+1)`、`H=[δ,1−δ]`、长度 `l=1−2δ≥1/2`。映射到 `[-1,1]` 后，外点 `u=−1` 对应 `x₀=−3/l`。degree N 的 Legendre reproducing kernel 满足

\[
|K_N(-1,u)|\le (N+1)^2\alpha_\delta^N/l,
\quad\alpha_\delta=3/l+\sqrt{9/l^2-1}.
\]

因为 `|P_j(x)|≤1` 于 `[-1,1]`，而 Laplace 的 Legendre 表示给 `|P_j(x₀)|≤αδ^j`。用 `R≥0` 就得 `∫_H R≥l|B|/[(N+1)²αδ^N]`。`W_k` 在 H 上至少为 `δ^(k−1)/[2(k−1)!]`，且

\[
\log\alpha_\delta-\log(3+2\sqrt2)
=\operatorname{arcosh}(3/(1-2\delta))-\operatorname{arcosh}3
\le3\sqrt2\,\delta.
\]

代入即得 (20)。这是 target-normalized 比值下界，适用于非整数 R；带符号族 (5)、(17) 不在它的适用范围。

若只需要正整数 polynomial 原积分的 raw 下界，moment 分支已给更强的 `−log4` 指数，见 [cyclotomic Mellin 报告](E:/kimi-build/zeta5/research/odd_zeta_cyclotomic_mellin_20261004.md)。故不能把本节较弱的 raw 推论宣传成新的更强整性障碍；它的作用是保留 `B` 的归一化信息。任何一种正性下界都不能直接升级为实际 content 定理。

## 8. 原始 Padé 文献提供的更有力机制与边界

[Fischler–Rivoal，1309.2534v1](https://arxiv.org/pdf/1309.2534v1) 的 Theorem 1 完整解决一个 mixed Padé 问题，同时控制多个 polylog 的无穷远消零和 `z=1` 的 monodromy/endpoint 消零；它输出真正的多重 Euler integral，并证明 uniqueness。Proposition 1 把特定高深 multiple zeta 值化成 `2ζ(2k+1)`。但在 weight `7`，完整积分仍给 `1,ζ(3),ζ(5),ζ(7)` 的组合；这个身份不能变成指定 ζ(7) 无理性。该文 §6 还明确区分已有 hypergeometric integral 与尚待建立的适配 Padé 问题。

与单个 fixed-log Mellin filter 相比，该机制同时改变多个变量中的势函数，并以 endpoint 条件消掉真实干扰 polylog。它值得作为下一阶段的具体结构模板：先写 closed function system，再证明 mixed problem 的 normality 和所有 endpoint coefficients，最后核目标投影后的分母；不能用一个形式上的高阶矩消元替代这些步骤。

[Prévost–Sorokin 作者原件](https://www-lmpa.univ-littoral.fr/publications/articles/lmpa326.pdf) §3 的 theorem 给 cyclic graph 系统的 unique Hermite–Padé 解，§5 将 `C_n(1)` 认作实际 Apéry ζ(3) 近似；这是上述多条件确有算术效力的低权示例。它没有给任意奇 weight 的纯单值结论。

Catalan 的更强 hypergeometric 结构也须核实际分母。[Krattenthaler–Rivoal，0810.1927v1，Theorems 1–2](https://arxiv.org/pdf/0810.1927v1) 准确证明其指定线性型系数 `2^(4n)a_n` 与 `2^(4n)L_(2n)^2 b_n` 为整数，运用多重 hypergeometric 变换改善 standard 分母估计；作者同时明确这仍不足证明 G 无理。[Zudilin，math/0210423v1，§4](https://arxiv.org/pdf/math/0210423v1) 也明确说明该类二阶 recurrence 及其整性为何没有跨过无理性预算。不能把“有 Apéry 型 recurrence”当成一般无理性定理。

Catalan 曲线上 chain 的四项显式分解现已由另一分支得到，故无需另起庞大 factor 算法。其参数 `ρ`、`c` 降到有理 conic 商，但四个 Bloch arguments 仍在 `K(C)` 中，不能称整条 chain 为 genus-zero chain。一般分解的可靠起点仍是 Rost Proposition 2.2(H) 的有理函数域 residue 正合性以及 Milnor K₂ 的 Steinberg 关系；它们提供常数核与归纳因式分解框架，并不保证分解长度/height 的最优性。[Rost 原件](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)。

## 9. 已交付的可复核输入与后续量词

可直接继续使用的是 (5)–(15)：整数分子、普通矩消元、真实 pure-target 线性型、actual nonzero，以及一个全族固定 weight 的明确衰减指数。它是更高阶 log 消元的已认证基准，不把新的候选 (17) 标为成功推广。

对于 q7 log-moment 候选，下一项真正必要的新命题是：证明 (19) 的 actual endpoint value 非零，并给其绝对指数与所有 target/rational coefficients 的实际共同分母、gcd。对 ordinary Rodrigues 族，未解决项则是实际本原 content 的一般量词；标准 multiplier 失败已经完成证明。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_relative_family_audit_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_relative_family_audit_20261004_verify.json) 已通过，检查四个固定 Rodrigues 小例、Stirling 导数身份、G 半幂 kernel 的前三阶完整导数卷积、parity 纯目标、最小公共分母/gcd，以及 `(n,q)=(2,2),(1,6),(1,7)` 的 Mellin 因式、log 矩和 top-log 区别。不做参数扫描、不数值计算 ζ(7) 或 G；上述 analytic 全族命题由书面证明支持。

只读独立审阅状态：根任务已审 §§3–7，通过；paper_mechanism 已独立审 §§3–4 的完全单调非零与固定权指数，通过。两者都核清标准 multiplier 失败与实际本原问题的范围区别。另本文只读审过 cyclotomic Mellin 报告 §§4–8 和 log-moment 候选 §§1–4，没有发现必要实质修正。本稿此版本冻结。

## 10. 本轮归档的精确 primary 版本

- Fischler–Rivoal，*Multiple zeta values, Padé approximation and Vasilyev's conjecture*：`1309.2534v1`，2013-09-10，20 页。[PDF](https://arxiv.org/pdf/1309.2534v1)，[本地固定版本](E:/kimi-build/zeta5/literature/fischler_rivoal2013_mzv_pade_vasilyev_v1.pdf)。另有作者 2013-12-21 修订稿，21 页，[作者 PDF](https://rivoal.perso.math.cnrs.fr/articles/mzvconj.pdf)；arXiv 页面只有 v1，不存在已核验的 v2，两个版本不能混淆。
- Krattenthaler–Rivoal，*On a linear form for Catalan's constant*：`0810.1927v1`，2008-10-10，12 页；South East Asian J.Math.Math.Sci.6(2)(2008),3–15。[PDF](https://arxiv.org/pdf/0810.1927v1)，[本地固定版本](E:/kimi-build/zeta5/literature/krattenthaler_rivoal2008_catalan_linear_form_v1.pdf)。
- Prévost–Sorokin，*Hermite–Padé approximants and Apéry theorem*：[作者公开 PDF](https://www-lmpa.univ-littoral.fr/publications/articles/lmpa326.pdf)，[本地固定版本](E:/kimi-build/zeta5/literature/prevost_sorokin_hermite_pade_apery_author.pdf)，8 页。该 PDF 本身无明确首页版本日期，本文不猜出版年；归档元数据保留这个限制。

- Zudilin，*A few remarks on linear forms involving Catalan's constant*：`math/0210423v1`，2002-10-28，已在本地文献库；本轮直接核其 §4。[PDF](https://arxiv.org/pdf/math/0210423v1)。

本轮根任务已完成上述新增固定 PDF 与对应原始元数据归档；本文保留公开 primary 链接及版本范围。
