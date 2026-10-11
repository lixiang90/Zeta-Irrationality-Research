# 第225轮：实际六阶算子的主符号与稳定周期衰减

2026-10-08，A。保持222–224同一 R_n、三个偶 A 序列、完整 C 和原 Δ/Ξ/J。本稿把中心化 principal-part 算子的实际系数极限连接到一个六维商代数，给出确切 characteristic polynomial；继而完整证明实际 I 的稳定空间衰减上界。不将 saddle 方程本身当作实际主模 connection，也不把六阶 difference order 当作微分 rank。旧稿/main/manifest 不改。

唯一预先限定的 quotient-algebra 算法实际执行 **2次**：第一次在手写 quadratic trace 的加法错误处退出，无最终输出；修复该固定常数计算后第二次 exit0。无 actual sequence 采样、recurrence guessing 或扫描。全部执行如实登记于§8。

## 1. 固定算子与正确的缩放极限

**S1.** 沿224 T2–T8，

\[
A_n(z)=-(n+z+1)^3(n-z)^9,\quad B_n(z)=(z+1)^9(2n-z)^3,
\]
\[
\mathscr D_nY=A_n(z)Y(z+1)-B_n(z-1)Y(z),\quad
P_j(n,z)=(-1)^j\frac{[(n+z+1)_{3j}(2n-z+1)_{3j}]^3}
{[(z+1)_j(n-z+1)_j]^9}.
\tag{S1}
\]

只取固定 j=0,…,6。224实际有限 principal parts 给 Y_j，满足
R_j=P_j−𝒟_nY_j 为 degree≤10 的 z↦n−z 对称多项式，Y_j=O(z⁻²)，有限 poles 仅在 n+i、1−i（1≤i≤j）。原 M 的行basis是 (z−n/2)^(2a)，a=0,…,5；λ_j=(−1)^j det M̂_j。

置 x=z/n、u=x(1−x)、V=1+2/u，并用大写 V 区别旧局部 deformation 参数 v。直接有限乘积给，在 x∉{0,1,2} 时，

\[
K_n(nx)\longrightarrow-\left(\frac{N(x)}{D(x)}\right)^3,
\quad N=(1+x)(1-x)^3,\quad D=x^3(2-x),
\]
\[
P_j(n,nx)\longrightarrow p(u)^j,\qquad p(u)=-V^9.
\tag{S2}
\]

所以 Root 提供的两条极限公式正确，reflection x↔1−x 保持 P 的极限。这里尚未声称这些点都是某一实际周期的非零 saddle contribution。

**S3.** 有 N+D=1−2u−2u²、ND=(u+2)u³。因此

\[
N^3+D^3=g(u),\quad
g(u)=(1-2u-2u^2)(u^4+2u^3-4u+1)
=(1-2u-2u^2)(u-1)((u+1)^3-2).
\tag{S3}
\]

K-limit=1 的方程是 g(u)=0。其 g(0)=1、degree6，六根 distinct；相应 V 方程为

\[
(V^2-6V-3)(V-3)(V^3-9V^2+3V-3)=0.
\tag{S4}
\]

这些消元本身仅给候选。下一节支付它们与**原 cofactor 算子**的连接。

## 2. 有限余数的真实极限：不允许未付 blow-up

**S5.** 令 h=1/n，在 Q(h)(x) 中置

\[
r_{j,h}(x)=R_j(1/h,x/h),\qquad
q_{j,h}(x)=h^{-12}Y_j(1/h,x/h).
\]

它们是有限 principal-part 公式的真实 rational functions。r 是 x 的 degree≤10 对称多项式；q 在∞为 O(x⁻²)，可能 poles 只在 1+ih、(1−i)h，1≤i≤j。其定义允许 h=0 暂有 pole，不能免费取极限。

精确身份为

\[
P_j(1/h,x/h)=r_{j,h}(x)
+a_h(x)q_{j,h}(x+h)-b_h(x)q_{j,h}(x),
\]
\[
a_h=-(1+x+h)^3(1-x)^9,\quad
b_h=x^9(2-x+h)^3,\quad a_0-b_0=-g(u).
\tag{S5}
\]

**S6：h-adic regularity lemma。** 假设 r 或 q 有负 h valuation，取二者中的最小指数 s<0。左侧 S5 在 h=0 正则，因此最低层满足
r_s−g(u)q_s=0。r_s 是 polynomial；q_s 可能 poles 仅在 x=0,1，且仍为 O(x⁻²)。后一个性质可由所有 q 共同的固定 degree monic denominator 支付：分母由上述有限 pole 因子组成，分子degree至少低2；最低 h 系数亦保持该 degree 差。

