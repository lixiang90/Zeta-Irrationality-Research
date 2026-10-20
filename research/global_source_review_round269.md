# 第269轮正式复盘：增长极点的纯目标正配对

2026-10-20结算。完成[宏观任务](source_gate_charter_round269_20261013.md)。**没有新无理性定理，也没有完整数值净预算。** 本轮自证一项不同的全尺度构造：对X=ζ(2)+2G，得到实际严格正Gram矩阵R_m+XI_m，R_m∈Sym_m(Q)，目标系数秩恰m。只给下一轮同对象高度及完整净预算核查；不恢复旧扫描。

## 1. 全路线机会成本与来源决定

| 来源 | 已付或本轮所核 | 决定 |
| --- | --- | --- |
| ζ5基线、ζ7旧Gram、K5 | 已有完整成果/限定障碍，见[成果地图](../docs/RESEARCH_DIRECTIONS.md) | 不把基线或旧参数加高算新结果 |
| mixed scalar/AP及实际整jet | 262–264已关闭的具体模型 | 原停止范围保留 |
| M₀,₈完整pair | 266安全模型不足，canonical/实际率条件保留 | 不续期 |
| 非显式Siegel目标商 | [268](siegel_target_quotient_round268.md)实际坏族及完整标准消元上包络 | 不把存在好族未排除当准入 |
| Viola–Marcovecchio围道/group | 实际完整读取仍仅OWR两页报告 | 保留缺完整费用的接口，不拨数学实现轮 |
| Eskandari偶滤波 | 已存v1，265已审自然清整族 | 不再领取已除去的16^m；不重开 |
| Apéry/Calabi–Yau及椭圆L比值 | 实际数值通道、整数运输和全叶条件仍不匹配 | 不跨源借费或更换最终目标 |
| p-adic/adelic、直接Nikishin | 没有指定实值的同值桥或同源正配对 | 不移交局部小值/ambient perfectness |
| 固定分母纯X正Gram | 正性与投影成立，周期系数秩一 | 二次预算入口关闭，线性Padé费用未付 |
| 本轮增长极点构造 | 完整五周期图、显式共同纯空间、实际正性和增长目标秩 | 只给一轮高度/完整预算来源核查 |

