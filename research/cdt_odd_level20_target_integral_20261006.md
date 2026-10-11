# level20 的真实目标积分：actual rank5、共同解析叶与新算术接口

日期：2026-10-06。本文新建，不改冻结稿。已经闭合的正输入是一个真实 target 积分的实际 rank5、同一共同解析 cover 及完整分母类型；加到已证纯背景 P10 时得到实际 rank14。尚未证明它提供额外的第三层或第四层 Smith 增益。提高矩阵的统一 p 缩放会提高旧行的基线，不能把该变化直接记作新收益。

## 1. 必须在原点正规化的真实积分

使用 [真实周期](cdt_odd_conjugate_projection_20261005.md)、[完整模型](cdt_odd_level20_model_20261006.md) 与 [共同叶](cdt_odd_level20_leaf_20261006.md)。固定 H=H₋，反证假设 L(3,χ₅)∈Q；因此 H 的系数在 K=Q(√5) 中，H₀:=H(0)=Θ/5∈K，通常非零。

直接 ∫H(t)dt/t 含 H₀logt，不是原点全纯函数。本文取实际规范芽

\[
\boxed{I_H(t)=\int_0^t\frac{H(v)-H_0}{v}\,dv,
\qquad I_H(0)=0,\quad\vartheta I_H=H-H_0.}
\tag{I1}
\]

这里 \(\vartheta=t\partial_t\)。积分核与常数项都由实际 H 决定，未添加新的数值有理性假设。

## 2. 完整 rank5 connection 与实际 rank 下界

原模型给 \(\partial^3H+a_2\partial^2H+a_1\partial H+a_0H=U\)。定义 Euler coefficients

\[
B_2=ta_2-3,\quad B_1=2-ta_2+t^2a_1,
\quad B_0=t^3a_0,\quad F=t^3U.
\]

则

\[
\mathcal L_EH:=\{\vartheta^3+B_2\vartheta^2+B_1\vartheta+B_0\}H=F,
\tag{I2}
\]

且 Bᵢ、F 属于 K(t)。完整五维系统可用 (1,I_H,H,ϑH,ϑ²H)；导数分别为

\[
0,\quad H-H_0,\quad\vartheta H,\quad\vartheta^2H,
\quad F-B_0H-B_1\vartheta H-B_2\vartheta^2H.
\tag{I3}
\]

故实际函数模 W_new:=W_old+K(t)I_H 的 rank≤5，其中 W_old=span(1,H,ϑH,ϑ²H) 已证 rank4。等价地，I_H 满足真实四阶非齐次方程

\[
\mathcal L_E\vartheta I_H=F-H_0B_0.
\tag{I4}
\]

本文的 connection 和 rank 使用上面的原函数基；实际 CDT 整数 source 沿用既有 pole-clearing gauge \(g=\Delta^2\)，其 species 是 \((1,I_H,gH,g\vartheta H,g\vartheta^2H)\)。I_H 不乘 g。固定 polynomial gauge 不改变函数模与实际 rank，已有 target 的分母和局部行按旧稿保留；下文的 source kernel 明确使用这三个 g-target blocks。

上界不能自行当成等号。真正下界来自 [模型 §6](cdt_odd_level20_model_20261006.md) 已证的未消 cusp t=∞：H 的最高 log(t)³ 项系数为 −17/120，且与 Θ 无关。由 (I1)，I_H 的最高项为

\[
\boxed{-\frac{17}{480}\log(t)^4.}
\tag{I5}
\]

减去 H₀只影响一次对数项，不能消去 (I5)。在该 cusp 取消去有限字符的共同 monodromy 幂；I_H 的四次 monodromy 差非零，而第五次差为零。五个 translates 独立，所以任何齐次有理微分方程的阶至少5。结合 (I3)，

\[
\boxed{\dim_{K(t)}W_{new}=5,
\qquad W_{new}/W_{old}\simeq\mathbf1.}
\tag{I6}
\]

最后的 trivial quotient 来自 ϑI_H∈W_old。I_H 的实际 cyclic rank 也是5；这里确有新函数方向，并非形式上多列一个积分。

## 3. 与已有纯背景的交仍只有常数

设 B 是一个已证的实际纯背景微分模，包含1，并且 W_old∩B=K(t)·1。要求其在 t=∞ 的局部 monodromy quasi-unipotent；已有 P10 满足。令 X=W_new∩B。

由 (I6)，X/(X∩W_old) 嵌入一维 trivial quotient，且 X∩W_old=K(t)·1。所以 dimX≤2。若 dimX=2，维数公式给 W_new=W_old+X。取使两者局部 monodromy 都 unipotent 的共同幂，记其 logarithm 为 N。这里 N 作用在对应 connection 的 horizontal fiber（或统一取对偶），不是把 K(t)-函数模直接当成 C-解空间。W_old rank4 使 N⁴=0，X rank2 使 N²=0；二者之和于是仍被 N⁴杀掉。这与 (I5) 的 N⁴≠0 矛盾。因此

\[
\boxed{W_{new}\cap B=K(t)\cdot1.}
\tag{I7}
\]

已有 [低成本纯系统](cdt_odd_low_cost_polylog_20261006.md) 的 P10 是实际 rank10、由有限字符的一维模迭代扩张组成。W_old 的非恒定 quotient 是 Zariski-dense SL₂ 的不可约 Sym² twist，不能嵌入该 solvable 背景；所以其旧交为常数。把 (I7) 用于 P10，得到

\[
\boxed{\dim(P10+W_{new})=10+5-1=14.}
\tag{I8}
\]