g(x(1−x)) 在 x=0,1 的值均为1。所以 r_s=gq_s 是 polynomial 迫使 q_s 在0、1也无pole。它无任何 finite pole，又在∞趋0，故 q_s=0，随后 r_s=0，与最低层非零矛盾。于是 r、q **实际在 h=0 正则**。这一步排除了 individual principal parts 合并时可能的 n-growth，不由有限 n 插值推断。

**S7.** 取真实极限，S5给

\[
r_{j,0}(x)=p(u)^j+g(u)q_{j,0}(x).
\tag{S6}
\]

q 的有限 poles 仅在 x=0,1；g 的六 u 根均不在 u=0。r 是 degree≤5 的 u 多项式。因此在
\(\mathcal A=\mathbb Q[u]/(g)\) 中，

\[
r_{j,0}(u)=\operatorname{rem}_{g}(p(u)^j),\quad j=0,…,6.
\tag{S7}
\]

余数存在且唯一：u 在商代数中是 unit，g(0)=1；g squarefree，S6在六根上给相同值，而 degree≤5 多项式由这六值唯一确定。它连接的是224实际有限余数，不只是临界点的数值。

## 3. 六阶主 characteristic 和每个 coefficient 的 degree

**S8.** 令 K 是 S7 在 basis 1,u,…,u⁵ 的6×7幂矩阵，令 c_j=(−1)^j det K̂_j。一次成功 Fraction 计算给 K rank6，七个 c_j 全非零，且

\[
\chi(q)=\sum_{j=0}^6(c_j/c_6)q^j
=(q+19683)(q^2+19704870q-19683)
(q^3+283965993q^2+3308931q+19683).
\tag{S8}
\]

全七系数按升幂为

\[
(-7625597484987,\ 6352122317573682,\ 1173358131624168759,
\ 110136541593667008348,\ 5601490133371587,\ 303690546,\ 1).
\tag{S9}
\]

输出保存全部 powers、矩阵和七 minors；另 exact 核 χ(p)=0 mod g、g 与 χ squarefree，及三个 V 因子的 q=−V⁹代入。不是按序列值拟合该 polynomial。

**S9.** 原 row basis 经缩放变成 n^(2a)(x−1/2)^(2a)。由于 (x−1/2)²=1/4−u，从此basis到u-basis的6×6常矩阵 determinant为 (−1)^(0+…+5)=−1。所有6×6 minor 同乘 n³⁰。所以 S7严格给

\[
n^{30}\lambda_j(n)\longrightarrow-c_j\ne0,\qquad
\lambda_j(n)/\lambda_6(n)=\chi_j+O(1/n).
\tag{S10}
\]

每个有理 λ_j 的 numerator-degree 减 denominator-degree **恰为−30**。它们在所有充分大正整数均非零；本稿没有给最后一个异常整数的显式位置。prefix 乘子和224粗 D₀⁶¹²清分母不改变 S10 的 normalized recurrence。原 r= n/2 实际递推为

\[
f_{r+6}+\sum_{j=0}^5(\chi_j+O(1/r))f_{r+j}=0,
\tag{S11}
\]

适用于四个实际 A₃,A₅,A₇,C 偶序列和实际 I 偶序列。O(1/r)来自 rational functions 在 h=0 正则，不是经验误差。224已完整支付 bilateral/halfline 求和边界，本稿复用其同一 operator；没有换周期。

## 4. 实际 companion 谱与全 source 上界

**S10.** 令 α 是 V³−9V²+3V−3 唯一实根，8<α<9。导数零点 3±2√2 处该 cubic 的值为−16V<0，所以只存在一个实根；另两根为 conjugate pair、modulus sqrt(3/α)。六 characteristic values 为−V⁹。χ squarefree 保证 limiting companion 可对角化。

设

\[
L_1=\alpha^9,\quad L_2=(3+2\sqrt3)^9,\quad L_3=3^9,
\quad\kappa=(3/\alpha)^{9/2},\quad\eta=19683.
\tag{S12}
\]

前三个模满足 L₁>L₂>L₃>1；另三个模为 κ,κ,(2sqrt3−3)⁹，均<1且 κ 最大。最后比较不需 root solver：α<9给 sqrt(3/α)>1/sqrt3>1/2，而 2sqrt3−3<1/2。

