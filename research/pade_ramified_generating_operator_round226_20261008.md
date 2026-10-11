# 第226轮：实际生成算子的完整无log局部桥与一张付清的小分歧共同图

2026-10-08，C。固定224/225最终 R_n、原 A3/A5/A7/C、Δ/Ξ及有理 g 的 H_g，不改冻结稿/main/manifest。数学程序0。本稿新增纸证是：实际多项式递推直接转成有限定义的生成微分算子；simple-leading点的完整 Frobenius/inhomogeneous/收敛桥；原 A/C 的六点无log；以及 actual exterior dominant point 的完整二重填入和显式共同图。它不是由半整数径向主渐近直接猜 Puiseux，也没有得到数值无理性或CDT strict gate。

## 1. 历史范围与同一对象

**R1.** 历史完整局部填充已在 level7 paid-map稿§§1–3用实际三次cover支付；该稿同时保留原∞的log与其他0/σ前像。Theta universal-cover稿§1与gamma algebraic-reference稿§1的finite-cover障碍，依赖各自非零log/residue，限于其指定载体。这些已知方法说明应检查完整局部方程与全部前像，不能将其log上限搬到本packet，也不能只把本轮半整数主项当作无log证明。

冻结输入为 [224 operator](pade_centered_even_telescoper_round224_20261008.md) T1–T18、[225 actual symbol](pade_actual_leading_symbol_round225_20261008.md) S1–S19及[225 powers](pade_relation_power_rank_gate_round225_20261008.md) P1–P15。记原四个标量解为 f_r=A3,2r、A5,2r、A7,2r、C2r；I2r亦满足同一递推。这里的生成变量为z，θ=z∂z；不把差分order6或20当作最小微分rank。

## 2. 实际标量生成微分算子与完整head

**R2.** 直接采用224 T12的已付多项式：

\[
p_j(r)=r(r-1)(r-2)D_0(2r)^{612}\lambda_j(2r),\quad
D_0(n)=\prod_{c=-5}^{12}(n+c),\quad0\le j\le6.
\]

它们满足Σp_j(r)f_(r+j)=0，对所有整数r≥0成立，r=0,1,2所有系数为0。225已付每个λ_j的degree差恰−30，故每个p_j的degree相同，恰为

\[
N=3+18\cdot612-30=10989.
\tag{R2}
\]

写 p_j(r)=d_j r^N+e_j r^(N−1)+…，所有d_j≠0，C(u)=Σd_j u^j=d_6χ(u)，χ是225确切six-root characteristic。这个巨大N只是明确粗清分母版本的微分阶数；不领取相应CDT函数数或最小阶。

**R3.** 对实际 F(z)=Σ_(r≥0)f_r z^r，逐项改变k=r+j，得到完整身份

\[
\mathcal L F=b_f(z),\qquad
\mathcal L=\sum_{j=0}^6z^{6-j}p_j(\theta-j),
\]
\[
b_f(z)=\sum_{j=0}^6z^{6-j}p_j(\theta-j)
             \sum_{k=0}^{j-1}f_kz^k.
\tag{R3}
\]

b_f为degree≤5的实际多项式head，使用原初值，未删除finite tail或prefix。四个有理源的b_f在Q[z]；实际I的head可在C[z]，以下局部证明不要求其有理。R3先是formal身份，已付source增长保证原点实际解析芽，故在初始小盘为解析身份。

## 3. 六个simple-leading点的实际indicial polynomial

**R4.** L的θ^N与θ^(N−1)系数分别为

\[
A(z)=\sum d_jz^{6-j}=d_6z^6\chi(1/z),\qquad
B(z)=\sum(e_j-Njd_j)z^{6-j}.
\tag{R4}
\]

χ六根µ distinct、非零。因此每个ρ=1/µ≠0处A有simple zero。普通∂z表示的最高两项为

\[
a_N(z)=z^NA(z),\qquad
a_{N-1}(z)=z^{N-1}\{\tbinom N2 A(z)+B(z)\}.
\tag{R5}
\]

