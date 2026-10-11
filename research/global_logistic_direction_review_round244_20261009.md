# 第244轮：logistic方向独立复盘与一个字符移位候选

2026-10-10，A；第244轮既定文件名仍用20261009。数学程序、CAS、参数/素数扫描及Lean运行0。本稿独立完整复读240正式复盘、243报告及相关证明，只选择一个新对象，不优化旧Schur层。

## 1. 关闭哪条支路，保留哪些资产

建议**结束固定K5源当前逐层Schur/增长素数窗口优化的默认主线**。理由是投资门槛，绝非actual费用lower或源no-go。

240支付整个简单极点空间的真实投影；241支付每个固定有理关系点的无界非零；242支付完整调和头、所有素数幂与全prime安全机制。243又精确支付商部首层、全部minor内容及zero-slot优化，净上界从1009/40改善到1511/60，宏观节省1/24。另一方面，原实处−6完整Fstar证书仍未独立认证，足够小的完整primitive费用也未付。

若只更改 \(2n<p<3n\) 而沿用其它已选bounds，认证小于6需要新signed窗口upper
\[
 B_{\rm new}<5/8-I_{\rm in},\qquad I_{\rm in}\ge12/5.
\]
这要求所选证书总节省超过42/5；目前的1/24没有提供可跨门槛的机制。此比较不能限制真实费用，也不排除将来一个完整、更强的同对象证书。s=1限制目标秩下降不等于完整Schur低秩，不能为此自动续开多轮。

## 2. 唯一候选与数值出口

候选固定 \(\chi=\chi_{-7}\)，
\(\chi(1),\ldots,\chi(6)=(1,1,-1,1,-1,-1)\)，
\[
 Y=L(2,\chi)=\sum_{m\ge1}\chi(m)/m^2.
\]
目标出口是Y的无理性；不把已知 \(\chi_{-3}\) 定理换个conductor就当证明，也不同时启动其它字符或更高权。

