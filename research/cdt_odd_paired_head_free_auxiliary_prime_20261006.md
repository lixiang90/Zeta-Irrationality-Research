# 配对消头空间的辅助素数：真实 first jet、双矩阵判据与有限证据

日期：2026-10-06。NEW 数学稿，conifold_arithmetic_hypothesis。

本轮旧/同行数学 MD/PY/JSON/receipt 均仅读，执行、import、重跑为0。自有 NEW 探针只有首次1次执行，准确 scope 见 A12；它不是全部 m 定理。本文完成了真实限制形式的全尺度 block factorization，尚未证明其两个有限域 determinant 在无限辅助素数上同时为 unit，因而没有新的 ζ 数值无理性/线性无关性结论。

## A1. 实际对象与冻结输入

本轮实际全文重读冻结 research/cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md P1–P9，
SHA93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8。
其 paired space 是

\[
\mathcal A_n=\{P\in Q[t]_{<3n}:
 P(z)/d_z=P(z')/d_{z'},\quad1\le z\le n,\quad z'=2n+1-z\},
\quad d_z=(z)_{6n+1}.
\tag{A1}
\]

本文仅研究原三重零 R 的 actual restriction，不将它与 quartic-zero restored layouts 混合。实际整数值格是 M₃ₙ=⊕_{i<3n}Z binom(t−1,i)，A_Z=A_n∩M₃ₙ。同行 NEW saturated basis 提供此格的完整基、全 finite-place direct-summand 性；本文的局部证明亦直接给 auxiliary-p 的饱和性，不假设 raw d_z 约束已 primitive。

原 double-pole form 记为

\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-(s-1)a(s-3)!H_j^{(s-2)}-b(s-2)!H_j^{(s-1)},
\]
\[
V_j=C_jU_j+(s-1)!\{X-aH_j^{(s-1)}-bH_j^{(s)}\}.
\tag{A2}
\]

固定 s≥4，a,b∈Q；局部取 a,b∈Z_p 且 b为unit。paired head cancellation 对 s=5 有真实解析意义；下述局部 arithmetical factorization 本身也适用于其他固定 s，但不声称该空间对 s>5 仍消除全部解析 head。

## A2. 辅助素数与准确局部约束

取 n=2m、p=9m+1 prime，p>s+1。p是奇素数，故 m必为偶数。令

\[
q=3m,\quad h=6m,\quad c=4m+1,\quad
A(t)=(t)_{3m},\quad S(t)=\prod_{z=1}^{4m}(t-z).
\tag{A3}
\]

负节点是 a_ℓ=−ℓ，0≤ℓ<3m；positive head 节点 z=1,…,4m。所有 d_z=(z)₁₂ₘ₊₁ 恰含一层 p，因为 z<p、z+12m<2p。设 e_z=d_z/p∈Z_p^*。去掉唯一的 p，

\[
e_z=\frac{(p-1)!}{(z-1)!}
 (3m+z-1)!\prod_{r=1}^{3m+z-1}(1+p/r).
\tag{A4}
\]

所有 r<p，Wilson给

\[
e_z\equiv-A(z)\pmod p.
\tag{A5}
\]

真实 constraints 是 e_{z'}P(z)−e_zP(z')=0。除掉 p 的共同因子与逐pair实际gcd不会留下额外 auxiliary-p index：positive evaluation at4m consecutive distinct nodes是 split surjection Z_p[t]_<6m→Z_p^(4m)，each pair coefficient均unit，所以2m constraints满射、kernel是rank4m direct summand。

因 h<p，全部 factorial i! 为 p-unit，monomial、binomial/Newton 原格在此 p 的基变换均为 GL_h(Z_p)。若取 A_Z 的任何完整整数基，其局部 restriction 与下文选择的局部基只差 unit determinant；不能从 raw pair 基继承此结论。

## A3. paired reduction 的负评价秩

