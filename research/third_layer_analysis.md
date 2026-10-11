# ζ(7)：第二次配对的统一公式与六极点窗口第三层界

本轮在前两轮的统一引理基础上，补出局部 Hermite 分解和第二次配对公式，得到此前的完整窗口目标：

\[
\boxed{v_p^G\Delta(\delta,X)\ge48N-24p+22+a-b,\qquad
b=\max(0,\min(a,2d-a)),\quad d=3N-p+1.}\tag{1}
\]

这是统一书面推导，附精确有限证书，尚未 Lean 形式化。**ζ(7) 无理性仍未证明。** 完成的是一个特定素数窗口内的算术下界；全局算术常数和实侧比较还需在同一参数下重新计算。

本报告日期：2026-09-29。此前接口见 [two_sided_analysis.md](two_sided_analysis.md)、[normalization_hensel_analysis.md](normalization_hensel_analysis.md)；矩泛函的精确 Taylor 分布公式见 [distribution_analysis.md](distribution_analysis.md)。

**后续更新：** [global_envelope_analysis.md](global_envelope_analysis.md) 已完成本报告末尾提出的同参数全局接入，包含一般 α 的局部收益公式、完整算术包络与实侧下界的严格区间比较，以及最高次系数给出的窗口收益上限。本报告以下保留局部证明完成时的记录；全局比较没有闭合 ζ(7) 无理性证明。

## 1. 参数、归一化与待证明接口

仍取素数 p≥11，

\[
\lceil p/3\rceil\le N\le\lfloor3p/8\rfloor,\quad 0\le a\le N,
\quad K=3p-1-a,\quad h=K-N,
\]
\[
m=(p-1)/2,\quad D_j=\prod_{c=1}^j(t+c^2),\quad F=D_m,
\quad J=D_N/D_a,\quad n=N-a+d.
\]

沿用 CRT 基 E、固定权 u,v，以及整矩阵

\[
M=P_u^{-1}GP_v^{-1},\qquad
G(P,Q)=\mu_{\delta,X}(D_N^8PQ/D_K),\qquad
\tau_0=\sum u+\sum v=38N-21p+19+2a.
\]

令 \(H=129/128+\delta\)。在 p 的 Gauss DVR 上运算，剩余域取 \(k=\mathbb F_p(\delta,X)\)。归一化 X 系数至少含 p⁵，因此本报告涉及的前三层模 p 计算不依赖 X。

已知第一层显式方向是

\[
\Phi=t^2F^8/D_N^5,\quad q_R=\Phi R,\quad\deg R<n.
\]

它们对应的归一化坐标 Z 模 p 独立，MZ 至少含 p。此前第一次配对的根空间已经识别为 J 的倍数。因此本轮从

\[
\Phi_2=\Phi J=\frac{t^2F^8}{D_N^4D_a},\qquad\deg U<d
\]

出发，证明真正的二阶提升存在，并计算其第二次配对。

## 2. 消去局部块后，剩余矩阵严格对称

取上一报告的

\[
S=\{c>N,\ i<4\}\cup\{a<c\le N,\ i<3\},\qquad R=S^c.
\]

\(M_{SS}\) 在 Gauss DVR 上可逆。记

\[
A=M_{RR}-M_{RS}M_{SS}^{-1}M_{SR}.\tag{2}
\]

对于 R 中的每个指标，均有 \(u_i-v_i=1\)。又有
\(M^T=\Lambda M\Lambda^{-1}\)，\(\Lambda=\operatorname{diag}(p^{u_i-v_i})\)。对加权对称矩阵作 Schur 消元后，剩余权为 \(\Lambda_R=pI\)，所以

\[
\boxed{A=A^T,\qquad\bar A=\overline{M_{RR}}.}\tag{3}
\]

第二个等式用到了 \(\overline{M_{SR}}=0\)。A 的阶数为 \(r=p+1+2a\)。令 B 为 Z 的 R 行，仍有 \(\bar B\) 秩 n、AB∈pO。

