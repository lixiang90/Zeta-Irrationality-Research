# 高 weight double-pole 目标投影、primitive 整化与真实格费用

日期：2026-10-06。NEW 全尺度纸面推导，quarter_actual_rank。旧/同行 MD、PY、JSON、manifest全部只读；未执行、import或重跑任何旧或同行 producer。本稿没有数学 producer、数值搜索或外部 Lean执行。root负责全素数安全费用，arithmetic负责content，toric负责解析比较；本文负责三者必须共同使用的实际 normalization/格接口。

## P1. 实际输入与一手原页

本轮实际全文重读冻结 [mixed稿](cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md) H1–H9，SHA **e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463**；以及冻结 [独审](cdt_odd_mixed_zeta_character_hankel_independent_review_20261006.md) J1–J7，SHA **dfa064d0ddf9361ae48da4fd95e7b8c7816f3d459b4ccb861a679ac53291fe79**。两份全文输出无截断，SHA重新核对吻合。

本轮实际读取 Lai PDF **7–14、17–19**（11页，不称全文25页）：literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf，SHA **838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58**。PDF7–11明确 binomial basis、residue-class minors、factorial normalization；12–14是 prime summation；17–19是 Proposition5.5与 contour-shift/triple-zero关键步骤。此前轮次1–7、20–23的阅读不冒认本轮又全读。本文没有新PDF下载；normal TLS acquisition由既存root来源收据固定。

## P2. Double-pole family确实投影到单一目标

固定 \(s\ge4,r\in\mathbf Q\)，令 \(\xi=\zeta(s)-r\zeta(s-1)\)。先用原布局
\[
R_n(t)=\frac{(6n)!^2}{(2n)!^3}\,
\frac{S_{2n}(t)^3}{(t)_{6n+1}^2},
\qquad S_{2n}(t)=\prod_{m=1}^{2n}(t-m),\quad h=3n.
\]
设 \(W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3\)，
\(C_j=5H_j-3H_{2n+j}-2H_{6n-j}\)。在 H9 rational form 中实际代入 **a=−r、b=1、c=X**：
\[
U_j=(s-1)r(s-3)!H_j^{(s-2)}-(s-2)!H_j^{(s-1)},
\]
\[
V_j(X)=C_jU_j+(s-1)![X+rH_j^{(s-1)}-H_j^{(s)}].
\]
定义
\[
B_{n,s,r,X}(P,Q)=\sum_{j=0}^{6n}W_j
\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
C_{n,s,r}(X)=
\frac{\det[B_{n,s,r,X}(t^i,t^j)]_{0\le i,j<h}}
{\prod_{i=0}^{h-1}i!^2}\in\mathbf Q[X].
\tag{P1}
\]
H9 partial fraction身份是实际目标投影：
\[
B_{n,s,r,\xi}(P,Q)
=(-1)^{s-3}(-(s-1)r)\sum_{m\ge1}(R_nPQ)^{(s-3)}(m)
{}+(-1)^{s-2}\sum_{m\ge1}(R_nPQ)^{(s-2)}(m).
\tag{P2}
\]
不需要额外独立目标或一个未经证明的 period comparison。a,b,c的全整数版本仅需清固定 r和候选有理\xi分母；整体 fixed factor D的 h次方只贡献O(n)，不能与 n-dependent lattice混同。

P1中X的系数矩阵是
\[
(s-1)!\sum_jW_j\,v_jv_j^{\mathsf T},
\qquad v_j=(1,-j,\ldots,(-j)^{h-1})^{\mathsf T}.
\]
它在实数域正定：W_j>0，非零次数<h polynomial不可能在6n+1个nodes全部为零。因此 \(\deg C_{n,s,r}=h\)，最高系数正，非零性是实际的。但 polynomial非零不等于每个 rational v有无穷次 nonzero evaluation；后者由P4补。

## P3. Normalization与格基不能创造 strict margin

