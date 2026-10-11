# 第248轮：真实 degree-three 函数域的提升与同源能量门槛

2026-10-10，B，纸证。固定247的原坐标 \(x=u/(1+7u)\) 与完整五行 \((1,Z,Z^2,H,\delta H)\)。本文支付共同图的实际曲线提升、坏 cusp 的必要遗漏条件，以及由整函数域三行自身强迫的能量下界。没有取得新的数值无理性或线性无关性定理；不把坏叶的存在当作所有图失败。

## 1. 固定源与实际 pole divisor

实际 FULL 读取的247两数学稿已经支付
\[
\mathcal F=\mathbb Q(u,Z)=\mathbb Q(X_0(14)),\quad
[\mathcal F:\mathbb Q(u)]=3,\quad (1,Z,Z^2)\text{ 为基},
\]
\[
u=(\eta(7\tau)/\eta(\tau))^4,\quad Z=f(2\tau)/f(\tau),\quad
f=\eta(\tau)^3\eta(7\tau)^3,\quad P=1+13u+49u^2,
\]
\[
\delta=u\partial_u=x(1-7x)\partial_x,\qquad
\mathscr L=P^2\delta^2-2u(1+16u+49u^2).
\tag{F1}
\]
对 \(a,b,c\in\mathbb Q,(b,c)\ne(0,0)\)，固定
\[
H=aA+bAR+cAD,\qquad
\mathscr LH=b r_R+c r_D\in\mathcal F.
\tag{F2}
\]
这五行实际 rank5。完整 \(d_N^2\) prefix 用 CDT2.5.1 的 **五行两列**矩阵
\[
(b_{ij})=
\begin{pmatrix}0&0\\0&0\\0&0\\1&1\\1&1\end{pmatrix}.
\tag{F3}
\]
行和为 \((0,0,0,2,2)\)，固定清分母不改变 \(\tau=32/25\)；不能把 \(d_N^2\) 当成单列 \(d_{2N}\)。三行 \((1,Z,Z^2)\) 在同一原坐标均有整数 Taylor 系数，实际 rank3。

记 \(E\) 为该函数域的光滑射影曲线。它是 \(X_0(14)\)，而非 \(X_0(7)\)。指数24、四个 cusp 的宽度 \(1,14,7,2\)、无 order2/3 elliptic points 给
\[
g(E)=1+24/12-4/2=1.
\tag{F4}
\]
实际有理函数 \(x:E\to\mathbb P^1\) 的 pole divisor 是
\[
D_x=(x)_\infty=\pi_u^*(-1/7),\qquad \deg D_x=3.
\tag{F5}
\]
这是 divisor 等式，保留可能的重数，不假定三个支持点互异。\(u=\infty\) 的 cusp0 和 cusp1/2 在 \(x=1/7\) 上，不是 \(x\) 的 pole。不能把这些 cusp 与 \(D_x\) 混同。

## 2. 共同图严格提升到 \(E\)