所有低项均analytic。最高项只simple zero，除它后各低项至多simple pole，故该点是实际 regular singular point。不是把递推根自动称为微分方程的指数。

**R5.** 置t=z−ρ。代入t^σ，最低项为

\[
(\sigma)_{\underline{N-1}}
\{a_N'(\rho)(\sigma-N+1)+a_{N-1}(\rho)\}.
\tag{R6}
\]

因此indices为0,…,N−2以及 σ=N−1−a_(N−1)(ρ)/a_N′(ρ)。令E(u)=Σe_j u^j；在C(µ)=0处，

\[
\frac{B(\rho)}{\rho A'(\rho)}
=N-\frac{E(\mu)}{\mu C'(\mu)},\qquad
\sigma=-1+\frac{E(\mu)}{\mu C'(\mu)}.
\tag{R7}
\]

225 P6/P7实际 harmonic/Galois桥已证 normalized recurrence的全部six roots γ=−11/2。乘共同清分母因子只向E增加C的倍数，不改变根上的商；故E(µ)/(µC′(µ))=−γ=11/2。**确切σ=9/2**，不是只从F的一个径向leading估计反推。余下大量integer indices之间有形式共振；下一节实际支付它们全有analytic解、没有log。

## 4. 任意阶simple-leading引理：inhomogeneous与convergence自证

**R6.** 更一般，令Σ_(k0..N)a_k(t)F^(k)=b(t)，全部系数与b analytic，a_N有simple zero，置

\[
\eta=-a_{N-1}(0)/a_N'(0),\qquad\sigma=\eta+N-1,
\]

假设η非整数。取 augmented derivative state Y=(F,F′,…,F^(N−1),1)。其一阶系统 Y′=(R/t+Q(t))Y 的residue仅可能有最后一个derivative row非零；inhomogeneous项也在这一行。因此rank R≤1，trace R=η。η≠0给R²=ηR，R diagonalizable，eigenvalues为η和若干0。augmentation支付完整polynomial head，不把它丢掉再误称homogeneous。

**R7（holomorphic gauge与显式majorant）。** 在对角化常basis中求H(0)=I，Y=H(t)Z、Z′=RZ/t。写Q(t)=Σ_(m≥0)Q_m t^m、H=I+Σ_(k≥1)H_k t^k，准确递推为

\[
(kI-\operatorname{ad}R)H_k
=\sum_{m=0}^{k-1}Q_mH_{k-1-m}.
\tag{R8}
\]

adR的eigenvalues仅0、η、−η。η非整数保证对全部k≥1可逆，且存在固定K使其norm≤K/k；有限多个小k单独吸收，大k直接用几何逆。取h>0、A>0使||Q_m||≤Ah^(−m)。若h_k=||H_k||，h_0=1，则

\[
k h_k\le KA\sum_{m=0}^{k-1}h^{-m}h_{k-1-m}.
\]

标量majorant的生成函数为

\[
y(t)=\exp\!\left(\int_0^t\frac{KA\,ds}{1-s/h}\right)
=(1-t/h)^{-KAh}.
\tag{R9}
\]

它在|t|<h解析，系数非负并逐项majorize H。因此H实际收敛、局部invertible。这里没有调用未读的高阶Frobenius定理或把formal gauge当analytic。

**R8（完整解与analytic particular）。** 因R semisimple，Z=t^R c只含analytic常数方向与t^η方向，无log。augmentation的residue image只有最后derivative方向，而η≠0；其0-eigenspace中可选择最后constant-coordinate为1，得到实际analytic particular。等价地，任意自由F的前N−1个Taylor系数给出递推，次数k未知系数F_(k+N−1)的因子是

\[
(k+N-1)_{\underline{N-1}}a_N'(0)(k-\eta)\ne0\quad(k\ge0).
\tag{R10}
\]

上述gauge majorant证明其收敛。homogeneous的N−1个analytic解也如此支付，未遗漏integer resonance。

一阶state的fractional方向从F^(N−1)的t^η开始。derivative-chain恒等式迫F的fractional系数至少从t^(η+N−1)开始：否则其N−1次导数将产生更低非整数指数，无法由analytic项消去。若该方向非零，最高state的非零首项又保证阶数恰为η+N−1。因此每个完整局部解，任意搬运分支，均为

\[
F(t)=F_{\rm an}(t)+t^\sigma F_{\rm frac}(t),
\qquad F_{\rm an},F_{\rm frac}\in\mathbb C\{t\}.
\tag{R11}
\]

F_frac允许为0。对原A/C，σ=9/2，所以**六个特征点的全部actual branches局部monodromy平方为I**；t=u²后F holomorphic。任何固定数量原z-derivatives则meromorphic，可有有限poles，不能全称analytic。

## 5. 有理matrix recurrence的同一局部引理

**R9.** 此节为general vector接口，并有限应用到实际dominant exterior point；不要求其他十九个products互异。若真实state recurrence为v_(r+1)=C(r)v_r，取q(r)使P=qC为polynomial matrix，deg q=N、degP≤N，C(r)=C0+C1/r+O(r^-2)。若必要可另乘有限prefix因子，使原state身份在所有r≥0成立。实际生成向量V满足

\[
\{q(\theta-1)I-zP(\theta)\}V=q(-1)v_0.
\tag{R12}
\]

设q=q_N r^N+q_(N−1)r^(N−1)+…，则最高两层θ系数为

\[
B_0(z)=q_N(I-zC_0),
\]
\[
B_1(z)=(q_{N-1}-Nq_N)I
-z(q_{N-1}C_0+q_N C_1).
\tag{R13}
\]

在µ为C0的simple非零eigenvalue、ρ=1/µ处，取left/right ℓ,e且ℓe=1。最高ordinary derivative matrix z^NB0只有simple corank1，其逆residue为 eℓ/[ℓ(z^NB0)′e]。增添所有derivative-chain及constant1后，一阶residue仍rank1；其非零eigenvalue是

\[
\eta=-\frac{\ell\,\rho^{N-1}B_1(\rho)e}
 {\ell(z^NB_0)'(\rho)e}
=-N-\frac{\ell C_1e}{\mu}.
\tag{R14}
\]

inhomogeneous residue与所有lower derivative blocks均在同一个image方向，故augment后没有额外zero-eigenvalue Jordan block。令γ=ℓC1e/µ，若η非整数，则R7的同一convergent gauge与R8的analytic particular支付

\[
V(t)=V_{\rm an}(t)+t^{-\gamma-1}V_{\rm frac}(t).
\tag{R15}
\]

这是完整vector方程的结论；没有免费由matrix size读取CDT rank。

**R10（actual wedge的全部prefix）。** 原companion只有最后一行分母p6。每个∧³minor最多包含该行一次，因此对实际20-state exterior system，可直接取q=p6、P=p6(∧³C)，P为degree≤N polynomial matrix，N仍10989。身份qW_(r+1)=PW_r在p6=0的整数也成立：若该minor不用新第六state，它只是乘q的shift；若用它，原Σp_j f_(r+j)=0通过det的最后一行线性性恰给该identity。r=0,1,2所有p_j=0，P亦0。无需定位最后一个minor整数异常，也未重跑producer。

225 P8的constant/nearidentity gauge把原companion next层改为γC0，γ=−11/2。取∧³后next层为3γ(∧³C0)，而nearidentity的commutator不改变simple eigenprojection ℓC1e。故actual exterior的simple方向为γ_w=−33/2。

**R11（dominant point）。** µM=µ1µ2µ3=−M，M=L1L2L3，是20个triple-products唯一最大模，故simple。其他products的模至多L1L2κ；这一结论只用225六模的严格大小，不证明其余products互异。因此R14/R15在ρM=−1/M支付

\[
W(z)=W_{\rm an}(z)+ (z-\rho_M)^{31/2}W_{\rm frac}(z),
\tag{R16}
\]

全部original transported branches均无log。原D、X是各实际exterior solution的指定分量；任何固定g的H_g=gD+X亦如此。double cover完整消去此处branch。关系假设下H_g在ρM本来analytic；R16没有借此假设修改原D/X，亦没有宣称其他十九点、0或∞已全部填入。

## 6. 一张真正的原三行ramified共同图及其准入结果

**R12.** 取ρ=ρM，

\[
T(t)=\rho(2t-t^2),\quad |t|<3/2,
\qquad \varphi(w)=T(3w/2),\quad|w|<1.
\tag{R17}
\]

T^(−1)(0)={0,2}，域内只有原生0；T^(−1)(ρ)={1}，multiplicity2。最高matrix的其他finite singular candidates为非zero reciprocal exterior eigenvalues。由R11，它们满足

\[
|\rho'/\rho|\ge L_3/\kappa>19683>21/4,
\]

而|2t−t²|<21/4，所以没有其他candidate前像进入此盘；∞亦在域外。原生0的实际germ analytic，t=1由R16完整doublefill。punctured盘的基本loops只有0和1：前者固定原芽，后者投影为dominant loop两次，全部local monodromy平方为I。monodromy theorem与这两个local fills给**原D、X及所有固定g的H_g在整盘holomorphic**。有限原z-derivatives则通过chain rule在branchpoint至多有限poles，整盘meromorphic。这确实是一张非univalent、原三行共同图，没有拿Taylor小圆冒称处理critical fiber。

**R13.** 导数为

\[
|\varphi'(0)|=3/M<1.
\tag{R18}
\]

因此这张实际图连τ=0的positive log-derivative入口都不过，更不能使用原safe166/9取得strict CDT矛盾。本稿没有算其energy，也没有优化map或宣称所有ramified maps均受R18限制。它支付的是**合法共同图存在性**及这一张图的失败，不能把存在性当净算术holonomy收益。

作为scalar校准，取ρ1=−1/L1、同一T/盘。其他six-point ratios至少(α/b)^9>(16/13)^9>81/13>21/4；其中(16/13)^4>9/4，平方再乘16/13给最后界。故原四A/C也有显式doublefill共同图，derivative3/L1<1。主三行的R17采用其自身20-state equation，未免费从这个scalar校准继承共同图。

## 7. 剩余缺口、primary与运行

**R14.** 本轮可兑现的新接口是：实际生成微分方程的有限定义、完整head、dominant全部分支无log与真实分歧共同盘。仍未付原三行最小微分rank、其他finite点完整局部分类、0/∞/所有其他叶、全place paid normalization、较大共同图及strict energy比较。Root另攻all20 products和更广局部域，不能在本稿保存时预登记其未冻结证明。正式全局复盘cadence仍222→228、窗口226–230；此一张小图不能作为数值目标完成，原goal active。

primary实际使用范围：[Novikov–Yakovenko author PDF](https://www.wisdom.weizmann.ac.il/~yakov/mero-flat.pdf)，46页原件，仅实际FULL文本PDF33–38（完整§6及相邻页段），其中§6.1 univariate normalization区分非zero integer eigenvalue差；没有将多变量Theorem6.1的较强定义直接套给重复zero eigenspace。本稿R7自己证明包含重复0的收敛与无log。另实际读[NIST DLMF2.7(i)](https://dlmf.nist.gov/2.7.i)全部相关ordinary/regular条件、E1–E6与convergence句；它是二阶校准，未承担本高阶或20-state theorem。整HTML下载不称FULL阅读。原件、选段与实际范围另存[scope](../literature/pade_ramified_admission_sources_round226_20261008/dual_reading_scope.md)。

数学producer创建/执行/import/rerun、数学失败、CAS、序列/prime/参数/能量扫描、积分、PSLQ与Lean均0。只有文件读取、PDF文本提取、primary下载与hash等文档操作；既有224/225数学程序未重跑。初次读取一个错误文件名失败未写文件；首批较长aggregate输出有截断，截断部分不登记FULL，采用此前真实FULL和后续完整读取/完整sections，范围见scope。本文与scope保存后均需actual FULL作者复读并报final bytes/SHA；自己的作者读不替代独审。

