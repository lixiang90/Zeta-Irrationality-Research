# 第264轮：完整整jet的费用下界与leading-box桥

2026-10-13。固定263的实际 $s$、全部 $b=0,c=\pm d\ne0$ 反证类、$f=(1,J,\theta_sJ)$、$\mathbb Q(s)$-rank3及普通Taylor输出。本稿没有新数值无理性定理，也没有把标量cap当成实际格费用。上一goal turn完成263数学首证书、正式复盘与持久状态，分类为progress；本轮推进其唯一剩余净预算关。

**裁决：** 单变量完整整jet的index-only BC入口有真实费用下界，即使第二Smith层理想也不能通过。balanced整jet格与正确leading消去约束的交集可证保留263信用，原monomial系数box也可重建，但当前证书支付的系数增长仍太大。这条box桥使用CDT§6.5的Cauchy/rearrangement解析估计；不把它冒称原BC metric下的新τ。原稳定窗口两轮到期，结束该实现的默认投入，返回宏观来源选择。完整intrinsic jump费用及全部tensor方法未被否定。

## 1. 同一实际有限矩阵与最高层rank下界

沿用[263评价格](joint_evaluation_lattice_round263_20261013.md)的
$$
 E_D=\mathbb Z[s]_{\le D}^{\oplus3},\quad
 N_D=3(D+1)+C,\quad
 \Gamma_D=T_{D,N_D}^{-1}(\mathbb Z^{N_D+1})\cap E_D.
$$
这里 $C$ 是固定来源的Shidlovsky常数，不随 $D,p$ 变化。对 $p>\sqrt{N_D}$ 的好素数，令 $k=k_r\in\{1,3\}$、$L=N_D-kp+1$。两个 $k$ 各占素数密度一半。最高层矩阵 $B=p^2T$ 的rank $r_p$ 是
$$
 (P_1,P_2)\longmapsto A P_1+\theta_sA P_2\pmod{s^L}
 \tag{1}
$$
的rank；若 $L\le0$ 取0。原packet的 $s^{kp}$ 和形式单位只改变截断位置或作可逆行变换。固定坏素数与小素数全部保留，但下界可不计其非负费用。

263已证 $\theta A/A=U_p/V_p$，$(U_p,V_p)=1$、$V_p(0)\ne0$、$\deg V_p=4p$、$\deg U_p\le4p$。乘单位 $V_p/A$ 把(1)化为
$$
 (P_1,P_2)\longmapsto V_pP_1+U_pP_2\pmod{s^L}.
 \tag{2}
$$
因此有三个独立可核的rank下界：

- $P_1$ 的unit Toeplitz子块给 $r_p\ge\min(D+1,L)_+$。
- $D\ge4p$ 且 $L\ge D+4p+1$ 时，完整多项式核恰为 $(-U_pR,V_pR)$，维数 $D-4p+1$，故 $r_p=D+4p+1$。对 $p\le D/4$、$k\le3$，这个截断条件成立。
- $D<4p$ 时完整多项式map单射，维数 $2D+2$。删掉 $s^L$ 及其以上最多 $(D+4p-L+1)_+$ 个坐标，只能使rank减少这么多。因此 $r_p\ge\min(2D+2,D-4p+L+1)$，与unit界取较强者。

令 $x=p/D$，忽略统一 $O(1)$ 后，这给 $r_p/D\ge\ell_k(x)+o(1)$，其中
$$
\ell_k(x)=
\begin{cases}
1+4x,&0\le x\le1/4,\\
2,&1/4\le x\le2/(k+4),\\
4-(k+4)x,&2/(k+4)\le x\le3/(k+4),\\
1,&3/(k+4)\le x\le2/k,\\
3-kx,&2/k\le x\le3/k,\\
0,&x\ge3/k.
\end{cases}
\tag{3}
$$
两个 $k$ 的端点均按这个顺序排列。这里没有要求每个原coeff处处非零，也不依赖未算的Bockstein rank。

## 2. 实际完整index的不可越过部分

263的精确Smith身份为
$$
 \log_p[E_D\otimes\mathbb Z_p:\Gamma_D\otimes\mathbb Z_p]
 =2r_p+t_p\ge2r_p,
 \tag{4}
$$
其中 $t_p$ 是第二层Bockstein rank。PNT_AP对(3)逐段积分：
$$
 \int_0^3\ell_1(x)\,dx
 =\frac38+\frac3{10}+\frac3{10}+\frac75+\frac12
 =\frac{23}{8},
$$
$$
 \int_0^1\ell_3(x)\,dx
 =\frac38+\frac1{14}+\frac3{14}+\frac5{21}+\frac16
 =\frac{179}{168}.
$$
各类密度 $1/2$ 与(4)的因子2相消；被去掉的 $p\le\sqrt{N_D}$ 窗口为 $o(D^2)$。因此
$$
 \boxed{\liminf_{D\to\infty}
 \frac{\log[E_D:\Gamma_D]}{D^2}\ge\frac{331}{84}.}
 \tag{5}