有限primary核查找到Sun–Zhou的现行v2：它确实给出涉及Y、\(\pi^2\) 和二阶调和数的模形式/binomial恒等式，相关对象不是本稿新发现的常数。实际读域是摘要、引言及Theorem1.1；该读域未给Y无理性定理，不能由此宣称全球未解决。[作者v2](https://arxiv.org/html/2602.12091v2)。
CDT已宣布的单值结论是 \(L(2,\chi_{-3})\) 及其与 \(1,\zeta(2)\) 的Q-LI；这个conductor-specific入口不能直接移植到7。[作者摘要](https://arxiv.org/abs/2408.15403)。

下一主投入前仍需核定这个数值出口的最新既有定理范围。若已有对应定理，保留下面的结构引理，取消“新数值”出口；搜索未命中不是新颖性证书。

## 3. 全函数空间投影：把最高调和头从5降到2

沿用240已自足支付的
\[
 t=\tfrac12+iy,\quad \rho(y)=\frac{\pi}{2\cosh^2\pi y},\quad
 B(G)=\int G(t)\rho(y)dy.
\]
置 \(c_a=a/7-1\)，定义新的完整泛函
\[
 \boxed{V_\chi(f)=-\frac1{49}\sum_{a=1}^6\chi(a)
 B\big((t+c_a)f(t+c_a)\big).} \tag{D1}
\]
域为有理多项式加负整数点 \(-j,\ j\ge1\) 的简单极点；允许所需任意有限degree。所有translated lines都避开这些极点。

由240的Fourier/Laplace身份，
\[
 B((t+c_a+j)^{-1})=\zeta(2,j+a/7),\quad
 B((t+c_a)^k)=B_k(a/7),
\]
其中 \(B_k(x)\) 是经典Bernoulli多项式，\(B_1(x)=x-1/2\)。
第一式的Laplace交换由 \(j+a/7-1/2>0\) 支付。字符和为0，故
\[
 \boxed{V_\chi((u+j)^{-1})
 =j\big(Y-H_{7j,\chi}^{(2)}\big),\quad
 H_{M,\chi}^{(2)}=\sum_{m=1}^M\chi(m)/m^2.} \tag{D2}
\]
确实 \(\sum_a\chi(a)\zeta(2,j+a/7)=49(Y-H_{7j,\chi}^{(2)})\)，
而 \(u/(u+j)=1-j/(u+j)\) 的常数被字符和消掉。
多项式值
\[
 V_\chi(u^e)=-\frac1{49}\sum_a\chi(a)B_{e+1}(a/7)\in\mathbf Q. \tag{D3}
\]
因此完整空间严格满足 \(V_\chi(f)=a(f)Y+b(f)\)，两系数有理；
没有遗漏其它周期或先删除不利列。

仍固定 \(R_n=D_n^4/D_{5n}\)、\(h=3n\)，以D2–D3定义
\(Q_{\chi,n}(T)=\det[V_{\chi,T}(u^{i+j}R_n)]_{i,j<h}\in\mathbf Q[T]\)。
目标系数仍是 \(a_e=-[u^{-2}]u^eR_n\)，
\(a_e=0\ (e<n-2)\)、\(a_{n-2}=-1\)，故秩至少 \(n-1\)。
这区别于秩一period-shift正Gram；也不保证关系点非零。

## 4. 共同积分线与uniform leading能量转移

移位不是免费的多叶Heine调用。这里可以真正统一到 \(\Re u=0\)：
\[
 K_a(u)=\frac{\pi}{2\sin^2\pi(u-a/7)}
\]
的原translated line为 \(\Re u=a/7-1/2\)，共同线0和它都处于
\((a/7-1,a/7)\) 同一无极点strip。\(f\) 的负整数极点也未穿过；
水平边指数衰减乘固定多项式，故逐叶移线给
\[
 V_\chi(f)=\int_{\mathbf R} f(iy)\mu_\chi(y)dy,\qquad
 \mu_\chi(y)=-\frac{\pi\,iy}{98}\sum_{a=1}^6
 \chi(a)\csc^2\pi(iy-a/7). \tag{D4}
\]
所有行列共享同一线，现在Andréief才产生同一个Vandermonde。

有常数 \(C_\chi\) 使
\[
 |\mu_\chi(y)|\le C_\chi|y|\rho(y).
\]
因为 \(|\sin\pi(iy-a/7)|^2=\sin^2(\pi a/7)+\sinh^2(\pi y)\)，
每一项对 \(\operatorname{sech}^2(\pi y)\) 的比值一致有界。
另一方面，对全部实y，
\[
 \frac{|R_n(iy)|}{|R_n(1/2+iy)|}
 \le\prod_{j=1}^{5n}\frac{|j+1/2+iy|}{|j+iy|}
 \le\prod_{j=1}^{5n}(1+1/(2j))\le C\sqrt n. \tag{D5}
\]
四份分子 \(D_n\) 的比值各不大于1；最后用harmonic和给统一常数。
再用 \(|iy|\le|1/2+iy|\)，D4–D5及绝对Andréief得
\[
 |Q_{\chi,n}(Y)|\le(C_\chi'\sqrt n)^h\,\mathcal H_n,\quad
 \mathcal H_n=\frac1{h!}\int_{\mathbf R^h}
 \prod_\ell |t_\ell R_n(t_\ell)|\rho(y_\ell)
 \prod_{i<j}(y_i-y_j)^2dy. \tag{D6}
\]
新prefactor的对数为 \(O(n\log n)=o(n^2)\)；没有mixed-node差异、
隐藏截断或非统一尾估计。**同一leading Heine envelope的转移已付**。
归一化 \(S_n^h/F_n\) 也完全相同；但−6数值仍条件于原完整Fstar
证书，D6不等于它的独立认证。

D4另有实际几何结构：\(\mu_\chi\) 为正的偶函数（0处为0）。
令 \(C_y=\cosh2\pi y,S_y=\sinh2\pi y,\theta_a=\pi a/7\)，y>0时
\[
 \sum_a\chi(a)\csc^2\pi(iy-a/7)
 =4iS_y\sum_{a=1}^3
 \frac{\chi(a)\sin(2\theta_a)}{(C_y-\cos2\theta_a)^2}.
\]
a=1正项严格大于a=3负项的绝对值，a=2正，所以虚部正。
然而 \(R_n(iy)\) 有变化的复相位；这个正密度**不证明原矩阵正定**
或 \(Q_{\chi,n}(q)\ne0\)。本稿不另开对称核，也不借对称源的非零证书。

## 5. 完整整数模型与不能省略的固定7账

\(S_n=(5n)!/(n!)^4\) 仍清全部残数；整数首一除法仍给
\(q_e\in\mathbf Z[u]\)。额外常数这次靠 \(\sum\chi=0\) 消掉。
全列池 \(e\le6n-2\) 给 \(\deg(uq_e)\le5n-1\)。
Bernoulli展开 \(B_k(a/7)=\sum_{\ell=0}^k\binom k\ell B_\ell\left(\frac a7\right)^{k-\ell}\)
的分母由 \(7^k d_{5n}\) 清整；此处右端 \(B_\ell\) 指Bernoulli数，
幂只作用于 \(a/7\)。
D2的头分母由 \(d_{35n}^2\) 清整，因此一个明确完整safe模型是
\[
 \boxed{(7^{5n+1}S_nd_{35n}^2)^hQ_{\chi,n}(T)\in\mathbf Z[T].} \tag{D7}
\]
它包含全部系数、行列、prime powers；绝非primitive净费。

固定7不能被并入 \(o(n^2)\) 小素数误差。字符头中的7倍数项本来为0，
故这些头在7整；危险来自D3的degree-dependent Bernoulli移位。
对 \(n\ge3,\ e=i+j\)，更精确地
\[
 g_7\big(S_n[V_{\chi,T}(u^eR_n)]\big)
 \ge\min(0,n-e-3).
\]
所以同时把第i行、第i列乘 \(7^i\) 确实使完整 \(S_nM_\chi\) 在7整。
但det多乘 \(7^{h(h-1)}\)，这个leading指数必须与arch大小及
\(S_n^h/F_n\) 一起付；不能把basis gauge称作免费除掉conductor。
这仍不是新的净预算证书。

还有比fixed7更先要审的新导子窗口。对 \(p>5n,\ p\ne7\)，
全部残数、商部及 \(S_n^h/F_n\) 在p整且归一化为单位，而
\[
 p^2H_{7j,\chi}^{(2)}
 \equiv\chi(p)\sum_{m\le\lfloor7j/p\rfloor}\chi(m)m^{-2}\pmod p.
\]
特别在 \(35n/2<p<35n\)，只剩m=1。令
\(J=\lceil p/7\rceil,\ 0<k=5n-J+1\le h\)（n≥2时k<h），完整矩阵为
\[
 M_\chi=W-\chi(p)p^{-2}\sum_{j=J}^{5n}j\lambda_jv_jv_j^t,
 \quad W\in M_h(\mathbf Z_p[T]),\quad v_j=((-j)^i)_{i<h}. \tag{D8}
\]
节点模p不同、每个 \(j\lambda_j\) 为单位。h×k Vandermonde满列秩，
转置满行秩，故 \(p^2M_\chi\bmod p\) 的rank精确k，前k阶minor单位。
完整det可至多用k个 \(p^{-2}\) atoms，全部系数估值至少−2k，因此
\[
 v_p(d_{\chi,n})\le2k,\qquad
 \int_{35/2}^{35}2(5-x/7)\,dx=175/4. \tag{D9}
\]
这是合法粗upper的贡献，不能作为actual费用lower；首层k阶minor
非零也不决定完整h阶det。它说明降低最高头阶数，同时把素数支持
扩大到35n，不能只算阶数“2”的收益。
本轮另实际FULL核Root新载体稿R1–R12；D8–D9与它的同对象归一化一致。

## 6. 四接口与下次投入决定

| 接口 | 本候选状态 |
|---|---|
| 真实数值周期出口/完整projection | D1–D3已付；全球既有结果范围仍须有限核定 |
| 完整整模型 | D7已付；fixed7与其余all-prime primitive净费未付 |
| 每个固定有理关系点的无界非零 | 未付；241K5证书不移植，正密度也不替代它 |
| 同对象能量 | D6的uniform leading转移已付；原−6完整认证未付 |

只批准一次先行检验：对固定D1、原 \(R_n\) 和完整 \(3n\) 池，
支付整个新增 \(5n<p\le35n\) 导子窗口及fixed7 Gauss/gauge，
再与其余窗口和同一Heine度量合成净预算接口。
若这一关只有common LCD或局部小节省，没有能改变strict比较的宏观机制，
暂停这个候选；不以“最高头只有2”自动续开六轮。
只有实际预算方向可达，才投入它自己的增长prime无限非零。
新的数值定理仍为0；原K5资产保留为结构工具，停止的是默认局部优化资源。

实际FULL/选读、primary身份及数学0账见
[本人scope](../literature/global_review_sources_round244_20261009/alternative_reading_scope.md)。

