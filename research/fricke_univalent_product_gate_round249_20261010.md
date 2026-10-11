# 第249轮：真实共轭分支与两实处单叶容量的乘积界

2026-10-10，Root。实际读A248完整六节的冻结商源，重新推导下述有限forcing及局部几何。本文证明：假设g+=Y/2+√2π²/28属于K=Q(√2)，其实际三行源在两实处的任何univalent共同合法图均满足c+c−≤16。结合当前7b d_N²安全类型及数域CDT必要条件，关闭该**两处均univalent的基本入口**。不排除multivalent图、额外finite-place收益、更优整模型或其它源；没有新的数值无理性定理。

## 1. 固定完整源及有限奇点

置s=√2、Q±=1−(7∓4s)t+t²、E=Q+Q−，δ=t∂t，A±=A(τ)±sA(2τ)，I±=R±(2s/7)D。A248已付真正的Fricke商t=(η₁η₁₄/(η₂η₇))⁴，Q(X₀(14))=Q(t,y)、y²=E；A±²/f₁₄=(3±2s)Q±/t。

令B±,g=A±(I±−g)。整个Γ₀(14)与W₁₄的返回都保持二阶齐次span(A±,τA±)，且任何B的返回分支之差属于这个span。Γ返回由Bol affine polynomial直接给出；W返回由已付g± cocycle给出，即使g≠g±，差也只是常数乘A±及τA±。对word逐次组合仍如此，不要求各周期系数都零。

δ-form的齐次二阶方程为L±=δ²+p₁,±δ+p₀,±，p₁,±=−δlogQ±+(1/2)δlogE。普通导数形式的一次系数为

\[
p_\pm(t)=\frac1t+\frac12\left(\frac{Q_\mp'}{Q_\mp}-\frac{Q_\pm'}{Q_\pm}\right).
\tag{1}
\]

其有限奇点只有0及E四根。证明不借未经消去的u/P因子：H中A±仅在相应两个branchpoints有simple zero；δ-Wronskian为(3±2s)Q±/(2πiy)。在其它非零有限点，两实际solutions全纯、Wronskian非零，monic方程系数全纯。t=0及∞的两cusp chart给regular singular、齐次exponents(0,0)。相应Q±根的两解可取A±和(τ−τe)A±，其orders为1、2于local uniformizer w，故t-exponents(1/2,1)；其它Q根处为(0,1/2)。无额外有限奇点。

## 2. 完整forcing的极简有理证书

由A248全函数乘积微分身份，L±B±,g=A±h±/G₀²，其中h±=Θ²I±、G₀=Θlogt。该比值在Γ与W下invariant。

在相应Q±零点，A±有simple zero，h±的automorphy multiplier是A±的立方；固定点的multiplier为−1，故h±也有至少一阶零。G₀有simple zero，所以forcing在此全纯。在另两个Q根A±及h±全纯，G₀²有二阶零，故forcing至多t-simple pole。0处native为O(t)，W-invariance支付另一cusp；∞处A±、h±、G₀的cusp权分别给至多log、log³、log²，比值有界。因此Q∓·forcing是degree≤2 polynomial且constant0。这先支付完整degree bound。

native头可在有限乘积/已付Eisenstein系数中直接纸算：hR=q−3q²+O(q³)，hD=q+4q²+O(q³)，A+=(1+s)+2q+O(q²)，G₀=1−4q+O(q²)，q=t+4t²+O(t³)。于是

\[
\mathcal R_+(t)=\frac{11+9s}{7}t+\frac{141+99s}{7}t^2+O(t^3).
\]

两系数唯一确定已经限定的二维空间，得到整个函数身份

\[
\boxed{\mathcal R_\pm(t)=
\frac{t[11\pm9s-8(1\pm s)t]}{7Q_\mp(t)}.}
\tag{2}
\]

这不是从有限头猜全方程，也不要求运行CAS。特别R+(∞)=−8(1+s)/7≠0。齐次∞的exponents(0,0)给δ-form p₁,p₀=O(1/t)。Regular-singular variation/Frobenius因而使每一particular solution在∞的最高log²层为

\[
\boxed{B_{+,g}(t)=-\frac{4(1+s)}7(\log t)^2+O(\log t).}
\tag{3}
\]

此式在sector内，系数另可由原cusp1/2渐近核对。返回分支差是齐次，至多log，所以每一到达∞的叶保留同一个非零log²系数。绕∞一周改变log为log±2πi，产生非零一级log项，monodromy不能平凡。负号源亦如此，但下文正处cap已经足够。

## 3. 原生小根与实际共轭的不可补平方根

令

\[
r=\frac{7+4s-\sqrt{77+56s}}2\in(0,1).
\]

Q−的两根是r、1/r；Q+的两根共轭且模长1，因为其discriminant77−56s<0、constant1。四根的模长均≤1/r。

τ*=i/√14是W固定点。t(τ*)是正数，且product表达式在0<q<1时每个(1+q^{7j})/(1+q^j)<1，故0<t(τ*)<q*<1。W在此反转local uniformizer，t-map ramification degree2，所以E(t*)=0。因此t*=r。

