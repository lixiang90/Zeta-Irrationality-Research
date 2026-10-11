# 第220轮：Legendre/Catalan 完整源的实处界与全局入口

2026-10-08。NEW 纸面复盘。本稿在同一坐标 u=x/16、同一三行实际函数和完整多项式源上，支付系数增长、零估计、真实非零 Taylor 子式及其有限处/实处界。结果是：33/4 确实可以控制这些 Taylor 子式的分母，但已证实处界没有提供目标周期的小量；假设 G 有理也没有消除目标尖点的强迫二次对数。应先解决“目标关系产生新的过收敛函数”，再优化容量。本稿不证明新的无理性结论。

## 1. 冻结输入与准确比较对象

本轮实际 FULL 复读下列两份最终保存稿，身份与第219轮冻结身份一致：

| 输入 | bytes | SHA-256 |
|---|---:|---|
| [实际 Legendre 连接](eisenstein_legendre_catalan_connection_round219_20261008.md) | 13940 | 67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39 |
| [完整有限 jet 整格](eisenstein_legendre_integral_flags_round219_20261008.md) | 15599 | bc41296fb85c5548adae93d25cde5f9e4983f5d223ada8e6a39cd1b87b765730 |

连接稿由本作者撰写；此次 FULL 复读是输入核验，不冒充对自己稿的独审。整格稿的本作者独审另有 [第219轮独立审阅收据](research_round219_integral_flags_review_20261008.md)。本稿的新数学仍须另行独审。

沿实际 q=0 分支，x=λ(2τ)，F(x)={}_2F_1(1/2,1/2;1;x)，

\[
U=F K(q(x)),\qquad
L_xU=\frac1{16(1-x)},\qquad
L_x=x(1-x)\partial_x^2+(1-2x)\partial_x-\tfrac14.
\tag{R1}
\]

本稿始终使用

\[
u=x/16,\quad
Y=(\mathcal U,\mathcal V,\mathcal W)^t
=(U(16u),\theta_uU(16u),(1-16u)^{-1})^t,
\tag{R2}
\]

以及完整源和完整系数 jet

\[
L_D=(\mathbf Z[u]_{\le D})^3,\qquad
E_N(a,b,c)=[a\mathcal U+b\mathcal V+c\mathcal W]_{0,\ldots,N}.
\tag{R3}
\]

原冻结 cutoff 是 N=3D，源秩 3D+3，输出秩 3D+1。已证

\[
\log [L_D:L_{D,N}^{\rm int}]\le\frac{33}{4}D^2+o(D^2),
\quad L_{D,N}^{\rm int}=\{v:E_N(v)\in\mathbf Z^{N+1}\}.
\tag{R4}
\]

这是完整源的有限 jet 成本。它不是已经指定的目标周期行列式，也不是 CDT 定理中的 τ。下文先构造它真正能控制的系数子式，再检查目标尖点是否满足直接 holonomy 的解析条件。

## 2. 实际实处增长与 G-function 身份

写 U(x)=Σu_nx^n，c_n=binom(2n,n)^2/16^n。冻结稿给出精确正系数公式

\[
u_n=c_n\sum_{j=1}^n\frac1{16j^2c_j},\qquad n\ge1.
\tag{R5}
\]

从 c_1=1/4 及

\[
\frac{(n+1)c_{n+1}}{n c_n}
=1+\frac1{4n(n+1)}
\]

得到完全初等的两侧界

\[
\frac1{4n}\le c_n\le\frac{e^{1/4}}{4n},\qquad
\boxed{\frac{e^{-1/4}H_n}{16n}\le u_n
\le\frac{e^{1/4}H_n}{16n}},\quad H_n=\sum_{j=1}^n1/j.
\tag{R6}
\]

这里用 Σ_{j≥1}1/[j(j+1)]=1 和 log(1+t)≤t 控制乘积，再逐项代入 R5。没有调用数值渐近拟合。故 b_n=16^nu_n 的指数增长率恰为 16；mathcal U、mathcal V 的收敛半径恰为 1/16。mathcal W 在同一点有实际简单极点。

对 0<r<1/16 置 z=16r。由正系数及 ΣH_nz^n=−log(1−z)/(1−z)，有

\[
\sup_{|u|=r}|\mathcal V(u)|
\le\frac{e^{1/4}}{16}\frac{-\log(1-z)}{1-z},\qquad
\sup_{|u|=r}|\mathcal W(u)|=\frac1{1-z}.
\tag{R7}
\]

mathcal U 的界可再用 u_n≤n u_n。因此三行有共同界

