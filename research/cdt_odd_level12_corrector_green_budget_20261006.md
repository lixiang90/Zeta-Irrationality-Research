# D12 整数校正族：全尺度 Green 单调、相位与固定成本

日期：2026-10-06。本文新增纯证明记录，不执行、import 或改动任何已冻结 producer，不扫描整数、word 或素数。实际 source 与秩来自[整数校正族](cdt_odd_level12_zero_period_corrector_family_20261006.md)，双反射合法叶来自[多反射证明](cdt_odd_level12_corrector_multireflection_20261006.md) §§1–3。本文已实际只读审核后者这三节的 real-slash、完整 fundamental domain、唯一 funnel、H/t 下降及 gauge；不代替其其它周期分类。

结论限定于这里真实认证的单反射和双反射叶：精确 Green 半径在整数族中随归一 width 严格下降，最大值在 n=0。对每个固定 n，原三目标行仍有满三层逐行分母；两个既定 log 数组也不能由本族地图触发 plain CDT 矛盾。§7.1进一步覆盖 Γ0(12)W 的 χ− det12 zero reflection 与其 real mirror 给出的两-circle盘，仍要求同一实际 source 合法 kill 该 reflection。这不是全部实际 stabilizer、所有可用地图或混合 Smith 格的 no-go。

## 1. 实际对象与 Green 归一

令
\[
\begin{gathered}
s_n=644n^3+552n^2+147n,\quad p_n=84n^2+48n+7,\\
a_n=24+84n,\quad c_n=12p_n,\qquad n\in\mathbb Z,\\
J_n=\begin{pmatrix}a_n&-7\\c_n&-a_n\end{pmatrix},\qquad
\widetilde J_n=\begin{pmatrix}-a_n&-7\\c_n&a_n\end{pmatrix}.
\end{gathered}
\tag{G1}
\]
实际 primitive 是 h_n^-=f_L+s_nf_R−Θ、h_n^+=σf_L+s_nf_R+Θ，Θ=34560√3 L(3,χ12)。它们分别对 W、J_n 与 mirror J̃_n 有真实 weight−2 anti identity；B=E2−12E2(12τ) 在这些变换下 weight2 anti，所以 H_n^±=Bh_n^± 真正不变。反证 L(3,χ12)∈Q 时两支才成为 coefficientwise K=Q(√3) 共轭 germs。保留 Θ，不能把周期常数任意删掉。

固定第一叶 X_+=〈T,W〉 的归一 width 为 √12。第二叶可以取单反射 X_n=〈T,J_n〉，也可以取已认证的 X_n^aug=〈T,J_n,J̃_n〉。它们均填唯一 cusp、coarse 化真正下降的 elliptic germs，得到 Riemann disk；全部其它 critical fibers 保留其真实 ramification。每支 t(q)=q+O(q²)，完整四行
\[
1,\quad g_\delta H_n,\quad g_\delta\vartheta_tH_n,
\quad g_\delta\vartheta_t^2H_n,\qquad
g_\delta=[1-4(2+\delta\sqrt3)t+4t^2]^2
\tag{G2}
\]
在相应叶全纯，实际 K(t)-rank 为4。这里ϑ_t=t∂_t，g 在导数之外；不把裸 Euler rows 自动当全局全纯。

对这些填后盘，记 R 为 local cusp coordinate q 的 conformal radius。已冻结的 [Hecke Green 证明](cdt_odd_level12_hecke_radius_20261006.md) 和 [n=0 augmented Green 证明](cdt_odd_level12_augmented_radius_20261006.md) 给精确归一
\[
\log R=\frac{2\pi^2}{w^2}\,\mathcal C,\qquad
\mathcal C=\sum_{G_\infty\backslash G/G_\infty,\,c_g\ne0}c_g^{-2}.
\tag{G3}
\]
该式来自 positive Eisenstein/Poisson series 的 cusp constant 与 funnel 的零边界 Green 函数。不是把一个 Taylor 收敛半径当 conformal radius。

