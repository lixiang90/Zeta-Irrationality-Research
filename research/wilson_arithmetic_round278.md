# 第278轮：同一双quarter平方余项的完整安全算术证书

2026-10-20，独立算术子任务；只写本文件。开始核实际子goal为null，不创建或恢复goal；已运行状态工具，读取AGENTS、STATE、长期goal、278章程及277的W1–W15。实际主目标仍为指定 \(L(2,\chi_{-8})\) 的新无理性；完整反证为 \(L=u/v\)、\(u\in\mathbf Z,v>0,\gcd(u,v)=1\)。固定原W9两个quarter、shift=degree=n，不换目标或载体。不执行数学程序、n/prime扫描或新的有限诊断；以下为一般代数与全部素数幂证明。

**结论：** 本稿支付W9全部分母并给出一个线性指数的完整整数对，净安全率仍为 \(8+12\log2>0\)。实际最小分母的唯一剩余信用是该完整整数对的共同内容，尚未证明足够的全尺度下界。不是用单q分母当实际费用，也不是实际最小费用的正下界；本轮安全证书不足，不能据此证明L无理或否定全部子列。

## 1. 同一正交来源的整数递推对

沿用[W4–W7](wilson_square_source_round277.md)的真实测度及正交归一。令

\[
P_n(y)=(-1)^n((n+1)!)^2T_n(y),\qquad
Q_n(t)=(-1)^nP_n(-t)=((n+1)!)^2q_n(\sqrt t).
\]

首一多项式的中系数已由W6给出 \(\beta_n=(n+1)(2n+3)\)。其范数是
\(\|P_n\|^2=((n+1)!)^4/[2(n+1)]\)，故三项递推另一系数为

\[
\gamma_n=\frac{\|P_n\|^2}{\|P_{n-1}\|^2}=n(n+1)^3.
\]

因此

\[
Q_0=1,\quad Q_1=t+3,\quad
Q_{n+1}=(t+\beta_n)Q_n-\gamma_nQ_{n-1}\in\mathbf Z[t].
\tag{A278.1}
\]

定义同一差商的伴随多项式

\[
R_n(t)=\int\frac{Q_n(t)-(-1)^nP_n(y)}{t+y}\,d\mu(y).
\]

这里 \(y=x^2\)，并未更换积分或伴随对象。将A278.1的差式除以t+y再积分，余项为 \(\int(-1)^nP_n\,d\mu\)，对n≥1由正交性为0。因此R满足同一递推，\(R_0=0,R_1=1/2\)。特别

\[
2R_n\in\mathbf Z[t],\quad \deg(2R_n)=n-1,\quad
\operatorname{lc}(2R_n)=1,\qquad
S_n(a)=\frac{R_n(a^2)}{((n+1)!)^2}.
\tag{A278.2}
\]

这已整体支付W3所有Bernoulli矩；不能再以逐项矩的表观分母另加费用。接下来还会消掉本递推的过大阶乘清整，不能将A278.1的gross整数Q直接当最小费用。

## 2. q的全部奇处与精确二处

记 \(b\in\{4n+1,4n+3\}\)、\(a=b/4\)。W4有精确恒等式

\[
a^2q_n(a)=\sum_{k=0}^n\binom nk
\binom a{k+1}\binom{a+k}{k+1}.
\tag{A278.3}
\]

因为 \(a\in\mathbf Z_p\) 对每个奇素数p成立，整数值二项式多项式在 \(\mathbf Z_p\) 上p整，故A278.3证明 \(a^2q_n(a)\) 在所有奇p均整。这包含p的全部幂，不只p≤n或一阶模p。

另一方面，W4第k项的二处赋值为

\[
v_2\binom nk-4k-2v_2((k+1)!).
\]

其中 \(b^2-16h^2\) 恒奇。k=n项的赋值严格小于所有k<n项：与第k项之差为
\(v_2\binom nk+4(n-k)+2[v_2((n+1)!)-v_2((k+1)!)]>0\)。所以没有二处抵消，且

\[
\nu_n:=4n+2v_2((n+1)!),\qquad
v_2q_n(b/4)=-\nu_n.
\tag{A278.4}
\]

结合A278.3，得到两个正奇整数

\[
\boxed{B_{n,b}=2^{\nu_n}b^2q_n(b/4)\in2\mathbf Z+1.}
\tag{A278.5}
\]

按W12及 \(v_2((n+1)!)=n+1-s_2(n+1)\)，每个固定quarter满足

\[
\lim_{n\to\infty}\frac{\log B_{n,b}}n=6\log2+\log\rho,
\quad \rho=(11+5\sqrt5)/2.
\tag{A278.6}
\]