R 上对应的物理多项式基为 \(q_i=p^{-v_i}E_i\)，且
\(M_{ij}=G(q_i,q_j)/p\)。这个表示将 \(\bar A\) 的分析化为双线性泛函的局部 Taylor 计算。

## 3. 用 Hermite 插值识别完整第一层核

### 3.1 可见多项式与插值数据

R 中 v=0 的坐标共有 2N+1 个：原点高坐标、所有内类 i≥2 的存留坐标。它们的模 p 多项式恰好组成

\[
\chi(t)\,k[t]_{<2N+1},\qquad
\chi=\frac{tF^6}{D_N^3D_a}.
\tag{4}
\]

这里及下文的多项式局部恒等式在 k[t] 中理解。证明是 CRT 基因子计数：原点最小重数 1，截短内类最小重数 2，完整内类最小重数 3，外类最小重数 6。χ 的次数为 \(h-(2N+1)\)，所以维数也吻合。

其余“隐藏”坐标为：原点低坐标 1 个；每个截短内类低坐标 2 个；每个外类高坐标 2 个。它们的物理多项式带 p 或 p²，不能从模 p 多项式中读出，必须保留。

对可见多项式 \(q=\chi V\)，使用以下插值数据：

- 原点：V(0)；
- 截短内类 1≤c≤a：V(−c²)；
- 外类 N<c≤m：V(−c²)、V′(−c²)。

数据数目为

\[
s=1+a+2(m-N)=p-2N+a\le2N+1.
\]

节点互异，故 Hermite 取值映射满射。其核为

\[
T(t)\,k[t]_{<n},\qquad
T=tD_a(F/D_N)^2,
\]

而 \(\chi T=\Phi\)。因此，如果隐藏坐标与这些插值数据上的配对非退化，那么整个核就恰好是 B。

### 3.2 局部化所用的精度

对整系数商多项式 Q，置 f(x)=x⁷Q(−x²)，\(S_j=[u^j]f(u)+2\sum_{c=1}^m[u^j]f(c+u)\)。已有公式给出

\[
\mu(Q)\equiv S_5/(6p)-S_6/2+7pS_7/12\pmod {p^3}.
\tag{5}
\]

外类的六个实际移位因子满足单点公式

\[
f(c+u)=\prod_{j=-3}^{2}(u-jp)A_c(u)
\quad\Longrightarrow\quad
\frac{\mu_c(f)}p\equiv-\frac72 A_c'(0)\pmod p.
\tag{6}
\]

此处 μ_c 已包括非零节点在 S_j 中的系数 2。不同非零类的留数在另一类处有单位分母；在当前阶数，其贡献消失。原点留数在其他非零节点处留下的全局常数和需另行计算，已计入下述原点块。

由 (5)—(6)，\(\bar A\) 只依赖各类的上述插值数据及本类隐藏坐标。完整内类剩余多项式有三重零点，其自身留数至少达到 G 的 p² 阶，故在 G/p 模 p 中不再留下局部块。于是 Hermite 插值把 \(\bar A\) 分成下面互不耦合的小块，以及 n 维零块。

### 3.3 截短内类的三阶块

在 c≤a 处用 \(z=(t+c^2)/(2cp)\)。分母只有五个节点

\[
\mathcal Z_5=\{0,1,-1,-2,2\},\quad
w_{-1}=w_2=1,\quad w_{-2}=H.
\]

定义

\[
C_j^{(5)}=\sum_{z\in\{-1,2,-2\}}
\frac{w_z z^j}{\prod_{y\in\mathcal Z_5\setminus\{z\}}(z-y)},\qquad
S_j^{(5)}=\sum_{z\in\mathcal Z_5}
\frac{z^j}{\prod_{y\ne z}(z-y)},
\]
\[
T_j=C_{8+j}^{(5)}+S_{j+2}^{(5)}/6+S_{j+1}^{(5)}/2+7S_j^{(5)}/12.
\tag{7}
\]

两个隐藏坐标和一个取值坐标，经单位缩放后给出

\[
\mathsf T=(T_{i+j})_{0\le i,j<3},\qquad
\boxed{\det\mathsf T=-\frac{1122304H-529}{432}.}\tag{8}
\]

