# 第276轮：实际 Euler–Newton 系数的实处有限率改进

2026-10-20。独立实处子任务，只写本文件。开始读取实际 goal（本子代理返回 `null`）、核工作树初始干净、运行 `research_state.py show`，恢复 AGENTS、长期目标、276章程和275/270/269所指定证据。账中的 active 未被当作恢复某个暂停 goal 的授权。没有运行 m、prime 或参数扫描。

**结论：没有证明裸 \(Q_m(X)\) 的全序列非负二次 liminf，也没有证明 \(R_m\succeq0\)。新付的是同一实际对象的有限 m 实处 upper，以及由它得到的准确二次率改进：**

\[
\limsup_{m\to\infty}m^{-2}\log\det M_m
\le 16\log2+1+32\mathfrak h(1/4).
\tag{R1}
\]

旧 upper 是 \(25\log2+32\mathfrak h(1/4)\)，故严格下降 \(9\log2-1>0\)。这是实际 Euler 插值数据与 Newton 恢复一起给出的全尺度安全 upper；其常数仍为正，不能排除或证明任何负二次子列，不能据此续开已限定的一轮窗口。

## 1. 原对象、数值目标和完整反证

固定 [269 G4–G7](global_source_review_round269.md) 唯一基底，保持

\[
n=8m,\quad N=8m-1,\quad M=4m-1,\quad s=2m,
\qquad p_i(z)=z^i+z^{4m}v_i(z),\quad 0\le i<m.
\]

实际正 Gram、首一多项式与最小清整均不变：

\[
g(T)=(-\log T)(2+1/(2\sqrt T)),\qquad
M_m=\left(\int_0^1
\frac{p_i(1+T)p_j(1+T)}{(1+T)^{8m}}g(T)\,dT\right)
=R_m+XI_m>0,
\]
\[
X=\zeta(2)+2G,\qquad Q_m(Z)=\det(R_m+ZI_m),\qquad
\lambda_m=\operatorname{den}(Q_m)\in\mathbf Z_{>0}.
\]

完整反证始终是实际 \(X=u/v\)、\(u\in\mathbf Z\)、\(v>0\)、\(\gcd(u,v)=1\)；此时
\(0<v^m\lambda_mQ_m(X)\in\mathbf Z\)。所需出口是同一预定无界子列上

\[
\limsup m^{-2}\log|\lambda_mQ_m(X)|<0.
\tag{R2}
\]

本子任务首命题是利用真实 Euler 约束裁决裸 Q 的必要衰减；若不能裁决，准确记录同对象 finite-rate 改进与未付接口。停止条件沿276章程，最多一完成轮，不把上包络改善自动升级为数值准入。

新规范固定为

\[
\Lambda_m^{\rm row}
=2^{30m^2}d_{16m}^{\,2m}\prod_{i<m}d_{N-i}^{\,2},\qquad
c_m^{\rm row}=\operatorname{content}(\Lambda_m^{\rm row}Q_m),
\]
\[
\lambda_mQ_m(X)=\Lambda_m^{\rm row}\det M_m/c_m^{\rm row}.
\tag{R3}
\]

275已领旧内容信用不再扣除。若只使用本稿的改进 upper，额外内容充分门槛相应降为下文R12；仍未付该内容。

## 2. 保留实际第 i 行的 Euler 数据

沿 [270 Euler公式 E1–E4](growing_pole_euler_inverse_round270.md)，置

\[
b_r(\alpha)=(-1)^r\binom\alpha r,\quad R_i=N-i,
\quad H_i(\alpha)=[z^M]v_i(z)(1-z)^\alpha,
\quad F_i(x)=H_i((x-1)/2).
\]

节点为 \(j=0,\ldots,s-1\)、\(\alpha_j=(j-1)/2\)。实际数据是

\[
F_i(j)=c_j/2,\qquad F_i'(j)=-b_{R_i}'(\alpha_j)/4,
\]
\[
c_{2k}=b_i(k)-b_{R_i}(k-1/2),\qquad c_{2k+1}=b_i(k).
\tag{R4}
\]

