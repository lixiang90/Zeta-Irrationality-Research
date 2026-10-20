# 第273轮：固定 Abel 来源的 Taylor 商清整与旧内容信用独审

2026-10-20，子代理 `primary_mechanism_273`。本稿只写该文件，不改状态账。开始时 goal 工具返回 null；273状态账进行中，`git status --short` 为空。实际全文读273任务、272结算、271报告及一手来源审计、272 Hermite结构稿、241和242两份算术稿；没有数学扫描、CAS或Lean执行。

**独审结论：根提出的整数值 Taylor 商机制适用于271的同一个实际来源，完整安全倍数可从272的 exp(O(m log m)) 降到 exp(O(m))；它也给原272整数多项式的全系数内容一个新的全尺度下界。未证明严格负本原净率。** 旧242付的是K5简单极点及Bernoulli泛函，不能说已支付本Abel来源的三层Taylor商、半步坐标和全部头。以下逐项核证根的新适配，不把通用初等恒等式说成新外部定理。

## 1. 整数节点的完整 Taylor 商

记 \(d_N=\operatorname{lcm}(1,\ldots,N)\)。若 \(f\in\operatorname{Int}(\mathbf Z)\)、\(\deg f\le E\)、\(k\in\mathbf Z\)，定义多项式算子

\[
T_kf(q)=\frac{f(q)-f(k)}{q-k}.
\]

整数平移保持整数值格，故 \(f(q)=\sum_{j=0}^E c_j\binom{q-k}{j}\)，其中 \(c_j\in\mathbf Z\)。对 \(j\ge1\)，精确有

\[
T_k\binom{q-k}{j}
=\frac1j\binom{q-k-1}{j-1}.
\tag{M1}
\]

因此 \(d_ET_kf\in\operatorname{Int}(\mathbf Z)\)。逐次应用同一结论，且次数只下降，得到

\[
d_E^sT_k^sf\in\operatorname{Int}(\mathbf Z),\qquad s=0,1,2,3.
\tag{M2}
\]

多项式在k取值的可去延拓给

\[
T_k^sf(q)=\frac{f(q)-\sum_{r=0}^{s-1}
f^{(r)}(k)(q-k)^r/r!}{(q-k)^s}.
\tag{M3}
\]

所以M3恰是 \(f(q)/(q-k)^s\) 的完整多项式商部，所有低次Taylor项都进入proper部分。若proper有理函数 \(R(q)=\sum_{k,s\le3}a_{s,k}(q-k)^{-s}\)，则 \(R(q)f(q)\) 的完整商部就是 \(\sum_{k,s}a_{s,k}T_k^sf(q)\)。这里先对固定R作部分分式，再乘整数值f；无需把f转成单项式整系数多项式。

## 2. 271唯一来源的全部 Euler 头

对象及所有符号与[271](global_budget_review_round271.md)、[272](abel_beta45_budget_round272.md)相同：

\[
n=2m-1,\quad q=t+m-\tfrac12,\quad
L_0=d_{4m-3},\quad C=8L_0^2,
\]
\[
f_i(q)=p_i((q+\tfrac12)^2),\quad
Cf_i\in\operatorname{Int}(\mathbf Z),\quad
d=6m-2,\quad E=2d=12m-4,\quad D=E-3.
\]

R的全部极点在q坐标是整数 \(-m,\ldots,m-1\)，最高阶3，且R proper。原部分分式数据满足

\[
2^{6n}a_{3,k}\in\mathbf Z,\quad
L_0g_k\in\mathbf Z,\quad 2L_0^2h_k\in\mathbf Z,
\quad a_{2,k}=a_{3,k}g_k,\quad a_{1,k}=a_{3,k}h_k.
\]

故 \(A_R=2^{6n+1}L_0^2\) 同时清除R的全部三层系数。对每个i,j，\(C^2f_if_j\) 是次数≤E的整数值多项式。由M2–M3，若 \(H_{ij}\) 是原 \(R_mP_iP_j\) 的商部，则

\[
A_RC^2d_E^3H_{ij}(q-m+\tfrac12)
\in\operatorname{Int}(\mathbf Z)\subset\mathbf Q[q],\qquad \deg H_{ij}\le D.
\tag{M4}
\]

Vandermonde恒等式及 \(4^r\binom{-1/2}{r}\in\mathbf Z\) 说明：对次数≤D的整数值多项式，代入 \(q=t+m-1/2\) 后乘 \(4^D\) 仍为原t变量上的整数值多项式。两次微分再付 \(d_E^2\)，由272 H13可逐次验证；Euler泛函的原t=0起点恒等式为