设C非零有理polynomial，取唯一正 d使P=dC是primitive整数polynomial且保持正比例方向。若整体乘正有理 \(c_n\)，则同一个primitive P的 multiplier变为d/c_n。因此
\[
\log(d/c_n)+\log|c_nC(\xi)|
=\log d+\log|C(\xi)|.
\tag{P3}
\]
若 \(\log c_n=\gamma n^2+o(n^2)\)，清分母预算A和衰减预算B同时变为A−γ、B−γ，strict margin B−A完全不变。仅改变normalization不能改善判据。

对basis transformation \(A_n\in\operatorname{GL}_h(\mathbf Q)\)，Gram矩阵congruence给det乘 \((\det A_n)^2\)。如果还是同一空间、同一form，则这是P3的整体factor；其 primitive polynomial和真正margin不变。按local lattice使用 \(A_n\in\operatorname{GL}_h(\mathbf Z_p)\) 时，所有minor ideals与Smith exponents均不变。Non-unimodular n-dependent A_n确可移走表面分母，但必须支付它的index与相应archimedean determinant factor。

P1的factorial除数是 actual binomial lattice
\[
\mathcal M_h=\sum_{i<h}\mathbf Z\binom ti,
\]
其basis transition diagonal是1/i!。Lai PDF7明确这一点。它不是任意后加的正规化；prime-by-prime与real estimate必须评价同一个 normalized determinant。新增subspace则不是整体factor，必须重新证明其rank、nonvanishing、arithmetic rows与energy。

## P4. H9辅助素数上精确的内容、全部minor与primitive reduction