这个计算直接来自局部物理多项式的三个首项 \(p^2,\ p(t+c^2),\ (t+c^2)^2\)。共同单位及 \((2c)^i\) 的行列缩放不影响秩。小节点 z=0 的直接 Taylor 项与留数展开中的缺项按上一报告相同方式补偿，故 (7) 使用全五节点的 S_j。

精确矩为

\[
\begin{aligned}
T_0&=(64H+63)/6,&T_1&=(-128H+129)/6,\\
T_2&=128(H+1)/3,&T_3&=(-256H+258)/3,\\
T_4&=(2048H+2063)/12,&T_5&=(-1024H+1032)/3,\\
T_6&=(8192H+8267)/12.
\end{aligned}
\tag{9}
\]

### 3.4 原点的二阶块

设 E₀ 是零类低基，局部使用 \(p^2E_0\) 与 \((t+4p^2)E_0\)。除去共同单位以及可见坐标的单位缩放，原点块为

\[
\mathsf Z=
\begin{pmatrix}(256H-3)/12&-2/3\\-2/3&-17/12\end{pmatrix},
\quad
\boxed{\det\mathsf Z=-\frac{4352H+13}{144}.}\tag{10}
\]

这里有两个不可遗漏的项。

第一，原点极点泛函的首项分别是
\(p^{-1}(-1+1/2)\) 和 \(p^{-1}(-64H+1/4)\)，来自 \(-j^6H_j^{(7)}+1/(2j)\)。不能仅保留调和数。

第二，若 \(L(t)=D_N(t)^7E_0(t)\)，首一除法得到的商满足

\[
p\mu\!\left(\left\lfloor\frac{L(t)}{t+p^2}\right\rfloor\right)
\equiv-L(0)/6\pmod p.
\]

原因是非零节点处 \(x^7L(-x^2)/(-x^2)\) 的第五阶项由已知零点消失，而减去的极点在这些节点贡献 x⁵；加权节点数为 p−1。原点的第五阶商系数则为零。这给出混合项 −1/6；高—高商项为 \(7/12-3/6=1/12\)。加上极点部分，正好得到 (10)。其他类的插值数据为零时，外区六零点项也为零，因此这是独立的原点块。

### 3.5 外类的四阶块

每个外类使用两个隐藏坐标 i=4,5，以及 V(−c²)、V′(−c²)。块具有形状

\[
\mathsf O_c=\begin{pmatrix}0&C_c\\C_c^T&D_c\end{pmatrix},\qquad
C_c=\begin{pmatrix}*&u_c\\v_c&0\end{pmatrix},\quad
D_c=\begin{pmatrix}*&*\\*&0\end{pmatrix},\qquad u_cv_c\ne0.
\tag{11}
\]

验证要点：两个隐藏物理多项式各含 p²，因此它们互相配对在此层为零。一个隐藏与一个可见多项式配对，只需 pμ 的首项 S₅/6；本类局部因子分别为 \((t+c^2)^4\)、\((t+c^2)^5\)。第一行于是涉及取值和一阶导数，第二行只涉及取值。其两个交叉首系数分别为 −32c⁵/3 乘以单位，因此非零。其他类至少六重零点，不能进入第五阶项。

两个可见坐标的贡献由 (6) 给出，只涉及两个输入多项式乘积 UV 的取值及其**一阶**导数。因此不存在“两边都取一阶导数”的项，得到 D_c 的右下角为零。由 C_c 可逆，整个四阶块可逆，无需知道星号项。

### 3.6 第一层核的统一结论

(8)、(10) 的分子系数分别互素，分母只含 2、3。因此在每个 p≥11 的参数域 k 中都可逆。外块由 (11) 可逆。局部非零块的总维数为

\[
2+3a+4(m-N)=r-n.
\]

由 Hermite 插值满射及 (4)，得到

\[
\boxed{\ker\bar A=\operatorname{im}\bar B,\qquad\dim\ker\bar A=n.}\tag{12}
\]

这填补了此前只构造出 n 个核方向、尚不能排除更多方向的统一接口。结论在参数域中成立，不是对每个 δ 特殊化的等维声明。

