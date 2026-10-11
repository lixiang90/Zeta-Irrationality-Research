# Level12 χ12 尖点源的精确 Manin 周期接口与两源零周期障碍

日期：2026-10-06。本稿只读冻结的 cuspidal_corrector_window 等输入，不执行、import 或修改其 producer。新的固定24-coset计算另建，给实际 \(L(3)\) 与共轭源在 \(2/7\) 的 additive endpoint 同一个模符号矩阵表示。

得到的新结论是有限源窗口的严格限制：在 \(K=\mathbf Q(\sqrt3)\) 的二维 \(\chi_{12}\)-cuspidal W-minus 窗口中，没有非零源同时保留第一支零 \(L(3)\) 周期并使第二支在既定反射 \(M\) 的周期实部为零。这不证明两 \(L(3)\) 数值在 K 上线性无关，不排加入平凡字符 \(U\)，不排其它反射、其它源或完整 stabilizer 路线。

## 1. 实际源、规范与所需周期

令 \(r=\sqrt3\)、\(\sigma r=-r\)，沿用已证明的实际整数源
\[
X=(X_0,X_2),\quad
X_0=16(C_6-3rC_0),\quad X_2=16(C_4-rC_2),\qquad X|W=-X.
\tag{1}
\]
系数共轭 \(\bar X=\sigma X\) 是实际 W-plus 源。这里 bar 始终仅指 source coefficients，不作用于未知周期数。

写
\[
f_F=\theta_q^{-3}F=\sum_{n\ge1}\frac{a_n(F)}{n^3}q^n,\quad
\Omega=(\Omega_0,\Omega_2)=(L(X_0,3),L(X_2,3)),
\quad
\Psi=(L(\bar X_0,2),L(\bar X_2,2)).
\tag{2}
\]
\(\Omega_0,\Omega_2>0\)，且冻结稿已严格证明
\(3r<\Omega_0/\Omega_2<4+r\)。

对任意 weight4 cusp source，
\[
f_F(x)=4\pi^3i\int_x^{i\infty}F(\tau)(\tau-x)^2\,d\tau.
\tag{3}
\]
这是同一个 q-constant-zero primitive 的实际边界值。常数来自逐项积分
\(\int_0^{i\infty}e^{2\pi in\tau}\tau^2d\tau=-i/(4\pi^3n^3)\)。
这里的 fixed cusp source是有限个 normalized eigenforms的线性组合；Ramanujan–Deligne bound给
\(a_n(F)=O_\varepsilon(n^{3/2+\varepsilon})\)。取 \(0<\varepsilon<1/2\)，则
\(\sum |a_n(F)|/n^3<\infty\)，所以 \(f_F(x)\) 在 rational x 绝对收敛；所有随后路径都是收敛的 cusp integrals。Paşol–Popa原件PDF p14 Proposition5.11证明也明确使用该 Ramanujan bound。

## 2. 固定72维 Manin 模型与真实 cusp 子空间

采用 \(\Gamma_0(12)\backslash {\rm PSL}_2(\mathbf Z)\simeq
\mathbf P^1(\mathbf Z/12)\) 的24个固定左 cosets \(A_j\)。具体 SL2 整矩阵和以下全部基保存在同名 JSON；它们由固定有限 coset closure 产生，不是研究参数或 word 搜索。

每个分量的 multiple period polynomial为
\[
\rho_F(A_j)(z)=\int_0^{i\infty}(F|_4A_j)(\tau)(\tau-z)^2\,d\tau
=\rho_{j,0}+\rho_{j,1}z+\rho_{j,2}z^2.
\]
系数按72维列排列。若 \(A_jg^{-1}=\gamma A_l\)，则
\[
(B_g\rho)_j=\chi_{12}(\gamma)R_g\rho_l,\qquad
R_g=\begin{pmatrix}
d^2&bd&b^2\\2cd&ad+bc&2ab\\c^2&ac&a^2
\end{pmatrix}.
\tag{4}
\]
令 \(S=(0,-1;1,0)\)、\(T=(1,1;0,1)\)、\(U=TS\)。完整 Manin 空间是
\[
\mathcal W=\ker(1+B_S)\cap\ker(1+B_U+B_U^2),\quad \dim_{\mathbf Q}\mathcal W=12.
\]
coboundaries为 \((1-B_S)\ker(B_T-1)\)，准确维4。不能把12维 Manin 空间直接当作8维实际 cusp periods；这是原论文 §7 的 extra relations 要解决的区别。

