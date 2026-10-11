# BB 八维系统的固定有理 gauge：全素数 packet 定理

日期：2026-10-04。本独立附录保持 [自然 fine 报告](E:/kimi-build/zeta5/research/odd_zeta_bb_fine_budget_20261004.md) 冻结。**状态：完整全尺度证明已由 root 与 zeta7_distribution_new 分别只读独立审阅通过。** 原坐标仍是 z，不处理代数覆盖或 N 依赖的变换。

## 1. 空间、过滤与可证明的目标

固定 c∈Q，在已经认证的实际函数空间中取

\[
W_5=\mathbf Q(z)\operatorname{span}\{1,L_1,L_2,L_3,L_4\},\quad
W_7=W_5+\mathbf Q(z)U+\mathbf Q(z)V,
\]

\[
W_8=W_7+\mathbf Q(z)f_c.
\]

实际秩分别为 5、7、8，来自 [冻结的真实周期系统报告](E:/kimi-build/zeta5/research/odd_zeta_new_period_systems_20261004.md) 的函数独立证明，完全不预设 ζ(7) 的无理性。

已证结论是：每个固定原点正则 h∈W₈ 若不属于 W₇，则任何固定 n^e / lcm 类型都必须有 σ_h≥7；若 h∉W₅，则必须有 σ_h≥4。这使自然 fine 报告的 201/64 下界保持于 W₈ 的全部固定 Q(z) 基，而不是只保持自然八行。

关键改进是使用所有固定 offset 的 packet，而不只使用 n=p+1。确实 `(θ−1)^7` 会清掉自然函数在 p+1 的见证；单个 offset 不能证明 gauge 不变性。

## 2. 有限坏素数与 Laurent 卷积

任意固定 a(z)∈Q(z) 在 0 是有限负部的 Laurent 级数。排除其多项式系数分母及分母非零首项的分子素因子后，其全部 Laurent 系数都 p 整：形式逆递推即可证明。因此给定一个固定组合 h，只需删除有限素数集，使所有乘子的系数、固定 c 及下文选定的非零有理数均 p 整。

每个乘子的最低 Laurent 指数固定，记其总下界为 −B。h 的第 p+r 项只能使用原函数的至多 p+r+B 项。虽然卷积中包含许多低于 p 的指标，所有在 p 之前的低赋值项在乘足够高的 p 幂后都归零；真正保留的 p+j 项仅有固定范围 `−B≤j≤r+B`。因此下文不存在依赖 p 的无限 packet 求和。

允许 h 的表达式在 0 各有有限极点而相互抵消；h 本身要求正则以使用 CDT formal function 条件。选择固定 r 后，p 足够大也保证 p+r≥1。

## 3. f_c 方向的七阶 packet

对每个固定整数 j，所有充分大好奇素数 p 满足

\[
p^7[z^{p+j}]f_c\equiv
\begin{cases}-\frac52 C_j&j\ge0,\\0&j<0,\end{cases}
\pmod p,
\quad C_j=\binom{2j}{j}.
\tag{1}
\]

这里表达式在乘 p⁷ 后 p 整。证明：j<0 时，t_k 的求和没有 t_p，所有 k≤p+j 的赋值至少 −1，因此归零。j≥0 时，t_p 是唯一 −7 项；其他 k<p 至少 −1，`p<k≤p+j` 至少 −4，对固定 j 与足够大 p，C_k 是单位。p^7t_p≡1/C_p；Lucas 给 C_p≡2、C_(p+j)≡2C_j。因此

\[
p^7d_{p+j}\equiv-\frac52\frac{C_{p+j}}{C_p}
\equiv-\frac52C_j.
\]

在所有指标 n≤p+固定常数中，W₇ 的各原函数系数赋值都至少 −6：V 在 n=p 是 −6，U 至少 −5，L_j 至少 −j，其他近 p 位置的谐波项至多 −4。原点有理函数的好素数系数全部整。所以这些 lower terms 在 p⁷ packet 中全灭。

取 `h=P(z)f_c+lower`，P∈Q(z) 非零。由上一节的 Laurent 卷积，固定 r 处有

\[
p^7[z^{p+r}]h\equiv-\frac52[z^r]P(z)b(z)\pmod p,
\quad b(z)=(1-4z)^{-1/2}.
\tag{2}
\]

b 非有理，非零有理 P 的乘积 Pb 也非有理。若 Pb 没有任何正 Laurent 系数，它就是有限 Laurent 多项式，会为有理函数；矛盾。因此存在固定正整数 r，使 `(Pb)_r≠0`。再排除这个固定有理系数的分子分母素数及 r 的素因子，(2) 给

\[
v_p([z^{p+r}]h)=-7,
\quad p\nmid p+r.
\tag{3}
\]

注意没有使用 r=0 的系数；r>0 确保 n^e 不能供应 p。每个 lcm endpoint 为 O(p)<p²，故 (3) 仍强制至少七个 b≥1 的活动层，σ_h≥7。特别是该方向的实际公共前缀分母下指数至少 7，但固定坏素数可另外增加指数，本文不声称所有 gauge 的上指数也为 7。

## 4. U、V 商方向：最高两层的单点 packet

写 `h=P(z)V+Q(z)U+Σ_(j=1)^4R_j(z)L_j+R_0(z)`，且 P、Q 不同时为零。对于任意固定整数 j，

\[
p^6[z^{p+j}]V\equiv-\delta_{j,0}\pmod p,
\quad p^6[z^{p+j}]U\equiv0\pmod p.
\tag{4}
\]

