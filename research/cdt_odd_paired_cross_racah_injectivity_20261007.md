# 固定 λ2 真实交叉块的第二 Racah 正常性、显式右逆与混合核判据

2026-10-07，NEW，/root/conifold_arithmetic_hypothesis。本轮504既存记录（503数学文件加1执行guard）及全部旧、同行producer/JSON/审阅/收据只读；旧/同行execute/import/rerun0。本文纯纸面推导，当前新增数学程序执行0。实际目标、middle、halfjet和固定两个第五幂种子全部保留；不证明无限M5 unit或新特殊值定理。本文仍待root/同行全文独审，不提前冻结最终来源收据。

## 1. 实际输入与同一目标

实际全文读取当前main §§138–141，物理SHA0013e246f36b8d538e9555839b611283a3f90e7be9784c28e11469b1b0a9c2ab；audit research/cdt_odd_delivery_20261006.json前70行，SHA8963ba9b895508a2fed9438d3011175b556bf6fc4d1b3dacf3b75a314b58b603。两者是本轮开始时的实际读取快照，不要求以后可变main/audit保持这些指纹。完整回读冻结2e04十一节R1–R30、冻结f988十一节Z1–Z23。

p=18r+1素数，a=5r，F=Fp，u=y²，
\[
S(u)=\prod_{j=a+1}^{9r}(u-j^2),\qquad
S(k^2)=\frac{(-1)^{r+k+1}}{(a-k)!(a+k)!}.
\tag{C1}
\]
记Σ_l为k=−l,…,l的和。沿用实际forms
\[
G(f)=\tfrac12(\Sigma_a+\Sigma_{r-1})S^{-5}f,\quad
C(f)=\tfrac12(5\Sigma_a-\Sigma_{r-1})S^{-1}f,\quad
H(f)=\tfrac12(\Sigma_a+\Sigma_{r-1})S^3f.
\tag{C2}
\]
它们作用于u-polynomials。deg T<r、deg Q<3r；原4r矩阵M5=[[G,C],[Ct,H]]。G的未知高阶moments仅由两个实际第五幂种子A0/A1和明确双boundary决定，不能generic化。

本文先证明一种**不同于完整三次权重**的正常性，再将它用于实际C。完整权重只是已付费合法工具，不删除C2的middle。

## 2. 完整交叉权重是第二族 Racah

定义
\[
J(f)=\tfrac12\Sigma_a S(k^2)^{-1}f(k^2),\quad
s_0=S(0)=(-1)^{r+1}/(a!)^2.
\tag{C3}
\]
折叠后
\[
J(f)=\tfrac12s_0^{-1}\sum_{k=0}^a v_k f(k^2),\quad
v_0=1,\qquad v_k=2\frac{(a+1)_k}{(-a)_k}\quad(k>0).
\tag{C4}
\]
这恰是KS Eq1.2.2在
\[
\alpha=-a-1,\quad\beta=2a+1,\quad\gamma=a,\quad\delta=-a-1,
\quad g=\gamma+\delta+1=0
\tag{C5}
\]
的有限有理极限。对应多项式
\[
P_n(u)={}_4F_3
\left(\begin{matrix}-n,n+a+1,-y,y\\-a,a+1,a+1\end{matrix};1\right),
\quad0\le n\le a.
\tag{C6}
\]
P_n(0)=1；其最高项系数为
\[
\ell_n=\frac{(n+a+1)_n}{(-a)_n(a+1)_n^2}.
\tag{C7}
\]

证明及极限范围：保持α+1=−a，用KS有限有理正交恒等式，并取γ=a+epsilon、δ=−a−1，最后epsilon→0。含g因子
(g)_k(1+g/2)_k/(g/2)_k在k0恒1、k>0趋2k!。其他Pochhammer两次(a+1)/(-a)与一次反向cancel，正好得C4；不能把k0也设为2。全部求和以内分母在极限处非零；有限正交身份由非空通常参数域延拓为有理恒等式。不存在有限域positivity假设。

## 3. 所有完整交叉 profiles 的单位范数

