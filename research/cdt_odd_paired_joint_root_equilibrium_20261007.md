# 真实联合根—镜像目标：付费对数改进、紧根最优存在与严格对偶

2026-10-07，NEW，作者 `/root/scaled_root_finalize`。本轮开始时540冻结记录及 last audit SHA `7141ac2383dee7e1f2bf0828c993a17de4c0738b4f8a90dd6a627f9d97a43be3` 保持只读。原 B6/κ3/s5、degree<3n、rank2n、原饱和整数值格 S 与 whole-X D_A(X) 不动。本稿纯纸面；新增数学 producer 执行0，旧/成功/同行 execute-import-rerun0，辅助素数扩表0。最终独审和来源收据另存，当前不预先声明完成。

## 1. 真正要优化的同一对象

实际全文回读当前 main §155、冻结 [mirror/root 稿 C1–C22](cdt_odd_paired_mirror_root_correlation_20261007.md)、[multiroot 稿 P1–P14](cdt_odd_paired_multiroot_potential_improvement_20261007.md)、[mirror 稿 M1–M23](cdt_odd_paired_mirror_choice_energy_20261006.md)。另实际读取冻结 energy E1–E4、E18–E25 中所用的准确常数，不冒称该 energy 稿本轮全部全文回读。

对有限正原子概率测度 ρ=Σω_iδ_(s_i)，s_i>0，定义

\[
U_\rho(y)=\int\log|s-y^2|d\rho(s),\quad
A_\rho(y)=Q(y)+U_\rho(y),\quad M_\rho=\sup_{y\ge0}A_\rho(y),
\]
\[
L_\rho(x)=\int\log(s+x^2)d\rho(s),\quad
\mathcal F_\rho=\max_{p\in\mathcal C}\Phi_\rho(p),\quad
\boxed{\mathcal J(\rho)=M_\rho+\mathcal F_\rho.}
\tag{J1}
\]

根处的 U 按−∞解释；Q、h、K 和 mirror constraint C 准确沿冻结稿：

\[
\mathcal C=\{p(x)dx:0\le p\le1,\ p(x)+p(2-x)=1\text{ a.e. on }[0,2]\},
\]
\[
K(x,y)=\log\left|\frac{x-y}{x+y}\right|,\quad
h(t)=(6+t)\log(6+t)-2t\log t-(2-t)\log(2-t)-6\log6+2,
\]
\[
\Phi_0(p)=2\int_0^2h(2-x)p(x)dx+\iint K(x,y)p(x)p(y)dxdy,
\quad\Phi_\rho(p)=\Phi_0(p)-\int_0^2L_\rho(x)p(x)dx.
\tag{J2}
\]

C 中每个 density 总质量为1。冻结 mirror 的 log-tail 估计使 K-energy 在 C 上连续，C 弱紧；K 严格负定使 Φ_ρ 严格凹，故最大值存在且 maximizer p_ρ 唯一。这里每个 head 的 L 与同一个实际 choice 密度共同支付；没有改回逐 pair 全小距离下界。

## 2. exact 联合目标传回原行列式的完整费用

置 c_n=2n+1/2，N=floor(n/2)，ΣN_i=N；N>0时选 N_i/N=ω_i+O(1/n)，N=0时所有N_i=0、q=1。定义
\[
q_{n,\rho}(z)=\prod_i((z-c_n)^2+n^2s_i)^{N_i}.
\tag{J3}
\]
degree(q)≤n，全部真实 head 上 q>0。沿原高列 determinant1 剪切保留 whole-X D_A(X)，系数可先在实数中；原整化费继续用于同一多项式，未声称新列免费成为整数基。

