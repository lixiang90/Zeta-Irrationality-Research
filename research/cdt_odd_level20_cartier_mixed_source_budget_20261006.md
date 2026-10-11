# mod p primitive 的 mixed source 次数与第二层接口

日期：2026-10-06。本文只新增，不修改冻结稿、不运行旧producer。输入为 [第二层packet](cdt_odd_level20_cartier_packet_s2_20261006.md)、[Hasse商](cdt_odd_level20_hasse_20261006.md)、新增的 [有理原函数](cdt_odd_level20_cartier_rational_primitive_20261006.md)、[三jet/q-Bockstein](cdt_odd_level20_cartier_mixed_bockstein_20261006.md) 和 [固定rank19 source](cdt_odd_level20_cartier_rank19_budget_20261006.md)。研究的是原整格内一条混合消除路线的次数与层数；不是已经成功的slow coker解，也没有新增数值无理性定理。

## 1. 原source中的问题与条件输入

取好未分歧place、p≥7、p²>N，N=19(D+1)+O(1)，并排除固定规范及周期分母。令O为局部整数环、k为剩余域、ϑ=t∂t。原degree≤D pure source E_D包含六个I_j，以及三个旧species

\[
 F_r=g\vartheta^rH_-,\quad r=0,1,2,
 \qquad g=\Delta^2,\quad\deg g=8,
\]

其统一integral evaluation是Ψ=p⁴eval。记Y=p³H_-、Z_c=p⁴Σc_jI_j，c₀∈ker M̄_p。于是Z_c∈pO[t]/t^N，而旧columns为p·gϑ^rY，本来已有baseline1。

新增有理原函数稿提供本题的全char-p输入

\[
 P=P_{\rm Hasse},\quad P(0)=1,\quad\deg P=3p-3,
 \quad u=J/P,\quad\deg J\le3p-3,\quad u(0)=0,
\]
\[
 \vartheta(uA_-)=Q_cA_-,\qquad
 Q_c=P_c/[(1-t)N_-C_-],\quad\deg P_c\le5.
\tag{M1}
\]

M1是全formal **mod p** 身份；其证明依赖链接稿的relative Cartier、rational exactness与pole bounds，这里不以formal逐项积分代替它。该稿更给degP_c≤4与P_c(0)=P_c(1)=0；下面次数账本不需加强原先≤5的安全界。取任一integral lift ĉ₀，置W_c=Z_ĉ₀/p modp。冻结packet给

\[
 \vartheta W_c=(Q_cA_-)\bar f_\varepsilon(t^p),
\]

所以M1只推出

\[
 W_c-uA_-\bar f_\varepsilon(t^p)=R_c(t^p)
       \pmod{t^N}
\tag{M2}
\]

的某个slow余项，R_c(0)=0。ϑ的kernel由p倍次数组成；R_c不因ϑ身份自动为零。真实ΘA载体保留在f_ε中，没有把char0 exactness或modp primitive混淆。

## 2. 直接清P：degree约3p的安全接口

使用原坐标、integral coefficient lifts，取row的六I坐标为gP·c₀、旧F₀坐标为−J、其余旧F坐标为0。其原Ψ像为

\[
 X=(gP)Z_c-pJgY,
 \qquad \bar X/p=gP\,R_c(t^p).
\tag{M3}
\]

新I坐标nonzero，所以该row primitive；gP作为t=0的formal unit允许局部分析，却不是degree≤D polynomial source的免费unit。清分母后source degree恰为deg(gP)=3p+5（c₀≠0），旧coefficient J的degree较小。因此该具体row在E_D中的polynomial multiples只能先选

\[
 \deg h\le D-(3p+5),\qquad
 r_{\rm clear}=(D-3p-4)_+.
\tag{M4}
\]

窗口为p≤D/3+O(1)，完整N仍须用于全部身份。M3的余项乘以gP后通常又含非p倍support；可用formal unit除回M2分析，但不能把乘过gP的输出直接叫成纯slow列。

## 3. 三jet插值：可避免清P的约1.5p接口

M1本身还允许一个较短的代数表示。记