KS PDF29 Eq1.2.2逐因子特化给
\[
\sum_{k=0}^a v_kP_n(k^2)P_m(k^2)=\nu_n\delta_{nm},
\tag{C8}
\]
\[
\nu_0=(-1)^a\frac{(2a+1)!}{(a+1)(a!)^2},\qquad
\frac{\nu_n}{\nu_0}
=\frac{(n+a+1)_n(n!)^3(2a+2)_n}
{(a+2)_{2n}(-a)_n(a+1)_n^2}.
\tag{C9}
\]
Norm numerator中的三个因素是(1)_n、(1)_n、(2a+2)_n；不是把旧三次族的(-2a)_n³沿用过来。原件已实际文本读并渲染PDF29目视核对。

**Theorem C10。** 每个实际p18r1及0≤n≤a，ν_n、ell_n全为F单位，故完整J所有leading Hankel profiles d≤a+1可逆。

所有factorial/Pochhammer因素的绝对值严格小于p，最大指标3a+1=15r+1<p；(-a)_n在n≤a无零。n0空积另算。因此
\[
\jmath_n=J(P_n^2)=s_0^{-1}\nu_n/2\in F^\times,\quad
\det J^{[d]}=\prod_{n<d}\jmath_n/\ell_n^2\in F^\times.
\tag{C11}
\]
这个定理完整保留终止节点与halfjet，不假设实际G、H、M5或其任何中间leading minor可逆。C3常数也与冻结Z15的直接完整boundary求值一致：
J(1)=−(2a+1)!/(2a+2)。

## 4. 消去真实middle的检验多项式：实际C满行秩

令
\[
\mathfrak m(u)=\prod_{k=0}^{r-1}(u-k^2).
\tag{C12}
\]
这是degree r的monic polynomial，严格在全部实际middle节点上为0，包括原点。对deg T<r、deg W<2r，Q=mathfrak m W具有deg Q<3r，且C2准确给
\[
\boxed{C(T,\mathfrak m W)=5J(T\mathfrak m,W).}
\tag{C13}
\]

**Theorem C14。** 对每个实际辅助素数p，原固定λ2交叉矩阵C（r×3r）行秩准确r；C^t: F[u]_<r→F[u]_<3r^*是单射。

若C(T,Q)=0对全部deg Q<3r成立，则C13给J(Tmathfrak m,W)=0对全部deg W<2r成立。Tmathfrak m具有deg<2r，C10的完整J^[2r]非退化，故Tmathfrak m=0，因而T=0。这个证明只除已证完整norm，并未除实际cross leading r×r minor，也未要求任何perfect intermediate path。

更一般的support lemma：若非退化complete functional在degrees<t+m的leading profile正常，mask支撑于m个不同节点，cross等于c·complete减去mask项，c非零，且第一/第二degrees分别<t、<t+2m，则乘其monic vanishing polynomial可证明该rectangular cross满行秩t。当前t=m=r恰达degree cutoff3r。

在M5核中，(T,0)不可能非零；核向Q的投影单射。这不是M5 unit，也不保证C在ker H上的限制单射，更不保证有限域任何相关Gram非退化。

## 5. 只用已知单位的显式右逆和完整ker C基

全部以下矩阵以monomial coefficient bases计算。令L（2r×r）表示乘mathfrak m：T↦mathfrak m T，按前r/后r系数分成L=(L0;L1)。L1是对角全1的upper triangular，detL1=1。令
\[
Z_+=\binom{0}{L_1^{-t}},\qquad
Z_0=\binom{I_r}{-L_1^{-t}L_0^t},
\quad L^tZ_+=I,\ L^tZ_0=0.
\tag{C15}
\]
置J2=J^[2r]、W+=J2^-1 Z+/5、W0=J2^-1 Z0，并用相应columns作为W-polynomials。定义r个Q-polynomials
\[
\mathcal R_j=\mathfrak m W_{+,j}.
\tag{C16}
\]
C13立即给C(u^i,R_j)=delta_ij。所有inverse分母只有5、J2和monic L1，均已证单位。

