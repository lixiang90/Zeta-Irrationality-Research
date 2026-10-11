# 混合 ζ 双极点布局：完整解析衰减、有限头项与正确轮廓

日期：2026-10-06。NEW 全尺度纸面证明。旧/同行数学稿、PY、JSON 与 manifest 均只读，数学 producer 的执行、import、重跑为0。本稿直接研究冻结 [mixed 稿](cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md) H9 的 double-pole 布局，没有将 H4 的 simple-pole bound 移植到此处。

**实际结论。** 每个固定整数 s≥4、固定 a,b∈Z、b≠0，都有完整解析行列式的全 n 上界

\[
\boxed{|J^{\rm an}_{n,s}|\le C_{s,a,b}^{3n}\,3^{-9n^2},\qquad n\ge1,}
\tag{D1}
\]

其中 C>0 是显式固定常数。故严格 n² 衰减主项至少为 `9 log 3`；fixed derivative order 在这个**安全完整轮廓界**中只付 O(n)。s=5 不能直接继承 Lai 的右移轮廓：实际出现 exact-rank-2n 的非零离散头项。本稿同时给出其正确 mixed Heine 展开。尚未证明 arithmetic cost 小于 `9 log 3`，也未证明原布局 s=5 的最佳 decay constant 与 Lai weight4 相同。因此没有新的特殊值无理性或线性无关性结论。

## A1. 真实对象及“有理行列式”的识别条件

固定

\[
R_n(z)=\frac{(6n)!^2}{(2n)!^3}
\frac{\prod_{m=1}^{2n}(z-m)^3}{\prod_{j=0}^{6n}(z+j)^2},
\qquad h=3n,
\qquad F_h=\prod_{j=0}^{h-1}j!^2.
\tag{D2}
\]

在 `deg P<6n` 上定义实际解析泛函

\[
L^{\rm an}_{n,s}(P)=(-1)^{s-3}(s-1)a
\sum_{m\ge1}(R_nP)^{(s-3)}(m)
+(-1)^{s-2}b\sum_{m\ge1}(R_nP)^{(s-2)}(m),
\]
\[
J^{\rm an}_{n,s}=F_h^{-1}
\det[L^{\rm an}_{n,s}(z^{i+j})]_{0\le i,j<h}.
\tag{D3}
\]

degree 条件保证 `deg(R_nP)≤−3`，全部 fixed-order derivative series 绝对收敛。D1 是这个真实 analytic determinant 的 bound，不需假设 aζ(s−1)+bζ(s)=c。

冻结 H9.3 定义的 rational form 另包含整数 c。只有在候选关系

\[
a\zeta(s-1)+b\zeta(s)=c
\tag{D4}
\]

成立时，H9 的 exact partial fraction identity 才识别 `J^rat=J^an`。本稿绝不将 D1 赋给任意虚构 c 的 rational form。H9 的无穷非零子序列属于独立算术证明，不来自正性；本稿没有重复或更改该证明。

## A2. Fixed-order periodic Cauchy kernels：全部正整数的正确积分

令 `q(z)=π cot(πz)`，并定义

\[
K_s(z)=-(s-1)a q^{(s-3)}(z)-b q^{(s-2)}(z).
\tag{D5}
\]

整数 m 附近 q 的唯一 principal part 是 `(z−m)^{-1}`，所以对任何在 m 全纯的 f，

\[
\operatorname{Res}_{z=m}f(z)q^{(d)}(z)=(-1)^d f^{(d)}(m).
\tag{D6}
\]

因此 K_s 的 residue 是 D3 的对应 summand 的负值。取左边向上的 clockwise rectangle，左边 `Re z=1/2`、右边 `Re z=T+1/2`、上下边 `Im z=±T`，T 为足够大整数。d≥1 时 q^(d) 在上下边为 `O_d(e^{-2πT})`，在右边为 `O_d(e^{-2π|Im z|})`；f=R_nP 的 degree≤−3。上下及右边积分均趋0，绝对收敛的 residue sum 可取极限。获得

\[
\boxed{L^{\rm an}_{n,s}(P)=\frac1{2\pi i}
\int_{1/2-i\infty}^{1/2+i\infty}R_n(z)P(z)K_s(z)\,dz.}
\tag{D7}
\]