若单位圆盘地图真的经这个叶 lift，且0映唯一 filled cusp，则 Schwarz lemma 给
\[
\log|\phi'(0)|\le\log R.
\tag{G4}
\]
t(q) 的一次项1使 t-radius 与 q-radius 相同。非单射 self-map 不会提高 (G4)。这里不对无法经该叶 lift 的其它 analytic continuation maps 作断言。

## 2. 单反射：精确半径严格随 w 下降

在 center-shift 坐标 ζ=(c_n/√12)(τ−a_n/c_n) 下，T:ζ↦ζ+w_n，J_n:ζ↦−1/ζ，其中 w_n=√12 p_n。Hecke double words 的 continuant 为
\[
c_0=1,\quad c_1=m_1w,\quad
c_k=m_kwc_{k-1}-c_{k-2},\qquad m_j\in\mathbb Z\setminus\{0\}.
\tag{G5}
\]
令 D=diag(m1,…,mk)，A_k 为 path adjacency matrix（相邻 entries 为1）。则
\[
c_k(w)=\det(wD-A_k)=\det D\prod_{j=1}^k(w-\lambda_j),
\quad \lambda_j\in\operatorname{Spec}(D^{-1}A_k),\quad |\lambda_j|\le2.
\tag{G6}
\]
最后界由最大 row-sum norm≤2；不要求 D 正定或 λ_j 全实。对 real w>2，
\[
\frac d{dw}\log|c_k(w)|
=\sum_j\operatorname{Re}\frac1{w-\lambda_j}>0.
\tag{G7}
\]
因为 Re(w−λ_j)>0，且 Re(1/z)=Re(z)/|z|²。每项 |c_k| 因而严格增加。所有 double-word 标签集与 w 无关，所以逐项比较 (G3) 的正级数，连同 w^−2 的严格下降，得到精确 logR(w) 严格下降。不需要把导数移入无穷和。

本族 p_n≥7 且仅 n=0 取等号，因此
\[
\log R(X_n)\le\log R(X_0),\qquad n\ne0\text{ 时严格}.\tag{G8}
\]
既有全 word majorant 给 C(w)=1+O(w^−2)，故 logR(w)=2π²w^−2+O(w^−4)；这是渐近证明，不是有限 n 数据拟合。

## 3. 双反射：三种间距一起增长，逐 word 精确比较

使用 unshifted ζ=(c_n/√12)τ。令 q_n=|14n+4|，u_n=√3 q_n>0（必要时交换两反射标签），则
\[
w_n=2\sqrt3p_n,\quad
S_{\pm u_n}(\zeta)=\pm u_n-\frac1{\zeta\mp u_n},\quad
0<2u_n<w_n.
\tag{G9}
\]
全部 translated circles 的最小 center separation 为 d_n=min(2u_n,w_n−2u_n)≥6√3；n≠0 时 d_n≥20√3。这些是真实多反射稿 §§2–3 已证明的输入。

按整数顺序
\[
0,-1,1,-2,2,-3,3,\ldots
\tag{G10}
\]
p_n 严格增加。对 m≥1，有 p_m−p_−m=96m；对 m≥0，有 p_−(m+1)−p_m=36(2m+1)。而
\[
q_m=14m+4\ (m\ge0),\qquad q_{-m}=14m-4\ (m\ge1),
\]
相邻 q 的增加分别为8和6。最后 r_n=p_n−q_n 满足
\[
r_m=84m^2+34m+3,\quad r_{-m}=84m^2-62m+11,
\]
两种相邻增加分别为96m−8（m≥1）、72m+30（m≥0）。所以 w_n、2u_n、w_n−2u_n 都在 (G10) 上严格增加；不是仅靠 w 增长猜 radius 单调。

