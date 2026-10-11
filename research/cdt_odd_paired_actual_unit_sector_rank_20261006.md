# 真实配对格的 unit-tail 精确像秩与镜像约束信用

2026-10-06，NEW，quarter_actual_rank。基线471数学输入及全部旧/同行数学 producer 冻结只读；本文不改原 S、原 B6/k3/s5、degree<3n 或 whole-X determinant。新的局部坐标只用于 finite-place 证明，不把其 unimodular 性当作实处范数费用为零。

## U1. 对象与已证结论

原整数值格及真实配对格为

\[
M_{3n}=\bigoplus_{0\le i<3n}\mathbf Z\binom{t-1}{i},\qquad
A_{n,\mathbf Z}=\{P\in M_{3n}:P(m)/d_m=P(c-m)/d_{c-m},\ 1\le m\le n\},
\]
\[
c=2n+1,\qquad d_m=(m)_{6n+1}=\frac{(6n+m)!}{(m-1)!}.
\tag{U1}
\]

取 frozen lattice I8 的完整整数基 S：G_m=p_mL_m+q_mL_{c-m}，以及全部 f_i，2n≤i<3n，其中

\[
g_m=\gcd(d_m,d_{c-m}),\quad p_m=d_m/g_m,\quad q_m=d_{c-m}/g_m.
\tag{U2}
\]

D_A(X) 仍是冻结 form 在这个 S 上的 rank2n determinant。固定有理 sources 先清同一固定分母，其费用 O(n) 在实处、有限处共同保留。以下所有估值逐 X 系数成立。

设 p>5 为 prime，p≤2n、p²>8n，记

\[
2n=ap+r_2,\quad3n=Qp+R,\quad6n=hp+r_6,
\quad0\le r_2,R,r_6<p,
\]
\[
V=p-r_2,\quad u=\min(r_6+1,V),\quad b_0=(2u-V)_+,
\quad f=au-\frac{a b_0}{2}.
\tag{U3}
\]

f 是整数；下文给出其实际约束计数。unit-tail map 定义在原 A_Z/pA_Z 上，取全部 p≤j≤6n、v_p(W_j)=0 的 (P(−j),pP′(−j))。它的实际像秩记 d_actual，核维数记 k。

**定理。** 对上述所有 p，有

\[
\boxed{d_{actual}\le Qu+\min(R,u)-f.}
\tag{U4}
\]

若 Q≥a+1，则有准确等式

\[
\boxed{d_{actual}=Qu+\min(R,u)-f,\qquad
k=2n-Qu-\min(R,u)+f.}
\tag{U5}
\]

特别 p≤n 一律满足精确等式；n<p≤3n/2 亦满足。对 3n/2<p≤2n 本文只证明 U4，不将有限验证中的现象提升为 exact rank。用真实弱格 DND 接口，有

\[
\boxed{v_p^{Gauss}D_A(X)\ge-10n+2[2n-Qu-\min(R,u)+f]_+.}
\tag{U6}
\]

这补的是 actual paired image，强于 frozen 150bb 的 ambient rank cap；不需要未知有限域 Gram unit、辅助素数无穷 normality 或 D_A(c) 非零。U6 本身也不证明这些条件。

## U2. 饱和格使模 p 约束充分，而非仅必要

头部 evaluation E:M3n→Z2n，P↦(P(1),…,P(2n))，前2n个 Newton 向量的矩阵 lowertriangular diagonal1，后n个向量在头部为零，故 E 是整数 split surjection。除掉 g_m 后，primitive constraint 是

\[
C_m(P)=q_mP(m)-p_mP(c-m)=0.
\tag{U7}
\]

在头部 evaluation 坐标中，各 pair 互不相交，gcd(p_m,q_m)=1，所以 C: M3n→Zn 满射。其 kernel 正是 A_Z，且短正合列 split。故

\[
A_Z/pA_Z=\ker(\overline C:M3n/pM3n\to\mathbf F_p^n),
\qquad\dim A_Z/pA_Z=2n.
\tag{U8}
\]

