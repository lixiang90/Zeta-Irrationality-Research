# 同一配对格在 n/2<p≤n 的完整第二 Smith 层

2026-10-06，NEW 纸面候选，尚待独立审阅。全部旧/同行数学 producer 仅读，未执行、import 或重跑。本稿研究冻结同一 B6/k3/s5 的 primitive paired C!，没有更换整数格或约除新 gcd。

## S1. 全尺度候选结论

设 n≥1、p 为素数，n/2<p≤n、p²>8n、p>17。令

\[
K=2n-1=ap+z,\quad0\le z<p,\qquad
6n+1=hp+e,\quad\tau=p-e.
\tag{S1}
\]

此处 a∈{1,2,3}、h∈{6,…,11}。记

\[
\begin{aligned}
M_H&=\max\{0,\min(\tau,z+1-\tau,\lfloor(z+1)/2\rfloor)\},\\
M_T&=\max\{0,\min(\tau-z-1,p-\tau,\lfloor(p-z-1)/2\rfloor)\},\\
M&=M_H+M_T,\qquad M_4={\bf1}_{a=3}M_H.
\end{aligned}
\tag{S2}
\]

M 是不同 carry 的 offcenter mirror residue blocks 个数，M₄ 是其中每个 residue 都有四个实际 lifts 的个数。本稿证明真实 C! 的完整 p-adic Smith valuations 为

\[
\boxed{0^{p-M},\quad
1^{n-p+M-M_4},\quad2^{M_4}.}
\tag{S3}
\]

因而 δ_p=v_p I_n(C!)=n−p+M+M₄。它是全尺度 exact Smith 声明，不能仅从第一层图的 rank 推出；其 upper bounds 在 S9–S13 显式构造。

## S4. actual primitive 约束与同一 Plücker 对象

按冻结 [dual-carry稿](cdt_odd_paired_dual_plucker_carry_rate_20261006.md) D1–D7，取 degree<2n 的低 Newton 块。对 head sites k=0,…,K，令 d_k=(k+1)_{6n+1}，对镜像 k'=K−k 以 gcd(d_k,d_k') 约除，primitive 方程是

