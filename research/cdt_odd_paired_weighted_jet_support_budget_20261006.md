# 真实整数值 jet 支撑的联合加权 minor 界及可兑现主率

2026-10-06，root，NEW 纸面推导。455 个既存冻结数学输入及所有旧/同行 producer 只读；本稿不改变 B=6、κ=3、s=5、degree<3n、rank2n 的实际饱和配对格。此稿给整个 X 多项式的新有限素数下界，并在新的一层 unit-tail 界之外严格再兑现 1/84 的 n² 信用；未证明新的特殊值无理性或无限目标非零。

## W1. 同一个行列式和输入

记 L=A_n∩⊕_{i<3n}Z binom(t−1,i)，其完整基为上一轮严格给出的 G_m 与 f_{2n},…,f_{3n−1}，rank d=2n。实际形式是
\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,
\quad U_j=-8aH_j^{(3)}-6bH_j^{(4)},
\]
\[
V_j(X)=(5H_j-3H_{2n+j}-2H_{6n-j})U_j
 +24(X-aH_j^{(4)}-bH_j^{(5)}).
\tag{W1}
\]
取整数 a,b，b≠0，X 形式变量，D_A(X)=det B_X|_L。固定有理 a,b 先乘固定公共分母，只付 O(n)；不得免费改变 n-dependent 基。以下 valuation 一概为 Q[X] 的 Gauss valuation，不要求任一 specialization 非零。

本轮实际全文读取：arithmetic cost A1–A14、primitive review P1–P9、head-free lattice I1–I25、all-prime budget B1–B22、auxiliary prime A1–A13、Jacobi K1–K26、上一轮 credit-cap S1–S10；最终 receipt 实际登记指纹。所有旧 PY/JSON 仅读，不执行。下面的 local proof 自足，不套原共同 monomial-minor Λ_p 与独立最大 wedge 费用。

## W2. 整数值 ψ 基及 scaled derivative

设 p>5、p²>8n、p≤6n。写
\[
3n=Qp+R,\qquad0\le R<p,\qquad \psi(t)=(t^p-t)/p.
\]
对 i=i_0+pi_1<3n，令 b_i(t)=binom(t,i_0)binom(ψ(t),i_1)。它在每个整数上为 Z_p 值，degree i，leading coefficient 是 1/(i_0!i_1!p^{i_1})。因为 i<p²，v_p(i!)=i_1，i_0!,i_1! 都为 units，故与 binom(t−1,i) 的三角变换对角全部为 units。于是这是原 ambient 格的 GL_{3n}(Z_p) 基；不是扩大为自由 residue/jet 格。

每个 P∈ambient 都有 P(z),pP'(z)∈Z_p（整数 z）。后者也可由 pD_i^{-1} 与 p²>i，或直接对 b_i 求导证明。令 c∈F_p、v=ψ(z) mod p，z≡c，则
\[
P(z)\equiv g_c(v),\qquad pP'(z)\equiv-g_c'(v)\pmod p.
\tag{W2}
\]
因为 pψ'(z)=pz^{p−1}−1≡−1，低 digit 因子的 p 倍导数模 p 为0。这里 g_c degree≤Q；前 Q 层的每个 residue coefficient 独立，最后第 Q 层只有 R 维低 digit 多项式值。Q<p，binom(v,i_1) 是普通单位三角 polynomial basis。

## W3. 指定 jet-row minor 的真实 rank 费用

