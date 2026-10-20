# 第280轮独立公式证明：实际非对角复Beta配对的可分性

2026-10-20，作者 `/root/sv_formula_280`。唯一写入本文件。恢复时实际子goal为null，未另建goal；根goal由根核定。已核初始git状态为空、状态修订20，读AGENTS、长期goal、280章程、279周期来源；遵守当前一个完成轮的来源窗口。这里固定指定ζ(7)的完整反证ζ(7)=u/v，u∈Z、v>0、gcd(u,v)=1；不假设任何其余奇ζ有理。本文件证明该窗口的首公式，不交付反证整数或数值无理性结论。

**结论：章程的候选公式对全部整数i,j≥1成立。** 下面从每对实际收敛条带直接作Schwinger积分证明，不用相邻整数移位积分的分部积分，不从对角开平方。结果为

\[
 \boxed{\mathcal K_{ij}(t)=B(t)v_i(t)v_j(t)},\qquad
 v_i(t)=\frac{(t)_i^2}{(2t)_{2i}},\quad
 B(t)=\frac t2\frac{\Gamma(t)^2\Gamma(1-2t)}
 {\Gamma(2t)\Gamma(1-t)^2}.
 \tag{F280.1}
\]

右侧在t=0解析。因v_i具有一阶零，固定9jet总矩阵的全m秩至多8，ζ7系数矩阵精确秩1；增长Gram入口因而触发章程停止条件。这里的秩界是结构定理，不能替数值无理性。

## F280.2 实际积分、相位和收敛域

记Q(z)=z(1−z)，d²z=dxdy，

\[
 I_{ij}(t)=\frac1\pi\int_{\mathbb C}
 Q(z)^i\overline{Q(z)}^{\,j}|Q(z)|^{2t-2}\,d^2z,
 \qquad \mathcal K_{ij}=\frac t2\operatorname{AC}I_{ij}.
 \tag{F280.2}
\]

|Q|^{2t−2}的含义固定为exp((2t−2)log|Q|)，其中log|Q|是实对数；i,j为整数，多项式因子没有选支。原点与1处绝对值为常数阶r^{i+j+2Re t−2}，加面积元要求i+j+2Re t>0；无穷远为r^{2i+2j+4Re t−4}，加面积元要求2i+2j+4Re t−2<0。因此恰当的绝对收敛条带为

\[
 -\frac{i+j}{2}<\operatorname{Re}t<\frac{1-i-j}{2}.
 \tag{F280.3}
\]

每个闭子条带上，带任意有限次log|Q|因子的绝对积分仍收敛，所以Iij是该条带上的全纯函数。整矩阵无需共同条带，也没有把求9jet移进原积分。对变量作z↦bar z，测度和|Q|不变，故在各自同一条带上Iij(t)=Iji(t)；另外取复共轭得overline(Iij(t))=Iji(bar t)。这些是两条不同身份；没有把复杂参数t错误地认成实数。

## F280.3 一项全条带合法的Gaussian评价

先令i≥j，d=i−j≥0，s=t+j。对实参数

\[
 -d/2<s<(1-d)/2
 \tag{F280.4}
\]

原积分成为

\[
 I_{ij}(t)=\frac1\pi\int_{\mathbb C}
 Q(z)^d |z|^{2s-2}|1-z|^{2s-2}\,d^2z.
 \tag{F280.5}
\]

该区间始终非空，且1−s>0、1−2s>0、s+d>0。用正实Laplace核

\[
 |z|^{2s-2}=\frac1{\Gamma(1-s)}
 \int_0^\infty u^{-s}e^{-u|z|^2}\,du
 \tag{F280.6}
\]

及其1−z版本。全部换序有绝对依据：把Q(z)^d换成|Q(z)|^d，正核先用Tonelli还原为Γ(1−s)²倍的(F280.5)绝对积分，而它由(F280.3)有限。故

\[
 I_{ij}(t)=\frac1{\pi\Gamma(1-s)^2}
 \int_{u,v>0}u^{-s}v^{-s}
 \int_{\mathbb C}Q(z)^d e^{-u|z|^2-v|1-z|^2}\,d^2z\,du\,dv.
 \tag{F280.7}
\]

