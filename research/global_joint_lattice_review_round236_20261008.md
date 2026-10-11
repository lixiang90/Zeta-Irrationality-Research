# 第236轮全局复盘：完整源联合整格已有一个可认证的起步窗口

2026-10-08，Packet/B。建议**有界重构一次，先付整格到实际过滤源的桥，不恢复固定基/图/素数参数扫描**。235已经关闭的算术模板不能改名恢复；本轮给一个新的完整prime-jet rank、完整CRT整模型及已读原文允许的准确接口。尚无新的数值无理性/线性无关性定理，数学程序0。

## 1. 当前门槛与真正未被排除的对象

实际FULL只读235算术最终稿8633 B / SHA256 2ff4e12e1965d03b49df9f2b201a955aa1b8449ea051b03580087b535c424d23。固定g∈Q、固定u，令

\[
f=(1,uE,b_gJ_g),\quad
E=\sum_{n\ge0}\frac{3^n u^n}{2n+1},\quad
S=\sqrt{1-4u},\quad J_g=S(g-2I),\quad I'=\frac E S.
\tag{J1}
\]

这里b_g是固定正整数，b_gg∈Z。三行实际Q(u)-rank3。235证明任意固定basis/literal n^e/有限LCM矩阵都有τ♭♭+τ♯≥7/3。它不证明degree-D变化的实际多项式整格最优。冻结全部共同图cap为C*=3π³√2/8<18；在分子至少log c的rank3判据里，新的有效费用必须
τ_eff<(2/3)log C*，尚需同图真实energy。这是必要门槛，不是从raw index定义出的已付τ。

现在固定完整源

\[
L_D=\mathbb Z[u]_{\le D}^3,\quad M=3(D+1),\qquad
T_N(c,b,a)=[c+b(uE)+a(b_gJ_g)]_{0,\ldots,N}.
\tag{J2}
\]

Λ_(D,N)={P∈L_D:T_N(P)∈Z^(N+1)}才是本轮对象；保留所有M列和全部0,…,N输出。以下没有旧W、Θ族或有限参数拟合。

## 2. 原文允许的改进不是免费换τ

复用当前220页CDT作者PDF，3628820 B / SHA256 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c。本轮实际FULL读物理50–54、82–88；82–88首次输出尾部截断后，另完整读取86–88补齐，未把截断当FULL。

§6.6的公开τ计算为**模板内所有可发生首项分母的worst-case**。它在(6.6.4)–(6.6.6)允许任意符合类型的函数和species置换，而忽略辅助多项式指数k的均匀分布限制。Remark6.6.15明确允许在更复杂的limiting formula中利用该限制和更细的实际分母，但作者没有在主应用中取得非可忽略改进。这是一项可研究的重证入口，不是将Λ_(D,N)指数代入Theorem8.0.1的许可。

实际函数间p-adic cancellation与degree-D整格可以更大；它们改变source lattice的同时，也改变box principle、balanced tensor restriction与实处metric。必须把这些都送回同一个filtered evaluation source及同一个首个非零β。只看有限处index省了多少，不能扣掉旧τ7/3。

## 3. 新全尺度prime-jet lemma

设D≥0、N≥1，p>3且p∤b_g，满足

\[
N<p\le2N-1,\quad h=(p+1)/2,\quad k=(p-1)/2,\quad m=N-h\ge0.
\tag{J3}
\]

全部E/J原系数下标≤N<p，外积分分母均为p单位；内奇分母小于2p，仅有一次p。所以完整tuple所有输出至多simple p极点，无p²层、无遗漏的g项或finite heads。235完整截断残差给

\[
pT_N(c,b,a)\equiv
3^ku^h\{b+b_gaA\}\pmod{(p,u^{N+1})},
\quad
uA'+\left(\frac12+\frac{2u}{1-4u}\right)A=-2,\quad A_0=-4.
\tag{J4}
\]

完整证明也可直接从J1给出：pE≡3^ku^k，而J_g′+2J_g/(1−4u)=−2E；代入pJ_g=3^ku^hA，h≡1/2 modp，即得J4的ODE。原生gS整项的残差为0，初始active coefficient给A_0=−4。
这里只使用A_0,…,A_m；m≤(p−3)/2，故其递推的2j+1<p，归约全有定义。b_g为单位，可吸收它；c整行残差为0。

定义完整residue mapρ:(a,b)∈Fp[u]≤D²↦[aA+b]_(0,…,m)。若m≤D，b本身已覆盖全部m+1输出。若m>D，先用b自由清掉0,…,D，剩余r=m−D个输出；对a_D,a_(D−1),…逆序，其前r个列与这些输出形成

