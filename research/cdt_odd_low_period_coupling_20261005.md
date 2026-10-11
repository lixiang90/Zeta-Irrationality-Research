# χ₅ 奇权的低周期耦合：真实 level 10 投影、对数接口与共轭叶

日期：2026-10-05。本稿从原始文献和实际 Fourier 级数重新推导，旧稿冻结。

本轮恢复并补全三个真实接口：纯 \(L(3,\chi_5)\) 的 Fricke 周期；与 \(\log\phi\) 的低权耦合；以及共轭模型在有理 cusp 处的完整 \(\pi^3\) 周期。它们给出实际正则叶和完整安全整数模型，但没有闭合新的数值无理性或线性无关性判据。另一分支新发现的 level 20 构造已通过本分支独立的矩阵/临界值审阅，它确实同时修复两种嵌入的 Fricke 正则性；所余问题转移到真实覆盖、函数秩和完整算术成本。

## 1. 原始文献的准确归一化

原件 [Beukers, *Irrationality proofs using modular forms*](E:/kimi-build/zeta5/literature/beukers1987_modular_irrationality.pdf)，Astérisque 147–148 (1987)，271–283，PDF 第 11 页、印刷第 280 页的 Theorem 4 已逐页渲染并视觉核查。该文证明
\[
8\zeta(3)-5\sqrt5L(3,\chi_5)\notin\mathbb Q(\sqrt5).
\]
这是既有定理；不能重述为本项目的新结论，也不单独证明 \(L(3,\chi_5)\) 无理。

令 \(\chi=\chi_5\)，即剩余类 \(1,4\) 取 \(1\)，\(2,3\) 取 \(-1\)，\(0\) 取 \(0\)，并令 \(q=e^{2\pi i\tau}\)、\(\theta_q=q\,d/dq\)。采用原文归一化：
\[
\begin{aligned}
\mathcal E_4(\tau)&=1+\sum_{d\ge1}\frac{\chi(d)d^3q^d}{1-q^d},&
\mathcal F_4(\tau)&=\sum_{m,n\ge1}\chi(n)m^3q^{mn},\\
\mathcal E_2(\tau)&=-\frac15+\sum_{d\ge1}\frac{\chi(d)dq^d}{1-q^d},&
\mathcal F_2(\tau)&=\sum_{m,n\ge1}\chi(n)m q^{mn}.
\end{aligned} \tag{1}
\]
特别是 \(\mathcal E_2\) 的常数为 \(-1/5\)。广义 Bernoulli 公式
\[
B_{k,\chi}=5^{k-1}\sum_{a=1}^4\chi(a)B_k(a/5),\qquad
L(1-k,\chi)=-B_{k,\chi}/k
\]
独立给出 \(L(-1,\chi)=-2/5\)、\(L(-3,\chi)=2\)，所以两常数分别是 \(L(-1,\chi)/2=-1/5\)、\(L(-3,\chi)/2=1\)。

这些是 weight \(k\)、Nebentypus \(\chi\) 的 Hecke Eisenstein 级数。实际 Gauss 和取正实支 \(\sum_{a=1}^4\chi(a)e^{2\pi ia/5}=\sqrt5\)。标准 lattice/Poisson 变换在本归一化下为
\[
\mathcal E_k(-1/(5\tau))
 =5^{k-1}\sqrt5\,\tau^k\mathcal F_k(\tau),\qquad
\mathcal F_k(-1/(5\tau))
 =\sqrt5\,\tau^k\mathcal E_k(\tau),\quad k=2,4. \tag{2}
\]
原文 p280 的 \(\mathcal E_4-5\sqrt5\mathcal F_4\) 和
\(\mathcal E_2-\sqrt5\mathcal F_2\) 恰是各自的负 Fricke 特征向量。式 (2) 的平方为 \(5^k\tau^{2k}\) 所需因子；不是把 \(\sqrt5\) 形式地视为有理系数。

## 2. level 10 的纯 \(L(3,\chi)\) source 与完整周期

记 \(a=5\sqrt5/4\)、\(W=W_{10}:\tau\mapsto-1/(10\tau)\)，定义
\[
\begin{aligned}
V_-(\tau)&=\mathcal E_4(\tau)-\mathcal E_4(2\tau)
 +a\mathcal F_4(\tau)-16a\mathcal F_4(2\tau),\\
V_+(\tau)&=\mathcal E_4(\tau)-\mathcal E_4(2\tau)
 -a\mathcal F_4(\tau)+16a\mathcal F_4(2\tau).
\end{aligned} \tag{3}
\]
它们是 \(K=\mathbb Q(\sqrt5)\) 中的系数共轭，均在 \(\infty\) 无常数。式 (2) 逐项给出
\[
V_-(W\tau)=-100\tau^4V_-(\tau),\qquad
V_+(W\tau)=+100\tau^4V_+(\tau). \tag{4}
\]
所以两者也在 cusp \(0\) 消失；Hecke Mellin 积分在这条配对路径两端收敛。

