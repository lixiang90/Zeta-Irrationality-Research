# R0 toric family 的 boundary Chow 群消失与 completion 唯一性：独立核查

日期：2026-10-06。本稿只核查一个新的正结论：在已构造 split toroidal family 的实际 boundary strata 下，coordinate-symbol completion 在 rational higher-Chow **class** 层面唯一。未执行、导入或修改任何旧 mathematical producer；旧 Markdown、Python、JSON 与 manifest 全部只读。本稿不宣称新的数值无理性、regulator-current equality 或 Betti lift uniqueness。

## 1. 几何输入和精确结论

实际全文读取 `cdt_odd_R0_toric_completion_20261006.md`。本核查采用该稿 §4 的已明确几何输入：\(Y/\mathbb Q\) 是光滑四维 quasi-projective variety，\(Y^*=U^4\)，\(U=\mathbb P^1\setminus\{0,\infty,-1\}\)，且 \(E=Y\setminus Y^*\) 是 split SNC divisor。

设 \(D^r\subset E\) 是至少 \(r\) 个 boundary components 相交的 closed union，\(D^{r,*}=D^r\setminus D^{r+1}\)。有限个 strata 实际是

\[
D_{S,\tau}^{\circ}\simeq U^{4-s}\times\mathbb G_m^{s-r},
\qquad 2\le s\le4,\quad 1\le r\le s-1.
\]

因此 \(D^{1,*}\) 的 components 是三维 rational-open-curve products；\(D^{2,*}\) 的 components 是 \(U\times\mathbb G_m\) 或 \(\mathbb G_m^2\)；\(D^{3}=D^{3,*}\) 的 components 是 \(\mathbb G_m\)；\(D^4=\varnothing\)。这里所有 varieties 和 removed points 均定义于 \(\mathbb Q\)，不是在 \(\mathbb Q(x)\) 上计算。

在这些输入下，新结论为

\[
\boxed{CH^3(E,4)_{\mathbb Q}=0.} \tag{1.1}
\]

由 localization 得

\[
\boxed{CH^4(Y,4)_{\mathbb Q}\longrightarrow
CH^4(Y^*,4)_{\mathbb Q}\text{ 是单射}.} \tag{1.2}
\]

故 toric-completion 稿已构造的 lift \(\Xi\) 是唯一的 rational higher-Chow class。完整 fixed-lattice resolution 和全局 split identification 的几何证明未由本稿重新构造；这里独立核查的是从上述实际 strata 到 (1.1)–(1.2) 的 group-theoretic 推导。

## 2. 三个 base groups 与 weight-one vanishing

以下全部 groups tensor \(\mathbb Q\)。Doran–Kerr published PDF25 的 Bloch–Grothendieck–Riemann–Roch identification 给

\[
K_q^{\rm alg}(k)_{\mathbb Q}\simeq
\bigoplus_p CH^p(k,q)_{\mathbb Q}.
\]

同一 primary PDF26 对 number fields 明确 \(K_{2m}(k)_{\mathbb Q}=0\)，并且 \(CH^2(k,3)_{\mathbb Q}=0\) 对 totally real \(k\)。于是

\[
CH^2(\mathbb Q,3)_{\mathbb Q}=0,
\quad CH^2(\mathbb Q,4)_{\mathbb Q}=0,
\quad CH^3(\mathbb Q,4)_{\mathbb Q}=0. \tag{2.1}
\]

后两项是同一个 rational even-\(K_4\) 消失的 Adams summands，不能误写成关于 arbitrary function fields 的 Beilinson–Soulé conjecture。

对每个 smooth \(Z/\mathbb Q\)，MVW Theorem4.1/Corollary4.2 给 weight-one motivic complex \(\mathbb Z(1)\simeq\mathcal O^*[-1]\)；Theorem19.1 给

\[
CH^1(Z,q)=H^{2-q,1}(Z,\mathbb Z).
\]

因此

\[
CH^1(Z,q)=0\qquad(q\ge2). \tag{2.2}
\]

这条 statement 对所有所用 smooth quasi-projective products 有效，而不是仅对 generic point 有效。

## 3. 不使用 motive splitting 的 product 归纳

令 \(A=\mathbb P^1_{\mathbb Q}\setminus T\)，其中 \(T\) 是非空有限个 \(\mathbb Q\)-points。令 \(Z/\mathbb Q\) smooth quasi-projective。Levine Corollary5.4 的 rational projective-bundle formula 给