固定u,v>0，置λ=u+v、c=v/λ，完成平方得

\[
 u|z|^2+v|1-z|^2=\lambda|z-c|^2+\frac{uv}{\lambda}.
\]

任意全纯多项式p均满足

\[
 \frac1\pi\int_{\mathbb C}p(z)e^{-\lambda|z-c|^2}\,d^2z
 =\frac{p(c)}\lambda.
 \tag{F280.8}
\]

证明是有限Taylor展开p(c+w)并逐项积分：所有w^k、k>0的完整圆周矩为0，常数项的Gaussian积分为π/λ。绝对收敛使这个有限展开合法。取p=Q^d，Q(c)=uv/λ²，代回(F280.7)，得到

\[
 I_{ij}(t)=\frac1{\Gamma(1-s)^2}
 \int_{u,v>0}u^{d-s}v^{d-s}
 (u+v)^{-2d-1}e^{-uv/(u+v)}\,du\,dv.
 \tag{F280.9}
\]

这些步骤没有把一个发散的多项式积分拆为不收敛的相邻shift积分；Gaussian矩是在固定正u,v时计算的有限全纯多项式。

## F280.4 Gamma身份与唯一延拓

在(F280.9)置u=λx、v=λ(1−x)，0<x<1，Jacobian为λ。λ幂恰为λ^{−2s}，所以

\[
 \begin{aligned}
 I_{ij}(t)
 &=\frac1{\Gamma(1-s)^2}
 \int_0^1[x(1-x)]^{d-s}
 \int_0^\infty\lambda^{-2s}e^{-\lambda x(1-x)}\,d\lambda\,dx\\
 &=\frac{\Gamma(1-2s)}{\Gamma(1-s)^2}
 \int_0^1[x(1-x)]^{d+s-1}\,dx\\
 &=\frac{\Gamma(1-2s)\Gamma(s+d)^2}
 {\Gamma(1-s)^2\Gamma(2s+2d)}\\
 &=\frac{\Gamma(t+i)^2\Gamma(1-2t-2j)}
 {\Gamma(1-t-j)^2\Gamma(2t+2i)}.
 \end{aligned}
 \tag{F280.10}
\]

λ积分和Euler积分的参数均严格为正，正是(F280.4)的三个已核不等式。证明首先覆盖非空实开区间；Iij在(F280.3)全纯，Gamma右侧的四个参数1−2s、s+d、1−s、2s+2d在对应复条带上实部均为正，因而也全纯。恒等定理给整个复条带上的相等。Gamma右侧由此提供全t平面的唯一亚纯延拓，后续可能的极点依Γ商本身计算；不能另选任意counterterm改变它。i<j时先用Iij(t)=Iji(t)对调，然后同理，得到全部i,j的延拓。

为了把右侧化为(F280.1)，只在避开所有极点的开集使用Γ递推，随后按亚纯恒等式延拓：

\[
 \frac{\Gamma(t+i)^2}{\Gamma(t)^2}=(t)_i^2,
 \quad\frac{\Gamma(2t)}{\Gamma(2t+2i)}=\frac1{(2t)_{2i}},
\]
\[
 \frac{\Gamma(1-2t-2j)}{\Gamma(1-2t)}=\frac1{(2t)_{2j}},
 \quad\frac{\Gamma(1-t)^2}{\Gamma(1-t-j)^2}=(t)_j^2.
 \tag{F280.11}
\]

第三项的2j次递推符号为(−1)^{2j}=1，第四项的(−1)^j被平方；没有漏掉(−1)^{i−j}、额外π或i的相位。乘四项恰为vi vj，而非仅对角平方。i=j立即恢复279已证的(t)_i^4/(2t)_{2i}²。上式对称于i,j且系数实，故延拓保持Kij(t)=Kji(t)、overline(Kij(t))=Kji(bar t)。

## F280.5 固定jet的直接后果与有效范围

写

