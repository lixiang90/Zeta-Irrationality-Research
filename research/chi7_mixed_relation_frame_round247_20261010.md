# 第247轮：同一五行系统承载 1、L(2,χ−7)、π² 的有理关系

2026-10-10，Root，纸证。本文把已经完成的真实 dyadic Fricke 比较与 degree-three 整函数域合并，支付关系敏感的完整 cusp0 投影及实际 rank5。尚无共同合法解析图或严格 holonomy 差额，因此没有新的数值线性无关性定理。

## 1. 固定对象与真实 forcing

沿用 A247 的 D1–D11 与 C247 的 D2–D6。固定 χ=χ−7、Y=L(2,χ)，以及
\[
u=(\eta(7\tau)/\eta(\tau))^4,\quad v=u_7(2\tau),\quad
Z=f(2\tau)/f(\tau),\quad f=\eta(\tau)^3\eta(7\tau)^3,
\]
\[
P=1+13u+49u^2,\quad \delta=u\partial_u,\quad
\mathscr L=P^2\delta^2-2u(1+16u+49u^2).
\]
Yang 的实际 period A 满足 A(0)=1、\(\mathscr LA=0\)。原算子在 C(u) 上不可约，其齐次解析解为 A、τA；这些输入在246已自含核过。

取 A247 的实际 convergent primitives R、D：
\[
R=K(q)-2K(q^2),\qquad D=C(q)-C(q^2)/4,
\]
\[
\Theta^2R=E_0(q)-8E_0(q^2),\qquad
\Theta^2D=E_1(q)-E_1(q^2),\quad \Theta=q\partial_q.
\]
完整函数域 \(\mathcal F=\mathbb Q(u,Z)=\mathbb Q(X_0(14))\) 对 Q(u) 恰 degree3，basis 为 1、Z、Z²；v∈F。真实 forcing 为
\[
r_R=uP[1+8u-8Z(1+8v)],
\]
\[
r_D=uP[-7-8/(7u)+Z(7+8/(7v))]\in\mathcal F.
\tag{1}
\]
第二式来自已经付 degree bound 的恒等式 E₁=−f(7+8/(7u))，不是对去常数 E₁+8/7 的错误模性调用。

给定 a,b,c∈Q 且 (b,c)≠(0,0)，定义同一个实际函数
\[
H=aA+bAR+cAD,\qquad \sigma=a+bY/2+c\pi^2/8.
\tag{2}
\]
变化常数公式给 \(\mathscr LH=b r_R+c r_D\)。因此
\[
V=\mathcal F+\mathbb Q(u)H+\mathbb Q(u)\delta H
\tag{3}
\]
在 δ 下稳定，rational connection 由 F 的 degree-three 最小式及 (1) 唯一定义。这先给维数≤5，确切秩在§3另证。

## 2. 有理关系等价于指定 cusp 的完整 jump 取消

记 Wτ=−1/(14τ)。A247 已对整个 H 证明
\[
\tau R(W\tau)=\frac{2i\sqrt7}{49}D(\tau)+\frac Y2\tau-
\frac{i\sqrt7\pi^2}{196},
\]
\[
\tau D(W\tau)=\frac{i\sqrt7}{4}R(\tau)+\frac{\pi^2}{8}\tau-
\frac{i\sqrt7Y}{8}.
\]
用实际 \(A(W\tau)=-2i\sqrt7\tau A(2\tau)\)，相乘得
\[
AR(W\tau)-\frac Y2 A(W\tau)
=\frac47 A(2\tau)[D(\tau)-\pi^2/8],
\]
\[
AD(W\tau)-\frac{\pi^2}{8}A(W\tau)
=\frac72 A(2\tau)[R(\tau)-Y/2].
\tag{4}
\]
这里 AR(Wτ) 的意思为 A(Wτ)R(Wτ)，AD 同理。于是精确地
\[
H(W\tau)=\sigma A(W\tau)+A(2\tau)
\left[\frac47b(D(\tau)-\pi^2/8)+\frac72c(R(\tau)-Y/2)\right].
\tag{5}
\]
在 canonical cusp0 的实际参数 \(w=e^{2\pi i\tau}\) 中，方括号为收敛级数，A(2τ)=A(w²)，而
\(A(W\tau)=-(\sqrt7/\pi)\log w\,A(w^2)\)。因此完整返回 jump 为
\[
\Delta_0H=-2i\sqrt7\,\sigma A(w^2).
\tag{6}
\]
所以 σ=0 当且仅当 H 在这一指定 cover cusp 上亚纯，此时实际全纯，δH 亦全纯。F 的三行在该 cover 上亚纯。这个证明支付整个 log coefficient，不只是径向有限部分。

必须保留实际 ramification2：以 \(x=u/(1+7u)\) 为 base 坐标，\(x-1/7=-w^2+O(w^4)\)。式(5)一般有奇次 w 项，Z∼1/(8w)。故这是 cover 上的填点，不能把它当 base 的普通填点，也不能无条件填满 x=1/7 的所有到达叶。

