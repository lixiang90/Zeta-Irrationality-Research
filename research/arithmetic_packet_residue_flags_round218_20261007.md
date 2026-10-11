# Genuine source packets: residue flags, local indices, and a one-layer ceiling

2026-10-07, round218. NEW paper derivation. This note supplies an exact local-lattice interface for a different carrier strategy: start with a genuine connection/source packet, then pay its successive residue ranks. It does not construct such a packet for a new numerical zeta/L target. The elementary lattice statements are not claimed novel in the literature.

## 1. Source scope and the change of proof object

The selected new author manuscript is Christopher D. Long, *Hybrid arithmetic holonomy and twenty-two individual p-adic zeta values*, repository snapshot b46a1770901551961710e155d775aae7c5ea39e7. Root actually read its TEX lines1185–1536: the Hasse degree lemma, genuine-source rank–nullity theorem, deepest-row decomposition, small-prime lattices and their index calculation. The global source/BGG/descent bridges, large-prime Cartier theorem, analytic continuation and claimed numerical theorems have not been independently audited. No claimed p-adic irrationality theorem is used here. The files and reading limitations are recorded in [the source scope](../literature/cdt_hasse_joint_gate_sources_20261007/reading_scope.md).

Root also actually read CDT's archived 218-page *The linear independence of 1, ζ(2), and L(2,χ−3)*, PDF pp193–195, §15.2 through the special-value argument, and the corresponding selected public text. Local freeness of the entire arithmetic analytic module is posed there as an additional effective question; knowing one differential module's rational rank does not supply it. A regular-point mechanism in that section cannot directly settle the singular-endpoint values Li_s(1)=ζ(s).

The transferable calculation below is proved independently from explicit hypotheses. It distinguishes a full source module from freely chosen scalar coordinates, and a mod-prime kernel from a compatible higher-power lattice. In particular none of the fixed Jacobi carrier's old prime windows or actual rank statements is transferred to a new source.

## 2. Exact residue-flag formula on one finite jet evaluation

Fix a prime ℓ. Let L be a free Z_ℓ-module of rank n, let Y=Z_ℓ^q, and let E:L→Q_ℓ^q be the actual finite jet evaluation. Assume T=ℓ^e E maps L to Y for an integer e≥0. Define

\[
L_k=\{v\in L:T(v)\in\ell^kY\},\qquad 0\le k\le e.
\tag{R1}
\]

Thus L_0=L, ℓ^kL⊂L_k, and L_e is precisely the sublattice of the original source whose evaluated jets are integral. Each L_k is a finite-index free lattice. Define

\[
\delta_k:L_k/\ell L_k\longrightarrow Y/\ell Y,
\qquad v\longmapsto\ell^{-k}T(v)\bmod\ell,
\qquad \rho_k=\operatorname{rank}\delta_k.
\tag{R2}
\]

This map is well-defined and its lifted kernel is L_{k+1}. Consequently

\[
\boxed{v_\ell[L:L_e]=\sum_{k=0}^{e-1}\rho_k.}
\tag{R3}
\]

Here v_ℓ of the finite index means its exponent. For e=0 the sum and index exponent are zero. To check all powers at once, take Smith invariants t_i≥0 of T, with t_i=∞ for zero invariant factors and with n source factors in all. The basis of L_k is ℓ^{max(0,k−t_i)}v_i for finite t_i, with unscaled zero directions. Therefore

\[
\rho_k=\#\{i:t_i\le k\},\qquad
v_\ell[L:L_e]=\sum_i\max(0,e-t_i).
\tag{R4}
\]

No injectivity or full finite-jet rank is needed. This is an exact formula for the fixed original source and the selected jet cutoff, not for arbitrary rational changes of frame or for all higher jets.

For a rational n×n numerical evaluation matrix E, if a basis matrix B of L_e has E B integral, then v_ℓ(det E)≥−v_ℓ(det B)=−v_ℓ[L:L_e], conditional on det E≠0. A rectangular output permits this argument on each n-row output minor. Rationality of the numerical evaluation, and the same source/row normalization, must be paid before using a product formula. The jet statement alone provides neither.

## 3. What one residue kernel actually buys

Suppose a κ-dimensional subspace K̄⊂L/ℓL satisfies T(K̄)=0 modulo ℓ. Then ρ_0≤n−κ while every ρ_k≤n, so

\[
v_\ell[L:L_e]\le en-\kappa\qquad(e\ge1).
\tag{R5}
\]

This is a determinant-level improvement even when no scalar row divisor exists. Choose a lifted basis whose first κ vectors span a saturated direct summand K; T(K)⊂ℓY. The lattice ℓ^{e−1}K⊕ℓ^eK^c has integral E-evaluation and index exponent en−κ. Thus R5 can be used without computing the full Smith form.

A one-layer rank relation supplies no larger saving by itself. The explicit matrix T=diag(ℓI_κ,I_{n−κ}) has exactly that mod-ℓ kernel and Smith valuations 1 on K, 0 otherwise; its integral-evaluation index is exactly en−κ for every e≥1. Any extra saving requires evidence at a subsequent source lattice L_k, or a genuinely higher-power identity. Applying the same mod-ℓ claim repeatedly to an unchanged basis is invalid.

For example e=1 and ρ_0≤J gives index exponent≤J. This explains the elementary denominator implication of a complete large-prime residue-rank packet. It does not prove the actual packet rank, unit residue or determinant nonzero.

## 4. A conditional genuine-source algebraization criterion

Let D grow, fix ξ>0, and let L_D^+ be a free genuine positive source of rank n_D=rD+O(1), with fixed integer r≥2. Assume the following at every good ℓ in the chosen range, uniformly in D and ℓ.

