# D12 同角色 gauge–Eichler 张量：真实周期与 Taylor 障碍

日期：2026-10-06。独立新证明记录；不修改冻结 source、预算、transport 或 radius 文件，不作参数或素数搜索，不运行旧或 peer producer。本稿核查一个具体正方向：用权2 χ12 Eisenstein gauge 与权4 χ12 的三重积分作 Fricke 张量收缩，能否得到 Q 系数、同一 W12 解析叶的实际 scalar。

结论分三层。原始 `(1,χ12)/(χ12,1)` 双包的交换系数确实能作有理张量收缩，但唯一非零常数 source 产生的三次对数不能由 quadratic Eichler periods 消去。同 level12 另有 `(χ−3,χ−4)/(χ−4,χ−3)` 双包，其两端常数均为0，不能笼统称必须升到 level24；然而该包的周期只有已知的 Tate π³，实际完成的 invariant 不再有代数 Taylor 系数。升 level24 可把原始 source 的两端常数消去，但两个有理 tensor 之间只存在一个 K 系数的 middle-period 消去方向，不能直接取有理 trace。

上述都是指定 Eisenstein packets、指定 gauge 和有限 quadratic period correction 的障碍；不排混入原 D12 trivial-character oldforms、cusp forms 的不同真实投影，更不排整个 modular/holonomy 方法。没有新数值无理性或线性无关性定理，也没有免费确定新 scalar 的实际 rank。

## 1. 文献、规范与整个 level12 同角色 Eisenstein 空间

记 `r=√3`、`K=Q(r)`、`χ=χ12=χ−3 χ−4`，`q=e^(2πiτ)`、`θ=(2πi)⁻¹d/dτ`。对 real primitive characters α、β，conductors 分别为 L、R，采用

\[
E_{k,\alpha,\beta}=c_0+\sum_{n\ge1}
 \left(\sum_{d\mid n}\alpha(n/d)\beta(d)d^{k-1}\right)q^n,
\quad
c_0=\begin{cases}-B_{k,\beta}/(2k)&L=1,\\0&L>1.\end{cases}
\tag{T1}
\]