这一步确保下文构造的 ambient mod-p 解都能在**原 S 坐标**中 lift 为 exact characteristic-zero paired polynomial。没有将满足模 p raw equation 的多项式自动当成饱和格；先用实际 gcd 和整数满射给出了充分性。

## U3. 真整数值 ψ 坐标与不能增加的最后一层

取 ψ(t)=(t^p−t)/p。原 M3n⊗Z_p 的真实 GL 基是

\[
b_i(t)=\binom{t}{i_0}\binom{\psi(t)}{i_1},\qquad i=i_0+pi_1<3n,\quad0\le i_0<p.
\tag{U9}
\]

实际 GL 证明如下：i<p²，i0!,i1! 为 p-units，ψ(Z_p)⊂Z_p，b_i integer-valued。有限差分展开到 binom(t,j) 的系数都在 Z_p；highest coefficient 比为 i!/(i0!i1!p^i1)，其 valuation=floor(i/p)−i1=0。按 degree 的 triangular 变换为 GL3n(Z_p)，t→t−1 再给原整数 unitriangular 变换。未换成普通 coefficient CRT 格。

模 p 时，每个 residue r 上可写 local polynomial Φ_r(Y)，Y=ψ(t)，degree≤Q。底部 Q 个 coefficients 是任意 residue functions；顶层 coefficient 来自一个 degree<R 的 low-digit polynomial。R=0 时顶层不存在。于是任意 u 个不同 residues 上的 local coefficient space B_U 维数准确为

\[
d_{amb}=Qu+\min(R,u).
\tag{U10}
\]

底层是完整 Vandermonde evaluation 的 p 个自由值；顶层 restriction rank 为 min(R,u)，没有给每个 residue 免费加一个 top coefficient。固定顶层后，底层依然可在各 residue 独立取值，这正是后续 outside-head 延拓所用的自由度。

对整数 z 及 Y0∈Z_p，二项展开给

\[
\psi(z+pY_0)\equiv\psi(z)-Y_0\pmod p,
\qquad p\psi'(t)\equiv-1\pmod p.
\tag{U11}
\]

low-digit factors 的导数乘 p 为零，因此 P(t) 与 pP′(t) 模 p 分别是 Φ_r(ψ(t)) 与 −∂YΦ_r(ψ(t))。这保留原 degree<3n，不能换成更大的自由 jet 空间。

## U4. unit-W tail 与实际头部 carry 势差

原 W_j=binom(6n,j)^2 binom(2n+j,j)^3。对 j=ρ+lp，large-prime Legendre identity 给

\[
v_p(W_j)=2\mathbf1_{\rho>r_6}+3\mathbf1_{\rho\ge V}.
\tag{U12}
\]

unit residues 准确为 ρ=0,…,u−1，包含 ρ=0 与 r6=0 的端点。每个这样的 residue 具有 tail j=ρ+lp，l=1,…,h。h<p，由 p²>8n 得；且 h=floor6n/p≥2Q≥Q+1，因为 p≤2n 使 Q≥1，Q=1 时 h≥3。不同 l 给不同 ψ-values，所以完整 tail evaluation 为零当且仅当该 residue 的 Φ 完全为零，随后其 scaled derivative 也为零。

因此 actual unit-tail Hermite map 的秩正是 A_Z/pA_Z 到 B_U 的像秩，不需以单点 value 为零推出 derivative 为零。

注意 negative pole residue ρ 对应的 positive head residue 是 **t=m≡−ρ(mod p)**，不是 m−1。ρ=0 时 head 是 p,2p,…,ap；ρ>0 且 ρ<V 时 positive residue p−ρ>r2。故所有 inner residues 0≤ρ<V 恰有 a 个 positive head sites；其余 outer residues V≤ρ<p 恰有 a+1 个。这些 sites 的 ψ-values 互异，因 a+1<p（2n<p²/4）。

从 d_m 的实际 factorial 直接算，而非从 W_j 反推：写 m=lp+t，0≤t<p，则

