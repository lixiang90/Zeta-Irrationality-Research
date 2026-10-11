# 固定真实middle的三种权重：临界M5的三个初始矩与显式端点归约

2026-10-06，/root/conifold_arithmetic_hypothesis。NEW，baseline471全部既存数学输入只读。旧和同行producer执行/import/rerun均0。本轮新自有producer恰首次1次PASS，源及JSON此后冻结。本文证明原固定λ2的全尺度算术恒等式，不证明无限M5非零或新的ζ/L定理。

## 1. 本轮直接推进的实际目标

实际完整重读main§§127–132及冻结c4dcee的T1–T27；组合读取旧结构dcc6中段首次截断，随后单独实际补读U13–U28和U29开头。沿用真实χ、halfjet和原profile(r,3r)，不选genericλ，不用QQ fullunit推shortunit。以下直接对M5各块的真实moments归约；允许G0及所有中间profiles奇异。

取p=18r+1素数、a=5r，y-variable中

\[
S_y(y)=\prod_{j=5r+1}^{9r}(y^2-j^2),\quad
S(u)=\prod_{j=5r+1}^{9r}(u-j^2),\quad u=y^2.
\tag{Z1}
\]

S_y在−a≤k≤a全非零。对even polynomial f(y)，定义真实folded forms

\[
G(f)=\tfrac12\left(\sum_{k=-a}^a+\sum_{k=1-r}^{r-1}\right)
S_y(k)^{-5}f(k),
\]
\[
C(f)=\tfrac12\left(5\sum_{k=-a}^a-\sum_{k=1-r}^{r-1}\right)
S_y(k)^{-1}f(k),\qquad
H(f)=\tfrac12\left(\sum_{k=-a}^a+\sum_{k=1-r}^{r-1}\right)
S_y(k)^3f(k).
\tag{Z2}
\]

它们准确是旧G0、C5、H0的moment functionals；f=T(y²)T'(y²)、T(y²)Q(y²)、Q(y²)Q'(y²)时degrees分别≤4r−4、8r−4、12r−4。M5仍为[[G0,C5],[C5^t,H0]]，4r阶。Middle cut与k0的folding是Z2中的真实双和，没有删除halfjet。

## 2. Wilson/Fermat给同一固定Pochhammer比值

PS=u^(9r+1)−u把square nodes与head分割；Wilson对0≤k≤a给

\[
S_y(k)=\frac{(-1)^{r+k+1}}{(a-k)!(a+k)!},\quad
w_0=S_y(0)^{-1}=(-1)^{r+1}(a!)^2.
\tag{Z3}
\]

令h_k=S_y(k)^−1/w0，h_−k=h_k，则

\[
h_k=\left(-1\right)^k\frac{(a-k)!(a+k)!}{(a!)^2}
=\frac{(a+1)_k}{(-a)_k},\quad 0\le k\le a,
\qquad
(k-a)h_{k+1}=(k+a+1)h_k\quad(k<a).
\tag{Z4}
\]

这里(a+1,-a)≡(13/18,5/18)modp，两个rational parameters固定。全部出现的阶乘指标<p、分母Pochhammer在k≤a无零。不能把h_(a+1)当普通unit：它正越过first denominator pole；下文单独处理这个端点。

三个weight ratios是h^5、h^1、h^−3。C是fixed-parameter truncated2F1(1,13/18;5/18;1)型的polynomial moments，G是相同比值第五幂的6F5型moments；真实middle给另一截断r−1。不是标准complete finite-character hypergeometric sum的自动识别。

## 3. 三个无目标norm分母的离散算子

在Fp[y]设

\[
\mathscr D_1g=(y+a+1)g(y+1)-(y-a-1)g(y),
\]
\[
\mathscr D_5g=(y+a+1)^5g(y+1)-(y-a-1)^5g(y),
\]
\[
\mathscr D_{-3}g=(y-a)^3g(y+1)-(y+a)^3g(y).
\tag{Z5}
\]

对称空间B={g:g(1−y)=g(y)}以(y−1/2)^(2j)为basis。逐项代入−y，Z5皆把B映到even polynomials。对monic degree n的g∈B，highest coefficients分别是

\[
\deg\mathscr D_1g=n,\ [y^n]=n+2a+2;
\quad\deg\mathscr D_5g=n+4,\ [y^{n+4}]=n+10a+10;
\]
\[
\deg\mathscr D_{-3}g=n+2,\ [y^{n+2}]=n-6a,
\tag{Z6}
\]

