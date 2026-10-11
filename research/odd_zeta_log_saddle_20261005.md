# q=7 对数矩端点的围道表达与振荡强渐近

日期：2026-10-05。承接冻结的[整数候选](odd_zeta_log_moment_candidate_20261004.md)。
本稿研究实际积分 \(I_7(R_{n,7})\)，不以 ζ(7) 的无理性为前提。
核心结果是：它有共轭 saddle 的振荡强渐近，**原始积分的 limsup 指数为正**；
每个充分大的相邻两项块中至少一项非零且指数大。
这不是全部单项非零定理，也不是实际本原整数形式的完整预算定理。

## 1. Mellin–Barnes 的真实目标表达

记 \(q\ge k\ge2\)，\(N=qn\)，保留
\[
M_{n,q}(z)=\frac{(-1)^N N!}{(n!)^q}
\frac{\prod_{j=1}^n(z-j)^q}{\prod_{r=0}^{N}(z+r)},\qquad
K(z)=\pi\csc(\pi z).
\]
对 \(0<c<1\)，核身份
\[
\frac1{1+u}=\frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
K(z)u^{z-1}\,dz
\]
成立。这是 Mellin inversion 的标准二项核，也可向右取留数直接核其交错级数。
权 \(u^{c-1}|\log u|^{k-1}\) 可积，\(K\) 及其导数在垂直方向指数衰减，
故 Fubini 与 \(k-1\) 次分部积分合法：
\[
\boxed{I_k(R_{n,q})=
\frac1{(k-1)!\,2\pi i}
\int_{c-i\infty}^{c+i\infty}
M_{n,q}(z)K^{(k-1)}(z)\,dz.}
\tag{1}
\]
两个 \((-1)^{k-1}\) 正好抵消，不可遗漏符号。

\(K^{(k-1)}\) 在每个整数处最多有 \(k\) 阶极点，
\(M\) 在 \(1,\ldots,n\) 各有 \(q\) 阶零。
因此 \(q\ge k\) 时 integrand 在这些点正则；
可把线移至 \(c_n=n+1/2\)，且没有留数项。
固定 \(n\) 的水平尾部由 \(M(z)=O(1/z)\) 与 \(K^{(k-1)}\) 的指数衰减消失。

**不能把整条线再平移到 \(an>n+1\)：** \(n+1,n+2,\ldots\) 的核极点不被消去。
下面只在上、下半平面变形，避开这些实轴极点。

## 2. q=7 的指数函数与精确 Gamma 身份

以下固定 \(q=k=7\)，缩放 \(z=nw\)。原始 Mellin 函数准确等于
\[
M_{n,7}(nw)=(-1)^n
\frac{\Gamma(7n+1)}{\Gamma(n+1)^7}
\frac{\Gamma(nw)^8}
{\Gamma(n(w-1))^7\Gamma(n(w+7)+1)}.
\tag{2}
\]
在 \(\operatorname{Re}w>1\) 使用连续的主对数，令
\[
F(w)=7\log7+8w\log w
-7(w-1)\log(w-1)-(w+7)\log(w+7),
\]
\[
h(w)=\frac{(w-1)^{7/2}}{w^4(w+7)^{1/2}},
\quad C_0=\frac{\sqrt7}{(2\pi)^3}.
\]
Stirling 公式在任何含下述 saddle 的闭邻域上统一给
\[
M_{n,7}(nw)=(-1)^n C_0 n^{-4}h(w)
e^{nF(w)}(1+O(1/n)).
\tag{3}
\]
这里 \(n^{-4}\) 包含 Gamma 比值的 \(n^{-1}\)；漏掉它会改变强渐近的多项式阶数。