令 \(f_\pm=\theta_q^{-3}V_\pm\)，在 \(\infty\) 取零初值。其 Dirichlet 级数为
\[
L(V_\pm,s)
 =(1-2^{-s})\zeta(s)L(s-3,\chi)
 \mathord{\pm}a(1-16\,2^{-s})\zeta(s-3)L(s,\chi), \tag{5}
\]
其中 \(V_-\) 对应上面的加号、\(V_+\) 对应减号；下标指 Fricke 特征符号。

记
\[
\Theta=\frac{5\sqrt5}{8}L(3,\chi).
\]
由 \(\Lambda_\chi(s)=(5/\pi)^{s/2}\Gamma(s/2)L(s,\chi)
=\Lambda_\chi(1-s)\)，
\[
L'(-2,\chi)=-\frac{25\sqrt5}{4\pi^2}L(3,\chi),\qquad
L(2,\chi)=\frac{4\pi^2}{25\sqrt5}. \tag{6}
\]
必须计算 \(s=1\) 处 \(\zeta(s)L(s-3,\chi)\) 的有限极限，不得把它误写成 \(0\)：
\[
\begin{array}{c|ccc}
&L(V,1)&L(V,2)&L(V,3)\\ \hline
V_-&-5\Theta/\pi^2&0&\Theta\\
V_+&-5\Theta/\pi^2&-\pi^2/10&-\Theta .
\end{array} \tag{7}
\]

Hecke 的实际 Eichler 积分恒等式（原文 Proposition 1.2；可直接对两端 Mellin 路径应用）由全部临界值给出
\[
\boxed{f_-(\tau)+10\tau^2f_-(W\tau)
 =\Theta(1+10\tau^2)} \tag{8}
\]
和
\[
\boxed{f_+(\tau)-10\tau^2f_+(W\tau)
 =-\Theta(1-10\tau^2)-\frac{i\pi^3}{5}\tau.} \tag{9}
\]
式 (9) 的中间项是实际周期，不能在 \(K\) 中共轭式 (8) 来删去。

令 \(E_2\) 为常数 \(1\)、系数 \(-24\sigma_1(n)\) 的经典级数，并取
\[
A(\tau)=E_2(\tau)-10E_2(10\tau).
\]
准模异常项相消，\(A(W\tau)=-10\tau^2 A(\tau)\)；\(A\) 是 trivial character 的 weight 2 模形式，常数 \(-9\)。于是
\[
H_-=A(f_--\Theta),\qquad H_-(W\tau)=H_-(\tau) \tag{10}
\]
是最近 Fricke 固定点处的真实正则叶。

若假设 \(L(3,\chi)\in\mathbb Q\)，\(H_-\) 的系数在 \(K\)；其系数共轭为
\(H_+=A(f_++\Theta)\)。但
\[
H_+(\tau)+H_+(W\tau)=-\frac{i\pi^3}{5}\tau A(\tau), \tag{11}
\]
并非同一个 Fricke 正则叶。可用 \((i\pi^3/10)\tau\) 修正 \(f_++\Theta\) 使其满足齐次反演，但这引入 \(\pi^3\log q\)，未给出 \(K[[q]]\) 的有理算术芽。仅完成一个嵌入的解析改善不足以对两个嵌入同时使用数域算术判据。

## 3. 低权 source 的真实 \(\log\phi\) 周期与整数模型

取 \(\phi=(1+\sqrt5)/2\)、\(b=\sqrt5/2\)，定义
\[
B_-=\mathcal E_2-\mathcal E_2(2\tau)
 +b\mathcal F_2-4b\mathcal F_2(2\tau),\qquad
B_+=\operatorname{conj}_K B_- . \tag{12}
\]
两者在 \(\infty\) 无常数，\(B_-(W\tau)=-10\tau^2B_-(\tau)\)、
\(B_+(W\tau)=+10\tau^2B_+(\tau)\)。令 \(g_\pm=\theta_q^{-1}B_\pm\) 在 \(\infty\) 取零初值。其 Dirichlet 级数是
\[
(1-2^{-s})\zeta(s)L(s-1,\chi)
\mathord{\pm}b(1-4\,2^{-s})\zeta(s-1)L(s,\chi). \tag{13}
\]
利用
\[
L(1,\chi)=\frac2{\sqrt5}\log\phi,\qquad
L'(0,\chi)=\frac{\sqrt5}{2}L(1,\chi)=\log\phi,
\]
两个有限极限分别给出 \(L(B_-,1)=\log\phi\)、\(L(B_+,1)=0\)。真实 period relation 因而为
\[
\boxed{g_-(\tau)+g_-(W\tau)=\log\phi,\qquad
g_+(\tau)-g_+(W\tau)=0.} \tag{14}
\]
这确实把困难的奇权 source 和已知的低权对数周期放到同一 Fricke 几何中。但 \(\log\phi\) 已知超越，不能把其实际周期不经处理视为有理背景常数。

