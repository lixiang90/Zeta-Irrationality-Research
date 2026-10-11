# Conifold规范化解的显式二进制分母界与奇素数接口

日期：2026-10-06。作者：root。本稿为本轮新建证明，不改写旧数学文件。

## D1. 输入、结论和目前的范围

本轮实际回读主进度§79–84、
[规范化局部解](cdt_odd_conifold_arithmetic_center_20261006.md)、
[端点敏感九维模型](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md)。
令 $t=1-x, D=d/dt, w=1-t$，使用已固定的有理算子

\[
P=t w^4D^4+w^3(2-8t)D^3+
 \frac{w^2(29t-15)}2D^2+w(4-5t)D-\frac w{16}.
\]

规范化解 $g_0,g_1,g_2,h\in\mathbb Q[[t]]$ 满足

\[
Pg_i=0,\quad Ph=\frac{\sqrt{1-t}}{16};\qquad
(c_0,c_1,c_2)=
(1,0,0),(0,1,0),(0,0,1),(0,0,0),
\]

其中最后一组三个初值属于 $h$。这是实际P及实际规范化，未换成仅有相同局部指数的方程。

**全尺度定理。** 对以上任一解 $f=\sum c_nt^n$，所有 $n\ge0$ 均有

\[
\boxed{2^{b(n)}c_n\in\mathbb Z_2,\qquad
b(n)=2n+2v_2(n!)-\lfloor n/2\rfloor.}
\tag{D1}
\]

尤其 $v_2(\operatorname{den}c_n)\le b(n)\le7n/2$，并且

\[
\lim_{n\to\infty}\frac{b(n)}n=\frac72.
\tag{D2}
\]

这比“存在未显式给出的坏素数常数”具体，且完全不以有限数据为证明。
它只处理素数2。下文另列奇素数通用半径条件，未完成的几何核验不作为本定理假设。
不由此宣称新的数值无理性、线性无关性或最优分母常数。

## D2. 平方为零的留数基底

对 $Pf=\beta\sqrt w/16$，定义

\[
y=(f,f',f''+tf''',t^2f''')^T,\qquad \delta=tD.
\]

设

\[
A_0=-\frac1{16w^3},\quad A_1=\frac{4-5t}{w^3},\quad
A_2=\frac{29t-15}{2w^2},\quad A_3=\frac{2-8t}{w},\quad
B=\frac{17t-3}{2w^2}=\frac6w+A_2.
\]

直接由P解出四阶导数，得到精确等式

\[
\delta y=G(t)y+
 \frac{\beta}{16w^{7/2}}(0,0,t,t^2)^T,
\quad
G(t)=\begin{pmatrix}
0&t&0&0\\
0&0&t&-1\\
-tA_0&-tA_1&-tA_2&B\\
-t^2A_0&-t^2A_1&-t^2A_2&tB
\end{pmatrix}.
\tag{D3}
\]

例如

\[
\delta(f''+tf''')=2tf'''+t^2f'''',\quad
2-A_3=6t/w,
\]

