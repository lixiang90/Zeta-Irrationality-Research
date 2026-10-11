# 真实连接矩：A 的首项、全奇 ζ 的正确 Apéry 极限与校正边界

日期：2026-10-06。NEW 纯证明。冻结输入只读；不运行或 import 旧 producer。本文补上[spin 稿](cdt_odd_classical_spin_pullback_20261006.md)明确留下的 A_n 首项和 F/A 极限，保留新的连接周期，不认领数值无理性。

## 1. 一个收敛的统一矩函数

令 Φ(t)=[Γ(t)/Γ(t+1/2)]⁴，并定义

\[
 T(\epsilon)=\sum_{m\ge0}\Phi(m+\tfrac12+\epsilon),\qquad
 P_j=T^{(j)}(0),\quad M_j=(-1)^jP_j.
 \tag{M1}
\]

T 在 Re ε>−1/2 全纯：在任意 compact set，Gamma ratio 的一致 Stirling 界给第 m 项 O(m⁻²)，因此 locally uniform 收敛且可逐次求导。四次 Euler Beta 积分及 geometric series 精确给

\[
 T(\epsilon)=\pi^{-2}\int_{[0,1]^4}
 \frac{\prod_i u_i^{-1/2}(1-u_i)^{-1/2}}{1-U}
 U^\epsilon\,du,
 \quad U=\prod_i u_i.
 \tag{M2}
\]

对于 Re ε>−1/2，0 边界可积。所有 u_i→1 时，以 v_i=1−u_i 记，1−U 与 Σv_i 可比；权重为 ∏v_i⁻¹/²/(Σv_i)，四变量径向积分近零为 O(dr)，所以这个唯一新的角点也可积。固定 ε 的所有 log 插入仍可积。故

\[
 \boxed{M_j=\pi^{-2}\int_{[0,1]^4}
 \frac{\prod_i u_i^{-1/2}(1-u_i)^{-1/2}}{1-U}
 (-\log U)^j\,du>0\quad(j\ge0).}
 \tag{M3}
\]

它同时组织冻结 spin 稿的 S_r=M_{2r}。还可写成

\[
 T(\epsilon)=\left[\frac{\Gamma(1/2+\epsilon)}{\Gamma(1+\epsilon)}\right]^4
 {}_5F_4\left(1,\tfrac12+\epsilon,\tfrac12+\epsilon,\tfrac12+\epsilon,\tfrac12+\epsilon;
 1+\epsilon,1+\epsilon,1+\epsilon,1+\epsilon;1\right).
 \tag{M4}
\]

这是实际收敛矩函数的恒等式。高阶 ε 导数包含 log 插入及新的扩张，不能据此把所有 M_j 都当成原 rank4 齐次周期，更不能声称统一公式已证明所有奇 ζ 无理。

## 2. A 的首项完全由 M₁ 决定

统一记 a_n=binom(2n,n)⁴/256ⁿ、y₀(x)=Σa_nxⁿ，以及冻结的 B(x)=8Σa_n(H_{2n}−H_n)xⁿ。令

\[
 E=B-8\log2\,y_0=\sum e_nx^n.
 \tag{M5}
\]

精确 digamma 公式 ψ(n+1/2)−ψ(n+1)=2(H_{2n}−H_n−log2) 给

\[
 \Phi'(n+1/2)=\pi^2 e_n,
 \qquad E(1)=P_1/\pi^2=-M_1/\pi^2<0.
 \tag{M6}
\]

这里 e₀=−8log2；n≥1 时 a_n=1/(π²n²)+O(n⁻³)、H_{2n}−H_n−log2=−1/(4n)+O(n⁻²)，故 e_n=O(n⁻³) 且 Σe_n 绝对收敛。冻结 Wronskian 恒等式严格化为

\[
 A(x/256)=y_0^2+x(y_0E'-y_0'E).
 \tag{M7}
\]

本式左侧按旧记法表示 ΣA_n(x/256)ⁿ；常数 −8log2 的 gauge 不改变 Wronskian。y₀² 与 y₀·xE′ 的第 n 系数均 O(n⁻²)：其两个因子系数都是 O((n+1)⁻²)，将 convolution 在 n/2 分开即可证明。

剩余项 [xⁿ](xy₀′E)=Σ_{j=0}^{n−1}(n−j)a_{n−j}e_j。在 j≤n/2 上，n(n−j)a_{n−j} 一致有界且对固定 j 趋于 1/π²，绝对可和 e_j 支配该段；在 j>n/2 上，|e_j|=O(n⁻³)，并且 Σ_{k≤n/2}ka_k=O(log n)，乘 n 后的尾段 O(log n/n²) 趋零。严格得到

\[
 \boxed{\frac{A_n}{256^n}\sim\frac{\kappa}{n},\qquad
 \kappa=-\frac{E(1)}{\pi^2}=\frac{M_1}{\pi^4}>0.}
 \tag{M8}
\]

这是全 n 渐近证明，不是有限拟合，也不需要猜测 CY 连接矩阵的数值条目。

## 3. 真实 Apéry 极限以及校正所需的新目标

冻结全固定 r≥1 的 F_{n,r}~256ⁿM_{2r}/n，以及真实系数关系

\[
 F_{n,r}=C_{n,r}+(2r+2)!(2^{2r+3}-1)A_n\zeta(2r+3)
 \tag{M9}
\]

与(M8)合起来准确给

