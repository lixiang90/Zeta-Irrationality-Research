# level 20 Hasse 局部整格的独立审阅

日期：2026-10-06。审阅对象是 [Hasse 主报告](cdt_odd_level20_hasse_20261006.md) §§2–5 的实际书面证明；既有冻结文件不作修改。本稿确认一个局部指数改进，不宣称全局 CDT 成本下降或新的数值无理性定理。

## 1. 约化、Fricke 下降和除子

独立计算
\[
\operatorname{disc}(1-12t+28t^2-32t^3+16t^4)=-2^{16}5^2.
\]
因此全部 \(p\ge7\) 下四个分支值互异，二阶商 tame，三个 cusp 值 \(0,1,\infty\) 不碰撞。\(X_0(20)\) 的好约化与冻结模型的 \(Z^2=\Delta(t)\)、\(dt/Z=B\,dq/q\) 一致；后者是 genus-one 曲线的处处非零微分。这也说明 \(B\) 在约化中仍只在六个 cusp 各有一阶零。

\(E_{p-1}^{\rm std}\) 是 \(p\)-integral，其 reduction 是 q-expansion 为1的 Hasse section。Fricke 把其平方与 \(B^{p-1}\) 的比值变成
\(20^{p-1}E_{p-1}^{\rm std}(20\tau)^2/B^{p-1}\)；同权 q-expansion principle 与 \(20^{p-1}=1\bmod p\) 给实际下降。

于是 \(\mathcal H_p=P_p/[t(1-t)]^{p-1}\) 的三个商 cusp 极点均为 \(p-1\)，所以 \(\deg P_p=3(p-1)\)。以 \(t=q+O(q^2),B=q+O(q^2)\) 规范化，\(P_p(0)=1\)。非 branch 根的重数为偶数，最多四个 branch 根可以贡献奇数重数，故
\[
\deg\operatorname{rad}P_p\le\frac{3(p-1)+4}{2}.
\]
这个上界不需要额外假定所有 Hasse 零简单。主证书的“重数至多2”固定样本检验是更强的附加信息。

