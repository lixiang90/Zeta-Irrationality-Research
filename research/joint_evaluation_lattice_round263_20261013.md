# 第263轮：实际截断评价格、Hasse核与完整Smith层

2026-10-13。固定第259–262轮普通坐标 $s$、反证类 $b=0,c=\pm d\ne0$与 $f=(1,J,\theta_sJ)$。本稿没有数值无理性定理。目的不是重开标量前缀排序，而是把剩余接口定义成明确的有限维整数格，并证明一个真实、随素数尺度增长的消去机制。未运行producer、CAS、有限素数/参数扫描或Lean；以下均为纸面恒等式与格论。

**结论先列清。** 特征零的period秩2不可约，不能排除模 $p$ 的Hasse核。下文证明它在一个完整Toeplitz评价矩阵中产生至少一层实际Smith收益；给出决定第二层的明确Bockstein商映射，并把第一层输送到原来的balanced/discrepancy tensor选列。所得是可验证的完整整jet格指数上界改善，尚不是新的CDT $\tau$，也没有跨过数值反证所需的净余量。

## 1. 真实source与所有参数下的有限矩阵

令 $J=C_0A(a+bB_3+cC_3+dB_4)$，其中固定 $C_0$清掉关系系数分母。仍有 $A\in1+s\mathbb Z[[s]]$、$s(q),q(s)$双向整数，且 $\{1,J,\theta_sJ\}$为实际 $\mathbb Q(s)$-独立、微分闭合的秩3系统。

对每个 $D,N\ge0$，定义
$$
 E_D=\mathbb Z[s]_{\le D}^{\oplus3},\qquad M=3(D+1),
$$
$$
 \Psi_D(P_0,P_1,P_2)=P_0+P_1J+P_2\theta_sJ,
 \qquad T_{D,N}P=([s^n]\Psi_D(P))_{0\le n\le N}.
\tag{1}
$$
在原始monomial source基 $(i,k)$, $0\le k\le D$, $i=0,1,2$上，矩阵为
$$
 (T_{D,N})_{n,(i,k)}=f_{i,n-k},\qquad f_{0,m}=1_{m=0},\quad f_{i,m}=0\ (m<0).
\tag{2}
$$
这是一个指定的 $(N+1)\times3(D+1)$ rational Toeplitz矩阵，包含常数块和全部输出系数。定义完整整jet逆像格
$$
 \Gamma_{D,N}=\{P\in E_D:T_{D,N}P\in\mathbb Z^{N+1}\}.
\tag{3}
$$
它对所有 $D,N$有定义并为有限指数格，因为262的 $M_N$清所有原函数的前缀。安全子格为
$$
 \Gamma^0_{D,N}=\mathbb Z[s]_{\le D}\oplus M_N\mathbb Z[s]_{\le D}^{\oplus2}
 \subset\Gamma_{D,N},
\quad [E_D:\Gamma^0_{D,N}]=M_N^{2(D+1)}.
\tag{4}
$$
不能将 $\Gamma$换成只清某个首项的格。

为进入完整vanishing-filtration桥，选固定的Shidlovsky常数 $C$，令
$$
 N_D=3(D+1)+C.
\tag{5}
$$
CDT Theorem3.2.8的实际微分闭合版本保证适当固定 $C$覆盖所有jumps，因此 $T_{D,N_D}$在特征零有列秩 $M$。本稿不计算有效 $C$，不把任意拍定的数字称为该常数；(1)–(4)不依赖这个零估计，只有完整slopes桥使用它。$C$依赖固定关系系数而不依赖 $D,p$。

## 2. 大素数下的完整最高packet

固定非坏素数 $p>\max(3,\sqrt N)$，故 $N<p^2$。令 $r=p\bmod12$，其首存活指数 $k_r$为262的1或3。261的完整divisor identities给
$$
 p^2J\equiv A(s)S_{r,p}(s^p),\qquad
 p^2\theta_sJ\equiv\theta_sA(s)S_{r,p}(s^p)
 \pmod{(p,s^{N+1})},