这是包含全部 m≥1 的完整积分。s=4 时 D5 是 Lai Lemma6.1 的 kernel `π² csc²(πz)(3a−2bπcot(πz))`；本例 s=5 时则是 `−4a q''−b q'''`。这些 identity 的符号由 clockwise contour 与 D6 两次负号确定。

## A3. 原布局在左直线上的精确正包络

记 `u_m=binom(2m,m)/4^m`。半整数阶乘产品直接给

\[
R_n(1/2)=\frac{u_{2n}^3}{(6n+1/2)^2 u_{6n}^2}>0.
\tag{D8}
\]

因为 central binomial coefficient 是全部2m+1个 binomial coefficients 的最大值，其和为4^m，故

\[
\frac1{2m+1}\le u_m\le1.
\]

D8 随即给 `R_n(1/2)≤4`：`(12n+1)/(6n+1/2)=2`。这个弱而精确的上界对所有 n≥1 成立，不依赖 Stirling 数值误差。

对任意 x∈R，原 rational product 中的相同半整数 factors 消去，得到

\[
\frac{|R_n(1/2+ix)|}{R_n(1/2)}=
\frac{\prod_{j=0}^{2n-1}(1+x^2/(j+1/2)^2)^{1/2}}
{\prod_{j=2n}^{6n}(1+x^2/(j+1/2)^2)}
\le\sqrt{\cosh(\pi x)}\le e^{\pi|x|/2}.
\tag{D9}
\]

使用的 classical Euler product 是 `cosh(πx)=∏_{j≥0}(1+x²/(j+1/2)²)`，其 factors≥1，故从有限 product 到 infinite product 的不等式方向明确。于是

\[
\boxed{|R_n(1/2+ix)|\le4e^{\pi|x|/2}\quad(n\ge1,x\in\mathbf R).}
\tag{D10}
\]

该包络专门由此 double-pole 布局及其 factorial normalization 得出，没有 simple-pole 输入。

## A4. Higher derivatives 只在完整左轮廓付固定常数

定义整系数 polynomials

\[
p_0(u)=1,\qquad
p_{k+1}(u)=-2u p_k(u)-(1+u^2)p_k'(u),
\quad M_d=\max_{v\in[-1,1]}|p_{d-1}(-iv)|.
\tag{D11}
\]

由 `q'=−(π²+q²)` 归纳得 `q^(d)=q' π^{d−1}p_{d−1}(q/π)`。在 Re z=1/2 上，`q(z)=−iπ tanh(πx)`、`|q'|=π² sech²(πx)`，从而

\[
|q^{(d)}(1/2+ix)|\le4\pi^{d+1}M_d e^{-2\pi|x|}.
\]

令

\[
D_{s,a,b}=(s-1)|a|\pi^{s-2}M_{s-3}
+|b|\pi^{s-1}M_{s-2},
\qquad C_{s,a,b}=\frac{16}{\pi}D_{s,a,b}.
\tag{D12}
\]

固定 s,a,b 时，这些是有限固定常数；b≠0 确保 D>0。将 D10 与 K_s bound 合并，真实 moment density

\[
\omega_{n,s}(x)=\frac1{2\pi}R_n(1/2+ix)K_s(1/2+ix)
\]

满足

\[
\boxed{|\omega_{n,s}(x)|\le
\frac{8D_{s,a,b}}{\pi}e^{-(3\pi/2)|x|}.}
\tag{D13}
\]

对 s=5，p₁=−2u、p₂=2+6u²，故 M₂=2、M₃=4；可用显式

\[
\boxed{C_{5,a,b}=128\pi^2|a|+64\pi^3|b|.}
\tag{D14}
\]

不需要对 R_n 直接求高阶导数再粗付 n^d：全部 derivatives 已合法转移到固定 periodic kernel，而全部正整数 residues 都保留在 D7 中。

## A5. Reference integral 的完整自证与 n² bound

令 `w(y)=sech(πy)`。Classical beta integral（代换 u=e^(2πy)）给

\[
\int_\mathbf R w(y)e^{ty}\,dy=\frac1{\cos(t/2)},\qquad |t|<\pi.
\tag{D15}
\]

定义 polynomials P_k(y) 的 generating series

\[
\sum_{k\ge0}P_k(y)z^k=(1+z^2)^{-1/2}e^{2y\arctan z}.
\]

