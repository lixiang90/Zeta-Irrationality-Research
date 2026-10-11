# 第241轮：三阶 logistic 的固定 prime-edge Gram 块

2026-10-09，文件名沿用本轮既定20261008。C独立纸证；本人数学程序0。原始固定矩阵仍为
\[
U(f)=\tfrac32B((tf)')+\tfrac1{24}B((tf)'''),\quad
R_n=D_n^4/D_{5n},\quad h=3n,\quad
Q_n(T)=\det[U_T(t^{i+j}R_n)]_{i,j<h}.
\]
T代表3ζ(3)+ζ(5)。本文支付新局部表的全部有限常数与非退化，不借原K3的表。全阶distribution/off-disc证明分别由Root/B负责；下文全矩阵结论明确以该桥为前提。没有新的数值无理性结论。

## 1. 同一局部尺度发生了什么

实际FULL读原Tang pinned Local、Distribution、Basis以及240已存LocalShape/Gram/PrimeObstruction。n=p−1时用原完整CRT基
\[
\phi_{b,i}=(t+b)^i\prod_{d\ne b}(t+d)^{m_d},\qquad
m_0=4,\ m_b=3\ (1\le b\le p-5),\ m_b=2\ (p-4\le b<p).
\]
总尺寸3p−3，基变换在p处为unit。G(t)=tf(t)，置g_b(u)=G(pu−b)。微分与polynomial Bernoulli multiplication给不同阶的外因子p⁻²、p⁻⁴；本文并不把polynomial身份单独当作含极点的完整distribution。

按Root采用的未除24约定，局部主泛函是
\[
V_3(u^e)=(e)_3B^+_{e-3},\qquad
V_3((u+m)^{-1})=24H_m^{(5)},                     \tag{D1}
\]
其中e<3时第一式为0。V₁对应eB⁺_(e−1)、2H_m³。三阶新源的局部归一化是
\[
\frac1{24}p^{-4}(V_3+36p^2V_1),                 \tag{D2}
\]
在p≥7时第一阶修正有至少两层额外p。V₃是保留完整有理商部与harmonic tail后的局部有理泛函；它不是把全局ζ₅任意删除后的实际积分。将关系点T与跨p修正控制成更高局部层，是完整distribution桥的独立责任。

三个待核主函数与尺寸仍是
\[
r_0=\frac u{(u+1)(u+2)(u+3)(u+4)},\quad m_0=4,
\]
\[
r_L=\frac{u^3}{(u+1)(u+2)(u+3)(u+4)},\quad m_L=3,\qquad
r_H=\frac{u^3}{(u+1)(u+2)(u+3)},\quad m_H=2.
\]
定义M_a=[V₃(u^{i+j}r_a)]_(0≤i,j<m_a)。它们不是旧V₁的Gram块。

## 2. 保留商部的完整有限节点公式

令D₄(u)=∏_(j=1)^4(u+j)，且
\[
H_1^5=1,\quad H_2^5=33/32,\quad
H_3^5=8051/7776,\quad H_4^5=257875/248832.
\]
对1≤k≤7作首一除法uᵏ/D₄。其simple residues为
\[
\frac{(-j)^k}{\prod_{a\ne j}(a-j)}.
\]
k≤6时商部degree≤2，V₃杀掉它；k=7时商部为
u³−10u²+65u−350，V₃值恰为6。故
\[
V_3(u^k/D_4)=
\sum_{j=1}^4\frac{24H_j^5(-j)^k}{\prod_{a\ne j}(a-j)}
+6[k=7].                                      \tag{D3}
\]
这付清原表所需的全部七项，不漏最后的polynomial head。

置x_j=−j和
\[
\beta=(-4,\ 99/4,\ -8051/216,\ 257875/15552).
\]
则
\[
M_0=\left[\sum_j\beta_jx_j^{i+k}\right]_{i,k=0}^3
+6E_{33},\qquad
M_L=\left[\sum_j\gamma_jx_j^{i+k}\right]_{i,k=0}^2
+6E_{22},                                    \tag{D4}
\]
\[
\gamma_j=\beta_jx_j^2
=(-4,\ 99,\ -8051/24,\ 257875/972).
\]
对r_H全部k=3,4,5的商部degree≤2，V₃均为0，因而没有corner修正。它的三个moments精确为
\[
(-3587/24,\ 14937/24,\ -53739/24).
\tag{D5}
\]
例如u³/D₃的residues为−1/2、8、−27/2；乘24H_j⁵立刻给D5首项。后两项各多乘−j。

## 3. 三det的自含纸算与符号

