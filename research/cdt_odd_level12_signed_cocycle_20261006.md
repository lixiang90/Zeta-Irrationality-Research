# D12 共轭真实周期的 signed cocycle：全部 η 迭代与反射族

日期：2026-10-06。独立新 proof note；不修改冻结输入，不搜索生成元或参数，不运行任何旧/peer producer。本文从实际完成的非cuspidal W Laurent 身份得到一个三维、可精确计算的真实 cocycle，并证明一整族变换均不能加入目标函数的不变群。它不分类整个 stabilizer，不声称当前 augmented group 已经最大，也不提供数值无理性定理。

## 1. 实际函数、slash 及符号不能省略

采用[已证 pure source](cdt_odd_level12_source_period_20261006.md)的 Fσ、fσ=θq⁻³Fσ、fσ(i∞)=0，以及

\[
 \Theta=34560\sqrt3 L(3,\chi_{12}),\qquad
 h=f_\sigma+\Theta,\quad B=E_2-12E_2(12\tau),\quad H_\sigma=Bh.
 \tag{C1}
\]

以下恒等式是实际复解析函数的无条件恒等式；不把 σ 作用于未知 L 值。令 Γ=kerχ12⊂PSLΓ0(12)，并取

\[
 T=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
 W=\begin{pmatrix}0&-1\\12&0\end{pmatrix},\quad
 M=\begin{pmatrix}24&-7\\84&-24\end{pmatrix},\quad
 M'=\begin{pmatrix}-24&-7\\84&24\end{pmatrix},\quad
 \eta=\begin{pmatrix}1&0\\12&1\end{pmatrix}=WT^{-1}W^{-1}.
 \tag{C2}
\]

M 正规化 Γ；M²=−12I，M′M⁻¹∈Γ。群 \(\mathcal G=\langle\Gamma,M\rangle\) 上有实际 source 的符号 ε：Γ 上 +1、ΓM 上 −1。Fσ 与 B 都满足 Fσ|4γ=εγFσ、B|2γ=εγB。

对正 determinant 矩阵 γ=(a,b;c,d)，固定归一化

\[
 (f|_{-2}\gamma)(\tau)=\det(\gamma)^{-1}(c\tau+d)^2 f(\gamma\tau).
 \tag{C3}
\]

这是 right action：\((f|\gamma)|\delta=f|\gamma\delta\)。归一化使任意非零 scalar matrix 的 slash 为 identity。定义实际 polynomial defect

\[
 c(\gamma)=h|_{-2}\gamma-\epsilon_\gamma h.
 \tag{C4}
\]

Bol 身份与 Fσ 的 source sign 保证 c(γ)∈C[τ]≤2。它满足

\[
 c(\gamma\delta)=c(\gamma)|_{-2}\delta+
                  \epsilon_\gamma c(\delta).
 \tag{C5}
\]

所以不是无符号的 ordinary modular cocycle。若 b(γ)=εγc(γ)、ρ(δ)=εδ|−2δ，则 b(γδ)=b(γ)ρ(δ)+b(δ)，给标准三维 signed Sym² right representation。

实际 scalar 目标的变化是

\[
 H_\sigma(\gamma\tau)-H_\sigma(\tau)
       =\epsilon_\gamma B(\tau)c(\gamma)(\tau).
 \tag{C6}
\]

B 非恒零，故 Hσ 保持 γ **准确当且仅当** c(γ)=0。真实 T-periodicity、[实际 canonical M/M′ periods](cdt_odd_level12_full_leaf_20261006.md)给

