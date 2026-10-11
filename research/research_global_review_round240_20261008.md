# 第240轮正式全局复盘：从旧 holonomy 源转向完整混合矩泛函

2026-10-08。上次正式复盘236，本轮相隔4个完成轮次，按用户4～8轮要求提前执行并重新计数。**目标仍是新的数值无理性或线性无关性定理；本轮没有得到这种定理。** 这次复盘改变下一阶段资源分配：停止默认优化旧三函数源，选定一个已付真实周期投影的新完整矩阵，先检验决定成败的整化与非零关。

## 1. 最近四轮的真正收益与停止理由

237把 degree-D 联合整数格和实际 Taylor determinant 接到同一 BC 度量，明确 finite credit 与源 index 抵消后的内在费用。238支付填点源的全尺度单射及真实单缺行余子式；239给出同一余子式的完整 CRT 整性、统一2/3整数内容，使安全费用 upper 改善为
\[
 a\le21/2-\log12.
\]
它们是实质成果；没有借不同 minor 的衰减，也没有以有限头替代全尺度证明。

239随后重查精确椭圆积分容量式，将原共同图 cap 收紧为
\[
 |\phi'(0)|\le\pi^3/2^{7/4}.
\]
在已付固定共同 BC metric、完整原 flag 和相同 height/HS 假设的证书类中，严格反证需要的阈值不超过3log(cap)，而上述已证费用 upper 仍高于它。因此本轮暂停其剩余 prime/图优化。**这是现有证书不足，不是实际最优费用 lower，更不是所有 CDT 方法失败。** 恢复此源须有跨过紧门槛的具体费用证明或一项真正超出当前证书类、可完整支付的新机制。

## 2. 全局路线比较

| 路线 | 已付的有效接口 | 首个未付核心关 | 本轮资源决定 |
|---|---|---|---|
| 原三函数直接 holonomy | 真实关系填点、全阶秩/flag、实际费用upper、紧全图cap | 更好的实际 primitive费用或新 metric/几何能量机制 | 暂停；不默认追加局部素数和参数轮 |
| 固定 M₀,₁₀ 七重积分 | 原 Fⁿω、十一通道、D₃的三禁坐标等价 | 原相对类全部n的 cut/边界证书，随后两 Tate 通道与投影指数 | 条件后备；所查对角 Euler parity 法已在原对象上被排除 |
| Catalan/c₄混合周期移植 | 旧源码的完整列池投影、全finite模型、增长prime非零及同对象mixed energy链 | 新目标的完整 integer nuisance projection与实际非零 | 保留架构；不复用旧 G 的seed/预算，不恢复固定背景填点 |
| conifold、非CM椭圆、形式 odd holonomy | 先前已证 regulator/PF或部分真实关系接口；DD formal自由性 | 目标敏感完整标记/共同图，或数值周期关系到整源的严格界 | 暂缓；深理论名称、formal非零不增加数值证据 |
| 新 logistic 全泛函混合矩阵 | 本轮支付任意固定有限odd ζ组合（可附ζ₂）的完整投影、同外场upper稳定性、增长的目标系数秩和完整安全整模型 | 同一完整 determinant 的 primitive Gauss费用和实际关系点无限非零 | **唯一有界主线：先3ζ₃+ζ₅，暂不扩权** |
| 低权 K=2G−(π/2)log2 | 本轮新给真实端点投影/native填点及全部素数幂 d_Nd_floor(N/2) 模型 | 真实多叶共同map及严格秩余量；已有两张缩放图不足 | 有条件备用；不自动开图搜索 |

这个选择修正了236的自动后备预设。本轮新的一手完整关系机制，比尚未支付原投影的七重积分更靠近一个可以直接否证或通过的整模型关。各路线的已付部分保留，不混用它们的非零、分母或最小指数。

## 3. 本轮新数学：统一接口，但尚不是统一定理

取 t=1/2+iy、ρ=(π/2)sech²(πy)，B(G)=∫G(t)ρdy。对固定有理系数的有限组合
\[
 X=c_2\zeta(2)+\sum_{k\ge3\ {\mathrm{odd}}}c_k\zeta(k),\quad
 U_X(f)=B\left[\left(-c_2+
 \sum_{k\ge3\ {\mathrm{odd}}}\frac{c_k}{(k-1)!}\partial_t^{k-2}\right)(tf)\right],
\]
本轮重新纸证完整公式
\[
 U_X((t+j)^{-1})=jX-j\left(c_2H_j^{(2)}+
 \sum_{k\ge3\ {\rm odd}}c_kH_j^{(k)}\right)-c_2,
\]
多项式商部的值则是有理 Bernoulli 导数组合。因此对仅有这些简单极点的整个所需空间，X∈Q使**完整矩表**有理，不遗漏其它ζ通道。

固定阶微分转到密度后，W_X是ρ乘tanh的固定多项式，|W_X|≤C_Xρ。对同一 R_n=D_n⁴/D_(5n)、3n×3n矩阵，其 absolute Heine上界只多 exp(O_X(n))，所以leading n²实处外场率不因所选固定有限组合改变。原来源的 −6 常数须保留其完整 FstarInput 证书；本轮选读不能当成独立认证该全部数值输入，更不转移 primitive 内容或 prime-edge 非零。

