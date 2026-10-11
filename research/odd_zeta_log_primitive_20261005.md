# 对数矩族的本原根分母：第二素数阶梯与真实缺层预算

日期：2026-10-05。承接已冻结的[算术稿](odd_zeta_log_arithmetic_20261005.md)，
本稿另行保存，不修改前稿。研究仍限
\(R_{n,7}(u)=\sum_{r=0}^{7n}(-1)^r\binom{7n}{r}\binom{n+r}{n}^{7}u^r\)。
本轮证明完整本原候选根的局部付费层和第二 \(p\)-adic 块展开。
它恢复了一部分非单位情形的全部七层分母，但未证明所有素数都恢复，
也未证明剩余高阶零域的加权密度。另证明不依赖任何素数例外或 content
假设的三相邻真实根分母高度下界。无参数扫描或新的无理性结论。

## 1. 直接把完整 gcd 吸收入候选有理根

沿用 \(N=7n\)、\(a_r=\binom Nr\binom{n+r}{n}^{7}\)、
\(B=\sum a_r>0\)、\(T_j=\sum_{r=j}^N a_r\)，以及
\[
I=\frac{63B}{64}\zeta(7)+S,
\qquad S=\sum_{j=1}^N\frac{(-1)^jT_j}{j^7}=s/M<0,
\quad \gcd(s,M)=1.
\]
定义候选根及其**实际约分分母**
\[
\alpha=-\frac{64S}{63B},\qquad
q_n=\operatorname{den}(\alpha)=\frac{63MB}{h},
\quad h=\gcd(63MB,64s).
\tag{1}
\]
因此 \(q_n\) 恰是本原整数线性型的 ζ 系数，不是统一 LCM 的替代名称。
本原值准确为
\[
\mathscr P_n=q_n(\zeta(7)-\alpha)
=\frac{64q_n}{63B}I=\frac{64M}{h}I.
\tag{2}
\]

以下取素数 \(p>7\)、\(n<p\le7n\)。此时
\(N<7p<p^2\)，写 \(N=Hp+d\)，\(1\le H\le6\)、\(0\le d<p\)。
令
\[
Z=p^7S\in\mathbb Z_{(p)},\qquad r=v_p(B),\quad t=v_p(Z).
\]
由于 \(S<0\)，\(t\) 有限；\(r,t\ge0\)。直接由 (1) 得全尺度精确式
\[
\boxed{v_p(q_n)=\max\{0,7+r-t\}.}
\tag{3}
\]
它包含完整 gcd：若 \(t<7\)，则 \(v_p(M)=7-t\)，约分的 \(s\) 为单位，
\(p\nmid h\)，故付费 \(7-t+r\) 层；若 \(t\ge7\)，则 \(p\nmid M\)，
\(v_p(h)=\min(r,t-7)\)，付费 \(\max(0,7+r-t)\) 层。
特别地，若 \(r\ge1,t=1\)，虽然 \(S\) 的分母只有六层，
**\(\alpha\) 的分母仍至少七层**。仅核 \(M\) 会漏掉 \(B\) 支付的部分。

## 2. 第二 \(p\)-adic 块展开的全部系数

取 \(\mathbb Z_{(p)}\) 中的调和数
\(h_m=\sum_{j=1}^m1/j\)、\(h_0=0\)，本节出现的上标均小于 \(p\)。
令 \(e=\min(d,p-n-1)\)，对 \(0\le s\le e\) 定义
\[
b_s=\binom ds\binom{n+s}{n}^{7},\qquad
C=\sum_{s=0}^e b_s,
\]
\[
A=\sum_{s=0}^e b_s H(h_d-h_{d-s}),\qquad
D=\sum_{s=0}^e b_s(h_{d-s}+7h_{n+s}-8h_s).
\tag{4}
\]
低位借位区另给
\[
E=\sum_{s=d+1}^{p-n-1}
(-1)^{s-d-1}\frac{d!(s-d-1)!}{s!}\binom{n+s}{n}^{7},
\quad U=A+HE,\quad V=D-E.
\tag{5}
\]
若上限小于下限，\(E=0\)。所有分母均为 \(p\)-unit。
\(C\) 保留其实际整数值，\(U,V\) 在模 \(p^2\) 的公式中只需模 \(p\) 值。

定义完整块 \(0\le l\le H\)
\[
\mathcal B_l=\sum_{\substack{0\le s<p\\lp+s\le N}}a_{lp+s}.
\]
则新的全尺度展开是
\[
\boxed{\mathcal B_l\equiv\binom Hl\big[C+p(U+lV)\big]\pmod{p^2}.}
\tag{6}
\]
这里包括最后一个不足 \(p\) 项的块，不能删去借位区后套普通 Lucas。