记冻结 coupled C9 中真实正 choice 和的平方为 T_(n,q)。该准确全 n 上界给
\[
\log|D_{A,n}(\xi)|\le\log Z_{H,n}-2\log F_n-2\log\Gamma_n
+n\log A_n(q)+\log T_{n,q},
\tag{J4}
\]
其中 ξ=aζ(4)+bζ(5)、b≠0。只有假设 ξ 有理，才能与那个有理 input 的 D_A 值识别。冻结全轴/奇偶/舍入转移及 exact mirror limit 给
\[
n\log A_n(q)\le(4n^2+4Nn)\log n+n^2M_\rho+O(n\log(n+2)),
\]
\[
\log T_{n,q}=-(4n^2+4Nn)\log n+n^2\mathcal F_\rho+o(n^2).
\tag{J5}
\]
前式的 pole exclusion、固定根权重舍入和指数尾部均由冻结 P2 完整支付；后式是冻结 C17 的实际正和 equality。没有把它当 complex determinant equality，或将尚未给速率的 o(n²) 免费改成 O(nlogn)。

设
\[
H_* =\int_1^2h(t)dt,\quad G_* =\int_2^3(u\log u-u)du,
\quad M_0=\sup_yQ(y),\quad M_1=\sup_y[Q(y)+\log(1+y^2)].
\]
冻结 energy E19/E21 准确给 limsup n⁻²(log Z_H−2log F)≤M_1−2G_*。从同一 E3/E22 有
\[
\beta_0+\tfrac12\log2=-M_0-M_1-2H_*+2G_*.
\]
因此定义
\[
\boxed{\mathcal B(\rho)=2G_*-M_1-\mathcal J(\rho)
=\beta_0+\tfrac12\log2+M_0+2H_*-\mathcal J(\rho).}
\tag{J6}
\]
J4–J5 中所有 n²logn 准确相消，得到
\[
\limsup_{n\to\infty}n^{-2}[\log|D_{A,n}(\xi)|+2\log\Gamma_n]
\le-\mathcal B(\rho),
\]
\[
\boxed{\limsup n^{-2}\log|D_{A,n}(\xi)|
\le-\mathcal B(\rho)-2\gamma,\quad
\gamma=\liminf n^{-2}\log\Gamma_n.}
\tag{J7}
\]
第一式表示对每个 ε>0，充分大的全部 n 都满足 log|D_A|≤−(B−ε)n²−2logΓ；有限初项可单独付常数。这是全尺度 transfer，不是有限项拟合，也不删除 Γ。

冻结 C19 给 F_ρ≤2H_*−I_ρ−d_ρ，所以
\[
\mathcal B(\rho)\ge\beta_0+\tfrac12\log2+\varepsilon_\rho+d_\rho,
\quad\varepsilon_\rho=M_0-M_\rho+I_\rho.
\tag{J8}
\]
因此 J 下降多少，就在同一原 determinant 的已付解析 rate 上增加多少；不再把 I、d 或 κ/Hardy 额外扣第二次。

## 3. 有限根联合目标总能严格改进：收益为 t log(1/t)

**Theorem J9。** 对每个有限正原子 ρ，存在另一有限正原子 σ 和常数 α>0、C≥0、t_0>0，使 0<t<t_0 时
\[
\boxed{\mathcal J((1-t)\rho+t\sigma)
\le\mathcal J(\rho)-\alpha t\log(1/t)+Ct.}
\tag{J9}
\]
特别充分小的 t 给真实 joint 目标严格下降，其右方向差商趋−∞。这比此前只优化 M_ρ−I_ρ 的 P3 强，真实镜像 field 的最坏变化已支付。

