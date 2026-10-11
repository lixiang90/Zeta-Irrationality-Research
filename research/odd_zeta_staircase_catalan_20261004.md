# Catalan 旧坐标中固定基变换与多类型算术阶梯的障碍

日期：2026-10-04。本文只研究旧规范变量 `w=z/16`；[bridge 报告](E:/kimi-build/zeta5/research/odd_zeta_bridge_catalan_20261004.md) 与 [system 报告](E:/kimi-build/zeta5/research/odd_zeta_bridge_catalan_system_20261004.md) 保持冻结。本文不以共同前缀分母的指数下界代替 CDT 的精细算术类型，而给出一个更早的逐素数出现位置，从而直接约束其中的 lcm 层。

## 1. 新结论及范围

固定 `c∈Q`，令

\[
V_c=\mathbf Q(w)\operatorname{span}\{1,F,U,f_c\},\qquad U=\theta F,\quad\theta=w\frac d{dw},
\]

其中 F、f_c 与原点正则芽均按 system 报告的定义。该空间实际秩为 4。

**主命题。** 对每个固定的 `h∈V_c∩Q[[w]]`，若 `h∉Q(w)`，存在常数 `K_h≥0` 和有限素数集 `S_h`，使每个充分大的奇素数 `p∉S_h` 都出现在 h 的某个系数分母中，而且该项的位置满足

\[
1\le m\le \left\lceil\frac{p-3}{4}\right\rceil+K_h.
\tag{1}
\]

这同时覆盖任意非零固定组合 `P(w)F+Q(w)U`，以及 f_c 系数非零的整个商方向；不需要假定 `c−G≠0`。允许先乘一个固定 w 的幂使亚纯芽正则，结果只改变 K_h。

其两个直接推论是：

1. h 的实际共同前缀分母 `δ_h(N)` 满足 `liminf logδ_h(N)/N≥4`。
2. 若 h 有 CDT 精细分母类型 `n^e∏_j lcm(1,…,⌊b_j n+c_j⌋)`，其中 e、b_j、c_j 都固定，那么至少一个活动层满足 `b_j≥4`。这一点不能从前缀指数单独推出；关键是 (1) 给出的 `m<p`。

因此，在旧 w 坐标内，任意固定有理基变换、任意固定阶有理微分组合，都不能把这些非有理方向改成纯 `n^e` 类型。本文不处理代数变量替换、N 依赖的变换、Hadamard 操作、张量积、另一个周期系统或新的整模型。

## 2. 每个非有理方向均可经固定阶运算恢复 F

采用 system 报告中的有理系数

\[
A=\frac{8w-3}{16(1-w)},\quad B=\frac{3w-2}{2(1-w)},\quad C=\frac1{32(1-w)},
\]

\[
k=\frac{2w}{1-4w},\quad r=-\frac{10w}{1-4w},\quad s=-\frac{12w}{1-4w}.
\]

实际函数满足

\[
\theta F=U,\quad\theta U=AF+BU+C,\quad\theta f_c=kf_c+rF+sU.
\tag{2}
\]

下文使用旧报告已经独立证明的两个有理解排除：

- Riccati 方程 `θt+t²=A+Bt` 在 C(w) 中无解。
- 二维非齐次系统 `θβ=kβ−Aγ+r, θγ=−β+(k−B)γ+s` 在 C(w) 中无解；其 forcing 取相反号也无解，因为整体取负会给前一个系统的解。

这两个排除都由有限点极点阶与无穷远的谱证明，与 c 或 G 的数值无关。

### 2.1. 三维下层 W 中的恢复公式

令 `W=Q(w)span{1,F,U}`，写

\[
h=T+PF+QU,\qquad T,P,Q\in\mathbf Q(w).
\]

若 h 非有理，则 P、Q 不同时为零。由 (2)，

\[
\binom{h-T}{\theta h-\theta T-QC}
=M\binom F U,
\quad
M=\begin{pmatrix}P&Q\\\theta P+QA&P+\theta Q+QB\end{pmatrix}.
\tag{3}
\]