有限节点Hankel determinant的Cauchy–Binet公式为
\[
\det\left[\sum_jw_jx_j^{i+k}\right]_{i,k<r}
=\sum_{|J|=r}\left(\prod_{j\in J}w_j\right)
\prod_{a<b,\ a,b\in J}(x_b-x_a)^2.
\tag{D6}
\]
在D4的右下角加6，只加6倍左上principal minor；不存在其它cofactor项。四节点全Vandermonde平方为144；三节点123/124/134/234的平方依次4、36、36、4。

设A=8051·257875=2076151625。按D6逐项展开给
\[
\det M_0=\frac{269A}{62208}
+11\cdot8051-\frac{11\cdot257875}{8}
=\boxed{\frac{541936393813}{62208}>0},          \tag{D7}
\]
\[
\det M_L=66\cdot8051-2376-\frac{668233}{4}
-\frac{112\cdot257875}{9}-\frac{43A}{3888}
=\boxed{-\frac{100344353231}{3888}<0}.         \tag{D8}
\]
D5直接给
\[
\det M_H=\frac{3587\cdot53739-14937^2}{24^2}
=\boxed{-\frac{210779}{4}<0}.                  \tag{D9}
\]
这是有限显式有理恒等式；全prime子族结论不来自prime样本。

Root的唯一fixed exact程序另独立核对上述三个det及全部moments，一次exit0；其完整JSON本轮已实际FULL读。它给分子分解
\[
541936393813=59\cdot2953\cdot3110519,
\]
\[
100344353231=19\cdot7477\cdot706337,\qquad
210779=131\cdot1609.
\]
分母仅含2、3。纸证仅需分子非零；这个有限分解方便排坏素数。因此全部充分大p上三个新块均是unit。

直接继承旧表的命题确实不成立：新V₃ zero前两矩为
907/15552、−25/3888，而旧V₁为1/1296、7/648；前项同为正，后项符号相反，故两表不成一个非零scalar倍。新表非退化说明应替换表和缩放，不能因此宣称整条新路线失败。

## 4. 仅在完整桥付清后的全矩阵推论

自变量微分增加两次p⁻¹后，同class的raw base exponent应为
\[
\begin{array}{c|c|c|c}
a&\text{own numerator exponent}&|\mathrm{near}|&
\text{base}=\mathrm{own}-|\mathrm{near}|-4\\\hline
0&1&4&-7\\
L&4&5&-5\\
H&4&4&-4
\end{array}
\]
i,k的附加指数仍为i+k。旧base是−5、−3、−2，所以原K3归一化不能免费复用。

**条件推论。** 若Root/B给同一实际U_T全矩阵的完整distribution、所有off-disc余量及关系参数polynomial的更高层，得到由D2–D4组成的unit block diagonal reduction，则
\[
v_pQ_{p-1}(q)
=4(-7)+4\cdot3
+(p-5)\{3(-5)+3\cdot2\}
+4\{2(-4)+2\cdot1\}
=\boxed{-9p+5}.                              \tag{D10}
\]
适用于每固定q∈ℚ以及充分大p∤den(q)，而不是generic q；如果reduction作为ℤ_(p)[T]恒等式付清，则清该leading power后的整个polynomial模p是非零常数，原PrimeObstruction的纯代数引理便给同一primitive P_(p−1)(q)≠0。本文不以fixed表单独认证这两个前提。

归一化也须同对象：
\[
v_pS_{p-1}=4,\quad
v_pF_{p-1}=2\sum_{i=0}^{3p-4}\lfloor i/p\rfloor=6p-12,
\]
所以v_p(S_n^(3n)/F_n)=6p。若D10及整polynomial常数reduction成立，
\[
v_p^{\rm Gauss}\widetilde Q_{p-1}=5-3p=2-3n.
\tag{D11}
\]
这个prime-edge负valuation是O(n)，并不是所有prime累计的n² primitive费用证明。即使该edge桥成功，240所需全系数Gauss预算仍须另付；也不证明新数值定理。

## 5. 范围、决定与账

本轮新成果是D3–D9的完整固定局部Gram非退化和旧table直接继承的精确排除。它使原固定-base/prime-edge入口值得完成同一actual矩阵的distribution/off-disc证明；不需要prime扫描。若完整桥支付了D10的常数reduction，实际每固定有理点的无界非零便有具体证书；若没有，不能以这三个unit块或formalrank代替它。

本人数学运行0。Root唯一bounded exact fixedconstant check为1次，本人只FULL读其JSON，不重跑producer或核Lean；这个核对不是varying-prime样本。新下载仅五份固定commit的必要Lean源码，没有PDF或参数文献扩张。本人实际primary范围及hash见[scope](../literature/logistic_prime_edge_round241_20261008/dual_reading_scope.md)。中断前已FULL读的240三份源码沿用，恢复后不重做已完成数学作业。旧稿/main/manifest不改；最终保存后作者FULL复读，身份另报。
