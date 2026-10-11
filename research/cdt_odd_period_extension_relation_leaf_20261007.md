# 周期扩张中的数值关系与真实填洞：Apéry 校准和九阶 ζ(5) 实现

2026-10-07，NEW，作者 /root/source_pencil_finalize。Authority 为总稿 §§171–175 与 delivery_kernel_profiles，SHA `313ad01a4abe88dd8a8193561b30232dfa131c8832d126af18390eafc8514e72`；572 个旧冻结记录（567 数学、5 guards）只读。本人实际全文读该轮 authority、旧 conifold/R0 四稿及本轮原件下列页域，不声称全文人工重审所有572记录。本轮纯纸证：数学 producer 的创建、execute、import、rerun 及 prime 扩表均为0。PDF 提取/渲染、正常 TLS 归档和文件 SHA 属文献操作。

真实数值源始终为 ξ=αζ(4)+βζ(5)，α、β 固定有理，β≠0。本文没有替换原 B 的整模型或移植其费用。先建立已知 ζ(3) 的真正填洞校准，再给同一 ξ 的明确新函数实现，证明其端点关系为什么尚不能填洞。新的具体接口是：关系必须控制连接矩阵的完整跳跃系数；普通点值为零不能代替这项条件。

## 1. 完整跳跃消去的可检查接口

在同一实际 regular-singular 系统和固定解析延拓路径中，设 A 是一个齐次周期，B 是一个指定非齐次解；两者的 Taylor germ、基点和有理结构已固定。令 F_c=cA−B。设存在实际正规函数 V 和精确常数 κ，使

\[
V=\kappa A-B,
\qquad V\text{ 在穿孔点 }\sigma\text{ 延拓为 holomorphic germ}.
\tag{E1}
\]

同一个局部 monodromy T 因此给出完整函数 germ 身份

\[
(T-I)F_c=(c-\kappa)(T-I)A.
\tag{E2}
\]

若 (T−I)A≠0，则 c=κ 恰好消去整个跳跃，不只是一个端点 flag 或最高 log 系数。若该系统在 σ 的指数无负整数，且单值解无 pole，则 E2 为零进一步给 holomorphic 填洞；否则应保留真实 meromorphic pole。E1 是 connection identity，不能由 F_c(t_0)=0 推导。对多个独立 log 链或多个 punctures，必须逐个支付所有 monodromy 分量。有限覆盖只消去有限阶部分，不能消去非零 log 链。

数值有理性可同时产生合理 Taylor germ 和更大实际 leaf，必须是 κ∈Q 令 E2 消失这类情形。若仅 F_c=F_0−c，则所有跳跃与 c 无关；即便 F_c(t_0)=0，也没有这个机制。

## 2. 已知 Apéry 正规函数：同一 germ、全系数和完整分母

本节只校准已知 ζ(3) 无理性，不把 ζ(3) 替换为本项目目标。GKS v3 PDF28 的实际 V12 模型给

\[
\mathcal L=\theta^3-t(2\theta+1)(17\theta^2+17\theta+5)+t^2(\theta+1)^3,
\quad \theta=t\frac d{dt}.
\tag{E3}
\]

取 A=Σ a_nt^n，a_n=Σ_{k=0}^n binom(n,k)^2binom(n+k,k)^2，A(0)=1、a_1=5；取 B=Σ b_nt^n，b_0=0、b_1=1、LB=t。其实际 higher normal function V 满足 LV=−12t、V_0=2ζ(3)、V_1=−12+10ζ(3)，所以唯一 analytic germ 的初值比较给

\[
\boxed{V/12=(\zeta(3)/6)A-B.}
\tag{E4}
\]

每个 n≥0 都有实际 integral coefficient

\[
[t^n]V=I_n=
\int_{[0,1]^3}
\frac{[x(1-x)y(1-y)z(1-z)]^n}
{[1-z(1-xy)]^{n+1}}\,dx\,dy\,dz>0,
\quad I_0=2\zeta(3).
\tag{E5}
\]

这项连接和归一化来自同一实际正规函数，不是任意添加一个 ζ(3) 常数。原 Apéry 文献 PDF4 的整数模块断言为 2D_n^3v_n∈Z，其中 D_n=lcm(1,…,n)、v_0=0、v_1=6；原 recurrence 与 E3 完全相同，所以 v_n=6b_n。保守而足够的完整全 prime cap 是