本稿用真实 Hecke 分离：
\[
\mathcal V=\mathcal W\cap\ker(B_5^2+80),\qquad \dim\mathcal V=8.
\tag{5}
\]
新的 q/Sturm 计算证明在四维实际 \(\chi_{12}\) cusp source空间上 \(T_5^2=-80\)。也可由下面两维 X/\(\bar X\) 传递矩阵直接得到。于是实际 \(\rho_F^\pm\) 都在 (5)。Paşol–Popa Theorem5.14 的 injectivity给每个 parity 维4；新固定线性代数也给 \(\mathcal V^\pm\) 各维4。因此 (5) 在每个 parity 正好是实际 cusp image，已排除 coboundary 假周期。

parity为 \(\varepsilon=(-1,0;0,1)\) 的 Paşol–Popa convention：
\(\rho^\pm=(\rho\pm B_\varepsilon\rho)/2\)。W-plus、W-minus 在每个 parity 各维2。对实际 real q coefficients，
\[
\rho^+\in i\mathbf R^{72},\qquad \rho^-\in\mathbf R^{72};
\tag{6}
\]
故 (3) 的 endpoint 实部来自 \(\rho^+\)，虚部来自 \(\rho^-\)。星号采用原文 convention；不能直接移用采用相反 overall sign 的 homology star 标签。

## 3. 固定 Hecke 源传递与两个 even carriers

以行 source基 \(X,\bar X\) 记算子，新的实际 q coefficients1至8给
\[
T_5X=\bar X H_5,\quad
H_5=\begin{pmatrix}1&-r\\-27r&1\end{pmatrix},\qquad
T_7X=\bar X H_7,\quad
H_7=\begin{pmatrix}-3r&-1\\33&-3r\end{pmatrix}.
\tag{7}
\]
两边是已证明的 weight4 level12 \(\chi_{12}\) cusp forms；Sturm bound8使固定检查成为完整身份。新证书独立从 eta logarithmic derivative 和 \(u+u^2=x-2xu-2xu^2\) 重算 q coefficients，没有 import 已冻代码。所有 q 截断只用于这些 Sturm 身份，未用来证明周期数字关系。

coefficients共轭与 rational Hecke commuting给
\[
T_5^2=-80,\quad T_7^2=-60,\qquad
T_{57}X=XH,\quad
H=\sigma(H_5)H_7=
\begin{pmatrix}30r&-10\\-210&-30r\end{pmatrix},
\quad H^2=4800.
\tag{8}
\]
\(T_5,T_7\) 与 W反对易，\(T_{57}=T_5T_7\) 与 W commuting。
准确 Hecke eigen-sources为
\[
Y_+=X_0-rX_2,\quad T_{57}Y_+=40rY_+;
\qquad
Y_-=X_0+7rX_2,\quad T_{57}Y_-=-40rY_-.
\tag{9}
\]
它们的 \(L(3)\) 都非零，由上述 strict positive ratio 得出。两个 even period eigenlines在 K 上各维1；所以 full even period vectors可按这两份实际 \(L(3)\) 归一，随后系数全在 K。这是严格的形式周期接口，**不是**两归一化数字的 K 线性无关证明。

LMFDB实际原页的四个 inner twists为 \(1,\chi_{-3},\chi_{-4},\chi_{12}\)；中间两者 odd、最后一个 even。它们不能被当成同一个未经计算的 period数字。特别 odd twist改变 Betti parity，而 ramified primes的普通 coefficient twist还会删去 Euler factors。本文没有以数据库 embedding 或 twist标签替代实际模符号等式，也没有声称证明了所有 twisting period comparison。

## 4. \(L(3)\) 与 \(2/7\) 在同一个矩阵中的精确关系