若 j≠0，系数序号为 p 单位；j<0 时全部谐波项 p 整，j>0 时 H_(p+j−1)^(4) 的最低层为 −4，所以乘 p⁶ 归零。j=0 时 V 的纯 p^−6 项给 −1，U 的最高分母只有 p⁵。低 L_j 的最高分母是 p⁴，故也归零。

若 P 不是常数，其 Laurent 级数有某个固定 `r≠0` 的非零系数 P_r；由 (4) 与有限坏素数处理，有

\[
p^6[z^{p+r}]h\equiv-P_r\not\equiv0\pmod p.
\]

故该方向在与 p 互素的指标处有精确 −6 层，强制 σ_h≥6≥4。r 可以为负；固定负 r 并不造成问题，充分大 p 时 p+r 为正，且排除 r 的有限素因子后仍与 p 互素。

若 P 是常数，取 r≠0 时它不会把 V 的 n=p 纯项移到 p+r。此时

\[
p^5[z^{p+j}]U\equiv-\delta_{j,0}\pmod p,
\]

而 P V、低 L_j 在 j≠0 的 p⁵ packet 中归零。若 Q 不是常数，选择非零的 Q_r、r≠0，得到精确 −5 层，故 σ_h≥5≥4。

## 5. 两系数均常数时，L₄ 的全部 shift 也不能消掉尾 packet

剩下 P、Q 是常数且不同时为零。对固定 r>0，U、V 的第 p+r 项在 p⁴ 层分别给

\[
p^4u_{p+r}\equiv-5\frac{(-1)^r}{r},\qquad
p^4v_{p+r}\equiv-5\frac{(-1)^r}{r^2}.
\tag{5}
\]

这是 H_(p+r−1)^(4) 中唯一 p^−4 项的贡献；n=p+r 是单位。L₄ 在 p⁴ packet 中只有 n=p 的纯项，值 −1；R₄ 的所有 Laurent shifts 因而贡献 `−(R₄)_r`。低 L₁、L₂、L₃ 与有理项归零。得到

\[
p^4[z^{p+r}]h\equiv[z^r]\Psi(z)\pmod p,
\]

\[
\Psi(z)=-5\bigl(P L_2(z)+Q L_1(z)\bigr)-R_4(z).
\tag{6}
\]

由于 1、L₁、L₂ 在 C(z) 上实际独立，P、Q 不同时为零时 Ψ 非有理。若其所有正 Laurent 系数都为零，它为有限 Laurent 多项式，矛盾。因此选定某固定 r>0，使 Ψ_r≠0，再删除其分子分母和 r 的有限素因子，便得到

\[
v_p([z^{p+r}]h)=-4,
\quad p\nmid p+r.
\tag{7}
\]

所以全部 W₇\W₅ 固定有理组合都有 σ_h≥4。这里显式包含 R₄ 的全部卷积，未以“低函数分母不重要”略去它。

## 6. 任意固定八行 gauge 与携带商方向的子族

以上全尺度 packet 推出以下过滤维数结论。任意 W₈ 的八个 Q(z) 独立基，至少三行不属于 W₅，否则在商 W₈/W₅ 的像不能张成秩 3；至少一行不属于 W₇，否则不能张成秩 1 商。由 §§3–5，至少三行 σ≥4，且至少一行 σ≥7。

CDT 嵌套 lcm 列使行和非递减，所以任意合法行排序均有 `σ₆≥4,σ₇≥4,σ₈≥7`。因此其平坦成本仍至少为 201/64，任何 n^e 成本非负。若全部解析映射的像仍限制在旧 U₁ slit 域，log|φ′(0)|≤log4，正预算仍不成立。

**子族推论。** 更一般地，取 W₈ 中任意 `1≤m≤8` 个固定 Q(z) 独立的正则函数，只要其中至少一个 h∉W₇，则由第 3 节 σ_h≥7。合法嵌套表的最后行因此必须满足 σ_m≥7，从而

\[
\tau^\flat\ge\frac{7(2m-1)}{m^2}
\ge\frac{105}{64}>\log4.
\tag{8}
\]

第二个不等式来自 `(2m−1)/m²` 在正整数 m≥1 上非递增，最小允许值在 m=8；可直接比较相邻两项。故任何包含这个商方向的固定独立子族也不能靠减少函数数目恢复旧域正预算。这仅是上述数学子族条件，不扩展成对所有无理性证明方式的排除。

这仅是旧 z 坐标、固定 Q(z) 基变换、该已认证函数空间、固定有限 n^e / lcm 型及映入旧 U₁ 模板的结论。它不排除代数覆盖、扩张函数空间、N 依赖 gauge、不同整数评价模块或在 slit 之外经拉回单值的模板。

**具体排错例。** 对 h=(θ−1)^7 f_c，p+1 项的 −7 层被清掉，但

\[
p^7h_{p+2}\equiv-\frac52(2-1)^7 C_2=-15\pmod p
\]

仍给所有充分大 p 的 −7 层。使用 packet 的意义是移动到未被固定算子杀掉的某一个 offset，而不是假定 p+1 见证本身不变。

作为第二个抵消例，`h=U+V+10zL₄` 的 p+1 项的 p⁴ packet 为 0，但 p+2 项仍是 `−15/4 mod p`。这显式包含低 L₄ 的移位抵消。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_bb_fixed_gauge_packet_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_bb_fixed_gauge_packet_20261004_verify.json) 仅检查上面两个固定例在指定 p=11、13 的模身份和赋值，全部通过；不做参数或素数搜索，也不代替全尺度证明。root 与 zeta7_distribution_new 的独立审阅覆盖有限坏素数、r<0/r=0、Laurent 依赖范围、低 L₄ 的全部卷积及维数过滤。自然报告的主文件未因本附录扩范围而修改。

没有得到 ζ(7) 无理性的证明。
