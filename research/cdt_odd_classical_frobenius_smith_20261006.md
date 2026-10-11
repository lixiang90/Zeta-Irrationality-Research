# Classic rank10：实际 forcing 的 Frobenius packet 与两层原格 Smith 收益

日期：2026-10-06。NEW 证明稿；冻结输入只读，没有运行、import 或修改旧/同行 producer，没有扫描素数、次数或参数。原始文献另存[清单](../literature/manifest_cdt_odd_classical_frobenius_smith_20261006.json)。本稿得到一个已经具体化的正接口：实际 H 的全前缀两阶 Frobenius packet，在原 rank10 polynomial source 中给三条第一层、两条第二层评价关系。它们是不同 Smith 阈值的信用，不是五个独立的普通 kernel，也没有删除 forcing 或降低 actual rank。

## 1. 同一目标、原格和准确 prefix 窗口

采用[完整 actual rank10](cdt_odd_classical_zeta7_full_rank_20261006.md)的真函数
\[
\mathcal F=(1,H_z,\theta H_z,\theta^2H_z,\theta^3H_z,
 F_z,\theta F_z,\ldots,\theta^4F_z),\quad x=256z,\quad
\theta=x\partial_x=z\partial_z.
\tag{C1}
\]
这里
\[
H(x)=\sum_{n\ge1}a_nx^n,\quad
a_n=\frac{(n-1)!^4}{(1/2)_{n+1}^4},\quad H_z(z)=H(256z),
\quad [(\theta+1/2)^4-x\theta^4]H=16x.
\tag{C2}
\]
F 是冻结的完整 C₂+91440ζ(7)A 源，不把它替换成齐次 primitive5。反证假设ζ(7)∈Q只为给这个同一实际 germ 的 rational coefficients 与固定清分母数 D₀，不改变其真实数值或 rank。

固定任意0<ε<1。已有完整安全型是：constant 行无分母；四条 H 行各用四列 b=2+ε；五条 F 行各用三列 b=1和八列 b=2+ε。这个数组只有 e=0。H 的 Δ_(2N+1)^4 安全界和 F 的 D₀Δ_N³Δ_(2N)^8 输入见[共同叶算术稿](cdt_odd_classical_lambda_leaf_arithmetic_20261006.md)§5及[冻结经典投影](cdt_odd_classical_derivative_projection_20261006.md)。有限 initial 项并入固定 D₀。

对 odd p∤D₀，下面所有 packet 均明确只在 n<N 的 prefix 使用，并要求
\[
\boxed{p^2>2N+1.}\tag{C3}
\]
仅 N<p²不足：H 的 odd denominator 到2n+1，可能已经含p²层。接完整安全数组时另取 p²>(2+ε)N 并留固定 initial 的 margin。这个条件保证 p⁴a_n 对全部所需 n 都 p-integral，且 odd valuation只有一次；不能从本稿把 p⁴H 称为全无限级数的整函数。

令 U 为 p⁴H 的 n<N reduction。K U=0 modp²在这个 prefix 成立，因为真实 RHS 是16p⁴x。所有以下 theta 操作保留 prefix 次数；没有从 modp 身份除p，也没有将截断身份提升为全形式身份。

## 2. 全 prefix 第一层 packet：次数约p/2

设 h=(p−1)/2、d=(p+1)/2。由(C2)对 n≥2的准确 recurrence
\[
(n+1/2)^4a_n=(n-1)^4a_{n-1},
\tag{C4}
\]
以及所有 odd 层的计数式，可知在(C3)中
\[
v_p(a_n)=-4\quad\Longleftrightarrow\quad
n\bmod p\in\{0,h,h+1,\ldots,p-1\};
\]
其他positive residues给 v_p(a_n)=0。这里 n=kp+h至kp+p恰为一个连续 packet；n=0单独是H₀=0。p=3也符合，不另假设p为ordinary。

定义两个系数 p-integral的实际有限多项式
\[
\begin{aligned}
T(x)&=\sum_{j=0}^{d}t_jx^j,
&t_j&=\left[\frac{(-1/2)_j}{j!}\right]^4,\\
V(x)&=\sum_{j=0}^{d}v_jx^j,
&v_j&=\left.\partial_\rho
 \left[\frac{(-1/2+\rho)_j}{(1+\rho)_j}\right]^4\right|_{\rho=0}.
\end{aligned}\tag{C5}
\]
j≤d<p；numerator的全部因子也是p-units，所以 t_j、v_j∈Z_(p)。T₀=1、V₀=0，degT=d且leading coefficient为p-unit。