**证明。** 先用
\(\binom{Hp}{lp}\equiv\binom Hl\pmod{p^2}\)。一个自足证明是
\[
\binom{Hp}{lp}=\frac Hl\prod_{j=1}^{lp-1}\frac{Hp-j}{j}\quad(0<l<H).
\]
其中 \(j=ap\) 给 \(\binom{H-1}{l-1}\)；其余因子为
\(-1(1-Hp/j)\)，总负号为偶数。模 \(p\) 的倒数和为
\(l\sum_{s=1}^{p-1}1/s=0\)，所以这些因子之积为 \(1\pmod{p^2}\)。
端点 \(l=0,H\) 直接成立。

当 \(s\le e\)，全部低位阶乘和 \(s+1,\ldots,s+n\) 是单位，
阶乘乘积的一阶 Taylor 展开给
\[
\binom{Hp+d}{lp+s}\equiv\binom Hl\binom ds
\big[1+p(Hh_d-lh_s-(H-l)h_{d-s})\big],
\]
\[
\binom{n+lp+s}{n}^{7}\equiv\binom{n+s}{n}^{7}
\big[1+7lp(h_{n+s}-h_s)\big]\pmod{p^2}.
\]
两式相乘后恰为
\(\binom Hl b_s[1+p\{H(h_d-h_{d-s})+l(h_{d-s}+7h_{n+s}-8h_s)\}]\)。

若 \(d<s\le p-n-1\)，只有第一个二项式产生一次低位借位。
由 \((ap+b)!/p^a\equiv(-1)^aa!b!\pmod p\) 得
\[
\frac1p\binom{Hp+d}{lp+s}
\equiv H\binom{H-1}{l}
(-1)^{s-d-1}\frac{d!(s-d-1)!}{s!}\pmod p
\quad(0\le l<H).
\tag{7}
\]
这里用 Wilson 反射 \((p-k)!\equiv(-1)^k/(k-1)!\)，\(k=s-d\)。
第二个二项式仍为单位，其模 \(p\) 值是 \(\binom{n+s}{n}\)。
故此区对块的贡献为 \(pH\binom{H-1}{l}E\)。
当 \(n+s\ge p\)，第二个二项式有一次进位，其七次幂至少含 \(p^7\)，
不贡献模 \(p^2\) 项。
最后使用 \(H\binom{H-1}{l}=(H-l)\binom Hl\)，与良性区合并为 (6)。证毕。

## 3. 高阶共同因子与第二零域

令 \(w_l=\sum_{j=1}^l(-1)^j/j^7\)、\(w_0=0\)，并定义固定有理数
\[
\kappa_H=\sum_{l=0}^H\binom Hl w_l<0,\quad
\lambda_H=\sum_{l=0}^H l\binom Hl w_l,\quad
\rho_H=\lambda_H-\frac H2\kappa_H.
\tag{8}
\]
\(\kappa_H\) 就是前稿的六个常数。
由于 \(N<p^2\)，精确有
\[
Z=\sum_{l=1}^H\frac{(-1)^lT_{lp}}{l^7}+p^7W,
\qquad W=\sum_{\substack{1\le j\le N\\p\nmid j}}\frac{(-1)^jT_j}{j^7}
\in\mathbb Z_{(p)}.
\tag{9}
\]
因此模 \(p^2\) 可以仅对完整块求和。由 (6) 得
\[
\boxed{B\equiv2^H\left[C+p\left(U+\frac H2V\right)\right]\pmod{p^2},}
\]
\[
\boxed{Z\equiv\kappa_H C+p(\kappa_H U+\lambda_H V)\pmod{p^2}.}
\tag{10}
\]
相减给
\[
\boxed{Z-\frac{\kappa_H}{2^H}B\equiv p\rho_H V\pmod{p^2}.}
\tag{11}
\]
\(\rho_H\) 对每个 \(H\ge1\) 非零。事实上二项式离散差分给
\[
\rho_H=\frac H2\sum_{l=0}^{H-1}\binom{H-1}{l}(w_{l+1}-w_l)
=-\frac{H}{2\cdot6!}\int_0^1(-\log u)^6(1-u)^{H-1}\,du<0.
\tag{12}
\]
这不是对六个小数的观察。

为统一记号，取 \(\mathcal F_2\) 包含 \(2,3,5,7\) 及六个
\(\kappa_H,\rho_H\) 分子分母的全部素因子，并删去此固定集合。
若 \(C\not\equiv0\pmod p\)，则 \(r=t=0\)，由 (3) 付费七层。
若 \(C\equiv0\pmod p\)，必须先以实际整数求 \(c=C/p\)，再定义模 \(p\) 的值
\[
a=c+U+HV/2,\qquad
b=\kappa_H(c+U)+\lambda_HV=\kappa_Ha+\rho_HV.
\tag{13}
\]
它们分别是 \(B/(2^Hp)\)、\(Z/p\) 的模 \(p\) 值。

