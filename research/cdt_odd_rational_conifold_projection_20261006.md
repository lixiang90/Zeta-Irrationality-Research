# R0 的代数系数线性投影障碍与全参数正则族

日期：2026-10-06。NEW纯证明；只读上一轮冻结 R0/Kummer、P4/Sp4 与 conifold 校正输入，不执行、导入或修改旧/同行数学 producer。本文的否定结论限于明确的线性微分表达式空间，不排新的 inhomogeneous sources、tensor/nonlinear 模型或其它解析叶。没有数值 period independence、无理性或 Lean 声明。

## 1. 明确的真实输入

固定
\[
P=\theta^4-x(\theta+1/2)^4,\quad
y_0=\sum_{n\ge0}\left[\frac{(1/2)_n}{n!}\right]^4x^n,
\quad W=\sqrt x\,B,
\quad PW=\sqrt x/16.
\tag{D1}
\]
P 的 connected monodromy 为 Sp4，故绝对不可约且在任意有限代数覆盖上仍不可约。上一轮已证明在 canonical conifold branch
\[
W-\frac{\pi^4}{16}y_0\text{ 全纯于 }x=1.
\tag{D2}
\]
四阶 conifold monodromy 是非零 rank1 transvection；y0 的 log coefficient 为 \(t\log t/\pi^2\)、t=1−x，因此 \(\Delta y_0\ne0\)。

使用 x=u² 的覆盖后 W=uB(u²) 是真正的有理 Taylor germ；native x 上是 x^(1/2)Q[[x]]，两者不能混写。D2 的校正系数 π⁴/16 非代数。

## 2. 全代数函数系数的线性微分表达式

设 k 是任何 number field，F 是包含 Qbar 常数和 u 的有限代数函数域，定义在一个有限代数覆盖上；允许进一步 ramification。系数只用 F 的代数函数，不允许加入超越常数。用 D 表示该覆盖上延伸的 d/dx。对任意有限阶 A,B∈F[D]、h∈F，考虑
\[
G=A(W)+B(y_0)+h.
\tag{D3}
\]
**命题。** 若 G 在一个覆盖 conifold 的点全纯，则 A、B 均在 F[D] 中右整除 P（P 的 pullback 用同一个 D 表示）。因此
\[
G=A_1(\sqrt x/16)+h\in F.
\tag{D4}
\]
即该表达式的全部 period 层均被消去，剩下已知代数 forcing。

证明：在所选覆盖点绕行一圈，F 系数单值；若其 ramification index 为 e，P 的 transvection 变为 T1^e=1+eN，\(\delta:=\Delta y_0\ne0\)。D2 给 \(\Delta W=(\pi^4/16)\delta\)，故 G 全纯迫
\[
\{(\pi^4/16)A+B\}\delta=0.
\tag{D5}
\]
将 A、B 按 P 右除，余式 RA、RB 的阶数小于4。若 (π⁴/16)RA+RB 非零，它就是 δ 的一个阶数<4 的 annihilator，与 P 在该覆盖上的绝对不可约性矛盾。故
\((\pi^4/16)RA+RB=0\) 为 operator identity。

π⁴ 对 Qbar 超越，亦不属于 F：F 是 transcendence-degree-one algebraic function field，其常数代数闭包为 Qbar。每个余式系数在 F 中，因此上述 identity 强制 RA=RB=0（若某一 RA 系数非零，它会给 π⁴=−16 RB/RA∈F）。D4 随之成立。证明完毕。

若只取 A(W)+h，同样不需要 π 的超越性：Aδ=0 已迫 P 右整除 A。本文允许全部 finite-order rational/algebraic differential coefficients，但仅线性依赖 W、y0；**不**把这件事扩大为任意 rational/nonlinear differential expression 的分类。

P 在原点的 MUM Jordan4 只有一个 single-valued homogeneous germ，所以任何原点 meromorphic、number-field-initial homogeneous correction 都是一个代数常数倍 y0。这使 D3 覆盖了全部此类线性 homogeneous 背景及其有限微分表达式，仍未覆盖 de-log 的更大 inhomogeneous source 系统。

## 3. 一个正的全参数 conifold 正则族

定义在 Re ε>−1/2 的参数范围
\[
S_\varepsilon(x)=x^\varepsilon
\sum_{n\ge0}\left[\frac{\Gamma(n+1/2+\varepsilon)}{
\Gamma(n+1+\varepsilon)}\right]^4x^n,
\quad \Phi(\varepsilon)=\left[\frac{\Gamma(1/2+\varepsilon)}{
\Gamma(1+\varepsilon)}\right]^4.
\]
在 canonical x^(ε) branch，逐项 recurrence 给
\[
PS_\varepsilon=\varepsilon^4\Phi(\varepsilon)x^\varepsilon.
\tag{D6}
\]
右端在 conifold 附近关于 x、ε 共同全纯。

