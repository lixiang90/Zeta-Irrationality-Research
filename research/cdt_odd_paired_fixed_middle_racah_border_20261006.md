# 原固定 λ2 的 Racah 完整块、真实 middle 秩二位移与 2r 阶非零门槛

2026-10-06，/root/conifold_arithmetic_hypothesis。NEW。Baseline487 既存数学、producer、JSON、审阅和收据全部只读，旧/同行执行/import/rerun0。本稿全尺度证明不假设 G0、实际 H0 或实际中间 profile 正常；不证明无限辅助素数的 M5 unit或新ζ/L定理。

## 1. 输入与实际目标

物理核main SHA ee3475aa18e73d8477d0cdece0a5e7504cfb99e3d5a52d6a66cfa1f2e7536837、audit SHA8a74a9ed32e524467ffa9d5fd866f71d652ce056cc794410d540574880f72faf；实际读main§§133–137、audit前40行，并完整回读冻结f988十一节Z1–23，没有声称完整重读main或audit。

p=18r+1素数、a=5r、F=Fp，u=y²，
\[
S_y(y)=\prod_{j=5r+1}^{9r}(y^2-j^2),\quad
S(u)=\prod_{j=5r+1}^{9r}(u-j^2).
\tag{R1}
\]
沿用两个cutoffs及halfjet：
\[
G(f)=\tfrac12(\Sigma_a+\Sigma_{r-1})S_y^{-5}f,\quad
C(f)=\tfrac12(5\Sigma_a-\Sigma_{r-1})S_y^{-1}f,\quad
H(f)=\tfrac12(\Sigma_a+\Sigma_{r-1})S_y^3f.
\tag{R2}
\]
Σ_l为k=−l,…,l之和。deg_u T<r、deg_u Q<3r；M5=[[G0,C5],[C5^t,H0]]，4r阶。完整块只作合法消元工具，不代替实际R2。

## 2. 原点半权重的 Racah 极限

Wilson给
\[
S_y(k)=\frac{(-1)^{r+k+1}}{(a-k)!(a+k)!},\quad
s_0=S_y(0)=\frac{(-1)^{r+1}}{(a!)^2}.
\tag{R3}
\]
令
\[
\mathcal H(f)=\sum_{k=-a}^aS_y(k)^3f(k^2).
\tag{R4}
\]
折叠后权重在k0为s0³，在k≥1为2S_y(k)³，即
\[
\mathcal H(f)=s_0^3\sum_{k=0}^a w_kf(k^2),\quad
w_0=1,\quad w_k=2(-a)_k^3/(a+1)_k^3\ (k>0).
\tag{R5}
\]

**Lemma R6。** 这恰是Racah权重在
\[
\alpha=\gamma=-a-1,\quad\beta=-2a-1,\quad\delta=a,\quad
g=\gamma+\delta+1=0
\tag{R6}
\]
的有理极限。其多项式为
\[
R_n(u)={}_4F_3\left(\begin{matrix}-n,n-3a-1,-y,y\\-a,-a,-a\end{matrix};1\right),
\quad0\le n\le a.
\tag{R7}
\]
\((-y)_j(y)_j=(-1)^j\prod_{i=0}^{j-1}(u-i^2)\)，故R_n是u多项式，R_n(0)=1。

证明：作者原件Koekoek–Swarttouw PDF29 Eq1.2.2的权重含
\((g)_k(1+g/2)_k/(g/2)_k=(g+2k)(g+1)_k/(g+k)\)。
k0值恒1，k>0极限为2k!；连同其他三个上/下Pochhammer准确得到R5。不能把原点0/0误当2。

有限正交式是参数有理恒等式：保持α+1=−a，在非空通常正交参数域成立，有限有理和恒等式延拓后再取可去极限。可取γ=−a−1+ε、δ=a、β=−2a−1趋近；全部j≤a的(-a)_j非零，无终止以内的分母极点。本稿不把positivity当有限域性质。

## 3. 全部完整 profile 的单位范数

