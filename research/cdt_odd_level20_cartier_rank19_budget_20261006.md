# level20 六个真实核积分的 rank19 系统：一张固定合法账本

日期：2026-10-06。本文只新增，不修改冻结旧稿，不枚举背景或扫描素数。输入是已证实际 rank19、同一共同解析叶、完整 nD_n³类型，以及旧三个 H-target rows 的 S1/S2。结论是一个固定安全 unit 数组及其全部 cutoff 的精确成本；没有给六个新积分免费 Smith 信用，也没有排除其它类型、格或 packet 输入。

## 1. 真实系统与完整类型

使用 [实际 cohomology §2–4](cdt_odd_level20_cartier_cohomology_20261006.md) 的单 sign 六个正规 H primitive

\[
R_j=t^j/D_-,\quad D_-=(1-t)N_-C_-,\quad 0\le j\le5,
\]
\[
J_j^H=\int_0^t\{R_j(v)H_-(v)-R_j(0)H_-(0)\}\,dv/v.
\tag{R1}
\]

它们是实际函数。该稿证明每个非零核的类 non-exact、六个新增方向在 P10+W_H 之外仍独立，故

\[
\mathcal F_{19}=\mathcal P_{10}
  +(gH_-,g\theta H_-,g\theta^2H_-)
  +(J_0^H,\ldots,J_5^H),\qquad g=\Delta^2
\tag{R2}
\]

实际 rank=19。这里 P10 已含常数1；没有另外重复计 W_H 的常数。I_H=J_{R=1}^H 本来就是六个核积分的 constant linear combination，因为 D_- 是 degree5 多项式，也不能再次追加计一维。

全部函数的微分闭包是 rational connection：背景方程来自 [低成本 P10](cdt_odd_low_cost_polylog_20261006.md)，旧 H 方程来自 [完整模型](cdt_odd_level20_model_20261006.md)，新增 J 的导数由 (R1) 给出。实际 leading cutoff 可用闭合系统的 Shidlovsky 估计 N_D=19(D+1)+O(1)。[正规 primitive 叶](cdt_odd_level20_cartier_primitive_leaf_20261006.md) 与 cohomology 稿证明六个 J^H 都共用此前真实 G-disk；不得将带 ΘJ^A 的完整 Cartier primitive 当成这些 J^H。

固定以下粗 unit 安全型。D_n=lcm(1,…,n)；每行都容许原完整模型的固定清因子与固定指标偏移。

|实际函数|flat unit columns 数 σ|序号指数 e|完整安全型|
|---|---:|---:|---|
|1|0|0|1|
|L|0|1|n|
|T₂、Li₂|1 各一行|1|nD_n|
|T₃、L Li₂、Li₁,₂、Li₃|2 各一行|1|nD_n²|
|K₂|2|0|D_n²|
|I_K|2|1|nD_n²|
|三个旧 H-target rows|3 各一行|0|D_n³|
|六个 J_j^H|3 各一行|1|nD_n³|

背景类型取已证安全型的 unit 粗化，未使用分数尺度的放宽值；六个 J 行的 e=1 完整保留。

## 2. 原 flat 值和同一 cutoff 的 Smith 接口

按 σ 排序，完整 unit 表为

\[
\sigma=(0^2,1^2,2^6,3^9),\qquad
\sum\sigma_i=41,\quad E=\sum e_i=14,\quad e_*=1.
\tag{R3}
\]

三个 binary columns 可取嵌套列，CDT 原 unit-array transportation 值精确为

\[
\boxed{\tau^{\flat\flat}
=\frac1{19^2}\sum_{i=1}^{19}(2i-1)\sigma_i
=\frac{12+168+783}{361}=\frac{963}{361}.}
\tag{R4}
\]

这是具体嵌套 unit 表的真实值，不是任意分数数组的 comonotone 放宽下界。

沿用 [已冻结 integrated tensor bridge](cdt_odd_level20_integrated_tensor_bridge_20261006.md) 的定义，θ_i=max(1/b_i,h)；两条 zero-column 行为1与L，其余θ=1。因此 a₀=2，a(ξ)=min(ξ,1)。序号指数不进入 matching θ；它在同一 ξ 的 sharp 部分计入。

ν_i=σ_i+e_i、s=maxν_i 给

\[
\boxed{\nu=(0,1,2^3,3^8,4^6),\quad s=4,
\quad\sum\nu_i=55.}
\tag{R5}
\]

对 p²>N_D 的好素数，pure p⁴-prefix matrix 的背景／新增积分 certified floors 为4−ν_i。旧三 target 的 floor 本来为1；旧 S1将 k₁ 个方向提升至threshold2，旧 S2将 k₂ 个方向提升至threshold3：

\[
k_1=2(D-\delta_H+1)_+,\quad\delta_H\le(3p+9)/2,
\qquad k_2=(D-3p-19)_+.
\tag{R6}
\]