另直接核验了 Katz 作者原稿 [*On a question of Zannier*](../literature/katz_on_a_question_of_zannier.pdf) PDF p3 的 \(E_{p-1}\) 整性与 p4 Theorem 3.1 的 Hasse 识别及 q-expansion principle。其 [作者原件](https://web.math.princeton.edu/~nmk/zannier8.pdf) 和 [独立 manifest](../literature/manifest_cdt_odd_hasse_review_20261006.json) 已存入文献库；未在缺乏出版记录时赋予它猜测日期。它支持 Hasse 输入，不代替本项目的 level20 除子推导。

## 2. 对数微分和算子次数

由 \(\mathcal H_p=B^{1-p}\) 的实际形式级数，
\[
B'/B=P_p'/P_p+1/t-1/(1-t)\quad\bmod\mathfrak p.
\]
冻结模型的 \((A/B)^2=N^2C/[25t^2(1-t)^2]\) 给两个 cusp 项的精确抵消，得到主稿式(4)。以
\(Q_p=\operatorname{rad}P_p\)、\(V_p=Q_pP_p'/P_p\)、\(D_p=NCQ_p\) 清分母，主稿的 \(M_p\) 正确。

这里必须使用 \(\vartheta=t\partial_t\)，而非 \(\theta_q=q\partial_q\)。\(\vartheta\) 不增加多项式次数，也不把截断外的系数向低次移动。两个关系向量
\[
(-M_p,D_p,0),\qquad
(-\vartheta M_p,\vartheta D_p-M_p,D_p)
\]
均有次数至多 \(\delta_p=\deg D_p\le(3p+9)/2\)。从第三坐标及第二坐标依次比较，证明它们的任意两个多项式倍数在 \(k[t]^3\) 中独立。

## 3. 完整最高 packet

对 \(1\le j<p\)，\(E_4\) divisor sum 中含 \(p\) 的新项具有 \(p^3\) 因子；\(F_4\) 不含该因子的项多出 \(\chi_5(p)\)。oldform 的2、4 dilation 与 \(p\) 互素，故两份 source 具有主稿 §4 的完整 packet。

整数反演 \(q(t)\) 给 \(q(t)^p=q(t^p)\bmod p\)，而不涉及对 \(r=\sqrt5\) 的未知周期作用。仅对指数 \(<p^2\) 的前缀，乘 \(p^3\) 后可 reduction；在反证假设 \(c\in\mathbb Q\) 且排除其固定分母素数后，周期常数项 reduction 为0。因此
\[
p^3H=A(t)F(t^p)\quad\bmod(\mathfrak p,t^{p^2})
\]
正确。\(F(0)=0\)，且 \(\vartheta F(t^p)=0\)，两个算子遂消掉整个最高层。普通 \(\partial_t\) 会改变截断范围；主稿选 Euler 算子避免了这个问题。

## 4. 两个有限秩上界的直接证明

固定主稿 §5 的 \(p<N<p^2\)，用 \(d\) 表示辅助多项式次数上界，避免与算子分母 \(D_p\) 混淆。设
\[
a=\vartheta A/A=M_p/D_p,\qquad
b=\vartheta^2A/A=\vartheta a+a^2
 =\frac{(\vartheta M_p)D_p-M_p\vartheta D_p+M_p^2}{D_p^2}.
\]
第二个分子的次数至多 \(2\delta_p\)。因为 \(P_p(0)=1\)，\(Q_p(0)\ne0\)，从而 \(D_p(0)\ne0\)，公共分母在原点可作级数逆。

任意 \(P_i\in k[t]_{\le d}\) 的最高层像为
\[
\frac{A(t)F(t^p)}{D_p(t)^2}\left[
P_0D_p^2+P_1M_pD_p+
P_2\{(\vartheta M_p)D_p-M_p\vartheta D_p+M_p^2\}\right].
\]
括号中的多项式次数至多 \(d+2\delta_p\)。故该像空间维数至多 \(d+2\delta_p+1\)；无需假定 \(F\) 是 unit 或该乘法为单射。

同时 \(F(0)=0\)，所以全部像从 \(t^p\) 开始；在 \(k[t]/(t^N)\) 中只有 \(N-p\) 个可用坐标，故秩至多 \(N-p\)。若某 embedding 的 leading packet 偶然再次消失，只会增强这个上界。结合源空间维数，即得到主稿式(10)的三个上界。

\(d\ge\delta_p\) 时，两关系向量各乘次数至多 \(d-\delta_p\) 的多项式，给 \(2(d-\delta_p+1)\) 个独立 kernel 方向，与公共分母上界一致。

## 5. 整格指数和适用范围

所有 \(n<N<p^2\) 的系数 valuation 原先至少为 \(-3\)。kernel 的逆像恰是使其至少为 \(-2\) 的 coefficient lattice；\(p\) 在 \(K\) 中未分歧，故 \(p^3\) 后 reduction 为0 与这个 valuation 条件等价。因此
\[
[E_d:\Lambda_{\mathfrak p,d,N}]
=\operatorname{Norm}(\mathfrak p)^{r_{p,d,N}}
\]
精确成立。split 与 inert primes 都按 residue field \(k\) 同样证明。有限多个不同素理想条件可在同一个实际 \(\mathcal O_K\) coefficient lattice 上 CRT 拼接，指数相乘。

审阅结论：实际正文 §§2–5 通过，无需数学修改。本文没有运行或改写 root 的63项 producer；独立计算和证明核验的范围如上。这个局部界只涉及一个实际三元组的前缀，不免费增加函数秩，也不直接修改完整 CDT 的 \(\tau\)。root §6 列出的源格 determinant、分次评价高度、剩余 valuation 层和 tensor compatibility 仍是实质缺口。
