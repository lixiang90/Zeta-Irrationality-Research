# 第250轮 全椭圆返回的周期奇偶性与混合图障碍

2026-10-10，Root，纸证。固定248的实际Fricke商和249的完整三行模型。在假设g=g_+∈K=Q(√2)下，本文证明实际共轭源在四个有限分支点的每个运输到达叶都有不可去的sqrt；任何合法负处图必须提升到同一椭圆曲线。进一步证明当前arch-only安全判据在正处单叶、负处任意多叶的全部入口都失败。两处均多叶、有限处收益及更优整型尚未排除，没有新数值无理性定理。

## 1 全部有限返回可直接参数化

记s=√2、χ=χ−7、Y=L(2,χ)、A_±=A(τ)±sA(2τ)、I_±=R±(2s/7)D，g_±=Y/2±sπ²/28，B_±,c=A_±(I_±−c)。实际商是Γ*=Γ₀(14)+W₁₄，t=(η₁η₁₄/(η₂η₇))⁴，y²=E(t)=t⁴−14t³+19t²−14t+1。

Γ₀(14)没有椭圆元素：trace0会在mod7迫−1为平方；trace±1与mod2的a,d均奇矛盾。Γ*的其它coset元素γW₁₄，γ=[[a,b],[14c₀,d]]，其det为14、trace=14(b−c₀)。有限椭圆元素必须|trace|<2√14，因此trace=0，且只有order2。乘−1选d>0后，它恰为
\[
r_{a,b,d}=\begin{pmatrix}14b&-a\\14d&-14b\end{pmatrix},
\qquad ad-14b^2=1,
\qquad \tau_r=b/d+i/(\sqrt{14}d).
\tag{P1}
\]
d必奇，(d,7)=1，(b,d)=1。这是全部可能的有限stabilizer，不是固定四矩阵的样本推广。

t在X₀(14)的degree2商已付，其全部有限ramification值就是E的四根。除去cusps和这些固定点后，t:H→P¹是Γ*的正则覆盖。实际A_±、I_±、B_±,c在H单值全纯，故任意ordinary path的解析延拓均可用逆t路径提升并评价这些实际函数。到一个有限分支点的任何运输叶都落在H中某个固定点，局部返回为其order2 stabilizer；共轭仍属于(P1)。因此检验全部(P1)就覆盖全部有限到达叶，无需先证明249四个代表生成整个返回群。

## 2 通用周期与分母奇偶性

置j_+=−i√14χ(d)(dτ−b)、j_−=−j_+。已经支付的weight1与weight3模性分别给A_±(rτ)=j_±A_±(τ)、h_±(rτ)=j_±³h_±(τ)，其中h_±=Θ²I_±。Bol两次链式微分使P_r=j_±I_±(rτ)−I_±(τ)为affine；involution再使它唯一为g_r,±(j_±−1)。因而全H上
\[
I_\pm(r\tau)-g_{r,\pm}=j_\pm^{-1}(I_\pm(\tau)-g_{r,\pm}).
\tag{P2}
\]
取τ=b/d+i/(14d²ε)，rτ=b/d+iε，τ→i∞，I_±(τ)→0，|j_±|→∞，得到真正的radial Abel常数
\[
g_{r,\pm}=\lim_{\epsilon\downarrow0}
I_\pm(e^{2\pi ib/d-2\pi\epsilon}).
\tag{P3}
\]
因d奇，R的logistic分母的有限phase类没有−1；因(d,7)=1，D的T分母没有非平凡七次单位根。除z=1的removable点外，有限径向phase集合上的核一致有界。故绝对收敛的m⁻²支配严格支付(P3)及以下求和，不使用未付的non-tangential有限部分。

