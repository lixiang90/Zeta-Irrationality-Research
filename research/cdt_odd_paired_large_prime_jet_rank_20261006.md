# 配对整数格的真实负节点核、二阶 jet 整除与全素数费用改善

日期：2026-10-06。NEW 全尺度纸面证明；本稿当前供独立审阅，尚未提前冻结。旧/同行数学 MD、PY、JSON、manifest 全部仅读，执行、import、重跑次数为0。

本轮在同一个 rank2n 配对饱和整数格上证明一个新的局部估值界，而非更换格或再次约除 gcd。对每个 n≥1、每个素数 3n<p≤6n，真实 unit-tail evaluation 的核维数 k(n,p) 可显式计算，并给出

\[
\boxed{v_p^{\mathrm{Gauss}}D_A(X)\ge-10n+2k(n,p).}
\tag{J1}
\]

把这一界与冻结的全素数预算取较强者，得到严格较小的安全费用

\[
\boxed{A_{\mathrm{jet}}^{\mathrm{safe}}=
\frac{1069856243}{24190320}\in[44.226,44.227),
\qquad A_{\mathrm{old}}^{\mathrm{safe}}-A_{\mathrm{jet}}^{\mathrm{safe}}=\frac23.}
\tag{J2}
\]

这是覆盖整段素数区间的 n² 费用改善。它不是 actual content 的等式，不是 exact Smith 等式，也没有解决无限 nonzero 条件或得到特殊值无理性结论。

## J3. 完全相同的对象与 actual p-local 格

沿用冻结 [all-prime budget](cdt_odd_paired_all_prime_budget_20261006.md) B2–B3：ambient Newton 格为 degree<3n 的整数值多项式，f_i(t)=binom(t−1,i)，0≤i<3n。令

\[
c=2n+1,\quad d_z=(z)_{6n+1}=\frac{(6n+z)!}{(z-1)!},
\quad g_z=\gcd(d_z,d_{c-z}),
\quad p_z=d_z/g_z,\quad q_z=d_{c-z}/g_z.
\]

配对饱和格 A_Z 的条件为 q_z P(z)−p_z P(c−z)=0，1≤z≤n；这是 P(z)/d_z=P(c−z)/d_{c-z} 的真实 primitive 条件。取冻结完整整数基矩阵 S，定义 D_A(X)=det(S^T H_N(X)S)。本稿没有 first2n factorial normalizer，没有 quartic-zero 布局，没有额外 primitive-gcd 信用。

现固定 3n<p≤6n。必有 p≥5、p²>8n，且全部 i!、i<3n 是 p-unit。因此 actual Newton 格经 GL_{3n}(Z_p) 与 monomial coefficient 格识别；这是冻结 B20 中 i_1=0 的首层，而不是免费扩张 ragged layer。各 2n 个 head 点 1,…,2n 在 F_p 中互异，插值 Vandermonde 的 determinant 为 p-unit，故 head evaluation 在 Z_p 上满射。每个 primitive pair 方程至少一个系数为 p-unit，各 pair 不交，因而

\[
U=A_Z\otimes Z_p\text{ 是 rank2n 直和项},\qquad
U/pU=\ker(\overline C)\subset F_p[t]_{<3n}.
\tag{J4}
\]

这里没有把未饱和方程约减后误当 actual reduction。

## J5. 实际 form、系数与 whole-X 估值

原 triple-zero、B6、s5 form 为

\[
B_X(P,Q)=\sum_{j=0}^{6n}W_j\{U_j(PQ)'(-j)+V_j(X)P(-j)Q(-j)\},
\]
\[
W_j=\binom{6n}{j}^{\!2}\binom{2n+j}{j}^{\!3},\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j},
\]
\[
U_j=-8aH_j^{(3)}-6bH_j^{(4)},\qquad
V_j(X)=C_jU_j+24\{X-aH_j^{(4)}-bH_j^{(5)}\}.
\tag{J5}
\]

a,b∈Z 固定，b≠0；不要求它们是 p-units。系数 −8 来自 (s−1)(s−3)!=8，不能错写成 −4。本轮 NEW verifier 的首次运行前静态核对已修正这一系数；不存在失败后重跑。固定有理 a,b 先乘固定 D，整个 determinant 付 D^{2n}=exp(O(n))，不改变 n² 主率。v_p 指 whole Q[X] 的 Gauss valuation。

## J6. unit-tail 的真实节点集合

写 j=p+ρ。由于 p>3n，tail 中 0≤ρ≤6n−p<p。Legendre 的单层 carry 给

\[
v_pW_{p+\rho}=
\begin{cases}
0,&0\le\rho<p-2n,\\
3,&p-2n\le\rho\le6n-p,
\end{cases}\quad(3n<p<4n),
\]
\[
v_pW_{p+\rho}=0\quad(4n<p\le6n).
\tag{J6}
\]

