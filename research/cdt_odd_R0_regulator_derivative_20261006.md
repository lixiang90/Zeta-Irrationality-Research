# 唯一 R0 family symbol 的 compact regulator 微分：ell=4 的独立 current 证明

日期：2026-10-06。NEW 全尺度纸面证明。实际全文读冻结 toric completion 与 uniqueness 稿，重新核 KLM、KLII、Li、DK 和 Deligne 原件；旧稿、同行稿、Python、JSON、manifest 全部只读，未执行或 import mathematical producer。本稿不调用 DK Lemma4.1 的 ell=2,3 结论作为 ell=4 定理。

## 1. 固定对象及本轮结论

沿冻结模型取
\[
\phi(v)=\prod_{j=0}^3(1+v_j)^2/v_j,\qquad
Y=f^{-1}(\mathbf G_m)\subset\widetilde P,\qquad Y^*=U^4,
\quad U=\mathbf P^1_{\mathbf Q}\setminus\{0,\infty,-1\}.
\]
\(Y\) 是光滑四维 variety，\(f\) proper projective。令
\[
B=\mathbf G_m\setminus\{256\},\quad Y_B=f^{-1}(B),\quad
X_\lambda=f^{-1}(\lambda),\quad X_\lambda^*=X_\lambda\cap Y^*.
\]
冻结 toric 稿已证明 \(f:Y_B\to B\) smooth，边界 \(E_B\) 是 relative SNC：所有边界 intersections 到 \(B\) 都 smooth。冻结 uniqueness 稿给唯一且非零的
\[
\Xi\in CH^4(Y,4)_{\mathbf Q},\qquad \Xi|_{Y^*}=\xi=\{v_0,v_1,v_2,v_3\}.
\]
下面研究这个指定 \(\mathbf Q\)-family class 的 complex regulator；没有在 base change 后重新选择另一 completion。

记 \(\Omega=d\log v_0\wedge\cdots\wedge d\log v_3\)，并固定旧真实周期稿 §3 的 **左** residue convention：
\[
\frac{\Omega}{\phi-\lambda}
=\frac{d(\phi-\lambda)}{\phi-\lambda}\wedge\rho_\lambda
\quad\text{mod regular forms},\qquad
\rho_\lambda=\operatorname{Res}_{X_\lambda^*}\frac{\Omega}{\phi-\lambda}.
\tag{R1}
\]
本稿证明：

1. \(\Omega\) 在整个 \(Y\) 上延拓为 holomorphic algebraic \(4\)-form \(\Omega_Y\)，\(\rho_\lambda\) 延拓为 compact \(X_\lambda\) 上的 holomorphic \(3\)-form。
2. 对每个小 simply connected analytic disk \(D\subset B(\mathbf C)\)，存在 holomorphic cohomology lift \(R_\lambda\) of
   \(AJ(\Xi_\lambda)\in H^3(X_\lambda,\mathbf C)/H^3(X_\lambda,\mathbf Q(4))\)，且
\[
\boxed{\nabla_{\partial_\lambda}R_\lambda=[\rho_\lambda]\quad
\text{in }H^3(X_\lambda,\mathbf C).}
\tag{R2}
\]
   不同连续 lifts 的差为 flat rational Tate class，因此此微分无 lift ambiguity。
3. 对这个实际 compactification，
\[
\boxed{H^3(X_\lambda,\mathbf Q)\longrightarrow H^3(X_\lambda^*,\mathbf Q)
\text{ injective}.}
\tag{R3}
\]
   所以这里不存在 compact degree-three cohomology 在 open restriction 中丢失的 kernel。

这些结论不识别某个 raw graph-current pairing 与 compact higher normal function 的精确 Betti lift，不删除 closed-period ambiguity，不证明 conifold special value、积分格 saturation 或数值无理性。

## 2. toroidal boundary 上的真实 top-form 延拓

在冻结稿的某个 fixed-grid chart，用 \(z_i=v_i,1/v_i,v_i+1\) 分别对应 fixed coordinate \(0,\infty,-1\)。对 fixed \(0,\infty\)，\(d\log v_i=\pm d\log z_i\)；对 fixed \(-1\)，
\[
d\log v_i=\frac{z_i}{z_i-1}\,d\log z_i.
\]
因此在 toric monomial modification 上，\(\Omega\) 等于 logarithmic toric volume form 乘一个 unit 和 \(\prod_{v_i=-1}z_i\)。若 primitive ray \(a\) 给一个 boundary divisor，其 order 为
\[
\operatorname{ord}_{E_a}\Omega
=\sum_{i:v_i=-1}a_i-1.
\tag{R4}
\]
理由是 smooth toric chart 的 invariant logarithmic volume form 对每个 toric prime divisor 恰有一个 simple pole；原 monomials \(z_i\) 的 order 是 \(a_i\)。