每packet的起点 n₀=h+kp满足 n₀+1/2=p(k+1/2)。对0≤j≤d，whole coefficient ratio准确是
\[
\frac{a_{n_0+j}}{a_{n_0}}
=\left[\frac{(-1/2+p(k+1/2))_j}
 {(1+p(k+1/2))_j}\right]^4
\equiv t_j+p(k+1/2)v_j\pmod{p^2}.
\tag{C6}
\]
这是在p-unit denominators处的有限 rational-function Taylor 展开，余项含p²。packet之外 U_n∈p⁴；它们对modp²仍为0。把起点系数 U_(h+kp)当作慢系数 w_k，取 s=x^p、W(s)=Σw_ks^k（仅需要 prefix 项），便得整段严格身份
\[
\boxed{U\equiv x^h\{T(x)W(s)
 +pV(x)(\theta_s+1/2)W(s)\}\pmod{p^2,x^N}.}
\tag{C7}
\]
packet间没有重叠；每段延伸到 kp+p，下一段从(k+1)p+h开始。prefix末尾只截断相应最后一段。因此(C7)不局限于第一个packet或fixed offset，更不依赖慢系数本身的任何未知特殊性质。转到原 z 时使用 x=256z、s=256^pz^p；256是odd p-unit，所有degree和整性原封保留，不更换全局 source。

modp的(C7)给真实的一阶 polynomial relation
\[
\mathcal L_1=T\theta-hT-\theta T,\qquad
\mathcal L_1U\equiv0\pmod{p,x^N},\quad
\deg\mathcal L_1\le d.
\tag{C8}
\]
另有 θℒ₁、θ²ℒ₁，均degree≤d、order≤3，故能作用于(C1)的四条H行；没有引入第五条H derivative。

## 3. 第二层消元：真实primitive row，不重复计算第一层

下面的计算在 Z_(p)[[x]] 中进行，T₀=1使T可逆。置
\[
B=T\theta V-V\theta T,\qquad Q=T^2+B.
\tag{C9}
\]
degB≤2d−1，因为两个top-degree terms抵消；Q₀=1且degQ=2d、leading coefficient为p-unit。用 y=x^hT、v=x^hV写(C7)。设 α=θy/y=h+θT/T，β=θv−αv=x^hB/T。由于 θ_t W(x^p)=pθ_sW，准确有
\[
(\theta-\alpha)U
\equiv p\{(y+\beta)\theta_sW+(\beta/2)W\}\pmod{p^2}.
\tag{C10}
\]
令 α₂=θ(y+β)/(y+β)=h+θQ/Q−θT/T。再作用 θ−α₂，把slow导数带来的p²项保留为误差，而快系数余项必须真正消掉，得到
\[
\left\{(\theta-\alpha_2)(\theta-\alpha)
-p\frac{Q\theta B-B\theta Q}{2QT^2}\right\}U
\equiv0\pmod{p^2,x^N}.
\tag{C11}
\]
这里 p 的correction不能删去；只用乘积两阶算子一般只有第一层。Q=T²+B进一步给
\[
Q\theta B-B\theta Q=T(T\theta B-2B\theta T),
\]
所以清 QT 足够，无需QT²。得到实际 polynomial row
\[
\begin{aligned}
\mathcal L_2&=P_2\theta^2+P_1\theta+P_0,\\
P_2&=QT,\\
P_1&=-(2hQ+\theta Q)T,\\
P_0&=(h^2Q+h\theta Q)T+(\theta Q)(\theta T)-Q\theta^2T
 -\frac p2(T\theta B-2B\theta T).
\end{aligned}\tag{C12}
\]
所有coefficients p-integral，degree≤3d，P₂ degree恰3d且modp非零。由(C11)
\[
\mathcal L_2U,\quad\theta\mathcal L_2U
\equiv0\pmod{p^2,x^N};
\quad\operatorname{order}\le3,\quad\deg\le3d.
\tag{C13}
\]
Euler left multiplication不增加polynomial degree。

具体nested关系也可直接看到：
\[
\overline{\mathcal L_2}
=(Q\theta-hQ-\theta Q)\overline{\mathcal L_1},
\tag{C14}
\]
θℒ₂同样落在modp的ℒ₁、θℒ₁、θ²ℒ₁ polynomial span中。若R·ℒ₂的degree≤D，则modp系数乘子的degree≤D−d，完全处于同一个 admissible第一层source中。因此第二层没有被当作两条额外普通kernel；它将第一层中的两类primitive directions提高一个Smith阈值。任意解W的full formal模型满足这些算子恒等式，但实际U的应用范围仍只有(C3)/(C7)的prefix。