证明先核全部 numerator 最大点有限：
\[
A'_\rho(y)=7\arctan(2/y)-2\arctan(8/y)-2\pi
+\sum_i\frac{2\omega_i y}{y^2-s_i}.
\tag{J10}
\]
其0+导数π/2>0，旧根附近 pole 主导、无穷远导数→−2π。因此最大点避开0、全部旧根及无穷尾。在每个剩余紧区间导数为非零实解析函数：相邻根的 pole、首段0+导数或末段无穷极限排除恒零。紧集内零点有限，故全部最大点为 y_1,…,y_h，均>0且不等于旧根。每个局部解析最大点有有限偶数消失阶 m_j≥2，可取互不交叠、避开旧根的 U_j 及 a_j>0，使
\[
A_\rho(y)\le M_\rho-a_j|y-y_j|^{m_j}\quad(y\in U_j).
\]
置 m_*=Σ_jm_j，v_j=m_j/m_*，
\[
\sigma=\sum_jv_j\delta_{y_j^2},\qquad\alpha=1/m_*.
\tag{J11}
\]
在 U_j 内，其他新根 log 项及全部旧根项有统一有限上界；log|y²−y_j²|=log|y−y_j|+log(y+y_j)。故存在 b_j∈R，使
\[
U_\sigma(y)-U_\rho(y)\le v_j\log|y-y_j|+b_j.
\]
令 ρ_t=(1−t)ρ+tσ。对 r=|y−y_j|>0，
\[
A_{\rho_t}(y)\le M_\rho-a_jr^{m_j}+tv_j\log r+tb_j.
\]
全 r>0 的该上界最大值准确为
\[
M_\rho+\frac{tv_j}{m_j}
\left[\log\frac{tv_j}{a_jm_j}-1\right]+tb_j
=M_\rho-\alpha t\log(1/t)+t\{b_j+\alpha[\log(1/(a_jm_*))-1]\}.
\tag{J12}
\]
根点处为−∞。取 C_N≥0 不小于全部括号，得到 U=∪U_j 上的统一上界。

U 的补集无最大点；上半连续性和统一无穷尾给 η>0，使 A_ρ≤M_ρ−η。在 U 外用精确 convex combination 得
\[
A_{\rho_t}\le(1-t)(M_\rho-\eta)+tM_\sigma.
\]
令 H=(M_σ−M_ρ+η)_+。只须 tH≤η/2 和 αtlog(1/t)≤η/2，即使补集上界也不超过 M_ρ−αtlog(1/t)+C_Nt。充分小 t 同时满足这些条件。所以
\[
M_{\rho_t}\le M_\rho-\alpha t\log(1/t)+C_Nt.
\tag{J13}
\]

现在支付 actual mirror optimizer 的移动：L_σ−L_ρ 在[0,2]上有界连续，置 B=||L_σ−L_ρ||_∞。对每个 p∈C，质量为1给
\[
\Phi_{\rho_t}(p)=\Phi_\rho(p)-t\int(L_\sigma-L_\rho)p
\le\Phi_\rho(p)+tB,
\quad\mathcal F_{\rho_t}\le\mathcal F_\rho+tB.
\tag{J14}
\]
没有假定 p_ρ 保持不动或丢掉最坏 choice。J13–J14 给 J9，C=C_N+B。进一步 t≤exp(−2C/α) 时，付费信用至少
\[
g(t)=\alpha t\log(1/t)-Ct\ge\tfrac12\alpha t\log(1/t)>0.
\tag{J15}
\]

