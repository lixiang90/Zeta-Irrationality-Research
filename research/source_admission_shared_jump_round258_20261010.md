# 第258轮：数值关系的完整跳变接口与经典Hadamard闭包边界

2026-10-10。257归档117项已在本轮重新逐项核验，new_main/new_policy身份也匹配；上一goal turn为progress。本轮执行一次有界跨架构来源准入，不重开已经结算的χ−8 monomial prototype。总目标仍是新的数值ζ/L无理性或线性无关性定理，尚未达到。

本稿固定比较对象：真实endpoint族 `1,ζ(2),L(2,χ−3),β(2)` 的四圆分通道经典Li2 lift；校准对象是CDT固定v2的Zagier H_A/H_B/H_C。拟补域为这四圆分通道分支点的邻域。下面证明完整跳变接口的必要条件，并把经典通道在有限Hadamard组合下的边界闭合。这些是来源选择的证据，不是该四项数值线性无关的证明。

## 1. 自动关系提升必须共享完整坏芽

令b为待填入点，在一个固定穿孔sector上取实际函数F_0,…,F_m。记 `M_b` 为在b亚纯的实际germs，令 `Q_b` 为所用germ向量空间模M_b；这是复向量空间，不把一个holomorphic jump误称非meromorphic函数。设Θ=(1,Θ_1,…,Θ_m)为实际数值period vector，定义

\[
J_b(c)=\left[\sum_{j=0}^m c_jF_j\right]\in Q_b,
\qquad R_\Theta(c)=c_0+\sum_{j=1}^m c_j\Theta_j.
\tag{S1}
\]

以下两条件等价：

1. 对每个复系数c，`R_Θ(c)=0`均使完整Σc_jF_j在b亚纯。
2. 存在一个完整坏芽类B_b，使 `[F_j]=Θ_jB_b`，其中Θ_0=1。

证明：若1成立，e_j−Θ_je_0属于ker R_Θ，所以 `[F_j]=Θ_j[F_0]`，取B_b=[F_0]。反向由线性性直接成立。对一组待补点分别应用，所有点须使用同一个数值Θ，但允许各自不同的B_b。

这是**对任意潜在关系的自动提升**的充要条件。它不是某一个实际有理关系能成立的必要条件，更不证明Θ的数值独立。若只寻找一个具体c，应直接证明所有所需点上J_b(c)=0；不能以本等价式的较强条件否决所有特定c。

特别地，如果目标常数1的carrier选成字面常函数F_0=1，则B_b=0，自动提升要求全部F_j本来就在b亚纯。成功的period-kernel构造因此通常需要一个**非平凡的unit-period carrier**：其局部比较系数为1，但函数有与其它period carrier共享的坏芽。CDT的H_A正是这种角色；辅助pure常函数1是另一个输入，不能混作H_A。

即使最高log系数已经按Θ排成一行，也须证明全部坏芽而非只一个系数。例如F_0=(log u)^2、F_1=Θ_1(log u)^2+log u。系数c=(−Θ_1,1)满足数值关系，却留下log u。有限jets、一个局部leading项或抽象period投影均不能代替(S1)的完整germ商。

## 2. 固定圆分endpoint lift的实际数值识别

令ω=e^(2πi/3)，取在z=0的principal Taylor branches。固定

\[
H_R(z)=a-\frac{3b}{2}\{\operatorname{Li}_2(\omega z)+\operatorname{Li}_2(\omega^2z)\}
+\frac c{i\sqrt3}\{\operatorname{Li}_2(\omega z)-\operatorname{Li}_2(\omega^2z)\}
+\frac d{2i}\{\operatorname{Li}_2(iz)-\operatorname{Li}_2(-iz)\},
\tag{S2}
\]

a,b,c,d为有理数。由绝对收敛的n^(−2)和及character Fourier投影，

\[
H_R(1)=a+b\zeta(2)+cL(2,\chi_{-3})+d\beta(2).
\tag{S3}
\]

