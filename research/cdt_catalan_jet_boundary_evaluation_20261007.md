# Catalan 二阶边界周期的 level-four 多对数身份与指数有理近似

2026-10-07。固定真实 \(U(z)=M_z(0,1)\)、\(V(z)=Z_z(0,0)\)，求值

\[
\Omega=\frac{[z^2]U-\tfrac32[z^2]V}{3}.
\tag{O1}
\]

本稿得到准确的 \(\zeta(4),\zeta(3)\log2\) 与四次单位根处深度二多对数组成；另给指数收敛的 beta 导数级数、完整全素数系数分母 cap，以及一个严格有理区间。没有证明 \(\Omega\) 与 \(\beta(4)-G/3\) 独立，也没有把一个有限近似的周期空间误当成极限的有理周期空间。

## 1. 同一实际积分在 \(x=e^{-u}\) 下的身份

本轮实际全文重读 [全列池投影稿](cdt_catalan_jet_pool_projection_rank_20261007.md)、[完整 higher-jet 稿](cdt_catalan_higher_jet_holonomy_bridge_20261007.md)，以及原仓库 Catalan `foundations.tex` 全434行。P9a 的真实 \(u=\operatorname{artanh}t\) 积分给

\[
[z^2]U=\int_0^\infty\frac{u^2\log(\cosh u)}{\sinh u}du,
\qquad
[z^2]V=\int_0^\infty
\frac{u^2(u+\log(\cosh u))}{\sinh(2u)}du.
\tag{O2}
\]

它们在0和无穷都绝对收敛；原参数在 \(|\Re z|<1\) 内的局部一致支配允许取 Hasse 系数。置 \(x=e^{-u}\)，则

\[
\Omega=\frac23\int_0^1\frac{\log^2x\,
 \log((1+x^2)/(2x))}{1-x^2}dx
-\int_0^1\frac{x\log^2x\,
 \log((1+x^2)/(2x^2))}{1-x^4}dx.
\tag{O3}
\]

\(\log(1+x^2)\) 和 \(1-x^4\) 的自然字母表包含 \(\pm i\)，不能未经证明地降成 level two。O3 是真实端点变换，没有添加独立形式变量。

## 2. 准确的 colored 多对数组成

定义本稿使用的双参数约定，避免与其他 MPL 参数约定混淆：

\[
\mathcal L_{3,1}(z,w)
:=\sum_{n>k\ge1}\frac{z^nw^k}{n^3k},
\qquad |z|,|w|\le1.
\tag{O4}
\]

所有这里用到的值绝对收敛，因为 \(\sum_n H_{n-1}/n^3<\infty\)。令

\[
\mathcal A=\Re\bigl(\mathcal L_{3,1}(1,i)
-\mathcal L_{3,1}(-1,i)\bigr),
\quad
\mathcal B=\mathcal L_{3,1}(1,-1)
-\mathcal L_{3,1}(-1,1).
\tag{O5}
\]

**实际组成定理。**

\[
\boxed{\quad
\Omega=\frac{195}{64}\zeta(4)
-\frac{91}{96}\zeta(3)\log2
-\frac43\mathcal A+\frac18\mathcal B.
\quad}
\tag{O6}
\]

证明如下。几何级数直接给四个 absolutely convergent log moments：

\[
\int_0^1\frac{\log^2x}{1-x^2}dx=\frac74\zeta(3),\quad
\int_0^1\frac{\log^3x}{1-x^2}dx=-\frac{45}{8}\zeta(4),
\]
\[
\int_0^1\frac{x\log^2x}{1-x^4}dx=\frac7{32}\zeta(3),\quad
\int_0^1\frac{x\log^3x}{1-x^4}dx=-\frac{45}{128}\zeta(4).
\tag{O7}
\]

分开 \(\log(1+x^2),\log2,\log x\)，O3 中的后二者合计恰为 O6 的两个经典常数项。其余部分是

\[
\frac43\mathcal S_U-2\mathcal S_V,
\quad
\mathcal S_U=\sum_{m\ge0,k\ge1}
\frac{(-1)^{k+1}}{k(2m+2k+1)^3},
\quad
\mathcal S_V=\sum_{m\ge0,k\ge1}
\frac{(-1)^{k+1}}{k(4m+2k+2)^3}.
\tag{O8}
\]

对两双和，先固定 \(k\) 求绝对值外和，得到 \(O(k^{-2})\)；再除 \(k\) 后可求和。因此 log 展开、换序和以下 parity 过滤均由绝对收敛合法，不使用 Abel 或其他正则化。

在 \(\mathcal S_U\) 中置外指标 \(n=2m+2k+1\)、内指标 \(j=2k\)。得到 \(n\) 奇、\(j\) 偶、\(n>j\)，以及 \(1/k=2/j\)、\((-1)^k=i^j\)。所以