threshold1、2、3、4 的 baseline 数分别为13、5、2、1乘(D+1)，故

\[
\boxed{\sum\text{certified floors}
\ge21(D+1)+k_1+k_2,
\qquad 4-21/19=55/19.}
\tag{R7}
\]

六个新 J 的 baseline floor为0，没有另加 S3/S4。额外行只是扩大原 pure 坐标格：旧关系仍只支持三个旧 target blocks，其 threshold 必须按 p⁴ 缩放移至2和3。near-balanced 张量的 cap相应为4，codimension损失4dc；固定 source 的其余处理沿用 integrated bridge。匹配内窗 p≤min(ξ,1)D 保留，因 a₀=2不限制旧收益。因此同一 cutoff 的合法成本是

\[
\boxed{\kappa_{19}(\xi)=\frac{963}{361}
 +\frac2{361}\{14\xi+I_{19}(\xi)-\gamma(\min(\xi,1))\},}
\tag{R8}
\]

γ是旧 S1/S2 素数积分，最大5/6。其 finite 归一信用为γ/19，最终成本信用为2γ/361；不把新 rank19 自动换成新的局部收益。含多重积分的 e 不影响支持分离的已证旧行，但各行的 source 与 sharp 基线仍完整付费。

## 3. 全 cutoff 的直接精确核算

令 P(ξ)=14ξ+I₁₉(ξ)。直接使用原 Definition6.0.1 及 integrated bridge 的全尺度式。对0≤ξ≤1，

\[
P'(\xi)=14-19+\xi=\xi-5<0.
\tag{R9}
\]

对ξ≥1，将每个k=1,…,18的两个原积分项合并。置u_k=19−kξ，则

\[
A_k(\xi)=\frac{(u_k-1)_+}{k}
 +\frac{\min(1,(u_k)_+)^2}{2k}
=\begin{cases}
(u_k-1/2)/k,&u_k\ge1,\\
u_k^2/(2k),&0\le u_k\le1,\\
0,&u_k\le0.
\end{cases}
\tag{R10}
\]

其导数从−1经−u_k到0单调不降，各项都是 convex，P亦convex。在

\[
19/15\le\xi\le18/14=9/7
\]

时k≤14均有u_k≥1，k≥15均有u_k≤0。因此

\[
I_{19}(\xi)=\frac{37}2H_{14}-14\xi,
\quad P(\xi)=\frac{37}2H_{14},
\qquad H_{14}=\frac{1171733}{360360}.
\tag{R11}
\]

convex性及 (R9) 证明这是全[0,19]的minimum；无需 cutoff 搜索。该整个最小区间ξ>1，故γ已饱和5/6。P≥Pmin、γ≤5/6并在相同区间同时等号，得到真正的逐尺度minimum

\[
\boxed{\min_\xi\kappa_{19}(\xi)
=\frac{963+37H_{14}-5/3}{361}
=\frac{389780201}{130089960}.}
\tag{R12}
\]

例如固定 ξ=9/7 就实现该成本；并非把已经最小化的 τsharp 与另一 ξ 的最大收益相减。

## 4. 该固定表仍不能跨当前解析门槛

当前共同 cover 的原点唯一零点、省去1给ρ≤log16；普通 Jensen 或已证明 numerator≥ρ 的标准 convexity 需要

\[
\boxed{\rho>\frac{19}{18}\min\kappa_{19}
=\frac{389780201}{123243120}.}
\tag{R13}
\]

此数减14/5为8939893/24648624>0，而14/5>log16由先前正Taylor有理证书已严格证明。因此这张固定合法表失败。

这不否定六个 actual 新积分的增秩，也不否定全p三维实际 Hecke 核。这里只说明：给新增 nD_n³行完整成本、只保留已证旧 S1/S2时，这个具体 rank19 系统的 unit 账本没有严格余量。未分析其它 denominator 类型、换基、改格、真实 mixed Cartier 新高层、target 积分更深扩张或其它解析几何，不将本表扩大为统一 no-go。

## 5. 核验范围

[配套新 Fraction 脚本](cdt_odd_level20_cartier_rank19_budget_20261006_verify.py) 与 [JSON](cdt_odd_level20_cartier_rank19_budget_20261006_verify.json) 由作者执行26项检查，只核这一个固定表的 counts、flat值、ν/floors、全ξ最小区间的端点与成本、严格有理门槛；不运行旧producer，不枚举类型族或素数。R9–R11的全ξ论证、实际rank、共同叶、完整类型及 tensor 接口分别依靠正文与明确引用的已审数学输入。未证明新积分的额外Smith，也没有新的数值无理性结论。

root 已对实际正文 §1–5 作完整只读独审，通过安全类型、实际行数、旧 target threshold2/3与纯支持扩格、matching a₀=2、全ξ凸性与plateau、κ和必要尺度的有理核算及限定scope；未执行本稿或旧producer。
