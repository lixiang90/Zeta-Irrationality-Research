# 第253轮：固定 RV 包的 χ−8 常数方向全尺度证书

2026-10-10，A；数学程序0。固定第252轮的五列包，不换参数、不运行有限头或 CAS。本文证明实际四次 cyclotomic 余数矩阵对全部 n≥2 满秩，因而支付纯目标系数投影。没有证明投影后数值形式的无限非零、primitive 费用或解析严格余量。

## 1. 实际来源与完整归一化

采用 [Rhin–Viola2005](https://www.numdam.org/item/ASNSP_2005_5_4_3_389_0.pdf) (2.1)–(2.4)、Theorem2.1 的真实双围道对象 I_z^(2)。保持

\[
(h,j,k,l,m)=(10n+r,8n,8n,5n,10n),\quad n\ge2,\quad0\le r\le4,
\qquad\Lambda_n=d_{13n+4}d_{12n+4}.
\]

如252，I_z=I_z^(0)−(log z)I_z^(1)，

\[
F_{n,r}(z)=\Lambda_n z^{16n}(z-1)^{3n}I_z(h,j,k,l,m)
=P_{n,r}(z)-Q_{n,r}(z)\operatorname{Li}_2(1/z),
\quad P_{n,r},Q_{n,r}\in\mathbb Z[z].                  \tag{R1}
\]

这里是完整 RHS，原式的 log/Li₁ 已由 residue subtraction 消去。个别 theorem normalization 的 β=3n−r，乘整数 LCM 比与 (z−1)^r 正好得到 R1。Theorem2.1 还明确给

\[
Q_{n,r}(z)=\Lambda_n z^{16n}(z-1)^{3n} I_z^{(2)}(h,j,k,l,m). \tag{R2}
\]

不把任意超几何猜式代替 R2；下两节直接提取其两个正向 residue。

## 2. 两个真实 residue 的全 n 提取

令 h=10n+r。原内分母为
\[
[x+(z-x)y]^{6n+1},\qquad y_0=-x/(z-x).
\]
展开 y^(8n)(1−y)^(5n) 并取内 residue，得到

\[
\mathop{\rm Res}_{y=y_0}
\frac{y^{8n}(1-y)^{5n}}{[x+(z-x)y]^{6n+1}}
=\sum_{b=0}^{5n}\binom{5n}{b}\binom{8n+b}{6n}
\frac{x^{2n+b}}{(z-x)^{8n+b+1}}.                        \tag{R3}
\]

两个符号 (−1)^b 与 y₀^(2n+b) 中的 (−1)^(2n+b) 正好相消。外部 x^(8n)(1−x)^h 乘进去，在 x=z 取正向 residue；由于 (z−x)^(−8n−b−1) 带 (−1)^(b+1)，有

\[
I_z^{(2)}=z^{-13n}\sum_{c=0}^h(-1)^{c+1}\binom hc z^c
\sum_{b=0}^{5n}(-1)^b\binom{5n}{b}\binom{8n+b}{6n}
\binom{10n+b+c}{8n+b}.                                 \tag{R4}
\]

这是有限的系数恒等式，来自完整 contour 的 residue，不需要任何极限换序。原 normalization z^(−l−m)=z^(−15n)，外导数的剩余 z次数为2n+c，解释 R4 的 z^(−13n)。

内层整数和可完全消去。先写

\[
\binom{8n+b}{6n}\binom{10n+b+c}{8n+b}
=\frac{(8n+c)!}{(6n)!(2n+c)!}\binom{10n+b+c}{8n+c}.
\]

对最后的 binomial 取 v^(8n+c) 系数，使用
Σ_b(−1)^b binom(5n,b)(1+v)^b=(−v)^(5n)，得

\[
\sum_b(-1)^b\binom{5n}{b}\binom{8n+b}{6n}
\binom{10n+b+c}{8n+b}
=(-1)^{5n}\frac{(10n+c)!(8n+c)!}
{(6n)!(7n)!(2n+c)!(3n+c)!}.                             \tag{R5}
\]

所有 c≥0 都合法；没有采样 n 或把 terminating identity 作为猜测。

## 3. 与移位无关的精确算子

令 θ=z d/dz，固定

\[
T_n(\theta)=\prod_{j=2n+1}^{10n}(\theta+j)
\prod_{j=3n+1}^{8n}(\theta+j),
\qquad \kappa_n=\frac{(-1)^{5n+1}\Lambda_n}{(6n)!(7n)!}.
\]

算子 T_n 在 z^c 上的 eigenvalue 正是 R5 中两段 factorial ratio 的乘积。因此 R2–R5 给实际所有五列的统一身份

\[
\boxed{\ Q_{n,r}(z)=\kappa_n z^{3n}(z-1)^{3n}
T_n(\theta)(1-z)^{10n+r}\ },\qquad0\le r\le4.            \tag{R6}
\]

κ_n 非零、与r无关。虽然写法含有 factorial denominator，R1给 Q整系数；也可由 R5 左边的整数和直接核对每个 coefficient。此处不约分Λ_n，不提前领取任何 primitive 净费用。

若需要 contiguous 接口，可保持完全可核的算子形式：对任意实多项式 V，

\[
\sum_{r=0}^4v_rQ_{n,r}
=\kappa_n z^{3n}(z-1)^{3n}
T_n(\theta)\{(1-z)^{10n}V(1-z)\},\quad V(u)=\sum_{r=0}^4v_ru^r.
                                                               \tag{R7}
\]

它比未付的 scalar recurrence 足够强，下一节只用 degV≤3。

## 4. 保持正零点的自含引理

**引理。** 对任意非零实多项式 p 和 a>0，q=(θ+a)p 有至少与p一样多的正实零点，按重数计。

证明：写正根为0<x₁<⋯<x_s、重数m_i。q在x_i至少保留m_i−1重。函数 x^a p(x) 在[0,x₁]连续，0与x₁的值都是0；在内部可微，故有一个导数零点。相邻x_i之间每段再有一个导数零点。所有这些点正且互异，并且

\[
(x^ap(x))'=x^{a-1}(\theta+a)p(x).
\]

总数至少 Σ(m_i−1)+1+(s−1)=Σm_i。若s=0无事需证。q不是零多项式，因为其z^k系数乘非零k+a；其次数与p相同。证明不要求在0可微，因而适用于任何a>0。逐因子迭代，T_n保持正根总数且在实多项式上可逆。                     (R8)

## 5. 实际余数矩阵对全部 n 满秩

令Φ₈(z)=z⁴+1，并写

\[
Q_{n,r}(z)\bmod\Phi_8(z)=\sum_{j=0}^3q_{j,r}(n)z^j.
\]

**定理。** 对全部n≥2，前四列 r=0,…,3 的整数矩阵
\[
\mathcal R_n=(q_{j,r}(n))_{0\le j,r\le3}
\]
可逆。故固定五列的完整余数秩为4，nonconstant三行秩为3。

证明：假设前四列有非零实依赖 v。由R7，这意味着

\[
\Phi_8\mid T_n(\theta)\{(1-z)^{10n}V(1-z)\},
\quad0\ne V\in\mathbb R[u],\quad\deg V\le3,              \tag{R9}
\]

因为公共因子 z^(3n)(z−1)^(3n) 与Φ₈互素，且κ_n≠0。括号中的多项式非零，次数≤10n+3，至少有10n个正实根（z=1，计重数）。R8证明其T_n像仍非零、次数不增、正实根总数至少10n。

然而Φ₈有四个互异的非实根，不能与任何正实根重合。R9于是要求次数至少10n+4，矛盾。此证明甚至排除实依赖，特别排除Q依赖。前四列可逆又使去掉常数行的三行独立；加入第五列不改变这两个秩。                                      (R10)

所以第252轮P12对所有n≥2成立。这不是由五列比三约束多推出的 generic assertion，也没有以一个有限头证明无界结论。

## 6. 显式整数核向量与纯目标形式

设 Δ_n=det𝓡_n∈Z\{0}，e₀=(1,0,0,0)^T。取

\[
(v_{n,0},\ldots,v_{n,3})^T=\operatorname{adj}(\mathcal R_n)e_0,
\qquad v_{n,4}=0.
\]

则𝓡_n v=Δ_n e₀，因而

\[
\sum_{r=0}^4v_{n,r}Q_{n,r}\equiv\Delta_n\pmod{z^4+1}.   \tag{R11}
\]

这是固定五列包中的合法向量；只使用其已证可逆的前四列，不是更换包。Δ_n的非零现已支付，但它是 coefficient determinant，不是最后数值线性形式。

令χ=χ−8、ζ=e^(πi/4)、τχ=i√8，Y=L(2,χ)。继续用252的索引 z=ζ^(−a)，a=1,3,5,7，并以 R1 的 canonical continued integral 定义这些值。全部归一化仍是Λ_n z^(16n)(z−1)^(3n)。R11以及有限 Gauss 和给

\[
\frac1{\tau_\chi}\sum_a\chi(a)\sum_rv_{n,r}F_{n,r}(\zeta^{-a})
=A_n-\Delta_nY,\qquad A_n\in\mathbb Z.                  \tag{R12}
\]

具体若ΣvP_nr=Σ_kp_kz^k，则A_n=−Σ_kp_kχ(k)；τχ^(−1)Σχ(a)ζ^(−ak)=−χ(k)。额外导子清整常数仍是1，没有漏掉Li₁/log或固定2处。R12在全部n≥2都有非零目标系数Δ_n。

## 7. 首关通过的准确范围

已付：同一真实 double-contour 的全n系数公式R6、前四列全n可逆、显式整数向量R11、完整纯目标形式R12。这里的 Δ_n≠0 不意味着 A_n−Δ_nY≠0。后者可能发生真实值相消，仍需独立的无限非零证书。

同样未付：adjugate向量的可用高度与共同 primitive 内容、四个复杂积分的统一严格解析余量，以及这些项在同一完整归一化下的净预算。R8不是可搬用的能量估计，R1的安全LCD不是净费用。这一结果只通过253规定的系数交关，不自动开启参数、素数或地图优化，也不宣称新数值无理性。

本文只读252冻结稿与已存RV选页；没有新网页或PDF下载、数学程序或扫描。本人保存后实际完整复读本稿与读取范围，作者自读不冒充独立审阅。