## 3. 确切 rank5，及背景不能被完整五行恢复

下面的独立性对所有 a,b,c∈C、(b,c)≠0 都成立。A247 已付 cusp1/2 的
\[
R(-e^{-t})=-7L(3,\chi)/(8t)+O(1),\quad D(-e^{-t})\to\pi^2/8,
\]
C247 已付 \(A\sim\pi/(\sqrt7t)\)。若 b≠0，H 在此有非零二级 logarithm，aA 与 cAD 至多一级，不能相消。

若 b=0,c≠0，用 A247 已付 cusp1/7 的
\[
D(\zeta_7e^{-t})=\mathfrak g L(3,\chi)/(8t)+O(1),\quad
R(\zeta_7e^{-t})\to Y/2,\quad \mathfrak g\ne0.
\]
对 γ=(1 0;7 1)，τ=1/7+it/(2π) 给
\(\gamma^{-1}\tau=-1/7+2\pi i/(49t)\)，故实际模变换给
\(A(\tau)\sim2\pi i/(7t)\)。因此 H 又有非零 log²。两处均为全纯模驱动的 regular-singular germs；最高系数也可仅从 t⁻² 增长确定其不属于亚纯函数域。F 中任一函数在实际 cusp 上为有限阶 Laurent 级数；不可能有这种次幂级数之外的 log² 增长。故 H∉F_C。

F_C=C(u,Z) 在 δ 下稳定。V_C/F_C 是非零、被原不可约二阶 L 杀的 cyclic quotient，故维数恰2。于是五个实际函数
\[
(1,Z,Z^2,H,\delta H)
\tag{7}
\]
对 C(u) 独立，亦对 Q(x) 独立。没有以矩阵行数代替 actual rank。

还可证明 **A 不在 V_C 中**。记 M_A=C(u)A+C(u)δA。不可约性使 M_A 简单；M_A∩F_C 若非零则包含 A，但 canonical cusp0 的 A 有实际非零 log，不能属于 F_C。因此交为0。

若 A∈V_C，则 M_A⊂V_C，维数迫 V_C=F_C⊕M_A；两个块均微分稳定。沿这一直和投影写 H=y+z，y∈F_C，z∈M_A。对 LH∈F_C 投影得 Lz=0，Ly=b r_R+c r_D。所以 H−y=z 是原 L 的实际齐次解，在上述两个坏 cusp 至多一级 log。它不能删除 H 的非零 log²，而 y 为亚纯，矛盾。这里使用微分稳定投影，不能错误地声称任意 K 系数 A、δA 组合都被 L 杀。

这个非恢复证明针对已完整包含 F 的同一个五行系统；不把非恢复提升为所有 CDT 方法的必要条件。

## 4. 同坐标全 prefix 与条件数值出口

取正整数 B 清除 a,b,c。A(q)、q(u(x))、Z(q) 的整数级数已付；A247 的完整系数给 R、D 均用 d_N² 清除前 N 项。因此对每个 N 和 0≤k≤N，
\[
[x^k](1,Z,Z^2)\in\mathbb Z,\quad
B d_N^2[x^k]H,\ B d_N^2[x^k]\delta H\in\mathbb Z.
\tag{8}
\]
δ=x(1−7x)∂x 不索取 prefix 之外的系数。literal 全行整型为 (0,0,0,2,2)，实际 m=5，\(\tau=2(7+9)/25=32/25\)。固定 B 不改变渐近类型；未声称最优费用。

若对每个有理关系假设 σ=0，能够另付同一坐标的共同合法 φ、全部实际拉回单值亚纯，以及
\[
\log|\phi'(0)|>32/25,\qquad
J(\phi)/(\log|\phi'(0)|-32/25)<5,
\]
直接 CDT 将与实际 rank5 矛盾，从而排除该关系。全部关系的排除才给 1、Y、π² 对 Q 线性无关。本文尚未支付这些图和严格费用条件，**不宣称该数值结论**。

本轮新付的是实际有理关系的完整 cusp0 投影、同一完整五行秩与整模型及全 frame 非恢复。坏 cusp 仍在，合法图不能从局部填点继承；不启动地图或素数扫描。248正式全局复盘按原计划进行，比较此源与 Fricke 特征方向及其它真实周期源，不重置计数。

## 5. 读域与来源边界

Root 本轮实际全文读取 A247 六节D1–D16（9308 B，SHA256 ed85200e7b75f24d0f7e7ffa523ba16a3196fd199012657567e15f8d90d04017），C247 七节D1–D14（12786 B，SHA256 2cc22522b952f4b9c6587c9ebdf0e25d4a2a078afcf6221ff8dbf6f9b8c6079c），不是以作者消息代替读稿。旧 L 不可约性、A 整数级数为246已付输入；本稿不增加未实际读的一手定理。

全部推导为纸证，数学程序/CAS/interval/prime/parameter/map/Lean执行0，外 Git mutation0。有限检索不证明新颖性，也未重新核验他人整个论文/Lean 仓库。主目标 active；数值定理未得。