本稿所有 α、β 均 real quadratic 或 conductor1，故文献中 `α/β` 与 `αβ` 的 character 规范在这里相同。原件是 [William Stein, Explicitly Computing Modular Forms，§5.3、印刷p86/PDFp100](../literature/stein_modular_forms_computational_author.pdf)，式(5.3.1)、Theorems5.8–5.9；作者现行网页为 [Explicit Basis for the Eisenstein Subspace](https://wstein.org/books/modform/modform/eisenstein.html)。该定理允许 k2 非主角色 pair；本稿没有把 trivial/trivial k2 的例外漏掉。已有原件和 hash 复用 [primary manifest](../literature/manifest_cdt_odd_cartier_primary_20261006.json)，没有重新下载或重复计文献。

`cond(α)cond(β)t |12` 且 `αβ=χ12` 的全部 primitive pairs 正好是

\[
(1,\chi),\ (\chi,1),\ (\chi_{-3},\chi_{-4}),\
(\chi_{-4},\chi_{-3}),\qquad t=1.
\tag{T2}
\]

所以 k2 和 k4 的同角色 Eisenstein 空间各为这四个 packets 的直接和；level12 内没有原始 `(1,χ)/(χ,1)` 的额外 oldscale。这是这个角色空间的完整分类，**不是**所有 trivial-character、mixed-character sources 的分类。

使用 determinant-normalized slash

\[
 (F|_k\gamma)(\tau)=\det(\gamma)^{k/2}(c\tau+d)^{-k}F(\gamma\tau),
 \quad W_N=\begin{pmatrix}0&-1\\N&0\end{pmatrix}.
\tag{T3}
\]

三重积分的 slash 为 `|−2`，与冻结 [source-period](cdt_odd_level12_source_period_20261006.md) 和 [signed-cocycle](cdt_odd_level12_signed_cocycle_20261006.md) 相同。以下 σ 只作用于已写明的 algebraic coefficients，不作用于未知 transcendental periods。

## 2. Fricke 因子：直接 lattice 证明与 k2 求和问题

令 `g(α)=Σa α(a)e^(2πia/L)`。在本稿四个 pairs、k2或k4上，准确公式为

\[
 E_{k,\alpha,\beta}|_kW_{LR}
 =\alpha(-1)\left(\frac RL\right)^{k/2}
   \frac{g(\alpha)}{g(\beta)}E_{k,\beta,\alpha}.
\tag{T4}
\]

其中 `g(1)=1`。这不是把 newform 的 Fricke eigenvalue 公式误用到全部 Eisenstein space。直接证明如下：

\[
 \mathcal G_{k,\alpha,\beta}(\tau)
 =\sum'_{m,n\in\mathbb Z}
       \frac{\alpha(m)\beta(n)}{(Rm\tau+n)^k}
 =\frac{2(-2\pi i)^kg(\beta)}{R^k(k-1)!}
       E_{k,\alpha,\beta}(\tau).
\tag{T5}
\]

最后等式来自 n 按 β 的 conductor 分组后的 Lipschitz Fourier identity；m 正、负项由 parity 配成2倍，m0 项恰给(T1)的 Bernoulli 常数。直接换 `m′=n,n′=−m` 给

\[
 \mathcal G_{k,\alpha,\beta}|W_{LR}
 =\alpha(-1)(L/R)^{k/2}\mathcal G_{k,\beta,\alpha},
\]

再除(T5)的 Fourier normalization 得(T4)。

k4 逐 lattice point 绝对收敛。**k2 不能称逐点绝对收敛**，但这四个 pairs 有一个无需猜 regularization 的合法求和：按完整 character periods 作 rectangular blocks。χ12 的 centered support 是 `±1,±5`，它的总和与 first moment 均为0，故 `(1,χ)/(χ,1)` 的每个完整 block 在远处为 `O((|m|+|n|)⁻⁴)`。odd/odd pair 的两个 centered supports 是 `±1 mod3`、`±1 mod4`；两个角色各总和0，先后作 finite difference 同样给 order−4 的 rectangular block。零角色边界项不贡献。blocks 在二维上绝对可和，并在 `m′=n,n′=−m` 下准确交换完整 centered blocks。因此上述换元合法，k2 没有未计算的 quasimodular correction。固定 m 的 n 求和本身绝对收敛，所以(T5) Fourier 推导也与这个 block 定义一致。

Gauss sums 为 `g(χ)=2r`、`g(χ−3)=ir`、`g(χ−4)=2i`。尤其 canonical `E₂=E₂,1,χ` 的 Fricke 因子是 **+2r**、常数为−1。为了采用根任务提出的 `κ₂=−2r`，必须定义

\[
 G_E=-E_{2,1,\chi}=1-\sum_{n\ge1}
       \frac{\chi(n)nq^n}{1-q^n},\qquad
 G_F=E_{2,\chi,1}.
\tag{T6}
\]

于是 `G_E|₂W=κ₂G_F`、`G_F|₂W=κ₂⁻¹G_E`。本文不把这个符号误作 canonical E₂ 自身的符号。

## 3. 原始 χ12 双包：有理 tensor symbol 与真实 cubic 障碍

记

\[
 E=E_{4,1,\chi}=23+\sum\chi(n)n^3q^n/(1-q^n),
 \quad F=E_{4,\chi,1},\quad\kappa_4=24r.
\tag{T7}
\]

真正满足 `θ³f_E=E` 的完成 primitive 必须是

\[
 f_E=\frac{23(2\pi i\tau)^3}{6}
       +\sum_{n\ge1} E_nq^n/n^3,
 \quad f_F=\sum_{n\ge1}F_nq^n/n^3.
\tag{T8}
\]

Bol 身份只给

\[
 f_E|_{-2}W=\kappa_4f_F+P_E(\tau),\quad
 f_F|_{-2}W=\kappa_4^{-1}f_E+P_F(\tau),
 \quad\deg P_E,\deg P_F\le2.
\tag{T9}
\]

由于 `κ₂κ₄=−144`、`κ₂/κ₄=−1/12`，忽略这些实际 periods 的 homogeneous tensor symbols 确实有两个有理 W+ 方向：

\[
 I_1=G_Ef_E-144G_Ff_F,\qquad
 I_2=G_Ef_F-\frac1{12}G_Ff_E.
\tag{T10}
\]

但 λI₁+μI₂ 的 cubic-log coefficient 恰是

\[
 \frac{23(2\pi i)^3}{6}
       \left(\lambda G_E-\frac\mu{12}G_F\right).
\tag{T11}
\]

`G_E(0)=1`、`G_F=q+…`，两 q germs 独立，故非zero algebraic constants λ、μ 不能让(T11)恒零。任何 `q^j(log q)³` 都不是 Taylor germ，即使 j>0；quadratic polynomial periods 不能消掉最高 log³。

本节结论只认领(T10)这两个固定 tensor directions 的 algebraic constant combinations及 finite degree≤2 period corrections。加入两端 constant0 的 cusp 或 odd/odd primitives 不产生可抵消(T11)的 log³；但这句话不对任意 local q-meromorphic multiplier 作 no-go。任意 multiplier 的推广还必须另要求它是适当 weight2 modular coefficient，且 W-slash后仍为q-meromorphic germ，本文不证明那个更宽版本。已有 pure D12 source 使用的 trivial-character oldforms也在本节 scope之外。

另一个常见错误是只使用 `f_E⁰=f_E−23(2πiτ)³/6` 却保留(T9)。它的 source 是 `E−23`，不是 modular form，准确关系反而是

\[
 f_E^0|_{-2}W=\kappa_4f_F+P_E(\tau)
              +\frac{23(2\pi i)^3}{864\tau}.
\tag{T12}
\]

这个 reciprocal Tate 项来自完成 cubic 在 `|−2W` 下的像，不能删除。冻结 signed-cocycle 中 ordinary-W 的完整 Laurent 项正体现了同一个问题。

## 4. 同 level12 的 odd/odd 双包确实没有 cubic，但只有 Tate periods

令 α=χ−3、β=χ−4，

\[
 E_o=E_{4,\alpha,\beta},\ F_o=E_{4,\beta,\alpha},\quad
 A_o=E_{2,\alpha,\beta},\ B_o=E_{2,\beta,\alpha}.
\]

四个常数均为0，两 primitive `f_o=θ⁻³E_o`、`g_o=θ⁻³F_o` 是真实 rational Taylor germs，且 W 端的源常数也为0。由(T4)

\[
 A_o|W=c_2B_o,\ E_o|W=c_4F_o,
 \quad c_2=-2r/3,\ c_4=-8r/9,
 \quad c_2c_4=16/9,\ c_2/c_4=3/4.
\tag{T13}
\]

Dirichlet convolution给

\[
 L(s,E_o)=L(s,\alpha)L(s-3,\beta),\quad
 L(s,F_o)=L(s,\beta)L(s-3,\alpha).
\tag{T14}
\]

在 s2，两个 odd character 的 `L(−1)=0`，所以两个 Eichler polynomial 的 middle term 都为0。s1、s3 的非zero critical values 全为 algebraic·π³ 乘 normalization；**这里没有非临界的 L(3,χ12)**。Stein原件 §5.2.2、印刷p85/PDFp99 给 parity-matching positive L-value 的 Gauss–Bernoulli 公式，负整数值直接由 Bernoulli 定义得到：

\[
 L(0,\alpha)=1/3,\ L(0,\beta)=1/2,
 \quad L(3,\alpha)=\frac{4\pi^3}{81r},\
 L(3,\beta)=\frac{\pi^3}{32}.
\]

因为两端 source exponentially 衰减，Mellin 积分在 critical 点合法；从重积分核可得真实 endpoint 常数

\[
 c_E=f_o(0)=L(3,E_o)=\frac{2\pi^3}{81r},\quad
 c_F=g_o(0)=L(3,F_o)=\frac{\pi^3}{96}.
\tag{T15}
\]

原点0指 cusp τ→0 的上半平面极限，不是 q0。Taylor primitive 在 q0 的值为0。W² 与 middle term0 固定完整真实 cocycles：

\[
 f_o|_{-2}W=c_4g_o+12c_E\tau^2-c_4c_F,\
 g_o|_{-2}W=c_4^{-1}f_o+12c_F\tau^2-c_4^{-1}c_E.
\tag{T16}
\]

因此 `h_E=f_o−c_E`、`h_F=g_o−c_F` 确实准确交换，实际 W-invariant Taylor tensors 为

\[
 J_1=A_oh_E+\frac{16}{9}B_oh_F,\qquad
 J_2=A_oh_F+\frac34B_oh_E.
\tag{T17}
\]

它们的 primitive 部分有 Q coefficients，但 correction 是 π³K-gauge。该 correction 的系数矩阵行列式（除π⁶）为

\[
 \frac34\left(\frac{2}{81r}\right)^2
       -\frac{16}{9}\left(\frac1{96}\right)^2
 =\frac1{6561}-\frac1{5184}\ne0.
\tag{T18}
\]

两 gauges 的 coefficient q2 分别−1、−2，q1均1，故本身独立。任何非zero algebraic constant linear combination 的 correction 都非zero；因 π³ 超越，至少一个 Taylor coefficient 非代数。不能把(T17)作为 K[[q]] 算术 holonomy input，更不能在假 `L(3,χ12)∈Q` 下把这个已知 Tate period 变成有理数。

这完成了一个准确区分：**same-level constant0 packets 存在**，但该特定替代只投影到已知 Tate periods。它不是“level12 必须升24”的定理。

从(T2)还可读出更窄但完整的 source 障碍：在整个 weight4 χ12 Eisenstein 空间内，要求源在∞及 W∞均constant0，先迫 `(1,χ)` coefficient0，再迫 `(χ,1)` coefficient0；剩下的正好是 odd/odd 双包。因此单靠这个同角色 Eisenstein space、同时消两端 cubic，不能保留纯 L3χ12 packet。任意 cusp-source 在两端本已constant0，不能抵消被迫消失的两个原始 directions。

## 5. 升 level24：两个端点可修好，但有理 trace 再遇 middle period

对原始 E/F、G_E/G_F 定义

\[
 S_E=E(\tau)-E(2\tau),\quad
 S_F=F(\tau)-16F(2\tau),
\]
\[
 A_E=G_E(\tau)-G_E(2\tau),\quad
 A_F=G_F(\tau)-4G_F(2\tau).
\tag{T19}
\]

源及 gauges 在∞均constant0。直接 oldscale 换元给

\[
 S_E|_4W_{24}=-6rS_F,\quad
 A_E|_2W_{24}=rA_F.
\tag{T20}
\]

反向因子分别为−1/(6r)、1/r。原 E/F block 的 two-end constant 这个局部问题因此可在24修好；没有据此断言 genus0、完整整模型或 rank。

`f=θ⁻³S_E`、`g=θ⁻³S_F` 均 Q[[q]]，其 two rational homogeneous W+ tensor symbols 是

\[
 U_1=A_Ef-18A_Fg,\qquad
 U_2=A_Eg-\frac16A_Ff.
\tag{T21}
\]

但 middle periods 未消失。真实 Mellin 值为

\[
 L(2,S_E)=-\frac32\zeta(2),\quad
 L(2,S_F)=\frac14L(2,\chi)
         =\frac{\zeta(2)}{4r}\ne0.
\tag{T22}
\]

前者的 oldscale 因子是1−2⁻²，后者是1−16·2⁻²；这里没有把 n^-3 integration factor 错加到 modular oldform 的 L-series。`L(2,χ)=ζ(2)/r` 来自同一 parity-matching Bernoulli 公式。

在

\[
 f|W_{24}=-6rg+P_f,\quad g|W_{24}=-(6r)^{-1}f+P_g
\]

中写 middle coefficients 为 b_f、b_g。两端常数均0，使 period polynomial 合法。直接 endpoint 重积分给 `f′τ(0)=2πi L(2,S_E)`、`g′τ(0)=2πi L(2,S_F)`；而 `|−2W24` 在∞将这个 first endpoint derivative 送到 `−f′τ(0)τ` 或 `−g′τ(0)τ`。因此准确规范为

\[
 b_f=-2\pi iL(2,S_E)=\frac{i\pi^3}{2},\quad
 b_g=-2\pi iL(2,S_F)=-\frac{i\pi^3}{12r}\ne0,
 \quad b_f=-6r b_g.
\tag{T22a}
\]

这也与 Beukers1987 Proposition1.2的完整 Eichler identity相同；anti-source `S_E+6rS_F` 的 Sym² +1 polynomial eigenspace给出同一个 ratio。没有把两个 Fricke source 的 prefactors 无理由地设成相同。

准确 tensor defect 的 linear-τ 部分于是为

\[
 (\lambda U_1+\mu U_2)|W_{24}-(\lambda U_1+\mu U_2)
  \supset (\mu-6r\lambda)b_g(A_E+rA_F)\tau.
\tag{T23}
\]

常数 gauge counterterms 的 W-defect只有 τ0与τ²，不能取消(T23)；更高的 τ-polynomial counterterms本身破坏 Taylor germ，除非该 log coefficient恒零。因此指定两个 tensor directions 中的唯一 middle-free direction为 `μ=6rλ`：它在 K 而不是 Q 上，正好 factor为

\[
 U_1+6rU_2=(A_E-rA_F)(f+6rg).
\tag{T24}
\]

σ 把它送到 `(A_E+rA_F)(f−6rg)`；后者的 source 是 W-plus，middle L-value为−3ζ2，不为0。故“两个 signs 都各自消周期，然后有理 trace”的步骤仍不成立。该障碍只针对(T19)–(T21)这个明确 two-oldscale tensor family，不排更多 sources 的 period cancellation。

## 6. 升 level 的指定自然叶几何损失

若完成真实 period projection 后只使用自然 `<T,W24>` filled leaf，则标准化 Hecke 参数由 `√12` 变为 `√24`；不能把原来的 W12 半径带过去。沿用 [Hecke radius 全尺度公式的证明](cdt_odd_level12_hecke_radius_20261006.md)的假设 `π²/(3Λ²)<1`（w²24满足），获得下列 Green 归一及 geometric majorant；本段没有认领该 majorant 对全部 w>2适用：

\[
 \log R(w)=\frac{2\pi^2}{w^2}\mathcal C(w),\quad
 \mathcal C(w)\le1+\frac{\pi^2/(3w^2)}{1-\pi^2/(3\Lambda^2)},
 \quad\Lambda=(w+\sqrt{w^2-4})/2.
\tag{T25}
\]

在 w²24，`Λ²=11+2√30>21`、`π²<10`，故

\[
 \log R(\sqrt{24})<\frac56\frac{247}{212}
 =\frac{1235}{1272}<1,
\]

而 empty double word 给 `log R(√12)≥π²/6>3/2`。所以这两张指定自然 filled surfaces 的 q-radius 有严格损失。它不是任意 level24 continuation surface 或整个实际 period kernel 的上限，也不声称新的 tensor projection 已构造出合法 map。两 embedding 能否共同用一个更大实际群仍须真实 cocycle 证明。

## 7. 哪些步骤完成，哪些仍开放

已完成的全尺度输入是：四个同角色 Eisenstein packets 的分类；明确 Fricke 规范及合法 k2 lattice blocks；原始包的 cubic/Taylor 障碍；odd/odd 的真实 Tate periods及非代数 correction；two-oldscale 的 middle-period obstruction；指定自然 W24 surface 的严格 radius 比较。

没有把 tensor homogeneous symbols当作实际函数，没有给未知 period定义Galois action，没有免费增加导数/积分的实际 rank。尤其没有证明不存在更复杂 Q scalar：混入 trivial-character oldscales、更多相容周期、不同 modular character或完整实际 cocycle kernel 都仍可另研究。根任务已有 mixed-source D12 构造正好在本稿 same-character source scope 之外。

最具体的下一数学接口是：若寻找真正 Q scalar，同步求解全部 source constants、完整 quadratic periods与σ兼容，而不仅求 homogeneous Fricke eigenvectors；必须让 π³ 的 middle/cubic coefficients在同一个实际组合中消去。成功后再单独证明实际 rank、全整数模型、完整合法叶以及 CDT预算。本稿没有可直接放入现有预算的新目标。

## 8. 证明记录与审阅范围

本稿是纯理论 MD 证明记录，没有新 producer 或数值 certificate。Bernoulli/Gauss、Fricke/tensor矩阵、reciprocal、Tate determinant和唯一自然 radius比较均为正文写明的固定精确恒等式。没有调用、import、执行任何冻结或 peer producer，没有扫描参数、prime或prefix；没有把有限样本作为全尺度 lattice、Bol/Mellin或Taylor证明。

Root 已实际全文只读独审本MD §§1–8：核T4/T5合法 character blocks与Fricke规范、T9–T18实际cubic/Bol/oddpair corrections、T19–T24的middle endpoint及T25的w²24有理上界。按该独审要求，§3已删除任意local q-meromorphic multiplier的过宽推广，只保留固定tensor/algebraic constants scope；§6已将radius证明限于其 `π²/(3Λ²)<1` 假设；T22a补入准确endpoint derivative规范。没有执行producer或数值检验。本文在这个范围冻结，旧文件保持冻结。