记Csmall=[C(u^i,u^j)]_(i,j<r)，它是冻结Z15的全显式实际cross，无未知A0/A1。2r个kernel polynomials为
\[
\mathcal K_j=u^j-\sum_i\mathcal R_i(Csmall)_{ij}\quad(j<r),
\qquad
\mathcal K_{r+j}=\mathfrak m W_{0,j}\quad(j<r).
\tag{C17}
\]
它们在ker C，且组成其完整基：按mathfrak m作Euclidean division，前r个具有独立remainders，后r个具有独立quotients。于是
U=(R_0,…,R_(r−1),K_0,…,K_(2r−1))是原Q-space的完整basis，C U=[I_r,0]。

**确定行列式尺度。**
\[
\boxed{\det U=5^{-r}\det(J2)^{-1}\in F^\times.}
\tag{C18}
\]
按division coordinates (W coefficients,remainder coefficients)，从上述column排列移成(W+,W0,remainder)需sign(−1)^r；det[Z+,Z0]=(−1)^r detL1^-t=(−1)^r，两个sign抵消。monic division synthesis的det为1（交换2r与r blocks的sign为1）。因此C18不含未知actual cross minor。有限处这个局部basis变化不替换原S或其arch范数，不免费提供p-independent global rational gauge。

## 6. 同一目标的canonical mixed-boundary判据

以U作原Q-space congruence，写H'=U^t H U，分成r/2r blocks H11,H12,H21,H22。准确
\[
M'=\begin{pmatrix}
G&I&0\\ I&H11&H12\\0&H21&H22
\end{pmatrix},
\quad\det M'=(\det U)^2\det M5.
\tag{C19}
\]
不除G或任何H-block。核的第一行q1=−G t；消去q1得到
\[
\mathscr B=\begin{pmatrix}
I_r-H11\,G&H12\\-H21\,G&H22
\end{pmatrix}\quad(3r\times3r),
\tag{C20}
\]
\[
\boxed{\det M5=(-1)^r5^{2r}\det(J2)^2\det\mathscr B,
\quad\operatorname{corank}M5=\operatorname{corank}\mathscr B.}
\tag{C21}
\]
列排列(q1,t,q2)的sign为(−1)^(r²)=(−1)^r；identity pivot合法。核从(t,q2)重建q=R(−G t)+K q2。所有prefactors已证单位，G仍是两个固定实际种子的matrix。

冻结R20的2r矩阵N与此canonical gate直接相连：
\[
\det N=
\frac{5^{2r}\det(J2)^2}{\det E\,\det D_H}\det\mathscr B.
\tag{C22}
\]
D_H/E是上轮已证单位。C22没有把3r称为更小维数；新收益是actual C被显式单位规约，canonical identity block不需要任何unknown norm。

**Conditional r-gate。** 若实际H22=H|ker C非退化，才可令
H_eff=H11−H12 H22^-1H21，得到
\[
\det M5=(-1)^r5^{2r}\det(J2)^2\det H22\,
\det(I_r-H_{\rm eff}G),\qquad
\operatorname{corank}M5\le r.
\tag{C23}
\]
这把实际防相消变成r阶identity减fixed two-seed矩阵；H22正常性和最终det非零均未证明。H22奇异时C20–22仍准确，不将这个条件误列成目标非零的必要条件。H22的核精确意味着q∈ker C且Hq∈im C^t，范围比ker H∩ker C更大。

## 7. 两族完整变换给cross/border的全显式连接递推

记上轮完整三次族R_m和norm d_m，新的cross族P_n和normj_n。共同Newton basis
F_j(u)=prod_(i<j)(u−i²)给
\[
R_m=\sum_{j\le m} A^H_{mj}F_j,\quad
A^H_{mj}=\binom mj\frac{(m-3a-1)_j}{(-a)_j^3},
\]
\[
P_n=\sum_{j\le n} A^C_{nj}F_j,\quad
A^C_{nj}=\binom nj\frac{(n+a+1)_j}{(-a)_j(a+1)_j^2}.
\tag{C24}
\]
两组diagonal均为已知units。完整connection R_m=sum_(n≤m) B_mn P_n由下降递推
\[
B_{mm}=\kappa_m/\ell_m,\quad
B_{mn}=\frac{A^H_{mn}-\sum_{k=n+1}^{m}B_{mk}A^C_{kn}}{\ell_n}
\quad(n<m)
\tag{C25}
\]
准确求出，全部m≤a合法。只除ell_n，不除intermediate modified norms，允许真实mask任意奇异。