\[
 \ell_1=\vartheta A_-/A_-,\qquad
 \ell_2=\vartheta^2A_-/A_-,\qquad
 q=\operatorname{rad}(N_-C_-P),\quad d=\deg q.
\]

Hasse logder身份给ℓ₁在q的各非零根ξ有simple principal partρξ/(t−ξ)。固定N、C各自simple且互不碰撞的坏素数只需排有限个；P与N或C的碰撞不能排成有限集合，须保留。P重数e为0、1、2，ρ相应为e、e+1或e+1/2，非零者在p≥7均为unit。ℓ₂的double principal coefficient是ρ(ρ−1)ξ²。ρ=1的点，P至多simple或为N-only，故u=J/P没有double pole。其它double poles可用ℓ₂匹配，再用ℓ₁匹配剩余simple poles。

具体地，写ℓ₁=L₁/q、ℓ₂=L₂/q²、u=U/q²。gcd(L₁,q)=1。令q₂=gcd(q,L₂)；上述ρ=1条件给q₂|U。CRT解

\[
 V_2(L_2/q_2)=U/q_2\pmod{q/q_2},\qquad
 V_2=0\pmod{q_2},\quad\deg V_2<d.
\]

然后u−V₂ℓ₂=U₁/q；再解V₁L₁=U₁ modq、degV₁<d。余项V₀没有有限极点，因而是polynomial。这一无根算法的coefficients在k，自动处理P与NC相交。

在∞，ℓ₁的constant为degN+½degC+degP=2+1+3p−3=3p=0，因此ℓ₁、ℓ₂都是O(t⁻¹)；u bounded。于是degV₀≤d−2，而

\[
 uA_-=V_0A_-+V_1\vartheta A_-+V_2\vartheta^2A_-,
 \qquad\deg V_i\le d-1
 \le\frac{3p+7}{2}.
\tag{M5}
\]

M5的上界使用deg radP≤(3p+1)/2和deg(NC)=4；不是声明每个u都具有同样的最小degree。

原source的新row可以取I坐标g·c₀、旧F_r坐标−V_r；其Ψ像为

\[
 X=gZ_c-pg\sum_{r=0}^2V_r\vartheta^rY,
 \qquad \bar X/p=g\,R_c(t^p).
\tag{M6}
\]

所以不必把P当成source乘子。统一安全degree可取δ_p=(3p+7)/2（p≥7时已大于8），选multipliers的明确安全范围为

\[
 \deg h\le D-\delta_p,\qquad
 r_{\rm jet}=(D-\delta_p+1)_+.
\tag{M7}
\]

对应窗口到约2D/3。实际V_i可能更低degree；新的μ-basis或更低degree族须另记账，不由M7排除。

## 4. 真正的S2仍是完整Bockstein余核条件

令\(\bar\Psi_D\)为原source完整prefix的modp矩阵。在原E_D中取任意residue rowv∈kerΨ̄_D，并以其degree≤D integral lift定义

\[
 \beta_D(v)=[\Psi_D(\hat v)/p]
       \in\operatorname{coker}\bar\Psi_D.
\]

则v能在**同一个E_D**中提升成primitive S2，当且仅当β_D(v)=0。M3或M6只把该类的一个代表变为已知多项式乘slow余项，尚未证明其为零。

在此unit表中，其余13species的Ψ列本来divp，所以barΨ_D的像只来自六I。若v̂+p w_D成功，可移去w_D的background和old coordinates而不影响S2，因为它们的p倍评价已divp²。因此本节固定residue row的第二层lift可保持在同一九species支持内。这不允许另外加入unit background residue来改变v；后者是不同的mixed family。

还有一个source-degree陷阱：off-p row的degree≤δ，不等于成功lift也degree≤δ。若S2只通过v̂+p w_D、degw_D=D实现，不能再任意乘h并仍留E_D。要计满M4或M7的multiples，必须逐个证明所选h·v的β_D类为零，或者另证明base lift的所有correction degree≤δ。单个slow成功不自动给全span的成功。