\[
\mathcal S_U
=-\frac12\bigl(\mathcal L_{3,1}(1,i)
+\mathcal L_{3,1}(1,-i)
-\mathcal L_{3,1}(-1,i)
-\mathcal L_{3,1}(-1,-i)\bigr)=-\mathcal A.
\tag{O9}
\]

在 \(\mathcal S_V\) 中置 \(n=2m+k+1\)，分母为 \(8n^3k\)，且 \(n-k\) 为奇数。故

\[
\mathcal S_V=-\frac1{16}
\bigl(\mathcal L_{3,1}(1,-1)
-\mathcal L_{3,1}(-1,1)\bigr)=-\frac1{16}\mathcal B.
\tag{O10}
\]

O7–O10 证明 O6。这是一个已证明的实际周期身份；它没有把这些 MPL 当作数值独立的基，也没有证明它们不能进一步含有 \(\beta(4)\) 的成分。

## 3. 一个可逐项识别的单参数 Mellin/Hurwitz 表示

对 \(\Re a>0\)，定义真实单参数函数

\[
\mathcal J(a)=\int_0^1x^{a-1}
\frac{\log((1+x^2)/(2x))}{1-x^2}dx,
\quad
\mathcal Q(a)=\int_0^1x^{a-1}
\frac{\log((1+x^2)/(2x^2))}{1-x^4}dx.
\tag{O11}
\]

它们全纯：0端点由 \(x^{\Re a-1}(1+|\log x|)\) 支配，1端点两个 log 分子都消去 denominator 的一阶零。固定阶 \(a\) 导数仍局部可积。直接端点变换还给

\[
\frac{U(z)+U(-z)}2
=2\bigl(\mathcal J(1-z)+\mathcal J(1+z)\bigr),
\qquad V(z)=4\mathcal Q(2-z),
\]
\[
\Omega=\frac23\mathcal J''(1)-\mathcal Q''(2).
\tag{O12}
\]

第一条在 \(|\Re z|<1\) 内成立，第二条直接积分在 \(\Re z<2\) 内成立。记 \(\zeta(s,a)=\sum_{m\ge0}(m+a)^{-s}\)，则两二阶导数有显式 absolutely convergent 级数

\[
\mathcal J''(a)=\frac14\sum_{k\ge1}
\frac{(-1)^{k+1}}k\zeta(3,a/2+k)
-\frac{\log2}{4}\zeta(3,a/2)
+\frac38\zeta(4,a/2),
\]
\[
\mathcal Q''(a)=\frac1{32}\sum_{k\ge1}
\frac{(-1)^{k+1}}k\zeta(3,a/4+k/2)
-\frac{\log2}{32}\zeta(3,a/4)
+\frac3{64}\zeta(4,a/4).
\tag{O13}
\]

系数和参数步长由 \(\int_0^1 x^{c-1}\log^2x\,dx=2/c^3\) 直接得到。外和项为 \(O(k^{-3})\)，在 compact 子半平面局部一致收敛。这给可识别全部 \(U/V\) 偶 jets 的实际单参数级数接口；并未给实际 \(\mathbb Q[[z]]\) 芽或 CDT arithmetic type。

## 4. 指数收敛的 beta 导数级数

另一种展开避免慢速外尾：

\[
\log\frac{1+x^2}{2}
=-\sum_{k\ge1}\frac{(1-x^2)^k}{k2^k}.
\tag{O14}
\]

在 \([0,1]\) 上绝对一致收敛。定义正值

\[
J_{U,k}=\int_0^1\log^2x(1-x^2)^{k-1}dx,
\quad
J_{V,k}=\int_0^1
\frac{x\log^2x(1-x^2)^{k-1}}{1+x^2}dx.
\tag{O15}
\]

于是 O3 给真实指数级数

\[
\Omega=\frac{195}{64}\zeta(4)
+\sum_{k\ge1}\frac{-\tfrac23J_{U,k}+J_{V,k}}{k2^k}.
\tag{O16}
\]

这里 \(0<J_{U,k}\le2\)，且 \(0<J_{V,k}\le\tfrac12J_{U,k}\)，因为 \(x/(1+x^2)\le1/2\)。设 O16 截断至 \(k=N\) 为 \(\Omega_N\)，则

\[
\boxed{\quad
0<\Omega_N-\Omega
\le\frac43\frac{2^{-N}}{N+1}.
\quad}
\tag{O17}
\]

所有项的绝对值被 \(\tfrac43/(k2^k)\) 支配，故这里同样不需要正则化。

两个正积分是完整 beta 导数接口。记 \(B(a,k)=\int_0^1y^{a-1}(1-y)^{k-1}dy\)。则

