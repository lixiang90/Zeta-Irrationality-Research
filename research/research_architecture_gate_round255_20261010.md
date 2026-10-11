# 第255轮：函数族扩张的真实接口与完整参数单值化投影

本稿是跨架构比较的 Root 数学部分。目的为选择下一项可检验的完整接口，不声称已证明新的数值 ζ/L 无理性或线性无关性。第254轮固定 RV adj(R)e0 实现仍结束默认投入；不把粗 upper 的失败升格为实际误差下界。

## 1. UDC 的层级提升不能按名称移植

实际完整读 CDT《The Unbounded Denominators Conjecture》PDF20–21、25–29、49、51–52页，保存原页提取于 literature/architecture_sources_round255_20261010/root_udc_pdf20_21_25_29_49_51_52.txt。这是精确选段读域，未声称整篇62页重新全文核验。

原 Proposition3.0.1 对有界分母、有限 cusp width 的模函数给 dim_{Q(λ)}R_{2N}≤CN³logN；Theorem4.3.1 用 amalgam/CSP/Ihara 类型论证证明 f(pτ) 不属于旧源和新 congruence field 生成的代数。Theorem4.3.2 于是使相对扩张次数每个新 prime 至少翻倍。Proposition4.3.5 结合 congruence field 的 N³ 基准次数，比剩余 O(logN) 上界得到矛盾。这是相对 field degree 的倍增，不能简写成每次多一个 Taylor 行。

必要接口包括：实际模函数及有限指数不变群、全部 Fourier 系数有界分母、所有 cusp width 控制、旧 field 与新 congruence field 的交以及新源非包含性。目标值有理不能自动保证这些条件。Eichler integral 或多对数扩张不是有限指数模函数，仅有 degeneracy map 或 q→q^p 的形式不领原4.3.1。

### 一个自含的直接使用障碍

对整数 s≥2，θ=z d/dz，有

\[
[(1-z)\theta-1]\theta^s\operatorname{Li}_s(z)=0.
\]

任何在 {0,1,∞} 外无奇点的有理系数齐次线性算子若消去 Li_s，其解空间也包含其所有解析延拓差。绕1的标准正向局部单值化满足

\[
\Delta_1\operatorname{Li}_s(z)=-\frac{2\pi i}{(s-1)!}(\log z)^{s-1}.
\]

证明从 Li_1=−log(1−z) 开始，用 dLi_s=Li_{s−1}dz/z 归纳；s≥2 的差在 z→1 时趋零确定积分常数。故循环解空间含非恒定 log 多项式。绕0的 m 次作用为 log z→log z+2πim，在该多项式上对所有 m≥1 不恒等。因此最小循环方程的0局部 monodromy 无限；这不仅是某个非最小算子人为加入 log 的现象。

替换 z=16x 仅把1移至1/16。任何有限覆盖 x=t^d 对0的 monodromy 取 d 次幂，仍无限；有理 gauge 的共轭也不改变有限性。因此不能直接对该完整多对数循环模块使用原 Theorem7.2.1 的「0局部 monodromy 有限」条件。特定新商、投影或关系源可能改变模块，但必须证明它保留目标值并真正删除障碍；本论证不排除所有 ζ/L 变形。

## 2. 下一候选的真实新接口：完整区间，参数绕行投影

以下独立手推核对 A 的新 carrier。保持当前 Catalan foundations 的完整矩

\[
m_i=\int_{-1}^1t^i\frac{|t|}{\sqrt{1-t^2}}dt,
\qquad M_a(i,j)=\sum_{u\ge0}\frac{a^u m_{i+u}}{j+u+1},\quad |a|<1.
\]

等价为完整 (−1,1)×(0,1) Cauchy 核 (1−ats) 的双积分；不截半区，不省端点。设 S_i(a)=Σ_{u≥0}a^u m_{i+u}，φ=arcsin a，f=√(1−a²)，均取0附近 Taylor branch。由对称性和 t=sinθ 得

\[
S_0=\frac{2\varphi}{af},\quad M_a(0,1)=\frac{\varphi^2}{a^2},\quad
aM_a(0,0)=2\int_0^{\varphi}\frac{v}{\sin v}\,dv.
\]

后两式也可由当前 foundations 的 inverse-binomial 矩展开验证。取 a=1/√2，Y=L(2,χ_{−8})，ℓ=log(1+√2)。log tan(v/2)=−2Σ_{k odd}cos(kv)/k；在0到π/4上积分及分部积分，sin(kπ/4)=χ_{−8}(k)/√2，得到

\[
M_a(0,0)=4Y-\frac{\pi}{\sqrt2}\ell,
\quad S_0=\pi,\quad M_a(0,1)=\frac{\pi^2}{8}.
\]

令 T 为参数 a 绕 +1 一次而不绕0或−1的解析延拓。选择路径后 φ→π−φ，f→−f。φ 路径从π/4至3π/4没有碰到 sinφ=0。

\[
\Delta(aM_a(0,0))=2\int_{\pi/4}^{3\pi/4}\frac{v}{\sin v}dv
=\pi\int_{\pi/4}^{3\pi/4}\frac{dv}{\sin v}=2\pi\ell.
\]

因此 TM00=M00+2√2πℓ，TS0=−3π，TM01=9π²/8。完整 sheet 组合 \bar M=(3+T)M、\bar S=(3+T)S 的 starts 恰为

\[
\boxed{\bar M(0,0)=16Y,\qquad \bar S_0=0,\qquad
\bar M(0,1)=\frac{3\pi^2}{2}=9\zeta(2).}
\]

注意 (3+T) 对常数为乘4，不是幂等 projector；以上是指定线性组合。新 sheet 不是原正实积分的另一正分量。

### 全数组传播及全 raw pool 的接触消元