算术上 \(4V_\pm\in\mathbb Z[\sqrt5][[q]]\)，
\(2B_\pm\in\mathbb Z[\sqrt5][[q]]\)。对完整前缀 \(0\le n\le N\)，
\[
4L_N^3 f_\pm\in\mathbb Z[\sqrt5][[q]]_{\le N},\qquad
2L_N g_\pm\in\mathbb Z[\sqrt5][[q]]_{\le N},
\quad L_N=\operatorname{lcm}(1,\ldots,N). \tag{15}
\]
乘以 \(A\in\mathbb Z[[q]]\) 保留此安全模型。若行含假设的 \(\Theta\)，还须乘其固定数域分母。本式覆盖全部前缀，不是只清末项；不声称它是最小分母或完整最佳 content。

## 4. 实际单位根边界式与有限 Bernoulli 求值

记
\[
G_\chi(x)=\sum_{n\ge1}\chi(n)x^n
=\frac{x(1-x^2)}{\Phi_5(x)},\quad
G_\chi(1/x)=-G_\chi(x).
\]
在 \(|q|<1\) 对绝对收敛双和重组，得到实际 identity
\[
\boxed{
f_\mp(q)=\sum_{\substack{m\ge1\\m\ {\rm odd}}}\frac{G_\chi(q^m)}{m^3}
\mathord{\pm}a\sum_{n\ge1}\frac{\chi(n)}{n^3}\frac{q^n}{1+q^n}.} \tag{16}
\]
这里 \(f_-\) 取加号，\(f_+\) 取减号。证明使用
\[
\frac{z}{1-z}-2\frac{z^2}{1-z^2}=\frac{z}{1+z},
\]
以及第三原函数对 oldform \(q\mapsto q^2\) 的因子 \(2^{-3}\)。

若 \(c\) 为奇数且 \(5\nmid c\)，\(\rho=e^{2\pi ia/c}\) 为 primitive \(c\) 次单位根，则 \(\rho^m\) 不命中 \(\Phi_5\) 的零点或 \(-1\)。对径向 \(q=r\rho\)，两有理核在所有 \(m,n,r\) 上有统一界：它们只沿有限条不碰其极点的径向射线变化。因此式 (16) 的两和由 \(\sum n^{-3}\) 支配，给出有限实际径向极限。逐项应用 reciprocal kernel：
\[
f_-(\rho)+f_-(\rho^{-1})=2\Theta,\qquad
f_+(\rho)+f_+(\rho^{-1})=-2\Theta. \tag{17}
\]
这不是从数值近似猜测的关系。

现在固定 \(a=-3,c=13\)。令
\[
D_n=-\frac15\sum_{k=0}^4 k\,\chi(n+13k),\qquad 1\le n\le13.
\]
它是 \(\sum_{d\equiv n\pmod{13},d\ge1}\chi(d)r^d\) 在 \(r\uparrow1\) 的精确 Abel 极限。均值零使分子一阶展开给出该式。有限 Fourier 展开为
\[
G_\chi(\rho^m)=\sum_{n=1}^{13}D_n\rho^{nm},
\]
且 \(D_{13}=0,D_{13-n}=-D_n\)。证书还独立核查此有理身份在 \(\Phi_{13}\) 商环中成立。