R=Σχ(m)q^m/[m²(1+q^m)]。在奇数阶单位根上，每项logistic核实部为1/2，所以
\[
\operatorname{Re}R(e^{2\pi ib/d})=Y/2.
\tag{P4}
\]
对D=Σ_{k奇}T(q^k)/k²，T(z)=(z+2z²+z³+2z⁴+z⁵)/S₇(z)，S₇=1+z+⋯+z⁶。在Q[z]/(z^d−1)中乘S₇的矩阵为整矩阵。其det为
\[
\prod_{\omega^d=1}S_7(\omega)=
7\prod_{\omega\ne1}\frac{1-\omega^7}{1-\omega}=7,
\tag{P5}
\]
因为ω↦ω⁷置换全部非单位d次根。其逆矩阵由adjugate除7给出，因此唯一T多项式Σ_{a=0}^{d−1}c_a z^a满足c_a∈(1/7)Z；T(1)=1给Σc_a=1。T(z⁻¹)=T(z)给c_a=c_{d−a}，所以T在单位圆上为实数。

完整Bernoulli Fourier公式Σcos(2πkx)/k²=π²B₂(x)给
\[
\theta_{b,d}:=D(e^{2\pi ib/d})/\pi^2
=\sum_a c_a\{B_2(\{ba/d\})-\tfrac14B_2(\{2ba/d\})\}.
\]
在0≤x≤1时，括号精确为1/8−min(x,1−x)/2。令n_a为ba mod d的0至d−1代表，得到
\[
\boxed{\theta_{b,d}=\frac18-\frac{M_{b,d}}{2d},
\quad M_{b,d}=\sum_a c_a\min(n_a,d-n_a)\in\tfrac17\mathbb Z.}
\tag{P6}
\]
若θ=−1/8则M=d/2，迫7d偶数，违d奇。因此对全部(P1)
\[
\boxed{\theta_{b,d}\ne-1/8.}
\tag{P7}
\]
这是全参数分母证书，不是有界d计算。证明负处结论只需要(P4)及(P7)，无需把R的全部虚部或所有Γ周期预先证明成π²乘代数数。

## 3 实际共轭在所有有限叶都不补支

假设g=g_+∈K，实际系数共轭是B_−,bar g；不对未知Y施加任意Galois作用。若某有限叶普通补点，(P2)的全局返回要求bar g=g_r,−。因bar g为实数，先由(P4)迫R的虚部为0，再给
\[
\bar g=Y/2-(2s/7)\pi^2\theta_{b,d},
\qquad
g-\bar g=\frac{s(1+8\theta_{b,d})}{28}\pi^2.
\tag{P8}
\]
右侧系数是非零代数数，而左侧代数，故π²代数，矛盾。这个推导也覆盖g=bar g的情形。

普通补点的充要条件不能只用固定点值。取ζ=(τ−τ_r)/(τ−barτ_r)，rζ=−ζ，j_−=μ(1+ζ)/(1−ζ)，μ=−χ(d)。准确weight1 gauge Ã=A_−/(1−ζ)满足Ã(−ζ)=μÃ(ζ)。由(P2)，B_−,bar g的整个odd part是
\[
\begin{cases}
-(g_{r,-}-\bar g)\zeta\widetilde A,&\mu=+1,\\
 (g_{r,-}-\bar g)\widetilde A,&\mu=-1.
\end{cases}
\tag{P9}
\]
μ=+1时Ã(0)≠0，μ=−1时Ã有simple zero，均与248的完整divisor一致。由(P8)排除的等式，此odd part具有非零一次ζ项；t−t_r是ζ²乘analytic unit。所以四有限分支点的每个运输叶均含非零sqrt通道，不能普通补点。

## 4 任意负处图的椭圆提升与改进Bloch界

设负处合法holomorphic图φ_−:D→C、φ_−(0)=0，使实际完整三行源单值亚纯。若φ_−(z₀)=e是E根、其零阶为m，(P9)拉回的第一半整数项阶为m/2；亚纯性迫m偶。因此E(φ_−)全部零阶偶，在单连通圆盘有全纯平方根v，native v(0)=1。于是
\[
\psi=(\phi_-,v):D\longrightarrow\{y^2=E(t)\}
\tag{P10}
\]
提升到与248完全相同的紧椭圆曲线，且遗漏两个t=∞点。其准确微分ω=dt/y=f₁₄dq/q，native leading1，Abel提升F:D→C满足F′(0)=φ_−′(0)，并遗漏至少一个完整周期格coset。

