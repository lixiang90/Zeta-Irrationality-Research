# 第254轮：固定RV投影的实际解析预算与准入缺口

2026-10-10，B。只使用第253轮权威实现：n≥2，r=0,…,4，参数为(10n+r,8n,8n,5n,10n)，前四列的 R=Q/Λ 余数矩阵取 adjugate，第五系数为0。没有更换包、参数、向量、最大minor或数值目标；数学程序、有限头手算、参数/素数/map/word扫描均0。

本稿支付同对象的精确 determinant/primitive 比值、真正有限维 Christoffel 表达，以及更强的普通矩正交。它没有支付实际误差无限非零或 primitive 统一净衰减。建议结束这个默认 adjugate 实现的续轮投入；这不是所有RV方法的不可行性定理。

## 1. 保持完整对象与唯一向量

记 Φ=z⁴+1、Λ=d_(13n+4)d_(12n+4)。从第253轮已经完整支付的原双残数及包含 log 修正的身份，
\[
 F_{n,r}=P_{n,r}-Q_{n,r}\operatorname{Li}_2(1/z),\quad
 Q_{n,r}=\Lambda R_{n,r},\quad R_{n,r}\in\mathbf Z[z],
\]
\[
 R_{n,r}(z)=\frac{(-1)^{n+1}}{(6n)!(7n)!}
 z^{3n}(z-1)^{3n}T_n(\theta)(1-z)^{10n+r},
\quad T_n(v)=\prod_{j=2n+1}^{10n}(v+j)\prod_{j=3n+1}^{8n}(v+j).
\tag{A1}
\]
令 q_j 为 R_(n,r) mod Φ 的第j系数行，M=[q₀;q₁;q₂;q₃]。固定
\[
 D=\det M\ne0,\qquad v=\operatorname{adj}(M)e_0,\qquad v_4=0,
\quad U(t)=\sum_{r=0}^{3}v_rR_{n,r}(t).
\tag{A2}
\]
于是 U≡D mod Φ，Q_n=ΛU，c_n=ΛD。D非零依赖已付的全n Rolle证明，而不是本稿的 Gram 正性。第五列不被重新用来选另一个更小误差。

ρ(t)=−log t，K(t)=(1+t²)/(1+t⁴)，Y=L(2,χ₋₈)。第253轮原完整 I⁽⁰⁾−log(z)I⁽¹⁾的 Cauchy/Gauss 身份给
\[
 A_n-c_nY=\Lambda\mathcal E_n,
 \qquad \mathcal E_n=-\int_0^1\rho(t)K(t)U(t)\,dt.
\tag{A3}
\]
这里不以未修正的正双积分替代 A3。

## 2. 精确替换行与 primitive 内容

定义完整实误差行
\[
 e_r=-\int_0^1\rho K R_{n,r},\qquad
 E_n=\det[e;q_1;q_2;q_3].
\]
沿第一行展开，cofactor正是 adj(M)e₀，故
\[
 \mathcal E_n=e v=E_n,
 \qquad \frac{A_n-c_nY}{c_n}=\frac{E_n}{D}.
\tag{A4}
\]
这是所选的行列式，不是最大绝对值minor或平方和。若 p_r=P_(n,r)/Λ，定义有理完整头行
\[
 a_r=-\sum_k[p_r]_k\chi_{-8}(k),\qquad
 \widehat A=\det[a;q_1;q_2;q_3]=av.
\]
于是 A_n=ΛÂ，E_n=Â−DY。令 d=den(Â)>0，a*=dÂ∈Z，
\[
 g_0=\gcd(|a^*|,|dD|)>0.
\]
因为完整 A_n 是整数，d|Λ；因此原 g=gcd(|A_n|,|c_n|) 恰为
\[
 g=\frac{\Lambda}{d}g_0,\qquad
 (a_n,b_n)=\left(\frac{a^*}{g_0},\frac{dD}{g_0}\right),\qquad
 \ell_n=\frac d{g_0}E_n.
\tag{A5}
\]
若Â=0，按 den(0)=1，仍有g₀=|D|且A5成立。Λ的人工公共尺度完全消去；仍留下实际有理头的分母d及其与dD的公共内容g₀。不能以raw Λ加adjugate高度直接当primitive费用，也不能将Λ全部消去误说成d=1。

可核的严格准入条件因而是：同一E_n有统一上界 |E_n|≤C exp(−σn)，同一内容有 d/g₀≤C′ exp(τn)，且σ>τ，并另证无界n上E_n≠0。两条上界的差须真实严格；D≠0或某个行列式范数正不能代替最后一项。

## 3. 同一四维空间的 Christoffel 公式及其限度

令 w=ρK>0，G_(rs)=∫₀¹w R_rR_s。M可逆使四个R线性无关，所以G实对称正定。设B=[q₁;q₂;q₃]，
\[
 L=G^{-1}-G^{-1}B^T(BG^{-1}B^T)^{-1}BG^{-1},
 \qquad \mathscr K_n=q_0Lq_0^T>0.
\]
约束 Bx=0、q₀x=1 在此实际四维空间中有唯一解 x=v/D。LGL=L，故直接验证
\[
 \int_0^1w\left(\frac{U(t)}D\right)^2dt
 =x^TGx=\frac1{\mathscr K_n},
 \qquad
 \left|\frac{E_n}D\right|\le
 \sqrt{\frac{\int_0^1w}{\mathscr K_n}}.
\tag{A6}
\]
这是合法的有限维、带三条余数约束的 Christoffel 表达；其空间、度数和插值点均固定于A1–A2。它没有把U换成低degree正交多项式。实际 signed mean ∫wU/D 可以为0，A6仅为upper。要取得净预算仍须证明所选空间的𝒦_n增长与primitive b_n高度之间的严格差，或直接控制A5；本稿没有这样的增长证书。