采用 \(B_3(x)=x^3-\tfrac32x^2+\tfrac12x\)、在小数部分取值，定义
\[
\begin{aligned}
E_g&=\sum_{n=1}^{13}D_n\left[B_3(\{-3n/13\})
 -\tfrac18B_3(\{-6n/13\})\right],\\
F_g&=\frac12\sum_{k=1}^{12}\sum_{u=1}^4
(-1)^{k+1}\chi(u)B_3(\{-3k/13+u/5\}).
\end{aligned} \tag{18}
\]
所有项均为有理数；完整有限计算给出
\[
E_g=-\frac{45}{338},\qquad F_g=\frac{18}{4225}. \tag{19}
\]
由真实 Fourier–Bernoulli identity
\[
\operatorname{Li}_3(e^{2\pi ix})-\operatorname{Li}_3(e^{-2\pi ix})
=\frac43i\pi^3B_3(\{x\}),
\]
第一和在此 cusp 等于 \(\tfrac23i\pi^3E_g\)。
又在 odd \(c\) 次单位根处
\[
\frac{z}{1+z}=\frac12+\frac12\sum_{k=1}^{c-1}(-1)^{k+1}z^k.
\]
将 \(\chi(n)=\frac1{\sqrt5}\sum_{u=1}^4\chi(u)e^{2\pi iun/5}\) 代入第二和并配对逆根，得到
\[
\sum_{n\ge1}\frac{\chi(n)}{n^3}\frac{\rho^n}{1+\rho^n}
=\frac12L(3,\chi)+\frac{2i\pi^3}{3\sqrt5}F_g.
\]
所以
\[
\boxed{\lambda:=f_+(-3/13+i0)
=-\Theta+i\pi^3\left(\tfrac23E_g-\tfrac56F_g\right)
=-\Theta-\frac{6i\pi^3}{65}.} \tag{20}
\]

## 5. 这个边界值确实对应另一条正则叶

取
\[
\gamma=\begin{pmatrix}13&3\\30&7\end{pmatrix}\in\Gamma_0(10),
\quad\chi(7)=-1,\quad
\sigma=W_{10}\gamma=\begin{pmatrix}-30&-7\\130&30\end{pmatrix}.
\]
\(\sigma\) 的行列式为 \(10\)、迹为 \(0\)、平方为 \(-10I\)，并且
\[
h=-3/13,\qquad
\sigma(h+z)=h-\frac1{1690z}. \tag{21}
\]
由 \(V_+\) 的 Nebentypus 以及正 Fricke 特征值，
\[
V_+(\sigma\tau)=-100(13\tau+3)^4V_+(\tau).
\]
平移到 \(z=\tau-h\) 后，\(V_+(h+z)\) 因而具有负 weight 4、effective level \(1690\) 的真实 Fricke 关系，且在这条 Mellin 路径两端消失。对该函数直接应用 Hecke 关系：
\[
f_+(\tau)+1690(\tau+3/13)^2f_+(\sigma\tau)
=\lambda\left[1+1690(\tau+3/13)^2\right]. \tag{22}
\]
\(A\) 的 trivial character 与负 Fricke 特征值同样给出
\[
A(\sigma\tau)=-1690(\tau+3/13)^2 A(\tau).
\]
因此
\[
A(f_+-\lambda)
\]
是 \(\sigma\) 的真实 invariant 正则叶，其固定点为
\(-3/13+i\sqrt{10}/130\)。式 (20) 中的 \(\pi^3\) 项不能省略。
即使假设 \(L(3,\chi)\in\mathbb Q\)，这个叶的常数仍不属于 \(K\)；从它直接抽取 \(K\)-算术 holonomy 函数仍缺一个真实周期投影。

## 6. Ramanujan trace 是完整算术接口，但不是正则投影

固定 primitive 13 次根 \(\rho\)，
\[
\mathcal T_\pm(q)=\sum_{a=1}^{12}f_\pm(\rho^a q)
=\sum_{n\ge1}c_{13}(n)\,[q^n]f_\pm\ q^n,\qquad
c_{13}(n)=\begin{cases}12,&13\mid n,\\-1,&13\nmid n.\end{cases} \tag{23}
\]
这是实际函数 trace，其全部系数仍在 \(K\)，安全完整分母仍为 \(4L_N^3\)。所有端点都由第 4 节的支配收敛控制，式 (17) 给出
\[
\lim_{q\uparrow1}\mathcal T_+(q)=-12\Theta,\qquad
\lim_{q\uparrow1}\mathcal T_-(q)=12\Theta. \tag{24}
\]
它的价值是提供纯最高奇权周期且使用整数 Ramanujan 权的接口。

但式 (24) 只是一条端点关系。各项来自不同 cusp 与不同 elliptic involution；不能把其相加自动称为跨同一最近分支的正则函数。尤其 \(q\) 中的 Lambert/Eisenstein 芽本身并未因这条 trace 自动成为有理系数微分方程的 holonomic 函数。需要建立一个实际模曲线坐标、共同延拓区域及完整函数系统，再算秩与分母。

也不能混淆两种 trace：对系数域 \(K/\mathbb Q\) 取 trace 会给
\(f_-+f_+=2\sum_{m\ {\rm odd}}G_\chi(q^m)/m^3\)，从而删掉 \(\Theta\) 的触发坐标；式 (23) 是单位根旋转 trace，保留了端点 \(\Theta\)，但它的共同正则性仍待证明。