## 4. 固定原 rank10 polynomial source 的实际阈值账本

用原整数 source
\[
E_D=\bigoplus_{i=1}^{10}\mathbf Z[z]_{\le D}f_i(z),
\quad R=10(D+1),\quad N_D=10(D+1)+O(1).
\tag{C15}
\]
N_D来自同一actual独立、derivation-closed系统的有效Shidlovsky leading flag，不仅是dimension计数。令V_D⊂[0,N_D)、#V_D=R为实际leading rows。好p满足统一safe-prefix条件后，Ψ_p=p¹¹eval_(V_D)是整矩阵。它仍是原 pure source，没有将ℒ₁/ℒ₂换成新全局基，或偷偷扩大degree≤D空间。

四条H blocks原有 image p⁷，因为其prefix至多p⁴分母；constant block有image p¹¹；五条F blocks仅使用已证p¹¹安全上界。于是baseline floor和是
\[
11(D+1)+7\cdot4(D+1)=39(D+1).
\tag{C16}
\]
对于ℒ₁、θℒ₁、θ²ℒ₁乘次数≤D−d的polynomials，最高derivative阶依次1、2、3，leading coefficient都是T modp非零。依次比较最高derivative coefficient可严格证明它们modp线性独立，primitive rank为
\[
k_1=3(D-d+1)_+.
\tag{C17}
\]
它们在Ψ_p中有image p⁸，故给第8阈值的新floor。

对于ℒ₂、θℒ₂乘次数≤D−3d的polynomials，同样比较order3、2的最高QT coefficient，得primitive modp rank
\[
k_2=2(D-3d+1)_+.
\tag{C18}
\]
其Ψ_p images在p⁹，给第9阈值的新floor。(C14)确认modp层的嵌套；而原constant support与H support分离。两组lifts的整数span本身无需被假定互相独立，也不要求选一个同时保持species的Smith基。

逐阈值counts为：1至7至少5(D+1)，第8至少(D+1)+k₁，第9至少(D+1)+k₂，第10与11至少(D+1)。因此原 square leading minor有 certified capped Smith floors b_i≤11，满足
\[
\boxed{\sum_i b_i\ge39(D+1)+k_1+k_2.}
\tag{C19}
\]
这个原格determinant信用已经不同于只改变basis：没有换source，所有primitive向量均属于E_D⊗Z_(p)，degree损耗已记在(C17)/(C18)。其p-dependent rational coefficients可为p-units；仅用于原矩阵的local Smith证明，不当作一个免费全局arch-small新基。

## 5. 接真实 near-balanced species 与原 flat baseline

复用[已冻实际DVR/near-balanced接口](cdt_odd_level20_balanced_smith_bridge_20261006.md)§§1–2的普适引理，cap从3改为11。近似balanced source仍是E_D^⊗d的primitive species coordinate子格，codimension c/R^d→0（固定species tolerance，先D→∞，再d→∞）。tensor floors和至少dR^(d−1)[39(D+1)+k₁+k₂]，restriction损失至多11dc。真实balanced leading set在V_D^d内，此处仍可引用同一adapted-leading argument。

本数组 positive-column counts为ν=(0,4,4,4,4,11,11,11,11,11)，Σν=71、s=11。其θ=max(1/b)排序是zero1行、H四行1/(2+ε)、F五行1。matching充分窗口
\[
a_0=\min_{i\ge2}(i-1)/\theta_{(i)}=2+\epsilon.
\tag{C20}
\]
原CDT PDF122 Eq(8.0.2)明确在每个threshold k内部对 admissible balanced species/均匀degree coupling取 **maximum**，不是minimum；PDF123 Remark8.0.6与PDF124例亦保留这个上确界。任何coupling在每coordinate的成功列数≤ν_i，所以其normalized payoff至多Σν/m=71/10加species误差。反过来，取normalized n/N等距uniform grid，按上述排序把species i配到等宽1/10 bins，即n/D∈[i−1,i]（N~10D）。在p≤(2−δ)D的固定严格内窗，四个H bins的n≥D−o(D)使(2+ε)n>p，五个F bins的n≥5D−o(D)使n>p；全部positive列真正active。rounding后的species频率与grid discrepancy在原允许误差中，给同一71/10下界。因此原flat transport的 **maximum恰为** dΣν/m=71d/10，而原pure Smith baseline恰是11−39/10=71/10，二者准确接合。这不仅是一个all-active粗上界，也不是从不同window的优化成本中任意扣kernel维数。