\[
a_n\in\mathbf Z,\qquad 12D_n^3b_n\in\mathbf Z.
\tag{E6}
\]

这里只使用原件明确的倍数12，不需要更强的 D_n^3b_n 整性。若 c∈Q，取固定 d 清掉 c 的分母，则对全部 n≥0

\[
12dD_n^3[t^n](cA-B)\in\mathbf Z.
\tag{E7}
\]

固定12d、所有小 prime、constant coefficient 均已支付。

### 全 n 的实际定义域扩大

令 f=x(1−x)y(1−y)z(1−z)/(1−z+xyz)。对 a=xy，直接求 z 的最大值得 z=1/(1+√a)，且 z(1−z)/(1−(1−a)z)≤1/(1+√a)^2。设 s=√xy，则 (1−x)(1−y)≤(1−s)^2。故

\[
0\le f\le\left(\frac{s(1-s)}{1+s}\right)^2
\le\rho:=(\sqrt2-1)^4=17-12\sqrt2.
\tag{E8}
\]

最大值在 s=√2−1 取得；可在 interior 取 x=y=s、z=1/√2。直接由 E5 积分支配得到全部 n 的正性和衰减

\[
0<I_n\le I_0\rho^n.
\tag{E9}
\]

因此 V/12 的真实 Taylor 函数在 |t|<ρ^−1=17+12√2 内 holomorphic，包括最近的 conifold t=ρ。系统 E3 的两个非零有限 singularities 恰为 ρ、ρ^−1。展开普通导数，在任一根 r 处 leading a_3=t^3(1−34t+t²)，a_2(r)=(3/2)r³(2r−34)；indicial polynomial 为非零常数乘 s(s−1)(s−1/2)。所以局部指数是0、1、1/2，不应把此处的 rank-one 反射称为 unipotent transvection。

A 的 radius 恰为ρ：对 k/n→u，Stirling 给单项 n-th log 主率 2[(1+u)log(1+u)−(1−u)log(1−u)−2u log u]，在 u=1/√2 最大，值4log(1+√2)。选 k=floor(n/√2) 给下界，至多 n+1 项给同一上界。因此 lim a_n^(1/n)=ρ^−1。除ρ外没有同模 singularity；若其跳跃也为零，上述非负指数会使 A holomorphic 穿过ρ，从 E3 继续到更大 disk，矛盾。故 ΔA≠0，且 E4/E9 严格实现

\[
\boxed{\Delta_\rho(cA-B)=(c-\zeta(3)/6)\Delta_\rho A.}
\tag{E10}
\]

若 c=ζ(3)/6∈Q，E7–E9 给正整数 12dD_n³I_n/12，且由 logD_n=n+o(n) 及 logρ^−1>3 使其趋0，恢复已知矛盾。这里 e<3、ρ^−1>29>27 已给严格 logρ^−1>3。没有把有限系数实验当全 n 证明。

### 实际函数 rank 与 CDT 的限制

对任何 c，F_c=cA−B 不可能是有理函数。若 LF_c=−t 有有理 particular，则0处指数0,0,0和两个 conifold 的上述指数排除有限 pole；ordinary points 也排除 pole。因此 particular 必是多项式。但最高 degree d 的项经 t²(θ+1)³产生非零 degree d+2，不能等于−t。因此 {1,F_c} 的 Q(t) rank 恰2。

在有理性假设下，E7 给予 CDT 的 row sums (0,3)、e=(0,0)，τflat=9/4，τsharp=0。对 filled disk 的简单 φ(z)=rz、r<ρ^−1，CDT Cor.6.0.14 分子 J(φ)=log r；其 q=2 矛盾要求 log r>9/2。这里 logρ^−1<4，因为 ρ^−1<35<(8/3)^4<e^4。因此仅此 disk 不能产生 CDT rank 矛盾。E9 的 scalar 正整数方法确实成功；更大 slit/Riemann leaf 或别的函数包需要另算实际 conformal 分子。正文没有声称 disk 填洞已解决 CDT 的全部余量。

## 3. 实际 ξ 的新九阶函数实现：全部端点常数显式

取