\[
H_r=(A_{1+i+j})_{0\le i,j<r}
\quad(1\le r\le D+1).
\tag{J5}
\]

下一节给H_r精确det与unit条件。于是只要r≤D+1且p>4r−1，ρ的rank恰m+1，完整active输出全部onto。r=0即前面的b覆盖情形，不调用空Hankel除法。

特别N=3D+2时，或一般N=3D+C₀、C₀固定且D充分大，自动m−D≤D+1，而且p>4r−1：
4r−1=4N−2p−4D−3，等价3p>4N−4D−3；N≤4D+3与p>N已经保证它。

因此对于这个整个窗口，

\[
\boxed{\operatorname{rank}\rho=N-h+1,\qquad
[L_D\otimes Z_p:\Lambda_{D,N,p}]=p^{N-h+1}.}
\tag{J6}
\]

证明index：pT_N全整，T_N整当且仅当J4残差为0；这是原完整Z_p源到Fp的surjective map，其kernel index就是p的rank次方。J6是实际最大整数值source格的精确index，不只是row LCD或函数层独立；它仅对这个窗口断言。

## 4. Jacobi行列式自足证明

将J4的ODE乘1−4u，得到
u(1−4u)A′+(1/2)A=−2+8u。因此

\[
A_1=16/3,\quad A_n=\frac{8(n-1)}{2n+1}A_{n-1}\ (n\ge2),
\quad
A_{n+1}=8\,4^n B(n+1,3/2)
=8\int_0^1(4t)^n\sqrt{1-t}\,dt.
\tag{J7}
\]

不是旧调和moment矩；也没有用Q上的正性直接推Fp unit。下面计算其rational det。

对w(t)=√(1−t)，Rodrigues多项式
R_j=w⁻¹(j!)⁻¹(d/dt)^j[t^j(1−t)^(j+1/2)]
为degree j，leading coefficient
ℓ_j=(−1)^j Γ(2j+3/2)/(j!Γ(j+3/2))。Leibniz公式直接给这一值。分部积分j次的边界全为0：0处有t^j，1处剩余至少(1−t)^(3/2)。故R_j与所有degree<j多项式正交，并有
∫R_j t^j w=(−1)^j B(j+1,j+3/2)。
monic norm因此为
(j!)²Γ(j+3/2)²/[Γ(2j+3/2)Γ(2j+5/2)]。

单位三角的monic换基保留Gram det，乘这些norm、消去Gamma相邻因子，再用J7的8与4缩放，得

\[
\boxed{\det H_r=
2^{3r^2+r}
\frac{\prod_{j=0}^{r-1}(j!)^2}
{\prod_{i,j=0}^{r-1}(2i+2j+3)}.}
\tag{J8}
\]

这是全部r的纸证。若p>4r−1且p>3，分母中每个正奇数都<p，分子fact中每个正整数也<p；det严格为p单位，支付J5–J6。r=1给16/3，r=2给2^14/525，仅作纸面公式边界核，不是有限probe。没有CAS、prime scan或浮点积分。

## 5. 全有限处的实际CRT起步模型与精确窗口收益

取安全row尺度q_E=d_(2N−1)、q_J=d_Nd_(2N−1)，固定g分母已经由f₃=b_gJ支付；包括2、3及全部高幂。window外保留row lattice
Z_p[u]≤D ×q_E Z_p[u]≤D ×q_J Z_p[u]≤D，
window内改为J6的精确kernel。各条件只有有限个prime且为整系数有限同余，CRT给一个真实full-rank Γ_D,N⊂L_D，完整T_N(Γ_D,N)⊂Z^(N+1)。

window中的q_E、q_J都恰含一个p。下面精确式按N已经大于全部固定坏prime p|3b_g写；一般N须在两个window求和中都排除这些prime，并保留其fallback。故

\[
\log[L_D:\Gamma_{D,N}]=(D+1)(\log q_E+\log q_J)
-2(D+1)\!\sum_{N<p\le2N-1}\!\log p
+\!\sum_{N<p\le2N-1}\!(N-h+1)\log p.
\tag{J9}
\]

有限p|3b_g留在fallback，D充分大时不出现在window，不改主项。对N=3D+O(1)，PNT及partial summation给

\[
\sum_{N<p\le2N-1}(N-h+1)\log p
=\frac14N^2+o(N^2)=\frac94D^2+o(D^2).
\]