例如ω^n+ω^(2n)为3|n时2、其它时−1，故其n^(−2)和为−2ζ(2)/3；`(ω^n−ω^(2n))/(i√3)=χ−3(n)`，`(i^n−(−i)^n)/(2i)=χ−4(n)`。因此(S2)原本就是Q[[z]]，不需要假设(S3)=0才能有理化。固定整数关系的分母只需一个固定整体倍再乘d_N²清完整Taylor前缀。

四个不同branchpoints为ω²、ω、−i、i。绕α^(−1)的native单圈，

\[
\Delta_{\alpha^{-1}}\operatorname{Li}_k(\alpha z)
=-\frac{2\pi i}{(k-1)!}\{\log(\alpha z)\}^{k-1},\quad k\ge1.
\tag{S4}
\]

log在αz=1附近取值0的全纯branch。跳变本身在该点全纯，但非零跳变使原函数不能亚纯。其它α通道在那里单值。于是(S2)在四点全消跳当且仅当四个Li2 coefficients全为0，即b=c=d=0。若同时(S3)=0，才进一步有a=0。这里证明的是**消跳条件**，没有由假设数值关系本身推出b=c=d=0。

一个明确警示：令S_ω=Li2(ωz)+Li2(ω²z)，S_i=Li2(iz)+Li2(−iz)。由偶数项，S_i(1)=−ζ(2)/4，故 `3S_ω−8S_i` 在1为0，却仍在四处有非零跳变。endpoint函数值为0并不产生共同域增益。

## 3. 同通道全部权重和亚纯系数也不能隐藏跳变

固定有限非零α集合Γ和有限权重s。在C(z)上线性组合

\[
F(z)=r_0(z)+\sum_{\alpha\in\Gamma}\sum_{k=1}^s
r_{\alpha,k}(z)\operatorname{Li}_k(\alpha z)
\tag{S5}
\]

中，绕b=α^(−1)而不绕0或其它support，ΔF为(S4)给出的log-polynomial，其coefficients为r_α,k(z)。`log(αz)`在C(z)上超越：若存在有理系数多项式恒等，沿绕0的所有整数单圈继续，并选系数无极点且最高系数非零的basepoint，便得到一个非零复多项式有无穷多个相差2πi的根，矛盾。因此ΔF恒为0当且仅当该α的全部r_α,k恒为0。全部Γ点消跳则F仅剩r_0。

这证明了指定classic family的完整函数线性独立与support障碍，适用范围为同一z变量、固定rotation及有理单值coefficients；没有把它推广到一般pullback、Hadamard几何来源、任意Eichler积分或所有CDT构造。

在一个固定branchpoint处施加有限ramification `z=φ(u)`，φ(u_0)=b且ramification index e≥1，则u单圈对应z的e圈。因为(S4)在b局部单值，`(T^e−I)Li_k=eΔLi_k`，不因有限cover而消失。对(S5)，若原跳变非零，其pullback也非零（非常数局部映射的open mapping）；需把这个前像留在拟补入域才能应用。此命题不限制选择一个避开该前像的合法解析图，更不提供CDT能源lower。

## 4. 经典Li通道的有限Hadamard闭包不能保持原period就制造改图

定义一个明确有界的来源类别

\[
\mathscr H_\Gamma=\mathbb C\oplus
\operatorname{span}_{\mathbb C}\{\operatorname{Li}_k(\alpha z):
k\ge1,\ \alpha\in\langle\Gamma\rangle\},
\tag{S6}
\]

每个元素只用有限多个项；Γ为上文四个roots of unity时生成有限群μ12。由Taylor coefficients直接有

\[
\operatorname{Li}_k(\alpha z)\star\operatorname{Li}_l(\beta z)
=\operatorname{Li}_{k+l}(\alpha\beta z).
\tag{S7}
\]