\[
J_{U,k}=\frac18\partial_a^2B(a,k)|_{a=1/2}
=\frac12 B(1/2,k)\left(
\left(\sum_{j=0}^{k-1}\frac1{2j+1}\right)^2
+\sum_{j=0}^{k-1}\frac1{(2j+1)^2}\right),
\]
\[
B(1/2,k)=\frac{4^k}{k\binom{2k}{k}},
\quad
J_{V,k}=\frac18\partial_a^2
\left(\int_0^1\frac{y^{a-1}(1-y)^{k-1}}{1+y}dy\right)_{a=1}.
\tag{O18}
\]

第一条可直接对 \(B(a,k)=(k-1)!/\prod_{j=0}^{k-1}(a+j)\) 微分证明；不需要 gamma 函数的额外身份。

对整数 \(k\)，作**整数**多项式除法

\[
\frac{(1-y)^{k-1}}{1+y}
=\sum_{j=0}^{k-2}q_{k,j}y^j+\frac{2^{k-1}}{1+y},
\quad q_{k,j}\in\mathbb Z.
\tag{O19}
\]

\(k=1\) 时多项式和为空。由 \(\int_0^1\log^2y/(1+y)dy=2\eta(3)=\tfrac32\zeta(3)\)，得到

\[
J_{U,k}=2\sum_{j=0}^{k-1}
\frac{(-1)^j\binom{k-1}j}{(2j+1)^3},
\qquad
J_{V,k}=\frac14\sum_{j=0}^{k-2}\frac{q_{k,j}}{(j+1)^3}
+\frac{3\,2^{k-1}}{16}\zeta(3).
\tag{O20}
\]

因此每个有限近似准确属于

\[
\Omega_N=\alpha_N+\frac3{32}H_N\zeta(3)
+\frac{195}{64}\zeta(4),\qquad \alpha_N\in\mathbb Q,
\]
\[
\alpha_N=\sum_{k=1}^N\frac1{k2^k}
\left(-\frac23J_{U,k}
+\frac14\sum_{j=0}^{k-2}\frac{q_{k,j}}{(j+1)^3}\right),
\quad H_N=\sum_{k=1}^N\frac1k.
\tag{O21}
\]

不能将 O21 取极限后断言 \(\Omega\in\mathbb Q+\mathbb Q\zeta(3)+\mathbb Q\zeta(4)\)：这只是有理向量空间，在通常实拓扑下并不闭；且 \(H_N\) 发散，与 \(\alpha_N\) 的相消必须保留在同一个有限表达内。

## 5. 全素数分母付款与严格有理数值证书

令 \(D_M=\operatorname{lcm}(1,\ldots,M)\)。O20 的第一有限和由 \(D_{2N-1}^3\) 清分母；第二有理和由 \(4D_N^3\) 清分母。外面的 \(k2^k\) 仅一次性增加 \(D_N2^N\)。由于 \(D_N\mid D_{2N-1}\)，一个完整 cap 是

\[
\boxed{\quad
M_N=192\,2^N D_{2N-1}^{3}D_N,
\quad M_N\alpha_N,\quad
M_N\frac3{32}H_N,\quad M_N\frac{195}{64}\in\mathbb Z.
\quad}
\tag{O22}
\]

它覆盖全部素数和全部高幂；beta 形式中的中央二项式分母不再另付。按标准 \(\log D_M=M+o(M)\)，

\[
\log M_N=(7+\log2)N+o(N).
\tag{O23}
\]

这是一份安全系数预算，不称最小分母或必要费用。它远大于 O17 的 \(N\log2\) 收缩，因此当前近似本身没有给出无理性或 LI 矛盾；尤其不能把 O22 称为 \(\Omega_N\) 的整数模型，因 \(\zeta(3),\zeta(4)\) 仍未有理化。

数值证书使用**有理**的经典值上下界，不依赖浮点库的 zeta 精度。对 \(s=3,4\)，置

\[
d_{s,k}=\sum_{j=0}^k\frac{(-1)^j\binom kj}{(j+1)^s}
=\frac1{(s-1)!}\int_0^1(1-x)^k(-\log x)^{s-1}dx\in(0,1],
\]
\[
Z_{s,M}=\frac1{1-2^{1-s}}
\sum_{k=0}^{M-1}\frac{d_{s,k}}{2^{k+1}}.
\tag{O24}
\]

由正项几何求和 \(\sum(1-x)^k/2^{k+1}=1/(1+x)\)，

\[
0<\zeta(s)-Z_{s,M}\le
\frac{2^{-M}}{1-2^{1-s}}.
\tag{O25}
\]

有限 \(Z_{3,M},Z_{4,M}\) 分别可由 \(3\,2^MD_M^3\)、\(7\,2^MD_M^4\) 清分母。证书区间只把这些有理界与 O17/O21 合并；其辅助测量付款不冒充未来研究格的免费 arithmetic type。