以下等式先由 |a|<1 的绝对收敛级数证明，再解析延拓到指定 sheets；有理右侧受 (3+T) 后必须乘4：

\[
\bar M(i,j)-a\bar M(i+1,j+1)=\frac{4m_i}{j+1},\qquad
\bar S_i-a\bar S_{i+1}=4m_i.
\]

\bar S0=0 使全部 \bar S_i 在 K=Q(√2)。以 \bar K^-_d=\bar M(d,0)、\bar K^+_d=\bar M(0,d) 记边界，由原 moment recurrence 的同一逐项恒等式得到

\[
d\bar K^-_d=(d-1)\bar K^-_{d-2}+\bar S_{d-2}-\bar S_d\quad(d\ge2),
\quad\bar K^-_1=8/a;
\]

\[
(d-1)a^2\bar K^+_d=(d-2)\bar K^+_{d-2}+\frac8{d-1}\quad(d\ge2).
\]

后一式未投影时右侧还含 (a²−1)S0；投影后严格为零。以 starts 16Y、9ζ(2) 和 diagonal reduction 归纳，所有 i,j≥0 的 \bar M(i,j)∈K+KY+Kζ(2)，不仅有限头。Y 系数为16 a^{−j}c_{(i−j)/2}；ζ(2)系数为9a^{1−j}c_{(j−i−1)/2}，c非法指标取0。

对任何整数多项式 P,D 满足 tP/f(t)−D=O(t^L)，同一个完整 raw pool 0≤j<L 有

\[
\widehat F_j(P,D)=a^j\bar M(P,j)-9aZ(D,j)\in K+KY,
\]

因为 ζ(2)系数恰为9a[t^j](tP/f−D)=0。其 Y 系数为

\[
16\sum_i[t^i]P\,c_{(i-j)/2}.
\]

故它保留全 Catalan coefficient kernel 的非平凡真实目标投影，不是单个 start 猜测。原多项式 P_r,D_r、全部必要 raw columns 及整数 filter 可作为一个具体候选；此刻不选择或扫描新的比例参数。

## 3. 优先的完整有理归一化与真实全尺度目标秩

B 的进一步归一化经 Root 独立核对：设 N(i,j)=a^i\bar M(i,j)，μ_i=a^i m_i，U_i=a^i\bar S_i。m_i 奇数支撑为零、a²=1/2，故 μ_i∈Q；U0=0，U_i−U_{i+1}=4μ_i，全部U_i∈Q。三个递推写为

\[
N(i,j)-N(i+1,j+1)=\frac{4\mu_i}{j+1},
\]

\[
dN(d,0)=(d-1)a^2N(d-2,0)+a^2U_{d-2}-U_d,
\quad N(1,0)=8,
\]

\[
(d-1)a^2N(0,d)=(d-2)N(0,d-2)+\frac8{d-1}.
\]

因此它的完整 head 实际在Q，具体为

\[
N(i,j)=R_{ij}+16Y\,a^{i-j}c_{(i-j)/2}
+\frac32\pi^2\,a^{i-j+1}c_{(j-i-1)/2},\qquad R_{ij}\in Q.
\]

两个 period 系数的非零指数均为偶数，均为有理数；此处是明确构造的系数分解，不假设未知 Y 与π²已线性无关。优先的完整 raw 形式为

\[
F_j(P,D)=N(P,j)-9Z(D,j),\qquad
\frac{xP(x)}{\sqrt{1-2x^2}}-D(x)=O(x^L),\quad j<L.
\]

全 pool 的π²系数为(3/2)[x^j](xP/√(1−2x²)−D)，故 F_j∈Q+QY。该 moment-array 无需两 K 嵌入；与上一 K 归一化比较后，选此有理版本继续。a^i 的实处行费用仍必须计入，不能因系数有理而免费。

一个无需有限n扫描的具体全尺度行族是 n≥1、r=0,…,n−1：P_r(x)=2^n x^{2r}，D_r 为 xP_r/√(1−2x²) 的 <2n jet。其系数为 2^{n-l}binom(2l,l)，0≤l≤n−r−1，故P_r,D_r∈Z[x]，全部raw j<2n接触消元。在选列j=2s、s=0,…,n−1的 n×n Y系数矩阵中，s>r 时为零，s=r 时为16·2^n，故det=(16·2^n)^n≠0，ALL n≥1。

这是实际新 full-sheet carrier 的目标系数秩；不是关系点行列式非零，亦非旧positive Gram的复用。原48N Chebyshev行族及其全部有限处/实处证书不因此适用于这些行。

## 4. 唯一下一首关与停止条件

下一第256轮（同时为定期全局回顾）只检验上述 a=1/√2、3+T、N(i,j)=a^i\bar M、完整 raw pool 及所给全尺度整数接触行族：给出包含两张参数 sheets 的实际双变量生成芽/contour表示，证明它逐项匹配 F_j，给全 degree prefix 的 Z-整数模型和 exp(O(degree)) 级可核成本，并给选取全部列时的完整行尺度费用。泛用factorial导致的 exp(O(degree logdegree)) certificate 不作为进入quadratic总费用比较的准入证书。若只得到形式 recurrence、不匹配实际 contour，或不能支付全部 raw columns 与所选行归一化，则该 carrier 不进入后续无界非零/能量阶段；不自动开参数、prime、sheet-word扫描。已证明的目标系数秩保留，但不会替代下一首关。

即使第一接口通过，仍分别缺：关系点完整行列式无界非零；包含 successor/digit layers 的足够强有限处费用；同一个两sheet投影对象的全实处能量。原 Catalan 三个 base matrices、prime bounds、严格实能量均不能直接继承。当前只得到新的完整周期接口、ALL n目标系数秩与一个有界下一检验，没有新数值无理性定理。