\[
\mathbf a=(\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12,
\tfrac15,\tfrac25,\tfrac35,\tfrac45),\quad
U(w)=\sum_{n\ge1}u_nw^n,\quad
u_n=\frac{(n!)^9}{n^9\prod_j(a_j)_n},
\]
\[
w_0=-\frac{1024}{3125},\quad
P(T)=5532T^4-5600T^3+2275T^2-425T+30,
\quad G(w)=-\frac{P(\theta_w)U(w)}{380928}.
\tag{E11}
\]

所有 Taylor coefficients 属Q；U_0=0、U_1=2500/3，radius 为1。Au v4 Example X（PDF19，后续 Example XV PDF25–26）证明确切的 analytic identity

\[
\boxed{G(w_0)=\zeta(5).}
\tag{E12}
\]

本文使用已经证明的 E12；Kerr2026 Theorem4.11/Example4.14 将同一 U(1/z) 解释为规范 hypergeometric normal-function quasi-period。该几何解释在相应段落有 motivic-generator 假设；4.11(ii) 的 ζ 值一般定理另要求 Hodge conjecture 和 cycle defined overQ。本文不从这些未核的额外假设推 E12，更不把新的九阶几何实现宣称为已证明的 ζ(5) 无理性。

支付 even zeta carrier：选基点0处 arctan0=0，并沿实线从0到w_0延拓，定义

\[
R(w)=\frac{128}{45}\arctan(w/w_0)^4,
\quad R(w_0)=\frac{128}{45}(\pi/4)^4=\zeta(4).
\]
\[
\boxed{F_c(w)=\alpha R(w)+\beta G(w)-c,
\qquad F_c(w_0)=\xi-c.}
\tag{E13}
\]

这里 α、β、c 固定有理、β≠0；128/45、380928、π 分支和 endpoint 全部保留。R 是 elementary Tate-period carrier，G 是上述指定 quasi-period 的 rational differential projection。没有混入未列的 ζ(3)、log2 或任意 connection 常数。w_0 是 U 的 ordinary point，R 的实际 branchpoints 为 ±iw_0，亦不在实 endpoint；数值关系只令一个 ordinary point 的 F_c 值为0。

## 4. 九阶真正 log 障碍与所有有理变基后的 common module

因为 a tuple 关于1/2对称，u_n 的真实 recurrence（n≥2）为 u_n/u_{n−1}=(n−1)^9/∏_j(n−a_j)。连同 n=1 初值，严格有

\[
\bigl\{\prod_j(\theta_w-a_j)-w\theta_w^9\bigr\}U=w.
\tag{E14}
\]

在 u=1/w、D=u d/du 中，等价地

\[
\mathcal P_9 U=1,\qquad
\mathcal P_9=D^9-u\prod_j(D+a_j).
\tag{E15}
\]

这是同一选定 rational Taylor germ 的解析延拓方程，不是替换 particular solution。可直接造 local Frobenius family

\[
\Phi(s,u)=u^s\sum_{n\ge0}
\frac{\prod_j(s+a_j)_n}{(s+1)_n^9}u^n,
\qquad \mathcal P_9\Phi=s^9u^s.
\tag{E16}
\]

在 s=0 的前0,…,8阶导数形成齐次解的9阶 log 链；9阶导数 Z_9 满足 P_9Z_9=9!。因此任何 E15 的 particular 都与 Z_9/9! 差一个齐次解，且其 u=0 leading coefficient 必含 (logu)^9/9!。齐次解最多 log^8，不能改变此最高项。由 P(0)=30 和 θ_w=−D 得

\[
G(1/u)=-\frac{30}{380928\cdot9!}(\log u)^9
\quad\text{mod lower log degree and positive }u\text{ terms}.
\tag{E17}
\]

在 infinity 的任何 fixed local branch，R(1/u) 为 holomorphic germ（arctan(1/(uw_0))=π/2 的一个固定 odd integer multiple 加 analytic u-series）。所以 E13 的最高 log^9 系数为−30β/(380928·9!)，非零且不含 c。有限覆盖 u=v^h 只乘 h^9，不能消去这个跳跃。有理乘子即使有有限阶 zero，也仅把 log 链乘一个非零 Laurent monomial，仍不能使其单值。

从而对每个 c∈Q，{1,F_c} 的 Q(w) rank 恰2，而且完整 module 准确相同：

