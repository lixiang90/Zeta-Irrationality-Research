# 真正配对格的进位秩亏、whole-X 内容与可兑现 Smith 信用

2026-10-06，quarter_actual_rank。NEW 数学稿，供实际全文独审；旧439项数学输入及所有旧/同行 producer 只读。本文先证明一个不需要第二层精确 Smith 的普遍下界，并严格计算它在同一个 determinant 上的实际费用收益。后面的更高层接口单独标明所需输入，不把有限检验或裸信用积分当成特殊值结论。

## S1. 同一个对象、主结论和实际输入

保持原 B=6、三重零点、s=5、ambient degree<3n、rank2n 的 actual saturated integer-valued paired lattice。取整数 a,b，b≠0，形式变量 X；固定有理 a,b 先清固定分母，只付 O(n)。D_A(X) 为冻结稿中的同一 actual determinant。没有 quartic-zero/restored layout，没有换格或再次约除 Γ。

本轮实际完整回读冻结 dual 稿 D1–D10、D1–D21（SHA 0fb995f69cefcd4e6c92f7ffa42a8e595add4dda9a94951ed27a4693fb127047），冻结 budget B1–B22（SHA 55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc），原 budget JSON 的全部50 affine rows（SHA 7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b）。初次合并读取中 jet 稿 J16 被截断，已单独补读 J15–J17；不将截断输出称本轮新的完整 jet 阅读。此前冻结联合独审 Q7 已证明同对象、不交窗口的安全费用

\[
A_{\rm prev}^{\rm safe}=\frac{4624049789}{104824720}.
\tag{S1}
\]

其 SHA 为 7fa899348497a05b07eafa45fc75828f999550f0b6bc3d76e74b61c5b0db296a；此费用是已证明的上界，不是 actual content 或 actual cost 的等式。

对任意 n≥1、任意 prime n/2<p≤n 且 p²>8n，本文证明

\[
\boxed{\delta_p\ge n-p+M_p},
\qquad M_p=\#\{\text{进位不同的镜像 residue pairs}\}.
\tag{S2}
\]

因此 whole-X 安全费用严格减少

\[
\boxed{\Delta A=\frac{121537}{4476780}>0},\qquad
A_{\rm first}^{\rm safe}
=\frac{790225879771}{17925027120}\approx44.085.
\tag{S3}
\]

这是全尺度、正 measure 的 n² 信用；不依赖 finite-field Gram unit，也不证明无限非零或严格解析/算术余量。

## S2. actual weighted constraint 与整数格没有变化

令