设 \(\phi:\mathbb D\to\mathbb C_x\) 全纯，\(\phi(0)=0,\phi'(0)\ne0\)。若 native \(Z\circ\phi\) 延拓成单值亚纯函数 \(\zeta\)，则存在唯一延续 native 点的全纯映射
\[
\psi:\mathbb D\longrightarrow E,\qquad \phi=x\circ\psi.
\tag{F6}
\]
证明：\(U=\phi/(1-7\phi)\) 与 \(\zeta\) 是两个亚纯函数，满足已付的 degree-three 最小关系。因而它们在非例外点给出到该代数曲线的映射，提升到其 normalization \(E\)。在删去的离散点附近，两坐标均亚纯，故在射影模型有极限。normalization 在该极限上只有有限个点；小的连通穿孔邻域的提升落在其中一个局部支，局部参数有界，故可去。native 点唯一决定全盘提升。这也等价于光滑一维源到 normalization 的通常提升性质；没有把 \(E\to\mathbb P^1_x\) 当作普通无分歧覆盖。

由于 \(\phi\) 在盘内有限，\(\psi\) 必须避开 \(\operatorname{supp}D_x\)：若到达 pole，正的局部映射次数只能放大 pole，不能消去它。反之，任意 native \(\psi:\mathbb D\to E\setminus\operatorname{supp}D_x\) 给全纯 \(\phi=x\circ\psi\)，且三行函数域的拉回都亚纯。所以 F6 与 pole 遗漏正好描述 **三行函数域** 的共同图，不自动描述 \(H\) 的全叶合法性。

这里只需要 \(Z\) 行即可强迫提升；没有使用245被停用的 homogeneous-background recovery。原点 \(x=q+O(q^2)\)，因此 \(\phi'(0)\) 使用247的实际坐标归一化。

## 3. 坏 cusp 的最高对数不能靠换到达叶取消

247实际 whole-source 展开给：\(b\ne0\) 时 cusp1/2 的 \(H\) 有非零 \(\log^2\) 项；\(c\ne0\) 时 cusp1/7 的 \(D\) 通道有非零 \(\log^2\)，而 \(R\) 在该 cusp 有有限部分。齐次 \(A\) 通道不能取消这两个最高项。

此必要条件还可提升为同一曲线点的叶不变量。沿任意返回到同一 \(E\) 点的回路，forcing \(b r_R+c r_D\) 返回自身，因此两支 \(H\) 的差被 \(\mathscr L\) 杀。在 \(u=0\) 与 \(u=\infty\)，F1 的齐次 indicial polynomial 均为双根0：除以 \(P^2\) 后，势在相应端点消失。完整 Frobenius 齐次解至多含一级对数；有限 cusp cover 的拉回也不提高对数次数。因此返回叶的差不能改变非零 \(\log^2\) 最高系数。

于是任何五行共同合法图 F6 还必须满足
\[
b\ne0\Rightarrow \psi(\mathbb D)\not\ni P_{1/2},\qquad
c\ne0\Rightarrow \psi(\mathbb D)\not\ni P_{1/7}.
\tag{F7}
\]
到达这些点的有限局部次数仍留下非零 \((\log s)^2\)，不可能亚纯。这个结论针对实际点与 forcing 返回的全部叶，强于仅发现一个坏叶；仍不排除图避开这些点。

关系 \(\sigma=a+bY/2+c\pi^2/8=0\) 仅支付 canonical cusp0 的完整 jump 取消。它不能免费支付回绕后别的到达叶；不同返回叶仍可多一个齐次一级对数。对于候选 \(\psi\)，剩余精确条件是：所有盘内 cusp 原像的实际到达叶均无对数 monodromy，并有亚纯局部展开。验证这些条件后，删点盘的局部返回生成元均平凡，实际拉回才能延拓成全盘亚纯函数。F7 和 canonical 取消都只是这个完整条件的组成部分。

## 4. 整函数域三行强迫 \(J\ge3\lambda\)

使用实际选读的 CDT Theorem2.5.1，对同一个 \(\phi\) 仅应用整系数、对 \(\mathbb Q(x)\) 独立的三行 \((1,Z,Z^2)\)。它们全行类型0，所以在
\(\lambda=\log|\phi'(0)|>0\) 时
\[
3\le J(\phi)/\lambda,\qquad J(\phi)\ge3\lambda.
\tag{F8}
\]
这不是从五行安全费用反推的估计，而是实际三行子源的独立 holonomy 约束。

边界条件按原定理处理。若 \(\phi\) 全纯于闭单位盘邻域，直接用其有限自能量；若只有开盘数据，先取 \(\phi_\rho(s)=\phi(\rho s)\)，在 \(\rho|\phi'(0)|>1\) 时得到
\[
J(\phi_\rho)\ge3\log(\rho|\phi'(0)|).
\tag{F9}
\]
采用径向有限能量时再取 \(\rho\uparrow1\)；若径向能量为 \(+\infty\)，它不能满足本节的严格有限判据。这里没有无条件更换 Hermitian metric。

若 \(\phi\) 单叶，divided difference
\((\phi(z)-\phi(w))/(z-w)\) 在双盘无零，故其 log absolute value 的双圆均值恰为 \(\log|\phi'(0)|\)。对缩盘也一样，F9 即与 \(3\le1\) 矛盾。因此
\[
\text{单叶共同合法图}\quad\Longrightarrow\quad|\phi'(0)|\le1.
\tag{F10}
\]
单叶路线已停，不要求任何未知周期半径或 map 扫描。

对于一般多叶图，五行当前同坐标安全类型的严格 CDT 入口是
\[
\lambda>32/25,\qquad J(\phi)<5(\lambda-32/25).
\]
联 F8 得
\[
\boxed{\lambda>16/5,\quad |\phi'(0)|>e^{16/5}},\qquad
J(\phi)-\lambda\ge2\lambda.
\tag{F11}
\]
因此只比较导数与 \(e^{32/25}\) 不足以准入；曲线三行本身索取额外能量。本文没有证明不存在满足 F11 的多叶图，也没有把安全数组说成最优数组。若另在同坐标支付统一 \(c\le e^{16/5}\)，才会关闭当前数组的全部基本图入口。

## 5. 本轮决策与实际读域

保留资产：真实关系敏感 canonical 投影、rank5、完整整模型、实际非恢复，以及这里的新 F6/F7/F8。停止单叶图优化。多叶准入的第一门槛是实际 normalized 曲线提升后的统一导数预算与 F11 比较，或者重构当前完整源/数组；不继续从坏 cusp 或较小安全 prefix 推出严格数值结论。

官方 LMFDB 页面明确给 \(X_0(14)\) 模型
\(y^2+xy+y=x^3+4x-6\)，并列 modular degree1、optimal、Manin constant1。这些是选读的数据陈述；本文 F4–F11 不用数据库的近似 period，也不以该数据替代 eta 到 Weierstrass 的 normalized differential 推导。后续若用 Abel/Bloch 统一界，必须另支付这个归一化桥和真实 pole fiber；本文不借尚未阅读的新稿结论。

完整身份与 primary 读域见 [packet_reading_scope.md](../literature/global_review_sources_round248_20261010/packet_reading_scope.md)。仅重新核本文使用的具体输入，不宣称重新 FULL 审计246/247所用全部原论文。数学程序、CAS、Lean、interval、prime/parameter/map scan 执行均0；旧文件、主日志、政策及 manifest 未改。新数值定理未得。