在 \(Y\) 中保留的 rays 全部 horizontal，满足
\[
2\sum_{v_i=-1}a_i=\sum_{v_i=0,\infty}a_i.
\]
其 minimum support 同时有两类 coordinates，所以左边的整数和至少为1。R4 非负。其它 boundary divisors 处于 \(f=0,\infty\)，已从 \(Y\) 删去；interior 上所有 \(v_i\) 是 units。故 \(\Omega\) 在 \(Y\) 上每个 prime divisor 均无 pole。\(Y\) 光滑，canonical line bundle 是 reflexive；这个 rational section 在 codimension one 无 pole即为全局 regular section。得 \(\Omega_Y\)。

在 smooth family 的局部 holomorphic coordinates \((\lambda,z_1,z_2,z_3)\) 中，可写成
\[
\Omega_Y=d\lambda\wedge\eta.
\]
\(\eta\) modulo含 \(d\lambda\) 的 forms唯一；其 fibre restriction与 R1 的 \(\rho_\lambda\) 在 dense open 相同，故给出 compact holomorphic 延拓。这里没有把原 nonreduced facets 当成 smooth toric hypersurface boundary，也没有要求 \(\phi\) 是 Δ-regular。

## 3. arbitrary-n KLM 输入：精确次数、符号和 Tate 因子

只采用 rational real-admissible moving。KLM 原件早期 integral-moving 表述不能无修正地使用；Li2018 PDF2、4 Theorem2.4 明确其已证明版本是 \(\mathbf Q\)-quasi-isomorphism。KLII fixed v1 PDF53–59 的 Lemma8.14/8.16 给指定 smooth subvariety 的 real good position、quasiprojective moving，以及 commuting pullback 的 current complex。这里可用原 smooth projective compactification \(\widetilde P\)：其 reduced vertical boundary \(f^{-1}(0,\infty)_{\rm red}\) 是 toroidal SNC divisor，每个 smooth fibre \(X_\lambda\) 与它不交，故 Lemma8.16 的 fibre/boundary intersection前提全部满足。

取 real-admissible closed precycle \(C\) 代表 \(\Xi_{\mathbf C}\)。KLM §5 convention 是
\[
\partial_B=\sum_i(-1)^{i-1}(\partial_\infty^i-\partial_0^i)
=\sum_i(-1)^i(\partial_0^i-\partial_\infty^i).
\]
KLM published PDF11，Eq.(5.5)，对任意 \(p,n\) 给
\[
\partial T_C=T_{\partial_B C},\quad
d\Omega_C=2\pi i\,\Omega_{\partial_B C},\quad
dR_C=\Omega_C-(2\pi i)^n\delta_{T_C}-2\pi iR_{\partial_B C}.
\tag{R5}
\]
在 \(p=n=4\) 上，\(\partial_BC=0\)，故
\[
dR_C=\Omega_C-(2\pi i)^4\delta_{T_C},\qquad
\Omega_C\in F^4\mathcal D^4(Y),\quad R_C\in\mathcal D^3(Y).
\tag{R6}
\]
KLM PDF12 的 cohomological prefactor 是 \((-2\pi i)^{p-n}\)，这里恰为1。对应 rational lattice 是 \(\mathbf Q(4)=(2\pi i)^4\mathbf Q\)，不会在 R2 中额外出现 \(2\pi i\) 或其倒数。

因为 \(Y\) complex dimension4，\(F^4\mathcal D^4(Y)\) 只有 type \((4,0)\)。R5 给 \(d\Omega_C=0\)，所以 distributional \(\bar\partial\)-regularity 说明 \(\Omega_C\) 实际是 holomorphic \(4\)-form。这个结论是 closed top-type current 的局部 regularity，不是一般 current 自动光滑。