p=4n 不可能为素数。因此 unit-tail 的节点恰为 0,−1,…,−(R_0−1)，其中

\[
R_0=\begin{cases}p-2n,&p<4n,\\6n+1-p,&p>4n.\end{cases}
\]

定义真实 reduction 上的 evaluation map

\[
\pi:U/pU\longrightarrow F_p^{R_0},\quad
P\longmapsto(P(0),P(-1),\ldots,P(-(R_0-1))),
\quad k=\dim\ker\pi.
\tag{J7}
\]

这里算的是 π 的 rank，不是 tail Gram 的 rank；不需要有限域 Gram 非退化。

## J8. p>4n 时的 stripped factorial 与核

令 A(t)=(t)_{R_0}，K=3n−R_0=p−3n−1。A 在所有 head 点上是 unit，且 Wilson 直接给

\[
v_pd_z=1,\qquad d_z/p\equiv-A(z)\pmod p\quad(1\le z\le2n).
\tag{J8}
\]

理由是 6n+z<2p，将 (6n+z)! 中唯一的 p 提去后，(p−1)!≡−1，剩下 (6n+z−p)!；除以 (z−1)! 恰是 A(z)。

π 的核由 P=AQ、deg Q<K 给出；actual pair 条件变成 Q(z)=Q(c−z) 在全部 head 点成立。设 σ(t)=c−t，2 是 unit，分解 Q=Q_even+Q_odd。head-root polynomial S_h(t)=∏_{z=1}^{2n}(t−z) 为 σ-even。条件等价于 S_h|Q_odd。若 K≤2n，只剩 ceil(K/2) 个 even 系数；若 K>2n，odd 部分是 S_h 乘 degree<K−2n 的 odd 多项式。于是

\[
\boxed{k=\left\lceil K/2\right\rceil+max\{0,\lfloor(K-2n)/2\rfloor\}
=\max\{p-4n-1,\lceil(p-3n-1)/2\rceil\}.}
\tag{J9}
\]

所有 degree 均小于 p，故这是 polynomial divisibility，而非遗漏的 function-ring 关系。

## J10. 3n<p<4n 的第二次 carry：不可假装统一 unit

令

\[
H=2p-6n,\quad J=8n+1-2p,\quad H+J=c,
\quad A(t)=(t)_{p-2n},\quad B(t)=\prod_{z=H}^{2n}(t-z).
\tag{J10}
\]

H 为正偶数，J 为正奇数。A 是 π 的 node-root polynomial，在全部 head 上是 unit。实际 d_z 的 leading unit 为

\[
\begin{array}{ll}
z<H:&v_pd_z=1,\quad d_z/p\equiv-A(z)B(z),\\
z\ge H:&v_pd_z=2,\quad d_z/p^2\equiv-2A(z)B'(z).
\end{array}
\tag{J11}
\]

第一式：A(z)B(z) 将连续 factors z,…,6n+z−p 通过模 p 连接。第二式：6n+z<3p，stripped (6n+z)!/p²≡2(6n+z−2p)!；同时

\[
A(z)B'(z)=
\frac{(z+p-2n-1)!}{(z-1)!}(z-H)!(-1)^{2n-z}(2n-z)!
\equiv-\frac{(z-H)!}{(z-1)!}.
\]

最后一步是 Wilson 的 a!(p−1−a)!≡(−1)^{a+1}。因此 leading 的 −2 必须保留。

若一对 head 的 d 阶数分别 1、2，primitive pair reduction 强制阶数2点的 P 为0；若阶数相同，则 P 除以相应 leading unit 在 pair 两端相等。这个规则来自真正约除了 min valuation 的 primitive 条件，不是原未约除式。

## J12. H≤n：overlap 的 odd 约束

πkernel 写 P=AQ、deg Q<K=5n−p。H≤n 时没有两个阶数1点的 pair。两个阶数2点的 overlap 为 H,…,J；令

\[
I(t)=\prod_{z=H}^{J}(t-z),\quad
Z(t)=\prod_{z=J+1}^{2n}(t-z),\quad B=IZ.
\]

mixed pair 的阶数2点 J+1,…,2n 强制 Q=ZR。记

\[
\deg R<D=11n-3p+1,\qquad L=\deg I=2n+2-2H\text{ 为偶数}.
\]

on overlap，Q/B'=R/I'，且 I'(c−z)=−I'(z)，故 pair 条件成为 R(z)=−R(c−z)。等价于 I|R_even；odd 部分不受该约束。D−L=p−3n−1≥0，因此

\[
k=\lfloor D/2\rfloor+\lceil(D-L)/2\rceil=4n-p.
\tag{J12}
\]

I 与 Z 的点均互异，所有 degree bounds 保留；这一步不能将 overlap 偷换成全部 head。