## 4. 二阶提升存在，并可只用局部块求解

以 J 同时表示乘以 D_N/D_a 的系数矩阵，置 Z=BJ。第一次配对 C₁ 满足 \(C_1J=0\)。因为 A 对称且 (12) 成立，

\[
\bar B^T\overline{AZ/p}=0
\quad\Longrightarrow\quad
\overline{AZ/p}\in\operatorname{im}\bar A.
\]

所以可求得 Y，使

\[
\bar AY=-\overline{AZ/p},\qquad Q=Z+pY,\qquad AQ\in p^2O^r.
\tag{13}
\]

将右端变到第 3 节的局部直和基中，只需逆原点二阶块、截短内类三阶块和外类四阶块；根空间坐标为零。无需从高层 Smith 向量倒推修正。

定义真正的第二次配对

\[
C_2=\overline{Q^TAQ/p^2}.
\]

直接展开 (13)，得到

\[
\boxed{C_2=\overline{Z^TAZ/p^2}-Y^T\bar AY.}\tag{14}
\]

右侧与 Y 的具体解无关，因为两解之差在 ker Ā。第二项通常非零，不能把未修正的 Gram 值当作真正配对。

## 5. 未修正配对的统一 Laurent 公式

本节计算 \(G(\Phi_2U,\Phi_2V)/p^3\)。令 \(Z_{\rm full}\) 为 Φ₂ 在原 h 阶矩阵中的归一化列。Schur 修正不会改变这一阶：\(MZ_{\rm full}\) 在完整内类 S 行至少含 p²，在外类 S 行至少含 p³；\(\Lambda_S/p\) 的相应权为 p⁻¹、p⁻³。\(M_{SS}^{-1}\) 模 p 按类分块，跨类至少含 p。因此 Schur 二次修正至少含 p³（在 A 的 Gram 中），故

\[
\overline{Z^TAZ/p^2}
=\overline{G(\Phi_2U,\Phi_2V)/p^3}.
\tag{15}
\]

商矩的展开此处必须多保留一项：

\[
\mu(Q)\equiv S_5/(6p)-S_6/2+7pS_7/12-7p^3S_9/10\pmod {p^4}.
\tag{16}
\]

最后一项由 B₄=−1/30 给出。省略它会使最终配对标量错误。

\(\Phi_2\) 在截短内类有三重零点，完整内类四重，外类八重，原点二重。对 \(D_N^8\Phi_2^2UV/D_K\) 而言，留数估值分别至少为 10、11、11、6。非零类极点泛函最多损失七阶，原点最多损失一阶；因此模 p⁴ 只有截短内类留下贡献。原点对 (16) 的 Taylor 项也至少达到 p⁵。

截短内类的五节点计算给出 \(T_6-7/10\)。其中 7/10 来自 S₉ 项与 \(S_4^{(5)}=1\)。共同局部权有一个关键简化：