\[
 v_i(t)=t w_i(t),\qquad
 \alpha_i=w_i(0)=\frac{((i-1)!)^2}{2(2i-1)!}>0,
 \quad c_r=([t^r]w_i(t))_{i=1}^m\in\mathbb Q^m.
 \tag{F280.12}
\]

B(t)在0处的7jet为

\[
 B(t)=1+4\zeta(3)t^3+12\zeta(5)t^5
 +8\zeta(3)^2t^6+36\zeta(7)t^7+O(t^8).
 \tag{F280.13}
\]

因此对实际M_m=([t⁹]Kij)，令Hr=Σa+b=r ca cbᵀ，得到完整周期矩阵

\[
 M_m=H_7+4\zeta(3)H_4+12\zeta(5)H_2
 +8\zeta(3)^2H_1+36\zeta(7)H_0.
 \tag{F280.14}
\]

每列均在c0,…,c7的实际实span内，故对每个m≥1，不依赖任何ζ值的代数独立假设，rank_R M_m≤min(m,8)。这个上界比未使用vi的一阶零时的10更紧。完整亚纯核本身在避开离散零极点的参数处秩1；固定jet可能增加秩，但不能无界增加。ζ7的形式系数矩阵是36ααᵀ，每个m≥1均精确rank1。这并不单独断言实际M_m秩等于8，也不把形式周期span当实数线性独立；实际精确秩可由另一独审另证。

公式不领取未正则化积分的正性。即使小实t处(F280.1)给出秩1正半定核，也不能由此推其9阶Taylor系数矩阵正半定。没有证明全反证下新的整数非零、清整费、degree·log v或严格解析净余量。按章程，本固定9jet增长Gram来源因统一有界秩已应在一轮到期关闭；本文件不提出升jet、换下标或下一路线。

## F280.6 一手交叉核查与执行范围

实际浏览一手[Neretin，SIGMA 16 (2020) 072](https://sigma-journal.com/2020/072/sigma20-072.pdf)，正文第2页§1.1式(1.4)、第3页§1.2.3 double powers，以及第4页§1.3式(1.7)、(1.8c)。其一般复Beta的Γ商与(F280.10)一致；整数指数差使double powers单值。作者在那里改用Im指数的Gamma规范会去掉旧文的i因子，本文未将两种Γ规范混用。实际积分归一完全由(F280.2)、(F280.6)–(F280.10)自足固定，没有把该论文全篇作为已核输入。

另浏览[Neretin的Ramanujan Journal论文](https://d-nb.info/1211869059/34)§1.1及§2.2式(2.1)作定位。其所印收敛条件有sum<2一项；本文不采纳该条件，实际无穷远检验要求相应平均参数之和<1。该来源记录只用于准确划定实际读域，不是新的文献定理。

没有执行数值、符号CAS、参数/素数/规模扫描，也未改program、STATE、章程或其它资产。自足推导等待根及第三方独审；本作者不把自己的证明计作独立复核。

审核补记：随后只读逐式核[独立秩稿](sv_beta_rank_round280.md)R1–R13及[根结算](sv_beta_pairing_round280.md)S280.3–S280.8，全部通过。R7的评价矩阵是行j、列i的下三角矩阵，评价点−1,…,−k的Vandermonde与对角乘积有相同的(−1)^{k(k−1)/2}，故符号确为正；从多项式系数除回共同分母jet精确除以((1/2)_k)^k，无漏4次幂或阶乘。H的反对角为1、反三角支撑给detH=1；任意实背景连续缩零不经过奇异矩阵，给惯性(4,4)。A_m在m≥8满列，故实际rank8、惯性(4,4,m−8)及ker M=ker Aᵀ均成立；m<8没有据此过推非退化。任意8×8子式的分解只有两个8×8有理A子式和detH=1，因此确为有理数，并不需要周期独立。根的S280.3–8与本稿实际积分、相位、归一及固定9jet一致。此复核没有外部新增读域、数值或符号计算，也不认证根结算中的组织/发布执行状态；280文件此后冻结，不提前执行281。