取 \(n=2m,\ p=9m+1\) prime，\(p>s+1\) 且p不除r分母。令q=3m，h=2q=6m<p。用H9未缩放Hermite basis
\[
E_k=(1-2c_k(t+k))F_k^2,\quad F_k^{\rm jet}=(t+k)F_k^2,\quad
0\le k<q,
\]
其中H9的Lagrange F_k满足node values，\(c_k=F_k'(-k)\)。此basis在 \(\mathbf Z_p[t]_{<h}\) 上 **unimodular**：confluent Vandermonde determinant是nodes differences的四次幂乘积，全部为p-unit。H9 scaled basis则是 \(p^2E_k,pF_k^{\rm jet}\)，其transition T determinant满足
\[
v_p(\det T)=3q=9m.
\tag{P4}
\]
必须区分这两个bases。

在任意 \(X\in\mathbf Z_p\) 上，H9纸面Taylor与所有off-block errors给未缩放Gram blocks
\[
p^sB_{EE}\equiv-(s+1)u\,D,\quad
p^{s-1}B_{EF}\equiv su\,D,\quad
p^{s-2}B_{FF}\equiv-(s-1)u\,D\pmod p,
\tag{P5}
\]
其中 \(u=(s-2)!\) 为unit，\(D=\operatorname{diag}(W_{p+l})\) unit diagonal。这里X项在 reduction中消失；coefficients作为 \(\mathbf Z_p[X]\) polynomial同样成立。

因 \(s+1\) 是p-unit，B_EE的inverse乘B_EF属于p Mat_q(Z_p)。Integral Schur elimination因此是unimodular congruence；其FF block leading coefficient为
\[
-(s-1)uD-\frac{s^2u^2D^2}{-(s+1)uD}
=\frac{u}{s+1}D,
\tag{P6}
\]
是unit。（符号为正；只论unit也须保留真实计算。）所以 actual Gram的Smith exponents准确是
\[
\boxed{\underbrace{-s,\ldots,-s}_{q},
\underbrace{-(s-2),\ldots,-(s-2)}_{q}.}
\tag{P7}
\]
相同结论适用于binomial lattice，因为h<p时所有i!是p-unit。其k阶minor ideal valuation为
\[
\mu_k=
\begin{cases}
-sk,&0\le k\le q,\\
-sq-(s-2)(k-q),&q\le k\le h.
\end{cases}
\tag{P8}
\]
这里是完整minor ideal的精确结论，非只看某个entry或一个upper bound。

H9也给 \(p^{s-4}B(T,T)\in\operatorname{Mat}_h(\mathbf Z_p[X])\)，modp是constant block diagonal unit。于是det polynomial的Gauss valuation准确为
\[
\boxed{v_p^{\rm Gauss}(C_{2m,s,r})=-h(s-1)=-3n(s-1),}
\qquad
p^{h(s-1)}C_{2m,s,r}\bmod p
\text{是非零常数}.
\tag{P9}
\]
换算必须用P4的 \((\det T)^2\)，不能只用scaled form的unit determinant而宣布原det integral。

取globalprimitive \(P_{n,s,r}=d_nC_{n,s,r}\)。Primitive意味着每个p的coefficient min valuation为0，故在上述p上必有
\[
v_p(d_n)=h(s-1),\qquad
P_{2m,s,r}\bmod p=\text{非零常数}.
\tag{P10}
\]
Dirichlet给无穷p≡1mod9；对每个fixed rational v再避开其分母，即 \(P_{2m,s,r}(v)\ne0\)。因此 **single-target double-pole primitive family的无限nonzero evaluation条件已补**。不将它转移给H4 simple-pole布局。

真实费用比较：s=4在此p的det指数为−9n；s=5为−12n；s=7为−18n。Uniform entry p^s费用到det可省h个p指数，但这项saving各weight相同。s5相对s4额外3n的指数是不可避免的actual denominator/content费用，不可由unimodularbasis或primitive消去。单一auxiliary p只产生O(nlogn)，尚不能据此推出一个n²费用下界或strict margin失败。

## P5. 全素数minor转移的正确方向

Lai PDF8–11的residue decomposition可以重新自证到fixed s，而不是沿用数字30.83。对 \(p>\sqrt{8n}\)，设
\[
q_\rho=\left\lfloor\frac{6n-\rho}{p}\right\rfloor,\quad
w_\rho=2\left\lfloor\frac{6n}{p}\right\rfloor
-2\left\lfloor\frac{6n-\rho}{p}\right\rfloor
{}+3\left\lfloor\frac{2n+\rho}{p}\right\rfloor
-3\left\lfloor\frac{2n}{p}\right\rfloor .
\]
对于tail j=ρ+ℓp、ℓ≥1，harmonics给
\(v_pU_j\ge-(s-1),v_pV_j\ge-s\)；head j=ρ<p给
\(v_pU_\rho\ge0,v_pV_\rho\ge-1\)。若p同时大于6n−ρ和2n+ρ，head V也integral。Tail sum rank≤2qρ，head rank≤2。按translated monomialbasis和Cauchy–Binet重复Lai证明，m阶minor有安全下界
\[
F_{s,\rho}(m)=m^2+(w_\rho-s-1)m
{}+(s-1)\max(0,m-2q_\rho)
{}+\mathbf1_{m=1}\mathbf1_{p>\max(6n-\rho,2n+\rho)}.
\tag{P11}
\]
准确差是
\[
F_{s,\rho}(m)-F_{4,\rho}(m)
=-(s-4)\min(m,2q_\rho).
\tag{P12}
\]
Factorial normalization完全相同，不能按s随意更换。P11/P12是实际安全valuation **lower bound** 的变化，不是actual determinant分母 **lower bound**；possible cancellations只会使actual valuation更大。将其prime-sum积分误当不可改善费用，会反向使用不等式。

Lai Proposition5.5还利用 \(\log|J|=\sum_pv_p(J)\log p\) 的rational product formula，positive finite valuations亦有作用。Primitive polynomial的coefficient-clearing费用、specialized rational value的reduced denominator、整个finite valuation和不是同一个量。可用P9给真下界，但不能从P11优化出来的坏upper cost声称任何改进都不可能。

## P6. s5沿原右轮廓有真实rank2n修正

Lai PDF17–18将 contour放在 \(\Re z=2n+1/2\)，是因为其weight4只用一、二阶导数，而R在m=1..2n具有三重zero。对s5 target，实际P2为
\[
L_{n,5,r}(P)=-4r\sum_{m\ge1}(R_nP)''(m)
-\sum_{m\ge1}(R_nP)'''(m).
\]
令 \(L^{>2n}\) 为同式只sum m≥2n+1。Exact split是
\[
L_{n,5,r}(P)=L^{>2n}_{n,5,r}(P)
-\sum_{m=1}^{2n}R_n'''(m)P(m).
\tag{P13}
\]
Second derivative head为0，third不为0。写 \(K=(6n)!^2/(2n)!^3\)，
\[
d_m=(m)_{6n+1},\quad
R_n'''(m)=
6K(-1)^m\frac{[(m-1)!(2n-m)!]^3}{d_m^2}\ne0.
\tag{P14}
\]
在dim3n的polynomialspace中，finite-head Gram为
\(-\sum_{m\le2n}R_n'''(m)\mathrm{ev}_m\otimes\mathrm{ev}_m\)，rank准确2n。Evaluation map到Q^{2n}满射，diagonal各项非零，因此rank没有额外取消。它是随n线性增长的修正，不是换fixed kernel产生O(n)的无关常数。

所以“fixed higher derivativekernel只改解析bound O(n)，便继承Lai同一energy”在原布局s5不成立：所得contour控制tail determinant，而actual determinant还含P13。这是一项已证真实comparison障碍；不等于已证actual determinant不衰减。

## P7. 两个合法head-free subspace及其费用

最直接的subspace是 \(P=S_{2n}A,\deg A<n\)，dimension n。对products PQ，R_nPQ有五重zero，所以s5的second/third head均0。其target determinant仍是rational单目标polynomial，且X-leading Gram正定，degree准确n。但full H9 form nondegenerate不推出该restricted rational v有无穷nonzero；其new energy/rank/content须另证明，不能称原h3n预算。

还有一个保留dimension2n的actual rational candidate。配对m与m′=2n+1−m；P14的factorial numerator相同、sign相反。故取
\[
\mathcal A_n=
\{P\in\mathbf Q[t]_{<3n}:
P(m)/d_m=P(m')/d_{m'},\ 1\le m\le n\}
\tag{P15}
\]
让每对head bilinear恰相消。n个条件独立：full evaluation map到2n个nodes满射，而每对条件只涉及该对两坐标。因此dim A_n=2n，整个P13 correction在A_n×A_n上为0。它是finite-head nondegenerate rank2n部分上的maximal isotropic选择（加n维evaluation kernel），不是仅消掉一个vector。

相应X-leading Gram仍positive definite，target determinantdegree准确2n。但下列是未经gcd约除的整数约束行；若要取primitive rows，必须除去各行的实际gcd，并另核整个约束格的saturation：
\[
d_{m'}P(m)-d_mP(m')=0
\tag{P16}
\]
随n变；arithmetic descent本身合法，height、integral saturation、实际basis和nonzero却没有免费获得。例如第一对
\[
d_{2n}/d_1=\binom{8n}{2n-1},
\quad
\log(d_{2n}/d_1)
=(16\log2-6\log3)n+o(n).
\tag{P17}
\]
这是一个实际row的线性n height，不是fixed-coefficient cancellation。累积n个约束与archimedean基范数必须记账。本稿未将P15的raw row height当作已证总lattice determinant费用，更未声明其margin成功或失败。

## P8. 增加真实zero order的通用布局与nonzero证明

root提出的另一个实际修复无需restriction：取integer \(k\ge3,B>k\)，
\[
R_{n;k,B}(t)=\frac{(Bn)!^2}{(2n)!^k}
\frac{S_{2n}(t)^k}{(t)_{Bn+1}^2},
\quad h=(B-k)n.
\tag{P18}
\]
对degPQ<2h，R_nPQ在∞度数≤−3，故simple-coefficients sum为0；single-target P1/P2全部成立，改用
\[
W_j=\binom{Bn}{j}^2\binom{2n+j}{j}^{k},\quad
C_j=(k+2)H_j-kH_{2n+j}-2H_{Bn-j}.
\]
它有实际zero order k，若 \(k\ge s-1\)，则最高导数s−2的finite head全消，实际series等于tail。新h、新R的energy与all-place预算必须重新做。

**通用nonzero lemma。** 固定s≥4、r∈Q、k≥3、B>k。取 \(n=2m,\ p=(B+k)m+1\) prime，p>s+1且不除r分母。令 \(q=(B-k)m\)，h=2q。Tail j=p+l恰0≤l<q。所有upper limits<2p，且Bn−j<p；所以H_j⁽ᵛ⁾=p⁻ᵛ+integral、C_j leading \((k+2-k)/p=2/p\)。Lucas给
\[
\binom{2Bm}{p+l}\equiv\binom{q-1}{l},\qquad
\binom{4m+p+l}{p+l}\equiv\binom{4m+l}{l}\pmod p.
\]
右边factorials全部<p：\(4m+l\le(B-k+4)m-1<p\)因为k>2。因此W_j unit。Head j<p按P4同样给scaled integral errors。q个Hermite pairs的differences<p，H9完整Taylor/error proof照样给
\[
p^{s-4}B(T,T)\bmod p
=\operatorname{diag}_l\!
 \left[(s-2)!W_{p+l}
\begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix}\right].
\tag{P19}
\]
所有blockdet是unit，故full target polynomial在这些auxiliary primes具有nonzero constant reduction并有infinite nonzero rational evaluations；Dirichlet用于p≡1mod(B+k)，gcd为1。

