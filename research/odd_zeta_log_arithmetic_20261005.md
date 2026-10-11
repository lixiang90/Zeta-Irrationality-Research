# 对数矩候选的真实高度、素数块与本原化预算

日期：2026-10-05。只研究冻结的[候选](odd_zeta_log_moment_candidate_20261004.md)中
\(q=k=7\) 的族，不改该稿。以下是有限公式的全尺度算术分析，未证明 ζ(7) 无理。
目标系数的真实指数已经闭合；有理部分的实际分母指数和完整 content 的指数仍未闭合。

## 1. 整数系数与有理部分的正尾和

记 \(N=7n\)，
\[
a_r=\binom Nr\binom{n+r}{n}^{7},\quad
R(u)=\sum_{r=0}^N(-1)^r a_r u^r,
\quad B=R(-1)=\sum_{r=0}^N a_r>0.
\]
这些是整数，且 \(a_0=1\)。除法 \(R=(1+u)Q+B\) 给出的系数有更具体的形式：
\[
T_j=\sum_{r=j}^N a_r,\qquad
Q(u)=\sum_{j=1}^N(-1)^jT_j u^{j-1}.
\tag{1}
\]
比较最高项并向下递推即可证明，常数项也由 \(1-B=-T_1\) 检查。
因此
\[
I=I_7(R)=\frac{63B}{64}\zeta(7)+S,
\quad S=\sum_{j=1}^N\frac{(-1)^jT_j}{j^7}
=-\sum_{r=1}^N a_r A_r,
\quad A_r=\sum_{j=1}^r\frac{(-1)^{j-1}}{j^7}.
\tag{2}
\]
每个 \(A_r>0\)：偶数项成对为正，奇数项再增加一个正项。
故 **\(S<0\) 对所有 \(n\ge1\) 成立**，其约分 \(S=s/M\) 始终有
\(s<0,M>0,\gcd(s,M)=1\)。这不是特殊周期 \(I\) 的非零性证明。
整数值二项式多项式保证全部 \(a_r,T_j\) 整；直接得到
\[
M\mid L_{7n}^{7},\qquad
\limsup_{n\to\infty}\frac{\log M}{n}\le49.
\tag{3}
\]
后一式使用 \(\log L_x=x+o(x)\)。这里只是实际分母的上界。

## 2. \(B\) 的真实全尺度指数和主项

更一般固定正整数 \(q\)，设 \(N=qn\) 并将上式的七次幂换为 \(q\) 次幂。
令
\[
\Phi_q(t)=q\log q-t\log t-(q-t)\log(q-t)
+q\big((1+t)\log(1+t)-t\log t\big),\quad0\le t\le q,
\tag{4}
\]
端点按 \(0\log0=0\) 连续延拓。内部导数为
\[
\Phi'_q(t)=\log\frac{q-t}{t}+q\log\frac{1+t}{t},\qquad
\Phi''_q(t)=-\frac1{q-t}-\frac{q+1}{t}+\frac q{1+t}<0.
\]
导数在两端趋向 \(+\infty,-\infty\)。所以唯一最大点 \(t_q\in(0,q)\) 满足
\[
(q-t_q)(1+t_q)^q=t_q^{q+1}.
\tag{5}
\]
记 \(D_q=-\Phi''_q(t_q)>0\)，\(\beta_q=\Phi_q(t_q)\)。则
\[
\boxed{B_{n,q}\sim C_q n^{-q/2}e^{\beta_qn}},\qquad
C_q=(2\pi)^{-q/2}
\frac{\sqrt{q/[t_q(q-t_q)]}\,[(1+t_q)/t_q]^{q/2}}{\sqrt{D_q}}.
\tag{6}
\]
尤其 \(\log B_{n,q}/n\to\beta_q\)。

**证明。** 对 \(r/n\) 位于任一内部紧区间，Stirling 公式一致给
\[
a_r=(2\pi n)^{-(q+1)/2}
\sqrt{\frac q{t(q-t)}}\left(\frac{1+t}{t}\right)^{q/2}
e^{n\Phi_q(t)}(1+O(n^{-1})),\quad t=r/n.
\]
二项式的熵上界在全部 \(0\le r\le qn\) 给 \(a_r\le e^{n\Phi_q(r/n)}\)。
严格最大性使离开 \(t_q\) 任意固定邻域的总和为
\(O(n e^{(\beta_q-\epsilon)n})\)。在该邻域按
\(r=nt_q+x\sqrt n\) 作离散 Laplace 求和，二次项
\(-D_qx^2/2\) 给高斯因子 \(\sqrt{2\pi n/D_q}\)，得到 (6)。
这也说明次幂 \(n^{-q/2}\) 不能误写为单个二项式的 \(n^{-1/2}\)。