\[
 \boxed{\lim_{n\to\infty}\frac{F_{n,r}}{A_n}
 =\frac{\pi^4M_{2r}}{M_1}>0,}
 \tag{M10}
\]
\[
 \boxed{\lim_{n\to\infty}\frac{C_{n,r}}{A_n}
 =-(2r+2)!(2^{2r+3}-1)\zeta(2r+3)
 +\frac{\pi^4M_{2r}}{M_1}.}
 \tag{M11}
\]

特别 r=2 的真实极限为 −91440ζ(7)+π⁴M₄/M₁。它不是未经证明的纯 ζ(7) 极限。对实 x↑1，A(x/256)~−κlog(1−x)。因此减去 (M_{2r}/κ)A 可取消 F 的首个 log 发散，但其系数引入 π⁴M_{2r}/M₁；并未给有理系数的小线性形式或清除整个 local monodromy。

## 4. canonical conifold 的 forcing 仍阻止完整消除

只讨论从 x=0 沿实区间延拓到 x=1 的 canonical 分支。沿用冻结 forcing 记号 H=Σ_{n≥1}h_nxⁿ、h_n=(n−1)!⁴/(1/2)_{n+1}⁴。此处 h_n 与第2节 a_n 不混用。Gamma 比精确给

\[
 h_n=\pi^2\frac{\Gamma(n)^4}{\Gamma(n+3/2)^4}
 \sim\pi^2n^{-6}.
 \tag{M12}
\]

令 P₃(X)=48X³+80X²+40X+5、G=960x−(3/2)xθ²P₃(θ)H，则

\[
 [x^{n+1}]G=-\tfrac32n^2P_3(n)h_n
 \sim-72\pi^2/n,
 \qquad G(x)\sim72\pi^2\log(1-x).
 \tag{M13}
\]

Abelian 比较证明后一式；初值项 960x 是有界项。H 的 Fuchsian 模块在1有整数指数 0、1、2、5，非齐次多加一个有理方向，不产生非整数指数。因此 G 有收敛 Laurent-log 局部展开。单值的这类函数只能是 meromorphic；(M13)既排除有极点（增长快于 log），又排除 removable，故 G 的 canonical local monodromy 非零。

任意固定 c∈C 的 F=C₂+cA 均满足 L₅F=G。有理系数微分算子保留 single-valuedness，所以 F 在此 canonical conifold 分支不能 single-valued，更不能 holomorphic。包括按(M10)选择 c 以消去最高发散的组合：较低层的 branching 仍被真实 forcing 强制保留。

这个结论不分类所有 transported/conjugate 分支或其他模型的合法叶，也不排除新几何源的成功校正。[精确 rank10 稿](cdt_odd_classical_zeta7_full_rank_20261006.md)另用无穷远的不可取消 log⁷，排除整个 forcing 模块内的有理微分特解；二者是不同范围的证明。

## 5. 文献周期比较的严谨边界

Rogers–Wan–Zucker 的[版本明确的原始论文](https://arxiv.org/pdf/1303.2259v2) §5、(30)给 f(τ)=η(2τ)⁴η(4τ)⁴ 的准确关系 L(f,2)=π²y₀(1)/16。由 Φ(n+1/2)=π²a_n，严格有

\[
 \boxed{M_0=\pi^2y_0(1)=16L(f,2).}
 \tag{M14}
\]

论文 PDF13–14 已实际核读并[保存版本快照](../literature/rogers_wan_zucker2013_moments_elliptic_critical_l_values_v2.pdf)。这个正的 modular 周期识别只给 M₀；(31)中的 L(f,3) 用另一 7F6/椭圆积分表达，不能未经 comparison 推成 M₁、M₄ 或所有 log 矩的求值。

Bönisch–Klemm–Scheidegger–Zagier 的[作者 PDF](https://people.mpim-bonn.mpg.de/zagier/files/preprints/ADEK.pdf)中，PDF24 的(2.56)明确把 b_{N8}=−32ω_f⁻标成 conjecture；PDF27 在(3.11)前说明完整周期矩阵由数值计算得到。PDF36–37 的几何对应证明 modular 周期及 quasi-period 的出现，但(4.28)只在 multiplicative constant 意义下比较，不能直接当作本项目的完整整格比较。

其(2.4)、(2.6)、(3.6)的 Frobenius 记号给 X₁=(2πi)²Π₀,₁，且 x=256z，所以 conifold 处 Π₀,₁=E(1)。在论文 w⁺的这个坐标归一化下严格有 M₁=w⁺/4。这只是同一 Frobenius 值的命名，未证明 w⁺与标准 integral modular period 的精确倍数。

新的直接正矩证明(M8–M11)避开了这些未经校准的条目。下一步需要实际几何 cycle comparison、完整整格及 finite-place 成本；不能用高精度匹配替代。

## 6. 审阅与推进

本稿为 NEW 纯解析/代数证明，没有运行证书。conjugate_projection 实际全文只读独审 M1–M13，通过统一矩归一化、M8 两段 convolution、全固定 r 的正确极限及 canonical conifold 范围；另实际读 CY 作者 PDF8–9、24、26–27、36–37，确认 M₁=w⁺/4 及数值矩阵/乘法常数的限制。随后实际补审新增 M14 及本地 RWZ v2 PDF13–14，通过 L(f,2) 的准确归一化。root 实际核读这些数学链及 RWZ PDF13–14；未把相关段审阅记成整本论文或整格重建。最终哈希及审阅范围由新 root review 登记，本文现冻结。没有 Lean 验证、新 ζ(7) 无理性或数值线性无关性结论。
