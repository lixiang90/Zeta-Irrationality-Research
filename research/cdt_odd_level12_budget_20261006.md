# D12 的真实秩4数域预算：完整分母下界与所需折扣

日期：2026-10-06。本文新建；不修改、import 或执行任何既有 producer。输入是 [真实共轭坐标稿](cdt_odd_level12_paired_coordinate_20261006.md) 的全阶整数反演、实际秩4及完整安全算术，以及 [固定纯L源的完整分母与Hecke证明](cdt_odd_level12_source_denominators_20261006.md)。本文给出可检验的必要预算，§9引用随后已完成的真实fullleaf，将先前条件性解析上限升级到该指定地图类。没有证明 L(3,χ12) 无理。两 embedding 的实际函数使用各自的 t 坐标；不能把两个地图自动变成一个秩7系统，也不将纯L源的结论搬给另一个joint source。

## 1. 原文接口、秩和两 embedding

原件为 [CDT 固定218页版本](../literature/cdt2024_l2_chi_minus3.pdf)。本文实际只读 Definition6.0.1 / Theorem6.0.2 / (6.0.4)–(6.0.5)，PDF p66；Theorem8.0.1 / Remark8.0.6，pp122–124；Remark8.2.41–42，p143；Carathéodory 条件，p24。原文任意非负矩阵使用 τflatflat；只有嵌套单位列等原 standing 类型才可直接用加权行和。

令 r=√3，K=Q(r)，O_K=Z[r]。在反证假设 L(3,χ12)∈Q 下，真实源和坐标给

\[
H=H_-(q(t_-))\in K[[t]],\qquad
\sigma H=H_\sigma(q(t_+)),\quad \sigma r=-r.
\tag{D1}
\]

令 θ=t d/dt。实际闭合系统可取

\[
\mathcal W=\langle1,H,\theta H,\theta^2H\rangle_{K(t)},
\qquad \dim_{K(t)}\mathcal W=4.
\tag{D2}
\]

理由不仅是某个四阶 ODE：真实三阶 Bol 算子满足 L3H=R∈K(t)、R≠0，故1在导数闭包内；未消 cusp 的非零 cubic log 强迫最小齐次阶数4。因此(D2)的四行实际独立。两个 embedding 分别应用同一个 K(t) 秩4；数域扩张或换成两张地图不增加这个 m。

采用与原文相同的可在单位圆附近定义的地图 φ±，并设

\[
\rho_\pm=\log|\phi_\pm'(0)|,\quad
J_\pm=\iint_{\mathbb T^2}\log|\phi_\pm(z)-\phi_\pm(w)|\,d\mu(z)d\mu(w),
\quad \bar\rho=(\rho_-+\rho_+)/2,\quad \bar J=(J_-+J_+)/2.
\tag{D3}
\]

所有实际芽及使用的导数都必须沿相应地图全纯；若只获得 meromorphic pullbacks，需要先给一个固定 K[t] 因子清全部实际 poles。当前 compact quotient 计算没有完成这些解析条件。这里不从代数坐标表自动认证 φ±。

原文 Remark8.2.42 的字面陈述在平均ρ>σ_m时自动推出 holonomicity。对于已经实际微分闭合的系统，可用 Remark8.2.41 的 Shidlovsky 分支，保留平均ρ>τ即可：其数域闭合版本的证明已写在 [已审算术稿§6](cdt_odd_level20_arithmetic_20261006.md)。K 的 Arakelov degree 先除 [K:Q]；同一个有理 LCM 在有限 places 的总权仍为1，archimedean 两边取平均。因此合法预算是

\[
 m(\bar\rho-\tau)\le\bar J,
\tag{D4}
\]

不是把 m 换成8或7，也不是把两 embedding 的解析收益相加而不平均。若加入 e_i>0，必须计入原文完整 τsharp；若想扣局部 Smith 信用，还要保留同一个 cutoff ξ 及完整张量接口。

## 2. 全阶安全模型和 bare 成本

令 D_n=lcm(1,…,n)。由全阶整数 t±(q)、q(t±)，反证假设中的一个固定整数 C 清 Θ 的分母后，所有 n 和两个 embedding 有