常函数只和另一个常函数产生非零常数Hadamard项。因此该类在有限Hadamard乘积、常系数线性组合和群内rotation `z→γz,γ∈〈Γ〉` 下闭合。它不声称在任意rotation、有理函数乘法或任意pullback下Hadamard闭合。

(S4)–(S5)给完整分类：合并相同α、k后的非零polylog项必在相应support保留跳变。若所有剩余support消跳，元素只有常数。Hadamard可以让support碰撞，但在这个类别中碰撞后的完整消跳就是消掉对应Li coordinate；不是一个未知endpoint period关系新近提供的analytic收益。

此外(S7)改变weight。以Dirichletcharacter generating germs `f_{k,χ}(z)=Σχ(n)z^n/n^k` 计，

\[
f_{k,\chi}\star f_{l,\psi}=f_{k+l,\chi\psi},
\quad (f_{k,\chi}\star f_{l,\psi})(1)=L(k+l,\chi\psi),
\tag{S8}
\]

而不是L(k,χ)L(l,ψ)。若用inverse rotations把几种support逐一合到1，结果也是同一Li_(k+l)(z)的常系数倍；不能把原数值关系无证搬到新weight。该identity是精确所有coefficients的纸面证明，没有数值采样或参数扫描。

Pérez-Marco的[局部Hadamard单值化论文](https://arxiv.org/abs/2011.10497v1) Theorem1.1及证明解释一般integrable singularities的跳变卷积。Root实际完整读其物理1–6页；经典Li各阶都是integrable，(S4)亦在该原文物理6页给出。不过本稿(S7)–(S8)自含地由coefficients证明，不依赖未经阅读的其它sections。一般Hadamard的分支卷积可以创造这里没有的共同period芽，所以本边界不排除CDT的Zagier或Legendre构造。

## 5. 来源结算及下一需要的实际输入

本轮拒绝(S2)及(S6)有限闭包作为该四项数值关系的**自动消支并扩图来源**。原因是完整消跳失败，或Hadamard后原period目标已改变；不是该四项数字不独立，也不是所有μ12来源不可能。C(z)上的函数独立不能推出endpoint数值独立。原数值goal保持active。

新的可复用接口是(S1)：在进入任何approximation/holonomy成本优化之前，必须提供非平凡unit-period carrier、实际period comparison vector和同一完整坏芽。CDT的具体校准和外仓库KZ边界由本轮另两份primary审读给出；本稿保存时尚未读取它们的最终稿，不预记已审。

下一次实现若要进入，应固定一个原目标相关的actual family并逐个证明 `[F_j]=Θ_jB_b` 或为明确的某个潜在关系证明J_b(c)=0，然后证明完整最小函数族在同一新域亚纯、支付全prefix算术费用和严格holonomy余量。仅有endpoint ζ/L的Fourier公式、所有函数的holonomicity或上述Hadamard恒等式均不准入。

正式全局clock不在本轮重置：last256，258完成后计数2，next260、latest264；连续两轮未推进关键准入/净可行性则提前。本稿是来源结构进展，没有新数值定理或Lean认证。

## 6. 执行与来源范围

Root本轮实际解析257 manifest并核117项及main/policy；读period_holonomy_cdt_mechanism_20261005全文（项目记录，不继承其原作者primary审计）；读255holonomy架构稿全文。初次256全局稿与web组合输出被总预算截断，不记为本轮FULL原文审计。Root新下载2011.10497v1 18页PDF，只实际完整读物理1–6页的保存提取文件；相关元数据页面、作者站CDT PDF首页与目录、固定v2 metadata只按所显示范围采用，不声称全篇已审。

本轮Root数学程序、finite-n/CAS/interval/prime/参数/map/word扫描、Lean、外Git写及旧producer均0。文档下载、PDF提取、JSON/hash校验不是数学计算。新primary PDF1，下载/读取收据及后续实际scope保存在literature/source_admission_round258_20261010；团队其它下载与读取以各自scope单独记。全部新推导由本稿正文给纸面证明，不以绿色归档核验替代数学正确性。