\[
b_j=\binom{6n+j}{j-1},\quad m'=2n+1-m,\quad
\beta_m=\gcd(b_m,b_{m'}),\quad
p_m=b_m/\beta_m,\quad q_m=b_{m'}/\beta_m.
\]

对 Newton 基 f_j(t)=binom(t−1,j)，真实满射 primitive constraint 的低2n列为

\[
C_{m,j}=q_m\binom{m-1}{j}-p_m\binom{m'-1}{j},\quad0\le j<2n.
\]

连续整数节点 evaluation 是 unimodular，每 pair gcd1，故 C 满射；其 kernel 正是冻结实际饱和低块。C!:=C diag(j!) 与冻结 D6 同一矩阵，定义 δ_p 为全部 n-minors 的 ideal valuation。满射的有理 rank=n，乘非零 j! 后仍 rank=n；这不涉及 D_A 是否非零。

冻结 primitive complementary-minor 等式给全 prime 的准确 identity

\[
T_p=\sum_{j=0}^{3n-1}v_p(j!)-\delta_p.
\tag{S4}
\]

本稿只对这个 actual δ 加下界。模 p 时 j≥p 的 falling numerator 在每个整数 site 皆为0；首 p 列的 falling basis 在所有 residue 上的 evaluation 是 GL_p(F_p)。因 p≤n，所有 residues 在 head 0,…,2n−1 中实际出现，所以

\[
\operatorname{rank}(C!\bmod p)
=\operatorname{rank}\mathcal R_p,
\qquad (\mathcal R_p)_m=q_m e_{m-1}-p_m e_{m'-1},
\tag{S5}
\]

下标取模 p。这保留 j<2n 的真实 degree cutoff，没有扩成任意 jet function 格，也没有将普通 integer-valued 格换成 divided-difference-integral 格。

## S3. primitive 进位不同块只占一维

写 N=6n+1=hp+e，τ=p−e，并令 H=2n−1=up+z，0≤z<p。对 k=m−1=lp+r，d_{k+1}=(k+1)_N，所有 factorial 下标≤8n<p²，Legendre 给

\[
v_p(d_{k+1})=h+\mathbf1_{r\ge\tau}.
\tag{S6}
\]

从 d_j 除同一个 N! 得到 b_j，不影响 pair 相对 valuation 或实际 primitive 系数。镜像 residue 是 σ(r)=z−r mod p，且每个 residue 至少有两个实际 lifts（p≤n）。

对 r≠σ(r) 的两节点块，若进位相同，其 rows 的 rank至多2；本文不需要证明某个2×2 minor为 unit。若进位不同，每个 primitive pair row 只有进位较大侧的 coefficient 模 p 非零，所有 rows 都支撑同一个节点，rank至多1。唯一 fixed residue 的 loop 块 rank至多1。因为 p 为奇数，所有 residue coordinates 的基线块维数总和为 p；每个 mixed offcenter pair 至少额外损失一维。因此

\[
\operatorname{rank}\mathcal R_p\le p-M_p.
\tag{S7}
\]

Smith 的 n 个非负 valuations 中恰有 rank(C! mod p) 个为0，其余至少1。S5/S7直接给 S2。这里没有将 p>n 的 Smith 0/1 结论错误延伸至 p≤n；可能的第二/高层只会使 δ 更大。

## S4. 完整整数计数与 uniform 连续接口

两个 reflection intervals 分别为 [0,z] 和 [z+1,p−1]。前一 interval 的 mixed pairs 满足 r<τ≤z−r；后一 interval 以 r−z−1 平移后同理。精确计数是

\[
\boxed{M_p=[\min(\tau,z+1-\tau)]_+
+[\min(\tau-z-1,p-\tau)]_+.}
\tag{S8}
\]

其中 [t]_+=max(0,t)。Fixed point 从不 mixed，端点 e=0、z=0或z=p−1均已包含；不需要删除中心或猜测奇偶费用。

设 x=p/n∈(1/2,1)，u_x=floor(2/x)、h_x=floor(6/x)，定义

\[
Z(x)=2-u_xx,\quad T(x)=(h_x+1)x-6,
\]
\[
d_{\rm in}(x)=[\min(T,Z-T)]_+,\quad
d_{\rm out}(x)=[\min(T-Z,x-T)]_+,\quad d=d_{\rm in}+d_{\rm out}.
\tag{S9}
\]

有真正 uniform 的 |M_p−nd(p/n)|≤2。证明：若 p<n，则 p不整除2n，故 z+1=nZ；若 h=h_x，τ=nT−1，S8各项只差≤1。唯一 h不同情形是 p|6n+1，此时 actual e=0、M_p=0，nT=1，两个 continuous 正部各≤1。p=n 只可能 n为 prime，此时 z=p−1、e=1，M_p=1，而 continuous d(1)=0；同样在误差内。这里未把 floor 跳点作为未付大例外素数。

## S5. whole-X 内容的合法转移

在当前 window，δ_0:=Σ_{i=0}^{n−1}v_p(i!)=n−p。因此由 S4/S2

\[
T_p\le T_p^{\rm safe}-M_p,\qquad
T_p^{\rm safe}=\sum_{i=n}^{3n-1}v_p(i!).
\tag{S10}
\]

冻结 B18 的 whole-X common monomial-minor transfer 给

\[
v_p^{\rm Gauss}D_A(X)\ge
\max\{-10n,\Lambda_p-2T_p^{\rm safe}+2M_p\}.
\tag{S11}
\]

没有固定 X specialization、没有假设 a,b 是 p-units、也没有从 Gram 非零取得费用。全部原小 prime、大 prime 界保留。取旧合法 ℓ_p 与 S11 较大者，并在不满足新 window/p²条件时保持旧 ℓ_p，得一个全 n signed Q_n，D_A(X)/Q_n∈Z[X]。这是整个实际 polynomial 的 content 下界；positive ℓ_p也保留，不裁成纯分母。

若将来对 rational X=c另证明 D_A(c)≠0，则 rational specialization 的固定分母付 exp(O(n))。S11自身不提供该 nonzero。

## S6. cap 后的正信用，不积分裸 d

冻结原 raw budget g_raw 在 (1/2,1) 的12个实际 affine段依次如下；取 g_old=max(g_raw,−10)。

|区间|g_raw|
|---|---|
|(1/2,8/15)|40x−32|
|(8/15,6/11)|85x−56|
|(6/11,4/7)|30x−30|
|(4/7,3/5)|72x−54|
|(3/5,8/13)|12x−22|
|(8/13,2/3)|51x−46|
|(2/3,8/11)|21x−24|
|(8/11,3/4)|54x−48|
|(3/4,4/5)|6x−16|
|(4/5,6/7)|36x−40|
|(6/7,8/9)|x−14|
|(8/9,1)|28x−38|

直接逐段比较 g_new=max(g_raw+2d,−10)，真正 gain Δg=g_new−g_old 仅在下列9段非零：

|区间|Δg|
|---|---|
|(34/63,46/85)|63x−34|
|(46/85,6/11)|12−22x|
|(2/3,7/10)|18x−12|
|(7/10,8/11)|16−22x|
|(8/11,14/19)|22x−16|
|(14/19,3/4)|12−16x|
|(23/28,14/17)|56x−46|
|(14/17,5/6)|22x−18|
|(5/6,6/7)|12−14x|

这是12 affine raw段与 S9 max/min 的完整比较，不是有限 q 采样。所有未列段的 gain=0。三个相连 window 的面积分别为

\[
\frac{16}{58905},\qquad \frac{43}{2090},\qquad
\frac1{8092}+\frac{23}{10404}+\frac1{252}.
\tag{S12}
\]

相加为 S3 的121537/4476780。特别：h=10,9,6对应的原 raw 即使加第一层信用仍在 cap 下；不可将相应裸 mixed-pair triangle 面积当实际收益。

## S7. 全 n 与 PNT 费用方向

冻结 B15 对 x∈[1/2,1] 的 Λ/factorial连续模型误差 uniform O(1)；S4加入的误差仍为 O(1)。所有 prime p≤sqrt(8n)处不用新结论，原费用仅 O(n^(3/2)log n)，不影响主率。小 n和端点全由 S11 或旧 all-n 界完整覆盖。

对 bounded piecewise affine Δg，由 θ(t)∼t，先 step-function 后 Riemann逼近，得

\[
\liminf_{n\to\infty}n^{-2}\log Q_n
\ge-A_{\rm prev}^{\rm safe}+\int_{1/2}^1\Delta g(x)\,dx
=-A_{\rm first}^{\rm safe}.
\tag{S13}
\]

新 interval 与前轮 n<p≤2n carry、3n<p≤6n jet 两个 paid windows不交，故 S1 的收益不重复。由于 S2用的 C!已经是 primitive actual lattice，Γ的解析平方信用也不在 finite-place 再扣一次。A_first只是更便宜的安全费用上界；它仍大于当前解析率>12.003572854，不是 actual cost lower 或整个方法 no-go。

## S8. 第二层/普遍 capacity 信用的精确 comparison gate

本节采用已实际全文独核通过的 root NEW [CRT整模型](cdt_odd_paired_residue_crt_integral_model_20261006.md) R19–R21，SHA3265da7c600ef8c1624f4208448ec35d75e32d71d92d78f4576b2cfdd5cfbd33；正式[独审](cdt_odd_paired_residue_crt_integral_model_independent_review_20261006.md)另存NEW。该定理在同一 C!上证明

\[
\delta_p\ge\delta_0+
\sum_{\text{mixed offcenter orbit}}\lfloor L/2\rfloor,
\tag{S14}
\]

L为该 orbit 的 actual pair row数，则归一化额外信用为

\[
e_{\rm cap}(x)=
\lfloor(u_x+1)/2\rfloor d_{\rm in}(x)
+\lfloor u_x/2\rfloor d_{\rm out}(x),
\quad u_x=\lfloor2/x\rfloor.
\tag{S15}
\]

这保留 lift-count、ragged degree cutoff和同一 actual格。S14由上述全p真GL与column-capacity纸面定理提供，不由本稿有限代码证明；本稿已独核其全部R1–R21，包括baseline奇偶sum、实际primitive弱侧、exact整数计数。

对x∈[1/4,1]，actual extra=n e_cap(x)+O(1)的误差同样uniform：a=floor(2n/p)恰是u_x，b=2n−ap=nZ；正常h=h_x时τ=nT−1，R20的两个正部各与n d_in/out差≤1，floor权重≤4。唯一h跳动是p|6n+1，actual所有carry相同、extra0，continuous nT=1给两部分各≤4。这个论证包括p|n的b=0边界，不删除未经付费的例外prime。

当1/2<x<2/3，额外第二层只比 S9多一个 d_in，正是4-lift mixed块 M4。其support上 g_raw+4d_in 的 maxima，h=11,10,9分别为

\[
-\frac{280}{27},\qquad-\frac{314}{25},\qquad-\frac{330}{23},
\tag{S16}
\]

全部严格小于−10；因此新的 M4信用在当前 common-minor/entry-cap 模型中 paid gain=0。这不否定更强实际 Smith 定理，而是阻止从其裸面积直接报费用改善。

对1/4≤x≤1/2，S15与原 raw各 floor分段作同样精确 affine比较，结果仍 g_raw+2e_cap≤−10。NEW证书保存全部闭区间；它不是仅抽样。对0<x≤1/4，actual rows总数n且每mixed orbit费用 floor(L/2)≤L/2，故 e_cap≤1/2；原 B13 的 g_raw≤−4/x+2+x/4，加2e_cap≤1后仍严格低于−10。这把小x tail完整封口。

因此在已经严证的 S14下，现 transfer模型的 paid额外主率也恰与 S3相同，p<n/2与M4的新增主率均0。这里的零只针对这个明确的 safe bound-model，不是 actual content 或未来构造的 no-go。

## S9. NEW FIRST-ONLY 证书和实际执行史

自有 NEW `cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.py` 保存后完整静态读源码，确认输出不存在，首次且唯一运行1次，exit0 PASS；不读取、import或执行任何旧/同行producer，标准库 exact Fraction。

程序独立构造 n1..40、每个满足 n/2<p≤n和p²>8n的 actual primitive graph，共94案例，检查 S8及rank≤p−M，并独立检查与 C!首p falling列的rank相等。它不计算精确高Smith层，有限案例不替代 S2–S8纸面证明。

费用部分将原 raw段当literal数据独立录入，在 [1/4,1] 加入所有 floor/type边界、min/max affine相交点和cap零点，共76个闭 affine区间；端点上下比较核完整区间，而不是从中点取样外推。保存每区间 slope/intercept、exact积分，输出第一层与当时条件 capacity的 paid gain同为121537/4476780；subhalf额外0，M4额外0。S14的整格前提在执行时明确为conditional；执行后再实际全文独审 root R19，才将正文S8升级为已证输入。原已执行source/JSON的条件历史保持原样，不改、不重跑。

源码 SHA 378962de4c7f87851dc2e942318277b92d66b24814af00db43f9df009331711d。成功输出原路径 `cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.json`；最终指纹另记NEW receipt。已有输出后不再执行；没有失败run或distinct v2，没有外部Lean、PDF下载或外部源码新增。

## S10. 真正需要改进的接口

本稿的正结果是：无需精确Smith即可给超出δ0的actual lower，并在 whole-X上兑现严格主率。未补无限 nonzero与匹配margin。

S16和subhalf gate说明，仅把更高C!层信用放进 Λ_p−2T_p 的独立最差界，会丢掉 paired support与residue form之间的相关性。一个精确且可执行的下一接口是对 actual Cauchy–Binet支撑直接使用

\[
\min_{u_Iu_J\ne0}
\{v_pu_I+v_pu_J+\Lambda_{I,J,p}-e_{I,p}-e_{J,p}\},
\tag{S17}
\]

其中 Λ_{I,J,p} 是指定 falling/monomial rows、columns 的 residue minor下界。现 Λ_p−2T_p 将 Λ_{I,J,p}先在全部rows上取共同最小，再将 Plücker费用独立取最大；二者可能来自不相容的支撑。S17要求 actual degree cutoff和paired CRT packet共同参与，而不是再优化一个有限参数 q 或免费改变norm。

另一条严格路线是在真正 paired integer-valued residue/jet格上直接估 whole-X局部Gram的弱层，避免先转成共同 monomial-minor bound。这需证明 exact characteristic-zero paired lifts与各 ragged packet dimension，不能将自由mod-p polynomial reps当actual lifts。本稿没有提前宣布 S17 或此局部Gram路线已给新费用。