更需要确认直段[0,r]是原生叶。若在τ=iy、y>1/√14处t有critical point，则W固定该Γ₀(14)类，存在γ=(a b;c d)使γW(iy)=iy。令v=1/(14y)，Γ₀(14)的d为非零整数，故Imγ(iv)=v/(c²v²+d²)≤v<y，矛盾。因此t(q)在0<q<q*的导数无零，native leading为q，使它沿这条正q径严格递增到r。该论证不把另一到达叶替代原生径。

取ζ=(τ−τ*)/(τ−barτ*)，W作用ζ↦−ζ。A−在τ*有simple zero，由其实际weight1变换有A−/(1−ζ)为odd holomorphic函数、其ζ一阶系数非零。已付完整Fricke式使B−,g−=A−(I−−g−)为even holomorphic函数。

现假设g=g+∈K；负处实际系数共轭源是

\[
\bar B=A_-(I_--\bar g)=B_{-,g_-}+(g_--\bar g)A_-.
\]

若bar g=g−，则π²=(14/s)(g−bar g)代数，矛盾。因此其odd part精确为

\[
(g_--\bar g)\frac{A_-}{1-\zeta}\ne0.
\tag{4}
\]

又t−r=nonzero·ζ²+O(ζ⁴)，故bar B的**原生到达叶**含非零(t−r)^{1/2}项，不是t-meromorphic。这里没有对未知Y施加Galois automorphism，也未断言每一个其它返回叶都在r不补。

## 4. 两个单叶图的强制圆盘及乘积cap

设φ±:D→C、φ±(0)=0在各实处为univalent，完整源共同拉回single-valued meromorphic；c±=|φ±′(0)|。Koebe1/4给D(0,c±/4)⊂φ±(D)。因φ±有holomorphic inverse，拉回合法性使原生B对应叶在整个image内单值亚纯。

若c−>4r，则image包含直段[0,r]及r邻域，强制§3的原生叶在r meromorphic，与(4)矛盾。故c−≤4r。这不是由任意坏叶推出遗漏点，而是由强制内圆盘推出特定叶准入。

若c+>4/r，则image包含以0为中心、radius>1/r的圆盘，里面含全部有限奇点0及E四根。选1/r<ρ<c+/4，|t|=ρ上的B是image中单值亚纯函数，故此loop的返回平凡。方程没有其它有限奇点，loop在其ordinary locus同伦于∞外围loop；无论用哪一条ordinary pathtransport到∞，(3)使该返回非平凡，矛盾。允许image内meromorphic poles不影响单值loop结论。

因此

\[
\boxed{c_-\le4r,\quad c_+\le4/r,\quad c_+c_-\le16,}
\qquad
\boxed{\bar\lambda=\frac12\log(c_+c_-)\le\log4.}
\tag{5}
\]

只采用Koebe对univalent图的结论；未对multivalent图使用内圆盘定理，也未让原genus1 coordinate cap跨坐标使用。

## 5. 完整holomorphic清pole及安全类型

使用同一完整frame(1,7bB_g,7bEδB_g)，其中正整数b固定且bg∈O_K。乘E不改K(t)实际rank3，也不增加全prefix7b d_N²费用：E∈Z[t]，nativeconstant1，δ保持prefix。字面LCM array为3×2，两列均(0,1,1)，行和(0,2,2)，τ=2−2/9=16/9。

finite E点的每一实际B分支在modular local uniformizer w中holomorphic，t−e=w²·unit，故δB至多w⁻¹，EδB有界。0的返回分支为native analytic加A±(ατ+β)，即analytic+analytic·logt；finite-order pullback若meromorphic必须删除log，随后有界。其它finite点普通且全纯，φ不取∞。因此完整拉回若single-valued meromorphic，三行实际上全部holomorphic，符合数域版本的字面convergence条件。没有为了清pole偷偷减行或遗漏另一个embedding。

## 6. 精确预算范围与剩余关

数域CDT的archimedean normalization是两处平均J、平均λ，rank仍为K-rank3；fixed7b是常数费用。当前类型的严格基本目标为bar J<3(barλ−16/9)。同图整数常数子源rank1在正margin情形给bar J≥barλ，故strict必要barλ>8/3。而(5)给barλ≤log4<16/9<8/3，无法达到。更原始的literalRemark8.2.42还要求平均λ>σ_m=2，也不满足。

此处引用的是作者current220页版本Remark8.2.42的数域arch平均条件、任意矩阵类型公式及其必要预算，不把Q版Theorem2.7.1改称数域定理。B249亲读所用完整页并另写精确scope；本文的analytic(1)–(5)及holomorphic清pole独立自含。结论只关闭当前完整安全模型下**两处均univalent的arch-only basic入口**。增加实际finite-place charts可能改变费用/收益；multivalent一般图没有Koebe内圆盘，尚须真正完整的返回/共同图与预算证书。

本轮有限forcing身份、原生径与平方根、∞全叶log²、两个全univalent量词的乘积cap均为新纸证；数学程序/CAS/扫描0，未重跑248producer，外Git mutation0。作者最终全文自读及独立审查分别登记。数值目标g+∉K仍未证明，不领取ζ/L的新无理性或线性无关性结果。