**S11：自含 norm lemma。** 224的真实 six-state companion 𝒞(r)由 S10满足 𝒞(r)→𝒞∞。在 diagonalizing eigenbasis 的 sup norm 中，||𝒞∞||=L₁。因此任意 ε>0，在充分大 r 有 ||𝒞(r)||≤L₁+ε，直接迭代给每个实际 A/C 的 limsup root≤L₁。这只给 upper，不断言具体 sequence 的 L₁ coefficient 非零。

相同证明应用到∧²𝒞和∧³𝒞，因它们的 limiting matrices 也可对角化，得到

\[
\limsup\|v_a\wedge v_b\|^{1/r}\le L_1L_2,
\qquad
\limsup |\Delta_r|^{1/r},\limsup |\Xi_r|^{1/r}\le L_1L_2L_3.
\tag{S13}
\]

因此这些有理系数生成函数的实际 radius 至少 (L₁L₂L₃)⁻¹。固定有理 g 的 gΔ+Ξ也继承此上界。没有仅由 S13证明此 radius 是精确值或某个 singularity 不可去。

## 5. 真实 I 的稳定空间：完整 Volterra 边界与唯一性

**S12.** 223已支付同一实际 I_n=O(n⁻⁵ log n θⁿ)，θ=2⁴²/3²⁷<1。因此它的 six-state v_i(r) 有一个实际指数 σ<1 的 bound，取任何 max(κ,θ²)<σ<1。这里不能仅从 total spectral norm 剔除三个 large modes。

在 𝒞∞ eigenbasis 中写 v=(x,y)，stable diagonal D_s 的 norm为 κ，unstable D_u 的 inverse norm为 η⁻¹；𝒞(r)=diag(D_s,D_u)+E_r，E_r→0。令 E_s,E_u 为两组行。已有 σ<1 的实际 I 解满足

\[
x_r=D_s^{r-R}x_R+\sum_{k=R}^{r-1}D_s^{r-1-k}E_s(k)v_k,
\]
\[
y_r=-\sum_{k=r}^{\infty}D_u^{r-1-k}E_u(k)v_k.
\tag{S14}
\]

第二式由向未来迭代后乘 D_u 的逆得到；终项趋0，因为 η>1>σ。未来和绝对收敛，所以没有免费选择稳定投影。

**S13：weighted contraction。** 任取 κ<ρ<σ，令 B_ρ 为 r≥R 的 sequence 空间，norm为 sup ρ^(−(r−R))||v_r||。S14两组 sums 定义 linear operator T。若尾部 ||E_r||≤ε，则分别由两个几何和得到

\[
\|T\|_{B_\rho}\le\epsilon
\max\{(\rho-\kappa)^{-1},(\eta-\rho)^{-1}\}.
\tag{S15}
\]

同样的式子对 B_σ成立。令 R充分大使两个界都<1。forcing (D_s^(r−R)x_R,0)属于 B_ρ，故收缩级数 Σ T^m forcing 在 B_ρ给唯一解；它亦属于 B_σ。实际 I 解已经在 B_σ，并且与该解有相同 x_R、满足相同 S14。B_σ唯一性迫使二者相等。每个 κ<ρ<σ均如此，故

\[
\boxed{\displaystyle\limsup_{r\to\infty}|I_{2r}|^{1/r}\le\kappa.}
\tag{S16}
\]

本证明只用 actual recurrence、E_r→0 和已有真实 decay；不需要某个 small mode 的非零 connection。它不证明 I 的 exact rate、polynomial prefactor、无限非零或 least differential rank。

## 6. 同一 J/H 的更强半径及 strict-gain 接口

**S14.** 原 J 是 v_a∧v_b∧v_i 的 (0,1,2) 分量。S13的真实two-A wedge bound与S16的真实I bound给

\[
\limsup|J_r|^{1/r}\le T:=L_1L_2\kappa
=[(3+2\sqrt3)\sqrt{3\alpha}]^9.
\tag{S17}
\]

在 ζ(7)=g∈Q 假设下，原有理系数芽 H_g∈Q[[z]] 满足 H_g=Σ(gΔ_r+Ξ_r)z^r=ΣJ_rz^r，因此 R(H_g)≥T⁻¹。它与任意有限数量 ordinary/θ derivatives 在 |z|<T⁻¹共同全纯。S17仍不证明 J 无限非零、H非rational或最小微分rank。

**S15：与独立 connection 输入合并的准确范围。** 同轮 C 的新稿 [actual Fourier modes](pade_actual_fourier_modes_round225_20261008.md) G18–G21另证明