对于 \(\operatorname{Im}w\ge1/2\)，几何展开准确给
\[
K^{(6)}(nw)=2i\pi^7e^{i\pi nw}
\bigl(1+O(e^{-2\pi n\operatorname{Im}w})\bigr).
\tag{4}
\]
因此上半平面的主指数为
\[
H(w)=F(w)+i\pi w,\quad
F'(w)=8\log w-7\log(w-1)-\log(w+7),
\]
\[
\boxed{F''(w)=-\frac{56}{w(w-1)(w+7)}.}
\tag{5}
\]

## 3. 被认证的 saddle；不是数值拟合

方程 \(H'(w)=0\) 对应
\[
P(w)=w^8+(w-1)^7(w+7)=0.
\tag{6}
\]
取中心 \(c_*=1.1128732+1.5247965i\) 与半径 \(10^{-6}\) 的有理圆盘。
脚本用 exact rational Taylor coefficients 验证
\[
|P(c_*)|+\sum_{j=2}^8
\frac{|P^{(j)}(c_*)|}{j!}(10^{-6})^j
< |P'(c_*)|\,10^{-6}.
\]
Rouché 定理保证圆盘内恰有一个零点 \(w_*=a+ib\)。
下列区间由外包整个圆盘的 Arb/Acb ball 运算认证，不把浮点近似当根：
\[
1.1128<a<1.1130,\quad 1.5247<b<1.5249,
\]
\[
1.817<A:=\operatorname{Re}H(w_*)<1.819,\quad
9.177<\Omega:=\operatorname{Im}H(w_*)<9.179,
\]
\[
\operatorname{Re}F''(w_*)>2,\qquad
-4<\operatorname{Im}F'(w_*)<-2.
\tag{7}
\]
由 (6)，\(\exp(F'(w_*))=-1\)；最后一个区间选择唯一的对数值
\(F'(w_*)=-i\pi\)，故这里确为 \(H'=0\)，而非另一张分支的代数零点。
圆盘还认证
\[
\operatorname{Re}F(a)<0,\qquad
\operatorname{Re}H(a+i/2)<1,\qquad
b^2>\frac{a(a-1)(a+7)}{3a+6}.
\tag{8}
\]

近似中心值仅供辨识：
\[
w_*\simeq1.1128731934+1.5247965276i,\qquad
H(w_*)\simeq1.8178582154+9.1778786449i.
\]
这些小数不承担存在性、分支或严格正负的证明。

## 4. 主峰是唯一全局峰，连接段的成本严格较小

在直线 \(w=a+iy\) 上，置 \(g(y)=\operatorname{Im}F'(a+iy)\)。
由 (5)
\[
g'(y)=\operatorname{Re}F''(a+iy)
=-56\,\frac{a(a-1)(a+7)-(3a+6)y^2}
{|(a+iy)(a-1+iy)(a+7+iy)|^2}.
\tag{9}
\]
它先负后正，唯一转点在
\(y_{\rm turn}^2=a(a-1)(a+7)/(3a+6)\)。
同时 \(g(0)=g(\infty)=0\)，\(g(b)=-\pi\)，且 (8) 证明 \(b>y_{\rm turn}\)。
因此 \(g=-\pi\) 恰有两个解；较小者是 \(\operatorname{Re}H\) 的局部极小，
\(b\) 是唯一局部极大。\(\operatorname{Re}H(a+iy)\to-\infty\) 当 \(y\to\infty\)。
由 (7)–(8)，峰值 \(A\) 严格大于 \(y=0\) 与 \(y=1/2\) 的值，
故 \(b\) 也是 \(y\ge1/2\) 上唯一全局最大点。

上半围道从 \(c_n=n+1/2\) 走到 \(c_n+in/2\)，再横走到 \(na+in/2\)，
最后沿 \(na+i[\,n/2,\infty)\) 上行；下半取共轭路径。
所有水平移动在非实轴内完成，不跨过 \(n+1,n+2,\ldots\) 的极点。

对 \(n\ge5\)，连接段缩放后在 \(1<x\le a,\ 0\le y\le1/2\)。
该矩形内
\[
\operatorname{Re}F'(x+iy)
=8\log|x+iy|-7\log|x-1+iy|-\log|x+7+iy|>0.
\]
例如 \(|x+iy|\ge1\)、\(|x-1+iy|<3/5\)、\(|x+7+iy|<9\)，
故下界为 \(-7\log(3/5)-\log9>0\)，后者等价于 \(9(3/5)^7<1\)。
于是连接段的实指数不超过同一 \(y\) 下 \(x=a\) 的值。
(9) 的两个转向说明在 \(0\le y\le1/2\) 其最大值必在一个端点；
(8) 将其严格压到 1 以下，而 \(A>1.817\)。

在起始竖段 \(\operatorname{Re}z=n+1/2\)，
\(|\csc(\pi z)|=1/\cosh(\pi\operatorname{Im}z)\)；
所有所需导数也有固定倍数的 \(e^{-\pi|\operatorname{Im}z|}\) 界。
Gamma Stirling 的乘性余项在
\(\operatorname{Re}(n(w-1))\ge1/2\) 统一有界；
连接段上的振幅至多为固定多项式成本。
因此这些段的贡献为 \(O(n^C e^n)\)，与主峰指数之间有固定正间隔。
无穷尾部由 \(F(w)\to7\log7\)、\(h(w)=O(1/w)\) 和核指数衰减控制。
该论证没有遗漏一个更大的端点贡献或 real-axis residue。

## 5. 振荡强渐近与无条件非零块

\(b\) 处展开
\[
H(a+iy)=H(w_*)-\tfrac12F''(w_*)(y-b)^2+O((y-b)^3).
\]
\(\operatorname{Re}F''>0\) 保证高斯可积；取平方根为正实部支。
统一 Stirling、(4)、局部 Taylor 的偶次高斯展开及指数小尾部给
\[
\boxed{I_7(R_{n,7})=(-1)^n n^{-7/2}
\operatorname{Re}\!\left(D e^{nH(w_*)}\right)
+O(n^{-9/2}e^{nA}),}
\tag{10}
\]
其中
\[
\boxed{D=
\frac{i\sqrt7\,\pi^3\sqrt{2\pi}}{2880}
\frac{h(w_*)}{\sqrt{F''(w_*)}}.}
\tag{11}
\]
常数计算来自上半积分与下半的共轭相加；
\(n\,n^{-4}n^{-1/2}=n^{-7/2}\)。
三阶 Taylor 的首个奇项在对称高斯区间积分为零，剩余归一化误差 \(O(1/n)\)；
该误差是相对于单个复 saddle 振幅，不要求最终实部远离零。

主指数的指数本身是明确代数数。由 \(F'(w_*)=-i\pi\)，
\[
H(w_*)=F(w_*)-w_*F'(w_*)
=7\log7+7\log(w_*-1)-7\log(w_*+7).
\]
因此可令
\[
\Lambda=-\left(\frac{7(w_*-1)}{w_*+7}\right)^7,\qquad
(-1)^ne^{nH(w_*)}=\Lambda^n.
\]
这里没有假定其 argument 是 π 的无理倍；(10) 也可直接写成
\(n^{-7/2}\operatorname{Re}(D\Lambda^n)+O(n^{-9/2}|\Lambda|^n)\)。

圆盘计算另认证 \(D\ne0\)（近似 \(-0.005092+0.002429i\)）。
令 \(\phi=\arg D\)，\(\Theta=\Omega-3\pi\)，则 (10) 为
\[
I_7=e^{nA}n^{-7/2}
\bigl(|D|\cos(n\Theta+\phi)+O(1/n)\bigr).
\tag{12}
\]
区间认证 \(-1/4<\Theta<-6/25\)，故 \(\sin\Theta\ne0\)。

对任意实 \(\alpha\)，
\[
\max\{|\cos\alpha|,|\cos(\alpha+\Theta)|\}
\ge|\sin\Theta|/2.
\]
把 (12) 的两项误差吸收，得到常数 \(c>0,n_0\)，对每个 \(n\ge n_0\)，
至少一个 \(m\in\{n,n+1\}\) 满足
\[
\boxed{|I_7(R_{m,7})|\ge
c\,m^{-7/2}e^{mA}>0.}
\tag{13}
\]
而 (10) 的上界适用于所有充分大 \(n\)。因此
\[
\boxed{\limsup_{n\to\infty}\frac1n\log|I_7(R_{n,7})|=A>1.817.}
\tag{14}
\]
若某些 \(I_7\) 恰为零，约定 \(\log0=-\infty\)，不影响该 limsup。

**尚未证明**每个充分大单项非零，也没有证明归一化后绝对值的 liminf。
没有用“phase 小数看起来不为有理倍 π”假定相位等分布；
(13) 只用被认证的 \(\sin\Theta\ne0\)。

## 6. 对逼近预算的含义和没有排除的空间

这补上了上一轮候选“实际积分指数未明”的缺口：
\(q=7\) 族的原始端点并没有沿全部尺度指数趋零。
安全乘子 \(L_{7n}^{7}\) 后的 limsup 指数更为 \(49+A>0\)。

但对 \(S=s/M\)、\(B=R(-1)\)，真正本原整数形式为
\[
\ell_n=\frac{64M}{\gcd(63MB,64s)}I_7(R_{n,7}).
\]
该倍率可能小于 1，并需单独研究；
不能由原始积分增长或安全 LCM 失败推出本原形式全族失败。
其实际分母、gcd 见[算术分支](odd_zeta_log_arithmetic_20261005.md)。

还可把两分支合成一个只缺素数分布输入的条件结论。按算术稿定义
\(E_n=\sum_{n<p\le7n,\ C_{n,p}\equiv0\ (p)}\log p\)，忽略固定坏素数，
令 \(e=\limsup E_n/n\)。其无条件有限界为
\[
\log(64M/h)\ge7(\vartheta(7n)-\vartheta(n)-E_n)-\log B-O(1).
\]
在 (13) 每块选出的无穷指数大子序列上，结合
\(\log B/n\to\beta_7\) 与素数定理，严格得到
\[
\boxed{\limsup_{n\to\infty}\frac1n\log|\ell_n|
\ge A+42-\beta_7-7e.}
\tag{15}
\]
不必先证明所有单项非零。整数根隔离与正实对数界认证
\(\beta_7<23.19\)，故 **若 \(e\le2.94\)，右端严格大于 0**。
该式只是条件本原失败判据：\(e\le2.94\) 仍未证明，
反射例也没有否定它。这里的 \(e\) 是带 \(\log p\) 权重且除以 \(n\) 的量，
不是例外素数个数比例。小于该阈值时，至少无穷多本原形式增长；
并未宣称所有本原单项都增长。

(10) 同时给出了共轭 saddle 相位。
如尝试相邻尺度组合消去主振荡，新的组合需要重新核整数系数高度、
残余振幅、非零与全部分母；消掉一个渐近首项本身通常只节省多项式因子。
本稿没有排除经特殊子序列、整数尺度组合或改变 mixed 系统后获得新逼近的可能。

## 7. 可复核输入

[脚本](odd_zeta_log_saddle_20261005_verify.py)与
[JSON](odd_zeta_log_saddle_20261005_verify.json)
检查有理 Rouché 不等式、\(F''\) 恒等式、Gamma 比值的代数因子、
整个根圆盘上的分支与严格区间、连接段界和非退化振幅。
强渐近与所有尺度结论由 §§1–5 的围道、统一估计和局部高斯证明承担。

参照[标准 Stirling 展开](https://dlmf.nist.gov/5.11)；
本报告实际匹配的正交结构与文献范围见[结构报告](odd_zeta_log_structure_20261005.md)。
固定小例的相反符号由[非零分支](odd_zeta_log_nonzero_20261005.md)另行认证。
没有新无理性定理或 Lean 形式化。