本轮一段全新内联 Fraction/mpmath 计算取 \(N=192,M=256\)。以 O21 的准确 \(\alpha_N\)、O24 的准确有理下界和 O17/O25 的尾界，得到向外取整到55位小数的**严格有理区间**

\[
\boxed{\quad
2.5366889785183897331535011770827664395080804102784254349
<\Omega<
2.5366889785183897331535011770827664395080804102784254350.
\quad}
\tag{O26}
\]

取整前有理区间宽度约 \(1.10058163117959\cdot10^{-60}\)。独立直接对 O2/P9b 的 \(u\) 积分作80位和110位计算，两者相差约 \(1.5531\cdot10^{-81}\)；110位值为

\[
2.536688978518389733153501177082766439508080410278425434965229374005\ldots,
\]

落在严格区间内。用110位标准 zeta 值评价 \(\Omega_{192}\)，它比直接积分大约 \(4.79767412307\cdot10^{-61}\)，符合 O17 的方向和界。浮点积分只是独立核对；O26 的严格性来自准确有理运算及纸面尾界，而不是浮点一致性。另以外指标截断32的全新准确 Fraction 求和核对 O9/O10 的两个 parity identities，均逐项一致。

## 6. 对真实周期投影的准确影响

原 full pool 的最高边界项是 \(\Omega\mathcal D_N\)，\((\mathcal D_N)_{r,j}=[t^j]D_r\)。O6 将它替换成四个具体实际生成元 \(\zeta(4),\zeta(3)\log2,\mathcal A,\mathcal B\) 的固定有理组合，其 substitution coefficients 由192清分母，固定费用只到行列式的 \(O(n)\) 阶；原数组的 \(n^2\) 费用并没有因此消失。

在没有进一步已证周期关系的认证模型中，这四项的新系数矩阵都只是非零有理倍数的 \(\mathcal D_N\)。要求逐项消去它们仍等价于 \(\mathcal D_N v=0\)，所以先前精确的低坐标核和 \(8N+1\) endpoint 核仍成立。若其中某个深度二 period 可与原 \(G,\beta(4)\) 或其他 seed 合并，则必须使用真实身份重算全部 coefficient stack；O6 本身没有证明这种合并，也没有证明不存在这种合并。

因此本轮填补的是“边界种子是什么”的实际识别和可认证近似接口，不是其数值独立性。也不能把 O11–O13 的复参数 \(a\) 芽当作自动满足 CDT 的有理芽：其 Taylor 系数仍包含未消去的实际周期。

## 7. 阅读与验证范围

实际全文阅读三份指定输入：全列池稿全部8节/P1–P28及P9a–d；higher-jet稿全部8节/H1–H30；原仓库 foundations.tex 全434行。合并输出中 foundations 的中段被截断，随后单独完整显示全文补齐。未修改这些输入或任何原仓库文件。

本稿所有身份由上述实际积分、有限多项式除法、绝对收敛级数与正项尾界自行推导，没有引用外部未读降深/period-basis定理。新 PDF 阅读0页，新网页数学输入0，新文献下载0。

作者只运行1段全新内联计算：准确 Fraction 产生 O21/O24/O26，mpmath 在80/110位作独立实际 u 积分核对，以及截断32的 parity有限证书。没有执行旧620 producer/guard、旧数学脚本、prime扩表或Lean；没有 PSLQ、未知常数拟合或把浮点检查称为形式化验证。

root 已实际全文读本稿全部7节/O1–O26，并独立重推 O3 端点因子、O6 四项系数、O9/O10 parity、O12/O13 Mellin 归一化、O17 符号尾界、O18–O23 完整系数 cap、O24/O25 正 Euler 证书，明确数学 PASS。唯一文字微修是澄清 O21 后有理向量空间的拓扑范围；作者已收讫修订。作者另实际全文独审 [全部偶阶边界稿](cdt_catalan_all_even_jet_boundary_20261007.md) 全5节/A1–A15，重推正尾归一化、所有偶阶 seed 传播、同一原核、参数无限双极点及其适用变量范围，明确 PASS，没有为该交叉审查运行新程序。

root 又以1段全新内联 Fraction 独立重算 O26：JU 全部使用有限 binomial 展开，区别于作者的 beta 导数求值；JV 使用整数多项式除法；N192/M256 的正 Euler 有理上下界完整重构。55位上下端点与 O26 逐位一致，原有理区间宽度为约 \(1.1005816311795871017\cdot10^{-60}\)，明确 PASS。root 未复算作者的80/110位浮点积分或截断32 parity样本。作者收讫以上审查后完成最终全文回读；全文纸审与准确有限证书不称为 Lean 或其他机器形式化证明。