\[
\boxed{\operatorname{span}_{\mathbf Q(w)}\{1,F_c\}
=\operatorname{span}_{\mathbf Q(w)}\{1,F_0\}.}
\tag{E18}
\]

对任意 fixed holomorphic map，完整 basis 的 function pullbacks 是否 meromorphic 是 module 性质，任何 invertible Q(w) 变基都不能改变 E18 的共同 leaf。具体 scalar F_c 与 F_0 的所有跳跃也完全相同，且 positive-index Taylor coefficients 完全相同。c 的有理分母仅需一个 fixed multiplier。

因此这份实现不会在 ξ=c 的假设下产生新的 relation-filled leaf 或新的函数 rank。它确实跨出了 canonical polynomial-in-Ξ 模型，却仍有一个可检查的 common-reference obstruction：若仅用同一 pair 的 rank、全 prime cap 和 meromorphic leaf 构造 CDT 矛盾，同样的数据已经对有理 Taylor reference F_0 存在。该结论只针对此实现及其完整 module；不排除别的 higher normal functions、Hadamard systems 或真正以 c 改变 connection vector 的实现。

## 5. 全 prime cap、变量缩放与 CDT 分子一并支付

先在原 w 坐标精确化 u_n。Pochhammer multiplication 给

\[
u_n=\frac{3200000^n(n!)^{15}}
{n^9((2n)!)^5(5n)!}
=\frac{3200000^n}
{n^9\binom{2n}{n}^5\binom{5n}{n,n,n,n,n}}.
\tag{E19}
\]

对任意 prime p，令 x={n/p^k}。每层 factorial valuation 为
15floor(n/p^k)−5floor(2n/p^k)−floor(5n/p^k)
=−5floor(2x)−floor(5x)≥−9。
当 p^k>5n 时为0。因此全部 primes（包括2、5）均由

\[
\boxed{n^9D_{5n}^9u_n\in\mathbf Z}
\tag{E20}
\]

清分母；3200000^n 的 prime 因子只会有帮助。P(n) 为整数，G 再支付 fixed380928。

R(w) 的 arctan(w/w_0) coefficient 含 (−3125/1024)^n；其 2^{10n} 不能由 fixed multiplier 或 D_{5n}^9 免费覆盖。因此明确换变量

\[
w=1024s,\quad \widehat F_c(s)=F_c(1024s),
\quad s_0=-1/3125.
\tag{E21}
\]

此时 arctan argument 为−3125s。arctan^4 的每个 coefficient 是四个 odd positive indices ≤n 的卷积；各 index 整除 D_n，所以 D_n^4 足够。结合 E20，存在只依赖固定 α、β、c、45、380928 的整数 M，使全部 n≥1

\[
\boxed{M n^9D_{5n}^9[s^n]\widehat F_c(s)\in\mathbf Z.}
\tag{E22}
\]

constant coefficient −c 也由 M 支付。这是 scaled s 坐标的完整 safe upper cap，不是未证明的 optimal lower cost。scaled finite singular positions 同时变为 U 的1/1024、R 的±i/3125；infinity log 点仍在 infinity。原 endpoint−1024/3125 改为−1/3125。没有把 w 平面的 conformal radius 留在 s 平面。

由本轮实际读取 CDT PDF66–69 的 Theorem6.0.2/Cor.6.0.14，pair (1,M\widehat F_c) 可取九列 b=(0,5)^t、e=(0,9)，所以

\[
\sigma=(0,45),\quad \tau^{\flat}=135/4,
\quad\tau^{\sharp}=27/4,
\quad\boxed{\tau=81/2.}
\tag{E23}
\]

τsharp 由 Basic Remark6.0.17 的 e=(0,1) 值3/4乘9；同一正比例变换保留最小化。所有函数 holonomic，所以可用 Cor.6.0.14 的 holonomic 条件而非要求 conformal size>e^{45}。但仍必须存在实际 holomorphic map φ:(D,0)→(C_s,0)，其 function pullbacks 1、M\widehat F_c∘φ 在 unit disc 上 meromorphic，满足 |φ'(0)|>e^{81/2}，并支付