所有这些群有同一个 free-product double-word 标签集
\[
S_{a_0}T_w^{\ell_1}S_{a_1}\cdots T_w^{\ell_k}S_{a_k},
\quad a_j\in\{u,-u\},\quad
\ell_j=0\Longrightarrow a_j\ne a_{j-1}.
\tag{G11}
\]
对应 transition b_j=ℓ_jw+a_j−a_{j−1}。每个固定标签的 sign 不随 n 变化。其绝对值属于
\[
2u,\qquad |\ell|w,\qquad |\ell|w+2u,\qquad
|\ell|w-2u=(|\ell|-1)w+(w-2u).
\tag{G12}
\]
因此每个 |b_j| 在 (G10) 上严格增加且始终≥d0=6√3。

还须证明 mixed signs 不会破坏 continuant 单调。对固定 sign pattern，令 B_k=diag(b1,…,bk)、A_k 同上，则 c_k=det(B_k−A_k)。设 T_k=B_k^−1A_k，最大 row-sum norm≤2/d0<1，故
\[
(B_k-A_k)^{-1}=(I-T_k)^{-1}B_k^{-1}.
\]
path graph bipartite 使所有奇数次 T_k 的 diagonal 为0；偶数尾有统一界
\[
\left|\sum_{j\ge1}(T_k^{2j})_{aa}\right|
\le\frac{4/d_0^2}{1-4/d_0^2}=\frac1{26}<1.
\tag{G13}
\]
于是 inverse diagonal 的 sign 正好是 sign(b_a)。Jacobi determinant identity 给
\[
\frac{\partial\log|\det(B_k-A_k)|}{\partial |b_a|}
=\operatorname{sign}(b_a)(B_k-A_k)^{-1}_{aa}>0.
\tag{G14}
\]
在两组 b 的 abs coordinates 间插值，始终满足同一 sign pattern 和下界 d0，故每个非空 continuant |c_k| 严格增加。空 transition 有 S+、S− 两个 choices，c0=1，不改变这个比较。

所以 C_aug,n 的每个非空 word 项逐项减少；n=0 的正常收敛 majorant 同时支配全部 n。结合 (G3) 的 w_n^−2，得到
\[
\boxed{\log R(X_n^{\rm aug})\text{ 随 }w_n\text{ 严格下降，最大值在 }n=0.}
\tag{G15}
\]
这是实际正级数的比较，不靠任意 fundamental domain 包含关系。对一般任意 (w,u) family，单独增加 w 未必够；此处使用了 (G12) 的三个明确单调量。

## 4. 全 n 的合法 map 上界与原 point phase

在 unshifted augmented 坐标，q=e^(2πiζ/w_n)=e^(2πiτ)，原 cusp point 没有发生相位改变。如果对单反射采用 center-shift，则
\[
q_\zeta=e^{-2\pi ia_n/c_n}q;
\tag{G16}
\]
这个常数模长1，只旋转 local parameter。phase 不额外增加或减少 conformal derivative 的绝对值；其对双反射相对位置的影响已经完整计入 b_j，不能再添一个“phase radius”因子。