利用 (5) 可化简为
\[
\beta_q=q\log\frac{q(1+t_q)}{q-t_q}.
\tag{7}
\]
本目标 \(q=7\) 有
\[
t_7=5.373138032297703\ldots,\qquad
\boxed{\beta_7=23.179443965796084\ldots}.
\tag{8}
\]
这些小数是公式的数值说明；精确常数由 (5)、(7) 定义。
证书用有理端点 \(5373/1000<t_7<5374/1000\) 的多项式符号隔离根。
本节证明真实整数系数的指数，未借助有限系数增长拟合。

## 3. 全尺度 Lucas 块和分母最高层

设 \(p>7\) 为素数，满足
\(n<p\le7n\) 与 \(p^2>7n\)，写
\[
7n=Hp+d,\quad 1\le H\le6,\quad0\le d<p,
\quad e=\min(d,p-n-1),
\]
并定义实际整数
\[
C_{n,p}=\sum_{s=0}^{e}\binom ds\binom{n+s}{n}^{7}.
\tag{9}
\]
对 \(r=lp+s\)，Lucas 定理给
\[
a_{lp+s}\equiv
\binom Hl\binom ds\binom{n+s}{n}^{7}\pmod p
\]
当 \(s\le e\) 成立；其他 \(s\) 的值为零。
若 \(s>d\)，第一个二项式的低位已为零；若 \(n+s\ge p\)，
第二个二项式的低位上标小于 \(n\)，也为零。
由整块求和得到
\[
\boxed{B\equiv2^H C_{n,p}\pmod p},\qquad
\boxed{T_{lp}\equiv C_{n,p}\sum_{v=l}^H\binom Hv\pmod p}.
\tag{10}
\]

因 \(p^2>N\)，\(v_p(S)\ge-7\)，而 \(p^7S\in\mathbb Z_{(p)}\) 可模 \(p\) 约化。
只有 \(j=lp\) 的项留下，且奇 \(p\) 保持 \((-1)^{lp}=(-1)^l\)。所以
\[
\boxed{p^7S\equiv C_{n,p}\kappa_H\pmod p},\qquad
\kappa_H=\sum_{l=1}^H\frac{(-1)^l}{l^7}\sum_{v=l}^H\binom Hv
=-\sum_{v=1}^H\binom Hv A_v<0.
\tag{11}
\]
各 \(\kappa_H\) 为固定非零有理数：

| \(H\) | \(\kappa_H\) |
|---:|---:|
|1|\(-1\)|
|2|\(-383/128\)|
|3|\(-487733/69984\)|
|4|\(-534477557/35831808\)|
|5|\(-43115515337779/1399680000000\)|
|6|\(-87581665958203/1399680000000\)|

删去这些分子、分母的固定素因子集合 \(\mathcal F\)。则有**精确等价**
\[
C_{n,p}\not\equiv0\pmod p
\quad\Longleftrightarrow\quad v_p(M)=7,
\quad\Longleftrightarrow\quad p\nmid B.
\tag{12}
\]
这是关于当前指定范围素数的全尺度定理。
若 \(C_{n,p}=0\pmod p\)，只能先得 \(v_p(M)\le6\)，高层还需继续求和。
不能把 \(C\) 从 (11) 中约掉，尤其不能在 \(p\mid B\) 时把
\(p^7S/B\) 的模 \(p\) 值写成 \(\kappa_H/2^H\)。

## 4. 共同局部因子确会在无限尺度消失

有一个解析得出的无限反射族，说明 (12) 的单位前提不是形式细节。
若 \(n\) 奇、\(p>n\) 为奇素数且 \(p\mid8n+1\)，写
\(8n+1=jp\)，并假定 \(p\le7n\)。则
\[
H=j-1,\qquad d=p-n-1.
\]
此 \(d\) 为奇数，且 (9) 的上限就是 \(d\)。对于 \(0\le s\le d\)，
\[
\binom{n+s}{n}=\binom{n+s}{s}
\equiv(-1)^s\binom{p-n-1}{s}=(-1)^s\binom ds\pmod p.
\]
因此
\[
C_{n,p}\equiv\sum_{s=0}^{d}(-1)^s\binom ds^{8}=0\pmod p.
\tag{13}
\]
最后一个和作为整数已经为零，因为 \(s\leftrightarrow d-s\) 的两项相消。
例如每个素数 \(p\equiv3\pmod{16}\)、\(p\ge19\)，取
\[
n=(3p-1)/8
\tag{14}
\]
就有奇 \(n\)、\(n<p<7n\)、\(p^2>7n\)、\(H=2\)，故
\(p\mid B\) 且 \(v_p(M)\le6\)。Dirichlet 定理保证这种素数任意大；
可参见 [MIT 作者课程讲义 Theorem 18.1](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_full_lec.pdf)。