\[
\boxed{\text{局部权}=-1/D_a'(-c^2).}\tag{17}
\]

可直接核对：模 p 有 \(D_K=t^2F^6/D_a\)，而
\(2c^2F'(-c^2)=(-1)^m\)。将 W、\(\Phi_2^2\)、分母导数和局部坐标的 2c 因子代入后，十次幂的单位全部消去，只剩 (17)。

利用部分分式恒等式

\[
\sum_{c=1}^a\frac{U(-c^2)V(-c^2)}{D_a'(-c^2)}
=[t^{-1}]\frac{UV}{D_a},
\]

得到

\[
\boxed{\overline{Z^TAZ/p^2}=(7/10-T_6)\,\mathcal B_a,\qquad
\mathcal B_a(U,V)=[t^{-1}]UV/D_a.}\tag{18}
\]

a=0 时求和为空，两边皆零。

## 6. 修正二次项：外区恰好没有贡献

由此前 F₁ 的支撑结论，(13) 的右端在局部基中只有：截短内类的三个坐标，以及外类的第一个隐藏坐标。原点块为零。

外类方程具有形状

\[
\begin{pmatrix}0&C\\C^T&D\end{pmatrix}
\binom{y_h}{y_v}=\binom{f e_1}{0}.
\]

由 \(C=\left(\begin{smallmatrix}*&u\\v&0\end{smallmatrix}\right)\)，第二行方程迫使 \((y_v)_1=0\)。又因 D₂₂=0，所以

\[
\binom{y_h}{y_v}^{T}\mathsf O_c\binom{y_h}{y_v}
=-y_v^TDy_v=0.
\tag{19}
\]

由极化，同一构造中任意两个修正方向之间的外区配对也为零。因此所有修正二次项都来自截短内类。

设 \(w=(T_3,T_4,T_5)^T\)。截短内类目标的三个分量，除去共同单位及 2c 的缩放，就是 w；求解时逆的正是 \(\mathsf T\)。使用与 (17) 相同的单位消去，得到

\[
\boxed{Y^T\bar AY=-\bigl(w^T\mathsf T^{-1}w\bigr)\mathcal B_a.}\tag{20}
\]

把 (18)、(20) 代入 (14)，统一的真实配对公式是

\[
\boxed{C_2=\kappa(H)\,\mathcal B_a,}\tag{21}
\]
\[
\boxed{\kappa(H)=\frac7{10}-T_6+w^T\mathsf T^{-1}w
=\frac{200178112H+319463}{40(1122304H-529)}.}\tag{22}
\]

这比“有限样本的秩相同”更强：在自然多项式基 1,t,… 中，整个双线性配对就是同一个 Laurent 形式乘以统一标量。分子系数互素，因此在每个 p≥11 的参数域中 κ 非零。

## 7. 从第二次配对得到完整第三层下界

已有 Laurent 模型定理给出

\[
\operatorname{rank}\mathcal B_a=b=\max(0,\min(a,2d-a)).
\]

使用下面的对称矩阵旗标引理可直接计数。若 B 有 n 个独立的一阶核方向，其中 d 个可修正为 Q，使 AQ∈p²，且 \(\operatorname{rank}\overline{Q^TAQ/p^2}\le b\)，则

\[
v_p\det A\ge n+2d-b.
\tag{23}
\]

证明：取基的最后 d 列为 Q，中间 n−d 列为 B 的补充方向。对称矩阵变为

\[
\begin{pmatrix}
*&p*&p^2*\\p*&p*&p^2*\\p^2*&p^2*&p^2C
\end{pmatrix},\qquad \operatorname{rank}\bar C\le b.
\]

从中间 n−d 列提出 p、最后 d 列提出 p²，得到 n+d 阶。剩余矩阵最后 d 行模 p 只在最后 d 列非零，秩至多 b，所以再得到 d−b 阶。此引理本身不要求给定方向张成完整第一层核。

由 (13)、(21)，引理适用。加上 τ₀ 并用 det M=det M_SS det A，得到

\[
\tau_0+n+2d-b=48N-24p+22+a-b,
\]

即 (1)。由于这是 Gauss 赋值下的多项式系数整除结论，可令 δ=0 回到原泛函，即使某些局部逆在 δ=0 的特殊化处退化，最终行列式下界仍成立。

还可以显式构造第三阶列：取 Laurent 根空间矩阵 R₃，先求

\[
C_1T=-\bar B^T\overline{AQR_3/p^2},
\]

再通过局部块求 W，使

\[
\bar AW+\overline{AB/p}\,T=-\overline{AQR_3/p^2}.
\]

则 \(Q_3=QR_3+pBT+p^2W\) 满足 \(AQ_3\in p^3O^r\)。在参数域中，第一次配对的根空间恰为 im J，所以第一个方程由 (21) 的根空间关系保证可解。脚本直接核验了这些三阶列。

## 8. 异常特殊化得到更具体的解释

在原泛函 \(H=129/128\) 处，

\[
4352H+13=4399=53\cdot83,
\]
\[
1122304H-529=1130543=53\cdot83\cdot257.
\]

因此在 p=53、83，原点二阶块降一秩，每个截短内类三阶块也降一秩。只要上一阶段 S 块仍可逆，第一层核维数便增加 a+1，恰好解释此前 n+1、n+4、n+13 等异常样本。

这也解释了为什么 (22) 不能在这些素数直接代入原参数：其分母退化。保留参数、先证明系数整除、再特殊化行列式，仍是必需的步骤。没有声称所有 δ 的高层核空间都相同。更早的 p=53、δ=0 第三层模型反例仍有效。

## 9. 精确核验与证据范围

[second_pairing.py](second_pairing.py) 实现了：

1. 精确模 p⁶ 的对称 Schur 补；
2. 可见多项式与 χ 的除法、Hermite 插值换基、全部跨类零块；
3. 原点二阶块、截短内类三阶块及外区结构 (11)；
4. 仅通过局部块求解的一次修正；
5. 对未修正配对、修正二次项和实际配对分别核验 (18)、(20)、(21)；
6. 用 Laurent 根空间构造并直接验证模 p³ 的第三层列。

主数据 [second_pairing.json](second_pairing.json) 覆盖 p=11、31、43、53、83，及 a<d、a=d、d<a<2d、a≥2d。较早分解审计见 [second_pairing_normal_form.json](second_pairing_normal_form.json)，参数改变及原泛函见对应 center2、original 数据文件。退化样本明确报告局部不可逆，不记为正常提升成功。

18 组主参数均通过局部构造，共验证 70 个二阶方向和 32 个三阶方向。合并另外两个参数审计文件，共 28 组，其中 22 组可构造二阶提升，另 6 组在已明确的局部块处退化。独立脚本 [verify_second_pairing.py](verify_second_pairing.py) 用普通整数乘法重新核验 p=11、N=4、a=1 的保存证书；统计见 [second_pairing_validation.json](second_pairing_validation.json)。

还保留一个更细的限制：p=43、N=16、a=4、δ=2 时，局部求逆和公式 (21) 都通过，但第一次配对额外退化，脚本没有成功将指定 Laurent 根方向全部提升至三阶。这不影响旗标引理 (23) 给出的行列式下界；它再次说明，特殊化后的逐方向提升不能与参数域中的提升混为一谈。

符号恒等式单独保存在 [second_pairing_symbolic.json](second_pairing_symbolic.json)。这些都是有限实现证书；任意参数的结论依赖以上局部化、插值和矩阵引理。

## 10. 指定窗口收益与后续工作

在 α=1/8、y=p/K∈[1/3,3/8] 下，式 (1) 相对此前旧界的改善密度为

\[
\begin{cases}
15/4-10y,&1/3\le y\le11/32,\\
1-2y,&11/32\le y\le7/20,\\
11/4-7y,&7/20\le y\le3/8.
\end{cases}
\]

所以该窗口完整的已证改善为

\[
\boxed{127/11520=0.011024305555\ldots,}
\]

相对上一轮又增加 \(7/11520\)。精确积分见 [third_layer_gain.py](third_layer_gain.py) 和 JSON。本报告没有更新全局算术常数，亦没有把该 α=1/8 收益从 α=1/40 的旧缺口中扣除。

下一步应将本窗口界接入**同一 α 下的完整算术包络**，与实侧估计一起重新优化。若全局缺口仍为正，需要量化还缺多少，以及应从哪些新窗口或联合构造取得；不应仅凭这一局部定理宣布无理性证明闭合。新局部引理的独立审阅和 Lean 形式化也仍待进行。

复现主要检查：

```powershell
python research/second_pairing.py --triples 11:4:0,11:4:1,11:4:2,11:4:3,11:4:4,31:11:1,31:11:2,31:11:3,31:11:4,31:11:5,31:11:6,43:16:2,43:16:4,43:16:7,43:16:12,53:18:1,53:19:3,83:31:12
python research/second_pairing.py --center 2 --triples 11:4:1,17:6:1,31:11:2,43:16:4 --out second_pairing_center2.json
python research/second_pairing.py --center 0 --triples 11:4:1,31:11:4,43:16:0,53:18:0,53:18:3,83:31:0 --out second_pairing_original.json
python research/verify_second_pairing.py
python research/third_layer_gain.py
```