\[
\Delta_r=(-1)^r d_\Delta r^{-33/2}(L_1L_2L_3)^r(1+O(1/r)),
\quad d_\Delta>0,
\tag{S18}
\]

并给 Δ/Ξ在 z=−(L₁L₂L₃)⁻¹的不可去性。本作者实际FULL读其final全部 G1–G21；本稿的数学职责是 S1–S17，**不将自己的 quotient-algebra 运算冒称为 S18 的 Fourier connection 证明**。该 companion 的归一化、全line tails 和非零 Gaussian 常数须由其独立审阅支付。

采用此明确 companion 输入，generic Δ/Ξ 的 exact radius为 R_gen=(L₁L₂L₃)⁻¹，而目标 relation 的 H满足

\[
R(H_g)/R_{\rm gen}\ge L_3/\kappa>1.
\tag{S19}
\]

这是真实关系的 strict相对半径增益；只有 S13与S17两条 upper bounds 时，不能作这个结论。S18提供的不可去主点是必要新增输入。本稿将223 θ²的保守 J界改进为κ，不声称 exact J small mode。

## 7. 获得的结构与仍未支付的 gate

本轮已付 actual leading characteristic、五个实际 scalar solutions 的共同 Poincaré-type recurrence、source/外幂谱upper及actual I stable upper。配合另付的 S18，目标 rational relation 确实取消一个 generic dominant singularity，优于仅比较保证半径。下一接口仍是同一 H的完整 differential closure、independence/nonrational性、实际共同 meromorphic maps及其能量与整结构费用；这里没有把 ordinary linear contraction的小图当作 optimal uniformization。

差分 sixth order或∧³的20维都不等于 CDT微分rank；真实 G-function 性质和 safe12/26 分母沿223/224已证版本。尚未证明全部six asymptotic modes的 r powers、I/J 的非零small connection或 H非rational。fixed-rational shear 保留完整 (Δ,Ξ)背景时不会免费增加整个背景的common-map族。新相对半径结论应在真正cyclic target源上评估，不替完整背景的接口付款。本稿不推出任何新 ζ/L 无理性或线性无关性定理。

## 8. actual primary／两次执行与身份

新增 primary仅 [NIST DLMF2.9](https://dlmf.nist.gov/2.9)：实际选读§i 的 E1–E8及其前后条件（网页lines44–159），另定位§iii的 arbitrary-order参考句（line279）。§i实际讨论second-order，不能直接当本六阶的全渐近基定理；S11–S16均为本稿自含证明，不调用未读书籍或论文。两个 E5/E8 TEX网页请求失败，没有保存或虚称完整读其原件。精确范围另存 [来源与运行账](../literature/pade_asymptotic_sources_round225_20261008/lambert_reading_scope.md)。无新PDF/HTML下载。

本轮 actualFULL复读自己的224固定operator14482B／`32d41b069e688a3aa4e93c44721fe39a6f4ebe1ce646df7fe902bf660d507efd`和222 packet11908B／`35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`；C225 companion11160B／`37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`全部G1–G21亦实际FULL读。223已独审actual I和强分母身份复用，不冒称本轮重新FULL读它们或CDT整篇。

数学程序实际 **2次**，同一已预限定算法：

- 第1次 exit1，预置二次因子常数19704582错误，实际应19704870；在因子核验assert停止，无JSON。失败记录 [700B](pade_leading_symbol_first_run_failure_round225_20261008.txt)，SHA256 `ec02cd37b1e751c159e36405cd6602d8e7ae42db3b8518b5d59cb1cde14a27cf`。
- 固定计算至s₉的 Lucas recurrence 修复该常数后，第2次 exit0。[final producer](certify_pade_leading_symbol_round225_20261008.py)5136B／`51822e871272b0aee875042c73aa53be06792a1085bed5d4a97bf525846bdffa`；[完整 exact JSON](pade_leading_symbol_certificate_round225_20261008.json)5526B／`87e412c2184de9c424831dd20e16e0b0b0f4160946a0c63cc69db49331b6f304`。

成功运行后只将 producer/JSON的scope metadata改为明示“失败后修复执行”，数学数据未改、未再次运行。以上final文件须保存复读登记；本稿不隐藏第1次失败，也不将两次执行称为一次。scope固定degree6商代数、j0…6幂矩阵及cofactor/factor身份；无 actual n序列计算、recurrence guessing、root solver、numericalintegration、parameter/order/prime扫描、PSLQ、Lean或旧producer复跑。文档/网页/metadata操作不是数学执行。本文最终保存后实际FULL作者复读，身份另报；作者自读不代替独审。