只要对应highest coefficient非零。证明：最高y^(n+1/5/3)项抵消，下一项分别加上shift贡献n与两个linear factor的差；由反射，剩余odd powers自动为0。没有除任何unknown G/H/endpoint norm。

## 4. 全辅助素数上的临界nonresonance与唯一分解

**Theorem Z7。** 对每个实际p=18r+1：

1. D1在B_degree≤8r−4到even_degree≤8r−4间为同维isomorphism。因为0≤n≤8r−4时0<n+10r+2≤18r−2<p。
2. r≥2时，D5在B_degree≤4r−8上injective，image与span(1,y²)直和，准确覆盖even_degree≤4r−4。若9(n+10a+10)≡0，则9n+65=kp、k≡2mod9；首次nonnegative root n=4r−7，超过输入cutoff4r−8。其他根加p更高。故Z6全为units。
3. D−3在B_degree≤12r−6上injective，image与span1直和，准确覆盖even_degree≤12r−4。n−30r位于[−30r,−18r−6]；唯一可能multiples为−p，对应n=12r−1，仍在cutoff外；−2p低于整个interval。

每条由unit triangular highest coefficients和维数证明，因此每个critical f有**唯一**分解

\[
C:\ f=\mathscr D_1g;
\qquad G:\ f=\mathscr D_5g+c_0+c_1y^2;
\qquad H:\ f=\mathscr D_{-3}g+c_0.
\tag{Z8}
\]

r1的G cutoff只有常数，规定g0、c1=0；其余两条不变。所有系数可用known-unit triangular elimination求得，无perfect intermediate-path假设。

Z7是当前degree bounds上的全尺度specific arithmetic lemma，不是由finite cases外推。两个raising operators的resonant degree都是奇数且在此cutoff外；若扩展profile不能继续免费继承unit结论。

## 5. 真端点telescoping，包括first denominator pole

对j1或5、g∈B，内部−a≤k<a由Z4得

\[
h_k^j\mathscr D_jg(k)
=h_{k+1}^j(k-a)^j g(k+1)
 -h_k^j(k-a-1)^j g(k).
\tag{Z9}
\]

对0≤l<a，将−l..l求和，反射h_−k=h_k、g(1−y)=g(y)，给

\[
\sum_{k=-l}^l h_k^j\mathscr D_jg(k)
=2(a+l+1)^j h_l^j g(l+1).
\tag{Z10}
\]

对l=a，不能引用undefined h_(a+1)。最后一项k=a直接用D_j定义：其上边界是(2a+1)^j h_a^j g(a+1)，下边界k=−a是其负数（j odd）。因此全cutoff仍有

\[
\sum_{k=-a}^a h_k^j\mathscr D_jg(k)
=2(2a+1)^j h_a^j g(a+1).
\tag{Z11}
\]

这是显式last-node flux，不是把0·undefined误当0。真实middle取l=r−1，由Z10留下2(a+r)^j h_(r−1)^j g(r)。

负三次幂使用

\[
h_k^{-3}\mathscr D_{-3}g(k)
=h_{k+1}^{-3}(k+a+1)^3g(k+1)
 -h_k^{-3}(k+a)^3g(k).
\tag{Z12}
\]

此时h_(a+1)^−3对应S_y(a+1)^3/w0^−3，明确为0；左端k−a的(k+a)^3也为0。故

\[
\sum_{k=-a}^a h_k^{-3}\mathscr D_{-3}g(k)=0,
\]
\[
\sum_{k=1-r}^{r-1}h_k^{-3}\mathscr D_{-3}g(k)
=-2(a-r+1)^3h_{r-1}^{-3}g(r).
\tag{Z13}
\]

第二式的负号来自odd cube和两端反射；它不能因full flux0就被删除。

## 6. 原λ2全部moments的三个初始矩归约

取A0=G(1)、A1=G(y²)、B0=H(1)，它们是实际values，不是可任意选的诊断参数。Wilson明确化端点：

\[
w_0h_a=-(10r)!,\quad
w_0h_{r-1}=(4r+1)!(6r-1)!.
\tag{Z14}
\]

把Z8代入Z2、Z10–13，得到实际公式

\[
\boxed{C(f)=-5(10r+1)!\,g(5r+1)
 -(4r+1)!(6r)!\,g(r),\quad f=\mathscr D_1g.}
\tag{Z15}
\]

\[
\boxed{G(f)=c_0A_0+c_1A_1
 -[(10r+1)!]^5g(5r+1)
 +[(4r+1)!(6r)!]^5g(r).}
\tag{Z16}
\]

