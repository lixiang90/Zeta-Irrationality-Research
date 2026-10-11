# 第233轮：截区同一W的完整增长素数层与条件清整费用

2026-10-08，Packet/B。只做本轮有界gate。以232冻结稿12275 B、SHA256 8ea824753c808f6a8477cdae536cd6d22dcad1bfc98819bbc0de51d075447227为实际完整源，保留全部finite heads。新增自含纸证：增长素数的残差经单位卷积变成普通Cauchy矩阵，故下块极点秩全尺度精确可算；完整栈及实际关系费用仍有明确剩余条件。数学程序0，没有扫描或旧producer执行；没有新的数值无理性定理。

## 1. 固定同一对象，区分全有限处与新窗口

沿232记d≥1，m=d+1，L=3d+1，0≤r<2m、0≤s<m，

\[
A_{s,r}=c_{r+s},\quad B_{s,r}=\alpha_{r+s},\qquad
R_{r,s}=\rho_{r+s}
-\sum_{v=0}^{d-s-1}\frac{r_{r+s+v}}{2v+1},
\]

\[
W_d(X)=\det\begin{pmatrix}B\\(10/3)XA+\sqrt3R^T\end{pmatrix}
\in K[X],\quad K=\mathbb Q(\sqrt3).
\tag{F1}
\]

这里c_l=4⁻ˡbinom(2l,l)，
r_l=Σ_{b=0}^l(−1)ᵇbinom(l,b)(3/4)ᵇ/(2b+1)，
α₀=ρ₀=0且
2lα_l=(2l−1)α_(l−1)+4⁻ˡ、
2lρ_l=(2l−1)ρ_(l−1)+r_(l−1)。
目标仍V=Cl₂(π/3)=(3√3/4)L(2,χ₋₃)，真实评价W_d(V)。

232完整Fourier证明的
Q_d=2·4^L D²、D=lcm(1,…,2L+1)
给全素数全幂安全模型(3Q_d)²ᵐW_d∈O_K[X]。这只是已付upper；不能与一个实处upper相加后冒称最优no-go。下文新精确结果限于

\[
L<p\le2L+1,\qquad
k=(p-1)/2,\quad h=k+1-d,\quad q=L-k=2m-h,\quad
\eta=(-3)^k\bmod p=\left(\frac{-3}{p}\right)\in\{1,-1\}.
\tag{F2}
\]

p≥5。新窗口以外，包括2、3和p≤L的primitive内容/精确费用，本文没有从安全模型变成最优结论。固定g∈Q的分母也保留；下列评价定理取p∤den(g)，有限例外另清。

## 2. 基本r残差与ρ的全部卷积项

c和α在该窗口p整：c只有2幂分母，而232的α Fourier式外层j≤L<p。对于r_l闭式，l≤L<p时唯一可能含p的分母2b+1是b=k。因此

\[
p\,r_l\equiv0\ (l<k),\qquad
p\,r_{k+t}\equiv\eta\,c_t\pmod p\quad(0\le t\le L-k).
\tag{F3}
\]

证明：残差为(−3/4)ᵏbinom(k+t,k)。4ᵏ=2ᵖ⁻¹≡1；
binom(k+t,t)≡(1/2)ₜ/t!=c_t，因全部t!为p单位。其余项p倍后为0。由Fermat定理η是非零平方特征，不需要未付的Fermat商或Wieferich假设。

所有ρ_l至L最多只有简单p极点。ρ_l在l≤k时p整；令U_b=pρ_(k+1+b) modp，U₋₁=0，则递推精确给

\[
(2b+1)U_b=2b\,U_{b-1}+\eta c_b,\qquad
U_b=\eta\sum_{t=0}^b\frac{c_t}{2(b-t)+1},\quad0\le b<q.
\tag{F4}
\]

这些分母为p单位。后式可直接验递推，亦可用形式级数C(z)=Σc_tzᵗ=(1−z)⁻¹ᐟ²及
E(z)=Σzᵗ/(2t+1)：U=ηCE满足
2z(1−z)U′+(1−2z)U=ηC。
只在b<q<p内取系数，未把含1/p的无限级数代入有限域。