记 U=A_Z⊗F_p，dimU=4m；π:U→F_p^(3m) 是 negative evaluation。若 π(P)=0，则 P=AQ，degQ<3m，(A5)使 positive constraints 化为 Q(z)=Q(c−z)。Q(t)−Q(c−t) 的次数<3m，在4m不同head节点上为0，故恒为0。

因 p≠2，反射 even Q恰是 polynomials in (t−c/2)²，degQ<3m。m偶数给

\[
\dim\ker\pi=3m/2,\qquad \dim E:=\dim\pi(U)=5m/2.
\tag{A6}
\]

这不是原ambient rank3m的全部evaluation image。原 full-space 的 Hermite unit blocks 不能直接 restriction 后仍当非退化。

## A4. E 的准确 annihilator：维 m/2 的 even polynomials

记 T-space

\[
\mathcal T=\{T(t)=T(c-t),\ \deg T<m\},\quad\dim\mathcal T=m/2.
\tag{A7}
\]

head rows 的 linear combinations 在 P=AQ、degQ<3m 上消失，当且仅当它们可写成

\[
\sum_{z=1}^{4m}\frac{T(z)P(z)}{A(z)S'(z)},\qquad T\in\mathcal T.
\tag{A8}
\]

证明：head evaluation Vandermonde 的degree<3m annihilator由 μ_z=T(z)/S'(z)、degT<m给出，维m。paired rows要求 μ_{c-z}=−μ_z；S(c−t)=S(t)、S'(c−z)=−S'(z)，故恰要求T reflection-even。degree<m<4m将节点关系提升为多项式身份。

在 rational function T(t)P(t)/(A(t)S(t)) 上取所有 finite residues；numerator次数≤7m−2、denominator次数7m，无 infinity residue。由此 (A8) 等于

\[
-\sum_{A(a)=0}\frac{T(a)P(a)}{A'(a)S(a)}.
\tag{A9}
\]

这些 m/2 个negative row函数独立，因为 degT<m<3m且分母都是unit。因此

\[
E=\{e\in F_p^{3m}:
\sum_a T(a)e(a)/(A'(a)S(a))=0,\quad T\in\mathcal T\}.
\tag{A10}
\]

此处的 residue 身份是有限域上的代数恒等式；不使用 complex positivity。

## A5. leading trace 与第一个小 Gram

tail poles j=p+ℓ 对应 a=−ℓ。Lucas 与 frozen full-space Taylor 给

\[
W_{p+\ell}\equiv
\binom{3m-1}{\ell}^2\binom{4m+\ell}{\ell}^3
=K\,\frac{S(a)^3}{A'(a)^2},
\quad K=\frac{(3m-1)!^2}{(4m)!^3}\in F_p^*.
\tag{A11}
\]

令 D=diag(W_{p+ℓ})，为 nondegenerate ambient form。对 T∈T-space，定义

\[
v_T(a)=\frac{T(a)A'(a)}{K S(a)^4}.
\tag{A12}
\]

(A10)说明 E^{⊥D}={v_T:T∈T-space}。它的 Gram 为 K⁻¹G₀，其中

\[
G_0(T,T')=\sum_{A(a)=0}\frac{T(a)T'(a)}{S(a)^5}.
\tag{A13}
\]

因此

\[
D|_E\text{ nondegenerate}\quad\Longleftrightarrow\quad
\det G_0\ne0\text{ in }F_p.
\tag{A14}
\]

这把 leading restriction 的问题降到准确 m/2维矩阵，仍不能以其权重的实数正性证明 mod p unit。

## A6. 真正的 first jet：不能用裸 AQ 替代实际 paired lift

设

\[
I(t)=\prod_{\ell=2m+1}^{3m-1}(t+\ell)
=\gcd(A(t),A(c-t))\quad\text{over }F_p.
\tag{A15}
\]

degI=m−1为奇数，I(c−t)=−I(t)。这些 shared negative nodes 是 a=−ℓ with2m+1≤ℓ≤3m−1，reflection为 ℓ↔5m−ℓ；A∪A_ref 恰是 F_p 去head节点，overlap恰I的roots。

从 (A4) 得

\[
\frac{e_z}{(p-1)!}\equiv
A(z)\{1+pH_{3m+z-1}\}\pmod{p^2}.
\tag{A16}
\]

对 z'=c−z，H_{7m-z}≡H_{2m+z} modp，所以

\[
H_{3m+z-1}-H_{3m+z'-1}
\equiv H_{3m+z-1}-H_{2m+z}
=I'(z)/I(z)\pmod p.
\tag{A17}
\]

其中 H_{p−1−r}≡H_r 由 H_{p−1}=0与 reciprocals 的反射直接证明。

给任何 Q∈Q-space={Q(t)=Q(c−t),degQ<3m}，dim3m/2，选择相同反射的 Z_p polynomial lift。定义

\[
\widehat P_Q=AQ+\frac p2(A/I)I'Q.
\tag{A18}
\]

它次数<6m，系数 Z_p。式(A17)与 I'/I 的reflection-odd性质说明真实paired constraints在该 polynomial上模p²为0。A2中constraint map满射且有Z_p右逆，故可修正p² times一个degree<6m polynomial，得到actual paired P_Q，满足

\[
P_Q=\widehat P_Q+O(p^2 Z_p[t]_{<6m}).
\tag{A19}
\]

这是实际modp² lift，不是任选满空间 polynomial。对negative节点定义

\[
j_Q(a)=A'(a)Q(a),\qquad
\eta_a=\tfrac12{\bf1}_{I(a)=0}.
\]

在I roots，(A/I)I'=A'；在其他A roots，A/I为0。因此

\[
P_Q(a)/p\equiv\eta_a j_Q(a),\quad
P_Q'(a)\equiv j_Q(a)\pmod p.
\tag{A20}
\]

shared节点的半量first evaluation会进入真正weak Schur；把实际P_Q写成裸AQ而漏掉它一般不正确。

## A7. 全误差费用与 leading/weak blocks

记 u=(s−2)!b∈Z_p^*，M=p^s B_X。tail节点a−p的全尺度Taylor是

\[
P_Q(a-p)=p(\eta_a-1)j_Q(a)+O(p^2),\quad
P_Q'(a-p)=j_Q(a)+O(p).
\tag{A21}
\]

从 (A2) 的 harmonic 主项，

\[
p^{s-1}U_{p+\ell}=-u+O(p),\qquad
p^sV_{p+\ell}=-(s+1)u+O(p).
\tag{A22}
\]

a-source和X都不改变以下leading项：a-source的U比b-source高一层p，X-source乘p^s。对weak/weak，两evaluation均有p，derivative product有p，所以这些corrections都至少O(p³)；对strong/weak至少O(p²)。head j<p的U integral、V≥−1，乘p^s后至少p^(s−1)，s≥4保证在weak-leading p²之外。W的O(p) correction亦至少weak/weak p³。故以下三个blocks准确：

* strong/strong modulo p：−(s+1)u D|E；
* strong/weak 除p modulo p：u〈e,k_sj_Q〉D；
* weak/weak 除p² modulo p：u〈d_sj_Q,j_R〉D。

其中

\[
k_s(a)=s-(s+1)\eta_a,\quad
d_s(a)=-(s+1)\eta_a^2+2s\eta_a-(s-1)
=\frac{1-k_s(a)^2}{s+1}.
\tag{A23}
\]

η=0处 k_s=s，η=1/2处 k_s=(s−1)/2。对s5，这分别为5和2。

选actual paired strong liftswhose reductions覆盖E，并配A19的weak lifts，得到rank4m局部basis：modp两组分别覆盖 image与kernel，所以其相对actual saturated格的det是unit。不存在未付的p-dependent basis denominator。

## A8. 第二个矩阵与实际 weak Schur factorization

假设detG₀≠0，强块unit，可以用integral Schur elimination。D的orthogonal decomposition E⊕E⊥说明weak leading为

\[
\frac{u}{s+1}
\{\langle j_Q,j_R\rangle_D
-\langle\Pi_{E^\perp}(k_sj_Q),
                  \Pi_{E^\perp}(k_sj_R)\rangle_D\}.
\tag{A24}
\]

从 (A11)–(A13)，记明确 finite-field matrices

\[
H_0(Q,R)=\sum_a S(a)^3Q(a)R(a),\qquad
C_s(Q,T)=\sum_a k_s(a)Q(a)T(a)/S(a).
\tag{A25}
\]

j的Gram是KH₀，cross到v_T是C_s，v_T的Gram是K⁻¹G₀。因此

\[
\boxed{\text{actual weak Schur leading}
=\frac{uK}{s+1}\{H_0-C_sG_0^{-1}C_s^{\mathsf T}\}.}
\tag{A26}
\]

Q-space维3m/2、T-space维m/2，所有sum明确在3m个negative节点上。令

\[
\mathcal M_s=
\begin{pmatrix}G_0&C_s^{\mathsf T}\\C_s&H_0\end{pmatrix}
\quad(2m\times2m).
\tag{A27}
\]

则detM_s=detG₀ det(H₀−C_sG₀⁻¹C_sᵀ)。两矩阵完全与a和X无关，只含s、m、p及真实paired first jet。

## A9. 条件定理：真实 Smith、Gauss 与 nonzero criterion

若detG₀≠0且detM_s≠0，则M在actual paired saturated格上的Smith exponents恰为

\[
0^{\,5m/2},\quad2^{\,3m/2}.
\]

原B_X的exponents相应为

\[
\boxed{(-s)^{\,5m/2},\quad (-(s-2))^{\,3m/2}.}
\tag{A28}
\]

理由：strong rank5m/2且unit，cross在p中；integral Schur剩余p² times unit matrix，没有进一步退化。这个证明不是把 ambient full-space Smith直接截取。

在A_Z任意完整integer basis上取 actual determinant J_A(X)，不存在额外first2n factorial normalizer。因auxiliary p下ambient binomial/monomial基均unit、saturation也unit，得到

\[
\boxed{v_p^{\rm Gauss}J_A(X)=-m(4s-3),}
\]
\[
\boxed{p^{m(4s-3)}J_A(X)\bmod p
\text{ 是非零常数}.}
\tag{A29}
\]

同样valuation适用于任意X∈Z_p的specialization。a∈Z_p、b unit的source条件已足够；whole target polynomial的leading reduction与X、a无关。s5给−17m=−17n/2，较原fullspace−12n少7n/2指数；单个auxiliary prime只产生O(nlogn)，不是n²主率改进。

因此，若两显式finite-field determinants在无限p=9m+1上为unit，避开fixed a,b和候选rational目标的分母后，就严格取得paired space的无限nonzero rational evaluations。本文尚未证明这一无限unit条件。

## A10. 正确的有限域反射与不能免费使用的 positivity

A_ref reflection把negative indicesℓ0..3m−1送至ℓ2m+1..5m。union是Fp去4m个head的全部5m+1节点，intersection是m−1个I roots。对任何reflection-even f，

\[
\sum_{A(a)=0}f(a)
=\tfrac12\{\sum_{t\in F_p,\ S(t)\ne0}f(t)
              +\sum_{I(a)=0}f(a)\}.
\tag{A30}
\]

这适用于G₀、H₀的各entry。C_s则因k_s在overlap改变，

\[
C_s(Q,T)=\tfrac s2
\sum_{S(t)\ne0}Q(t)T(t)/S(t)
-\tfrac12\sum_{I(a)=0}Q(a)T(a)/S(a).
\tag{A31}
\]

这些是实际full-complement与middle correction的身份，不能删middle。

实数lift下G₀可看作正weighted Gram，但有限域的单位性不由实数正定性推出。H₀/C_s也不构成自动正定的有限域measure。因此本文不以有限域“positivity”替代两个determinant的证明。

## A11. 全素数费用接口与仍未补完的内容

paired determinant取完整saturated Newton基S，真实定义为det(SᵀB_NewtonS)，并非恢复四重零的size2n determinant。两次Cauchy–Binet给其Gauss valuation至少ambient B_Newton全部2n-minor的共同下界。

若把ambient monomial residue bounds转到Newton，安全factorial扣除是

\[
2\sum_{i=n}^{3n-1}v_p(i!),
\tag{A32}
\]

即最大的2n个row/column factorial，不是first2n项。对sqrt(8n)<p≤6n可用实际F_s,ρ的全部2n-minor优化；小prime另用−2ns floor(log_p(8n))，p>6n全部integral。这样提供whole-matrix安全全finite-place模型，但未证明足够便宜的主率。positive common content应保留，不把其safe bound当actual费用lower bound。

从A29的一个auxiliary-p真实valuation也不能推出全p n²下界。新的paired basis norm/解析energy另由root与quarter研究；本文没有把 quartic-zero 的能量或既有LP常数拼接到paired determinant上。

固定 a,b∈Q 的 source 分母仍应付费：取固定正整数 D 使 Da,Db∈Z，乘 D 后 ambient form 的 coefficients 对全部 finite places 使用相同整化；size2n 的 paired determinant 因此再乘 D^(2n)。其 finite/arch 费用是 O(n)，不影响 n² 主率，但不是免费的有理 gauge。A2–A9 的 auxiliary-p 结论限于 p不整除D 且 b为p-unit。

## A12. 自有首次精确探针与执行历史

NEW code：
research/cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.py，
SHA256256f5f32efa8755a6c3c234d25ed2d5395fbf7e45d9402af569c476bb6c94e42。

NEW output：
research/cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.json，
SHA256f8b0f099507d284850fb66ff5236b8e4d5e5d46025ad798c97bca467274ab30a。

准确历史：本轮新建上述代码；仅执行一次命令 python research/cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.py，exit0。文件对output存在设拒绝rerun保护。imports只有stdlib json/math/pathlib；没有读取、执行或import任何旧/peer producer。未修代码后再执行，也没有第二次执行。以modp⁸精确整数算法计算actual d_z/p constraints的kernel、restricted p⁵Gram及Smith；X=0，s5，probe参数 r=0与1 明确对应 source a=−r,b=1。

五个auxiliary primes及十cases：

| m | n | p | negative eval rank | restricted p⁵Gram Smith |
|---:|---:|---:|---:|---|
|2|4|19|5|0⁵,2³|
|4|8|37|10|0¹⁰,2⁶|
|8|16|73|20|0²⁰,2¹²|
|12|24|109|30|0³⁰,2¹⁸|
|14|28|127|35|0³⁵,2²¹|

每行对r0/r1均成立；所有constraint identities与rank公式检查通过。每个G₀的rank也准确为m/2。Smith exponents全部在precision8以内detected；X项从p⁵进入。

该程序没有覆盖所有m、没有证明Dirichlet子列中的两个determinant无限unit、没有计算all-prime预算、没有证明strict margin。十个有限case仅为寻找全尺度identity的证据。A2–A11的纸面定理独立于这些finite probes；conditional A9的hypotheses没有由十个case消除。

## A13. 本轮已证进展与精确未证项

已证全尺度：

* paired space的真实auxiliary-p constraints和negative evaluation rank；
* E⊥的m/2维weightedtrace模型；
* actual modp² paired lift，包括shared节点不可省的η=1/2；
* actual weak Schur与两明确determinant的block factorization；
* 在两unit条件下的准确Smith/Gauss/constant reduction与无限nonzero推论。

未证的是两个finite-field determinants在无限辅助素数上为unit，以及同一个saturated paired determinant的充分便宜全prime费用与解析能量净余量。当前不能宣布paired路线已取得无限nonzero，也不能以现有safe LP缺少margin宣布actual路线不可能。

来源收据与同行独审均另NEW保存；冻结旧稿不改。没有新的数值无理性、线性无关性或Lean定理。