对小的 real z,w，D15 给两个 generating series 的积分为 `1/(1−zw)`。其系数积分可以逐项求导：在固定小邻域内被 integrable exponential envelope 控制。于是 `∫P_jP_k w=δ_jk`，且 leading coefficient 是 `2^k/k!`。

有限 determinant 展开与 Fubini 给 Heine identity，不要求 measure 正；若只用于正 reference，得到对任意整数 h≥1、c>0 的精确 integral

\[
\boxed{\frac1{h!\prod_{k<h}k!^2}
\int_{\mathbf R^h}\Delta(\mathbf x)^2
\prod_{i=1}^h\operatorname{sech}(cx_i)\,d\mathbf x
=2^h\left(\frac\pi{2c}\right)^{h^2}.}
\tag{D16}
\]

具体而言，orthonormal P_k 的 triangular leading coefficients 给 unscaled reference determinant `∏k!²/4^k`；代换 x=(π/c)y 付 `(π/c)^(h²)`，其中 h² 而不是 h 来自 Vandermonde 及 volume 共同 scaling。这也核对了 Lai Lemma6.5 的 normalization。

D7 的 measure 有 absolute integrable moments。其 Heine identity 中 `z_i−z_j=i(x_i−x_j)`，所以 absolute value 受正 Δ(x)² integral 控制；没有用 signed weight 的假正性。D13 与 `e^{-c|x|}≤sech(cx)`、c=3π/2 给

\[
|J^{\rm an}_{n,s}|
\le\left(\frac{8D_{s,a,b}}\pi\right)^h
2^h\left(\frac13\right)^{h^2}
=C_{s,a,b}^{3n}3^{-9n^2}.
\]

这证明 D1 对全部 n≥1 成立。特别

\[
\limsup_{n\to\infty}n^{-2}\log|J^{\rm an}_{n,s}|
\le-9\log3.
\tag{D17}
\]

零 determinant 取 log=−∞；本解析结论不保证 nonzero。固定 derivative 改变 C，却在这一完整包络界中仅增加 `3n log C=O(n)`，没有隐藏 O(n²) 或 O(n log n) 的 derivative fee。该 statement 不主张最优真实 decay exponent 不随 s 改变。

## A6. 右移 contour 的实际失败与 general jet replacement

右 contour 取 `q_n=2n+1/2`。同一 residue argument 给 tail functional `L^>_{n,s}`，其 series 只含 m≥2n+1。精确差是

\[
L^{\rm an}_{n,s}(P)=L^>_{n,s}(P)+H_{n,s}(P),
\quad H_{n,s}(P)=
(-1)^{s-3}(s-1)a\sum_{m=1}^{2n}(R_nP)^{(s-3)}(m)
+(-1)^{s-2}b\sum_{m=1}^{2n}(R_nP)^{(s-2)}(m).
\tag{D18}
\]

R_n 在每个这些 m 的零阶恰为3。所以 s=4 时 H=0，正是 Lai 的 Lemma6.1；s=5 时