\[
CH^p(Z\times\mathbb P^1,q)_{\mathbb Q}
\simeq CH^p(Z,q)_{\mathbb Q}\oplus CH^{p-1}(Z,q)_{\mathbb Q}. \tag{3.1}
\]

对 removed sections \(Z\times T\subset Z\times\mathbb P^1\)，localization 的相邻部分是

\[
CH^p(Z\times\mathbb P^1,q)_{\mathbb Q}
\longrightarrow CH^p(Z\times A,q)_{\mathbb Q}
\longrightarrow \bigoplus_{t\in T}CH^{p-1}(Z,q-1)_{\mathbb Q}. \tag{3.2}
\]

从 (2.1) 开始对 factor 数量归纳。若对 \(Z\) 已知

\[
CH^2(Z,3)=CH^2(Z,4)=CH^3(Z,4)=0,
\]

则：

1. \((p,q)=(2,3)\)：(3.1) 的第二项 \(CH^1(Z,3)\) 和 (3.2) 的右项 \(CH^1(Z,2)\) 由 (2.2) 消失，故 \(CH^2(Z\times A,3)=0\)。
2. \((p,q)=(2,4)\)：对应项是 \(CH^1(Z,4)\) 和 \(CH^1(Z,3)\)，也都为零，故 \(CH^2(Z\times A,4)=0\)。
3. \((p,q)=(3,4)\)：(3.1) 的第二项是已知为零的 \(CH^2(Z,4)\)，(3.2) 的右项是已知为零的 \(CH^2(Z,3)\)，故 \(CH^3(Z\times A,4)=0\)。

所以对任意有限个这类 rational-open curves 的 product \(Z\)，包括零个 factors 的 \(\operatorname{Spec}\mathbb Q\)，严格有

\[
\boxed{CH^2(Z,3)_{\mathbb Q}=CH^2(Z,4)_{\mathbb Q}
=CH^3(Z,4)_{\mathbb Q}=0.} \tag{3.3}
\]

这一证明既不需要 mixed-Tate motive 的 direct-sum splitting，也不需要 Künneth identification 或 singular-variety cohomological spectral sequence。

## 4. Singular boundary 的 indexing 核查

Boundary \(E,D^2\) 可以 singular。此处采用 homological higher-Chow notation \(CH_0(-,4)\)，所以每次 closed/open localization 都保留同一个 dimension index；随后才根据 pure dimensions 转换成 codimension notation。

MVW Properties17.4 的 localization 对任意 scheme/open pair 成立。因为 \(D^3\) 是 smooth disjoint union of one-dimensional \(\mathbb G_m\)，由 (2.2)

\[
CH_0(D^3,4)_{\mathbb Q}=CH^1(D^3,4)_{\mathbb Q}=0.
\]

由 (3.3)，两维 smooth stratum union \(D^{2,*}\) 满足

\[
CH_0(D^{2,*},4)_{\mathbb Q}=CH^2(D^{2,*},4)_{\mathbb Q}=0.
\]

Localization 的 exact segment

\[
CH_0(D^3,4)_{\mathbb Q}\longrightarrow
CH_0(D^2,4)_{\mathbb Q}\longrightarrow
CH_0(D^{2,*},4)_{\mathbb Q}
\]

于是给 \(CH_0(D^2,4)_{\mathbb Q}=0\)。同样，三维 stratum union \(D^{1,*}\) 由 (3.3) 满足 \(CH_0(D^{1,*},4)=CH^3(D^{1,*},4)=0\)，exact segment

\[
CH_0(D^2,4)_{\mathbb Q}\longrightarrow
CH_0(E,4)_{\mathbb Q}\longrightarrow
CH_0(D^{1,*},4)_{\mathbb Q}
\]

给 \(CH_0(E,4)=CH^3(E,4)=0\)。没有把 smooth-variety pullback 或 purity theorem 错用于 singular \(E\)；这里只用一般 localization 和实际 pure dimensions。

最后，\(E\subset Y\) pure codimension one，故 exact segment

\[
CH^3(E,4)_{\mathbb Q}\longrightarrow CH^4(Y,4)_{\mathbb Q}
\longrightarrow CH^4(Y^*,4)_{\mathbb Q}
\]

证明 (1.2)。结合已有 existence，coordinate symbol 有且仅有一个 family completion class。

## 5. 适用边界