**有理参数。** 对固定有限正根配置，M 连续：最大点有统一紧集和避根距离，参数子列逼近旧根会因正权 log→−∞被排除；其余处普通连续性给 upper，旧最大点给 lower。L 在[0,2] uniformly 连续，因此 |F_ρ−F_ρ'|≤||L_ρ−L_ρ'||∞。所以 J 也连续。把 ρ_t 的位置及权重用正有理数近似，保持权重和1，可得完全有理的有限 ρ' 且
\[
\mathcal J(\rho')\le\mathcal J(\rho)-g(t)/2.
\tag{J16}
\]
其 q 系数有理；原 degree、S 和 whole-X determinant 未改变。J7 因而给至少 g(t)/2 的同对象新增解析 credit。没有程序执行或有限素数单位数据。

## 4. 从现有根4/7出发的明确对数量级

对 ρ=δ_(4/7)，A''_ρ=Q''−2(s+y²)/(y²−s)²。y²<416 时 Q''<0，所以 A''<0。y²≥416 时
\[
Q''=\frac{2(y^2-416)}{(y^2+4)(y^2+64)}<2/y^2,
\quad\frac{2(s+y^2)}{(y^2-s)^2}\ge2/y^2
\quad\text{if }y^2\ge s/3.
\]
这里 s=4/7，条件自动满足。因此两段 (0,√s)、(√s,∞) 中 A 都严格凹；各段端点导数的符号给恰一个峰。全部全局最大点 h≤2，每个 m_j=2，故 J11 可取 α=1/(2h)≥1/4。于是有 C≥0、t_0>0，使
\[
\boxed{\mathcal J(\rho_t)\le\mathcal J(\delta_{4/7})
-\tfrac14t\log(1/t)+Ct.}
\tag{J17}
\]
取 g_0(t)=tlog(1/t)/4−Ct>0、且满足上述邻域/补集条件，再作 J16 有理近似，则冻结保守 rate 与 J7–J8 给
\[
\boxed{\limsup n^{-2}\log|D_{A,n}(\xi)|
<-12.62342839512558-g_0(t)/2.}
\tag{J18}
\]
这是真实全尺度且已支付镜像移动的正 credit，g_0 的构造常数来自全部实际峰和局部下降。尚未给 t、C、g_0 的新的有理区间数值，所以不报告新的绝对小数 rate，也不把未知 optimum 当数值结论。J17 的对数系数1/4是纸面已证。

## 5. 连续根测度：先控制奇点再作紧性

以下只固定任意紧正根区间 S=[a,b]，0<a≤b<∞，允许所有概率测度 ρ∈P(S)。J1–J2 的定义保持，U 可在某些 y 为−∞。在每个固定 y-compact 上，max(log|s−y²|,−R)有界连续，R→∞单调下降；因此U以及A是上半连续的，有限sup实现。M 始终有限，因为 y>√b 的固定点有有限统一 lower，尾部
\[
A_\rho(y)\le Q(y)+\log(b+y^2)\longrightarrow-\infty
\]
uniform in ρ。故全部最大点位于固定紧区间。对足够小 y>0，Q'(y)>π/4 且 |U'_ρ(y)|≤2y/(a−y²)<π/4，所以 A 严增、0不是最大点。

令 V 为所有有限混合的正半轴有界区间 uniform probability measures。对 ν∈V，定义
\[
\ell_\nu(s)=\int\log|s-y^2|d\nu(y).
\tag{J19}
\]
这在 S 上有界连续。理由：log|s−y²|=log|√s−y|+log(√s+y)，第一项积分用 zlog|z|−z 的连续 primitive（0log0=0），第二项在 S×supportν 上普通连续。ν的每个区间下端严格正。

**平均恢复 lemma。** 对任意ρ∈P(S)，
\[
\boxed{M_\rho=\sup_{\nu\in V}\left[\int Qd\nu+\int\ell_\nu(s)d\rho(s)\right].}
\tag{J20}
\]
≤方向是任何平均≤sup。证明≥时取一个 finite maximizing y_0>0，令ν_ε为[y_0−ε,y_0+ε]上的uniform，ε<y_0/2。对 d=√s−y_0，有 elementary bound
\[
\frac1{2\epsilon}\int_{-\epsilon}^{\epsilon}\log|d-v|dv
\ge\log|d|-(1+\log2).
\tag{J21}
\]
若 |d|≥2ε，用 |d−v|≥|d|/2；若 |d|≤2ε，缩放后的平均为 [(1+z)log|1+z|+(1−z)log|1−z|]/2−1，其中z=d/ε。它是偶函数，对z>0导数log|(1+z)/(1−z)|/2≥0，故最小值−1，而 log|z|≤log2。第二项 log(√s+y) 的平均和点值差 uniform→0。由于 A_ρ(y_0)>−∞，点值 log|s−y_0²| 的负部可积，且 y_0²不能为ρ的atom。J21给同一个可积 lower dominator；Fatou于是给 liminf∫ℓ_(ν_ε)dρ≥U_ρ(y_0)，Q连续，得到J20。这里没有把负无穷 kernel 当普通连续 payoff。

J20使 M 是 continuous-affine functions of ρ 的 supremum，故 lower semicontinuous。upper semicontinuity也准确成立：取ρ_k→ρ的最大点y_k，统一紧尾部允许子列y_k→y；在固定compact上 truncation
\[
\max(\log|s-y^2|,-R)
\]
有界连续。先weak limit、后R→∞，给 limsup U_(ρ_k)(y_k)≤U_ρ(y)，因此limsup M_(ρ_k)≤M_ρ。M于是弱连续。

同时 L_(ρ_k)→L_ρ uniformly on[0,2]：连续kernel log(s+x²)在 S×[0,2]上uniform连续，用有限x-net和weak convergence直接证明。因此 F、J也连续。M和F均为 affine root functionals 的supremum，J凸。

**Theorem J22。** 对每个固定紧正 S，存在 ρ_S∈P(S)使
\[
\mathcal J_S=\min_{\rho\in P(S)}\mathcal J(\rho)=\mathcal J(\rho_S).
\tag{J22}
\]
证明为 P(S)弱紧、J连续；没有把未受限(0,∞)当紧集。有限正有理位置/权重测度弱稠密于P(S)，若S单点为无理数须保留该单点、不能声称该区间内有理根稠密。对 a<b，完全有理的有限配置因此可把 J 逼近 J_S；每个固定配置由J7传回原q。此处不使用随n变化的连续最优配置绕过固定根转移。

有限原子若在P(S)中最优，而它的所有 contour maximum squares都属于S，则J9的σ也在P(S)，导致矛盾。因此这类有限最优配置必有一个最大点平方落在S外。它不证明未受限最优存在，也不证明任意受限最优无原子；边界限制可能阻止新根进入。

## 6. 紧根问题的严格联合对偶，不作形式 minimax 交换

对 ν∈V、p∈C，置
\[
G_{\nu,p}(s)=\ell_\nu(s)-\int_0^2\log(s+x^2)p(x)dx,
\]
\[
\mathscr G(\rho;\nu,p)=\int Qd\nu+\Phi_0(p)+\int G_{\nu,p}(s)d\rho(s).
\tag{J23}
\]
G_(ν,p)在S上连续；J20和J1的两个独立sup准确给 J(ρ)=sup_(ν,p)Gscript。该 payoff在ρ上affine连续，在(ν,p)上concave，因为Φ0凹。

**Theorem J24（exact value duality）。**
\[
\boxed{\mathcal J_S=
\sup_{\nu\in V,\ p\in\mathcal C}
\left\{\int Qd\nu+\Phi_0(p)+\min_{s\in S}G_{\nu,p}(s)\right\}.}
\tag{J24}
\]
弱对偶≤方向直接对任意ρ积分min_sG≤∫G。下面自证相反方向，不把有log poles的原始点质量ν免费代入一般 theorem。

取 c<J_S。每个ρ∈P(S)都有某(ν,p)使Gscript>c；固定(ν,p)在ρ上连续，故这些open sets覆盖紧P(S)，可取有限cover，记相应连续affine functions g_1,…,g_m。其值向量
\[
W=\{(g_1(\rho),\ldots,g_m(\rho)):\rho\in P(S)\}
\]
紧、凸，且与D=(−∞,c]^m不交。有限维严格分离给非零λ_j≥0（有负系数时D的该向上support为∞，不能分离），归一化Σλ=1后
\[
\min_\rho\sum_j\lambda_jg_j(\rho)>c.
\]
置νbar=Σλν_j∈V、pbar=Σλp_j∈C。Φ0凹而其他项线性，所以
\[
\mathscr G(\rho;\overline\nu,\overline p)
\ge\sum_j\lambda_jg_j(\rho)>c\quad\text{for all }\rho.
\]
对ρ取min就是constant+min_sG_(νbar,pbar)>c。c可任意逼近J_S，得到J24。该证明的有限cover来自J19–J20已处理的平均kernel；没有未经验证的−∞ minimax交换或ν端dual attainment断言。

J24给具体可核查的 global lower certificate：任何显式有限interval-mixture ν、合法mirror density p 和G_(ν,p)的全S下界，都会下界J_S。任何固定根ρ对M、maxΦ的真实全域upper则上界J_S。两者差可检验全局root优化余量，而不是用有限sampling宣称最优。当前未运行这个新的primal/dual数值证书。

## 7. root 与 mirror 的同时一阶接口

对有限ρ、有限σ，若σ在旧全部最大点y_j²没有atom，使新log在这些点附近有界连续，则紧集最大点 argument 给
\[
\left.\frac{d}{dt^+}M_{(1-t)\rho+t\sigma}\right|_{t=0}
=\max_j[U_\sigma(y_j)-U_\rho(y_j)].
\tag{J25}
\]
旧根由(1−t)ρ的uniform正权排除；新根不在旧最大集合，其邻域有旧gap。又紧根测度的M连续、最大点的上半连续极限必须落在旧最大集合，因此充分小t的全部最大点都在避开新旧根的上述邻域。其上方向势有界连续，给J25的准确max-directional formula，不把导数穿过pole。对镜像项，由C弱紧、Φ连续、旧maximizer唯一，ρ_t的maximizer子列必趋p_ρ。用固定p_ρ与变化p_(ρ_t)两边夹住差商，得
\[
\left.\frac{d}{dt^+}\mathcal F_{(1-t)\rho+t\sigma}\right|_{t=0}
=-\int_0^2(L_\sigma-L_\rho)p_\rho.
\tag{J26}
\]
故两项的准确联合一阶导数为
\[
\boxed{\mathcal J'(\rho;\sigma-\rho)=
\max_j[U_\sigma(y_j)-U_\rho(y_j)]
-\int_0^2(L_\sigma-L_\rho)p_\rho.}
\tag{J27}
\]
与此同步，p_ρ满足冻结C18的box/mirror条件，外场含Ψ_ρ/2。当σ置于所有轮廓峰时J25的有限连续前提不成立，正确结论由J9是差商→−∞，不能把−∞冒换成一个普通梯度。

这些条件、J24和J9共同明确两个未知者：根测度与真实mirror密度。没有假定全小距离density、monic归一化或一般S-curve自动给本项目的解。

## 8. 新原始文献与准确阅读范围

先检查literature未有Sion/minimax原件，再搜索并以正常verified TLS从publisher保存 Maurice Sion, *On general minimax theorems*, Pacific J.Math.8(1958),171–176：[原件](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf)/[本地](../literature/cdt_paired_joint_root_sources_20261007/sion1958_general_minimax_pjm8_171_176.pdf)。归档PDF9页、740453bytes、SHA256 `e21e748347986009d1d5cce9526e8aad5ff37de0c0cd911fb45df9ae75a4020c`。实际完整文本读PDF1–7共7distinct页，其中PDF2–7为该6页article，PDF1为封面；PDF5–6另render目视核compactness推论与4.2′。未读PDF8–9，不称整个归档全文读完。

PDF5的3.4及其后的一端紧推论明确compactness和semicontinuity要求（原件将该corollary印作3.3，未改原件）；PDF6的4.1/4.2′用concave-convexlike结构与一端compact归结有限cover。本稿payoff先用interval averages排除−∞，再独立给有限cover/分离证明J24；未把原始singular kernel未经条件核查直接套用Sion。原件给出的理论方向和本题的完整额外论证区分清楚。

第一次PDF文本输出在PDF2因Windows GBK console遇UnicodeEncodeError；改UTF-8后读取PDF2–7。它是阅读工具编码失败，未修改原件，也不是数学producer失败或重跑。没有关闭TLS、没有新增外部源码/HTML或数学执行。

## 9. 本轮实际进展与未证条件

已证：真正J=M+maxΦ的全尺度同对象transfer；每个固定有限正根配置可付费获得αtlog(1/t)−Ct的严格joint改进；现有4/7起点可取对数系数至少1/4，并可转成完全有理配置；固定紧正根区间的连续凸最优问题、最优存在、有限有理配置逼近，以及已处理log奇点的exact联合dual value。仍未解出root measure、p-density或新的绝对小数rate。

原actual目标压缩与剩余矩阵的无限非退化、fixed rational source无限成功、whole-X无限非零及足够strict margin仍缺。safe normalization upper约40.314517426不是最小费用、费用下界或no-go。有限原子永远可改进也不推出信用无界；紧区间exact dual不等于未受限全局最优已存在。没有新增ζ/L/Catalan无理性或线性无关性结论，没有Lean。本文待实际全文独审、作者最终回读后再作FINAL来源收据。