这是完整安全整数q分子的大小，并非实际r_n最小分母的下界。

## 3. S的全部奇素数幂：实际Newton矩与lcm平方

本节机制由根提出，本代理独立逐式重建；不是自审根的最终稿。令

\[
\mathcal R_k(y)=\frac{\prod_{h=1}^k(h^2+y)}{(k!)^2},\qquad
T_n(y)=\sum_{k=0}^n\frac{(-1)^k\binom nk}{(k+1)^2}\mathcal R_k(y).
\]

\(\int T_0=1/2\)、\(\int T_n=0\) 对n≥1成立，二项反演遂给

\[
\int\mathcal R_k(y)d\mu(y)=\frac{(k+1)^2}2.
\tag{A278.7}
\]

这对所有k的一般证明比逐项计算Bernoulli数更直接。置

\[
\mathcal A_k(z)=\int\frac{\mathcal R_k(z)-\mathcal R_k(y)}{z-y}d\mu(y).
\]

因 \(\mathcal R_k=(y+k^2)\mathcal R_{k-1}/k^2\)，A278.7给

\[
\mathcal A_0=0,\quad
\mathcal A_k(z)=\frac{z+k^2}{k^2}\mathcal A_{k-1}(z)+\frac12
=\frac12\sum_{j=1}^k\prod_{h=j+1}^k\frac{z+h^2}{h^2}.
\tag{A278.8}
\]

在同一z=−a²处，乘积精确等于

\[
\prod_{h=j+1}^k\frac{h^2-a^2}{h^2}
=(-1)^{k-j}\frac{\binom{a-j-1}{k-j}\binom{a+k}{k-j}}{\binom kj^2},
\quad
S_n(a)=-\sum_{k=1}^n\frac{(-1)^k\binom nk}{(k+1)^2}\mathcal A_k(-a^2).
\tag{A278.9}
\]

空积按1；j=k项亦包含。上述两个泛化二项式在所有奇p均p整。

令 \(d_m=\operatorname{lcm}(1,\ldots,m)\)，\(d_m^{\rm odd}\) 为其奇数部分。对0≤j≤k，有

\[
(k+1)\binom kj\mid d_{k+1}.
\tag{A278.10}
\]

逐p幂证明如下：其赋值是

\[
\sum_{\ell\ge1}\left(
\left\lfloor\frac{k+1}{p^\ell}\right\rfloor
-\left\lfloor\frac j{p^\ell}\right\rfloor
-\left\lfloor\frac{k-j}{p^\ell}\right\rfloor\right).
\]

每个括号是0或1，p^ℓ>k+1时为0，故总和≤\(\lfloor\log_p(k+1)\rfloor=v_p(d_{k+1})\)。这已涵盖所有高次幂，不能只用p层的组合恒等式替代。

把A278.10代入A278.9便得：对所有奇p，\(d_{n+1}^2S_n(a)\) p整。记

\[
u_n=(d_{n+1}^{\rm odd})^2.
\tag{A278.11}
\]

A278.2另给S的精确二处：在t=b²/16处，\(2R_n(t)\) 的首项赋值 \(-4(n-1)\) 严格小于全部低项。因此n≥1有

\[
v_2S_n(b/4)=3-\nu_n,
\quad
\boxed{C_{n,b}=2^{\nu_n-3}u_nS_n(b/4)\in2\mathbf Z+1.}
\tag{A278.12}
\]

这将全部矩、associated多项式、odd素数幂及二处放在同一对象中，而非只付q。由A278.5与12，真实商是

\[
\boxed{\frac{S_n(b/4)}{q_n(b/4)}=
\frac{8b^2C_{n,b}}{u_nB_{n,b}}.}
\tag{A278.13}
\]

## 4. 外a幂、全部prefix和双镜像的完整整数对

将A278.13代入原W9，个别尾部准确为

\[
\frac{U_n(b/4)}{16}
=\frac{b+4}{2b^3}-\frac{32C_{n,b}}{b\,u_nB_{n,b}}.
\tag{A278.14}
\]

每个尾部的v₂均为−1，但两个b均奇，其二倍均为二处奇单位，故相加为二处整数。完整prefix则为

\[
\mathcal P_n=\sum_{k=0}^{n-1}(-1)^k
\left(\frac1{(4k+1)^2}+\frac1{(4k+3)^2}\right),
\tag{A278.15}
\]

原本已在二处整。因此**完整r_n二处整**；不能由个别tail的1/2反推r_n有二分母。

对n≥1记 \(b_1=4n+1,b_3=4n+3\)，取