\[
 c(T)=c(M)=c(M')=0.
 \tag{C7}
\]

这里 h|M=−h；不能误写成 h|M=h。相应 Bh 才是 scalar invariant。

## 2. 从完整 ordinary W Laurent 身份计算 c(η)

令 Gσ=Fσ|4W，其∞常数 b0=132480；令 gσ=θq⁻³(Gσ−b0)。输入是 source 稿式(21)的完整身份

\[
 f_\sigma-g_\sigma|_{-2}W
 =-\Theta+12\Theta\tau^2-3840i\pi^3\tau+
       \frac{3680i\pi^3}{3\tau}.
 \tag{C8}
\]

用真正 cubic primitive 完成非零常数 source：

\[
 \widetilde g=g_\sigma+
       \frac{b_0(2\pi i)^3}{6}\tau^3.
\]

其 W-slash 正好等于 reciprocal 项 3680iπ³/(3τ)，故

\[
 h=\widetilde g|_{-2}W+R_W,\qquad
 R_W=12\Theta\tau^2-3840i\pi^3\tau.
 \tag{C9}
\]

真正 gσ 是 T-periodic，但完成项不是。准确的 translation defect 为

\[
 D_-:=\widetilde g|_{-2}T^{-1}-\widetilde g
  =i\pi^3(529920\tau^2-529920\tau+176640).
 \tag{C10}
\]

由 Wη=T⁻¹W（在忽略 scalar 的 normalized slash 中）及(C9)，

\[
 c(\eta)=D_-|_{-2}W+R_W|_{-2}\eta-R_W.
\]

第一项为 iπ³(44160+529920τ+2119680τ²)；τ²|η=τ²、τ|η=τ+12τ²，第二部分为 −46080iπ³τ²。于是

\[
 \boxed{c(\eta)=i\pi^3P(\tau),\qquad
 P=44160+529920\tau+2073600\tau^2.}
 \tag{C11}
\]

所有 Θ 项在实际 h 的等式中准确抵消。若从 f 的 ordinary W 关系直接删 reciprocal 或 constant completion，将不能得到这一真实 cocycle。

## 3. 所有非零 η 次幂均留下周期

由(C5)，n>0 时

\[
 c(\eta^n)=\sum_{j=0}^{n-1}c(\eta)|_{-2}\eta^j.
 \tag{C12}
\]

使用 ηʲ=(1,0;12j,1)，对三个 polynomial 系数求和给所有整数 n 的闭式

\[
 \boxed{c(\eta^n)=i\pi^3P_n(\tau),\quad
 P_n=44160n+529920n^2\tau+
       (2119680n^3-46080n)\tau^2.}
 \tag{C13}
\]

负 n 由 c(η⁻ⁿ)=−c(ηⁿ)|η⁻ⁿ 或直接递推得到同一 polynomial；n=0 为0。该闭式本身已经证明 n≠0 时 defect 非零。

还有一个适用于后续 word 计算的正定 cone 证明：

\[
 P/44160=1+12\tau+(1080/23)\tau^2,
 \quad\operatorname{disc}(P/44160)=-1008/23<0.
 \tag{C14}
\]

P 是实轴上严格正的 homogeneous binary quadratic form。正 determinant normalized slash 保持这个 positive cone；即便某个 real τ 是分式变换的 pole，homogeneous 表达仍严格正。因此(C12)各项同为严格正，n>0 不会相消；n<0 的 defect polynomial 严格负。闭式的全 n discriminant 也为

\[
 \operatorname{disc}(P_n)
 =-4069785600 n^2(23n^2-2)<0\quad(n\ne0).
 \tag{C15}
\]

结论是：所有 n≠0 的 ηⁿ 均不保持 Hσ；这是整个离散 family 的真实函数结论，而非 finite endpoint checks。

## 4. 整族 Γ-translated M 反射的准确真实周期

取全部整数 n 的指定 group-derived family

\[
 J_n=\eta^n M\eta^{-n}
 =\begin{pmatrix}
 24+84n&-7\\84+576n+1008n^2&-24-84n
 \end{pmatrix}.
 \tag{C16}
\]

其det为12、trace为0、εJn=−1，endpoint为

\[
 a_n/c_n=(7n+2)/(84n^2+48n+7).
\]

这个 family 的每个 source 两端常数均为0，由 Bol/trace-zero Sym² +1 eigenline，存在唯一真实 period λJn 使

\[
 f_\sigma+f_\sigma|_{-2}J_n
  =\lambda_{J_n}Q_{J_n},\qquad
 Q_{J_n}=1+(c_n\tau-a_n)^2/12.
 \tag{C17}
\]

这里 λJn 确是 actual endpoint limit：趋近 a_n/c_n 时 fσ(Jnτ) 在 transformed infinity exponentially趋0，等式给有限 limit；无需另外任意 regularization。h 的 defect 为

\[
 c(J_n)=(\lambda_{J_n}+\Theta)Q_{J_n}
       =(c(\eta^n)+c(\eta^n)|_{-2}M)|_{-2}\eta^{-n}.
 \tag{C18}
\]

对 n≠0，括号的两个 real quadratic 同号且严格定号，再经 η⁻ⁿ slash 保持定号，所以 c(Jn)非零。准确 scalar（由(C13)/(C18)的 constant 系数）为

\[
 \boxed{\lambda_{J_n}=-\Theta+i\pi^3\,
 \frac{1920n(644n^2+552n+147)}{84n^2+48n+7}.}
 \tag{C19}
\]

分子内 quadratic discriminant −73968、分母 discriminant −48，两者 leading coefficient正。因此 imaginary coefficient 准确与 n 同号且 n≠0 时非零。n=0 是已知 canonical M；n=1 给独立 finite-B3 稿的 2578560/139，作为固定 normalization cross-check。本文没有搜索 endpoints。

Γ 内 η 保持 compact coordinate v，所以这些 Jn 属于同一个 algebraic involution branch 的不同真实 continuation fibers。式(C18)/(C19)说明这些非zero fibers不能无分歧填入 Hσ 的 quotient leaf；保留 ordinary upper-half-plane point 的 ram2 仍是合法解析输入。不能据此禁止任何 ramified cover，也不能推 full Γ quotient 的所有 fibers 均坏。

## 5. 精确三维 word 接口及开放的 stabilizer

在实际子群 \(\mathcal L=\langle T,M,M',\eta\rangle\) 上，固定生成元的 c 为0、0、0、iπ³P。逆元用

\[
 c(\gamma^{-1})=-\epsilon_\gamma c(\gamma)|_{-2}\gamma^{-1}.
 \tag{C20}
\]

因此任意给定 finite word 的 c/(iπ³) 是 rational degree≤2 polynomial，使用(C5)的三维 normalized Sym² matrix exactly 计算。它不含未知 L-value，也不是 formal endpoint trace。因为输入就是 actual h，各群关系产生相同 cocycle；c=0 正是该 word 对 actual Hσ 的 invariant 判据。

已知 \(G_{\rm aug}=\langle T,M,M'\rangle\) 确在 kernel 中，并有[独立完整基本域与合法盘证明](cdt_odd_level12_augmented_radius_20261006.md)。本稿证明 ηⁿ 及 Jn(n≠0) 不在 kernel；它没有证明 \(\mathcal L=\mathcal G\)、没有证明整个 kernel 等于 Gaug，也没有证明添加 η 的所有 mixed words 皆非zero。包含不同 source signs 的一般 word 可以有相消，positive-cone证明只用于以上准确指定的 families。

真正开放的下一接口是：给 Γ/M 的有限生成元完整 cocycle；解它的 Sym² signed kernel，并对任何新找到的实际 zero generators 重新构造合法基本域和容量。不能用 source 的 modular group 或 compact-curve automorphisms 直接代替这个真实 kernel。

## 6. NEW 精确证书与审阅边界

同名新 verify 独立定义全部矩阵和 slash；只核预定(C9)–(C19)的 symbolic identities、全整数 n recurrence、discriminants、source signs矩阵输入及 n=1 normalization。它不 import 旧 producer、不枚举研究参数、不对 π³ 或 L 值赋 Galois action。有限 checks 不替代正文 Bol、positive cone、actual endpoint 与 finite-word cocycle证明。

新证书作者第三次执行完成，32项全部通过。前两次在全 n discriminant 和 symbolic Jn matrix 的未展开表达式结构比较处停止；改为逐项 rational-expression 化简比较后通过。数学源、候选、固定检查范围均未改变，未扫描 n 或 prime。保存这个执行历史，不能称首次单次全通过。

root 已实际全文只读正文 §§1–6 与新 verify.py，限定独立复核通过：signed (C5)/(C6)、cubic completion 导致(C10)/(C11)、正定 cone、Jn 的 +1 Sym² eigenline及真实 endpoint 规范；没有执行 producer。作者的32项精确检查与上述全尺度证明范围分别记录。本文现据该实际审阅冻结；其它 peer 如有后续审阅，另记录其确切范围，不倒填为本轮输入。

旧 source/fullleaf/paired-coordinate 文件保持冻结。本文与 radius 稿的限制必须分开：指定群容量小不等于全部真实 kernel 已被分类。全 kernel 分类仍开放。