代入 $f''=y_2-y_3/t, f'''=y_3/t^2$，即得第三行；第四行同理。
这也检验了源项的幂次与符号。
留数 $G(0)$ 只有第四列非零，相关条目为 $-1,-3/2$，其平方为零。

为了把非齐次解一并纳入，另设 $u=w^{-7/2}$，

\[
\delta u=\frac{7t}{2w}u,\qquad
G_5=\begin{pmatrix}
G&(0,0,t/16,t^2/16)^T\\
0&7t/(2w)
\end{pmatrix}.
\tag{D4}
\]

齐次解取第五坐标0；非齐次解 $h$ 取第五坐标 $u$。

## D3. 一个对素数2可直接使用的整系数系统

作 $t=4z$，并令

\[
S=\operatorname{diag}(1,2,4,1,1),\quad
Z(z)=S(y(4z),\beta u(4z))^T,\quad v=1-4z.
\]

由于 $z\partial_z=t\partial_t$，新系统为

\[
zZ'=H(z)Z,\qquad H=SG_5(4z)S^{-1}=
\begin{pmatrix}
0&2z&0&0&0\\
0&0&2z&-2&0\\
z/v^3&-32z(1-5z)/v^3&-2z(116z-15)/v^2&2(68z-3)/v^2&z\\
z^2/v^3&-32z^2(1-5z)/v^3&-2z^2(116z-15)/v^2&2z(68z-3)/v^2&z^2\\
0&0&0&0&14z/v
\end{pmatrix}.
\tag{D5}
\]

所有Taylor矩阵 $H_j$ 都属于 $M_5(\mathbb Z_2)$：每个分母只是 $v^k$，分子均为整系数多项式。
留数 $R=H_0$ 的唯二非零条目为 $R_{1,3}=-2, R_{2,3}=-6$，下标从0开始。
因此

\[
R^2=0,\qquad R\in2M_5(\mathbb Z_2).
\tag{D6}
\]

四个规范化解的初值向量分别是

\[
(1,0,0,0,0), (0,2,0,0,0), (0,0,8,0,0), (0,0,0,0,1),
\]

均为整向量且在 $\ker R$。反之，$RZ_0=0$ 与三个任意标量Taylor初值及任意源项相对应。
特别是本基底既未丢弃实际的规范化解，也未引入其Taylor展开中的对数项。

## D4. 全尺度递推证明

写 $Z=\sum d_nz^n, H=R+\sum_{j\ge1}H_jz^j$。对 $n\ge1$，

\[
(nI-R)d_n=\sum_{j=1}^nH_jd_{n-j},\qquad
(nI-R)^{-1}=\frac In+\frac R{n^2}.
\tag{D7}
\]

令 $k=v_2(n)$。右侧逆矩阵的分母指数至多

\[
e(k)=\max\{k,2k-1\}=
\begin{cases}0&k=0,\\2k-1&k\ge1.\end{cases}
\tag{D8}
\]

这是 $2\mid R$ 带来的改进；无需使用任意素数的Frobenius存在性。
设

\[
E_n=\sum_{j=1}^ne(v_2(j))=2v_2(n!)-\lfloor n/2\rfloor.
\tag{D9}
\]

该数列非减。若 $2^{E_m}d_m$ 对所有 $m<n$ 整，则D7右侧乘 $2^{E_{n-1}}$ 整，
再由D8乘 $2^{e(v_2(n))}$ 后 $d_n$ 整。初值整，归纳得到所有 $n$ 的 $2^{E_n}d_n$ 整。
第一坐标是 $f(4z)=\sum4^nc_nz^n$，故得D1。

由 $v_2(n!)=n-s_2(n)$，其中 $s_2(n)$ 是二进制数字之和，

\[
b(n)=4n-2s_2(n)-\lfloor n/2\rfloor\le7n/2,
\]

且 $s_2(n)=O(\log(n+1))$，证明D2。
任意固定阶 $\theta_x=-(1-t)D_t$ 导数也可用 $b(n+j)$ 控制：
展开 $\theta_x^j$ 为整多项式系数的普通导数，Taylor系数只是固定范围内的整数倍移位系数。
这不需要把整Betti格自动视为整Taylor基底。

## D5. 乘积、积分及端点敏感模型中的费用

对非负整数 $a,b$，

\[
b(a)+b(b)-b(a+b)=
-2v_2\binom{a+b}a+
\lfloor(a+b)/2\rfloor-\lfloor a/2\rfloor-\lfloor b/2\rfloor
\le1.
\tag{D10}
\]

所以两个系数序列的卷积只多一个固定的二进制分母因子。
平方根倒数 $w^{-1/2}$ 的第 $k$ 项是 $4^{-k}\binom{2k}k$，其分母指数至多 $2k\le b(k)$。正平方根是 $w\,w^{-1/2}$，由乘整多项式得同一安全界。

沿用已固定模型的

\[
F_j(t)=-\frac1{16}\int_0^t\frac{g_j(u)}{\sqrt{1-u}}\,du,\quad j=1,2,
\]

则第 $m\ge1$ 项的分母指数至多

\[
b(m-1)+1+v_2(m)+4\le b(m)+3.
\tag{D11}
\]

最后一个不等式使用

\[
b(m)-b(m-1)=2+e(v_2(m))\ge2+v_2(m).
\]

因此 $F_1g_2-F_2g_1$ 的第 $n$ 项可用 $2^{b(n)+4}$ 清掉二进制分母。
取最多三阶的固定导数和另一项 $-2q\theta^jv$ 时，对 $q\in\mathbb Q$ 乘一个固定初始分母；
对 $q\in\overline{\mathbb Q}$ 则先固定其数域及整初始因子，再在每个2上方place使用同一有理因子。
混合坐标含两个最多三阶的导数及一个平方根。各项总索引移位至多6，
可统一保守使用 $2^{b(N+6)+O(1)}$ 清掉前 $N$ 项的二进制分母。

这给九维模型的二进制**主指数费用** $\tfrac72\log2$，固定移位不改变主指数。
若只接受整有理的变量缩放，$16^n$ 是方便的安全替代；
不能在不核算数域与全部places的情况下，免费改用 $2^{7/2}$ 缩放。
该改进本身也不产生新的可填奇点或新的数值反证。

## D6. 奇素数条件：已验证什么、还缺什么

原始四维G满足以下三个条件，对每个奇素数都已由D3直接验证：

1. 在 $|t|_p<1$ 无极点（可能极点只有1）；
2. $G(0)$ 幂零；
3. Gauss范数至多1（所有系数属于 \(\mathbb Z[1/2]\)）。

第四个条件是**通用点的基本解矩阵在半径1的开圆盘收敛**。
只凭前三条不能把第四条加入结论。

本轮实际阅读Fischler–Rivoal已归档正式版PDF第6–8页：其Theorem 3明确列出这四条条件，
并给出

\[
|U_n|_p\le T_p(n)^{\mu-1+v_p((\mu-1)!)+\beta_\mu},\quad
\beta_\mu=\min\left\{\mu-1,v_p\prod_{j=1}^\mu\binom\mu j\right\}.
\tag{D12}
\]

在本四维系统中，若相应奇素数满足第四条，则

\[
v_p(\operatorname{den}c_n)\le
\begin{cases}
3\lfloor\log_p n\rfloor&p\ge5,\\
5\lfloor\log_3 n\rfloor&p=3.
\end{cases}
\tag{D13}
\]

初值整且没有额外Laurent移位；取幂零Levelt矩阵 $U(t)t^{G(0)}$，
整初值在 \(\ker G(0)\) 中，故规范化齐次解正是 $U(t)c$。
此处在 $p=3$ 不能漏掉 $v_3(3!)=1$ 和 \(\beta_4=1\)。
单个素数3多出的 $3^{2\lfloor\log_3 n\rfloor}$ 是多项式费用，不是新的指数费。

**条件性全奇素数推论。** 若第四条对所有奇素数成立，令 $D_N^{\rm odd}$ 是
\(\operatorname{lcm}(1,\ldots,N)\) 的奇数部分，则对前三个齐次解

\[
2^{b(n)}(D_n^{\rm odd})^3
3^{2\lfloor\log_3 n\rfloor}c_n\in\mathbb Z.
\tag{D14}
\]

其中 $n=0$ 按1处理。积分F的奇素数费用相应变成LCM四次，
九维模型的纯收缩坐标是LCM七次，混合坐标是LCM六次；
素数3的额外有限幂次仍只有多项式增长。
本稿的D14保持条件性，直至固定toric紧化在所有奇素数的整光滑模型和相应GM收敛性均获得单独核验。

## D7. 数据、核验和文献阅读记录

作者新建
[有限递推实验](cdt_odd_R0_conifold_effective_denominator_20261006_probe.py) 与
[数据](cdt_odd_R0_conifold_effective_denominator_20261006_probe.json)，首次执行恰1次，计算到180阶。
该实验没有执行或import旧/peer数学producer。各序列在扣除LCM三次或四次后，
前缀额外奇分母均为1；这只是有限支持，不证明D14的条件。

另新建
[符号核验器](cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.py) 与
[结果](cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.json)，首次执行恰1次，
13项检查通过，包括D3–D6和精确逆矩阵身份，以及上述180阶数据对D1的符合性。
全尺度D1的依据是D4的归纳证明，而不是180阶核验。
本作者本轮新数学producer合计2次首次执行，旧/peer数学producer执行与import均为0。

一手阅读：

- Fischler–Rivoal，正式版PDF6–8实际全文读取，Theorem 3及其适用条件。
  [作者文稿](https://rivoal.perso.math.cnrs.fr/articles/dengfn.pdf)。
- Katz，*Travaux de Dwork*，本轮从作者网站新归档35页PDF；实际阅读PDF9–12的Proposition 3.1，
  其3.1.2把F晶体水平解提升到开单位多圆盘收敛。
  另实际全文读PDF23的第7节几何输入，并视觉核PDF10和23；其中明确要求proper smooth及de Rham局部自由，不能遗漏后一个前提。
  [作者存档](https://web.math.princeton.edu/~nmk/old/travdwork.pdf)。
  此来源不能免除本项目模型的好约化和GM实现核验。
- Dwork 1973广义超几何IV、Beukers–Vlasenko *Dwork Crystals I* 的归档metadata与命中页定位，
  以及Katz 1968 PDF1–3与关键词定位均已做；本稿不把这些定位声称为相关全部定理的实际阅读。

状态：D1–D11为本轮完整证明；D12为实际核读的一手定理；D13–D14为带明确第四条件的推论。
真实Betti格、de Rham比较、数值无理性和CDT可填域仍需分别处理。

冻结前修订记录：初稿有若干数学分隔符和quad命令排版错误；作者在quarter实际全文审阅指出后统一修复，并补明正平方根由乘整多项式取得同界。
D1–D11的矩阵、指数及归纳证明未因此改变；两个数学producer均未重跑。
下载Katz时curl先返回运行session，作者曾在下载未完成时尝试读取而失败；等待同一下载完成后实际读取35页完整文件，只有完成后的SHA被归档。