\[
C D_n^3 [H]_n\in O_K.
\tag{D5}
\]

Euler 导数只乘 n、n²，因此同一(D5)也适用于 θH、θ²H；这里不把普通导数造成的 index shift 当成免费降低成本。bare 完整矩阵为

\[
b=\begin{pmatrix}0&0&0\\1&1&1\\1&1&1\\1&1&1\end{pmatrix},\qquad e=(0,0,0,0).
\tag{D6}
\]

每列 zero-prefix 长度1，故原文 Remark8.0.6 给精确值

\[
\tau^{\flat\flat}=\tau^\flat
=\frac{3(3+5+7)}{16}=\frac{45}{16},\qquad \tau^\sharp=0.
\tag{D7}
\]

这不是某个数值 transport 的近似。下面进一步证明，对这三条 native Euler 行，任意固定 componentwise LCM / n^e 型都不能把(D7)降低。这个结论不涉及混合整格。

## 3. p+1 主部：natural 分母数组的严格下界

使用真实源的 literal Lambert 系数。对 p≥5、p∤12，记 ε=χ12(p)。只有 ordinary oldscale j=1 在 prime p 有非零正系数。由

\[
E_{4,p}=240(1+p^3),\quad E_{\chi,p}=1+\varepsilon p^3,
\quad F_{\chi,p}=\varepsilon+p^3
\]

准确得到

\[
F_{-,p}=u_\varepsilon+p^3 v_\varepsilon,
\quad u_\varepsilon=294960-69120r\varepsilon=240(1229-288r\varepsilon),
\quad v_\varepsilon=292080+2880\varepsilon-69120r.
\tag{D8}
\]

两 ε 的代数 norm 相同：

\[
\operatorname{Norm}(1229-288r\varepsilon)=1261609,
\qquad\operatorname{Norm}(u_\varepsilon)=72668678400\ne0.
\tag{D9}
\]

因此排除固定 Θ 分母和(D9)的有限 primes 后，uε 在 p 上每个好 place 都是 unit。不需要对 χ(p) 的两类采用密度假设。

写 B=E2−12E2(12τ)，则 B0=−11、B1=−24，H_q=B(f−Θ)。对 n<p，所有系数 p-integral；在 p 和 p+1，仅 f_p=F_p/p³能产生三层分母。故

\[
p^3[H_q]_p\equiv-11u_\varepsilon,
\qquad p^3[H_q]_{p+1}\equiv-24u_\varepsilon\pmod{\mathfrak p}.
\tag{D10}
\]

第一式再排除 p=11。第二式只额外排除2、3，因 p+1不是 p 的倍数而特别适合核序号成本。反演 q=t+a2t²+… 有 O_K 整系数。由

\[
[t^p]q(t)^p=1,\qquad[t^{p+1}]q(t)^p=p a_2
\]

及 n<p 的 p-integrality，得到同一 p+1 主部

\[
p^3[H(t)]_{p+1}\equiv-24u_\varepsilon,
\quad p^3[\theta^jH(t)]_{p+1}\equiv-24u_\varepsilon
\quad(j=0,1,2)\pmod{\mathfrak p}.
\tag{D11}
\]

第二个等式用了 (p+1)^j≡1；另一 embedding 是(D8)–(D11)的真正系数共轭，norm 仍相同。这里没有误把 K 系数反演的 Frobenius 当成逐系数不变；所需计算只用 leading1 和整数性。

先取每条 H 的完整 prefix 清分母的最小正有理整数 δ(N)。由(D10)第一式，δ(N)被所有好 p≤N 的 p³整除；(D5)是上界。素数定理遂给

\[
\log\delta(N)=3N+o(N).
\tag{D12}
\]

所以“单条函数完整 prefix 的指数3”是必要的。它不意味着真实系数逐项恒有三层，也不禁止适配 p 的格。

更强地，若某条 native 行存在固定安全型

\[
C_i n^{e_i}\prod_{h=1}^sD_{\lfloor b_{i,h}n\rfloor},
\quad e_i\in\mathbb Z_{\ge0},\quad b_{i,h}\in\mathbb R_{\ge0},
\tag{D13}
\]