* The multiplier of the unique deepest row is an integral linear function of the actual source,
  q_λ(x,z)=Σ_{j=0}^{r−1}Q_{j,λ}(x)z^j, with a fixed denominator g(x), g(0) an ℓ-adic unit, and deg(gQ_{j,λ})≤D+C_0.
* On the actual splitting the comparison z_σ(x) is in Z_ℓ[[x]], and its reduction is a_ℓ(x)/b_ℓ(x), with b_ℓ(0)≠0 and max(deg a_ℓ,deg b_ℓ)≤cℓ+C_1 for a fixed c>0.
* For jets through the actual cutoff N^♯=⌊ξD⌋+C_2, the deepest row is cleared by ℓ^{sa}, a=v_ℓ(lcm(1,…,N^♯)); every other row is cleared by ℓ^{(s−1)a}. Its coefficients and the deepest-row unit are integral on this splitting. Here s≥1 is fixed independently of r. Fixed rational period parameters contribute only to an explicitly excluded finite prime set.

These are assumptions to verify, not conclusions from analytic holonomy. Rational coordinates on a chart must truly describe this source evaluation with the stated integral model; a weight-bearing torsor row cannot simply be called a rational scalar on the base.

Clearing b_ℓ^{r−1}g gives an F_ℓ-linear map on the genuine source into polynomials of degree at most D+(r−1)δ_ℓ+C_0, where δ_ℓ=max(deg a_ℓ,deg b_ℓ). Rank–nullity therefore supplies a subspace with

\[
\kappa_{D,\ell}\ge
(r-1)\max\{0,D-c\ell-C_3\}.
\tag{R6}
\]

For every lift in that subspace, the entire deepest-row multiplier is divisible by ℓ as a formal series: g and b_ℓ have invertible constant terms, so the cleared zero polynomial implies a zero series. Multiplication by ℓ^{sa−1} then clears the deepest row, including its integral period constant. It clears every remaining row because sa−1≥(s−1)a when a≥1. The complement uses ℓ^{sa}. Hence the positive source index has the safe bound

\[
v_\ell[L_D^+:L_{D,\ell}^{\rm good}]
\le sa n_D-\kappa_{D,\ell}\qquad(a\ge1).
\tag{R7}
\]

For a=0, the original source already has integral evaluation under the stated clearing hypotheses; use index exponent zero, without subtracting a kernel dimension. A prime in the bounded cutoff difference between N^♯ and ξD is treated this way when necessary. If no deepest multiplier kernel is proved, R7 reduces to the baseline, regardless of how many basis functions share the same analytic differential module. If several rows have the same maximal depth, all their multipliers must vanish on the chosen source directions; the unique-deepest-row assumption cannot be dropped.

## 5. Summation, ceilings and the unproved later layers

With all preceding uniform hypotheses, a fixed exceptional set with e_ℓ=O_ℓ(log D), and source rank O(D), the small-prime indices have a lattice certificate with

\[
\limsup_{D\to\infty}D^{-2}
\sum_{\ell\le\xi D}\log[L_D^+:L_{D,\ell}^{\rm good}]
\le sr\xi-(r-1)\int_0^\xi(1-cx)_+dx.
\tag{R8}
\]

Proof: Σ_{ℓ≤N^♯}a logℓ=log lcm(1,…,N^♯)=ξD+o(D), n_D=rD+O(1), and partial summation of the weighted prime number theorem gives Σκ logℓ≥(r−1)D²∫_0^ξ(1−cx)_+dx+o(D²). The fixed constants/ceilings cost O(D), the fixed bad primes cost O(D log D), and the O(1) source-rank error costs O(D). The finitely many integers in a fixed-size cutoff difference contribute at worst O(D log D), so replacing unavailable a=0 savings by the integral baseline changes no D² term. R8 pays only the specified small-prime/cutoff part; later coefficient pivots, larger primes, archimedean covolumes and actual nonzero still require proofs.

The conservative gain supplied by this one kernel is bounded by (r−1)ξ on the D² scale. Relative to the baseline srξ it is strictly less than 1/s. This is a ceiling for the guarantee from R6–R8, not a necessary arithmetic cost or an impossibility theorem. In particular simply raising integration depth does not automatically generate a growing fraction of denominator savings from the same first-layer kernel.

The exact replacement for repeated first-layer claims is R3: pay the residue map on each successively modified source L_k. A new construction may lower several ρ_k, and may then beat the single-layer ceiling. To assert this one must verify source lift integrality, all equal-depth rows, finite-jet support and compatibility of the later maps. A congruence for an isolated raw coordinate or an integral numerator on a separate chart is not enough.

## 6. Consequence for the research route

The round217 four-master rank and zero theorem do not give the hypotheses of section4 for the actual Catalan carrier; in particular there is no paid rational comparison coordinate with uniform degree cℓ, actual global source splitting or unique-deepest-row evaluation of that kind. R8 is not substituted into any old Catalan, β(4), ζ(7) or η(7) numerical comparison.

The useful change is to design a new carrier from its full connection/source module and residue flags, with explicit target-period evaluation, instead of selecting large Jacobi supports and subsequently trying to clear their matrices. A candidate is promoted only after its real period identity and at least one complete small-prime kernel are constructed on the same source. Higher-depth targets also need a quantitative mechanism for later flags or a different analytic geometry. CDT §15.2's additional local-finiteness issue remains open here.

This note was proved on paper; mathematical program executions are zero. It adopts no numerical theorem from the new author manuscript, does not run its interval certificate, and does not claim to settle any published conjecture. Independent review is pending.