\tag{6}
$$
其中 $S_{r,p}(z)\in\mathbb F_p[[z]]$的阶恰为 $k_r$，首系数非零。整个范围内每个原Lambert系数最多含一次 $p$；整数换元给 $q(s)^p=q(s^p)\pmod p$，而 $\theta_s(S(s^p))=0\pmod p$。所以(6)是完整截断packet，不是仅在 $k_rp$处的一个系数见证。

记 $\kappa=k_rp$，则 $S_{r,p}(s^p)=s^\kappa$乘形式单位。模 $p$的正规化矩阵
$$
 B_{D,N,p}=p^2T_{D,N}\in M_{N+1,M}(\mathbb Z_p)
\tag{7}
$$
的常数source块为0，另两块正是
$$
 (P_1,P_2)\longmapsto
 s^\kappa\cdot\text{unit}\cdot(A P_1+\theta_sA P_2)
 \pmod{s^{N+1}}.
\tag{8}
$$
若 $\kappa>N$，261的全前缀消去已证明本截断 $J,\theta_sJ$在 $p$处整；该处无需付 $p^2$。不能把所有素数都当成活跃。

## 3. 一个实际Hasse有理行：粗度数 $h_p\le4p$

固定CDT v2 Lemma11.1.4明确给
$$
 A(t)=\sum_{n\ge0}a_nt^n,\qquad
 a_n=\sum_{j=0}^n\binom nj^2\binom{2j}{j}.
\tag{9}
$$
Lucas逐位分解证明 $a_{pn+m}\equiv a_na_m\pmod p$（$0\le m<p$）。若 $2j_0<p$，central binomial分成高低两位；若 $2j_0\ge p$，低位上标 $2j_0-p<j_0$，两边该项均为0。对 $j=pj_1+j_0$求和即得全部 $n,m$的身份，不需要测试素数。

因此，令 $H_p(t)=\sum_{m=0}^{p-1}a_mt^m$，有
$$
 A(t)=H_p(t)A(t^p)\pmod p,
 \qquad \theta_sA/A=\theta_s\log H_p(t(s))\pmod p.
\tag{10}
$$
用259的完整坐标
$$
 t(s)=T(s)/Q(s),\quad
 T=s(1-s)(1-2s+2s^2),\quad
 Q=(1-s+s^2)(1+2s-2s^2),
$$
两多项式次数均为4且 $Q(0)=1$。设
$$
 H_p^*(s)=Q(s)^{p-1}H_p(T/Q)\in\mathbb F_p[s],
 \quad \deg H_p^*\le4(p-1),\quad H_p^*(0)=1.