| 第二层条件 | 真实赋值 | 候选根实际付费 |
|---|---|---|
|\(a\ne0,b\ne0\)|\(r=t=1\)|恰七层|
|\(a=0,b\ne0\)|\(r\ge2,t=1\)|至少八层|
|\(a\ne0,b=0\)|\(r=1,t\ge2\)|至多六层；必须继续求 \(Z\)|
|\(a=b=0\)|\(r,t\ge2\)，且 \(V=0,c+U=0\)|高阶未定|

第三行给真正层损失的充分局部条件，尚未证明此行在本原族的无限尺度可实现，
也未证明它不可实现。第四行不能通过约掉 \(C\) 或约掉 \(p\) 后继续假定单位。
此外 (9) 的 \(p^7W\) 在探查 \(t\ge7\) 时不可删除。

## 4. 已恢复的指定非单位实例与不允许的推广

固定精确证书取三个先验反射实例，分别覆盖前稿 \(8n+1=jp\) 的 \(j=3,5,7\)：

| \((n,p)\) | \(H,d\) | \(C\bmod p\) | \(a,b\bmod p\) | \(v_p(B),v_p(Z)\) | \(v_p(q_n)\) |
|---|---|---:|---:|---:|---:|
|\((7,19)\)|\(2,11\)|0|\(0,0\)|\(2,2\)|7|
|\((23,37)\)|\(4,13\)|0|\(15,30\)|\(1,1\)|7|
|\((27,31)\)|\(6,3\)|0|\(8,27\)|\(1,1\)|7|

后两行由第二 jet 已足够恢复七层；首行须再查实际 \(Z\)，证书给其第二阶首项非零。
这些是对公式的固定验证，不能升级为所有反射实例均恢复，
也不能从第二零域在这三例中的表现推出其一般密度。
另一个预先指定的单位例 \((n,p)=(6,41)\) 核第一层和全部第二块公式。

作为代数上的范围检查，(10) 本身不强制七层恢复：取形式数据
\(C=0,U=-\lambda_H,V=\kappa_H\)，则第二余项值 \(b=0\)，
而 \(a=-\rho_H\ne0\)。这只说明现有恒等式允许第三行的线性方向，
**不是**实际二项式族已经实现该方向的反例。
若欲排除此方向，必须另证明实际 \(C/p,U,V\) 的约束。

## 5. 用真实缺层量替代第一层单位密度

对于上述窗口且 \(p\notin\mathcal F_2\)，定义
\[
\nu_{n,p}=\max\{0,7-v_p(q_n)\}
=\min\{7,\max(0,t-r)\},\quad
\mathcal D_n=\sum_{n<p\le7n,\ p\notin\mathcal F_2}\nu_{n,p}\log p.
\tag{14}
\]
它量度完整约分根的**真实缺层**，并已包含目标系数及全部 gcd。
所有单位情形及 \(t=1\le r\) 的非单位情形均为 \(\nu=0\)。
因此无条件、有限尺度地有
\[
\boxed{\log q_n\ge7(\vartheta(7n)-\vartheta(n))-\mathcal D_n-O(1).}
\tag{15}
\]
再定义明确的第二零域重量
\[
E_n^{(2)}=
\sum_{\substack{n<p\le7n,\ p\notin\mathcal F_2\\C\equiv0\ (p),\ b\equiv0\ (p)}}\log p.
\]
由 (13) 的前两行及单位情形，可得
\[
\boxed{\mathcal D_n\le7E_n^{(2)}\le7E_n+O(1),}
\tag{16}
\]
其中 \(E_n\) 为前稿第一层 \(C=0\) 的全部重量，有限删除集合之差只给 \(O(1)\)。
这是比“全部非单位素数都丢掉七层”更细的本原预算。

使用前稿 \(\log B/n\to\beta_7=23.179443965796\ldots\)，以及
[冻结实侧稿](odd_zeta_log_saddle_20261005.md)已证
\(\limsup\log|I|/n=A>1.817\)（允许零项的 \(\log0=-\infty\)），
令 \(d_*:=\limsup\mathcal D_n/n\)，则 (2)、(15) 给
\[
\boxed{\limsup\frac{\log|\mathscr P_n|}{n}
\ge A+42-\beta_7-d_*.
}\tag{17}
\]
若 \(e_2=\limsup E_n^{(2)}/n\)，还得下界
\(A+42-\beta_7-7e_2\)。若
\(e_2<(A+42-\beta_7)/7\simeq2.94834\)，就排除本原型趋零。
此处不要求每个充分大 \(n\) 的 \(I\) 非零；只在实侧的大值子序列上使用
对全部尺度成立的分母下界。