与同一row-clearing lattice的真实enlargement gain为
2(D+1)N−N²/4+o(D²)=(15/4)D²+o(D²)；
完整fallback的logindex=(45/4)D²+o(D²)。三个值分别是window cost、同对象finite收益、完整safe upper，不能混写成CDTτ，更不能从7/3减15/4。

45/4是一个已付完整有限整模型的upper，不是最优all-prime lower。继续细化p≤N可能减费；首层全rank又说明这个p>N窗口已经饱和，不能再凭“更巧的kernel”在同一完整输出中制造额外rank亏损。

## 6. 非零jet可用已给定理，真正的第一桥仍未付

本源实际derivation closure可明确写成

\[
\frac d{du}\begin{pmatrix}1\\uE\\J_g\end{pmatrix}
=
\begin{pmatrix}
0&0&0\\
[2(1-3u)]^{-1}&(2u)^{-1}&0\\
0&-2/u&-2/(1-4u)
\end{pmatrix}
\begin{pmatrix}1\\uE\\J_g\end{pmatrix}.
\tag{J10}
\]

b_g只作固定rational row缩放，不改closure或rank。采用当前CDT Theorem3.2.8（Shidlovsky）及Lemma3.2.14末句，存在固定C(g)，使degree≤D任意非零source的ord₀≤3(D+1)+C(g)。这不是本文新证明，也没有算出最小常数；它足够令N=3D+C₀的完整jet映射单射。N=3D+2只是outputcount匹配，本稿仍不claim它已单射。固定O(1)改变不影响J6/J9主项。

但Γ_D,N不是原文balanced tensor/polynomial source bundle的自动替代。具体地，整格vector在单变量中混合species；tensoring后若按原文balanced species及均匀辅助指数k删项，原有p-adic cancellations可能被破坏。CRT源基的实处高度也没有由logindex免费支付。

**237首个核心引理应明确为**：将Γ_D,N及其vanishing filtration送入同一BC metric与完整filtered evaluation，逐项支付有限评价norm、实处metric degree、meromorphic pullback的极点清除及graded高度总和。若能直接建立source-joint criterion，就不必沿用原文的balanced tensor构造；不能提前把κ=45/4按某个常数除后叫作已付τ。即使暂按拟议直接公式τ=2κ/9估算，它仅为5/2，比旧7/3还大；这一条件代入并不是已证新判据。

若选择原文tensor实现，则应对balanced/seeding空间𝔅_(D,d,ε)控制
(Γ_D,N^⊗d)∩𝔅_(D,d,ε)
的实际metric degree/coefficients height；在保留原vanishing order α≈3dD/2及首项分布的同时，产生非零F，其同一leading β由完整coordinate jets确实为整数，并给
log H(F)≤α τ_joint+o(α)
或等价的完整valuation/covolume估计。必须连同同图Cauchy energy证明严格净差。只有这时τ_joint才有进入判据的意义。

这不是一个“index/常数=τ”的定义。原文Remark6.6.15允许重作这种估计，但没有交付它；J9单独也不交付它。可先用全部prime安全模型测试这道桥，之后只细化真正决定缺口的prime层，不开参数扫描或无限多轮Smith优化。

## 7. 与既有paid资产比较及有界决定

实际FULL读222联合整格8410 B / 6c45b5ab4083d012d32f35cfad6f29f522b66f8b3420c8461490677d460d80cc：它已付完整top flag、unit shear及fallback，却缺mid/low和同源高度转移；其source不同，不能继承费用或非零性。实际FULL读229余子式去标量2684 B / 398d55ca195fff9bd3e41597cc3137313bccd543038edbebd66e10e959d0ae2d：精确去除人为共同标量是可迁移原则，但不证明真实W值非零。旧W已停，本轮不借其rank。

本源比那些旧门槛多出两项已付资产：一个**全尺度完整window的最优local index**，以及可直接采用的derivative-closed O(1)零估计。缺的首先是J9到同一个filtered/tensor source的metric桥，而不是“再找几枚prime”或“再说明函数独立”。

因此保留一次有界237重构：先证明或否定上一节的精确桥及可能严格余量。若只能重复row矩阵费用、或混合整格进入实际filtered source时收益全部被实处/删项费用抵消，应停止此源的联合格提案，转新周期载体；不把安全upper不够好当全joint no-go。若桥成立，再只付导致定量缺口的prime层。目标仍是新的真实数值结论，本文不以t候选的搜索absence认证全球novelty。

实际读域与primary选页身份在literature/global_review_sources_round236_20261008/packet_reading_scope.md。数学程序0、扫描0、新PDF0、Git0、旧文件修改0；仅NEW236数学稿及packet来源记录。保存后实际FULL作者复读并另报bytes/SHA。