\[
\ell_n=(d_{4n-1}^{\rm odd})^2,\qquad
\boxed{M_n=\ell_n b_1^3b_3^3B_{n,b_1}B_{n,b_3}\in2\mathbf Z+1.}
\tag{A278.16}
\]

u_n整除ℓ_n；全部prefix的奇分母也整除ℓ_n。定义两个明确的奇整数

\[
X_{n,b}=\frac{M_n(b+4)}{b^3}
-\frac{64M_nC_{n,b}}{b\,u_nB_{n,b}},
\qquad
N_n=M_n\mathcal P_n+\frac{(-1)^n}2(X_{n,b_1}+X_{n,b_3}).
\tag{A278.17}
\]

各商确为整数，X第一项奇、第二项偶，故两个X之和偶，N_n为整数。A278.14–15直接给

\[
\boxed{r_n=N_n/M_n.}
\tag{A278.18}
\]

这是一份同一实际r_n的完整整数对，包括两个quarter、全部prefix、外a⁻³、真实伴随商和二处合并。没有引用旧WZ/Catalan/RV的内容费用。

若 \(g_n=\gcd(M_n,N_n)>0\)，则实际既约对为

\[
A_n=N_n/g_n,\qquad d_n=M_n/g_n.
\tag{A278.19}
\]

这不是约分的估计，而是精确最小分母桥。所有可能跨prefix、跨镜像和同素数高幂的抵消都保存在这一g_n中，不能从分别清整的乘积再领取未证信用。

## 5. 全尺度安全费用与尚未支付的唯一净信用

由 \(\log d_m=m+o(m)\)、\(\log d_m^{\rm odd}=m+o(m)\)，及A278.6，得到

\[
\lim\frac{\log M_n}{n}=8+12\log2+2\log\rho.
\tag{A278.20}
\]

原W14已独证同一r_n的精确裸率，所以这份**完整安全整数形式**有精确率

\[
\boxed{\lim\frac1n\log\bigl(M_n|L-r_n|\bigr)=8+12\log2>0.}
\tag{A278.21}
\]

按原完整反证 \(L=u/v\)，非零整数仍为
\(0<|vd_n(L-r_n)|=|ud_n-vA_n|\in\mathbf Z\)；v固定不影响线性率。对任何事先指定的无界子列 \(\mathcal N\)，A278.19–21严格等价地给

\[
\limsup_{n\in\mathcal N}\frac1n\log(d_n|L-r_n|)
=8+12\log2-
\liminf_{n\in\mathcal N}\frac{\log g_n}{n}.
\tag{A278.22}
\]

因此在本严格负线性指数接口内，所需的完整共同内容证书正是

\[
\liminf_{n\in\mathcal N}\frac{\log g_n}{n}>8+12\log2.
\tag{A278.23}
\]

本稿没有支付A278.23，也没有给反向全子列障碍。M是合法完整upper，A278.21证明这份安全输出增长；它不证明最小d_n增长太快。q求值的二处分母已在S/q和双镜像中取消；逐项LCM被实际Newton矩压为平方；粗阶乘也未保留。即使这些信用真实，仍不得用有限gcd或可能巨大content替代A278.23。

本278一轮到期裁决应是：完整安全费用与最小分母桥已付，严格净费用未闭合，未准入数值无理性结论；如无其它独审补足的完整负预算，不以此正upper另开同源费用轮。未来重开须提供同一完整对上足额全尺度共同内容，或另一个确实改变完整净预算的机制，并重新接受宏观机会成本比较。n=0不影响任何无界子列或率，若需要该单个有理数可直接由W9求取；未把n≥1的证明伪称包括n=0。

## 6. 独审及交叉审范围

`wilson_independent_278`实际全文读A278.1–23，独立重建伴随S的符号、Newton差商常数1/2、全部odd素数高幂、C的二处、外b⁻³及1/16、X的奇性、完整整数对和真实g的子列量词。其[独审稿](wilson_independent_round278.md)保存独立证明；没有领取任何尚未付清的g信用。作者未将自己的重建当独审。

本代理另实际全文读取[primitive稿](wilson_primitive_round278.md)的P1–P12及固定n=2表，仅作纸面核查，没有重跑诊断。P2差商负号、P3尾部的64系数、P4全r的二处整、P5包含prefix的完整gross桥、P6所有n的Casoratian、P6a归一常数、P7只在两赋值不等时的保留及P9–P12的q奇整性/二赋值均通过。其Q是本稿Q经变量替换及\((-1)^n16^n\)的规范，H与本稿R相应差一个\((-1)^{n+1}2\cdot16^{n-1}\)；两稿没有把这个gross规范当实际下界。固定n=2表与P3可直接整式核对，只确认符号及系数，不推广样本gcd。
