# 完整三维尖点校正：U 的真实端点与周期比例的精确必要充分条件

日期：2026-10-06。只读冻结的 level12 cusp window 与 χ12 Manin 接口；不执行、导入或修改旧/同行数学 producer。本稿新增平凡字符的独立 Manin/oldscale 实现。结论限于真实源空间 \(KU+KX_0+KX_2\)、第一支 \(W_{12}\) 与指定第二支 \(M\)（端点 \(2/7\)）。没有证明未知周期的数值线性无关，没有排除其它反射、源或整模型。

新的精确结果有两项：

\[
f_U(2/7)=L(U,3)+\frac{6\pi i}{7}L(f_6,2),
\tag{1}
\]

以及：存在非零 \(K\) 尖点校正同时满足第一支零 \(L(3)\) 与第二支端点实部零，**当且仅当三个真实 \(L(3)\) 周期在 \(K\) 中全部成比例**。只存在一条 K 周期关系仍然不够。若满足这个实部条件，完整反射还须另核一条 central-period/Tate 条件。

## 1. 实际 source 与积分规范

令 \(K=\mathbf Q(r)\)、\(r=\sqrt3\)、\(\sigma r=-r\)。使用冻结稿中已证明的实际整数源
\[
f_6=\eta(\tau)^2\eta(2\tau)^2\eta(3\tau)^2\eta(6\tau)^2,
\quad U=f_6(\tau)-4f_6(2\tau),
\quad X=(X_0,X_2).
\]
三个源都为 weight4、\(W_{12}\)-minus；\(\sigma U=U\)，而 \(\bar X=\sigma X\) 为 W-plus。\(\sigma\) 始终只作用于 source coefficients。

写
\[
\Omega_U=L(U,3)=\tfrac12L(f_6,3)>0,
\quad \Omega=(\Omega_0,\Omega_2)=(L(X_0,3),L(X_2,3)),
\quad \Psi=(L(\bar X_0,2),L(\bar X_2,2)),
\quad C_6=L(f_6,2)>0.
\tag{2}
\]
最后的严格正性直接来自 eta product 在正虚轴的正 Mellin integral。冻结稿已证 \(\Omega_0,\Omega_2>0\)；以下只用其非零性。

对 q-constant-zero primitive \(f_F=\theta_q^{-3}F\)，实际边界值为
\[
f_F(x)=4\pi^3i\int_x^{i\infty}F(\tau)(\tau-x)^2d\tau.
\tag{3}
\]
\(a_n(F)=O_\varepsilon(n^{3/2+\varepsilon})\) 使 \(a_n(F)/n^3\) 绝对可和。因此 rational x 的值、路径分解与随后 period identities 都是实际收敛积分，不是 regularized 猜测。

## 2. 独立平凡字符 Manin 模型与 oldscale

新实现分别建立 \(\Gamma_0(6)\) 的12个 cosets、\(\Gamma_0(12)\) 的24个 cosets，分别得到36维、72维 induced \(\operatorname{Sym}^2\) 空间。固定代表来自 \(\mathbf P^1(\mathbf Z/N)\)，沿 S、T closure 一次确定。完整 Manin relations 为
\[
(1+B_S)\rho=0,\qquad (1+B_{TS}+B_{TS}^2)\rho=0.
\]
level6、level12 Manin 空间的精确维数分别为6、12，不能将它们直接当作 cusp period 空间。

新计算中 \(T_5=6\) 的 eigenspace 在 level6 维2、两种 parity 各维1；level12 的对应 oldspace 维4。独立 eta product jet 给 \(T_5f_6=6f_6\) 至 Sturm bound8，系数1至8为
\((1,-2,-3,4,6,6,-16,-8)\)。两边均为 level6 modular cusp forms；level6 的 Sturm bound4 已足够，检查到8只给交叉证据。

Paşol–Popa Theorem5.14 给实际 cusp periods 在每个 parity 的 injectivity。\(f_6\ne0\)，故其两份实际 period vectors 都非零，属于上述一维 eigenspaces；所以该一维 cut 正好由实际 \(\rho_{f_6}^{\pm}\) 生成。这里没有以包含 coboundary 的 Manin 空间替代真实 period image，也没有用 period 数值 independence 作输入。

由 \(\Gamma_0(12)\subset\Gamma_0(6)\)，level6→12 lift \(L\) 仅将 level12 coset reduction 后复制同一 integral polynomial。令 \(D=\operatorname{diag}(2,1)\)，det-normalized weight4 slash 满足
\[
f_6|_4D=4f_6(2\tau),\qquad
\rho_U=(1-B_D)L\rho_{f_6}.
\tag{4}
\]
新 slash operator 从真实路径变换推导。对 \(g=(a,b;c,d)\)、\(\det g=\delta\)，令 u=gτ，则
\((F|_4g)(\tau)d\tau=(a-cu)^2F(u)du/\delta\)；三个 period coefficients 的 transformed polynomials 因而统一带 \(1/\delta\)。这给 (4)，没有漏掉 oldscale4 或路径尺度2。

