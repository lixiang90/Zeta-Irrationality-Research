# 初等 cyclotomic Mellin 近似：纯目标余类、真实分母窗口与本原预算

日期：2026-10-04。另立新族，不修改冻结的 BB、K₂ 或旧算术报告，不作参数扫描。本族是经典 polylog Mellin 积分在本项目中的具体构造，不声称全球新颖。

**本轮实质结果。** 对 \(t^{an}(1-t)^{bn}/(1+t^2)\) 的纯目标子列，得到逐素数、全尺度的真实有理项分母下界，并允许完整 gcd 后证明：固定整数 \(a\ge4b>0\) 时，Catalan（k=2）与 ζ(7)（k=7）的这组本原整数线性形式均指数发散。对 parity 优化的 \(tR(t^2)\)、\(R=u^{an}(1-u)^{bn}\)，ζ(7) 的排除范围加强为 \(a\ge2b>0\)。

这不排除全部单核近似：平衡参数、signed Rodrigues、多项式线性组合、尺度依赖修正或更高极点仍在范围之外。后附统一 LCM 障碍是较弱结果，不能代替真实分母／本原结论。

## 1. Mellin 身份与符号、2 的幂

固定整数 \(k\ge2\)，定义
\[
J_k(P)=\frac1{(k-1)!}\int_0^1
\frac{(-\log t)^{k-1}P(t)}{1+t^2}\,dt. \tag{1}
\]
由
\[
\frac1{(k-1)!}\int_0^1(-\log t)^{k-1}t^m\,dt
=\frac1{(m+1)^k}
\]
和绝对可积的几何级数，
\[
J_k(1)=\beta(k),\qquad J_k(t)=2^{-k}\eta(k)
=\frac{2^{k-1}-1}{2^{2k-1}}\zeta(k). \tag{2}
\]
其中 \(\eta(k)=(1-2^{1-k})\zeta(k)\)。第二项是正号；k=7 的系数恰为 \(63/8192\)。这与 [NIST DLMF 25.12.11 的 polylog Mellin 表达](https://dlmf.nist.gov/25.12.E11) 一致，但本稿的身份已由上述实积分直接推导。

对 \(P\in\mathbf Z[t]\)，以首一多项式 \(1+t^2\) 作整数除法：
\[
P=(1+t^2)Q+A+Bt,\qquad Q=\sum_mq_mt^m\in\mathbf Z[t],\quad A,B\in\mathbf Z.
\]
于是
\[
\boxed{J_k(P)=A\beta(k)+Bc_k\zeta(k)+R_k(Q),\quad
c_k=\frac{2^{k-1}-1}{2^{2k-1}},\quad R_k(Q)=\sum_m\frac{q_m}{(m+1)^k}.} \tag{3}
\]
若 \(\deg P=D\ge2\)，则 \(\deg Q\le D-2\)，故
\[
\operatorname{den}R_k(Q)\mid L_{D-1}^{\,k},\qquad
L_N=\operatorname{lcm}(1,\ldots,N),\quad L_0=1. \tag{4}
\]
ζ 系数额外只需固定 \(2^{2k-1}\)，不影响随 D 的指数。

## 2. 二项族的全部纯目标余类

以下 a、b 都是固定正整数，n 为正整数，记
\[
P_n=t^{an}(1-t)^{bn},\quad D=(a+b)n,\quad d=2a-b.
\]
把 t=i 代入整数除法得
\[
\boxed{A_n+iB_n=i^{an}(1-i)^{bn}
=2^{bn/2}\exp\!\left(\frac{\pi i\,dn}{4}\right).} \tag{5}
\]
因此
\[
\begin{array}{ll}
\text{纯 }\beta(k): &dn\equiv0\pmod4,\quad
B_n=0,\ A_n=(-1)^{dn/4}2^{bn/2},\\
\text{纯 }\zeta(k): &dn\equiv2\pmod4,\quad
A_n=0,\ B_n=(-1)^{(dn-2)/4}2^{bn/2}.
\end{array} \tag{6}
\]
两种情形都自动有 bn 偶数。完整 n 余类为：

| d mod 4 | 纯 β | 纯 ζ |
|---|---|---|
| 0 | 全部 n | 不存在 |
| 1 或 3 | n≡0 mod4 | n≡2 mod4 |
| 2 | n 偶 | n 奇 |

dn 为奇数时 A、B 均非零、绝对值 \(2^{(bn-1)/2}\)，是两周期混合。特别，a=b=1 给 n≡0 mod4 的纯 Catalan（k=2）和 n≡2 mod4 的纯 ζ(7)（k=7）。相位为 0、2、4、6 mod8 时目标系数的符号依次为 +A、+B、−A、−B，不能全写成同一正系数。

## 3. 实余项的全尺度上界与精确指数

令
\[
t_*=\frac a{a+b},\quad \rho=\frac{a^ab^b}{(a+b)^{a+b}},\quad
E(a,b)=-\log\rho=(a+b)\log(a+b)-a\log a-b\log b.
\]
因为 \(0<P_n(t)\le\rho^n\) 在 (0,1) 成立，
\[
0<J_k(P_n)\le\beta(k)\rho^n. \tag{7}
\]
在 t_* 的任意小闭区间，Mellin 权重连续且严格为正。用该区间给下界，再缩小区间，得到
\[
\lim_{n\to\infty}\frac1n\log J_k(P_n)=-E(a,b). \tag{8}
\]
非退化 Laplace 法也给
\[
J_k(P_n)\sim
\frac{(-\log t_*)^{k-1}}{(k-1)!(1+t_*^2)}
\sqrt{\frac{2\pi ab}{(a+b)^3n}}\ \rho^n.
\]
后面的分母结论只需 (8)，不依赖浮点拟合。

## 4. 完整 gcd 引理：约掉全部 content 后仍可控制

**引理。** 设 \(R=r/M\) 已约分，M>0，\(\gcd(M,r)=1\)。设目标系数为 \(BC/D_0\)，其中 B、C 是非零整数，D₀ 是正整数。由
\[
J=(BC/D_0)X+r/M
\]
得到整数对
\[
(q,p)=(MBC,-D_0r),\qquad qX-p=MD_0J.
\]
记 \(h=\gcd(|q|,|p|)\)，则
\[
\boxed{h\mid D_0|BC|,\qquad
|\ell|:=\frac{|qX-p|}{h}\ge\frac{M|J|}{|BC|}.} \tag{9}
\]
**证明。** 对每个素数 l，约分条件给
\(\min(v_l(M),v_l(r))=0\)。因此
\[
v_l(h)=\min(v_l(M)+v_l(BC),v_l(D_0)+v_l(r))
\le v_l(BC)+v_l(D_0).
\]
这证明整除，而不是忽略 M 因子。代入 \(MD_0J/h\) 得 (9)。□

纯 β 时取 \(B=A_n,C=D_0=1\)。纯 ζ 时取
\[
B=B_n,\quad C=2^{k-1}-1,\quad D_0=2^{2k-1}.
\]
特别，k=7 的整数对为
\[
(q,p)=(63MB_n,-8192r),\qquad
h\le8192\cdot63|B_n|. \tag{10}
\]
故两类都有
\[
\log h\le\frac{bn}{2}\log2+O_k(1). \tag{11}
\]
本引理使用真实最小有理项分母 M，已允许全部小素数抵消和完整 gcd；没有假定统一 LCM 的 content 较小。对同一个形式再作整数倍放大，不能比其本原形式更小。

## 5. 真实分母的逐素数窗口定理

写 \(Q_n=\sum q_mt^m\)，\(R_n=R_k(Q_n)\)。因为 \(P_n\) 在次数 an 以下没有系数，除法的低次递推给
\[
q_{2j}=(-1)^{j+1}A_n,\qquad
q_{2j+1}=(-1)^{j+1}B_n,\qquad m<an. \tag{12}
\]
令固定正整数 h 满足 hb<a，取素数
\[
\frac{D}{h+1}<p<\frac{an}{h}. \tag{13}
\]
这些窗口随 n 线性移动。n 充分大时 p 为奇素数、p>h、p²>D，且
\[
\left\lfloor\frac{D-1}{p}\right\rfloor=h,\qquad hp<an.
\]
R_n 中全部分母含 p 的项恰为 \(m+1=lp\)，1≤l≤h；它们都处于 (12) 的低区。乘 pᵏ 后在 p 的局部环取剩余类，其他项消失：
\[
p^kR_n\equiv\sum_{l=1}^h q_{lp-1}l^{-k}\pmod p.
\]

**纯 β 子列。** 由 (12)
\[
p^kR_n\equiv(-1)^{(p+1)/2}A_n
\sum_{\substack{1\le l\le h\\l\ {\rm odd}}}
\frac{(-1)^{(l-1)/2}}{l^k}\pmod p. \tag{14}
\]
固定交错奇分母部分和严格为正：它是递减正项交错级数的部分和。有理分子非零，除有限个依赖 k、h 的素数外，它为 p-unit。A_n 是 2 的幂乘符号，亦为 p-unit。窗口下端趋于无穷，有限例外最终全不在窗口内。因此对 (13) 的每个充分大素数，
\[
\boxed{v_p(R_n)=-k.} \tag{15}
\]

**纯 ζ 子列。** 同样有
\[
p^kR_n\equiv B_n\sum_{\substack{2\le l\le h\\l\ {\rm even}}}
\frac{(-1)^{l/2}}{l^k}
=-2^{-k}B_n\sum_{j=1}^{\lfloor h/2\rfloor}
\frac{(-1)^{j-1}}{j^k}\pmod p. \tag{16}
\]
固定部分和在 h≥2 时非零，所以 (15) 对这些 h 成立。h=1 时 (16) 为零，不能宣称该窗口强制 \(p^k\)。这是两目标成本的区别。

本证明不要求 p∤n，也不是固定几个 n 的试算。每个素数层的精确赋值都由同一低次递推和非零部分和证明。

令
\[
H=\left\lceil a/b\right\rceil-1,\quad
S_\beta(a,b)=\sum_{h=1}^{H}\left(\frac ah-\frac{a+b}{h+1}\right),
\]
\[
S_\zeta(a,b)=\sum_{h=2}^{H}\left(\frac ah-\frac{a+b}{h+1}\right), \tag{17}
\]
空和为 0。不同 h 的窗口互不相交：其上端 an/h 小于前一窗口的下端 D/h。由素数定理，若 \(M_n=\operatorname{den}R_n\)，沿相应纯子列
\[
\boxed{
\liminf\frac{\log M_n}{n}\ge kS_\beta(a,b)
\quad\text{或}\quad
\liminf\frac{\log M_n}{n}\ge kS_\zeta(a,b).} \tag{18}
\]
这是下界，不声称 M_n 的精确指数。

## 6. 原单核族的真实本原排除区间

合并 (8)、(9)、(18)：
\[
\liminf_{n\to\infty}\frac{\log|\ell_n|}{n}
\ge\Phi_\star(a,b,k),
\]
\[
\boxed{\Phi_\star=kS_\star(a,b)-E(a,b)-\frac b2\log2,\qquad
\star\in\{\beta,\zeta\}.} \tag{19}
\]
若右端正，则 \(|\ell_n|\to\infty\)，完整约去 content 也不能得到趋零整数形式。

可无扫描地给出宽参数区间。置 x=a/b，\(\mathcal H_m=\sum_{j=1}^m1/j\)。在 H=ceil(x)−1 固定的区间上
\[
S_\beta/b=x\frac H{H+1}-(\mathcal H_{H+1}-1).
\]
当 x>1，\(S_\zeta=S_\beta-(a-b)/2\)，包括只有 h=1 时右端为 0。这些分段线性函数在整数 x 处连续。x≥4 时 \(H/(H+1)\ge3/4\)，而
\[
\frac d{dx}(E/b)=\log(1+1/x)<1/4.
\]
故
\[
\frac d{dx}(\Phi_\beta/b)>0\quad(k\ge2),\qquad
\frac d{dx}(\Phi_\zeta/b)>0\quad(k\ge7).
\]
在 x=4，
\(S_\beta/b=23/12,\ S_\zeta/b=5/12\)，最小 k 的预算为
\[
\Phi_\beta(4b,b,2)/b
=\frac{23}6-5\log5+\frac{15}2\log2>0,
\]
\[
\Phi_\zeta(4b,b,7)/b
=\frac{35}{12}-5\log5+\frac{15}2\log2>0. \tag{20}
\]
精确有理界 \(\log2>693/1000\)、\(\log5<161/100\) 分别给严格下界 \(1177/1200\)、\(77/1200\)。界由 atanh 正项级数和显式几何尾界认证，不靠浮点符号判断。因此
\[
\boxed{a\ge4b>0:
\ \text{纯 Catalan 的 k=2 子列与纯 }\zeta(7)\text{ 的 k=7 子列，
全部本原形式指数发散。}} \tag{21}
\]
本来不存在纯 ζ 子列的参数，对应条件为空。更一般的正预算参数也由 (19) 覆盖；没有证明 (21) 是最佳边界。

平衡 a=b 时 H=0，(18) 没有给增长下界。不能由“统一 LCM 太大”或“这些窗口不存在”推出平衡族实际本原形式失败。也不能交换 a、b：Mellin 权重及极点位置不被 t↦1−t 固定。

## 7. parity 优化的纯 ζ 族：正确度数与真实窗口

另取
\[
P(t)=tR(t^2),\qquad
I_k^+(R)=\frac1{(k-1)!}\int_0^1
\frac{(-\log u)^{k-1}R(u)}{1+u}\,du.
\]
u=t² 给
\[
\boxed{J_k(tR(t^2))=2^{-k}I_k^+(R).} \tag{22}
\]
若 \(R=(1+u)S+B\)，则
\[
I_k^+(R)=B\eta(k)+\sum_j\frac{s_j}{(j+1)^k}. \tag{23}
\]
若 \(\deg R=d\)，\(\deg S=d-1\)，标准分母是 \(L_d^k\)，不是原 P 次数 \(2d+1\) 对应的 LCM。k=7 令 \(r/M=\sum_js_j/(j+1)^7\) 已约分，整数对为
\[
(q,p)=(63MB,-64r).
\]
它表示 \(64M I_7^+(R)=8192M J_7(P)\)，两种变量的固定倍数一致。

取 \(R_n=u^{an}(1-u)^{bn}\)，\(d=(a+b)n\)，有
\[
B_n=R_n(-1)=(-1)^{an}2^{bn},\qquad
s_j=(-1)^{j+1}B_n\quad(j<an).
\]
每个 n 都是纯 ζ 方向，不需相位筛选。对同一窗口
\(d/(h+1)<p<an/h,\ hb<a\)，有
\[
p^kR_n^{\rm rat}\equiv
B_n\sum_{l=1}^h\frac{(-1)^l}{l^k}\pmod p. \tag{24}
\]
eta 部分和对每个 h≥1 都非零；于是分母下界使用全部 \(S_\beta\) 窗口。完整 gcd 引理给
\(\log h_n\le bn\log2+O_k(1)\)，故
\[
\boxed{\liminf\frac{\log|\ell_n|}{n}
\ge kS_\beta(a,b)-E(a,b)-b\log2.} \tag{25}
\]
k=7、x=a/b≥2 时分段导数至少
\(7/2-\log(3/2)>0\)。在 x=2，
\[
7S_\beta/b-E/b-\log2
=\frac72-3\log3+\log2>0.
\]
\(\log3<1099/1000,\ \log2>693/1000\) 给严格下界 \(112/125\)。因此
\[
\boxed{a\ge2b>0:
\ P_n=t^{2an+1}(1-t^2)^{bn}
\text{ 的纯 }\zeta(7)\text{ 本原形式全部指数发散。}} \tag{26}
\]
(26) 使用正确的 u 次数及真实分母，已计入目标系数 \(2^{bn}\) 所能带来的全部 gcd 上界；不是原度数 LCM 的假性障碍。signed Rodrigues 与原子列的线性组合不在本证明范围。

## 8. 附：宽非负整数多项式的统一账本障碍

本节不用 §5 的真实分母，只说明统一 LCM 成本。

设非零 \(P\in\mathbf Z[t]\) 在 [0,1] 非负，实际次数 D≥1，首项系数 \(a_D\ne0\)。令 \(\mathcal L_D(t)=P_D(2t-1)\) 为 shifted Legendre polynomial。在 [0,1] 有 \(|\mathcal L_D|\le1\)，首项系数 \(\binom{2D}D\)，且与低次多项式正交。Rodrigues 身份
\[
\mathcal L_D(t)=\frac1{D!}\frac{d^D}{dt^D}[t^D(t-1)^D]
\]
经 D 次分部积分给
\[
\int_0^1t^D\mathcal L_D(t)\,dt
=\frac1{(2D+1)\binom{2D}D}.
\]
故
\[
\int_0^1P(t)\,dt
\ge\left|\int_0^1P(t)\mathcal L_D(t)\,dt\right|
=\frac{|a_D|}{(2D+1)\binom{2D}D}
\ge\frac1{(2D+1)4^D}. \tag{27}
\]
为处理 t=1 的 Mellin 权重零，固定 0<c<1，重标度得到
\[
\int_0^cP(t)\,dt\ge
\frac{c^{D+1}}{(2D+1)\binom{2D}D}.
\]
此区间的权重至少
\(m_{k,c}=(-\log c)^{k-1}/[2(k-1)!]>0\)，于是
\[
J_k(P)\ge\frac{m_{k,c}c^{D+1}}{(2D+1)4^D}.
\]
令 c↑1，任意这样的次数递增序列都有
\[
\liminf_{D\to\infty}\frac{\log J_k(P_D)}D\ge-\log4. \tag{28}
\]
由 \(\log L_D=D+o(D)\)，标准统一乘子满足
\[
\liminf\frac{\log(L_{D-1}^kJ_k(P_D))}D
\ge k-\log4>0\quad(k\ge2). \tag{29}
\]
同一证明适用 (22) 的正核 1/(1+u)，使用 R 的次数 d。

(4) 的统一有理项分母在整个整数多项式空间上不能降低：取
\(P=1+(1+t^2)t^m\)，其纯 β 系数为 1、有理项 \(1/(m+1)^k\)；0≤m≤D−2 穷尽 \(L_{D-1}^k\) 的所有层。这是空间统一乘子的最优性，不是二项子族实际分母的最优性。

若完整 content 为 h_D，本原值为统一形式除以 h_D，则想让其趋零，至少必须
\[
\liminf\frac{\log h_D}D\ge k-\log4.
\]
固定群因子或多项式级 content 不够，指数 content 仍可能救济。本节不排除它；§6–7 才在指定区间把完整 gcd 纳入后排除。

## 9. 剩余输入、证书及审核范围

余下直接算术问题是平衡与小 a/b 区域的实际 \(M_n\) 及 numerator 的 2-adic content；低区窗口不自动穷尽它们。signed moments／Rodrigues、多个尺度组合或新核需重新证明正性、目标纯度与真实清分母，不能继承 (21)/(26) 为排除。

[精确脚本](E:/kimi-build/zeta5/research/odd_zeta_cyclotomic_mellin_20261004_verify.py) 和 [JSON](E:/kimi-build/zeta5/research/odd_zeta_cyclotomic_mellin_20261004_verify.json) 已运行通过。只检查四个预先指定原族例和一个 parity 例的整数除法、相位、固定 prime windows、整数对与 gcd 界、变量归一化、对数级数严格有理界，以及一次固定 Legendre/Rodrigues 常数证书。没有参数扫描。

全尺度结果由 §§4–8 的书面证明承担；有限例不替代它们。几何分支已只读复审 §§4–6 的完整 gcd、所有素数窗口与分段预算，distribution 分支另复审 §§4–8，核对 parity 的全部 2 的幂、正确次数、eta 部分和、有限坏素数及非负整数 Legendre 下界，均通过。引理的 B、C 非零范围已显式补齐，无其他必要纠错。本稿与证书在两轮审阅后冻结。