## 4. 全尺度普通矩正交与变号障碍

本包还有较第253轮log矩更长的普通矩消失：
\[
 \int_0^1t^jR_{n,r}(t)\,dt=0,
 \qquad -n\le j\le4n-1,
 \quad 0\le r\le3.
\tag{A7}
\]
证明：置 f=(1−t)^(10n+r)，w_j=t^(3n+j)(1−t)^(3n)。Euler算子的积分伴随为 −θ−1。把13n阶T逐项移到w_j后，
\[
 T_n(-\theta-1)w_j
 =\sum_{i=0}^{3n}(-1)^i\binom{3n}{i}
 T_n(-3n-j-i-1)t^{3n+j+i}=0.
\]
因为3n+j+i+1全在第一组根的区间[2n+1,10n]内。全部边界亦为0：在0，3n+j≥2n>0，Euler伴随保持这一下界；在1，每个边界乘积的总微分阶至多13n−1，而f与w_j的零阶总和是13n+r。两因子不可能同时失去其零。该证明对负j没有偷用0处不可积的单独对象；实际 R 含t³ⁿ。

A7线性组合也适用于U。以正权t^(−n)写成k=0,…,5n−1的普通多项式矩。假设U在(0,1)的变号点少于5n个，以这些点的线性因子构成测试多项式p，再选其整体符号，则t^(−n)U(t)p(t)非负且非恒0，其积分应正，却由A7为0。所有积分在0由U的t³ⁿ可积。因此
\[
 U\text{ 在 }(0,1)\text{ 至少有 }5n\text{ 次变号。}\tag{A8}
\]
这明确排除把所选线性积分A3直接当作常号正Gram的解释；它不排除另一个已证明的signed-integral变换，也不证明A3为零。Rolle的正实根数、A8和正测度并不能共同推出E_n≠0。

## 5. 完整 Mellin 因子与一个诚实的统一upper

令 M_U(s)=∫₀¹t^sU(t)dt，先在Re s>−3n−1定义。U最低degree≥3n、最高degree≤16n+3，故
\[
 \mathcal D_n(s)=\prod_{k=3n}^{16n+3}(s+k+1),\qquad
 M_U(s)=\frac{\mathcal G_n(s)H_n(s)}{\mathcal D_n(s)},
\]
\[
 \mathcal G_n(s)=\prod_{j=-n}^{4n-1}(s-j)
                    \prod_{j=0}^{2n-1}(s-j),
 \qquad H_n\in\mathbf Z[s],\quad\deg H_n\le3n+3.
\tag{A9}
\]
分母乘M_U是整数多项式。U含(1−t)³ⁿ，沿实s→+∞有M_U=O(s^(−3n−1))，所以其 numerator degree≤10n+3。A7给第一组根；第253轮已付的log矩使0,…,2n−1为双根。这些点均不是𝒟的极点。𝒢是monic整数多项式，除尽后H仍整系数。此为全n因子式；s→∞常数可依赖n，不当n能量。

K的χ幂级数及 ∫ρ|U|/(1−t)<∞ 保证绝对交换，给
\[
 E_n=\sum_{k\ge0}\chi_{-8}(k+1)M_U'(k).
\tag{A10}
\]
完整输入仍是A1所选H_n，不是任意degree≤3n+3多项式。这将全部普通/log正交压进同一个算术有理函数，但尚未给该χ求和的符号或统一大小。

确实可以无样本地给一个较粗的uniform upper。K在四个ξ⁴=−1处的residue为(1+ξ²)/(4ξ³)，绝对值√2/4。以t=1/2为中心，每个极点距离²≥5/4−1/√2>1/2。把四个几何级数截到degree2n−1得到实多项式k_n，且在[0,1]
\[
 |K-k_n|<7\,2^{-n}.
\]
因为每项余比至多1/√2，四项总常数至多2/(1−1/√2)=4+2√2<7。log正交消掉k_n，故 |E_n|≤7·2^(−n)∫ρ|U|。

用253全系数正和界，首四列core的l₁≤2^(48n+6)，余数系数≤2^(51n+6)，所以固定v仍有 |v_r|≤6·2^(153n+18)。公共 t³ⁿ(1−t)³ⁿ≤2^(−6n)，而∫ρ=1，得到完整
\[
 |E_n|\le168\,2^{194n+24},\qquad
 |\ell_n|\le168\,2^{194n+24}\frac d{g_0}.
\tag{A11}
\]
它是合法但远未负指数的upper，不是实际增长lower，更不是全方法no-go。没有用它推断primitive误差不衰减。Root同时独立研究更强原积分能量；本稿不把未读消息作为新界输入。

## 6. 本轮判断与实际读域

固定源的两个真实最早缺口现在可精确指出：A4/A10这个选中signed cofactor的无界非零；A5同一有理头内容与同一误差的uniform严格预算。A6不是免费正性，A8说明直接常号机制不存在，A11的upper不足也不证实际失败。没有给数值无理性/LI定理。在没有另一完整核心证书的条件下，不建议因正交或Mellin子引理自动延长此默认实现；保留其数学资产用于全局比较，其他向量、第五列、参数和源仍需新的准入授权。

本轮实际FULL读Root2539888、报告5913及manifest14372；另FULL读B2537244和C2538159作为实际系数核对，FULL复读既存RV物理4–6文本，含定义(2.1)–(2.4)及完整Theorem2.1。不冒称49页全文证明或新增数值文献结论。A7的伴随方向与Mellin压缩曾同Root交流，本稿逐式自含验证；作者自读不是独审。精确输入身份见同轮packet_reading_scope.md。数学程序、有限头手算、下载、扫描及旧producer执行0；只新增本稿与scope，未写旧数学稿/main/policy/manifest。
