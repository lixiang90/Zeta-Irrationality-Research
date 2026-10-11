# 原配对行列式的低高块耦合、Schur 消元与新增解析衰减

日期：2026-10-07。NEW 全尺度证明稿；原 B6/κ3/s5、degree<3n、rank2n、原饱和 S 与 whole-X D_A 全部保持。504 个既有数学输入及同行 producer 只读，执行/import/rerun 为0。唯一自有 NEW guarded FIRST1 程序只认证八个实数严格不等式，PASS；没有素数、行列式非零或 Lean 实验。本文暂待 root 独审，不提前宣布最终来源收据冻结。

## C1. 本轮真正改进的对象

冻结 root analytic R1–R16 给

\[
R_n(z)=\frac{(6n)!^2}{(2n)!^3}\frac{S_n(z)^3}{(z)_{6n+1}^2},\quad
S_n(z)=\prod_{j=1}^{2n}(z-j),\quad c_n=2n+\tfrac12,
\]
\[
K(z)=-4a(\pi\cot\pi z)''-b(\pi\cot\pi z)''',\quad
\xi=a\zeta(4)+b\zeta(5),\quad a,b\in\mathbf Z,\ b\ne0.
\tag{C1}
\]

取冻结的实际饱和整数值格 A_Z 的基 G_1,…,G_n,f_{2n},…,f_{3n−1}，记其 Newton 系数列为 S。这里 f_i(z)=binom(z−1,i)。D_A(X)=det(SᵀH_n(X)S) 是同一个原 whole-X 多项式；只在 X=ξ 处使用已经证明的真实轮廓表示。假设 ξ=c∈Q 后才能把这份积分识别为 D_A(c)。

设 m'=2n+1−m、β_m=gcd(b_m,b_m')、b_j=binom(6n+j,j−1)，Γ_n=∏β_m。冻结 energy E1 的实际低列为

\[
\frac{G_m(z)}{S_n(z)}=
\ell_m(z)=\frac{\kappa_m}{z-m}+\frac{\kappa_{m'}}{z-m'},\quad
\kappa_j=\frac{(-1)^j(6n+j)!}
{(6n+1)!\,\beta_m\,(j-1)!^2(2n-j)!}.
\tag{C2}
\]

(j−1)!² 不可删除。高列写成 S_n(z)h_k(z)/(2n+k)!，h_k=∏_{v=1}^k(z−2n−v)，0≤k<n；h_k 是 monic degree k，故其 span 准确为 degree<n 的所有多项式。记 F_n=∏_{k=0}^{n−1}(2n+k)!。

本文比冻结 separated Cauchy–Hardy/mirror upper bound 严格改善一项 n² 主率。最终不等式仍经过正 Gram 包络，故没有把“人工正包络最优”当成真实复行列式 no-go；另在 C9 给出保留真实复相位的精确接口。

## C2. 精确低高块消元，不改 whole-X determinant

取任意多项式 q，degree(q)≤n，且 q(j)≠0，1≤j≤2n。逐项恒等式

\[
\frac1{z-j}-\frac{q(z)-q(j)}{(z-j)q(j)}
=\frac{q(z)}{(z-j)q(j)}
\tag{C3}
\]

第二项是 degree≤n−1 的多项式。因此对每个低列 ℓ_m 减去

\[
p_m(z)=\sum_{j\in\{m,m'\}}
\kappa_j\frac{q(z)-q(j)}{(z-j)q(j)}
\]

是沿原高列 span 的精确剪切，剩下

\[
e_m(z)=q(z)\sum_{j\in\{m,m'\}}
\frac{\kappa_j}{q(j)(z-j)}.
\tag{C4}
\]

乘回 S_n 后全部仍为 degree<3n 的多项式。原整数基到新列的变换是 determinant1 的上/下三角剪切（依排列约定）；系数一般只在 Q 或 C 中，并不声称新列仍为原整数基。对所有 X，双线性 Gram 作 TᵀH(X)T 后 determinant 乘 det(T)²=1，所以 D_A(X) 完全相同。原整化费用直接继续用于这个同一多项式；理由是精确 determinant 恒等式，非“新基免费整化”或泛泛 height 忽略。

## C3. 保留耦合的全 n 正 Gram 上界

在 z=c_n+ix 上设

\[
W_n(x)=\frac{|R_n(z)K(z)|\,|S_n(z)|^2}{2\pi},\qquad
A_n(q)=\sup_{x\in\mathbf R}W_n(x)|q(c_n+ix)|^2.
\tag{C5}
\]

固定 n 下所有以下积分绝对收敛：K 在竖线按 e^(−2π|x|) 衰减；所有原/剪切列乘 S_n 后 degree<3n；R_n 与这些乘积至多 polynomial growth，故指数尾部支配。冻结 root R6 的有限展开也可对剪切列使用。

抽出每列的 common S_n 后，complex measure 为 dω_n=R_n(z)K(z)S_n(z)²dx/(2π)，其 total variation 准确为 W_n(x)dx。高列暂用未除 factorial 的 monic h_k，所以 D_A(ξ)=det B_q/F_n²。令 B_q 为 e/high 关于 dω_n 的 complex bilinear Gram，P_q 为相同列关于 W_n(x)dx 的 Hermitian Gram。真实 Andreief 加三角不等式给 |det B_q|≤det P_q，而 Hermitian Gram 的 block Schur 恒等式给

\[
\det P_q=\det H\;\det(E-C H^{-1}C^*)
\le\det H\;\det E.
\tag{C6}
\]

H 是高 monic 多项式 Gram，严格正定；它是人工正 Gram，H⁻¹ 的使用不假设真实高 block 非零。其 determinant 准确为

\[
Z_{H,n}=\frac1{n!}\int_{\mathbf R^n}
|\Delta(c_n+ix)|^2\prod_jW_n(x_j)\,dx_j.
\tag{C7}
\]

令镜像选择集合 𝒜_n 为每个 pair {m,m'} 恰取一个 a_m。用 C4 的 determinant 多线性在 L²(W_n^⊗n/n!) 中展开，只在这些既有 2^n 个镜像选择间用 triangle。每个选择的 Cauchy Gram 具有 weight W_n|q|²，因此 Loewner 上界 ≤A_n(q) 乘无权 Hardy Gram。记 δ_j=c_n−a_j>0，其 determinant 是冻结 E14 的

\[
\mathcal H_n(a)=(2\pi)^n\prod_j(2\delta_j)^{-1}
\prod_{i<j}\left(\frac{\delta_j-\delta_i}{\delta_j+\delta_i}\right)^2.
\tag{C8}
\]

于是得到真正全 n 界

\[
\boxed{
|D_A(\xi)|\le
\frac{Z_{H,n}A_n(q)^n}{F_n^2\Gamma_n^2}
\left(\sum_{a\in\mathcal A_n}
\prod_{m=1}^n\frac{|\widetilde\kappa_{a_m}|}{|q(a_m)|}
\sqrt{\mathcal H_n(a)}\right)^2,\quad
\widetilde\kappa_j=\beta_m\kappa_j.
}
\tag{C9}
\]

没有先拆 full compound 的 low/high Laplace triangle；旧 binom(2n,n) 因子甚至不必出现，其 O(n) 大小不参与以下主率。C9 保留实际 low/high 同一 Hilbert 空间的消元；Γ_n 及实际 high Gram 已全部显式支付。

## C4. 可支付的简单 q，奇偶 n 一并覆盖

取 N=floor(n/2)，

\[
q_n(z)=((z-c_n)^2+n^2)^N,\qquad \theta_n=2N/n.
\tag{C10}
\]

degree2N≤n；在所有真实 head 上 q_n(j)>0。q 的中心为 c_n=2n+1/2，而 head 镜像中心为 n+1/2，故两镜像 q 值一般不同。本文从未假定它们相同；C9 对每个实际 q(a_m) 分别计费。

冻结 energy E16/E18 的全域 envelope 是

\[
W_n(ny)\le C n^{4n+C}(1+|y|)^C e^{nQ(y)},
\]
\[
Q(y)=12\log6-6\log2-6+7J_2(y)-2J_8(y)-2\pi|y|,
\quad
J_A(y)=\int_0^A\log\sqrt{v^2+y^2}\,dv.
\tag{C11}
\]

这里 n y 是实际竖线 x，c_n/n=2+1/(2n) 的误差已经在上述 frozen uniform bound 中。没有换到恢复 κ4 布局。沿该竖线 q_n(c_n+iny)=n^(2N)(1−y²)^N，所以

\[
M_0=\sup_yQ(y),\quad
M_* =\sup_y\{Q(y)+\log|1-y^2|\}.
\tag{C12}
\]

在 y=±1 按 −∞ 解释第二式，sup 有限。对 θ∈[0,1]，

\[
\sup_y\{Q(y)+\theta\log|1-y^2|\}
\le(1-\theta)M_0+\theta M_*.
\tag{C13}
\]

因此 odd n 仅损失 O(n)，不用补一个会让近 head 小值失控的 odd 因子。n=1 时 q=1、θ=0，最终常数上界仍可覆盖。

## C5. 纸面证明 M_*≤M_0−1/16

对 y>0，冻结 E18 的导数为

\[
Q'(y)=7\arctan(2/y)-2\arctan(8/y)-2\pi,\quad
Q''(y)=-\frac{14}{4+y^2}+\frac{16}{64+y^2}.
\tag{C14}
\]

Q''<0 当 y²<416，Q''>0 当 y²>416，且 Q'→−2π。NEW 严格证书给 Q'(1/4)>0、Q'(1)<0、Q'(2)+4/3<0。因此 Q 在 [0,1/4] 增，在 [1,∞) 减；y≥2 时 Q'(y)≤max(Q'(2),−2π)<−4/3。

记 ε₀=1/16。八个有理区间证书中的四个主要 comparisons 以 1/20 为阈值，保存的下端再都严格大于 1/80，故同一不可重跑证书直接推出

\[
Q(1/4)+\varepsilon_0<Q(1/2),\quad
Q(1)+\varepsilon_0<Q(1/2),
\]
\[
Q(\sqrt2)+\log3+\varepsilon_0<Q(1/2),\quad
\log(15/16)<-\varepsilon_0.
\tag{C15}
\]

逐段控制，不用有限采样代替全域 supremum：

* 0≤y≤1/4：log|1−y²|≤0，故 ≤Q(1/4)<M₀−ε₀。
* 1/4≤y≤1：|1−y²|≤15/16，故 ≤M₀−ε₀，y=1 为 −∞。
* 1≤y≤√2：|1−y²|≤1，故 ≤Q(1)<M₀−ε₀。
* √2≤y≤2：Q≤Q(√2)、log(y²−1)≤log3，故 ≤M₀−ε₀。
* y≥2：导数 Q'(y)+2y/(y²−1)<0，因为第二项≤4/3；故 ≤Q(2)+log3≤Q(√2)+log3<M₀−ε₀。

Q 为偶函数，所以负半轴同样成立，完成

\[
\boxed{M_*\le M_0-1/16.}
\tag{C16}
\]

本证书只有严格 elementary constants 的作用。导数单调性、全域分段、奇偶 n、Gram/剪切恒等式是上述纸面证明，未冒称八项检查证明了所有 n 的 determinant。

### C5a. 同一已保存区间的纸面强化至 7/50，不修改成功程序

上面的粗分段保留为首次证书实际断言的依据。现在用同一八项保存区间作新增纸面推导：设 d=Q'(1/4)、c=51/20。保存区间严格给 1/2<d<763/1000、Q(1/2)−Q(1/4)>9/100、Q'(1)<−4/3、Q(1/2)−Q(1)>7/50。

对 0≤y≤1，由 C14 得 Q''≤−14/5+1/4=−c，强凹性与 log(1−y²)≤−y² 给

\[
Q(y)+\log(1-y^2)
\le Q(1/4)+d(y-1/4)-\frac c2(y-1/4)^2-y^2
\]
\[
\le Q(1/4)-\frac d4-\frac c{32}
+\frac{(d+c/4)^2}{2(c+2)}.
\]

末项相对于 Q(1/4) 的 offset 对 d>1/2 严格递增。代 d≤763/1000 后，offset+1/20=−178324/36400000<0。因此该全区间的上界严格小于 Q(1/4)−1/20<Q(1/2)−7/50≤M₀−7/50。y=1 处仍按 −∞ 解释。

对 y>1，C14 的先减后增结构及其 −2π 极限给 Q'(y)≤max(Q'(1),−2π)<−4/3。令 u=y−1>0，concavity 切线给

\[
\log(y^2-1)=\log u+\log(u+2)
\le(u-1)+\log3+(u-1)/3
<4u/3.
\]

最后一步 log3<4/3 可直接在 [1,3] 积分 1/t≤(4−t)/3 且内点严格的上界证明。因此 Q(y)+log(y²−1)<Q(1)<M₀−7/50。负半轴按偶性覆盖，新增全域纸证为

\[
\boxed{M_*\le M_0-7/50.}
\tag{C16a}
\]

本强化没有改动成功 PY/JSON/guard，没有第二次数学执行。源执行时只 assert 原八个 comparisons；d 与 Q 差值的纸面比较、强凹性和切线估计在本节明确推导，不伪称首次程序已 assert 7/50。

## C6. 不遗漏无穷尾部、poly prefactor 与实际 head 值

Q(y)=−2π|y|−2log|y|+O(1)，故 uniformly θ∈[0,1]，Q+θlog|1−y²|≤−π|y| 当 |y| 足够大。其 finite maximum 统一有界，compact 部分的 (1+|y|)^C 有界；tail 的 polynomial prefactor 由 e^(−nπ|y|) 支配。这证明从 C11–C16a 得

\[
\log A_n(q_n)\le(4n+4N+C)\log n
+n(M_0-7\theta_n/50)+O(1).
\tag{C17}
\]

所有 C、O 常数只依赖固定 a,b，非镜像选择和 n；n=1 单独增大常数即可。

对任意 mirror choice，δ_left=2n+1/2−m，δ_right=m−1/2，故 δ_choice≥m−1/2。于是

\[
\sum_m\log q_n(a_m)
\ge 2Nn\log n+N\sum_{m=1}^n
\log\left(1+\left(\frac{m-1/2}{n}\right)^2\right).
\tag{C18}
\]

函数 log(1+t²) 在 [0,1] 的导数≤1；midpoint Riemann 误差给该 sum≥nI−1/2，其中

\[
I=\int_0^1\log(1+t^2)\,dt=\log2-2+\pi/2.
\tag{C19}
\]

因此 C9 的每项均被同一个旧镜像 coefficient 项乘
n^(−2Nn)e^(−NnI+N/2) 支配。没有用虚假的 q 镜像相等，也没有分别最大化未匹配 height；实际 low/high 与每个选择的 q 值都已计入。

综合 C17–C19，低块的整个共同因子满足

\[
\log\left(A_n(q_n)^n n^{-4Nn}e^{-2NnI+N}\right)
\le4n^2\log n+n^2 M_0
-2Nn(7/50+I)+O(n\log n).
\tag{C20}
\]

2Nn=n²（even）或 n²−n（odd），差准确为 O(n)。旧 high Gram Z_H/F_n²、old mirror Hardy sum、原 Γ_n 全部 unchanged，故这些已经支付的主率不能再扣一次。

## C7. 同一原格的严格新率

冻结 mirror M13 的 separated bound 给 β_mirror>9.09188285412558；原 Γ 的下率 γ≥1.455845 已只支付一次，从而此前总解析率 >12.00357285412558。C20 在完全相同的 Stirling/n²logn cancellation 中额外给

\[
\boxed{\varepsilon=7/50+I=7/50+\log2-2+\pi/2.}
\tag{C21}
\]

该结论是先有全 n C9/C17/C18，再接旧已证 rates，不把前几项 determinant 的数值 decay 当定理。可不用任何新增小数计算给保守有理下界：log(1+u) 的八项 alternating lower polynomial 在 u∈[0,1] 上有效，积分得

\[
I\ge\sum_{j=1}^8\frac{(-1)^{j+1}}{j(2j+1)}
=\frac{1597121}{6126120}>\frac{13}{50},
\]
\[
\boxed{\varepsilon>2/5=0.4,\qquad
\limsup_{n\to\infty}\frac{\log|D_{A,n}(\xi)|}{n^2}
<-12.40357285412558.}
\tag{C22}
\]

严格 limsup 号来自 frozen baseline rate 本身严格大于所写常数；D_A(ξ)=0 的项取 log0=−∞。精确 ε 约0.40394，但本文的已认证保守结论只需 C22。

同一原格算术 signed rational normalization scale safeA≈40.314517426059346 仍高于新已证解析率。该 upper scale 与 decay 的比较尚未 strict；更不把 safe 上界不足当 actual arithmetic cost 下界或方法 no-go。没有新增 ξ、ζ(7)、Catalan 无理性或线性无关性定理。

## C8. 任意 q 的变分入口与当前证明范围

C9 对任意 degree≤n、head 不为零的 q 成立；它是可继续优化的 weighted polynomial approximation 问题，而非改变原整数格。若 q 用多对 vertical roots ±inr_j，可同时保留真实 denominator values 和 numerator log factors。任何选择都必须共同计算

\[
n\log\sup W_n|q|^2-2\sum_m\log|q(a_m)|
\]

及同一个 mirror Hardy coefficient，不能只压 numerator 然后免费忽略 head denominator。这正是下一次大幅收益可能发生的地方；本文没有求全局 optimal q、没有假定对称 S-curve 自动适用，也没有声称本次 ε 是可达的上限。

精确 positive Schur formula C6 还能先做实际 orthogonal projection，而不是只用一个 q remainder。其遗漏项 C H⁻¹C* 非负；本次 q 剪切仅构造一个显式全尺度上界，不是证明 exact Schur eigenvalue rate 已求出。

## C9. 真实复相位的精确接口，不能把 O(n) 信用当 D²

这段用原基 g_i、原 complex measure dμ=R_nK dx/(2π)，正 measure dν=|dμ|，避开 q 表达的记号混淆。记 B_ij=∫g_i g_j dμ、G_ij=∫g_i overline(g_j)dν，G>0，C=G^(−1/2)。令 e=Cg、τ=dμ/dν（zero density 处任意取 modulus1），

\[
T_{ij}=\int e_i e_j\tau\,d\nu.
\quad T=CBC^{\mathsf T},\qquad
\boxed{|D_A(\xi)|=\det G\,|\det T|.}
\tag{C23}
\]

e_i orthonormal；Cauchy–Schwarz 给 |vᵀTw|≤||v||₂||w||₂，故所有 singular values σ_j(T)≤1。这可以等价看作 phase-times-conjugation antiunitary 在 V=span(e_i) 上的 compression，保留真实 complex phase，非把 τ 换成1。

若要由此再得到 κn² 主率，需要证明 Σ_j−logσ_j≥κn²。例如 cn 个 singular values≤e^(−dn) 时给 cd n²。仅有一个 fixed-size defect、仅有 σ≤ρ<1 的 O(n) 个方向，或 trace(I−T*T)≥cn，都只保守给 O(n) 而非自动 n²；这不是说更强估计不存在。detT 可为0；证明其无限次非零仍是独立目标，C23 的 artificial G 正性不给该结论。

## C10. 一手文献实读、启发与未套用条件

本轮 NEW 原件全部以 arXiv 正常 TLS 保存于 literature/cdt_paired_complex_gram_sources_20261007：

1. Borodin, *Biorthogonal ensembles*, math/9804027v1，26页；本人实际 PDF1–8。Eq2.8–2.15 与 Proposition2.2 的 finite moment/inverse kernel 视角启发 C6/C23，但其 asymptotic Jacobi/Laguerre/Hermite model 不是当前 actual paired basis。
2. Bertola–Gekhtman–Szmigielski, *Cauchy Biorthogonal Polynomials*, 0904.2602v1，38页；本人实际 PDF1–10、13–14。Theorem2.1 的 strict TP 要 real ordered supports、TP kernel、positive Stieltjes measures；当前 τ/vertical z 不满足，不能以它推出 D_A(ξ) 非零。它的 rank-one shift/Cauchy结构启发保留耦合，而本文所用 finite Gram 恒等式均直接自证。
3. Bertola, *Moment determinants as isomonodromic tau functions*, 0805.0446v1，24页；本人实际 PDF1–4、9–11。§3 semiclassical weight 要 V' rational，§4及Theorem4.1 要对应 moment/RHP 正确识别。当前 cot derivatives 的 logarithmic derivative 具有周期 poles，实际低列亦是 paired rational source；本文未完成这一 rational-connection/tau 识别，不能把 tau 非零或 Schlesinger 标准式免费接入。
4. Kuijlaars–Silva, *S-curves in Polynomial External Fields*, 1311.7026v1，33页；本人实际 PDF1–7。Theorem2.3针对 polynomial V degree≥2 与指定 admissible contour class；当前 Q 含 J/log 与 |y|、real lattice poles 和 paired determinant，不能直接套该 S-curve 存在定理。合理下一接口需针对 actual q/C23 的矩阵或向量平衡逐项证明条件。

共121归档页，本人实际34distinct页；未称这些 PDF 全文读。尝试 Mathnet 的 Gonchar–Rakhmanov 原文下载遇正常 TLS issuer 校验失败，未保存、未关闭证书检查；其 locator 不作为本文定理依据。所有 PDF 只读提取没有执行数学 producer。新严格证书已保存 source/output/guard，成功后永久不重跑；精确 fingerprints 与实际 source receipts 待 root 实际独审后再一向最终归档。

本轮完成的数学是 C9 的真实 coupled all-n estimate、C16/C16a 全实轴压低、C20 全尺度费用支付及 C22 新解析率，以及 C23 的 actual complex-phase reduction。剩余是足够大的同对象 strict margin、无限 actual determinant 非零、或真正价值敏感的全局 holonomy 输入；本轮不把这些未证条件写成结论。