## 7. 新的 level 20 两嵌入修复已独立通过

另一分支的完整证明见 [两嵌入投影报告](cdt_odd_conjugate_projection_20261005.md)。本分支独立审阅的实际公式是
\[
\begin{aligned}
V_{-,20}&=\mathcal E_4-5\mathcal E_4(2\tau)+4\mathcal E_4(4\tau)
 -a\bigl(\mathcal F_4-20\mathcal F_4(2\tau)+64\mathcal F_4(4\tau)\bigr),\\
A_{-,20}&=\mathcal E_2-4\sqrt5\mathcal F_2(4\tau),
\end{aligned}
\]
正下标形式为 \(K\)-系数共轭。两 weight 4 eigenvalues 为
\(\mp400\tau^4\)，两 weight 2 eigenvalues 为
\(\mp20\tau^2\)。两个 oldform 多项式
\[
P_E(s)=(1-2^{-s})(1-4\,2^{-s}),\quad
P_F(s)=(1-16\,2^{-s})(1-4\,2^{-s})
\]
都在 \(s=2\) 为零。记
\[
\Theta_{20}=-\frac{5\sqrt5}{16}L(3,\chi),
\]
则两 \(L(1)\) 均为 \(-10\Theta_{20}/\pi^2\)，两 \(L(3)\) 为
\(\pm\Theta_{20}\)。因此实际 period relation 没有 level 10 的 \(\pi^3\tau\) 项，而且
\[
A_{-,20}(f_{-,20}-\Theta_{20}),\qquad
A_{+,20}(f_{+,20}+\Theta_{20})
\]
同时在 \(W_{20}\) 下 invariant。若假设 \(L(3,\chi)\in\mathbb Q\)，这两芽确实是 \(K[[q]]\) 中彼此共轭的实际正则叶。此进展解决了本稿 §2 的两嵌入匹配缺口；它仍不代替严格 CDT 不等式。

假设 \(L(3,\chi)\in K\) 比假设在 \(\mathbb Q\) 中更弱。前一假设的域共轭值未必等于原实际 \(L\) 值，不能凭上述符号自动升级为 \(L(3,\chi)\notin K\) 的结论。

根分支给出的同 level 10 真正 \(\zeta(3)\) 校准 source
\[
7E_4(\tau)-132E_4(2\tau)+825E_4(5\tau)-700E_4(10\tau)
\]
也已独立核查：常数零、负 Fricke eigenvalue、临界 \(L(2)=0\)、
\(L(3)=432\zeta(3)\)、\(L(1)=-2160\zeta(3)/\pi^2\)。它是联合真实周期路线的对照，不产生新的 \(\zeta(3)\) 无理性结论。

## 8. 证书和审阅边界

[精确脚本](cdt_odd_low_period_coupling_20261005_verify.py) 与
[JSON](cdt_odd_low_period_coupling_20261005_verify.json) 包含 228 项固定精确检查，已执行通过：广义 Bernoulli 常数；两个 level 10 Fricke 矩阵与临界值；低权对数周期常数；实际 \(\sigma\) 的平移反演；全部有限 Bernoulli 和；前 36 个实际核系数和全部安全整数前缀；13 次 Ramanujan trace；以及 §7 所列 level 20 和 \(\zeta(3)\) source 的独立固定代数检查。

全尺度整数化来自 §3 的逐项证明；实际周期来自 Hecke/Mellin 和 §4 的支配收敛及 Bernoulli identity，不把有限检查升级为这些解析命题的独立形式化证明。尚未证明最优 content、实际共同覆盖或严格 holonomy 矛盾，亦未进行 Lean 验证。

限定的独立交叉审阅：conjugate_projection 分支重推 §4–5 的完整数学证明，包括 \(D_n\) 的反对称、两个 Fourier–Bernoulli 因子、全部 \(E_g,F_g\) 有理和、\(\lambda\)、\(\sigma\) 的矩阵/平移反演及真实配对 Mellin 周期，均通过。该审阅不覆盖本稿其余小节的全部证明、脚本实现或未来 CDT 不等式。本分支则独立重推另稿 §1–6 的 level 20 数学主体，包括全部 cusp 表与素数 packet；没有冒充执行另稿脚本。

当前下一步应优先在 level 20 的两个真实正则叶上建立共同模曲线坐标、数域全部嵌入的解析覆盖、真实函数秩与完整整数模型。level 10 的单位根 trace 则保留为另一条有明确最高周期输入、但尚未完成共同正则性的接口。
