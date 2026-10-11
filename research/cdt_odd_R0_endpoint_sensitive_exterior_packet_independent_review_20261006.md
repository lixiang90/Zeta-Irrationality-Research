# 独立审阅：R₀ endpoint-sensitive exterior packet 与 real Betti normalization

日期：2026-10-06。审阅者为 toric/current 路线作者，未参与下列两个主稿的写作；以下为实际阅读全文、纸面重算及一手页阅读后的 NEW 独审记录。旧/同行数学 MD/PY/JSON/manifest 只读，producer 执行/import数0，未以 symbolic/numerical verifier代替证明。

## I1. 实际终稿与准确scope

实际全文审阅：

* [endpoint-sensitive exterior packet](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md)，终稿SHA256
  b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef。
  E1–E30全读，包括新增 E7a 的四行 \(D^7\) 与 mixed \(D^6\) budget、
  E20.3 contraction-model holomorphy；另实际回读最终 E11/E30 的
  odd Kummer / even-cover限定。
* [real Betti normalization](cdt_odd_R0_real_Betti_normalization_20261006.md)，终稿SHA256
  dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f。
  R1–R45全文实际读，特别独算 physical versus signed monodromy、
  R25 intersection、R33/R34 connection relation以及R39–R42 positive cost。
* actual non-split输入 [Kummer interface](cdt_odd_R0_kummer_period_interface_20261006.md)
  本轮全文实际读，SHA256
  803b3eced9825fe5f40005728430188e36c4a8cd123d41223972cceb23c2e172。
  其 §4 rational-particular no-go、regular-singular单值 argument和
  §5 local \(J_4(1)\oplus(-1)\) 独核。
* 当前main仅声称实际§§73–78、delivery仅current R₀ state keys。
  frozen Yukawa稿此前已实际全文独审，primary实际页与scope见I9。

结论：在各主稿明确给定的冻结几何/Sp₄/period输入下，两个终稿的全尺度
正面结论通过本次独审。没有将 actual rank 或 polynomial-flag detection
登记为目标数的新无理性；两个稿自己的 arithmetic/integral/capacity缺口
保留。

## I2. Exterior E4–E6：实际Ga⁴、九秩及完整十秩

五维connection E4由
\[
 t\theta^4f=x(2\theta^3+\tfrac32\theta^2+
                   \tfrac12\theta+\tfrac1{16})f
            +\beta\sqrt{x}/16
\]
逐行直接得到，source row为 \(\theta(\beta\sqrt{x})=\beta\sqrt{x}/2\)。
E7端点三minor的行矩阵首行为 \((\alpha_0,0,0)\)，后两homogeneous columns
在 \(\theta,\theta^2\) 行为 \((-1,-1)\)、\((0,2)\)，所以
\(\Phi_{012}(1)=-2\alpha_0\)，符号通过。

E9只是实际 Lagrangian \(g_1,g_2\) 的 symplectic constraint，不损失真实
minor信息。mixed minors \(ij4\) 的 \(\sqrt{x}\) 在第一solution column；
三行determinant的cyclic排列为正，因而其值确为 \(\sqrt{x}(g_1\wedge g_2)_{ij}\)。
对 E8 的flat \(B(x)\)，constraint derivative为其自身乘 \(1/2\)。
E10的elimination没有在conifold除 \(t\)。

Galois radical证明实际成立：projection的connected component给
\(\mathrm{Sp}_4\times1\)，一个负Kummer component再给全部
\(\mathrm{Sp}_4\times\mu_2\)。kernel是 standard \(V\) 的 stable additive
linear subgroup，故为0或全部 \(V\)。为0将使五维representation在reductive
group下completely reducible，并给 rational differential splitting；实际
Kummer no-go已经排除。故kernel为 \(\mathbf G_a^4\)，不是由abstract Ext
dimension猜测所得。