## 3. 保留whole heads后的精确残差

若r<h，则r+s≤k且全部头的r+s+v<k，故pR_(r,s)≡0。
取r=h+u，0≤u<q。F4中ρ的下标偏移为b=u+s−d；
当b≥0其残差之和恰是
−ηΣ_{t=0}^b c_t/[2(t−u+d−s)−1]。
有限头在v=t+d−u−s−1处的残差，补上
t=max(0,b+1),…,u。两段精确合并为

\[
pR_{h+u,s}\equiv-\eta\sum_{t=0}^u
\frac{c_t}{\,2(d-s-u+t)-1\,}\pmod p .
\tag{F5}
\]

这包括s=d的空头和ρ的负偏移情形；没有只取递推主项。特别最高头下标为L−1；p=2L+1时q=0，全部R均p整，尽管r_L本身可以有p极点。

定义q×q下三角矩T_(u,v)=c_(u−v)（v≤u，其它0），以及q×m矩

\[
Z_{u,s}=\frac1{\,2(d-s-u)-1\,}.
\]

c₀=1，所以T为Fp单位矩，且

\[
pR\equiv\begin{pmatrix}0_{h\times m}\\-\eta TZ\end{pmatrix}.
\tag{F6}
\]

## 4. 普通Cauchy单位性全尺度成立，但它不是完整栈的单位性

Z的节点可取a_u=2(d−u)−1、b_s=2s，Z_(u,s)=1/(a_u−b_s)。
任意行/列节点差均为非零模p，因为q<p、m<p且这些下标差小于p。
每个分母的整数绝对值不超过max(2d−1,2q−1)<p，亦不为0。
任取相同数量的行列，其Cauchy行列式（由清分母后交错多项式/Vandermonde直接证明）为

\[
\det\left(\frac1{a_i-b_j}\right)
=\frac{(-1)^{t(t-1)/2}
\prod_{i<j}(a_j-a_i)\prod_{i<j}(b_j-b_i)}
{\prod_{i,j}(a_i-b_j)}\ne0\quad\text{于 }\mathbb F_p.
\tag{F7}
\]

故rank Z=min(q,m)，并且rank(pR)=min(q,m)。
这与旧q2的squared-Cauchy层不同：此处没有另欠permanent/Gaudin单位性；没有借用旧对象的任何Hankel或反射结论。

完整最高层是2m×2m矩

\[
\mathcal G_p=\begin{pmatrix}B\\(pR)^T\end{pmatrix}\bmod p .
\]

当q<m（p>4d+1），rank𝒢≤m+q<2m，最高m极点层必退化；不能将它误称真实费用已降到0。由F6只有q个列含简单极点，且只有m个底行含极点，故对p整X始终有
v_𝔭W_d(X)≥−min(m,q)。

当q≥m，分B=[B₀,B₁]为h与q列，同时对active列乘T⁻ᵀ，置B̂₁=B₁T⁻ᵀ。令K_Z为ker Zᵀ的任意Fp基（q×(q−m)矩），则线性代数精确给

\[
\operatorname{rank}\mathcal G_p
=m+\operatorname{rank}[B_0,\widehat B_1K_Z].
\tag{F8}
\]

右侧最后一矩是m×m；它正是B在完整底块核上的restriction。实数上的[A;B]全池可逆、下块Z满秩和该restriction满秩是三个不同命题；本稿只证明前两项已有各自证书，没有以它们冒付第三项。

## 5. 最高栈单位时的必要关系值费用：两个嵌入同时支付

令𝒫_d为窗口L<p≤4d+1内满足det𝒢_p≠0的实际素数集合。本文未证明该集合无界、密度正或包含整个窗口。对其中任意p及p整g，

\[
p^mW_d(X)\bmod\mathfrak p
=(\sqrt3)^m\det\mathcal G_p\ne0
\quad\text{作为常数多项式，}
\qquad v_{\mathfrak p}W_d(g)=-m .
\tag{F9}
\]