\[
q_k P(k)-p_kP(k')=0,
\quad q_k=d_{k'}/\gcd(d_k,d_{k'}),\quad
p_k=d_k/\gcd(d_k,d_{k'}).
\tag{S4}
\]

这里将 polynomial 变量从原 t 移到 k=t−1；integer coefficient translation 是 GL。C!:C diag(j!) 的第 j 列为 q_k(k)_{\underline j}−p_k(k')_{\underline j}。falling 到 monomial 是 integer unitriangular，所以 image 正是同一个 integer-coefficient degree<2n polynomial 的 primitive evaluations。原全素数实际量仍是

\[
T_p=\sum_{i=0}^{3n-1}v_p(i!)-\delta_p.
\tag{S5}
\]

因此相对冻结 largest2n 安全 factorial 费，本窗口的可用两侧改善是 2(δ_p−(n−p))=2(M+M₄)，不是 2δ_p。必须先减已付的 Σ_{i<n}v_p(i!)=n−p。

## S6. 整 CRT 分块与真实 degree cutoff

对 residue r=0,…,p−1，实际 sites 为 r+lp≤K，l=0,…,L_r−1。令 Q_r(t)=∏_{l<L_r}(t−r−lp)。不同 Q_r 的 resultant 是 residue unit，因此它们在 Z_p[t] 中 comaximal。monic division/CRT 给出

\[
Z_p[t]_{<2n}\simeq\bigoplus_r Z_p[t]_{<L_r}\pmod{Q_r}
\tag{S6}
\]

的真正 GL_{2n}(Z_p) 模型，没有额外 local index。每个局部用 monic step-Newton 基

\[
B_{r,j}(t)=\prod_{b=0}^{j-1}(t-r-bp),\quad0\le j<L_r,
\qquad B_{r,j}(r+lp)=p^j j!\binom lj.
\tag{S7}
\]

它保留 L_r=a+1 对 r≤z、L_r=a 对 r>z 的实际 ragged cutoff。此窗口 L_r≤4<p，故 j! 均 unit，packet costs 恰0,1,2,3。

特别 modp² 只剩局部 j0,j1，且每个 residue 至少两个 lifts（a1仅 p=n，此时全部 L2）。image 上的 degree cutoff 允许完整 value/first-jet packet。这个完整性来自 2n≥2p 或 S6 的 actual local lengths，不是免费增加第三层或删掉原 degree bound。

mirror r↦z−r modp 保持 r≤z 和 r>z 两组；offcenter 两个 residues 的 L 相等，mirror lifts 恰 l↦L−1−l。唯一 center residue 的 L 为偶数，即2或4。primitive constraints 因此按每个 orbit 独立直和。父任务的 NEW CRT 接口可给同一分块的全prime版本；本节自证仅取本稿需要的有限窗口。

## S8. 去 p 单位与未知一阶 lifts 的界线

令 c(r)=1_{r≥τ}。p²>8n 保证所有 factorial arguments<p²。Wilson stripping 给

\[
v_pd_{r+lp}=h+c(r),\quad
p^{-h-c(r)}d_{r+lp}\equiv A_r f_{h+c(r)}(l)\pmod p,
\]
\[
f_H(l)=\binom{H+l}{l},\qquad
A_r=(-1)^{h+c(r)}(h+c(r))!
\frac{(r+e-c(r)p)!}{r!}\in F_p^\times.
\tag{S8}
\]

H≤12，l≤3，所以 f_H(l) 中的 factorial indices≤15<p；A_r 中剩余 factorial arguments 亦小于p。不同 residue 的 A_r 可通过 column-unit normalization 吸收；不同 pair 的 gcd-unit 可通过 row-unit normalization 吸收。以下 leading calculations 因而不改变实际 Smith valuations。

本稿没有假定 unknown stripped units modp² 等于其 modp leading。upper-bound minors 中 p^j 已逐 column 提出，其最低项只使用 S8；mixed block 第一列还可用实际 unit coefficient 精确归一化为1。未计的一阶 unit corrections 不会被误删。

## S9. same-carry 两 residue blocks：L2、L3

令 H=h+c。leading value columns 是 f_H(L−1−l)、−f_H(l)。L2 的 determinant 是单位倍 ((H+1)²−1)=H(H+2)，因此 Smith=(0,0)。

L3 用中心坐标 x=l−1。令 E=f+f_rev（even）、O=f−f_rev（odd）。value columns 生成 E,O，slope columns 的 leading p-quotient 生成 xE,xO（加 value columns 的常数倍不影响）。odd subspace 一维，O 的端点差为 1−f_H(2)=−H(H+3)/2；even subspace 的 E_mid=2(H+1)，而 xO_mid=0 且端点非零。三列 independent，所以选两个 value、一个 p-slope minor 的 valuation 恰1。modp rank为2亦给 lower≥1，故 Smith=(0,0,1)。

## S10. same-carry L4 的两个 unit 因子

设 x=l−3/2。even 和 odd subspaces 各二维，value/slope 四列等价于 E,O,xE,xO。用位置 l0,l1 表示两维，写

\[
E_0=\frac{(H+4)(H^2+2H+3)}6,\quad
E_1=\frac{(H+1)(H+4)}2,
\]
\[
O_0=-\frac{H(H^2+6H+11)}6,\quad
O_1=-\frac{H(H+1)}2.
\]

对应 even pair (E,xO) 与 odd pair (O,xE) determinants 为

\[
\det_{\rm even}=-\frac{H(H+1)(H+3)(H+4)(H+5)}{12},
\]
\[
\det_{\rm odd}=-\frac{H(H-1)(H+1)^2(H+4)}{12}.
\tag{S9}
\]

H6..12，p>17，使上述全部 factors 为 units。故四列（两 value、两 p-slope）minor valuation恰2。modp rank2 强制≥2，所有 Smith非负，得到 (0,0,1,1)。这不使用目标 B_X Gram unit；只是 C! 的真实 image。

## S11. different-carry L2、L3 的实系数归一化

把 carry较大的 residue 放在 high side。primitive row 的 high coefficient 是实际 unit，low coefficient 是 p·unit。逐 row 除 high unit 后，局部矩阵 columns 有

\[
\mathbf1,\quad p\,l,\quad
-p\,\Gamma_l,\quad -p^2(L-1-l)\Gamma_l,\quad
p^2l(l-1),\ldots,
\tag{S10}
\]

其中 Γ_l 是实际 Z_p unit，reduction 为某个与 l 无关的非零常数乘

\[
\gamma_l=
\frac{(h+l+1)!}{l!}\,
\frac{(L-1-l)!}{(h+L-1-l)!}.
\tag{S11}
\]

constant 可 column-unit 吸收。L2 的 columns 1,pl 直接给 valuation1 minor，modp rank1 给 lower1，所以 Smith=(0,1)。

L3 时 γ0=2/(h+2)、γ1=h+2、γ2=(h+1)(h+2)(h+3)/2，故

\[
\gamma_0-2\gamma_1+\gamma_2
=\frac{h(h+1)(h+3)(h+4)}{2(h+2)}\in F_p^\times.
\tag{S12}
\]

1,l,γ 的 rank 为3，实际 columns 1,pl,−pΓ 的 minor valuation恰2。modp rank1 给lower2，所以 Smith=(0,1,1)。

## S12. different-carry L4：真正第二层和上界

L4 的 γ 值依次是

\[
\frac6{(h+2)(h+3)},\quad2,\quad
\frac{(h+2)(h+3)}2,\quad
\frac{(h+1)(h+2)(h+3)(h+4)}6.
\]

前三点二阶差为

\[
\gamma_0-2\gamma_1+\gamma_2
=\frac{h(h+1)(h+4)(h+5)}{2(h+2)(h+3)}\in F_p^\times.
\tag{S13}
\]

因此 1,l,γ independent。modp rank1，所以至少三条 positive Smith 指数。消去第一 unit column 后，再除 p，modp 的剩余像只由 l 和 γ 的差产生，rank恰2；j≥2 columns 已有 p²，低一阶 column 也有 p²，actual Γ 的一阶修正不进入 modp²。因此三条 positive 指数中恰有一条≥2，determinantal ideal valuation至少4。

upper bound 不能只证明这一 rank。若 1,l,γ,l² independent，S10 的高二阶 column p²l(l−1) 给 valuation4 minor。若不 independent，则 γ 在四个互异点上是一个 non-affine quadratic polynomial（由 S13），所以 (L−1−l)γ 含非零 cubic leading coefficient，不在 span(1,l,γ) 中。此时改用真实 low first-jet column −p²(L−1−l)Γ，仍给 valuation4 minor。所有这一组 columns 都在 actual CRT cutoff 内。

故 lower与upper相遇，完整 Smith 恰为 (0,1,1,2)。不必假设 γ 的三阶差为 unit；例如该差可能含素数43或179，本稿的两种 column choice 消除了这一多余条件。这一步也严格区别 second-layer rank 与 determinant equality。

## S13. center loops 不产生额外 second layer

center 的 L 必为2或4，pair rows 取 l<L/2。L2 的 value difference f_H(1)−f_H(0)=H 是unit，所以唯一 Smith为0。

L4 的两个 rows l0与l1，value leading列是

\[
v=(f_H(3)-1,\ f_H(2)-f_H(1)),
\]

first-slope leading p-quotient 是

\[
w=(-3,\ f_H(2)-2f_H(1)).
\]

其 determinant 为

\[
\det(v,w)=\frac{H(H-1)(H+1)^2(H+4)}{12}\in F_p^\times.
\tag{S14}
\]

modp rank1、该实际两列 minor valuation1，故 loop Smith=(0,1)。所有 first-order actual unit corrections 已被该提出p的最低 determinant 项覆盖。

## S15. 全块接合、精确计数与 small-prime fallback

same-carry offcenter Lrows 的 modp rank2，different-carry 为1；center rank1。全部 p 个 residues的最大 value rank合计p，每个不同carry offcenter损失1，所以 zero Smith数为p−M。S9–S13证明只有 L4不同carry多一条指数2，其余正指数全为1，因而 S3 成立。

对 head r0..z，mirror是z−r；different-carry lower r恰满足 r<τ≤z−r。计数是S2的M_H。对 tail r>z，mirror为p+z−r；平移r↦r−z−1后得到M_T。L4只在a3的head，所以M4=1_{a3}M_H。center不会被误计为offcenter。

p≤17 的有限primes在 p>n/2 下只有n<34；若本窗口未满足p²>8n，亦只是原全n费用模型的非covered部分。本稿不在那里声称 exactS3，完整全prime整化保留冻结entry cap和oldlegalbound。固定有限p/n例外付O(nlogn)或更小，不改任何已证PNT主率。

## S16. 算术预算接口：只能支付穿过 cap 的收益

S5给 same whole-X bound

\[
v_p^{\rm Gauss}D_A(X)\ge\Lambda_p-2T_p^{\rm safe}+2(M+M_4),
\tag{S15}
\]

还必须与原合法 −10n entry bound取max。这是原 actual primitive S 的费用，不再另扣gcd，且所有X系数适用。

本轮另实际全文读 [credit-cap稿](cdt_odd_paired_smith_credit_cap_transfer_20261006.md) 候选5548fcf69b24f2bab4d3ff9c2ef0023cb594e749e32ff8affc863160d0174647，尤其S4–S8的uniform计数、完整12个raw affine段和cap比较。S3本身没有把2M4裸面积当主率：它只在1/2<x=p/n<2/3的head mixed support上出现。写 d_4=[min((h+1)x−6,8−(h+4)x)]_+，则原raw加完整层信用4d_4在h11、10、9三段的最大值分别为

\[
-280/27,\quad-314/25,\quad-330/23,
\]

全部严格低于−10（顶点分别14/27、14/25、14/23；跨原raw分段后也作两端比较）。因此全尺度S3给出的M4信用，经过当前合法entry cap后，新增paid主率确实为0，uniform O(1)离散误差不改变PNT主率。

该credit-cap稿的第一层已独立给 ΔA=121537/4476780；与前轮不交窗口接合的safe A为790225879771/17925027120。本稿不重复计这份信用，不将作者的有限证书当作自己执行。本稿真正增强的是actual C!的exact上层结构，费用接合保留same whole-X对象；不存在新的matched margin或actual cost下界。

## S17. 当前来源与验证范围

本轮实际全文读取冻结dual-carry最终0fb995f、主报告§§116–120；仅读冻结probe JSON中n/2<p≤n的13个已存案例全部Smith字段，未运行其源。它们显示过指数2，但不能证明本稿S3。另实际全文读父代理本轮 NEW [CRT稿](cdt_odd_paired_residue_crt_integral_model_20261006.md) R1–R21：其全prime局部整GL、实际primitive blocks和容量下界与本稿一致；本稿S9–S13另外完成这个窗口的全部上层units与exact equality。

自有 NEW `cdt_odd_paired_second_smith_layer_20261006_verify.py` 执行前实际全文静态核读，首次且唯一一次运行，退出码0。guard先创建输出，禁止再次运行；程序不读取旧/同行数学输入。从 d_k=(k+1)_{6n+1} 的完整 integers及真实gcd独立构造每个CRT block，用Fraction最小valuation pivot/actual Schur complement计算全部Smith；并未删去modp²的单位修正。覆盖n18..64、p>17、n/2<p≤n、p²>8n的216cases、3977blocks，4625项断言全部PASS。PY SHA17d76f57b1ae6e8f26ecadc21036a71567759177ca01f2f1fdbccaed00f4e806，JSON SHA516d84723f0a827dfafea94eb28db7917ffd1b2a45157b9b7adbdc154acff735；实际完整核读源码和全部216cases的全部输出字段（外层首次合并输出截断后单独补全）。这些只证明有限实现机制，S3的全尺度证明是上文纸面论证。

本轮新PDF归档0、本人本轮primary PDF实读0页。纸面CRT、Wilson、unit minors和second-layer机制自足；没有把别人的实际阅读计入本人，也没有将新增PDF0写成对旧source未读的替代。source receipt另存NEW，所有旧/同行 producer执行/import/rerun均为0。

S3没有证明actualD_A在任何目标无限nonzero，没有使Padé缺陷自动为0，也没有新的ζ/L/Catalan无理性或Lean结论。它解决的是本素数窗口 C! 的完整实际Smith层；p≤n/2的高层仍未覆盖。