**尚缺的输入。** 没有证明 \(d_*<A+42-\beta_7\)，也没有证明该 \(e_2\) 阈值。
第二零域条件涉及 \(C/p\) 的真实高位、调和和及借位项，不能仅凭
第一层 \(C\) 的有限域零点计数直接推出。
同样，无证据允许统一断言 \(t\le r+3\)；若能另证这样的全素数界，
则 \(\nu\le3\)、\(d_*\le18\)，(17) 会立即严格为正，但本稿没有该定理。
现交付的是精确局部接口、非单位层恢复机制和剩余问题的缩小，未闭合全族预算。

### 5.1 无条件的三相邻真实根分母高度

这里另有一个绕过全部素数例外与 gcd 估计的全尺度结论。
冻结的实侧及高度渐近给
\[
I_n=n^{-7/2}\operatorname{Re}(D\Lambda^n)
+O(n^{-9/2}|\Lambda|^n),\quad D\ne0,
\]
\[
B_n=C_Bn^{-7/2}\rho^n(1+O(n^{-1})),\quad C_B>0,
\quad \rho=e^{\beta_7},\quad |\Lambda|=e^A.
\]
令
\[
L=\Lambda/\rho,\qquad K=64D/(63C_B)\ne0.
\]
则 \(|L|=e^{A-\beta_7}<1\)，且 \(\sin(\arg L)\ne0\)，两者都由冻结鞍点稿核准。
归一化误差的相同 \(n^{-7/2}\) 因子准确相消：
\[
F_n:=\frac{64I_n}{63B_n}
=\operatorname{Re}(KL^n)+O(n^{-1}|L|^n),
\qquad \alpha_n=\zeta(7)-F_n.
\tag{18}
\]
因此实际有理根的相邻差准确有渐近
\[
\delta_n:=\alpha_{n+1}-\alpha_n
=\operatorname{Re}\big(K(1-L)L^n\big)+O(n^{-1}|L|^n).
\tag{19}
\]
这里 ζ(7) 在差中完全消去，未假定它是有理或无理。

写 \(\theta=\arg L\)，\(H_0=K(1-L)\ne0\)。因为
\[
\cos^2 x+\cos^2(x+\theta)\ge1-|\cos\theta|>0,
\]
两连续差的归一化主相位不可能同时小于一个固定正数。
吸收 (19) 的 \(O(n^{-1})\) 误差，存在 \(c_0,C_0>0\)、\(n_0\)，
使所有 \(n\ge n_0\) 至少有一个 \(j\in\{n,n+1\}\) 满足
\[
|\delta_j|\ge c_0|L|^j>0,
\qquad |\delta_j|\le C_0|L|^j
\quad\hbox{对全部充分大的 }j.
\tag{20}
\]
若 \(\alpha_j=A_j/q_j\)、\(\alpha_{j+1}=A_{j+1}/q_{j+1}\) 为各自实际约分，
非零差的交叉分子是非零整数，故
\[
\frac1{q_jq_{j+1}}\le|\delta_j|\le C_0|L|^j,
\quad q_jq_{j+1}\ge C_0^{-1}|L|^{-j}.
\]
因 \(j\ge n\)、\(|L|<1\)，于是对每个充分大 \(n\) 都有
\[
\boxed{\max(q_n,q_{n+1},q_{n+2})
\ge C_0^{-1/2}\exp\big((\beta_7-A)n/2\big),}
\tag{21}
\]
进而
\[
\boxed{\liminf_{n\to\infty}\frac1n
\log\max(q_n,q_{n+1},q_{n+2})
\ge\frac{\beta_7-A}{2}\simeq10.68079.}
\tag{22}
\]
这是真实约分根分母的无条件指数下界，不是统一整数化成本的下界。
两连续差中至少一个非零足够，不需要每一对根不同，也不需要每个 \(I_n\) 非零。
不由有限根分母的拟合推导指数；所用实侧渐近和有理数分离都是全尺度输入。

该下界只有归一化误差衰减指数 \(\beta_7-A\simeq21.36159\) 的一半。
即使分母与误差的大项恰好在同一尺度，半指数的高度下界仍容许本原值衰减。
而 (21) 的大分母项也未必与实误差大项重合。因此 (22) 本身既不证明
本原值趋零，也不排除它趋零；全族无理性或失败预算仍未闭合。

## 6. 证书范围

[脚本](odd_zeta_log_primitive_20261005_verify.py)与
[JSON](odd_zeta_log_primitive_20261005_verify.json)核上述四个指定输入的全部 \(p\) 块、
借位展开、\(B,Z\) 模 \(p^2\)、完整约分根及全部 gcd；另核六个固定
\(\kappa,\lambda,\rho\) 的差分恒等式及形式线性方向。
证书还用独立形式变量核 (19) 的差分系数；§5.1 的全尺度相位与有理分离
证明不由此有限符号检查替代。
不计算实周期，不参数扫描，不以有限实例代替全尺度证明。
原候选、前轮算术稿及其证书均保持冻结。
