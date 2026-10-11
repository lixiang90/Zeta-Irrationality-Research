# CDT 的实际成功机制与一个闭合的五项 dilogarithm 目标族

日期：2026-10-05。本稿只新增本文件及其证书，不改冻结的全局 holonomy、
周期桥梁、K2 或对数矩记录。

本轮有一个完整的数值结论：对每个整数 \(N\ge10^6\)，下面显式列出的
五个有理点 dilogarithm 的组合 \(\Phi_N\) 无理。证明是一个真实函数恒等式
加 CDT 已证 Theorem C 的直接推论。这里不声称全球首次发现，也不声称这五个
单独的 dilogarithm 全部无理。更主要的研究交付，是把原文成功机制接成可审计链：
**数值关系 → 有理系数过收敛 Hadamard 芽 → 完整分母阶梯 → 实际独立秩 17 →
严格 holonomy 矛盾**。同一链不能仅靠动机层形式投影代替。

## 1. 版本与采用的已证输入

全文按[库内固定 CDT PDF](../literature/cdt2024_l2_chi_minus3.pdf)
arXiv:2408.15403v2，2024-09-16，218 页，引用**印刷页码**；本版印刷页码
恰与 PDF 的从 1 开始页号一致。作者站的 220 页新版不在本稿中混用编号。
[原始固定版本元数据](https://arxiv.org/abs/2408.15403v2)。

采用的数值定理是 Theorem C（页 4–5），即 Theorem 14.0.1（页 174）：
对整数 \(m,n\notin\{-1,0\}\)，若
\[
|m/n-1|<10^{-6},
\tag{1}
\]
则 \(\log(1+1/m)\log(1+1/n)\) 无理。\(m\ne n\) 时，
\[
1,\quad\log(1+1/m),\quad\log(1+1/n),
\quad\log(1+1/m)\log(1+1/n)
\tag{2}
\]
在 \(\mathbb Q\) 上线性无关。以下为清楚核对实分支，专取正 \(m,n\)。
原定理更大参数范围不因这个选择而被否定。

采用的函数与分析输入分别是：§14.1、Proposition 14.1.11 的过收敛与
对称化；Lemma 14.3.1 的 17 个**实际函数**独立性；Corollary 9.0.19 的
分支拉回；Theorem 7.0.1 及 Appendix A.6 的严格解析界。它们是原文的
已证结果，不是假设，也不由本稿的有限系数证书重证。

## 2. 一个明确的新项目目标：五项有理点 Li2 的组合

对 \(m,n\ge2\)，定义
\[
\begin{split}
\Phi_{m,n}={}&
\operatorname{Li}_2\!\left(\frac{n+1}{n(m+1)}\right)
+\operatorname{Li}_2\!\left(\frac{m+1}{m(n+1)}\right)
-\operatorname{Li}_2\!\left(\frac1{mn}\right)\\
&-\operatorname{Li}_2\!\left(\frac1{m+1}\right)
-\operatorname{Li}_2\!\left(\frac1{n+1}\right).
\end{split}
\tag{3}
\]
所有参数严格位于 \((0,1)\)，取实主支。我们直接证明
\[
\boxed{\Phi_{m,n}=\log(1+1/m)\log(1+1/n).}
\tag{4}
\]
因此当 (1) 成立且 \(m\ne n\) 时，
\(1,\log(1+1/m),\log(1+1/n),\Phi_{m,n}\) 线性无关。
特别令 \(m=N,n=N+1\)：
\[
\begin{split}
\Phi_N={}&\operatorname{Li}_2\!\left(\frac{N+2}{(N+1)^2}\right)
+\operatorname{Li}_2\!\left(\frac{N+1}{N(N+2)}\right)
-\operatorname{Li}_2\!\left(\frac1{N(N+1)}\right)\\
&-\operatorname{Li}_2\!\left(\frac1{N+1}\right)
-\operatorname{Li}_2\!\left(\frac1{N+2}\right)\notin\mathbb Q
\qquad(N\ge10^6).
\end{split}
\tag{5}
\]
阈值是严格的：\(|m/n-1|=1/(N+1)<10^{-6}\)。
\(N=999999\) 正好等于边界，本文不从 CDT 推出它的结论。
更一般，固定非零整数 \(r\)，取 \(m=n+r\) 和 \(n>10^6|r|\)，
也得到全部 \(\Phi_{n+r,n}\) 无理。这些都是**原定理的直接推论**。

### 2.1 真实五项恒等式的证明

对 \(0<X,Y<1\)，置
\[
D=1-XY,\quad f=\frac{X(1-Y)}D,\quad g=\frac{Y(1-X)}D,
\quad A=\frac{1-X}D,\quad B=\frac{1-Y}D.
\]
所有上述函数为正，且 \(X,Y,XY,f,g\in(0,1)\)。记
\[
E(X,Y)=\operatorname{Li}_2(X)+\operatorname{Li}_2(Y)
-\operatorname{Li}_2(XY)-\operatorname{Li}_2(f)-\operatorname{Li}_2(g)
-\log A\log B.
\tag{6}
\]
由实际微分式
\(d\operatorname{Li}_2(z)=-\log(1-z)\,dz/z\)，并使用
\(1-f=A,\ 1-g=B\)，分别计算得到 \(\partial_XE=\partial_YE=0\)。
这里所有 log 拆分均在实正数上进行，没有模 \(2\pi i\) 的分支差。
令 \(Y\downarrow0\)，有 \(f\to X,g\to0,A\to1-X,B\to1\)，
所以 \(E\to0\)，常数为零。这证明了 (6) 恒等为零。
证书将 \(\log X,\log Y,\log(1-X),\log(1-Y),\log(1-XY)\) 作为
独立形式变量，准确检查两个偏导数的所有有理系数为零。
Li2 的实际微分与主支可对照 [NIST DLMF 25.12.2](https://dlmf.nist.gov/25.12.E2)。

再取
\[
X=\frac{n+1}{n(m+1)},\qquad Y=\frac{m+1}{m(n+1)}.
\]
直接代数化简给
\[
XY=\frac1{mn},\quad f=\frac1{m+1},\quad g=\frac1{n+1},
\quad A=\frac m{m+1},\quad B=\frac n{n+1}.
\]
代入 (6)，两个负 log 的乘积恰为 (4)。没有额外 \(\pi^2\)、
\(\pi\log\) 或未知周期常数，故这是实际数值关系，而不是形式周期删除。

还有一个独立的真实积分识别：
\[
\Phi_{m,n}=\int_0^1\!\int_0^1
\frac{du\,dv}{(m+u)(n+v)}.
\tag{7}
\]
这说明目标是两个相对 logarithm 周期的 cup product。
其完整积分模型和五项参数函数的独立微分秩由根任务另稿处理；
不能把 (7) 自动标成非零绝对 Milnor K2 类或椭圆 regulator。
本轮早先的 K2 记录已说明：符号的有理退化不排除开放路径的非零相对周期。

## 3. CDT 如何把一个数值关系变成有理系数过收敛芽

取 \(a=2m+1,b=2n+1\)，以及
\[
Q_a(x)=1-2ax+x^2,\quad
A_a(x)=Q_a(x)^{-1/2},\quad
H_a(x)=A_a(x)\int_0^xA_a(t)\,dt.
\tag{8}
\]
在 \(x=0\) 取平方根常数项 1。它们是真实函数，满足
\[
Q_a A'_a+(x-a)A_a=0,
\qquad Q_a H'_a+(x-a)H_a=1,
\qquad H_a(0)=0.
\tag{9}
\]
若 \(A_a=\sum u_j(a)x^j,H_a=\sum v_j(a)x^j\)，从 (8) 有
\[
u_j(a)=\sum_{k=0}^j\binom jk\binom{j+k}k m^k\in\mathbb Z,
\qquad
v_j(a)=\sum_{t=1}^j\frac{u_{j-t}(a)u_{t-1}(a)}t.
\tag{10}
\]
故 \(L_jv_j(a)\in\mathbb Z\)，\(L_j=\operatorname{lcm}(1,\ldots,j)\)。
原函数的完整系数分母已由具体卷积式闭合；不靠固定几何坏素数推定。

令 \(\eta_a=\tfrac12\log((a+1)/(a-1))=\tfrac12\log(1+1/m)\)。
原文证明 \(H_a-\eta_aA_a\) 在
\(\alpha_a=a-\sqrt{a^2-1}\) 过收敛：积分从 \(\alpha_a\) 开始后与
\(A_a\) 的两个局部 \(-1\) monodromy 相乘，得到正则延拓。
这里抵消的是实际局部分支，其系数是实际 \(\eta_a\)；不是先令某个形式周期为零。

记 Hadamard 乘积 \((\sum c_jx^j)\star(\sum d_jx^j)=\sum c_jd_jx^j\)，
定义
\[
P_a=(H_a-\eta_aA_a)\star A_b,\quad
P_b=A_a\star(H_b-\eta_bA_b),
\quad P_{ab}=H_a\star H_b-\eta_a\eta_b(A_a\star A_b).
\tag{11}
\]
三者在最小乘积奇点 \(\alpha_a\alpha_b\) 过收敛。
最后一项可以展开成两个含一个过收敛因子的 Hadamard 乘积与一个
含两个过收敛因子的乘积；原文 §14.1 给出同一分支结论。

若有整数数值关系
\[
r_0+r_a\eta_a+r_b\eta_b+r_{ab}\eta_a\eta_b=0,
\tag{12}
\]
则
\[
\begin{split}
P&=r_aP_a+r_bP_b+r_{ab}P_{ab}\\
&=r_0(A_a\star A_b)+r_a(H_a\star A_b)
+r_b(A_a\star H_b)+r_{ab}(H_a\star H_b)\in\mathbb Q[[x]].
\end{split}
\tag{13}
\]
其系数由 \(L_j^2\) 完全整数化。所有未知数值周期在这一**具体关系**下
恰抵消；没有假定周期映射单射，也没有假定它们具有可任意作用的 Galois 共轭。
若只猜测乘积有理，便是 (12) 中 \(r_a=r_b=0\) 的特例。

### 3.1 真实 Hadamard 微分方程

令
\[
q_4(x)=1-4abx+(-2+4a^2+4b^2)x^2-4abx^3+x^4,
\]
定义 \(M=p_2\partial_x^2+p_1\partial_x+p_0\)，其中
\[
\begin{split}
p_2={}&(x-1)x(1+x)q_4,\\
p_1={}&-1+8abx+(5-12a^2-12b^2)x^2+16abx^3\\
&+(-7+4a^2+4b^2)x^4-8abx^5+3x^6,\\
p_0={}&ab+(1-3a^2-3b^2)x+8abx^2-(2+a^2+b^2)x^3-abx^4+x^5.
\end{split}
\tag{14}
\]
这就是固定 v2 (14.1.2)，满足
\[
M(A_a\star A_b)=0,
\]
\[
M(H_a\star A_b)=-b+3ax-3bx^2+ax^3,
\quad M(A_a\star H_b)=-a+3bx-3ax^2+bx^3,
\]
\[
M(H_a\star H_b)=-1+2x^2-x^4.
\tag{15}
\]
故 (13) 具有有理系数非齐次方程，且先验 holonomic。
\(x=\pm1\) 在 \(a\ne\pm b\) 时只是表观奇点；真正有限非零奇点为
\((a\pm\sqrt{a^2-1})(b\pm\sqrt{b^2-1})\)。原点与无穷远也须保留。

本稿核对定义时修正固定 v2 的两个小显示错误，未扩大为对主定理的质疑：
页 175 的 \(H\) 显示级数按 (8)–(9) 应为
\(x+3ax^2/2+(15a^2-4)x^3/6+\cdots\)；
页 178 的 (14.1.7)–(14.1.8) 若按前式右侧 \(r_0\) 的约定，后一式
的 \(A_a\star A_b\) 系数应取 \(-r_0\)。本文统一采用 (12)，使 (13) 的正号无歧义。
有限证书同时核 (9)、(10)、(14)、(15)，不复制错误的显示项。

## 4. 对称化是实际有理下降；分母翻倍与新增积分均要付费

置
\[
w(x)=\frac{x}{x-1},\qquad y=x+w(x)=xw(x)=\frac{x^2}{x-1},
\quad G(y)=P(x)+P(w(x)).
\tag{16}
\]
这是二次覆盖的真实 trace。令 \(S_k=x^k+w(x)^k\)，则
\[
S_0=2,\quad S_1=y,\quad S_k=yS_{k-1}-yS_{k-2}\in\mathbb Z[y].
\tag{17}
\]
\(S_k\) 的最小非零次数为 \(\lceil k/2\rceil\)。所以 \(G\) 的第 \(j\)
系数只使用 \(P\) 的 \(k\le2j\) 系数，且组合整数；
\(L_{2j}^2[y^j]G\in\mathbb Z\)。这是全部素数的真实成本，
不是仅验证少数模 \(p\) 系数。固定阶求导只把安全指标移到
\(L_{2j+6}^2\)；原文 Remark 6.0.12 允许固定指标偏移，以严格余量和
\(b\mapsto b+\epsilon\) 后的连续极限处理。

原文 pushforward 得四阶 \(\mathcal L\)，有
\(\mathcal L(G)\in\mathbb Q[y]\)，其真正奇点位于
\(0,4,\pi((a\pm\sqrt{a^2-1})(b\pm\sqrt{b^2-1})),\infty\)，
\(y=4\) 是阶 2 的局部 monodromy。四阶是方程数据，不等于下述评估模块秩。

取原文的七个 pure 函数 \(B_1,\ldots,B_7\)（§10），再加入
\[
G,G',G'',G''',
\quad\int yG\,dy,\quad\int G\,dy,
\quad\int\frac{G-G(0)}y\,dy,
\tag{18}
\]
以及从 \(G\) 减去次数 1、2、3 的 Taylor 多项式后，分别除以
\(y^2,y^3,y^4\) 的三个积分。全部原函数取在 0 处为零。
这些积分的第 \(j\) 系数含 \(1/j\)，安全型为
\(jL_{2j+6}^2\)；不能把因子 \(j\) 免费删除。

Lemma 14.3.1（页 184–186）证明此 **17 个实际函数** 在
\(\mathbb C(y)\) 上线性无关，适用条件为整数 \(a,b\notin\{-1,0,1\}\)
且 \(0<|a/b-1|<10^{-3}\)。正参数 (1)、\(m\ne n\) 蕴含这些条件。
原文利用 monodromy 将不可能的新函数约化到齐次解，随后根据所有真正与表观
奇点的局部指数，把可能的有理关系化为一个 determinant 非零的有限线性系统。
这既不是数形式符号，也不是给同一个四阶方程不断求导，凭空得到 17 阶秩。
六个积分和七个不同 pure 辅助函数是实际新增输入。

完整有序账本如下。固定偏移统一记作 \(+6\)，对 pure 函数可去掉；
固定整体有理倍也不会改变阶梯指数。

| 位置 | 实际函数 | 主分母型 | 额外积分指数 \(e_i\) |
|---|---|---|---:|
|1|\(B_1=1\)|1|0|
|2|\(B_2\)|\(L_{2j}\)|0|
|3|\(B_3\)|\(L_{2j}\)|1|
|4–5|\(B_4,B_5\)|\(L_{2j}^2\)|0|
|6–9|\(G,G',G'',G'''\)|\(L_{2j+6}^2\)|0|
|10–11|\(B_6,B_7\)|\(L_{2j}^2\)|1|
|12–17|六个 (18) 型积分|\(L_{2j+6}^2\)|1|

主阶梯矩阵两列依次为
\((0,0),(2,0),(2,0)\)，随后十四个 \((2,2)\)；两列都非降。
积分向量为 \(e=(0,0,1;0,0,0,0,0,0;1,1,1,1,1,1,1,1)\)，
共有九个 1。原文 (14.5.2)–(14.5.4) 的精确成本是
\[
\tau^{\flat}=\frac{1136}{289},\qquad
\tau^{\sharp}=\frac{78419}{242760},\qquad
\boxed{\tau=\frac{1032659}{242760}.}
\tag{19}
\]
\(\tau^{\sharp}\) 的最小化来自原文；本稿证书检查账本及分数相加，
不把一次代入当作其全局最小化的替代证明。

## 5. 解析叶与严格余量：为什么这次会成功

近参数条件使一个乘积奇点在 0 附近，两个在 1 附近，一个很大。
过收敛的 \(P\) 已消掉最小奇点的坏分支，但没有删除其他奇点。
通过 (16) 与原文 §14.4，\(G\) 的额外真正奇点全部落在
\[
|y|<10^{-24}/16\quad\text{或}\quad|y|>10^6.
\tag{20}
\]
小奇点使用它在原点的过收敛叶处理。所有新的奇点与 \(0,4,\infty\)
的本来几何必须一起检查，不能只用“半径大”一句代替。

原文 Appendix A.6 选择 \(\varphi=h\circ\psi\)，其中 \(h\) 是
\(Y_0(2)\) 的 hauptmodul，\(|h'(0)|=256\)，
\(|\psi'(0)|=1287/2516\)。Corollary 9.0.19 的条件包括原点附近的
univalent leaf 包含全部需要抵消的小奇点原像，其他奇点被映射避开，
以及椭圆点 \(y=4\) 的阶 2 分支兼容。它实际保证各函数拉回为单位圆盘
上的亚纯函数；本文没有把多值函数未经单值化直接当成全盘函数。

Theorem 7.0.1 的先验 holonomic 版本适用：
有理系数、主阶梯列有序、完整 \(e\)、函数独立、亚纯拉回，且
\(\log|\varphi'(0)|>\tau\)。固定分母偏移按 Remark 6.0.12 处理。
它给出
\[
17\le\frac{J(\varphi)}{\log|\varphi'(0)|-\tau},\qquad
J(\varphi)=\iint_{\mathbb T^2}\log|\varphi(z)-\varphi(w)|\,d\mu(z)d\mu(w).
\tag{21}
\]
原文 Appendix A.6（页 206）证明 \(J(\varphi)<10\)。因此
\[
\boxed{\frac{10}{
\log(256\cdot1287/2516)-1032659/242760}
=16.1032097\ldots<17.}
\tag{22}
\]
分母严格为正，且比 \(10/17\) 大。Arb 外包区间证书独立核对这个严格
不等式；解析积分 \(J<10\) 仍是原文输入，不称本项目重做了围道 quadrature。
数值关系 (12) 导出的函数组与 (21)–(22) 冲突，因此原定理成立。

### 5.1 Appendix B 的作用与局限

Appendix B 页 206 起给更基础的动态 box 原理：统一分母型的独立函数满足
\[
h\le\frac{2T(\varphi)}{\log|\varphi'(0)|-(b_1+\cdots+b_r)},
\tag{23}
\]
须分母严格为正。它解释了如何以最低非零 Taylor 系数的算术下界，
和同一芽的解析上界产生矛盾；并没有一个可直接代入任意周期的免分母定理。

对本次含新增积分的 17 个函数，若只用自然安全共同型
\(L_{2j}^2L_j\)，即用 \(j\mid L_j\) 吸收新增 \(j\)，则
\(b_1+b_2+b_3=5\)，而
\(\log(256\cdot1287/2516)<5\)。同一地图下 (23) 的正分母条件失败。
这里不声称 5 是所有可能分母表示的最小成本；它准确指出这种共同上界
处理不能复制成功证明。细阶梯、\(\tau^{\sharp}\) 与加入积分后的秩优势
是实际作用的核心，不能把新增函数当作免费增加秩。

## 6. 对统一周期研究的可复用结论及明确边界

本轮完整推出的是 (4)–(5) 的真实目标识别与 CDT 的数值推论。
本项目没有取得新的单个导子 Dirichlet L 值或奇 ζ 的无理性定理。
也没有声称五项 Li2 中某一个已被指定为无理；(5) 只保证该组合无理，
因而其中至少一个值无理，但未指定是哪一个。

与旧桥梁记录相比，此例提供一个明确操作范本：

1. 用实际数值恒等式把目标周期识别为可处理的组合，核零常数与实分支。
2. 保留全部周期项，直到假定的整数关系使**确切** Hadamard 线性组合进入
   \(\mathbb Q[[x]]\)。这个条件性有理化是数值逻辑步骤，不等于动机扩张分裂。
3. 用全部系数的整数公式证明 \(L_j,L_j^2,L_{2j}^2\) 与积分因子，
   不能从有限良约化素数或固定群投影指标推得这些增长分母。
4. 扩大的是实际积分函数与 pure 辅助系统，并重证其独立性及叶延拓；
   一般导数重复不会增加有限 connection 的秩。
5. 最后核同一系统的严格 \(J<h(\log|\varphi'|-\tau)\)，而不是将
   某一行的最佳分母、另一行的解析半径、形式总维数拼接。

原文 §15.1.10（页 192）明确指出三个或更多 logarithm 的同类 Hadamard
推广在其现有预算下遇到 \(e^3>16\) 的障碍；也建议研究多个两-log 乘积
的同时 Hermite–Padé。本文不把“可以继续 Hadamard 相乘”当作已证明的
三-log 无理性路线。\(\log2\log3\)、\(\pi\log2\) 同样不在 (1) 的定理范围。

进一步可研究的真正输入，是多个实际乘积关系能否提供新的有理过收敛函数，
并在共同参数系统中使增秩超过新增分母成本；这需要重新给具体 connection、
integer model 与单值叶数据，不能仅重述周期猜想。本轮已有五项目标和全账本，
可用于校准该工作，但不声明这样的同时独立定理已经完成。

## 7. 精确证书与审计范围

[脚本](period_holonomy_cdt_mechanism_20261005_verify.py)与
[JSON](period_holonomy_cdt_mechanism_20261005_verify.json)含 120 项固定核验：
两个预先指定参数对 \((m,n)=(2,3),(10^6,10^6+1)\) 的真实 A/H 递推、
Hadamard 微分身份和全部安全分母；对称 trace 的整数递推、求导偏移及六个
积分阶梯；五项恒等式的两个偏导数、零边界和全部有理参数映射；
严格参数边界、\(\tau\) 算术及 Arb 包含的 (22)。

有限证书不代替原文 Lemma 14.3.1 的全尺度独立性、
\(\tau^{\sharp}\) 全局最小化、Corollary 9.0.19 的全部叶条件或 Appendix A.6
的解析积分界。JSON 显示这些外部已证输入，并保存原始 v2 与本稿 SHA。
没有参数扫描，没有用 Li2 或 log 的数值小数判断无理性。