\[
\boxed{H(f)=c_0B_0
 -\frac{g(r)}{[(4r)!(6r-1)!]^3},
\quad f=\mathscr D_{-3}g+c_0.}
\tag{Z17}
\]

所有factorials在Fp为units。G全end给负号、middle给正号；C两个boundary皆负；H full为0但middle给负。这些符号均由真实cutoff推得。

**Corollary。** 原M5的cross块全部显式已知，不再需要未知cross初始矩；G块仅依赖A0,A1，H块仅依赖B0。这是直接固定original λ2的constant-number moment reduction，区别于冻结K24阶数N随r增长的spectral recurrence。

本稿既不要求A0、A1、B0各为unit，也不要求G0非退化。旧p37的真实A0=0并不破坏任何Z8–17。最终M5可正常，即使某个初始矩或中间leading minor为0。

## 7. full正三次权重的Dixon单位，及真实middle的剩余

从Z3，有integer-identity reduction

\[
\sum_{k=-a}^a S_y(k)^3
=\frac{(-1)^{r+1}}{[(2a)!]^3}
\sum_{k=-a}^a(-1)^k\binom{2a}{a+k}^3
=\frac{(-1)^{r+1}(15r)!}{[(5r)!]^3[(10r)!]^3}
\in F^\times.
\tag{Z18}
\]

这里引用的Dixon identity可自证，避免把标准Selberg template硬套actual target：
对D(a,b,c)=CT Π_i≠j(1−x_i/x_j)^a_i，正a,b,c时Lagrange identity Σ_i Π_j≠i(1−x_i/x_j)^−1=1给D(a,b,c)=D(a−1,b,c)+D(a,b−1,c)+D(a,b,c−1)。零边界先对相应x_i取CT，剩余两变量Vandermonde为(b+c)!/(b!c!)。唯一归纳解是(a+b+c)!/(a!b!c!)。a=b=c时令x=x1/x2、y=x2/x3，product是(−1)^(3a)x^−2a y^−2a(1−x)^(2a)(1−y)^(2a)(1−xy)^(2a)。取CT、shift k−a即得到cube sum。全为整数多项式身份，可以在15r<p处合法modp且无p阶乘分母。

但是

\[
\boxed{B_0=\frac{(-1)^{r+1}}{2[(10r)!]^3}
\left\{\frac{(15r)!}{[(5r)!]^3}
 +\sum_{k=1-r}^{r-1}(-1)^k\binom{10r}{5r+k}^{3}\right\}.}
\tag{Z19}
\]

固定middle的incomplete cubic sum仍保留。Z18 fullunit不是B0unit，更不是M5unit。

另两个真实scalar种子准确为

\[
A_j=w_0^5\left\{0^{2j}
 +2\sum_{k=1}^{r-1}k^{2j}h_k^5
 +\sum_{k=r}^{a}k^{2j}h_k^5\right\},\quad j=0,1,
\tag{Z20}
\]

其中0^0按常数f0=1解释。它们是指定fixed-parameter第五幂partial hypergeometric值；没有从Gosper operator invertibility推其非零。

## 8. 真实临界det的三scalar polynomial，不偷换generic值

对每个u-monomial product，Z8给唯一g,c；用Z15–17构造显式矩阵

\[
\mathcal M_{r,p}(A,B,C)=
\begin{pmatrix}A\,G^{(0)}+B\,G^{(1)}+G^{bdry}&C^{bdry}\\
(C^{bdry})^t&C\,H^{(0)}+H^{bdry}\end{pmatrix}.
\tag{Z21}
\]

全部coefficient matrices由unit triangular算子与known factorial endpoints准确给出。定义

\[
\mathcal P_{r,p}(A,B,C)=\det\mathcal M_{r,p}(A,B,C).
\tag{Z22}
\]

则

\[
\boxed{\det M_5=\mathcal P_{r,p}(A_0,A_1,B_0).}
\tag{Z23}
\]

总degree≤4r，A/B的combineddegree≤r，Cdegree≤3r，因为这些variables只出现于对应r或3r diagonal block。没证明此polynomial generically非零，也不需要它先可逆来定义；更没有将任意generic (A,B,C)代替实际Z19/Z20。

**本轮实际减少的未知量**是从全部4r阶矩阵entries，归约到三个完全指定初始算术scalars及全显式boundary系数。下一nonzero定理要在真实Z19/Z20处证明Z22不为0。