这个矩阵一定可逆。Q=0 时行列式是 P²；Q≠0 时令 `t=−P/Q`，有

\[
\frac{\det M}{Q^2}=\theta t+t^2-Bt-A.
\tag{4}
\]

行列式为零会给已排除的 Riccati 解。因而

\[
F=\frac{(P+\theta Q+QB)(h-T)-Q(\theta h-\theta T-QC)}{\det M}.
\tag{5}
\]

特别地，存在固定有理微分算子 D_h，阶数至多 1，及固定有理 R_h，使 `F=D_hh+R_h`。

### 2.2. f_c 商方向也不能只生成便宜的齐次解

若 h 的 f_c 系数非零，除以该固定有理系数后可写为

\[
v=f_c+\alpha+\beta F+\gamma U.
\]

对 v 施加 `θ−k`，得到 g∈W，其 F、U 系数分别是

\[
r+\theta\beta+A\gamma-k\beta,
\qquad s+\beta+\theta\gamma+(B-k)\gamma.
\tag{6}
\]

若 g 有理，这两个系数必须为零，因为实际函数 1、F、U 独立。于是 (β,γ) 会解 forcing 为 (−r,−s) 的二维系统，违背上面的有理解排除。故 g 非有理。

现在对 g 应用 (5)，便得到

\[
F=D_hh+R_h,\qquad D_h\in\mathbf Q(w)[d/dw],\quad\operatorname{ord}D_h\le2,
\quad R_h\in\mathbf Q(w).
\tag{7}
\]

这不是仅对固定整数代表的试验，而是覆盖全部有理 α、β、γ 及每个固定有理 c。即使 c 假设恰等于 G，论证仍成立。

## 3. 有理微分运算的逐素数转移引理

**引理。** 设 H、Y 是 Q 系数原点正则芽，且

\[
Y=\sum_{j=0}^d a_j(w)H^{(j)}+R(w),\qquad a_j,R\in\mathbf Q(w).
\tag{8}
\]

存在有限素数集 S 和固定整数 K≥0，使对 p∉S：若 H 的 0 至 n+K 项系数均 p 整，则 Y 的第 n 项系数 p 整。

证明。将每个有理系数在原点写为有限阶 Laurent 芽。固定排除其多项式系数分母及原点非零分母首项的分子素因子后，它们的全部 Laurent 系数都 p 整：对分母多项式的形式逆作递推即可。R 也如此。设每个 a_j 的最低 Laurent 次数≥−s；Y 的第 n 项只使用 H 的至多 n+s+d 项，因为普通导数 j 次只把指标提高 j，并乘整数下降阶乘。取 K=s+d 的非负上界即可。Laurent 的负幂不影响此有限依赖范围，恒等式保证最终 Y 正则。

**必须区分的限制。** 固定有理乘子可以在有限坏素数处制造指数成本，例如 `1/(1−w/2)` 的 2 分母随 n 增长。因此本文并不声称所有固定有理运算保持实际总分母指数相等；引理只保持所有充分大好素数的早出现性质。这恰好足够推下界。

## 4. F 的早出现素数给出主命题

F 的第 n 项系数为

\[
\eta_n=\frac{16^n(2n)!(2n+1)!}{(4n+3)!}.
\]

对每个奇素数 p，取 `n_p=ceil((p−3)/4)`，则

\[
2n_p+1<p\le4n_p+3<2p,
\quad v_p(\eta_{n_p})=-1.
\tag{9}
\]

两项 numerator factorial 不含 p，denominator factorial 恰含一次；16 的幂是 p 单位，所以这里没有抵消。将第 2 节的恢复恒等式 (7) 代入第 3 节的引理，如果 h 的所有 0 至 n_p+K_h 项均 p 整，η_{n_p} 就会 p 整，与 (9) 矛盾。对充分大 p，h₀ 这个固定有理数本身 p 整，故坏项的位置实际≥1，得到 (1)。

对于共同前缀分母，所有充分大奇素数 `p≤4(N−K_h)+3` 都必须进入 δ_h(N)。除去有限集合不影响素数定理的主项，因此