\[
v_p(d_m)=\left\lfloor\frac{m+6n}{p}\right\rfloor-
\left\lfloor\frac{m-1}{p}\right\rfloor
=\begin{cases}h+1,&t=0\text{ 或 }t\ge p-r_6,\\h,&\text{其他。}\end{cases}
\tag{U13}
\]

所有 factorial endpoints≤8n<p²，所以没有遗漏 p² 层。以 ρ=−t 表示，准确高 carry 条件就是 ρ≤r6，包含 ρ0。尤其 unit sector 中全部 d_m 都有 valuation h+1。

## U5. 镜像在 inner packet 上的动作及独立约束数

positive reflection m↦c−m 在 inner rho packet 0,…,V−1 上是

\[
\sigma(\rho)=V-1-\rho.
\tag{U14}
\]

因为 −(c−m)≡−(r2+1)−ρ≡V−1−ρ。它把各含 a 个实际 head sites 的 cluster 双射配对；outer packet 在自身反射，含 a+1 个 sites，与 inner 不混。

unit cluster 与其镜像有两种情况。

* 镜像亦在 unit sector：两边 d_m 的 valuation 都为 h+1，primitive p_m、q_m 都是 p-units。每个实际 head pair 留下一条两侧 value 的非零线性约束。
* 镜像在 inner packet 的 nonunit 部分：镜像 ρ>r6，d_m 的 valuation 为 h。除掉共同 gcd 的 p-adic valuation h 后，高 carry 侧的系数被 p 整除，低 carry 侧为 unit。U7 的模 p 方程因此准确强迫 **高 carry unit 侧的 head value 为零**；outside value 不进入该方程。

这个方向不能颠倒。例如 unit 侧为 m 时，q_m=d_m′/g 是 unit、p_m=d_m/g 被 p 整除，所以 q_m P(m)=0。若 unit 侧为 m′，同样得到 P(m′)=0。

两边都 unit 的 residues 数为

\[
|\{0,\ldots,u-1\}\cap\sigma\{0,\ldots,u-1\}|=(2u-V)_+=b_0.
\tag{U15}
\]

共有 au 个 unit head sites，内部真实 pair 使用 a b0 个 sites，因此相应独立约束数为

\[
f= a(u-b_0)+\frac{a b_0}{2}=au-\frac{a b_0}{2}=a\min(u,V/2).
\tag{U16}
\]

最后表达式允许 V/2 半整数，f 仍是整数：若反射出现固定 residue，则 V odd；由 2n=ap+r2 和 p odd 得 a、r2 同 parity，V odd 强迫 a even。该固定 residue 的 a 个 sites 在整数头部成 a/2 pairs，因为 c odd，无 fixed integer site。其余 pairs 发生在两不同 residues，各 pair 的头部坐标互不相交。故以上每条 primitive row 独立，没有把 loop 算成两个约束。

## U6. actual image 的上界与准确 outside-head 延拓

首先 p≤2n 时 Q≥a。固定 unit-sector 顶层数据后，每个 unit residue 的底 Q coefficients 可在其 a 个不同 head ψ-values 上任意插值。因此 map B_U→F_p^(au)（unit head values）满射。U16 中的 f 条约束在这个 head 空间上独立，故在 B_U 上亦独立。

实际 A_Z/pA_Z 的 image 必须满足它们，因此 image 落在 codimension f 的子空间。这证明 U4，包括 Q=a 的剩余区间。顶层在不同 residues 上的依赖没有破坏这个满射：这里只改变自由的底 Q 层，不改变顶层。

现在设 Q≥a+1。取任意 B_U 数据，满足这 f 条约束。依次作以下延拓，证明它已来自 actual paired reduction。

