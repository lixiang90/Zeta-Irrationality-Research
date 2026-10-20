# 第277轮：四分点 χ−8 的真实连续双 Hahn 平方余项

2026-10-20，根的全尺度来源证书。最终目标固定为新的指定值 \(L=L(2,\chi_{-8})\) 无理性；全部反证为实际 \(L=u/v\)，u∈Z、v>0、gcd=1。对象只取下述两四分点、平移n及同次数n的正交逼近。这里先支付纯投影、实际非零和精确裸指数，**未支付实际既约分母，不准入数值证明**。不是重开275的WZ同步前缀或原RV/multileaf来源。

来源线索为 Prévost [2606.15132v1](https://arxiv.org/html/2606.15132v1) 的余项Padé与生成多项式。根实际读§1–6（HTML48–415），未采用打印Theorem1的冲突规范：r=1的ρ符号、两处a_n系数及整数w₁导数阶均须重核。下文直接重建z=−1、s=2的实际对象，不从一般signed权的支配上界推正交平方。原文称Wilson类，此处准确为**连续双Hahn a=b=c=1**；标准输入另核官方 [DLMF18.25.2、7–8](https://dlmf.nist.gov/18.25#ii)及[18.26.2](https://dlmf.nist.gov/18.26#i)。下文身份与选择不作全球首次性声明。

## W1. 从实际 Lerch 积分到正确正测度

记 \(\Phi(a)=\sum_{k\ge0}(-1)^k/(k+a)^2\)，a>0，\(f(x)=1/\sinh(\pi x)\)。有
\[
\Phi(a)=\frac1{2a^2}
+\int_0^\infty\frac{2ax}{(a^2+x^2)^2}f(x)\,dx.
\tag{W1}
\]
可从 \(\Phi(a)=\int_0^\infty t e^{-at}/(1+e^{-t})\,dt\) 重建：经典cosh乘积的对数导数给
\[
\int_0^\infty\sin(tx)f(x)\,dx
=2\sum_{j\ge0}\frac{t}{(2j+1)^2\pi^2+t^2}
=\tfrac12\tanh(t/2).
\]
代入 \(1/(1+e^{-t})=1/2+\tfrac12\tanh(t/2)\) 后交换积分，内层为 \(2ax/(a^2+x^2)^2\)。绝对可积性可由 \(|\sin(tx)|\le tx\)、\(\int xf(x)dx<\infty\)、\(\int t^2e^{-at}dt<\infty\) 给出，不能靠条件振荡交换。

令
\[
w(x)=-x^2f'(x)=\pi x^2\frac{\cosh\pi x}{\sinh^2\pi x}>0,
\quad
H(x)=\left|\frac{\Gamma(1+ix)^3}{\Gamma(2ix)}\right|^2
=4\pi^2x^4\frac{\cosh\pi x}{\sinh^2\pi x}.
\]
所以 \(x^2w=H/(4\pi)\)。在原文积分定义m=s=2中，\(x^2\int_x^\infty f''(t)dt=-x^2f'(x)\)，导数是一阶，不能沿用误印的二阶。两端分部积分的边界均0，给
\[
\int_0^\infty w(x)dx=2\int_0^\infty xf(x)dx=\tfrac12,
\quad
\Phi(a)=\frac1{2a^2}+\frac1a\int_0^\infty\frac{w(x)}{a^2+x^2}dx.
\]
定义固定正测度及Stieltjes函数
\[
d\mu(x)=\frac{H(x)}{4\pi}dx=-x^4f'(x)dx,\qquad
F(t)=\int_0^\infty\frac{d\mu(x)}{t+x^2}.
\]
用 \(x^2/(a^2+x^2)=1-a^2/(a^2+x^2)\)，精确得到
\[
\boxed{\Phi(a)=\frac1{2a^2}+\frac1{2a^3}-a^{-3}F(a^2).}
\tag{W2}
\]
这是收敛正测度，不用Hadamard有限部，也无遗漏的π或log背景栏。

## W2. 同一测度的有理矩与真实正交多项式

全部矩为有理数：
\[
\mu_j=\int x^{2j}d\mu
=(2j+4)\int_0^\infty x^{2j+3}f(x)dx
=(-1)^{j+3}(2^{2j+4}-1)B_{2j+4}.
\tag{W3}
\]
第二式由分部积分，第三式由csch的指数展开和偶ζ公式。von Staudt–Clausen给每个奇分母p满足p−1整除2j+4，故被 \(2^{2j+4}-1\) 消掉；2处B的赋值恰−1，故 \(\mu_j\in\tfrac12\mathbf Z\)、\(v_2(\mu_j)=-1\)。只需有理性即可定义后文，半整数不等于最后逼近分母免费。

把多项式变量记为y，固定
\[
T_n(y)={}_3F_2\!\left(\begin{matrix}-n,1-i\sqrt y,1+i\sqrt y\\2,2\end{matrix};1\right)
=\sum_{k=0}^n\frac{(-1)^k\binom nk}{((k+1)!)^2}\prod_{h=1}^k(h^2+y).
\tag{W4}
\]
上述标准连续双Hahn正交性以参数(1,1,1)给
\[
\int T_n(x^2)T_m(x^2)d\mu=0\ (n\ne m),\qquad
h_n:=\int T_n(x^2)^2d\mu=\frac1{2(n+1)}.
\tag{W5}
\]
DLMF多项式为 \(S_n=((n+1)!)^2 T_n\)，其norm是 \(2\pi n!((n+1)!)^3\) 对Hdx；除上述归一和4π即得W5。此处不把支配测度换成原signed测度；W2已精确给同一个H。

最高两项还给 \(P_n=(-1)^n((n+1)!)^2T_n\) 首一且
\[
[y^{n-1}]P_n=-\frac{n(n+1)(4n+5)}6=:c_n.
\]
正交三项递推的中系数因此是
\[
\beta_n=c_n-c_{n+1}=(n+1)(2n+3)
=\frac1{h_n}\int x^2T_n(x^2)^2d\mu.
\tag{W6}
\]
最后等式也直接由yP_n向P_n投影得到，无须另借渐近公式。

## W3. 完整有理逼近及严格平方误差

固定 \(a>n\)、\(q_n(a)=T_n(-a^2)>0\)，定义
\[
S_n(a)=\int_0^\infty
\frac{q_n(a)-T_n(x^2)}{a^2+x^2}d\mu(x)\in\mathbf Q
\quad(a\in\mathbf Q),
\qquad f_n(a)=S_n(a)/q_n(a).
\tag{W7}
\]
除式恰为degree≤n−1的有理多项式，全部矩由W3给出；n=0时S=0。正号q来自W4：每个h≤k≤n<a使a²−h²>0，整个和每项正。

先由定义得 \(F(a^2)-f_n=q_n^{-1}\int T_n(x^2)/(a^2+x^2)d\mu\)。再用 \((T_n(x^2)-q_n)/(a^2+x^2)\) 的degree≤n−1及W5，得到同一对象的恒等式
\[
D_n(a):=F(a^2)-f_n(a)
=\frac1{q_n(a)^2}\int_0^\infty
\frac{T_n(x^2)^2}{a^2+x^2}d\mu>0.
\tag{W8}
\]
定义 \(U_n(a)=1/(2a^2)+1/(2a^3)-a^{-3}f_n(a)\)，则 \(\Phi(a)-U_n(a)=-a^{-3}D_n(a)<0\)。这里出现第二个q，是因为已经付清真实正交，不是把原文一般one-V上界擅自平方。

## W4. 两镜像的指定 χ−8 投影和全部反证

只取 \(\Theta=\{1/4,3/4\}\)、\(a_{\theta,n}=n+\theta\)，n≥0；定义实际有理数
\[
r_n=\frac1{16}\sum_{\theta\in\Theta}
\left\{\sum_{k=0}^{n-1}\frac{(-1)^k}{(k+\theta)^2}
+(-1)^nU_n(a_{\theta,n})\right\}.
\tag{W9}
\]
按八余类直接拆原级数，
\[
16L(2,\chi_{-8})=\Phi(1/4)+\Phi(3/4).
\]
平移身份及W8给
\[
L-r_n=\frac{(-1)^{n+1}}{16}
\sum_{\theta\in\Theta}a_{\theta,n}^{-3}D_n(a_{\theta,n})\ne0
\quad\text{对每个n≥0}.
\tag{W10}
\]
两个镜像误差同号，没有用单镜像π²背景或未知振幅。若 \(r_n=A_n/d_n\) 既约、d_n>0，任意实际 \(L=u/v\) 给
\[
0<|vd_n(L-r_n)|=|ud_n-vA_n|\in\mathbf Z.
\tag{W11}
\]
因此只能在**同一实际d_n**上支付费用，不能把单个q分母、W3半整数或旧WZ内容转交给它。

## W5. 精确全尺度裸指数

对θ固定为上述两值，
\[
q_n(n+\theta)=\sum_{k=0}^n
\binom nk\frac{\prod_{h=1}^k((n+\theta)^2-h^2)}{((k+1)!)^2}.
\]
各项正。统一Stirling给第k项的对数为
\[
n\varphi(k/n)+O(\log(n+2)),\quad
\varphi(t)=(1+t)\log(1+t)-2(1-t)\log(1-t)-3t\log t.
\]
两端使用0log0=0；端点的Gamma参数至少θ，不越过0，误差一致。有限和至多n+1项，最大项给上下界。唯一内部最大点
\[
t_*=(\sqrt5-1)/2,\quad
\varphi'(t)=\log\frac{(1+t)(1-t)^2}{t^3},\quad
\varphi(t_*)=-5\log t_*=\log\rho,\quad
\rho=(11+5\sqrt5)/2.
\]
取最近整数k即给
\[
\lim n^{-1}\log q_n(n+\theta)=\log\rho.
\tag{W12}
\]
误差积分也没有隐藏指数：以 \(T_n^2d\mu/h_n\) 为概率测度，用Jensen及W6，
\[
\frac{h_n}{a^2+\beta_n}
\le J_n(a):=\int\frac{T_n(x^2)^2}{a^2+x^2}d\mu
\le\frac{h_n}{a^2}.
\tag{W13}
\]
a=n+θ使两界均为正的Θ(n⁻³)；再乘a⁻³和q⁻²。W10的正项相加保留同一指数，故
\[
\boxed{\lim_{n\to\infty}n^{-1}\log|L-r_n|=-2\log\rho.}
\tag{W14}
\]
不仅是一个安全upper；精确率也约束以后采用的费用或子列量词。

## W6. 所需完整费用、独审与来源选择

数值准入的充分门槛是：对一个明确预定的无界子列及某δ>0，完整实际既约分母满足
\[
\limsup n^{-1}\log d_n\le2\log\rho-\delta.
\tag{W15}
\]
W14同时说明，如果成功要求同一严格负线性指数，W15型严格费用余量也是必要的。临界率的次指数出口另核；没有把严格指数判据当成所有无理性方法。

目前没有d_n的完整全素数幂结算。特别quarter求值q的二处负赋值可在线性商S/q中取消，不能据此称实际d_n至少有该2幂；两镜像合并、有限前缀和外a⁻³还都要一起约分。根未执行n/prime/参数扫描、历史producer或CAS，不能用样本替这项。

此源与旧G的Zudilin递推拥有同样ρ不证明它们等价或给新内容；根读[旧v3](https://arxiv.org/html/math/0201024v3)§1及所需§2–3，只用于去重与“快速逼近仍需付费”的边界。当前实际对象为W9纯χ−8双quarter输出，不把其一手新颖性或最终结果认作已完成。旧WZ的10log2尾速也不转交；不同逼近的d不同。

独审：analytic_gate_277独立从W1重推W2、官方连续双Hahn规范、W8平方及W12–W14；alternative_gate_277独立核整数导数纠错、权的精确身份、双quarter纯投影与误差同号。最终审读范围分别保存在[解析竞争稿末](analytic_gate_round277.md)和[一手竞争稿末](alternative_gate_round277.md)；作者不审自己的证明。根逐式核三竞争稿的主结论，不把工具/状态测试当数学认证。

资源决定：这项真实新正交匹配支持**仅一轮278完整实际费用核查**，不重开其它source，也不声称有足够负净预算。若完整预算仍不能过W15且没有付足的新机制，窗口到期结束。新文档、局部no-go和裸率本身不重置未改善完整净预算的计数。