则取 n=p+1。n^e_i是 unit；固定 b 对充分大 p 每个 LCM 因子的 valuation 至多1，且 b<1 的列最终完全没有 p 层。由(D11)，每条目标行必有至少三列 b_i,h≥1。固定 C_i 只排有限 primes。

原文(8.0.2)对同一行内部的列排列不敏感，因为只数 active 列的个数。将每条目标行的三个 b≥1列移到前三列后，整个数组 componentwise 支配(D6)；τflatflat 对 b 单调，τsharp非负。因此

\[
\boxed{\tau^{\flat\flat}(b)+\tau^\sharp(e)\ge45/16}
\tag{D14}
\]

对(D2)这三条 natural Euler 行的全部有限固定类型(D13)成立。不应把这个结论推广成“任意换基、任意混合格和整个函数包都需要同一成本”。例如把实际 packet 分成不同 prime-dependent lattice directions，正是(D14)没有处理的路线。

## 4. 两真源的 Hecke identity/swap 与 scope

把实际 source 写成 F−=U+E+Y，其中 U 是全部 trivial oldscales，E=2880Eχ，Y=−69120rFχ。U_p 表示 coefficient extraction。Lambert divisor recurrence 给全 q identity

\[
U_p F_- =R_\varepsilon+p^3S_\varepsilon-p^3V_pT_\varepsilon,
\]
\[
R_\varepsilon=U+E+\varepsilon Y,\quad
S_\varepsilon=U+\varepsilon E+Y,\quad
T_\varepsilon=U+\varepsilon E+\varepsilon Y.
\tag{D15}
\]

具体是 U_pU=(1+p³)U−p³V_pU、U_pE=(1+εp³)E−εp³V_pE、U_pY=(ε+p³)Y−εp³V_pY。该式也含常数项；真实 source 的∞constant为0。因此在 span{F−,σF−} 上，U_p mod p³ 是 ε=+1时 identity、ε=−1时 swap，行列式分别为+1、−1。这里须另排两源 reduction 相关的有限坏 primes；实际前两项矩阵 determinant=429616742400r≠0，正如 source_denominators §4 所证明，所以排该 norm 后源层确为二维。

这是与 level20 cuspidal-source 包不同的一个具体机制，但没有证明 native slow3×3、较大 Cartier 矩阵或 polynomial source 的 injectivity。必须保留实际 gauge、coordinate 和完整 carrier，再把 Hecke 源空间接口接到 Cartier/cohomology。不能从这二维 source span 的可逆性直接宣称没有 mixed Smith 收益。

## 5. Jensen 给严格必要尺度；容量上界的条件

对每个合法 φ，固定 w 后 Jensen 给

\[
\int_{\mathbb T}\log|\phi(z)-\phi(w)|\,d\mu(z)\ge\log|\phi(w)|,
\quad \int_{\mathbb T}\log|\phi(w)|\,d\mu(w)\ge\rho.
\]

故 J±≥ρ±，平均后 \bar J≥\barρ。要让(D4)的上界严格小于 m，必须

\[
\bar\rho>\frac{m}{m-1}\tau.
\tag{D16}
\]

bare m4 因而要求

\[
\boxed{\bar\rho>15/4.}
\tag{D17}
\]

只满足 \barρ>45/16还不够；忽略 J 的门槛会把可行性高估。本文(D16)针对原 Bost–Charles numerator；标准 convexity 若要采用同一 floor，另引用 [已审 convexity 稿](cdt_odd_level20_convexity_20261006.md) 的具体合法范围，不在这里把所有可能 metric、多地图或任意 raw 参数一并排除。

CDT p24 的 Carathéodory 上界要求 φ:D→C\{a}、a≠0且 φ⁻¹(0)={0}，按 a 缩放得到 |φ′0|≤16|a|。D12 compact 坐标已给成对 finite cusp 值

\[
a_-=2+r,\quad a_+=2-r,\quad a_-a_+=1;
\]
\[
b_-=\frac{2+r\pm i}{2},\quad b_+=\frac{2-r\pm i}{2},
\quad |b_-b_+|=1.
\tag{D18}
\]