新增三jet/q-Bockstein稿的M17只允许constant c₁改变ĉ→ĉ+pc₁，保留q坐标的完整horizontal余项。若其明确slow前缀条件成功，新I coefficients仍是g(ĉ+pc₁)，旧coefficients仍是V_r，所以base lift的degree确≤δ，随后按M7乘h是合法的。这是一个更窄、可以保持次数的充分接口；本稿没有证明M17有任何nonzero可解方向。

旧H的baseline1 rows可以用来形成M6。已经计入的Hasse两行在共同p⁴评价中是threshold2；旧平方lift行是threshold3。因此这些旧高层行的Ψ/p modp均为0：添加它们不能改变β_D，也不能自动解决新的slow余类。相反，成功mixed row若保留nonzero I投影，可以提供与旧H高层空间独立的新threshold2。

## 5. 不重复计第一层的明确条件账本

设k_p=dimkerM̄_p≤3，选择k_p个independent c₀，并按M4或M7选定multiples。它们的I投影分别为gP h c₀或g h c₀，彼此residue-independent。但每一row的**第一层**已经落在native kerM的polynomial shifts加旧species baseline1的空间内；off-p primitive没有新增第一层质量。

令q_p为选定span中能在E_D内成功S2的、以I投影衡量的rank。对于本稿固定safe multiplier-family，仅有

\[
 0\le q_p\le k_p r_p\le3r_p;
\tag{M8}
\]

没有正q_p下界。若成功，threshold2可追加q_p；threshold1不能再重复追加同一个q_p，threshold3、4则没有自动信用。独立性依据是new mixed span的I投影injective，而旧已计高层空间只支持H坐标；无需把mixed row误称为pure-I支持。

在同一matching内窗与field-normalized PNT下，即使所有好prime k_p=3、所有余核条件都成功，固定安全族的**新增第二层**D²信用至多

\[
 \Gamma_{2,\rm clear}(a)
 \le3\int_0^{\min(a,1/3)}(1-3x)\,dx\le\frac12,
\]
\[
 \Gamma_{2,\rm jet}(a)
 \le3\int_0^{\min(a,2/3)}(1-\tfrac32x)\,dx\le1.
\tag{M9}
\]

这些是规定safe multiplier族的乐观上界，不是所有mixed char-p primitives的全方法上界；尤其不能从degree上界推断其实际最小degree。若从未计native S1的冻结rank19表起步，只认领这些成功rows，可同时计它们的两层，最多2Γ₂；若已认领全部native S1，则只能追加Γ₂。二者是同一方向的不同账本，不能叠加成三层。

实际global桥仍须证明这些threshold计数取代同一baseline，而非重复raw row因子。若通过原integrated tensor接口认领，新增finite归一信用为Γ₂/19，cost信用为2Γ₂/361；所有small powers、fixed bad places及窗口外成本仍保留。既有 [same-nine-species/cap4/≤2D ceiling](cdt_odd_level20_cartier_native_s1_budget_20261006.md) 也涵盖本路线在该范围内的信用，所以这些规定输入不足以跨log16。它不排background混合、窗口外、更高Smith阶或改变完整source。

M1与M5已给出次数可控的off-p接口。剩余最小可执行目标是：在原degree-D source对M7指定span证明β_D=0（或取得上述constant-c₁接口的nonzero解）；以I投影给primitive independent rank；再按实际prefix与同一baseline接globally。仅M1或M5不完成这些步骤。

## 6. 核验范围

本文不执行任何producer、不扫描素数。M3/M6是原source坐标的直接代数身份；M5是M1条件下的polynomial CRT证明，包含不能排除的P与NC碰撞；M9只使用两个固定斜率3、3/2的有理积分。未取得slow coker成功、正密度、S3或新global高度定理。旧冻结报告和证书均未改。

root已实际完整只读§§1–6并独审通过：原p⁴ source坐标、两种degree接口、全碰撞无根CRT、成功lift的degree陷阱、constant-c₁成功时仍保留δ、只新增threshold2、规定safe-family的Γ≤1/2或1，以及可删p倍background lift的支持澄清。该审阅没有把M17可解、safe degree是全方法最小degree、unit background residue或净Smith高度认领成已证；root未执行producer。

本文已冻结；后续unit background residue、slow coker或更高层研究另建报告，不修改冻结输入。