$$
这是实际canonical完整整jet格的index下界。任何完整整jet整数化子格 $\Gamma'_D\subset E_D$ 均包含于 $\Gamma_D$，其index不会更小。即使令所有 $t_p=0$、其它places免费，(5)仍成立。

在[237同metric BC桥](joint_lattice_metric_bridge_round237_20261008.md)中，**仅将有限graded heights放宽到0、以完整index作为费用**的证书需要 $\tau_{\rm index}=2\kappa/9$，其中 $\kappa$ 为完整index率的有效upper。任何这样的upper至少是(5)，故
$$
 \tau_{\rm index}\ge\frac{331}{378}
 >\frac{20}{27}>\frac23\log3.
 \tag{6}
$$
最后的严格必要门槛来自[262](research_next_route_progress_round262_20261012.md)，同一合法图 $\lambda<\log3<10/9$。所以这一个index-only入口确实关闭，不能靠第二Smith层更低rank重开。它覆盖当前全部±关系类和该完整整数化子格，不覆盖全部算术holonomy。

**不能扩大下界的对象。** 原同metric的intrinsic费用是实际jump子式
$$
 \mathcal A_D=-\log|\det T_{V_D}|,
$$
而不是 $\log[E_D:\Gamma_D]$。237精确抵消公式仍为
$$
 \mathcal A_D=\log[E_D:\Gamma_D]
       +\sum_{n\in V_D}h_{\rm fin}(\psi_{\Gamma_D}^{(n)}).
 \tag{7}
$$
在237所用的统一 $\limsup$ upper证书中，需要 $\limsup\mathcal A_D/D^2<3\log3$。由(5)，该统一证书须有尚未证明的负graded信用超过
$$
 \frac{331}{84}-3\log3>\frac{17}{28}
 \tag{8}
$$
每 $D^2$。这不是整个BC接口必须使用 $\limsup$ 的要求：逐个 $D$ 的slopes式也允许沿无界子列取得足够的upper；那时(8)信用只须沿该子列成立。无论统一或子列，(5)的 $\liminf$ lower都排除index-only证书。这里是条件性的剩余债务，不是已经取得的信用。安全源index率8相对(5)的最大raw节省至多 $341/84$；index-only所需节省超过 $14/3$，仍差至少 $17/28$。标量 $32/27$ 或 $8/9$ 没有参与这个实际下界。

## 3. balanced格相交不会自动吞掉全部信用

沿用263的 $E=E_{D,d,\varepsilon}\cong\mathbb Z^R$、完整cube评价矩阵、$\Gamma$、$g=M_{N_D}^{2d/3}$，故 $gE\subset\Gamma\subset E$。固定小 $\varepsilon$，先选 $\delta$，再 $d\gg_{\varepsilon,\delta}1$，最后 $D\to\infty$。

一变量实际jump集 $V_D$ 有 $3(D+1)$ 个点，全部在 $[0,N_D]$。CDT Corollary3.1.11（把其 degree $<D$ 换为 $\le D$）保证：原full tensor空间中的每个非零function，其全部最小总次数monomials都在 $V_D^d$。balanced source是这个空间的子空间，性质仍成立。

只对 $V_D^d$ 中不符合6.2.9分布，或 $\max n_j\le(3-\delta)D$ 的bad Taylor行施加零约束。设其有理核为 $W\subset E\otimes\mathbb Q$，$q=\operatorname{codim}W$，$S=E\cap W$。实际jump集相对完整长度 $3D$ 的区间只有 $O_f(1)$ 个缺项；所以CDT§6.3的计数同样给
$$
 q/R=o_{d,\varepsilon,\delta}(1)
 \tag{9}
$$
并随 $d$ 指数衰减。选择 $\delta$ 满足原(6.3.1)即可。$S$ 是饱和rank $r=R-q$ 子格。

令 $t=[E:\Gamma]$、$h=[S:S\cap\Gamma]$。exact quotient给
$$
 t=h[E:S+\Gamma],\qquad [E:S+\Gamma]\le g^q.
 \tag{10}
$$
后者因为 $E/S\cong\mathbb Z^q$、$S+\Gamma$ 含 $S+gE$。若完整source的信用是 $C_*=R\log g-\log t$，则
$$
 \boxed{C_*-q\log g
 \le r\log g-\log h\le C_*.}
 \tag{11}
$$
由(9)，263已证的 $dDR/96$ 保守信用确实在自然整数消去核中保留主量级。不能把“必须相交”本身当作全收益被取消的证明；这里也没有据此领取新净τ。

## 4. 在原monomial坐标中实际支付短向量

清掉有限bad-row分母后，$W=\ker A$，$A$ 为整数矩阵，rank $q$，最大entry $H_A\le\exp(C_f dD)$。理由：每个原coeff的分母与实绝对值均为 $\exp(O_f(N_D))$，tensor列清整 $g$ 及行height均为 $\exp(O_f(dD))$；$C_f$ 允许依赖固定关系，不依赖 $D,d$。