* 本结论是 \(CH^4(Y,4)_{\mathbb Q}\) 中 class 的唯一性。不同 admissible cycle representatives 仍可相差 Bloch boundaries；不能称 cycle representative 唯一。
* 因 regulator 是 Chow-class homomorphism，同一唯一 class 的 regulator **cohomology class** 确定。但具体 current representative、Betti lift、closed-chain marking、Tate normalization 与旧 Stieltjes period 的 equality 未在这里证明。
* 本稿不自动声称 arbitrary individual fibres 上的 completion 唯一。那需要逐一检查 base field、fibre boundary filtration 和相应 groups，特别不能把 \(\mathbb Q(x)\) 当成 totally real number field。
* Split rational-point 条件有实质作用。例如 \(A=\mathbb P^1_{\mathbb Q}\setminus\operatorname{Spec}\mathbb Q(i)\) 的 localization 给 \(CH^3(A,4)_{\mathbb Q}\simeq CH^2(\mathbb Q(i),3)_{\mathbb Q}\simeq\mathbb Q\)：两侧 projective-line groups 分别来自 rational \(K_4\)、\(K_3\)，均为零。故 (3.3) 不适用于 arbitrary open rational curves with non-rational removed points。
* 本稿未处理 integral torsion，也未产生新的数值无理性定理。

## 6. 实际 primary 阅读范围

1. Doran–Kerr, *Algebraic K-theory of toric hypersurfaces*, [本地 published primary](../literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf)：实际读 PDF25–29（printed421–425），核对 Adams decomposition、number-field even-\(K\) vanishing、totally-real \(CH^2(k,3)\)、singular boundary localization 和 codimension filtration。
2. Mazza–Voevodsky–Weibel, *Lecture Notes on Motivic Cohomology*, [本地 Clay primary](../literature/mazza_voevodsky_weibel2006_motivic_cohomology_clay_20261006.pdf)：实际读 PDF40–42（printed25–27）、PDF151（printed136）、PDF174,176–178（printed159,161–163），核对 weight-one groups、一般 localization、motivic/higher-Chow comparison。
3. Levine, *Bloch's higher Chow groups revisited*, [本地 Astérisque primary](../literature/levine1994_higher_chow_revisited_20261006.pdf)：实际读 PDF84–85（printed317–318），核对 smooth quasi-projective projective-bundle formula。

全部证据为纸面推导和 primary 阅读。无 mathematical producer、数值搜索、Lean certificate 或 broader geometry audit claim。

## 7. 对 NEW 主证明 U1–U14 的逐项独审

在完成上述独立推导后，实际全文读取 NEW `cdt_odd_R0_toric_completion_uniqueness_20261006.md`，并核对其内容 SHA256 为

`b6baab390cd23c15b1edc717e11a3b97c42dfc4f5c16a8c87c10fe74676f66a2`。

* U1–U2：boundary component types、pure dimensions 和所称 family-class injectivity 范围与本文 §1 一致。
* U3–U8：三个 base groups、weight-one vanishing、projective-bundle formula、localization 的 \(q-1\) 索引和归纳顺序均正确；没有需要额外 conjecture 的 product splitting。
* U9–U12：对于 singular \(E,D^2\)，全文保留 \(CH_0(-,4)\) dimension index；依 pure dimensions 换回 codimension index。逐层 exactness 推导合法。
* U13–U14：generic graph-symbol restriction 到 \(K_4^M(\mathbb Q(v_0,v_1,v_2,v_3))\) 后，沿 \(v_j=0\) 逐个 tame residue 到 \(\pm1\in K_0^M(\mathbb Q)=\mathbb Z\)。各次剩余变量确为 units，故 rationalized terminal image 非零。这证明原 \(\xi\) 及其 completion \(\Xi\) class 非零，未假设 generic restriction injective。
* 这些 \(v_j=0\) valuations 属于 \(\lambda=\infty\) 的 vertical directions，位于 \(Y=f^{-1}(\mathbb G_m)\) 以外。与实际 surviving horizontal divisor 上 \(\{-1\}\) 因子令 \(d_1\xi=0\) 的陈述无冲突。
* 主稿明确仅声称 rational family Chow class 非零且唯一，保留 individual-fibre、regulator-current、integral marking 和数值无理性的缺口。这些范围限制正确。

独审结论：在 toric 稿 §4 的实际 global split-strata 输入下，NEW 主证明 U1–U14 的 group vanishing、unique completion 和 class nonvanishing 推导通过。本文没有把这一审查扩大成对 toroidal resolution 几何、specific regulator identity 或数值 goal 的证明。