所以**若未来两张实际合法地图分别具有唯一零点，并各省略一对(D18)的匹配值**，严格平均上限是

\[
\bar\rho\le\log16.
\tag{D19}
\]

加入仅在0、1有 singularities 的辅助函数，并要求两图都省去1且各自 unique-zero，也给同样条件性(D19)。但当前实际坐标稿没有证明 full leaf、全部 interior fibers、unique-zero 或所需 omissions。仅有 genus0、compact cusp 值和局部 period 消除，不足以无条件认证(D19)。因此本文不宣称当前所有 D12 解析方法的容量都至多 log16。

在(D19)的指定地图类中，bare natural 成本甚至有 log16<45/16，更不满足(D17)。全局无理性证明需要改变合法成本包或改变这组解析 standing conditions，而不是仅改善一个 Taylor 半径估计。

## 6. 可证明实际增秩的几个固定背景账本

这节只给具体安全账本，既不扫描背景也不声称最优。实际 D12 homogeneous quotient 的 monodromy 是由 B、τB、τ²B 变换得到的 Sym²标准 Γ 表示（或其对偶）；Γ是SL2(Z)有限指数群，Zariski closure 是SL2。因此商不可约且 rank3。它的实际 quotient identification 来自 minimal L3，而不是把三个 homogeneous solutions 免费加到 H tuple。

取 [完整低成本背景](cdt_odd_low_cost_polylog_20261006.md) 的正则芽

\[
L=-\log(1-t),\quad T_2=L^2/2,\quad
K_2=\frac1{\sqrt{1-t}}\int_0^t\frac{L(u)}{u\sqrt{1-u}}\,du,
\quad I_K=\int_0^tK_2(u)\,du/u.
\]

实际背景闭包分别为(1,L)、(1,L,K2)、(1,L,T2,K2)、(1,L,T2,K2,IK)，秩2、3、4、5。它们只含 trivial/sign 的一维 composition factors；K2 的 genuine sign factor不在纯log系统里，IK额外方向由 r′+r/[2(1−t)]=1/t无有理解证明。不可约 rank3 quotient 迫它们与 \mathcal W 的交恰为常数1，所以合并实际秩分别为5、6、7、8。这是作用于实际函数的 differential-module 证明，不是 formal ODE solution 数目。

|完整实际 tuple|固定安全 row sums σ|E / emax|τ|Jensen 必要平均ρ|
|---|---|---|---|---|
|bare，m4|(0,3,3,3)|0 / 0|45/16|15/4|
|加L，m5|(0,1,3,3,3)|0 / 0|66/25|33/10|
|加L,K2，m6|(0,1,2,3,3,3)|0 / 0|47/18|47/15|
|加L,T2,K2，m7|(0,1,2,2,3,3,3)|0 / 0|18/7|3|
|再加IK，m8|(0,1,2,2,2,3,3,3)|1 / 1|177/64|177/56|

单位嵌套列是合法精确 flat 表；T2 这里用固定2D_n²的粗安全型，未使用较细半尺度。IK 使用 nD_n²，因此 m8 flat=81/32而不是全部成本。Definition6.0.1 给 min(ξ+I8(ξ))=15/2，在 ξ∈[4,7]达到，故 sharp=15/64、完整τ=177/64。该精确分段推导已写在 [积分张量稿§5](cdt_odd_level20_integrated_tensor_bridge_20261006.md)，这里没有运行该 producer。

以上所有必要尺度都大于 log16。它们还要求**同一对地图**解析化目标和全部背景；IK遇其它 φ-zero时的 branch 积分也必须核查，unique-zero是一个安全条件。新增函数的成本和新增 singularities均不可省略。表格排除的是这些指定安全账本在(D19)地图类中的 plain holonomy rank 矛盾，不排更精细数组或其它实际辅助函数。

## 7. 什么程度的 Hasse/Smith 折扣才可能有效

设未来真正证明固定原格累计 gain γ，并把它接到实际 near-balanced tensor、leading flag 和同一有限高度 baseline。已审 [balanced 接口](cdt_odd_level20_balanced_smith_bridge_20261006.md) 的归一是有限高度扣 γ/m，最终成本扣2γ/m²。不能把一变量 effective cost直接代入第八节，也不能只改变 source degree而漏掉换格 index。