精确normalization必须另付：未缩放Hermitebasis的Smith exponents仍是q个−s和q个−(s−2)，monomialdet Gauss valuation为−h(s−1)。但**只有B≤3k时h<p，factorials为unit**。一般B>3k有h<2p而h可能≥p，所以
\[
v_p\!\left(\prod_{i<h}i!^2\right)
=2(h-p)_+,
\]
\[
\boxed{v_p^{\rm Gauss}(C_{2m,s,r;k,B})
=-h(s-1)-2(h-p)_+.}
\tag{P20}
\]
Multiplying by the corresponding positive p-power仍给constant unit reduction，故primitive/nonzero结论不受影响；费用却不能省略。此项是本独审发现的general B normalization gate。

特别s5取k4、B6给h2n、p10m+1；k4、B8给h4n、p12m+1，二者B≤3k，factorialsunit，zero order4严格足以移除third-derivative head。这是真实可继续比较的新布局，而非换normalization。但单一auxiliary-p结论与zero-order修复还不足以给新的数值定理。

## P9. 本轮已补的判别与未完成部分

已证：

1. Double-pole布局的actual单目标primitive polynomial，degree精确h；辅助素数上primitive reduction为非零常数，因此无限nonzero rational evaluations成立。
2. 原布局auxiliary-p的全部Smith/minor valuations精确可算，s5增加的真实分母指数为3n；scalar normalization/non-unimodular basis不能免费制造margin。
3. 全s residue-minor安全估计的正确差P12；它的prime integral不是actual费用下界。
4. 原s5存在exact rank2n的finite-head修正，S-restriction及paired dimension2n subspace确实消除该修正，但各自新费用/nonzero还需核。
5. General k,B layout恢复足够zero order，同时保留通用unit-block nonzero；B>3k的factorial费P20不可漏。

尚缺 matched strict inequality：新布局的全部prime估计、primitive/content可省费用、与同一normalized determinant相匹配的real energy。当前这些正面lemma没有证明新的ζ/L/Catalan无理性、线性无关性或Lean定理，未声明任何primitive预算已经达到strict margin。作者完成全文回读与独审后本NEW稿才冻结；root main/delivery/audit由root负责。
