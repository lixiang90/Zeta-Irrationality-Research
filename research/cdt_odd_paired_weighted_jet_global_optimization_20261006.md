# 原配对格联合 jet 权重的精确 36 顶点优化与全窗口预算

2026-10-06，NEW，toric_chow_completion。471 个既存数学输入与旧、同行 producer 全部冻结只读。本稿保留原 B6/κ3/s5、degree<3n、rank2n 的饱和配对整数格 S，以及同一个 whole-X determinant D_A(X)。新程序仅用于独立有理数 affine certificate，不产生有限 prime 探针；执行状态在末节和独立来源收据登记。

## O1. 对象与已经证明的局部接口

令 M=⊕_{i<3n}Z binom(t−1,i)，L=ker C⊂M，C 的实际 primitive rows 为 q_mP(m)−p_mP(2n+1−m)，其中 p_m=d_m/g_m、q_m=d_{2n+1−m}/g_m、d_m=(m)_{6n+1}，g_m 是两 d 的 gcd。原 S 是 L 的完整 rank2n 整数基。全文沿用

\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^{2}\binom{2n+j}{j}^{3},\quad U_j=-8aH_j^{(3)}-6bH_j^{(4)},
\]
\[
V_j=(5H_j-3H_{2n+j}-2H_{6n-j})U_j+24(X-aH_j^{(4)}-bH_j^{(5)}).
\tag{O1}
\]

估值为 Q[X] 的 Gauss valuation，因而逐 X coefficient 成立。先取整数 a,b；固定有理来源的统一分母仍付 O(n)，实处 S 不换基。

本轮实际全文读取冻结 weighted W1–W10（b9535b…），其整数值 ψ=(t^p−t)/p 基、指定 jet minor 的 mod-p rank 费用和真实 node-block 权重给如下自足优化接口。设 p>5、p²>8n、p≤6n，d=2n，3n=Qp+R，0≤R<p，并令

\[
q_\rho=\lfloor(6n-\rho)/p\rfloor,\qquad
w_\rho=2\lfloor6n/p\rfloor-2q_\rho
 +3\lfloor(2n+\rho)/p\rfloor-3\lfloor2n/p\rfloor\in\{0,2,3,5\}.
\]

全尺度、同一个 D_A 已证