在九维kernel中，bottom为 \(\bigwedge^3V\simeq V\)，quotient为
\(\chi\otimes\bigwedge^2_0V\)，维数分别4、5且不可约。实际quotient
\(g_1\wedge g_2\ne0\)，Sp₄ span为5；translation differences
\(a\wedge g_1\wedge g_2\) 有非零项，其Sp₄ span给bottom4。因而actual
orbit span是9。若有 rational-function coordinate row relation，它被全部
Galois conjugates保持，杀九维solution span；fundamental matrix可逆迫row为0。
这证明 E15为实际9，不只一个上界。

scalar012 evaluation kernel为G-stable；bottom上由E7非零，因此与bottom
交集0。若其quotient非零，则irreducibility给全部5，任意translation在一个
非零quotient上产生非零bottom，矛盾。故scalar最小order也9。composition
factors与dual均没有trivial factor，加入1得到实际10。有限cover保留connected
\(\mathbf G_a^4\rtimes\mathrm{Sp}_4\)，同一结论不降秩。

End只为scalar亦通过：不同不可约4/5迫endomorphism保持bottom，translation
迫两diagonal scalars相等，off-diagonal Hom为0。这准确区分 differential-field
Galois translations 与 commute整个G的horizontal module automorphisms。

## I3. E7/E7a：逐系数D十到D七，未免费改变holomorphic格

本轮实际重读 FR published原件PDF2–5、9。Thm1给 order \(\mu\) 的
\(D_{bn+b_0}^{\mu-1}C^{n+1}\)，Thm2在geometric operator下无条件，
PDF9保留全部有限坏素数的 exponential \(C\)。当前四阶 homogeneous
germs因此可用 \(D^3\)；五阶 particular的safe模型为 \(D^4\)。
对 rational holomorphic local solutions，使用原方程的order，不把
log-coefficient一般需 \(\mu^2\) 的情形混入。integer conifold exponents
给 \(b=1\)。冻结G-function/geometric输入依旧是该应用的前提。

原三minor的 \(4+3+3=10\) 与 mixed \(3+3=6\) 通过。Euler jets只把
index最多移动3、乘integer factorial ratios；三重convolution的indices之和
为 \(n\)，所以 \(C^{n+12}\) 是统一安全界，不能错误累积为 \(C^{3n}\)。
\(4\mid C\)支付 square-root twist。假设仅 \(\alpha_0\in K\)，乘 \(d_0\)
清分母即足够；\(\alpha_1,\alpha_2\) 已在全函数level消去。

独立重算 E7a 的contraction：
\[
 c_B=
 \begin{pmatrix}
 t&0&0&0\\-x&t&0&0\\x/2&0&t&0\\0&x/2&x&t
 \end{pmatrix}.
\]
它的四列由
\(c(e_i\wedge e_j\wedge e_k)=B_{ij}e_k-B_{ik}e_j+B_{jk}e_i\)
直接得到。写 \(c_B=tI+N\)，下三角 \(N\) 满足 \(N^2=0\)：
唯一潜在二步entry为
\((x/2)(-x)+x(x/2)=0\)。
所以inverse确只有 \(t^{-1},t^{-2}\)，不是一个免费holomorphic/integral
gauge；\(\det c_B=t^4\)、\(\operatorname{Pf}B=-t^2\) 均通过。

self-adjoint concomitant identity给
\(\theta C(\Psi,g_j)=\sqrt{x}g_j/16\)；
\(\theta=-(1-t)\partial_t\) 因而给
\[
 F_j=-\frac1{16}\int_0^t g_j(u)/\sqrt{1-u}\,du.
\]
constant pairings是 \(-3\alpha_0/2,2\alpha_0\)，所以
\(Z_j=F_1\theta^jg_2-F_2\theta^jg_1-2\alpha_0\theta^jv\) 精确。