248已独立付两个实际closed cycles及period格的covering radiusR₀<5/3：ω=−dX/Y、Y²=(X−1)(4X²+5X+23)，periods a、a/2+ib，其中a²<80/13、b²<200/47，因此R₀²<1590/611<25/9。这里使用相同曲线和同一微分的明确归一化，没有从旧x坐标直接搬导数cap。

改进的自含Bloch引理：若F:D→C遗漏covering radiusR₀的格coset，则|F′(0)|≤8R₀。取0<ρ<1，选ζ₀使M=(ρ−|ζ₀|)|F′(ζ₀)|最大，M≥ρ|F′(0)|。置h(w)=F(ζ₀+dw)−F(ζ₀)，d=ρ−|ζ₀|，α=h′(0)，|α|=M；最大性给|h′(w)|≤M/(1−|w|)。在|w|<1/2上，对h′(v/2)/(2α)用Schwarz–Pick，其0值为1/2，得到
\[
|h'(w)-\alpha|\le\frac{3M|w|}{1-|w|}.
\]
积分后，在|w|=1/4上Rouché使h的像包含半径M[1−3log(4/3)]的圆盘。因log(4/3)<∫₀^{1/3}(1−x+x²)dx=47/162<7/24，此半径>M/8。遗漏coset迫M/8≤R₀；令ρ↑1得引理，constant情形平凡。因此
\[
\boxed{c_-:=|\phi_-'(0)|\le8R_0<40/3.}
\tag{P11}
\]
这里允许φ_−与F任意多叶。

## 5 新整数背景与混合入口的严格比较

新增合法整数背景并非恢复A_−。由t(q)∈qZ[[q]]首项1、f₁₄(q)/q∈1+qZ[[q]]，有y(q)=Θt/f₁₄∈Z[[q]]；整数形式逆q(t)给
\[
y(t)\in\mathbb Z[[t]],\qquad \operatorname{rank}_{\mathbb Q(t)}(1,y)=2.
\tag{P12}
\]
秩来自E四根简单、非平方。负处图(P10)使native y的拉回全纯，故CDT基本整数型τ=0给J_−≥2λ_−当λ_−>0；λ_−≤0时Jensen的J_−≥λ_−也蕴含同一较弱不等式。正处J_+≥λ_+，其中λ_±=log c_±。

249当前完整K模型是rank3、两列(0,1,1)、τ=16/9。任何arch-only严格秩矛盾要求
\[
\frac{J_++J_-}{2}<3\left(\frac{\lambda_++\lambda_-}{2}-\frac{16}{9}\right).
\]
结合新背景必要
\[
\boxed{\lambda_++\lambda_-/2>16/3,
\quad c_+\sqrt{c_-}>e^{16/3}.}
\tag{P13}
\]
若正处仍单叶，249全部∞返回叶log²证书与Koebe给c_+≤4/r，其中r=(7+4s−√(77+56s))/2。因r⁻¹<7+4s、s<23/16，有c_+<51。由(P11)，sqrt(c_−)<11/3。因此c_+sqrt(c_−)<187。另一方面e⁵>Σ_{n=0}⁹5ⁿ/n!>141、e^{1/3}>4/3，故e^{16/3}>188。与(P13)矛盾。

于是当前安全完整模型下，**正处单叶、负处任意多叶的所有arch-only基本入口均被关闭**，扩大了249仅两处都单叶的排除范围。完全双多叶图尚无正处cap或实际严格能量比较；(P13)必要条件不是新数值目标的证明。正处普通补支仍涉及θ=+1/8和R虚部0，(P7)没有支付这个相反符号的分类。

## 6 阅读与结果边界

本轮Root实际FULL读248商源12413 B、248椭圆cap8699 B、249返回稿11197 B、249预算10490 B及Root249全部8502 B。另实际FULL读CDT固定v2物理16–20完整TXT18249 B，采用Theorem2.5.1的整数背景秩界及其meromorphic条件，及249DLMF完整所用公式选段1000 B。没有新GET或全文上游PDF认证；数域full模型归一化复用249已付接口。

(P1)–(P13)是同对象纸证，Root数学程序/CAS/interval/word/prime/map/parameter/Lean运行0。作者保存后全文复读及B的独立审查分别登记。全negative transported不填、实际椭圆lift、改进Bloch与新背景确实改变strict比较；新数值定理仍未得，goal active。