## J13. H>n：central 的 even 约束

现在两个阶数2点的 overlap 为空，所有 H,…,2n 均是 mixed high 点，强制 Q=BR。于是 deg R<D=p−3n−1。两个阶数1点的 central set 为 J+1,…,H−1，长度

\[
L=H-J-1=4p-14n-2\ge0\text{ 为偶数}.
\]

其 leading 条件变成 R(z)=R(c−z)，所以该 central-root polynomial 整除 R_odd。由 D−L=11n−3p+1，得到

\[
k=\lceil D/2\rceil+max\{0,\lfloor(D-L)/2\rfloor\}
=\max\{4n-p,\lceil(p-3n-1)/2\rceil\}.
\tag{J13}
\]

若 central set 为空，L=0，以上维数照样成立。连同 J12：

\[
\boxed{k(n,p)=
\begin{cases}
\max\{4n-p,\lceil(p-3n-1)/2\rceil\},&3n<p<4n,\\
\max\{p-4n-1,\lceil(p-3n-1)/2\rceil\},&4n<p\le6n.
\end{cases}}
\tag{J14}
\]

## J15. actual weak lifts 与二阶整除

选择 U/pU 的 basis，使其中最后 k 个向量是 kerπ 的 basis。由 J4 它可提升为 U 的真正 Z_p basis；前 R=2n−k 个称 strong，后 k 个称 weak。这些是 exact characteristic-zero paired vectors，而非仅 modp 的自由 polynomial。

每个 weak lift Q 在 unit-tail 的 −j=−p−ρ 点满足 Q(−j)∈pZ_p；Q'(−j)∈Z_p，所有 strong 值与导数也 integral，因为 degree<3n<p。写 M=p^5 B_X。实际 harmonic 下标≤8n<p²，故

* head j<p：U_j integral，V_j 的 whole-X valuation≥−1，因此 M-head 的全部 terms 在 p^4Z_p[X]；
* tail j≥p：v_pU_j≥−4、v_pV_j≥−5，因此 p^5U_j∈pZ_p、p^5V_j∈Z_p[X]；
* 非 unit-tail 的 W_j∈p³Z_p，故即使不使用 weak vanishing，其 M-contribution 也在 p³Z_p[X]。

对 unit-tail，strong×weak 的 value product 带一个 p，derivative coefficient 自带 p；weak×weak 的 value product 带 p²，(PQ)' 中每项也至少带一个 p，再乘 derivative coefficient 的 p。故整个 whole-X 矩阵满足

\[
M_{\mathrm{strong,weak}}\in pZ_p[X],\qquad
M_{\mathrm{weak,weak}}\in p^2Z_p[X].
\tag{J15}
\]

这只使用真实 evaluation kernel 和 elementary valuation，不使用未知强/弱 Gram unit，不使用 Schur complement 的非退化。

## J16. 所有 minors 的已证 polygon，严格区别 exact Smith

令 D=diag(1^R,p^k)。J15 等价于 M=D N D，其中 N∈Mat_{2n}(Z_p[X])。于是所有 r×r minors 都满足

\[
v_p^{\mathrm{Gauss}}\mathrm{minor}_r(M)\ge2(r-R)^+,
\quad
v_p^{\mathrm{Gauss}}\mathrm{minor}_r(B_X)\ge-5r+2(r-R)^+.
\tag{J16}
\]

理由是任意 r rows、r columns 各自至少含 (r−R)^+ 个 weak indices，两侧 D 的费用相加。对 full determinant r=2n 即得 J1。actual basis change 的 determinant 为 p-unit，因此返回冻结 S 的 D_A 不改变其 Gauss valuation。D_A=0 时 v_p=+∞，声明同样成立。

J16 是全尺度 determinantal-ideal/Smith polygon 的下界。不能据它宣称 exact Smith 为 0^R,2^k：例如 N 的 mixed block 可产生 1,1 的 elementary exponents。也不能据它得到非零 determinant；N 的实际单位条件仍未证。

## J17. 同一个全素数 signed ratio 的改进

冻结 B10–B11 对每个 n 给合法整数 ℓ_p，D_A/Q_n∈Z[X]，且 B14–B16 给 A_old=1085983123/24190320。本稿取

\[
\ell'_p=\begin{cases}
\max\{\ell_p,-10n+2k(n,p)\},&3n<p\le6n,\\
\ell_p,&\text{其他素数},
\end{cases}\qquad
Q'_n=\prod_p p^{\ell'_p}.
\tag{J17}
\]

J1 与旧合法下界取 max，方向正确，故每个 n 的全部形式系数都有 D_A/Q'_n∈Z[X]。p≤√8n 的原全n cap 与 p>6n 的 integrality 完整保留。这里没有重复计算 primitive pair gcd，没有改变 archimedean basis，亦没有只清 specialization 的分母。