逐系数 \(F_j\) 只需 g的 \(D^3\)、integration的一个 \(n\mid D\) 和
inverse-square-root的 \(4^k\)，即 \(16D^4\)；再乘gjet得到 \(D^7\)。
convolution同样按indices总和，只产生固定额外C幂，不产生 \(C^{2N}\)。
因此 E18.4是严格全部prefix命题，五mixed行仍D六。该预算并非effective
最佳 \(C\)、Smith、Betti comparison或CDT capacity。

目标Z端点独算为
\((0,2\alpha_0,-\alpha_0,\alpha_0/4)\)。
其中 \(\theta v=-1,\theta^2v=1/2\)；P在 \(t=0\) 的关系
\(2\theta^3v+(3/2)\theta^2v+(1/2)\theta v+v/16=0\)
给 \(\theta^3v=-1/8\)，不依赖未核的第三Taylor系数。
新packet rationally invertible而实际rank9/10仍保持，Z0 scalar同一
kernel argument给order9。

## I4. E20与E20.1/2/3：monodromy fixed不等于raw jets全纯

对rank-one transvection，decomposable三wedge fixed等价于其plane invariant。
因第一向量source非零，plane与V的intersection正是homogeneous
Lagrangian \(P_\gamma\)。invariance若来自 \(\ell|_L=0\)，则
\(P_\gamma\subset v^\perp\)，Lagrangian duality迫 \(v\in P_\gamma\)；
反过来 \(v\in P_\gamma\) 足够。因此E20对所有q不敏感，成立。

但raw jets可能有 poles，主稿正确没有免费把fixed branch当holomorphic：
独算
\[
 \det D^{0,1,2}(t\log t,t,k_0)=-k_0/t+\cdots,\qquad
 \det D^{1,2,3}(t\log t,t,c_2t^2)=-2c_2/t^2+\cdots .
\]
regular invertible Euler row change不能使整个tuple的非零pole消失。
这支持E20.1的额外第一column全纯条件。

至多一列bad log direction，jets最大pole二阶，故 \(t^2\Phi\) 正好
regularize所有fixed-branch poles；非fixed branch的log不能由nonzero
polynomial消去。E20.2成立。辛配对模型更直接：两个homogeneous
columns全纯时，\(\theta C(f,g)\) 的右端也全纯，而 \(\theta\) 在1为
unit times derivative，两个C值遂全纯；全部Z行全纯，即使f自己有log。
inverse有pole，所以E20.3与原raw holomorphic lattice不同。三个准确scope
均通过，仍未构造一个实际值敏感的transport word。

## I5. E21–E30：真正∞Jordan与值敏感origin flag

Stieltjes \(x=-R\) 的scaling argument逐项核验：\(b(z)\in[0,\log256]\)，
\(z=Lw,L=\log(256R)\)，integrand被
\(\mathbf1_{\|w\|_1\le1}+\mathbf1_{\|w\|_1>1}e^{1-\|w\|_1}\)
统一控制。4维crosspolytope体积2/3，故
\(B(-R)\sim L^4/(384R)\)。
actual \(W(-R)\) 的nonzero log四项与regular-singular exponent1/2严格迫
\(J_5(-1)\)。odd winding semisimple sign为−；even winding的regular
nilpotent唯一invariant三plane位于V，而actualplane含非零source，遂E22
全部finite-cover不能填平。这里不是有限asymptotic拟合。

origin local splitting \(E=V\oplus\mathbf CW\) 按 \(1,-1\) generalized
eigenspaces给canonical \(p_+\)。actualW的marking给E24，未知两初值在
wedge中完全消去。symplectic contraction满足
\(c(\Phi_0)=-2v\)，actual \(C(y_0,v)=1/\pi^2\ne0\)。
regular symplectic \(J_4\) 有
\(\ker N_0^3=y_0^\perp\)。
而 \(C(y_0,c(y_0\wedge a\wedge b))=0\)，所以E28的
\(N_0^3p_+\Phi(q)=0\iff q=\alpha_0\)严格成立。它是新的actual最高log
旗标检测，不是已获CDT填点或数值无理性。