令 \(\ell\) 取 \(\rho_F(I)\) 的常数项，\(e\) 为 (3) 中 \(x=2/7\) 的积分行，\(m\) 取 \(\rho_F(I)\) 的一次项。路径
\[
\{2/7,\infty\}=\{0,\infty\}+\{1/3,0\}+\{2/7,1/3\}
\]
由矩阵 \(I\)、\((0,1;-1,3)\)、\((1,2;3,7)\) 给出。对 \(P=(\tau-2/7)^2\)，三个 transformed polynomials分别是
\[
P,\quad (2\tau+1)^2/49,\quad \tau^2/49.
\]
因此 e 是明确 rational72维行，未以数值 Fourier samples猜测。

新的完整 Manin 矩阵给三条确切 functional identities：
\[
\begin{aligned}
\ell B_5&=80\ell+\tfrac12\ell B_{57}
&&\text{on W-minus, even cusp periods},\\
e&=-\tfrac{25}{91}\ell-\tfrac1{364}\ell B_{57}
&&\text{on W-plus, even cusp periods},\\
e&=\tfrac17m
&&\text{on W-plus, odd cusp periods}.
\end{aligned}
\tag{10}
\]
它们在上节实际 cusp space上成立，而不是 modulo coboundary。可手核的新 JSON基中
\[
\begin{array}{c|cc}
&\text{W-minus even basis}&\text{W-plus even basis}\\
\ell&(-1/17,-1/34)&(1/3,7/54)\\
\ell B_{57}&(240/17,190/51)&(160/3,170/27)\\
e&(-89/833,-36/833)&(-5/21,-10/189)
\end{array}
\]
第一列的 \(\ell,\ell B_{57}\) determinant为 \(10/51\ne0\)。W-plus odd基上
\(m=(-69/8,-1/16)\)、\(e=(-69/56,-1/112)\)。完整矩阵与等式检查都在 NEW JSON。

从 (7)、(8)、(10)，得到真实系数共轭源的关键值
\[
L(\bar X,3)=\Omega\,A,\qquad
A=(80I+\tfrac12H)H_5^{-1}
=\begin{pmatrix}
-1+\tfrac32r&-\tfrac12-r\\
\tfrac{33}2-27r&-1+\tfrac32r
\end{pmatrix}.
\tag{11}
\]
这条是实际 period relation，不是把 \(L(\bar X,3)\) 写成 \(\sigma\Omega\)。

完整 additive endpoint公式为
\[
\boxed{
f_{\bar X}(2/7)=\Omega R+\frac{2\pi i}{7}\Psi,\qquad
R=\frac5{14}\begin{pmatrix}
1-3r&1+r\\-33+27r&1-3r
\end{pmatrix}.}
\tag{12}
\]
规范中 \(m=\rho_{I,1}=L(F,2)/(2\pi^2)\)，故虚部恰为 \(2\pi L(F,2)/7\)；没有丢 Gauss 或 \(2\pi i\) 因子。矩阵 \(R=A[-25I/91-\sigma(H)/364]\)。

(12) 把所需未知量准确分为两份 even \(L(3)\) 与真实 W-plus central \(L(2)\)。同一源码函数对任意 rational endpoint的 continued-fraction路径给 rational72维行；这是全尺度接口，不是全部其它 reflections已求值的声称。

## 5. 新的全 K 两源障碍

假设 \(C=uX_0+wX_2\)、\(u,w\in K\)，满足
\[
L(C,3)=0,\qquad \operatorname{Re} f_{\sigma C}(2/7)=0.
\tag{13}
\]
若 \(u=0\)，\(\Omega_2>0\) 强制 w=0。若 \(u\ne0\)，令
\[
\alpha=\Omega_0/\Omega_2=-w/u\in K,\quad
\alpha=a+br,\quad a,b\in\mathbf Q,\quad
\sigma\alpha=a-br.
\]
(12) 与 coefficientwise conjugation给
\[
(\alpha,1)R(1,-\sigma\alpha)^t=0.
\]
消去非零因子 \(5/14\)，rational与 r coefficients分别为
\[
-a^2+3b^2-18b-33=0,\qquad
-a^2+3b^2+2b+27=0.
\tag{14}
\]
相减迫 \(b=-3\)，再迫 \(a^2=48\)。48不是 rational square，与 \(a\in\mathbf Q\) 矛盾。因此 (13) 只有零解。