1. B_U 的顶层数据本身来自 degree<R 的 low-digit polynomial restriction；选一个实际 global top polynomial 原像，固定其在全部 residues 上的值。R=0 时跳过此步。
2. unit residues 的底 Q coefficients 保持所给数据。每个 nonunit residue 的底 Q coefficients 仍自由；其 positive head cluster 长度至多 a+1≤Q。用这些独立底层 coefficients，把该 residue 的全部 head values 插值为零，抵消已选 top polynomial 在这些点的贡献。不同 head ψ-values 的 Vandermonde rank 为 cluster 长度，degree<Q 完全足够。
3. unit/unit pairs 满足所给 f 条约束。unit/nonunit pairs 的模 p primitive row 只留下 unit 高 carry 侧的 value，已为零。所有 nonunit/nonunit pairs 两侧 head values 都为零，故满足其 primitive row，不需分析其 unit 比值。

得到的 global ambient vector 满足全部 C 的模 p 方程。由 U8，它正是 A_Z/pA_Z 中的 vector，能在原 S 坐标 lift 成 exact characteristic-zero paired polynomial。因此满足 f 条 unit 约束的每个 B_U 数据都延拓成功，image 恰等于这个 codimension f 子空间，证明 U5。

这个步骤解决了 paired constraints 对 ragged top 的耦合：并未随意修改 top；先选真实允许的 top，再只用完全自由的底层消去 outside head 值。对 Q=a 的区间，外部可能有 a+1 个 sites，本文不免费调用该延拓，故保留 U4 而不声明等式。

## U7. 原 whole-X form 的精确核信用

frozen toric G3–G6 与 150bb C5 的 actual DND 接口逐 X 系数成立：p⁵B_X 的 unit-tail block 在 (P,pP′) jets 上 integral，nonunit tails 至少被 p² 整除，head block 被 p⁴ 整除。取实际 A_Z⊗Z_p 的 GL basis，最后 k 个向量来自真实 unit-tail 核的模 p basis，仍由原 S lift。于是

\[
p^5B_A(X)=D N(X)D,\qquad D=\operatorname{diag}(1^{2n-k},p^k),
\quad N(X)\in\operatorname{Mat}_{2n}(Z_p[X]).
\tag{U17}
\]

对整个 determinant 取估值，得 −10n+2k。使用 U4 给 k≥[2n−Qu−min(R,u)+f]+，使用 U5 则 k 的表达式准确且自动非负，得到 U6。若 D_A 为零多项式，估值为∞，该 lower bound 仍合法；没有推断非零。

这与 frozen common-minor/Plücker 或 C! Smith 是不同的局部对象。U17 的 basis 只是 Z_p-unimodular，原 S 的实处解析 determinant 没有换基或重新定标。

## U8. 全尺度连续模型与一个真实正 paid window

对 x=p/n∈[1/4,1]，定义

\[
a=\lfloor2/x\rfloor,\ Q=\lfloor3/x\rfloor,\ h=\lfloor6/x\rfloor,
\quad U(x)=\min(6-hx,(a+1)x-2),
\]
\[
V(x)=(a+1)x-2,\quad R(x)=3-Qx,\quad
F(x)=a\min(U(x),V(x)/2),
\]
\[
\kappa_{pair}(x)=2-QU(x)-\min(R(x),U(x))+F(x),
\quad g_{pair}(x)=-10+2\kappa_{pair}(x).
\tag{U18}
\]

U5 保证这个连续模型的核量非负，亦可由其线性代数证明取极限得到。在固定 window 上，u=nU+ε、0≤ε≤1，V=nV(x)、R=nR(x)，故 |f−nF|≤a，|k−nκ_pair|≤Q+1+a；在 [1/4,1] 可用统一误差≤21。所有 p|2n、p|3n、p|6n 及 floor 跳点都由实际整数公式覆盖，没有删除例外 prime。于是 U6 给 n g_pair(p/n)−42 的全尺度合法界。

作为无需另一证书的实付结论，取 4/7<x<3/5。在这里 a3、h10、Q5、U=6−10x、R=U/2、V=4x−2。471基线在整个 window 上的已付模型正是 150bb C7 的 g_C=110x−72；旧 root weighted 已付窗口 (31/42,3/4) 与这里不交，toric 2856 已付窗口 x>1 也不交。