\[
\log\delta_h(N)\ge4N+o(N).
\tag{10}
\]

这里不需要把恢复算子的坏素数成本估为小量，也没有从逐项门槛偷推必要条件。

## 5. n^e 无法供应过早出现的 p

设一个固定非有理 h 的正整数项系数满足精细类型

\[
h_m=\frac{a_m}{m^e\prod_{j=1}^r L(\lfloor b_jm+c_j\rfloor)},
\qquad a_m\in\mathbf Z,\quad e\in\mathbf N,
\tag{11}
\]

其中 `L(t)=lcm(1,…,max(1,t))`。允许先乘固定整数清有限初值及固定系数分母；这只增加有限坏素数集。e、r、b_j≥0 及 c_j 都固定。

如果每个 b_j<4，由 (1) 对每个充分大 p 选出有分母 p 的系数位置 m。此时 `m≤p/4+O_h(1)<p`，所以 `p∤m^e`；同时对所有 j 都有

\[
b_jm+c_j\le\frac{b_j}4p+O_{h,j}(1)<p.
\]

因此 (11) 的整个所标分母均 p 整，无法包含 p，与已选系数矛盾。故

\[
\max_j b_j\ge4,
\qquad \sigma:=\sum_jb_j\ge4.
\tag{12}
\]

这是精细阶梯的直接局部障碍；即使 e 任意大仍成立。常量 offset 不能改变它。相反，在改变坐标后若第一次有分母 p 的位置移到 `m≈p`，n^e 就可能承担该 p；本命题没有跨坐标不变性。

## 6. 原始 CDT 判据中的权重，以及本报告能排除什么