\[
\mathcal E\!\left(\binom tr\right)=\frac{(-1)^r}{2^{r+1}}.
\]

所以同一个整数

\[
\widehat S_m=A_RC^2d_E^5\,4^D2^{D+1}
=\boxed{2^{48m-19}L_0^6d_E^5}
\tag{M5}
\]

清除每个 \(\mathcal E(H_{ij}'')\)。它包括全部多项式商部，不仅最高项；\(m=1\)时E=8、D=5，各指数也合法。所付费用 \(\log\widehat S_m=O(m)\) 使用标准 \(\log d_N=O(N)\)，不需任何内容猜测。

## 3. 同一倍数清除全部有限头和目标栏

原完整乘积jet已给右半主部 \((A_{3,k},A_{2,k},A_{1,k})=(a_{3,k},3a_{3,k},0)\) 于对角，交叉项为零，左半由反射确定。实际有限调和头的非零奇分母最大为 \(2n-1=4m-3\)，幂次至多5；所以 \(2^{6n}L_0^5\) 已清所有头及目标系数192\(a_{3,k}\)。

M5中 \(L_0^6\) 包含这一奇素数费用，且 \(48m-19\ge6n\) 对全m≥1成立。因此全部有限头已由M5支付，无需再乘 \(d_{4m}^5\)：

\[
\boxed{\widehat S_mA_m,\ \widehat S_mB_m\in M_m(\mathbf Z).}
\tag{M6}
\]

这是一份完整同对象安全证书，不是最小分母、实际内容恰值或负净率。

## 4. 对272原内容的实际新下界

保留272的旧安全倍数及其原整数多项式：

\[
S_m=2^{12m+2}(d!)^2L_0^4d_{4m}^5,
\quad F_m=\Lambda_mQ_m,\quad
\Lambda_m=S_m^m|\det B_m|,\quad g_m=\operatorname{content}(F_m).
\]

271的同一个最小首一清整 \(\lambda_m\) 满足 \(g_m=\Lambda_m/\lambda_m\)。M6使
\(\widehat\Lambda_m=\widehat S_m^m|\det B_m|\) 成为正整数，且 \(\widehat\Lambda_mQ_m\in\mathbf Z[Z]\)，故 \(\lambda_m\le\widehat\Lambda_m\)。因此

\[
\boxed{g_m\ge\left(\frac{S_m}{\widehat S_m}\right)^m},\qquad
\boxed{\log g_m\ge12m^2\log m-O(m^2).}
\tag{M7}
\]

第二式由Stirling公式、\(d=6m-2\)及所有LCM对数为O(m)得到。比值不必是整数；M7来自同一个实际首一多项式的最小清整，并非凭有限样本猜gcd。它真实支付了原272阶乘来源的一整层内容，足以改变“完整商部目前只能付阶乘安全费”的证据状态。

进一步与272.10的同对象完整实际上界合并。由最小清整的上述不等式，

\[
\log\lambda_m+\log\det M_m-\log|\det B_m|
\le m\log\widehat S_m+\log\det M_m.
\]

使用标准 \(\log d_N=N+o(N)\)，M5给
\(\log\widehat S_m=(84+48\log2+o(1))m\)。因此

\[
\boxed{\log\lambda_m+\log\det M_m-\log|\det B_m|
\le[C_*+o(1)]m^2,\qquad
C_*=86+48\log2+12\log6>0.}
\tag{M8}
\]

原272完整安全upper含 \(12m^2\log m+O(m^2)\)，M8将同一完整本原净预算证书降为有限二次常数；这是一项全对象预算改善。M7–M8没有消掉剩余正二次费用，不产生数值可行准入或新无理性结论。只有同一归一化下严格负本原净率才准入数值实施。

实际去重读域还包括242 G10–G16及241 A1–A4；它们的有限整数评价/Newton技术可作方法背景，模型是K5/Bernoulli而非本稿M4–M6。外部有界检索选读[CMF 2507.08138v1](https://arxiv.org/html/2507.08138v1)引言、§2.3 Theorem2.1、§2.4 Definitions7–10/Theorem2.3及§5.1 Conjectures1–4，以及[factorial reduction原论文](https://link.springer.com/article/10.1007/s40598-024-00250-z)§§2.1–2.3的Theorems1–2及Conjectures1.1–1.4；这些未提供本固定来源的内容定理，未作为M1–M7的数学输入。Lai v2、旧H9和β有限集合结论未重新登记成新来源。