Eq1.2.2专门化给
\[
\sum_{k=0}^a w_k R_n(k^2)R_m(k^2)=h_n\delta_{nm},\quad
h_0=\frac{(3a)!(a!)^3}{((2a)!)^3},
\tag{R8}
\]
\[
h_n=h_0\frac{(n-3a-1)_n n!(-2a)_n^3}
{(-3a)_{2n}(-a)_n^3},\quad
\kappa_n=[u^n]R_n=\frac{(n-3a-1)_n}{(-a)_n^3}.
\tag{R9}
\]

**Theorem R10。** 每个p18r1及0≤n≤a的h_n、κ_n均为F单位，故完整H全部leading Hankel profiles d≤a+1正常。

证明：最大阶乘指标3a=15r<p。n!及(-a)_n、(-2a)_n、(-3a)_(2n)的因子均严格非零且绝对值≤3a<p。n≥1时(n−3a−1)_n因子从n−3a−1到2n−3a−2，全部负，绝对值≤3a且≥a+2；n0为空积。全部分子分母单位。因此monic p_n=R_n/κ_n满足
\[
b_n=\mathcal H(p_n^2)=s_0^3h_n/\kappa_n^2,\quad
\det\mathcal H^{[d]}=\prod_{n<d}b_n\in F^\times.
\tag{R11}
\]
先前Dixon full H(1)单位只是n0；R10加强到所有完整profiles，未假定实际H0正常。

## 4. 完整核与 Christoffel–Darboux

取d=3r，
\[
D_{ij}=\tfrac12\mathcal H(u^{i+j}),\quad
d_n=\tfrac12s_0^3h_n,\quad \rho_n=d_n/\kappa_n^2.
\tag{R12}
\]
D已可逆，detD=∏_(n<d)ρ_n。令v_d(u)=(1,u,…,u^(d−1))^t，
\[
K_d(u,v)=\sum_{n<d}\frac{R_n(u)R_n(v)}{d_n}
=v_d(u)^tD^{-1}v_d(v).
\tag{R13}
\]
全部分母仅为已证单位。monic递推telescoping给
\[
K_d(u,v)=\frac{p_d(u)p_{d-1}(v)-p_{d-1}(u)p_d(v)}
{\rho_{d-1}(u-v)}\quad(u\ne v).
\tag{R14}
\]
u=v时取可去极限
\((p_d'p_{d-1}-p_{d-1}'p_d)/\rho_{d-1}\)。d=3r≤a，p_d/κ_d仍合法单位。自证：monic正交三项递推下项系数ρ_n/ρ_(n−1)，两变量相减除ρ_n求和，内部相消。只用已证完整norm。

## 5. 真实 middle 秩恰 r

u_k=k²（0≤k<r），V_(ik)=u_k^i，0≤i<d，并取
\[
E=\operatorname{diag}(e_k),\quad e_0=\tfrac12s_0^3,\quad
e_k=S_y(k)^3\ (k>0).
\tag{R15}
\]
准确有
\[
H_0=D+VEV^t.
\tag{R16}
\]
V的前r行是互异squares的Vandermonde，E单位，故更新秩恰r。由D可逆，
\[
\det H_0=\det D\det E\det(E^{-1}+V^tD^{-1}V),\quad
\operatorname{corank}H_0=\operatorname{corank}(E^{-1}+V^tD^{-1}V)\le r.
\tag{R17}
\]
核等价不要求实际H0可逆：H0q0时z=EV^tq、q=−D^-1Vz；反向同样成立。小矩阵entries为K_d(u_k,u_l)，原点e0仍是半权重。R17并未证明该r阶门槛单位。

## 6. 固定 M5 无条件压缩至 2r