在 \(Y^*\) 上，\(C\) 与 unit graph symbol \(\xi\) 代表同一 higher-Chow class，差是 \(\partial_B M\)，\(M\) 的 \((p,n)=(4,5)\)。若需要 real-admissible \(M\)，在该 open variety 上使用同一个 rational quasi-isomorphism；graph symbol在 interior 上已经有 real good position。有
\[
\Omega_M\in F^4\mathcal D^3(Y^*)=0.
\]
KLM 的 map-of-complexes 故给 \(\Omega_{\partial_B M}=0\)。Graph symbol 的 \(\Omega_\xi\) 恰为 \(\Omega\)。因此
\[
\Omega_C|_{Y^*}=\Omega,\qquad
\boxed{\Omega_C=\Omega_Y\ \text{on all }Y.}
\tag{R7}
\]
最后一步是两个 holomorphic forms 在 dense open 相同。所有可能 boundary corrections 的 top-form 已被严格排除；没有仅在 generic field 比较。

## 4. local compact lift：BM membrane 与 de Rham smoothing

取小 contractible disk \(D\subset B(\mathbf C)\)，写 \(Y_D=f^{-1}(D)\)。proper smoothness 和 Ehresmann 给 \(Y_D\) 与某个 compact fibre 的 homotopy equivalence。因此
\[
H^4(Y_D,\mathbf C)\xrightarrow{\sim}H^4(X_{\lambda_0},\mathbf C).
\]
R7 的 \(\Omega_Y\) pullback 到 complex dimension3 的 fibre 是0，所以 \([\Omega_Y]=0\) on \(Y_D\)。R6 得
\[
(2\pi i)^4[T_C]=[\Omega_Y]=0.
\]
\(T_C\) 为 rational Borel–Moore chain，其 rational cohomology class 也为0：从 rational cohomology 到 complex cohomology 的 map 是 injective。由 Poincaré duality，\(T_C\) 在 BM homology 中 bounds 一个 rational BM \(5\)-chain \(\zeta\)，\(\partial\zeta=T_C\)。KLM current differential convention 在这里给 \(d\delta_\zeta=\delta_{T_C}\)。定义
\[
\widetilde R=R_C+(2\pi i)^4\delta_\zeta,\qquad d\widetilde R=\Omega_Y.
\tag{R8}
\]
这是 compact fibrewise regulator lift 的 membrane correction，尚未指定与旧 cube/tube marking 相同的 \(\zeta\)。

由于 \(\Omega_Y\) 的 ordinary de Rham class为0，取 smooth \(3\)-form \(\eta_0\) 满足 \(d\eta_0=\Omega_Y\)。Closed current \(\widetilde R-\eta_0\) 有 smooth closed representative \(a_0\)，其差为 exact current。故可选择 smooth \(3\)-form
\[
S=\eta_0+a_0,\quad dS=\Omega_Y,\quad S-\widetilde R=dK
\tag{R9}
\]
（适当调整 \(K\) 的符号）。每个 fibre restriction \(S|_{X_\lambda}\) 都 closed。