每个𝔭|p都成立：p>3不分歧，√3在各局部环为单位；𝒢的行列式已在Fp非零。其证明是在F1中将全部底行乘p；pXA模p为0，所以上述最深项不依赖g。它同时是形式多项式的真实强迫系数深度和所有p整评价的真实深度，无法靠“目标关系下相消”消掉这一层。

因此任意a_d∈K×若使a_dW_d(g)∈O_K，必须在这些𝔭处有v_𝔭(a_d)≥m。以正有限处清整费用而非一般scalar的裸Norm记账，得到必要局部费用

\[
\sum_{\mathfrak p}\max(0,v_{\mathfrak p}(a_d))\log N\mathfrak p
\ \ge\ 2m\sum_{\substack{p\in\mathcal P_d\\p\nmid\mathrm{den}(g)}}\log p .
\tag{F10}
\]

因Σ_{𝔭|p}f_𝔭=2，分裂/惰性两情形都包含。若限定a_d为整的scalar清因子，则log|Norm(a_d)|等于全部非负有限费用，也满足F10。一般a_d可有其它处负估值，不能直接把F10写成其裸Norm lower；那些负估值必须由W在其它处的真实正内容支付。

**仅条件示例：** 若整个窗口L<p≤4d+1都单位，固定g的有限坏素数最终不在该增长窗口，PNT给F10右侧=2d²+o(d²)。这不是已证窗口单位性，也不是index直接等于CDTτ。对一般实际𝒫_d只有F10的精确部分下界。p>4d+1和top栈不满时还需regular gA、ρ的p整部分及所有头的下一层；不能按m极点免费收费，也不能按亏秩直接领取relation-saving。

## 6. 边界无限子族的条件更少，但仍没有支付它

若p=4d+1为素数，h=q=m，T与Z均单位。此时block triangular给

\[
\det\mathcal G_p=(-\eta)^m
\det(\alpha_{r+s})_{0\le r,s\le d}\,\det Z .
\]

所以最高层单位、valuation −m和该真实α初Hankel在Fp非零完全等价；不再需要旧squared-Cauchy单位性的第二证书。d=(p−1)/4不包含“固定d产生无穷prime”的猜测。但该α Hankel非零并未由232全栈实秩证明推出；旧Hankel c_n(H₂ₙ−Hₙ)的反射/Fermat商也不能移植给α_n。

本轮的算术变化是真实且限定的：全有限头极点变为一阶Cauchy，故底块秩已付；若完整restriction单位，得到的是不可免费消掉的关系值分母负担，同时支付该尺度非零。它不是228的rank-one Gram content cap，也尚未给新的净费用改善。关于无界restriction、p≤L和固定2/3的primitive内容、另一嵌入实增长及同对象target-specific误差，仍须直接支付。

C233另独立指出一个也可直接核的实行消：232的B=γ(A−3I)给A+B/(2γ)=(3/2)A_high，其中I是低区矩，A_high=A−I。于是W_d(g)在恢复真实N后再给下块加λ(g−V)B/(2γ)，λ=10/3，即变为Nᵀ+(3λ/2)(g−V)A_high；这对所有g都只有高区支撑。含π的行操作不改变实det，但不是O_K整格变换。因此232某一特定行表示中的低区取消不能单独作严格收益证书。F5–F10仍对应原有理系数B和完整R，不用这种实shear替代算术源。

## 7. 本轮gate和读取边界

本稿以232实际FULL最终源为起点，重新核其完整r/α/ρ Fourier公式、finite heads及同一W定义。F2–F10是本轮新纸面有限域/局部证明，不借probe、不运行CAS，不声称扫描得到𝒫_d性质。普通Cauchy恒等式已在F7自证；没有新增外部primary定理或假装FULL文献审阅。

只保留一个下一步算术接口：[B₀,B̂₁kerZᵀ]的实际单位性/内容，而不继续多参数筛选。其若未付，不把QL安全费用正和当no-go；其若已付，必须将F9的真实最深费用和其它所有places一并与同对象实误差比较。233是否继续原目标主线由完整bounded gate决定；本文不单独宣布通过或永久失败。

保存后作者实际FULL复读，报告最终bytes/SHA。全部数学执行0；仅NEW233稿，旧232及更早稿/main/manifest未改。