指定例 \((n,p)=(7,19)\) 精确有
\[
v_{19}(B)=2,\quad v_{19}(M)=5,\quad v_{19}(s)=0.
\tag{15}
\]
这个例子的 \(S/B\) 分母仍含 \(19^7\)：目标系数与有理部分共同变化，
不能从 \(M\) 少了两层推断完整本原值少了同样两层。
同样，(14) 每个尺度只指定一个素数，其对数重量为 \(O(\log n)\)；
它**不否定** \(\log M/n\) 可能具有最大指数，也不证明例外素数有正比例重量。

## 5. 完整 content 的精确逐素数公式

明确整数对为
\[
(63MB,64s),\qquad h=\gcd(63MB,64s),\qquad
\mathscr P_n=\frac{64M}{h}I.
\tag{16}
\]
两系数除以 \(h\) 才是本原线性型。对每个素数 \(p\)，完整公式是
\[
v_p(h)=\min\{v_p(M)+v_p(B)+v_p(63),\ v_p(s)+v_p(64)\}.
\tag{17}
\]
尤其对奇 \(p\)，由 \(\gcd(M,s)=1\) 得
\[
v_p(h)=\min\{v_p(63B),v_p(s)\},
\quad h_{\rm odd}=\gcd(63B,s)_{\rm odd}.
\tag{18}
\]
若奇 \(p\mid M\)，则 \(p\nmid s\)，**\(p\nmid h\)**。
故 (12) 的每个单位素数的七层真实分母，在完整本原化中全部保留。
对 \(p=2\) 使用 (17)，不得直接沿用奇素数简化：若 \(M\) 偶，
其指数为 \(\min\{v_2(M)+v_2(B),6\}\)；若 \(M\) 奇，
则为 \(\min\{v_2(B),6+v_2(s)\}\)。
从而有正确的统一上界
\[
h\le64\gcd(63B,s)\le64\cdot63B,
\qquad |\mathscr P_n|\ge\frac{M}{63B}|I|.
\tag{19}
\]
其证明保留了 \(M\) 可能与 \(B\) 有共同素因子的情形，
并没有错误地从 \(\gcd(M,s)=1\) 推 \(\gcd(MB,64s)\le B\)。

## 6. 可使用的全尺度预算与尚缺输入

对于足够大 \(n\)，\(p>n\) 自动有 \(p^2>7n\)。令
\[
E_n=\sum_{\substack{n<p\le7n,\ p\notin\mathcal F\\C_{n,p}\equiv0\ (p)}}\log p,
\quad\vartheta(x)=\sum_{p\le x}\log p.
\]
(12)、(18) 给出无条件、但含实际例外集合的有限下界
\[
M\ge\prod_{\substack{n<p\le7n,\ p\notin\mathcal F\\C_{n,p}\ne0\ (p)}}p^7,
\qquad
\log\frac{64M}{h}\ge
7\big(\vartheta(7n)-\vartheta(n)-E_n\big)-\log B-O(1).
\tag{20}
\]
因此若 \(I\) 最终非零，且
\(\ell=\liminf\log|I|/n\)、\(e=\limsup E_n/n\) 为有限实数，则
\[
\boxed{\liminf\frac{\log|\mathscr P_n|}{n}
\ge\ell+42-\beta_7-7e.}
\tag{21}
\]
当右侧严格为正时，本原值指数发散，是本具体族的失败判据；
当它非正时此下界不作成功判断。这里 \(42\) 只计 \((n,7n]\) 的素数窗口，
不等于统一上界的 \(49\)。例如 \(e=0\) 时已认证算术下界为
\(42-\beta_7=18.8205560342\ldots\)，但 **\(e=0\) 尚未证明**。

更精确的实际预算恒等式为
\[
\frac{\log|\mathscr P_n|}{n}
=\frac{\log|I|}{n}+\frac{\log M}{n}-\frac{\log h}{n}+o(1).
\tag{22}
\]
本稿没有以有限 \(\gcd\) 值猜测 \(\log h=o(n)\)，也没有声称
\(\log M/n\to49\)。仍需证明的独立算术输入是：

1. 对 (9) 的单位/非单位素数集合给加权全尺度估计，或者直接控制 \(M\)；
2. 控制 (18) 的共同因子指数，而非仅多项式系数的 gcd；
3. 将根任务的实际余项与非零性结论代入 (22) 的同一归一化。

反射族给出一项确切的局部消失机制；其余非单位分布仍是具体困难。
该困难不能由“二项式是整数值多项式”这一事实本身排除。

## 7. 精确证书与审计范围

[脚本](odd_zeta_log_arithmetic_20261005_verify.py)及
[JSON](odd_zeta_log_arithmetic_20261005_verify.json)只核固定代表：
整数尾和、约分有理部分、全部 content、六个固定 \(\kappa_H\)、
根的有理隔离、Lucas 块公式、\((7,19)\) 的反射和实际估值。
没有参数扫描、没有用数值周期决定零性；全尺度定理来自本稿的
Stirling/Laplace、Lucas、反射配对及逐素数 gcd 证明。
旧候选的全部文件保持冻结。