必须核其 class确实 lifts \(AJ(\Xi_\lambda)\)。对任意指定 fibre，KLII moving 让 \(C\) 变成 \(C'=C+\partial_B M\)，其中 \(C'\) real-admissible 并可 pullback 到该 fibre，\(M\) real-admissible。因为 \(\Omega_M=0\)，R5 精确给
\[
R_{\partial_B M}=-\frac{dR_M}{2\pi i}-(2\pi i)^4\delta_{T_M},
\quad T_{\partial_B M}=\partial T_M.
\]
同时取 \(\zeta'=\zeta+T_M\)（再作保持 boundary 的 topological move）。于是
\[
\bigl(R_{C'}+(2\pi i)^4\delta_{\zeta'}\bigr)
-\bigl(R_C+(2\pi i)^4\delta_\zeta\bigr)
=-\frac{dR_M}{2\pi i}.
\tag{R10}
\]
若 primitive 尚不能直接 pullback，KLII PDF50–52 Lemma8.7 的 intersection-current filtered quasi-isomorphism 让这个 exact current 取得可 pullback 的 primitive；因此其 fibre restriction 是 exact。KLM PDF13 的 membrane prescription 与 KLII PDF59 的 commuting pullback，说明 R9 的 fibre cohomology class正是 \(AJ(\Xi_\lambda)\) 的 lift。没有要求一个 raw representative 同时 transverse 所有 fibres。

## 5. Cartan 微分及左 residue 正号

令 \(V\) 是 \(\partial_\lambda\) 的任意 smooth horizontal lift。Cartan formula 对 R9 给
\[
\nabla_{\partial_\lambda}[S|_{X_\lambda}]
=[(\iota_VdS)|_{X_\lambda}]
=[(\iota_V\Omega_Y)|_{X_\lambda}]
=[\rho_\lambda].
\tag{R11}
\]
Exact 项 \(d\iota_VS\) 在 fibre cohomology 中消失。两个 lifts \(V\) 的差 vertical；其 contraction \(\Omega_Y=d\lambda\wedge\eta\) 限制到 fibre为0，所以 R11 无 horizontal-lift ambiguity。对 antiholomorphic base direction，holomorphic top-form 的 contraction为0，所以这些 local cohomology lifts是 holomorphic sections。

Tate-lattice 中两个 continuous cohomology lifts的差是 flat \(H^3(X_\lambda,\mathbf Q(4))\)-section；在 local flat coordinates中，一个 continuous function若取值于 countable rational vector space，只能局部常值。故 \(\nabla\) 消除此 lift ambiguity。

正号依赖 R1 中 normal differential放在左边。直接有 \(\Omega=d\phi\wedge\rho_\lambda=d\lambda\wedge\rho_\lambda\)，因而 contraction是 \(+\rho_\lambda\)。冻结 toric 稿 §8 的负号仅是未证明候选；本稿将其纠正。不能把 DK Lemma4.1 proof 的 right-wedge \(ds\) 形式跳过 contraction 的 parity，直接照搬至 ell=4。作为独立符号核对，DK Cor4.1 的 \(t=1/\lambda\) 规范满足
\[
\omega_t=\operatorname{Res}\frac{\Omega}{1-t\phi}
=-\lambda\rho_\lambda,\qquad
\nabla_{t\partial_t}R=\omega_t,\quad t\partial_t=-\lambda\partial_\lambda,
\]
同样对应 R11 的正号；这里不以该 corollary 的 regular-family 定理作为证明输入。

旧真实几何的 exact identity 是
\[
\Omega_x^{\rm cube}=\frac{16\Omega}{\phi-256x},\quad
\omega_x=\sqrt{x}\operatorname{Res}\Omega_x^{\rm cube}
=16\sqrt{x}\rho_{256x}.
\]
故在选定 \(\sqrt{x}\) branch（或 algebraic cover）上
\[
\boxed{\nabla_{\theta_x}R=16\sqrt{x}\,[\omega_x].}
\tag{R12}
\]
R12 是 compact \(H^3\) 的 cohomological regulator derivative，尚不是某个 scalar period 与 \(W\) 的相等式。

## 6. 全部 compact H3 的 open restriction kernel 实际为零

令 \(E_\lambda=X_\lambda\setminus X_\lambda^*\)，其 irreducible components \(E_{i,\lambda}\) 都是 smooth projective surfaces。冻结 toric global product式显示其 dense open strata在 fibre上为
\[
U^2,\qquad U\times\mathbf G_m,\qquad \mathbf G_m^2.
\]
各 lower boundary strata 在 fibre中 dimension≤1；因此不可能另有一个完全处于 lower strata 的 surface component。上述 connected irreducible dense open强制 \(E_{i,\lambda}\) irreducible，且 rational。Smooth projective rational surface有 \(H_1=H_3=0\)：取与 \(\mathbf P^2\) 的 common resolution，surface indeterminacy由 point blowups消除，point blowup只增加 degree-two cohomology，degree-one、three cohomology不变。

令 \(\widetilde E_\lambda=\coprod_iE_{i,\lambda}\to E_\lambda\)，它是这个 SNC union 的 resolution。Deligne HodgeIII PDF37（printed40）Corollary8.2.8 给 graded Gysin exactness；在 target degree3，显式为
\[
\bigoplus_i H^1(E_{i,\lambda},\mathbf Q)(-1)
\xrightarrow{\sum(i_i)_*}H^3(X_\lambda,\mathbf Q)
\longrightarrow H^3(X_\lambda^*,\mathbf Q)
\quad\text{exact}.
\tag{R13}
\]
左项为0；等价地，surface Poincaré duality下对应 homological source
\[
H_3(\widetilde E_\lambda,\mathbf Q)=\bigoplus_iH_3(E_{i,\lambda},\mathbf Q)=0.
\]
得 R3。该原始 corollary已经处理 reducible/singular boundary的 intersections，无需假造一般支持群 spectral sequence。Kernel在 complex coefficients及 \(\mathbf C/\mathbf Q(4)\) coefficients上也为零：这两个 coefficient groups都是 \(\mathbf Q\)-vector spaces，R3 与它们作 \(\mathbf Q\)-tensor 时 exactness保持。不是一般 quotient functor保持单射的断言。Compact与open fibre均 complex dimension3，因此 \(F^4H^3=0\)；在 \((p,n)=(4,4)\) 的 regulator target上，\(AJ=H^3(\mathbf C/\mathbf Q(4))\)。故 compact AJ class的 open restriction 也 injective。

这没有给 integral saturation，也没有识别 rank-four PF module是全部 compact \(H^3\)。它只给本例明确的 restriction kernel，以及 R2 所在 compact cohomology的可靠接口。

另有一个作用域明确的非零性 corollary。旧真实周期稿 §3 的 compact cycle \(\Gamma_x\subset X_{256x}^*\) 满足
\[
\int_{\Gamma_x}\rho_{256x}
=-\frac{i\pi^3}{4\sqrt{x}}\,y_0(x)\ne0\qquad(0<x<1),
\]
因为 \(y_0(x)={}_4F_3(\frac12^4;1^3;x)\) 的各级数系数为正。因此 R2 的 regulator family 不平坦，也不恒为零。局部 flat coordinates中的每个 rational Tate value \(q\) 与 holomorphic lift \(R_\lambda\) 相等的 locus至多 discrete，否则 identity theorem使其恒等于 \(q\)，与非零 derivative矛盾。Lattice为countable，故在该 analytic parameter域除至多 countable subset外，\(AJ(\Xi_\lambda)\ne0\)。这是 very-general参数的 statement；不证明任何指定 algebraic参数（尤其 conifold）上的 regulator 非零或目标数无理性。

## 7. 对 raw current 与 scalar forcing 的限制

若某项 current确为 boundary pushforward \(i_*K\)，与 compact holomorphic \(3\)-form的 pairing为0，因为 \(i^*\omega_x=0\) on complex surface。这不能删去一个 Bloch homotopy或 membrane correction所带来的 closed-period class。

尤其 meromorphic coordinate raw graph在该 resolved boundary上可能有 shared zero/pole divisors，不自动满足多个 cube faces的 proper intersection；正切或 rotated-cut 的 raw-symbol积分不能免费视为代表 \(\Xi\) 的完整 admissible current。唯一性定理只固定 higher-Chow class；R3 只固定 regulator class的 compact extension；R8 的具体 membrane和 R9 的具体 Betti lift仍须与旧真实 cube/tube chain比较。

因此本稿不证明 \(\langle R,\omega_x\rangle=-16(2\pi i)^3W\)，也不删除允许的 homogeneous period。本稿不计算 Yukawa constant，不作 rank-four polarization或 integral projector证明，不处理 singular \(\lambda=256\) 的 integral nearby-cycle lift；没有新的目标数无理性或线性无关性结论。

## 8. 实际来源范围

* KLM, published Compositio142(2006),374–396：NEW23-page原件；本审阅者实际读 PDF1、8–23。核心是 PDF10–13 (5.2)–(5.5)、normalization和 membrane；PDF17 §5.9 quasiprojective注意事项；早期 integral-moving claim不作为前提。
* Kerr–Lewis, KLII fixed arXiv math/0611333v1，封面日期2006-11-11：NEW68-page原件（本地 filename含2007，不把它当作v1日期）；本审阅者实际读 PDF1、50–61。核 real/rational moving、指定fibre pullback、intersection-current quasi-isomorphism和map-of-complexes。
* Li2018, SIGMA14,118：NEW12-pagepublished primary；本审阅者实际读 PDF1–4、7–8、11。Theorem2.4只在 rational coefficients使用；不把 integral-regulator construction额外转化成 integral uniqueness。
* DK2011 published204-page原件：本轮重新实际读 PDF5–15、20–25、30–37、57–83。用于核 general current 与 proper-family smoothing的脉络；ell2,3 Lemma4.1与regular-family corollaries不直接套用。
* Deligne1974 HodgeIII frozen74-page原件：本轮实际读 PDF35–41，尤其 PDF37 Cor8.2.8，得到 R13 的实际 compact kernel。
* 三份冻结输入稿均实际全文阅读：toric completion、family uniqueness、真实 relative-cycle mirror。

精确URL、pages、SHA和阅读范围见本稿新的 literature/manifest_cdt_odd_R0_regulator_derivative_20261006.json。本文全部新增数学为上述纸面推导；未创建或运行 mathematical producer、未使用 numerical PSLQ、未宣称 Lean formalization。
