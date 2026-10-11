# 指定 weighted jet 支撑真正承受的 primitive 配对约束

2026-10-06，NEW，quarter_actual_rank。487 个既存数学输入、全部旧/同行 producer 和旧收据冻结只读。本文保持原 B6/k3/s5、degree<3n、原整数值饱和配对格、完整 S 和 whole-X 行列式；不执行/import/rerun 旧或同行程序。

## P1. 同一对象和本轮结论

沿用冻结 e483 的实际整数格
\[
M_{3n}=\bigoplus_{i<3n}\mathbf Z f_i,\quad f_i=\binom{t-1}{i},\quad
c=2n+1,\quad d_m=(m)_{6n+1}=\frac{(6n+m)!}{(m-1)!}.
\]
写 m'=c-m、g_m=gcd(d_m,d_m')、p_m=d_m/g_m、q_m=d_m'/g_m。原饱和格及完整基为
\[
A_{n,\mathbf Z}=\ker(C_m)_{m=1}^n,\qquad C_m(P)=q_mP(m)-p_mP(m'),
\]
\[
S=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\qquad
G_m=p_mL_m+q_mL_{m'},\quad L_m(k)=\delta_{mk}\ (1\le k\le2n).
\tag{P1}
\]
L_m 是 degree2n−1 的整数值 cardinal polynomial。D_A(X) 仍是冻结 b953 W1 的 form 在 S 上的 rank d=2n determinant。固定有理 sources 先清同一个固定分母，只付 O(n)；以下估值均逐 X 系数。

**本轮新增定理：** 对任意指定 d 个实际 jet rows，只有其“大 residue blocks”所承受的 primitive head constraints 可以扣除。本文给出准确的可用约束数 f_B、严格 rank bound 与 whole-X minor 接口；无需 selected local jets injective。一个明确窗口相对487基线严格付出 1/216 的 n² 改进。它已包含在 toric 本轮更广的共同 max 中，不能重复相加。

## P2. 实际系数空间与任意选中 rows

设 p>5 为 prime，p≤2n、p²>8n，写
\[
2n=ap+r_2,\quad3n=Qp+R,\quad6n=hp+r_6,
\quad0\le r_2,R,r_6<p,
\]
\[
V=p-r_2,\quad u=\min(r_6+1,V),\quad U=\{0,\ldots,u-1\},\quad
\sigma(\rho)=V-1-\rho\quad(0\le\rho<V).
\tag{P2}
\]
冻结 e483 U8–U16 已独立证明：C:M3n→Zn 是整数 split surjection，所以 A/pA=ker Cmodp；实际 integer-valued ψ 基
\[
\psi(t)=(t^p-t)/p,\qquad
\binom{t}{i_0}\binom{\psi(t)}{i_1},\quad i=i_0+pi_1<3n
\tag{P3}
\]
与原 Newton 格作 GL3n(Z_p) 变换。这里 i<p²，highest coefficient 比为 p-unit，变换整性由整数值 finite differences 得到。local polynomial Φ_ρ(Y) 作用于 t≡−ρ，前 Q coefficients 在各 residue 完全自由，第 Q coefficient 只能来自 degree<R 的 low-digit polynomial。故任意 residue set B 上的完整 coefficient projection 空间维数是
\[
\dim\mathcal B_B=Q|B|+\min(R,|B|).
\tag{P4}
\]
P(−j)、pP'(−j) 模 p 是 Φ_ρ(ψ(−j))、−Φ_ρ'(ψ(−j))。P4 是**系数源空间**，不声称 selected jets 在它上面 injective。

令 Y 为原 S 到全部 j=0,…,6n 的 value/scaled-derivative rows 的 Z_p 矩阵。指定 d=2n 行 I；记 r_ρ 为在 j≡ρ 的选中行数，Σr_ρ=d，并定义
\[
B=\{\rho:r_\rho>Q\},\quad C=B\cap U,
\]
\[
\boxed{f_B=a|C\setminus\sigma(U)|+\frac a2|C\cap\sigma(C)|.}
\tag{P5}
\]
P5 的第二项同时处理 offcenter mirror pairs 与 fixed residue loops。

## P3. supported primitive constraints 的独立性

直接从 d_m 的 factorial 算式（端点≤8n<p²）得：unit-W sector U 中的实际 head d_m 都有 valuation h+1；其 inner mirror 若不在 U 则 valuation h。positive head residue 是 m≡−ρ，而非 m−1。所有 inner residues 0≤ρ<V 均有恰 a 个真实 positive head sites；其 ψ-values 互异。

因此在指定 coefficient set B 中，实际 A 的 image 必须满足下列**仅使用 B 中数据**的 primitive constraints。

1. ρ∈C\σ(U)：其 mirror 在 inner nonunit packet。除掉真实 gcd 后，primitive equation 强迫 unit 高 carry 侧的 a 个 head values 为零；outside value 的 coefficient 被 p 整除。这有 a 条约束。
2. ρ、σρ 都在 C：两边 d_m carry 相等，primitive coefficients 都是 p-units。两个不同 residues 间的 a 个 actual head pairs 各给一条关系。若 σρ=ρ，该 residue 的 a 个 sites 成 a/2 actual pairs，因为 c odd 没有 fixed integer head site。

若 unit mirror 仍在 U 但不在 C，**本文不扣这一关系**：另一边不在所用大系数源空间内。也不把其它 nonunit relations 免费加入。

所有上述 head pairs 或 forced head sites 互不重叠，故它们在 head value coordinates 上独立。p≤2n 给 Q≥a。固定真实 ragged top coefficients 为零，每个 unit residue 的自由底 Q 层在其 a 个不同 head ψ-values 上任意插值；这是 degree<Q 的 Vandermonde surjection。因此这些 f_B 条 constraints 在实际 P4 系数源空间上仍独立，未破坏 top-layer 的共享。

P5 为整数：V odd 时 a even（2n=ap+r2、p odd），故 loop贡献 a/2 整。非loop的 C∩σC 数为偶数。没有把 loop 当作两个 offcenter relations。

综上，实际 A 到 B 的 coefficient projection 落在 codimension f_B 的已明确子空间；其维数至多
\[
Q|B|+\min(R,|B|)-f_B.
\tag{P6}
\]
本定理只需必要 constraints，未假设任意满足这些关系的数据均能作 outside-head 延拓。后者对整个 U 的精确条件已在冻结 U5 给出，而对任意 B 不免费扩大。

## P4. 真正的 selected-row rank bound

先将 r_ρ≤Q 的所有 small blocks 当作至多 Σsmall r_ρ 的自由贡献。余下 big rows 是实际 coefficient projection P6 的某个线性 observation；无论该 observation 是否能恢复常数项，其 rank 都不超过源维数。故
\[
\boxed{\operatorname{rank}_{\mathbf F_p}Y_I\le
\sum_\rho\min(r_\rho,Q)+\min(R,|B|)-f_B.}
\tag{P7}
\]
原 S 是完整格基，所有 entries 在 Z_p；整数 unit elimination 或 Smith rank 给
\[
\boxed{v_p\det Y_I\ge d-\sum_\rho\min(r_\rho,Q)
-\min(R,|B|)+f_B.}
\tag{P8}
\]
右侧若负，仍是合法弱下界，可与0取max。它不等同于所选矩阵 exact Smith，也不将 finite verification 提升为 exact rank。

P7 的比较对象必须准确：它改进旧 W3 的**系数源 cap**，不是宣称 selected image 相对其自身 unconstrained exact rank 总下降 f_B。特别 derivative-only rows 可能看不见常数方向；不可把这里 f_B 再直接加到一个已经扣除了 observation kernel 的更强 rank cap。更不可把全 U 的 global f 扣到任意 I：未在 B 中完整支持的 mirror relations未计入。

## P5. actual whole-X 支撑相关费用

冻结 b953 W5–W6 给 p⁵B_A(X)=YᵗA(X)Y，actual node block 是
\[
A_j=W_j\begin{pmatrix}p^5V_j(X)&p^4U_j\\p^4U_j&0\end{pmatrix},\quad
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3.
\tag{P9}
\]
令 q_ρ=floor((6n−ρ)/p)，w_ρ=v_p(W_{ρ+lp})∈{0,2,3,5}。head l0 比 tail entries 多付至少4。A 的非零 minor在每个 node 的左右 row counts 相同，均为0/1/2；因此两边 Y_I、Y_J 的 residue r、B、C、f_B **完全一致**，即使 value/derivative types 不同。

两次 Cauchy–Binet、actual block valuation 与 P8 给
\[
\Omega_p^{support}=\min_{\substack{\sum r_\rho=2n\\0\le r_\rho\le2q_\rho+2}}
\left[\sum_\rho\{w_\rho r_\rho+4(r_\rho-2q_\rho)_+
+2(r_\rho-Q)_+\}-2\min(R,|B|)+2f_B(r)\right],
\]
\[
\boxed{v_p^{Gauss}D_A(X)\ge-10n+\Omega_p^{support}.}
\tag{P10}
\]
这是依赖 actual mirrorgraph 的 whole-X lower bound，不是其 exact valuation；零多项式亦合法。n-dependent Z_p GL 仅用于 finite-place 证明，原 S 的实处 determinant、范数和 source 全部不换。固定 source 分母照付 O(n)。

P10 比旧 Ω 更严格，但本文未声称对整个 mirrorgraph 求出了精确最优解。toric 本轮用 supported source bound 导出另一组全尺度 dual lower bounds；其 closed-cover 预算与本文 P10 要逐 prime 共同取max，不能加裸面积。

## P6. 一个无需全graph求解的正 paid window

取
\[
\frac{2n}{3}<p<\frac{17n}{24},\qquad p>5,\quad p^2>8n.
\tag{P11}
\]
这里 a2、Q4、h8，u=V=3p−2n 为 odd。unit packet 恰是完整 inner mirror packet；其 w0/q8 数目为 u。另有 w3/q8 数 8n−11p+1，w5/q7 数 9p−6n−1。所有合法 r 的 local cost记
\[
F_{w,q}(r)=wr+4(r-2q)_++2(r-4)_+.
\]
以 λ3、η2 定价：F−3r−2·1_{r>4}。unit nonbig r≤4 最小为−12（r4）；unit big r>4 最小为−26（r16）。w3/q8、w5/q7 的最小值都是0。这些是分段线性有限整数区间的严格 inequalities，不依赖选中 jets injective。

一个 unit offcenter mirror pair，若两边都big，则总价≥−52，加 2f_B=4 后≥−48；只有一边big时≥−38，无big时≥−24。fixed residue loop 若big价≥−26，加2后≥−24；nonbig价≥−12。因此全部unit residues的 priced cost加2f_B至少−24u。

在 P10 中 −2min(R,|B|)≥−2|B|；Σr=2n。故 exact finite-n bound 是
\[
\Omega_p^{support}\ge6n-24u,\qquad
\boxed{v_p^{Gauss}D_A(X)\ge44n-72p.}
\tag{P12}
\]
u 精确为3p−2n，所以 P12 不漏整数边界常数。

## P7. 与487同一预算的严格比较

冻结 global Ω 的 saved closed-cover 记录，在整个 P11 上给已付主率
\[
g_{487}(x)=\max(48-78x,10-24x),\qquad x=p/n.
\tag{P13}
\]
前项是 λ3η2 Ω face；后项是 actual unit-sector DND。交点19/27。本文 g_support=44−72x，故相对现有487的共同max增量为
\[
g_{support}-g_{487}=
\begin{cases}6x-4,&2/3<x<19/27,\\34-48x,&19/27\le x<17/24.\end{cases}
\]
\[
\boxed{\int_{2/3}^{17/24}(g_{support}-g_{487})dx
=\frac1{243}+\frac1{1944}=\frac1{216}>0.}
\tag{P14}
\]
其它 places 保持487基线，只在 P11 使用旧合法整数 lower bound 与 P12 的 max。finite boundary 的旧误差统一 O(1)，每个 prime只付 O(log p)，故总误差 O(n)；有界分段仿射模型的 PNT 给真正的 n² 主率 P14。

487 signed rational normalization 的安全费用
\[
A_{487}^{safe}=\frac{68678357676574195925297901887}
{1702339643838709841383978560}
\tag{P15}
\]
因此在同一原 S 和 whole-X 对象下至少可降 1/216。这里仍是 D_A/Q_n∈Z[X] 的安全有理 scale 费用，包含正 content，不冒称最小整数 denominator 的实际下界。toric 本轮更广的 joint max包含 P14，不能再加1/216。strict margin 与无限 rational-target nonzero 仍未成立。

## P8. 阅读、验证与界限

本轮实际全文读：background §§133–137；e483 unit-sector U1–U10/equations U1–U21；b953 weighted W1–W10/equations W1–W14；1b792 global Ω O1–O11/equations O1–O20。全输出无截断。saved global Ω JSON全syntax parse、metadata、first2 complete records，以及 floors(Q,h,a2)=(4,8,2) 的8个 complete records实际阅读；不称113条逐条人工重算。没有旧/同行 producer execution/import，没有新的 primary 文献下载或新PDF页阅读。插值、约束独立、匹配、PNT及窗口定价的实际证明在上文。

自有 DISTINCT NEW [支撑 verifier](cdt_odd_paired_selected_jet_primitive_support_20261006_verify.py) 完整静态读取后首次且唯一执行1次，exit0 PASS；success1、failed0、rerun0、旧/同行 producer execution/import0、外部Lean0。guard 在数学运算前 exclusive-create 输出，失败会被保留。成功后 source/JSON 不改、不重跑。

它 literal 构造原 S、真实 primitive rows 和 selected jet matrices，6个(n,p)=(19,13),(27,19),(53,37),(10,11),(33,19),(55,41)，每case5种 selected-support profiles，17059checks。包括 derivative-only、unit-first、完整秩 negative-value minors，并得到12个“global-f任意扣除”失效的真实例子。例如(n,p)=(19,13)的 saved greedy value minor 在原 S 上 rank38、旧 coefficient cap38、f_global1、f_B0；错误扣全局f会断言rank≤37。全尺度定理不依赖这些 finite cases。

程序同时逐整数r核 window定价、36个旧λ/η face 的端点支配与 exactFraction gain1/216。它不计算辅助 prime units或新增其表。成功后全JSON syntax parse；所有metadata、30个profile的全部字段/每条node-type label、12counterexamples、36face及gain字段已实际读取。前两次 verbose输出截断，随后以显式v=value、d=scaled_derivative编码补全全部30records；不将截断输出冒记成完整读取，也不称17059asserts逐条人工重新运算。

已证：支持在 big coefficient source 上的真实 primitive constraints、任意 selected row rank cap、左右node匹配下的双份约束费用、exact finite-n P12、相对487的实付1/216。仍缺：selected arbitrary-support exact image/Smith、全graph最优、足够解析–算术严格margin、无穷实际目标非零。没有新的 ζ/L/Catalan 无理性或线性无关性数值定理，没有外部Lean执行。

本文候选，待独审后冻结；所有487旧输入保持不改。