下面直接pigeonhole，不假设低height的CRT基。在整数box $\{0,\ldots,H\}^R$，同时记录coset $y\bmod\Gamma$ 和 $Ay$。记录数不超过
$$
 t(2RH_AH+1)^q.
$$
选 $H$ 使 $(H+1)^R$ 超过这个数，两点之差给原monomial坐标中的非零
$$
 P\in\Gamma\cap W,\qquad \|P\|_\infty\le H,
$$
且可取
$$
 \log H\le\frac{\log t+q\log(3RH_A)+O(R)}{R-q}.
 \tag{12}
$$
原full source评价单射保证 $F=\Psi(P)\ne0$；bad Taylor约束和最小monomial位于 $V_D^d$ 保证正确leading-cell。完整jet整性保证非零leading $\beta\in\mathbb Z\setminus\{0\}$，无需在cube以外断言全部coeff整。

263的安全率与保守信用给
$$
 \log t\le\left(\frac83-\frac1{96}+o_{d,\varepsilon}(1)\right)dDR
             +o_D(dDR).
$$
结合(9)、(12)，在先 $D$、再 $d$、最后 $\varepsilon$ 的结算顺序下，
$$
 \boxed{\log\|P\|_\infty
 \le\left(\frac{85}{32}+o(1)\right)dD.}
 \tag{13}
$$
这确实是一条leading-box桥。但它给的系数高度不是原Lemma6.2.6的 $\exp(\varepsilon dD)$。指数收益不能既保留原小box、又免费消去leading分母。

## 5. Cauchy预算与BC预算分开

在CDT§6.5原monomial/Cauchy证明的(6.5.14)中，(13)新增的项是 $\log\|P\|_\infty$。其它原生函数sup、共同pole清除与 $\log R$ 对固定 $d$ 都是 $o_D(dD)$；damping与rearrangement仍作用于原辅助degrees。以 $\alpha=3dD/2$ 归一化，source-height费为
$$
 \tau_{\rm box}=\frac23\frac{85}{32}=\frac{85}{48}.
 \tag{14}
$$
一图原§6.5解析项是
$$
 I_\phi=\iint_{\mathbb T^2}\log\max(|\phi(z)|,|\phi(w)|)\,d\mu(z)d\mu(w),
$$
不是BC的 $\mathcal J=\iint\log|\phi(z)-\phi(w)|$。对完整leading整数，(6.5.27)只给
$$
 0\le I_\phi/3-\lambda+85/48+o(1).
 \tag{15}
$$
由Jensen，$I_\phi\ge\lambda$。要从这个保守证书获得严格矛盾，至少必要 $85/48<2\lambda/3$，而同载体 $\lambda<\log3$；$\lambda\le0$ 的图本来也不能跨这个正费用门槛。显示upper证书远不足。**(14)不是最小可行系数高度的下界，也不是已经建立的BC τ。** §8.2的Hermitian/graded norm转换若要采用，须另付；没有通过换norm来保留旧度或旧能量。

## 6. 停止范围、复核与下一动作

本轮完成：实际最高rank envelope、完整单变量index下界及index-only BC排除；balanced消去核的exact信用界；原monomial box短向量与正确leading构造；Cauchy source-height成本。未付：原BC actual jump-minor的负graded费用、新的足够tensor预算、全部其它metrics或新周期源。

第二Smith层即使理想也救不了(6)的入口；(14)的保守信用不足以支持其有用性。因此本轮不计算β、不作素数/参数/地图/Padé扫描、不重跑旧producer、不新增Lean认证。相应无界纸证与范围本身改变下一行动：关闭263–264稳定窗口，下一轮作真实来源/负graded机制的宏观准入选择。重开须有满足(8)量级的新同对象统一或无界子列证明，或有独立预算的不同真实carrier/接口；不是改task名、重复Frobenius核或更大有限矩阵。

本轮主代理实际读：263评价格§§1–8、237 bridge B1–B14；固定CDT v2 locator的Corollary3.1.11及其证明、§§6.2–6.4、§6.5至(6.5.27)，另读261精化稿和262相关门槛。早期一次大批输出截断仅用于定位，不标全文读。外部只核[CDT arXiv v2](https://arxiv.org/pdf/2408.15403v2)为218页及作者公开入口，不重新下载或审计全篇。

rank envelope由方向代理独立提出，主代理独立重建多项式rank、五段区间与两份有理积分。交集与box桥由主代理、另一原文审阅者分别推得；该审阅者指出rearrangement与BC norm不可混认，本稿已按这个边界写明。保存后两位审阅者分别全文纸核(1)–(15)及范围，所提删尾正部和统一/子列量词已修正；未发现其它阻断问题。不继承历史FULL或Lean标签。状态、计数与当前任务由program.json维护。