目标系数 a_e=Σ_j j residue(t^eR_n,−j)满足 a_e=0（e<n−2）、a_(n−2)=−1。其左上(n−1)阶 Hankel块反三角且 determinant非零，所以目标系数 rank≥n−1。这排除228的秩一目标系数正 Gram假设；**没有证明完整矩阵秩或目标值非零**。

主选 X=3ζ₃+ζ₅ 对应 U_X=B[(3/2)∂(tf)+(1/24)∂³(tf)]。完整 residue factorial式及 Bernoulli 分母定理给
\[
 (24S_nd_{5n}^5)^{3n}Q_{X,n}(T)\in\mathbb Z[T],\qquad
 S_n=(5n)!/(n!)^4.
\]
全部行列、全部 determinant系数、全部 prime powers均包含。这是安全起点，不是足够小的 primitive费用。完整证明见[全泛函稿](global_logistic_whole_functional_bridge_round240_20261008.md)，投影/安全模型/增长秩另有 B、C 独立纸核。

另一项改变后备投入的证明来自原七重积分：精确转cubical后，ω=(x₂x₄x₆/Q)dx，F又含全部(1−x_i)。能保留Q的唯一非零对角Euler场在ω上的 numerator权重与divergence恰抵消；对每个n≥1，F的单坐标divisors又迫所有场系数为0。因此所查的新奇维 primitive机制不能移植到**原 Fⁿω**。这没有反驳一般D₃/relative投影。[原对象证明](global_period_projection_review_round240_20261008.md)。

## 4. 当前仓库与新文献确实改变了哪些判断

本轮 fresh只读核查 E:/codex-build/math：本地 HEAD、public ls-remote HEAD/main均为 fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status为空，与236基准相同，没有需同步的新commit。没有fetch/reset/外仓库写入。

在实际读取的README/history/定向目录与相关正文范围中，Catalan稿给出单个G无理性声明；Deligne–Drinfeld仍是形式Lie自由性，odd ζ深度一系数的非零只用ζ(n)>0。它不成为全部odd ζ数值无理性的证明。没有依据这些限定读域认定全球不存在其它结果，也没有本轮全仓库或Lean认证。Catalan可移植的实质是完整投影→整数列过滤→完整有限处→增长尺度非零→同一mixed energy链。

仓库之外出现了值得跟进的一手输入：[Tang构造](https://github.com/dtq1997/zeta2-zeta3-linear-independence)声明1、ζ₂、ζ₃的Q-LI；[Lai v1](https://arxiv.org/abs/2610.06838v1)声明1、ζ₃、ζ₄的Q-LI并展示double-pole混合泛函与局部矩阵整除的机制。本轮读其限定核心，未重新认证其全部proof/内核。它们均不覆盖主选3ζ₃+ζ₅，也不由这些声明推出ζ₇无理。本文不从限定搜索未命中推主选的全球新颖性。相关PDF、原源码及读取范围已保存literature。

## 5. 241–244的唯一主窗口与退出条件

**241只做一项首证书：** 固定上述 R_n、U_X、完整3n列池，在 n=p−1上推全部局部块和primitive reduction，检验能否给一个对充分大prime成立的固定阶非零证书。必须保留全部调和头、多项式商部、所有残数、边界及原目标polynomial；不照搬 Tang K3 的 −2层、Catalan的三个48阶seed，也不以小prime样本推无限非零。

随后仅在该证书产生实质输入时，支付同一归一化的全系数 Gauss费用。一个明确充分出口是：无界尺度上 P_(X,n)(q)≠0（每个固定q∈Q），log|d_(X,n)|≤(6−ε)n²+o(n²)，以及同一原实处证书经完整认证的转移。这样 degree O(n) 的目标分母只付O(n)，才有趋零非零整数反证。**三项现在都不能预领。** 可接受另一个完全支付的同对象严格判据，但不能换对象后沿用这里的预算。

连续两轮未缩小实际非零或primitive费用的核心缺口，提前做方向检查。244前仍只有安全LCD、generic秩或有限头，则停止该源的局部优化，不自动扩大权/参数。ζ₇作为较高权同框架后备；原M₀,₁₀只在全n相对投影首关有新证书时恢复主资源。

正式复盘计数从240重启：下一次默认246，允许244–248，最迟248；普通战术检查不重置。每轮继续报告已付投影、已付整模型、已付无限非零和数值结论，明确下轮一个门槛。研究目标仍active。

## 6. 核查范围与本轮状态

本轮数学程序、参数扫描、旧producer重跑、Git mutation、Lean执行均0。新数学均纸证；文献下载、源码读取、PDF选页提取与归档是文档操作。Root FULL读239最终报告/manifest/policy、236/228三份全局比较、227停止稿、本轮三条路线稿和新全泛函稿；本轮新Tang源码14个选定文件已FULL读。没有把目录检索、README声明或import链当作独立数学认证。

证据范围、fresh仓库状态、来源身份和独审另存本轮literature及review receipts。新数值定理0；新接口已改变下一步方向，尚不能称全部odd ζ或类似常数的通用无理性方法。