令G=G0、C=C5为实际R2，取border
\[
\mathcal B=\begin{pmatrix}G&C&0\\C^t&D&V\\0&V^t&-E^{-1}\end{pmatrix}.
\tag{R18}
\]
消去已知−E^-1，得detB=(−1)^r det(E^-1)detM5；消去已知D，得到
\[
\mathcal N=\begin{pmatrix}
G-CD^{-1}C^t&-CD^{-1}V\\
-V^tD^{-1}C^t&-E^{-1}-V^tD^{-1}V
\end{pmatrix},
\tag{R19}
\]
\[
\boxed{\det M_5=(-1)^r\det E\det D\det\mathcal N,\quad
\operatorname{corank}M_5=\operatorname{corank}\mathcal N.}
\tag{R20}
\]
两次是invertible block congruence，prefactors全部明确单位。不除实际H0/G0，允许任意实际中间profiles奇异。

核精确重建：
\[
(t,z)\in\ker N\ \Longleftrightarrow\
q=-D^{-1}(C^tt+Vz),\ (t,q)\in\ker M_5,\quad z=EV^tq.
\tag{R21}
\]
前向将R19代回两行；反向由实际M5第二行和R16唯一求出q。

用冻结Z15–16，N中只有左上r×r块含两个指定第五幂种子A0,A1，其他由factorial双boundaries、R7–15和真实middle nodes明确给出。detN在A0,A1上combineddegree≤r，无独立自由B0；实际B0已由同一个Racah更新结构化处理。A0/A1仍是冻结Z20固定值，不能generic化。R20是新的同一对象非零门槛，不是其解答。

## 7. 真实 middle 的秩二 spectral displacement

Racah差分Eq1.2.5专门化为
\[
\lambda_nR_n(k^2)=B_k(R_n((k+1)^2)-R_n(k^2))
+L_k(R_n((k-1)^2)-R_n(k^2)),\quad
\lambda_n=n(n-3a-1),
\tag{R22}
\]
\[
B_0=-a^3,\ L_0=0,\quad
B_k=(k-a)^3/[2(2k+1)],\
L_k=(k+a)^3/[2(2k-1)]\ (k\ge1).
\tag{R23}
\]
B_a0。B0不能用k>0公式代0得−a³/2；它是同一g→0极限的半权重值。R5满足w_kB_k=w_(k+1)L_(k+1)，包括k0。

以R_n basis的middle Gram
U_(ij)=Σ_(k<r)e_k R_i(k²)R_j(k²)；
x_i=R_i(r²), y_i=R_i((r−1)²)。Green telescoping给
\[
\boxed{(\lambda_i-\lambda_j)U_{ij}
=\omega_r(x_i y_j-y_i x_j),\quad
\omega_r=e_{r-1}B_{r-1}\in F^\times.}
\tag{R24}
\]
证明：两条R22交乘相减，乘e_k，求和k0..r−1，内部按detailedbalance相消，L0=0，留下唯一右flux。r1使用e0B0，保持halfjet。

J=diagλ_n，实际H在R_n basis为 \(\widehat H=\operatorname{diag}(d_n)+U\)，因此
\[
\boxed{[J,\widehat H]=\omega_r(xy^t-yx^t),\quad
\operatorname{rank}[J,\widehat H]=2.}
\tag{R25}
\]
x,y独立：R0恒1，R1(r²)−R1((r−1)²)=κ1(2r−1)为单位。d3r≥3。i≠j<d时λ_i−λ_j=(i−j)(i+j−3a−1)全单位。故R24明示全部offdiagonal；diagonal仍为实际middle和，不得由rank2位移免费补齐。

## 8. 排除谱不变 kernel，但不排除一般相消

**Theorem R26。** ker \(\widehat H\) 不包含非零J-invariant subspace，特别不含单个Racah spectral coordinate。

J在F中有simple spectrum，非零invariant subspace含某个coordinate ε_n。若Hhatε_n0，R25给xy_n−yx_n0；x/y独立，故R_n在r−1,r都零。r1立即与R_n(0)=1矛盾；r≥2由R22从r−1逐级向0递推，L_k全单位，迫R_n(0)=0，仍矛盾。未除实际norm，未假定intermediate正常。

这不是kerH0=0：一般核可混合多个channels并且不被J保持。更不是M5unit。R20–21保留完整目标，下一步须在真实两个第五幂种子处排除2r门槛的混合boundary相消。

## 9. 三权重共用两侧 polynomial Pearson，真实 jumps 明付