本轮另实际全文读root的NEW [single bordered gate稿](cdt_odd_paired_single_bordered_nonzero_gate_20261006.md) B1–B8，逐核其两个ambient-unit Schur、det比例及退化strong块的Smith论证。其B9严格给原p^(17m)D_A(X)的whole-X reduction=known unit·detM5，即使G0奇异亦成立。因此M5unit在无穷辅助p上足以给每个fixed rational candidate的无限D_A非零，G0unit不是这个归一化leading gate的额外要求。这并不声称M5unit是D_A非零的必要条件：该稿B11另给真正higher-layer最大Smith指数≤2时的替代充分条件，当前actual higher-layer条件仍未证。本稿不重建global整格/Smith费用，也不执行root程序或冒用其primary阅读。

## 9. Hasse/finite-hypergeometric文献为何尚不替代固定值证明

NEW实际读Adolphson–Sperber：其Hasse invariant是明确exponential-sum family最低valuation的coefficient，非零polynomial与某个固定specialization非零是两个statement；Theorem6.6用其固定A、e和minimal digit profiles构造sum-of-products。当前Z19/Z20和Z22尚未构造这种同一个fixed exponential-sum/cohomological family的合法比较，不能叫作已经识别的Hasse invariant。

即使将来有该比较，ordinary specialization也须另证。例如其PDF1 Legendre Hasse polynomial Σ_(i=0)^h binom(h,i)^2 λ^i，h=(p−1)/2；当p≡3mod4时h odd，在λ−1把i与h−i配对即全相消。这一全尺度算术例子说明fixed rational parameters和nonzero Hasse polynomial不能自动排除fixed badvalue，不是当前M5反例。

真实maskχ在degree<N的CRT代表中被O=P/M整除，degO=4r+1；χ非零，故degχ≥4r+1。这严格排除把actual middle indicator直接写成p-independent bounded-degree polynomial的捷径。它不排除另一个高维/motivic表达或新的独立周期，范围只是这个真实node空间的直接polynomial mask。

Gosper原文的polynomial certificate定理有shifted gcd及characteristic-zero度数分析；这里Z5–17另自证modp cutoffs、resonance和真实boundaries。没有将其印刷算法定理免费转成无限辅助prime上的normality。

## 10. Primary归档、准确阅读与执行边界

正常verified TLS新增2份独立原件：

- Gosper1978《Decision procedure for indefinite hypergeometric summation》，[Rutgers保存原件](https://sites.math.rutgers.edu/~zeilberg/akherim/gosper1978.pdf)，3页，实际PDF1–3完整文本读取。Eq8 polynomial certificate、degree resonance与division-by-zero caveat实际读；纸面finitefieldZ5–17自证，不直接套printed gcd theorem。
- Adolphson–Sperber《Hasse invariants and mod p solutions of A-hypergeometric systems》，[arXiv1209.2448v1](https://arxiv.org/pdf/1209.2448v1)，22页，实际PDF1–7及14–17，11distinct页；PDF1 Legendre，PDF2 Eq1.2/1.3，PDF3normalized与unnormalized系统区别，PDF4–7 good/verygood profiles及modp bases，PDF14–17 digit decomposition与Theorem6.6实际读。未称读剩余11页。

新增archive25页，author实际14distinct页；没有archive外部源码/HTML，没有证书bypass。新receipt另存准确URL/hash。

NEW同stem_verify.py完整静态读后，exclusive-create guard在数学开始前保存first state；首次且唯一1run exit0 PASS。仅旧已考察r1/2/4，75个全critical moment身份，threeoperators反射/leadingunit/唯一分解及Dixonfullunit验证；不扩auxprime表、不计算或assert M5nonzero。源SHA4b6dce00c79c0d26d89a418af05966d8f8a7ada32b00ce636c9de20b6576b012，成功PY/JSON保持冻结，不重跑。

## 11. 已证、未证与具体下步

已证：固定原λ2的三种真实weights有allscale临界Gosper decompositions；cross全部moments显式双boundary；G/H高阶矩只需两个/一个实际种子；full cubic Dixon unit与真实incomplete middle精确分离；M5准确成为三个指定scalars的determinant polynomial。所有degree profile、χ、halfjet、first denominator pole均保留。

未证：Z23在无穷p上非零；global rational-specialization infinite nonzero；新的allplace模型与arch费用；strict margin或新ζ/L特殊值定理。三个初始scalars不是genericλ，也没有可免费选择的目标归一化。

下一具体门槛是求Z22在Z19/Z20真实值处的防相消身份，或构造保持两个cutoffs的合法Hasse/cohomological比较并证明ordinary primes。另一方向可用D5/D−3的triangular certificates直接研究M5核，由唯一分解把degree equations化为三个fixed scalar值的约束；不能通过假定所有中间Hankel正常来完成这一步。