\[
v_pD_A\ge-10n+\Omega_p,
\tag{O2}
\]
\[
\Omega_p=\min_{\substack{0\le r_\rho\le2q_\rho+2\\\sum r_\rho=d}}
\left[\sum_\rho f_\rho(r_\rho)-2\min(R,\#\{\rho:r_\rho>Q\})\right],
\quad f_\rho(r)=w_\rho r+4(r-2q_\rho)_++2(r-Q)_+.
\tag{O3}
\]

左、右 jet minors 在同一个 A block-minor 中具有相同 residue counts r_ρ；O3 没有使用彼此独立的最坏 Plücker 费用。它仍只是实际 determinant 的 lower bound，不是实际 Gram Smith 的准确估值。以下精确解决 O3，不把这个模型的最优性扩张到真实行列式。

## O2. 共享信用的一个真实槽位

若 Q≥1，则 floor(6n/p)≥2Q，从而 q_ρ≥2Q−1，故 Q+1≤2q_ρ。f_ρ 的依次边际槽位为：前 Q 个价格 w_ρ；接着 2q_ρ−Q 个价格 w_ρ+2；最后两个价格 w_ρ+6。唯一可获一次 −2 信用的槽位是第 Q+1 个。其前方价格 w，其获信用后的价格也为 w，后方价格≥w+2。

Q=0 时前段为空；若 q_ρ≥1，第一槽价格 w+2；若 q_ρ=0，第一槽已经为 w+6。第一槽同样是唯一可获信用的槽位。两种情况下获 −2 后均不大于其后的边际。总共有 p 个特殊槽位，全局只允许至多 R 次信用，不能给每个 residue 免费复制最后一层。

## O3. 一个整数最小费用 flow 的准确等价

把所有边际槽位作为容量1的 vertices。普通路径为 source→slot→sink，第一条边的费用是该槽的未折扣边际，slot→sink 容量1、费用0。对每个特殊槽位，再开 source→coupon→slot 的路径：source→coupon 容量 R、费用 −2；coupon→slot 容量1、费用为未折扣的槽价。source 送 d 单位，sink 收 d 单位。其余边容量1。

任一 O3 的前缀选择给一个合法 flow：在被选的特殊槽位中，选 min(R,K) 个走 coupon，费用恰好是 O3。反向取任一整数 flow；每个槽至多选一次，credit 使用量≤R。若某 residue 选择了较后槽而漏了较前槽，交换二者。

* 被换出的槽非特殊槽时，换到任一较早普通槽的费用不增；如较早特殊槽尚未用信用，其普通费用也不大于后槽。
* 被换出的槽是获信用的特殊槽时，较早槽价格≤它折扣后的价格；删除该次信用并选早槽，费用不增，且全局 coupon 约束更宽松。

反复交换得到每 residue 一个前缀。为所得选中的特殊槽位使用最大允许的 min(R,K) 次信用只会进一步降低费用。因此整数 flow 的 minimum 正好等于 Ω_p。

这个 flow 的实数 LP 也具有整数最优解。给一个简短整性证明：取最优 extreme flow；若不在边界的 edges 构成一个无向环，可以在该环沿两方向作保持所有 vertex balances 的 ±ε 改动。最优性迫两方向一阶费用均0，移到至少一条边界，故这样的点不能是 extreme。非边界 edges 因而组成 forest；从每棵树的 leaf 逐步消去，整数 balance 与整数固定边界迫余边 flow 为整数。可行集 bounded 且非空，有 extreme optimum，所以实数与整数 minimum 相同。这里用的是原 O3 的整数容量，没有引入新的算术格或实处范数。

## O4. 准确 dual 与合法 lower bound

每个普通选择和特殊 credit 选择均可用变量表示，slot 容量是1；唯一耦合是所选总数 d、credit 总数≤R。对前者用 multiplier λ，后者用 γ≥0。令 η=2−γ。若 0≤η≤2，则折扣后的边际仍单调，独立槽位的 priced minimum 正好是一个前缀 minimum。记

\[
\alpha(w,q,Q;\lambda,\eta)=
\min_{0\le r\le2q+2}\{wr+4(r-2q)_++2(r-Q)_+-\lambda r-\eta\mathbf1_{r>Q}\}.
\tag{O4}
\]

对所有 λ∈R、η∈[0,2]，直接代入 O3 即得合法 lower bound

\[
\Omega_p\ge \Phi_p(\lambda,\eta)
=\lambda d-(2-\eta)R+\sum_{\rho=0}^{p-1}\alpha(w_\rho,q_\rho,Q;\lambda,\eta).
\tag{O5}
\]

准确性可由这个有限 flow LP 的以下 polyhedral separation proof 得到，而不是假设 greedy。令 K 为独立槽位选择的 compact polytope，z记录普通/credit选择。写 Az为总选择数、Bz为credit数、cz为费用。集合

\[
\mathcal E=\{(Az,Bz+u,cz+v):z\in K,\ u,v\ge0\}
\]

是 polyhedron：由 finite inequalities 描述的 K 添加两个半轴后，逐变量 Fourier–Motzkin elimination 给有限 inequalities 的线性投影。在最小可行费用 m=Ω_p 处，(d,R,m)∈E，(d,R,m−ε)∉E 对全部 ε>0。故在 E 的有限 defining inequalities 中，至少一条在此点 active 且费用 coefficient严格正；否则所有 active inequalities 都不限制向下费用，而非active inequalities在足够小ε下仍满足，矛盾。因为 E 包含向上 credit-capacity 和费用半轴，该 active inequality 归一化为 c−λs+γb≥k，其中 γ≥0。于是对所有 z∈K 有 cz−λAz+γBz≥k；取 optimal z，同时 (d,R,m) active，得 γ(R−Bz)=0 及 k=min_K(cz−λAz+γBz)。因此 m=λd−γR+min_K(cz−λAz+γBz)，正是独立slot定价的 dual，无 gap且 attained。slot容量逐项给 O4/O5。结合 O3 的整性，dual optimum 等于整数 Ω_p。

若 η<0，特殊槽的 coupon 路径比普通路径更贵，独立 priced minimum 忽略它；改为 η=0 使 -(2−η)R 不减，minimum 相同。因而最大值无需 η<0。若 λ<0，全部 priced prefixes 费用非负，α=0，dual≤0；λ=0、η=2 给0。若 λ>11，所有槽都选中，dual 的 λ 斜率 d−Σ(2q_ρ+2)<0，故移回11不减。于是准确 optimum 在 [0,11]×[0,2]。

## O5. 精确 36 顶点定理

O4 在该 rectangle 上的折线仅为 λ 等于槽价 w、w+2、w+6（整数），以及 λ+η 等于特殊槽未折扣价格 w+2 或 w+6（整数）。在每个 arrangement polygon 上，各 α 和 Φ 均 affine；一个最大值可取该 polygon 的 vertex。竖线、斜线和 rectangle 边的交点均具有 λ 整数、η∈{0,1,2}。故对全部 O1 的 p,n，准确成立

\[
\boxed{\Omega_p=\max_{\substack{\lambda=0,1,\ldots,11\\\eta=0,1,2}}\Phi_p(\lambda,\eta).}
\tag{O6}
\]

这里是 12×3=36 个表达式，与 n,p 无关。其每一项即使不调用 dual equality，也已由 O5 独立证明为合法内容界；后面的安全费用只使用这些 lower bounds。准确 Ω 的等价不声称 actual determinant 就达到它。

## O6. 连续 residue type 与全部进位端点

写 x=p/n，Q=floor(3/x)、h=floor(6/x)、a_2=floor(2/x)，定义

\[
c=6-hx,\quad t=(a_2+1)x-2,\quad r=3-Qx.
\tag{O7}
\]

0≤c<x，0<t≤x。在 actual integer count 中令 e=6n−hp、T=(a_2+1)p−2n，q_ρ=h 当且仅当 ρ≤e；w 的第二个 carry 在 ρ≥T 开始。

若 e+1≤T，三 type 为 (w,q)=(0,h),(2,h−1),(5,h−1)，准确 count 为 e+1、T−e−1、p−T。若 e+1>T，三 type 为 (0,h),(3,h),(5,h−1)，准确 count 为 T、e+1−T、p−e−1。边界空 type 的 count 为0，特别 e=0、T=p、p整除2n/6n均覆盖。

相应连续 counts 仅将 e+1 换成 nc：

\[
(N_0,N_2,N_5)=(c,t-c,x-t)\quad(c\le t),
\]
\[
(N_0,N_3,N_5)=(t,c-t,x-c)\quad(c\ge t).
\tag{O8}
\]

对36个 candidate 定义

\[
\phi_{\lambda,\eta}(x)=2\lambda-(2-\eta)r+
\sum_{types}\alpha(w,q,Q;\lambda,\eta)N_w(x),
\quad g_\Omega(x)=-10+\max_{36}\phi_{\lambda,\eta}(x).
\tag{O9}
\]

在任何固定 compact x window 中，f和candidate的常数全部有界，actual 与 O9 的误差由移位一条 residue 产生，统一 O(1)。在 x∈[1/4,6]，Q≤12、q≤24、r槽≤50；|α|≤550 即够，两个 type 各误差≤1，故可以统一保守付 C=1100：

\[
v_pD_A\ge n g_\Omega(p/n)-1100.
\tag{O10}
\]

在 floor 跳点使用 actual floor 定义；左右 limit 的 candidate 给同一界至少误差 C，因为 integer formula始终有效，而固定多个端点 primes 总贡献也为 O(n)。未删除任何 exceptional n 或 prime。

## O7. 一个无需程序的确切新增 paid 1/24

取 2n/3<p<17n/24，p²>8n、p>5。这里 h=8、Q=4、a_2=2，e+1>T，unit type count 正好 T=3p−2n，其余是 w3/q8 与 w5/q7。candidate λ=3、η=2 给

\[
\alpha(0,8,4;3,2)=-26,\qquad
\alpha(3,8,4;3,2)=\alpha(5,7,4;3,2)=0.
\]

前者在 r=16 取值；各段 slopes 检查它是 minimum，后两者在 r=0 取 minimum。O5 因此是准确的有限 n lower bound

\[
\Omega_p\ge6n-26(3p-2n)=58n-78p,
\quad\boxed{v_pD_A\ge48n-78p.}
\tag{O11}
\]

此处 η=2 对应 γ=0，虽然实际总信用可能受 R 约束，dual 仍是合法 relaxation；没有把 R 免费复制到每条 residue。471已付 C 模型在该段为14−30x，其他旧 entrycap/Plücker、x>1的G、旧root1/84均不更强。因此新增正 part 为34−48x，严格面积

\[
\boxed{\int_{2/3}^{17/24}(34-48x)\,dx=1/24.}
\tag{O12}
\]

这是真正相对于471安全费用的信用，而不是 Ω 自身的裸面积或同一费用的重复扣除。

## O8. 471 基线的准确共同 max

本稿独立 certificate 以 frozen55278的47条合并 raw affine 行为 literal 输入（原50行只合并3个同 affine 的 entrycap 分点）。它不读、import或执行旧 producer。令 raw(x) 为其原 Λ−2T 下界。

旧 carry credit 在 1/2<x<1 中为 2(d_in+d_out)，其中

\[
z=2-\lfloor2/x\rfloor x,\quad T=(h+1)x-6,
\quad d_{in}=\max(0,\min(T,z-T)),
\quad d_{out}=\max(0,\min(T-z,x-T)).
\tag{O13}
\]

在1<x<2仅加2d_in；其他段按已经证明的 cap兑现门槛不加新的裸面积。首先取 max(−10,raw+carry)。再与 frozen C/G 的

\[
g_{sector}(x)=-10+2[2-Q u-\min(3-Qx,u)]_+,
\quad u=\min(6-hx,(\lfloor2/x\rfloor+1)x-2),
\tag{O14}
\]

在 x∈[1/4,2] 取 max。旧大素数 J 是 max(−2−2x,x−13) 于3<x≤4、max(2x−18,x−13)于4<x≤6；旧root weighted只在31/42<x<3/4加入240x−184。这些共同 max 定义 g_471(x)。程序必须准确验证其费用积分等于冻结471公式

\[
A_{471}=\frac{45711182732576087}{1070827036198920}
-\frac{16469}{23100}-\frac1{84}.
\tag{O15}
\]

小于1/4的窗口保持旧−10模型，费用为5/2，故 A_471=5/2−∫_{1/4}^{6}g_471(x)dx。它是 baseline一致性检查，不重算旧producer，不把 raw fee、共同gcd或局部GL再次当作新信用。

## O9. 同轮 actual paired image 的合接范围

本轮实际全文独读 quarter 新稿 e4830013… U1–U10。其从 actual primitive split C、d_m factorial carry 和 inner反射得到：V=p−(2n modp)，u=min(6n modp+1,V)，a_2=floor2n/p，独立真实 unithead约束

\[
f=a_2\min(u,V/2).
\]

其 whole-X DND 已证对 p≤2n 的内容下界

\[
v_pD_A\ge-10n+2[2n-Qu-\min(R,u)+f]_+.
\tag{O16}
\]

Q≥a_2+1 时像秩准确；Q=a_2 区间仅需要已证明的 upper rank，不升级为 exact。U6先固定真实globaltop，再用底Q层插outsidehead零，保证 lift 在原 S 而非自由ambient。本稿只将这个实际读过的 theorem 作为第二个合法界，于x∈[1/4,2]定义

\[
g_{pair}(x)=-10+2[2-Q u-\min(3-Qx,u)+a_2\min(u,((a_2+1)x-2)/2)]_+.
\tag{O17}
\]

将分别报告 Ω-only 相对471的信用，和 max(g_471,g_Ω,g_pair) 相对471的 combined信用。两者不能相加；也不能再外加quarter的19/980窗口信用，因为它已经被共同max包含。finite integer error在[1/4,2]统一有界，其他places保持原费用。

## O10. 全窗口 exact affine certificate 的证明方式

在[1/4,6]加入2/j、3/j、6/j的所有floorbreak、raw行端点、window端点。在每个floorcell中再加入 c=t、O13各affine比较、O14的min/positivepart，以及O17的 V/2和positivepart所需交点。随后加入该cell内 baseline 与36个candidate以及paired界的全部pairwise交点。每个最终closed subcell内所有函数均 affine，其max由任一 interior point选择；certificate在两端逐个确认winner dominate，exactFraction积分。整个闭区间被无缝partition，无随机采样、数值最优猜测或有限prime表。

实际 bound 的 uniform O(1)减项逐prime总共付 O(n)，small p≤sqrt8n 保持旧 O(n^(3/2)logn)预算，p>6n保留旧whole-X integrality。因此分段连续主率的共同max和PNT给

\[
\log|Q_n^{-1}|
\le (A_{471}-\Delta)n^2+o(n^2),
\quad\Delta=\int_{1/4}^{6}(\max(g_{471},g_\Omega)-g_{471})dx,
\tag{O18}
\]

以及用 combinedmax 的同型定理。这里 A 是原 S 下清分母并除共同内容之后的 rational normalization scale 的实绝对值费用；一般不能把跨prime保留的正content信用叫作 raw denominator(D_A) 的上界。先在每个prime选actualinteger lowerbound ℓ_p，并构造合法signed scaling Q_n=Π_p p^{ℓ_p}，故 D_A/Q_n∈Z[X]，其 log|Q_n^{-1}|=−Σ_pℓ_p logp 同时计入负估值的分母和正估值的共同内容。只在大primewindow优化，因而所有places的旧安全证明仍在。实处仍是原S，没有localGL的免费archfee。

## O11. 完整积分结果和已经执行的 FIRST1 证书

NEW源码保存后实际完整静态read，guard尚不存在，首次且唯一执行1次：exit0 PASS，success1、failed0、rerun0、旧/同行execute/import0。源码/JSON成功后不改不重跑。它只做 O10 的 exactFraction affine 全window证书，不重复 finiteprime表，也不执行/import旧或同行 producer。生成49 initialcells、261 branchcells、1601完整affine arrangement cells，合并为113 certificate rows，266036 closed endpoint/cover/area checks。

程序准确复现 O15 的基线费用

\[
A_{471}=\frac{224674976889262531}{5354135180994600}.
\]

全部closedcover相加给

\[
\boxed{\Delta_\Omega=\frac{1433895329207009209}{2765986534444032900}
 =0.518402859649\ldots,}
\]
\[
\boxed{A_\Omega=\frac{90135864061549507}{2174857836049080}
 =41.444485504989\ldots.}
\tag{O19}
\]

与本轮 O16 的 actual paired image 共同取max则给

\[
\boxed{\Delta_{combined}=\frac{4594551260881450309261834591}
 {2837232739731183068973297600}=1.619377640946\ldots,}
\]
\[
\boxed{A_{combined}=\frac{68678357676574195925297901887}
 {1702339643838709841383978560}=40.343510723692\ldots.}
\tag{O20}
\]

O19和O20都相对于完整471费用；O20包含O19以及本轮paired界的部分重叠，不能相加。quarter的19/980也不能再次扣除。一个较大独立Ω窗口是2<x<16/7：Q1、h2、a_2=0，λ3η2给 gΩ=12−8x，基线是−x−4，新增16−7x面积2/7。113行证书还保留所有其它正/零段；它不是从数值最优或有限prime估值外推。

成功后实际parse整个JSON，并完整读取全部metadata及113行的每个字段，包括floortype、三种winner标签/affine系数、两种gain系数和两种exactarea；无截断。没有声称逐条人工重新运行266036计算；纸面全尺度证明、实际完整静态source和闭区间certificate给可审依据。源码、JSON、finalpaper指纹及准确readscope登记于独立NEWreceipt，末次状态待独审冻结。

本轮实际read：baseline main§§127–132；冻结weighted W1–W10；冻结credit-cap S1–S10；冻结largejet J1–J23；冻结C1–C10；冻结55278 JSON全部metadata/50 affine rows；同行e483 U1–U10。不存在为本稿新增的PDF/HTML/外部代码下载；所需flow整性、dual分离、prefix和affine顶点证明都在本稿。另行审阅同行稿的primary页只记该正式独审实际scope，不伪计为本稿新来源。旧 source/manifest/math仍只读。

已证改进是同一个actual整模型的whole-X finite-place费用，不证明 infinite target-unit、不证明任何 special value非零，不把安全上界不足当真实cost下界。解析已证>12.003572854…，仍需strictmargin；没有新增ζ(7)、Catalan或ζ/L无理性/线性无关性定理，没有Lean执行。