令 \(\ell\) 取 I-coset polynomial 的常数项，\(m\) 取一次项，\(e\) 是 (3) 中 \(x=2/7\) 的积分行。continued fraction 路径同样为
\(\{2/7,\infty\}=\{0,\infty\}+\{1/3,0\}+\{2/7,1/3\}\)。
新 JSON 中实际 finite basis 的行值为

|functional|level6 even basis|level6 odd basis|
|---|---:|---:|
|\(\ell_6\)|\(-1/3\)|—|
|\(m_6\)|—|\(1\)|
|\(\ell_{12}(1-B_D)L\)|\(-1/6\)|—|
|\(e(1-B_D)L\)|\(-1/6\)|\(3/7\)|

这些行值是 rational basis 坐标，不是周期数字本身；实际归一由 \(\rho_{f_6}^{\pm}\) 提供。于是
\[
e\rho_U^+=\ell\rho_U^+,
\qquad e\rho_U^-=\tfrac37m\rho_{f_6}^-.
\tag{5}
\]
规范 (3) 给 \(4\pi^3i\ell\rho_U=L(U,3)\)，且
\(m\rho_{f_6}=L(f_6,2)/(2\pi^2)\)。将 (5) 代入即得 (1)。

特别 \(L(U,2)=0\) 仍成立，却不能删除 U 的整个 odd period vector。其 \(2/7\) carrier 是真实 \(L(f_6,2)\)。新计算还核 \(\rho_U^-\ne0\)，与 Eichler–Shimura injectivity 相符。

## 3. 完整三源实部的精确 criterion

冻结 χ12 接口给
\[
f_{\bar X}(2/7)=\Omega R+\frac{2\pi i}{7}\Psi,
\qquad R=\frac5{14}
\begin{pmatrix}1-3r&1+r\\-33+27r&1-3r\end{pmatrix}.
\tag{6}
\]
对 \(C=tU+uX_0+wX_2\)，\(t,u,w\in K\)，第一支 zero W period 与指定第二支 zero real period 分别为
\[
t\Omega_U+\Omega v=0,
\qquad \sigma(t)\Omega_U+\Omega R\sigma(v)=0,
\quad v=(u,w)^t.
\tag{7}
\]
这是三份实际 source integral，不将任何未知 \(\Omega_j\) 变成 \(\sigma\Omega_j\)。

**命题。** (7) 有非零 K 解，当且仅当
\[
\alpha=\Omega_0/\Omega_2\in K,
\qquad \beta=\Omega_U/\Omega_2\in K.
\tag{8}
\]
若有解，该 K 解空间准确一维。

**证明必要性。** 先排 t=0 的非零解。此时若 u=0，第一式与 \(\Omega_2\ne0\) 给 w=0。若 u≠0，则 \(\alpha=-w/u\in K\)。写 \(\alpha=a+br\)、\(a,b\in\mathbf Q\)，第二式化为
\[
(\alpha-\sigma\alpha)(1-3r)-(1+r)\alpha\sigma\alpha-33+27r=0.
\]
其有理、r 系数分别为
\(-a^2+3b^2-18b-33\)、\(-a^2+3b^2+2b+27\)。相减给 b=−3，继而 a²=48，矛盾。这重核了先前二源障碍，但未据此排全部三源。

故任意非零解 t≠0。令 \(\lambda=\sigma(t)/t\)，则 \(\lambda\sigma\lambda=1\)。消去 \(\Omega_U\)，得到
\[
\Omega\{R\sigma(v)-\lambda v\}=0.
\tag{9}
\]
括号向量不能为0：若为0，作系数共轭再代回给
\(R\sigma(R)v=v\)。而新固定矩阵计算给
\[
R\sigma(R)=\begin{pmatrix}
-125/7-375r/49&125/49\\375/7&-125/7+375r/49
\end{pmatrix},
\quad\det(1-R\sigma(R))=103776/2401\ne0.
\tag{10}
\]
所以 v=0，与第一式的 t≠0、\(\Omega_U\ne0\) 矛盾。于是 (9) 是两非零实际周期之间的一条非零 K 关系，迫 \(\alpha\in K\)。第一式随即给 \(\beta=-(u\alpha+w)/t\in K\)。