令d=3r，u_k=k²(k<r)，A_nk=P_n(u_k)(n<r)，V_mk=R_m(u_k)(m<d)，Ec=diag(S(0)^−1/2,S(1)^−1,…,S((r−1)²)^−1)。在这两个basis间，
\[
C_{nm}=5\jmath_n B_{mn}-(A E_c V^t)_{nm}.
\tag{C26}
\]
完整orthogonality使n>m的first term严格0。三次D_H在Rbasis为diag d_m，故原2r N的cross/border块
\[
\boxed{C D_H^{-1}V
=5\,\operatorname{diag}(\jmath_n)\,B_{[d,r]}^t
\,\operatorname{diag}(d_m^{-1})V
-A E_c(V^tD_H^{-1}V).}
\tag{C27}
\]
这为目标提供两族unit-denominator有限connection及真实middle kernel的全显式formula。C27是在所述P_n/R_m两个已付费unit bases中的相应block，T-basis变化必须同时作用于G，不直接当作旧monomial矩阵的逐entry数值。χ的第二项仍在；不能由完整transform可逆推出其压缩block单位。C24–27没有新未知hypergeometric seeds，未知仍只在G的两个指定第五幂值。

## 8. 自然contiguous路径的全尺度实际rank collapse

不能用Racah doubles的印刷正交关系免费假定全部中间norm正常。具体从上轮三次族按Racah-I移动j步，参数为
(-a−1,−2a−1+j,−a−1+j,a−j)，保持g0与终止α+1=−a。0≤j≤a时fold weights准确为
\[
v_0^{(j)}=1,\qquad
v_k^{(j)}=
2\frac{(-a)_k^2(-a+j)_k}{(a+1)_k^2(a+1-j)_k}
\quad(1\le k\le a).
\tag{C28}
\]
在F中所有分母units，support恰为k0,…,a−j。因此完整(a+1)moment matrix秩恰a−j+1（不同squares的Vandermonde、非零支持权重）。特别j=a是确切rank1，不是数值异常；j=2r+2≤a时支持数3r−1，3r-profile必奇异。

继续I至2a+1步再用II至2a+1步，在参数层面可以到C5，但途中上述rank collapse已发生，随后还可能跨分母poles。故这条自然shift path不能在“每步unit norm”假设下计算目标。C25是直接完整两族的三角connection，绕开该无效假设，而不是宣称所有其他path也失败。C28不是actual M5反例，是具体Christoffel转移函数族的全尺度rank障碍。

## 9. 与higher-source Gram接口的准确范围

root研究的source-a斜率是E-map在leading radical上的Gram。本轮已经实际全文读取 NEW [source-radical稿](cdt_odd_paired_source_radical_response_20261007.md) S1–S6各节、公式S1–S14，并再次读取冻结bordered稿B1–B2的实际L/J/D。以下独证代数identity并将完整cross准确接回其物理half-fold；不把root首次程序的S6/S8范围冒记为对S12–14的有限验证。

