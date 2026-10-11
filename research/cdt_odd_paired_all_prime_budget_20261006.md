# 配对饱和整数格的全素数预算、真实 Plücker 分母与局部整数值模型

日期：2026-10-06。NEW 全尺度纸面证明；当前是供独审的候选稿，尚未提前冻结。所有冻结/同行数学 MD、PY、JSON、manifest 仅读，不执行、import或重跑。本稿自有 NEW 有理分段证书首次且唯一运行一次，291项exact checks通过。证书只积分已在正文证明的连续bound-model，不用有限n推成全尺度结论。

**实际进展。** 对同一个 rank2n 配对饱和整数值格的真实多项式 D_A(X)，保留 ambient degree<3n，得到全有限素数、全X系数的 common-content 下界。其可证明的安全 n² 费用为

\[
\boxed{A_{\rm pair}^{\rm safe}=
\frac{1085983123}{24190320}<44.894.}
\tag{B1}
\]

相比不分residue的同一格coarse fee60，严格改善大于15.106。本稿另证明支持敏感的 actual Plücker denominator refinement；其数值优化尚未被计入B1，不把有限格gcd当作免费real收益。还建立一个真实GL(Z_p)整数值局部基及其已证leading约束，未把它升级成未知Smith界。

没有 matched arithmetic/analytic margin；没有证明该paired多项式每个有理目标的无限nonzero。辅助素数两unit条件仍保持。没有新的特殊值无理性/线性无关性或Lean定理。B1是费用上界，比较不够不是actual费用下界或no-go。

## B2. 完全相同的格、form与degree