\[
\boxed{H_{n,5}(P)=-b\sum_{m=1}^{2n}R_n'''(m)P(m).}
\tag{D19}
\]

并且实际非零值为

\[
R_n'''(m)=6\frac{(6n)!^2}{(2n)!^3}
(-1)^m\frac{(m-1)!^5(2n-m)!^3}{(m+6n)!^2}\ne0.
\tag{D20}
\]

对于 s≥5，Leibniz 展开将 H 写为2n个points的 jet functional，最高 P derivative order 为 s−5；其 coefficient 含 `(-1)^(s−2)b binom(s−2,3)R_n'''(m)`，非零。相应 bilinear form 的 rank 至多 `min(3n,2n(s−4))`。当 s≥6 时这个 bound 不再强制任何 contour factors 留下，故不能据旧 size3n contour proof 判断完整 determinant。

当 s=5，在 dimension3n 的 polynomial space 上，evaluation map到2n个 distinct m 是 surjective，而 D19 的全部2n weights 非零。因此 bilinear head form 的 rank **恰为2n**，不是只是一个粗 upper bound。

## A7. s=5 正确 mixed Heine 展开；至少 n 个 contour variables 的含义

令 `d_m=−bR_n'''(m)`，并取 right-contour density

\[
\omega^>_{n,5}(x)=\frac1{2\pi}R_n(q_n+ix)K_5(q_n+ix).
\]

在复 z 平面上，完整 moment measure 是 continuous right vertical line 与 finite atoms 的和

\[
d\mu=\omega^>_{n,5}(x)dx+\sum_{m=1}^{2n}d_m\delta_m.
\tag{D21}
\]

其所有所需 moments 绝对可积。展开 Heine identity，重复选择同一 atom 会被 Vandermonde 杀掉，因此得到 exact finite sector formula

\[
J^{\rm an}_{n,5}=\frac1{F_h}
\sum_{M\subset\{1,\ldots,2n\}}
\frac{\prod_{m\in M}d_m\,\Delta(M)^2}{(h-|M|)!}
\int_{\mathbf R^{h-|M|}}
\Delta(q_n+ix_1,\ldots,q_n+ix_{h-|M|})^2
\prod_{m\in M}\prod_i(q_n+ix_i-m)^2
\prod_i\omega^>_{n,5}(x_i)\,d\mathbf x.
\tag{D22}
\]

`Δ(empty)=1`。组合系数来自选择 |M| 个 slots 和各 distinct atoms 的排列：`binom(h,k)k!/h!=1/(h−k)!`。所以每个 sector 的 continuous variable 数 `h−|M|≥n`，与 exact-rank-2n 的 algebraic statement 一致。

但“至少 n 个 contour factors”**不等于**完整衰减仍为原 `−31.6 n²`：D20 的2n atom weights 与 D22 的 atom-atom/mixed Vandermonde factors 都贡献 n² 级 energy，不能只保留 tail kernel 的 exponential term。取 absolute values 给合法 positive-envelope sector sum，但尚未优化该 mixed energy。D1 已对整个 determinant 给出严格 bound，不依赖删掉这些 sectors 或假设相消。

## A8. 已核的 margin、尚未知的算术常数及合理新布局

严格可用的完整 analytic exponent 是

\[
B_{\rm safe}=9\log3=9.887510\ldots.
\tag{D23}
\]

decimal仅便于阅读；定理使用 exact `9 log3`。若在候选 D4 下实际 rational determinant 的全-place denominator/order sum另证明为

\[
\sum_p v_p(J^{\rm rat}_{n,s})\log p\ge-A_s n^2+o(n^2),
\qquad A_s<9\log3,
\]

则 H9 的无穷非零 subsequence 与 product formula、D17 给矛盾。当前没有证明这个 A_s；Lai weight4 的30.83既不适用于高weight，也远高于本安全 bound，不能将其当作已匹配的 margin。当前无理性 criterion 的已核 margin 是条件 `9 log3−A_s>0`，不是一个已知正数。

在**保持左 contour 不变**的体系中，固定 derivative order 仅改变 O(n) 项。尝试获得 Lai 更强的右 contour energy 时，s=5 已新增 n-dependent atomic measure，改变的对象可在 n² 层面起作用，不能只称为 O(n log n)。本稿没有证明最优 rate 下降，更没有以 upper bound 不够强证明目标不可能。

要从 contour identity 层面重新消去全部 head，可将 numerator zero multiplicity提高到至少 s−1。但若采用一般 layout `((z−Bn)_(Bn))^(s−1)/(z)_(An+1)^2`、size Cn，则绝对收敛至少需 `(s−1)B+2C≤2A`；A=6、B=2、C=3 在 s=5 已不满足。增大 A、减小 size 或改 numerator 后，partial fractions、all-prime cost、辅助素数 nonzero 和 energy 都属于 NEW 问题，不能继承 H9。

另一种严谨但尚未匹配费用的选择，是限制到被 head bilinear form 消去的 rational subspace。本稿只证明 `R_n P` 有足够额外 zeros 的明显子空间 dimension n；更大的配对 subspace 由同行另研究。此类 restriction 的 basis determinant、norm 和新的 nonzero 条件都须独立给出，不能将原 normalized3n Hankel bound 直接缩到2n。

## A8a. 恢复全部 zeros 的一般布局：独立全尺度 contour energy

下述是 NEW analytic candidate，尚未继承任何旧布局的算术或 nonzero theorem。固定整数 k≥3、B>k，令 s=k+1、d=B−k，定义

\[
R_{n;k,B}(z)=\frac{(Bn)!^2}{(2n)!^k}
\frac{\prod_{m=1}^{2n}(z-m)^k}{\prod_{j=0}^{Bn}(z+j)^2},
\qquad h=dn.
\tag{D24}
\]

其 degree为 `−2h−2`，故 degP<2h 时 R P 的 degree≤−3；所有 moment series 收敛。每个 m=1,…,2n 的 zero order 是 k，而最高 derivative 是 s−2=k−1，所以全部 head residues 确实为0。D7 可合法改成右 contour `Re z=2n+1/2`；该事实是此布局的直接证明，不是仅改 variable 后继续引用旧 Lemma6.1。

对 y≥0，定义

\[
\begin{aligned}
G_{k,B}(y)={}&(k+2)\log(y^2+4)
 -(B+2)\log(y^2+(B+2)^2)\\
 &+(k+2)y\arctan(2/y)-2y\arctan((B+2)/y)\\
 &+2B\log B-2k\log2 .
\end{aligned}
\tag{D25}
\]

y=0 取连续极限。以下 uniform product bound 对所有 n≥1、real x 成立：

\[
\boxed{|R_{n;k,B}(2n+1/2+ix)|
\le\frac{A_{k,B}}n\exp\bigl(nG_{k,B}(|x|/n)\bigr),}
\]
\[
A_{k,B}=\frac B{B+2}\pi^{1-k/2}
\exp\bigl(k/2+1/(6B)\bigr).
\tag{D26}
\]

给出 bound 的全尺度推导。令 g(u)=log(u²+y²)，u>0 上 increasing。Midpoint sums 的 elementary interval 比较给

\[
\sum_{m=1}^{2n}g((m-1/2)/n)
\le n\int_0^2 g(u)du+\log(4n)+1,
\]
\[
\sum_{j=0}^{Bn}g(2+(j+1/2)/n)
\ge n\int_2^{B+2}g(u)du+\log2+\log(B+2).
\tag{D27}
\]

第一式先以左端 midpoint 到2的 intervals 得 `sum≤n∫_{1/(2n)}²g+(1/2)g(2)`。利用 primitive `u log(u²+y²)−2u+2y arctan(u/y)`，被删去的小 interval 给附加项至多 `log(4n)+1`；所用比值 `(y²+4)/(y²+1/(4n²))≤16n²` 对全部 y≥0 有效。第二式将 `[2,B+2]` 分为两端半 interval 与中间全 intervals，以 increasing g 的右端值上估 integral，留下首末 sample 的各一半，其和至少 log2+log(B+2)。

用 elementary Stirling bounds

\[
\sqrt{2\pi m}(m/e)^m\le m!
\le\sqrt{2\pi m}(m/e)^m e^{1/(12m)}
\]

处理 `(Bn)!²/(2n)!^k`。将产品中的 n powers 分出后，factorial prefactor 为常数倍 `n^{−1−k/2}`，D27 的 numerator 附加项给 `4^{k/2}n^{k/2}e^{k/2}`，denominator endpoints 给 `2(B+2)`。剩余 exponential integral 直接等于 nG；逐项整理得到 D26 中的 A。因此没有依赖有限 n 拟合，也没有留一个未经说明的 uniform-in-x error。

直接求导得到

\[
G'_{k,B}(y)=(k+2)\arctan(2/y)
             -2\arctan((B+2)/y),
\]
\[
G''_{k,B}(y)=
\frac{2\bigl((B-k)y^2-(B+2)((k+2)(B+2)-4)\bigr)}
{(y^2+4)(y^2+(B+2)^2)}.
\tag{D28}
\]

G' 从 kπ/2 严格下降到一个 negative minimum，再上升到0 from below。因此，对任何 y*>0 使 `0<λ=G'(y*)<2π`，有全半轴的 tangent envelope

\[
G(y)\le c_1+\lambda y,
\qquad c_1=G(y_*)-y_*\lambda,
\qquad \kappa=2\pi-\lambda>0.
\tag{D29}
\]

证明是 G'(y)−λ 在 y* 前为正、之后始终负；不需要 G 在整个半轴 concave。

D12 的 derivative-kernel constant仍适用，因为 right contour 的 real part 是 integer+1/2。D26、D29 的 density bound 与 exact reference integral D16 给这个布局的完整 normalized determinant

\[
\boxed{|J^{\rm an}_{n;s,B}|
\le\left(\frac{4A_{k,B}D_{s,a,b}}{\pi n}\right)^{dn}
\exp(-\beta_{k,B}(y_*)n^2),}
\]
\[
\boxed{\beta_{k,B}(y_*)
=d^2\log(2\kappa/\pi)-d c_1.}
\tag{D30}
\]

这是给定 k,B,y* 下的严格 explicit exponent，正负均按该式判断。Fixed kernel fee 与 product prefactor仅为 O(n log n)，不会抹去 n² coefficient；新的 layout 确实改变 G、h 和该 coefficient。算术 lattice 与 nonzero 输入尚须另证，故 D30 只是匹配算术费用时可以真实使用的 analytic theorem。

## A8b. s=5 的 B=5、6、8：三个严格正 analytic candidates

对 k=4，可共用 y*=1。令

\[
\kappa_B=6\arctan(1/2)-2\arctan(1/(B+2)),
\]
\[
R_B=\frac{2^8((B+2)^2+1)^{B+2}}{5^6 B^{2B}},
\quad d=B-4,
\quad \beta_B=d\log R_B+d^2\log(2\kappa_B/\pi).
\tag{D31}
\]

此处 R_B 是固定正数，不是 rational function R_n。D31 是 D30 的 exact specialization，`R_B=e^{-c₁}`。所需 tangent hypotheses 真正成立：alternating arctan bounds 给

\[
\frac{69}{28}<\kappa_B<3\qquad(B\ge5),
\]

因为 arctan(1/2)>11/24、arctan(1/(B+2))≤1/7。于是 λ=2π−κ_B>0，κ_B>0；用 π<22/7 还给 `2κ_B/π>69/44>1`。

三个 exact choices 为：

| B | determinant size | R_B | strict analytic n² coefficient |
|---|---:|---:|---|
| 5 | n | `2^15/25` | `log(2^15/25)+log(2κ₅/π)` |
| 6 | 2n | `2^8 65^8/(5^6 6^12)` | `2log R₆+4log(2κ₆/π)` |
| 8 | 4n | `101^10/(5^6 2^40)` | `4log R₈+16log(2κ₈/π)` |

每个 R_B>1 可直接整数比较，故三个 β_B 都**严格为正**。例如 R₆=`256·65²·(13/36)^6>256·4225/729>1`，R₈>`5^14/2^20>1`。没有用 floating-point sample 将 β 声称为严谨界；表中 exact logarithm/arctan expression 就是 D30 的可审核 theorem。

匹配 criterion 分别是全-place arithmetic exponent `A_{5,B}<β_B`，并具有与该具体 size/normalization 相容的无穷 nonzero subsequence。当前本文未取得这些 arithmetic A。B6 是恢复 quartic zeros 后的 size2n choice，B8 为 size4n choice，B5 为 size n choice；它们的 nonzero/local blocks、factorial budget、prime ranges 都已改变。即使作者或同行另证明新 nonzero，也不能免费继承 old B6/k3/size3n 的30.83。

## A9. 原件阅读、推导与冻结范围

实际全文读 mixed H1–H9；实际读 [Lai 原件](../literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf) PDF1–7、17–25，共16页，尤其完整 Section6（PDF17–22）的 Lemmas6.1–6.5 和 Proposition6.6。原件25页、SHA256 `838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58`，由既存正常TLS来源收据固定，本轮不重新下载。PDF8–16 的完整 prime-by-prime proof 未本轮阅读，因而不登记其算术结果为独验。

Lai 的31.614…属于本文已读的 tail contour/orthogonal-polynomial computation；其 weight4 提供 H=0 条件，不能代替 s5 的 D18–D22。D7–D31、明确 C₅、全部 n≥1 界及 source-kernel differentiation 是本稿新增纸面证明；没有数值 Hankel 搜索、PSLQ、有限 n 拟合或数学 producer。恢复零阶的新布局由父任务提出参数后，本文独立证明完整 analytic interface，没有以尚未实际阅读的同行算术稿为已证输入。

本稿保存后实际全文回读、同行独审另存。NEW 来源收据记录 source/旧稿 pins、actual16页与数学执行0；旧数学稿和历史收据均不修改。没有新的 ζ、L 或 Catalan 无理性/线性无关性结论，也没有 Lean 验证。
