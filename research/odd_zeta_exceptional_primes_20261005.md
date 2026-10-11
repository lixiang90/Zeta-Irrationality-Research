# q=7 异常素数：有限域表示、反射分类和可用的平均接口

日期：2026-10-05。本稿另存，不改冻结的候选、算术、鞍点或其复核稿。
结论是第一层异常块的精确代数表示、逐项反射零点的全尺度分类、
一个完整 scalar Lucas 路线的反例，以及可与实侧大值结合的条件双计数引理。
**没有证明所需的异常素数密度界，亦没有新增无理性结果。**

相关资料存在撤稿问题：Ghosh–Ward 的 arXiv:1601.06765 最新 v4
于 2020-04-23 撤稿，原始页面的理由是
“Errors in paper uncorrected. Kenneth Ward passed away June 2019”。
本轮归档的 v2 仅用于历史与适用范围审计，**其任何定理均未作为输入**。
这是整篇论文的后续状态，不能把旧 v2 独立标成已经可靠验证的根数定理。
见[原始最新元数据](https://arxiv.org/abs/1601.06765)、
[本地 v4 HTML](../literature/ghosh_ward_arxiv_v4_metadata_20261005.html)和
[历史 v2 PDF，后续撤稿](../literature/ghosh_ward2016_truncated_hypergeometric_v2_withdrawn.pdf)。

## 1. 研究对象及不应混淆的两层问题

沿用[冻结算术稿](odd_zeta_log_arithmetic_20261005.md)的记号：
\[
a_r=\binom{7n}{r}\binom{n+r}{n}^{7},\qquad
B_n=\sum_{r=0}^{7n}a_r,
\]
取素数 \(p>7\)、\(n<p\le7n\)，写
\[
7n=Hp+d,\quad 1\le H\le6,\quad0\le d<p,
\quad m=p-n-1,\quad e=\min(d,m).
\]
实际整数块为
\[
C_{n,p}=\sum_{s=0}^{e}\binom ds\binom{n+s}{n}^{7}.
\tag{1}
\]
因为 \(7n<7p<p^2\)，前稿的 Lucas 与最高分母层公式适用：
\[
B_n\equiv2^H C_{n,p}\pmod p,\qquad
p^7S_n\equiv\kappa_H C_{n,p}\pmod p.
\tag{2}
\]
其中 \(\kappa_H\) 是六个固定非零有理数。除去固定有限坏素数，
\(C\ne0\) 保证实际有理分母及本原候选根支付七层。
\(C=0\) 只表示**第一层共同消失**；不能据此断言实际本原分母损失七层。
[新的第二 jet 稿](odd_zeta_log_primitive_20261005.md)已经给出
\(v_p(q_n)=\max(0,7+v_p(B_n)-v_p(p^7S_n))\)，并恢复部分非单位情形。
本稿控制第一层的目标是一个安全充分条件，不替代该更精确接口。

## 2. 参数完全匹配的两个多项式

由 \(n+1\equiv-m\pmod p\) 得
\[
\binom{n+s}{n}\equiv(-1)^s\binom ms\pmod p,
\quad
C_{n,p}\equiv\sum_{s=0}^{e}(-1)^s\binom ds\binom ms^{7}.
\tag{3}
\]
所有 \(0\le s\le e\) 的项非零。记 \((x)_s=x(x+1)\cdots(x+s-1)\)，
在 \(\mathbb F_p[Z]\) 定义普通 Pochhammer 截断多项式
\[
F_{n,p}(Z)=\sum_{s=0}^{e}
\frac{(-d)_s(n+1)_s^7}{(s!)^8}Z^s.
\tag{4}
\]
则 \(C_{n,p}=F_{n,p}(-1)\)（模 \(p\)），这是终止的 \({}_8F_7\)，
上参数为 \(-d,n+1,\ldots,n+1\)，下参数七个 \(1\)。
所有分母为单位；系数递推连同截断末端严格给出
\[
\theta_Z^8F_{n,p}
-Z(\theta_Z-d)(\theta_Z+n+1)^7F_{n,p}=0,
\qquad\theta_Z=Z\,d/dZ.
\tag{5}
\]

为计数**指标** \(n\) 的零点，需要另一个对象。定义
\[
\mathcal T_p(X)=
\sum_{s=0}^{p-1}(-1)^s
\frac{(-7X)_s(X+1)_s^7}{(s!)^8}
\quad\bmod(X^p-X).
\tag{6}
\]
取唯一的次数不超过 \(p-1\) 代表。对每个 \(x\in\{0,\ldots,p-1\}\)，
令 \(d=7x\bmod p,m=p-x-1\)，则 (6) 在 \(x\) 处因前两上参数终止，
值恰等于 (1) 的模 \(p\) 值。因此它在原素数窗口上准确编码 \(C_{n,p}\)。
有 \(\mathcal T_p(0)=\mathcal T_p(-1)=1\)，所以它非零。
原表达次数至多 \(8(p-1)\)，约化后至多 \(p-1\)，
只由一般多项式定理得零点数不超过 \(p-2\)，这对预算没有足够改进。

必须区分 \(F_{n,p}\) 在**自变量** \(Z\) 的根数和 \(\mathcal T_p\)
在**指标** \(X\) 的根数。前者固定参数，后者固定 \(Z=-1\) 并同时改变
八个上参数。一个控制前者的定理不能直接控制后者。
Greene 1987 Definition 3.10（印刷页 83）的有限域超几何函数由
乘法字符与 Jacobi 和定义；它也不能仅因名称相同就与 (4) 等同。
尚需精确参数及归约转换，本文没有假定该转换。
见[作者原始 PDF](https://www.d.umn.edu/~jgreene/papers/Hypergeometric_Trans.pdf)、
[本地副本](../literature/greene1987_hypergeometric_finite_fields_author.pdf)。

固定精确证书计算两个预选指标多项式：\(p=11\) 无根，\(p=19\)
恰有根 \(X=7\)，后者为旧反射例。这是两份完整有限域根证书；
没有据此猜测平均零点数。系数、全部值与
\(\gcd(\mathcal T_p,X^p-X)\) 保存在 JSON。

## 3. 所有大支撑的逐项反射零点均来自原反射族

称 (3) 有**逐项反转相消**，若
\[
t_s=(-1)^s\binom ds\binom ms^7,
\qquad t_{e-s}=-t_s\quad(0\le s\le e).
\tag{7}
\]
这是明确的一种自动消失机制，**不是**全部 \(C=0\) 的定义。

**命题。** 若 \(e\ge13\)，则 (7) 当且仅当 \(d=m\) 且 \(d\) 奇。
若 \(p\not\equiv1\pmod7\)，结论对所有 \(e\ge0\) 成立。

**证明。** 中央项非零，故 (7) 迫使 \(e\) 奇；\(e=0\) 也不可能。
先设 \(e=d\le m\)。由二项式 \(\binom ds\) 的对称性，(7) 等价于
\[
r_s^7=1,\qquad r_s=\frac{\binom m{d-s}}{\binom ms}.
\]
对 \(s=0,\ldots,d-1\)，相邻商为
\[
\frac{r_{s+1}}{r_s}=
\frac{A(s)}{B(s)},\quad
A(s)=(d-s)(s+1),\quad
B(s)=(m-d+s+1)(m-s).
\]
全部分母非零，并有恒等式
\[
A(s)-B(s)=\Delta=(d-m)(m+1).
\tag{8}
\]
若 \(\Delta\ne0\)，多项式 \(A^7-B^7\) 的次数准确为 12，
最高系数为 \(7\Delta\ne0\)。它不能在 \(d\ge13\) 个不同的
\(s=0,\ldots,d-1\) 上为零。故 \(\Delta=0\)，而
\(m\le p-2\)，于是 \(d=m\)。若 \(p\not\equiv1\pmod7\)，
七次幂在 \(\mathbb F_p^\times\) 上单射，\(r_s=1\)，
直接由相邻商得 \(\Delta=0\)，不需支撑长度条件。

再设 \(e=m\le d\)。因 \(\binom ms\) 对称，(7) 迫使
\(\binom d{m-s}/\binom ds=1\) 对所有 \(s\) 成立。相邻商同样给
\[
(m-s)(s+1)-(d-m+s+1)(d-s)=(m-d)(d+1)=0.
\]
故 \(d=m\) 或 \(d=p-1\)。后一种在 \(s=0\) 处的商为
\(\binom{p-1}{m}=(-1)^m=-1\)，矛盾。反向在 \(d=m\) 奇时，
\(t_s=(-1)^s\binom ds^8\) 立即逐项相消。证毕。

\(d=m\) 等价于 \(p\mid8n+1\)，且 \(m\) 奇等价于 \(n\) 奇，
所以大支撑情形恰回到前稿反射族。仍可能有小支撑 \(e\le12\)、
\(p\equiv1\pmod7\) 的其他逐项机制；本文未声称它们存在或不存在。

更强的是，**全部逐项反转相消素数的总对数重量为 \(O(\log n)\)**。
对 \(n\ge2\)：若 \(e\le12\)，则 \(m\le12\) 或 \(d\le12\)。
前者使 \(p\in(n,n+13]\)，至多 13 个整数；后者使 \(p\) 整除
\(7n-j\) 中某个 \(j=0,\ldots,12\)。若 \(e\ge13\)，则
\(p\mid8n+1\)。故允许重复计数的安全上界为
\[
\sum_{p\text{ 满足 }(7)}\log p
\le13\log(n+13)+13\log(7n)+\log(8n+1).
\tag{9}
\]
这闭合了这一自动机制的权重，但没有控制不逐项配对的总和消失。

## 4. 常数项几何：直接有部分 Lucas，但完整 scalar Lucas 已被反证

一般 \(q\ge1\)，置
\[
U=\prod_{i=1}^{q}(1+x_i),\quad V=\prod_{i=1}^{q}x_i,
\quad\mathcal L_q=\frac{U(1+U)^q}{V}.
\]
展开 \((1+U)^{qn}\) 后逐变量取常数项，严格得到
\[
B_{n,q}=\operatorname{CT}\mathcal L_q^n.
\tag{10}
\]
因为 \(U^{q+1}/V\) 已经包含整个指数立方体且系数为正，
\[
\operatorname{Newt}(\mathcal L_q)=[-1,q]^q.
\tag{11}
\]
\(q=7\) 的内部格点为 \(\{0,\ldots,6\}^7\)，共有 \(7^7\)，
不是唯一原点。将多面体缩放为 \(M^{-1}\operatorname{Newt}\)，
最小可用整数 \(M=7\)；这时内部只含原点，而 \(M<7\) 时
任一正单位坐标向量已为内部格点。

于是恰匹配 Straub, *Partial Lucas-type congruences*, arXiv:2511.01174v1,
Theorem 1.2 / 2.2 的假设，给出
\[
B_{ap+b,7}\equiv B_{a,7}B_{b,7}\pmod p,
\qquad0\le b<p/7.
\tag{12}
\]
本例亦有直接证明：Frobenius 将 \(\mathcal L^{ap+b}\) 换成
\(\mathcal L(x^p)^a\mathcal L(x)^b\)。\(b<p/7\) 时后一个因子
各坐标指数位于 \([-b,7b]\subset(-p,p)\)，所以可与前者匹配的
\(p\)-倍指数只有零。这就给 (12)，无须未知根数定理。
见[作者原始 PDF](https://arminstraub.com/downloads/pub/partial-lucas.pdf)、
[固定 v1](https://arxiv.org/pdf/2511.01174v1)、
[本地副本](../literature/straub2025_partial_lucas_v1.pdf)。
Samol–van Straten, arXiv:0911.0797v1, Theorem 3.3 的唯一内部格点条件
同样不能直接用于 (11)；见[原始 v1](https://arxiv.org/pdf/0911.0797v1)、
[本地副本](../literature/samol_vanstraten2009_dwork_reflexive_v1.pdf)。

所需异常窗口恰有 \(p\le7n\)，即 \(n\ge p/7\)，处于 (12)
直接给出的低位范围之外。更具体地，完整标量 Lucas 身份确实失败：
\[
B_{13,7}\equiv2\pmod{11},\qquad
B_{1,7}B_{2,7}\equiv4\pmod{11}.
\tag{13}
\]
这是固定精确整数反例。它还排除：同一完整 \(B_{n,7}\) 序列存在一个
**整数** Laurent 常数项幂表示，且其 Newton 多面体满足上述
\(M=1\) 的唯一内部原点条件。否则该表示会给出所有素数的完整 Lucas，
与 (13) 冲突。它不排除把 11 列为坏素数的有理表示、矩阵 Cartier 状态，
或更一般变换，亦不证明除有限素数后仍不存在完整 Lucas。

## 5. 次线性指标根数足够；逐行均匀密度不是唯一接口

删除冻结算术稿的固定有限坏素数，定义
\[
E_n=\sum_{\substack{n<p\le7n\;C_{n,p}=0\ (p)}}\log p,
\quad N_p=\#\{x\in\mathbb F_p:\mathcal T_p(x)=0\}.
\]
这里对 \(E_n\) 的固定删去集合省略于排版，不能省略于实际 (2) 的使用。

**条件桥梁。** 若能证明 \(N_p=o(p)\) 对素数 \(p\to\infty\) 成立，
则对每个 \(\epsilon>0\)，满足 \(E_n>\epsilon n\) 的行在
\(X<n\le2X\) 中为 \(o(X)\)。进一步结合冻结实侧证明，得到
\[
\limsup_{n\to\infty}\frac{\log|\mathscr P_n|}{n}
\ge A+42-\beta_7>20.627.
\tag{14}
\]
这是一个**未满足假设的条件结论**，不是本文给出的本原失败定理。

**证明。** 对每个 \(p\le14X\)，原窗口总要求 \(n<p\)，所以各行是
不同的 \(\mathbb F_p\) 指标；双计数给
\[
\sum_{X<n\le2X}E_n
\le\sum_{p\le14X}N_p\log p=o(X^2).
\tag{15}
\]
最后一步可先删固定 \(p\le P\)，再用 \(N_p\le\delta p\) 和
\(\sum_{p\le14X}p\log p\le14X\,\vartheta(14X)=O(X^2)\)，
让 \(\delta\to0\)。Markov 不等式给坏行 \(o(X)\)。

[冻结鞍点稿](odd_zeta_log_saddle_20261005.md)给每个充分大的相邻行块
至少一个 \(|I_n|\ge c n^{-7/2}e^{An}\)，所以 dyadic 区间中此类大值行
至少占一半（减去端点常数）。它必与 \(E_n\le\epsilon n\) 的密度一行
相交，且任意大区间都有相交行。对这些行使用冻结算术稿的有限本原下界
\[
\log(64M_n/h_n)\ge
7\{\vartheta(7n)-\vartheta(n)-E_n\}-\log B_n-O(1),
\]
以及 \(\log B_n/n\to\beta_7\) 和素数定理，得到
\(\limsup\ge A+42-\beta_7-7\epsilon\)。让 \(\epsilon\to0\) 即 (14)。
不需要证明每个大 \(n\) 的 \(I_n\) 非零。

这个假设比逐行的 \(\limsup E_n/n\le2.94\) **用途不同**：它只控制
平均行，且已足够与密度至少一半的实侧大值相交。它不推出逐行界。
事实上，即使一个任意多项式族每个 \(p\) 只有一个根，也不能推出该族的
逐行加权界：取 \(n_j=8^j\)，区间 \((n_j,7n_j]\) 两两不交，
在其中每个素数定义 \(Q_p(X)=X-n_j\)。每个 \(Q_p\) 只有一个根，
但指定行 \(n_j\) 的零素数重量为
\(\vartheta(7n_j)-\vartheta(n_j)\sim6n_j\)。这仅反证一般推论，
不是实际 \(\mathcal T_p\) 的反例。平均计数和同一行跨素数相关性须分开。

## 6. 已闭合的范围与下一项真正需要的命题

1. 大支撑逐项反转相消完整分类，且全部该机制的素数重量为 \(O(\log n)\)。
   因而继续列举同一反射族不会接近正线性缺层预算。
2. 指标零点问题已有明确 \(\mathcal T_p\) 和次数界，但没有次线性根数定理。
   需要控制上参数随指标同步改变的族，不能套自变量根数或未核参数的
   Greene 字符和结果；后续撤稿的 Ghosh–Ward 定理不属于可用输入。
3. 常数项表示的自然 Newton 几何只能直接支付 \(n<p/7\)，而目标异常
   窗口恰处于其外；完整全素数标量 Lucas 还被 (13) 严格排除。
   多状态 Cartier 或更高 jet 仍可研究，但必须证明具体新约束。
4. 一个可研究的较弱充分目标是 \(N_p=o(p)\)，或仅证明 (15) 的
   \(o(X^2)\) 双平均，不必追求每行 \(E_n/n\) 界。
   也可改为计数[第二零域稿](odd_zeta_log_primitive_20261005.md)的实际缺层，
   但 \(C/p\) 的高位不是单独 (6) 所含的有限域值，须增加真实高阶数据。

[精确脚本](odd_zeta_exceptional_primes_20261005_verify.py)及
[JSON](odd_zeta_exceptional_primes_20261005_verify.json)含 27 项固定核验：
参数匹配与末端微分身份、两类反射商的符号恒等式与次数 12、三个预选反射、
两个完整指标多项式根证书、小维常数项身份、两个部分 Lucas 和一个完整
Lucas 反例。它们不核验任何未证的渐近根数或密度界；全尺度命题由上述证明给出。