## J18. 连续 gain 与 PNT：严格减去 2/3

令 x=p/n。J14 的 rounding 误差在 3<x≤6 中 uniform O(1)，故新的 normalized bound 为

\[
g_J(x)=-10+2\max\{4-x,(x-3)/2\}\quad(3<x<4),
\]
\[
g_J(x)=-10+2\max\{x-4,(x-3)/2\}\quad(4<x\le6).
\tag{J18}
\]

实际仅读旧 JSON 的三个终 segments，并回读旧正文的完整 model/PNT 证明：

\[
g_{\mathrm{old}}(x)=
\begin{cases}-2x-2,&3<x<4,\\2x-18,&4<x<5,\\12x-68,&5<x<6.\end{cases}
\]

因此 max 之后的确切改善为

\[
\Delta(x)=\begin{cases}
3x-11,&11/3<x<4,\\
5-x,&4<x<5,\\
0,&\text{其余 }x\in(0,6).
\end{cases}
\tag{J19}
\]

相应积分是

\[
\int_{11/3}^{4}(3x-11)\,dx=\frac16,\qquad
\int_4^5(5-x)\,dx=\frac12.
\tag{J20}
\]

各端点 rounding 只给 O(1) 每素数费用，Σ_{p≤6n}O(1)logp=O(n)。由 θ(T)∼T 对 bounded piecewise affine Δ 的加权 PNT（先 step functions，后 Riemann 上下逼近），结合旧 B15 的同一 uniform model，得到

\[
\liminf_{n\to\infty}n^{-2}\log Q'_n
\ge-\frac{1085983123}{24190320}+\frac23
=-\frac{1069856243}{24190320}.
\tag{J21}
\]

这不是将单个辅助 prime 的 gain 积分，更不是有限 rank samples 推成全 n。两段正 gain 来自 J8–J16 的纸面定理。安全费仍明显不足以匹配当前已证解析率；这不是 actual arithmetic cost 下界或方法 no-go。父任务正在独立研究 n<p≤2n 的 actual Plücker refinement，其与本稿 interval 不交，但其新稿未经本稿作者实际独读之前，不在 J2 中合并。

## J22. 自有首次 finite verifier：准确范围与未证项

NEW [verifier](cdt_odd_paired_large_prime_jet_rank_20261006_verify.py) 仅首次执行1次，output guard 禁止已有 JSON 时重跑。输出 [JSON](cdt_odd_paired_large_prime_jet_rank_20261006_verify.json) 为 PASS：n=1,…,10 的所有 3n<p≤6n，共43 cases，15383 exact checks。程序不读取、import、执行任何旧或同行数学文件；只用 stdlib。

有限检查实际构造 primitive pair constraints，验证其 modp rank=n、joint negative-evaluation kernel 的维数 J14，以及 J8/J11 的 stripped-unit identity。另对 integer sources (a,b)=(0,1),(1,1) 检查 p² jet 整除。代码中的 weak coefficient representatives 是 ker(overline C,π) 的任意整数系数提升，**不是** exact characteristic-zero paired lifts；这组检查只测试所有具有同样 negative value divisibility 的 polynomial 的 J15 局部机制。纸面 J4/J15 单独保证真正 paired basis 的提升。

程序计算 p^4U 的 a 项为 −8apH_{floor(j/p)}^{(3)}，p^5V 的 a 项为 −24apH_{floor(j/p)}^{(4)}，均 modp²；p^5X 项在此有限模数下消失，纸面 whole-X 界另外已经证明。finite scope 不包括一般有理目标的无限 nonzero、不包括 full Smith equality、不包括 p≤3n 的 ψ higher layers。

## J23. 实际来源读取与本轮边界

本轮实际完整读取冻结 budget B1–B22 及其来源 receipt，lattice I1–I25、auxiliary A1–A13、mixed arithmetic A1–A14（含 A30a）。第一次组合输出中 lattice/arith 截断，随后分别以完整足量输出补读，不以被截断片段宣称完成。另仅读旧 budget JSON 的 3<x<4、4<x<5、5<x<6 三个 affine segments。未运行这些对象的任何 producer。没有新增 PDF 下载；本轮没有将历史 PDF 阅读误记为新增阅读。本稿 Wilson、parity decomposition、lifting 与 minor divisibility 均在正文自证，PNT 使用已实际回读的冻结证明。

本轮数学 producer 恰1个、首次恰1 run PASS；旧/同行数学 execute/import/rerun 全0。最终 receipt 另存 NEW，不修改旧 pins。本稿仍需独审后冻结；后续研究须保留：p≤3n 的真实 ψ higher layers；弱/强 Gram 的 unit 或 nonzero；同一 determinant 的 strict arithmetic/analytic margin。J21 是新 safe upper fee，而不是研究目标已经完成。