[Viola报告](https://ems.press/content/serial-article-files/46958)印刷1100–1101页给正双积分及参数反转，未给可独证的完整群清整和鞍点率。本轮定向检索未取得其中所称后续完整稿，不声称它不存在。其报告指数0.6293、[Eskandari v1](https://arxiv.org/abs/2609.26354v1)指数0.62是逼近误差的保证，不是整数形式衰减率，也不是实际指数上界。后者0<|G−p/q|≤q^-0.62只给0<|qG−p|≤q^0.38；不能推出趋零。两者向量仍只有1,G；X∈Q后仍有ζ2栏。265的自然清整失败也不排除额外本原gcd。

GKS固定[2009.14762v3](https://arxiv.org/abs/2009.14762v3)所证Mukai例只到已知ζ2、ζ3及L(3,χ−3)等出口。GZ正式版的ζ7 κ表达以实验身份出现；即使领取原始显示式仍有π²ζ5、π⁴ζ3通道。另行采用本地九阶Gamma/Tate纯化时，得到的是ζ7/(2πi)^7，其有理性不由ζ7∈Q推出；这与原始κ显示式的归一化分开。KZ的具体conductor15比值超当前Dirichlet目标，且[原反项载体](cdt_odd_noncritical_elliptic_counterterm_carrier_20261007.md)仍须同坐标λ>21/10、J<5(λ−21/10)的全叶余量；不能凭Apéry limit或安全清整续期。

[2505.23088v1](https://arxiv.org/abs/2505.23088v1)实际使用1和一包p-adic奇ζ。实ζ7=q不提供ζ_p(7)=q，也不消其他p-adic通道，故未提供同一P_n(q)的产品公式桥。这不是否定全部adelic方法。

## 2. 拦截两个伪新入口

### 2.1 固定分母的实际纯X正源

直接展开正积分得
$$
X=\int_0^1\frac{(-\log t)(2+8t)}{1+t^2}\,dt
 =\int_0^1\frac{(-\log T)(2+1/(2\sqrt T))}{1+T}\,dT.
$$
记右侧测度为ν，则ν≥(1−T)dT且
$$
\nu_{k+1}+\nu_k=\frac2{(k+1)^2}+\frac2{(2k+1)^2},
\qquad \nu_0=X.
$$
因此ν_k=(-1)^kX+r_k，r_k∈Q。对含1、次数≤D的m维有理多项式空间，实际Gram矩阵M正定，b_i=p_i(−1)，完整目标铅笔为M+(Z−X)bbᵗ，记其行列式为Δ(Z)。其Z系数A=det(M)K>0，其中K=bᵗM⁻¹b。

沿[252](public_repository_global_review_round252_20261010.md)的已证Jacobi比较，ν≥(1−T)dT给K≤8(D+1)²64^D。因此任何非零λ∈Q使λΔ∈Z[Z]，均有
$$
|\lambda\Delta(X)|=\frac{|\lambda A|}{K}
 \ge[8(D+1)^2\,64^D]^{-1}.
$$
包含最优共同约分及有理换基。D=o(m²)时不能给严格负m²率。其线性Padé仍需原生实际来源倍数C_s满足limsup s^-1logC_s<2log(3+2√2)，正性和裸误差不替这项费用。以下新构造改变的是极点阶数与完整系数秩。

### 2.2 只改最终整值规范没有二次信用

非零F∈Z[Z]、degF=d时，全部整数值的共同因子g_val满足g_val | d!·g_coef。证明：Newton有限差分给F=ΣΔ^kF(0)·binom(Z,k)，g_val整除每个差分，而d!binom(Z,k)∈Z[Z]，所以g_val整除d!F的每个系数，进而整除其系数内容d!g_coef。故d=O(n)时此规范至多额外O(n logn)，不改变二次主项。它不否定原source增长行格的真实收益、指定q额外估值或其他次数。

## 3. 增长极点的完整原生周期图

对正整数n定义实际正泛函
$$
\mathcal I_n(P)=\int_0^1
 \frac{P(T)(-\log T)(2+1/(2\sqrt T))}{(1+T)^n}\,dT.
 \tag{G1}
$$
内部密度严格正，端点可积。把P/(1+T)^n=A(T)+Σ_{j=1}^n a_j/(1+T)^j完整分解。A的第k单项式矩为2/(k+1)²+2/(2k+1)²，全部有理头保留。

为核全部极点，令I_j(α)=∫₀¹T^{α−1}(1+T)^−j dT。分部积分给
$$
I_j(\alpha)=f_j(\alpha)I_1(\alpha)+U_j(\alpha),\quad
f_j=\prod_{h=1}^{j-1}(1-\alpha/h),\quad U_1=0,
$$
$$
U_j=(1-\alpha/(j-1))U_{j-1}+2^{1-j}/(j-1).
$$
对α>0求负导数。用I₁(1)=log2、I₁(1/2)=π/2、−I₁′(1)=ζ2/2、−I₁′(1/2)=4G，得到全部形式周期向量(1,ζ2,G,log2,π)。有理栏为
$$
\sum_k[A]_k\left(\frac2{(k+1)^2}+\frac2{(2k+1)^2}\right)
-\sum_{j=1}^na_j(2U'_j(1)+\tfrac12U'_j(1/2)).
 \tag{G2}
$$

置z=1+T，C_f(P)=[z^{n−1}]f(z)P(−1+z)，并仅在形式jet中定义
$$
a(z)=(1-z)^{-1/2},\qquad L(z)=-\log(1-z).
$$
它们不被沿T∈(0,1)作实际密度使用。四个非有理栏严格为
$$
[\zeta2]=C_1,\qquad [G]=2C_a,\qquad
[\log2]=2C_L,\qquad [\pi]=\tfrac14 C_{aL}.
 \tag{G3}
$$
例如[z^h]a=binom(2h,h)/4^h，[z^h]aL=2[z^h]a·Σ_{k=1}^h(2k−1)^−1；与负导数逐项相符。无需假设这些实际数值独立。

要对空间V的全部pq纯化为X，须共同双线性条件C_{a−1}(pq)=C_L(pq)=C_{aL}(pq)=0。高阶消零的免费选择确实失败：n=2h+1、V=(1+T)^hW时实际回到§2的n=1配对，目标秩≤1；n=2h、V=(1+T)^hW时只剩有理矩。下面不用此选择。

## 4. 显式非单项式共同纯空间

固定m≥1、n=8m、N=n−1。以下直接以z表示基多项式，实际使用p_i(1+T)。设
$$
l_i(z)=z^i\quad(0\le i<m),\qquad
\mathcal U=z^{4m}\mathbb Q[z]_{\le4m-1}.
$$
对f∈{1,a−1,L,aL}定义B_f(p,q)=[z^N]f(z)p(z)q(z)。线性映射
$$
\mathcal T:\mathcal U\longrightarrow\mathbb Q^{4m},
\quad u\longmapsto(B_f(u,l_j))_{f,\ 0\le j<m}
 \tag{G4}
$$
是有理可逆方阵。因为u=z^{4m+h}时其条目为[z^{4m−1−h}]z^jf；它是四族z^j{1,a−1,L,aL}的首4m个Taylor jet矩阵，取转置并把jet阶数倒序。

证明满秩不用generic性。把a−1换成a，再令w=1−z，经有理三角换基成为
$$
w^k,\quad w^{k-1/2},\quad
w^k\log w,\quad w^{k-1/2}\log w,\qquad 0\le k<m.
$$
这是2m个不同Euler指数、各重数2的完整解族。w=1为普通点；令t=logw后的合流Vandermonde非零，所以首4m jet可逆。原系数均有理。

对每个i唯一选u_i∈𝒰，使
$$
B_1(u_i,l_j)=\tfrac12\delta_{ij},\qquad
B_f(u_i,l_j)=-\tfrac12B_f(l_i,l_j)
\quad(f=a-1,L,aL).
 \tag{G5}
$$
令p_i=l_i+u_i。高高乘积最低次数8m>N，四类trace全零；低低次数≤2m−2<N，B₁低低为零。交叉项由(G5)及对称性严格给
$$
B_1(p_i,p_j)=\delta_{ij},\qquad
B_{a-1}(p_i,p_j)=B_L(p_i,p_j)=B_{aL}(p_i,p_j)=0.
 \tag{G6}
$$
低jet保证p_i线性独立，deg p_i≤8m−1。故同一个实际正Gram是
$$
M_m=\bigl(\mathcal I_{8m}(p_i(1+T)p_j(1+T))\bigr)
 =R_m+XI_m>0,\qquad R_m\in\operatorname{Sym}_m(\mathbb Q).
 \tag{G7}
$$
这是全尺度纯目标空间，实际目标系数秩恰m，不是ambient秩推断，也不是逐行自由selector。

还可明确(G4)的绝对行列式：
$$
|\det\mathcal T|=
2^{-4m(2m-1)}
\frac{\left(\prod_{j=1}^{2m-1}j!\right)^4}
{\prod_{h=1}^{4m-1}h!},\quad
\log|\det\mathcal T|=-16(\log2)m^2+O(m\log m).
 \tag{G8}
$$
指数为间距1/2的2m点，各重2；再除Taylor行阶乘即得。它只认证可逆性/尺度，不能把逆det当实际来源高度，更不能当本原费用。

## 5. 尚未支付的完整预算及正式决定

定义唯一实际对象
$$
Q_m(Z)=\det(R_m+ZI_m)\in\mathbb Q[Z],\quad
\deg Q_m=m,\quad Q_m(X)>0.
$$
令λ_m>0为Q_m全部系数的最小共同分母，则P_m=λ_mQ_m∈Z[Z]且本原；因Q_m首一，λ_m是正整数。这不是说Q_m已经整系数。

若X=u/v，v>0，则v^mP_m(X)是正整数。故充分出口是同对象严格
$$
\limsup_{m\to\infty}\frac{\log\lambda_m+\log\det M_m}{m^2}<0.
 \tag{G9}
$$
线性评价分母m logv被吸收，全部有理反证覆盖；无需先证Q_m(q)对任意q都非零。**(G9)没有支付。** 基底分母、全部有限头、2处与所有prime powers、本原信用及同一Gram的实处界均不能省略。先清基底再取det与直接清Q只能选一致费用链，不能重复计费；有理换基也不免费改变本原多项式。

本轮完成正式全路线比较，last_global_review=269。全尺度新纯配对及实际非零已证，但未给数值准入/完整负净预算，连续未改善该项计数保留9。所有已闭数学窗口不重开。唯一下一项为[270一轮来源预算核查](growing_pole_budget_charter_round270_20261020.md)，固定上述n=8m、p_i、R_m、Q_m；不调参数或扫描。只有匹配完整费用和实处界才准入后续数值实施，否则到期结束，总goal保持active。

新构造的决定依据是(G6)–(G7)，不是仅有尚未排除的共同各向同性猜测。低阶源的原秩一障碍不覆盖实际rank m的新对象；旧Catalan PV双变量、K5、M₀,₈及mixed整jet也不是它的同一载体。

审阅范围：根代理全文读成果地图、原ζ5方法扩展、269任务及本轮恢复入口，重读252的Jacobi证明段，独立推导(G1)–(G9)。三位代理均全文复读保存的269证明与270任务，分别重建全部周期映射、Euler共同纯空间、正性、det常数、整化与反证链；原贡献不计自身独审。整稿审阅发现的λ≠0遗漏已修正，GZ原式与Tate纯化已拆开；270明确实际评价量词及允许严格足够的费用上界。

本轮来源核查的实际范围保留如下，不能从代理间复述继承FULL标签：

- 围道代理全文核Viola报告两页；Eskandari v1核§1.1–1.3、§2、§5与§4末接口，未完整复核§3–4的渐近与实侧估计。
- Apéry代理核GKS v3 PDF第1–7、14、23–26、28–33页，GZ已存作者稿第1–5、11–21页；另核2021正式版的版本信息、κ实验表述及Theorem6相关文字；KZ第1–6页及本地反项载体独审。
- 全路线代理核p-adic v1引言、Lemma2.1、Definition3.1、Lemma4.5/6.3及§7–8高度/乘积判据接口；没有全文审计该论文。

这些网页与固定版本的实际选读不构成全球新颖性穷尽；候选值此前已做[262定向核查](next_route_novelty_20261012.md)，本轮不声称首次性。没有数学producer、CAS、参数/n/prime/Padé扫描或Lean执行；原文献与形式化资产保留。