记 \(\mathsf H_a=\sum_{h=1}^a1/h\)、\(\mathsf H_0=0\)，并定义

\[
B_{m,i}=\binom{m-1}{i}\ge1,\qquad
C_m=2^{s-1}\binom N{s-1}.
\]

因为整数 \(0\le k<m\) 满足
\(|b_i(k)|=\binom ki\le B_{m,i}\)（\(k<i\) 时为0），而270已证
\(|b_{R_i}(k-1/2)|\le1\)，所以

\[
|c_j|/2\le B_{m,i}.
\tag{R5}
\]

这一步利用真实第 i 行数据，不能把 \(\binom{m-1}{i}\) 错写成 \(2^i\)。同一原证书给所有节点
\(|b_{R_i}'(\alpha_j)|/4\le\mathsf H_{2N+1}\)。连续整数 Hermite 基仍满足
\(|\ell_j(x)|\le C_m\)、\(|\ell_j'(j)|\le\mathsf H_{s-1}\)，对全部整数 \(1\le x\le N\) 成立。

因此，把R5直接代回270 E3，而非先采用共同最高行数据，得到明确有限量

\[
E_{m,i}:=sC_m^2
\left[B_{m,i}(1+2N\mathsf H_{s-1})
+N\mathsf H_{2N+1}\right]
\]
及

\[
|F_i(x)|\le E_{m,i}\qquad(1\le x\le N,\ x\in\mathbf Z).
\tag{R6}
\]

这里只估计固定原插值解，没有另选 Hermite 数据或正交多项式。

## 3. Newton 恢复须按系数阶保留 \(2^r\)

270 E4逐系数恰为

\[
[z^{M-r}]v_i(z)
=(-1)^r\sum_{t=0}^r(-1)^{r-t}\binom rt F_i(2t+1),
\quad 0\le r\le M.
\]

由R6立刻得到

\[
|[z^{M-r}]v_i|\le2^rE_{m,i}.
\tag{R7}
\]

旧 E9先把全部 \(2^r\) 统一为 \(2^M\)，再在 \([1,2]\) 上对每个系数付 \(z^{M-r}\) 的最坏放大，丢失了这两个因子的互补性。本稿保留R7再求值，不把一个正 upper 当作实际增长。

原 G5最高 m 个系数仍给 \(\deg v_i=M-i\)。于是对每个实际 \(1\le z\le2\)，

\[
\begin{aligned}
|v_i(z)|
&\le E_{m,i}\sum_{r=i}^{M}2^r z^{M-r}\\
&\le(M-i+1)2^M E_{m,i}.
\end{aligned}
\tag{R8}
\]

最后不等式只用了 \(2^rz^{M-r}\le2^M\)。原积分的实际函数为
\(q_i(z)=p_i(z)/z^{4m}=z^{i-4m}+v_i(z)\)，故

\[
|q_i(z)|\le A_{m,i}:=1+(M-i+1)2^M E_{m,i}.
\]

利用 \(\int_0^1g(T)\,dT=4\)，Hadamard给全 m 的同对象 finite-rate bound

\[
\boxed{0<\det M_m\le4^m\prod_{i=0}^{m-1}A_{m,i}^2.}
\tag{R9}
\]

R9没有把 \(p_i\) 换成达到单首极小范数的辅助多项式，也没有改变Gram空间、坐标、权或尺度。R5–R9的新信用来自实际Euler数据和Newton变换，不是重证270已sharp的单首下界。

## 4. 二次率与完整本原 upper

Stirling给

\[
\log C_m=2m\log2+8m\mathfrak h(1/4)+O(\log m).
\]

因 \(B_{m,i}\ge1\)，R6/R8中的其余因子只贡献统一 \(O(\log m)\)，故

\[
\log A_{m,i}
=8m\log2+16m\mathfrak h(1/4)+\log B_{m,i}
+O(\log m)
\tag{R10}
\]

在全部 \(0\le i<m\) 上一致。另一方面

\[
\sum_{i=0}^{m-1}\log\binom{m-1}{i}
=m\log((m-1)!)-2\sum_{i=0}^{m-1}\log(i!)
=\tfrac12m^2+O(m\log m).
\tag{R11}
\]

把R10–R11代入R9即得R1；特别是误差为 \(O(m\log m)\)，没有有限样本拟合或交换不一致的行极限。

与275的 \(\log\Lambda_m^{\rm row}=(47+30\log2)m^2+o(m^2)\) 合并，并仅使用 \(c_m^{\rm row}\ge1\)，得到新的完整安全净上包络

\[
\boxed{\limsup m^{-2}\log|\lambda_mQ_m(X)|
\le C_{\rm row}^{\rm new}:=
48+46\log2+32\mathfrak h(1/4)>0.}
\tag{R12}
\]

它比275的 \(47+55\log2+32\mathfrak h(1/4)\) 严格下降 \(9\log2-1\)。所有算术费用仍是原已审的R3；本稿未证明或重复领取任何新 \(c_m^{\rm row}\) 内容。若沿此 upper 给充分负预算，仍需额外内容信用严格超过R12，或另付实际实处改进。

## 5. 未解决的 lower 与尝试范围

本稿保留270的全序列下界

\[
\liminf m^{-2}\log\det M_m
\ge-8\log(3+2\sqrt2)-14\log2<0.
\]

它没有改善为非负，故 \(\lambda_m\ge1\) 暂不能据此排除全部负二次无界子列。R1/R12是正的 upper，亦不能承担该排除结论。完整反证与实际全 m 非零保持，但严格净率R2未付。

对真实Euler额外约束，纸面另得到精确残差分解：令 \(\mathcal H_m\) 是上述 \(2m\) 节点的值/导数Hermite插值算子；令 \(J_i\) 为次数≤\(4m-1\) 的唯一多项式，在两节点 \(k-1/2,k\) 都取值 \(b_i(k)\)，且两处导数均为0。由于 \(b_{R_i}(k)=0\) 对全部 \(0\le k<m\) 成立，R4等价于

\[
H_i=\tfrac12\{J_i-\mathcal H_m b_{R_i}\}.
\tag{R13}
\]

进一步，\(J_i'\) 被
\(\Omega_m(\alpha)=\prod_{j=0}^{2m-1}(\alpha-(j-1)/2)\) 整除；若 \(J_i'=\Omega_mS_i\)，则
\(\deg S_i\le2m-2\)，且每个半步区间
\(\int_{k-1/2}^{k}\Omega_mS_i\,d\alpha=0\)。这些是实际插值恒等式；本稿没有从它们导出原实区间Gram的正核或 \(R_m\succeq0\)，不把Hermite平方基或逐行符号直接当作矩阵正半定。

还曾考虑全半轴Mellin有限部的正性桥，但在 \(\alpha=1+\varepsilon\) 展开
\(\pi/\sin(\pi\alpha)=-\varepsilon^{-1}-(\pi^2/6)\varepsilon+\cdots\) 时，\(-\partial_\alpha\) 的有限部除周期项还含二阶Euler导数的有理项；G6只直接杀一阶项，不能删去二阶项。故未把该提案写为全半轴正性定理或det lower。这一纠错不影响R4–R12。

本子任务准确结算为：新增真实固定对象的全尺度 finite-rate upper 改善，未获数值准入，未裁裸Q的全部负二次子列；R PSD/尾正核/额外本原内容均未付。仅此 upper 改善不足以延长276一完成轮的期限。无新无理性定理，也无全部本原方法的 no-go。

## 6. 对276根结算、277章程和另一作者积分式的交叉审查

同日按根要求，只读全文核[276根结算](growing_pole_primitive_round276.md)、[277章程](source_gate_charter_round277_20261020.md)及[独审稿](growing_pole_independent_round276.md)，未修改它们或状态账，没有开始277数学窗口。本稿R1–R13为本作者贡献，本次不将自己的实处证明重新记作独审；下列I276.2–4是另一作者的推导，已独立重建。

逐单项式核I276.2：若 \(v_i\) 的一项为 \(v_{ih}z^h\)，则 \(r=M-h\ge i\)，而
\[
\int_1^\infty(z-1)^\alpha z^{-r-1}\,dz
=\Gamma(\alpha+1)\Gamma(r-\alpha)/\Gamma(r+1)
\]
在 \(-1<\alpha<r\) 收敛。反射公式乘 \(-\sin(\pi\alpha)/\pi\) 恰给 \(b_r(\alpha)\)。另一项 \(z^{-(4m-i)}z^{-4m}\) 对应 \(r=N-i\)，故全部项共同的开带确为 \(-1<\alpha<i\)。在该带的紧子区间上，端点幂乘任意固定次数log有统一可积包络，所以所需一次参数求导合法。

从原E1另核 \(K_i=2H_i+b_{N-i}\) 在整数/半整数节点的数据：\(K_i(k)=K_i(k-1/2)=b_i(k)\)，两处 \(K_i'\) 都是0。写 \(K_i=c(\alpha)J_i^{\rm tail}(\alpha)\)、\(c=-\sin(\pi\alpha)/\pi\)。在整数 \(k<i\)，\(c(k)=0\)、\(c'(k)=-(-1)^k\ne0\)，所以零导数给整数零矩，未除以零。半整数处 \(c'=0\)、\(c=(-1)^k/\pi\ne0\)，故零导数给log零矩；当 \(k<i\) value为0，当 \(k=i\) value为 \((-1)^i\)，恰给归一化积分 \(+\pi\)。半整数 \(k\le i\) 全在收敛开带内。I276.2–4及 \(i=0\) 的边界说明均正确。

根276.3/276.4的率合并也正确：有限处安全率 \(45+30\log2\) 加本稿裸upper \(16\log2+1+32\mathfrak h(1/4)\)，恰为 \(46+46\log2+32\mathfrak h(1/4)\)。相对275下降 \(1+9\log2\)，即新内容2与实处 \(9\log2-1\) 之和，没有重扣275旧内容。276.5从旧裸lower加同一新安全费率得到，仍只给未约内容安全族及必要剩余内容门槛。本次未重证有限处稿C6–C18的全部素数幂链，不继承其它作者的该部分独审标签。

对有限部纠错另独立展开：\(-\partial_\alpha\{\pi G(\alpha)/\sin(\pi\alpha)\}\) 在1处的有限部是 \(G''(1)/2+\pi^2G(1)/6\)，权中2倍给 \(G''(1)+2\zeta(2)G(1)\)。由 \(f_r(\alpha)=[z^{r-1}](1-z)^{\alpha-1}\) 可直接核 \(f_r''(1)=[z^{r-1}]L^2\)，所以额外 \(C_{L^2}\) 确未由G6删除。根所列反例有限部为 \(-1+6-1=4\)，符号和范围正确；它仅否定一般有限部保号推理，不是原G5反例。根对收敛约束作用于signed函数、域延伸至z>2、固定m2样本不升级为全m以及裸lower未决的限定准确；本次未重跑样本producer。

最后核1/1到期和277入口：新完整upper改善可登记本轮预算进展，但不自动延长期限。因首一Q给 \(\lambda_m\ge1\)，在**固定当前正裸upper包络**下，把全部安全费用约尽也只剩这个正upper，故仅继续减费不能用该证书闭合严格负预算。此处是证书能力的限制，不是实际裸率非负或全部内容方法的数学排除。277明确要求新全尺度真实实率机制或已经闭合的同对象负预算，且保留旧source关闭范围，未把该限制扩大成全方法no-go。此审读未发现需修正的数学、量词或到期条款。