\[
M(r)\le C\frac{1+\log(1/(1-16r))}{1-16r}.
\tag{R8}
\]

例如 r_D=(1−1/D)/16，D≥2，给出 log M(r_D)=O(log D)。这是一项实际解析收益：不需要数值采样便有同源、逐行、接近收敛边界的有效增长控制。

三行均为有理系数 G-functions。其证明已是具体的：R6 给出指数实处界；整格稿给出 d_n^2b_n∈Z、mathcal W 整数系数及 log d_n=O(n)；R2 的有理微分系统给出 holonomic 性。这里采用 [Fischler–Rivoal，引言第一页的 G-function 定义](https://arxiv.org/pdf/1606.00706)：指数共轭界、指数公共分母界和有理系数线性微分方程。G-function 身份没有把尖点的对数分支变成普通点，也没有提供目标 G 的无理性。

## 3. 完整源的新零估计：ord R≤3D+3

先支付所需的完整局部对数系数。置 y=1−x，ell=log(16/y)，f(y)=F(y)。实际分支有局部收敛形式

\[
U(1-y)=A(y)\,ell^2+B_1(y)\,ell+C(y),\qquad
A(y)=f(y)/32,
\tag{R9}
\]

其中 A、B_1、C 在 y=0 全纯。一个直接纸面证明如下。代入 Legendre 方程，三项所需条件是

\[
L_yA=0,\quad L_yB_1=4(1-y)A'-2A,
\]

\[
L_yC=\frac1{16y}-\frac{2(1-y)A}{y}
+2(1-y)B_1'-B_1.
\tag{R10}
\]

A(0)=1/32 使最后一式的 1/y 项消失。其余右端全纯；系数递推 (n+1)^2h_{n+1}−(n+1/2)^2h_n=R_n 给出唯一全纯解，收敛性由递推与右端的 Cauchy 界得到。取实际连接稿确定的 B_1(0)=−G/(2π)、C(0)=π²/48。构造出的解与实际 U 同有

\[
U(1-y)=ell^2/32-G\,ell/(2\pi)+\pi^2/48+O(y\,ell^2).
\]

两者之差满足齐次 Legendre 方程并趋于零；两个齐次局部解分别有非零常数首项和非零一次对数首项，故差为零。这证明的是完整 R9，而非只读出二次对数的常数首项。

令 M 为绕 x=1 的逆时针单值变换，Δ=M−1，B(x)=F(1−x)。因 ell↦ell−2πi，R9 给出

\[
\Delta^2U=-\frac{\pi^2}{4}B(x),\qquad
\Delta^2(aU+b\theta_xU+c/(1-x))
=-\frac{\pi^2}{4}(aB+bxB').
\tag{R11}
\]

B'/B 不属于 C(x)：冻结的收敛互补周期展开及逐项微分给出

\[
B(x)=\pi^{-1}\log(16/x)+O(x\log x),\quad
B'(x)=-1/(\pi x)+O(\log x).
\]

于是 xB'/B→0，而 B'/B 无界；有理函数若第一条件成立，在0便不能有极点，因而必须有界，矛盾。因此只要 (a,b)≠(0,0)，R11 的右端便不恒零。

现回到同一 u 源。定义

\[
Q(u)=u(1-16u),\qquad \delta=Q\partial_u,
\qquad \delta Y=\mathsf B(u)Y,
\]

\[
\mathsf B(u)=
\begin{pmatrix}0&1-16u&0\\4u&16u&u\\0&0&16u\end{pmatrix}.
\tag{R12}
\]

对 r_0=(a,b,c)、deg a,b,c≤D，递推 r_{j+1}=δr_j+r_j mathsf B。则 deg r_j≤D+j，且 δ^jR=r_jY。设

\[
S=\begin{pmatrix}r_0\\r_1\\r_2\end{pmatrix}.
\tag{R13}
\]

若 (a,b)≠(0,0)，det S≠0。证明：若前三行相关，其生成的循环微分模块秩至多二，并在 δ 下稳定，所以 R 满足阶数至多二的有理系数标量微分方程。但 R、ΔR、Δ²R 的最高对数次数依次为二、一、零，其非零共同最高系数由 R11 支付，故三者在 C 上线性无关。它们均是该标量方程的局部解，与阶数至多二矛盾。此论证不要求未知 G 取无理值。

又 deg det S≤D+(D+1)+(D+2)=3D+3。若 ord_{u=0}R=M，则 δ^jR 也有零阶至少 M，因为 Q 在0有简单零。由

\[
(\det S)\mathcal W
=\big[\operatorname{adj}(S)(R,\delta R,\delta^2R)^t\big]_3,
\quad\mathcal W(0)=1,
\]

得到 M≤ord_0 det S≤3D+3。若 a=b=0，则非零 R=c mathcal W 的零阶≤D。故

\[
\boxed{0\ne(a,b,c)\in(\mathbf C[u]_{\le D})^3
\Longrightarrow R\not\equiv0,\quad\operatorname{ord}_0R\le3D+3.}
\tag{R14}
\]

特别地，原 E_{3D} 的核维数在2至3之间，秩在3D至3D+1之间：下界来自矩阵尺寸；上界来自将核单射到剩余三项系数 3D+1、3D+2、3D+3。因此原 cutoff 不能有完整 3D+3 列的非零方形子式。新 cutoff N*=3D+3 的 E_{N*} 则对完整源单射，有一个真正非零的 (3D+3) 阶 Taylor 子式。R14 是零估计及非零证书，不是目标周期评价证书。

## 4. 同源 Taylor 子式确实能使用33/4，但实处界是增长

增加三项 cutoff 的有限处成本可以从冻结的条件定理重新推导，不需要修改原稿。令 N*=3D+3，D≥6。对 N*/2<p≤N* 的每个奇素数，若 p≥2D+3，则 D≥N*−p，满足整格稿 A17 的第一满射条件。否则 p≤2D+1，h=(p−1)/2≤D；而

\[
p>(3D+3)/2\ge(4D+7)/3\quad(D\ge6)
\]

保证 N*−p≤D+h，满足第二条件。因此整个新窗口仍有 exact local index exponent 2(N*−p+1)。全部小素数/高素数幂保留 d_{N*}² 的逐行界，2仍整，p>N*仍整。相对 4(D+1) 的 fallback，新窗口节省指数

\[
4(D+1)-2(N^*-p+1)=2p-2D-4.
\]

同一加权 PNT 给出节省 (15/4)D²+o(D²)，fallback 为12D²+o(D²)，故

\[
\boxed{\log I_D^*:=\log[L_D:L_{D,N^*}^{\rm int}]
\le\frac{33}{4}D^2+o(D^2).}
\tag{R15}
\]

这是本轮的新条件推论，保留完整 u 源及全部 0,...,N* 项；它不把冻结 N=3D 的 statement 改成另一个 statement。

有限指数如何控制真正子式，可以精确说明。若 J 是 L_{D,N}^{int} 的整数基矩阵，|det J|=I，E_N J 为整数矩阵。Jacobi 的互补子式恒等式使 J^{-1} 的任意阶子式分母整除 I；Cauchy–Binet 随即给出 E_N 的任意阶子式 δ_N∈I^{-1}Z。因此任何非零有理 Taylor 子式满足

\[
|\delta_N|\ge I^{-1}.
\tag{R16}
\]

可用 Smith normal form 得到相同结论。这里并未把 entrywise denominator 的 r 次幂当作精确 determinant denominator。R4、R15 分别适用于其各自完整 cutoff；R14 保证每个 D 的新 cutoff 至少存在一个非零最大子式 δ_D^*。

另一方面，对列 u^k f_i、f_i∈{mathcal U,mathcal V,mathcal W} 和输出行 n，系数矩阵项 e_{n,(i,k)} 满足

\[
|e_{n,(i,k)}|\le M(r)r^{-(n-k)}\quad(n\ge k),
\quad e_{n,(i,k)}=0\quad(n<k).
\]

抽出各行 r^{-n}、各列 r^k 后，由 Hadamard 得到任意 s 阶子式

\[
\log|\delta|\le
\left(\sum_{n\in\mathcal R}n-\sum_{(i,k)\in\mathcal C}k\right)\log(1/r)
+s\log M(r)+\frac{s}{2}\log s.
\tag{R17}
\]

对 N=3D 的最大非零秩 s∈{3D,3D+1}，括号为3D²+O(D)。若 s=3D+1，则它精确等于3D²+k_1+k_2，其中 k_1,k_2 是两条删去的源列次数。对新 N*=3D+3，全部3D+3列与输出除去第j行，括号精确等于3D²+9D+6−j。用 R8 的 r_D 得到

\[
\boxed{\log|\delta|\le3\log(16)D^2+O(D\log D).}
\tag{R18}
\]

于是新非零子式拥有真正同对象的两侧界

\[
-\frac{33}{4}D^2-o(D^2)
\le\log|\delta_D^*|
\le3\log(16)D^2+O(D\log D).
\tag{R19}
\]

这比较有效，但没有矛盾：右端是正增长率。不能因为3log16与33/4数值接近，便把它们相减声明严格余量。用 R16 强迫非零子式消失需要同一子式的实处上界小于 exp[−(33/4+ε)D²]；R18 离这个条件很远。源整格的有限指数也没有单独支付一个小范数整数源基。

坐标成本还可精确追踪。令 E^x、E^u 是 x、u 两套标准单项式源/系数 jet 矩阵，则

\[
E^u_{n,(i,k)}=16^{n-k}E^x_{n,(i,k)},\qquad
\delta^u=16^{\sum n-\sum k}\delta^x.
\tag{R20}
\]

前述最大子式因此有实际实处缩放3log16 D²+O(D)。改用 x 图的容量、将 u jet 重新除以16^n、或将源列改为 x^k，都必须同时改变有限格和实处基。R20 阻止只保留 u 的2整性收益、却免费借用 x 的实处归一化。

## 5. 直接 holonomy 接口与已付出的容量

本轮选读 [CDT 固定主文 v2，Theorem 2.5.1及§§2.6–2.7](https://arxiv.org/abs/2408.15403v2) 和 [短稿 Theorem 2.1](https://arxiv.org/html/2510.04156v1#S2.SS1)。直接定理要求有理函数域上的独立有理系数 germs、规定的系数分母类型、共同 holomorphic map 后的 meromorphic 延拓，以及正的 log|φ'(0)|−τ；结论由边界二重对数能量给出。holonomic 假设允许使用 τ 阈值。此直接定理没有要求先构造 Betti/Hodge 包。需要核对的是这些具体解析/算术输入。

当前同一三行按顺序 (mathcal W,mathcal U,mathcal V)，可使用两列均为 (0,1,1)^t 的分母数组：mathcal W 整数，而后两行 d_n² 足够。R11 已支付三行 C(u) 线性独立。该基本定理的参数是

\[
\boxed{\tau=\frac{1\cdot0+3\cdot2+5\cdot2}{3^2}=\frac{16}{9}.}
\tag{R21}
\]

它来自全系数分母类型；R4的33/4来自特定多项式源、特定 cutoff 的指数。不证明两个评价/过滤对象的同一化，便没有将33/4换入 R21 的许可。

有完全付出的单值解析域

\[
\Omega_u=\mathbf C\setminus[1/16,\infty),\qquad
\phi(z)=\frac{z}{4(1+z)^2},\quad\phi'(0)=1/4.
\tag{R22}
\]

三行在此域上有初始分支的单值 holomorphic 延拓；0处初始 germ 全纯。对于闭圆盘映射，使用 φ_s(z)=φ(sz)、0<s<1，避免边界极点，其导数为 s/4。此族的对数能量为 log(s/4)，由 (φ_s(z)−φ_s(w))/(z−w) 非零及二次平均值公式直接得到。其导数条件没有通过 R21。

而且1/4是这个完整三行对象所有 univalent admissible maps 的导数上限。任一此类映射的像必须避开1/16，因为 mathcal U 在该点不 meromorphic。由 [McMullen 作者课程笔记，Theorem 4.20 的 Koebe 1/4 定理](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/10/html/home/course/course.pdf)，像包含以0为心、半径 |φ'(0)|/4 的圆盘，故 |φ'(0)|≤1/4。R22 的开放圆盘 map 达到上限。这是 univalent 范围的实际容量上限，不是对所有 multivalent maps 的否定。

还可以支付一个较大的 multivalent 族。令 Λ(q)=λ(2τ)、q=e^{2πiτ}，取

\[
\psi_s(z)=\Lambda(sz)/16,\qquad\psi_s'(0)=s,\quad0<s<1.
\tag{R23}
\]

冻结连接稿的 theta 产品证明 Λ、F 在 |q|<1 全纯，F无零，Λ不取1。actual K(q) 在此圆盘全纯。因此 mathcal U(ψ_s)=F(sz)K(sz) 全纯；由 Θx=x(1−x)F²，mathcal V 的拉回也全纯；mathcal W 同样全纯。三行和 map 均在 |z|≤1 的邻域定义。这个共同 map 的导数可趋于1，是真实的 multivalent 解析收益，但 log s<0 仍不超过16/9。这里没有证明1是全体 multivalent admissible maps 的最优上限，也没有为未构造的 map 计算能量。

在 x 坐标，Λ'(0)=16；但 U 的系数类型有实际16^n分母，不能套用 R21 的同一个 d_n² 类型。R20 已显示真实矩阵的配套改变。仅把 x 的16导数与 u 的整性放在一个不等式中是不合法的。

## 6. 目标尖点的实际门槛与继续建议

G 是实际奇异尖点 u=1/16 的规范化系数，不是任意普通点函数值。若假设 G=g∈Q，则

\[
H_g(x)=U(x)+(g/2)F(x)\in\mathbf Q[[x]],
\quad
H_g(1-y)=ell^2/32+\pi^2/48+O(y\,ell^2).
\tag{R24}
\]

故该数值假设只消去一次对数的规范化系数，强迫二次对数仍在；它没有把1变成可穿越的 meromorphic 点。H_g 的完整最高对数系数仍为 f(y)/32，因为 F至多一次对数。已知 Tate 项的精确减法是 π²F²/(32B)，不是固定三行空间中已付出的有理系数线性源。单独消去 leading ell² 常数，或加入一个纯 F² 常数倍，不等于支付完整 f(y)/32 的局部系数及全系数整性。

更强地，R11 给出：C(x)U+C(x)theta U+C(x)/(1−x) 中在1附近单值 meromorphic 的元素恰为有理第三行。因为 meromorphic germ 的 Δ²为零，而 B'/B 非有理强迫 a=b=0。这个结论不随 G 是否有理而改变。有限分歧也不能修复：若1−16φ(z)在z0有零阶k≥1，log的增量乘k，Δ_z²的非零右端乘k²。由非常数 map 的开映射性，其解析系数的合成仍不恒零。

因此当前 G∈Q 假设没有在完整三行中增加一个能通过目标尖点的新有理系数 meromorphic 函数。这才是直接 CDT 入口缺失的具体原因；不能笼统归因于 Betti/Hodge 尚无，也不能用另一个普通点替代目标。

R14和R15完成了一项可继续使用的局部技术资产：完整源在 N*=3D+3 处单射，真实非零 Taylor 最大子式的有限成本仍为33/4。但 Taylor 高零阶只在收敛圆内部给出 Cauchy 余项小量；目标1/16位于实际收敛边界，沒有大于目标距离的圆供指数衰减使用。R9的对数系数也不能由这些子式自行提取成一个带已付整性的数值行列式。

继续建议：保留这份 connection/finite-jet 模型作为精确局部原型，停止对当前三行作主线容量调参。下一步先扩大或更换实际函数源，给出一个明确构造，使待反证的 G 数值关系产生新的 Q[[u]] 函数，并证明它的共同 meromorphic 延拓和独立性；随后重新支付该函数源的分母、完整过滤/评价、实处能量与严格余量。如果改走含 singular-cusp 正则化的周期 determinant 路线，则需另外指定实际减法、目标评价、数值非零和同源有限格，不能借 R15 自动继承。当前结果没有排除别的载体、别的周期组合或别的无理性方法。

## 7. 实际阅读、执行账本与审阅边界

输入两稿的本轮 FULL 保存文件读取与 SHA-256 已在§1列出。另实际读 Root 的新局部门槛稿 [目标关系与过收敛](legendre_target_relation_obstruction_round220_20261008.md)，用于交叉比对；R9–R14在本稿按实际 Legendre 方程独立重推，并不把该稿的作者读当作它的独审收据。

主文源是本地 `literature/cdt2024_l2_chi_minus3.pdf` 的固定218页 v2。本轮 PDF文本提取实际完整阅读 printed/PDF pages16–20，范围包含 Theorem2.5.1、其holonomic条件、§2.6 G-functions 和 §2.7 univalent定理；未声称FULL218页。短稿实际 web 选读 arXiv2510.04156v1 §2.1，Theorem2.1与Remark2.2；作者站 ICM.pdf同节定位仅用于版本交叉定位，不混用页码。Fischler–Rivoal arXiv1606.00706仅使用引言第一页的定义；McMullen官方作者课程笔记仅使用printed page64 Theorem4.20及其证明。新的基础公式沿用冻结连接稿已支付的DLMF/Stein身份，本轮不声称重新全文阅读其所有网页。

数学程序、符号引擎、有限矩阵执行、prime/parameter grids、PSLQ、Lean、数值能量积分与旧生产器执行均为零。R5–R24以及新N*的窗口/PNT主项均为纸面推导。实际工具仅进行网页文献定位、冻结Markdown FULL读取/散列、指定PDF页段文本提取、保存和复读本 NEW 稿；无新 HTML/PDF 下载。未修改旧研究稿、main或manifest。本稿最终身份和作者实际FULL保存稿复读结果在handoff给出；独立PASS只能由另一审阅者对同一最终身份另行登记。