记 \(\widetilde W=S_y^{-5}\begin{psmallmatrix}1&5S_y^4\\5S_y^4&S_y^8\end{psmallmatrix}\)。
内部−a≤k<a有S_y(k+1)/S_y(k)=(k−a)/(k+a+1)。定义
\[
A=\operatorname{diag}((k-a)^4,1),\ B=\operatorname{diag}(k-a,(k+a+1)^3),
\]
\[
P=\operatorname{diag}((k+a+1)^4,1),\ Q=\operatorname{diag}(k+a+1,(k-a)^3).
\tag{R27}
\]
逐entries得到
\[
A(k)\widetilde W(k+1)B(k)=P(k)\widetilde W(k)Q(k).
\tag{R28}
\]
实际signed weight是
\[
W(k)=\tfrac12\widetilde W(k)+\tfrac12\chi(k)Z(k),\quad
Z(k)=S_y(k)^{-5}z(k)z(k)^t,\ z=(1,-S_y(k)^4)^t.
\tag{R29}
\]
所以内部exactdefect
\[
A(k)W(k+1)B(k)-P(k)W(k)Q(k)
=\tfrac12(\chi(k+1)-\chi(k))P(k)Z(k)Q(k).
\tag{R30}
\]
χ在−r、r−1两边jump+1、−1，每个defect非零rank1。k=a跨full firstpole，R28不能当作endpointzero；必须另用冻结Z11 lastnodeflux。没有通过印刷finite-support Pearson theorem的θ(0)=0免费抹掉边界。

## 10. 新 primary 及准确读域

正常TLS归档三份，共233 archivepages：

- Mañas等《Pearson Equations … I》，[arXiv2107.01747v3](https://arxiv.org/pdf/2107.01747v3)，25页，实际完整读PDF1–10,13–15，13distinct。Theorem1的θ(0)=0、fullsupport及Gramfactorization前提不能证明本目标，R28–30自证实际边界。
- Li–Long–Tu《A Whipple7F6 Formula Revisited》，[arXiv2103.08858v2](https://arxiv.org/pdf/2103.08858v2)，38页，实际完整读PDF1–5。primitive/selfdual及具体very-well-poised parameters已读，原第五幂1/1取消对不能直接套该文specificmotive或fixedordinary结论。
- Koekoek–Swarttouw《The Askey-scheme …》，[作者原件98-17](https://tudelft.roelofkoekoek.nl/documents/as98.pdf)，170页，实际完整读PDF7,28–30，4distinct。Eq1.2.1–1.2.5和有理极限已核；R6halfjet、R10单位自证。旧机构URL正常TLS404，无原件；沿现行作者主页实际链接下载成功，无bypass。

作者实际22distinctpages，未读剩余211页；归档不等于读完。DLMF18.25现场阅读辅助核对，主公式范围以作者报告为准。URL/SHA/attempt另NEWreceipt。

本稿先作全尺度纸证。NEW同stem_verify.py完整静态回读后，guard exclusive-create先记录STARTED_FIRST1；首次且唯一1run exit0 PASS，共937身份checks，仅旧r1/2/4。核权重、所有完整norm、distinct-node CD、middle位移及2r同一det/corank，不扩auxprime、不assert M5unit。JSON所有三cases/全部字段已完整读，finite机制scope不升级无限单位；R14 diagonal极限及R28–30没有另做程序assert，由纸面证明负责。源/JSON/guard执行后冻结，不改不重跑。旧/同行执行/import/rerun0。

## 11. 已证与未证

已证：完整cubic恰为halfjet Racah；全部完整profiles单位norm；真实middle rankr与corankH≤r；固定M5合法压缩2r、核精确重建；actualH秩二spectral位移及无spectral-invariant核；三权重共用polynomialPearson且两jump/fullpole保留。

未证：真实2rdet在无限p上unit，固定第五幂种子防相消，或actualhigherSmith替代；sameobject global strictmargin；新ζ/L无理性或LI。完整normality仅作已付费合法消元，未替换实际λ2问题。