严谨顺序为：先固定ε、tensor dimension及species tolerance；取p≤(2−δ)D且满足 p²>(2+ε)N_D，选择足够小的discrepancy；D→∞、tensor dimension→∞、tolerances→0，最后δ↓0。新坏place有限与小prime高幂照原upper处理，只删o(D²)的新信用；**没有忽略原p=2坐标成本**，它完整保留在原原z模型的old height中。

素数定理把新增floor和转成
\[
\begin{aligned}
\gamma_1&=3\int_0^2(1-x/2)dx=3,\\
\gamma_2&=2\int_0^{2/3}(1-3x/2)dx=2/3,\\
\boxed{\gamma=\gamma_1+\gamma_2=11/3.}
\end{aligned}\tag{C21}
\]
积分第二项是第二Smith阈值的一层，绝不是重复第一层。原第八节finite累计高度归一收益是γ/m=11/30；HS/source metric、arch evaluation与graded norms均未改变。按冻结接口§5的真实斜率归一，最终cost改进才为
\[
\boxed{\kappa_\epsilon=\tau^{\flat\flat}(b_\epsilon)
-\frac{2\gamma}{10^2}
=\tau^{\flat\flat}(b_\epsilon)-\frac{11}{150}.}
\tag{C22}
\]
因此该same-source、same-coordinate、same-metric普通CDT输入给
\[
10(\rho-\kappa_\epsilon)\le J.
\tag{C23}
\]
这是真正完成all-prefix→原格Smith→near-balanced determinant的正接口。它不通过ordinary density、特殊p样本或Levelt格比较获得，不把primitive exterior5额外算作免费函数秩。

## 6. 能证明的进展与剩余方向

原z λ-leaf的avoid conifold/unique0类仍有ρ≤−log16。数组safe rates及τ远大于这点11/150改进，故本稿没有在这个map类给ζ(7)矛盾，也未claim fulltarget最优费用。改到x=256z需保留已冻source/grade完整转换和原p=2主项，不能只挑本稿odd-p收益和archlog16。

新实际结果是四条forcing行已拥有可核的两层Frobenius整评价。下一有用条件是：完整F五行的真实p-dependentpacket，或一个与它们同原格、degree可计的higher-threshold关系；也可给另一个真实源的连接period消除。仅有齐次P4 unit-root、primitive外平方格或晶体存在不自动提供这些输入。尚不研究第三层，也不从(C22)外推其它数组/其它模型。

## 7. 原始文献输入和核验范围

[Dwork1973 IV](https://www.numdam.org/item/ASENS_1973_4_6_3_295_0/) Theorems1.1、3.1与§4研究hypergeometric系列比值/对数解的p-adic同余，Theorem3.1保留§3(v)(vi)参数条件。本稿实际读PDF2–3、8–12、16–18；不把它称为自动适用于完整rank10扩张的Frobenius定理。这里(C6–C13)由给定recurrence直接推导，不需要未经核实的晶体comparison。

[Beukers–Vlasenko Dwork crystals I v4](https://arxiv.org/abs/1903.11155v4) §3、Theorems4.3/5.3/5.7给integral Cartier与period coefficient congruences；actual应用需具体Laurent polynomial、factorial整模块、Hasse–Witt invertibility及源comparison。实际读PDF1–5、8–14。forcing扩张与primitive5/完整10的整模型在该文没有被自动识别；unit-root quotient也不是fullrank10。上述概述各不超过200词，没有以secondary来源代替primary。

新literature原件两份及SHA/实际读取范围保存独立manifest。本稿数学来自whole-prefix证明，不靠有限素数实验。NEW[固定符号脚本](cdt_odd_classical_frobenius_smith_20261006_verify.py)与[证书](cdt_odd_classical_frobenius_smith_20261006_verify.json)由作者首次单次执行，16项全通过。它仅检查(C12)的抽象消元、因式约去、nested coefficient identities、counts与有理积分；degree bound来自正文，不用符号样本代替。它不import旧脚本，不计算未知L值，不验证某个p样本来代替全p证明。

根任务实际阅读全文/PY/JSON及旧DVR桥§§1–7，通过whole-prefix原格关系、nested counts、阈值8/9、balanced/source/grade归一、strict matching window、γ=11/3与credit11/150；它另实际回读原CDT PDF122–124确认maximum与exact all-active cap，未执行producer。conjugate_projection实际只读本稿§§2–4并独审核packet residues、ratio shift、快慢分离、必要correction、QT清分母/3d degree、nested(C14)与原4H支持的primitive counts/baseline，通过；它未重跑producer，未以该范围代替§5的完整metric或未知fullF高层输入。本文据这些准确范围冻结，不扩为完整F₂最优成本或新ζ(7)数值定理。