$$
由于 $-(p-1)=1\pmod p$，准确的有理logder为
$$
 \frac{\theta_sA}{A}=
 \frac{s(H_p^{*\prime}Q+H_p^*Q')}{H_p^*Q}
 =\frac{U_p}{V_p}\in\mathbb F_p(s),
\quad (U_p,V_p)=1,
\quad V_p(0)\ne0,
\quad h_p:=\max(\deg U_p,\deg V_p)\le4p.
\tag{11}
$$
这里取约分后的 $U_p,V_p$。本节自身的Lucas论证只需要粗界 $h_p\le4p$；同轮已独立复核的[support稿S3](joint_evaluation_support_round263_20261013.md)进一步证明 $H_p^*Q$平方自由、与其Euler导数互素且degree恰4p，所以本实际载体有 $h_p=4p$。以下保守指数估计只用粗界，不从它反推所有方法失败。

这使
$$
 A(-U_pR)+\theta_sA(V_pR)=0\pmod p,
 \qquad \deg R\le D-h_p.
\tag{12}
$$
产生 $s_p=(D-h_p+1)_+$个独立的真实period-source核方向。其系数依赖 $p$、度数随 $p$增长；它不是262关闭的固定有理换基。特征零不可约性不约束这个模 $p$核。

更准确地，若 $N-\kappa\ge D+h_p$且 $D\ge h_p$，(8)为0等价于多项式 $P_1V_p+P_2U_p$恒为0；该多项式次数不超过 $D+h_p$，其完整这么多前缀已被检查。coprime性给全部period核恰为(12)，因此
$$
 \operatorname{rank}_{\mathbb F_p}\overline B_{D,N,p}=D+h_p+1.
\tag{13}
$$
除此准确窗口外始终有
$$
 r_p:=\operatorname{rank}\overline B\le
 \min\{2(D+1),\,(N-\kappa+1)_+,\,2(D+1)-s_p\}.
\tag{14}
$$
最后一个界只用实际核，不要求(13)的完整度数条件。对于(5)且 $p\le D/4$，粗(11)保证准确窗口；大素数下的关系不存在“所有source均模 $p$注入”的障碍。

## 4. 前两Smith层：一个精确有限维kernel/quotient

设(7)的非零Smith指数为 $e_1,\ldots,e_M\ge0$；若截断尚无特征零满列秩，补上 $e_i=\infty$。定义
$$
 K_p=\ker\overline B\subset\mathbb F_p^M,
$$
$$
 \beta_p:K_p\longrightarrow
 \mathbb F_p^{N+1}/\operatorname{im}\overline B,
 \qquad \beta_p(u)=\left[B\widetilde u/p\pmod p\right].
\tag{15}
$$
任一 $p$-integral lift $\widetilde u$均可用；换lift加 $pv$只改变 $\overline Bv$，所以这个Bockstein映射是定义良好的线性映射。逐个Smith对角项核验得到
$$
 r_p=\#\{e_i=0\},\quad t_p:=\operatorname{rank}\beta_p=\#\{e_i=1\},
$$
$$
 \boxed{\log_p[E_D\otimes\mathbb Z_p:\Gamma_{D,N}\otimes\mathbb Z_p]
 =\sum_i(2-e_i)_+=2r_p+t_p.}
\tag{16}
$$
所以完整整jet指数并非两行prefix LCD的乘积；其前两Smith层可由一个具体有限矩阵及商映射严格决定。

常数source块在 $B$中为 $p^2I$，故其 $D+1$方向在 $K_p$中且 $\beta_p=0$。于是
$$
 t_p\le2(D+1)-r_p,
 \qquad 2r_p+t_p\le2(D+1)+r_p.
\tag{17}
$$
结合(14)，相对scalar $4(D+1)$费用，真正完整格的局部index上界至少节省 $s_p$。这是实际整数逆像格的upper改善，不是对实际费用作下界。

在准确窗口(13)，除了常数块，(15)的全部输入就是(12)。选择系数整数lift $\widetilde U_p,\widetilde V_p$，待计算的商Toeplitz映射可直接写为
$$
 R\longmapsto\left[
 p(\widetilde V_p\theta_sJ-\widetilde U_pJ)R\right]_{0,\ldots,N}
 \quad\bmod\operatorname{im}\overline B.
\tag{18}
$$
它在本截断是 $p$-integral。$t_p$就是这个map的rank，至多 $s_p$。其rank若小于 $s_p$，还产生第二层extra收益；若恰为 $s_p$，则这里只得到一层Hasse收益。必须有真实模 $p^2$ Frobenius/lift证书才能支付(18)，不能由(11)免费升级。只核一个首项、一个 $N$或几个 $p$不会给全尺度rank。

## 5. 单变量CRT整格的全尺度upper改进

保留全部小素数与全部prime powers的 $M_{N_D}$，在大素数窗口才应用(16)–(17)，所有有限坏素数照原费用付清。

特殊反证类有 $\log M_{N_D}=4D+o(D)$，所以(4)的scalar index为 $8D^2+o(D^2)$。先不使用Hasse，(14)的延迟支持本身给额外局部节省
$$
 (k_rp-D-O(1))_+\quad (p\le N_D/k_r).
$$
PNT_AP逐类积分给总节省
$$
 \frac14\sum_r\int_{D/k_r}^{3D/k_r}(k_ru-D)\,du
 =\frac43D^2+o(D^2).
\tag{19}
$$
它来自真正最高packet的延迟，不应包装成新Hasse结果。

粗Hasse窗口 $\sqrt{N_D}<p\le D/4$再至少节省 $D-4p+1$。该窗口与(19)不重叠，因为最小 $D/k_r$为 $D/3$。全部类共同的PNT给
$$
 \sum_{\sqrt{N_D}<p\le D/4}(D-4p+1)\log p
 =\frac18D^2+o(D^2).
\tag{20}
$$
故下列为一个实际CRT格指数upper证书：
$$
 \boxed{\limsup_{D\to\infty}\frac{\log[E_D:\Gamma_{D,N_D}]}{D^2}
 \le 8-\frac43-\frac18=\frac{157}{24}.}
\tag{21}
$$
这里未对同一素数重复领取两种kernel；未删除原小素数费用；未宣称指数upper等于实际指数。

237单变量完整joint-lattice/BC桥在其§1先陈述一般rank-m版本，不限旧源。将它作用于本对象时，必须重新核同metric、完整整jet、实际微分闭合/独立与零估计条件；本稿§§1、8与主代理对237§§1–4及原CDT3.2.8的复读核了这些条件，不借旧源参数或数值表。因此(21)给本粗模型有效费用upper $2(157/24)/9=157/108$。它比本节较粗的 $16/9$upper改善，仍比262自然balanced cap的 $32/27$更大。两种source/height结算不同，不能从较差upper声称自然AP费用反而增长，或把这份证书与262 cap直接相减。该粗证书尚未使 $\lambda<10/9$的严格数值反证可行；**这不是实际费用lower或全方法no-go。**

## 6. 明确的ALL-$D,d$ balanced评价格

为对应原CDT 6.2而不是只做 $d=1$，固定 $d\equiv0\pmod3$、$\varepsilon>0$。令
$$
 \mathcal I_{D,d,\varepsilon}=
 \{(\mathbf i,\mathbf k):\mathbf i\in V_3^d,
 \ \mathbf k\in\{0,\ldots,D\}^d,
 \ \mathbf k/D\in P_\varepsilon^d\},
$$
$$
 E_{D,d,\varepsilon}=\mathbb Z^{\mathcal I_{D,d,\varepsilon}},
 \quad R=|\mathcal I_{D,d,\varepsilon}|.
$$
source的第 $(\mathbf i,\mathbf k)$列为原生函数
$\prod_j s_j^{k_j}f_{i_j}(s_j)$。全部输出是 $\mathbf n\in\{0,\ldots,N_D\}^d$，明确评价矩阵为
$$
 (T_{D,d,\varepsilon})_{\mathbf n,(\mathbf i,\mathbf k)}
 =\prod_{j=1}^d f_{i_j,n_j-k_j}.
\tag{22}
$$
定义 $\Gamma_{D,d,\varepsilon}=T^{-1}(\mathbb Z^{(N_D+1)^d})\cap E$。这包含全部合法coefficients、labels与辅助degrees，并检查完整jet立方体。每列有恰 $2d/3$个非恒定species，故
$$
 g=M_{N_D}^{2d/3},\qquad gE\subset\Gamma\subset E,
 \qquad gT\text{ 为integer矩阵}.
\tag{23}
$$
对任意素数 $p$，设 $b_p=v_p(g)$，$e_j^{\rm bal}$为 $gT$的Smith指数，则精确地
$$
 \log_p[E\otimes\mathbb Z_p:\Gamma\otimes\mathbb Z_p]
 =\sum_{j=1}^{R}(b_p-e_j^{\rm bal})_+.
\tag{24}
$$
这就是有全部 $D,d$参数的实际联合CRT格，不是“可能存在gcd”的抽象愿望。它还没有要求source消去全部非leading Taylor系数；要进入CDT的box construction，必须另与6.3的消去子空间相交。

## 7. 第一Smith层确能传到balanced tensor，而非免费丢弃支持

定义一变量全整化矩阵
$$
 W_D=T_{D,N_D}\operatorname{diag}(I_{D+1},M_{N_D}I_{D+1},M_{N_D}I_{D+1}).
$$
它在所有素数处整。在 $p>\sqrt{N_D}$、$p\le D/8$处，$v_p(M_{N_D})=2$，(12)仍给 $s\ge D-4p+1$个模 $p$核方向，所以其 $M$个Smith指数至少 $s$个为正，且 $s/M\ge1/6$。

全tensor $W_D^{\otimes d}$的Smith指数是所有 $d$个一变量指数之和。若 $c_\ell$为指数小于 $\ell$的数量，忽略更深层即可得有限计数界
$$
 c_\ell\le\sum_{j=0}^{\ell-1}\binom dj s^j(M-s)^{d-j}.
\tag{25}
$$
由于恰有 $2d/3$个非恒定labels，(23)的 $gT$正是全tensor的 $\mathcal I$选列。任何该选列矩阵在模 $p^\ell$下的image都是全image的submodule。有限DVR模的最少生成元数等于其 $p$-torsion维数，submodule的这个维数不超过全image。因此
$$
 \#\{e_j^{\rm bal}<\ell\}\le c_\ell.
\tag{26}
$$
这没有假设Hasse多项式multiples逐项维持discrepancy，也没有将特征零monomial basis随意换成别的低height basis；它是同一有限矩阵的选列Smith比较。

还须明确 $p$-饱和后的source仍是原整数source。对(23)有 $g=p^{b_p}$乘 $p$-单位，且本窗口 $b_p=4d/3$。选取 $gT$的 $\mathbb Z_p$-unimodular Smith source基 $v_j$。令 $m_j=\min(e_j^{\rm bal},b_p)$，则
$$
 P_j=g p^{-m_j}v_j\in E\otimes\mathbb Z_p,
 \qquad T(P_j)=p^{-m_j}(gT)v_j\in\mathbb Z_p^{(N_D+1)^d}.
$$
前一整性由 $m_j\le b_p$保证，后一整性由 $m_j\le e_j^{\rm bal}$保证。特别是领取 $\ell=\lfloor d/12\rfloor$层时 $\ell<b_p$，所以不会以给原source引入 $p$分母为代价。其他素数处保留原source的全整性；(3)/(24)的有限模数同余条件经CRT给真正全局整数逆像格。这里没有声称这些CRT基在实处有小范数，那个费用仍在§8支付。

取 $\ell=\lfloor d/12\rfloor$。用 $2^{-j}$的初等Markov界，(25)给
$$
 c_\ell/M^d\le\left(2^{1/12}\frac{11}{12}\right)^d=:\eta^d,
 \qquad \eta<1.
\tag{27}
$$
最后一个严格比较可由 $(12/11)^{12}>1+12/11>2$核验。另一方面，CDT Lemma6.2.4和(6.2.2)给，对固定 $\varepsilon$、先 $D\to\infty$再 $d\to\infty$，$R/M^d$只损失poly$(d)$与趋1的discrepancy概率，不是指数损失。因此 $c_\ell/R\to0$。几乎全部balanced-source的Smith指数至少 $d/12$，在(24)中领取的是 $\min(e_j^{\rm bal},b_p)$，而本窗口 $b_p=4d/3>d/12$。

于是这个**完整整jet格**相对于(23)的安全scalar源，已有全尺度指数upper节省
$$
 \log[E:gE]-\log[E:\Gamma]
 \ge\left(\frac1{96}-o_{d,\varepsilon}(1)\right)dDR+o_D(dDR).
\tag{28}
$$
其因子来自 $(d/12)R$乘 $\sum_{\sqrt{N_D}<p\le D/8}\log p\sim D/8$。这是保守窗口；没有最优化 $p$、degree或参数。所有小素数仍用(23)支付。

对当前 $\gamma=4/3$，安全源的 $\log[E:gE]/(dDR)\to8/3$，故(28)给实际balanced格指数upper至少减 $1/96$。此归一化是**整source index每 $dDR$**，不能把 $8/3-1/96$称成262的 $\tau$，也不能与 $\tau<20/27$直接比较。

## 8. 必须支付的source index、metric和真实leading filtration

格变换不是免费的。若 $L=E_{D,d,\varepsilon}$使用原来的实处tensor/BC或6.5 source metric，$\Gamma\subset L$仅限制同一norm，则
$$
 \widehat{\deg}\Gamma=\widehat{\deg}L-\log[L:\Gamma].
\tag{29}
$$
CRT/HNF基的坐标即使很大，也不能另声称它有免费低height；其covolume已在(29)中记账。若使用coefficient sup-norm box principle，要重建该source格与6.3消去约束交的体积及短向量估计，而不是换norm后继续用旧degree。

同一rational vanishing filtration的graded lattice指数与source指数逐层相乘；精确finite graded heights减少的 $\log[L:\Gamma]$和(29)的degree损失相抵。这是237完整bridge已证明的恒等式。改善整化格index给的是同一个intrinsic费用的更好upper，不能说仅改变格便降低了其真实值。

对单变量完整jump集 $V_D$，native jump-minor $T_{V_D}$满足
$$
 \mathcal A_D=\sum_{n\in V_D}h_{\rm fin}(\psi_L^{(n)})
 =-\log|\det T_{V_D}|,
\tag{30}
$$
而完整jet整数化只给 $\mathcal A_D\le\log[L:\Gamma]$。262的 $32/27$、$8/9$是worst-case coefficient-prefix cap；本稿(16)、(24)是完整evaluation-image的指数；(30)才是原metric下实际jump的精确累计费用。三者不应混称。

此外，CDT 6.3要求辅助function的全部minimal monomials具有6.2的正确 $\mathbf n$分布。整jet CRT格本身不保证其非零leading项落在正确cell，也不保证 $e^{\varepsilon dD}$的原系数box仍容纳新source的非零解。(28)已经跨过“balanced选列可能破坏kernel”的第一障碍，但没有付完这个leading-box桥和同一archimedean高度估计。

## 9. 下一首证书、停止条件和读域

本轮机制是真实scale-dependent Hasse核，不由262固定换基停止结论排除。但下一轮不以局部kernel数量为投入依据，唯一优先关应是**足够净预算的匹配桥**：将(24)–(28)与原6.3的完整消去source交，证明正确minimal jet仍有足够的短整向量，并将source指数、native/target norm及arch energy同时转成适用判据。只复制原leading-coefficient LCD estimate不够，$dDR/96$也不能直接领取成 $1/144$或其它 $\tau$节省。

只有这个桥先指出真正需要的额外量，并证明它可改变同对象严格净余量时，才把(18)的**第二Smith层**选为有界子命题：在明确 $D/p,N/p$窗口，用真实模 $p^2$ period/Frobenius lift证明Bockstein的rank bound，且立即结算它在完整index或native jump-minor上的贡献。证明Bockstein满秩只关闭该层、该窗口，不升级为全方法no-go；新一个模 $p$引理本身不延长研究窗口。

若下一稿只重新证明(12)，或只报告一份较小HNF/index而没有足够净预算桥，就没有缩小剩余缺口，不进入prime/参数扫描。当前粗证书不足以认证新的数值反证；它也未证明真实宏观费用下界，不能据此终止全部联合评价格方法。

实际本轮读取：262 AP稿当前全文、262总稿与本人的262carrier稿；固定CDT v2本地locator的3.2.8–3.2.13、6.2.1–6.2.15及6.3开头、6.6.1–6.6.16、11.1.4及其明确binomial formula；237 metric bridge全文，261 arithmetic稿R1–R6。没有全文读取218页CDT、没有重新核全部上游证明。本稿(9)–(12)的Lucas/Hasse粗度数、(15)–(18)的精确Smith/Bockstein及(25)–(28)的选列计数为本轮自证，待独立审阅；hash或旧PASS不替代该审阅。

来源入口：[固定CDT locator](../literature/trace_sources_round221_20261008/cdt_fixed_v2_locator.txt)、[262 AP审查](next_route_ap_cost_20261012.md)、[261实际packet](refined_budget_arithmetic_round261_20261010.md)、[259完整坐标](source_selection_mixed_field_round259_20261010.md)、[237同metric bridge](joint_lattice_metric_bridge_round237_20261008.md)。

保存后，主代理与另一独立审阅者全文纸核本稿的局部Smith/Bockstein、延迟与Hasse积分、tensor低深度计数、选列image比较、原整数source饱和及CRT指数，未发现阻断问题。粗/sharp degree文字按support稿统一；该数学复核不替代完整leading-box净预算桥，也不继承作者的原文FULL或Lean标签。