令 Y 是把任一完整 L 基送到所有 nodes j=0,…,6n 的两行 (P(-j),pP'(-j)) 的整数矩阵。选 d 行 I，按 j≡ρ mod p 记选取数 r_ρ，Σr_ρ=d。设 K(r)=#{ρ:r_ρ>Q}。由 W2，
\[
\operatorname{rank}_{F_p}Y_I\le
\sum_\rho\min(r_\rho,Q)+\min(R,K(r)).
\tag{W3}
\]
证明：先将 r_ρ≤Q 的全部 rows 当作至多 r_ρ 个自由贡献；其余 blocks 的前 Q 层至多每 residue Q 维，最后层在每个 block 至多一条列方向，且总 coefficient dimension R，故其贡献至多 min(R,K)。限制到实际 L 只会减小 rank。这一证明不要求每个局部 evaluation/derivative minor 都独立，也不假设 Gram 正常。

对任意整 d×d 矩阵，mod p rank≤r 蕴含 determinant 被 p^{d−r} 整除（Smith 或 unit row elimination）。所以指定 Y_I 有
\[
v_p\det Y_I\ge d-\sum_\rho\min(r_\rho,Q)-\min(R,K(r)).
\tag{W4}
\]
这正把 degree cutoff、ragged top layer 和同一个指定 minor 保留下来；没有先用最差 factorial 转到 monomials。

## W4. 实际 node-block 的权重

令 M=p^5B_X|_L。它准确等于 Y^tAY，其中 A 是 j-node 的 block diagonal matrix，
\[
A_j=W_j\begin{pmatrix}p^5V_j(X)&p^4U_j\\p^4U_j&0\end{pmatrix}.
\tag{W5}
\]
所有 coefficients 整。写
\[
q_\rho=\lfloor(6n-\rho)/p\rfloor,
\quad w_\rho=2\lfloor6n/p\rfloor-2q_\rho
 +3\lfloor(2n+\rho)/p\rfloor-3\lfloor2n/p\rfloor.
\]
Legendre 给 j=ρ+lp 时 v_p(W_j)=w_ρ∈{0,2,3,5}。l≥1 的全部 entries valuation≥w_ρ；l=0 的 U_ρ integral、V_ρ≥−1，故 entries≥w_ρ+4。ρ=0 有更高 divisibility/较低 rank，以下仍取这个安全弱界。

A 的非零 minor 必须在每个 node 左右选相同数 l_j∈{0,1,2}；否则 block diagonal permutation 展开没有 perfect matching。因此左右的 residue counts 都是同一 r_ρ。其 node-block valuation 至少
\[
\sum_\rho\{w_\rho r_\rho+4(r_\rho-2q_\rho)_+\},
\qquad 0\le r_\rho\le2q_\rho+2.
\tag{W6}
\]
只要尾节点容量不足，超过的每行必来自 head；左右同 node 数已保证真正的 block-minor 权重，不把它当两个独立 packet 优化。

## W5. 全尺度 whole-X 联合界

两次 Cauchy–Binet、W4、W6 给
\[
\Omega_p=\min_{\substack{0\le r_\rho\le2q_\rho+2\\\sum r_\rho=2n}}
\left[\sum_\rho\{w_\rho r_\rho+4(r_\rho-2q_\rho)_+
                 +2(r_\rho-Q)_+\}
       -2\min(R,\#\{\rho:r_\rho>Q\})\right],
\tag{W7}
\]
\[
\boxed{v_p^{\rm Gauss}D_A(X)\ge-10n+\Omega_p.}
\tag{W8}
\]
优化非空，因为全节点 jet capacity=2(6n+1)>2n。每项的 degree-rank 部分非负，Ω_p≥0。此界可与每个既有同对象的合法 finite-place 界取 max，并保留正 content。它不要求 G0/M5 units，也不声明 Ω_p 是 actual determinant valuation 或最优 content。

W7 的最后信用至多 R，且每个 r_ρ>Q 只能得一次。可用整数 DP (总行数,已用信用) 精确计算：某 block r>Q 可选 credit 0/1，local cost减2，global credit≤R。未证明它是一个普通无约束 greedy；不把最后一层的共享秩免费复制给每个 residue。

## W6. 一个无需数值搜寻的明确新付区间

取
\[
\frac{31n}{42}<p<\frac{3n}{4},\qquad p^2>8n,
\tag{W9}
\]
则 Q=4、R=3n−4p，floor(6n/p)=8、floor(2n/p)=2。令 c=6n−8p、t=3p−2n；此区间 c<t。各 type 的**精确整数数目**为
\[
u=c+1=6n-8p+1\quad(w=0,q=8),
\]
\[
v=t-u=11p-8n-1\quad(w=2,q=7),
\]
\[
z=p-t=2n-2p\quad(w=5,q=7).
\tag{W10}
\]
没有 w3 type。以下三个 inequality 对全部合法 r 直接成立：
\[
2(r-4)_++4(r-16)_+\ge4r-40,
\]
\[
2r+2(r-4)_++4(r-14)_+\ge4r-8,
\]
\[
5r+2(r-4)_++4(r-14)_+\ge4r.
\tag{W11}
\]
分别在 r=16、r∈[4,14] 饱和；边界段斜率直接检查。将 W7 的 credit 放宽为≤R，仅削弱下界，得
\[
\Omega_p\ge4(2n)-40u-8v-2R
              =240p-174n-32,
\]
\[
\boxed{v_p^{\rm Gauss}D_A(X)\ge240p-184n-32.}
\tag{W12}
\]
这是实际行列式的新 finite inequality，−32 是已付整数边界，不能丢掉后称 finite-n 精确等式。

## W7. 相对于新一层界的真正额外 1/84

在 W9，unit-tail ambient coefficient-image dimension≤4u+min(R,u)=4u+R，因为 u=2R+1。故新一层 whole-X DND 界是
\[
v_pD_A\ge-10n+2(2n-4u-R)_+
             =72p-60n-8.
\tag{W13}
\]
该区间正部为正。归一化为 x=p/n，W12、W13 主率分别为 240x−184 与72x−60，新 gain=168x−124>0。上一轮此段 raw=54x−48、实付 first-Smith 后=38x−36，新 DND 的72x−60严格较大；所以这项不是被旧 cap 或旧 Smith 信用吞掉的裸面积。M4新增信用不在此段；大素数窗口也与 W9 不交。

所有有限整数误差 uniform O(1)，p≤sqrt(8n) 保持旧界。PNT 在固定窗口给
\[
\int_{31/42}^{3/4}(168x-124)\,dx=\boxed{1/84}.
\tag{W14}
\]
于是把 W12 与本轮 p≤n 的新一层界逐 prime 取 max 后，在其已证费用上界之外**至少再减 1/84**。不能将 W7 在整个 (0,6) 的未知最优积分也计入；本稿仅严格兑现 W14。与同行同窗口的新估计要先取 max，绝不能直接相加裸 gain。

## W8. 为什么这比独立最差转移更强

W4 依赖指定 jet rows 的同一 r_ρ，W6 在 A minor 的左右匹配中保持该 r_ρ。w2/w5 与 unit-row 超出 Q 的 rank 费用因此共同付账。特别 W11 说明 w2 在前4个 rows 后增加到每行4，而 w5 至少每行5；仅用“非unit至少p²”会丢掉这个区别。这是新的支撑相关估计，未使用任何 Gram inverse 或目标非零。

要进一步推进，可保留 derivative-row 常数方向的更小 rank、ρ=0真实rank1、p²及更高 jet Smith 费用，或使用 actual paired image 的维数替代 W3 的 ambient cap；均须重新证明同一支撑模型。

## W9. 一手文献与不能直接套用的范围

正常 verified TLS 新归档 [Grinberg–Petrov, A greedoid and a matroid inspired by Bhargava’s p-orderings](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v28i3p6)，EJC28(3)(2021),P3.6，DOI10.37236/9046。本地原件 [PDF](../literature/grinberg_petrov2021_greedoid_matroid_p_orderings_ejc_20261006.pdf)，36页、502160bytes，SHA2787a79515efb6bff9078eeef1d5780eb42cab83f4409d3c6337fe139613a841。

本轮实际完整读 PDF1–4、10–14、31–33，共12distinct页，没有称全文36页。Theorem21及PDF12–13证明给 ultra-triple perimeter 的 greedy 最大性质；PDF31–33将 d=−v_p(a−b) 与 P-ordering 连接。这提示继续用支撑组合结构记录 valuation，但本 W7 的 Hermite rows、ragged信用和 block匹配尚未构造成该 ultra-triple，故不引用其定理来证明 W7 的最优性。W2–W14均为本稿独立证明。

PDF31提到 valuation 加法时印成 v(a+b)≤max{v(a),v(b)}，这不是通常 p-adic valuation 的正确公理；本稿使用 v(a+b)≥min{v(a),v(b)}，没有采用该误印。也未从它推特殊值定理。

## W10. 验证和剩余研究门槛

NEW [first-only 程序](cdt_odd_paired_weighted_jet_support_budget_20261006_verify.py) 保存后实际完整静态读取；首次且唯一执行1次，exit0、PASS，失败/重跑/旧同行execute/import均0。source SHA36112ffcb950479e89a1744ee35721770f8216cd96b7352d7c9b785ad5e40932；[JSON](cdt_odd_paired_weighted_jet_support_budget_20261006_verify.json) SHA bb3ceac4bb22ac030fbf8ed43337738b70b0af3fdf7f687147862e5f1b7a4eba，成功后不改、不重跑。

它独立检查 W7整数DP、W10实际type计数、W11全部有限r、实际paired Newton基的指定jet矩阵 modp rank及W14 exactFraction积分；记录1425项计数检查，三个(n,p)是(23,17)、(31,23)、(55,41)。实际完整saturated basis modp秩分别46、62、110；所选真实jet矩阵rank为16、22、40，不超过纸面cap21、29、53。weighted Ω为66、98、238；最后case比一层194多44，前两case有限边界下不强于一层。程序不算实际Gram determinant，更不把单一有限case称全素数收益。纸面 W12 的−32仍保留。

成功后实际 parse 整个JSON，读取全部metadata、三case的全部allocation/费用/rank字段及rowlabels首尾；没有声称逐条人工回算全部selected rows。完整执行史和scope写最终receipt。有限机制证据不替代纸面全尺度证明，也不证明 actual G0/M5 infinite units。

本轮此稿推进的是同对象、whole-X、新 paid all-prime费用。当前解析率仍只有>12.003572854…，strict arithmetic–analytic margin仍未建立；无限实际目标非零仍待补。没有ζ(7)、Catalan或ζ/L新的无理性/线性无关性结论，没有新增Lean执行/定理。