对 bare m4，合法接通后的条件式才是

\[
\tau_{\rm eff}=45/16-\gamma/8,
\qquad \bar\rho>15/4-\gamma/6.
\tag{D20}
\]

若未来已证容量上限为 C，则必要信用是

\[
\boxed{\gamma>45/2-6C.}
\tag{D21}
\]

在(D19)类 C=log16 时，右边约5.8644677。即使条件性赠予旧 level20 的 γ=5/6，bare cost只变成65/24、必要平均ρ仍为65/18。**本文不把旧5/6输入转移给D12。** Γ的PSL index为48；W和M quotient各为24，不是level20旧表的18。Hasse divisor、polynomial degree、excellent Frobenius、primitive行、完整 source packet和全局 tensor匹配均须对当前 source重证。

可检查的 degree 接口是：若另证每个好 prime 上 S1 数量至少2(D−c1p+O(1))_+、S2 数量至少(D−c2p+O(1))_+，其中 c1,c2>0，在同一 matching窗口 p≤aD内，则

\[
\gamma(a)=2\int_0^{\min(a,1/c_1)}(1-c_1x)dx
 +\int_0^{\min(a,1/c_2)}(1-c_2x)dx.
\tag{D22}
\]

饱和上限为1/c1+1/(2c2)。例如若一个**另待证明**的D12构造仅给 degree~2p与~4p，则即使完全接通并饱和，γ=5/8；bare cost175/64、必要平均ρ175/48，仍远高于log16。这个例子没有从index24自动推出某个单零weight2form或相应 Hasse polynomial。

同一 bare 原格、仅支持三个目标 species、p≤aD≤D且Smith信用只截到三层时，还可给极乐观 ceiling：每条目标 source的baseline floor为0，至多给3层；三个 species合计额外最多9(D+1)每prime。故该指定窗口的总 gain 至多9a，且已包括一切互相重叠的三层信用，不能再加另一份 γ。因此要跨(D19)，即使把所有这些 capped层全部赠予，也须 a>(45/2−6log16)/9≈0.6516075。这个 ceiling仍大于(D21)的所需量，不能据此证明方法不可能。它不处理background mixed支持、窗口之外、高于三层的Smith exponents或新格。

## 8. 下一步需要的实际输入与审阅范围

本文初始账本所列的解析缺口——两张实际 filled leaves及合法盘地图、native导数的pole清因子、zeros与omissions——已由下节列明的新输入完成。剩余解析缺口是计算或严格估计这对地图的实际 \barρ和\bar J，而不仅是给上限。并行算术缺口是：把(D15)的 source identity/swap接到有固定degree控制的真实 Cartier/cohomology矩阵，研究能否获得足够大、且超出原baseline的 primitive Smith thresholds。完整prefix率3和(D14)不排这条函数包路线。

本文实际只读审阅 paired-coordinate §§2–4和§6，核character cover/Q(v)、W正号、共轭pair、整数反演与actual rank4；未运行其76check producer。作者已将 cusp规范澄清为 −36160/27 是(2πiτc)³系数，width6 local log q_c³系数为−289280；两者非零，秩证明不受影响。本文也只读列明CDT原件、旧算术/背景/积分接口，不重新执行任何冻结证书。

本文也已实际只读 source_denominators §§1–4，核(D8)–(D11)、norm、完整prefix率、Euler行的固定列下界及全q Hecke identity/swap；未运行其 source-family producer，也未外推另一源。

本文(D8)–(D14)是 literal coefficient、全阶整反演和素数定理给出的全尺度证明；[新独立算术脚本](cdt_odd_level12_budget_20261006_verify.py)及[固定JSON](cdt_odd_level12_budget_20261006_verify.json)由作者执行一次，27项固定精确检查全部通过。它只核数字、五个固定账本与γ归一，不读取任何旧producer，也不替代全尺度论证。没有新数值无理性或线性无关性定理，没有声称全方法 no-go，没有Lean认证。