最终E30已明确必要的cover parity：odd loop mixed quotient semisimple−1
不能fixed；even cover杀χ后，plane invariant与det1 gives fixed wedge，
条件为 \(N_0H\in\ker N_0^2\)，等价于 \(C(y_0,H)=0\)。
这一限定对最终声明必要，终稿已正确纳入。canonical \(P\) 含v而
\(C(y_0,v)\ne0\)，故它不是唯一invariant \(P_0=\ker N_0^2\)；
canonicalbranch仍不填平。不能把最高log旗标的唯一q变成已构造fillable
sheet。

## I6. Real稿R1–R29：actual实结构与physical sign独核

linear rational involution \(B\) 与antilinear \(C=BK\) 的区别正确。
complex dimension3 conjugation degree−1给raw cup anti-symplectic；
\(\bar a^3=-a^3\) 则Tate-three de Rham cup实相容。KLM principal
unit triple的cut coorientation与a的conjugation两个负号相消；actual
unit/regulator class的C不变性和已证 rational restriction injection
给compact AJ real average，合法但仅rational。

PD方向独算 \(BPD\gamma=-PD(c_*\gamma)\)。actualδ imaginary sphere的
antipodal map在S³ degree+1；Γ的三CCW contours共轭给product sign−，
与sheet-root负号一起保留graph。因此 \(PD\delta\) 为minus、
\(PD\Gamma\)为plus。anti-symplectic nondegenerate四sector使plus/minus
各dim2；再施δevaluation的nonzero functional，允许的rational shift
确剩一条Q-line。fullH³/sector projection在稿中有明确区分。

特别核准R25没有把period的signed transport当physical monodromy：
\(\eta=\omega/\sqrt{x}\) 的operator在origin exponents−1/2，physical
\(M_0\) trace−4；在∞ exponents1，trace+4。
\(U_0=-M_0\)才给P-period的logshift。由
\(M_1=I+\delta\otimes(\cdot\delta)\)，
\(\operatorname{tr}(M_0M_1)=-4-(\delta\cdot M_0\delta)=4\)，
故 \(\delta\cdot M_0\delta=-8\)、\(\delta\cdot U_0\delta=8\)。

\(\gamma_L=(U_0-U_0^{-1})\delta-2\Gamma\) 是actual closed integral
cycle。conjugation为minus，δintersection \(8-(-8)-16=0\)。
signedN为singleJ4，\(\delta\cdot\Gamma_V=8\)迫 \(N^3\delta\ne0\)；
\(N(\gamma_L)_V=2N^2\delta\ne0\)，故其projectedrational class非零且生成
剩余line。未推projector integral或primitive generator，scope正确。

## I7. Real稿R30–R45：R34、R39及strict positive cost独核

Frobenius recurrence确给 \(PF_\rho=\rho^4x^\rho\)，前四rho derivatives
生成所有homogeneous解。origin concomitant matrix由leading log
polynomials直接得 \(C(f_0,f_3)=-1,C(f_1,f_2)=1\)，其余independent
pairs为0。actual \(C(y_0,g)=-1\)遂固定g的f3 coefficient为1。

对logshifta，独算
\[
 C(g,g_{U_0})=a(2b_1-b_2^2)+a^3/6.
\]
actualcycle dual sign与R25给 \(2b_1-b_2^2=a^2/3\)。
又
\[
 g_{U_0}-g_{U_0^{-1}}
 =2af_2+2ab_2f_1+(2ab_1+a^3/3)f_0.
\]
减 \(2\Gamma\) 的period \(a^3f_0\)，再乘normalized factor−a/16，
准确得到R34，未漏physical负号：
\[
 p_L={\pi^2\over2}
 \{f_2+b_2f_1+(b_2^2/2+2\pi^2/3)f_0\}.
\]