冻结 [integral lattice](cdt_odd_paired_head_free_integral_lattice_20261006.md) I1–I25实际完整读取。其整数值格 M₃ₙ有Newton基 f_i(t)=binom(t−1,i)、0≤i<3n。配对空间由 P(m)/d_m=P(m')/d_m'给出，m'=2n+1−m、d_j=(j)₆ₙ₊₁；primitive pair参数 p_m=d_m/g_m、q_m=d_m'/g_m，g_m=gcd(d_m,d_m')。真实饱和格 A_Z 的完整整数基为

\[
G_m=p_m L_m+q_mL_{m'},\quad1\le m\le n;
\qquad f_{2n},\ldots,f_{3n-1}.
\tag{B2}
\]

L_j是整数值cardinal polynomial。记基矩阵S∈Mat₃ₙ×₂ₙ(Z)。原三重零点form的参数固定B=6、κ=3、s=5；取固定a,b∈Z、b≠0，Λ_X为冻结 [arithmetic稿](cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md) A3–A4的实际partial fraction泛函。定义

\[
H_N(X)_{ij}=\Lambda_X(f_i f_j),\qquad
D_A(X)=\det(S^T H_N(X)S)\in\mathbf Q[X].
\tag{B3}
\]

这里没有first2n factorial normalizer。每个基degree≤3n−1，乘积degree≤6n−2。B3与冻结 [auxiliary稿](cdt_odd_paired_head_free_auxiliary_prime_20261006.md) A11、父任务 [actual analytic Plücker稿](cdt_odd_paired_head_free_analytic_plucker_root_20261006.md) R1–R6为同一个对象，不是quartic-zero布局。

固定a,b∈Q时，先选D>0使Da,Db∈Z，同时将整个form乘D。D_A因而乘D^(2n)，finite/real均付O(n)，不改变n²率。X=c=u/v∈Q的specialization整化另付v^(2n)。以下先对integer source及形式X证明，不能假设未知数值关系已成立。

## B4. 每个n、每个p的安全整数下界

v_p指whole Q[X]的Gauss valuation，v_p0=+∞。s5、integer sources下，integer-valued基的导数lcm、harmonics下标≤8n给

\[
v_p^{\rm Gauss}D_A\ge-10n\lfloor\log_p(8n)\rfloor
\qquad\text{所有 }p,n.
\tag{B4}
\]

理由：每个H_N entry至少−5floor(log_p8n)，实际S整数，两次basis乘法不使其变差；size2n determinant付2n倍。这包括p≤s与全部小n，未假设a,b的p-unit。对应导数身份为 lcm(1,…,i)f_i'(z)∈Z 对每个整数z，i<3n；harmonic与fixed factorial的实际费用在冻结arithmetic A3自证，不把derivative系数漏掉。

对p>6n，Newton values/derivatives、H_j与H₆ₙ₋ⱼ均integral；唯一可能H₂ₙ₊ⱼ的p分母被binom(2n+j,j)³的carry清掉。因此

\[
v_p^{\rm Gauss}D_A\ge0\quad(p>6n).
\tag{B5}
\]

B5包括6n<p≤8n，不仅pole下标范围；与小p界分开证明。

## B6. 全large-prime residue minors；保留largest2n factorial

若√(8n)<p≤6n，p²>8n，定义

\[
q_\rho=\lfloor(6n-\rho)/p\rfloor,
\quad w_\rho=2\lfloor6n/p\rfloor-2q_\rho
 +3\lfloor(2n+\rho)/p\rfloor-3\lfloor2n/p\rfloor,
\]
\[
e_\rho={\bf1}_{p>\max(6n-\rho,2n+\rho)},
\quad F_\rho(m)=m^2+(w_\rho-6)m+4(m-2q_\rho)^+
 +e_\rho{\bf1}_{m=1}.
\tag{B6}
\]

wρ∈{0,2,3,5}。任意m-order monomial minor of residue form≥Fρ(m)，m>2qρ+2时为0；tail rank≤2qρ、head rank≤2保证这条共同界。相邻marginals为

\[
\Delta_m=2m+w-7+4{\bf1}_{m>2q}
 +e({\bf1}_{m=1}-{\bf1}_{m=2}),
\tag{B7}
\]

非递减，所以有限分配是凸整数优化。ρ0的head实际rank1可改进，但此处用rank2弱界同样严格，未以single residue夸大主率改善。

记

\[
\Lambda_p=\min_{\sum_\rho m_\rho=2n,\ 0\le m_\rho\le2q_\rho+2}
\sum_\rho F_\rho(m_\rho),\qquad
E_p^{\max}=2\sum_{i=n}^{3n-1}\lfloor i/p\rfloor.
\tag{B8}
\]

所有2n×2n monomial minors都有下界Λp，按两次Cauchy–Binet及整数值基实际row/column factorial归一化，得到

\[
v_p^{\rm Gauss}D_A\ge\Lambda_p-E_p^{\max}.
\tag{B9}
\]

它保留degree3n中最大的2n项n..3n−1，而不是first2n项。B4在此large-p域又给−10n，所以实际安全下界是

\[
\ell_p=\max\{-10n,\Lambda_p-E_p^{\max}\}.
\tag{B10}
\]

对p≤√8n取ℓp=−10n floor(log_p8n)，对p>6n取0。全部ℓp为整数。Q_n=∏p p^ℓp是严格的signed common-content ratio，并有

\[
\boxed{D_A(X)/Q_n\in\mathbf Z[X].}
\tag{B11}
\]

positive ℓp 的真实信用保留，没有先裁成纯denominator，也未称其actual primitive gcd。若c=u/v且D_A(c)≠0，则v^(2n)D_A(c)/Q_n是非零整数，故 |D_A(c)|≥Q_n/v^(2n)。这项nonzero条件不由B11自带。

## B12. 有界连续费用；小x不能只积分未截断模型

取x=p/n、u=ρ/p，连续q=⌊6/x−u⌋，w=2·1_{u>{6/x}}+3·1_{u≥1−{2/x}}，e=1_{x>6−xu}1_{x>2+xu}。对各constant type，F是B6同式、capacity2q+2。定义

\[
\begin{aligned}
\mathcal C(x)&=x\min_{\int_0^1m(u)du=2/x}
\int_0^1F_{q(u),w(u),e(u)}(m(u))du,\\
\mathcal E(x)&=2\int_1^3\lfloor t/x\rfloor dt,\\
g_{\rm raw}(x)&=\mathcal C(x)-\mathcal E(x),\quad
g(x)=\max\{g_{\rm raw}(x),-10\},\qquad0<x\le6.
\end{aligned}
\tag{B12}
\]

m(u)是integer-valued measurable allocation；允许在同一type的不同u点分配相邻整数，不是让F对fractional m任意插值。通过排序凸marginals取前2单位weighted capacity，即得连续最小值。

这里min约束是2/x，ambientdegree还是3。未截断g_raw会包含−4/x级项，不能直接据它积分成有限n²费用；这不说明actualcost发散。B4的同一格entry bound正是合法截断。

更精确地，0<x≤1/4时 q_min≥6/x−2，ceil(2/x)≤2q_min。取m=floor(2/x)、ceil(2/x)按适当比例分配，可使全部m在tail容量内；e=0，w≤5。因此

\[
\mathcal C(x)\le4/x-2+x/4,
\quad\mathcal E(x)\ge8/x-4,
\quad g_{\rm raw}(x)\le-4/x+2+x/4\le-223/16<-10.
\]

于是

\[
\boxed{g(x)=-10\quad(0<x\le1/4).}
\tag{B13}
\]

小x model的积分不是未知尾项，恰为−5/2。

## B14. 精确有限分段积分及certificate的范围

在x≥1/4上，q≤24。type boundaries的scaled lengths由0、r₆=6−floor(6/x)x、r₂=(floor(2/x)+1)x−2、x的有序差给出。各length为affine x，每个type的integer marginals固定。将相同cost的marginals合并，其capacity亦affine；累积capacity首次达到resource2处得到affine cost。

Base breakpoints为1/j、2/j、3/j、6/j、8/j在[1/4,6]内的所有值：6、2给residue floors，3、1给largest-factorial floors，8给r₆与r₂的交点。再加入每个cumulative-capacity=2的affine根及g_raw=−10的根。在这些分段上g精确affine，并且有限。没有以finite n residue sampling代替整个连续优化。

自有 NEW [Fraction certificate](cdt_odd_paired_all_prime_budget_verify_20261006.py) 首次唯一运行一次，输出 [NEW JSON](cdt_odd_paired_all_prime_budget_verify_20261006.json)：47 base breakpoints、50最终segments、291 exact checks。interval内部的额外检查仅核代码分支与已列根相容；全分段覆盖依靠上述枚举证明，而不是sample本身。

精确输出为

\[
\int_0^6g(x)dx=-\frac{1085983123}{24190320},
\quad A_{\rm pair}^{\rm safe}\in[44.893,44.894),
\]
\[
60-A_{\rm pair}^{\rm safe}=\frac{365436077}{24190320}>15.106.
\tag{B14}
\]

程序只用stdlib Fraction、json、hashlib、pathlib，不读取或import任何旧/同行producer。全部segment的affine coefficients/endpoints/integrals在JSON中有理保存。B14是bound-model exact value，不是actual valuation/content equality，也不是特殊值定理。

## B15. 离散模型到PNT：真实全素数n²结论

对固定ε≥1/4，x∈[ε,6]的q/capacity/marginal均uniform bounded。type的整数residue数与连续length·n仅差O(1)，在各类填充整数资源2n与连续排序的差也为O(1)：只涉及有限类与一个cutoff marginal；partial allocation rounding可用下一marginal补完。factorial sums与B12积分的Riemann比较亦uniform O(1)。因而

\[
\ell_p\ge n g(p/n)-C\qquad(n/4<p\le6n),
\tag{B15}
\]

当n>128这整个区间在large-prime域；小n仍由B4–B11给全n有限整化，不被PNT覆盖而遗漏。由θ(T)=Σ_{p≤T}logp∼T以及bounded piecewise continuous test-function的PNT加权积分，B15给

\[
\liminf n^{-2}\sum_{n/4<p\le6n}\ell_p\log p
\ge\int_{1/4}^6g(x)dx.
\]

小prime p≤√8n的B4费用为O(n^{3/2}logn)；√8n<p≤n/4的entry bound付至多10nθ(n/4)=(5/2+o(1))n²。p>6n integral separate。故

\[
\boxed{\liminf_{n\to\infty}\frac1{n^2}\log Q_n
\ge-A_{\rm pair}^{\rm safe}.}
\tag{B16}
\]

同一格的coarse60依据亦明确：Σ_{p≤6n}floor(log_p8n)logp=θ(6n)+O(√n logn)∼6n，故B4直接给清分母费用≤(60+o(1))n²。B10/B12的max是两个合法valuation lower bounds取较强者；A_safe则是该signed lower bound积分的相反数，不把min-cost的方向倒置。

PNT test-function步骤只需对step functions先用θ，再以Riemann上下step逼近；实际阅读的Lai PDF12 Lemma5.1正给此论证。B16结合B11适用于同一个D_A的全部形式系数，未借quartic energy或不同norm的covolume。

## B17. actual Plücker支持与每个p更强的分母桥

S=diag(A_low,I_high)，因此非零u_I=detS_I必须含全部indices2n..3n−1，再选n个low indices0..2n−1。记真实非零support为ℐ*，而全部允许subsets为ℐ。所有u_I是整数且gcd1，由实际饱和格推出，不等于restricted Gram非退化。

令

\[
e_{I,p}=\sum_{i\in I}v_p(i!),\qquad
T_p=\max_{I\in\mathcal I^*}\{e_{I,p}-v_p(u_I)\}.
\tag{B17}
\]

对应Newton minor的确切row/column factorial费用是e_I+e_J：f_i的falling numerator到monomial为integer unitriangular，所有monomial2n-minor共界Λp经Cauchy–Binet保持，故

v_pdet(H_{N,I,J})≥Λp−e_I−e_J。

再在实际S两侧展开，得到比B9更精细的全n界

\[
\boxed{v_p^{\rm Gauss}D_A\ge\Lambda_p-2T_p,
\quad\text{还可取max}\{-10n,\Lambda_p-2T_p\}.}
\tag{B18}
\]

所有u_I的actual divisibility在这里真正计入；不能在real Plücker norm与finite T_p两处重复免费扣同一factor。T_p可通过diag(1/i!)S的full wedge最小valuation直接计算，等于其monomial coefficient wedge denominator：falling numerator的integer GL矩阵不改变所有maximal minors的共同min valuation。这是finite-place identity，不是不同格的norm替换。

本轮实际全文读父任务 [primitive gcd 稿](cdt_odd_paired_primitive_gcd_rate_20261006.md) G1–G10：其G3给同一primitive pair的gcd主率，G13给同一Cauchy平方展开的真实−2γ信用。这里S已经用primitive pair约除；B17只能按该实际S的u_I计费，不在B11之外再将G13当一次免费common-content除法。

由真实support与gcd1，至少一个u_I在给定p为unit，所以准确有

\[
\sum_{i=0}^{n-1}v_p(i!)+\sum_{i=2n}^{3n-1}v_p(i!)
\le T_p\le\sum_{i=n}^{3n-1}v_p(i!).
\tag{B19}
\]

因此B18严格包含B9；B14的数值只使用右侧安全upper，不声称已经算完T_p。左侧说明单靠这个common monomial-minor transfer的Plücker优化不能消除small-x问题：其连续最小factorial费为2[∫₀¹floor(t/x)+∫₂³floor(t/x)]≥6/x−4；结合B13的feasible LP upper，该transfer模型甚至至多−2/x+2+x/4。必须仍保留entry cap或建立真正新的整数值局部rank估计。这只是指定bound-model结构，绝不是actual cost或整个方法的no-go。

## B20. 真实p局部整数值基：已证GL与leading范围

在p²>8n且i<3n下，写i=i₀+pi₁，0≤i₀<p、0≤i₁<p，令

\[
\psi_p(t)=\frac{t^p-t}{p},\qquad
b_i(t)=\binom{t}{i_0}\binom{\psi_p(t)}{i_1}.
\tag{B20}
\]

对t∈Z_p，ψ_p(t)∈Z_p，两个binomial denominators均p-unit，所以b_i是Z_p-integer-valued。用finite differences在整数0,…,i展开到binom(t,j)，所有coefficients属Z_p；degree为i，leading与binom(t,i)之比

\[
\frac{i!}{i_0!\,i_1!\,p^{i_1}}
\]

为p-unit，因为i<p²给v_p(i!)=i₁。因此所有b_i、i<3n与原Newton基的变换实际属于GL₃ₙ(Z_p)，未用超越或未计分母gauge。该结论只用于finite-place，不把其real norm当1。

对整数a与Y∈Z_p，binomial展开给

\[
\psi_p(a+pY)\equiv\psi_p(a)-Y\pmod p,
\quad p\psi'_p(a+pY)\equiv-1\pmod p.
\tag{B21}
\]

后者是pψ'=pt^{p−1}−1。前者展开(t+pY)^p时除以p后的非constant terms皆在pZ_p（p2也成立）。在site t=a−ℓp上，这给ψ value≡ψ(a)+ℓ；binom(t,i₀) reduction只依赖a modp，且p times其derivative为0 modp。于是每residue的leading evaluation及p-scaled first derivative仅通过i₁方向的ψ polynomial与其导数变化。

若3n=qp+r、0≤r<p，degree restriction保留q个完整i₁ layers和一个仅i₀<r的ragged layer，不能免费扩成p(q+1)维。对actual paired格还必须同时变换S，局部G或Plücker条件不消失。B20–B21没有给出全部p-powers的tail/head Schur，未证明其Smith下界、actual restricted rank或n²费用节省；尚未把它计入B1。它是可正确开展新rank估计的整模型接口。

## B22. 来源实际阅读、执行与当前未补项

本轮实际完整读取冻结lattice I1–I25、arithmetic A1–A14（含A30a）、root budget R1–R9、auxiliary A1–A13、root actual analytic Plücker R1–R6。初次批量读取arith/root出现组合输出截断，随后以足够output budget重新全文读取成功；不将被截断片段当已完成阅读。所有linked数学producers均未执行/import。

另实际全文只读本轮父任务primitive gcd G1–G10（所有G1–G13编号公式），其same-object费用归属用于B18的接口说明；仅读其MD，不执行它的PY。

一手来源[Lai原件](../literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf)本轮新增实际完整读取PDF8–16，共9页，尤其Lemma4.3/4.4的integer shift/minor证明、Lemma5.1的PNT测试函数、原weight4的分段求和。此前实际已读PDF1–7、17–25共16页，因此审阅者累计覆盖1–25，但不称本轮全文25页。本文s5/F-tail4/配对size2n/最大2n factorial/cap−10均独立推导，不移植该原件weight4的30.83。未新增PDF下载。

本轮自己NEW数学producer1个、首次唯一执行1次、PASS291；旧/同行数学执行import重跑0；PDF抽文本、hash和JSON metadata读取非数学producer。NEW来源收据另存，不改历史收据。本候选保存后全文回读并交独审，最终冻结状态另报。

未补：B17实际T_p的主率精确优化；B20在paired格上的全部rank/Smith提升；同一个D_A的充分解析衰减及strict margin；两个辅助finite-field determinants在无限prime上为unit。这些gate不因B16的safeA变成已证。若未来针对同一D_A证明β>A_safe且无限nonzero，才可结合product formula得到数值结果。