已核对 [CDT 原始主文，Theorem 2.5.1，pp.16–17](https://math.berkeley.edu/~ytang/L2chi.pdf)：基本版本使用 lcm 类型；`n^e` 的精细版本是其 [Theorem 6.0.2、Definition 6.0.1，pp.66–68](https://math.berkeley.edu/~ytang/L2chi.pdf)，不是基本定理本身。对应 arXiv 原始版本为 [2408.15403v2](https://arxiv.org/abs/2408.15403v2)。这些判据按函数行分配嵌套的 lcm 层，并用

\[
\tau^\flat(\mathbf b)=\frac1{m^2}\sum_{i=1}^m(2i-1)\sigma_i,
\qquad
\tau(\mathbf b;\mathbf e)=\tau^\flat(\mathbf b)+\tau^\sharp(\mathbf e)
\tag{13}
\]

作预算；这里 `σ_i=Σ_jb_{i,j}`。精细积分成本为

\[
\tau^\sharp(\mathbf e)=\frac2{m^2}\min_{0\le\xi\le m}
\left[\xi\sum_i e_i+(\max_i e_i)I^m_\xi(\xi)\right]\ge0,
\tag{14}
\]

非负性直接来自 Definition 6.0.1 的非负积分。固定 `b n+c` offset 由主文 Remark 6.0.12 允许。已知 holonomic 时，应用所需的最大解析映射导数仍须满足 `log|φ′(0)|>τ(b;e)`；改善分子中的积分不会免除这个前提。

现在取 V_c 中任意 `m≥2` 个 Q(w) 独立的原点正则函数，以及任意满足上述精细类型的分母表。因为有理函数都位于同一个 Q(w) 一维子空间，至多一行可以是有理函数，其余每一行都由 (12) 强制 σ_i≥4。无论把可能的有理行放在哪里，最小加权成本只能在把它放到权重最小的第一行时取得，因此

\[
\tau^\flat(\mathbf b)\ge4\left(1-\frac1{m^2}\right).
\tag{15}
\]

|独立函数数 m|必要 τ♭ 下界|
|---|---|
|2|3|
|3|32/9|
|4|15/4|

整个 V_c 的 m 不超过 4。若 m=1 且该行非有理，则直接有 τ♭≥4；单独一行有理函数不能承担目标无理性的矛盾证明。

在当前单值域 `D=C∖[1,∞)`，任何圆盘到 D 的正则映射满足 `φ(0)=0` 时都有 `|φ′(0)|≤4`，由标准映射 `ψ(v)=4v/(1+v)²` 和 Schwarz 引理得到。故 (15) 对所有 m=2、3、4 都严格超过 `log4`；(14) 只会增加总成本。

**因此本文已排除以下完整且有限的范围：在旧 w 变量，选择 V_c 内任意固定有理基、任意固定阶微分组合，给它们分配 CDT Theorem 2.5.1 / 6.0.2 的任意固定 `n^e` 与嵌套 lcm 类型，而所有解析映射的像均留在 D 的方案，无法满足这两个定理的正预算前提。** 此处是针对精细类型的证明，强于只报告 scalar 指数≥4。

没有因此排除整个 arithmetic holonomy 方法。特别是允许解析映射越过 slit 并在拉回后才单值、代数覆盖改变原点参数、另增实际独立的函数、重新计算覆盖后的整数结构或发展更细的素数分布预算，都不属于本命题。

## 7. 可以确定的真实分母类型

F 和 U 的前缀分母指数恰为 4。F 的有限共同分母是 system 报告已经证明的 `2O_(4N+3)`；U 的上界相同，非有理性与 (10) 给下界。更一般地，若固定 P、Q、T 的 Taylor 系数被一个固定整数同时清分母，则每个非有理 `T+PF+QU` 都有指数恰为 4：乘法卷积给上界 `D·2O_(4N+3)`，(10) 给下界。固定有理系数多项式组合属于这一范围。

若 P、Q、T 有有限阶原点极点，可先乘固定 w 幂；若乘子在固定坏素数处有逐项增长的分母，则只保留下界，不能声称恰为 4。

f_c 方向仍只有已经严格证明的区间

\[
4\le\liminf\frac{\log\delta_{f_c}(N)}N
\le\limsup\frac{\log\delta_{f_c}(N)}N\le5.
\]

其逐项安全类型可以取 `(b,e)=(4+1,0)`；F、U 则取 `(4,0)`，允许常量 offset 及固定整数归一化。因而已有自然四行表

\[
\mathbf b=\begin{pmatrix}0&0\\4&0\\4&0\\4&1\end{pmatrix},\qquad
\mathbf e=0,
\quad\tau^\flat=\frac{67}{16}.
\]

即使 f_c 的第二个 lcm 层可以完全消去，本报告仍给任何固定基的下界 15/4；旧坐标中改善 5 到 4 不会单独恢复正预算。本报告没有证明任意含 f_c 组合的最优上指数恰为 4 或 5。

## 8. 后续需要的新输入

这个结果把原来的缺口缩小为明确的坐标与整数结构问题：对新的代数覆盖或周期系统，需要重新证明其真实函数独立性、逐项分母类型，以及每个素数首次出现的指标。不能把旧 w 的 (1) 强行运输成覆盖后相同的 `p/4` 指标。

若覆盖后能使相关原函数成为有理系数的积分、其分母仅由 n^e 支付，应直接用 (14) 计算新的 τ♯，再与覆盖后可合法延拓的解析映射比较；原函数空间的实际秩也必须重新核查。另一方面，如果计划依靠参数相关的系数 content，则需要真正的整数理想或局部抵消证书，本报告的固定 Q(w) 运算不会替代它。

本轮没有参数扫描。[精确符号脚本](E:/kimi-build/zeta5/research/odd_zeta_staircase_catalan_20261004_verify.py) 与 [JSON 证书](E:/kimi-build/zeta5/research/odd_zeta_staircase_catalan_20261004_verify.json) 核对了通用恢复矩阵、Riccati 符号、商方向 forcing 及有理权重；它们不代替本文的全素数论证。本文 §§2–7 已经 paper_mechanism 只读独立审阅通过。

证明使用旧报告已经独立审计的实际函数独立性与有理特解排除，并给出了覆盖所有固定有理组合的逐素数必要条件；没有得到 G 或 ζ(7) 无理性的证明。