rho derivatives of \(A_n\)给R35的两个harmonic formulas。
代入R34得R36，每项的static coefficient leading
\((b_2+8\log2)^2/(\pi^2n^2)\)，remainder \(O(n^{-3})\)。
外面的\(\log x=O(t)\)只贡献higher-order logs；一阶 \(t\log t\)
coefficient因此为 \((b_2+8\log2)^2/4\)。
δintersection0使actualγL-period在conifold全纯，故该coefficient必须0。
R38 \(b_2=-8\log2\) 与 \(b_1=32\log^22-2\pi^2/3\) 成立。

positive tail
\[
 \ell_n''+4\pi^2/3
 =4\sum_{k=n}^\infty((k+\tfrac12)^{-2}-(k+1)^{-2})>0
\]
逐项核准。因此R39全部summands严格正，endpoint n0项正好
\(16\pi^2\log^22+\pi^4/3\)，其余正，R41严格大于这个值。
tail \(O(n^{-4})\)与uniform domination成立，是真实analytic limit，
未声称singular-fibre integralcycle。origin log² coefficient
\(\pi^2y_0/4\)也直接由R36取最高log²，故合法不同lift不能都保留
原algebraic Nilsson packet；不是conifoldjets的非代数性证明。

R44双圈budget亦核：
\(C(g,g_{U_0^2})=2a^3\)给δintersection32；
V-periodinjectivity给 \(N^3\delta=2\Gamma_V\)，sinh展开使该新cycle的
Vprojection恰2γL，scalar2pL。稿中没有把sector身份扩为全部homology。

## I8. 两篇正结果与explicit current marking的相容性

两稿都保留value-sensitive arithmetic/integral/capacity工作，未宣称
\(\alpha_0\)代数假设等同于 \(R_0-M_0\)有理假设：
\(\alpha_0=\pi^2(R_0-M_0)/16\)，后者不提供前者所需整化。

real稿允许的real-compatible、δ-normalized lifts之间的Q-line自由，
并不否定另一explicit current marking给某个指定lift的精确scalar。
本审阅者另稿的centered-current construction给一个这样的marking；
这里不将自己的稿算成独立审过，也不从该marking推integral格或数值结果。

exterior actual9/with1实际10、D七预算、origin最高log旗标是可变更CDT
输入的严格结果。要完成目标，还要effective有限坏素数C、实际Betti/
de Rham比较与整数saturation，以及使用endpoint flag的capacity/holonomy
不等式。real R41计算出的positive period成本恰说明仅靠reality和δeval
不能免费固定scalarendpoint。

## I9. 本次实际一手阅读与执行receipt

本轮重新实际整页读：

* Fischler–Rivoal, *Denominators of the coefficients of G-functions*，
  [published primary](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)，
  PDF2–5、9，SHA256
  c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68。
  准确用于Thm1/2、geometric无条件、rational local solutions与全部坏素数C。
* KLM, *The Abel–Jacobi map for higher Chow groups*，
  [published primary](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，
  PDF8–12，SHA256
  8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9。
  此为本轮centered-current研究实际整页重读，亦支持本独审的intrinsic
  unit-product/conjugation/current cone convention；未声称全文原件重读。

此前已实际读而本轮只复用：

* BK 作者原件PDF6–7、12、19及Movasati PDF93–95；
  用于冻结actualPF/PL/Yukawa输入。此前Yukawa独审文件SHA
  6207c36f8939dd6d46e9071a9b52e96672862b7abb01dbd042ed3b6e53812af0。
* DeligneIII PDF35–41的SNC restriction/support background。
  本次Frobenius、group/orbit、convolution和harmonic-tail证明逐项独立重算，
  不是由source摘要推导一个未读的算术定理。

新增PDF0、网络下载0、数学producer0、旧/同行producer执行或import0。
Python仅fitz阅读原件及hashlib登记SHA；PowerShell仅只读稿件和hash；
本审阅以apply_patch另存NEW，没有修改任何peer/冻结数学文件。