\[
J_s(\phi)=\iint_{\mathbb T^2}
\log\max(|\phi(z)|,|\phi(w)|)\,d\mu_H(z)d\mu_H(w),
\quad
2\le\frac{J_s(\phi)}{\log|\phi'(0)|-81/2}.
\tag{E24}
\]

边界 integral 可按合法 radial exhaustion/limit 使用，须保持定理边界假设。若对原 w-map ψ 改为 φ=ψ/1024，则 log|φ'(0)|=log|ψ'(0)|−log1024，J_s=J_w−log1024；scale 的 archimedean 代价明确存在。本文没有找到击破 E24 的 actual leaf，也没有把 τsafe 太大当真实费用下界。

## 6. 本轮成果、未证处与文献实读

本文的可用新接口包括：E1–E2 的完整 connection-jump 条件；E4–E10 对一个真实 higher normal function 的同对象校准与全 n 域扩大；E11–E18 为原 ξ 给出所有 endpoint 常数都支付的九阶实际 analytic 实现和 rational-basis common-module 障碍；E19–E24 给该实现准确变量中的全 prime cap 和 CDT 费用。已知 Apéry 结论仅作机制校准。九阶 source 模型尚未产生新的无理性、LI 或 Lean 定理。

下一缺口现在具体化为：找到 ξ 作为 cA−B 的真实 connection coefficient，且在 c=ξ 的假设下 E2 的全部实际跳跃消失，保留 Q(x) independent functions 和完整 Taylor caps。证明 Hodge point 的 ordinary endpoint 取值或高层 regulator singularity class 为零，均不能替代这个 equality。真正不同的几何实现仍值得寻找；本模型的障碍不能提升为一般 no-go。

本轮本人 primary 实际 distinct 页域如下（不继承上轮读页）：

- GKS v3，既有 `golyshev_kerr_sasaki2023_apery_extensions_v3_20261006.pdf`：PDF1–4、21–25、28–30，12页；归档整本35页不是本人本轮全文读。
- Apéry1979，既有 `apery1979_asterisque.pdf`：实际全文 PDF1–4，4页（包含 archive cover）。原整模块取保守固定12倍。
- Kerr2020，新增 [Unipotent extensions and differential equations](https://arxiv.org/abs/2008.03618v1)：正常 TLS 原件 `../literature/cdt_period_extension_sources_20261007/kerr2020_unipotent_extensions_arxiv2008_03618v1.pdf`，38页，553617bytes，SHA `9eb05bd0f73e26a2861257dd844dabd170b525dd456a479548f9c96eb0c20e98`；本人实际 PDF1–5，5页，用于 unipotent extension/Frobenius 背景而非无条件套用其所有结论。
- Kerr2026，新增 [Three vignettes on hypergeometric normal functions](https://arxiv.org/abs/2602.04128v1)：正常 TLS 原件 `../literature/cdt_period_extension_sources_20261007/kerr2026_three_vignettes_arxiv2602_04128v1.pdf`，25页，735709bytes，SHA `e619e19d73f196a64d1deb5cc6744e338fa150889c9b89a033a0552a02d2ec1e`；本人实际全文 PDF1–25，25页，特别保留4.11(ii)的 cycle/Hodge 条件。
- Au v4，新增 [Wilf–Zeilberger seeds and non-trivial hypergeometric identities](https://arxiv.org/abs/2312.14051v4)：正常 TLS 原件 `../literature/cdt_period_extension_sources_20261007/au2024_wilf_zeilberger_seeds_arxiv2312_14051v4.pdf`，30页，938673bytes，SHA `e1312118c89628b095878a1b8c0e7166470a1b11b804905722e5faa743fbb78c`；本人完整读 PDF1–2、16、19、25–26，共6页。PDF26 提取有乱码，已实际渲染目读；PDF27 的未完整乱码提取不计读页。Example X 的非零 g(n) boundary term 与 Example XV 的 pole subtraction 均保留，不执行 WZ notebook。
- CDT 固定 v2，既有 `cdt2024_l2_chi_minus3.pdf`：本轮完整读 PDF66–69，4页。

本稿相关 primary distinct 共56页，新归档原件3份；不把新增38+25+30整本93页均称为全文阅读。本人随后单独审相位稿所读 primary 如有新增，列在该审稿/最终来源收据，不能混算为本文已读。唯一 NEW 主稿待 actual FULL 独审，收审后全文回读再单向 FINAL 来源收据；旧572记录不改。
