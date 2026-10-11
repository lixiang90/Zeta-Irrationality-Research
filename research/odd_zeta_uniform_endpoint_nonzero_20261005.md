# 固定目标周期的 prime-filter 非零桥梁：全部权与 Catalan 接口

日期：2026-10-05。继续已冻结的 [q=7 特例](E:/kimi-build/zeta5/research/odd_zeta_log_nonzero_20261005.md)。本稿将其非零机制推广到每个固定 `q≥2,k≥2`，并核准 Catalan 的不同分母窗口。只证明无穷指定子序列最终非零，不证明新常数无理，不证明每个 n 非零，不将单个素数的成本升级为整体指数成本。

## 1. 不预设周期无理的统一引理

设 θ 是任意固定实数；`a_n∈Q\{0},b_n∈Q`，候选有理根 `α_n=−b_n/a_n`。设一个无限指标子集具有互异素数 p_n，且

\[
v_{p_n}(\alpha_n)<0.
\tag{1}
\]

则在该子集中，`a_nθ+b_n=0` 至多发生有限次。

证明：若没有零项，结论即成立。若有一项为零，它先迫使 `θ=α_n∈Q`。此后任何零项的 p_n 都必须整除这个固定有理数的分母；有限分母不可能含无穷互异素数。因此零项有限。此证明没有把 θ 的无理性当作前提。

这是一项可复用的非零接口：先得到真实纯目标身份，再在每项的候选有理根上强制一个变化的分母素数。它不估计实值大小、整数对高度或完整 gcd。阈值通常非有效；如果 θ 是有理数，其未知分母决定例外素数。

## 2. 所有固定 q,k 的纯 ζ(k) 接口

固定 `q≥2,k≥2`。写 `N=qn`、

\[
a_r=\binom Nr\binom{n+r}{n}^{q},\quad
R_{n,q}(u)=\sum_{r=0}^N(-1)^ra_ru^r=(1+u)Q(u)+B,
\]

\[
B=\sum_{r=0}^Na_r>0,\quad
Q(u)=\sum_{m=0}^{N-1}d_mu^m,\quad
d_m=(-1)^{m+1}\sum_{r=m+1}^Na_r.
\]

真实积分身份是

\[
I_k(R)=\frac1{(k-1)!}\int_0^1
\frac{(-\log u)^{k-1}R(u)}{1+u}\,du
=B e_k\zeta(k)+S_k,
\]

\[
e_k=1-2^{1-k}>0,\qquad
S_k=\sum_{m=0}^{N-1}\frac{d_m}{(m+1)^k}.
\tag{2}
\]

该纯性与除法不要求 `q≥k`；后者只在利用完整 log-moment 消元时才需要。

取素数

\[
p=qn-1>2q,\qquad
p\nmid C_q(2^{k-1}-1),\quad C_q=q^q+(q+1)^q.
\tag{3}
\]

这里固定 q,k 时只删除有限素数。`N=p+1`、`n+1<p`，Lucas 定理使 `a_r mod p` 只在 `r=0,1,p,p+1` 可能非零，依次为 `1,(n+1)^q,1,(n+1)^q`。因此

\[
B\equiv 2C_q/q^q\ne0,\qquad
d_{p-1}\equiv-C_q/q^q\ne0\pmod p.
\]

在 (2) 唯一含 p 的分母是 p，故

\[
v_p(S_k)=-k,\quad v_p(B)=0.
\]

候选根 `α_{n,k}=−S_k/(B e_k)` 于是满足

\[
\boxed{v_p(\alpha_{n,k})=-k,\qquad
p^k\alpha_{n,k}\equiv
\frac{2^{k-2}}{2^{k-1}-1}\pmod p.}
\tag{4}
\]

Dirichlet 定理给 `p≡−1 modq` 的素数无穷，删去 (3) 的有限例外后仍无穷。引理遂给：对每个固定 q,k，(3) 的子序列中所有但有限个 `I_k(R_{n,q})` 非零，不需要事先知道 ζ(k) 无理。

若 `S_k=s/M` 已约分，则 p 不整除真实整数对

\[
\big((2^{k-1}-1)MB,\ 2^{k-1}s\big)
\]

的 gcd，约成整数本原对后的 p 赋值为 `(k,0)`。这仍仅是局部结论。

## 3. Catalan 接口用不同的 prime window

同一 R 的真实 Catalan 积分为

\[
J_G(R)=\int_0^1\frac{(-\log t)R(t^2)}{1+t^2}\,dt
=BG+S_G,
\qquad S_G=\sum_{m=0}^{N-1}\frac{d_m}{(2m+1)^2}.
\tag{5}
\]

固定 `q≥2`，取 `n≥2` 以及素数

\[
p=2qn-1=2N-1.
\tag{6}
\]

此时 `N+n=(q+1)n<p`，因为 `(q−1)n>1`。所以

\[
a_N=\binom{N+n}{n}^{q}
\]

是 p-unit，而 `d_{N-1}=(-1)^Na_N` 也是 p-unit。分母 `2m+1` 从 1 到 `2N−1=p`，唯一含 p 的分母是最后一个。因此

\[
v_p(S_G)=-2,\qquad
\boxed{v_p(-S_G/B)=-2-v_p(B)<0.}
\tag{7}
\]

这里不要求 B 是 p-unit；若它含 p，只会进一步提高候选根的分母成本。这与 ζ 接口需要控制 B 的 Lucas 窗口有明确区别。

Dirichlet 定理给 `p≡−1 mod2q` 的素数无穷，删掉有限的 `n<2` 情形后，引理给：每个固定 q 的 (6) 子序列中至多有限个 `J_G(R_{n,q})=0`。该结论同样不预设 Catalan 常数无理。

约分 `S_G=s/M` 后，真实整数对 `(MB,s)` 的 gcd 不含 p，本原对的 p 赋值为 `(2+v_p(B),0)`。没有换用统一 LCM，也没有遗漏 B 可能有的额外 p 因子。

## 4. 统一与预算的准确范围

本稿的“统一”指固定参数下，同一候选有理根引理同时处理奇数 ζ 与 Catalan；不是对全部 q,k 给同一个有效例外阈值。Dirichlet 是明确的标准外部输入；有限验证不证明它。

每项只强制一个 `p=O(n)`，所以单项下界 `logM≥klogp` 或 `2logp` 仍是 `o(n)`。本稿不由此导出完整分母指数或充分大的 content。若未来某族能在相同子序列认证本原整数线性型趋零，这个引理就独立支付无穷非零要求；若实侧没有衰减，它也不能挽救预算。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_uniform_endpoint_nonzero_20261005_verify.py)与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_uniform_endpoint_nonzero_20261005_verify.json)核六个预先指定输入：ζ 接口 `(q,n,k,p)=(2,3,3,5),(3,4,5,11),(7,6,7,41)`，Catalan 接口 `(q,n,p)=(2,2,7),(3,2,11),(7,3,41)`。验证全部精确分母、根估值、同余与本原整数对；不数值计算任何目标周期，不扫描参数。全尺度命题来自 §§1–3 的书面证明。

只读独立审阅：根任务已完整复核统一引理、ζ 与 Catalan 的不同素数窗口、全部局部估值、完整 content 范围及量词，通过。本稿此版本冻结。