## 9. 实际fullleaf输入：合法gauge与更强平均cap

本文实际只读 [新fullleaf稿](cdt_odd_level12_full_leaf_20261006.md) §§5–7，限定审阅通过：全部10cusps、cubic carriers、两个Hecke群的filled disk、unique-zero、所有nonzero cusp omissions，以及fixed polynomial清极点。未运行其77check producer，未独立重算§§3–4的37/139 Bernoulli endpoints，也未据此求实际radius或J。

取 aδ=2+δr，对应两embedding，令

\[
g_\delta(t)=(1-4a_\delta t+4t^2)^2\in O_K[t],\qquad
g_\delta(0)=1,\quad[g_\delta]_1=-8a_\delta.
\tag{D23}
\]

实际filled source是 <T,W> 和 <T,M> 的coarse quotient各自填唯一q cusp。原生H在上半平面全纯且对对应真实group不变。非canonical Γ fibers保留为ordinary source points；t有ramification2时∂t²H最多w^-3，g有w^4，故

\[
1,g_\delta H_\delta,g_\delta\theta H_\delta,
g_\delta\theta^2H_\delta
\tag{D24}
\]

全在该source盘上全纯。σg+=g−；固定degree4与整系数不加新LCM费用，同一非零gauge不改变实际rank4或微分闭包。

bare列下界还可延伸到这个真正解析合法的(D24)。由(D10)–(D11)，

\[
p^3[g_\delta H_\delta]_{p+1}
\equiv(88a_\delta-24)u_\varepsilon,
\quad\operatorname{Norm}(88a_\delta-24)
=\operatorname{Norm}(152+88\delta r)=-128,
\]
\[
p^3[g_\delta\theta^jH_\delta]_{p+1}
\equiv-24u_\varepsilon\quad(j=1,2)\pmod{\mathfrak p}.
\tag{D25}
\]

后一式中来自degree1 gauge系数的项为 p^j[H]_p，模p主部为0。故三个合法target行对好p仍有完整三层，(D14)的固定componentwise数组下界仍是45/16。

actual地图的全部nonzero cuspimages省略已证，而不是仅任选一对省略值。第一embedding的最小模长是|b−|=√(2+r)，第二embedding是a+=2−r。因此

\[
\boxed{\bar\rho\le C_*:=\log16-\tfrac14\log(2+r).}
\tag{D26}
\]

数值约2.44334925。它适用于实际t±和这些filled leaves（或保持同一omissions/unique-zero的限制地图），不是任意source、任意坐标或全部数学方法的上限。把unit Möbius改写后的较弱平均cap log16当成新收益是错误的，因为origin derivative仍为1、原t仍可用(D26)。

若只改(D24)的target原格且新信用限于matching≤D、三target支持和三层cap，(D21)加强为

\[
\gamma>45/2-6\log16+(3/2)\log(2+r)
\quad(\text{约 }7.83990451).
\tag{D27}
\]

同支持/窗口的极乐观 ceiling仍是9a，因此a至少须超过(D27)右边除9；这仍没有排除bare整格路线。旧§6五张固定账本当然继续不够。相同限制下m7单位背景账本所需γ>63−21C*约11.68967，已经超过9；这一小scope的失败不能推广到unit背景参与混合、额外Smith层、窗口外收益或更细辅助数组。

反过来，新的actual cusp-log polynomial背景能改变账本，不受上述指定旧表的排除。它另记于新的cheap-log报告，须使用原文任意矩阵τflatflat的安全估计，不把多positive-level列的加权行和自动当成等号。

独立限定审阅：root实际全文及新PY通过§§1–8的预算、field归一和componentwise scope，并随后实际完整只读本§9，通过g1主部、Norm−128、fullleaf输入和C*范围；low_period_closure实际只读§§6–7，通过helper交与五张固定成本、IK sharp和2γ/m²归一。两位均未执行本文producer。新增本节的fullleaf与gauge范围由列明实际输入及上述正文审阅承担；27项证书不扩张为本节新全尺度证明。本文三件在记录该范围后冻结，不再运行producer；后续新的背景或成本优化另建数学输入。
