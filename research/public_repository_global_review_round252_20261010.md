# 第252轮：公开成功机制与一个新的 χ−8 周期投影首关

2026-10-10，A；纸面数学，数学程序0。当前 χ−7 Fricke 源的默认投入结束；这里不继续其填叶、地图或素数优化。本文没有新的数值无理性定理。

## 1. 当前公开状态与已知出口

本轮只读检查 `E:/codex-build/math`：HEAD、远端 HEAD 和 `refs/heads/main` 均为 `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`，porcelain 状态为空。没有 fetch、reset 或外仓库写入。官方 [openai/math](https://github.com/openai/math) 页面与本地 README/history 相符：作者列719篇、372个家族；history 的最新修订为2026-10-07。其 formalization 比例是作者声明，本轮没有运行 Lean 或认证全仓库。

这与第240轮采用的 snapshot 相同。本轮完整读取 README/history，按 CONTENTS 关键词定位；没有在这个实际读域找到新增的“所有奇数 ζ 已解决”结论。目录中的 Deligne–Drinfeld 形式结构、Dirichlet 零点区域及 BSD 公式不能当作未知特殊值的数值线性无关性。搜索和目录定位不证明全球文献没有别的结果。

Catalan 是本项目已有 baseline；ζ(5) baseline 来自独立 Fauzan/mo271 来源，不能归给 OpenAI math。Prellberg 的 [arXiv:2609.06895v1](https://arxiv.org/html/2609.06895v1) Theorem1.1 已声明三个有理参数 dilogarithm 的无理性；本轮不把这三个数重新选为新目标。

## 2. 成功证明真正移植的对象

本轮完整读 Catalan 的 foundations、nonvanishing、real-place、introduction、conclusion，并读 odd-primes 最终有限处命题及其完整证明。其关键接口是：混合矩的整列接触恒等式消除 ζ(2) 通道；增长行列式的非零由 Frobenius 与两个 palindromic 基归约到三个固定矩阵；实处使用两叶积分、统一插值和能量；有限处估计完整行列式。不能只搬一个端点值、正核或微分方程阶数。这里没有重跑固定矩阵证书，也没有全文独审 energy/certificate。

另一个不同机制是 Rhin–Viola 的系数级 factorial identities。Prellberg §3.2 在同一积分的两种展开中逐项选择局部变换；其收益涉及完整系数向量，有限数据有明确的全参数稳定性步骤。这不是“试到很大 n”就付无限结论。本文以下采用已发表的 [Rhin–Viola2005 Theorem2.1](https://www.numdam.org/item/ASNSP_2005_5_4_3_389_0.pdf) 作为输入，支付新的 cyclotomic 投影；不领取其有理参数解析余量。

## 3. 一个可以完全关闭的朴素 χ−8 Gram 入口

令 χ=χ−8，模8取值在1、3为1，在5、7为−1，偶数为0。记 Y=L(2,χ)。由绝对收敛幂级数及积分，

\[
Y=\int_0^1\frac{(-\log x)(1+x^2)}{1+x^4}\,dx>0,
\qquad I_j=\int_0^1\frac{x^j(-\log x)(1+x^2)}{1+x^4}\,dx,
\]
\[
I_{j+4}+I_j=\frac1{(j+1)^2}+\frac1{(j+3)^2}.                 \tag{P1}
\]

故每个四次幂矩都有全尺度身份

\[
I_{4k}=(-1)^kY+
\sum_{i=0}^{k-1}(-1)^{k-1-i}
\left(\frac1{(4i+1)^2}+\frac1{(4i+3)^2}\right).             \tag{P2}
\]

这已经给纯 Q+QY 的完整模型、指数级 prefix LCD，以及每阶正 Gram 非零；却没有改变周期系数秩。

具体取 t=x^4，正测度

\[
d\mu(t)=\frac{(-\log t)t^{-3/4}(1+\sqrt t)}{16(1+t)}\,dt
\ge\frac{1-t}{32}\,dt.                                  \tag{P3}
\]

对任意 m维 Q多项式空间 V，含1、次数≤D，取基 p_i。设 M=(μ(p_i p_j))、b_i=p_i(-1)。P2 给完整形式

\[
G(X)=M+(X-Y)bb^T\in\operatorname{Mat}_m(\mathbb Q[X]),
\quad \det G(X)=P X-Q,\quad
P=\det M\,K>0,
\quad K=b^TM^{-1}b.                                     \tag{P4}
\]

评价点是 −1，不能直接套端点1的多项式 Christoffel 界。这里支付一个足够的指数界。令 B_j=binom(2j+1,j)，权1−t的首一正交多项式为

\[
q_j(t)=\frac{(-1)^j}{j!B_j(1-t)}
\frac{d^j}{dt^j}\{t^j(1-t)^{j+1}\},
\qquad \|q_j\|_{1-t}^2=\frac1{2(j+1)B_j^2}.
\]

分部积分给正交性及该范数。Leibniz 展开并用 Vandermonde 求和给

\[
|q_j(-1)|\le B_j^{-1}\sum_{r=0}^j
\binom jr\binom{j+1}{r+1}2^r\le2^j,
\]

因为不含2^r的和恰为B_j。因此，P3及有限维 Cauchy 不等式给

\[
K=\sup_{p\in V\setminus0}\frac{|p(-1)|^2}{\mu(|p|^2)}
\le32\sum_{j=0}^D\frac{|q_j(-1)|^2}{\|q_j\|_{1-t}^2}
\le256(D+1)^2 64^D.                                    \tag{P5}
\]

任意非零有理 scalar v，只要把完整多项式 v detG(X) 清整，vP 就是非零整数。因此

\[
|v\det G(Y)|=\frac{|vP|}{K}
\ge\frac1{256(D+1)^2 64^D}.                              \tag{P6}
\]

若D=O(m)，不存在严格 exp(−δm²) 的完整 scalar 整化收益。这包含最优共同系数约分和任意有理基变换，使用的是非零最高系数的必要整性，而不是安全 LCD 的 upper。当D=o(m²)时结论同样成立。它只关闭这一秩一正 Gram 类的严格二次预算，不关闭所有 χ−8 方法、次主阶方法或真正的 mixed source。与第228轮判据相比，新处是评价点−1及其完整界。

## 4. 一个不同的实际出口：八次根 RV 全系数投影

令 ζ=e^{πi/4}、τχ=Σ_{a=1,3,5,7}χ(a)ζ^a=i√8。绝对收敛给

\[
\sum_{a=1,3,5,7}\chi(a)\operatorname{Li}_2(\zeta^a)
=\tau_\chi Y.                                          \tag{P7}
\]

证明只需把内层有限和写成 τχχ(k)，再逐项求和；偶数k时内层为0。等价实身份为
Y=[Cl₂(π/4)+Cl₂(3π/4)]/√2。已有有理参数 Li₂ 定理不支付这个单位圆边界目标。

现在固定一个包，不做参数选择：n≥2，r=0,…,4，

\[
\nu_{n,r}=(h,j,k,l,m)=(10n+r,8n,8n,5n,10n).
\]

在 RV 的定义中 I_z=I_z^(0)−(log z)I_z^(1)。全部参数非负；其 Theorem2.1 的 H=13n+r、K=12n+r、α=16n、β=3n−r。令

\[
\Lambda_n=d_{13n+4}d_{12n+4},\qquad
F_{n,r}(z)=\Lambda_n z^{16n}(z-1)^{3n}I_z(\nu_{n,r}).
\]

个别 theorem identity 乘整数 LCM 比和 (z−1)^r 后得到 **完整右端**

\[
F_{n,r}(z)=P_{n,r}(z)-Q_{n,r}(z)\operatorname{Li}_2(1/z),
\qquad P_{n,r},Q_{n,r}\in\mathbb Z[z].                  \tag{P8}
\]

因此本包没有遗漏 Li₁ 或 log 通道；若改用未减去 residue 的 I_z^(0)，P8 不成立，不能实施以下投影。这里采用已发表定理，不声称本轮重证其全部前置算术引理。

对 z=ζ^(−a)，从 |z|>1 延拓并径向到达该点。Li₂(1/z) 采用单位圆内幂级数的连续边界值；P8 定义同一 canonical continued integral。所有点都不等于0、1。没有把复杂积分原实区间直接搬到单位圆。

写 Q_{n,r} mod(z⁴+1)=Σ_{j=0}³q_{j,r}z^j。若存在整数向量 v_n∈Z⁵，使

\[
\sum_rv_{n,r}(q_{1,r},q_{2,r},q_{3,r})=0,
\qquad c_n=\sum_rv_{n,r}q_{0,r}\ne0,                    \tag{P9}
\]

则 Q_n=Σv Q_{n,r} 在四个点都等于同一整数 c_n。取 P_n=Σv P_{n,r}，有精确整数形式

\[
\frac1{\tau_\chi}\sum_{a=1,3,5,7}\chi(a)
\sum_rv_{n,r}F_{n,r}(\zeta^{-a})=A_n-c_nY,
\qquad A_n\in\mathbb Z.                               \tag{P10}
\]

这里不需要额外的8或√2清整常数：若P_n(z)=Σp_kz^k，则

\[
\tau_\chi^{-1}\sum_a\chi(a)P_n(\zeta^{-a})
=-\sum_kp_k\chi(k)\in\mathbb Z.                        \tag{P11}
\]

完整 composite normalization 正是Λ_n、z^(16n)(z−1)^(3n)、整数向量v_n与最后的 χ-trace/τχ；每一项已显示。根处 z^(16n)=1，(z−1)^(3n) 仍是需要计入解析高度的真实因子。积分系数清整没有数域共轭遗漏，投影后输出在Q；但v_n的高度、共同 primitive content与积分小界仍须另付。

## 5. 唯一建议的253首证书及停止条件

P9尚未证明，对任何n都没有计算。三行矩阵必有整数 kernel 不意味着 kernel 能保留 c_n。确切判定是

\[
\operatorname{rank}_{\mathbb Q}(q_{j,r})_{0\le j\le3,0\le r\le4}
>
\operatorname{rank}_{\mathbb Q}(q_{j,r})_{1\le j\le3,0\le r\le4}. \tag{P12}
\]

rank4是充分条件，不是已付条件；不能以五列比三约束多作 generic 保证。建议253仅交付这个固定包在无界n上的实际 P12 证书，最好是系数提取/contiguous 恒等式，或证明其失败的结构原因。不得以有限头、任意换包或参数扫描替代。若这一关没有可核推进，停止本包；不自动开启若干轮地图或素数优化。

即使P12通过，也仅得到新的完整纯目标模型。仍未付：P10在无界n上的实际非零、v_n及所有系数的净 primitive 费用、四个复杂积分的统一严格解析余量。现有 Catalan 固定矩阵证书、RV 有理点小界及241 logistic 非零不能代替它们。新数值出口是Y的无理性，或另明确支付的更强关系；不是已知 Catalan/ζ(5)，也不以本文的有限文献读域证明全球新颖性。

B的 χ−8 截区 mixed-moment 模型是另一项完整投影资产；它复用了232/233架构，而且低区可以对所有g作数值 row-add 消去，不能据此领取关系专属能量。本轮不建议默认延长那个预算支路。若要保留一个与 Fricke 不同的入口，优先上述固定 RV 全系数投影首关。

## 6. 本轮验证边界

本人纸面逐式核P1–P12；没有数学程序、Lean 执行、数值扫描或外仓库修改。Catalan 的公布结论在此作为现有 baseline，不把作者程序表当作本人重新运行证书。RV完整 theorem statement 与证明终结接口已读，前置引理不是本轮全文重审；Prellberg只读所列完整关键节。精确读域、下载件及身份见同轮 `alternative_reading_scope.md`。本稿保存后本人再次完整读取；作者自读不冒充独立审计。