镜像约束带来的额外提高是

\[
g_{pair}-g_C=2F(x)=
\begin{cases}12x-6,&4/7<x<7/12,\\36-60x,&7/12\le x<3/5.\end{cases}
\tag{U19}
\]

全部区间为正，准确面积为

\[
\boxed{\int_{4/7}^{3/5}(g_{pair}-g_C)\,dx
=\frac{13}{1176}+\frac1{120}=\frac{19}{980}>0.}
\tag{U20}
\]

对各 n，只在该 prime window 取旧整数 lower bound 与 U6 的 max；其他 places 保持471基线。仍有 D_A(X)/Q_n^new∈Z[X]。uniform O(1) local 误差在 window 中只付 O(n)，bounded piecewise-affine PNT（θ(t)∼t，先 step approximation）给同一原基下的安全费用从 A471^safe 降至少19/980。这里 A471^safe 精确为

\[
\frac{45711182732576087}{1070827036198920}-\frac{16469}{23100}-\frac1{84}.
\tag{U21}
\]

本文不计算 U18 的全 [1/4,1] 积分，也未将本轮 toric 更高 weighted 模型的潜在重叠收益直接相加；合并须共同取max。U20 只相对于已冻结471基线给独立严格改进。

## U9. FIRST-ONLY 有限机制验证及准确阅读范围

自有 DISTINCT NEW `cdt_odd_paired_actual_unit_sector_rank_20261006_verify.py` 先完整静态读取，确认输出不存在，然后首次且唯一执行1次，exit0 PASS；success1、failed0、rerun0，旧/同行producer执行/import0、外部Lean0。guard 在数学运算前 exclusive-create 状态文件，若失败会保留失败状态；此处没有失败被抹去。

程序只 import stdlib，literal 重建 U1/U2 的 factorial gcd、原 Newton S columns，直接校验原 primitive paired rows，然后构造全部实际 unit-tail value 与 p-scaled derivative 矩阵。n≤28、7≤p≤2n、p²>8n，143cases、124959checks，其中 Q≥a+1 的91cases验证 U5，52cap-onlycases只验证 U4；不会把这些有限例子当作全尺度 theorem。

source/JSON 成功后保持只读，最终 SHA 在独立来源收据记录。本文全尺度证明是 U2–U7，有限程序仅校验定义和方向的机制。

本轮实际读取：background 主报告 §§127–132；冻结 lattice I1–I10（全部I1–I25公式）；150bb C1–C10（全部C1–C21公式/47行）；2856 toric G1–G15；b953 weighted W1–W10（全部W1–W14公式）。全部输出无截断。没有本轮新 PDF/HTML/外部源码下载或 primary 新读，所需插值、valuation、线性代数在本文给出实际步骤。程序源码完整静态读取；成功后 JSON 的实际 parse/read 范围由最终收据准确登记，不提前记为全部143条人工重算。

## U10. 已证、仍缺与下一步

已证：原实际 paired integer-valued 格在 unit-tail 完整 ψ coefficient sector 上的 supported primitive constraints 数 f；Q≥a+1 时精确像秩和 exact characteristic-zero 延拓；所有 p≤2n 的相应秩上界；同一个 D_A(X) 的 whole-X 内容信用及独立正 paid 主率19/980。新的信用来自原配对关系，未暗换格或 source。

仍缺：Q=a 区间的 exact image、非unit-weighted 多sector同时优化的精确actual约束兑现、无限 rational-target nonzero、足够 strict margin。当前已证算术安全费用仍远大于解析率，因此没有新增 ζ/L/Catalan 无理性或线性无关性定理。后续可以把 U5 的 actual image 损失与各 weighted jetrow 支撑联系；不能只在任意部分 rows 上无条件减 f，必须证明那些 rows 真正看见相应 head interpolation constraints。

本文待独审，未提前冻结；旧471数学输入、旧收据均保持不改。