此障碍不需要假设 \(\Omega_0,\Omega_2\) 在 K 上线性无关，也不需要未知 central值的非零性。它比单纯“有两个未知周期”更明确：即使偶然存在 K 的 first-period零方向，它也不能同时给既定 M 的 second-embedding real zero。Eisenstein \(F_L+sR\) 在 M 的其余 cocycle只沿 \(i\pi^3\) 线，因此调整那个 R系数不能取消这个 cusp实部。

加入平凡字符 cusp U 后 first condition是
\(t\Omega_U+u\Omega_0+w\Omega_2=0\)，上面的二源证明不能套用；其 \(2/7\) 模符号也需另外保留。其它反射的 real endpoint矩阵也可能不同。故本文不把 (14) 扩大为完整三维 cusp kernel或全稳定子排除。

## 6. 若改以 cusp 周期作为目标：合法触发器与共轭缺口

例如对 rational \(\alpha\)，取
\(C=X_0-\alpha X_2\)。假设 \(L(C,3)\in K\) 时，
\(f_C-L(C,3)\) 的第一支 q germ确为 arithmetic；完整 W period cancellation给第一支适当 modular multiplier后的正则反射接口。

第二embedding的合法 germ是
\[
\sigma f_C-\sigma(L(C,3)),
\]
它的真实 W-plus period仍为 (11) 的 source integral，真实 M endpoint仍为 (12)。不能把二者换成 \(\sigma(L(C,3))\)。单个数在 K 的反证假设只允许共轭已假定的代数数，不能共轭其它未知 \(\Omega_j,\Psi_j\)。因此本文没有从“Ω比值若有理”的一句假设自动得到共同 filled leaf。

对两个 eigen-target \(L(Y_\pm,3)\) 也须同样保留 (11)、(12) 与 odd-period carrier。Paşol–Popa 的 newform period algebraicity仅使各 eigenline的 normalized polynomial coefficients代数，不证明 period自身的有理性或跨 eigenlines的数值比值。明确这些条件后可把完整 period tuple作为联合目标，但本稿尚未给其 CDT矛盾。

## 7. 原始文献、固定证书与审核范围

本轮实际读 Paşol–Popa《Modular forms and period polynomials》§2、§5.3–5.5及§7，尤其 Theorems2.1/5.14 与 Proposition5.11；实际读 Stein 原著 printed pp131–139 的 cuspidal modular symbols、integration pairing与Hecke兼容；实际读 Manin1973原文 pp371–375 的 periods theorem。Manin该篇的主 periods theorem限定 full modular group；本稿level/character接口用 Paşol–Popa 的明示 extension，未把1973主定理的范围扩大。

相关原件与本轮阅读清单另保存 literature/cdt_odd_level12_manin_period_primary_20261006.json；Manin公开原件新增保存，Paşol–Popa与Stein沿用库内同一原件、不下载覆盖。

NEW producer执行历史：
第一次22项 Manin checks通过；第二次增 q transfer时 exact solve成功，但未简化 Sympy表达式的 structural equality失败，没有产生扩展终证书；第三次修正比较并保留一额外qjet，28项通过；第四次加实际 endpoint identities，33项通过；第五次加 (14) anisotropic K障碍与eigenlines，40项通过。没有运行或import冻结/同行producer。固定检验不替代正文 integration/character/Sturm/ES范围论证。

root实际完整只读本MD与NEW PY，并读NEW JSON的functional rows、cosets、shapes、checks与完整执行历史；没有逐项重算长basis。root还实际回读Paşol–Popa原件PDF pp3–4、13–16，独核Theorem5.14的character coinduced map/injectivity、代码det-normalized slash与一次系数、(3)的4π³i、m=L2/(2π²)、(11)/(12)与全K式(14)通过。root没有执行producer，没有把此源二window的结构排除提升为numeric LI。

其它独审只按实际完成的范围另记；尚无新的数值无理性或线性无关性定理。