一致 Gamma ratio asymptotics给 compact ε 上系数
\(n^{-2}+O(n^{-3})\)。与 Li2/x 的可和导数比较给 Sε 的首 t logt 系数恒为1，与 ε 无关。在1处取 analytic particular（0、1、2次系数为0，从3次起非共振递推）；局部 Frobenius 收敛和参数依赖给共同全纯 particular。余下 homogeneous 层只有同一 rank1 log block。因此首 log 系数确定全部 log series，得到
\[
\boxed{S_\varepsilon-S_\eta\text{ 在 canonical }x=1
\text{ 分支共同全纯，对任意上述 }
\varepsilon,\eta.}
\tag{D7}
\]
D7 是 D2 的真正推广：S0=π²y0、S1/2=ν，故 ν−π²y0 正好是这个全参数差分。

令 \(Z_j=\partial_\varepsilon^jS_\varepsilon|_0\)。共同全纯性立即给
\[
Z_j\text{ 在1全纯，所有 }j\ge1.
\tag{D8}
\]
对于 j≥4，精确 forcing 为
\[
PZ_j=\frac{j!}{(j-4)!}
\partial_\varepsilon^{j-4}\{\Phi(\varepsilon)x^\varepsilon\}|_0.
\tag{D9}
\]
它是 logx 的 degree j−4 polynomial，最高系数 \(j!\pi^2/(j-4)!\) 非零，故 θ^(j−3)P 消去 Zj，阶数 j+1。原点 Zj 的最高项为 π²(logx)^j；绕0的 finite differences 给 j+1 个独立 germs，所以 j≥4 的实际最小阶数恰为 j+1。

这一正族不能免费作为 CDT arithmetic Taylor germs：每个 j≥1 在0都有非零 log^j 项，任意有限代数覆盖不能删掉该最高 log；有限常数线性组合也不能消去最大的 j。更一般的 rational ε 系列在原点可通过 Kummer cover成为 Taylor，但归一 Φ(ε) 仍须实际核算 Gamma constants。D7 不证明它们之间的 quotient algebraic，也不证明其 full integral models 已建立。

## 4. 新的一手文献与后续方向

本轮实际保存并阅读 EHMM III (Grove–Long–Rosen–Tu, arXiv2607.25173v1,35页)与 Rosen2026 weight3 transformation 论文 journal 原件（33页）。精确版本、哈希和实际阅读页见新 manifest。

EHMM III §2.1 的 residue/Clausen 分解将 length4 datum 拆成 length2 algebraic factor 与 length3 modular background；§4 的 CFGL theorem 对指定 R、Frobenius σ、integral change of variable unit-leading coefficient 给全 prime-power index recurrence，Proposition4.3 再给指定 truncated 4F3(1) 的 mod p relation。它不直接构造 D1 的 length5/Kummer extension，不给本19/原rank10评价矩阵的完整 Smith flags。其 whole-prime-power theorem 是值得迁移的结构输入，但仍需证明真实 differential/lattice comparison。

Rosen论文的 beta-normalized 3F2/L1 表达式与同一 eigenform even twist 的 period theorem说明可在真实 integral normalization 下消去 Gamma factors；其 conjugate datum/deRham discussion 不允许把未知 period 值自动作 coefficient σ。这里没有使用其 numerical unit-identification步骤作为新精确证明。

必须记录一个具体版本冲突：EHMM III v1 PDF25 将 π²·4F3(half4;1³;1)/16 写为 L(f8.4.a.a,1)。本轮实际回读 Rogers–Wan–Zucker原件PDF13 (30)，对 f2=η(2τ)^4η(4τ)^4 准确给同一数为 L(f2,2)。本项目因此沿用已校准 L2 公式，不将新预印本的那个 index 直接迁移为新目标。这里只记录原件之间的冲突；未据此否定 EHMM III 其它独立结果。

具体下一步由 D5 改变：同一 W/y0 模块的代数系数线性投影不能保留 R0 的 period 层又免费填1，须引入新的 arithmetic inhomogeneous/relative-cycle 源，或在 tensor 层保留新的 Γ-free 目标并重新核所有费用。D7/D8 可提供真实 logcycle normalization，但 log-at0 和 Gamma初值仍必须计入完整模型。

纯证明执行记录：本文未创建或运行数学 verifier；只执行 TLS-verified PDF 下载与只读 PDF 文本提取。没有有限 checks 代替上述微分模、Frobenius 或全参数证明。等待 root 限定独审；不认领目标完成。