用 n=0 augmented 稿的精确 Green upper 与第一叶 upper，有
\[
\log R_+<\frac{290884}{123333},\qquad
\log R(X_n^{\rm aug})\le\log R(X_0^{\rm aug})
<\frac{\pi^2}{147(1-\pi^2/343)}.
\tag{G17}
\]
其有理比较采用 π²<484/49；冻结旧证书已经准确给出
\[
\bar\rho_n:=\frac{\log|\phi_+'(0)|+
\log|\phi_{-,n}'(0)|}{2}
<\frac{2443691800}{2013164559}<\frac54.
\tag{G18}
\]
这里第二地图经真实 X_n^aug lift；不要求选 Riemann map 才有 upper。第一 source 虽随 n 改变，第一几何叶 〈T,W〉 和 q/t 归一不变。新背景要求的共同延拓只会缩小可选地图类，不提高 (G18)。

也可以直接使用单反射的统一平均 upper<6/5；它和 (G18) 是不同地图类的安全界，不能把较小的单反射界强塞给所有 augmented maps。

## 5. 每个固定 n 的满三层 componentwise 分母

以下先固定 n，再令 CDT source degree 或 prefix 长度增长。除有限坏素数（允许依赖这个固定 n）外，R 在 good p 的第 p 项为240(1+p³)，所以 F_n 的模 p³ leading packet 为
\[
u_{n,\epsilon}=294960+240s_n-69120\sqrt3\,\epsilon
=240(1229+s_n-288\sqrt3\,\epsilon),\quad\epsilon=\chi_{12}(p).
\tag{G19}
\]
其范数
\[
\operatorname{Norm}(u_{n,\epsilon})
=240^2[(1229+s_n)^2-248832]\ne0
\tag{G20}
\]
对所有整数 n 非零，因为248832=3·288²不是 integer square。这是全 n 非消去证明，不是一个素数试验。排除这个固定非零范数、p|12、B0=−11 以及 Θ 固定分母的素因子后，u 在两 embedding 上均为 p-unit。

已实际回读 [source denominators](cdt_odd_level12_source_denominators_20261006.md) 的 D4–D8：低于 p 的 primitive 系数全 p-integral，p 项主部为 B0u/p³，p+1 项只有 B1u/p³，其中 B0=−11、B1=−24。整数 q(t)=t+… 的 p 次幂在 p+1 的额外项含 p，因此
\[
p^3[t^p]H_n\equiv-11u_{n,\epsilon},\qquad
p^3[t^{p+1}]H_n\equiv-24u_{n,\epsilon}\pmod p.
\tag{G21}
\]
这是 fixed-prefix 赋值论证；不用假设完整 native Cartier 矩阵可逆。

G2 的 g0=1、g1=−8aδ，其中 aδ=2+δ√3。于是
\[
\begin{aligned}
p^3[t^{p+1}](g_\delta H_n)&\equiv(88a_\delta-24)u_{n,\epsilon},\\
p^3[t^{p+1}](g_\delta\vartheta_t^jH_n)&\equiv-24u_{n,\epsilon},\qquad j=1,2.
\end{aligned}
\tag{G22}
\]
第二式的 g1·[t^p]ϑ^jH 额外含 p^j 而消失；第 p+1 系数乘 (p+1)^j≡1。第一式因子 Norm(88aδ−24)=−128，在 p≥5 为 unit。因此三目标行均保留全部三层。

配合原 LCM_N³ 安全 upper，由素数定理每条目标行的最小公共 prefix denominator M_N 满足 logM_N=3N+o(N)。更具体地，固定 CDT row 类型 N^e∏LCM_floor(b_jN) 在 N=p+1 时 N^e 为 p-unit；固定 b_j<1 的列最终不含 p，b_j≥1 每列至多一层。因此至少三列 b_j≥1，不能由固定 Euler row 或整数 corrector 免费降成 two-layer cost。

这只是自然 componentwise 数组的必要成本；不排 p-dependent mixed integer lattices、跨背景消去、Smith determinant gain。n 若依赖 D，log|s_n| 及 source-height 等也须另计，本文的 fixed-n 成本不授权这一交换极限。

## 6. 明确固定数组的 plain-CDT 必要尺度

在原 ordinary Jensen 指标及其合法边界/limit 条件下，\(\bar J\ge\bar\rho\)。若用 rank m、既定 e0 数组真实成本 τ，则 holonomy contradiction 必须满足
\[
m(\bar\rho-\tau)>\bar J,
\quad\text{所以必要 }\bar\rho>\frac m{m-1}\tau.
\tag{G23}
\]
这不是声称 J 的 lower bound 可达到，也不是所有 refined metrics 的 no-go。

对裸四行及两个已认证 cheap-log arrays：

|固定实际数组|m|精确 τ|必要平均 ρ|
|---|---:|---:|---:|
|G2 四行，三 target 各三 unit LCM 列|4|45/16|15/4|
|全部 total-degree≤2 的三个 cheap logs，加三 target|13|366/169|61/26|
|全部 total-degree≤3 的三个 cheap logs，加三 target|23|1146/529|573/253|

两个 log cost 是[冻结联合 transport](cdt_odd_level12_cheap_log_transport_20261006.md) T5 的精确真值；348/169、1078/529仅为早先 comonotone lower，不在本表当成本。三个 logs 的 punctures 是同一实际 nonzero cusps，所有新叶继续遗漏它们；simply connected disk 上可取 zero-origin branch。residue independence、packing arithmetic 与只有一维 composition factors 的背景由[cheap-log证明](cdt_odd_level12_cheap_log_packet_20261006.md)给出；其与 rank3 irreducible target quotient 交仅常数，故实际 rank13/23 对各固定 n 仍成立。

这三个必要尺度均大于5/4；(G18) 因而严格排除本族这些地图与这些 componentwise 数组通过 plain-CDT/ordinary-J 得到新的无理性矛盾。表中没有给任何未证明的 mixed Smith 信用，也没有把“合法函数更多”直接变成更低成本。

## 7. 新结论的边界与下一接口

本轮完成的是两个全尺度结论：真实整数 corrected double-reflection family 的精确 Green 半径逐 word 单调，及每个固定 source 的原三行三层成本持续存在。因此继续选本族其它 n 不会改善本表的 capacity/cost 缺口。

它没有分类 H_n 的完整 zero-period subgroup。进一步真实 zero-period generators 可能改变整个 double-word index set，不能由这里的逐项比较排除；必须先证明同一实际 source 的完整 period identity 和新 leaf 合法性。多反射稿 §§4–6 提供其它 det12 反射的 rational exact period interface；本文仅追加实际只读核其§5的 matrix/Jacobi、centered-circle geometry 和已合法 zero reflection 的叶接口，不核其全部有限 Bernoulli 周期值或完整 stabilizer。

当前 R 校正已保留纯 L 周期；它给新实际反射和真实镜像，却没有给新的 Taylor/Smith 净信用。跨背景 mixed lattices、其它 source、whole-vector bundle theorem、ζ(7) 不同 ODE 仍是独立研究方向。本结论不宣称数值 L(3,χ12) 无理。

### 7.1 所有 eligible χ− reflection 与 real mirror 的固定两-circle盘

考虑 γ∈Γ0(12)、χ12(γ)=−1 且 J=γW 为 det12 trace0 involution。按多反射稿§5的准确规范，
\[
J=\begin{pmatrix}12b&-a\\12d&-12b\end{pmatrix},\quad
ad=12b^2+1,\quad d>0,\quad\chi_{12}(d)=-1.
\tag{G24}
\]
需要同一实际 rational-corrected source h_s^+=σf_L+s f_R+Θ、s∈Q 已真正满足 h_s^+|−2 J=−h_s^+；这里只接受完整 function identity，不用一个 endpoint 猜它。real q coefficients 给 mirror anti identity，T-periodicity使 T-conjugation 也保持 zero。

T-conjugation 可将 b 改成 centered residue，令 b0=|b| 满足0<b0<d/2。d 与6 coprime且 odd，b0不能为0。由−12b²≡1 mod d，有 (−12/d)=1；χ12(d)=−1迫 (−1/d)=−1，从而 d≡7 mod12、d≥7。设 r0=d−2b0 为 positive odd integer。

若 b0=1，d|13，与χ12(d)=−1不容；若 r0=1，将12b0²+1≡3r0²+1 mod d得 d|4，同样不容。因此 b0≥2、r0≥3。等号更严格：
\[
b_0=2\Longrightarrow d\mid49\Longrightarrow d=7;\qquad
r_0=3\Longrightarrow d\mid28\Longrightarrow d=7.
\tag{G25}
\]
最后的 χ12(d)=−1 排除了d=1、49等其它正因子。所以 d=7 时准确只有 b0=2；其反射是旧 M 或 M′ 的 T-conjugates。除此之外
\[
d\ge19,\quad b_0\ge3,\quad r_0\ge5.
\tag{G26}
\]

标准化后 width w=√12d、两centers±u=±√12b0；min separation为√12 min(2b0,r0)≥6√3。完整盘合法性由多反射稿§5逐项复用§3的 coverage、单 boundary cycle、real mirror与 actual t/H/g下降；其 boundary trace=24b0r0−2≥142。因此使用同一 double-word 标签集和 G13–G14是合法的。

相对 baseline d=7、b0=2 的三间距，d>7 时
\[
w>7\sqrt{12},\qquad 2u>4\sqrt{12},\qquad
w-2u>3\sqrt{12}.
\tag{G27}
\]
G12的每个 transition abs 均严格增加且 sign 不变；G13–G15无需族参数是一条整数二次曲线即可逐 word比较。于是每个这样的真实 zero reflection/mirror pair盘满足
\[
\log R(X_{J,\bar J})\le\log R(X_0^{\rm aug}),
\quad\text{等号仅 centered }(d,b_0)=(7,2).
\tag{G28}
\]
baseline等号指两个-circle几何盘，不把其它period群的 quotient误认成同一盘。若同一source还有更多真实zero generators，G28不限制那个更大群产生的新叶。

固定 rational sR 的算术也保持 G19–G22：只把s_n换成s。Norm u_s=240²[(1229+s)²−248832]非零，因为288√3∉Q；固定分母与该固定范数只排有限坏素数。每个 fixed rational s 的两目标 embeddings各三行依然满3层。R在用于rank lower bound的两个cusp常数都为0，原非zero cubic支保留，故已合法 corrected model的rank4不被这次 rational校正破坏。三个cheap-log backgrounds仍使用同一t punctures，预算原数组也不变。

因此§6的plain/ordinary-J失败适用于这些 **已经完整认证 zero identity 的 χ− reflection/mirror pair盘**；不是所有source、所有反射余类、完整origin stabilizer或其它maps的no-go。本节没有搜索或计算更多 (b,d) 周期值。

## 8. 执行与审阅记录

本文纯 MD，无新 producer。作者实际只读 frozen integer-corrector、source-denominators、n=0 Hecke/augmented Green 和 exact-log-transport；实际独审新 multireflection §§1–3，通过 real-slash、d_n、完整 quotient 与实际 H/t/g 下降。没有运行、import、改动旧 producer，没有计算任意有限 n/素数/word 样本。全尺度 monotonicity 由 G6–G15，分母率由 G19–G22 承担。

实际限定只读独审：root完整阅读加入§7.1之前的本MD §§1–8，通过 G6–G15 的 spectral/Neumann/whole-word比较、相位/Green归一、G19–G22的fixed-n范数与三层主部及固定预算范围；随后实际完整阅读新增§7.1，独核 G24–G28 的 centered residue、Jacobi、两等号情形、三间距比较和 eligible zero-reflection/mirror pair scope，通过。root还实际读了多反射完整周期接口与两个新 rational-corrected sources 的 q-integrality；本稿不借此扩大为全 stabilizer结论。root未执行任何producer。low_period_closure实际读先前版本§§1–6，独审通过§§2–4和G19–G22的algebra；其未重证 upstream source-denominators D4–D8或old log transport，故不记为这些上游输入的完整独审。本文作者随后实际只读多反射更新§5，核G24–G28所用det/Jacobi、centered-circle和合法pair leaf条件，未运行其producer。

本文在上述实际限定审核状态冻结，纯MD无PY/JSON，也无数学producer执行。后续 extra generators、mixed Smith或其它source另开文件，不改此证明记录。