令D是非退化diagonal node metric，Z/J均full-column-rank，im Z=ker L。设eta diagonal，K=5I−6eta，定义
G_L=L D^-1 L^t、C_L=L K J、H_J=J^t D J、F_L=L(1−eta)J。故C_L+LJ=6F_L。对leading kernel参数(t,q)满足G_L t=C_L q、H_J q=C_L^t t，用
Zz=(KJq−D^-1L^t t)/6恢复z，设Ev=Zz−(1−eta)Jq，得到
\[
Ev=-(Jq+D^{-1}L^t t)/6,\qquad
(Ev)^tD(Ev')=(t^tF_Lq'+t'^tF_Lq)/6.
\tag{C29}
\]
证明：展开右侧Gram乘36，前两项q^tH_Jq'和t^tG_Lt'，由kernel equations改写成t'^tC_Lq与t^tC_Lq'，其余两项是LJ；再C_L+LJ=6F_L。恢复z确在im Z是第一kernel equation的另一种写法；若适用原leading block，其second equation同样给H_Jq=C_L^tt。

**Theorem C30（实际质量map单射）。** 在source-radical稿的真实L/Z/J/D和原fixed λ2 leading radical上，E是单射。

若Ev0，则Jq=−D^-1L^t t，因此H_Jq=−(LJ)^tt；结合second kernel equation得6F_L^tt0。C10的完整J^[r]单位使这个完整rectangular F_L满行秩r，故t0；J单射迫q0，Z单射迫z0。这里甚至不需要C14的实际modified cross，只需本轮第二Racah的完整normality。

实际fold identification：冻结B1给L_(i,l)=T_i(a_l)/(A'(a_l)S(a_l))及J_(l,j)=A'(a_l)Q_j(a_l)，所以L(1−eta)J准确是sum_l (1−eta_l)T_i(a_l)Q_j(a_l)/S(a_l)，没有κ额外系数。这里a_l=−l、l0,…,6r−1、c=8r+1，在F中c/2=13r+1，centered y=a_l−c/2=5r−l。reflection-common节点恰l=4r+1,…,6r−1，故|y|<r上每次eta=1/2，其余eta0。nonzero middle的正负两次各1/2，原点只有一次1/2；outer正y=r,…,5r各出现一次。对even T/Q及S，正好

F_L(T,Q)=½Σ_(y=−5r)^(5r) S(y²)^−1 T(y²)Q(y²)=J(TQ)。

这里所有T/Q基改动是明确单位monomial变换，原点halfjet没有抹去。由C10完整J首r阶单位得F_L满行秩，上一段代数证明因此在实际模型无条件适用。C29还能给rank(G_K)≤2rank(t:K→F^r)；但**E单射仍不推出其restricted Gram非退化**。C29保留真正防相消问题，而不是用finite-field positivity填空。

下一足够精确的问题是：以C17给出的真实ker C basis计算H22及C27的cross-boundary块，在actual第五幂种子处证明C20无混合核，或证明C23的两项具体normality。它们都保留λ2、profile(r,3r)、halfjet与χ，允许所有不相关中间profiles奇异。

## 10. 新primary、实际读域及费用边界

正常TLS新增独立原件两份，共45archivepages：

- Mañas，Pearson Equations … III，https://arxiv.org/pdf/2107.02918v2，18页，实际完整文本PDF1–4,7–10,12–14，11distinct。PDF2–3要求Hankel minors非零；PDF7 Proposition4明确要求各shifted Gram的Cholesky，PDF8 Christoffel公式要求所除evaluation不为0；PDF12–14保留second-kind/masses与边界。不把这些前提当作当前目标已证。
- Oste–Van der Jeugt，Doubling (Dual) Hahn …，https://arxiv.org/pdf/1507.01821v3，27页，实际完整PDF1,16–18,23–25，7distinct。Eq5.3/5.5的分母、Appendix Theorem11四个specific shifts和n/x与α/γ、β/δ交换已读；Proposition12的实正参数条件不适用于本Fp目标，本文只用有理身份并独证C28边界。

本轮复用KS归档原件，实际完整PDF28–30三页，PDF29另render并目视核norm。新增原件实际18页，复用3页；不把45archivepages冒称全文阅读。正常TLS、无外部源码/HTML、无certificate bypass。来源URL/SHA/actualpages另NEW候选收据，等待root交叉审阅后再finalize。

所有构造只在真实辅助素数的F里用已证units，不重选原S、不改变其globalrank，不继承免费arch normalization，也不改上轮same-S安全费用40.314517426059346。本稿纯纸证新增数学执行0，不扩大辅助prime unit表，没有外部Lean。

## 11. 当前新增命题和未证条件

已证：完整cross是第二Racah族且全部profiles单位；原actual C全辅助p满行秩；明确known-unit右逆和完整2r kernel basis及确定det尺度；同一M5的canonical mixed-boundary determinant/corank恒等式；在明确实际H22条件下r阶anti-cancellation gate；两Racah全connection和真实cross/border公式；自然contiguous族全尺度support/rank collapse；C29质量Gram恒等式与实际half-fold完整对齐后的C30真实质量map单射定理。

仍缺：actual H22非退化或C20一般混合核消失、实际固定A0/A1防相消、无穷辅助p目标unit或actualhigherSmith替代、足够strictmargin、新ζ/L/Catalan无理性或LI定理。完整正交与pure-component injectivity不升级这些条件。