(10) 的两个 eigenvalues 为 \((-875\pm500r)/49\)，均严格负；本证明只需没有 eigenvalue1，不能把负 eigenvalues 本身误作数值 period independence。

**证明充分性与唯一性。** 若 (8) 成立，将 (7) 除以实际非零 \(\Omega_2\)。第二式现在全部系数都在 K，可以合法作 \(\sigma\)（此时两个比值已经是假设中确定的代数数）。等价于两个普通 K 行方程
\[
\begin{pmatrix}\beta&\alpha&1\end{pmatrix}(t,u,w)^t=0,
\qquad
\begin{pmatrix}\sigma\beta&(\sigma\alpha,1)\sigma R\end{pmatrix}(t,u,w)^t=0.
\tag{11}
\]
两行独立。若第二行等于 μ 倍第一行，非零 β 给
\(\mu=\sigma\beta/\beta\)、\(\mu\sigma\mu=1\)。其后两项作共轭再复合迫行 \((\alpha,1)\) 为 \(R\sigma R\) 的 eigenvalue1 向量，与 (10) 矛盾。故 rank2、核维1。此核中 t 也不能为0，由上面的二源障碍。证明完毕。

因此可用的三源校正需要 **两份实际 K 比值**。若三个周期的 K-span 维数为2，虽存在一条 K 关系，仍无法同时给本 M 的实部零。这是本轮新的完整三源限制，不是三个周期在 K 上线性无关的证明。

## 4. 完整反射仍保留 central/Tate condition

由 (1)、(6)，第二支完整 cusp endpoint 为
\[
f_{\sigma C}(2/7)=
\sigma(t)\Omega_U+\Omega R\sigma(v)
+\frac{\pi i}{7}\{6\sigma(t)C_6+2\Psi\sigma(v)\}.
\tag{12}
\]
满足 (7) 只取消实部。使用冻结的 canonical pure target 源 \(F_L\) 与 zero-first-period 源 R（本节 R 指 Eisenstein source，矩阵仍按 (6)），其真实 M cocycle 为
\(c_{F_L}(M)=0\)、\(c_{R}(M)=-(1920/7)i\pi^3Q_M\)。
加入 \(sR\)、\(s\in K\)，完整第二支零反射迫
\[
\boxed{\sigma(s)=
\frac{6\sigma(t)L(f_6,2)+2\Psi\sigma(v)}{1920\pi^2}.}
\tag{13}
\]
所以还需要右边属于 K。实部 criterion 成立时 (7) 的非零方向只有一个 K 维；改变该方向的 K 标量不能免费使 (13) 成为代数数。

这是完整指定反射的可判定接口：先核 (8) 的两份 L3 比值，再核一个实际 central combination 与 π² 的 K 比值。两者目前均未得到所需数值证明。不把 formal period 空间的维数或 source coefficient 共轭当作这些未知比值的证明。

若未来把这些 period tuple 自身作为联合线性无关目标，(7)、(12) 可作为合法 projection 约束继续建立整模型和全部 embedding 的解析叶；本稿没有完成该 CDT 预算，没有声称既有叶就是完整 stabilizer，也没有新的数值无理性定理。

## 5. 原件与验证范围

实际阅读 Paşol–Popa 原件 PDF pp3–4、13–16，核 induced convention、Manin/coboundary distinction、Hecke compatibility、Theorem5.14 injectivity、critical Mellin constants 和 Proposition5.11 的归一范围。该命题只给同一 eigenform 的 normalized polynomial 系数代数，不给不同 eigenforms 的真实数值比值；本文没有超出这一范围。

复用 literature/pasol_popa_period_polynomials_20261006.pdf（32页，SHA256 1de88be12c3d7bac48d263fe0f5143f622e76ff23db236520508de4d336fbfb5），原网页 [arXiv 1202.5802v5](https://arxiv.org/abs/1202.5802v5)。没有重复下载覆盖；本轮阅读清单另建 literature/cdt_odd_level12_trivial_period_primary_20261006.json。

新 producer 执行历史如实保存：第一次在错误的预期 level6 Manin dimension8 上失败，尚未输出终证书；正确维数6。第二次只修正该记账预期，21项通过；第三次新增七项固定 semilinear 矩阵与二源式检查，28项通过。未执行或 import 任何冻结/同行 producer，未作 word、parameter 或 prime 搜索。

28项有限检查覆盖新的 cosets、Manin维数、实际 T5 cut、degeneracy、U anti-W、完整 even/odd endpoints、eta/Sturm identity及 (10) 的矩阵数值；正文的实际积分、ES 范围与 (8) 必要充分证明是数学论证，有限 checks 不替代它们。尚待 root 独立审阅；不存在 Lean 形式化验证声明。