此 argument 使用 actual modules、quotient 与局部 monodromy，不以“新增一个积分”替代独立性证明。

## 4. 同一个全 disk 共同叶

[共同叶 §8](cdt_odd_level20_leaf_20261006.md) 已证 G=⟨T,W₂₀⟩ 的 coarse surface 在填入唯一 cusp 后是 disk，并给出 H 的实际全纯下降与 t 的下降；内部 t 没有∞或1，唯一零点是填入的 cusp，且是 simple zero。

在该填充 disk 上，\((H-H_0)\,dt/t\) 全纯：唯一 t=0 处由正规化消去极点；其它内部点没有新的极点。Fricke elliptic 点处也用 coarse 坐标的全纯下降，不能仅用未下降的 τ 原始值。disk simply connected，故该一形式有唯一取值 I_H(0)=0 的全局全纯 primitive。

因此 I_H 在此前同一个共同 cover 上全纯；所有导数由 (I3) 闭合。此结论不为解析端增加 capacity，沿用当前真实 cover。它并未把 boundary 的 t=1、∞ 或其它 cusp 奇点删除。

## 5. 全分母：精确的 added-integration 类型

设 \(D_n=\operatorname{lcm}(1,\ldots,n)\)，\(D_0=1\)。真实 q-series 和整数互逆 t↔q 已证，存在一个与 n 无关的整数 C₀，使 H=Σh_ntⁿ 满足 C₀D_n³h_n∈O_K。由 (I1)，

\[
I_H=\sum_{n\ge1}\frac{h_n}{n}t^n,
\qquad\boxed{C_0\,nD_n^3[t^n]I_H\in O_K.}
\tag{I9}
\]

因此其真实类型是三条 unit LCM columns 加一个 integration index n，e=1。不能把它无偿并入 e=0 balanced Smith 稿；第八节的序号因子与 fine transport 须重新接合。

对好 p、前缀 n<N≤p²，p⁴I_H integral；p³H、p³ϑH、p³ϑ²H integral。这里只是前缀整性，不能说 p⁴I_H 的无界全级数全局 integral。

## 6. primitive 来源与尚未闭合的混合 Cartier 接口

记在上述前缀中的 Z=p⁴I_H、Y=p³H。则

\[
\vartheta Z=pY-p^4H_0,
\quad\vartheta^2Z=p\vartheta Y,
\quad\vartheta^3Z=p\vartheta^2Y.
\tag{I10}
\]

旧两层 L₂Y∈p² 给 L₂ϑZ∈p³（固定常数项乘 p⁴ 不影响）。它看似是一个 order3 S3 行，但清固定 g 后转回实际五种 species，I_H 的坐标为0；其余三个 g-target rows 的 p⁴评价本来就比旧 p³评价多一层。这是**旧 target 方向的 baseline shift**，不能记为新增 primitive 第三层收益。

更严格地，\(Z\bmod p\in k[t^p]/(t^N)\)。以下首项与 kernel 判断明确取 \(p<N\le p^2\)，使首阶 p 进入实际前缀；N≤p 时 Z 的 reduction 为零，不适用该判断。对 p≠109 及旧有限坏素数，其首阶恰为 p：令 κ=5√5/4，已有最高 packet 首项给

\[
\boxed{[t^p]Z\equiv-\frac{1-\kappa\chi(p)}5\pmod{\mathfrak p},
\quad N_{K/\mathbf Q}(1-\kappa\chi(p))=-109/16\ne0.}
\tag{I11}
\]

这是 q 的首个最高层经整数 t↔q 互逆得到的实际系数；未进行素数搜索。

在 pure p⁴ matrix 的五种 species 中，constant、三个 H blocks 的像均在p中。若 polynomial row（各坐标 degree≤D）在**完整前缀** tᴺ上有 S≥1，则 modp只剩 c_I(t)Z。因此

\[
c_I Z=0\pmod{p,t^N}\ \Longrightarrow\
t^{N-p}\mid\bar c_I.
\tag{I12}
\]

在 D<N−p 的窗口中，必 \(\bar c_I=0\)。例如实际 rank5 leading cutoff 可取 N≥5(D+1)，p≤D 的主窗口满足此条件。这是对完整 prefix polynomial kernel 的结论；不能自动拿它排除只取若干 leading rows 的 kernel。

由此可见真正新方向可能有 c_I=p·d(t)，其 H 坐标 modp非零。在第二层比较中，需要实际关系

\[
d(t)(Z\bmod p)+\sum_{j=0}^2 c_j(t)(g\vartheta^jY\bmod p)=0
\tag{I13}
\]

并进一步控制 lift 到更高 p 层后的误差、primitive content 与 polynomial degree。这涉及正规目标积分的真实 Cartier primitive packet；目前未证明 (I13) 存在 degree O(p) 的新增独立行。I_H 不能自动写成另一个单 prefactor·W(s) 然后套 universal order3。新增 actual rank14、完整整性与共同 leaf 已经成立，新增 Smith 收益和 e=1 全局 budget 仍待证明。

## 7. 核验范围

[最小 symbolic 脚本](cdt_odd_level20_target_integral_20261006_verify.py) 与 [证书](cdt_odd_level20_target_integral_20261006_verify.json) 只核 Euler 转换、正规积分形式、log⁴ 系数和最高 packet 的固定代数范数。实际 rank、交模、共同解析域与全分母来自上面的全尺度论证。未扫描参数或素数，未重跑冻结 producer；没有得到新的数值无理性定理。
